# Esame-2025-Feb07-SOLUZIONE

<!-- pagina 1 -->
Nome & Cognome:
Algebra Lineare, Esame Finale
Febbraio 7, 2025
• Tutto il lavoro deve essere unicamente vostro.
• L’utilizzo di calcolatrici `e vietato.
• Ognuno pu`o portare un foglio protocollo o due fogli A4 (in totale 4 facciate A4)
con formulario, appunti del corso, ecc. scritto a mano.
• L’esame dura 2 ore.
• Scrivete il vostro nome su tutte le pagine, nel caso qualche foglio si staccasse.
• Controllate di avere tutte le 9 pagine dell’esame.
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
(c)
(d)
(•)
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
(•)
(e)
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
(•)
(b)
(c)
(d)
(e)
8.
(a)
(b)
(c)
(d)
(•)
9.
(a)
(b)
(c)
(•)
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
1.(1 pt.) Dato z =
√
2
2 (1 −i), allora z2025 `e uguale a:
(a)
2025(1 + i).
(b)
22025(1 −i).
(c)
√
2
2 (1 −i).
(d)
1 + i.
(e)
1.
Soluzione. In coordinate polari z = e−π
4 i per cui z2025 = e−2025π
4
i. Poich´e −2025π
4
=
−π
4 −2π·(253), l’angolo −2025π
4
`e uguale all’angolo −π
4 per cui z2025 = e−π
4 = z =
√
2
2 (1−i).
2.(1 pt.) Identificate la risposta corretta alla domanda “C ammette una struttura di
spazio vettoriale su R?”:
(a)
No, poich´e C `e gi`a uno spazio vettoriale su C stesso.
(b)
Si, perch´e ogni campo `e uno spazio vettoriale su R.
(c)
No, ma poich´e C contiene R, R `e uno spazio vettoriale su C.
(d)
No, in quanto C e R sono campi diversi.
(e)
Si, R `e sottoinsieme di C e le operazioni +, · su R sono le stesse che in C.
Soluzione. La risposta corretta `e la (e). Le altre sono incorrette in quanto le moti-
vazioni addotte o sono affermazioni vere ma non rispondono alla domanda (risposte (a)
e (d)) o adducono motivazioni che sono direttamente false (risposte (b), (c)).
3.(1 pt.) Siano A, B, C ∈M(2, R) definiti da
A =

0
−1
1
−1

,
B =

−1
0
1
1

,
C =

−2
−1
2
−2

.
Allora ABC `e uguale a:
(a)

−1
−2
0
6

.
(b)

0
−2
3
1

.
(c)

0
3
2
4

.
(d)

1
3
2
−4

.
(e)

−3
−2
4
−2

.
2

<!-- pagina 3 -->
Nome & Cognome:
Soluzione Questo `e un calcolo. Calcoliamo ABC = (AB)C:
AB =

0
−1
1
−1
 
−1
0
1
1

=

−1
−1
−2
−1

⇒
(AB)C =

−1
−1
−2
−1

.
4.(1 pt.) Determinare il rango della matrice


2
3
5
4
5
6
8
9
8


(a)
4.
(b)
1.
(c)
3.
(d)
2.
(e)
0.
Soluzione. Tramite mosse di Gauss sulle righe, otteniamo


2
3
5
4
5
6
8
9
8

R3→R3−2R2
−→


2
3
5
4
5
6
0
−1
−4


R2→R2−2R1
−→


2
3
5
0
−1
−4
0
−1
−4

R3→R2−R3
−→


2
3
5
0
−1
−4
0
0
0


L’ultima matrice contiene due pivot, per cui il rango `e 2.
5.(1 pt.) Sia
A =


0
1
2
2
1
6
1
1
1

.
Il determinante di A3 `e:
(a)
111.
(b)
12.
(c)
21.
(d)
216.
(e)
261.
Soluzione. Il determinante di A `e:
det A = −1 det

2
6
1
1

+ 2 det

2
1
1
1

= −1(−4) + 2(2) = 6
Pertanto det A3 = (det A)3 = 63 = 216.
3

<!-- pagina 4 -->
Nome & Cognome:
6.(1 pt.) Quali dei seguenti `e un prodotto Hermitiano su C2?
(a)
g((x1, y1), (x2, y2)) = 3x1x2 + 3x1y2 −3y1x2 + y1y2.
(b)
g((x1, y1), (x2, y2)) = x1x2 + 3ix1y2 −3iy1x2 + 3y1y2.
(c)
g((x1, y1), (x2, y2)) = 3ix1x2 + x1y2 + y1x2 + iy1y2.
(d)
g((x1, y1), (x2, y2)) = ix1x2 + 3ix1y2 −3iy1x2 + y1y2.
(e)
g((x1, y1), (x2, y2)) = 3x1x2 + x1y2 −iy1x2 + 3y1y2.
Soluzione. La matrice associata di un prodotto Hermitiano `e una matrice Hermitiana.
In particolare, i coefficienti di x1x2 e y1y2 devono essere reali, mentre i coefficienti di x1y2
e y1x2 devono essere coniugati tra loro. L’unico prodotto con queste propriet`a `e (b).
7.(1 pt.) L’immagine dell’applicazione lineare T : R2[x] →R2[x], dato da
T(ax2 + bx + c) = (a −b)x2 + (a + b)x −c,
`e:
(a)
R2[x].
(b)
Span(x2, x)
(c)
R1[x].
(d)
{p(x) = ax2 + bx + c ∈R2[x] ; a + b = 0}.
(e)
R1[x]⊥.
Soluzione 1. Per il teorema della dimensione dim(Im(T)) = dim R2[x] −dim ker(T).
Sappiamo che ax2 + bx + c ∈ker(T) se e solo se (a −b)x2 + (a + b)x −c = 0, ovvero
a −b = 0, a + b = 0, c = 0. Questo implica per`o che a = b = c = 0 pertanto ker(T) = {0}
e dim ker(T) = 0. Otteniamo dim(Im(T)) = dim R2[x] per cui Im(T) = R2[x].
Soluzione 2. Abbiamo 1 = T(−1), x = T(1
2x2 + 1
2x) e x2 = T(1
2x2 −1
2x). Allora
{1, x, x2} ⊂Im(T) e concludiamo (dal fatto che Im(T) `e un sottospazio) che R2[x] =
Span(1, x, x2) ⊆Im(T) ⊆R2[x], e segue Im(T) = R2[x].
Soluzione 3. La matrice che descrive T nella base canonica `e M =


1
−1
0
1
1
0
0
0
−1

.
Abbiamo det M = −2 e allora M `e invertibile. Concludiamo che anche T `e invertibile e
allora suriettivo.
4

<!-- pagina 5 -->
Nome & Cognome:
8.(1 pt.) Trovare l’insieme degli autovalori del endomorfismo T : R3 →R3, dato da
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
x + 2z
−2x + 3y −z
x + 2z

.
(a)
{−1, 2, −3}.
(b)
{−1, −3}.
(c)
{}.
(d)
{±1, ±3}.
(e)
{0, 3}.
Soluzione. Sappiamo che gli autovalori di T sono gli stessi degli autovalori di [T]B
B,
per una qualunque base B di R3. Prendendo B la base canonica, ottieniamo facilmente
[T]B
B =


1
0
2
−2
3
−1
1
0
2


per cui
pT(t) = det


1 −t
0
2
−2
3 −t
−1
1
0
2 −t

= (3 −t) det

1 −t
2
1
2 −t

=(3 −t)(t2 −3t) = −t(t −3)2.
Gli autovalori pertanto sono 0, 3.
9.(1 pt.) L’endomorfismo T : R2[x] →R2[x] dato da
T(ax2 + bx + c) = (2a −c)x2 + (a −b + c)x + a
ha autovalore λ = −1. Qual `e l’autospazio che corrisponde a questo autovalore?
(a)
Span(x, x + 1).
(b)
Span(x2, x).
(c)
Span(2x + 1).
(d)
Span(x).
(e)
Span(x2 + x + 1).
Soluzione. L’autospazio da calcolare `e
ker(T + I) = {ax2 + bx + c | (3a −c)x2 + (a + c)x + (a + c) = 0}
Gli elementi dell’autospazio soddisfano pertanto 3a −c = 0 e a + c = 0, da cui si ottiene
a = c = 0 pertanto
ker(T + I) = {ax2 + bx + c | a = c = 0} = Span(x).
5

<!-- pagina 6 -->
Nome & Cognome:
10.(1 pt.) L’ntersezione della retta r = t(2, −2, 0) + s · t(1, −2, 1) (s ∈R) con il piano
π = {2x −2y + z = 1} `e:
(a)
Tutto il piano π.
(b)
P = t(−1, −1, 1).
(c)
P = t(1, 0, −1).
(d)
Non hanno un’intersezione.
(e)
Tutta la retta r.
Soluzione 1. La retta ha coordinate parametriche
x = 2 + s,
y = −2 −2s,
z = s.
Sostituendo queste coordinate nell’equazione del piano otteniamo
1 = 2(2 + s) −2(−2 −2s) + s = 8 + 7s
⇒
s = −1
Pertanto, la retta incontra il piano quando s = −1, nel punto
P = t(2, −2, 0) + (−1) · t(1, −2, 1) = t(1, 0, −1).
Soluzione 2. L’intersezione non pu`o essere tutto il piano e vediamo subito che non
`e tutta la retta r (per esempio perch´e il punto t(2, −2, 0) (che corrisponde a s = 0)
non `e nel piano.
Allora l’intersezione o `e un punto o l’insieme vuoto.
Si pu`o allora
controllare i due punti dati nelle risposte (b) e (c). Il punto P della risposta (b) `e nel
piano, ma non nella retta: Se fosse un punto della retta, ci dovrebbe essere un s tale che
t(2, −2, 0) + s · t(1, −2, 1) = P = t(−1, −1, 1). La prima componente ci da 2 + s = −1
(allora s = −3), la terza componente ci da 0 + s = 1 (allora s = 1). Concludiamo che
non possiamo trovare s `e allora P̸ ∈r. Invece per il punto P della risposta (c) troviamo
P ∈r e P ∈π, allora (c) deve essere la risposta giusta.
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
x + 2y
= 2,
−x + ky + kz
= k −1,
2x −2ky
= 4.
(1) Discutere per quali valori di k la matrice A dei coefficienti `e invertibile.
(2) Al variare di k ∈R, discutere quante soluzioni ammette il sistema lineare.
(3) Per ogni k ∈R per cui il sistema ammette soluzioni, trovare tutte le soluzioni.
Soluzione. 1) La matrice dei coefficienti `e


1
2
0
−1
k
k
2
−2k
0


Questa `e invertibile se
0̸ = det A = −k det

1
2
2
−2k

= −k(−2k −4) = 2k(k + 2)
Pertanto, A `e invertibile se e solo se k /∈{0, −2}.
2) Per k̸ = 0, −2, la matrice dei coefficienti A `e invertibile per il punto precedente e
quindi il sistema ammette un’unica soluzione. Per k = 0 abbiamo matrice completa
(A|b) =


1
2
0
2
−1
0
0
−1
2
0
0
4


R37→R3+2R2
−→


1
2
0
2
−1
0
0
−1
0
0
0
2


da cui otteniamo rank(A) = 2 < 3 = rank(A|b) per cui, da Rouch´e-Capelli, non ci sono
soluzioni. Per k = −2 otteniamo


1
2
0
2
−1
−2
−2
−3
2
4
0
4

R37→R3−2R1
−→


1
2
0
2
−1
−2
−2
−3
0
0
0
0

R27→R1−R3
−→


1
2
0
2
0
0
−2
−1
0
0
0
0


Poich´e rank(A) = rank(A|b) = 2, nuovamente per Rouch´e Capelli esistono infinite
soluzioni che dipendono da 3 −rank(A) = 1 parametri liberi.
7

<!-- pagina 8 -->
Nome & Cognome:
3) Per k̸ = 0, −2 l’unica soluzione si pu`o trovare come x = A−1b. Alternativamente,
possiamo risolvere il sistema:


1
2
0
2
−1
k
k
k −1
2
−2k
0
4

R27→R2+R1
−→


1
2
0
2
0
k + 2
k
k + 1
2
−2k
0
4


R37→R3−2R1
−→


1
2
0
2
0
k + 2
k
k + 1
0
−2(k + 2)
0
0

R37→R3+2R2
−→


1
2
0
2
0
k + 2
k
k + 1
0
0
2k
2(k + 1)


R27→R2−R3/2
−→


1
2
0
2
0
k + 2
0
0
0
0
2k
2(k + 1)


Da qui si ottiene z = k+1
k , y = 0 e x = 2.
Per k = −2 partiamo dal sistema ridotto nel punto precedente


1
2
0
2
0
0
−2
−1
0
0
0
0


da cui si ottiene z = 1
2 e x + 2y = 2 per cui lo spazio delle soluzioni `e





2 −2y
y
1/2


 y ∈R


=


2
0
1/2

+ Span


−2
1
0

.
8

<!-- pagina 9 -->
Nome & Cognome:
12.(11 pts.) Sullo spazio R2[x] definiamo il prodotto scalare
g(p(x), q(x)) = p(1)q(1) + p(−1)q(−1) + p(1)q(0) + p(0)q(1) + 2p(0)q(0).
(1) Trovare la matrice associata al prodotto scalare g nella base canonica B = {1, x, x2}.
(2) Calcolare le norme ∥x∥e ∥x2∥e l’angolo fra i polinomi x e x2 rispetto al prodotto
scalare g.
(3) Trovare una base del complemento ortogonale di Span(x, x2) rispetto al prodotto
scalare g.
Soluzioni. 1) La matrice associata a g `e
S = [g]B =


g(1, 1)
g(1, x)
g(1, x2)
g(1, x)
g(x, x)
g(x, x2)
g(1, x2)
g(x, x2)
g(x2, x2)

=


6
1
3
1
2
0
3
0
2

.
(2) Calcoliamo
∥x∥=
p
g(x, x) =
p
S2,2 =
√
2,
∥x2∥=
p
g(x2, x2) =
p
S3,3 =
√
2.
Inoltre, dal fatto che g(x, x2) = S2,3 = 0 si ottiene subito che l’angolo tra x e x2 `e π/2.
(3) Il primo modo per calcolare il complemento ortogonale `e di calcolare i coefficienti
a, b, c tali per cui ax2 + bx + c ⊥Span(x, x2):

0 = g(ax2 + bx + c, x) = ag(x2, x) + bg(x, x) + cg(1, x) = 2b + c,
0 = g(ax2 + bx + c, x2) = ag(x2, x2) + bg(x, x2) + cg(1, x2) = 2a + 3c.
⇒

2b + c = 0
2a + 3c = 0
⇒


a
b
c

=


−3/2 · s
−1/2 · s
s

, s ∈R
Pertanto, il complemento ortogonale di Span(x, x2) consiste nei multipli di −3
2x2 −1
2x+1
(o equivalentemente nei multipli di 3x2 + x −2).
Alternativamente: il complemento ortogonale di Span(x, x2) ha dimensione = dim R2[x]−
dim Span(x, x2) = 3 −2 = 1 e per trovare un generatore basta prendere un qualunque
polinomio p(x) /∈Span(x, x2) e calcolare p(x) −prSpan(x,x2)(p(x)), dove prSpan(x,x2) de-
nota la proiezione ortogonale su Span(x, x2). Prendendo p(x) = 1 e notando (punto
precedente) che x, x2 sono una base ortogonale di Span(x, x2), calcoliamo
1 −prSpan(x,x2)(1) = 1 −g(1, x)
g(x, x)x −g(1, x2)
g(x2, x2)x2 = 1 −1
2x −3
2x2.
Pertanto un generatore del complemento ortogonale di Span(x, x2) `e 3
2x2 + 1
2x −1.
9
