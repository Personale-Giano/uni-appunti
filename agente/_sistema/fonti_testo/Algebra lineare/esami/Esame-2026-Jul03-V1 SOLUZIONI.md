# Esame-2026-Jul03-V1 SOLUZIONI

<!-- pagina 1 -->
Nome & Cognome:
Algebra Lineare, Esame Finale
3 Luglio 2026
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
(•)
(c)
(d)
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
1.(1 pt.) Sia V = R3[x] lo spazio dei polinomi di grado al massimo tre a coeﬃcienti reali.
Consideriamo il sottoinsieme W = {p(x) ∈V | p(2) = 0, p(−2) = 0}. La dimensione di
W `e:
(a)
2.
(b)
W non `e sottospazio di V .
(c)
1.
(d)
4.
(e)
3.
Soluzione.
Poich´e p(2) = 0 e p(−2) = 0, il polinomio p(x) deve avere come fattori
(x −2) e (x + 2). Dunque
p(x) = (x −2)(x + 2)q(x) = (x2 −4)q(x),
dove q(x) ha grado al massimo 1, cio`e q(x) = ax+b. Quindi ogni elemento di W si scrive
come
p(x) = (x2 −4)(ax + b),
e dipende da due parametri liberi a, b ∈R. Ne segue che dim W = 2.
2.(1 pt.) Sia T : R2 →R2 l’endomorﬁsmo deﬁnito da T(t(x, y)) = t(2x + y, 3y). Quale
dei seguenti vettori `e un autovettore di T?
(a)

1
1

.
(b)

0
1

.
(c)

2
1

.
(d)
T non ha autovettori reali.
(e)

−1
1

.
Soluzione. Un vettore v `e un autovettore se T(v) = λv per qualche λ ∈R. Possiamo
o trovare tutti gli autovettori con il metodo standard, o proviamo semplicemente con i
quattro vettori dati. Per
v =

1
1

,
si ottiene
T

1
1

=

2 · 1 + 1
3 · 1

=

3
3

= 3

1
1

.
2

<!-- pagina 3 -->
Nome & Cognome:
Quindi il vettore in (a) `e un autovettore. Nello stesso modo, si vede che gli altri vettori
non sono autovettori, per esempio per il vettore in (b) si ottiene
T

0
1

=

2 · 0 + 1
3 · 1

=

1
3
̸
= λ

0
1

per qualsiasi λ (e simile per i vettori in (c) e (e)).
3.(1 pt.) Trovare l’insieme degli autovalori dell’endomorﬁsmo T : R3 →R3 dato da
T(t(x, y, z)) = t(2x, x + 3y, z):
(a)
T non ammette autovalori reali.
(b)
{1, 2}.
(c)
{1, 2, 3}.
(d)
{2, 3}.
(e)
{0, 1, 5}.
Soluzione. L’applicazione lineare T ha matrice associata
A =


2
0
0
1
3
0
0
0
1

.
Questa matrice `e triangolare, quindi i suoi autovalori sono gli elementi sulla diagonale
principale. Pertanto gli autovalori sono 1, 2, 3 e la risposta corretta `e (c).
4.(1 pt.) Si consideri l’applicazione lineare T : R2[x] →R3 data da
T(ax2 + bx + c) =


a + b
a + b
c

.
Qual `e la dimensione dell’immagine Im(T)?
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
Soluzione.
Dalla deﬁnizione di T, si vede che i vettori dell’immagine hanno tutti la
forma


s
s
t

,
s, t ∈R
(dove s = a + b e t = c). Ci sono dunque due parametri liberi, e quindi dim(Im(T)) = 2.
La risposta corretta `e (e).
3

<!-- pagina 4 -->
Nome & Cognome:
5.(1 pt.) Dati spazi vettoriali U, V, W, siano S : U →V e T : V →W applicazioni
lineari tali che T ◦S(u) = 0W per ogni u ∈U. Quale delle seguenti informazioni si pu`o
dedurre:
(a)
ker(T) ⊆Im(S).
(b)
Im(S) = ker(T).
(c)
Im(S) = V .
(d)
Im(S) ⊆ker(T).
(e)
ker(S) ⊆Im(T).
Soluzione. L’ipotesi (T ◦S)(u) = 0W per ogni u ∈U signiﬁca che, per ogni u ∈U,
il vettore S(u) ∈V viene mandato da T nel vettore nullo. Quindi ogni vettore S(u)
dell’immagine di S appartiene al nucleo di T. In altre parole,
Im(S) ⊆ker(T).
La risposta corretta `e la (d).
6.(1 pt.) Sia A ∈M(3, R) la matrice
A =


1
0
2
3
−1
1
2
0
5

.
Il determinante di A3 `e:
(a)
−8.
(b)
−1.
(c)
0.
(d)
1.
(e)
8.
Soluzione. Usiamo la propriet`a det(A3) = (det A)3. Calcoliamo prima det A: svilup-
pando lungo la seconda colonna, otteniamo
det A = 0 + (−1) det

1
2
2
5

+ 0 = (−1)(5 −4) = −1.
Dunque det(A3) = (−1)3 = −1. La risposta corretta `e la (b).
4

<!-- pagina 5 -->
Nome & Cognome:
7.(1 pt.) Quale dei seguenti `e una radice del polinomio p(z) = z3 + 2z2 + z + 2?
(a)
z = 0.
(b)
z = i.
(c)
z = 1 + i.
(d)
z = 1.
(e)
z3 + 2z2 + z + 2 = 0.
Soluzione. Osserviamo che
p(z) = z3 + 2z2 + z + 2 = z2(z + 2) + 1(z + 2) = (z2 + 1)(z + 2).
Le radici sono quindi
z = −2,
z = i,
z = −i.
Tra le alternative proposte compare solo z = i. La risposta corretta `e la (b).
Alternativamente, si potrebbe sostituire le risposte di (a), (b), (c), (d) nel polinomio e
controllare se si ottiene 0, per esempio per z = i e per z = 1 si ottiene
p(i) = i3 + 2i2 + i + 2 = (−i) −2 + i + 2 = 0
p(1) = 13 + 2 · 12 + 1 + 2 = 1 + 2 + 1 + 2 = 6̸ = 0
e quindi la risposta z = i e corretta, mentre z = 1 `e sbagliata.
8.(1 pt.) In R3, l’intersezione della retta r = t(1, 0, 1) + Span t(1, 1, −2) con il piano
π = {x −y + z = 2} `e:
(a)
Tutta la retta r.
(b)
P =


2
1
−1

.
(c)
Tutto il piano π.
(d)
P =


1
0
1

.
(e)
Vuota.
Soluzione. La retta in forma parametrica `e data da
x = 1 + t,
y = t,
z = 1 −2t.
Sostituendo nell’equazione del piano, otteniamo
(1 + t) −t + (1 −2t) = 2,
cio`e 2 −2t = 2 o equivalentemente t = 0. Dunque il punto di intersezione `e t(1, 0, 1). La
risposta corretta `e la (d).
5

<!-- pagina 6 -->
Nome & Cognome:
9.(1 pt.) Siano A, B ∈M(2, R) deﬁnite da A =

1
−2
0
3

e B =

2
1
−1
0

. La traccia
della matrice prodotto AB `e uguale a:
(a)
4.
(b)
6.
(c)
8.
(d)
5.
(e)
2.
Soluzione. Calcoliamo il prodotto
AB =

1
−2
0
3
 
2
1
−1
0

=

1 · 2 + (−2) · (−1)
1 · 1 + (−2) · 0
0 · 2 + 3 · (−1)
0 · 1 + 3 · 0

=

4
1
−3
0

.
La traccia `e la somma degli elementi diagonali, quindi tr(AB) = 4 + 0 = 4. La risposta
corretta `e la (a).
10.(1 pt.) In R2 si consideri la base
B =

2
1

,

1
1

.
Il vettore delle coordinate di w =

5
1

rispetto alla base B `e:
(a)
[w]B =

4
−3

.
(b)
[w]B =

2
1

.
(c)
[w]B =

5
1

.
(d)
[w]B =

3
2

.
(e)
[w]B =

1
1

.
Soluzione. Dobbiamo trovare α, β ∈R tali che
α

2
1

+ β

1
1

=

5
1

.
Questo equivale al sistema
(
2α + β = 5,
α + β = 1.
Sottraendo la seconda equazione dalla prima si ottiene α = 4, e quindi β = −3. Perci`o
[w]B =

4
−3

.
La risposta corretta `e la (a).
6

<!-- pagina 7 -->
Nome & Cognome:
Risposta aperta
Per ricevere punteggio parziale, dovete mostrare il vostro lavoro!
11.(11 pts.) Si consideri il sistema lineare:





x + ky + z = 1,
(k + 1)x + (k + 1)y + 2z = k + 1,
x + y + kz = k2.
(1) Determinare per quali valori di k ∈R la matrice dei coeﬃcienti del sistema `e
invertibile.
(2) Al variare di k ∈R, discutere il numero di soluzioni ammesse dal sistema lineare.
(3) Trovare esplicitamente l’insieme delle soluzioni nei casi k = 0 e k = 1.
Soluzione. (1) La matrice dei coeﬃcienti `e
A =


1
k
1
k + 1
k + 1
2
1
1
k


calcoliamo il determinante, prima applicando la terza mossa di Gauss lungo la prima
colonna, poi sviluppo di Laplace:
det


1
k
1
k + 1
k + 1
2
1
1
k

= det


1
k
1
0
(k + 1)(1 −k)
1 −k
0
1 −k
k −1

= det

(k + 1)(1 −k)
1 −k
1 −k
k −1

Quindi
det A = (k + 1)(1 −k)(k −1) −(1 −k)2 = −(k + 1)(1 −k)2 −(1 −k)2 = −(k + 2)(1 −k)2.
Pertanto la matrice dei coeﬃcienti `e invertibile se e solo se det A̸ = 0 ⇐⇒k̸ ∈{1, −2}.
(2) Quando la matrice A dei coeﬃcienti `e invertibile, il sistema Ax = b ha sempre
esattamente una soluzione, x = A−1b. In particolare per tutti i valori k ∈R \ {1, −2}
esiste una ed una sola soluzione. Dobbiamo discutere gli ultimi due casi separatamente.
Con le stesse mossi di Gauss come sopra otteniamo per la matrice completa


1
k
1
1
k + 1
k + 1
2
k + 1
1
1
k
k2

→


1
k
1
1
0
(k + 1)(1 −k)
1 −k
0
0
1 −k
k −1
k2 −1

.
7

<!-- pagina 8 -->
Nome & Cognome:
Se k = 1 la seconda e la terza riga spariscono completamente. Con rk(A) = rk(A|b) = 1
deduciamo che il sistema ammette inﬁnite soluzioni che dipendono da 3−1 = 2 parametri.
Invece per k = −2 la matrice completa diventa


1
−2
1
1
0
−3
3
0
0
3
−3
3

→


1
−2
1
1
0
−3
3
0
0
0
0
3


e vediamo che rk(A)̸ = rk(A|b) e quindi il sistema non ammette soluzioni.
(3) Trattiamo prima il caso k = 0. Sappiamo gi`a che esiste esattamente una soluzione.
Il sistema diventa





x + z = 1,
x + y + 2z = 1,
x + y = 0.
Dalla terza equazione segue y = −x. Sostituendo nella seconda,
x + (−x) + 2z = 1
=⇒
2z = 1
=⇒
z = 1
2.
Dalla prima equazione segue allora
x = 1 −z = 1 −1
2 = 1
2,
e quindi y = −x = −1
2. La soluzione `e
(x, y, z) = (1
2, −1
2, 1
2).
Nel caso k = 1 abbiamo gi`a osservato sopra che il sistema si riduce a una equazione:
x + y + z = 1.
Quindi l’insieme delle soluzioni `e
{(x, y, z) = (1 −s −t, s, t) : s, t ∈R} .
8

<!-- pagina 9 -->
Nome & Cognome:
12.(11 pts.) Su V = R3, deﬁniamo il prodotto scalare gS associato alla matrice:
S =


2
1
0
1
2
0
0
0
1


(1) Siano u = t(1, 0, 1) e v = t(1, 1, 0). Calcolare le norme ∥u∥gS, ∥v∥gS e il coseno
dell’angolo compreso tra i due vettori rispetto al prodotto scalare gS.
(2) Trovare una base ortonormale per W = Span(u, v) rispetto a gS.
(3) Trovare una base del complemento ortogonale di W rispetto a gS.
Soluzione. (1) Per deﬁnizione del prodotto scalare gS si ha
⟨x, y⟩gS = txSy.
Calcoliamo le norme:
∥u∥2
gS = tuSu =
 1
0
1


2
1
0
1
2
0
0
0
1




1
0
1

=
 1
0
1


2
1
1

= 3,
quindi ∥u∥gS =
√
3. Analogamente,
∥v∥2
gS = tvSv =
 1
1
0


2
1
0
1
2
0
0
0
1




1
1
0

=
 1
1
0


3
3
0

= 6,
perci`o ∥v∥gS =
√
6. Inﬁne,
⟨u, v⟩gS = tuSv =
 1
0
1


3
3
0

= 3.
Dunque il coseno dell’angolo tra u e v rispetto a gS `e
cos θ =
⟨u, v⟩gS
∥u∥gS∥v∥gS
=
3
√
3
√
6 = 1
√
2 =
√
2
2 .
(2) Vogliamo costruire una base ortonormale di W rispetto a gS. Possiamo applicare
Gram–Schmidt per ottenere prima due vettori ortogonali. Poniamo prima ew1 = u. Poi
deﬁniamo
ew2 = v −⟨v, u⟩gS
∥u∥2
gS
u = v −3
3u = v −u =


0
1
−1

.
9

<!-- pagina 10 -->
Nome & Cognome:
Allora una base ortonormale di W rispetto a gS `e dato da
w1 =
1
∥ew1∥gS
ew1 = 1
√
3 ew1 =
√
3
3


1
0
1


e
w2 =
1
∥ew2∥gS
ew2 = 1
√
3 ew2 =
√
3
3


0
1
−1

,
dove abbiamo usato ∥ew2∥2
gS = ⟨ew2, ew2⟩gS =
 0
1
−1


1
2
−1

= 3.
(3) Cerchiamo ora il complemento ortogonale di W rispetto a gS, cio`e
W ⊥= {x ∈R3 : ⟨x, u⟩gS = 0, ⟨x, v⟩gS = 0}.
Ponendo
x =


a
b
c

,
otteniamo le due condizioni
⟨x, u⟩gS = txSu =
 a
b
c


2
1
1

= 2a + b + c = 0,
e
⟨x, v⟩gS = txSv =
 a
b
c


3
3
0

= 3a + 3b = 0.
Quindi dobbiamo risolvere il sistema
(
2a + b + c = 0,
a + b = 0.
Dalla seconda equazione si ha b = −a; sostituendo nella prima otteniamo 2a −a + c = 0
e quindi c = −a. Dunque x = t(a, −a, −a). Segue che
W ⊥= Span





1
−1
−1





e una base del complemento ortogonale `e quindi data da





1
−1
−1




.
10
