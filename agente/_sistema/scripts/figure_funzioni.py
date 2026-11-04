"""Figure dei capitoli 30-40 di Programmazione (chiamata di funzione, algoritmi su array). PNG in _sistema/figure/prog/.
Uso: python figure_funzioni.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_info import vuoto, BLU, ROSSO, VERDE, GRIGIO, plt, _salva
from matplotlib.patches import FancyArrowPatch, Rectangle

LOCALI, RETVAL, PARAM, CONTROLLO, LIBERO, CODICE = "#CFDDF3", "#CFE5E5", "#EBD3E2", "#FBE3C2", "#EEF3FA", "#FFE9A8"


def _cella(ax, x, y, w, h, testo="", fc=LOCALI, ec="#4a6fa5", fs=10.5, bold=False, col="black"):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=1.2))
    if testo:
        ax.text(x + w / 2, y + h / 2, testo, ha="center", va="center", fontsize=fs, fontweight="bold" if bold else None, color=col)


def _puntatore(ax, x, y, nome, col):
    """Etichetta FP/SP a sinistra della cella, con la punta sul bordo a quota y."""
    ax.annotate(nome, xy=(x, y), xytext=(x - 0.85, y), ha="right", va="center", fontsize=10, fontweight="bold", color=col,
                arrowprops=dict(arrowstyle="-|>", color=col, lw=1.4))


def _graffa(ax, x, y0, y1, testo, col, dx=0.16):
    ax.plot([x, x + dx, x + dx, x], [y0, y0, y1, y1], color=col, lw=1.5, clip_on=False)
    ax.text(x + dx + 0.12, (y0 + y1) / 2, testo, ha="left", va="center", fontsize=9.5, color=col)


def _freccia_indirizzi(ax, x, y0, y1):
    ax.annotate("", xy=(x, y1), xytext=(x, y0), arrowprops=dict(arrowstyle="-|>", color=GRIGIO, lw=1.2))
    ax.text(x + 0.14, (y0 + y1) / 2, "indirizzi crescenti", rotation=90, ha="left", va="center", fontsize=9, color=GRIGIO)


def stack_evoluzione():
    """I sette stati dello stack con main -> sumSquares -> square (due volte)."""
    stati = [["main"], ["main", "sum\nSquares"], ["main", "sum\nSquares", "square"], ["main", "sum\nSquares"],
             ["main", "sum\nSquares", "square"], ["main", "sum\nSquares"], ["main"]]
    fig, ax = vuoto(10.4, 3.4, (-0.9, 16.6), (-0.9, 5.0))
    for k, frames in enumerate(stati):
        x = k * 2.3
        _cella(ax, x, 0, 1.3, 0.55, "codice", fc=CODICE, ec="#b8921f", fs=9)
        _cella(ax, x, 0.55, 1.3, 4.05, "", fc=LIBERO, ec="#9db4d3")
        y = 4.6
        for i, f in enumerate(frames):
            attivo = i == len(frames) - 1
            _cella(ax, x, y - 0.95, 1.3, 0.95, f, fc="#8FA9DB" if attivo else "#D8E2F4", bold=attivo, fs=8.5)
            y -= 0.95
        fp = y + 0.95
        ax.text(x - 0.08, fp, "FP", ha="right", va="center", fontsize=8.5, color=ROSSO, fontweight="bold")
        ax.text(x - 0.08, y, "SP", ha="right", va="center", fontsize=8.5, color=BLU, fontweight="bold")
        ax.text(x + 0.65, -0.32, f"stato {k + 1}", ha="center", fontsize=9, color=GRIGIO)
    ax.text(7.5, -0.75, "il riquadro più scuro è il frame attivo; quelli sopra sono sospesi", ha="center", fontsize=9.5, color=GRIGIO)
    _freccia_indirizzi(ax, 15.7, 0.2, 4.5)
    return _salva(fig, "prog/stack_evoluzione")


def record_attivazione():
    """Disposizione del modello: variabili del chiamante, retval, params, next(PC), FP addr, variabili del chiamato."""
    fig, ax = vuoto(8.6, 4.3, (-3.0, 11.6), (-0.5, 7.2))
    x, w = 0, 4.8
    righe = [("variabili locali del chiamante", LOCALI, 1.0), ("valore di ritorno (retval)", RETVAL, 0.7), ("parametri (params)", PARAM, 1.0),
             ("indirizzo di ritorno: next(PC)", CONTROLLO, 0.7), ("FP del chiamante (FP addr)", CONTROLLO, 0.7), ("variabili locali del chiamato", LOCALI, 1.0)]
    y = 6.8
    bordi = []
    for t, c, h in righe:
        _cella(ax, x, y - h, w, h, t, fc=c, fs=9.5)
        bordi.append((y, y - h))
        y -= h
    _cella(ax, x, 0.0, w, y, "spazio libero dello stack", fc=LIBERO, ec="#9db4d3", fs=9.5, col=GRIGIO)
    fp, sp = bordi[5]
    _puntatore(ax, x, fp, "FP", ROSSO)
    _puntatore(ax, x, sp, "SP", BLU)
    ax.text(x - 0.2, (bordi[1][0] + bordi[4][1]) / 2, "offset\npositivi\nda FP", ha="right", va="center", fontsize=9, color=GRIGIO)
    _graffa(ax, w + 0.05, sp, fp - 0.03, "stack frame del\nchiamato (offset\nnegativi da FP)", "#6a3fb5")
    _graffa(ax, w + 0.05, bordi[4][1] + 0.03, bordi[0][0], "regione gestita\ndal chiamante", GRIGIO)
    _graffa(ax, w + 3.3, sp, bordi[1][0], "record di\nattivazione\ndel chiamato", ROSSO)
    return _salva(fig, "prog/record_attivazione")


def scambio_valore_puntatori():
    """A sinistra swapSbagliato lavora su copie; a destra swap scrive in x e y tramite pA e pB."""
    fig, ax = vuoto(9.4, 4.0, (-1.4, 14.6), (-0.9, 6.4))

    def colonna(x0, titolo, celle, col):
        ax.text(x0 + 1.9, 6.0, titolo, ha="center", fontsize=11, fontweight="bold", color=col)
        y = 5.6
        pos = {}
        for nome, testo, fc in celle:
            _cella(ax, x0, y - 0.8, 3.8, 0.8, testo, fc=fc, fs=10.5)
            pos[nome] = y - 0.4
            y -= 0.8
        return pos

    sx = colonna(0, "swapSbagliato(x, y)", [("x", "int x = 10", LOCALI), ("y", "int y = 20", LOCALI), ("a", "int a = 10 → 20", PARAM), ("b", "int b = 20 → 10", PARAM),
                                             ("c", "dati di controllo", CONTROLLO), ("t", "int tmp = 10", LOCALI)], ROSSO)
    ax.text(1.9, -0.45, "cambiano solo le copie: x e y restano 10 e 20", ha="center", fontsize=9.5, color=ROSSO)
    dx = colonna(8.6, "swap(&x, &y)", [("x", "int x = 10 → 20", LOCALI), ("y", "int y = 20 → 10", LOCALI), ("a", "int* pA", PARAM), ("b", "int* pB", PARAM),
                                        ("c", "dati di controllo", CONTROLLO), ("t", "int tmp = 10", LOCALI)], VERDE)
    for da, a, r in (("a", "x", 0.55), ("b", "y", 0.55)):
        ax.add_patch(FancyArrowPatch((12.4, dx[da]), (12.4, dx[a]), connectionstyle=f"arc3,rad={r}", arrowstyle="-|>", mutation_scale=13, color=VERDE, lw=1.6))
    ax.text(10.5, -0.45, "pA e pB contengono gli indirizzi: *pA = ... scrive in x", ha="center", fontsize=9.5, color=VERDE)
    return _salva(fig, "prog/scambio_valore_puntatori")


def dimensione_capacita():
    """Array con AMAX = 10 e aLen = 6: elementi validi, disponibili, indice 10 non valido."""
    fig, ax = vuoto(9.0, 2.7, (-1.2, 12.2), (-1.5, 2.4))
    valori = ["17", "21", "-3", "8", "19", "7", "??", "??", "??", "??"]
    for i, v in enumerate(valori):
        ok = i < 6
        _cella(ax, i, 0, 1, 0.8, v, fc="#E8EFFA" if ok else "#DDDDDD", ec="#4a6fa5" if ok else "#888888", bold=ok, col="black" if ok else "#666666")
        ax.text(i + 0.5, 0.97, str(i), ha="center", fontsize=9.5, color=GRIGIO)
    _cella(ax, 10, 0, 1.1, 0.8, "non\nvalido", fc="#FBE9E7", ec=ROSSO, fs=8.5, col=ROSSO)
    ax.text(10.5, 0.97, "10", ha="center", fontsize=9.5, color=GRIGIO)
    ax.plot([0, 0, 6, 6], [1.3, 1.45, 1.45, 1.3], color=BLU, lw=1.5)
    ax.text(3, 1.55, "dimensione: aLen = 6, indici [0, aLen)", ha="center", va="bottom", fontsize=9.5, color=BLU)
    ax.plot([6.03, 6.03, 10, 10], [1.3, 1.45, 1.45, 1.3], color=GRIGIO, lw=1.5)
    ax.text(8.2, 1.55, "disponibili: [aLen, AMAX)", ha="center", va="bottom", fontsize=9.5, color=GRIGIO)
    ax.plot([0, 0, 10, 10], [-0.15, -0.3, -0.3, -0.15], color=ROSSO, lw=1.5)
    ax.text(5, -0.72, "capacità: AMAX = 10 elementi, indici validi [0, AMAX)", ha="center", fontsize=9.5, color=ROSSO)
    ax.text(5, -1.2, "vincolo: 0 ≤ aLen ≤ AMAX", ha="center", fontsize=10, fontweight="bold")
    return _salva(fig, "prog/dimensione_capacita")


def indici_coppie():
    """Spazio degli indici degli elementi e spazio degli indici delle coppie adiacenti."""
    fig, ax = vuoto(7.2, 2.3, (-2.6, 6.2), (-1.5, 1.5))
    vals = [2, 4, 4, 6, 9]
    for i, v in enumerate(vals):
        _cella(ax, i * 1.1, -0.2, 1.1, 0.7, str(v), bold=True)
        ax.text(i * 1.1 + 0.55, 0.75, str(i), ha="center", fontsize=10.5, color=BLU)
    ax.text(-0.15, 0.82, "indici elementi [0, aLen)", ha="right", va="center", fontsize=9, color=BLU)
    ax.text(-0.15, 0.15, "a", ha="right", va="center", fontsize=11, fontweight="bold")
    for i in range(1, 5):
        xc = i * 1.1
        ax.plot([xc - 0.5, xc - 0.5, xc + 0.5, xc + 0.5], [-0.3, -0.5, -0.5, -0.3], color=VERDE, lw=1.5)
        ax.text(xc, -0.85, str(i), ha="center", fontsize=10.5, color=VERDE, fontweight="bold")
    ax.text(-0.15, -0.85, "indici coppie [1, aLen)", ha="right", va="center", fontsize=9, color=VERDE)
    ax.text(2.75, -1.32, "la coppia i è (a[i-1], a[i]): 5 elementi, 4 coppie", ha="center", fontsize=9.5, color=GRIGIO)
    return _salva(fig, "prog/indici_coppie")


def bubble_fasi():
    """Le tre fasi del Bubble Sort su {6, 2, -8, 10, 4}: i valori sono calcolati eseguendo l'algoritmo."""
    a = [6, 2, -8, 10, 4]
    fasi = []
    ordinato = False
    while not ordinato:
        ordinato = True
        righe = [(list(a), None)]
        for i in range(1, len(a)):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                ordinato = False
                righe.append((list(a), i))
            else:
                righe.append((list(a), -i))
        fasi.append((righe, ordinato))
    assert a == [-8, 2, 4, 6, 10] and len(fasi) == 3
    fig, ax = vuoto(9.6, 3.6, (-0.4, 21.4), (-1.0, 8.2))
    for f, (righe, fine) in enumerate(fasi):
        x0 = f * 7.2
        ax.text(x0 + 2.5, 7.75, ["Prima fase", "Seconda fase", "Terza fase"][f], ha="center", fontsize=10.5, fontweight="bold")
        for r, (vals, ev) in enumerate(righe):
            y = 6.3 - r * 1.3
            for i, v in enumerate(vals):
                scambiati = ev is not None and ev > 0 and i in (ev - 1, ev)
                confrontati = ev is not None and ev < 0 and i in (-ev - 1, -ev)
                fc = "#FBD9D3" if scambiati else ("#DDEFD9" if confrontati else "#F3F6FB")
                _cella(ax, x0 + i, y, 1, 1.05, str(v), fc=fc, ec="#8aa0bf", fs=9.5, bold=scambiati)
        ax.text(x0 + 2.5, -0.65, "nessuno scambio: ordinato" if fine else "scambi fatti: nuova fase", ha="center", fontsize=9.5, color=VERDE if fine else ROSSO)
    return _salva(fig, "prog/bubble_fasi")


if __name__ == "__main__":
    for f in (stack_evoluzione, record_attivazione, scambio_valore_puntatori, dimensione_capacita, indici_coppie, bubble_fasi):
        print(f())
