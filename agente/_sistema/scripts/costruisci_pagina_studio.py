"""Costruisce la pagina di studio interattiva ("Quaderno di ripasso") con i dati veri.

Legge:  esami/quiz_*.md, esami/prob_*.md, flashcard/<materia>*.md, i Word (evidenziazioni gialle = studiato),
        piano_oggi.md, pagina_studio/{template.html (solo <head> e CSS), extra.css, body.html, app.js, gen.js}
Scrive: pagina_studio/index.html (la pagina) e pagina_studio/data.json (i dati, caricati con fetch).
Il sito si apre con apri_quaderno.bat o serve.py (che ricostruisce e serve su http://127.0.0.1:8765).

Il collaudo del generatore di esercizi è pagina_studio/test_gen.js (node test_gen.js).
Uso: python costruisci_pagina_studio.py
"""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

import sys as _s, pathlib as _pl
_s.path.insert(0, str(_pl.Path(__file__).resolve().parent))
from percorsi_word import trova as _trova  # noqa: E402
BASE = Path(__file__).resolve().parent.parent          # _sistema
UNI = BASE.parent.parent                                # cartella UNI
PAG = BASE / "pagina_studio"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from anki_build import parse_cards  # noqa: E402

# Percorsi dei Word: accetta sia i file sciolti in UNI\ sia le vecchie sottocartelle.
WORD = {
    "Algebra lineare": ["Riassunto Algebra lineare.docx", "Algebra lineare/Riassunto Algebra lineare.docx"],
    "Matematica discreta": ["Riassunto Matematica discreta.docx", "Matematica discreta/Appunti matematica discreta.docx"],
    "Fondamenti Info": ["Riassunto Fondamenti Informatica.docx", "Fondamenti Info/Fondamenti Informatica.docx"],
    "Programmazione": ["Riassunto Programmazione.docx", "Programmazione/Riassunto Programmazione.docx"],
}
# Date d'esame (AAAA-MM-GG), da compilare quando Moodle le pubblica; si possono anche inserire nella pagina.
ESAMI = {}

# Pesi d'esame di Matematica discreta: (tema, quiz su 150, problemi su 30, parole chiave per «nel Word»)
FREQ = [
    ("Permutazioni: cicli, tipo, periodo", 48, 14, r"permutazion|cicli disgiunti"), ("Aritmetica modulare e congruenze", 21, 10, r"congruenz|aritmetica modulare"),
    ("Z_N moltiplicativo (inversi, φ di Eulero)", 16, 9, r"φ di Eulero|funzione di Eulero|invertibil[ei] in ℤ"), ("Omomorfismi tra gruppi", 1, 9, r"omomorfism"),
    ("Coefficienti binomiali e combinatoria", 15, 15, r"coefficient[ei] binomial|combinatori"), ("Gruppi, sottogruppi, generatori", 29, 11, r"sottogrupp|gruppo ciclico|generator"),
    ("Parità delle permutazioni", 6, 6, r"parità"), ("MCD e algoritmo di Euclide", 1, 7, r"algoritmo di euclide|massimo comun divisore|MCD"),
    ("Funzioni, composizione, iniettività", 33, 4, r"iniettiv"), ("Appartenenza, inclusione, insiemi", 37, 0, r"appartenenza|inclusione"),
    ("Prodotto cartesiano, operazioni sugli insiemi", 21, 4, r"prodotto cartesiano"), ("Relazioni, equivalenze, induzione", 0, 0, r"equivalenz|induzione"),
]

# Tag delle domande -> tema. L'ordine di PRIORITA decide il tema quando una domanda ha più tag.
TAG_TEMA = {
    "permutazioni": "Permutazioni", "cicli-tipo-periodo": "Permutazioni", "parita": "Permutazioni",
    "aritmetica-modulare": "Aritmetica modulare e ℤ_N", "Z_N-moltiplicativo": "Aritmetica modulare e ℤ_N", "Z_N-additivo": "Aritmetica modulare e ℤ_N",
    "generatori": "Aritmetica modulare e ℤ_N", "MCD-euclide": "Aritmetica modulare e ℤ_N",
    "gruppi": "Gruppi e omomorfismi", "sottogruppi": "Gruppi e omomorfismi", "omomorfismi": "Gruppi e omomorfismi", "nucleo-immagine": "Gruppi e omomorfismi",
    "combinatoria": "Combinatoria", "disposizioni": "Combinatoria", "combinazioni": "Combinatoria", "coefficienti-binomiali": "Combinatoria",
    "funzioni": "Funzioni", "iniettiva-suriettiva-inversa": "Funzioni", "composizione": "Funzioni",
    "partizioni": "Partizioni e relazioni", "insiemi": "Insiemi", "appartenenza-inclusione": "Insiemi", "operazioni-insiemi": "Insiemi", "prodotto-cartesiano": "Insiemi",
    "base-2": "Binario", "altro": "Altro",
}
PRIORITA = ["Permutazioni", "Gruppi e omomorfismi", "Aritmetica modulare e ℤ_N", "Combinatoria", "Funzioni", "Partizioni e relazioni", "Binario", "Insiemi", "Altro"]
# Capitoli del Word di Mate discreta per tema (None = non ancora nel Word)
TEMI = {t: {"capitoli": None} for t in PRIORITA}
TEMI["Insiemi"]["capitoli"] = "cap. 1-3"
TEMI["Partizioni e relazioni"]["capitoli"] = "cap. 6-9"
TEMI["Funzioni"]["capitoli"] = "cap. 10-19"
# Peso d'esame del tema (0..1), dalla tabella FREQ
PESO_TEMA = {"Permutazioni": 0.0, "Aritmetica modulare e ℤ_N": 0.0, "Gruppi e omomorfismi": 0.0, "Combinatoria": 0.0, "Funzioni": 0.0, "Insiemi": 0.0, "Partizioni e relazioni": 0.0, "Binario": 0.0, "Altro": 0.0}
PESO_FREQ = {"Permutazioni": [0, 6], "Aritmetica modulare e ℤ_N": [1, 2, 7], "Gruppi e omomorfismi": [3, 5], "Combinatoria": [4], "Funzioni": [8], "Insiemi": [9, 10], "Partizioni e relazioni": [11]}


# Copertura: un tema di quiz compare solo se il Word di quella materia lo tratta (almeno 3 occorrenze delle parole chiave).
# Così i quiz seguono le lezioni fatte: quando si aggiungono capitoli sul tema, le domande compaiono da sole.
COPERTURA_RX = {
    ("Matematica discreta", "Insiemi"): r"appartenenza|inclusione|prodotto cartesiano",
    ("Matematica discreta", "Partizioni e relazioni"): r"partizion|equivalenz",
    ("Matematica discreta", "Funzioni"): r"iniettiv",
    ("Matematica discreta", "Numeri naturali e induzione"): r"induzione",
    ("Matematica discreta", "Permutazioni"): r"permutazion|cicli disgiunti",
    ("Matematica discreta", "Aritmetica modulare e ℤ_N"): r"congruenz|aritmetica modulare|classi di resto",
    ("Matematica discreta", "Gruppi e omomorfismi"): r"omomorfism|sottogruppo|gruppo ciclico|struttura di gruppo",
    ("Matematica discreta", "Combinatoria"): r"coefficient[ei] binomial|combinazion|disposizion",
    ("Matematica discreta", "Binario"): r"notazione binaria|scrittura in base|base 2",
    ("Algebra lineare", "Campi"): r"\bcamp[oi]\b", ("Algebra lineare", "Numeri complessi"): r"numeri complessi", ("Algebra lineare", "Coniugato e modulo"): r"coniugat",
    ("Algebra lineare", "Forma polare"): r"polare", ("Algebra lineare", "Potenze e radici"): r"radic[ei] n-esim|moivre|potenz", ("Algebra lineare", "Vettori"): r"vettor",
    ("Algebra lineare", "Matrici"): r"prodotto fra matrici|\btraccia\b|trasposta", ("Algebra lineare", "Rango"): r"\brango\b|rk\(",
    ("Algebra lineare", "Determinante"): r"determinant", ("Algebra lineare", "Matrice inversa"): r"invertibil|matrice inversa|cofattor",
    ("Programmazione", "Funzioni e parametri"): r"passaggio per valore|parametr[oi] formal|prototip",
    ("Fondamenti Info", "Rappresentazione binaria"): r"binari|complemento a due|esadecimal", ("Fondamenti Info", "Circuiti e memoria"): r"flip-flop|\bram\b|memoria",
    ("Fondamenti Info", "Compressione ed errori"): r"compressione|hamming", ("Fondamenti Info", "Logica proposizionale"): r"tavol[ae] di verit|tautologi|contraddizion",
    ("Fondamenti Info", "Logica avanzata"): r"quantificat|regol[ae] di inferenza|predicat",
    ("Fondamenti Info", "Automi e grammatiche"): r"\bautom[ai]\b|grammatic", ("Fondamenti Info", "Insiemi e relazioni"): r"relazion[ei] di equivalenza|prodotto cartesiano",
    ("Programmazione", "Algoritmi"): r"algoritm", ("Programmazione", "Assembly e macchina"): r"assembly", ("Programmazione", "Tipi e memoria"): r"memoria",
    ("Programmazione", "Variabili e assegnamento"): r"assegnament", ("Programmazione", "Operatori"): r"operator", ("Programmazione", "Puntatori"): r"puntator",
    ("Programmazione", "Input e output"): r"scanf|printf", ("Programmazione", "Compilazione e terminale"): r"gcc|compilazion", ("Programmazione", "Controllo di flusso"): r"\bfor\b|\bwhile\b|\bif\b",
}


def copertura(texts):
    """{(materia, tema): occorrenze nel Word}; i temi senza espressione (es. «Altro») non sono mai coperti."""
    return {k: len(re.findall(rx, texts.get(k[0], ""), re.I)) for k, rx in COPERTURA_RX.items()}


def _intervalli(nums):
    """[21, 22, 23, 26] -> 'cap. 21-23, 26'"""
    parti, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        parti.append(str(nums[i]) if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return "cap. " + ", ".join(parti)


def capitoli_per_tema():
    """{materia: {tema: {"cap": "cap. 21-31", "n": primo capitolo}}}: dove i riassunti trattano ogni tema dei quiz
    (almeno 2 occorrenze delle parole chiave di COPERTURA_RX nel capitolo). Serve ai suggerimenti «Rivedi» dopo un errore."""
    out = {}
    for mat, slug in SLUG.items():
        f = SITO / "contenuti" / f"{slug}.json"
        if not f.exists():
            continue
        caps = json.loads(f.read_text(encoding="utf-8"))["capitoli"]
        testi = [(c["num"], c["titolo"] + "\n" + "\n".join(re.sub(r"<[^>]+>", "", b.get("h", "")) for b in c["blocks"])) for c in caps]
        for (m, tema), rx in COPERTURA_RX.items():
            if m != mat:
                continue
            conta = {n: len(re.findall(rx, t, re.I)) for n, t in testi if n}
            mx = max(conta.values() or [0])
            # solo i capitoli dove il tema è denso (almeno il 35% del capitolo che ne parla di più): niente citazioni di passaggio
            nums = sorted(n for n, k in conta.items() if k >= max(2, 0.35 * mx))
            if nums:
                out.setdefault(mat, {})[tema] = {"cap": _intervalli(nums), "n": max(nums, key=lambda n: conta[n])}
    return out


# Schede generate dai riassunti: una per ogni Definizione/Teorema/Proposizione dei capitoli che non hanno già schede scritte a mano
# (le schede in _sistema/flashcard arrivano fino a questi capitoli esclusi). L'id è quello del blocco: i progressi restano stabili.
SCHEDE_AUTO_DA = {"Algebra lineare": 10, "Matematica discreta": 21, "Fondamenti Info": 12, "Programmazione": 9}
# etichetta vera («Definizione.», «Teorema (Binet):», «Definizione Formale:»), non la voce di un elenco («Definizione (function definition)…»)
_ETICHETTA = re.compile(r"^\s*<strong>\s*(Definizione|Teorema|Proposizione|Lemma|Corollario)\b(?:\s+formale)?(?:\s*\([^)<]{1,40}\))?\s*(?:[.:]\s*</strong>|</strong>\s*[.:])\s*", re.I)
_SUP = str.maketrans("0123456789+-−n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻ⁿ")
_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def _testo_scheda(h):
    import html as _h
    h = re.sub(r"<sup>([^<]*)</sup>", lambda m: m.group(1).translate(_SUP) if all(c in "0123456789+-−n" for c in m.group(1)) else "^(" + m.group(1) + ")", h)
    h = re.sub(r"<sub>([^<]*)</sub>", lambda m: m.group(1).translate(_SUB) if m.group(1).isdigit() else "_" + m.group(1), h)
    h = re.sub(r"</?strong>", "**", h)
    h = re.sub(r"</?code>", "`", h)
    return _h.unescape(re.sub(r"<[^>]+>", "", h)).strip()


def schede_dai_riassunti():
    out = []
    for mat, slug in SLUG.items():
        f = SITO / "contenuti" / f"{slug}.json"
        if not f.exists():
            continue
        for c in json.loads(f.read_text(encoding="utf-8"))["capitoli"]:
            if not c["num"] or c["num"] < SCHEDE_AUTO_DA.get(mat, 10 ** 6):
                continue
            titolo = re.sub(r"^\s*(?:Capitolo\s+)?\d+\s*[.:]?\s*", "", c["titolo"])
            sezione, blocchi = titolo, c["blocks"]
            for i, b in enumerate(blocchi):
                if b["t"] == "h3":
                    sezione = _testo_scheda(b["h"]).replace("**", "")
                    continue
                m = _ETICHETTA.match(b.get("h", "")) if b["t"] in ("p", "li") else None
                if not m:
                    continue
                tipo = m.group(1).capitalize()
                # la risposta è il blocco più i seguiti (formula, elenco delle condizioni, «In parole povere»), fino alla prossima sezione
                risposta = [_testo_scheda(b["h"][m.end():])]
                for nb in blocchi[i + 1:i + 6]:
                    if nb["t"] == "h3" or (nb["t"] in ("p", "li") and _ETICHETTA.match(nb.get("h", ""))) or "h" not in nb:
                        break
                    t = _testo_scheda(nb["h"])
                    risposta.append(("In parole povere: " + t) if nb.get("c") == "pp" else (("- " + t) if nb["t"] == "li" else t))
                    if nb.get("c") == "pp":
                        break
                termine = re.search(r"\*\*([^*]{2,60})\*\*", risposta[0])
                if tipo == "Definizione" and termine:
                    domanda = f"Definizione: che cos'è {termine.group(1).strip()}? (cap. {c['num']}, {sezione})"
                else:
                    domanda = f"{tipo} del cap. {c['num']} «{titolo}», sezione «{sezione}»: enunciala."
                r = "\n".join(x for x in risposta if x)
                out.append(dict(id="riass-" + b["b"].replace(".", "-") + "-" + slug[:4], m=mat, t=f"Cap. {c['num']} · {sezione}",
                                d=domanda, r=r, lungo=len(r) > 400, da_quiz=False, auto=True))
    return out


def parse_quizzes():
    out = []
    for f in sorted((BASE / "esami").glob("quiz_*.md")):
        prova = ""
        for blk in re.split(r"(?m)^(?=#{1,2} )", f.read_text(encoding="utf-8")):
            if blk.startswith("# "):
                prova = blk.splitlines()[0][2:].strip()
                continue
            if not blk.startswith("## ["):
                continue
            head, _, body = blk.partition("\n")
            m = re.match(r"## \[([^\]]+)\]\s*argomenti:\s*(.*)", head)
            r = re.search(r"(?m)^RISPOSTA:\s*(\d)", body)
            if not m or not r:
                continue
            pre, _, post = body.partition("RISPOSTA:")
            lines = pre.strip().splitlines()
            first_opt = next((i for i, l in enumerate(lines) if re.match(r"^1\.\s", l)), None)
            if first_opt is None:
                continue
            opts = [re.sub(r"^\d\.\s*", "", l).strip() for l in lines[first_opt:] if re.match(r"^[1-5]\.\s", l)]
            if len(opts) != 5:
                continue
            sp = re.search(r"(?ms)SPIEGAZIONE:\s*(.*?)(?=^ATTENZIONE:|\Z)", post)
            at = re.search(r"(?ms)ATTENZIONE:\s*(.*)", post)
            out.append(dict(id=m.group(1), prova=prova, args=[a.strip() for a in m.group(2).split(",") if a.strip()],
                            q="\n".join(lines[:first_opt]).strip(), o=opts, a=int(r.group(1)),
                            s=(sp.group(1).strip() if sp else ""), w=(at.group(1).strip() if at else "")))
    return out


def parse_problems():
    out = []
    for f in sorted((BASE / "esami").glob("prob_*.md")):
        for blk in re.split(r"(?m)^(?=## \[)", f.read_text(encoding="utf-8")):
            m = re.match(r"## \[([^\]]+)\]\s*argomenti:\s*(.*)", blk)
            if not m:
                continue
            t = re.search(r"(?ms)\*\*Testo:\*\*\s*(.*?)(?=^\*\*Soluzione:\*\*)", blk)
            s = re.search(r"(?ms)\*\*Soluzione:\*\*\s*(.*?)(?=^\*\*Concetti usati:\*\*|\Z)", blk)
            c = re.search(r"(?ms)\*\*Concetti usati:\*\*\s*(.*?)(?=^## |\Z)", blk)
            if not (t and s):
                continue
            out.append(dict(id=m.group(1), args=[a.strip() for a in m.group(2).split(",") if a.strip()],
                            testo=t.group(1).strip(), soluzione=s.group(1).strip(), concetti=(c.group(1).strip() if c else "")))
    return out


def card_id(mat, title, d):
    return mat[:3] + hashlib.sha1((title + "|" + d).encode("utf-8")).hexdigest()[:10]


def parse_all_cards():
    out, seen = [], set()
    for mat in WORD:
        files = sorted((BASE / "flashcard").glob(f"{mat}.md")) + sorted((BASE / "flashcard").glob(f"{mat}.*.md"))
        for p in files:
            for (t, q, a) in parse_cards(p):
                cid = card_id(mat, t, q)           # id basato sul contenuto: i progressi non si spostano se le schede cambiano
                if cid in seen:
                    continue
                seen.add(cid)
                out.append(dict(id=cid, m=mat, t=t, d=q, r=a, lungo=len(a) > 400, da_quiz=p.name.endswith(".quiz.md")))
    return out


def find_word(mat):
    for rel in WORD[mat]:
        p = _trova(UNI, '', Path(rel).name)
        if p.exists():
            return p
    return None


def chapters(path):
    """[(numero, titolo, stato)] stato 2 = studiato (almeno 3 paragrafi evidenziati), 1 = tracce isolate, 0 = no. Più il testo intero."""
    from docx import Document
    doc = Document(str(path))
    chs, cur, text = [], None, []
    for p in doc.paragraphs:
        txt = p.text.strip()
        text.append(txt)
        if txt and p.style.name.lower().startswith(("heading 1", "titolo 1")):   # ignora titoli vuoti
            m = re.match(r"(?:Capitolo\s+)?(\d+)[.:]?\s*(.*)", txt)
            cur = [int(m.group(1)) if m else len(chs) + 1, (m.group(2) if m else txt), 0, 0]
            chs.append(cur)
        if cur is not None and txt:
            cur[3] += 1
            if any(r.font.highlight_color is not None for r in p.runs):
                cur[2] += 1
    res = []
    for n, t, hl, tot in chs:
        res.append((n, t, 2 if hl >= 3 else (1 if hl else 0), hl, tot))   # le evidenziazioni sono a pezzi: da 3 paragrafi in su = studiato
    return res, "\n".join(text)


def _manuale():
    """studiato_manuale.json: {"Materia": [numeri di capitolo]} segnati come studiati a mano (le evidenziazioni nei Word non si toccano)."""
    f = BASE / "studiato_manuale.json"
    try:
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    except Exception:
        return {}


SITO = Path.home() / "Documents" / "GitHub" / "quaderno-privato"     # repo del sito: i riassunti vivono lì (non più nei Word)
SLUG = {"Algebra lineare": "algebra", "Matematica discreta": "matematica-discreta", "Fondamenti Info": "fondamenti",
        "Programmazione": "programmazione"}


def _evid_sito():
    """Evidenziazioni e capitoli 'studiati a mano' del sito: dall'esportazione dal database (evid_export.json, la scrive
    esporta_evid.js) o, in mancanza, da quelle di partenza ricavate dai Word."""
    for f in (BASE / "evid_export.json", SITO / "contenuti" / "_seed_evidenziazioni.json"):
        if f.exists():
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
                return d.get("evid", d), d.get("man", {})
            except Exception:
                pass
    return {}, {}


def capitoli_sito(slug, evid, man):
    """Come chapters(), ma dai contenuti del sito: ([(n, titolo, stato, paragrafi evidenziati, paragrafi)], testo intero)."""
    f = SITO / "contenuti" / f"{slug}.json"
    if not f.exists():
        return None
    dati = json.loads(f.read_text(encoding="utf-8"))
    ev = evid.get(slug, {})
    res, testi = [], []
    for c in dati["capitoli"]:
        blocchi = [b for b in c["blocks"] if b["t"] in ("p", "li", "pre")]
        testi.append(c["titolo"])
        for b in c["blocks"]:
            if b["t"] in ("p", "li", "pre", "h3"):
                testi.append(re.sub(r"<[^>]+>", "", b["h"]))
        hl = sum(1 for b in blocchi if ev.get(b["b"]))
        n = c["num"] if c["num"] is not None else len(res) + 1
        t = re.sub(r"^\s*(?:Capitolo\s+)?\d+\s*[.:]?\s*", "", c["titolo"])
        res.append((n, t, 2 if hl >= 3 else (1 if hl else 0), hl, len(blocchi)))
    return res, "\n".join(testi)


def avanzamento():
    out, texts = {}, {}
    evid, man_sito = _evid_sito()
    for mat in WORD:
        sito = capitoli_sito(SLUG[mat], evid, man_sito)
        if sito is not None:
            res, text = sito
            texts[mat] = text
            manuali = set(man_sito.get(SLUG[mat]) or [])
        else:
            p = find_word(mat)
            if p is None:
                out[mat] = dict(capitoli=0, studiati=0, lezioni="nessun capitolo", prossimo="Riassunto non trovato.", elenco=[])
                continue
            res, text = chapters(p)
            texts[mat] = text
            manuali = set((_manuale().get(mat) or []))   # capitoli che Emanuele ha chiesto di segnare come studiati senza evidenziarli
        res = [(n, t, 2 if n in manuali else s, hl, tot) for n, t, s, hl, tot in res]
        done = [n for n, _, s, *_ in res if s == 2]
        part = [n for n, _, s, *_ in res if s == 1]
        todo = [n for n, _, s, *_ in res if s == 0]
        def rng(l):
            if not l:
                return "nessuno"
            parts, a = [], l[0]
            for i, x in enumerate(l):
                if i + 1 == len(l) or l[i + 1] != x + 1:
                    parts.append(str(a) if a == x else f"{a}-{x}")
                    a = l[i + 1] if i + 1 < len(l) else None
            return ", ".join(parts)
        nota = f"Studiati: {rng(done)}." + (f" In parte: {rng(part)}." if part else "") + (f" Da studiare: {rng(todo)}." if todo else " Tutto studiato.")
        out[mat] = dict(capitoli=len(res), studiati=len(done), lezioni=f"{len(res)} capitoli (ultimo: {res[-1][0]}. {res[-1][1]})" if res else "nessun capitolo", prossimo=nota,
                        elenco=[dict(n=n, t=t, s=s, hl=hl, tot=tot) for n, t, s, hl, tot in res])
    lab = capitoli_sito("laboratorio", evid, man_sito)   # il laboratorio fa parte di ciò che è stato trattato per Programmazione
    if lab is not None and "Programmazione" in texts:
        texts["Programmazione"] += "\n" + lab[1]
    else:
        labw = _trova(UNI, "", "Riassunto Laboratorio.docx")
        if labw.exists() and "Programmazione" in texts:
            texts["Programmazione"] += "\n" + chapters(labw)[1]
    return out, texts


def piano():
    """La sezione «## Oggi» del piano serale, solo se il piano è di ieri o di oggi: un piano vecchio (attività ferma)
    mostrerebbe consigli superati, come è successo dal 16 ott al 3 nov 2026."""
    p = BASE / "piano_oggi.md"
    if not p.exists():
        return ""
    t = p.read_text(encoding="utf-8")
    d = re.search(r"\d{4}-\d{2}-\d{2}", t.splitlines()[0] if t else "")
    try:
        vecchio = (date.today() - date.fromisoformat(d.group(0))).days > 1 if d else True
    except ValueError:
        vecchio = True
    if vecchio:
        print(f"  piano_oggi.md è del {d.group(0) if d else '?'}: non lo mostro nel Quaderno")
        return ""
    m = re.search(r"(?ms)^## Oggi.*?\n(.*?)(?=^## Da tenere|\Z)", t)
    return m.group(1).strip() if m else ""


def diff_evidenziazioni(avanz):
    """Confronta le evidenziazioni gialle di oggi con l'ultimo controllo (evidenziazioni.json) e scrive evidenziazioni_oggi.md."""
    import json as _j
    snap = BASE / "evidenziazioni.json"
    prev = _j.loads(snap.read_text(encoding="utf-8")) if snap.exists() else {}
    cur = {m: {str(c["n"]): [c["hl"], c["tot"], c["t"]] for c in x["elenco"]} for m, x in avanz.items()}
    righe = []
    for m, caps in cur.items():
        for n, (hl, tot, t) in caps.items():
            old = (prev.get("materie", {}).get(m, {}).get(n) or [0])[0]
            if hl != old:
                stato = "studiato" if hl >= 3 else "iniziato"
                righe.append(f"- {m}, cap. {n} «{t}»: {'+' if hl > old else ''}{hl - old} paragrafi evidenziati (ora {hl} su {tot}, {stato})")
    out = [f"# Evidenziazioni: cambiamenti dall'ultimo controllo ({prev.get('data', 'primo controllo')})", ""]
    out += righe or ["Nessun cambiamento."]
    (BASE / "evidenziazioni_oggi.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    snap.write_text(_j.dumps(dict(data=str(date.today()), materie=cur), ensure_ascii=False), encoding="utf-8")
    print("\n".join(out))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    mate = parse_quizzes()
    for q in mate:  # tema = primo tema per priorità tra i tag della domanda
        q["m"] = "Matematica discreta"
        q["theme"] = next((t for t in PRIORITA if any(TAG_TEMA.get(x) == t for x in q["args"])), TAG_TEMA.get(q["args"][0], "Altro") if q["args"] else "Altro")
    from quiz_banche import tutte
    quiz, probs, cards = tutte(mate), parse_problems(), parse_all_cards()
    auto = schede_dai_riassunti()
    cards += auto
    print(f"  schede dai riassunti (definizioni e proposizioni): {len(auto)}")
    avanz, texts = avanzamento()
    cop = copertura(texts)
    visibili, nascoste = [], {}
    for q in quiz:
        if cop.get((q["m"], q["theme"]), 0) >= 3:
            visibili.append(q)
        else:
            nascoste.setdefault(q["m"], {}).setdefault(q["theme"], 0)
            nascoste[q["m"]][q["theme"]] += 1
    quiz = visibili
    from quiz_banche import tema_fondamenti, solo_it, titolo_it, inglese
    for c in cards:   # i quiz del sito sono bilingui: tengo l'italiano, titoli puliti
        if c["m"] == "Fondamenti Info":
            c["d"], c["r"], c["t"] = solo_it(c["d"]), solo_it(c["r"]), titolo_it(solo_it(c["t"]))
    from quiz_banche import chiave_testo, immagini_per_testo
    imm = immagini_per_testo()   # disegni scaricati dal sito esami, collegati alle schede dallo stesso testo
    for c in cards:
        if c["m"] == "Fondamenti Info" and c["da_quiz"] and chiave_testo(c["d"]) in imm:
            c["img"], c["imgf"] = imm[chiave_testo(c["d"])]
    cards = [c for c in cards if not inglese(c["d"] + " " + c["r"])]   # solo italiano: via le schede scritte solo in inglese
    n_cards = len(cards)   # schede ricavate dai quiz del sito di Fondamenti: tolte quelle su argomenti non ancora trattati
    cards = [c for c in cards if not (c["m"] == "Fondamenti Info" and c["da_quiz"]) or cop.get((c["m"], tema_fondamenti(c["d"] + " " + c["r"], c["t"])), 0) >= 3]
    print(f"  schede: {len(cards)} (nascoste {n_cards - len(cards)} su argomenti non ancora trattati)")
    coperti = {m: sorted(t for (mm, t), n in cop.items() if mm == m and n >= 3) for m in WORD}
    if "--diff" in sys.argv:
        diff_evidenziazioni(avanz)
    mate_txt = texts.get("Matematica discreta", "")
    freq = [[t, q, p, len(re.findall(rx, mate_txt, re.I)) >= 2] for (t, q, p, rx) in FREQ]
    pesi = {}
    for tema, idx in PESO_FREQ.items():
        pesi[tema] = sum(FREQ[i][1] / 150 + FREQ[i][2] / 30 for i in idx)
    mx = max(pesi.values()) or 1
    pesi = {k: round(v / mx, 3) for k, v in pesi.items()}
    data = dict(oggi=str(date.today()), quiz=quiz, problemi=probs, cards=cards, materie=avanz, freq=freq,
                tagTema=TAG_TEMA, priorita=PRIORITA, temi=TEMI, temiCap=capitoli_per_tema(), pesi=pesi, piano=piano(), esami=ESAMI, nascoste=nascoste, coperti=coperti)
    (PAG / "data.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    head = (PAG / "template.html").read_text(encoding="utf-8").split('<div class="app">')[0]
    head = head.replace("</style>", (PAG / "extra.css").read_text(encoding="utf-8") + "\n</style>", 1)
    html = '<meta charset="utf-8">\n' + head + (PAG / "body.html").read_text(encoding="utf-8") + "\n<script>\n" + (PAG / "gen.js").read_text(encoding="utf-8").replace("if (typeof module", "if (false && typeof module") + "\n" + (PAG / "app.js").read_text(encoding="utf-8") + "\n</script>\n"
    (PAG / "index.html").write_text(html, encoding="utf-8")
    print(f"{len(quiz)} domande, {len(probs)} problemi, {len(cards)} schede; index.html {len(html) // 1024} KB, data.json {(PAG / 'data.json').stat().st_size // 1024} KB")
    for m, x in avanz.items():
        print(f"  {m}: {x['studiati']}/{x['capitoli']} studiati. {x['prossimo']}")
    print("  nel Word:", [f[0][:18] for f in freq if f[3]])
    print("  quiz visibili:", {m: sum(1 for q in quiz if q["m"] == m) for m in WORD}, "| nascosti (argomenti non ancora trattati):", nascoste)


if __name__ == "__main__":
    main()
