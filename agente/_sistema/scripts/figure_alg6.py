"""Figure dei capitoli 38-46 di Algebra lineare (sistemi lineari). PNG in _sistema/figure/alg/.
Uso: python figure_alg6.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
from figure_math import BLU, ROSSO, VERDE, GRIGIO, plt, Rectangle, _salva


def matrice_scalini():
    """Una matrice a scalini con i pivot evidenziati e la scala disegnata."""
    M = [["1", "3", "0", "2", "5"], ["0", "0", "2", "-1", "4"], ["0", "0", "0", "3", "1"], ["0", "0", "0", "0", "0"]]
    piv = {(0, 0), (1, 2), (2, 3)}
    fig, ax = plt.subplots(figsize=(5.2, 3.0)); ax.axis("off"); ax.set_aspect("equal"); ax.set_xlim(-0.3, 7.8); ax.set_ylim(-4.5, 0.4)
    for i, r in enumerate(M):
        for j, v in enumerate(r):
            p = (i, j) in piv
            ax.add_patch(Rectangle((j, -i - 1), 1, 1, fc="#FFE3D6" if p else ("#F3F4F6" if v == "0" else "white"), ec="#c5cede", lw=0.8))
            ax.text(j + 0.5, -i - 0.5, v, ha="center", va="center", fontsize=13, color=ROSSO if p else ("#9aa3b2" if v == "0" else "black"), fontweight="bold" if p else None)
    xs, ys = [0, 0, 2, 2, 3, 3, 5], [0, -1, -1, -2, -2, -3, -3]
    ax.plot(xs, ys, color=ROSSO, lw=2.2)
    ax.text(5.25, -0.5, "pivot: il primo elemento\nnon nullo di ogni riga", fontsize=9.5, color=ROSSO, va="center")
    ax.text(5.25, -2.5, "ogni pivot sta più a destra\ndi quello sopra", fontsize=9.5, color=GRIGIO, va="center")
    ax.text(5.25, -3.5, "le righe nulle stanno\nin fondo", fontsize=9.5, color=GRIGIO, va="center")
    return _salva(fig, "alg/matrice_scalini")


def _retta(ax, a, b, c, col, **kw):
    """Disegna a x + b y = c nella finestra [-5, 7] x [-4, 5]."""
    xs = np.array([-5.0, 7.0])
    ax.plot(xs, (c - a * xs) / b, color=col, lw=2, **kw)


def _assi(ax, titolo):
    ax.set_xlim(-5, 7); ax.set_ylim(-4, 5); ax.set_aspect("equal")
    ax.axhline(0, color="#bbb", lw=0.8); ax.axvline(0, color="#bbb", lw=0.8)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(titolo, fontsize=10.5)


def tre_casi():
    """Esempio 12.9: x + ky = 4 - k, kx + 4y = 4 per k = 1, k = -2 e k = 2."""
    fig, axs = plt.subplots(1, 3, figsize=(10.2, 3.1))
    _assi(axs[0], "k = 1: una soluzione")
    _retta(axs[0], 1, 1, 3, BLU); _retta(axs[0], 1, 4, 4, VERDE)
    axs[0].plot([8 / 3], [1 / 3], "o", color=ROSSO, ms=7)
    axs[0].annotate("(8/3, 1/3)", xy=(8 / 3, 1 / 3), xytext=(3.2, 1.9), fontsize=10, color=ROSSO)
    axs[0].set_xlabel("rk(A) = rk(A | b) = 2", fontsize=9.5)
    _assi(axs[1], "k = -2: nessuna soluzione")
    _retta(axs[1], 1, -2, 6, BLU); _retta(axs[1], -2, 4, 4, VERDE)
    axs[1].set_xlabel("rk(A) = 1, rk(A | b) = 2", fontsize=9.5)
    _assi(axs[2], "k = 2: infinite soluzioni")
    _retta(axs[2], 1, 2, 2, ROSSO)
    axs[2].set_xlabel("rk(A) = rk(A | b) = 1", fontsize=9.5)
    axs[2].text(0.4, 4.4, "le due equazioni\ndanno la stessa retta", fontsize=9.5, color=ROSSO, va="top")
    fig.tight_layout()
    return _salva(fig, "alg/rouche_tre_casi")


def soluzioni_affini():
    """S0 passa per l'origine; S = x + S0 è la stessa retta spostata (x + 2y = 0 e x + 2y = 2)."""
    fig, ax = plt.subplots(figsize=(5.0, 3.5))
    _assi(ax, "")
    _retta(ax, 1, 2, 0, BLU); _retta(ax, 1, 2, 2, ROSSO)
    ax.plot([0], [0], "o", color=BLU, ms=5)
    ax.plot([2], [0], "o", color=ROSSO, ms=7)
    ax.text(2.2, 0.25, "soluzione particolare x = (2, 0)", fontsize=9.5, color=ROSSO)
    ax.text(-4.8, 3.6, "S: x + 2y = 2", fontsize=10.5, color=ROSSO)
    ax.text(-4.8, -1.2, "S₀: x + 2y = 0", fontsize=10.5, color=BLU)
    ax.annotate("", xy=(2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=1.8))
    ax.text(0.6, -0.65, "x", fontsize=10.5, color=VERDE)
    return _salva(fig, "alg/soluzioni_affini")


if __name__ == "__main__":
    for f in (matrice_scalini, tre_casi, soluzioni_affini):
        print(f())
