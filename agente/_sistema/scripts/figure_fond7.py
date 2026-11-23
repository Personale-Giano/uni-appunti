"""Figure dei capitoli 45-46 di Fondamenti (funzioni, L23 del 20 nov 2026): diagrammi a frecce
di relazioni che sono o non sono funzioni, iniettive, suriettive, biiettive; inversa e composizione.
PNG in _sistema/figure/fond/.  Uso: python figure_fond7.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_math import BLU, ROSSO, VERDE, ARANCIO, GRIGIO, ovali_ax, pannelli


def _pannello(A, B, coppie, titolo, rosse=(), nomeA="X", nomeB="Y"):
    """Un pannello X -> Y; le coppie in `rosse` sono disegnate in rosso tratteggiato (quelle che creano il problema)."""
    def disegna(ax):
        ovali = [dict(nome=nomeA, elems=A, cx=2.3, w=2.4, h=4.6), dict(nome=nomeB, elems=B, cx=7.7, w=2.4, h=4.6)]
        frecce = []
        for a, b in coppie:
            r = (a, b) in rosse
            frecce.append(dict(da=(0, a), a=(1, b), col=ROSSO if r else BLU, tratt=r))
        ovali_ax(ax, ovali, frecce, titolo=titolo, fs=11)
    return disegna


def funzioni_e_no():
    """Quattro diagrammi: due relazioni che non sono funzioni e due funzioni (una né iniettiva né suriettiva, una biiettiva)."""
    X3, X4, Y3 = [1, 2, 3], [1, 2, 3, 4], ["p", "q", "r"]
    d = [
        _pannello(X4, Y3, [(1, "q"), (2, "p"), (3, "r")], "(a) non è una funzione:\nda 4 non esce nessuna freccia"),
        _pannello(X3, Y3, [(1, "p"), (2, "q"), (2, "r"), (3, "r")], "(b) non è una funzione:\nda 2 escono due frecce",
                  rosse={(2, "q"), (2, "r")}),
        _pannello(X3, Y3, [(1, "r"), (2, "p"), (3, "r")], "(c) funzione né iniettiva\nné suriettiva", rosse={(1, "r"), (3, "r")}),
        _pannello(X3, Y3, [(1, "q"), (2, "r"), (3, "p")], "(d) funzione biiettiva: a ogni\npunto di Y arriva una sola freccia"),
    ]
    return pannelli("fond/funzioni_frecce", d, ncols=4, larghezza=3.3, altezza=3.2)


def inversa_composizione():
    """Sinistra: f e la sua inversa (frecce rovesciate). Destra: g, f e la composizione f ∘ g (si seguono i cammini)."""
    def inversa(ax):
        ovali = [dict(nome="X", elems=[1, 2, 3], cx=1.6, w=2.0, h=4.4), dict(nome="Y", elems=["a", "b", "c"], cx=5.0, w=2.0, h=4.4),
                 dict(nome="X", elems=[1, 2, 3], cx=8.4, w=2.0, h=4.4)]
        fr = [dict(da=(0, 1), a=(1, "c"), col=BLU), dict(da=(0, 2), a=(1, "a"), col=BLU), dict(da=(0, 3), a=(1, "b"), col=BLU),
              dict(da=(1, "c"), a=(2, 1), col=VERDE), dict(da=(1, "a"), a=(2, 2), col=VERDE), dict(da=(1, "b"), a=(2, 3), col=VERDE)]
        ovali_ax(ax, ovali, fr, titolo="(a) f (blu) e f⁻¹ (verde): le frecce di f⁻¹\nsono quelle di f percorse al contrario", fs=11)
        ax.text(3.3, 0.15, "f", color=BLU, ha="center", fontsize=12, style="italic")
        ax.text(6.7, 0.15, "f⁻¹", color=VERDE, ha="center", fontsize=12, style="italic")

    def composizione(ax):
        ovali = [dict(nome="X", elems=[1, 2, 3], cx=1.6, w=2.0, h=4.4), dict(nome="Y", elems=["a", "b", "c"], cx=5.0, w=2.0, h=4.4),
                 dict(nome="Z", elems=["u", "v", "w"], cx=8.4, w=2.0, h=4.4)]
        fr = [dict(da=(0, 1), a=(1, "b"), col=BLU), dict(da=(0, 2), a=(1, "c"), col=BLU), dict(da=(0, 3), a=(1, "b"), col=BLU),
              dict(da=(1, "a"), a=(2, "w"), col=GRIGIO, tratt=True), dict(da=(1, "b"), a=(2, "u"), col=ARANCIO),
              dict(da=(1, "c"), a=(2, "v"), col=ARANCIO)]
        ovali_ax(ax, ovali, fr, titolo="(b) g (blu) e poi f (arancio): f ∘ g manda 1 e 3 in u, 2 in v;\nla freccia tratteggiata da a non viene mai usata", fs=11)
        ax.text(3.3, 0.15, "g", color=BLU, ha="center", fontsize=12, style="italic")
        ax.text(6.7, 0.15, "f", color=ARANCIO, ha="center", fontsize=12, style="italic")

    return pannelli("fond/inversa_composizione", [inversa, composizione], ncols=2, larghezza=5.6, altezza=3.4, wspace=0.08)


if __name__ == "__main__":
    for f in (funzioni_e_no, inversa_composizione):
        print(f())
