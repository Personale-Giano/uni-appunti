"""Controllo automatico delle bozze dei riassunti (e dei contenuti già sul sito).

Nato dalla rilettura del 3 nov 2026, che ha trovato nei capitoli pubblicati formule troncate, `\\n` del C
diventati a capo, tilde mangiate dal corsivo, asterischi markdown, «questo Word» e rimandi a capitoli tolti.

Uso:
    python lint_bozza.py <materia> bozza.md       controlla una bozza (lo fa già aggiungi_capitolo_sito.py)
    python lint_bozza.py --contenuti               controlla tutti i contenuti del sito (solo avvisi)
Errori = da correggere prima di inserire; avvisi = da guardare.
"""
import html
import json
import re
import sys
from pathlib import Path

REPO = Path.home() / "Documents" / "GitHub" / "quaderno-privato"
MATERIE = ("algebra", "matematica-discreta", "fondamenti", "programmazione", "laboratorio")

MD_CORSIVO = re.compile(r"(?<![*\w\\])\*(?!\s)[^*\n]{1,40}?(?<![\s\\])\*(?![*\w])")
META = re.compile(r"\bNotebookLM\b|\ble fonti (?:dicono|forniscono|riportano)|\bnell'audio\b|\bnel documento\b|come detto nell", re.I)
WORD = re.compile(r"(?<!\()\bWord\b(?! Processing)(?!\))(?<!Microsoft Word)")
FINE_SOSPESA = re.compile(r"(?:=|≡|⟹|⟺|→|\+|−|-|·)\s*$")
SPAZIO_PUNT = re.compile(r"\S\s{2,}[,.;:]|\s[,;](?=\s*[,;])")
RIMANDO = re.compile(r"\b(?:capitol[oi]|cap\.)\s+(\d+)\b", re.I)


def testo(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h))


def virgolette_dispari(riga_c):
    """Riga di codice C con un numero dispari di virgolette: tipico di un \\n diventato a capo."""
    s = re.sub(r"//.*", "", riga_c)
    s = re.sub(r"'(?:\\.|[^'\\])'", "", s)
    s = s.replace('\\"', "")
    return s.count('"') % 2 == 1


def righe_bozza(src):
    """(numero riga, testo, dentro_codice)"""
    dentro = False
    for i, r in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
        if r.lstrip().startswith("```"):
            dentro = not dentro
            continue
        yield i, r, dentro


def controlla_blocco(b, slug):
    """Controlli sul testo convertito di un blocco (servono sia per le bozze sia per il sito)."""
    err, avv = [], []
    if "h" not in b:
        return err, avv
    t = testo(b["h"])
    dove = b.get("b", "?")
    if b["t"] == "pre":
        for r in t.split("\n"):
            if virgolette_dispari(r):
                err.append(f"{dove}: riga di codice con virgolette spaiate (un \\n diventato a capo?): {r.strip()[:60]}")
        return err, avv
    t = testo(re.sub(r"<code>.*?</code>", "▯", b["h"]))  # il codice in linea non si controlla come testo
    if "**" in t:
        err.append(f"{dove}: «**» rimasto nel testo")
    if re.search(r"[\^_]\{", t):
        err.append(f"{dove}: apice/pedice non convertito: …{t[max(0, t.find('{') - 15):t.find('{') + 15]}…")
    if MD_CORSIVO.search(t):
        err.append(f"{dove}: corsivo markdown con asterischi: {MD_CORSIVO.search(t).group(0)} (si scrive ~parola~)")
    if b["t"] in ("p", "li") and FINE_SOSPESA.search(t) and not t.rstrip().endswith(":"):
        err.append(f"{dove}: il paragrafo finisce con «{t.rstrip()[-3:]}»: formula troncata?")
    if SPAZIO_PUNT.search(t):
        err.append(f"{dove}: spazio vuoto prima della punteggiatura (simbolo o formula sparita?): …{SPAZIO_PUNT.search(t).group(0)}…")
    if WORD.search(t):
        err.append(f"{dove}: parla del «Word» (i riassunti ora sono sul sito)")
    if META.search(t):
        err.append(f"{dove}: frase di cornice da evitare: «{META.search(t).group(0)}»")
    if t.count("~") % 2:
        avv.append(f"{dove}: tilde isolata nel testo: è voluta?")
    return err, avv


def controlla(src, slug, blocks, dati, repo=REPO):
    """Bozza + blocchi già convertiti -> (errori, avvisi)."""
    err, avv = [], []
    for i, r, dentro in righe_bozza(src):
        if dentro:
            continue
        s = re.sub(r"`[^`]*`", "", r.replace("\\*", ""))
        if s.count("**") % 2:
            err.append(f"riga {i}: «**» spaiato")
        if MD_CORSIVO.search(s.replace("**", "")):
            err.append(f"riga {i}: corsivo con asterischi singoli ({MD_CORSIVO.search(s.replace('**', '')).group(0)}): usa ~parola~")
        if any(re.search(r"\*\*|~\S|\^\{|_\{", span) for span in re.findall(r"`([^`]*)`", r)):
            avv.append(f"riga {i}: marcatori dentro i backtick: restano letterali")
    for b in blocks:
        e, a = controlla_blocco(b, slug)
        err += e
        avv += a
    # rimandi ad altri capitoli: devono esistere (per il laboratorio i numeri sono spesso quelli della teoria)
    esistenti = {c["num"] for c in dati["capitoli"]}
    nuovo = max(esistenti or {0}) + 1
    for b in blocks:
        for m in RIMANDO.finditer(testo(b.get("h", ""))):
            n = int(m.group(1))
            if n not in esistenti and n > nuovo + 3 and slug != "laboratorio":
                avv.append(f"{b['b']}: rimanda al capitolo {n}, che non esiste")
    testo_tutto = " ".join(testo(b.get("h", "")) for b in blocks)
    if re.search(r"\bil (?:prossimo capitolo|capitolo successivo)\b", testo_tutto, re.I):
        avv.append("annuncia «il prossimo capitolo»: controlla che parli davvero dell'argomento seguente")
    # stile: definizioni con la loro spiegazione «In parole povere», elenchi non dominanti
    n_def = sum(1 for b in blocks if b["t"] in ("p", "li") and re.match(r"\s*(?:<[^>]+>)*\s*(Definizione|Teorema|Proposizione)\b", b.get("h", "")))
    n_pp = sum(1 for b in blocks if b.get("c") == "pp")
    if n_def > n_pp:
        avv.append(f"{n_def} definizioni/teoremi ma {n_pp} riquadri «In parole povere» (STILE.md: uno dopo ogni definizione)")
    testuali = [b for b in blocks if b["t"] in ("p", "li")]
    if testuali:
        quota = sum(b["t"] == "li" for b in testuali) / len(testuali)
        if quota > 0.6:
            avv.append(f"elenchi puntati al {quota:.0%} dei paragrafi (mediana dei capitoli ≈ 44%): più discorsivo")
    return err, avv


def controlla_contenuti(repo=REPO):
    """Scansione di tutti i capitoli del sito: righe 'materia blocco problema' (con 'evidenziato' se lo è)."""
    evid = {}
    f = Path(__file__).resolve().parent.parent / "evid_export.json"
    if f.exists():
        evid = json.loads(f.read_text(encoding="utf-8")).get("evid", {})
    out = []
    for slug in MATERIE:
        fj = repo / "contenuti" / f"{slug}.json"
        if not fj.exists():
            continue
        for c in json.loads(fj.read_text(encoding="utf-8"))["capitoli"]:
            for b in c["blocks"]:
                e, _a = controlla_blocco(b, slug)
                for x in e:
                    nota = " [evidenziato: lasciare]" if evid.get(slug, {}).get(b.get("b")) else ""
                    out.append(f"{slug} {x}{nota}")
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) >= 2 and sys.argv[1] == "--contenuti":
        righe = controlla_contenuti()
        print("\n".join(righe) if righe else "Contenuti del sito: nessun problema trovato.")
        return
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from aggiungi_capitolo_sito import ALIAS, blocchi_da_bozza  # noqa: E402
    slug = ALIAS.get(sys.argv[1].lower(), sys.argv[1].lower())
    src = Path(sys.argv[2])
    dati = json.loads((REPO / "contenuti" / f"{slug}.json").read_text(encoding="utf-8"))
    _t, blocks = blocchi_da_bozza(src, REPO, "capX", prova=True)
    err, avv = controlla(src, slug, blocks, dati)
    for x in avv:
        print("AVVISO:", x)
    for x in err:
        print("ERRORE:", x)
    print(f"{len(err)} errori, {len(avv)} avvisi")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
