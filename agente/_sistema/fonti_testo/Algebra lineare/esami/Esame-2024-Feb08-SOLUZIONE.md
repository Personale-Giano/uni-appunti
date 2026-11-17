# Esame-2024-Feb08-SOLUZIONE

<!-- pagina 1 -->
Nome & Cognome:
Algebra Lineare, Esame Finale
Febbraio 8, 2024
• Tutto il lavoro deve essere unicamente vostro.
• L’utilizzo di calcolatrici `e vietato.
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
(•)
(c)
(d)
(e)
2.
(a)
(b)
(c)
(•)
(e)
3.
(a)
(b)
(c)
(•)
(e)
4.
(a)
(b)
(•)
(d)
(e)
5.
(a)
(b)
(c)
(•)
(e)
6.
(a)
(b)
(c)
(•)
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
(d)
(•)
10.
(a)
(•)
(c)
(d)
(e)
Non scrivere qua sotto!
Risp. Multiple
Risp. Aperte
Totale

<!-- pagina 2 -->
Nome & Cognome:
Risposta multipla
1.(1 pt.) Trovare il numero z ∈C tale che (i −1)(i −2)z = (i + 1)(i + 2)(i + 3)?
(a)
z = 10 + 3i.
(b)
z = i −3.
(c)
z = 30 + 10i.
(d)
z = 3i −1.
(e)
z = 1 −30i.
Soluzione. Calcoliamo: (i−1)(i−2) = 1−3i, e (i+1)(i+2)(i+3) = (1+3i)(i+3) = 10i,
per cui l’eqazione diventa (1 −3i)z = 10i, e
z =
10i
1 −3i = 10i · (1 −3i)
|1 −3i|2
= 10i · (1 + 3i)
10
= i −3.
2.(1 pt.) Quale degli seguenti insiemi non `e un sottospazio di R2[x]:
(a)
{p(x) ∈R2[x] | p(0) = 0}.
(b)
{(t + s)x2 −tx −s | s, t ∈R}.
(c)
{p(x) = ax2 + bx + c | a = 2c, b = 0}. (d)
{(1 + t)x2 + tx | t ∈R}.
(e)
{p(x) ∈R2[x] | p(1) = 0 = p(2)}.
Soluzione 1.
Si nota che il polinomio nullo non `e nell’insieme (d), poich´e p(x) =
(1 + t)x2 + tx ha almeno uno dei coeﬃcienti nonzero. Questo pertanto non pu`o essere un
sottospazio.
Soluzione 2. Prendendo due polinomi p1 e p2 in uno degli insiemi, si nota che abbiamo
sempre anche p1 + p2 nello stesso insieme, tranne per (d) dove troviamo (p1 + p2)(x) =
(2 + t + s)x2 + (t + s)x, allora un polinomio che non `e del tipo dell’insieme.
3.(1 pt.) I polinomi
p1(x) = x2 + x + 1,
p2(x) = x2 + x −1,
p3(x) = x −2
formano una base di R2[x]. Il vettore delle coordinate di q(x) = (x + 1)2 in questa base
`e:
(a)
(1, 2, 1).
(b)
(2p1, −p2, p3).
(c)
(3, −2, −1).
(d)
(2, −1, 1).
(e)
(x2, 2x, 1).
2

<!-- pagina 3 -->
Nome & Cognome:
Soluzione 1. Dobbiamo calcolare (a, b, c) tali che q(x) = x2 +2x+1 `e uguale a ap1(x)+
bp2(x) + cp3(x) = (a + b)x2 + (a + b + c)x + (a −b −2c):



a + b = 1
a + b + c = 2
a −b −2c = 1
Sottraendo la seconda equazione alla prima si ottiene c = 1 e le equazioni rimanenti
danno a + b = 1, a −b = 3, da cui a = 2 e b = −1. Dunque la soluzione `e (2, −1, 1).
Soluzione 2. Le risposte (b) e (e) non hanno senso. Per le altre tre risposte calcoliamo
il polinomio con le coordinate date:
(a) p1(x) + 2p2(x) + p3(x) = x2 + x + 1 + 2x2 + 2x −2 + x −2 = 3x2 + 4x −3̸ = q(x),
(c) 3p1(x) −2p2(x) −p3(x) = 3x2 + 3x + 3 −2x2 −2x + 2 −x + 2 = x2 + 7̸ = q(x),
(d) 2p1(x) −p2(x) + p3(x) = 2x2 + 2x + 2 −x2 −x + 1 + x −2 = x2 + 2x + 1 = q(x).
4.(1 pt.) Date le matrici
A =


√
2
0
−
√
2
√
3
√
3
0
√
5
0
√
5

,
B =


√
3
−
√
2
0
0
√
2
√
5
√
3
0
√
5


calcolare tr(AB):
(a)
30.
(b)
(
√
2 +
√
3 +
√
5)2.
(c)
5.
(d)
√
30.
(e)
√
5.
Soluzione. Calcoliamo gli elementi sulla diagonale di AB:
AB =


0
⋆
⋆
⋆
0
⋆
⋆
⋆
5


per cui tr(AB) = 5.
Attenzione. tr(AB)̸ = tr(A) tr(B).
3

<!-- pagina 4 -->
Nome & Cognome:
5.(1 pt.) La composizione S ◦T di S : R3 →R2, S(x, y, z) = (x + y, 2z) e T : R2 →R3,
T(x, y) = (x + y, x −y, y) `e:
(a)
(x, y, z) 7→(2x, 2y, 2z).
(b)
(x, y) 7→(x + 2y, 2x −2y).
(c)
(x, y, z) 7→(x + y + 2z, x + y −2z, 2z).
(d)
(x, y) 7→(2x, 2y).
(e)
Non `e ben deﬁnito.
Soluzione. (S ◦T)(x, y, z) = S(T(x, y, z)) = S(x+y, x−y, y) = ((x+y)+(x−y), 2y) =
(2x, 2y). La risposta corretta `e quindi (d).
6.(1 pt.) Il nucleo dell’applicazione lineare T : M(n) →M(n), T(A) = A + AT:
(a)
Consiste in matrici diagonali.
(b)
Consiste nella matrice zero.
(c)
Consiste di matrici simmetriche.
(d)
Consiste in matrici antisimmetriche.
(e)
`E vuoto.
Soluzione. A ∈ker(T) se e solo se T(A) = A + AT = 0, ovvero A = −AT. In altre
parole, A ∈ker(T) se e solo se A `e antisimmetrica.
7.(1 pt.) La forma quadratica q(x) = 2x2
1 + 2x1x2 + 2x2
3 si pu`o scrivere come qS(x) con
matrice S uguale a:
(a)


2
1
0
1
0
0
0
0
2

.
(b)


2
2
0
2
0
0
0
0
0

.
(c)


2
2
0
2
0
0
0
0
2

.
(d)


2
0
0
0
0
1
0
1
2

.
(e)


2
0
0
0
0
1
0
0
2

.
4

<!-- pagina 5 -->
Nome & Cognome:
Soluzione. Ricordiamo che S `e la matrice i cui elementi sulla diagonale sono i coeﬃcienti
degli x2
i (nel nostro caso uguali a 2,0,2), mentre gli altri coeﬃcienti aij sono la met`a del
coeﬃciente di xixj. Nel nostro caso:
S =


2
1
0
1
0
0
0
0
2


8.(1 pt.) In R2[x], sia dato il prodotto
⟨p(x), q(x)⟩= p(0)q(0) + p(1)q(1) + p(−1)q(−1).
Rispetto a questo prodotto, l’angolo tra p(x) = x e q(x) = x2 `e:
(a)
x3.
(b)
π/4.
(c)
0.
(d)
1.
(e)
π/2.
Soluzione. Calcoliamo ⟨x, x2⟩= 0 · 0 + 1 · 1 + (−1) · 1 = 0, per cui cos θ =
⟨x,x2⟩
∥x∥·∥x2∥= 0 e
quindi θ = π/2.
9.(1 pt.) Quale delle seguenti applicazioni lineari T : C2 →C2 non `e autoaggiunto
rispetto al prodottto hermitiano Euclideo?
(a)
T(x, y) = (2x −y, −x + 2
√
2y).
(b)
T(x, y) = (x −(i + 2)y, (i −2)x + y).
(c)
T(x, y) = (x + 2y, 2x).
(d)
T(x, y) = (x −2iy, 2ix + y).
(e)
T(x, y) = (2ix −(1 + i)y, −(1 −i)x + 2y).
Soluzione. Ricordiamo che una applicazione lineare T `e autoaggiunta rispetto al prodotto
Euclideo, se e solo se la matrice associata di T rispetto alla base canonica `e Hermitiana
(ovvero A = tA). Calcoliamo le matrici associate agli operatori proposti:
(a) =

2
−1
−1
2
√
2

(b) =

1
−(i + 2)
i −2
1

(c) =

1
2
2
0

(d) =

1
−2i
2i
1

(e) =

2i
−(1 + i)
−(1 −i)
2

L’unica non Hermitiana ´e la (e), in quanto ha un elemento non reale sulla diagonale.
5

<!-- pagina 6 -->
Nome & Cognome:
10.(1 pt.)
La distanza tra le rette r1 = (2, 0, 0) + Span(1, 1, 1) e r2 = (1, 2, 0) +
Span(−1, 1, −1) `e:
(a)
2
√
2.
(b)
1
√
2.
(c)
2.
(d)
4
√
2.
(e)
8.
Soluzione.
Chiamiano p1 = (2, 0, 0), v1 = (1, 1, 1) il punto e la direzione di r1, e
similmente p2 = (1, 2, 0), v2 = (−1, 1, −1) il punto e la retta di r2.
Ricordiamo la
formula:
d(r1, r2) = | det(p1 −p2, v1, v2)|
∥v1 × v2∥
Calcoliamo
v1 × v2 = (−2, 0, 2)
⇒
∥v1 × v2∥= 2
√
2
det(p1 −p2, v1, v2) = det


1
−2
0
1
1
1
−1
1
−1

= −2
Per cui
d(r1, r2) =
2
2
√
2 = 1
√
2
6

<!-- pagina 7 -->
Nome & Cognome:
Risposta aperta
Per ricevere punteggio parziale, dovete mostrare il vostro lavoro!
11.(11 pts.) Data la matrice
A =



2k
0
0
1
0
1
0
k2
0



con un parametro k ∈C.
(1) Al variare di k, trovare gli autovalori di A.
(2) Per quali valori di k la matrice A `e diagonalizzabile?
(3) Per k = i, trovare una base di autovettori di A.
Soluzione.
(1) Calcoliamo il polinomio caratteristico di A:
pA(t) = det


2k −t
0
0
1
−t
1
0
k2
−t

= (2k −t) det

−t
1
k2
−t

=(2k −t)(t2 −k2) = (2k −t)(t −k)(t + k)
Pertanto gli autovalori di A sono k, −k, e 2k.
(2) Se k̸ = 0, i tre autovalori sono tutti distinti, e dunque A `e diagonalizzabile. Per k = 0
la matrice diventa
A =



0
0
0
1
0
1
0
0
0



e il polinomio caratteristico (calcolato prima) diventa pA(t) = −t3. In questo caso per-
tanto abbiamo solo un autovalore 0 con molteplicit`a algebrica 3, tuttavia la molteplicit`a
geometrica `e
mg(0) = dim ker A = 3 −rk(A) = 3 −rk



0
0
0
1
0
1
0
0
0


= 3 −1 = 2̸ = 3
pertanto A non `e diagonalizzabile se k = 0.
7

<!-- pagina 8 -->
Nome & Cognome:
(3) Per k = i, la matrice diventa
A =



2i
0
0
1
0
1
0
−1
0



e gli autovalori di A sono 2i, i, −i. Calcoliamo gli autovettori:
λ = 2i: V2i = ker(A −2i) = ker



0
0
0
1
−2i
1
0
−1
−2i


`e dato da:
V2i =





x
y
z



0 = 0
x −2iy + z = 0
−y −2iz = 0


=





x
y
z



x = 3t
y = −2it
z = t


= Span


3
−2i
1


λ = i: Vi = ker(A −i) = ker



i
0
0
1
−i
1
0
−1
−i


`e dato da:
V2i =





x
y
z



ix = 0
x −iy + z = 0
−y −iz = 0


=





x
y
z



x = 0
y = −it
z = t


= Span


0
−i
1


λ = −i: V−i = ker(A + i) = ker



3i
0
0
1
i
1
0
−1
i


`e dato da:
V2i =





x
y
z



3ix = 0
x + iy + z = 0
−y + iz = 0


=





x
y
z



x = 0
y = it
z = t


= Span


0
i
1


Pertanto la base ti autovettori `e ottenuta scegliendo una base da ogni autospazio:
B =





3
−2i
1

,


0
−i
1

,


0
i
1





8

<!-- pagina 9 -->
Nome & Cognome:
12.(11 pts.) Sia T : R3 →R3 l’endomorﬁsmo dato da
T(t(x, y, z)) = t(x + 2y + 3z, 2x + 4y + 6z, 3x + 6y + 8z).
(1) Determinare la matrice A associata a T rispetto alla base canonica di R3, e
calcolare il rango di T.
(2) Calcolare tutti i vettori t(x, y, z) tali che T(t(x, y, z)) = t(5, 10, 5).
(3) Determinare tutti i valori reali di k tali che il vettore t(k, k2, 0) appartiene
all’immagine di T.
Soluzione. (1) La matrice associata a T rispetto alla base canonica `e la matrice con
colonne Te1 = t(1, 2, 3), Te2 = t(2, 4, 6) e Te3 = t(3, 6, 8):
A =


1
2
3
2
4
6
3
6
8


Applichiamo l’algoritmo di Gauss ad A:


1
2
3
2
4
6
3
6
8

R2−2R1
→


1
2
3
0
0
0
3
6
8

R3−3R1
→


1
2
3
0
0
0
0
0
−1

R3↔R2
→


1
2
3
0
0
−1
0
0
0


La matrici a scalini ottenuta ha due pivots, dunque rk(A) = 2.
(2) Se v = t(x, y, z) `e tale che T(v) = t(5, 10, 5), allora


x + 2y + 3z
2x + 4y + 6z
3x + 6y + 8z

= T(v) =


5
10
5


⇒



x + 2y + 3z = 5
2x + 4y + 6z = 10
3x + 6y + 8z = 5
Risolviamo il sistema:


1
2
3
5
2
4
6
10
3
6
8
5

R2−2R1
→


1
2
3
5
0
0
0
0
3
6
8
5

R3−3R1
→


1
2
3
5
0
0
0
0
0
0
−1
−10


R3↔R2
→


1
2
3
5
0
0
−1
−10
0
0
0
0

R1+3R2
→


1
2
0
−25
0
0
−1
−10
0
0
0
0

−R2
→


1
2
0
−25
0
0
1
10
0
0
0
0


Le soluzioni richieste soddisfano pertanto le equazioni x + 2y = −25, z = 10. In forma
parametrica, abbiamo che


x
y
z

=


−25 −2t
t
10


9

<!-- pagina 10 -->
Nome & Cognome:
(3) Ricordiamo che un vettore w =


k
k2
0

∈R3 appartiene all’immagine di T se esiste
un vettore v =


x
y
z

∈R3 che veriﬁchi l’equazione Tv = w, ovvero tale che


x + 2y + 3z
2x + 4y + 6z
3x + 6y + 8z

= T(v) = w =


k
k2
0

.
Come nel punto precedente, questo equivale a scrivere il sistema



x + 2y + 3z = k
2x + 4y + 6z = k2
3x + 6y + 8z = 0
↔


1
2
3
k
2
4
6
k2
3
6
8
0


e i vettori t(k, k2, 0) nell’immagine corrispondono ai valori di k per cui il sistema sopra
ammette soluzione. Per Rouch´e Capelli, questo avviene quando il rango della matrice
completa `e uguale al rango della matrice dei coeﬃcienti A, che `e = 2 per il primo punto.
Calcoliamo dunque:
rk


1
2
3
k
2
4
6
k2
3
6
8
0

R2−2R1
→
rk


1
2
3
k
0
0
0
k2 −2k
3
6
8
0


R3−3R1
→


1
2
3
k
0
0
0
k2 −2k
0
0
−1
−3k

R3↔R2
→


1
2
3
k
0
0
−1
−3k
0
0
0
k2 −2k


Il rango di questa matrice `e 2 se e solo se la terza riga non ha pivot, cio`e se e solo se
k2 −2k = k(k −2) = 0. Pertanto, w = t(k, k2, 0) appartiene all’immagine di T, se e solo
se il sistema T(v) = w ammette soluzione, se e solo se k ∈{0, 2}.
10
