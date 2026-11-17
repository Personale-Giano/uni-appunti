# -*- coding: utf-8 -*-
"""Il principio di induzione (Fondamenti dell'Informatica, cap. 37). Formato (b), 16:9.

Fonte: _sistema/bozze/fondamenti_cap37.md (stessa notazione: S_n la somma, S(n) l'enunciato,
passo base, passo induttivo, ipotesi induttiva; la catena S_(n+1) = S_n + (n+1) = ... e' quella del capitolo).
    python fai_video.py copioni/fondamenti_induzione.py [--prova]
"""
from videolib import *

FORMULA = r"S_n = (n(n+1))/2"
SOMMA = r"S_n = 1 + 2 + dots.c + n = (n(n+1))/2"


def tessera(numero, h=1.6, w=0.38, colore=TESTO):
    r = RoundedRectangle(corner_radius=0.06, width=w, height=h, stroke_color=colore, stroke_width=3,
                         fill_color=colore, fill_opacity=0.18)
    n = etichetta(str(numero), F["piccolo"], TENUE).next_to(r, DOWN, buff=0.18)
    g = VGroup(r, n)
    g.rett = r
    return g


def fila(numeri, passo=1.3, **kw):
    f = VGroup(*[tessera(k, **kw) for k in numeri])
    for i, t in enumerate(f):
        t.shift(RIGHT * i * passo)
    return f


def cade(t, passo=1.3, colore=None):
    """La tessera ruota sullo spigolo in basso a destra fino ad appoggiarsi alla successiva."""
    r = t.rett
    ang = np.arcsin(min(0.95, (passo - r.width) / r.height))
    an = r.animate(path_arc=-ang).rotate(-ang, about_point=r.get_corner(DR))
    return an.set_stroke(colore).set_fill(colore) if colore else an


class Induzione(ScenaBase):
    META = dict(materia="fondamenti", slug="induzione", titolo="Il principio di induzione",
                formato="16:9", voce="it-IT-GiuseppeMultilingualNeural", velocita=0,
                fonte="_sistema/bozze/fondamenti_cap37.md")

    SEGMENTI = [
        Seg("aggancio", "La domanda",
            "Come fai a dimostrare che una proprietà vale per infiniti numeri? "
            "Non puoi controllarli uno per uno: non finiresti mai. "
            "Per questo c'è il principio di induzione. Oggi vedi come funziona, con un esempio."),
        Seg("domino", "L'idea: le tessere del domino",
            "Pensa a una fila di tessere del domino, numerate da uno in poi. Sai due cose. "
            "Primo: la tessera uno cade. "
            "Secondo: ogni tessera che cade fa cadere la successiva. "
            "Allora cadono tutte? Sì. La uno cade, quindi cade la due. "
            "La due cade, quindi cade la tre. E così via, senza fine."),
        Seg("esempio", "Un esempio con i numeri",
            "Ora un esempio concreto: somma i primi interi. "
            "Fino a uno, ottieni uno. Fino a due, tre. Fino a tre, sei. Fino a quattro, dieci. "
            "Qualcuno ti propone una formula: la somma fino a enne vale enne, per enne più uno, diviso due. "
            "Prova con quattro: quattro per cinque, diviso due. Quanto fa? "
            "Dieci: torna. Ma qualche controllo non basta: i numeri sono infiniti."),
        Seg("principio", "Il principio di induzione",
            "Ecco il principio di induzione. Chiama esse di enne l'enunciato che vuoi dimostrare. "
            "Devi fare due passi. "
            "Il passo base: dimostri che l'enunciato vale per uno. È la prima tessera. "
            "Il passo induttivo: supponi che l'enunciato valga per un enne qualsiasi, "
            "e dimostri che vale per enne più uno. "
            "È la tessera che fa cadere la successiva."),
        Seg("ipotesi", "L'ipotesi induttiva",
            "Quello che supponi nel passo induttivo ha un nome: ipotesi induttiva. "
            "Non l'hai dimostrata: la supponi vera, e la usi per arrivare a enne più uno. "
            "Fatti i due passi, l'enunciato vale per ogni enne: le tessere cadono tutte.", velocita=-6),
        Seg("base", "Dimostrazione: passo base",
            "Dimostriamo la formula della somma per induzione. Qui l'enunciato è la formula stessa. "
            "Passo base: enne vale uno. La somma è uno. "
            "La formula dà uno per due, diviso due: cioè uno. "
            "Coincidono: il passo base è fatto.", velocita=-8),
        Seg("passo", "Dimostrazione: passo induttivo",
            "Passo induttivo. Supponi la formula vera per enne: è l'ipotesi induttiva. "
            "Devi arrivare alla stessa formula, con enne più uno al posto di enne. "
            "Parti dalla somma fino a enne più uno. "
            "È la somma fino a enne, più l'ultimo termine: enne più uno. "
            "Qui usi l'ipotesi induttiva: sostituisci la somma fino a enne con la sua formula. "
            "Ora porta tutto a denominatore due. Poi raccogli enne più uno. "
            "Ottieni enne più uno, per enne più due, diviso due. "
            "È la formula con enne più uno al posto di enne: il passo induttivo è fatto.", velocita=-15),
        Seg("errori", "Due errori tipici",
            "Attenzione a due errori tipici. Primo errore: saltare il passo base. "
            "Se la prima tessera non cade, la catena non parte. Non puoi concludere niente, anche se il passo induttivo funziona. "
            "Secondo errore: nel passo induttivo, usare la formula con enne più uno. "
            "È quella che devi dimostrare: non puoi darla per vera. "
            "Puoi dare per vera solo l'ipotesi induttiva."),
        Seg("riepilogo", "Riepilogo",
            "Riassumendo, in tre punti. Uno: il passo base. L'enunciato vale per uno. "
            "Due: il passo induttivo. Se l'enunciato vale per enne, allora vale per enne più uno. "
            "Tre: nel passo induttivo dai per vera solo l'ipotesi induttiva, mai quello che devi dimostrare."),
        Seg("verifica", "Tocca a te",
            "Ora tocca a te. Riguarda la dimostrazione della somma: "
            "in quale passaggio abbiamo usato l'ipotesi induttiva? [pausa 2.8] "
            "Nel secondo: quando abbiamo sostituito la somma fino a enne con la sua formula. "
            "Per allenarti, dimostra per induzione che la somma dei primi enne numeri dispari "
            "vale enne al quadrato.", pausa_dopo=1.5),
    ]

    # ------------------------------------------------------------------
    def seg_aggancio(self, s):
        dom = self.testo("Vale per infiniti numeri?", 7, peso=BOLD)
        self.poni(dom, 0.5, 0.78)
        self.play(FadeIn(dom), run_time=0.4)
        numeri = VGroup(*[formula(str(k), 7) for k in range(1, 8)], formula("dots.c", 7))
        numeri.arrange(RIGHT, buff=0.75)
        self.poni(numeri, 0.5, 0.48)
        spunte = VGroup(*[self.spunta(n).scale(0.8).next_to(n, DOWN, buff=0.25) for n in numeri[:-1]])
        self.alla("uno per uno", LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in numeri], lag_ratio=0.25),
                  LaggedStart(*[Create(x) for x in spunte], lag_ratio=0.25), run_time=3.0)
        nome = self.testo("principio di induzione", 7, ACCENTO, BOLD)
        self.poni(nome, 0.5, 0.14)
        self.alla("principio di induzione", Write(nome), run_time=1.0)
        self.alla("con un esempio", numeri.animate.set_opacity(OPACITA_SFONDO),
                  spunte.animate.set_stroke(opacity=OPACITA_SFONDO), run_time=0.4)

    # ------------------------------------------------------------------
    def seg_domino(self, s):
        self.pulisci()
        f = fila(range(1, 9))
        punti = formula("dots.c", 7).next_to(f, RIGHT, buff=1.5).shift(UP * 0.2)
        g = VGroup(f, punti)
        self.poni(g, 0.5, 0.34)
        self.alla("fila di tessere", LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in f], FadeIn(punti),
                                                 lag_ratio=0.12), run_time=1.6)
        r1 = self.testo("1.  la tessera 1 cade", colore=VERDE)
        r2 = self.testo("2.  ogni tessera fa cadere la successiva", colore=AZZURRO)
        righe = VGroup(r1, r2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        self.poni(righe, 0.5, 0.84)
        self.alla("Primo", FadeIn(r1, shift=RIGHT * 0.2), f[0].rett.animate.set_stroke(VERDE).set_fill(VERDE))
        fr = CurvedArrow(f[2].rett.get_top() + UP * 0.12, f[3].rett.get_top() + UP * 0.12, angle=-1.2,
                         color=AZZURRO, stroke_width=5, tip_length=0.22)
        self.alla("Secondo", FadeIn(r2, shift=RIGHT * 0.2), Create(fr))
        self.alla("Allora cadono tutte", FadeOut(fr), run_time=0.3)
        self.alla("La uno cade", cade(f[0]), run_time=0.5)
        self.alla("cade la due", cade(f[1], colore=VERDE), run_time=0.5)
        self.alla("cade la tre", cade(f[2], colore=VERDE), run_time=0.5)
        self.alla("E così via", LaggedStart(*[cade(t, colore=VERDE) for t in f[3:]], lag_ratio=0.5), run_time=2.2)

    # ------------------------------------------------------------------
    def seg_esempio(self, s):
        self.pulisci()
        sx = [r"1", r"1 + 2", r"1 + 2 + 3", r"1 + 2 + 3 + 4"]
        dx = ["1", "3", "6", "10"]
        righe = []
        for i in range(4):
            a, u, b = formula(sx[i], 6.5), formula("=", 6.5), formula(dx[i], 6.5)
            u.move_to(self.punto(0.36, 0.86 - i * 0.2))
            a.next_to(u, LEFT, buff=0.25)
            b.next_to(u, RIGHT, buff=0.25)
            a.set_y(u.get_y())
            b.set_y(u.get_y())
            righe.append(VGroup(a, u, b))
        for i, quando in enumerate(["Fino a uno", "Fino a due", "Fino a tre", "Fino a quattro"]):
            self.alla(quando, FadeIn(righe[i][0], shift=RIGHT * 0.2), FadeIn(righe[i][1]), run_time=0.4)
            self.play(FadeIn(righe[i][2]), run_time=0.3)
        et = self.testo("somma fino a n", colore=TENUE)
        fo = formula(FORMULA, 8, ACCENTO)
        self.poni(fo, 0.76, 0.66)
        et.next_to(fo, UP, buff=0.3)
        self.alla("una formula", FadeIn(et), run_time=0.4)
        self.alla("vale enne", Write(fo), run_time=1.6)
        prova = formula(r"S_4 = (4 dot 5)/2", 7)
        self.poni(prova, 0.72, 0.26)
        self.alla("Prova con quattro", FadeIn(prova, shift=UP * 0.2))
        ris = formula(r"S_4 = (4 dot 5)/2 = 10", 7)
        ris.move_to(prova, aligned_edge=LEFT)
        self.fino_a("Dieci", anticipo=0.15, n=2)
        self.trasforma(prova, ris, run_time=0.5)
        sp = self.spunta(ris)
        self.play(Create(sp), righe[3][2].animate.set_color(VERDE), run_time=0.4)
        dub = self.testo("e tutti gli altri n?", colore=ROSSO)
        dub.move_to(self.punto(0.36, 0.06))
        self.alla("non basta", FadeIn(dub, shift=UP * 0.2))
        self.evidenzia(dub, fo)

    # ------------------------------------------------------------------
    def _schema(self):
        """Lo schema del principio: usato in «principio», «ipotesi» e «riepilogo»."""
        base = self.testo("passo base", colore=VERDE, peso=BOLD)
        indu = self.testo("passo induttivo", colore=ACCENTO, peso=BOLD)
        f1 = formula("S(1)", 7)
        f2 = formula("forall n >= 1 quad S(n) -> S(n+1)", 7)
        base.move_to(self.punto(0.03, 0.62), aligned_edge=LEFT)
        indu.move_to(self.punto(0.03, 0.34), aligned_edge=LEFT)
        f1.move_to(self.punto(0.31, 0.62), aligned_edge=LEFT)
        f2.move_to(self.punto(0.31, 0.34), aligned_edge=LEFT)
        return base, indu, f1, f2

    def seg_principio(self, s):
        self.pulisci()
        en = formula("S(n)", 7.5)
        et = self.testo("l'enunciato da dimostrare", colore=TENUE)
        testa = VGroup(en, et).arrange(RIGHT, buff=0.5)
        testa.move_to(self.punto(0.03, 0.9), aligned_edge=LEFT)
        self.alla("esse di enne", Write(en), run_time=0.7)
        self.play(FadeIn(et), run_time=0.4)
        base, indu, f1, f2 = self._schema()
        self.alla("Il passo base", FadeIn(base, shift=RIGHT * 0.2))
        self.alla("vale per uno", Write(f1), run_time=0.7)
        t1 = tessera(1, h=1.0, w=0.26, colore=VERDE)
        t1.move_to(self.punto(0.89, 0.62))
        self.alla("prima tessera", FadeIn(t1, shift=UP * 0.2))
        self.alla("Il passo induttivo", FadeIn(indu, shift=RIGHT * 0.2))
        fa = formula("forall n >= 1 quad S(n)", 7).move_to(f2, aligned_edge=LEFT)
        self.alla("supponi che", Write(fa), run_time=1.2)
        self.fino_a("e dimostri", anticipo=0.15)
        self.trasforma(fa, f2, run_time=0.8)
        tn = tessera("n", h=1.0, w=0.26, colore=ACCENTO)
        tn1 = tessera("n+1", h=1.0, w=0.26, colore=ACCENTO)
        tn.move_to(self.punto(0.85, 0.34))
        tn1.move_to(self.punto(0.94, 0.34))
        self.alla("È la tessera che fa cadere", FadeIn(tn, shift=UP * 0.2), FadeIn(tn1, shift=UP * 0.2))
        self.play(Rotate(tn.rett, -0.75, about_point=tn.rett.get_corner(DR)), run_time=0.5)
        self.schema = dict(testa=testa, base=base, indu=indu, f1=f1, f2=f2, t1=t1, tn=tn, tn1=tn1)

    def seg_ipotesi(self, s):
        d = self.schema
        f2 = d["f2"]
        f2c = formula(f"forall n >= 1 quad {col('S(n)', AZZURRO)} -> S(n+1)", 7).move_to(f2)
        ip = formula("forall n >= 1 quad S(n)", 7).move_to(f2c, aligned_edge=LEFT)
        ip = VGroup(*ip[-4:])                                          # solo per misurare la parte S(n)
        nome = self.testo("ipotesi induttiva", colore=AZZURRO, peso=BOLD)
        graffa = Brace(ip, DOWN, buff=0.12, color=AZZURRO)
        nome.next_to(graffa, DOWN, buff=0.12)
        self.fino_a("ipotesi induttiva", anticipo=0.5)
        self.trasforma(f2, f2c, run_time=0.4, corrispondenze=False)
        self.play(GrowFromCenter(graffa), FadeIn(nome, shift=UP * 0.1), run_time=0.5)
        d["f2"] = f2c
        self.alla("la supponi", Indicate(nome, color=AZZURRO, scale_factor=1.08), run_time=0.7)
        fine = formula("forall n >= 1 quad S(n)", 7.5, VERDE)
        fine.move_to(self.punto(0.31, 0.9), aligned_edge=LEFT)
        self.alla("vale per ogni enne", FadeOut(d["testa"][1]), ReplacementTransform(d["testa"][0], fine), run_time=0.8)
        self.alla("cadono tutte", Rotate(d["tn1"].rett, -0.75, about_point=d["tn1"].rett.get_corner(DR)),
                  Rotate(d["t1"].rett, -0.75, about_point=d["t1"].rett.get_corner(DR)), run_time=0.5)

    # ------------------------------------------------------------------
    def seg_base(self, s):
        self.pulisci()
        self.fino_a("Qui l'enunciato", anticipo=0.3)
        self.enunciato(formula("S(n) : quad " + SOMMA, 5.0))
        nome = self.testo("passo base", colore=VERDE, peso=BOLD)
        nome.move_to(self.punto(0.03, 0.84), aligned_edge=LEFT)
        caso = formula("n = 1", 7)
        caso.next_to(nome, RIGHT, buff=0.6)
        self.alla("Passo base", FadeIn(nome, shift=RIGHT * 0.2))
        self.alla("enne vale uno", FadeIn(caso), run_time=0.4)
        a = formula("S_1 = 1", 8)
        self.poni(a, 0.28, 0.48)
        self.alla("La somma è uno", Write(a), run_time=0.7)
        b = formula("(1 dot 2)/2", 8)
        self.poni(b, 0.66, 0.48)
        b2 = formula("(1 dot 2)/2 = 1", 8).move_to(b, aligned_edge=LEFT)
        self.alla("La formula dà", Write(b), run_time=0.8)
        self.fino_a("cioè uno", anticipo=0.15)
        self.trasforma(b, b2, run_time=0.5)
        sp = self.spunta(nome)
        sp.next_to(caso, RIGHT, buff=0.4)
        self.alla("Coincidono", a.animate.set_color(VERDE), b2.animate.set_color(VERDE), run_time=0.4)
        self.alla("è fatto", Create(sp), run_time=0.4)
        self.base = VGroup(nome, caso, sp)
        self.conti_base = VGroup(a, b2)

    def seg_passo(self, s):
        self.play(FadeOut(self.conti_base), self.base.animate.set_opacity(OPACITA_SFONDO), run_time=0.4)
        nome = self.testo("passo induttivo", colore=ACCENTO, peso=BOLD)
        nome.move_to(self.punto(0.03, 0.84), aligned_edge=LEFT)
        self.play(FadeOut(self.base), FadeIn(nome, shift=RIGHT * 0.2), run_time=0.4)
        # ipotesi induttiva e tesi, affiancate
        e_ip = self.testo("ipotesi induttiva", colore=AZZURRO)
        f_ip = formula(FORMULA, 6.5, AZZURRO)
        e_te = self.testo("da dimostrare", colore=TENUE)
        f_te = formula(r"S_(n+1) = ((n+1)(n+2))/2", 6.5, TENUE)
        f_ip.move_to(self.punto(0.24, 0.5))
        f_te.move_to(self.punto(0.72, 0.5))
        e_ip.next_to(f_ip, UP, buff=0.38)
        e_te.next_to(f_te, UP, buff=0.38)
        e_te.set_y(e_ip.get_y())
        self.alla("Supponi la formula", FadeIn(f_ip, shift=UP * 0.15))
        self.alla("ipotesi induttiva", FadeIn(e_ip), run_time=0.4)
        f_te0 = formula(r"S_(n+1) = ((n+1)((n+1)+1))/2", 6.5, TENUE).move_to(f_te)
        self.alla("Devi arrivare", FadeIn(e_te), FadeIn(f_te0, shift=UP * 0.15))
        self.fino_a("al posto di enne", anticipo=0.2)
        self.trasforma(f_te0, f_te, run_time=0.7)
        # la catena, che si trasforma sul posto
        y = 0.13
        c0 = formula(r"S_(n+1)", 8)
        c1 = formula(f"S_(n+1) = {col('S_n', AZZURRO)} + {col('(n+1)', ACCENTO)}", 8)
        c2 = formula(f"S_(n+1) = {col('(n(n+1))/2', AZZURRO)} + {col('(n+1)', ACCENTO)}", 8)
        c3 = formula(f"S_(n+1) = (n(n+1))/2 + {col('(2(n+1))/2', ACCENTO)}", 8)
        c3b = formula(f"S_(n+1) = (n(n+1) + {col('2(n+1)', ACCENTO)})/2", 8)
        c4 = formula(f"S_(n+1) = {col('((n+1)(n+2))/2', VERDE)}", 8)
        for c in (c1, c2, c3, c3b, c4):
            c.move_to(self.punto(0.5, y))
        c0.move_to(c1, aligned_edge=LEFT)
        self.alla("Parti dalla somma", Write(c0), run_time=0.7)
        self.fino_a("È la somma fino a enne", anticipo=0.15)
        self.trasforma(c0, c1, run_time=0.9)
        self.alla("l'ultimo termine", Indicate(c1[-5:], color=ACCENTO, scale_factor=1.12), run_time=0.8)
        riq = riquadro(f_ip, AZZURRO, margine=0.16, riempi=SFONDO)
        riq.set_fill(opacity=0)
        self.alla("Qui usi", Create(riq), run_time=0.5)
        self.fino_a("sostituisci", anticipo=0.15)
        self.trasforma(c1, c2, run_time=1.0)
        sp_ip = self.spunta(f_ip, AZZURRO)
        sp_ip.next_to(riq, RIGHT, buff=0.2)
        self.play(Create(sp_ip), run_time=0.3)
        self.fino_a("denominatore due", anticipo=0.4)
        self.trasforma(c2, c3, run_time=0.9)
        self.fino_a("Poi raccogli", anticipo=0.3)
        self.trasforma(c3, c3b, run_time=0.8)
        self.fino_a("Ottieni", anticipo=0.15)
        self.trasforma(c3b, c4, run_time=1.0)
        sp = self.spunta(nome)
        self.alla("È la formula con", f_te.animate.set_color(VERDE), e_te.animate.set_opacity(OPACITA_SFONDO),
                  Indicate(c4, color=VERDE, scale_factor=1.05), run_time=0.8)
        self.alla("è fatto", Create(sp), run_time=0.4)

    # ------------------------------------------------------------------
    def seg_errori(self, s):
        self.pulisci()
        self.togli_enunciato()
        e1 = self.testo("1.  saltare il passo base", colore=ROSSO, peso=BOLD)
        e1.move_to(self.punto(0.03, 0.88), aligned_edge=LEFT)
        f = fila(range(1, 7), h=1.3, w=0.32)
        self.poni(f, 0.5, 0.48)
        self.alla("Primo errore", FadeIn(e1, shift=RIGHT * 0.2), FadeIn(f), run_time=0.5)
        cr = self.croce(f[0])
        cr.scale(1.6).next_to(f[0].rett, UP, buff=0.2)
        self.alla("prima tessera non cade", Create(cr), f[0].rett.animate.set_stroke(ROSSO).set_fill(ROSSO), run_time=0.5)
        fermo = self.testo("la catena non parte", colore=TENUE)
        fermo.next_to(f, DOWN, buff=0.5)
        self.alla("la catena non parte", FadeIn(fermo), run_time=0.4)
        self.fino_a("Secondo errore", anticipo=0.6)
        self.pulisci(run_time=0.3)
        e2 = self.testo("2.  usare quello che devi dimostrare", colore=ROSSO, peso=BOLD)
        e2.move_to(self.punto(0.03, 0.88), aligned_edge=LEFT)
        self.play(FadeIn(e2, shift=RIGHT * 0.2), run_time=0.4)
        no = formula(r"S_(n+1) = ((n+1)(n+2))/2", 7.5)
        si = formula(FORMULA, 7.5, AZZURRO)
        no.move_to(self.punto(0.3, 0.56))
        si.move_to(self.punto(0.3, 0.2))
        self.alla("la formula con enne più uno", FadeIn(no, shift=UP * 0.15))
        cx = Arrow(ORIGIN, LEFT * 0.7, buff=0, color=ROSSO, stroke_width=5)
        cx.next_to(no, RIGHT, buff=0.4)
        t_no = self.testo("non usarla", colore=ROSSO).next_to(cx, RIGHT, buff=0.3)
        self.alla("devi dimostrare", GrowArrow(cx), FadeIn(t_no), run_time=0.5)
        sx = self.spunta(si).scale(1.3)
        sx.move_to([cx.get_x(), si.get_y(), 0])
        t_si = self.testo("puoi usarla", colore=AZZURRO).next_to(sx, RIGHT, buff=0.3)
        self.alla("Puoi dare per vera", FadeIn(si, shift=UP * 0.15), run_time=0.4)
        self.alla("ipotesi induttiva", Create(sx), FadeIn(t_si), run_time=0.5)

    # ------------------------------------------------------------------
    def seg_riepilogo(self, s):
        self.pulisci()
        righe = [("1", "passo base", "S(1)", VERDE, 0.82),
                 ("2", "passo induttivo", "forall n >= 1 quad S(n) -> S(n+1)", ACCENTO, 0.52)]
        fatti = []
        for num, nome, fo, colore, fy in righe:
            n = formula(num, 7, TENUE).move_to(self.punto(0.04, fy))
            t = self.testo(nome, colore=colore, peso=BOLD).move_to(self.punto(0.1, fy), aligned_edge=LEFT)
            f_ = formula(fo, 7.5).move_to(self.punto(0.4, fy), aligned_edge=LEFT)
            fatti.append((n, t, f_))
        n3 = formula("3", 7, TENUE).move_to(self.punto(0.04, 0.22))
        t3 = self.testo("dai per vera solo", colore=TESTO).move_to(self.punto(0.1, 0.22), aligned_edge=LEFT)
        t3b = self.testo("l'ipotesi induttiva", colore=AZZURRO, peso=BOLD).next_to(t3, RIGHT, buff=0.22)
        t3b.align_to(t3, DOWN)
        self.alla("Uno", FadeIn(fatti[0][0]), FadeIn(fatti[0][1], shift=RIGHT * 0.2), run_time=0.4)
        self.alla("vale per uno", Write(fatti[0][2]), run_time=0.6)
        self.alla("Due", FadeIn(fatti[1][0]), FadeIn(fatti[1][1], shift=RIGHT * 0.2), run_time=0.4)
        self.alla("Se l'enunciato", Write(fatti[1][2]), run_time=1.4)
        self.alla("Tre", FadeIn(n3), FadeIn(t3, shift=RIGHT * 0.2), n=2, run_time=0.4)
        self.alla("ipotesi induttiva", FadeIn(t3b), run_time=0.4)

    # ------------------------------------------------------------------
    def seg_verifica(self, s):
        self.pulisci()
        dom = self.testo("Dove abbiamo usato l'ipotesi induttiva?", peso=BOLD)
        dom.move_to(self.punto(0.5, 0.92))
        l1 = formula(r"S_(n+1) = S_n + (n+1)", 7)
        l2 = formula(r"= (n(n+1))/2 + (n+1)", 7)
        l3 = formula(r"= ((n+1)(n+2))/2", 7)
        l1.move_to(self.punto(0.3, 0.68), aligned_edge=LEFT)
        x_ug = l1[4].get_left()[0] if len(l1) > 4 else l1.get_center()[0]   # allinea gli «=»
        for i, l in enumerate((l2, l3)):
            l.move_to(self.punto(0.3, 0.42 - i * 0.26), aligned_edge=LEFT)
            l.shift(RIGHT * (x_ug - l.get_left()[0]))
        num = [formula(str(i + 1), 6, TENUE).move_to([self.punto(0.22, 0)[0], l.get_y(), 0])
               for i, l in enumerate((l1, l2, l3))]
        self.alla("Riguarda la dimostrazione", LaggedStart(*[FadeIn(VGroup(n, l), shift=UP * 0.15)
                                                               for n, l in zip(num, (l1, l2, l3))], lag_ratio=0.3),
                  run_time=1.4)
        self.alla("in quale passaggio", FadeIn(dom), run_time=0.4)
        riq = riquadro(VGroup(num[1], l2), AZZURRO, riempi=SFONDO)
        riq.set_fill(opacity=0)
        self.alla("Nel secondo", Create(riq), num[1].animate.set_color(AZZURRO), run_time=0.6)
        self.evidenzia(riq, num[1], l2, dom)
        self.fino_a("Per allenarti", anticipo=0.5)
        self.pulisci(run_time=0.3)
        tu = self.testo("prova tu, per induzione", colore=TENUE)
        es = formula(r"1 + 3 + dots.c + (2n - 1) = n^2", 8.5, ACCENTO)
        self.poni(es, 0.5, 0.45)
        tu.next_to(es, UP, buff=0.5)
        self.play(FadeIn(tu), run_time=0.3)
        self.alla("la somma dei primi", Write(es), run_time=2.0)
