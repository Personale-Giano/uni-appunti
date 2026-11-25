"""Figure dei capitoli 50-51 di Programmazione (slide 09A del 24 nov: matrici nello heap) e dei capitoli 19-20
del Laboratorio (Lab07: elimina vocali, intervalli semiaperti). PNG in _sistema/figure/prog/ e _sistema/figure/lab/.
Uso: python figure_prog10.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_info import vuoto, BLU, ROSSO, VERDE, GRIGIO, _salva
from figure_funzioni import _cella, _graffa, LOCALI, LIBERO
from matplotlib.patches import FancyArrowPatch

HEAP, EC_HEAP = "#CFE8CF", "#3c8a4a"
RIGHE = [("#DCE8F7", "#4a72a8"), ("#F7E6CF", "#b07a2a"), ("#E6DDF4", "#6a4fa0")]


def _arco(ax, p, q, col, rad=0.3, lw=1.6):
    ax.add_patch(FancyArrowPatch(p, q, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>", mutation_scale=13, color=col, lw=lw, zorder=5))


def _blocco_heap(ax, x0, y, rows, cols, valori, L=0.62, H=0.7):
    """Blocco contiguo di rows*cols interi, colorato per righe; restituisce l'ascissa d'inizio di ogni riga."""
    inizi = []
    for i in range(rows):
        fc, ec = RIGHE[i % 3]
        inizi.append(x0 + i * cols * L)
        for j in range(cols):
            k = i * cols + j
            _cella(ax, x0 + k * L, y, L, H, str(valori[i][j]), fc=fc, ec=ec, fs=9.5, bold=True)
    return inizi


def matrice_heap():
    """int (*m)[4] = malloc(3 * 4 * sizeof(int)): un solo blocco contiguo, m punta alla riga 0, m + 1 salta 16 byte."""
    rows, cols = 3, 4
    val = [[i * cols + j for j in range(cols)] for i in range(rows)]
    L, H = 0.62, 0.7
    fig, ax = vuoto(9.0, 4.3, (-0.4, 12.4), (-2.6, 4.0))
    # stack: il solo puntatore
    ax.text(1.4, 3.55, "stack", ha="center", fontsize=10.5, fontweight="bold", color=BLU)
    _cella(ax, 0, 2.2, 2.8, 0.8, "int (*m)[cols]", fc=LOCALI, fs=9.5, bold=True)
    ax.text(1.4, 1.85, "con cols = 4", ha="center", va="top", fontsize=9, color=GRIGIO)
    # heap: il blocco
    x0, y = 3.9, 0.3
    ax.text(x0 + rows * cols * L / 2, 3.55, "heap: un solo blocco di 3 · 4 · sizeof(int) = 48 byte", ha="center", fontsize=10.5,
            fontweight="bold", color=EC_HEAP)
    inizi = _blocco_heap(ax, x0, y, rows, cols, val, L, H)
    for i, xs in enumerate(inizi):
        ax.text(xs + cols * L / 2, y + H + 0.25, f"riga {i}  (m[{i}])", ha="center", fontsize=9, color=RIGHE[i][1])
        ax.text(xs + 0.05, y - 0.3, f"m + {i}" if i else "m", ha="left", fontsize=9, color=ROSSO, family="monospace")
        ax.plot([xs, xs], [y - 0.12, y + H + 0.1], color=ROSSO, lw=1.4)
    _arco(ax, (2.8, 2.6), (x0 + 0.15, y + H), VERDE, rad=-0.25, lw=1.7)
    ax.text(3.3, 2.75, "punta alla riga 0", ha="left", fontsize=9, color=VERDE)
    # salto di una riga
    xa, xb = inizi[0], inizi[1]
    ax.annotate("", xy=(xb, -0.75), xytext=(xa, -0.75), arrowprops=dict(arrowstyle="-|>", color=ROSSO, lw=1.4))
    ax.text((xa + xb) / 2, -1.15, "m + 1: salta una riga intera\n= 4 · sizeof(int) = 16 byte", ha="center", va="top", fontsize=9, color=ROSSO)
    # elemento m[2][1]
    k = 2 * cols + 1
    assert val[2][1] == 9 and k * 4 == 36
    xe = x0 + k * L + L / 2
    ax.annotate("m[2][1]: 36 byte dopo l'inizio", xy=(xe, y), xytext=(xe + 0.9, -1.6), ha="center", fontsize=9, color=BLU,
                arrowprops=dict(arrowstyle="-|>", color=BLU, lw=1.2))
    return _salva(fig, "prog/matrice_heap")


def leggi_matrice_heap():
    """Dopo leggiMatrice con input 2 3 / 1 2 3 4 5 6: rows, cols, p e m in main, un blocco nello heap."""
    rows, cols = 2, 3
    val = [[1, 2, 3], [4, 5, 6]]
    fig, ax = vuoto(10.0, 4.4, (-0.6, 15.8), (-1.6, 5.4))
    w, h = 4.6, 0.72
    ax.text(w / 2, 4.95, "stack frame di main", ha="center", fontsize=10.5, fontweight="bold", color=BLU)
    celle = [("size_t rows = 2", None), ("size_t cols = 3", None), ("int_matrix_ptr_t p", "p"), ("int (*m)[cols]", "m")]
    pos = {}
    for k, (t, nome) in enumerate(celle):
        yy = 4.1 - k * h
        _cella(ax, 0, yy, w, h, t, fc=LOCALI, fs=9.5)
        if nome:
            pos[nome] = yy + h / 2
    x0, y = 7.3, 1.6
    L, H = 1.0, 0.8
    ax.text(x0 + rows * cols * L / 2, 3.15, "heap: 2 · 3 · sizeof(int) byte", ha="center", fontsize=10.5, fontweight="bold", color=EC_HEAP)
    inizi = _blocco_heap(ax, x0, y, rows, cols, val, L, H)
    for i, xs in enumerate(inizi):
        ax.text(xs + cols * L / 2, y - 0.35, f"riga {i}", ha="center", fontsize=9, color=RIGHE[i][1])
    _arco(ax, (w, pos["p"]), (x0 + 0.1, y + H), VERDE, rad=-0.2)
    _arco(ax, (w, pos["m"]), (x0 + 0.1, y + H * 0.45), VERDE, rad=0.15)
    ax.text(5.0, 4.3, "p e m: due puntatori allo stesso blocco (aliasing)\nuna sola free(m), poi m = p = NULL", ha="left", va="center",
            fontsize=9, color=ROSSO)
    ax.text(w / 2, -0.75, "solo con m (tipo preciso, righe da 3 int)\nsi può scrivere m[i][j]; con p no", ha="center", va="center",
            fontsize=9, color=GRIGIO)
    ax.text(x0 + 3, -0.75, "il frame di leggiMatrice è già stato deallocato,\nil blocco nello heap resta", ha="center", va="center",
            fontsize=9, color=GRIGIO)
    return _salva(fig, "prog/leggi_matrice_heap")


def _riga_char(ax, x0, y, chars, L, fcs, ec="#4a6fa5", fs=11):
    for k, c in enumerate(chars):
        _cella(ax, x0 + k * L, y, L, 0.8, c, fc=fcs[k], ec=ec, fs=fs, bold=c != "\\0")


def elimina_vocali():
    """"informazione": prima e dopo elimina_vocali; i caratteri sono calcolati simulando pSrc e pDst."""
    s = list("informazione") + ["\\0"]
    dopo = s[:]
    dst = 0
    src = 0
    while s[src] != "\\0":
        if s[src] not in "aeiouAEIOU":
            dopo[dst] = s[src]
            dst += 1
        src += 1
    dopo[dst] = "\\0"
    assert "".join(dopo[:dst]) == "nfrmzn" and dst == 6 and src == 12
    L = 0.85
    fig, ax = vuoto(10.6, 4.3, (-2.6, 12.2), (-1.4, 5.0))
    ax.text(-0.3, 3.7, "prima", ha="right", va="center", fontsize=10.5, fontweight="bold")
    voc = ["#F7D9D2" if c in "aeiou" else "#DCE8F7" for c in s]
    _riga_char(ax, 0, 3.3, s, L, voc)
    ax.text(5.5, 4.55, "in rosa le vocali da eliminare; pSrc e pDst partono entrambi da pStr", ha="center", fontsize=9, color=GRIGIO)
    ax.text(-0.3, 1.0, "dopo", ha="right", va="center", fontsize=10.5, fontweight="bold")
    fcs = ["#DCE8F7" if k < dst else ("#FFF2B3" if k == dst else "#E4E4E4") for k in range(len(dopo))]
    _riga_char(ax, 0, 0.6, dopo, L, fcs)
    for nome, k, col, dy in (("pStr", 0, BLU, 0), ("pDst", dst, ROSSO, 0), ("pSrc", src, VERDE, 0)):
        xx = k * L + L / 2
        ax.annotate(nome, xy=(xx, 0.6), xytext=(xx, -0.55), ha="center", fontsize=9.5, color=col, fontweight="bold",
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.3))
    ax.plot([0, dst * L], [1.55, 1.55], color=BLU, lw=1.5)
    ax.text(dst * L / 2, 1.85, "stringa risultato \"nfrmzn\"", ha="center", fontsize=9, color=BLU)
    ax.plot([(dst + 1) * L, len(dopo) * L], [1.55, 1.55], color=GRIGIO, lw=1.5)
    ax.text((dst + 1 + len(dopo)) * L / 2, 1.85, "residui, non più parte della stringa", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "lab/elimina_vocali")


def intervallo_semiaperto():
    """Array di 12 elementi con len = 12, sotto-intervallo [left, right) = [3, 7): 4 elementi, da a[3] ad a[6]."""
    a = [17, 21, -3, 8, 19, 7, 2, 5, 6, 61, 1, 11]
    left, right = 3, 7
    L = 0.9
    fig, ax = vuoto(10.4, 3.6, (-1.6, 13.2), (-2.2, 3.4))
    for i, v in enumerate(a):
        dentro = left <= i < right
        _cella(ax, i * L, 0, L, 0.8, str(v), fc="#FFE3A6" if dentro else "#DCE8F7", ec="#b07a2a" if dentro else "#4a6fa5",
               fs=10, bold=dentro)
        ax.text(i * L + L / 2, 1.0, str(i), ha="center", fontsize=8.5, color=GRIGIO)
    _cella(ax, len(a) * L, 0, L, 0.8, "NON\nVALIDO", fc="#C9302C", ec="#8a1f1c", fs=6.5, col="white", bold=True)
    ax.text(-0.25, 1.0, "indici", ha="right", fontsize=8.5, color=GRIGIO)
    for nome, k, col in (("left = 3", left, ROSSO), ("right = 7", right, ROSSO), ("len = 12", len(a), BLU)):
        ax.annotate(nome, xy=(k * L, 0), xytext=(k * L, -1.0), ha="center", fontsize=9.5, color=col, fontweight="bold",
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.3))
    ax.plot([left * L, right * L], [1.55, 1.55], color="#b07a2a", lw=1.6)
    ax.text((left + right) * L / 2, 1.85, "[left, right): right − left = 4 elementi, da a[left] ad a[right − 1]", ha="center",
            fontsize=9.3, color="#b07a2a")
    ax.plot([0, len(a) * L], [2.65, 2.65], color=BLU, lw=1.4)
    ax.text(len(a) * L / 2, 2.85, "[0, len): tutti gli indici validi", ha="center", fontsize=9.3, color=BLU)
    ax.text(len(a) * L / 2, -1.9, "left è il primo indice incluso, right il primo escluso:  0 ≤ left ≤ right ≤ len", ha="center",
            fontsize=9.3, color=GRIGIO)
    return _salva(fig, "lab/intervallo_semiaperto")


if __name__ == "__main__":
    for f in (matrice_heap, leggi_matrice_heap, elimina_vocali, intervallo_semiaperto):
        print(f())
