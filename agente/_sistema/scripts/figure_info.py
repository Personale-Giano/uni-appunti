"""Figure dei Word di Fondamenti Informatica e Programmazione. Genera i PNG in _sistema/figure/fond/ e figure/prog/
e scrive i piani (piano.json) nelle stesse cartelle.
Uso: python figure_info.py
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, OUT, np, plt, Circle, Ellipse, Arc, Rectangle, FancyArrowPatch, _salva
from matplotlib.patches import Polygon, PathPatch, Wedge
from matplotlib.path import Path as MPath

CH = "#eaf1fb"   # riempimento azzurro chiaro


def vuoto(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h)); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl)
    return fig, ax


def box(ax, x, y, w, h, testo="", fc=CH, ec="#444", lw=1.3, fs=11, col="black", style="round,pad=0.02,rounding_size=0.08", bold=False):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fc, ec=ec, lw=lw, zorder=2))
    if testo:
        ax.text(x + w / 2, y + h / 2, testo, ha="center", va="center", fontsize=fs, color=col, zorder=3, fontweight="bold" if bold else "normal")


def freccia(ax, p, q, col="#333", lw=1.5, rad=0.0, st="-|>", ms=12, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=st, mutation_scale=ms, color=col, lw=lw, connectionstyle=f"arc3,rad={rad}", zorder=4, linestyle=ls))


def num(ax, x, y, n, col=ROSSO):
    ax.add_patch(Circle((x, y), 0.16, fc=col, ec="none", zorder=6)); ax.text(x, y, str(n), color="white", ha="center", va="center", fontsize=8.5, zorder=7, fontweight="bold")


# ====================================================================== FONDAMENTI
def hex_blocchi():
    fig, ax = vuoto(5.4, 2.7, (-0.4, 8.4), (-2.6, 1.9))
    bits = "10110101"
    for i, b in enumerate(bits):
        box(ax, i, 0, 0.9, 0.9, b, fc="#fbeed3" if i < 4 else "#e6f3e8", fs=14)
    for k, (x0, c, h, bl) in enumerate(((0, "#d99a1c", "B", "1011 = 11"), (4, "#1e8449", "5", "0101 = 5"))):
        ax.plot([x0 + 0.05, x0 + 0.05, x0 + 3.85, x0 + 3.85], [-0.08, -0.25, -0.25, -0.08], color=c, lw=1.6)
        freccia(ax, (x0 + 1.95, -0.3), (x0 + 1.95, -1.05), c)
        box(ax, x0 + 1.4, -1.8, 1.1, 0.7, h, fc="white", ec=c, fs=16, bold=True)
        ax.text(x0 + 1.95, -2.2, bl, ha="center", fontsize=9.5, color=c)
    ax.text(4, 1.35, "8 bit = 2 blocchi da 4 bit = 2 cifre esadecimali:  10110101₂ = B5₁₆", ha="center", fontsize=10)
    return _salva(fig, "fond/ch02_blocchi_esadecimale")


def hdd():
    fig, ax = vuoto(4.6, 4.2, (-3.0, 3.4), (-2.6, 2.6))
    for r in np.linspace(0.55, 2.2, 7):
        ax.add_patch(Circle((0, 0), r, fill=False, ec="#9aa5b1", lw=0.9))
    ax.add_patch(Circle((0, 0), 0.3, fc="white", ec="#555", lw=1.2, zorder=3))
    for a in range(0, 360, 45):
        ax.plot([0.55 * math.cos(math.radians(a)), 2.2 * math.cos(math.radians(a))], [0.55 * math.sin(math.radians(a)), 2.2 * math.sin(math.radians(a))], color="#cdd3da", lw=0.7)
    ax.add_patch(Wedge((0, 0), 1.7, 45, 90, width=0.275, fc="#f5b7a8", ec=ROSSO, lw=1.2, zorder=3))
    ax.add_patch(Wedge((0, 0), 1.1, 135, 225, width=0.275, fc="none", ec=BLU, lw=2.4, zorder=3))
    ax.text(-2.8, 0.55, "traccia", color=BLU, fontsize=11, ha="left")
    freccia(ax, (-2.0, 0.5), (-1.12, 0.1), BLU, 1.2)
    ax.text(1.2, 2.45, "settore", color=ROSSO, fontsize=11)
    freccia(ax, (1.25, 2.4), (0.95, 1.6), ROSSO, 1.2)
    ax.plot([2.9, 1.35], [-1.9, -0.5], color="#333", lw=5, solid_capstyle="round", zorder=5)
    ax.plot(1.35, -0.5, "o", color="#333", ms=7, zorder=6)
    ax.text(2.0, -2.3, "braccio con testina", fontsize=10.5, ha="center")
    ax.set_title("Piatto di un disco rigido", fontsize=11)
    return _salva(fig, "fond/ch03_hdd_tracce_settori")


def cd_spirale():
    fig, ax = vuoto(4.2, 4.0, (-2.6, 2.6), (-2.6, 2.7))
    t = np.linspace(0, 7 * 2 * math.pi, 1500); r = 0.5 + 0.28 * t / (2 * math.pi)
    ax.plot(r * np.cos(t), r * np.sin(t), color=BLU, lw=1.3)
    ax.add_patch(Circle((0, 0), 2.45, fill=False, ec="#444", lw=1.5)); ax.add_patch(Circle((0, 0), 0.4, fc="white", ec="#444", lw=1.3, zorder=3))
    freccia(ax, (0.55, 0.1), (2.3, 0.1), ROSSO, 1.6, ms=11)
    ax.text(1.4, 0.3, "lettura", color=ROSSO, ha="center", fontsize=10)
    ax.set_title("CD/DVD: un'unica traccia a spirale", fontsize=11)
    return _salva(fig, "fond/ch03_cd_spirale")


def rgb():
    fig, ax = vuoto(5.6, 3.0, (-0.2, 10.4), (-2.3, 3.3))
    ax.add_patch(Rectangle((0, 0.5), 2.1, 2.1, fc="#ff8000", ec="#444", lw=1.3))
    ax.text(1.05, 3.0, "colore", ha="center", fontsize=10.5)
    ax.text(3.0, 1.55, "=", fontsize=22, va="center")
    for k, (n, c, v, bg) in enumerate((("Rosso", ROSSO, "FF", "#f6d5d0"), ("Verde", VERDE, "80", "#d4ecda"), ("Blu", BLU, "00", "#d6e2f5"))):
        x = 3.8 + k * 1.95
        box(ax, x, 0.5, 1.75, 2.1, "", fc=bg, ec=c)
        ax.text(x + 0.875, 2.2, n, ha="center", fontsize=11, color=c); ax.text(x + 0.875, 1.5, v, ha="center", fontsize=20, color=c, fontweight="bold"); ax.text(x + 0.875, 0.8, "8 bit", ha="center", fontsize=9.5, color=c)
    ax.text(4.8, -0.35, "24 bit = 3 byte = 6 cifre esadecimali: #FF8000", ha="center", fontsize=11)
    ax.text(4.8, -0.95, "(2 cifre per il rosso, 2 per il verde, 2 per il blu)", ha="center", fontsize=9.5, color=GRIGIO)
    return _salva(fig, "fond/ch04_rgb_esadecimale")


def celle_memoria():
    fig, ax = vuoto(6.2, 3.6, (-1.9, 8.9), (-4.0, 2.2))
    cont = ["01001101", "11000011", "00000101", "01101010", "10101010", "00110011", "11110000", "00001111"]
    for i, c in enumerate(cont):
        box(ax, i * 1.05, 0, 1.0, 0.9, "", fc="#fbeed3" if i == 3 else CH)
        ax.text(i * 1.05 + 0.5, 0.45, "1 byte", ha="center", va="center", fontsize=8)
        ax.text(i * 1.05 + 0.5, -0.3, str(i), ha="center", fontsize=11, color=BLU)
    ax.text(-0.2, -0.3, "indirizzi", ha="right", fontsize=9, color=BLU)
    ax.text(4.2, 1.35, "memoria principale: celle consecutive, ciascuna con il proprio indirizzo", ha="center", fontsize=10)
    freccia(ax, (3.65, -0.7), (5.3, -2.0), GRIGIO, 1.0, ls="--"); freccia(ax, (3.65, -0.7), (1.3, -2.0), GRIGIO, 1.0, ls="--")
    for i, b in enumerate("01101010"):
        box(ax, 1.3 + i * 0.5, -2.7, 0.5, 0.7, b, fc="white", fs=11, style="square,pad=0")
    ax.text(1.55, -3.05, "MSB", ha="center", fontsize=9.5, color=ROSSO, fontweight="bold"); ax.text(5.05, -3.05, "LSB", ha="center", fontsize=9.5, color=VERDE, fontweight="bold")
    ax.text(3.0, -3.55, "il contenuto della cella 3, bit per bit", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "fond/ch05_celle_memoria")


def _gate(ax, x, y, tipo):
    """Disegna la porta con ingresso a sinistra a (x, y) di altezza 1, larghezza 1.2."""
    def P(vs, cs):
        return PathPatch(MPath(vs, cs), fc="#eaf1fb", ec="#333", lw=1.6, zorder=3)
    M, L, C3, Z = MPath.MOVETO, MPath.LINETO, MPath.CURVE3, MPath.CLOSEPOLY
    if tipo == "AND":
        th = np.linspace(-math.pi / 2, math.pi / 2, 30)
        pts = [(x, y), (x + 0.6, y)] + [(x + 0.6 + 0.5 * math.cos(a), y + 0.5 + 0.5 * math.sin(a)) for a in th] + [(x + 0.6, y + 1), (x, y + 1), (x, y)]
        ax.add_patch(Polygon(pts, closed=True, fc="#eaf1fb", ec="#333", lw=1.6, zorder=3)); ex = x + 1.1
    elif tipo in ("OR", "XOR"):
        vs = [(x, y), (x + 0.6, y), (x + 1.1, y + 0.5), (x + 0.6, y + 1), (x, y + 1), (x + 0.3, y + 0.5), (x, y)]
        cs = [M, C3, C3, C3, C3, C3, C3]
        # lato superiore e inferiore curvi
        vs = [(x, y), (x + 0.7, y), (x + 1.1, y + 0.5), (x + 1.1, y + 0.5), (x + 0.7, y + 1), (x, y + 1), (x, y + 1), (x + 0.3, y + 0.5), (x, y)]
        cs = [M, C3, C3, M, C3, C3, M, C3, C3]
        ax.add_patch(PathPatch(MPath(vs, cs), fc="#eaf1fb", ec="#333", lw=1.6, zorder=3)); ex = x + 1.1
        if tipo == "XOR":
            ax.add_patch(PathPatch(MPath([(x - 0.15, y), (x + 0.15, y + 0.5), (x - 0.15, y + 1)], [M, C3, C3]), fc="none", ec="#333", lw=1.6, zorder=3))
    else:  # NOT
        ax.add_patch(Polygon([(x, y), (x, y + 1), (x + 0.9, y + 0.5)], closed=True, fc="#eaf1fb", ec="#333", lw=1.6, zorder=3))
        ax.add_patch(Circle((x + 0.98, y + 0.5), 0.08, fc="white", ec="#333", lw=1.4, zorder=3)); ex = x + 1.06
    ins = [(y + 0.5,)] if tipo == "NOT" else [(y + 0.25,), (y + 0.75,)]
    for (iy,) in ins:
        ax.plot([x - 0.45, x + 0.02], [iy, iy], color="#333", lw=1.4)
    ax.plot([ex, ex + 0.45], [y + 0.5, y + 0.5], color="#333", lw=1.4)


def porte():
    fig, ax = vuoto(7.4, 3.9, (-0.6, 15.6), (-4.4, 2.7))
    tabelle = {"AND": [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)], "OR": [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)], "XOR": [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)], "NOT": [(0, 1), (1, 0)]}
    for k, (nome, tab) in enumerate(tabelle.items()):
        x = 0.4 + k * 3.9
        _gate(ax, x, 0.6, nome)
        ax.text(x + 0.8, 2.1, nome, ha="center", fontsize=12, fontweight="bold", color=BLU)
        if nome == "NOT":
            hdr = ("a", "out")
        else:
            hdr = ("a", "b", "out")
        ty = -0.4
        ax.text(x + 0.8, ty, "  ".join(hdr), ha="center", fontsize=9.5, family="monospace", fontweight="bold")
        for j, riga in enumerate(tab):
            ax.text(x + 0.8, ty - 0.55 * (j + 1), "  ".join(str(v) for v in riga), ha="center", fontsize=10, family="monospace", color=ROSSO if riga[-1] else "black")
    return _salva(fig, "fond/ch05_porte_logiche")


def bitmap():
    pat = ["00111100", "01000010", "10100101", "10000001", "10100101", "10011001", "01000010", "00111100"]
    fig, ax = vuoto(5.4, 3.4, (-0.3, 14.6), (-0.4, 8.5))
    for r, riga in enumerate(pat):
        for c, b in enumerate(riga):
            ax.add_patch(Rectangle((c, 7 - r), 1, 1, fc="black" if b == "1" else "white", ec="#888", lw=0.7))
        ax.text(8.5, 7.5 - r, riga, family="monospace", fontsize=10, va="center")
    ax.text(10.9, 4.0, "1 pixel =\n1 bit", fontsize=9.5, ha="center", va="center", color=BLU)
    ax.text(4, 8.55, "immagine in bianco e nero: 1 pixel = 1 bit", fontsize=10, ha="center")
    ax.text(10.9, 8.55, "", fontsize=1)
    return _salva(fig, "fond/ch06_bitmap_bn")


def campionamento():
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    t = np.linspace(0, 2 * math.pi * 2, 600); ax.plot(t, np.sin(t) + 0.3 * np.sin(2.7 * t), color=GRIGIO, lw=1.6, label="onda sonora")
    ts = np.linspace(0.25, 4 * math.pi - 0.25, 17); ys = np.sin(ts) + 0.3 * np.sin(2.7 * ts)
    ax.vlines(ts, 0, ys, color=BLU, lw=1.2); ax.plot(ts, ys, "o", color=BLU, ms=5, label="campioni (misure a intervalli regolari)")
    ax.axhline(0, color="black", lw=0.8); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel("tempo"); ax.set_ylabel("ampiezza")
    ax.annotate("", xy=(ts[3], -1.55), xytext=(ts[2], -1.55), arrowprops=dict(arrowstyle="<->", color=ROSSO, lw=1.2)); ax.text((ts[2] + ts[3]) / 2, -1.9, "intervallo costante", color=ROSSO, ha="center", fontsize=9)
    ax.set_ylim(-2.1, 3.0); ax.legend(frameon=False, fontsize=8.5, loc="upper right", ncol=1)
    ax.spines["bottom"].set_visible(False)
    return _salva(fig, "fond/ch06_campionamento")


def pesi_binari():
    fig, ax = vuoto(5.6, 3.0, (-0.6, 7.9), (-2.2, 3.0))
    bits = "100101"; pesi = [32, 16, 8, 4, 2, 1]; esp = [5, 4, 3, 2, 1, 0]
    for i, (b, p, e) in enumerate(zip(bits, pesi, esp)):
        x = i * 1.2
        ax.text(x + 0.5, 2.2, f"2$^{e}$", ha="center", fontsize=11, color=GRIGIO)
        ax.text(x + 0.5, 1.65, str(p), ha="center", fontsize=11, color=BLU)
        box(ax, x, 0.4, 1.0, 1.0, b, fc="#fbeed3" if b == "1" else "white", fs=16, bold=True)
        ax.text(x + 0.5, -0.15, str(p) if b == "1" else "0", ha="center", fontsize=11, color=ROSSO if b == "1" else GRIGIO)
    ax.text(3.6, -0.85, "32 + 4 + 1 = 37", ha="center", fontsize=13, color=ROSSO, fontweight="bold")
    ax.text(3.6, -1.6, "100101₂ = 37₁₀  (ogni bit vale quanto il suo peso, se è 1)", ha="center", fontsize=9.5, color=GRIGIO)
    return _salva(fig, "fond/ch07_pesi_binari")


def divisioni():
    fig, ax = vuoto(4.8, 3.4, (-0.3, 8.0), (-1.6, 4.3))
    righe = [("13 : 2 = 6", "1", "LSB"), (" 6 : 2 = 3", "0", ""), (" 3 : 2 = 1", "1", ""), (" 1 : 2 = 0", "1", "MSB")]
    for i, (t, r, nota) in enumerate(righe):
        y = 3.2 - i * 0.95
        ax.text(0, y, t, family="monospace", fontsize=12, va="center")
        ax.text(3.6, y, "resto", fontsize=9.5, va="center", color=GRIGIO)
        box(ax, 4.5, y - 0.33, 0.7, 0.66, r, fc="#f6d5d0", ec=ROSSO, fs=13, bold=True)
        if nota:
            ax.text(5.4, y, nota, fontsize=9.5, va="center", color=ROSSO)
    freccia(ax, (6.5, 0.4), (6.5, 3.2), BLU, 1.8)
    ax.text(6.7, 1.8, "si leggono\ndal basso\nverso l'alto", fontsize=9.5, color=BLU, va="center")
    ax.text(2.6, -0.85, "13₁₀ = 1101₂", fontsize=13, ha="center", fontweight="bold")
    return _salva(fig, "fond/ch07_divisioni_successive")


def somma_binaria():
    fig, ax = vuoto(4.8, 3.2, (-1.4, 6.6), (-3.2, 3.4))
    a = [None, 1, 1, 0, 1, 0]; b = [None, 1, 1, 0, 1, 1]; rip = [1, 1, 0, 1, 0, 0]; ris = [1, 1, 0, 1, 0, 1]
    ax.text(-0.9, 2.5, "riporti", fontsize=9.5, color=ROSSO, va="center")
    for i in range(6):
        x = i
        if rip[i]:
            ax.text(x + 0.5, 2.5, "1", color=ROSSO, ha="center", va="center", fontsize=13, fontweight="bold")
        if a[i] is not None:
            ax.text(x + 0.5, 1.5, str(a[i]), ha="center", va="center", fontsize=15, family="monospace"); ax.text(x + 0.5, 0.6, str(b[i]), ha="center", va="center", fontsize=15, family="monospace")
        ax.text(x + 0.5, -1.0, str(ris[i]), ha="center", va="center", fontsize=15, family="monospace", fontweight="bold", color=BLU)
    ax.text(-0.9, 1.5, "26", fontsize=11, color=GRIGIO, va="center"); ax.text(-0.9, 0.6, "+ 27", fontsize=11, color=GRIGIO, va="center"); ax.text(-0.9, -1.0, "= 53", fontsize=11, color=BLU, va="center")
    ax.plot([-0.2, 6.2], [0.0, 0.0], color="black", lw=1.4)
    ax.text(3, -2.2, "11010 + 11011 = 110101", ha="center", fontsize=11)
    ax.text(3, -2.8, "si procede da destra; 1 + 1 dà 0 con riporto di 1", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "fond/ch07_somma_binaria")


def complemento_due():
    fig, ax = vuoto(5.0, 5.0, (-2.3, 2.3), (-2.3, 2.3))
    ax.add_patch(Circle((0, 0), 1.25, fill=False, ec="#999", lw=1.2))
    for k in range(16):
        ang = math.radians(90 - k * 22.5 - 0)     # in senso orario dal vertice (0000)
        val = k if k < 8 else k - 16
        x, y = 1.25 * math.cos(ang), 1.25 * math.sin(ang)
        col = BLU if val >= 0 else ROSSO
        ax.plot(x, y, "o", color=col, ms=6, zorder=5)
        ax.text(1.62 * math.cos(ang), 1.62 * math.sin(ang), f"{k:04b}", ha="center", va="center", fontsize=8.5, family="monospace", color=col)
        ax.text(2.0 * math.cos(ang), 2.0 * math.sin(ang), f"{val}", ha="center", va="center", fontsize=10, color=col, fontweight="bold")
    ax.text(0, 0.15, "4 bit", ha="center", fontsize=11); ax.text(0, -0.2, "bit di segno 1\n= negativo", ha="center", fontsize=8.5, color=ROSSO)
    cut = math.radians(90 - 7.5 * 22.5 - 0)
    ax.plot([0.95 * math.cos(cut), 1.5 * math.cos(cut)], [0.95 * math.sin(cut), 1.5 * math.sin(cut)], color="#333", lw=1.2, ls="--")
    return _salva(fig, "fond/ch08_complemento_a_due")


def hamming():
    fig, ax = vuoto(6.0, 2.7, (-0.8, 12.2), (-2.4, 2.4))
    xs = [0, 3.7, 7.4, 11.1]
    ax.plot([xs[0], xs[3]], [0, 0], color="#bbb", lw=2, zorder=1)
    nomi = ["parola legale A", "1 bit errato", "2 bit errati", "parola legale B"]
    cols = [BLU, ARANCIO, ARANCIO, BLU]
    for x, n, c in zip(xs, nomi, cols):
        ax.plot(x, 0, "o", color=c, ms=13 if c == BLU else 9, zorder=3); ax.text(x, 0.65, n, ha="center", fontsize=9.5, color=c)
    for i in range(3):
        ax.text((xs[i] + xs[i + 1]) / 2, -0.38, "1 bit", ha="center", fontsize=8.5, color=GRIGIO)
    ax.annotate("", xy=(0, -1.2), xytext=(xs[3], -1.2), arrowprops=dict(arrowstyle="<->", color=ROSSO, lw=1.4)); ax.text(5.55, -1.55, "distanza di Hamming 3", ha="center", fontsize=10, color=ROSSO)
    ax.text(xs[1], 1.5, "più vicina ad A:\nsi corregge in A", ha="center", fontsize=9, color=VERDE)
    ax.text(xs[2], 1.5, "non è legale:\nerrore rilevato", ha="center", fontsize=9, color=VERDE)
    return _salva(fig, "fond/ch11_distanza_hamming")


# ====================================================================== PROGRAMMAZIONE
def fl_box(ax, x, y, w, h, t, kind="proc", fs=10):
    cx, cy = x, y
    if kind == "proc":
        box(ax, cx - w / 2, cy - h / 2, w, h, t, fc=CH, fs=fs, style="square,pad=0")
    elif kind == "term":
        box(ax, cx - w / 2, cy - h / 2, w, h, t, fc="#e6f3e8", fs=fs, style="round,pad=0,rounding_size=0.35")
    else:
        ax.add_patch(Polygon([(cx - w / 2, cy), (cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2)], closed=True, fc="#fbeed3", ec="#444", lw=1.3, zorder=2))
        ax.text(cx, cy, t, ha="center", va="center", fontsize=fs, zorder=3)


def flow_moltiplicazione():
    fig, ax = vuoto(4.6, 5.4, (-2.6, 3.4), (-6.4, 1.0))
    fl_box(ax, 0, 0.4, 1.6, 0.6, "inizio", "term")
    fl_box(ax, 0, -1.0, 2.2, 0.7, "s ← 0 ;  i ← 0")
    fl_box(ax, 0, -2.7, 2.2, 1.2, "i < n ?", "dec")
    fl_box(ax, 0, -4.4, 2.2, 0.7, "s ← s + m")
    fl_box(ax, 0, -5.4, 2.2, 0.7, "i ← i + 1")
    fl_box(ax, 2.6, -2.7, 1.6, 0.6, "fine: s = m·n", "term", fs=8.5)
    freccia(ax, (0, 0.1), (0, -0.65)); freccia(ax, (0, -1.35), (0, -2.1)); freccia(ax, (0, -3.3), (0, -4.05)); freccia(ax, (0, -4.75), (0, -5.05))
    ax.plot([-1.1, -2.0, -2.0], [-5.4, -5.4, -2.7], color="#333", lw=1.5); freccia(ax, (-2.0, -2.7), (-1.15, -2.7))
    freccia(ax, (1.1, -2.7), (1.8, -2.7))
    ax.text(0.12, -3.7, "sì", color=VERDE, fontsize=10); ax.text(1.2, -2.45, "no", color=ROSSO, fontsize=10)
    return _salva(fig, "prog/ch02_flow_moltiplicazione")


def tre_strutture():
    fig, axs = plt.subplots(1, 3, figsize=(8.4, 3.4)); [a.set_aspect("equal") or a.axis("off") for a in axs]
    ax = axs[0]; ax.set_xlim(-1.6, 1.6); ax.set_ylim(-4.3, 1.0); ax.set_title("sequenza", fontsize=11)
    for k, y in enumerate((0, -1.6, -3.2)):
        fl_box(ax, 0, y, 1.8, 0.8, f"istruzione {k + 1}")
        if k < 2:
            freccia(ax, (0, y - 0.4), (0, y - 1.2))
    ax = axs[1]; ax.set_xlim(-2.4, 2.4); ax.set_ylim(-4.3, 1.0); ax.set_title("selezione", fontsize=11)
    fl_box(ax, 0, 0, 2.2, 1.2, "condizione?", "dec", 9)
    fl_box(ax, -1.3, -2.0, 1.7, 0.8, "blocco A"); fl_box(ax, 1.3, -2.0, 1.7, 0.8, "blocco B")
    freccia(ax, (-0.7, -0.3), (-1.3, -1.6)); freccia(ax, (0.7, -0.3), (1.3, -1.6)); ax.text(-1.4, -0.7, "sì", color=VERDE, fontsize=10); ax.text(1.0, -0.7, "no", color=ROSSO, fontsize=10)
    ax.plot([-1.3, -1.3, 0], [-2.4, -3.2, -3.2], color="#333", lw=1.4); ax.plot([1.3, 1.3, 0], [-2.4, -3.2, -3.2], color="#333", lw=1.4); freccia(ax, (0, -3.2), (0, -4.0))
    ax = axs[2]; ax.set_xlim(-2.4, 2.4); ax.set_ylim(-4.3, 1.0); ax.set_title("iterazione", fontsize=11)
    fl_box(ax, 0, 0, 2.2, 1.2, "condizione?", "dec", 9); fl_box(ax, 0, -2.0, 1.8, 0.8, "blocco")
    freccia(ax, (0, -0.6), (0, -1.6)); ax.text(0.15, -0.95, "sì", color=VERDE, fontsize=10)
    ax.plot([0.9, 1.8, 1.8], [-2.0, -2.0, 0], color="#333", lw=1.4); freccia(ax, (1.8, 0), (1.1, 0))
    ax.plot([-1.1, -1.8, -1.8], [0, 0, -4.0], color="#333", lw=1.4); freccia(ax, (-1.8, -4.0), (-0.6, -4.0)); ax.text(-1.75, -0.4, "no", color=ROSSO, fontsize=10)
    ax.text(0, -4.0, "uscita", fontsize=9, color=GRIGIO, va="center")
    fig.subplots_adjust(wspace=0.05)
    return _salva(fig, "prog/ch03_tre_strutture")


def memoria_aree():
    fig, ax = vuoto(4.4, 3.6, (-1.8, 5.2), (-4.6, 1.2))
    box(ax, 0, -1.4, 3.4, 1.4, "Area del programma\n(istruzioni binarie)", fc="#fbeed3", fs=10.5, style="square,pad=0")
    box(ax, 0, -4.2, 3.4, 2.8, "Area dei dati\n(variabili, a partire da\nquello che resta)", fc="#e6f3e8", fs=10.5, style="square,pad=0")
    ax.text(-0.15, -0.05, "indirizzo 0", ha="right", fontsize=9.5, va="top", color=BLU); ax.text(-0.15, -4.2, "indirizzi alti", ha="right", fontsize=9.5, va="bottom", color=BLU)
    freccia(ax, (-1.3, -0.5), (-1.3, -3.7), BLU, 1.2); ax.text(-1.5, -2.1, "indirizzi\ncrescenti", fontsize=8.5, color=BLU, ha="right", va="center")
    ax.set_title("La RAM vista dalla CPU", fontsize=11)
    return _salva(fig, "prog/ch04_memoria_aree")


def compilazione():
    fig, ax = vuoto(6.4, 2.0, (-0.2, 13.3), (-1.4, 1.8))
    for x, t, fc in ((0, "codice sorgente\n(testo in C)", CH), (4.7, "compilatore", "#fbeed3"), (8.0, "codice macchina\n(eseguibile)", "#e6f3e8")):
        w = 3.3 if "compil" not in t else 2.7
        box(ax, x, -0.6, w if x == 0 else (2.7 if x == 4.7 else 3.3), 1.2, t, fc=fc, fs=10)
    freccia(ax, (3.3, 0), (4.65, 0)); freccia(ax, (7.45, 0), (7.95, 0)); freccia(ax, (11.35, 0), (12.0, 0))
    ax.text(12.15, 0, "CPU", fontsize=11, va="center", fontweight="bold")
    ax.text(5.75, -1.1, "tradotto per intero, prima dell'esecuzione", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "prog/ch05_compilazione")


def variabile():
    fig, ax = vuoto(6.4, 2.8, (-0.4, 13.2), (-2.2, 2.9))
    for x, nome, tipo, ind, val in ((0.2, "contatore", "int, 4 byte", "0x904A", "1"), (6.8, "media", "float, 4 byte", "0x367F", "60.54")):
        ax.text(x + 2.6, 2.1, nome, ha="center", fontsize=12, color=BLU, fontweight="bold")
        box(ax, x, 0.5, 5.2, 1.2, val, fc="#fbeed3", fs=16, bold=True, style="square,pad=0")
        ax.text(x + 2.6, -0.1, f"indirizzo {ind}", ha="center", fontsize=10, color=ROSSO)
        ax.text(x + 2.6, -0.75, f"tipo {tipo}", ha="center", fontsize=10, color=VERDE)
    ax.text(6.4, -1.8, "nome · tipo · indirizzo · valore", ha="center", fontsize=10, color=GRIGIO)
    return _salva(fig, "prog/ch06_variabile_quaterna")


def stack_fp_sp():
    fig, ax = vuoto(5.2, 3.8, (-3.6, 5.8), (-5.4, 1.4))
    for i, (n, a) in enumerate((("x", "0x03FC"), ("y", "0x03F8"), ("z", "0x03F4"))):
        y = -i * 1.3
        box(ax, 0, y - 1.3, 2.6, 1.3, f"{n}  (int, 4 B)", fc="#e6f3e8", fs=11, style="square,pad=0")
        ax.text(2.75, y - 0.65, a, fontsize=9.5, color=BLU, va="center")
    ax.text(-0.85, 0.05, "FP", ha="right", color=ROSSO, fontsize=12, fontweight="bold", va="center"); freccia(ax, (-0.75, 0.05), (-0.02, 0.05), ROSSO, 1.8)
    ax.text(-0.85, -3.9, "SP", ha="right", color=ROSSO, fontsize=12, fontweight="bold", va="center"); freccia(ax, (-0.75, -3.9), (-0.02, -3.9), ROSSO, 1.8)
    ax.text(-0.85, 0.65, "base della\nzona delle variabili", fontsize=8.5, color=GRIGIO, ha="right"); ax.text(-0.85, -4.45, "cima corrente", fontsize=8.5, color=GRIGIO, ha="right")
    freccia(ax, (4.7, -0.2), (4.7, -3.7), BLU, 1.2); ax.text(4.9, -1.9, "cresce\nverso\ni bassi", fontsize=8.5, color=BLU, va="center")
    ax.set_title("Lo stack dopo int x; int y; int z;", fontsize=10.5)
    return _salva(fig, "prog/ch07_stack_fp_sp")


def esecuzione(nome, titolo, mem, r0, r1, tmpl_alu, passi, dest=-1):
    """mem: [(etichetta, valore, nota)]; l'ultima cella e' la destinazione (evidenziata). passi: 4 righe di legenda."""
    fig, ax = vuoto(6.4, 4.4, (-0.4, 11.8), (-5.2, 3.6))
    ax.text(1.7, 3.1, "RAM", ha="center", fontsize=11, color=BLU, fontweight="bold")
    ys = []
    for i, (n, v, nota) in enumerate(mem):
        y = 2.0 - i * 1.5; ys.append(y)
        is_d = i == (dest % len(mem))
        box(ax, 0, y - 0.55, 3.4, 1.1, f"{n} = {v}", fc="#d4ecda" if is_d else CH, ec=VERDE if is_d else "#444", fs=10.5, style="square,pad=0")
        if nota:
            ax.text(0.05, y + 0.62, nota, fontsize=8, color=GRIGIO, va="bottom")
    ax.text(7.0, 3.1, "CPU", ha="center", fontsize=11, color=BLU, fontweight="bold")
    box(ax, 5.6, 1.2, 2.4, 0.9, f"R0 = {r0}", fc="#fbeed3", fs=11, style="square,pad=0"); box(ax, 5.6, -0.3, 2.4, 0.9, f"R1 = {r1}", fc="#fbeed3", fs=11, style="square,pad=0")
    box(ax, 9.4, 0.4, 2.2, 1.0, "ALU", fc="#e6f3e8", fs=11, bold=True, style="square,pad=0")
    freccia(ax, (3.45, ys[0]), (5.55, 1.65), ROSSO); num(ax, 4.1, 1.95, 1)
    freccia(ax, (3.45, ys[1]), (5.55, 0.15), ROSSO); num(ax, 4.1, 0.2, 2)
    freccia(ax, (8.05, 1.65), (9.35, 1.05), ROSSO); freccia(ax, (8.05, 0.15), (9.35, 0.75), ROSSO); num(ax, 8.7, 1.65, 3)
    ax.text(10.5, -0.2, tmpl_alu, ha="center", va="top", fontsize=9, color=ROSSO)
    num(ax, 0.0, ys[dest] + 0.55, 4, VERDE)
    for k, t in enumerate(passi):
        ax.text(0.0, -2.3 - k * 0.6, f"{k + 1}  {t}", fontsize=9.5, family="monospace", va="center")
    ax.set_title(titolo, fontsize=10.5)
    return _salva(fig, nome)


def esec_z():
    return esecuzione("prog/ch08_esecuzione_z", "Esecuzione di z = x + y", [("x", 5, ""), ("y", 2, ""), ("z", "7", "(prima: ?)")], 5, 2, "5 + 2 = 7\n(risultato in R0)",
                      ["LOAD  R0, @x", "LOAD  R1, @y", "ADD   R0, R1", "STORE R0, @z"])


def esec_asm():
    return esecuzione("prog/ch05_esecuzione_somma", "Somma a basso livello: A + B", [("A", "12 → 4", "cella 400"), ("B", -8, "cella 404")][::-1][::-1], 12, -8, "12 + (−8) = 4\n(risultato in R0)",
                      ["LOAD  R0, @A", "LOAD  R1, @B", "ADD   R0, R1", "STORE R0, @A"], dest=0)


def indirizzi_xyz():
    fig, ax = vuoto(5.2, 2.6, (-1.0, 9.6), (-2.2, 2.3))
    for i, (n, a, v) in enumerate((("z", "0x03F4", 7), ("y", "0x03F8", 2), ("x", "0x03FC", 5))):
        x = i * 3.0
        box(ax, x, 0, 2.6, 1.4, f"{v}", fc=CH, fs=16, bold=True, style="square,pad=0")
        ax.text(x + 1.3, 1.75, n, ha="center", fontsize=13, color=BLU, fontweight="bold")
        ax.text(x + 1.3, -0.45, a, ha="center", fontsize=10, color=ROSSO)
    ax.text(4.3, -1.5, "indirizzi crescenti da sinistra a destra: lo stack cresce verso gli indirizzi bassi", ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "prog/ch09_indirizzi_xyz")


def puntatore():
    fig, ax = vuoto(5.4, 2.4, (-0.6, 9.8), (-1.9, 2.4))
    box(ax, 0, 0, 3.0, 1.3, "0x03FC", fc="#fbeed3", fs=13, bold=True, style="square,pad=0"); ax.text(1.5, 1.7, "pX  (int*)", ha="center", fontsize=11, color=BLU, fontweight="bold"); ax.text(1.5, -0.45, "indirizzo 0x03F8", ha="center", fontsize=9.5, color=ROSSO)
    box(ax, 6.2, 0, 3.0, 1.3, "5", fc=CH, fs=16, bold=True, style="square,pad=0"); ax.text(7.7, 1.7, "x  (int)", ha="center", fontsize=11, color=BLU, fontweight="bold"); ax.text(7.7, -0.45, "indirizzo 0x03FC", ha="center", fontsize=9.5, color=ROSSO)
    freccia(ax, (3.05, 0.65), (6.15, 0.65), VERDE, 2.0)
    ax.text(4.6, 0.95, "punta a", ha="center", fontsize=9.5, color=VERDE)
    ax.text(4.6, -1.5, "pX = &x: il valore di pX è l'indirizzo di x", ha="center", fontsize=9.5, color=GRIGIO)
    return _salva(fig, "prog/ch11_puntatore")


def aliasing():
    fig, ax = vuoto(5.4, 3.0, (-0.6, 9.8), (-1.5, 3.8))
    box(ax, 6.2, 0.9, 3.0, 1.3, "1234", fc=CH, fs=16, bold=True, style="square,pad=0"); ax.text(7.7, 2.5, "x  (int)", ha="center", fontsize=11, color=BLU, fontweight="bold")
    box(ax, 0, 2.0, 3.0, 1.0, "&x", fc="#fbeed3", fs=12, bold=True, style="square,pad=0"); ax.text(1.5, 3.3, "pX", ha="center", fontsize=11, color=BLU, fontweight="bold")
    box(ax, 0, 0.0, 3.0, 1.0, "&x", fc="#fbeed3", fs=12, bold=True, style="square,pad=0"); ax.text(1.5, -0.4, "pXbis", ha="center", fontsize=11, color=BLU, fontweight="bold")
    freccia(ax, (3.05, 2.5), (6.15, 1.9), VERDE, 1.8); freccia(ax, (3.05, 0.5), (6.15, 1.2), VERDE, 1.8)
    ax.text(4.6, -1.0, "x, *pX e *pXbis sono la stessa cella", ha="center", fontsize=9.5, color=GRIGIO)
    return _salva(fig, "prog/ch12_aliasing")


def scanf_stati():
    fig, ax = vuoto(6.4, 3.0, (-2.3, 10.4), (-3.0, 3.0))
    cols = ["inizio", "scanf(&x)\ndigito 5", "scanf(&y)\ndigito 2", "z = x + y"]
    vals = [("?", "?", "?"), ("5", "?", "?"), ("5", "2", "?"), ("5", "2", "7")]
    nomi = [("x", "0x03FC"), ("y", "0x03F8"), ("z", "0x03F4")]
    for j, (c, v) in enumerate(zip(cols, vals)):
        x = j * 2.5
        ax.text(x + 1.1, 2.3, c, ha="center", va="center", fontsize=9.5, color=BLU)
        for i in range(3):
            nuovo = (j > 0 and v[i] != vals[j - 1][i])
            box(ax, x, 1.0 - i * 1.4 - 0.5, 2.2, 1.1, v[i], fc="#f6c6c0" if nuovo else CH, fs=15, bold=True, style="square,pad=0")
    for i, (n, a) in enumerate(nomi):
        ax.text(-0.15, 1.05 - i * 1.4, f"{n}\n{a}", ha="right", va="center", fontsize=9.5, color=BLU)
    ax.text(4.3, -3.0, "in rosso la cella appena scritta", ha="center", fontsize=9, color=ROSSO)
    return _salva(fig, "prog/ch10_scanf_memoria")


def tutte():
    fond = [
        (34, hex_blocchi, "Da binario a esadecimale: blocchi da 4 bit, ciascuno diventa una cifra.", 10.0),
        (50, hdd, "Piatto di un disco rigido: tracce concentriche divise in settori, e la testina.", 8.0),
        (62, cd_spirale, "In un CD i dati stanno su un'unica traccia a spirale.", 7.0),
        (86, rgb, "Un colore RGB a 24 bit scritto con 6 cifre esadecimali.", 10.0),
        (94, porte, "Le porte logiche AND, OR, XOR e NOT con le loro tavole di verità.", 14.0),
        (106, celle_memoria, "La memoria come sequenza di celle numerate; dentro la cella, il bit più significativo (MSB) a sinistra e il meno significativo (LSB) a destra.", 11.0),
        (125, bitmap, "Immagine in bianco e nero: ogni pixel è un bit.", 8.5),
        (136, campionamento, "Campionamento: si misura l'ampiezza dell'onda a intervalli regolari.", 10.5),
        (160, pesi_binari, "Da binario a decimale: ogni bit uguale a 1 contribuisce con il suo peso.", 10.0),
        (172, divisioni, "Da decimale a binario: i resti delle divisioni per 2, letti dal basso verso l'alto.", 8.5),
        (187, somma_binaria, "La somma binaria 11010 + 11011, con i riporti.", 8.5),
        (208, complemento_due, "Complemento a due su 4 bit: i numeri con bit di segno 1 sono negativi.", 9.5),
        (280, hamming, "Con distanza minima 3 un errore si corregge, due si rilevano.", 11.0),
    ]
    prog = [
        (27, flow_moltiplicazione, "Diagramma di flusso della moltiplicazione per somme ripetute.", 8.0),
        (40, tre_strutture, "Sequenza, selezione e iterazione.", 14.0),
        (78, memoria_aree, "La memoria centrale: area del programma e area dei dati.", 8.0),
        (112, esec_asm, "Come la CPU esegue la somma A + B: due LOAD, ADD, STORE.", 11.0),
        (135, compilazione, "Il C è compilato: il sorgente viene tradotto in codice macchina prima di essere eseguito.", 11.5),
        (181, variabile, "Ogni variabile ha nome, tipo, indirizzo e valore.", 11.0),
        (228, stack_fp_sp, "Lo stack con FP e SP dopo tre dichiarazioni.", 8.5),
        (266, esec_z, "Esecuzione di z = x + y: due LOAD, ADD, STORE.", 11.0),
        (323, indirizzi_xyz, "Gli indirizzi di x, y e z nello schema del corso.", 9.5),
        (349, scanf_stati, "Lo stato della memoria durante l'esecuzione del programma con scanf.", 11.0),
        (413, puntatore, "Il puntatore pX contiene l'indirizzo di x.", 9.5),
        (460, aliasing, "Aliasing: due puntatori alla stessa variabile.", 9.5),
    ]
    for cartella, lista in (("fond", fond), ("prog", prog)):
        (OUT / cartella).mkdir(exist_ok=True)
        piano = [dict(dopo=d, figura=fn(), didascalia=did, larghezza=l) for d, fn, did, l in lista]
        (OUT / cartella / "piano.json").write_text(json.dumps(piano, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{len(piano)} figure in {OUT / cartella}")


if __name__ == "__main__":
    tutte()


def stati_variabili(nome, titolo, nomi, colonne, larg=6.4):
    """Tabella di istantanee della memoria: una colonna per passo. nomi: nomi delle variabili (righe);
    colonne: [(intestazione, [valori...])]; in rosso le celle che cambiano rispetto alla colonna precedente."""
    n = len(nomi); nc = len(colonne)
    fig, ax = vuoto(larg, 0.9 + 0.55 * n, (-1.6, nc * 3.0 + 0.2), (-n * 1.4 - 0.2, 2.6))
    for j, (c, vals) in enumerate(colonne):
        x = j * 3.0
        ax.text(x + 1.25, 1.65, c, ha="center", va="center", fontsize=9.5, color=BLU)
        for i in range(n):
            nuovo = j > 0 and vals[i] != colonne[j - 1][1][i]
            box(ax, x, -i * 1.4 - 0.55, 2.5, 1.1, str(vals[i]), fc="#f6c6c0" if nuovo else CH, fs=15 if len(str(vals[i])) <= 3 else 9.5, bold=True, style="square,pad=0")
    for i, n_ in enumerate(nomi):
        ax.text(-0.15, -i * 1.4, n_, ha="right", va="center", fontsize=11, color=BLU, family="monospace")
    ax.set_title(titolo, fontsize=10.5)
    return _salva(fig, nome)


def swap_naive():
    return stati_variabili("prog/ch13_swap_ovvio", "x = y;  y = x;  (in rosso la cella appena scritta)", ["x", "y"],
                           [("inizio", [5, 2]), ("dopo x = y;", [2, 2]), ("dopo y = x;", [2, 2])], 5.4)


def swap_temp():
    return stati_variabili("prog/ch13_swap_temp", "temp = x;  x = y;  y = temp;  (in rosso la cella appena scritta)", ["x", "y", "temp"],
                           [("inizio", [5, 2, "?"]), ("temp = x;", [5, 2, 5]), ("x = y;", [2, 2, 5]), ("y = temp;", [2, 5, 5])], 7.0)


def tazze():
    return stati_variabili("prog/ch13_tazze", "Le tazze X e Y e la tazza ausiliaria A", ["X", "Y", "A"],
                           [("inizio", ["tè verde", "tè nero", "vuota"]), ("passo 1", ["vuota", "tè nero", "tè verde"]),
                            ("passo 2", ["tè nero", "vuota", "tè verde"]), ("passo 3", ["tè nero", "tè verde", "vuota"])], 7.0)


def float_double_memoria():
    """Tre variabili x, y, z come celle di larghezza proporzionale ai byte: float (4 B) e double (8 B)."""
    righe = [("float x = 5, y = 2, z = x / y;", [("float x", "5.0", 4), ("float y", "2.0", 4), ("float z", "2.5", 4)]),
             ("double x = 5, y = 2, z = x / y;", [("double x", "5.0", 8), ("double y", "2.0", 8), ("double z", "2.5", 8)]),
             ("float x = 5, y = 2;  double z = x / y;", [("float x", "5.0", 4), ("float y", "2.0", 4), ("double z", "2.5", 8)])]
    fig, ax = vuoto(6.6, 4.6, (0, 27), (-1.6, 14.2))
    u = 1.05   # unita' di larghezza per byte
    for r, (tit, celle) in enumerate(righe):
        y = 12.2 - r * 4.6
        ax.text(0, y + 1.3, tit, fontsize=9.5, family="monospace", va="center")
        x = 0.0
        for nome, val, byte in celle:
            w = byte * u * 1.0
            box(ax, x, y - 0.75, w, 1.5, val, fc="#fbeed3" if byte == 8 else CH, fs=12, bold=True, style="square,pad=0")
            ax.text(x + w / 2, y - 1.1, f"{nome}\n{byte} B", ha="center", va="top", fontsize=8, color=BLU)
            x += w
    return _salva(fig, "prog/ch14_float_double_memoria")


def conversioni_divisione():
    """Tre calcoli di x / y con tipi diversi: dove si perde la parte frazionaria."""
    righe = [("float z = x / y;", "int x = 5, y = 2", "5 / 2  →  2", "divisione fra interi:\nla frazione si perde qui", "float z = 2.0", ROSSO),
             ("int z = x / y;", "float x = 5, y = 2", "5.0 / 2.0  →  2.5", "divisione fra reali:\nnessuna perdita", "int z = 2", ROSSO),
             ("float z = x / (float)y;", "int x = 5, y = 2", "5 / 2.0  →  2.5", "y diventa float, quindi\nx viene promosso a float", "float z = 2.5", VERDE)]
    fig, ax = vuoto(7.2, 4.4, (0, 30), (-1, 14))
    for r, (cod, op, calc, nota, ris, col) in enumerate(righe):
        y = 11.2 - r * 4.4
        ax.text(0, y + 1.6, cod, fontsize=10, family="monospace", va="center", fontweight="bold")
        box(ax, 0, y - 0.8, 7.6, 1.6, op, fc=CH, fs=9, style="square,pad=0")
        freccia(ax, (7.7, y), (9.3, y))
        box(ax, 9.4, y - 0.8, 9.0, 1.6, calc, fc="#fbeed3", fs=10, style="square,pad=0", bold=True)
        ax.text(13.9, y - 1.15, nota.replace("\n", "\n"), ha="center", va="top", fontsize=7.5, color=GRIGIO)
        freccia(ax, (18.5, y), (20.1, y))
        box(ax, 20.2, y - 0.8, 8.8, 1.6, ris, fc="#f6c6c0" if col == ROSSO else "#d4ecda", fs=10, style="square,pad=0", bold=True)
    return _salva(fig, "prog/ch16_conversioni_divisione")


def tavole_booleane():
    """Tavole di verita' di AND, OR, NOT con gli operatori del C."""
    fig, ax = vuoto(7.2, 2.8, (0, 30), (-4.0, 5.2))
    tab = [("condizione1 && condizione2", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)], 0.0),
           ("condizione1 || condizione2", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)], 11.0),
           ("!condizione", [(0, 1), (1, 0)], 22.0)]
    for tit, righe, x0 in tab:
        ax.text(x0 + 3.6, 4.4, tit, ha="center", fontsize=8.6, family="monospace", fontweight="bold", color=BLU)
        n = len(righe[0]); w = 2.4
        for j, h in enumerate(("c1", "c2", "ris") if n == 3 else ("c", "!c")):
            ax.text(x0 + 0.2 + j * w + w / 2 - 0.1, 3.2, h, ha="center", fontsize=9, color=GRIGIO)
        for i, r in enumerate(righe):
            for j, v in enumerate(r):
                ris = j == n - 1
                box(ax, x0 + 0.2 + j * w, 2.0 - i * 1.15 - 0.45, w - 0.2, 0.95, str(v), fc=("#f6c6c0" if (ris and v) else CH), fs=11, bold=ris, style="square,pad=0")
    ax.text(15, -3.3, "1 = vero, 0 = falso", ha="center", fontsize=8.5, color=GRIGIO)
    return _salva(fig, "prog/ch17_tavole_booleane")


def intervalli():
    """I quattro tipi di intervallo sulla retta, con la loro espressione in C."""
    righe = [("chiuso", "min <= x && x <= max", True, True), ("semiaperto sinistro", "min <= x && x < max", True, False),
             ("semiaperto destro", "min < x && x <= max", False, True), ("aperto", "min < x && x < max", False, False)]
    fig, ax = vuoto(7.0, 3.6, (-8, 24), (-1.2, 14.2))
    for r, (nome, expr, a, b) in enumerate(righe):
        y = 12.0 - r * 3.6
        ax.text(-7.5, y, nome, ha="left", va="center", fontsize=9.5, color=BLU)
        ax.plot([3, 20], [y, y], color="#bbb", lw=1)
        ax.plot([6, 16], [y, y], color=BLU, lw=4, solid_capstyle="butt")
        for x, chiuso in ((6, a), (16, b)):
            ax.add_patch(Circle((x, y), 0.45, fc=BLU if chiuso else "white", ec=BLU, lw=1.8, zorder=4))
        ax.text(6, y - 0.95, "min", ha="center", va="top", fontsize=8, color=GRIGIO); ax.text(16, y - 0.95, "max", ha="center", va="top", fontsize=8, color=GRIGIO)
        ax.text(21, y, expr, ha="left", va="center", fontsize=8.6, family="monospace")
    ax.set_xlim(-8, 36)
    return _salva(fig, "prog/ch18_intervalli")


def flusso_if():
    """Diagrammi di flusso di if, if-else e if-else if-else."""
    fig, axs = plt.subplots(1, 3, figsize=(8.8, 3.6)); [a.set_aspect("equal") or a.axis("off") for a in axs]
    ax = axs[0]; ax.set_xlim(-2.4, 2.4); ax.set_ylim(-5.0, 1.0); ax.set_title("if", fontsize=11)
    fl_box(ax, 0, 0, 2.2, 1.2, "condizione?", "dec", 9); fl_box(ax, -0.2, -2.2, 1.8, 0.8, "blocco")
    freccia(ax, (0, -0.6), (0, -1.8)); ax.text(0.15, -1.1, "sì", color=VERDE, fontsize=10)
    ax.plot([1.1, 1.9, 1.9], [0, 0, -3.4], color="#333", lw=1.4); ax.text(1.3, 0.12, "no", color=ROSSO, fontsize=10)
    ax.plot([0, 0], [-2.6, -3.4], color="#333", lw=1.4); ax.plot([1.9, 0], [-3.4, -3.4], color="#333", lw=1.4); freccia(ax, (0, -3.4), (0, -4.4))
    ax = axs[1]; ax.set_xlim(-2.4, 2.4); ax.set_ylim(-5.0, 1.0); ax.set_title("if-else", fontsize=11)
    fl_box(ax, 0, 0, 2.2, 1.2, "condizione?", "dec", 9); fl_box(ax, -1.3, -2.0, 1.7, 0.8, "blocco A"); fl_box(ax, 1.3, -2.0, 1.7, 0.8, "blocco B")
    freccia(ax, (-0.7, -0.3), (-1.3, -1.6)); freccia(ax, (0.7, -0.3), (1.3, -1.6)); ax.text(-1.4, -0.7, "sì", color=VERDE, fontsize=10); ax.text(1.0, -0.7, "no", color=ROSSO, fontsize=10)
    ax.plot([-1.3, -1.3, 0], [-2.4, -3.2, -3.2], color="#333", lw=1.4); ax.plot([1.3, 1.3, 0], [-2.4, -3.2, -3.2], color="#333", lw=1.4); freccia(ax, (0, -3.2), (0, -4.2))
    ax = axs[2]; ax.set_xlim(-3.2, 3.4); ax.set_ylim(-6.6, 1.0); ax.set_title("if-else if-else", fontsize=11)
    fl_box(ax, 0, 0, 2.2, 1.2, "cond. 1?", "dec", 9); fl_box(ax, -2.0, -1.9, 1.5, 0.7, "blocco 1", fs=8.5)
    freccia(ax, (-0.7, -0.3), (-2.0, -1.5)); ax.text(-1.6, -0.5, "sì", color=VERDE, fontsize=9)
    freccia(ax, (0.7, -0.3), (1.0, -1.5)); fl_box(ax, 1.0, -2.1, 2.0, 1.2, "cond. 2?", "dec", 8.5); ax.text(0.9, -0.8, "no", color=ROSSO, fontsize=9)
    fl_box(ax, -0.1, -4.3, 1.5, 0.7, "blocco 2", fs=8.5); fl_box(ax, 2.3, -4.3, 1.8, 0.7, "default", fs=8.5)
    freccia(ax, (0.6, -2.5), (-0.1, -3.9)); freccia(ax, (1.5, -2.7), (2.3, -3.9)); ax.text(-0.1, -3.0, "sì", color=VERDE, fontsize=9); ax.text(2.2, -3.2, "no", color=ROSSO, fontsize=9)
    fig.subplots_adjust(wspace=0.05)
    return _salva(fig, "prog/ch19_flusso_if")


def scope_temp():
    return stati_variabili("prog/ch20_scambio_condizionato", "if (y < x) { int temp = x; x = y; y = temp; }  con x = 10, y = 5", ["x", "y", "temp"],
                           [("inizio", [10, 5, "—"]), ("entra", [10, 5, 10]), ("x = y;", [5, 5, 10]), ("y = temp;", [5, 10, 10]), ("esce", [5, 10, "—"])], 8.6)
