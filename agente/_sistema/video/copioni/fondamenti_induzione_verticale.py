# -*- coding: utf-8 -*-
"""Il principio di induzione in 60-90 secondi (Fondamenti, cap. 37). Formato (a), verticale 9:16.

Fonte: _sistema/bozze/fondamenti_cap37.md. Versione breve di copioni/fondamenti_induzione.py.
    python fai_video.py copioni/fondamenti_induzione_verticale.py [--prova]
"""
from videolib import *


def tessera(numero, h=1.5, w=0.36, colore=TESTO):
    r = RoundedRectangle(corner_radius=0.06, width=w, height=h, stroke_color=colore, stroke_width=3,
                         fill_color=colore, fill_opacity=0.18)
    n = etichetta(str(numero), F["piccolo"], TENUE).next_to(r, DOWN, buff=0.18)
    g = VGroup(r, n)
    g.rett = r
    return g


def fila(numeri, passo=1.15, **kw):
    f = VGroup(*[tessera(k, **kw) for k in numeri])
    for i, t in enumerate(f):
        t.shift(RIGHT * i * passo)
    return f


def cade(t, passo=1.15, colore=VERDE):
    r = t.rett
    ang = np.arcsin(min(0.95, (passo - r.width) / r.height))
    return r.animate(path_arc=-ang).rotate(-ang, about_point=r.get_corner(DR)).set_stroke(colore).set_fill(colore)


class InduzioneVerticale(ScenaBase):
    META = dict(materia="fondamenti", slug="induzione_verticale", titolo="Induzione in un minuto",
                formato="9:16", voce="it-IT-GiuseppeMultilingualNeural", velocita=0,
                fonte="_sistema/bozze/fondamenti_cap37.md")

    SEGMENTI = [
        Seg("aggancio", "Induzione",
            "Come dimostri una formula per infiniti numeri? Non puoi provarli tutti. "
            "Ti aiuta il principio di induzione: funziona come una fila di tessere del domino.",
            pausa_dopo=0.5),
        Seg("esempio", "Un esempio",
            "Prendi la somma dei primi enne interi. La formula dice: enne, per enne più uno, diviso due. "
            "Prova con tre. Uno più due più tre fa sei. E tre per quattro, diviso due, fa sei. Torna. "
            "Ma come fai per tutti gli altri numeri?", pausa_dopo=0.5),
        Seg("principio", "Due passi",
            "Fai due passi. Passo base: dimostri che la formula vale per uno. È la prima tessera che cade. "
            "Passo induttivo: supponi che valga per enne, e dimostri che vale per enne più uno. "
            "È ogni tessera che fa cadere la successiva. "
            "Così cadono tutte: la formula vale per ogni enne. "
            "Ma servono tutti e due i passi: uno da solo non basta.", pausa_dopo=0.5),
        Seg("errore", "L'errore tipico",
            "L'errore tipico è saltare il passo base. Se la prima tessera non cade, la catena non parte.",
            pausa_dopo=0.5),
        Seg("verifica", "Tocca a te",
            "Ora tocca a te. Nel passo induttivo, che cosa puoi dare per vero? [pausa 2.2] "
            "Solo la formula per enne: si chiama ipotesi induttiva.", pausa_dopo=1.2),
    ]

    def seg_aggancio(self, s):
        d1 = self.testo("Una formula vera per", 3.6, peso=BOLD)
        d2 = self.testo("infiniti numeri?", 3.6, ACCENTO, BOLD)
        d = VGroup(d1, d2).arrange(DOWN, buff=0.25)
        self.poni(d, 0.5, 0.82)
        self.add(d)
        num = VGroup(*[formula(str(k), 4.2) for k in range(1, 6)], formula("dots.c", 4.2)).arrange(RIGHT, buff=0.6)
        self.poni(num, 0.5, 0.56)
        self.alla("provarli tutti", LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in num], lag_ratio=0.2), run_time=1.2)
        nome = self.testo("principio di induzione", 3.4, ACCENTO, BOLD)
        self.poni(nome, 0.5, 0.36)
        self.alla("principio di induzione", Write(nome), run_time=0.8)
        f = fila(range(1, 6))
        self.poni(f, 0.5, 0.17)
        self.alla("fila di tessere", LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in f], lag_ratio=0.15), run_time=1.0)

    def seg_esempio(self, s):
        self.pulisci()
        et = self.testo("somma fino a n", colore=TENUE)
        fo = formula(r"S_n = (n(n+1))/2", 4.6, ACCENTO)
        self.poni(fo, 0.5, 0.8)
        et.next_to(fo, UP, buff=0.3)
        self.alla("dei primi enne interi", FadeIn(et), run_time=0.4)
        self.alla("enne, per enne", Write(fo), run_time=1.4)
        caso = formula("n = 3", 4.2, TENUE)
        self.poni(caso, 0.5, 0.58)
        self.alla("Prova con tre", FadeIn(caso, shift=UP * 0.15), run_time=0.4)
        a = formula("1 + 2 + 3", 4.4)
        a2 = formula("1 + 2 + 3 = 6", 4.4)
        self.poni(a2, 0.5, 0.42)
        a.move_to(a2, aligned_edge=LEFT)
        self.alla("Uno più due", Write(a), run_time=0.9)
        self.fino_a("fa sei", anticipo=0.15)
        self.trasforma(a, a2, run_time=0.4)
        b = formula(r"(3 dot 4)/2", 4.4)
        b2 = formula(r"(3 dot 4)/2 = 6", 4.4)
        self.poni(b2, 0.5, 0.22)
        b.move_to(b2, aligned_edge=LEFT)
        self.alla("E tre per quattro", Write(b), run_time=0.9)
        self.fino_a("fa sei", anticipo=0.15, n=2)
        self.trasforma(b, b2, run_time=0.4)
        sp = self.spunta(b2)
        self.alla("Torna", Create(sp), a2.animate.set_color(VERDE), b2.animate.set_color(VERDE), run_time=0.4)
        dub = self.testo("e tutti gli altri n?", colore=ROSSO)
        self.poni(dub, 0.5, 0.04)
        self.alla("Ma come fai", FadeIn(dub, shift=UP * 0.15), run_time=0.4)

    def seg_principio(self, s):
        self.pulisci()
        base = self.testo("passo base", 3.2, VERDE, BOLD)
        f1 = formula("S(1)", 4.4)
        indu = self.testo("passo induttivo", 3.2, ACCENTO, BOLD)
        f2 = formula("S(n) -> S(n+1)", 4.4)
        self.poni(base, 0.5, 0.94)
        self.poni(f1, 0.5, 0.82)
        self.poni(indu, 0.5, 0.64)
        self.poni(f2, 0.5, 0.52)
        f = fila(range(1, 6))
        self.poni(f, 0.5, 0.31)
        self.alla("Passo base", FadeIn(base, shift=UP * 0.15), run_time=0.4)
        self.alla("vale per uno", Write(f1), FadeIn(f), run_time=0.7)
        self.alla("prima tessera", cade(f[0]), run_time=0.5)
        self.alla("Passo induttivo", FadeIn(indu, shift=UP * 0.15), run_time=0.4)
        fa = formula("S(n)", 4.4).move_to(f2, aligned_edge=LEFT)
        self.alla("supponi che", Write(fa), run_time=0.6)
        self.fino_a("e dimostri", anticipo=0.15)
        self.trasforma(fa, f2, run_time=0.7)
        self.alla("ogni tessera", cade(f[1]), run_time=0.5)
        self.alla("Così cadono tutte", LaggedStart(*[cade(t) for t in f[2:]], lag_ratio=0.5), run_time=1.4)
        fine = formula("forall n >= 1 quad S(n)", 4.6, VERDE)
        self.poni(fine, 0.5, 0.07)
        self.alla("vale per ogni enne", Write(fine), run_time=0.8)

    def seg_errore(self, s):
        self.pulisci()
        e1 = self.testo("saltare il passo base", 3.2, ROSSO, BOLD)
        self.poni(e1, 0.5, 0.82)
        f = fila(range(1, 6))
        self.poni(f, 0.5, 0.5)
        self.alla("saltare", FadeIn(e1, shift=UP * 0.15), FadeIn(f), run_time=0.5)
        cr = self.croce(f[0]).scale(1.6)
        cr.next_to(f[0].rett, UP, buff=0.2)
        self.alla("prima tessera non cade", Create(cr), f[0].rett.animate.set_stroke(ROSSO).set_fill(ROSSO), run_time=0.5)
        fermo = self.testo("la catena non parte", colore=TENUE)
        self.poni(fermo, 0.5, 0.26)
        self.alla("la catena non parte", FadeIn(fermo, shift=UP * 0.15), run_time=0.4)

    def seg_verifica(self, s):
        self.pulisci()
        d1 = self.testo("Nel passo induttivo,", 3.2, peso=BOLD)
        d2 = self.testo("cosa dai per vero?", 3.2, ACCENTO, BOLD)
        d = VGroup(d1, d2).arrange(DOWN, buff=0.25)
        self.poni(d, 0.5, 0.8)
        self.alla("Nel passo induttivo", FadeIn(d, shift=UP * 0.15), run_time=0.4)
        f2 = formula(f"{col('S(n)', AZZURRO)} -> S(n+1)", 4.6)
        self.poni(f2, 0.5, 0.52)
        self.alla("che cosa puoi", FadeIn(f2), run_time=0.4)
        ip = formula("S(n)", 4.6).move_to(f2, aligned_edge=LEFT)
        gr = Brace(ip, DOWN, buff=0.12, color=AZZURRO)
        nome = self.testo("ipotesi induttiva", 3.2, AZZURRO, BOLD)
        nome.next_to(gr, DOWN, buff=0.2)
        nome.set_x(self.punto(0.5, 0)[0])
        self.alla("Solo la formula", GrowFromCenter(gr), run_time=0.4)
        self.alla("ipotesi induttiva", FadeIn(nome, shift=UP * 0.1), run_time=0.4)
