"""Dati della homepage (Quaderno di ripasso: Oggi, Quiz, Domande, Schede) di uno spazio separato.

Legge da spazi_contenuti/<nome>/:
  spazio.json                      materie dello spazio
  <slug>.json                      riassunti (capitoli e blocchi): da qui schede, domande aperte, avanzamento
  quiz/<slug>_capNN.md             quiz a scelta multipla (formato in ISTRUZIONI_QUIZ.md)
Scrive <uscita>/data.json nello stesso formato del Quaderno principale (costruisci_pagina_studio.py), così la stessa app lo legge.

Uso: python costruisci_quaderno_spazio.py <cartella_spazio> <cartella_uscita>
Stampa una riga JSON con mats/rslug/sim, che pubblica_quaderno.py usa per adattare la pagina.
"""
import html as H
import json
import re
import sys
from datetime import date
from pathlib import Path

ETICHETTA = re.compile(r"^\s*<strong>\s*(Definizione|Teoria|Legge|Esperimento)\b\s*(\(([^)<]{1,80})\))?\s*[.:]?\s*</strong>\s*[.:]?\s*", re.I)
_SUP = str.maketrans("0123456789+-−n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻ⁿ")
_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def testo(h):
    h = re.sub(r"<sup>([^<]*)</sup>", lambda m: m.group(1).translate(_SUP) if all(c in "0123456789+-−n" for c in m.group(1)) else "^(" + m.group(1) + ")", h)
    h = re.sub(r"<sub>([^<]*)</sub>", lambda m: m.group(1).translate(_SUB) if m.group(1).isdigit() else "_" + m.group(1), h)
    h = re.sub(r"</?strong>", "**", h)
    return H.unescape(re.sub(r"<[^>]+>", "", h)).strip()


def senza_num(t):
    return re.sub(r"^\s*(?:Capitolo\s+)?\d+\s*[.:]?\s*", "", t)


def tema(c):
    return f"Cap. {c['num']} · {senza_num(c['titolo'])}"


def schede(mat, slug, caps):
    out = []
    for c in caps:
        sezione = senza_num(c["titolo"])
        bl = c["blocks"]
        for i, b in enumerate(bl):
            if b["t"] in ("h3", "h4", "h5"):
                sezione = testo(b["h"]).replace("**", "")
                continue
            m = ETICHETTA.match(b.get("h", "")) if b["t"] in ("p", "li") else None
            if not m:
                continue
            tipo, nome = m.group(1).capitalize(), (m.group(3) or "").strip()
            corpo = testo(b["h"][m.end():])
            risposta = [corpo]
            for nb in bl[i + 1:i + 7]:
                if nb["t"] not in ("p", "li") or "h" not in nb or ETICHETTA.match(nb["h"]):
                    break
                t = testo(nb["h"])
                if nb.get("c") == "pp":
                    risposta.append("In parole povere: " + re.sub(r"^\(?In parole povere:\s*", "", t).rstrip(")"))
                    break
                if nb["t"] == "li":
                    risposta.append("- " + t)
                elif tipo == "Esperimento":
                    break
                else:
                    break
            if tipo == "Definizione":
                term = re.search(r"\*\*([^*]{2,70})\*\*", corpo)
                if not term:
                    continue
                d = f"Che cosa si intende per {term.group(1).strip()}?"
            elif tipo == "Esperimento":
                d = f"L'esperimento di {nome}: che cosa voleva capire, come si è svolto, che cosa è risultato e perché è importante?" if nome else "Descrivi l'esperimento: domanda, procedura, risultato."
            else:
                d = f"{tipo} {('«' + nome + '»') if nome else ''}: che cosa sostiene?".replace("  ", " ")
            r = "\n".join(x for x in risposta if x)
            out.append(dict(id=f"{slug[:3]}-{b['b'].replace('.', '-')}", m=mat, t=f"Cap. {c['num']} · {sezione}", d=d, r=r,
                            lungo=len(r) > 400, da_quiz=False, auto=True))
    return out


def domande_aperte(mat, slug, caps):
    out = []
    for c in caps:
        dentro = False
        for b in c["blocks"]:
            if b["t"] in ("h3", "h4", "h5"):
                dentro = testo(b["h"]).startswith("Domande di ripasso")
                continue
            if not dentro or b["t"] != "li":
                continue
            m = re.match(r"^\s*<strong>(.*?)</strong>\s*(.*)$", b["h"], re.S)
            if not m:
                continue
            out.append(dict(id=f"{slug[:3]}-dom-{b['b'].replace('.', '-')}", m=mat, args=[f"{slug}:cap{c['num']}"],
                            testo=testo(m.group(1)), soluzione=testo(m.group(2)), concetti=""))
    return out


def quiz(mat, slug, cartella):
    out = []
    for f in sorted((cartella / "quiz").glob(f"{slug}_cap*.md")):
        for blk in re.split(r"(?m)^(?=## \[)", f.read_text(encoding="utf-8")):
            m = re.match(r"## \[([^\]]+)\]\s*argomenti:\s*(\S+)", blk)
            r = re.search(r"(?m)^RISPOSTA:\s*(\d)", blk)
            if not m or not r:
                continue
            righe = blk.split("\n")[1:]
            opz = [(i, re.sub(r"^[1-5]\.\s*", "", l).strip()) for i, l in enumerate(righe) if re.match(r"^[1-5]\.\s", l)]
            if len(opz) < 3:
                print(f"  quiz {m.group(1)}: risposte non trovate", file=sys.stderr); continue
            q = "\n".join(righe[:opz[0][0]]).strip()
            sp = re.search(r"(?ms)^SPIEGAZIONE:\s*(.*?)(?=^ATTENZIONE:|\Z)", blk)
            a = int(r.group(1))
            if not 1 <= a <= len(opz):
                print(f"  quiz {m.group(1)}: RISPOSTA fuori intervallo", file=sys.stderr); continue
            cap = re.sub(r"\D", "", m.group(2))
            out.append(dict(id=m.group(1), m=mat, prova="", args=[f"{slug}:cap{cap}"], q=q, o=[o for _, o in opz], a=a,
                            s=(sp.group(1).strip() if sp else ""), w=""))
    return out


def main():
    cartella, uscita = Path(sys.argv[1]), Path(sys.argv[2])
    sp = json.loads((cartella / "spazio.json").read_text(encoding="utf-8"))
    materie, tag_tema, priorita, temi_cap, cards, probs, qz, rslug = {}, {}, [], {}, [], [], [], {}
    for mt in sp["materie"]:
        mat, slug = mt["nome"], mt["slug"]
        f = cartella / f"{slug}.json"
        caps = json.loads(f.read_text(encoding="utf-8"))["capitoli"] if f.exists() else []
        rslug[mat] = slug
        el = [dict(n=c["num"], t=senza_num(c["titolo"]), s=0, hl=0, tot=sum(1 for b in c["blocks"] if b["t"] in ("p", "li", "pre"))) for c in caps]
        materie[mat] = dict(capitoli=len(el), studiati=0, elenco=el,
                            lezioni=f"{len(el)} capitoli" if el else "riassunti in preparazione",
                            prossimo=("Da studiare: " + (f"{el[0]['n']}-{el[-1]['n']}" if len(el) > 1 else str(el[0]["n"])) + ".") if el else "I riassunti arrivano appena c'è il materiale.")
        for c in caps:
            t = tema(c)
            tag_tema[f"{slug}:cap{c['num']}"] = t
            priorita.append(t)
            temi_cap.setdefault(mat, {})[t] = {"cap": f"cap. {c['num']}", "n": c["num"]}
        cards += schede(mat, slug, caps)
        probs += domande_aperte(mat, slug, caps)
        qz += quiz(mat, slug, cartella)
    for q in qz:
        q["theme"] = tag_tema.get(q["args"][0], "Altro")
    data = dict(oggi=str(date.today()), quiz=qz, problemi=probs, cards=cards, materie=materie, freq=[], tagTema=tag_tema,
                priorita=priorita, temi={}, temiCap=temi_cap, pesi={}, piano="", esami={}, nascoste={}, coperti={})
    uscita.mkdir(parents=True, exist_ok=True)
    (uscita / "data.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    con_capitoli = [m for m, x in materie.items() if x["capitoli"]] or list(materie)
    print(json.dumps(dict(mats=con_capitoli, rslug=rslug, titolo=sp.get("titolo", "Quaderno"),
                          conti=dict(quiz=len(qz), schede=len(cards), domande=len(probs))), ensure_ascii=False))


if __name__ == "__main__":
    main()
