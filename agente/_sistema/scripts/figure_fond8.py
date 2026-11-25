"""Figure dei capitoli 50-52 di Fondamenti (relazioni, L24 del 23 nov 2026): grafi diretti (digrafi) di relazioni
su un insieme, con cappi; il grafo a dieci punti dell'esercizio sui quantificatori.
PNG in _sistema/figure/fond/.  Uso: python figure_fond8.py
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, pannelli

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Polygon, Arc


def digrafo_ax(ax, pos, archi, titolo=None, colori=None, fs=13, lim=None, rad_doppi=0.18, dir_cappi=None, r_cappio=0.22, etich=None):
    """pos: dict nodo -> (x, y); archi: lista di coppie (a, b), (a, a) = cappio.
    colori: dict arco -> colore. Gli archi presenti in entrambi i versi vengono incurvati per non sovrapporsi."""
    colori = colori or {}
    dir_cappi = dir_cappi or {}
    ax.set_aspect("equal"); ax.axis("off")
    xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
    if lim:
        ax.set_xlim(lim[0], lim[1]); ax.set_ylim(lim[2], lim[3])
    else:
        ax.set_xlim(min(xs) - 1.0, max(xs) + 1.0); ax.set_ylim(min(ys) - 1.0, max(ys) + 1.0)
    cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
    s = set(archi)
    for a, b in archi:
        col = colori.get((a, b), BLU)
        if a == b:   # cappio: cerchio tangente al nodo, rivolto verso l'esterno, con la punta della freccia
            x, y = pos[a]
            ang = dir_cappi.get(a, math.atan2(y - cy, x - cx) if (x, y) != (cx, cy) else math.pi / 2)
            r = r_cappio
            ox, oy = x + r * math.cos(ang), y + r * math.sin(ang)
            base = math.degrees(ang) + 180   # direzione dal centro del cerchio verso il nodo
            ax.add_patch(Arc((ox, oy), 2 * r, 2 * r, theta1=base + 28, theta2=base + 332, color=col, lw=1.4))
            t_end = math.radians(base + 332)
            pe = (ox + r * math.cos(t_end), oy + r * math.sin(t_end))
            t_pre = math.radians(base + 300)
            pp = (ox + r * math.cos(t_pre), oy + r * math.sin(t_pre))
            ax.add_patch(FancyArrowPatch(pp, pe, arrowstyle="-|>", mutation_scale=11, color=col, lw=0.01,
                                         connectionstyle="arc3,rad=-0.25", shrinkA=0, shrinkB=0))
            continue
        rad = rad_doppi if (b, a) in s else 0.0
        ax.add_patch(FancyArrowPatch(pos[a], pos[b], arrowstyle="-|>", mutation_scale=13, color=col, lw=1.5,
                                     connectionstyle=f"arc3,rad={rad}", shrinkA=9, shrinkB=9))
    for n, (x, y) in pos.items():
        ax.plot(x, y, "o", color="black", ms=5, zorder=5)
        dx, dy = (etich or {}).get(n, (-0.32, 0.25))
        ax.text(x + dx, y + dy, str(n), fontsize=fs, ha="center", va="center", zorder=6)
    if titolo:
        ax.set_title(titolo, fontsize=fs - 2, pad=4)


def relazione_abcd():
    """R = {(a,a),(b,c),(c,b),(d,d)} su {a,b,c,d}: simmetrica, non riflessiva, non antisimmetrica, non transitiva."""
    pos = {"a": (0, 2), "b": (2.6, 2), "c": (0, 0), "d": (2.6, 0)}
    archi = [("a", "a"), ("b", "c"), ("c", "b"), ("d", "d")]
    d = lambda ax: digrafo_ax(ax, pos, archi, rad_doppi=0.22, lim=(-1.0, 3.6, -0.9, 2.9),
                              dir_cappi={"a": math.radians(135), "d": math.radians(-45)},
                              etich={"a": (0.35, -0.3), "b": (0.35, 0.25), "c": (-0.35, -0.25), "d": (-0.35, 0.3)})
    return pannelli("fond/relazione_abcd", [d], ncols=1, larghezza=3.4, altezza=2.8)


def ordine_e_equivalenza():
    """(a) ≤ su {1,2,3,4}; (b) equivalenza su {1,...,6} con classi {1,3,5}, {2,6}, {4}; (c) uguaglianza su {a,b,c}."""
    pos1 = {1: (0, 2), 2: (2.4, 2), 3: (0, 0), 4: (2.4, 0)}
    archi1 = [(i, i) for i in range(1, 5)] + [(i, j) for i in range(1, 5) for j in range(1, 5) if i < j]
    dc1 = {1: math.radians(135), 2: math.radians(45), 3: math.radians(-135), 4: math.radians(-45)}
    a = lambda ax: digrafo_ax(ax, pos1, archi1, titolo="(a) x ≤ y su {1, 2, 3, 4}:\nordine totale", dir_cappi=dc1,
                              lim=(-1.0, 3.4, -1.0, 3.0), etich={1: (-0.5, -0.4), 2: (0.5, -0.4), 3: (-0.5, 0.4), 4: (0.5, 0.4)})
    pos2 = {1: (0, 2), 3: (2.2, 2), 5: (1.1, 0.2), 2: (3.6, 2), 6: (3.6, 0.2), 4: (4.9, 1.1)}
    cl = [1, 3, 5]
    archi2 = [(i, i) for i in range(1, 7)] + [(i, j) for i in cl for j in cl if i != j] + [(2, 6), (6, 2)]
    dc2 = {1: math.radians(135), 3: math.radians(90), 5: math.radians(-90), 2: math.radians(90), 6: math.radians(-90),
           4: math.radians(90)}
    b = lambda ax: digrafo_ax(ax, pos2, archi2, titolo="(b) equivalenza con classi\n{1, 3, 5}, {2, 6}, {4}", dir_cappi=dc2,
                              lim=(-0.9, 5.6, -0.8, 3.0),
                              etich={1: (-0.3, -0.4), 3: (0.45, -0.15), 5: (-0.45, 0.05), 2: (-0.4, 0.0), 6: (-0.4, 0.0), 4: (0.4, -0.1)})
    pos3 = {"a": (0, 1), "b": (1.5, 1), "c": (3.0, 1)}
    c = lambda ax: digrafo_ax(ax, pos3, [("a", "a"), ("b", "b"), ("c", "c")], titolo="(c) uguaglianza su {a, b, c}:\nordine ed equivalenza",
                              dir_cappi={k: math.radians(90) for k in pos3}, lim=(-0.8, 3.8, 0.0, 2.2),
                              etich={k: (-0.3, -0.05) for k in pos3})
    return pannelli("fond/ordine_equivalenza", [a, b, c], ncols=3, larghezza=3.6, altezza=3.3, wspace=0.05)


def grafo_dieci_punti():
    """Il grafo del quiz sui quantificatori: dominio {1,...,10}, A = {6,7,8}, B = {3,4,5}."""
    pos = {1: (1.3, 6.3), 2: (5.0, 6.0), 3: (0.6, 4.2), 4: (2.9, 4.4), 5: (5.4, 3.7),
           6: (0.7, 2.0), 7: (3.8, 2.0), 8: (6.6, 2.0), 9: (3.0, 0.2), 10: (5.6, 0.2)}
    archi = [(3, 1), (4, 2), (5, 2), (6, 3), (6, 4), (7, 4), (7, 2), (8, 5), (9, 6), (9, 7), (9, 10), (10, 8)]

    def d(ax):
        ax.add_patch(Polygon([(-0.1, 3.6), (6.1, 3.2), (6.1, 4.9), (-0.1, 5.1)], closed=True, fc="#d6e4f5", ec=BLU, lw=1.2, zorder=0))
        ax.add_patch(Rectangle((-0.1, 1.45), 7.3, 1.15, fc="#d6e4f5", ec=BLU, lw=1.2, zorder=0))
        ax.text(1.8, 4.55, "B", color=BLU, fontsize=16, fontweight="bold")
        ax.text(2.2, 1.85, "A", color=BLU, fontsize=16, fontweight="bold")
        digrafo_ax(ax, pos, archi, lim=(-0.6, 7.6, -0.6, 6.9),
                   etich={1: (-0.35, 0.1), 2: (0.0, 0.35), 3: (-0.35, 0.0), 4: (-0.25, 0.3), 5: (0.35, 0.0), 6: (-0.35, 0.0),
                          7: (0.35, 0.0), 8: (0.35, 0.0), 9: (0.0, -0.4), 10: (0.0, -0.4)})
    return pannelli("fond/grafo_dieci_punti", [d], ncols=1, larghezza=5.2, altezza=4.4)


if __name__ == "__main__":
    for f in (relazione_abcd, ordine_e_equivalenza, grafo_dieci_punti):
        print(f())
