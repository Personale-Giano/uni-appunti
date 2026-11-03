"""Correzioni del 3 nov 2026 ai riassunti del sito (errori trovati rileggendo tutti i capitoli).
Ogni correzione: (materia, blocco, vecchio, nuovo). Si rifiuta se una evidenziazione di Emanuele
cambierebbe testo o posizione (controllo sugli offset UTF-16 del testo visibile)."""
import html, json, re, shutil, sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
CONT = Path(r"C:\Users\admin\Documents\GitHub\quaderno-privato\contenuti")
EVID = json.loads(Path(r"C:\Users\admin\Desktop\UNI\agente\_sistema\evid_export.json").read_text(encoding="utf-8"))["evid"]
BACKUP = Path(r"C:\Users\admin\Desktop\UNI\agente\_sistema\backup") / ("sito-prima-correzioni-" + datetime.now().strftime("%Y%m%d-%H%M"))

C = [
    # Algebra
    ("algebra", "cap5.21", "z<sup>−1</sup> = ", "z<sup>−1</sup> = (z̄)/(|z|<sup>2</sup>)"),
    ("algebra", "cap13.28", "(e quindi le potenze, capitolo 5)", "(e quindi le potenze)"),
    # Matematica discreta
    ("matematica-discreta", "cap8.32", "se  , allora a = b", "se a | b e b | a, allora a = b"),
    ("matematica-discreta", "cap8.33", "1 / -1 e -1 / 1", "1 | -1 e -1 | 1"),
    # Fondamenti
    ("fondamenti", "cap10.19", "Lempel-Ziv-Welsh", "Lempel-Ziv-Welch"),
    ("fondamenti", "cap10.19", "Lempel, Ziv e Welsh", "Lempel, Ziv e Welch"),
    ("fondamenti", "cap10.25", "(<strong>crominanza</strong>)",
     "(<strong>crominanza</strong>): per questo il primo passo è fare la media dei valori di crominanza su quadrati di 2×2 pixel, che riduce di un fattore quattro l&#x27;informazione sul colore lasciando intatta quella sulla luminosità."),
    ("fondamenti", "cap10.29", "sfruttando due principi psicoacustici",
     "sfruttando due principi psicoacustici: il <strong>mascheramento temporale</strong> (per un breve periodo dopo un suono forte l&#x27;orecchio non percepisce i suoni più deboli) e il <strong>mascheramento in frequenza</strong> (un suono a una certa frequenza copre i suoni più deboli a frequenze vicine)."),
    ("fondamenti", "cap12.19", "capitoli 1 e 5 di questo Word", "capitoli 1 e 5 di questo riassunto"),
    ("fondamenti", "cap13.25",
     "la tilde <em>; nei linguaggi di programmazione (C, C++, Java) il punto esclamativo </em><em><code>!</code></em><em>.</em>",
     "la tilde ~; nei linguaggi di programmazione (C, C++, Java) il punto esclamativo <code>!</code>."),
    ("fondamenti", "cap21.31", "solo se il dominio è finito e molto piccolo (anche qualche miliardo)",
     "solo se il dominio è finito e non troppo grande (qualche miliardo di elementi è ancora alla portata di un computer)"),
    ("fondamenti", "cap23.7", "¬∀x P(x) = ∃x ¬P(x) e ¬∃x P(x) = ∀x ¬P(x)", "¬∀x P(x) ≡ ∃x ¬P(x) e ¬∃x P(x) ≡ ∀x ¬P(x)"),
    ("fondamenti", "cap24.26", "Per dimostrare un&#x27;implicazione la si assume come ipotesi: si <strong>assume anche p</strong>.",
     "Per dimostrare un&#x27;implicazione se ne assume l&#x27;ipotesi: si <strong>assume anche p</strong>."),
    # Programmazione
    ("programmazione", "cap10.29", "Dichiarare avere un valore, avere un indirizzo, essere inizializzata",
     "Dichiarazione, valore, indirizzo e inizializzazione"),
    ("programmazione", "cap14.18", "%f\n&quot;", "%f\\n&quot;"),
    ("programmazione", "cap14.18", "%.3f\n&quot;", "%.3f\\n&quot;"),
    ("programmazione", "cap14.18", "%.3e\n&quot;", "%.3e\\n&quot;"),
    ("programmazione", "cap17.15", "e l&#x27;espressione vale il valore copiato (se ne vedrà la conseguenza nel capitolo 20).",
     "e l&#x27;espressione vale il valore copiato: se è diverso da 0 la condizione risulta sempre vera, qualunque fosse il valore di partenza di x."),
    ("programmazione", "cap19.33",
     "Il prossimo capitolo raccoglie gli errori più comuni con questi costrutti, la visibilità delle variabili dentro i blocchi e alcuni schemi che si ripetono spesso.",
     "Resta da vedere che cosa succede a una variabile dichiarata dentro il blocco di un if. L&#x27;esempio è lo <strong>scambio condizionato</strong>, che scambia x e y (letti da tastiera) solo quando non sono in ordine: <code>if (y &lt; x) { int temp = x; x = y; y = temp; }</code>."),
    ("programmazione", "cap26.11", "(UCS-16, 16 bit per carattere, un sottoinsieme; UCS-32, 32 bit, completo ma molto costoso in spazio)",
     "(UCS-2, 16 bit per carattere, un sottoinsieme; UCS-4, 32 bit, completo ma molto costoso in spazio; nelle slide sono chiamate «UCS-16» e «UCS-32», ma i nomi standard sono UCS-2 e UCS-4)"),
    ("programmazione", "cap27.25", "float y2 = square(y);", "float y2 = square(y);      // y: una variabile float definita prima"),
    # Laboratorio
    ("laboratorio", "cap8.2", "(capitolo 9 di questo riassunto) ai programmi", "(capitolo 9 di questo riassunto), ai programmi"),
    ("laboratorio", "cap8.32", "tutti distinti,: il testo", "tutti distinti; il testo"),
    ("laboratorio", "cap12.33", "si continua a dimezzare (57, 60, 61…) fino al tentativo 62",
     "si continua a dimezzare (57, poi 60) fino al tentativo 62"),
]


def testo(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h)).encode("utf-16-le")


def main(applica):
    dati = {}
    for m in {c[0] for c in C}:
        dati[m] = json.loads((CONT / f"{m}.json").read_text(encoding="utf-8"))
    blocchi = {m: {b["b"]: b for cap in d["capitoli"] for b in cap["blocks"] if "b" in b} for m, d in dati.items()}
    # asterischi markdown rimasti nel testo → corsivo, solo dove non spostano evidenziazioni
    for bid in ([] if "fondamenti" not in blocchi else ["cap12.7", "cap13.10", "cap13.25", "cap13.26", "cap13.27", "cap15.25", "cap16.13", "cap17.3", "cap17.5", "cap18.2"]):
        b = blocchi["fondamenti"][bid]
        nuovo = re.sub(r"\*([^*<>]{1,30})\*", r"<em>\1</em>", b["h"])
        t0, t1 = testo(b["h"]), testo(nuovo)
        if all(t0[2 * a:2 * z] == t1[2 * a:2 * z] for a, z in EVID["fondamenti"].get(bid, [])):
            C.append(("fondamenti", bid, None, None))
        else:
            print(f"fondamenti           {bid:9} asterischi lasciati (sposterebbero un'evidenziazione)")
    prima = {}
    for m, bid, vecchio, nuovo in C:
        b = blocchi[m][bid]
        prima.setdefault((m, bid), b["h"])
        if vecchio is None:
            b["h"] = re.sub(r"\*([^*<>]{1,30})\*", r"<em>\1</em>", b["h"])
            continue
        assert b["h"].count(vecchio) == 1, (m, bid, vecchio[:50], b["h"].count(vecchio))
        b["h"] = b["h"].replace(vecchio, nuovo)
    ok = True
    for (m, bid), h0 in prima.items():
        t0, t1 = testo(h0), testo(blocchi[m][bid]["h"])
        for a, z in EVID[m].get(bid, []):
            if t0[2 * a:2 * z] != t1[2 * a:2 * z]:
                ok = False
                print("EVIDENZIAZIONE TOCCATA:", m, bid, [a, z])
        print(f"{m:20} {bid:9} evid={EVID[m].get(bid)}  ok")
    if not ok:
        sys.exit("fermo: una correzione sposterebbe un'evidenziazione")
    if applica:
        BACKUP.mkdir(parents=True)
        for m, d in dati.items():
            shutil.copy2(CONT / f"{m}.json", BACKUP / f"{m}.json")
            (CONT / f"{m}.json").write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print("applicate", len(C), "correzioni; backup in", BACKUP)


if __name__ == "__main__":
    main("--applica" in sys.argv)
