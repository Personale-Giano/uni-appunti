# -*- coding: utf-8 -*-
"""videolib: video-spiegazione dai riassunti (Manim + Typst + edge-tts + ffmpeg).

Regole: REGOLE_VIDEO.md (stessa cartella). Guida all'API: README.md.
Un video e' un file Python (il «copione») con una classe che eredita da
ScenaBase: SEGMENTI = [Seg(id, titolo, testo_parlato), ...] e un metodo
seg_<id>(self, s) per ogni segmento con le azioni visive.
Si lancia con:  python fai_video.py copioni/<file>.py [--prova] [--verticale]
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
import re
import shutil
import subprocess
import time
import wave
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from manim import *  # noqa: F401,F403  (il copione fa «from videolib import *»)
from manim import config

# --------------------------------------------------------------------------
# Percorsi
# --------------------------------------------------------------------------
QUI = Path(__file__).resolve().parent                 # agente/_sistema/video
AGENTE = QUI.parent.parent                            # agente
CACHE_AUDIO = QUI / "cache_audio"
MEDIA = QUI / "media"
QA_DIR = QUI / "qa"
USCITA = AGENTE / "video"
FIGURE = AGENTE / "_sistema" / "figure"

# --------------------------------------------------------------------------
# Tema: grafite, 1 accento, colori semantici fissi
# --------------------------------------------------------------------------
SFONDO = "#1c1f26"
PANNELLO = "#262b35"      # riquadri, sfondo del codice
TESTO = "#ece8df"         # bianco sporco
TENUE = "#a3acba"         # testo secondario (contrasto 7:1 sul fondo)
ACCENTO = "#ffc233"       # giallo: il punto d'attenzione, il termine che cambia
VERDE = "#5fd38d"         # vero / passo base / corretto
ROSSO = "#ff7b72"         # errore / falso
AZZURRO = "#6cb6ff"       # ipotesi, dato noto
VIOLA = "#c9a0ff"         # altro ruolo semantico (es. parametri)
ARANCIO = "#ffa657"       # altro ruolo semantico (es. il registro FP)
FONT = "Segoe UI"
MONO = "Consolas"
OPACITA_SFONDO = 0.35     # «il resto» quando si evidenzia

VOCE = "it-IT-GiuseppeMultilingualNeural"   # pause brevi tra le frasi; alternativa: it-IT-DiegoNeural
SR = 48000

FORMATI = {
    "16:9": dict(
        nome="16:9", pw=1920, ph=1080, fw=128 / 9, fh=8.0, fps=30,
        prova=(854, 480, 15),
        # margini della zona sicura in frazione (alto, basso, sinistra, destra)
        sicura=(0.055, 0.07, 0.045, 0.045),
        corpo=5.0, grande=7.0, piccolo=3.8, minimo=3.5, min_formula=4.5,   # % dell'altezza (corpo del font)
        ppm=(120, 170), parole_schermo=12, fermo_max=12.0,
        domanda_entro=10.0, durata=(120, 480),
    ),
    "9:16": dict(
        nome="9:16", pw=1080, ph=1920, fw=9.0, fh=16.0, fps=30,
        prova=(432, 768, 15),
        sicura=(0.15, 0.35, 0.06, 0.18),
        corpo=2.9, grande=4.2, piccolo=2.4, minimo=2.2, min_formula=2.6,
        ppm=(125, 180), parole_schermo=12, fermo_max=8.0,
        domanda_entro=3.5, durata=(55, 95),
    ),
}
F = dict(FORMATI["16:9"])   # formato corrente (lo imposta imposta_formato)

# unita' di scena per punto di font_size (misurate: altezza della x / 0,5 e / 0,43)
_K_TESTO = 0.667 / 48
_K_FORMULA = 0.527 / 48


def imposta_formato(nome="16:9", prova=False, media_dir=None):
    """Imposta Manim (risoluzione, quadro, sfondo) per il formato scelto."""
    F.clear()
    F.update(FORMATI[nome])
    F["prova_attiva"] = bool(prova)
    pw, ph, fps = (F["prova"] if prova else (F["pw"], F["ph"], F["fps"]))
    config.pixel_width, config.pixel_height, config.frame_rate = pw, ph, fps
    config.frame_width, config.frame_height = F["fw"], F["fh"]
    config.background_color = SFONDO
    config.media_dir = str(media_dir or MEDIA)
    config.disable_caching = True
    config.verbosity = "WARNING"
    config.progress_bar = "none"
    a, b, s, d = F["sicura"]
    F["x0"], F["x1"] = -F["fw"] / 2 + s * F["fw"], F["fw"] / 2 - d * F["fw"]
    F["y1"], F["y0"] = F["fh"] / 2 - a * F["fh"], -F["fh"] / 2 + b * F["fh"]
    return F


imposta_formato(os.environ.get("VIDEO_FORMATO", "16:9"), os.environ.get("VIDEO_PROVA") == "1")


def ffmpeg_exe():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


# ==========================================================================
# 1. COPIONE E VOCE
# ==========================================================================
_PAUSA = re.compile(r"\[pausa\s+([\d.,]+)\]")


def _norm(s):
    return re.sub(r"[^0-9a-zàèéìíòóùú]+", " ", s.lower()).split()


@dataclass
class Parola:
    t: float        # inizio (s, dall'inizio del segmento)
    d: float        # durata
    testo: str      # com'e' scritta nel copione, con la punteggiatura
    fine_pezzo: bool = False


class Seg:
    """Un segmento del copione.

    testo: SOLO parlato, gia' normalizzato per la voce («enne piu' uno», mai simboli).
           «[pausa 2.5]» inserisce un silenzio (es. dopo la domanda di verifica).
    velocita: percentuale rispetto alla voce normale (es. -5 sulle formule).
    pausa_dopo: silenzio dopo il segmento (0,8-1,2 s tra segmenti).
    """

    def __init__(self, id, titolo, testo, velocita=None, voce=None, pausa_dopo=0.9):
        self.id, self.titolo = id, titolo
        self.testo = " ".join(testo.split())
        self.velocita, self.voce, self.pausa_dopo = velocita, voce, pausa_dopo
        self.parole: list[Parola] = []
        self.durata = 0.0          # durata dell'audio (pause interne comprese)
        self.durata_voce = 0.0     # senza le pause esplicite
        self.audio = None          # np.int16 mono a SR
        self.t0 = None             # istante di inizio nel video (lo scrive la scena)

    # ---- tempi delle parole ------------------------------------------------
    def _indice(self):
        piatti = []
        for i, p in enumerate(self.parole):
            for tok in _norm(p.testo):
                piatti.append((tok, i))
        return piatti

    def _trova(self, frase, n=1):
        cerca = _norm(frase)
        if not cerca:
            raise ValueError("frase vuota")
        piatti = self._indice()
        toks = [t for t, _ in piatti]
        trovati = [i for i in range(len(toks) - len(cerca) + 1) if toks[i:i + len(cerca)] == cerca]
        if len(trovati) < n:
            raise KeyError(f"segmento «{self.id}»: «{frase}» (occorrenza {n}) non e' nel testo parlato. "
                           f"Occorrenze trovate: {len(trovati)}")
        i = trovati[n - 1]
        return piatti[i][1], piatti[i + len(cerca) - 1][1]

    def quando(self, frase, n=1):
        """Istante (s dall'inizio del segmento) in cui comincia la frase/parola."""
        a, _ = self._trova(frase, n)
        return self.parole[a].t

    def fine_di(self, frase, n=1):
        """Istante in cui finisce la frase/parola."""
        _, b = self._trova(frase, n)
        return self.parole[b].t + self.parole[b].d

    @property
    def n_parole(self):
        return len(_PAUSA.sub(" ", self.testo).split())

    def pezzi(self):
        """[(testo, pausa_dopo_il_pezzo)]"""
        parti = _PAUSA.split(self.testo)
        out = []
        for i in range(0, len(parti), 2):
            t = parti[i].strip()
            pausa = float(parti[i + 1].replace(",", ".")) if i + 1 < len(parti) else 0.0
            if t:
                out.append((t, pausa))
            elif out and pausa:
                out[-1] = (out[-1][0], out[-1][1] + pausa)
        return out


def _chiave(testo, voce, velocita):
    return hashlib.sha1(f"{voce}|{velocita}|{testo}".encode("utf-8")).hexdigest()[:20]


async def _edge(testo, voce, rate):
    import edge_tts
    com = edge_tts.Communicate(testo, voce, rate=rate, boundary="WordBoundary")
    audio, parole = b"", []
    async for ch in com.stream():
        if ch["type"] == "audio":
            audio += ch["data"]
        elif ch["type"] == "WordBoundary":
            parole.append([ch["offset"] / 1e7, ch["duration"] / 1e7, ch["text"]])
    if not audio or not parole:
        raise RuntimeError("edge-tts: risposta vuota")
    return audio, parole


def _mp3_a_pcm(mp3: Path):
    r = subprocess.run([ffmpeg_exe(), "-v", "error", "-i", str(mp3), "-ar", str(SR), "-ac", "1",
                        "-f", "s16le", "-"], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("ffmpeg: " + r.stderr.decode("utf-8", "replace")[:300])
    return np.frombuffer(r.stdout, dtype=np.int16).copy()


def sintetizza_pezzo(testo, voce=VOCE, velocita=0, tentativi=5):
    """Voce per un pezzo di testo, con cache su disco. Ritorna (pcm int16, [[t, d, parola], ...])."""
    CACHE_AUDIO.mkdir(parents=True, exist_ok=True)
    k = _chiave(testo, voce, velocita)
    mp3, js, wav = CACHE_AUDIO / f"{k}.mp3", CACHE_AUDIO / f"{k}.json", CACHE_AUDIO / f"{k}.wav"
    if not (mp3.exists() and js.exists()):
        rate = f"{'+' if velocita >= 0 else '-'}{abs(int(velocita))}%"
        errore = None
        for i in range(tentativi):
            try:
                audio, parole = asyncio.run(_edge(testo, voce, rate))
                break
            except Exception as e:  # rete, servizio non ufficiale: si riprova
                errore = e
                time.sleep(2 * (i + 1))
        else:
            raise RuntimeError(f"Sintesi vocale fallita dopo {tentativi} tentativi ({errore}). "
                               "Serve la rete; i pezzi gia' fatti restano in cache.")
        mp3.write_bytes(audio)
        js.write_text(json.dumps({"testo": testo, "voce": voce, "velocita": velocita, "parole": parole},
                                 ensure_ascii=False, indent=0), encoding="utf-8")
    parole = json.loads(js.read_text(encoding="utf-8"))["parole"]
    if wav.exists():
        with wave.open(str(wav), "rb") as w:
            pcm = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).copy()
    else:
        pcm = _mp3_a_pcm(mp3)
        # coda di silenzio ridotta a 0,12 s: le pause le decide il copione
        forte = np.where(np.abs(pcm) > 250)[0]
        fine = max(int((parole[-1][0] + parole[-1][1]) * SR), int(forte[-1]) if len(forte) else 0)
        pcm = pcm[: min(len(pcm), fine + int(0.12 * SR))]
        scrivi_wav(wav, pcm)
    return pcm, parole


def scrivi_wav(percorso, pcm):
    with wave.open(str(percorso), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(np.asarray(pcm, dtype=np.int16).tobytes())


def sintetizza(segmenti, voce=VOCE, velocita=0, log=print):
    """Riempie parole/durata/audio di ogni segmento (cache per pezzo)."""
    for s in segmenti:
        v = s.voce or voce
        vel = s.velocita if s.velocita is not None else velocita
        blocchi, s.parole, t, s.durata_voce = [], [], 0.0, 0.0
        for testo, pausa in s.pezzi():
            pcm, parole = sintetizza_pezzo(testo, v, vel)
            scritte = testo.split()
            stesso = len(scritte) == len(parole)
            for i, (pt, pd, ptxt) in enumerate(parole):
                s.parole.append(Parola(t + pt, pd, scritte[i] if stesso else ptxt))
            if s.parole:
                s.parole[-1].fine_pezzo = True
            blocchi.append(pcm)
            dur = len(pcm) / SR
            s.durata_voce += dur
            t += dur
            if pausa:
                blocchi.append(np.zeros(int(pausa * SR), dtype=np.int16))
                t += pausa
        s.audio = np.concatenate(blocchi) if blocchi else np.zeros(0, dtype=np.int16)
        s.durata = len(s.audio) / SR
        if log:
            log(f"  voce {s.id:<14} {s.durata:5.1f} s  {s.n_parole:3d} parole  "
                f"{60 * s.n_parole / max(s.durata_voce, 0.1):4.0f} parole/min")
    return segmenti


# ---- controllo del copione -------------------------------------------------
_SIMBOLI = re.compile(r"[=+*/^_{}<>≥≤≠∀∃→⟹⟺∈∉⊆∪∩Σ∑√·×%#|\\]|\d\s*[-−]\s*\d")
_LETTERA = re.compile(r"(?<![\wàèéìòù'’])([b-df-hj-np-zB-DF-HJ-NP-Z])(?![\wàèéìòù'’])")


def frasi_del_testo(testo):
    pulito = _PAUSA.sub(" ", testo)
    return [f.strip() for f in re.split(r"(?<=[.?!])\s+", pulito) if f.strip()]


def controlla_copione(segmenti, formato=None):
    """Controlli 2, 5, 6, 7, 10 della checklist + durata. Ritorna [(gravita, messaggio)]."""
    fm = FORMATI[formato] if formato else F
    out = []
    lo, hi = fm["ppm"]
    tutte = []
    for s in segmenti:
        if s.durata_voce:
            ppm = 60 * s.n_parole / s.durata_voce
            if not lo <= ppm <= hi:
                out.append(("avviso", f"[{s.id}] {ppm:.0f} parole/min (atteso {lo}-{hi}): cambia «velocita» del segmento"))
        for f in frasi_del_testo(s.testo):
            n = len(f.split())
            tutte.append(n)
            if n > 22:
                out.append(("errore", f"[{s.id}] frase di {n} parole (max 22): «{f[:60]}…»"))
        pulito = _PAUSA.sub(" ", s.testo)
        m = _SIMBOLI.search(pulito)
        if m:
            out.append(("errore", f"[{s.id}] simbolo non normalizzato nel parlato: «{pulito[max(0, m.start() - 15):m.end() + 15]}»"))
        m = _LETTERA.search(pulito)
        if m:
            out.append(("errore", f"[{s.id}] lettera isolata «{m.group(1)}»: scrivila come si pronuncia (enne, kappa, esse…)"))
    if tutte:
        media = sum(tutte) / len(tutte)
        if media > 16:
            out.append(("avviso", f"frasi lunghe in media {media:.1f} parole (obiettivo 12-15)"))
    # domanda iniziale
    if segmenti and segmenti[0].parole:
        t_dom = next((p.t + p.d for p in segmenti[0].parole if p.testo.endswith("?")), None)
        if t_dom is None or t_dom > fm["domanda_entro"] + 2.5:
            out.append(("errore", f"nessuna domanda entro i primi {fm['domanda_entro']:.0f} s (aggancio)"))
    # domanda di verifica finale con pausa >= 2 s e risposta
    ok = False
    for s in segmenti[-2:]:
        for m in re.finditer(r"\?\s*\[pausa\s+([\d.,]+)\]\s*\S", s.testo):
            if float(m.group(1).replace(",", ".")) >= 2:
                ok = True
    if not ok:
        out.append(("errore", "manca la domanda di verifica finale: «…? [pausa 2.5] risposta» negli ultimi due segmenti"))
    tot = sum(s.durata + s.pausa_dopo for s in segmenti)
    if tot and not fm["durata"][0] <= tot <= fm["durata"][1]:
        out.append(("avviso" if tot < fm["durata"][1] else "errore",
                    f"durata prevista {tot:.0f} s fuori da {fm['durata'][0]}-{fm['durata'][1]} s"))
    return out


# ==========================================================================
# 2. OGGETTI DI SCENA (testi, formule, codice, caselle, pila)
# ==========================================================================
def _marca(m, tipo, parole=0, pct=None, conta=True):
    m.vl = dict(tipo=tipo, parole=parole, pct0=pct, h0=max(m.height, 1e-6), conta=conta)
    return m


def testo(s, pct=None, colore=TESTO, peso=NORMAL, font=FONT, tipo="testo", conta=True, **kw):
    """Testo non matematico. pct = corpo del font in % dell'altezza del quadro."""
    pct = pct or F["corpo"]
    fs = pct / 100 * F["fh"] / _K_TESTO
    m = Text(s, font=font, font_size=fs, color=colore, weight=peso, **kw)
    return _marca(m, tipo, parole=len(s.split()), pct=pct, conta=conta)


def etichetta(s, pct=None, colore=TESTO, peso=NORMAL, font=FONT):
    """Etichetta attaccata a un oggetto (non conta nel limite delle 12 parole)."""
    return testo(s, pct or F["piccolo"], colore, peso, font, tipo="etichetta", conta=False)


def col(espr, colore):
    """Dentro una formula Typst: colora una parte.  formula(f"S_n + {col('(n+1)', ACCENTO)}")"""
    return f'#text(fill: rgb("{colore}"))[${espr}$]'


def formula(typst, pct=None, colore=TESTO):
    """Formula in sintassi Typst (niente LaTeX): formula(r"sum_(i=1)^n i = (n(n+1))/2")."""
    pct = pct or F["grande"]
    fs = pct / 100 * F["fh"] / _K_FORMULA
    m = MathTypst(typst, font_size=fs, color=colore)
    return _marca(m, "formula", pct=pct)


def adatta(m, larg=None, alt=None):
    """Riduce m (mai ingrandisce) perche' stia in larg x alt (unita' di scena)."""
    k = 1.0
    if larg and m.width > larg:
        k = min(k, larg / m.width)
    if alt and m.height > alt:
        k = min(k, alt / m.height)
    if k < 1:
        m.scale(k)
    return m


def riquadro(m, colore=TENUE, margine=0.22, riempi=PANNELLO, spessore=2):
    r = RoundedRectangle(corner_radius=0.12, width=m.width + 2 * margine, height=m.height + 2 * margine,
                         stroke_color=colore, stroke_width=spessore, fill_color=riempi, fill_opacity=0.9)
    r.move_to(m)
    return r


class Codice(VGroup):
    """Codice C con numeri di riga e barra sulla riga corrente.

    c = Codice(sorgente, pct=3.8);  self.play(c.riga(3))  -> sposta la barra sulla riga 3 (da 1).
    """

    def __init__(self, sorgente, pct=None, linguaggio="c", larg=None):
        super().__init__()
        pct = pct or (4.3 if F["nome"] == "16:9" else F["piccolo"])
        fs = pct / 100 * F["fh"] / _K_TESTO
        self.sorgente = sorgente.strip("\n")
        self.blocco = Code(code_string=self.sorgente, language=linguaggio, formatter_style="monokai",
                           background="rectangle",
                           background_config=dict(fill_color=PANNELLO, stroke_color=TENUE, stroke_width=1,
                                                  corner_radius=0.12, buff=0.25),
                           paragraph_config=dict(font=MONO, font_size=fs, line_spacing=0.6))
        self.add(self.blocco)
        if larg:
            adatta(self, larg=larg)
        self.n_righe = len(self.sorgente.split("\n"))
        self.barra = None
        self.riga_corrente = None
        _marca(self, "codice", pct=pct)

    def _numeri(self):
        return self.blocco.submobjects[1]

    def y_riga(self, n):
        num = self._numeri()
        return num[n - 1].get_center()[1]

    def _nuova_barra(self, n, colore):
        sf = self.blocco.submobjects[0]
        passo = abs(self.y_riga(1) - self.y_riga(2)) if self.n_righe > 1 else self._numeri()[0].height * 1.6
        b = RoundedRectangle(corner_radius=0.06, width=sf.width - 0.12, height=passo * 0.98,
                             stroke_color=colore, stroke_width=2, fill_color=colore, fill_opacity=0.16)
        b.move_to([sf.get_center()[0], self.y_riga(n), 0])
        return b

    def riga(self, n, colore=ACCENTO):
        """Animazione: evidenzia la riga n (la prima e' 1)."""
        self.riga_corrente = n
        if self.barra is None:
            self.barra = self._nuova_barra(n, colore)
            self.add(self.barra)
            return FadeIn(self.barra, run_time=0.3)
        return self.barra.animate.move_to([self.barra.get_center()[0], self.y_riga(n), 0])

    def togli_barra(self):
        b, self.barra = self.barra, None
        self.remove(b)
        return FadeOut(b, run_time=0.3)


class TabellaTraccia(VGroup):
    """Tabella di traccia: una colonna per variabile, una riga per passo.

    t = TabellaTraccia(["i", "s"]);  self.play(t.passo(1, 1));  self.play(t.passo(2, 3))
    """

    def __init__(self, colonne, pct=None, larg_col=1.3, righe_max=7):
        super().__init__()
        self.pct = pct or F["piccolo"]
        self.colonne, self.larg_col, self.righe_max = list(colonne), larg_col, righe_max
        self.h = self.pct / 100 * F["fh"] * 1.75
        self.righe = []
        testa = VGroup()
        for j, c in enumerate(self.colonne):
            t = etichetta(c, self.pct, ACCENTO, BOLD, MONO)
            t.move_to([j * larg_col, 0, 0])
            testa.add(t)
        linea = Line([-larg_col / 2, -self.h / 2, 0], [(len(colonne) - 0.5) * larg_col, -self.h / 2, 0],
                     stroke_color=TENUE, stroke_width=2)
        self.testa = testa
        self.add(testa, linea)

    def passo(self, *valori, colore=TESTO):
        """Animazione: aggiunge una riga (None o "" = cella vuota); la riga prima si attenua."""
        if len(self.righe) >= self.righe_max:
            raise ValueError("TabellaTraccia: troppe righe, usa input piu' piccoli")
        riga = VGroup()
        y = self.testa.get_center()[1] - self.h * (len(self.righe) + 1) * self.get_scale_y()
        for j, v in enumerate(valori):
            if v is None or v == "":
                continue
            t = etichetta(str(v), self.pct, colore, NORMAL, MONO)
            t.scale(self.get_scale_y())
            t.move_to([self.testa[j].get_center()[0], y, 0])
            riga.add(t)
        anim = [FadeIn(riga, shift=DOWN * 0.15)]
        if self.righe:
            anim.append(self.righe[-1].animate.set_opacity(0.55))
        self.righe.append(riga)
        self.add(riga)
        return AnimationGroup(*anim, run_time=0.4)

    def get_scale_y(self):
        return self.testa[0].height / self.testa[0].vl["h0"]


class Caselle(VGroup):
    """Array / celle di memoria in fila, con indici sotto e frecce-puntatore.

    a = Caselle([3, 1, 4, 1], nome="a");  self.play(a.imposta(2, 9));  f = a.freccia(0, "i")
    self.play(Create(f));  self.play(a.sposta(f, 1))
    """

    def __init__(self, valori, nome=None, indici=True, lato=None, pct=None, colore=AZZURRO):
        super().__init__()
        self.pct = pct or F["corpo"]
        self.lato = lato or self.pct / 100 * F["fh"] * 2.2
        self.colore = colore
        self.celle, self.valori, self.idx = VGroup(), [], VGroup()
        for i, v in enumerate(valori):
            q = Square(self.lato, stroke_color=colore, stroke_width=3, fill_color=colore, fill_opacity=0.12)
            q.move_to([i * self.lato, 0, 0])
            self.celle.add(q)
            t = etichetta(str(v), self.pct, TESTO, NORMAL, MONO).move_to(q)
            self.valori.append(t)
            if indici:
                k = etichetta(str(i), F["piccolo"], TENUE, NORMAL, MONO).next_to(q, DOWN, buff=0.12)
                self.idx.add(k)
        self.add(self.celle, VGroup(*self.valori), self.idx)
        if nome:
            self.nome = etichetta(nome, self.pct, colore, BOLD, MONO).next_to(self.celle, LEFT, buff=0.3)
            self.add(self.nome)
        self.center()

    def cella(self, i):
        return self.celle[i]

    def imposta(self, i, v, colore=ACCENTO):
        """Animazione: scrive v nella casella i."""
        nuovo = etichetta(str(v), self.pct, colore, NORMAL, MONO)
        nuovo.scale(self.celle[i].width / self.lato).move_to(self.celle[i])
        vecchio = self.valori[i]
        self.valori[i] = nuovo
        self.submobjects[1].remove(vecchio)
        self.submobjects[1].add(nuovo)
        return AnimationGroup(FadeOut(vecchio, shift=UP * 0.2), FadeIn(nuovo, shift=UP * 0.2), run_time=0.4)

    def freccia(self, i, nome, colore=ACCENTO, sopra=True):
        """Freccia con etichetta che punta la casella i (da aggiungere con Create/FadeIn)."""
        q = self.celle[i]
        d = UP if sopra else DOWN
        buff = 0.1 if sopra or not len(self.idx) else 0.25 + self.idx[0].height
        punta = q.get_edge_center(d) + d * buff
        fr = Arrow(punta + d * 0.75, punta, buff=0, stroke_width=5, color=colore, max_tip_length_to_length_ratio=0.3)
        et = etichetta(nome, F["piccolo"], colore, BOLD, MONO).next_to(fr, d, buff=0.08)
        g = VGroup(fr, et)
        g.sopra = sopra
        return g

    def sposta(self, freccia, i):
        """Animazione: la freccia va sulla casella i."""
        return freccia.animate.set_x(self.celle[i].get_center()[0])


class Pila(VGroup):
    """Stack disegnato come pila di caselle che cresce verso il basso (indirizzi decrescenti).

    p = Pila(larg=3.4, posti=8)
    self.play(p.push("main", colore=AZZURRO, alt=2))       # un frame alto due posti
    self.play(p.push("x", 2))                               # casella «x = 2»
    fp = p.puntatore("FP", ROSSO, lato=LEFT, livello=0)     # livello = confine: 0 in cima, k sotto la k-esima casella
    self.play(FadeIn(fp));  self.play(p.sposta("FP", 1));  self.play(p.pop())
    """

    def __init__(self, larg=3.4, posti=8, alt_posto=None, pct=None, titolo=None):
        super().__init__()
        self.pct = pct or F["piccolo"]
        self.larg, self.posti = larg, posti
        self.hp = alt_posto or self.pct / 100 * F["fh"] * 2.0
        self.guida = Rectangle(width=larg, height=self.hp * posti, stroke_color=TENUE, stroke_width=1.5,
                               stroke_opacity=0.6, fill_color=PANNELLO, fill_opacity=0.5)
        self.add(self.guida)
        self.celle = []          # dict(nome, box, testo, alt, colore, gruppo)
        self.punt = {}
        self.gr_celle = VGroup()
        self.add(self.gr_celle)
        if titolo:
            self.titolo = etichetta(titolo, self.pct, TENUE).next_to(self.guida, UP, buff=0.15)
            self.add(self.titolo)

    # geometria ------------------------------------------------------------
    def _k(self):
        return self.guida.height / (self.hp * self.posti)

    def occupati(self):
        return sum(c["alt"] for c in self.celle)

    def y_livello(self, livello):
        """y del confine: 0 = cima della pila, k = sotto la k-esima casella."""
        posti = sum(c["alt"] for c in self.celle[:livello])
        return self.guida.get_top()[1] - posti * self.hp * self._k()

    def livello_sotto(self, nome):
        return self._i(nome) + 1

    def livello_sopra(self, nome):
        return self._i(nome)

    def _i(self, nome):
        for i in range(len(self.celle) - 1, -1, -1):
            if self.celle[i]["nome"] == nome:
                return i
        raise KeyError(f"Pila: nessuna casella «{nome}»")

    def cella(self, nome):
        return self.celle[self._i(nome)]["gruppo"]

    def _scritta(self, nome, valore, colore_testo=TESTO, peso=NORMAL):
        s = nome if valore is None else f"{nome} = {valore}"
        t = etichetta(s, self.pct, colore_testo, peso, MONO)
        t.scale(self._k())
        return t

    # operazioni -----------------------------------------------------------
    def push(self, nome, valore=None, colore=AZZURRO, alt=1, peso=NORMAL, mostra=None):
        """Animazione: impila una casella (alt = quanti posti occupa). mostra = scritta diversa dal nome."""
        if self.occupati() + alt > self.posti:
            raise ValueError("Pila piena: aumenta «posti»")
        k = self._k()
        y_top = self.y_livello(len(self.celle))
        box = Rectangle(width=self.guida.width, height=alt * self.hp * k, stroke_color=colore, stroke_width=3,
                        fill_color=colore, fill_opacity=0.28)
        box.move_to([self.guida.get_center()[0], y_top - alt * self.hp * k / 2, 0])
        t = self._scritta(mostra or nome, valore, peso=peso).move_to(box)
        g = VGroup(box, t)
        self.celle.append(dict(nome=nome, mostra=mostra or nome, box=box, testo=t, alt=alt, colore=colore, gruppo=g))
        self.gr_celle.add(g)
        return FadeIn(g, shift=DOWN * 0.25, run_time=0.5)

    def pop(self, n=1):
        """Animazione: toglie le ultime n caselle."""
        tolte = [self.celle.pop() for _ in range(n)]
        gruppi = [c["gruppo"] for c in tolte]
        for g in gruppi:
            self.gr_celle.remove(g)
        return AnimationGroup(*[FadeOut(g, shift=UP * 0.25) for g in gruppi], run_time=0.5)

    def imposta(self, nome, valore, colore=ACCENTO):
        """Animazione: cambia il valore scritto nella casella."""
        c = self.celle[self._i(nome)]
        nuovo = self._scritta(c["mostra"], valore, colore).move_to(c["box"])
        vecchio = c["testo"]
        c["gruppo"].remove(vecchio)
        c["gruppo"].add(nuovo)
        c["testo"] = nuovo
        return AnimationGroup(FadeOut(vecchio), FadeIn(nuovo), run_time=0.4)

    def attiva(self, *nomi):
        """Animazione: le caselle indicate piene (frame attivo), le altre attenuate (sospese)."""
        an = []
        for c in self.celle:
            on = c["nome"] in nomi
            an.append(c["box"].animate.set_fill(opacity=0.5 if on else 0.12))
            an.append(c["testo"].animate.set_opacity(1.0 if on else 0.6))
        return AnimationGroup(*an, run_time=0.4)

    def puntatore(self, nome, colore=ACCENTO, lato=LEFT, livello=None, lung=0.85):
        """Crea la freccia «nome» sul confine indicato (default: fondo della pila). Poi FadeIn(...)."""
        livello = len(self.celle) if livello is None else livello
        x = self.guida.get_left()[0] if lato is LEFT else self.guida.get_right()[0]
        d = -1 if lato is LEFT else 1
        y = self.y_livello(livello)
        fr = Arrow([x + d * lung, y, 0], [x + d * 0.05, y, 0], buff=0, stroke_width=5, color=colore,
                   max_tip_length_to_length_ratio=0.3)
        et = etichetta(nome, self.pct, colore, BOLD, MONO).next_to(fr, RIGHT * d, buff=0.1)
        g = VGroup(fr, et)
        self.punt[nome] = g
        self.add(g)
        return g

    def sposta(self, nome, livello=None):
        """Animazione: la freccia «nome» va sul confine indicato (default: fondo della pila)."""
        livello = len(self.celle) if livello is None else livello
        g = self.punt[nome]
        dy = self.y_livello(livello) - g[0].get_center()[1]
        return g.animate.shift(UP * dy)


# ==========================================================================
# 3. SCENA BASE
# ==========================================================================
class ScenaBase(Scene):
    """Classe base dei video. Nel copione:

        class Video(ScenaBase):
            META = dict(materia="fondamenti", slug="induzione", titolo="…", formato="16:9")
            SEGMENTI = [Seg("aggancio", "La domanda", "Come fai a …?"), ...]
            def seg_aggancio(self, s):
                f = self.formula("1+2+3"); self.alla("somma", Write(f))
    """

    META: dict = {}
    SEGMENTI: list = []

    # ---- ciclo -----------------------------------------------------------
    def construct(self):
        self.camera.background_color = SFONDO
        self.qa = []                 # (gravita, seg, t, messaggio)
        self.cronologia = []         # dict(id, t0, durata)
        self._seg = None
        self._t_cambio = 0.0
        self._titolo = None
        self._enunciato = None
        self._fissi = []
        self._attenuati = []
        self._n_foto = {}
        self.cartella_qa = Path(getattr(self, "cartella_qa", QA_DIR / "_senza_nome"))
        self.cartella_qa.mkdir(parents=True, exist_ok=True)
        solo = getattr(self, "solo_segmenti", None)
        for i, s in enumerate(self.SEGMENTI):
            if solo and s.id not in solo:
                continue
            self._inizia(s)
            getattr(self, "seg_" + s.id)(s)
            self._chiudi(s, i)

    def _inizia(self, s):
        self._seg = s
        s.t0 = self.time
        self.cronologia.append(dict(id=s.id, t0=s.t0, durata=s.durata))
        if s.titolo:
            self.titolo_segmento(s.titolo)

    def _chiudi(self, s, i):
        self.fino_a(s.durata, _fine=True)
        self._controlla_schermo()
        self.foto(f"{i + 1:02d}_{s.id}")
        if s.pausa_dopo:
            self.wait(s.pausa_dopo)

    # ---- tempo -----------------------------------------------------------
    def ora(self):
        """Secondi dall'inizio del segmento corrente."""
        return self.time - self._seg.t0

    def fino_a(self, t, anticipo=0.0, n=1, _fine=False):
        """Aspetta fino a t secondi dall'inizio del segmento (o fino alla parola/frase t)."""
        nome = t if isinstance(t, str) else None
        if nome is not None:
            t = self._seg.quando(nome, n)
        dt = t - anticipo - self.ora()
        if dt > 1.0 / config.frame_rate:
            self.wait(dt)
        elif dt < -0.3 and not _fine:
            self._nota("avviso", f"animazione in ritardo di {-dt:.1f} s su «{nome or f'{t:.1f} s'}»: "
                                 "accorcia le animazioni prima o sposta l'aggancio")
        elif dt < -0.3 and _fine:
            self._nota("avviso", f"le animazioni finiscono {-dt:.1f} s dopo la voce")

    def alla(self, frase, *animazioni, n=1, anticipo=0.15, **kw):
        """Aspetta la parola/frase e fa partire le animazioni (entro ±0,3 s)."""
        self.fino_a(frase, anticipo=anticipo, n=n)
        if animazioni:
            kw.setdefault("run_time", 0.6)
            self.play(*animazioni, **kw)

    def play(self, *args, **kw):
        attesa = bool(args) and all(isinstance(a, Wait) for a in args)
        if not attesa and self._seg is not None:
            fermo = self.time - self._t_cambio
            if fermo > F["fermo_max"]:
                self._nota("avviso", f"schermo fermo per {fermo:.1f} s (max {F['fermo_max']:.0f})")
        super().play(*args, **kw)
        if not attesa:
            self._t_cambio = self.time
            if self._seg is not None:
                self._controlla_schermo()

    # ---- zone ------------------------------------------------------------
    @property
    def alt_testata(self):
        return F["piccolo"] / 100 * F["fh"] * (2.0 if F["nome"] == "16:9" else 2.2)

    def area(self):
        """Zona del contenuto (sotto la testata, dentro la zona sicura): (x0, x1, y0, y1)."""
        testata = self.alt_testata
        if self._enunciato is not None and F["nome"] == "16:9":
            testata = max(testata, self._enunciato.height)
        elif self._enunciato is not None:
            testata += self._enunciato.height + 0.1
        return F["x0"], F["x1"], F["y0"], F["y1"] - testata - 0.15

    def punto(self, fx=0.5, fy=0.5):
        """Punto dell'area di contenuto in frazioni: (0,0) in basso a sinistra, (1,1) in alto a destra."""
        x0, x1, y0, y1 = self.area()
        return np.array([x0 + fx * (x1 - x0), y0 + fy * (y1 - y0), 0.0])

    @property
    def larg(self):
        x0, x1, _, _ = self.area()
        return x1 - x0

    @property
    def alt(self):
        _, _, y0, y1 = self.area()
        return y1 - y0

    def poni(self, m, fx=0.5, fy=0.5, larg=None, alt=None):
        """Mette m nel punto (fx, fy) dell'area; larg/alt (frazioni dell'area) = ingombro massimo."""
        adatta(m, self.larg * (larg or 1.0), self.alt * (alt or 1.0))
        m.move_to(self.punto(fx, fy))
        return m

    # ---- fabbriche (stesse funzioni del modulo) ---------------------------
    testo = staticmethod(testo)
    etichetta = staticmethod(etichetta)
    formula = staticmethod(formula)

    def codice(self, sorgente, pct=None, larg=None):
        return Codice(sorgente, pct, larg=self.larg * larg if larg else None)

    def figura(self, percorso, larg=0.6, alt=0.9):
        """Figura PNG/SVG dei riassunti (percorso assoluto o relativo a _sistema/figure)."""
        p = Path(percorso)
        if not p.is_absolute():
            p = FIGURE / p
        m = SVGMobject(str(p)) if p.suffix.lower() == ".svg" else ImageMobject(str(p))
        k = min(self.larg * larg / m.width, self.alt * alt / m.height)
        m.scale(k)
        m.vl = dict(tipo="figura", parole=0, pct0=None, h0=m.height, conta=False)
        return m

    # ---- testata ----------------------------------------------------------
    def titolo_segmento(self, s):
        """Titolo del segmento, piccolo, in alto a sinistra (sostituisce il precedente)."""
        barra = Rectangle(width=0.09, height=F["piccolo"] / 100 * F["fh"] * 1.1, fill_color=ACCENTO,
                          fill_opacity=1, stroke_width=0)
        t = testo(s, F["piccolo"], TENUE, tipo="etichetta", conta=False)
        g = VGroup(barra, t).arrange(RIGHT, buff=0.18)
        g.move_to([F["x0"] + g.width / 2, F["y1"] - self.alt_testata / 2, 0])
        vecchio = self._titolo
        self._titolo = g
        if vecchio is not None:
            self.play(FadeOut(vecchio), FadeIn(g), run_time=0.3)
        else:
            self.play(FadeIn(g), run_time=0.3)

    def enunciato(self, m, anima=True):
        """Enunciato fisso in alto (a destra in 16:9, sotto il titolo in 9:16). m = formula o testo."""
        if isinstance(m, str):
            m = formula(m, F["corpo"])
        if F["nome"] == "16:9":
            adatta(m, larg=(F["x1"] - F["x0"]) * 0.55)
            m.move_to([F["x1"] - m.width / 2, F["y1"] - m.height / 2, 0])
        else:
            adatta(m, larg=(F["x1"] - F["x0"]))
            m.move_to([(F["x0"] + F["x1"]) / 2, F["y1"] - self.alt_testata - m.height / 2 - 0.1, 0])
        vecchio = self._enunciato
        self._enunciato = m
        if anima:
            if vecchio is not None:
                self.play(FadeOut(vecchio), FadeIn(m), run_time=0.4)
            else:
                self.play(FadeIn(m), run_time=0.4)
        return m

    def togli_enunciato(self):
        if self._enunciato is not None:
            self.play(FadeOut(self._enunciato), run_time=0.3)
            self._enunciato = None

    def fissa(self, *mobs):
        """Oggetti che pulisci() non deve togliere."""
        self._fissi.extend(mobs)

    def pulisci(self, *tieni, run_time=0.4):
        """Toglie tutto dallo schermo tranne titolo, enunciato, oggetti fissati e «tieni»."""
        salvi = [m for m in [self._titolo, self._enunciato, *self._fissi, *tieni] if m is not None]
        via = [m for m in self.mobjects if not any(m is s for s in salvi)]
        self._attenuati = [m for m in self._attenuati if any(m is s for s in salvi)]
        if via:
            self.play(*[FadeOut(m) for m in via], run_time=run_time)

    # ---- attenzione -------------------------------------------------------
    @staticmethod
    def _scala_opacita(m, k):
        for sm in m.get_family():
            if isinstance(sm, VMobject):
                if len(sm.points):
                    sm.set_fill(opacity=sm.get_fill_opacity() * k, family=False)
                    sm.set_stroke(opacity=sm.get_stroke_opacity() * k, family=False)
            elif isinstance(sm, ImageMobject):
                sm.set_opacity(min(1.0, getattr(sm, "_vl_op", 1.0) * k))
                sm._vl_op = min(1.0, getattr(sm, "_vl_op", 1.0) * k)

    def evidenzia(self, *mobs, run_time=0.4):
        """Un solo punto d'attenzione: tutto il resto (titolo ed enunciato esclusi) scende al 35%."""
        tieni = set()
        for m in mobs:
            tieni.update(id(x) for x in m.get_family())

        def foglie(m):
            if id(m) in tieni:
                return []
            fam = m.get_family()
            if not any(id(x) in tieni for x in fam):
                return [m]
            out = []
            for sm in m.submobjects:
                out += foglie(sm)
            return out

        esclusi = [x for x in (self._titolo, self._enunciato) if x is not None]
        gia = {id(m) for m in self._attenuati}
        da_attenuare = []
        for m in self.mobjects:
            if any(m is e for e in esclusi):
                continue
            da_attenuare += [x for x in foglie(m) if id(x) not in gia]
        da_ripristinare = [m for m in self._attenuati if id(m) in tieni]
        anim = []
        for m in da_attenuare:
            m.generate_target()
            self._scala_opacita(m.target, OPACITA_SFONDO)
            anim.append(MoveToTarget(m))
        for m in da_ripristinare:
            m.generate_target()
            self._scala_opacita(m.target, 1 / OPACITA_SFONDO)
            anim.append(MoveToTarget(m))
        self._attenuati = [m for m in self._attenuati if id(m) not in tieni] + da_attenuare
        if anim:
            self.play(*anim, run_time=run_time)

    def ripristina(self, run_time=0.4):
        """Riporta tutto a opacita' piena."""
        anim = []
        for m in self._attenuati:
            m.generate_target()
            self._scala_opacita(m.target, 1 / OPACITA_SFONDO)
            anim.append(MoveToTarget(m))
        self._attenuati = []
        if anim:
            self.play(*anim, run_time=run_time)

    def trasforma(self, a, b, run_time=0.8, corrispondenze=True):
        """La formula a diventa b (le parti uguali restano, il resto si trasforma). b prende il posto di a."""
        an = TransformMatchingShapes(a, b) if corrispondenze else ReplacementTransform(a, b)
        self.play(an, run_time=run_time)
        return b

    def spunta(self, m, colore=VERDE):
        """Segno di spunta accanto a m (ipotesi usata, passo fatto). Ritorna il mobject da animare."""
        h = max(0.22, m.height * 0.5) if m.height < 1 else 0.4
        s = VMobject(stroke_color=colore, stroke_width=7)
        s.set_points_as_corners([[-0.5 * h, 0, 0], [-0.15 * h, -0.4 * h, 0], [0.6 * h, 0.5 * h, 0]])
        s.next_to(m, RIGHT, buff=0.25)
        return s

    def croce(self, m, colore=ROSSO):
        h = 0.3
        s = VGroup(Line([-h / 2, -h / 2, 0], [h / 2, h / 2, 0]), Line([-h / 2, h / 2, 0], [h / 2, -h / 2, 0]))
        s.set_stroke(colore, 7)
        s.next_to(m, RIGHT, buff=0.25)
        return s

    # ---- controllo qualita' dello schermo ----------------------------------
    def _nota(self, gravita, msg):
        sid = self._seg.id if self._seg else "-"
        chiave = (gravita, sid, re.sub(r"[\d.,]+", "#", msg))
        if any(q[4] == chiave for q in self.qa):
            return False
        self.qa.append((gravita, sid, round(self.ora(), 1) if self._seg else 0.0, msg, chiave))
        return True

    @staticmethod
    def _opacita(m):
        op = 0.0
        for sm in m.get_family():
            if isinstance(sm, ImageMobject):
                op = max(op, getattr(sm, "_vl_op", 1.0))
            elif isinstance(sm, VMobject) and len(sm.points):
                op = max(op, sm.get_fill_opacity(), sm.get_stroke_opacity() if sm.get_stroke_width() > 0 else 0)
        return op

    @staticmethod
    def _box(m):
        return (m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1])

    def _controlla_schermo(self):
        visti, nuovi = [], False
        for top in self.mobjects:
            fam = top.get_family()
            if not any(len(getattr(x, "points", [])) or isinstance(x, ImageMobject) for x in fam):
                continue
            if self._opacita(top) < 0.05:
                continue
            x0, x1, y0, y1 = self._box(top)
            tol = 0.02
            if x0 < -F["fw"] / 2 - tol or x1 > F["fw"] / 2 + tol or y0 < -F["fh"] / 2 - tol or y1 > F["fh"] / 2 + tol:
                nuovi |= self._nota("errore", f"oggetto fuori dal quadro ({type(top).__name__}, x {x0:.1f}…{x1:.1f}, y {y0:.1f}…{y1:.1f})")
            for x in fam:
                if hasattr(x, "vl") and self._opacita(x) >= 0.05:
                    visti.append(x)
        parole = 0
        for m in visti:
            v = m.vl
            x0, x1, y0, y1 = self._box(m)
            nome = self._nome(m)
            tol = 0.03
            if x0 < F["x0"] - tol or x1 > F["x1"] + tol or y0 < F["y0"] - tol or y1 > F["y1"] + tol:
                nuovi |= self._nota("errore", f"fuori dalla zona sicura: {nome}")
            if v["pct0"] and v["tipo"] != "figura":
                pct = v["pct0"] * m.height / v["h0"]
                minimo = F["min_formula"] if v["tipo"] == "formula" else F["minimo"]
                if pct < minimo - 0.05:
                    nuovi |= self._nota("errore", f"testo troppo piccolo ({pct:.1f}% < {minimo}%): {nome}")
            if v["tipo"] == "testo" and v["conta"] and self._opacita(m) > 0.5:
                parole += v["parole"]
        if parole > F["parole_schermo"]:
            nuovi |= self._nota("errore", f"{parole} parole di testo a schermo (max {F['parole_schermo']})")
        scritti = [m for m in visti if m.vl["tipo"] in ("testo", "formula", "etichetta", "codice", "figura")]
        for i in range(len(scritti)):
            a = self._box(scritti[i])
            fam_a = None
            for j in range(i + 1, len(scritti)):
                b = self._box(scritti[j])
                ox = min(a[1], b[1]) - max(a[0], b[0])
                oy = min(a[3], b[3]) - max(a[2], b[2])
                if ox > 0.06 and oy > 0.06:
                    if fam_a is None:
                        fam_a = {id(x) for x in scritti[i].get_family()}
                    if id(scritti[j]) in fam_a or id(scritti[i]) in {id(x) for x in scritti[j].get_family()}:
                        continue
                    nuovi |= self._nota("errore", f"sovrapposizione: {self._nome(scritti[i])} / {self._nome(scritti[j])}")
        if nuovi:
            n = self._n_foto.get(self._seg.id, 0)
            if n < 3:
                self._n_foto[self._seg.id] = n + 1
                self.foto(f"problema_{self._seg.id}_{n + 1}", aggiorna=False)

    @staticmethod
    def _nome(m):
        if isinstance(m, Text):
            return f"«{m.text[:28]}»"
        if isinstance(m, MathTypst):
            return f"formula «{str(getattr(m, 'typst_code', getattr(m, 'math_expression', '')))[:28]}»"
        return type(m).__name__

    def foto(self, nome, aggiorna=True):
        """Salva il fotogramma corrente in qa/<video>/<nome>.png."""
        from PIL import Image
        try:
            if aggiorna:
                self.renderer.update_frame(self)
            img = Image.fromarray(self.renderer.get_frame()).convert("RGB")
            if img.width > 1280 or img.height > 1280:
                k = 1280 / max(img.size)
                img = img.resize((int(img.width * k), int(img.height * k)))
            img.save(self.cartella_qa / f"{nome}.png")
        except Exception as e:  # la foto non deve mai fermare il render
            self._nota("avviso", f"foto «{nome}» non salvata: {e}")


# ==========================================================================
# 4. SOTTOTITOLI
# ==========================================================================
def _frasi_con_tempi(segmenti):
    """[(t_inizio, t_fine, [Parola...])] per frase, tempi assoluti nel video."""
    out = []
    for s in segmenti:
        if s.t0 is None:
            continue
        cor = []
        for p in s.parole:
            cor.append(p)
            if p.testo[-1:] in ".?!" or p.fine_pezzo:
                out.append((s.t0, cor))
                cor = []
        if cor:
            out.append((s.t0, cor))
    return out


def _spezza(parole, max_car, max_parole=None, min_parole=1):
    """Divide una frase in blocchi di al piu' max_car caratteri, preferendo le virgole."""
    blocchi, cor = [], []
    for p in parole:
        prova = " ".join(x.testo for x in cor + [p])
        if cor and (len(prova) > max_car or (max_parole and len(cor) >= max_parole)):
            # taglia all'ultima virgola se non lascia un blocco troppo corto
            taglio = len(cor)
            for i in range(len(cor) - 1, min_parole - 1, -1):
                if cor[i].testo[-1:] in ",;:" and i + 1 >= min_parole:
                    taglio = i + 1
                    break
            blocchi.append(cor[:taglio])
            cor = cor[taglio:] + [p]
        else:
            cor.append(p)
    if cor:
        if blocchi and len(cor) < min_parole and len(" ".join(x.testo for x in blocchi[-1] + cor)) <= max_car + 8:
            blocchi[-1] += cor
        else:
            blocchi.append(cor)
    return blocchi


def _blocchi_sottotitoli(segmenti, max_car, max_parole=None, min_parole=1):
    out = []
    for t0, frase in _frasi_con_tempi(segmenti):
        for b in _spezza(frase, max_car, max_parole, min_parole):
            out.append([t0 + b[0].t, t0 + b[-1].t + b[-1].d + 0.35, " ".join(x.testo for x in b)])
    for i in range(len(out) - 1):
        out[i][1] = min(out[i][1], out[i + 1][0] - 0.02)
    return out


def _due_righe(s, largo=42):
    if len(s) <= largo:
        return s
    parole, meglio = s.split(), None
    for i in range(1, len(parole)):
        a, b = " ".join(parole[:i]), " ".join(parole[i:])
        if len(a) <= largo and len(b) <= largo:
            sc = abs(len(a) - len(b))
            if meglio is None or sc < meglio[0]:
                meglio = (sc, a + "\n" + b)
    return meglio[1] if meglio else s


def _t_srt(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def scrivi_srt(segmenti, percorso):
    """Sottotitoli a frasi (max 42 caratteri per riga, 2 righe)."""
    righe = []
    for i, (a, b, txt) in enumerate(_blocchi_sottotitoli(segmenti, 80), 1):
        righe.append(f"{i}\n{_t_srt(a)} --> {_t_srt(b)}\n{_due_righe(txt)}\n")
    Path(percorso).write_text("\n".join(righe), encoding="utf-8")
    return len(righe)


def scrivi_ass(segmenti, percorso, pw, ph):
    """Sottotitoli da bruciare nel verticale: 3-6 parole su una riga, sopra la zona coperta in basso."""
    a, b, s, d = FORMATI["9:16"]["sicura"]
    corpo = int(ph * 0.03)
    larg_utile = pw * (1 - s - d)
    max_car = int(larg_utile / (corpo * 0.56))
    margine_v = int(ph * (b - 0.085))       # dentro la fascia tra contenuto (35%) e interfaccia (~25%)
    ml, mr = int(pw * s), int(pw * d)

    def t_ass(t):
        cs = int(round(t * 100))
        return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"

    testa = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {pw}
PlayResY: {ph}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Segoe UI,{corpo},&H00DFE8EC,&H00DFE8EC,&H00261F1C,&H00000000,-1,0,0,0,100,100,0,0,1,{max(2, corpo // 12)},0,2,{ml},{mr},{margine_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    righe = []
    for t0, t1, txt in _blocchi_sottotitoli(segmenti, max_car, max_parole=6, min_parole=3):
        righe.append(f"Dialogue: 0,{t_ass(t0)},{t_ass(t1)},Sub,,0,0,0,,{txt}")
    Path(percorso).write_text(testa + "\n".join(righe) + "\n", encoding="utf-8-sig")
    return len(righe)


# ==========================================================================
# 5. FINALIZZAZIONE E CONTROLLI SUL FILE
# ==========================================================================
def traccia_audio(segmenti, durata_video, percorso_wav):
    """Mette l'audio di ogni segmento al suo t0 in una traccia lunga quanto il video."""
    n = int(round(durata_video * SR))
    tr = np.zeros(n, dtype=np.int32)
    for s in segmenti:
        if s.t0 is None or s.audio is None:
            continue
        i = int(round(s.t0 * SR))
        a = s.audio[: max(0, n - i)]
        tr[i:i + len(a)] += a
    scrivi_wav(percorso_wav, np.clip(tr, -32768, 32767).astype(np.int16))
    return percorso_wav


def _run(cmd, cwd=None):
    r = subprocess.run(cmd, capture_output=True, cwd=cwd)
    if r.returncode != 0:
        raise RuntimeError("ffmpeg ha fallito:\n" + r.stderr.decode("utf-8", "replace")[-1500:])
    return r.stderr.decode("utf-8", "replace")


def misura_loudness(percorso, prima=""):
    """(LUFS integrati, picco vero dBTP) del file audio/video; «prima» = filtri da applicare prima di misurare."""
    err = _run([ffmpeg_exe(), "-hide_banner", "-nostats", "-i", str(percorso), "-vn", "-af",
                (prima + "," if prima else "") + "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"])
    j = json.loads(err[err.rindex("{"): err.rindex("}") + 1])
    return float(j["input_i"]), float(j["input_tp"]), j


def filtro_volume(sorgente, lufs=-14.0, picco=-3.0):
    """Filtro ffmpeg che porta l'audio a «lufs»: guadagno fisso misurato con loudnorm + limitatore sui picchi.

    (loudnorm usato direttamente sbaglia di 0,5-1 LU sui video brevi e sul parlato con pause.)"""
    lim = f"alimiter=limit={10 ** (picco / 20):.3f}:level=disabled:attack=5:release=80"
    g = lufs - misura_loudness(sorgente)[0]
    for _ in range(2):                       # il limitatore toglie un po' di volume: si compensa
        g += lufs - misura_loudness(sorgente, f"volume={g:.2f}dB,{lim}")[0]
    return f"volume={g:.2f}dB,{lim}"


def rinormalizza(mp4):
    """Riporta a -14 LUFS l'audio di un MP4 gia' fatto, senza toccare il video."""
    mp4 = Path(mp4)
    tmp = mp4.with_suffix(".tmp.mp4")
    _run([ffmpeg_exe(), "-y", "-v", "error", "-i", str(mp4), "-c:v", "copy", "-af", filtro_volume(mp4),
          "-ar", str(SR), "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(tmp)])
    os.replace(tmp, mp4)
    return misura_loudness(mp4)[:2]


def finalizza(video_muto, wav, uscita_mp4, ass=None):
    """Audio a -14 LUFS (guadagno + limitatore), unione col video, sottotitoli bruciati se ass."""
    uscita_mp4 = Path(uscita_mp4)
    uscita_mp4.parent.mkdir(parents=True, exist_ok=True)
    af = filtro_volume(wav)
    cmd = [ffmpeg_exe(), "-y", "-v", "error", "-i", str(video_muto), "-i", str(wav)]
    cwd = None
    if ass:
        cwd = str(Path(ass).parent)                      # percorso relativo: niente «C:» da proteggere nel filtro
        cmd += ["-vf", f"ass={Path(ass).name}", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                "-pix_fmt", "yuv420p"]
    else:
        cmd += ["-c:v", "copy"]
    cmd += ["-af", af, "-ar", str(SR), "-c:a", "aac", "-b:a", "160k", "-map", "0:v:0", "-map", "1:a:0",
            "-movflags", "+faststart", str(uscita_mp4)]
    _run(cmd, cwd=cwd)
    return uscita_mp4


def info_mp4(percorso):
    """Controllo del file finale con PyAV: tracce, durate, risoluzione."""
    import av
    with av.open(str(percorso)) as c:
        v = c.streams.video[0]
        d = dict(larghezza=v.width, altezza=v.height, fps=float(v.average_rate),
                 durata_video=float(v.duration * v.time_base) if v.duration else float(c.duration / 1e6),
                 audio=len(c.streams.audio) > 0, mb=os.path.getsize(percorso) / 1e6)
        if d["audio"]:
            a = c.streams.audio[0]
            d["durata_audio"] = float(a.duration * a.time_base) if a.duration else None
            d["hz"] = a.rate
    return d


def _parole_a(segmenti, t, finestra=2.2):
    out = []
    for s in segmenti or []:
        if s.t0 is None:
            continue
        for p in s.parole:
            if t - 0.6 <= s.t0 + p.t <= t + finestra:
                out.append(p.testo)
    return " ".join(out)


def estrai_fotogrammi(mp4, cartella, ogni=5.0, segmenti=None, per_foglio=6, log=print):
    """Fotogrammi ogni «ogni» secondi + fogli di contatto con il tempo e le parole dette in quel momento.

    Misura anche il tratto piu' lungo di schermo fermo. Ritorna dict(fogli=[...], fermo=(durata, da, a)).
    """
    import av
    from PIL import Image, ImageDraw, ImageFont
    cartella = Path(cartella)
    cartella.mkdir(parents=True, exist_ok=True)
    for f in cartella.glob("f_*.png"):
        f.unlink()
    for f in cartella.glob("foglio_*.png"):
        f.unlink()
    foto, prec, t_cambio, fermo = [], None, 0.0, (0.0, 0.0, 0.0)
    prossimo = ogni / 2
    with av.open(str(mp4)) as c:
        v = c.streams.video[0]
        fps = float(v.average_rate)
        passo = max(1, int(round(fps / 3)))
        for i, fr in enumerate(c.decode(v)):
            t = i / fps
            if i % passo == 0:
                picc = fr.to_ndarray(width=160, height=int(160 * v.height / v.width) // 2 * 2, format="gray").astype(np.int16)
                if prec is not None and (np.abs(picc - prec) > 12).mean() > 0.0004:
                    if t - t_cambio > fermo[0]:
                        fermo = (t - t_cambio, t_cambio, t)
                    t_cambio = t
                prec = picc
            if t >= prossimo:
                img = fr.to_image()
                foto.append((t, img))
                prossimo += ogni
        if t - t_cambio > fermo[0]:
            fermo = (t - t_cambio, t_cambio, t)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 17)
    except OSError:
        font = ImageFont.load_default()
    fogli = []
    verticale = foto and foto[0][1].height > foto[0][1].width
    col_n = 3 if not verticale else 6
    per_foglio = per_foglio if not verticale else 6
    lw = 640 if not verticale else 320
    for n in range(0, len(foto), per_foglio):
        gruppo = foto[n:n + per_foglio]
        lh = int(lw * gruppo[0][1].height / gruppo[0][1].width)
        righe = (len(gruppo) + col_n - 1) // col_n
        foglio = Image.new("RGB", (col_n * lw, righe * (lh + 46)), "#000000")
        dr = ImageDraw.Draw(foglio)
        for k, (t, img) in enumerate(gruppo):
            x, y = (k % col_n) * lw, (k // col_n) * (lh + 46)
            foglio.paste(img.resize((lw, lh)), (x, y))
            detto = _parole_a(segmenti, t)
            riga = f"{int(t) // 60}:{int(t) % 60:02d}  {detto}"
            while dr.textlength(riga, font=font) > lw - 8 and len(riga) > 10:
                riga = riga[:-2]
            dr.text((x + 4, y + lh + 2), riga[: len(riga)], fill="#ffd866", font=font)
            img.resize((lw, lh)).save(cartella / f"f_{int(t):04d}.png")
        p = cartella / f"foglio_{n // per_foglio + 1:02d}.png"
        foglio.save(p)
        fogli.append(str(p))
    if log:
        log(f"  fotogrammi: {len(foto)} in {len(fogli)} fogli; schermo fermo al massimo {fermo[0]:.1f} s "
            f"(da {fermo[1]:.0f} a {fermo[2]:.0f} s)")
    return dict(fogli=fogli, fermo=fermo)


def pulisci_media(cartella=None):
    """Cancella i file intermedi di Manim (il disco e' quasi pieno)."""
    c = Path(cartella or MEDIA)
    if c.exists():
        shutil.rmtree(c, ignore_errors=True)


def scrivi_report(percorso, righe):
    Path(percorso).write_text("\n".join(righe) + "\n", encoding="utf-8")
