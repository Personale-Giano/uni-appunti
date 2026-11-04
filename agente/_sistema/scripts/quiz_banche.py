"""Banche di quiz per materia, lette da esami/*.md e uniformate per la pagina di ripasso.

Ogni domanda: id, m (materia), theme, prova, args, q, o (2-8 opzioni), a (1..n), s (spiegazione), w (avvertenza).
- Matematica discreta: esami/quiz_*.md (150 domande delle prove 2024-2026, 5 opzioni).
- Algebra lineare, Programmazione: esami/banca_algebra.md, esami/banca_programmazione.md (stesso formato).
- Fondamenti Info: esami/fondamenti_quiz.md (quiz del sito esami), solo le domande a scelta singola o vero/falso
  senza figure; le altre tipologie (abbinamenti, risposte multiple) restano nelle schede.
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ESAMI = BASE / "esami"

TEMI_ALGEBRA = {"campi": "Campi", "numeri-complessi": "Numeri complessi", "coniugato-modulo": "Coniugato e modulo", "forma-polare": "Forma polare",
                "potenze-radici": "Potenze e radici", "vettori": "Vettori", "sistemi-lineari": "Sistemi lineari"}
TEMI_PROG = {"algoritmi": "Algoritmi", "assembly": "Assembly e macchina", "tipi-e-memoria": "Tipi e memoria", "variabili-assegnamento": "Variabili e assegnamento",
             "operatori": "Operatori", "puntatori": "Puntatori", "scanf-printf": "Input e output", "compilazione-cli": "Compilazione e terminale",
             "controllo-flusso": "Controllo di flusso", "funzioni": "Funzioni e parametri", "array-stringhe": "Array e stringhe",
             "algoritmi-array": "Algoritmi su array"}


TEMI_FND = {"binario": "Rappresentazione binaria", "complemento-eccesso": "Rappresentazione binaria", "virgola-mobile": "Rappresentazione binaria",
            "memoria": "Circuiti e memoria", "circuiti-logica": "Circuiti e memoria", "codifica-testo": "Rappresentazione binaria",
            "compressione": "Compressione ed errori", "errori-hamming": "Compressione ed errori"}


TEMI_MAT = {"insiemi": "Insiemi", "appartenenza-inclusione": "Insiemi", "operazioni-insiemi": "Insiemi", "prodotto-cartesiano": "Insiemi",
            "induzione": "Numeri naturali e induzione", "partizioni": "Partizioni e relazioni", "relazioni": "Partizioni e relazioni", "equivalenze": "Partizioni e relazioni",
            "funzioni": "Funzioni", "iniettiva-suriettiva-inversa": "Funzioni", "composizione": "Funzioni"}


MESI = {"Gen": "gennaio", "Feb": "febbraio", "Mar": "marzo", "Apr": "aprile", "Mag": "maggio", "Giu": "giugno", "Lug": "luglio", "Ago": "agosto", "Set": "settembre", "Ott": "ottobre", "Nov": "novembre", "Dic": "dicembre"}
LEZIONI_IT = [("Bits and their storage (flip-flops)", "I bit e la loro memorizzazione (flip-flop)"), ("Bits and their storage", "I bit e la loro memorizzazione"),
              ("Hexadecimal Notation", "Notazione esadecimale"), ("Main Memory", "Memoria principale"), ("Mass Storage", "Memoria di massa"),
              ("The Binary System", "Il sistema binario"), ("Storing Integers", "Memorizzare gli interi"), ("Eccess Notation", "Notazione in eccesso"),
              ("floating point notation", "Notazione in virgola mobile"), ("Compression and Comunication Errors", "Compressione ed errori di comunicazione")]
RIPULISCI = re.compile(r"\s*\((?:circuiti e rappresentazione binaria|logica proposizionale e quantificatori|prove con quantificatori|sequenze e relazioni|logica sequenziale, automi, grammatiche|esami \d{4}|simulazioni d'esame 2023)\)?|\s*\(risposta sì/no\)|\s*\(copia\)|\s*\(SENZA VALORE LEGALE\)", re.I)


def titolo_it(t):
    """Titoli dei quiz del sito in italiano, brevi e leggibili (niente inglese né diciture burocratiche)."""
    t = RIPULISCI.sub("", t).strip()
    m = re.match(r"(\d{4})(Gen|Feb|Mar|Apr|Mag|Giu|Lug|Ago|Set|Ott|Nov|Dic)(\d{2})\b.*?Turno ?(\w+)", t)
    if m:
        turno = "turno unico" if m.group(4).lower() == "unico" else "turno " + m.group(4)
        return f"Esame del {int(m.group(3))} {MESI[m.group(2)]} {m.group(1)} ({turno})"
    m = re.match(r"TURNO ([IVX]+) (\d\d)/(\d\d)/(\d\d)", t)
    if m:
        return f"Prova del {m.group(2)}/{m.group(3)}/20{m.group(4)} (turno {m.group(1)})"
    m = re.match(r"Simulazione (\d)", t)
    if m:
        return f"Simulazione d'esame {m.group(1)}"
    for en, it in LEZIONI_IT:
        t = t.replace(en, it)
    t = re.sub(r"\s*\bQuiz$", "", t)
    return re.sub(r"\s+", " ", t).strip(" .")


_EN = re.compile(r"\b(the|of|and|is|are|which|following|consider|given|assume|choose|that|with|from|this|these|be|then|an)\b", re.I)
_IT = re.compile(r"\b(il|lo|la|le|gli|di|del|della|che|con|per|una|nel|nella|quale|quali|è|sono|come|dei|delle|se|allora|si)\b", re.I)


def inglese(t):
    """True se il testo è scritto (quasi) solo in inglese."""
    e, i = len(_EN.findall(t)), len(_IT.findall(t))
    return e >= 4 and e > 3 * i


def _carica_mappa_img():
    p = BASE / "pagina_studio" / "img" / "mappa.json"
    try:
        import json
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    except Exception:
        return {}


MAPPA_IMG = _carica_mappa_img()   # {id domanda: {"q": [file], "f": [file], "a": [file]}} scaricati dal sito esami


def parse_numbered(path, materia, temi, prefix_prova):
    """Formato '## [id] argomenti: tag' + testo + '1. ' ... '5. ' + RISPOSTA + SPIEGAZIONE (+ ATTENZIONE)."""
    out = []
    if not path.exists():
        return out
    prova = prefix_prova
    for blk in re.split(r"(?m)^(?=#{1,2} )", path.read_text(encoding="utf-8")):
        if blk.startswith("# "):
            prova = prefix_prova if path.name.startswith("banca_") else (blk.splitlines()[0][2:].strip() or prefix_prova)
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
        first = next((i for i, l in enumerate(lines) if re.match(r"^1\.\s", l)), None)
        if first is None:
            continue
        opts = [re.sub(r"^\d\.\s*", "", l).strip() for l in lines[first:] if re.match(r"^\d\.\s", l)]
        if not 2 <= len(opts) <= 8 or not 1 <= int(r.group(1)) <= len(opts):
            continue
        sp = re.search(r"(?ms)SPIEGAZIONE:\s*(.*?)(?=^ATTENZIONE:|\Z)", post)
        at = re.search(r"(?ms)ATTENZIONE:\s*(.*)", post)
        args = [a.strip() for a in m.group(2).split(",") if a.strip()]
        theme = temi(args) if callable(temi) else (temi.get(args[0], args[0]) if args else "Altro")
        out.append(dict(id=m.group(1), m=materia, theme=theme, prova=prova, args=args, q="\n".join(lines[:first]).strip(), o=opts,
                        a=int(r.group(1)), s=(sp.group(1).strip() if sp else ""), w=(at.group(1).strip() if at else "")))
    return out


def solo_it(s):
    """I quiz del sito sono bilingui («🇮🇹 testo 🇬🇧 text»): tiene solo l'italiano."""
    if "🇮🇹" not in s:
        return s.strip()
    def _tieni_formula(m):
        # in alcune domande la formula segue il testo inglese («...table.\(A + B\)»): appartiene a entrambe le lingue, si tiene
        f = re.search(r"(\\\(.*\\\))\s*$", m.group(0), flags=re.S)
        return " " + f.group(1) if f else ""
    return re.sub(r"\s+", " ", re.sub(r"🇬🇧.*?(?=🇮🇹|\Z)", _tieni_formula, s, flags=re.S).replace("🇮🇹", "")).strip()


FIG = re.compile(r"qui sopra|qui sotto|\bsopra\b|seguente circuito|nella figura|in figura|figura|immagine|diagramma|automa (qui|seguente)|tabella (qui|seguente)|seguente (tabella|automa)", re.I)
TEMI_FOND = [  # (tema, espressione): il primo che corrisponde vince
    ("Automi e grammatiche", re.compile(r"automa|grammatica|linguaggi|linguaggio|regolare|derivazion|macchina di turing|stati finiti", re.I)),
    ("Logica avanzata", re.compile(r"implica|→|⟹|⇒|\\to|\\implies|quantific|∀|∃|forall|exists|inferenza|regol[ae] di|dimostr|induzion|invarian|predicat|ipotetic", re.I)),
    ("Logica proposizionale", re.compile(r"logic|tavol[ae] di verit|tautolog|contraddizion|proposizion|equivalen|booleani|connettiv|\bvalid[ao]|\band\b|\bor\b|\bxor\b|negazion|congiunzion|disgiunzion", re.I)),
    ("Rappresentazione binaria", re.compile(r"binar|\bbit\b|complemento|floating|virgola|ottal|esadecim|\bbyte|ascii|unicode|eccesso|mantissa|compress|hamming|parit", re.I)),
    ("Circuiti e memoria", re.compile(r"circuit|porta|nand|\bnor\b|xor|flip|memoria|disco|\bram\b|cache|ssd|\bcd\b|dvd|nastro", re.I)),
    ("Insiemi e relazioni", re.compile(r"insiem|relazion|funzion|sequenz|prodotto cartesiano|partizion", re.I)),
]


def tema_fondamenti(testo, argomenti):
    for tema, rx in TEMI_FOND:
        if rx.search(testo) or rx.search(argomenti):
            return tema
    return "Altro"


def _norm(s):
    return re.sub(r"\s+", " ", s.strip().strip("'\"“”").rstrip(".").strip()).lower()


def parse_fondamenti():
    p = ESAMI / "fondamenti_quiz.md"
    if not p.exists():
        return []
    out = []
    for blk in re.split(r"(?m)^(?=## \[)", p.read_text(encoding="utf-8")):
        m = re.match(r"## \[([^\]]+)\] argomenti: (.*?) \| tipo: (\w+) \| quiz: (.*)", blk.splitlines()[0] if blk.strip() else "")
        if not m or m.group(3) not in ("multichoice", "truefalse"):
            continue
        qid, arg, tipo, quiz = m.groups()
        body = blk.split("\n", 1)[1] if "\n" in blk else ""
        risp = re.search(r"(?m)^RISPOSTA:\s*(.*)$", body)
        spieg = re.search(r"(?ms)^SPIEGAZIONE:\s*(.*?)(?=^## \[|\Z)", body)
        if not risp:
            continue
        pre = body.split("\nRISPOSTA:")[0].splitlines()
        first = next((i for i, l in enumerate(pre) if re.match(r"^- ([a-z]\.\s|Vero$|Falso$)", l)), None)
        if first is None:
            continue
        testo = solo_it("\n".join(pre[:first]).strip())
        opts = [solo_it(re.sub(r"^- ([a-z]\.\s)?", "", l).strip()) for l in pre[first:] if l.startswith("- ")]
        im = MAPPA_IMG.get(qid, {})
        figura = FIG.search(testo) or any(FIG.search(o) for o in opts)
        if len(opts) < 2 or (figura and not im.get("q")) or len(set(opts)) != len(opts) or inglese(testo):
            continue
        hit = [i for i, o in enumerate(opts) if _norm(o) == _norm(solo_it(risp.group(1)))]
        if len(hit) != 1:
            continue
        s = solo_it(spieg.group(1).strip()) if spieg else ""
        s = re.sub(r"\\\(|\\\)", "", s)
        if s.startswith("(nessuna"):
            s = ""
        out.append(dict(id=qid, m="Fondamenti Info", theme=tema_fondamenti(testo + " " + " ".join(opts), arg), prova=titolo_it(quiz), args=[arg.split("(")[0].strip()],
                        q=re.sub(r"\\\(|\\\)", "", testo), o=opts, a=hit[0] + 1, s=s or "Nessuna spiegazione sul sito: la risposta corretta è «" + opts[hit[0]] + "».", w="", img=["img/" + n for n in im.get("q", [])], imgf=["img/" + n for n in im.get("f", [])]))
    return out


def chiave_testo(t):
    """Chiave per collegare una scheda alla domanda del sito da cui deriva (prime parole del testo italiano)."""
    return re.sub(r"[^a-z0-9]+", "", solo_it(re.sub(r"\\\(|\\\)", "", t)).lower())[:70]


def immagini_per_testo():
    """{chiave del testo: (img domanda, img spiegazione)} per le domande del sito che hanno disegni scaricati."""
    out = {}
    p = ESAMI / "fondamenti_quiz.md"
    if not p.exists() or not MAPPA_IMG:
        return out
    for blk in re.split(r"(?m)^(?=## \[)", p.read_text(encoding="utf-8")):
        m = re.match(r"## \[([^\]]+)\]", blk.splitlines()[0] if blk.strip() else "")
        if not m or m.group(1) not in MAPPA_IMG:
            continue
        body = blk.split("\n", 1)[1] if "\n" in blk else ""
        testo = re.split(r"\n- [a-z]\.\s|\n- Vero|\nRISPOSTA:", body)[0]
        im = MAPPA_IMG[m.group(1)]
        out[chiave_testo(testo)] = (["img/" + n for n in im.get("q", [])], ["img/" + n for n in im.get("f", [])])
    return out


def tutte(mate_quiz):
    """Unisce le banche. mate_quiz = lista già letta per Matematica discreta (con theme)."""
    alg = parse_numbered(ESAMI / "banca_algebra.md", "Algebra lineare", TEMI_ALGEBRA, "Esercizi di Algebra lineare")
    prg = parse_numbered(ESAMI / "banca_programmazione.md", "Programmazione", TEMI_PROG, "Esercizi di Programmazione")
    fnd = parse_numbered(ESAMI / "banca_fondamenti.md", "Fondamenti Info", TEMI_FND, "Esercizi di Fondamenti")
    mat = parse_numbered(ESAMI / "banca_mate.md", "Matematica discreta", TEMI_MAT, "Esercizi dai tuoi appunti")
    return mate_quiz + mat + alg + parse_fondamenti() + fnd + prg
