r"""Aggiunge un capitolo (scritto in una bozza .md) ai riassunti del sito: da quando i Word non si usano più, i contenuti
stanno in <repo sito>/contenuti/<materia>.json e le pagine si costruiscono da lì (pubblica_quaderno.py).

Uso:
    python aggiungi_capitolo_sito.py <materia> bozza.md [--dry-run] [--repo CARTELLA_SITO]
    materia: algebra | matematica-discreta (o mate) | fondamenti | programmazione | laboratorio

Sintassi della bozza (la stessa di prima):
    # N. Titolo            (Programmazione/Laboratorio: # Capitolo N: Titolo)
    ## sottotitolo
    - elenco puntato
    una riga = un paragrafo; "(In parole povere: ...)" diventa il riquadro verde
    **grassetto**   ~corsivo~   `codice`   ^{apice}   _{pedice}   (\* = * letterale, \~ = ~ letterale)
    ```  blocchi di codice  ```
    ![didascalia](figure/percorso.png|larghezza_cm)     (percorso relativo a _sistema/)
    Il corsivo vuole la tilde attaccata al testo (~parola~); una tilde isolata resta un carattere.
    Dentro `codice` i marcatori non valgono. *asterischi singoli* NON sono corsivo: il controllo li blocca.
Prima di scrivere la bozza passa da lint_bozza.py (si scavalca con --forza); il testo convertito si vede con --anteprima.
Le evidenziazioni non si toccano: un capitolo nuovo parte senza evidenziazioni.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from migra_word import html_parti, numero, riquadro_pp, testo  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
REPO = Path.home() / "Documents" / "GitHub" / "quaderno-privato"
ALIAS = {"mate": "matematica-discreta", "matematica": "matematica-discreta", "matematica discreta": "matematica-discreta",
         "algebra lineare": "algebra", "fondamenti info": "fondamenti", "lab": "laboratorio"}
STAR, TILDE, I_ON, I_OFF = "\x00", "\x03", "\x01", "\x02"
# apici e pedici con un livello di graffe annidate (es. Σ_{σ ∈ S_{n}}); l'interno si appiattisce
TOKEN = re.compile(r"(\*\*|\x01|\x02|[\^_]\{(?:[^{}]|\{[^{}]*\})*\})")
NESTED = re.compile(r"[\^_]\{([^{}]*)\}")
# corsivo: tilde attaccata al testo da entrambi i lati; una tilde isolata ("la tilde ~;") resta un carattere
ITAL = re.compile(r"~(?=\S)([^~]*?\S)~")


def _letterale(s):
    return s.replace(STAR, "*").replace(TILDE, "~")


def parti_da_testo(riga):
    """Testo con marcatori -> parti con gli stessi campi dei Word (b, i, sup, sub, code).
    Il codice tra backtick si separa prima: dentro non valgono grassetto, corsivo, apici e pedici."""
    b = i = False
    parts = []
    pezzi = riga.replace("\\*", STAR).replace("\\~", TILDE).split("`")
    if len(pezzi) % 2 == 0:
        raise ValueError(f"backtick non chiuso: {riga[:80]}")
    for k, pezzo in enumerate(pezzi):
        if k % 2:
            if pezzo:
                parts.append({"t": _letterale(pezzo), "b": b, "i": i, "sup": False, "sub": False, "code": True, "mk": False})
            continue
        pezzo = ITAL.sub(lambda m: I_ON + m.group(1) + I_OFF, pezzo)
        for tok in TOKEN.split(pezzo):
            if not tok:
                continue
            if tok == "**":
                b = not b; continue
            if tok == I_ON:
                i = True; continue
            if tok == I_OFF:
                i = False; continue
            sup, sub = tok.startswith("^{"), tok.startswith("_{")
            corpo = NESTED.sub(r"\1", tok[2:-1]) if (sup or sub) else tok
            parts.append({"t": _letterale(corpo), "b": b, "i": i, "sup": sup, "sub": sub, "code": False, "mk": False})
    return parts


CONT = "contenuti"  # cartella dei contenuti nel repo; con --spazio diventa spazi_contenuti/<nome>


def figura(percorso, larg_cm, repo, prova=False):
    img = Path(percorso)
    if not img.is_absolute():
        img = BASE / img
    if not img.exists():
        sys.exit(f"Figura non trovata: {img}")
    blob = img.read_bytes()
    nome = hashlib.sha1(blob).hexdigest()[:14] + img.suffix.lower()
    if not prova:  # con --dry-run/--anteprima non si copia niente nel repo del sito
        dest = repo / CONT / "img"
        dest.mkdir(parents=True, exist_ok=True)
        (dest / nome).write_bytes(blob)
    from PIL import Image
    with Image.open(img) as im:
        w, h = im.size
    px = int(round(float(larg_cm or 11) * 96 / 2.54))
    return {"t": "fig", "src": nome, "w": px, "cx": w, "cy": h}


def blocchi_da_bozza(src, repo, cap_id, prova=False):
    out, n = [], 0
    in_code, codice = False, []

    def nuovo():
        nonlocal n
        n += 1
        return f"{cap_id}.{n}"

    titolo = None
    for raw in src.read_text(encoding="utf-8").splitlines():
        riga = raw.rstrip()
        if riga.lstrip().startswith("```"):
            if in_code and codice:
                out.append({"t": "pre", "b": nuovo(), "h": chr(10).join(html_parti(parti_da_testo_codice(r), codice=False) for r in codice)})
                codice = []
            in_code = not in_code
            continue
        if in_code:
            codice.append(raw.rstrip(chr(10)))
            continue
        if not riga.strip():
            continue
        m = re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", riga.strip())
        if m:
            didascalia, spec = m.group(1).strip(), m.group(2).strip()
            percorso, _, larg = spec.partition("|")
            f = figura(percorso, larg.strip(), repo, prova)
            if didascalia:
                f["cap"] = didascalia
            out.append(f)
            continue
        if riga.startswith(("## ", "### ", "#### ")):
            liv = "h5" if riga.startswith("#### ") else ("h4" if riga.startswith("### ") else "h3")   # ### e #### = sottolivelli
            parts = parti_da_testo(riga.lstrip("#").strip())
            neutri = [{**p, "b": False, "i": False, "code": False} for p in parts]
            out.append({"t": liv, "b": nuovo(), "h": html_parti(neutri)})
        elif riga.startswith("# "):
            titolo = riga[2:].strip()
        elif re.match(r"^\s*[-*] ", riga):
            parts = parti_da_testo(re.sub(r"^\s*[-*] ", "", riga))
            out.append({"t": "li", "b": nuovo(), "h": html_parti(parts), "k": "ul", "l": 0})
        else:
            parts = parti_da_testo(riga.strip())
            pp = riquadro_pp(parts)
            blk = {"t": "p", "b": nuovo(), "h": html_parti(parts)}
            if pp:
                blk["c"] = "pp"
            out.append(blk)
    if in_code:
        sys.exit("Blocco di codice ``` non chiuso in fondo alla bozza: il codice andrebbe perso")
    return titolo, out


def parti_da_testo_codice(riga):
    return [{"t": riga, "b": False, "i": False, "sup": False, "sub": False, "code": True, "mk": False}]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("materia")
    ap.add_argument("bozza")
    ap.add_argument("--repo", default=str(REPO))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--anteprima", action="store_true", help="stampa il testo convertito dei blocchi (da dare al revisore) senza scrivere")
    ap.add_argument("--forza", action="store_true", help="inserisce anche se lint_bozza.py trova errori")
    ap.add_argument("--spazio", help="spazio separato (es. nome dello spazio): contenuti in spazi_contenuti/<spazio>/; la materia deve essere in spazio.json")
    ap.add_argument("--sostituisci", action="store_true", help="rimpiazza un capitolo già sul sito, solo se non ha evidenziazioni (export recente, meno di 30 minuti)")
    a = ap.parse_args()
    slug = ALIAS.get(a.materia.lower(), a.materia.lower())
    repo = Path(a.repo)
    global CONT
    if a.spazio:
        CONT = f"spazi_contenuti/{a.spazio}"
        conf = json.loads((repo / CONT / "spazio.json").read_text(encoding="utf-8"))
        mat = next((m for m in conf.get("materie", []) if m["slug"] == slug), None)
        if not mat:
            sys.exit(f"La materia {slug} non è in {CONT}/spazio.json")
        if a.sostituisci:  # le evidenziazioni degli spazi non sono nell'export: niente sostituzioni automatiche
            sys.exit("--sostituisci non è disponibile negli spazi: le evidenziazioni non sarebbero controllate")
    fj = repo / CONT / f"{slug}.json"
    if a.spazio and not fj.exists() and not (a.dry_run or a.anteprima):
        fj.write_text(json.dumps({"slug": slug, "nome": mat["nome"], "chiave": mat["nome"], "preambolo": [], "capitoli": []},
                                 ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"creato {fj}")
    if not fj.exists() and a.spazio:
        dati_vuoti = {"capitoli": []}
    elif not fj.exists():
        sys.exit(f"Materia sconosciuta o contenuti mancanti: {fj}")
    src = Path(a.bozza)
    if not src.exists():
        sys.exit(f"Bozza non trovata: {src}")
    dati = json.loads(fj.read_text(encoding="utf-8")) if fj.exists() else dati_vuoti
    # titolo e numero dalla prima riga "# "
    prima = next((r for r in src.read_text(encoding="utf-8").splitlines() if r.startswith("# ")), None)
    if not prima:
        sys.exit("La bozza deve iniziare con '# N. Titolo'")
    titolo = re.sub(r"\s+", " ", prima[2:]).strip()
    n = numero(titolo)
    if n is None:
        sys.exit("Il titolo deve avere il numero del capitolo (es. '# 29. Titolo' o '# Capitolo 23: Titolo')")
    cap_id = f"cap{n}"
    esiste = any(c["num"] == n for c in dati["capitoli"])
    if esiste and not a.sostituisci:
        sys.exit(f"Esiste già il capitolo {n} in {slug}: scegli il numero successivo (ultimo: {max(c['num'] for c in dati['capitoli'] if c['num'])})")
    if esiste:  # le evidenziazioni sono intervalli di caratteri: un capitolo evidenziato non si riscrive
        fe = BASE / "evid_export.json"
        if time.time() - fe.stat().st_mtime > 1800:
            sys.exit("evid_export.json ha più di 30 minuti: prima `node scripts/esporta_evid.js` nel repo del sito")
        ev = json.loads(fe.read_text(encoding="utf-8"))["evid"].get(slug, {})
        if any(k.startswith(cap_id + ".") for k in ev):
            sys.exit(f"Il capitolo {n} ha evidenziazioni: non si può sostituire")
    prova = a.dry_run or a.anteprima
    try:
        _t, blocks = blocchi_da_bozza(src, repo, cap_id, prova)
    except ValueError as e:
        sys.exit(f"Bozza non convertibile: {e}")
    from lint_bozza import controlla  # noqa: E402
    errori, avvisi = controlla(src, slug, blocks, dati, repo)
    for x in avvisi:
        print("AVVISO:", x)
    for x in errori:
        print("ERRORE:", x)
    if a.anteprima:
        import html as _h
        for b in blocks:
            if "h" in b:
                print(f"[{b['b']} {b['t']}] " + _h.unescape(re.sub(r"<[^>]+>", "", b["h"])))
            else:
                print(f"[figura] {b.get('cap', '')}")
        return
    n_hl = sum(1 for b in blocks if b["t"] in ("p", "li", "pre"))
    if a.dry_run:
        print(f"[dry-run] aggiungerei il capitolo {n} «{titolo}» a {slug}: {len(blocks)} blocchi ({n_hl} di testo), {len(errori)} errori")
        return
    if errori and not a.forza:
        sys.exit(f"{len(errori)} errori nella bozza: correggili (o rilancia con --forza se sono voluti)")
    bk = BASE / "backup"
    bk.mkdir(exist_ok=True)
    shutil.copy2(fj, bk / f"{(a.spazio + '_') if a.spazio else ''}{slug}_contenuti_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    nuovo_cap = {"id": cap_id, "num": n, "titolo": titolo, "blocks": blocks}
    if esiste:
        dati["capitoli"] = [nuovo_cap if c["num"] == n else c for c in dati["capitoli"]]
    else:
        dati["capitoli"].append(nuovo_cap)
        if a.spazio:  # negli spazi i capitoli seguono il libro e possono arrivare in ordine sparso
            dati["capitoli"].sort(key=lambda c: c["num"] or 0)
    # stesso formato del file originale (fondamenti.json è indentato, gli altri compatti): diff piccoli
    indentato = fj.read_text(encoding="utf-8").startswith("{\n")
    fj.write_text(json.dumps(dati, ensure_ascii=False, indent=2, separators=(",", ": ")) if indentato
                  else json.dumps(dati, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"OK: capitolo {n} «{titolo}» aggiunto a {slug} ({len(blocks)} blocchi). Ora: python pubblica_quaderno.py --push")


if __name__ == "__main__":
    main()
