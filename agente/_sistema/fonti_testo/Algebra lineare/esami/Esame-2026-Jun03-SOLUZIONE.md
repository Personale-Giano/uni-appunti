# Esame-2026-Jun03-SOLUZIONE

<!-- pagina 1 -->
Nome & Cognome:
Algebra Lineare, Esame Finale
3 Giugno 2026
• Tutto il lavoro deve essere unicamente vostro.
• L’utilizzo di calcolatrici `e vietato.
• Ognuno pu`o portare un foglio protocollo o due fogli A4 (in totale 4 facciate A4)
con formulario, appunti del corso, ecc. scritto a mano.
• L’esame dura 2 ore.
• Scrivete il vostro nome su tutte le pagine, nel caso qualche foglio si staccasse.
• Controllate di avere tutte le 11 pagine dell’esame.
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
1.(1 pt.) Se (1 + i)z = 2i allora
1
z+i `e uguale a
(a)
0.
(b)
1
1+i.
(c)
1−2i
5 .
(d)
i
1+i.
(e)
2+i
5 .
Soluzione. Da (1 + i)z = 2i otteniamo
z =
2i
1 + i =
2i(1 −i)
(1 + i)(1 −i) = 2i + 2
2
= 1 + i.
Concludiamo che
1
z + i =
1
1 + 2i =
1 −2i
(1 + 2i)(1 −2i) = 1 −2i
5
.
2.(1 pt.) Il determinante di




1
e
1
1
π
2πe
3π
π
1
e
2
0
0
e
0
3




`e uguale a:
(a)
1.
(b)
0.
(c)
πe.
(d)
π + e.
(e)
6 + 2πe.
Soluzione. Notiamo prima che ogni entrate nella seconda colonna `e multiplo di e e ogni
entrata nella seconda riga `e multiplo di π. Allora, usando anche le mosse di Gauss
det




1
e
1
1
π
2πe
3π
π
1
e
2
0
0
e
0
3



= πe · det




1
1
1
1
1
2
3
1
1
1
2
0
0
1
0
3



= πe · det




1
1
1
1
0
1
2
0
0
0
1
−1
0
1
0
3




= πe · det


1
2
0
0
1
−1
1
0
3

= πe(3 −2) = πe.
(Infatti, gi`a dalla prima uguaglianza si vede che il determinante `e multiplo di (πe) e allora
solo le risposte (b) e (c) sono possibili – e allora invece di calcolare il determinante basta
anche solo calcolare il rango.)
2

<!-- pagina 3 -->
Nome & Cognome:
3.(1 pt.) Dati polinomi p(x) = 1, q(x) = x + 1, r(x) = x3 + x + 1, quali dei seguenti
polinomi forma, insieme a p(x), q(x), r(x) una base di R3[x]?
(a)
s(x) = 1.
(b)
s(x) = 3x + 3.
(c)
s(x) = q(x) + x2.
(d)
s(x) = r(x) + 1.
(e)
s(x) = r(x) + q(x).
Soluzione.
Nessuno dei polinomi p(x), q(x), r(x) contiene un termine x2. Allora per
poter generare il polinomio x2, il polinomio s(x) deve per forza contenere un tale termine.
L’unica risposta possibile `e dunque (c). Alternativamente, si vede subito che i polinomi
nelle altre risposte sono tutti contenuti in Span(p(x), q(x), r(x)) mentre il polinomio della
risposta (c) non lo `e.
4.(1 pt.) Data la matrice
S =


2
1
1
1
1
0
1
0
1


la matrice associata al prodotto scalare gS(x, y) = txSy rispetto alla base
B = {t(1, 0, 0), t(0, 2, 0), t(0, 0, 3)}
`e data da:
(a)


2
1
1
1
2
0
0
0
3

.
(b)


2
1
1
2
2
0
3
0
3

.
(c)


1
0
0
0
2
0
0
0
3

.
(d)


2
1
1
1
1
0
1
0
1

.
(e)


2
2
3
2
4
0
3
0
9

.
Soluzione. Scrivendo B = {v1, v2, v3} = {e1, 2e2, 3e3}, calcoliamo
[gS]B =


gs(v1, v1)
gs(v1, v2)
gs(v1, v3)
gs(v2, v1)
gs(v2, v2)
gs(v2, v3)
gs(v3, v1)
gs(v3, v2)
gs(v3, v3)

=


gs(e1, e1)
2gs(e1, e2)
3gs(e1, e3)
2gs(e2, e1)
4gs(e2, e2)
6gs(e2, e3)
3gs(e3, e1)
6gs(e3, e2)
9gs(e3, e3)


=


S11
2S12
3S13
2S21
4S22
6S23
3S31
6S32
9S33

=


2
2 · 1
3 · 1
2 · 1
4 · 1
6 · 0
3 · 1
6 · 0
9 · 1

=


2
2
3
2
4
0
3
0
9

.
3

<!-- pagina 4 -->
Nome & Cognome:
Soluzione alternativa. Denotiamo la base canonica con A, cosicch´e [gS]A = S, e la
matrice del cambio di base da B ad A `e
M = [I]B
A = [v1|v2|v3] =


1
0
0
0
2
0
0
0
3


Usando la formula per il cambio di base:
[gS]B = tM[gS]AM =


1
0
0
0
2
0
0
0
3




2
1
1
1
1
0
1
0
1




1
0
0
0
2
0
0
0
3

=


2
2
3
2
4
0
3
0
9


5.(1 pt.) Date
A =


0
1
1
0
0
1
0
0
0

,
B =


2
2
3
0
1
0
0
0
1


Quale identit`a vale:
(a)
AB = BA.
(b)
AB = B.
(c)
AB = I.
(d)
AB = A.
(e)
AB = 0.
Soluzione. Il prodotto AB (“prodotto righe per colonne”) si calcola
AB =


0 · 2 + 1 · 0 + 1 · 0
0 · 2 + 1 · 1 + 1 · 0
0 · 3 + 1 · 0 + 1 · 1
0 · 2 + 0 · 0 + 1 · 0
0 · 2 + 0 · 1 + 1 · 0
0 · 3 + 0 · 0 + 1 · 1
0 · 2 + 0 · 0 + 0 · 0
0 · 2 + 0 · 1 + 0 · 0
0 · 3 + 0 · 0 + 0 · 1

=


0
1
1
0
0
1
0
0
0

.
La risposta corretta `e allora la (d). (In realt`a, a questo punto anche la (a) potrebbe essere
corretta, ma calcolando qualche entrata di BA si nota subito che il risultato `e diverso e
allora si pu`o escludere la (a).)
6.(1 pt.) L’applicazione lineare T : R2 →R2, T

x
y

=

3x
x + 2y

, ha autovalori 3 e
2. La base di autovettori corrispondente, `e:
(a)
B = {t(3, 0), t(0, 2)}.
(b)
B = {t(1, 1), t(0, 1)}.
(c)
B = {t(3, 0), t(1, 2)}.
(d)
B = {t(3, 1), t(0, 2)}.
(e)
B = {t(1, 1), t(2, 2)}.
Soluzione. La matrice associata a T nella base canonica A `e
[T]A
A =

3
0
1
2

.
4

<!-- pagina 5 -->
Nome & Cognome:
Visto che questa matrice `e triangolare, gli autovalori sono esattamente gli elementi sulla
diagonale, cio`e 3 e 2 (come dato nel testo della domanda). Per trovare un autovettore
che corrisponde all’autovalore 3 risolviamo per v =t (x, y)
(A −3I2)v = 0 ⇔

0x + 0y = 0
1x −1y = 0 ⇔x = y ↔v ∈Span(t(1, 1)).
Simile, per l’autovalore 2 troviamo
(A −2I2)v = 0 ⇔

1x + 0y = 0
1x + 0y = 0 ⇔x = 0 ↔v ∈Span(t(0, 1)).
La base corretta `e allora quella della risposta (b).
7.(1 pt.) Il sistema lineare con matrice completa
A =


3
9
6
12
4
12
8
16
2
6
4
8


ha un numero di soluzioni pari a:
(a)
Infinite, che dipendono da 1 parametro.
(b)
Zero.
(c)
Un numero finito, maggiore di 1.
(d)
Infinite, che dipendono da 2 parametri.
(e)
Una.
Soluzione. Usiamo mosse di Gauss. Prima dividiamo la prima riga per 3, la seconda
per 4 e l’ultima per 2.


3
9
6
12
4
12
8
16
2
6
4
8

→


1
3
2
4
1
3
2
4
1
3
2
4


Notiamo che tutte le righe sono uguali (allora la seconda e la terza si eliminano con
l’algoritmo di Gauss). Per il teorema di Rouch´e-Capelli il sistema ammette soluzione e la
dimensione dello spazio di soluzioni `e n −rk(A) = 3 −1 = 2. La risposta (d) `e corretta.
8.(1 pt.) Sia data la seguente base dello spazio S2(R) di matrici simmetriche 2 × 2:
B =

E1 =

1
1
1
0

, E2 =

0
1
1
1

, E3 =

0
1
1
0

Il vettore [I2]B delle coordinate della matrice identit`a nella base B, `e:
5

<!-- pagina 6 -->
Nome & Cognome:
(a)
t(1, 1, 0).
(b)
t(E1, E2, E3).
(c)
t(1, 1, 1).
(d)
t(1, 1, −2).
(e)

1
0
0
1

.
Soluzione. Il vettore delle coordinate `e t(a, b, c) se
aE1 + bE2 + cE3 = I2 ⇔

a
a + b + c
a + b + c
b

=

1
0
0
1

⇔a = b = 1, c = −2.
6

<!-- pagina 7 -->
Nome & Cognome:
9.(1 pt.) Quale delle seguenti applicazioni lineari T : R2 →R2 `e autoaggiunta rispetto
al prodotto scalare Euclideo?
(a)
T(x, y) = (2x −y, −x + y).
(b)
T(x, y) = (x −y, x + y).
(c)
T(x, y) = (x, x).
(d)
T(x, y) = (−x + y, 2x −y).
(e)
T(x, y) = (x + y, y).
Soluzione. Sappiamo che l’applicazione T `e autoaggiunta se e solo se la matrice [T]A
A
`e simmetrica in ogni base ortonormale. In particolare possiamo usare la base canonica.
Nella base canonica, la matrice dell’applicazione della risposta (a) diventa

2
−1
−1
1

.
Questa matrice `e simmetrica e allora l’applicazione `e autoaggiunta. (Si vede velocemente
che per tutte le altre risposte le matrici associate non sono simmetriche.)
10.(1 pt.) La distanza tra le due rette
r1 = t(2, 1, 1) + Span(t(1, 2, 0)),
r2 = t(1, 1, 1) + Span(t(2, 3, 4))
`e:
(a)
0.
(b)
2
3.
(c)
8
9.
(d)
−2
3.
(e)
1.
Soluzione. Con la notazione
P1 = t(2, 1, 1),
v1 = t(1, 2, 0),
P2 = t(1, 1, 1),
v2 = t(2, 3, 4).
abbiamo la formula per rette sghembe
d(r1, r2) = |(P2 −P1) · (v1 × v2)|
∥v1 × v2∥
.
Calcoliamo
P2 −P1 = t(−1, 0, 0),
v1 × v2 = t(1, 2, 0) × t(2, 3, 4) = t(8, −4, −1),
e allora
d(r1, r2) = |t(−1, 0, 0) · (8, −4, −1)|
p
82 + (−4)2 + (−1)2
= 8
9.
7

<!-- pagina 8 -->
Nome & Cognome:
Risposta aperta
Per ricevere punteggio parziale, dovete mostrare il vostro lavoro!
11.(11 pts.) Si consideri la seguente matrice parametrica A ∈M3(C):
A =


k
0
−2
0
0
1
0
−1
0


(1) Posto k = i, si calcolino gli autovalori della matrice A, specificando per ciascuno la
molteplicit`a algebrica e geometrica, e una base per ogni autospazio. Si stabilisca,
quindi, se la matrice `e diagonalizzabile per questo valore di k.
(2) Si determini per quali valori del parametro k ∈C la matrice A `e diagonalizzabile
sopra il campo dei numeri complessi.
Soluzione. 1) Per k = i la matrice diventa
A =


i
0
−2
0
0
1
0
−1
0


e il polinomio caratteristico `e
pA(t) = det


i −t
0
−2
0
0 −t
1
0
−1
−t

= (i−t) det

0 −t
1
−1
−t

= (i−t)(t2−1) = −(t−i)2(t+i)
Gli autovalori di A sono quindi i e −i, con molteplicit`a algebriche
ma(i) = 2,
ma(−i) = 1.
Per λ = i, Ei(A) `e lo spazio delle soluzioni del sistema (A −iI)v = 0, con matrice dei
coefficienti
A −iI =


0
0
−2
0
−i
1
0
−1
−i

→


0
−i
1
0
0
−2
0
−1
−i

R3→iR3
−→


0
−i
1
0
0
−2
0
−i
1

→


0
−i
1
0
0
−2
0
0
0


e pertanto il sistema diventa

−2z = 0
−iy + z = 0
⇒



x = x
y = 0
z = 0
⇒Ei(A) =





x
0
0


 x ∈R


= Span





1
0
0





8

<!-- pagina 9 -->
Nome & Cognome:
Per λ = −i, E−i(A) contiene soluzioni di (A + iI)v = 0, con matrice dei coefficienti


2i
0
−2
0
i
1
0
−1
i

R3→iR3
−→


2i
0
−2
0
i
1
0
−i
−1

→


2i
0
−2
0
i
1
0
0
0


e pertanto il sistema diventa

2ix −2z = 0
iy + z = 0
⇒



x = −iz
y = iz
z = z
⇒Ei(A) =





−iz
iz
z


 x ∈R


= Span





−i
i
1





Poich`e Ei(A) ha una base di 1 solo elemento, mg(i) = 1̸ = 2 = ma(i) quindi A non `e
diagonalizzabile.
2) Calcoliamo gli autovalori di A al variare di k:
pA(t) = det


k −t
0
−2
0
0 −t
1
0
−1
−t

= (i−t) det

0 −t
1
−1
−t

= (k−t)(t2−1) = (k−t)(t−i)(t+1)
per k̸ = ±i, A ha tre autovalori distindi ed `e pertanto diagonalizzabile. Per il punto prece-
dente, se k = i la matrice non `e diagonalizzabile. Basta verificare la diagonalizzabilit`a se
k = −i. In questo caso
ma(i) = 1,
ma(−i) = 2
Poich´e 1 ≤mg(λ) ≤ma(λ) per ogni autovalore λ, si ha mg(i) = 1.
Per λ = −i,
ricordiamo che mg(−i) = 3 −rk(A + iI), e
A + iI =


0
0
−2
0
i
1
0
−1
i

→


0
i
1
0
0
−2
0
−1
i

R3→iR3
−→


0
i
1
0
0
−2
0
−i
−1

→


0
i
1
0
0
−2
0
0
0


Pertanto rk(A + iI) = 2, e mg(−i) = 1̸ = 2 = ma(−i). La matrice A pertanto non `e
diagonalizzabile per k = −i.
9

<!-- pagina 10 -->
Nome & Cognome:
12.(11 pts.) Siano v1 =


1
1
0

e v2 =


0
1
1

due vettori in R3.
(1) Si calcoli una base ortonormale del sottospazio V := Span(v1, v2).
(2) Si determini la proiezione ortogonale del vettore w =


2
1
2

sul sottospazio V .
(3) Si consideri la retta r definita da:
r =


2
0
1

+ Span(w)
Si calcoli il punto di intersezione tra la retta r e il piano V , e si determini il coseno
dell’angolo di intersezione tra la retta e il piano stesso.
Soluzione. 1) Anzitutto applichiamo Gram Smith per produrre una base ortogonale
{u1, u2}: u1 = v1, mentre
u2 = v2 −⟨v1, v2⟩
∥v1∥2 v1 =


0
1
1

−1
2


1
1
0

=


−1/2
1/2
1


La base ortonormale {v′
1, v′
2} si ottiene normalizzando u1, u2:
v′
1 =
1
∥u1∥u1 = 1
√
2


1
1
0


v′
2 =
1
∥u2∥u2 =
√
2
√
3


−1/2
1/2
1

= 1
√
6


−1
1
2


2) La proiezione di w su V := Span(v1, v2) = Span(v′
1, v′
2) (sapendo che v′
1, v′
2 formano
una base ortonormale) si calcola come:
prV (w) = ⟨w, v′
1⟩v′
1 + ⟨w, v′
2⟩v′
2 = 3
√
2v′
1 + 3
√
6v′
2 = 3
2


1
1
0

+ 3
6


−1
1
2

=


1
2
1


3) I punti di r sono della forma


x
y
z

=


2 + 2t
t
1 + 2t


questi intersecano V se si possono scrivere nella forma


x
y
z

= s1v1 + s2v2 =


s1
s1 + s2
s2


10

<!-- pagina 11 -->
Nome & Cognome:
Unendo le due equazioni, si ottiene il sistema (in t, s1, s2) dato da:



2 + 2t = s1
t = s1 + s2
1 + 2t = s2
che ha come soluzione t = −1, s1 = 0, s2 = −1. Sostituento s1, s2 nel piano si ottiene
che il punto di intersezione `e:
P = −v2 =


0
−1
−1


Il coseno dell’angolo di intersezione e’ dato dal coseno dell’angolo tra w e la sua proiezione
su V :
cos θ = ⟨prV (w), w⟩
∥w∥∥prV (w)∥=
6
3
√
6 =
√
2
√
3
11
