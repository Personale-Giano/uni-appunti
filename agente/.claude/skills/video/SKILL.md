---
name: video
description: Crea, solo su richiesta, un video che spiega un argomento dei riassunti universitari di Emanuele (o di Leonardo) con animazioni e voce italiana. Si usa con «/video <materia> <argomento o capitolo> [verticale]» o quando Emanuele chiede «fammi un video su…», «spiegamelo con un video», «un video del capitolo N». Non si usa mai di propria iniziativa.
---

# /video <materia> <argomento o capitolo> [verticale]

Produce un MP4 con animazioni (Manim + Typst), voce sintetica italiana (edge-tts) e sottotitoli, a partire
da un capitolo dei riassunti. Tutto il sistema è in `C:/Users/admin/Desktop/UNI/agente/_sistema/video/`.

**Prima di tutto leggi** `C:/Users/admin/Desktop/UNI/agente/_sistema/video/REGOLE_VIDEO.md` (formati, regole
di copione/schermo/audio, checklist dei 20 punti: sono vincolanti) e
`C:/Users/admin/Desktop/UNI/agente/_sistema/video/README.md` (API di `videolib`, comandi, problemi noti).
Come esempi completi apri i copioni già fatti in `_sistema/video/copioni/`:
`fondamenti_induzione.py` (dimostrazione), `programmazione_cap30_stack_frame.py` (codice C e stack).

## Procedura

1. **Fonte.** Il video dice le stesse cose del capitolo, con la sua notazione. Cerca il capitolo in
   `C:/Users/admin/Documents/GitHub/quaderno-privato/contenuti/<materia>.json` (algebra, matematica-discreta,
   fondamenti, programmazione, laboratorio), per Leonardo in `spazi_contenuti/leonardo/…` dello stesso repo,
   oppure la bozza in `C:/Users/admin/Desktop/UNI/agente/_sistema/bozze/<materia>_capN.md`. Leggi anche le
   eccezioni in `C:/Users/admin/Desktop/UNI/agente/STATO.md` (slide corrette nei capitoli): vale il capitolo.
   Se l'argomento non è nei riassunti, dillo e chiedi: non inventare.
2. **Formato** (REGOLE_VIDEO): (a) concetto in 60-90 s, verticale 9:16, 170-220 parole, sottotitoli bruciati,
   se Emanuele dice «verticale», «breve», «per il telefono»; (b) spiegazione completa 16:9, **3-8 minuti**,
   è il default; (c) esercizio svolto 16:9. Un solo obiettivo dicibile in una frase.
3. **Copione** in `_sistema/video/copioni/<materia>_<slug>.py`: una classe che eredita da `ScenaBase` con
   `META`, `SEGMENTI = [Seg(id, titolo, testo_parlato), …]` e un metodo `seg_<id>(self, s)` per segmento.
   Scaletta: aggancio con domanda (entro 10 s) · intuizione · esempio concreto con numeri **prima** della
   definizione · definizione formale · esempio svolto / dimostrazione · errore tipico · riepilogo in 3 punti ·
   domanda di verifica con `[pausa 2.5]` e risposta. Una domanda di previsione prima di un risultato chiave.
   Testo parlato: frasi ≤ 22 parole, seconda persona, niente simboli né lettere isolate («enne più uno»,
   «effe pi», «ics»), nomi in camelCase scritti staccati («sum squares»), stessa parola per lo stesso concetto.
   A schermo: ≤ 12 parole di testo, formule in Typst, un termine nuovo compare quando la voce lo dice.
4. **Voce e durate**: `fai_video.py copioni/<file>.py --solo-voce`. Correggi finché non ci sono errori sul
   copione; regola `velocita` per segmento (formule e dimostrazioni più lente, −8 … −15).
5. **Revisione del contenuto** (obbligatoria, prima del render finale): subagente `revisore-riassunti` con
   il percorso del copione e della fonte; chiedigli errori matematici/tecnici, affermazioni non sostenute dal
   capitolo, notazione diversa, incoerenze voce/schermo. Applica le correzioni.
6. **Render di prova**: `fai_video.py copioni/<file>.py --prova` (circa 1 minuto per 4 minuti di video).
7. **Guarda davvero i fotogrammi** con Read: tutti i `qa/<slug>_prova/fotogrammi/foglio_NN.png` (sotto ogni
   fotogramma c'è il tempo e ciò che la voce sta dicendo) e il `report.txt`. Cerca: sovrapposizioni (anche
   testo sopra frecce o forme, che il controllo automatico non vede), testo tagliato o piccolo, formule rese
   male, schermate vuote, immagine che non corrisponde alle parole. Correggi e ripeti: **almeno 2 giri**,
   finché la checklist passa. `--solo id1,id2` rende solo alcuni segmenti.
8. **Render finale**: `fai_video.py copioni/<file>.py` (circa 45 s di render per minuto di video a 1080p).
   Riguarda i fogli in `qa/<slug>/fotogrammi/` e controlla nel report: traccia audio presente, durata audio =
   durata video, circa −14 LUFS, nessun errore.
9. **Consegna**: `C:/Users/admin/Desktop/UNI/agente/video/<materia>/<slug>.mp4` (+ `.srt`, + `_copione.py`).
   Di' a Emanuele percorso, durata, cosa non hai potuto verificare (la voce non la puoi ascoltare: pronuncia
   di sigle e parole inglesi da controllare a orecchio).
10. **Pulizia** (disco quasi pieno): `fai_video.py` cancella da solo `media/`; a lavoro finito cancella anche
    `_sistema/video/qa/<slug>_prova/`. La cartella `cache_audio/` si può svuotare quando il video è approvato.
    `video/`, `qa/`, `cache_audio/`, `media/` sono in `.gitignore`: nel repo pubblico vanno solo libreria e copioni.

## Comandi

```bash
export PYTHONUTF8=1
PY=C:/Users/admin/AppData/Local/Programs/Python/Python312/python.exe
cd C:/Users/admin/Desktop/UNI/agente/_sistema/video
$PY fai_video.py copioni/fondamenti_induzione.py --solo-voce
$PY fai_video.py copioni/fondamenti_induzione.py --prova
$PY fai_video.py copioni/fondamenti_induzione.py            # finale; --verticale forza il 9:16
```
I render lunghi vanno lanciati in background (oltre 2 minuti). La prima sintesi della voce richiede la rete.

## Copione minimo (vero)

```python
from videolib import *

class Somma(ScenaBase):
    META = dict(materia="fondamenti", slug="somma_interi", titolo="La somma dei primi n interi",
                formato="16:9", voce="it-IT-GiuseppeMultilingualNeural", velocita=0)
    SEGMENTI = [
        Seg("aggancio", "La domanda",
            "Quanto fa la somma dei numeri da uno a cento? C'è una formula che lo dice subito."),
        Seg("formula", "La formula",
            "La somma fino a enne vale enne, per enne più uno, diviso due. "
            "Con cento, quanto viene? [pausa 2.5] Cento per centouno, diviso due: cinquemilacinquanta.",
            velocita=-8, pausa_dopo=1.5),
    ]

    def seg_aggancio(self, s):
        d = self.testo("1 + 2 + … + 100 = ?", 7, peso=BOLD)
        self.poni(d, 0.5, 0.6)                              # frazioni dell'area: (0,0) in basso a sinistra
        self.play(FadeIn(d), run_time=0.4)

    def seg_formula(self, s):
        self.pulisci()
        f = formula(r"S_n = (n(n+1))/2", 8, ACCENTO)        # Typst, mai LaTeX
        self.poni(f, 0.5, 0.65)
        self.alla("vale enne", Write(f), run_time=1.5)      # parte quando la voce dice «vale enne»
        g = formula(f"S_100 = (100 dot 101)/2 = {col('5050', VERDE)}", 7)
        self.poni(g, 0.5, 0.25)
        self.alla("Cento per centouno", FadeIn(g, shift=UP * 0.2))
```
Attrezzi principali (dettagli nel README): `self.testo`, `formula`, `col`, `etichetta`, `self.poni`,
`self.alla`, `self.fino_a`, `self.enunciato`, `self.evidenzia` / `self.ripristina`, `self.trasforma(a, b)`,
`self.spunta`, `self.pulisci`, `self.codice(src)` + `c.riga(n)`, `TabellaTraccia`, `Caselle`, `Pila`
(`push`, `pop`, `puntatore`, `sposta`, `attiva`), `self.figura("fond/x.png")`.
Voce di default: `it-IT-GiuseppeMultilingualNeural` (pause brevi tra le frasi, legge meglio le parole inglesi);
alternativa `it-IT-DiegoNeural` (più lenta, pause di quasi un secondo tra le frasi).

## Per materia
- **Dimostrazioni**: enunciato fisso in alto (`self.enunciato`), prima un caso numerico, un passaggio per
  volta con la formula che si trasforma, il termine che cambia colorato, spunta sull'ipotesi quando si usa,
  domanda finale «dove abbiamo usato l'ipotesi?».
- **Codice C**: codice a sinistra con la riga corrente (`c.riga`), a destra `TabellaTraccia`, `Caselle` o
  `Pila`; input piccoli; un'istruzione per passo; errore tipico; il codice è quello del capitolo.
- **Psicologia (Leonardo)**: domanda di ricerca, procedura come linea del tempo, previsione, un solo grafico
  o numero, interpretazione distinta dal risultato, autore e anno a schermo.

## Cosa non fare
- Nessun video non richiesto; nessun video «di tutto il capitolo» se bastano 5 minuti su un'idea.
- Niente musica, niente immagini di repertorio, niente animazioni decorative, niente testo che ripete la voce.
- Niente LaTeX/MiKTeX, ManimGL, manim-voiceover, torch, server MCP: non installare nulla senza necessità.
- Non saltare la revisione del contenuto né la visione dei fotogrammi: «0 errori automatici» non basta.
- Non pubblicare i video nel repo (`video/` è ignorata) e non mettere nei copioni testo copiato dal libro.
- Non superare 8 minuti (16:9) o 90 secondi (9:16): se non basta, proponi due video.
