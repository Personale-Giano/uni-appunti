"""Figure dei capitoli 64-67 di Algebra lineare (prodotti scalari I). PNG in _sistema/figure/alg/.
Uso: python figure_alg9.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
from matplotlib.patches import Arc
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, FancyArrowPatch, _salva


def _fr(ax, a, b, col, lw=2.2, ls="-"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13, color=col, lw=lw, linestyle=ls,
                                 shrinkA=0, shrinkB=0))


def _assi(ax, xlim, ylim, titolo):
    ax.set_aspect("equal"); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.axhline(0, color="#c3c9d4", lw=0.8); ax.axvline(0, color="#c3c9d4", lw=0.8)
    ax.set_title(titolo, fontsize=10.5)


def prodotto_scalare_angolo():
    """Tre casi del prodotto scalare euclideo in ℝ²: angolo acuto, retto, ottuso."""
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 2.9))
    v = np.array([2.0, 0.0])
    casi = (((1.0, 1.5), "angolo acuto: ⟨v, w⟩ = 2 > 0", VERDE),
            ((0.0, 1.8), "angolo retto: ⟨v, w⟩ = 0", ARANCIO),
            ((-1.2, 1.2), "angolo ottuso: ⟨v, w⟩ = −2,4 < 0", ROSSO))
    for ax, (w, tit, col) in zip(axs, casi):
        _assi(ax, (-1.8, 2.6), (-0.7, 2.3), tit)
        w = np.array(w)
        _fr(ax, (0, 0), tuple(v), BLU, lw=2.8); _fr(ax, (0, 0), tuple(w), col, lw=2.8)
        ax.text(v[0] - 0.1, -0.38, "v = (2, 0)", color=BLU, fontsize=10.5, fontweight="bold", ha="right")
        ax.text(w[0] + (0.12 if w[0] >= 0 else -0.12), w[1] + 0.12, "w = (%s, %s)" % (
            ("%g" % w[0]).replace(".", ",").replace("-", "−"), ("%g" % w[1]).replace(".", ",")),
            color=col, fontsize=10.5, fontweight="bold", ha="left" if w[0] >= 0 else "right")
        ang = np.degrees(np.arctan2(w[1], w[0]))
        ax.add_patch(Arc((0, 0), 0.9, 0.9, theta1=0, theta2=ang, color=GRIGIO, lw=1.4))
        m = np.radians(ang / 2)
        ax.text(0.62 * np.cos(m), 0.62 * np.sin(m), "θ", fontsize=12, color="black", ha="center", va="center")
        if abs(ang - 90) < 1e-6:
            ax.plot([0.22, 0.22, 0], [0, 0.22, 0.22], color=GRIGIO, lw=1.2)
    fig.suptitle("⟨v, w⟩ = ‖v‖·‖w‖·cos θ: il segno del prodotto scalare dice se l'angolo è acuto, retto o ottuso",
                 fontsize=11, y=1.03)
    return _salva(fig, "alg/prodotto_scalare_angolo")


def coordinate_base_b():
    """v = (2, 3) e w = (1, 2) nella base B = {v₁ = (0, 1), v₂ = (1, 1)}."""
    fig, ax = plt.subplots(figsize=(6.0, 5.6))
    _assi(ax, (-0.6, 3.4), (-0.6, 4.1), "Coordinate nella base B = {v₁ = (0, 1), v₂ = (1, 1)}")
    v1, v2 = np.array([0.0, 1.0]), np.array([1.0, 1.0])
    # reticolo della base B
    for k in range(-3, 6):
        ax.plot(*zip(*(k * v1 + s * v2 for s in (-2, 6))), color="#e3e7ee", lw=0.8, zorder=0)
        ax.plot(*zip(*(s * v1 + k * v2 for s in (-2, 6))), color="#e3e7ee", lw=0.8, zorder=0)
    v = 1 * v1 + 2 * v2; w = 1 * v1 + 1 * v2
    # v = v1 + 2 v2
    _fr(ax, (0, 0), tuple(2 * v2), GRIGIO, lw=1.4, ls="--")
    _fr(ax, tuple(2 * v2), tuple(v), GRIGIO, lw=1.4, ls="--")
    _fr(ax, (0, 0), tuple(v1), VERDE, lw=3.0); _fr(ax, (0, 0), tuple(v2), ARANCIO, lw=3.0)
    _fr(ax, (0, 0), tuple(v), BLU, lw=2.6); _fr(ax, (0, 0), tuple(w), ROSSO, lw=2.6)
    ax.text(-0.12, 0.55, "v₁", color=VERDE, fontsize=12, fontweight="bold", ha="right")
    ax.text(0.68, 0.45, "v₂", color=ARANCIO, fontsize=12, fontweight="bold")
    ax.text(v[0] + 0.1, v[1] + 0.05, "v = (2, 3) = v₁ + 2v₂\ncoordinate in B: (1, 2)", color=BLU, fontsize=10.5,
            fontweight="bold", va="bottom", ha="center")
    ax.text(w[0] - 0.12, w[1] + 0.1, "w = (1, 2) = v₁ + v₂\ncoordinate in B: (1, 1)", color=ROSSO, fontsize=10.5,
            fontweight="bold", ha="right", va="bottom")
    ax.text(2.25, 1.75, "2v₂", color=GRIGIO, fontsize=10)
    return _salva(fig, "alg/coordinate_base_b")


if __name__ == "__main__":
    for f in (prodotto_scalare_angolo, coordinate_base_b):
        print(f())
