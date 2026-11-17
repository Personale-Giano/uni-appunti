"""Figure dei capitoli 52-54 di Algebra lineare (cambio di base, composizione, matrici simili). PNG in _sistema/figure/alg/.
Uso: python figure_alg7.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, FancyArrowPatch, _salva


def _fr(ax, a, b, col, lw=2.2, ls="-"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13, color=col, lw=lw, linestyle=ls,
                                 shrinkA=0, shrinkB=0))


def _piano(ax, titolo):
    ax.set_aspect("equal"); ax.set_xlim(-2.2, 5.2); ax.set_ylim(-1.6, 8.0)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title(titolo, fontsize=10.5)


def cambio_base_vettore():
    """Lo stesso vettore v = (3, 7) letto nella base canonica e nella base w1 = (1, 1), w2 = (1, 2)."""
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 5.6))
    # sinistra: base canonica
    ax = axs[0]; _piano(ax, "base canonica: v = 3e₁ + 7e₂")
    for k in range(-2, 6):
        ax.plot([k, k], [-1.6, 8], color="#e3e7ee", lw=0.8)
    for k in range(-1, 8):
        ax.plot([-2.2, 5.2], [k, k], color="#e3e7ee", lw=0.8)
    ax.axhline(0, color="#9aa3b2", lw=0.9); ax.axvline(0, color="#9aa3b2", lw=0.9)
    _fr(ax, (0, 0), (3, 0), BLU, lw=1.6, ls="--"); _fr(ax, (3, 0), (3, 7), VERDE, lw=1.6, ls="--")
    _fr(ax, (0, 0), (1, 0), BLU, lw=2.8); _fr(ax, (0, 0), (0, 1), VERDE, lw=2.8)
    _fr(ax, (0, 0), (3, 7), ROSSO, lw=2.4)
    ax.text(0.45, -0.55, "e₁", color=BLU, fontsize=11, fontweight="bold")
    ax.text(-0.6, 0.45, "e₂", color=VERDE, fontsize=11, fontweight="bold")
    ax.text(1.7, -0.6, "3 volte e₁", color=BLU, fontsize=9.5)
    ax.text(3.15, 3.3, "7 volte e₂", color=VERDE, fontsize=9.5)
    ax.text(1.75, 7.3, "v = (3, 7)", color=ROSSO, fontsize=11, fontweight="bold")
    ax.text(1.5, -1.35, "coordinate: (3, 7)", ha="center", fontsize=10.5, color="black")
    # destra: base w1, w2
    ax = axs[1]; _piano(ax, "base {w₁, w₂}: v = −1·w₁ + 4·w₂")
    w1, w2 = np.array([1.0, 1.0]), np.array([1.0, 2.0])
    for k in range(-8, 9):  # reticolo della base: rette parallele a w1 e a w2
        p = k * w2; ax.plot([p[0] - 30, p[0] + 30], [p[1] - 30, p[1] + 30], color="#e3e7ee", lw=0.8)
        p = k * w1; ax.plot([p[0] - 30, p[0] + 30], [p[1] - 60, p[1] + 60], color="#e3e7ee", lw=0.8)
    _fr(ax, (0, 0), (-1, -1), BLU, lw=1.6, ls="--"); _fr(ax, (-1, -1), (3, 7), VERDE, lw=1.6, ls="--")
    _fr(ax, (0, 0), tuple(w1), BLU, lw=2.8); _fr(ax, (0, 0), tuple(w2), VERDE, lw=2.8)
    _fr(ax, (0, 0), (3, 7), ROSSO, lw=2.4)
    ax.plot([0], [0], "o", color="black", ms=4)
    ax.text(1.1, 0.75, "w₁ = (1, 1)", color=BLU, fontsize=10, fontweight="bold")
    ax.text(-1.25, 2.1, "w₂ = (1, 2)", color=VERDE, fontsize=10, fontweight="bold")
    ax.text(-2.1, -0.45, "−1 volta w₁", color=BLU, fontsize=9.5)
    ax.text(1.5, 2.6, "4 volte w₂", color=VERDE, fontsize=9.5)
    ax.text(1.75, 7.3, "v = (3, 7)", color=ROSSO, fontsize=11, fontweight="bold")
    ax.text(1.5, -1.35, "coordinate: (−1, 4)", ha="center", fontsize=10.5, color="black")
    fig.tight_layout()
    return _salva(fig, "alg/cambio_base_vettore")


def _onda(ax, x0, x1, y):
    t = np.linspace(x0, x1, 400)
    ax.plot(t, y + 0.08 * np.sin(2 * np.pi * (t - x0) / 1.05), color=GRIGIO, lw=1.2)


def composizione_teoria_calcoli():
    """Sopra: V -> W -> U con g∘f; sotto: K^n -> K^m -> K^p con le matrici associate e il prodotto."""
    fig, ax = plt.subplots(figsize=(8.2, 4.6)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 7.2)
    xs = (2.0, 6.0, 10.0)
    for x, nome in zip(xs, ("V  (base B)", "W  (base C)", "U  (base D)")):
        ax.text(x, 5.2, nome, ha="center", va="center", fontsize=15)
    for x, nome in zip(xs, (r"$\mathbb{K}^{n}$", r"$\mathbb{K}^{m}$", r"$\mathbb{K}^{p}$")):
        ax.text(x, 1.9, nome, ha="center", va="center", fontsize=16)
    _fr(ax, (3.25, 5.2), (4.75, 5.2), BLU); ax.text(4.0, 5.45, "f", color=BLU, ha="center", fontsize=14)
    _fr(ax, (7.25, 5.2), (8.75, 5.2), BLU); ax.text(8.0, 5.45, "g", color=BLU, ha="center", fontsize=14)
    ax.add_patch(FancyArrowPatch((2.0, 5.65), (10.0, 5.65), connectionstyle="arc3,rad=-0.22", arrowstyle="-|>",
                                 mutation_scale=13, color=ARANCIO, lw=2))
    ax.text(6.0, 6.85, "g ∘ f", color=ARANCIO, ha="center", fontsize=14)
    for x in xs:
        _fr(ax, (x, 4.75), (x, 2.4), VERDE, lw=1.8)
    _onda(ax, 0.3, 11.7, 3.55)
    ax.text(0.3, 6.6, "TEORIA", color=GRIGIO, fontsize=11, fontweight="bold")
    ax.text(0.3, 0.15, "CALCOLI", color=GRIGIO, fontsize=11, fontweight="bold")
    _fr(ax, (2.7, 1.9), (5.3, 1.9), ROSSO); ax.text(4.0, 2.15, r"$[f]^{B}_{C}$", color=ROSSO, ha="center", fontsize=13)
    _fr(ax, (6.7, 1.9), (9.3, 1.9), ROSSO); ax.text(8.0, 2.15, r"$[g]^{C}_{D}$", color=ROSSO, ha="center", fontsize=13)
    ax.add_patch(FancyArrowPatch((2.0, 1.45), (10.0, 1.45), connectionstyle="arc3,rad=0.2", arrowstyle="-|>",
                                 mutation_scale=13, color=ARANCIO, lw=2))
    ax.text(6.0, 0.25, r"$[g \circ f]^{B}_{D} = [g]^{C}_{D} \cdot [f]^{B}_{C}$", color=ARANCIO, ha="center", fontsize=13)
    return _salva(fig, "alg/composizione_teoria_calcoli")


def cambio_base_mappa():
    """f = I_W ∘ f ∘ I_V con le basi B′, B, C, C′ lungo il percorso e le tre matrici corrispondenti."""
    fig, ax = plt.subplots(figsize=(8.6, 3.3)); ax.axis("off"); ax.set_xlim(0, 13); ax.set_ylim(0, 5.0)
    xs = (1.3, 4.7, 8.3, 11.7)
    for x, sp, base, vet in zip(xs, ("V", "V", "W", "W"), ("B′", "B", "C", "C′"), ("v", "v", "f(v)", "f(v)")):
        ax.text(x, 3.9, sp, ha="center", va="center", fontsize=17)
        ax.text(x, 3.15, f"base {base}", ha="center", va="center", fontsize=10.5, color=VERDE)
        ax.text(x, 2.45, vet, ha="center", va="center", fontsize=11, color=GRIGIO)
    for (a, b), nome, col in zip(((xs[0], xs[1]), (xs[1], xs[2]), (xs[2], xs[3])), (r"$I_{V}$", "f", r"$I_{W}$"), (GRIGIO, BLU, GRIGIO)):
        _fr(ax, (a + 0.55, 3.9), (b - 0.55, 3.9), col)
        ax.text((a + b) / 2, 4.2, nome, ha="center", fontsize=13, color=col)
        ax.text((a + b) / 2, 2.45, "↦", ha="center", va="center", fontsize=12, color=GRIGIO)
    for (a, b), m, col in zip(((xs[0], xs[1]), (xs[1], xs[2]), (xs[2], xs[3])),
                              (r"$[I_{V}]^{B'}_{B} = P^{-1}$", r"$[f]^{B}_{C}$", r"$[I_{W}]^{C}_{C'} = Q$"), (ROSSO, ROSSO, ROSSO)):
        ax.text((a + b) / 2, 1.45, m, ha="center", va="center", fontsize=12.5, color=col)
    ax.text(6.5, 0.4, r"$[f]^{B'}_{C'} = Q \cdot [f]^{B}_{C} \cdot P^{-1}$   (le matrici si scrivono da destra a sinistra)",
            ha="center", va="center", fontsize=11.5, color=ARANCIO)
    return _salva(fig, "alg/cambio_base_mappa")


if __name__ == "__main__":
    for f in (cambio_base_vettore, composizione_teoria_calcoli, cambio_base_mappa):
        print(f())
