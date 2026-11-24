"""Figure del Word di Matematica discreta (capitoli 1-19). Genera i PNG in _sistema/figure/mate/ e restituisce il PIANO di
inserimento: lista di (indice del paragrafo dopo cui inserire, nome file, didascalia, larghezza in cm).
Uso: python figure_mate.py          (genera tutte le figure e scrive figure/mate/piano.json)
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figure_math as fm
from figure_math import (BLU, ROSSO, VERDE, ARANCIO, GRIGIO, OUT, np, plt, Circle, Ellipse, Rectangle, FancyArrowPatch, Arc,
                         ovali_ax, venn_ax, pannelli, _salva)

PIANO = []


def reg(indice, nome, didascalia, larg=11.0):
    PIANO.append(dict(dopo=indice, figura=f"figure/{nome}.png", didascalia=didascalia, larghezza=larg))


def fig1(nome, fig):
    return _salva(fig, nome)


# ---------------------------------------------------------------- capitoli 1-4: insiemi
def insieme_venn():
    fig, ax = plt.subplots(figsize=(3.8, 3.2))
    venn_ax(ax, {"A": {1, 2, 3}}, universo=True)
    ax.text(1.35, -1.35, "5", fontsize=11); ax.text(1.35, 1.35, "5 ∉ A", fontsize=10, color=ROSSO, ha="center")
    return _salva(fig, "mate/ch01_venn_insieme")


def sottoinsieme():
    fig, ax = plt.subplots(figsize=(4.4, 3.4)); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Ellipse((0, 0), 4.6, 3.2, fill=False, ec=ROSSO, lw=2)); ax.add_patch(Circle((-0.4, 0), 1.0, fill=False, ec=BLU, lw=2))
    ax.text(-0.4, 1.25, "S", color=BLU, fontsize=14, style="italic", ha="center"); ax.text(1.55, 1.1, "T", color=ROSSO, fontsize=14, style="italic")
    ax.text(-0.4, 0, "1, 2", ha="center", va="center", fontsize=12); ax.text(1.25, -0.1, "3, 4", ha="center", va="center", fontsize=12)
    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-1.9, 1.9)
    ax.set_title("S ⊆ T: ogni elemento di S sta anche in T", fontsize=11)
    return _salva(fig, "mate/ch02_sottoinsieme")


def scatole_cinesi():
    fig, ax = plt.subplots(figsize=(4.6, 3.2)); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Ellipse((0, 0), 5.2, 3.2, fill=False, ec="black", lw=2)); ax.add_patch(Ellipse((-1.2, 0), 2.0, 1.8, fill=False, ec=BLU, lw=2))
    ax.text(0, 1.8, "B = {A, 3}", ha="center", fontsize=12); ax.text(-1.2, 1.1, "A = {1, 2}", ha="center", color=BLU, fontsize=11)
    ax.text(-1.2, 0, "1   2", ha="center", va="center", fontsize=12); ax.text(1.4, 0, "3", ha="center", va="center", fontsize=13)
    ax.set_xlim(-2.8, 2.8); ax.set_ylim(-1.8, 2.1)
    ax.set_title("A ∈ B (A è un elemento di B), ma 1 ∉ B", fontsize=10)
    return _salva(fig, "mate/ch02_scatole_cinesi")


def unione_intersezione():
    ins = {"X": {1, 2}, "Y": {2, 3}}
    d = [lambda ax: venn_ax(ax, ins, evidenzia=lambda m: m["X"] & m["Y"], universo=True, titolo="X ∩ Y", fs=10),
         lambda ax: venn_ax(ax, ins, evidenzia=lambda m: m["X"] | m["Y"], universo=True, titolo="X ∪ Y", fs=10)]
    return pannelli("mate/ch03_unione_intersezione", d, larghezza=3.5, altezza=3.0)


def prodotto_griglia():
    A, B = [1, 2, 3], ["a", "b"]
    fig, ax = plt.subplots(figsize=(4.2, 2.8))
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            ax.add_patch(Rectangle((i, j), 1, 1, fc="#eaf1fb", ec="#555", lw=1)); ax.text(i + 0.5, j + 0.5, f"({a}, {b})", ha="center", va="center", fontsize=11)
    ax.set_xlim(0, 3); ax.set_ylim(0, 2); ax.set_aspect("equal")
    ax.set_xticks([0.5, 1.5, 2.5]); ax.set_xticklabels(A); ax.set_yticks([0.5, 1.5]); ax.set_yticklabels(B)
    ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]
    ax.set_xlabel("A = {1, 2, 3}", style="italic"); ax.set_ylabel("B = {a, b}", style="italic")
    ax.set_title("A × B: 3 · 2 = 6 coppie ordinate", fontsize=11)
    return _salva(fig, "mate/ch03_prodotto_cartesiano")


def differenza():
    ins = {"A": {1, 2}, "B": {2, 3}}
    d = [lambda ax: venn_ax(ax, ins, evidenzia=lambda m: m["A"] & ~m["B"], universo=True, titolo="A ∖ B = {1}", fs=10),
         lambda ax: venn_ax(ax, ins, evidenzia=lambda m: m["B"] & ~m["A"], universo=True, titolo="B ∖ A = {3}", fs=10)]
    return pannelli("mate/ch04_differenza", d, larghezza=3.5, altezza=3.0)


def complementare():
    fig, ax = plt.subplots(figsize=(3.9, 3.2)); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Rectangle((-2.2, -1.7), 4.4, 3.4, fc="#cfe1f5", ec="black", lw=1.2)); ax.add_patch(Circle((-0.3, 0), 1.0, fc="white", ec=BLU, lw=2))
    ax.text(-0.3, 0, "S", ha="center", va="center", fontsize=15, style="italic", color=BLU); ax.text(2.05, 1.5, "A", ha="right", va="top", fontsize=13, style="italic")
    ax.text(1.35, -0.9, "C$_A$(S)", fontsize=12, ha="center")
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-1.8, 1.8)
    ax.set_title("L'area azzurra è il complementare di S rispetto ad A", fontsize=10)
    return _salva(fig, "mate/ch04_complementare")


def demorgan():
    ins = {"S": {1}, "T": {2}}
    kw = dict(universo=True, mostra_elementi=False, fs=10)
    d = [lambda ax: venn_ax(ax, ins, evidenzia=lambda m: ~(m["S"] | m["T"]), titolo="C(S ∪ T)", **kw),
         lambda ax: venn_ax(ax, ins, evidenzia=lambda m: ~m["S"] & ~m["T"], titolo="C(S) ∩ C(T)", **kw),
         lambda ax: venn_ax(ax, ins, evidenzia=lambda m: ~(m["S"] & m["T"]), titolo="C(S ∩ T)", **kw),
         lambda ax: venn_ax(ax, ins, evidenzia=lambda m: ~m["S"] | ~m["T"], titolo="C(S) ∪ C(T)", **kw)]
    return pannelli("mate/ch04_de_morgan", d, ncols=2, larghezza=3.4, altezza=2.8)


def insieme_parti():
    fig, ax = plt.subplots(figsize=(5.2, 3.6)); ax.axis("off")
    livelli = [["∅"], ["{a}", "{b}", "{c}"], ["{a,b}", "{a,c}", "{b,c}"], ["{a,b,c}"]]
    pos = {}
    for r, lv in enumerate(livelli):
        for k, nm in enumerate(lv):
            x = (k - (len(lv) - 1) / 2) * 2.2; y = 3 - r * 1.5; pos[nm] = (x, y)
    arch = [("∅", "{a}"), ("∅", "{b}"), ("∅", "{c}"), ("{a}", "{a,b}"), ("{a}", "{a,c}"), ("{b}", "{a,b}"), ("{b}", "{b,c}"), ("{c}", "{a,c}"), ("{c}", "{b,c}"),
            ("{a,b}", "{a,b,c}"), ("{a,c}", "{a,b,c}"), ("{b,c}", "{a,b,c}")]
    for u, v in arch:
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1] - 0.18, pos[v][1] + 0.18], color=GRIGIO, lw=1.2, zorder=1)
    for nm, (x, y) in pos.items():
        ax.text(x, y, nm, ha="center", va="center", fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=BLU, lw=1.2), zorder=2)
    ax.set_xlim(-3.6, 3.6); ax.set_ylim(-2.0, 3.8)
    ax.set_title("P({a, b, c}) ha 8 elementi (le linee indicano l'inclusione)", fontsize=10)
    return _salva(fig, "mate/ch04_insieme_parti")


# ---------------------------------------------------------------- capitoli 5-9
def domino():
    fig, ax = plt.subplots(figsize=(5.8, 2.4)); ax.axis("off")
    etich = ["0", "1", "2", "…", "n", "n+1"]
    for k, e in enumerate(etich):
        ang = -8 * k if k < 5 else -45
        x = k * 1.15
        tr = matplotlib_transform(ax, x, ang)
        ax.add_patch(Rectangle((x, 0), 0.5, 1.5, fc="#fbeed3" if k < 5 else "#f6c6c0", ec="black", lw=1.2, transform=tr))
    for k, e in enumerate(etich):
        ax.text(k * 1.15 + 0.25 + (0.12 * k if k < 5 else 0.35), 0.6 if k < 5 else 1.0, e, ha="center", fontsize=11)
    ax.annotate("", xy=(6.5, 0.2), xytext=(0.6, 0.2), arrowprops=dict(arrowstyle="-|>", color=BLU, lw=1.5))
    ax.text(3.3, -0.55, "base: cade la tessera 0;  passo: se cade la n-esima, cade la (n+1)-esima", ha="center", fontsize=9.5, color=BLU)
    ax.set_xlim(-0.3, 7.5); ax.set_ylim(-0.9, 2.2)
    return _salva(fig, "mate/ch05_domino")


def matplotlib_transform(ax, x, ang):
    import matplotlib.transforms as mt
    return mt.Affine2D().rotate_deg_around(x + 0.25, 0, ang) + ax.transData


def ricoprimento():
    fig, ax = plt.subplots(figsize=(5.6, 2.8))
    ax.set_xlim(-0.3, 10.8); ax.set_ylim(-0.4, 3.6); ax.axis("off")
    ax.plot([0, 10.4], [0, 0], color="black", lw=1.2); ax.annotate("", xy=(10.7, 0), xytext=(10.2, 0), arrowprops=dict(arrowstyle="-|>", color="black"))
    for x, lab in ((0, "0"), (1.5, "100"), (4.0, "1000"), (8.0, "10 000")):
        ax.plot([x, x], [-0.08, 0.08], color="black"); ax.text(x, -0.35, lab, ha="center", fontsize=10)
    ax.add_patch(Rectangle((1.5, 0.3), 2.5, 0.0, fc="none")); ax.axvspan(1.5, 4.0, ymin=0.0, ymax=0.9, color="#f3d9a4", alpha=0.45, lw=0)
    for y, (a, b), nm, col in ((0.9, (0, 4.0), "A₁", BLU), (1.7, (1.5, 8.0), "A₂", ROSSO), (2.5, (4.0, 10.4), "A₃", VERDE)):
        ax.plot([a, b], [y, y], color=col, lw=5, solid_capstyle="butt"); ax.text((a + b) / 2, y + 0.18, nm, ha="center", color=col, fontsize=12, style="italic")
    ax.annotate("", xy=(10.75, 2.5), xytext=(10.2, 2.5), arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=2))
    ax.text(2.75, 3.15, "A₁ e A₂ si sovrappongono tra 100 e 1000", fontsize=9, ha="center", color=ARANCIO)
    return _salva(fig, "mate/ch06_ricoprimento")


def partizione_pari_dispari():
    fig, ax = plt.subplots(figsize=(4.6, 3.2)); ax.axis("off"); ax.set_aspect("equal")
    ax.add_patch(Ellipse((0, 0), 5.0, 3.4, fill=False, ec="black", lw=2)); ax.plot([0, 0], [-1.7, 1.7], color="black", lw=1.6)
    ax.text(-1.25, 0.15, "{0, 2, 4, 6, …}", ha="center", fontsize=11, color=BLU); ax.text(1.25, 0.15, "{1, 3, 5, 7, …}", ha="center", fontsize=11, color=ROSSO)
    ax.text(-1.25, 1.0, "P", ha="center", fontsize=14, style="italic", color=BLU); ax.text(1.25, 1.0, "D", ha="center", fontsize=14, style="italic", color=ROSSO)
    ax.text(0, 1.95, "ℕ", ha="center", fontsize=14, style="italic")
    ax.set_xlim(-2.8, 2.8); ax.set_ylim(-1.9, 2.3)
    ax.set_title("La partizione di ℕ in pari (P) e dispari (D)", fontsize=10)
    return _salva(fig, "mate/ch06_partizione_pari_dispari")


def non_partizione():
    fig, ax = plt.subplots(figsize=(4.2, 3.2))
    venn_ax(ax, {"A₁": {1, 2, 3}, "A₂": {3, 4, 5}}, universo=True, titolo="A₁ ∩ A₂ = {3} ≠ ∅: non è una partizione", fs=10)
    return _salva(fig, "mate/ch06_non_partizione")


def quoziente():
    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    ax.set_xlim(0, 11); ax.set_ylim(0, 6.2); ax.axis("off")
    ax.add_patch(Ellipse((2.6, 3.1), 4.2, 5.0, fill=False, ec="black", lw=1.6)); ax.plot([2.6, 2.6], [0.9, 5.3], color="black", lw=1.3)
    ax.text(2.6, 5.85, "ℕ", ha="center", fontsize=13, style="italic"); ax.text(1.8, 3.1, "P", ha="center", fontsize=14, color=BLU, style="italic"); ax.text(3.45, 3.1, "D", ha="center", fontsize=14, color=ROSSO, style="italic")
    ax.add_patch(Ellipse((8.6, 3.1), 2.2, 3.4, fill=False, ec="black", lw=1.6)); ax.text(8.6, 5.15, "Q = {P, D}", ha="center", fontsize=12)
    ax.plot(8.6, 3.9, "o", color=BLU); ax.plot(8.6, 2.3, "o", color=ROSSO); ax.text(8.9, 3.9, "P", fontsize=12, color=BLU, va="center"); ax.text(8.9, 2.3, "D", fontsize=12, color=ROSSO, va="center")
    ax.add_patch(FancyArrowPatch((1.95, 3.55), (8.4, 3.9), arrowstyle="-|>", mutation_scale=12, color=BLU, lw=1.4, connectionstyle="arc3,rad=-0.28")); ax.add_patch(FancyArrowPatch((3.9, 2.8), (8.4, 2.35), arrowstyle="-|>", mutation_scale=12, color=ROSSO, lw=1.4))
    ax.text(6.0, 0.4, "ogni blocco diventa un elemento di Q", fontsize=9.5, ha="center", color=GRIGIO)
    return _salva(fig, "mate/ch07_insieme_quoziente")


def relazione_divisibilita():
    fig, ax = plt.subplots(figsize=(4.8, 3.4)); ax.axis("off"); ax.set_aspect("equal")
    pos = {1: (-2, 0), 2: (0, 1.5), 3: (0, -1.5), 6: (2, 0)}
    for n, (x, y) in pos.items():
        ax.add_patch(Circle((x, y), 0.32, fc="white", ec="black", lw=1.4, zorder=3)); ax.text(x, y, str(n), ha="center", va="center", fontsize=12, zorder=4)
        ax.add_patch(Arc((x, y + 0.5 * (1 if y >= 0 else -1) + (0.06 if y >= 0 else -0.06)), 0.5, 0.5, theta1=0 if y >= 0 else 180, theta2=360 if y >= 0 else 540, color=GRIGIO, lw=1.1))
    for a, b in ((1, 2), (1, 3), (1, 6), (2, 6), (3, 6)):
        ax.add_patch(FancyArrowPatch(pos[a], pos[b], arrowstyle="-|>", mutation_scale=13, color=BLU, lw=1.5, shrinkA=14, shrinkB=14, zorder=2))
    ax.set_xlim(-3, 3); ax.set_ylim(-2.6, 2.6)
    ax.set_title("R = {(m, n) | m divide n} sull'insieme {1, 2, 3, 6}\n(i cappi indicano la riflessività)", fontsize=9.5)
    return _salva(fig, "mate/ch08_relazione_divisibilita")


def classi_equivalenza():
    fig, ax = plt.subplots(figsize=(5.6, 3.0)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 5.6)
    gruppi = [(2.0, "C₁ = [1] = [4] = [7]", [1, 4, 7], BLU), (6.0, "C₂ = [2] = [5] = [8]", [2, 5, 8], ROSSO), (10.0, "C₀ = [3] = [6] = [9]", [3, 6, 9], VERDE)]
    for x, lab, els, col in gruppi:
        ax.add_patch(Ellipse((x, 2.6), 3.2, 3.6, fill=False, ec=col, lw=2)); ax.text(x, 4.95, lab, ha="center", fontsize=9.2, color=col)
        for k, e in enumerate(els):
            ax.plot(x, 3.6 - k * 1.0, "o", color=col, ms=5); ax.text(x + 0.3, 3.6 - k * 1.0, str(e), va="center", fontsize=12)
    ax.text(6.0, 0.25, "Esempio: x R y se x e y hanno lo stesso resto nella divisione per 3.  Le classi sono disgiunte e ricoprono S = {1, …, 9}.", ha="center", fontsize=8.8, color=GRIGIO)
    return _salva(fig, "mate/ch09_classi_equivalenza")


def esistenza_unicita():
    A, B = ["a", "b", "c"], [1, 2]
    def pan(titolo, mappa):
        def f(ax):
            ov = [dict(nome="A", elems=A, cx=2.0, w=2.2, h=4.6), dict(nome="B", elems=B, cx=8.0, w=2.2, h=3.2)]
            fr = [dict(da=(0, a), a=(1, b), col=(ROSSO if (a, b) in extra else BLU)) for a, b in mappa for extra in [{("b", 2), ("b", 1)}]]
            ovali_ax(ax, ov, fr, titolo=titolo, fs=11)
        return f
    d = [pan("è una funzione", [("a", 1), ("b", 2), ("c", 2)]), pan("manca l'esistenza\n(c non ha frecce)", [("a", 1), ("b", 2)]), pan("manca l'unicità\n(b ha due frecce)", [("a", 1), ("b", 1), ("b", 2), ("c", 2)])]
    return pannelli("mate/ch09_esistenza_unicita", d, larghezza=3.3, altezza=3.0)


# ---------------------------------------------------------------- capitoli 10-14
def scacchiera_ax(ax, A, B, coppie, titolo=None, rosse=()):
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            on = (a, b) in coppie
            ax.add_patch(Rectangle((i, j), 1, 1, fc=(ROSSO if (a, b) in rosse else BLU) if on else "white", ec="#555", lw=1, alpha=0.85 if on else 1))
    ax.set_xlim(0, len(A)); ax.set_ylim(0, len(B)); ax.set_aspect("equal")
    ax.set_xticks([i + 0.5 for i in range(len(A))]); ax.set_xticklabels([str(a) for a in A]); ax.set_yticks([j + 0.5 for j in range(len(B))]); ax.set_yticklabels([str(b) for b in B])
    ax.tick_params(length=0); [s.set_visible(False) for s in ax.spines.values()]
    ax.set_xlabel("A", style="italic"); ax.set_ylabel("B", style="italic", rotation=0, labelpad=10)
    if titolo:
        ax.set_title(titolo, fontsize=10)


def scacchiera():
    return fm.scacchiera_grafico(["a", "b", "c", "d"], [1, 2, 3], {("a", 2), ("b", 2), ("c", 3), ("d", 1)}, "mate/ch10_scacchiera")


def non_funzione_scacchiera():
    A, B = ["a", "b", "c", "d"], [1, 2, 3]
    d = [lambda ax: scacchiera_ax(ax, A, B, {("a", 2), ("b", 2), ("b", 3), ("c", 3), ("d", 1)}, "b ha due caselle: non è una funzione", rosse={("b", 2), ("b", 3)}),
         lambda ax: scacchiera_ax(ax, A, B, {("a", 2), ("b", 2), ("c", 3)}, "d non ha nessuna casella: non è una funzione")]
    return pannelli("mate/ch10_non_funzione", d, larghezza=3.8, altezza=3.0, wspace=0.35)


def frecce_funzione():
    return fm.diagramma_funzione(["a", "b", "c", "d"], [1, 2, 3], {"a": 2, "b": 2, "c": 3, "d": 1}, "mate/ch10_frecce")


def f_uguale_g():
    x = np.linspace(-0.4, 2.4, 300); fig, ax = plt.subplots(figsize=(4.8, 3.4))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    ax.plot(x, 3 * x ** 2 - 1, color=BLU, lw=2, label="f(x) = 3x² − 1"); ax.plot(x, x ** 3 + 2 * x - 1, color=ROSSO, lw=2, ls="--", label="g(x) = x³ + 2x − 1")
    for px, py in ((0, -1), (1, 2), (2, 11)):
        ax.plot(px, py, "o", color="black", ms=6, zorder=5); ax.annotate(f"({px}, {py})", (px, py), textcoords="offset points", xytext=(8, -14) if px else (10, -3), fontsize=9)
    ax.set_xlim(-0.4, 2.6); ax.set_ylim(-3, 20); ax.legend(frameon=False, loc="upper left", fontsize=9)
    ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0); ax.set_title("Su {0, 1, 2} le due funzioni coincidono; su ℝ no", fontsize=10)
    return _salva(fig, "mate/ch10_f_uguale_g")


def identita():
    ov, fr = [dict(nome="A", elems=[1, 2, 3], cx=2.3, h=4.4), dict(nome="A", elems=[1, 2, 3], cx=7.7, h=4.4)], None
    fig, ax = plt.subplots(figsize=(4.6, 3.0)); ovali_ax(ax, ov, [dict(da=(0, k), a=(1, k)) for k in (1, 2, 3)], titolo="idₐ: ogni elemento va in sé stesso")
    return _salva(fig, "mate/ch11_identita")


def costante():
    ov = [dict(nome="A", elems=[1, 2, 3, 4], cx=2.3), dict(nome="B", elems=["α", "β", "γ"], cx=7.7, h=4.2)]
    fig, ax = plt.subplots(figsize=(4.6, 3.3)); ovali_ax(ax, ov, [dict(da=(0, k), a=(1, "β")) for k in (1, 2, 3, 4)], titolo="funzione costante: tutto va in β")
    return _salva(fig, "mate/ch11_costante")


def proiezione():
    fig, ax = plt.subplots(figsize=(4.4, 3.4)); ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.9); ax.axvline(0, color="black", lw=0.9); ax.set_xlim(-0.3, 4.6); ax.set_ylim(-0.6, 3.6)
    a, b = 3.0, 2.2; ax.plot(a, b, "o", color=BLU, ms=7); ax.text(a + 0.1, b + 0.12, "(a, b)", color=BLU, fontsize=11)
    ax.plot([a, a], [b, 0], ls="--", color=GRIGIO); ax.plot([a, 0], [b, b], ls="--", color=GRIGIO)
    ax.plot(a, 0, "o", color=ROSSO, ms=6); ax.plot(0, b, "o", color=VERDE, ms=6)
    ax.text(a, -0.25, "p₁(a, b) = a", ha="center", color=ROSSO, fontsize=10); ax.text(0.1, b + 0.12, "p₂(a, b) = b", color=VERDE, fontsize=10)
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    return _salva(fig, "mate/ch11_proiezioni")


def restrizione():
    x = np.linspace(0, 6, 400); f1 = 0.6 * np.sin(x) + 0.15 * x + 2; f2 = np.where((x > 2) & (x < 4), f1, f1 + 1.1 * np.sin((x - 2) * math.pi / 2) ** 2 * ((x <= 2) | (x >= 4)))
    f2 = np.where((x >= 2) & (x <= 4), f1, f1 + 0.9 * np.minimum(abs(x - 2), abs(x - 4)) ** 1.0 * ((x < 2) | (x > 4)))
    fig, ax = plt.subplots(figsize=(4.8, 3.2)); ax.axhline(0, color="black", lw=0.8)
    ax.axvspan(2, 4, color=VERDE, alpha=0.18); ax.plot(x, f1, color=BLU, lw=2, label="f"); ax.plot(x, f2, color=ROSSO, lw=2, ls="--", label="g")
    ax.plot([2, 4], [0, 0], color=VERDE, lw=5, solid_capstyle="butt"); ax.text(2, -0.45, "a", ha="center"); ax.text(4, -0.45, "b", ha="center")
    ax.set_xlim(0, 6); ax.set_ylim(-0.7, 5.2); ax.legend(frameon=False, loc="upper left"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("f ≠ g su ℝ, ma f|[a,b] = g|[a,b]", fontsize=10)
    return _salva(fig, "mate/ch11_restrizione")


def quoziente_non_ben_definita():
    fig, ax = plt.subplots(figsize=(5.8, 3.4)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 7)
    # classi di partenza: 1 cifra {3, 8, ...}; classi di arrivo: 1 cifra {6}, 2 cifre {16}
    ax.add_patch(Ellipse((2.4, 3.5), 3.4, 4.6, fill=False, ec=BLU, lw=2)); ax.text(2.4, 6.1, "classe di 1 cifra\n[3] = [8]", ha="center", fontsize=9.5, color=BLU)
    ax.plot(2.4, 4.4, "o", color="black"); ax.text(2.7, 4.4, "3", fontsize=12, va="center"); ax.plot(2.4, 2.6, "o", color="black"); ax.text(2.7, 2.6, "8", fontsize=12, va="center")
    ax.add_patch(Ellipse((9.0, 5.1), 3.4, 2.2, fill=False, ec=GRIGIO, lw=1.8)); ax.text(9.0, 6.4, "[6]: 1 cifra", ha="center", fontsize=9.5, color=GRIGIO); ax.plot(9.0, 5.1, "o", color="black"); ax.text(9.3, 5.1, "6", fontsize=12, va="center")
    ax.add_patch(Ellipse((9.0, 1.8), 3.4, 2.2, fill=False, ec=ROSSO, lw=1.8)); ax.text(9.0, 3.1, "[16]: 2 cifre", ha="center", fontsize=9.5, color=ROSSO); ax.plot(9.0, 1.8, "o", color="black"); ax.text(9.3, 1.8, "16", fontsize=12, va="center")
    ax.add_patch(FancyArrowPatch((2.6, 4.4), (8.8, 5.1), arrowstyle="-|>", mutation_scale=13, color=BLU, lw=1.6)); ax.add_patch(FancyArrowPatch((2.6, 2.6), (8.8, 1.8), arrowstyle="-|>", mutation_scale=13, color=ROSSO, lw=1.6))
    ax.text(5.7, 5.2, "x ↦ 2x:  3 ↦ 6", ha="center", fontsize=9.5, color=BLU); ax.text(5.7, 1.6, "8 ↦ 16", ha="center", fontsize=9.5, color=ROSSO)
    ax.text(6.0, 0.25, "Stessa classe di partenza, due classi di arrivo diverse: F([x]) = [2x] non è ben definita", ha="center", fontsize=9)
    return _salva(fig, "mate/ch12_quoziente_non_ben_definita")


def immagine_controimmagine():
    A, B = ["a₁", "a₂", "a₃", "a₄", "a₅"], ["b₁", "b₂", "b₃", "b₄"]
    f = {"a₁": "b₁", "a₂": "b₁", "a₃": "b₂", "a₄": "b₃", "a₅": "b₃"}
    def img(ax):
        S = {"a₁", "a₂", "a₃"}
        ov = [dict(nome="A", elems=A, cx=2.1, evid=S, sub="S", col=BLU), dict(nome="B", elems=B, cx=7.9, evid={f[a] for a in S}, sub="f(S)", col=BLU)]
        ovali_ax(ax, ov, [dict(da=(0, a), a=(1, f[a]), col=BLU if a in S else GRIGIO) for a in A], titolo="immagine di S: f(S) = {b₁, b₂}", fs=11)
    def ctr(ax):
        T = {"b₂", "b₃"}; pre = {a for a in A if f[a] in T}
        ov = [dict(nome="A", elems=A, cx=2.1, evid=pre, sub="f⁻¹(T)", col=ROSSO), dict(nome="B", elems=B, cx=7.9, evid=T, sub="T", col=ROSSO)]
        ovali_ax(ax, ov, [dict(da=(0, a), a=(1, f[a]), col=ROSSO if f[a] in T else GRIGIO) for a in A], titolo="controimmagine di T = {b₂, b₃}", fs=11)
    return pannelli("mate/ch13_immagine_controimmagine", [img, ctr], larghezza=4.4, altezza=3.6, wspace=0.55)


def parabola():
    return fm.controimmagine_x2(0, 2, "mate/ch13_parabola")


def tre_funzioni():
    def mk(titolo, A, B, m):
        def f(ax):
            ov = [dict(nome="A", elems=A, cx=2.0, w=2.2, h=4.8), dict(nome="B", elems=B, cx=8.0, w=2.2, h=4.8)]
            ovali_ax(ax, ov, [dict(da=(0, a), a=(1, b)) for a, b in m.items()], titolo=titolo, fs=11)
        return f
    d = [mk("iniettiva, non suriettiva\n(d non è raggiunto)", [1, 2, 3], ["a", "b", "c", "d"], {1: "a", 2: "b", 3: "c"}),
         mk("suriettiva, non iniettiva\n(1 e 2 vanno in a)", [1, 2, 3, 4], ["a", "b", "c"], {1: "a", 2: "a", 3: "b", 4: "c"}),
         mk("biettiva", [1, 2, 3], ["a", "b", "c"], {1: "b", 2: "c", 3: "a"})]
    return pannelli("mate/ch14_tre_funzioni", d, larghezza=3.4, altezza=3.2)


def x2_ini_sur():
    x = np.linspace(-3, 3, 400); fig, ax = plt.subplots(figsize=(4.6, 3.4))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8); ax.plot(x, x ** 2, color=BLU, lw=2)
    ax.axhline(-4, color=ROSSO, ls="--", lw=1.3); ax.text(-2.9, -4.4, "y = −4: nessuna intersezione\n(non suriettiva)", color=ROSSO, fontsize=9, va="top", bbox=dict(fc="white", ec="none", pad=1.5))
    ax.axhline(1, color=VERDE, ls="--", lw=1.3); ax.plot([-1, 1], [1, 1], "o", color=VERDE, ms=6); ax.text(0, 3.0, "y = 1: due intersezioni\n(non iniettiva)", color=VERDE, fontsize=9, ha="center", bbox=dict(fc="white", ec="none", pad=1.5))
    ax.set_xlim(-3, 3); ax.set_ylim(-6.5, 9.5); ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0); ax.set_title("f : ℝ → ℝ, f(x) = x²", fontsize=10)
    return _salva(fig, "mate/ch14_x2_iniettiva_suriettiva")


# ---------------------------------------------------------------- capitoli 15-19
def composizione():
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    ov = [dict(nome="A", elems=[1, 2, 3], cx=1.6, w=2.0, h=4.4), dict(nome="B", elems=["a", "b", "c"], cx=5.0, w=2.0, h=4.4), dict(nome="C", elems=["x", "y"], cx=8.4, w=2.0, h=3.2)]
    fr = [dict(da=(0, 1), a=(1, "a")), dict(da=(0, 2), a=(1, "b")), dict(da=(0, 3), a=(1, "c")), dict(da=(1, "a"), a=(2, "x"), col=ROSSO), dict(da=(1, "b"), a=(2, "x"), col=ROSSO), dict(da=(1, "c"), a=(2, "y"), col=ROSSO)]
    ovali_ax(ax, ov, fr, xlim=(0, 10), fs=11)
    ax.text(3.3, 6.05, "f", color=BLU, fontsize=13, style="italic", ha="center"); ax.text(6.7, 6.05, "g", color=ROSSO, fontsize=13, style="italic", ha="center")
    ax.text(5, -0.25, "g ∘ f:  1 ↦ x,   2 ↦ x,   3 ↦ y   (prima f, poi g)", ha="center", fontsize=10)
    ax.set_ylim(-0.6, 6.8)
    return _salva(fig, "mate/ch15_composizione")


def inversa():
    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    ov = [dict(nome="A", elems=[1, 2, 3], cx=2.2, h=4.2), dict(nome="B", elems=["a", "b", "c"], cx=7.8, h=4.2)]
    fr = [dict(da=(0, 1), a=(1, "b")), dict(da=(0, 2), a=(1, "c")), dict(da=(0, 3), a=(1, "a"))] + [dict(da=(1, b), a=(0, a), col=ROSSO, tratt=True, rad=0.25) for a, b in ((1, "b"), (2, "c"), (3, "a"))]
    ovali_ax(ax, ov, fr, fs=11)
    ax.text(5, 6.05, "f (blu) e f⁻¹ (rosso tratteggiato)", ha="center", fontsize=10); ax.set_ylim(0, 6.4)
    return _salva(fig, "mate/ch15_inversa")


def proiezione_non_iniettiva():
    fig, ax = plt.subplots(figsize=(4.4, 3.2)); ax.set_aspect("equal"); ax.axhline(0, color="black", lw=0.9); ax.axvline(0, color="black", lw=0.9)
    ax.set_xlim(-0.3, 4.6); ax.set_ylim(-0.6, 3.6); a = 3.0
    for b, c in ((1.0, BLU), (2.5, ROSSO)):
        ax.plot(a, b, "o", color=c, ms=7)
    ax.text(a + 0.12, 1.0, "(a, b)", color=BLU, fontsize=11); ax.text(a + 0.12, 2.5, "(a, b′)", color=ROSSO, fontsize=11)
    ax.plot([a, a], [0, 3.3], ls="--", color=GRIGIO); ax.plot(a, 0, "o", color="black", ms=6); ax.text(a, -0.45, "p₁(a, b) = p₁(a, b′) = a", ha="center", fontsize=9.5)
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_title("coppie diverse con la stessa prima componente", fontsize=10)
    return _salva(fig, "mate/ch16_proiezione_non_iniettiva")


def retta_affine():
    x = np.linspace(-1.5, 3.5, 100); fig, ax = plt.subplots(figsize=(4.4, 3.4))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8); ax.plot(x, 2 * x - 1, color=BLU, lw=2, label="y = 2x − 1")
    ax.axhline(3, color=VERDE, ls="--", lw=1.2); ax.plot(2, 3, "o", color=VERDE, ms=7); ax.annotate("una sola intersezione:\nx = (3 + 1)/2 = 2", (2, 3), textcoords="offset points", xytext=(-120, 28), fontsize=9, color=VERDE)
    ax.set_xlim(-1.5, 3.5); ax.set_ylim(-4.5, 6.5); ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0); ax.legend(frameon=False, loc="lower right")
    ax.set_title("ogni retta orizzontale taglia il grafico una volta: f è biettiva", fontsize=9.5)
    return _salva(fig, "mate/ch16_retta_affine")


def due_x_piu_uno():
    fig, ax = plt.subplots(figsize=(5.0, 3.4))
    A = [-2, -1, 0, 1, 2]; B = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
    ov = [dict(nome="ℤ", elems=A, cx=2.1, h=4.6), dict(nome="ℤ", elems=B, cx=7.9, h=5.6, evid={-2, 0, 2, 4}, sub="pari: non raggiunti", col=ROSSO)]
    ovali_ax(ax, ov, [dict(da=(0, a), a=(1, 2 * a + 1)) for a in A], titolo="f(n) = 2n + 1: arrivano solo i numeri dispari", fs=10, ylim=(0, 6.8))
    return _salva(fig, "mate/ch16_2n_piu_1")


def x2_restrizione():
    x = np.linspace(-3, 3, 400)
    def a(ax):
        ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8); ax.plot(x, x ** 2, color=BLU, lw=2); ax.set_ylim(-1, 9); ax.set_xlim(-3, 3)
        ax.set_title("ℝ → [0, +∞): suriettiva,\nnon iniettiva", fontsize=9.5); ax.axhline(4, color=ROSSO, ls="--", lw=1); ax.plot([-2, 2], [4, 4], "o", color=ROSSO, ms=5)
    def b(ax):
        xp = np.linspace(0, 3, 200); ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8); ax.plot(x, x ** 2, color=GRIGIO, lw=1, ls=":"); ax.plot(xp, xp ** 2, color=BLU, lw=2.4)
        ax.set_ylim(-1, 9); ax.set_xlim(-3, 3); ax.set_title("[0, +∞) → [0, +∞): biettiva", fontsize=9.5); ax.axhline(4, color=VERDE, ls="--", lw=1); ax.plot([2], [4], "o", color=VERDE, ms=5)
    return pannelli("mate/ch17_x2_restrizione", [a, b], larghezza=3.7, altezza=3.1, wspace=0.3)


def seno():
    x = np.linspace(-2 * math.pi, 2 * math.pi, 600); fig, ax = plt.subplots(figsize=(5.2, 3.0))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8); ax.plot(x, np.sin(x), color=GRIGIO, lw=1.2)
    xr = np.linspace(-math.pi / 2, math.pi / 2, 200); ax.plot(xr, np.sin(xr), color=BLU, lw=3); ax.axvspan(-math.pi / 2, math.pi / 2, color=BLU, alpha=0.08)
    for yy in (-1, 1):
        ax.axhline(yy, color=VERDE, ls="--", lw=1)
    ax.set_xticks([-math.pi, -math.pi / 2, 0, math.pi / 2, math.pi]); ax.set_xticklabels(["−π", "−π/2", "0", "π/2", "π"]); ax.set_ylim(-1.5, 1.5)
    ax.set_title("sen : [−π/2, π/2] → [−1, 1] è biettiva", fontsize=10)
    return _salva(fig, "mate/ch17_seno")


def non_commutativa():
    x = np.linspace(-2, 2, 300); fig, ax = plt.subplots(figsize=(4.6, 3.3))
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8); ax.plot(x, x ** 2 + 1, color=BLU, lw=2, label="(g ∘ f)(x) = x² + 1"); ax.plot(x, (x + 1) ** 2, color=ROSSO, lw=2, ls="--", label="(f ∘ g)(x) = (x + 1)²")
    ax.plot([1, 1], [2, 4], "o", color="black", ms=5); ax.annotate("in x = 1: 2 contro 4", (1, 3), textcoords="offset points", xytext=(10, -4), fontsize=9)
    ax.set_xlim(-2, 2); ax.set_ylim(-0.5, 9); ax.legend(frameon=False, loc="upper center", fontsize=9); ax.set_xlabel("x")
    return _salva(fig, "mate/ch18_non_commutativa")


def controesempio_composizione():
    fig, ax = plt.subplots(figsize=(6.0, 2.8))
    ov = [dict(nome="A = {0}", elems=[0], cx=1.6, w=2.0, h=2.6), dict(nome="B", elems=[0, 1], cx=5.0, w=2.0, h=3.2), dict(nome="C = {0}", elems=[0], cx=8.4, w=2.0, h=2.6)]
    fr = [dict(da=(0, 0), a=(1, 0)), dict(da=(1, 0), a=(2, 0), col=ROSSO), dict(da=(1, 1), a=(2, 0), col=ROSSO)]
    ovali_ax(ax, ov, fr, fs=11, ylim=(0.5, 5.4))
    ax.text(5, 0.7, "g ∘ f è biettiva, ma g non è iniettiva e f non è suriettiva", ha="center", fontsize=9.5)
    return _salva(fig, "mate/ch19_controesempio")


def tutte():
    plan = [
        (20, insieme_venn, "Un insieme come diagramma di Venn: 1, 2, 3 ∈ A e 5 ∉ A.", 6.5),
        (32, sottoinsieme, "S ⊆ T: la regione di S sta dentro quella di T.", 8.0),
        (49, scatole_cinesi, "Le scatole cinesi: A è un elemento di B, ma gli elementi di A non lo sono di B.", 8.5),
        (60, unione_intersezione, "Intersezione e unione di due insiemi X e Y (regioni in azzurro).", 11.0),
        (88, prodotto_griglia, "Il prodotto cartesiano A × B come griglia di coppie ordinate.", 8.0),
        (95, differenza, "La differenza non è commutativa: A ∖ B ≠ B ∖ A.", 11.0),
        (97, complementare, "Il complementare di S rispetto all'universo A.", 7.5),
        (111, demorgan, "Leggi di De Morgan: in ogni riga le due regioni azzurre coincidono.", 11.0),
        (141, insieme_parti, "L'insieme delle parti di {a, b, c}: 8 sottoinsiemi ordinati per inclusione.", 10.0),
        (167, domino, "L'effetto domino: la base fa cadere la prima tessera, il passo induttivo le fa cadere tutte.", 12.0),
        (204, ricoprimento, "Un ricoprimento di ℕ: A₁ e A₂ si sovrappongono tra 100 e 1000.", 11.0),
        (222, partizione_pari_dispari, "Una partizione di ℕ: pari e dispari non si sovrappongono e coprono tutto.", 8.5),
        (227, non_partizione, "Un ricoprimento che non è una partizione: 3 sta in entrambi i blocchi.", 8.0),
        (253, quoziente, "Dalla partizione all'insieme quoziente: ogni blocco diventa un elemento di Q.", 11.0),
        (266, relazione_divisibilita, "La divisibilità su {1, 2, 3, 6} come grafo orientato: una freccia da m a n se m divide n.", 9.0),
        (315, classi_equivalenza, "Esempio di classi di equivalenza: disgiunte e con unione uguale all'insieme.", 11.5),
        (345, esistenza_unicita, "Esistenza e unicità: la prima è una funzione, le altre due no.", 12.0),
        (351, scacchiera, "Il grafico Γ come caselle segnate nella scacchiera A × B: una casella per ogni elemento di A.", 8.0),
        (354, non_funzione_scacchiera, "Due modi in cui Γ non definisce una funzione (caselle in rosso: l'unicità fallisce).", 12.0),
        (361, frecce_funzione, "La stessa funzione con il diagramma a frecce.", 8.5),
        (368, f_uguale_g, "f e g hanno lo stesso grafico su {0, 1, 2} ma sono diverse su ℝ.", 9.5),
        (375, identita, "La funzione identità: ogni elemento resta dov'è.", 8.5),
        (377, costante, "Una funzione costante: tutti gli elementi vanno nello stesso punto.", 8.5),
        (382, proiezione, "Le proiezioni dal piano sugli assi.", 8.0),
        (394, restrizione, "Funzioni con grafici diversi ma uguali ristrette a [a, b].", 9.5),
        (407, quoziente_non_ben_definita, "La regola F([x]) = [2x] manda la stessa classe in due classi diverse.", 11.5),
        (416, immagine_controimmagine, "A sinistra l'immagine di un sottoinsieme S, a destra la controimmagine di T.", 12.0),
        (432, parabola, "La controimmagine di T = [0, 4] tramite x² è [−2, 2].", 9.0),
        (447, tre_funzioni, "Le tre situazioni: iniettiva, suriettiva, biettiva.", 12.0),
        (451, x2_ini_sur, "Con f(x) = x² su ℝ: nessuna intersezione per y = −4, due per y = 1.", 9.0),
        (462, composizione, "La composizione: si applica prima f e poi g.", 11.5),
        (471, inversa, "Una funzione biettiva e la sua inversa: le frecce si invertono.", 9.0),
        (481, proiezione_non_iniettiva, "La proiezione non è iniettiva: (a, b) e (a, b′) hanno la stessa immagine.", 8.0),
        (487, retta_affine, "La retta y = 2x − 1: ogni retta orizzontale la taglia una volta.", 8.5),
        (490, due_x_piu_uno, "f(n) = 2n + 1 su ℤ: i numeri pari non vengono mai raggiunti.", 9.5),
        (500, x2_restrizione, "Cambiando codominio e dominio si passa da suriettiva a biettiva.", 11.5),
        (505, seno, "La funzione seno ristretta a [−π/2, π/2] con codominio [−1, 1].", 10.0),
        (534, non_commutativa, "Le due composizioni sono funzioni diverse.", 9.0),
        (570, controesempio_composizione, "Il controesempio: g ∘ f biettiva senza che f sia suriettiva né g iniettiva.", 11.0),
    ]
    for idx, fn, did, larg in plan:
        path = fn()
        reg(idx, path[len("figure/"):-len(".png")], did, larg)
    (OUT / "mate").mkdir(parents=True, exist_ok=True)
    (OUT / "mate" / "piano.json").write_text(json.dumps(PIANO, ensure_ascii=False, indent=1), encoding="utf-8")
    return PIANO


if __name__ == "__main__":
    p = tutte()
    print(len(p), "figure in", OUT / "mate")


def quoziente_generale():
    """S diviso in blocchi A1..A4 (partizione) e l'insieme quoziente Q = {A1, ..., A4} (ogni blocco diventa un elemento)."""
    fig, ax = plt.subplots(figsize=(6.0, 3.4)); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(0, 12.4); ax.set_ylim(0, 7)
    cols = [BLU, ROSSO, VERDE, ARANCIO]
    ax.add_patch(Ellipse((3.0, 3.5), 5.6, 5.6, fill=False, ec="black", lw=2))
    ys = [5.6, 4.2, 2.8, 1.4]
    for yb in (2.1, 3.5, 4.9):
        dx = math.sqrt(max(2.8 ** 2 - (yb - 3.5) ** 2, 0)); ax.plot([3.0 - dx, 3.0 + dx], [yb, yb], color="black", lw=1.3)
    for k, y in enumerate(ys):
        ax.text(2.4, y, f"A$_{k + 1}$", ha="center", va="center", fontsize=14, color=cols[k], style="italic")
    ax.text(3.0, 6.75, "S", ha="center", fontsize=13, style="italic")
    ax.add_patch(Ellipse((9.9, 3.5), 3.2, 5.6, fill=False, ec="black", lw=2)); ax.text(9.9, 6.75, "Q", ha="center", fontsize=13, style="italic")
    for k, y in enumerate(ys):
        ax.plot(9.4, y, "o", color=cols[k], ms=7); ax.text(9.75, y, f"A$_{k + 1}$", va="center", fontsize=13, color=cols[k], style="italic")
        ax.add_patch(FancyArrowPatch((3.5, y), (9.2, y), arrowstyle="-|>", mutation_scale=11, color=cols[k], lw=1.3, zorder=1))
    ax.text(6.2, 0.15, "ogni blocco della partizione diventa un elemento di Q", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "mate/ch07_quoziente_generale")


def partizione_relazione():
    """Corrispondenza tra partizioni e relazioni di equivalenza: S = {1..5}, blocchi {1,2} {3} {4,5}; x R y se stesso blocco."""
    blocchi = [[1, 2], [3], [4, 5]]; cols = [BLU, ROSSO, VERDE]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.3), gridspec_kw=dict(width_ratios=[1, 1.05], wspace=0.45))
    a1.set_aspect("equal"); a1.axis("off"); a1.set_xlim(0, 8); a1.set_ylim(0, 6.2)
    a1.add_patch(Rectangle((0.2, 0.3), 7.6, 5.0, fill=False, ec="black", lw=1.6)); a1.text(0.45, 5.0, "S", fontsize=12, style="italic", va="center")
    pos = [(1.6, 3.0, 2.4, 2.2), (4.2, 1.5, 1.2, 1.4), (6.3, 3.0, 2.4, 2.2)]
    # blocchi come ovali
    cen = [(2.0, 3.1), (4.2, 1.5), (6.0, 3.4)]; dim = [(3.0, 2.0), (1.5, 1.8), (3.0, 2.0)]
    pt = {1: (1.3, 3.1), 2: (2.8, 3.1), 3: (4.2, 1.5), 4: (5.2, 3.4), 5: (6.7, 3.4)}
    for (cx, cy), (w, h), c, b in zip(cen, dim, cols, blocchi):
        a1.add_patch(Ellipse((cx, cy), w, h, fill=False, ec=c, lw=2))
    for k, (x, y) in pt.items():
        a1.plot(x, y, "o", color="black", ms=5); a1.text(x, y + 0.35, str(k), ha="center", fontsize=11)
    a1.set_title("partizione di S", fontsize=10.5)
    # matrice della relazione
    n = 5; a2.set_aspect("equal"); a2.set_xlim(0, n); a2.set_ylim(0, n)
    blk = {x: i for i, b in enumerate(blocchi) for x in b}
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            same = blk[x] == blk[y]
            a2.add_patch(Rectangle((x - 1, n - y), 1, 1, fc=cols[blk[x]] if same else "white", ec="#888", lw=0.8, alpha=0.75 if same else 1))
    a2.set_xticks([i + 0.5 for i in range(n)]); a2.set_xticklabels(range(1, n + 1)); a2.set_yticks([i + 0.5 for i in range(n)]); a2.set_yticklabels(range(n, 0, -1))
    a2.xaxis.tick_top(); a2.tick_params(length=0)
    for s in a2.spines.values():
        s.set_visible(False)
    a2.set_title("relazione di equivalenza R\n(casella colorata = x R y)", fontsize=10.5, pad=24)
    fig.text(0.485, 0.5, "⇄", ha="center", va="center", fontsize=26)
    fig.text(0.485, 0.2, "stesso blocco\n⟺ x R y", ha="center", va="center", fontsize=8.5, color=GRIGIO)
    return _salva(fig, "mate/ch09_partizione_relazione")


def inclusione_canonica():
    """j : S -> A, j(s) = s, con S = {1, 2} contenuto in A = {1, 2, 3, 4}."""
    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ov = [dict(nome="S", elems=[1, 2], cx=2.2, w=2.2, h=1.9), dict(nome="A", elems=[3, 1, 2, 4], cx=7.8, w=2.4, h=4.8)]
    ovali_ax(ax, ov, [dict(da=(0, 1), a=(1, 1)), dict(da=(0, 2), a=(1, 2))], titolo="inclusione canonica j : S → A,  j(s) = s", fs=12)
    return _salva(fig, "mate/ch10_inclusione_canonica")


def restrizione_frecce():
    """f : A -> B e la restrizione f|S (S sottoinsieme di A): stesse frecce, ma solo quelle che partono da S."""
    A, B = [1, 2, 3, 4], ["a", "b", "c"]; f = {1: "a", 2: "b", 3: "b", 4: "c"}; S = {1, 2}
    fig, ax = plt.subplots(figsize=(5.4, 3.5))
    ov = [dict(nome="A", elems=A, cx=2.2, w=2.4, h=4.6, evid=S, sub="S", col=BLU), dict(nome="B", elems=B, cx=7.8, w=2.4, h=4.2)]
    fr = [dict(da=(0, a), a=(1, f[a]), col=BLU if a in S else "#c3cad1", tratt=a not in S) for a in A]
    ovali_ax(ax, ov, fr, titolo="f (tutte le frecce) e f|S (solo le frecce blu)", fs=12)
    return _salva(fig, "mate/ch10_restrizione_frecce")
