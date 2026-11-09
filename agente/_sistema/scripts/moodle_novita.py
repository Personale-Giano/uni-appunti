"""Novità sui corsi Moodle di Emanuele, con l'API ufficiale (la stessa dell'app Moodle), senza browser.

Uso:
    python moodle_novita.py            # confronta con l'ultimo controllo e scrive _sistema/moodle_novita.md
    python moodle_novita.py --prova    # controlla solo che il token funzioni

Il token NON sta nel repository (che è pubblico). Si legge, in quest'ordine, da:
  - la variabile d'ambiente MOODLE_TOKEN
  - il file C:\\Users\\<utente>\\.moodle_unito_token (una riga, solo il token)
Si ottiene così: accedere una volta all'app Moodle sul telefono (sito informatica.i-learn.unito.it),
poi dal sito, menu utente > Preferenze > Chiavi di sicurezza, copiare la chiave «Moodle mobile web service».

Sola lettura: elenca file nuovi o modificati, attività nuove, testi delle sezioni cambiati (per esempio i resoconti
delle lezioni di Fondamenti) e discussioni nuove nei forum. Non scarica nulla.
Lo stato dell'ultimo controllo sta in _sistema/moodle_api_stato.json (escluso da git; moodle_stato.json è del controllo manuale dal browser, non toccarlo).
"""
import argparse
import hashlib
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

SITO = "https://informatica.i-learn.unito.it"
CORSI = {
    3831: "Algebra lineare",
    3829: "Matematica discreta",
    3747: "Fondamenti",
    3773: "Programmazione",
}
BASE = Path(__file__).resolve().parent.parent
STATO = BASE / "moodle_api_stato.json"
RAPPORTO = BASE / "moodle_novita.md"


def token() -> str:
    t = os.environ.get("MOODLE_TOKEN", "").strip()
    f = Path.home() / ".moodle_unito_token"
    if not t and f.exists():
        t = f.read_text(encoding="utf-8").strip()
    if not t:
        sys.exit(f"Manca il token: mettilo in {f} (vedi l'intestazione dello script).")
    return t


def chiama(tok: str, funzione: str, **parametri):
    dati = {"wstoken": tok, "wsfunction": funzione, "moodlewsrestformat": "json"}
    for k, v in parametri.items():
        if isinstance(v, list):
            for i, x in enumerate(v):
                dati[f"{k}[{i}]"] = x
        else:
            dati[k] = v
    req = urllib.request.Request(
        f"{SITO}/webservice/rest/server.php",
        data=urllib.parse.urlencode(dati).encode(),
        headers={"User-Agent": "uni-appunti-moodle-novita"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        risposta = json.loads(r.read().decode("utf-8"))
    if isinstance(risposta, dict) and risposta.get("exception"):
        raise RuntimeError(f"{funzione}: {risposta.get('errorcode')} - {risposta.get('message')}")
    return risposta


def testo(h: str) -> str:
    """HTML -> testo semplice, una riga per paragrafo."""
    h = re.sub(r"(?i)<br\s*/?>|</p>|</li>|</div>|</h\d>", "\n", h or "")
    t = html.unescape(re.sub(r"<[^>]+>", "", h))
    return "\n".join(r.strip() for r in t.splitlines() if r.strip())


def impronta(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]


def fotografia(tok: str) -> dict:
    """Stato attuale dei corsi: moduli, file, testi delle sezioni, discussioni dei forum."""
    foto = {}
    for cid, nome in CORSI.items():
        c = {"moduli": {}, "sezioni": {}, "discussioni": {}}
        for sez in chiama(tok, "core_course_get_contents", courseid=cid):
            if not sez.get("visible", 1):
                continue
            t = testo(sez.get("summary", ""))
            if t:
                c["sezioni"][str(sez["id"])] = {"nome": sez.get("name", ""), "testo": t, "h": impronta(t)}
            for m in sez.get("modules", []):
                if not m.get("visible", 1) or not m.get("uservisible", True):
                    continue
                desc = testo(m.get("description", ""))
                file = {
                    f["filename"]: {"dim": f.get("filesize"), "mod": f.get("timemodified"), "url": f.get("fileurl", "")}
                    for f in m.get("contents", []) if f.get("type") == "file"
                }
                c["moduli"][str(m["id"])] = {
                    "nome": m.get("name", ""), "tipo": m.get("modname", ""), "sezione": sez.get("name", ""),
                    "url": m.get("url", ""), "file": file, "desc": desc, "hdesc": impronta(desc),
                }
        for forum in chiama(tok, "mod_forum_get_forums_by_courses", courseids=[cid]):
            try:
                r = chiama(tok, "mod_forum_get_forum_discussions", forumid=forum["id"], sortorder=1, page=0, perpage=20)
            except RuntimeError:  # Moodle più vecchi
                r = chiama(tok, "mod_forum_get_forum_discussions_paginated", forumid=forum["id"], page=0, perpage=20)
            for d in r.get("discussions", []):
                c["discussioni"][str(d["discussion"])] = {
                    "forum": forum.get("name", ""), "titolo": d.get("name", ""),
                    "autore": d.get("userfullname", ""), "data": d.get("created") or d.get("timemodified"),
                    "testo": testo(d.get("message", ""))[:600],
                }
        foto[str(cid)] = c
    return foto


def data(ts) -> str:
    return datetime.fromtimestamp(ts).strftime("%d/%m/%Y %H:%M") if ts else "?"


def confronta(prima: dict, ora: dict) -> list:
    righe = []
    for cid, nome in CORSI.items():
        p, o = prima.get(str(cid), {}), ora[str(cid)]
        voci = []
        for mid, m in o["moduli"].items():
            vecchio = p.get("moduli", {}).get(mid)
            if vecchio is None:
                voci.append(f"- **Nuovo** ({m['tipo']}, {m['sezione']}): {m['nome']} {m['url']}")
                continue
            for fn, f in m["file"].items():
                vf = vecchio["file"].get(fn)
                if vf is None:
                    voci.append(f"- **File nuovo** in «{m['nome']}»: {fn} ({f['dim']} byte)")
                elif (vf["dim"], vf["mod"]) != (f["dim"], f["mod"]):
                    voci.append(f"- **File modificato** in «{m['nome']}»: {fn} ({vf['dim']} → {f['dim']} byte, {data(f['mod'])})")
            if vecchio.get("hdesc") != m["hdesc"] and m["desc"]:
                voci.append(f"- **Descrizione cambiata** in «{m['nome']}»: {m['desc'][:300]}")
        for sid, s in o["sezioni"].items():
            vs = p.get("sezioni", {}).get(sid)
            if vs is None or vs["h"] != s["h"]:
                nuove = [r for r in s["testo"].splitlines() if r not in (vs["testo"].splitlines() if vs else [])]
                if nuove:
                    voci.append(f"- **Testo nuovo** nella sezione «{s['nome'] or 'generale'}»:\n  > " + "\n  > ".join(nuove)[:1500])
        for did, d in o["discussioni"].items():
            if did not in p.get("discussioni", {}):
                voci.append(f"- **Annuncio** ({d['forum']}, {d['autore']}, {data(d['data'])}): {d['titolo']}\n  > {d['testo'][:400]}")
        if voci:
            righe += [f"## {nome}", *voci, ""]
    return righe


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prova", action="store_true", help="controlla solo il token")
    args = ap.parse_args()
    tok = token()
    try:
        info = chiama(tok, "core_webservice_get_site_info")
    except RuntimeError as e:
        sys.exit(f"Il token non funziona ({e}). Copialo di nuovo da Preferenze > Chiavi di sicurezza.")
    print(f"Token valido per {info.get('fullname')} su {info.get('sitename')} (Moodle {info.get('release', '?')}).")
    if args.prova:
        return
    ora = fotografia(tok)
    adesso = datetime.now().strftime("%d/%m/%Y %H:%M")
    if not STATO.exists():
        n = sum(len(c["moduli"]) for c in ora.values())
        testo_rapporto = f"# Novità su Moodle ({adesso})\n\nPrimo controllo: memorizzati {n} elementi dei 4 corsi. Le novità compariranno dal prossimo controllo.\n"
    else:
        prima = json.loads(STATO.read_text(encoding="utf-8"))
        righe = confronta(prima, ora)
        testo_rapporto = f"# Novità su Moodle ({adesso})\n\n" + ("\n".join(righe) if righe else "Nessuna novità dall'ultimo controllo.\n")
    STATO.write_text(json.dumps(ora, ensure_ascii=False, indent=1), encoding="utf-8")
    RAPPORTO.write_text(testo_rapporto, encoding="utf-8")
    print(testo_rapporto)


if __name__ == "__main__":
    main()
