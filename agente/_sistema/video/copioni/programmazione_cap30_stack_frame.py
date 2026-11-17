# -*- coding: utf-8 -*-
"""Lo stack frame e il modello della chiamata di funzione (Programmazione, cap. 30). Formato (b), 16:9.

Fonte: _sistema/bozze/programmazione_cap30.md (il video segue il capitolo, non le slide 06B:
offset solo come positivi/negativi; a, b, c sono parametri che ricevono una copia).
Nel parlato: FP = «effe pi», SP = «esse pi», sumSquares = «sum squares», x y z r = «ics, ipsilon, zeta, erre».
    python fai_video.py copioni/programmazione_cap30_stack_frame.py [--prova]
"""
from videolib import *

C_FP, C_SP = ARANCIO, AZZURRO                 # registri
C_PAR, C_CTRL, C_LOC = VIOLA, TENUE, VERDE    # parametri e valore di ritorno / dati di controllo / variabili locali
C_FRAME = AZZURRO                             # un frame intero (esempio delle chiamate)

CODICE_1 = r"""
#include <stdio.h>
int square(int x) {
    return x * x;
}
int sumSquares(int a, int b) {
    return square(a) + square(b);
}
int main(void) {
    int res = sumSquares(2, 3);
    printf("Risultato: %d\n", res);
    return 0;
}
"""

# come nel capitolo, senza #include e righe vuote (per stare nelle 12 righe)
CODICE_2 = r"""
int sommaProdotto(int a, int b, int c) {
    int somma = a + b + c;
    int prodotto = a * b * c;
    int risultato = somma + prodotto;
    return risultato;
}
int main(void) {
    int x = 2, y = 3, z = 4;
    int r = sommaProdotto(x, y, z);
    printf("Risultato: %d\n", r);
}
"""


class StackFrame(ScenaBase):
    META = dict(materia="programmazione", slug="cap30_stack_frame",
                titolo="Lo stack frame e il modello della chiamata di funzione",
                formato="16:9", voce="it-IT-GiuseppeMultilingualNeural", velocita=-4,
                fonte="_sistema/bozze/programmazione_cap30.md")

    SEGMENTI = [
        Seg("aggancio", "La domanda",
            "Una funzione ne chiama un'altra, che ne chiama un'altra ancora. "
            "Come fa il programma a ricordare dove tornare, e dove sono le variabili di ciascuna? "
            "La risposta è lo stack frame. Vediamo come funziona."),
        Seg("problema", "Il problema: indirizzi fissi",
            "Parti dal problema. Nei primi compilatori ogni variabile stava a un indirizzo fisso. "
            "Così una funzione non poteva essere eseguita due volte insieme, per esempio in modo ricorsivo. "
            "Le due esecuzioni avrebbero usato le stesse celle. "
            "Una funzione così si dice non rientrante. "
            "La soluzione arriva alla fine degli anni cinquanta: lo stack. "
            "Nel 1958 Dijkstra ne formalizza l'uso, come meccanismo generale per la ricorsione."),
        Seg("frame", "Lo stack frame",
            "Ecco il modello che usa il corso. È una convenzione: le macchine reali possono fare diversamente, "
            "ma la logica è la stessa. "
            "Lo stack è una zona di memoria che cresce verso gli indirizzi più bassi: nel disegno, verso il basso. "
            "Ogni chiamata di funzione riserva una porzione di stack tutta sua. "
            "Questa porzione si chiama stack frame. "
            "Quando la funzione finisce, il suo stack frame viene rilasciato, e la memoria torna disponibile."),
        Seg("registri", "I registri FP e SP",
            "Due registri tengono il segno. Il primo è effe pi, il frame pointer. "
            "Indica l'inizio dello stack frame della funzione attiva, e resta fermo per tutta la chiamata. "
            "Il secondo è esse pi, lo stack pointer. Indica il limite corrente dello stack. "
            "Si sposta ogni volta che riservi o liberi spazio: per esempio quando nasce una variabile locale. "
            "Tra effe pi e esse pi ci sono le variabili locali della funzione attiva."),
        Seg("chiamate", "Esempio: le chiamate",
            "Segui un programma vero. Il main chiama sum squares con due e tre. "
            "E sum squares chiama square due volte: prima con due, poi con tre. "
            "All'inizio è attivo solo il main. Sullo stack c'è il suo stack frame: "
            "effe pi all'inizio, esse pi alla fine. "
            "Ora il main chiama sum squares. Si impila un nuovo stack frame, e i due registri scendono. "
            "Adesso la funzione attiva è sum squares, e il main è sospeso. "
            "Poi sum squares chiama square con due. Arriva il terzo stack frame. "
            "Prima di guardare: dove punta effe pi adesso? [pausa 2.5] "
            "All'inizio del frame di square, perché ora la funzione attiva è square. "
            "Le altre due sono sospese: aspettano di riprendere."),
        Seg("ritorni", "Esempio: i ritorni",
            "Square calcola due per due e restituisce quattro. "
            "Il suo stack frame viene rilasciato, e torna attiva sum squares. "
            "Seconda chiamata a square, questa volta con tre. "
            "Guarda bene: il nuovo frame occupa la stessa zona di prima. "
            "Non c'è conflitto, perché il primo era già stato rilasciato. "
            "Square restituisce nove, e anche questo frame viene rilasciato. "
            "Sum squares somma quattro e nove, e restituisce tredici. Poi viene rilasciato anche il suo frame. "
            "Resta il main, come all'inizio: in res c'è tredici."),
        Seg("offset", "Trovare i dati: gli offset da FP",
            "Come fa una funzione a trovare i suoi dati? Usa effe pi come punto fermo. "
            "Effe pi non si muove durante la chiamata. "
            "Quindi ogni dato sta a una distanza costante da effe pi: questa distanza si chiama offset. "
            "A offset positivi, cioè sopra effe pi, trovi i parametri e il valore di ritorno. "
            "A offset negativi, cioè sotto effe pi, trovi le variabili locali. "
            "Vicino a effe pi ci sono anche i dati di controllo: il vecchio effe pi e l'indirizzo di ritorno. "
            "Servono per tornare al chiamante. "
            "E perché non usare esse pi come riferimento? Perché esse pi si sposta mentre la funzione lavora."),
        Seg("completo", "Esempio: parametri, ritorno, variabili",
            "Ora un esempio completo. Il main ha tre variabili: ics, ipsilon e zeta. Valgono due, tre e quattro. "
            "Poi chiama somma prodotto. "
            "Sullo stack si riserva una cella per il valore di ritorno: finirà nella variabile erre. "
            "Poi arrivano i parametri a, bi e ci, con una copia di due, tre e quattro. "
            "Poi i dati di controllo. Qui si ferma effe pi. "
            "Sotto effe pi nascono le variabili locali, una alla volta. Somma vale nove. "
            "Quanto vale prodotto? [pausa 2.2] Due per tre per quattro: ventiquattro. "
            "E risultato vale trentatré. "
            "A ogni nuova variabile esse pi è sceso. Effe pi invece è rimasto fermo."),
        Seg("errore", "Due errori tipici",
            "Un errore tipico: pensare che a, bi e ci siano le stesse celle di ics, ipsilon e zeta. "
            "Non lo sono. Sono celle diverse, che contengono una copia dei valori. "
            "Se somma prodotto cambiasse a, ics resterebbe due. "
            "Secondo errore: confondere i due registri. Esse pi si sposta, effe pi resta fermo."),
        Seg("riepilogo", "Riepilogo",
            "Riassumendo, in tre punti. Uno: ogni chiamata ha il suo stack frame. "
            "Nasce con la chiamata e viene rilasciato al ritorno. "
            "Due: effe pi indica l'inizio dello stack frame attivo e resta fermo. "
            "Esse pi indica il limite dello stack e si sposta. "
            "Tre: rispetto a effe pi, i parametri stanno a offset positivi, le variabili locali a offset negativi."),
        Seg("verifica", "Tocca a te",
            "Ora tocca a te. Mentre è in esecuzione square, quanti stack frame ci sono sullo stack? "
            "E quale funzione è attiva? [pausa 3] "
            "Sono tre: main, sum squares e square. È attiva square, le altre due sono sospese. "
            "Seconda domanda. La variabile somma, di somma prodotto, sta a un offset positivo o negativo rispetto a effe pi? "
            "[pausa 2.5] Negativo: è una variabile locale, quindi sta sotto effe pi.", pausa_dopo=1.5),
    ]

    # ---- attrezzi locali --------------------------------------------------
    def nuova_pila(self, fx, larg=2.8, posti=8, hp=0.62, indirizzi=True, lung=0.85, pct=None):
        p = Pila(larg=larg, posti=posti, alt_posto=hp, pct=pct)
        p.move_to(self.punto(fx, 0.5))
        p.lung = lung
        if indirizzi:
            p.alti = etichetta("indirizzi alti", colore=TENUE).next_to(p.guida, UP, buff=0.12)
            p.bassi = etichetta("indirizzi bassi", colore=TENUE).next_to(p.guida, DOWN, buff=0.12)
            p.add(p.alti, p.bassi)
        return p

    def registri(self, p, fp=None, sp=None):
        """Crea FP (a sinistra) e SP (a destra) sui confini indicati."""
        f = p.puntatore("FP", C_FP, LEFT, fp, lung=p.lung)
        s = p.puntatore("SP", C_SP, RIGHT, sp, lung=p.lung)
        return f, s

    # ------------------------------------------------------------------
    def seg_aggancio(self, s):
        nomi = ["main", "sumSquares", "square"]
        box = VGroup()
        for n in nomi:
            t = etichetta(n, F["corpo"], TESTO, NORMAL, MONO)
            r = riquadro(t, AZZURRO, margine=0.3)
            box.add(VGroup(r, t))
        box.arrange(RIGHT, buff=1.6)
        self.poni(box, 0.5, 0.66)
        fr = [Arrow(box[i].get_right(), box[i + 1].get_left(), buff=0.12, color=TESTO, stroke_width=5) for i in range(2)]
        self.play(FadeIn(box[0]), run_time=0.4)
        self.alla("ne chiama un'altra", GrowArrow(fr[0]), FadeIn(box[1]), run_time=0.5)
        self.alla("un'altra ancora", GrowArrow(fr[1]), FadeIn(box[2]), run_time=0.5)
        rit = [CurvedArrow(box[i + 1].get_bottom() + DOWN * 0.1, box[i].get_bottom() + DOWN * 0.1, angle=-1.1,
                           color=ACCENTO, stroke_width=5, tip_length=0.22) for i in (1, 0)]
        dom = self.testo("dove tornare?", colore=ACCENTO)
        dom.next_to(VGroup(*rit), DOWN, buff=0.25)
        self.alla("dove tornare", Create(rit[0]), Create(rit[1]), FadeIn(dom), run_time=0.8)
        dom2 = self.testo("dove sono le variabili?", colore=ACCENTO)
        dom2.next_to(dom, DOWN, buff=0.25)
        self.alla("dove sono le variabili", FadeIn(dom2, shift=UP * 0.15), run_time=0.4)
        nome = self.testo("stack frame", 7.5, ACCENTO, BOLD)
        self.fino_a("La risposta", anticipo=0.2)
        self.play(FadeOut(dom), FadeOut(dom2), run_time=0.3)
        nome.move_to(dom.get_center() + DOWN * 0.3)
        self.alla("stack frame", Write(nome), run_time=0.8)

    # ------------------------------------------------------------------
    def seg_problema(self, s):
        self.pulisci()
        mem = Caselle(["", "", "x", "", "", ""], indici=False, colore=TENUE)
        self.poni(mem, 0.5, 0.42)
        em = etichetta("memoria: indirizzi fissi", colore=TENUE).next_to(mem, DOWN, buff=0.25)
        self.alla("ogni variabile", FadeIn(mem), FadeIn(em), run_time=0.5)
        cx = mem.cella(2)
        self.play(cx.animate.set_stroke(AZZURRO).set_fill(AZZURRO, 0.25), run_time=0.3)
        e1 = self.testo("esecuzione 1", colore=TESTO)
        e2 = self.testo("esecuzione 2", colore=TESTO)
        e1.move_to(self.punto(0.3, 0.84))
        e2.move_to(self.punto(0.7, 0.84))
        a1 = Arrow(e1.get_bottom(), cx.get_top() + LEFT * 0.15, buff=0.12, color=TESTO, stroke_width=5)
        a2 = Arrow(e2.get_bottom(), cx.get_top() + RIGHT * 0.15, buff=0.12, color=TESTO, stroke_width=5)
        self.alla("due volte insieme", FadeIn(e1), GrowArrow(a1), run_time=0.5)
        self.play(FadeIn(e2), GrowArrow(a2), run_time=0.5)
        self.alla("le stesse celle", cx.animate.set_stroke(ROSSO).set_fill(ROSSO, 0.35),
                  a1.animate.set_color(ROSSO), a2.animate.set_color(ROSSO), run_time=0.5)
        nr = self.testo("non rientrante", 6.5, ROSSO, BOLD)
        self.poni(nr, 0.5, 0.08)
        self.alla("non rientrante", Write(nr), run_time=0.8)
        self.fino_a("La soluzione", anticipo=0.3)
        self.pulisci(run_time=0.3)
        st = self.testo("stack", 9, ACCENTO, BOLD)
        self.poni(st, 0.5, 0.6)
        self.alla("lo stack", Write(st), run_time=0.6)
        anno = self.testo("1958 · Dijkstra: lo stack per la ricorsione", colore=TENUE)
        anno.next_to(st, DOWN, buff=0.6)
        self.alla("Nel 1958", FadeIn(anno, shift=UP * 0.15), run_time=0.5)

    # ------------------------------------------------------------------
    def seg_frame(self, s):
        self.pulisci()
        p = self.nuova_pila(0.62, larg=3.6, posti=7, hp=0.66, pct=4.3)
        conv = self.testo("modello del corso", colore=TENUE)
        conv.move_to(self.punto(0.02, 0.85), aligned_edge=LEFT)
        conv2 = self.testo("(una convenzione)", colore=TENUE)
        conv2.next_to(conv, DOWN, buff=0.2, aligned_edge=LEFT)
        self.alla("che usa il corso", FadeIn(conv), FadeIn(p.guida), run_time=0.5)
        self.alla("una convenzione", FadeIn(conv2), run_time=0.4)
        self.alla("Lo stack è una zona", FadeIn(p.alti), FadeIn(p.bassi), run_time=0.4)
        x = p.guida.get_right()[0] + 0.5
        cresce = Arrow([x, p.guida.get_top()[1] - 0.2, 0], [x, p.guida.get_bottom()[1] + 0.2, 0], buff=0,
                       color=ACCENTO, stroke_width=5, max_tip_length_to_length_ratio=0.06)
        ec = etichetta("cresce", colore=ACCENTO, peso=BOLD).next_to(cresce, RIGHT, buff=0.15)
        self.alla("cresce verso", GrowArrow(cresce), FadeIn(ec), run_time=0.9)
        self.add(p)
        self.alla("Ogni chiamata", p.push("main", colore=C_FRAME, alt=2), run_time=0.5)
        self.alla("tutta sua", p.push("f", colore=C_FRAME, alt=2, mostra="funzione chiamata"), run_time=0.5)
        gr = Brace(p.cella("f"), LEFT, buff=0.15, color=ACCENTO)
        nome = self.testo("stack frame", 6, ACCENTO, BOLD).next_to(gr, LEFT, buff=0.2)
        self.alla("si chiama stack frame", GrowFromCenter(gr), Write(nome), run_time=0.7)
        self.fino_a("viene rilasciato", anticipo=0.2)
        self.play(p.pop(), FadeOut(gr), nome.animate.set_opacity(OPACITA_SFONDO), run_time=0.6)
        lib = etichetta("libero", colore=TENUE).move_to([p.guida.get_center()[0], p.y_livello(1) - p.hp, 0])
        self.alla("torna disponibile", FadeIn(lib), run_time=0.4)
        self.pila = p
        self.via = VGroup(conv, conv2, nome, lib, cresce, ec)

    def seg_registri(self, s):
        p = self.pila
        self.play(FadeOut(self.via), p.attiva(), run_time=0.4)
        r1 = VGroup(etichetta("FP", F["corpo"], C_FP, BOLD, MONO), self.testo("frame pointer", colore=C_FP)).arrange(RIGHT, buff=0.3)
        r1b = self.testo("inizio del frame: fermo", colore=TESTO)
        r2 = VGroup(etichetta("SP", F["corpo"], C_SP, BOLD, MONO), self.testo("stack pointer", colore=C_SP)).arrange(RIGHT, buff=0.3)
        r2b = self.testo("limite dello stack: mobile", colore=TESTO)
        r1.move_to(self.punto(0.0, 0.86), aligned_edge=LEFT)
        r1b.next_to(r1, DOWN, buff=0.2, aligned_edge=LEFT)
        r2.move_to(self.punto(0.0, 0.42), aligned_edge=LEFT)
        r2b.next_to(r2, DOWN, buff=0.2, aligned_edge=LEFT)
        fp, sp = self.registri(p, 1, 1)
        sosp = etichetta("sospesa", colore=TENUE)
        sosp.move_to([p.guida.get_right()[0] + 0.25, p.cella("main").get_center()[1], 0], aligned_edge=LEFT)
        att = etichetta("funzione attiva", colore=C_LOC)
        att.move_to([p.guida.get_center()[0], p.y_livello(1) - p.hp * 2.6, 0])
        self.alla("effe pi", FadeIn(r1, shift=RIGHT * 0.2), FadeIn(fp), FadeIn(sosp), run_time=0.5)
        self.alla("l'inizio dello stack frame", FadeIn(r1b), FadeIn(att), run_time=0.4)
        self.alla("esse pi", FadeIn(r2, shift=RIGHT * 0.2), FadeIn(sp), run_time=0.5)
        self.alla("il limite corrente", FadeIn(r2b), run_time=0.3)
        self.alla("riservi", p.push("i", 0, colore=C_LOC), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.4)
        self.alla("liberi", p.pop(), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.4)
        self.alla("nasce una variabile", p.push("i", 0, colore=C_LOC), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.4)
        self.play(p.push("s", 0, colore=C_LOC), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.4)
        loc = VGroup(p.cella("i"), p.cella("s"))
        gr = Brace(loc, RIGHT, buff=0.15, color=C_LOC)
        el = etichetta("variabili locali", colore=C_LOC).next_to(gr, RIGHT, buff=0.15)
        self.alla("Tra effe pi", GrowFromCenter(gr), FadeIn(el), run_time=0.6)

    # ------------------------------------------------------------------
    def seg_chiamate(self, s):
        self.pulisci()
        c = self.codice(CODICE_1, pct=3.8)
        c.move_to(self.punto(0, 1), aligned_edge=UL)
        p = self.nuova_pila(0.785, larg=3.0, posti=7, hp=0.66, pct=4.0)
        self.play(FadeIn(c), FadeIn(p), run_time=0.5)
        self.alla("Il main chiama", c.riga(9), run_time=0.4)
        self.alla("E sum squares chiama", c.riga(6), run_time=0.4)
        self.alla("All'inizio è attivo", c.riga(8), p.push("main", colore=C_FRAME, alt=2, peso=BOLD), run_time=0.5)
        fp, sp = self.registri(p, 0, 1)
        self.alla("effe pi all'inizio", FadeIn(fp), run_time=0.4)
        self.alla("esse pi alla fine", FadeIn(sp), run_time=0.4)
        self.alla("Ora il main chiama", c.riga(9), run_time=0.4)
        self.alla("Si impila", p.push("sumSquares", colore=C_FRAME, alt=2), run_time=0.5)
        self.alla("i due registri scendono", p.sposta("FP", 1), p.sposta("SP"), run_time=0.6)
        self.alla("Adesso la funzione attiva", p.attiva("sumSquares"), c.riga(6), run_time=0.5)
        self.alla("Poi sum squares chiama", Indicate(c.barra, color=ACCENTO, scale_factor=1.03), run_time=0.5)
        self.alla("Arriva il terzo", p.push("square", colore=C_FRAME, alt=2, mostra="square(2)"), run_time=0.5)
        dom = self.testo("dove punta FP adesso?", colore=ACCENTO, peso=BOLD)
        dom.next_to(c, DOWN, buff=0.3)
        self.alla("dove punta", FadeIn(dom, shift=UP * 0.15), run_time=0.4)
        self.alla("All'inizio del frame", p.sposta("FP", 2), p.sposta("SP"), run_time=0.7)
        self.alla("ora la funzione attiva", p.attiva("square"), c.riga(3), FadeOut(dom), run_time=0.5)
        e1 = etichetta("sospesa", colore=TENUE)
        e2 = etichetta("sospesa", colore=TENUE)
        x = p.guida.get_right()[0] + 0.25
        e1.move_to([x, p.cella("main").get_center()[1], 0], aligned_edge=LEFT)
        e2.move_to([x, p.cella("sumSquares").get_center()[1], 0], aligned_edge=LEFT)
        self.alla("sono sospese", FadeIn(e1), FadeIn(e2), run_time=0.4)
        self.cod, self.pila, self.sosp = c, p, (e1, e2)

    def seg_ritorni(self, s):
        c, p = self.cod, self.pila
        e1, e2 = self.sosp

        def ritorno(nome, v):
            t = etichetta(f"restituisce {v}", colore=VERDE, peso=BOLD)
            t.next_to(p.cella(nome), LEFT, buff=0.25)
            return t

        self.alla("restituisce quattro", p.imposta("square", 4, colore=VERDE), run_time=0.4)
        self.alla("viene rilasciato", p.pop(), FadeOut(e2), run_time=0.5)
        self.play(p.sposta("FP", 1), p.sposta("SP"), p.attiva("sumSquares"), c.riga(6), run_time=0.5)
        self.alla("Seconda chiamata", p.push("square", colore=C_FRAME, alt=2, mostra="square(3)"), FadeIn(e2), run_time=0.5)
        self.play(p.sposta("FP", 2), p.sposta("SP"), p.attiva("square"), c.riga(3), run_time=0.5)
        box = p.cella("square")[0]
        segno = DashedVMobject(Rectangle(width=box.width + 0.16, height=box.height + 0.16).move_to(box), num_dashes=40)
        segno.set_stroke(ACCENTO, 4)
        ez = self.testo("stessa zona di prima", colore=ACCENTO, peso=BOLD)
        ez.next_to(c, DOWN, buff=0.3)
        self.alla("la stessa zona", Create(segno), FadeIn(ez), run_time=0.7)
        self.alla("Square restituisce nove", FadeOut(segno), FadeOut(ez), run_time=0.3)
        self.play(p.imposta("square", 9, colore=VERDE), run_time=0.3)
        self.alla("anche questo frame", p.pop(), FadeOut(e2), run_time=0.5)
        self.play(p.sposta("FP", 1), p.sposta("SP"), p.attiva("sumSquares"), c.riga(6), run_time=0.5)
        self.alla("restituisce tredici", p.imposta("sumSquares", 13, colore=VERDE), run_time=0.4)
        self.alla("viene rilasciato anche il suo", p.pop(), FadeOut(e1), run_time=0.5)
        self.play(p.sposta("FP", 0), p.sposta("SP"), p.attiva("main"), c.riga(9), run_time=0.5)
        res = etichetta("res = 13", colore=VERDE, peso=BOLD, font=MONO)
        m = p.celle[0]
        res.move_to(m["box"].get_center() + DOWN * 0.28)
        self.alla("in res", m["testo"].animate.shift(UP * 0.28), FadeIn(res), run_time=0.5)

    # ------------------------------------------------------------------
    def seg_offset(self, s):
        self.pulisci()
        p = self.nuova_pila(0.5, larg=4.4, posti=6, hp=0.8, indirizzi=False, lung=1.0, pct=4.3)
        self.add(p)
        for an in (p.push("chiamante", colore=TENUE, mostra="… chiamante …"),
                   p.push("ritorno", colore=C_PAR, mostra="valore di ritorno"),
                   p.push("parametri", colore=C_PAR),
                   p.push("controllo", colore=C_CTRL, mostra="dati di controllo"),
                   p.push("locali", colore=C_LOC, alt=2, mostra="variabili locali")):
            pass
        fp, sp = self.registri(p, 4, 5)
        self.remove(p)
        self.play(FadeIn(p), run_time=0.6)
        self.alla("punto fermo", Indicate(fp, color=C_FP, scale_factor=1.15), run_time=0.7)
        off = self.testo("offset", 6.5, ACCENTO, BOLD)
        off2 = self.testo("distanza da FP", colore=TENUE)
        off.move_to(self.punto(0.0, 0.86), aligned_edge=LEFT)
        off2.next_to(off, DOWN, buff=0.2, aligned_edge=LEFT)
        self.alla("distanza costante", FadeIn(off2), run_time=0.4)
        self.alla("si chiama offset", Write(off), run_time=0.6)
        x = p.guida.get_right()[0] + 0.45
        y_fp = p.y_livello(4)
        su = Arrow([x, y_fp + 0.08, 0], [x, p.y_livello(1) - 0.1, 0], buff=0, color=C_PAR, stroke_width=5,
                   max_tip_length_to_length_ratio=0.12)
        giu = Arrow([x, y_fp - 0.08, 0], [x, p.y_livello(5) + 0.45, 0], buff=0, color=C_LOC, stroke_width=5,
                    max_tip_length_to_length_ratio=0.2)
        e_su = etichetta("offset positivi", colore=C_PAR, peso=BOLD).next_to(su, RIGHT, buff=0.15)
        e_giu = etichetta("offset negativi", colore=C_LOC, peso=BOLD).next_to(giu, RIGHT, buff=0.15)
        self.alla("A offset positivi", GrowArrow(su), FadeIn(e_su), run_time=0.6)
        self.evidenzia(p.cella("ritorno"), p.cella("parametri"), su, e_su, fp, off, off2, run_time=0.3)
        self.fino_a("A offset negativi", anticipo=0.15)
        self.ripristina(run_time=0.2)
        self.play(GrowArrow(giu), FadeIn(e_giu), run_time=0.5)
        self.evidenzia(p.cella("locali"), giu, e_giu, fp, off, off2, run_time=0.3)
        self.fino_a("i dati di controllo", anticipo=0.3)
        self.ripristina(run_time=0.2)
        self.evidenzia(p.cella("controllo"), fp, off, off2, run_time=0.3)
        ec = VGroup(etichetta("vecchio FP,", colore=TESTO), etichetta("indirizzo di ritorno", colore=TESTO))
        ec.arrange(DOWN, buff=0.1, aligned_edge=RIGHT)
        ec.move_to([p.guida.get_left()[0] - 0.3, p.cella("controllo").get_center()[1] + 0.45, 0], aligned_edge=RIGHT)
        self.alla("il vecchio effe pi", FadeIn(ec), run_time=0.5)
        self.fino_a("E perché non usare", anticipo=0.3)
        self.ripristina(run_time=0.3)
        self.play(FadeOut(ec), FadeOut(su), FadeOut(e_su), FadeOut(giu), FadeOut(e_giu), run_time=0.3)
        self.alla("esse pi come riferimento", Indicate(sp, color=C_SP, scale_factor=1.15), run_time=0.7)
        self.alla("si sposta", sp.animate.shift(UP * 0.8), run_time=0.5)
        self.play(sp.animate.shift(DOWN * 0.8), run_time=0.5)

    # ------------------------------------------------------------------
    def seg_completo(self, s):
        self.pulisci()
        c = self.codice(CODICE_2, pct=3.6)
        c.move_to(self.punto(0, 1), aligned_edge=UL)
        p = self.nuova_pila(0.8, larg=3.0, posti=11, hp=0.52, indirizzi=False, lung=0.5)
        self.play(FadeIn(c), FadeIn(p), run_time=0.5)
        self.alla("tre variabili", c.riga(8), run_time=0.4)
        fp, sp = self.registri(p, 0, 0)
        self.play(FadeIn(fp), FadeIn(sp), run_time=0.3)
        for nome, v, quando in (("x", 2, "ics"), ("y", 3, "ipsilon"), ("z", 4, "zeta")):
            self.alla(quando, p.push(nome, v, colore=C_LOC), run_time=0.3)
            self.play(p.sposta("SP"), run_time=0.25)
        self.alla("Poi chiama", c.riga(9), run_time=0.4)
        self.alla("una cella per il valore", p.push("ritorno", colore=C_PAR, mostra="r (ritorno)"), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.3)
        self.fino_a("i parametri", anticipo=0.15)
        for nome, v in (("a", 2), ("b", 3), ("c", 4)):
            self.play(p.push(nome, v, colore=C_PAR), run_time=0.35)
            self.play(p.sposta("SP"), run_time=0.25)
        self.alla("i dati di controllo", p.push("controllo", colore=C_CTRL, mostra="dati di controllo"), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.3)
        self.alla("Qui si ferma", p.sposta("FP", 8), c.riga(1), run_time=0.7)
        self.alla("Somma vale", c.riga(2), p.push("somma", 9, colore=C_LOC), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.3)
        self.alla("Quanto vale prodotto", c.riga(3), p.push("prodotto", "?", colore=C_LOC), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.3)
        self.alla("ventiquattro", p.imposta("prodotto", 24), run_time=0.4)
        self.alla("E risultato vale", c.riga(4), p.push("risultato", 33, colore=C_LOC), run_time=0.4)
        self.play(p.sposta("SP"), run_time=0.3)
        self.alla("esse pi è sceso", Indicate(sp, color=C_SP, scale_factor=1.2), run_time=0.7)
        self.alla("è rimasto fermo", Indicate(fp, color=C_FP, scale_factor=1.2), run_time=0.7)
        self.cod, self.pila = c, p

    def seg_errore(self, s):
        c, p = self.cod, self.pila
        fp, sp = p.punt["FP"], p.punt["SP"]
        e1 = self.testo("a, b, c ≠ x, y, z", colore=ROSSO, peso=BOLD, font=MONO)
        e1.next_to(c, DOWN, buff=0.45, aligned_edge=LEFT)
        abc = [p.cella(n) for n in "abc"]
        xyz = [p.cella(n) for n in "xyz"]
        self.alla("le stesse celle", FadeIn(e1, shift=UP * 0.15), run_time=0.4)
        self.evidenzia(*abc, *xyz, e1, run_time=0.4)
        x = p.guida.get_left()[0] - 0.1
        arco = CurvedArrow([x, xyz[0].get_center()[1], 0], [x, abc[0].get_center()[1], 0], angle=1.4,
                           color=ACCENTO, stroke_width=4, tip_length=0.18)
        ecopia = etichetta("copia", colore=ACCENTO, peso=BOLD).next_to(arco, LEFT, buff=0.1)
        self.alla("una copia dei valori", Create(arco), FadeIn(ecopia), run_time=0.6)
        self.alla("cambiasse a", p.imposta("a", 7), run_time=0.4)
        self.alla("ics resterebbe due", Indicate(xyz[0], color=VERDE, scale_factor=1.08), run_time=0.7)
        self.fino_a("Secondo errore", anticipo=0.4)
        self.play(FadeOut(arco), FadeOut(ecopia), FadeOut(e1), p.imposta("a", 2, colore=TESTO), run_time=0.3)
        self.ripristina(run_time=0.3)
        e2 = self.testo("SP si sposta, FP resta fermo", colore=ROSSO, peso=BOLD)
        e2.next_to(c, DOWN, buff=0.45, aligned_edge=LEFT)
        self.alla("confondere", FadeIn(e2, shift=UP * 0.15), run_time=0.4)
        self.alla("Esse pi si sposta", Indicate(sp, color=C_SP, scale_factor=1.2), run_time=0.7)
        self.alla("effe pi resta fermo", Indicate(fp, color=C_FP, scale_factor=1.2), run_time=0.7)

    # ------------------------------------------------------------------
    def seg_riepilogo(self, s):
        self.pulisci()
        ys = (0.82, 0.5, 0.18)
        num = [formula(str(i + 1), 7, TENUE).move_to(self.punto(0.08, y)) for i, y in enumerate(ys)]
        t1 = self.testo("ogni chiamata, uno", colore=TESTO)
        t1b = self.testo("stack frame", colore=ACCENTO, peso=BOLD)
        r1 = VGroup(t1, t1b).arrange(RIGHT, buff=0.22, aligned_edge=DOWN)
        r2 = VGroup(etichetta("FP", F["corpo"], C_FP, BOLD, MONO), self.testo("resta fermo,"),
                    etichetta("SP", F["corpo"], C_SP, BOLD, MONO), self.testo("si sposta")).arrange(RIGHT, buff=0.25)
        r3 = VGroup(self.testo("parametri", colore=C_PAR, peso=BOLD), etichetta("offset +", F["corpo"], C_PAR, NORMAL, MONO),
                    self.testo("locali", colore=C_LOC, peso=BOLD), etichetta("offset −", F["corpo"], C_LOC, NORMAL, MONO))
        r3.arrange(RIGHT, buff=0.3)
        r3[2].shift(RIGHT * 0.5)
        r3[3].shift(RIGHT * 0.5)
        for r, y in zip((r1, r2, r3), ys):
            r.move_to(self.punto(0.16, y), aligned_edge=LEFT)
        self.alla("Uno", FadeIn(num[0]), FadeIn(r1, shift=RIGHT * 0.2), run_time=0.5)
        self.alla("Due", FadeIn(num[1]), FadeIn(r2[:2], shift=RIGHT * 0.2), run_time=0.5)
        self.alla("Esse pi indica", FadeIn(r2[2:], shift=RIGHT * 0.2), run_time=0.5)
        self.alla("Tre", FadeIn(num[2]), n=2, run_time=0.3)
        self.alla("i parametri stanno", FadeIn(r3[:2], shift=RIGHT * 0.2), run_time=0.5)
        self.alla("le variabili locali", FadeIn(r3[2:], shift=RIGHT * 0.2), run_time=0.5)

    # ------------------------------------------------------------------
    def seg_verifica(self, s):
        self.pulisci()
        d1 = self.testo("Durante square: quanti stack frame?", peso=BOLD)
        d1b = self.testo("Quale funzione è attiva?", peso=BOLD)
        d1.move_to(self.punto(0.0, 0.9), aligned_edge=LEFT)
        d1b.next_to(d1, DOWN, buff=0.25, aligned_edge=LEFT)
        self.alla("quanti stack frame", FadeIn(d1), run_time=0.4)
        self.alla("E quale funzione", FadeIn(d1b), run_time=0.4)
        p = self.nuova_pila(0.7, larg=3.0, posti=6, hp=0.62, indirizzi=False, pct=4.3)
        p.shift(DOWN * 0.5)
        self.fino_a("Sono tre", anticipo=0.2)
        self.play(FadeIn(p), run_time=0.2)
        for nome, quando in (("main", "main"), ("sumSquares", "sum squares"), ("square", "square")):
            self.alla(quando, p.push(nome, colore=C_FRAME, alt=2), n=2 if nome == "square" else 1, run_time=0.35)
        fp, sp = self.registri(p, 2, 3)
        self.alla("È attiva square", p.attiva("square"), FadeIn(fp), FadeIn(sp), run_time=0.5)
        self.fino_a("Seconda domanda", anticipo=0.4)
        self.pulisci(run_time=0.3)
        d2 = self.testo("somma: offset positivo o negativo?", peso=BOLD)
        d2.move_to(self.punto(0.5, 0.75))
        self.alla("La variabile somma", FadeIn(d2), run_time=0.4)
        r2 = self.testo("negativo: è una variabile locale", colore=C_LOC, peso=BOLD)
        r2.move_to(self.punto(0.5, 0.45))
        r2b = etichetta("sta sotto FP", F["corpo"], TENUE)
        r2b.next_to(r2, DOWN, buff=0.3)
        self.alla("Negativo", FadeIn(r2, shift=UP * 0.15), run_time=0.4)
        self.alla("quindi sta sotto", FadeIn(r2b), run_time=0.4)
