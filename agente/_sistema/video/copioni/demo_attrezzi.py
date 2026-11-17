# -*- coding: utf-8 -*-
"""Collaudo degli attrezzi di videolib (codice, tabella di traccia, caselle, pila, figura).
Non e' un video da pubblicare: serve a controllare la libreria dopo una modifica.
    python fai_video.py copioni/demo_attrezzi.py --prova
"""
from videolib import *

SORGENTE = """
int somma(int a[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++)
        s += a[i];
    return s;
}
"""


class Demo(ScenaBase):
    META = dict(materia="prove", slug="demo_attrezzi", titolo="Collaudo", formato="16:9")
    SEGMENTI = [
        Seg("codice", "Codice e traccia",
            "Quanto vale la somma alla fine? Guarda il ciclo. All'inizio la somma vale zero. "
            "Al primo giro aggiungi tre. Al secondo giro aggiungi uno, e la somma diventa quattro."),
        Seg("pila", "Pila e figura",
            "Ora la pila. Il main entra per primo. Poi arriva la funzione chiamata, e il puntatore scende. "
            "Quando la funzione finisce, il suo spazio torna libero. Dove punta adesso il puntatore? "
            "[pausa 2] Punta di nuovo sotto il main."),
    ]

    def seg_codice(self, s):
        c = self.codice(SORGENTE)
        self.poni(c, 0.28, 0.6, larg=0.55)
        a = Caselle([3, 1, 4], nome="a")
        self.poni(a, 0.28, 0.3, larg=0.5)
        t = TabellaTraccia(["i", "s"])
        self.poni(t, 0.72, 0.8)
        self.play(FadeIn(c), FadeIn(a), FadeIn(t))
        f = a.freccia(0, "i", sopra=False)
        self.alla("zero", c.riga(2))
        self.play(t.passo("", 0))
        self.alla("primo giro", c.riga(4), FadeIn(f))
        self.play(t.passo(0, 3))
        self.alla("secondo giro", a.sposta(f, 1))
        self.alla("quattro", t.passo(1, 4))
        self.evidenzia(t)

    def seg_pila(self, s):
        self.pulisci()
        p = Pila(posti=6, titolo="stack")
        self.poni(p, 0.3, 0.5)
        fig = self.figura("fond/induzione_dispari_quadrati.png", larg=0.4, alt=0.6)
        self.poni(fig, 0.78, 0.5)
        self.play(FadeIn(p), FadeIn(fig))
        self.alla("main", p.push("main", alt=2, colore=AZZURRO))
        sp = p.puntatore("SP", ACCENTO, lato=RIGHT)
        self.play(FadeIn(sp))
        self.alla("funzione chiamata", p.push("x", 2, colore=VERDE), p.attiva("x"))
        self.play(p.sposta("SP"))
        self.alla("torna libero", p.pop(), p.attiva("main"))
        self.alla("Punta di nuovo", p.sposta("SP"))
