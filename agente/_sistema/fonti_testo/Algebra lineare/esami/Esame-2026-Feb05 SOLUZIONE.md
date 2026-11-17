# Esame-2026-Feb05 SOLUZIONE

<!-- pagina 1 -->
Nome & Cognome:
Algebra Lineare, Esame Finale
5 Febbraio 2026
• Tutto il lavoro deve essere unicamente vostro.
• L’utilizzo di calcolatrici `e vietato.
• Ognuno pu`o portare un foglio protocollo o due fogli A4 (in totale 4 facciate A4)
con formulario, appunti del corso, ecc. scritto a mano.
• L’esame dura 2 ore.
• Scrivete il vostro nome su tutte le pagine, nel caso qualche foglio si staccasse.
• Controllate di avere tutte le 10 pagine dell’esame.
• Ogni domanda a risposta multipla vale 1 punto.
• Le risposte alle domande aperte valgono 11 punti l’una.
• Le domande aperte verranno corrette solo a chi totalizzi almeno 6 punti su 10
nella parte a crocette.
Buon Lavoro!
PER FAVORE MARCATE LE RISPOSTE CON UNA X, non un cerchio!
1.
(a)
(b)
(•)
(d)
(e)
2.
(a)
(b)
(•)
(d)
(e)
3.
(a)
(b)
(•)
(d)
(e)
4.
(a)
(b)
(c)
(d)
(•)
5.
(a)
(b)
(c)
(•)
(e)
6.
(a)
(•)
(c)
(d)
(e)
7.
(a)
(b)
(c)
(•)
(e)
8.
(a)
(b)
(c)
(•)
(e)
9.
(•)
(b)
(c)
(d)
(e)
10.
(a)
(b)
(•)
(d)
(e)
Non scrivere qua sotto!
Risp. Multiple
Risp. Aperte
Totale

<!-- pagina 2 -->
Nome & Cognome:
Risposta multipla
1.(1 pt.) Quale dei seguenti numeri complessi non `e soluzione di z2026 = −1?
(a)
−i.
(b)
eπi/2.
(c)
eπi/1013.
(d)
i.
(e)
eπi/2026.
Soluzione. Notiamo che 2026 = 2·1013. Ora, caso per caso: ricordando che (±i)2 = −1,
otteniamo (±i)2026 = (−1)1013 = −1, e la soluzione non `e n´e (a) n´e (d), e neanche (b)
visto che eπi/2 = i. Inoltre, (eπi/2026)2026 = eπi = −1, per cui la soluzione non `e nemmeno
(e). Inﬁne, (eπi/1013)2026 = (eπi)2 = (−1)2 = 1, dunque la risposta giusta `e (c).
2.(1 pt.) Quale dei seguenti insiemi non `e un sottospazio di R2[x]:
(a)
{p(x) ∈R2[x] ; p(1) = p(2)}.
(b)
Span(x + 1, x2 −1).
(c)
{x2 + tx ; t ∈R}.
(d)
{p(x) = ax2 + bx + c ; a + b −c = 0}.
(e)
R1[x]⊥.
Soluzione. Notiamo che l’insieme in (c) non `e uno spazio vettoriale, ad esempio perch´e
non contiene il polinomio nullo: tutti i polinomi in questo insieme, infatti, hanno il coef-
ﬁciente di x2 uguale a 1. La risposta giusta `e dunque la (c).
Sulle altre risposte: uno span di vettori (insieme (b)) `e sempre un sottospazio, cos`ı come
il complemento ortogonale di un sottospazio (insieme (e)). L’insieme in (d) `e deﬁnito da
un sistema lineare omogeneo, dunque anch’esso un sottospazio. Inoltre, ricordando che
per p(x) = ax2 +bx+c ∈R2[x], vale p(1) = a+b+c e p(2) = 4a+2b+c, anche l’insieme
in (a) si pu`o scrivere come sistema lineare omogeneo:
{p(x) = ax2 + bx + c ∈R2[x] | 0 = p(2) −p(1) = 3a + b}}
3.(1 pt.) Siano A, B ∈M(2, R) deﬁniti da
A =

2
0
2
6

,
B =

1
1
1
0

.
Allora la traccia di ABA `e uguale a:
(a)
44.
(b)
10.
(c)
20.
(d)
64.
(e)
26.
2

<!-- pagina 3 -->
Nome & Cognome:
Soluzione. Calcoliamo tr(ABA) = tr((AB)A):
tr

2
0
2
6
 
1
1
1
0
 
2
0
2
6

= tr

2
2
8
2
 
2
0
2
6

= tr

8
∗
∗
12

= 20.
4.(1 pt.) Determinare il rango della matrice




2
0
2
6
0
5
0
2
2
10
2
10
6
5
6
20




(a)
4.
(b)
0.
(c)
3.
(d)
1.
(e)
2.
Soluzione. Eﬀettuiamo Gauss, cominciando con il dividere per 2 le righe 1 e 3:




2
0
2
6
0
5
0
2
2
10
2
10
6
5
6
20



→




1
0
1
3
0
5
0
2
1
5
1
5
6
5
6
20



→




1
0
1
3
0
5
0
2
0
5
0
2
0
5
0
2



→




1
0
1
3
0
5
0
2
0
0
0
0
0
0
0
0




Essendoci due pivots, il rango di A `e 2.
5.(1 pt.) Sia
A =


2
0
2
6
−1
2
0
2
6

.
Il determinante di A3 `e:
(a)
27.
(b)
−1.
(c)
4.
(d)
64.
(e)
9.
Soluzione. Calcoliamo det A, iniziando con l’eﬀettuare una mossa di Gauss:
det


2
0
2
6
−1
2
0
2
6

= det


2
0
2
0
−1
−4
0
2
6

= 2 det

−1
−4
2
6

= 2(−6 + 8) = 4.
Inﬁne, per il teorema di Binet, det(A3) = det(A)3 = 43 = 64.
3

<!-- pagina 4 -->
Nome & Cognome:
6.(1 pt.) Date l’applicazione lineare T : R2 →R2, T

x
y

=

3x
x + 2y

, e la base
B =

v1 =

0
1

, v2 =

1
1

, allora il vettore di coordinate [T(v1)]B `e:
(a)

1
2

.
(b)

2
0

.
(c)

0
2

.
(d)

1
0

.
(e)

0
1

.
Soluzione. [T(v1)]B = t(a, b) dove Tv1 = av1 + bv2. Calcoliamo:
Tv1 =

0
2

= 2v1 = 2v1 + 0v2,
pertanto [T(v1)]B = t(2, 0). La risposta corretta `e (b).
7.(1 pt.) L’immagine dell’applicazione lineare T : R2[x] →R2[x], data da
T(ax2 + bx + c) = (a −b)x2 −cx + c,
`e:
(a)
R2[x].
(b)
Span(2 + x2, x)
(c)
R1[x]⊥.
(d)
Span(1 −x, x2)
(e)
{p(x) = ax2 + bx + c ∈R2[x] ; a −b = 0}.
Soluzione. Sia {1, x, x2} la base canonica del dominio. Ricordiamo allora che
Im(T) = Span(T(1), T(x), T(x2)) = Span(1 −x, −x2, x2) = Span(1 −x, x2).
8.(1 pt.) Trovare l’insieme degli autovalori del endomorﬁsmo T : R3 →R3, dato da
T


x
y
z

=


2x + y −2z
−x + 2z
3z

.
(a)
{1, 2, 3}.
(b)
{−1, ±2}.
(c)
{2, 3}.
(d)
{1, 3}.
(e)
{±1, 3}.
4

<!-- pagina 5 -->
Nome & Cognome:
Soluzione. La matrice associata a T rispetto alla base canonica B `e
[T]B
B =


2
1
−2
−1
0
2
0
0
3


Gli autovalori di T sono le radici del polinomio caratteristico
pT(t) = det


2 −t
1
−2
−1
−t
2
0
0
3 −t

= (3 −t) det

2 −t
1
−1
−t

= (3 −t)(t2 −2t + 1) = (3 −t)(t −1)2.
Dunque gli autovalori sono 3 e 1.
9.(1 pt.) L’endomorﬁsmo T : R2[x] →R2[x] dato da
T(ax2 + bx + c) = (a + b −c)x2 + (a + b + c)x + (a + 2b)
ha autovalore λ = 2. Qual `e l’autospazio che corrisponde a questo autovalore?
(a)
Span(x + 1).
(b)
Span(x2 −1, x + 1).
(c)
Span(x2 + 1, x −1).
(d)
Span(x2 + x).
(e)
Span(x2 −1).
Soluzione. L’autospazio che ci interessa `e V2 = ker(T −2I). Calcoliamo
V2 ={p(x) = ax2 + bx + c ∈R2[x] | T(p(x)) −2p(x) = 0}
={p(x) = ax2 + bx + c ∈R2[x] | (−a + b −c)x2 + (a −b + c)x + (a + 2b −2c) = 0}
=


ax2 + bx + c ∈R2[x]

−a + b −c = 0
a −b + c = 0
a + 2b −2c = 0



Risolviamo il sistema, che ci dar`a i coeﬃcienti dei polinomi in V2, applicando Gauss e
Gauss-Jordan alla matrice dei coeﬃcienti:


−1
1
−1
1
−1
1
1
2
−2

→


−1
1
−1
0
0
0
0
3
−3

→


−1
1
−1
0
1
−1
0
0
0

→


−1
0
0
0
1
−1
0
0
0


Da qui, il sistema che si ottiene `e a = 0, b = c per cui si ha:
V2 = {p(x) = bx + b = b(x + 1) | b ∈R} = Span(x + 1).
5

<!-- pagina 6 -->
Nome & Cognome:
10.(1 pt.) La distanza tra le due rette
r1 = t(1, 1, 1) + Span(t(0, 1, 2)),
r2 = t(2, 3, 4) + Span(t(2, 2, 2))
`e:
(a)
4.
(b)
√
2.
(c)
0.
(d)
2
√
3.
(e)
t(1, 4, 3).
Soluzione. Scriviamo r1 = P + Span(v), r2 = Q + Span(w). Calcoliamo:
det(Q −P|v|w) = det


1
0
1
2
1
1
3
2
1

= det


1
0
1
1
1
0
2
2
0

= 0.
Poich`e v, w sono linearmente indipendenti, ∥v × w∦ = 0 e pertanto
d(r1, r2) = det(Q −P|v|w)/∥v × w∥= 0.
Per veriﬁcare il risultato, si nota subito che le due rette sono incidenti (nel punto t(1, 2, 3)).
6

<!-- pagina 7 -->
Nome & Cognome:
Risposta aperta
Per ricevere punteggio parziale, dovete mostrare il vostro lavoro!
11.(11 pts.) Si consideri il seguente sistema lineare nelle incognite x, y, z, con un parametro
k ∈R:





x + 2y + kz
= 1,
−x + y −kz
= 2,
kx + ky + z
= k −1.
(1) Calcolare il determinante della matrice A dei coeﬃcienti.
(2) Al variare di k ∈R, discutere quante soluzioni ammette il sistema lineare.
(3) Per k = 1, trovare tutte le soluzioni.
(4) Per k = 2, trovare tutte le soluzioni.
Soluzione. 1) La matrice dei coeﬃcienti, con il suo determinante, sono dati da:
A =


1
2
k
−1
1
−k
k
k
1


⇒
det(A) = det


1
2
k
0
3
0
k
k
1

= 3 det

1
k
k
1

= 3(1 −k2)
dove nel primo passaggio del calcolo del determinante, abbiamo sostituito R2 con R1+R2.
2) Dal primo punto notiamo che det(A) = 0 per k = ±1. In particolare, per k̸ = ±1 la
matrice A `e invertibile, e il sistema ammette un’unica soluzione. Consideriamo allora i
due casi k = ±1 separatamente.
Per k = 1 la matrice completa (A|b) del sistema diventa:


1
2
1
1
−1
1
−1
2
1
1
1
0

→


1
2
1
1
0
3
0
3
0
−1
0
−1

→


1
2
1
1
0
1
0
1
0
0
0
0

→


1
0
1
−1
0
1
0
1
0
0
0
0


(L’ultimo passaggio non `e essenziale ora ma ci servir`a al punto (3)).
In questo caso
rk(A) = rk(A|b) = 2, n = 3 e ci sono inﬁnite soluzioni che dipendono da 3 −2 = 1
parametro.
Nel caso k = −1 il sistema invece diventa:
(A|b) =


1
2
−1
1
−1
1
1
2
−1
−1
1
−2

→


1
2
−1
1
0
3
0
3
0
1
0
−1

→


1
2
−1
1
0
1
0
1
0
0
0
−2


Pertanto rk(A) = 2̸ = 3 = rk(A|b) e il sistema non ha soluzioni.
7

<!-- pagina 8 -->
Nome & Cognome:
3) Per k = 1 abbiamo gi`a ridotto la matrice a scalini, da cui otteniamo
(A|b) =


1
0
1
−1
0
1
0
1
0
0
0
0

⇒



x = −z −1
y = 1
z = z
e allora tutte le soluzioni (x, y, z) sono della forma (−t −1, 1, t) per un parametro t ∈R.
4) Per k = 2 sappiamo che esiste una sola soluzione. Calcoliamo
(A|b) =


1
2
2
1
−1
1
−2
2
2
2
1
1

→


1
2
2
1
0
3
0
3
0
−2
−3
−1

→


1
2
2
1
0
1
0
1
0
−2
−3
−1


→


1
2
2
1
0
1
0
1
0
0
−3
1

→


1
2
2
1
0
1
0
1
0
0
1
−1/3

→


1
2
0
5/3
0
1
0
1
0
0
1
−1/3


→


1
0
0
−1/3
0
1
0
1
0
0
1
−1/3


da cui si ottiene x = −1/3, y = 1, z = −1/3.
8

<!-- pagina 9 -->
Nome & Cognome:
12.(11 pts.) Si consideri la matrice simmetrica
S =


2
k
0
k
2
k
0
k
2


dove k `e un parametro reale in [−1, 1], e sia gS il prodotto scalare associato a S.
(1) Calcolare la matrice [gS]B associata a gS, rispetto alla base
B =


u1 =


1
0
−1

, u2 =


1
√
2
1

, u3 =


1
−
√
2
1





(2) Determinare per quali valori di k i vettori
u1 + u2 −u3
e
u2 + u3
sono ortogonali rispetto a gS.
(3) Per k = 1, calcolare la proiezione ortogonale di v = t(3, 0, 1) sul piano Span(u1, u2)
rispetto a gS.
Soluzione. 1) Chiamiamo S′ = [gS]B. Sappiamo che per calcolare le entrate di [gS]B
bisogna calcolare gS(ui, uj) = tuiSuj. Calcoliamo
Su1 =


2
0
−2

,
Su2 =


2 +
√
2k
2k + 2
√
2
2 +
√
2k

,
Su3 =


2 −
√
2k
2k −2
√
2
2 −
√
2k


Da cui calcoliamo:
• S′
11 = tu1(Su1) = (1, 0, −1) · t(2, 0, −2) = 4
• S′
21 = tu2(Su1) = (1,
√
2, 1) · t(2, 0, −2) = 0.
• S′
31 = tu3(Su1) = (1, −
√
2, 1) · t(2, 0, −2) = 0.
• S′
22 = tu2(Su2) = (1,
√
2, 1) · t(2 +
√
2k, 2k + 2
√
2, 2 +
√
2k) = 8 + 4
√
2k.
• S′
32 = tu3(Su2) = (1, −
√
2, 1) · t(2 +
√
2k, 2k + 2
√
2, 2 +
√
2k) = 0.
• S′
33 = tu3(Su3) = (1, −
√
2, 1) · t(2 −
√
2k, 2k −2
√
2, 2 −
√
2k) = 8 −4
√
2k.
Pertanto abbiamo
S′ = [gS]B =


4
0
0
0
8 + 4
√
2k
0
0
0
8 −4
√
2k


2) Presentiamo tre possibilit`a di calcolare il prodotto scalare tra i due vettori dati. Il
primo modo usa [u1 + u2 −u3]B = t(1, 1, −1), e [u2 + u3]B = t(0, 1, 1). A questo punto, si
9

<!-- pagina 10 -->
Nome & Cognome:
trova
gS(u1 + u2 −u3, u2 + u3) = t[u1 + u2 −u3]B · [gS]B · [u2 + u3]B
= (1, 1, −1) · S′ · t(0, 1, 1)
= (1, 1, −1) · t(0, 8 + 4
√
2k, 8 −4
√
2k) = 8
√
2k.
La seconda possibilit`a usa la bilinearit`a del prodotto scalare e l’ortogonalit`a dei vettori
u1, u2, u3. Si calcola
gS(u1 + u2 −u3, u2 + u3) = gS(u2, u2) −gS(u3, u3)
= (8 + 4
√
2k) −(8 −4
√
2k)
= 8
√
2k.
Finalmente, il terzo modo usa la base canonica.
Calcoliamo prima u1 + u2 −u3 =
t(1, 2
√
2, −1) e u2 + u3 = t(2, 0, 2). A questo punto, concludiamo
gS(u1 + u2 −u3, u2 + u3) = (1, 2
√
2, −1) · S · t(2, 0, 2)
= (1, 2
√
2, −1) · (4, 4k, 4)
= 4 + 8
√
2k −4 = 8
√
2k.
In ogni caso, i due vettori sono ortogonali quando questo prodotto `e uguale a 0, ovvero
se e solo se k = 0.
3) Sia k = 1. Dal conto al punto 1, sappiamo che u1, u2 sono ortogonali tra loro, e quindi
formano una base ortogonale di W := Span(u1, u2). Pertanto:
prW(v) = pru1(v) + pru2(v) = gS(v, u1)
gS(u1, u1)u1 + gS(v, u2)
gS(u2, u2)u2 = v · (Su1)
S′
11
u1 + v · (Su2)
S′
22
u2
Calcoliamo
v · (Su1) = (3, 0, 1) · t(2, 0, −2) = 4,
v · (Su2) = (3, 0, 1) ·


2 +
√
2
2 + 2
√
2
2 +
√
2

= 8 + 4
√
2.
Otteniamo quindi
prW(v) = 4
4u1 + 8 + 4
√
2
8 + 4
√
2u2 = u1 + u2 =


2
√
2
0

.
10
