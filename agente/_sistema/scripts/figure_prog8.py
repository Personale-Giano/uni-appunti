"""Figure dei capitoli 41-45 di Programmazione (slide 08A: memoria dinamica, heap, malloc/free). PNG in _sistema/figure/prog/.
Uso: python figure_prog8.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_info import vuoto, BLU, ROSSO, VERDE, GRIGIO, _salva
from figure_funzioni import _cella, _graffa, _freccia_indirizzi, LOCALI, RETVAL, PARAM, CONTROLLO, LIBERO, CODICE
from matplotlib.patches import FancyArrowPatch, Rectangle

HEAP, DATA, MORTO = "#CFE8CF", "#E3D3A4", "#E4E4E4"
EC_HEAP = "#3c8a4a"


def _arco(ax, p, q, col, rad=0.5, lw=1.7):
    ax.add_patch(FancyArrowPatch(p, q, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>", mutation_scale=14, color=col, lw=lw, zorder=5))


def dangling_stack():
    """leggiArraySbagliato: lo stack subito prima del return e subito dopo (il puntatore resta appeso)."""
    fig, ax = vuoto(10.0, 4.6, (-0.6, 17.6), (-1.3, 7.4))
    w, h = 4.4, 0.68

    def colonna(x0, righe):
        y = 6.3
        pos = {}
        for nome, testo, fc in righe:
            _cella(ax, x0, y - h, w, h, testo, fc=fc, fs=10)
            pos[nome] = (y, y - h)
            y -= h
        return pos

    ax.text(w / 2, 6.85, "subito prima del return", ha="center", fontsize=11, fontweight="bold", color=BLU)
    sx = colonna(0, [("aLen", "size_t aLen = 3", LOCALI), ("a", "int* a = ??", LOCALI), ("ret", "valore di ritorno (int*)", RETVAL),
                     ("out", "size_t* out_n = &aLen", PARAM), ("c", "dati di controllo", CONTROLLO), ("n", "size_t n = 3", LOCALI),
                     ("a2", "a[2] = 30", LOCALI), ("a1", "a[1] = 20", LOCALI), ("a0", "a[0] = 10", LOCALI)])
    _graffa(ax, w + 0.08, sx["a"][1] + 0.04, sx["aLen"][0], "main", GRIGIO)
    _graffa(ax, w + 0.08, sx["a0"][1], sx["ret"][0] - 0.04, "leggiArray\nSbagliato", "#6a3fb5")
    ax.text(w / 2, -0.55, "il VLA a vive nello stack frame\ndella funzione", ha="center", va="center", fontsize=9.5, color=BLU)

    x1 = 9.4
    ax.text(x1 + w / 2, 6.85, "subito dopo il return", ha="center", fontsize=11, fontweight="bold", color=ROSSO)
    dx = colonna(x1, [("aLen", "size_t aLen = 3", LOCALI), ("a", "int* a = indirizzo", "#FBD9D3")])
    y_alto, y_basso = dx["a"][1], sx["a0"][1]
    ax.add_patch(Rectangle((x1, y_basso), w, y_alto - y_basso, fc=MORTO, ec="#888888", lw=1.2, hatch="///"))
    ax.text(x1 + w / 2, (y_alto + y_basso) / 2 + 0.5, "stack frame deallocato:\nmemoria non più valida", ha="center", va="center", fontsize=10, color="#444444",
            bbox=dict(fc="white", ec="none", pad=3))
    ax.text(x1 + w / 2, y_basso + h / 2, "qui c'era a[0]", ha="center", va="center", fontsize=9.5, color=ROSSO, bbox=dict(fc="white", ec="none", pad=2))
    _graffa(ax, x1 + w + 0.08, dx["a"][1] + 0.04, dx["aLen"][0], "main", GRIGIO)
    _arco(ax, (x1, (dx["a"][0] + dx["a"][1]) / 2), (x1, y_basso + h / 2), ROSSO, rad=0.45)
    ax.text(x1 + w / 2, -0.55, "a in main è un dangling pointer:\npunta a un'area che non esiste più", ha="center", va="center", fontsize=9.5, color=ROSSO)
    return _salva(fig, "prog/dangling_stack")


def segmenti_memoria():
    """Modello semplificato: codice, data, heap (cresce verso l'alto), memoria libera, stack (cresce verso il basso)."""
    fig, ax = vuoto(8.6, 4.4, (-4.2, 12.4), (-0.4, 7.4))
    w = 3.4
    seg = [("codice", CODICE, "#b8921f", 0.8, "Code segment: le istruzioni del programma"),
           ("data", DATA, "#8a7430", 0.8, "Data segment: variabili globali e statiche"),
           ("heap", HEAP, EC_HEAP, 1.5, "Heap: memoria dinamica, gestita a mano\ncon malloc e free"),
           ("memoria libera", LIBERO, "#9db4d3", 2.2, "spazio libero condiviso da stack e heap"),
           ("stack", LOCALI, "#4a6fa5", 1.6, "Stack: variabili automatiche, gestito\nin automatico a ogni chiamata e ritorno")]
    y = 0.0
    quote = {}
    for nome, fc, ec, hh, descr in seg:
        _cella(ax, 0, y, w, hh, nome, fc=fc, ec=ec, fs=10.5, bold=nome in ("heap", "stack"), col=GRIGIO if nome == "memoria libera" else "black")
        ax.text(w + 0.35, y + hh / 2, descr, ha="left", va="center", fontsize=9.5)
        quote[nome] = (y, y + hh)
        y += hh
    ax.annotate("", xy=(-0.45, quote["heap"][1] + 0.75), xytext=(-0.45, quote["heap"][0] + 0.1), arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=2.2))
    ax.text(-0.65, quote["heap"][1], "lo heap cresce\nverso l'alto", ha="right", va="center", fontsize=9, color=VERDE)
    ax.annotate("", xy=(-0.45, quote["stack"][0] - 0.75), xytext=(-0.45, quote["stack"][1] - 0.1), arrowprops=dict(arrowstyle="-|>", color=BLU, lw=2.2))
    ax.text(-0.65, quote["stack"][0], "lo stack cresce\nverso il basso", ha="right", va="center", fontsize=9, color=BLU)
    ax.text(w / 2, y + 0.25, "indirizzi alti", ha="center", fontsize=9, color=GRIGIO)
    ax.text(w / 2, -0.3, "indirizzi bassi", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "prog/segmenti_memoria")


def heap_blocchi():
    """Sei stati dello heap: malloc(20), malloc(32), malloc(16), free(p2), malloc(20), free(p1). Le posizioni sono simulate (primo buco che basta)."""
    passi = [("m", "p1", 20), ("m", "p2", 32), ("m", "p3", 16), ("f", "p2", 0), ("m", "p4", 20), ("f", "p1", 0)]
    titoli = ["p1 =\nmalloc(20);", "p2 =\nmalloc(32);", "p3 =\nmalloc(16);", "free(p2);\np2 = NULL;", "p4 =\nmalloc(20);", "free(p1);\np1 = NULL;"]
    blocchi, stati, cima = {}, [], 0          # blocchi: nome -> (inizio, byte)
    for op, nome, byte in passi:
        if op == "m":
            occupati = sorted(blocchi.values())
            inizio, pos = None, 0
            for (b0, bl) in occupati:         # primo buco abbastanza grande
                if b0 - pos >= byte:
                    inizio = pos
                    break
                pos = b0 + bl
            if inizio is None:
                inizio = pos
            blocchi[nome] = (inizio, byte)
            cima = max(cima, inizio + byte)
        else:
            del blocchi[nome]
        stati.append(dict(blocchi))
    assert stati[4]["p4"] == (20, 20) and stati[5] == {"p3": (52, 16), "p4": (20, 20)} and cima == 68

    k = 0.062                                 # altezza per byte
    fig, ax = vuoto(10.6, 4.3, (-1.3, 17.6), (-2.2, 6.4))
    for s, stato in enumerate(stati):
        x = s * 2.95
        _cella(ax, x, 0.0, 2.1, 5.3, "", fc=LIBERO, ec="#9db4d3")
        for nome, (b0, bl) in stato.items():
            nuovo = passi[s][0] == "m" and passi[s][1] == nome
            _cella(ax, x, b0 * k, 2.1, bl * k, f"{nome}: {bl} byte", fc="#9FD3A4" if nuovo else HEAP, ec=EC_HEAP, fs=8.0, bold=nuovo)
        if passi[s][0] == "f":
            b0, bl = stati[s - 1][passi[s][1]] if s else (0, 0)
            ax.add_patch(Rectangle((x, b0 * k), 2.1, bl * k, fc="none", ec=ROSSO, lw=1.3, ls="--"))
            ax.text(x + 1.05, b0 * k + bl * k / 2, "liberato", ha="center", va="center", fontsize=8.8, color=ROSSO)
        ax.text(x + 1.05, 4.75, "memoria\nlibera", ha="center", va="center", fontsize=8.5, color=GRIGIO)
        ax.text(x + 1.05, -0.3, titoli[s], ha="center", va="top", fontsize=8.8, family="monospace")
        ax.text(x + 1.05, 5.55, f"passo {s + 1}", ha="center", fontsize=9, color=GRIGIO)
    ax.annotate("", xy=(-0.5, 3.2), xytext=(-0.5, 0.1), arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=2.0))
    ax.text(-0.75, 1.6, "heap", rotation=90, ha="right", va="center", fontsize=10, color=VERDE, fontweight="bold")
    ax.text(8.4, -1.85, "in verde scuro il blocco appena allocato; al passo 5 il nuovo blocco trova posto nel buco lasciato da p2", ha="center", fontsize=9.3, color=GRIGIO)
    return _salva(fig, "prog/heap_blocchi")


def leggi_array_heap():
    """Dopo il ritorno di leggiArray: main ha aLen e a nello stack, il blocco con 10, 20, 30 resta nello heap."""
    fig, ax = vuoto(8.8, 4.5, (-4.6, 12.0), (-0.5, 7.6))
    w, h = 4.0, 0.7
    _cella(ax, 0, 6.3, w, h, "size_t aLen = 3", fc=LOCALI, fs=10)
    _cella(ax, 0, 5.6, w, h, "int* a = indirizzo", fc=LOCALI, fs=10)
    _cella(ax, 0, 2.9, w, 2.7, "memoria libera", fc=LIBERO, ec="#9db4d3", fs=9.5, col=GRIGIO)
    for i, v in enumerate((10, 20, 30)):
        _cella(ax, 0, 0.8 + i * h, w, h, f"a[{i}] = {v}", fc=HEAP, ec=EC_HEAP, fs=10)
    _cella(ax, 0, 0.0, w, 0.8, "codice e dati statici", fc=CODICE, ec="#b8921f", fs=9.5)
    _arco(ax, (0, 5.95), (0, 1.15), VERDE, rad=0.5)
    ax.text(-1.55, 3.6, "a contiene\nl'indirizzo del\nprimo byte\ndel blocco", ha="right", va="center", fontsize=9.3, color=VERDE)
    _graffa(ax, w + 0.08, 5.63, 7.0, "stack frame di main", GRIGIO)
    _graffa(ax, w + 0.08, 0.83, 2.9, "blocco nello heap:\n3 * sizeof(int) byte", VERDE)
    ax.text(w + 0.4, 4.25, "il frame di leggiArray è stato\ndeallocato al ritorno,\nil blocco nello heap no", ha="left", va="center", fontsize=9.3, color=BLU)
    return _salva(fig, "prog/leggi_array_heap")


def select_copy_fasi():
    """selectCopy su b = {12, 1, 3, 4, 8} con Cond = pari: i valori sono calcolati eseguendo le tre fasi."""
    b = [12, 1, 3, 4, 8]
    cond = lambda x: x % 2 == 0
    count = sum(1 for x in b if cond(x))
    a, da = [], []
    for i, x in enumerate(b):
        if cond(x):
            a.append(x)
            da.append(i)
    assert count == 3 and a == [12, 4, 8] and len(a) == count
    fig, ax = vuoto(8.6, 3.9, (-3.4, 10.6), (-3.6, 2.9))
    L = 1.15
    ax.text(-0.2, 1.4, "b", ha="right", va="center", fontsize=12, fontweight="bold")
    ax.text(-0.75, 1.4, "(sorgente)", ha="right", va="center", fontsize=9, color=GRIGIO)
    for i, x in enumerate(b):
        ok = cond(x)
        _cella(ax, i * L, 1.0, L, 0.8, str(x), fc="#DDEFD9" if ok else "#F3F6FB", ec=EC_HEAP if ok else "#8aa0bf", bold=ok, fs=11)
        ax.text(i * L + L / 2, 1.98, str(i), ha="center", fontsize=9.5, color=BLU)
    ax.text(len(b) * L + 0.3, 1.4, f"fase 1: si contano i pari, count = {count}", ha="left", va="center", fontsize=9.5)
    x0 = 1.0
    ax.text(x0 - 0.2, -1.6, "a", ha="right", va="center", fontsize=12, fontweight="bold")
    ax.text(x0 - 0.75, -1.6, "(nello heap)", ha="right", va="center", fontsize=9, color=GRIGIO)
    for j, x in enumerate(a):
        _cella(ax, x0 + j * L, -2.0, L, 0.8, str(x), fc=HEAP, ec=EC_HEAP, bold=True, fs=11)
        ax.text(x0 + j * L + L / 2, -2.4, str(j), ha="center", fontsize=9.5, color=VERDE)
        ax.add_patch(FancyArrowPatch((da[j] * L + L / 2, 0.95), (x0 + j * L + L / 2, -1.15), arrowstyle="-|>", mutation_scale=13, color=VERDE, lw=1.5))
    ax.text(x0 + len(a) * L + 0.3, -1.45, "fase 2: a = malloc(count * sizeof(int))", ha="left", va="center", fontsize=9.5)
    ax.text(x0 + len(a) * L + 0.3, -1.95, "fase 3: a[j] = b[i]; j++ per ogni pari", ha="left", va="center", fontsize=9.5)
    ax.text(3.6, -3.2, "indice i sopra b, indice di copia j sotto a: l'ordine degli elementi è conservato", ha="center", fontsize=9.5, color=GRIGIO)
    return _salva(fig, "prog/select_copy_fasi")


if __name__ == "__main__":
    for f in (dangling_stack, segmenti_memoria, heap_blocchi, leggi_array_heap, select_copy_fasi):
        print(f())
