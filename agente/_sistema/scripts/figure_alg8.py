"""Figure dei capitoli 59-63 di Algebra lineare (autovalori e autovettori). PNG in _sistema/figure/alg/.
Uso: python figure_alg8.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, FancyArrowPatch, _salva


def _fr(ax, a, b, col, lw=2.2, ls="-"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13, color=col, lw=lw, linestyle=ls,
                                 shrinkA=0, shrinkB=0))


def _assi(ax, lim, titolo):
    ax.set_aspect("equal"); ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.axhline(0, color="#9aa3b2", lw=0.9); ax.axvline(0, color="#9aa3b2", lw=0.9)
    ax.set_title(titolo, fontsize=10.5)


def autovettori_iterate():
    """Sinistra: (1 0 ; 0 1/2) schiaccia verso l'asse x. Destra: (1 2 ; 2 1) nella base {(1, 1), (1, −1)}."""
    fig, axs = plt.subplots(1, 2, figsize=(10.2, 5.2))
    # sinistra
    ax = axs[0]; _assi(ax, 3.6, "A = ( 1 0 ; 0 ½ ): la y si dimezza a ogni passo")
    ax.set_xlim(-0.8, 3.6); ax.set_ylim(-0.8, 3.6)
    pts = [(2.0, 3.2 / 2 ** k) for k in range(6)]
    for k, p in enumerate(pts):
        ax.plot(*p, "o", color=ROSSO if k == 0 else BLU, ms=6 if k == 0 else 5)
    for p, q in zip(pts[:-1], pts[1:]):
        _fr(ax, (p[0] + 0.12, p[1] - 0.04), (q[0] + 0.12, q[1] + 0.04), GRIGIO, lw=1.2)
    ax.text(2.15, 3.2, "(x, y)", color=ROSSO, fontsize=11, fontweight="bold", va="center")
    ax.text(2.3, 1.6, "(x, y/2)", color=BLU, fontsize=10.5, va="center")
    ax.text(2.3, 0.8, "(x, y/4)", color=BLU, fontsize=10.5, va="center")
    ax.text(2.3, 0.25, "…  verso l'asse x", color=BLU, fontsize=10, va="center")
    _fr(ax, (0, 0), (1, 0), VERDE, lw=2.6); _fr(ax, (0, 0), (0, 1), VERDE, lw=2.6)
    ax.text(0.35, -0.42, "e₁ ↦ e₁", color=VERDE, fontsize=10)
    ax.text(-0.75, 1.15, "e₂ ↦ ½e₂", color=VERDE, fontsize=10)
    # destra
    ax = axs[1]; _assi(ax, 3.4, "A = ( 1 2 ; 2 1 ): assi girati di 45°")
    for d, col, nome in (((1, 1), BLU, "retta di v₁: si triplica"), ((1, -1), VERDE, "retta di v₂: si ribalta")):
        d = np.array(d, float)
        ax.plot([-4 * d[0], 4 * d[0]], [-4 * d[1], 4 * d[1]], color=col, lw=1, ls=":")
    ax.text(1.55, 2.95, "retta di v₁: si triplica", color=BLU, fontsize=9.5, ha="center")
    ax.text(2.0, -2.75, "retta di v₂: si ribalta", color=VERDE, fontsize=9.5, ha="center")
    v1, v2 = np.array([1.0, 1.0]), np.array([1.0, -1.0])
    _fr(ax, (0, 0), tuple(v1), BLU, lw=2.8); _fr(ax, (0, 0), tuple(v2), VERDE, lw=2.8)
    ax.text(0.95, 0.55, "v₁", color=BLU, fontsize=11, fontweight="bold")
    ax.text(0.55, -1.25, "v₂", color=VERDE, fontsize=11, fontweight="bold")
    a, b = 0.5, 1.0
    v = a * v1 + b * v2; Av = 3 * a * v1 - b * v2
    _fr(ax, (0, 0), tuple(v), ROSSO, lw=2.4); _fr(ax, (0, 0), tuple(Av), ARANCIO, lw=2.4)
    ax.plot([a * v1[0], v[0]], [a * v1[1], v[1]], color=GRIGIO, lw=1, ls="--")
    ax.plot([3 * a * v1[0], Av[0]], [3 * a * v1[1], Av[1]], color=GRIGIO, lw=1, ls="--")
    ax.text(v[0] + 0.1, v[1] - 0.3, "v = ½v₁ + v₂", color=ROSSO, fontsize=10.5, fontweight="bold")
    ax.text(Av[0] - 2.6, Av[1] + 0.1, "A·v = (3/2)v₁ − v₂", color=ARANCIO, fontsize=10.5, fontweight="bold")
    fig.tight_layout()
    return _salva(fig, "alg/autovettori_iterate")


def rotazione_senza_autovettori():
    """Rotazione di 90°: nessun vettore non nullo resta sulla sua retta."""
    fig, ax = plt.subplots(figsize=(5.2, 5.0)); _assi(ax, 2.6, "Rot di 90°: (x, y) ↦ (−y, x)")
    angoli = (15, 70, 200)
    for k, ang in enumerate(angoli):
        r = 1.6 + 0.35 * (k % 2)
        th = np.radians(ang)
        v = np.array([np.cos(th), np.sin(th)]) * r
        w = np.array([-v[1], v[0]])
        ax.plot([-3 * v[0], 3 * v[0]], [-3 * v[1], 3 * v[1]], color="#e3e7ee", lw=0.8, zorder=0)
        _fr(ax, (0, 0), tuple(v), BLU, lw=2.0); _fr(ax, (0, 0), tuple(w), ROSSO, lw=1.6, ls="--")
    th = np.radians(15); v = np.array([np.cos(th), np.sin(th)]) * 1.6
    ax.text(v[0] + 0.05, v[1] - 0.3, "v", color=BLU, fontsize=12, fontweight="bold")
    ax.text(-v[1] - 0.12, v[0] + 0.05, "Rot(v)", color=ROSSO, fontsize=11, fontweight="bold", ha="right")
    ax.text(0, -2.45, "blu: v   rosso: Rot(v), sempre perpendicolare a v", ha="center", fontsize=9.5, color="black")
    return _salva(fig, "alg/rotazione_senza_autovettori")


def autospazi_2112():
    """A = (2 1 ; 1 2): sulle due rette degli autovettori A agisce come un numero; fuori no."""
    fig, ax = plt.subplots(figsize=(6.0, 5.6)); _assi(ax, 3.5, "A = ( 2 1 ; 1 2 ): autospazi V₃ e V₁")
    ax.plot([-4, 4], [-4, 4], color=BLU, lw=1.2, ls=":"); ax.plot([4, -4], [-4, 4], color=VERDE, lw=1.2, ls=":")
    ax.text(2.9, 3.3, "V₃ = Span(1, 1)", color=BLU, fontsize=10, ha="right")
    ax.text(-2.9, 3.3, "V₁ = Span(−1, 1)", color=VERDE, fontsize=10, ha="left")
    _fr(ax, (0, 0), (3, 3), BLU, lw=1.6, ls="--"); _fr(ax, (0, 0), (1, 1), BLU, lw=2.8)
    ax.text(1.05, 0.6, "(1, 1)", color=BLU, fontsize=10.5, fontweight="bold")
    ax.text(1.9, 2.7, "A·(1, 1) = (3, 3)", color=BLU, fontsize=10, ha="right")
    _fr(ax, (0, 0), (-1, 1), VERDE, lw=2.8)
    ax.text(-1.2, 0.55, "A·(−1, 1) = (−1, 1)", color=VERDE, fontsize=10, ha="right")
    _fr(ax, (0, 0), (1, 0), ROSSO, lw=2.4); _fr(ax, (0, 0), (2, 1), ARANCIO, lw=2.0, ls="--")
    ax.text(0.55, -0.4, "e₁", color=ROSSO, fontsize=11, fontweight="bold")
    ax.text(2.1, 0.7, "A·e₁ = (2, 1)", color=ARANCIO, fontsize=10)
    return _salva(fig, "alg/autospazi_2112")


if __name__ == "__main__":
    for f in (autovettori_iterate, rotazione_senza_autovettori, autospazi_2112):
        print(f())
