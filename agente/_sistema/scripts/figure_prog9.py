"""Figure dei capitoli 46-49 di Programmazione (slide 09A: matrici). PNG in _sistema/figure/prog/.
Uso: python figure_prog9.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_info import vuoto, BLU, ROSSO, VERDE, GRIGIO, _salva
from figure_funzioni import _cella
from matplotlib.patches import FancyArrowPatch

R0, R1 = "#DCE8F7", "#F7E6CF"
EC0, EC1 = "#4a72a8", "#b07a2a"


def matrice_memoria():
    """int m[2][3] = {{0,1,2},{3,4,5}}: tabella e sequenza lineare in memoria (row-major), base 0x3E8, int da 4 byte."""
    m = [[0, 1, 2], [3, 4, 5]]
    ROWS, COLS, base = 2, 3, 0x3E8
    fig, ax = vuoto(9.4, 4.3, (-2.2, 15.6), (-4.6, 3.4))
    L, H = 1.1, 0.8
    ax.text(1.65, 3.25, "come tabella: m[i][j]", ha="center", fontsize=10.5, fontweight="bold")
    for j in range(COLS):
        ax.text(j * L + L / 2, 2.35, f"col {j}", ha="center", fontsize=8.5, color=GRIGIO)
    for i in range(ROWS):
        y = 1.2 - i * H
        ax.text(-0.15, y + H / 2, f"riga {i}", ha="right", va="center", fontsize=8.5, color=GRIGIO)
        for j in range(COLS):
            _cella(ax, j * L, y, L, H, str(m[i][j]), fc=R0 if i == 0 else R1, ec=EC0 if i == 0 else EC1, bold=True, fs=11)
    x0 = 5.2
    ax.text(x0 + 3 * L, 3.25, "in memoria: le righe una dopo l'altra", ha="center", fontsize=10.5, fontweight="bold")
    k = 0
    for i in range(ROWS):
        for j in range(COLS):
            x = x0 + k * L
            ind = base + (i * COLS + j) * 4
            _cella(ax, x, 1.2, L, H, str(m[i][j]), fc=R0 if i == 0 else R1, ec=EC0 if i == 0 else EC1, bold=True, fs=11)
            ax.text(x + L / 2, 2.15, f"m[{i}][{j}]", ha="center", fontsize=8, color=BLU)
            ax.text(x + L / 2, 0.85, hex(ind).upper().replace("0X", "0x"), ha="center", fontsize=7.8, color=GRIGIO)
            k += 1
    ax.text(x0 + 1.5 * L, 2.65, "riga 0", ha="center", fontsize=9, color=EC0)
    ax.text(x0 + 4.5 * L, 2.65, "riga 1", ha="center", fontsize=9, color=EC1)
    i, j = 1, 2
    pos = i * COLS + j
    ind = base + pos * 4
    assert ind == 0x3FC
    ax.add_patch(FancyArrowPatch((2 * L + L / 2, 0.35), (x0 + pos * L + L / 2, 0.6), connectionstyle="arc3,rad=0.2",
                                 arrowstyle="-|>", mutation_scale=13, color=ROSSO, lw=1.5))
    ax.text(6.6, -1.6, "indirizzo di m[i][j] = base(m) + (i · COLS + j) × sizeof(int)", ha="center", fontsize=10)
    ax.text(6.6, -2.5, f"m[1][2]:  0x3E8 + (1 · 3 + 2) × 4 = 0x3E8 + 20 = {hex(ind).upper().replace('0X', '0x')}",
            ha="center", fontsize=10, color=ROSSO)
    ax.text(6.6, -3.5, "per il calcolo serve COLS, non ROWS", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "prog/matrice_memoria")


if __name__ == "__main__":
    for f in (matrice_memoria,):
        print(f())
