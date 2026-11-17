"""Figure dei capitoli 37-42 di Fondamenti (induzione): somma dei dispari come quadrati,
tassellazione di Golomb con triomini, esercizio 39 (la L di triomini).
PNG in _sistema/figure/fond/.  Uso: python figure_fond6.py
"""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, plt, Rectangle, _salva

PALETTE = ["#AED6F1", "#F9E79F", "#A9DFBF", "#F5B7B1", "#D2B4DE", "#FAD7A0", "#A3E4D7", "#D5DBDB",
           "#85C1E9", "#F7DC6F", "#7DCEA0", "#F1948A", "#BB8FCE", "#F8C471", "#76D7C4", "#BFC9CA"]


def dispari_quadrati():
    """1, 1+3, 1+3+5, 1+3+5+7: ogni dispari è una «squadra» che porta dal quadrato n×n al (n+1)×(n+1)."""
    cols = [BLU, ARANCIO, VERDE, ROSSO]
    fig, axs = plt.subplots(1, 4, figsize=(10, 3.0))
    for n, ax in enumerate(axs, start=1):
        ax.set_xlim(-0.3, 4.3); ax.set_ylim(-1.0, 4.3); ax.set_aspect("equal"); ax.axis("off")
        for x in range(n):
            for y in range(n):
                k = max(x, y)  # la squadra a cui appartiene la cella
                ax.add_patch(Rectangle((x, y), 1, 1, fc=cols[k], ec="white", lw=2, alpha=0.85))
        somma = " + ".join(str(2 * k - 1) for k in range(1, n + 1))
        ax.text(n / 2, -0.55, f"{somma} = {n * n} = {n}²", ha="center", va="center", fontsize=10)
    fig.suptitle("Ogni nuovo dispari 2n + 1 si aggiunge lungo due lati e un angolo: dal quadrato n × n al quadrato (n + 1) × (n + 1)",
                 fontsize=9.5, color=GRIGIO, y=0.04)
    return _salva(fig, "fond/induzione_dispari_quadrati")


def _golomb(size, missing, ox, oy, board, cnt):
    """Tassellazione ricorsiva (prova di Golomb) della scacchiera size×size con origine (ox, oy) e quadrato mancante."""
    if size == 1:
        return
    h = size // 2
    mx, my = missing
    cnt[0] += 1
    t = cnt[0]
    sub = []
    for qx, qy in ((0, 0), (h, 0), (0, h), (h, h)):
        if ox + qx <= mx < ox + qx + h and oy + qy <= my < oy + qy + h:
            sub.append((qx, qy, missing))
        else:
            cx = ox + qx + (h - 1 if qx == 0 else 0)
            cy = oy + qy + (h - 1 if qy == 0 else 0)
            board[cy][cx] = t
            sub.append((qx, qy, (cx, cy)))
    for qx, qy, m in sub:
        _golomb(h, m, ox + qx, oy + qy, board, cnt)


def _disegna_tassellazione(ax, board, evid=None, buco=None):
    n = len(board)
    for y in range(n):
        for x in range(n):
            v = board[y][x]
            if v == -1:
                ax.add_patch(Rectangle((x, y), 1, 1, fc="#444444", ec="white", lw=1))
                continue
            fc = "#F5B041" if evid is not None and v == evid else PALETTE[v % len(PALETTE)]
            ax.add_patch(Rectangle((x, y), 1, 1, fc=fc, ec=fc, lw=0.5))
    # bordi tra triomini diversi
    for y in range(n):
        for x in range(n):
            v = board[y][x]
            if x + 1 < n and board[y][x + 1] != v:
                ax.plot([x + 1, x + 1], [y, y + 1], color="black", lw=1.1)
            if y + 1 < n and board[y + 1][x] != v:
                ax.plot([x, x + 1], [y + 1, y + 1], color="black", lw=1.1)
    ax.add_patch(Rectangle((0, 0), n, n, fill=False, ec="black", lw=2))
    ax.set_xlim(-0.2, n + 0.2); ax.set_ylim(-0.2, n + 0.2); ax.set_aspect("equal"); ax.axis("off")


def golomb_tassellazione():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.9))
    # sinistra: 4×4 deficiente
    b4 = [[0] * 4 for _ in range(4)]
    b4[2][1] = -1
    _golomb(4, (1, 2), 0, 0, b4, [0])
    _disegna_tassellazione(axs[0], b4)
    axs[0].set_title("4 × 4 deficiente: 5 triomini", fontsize=10.5, color=BLU)
    # destra: 8×8 deficiente, con i quadranti e il triomino centrale
    b8 = [[0] * 8 for _ in range(8)]
    b8[6][1] = -1
    _golomb(8, (1, 6), 0, 0, b8, [0])
    _disegna_tassellazione(axs[1], b8, evid=1)
    axs[1].plot([4, 4], [0, 8], color=ROSSO, lw=2.6, ls="--")
    axs[1].plot([0, 8], [4, 4], color=ROSSO, lw=2.6, ls="--")
    axs[1].set_title("8 × 8 deficiente: quattro quadranti 4 × 4\ne il triomino centrale (arancione)", fontsize=10.5, color=BLU)
    # controllo: ogni triomino copre 3 celle a forma di L
    for b in (b4, b8):
        c = Counter(v for r in b for v in r)
        assert c[-1] == 1 and all(k == 3 for t, k in c.items() if t > 0)
    fig.text(0.5, 0.02, "In grigio scuro il quadrato mancante. Il triomino centrale copre un quadrato di ciascuno dei tre quadranti senza buco:\n"
             "così ogni quadrante diventa una scacchiera 4 × 4 deficiente, tassellabile per ipotesi induttiva.",
             ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "fond/induzione_golomb")


def _L(size):
    """Celle della L di lato 2·size: quadrato 2size × 2size senza il quadrante in alto a destra."""
    return {(x, y) for x in range(2 * size) for y in range(2 * size) if not (x >= size and y >= size)}


def _tassella_L(size, ox=0, oy=0, rot=0, out=None, cnt=None):
    """Tassella la L (lato 2·size) con triomini: la L grande si divide in quattro L di metà lato.
    rot = numero di quarti di giro (antiorari) della L intorno al suo centro."""
    if out is None:
        out, cnt = {}, [0]
    L = 2 * size

    def ruota(x, y, r):
        for _ in range(r):
            x, y = L - 1 - y, x
        return x, y

    if size == 1:
        cnt[0] += 1
        for (x, y) in _L(1):
            rx, ry = ruota(x, y, rot)
            out[(ox + rx, oy + ry)] = cnt[0]
        return out, cnt
    h = size // 2
    # quattro L di lato size (= 2h) nella L di lato 2size (orientamento base: manca il quadrante alto-destra)
    pezzi = [((0, 0), 0), ((size, 0), 1), ((0, size), 3), ((h, h), 0)]
    # (origine, rotazione): in basso a sinistra uguale, in basso a destra ruotata, in alto a sinistra ruotata, al centro uguale
    for (px, py), r in pezzi:
        sub, _ = _tassella_L(h, 0, 0, r, {}, cnt)
        for (x, y), t in sub.items():
            bx, by = px + x, py + y
            rx, ry = ruota(bx, by, rot)
            out[(ox + rx, oy + ry)] = t
    return out, cnt


def esercizio39_L():
    fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.9))
    for ax, size in zip(axs, (1, 2, 4)):
        celle, cnt = _tassella_L(size)
        assert set(celle) == _L(size), size
        c = Counter(celle.values())
        assert all(k == 3 for k in c.values()) and len(c) == size * size
        L = 2 * size
        for (x, y), t in celle.items():
            ax.add_patch(Rectangle((x, y), 1, 1, fc=PALETTE[t % len(PALETTE)], ec=PALETTE[t % len(PALETTE)], lw=0.5))
        for (x, y), t in celle.items():
            if celle.get((x + 1, y), t) != t or ((x + 1, y) not in celle):
                ax.plot([x + 1, x + 1], [y, y + 1], color="black", lw=1.1)
            if celle.get((x, y + 1), t) != t or ((x, y + 1) not in celle):
                ax.plot([x, x + 1], [y + 1, y + 1], color="black", lw=1.1)
            if (x - 1, y) not in celle:
                ax.plot([x, x], [y, y + 1], color="black", lw=1.1)
            if (x, y - 1) not in celle:
                ax.plot([x, x + 1], [y, y], color="black", lw=1.1)
        ax.set_xlim(-0.3, L + 0.3); ax.set_ylim(-0.3, L + 0.3); ax.set_aspect("equal"); ax.axis("off")
        lato = {1: "1", 2: "2", 4: "4"}[size]
        ax.set_title(f"tre quadrati {lato} × {lato}: {size * size} triomin{'o' if size == 1 else 'i'}", fontsize=10.5, color=BLU)
    fig.text(0.5, 0.02, "Ogni L si divide in quattro L di metà lato (in basso a sinistra, in basso a destra, in alto a sinistra e al centro),\n"
             "ognuna tassellata come la figura precedente: per questo i triomini quadruplicano a ogni passo.",
             ha="center", fontsize=9, color=GRIGIO)
    return _salva(fig, "fond/induzione_L_triomini")


if __name__ == "__main__":
    print(dispari_quadrati())
    print(golomb_tassellazione())
    print(esercizio39_L())
