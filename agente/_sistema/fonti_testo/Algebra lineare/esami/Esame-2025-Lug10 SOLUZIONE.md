# Esame-2025-Lug10 SOLUZIONE

<!-- pagina 1 -->
Nome & Cognome:
Algebra Lineare, Esame Finale
10 Luglio 2025
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
(•)
(b)
(c)
(d)
(e)
2.
(•)
(b)
(c)
(d)
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
(•)
(d)
(e)
6.
(a)
(b)
(•)
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
(•)
(b)
(c)
(d)
(e)
10.
(•)
(b)
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
1.(1 pt.) Quale dei seguenti `e una radice di p(z) = z4 + 7z2 + 12:
(a)
z = −2i.
(b)
z = −2.
(c)
Il polinomio non ha radici.
(d)
z = 3 + 4i.
(e)
z = 4.
Soluzione: Se poniamo w = z2, otteniamo p(w) = w2 + 7w + 12 = (w + 3)(w + 4)
con radici w = −3 e w = −4. Le radici di p(z) sono allora le soluzioni di z2 = −4 e di
z2 = −3, cio`e z = ±2i e z = ±
√
3i. In particolare, risposta (a) `e corretta.
2.(1 pt.) Sia V = R3[x] lo spazio dei polinomi di grado al massimo tre e coefficienti reali.
Sia W il sottoinsieme dei polinomi p(x) ∈V con p(6) = 0. La dimensione di W `e:
(a)
Tre.
(b)
Due.
(c)
Quattro.
(d)
Uno.
(e)
W non ha una dimensione perch´e non `e un sottospazio vettoriale.
Soluzione 1: Se p(x) ∈R3[x] con p(6) = 0, allora p(x) = (x−6)q(x) con q(x) ∈R2[x].
La dimensione di W `e allora uguale alla dimensione di R2[x], cio`e tre.
Soluzione 2: Consideriamo T : V = R3[x] →R definito da T(p(x)) = p(6). T `e
una mappa lineare, e W `e il sottospazio ker(T), allora con la formula generale dim V =
dim ker(T) + dim Im(T). Poich´e la mappa T `e suriettiva (per ogni a ∈R il polinomio
p(x) = a
6x soddisfa T(p(x)) = a), otteniamo dim Im(T) = dim R = 1 e, dal teorema del
rango, dim W = dim V −dim Im(T) = 4 −1 = 3.
3.(1 pt.) Sia T : R3[x] →R la funzione T(p(x)) = p(7). La mappa T `e lineare?
(a)
No, perch´e (c · p)(7)̸ = c · p(7) per qualche c ∈R e qualche p(x) ∈R3[x].
(b)
No, perch´e (p + q)(7)̸ = p(7) + q(7) per qualche p(x), q(x) ∈R3[x].
(c)
No, perch´e p(7)̸ = 0 per qualche p(x) ∈R3[x].
(d)
S`ı.
(e)
No, perch´e 0V ∈R3[x] soddisfa 0V (7)̸ = 0.
2

<!-- pagina 3 -->
Nome & Cognome:
Soluzione: Le propriet`a T(c · p) = c · T(p) e T(p + q) = T(p) + T(q) sono soddisfatte,
allora T `e lineare e risposta (d) `e corretta.
4.(1 pt.) Sia
A =


1
−1
0
0
0
1
0
0
0
2
−1
0

.
Qual `e il determinante di A?
(a)
1.
(b)
0.
(c)
det(A) non `e definito.
(d)
2.
(e)
−1.
Soluzione: La matrice non `e quadrata, per cui det(A) non `e definito.
5.(1 pt.) Il sistema lineare con matrice completa
A =


3
12
15
6
2
8
10
4
4
16
20
8


ha un numero di soluzioni pari a:
(a)
Una.
(b)
Infinite, che dipendono da 1 parametro.
(c)
Infinite, che dipendono da 2 parametri.
(d)
Zero.
(e)
Un numero finito, maggiore di 1.
Soluzione: La riduzione a scalini ci da
A =


3
12
15
6
2
8
10
4
4
16
20
8

→


1
4
5
2
2
8
10
4
4
16
20
8

→


1
4
5
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
.
Abbiamo prima diviso la prima riga per 3 e poi cambiato le altre righe secondo le mosse
di Gauss R2 →R2−2R1 e R3 →R3−4R1. Visto che il rango della matrice dei coefficienti
`e 1 ed `e uguale al rango di A, otteniamo che la dimensione dello spazio di soluzioni `e
3 −1 = 2, per cui ci sono infinite soluzioni che dipendono da 2 parametri.
3

<!-- pagina 4 -->
Nome & Cognome:
6.(1 pt.) La matrice associata all’identit`a Id : R3 →R3 dalla base B = {e2, e3, e1} alla
base C = {e3, e2, e1} `e:
(a)


1
0
0
0
1
0
0
0
1


(b)
Il problema non `e ben definito.
(c)


0
1
0
1
0
0
0
0
1


(d)


0
0
1
1
0
0
0
1
0


(e)


0
0
1
0
1
0
1
0
0


Soluzione: Dobbiamo usare solo la definizione della matrice associata:
[Id]B
C =
h
[Id(e2)]C
[Id(e3)]C
[Id(e1)]C
i
=
h
[e2]C
[e3]C
[e1]C
i
Come prima colonna otteniamo le coordinate rispetto a C del primo elemento della base
B, cio`e e2. Queste coordinate sono t(0, 1, 0). Simile, le coordinate di e3 sono t(1, 0, 0) e
finalmente le coordinate di e1 sono t(0, 0, 1). La matrice con queste colonne `e quella della
risposta (c).
7.(1 pt.) L’immagine dell’applicazione lineare T : R1[x] →R2[x], T(ax+b) = bx2+ax−a
`e:
(a)
{p(x) = Ax2 + Bx + C ∈R2[x] ; B + C = 0}.
(b)
{p(x) ∈R2[x] ; p(0) = −a}.
(c)
{p(x) ∈R2[x] ; p(a −b) = p(a + b) = p(−2a) = 0}.
(d)
{p(x) = Ax + B ∈R1[x] ; A = B}.
(e)
{p(x) = ax2 + bx + c ∈R2[x] ; a = a −b, b = a + b, c = −2a}.
Soluzione: L’immagine `e, per definizione di T, uguale a
{p(x) = bx2 + ax −a ∈R2[x] ; a, b ∈R}.
`E semplice a vedere che questo insieme si pu`o riscrivere come insieme dato nella risposta
(a) [con A = b, B = a, C = −a]. Tutte le altre risposte non hanno senso.
4

<!-- pagina 5 -->
Nome & Cognome:
8.(1 pt.) L’angolo tra il piano Π = {x + z = 3} e la retta r = t(1, 0, 1) + s · t(2, 2, 0) `e:
(a)
1
2.
(b)
0.
(c)
π
3.
(d)
π
2 −1
2.
(e)
π
6.
Soluzione: Calcoliamo prima l’angolo tra il vettore normale N = t(1, 0, 1) al piano Π
e il vettore di direzione della retta r, cio`e t(2, 2, 0). Questo angolo `e
arccos

⟨t(1, 0, 1), t(2, 2, 0)⟩
||t(1, 0, 1)|| · ||t(2, 2, 0)||

= arccos

2
√
2 ·
√
8

= arccos 1
2 = π
3 .
L’angolo tra il piano e r `e π
2 meno l’angolo appena calcolato, allora π
2 −π
3 = π
6 .
9.(1 pt.) Data la matrice
A =


2
1
0
1
0
1

,
la traccia di A · tA `e
(a)
7.
(b)
9.
(c)
Non si pu`o calcolare, poich´e A non `e una matrice quadrata.
(d)
6.
(e)
0.
Soluzione: A · tA `e una matrice 3 × 3, ma per calcolare la traccia dobbiamo solo
calcolare gli elementi sulla diagonale. Otteniamo
A · tA =


2
1
0
1
0
1

·

2
0
0
1
1
1

=


5
∗
∗
∗
1
∗
∗
∗
1

,
e concludiamo che la traccia `e 5 + 1 + 1 = 7.
5

<!-- pagina 6 -->
Nome & Cognome:
10.(1 pt.) L’ntersezione tra le rette
r1 = t(3, 1, −4) + s1 · t(1, 1, −2)
r2 = t(1, −1, 0) + s2 · t(0, 1, 1)
con s1, s2 ∈R, `e:
(a)
P = t(1, −1, 0).
(b)
P = t(0, −1, −1).
(c)
P = t(1, 0, −1).
(d)
Non hanno un’intersezione.
(e)
P = t(−1, −1, 2).
Soluzione: Nel punto di intersezione (se esiste) i parametri s1, s2 soddisfano il sistema:



3 + s1 = 1
1 + s1 = −1 + s2
−4 −2s1 = s2
Dalla prima equazione si ottiene s1 = −2. Inserito nella seconda, si ottiene −1 = −1+s2
e quindi s2 = 0. Finalmente, inserito nell’ultima equazione si ottiene 0 = 0 e allora
anch’essa `e verificata. Pertanto, il punto di intersezione si trova in modo pi`u semplice
inserendo s2 = 0 in r2, allora P = t(1, −1, 0).
6

<!-- pagina 7 -->
Nome & Cognome:
Risposta aperta
Per ricevere punteggio parziale, dovete mostrare il vostro lavoro!
11.(11 pts.) Si consideri la seguente matrice:
A =


4
1
0
0
−2k
1
0
0
k2

.
(1) Al variare di k ∈R, calcolare gli autovalori di A, con le loro molteplicit`a algebrica
e geometrica.
(2) Determinare per quali valori di k ∈R la matrice `e diagonalizzabile.
(3) Per k = 1, determinare una matrice diagonale D ed una matrice invertibile P,
per cui A = PDP −1.
Soluzione:
(1) Il polinomio caratteristico `e
pA(λ) = det(A −λI) = det


4 −λ
1
0
0
−2k −λ
1
0
0
k2 −λ

= (4 −λ)(−2k −λ)(k2 −λ).
Gli autovalori sono allora λ1 = 4, λ2 = −2k, λ3 = k2. [Alternativamente si nota che A
`e una matrice triangolare, allora gli autovalori sono esattamente i valori sulla diagonale
principale.] Ci sono quattro casi:
(a) k = 0. In questo caso λ1 = 4 con molteplicit`a algebrica e geometrica 1, e λ2 =
λ3 = 0 con molteplicit`a algebrica 2. La molteplicit`a geometrica di questo autovalore `e
3 −rk(A)|k=0 = 3 −rk


4
1
0
0
0
1
0
0
0

= 3 −2 = 1.
(b) k = 2.
In questo caso λ2 = −4 con molteplicit`a algebrica e geometrica 1, e
λ1 = λ3 = 4 con molteplicit`a algebrica 2. La molteplicit`a geometrica di questo autovalore
`e
3 −rk(A −4I)|k=2 = 3 −rk


0
1
0
0
−8
1
0
0
0

= 3 −2 = 1.
7

<!-- pagina 8 -->
Nome & Cognome:
(c) k = −2.
In questo caso λ1 = λ2 = λ3 = 4 con molteplicit`a algebrica 3.
La
molteplicit`a geometrica di questo autovalore `e
3 −rk(A −4I)|k=−2 = 3 −rk


0
1
0
0
0
1
0
0
0

= 3 −2 = 1.
(d) k̸ ∈{0, 2, −2}. In questo caso λ1 = 4, λ2 = −2k, e λ3 = k2 sono tutti distinti e
allora hanno tutti molteplicit`a algebrica e geometrica uguale a 1.
(2) Dalla parte (1) vediamo che nei casi k ∈{0, 2, −2} esiste sempre un autovalore con
molteplicit`a algebrica > 1, ma molteplicit`a geometrica = 1. In questi tre casi, la matrice
A allora non `e diagonalizzabile. Invece nel caso k̸ ∈{0, 2, −2} gli autovalori sono tutti
distinti e A `e diagonalizzabile.
(3) Dalla parte (1) e (2) sappiamo che per k̸ ∈{0, 2, −2} la matrice `e diagonalizzabile
con tre autovalori distinti.
In particolare, per k = 1 questi autovalori sono λ1 = 4,
λ2 = −2, λ3 = 1. La matrice D ha gli autovalori sulla diagonale, allora
D =


4
0
0
0
−2
0
0
0
1

.
La matrice P invece ha come colonne gli autovettori corrispondenti. Calcoliamo allora
gli autovettori.
Per λ1 = 4, abbiamo
(A −4I)x = 0 ⇔


0
1
0
0
−6
1
0
0
−3




x1
x2
x3

= 0 ⇔x ∈Span


1
0
0

.
Per λ2 = −2, abbiamo
(A + 2I)x = 0 ⇔


6
1
0
0
0
1
0
0
3




x1
x2
x3

= 0 ⇔x ∈Span


−1
6
0

.
Finalmente, per λ3 = 1, abbiamo
(A −k2I)x = 0 ⇔


3
1
0
0
−3
1
0
0
0




x1
x2
x3

= 0 ⇔x ∈Span


−1
3
9

.
Allora
P =


1
−1
−1
0
6
3
0
0
9

.
8

<!-- pagina 9 -->
Nome & Cognome:
12.(11 pts.) Sia T : R3 →R3 l’endomorfismo dato da
T(t(x, y, z)) = t(x + y + 4z, 2x + 4y + 6z, x −y + 6z).
(1) Determinare la matrice A associata a T rispetto alla base canonica di R3, e
calcolare il rango di T.
(2) Calcolare tutti i vettori t(x, y, z) tali che T(t(x, y, z)) = t(5, 4, 11).
(3) Determinare tutti i valori reali di k tali che il sistema T(t(x, y, z)) = t(1, k2, 2k)
ammette infinite soluzioni.
Soluzione:
(1) La matrice A `e dato da
A =

T


1
0
0


 T


0
1
0


 T


0
0
1



=


1
1
4
2
4
6
1
−1
6

.
Per calcolare il rango di T (che `e uguale al rango di A), riduciamo A a scalini.


1
1
4
2
4
6
1
−1
6

R2−2R1
→


1
1
4
0
2
−2
1
−1
6

R3−R1
→


1
1
4
0
2
−2
0
−2
2

R3+R2
→


1
1
4
0
2
−2
0
0
0

.
Vediamo allora che il rango di T `e 2.
(2) L’equazione T(t(x, y, z)) =
t(5, 4, 11) `e equivalente a A · t(x, y, z) =
t(5, 4, 11),
allora a un sistema lineare con matrice completa


1
1
4
5
2
4
6
4
1
−1
6
11

.
Usando la stessa riduzione a scalini come nella parte (1), si trova


1
1
4
5
2
4
6
4
1
−1
6
11

→


1
1
4
5
0
2
−2
−6
0
0
0
0

.
Scegliendo z = t come parametro libero, si ottiene y = −3 + t e dalla prima equazione
x = 5 −4t −(−3 + t) = 8 −5t. Le soluzioni sono


x
y
z

=


8 −5t
−3 + t
t

⇐⇒


x
y
z

∈


8
−3
0

+ Span


−5
1
1

.
9

<!-- pagina 10 -->
Nome & Cognome:
(3) L’equazione T(t(x, y, z)) = t(1, k2, 2k) `e equivalente a A · t(x, y, z)) = t(1, k2, 2k),
allora a un sistema lineare con matrice completa


1
1
4
1
2
4
6
k2
1
−1
6
2k

.
Usando di nuovo la stessa riduzione a scalini come nella parte (1), si trova


1
1
4
1
2
4
6
k2
1
−1
6
2k

→


1
1
4
5
0
2
−2
k2 −2
0
0
0
k2 + 2k −3

.
Per il teorema di Rouch´e-Cappelli, il sistema ammette infinite soluzioni se e solo se
k2 + 2k −3 = (k + 3)(k −1) = 0, allora se e solo se k = −3 o k = 1.
10
