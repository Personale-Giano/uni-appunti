"""Inserisce blocchi NUOVI in capitoli già sul sito senza toccare i blocchi esistenti.

Serve per i capitoli con evidenziazioni (che --sostituisci rifiuta): le evidenziazioni sono legate
all'id del blocco (capN.K) e a intervalli di caratteri dentro il blocco, quindi aggiungere blocchi con
id nuovi (dopo l'ultimo usato nel capitolo) non le sposta. Nessun blocco esistente viene modificato.

Uso:
    python inserisci_blocchi_sito.py <materia> <file.md> [--anteprima] [--spazio <nome>]

Formato del file: una o più sezioni, ciascuna introdotta da una riga
    @@ dopo capN.K
seguita dal testo nella sintassi delle bozze (## titoli, - elenchi, **grassetto**, ``` codice ...).
I blocchi della sezione vengono inseriti subito dopo il blocco capN.K.
"""
import argparse
import html
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import aggiungi_capitolo_sito as m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("materia")
    ap.add_argument("file")
    ap.add_argument("--anteprima", action="store_true")
    ap.add_argument("--spazio", help="spazio separato: contenuti in spazi_contenuti/<spazio>/")
    a = ap.parse_args()
    slug = m.ALIAS.get(a.materia.lower(), a.materia.lower())
    repo = Path(m.REPO)
    if a.spazio:
        m.CONT = f"spazi_contenuti/{a.spazio}"  # anche le figure vanno nella cartella img dello spazio
    fj = repo / m.CONT / f"{slug}.json"
    raw = fj.read_text(encoding="utf-8")
    dati = json.loads(raw)
    sezioni, cur = [], None
    for riga in Path(a.file).read_text(encoding="utf-8").splitlines():
        mm = re.match(r"@@ dopo (cap(\d+)\.\d+)\s*$", riga)
        if mm:
            cur = {"dopo": mm.group(1), "n": int(mm.group(2)), "righe": []}
            sezioni.append(cur)
        elif cur is not None:
            cur["righe"].append(riga)
        elif riga.strip():
            sys.exit("Testo prima della prima riga '@@ dopo capN.K'")
    if not sezioni:
        sys.exit("Nessuna sezione")
    tot = 0
    for s in sezioni:
        cap = next((c for c in dati["capitoli"] if c["num"] == s["n"]), None)
        if cap is None:
            sys.exit(f"Capitolo {s['n']} non trovato")
        ids = [b.get("b") for b in cap["blocks"]]
        if s["dopo"] not in ids:
            sys.exit(f"Blocco {s['dopo']} non trovato")
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "pezzo.md"
            tmp.write_text(f"# {s['n']}. x\n" + "\n".join(s["righe"]).strip("\n") + "\n", encoding="utf-8")
            _t, nuovi = m.blocchi_da_bozza(tmp, repo, f"cap{s['n']}", a.anteprima)
        ultimo = max(int(i.split(".")[1]) for i in ids if i)
        for b in nuovi:
            if "b" in b:
                ultimo += 1
                b["b"] = f"cap{s['n']}.{ultimo}"
        k = ids.index(s["dopo"]) + 1
        cap["blocks"][k:k] = nuovi
        tot += len(nuovi)
        print(f"--- {cap['titolo']} | dopo {s['dopo']}")
        for b in nuovi:
            if "h" in b:
                print(f"[{b['b']} {b['t']}{' ' + b['c'] if b.get('c') else ''}] " + html.unescape(re.sub(r"<[^>]+>", "", b["h"])))
            else:
                print("[figura]")
    if a.anteprima:
        return
    bk = m.BASE / "backup"
    bk.mkdir(exist_ok=True)
    shutil.copy2(fj, bk / f"{(a.spazio + '_') if a.spazio else ''}{slug}_contenuti_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    indentato = raw.startswith("{\n")
    fj.write_text(json.dumps(dati, ensure_ascii=False, indent=2, separators=(",", ": ")) if indentato
                  else json.dumps(dati, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"OK: {tot} blocchi nuovi in {slug}. Ora: python pubblica_quaderno.py --push")


if __name__ == "__main__":
    main()
