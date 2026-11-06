# dispense_MDAG

<!-- pagina 1 -->
MDAG Parte II: Algebra Lineare e Geometria
Prof. Reto Buzano e Prof. Marco Radeschi
Autunno 2026, Università di Torino
Contents
1
Numeri Reali
2
2
Numeri Complessi I
6
3
Numeri Complessi II
10
4
Polinomi
15
5
Spazi Vettoriali I
20
6
Spazi Vettoriali II
26
7
Spazi Vettoriali III
31
8
Matrici I
36
9
Matrici II
41
10 Matrici III
46
11 Sistemi Lineari I
50
12 Sistemi Lineari II
56
13 Sistemi Lineari III
62
14 Applicazioni Lineari I
68
15 Applicazioni Lineari II
74
16 Applicazioni Lineari III
79
17 Autovalori e Autovettori I
85
18 Autovalori e Autovettori II
90
19 Prodotti Scalari I
96
20 Prodotti Scalari II
100
21 Prodotti Scalari III
105
22 Lo Spazio Euclideo I
111
23 Lo Spazio Euclideo II
116
24 Lo Spazio Euclideo III
122
25 Teorema Spettrale I
129
26 Teorema Spettrale II
134
1

<!-- pagina 2 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
1
Numeri Reali
1.A
Gli insiemi numerici
La teoria degli insiemi è trattata in più dettaglio nella parte di Matematica Discreta del corso. A
noi servono al momento solo gli insiemi numerici N, Z, Q, R, e C.
Un insieme è spesso indicato con due parentesi graﬀe {}, all’interno delle quali sono descritti tutti
i suoi elementi. A volte si descrivono solo alcuni elementi e si usano dei puntolini ... per indicare
il resto (in particolare se l’insieme ha un numero inﬁnito di elementi). Ecco qualche esempio.
Deﬁnizione 1.1 (Numeri naturali, interi e razionali)
L’insieme dei numeri naturali è
N = {0, 1, 2, 3, . . .}
Se aggiungiamo i numeri negativi otteniamo l’insieme dei numeri interi
Z = {. . . , −2, −1, 0, 1, 2, . . .}.
Se oltre ai numeri interi consideriamo tutti i numeri esprimibili come frazioni a
b, otteniamo
l’insieme dei numeri razionali
Q =
na
b ; a, b ∈Z, b̸ = 0
o
.
Questi insiemi numerici dovrebbero già essere familiari ﬁn dalle scuole superiori. Da un punto di
vista più rigoroso, l’insieme N è un concetto primitivo, mentre gli insiemi Z e Q sono costruiti
ciascuno a partire dal precedente in un modo opportuno. Per esempio per una costruzione precisa
dei numeri razionali dobbiamo dichiarare che le frazioni 1
7,
3
21, o
−8
−56 rappresentano tutti lo stesso
numero. Per rendere questo preciso, ci serve il concetto di una relazione di equivalenza – anche
questo concetto viene trattato in dettaglio nella parte di Matematica Discreta del corso.
1.B
Costruzione dell’insieme R
Sappiamo inoltre che in aritmetica esiste un insieme ancora più grande, chiamato R, formato da
tutti i numeri reali. La costruzione dei numeri reali è abbastanza complessa. A scuola impariamo
che un numero reale è un numero che può avere inﬁnite cifre dopo la virgola. Questa deﬁnizione
è corretta (c’è solo una piccola ambiguità da tenere a mente, riguardante il fatto che numeri del
tipo 5, 973¯9 e 5, 974 sono in realtà lo stesso) ma non ci dice nulla su come siano deﬁnite la somma
ed il prodotto di due numeri reali. Per deﬁnire somma e prodotto è più comodo deﬁnire i numeri
reali in un altro modo, che ha anche il pregio di essere più intrinseco ed indipendente dalla scelta
della base 10 (che abbiamo adottato solo perché la selezione naturale ci ha gentilmente fornito di
10 dita) usando il linguaggio dell’analisi.
Una successione di Cauchy di numeri razionali è una successione (an) di numeri razionali an ∈Q
con questa proprietà: per ogni numero razionale ε > 0 esiste un N > 0 per cui
|am −an| < ε
2

<!-- pagina 3 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
per ogni m, n > N. Intuitivamente, una successione di Cauchy di numeri razionali è una succes-
sione che vorrebbe tendere a qualcosa ma non è detto che il limite esista: se il limite non c’è, lo
dobbiamo creare, e lo facciamo in modo astratto usando le successioni stesse per deﬁnire nuovi
numeri. I numeri reali sono deﬁniti come classi di equivalenza di successioni di Cauchy di numeri
razionali. Due successioni di Cauchy sono equivalenti se la diﬀerenza è una successione che tende
a zero.
In modo meno astratto, la procedura funziona così: Sia (an) una successione di Cauchy di nu-
meri razionali. Se questa converge ad un numero razionale a∞, allora la successione rappresenta
semplicemente il numero a∞. Se invece non converge a nessun numero razionale, rappresenta un
nuovo numero reale, che non è contenuto in Q, un numero irrazionale.
Esempio 1.2
Un numero reale π ha sviluppo decimale
3, 1415926... . . .
Questo numero corrisponde ad una successione di Cauchy (an) di numeri razionali
a1 = 3, 1
a2 = 3, 14
a3 = 3, 141
a4 = 3, 1415
. . .
La successione che deﬁnisce questo numero reale chiaramente non è unica.
Esempio 1.3
La successione di numeri razionali
an =

1 + 1
n
n
è una successione di Cauchy che non converge ad un numero razionale.
Quindi essa stessa
deﬁnisce un nuovo numero reale e, il numero di Eulero.
Intuitivamente possiamo lavorare con l’idea che ogni numero reale può essere approssimato
(con precisione arbitraria) con numeri razionali come nell’esempio precedente e che con questa
costruzione abbiamo “tappato” tutti i “buchi” tra i numeri razionali. Infatti, a diﬀerenza di Q,
l’insieme R dei numeri reali è completo: ogni successione di Cauchy in R converge.
Questo
vuol dire che se facciamo la stessa costruzione di prima con successioni in R invece di Q, non
aggiungiamo più nessun altro numero.
3

<!-- pagina 4 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
1.C
Numeri irrazionali
Abbiamo
N ⊊Z ⊊Q ⊊R
Per vedere che Q̸ = R, possiamo subito convincerci del fatto che molti numeri reali che ci sono
familiari non sono razionali. Quella che segue è la prima proposizione del corso ed è illuminante
perché contiene un esempio di dimostrazione per assurdo.
Proposizione 1.4
Il numero
√
2 non è razionale.
Dimostrazione. Supponiamo per assurdo che
√
2 sia razionale. Allora
√
2 = a
b, dove a
b è una
frazione. Possiamo assumere che la frazione è sempliﬁcata ai minimi termini. Elevando al quadrato
e moltiplicando per b2 entrambi i membri otteniamo
a2 = 2b2.
Questa ci dice che a2 è pari. Ma allora a è anche pari, allora a = 2k e a2 = 4k2. Da questo
otteniamo
b2 = 2k2.
Allora anche b è pari. Per questo motivo a
b non è una frazione sempliﬁcata ai minimi termini.
1.D
Proprietà di R
Proposizione 1.5
Su R ci sono due operazioni binarie + e · con le seguenti proprietà:
1. esiste l’elemento neutro 0 per l’addizione +, per cui 0 + a = a + 0 = a, ∀a ∈R.
2. vale la proprietà commutativa a + b = b + a, ∀a, b ∈R.
3. vale la proprietà associativa a + (b + c) = (a + b) + c, ∀a, b, c ∈R.
4. ogni elemento a ∈R ha un inverso (o opposto) −a, per cui a + (−a) = (−a) + a = 0.
5. esiste l’elemento neutro 1 per la moltiplicazione ·, per cui 1 · a = a · 1 = a, ∀a ∈R.
6. vale la proprietà commutativa a · b = b · a, ∀a, b ∈R.
7. vale la proprietà associativa a · (b · c) = (a · b) · c, ∀a, b, c ∈R.
8. ogni elemento a ∈R con a̸ = 0 ha un inverso a−1, per cui a · a−1 = a−1 · a = 1.
9. vale la proprietà distributiva a · (b + c) = a · b + a · c, ∀a, b, c ∈R.
Un insieme con queste proprietà si chiama un campo. Discuteremo questo concetto in più det-
taglio nel futuro. Invece di scrivere a · b, scriviamo spesso solo ab.
4

<!-- pagina 5 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Un altro aspetto fondamentale di R, e anche degli insiemi numerici N, Z e Q, è che questi insiemi
sono ordinati: esiste una nozione di maggiore e minore fra numeri, per cui se a, b sono due numeri
distinti deve valere a > b oppure b > a. In generale diciamo che a > b se a −b > 0, quindi per
deﬁnire questa nozione è suﬃciente chiarire quali siano i numeri positivi (cioè maggiori di zero)
e quali i numeri negativi (minori di zero). In Z, quelli positivi sono 1, 2, 3, . . .. In Q, i numeri
positivi sono le frazioni a
b in cui a e b hanno lo stesso segno. In R, un numero è positivo se è
rappresentabile da una successione di Cauchy (an) di numeri razionali per la quale esiste un numero
razionale ε > 0 tale che an > ε deﬁnitivamente.
1.E
Un commento sulla notazione
Abbiamo usato parentesi graﬀe {} per un insieme. Per esempio,
{1, 2}
denota l’insieme che ha esattamente due elementi: il numero 1 e il numero 2. Altre parentesi
possono avere un signiﬁcato molto diverso. Per esempio con
(1, 2)
denotiamo l’intervallo aperto di tutti i numeri strettamente tra 1 e 2 (cioè, 1 e 2 non inclusi) e
con
[1, 2]
denotiamo l’intervallo chiuso di tutti i numeri tra 1 e 2 con questi due elementi inclusi.
In
particolare, anche (1, 2) e [1, 2] sono insiemi, ma contengono un numero inﬁnito di elementi.
Possiamo scrivere
(1, 2) = {x ∈R | 1 < x < 2},
[1, 2] = {x ∈R | 1 ≤x ≤2}.
In questo corso, denotiamo con (1, 2) anche un punto nel piano R2 o un vettore. In particolare,
la stessa notazione può avere un signiﬁcato molto diverso che dovrebbe essere chiaro dal contesto.
È però essenziale usare sempre la notazione giusta (per esempio, non usiamo mai {1, 2} per de-
notare punti in R2 o vettori).
Un altro commento è che usiamo regolarmente lettere dell’alfabeto greco. In particolare si dovreb-
bero imparare queste 9 lettere:
α (alpha),
ε (epsilon),
σ (sigma),
ϑ (theta),
ϕ (phi),
π (pi),
λ (lambda),
µ (mu),
ϱ (rho).
5

<!-- pagina 6 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
2
Numeri Complessi I
2.A
Numeri complessi
I numeri complessi sono un ampliamento dell’insieme dei numeri reali R, costruito con lo scopo di
ottenere migliori proprietà algebriche.
Deﬁnizione 2.1 (Numeri complessi)
Un numero complesso è un oggetto algebrico che si scrive nel modo seguente:
a + bi
dove a e b sono numeri reali arbitrari e i è un nuovo simbolo chiamato unità immaginaria.
Ad esempio, questi sono numeri complessi:
√
7,
2 + i,
23i,
4 −i,
−1 + πi
I numeri complessi si sommano e si moltiplicano nel modo usuale, tenendo a mente un’unica nuova
relazione:
i2 = −1.
La somma e la moltiplicazione di due numeri complessi a + bi e c + di si svolge quindi nel modo
seguente:
(a + bi) + (c + di) = a + c + (b + d)i
(a + bi) · (c + di) = ac + bci + adi + bdi2 = ac −bd + (ad + bc)i.
Nel prodotto abbiamo usato che i2 = −1. Ad esempio:
(7 + i) · (4 −i) = 29 −3i
L’insieme dei numeri complessi è indicato con il simbolo C. Abbiamo esteso la nostra sequenza di
insiemi numerici:
N ⊊Z ⊊Q ⊊R ⊊C
2.B
Proprietà di C
Proposizione 2.2
Con l’addizione e la moltiplicazione deﬁnite sopra, l’insieme C ha le seguenti proprietà:
1. esiste l’elemento neutro 0 per l’addizione +, per cui 0 + a = a + 0 = a, ∀a ∈C.
2. vale la proprietà commutativa a + b = b + a, ∀a, b ∈C.
3. vale la proprietà associativa a + (b + c) = (a + b) + c, ∀a, b, c ∈C.
4. ogni elemento a ∈C ha un inverso (o opposto) −a, per cui a + (−a) = (−a) + a = 0.
5. esiste l’elemento neutro 1 per la moltiplicazione, per cui 1 · a = a · 1 = a, ∀a ∈C.
6

<!-- pagina 7 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
6. vale la proprietà commutativa a · b = b · a, ∀a, b ∈C.
7. vale la proprietà associativa a · (b · c) = (a · b) · c, ∀a, b, c ∈C.
8. ogni elemento a ∈C con a̸ = 0 ha un inverso a−1, per cui a · a−1 = a−1 · a = 1.
9. vale la proprietà distributiva a · (b + c) = a · b + a · c, ∀a, b, c ∈C.
Allora, come R, anche C è un campo.
Una diﬀerenza fondamentale tra C e tutti gli insiemi numerici visti prima (N, Z, Q e R), è che
C non è ordinato: non esiste una nozione di maggiore e minore fra numeri complessi! [Si può
dimostrare che in un campo ordinato un quadrato è sempre positivo, ma qui i2 = −1 è negativo.]
2.C
Coniugio, modulo e inverso
Sia z = a + bi un numero complesso. I numeri a e b sono detti rispettivamente la parte reale e la
parte immaginaria di z. Scriviamo a = Re(z) e b = Im(z). Il numero z è reale, cioè appartiene
al sottoinsieme R ⊂C, se e solo se la sua parte immaginaria è nulla. Il coniugio (o coniugato)
di z = a + bi è il numero complesso
¯z = a −bi
ottenuto da z cambiando il segno della sua parte immaginaria. Notiamo che z = ¯z precisamente
quando b = 0, cioè quando z è reale. Scriviamo quindi
z ∈R ⇐⇒z = ¯z.
Il modulo di z = a + bi è il numero reale
|z| =
p
a2 + b2.
Il modulo |z| è nullo quando z = 0, cioè quando a = b = 0, ed è strettamente positivo se z̸ = 0.
Notiamo inoltre che
z · ¯z = (a + bi) · (a −bi) = a2 + b2 = |z|2.
Mostriamo adesso un fatto non banale: come nei numeri razionali e reali, ogni numero complesso
z̸ = 0 ha un inverso z−1 rispetto all’operazione di moltiplicazione, dato da
z−1 =
¯z
|z|2
Infatti se moltiplichiamo z e z−1 otteniamo
z · z−1 = z¯z
|z|2 = |z|2
|z|2 = 1.
7

<!-- pagina 8 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 2.3
L’inverso di i è −i, infatti i · (−i) = 1. L’inverso di 2 + i è
(2 + i)−1 =
2 −i
|2 + i|2 = 2 −i
5
.
Si veriﬁca che eﬀettivamente
(2 + i) · 2 −i
5
= 1.
2.D
Il piano complesso
Mentre i numeri reali R formano una retta, i numeri complessi C formano un piano detto piano
complesso. Ogni numero complesso a + bi può essere identiﬁcato con il punto di coordinate (a, b)
nel piano cartesiano o equivalentemente come un vettore applicato nell’origine 0 e diretto verso
(a, b), come illustrato nella Figura 1.
Gli assi delle ascisse e delle ordinate sono rispettivamente l’asse reale e l’asse immaginario di C.
L’asse reale è precisamente il sottoinsieme R ⊂C formato dai numeri reali. L’asse immaginario
consiste di tutti i numeri complessi del tipo bi al variare di b ∈R.
La somma z1 + z2 di due numeri complessi z1 e z2 viene calcolata interpretando z1 e z2 come
vettori e sommandoli quindi con l’usuale regola del parallelogramma, come mostrato nella Figura 2.
Il prodotto z1 · z2 di due numeri complessi è apparentemente più complicato, ma può essere
visualizzato agevolmente usando le coordinate polari – lo vediamo in Lezione 3.
Figura 1. Il piano complesso.
8

<!-- pagina 9 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Figura 2. La somma z1 + z2 di due numeri complessi z1 e z2 può essere calcolata con la
regola del parallelogramma. Qui z1 = 1 + 3i, z2 = 4 + i e quindi z1 + z2 = 5 + 4i.
2.E
Esercizi
Esercizio 2.4
Calcolare la parte reale e la parte immaginaria dei seguenti numeri complessi:
6 + 5i
3 −i ,
(2 + i)3
5i15
,
3 −2i
1 + 5i + 2 −3i
2 −i .
Esercizio 2.5
Dimostrare che valgono i fatti seguenti per ogni z, w ∈C :
|¯z| = |z|,
|z−1| = 1
|z|,
z + w = ¯z + ¯w,
zw = ¯z ¯w.
Esercizio 2.6
Disegnare nel piano complesso i seguenti sottoinsiemi:
1. A = {z ∈C tali che Re(z) > Im(z)};
2. B = {z ∈C tali che z + ¯z = i};
3. C = {z ∈C tali che |z −2| ≥2};
9

<!-- pagina 10 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
3
Numeri Complessi II
3.A
Coordinate polari
Come ricordato nella Figura 3, un punto (x, y) diverso dall’origine del piano cartesiano può essere
identiﬁcato usando la lunghezza r del vettore corrispondente e l’angolo ϑ formato dal vettore con
l’asse reale.
Figura 3. Il piano complesso (sinistra) e le coordinate polari (destra).
Deﬁnizione 3.1 (Coordinate polari)
Le coordinate polari del punto sono la coppia (r, ϑ). Per passare dalle coordinate polari alle
coordinate cartesiane (x, y) basta usare le formule
x = r cos ϑ,
y = r sin ϑ.
Viceversa,
r =
p
x2 + y2,
cos ϑ =
x
p
x2 + y2 ,
sin ϑ =
y
p
x2 + y2 .
Tornando ai numeri complessi, un numero z = x + yi può essere scritto in coordinate polari come
z = x + yi = r cos ϑ + (r sin ϑ)i = r(cos ϑ + i sin ϑ).
Notiamo che
|z| =
p
x2 + y2 = r
Il modulo di z è quindi la lunghezza del vettore che descrive z. Il coniugio ¯z = a −ib è il punto
ottenuto cambiando il segno della coordinata immaginaria: geometricamente questo corrisponde a
riﬂettere il punto rispetto all’asse reale. In coordinate polari, questo corrisponde a cambiare ϑ in
−ϑ lasciando ﬁsso r. Si veda la Figura 4 (sinistra).
Tornando alle coordinate polari, è comodo scrivere
eiϑ = cos ϑ + i sin ϑ
10

<!-- pagina 11 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
In questo modo ogni numero complesso z̸ = 0 si scrive come
z = reiϑ.
Il numero r = |z| è il modulo di z e l’angolo ϑ è detto argomento (o fase) di z. Il motivo profondo
per cui introduciamo inaspettatamente qui la costante e è dovuto alle rappresentazioni delle fun-
zioni ex, sin x e cos x come serie di potenze. Giustiﬁcare questa scelta ci porterebbe però troppo
lontano; per noi è suﬃciente considerare questa misteriosa esponenziale complessa eiϑ come un
simbolo che vuol dire semplicemente cos ϑ + i sin ϑ. Si tratta di una simbologia azzeccata, perché
eiϑ ha le proprietà usuali dell’esponenziale:
Proposizione 3.2
Vale la relazione
ei(ϑ+ϕ) = eiϑ · eiϕ.
Spiegazione. La relazione segue direttamente dalle formule di addizione per seno e coseno, sos-
tituendo eiα = cos α + i sin α.
Vediamo allora che le coordinate polari sono particolarmente utili quando moltiplichiamo due numeri
complessi. Se
z1 = r1eiϑ1,
z2 = r2eiϑ2
allora il loro prodotto è
z1z2 = r1r2ei(ϑ1+ϑ2).
In altre parole: quando si fa il prodotto di due numeri complessi, i moduli si moltiplicano e gli
argomenti si sommano. Notiamo in particolare che se z = reiϑ̸ = 0, il suo inverso è
z−1 = r−1e−iϑ
L’inverso z−1 ha argomento −ϑ opposto a quello ϑ di z e modulo
z−1 = r−1 inverso rispetto a
|z| = r, si veda la Figura 4 (destra).
Notiamo anche che due numeri complessi non nulli espressi in forma polare r0eiϑ0, r1eiϑ1, sono lo
stesso numero complesso se e solo se valgono entrambi i fatti seguenti:
• r0 = r1,
• ϑ1 = ϑ0 + 2kπ per qualche k ∈Z.
11

<!-- pagina 12 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Figura 4. Il coniugio ¯z di z si ottiene specchiando z lungo l’asse reale (sinistra).
L’inverso z−1 di z ha argomento −ϑ opposto a quello ϑ di z e modulo
z−1 inverso rispetto a |z|.
La circonferenza unitaria è mostrata in ﬁgura (destra).
Finalmente, notiamo che i numeri complessi eiϑ al variare di ϑ sono precisamente i punti che
stanno sulla circonferenza unitaria, determinati dall’angolo ϑ. In particolare per ϑ = π otteniamo
la celebre identità di Euler: eiπ = −1 e per ϑ = 2π otteniamo e2iπ = 1.
3.B
Potenza e radici n-esime di un numero complesso
Sia z0 = r0eiϑ0 un numero complesso ﬁssato diverso da zero. Mostriamo come risolvere l’equazione
zn = z0
usando i numeri complessi. In altre parole, determiniamo tutte le radici n-esime di z0. Scriviamo
la variabile z in forma polare come z = reiϑ. L’equazione adesso diventa
zn = rneinϑ = z0 = r0eiϑ0
L’equazione è soddisfatta precisamente se valgono entrambi i fatti seguenti:
• r =
n√r0,
• nϑ = ϑ0 + 2kπ per qualche k ∈Z.
La seconda condizione può essere riscritta richiedendo che
ϑ = ϑ0
n + 2kπ
n
per qualche k ∈Z.
Otteniamo quindi precisamente n soluzioni distinte:
per i valori k =
0, 1, . . . , n −1 otteniamo gli argomenti
ϑ = ϑ0
n , ϑ0
n + 2π
n , . . . , ϑ0
n + 2(n −1)π
n
.
12

<!-- pagina 13 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Le n soluzioni dell’equazione zn = z0 hanno tutte lo stesso modulo
n√r0 e argomenti che variano
in una sequenza di angoli separati da un passo costante 2π
n . Geometricamente, questo signiﬁca che
le soluzioni formano i vertici di un poligono regolare centrato nell’origine con n lati e raggio
n√r0.
(Figura 5).
Esempio 3.3
L’equazione zn = 1 ha come soluzioni i numeri complessi
z = ei 2kπ
n
dove k = 0, 1, . . . , n −1. Queste n soluzioni sono i vertici di un poligono regolare di raggio 1
con n lati, avente 1 come vertice. Questi numeri sono le radici n-esime dell’unità.
Esempio 3.4
Come mostrato nella Figura 5, le tre soluzioni dell’equazione z3 = −8 hanno modulo
3√
8 = 2 e
argomenti π
3 , π e 5π
3 . Si tratta dei numeri complessi
z1 = 2ei π
3 = 2

cos π
3 + i sin π
3

= 1 +
√
3i,
z2 = 2eiπ = −2,
z3 = 2ei 5π
3 = 2

cos 5π
3 + i sin 5π
3

= 1 −
√
3i.
Figura 5. Le radici seste di 1, cioè le soluzioni di z6 = 1, sono i vertici di un esagono regolare
centrato nell’origine con un vertice in 1 (sinistra). Le soluzioni di z3 = −8 sono i vertici di un
triangolo equilatero centrato nell’origine e di raggio
3√
8 = 2 (destra).
13

<!-- pagina 14 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
3.C
Esercizi
Esercizio 3.5
Calcola le soluzioni dell’equazione z4 = i e disegnarle nel piano complesso.
Esercizio 3.6
Determinare coordinate polari per i seguenti numeri complessi:
sin(2),
cos(2) + i sin(2),
cos(2) −i sin(2),
1 + i
2
,
1 −i
√
3.
Esercizio 3.7
Disegnare nel piano complesso i seguenti sottoinsiemi:
1. A = {z = reiϑ ∈C tali che ϑ = π
2 };
2. B = {z = reiϑ ∈C tali che ϑ = (2k + 1)π, k ∈Z};
3. C = {z = reiϑ ∈C tali che r = 1 e 0 ≤ϑ ≤π}.
Esercizio 3.8
Calcolare (1 −i)3 usando coordinate polari. Veriﬁcare il risultato usando coordinate cartesiane.
14

<!-- pagina 15 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
4
Polinomi
4.A
Deﬁnizione
I polinomi sono tipi particolarmente semplici di funzioni ottenute combinando numeri e variabili ed
usando solo le operazioni +, −e ·. Ricordiamo che un monomio è un’espressione algebrica che ha
una parte numerica (il coeﬃciente) ed una parte letterale; ad esempio questi sono monomi:
4x,
−2xy,
√
5x3.
Il grado di un monomio è la somma degli esponenti presenti sulle parti letterali: i tre monomi
descritti sopra hanno grado 1, 2 e 3 . Un monomio di grado zero è semplicemente un numero. Un
polinomio è una somma di monomi, ad esempio:
7 + 3x2 −
√
2y3.
Un polinomio è ridotto in forma normale se è scritto come somma di monomi con parti letterali
diﬀerenti e coeﬃcienti non nulli, oppure è il polinomio 0. Per ridurre un polinomio in forma nor-
male è suﬃciente raccogliere i monomi con la stessa parte letterale e quindi eliminare quelli con
coeﬃciente nullo.
Il grado di un polinomio scritto in forma normale è il massimo grado dei suoi monomi.
Ci interessano particolarmente i polinomi in cui compare una sola variabile x. Un polinomio di
questo tipo viene indicato con p(x) oppure più semplicemente con p. Un polinomio p(x) con una
sola variabile può essere sempre descritto ordinando i suoi monomi da quello di grado più alto a
quello di grado più basso: otteniamo quindi una scrittura del tipo
p(x) = anxn + · · · + a1x + a0
dove n è il grado di p(x) e an̸ = 0. Ad esempio:
x3 −2x + 5,
4x2 −7.
Un polinomio di grado zero è semplicemente un numero a0.
Denotiamo con R[x] l’insieme dei polinomi con coeﬃcienti in R in cui compare una sola variabile
x e con C[x] l’insieme dei polinomi con coeﬃcienti in C in cui compare una sola variabile x. Con
Rk[x] denotiamo i polinomi in R[x] che hanno grado ≤k. (Analogamente per Ck[x].)
4.B
Divisione con resto fra polinomi
I polinomi assomigliano ai numeri interi: possono essere sommati, moltiplicati, e si possono fare
le divisioni con resto. Prendiamo due numeri interi, ad esempio 44 e 6. Se dividiamo 44 per 6
otteniamo come quoziente 7 e come resto 2. In altre parole, otteniamo:
44 = 7 · 6 + 2.
15

<!-- pagina 16 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Notiamo che il resto 2 è ovviamente sempre più piccolo del divisore 6.
Analogamente, dati due polinomi p(x) (il dividendo) e d(x)̸ = 0 (il divisore), esistono sempre (e
sono unici) due polinomi q(x) (il quoziente) e r(x) (il resto) per cui
p(x) = q(x)d(x) + r(x)
con la proprietà che il resto r(x) abbia grado strettamente minore del divisore d(x).
Le divisioni fra polinomi si risolvono con carta e penna esattamente con la stessa procedura usata
per i numeri interi. Ad esempio, se dividiamo p(x) = x3 + 1 per d(x) = x2 −1 otteniamo
x3 + 1 = x
 x2 −1

+ (x + 1)
e la divisione ha come quoziente x e come resto x + 1.
Diciamo che il numero intero 7 divide 14 ma non divide 15, perché la divisione di 14 per 7 ha resto
nullo, mentre la divisione di 15 per 7 invece ha un certo resto. Usiamo la stessa terminologia per i
polinomi: se la divisione fra due polinomi p(x) e d(x) ha resto nullo, allora p(x) = q(x)d(x) per
qualche quoziente q(x) e diciamo che d(x) divide p(x). Possiamo usare la barra verticale | come
sinonimo di "divide" e scrivere ad esempio:
9 | 18,
(x + 1) |
 x3 + 1

.
Notiamo che eﬀettivamente
 x3 + 1

=
 x2 −x + 1

(x + 1).
4.C
Radici di un polinomio
Ricordiamo adesso una delle deﬁnizioni più importanti dell’algebra. Se p(x) è un polinomio e a è
un numero, indichiamo con p(a) il numero che otteniamo sostituendo a al posto di x. Ad esempio,
se p(x) = x2 −3, allora p(−2) = 4 −3 = 1.
Deﬁnizione 4.1
Un numero a è radice di un polinomio p(x) se p(a) = 0.
Ad esempio, il numero −1 è radice del polinomio p(x) = x3 + 1 perché p(−1) = 0. La determi-
nazione delle radici di un polinomio è uno dei problemi più classici dell’algebra. A questo scopo è
utile il criterio seguente.
Proposizione 4.2
Il numero a è radice di p(x) se e solo se (x −a) | p(x).
Dimostrazione. Se dividiamo p(x) per (x −a), otteniamo
p(x) = q(x)(x −a) + r(x)
16

<!-- pagina 17 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
dove q(x) è il quoziente e r(x) il resto. Sappiamo che il grado di r(x) è strettamente minore di
quello di (x−a), che è uno: quindi r(x) ha grado zero, in altre parole è una costante che scriviamo
semplicemente come r0. Quindi
p(x) = q(x)(x −a) + r0
Se sostituiamo a al posto di x, otteniamo
p(a) = q(a)(a −a) + r0 = 0 + r0 = r0.
Quindi a è radice di p(x) se e solo se r0 = 0. D’altra parte r0 = 0 se e solo se (x −a) divide p(x)
e quindi concludiamo.
Deﬁnizione 4.3
La molteplicità di una radice a di un polinomio p(x) è il massimo numero k tale che (x −a)k
divide p(x).
Informalmente, la molteplicità di a misura "quante volte" a è radice di p(x).
Esempio 4.4
Il polinomio x3 −1 ha la radice 1 con molteplicità 1 perché
x3 −1 = (x −1)
 x2 + x + 1

e (x−1) non divide x2+x+1, semplicemente perché 1 non è radice di x2+x+1. Analogamente
il polinomio
x3 −2x2 + x = (x −1)2x
ha la radice 1 con molteplicità 2 e la radice 0 con molteplicità 1.
Esempio 4.5
I polinomi
q1(x) = x2 −2x + 1,
q2(x) = x2 −1
possono essere scritti come
q1(x) = (x −1)2,
q2(x) = (x + 1)(x −1).
Questi hanno rispettivamente la radice 1 con molteplicità 2 e le radici −1, 1 entrambe con
molteplicità 1 . Il prodotto
p(x) = q1(x)q2(x) = (x −1)3(x + 1)
ha la radice 1 con molteplicità 3 e la radice −1 con molteplicità 1.
17

<!-- pagina 18 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Teorema 4.6
Un polinomio p(x) di grado n ≥1 ha al più n radici, contate con molteplicità.
Dimostrazione. Dimostriamo il teorema per induzione su n. Se n = 1, il polinomio è del tipo
p(x) = a1x + a0 ed ha chiaramente una sola radice −a0/a1. Quindi la tesi è soddisfatta.
Supponiamo la tesi vera per n −1 e la dimostriamo per n. Se p(x) non ha radici, siamo a posto.
Se ha almeno una radice a, allora per la Proposizione precedente possiamo dividere p(x) per x −a
e ottenere un altro polinomio q(x), cioè vale p(x) = (x−a)q(x). Il polinomio q(x) ha grado n−1
e quindi per ipotesi induttiva ha al più n −1 radici contate con molteplicità. Le radici di p(x)
contate con molteplicità sono esattamente quelle di q(x) più a. Quindi p(x) ha al più n−1+1 = n
radici e abbiamo concluso.
Esempio 4.7
Un polinomio di grado 1 è sempre del tipo p(x) = ax + b ed ha quindi sempre una sola radice
x = −b/a. Un polinomio di grado 2 è del tipo p(x) = ax2 + bx + c e come sappiamo bene dalle
scuole superiori le sue radici dipendono da ∆= b2 −4ac nel modo seguente.
• Se ∆> 0, il polinomio p(x) ha due radici distinte
x± = −b ±
√
∆
2a
entrambe di molteplicità uno.
• Se ∆= 0, il polinomio p(x) ha una sola radice
x = −b
2a
con molteplicità due.
• Se ∆< 0, il polinomio p(x) non ha radici reali.
In particolare, ci sono polinomi che non hanno radici reali.
4.D
Teorema fondamentale dell’algebra
Veniamo inﬁne al vero motivo per cui abbiamo introdotto i numeri complessi in questo corso.
Teorema 4.8 (Teorema fondamentale dell’algebra)
Un polinomio p(x) a coeﬃcienti complessi di grado n ha esattamente n radici, contate con
molteplicità.
Esistono varie dimostrazioni di questo teorema, che possono essere agevolmente trovate in rete.
Quelle più accessibili usano degli strumenti analitici un po’ lontano dagli argomenti trattati in
questo corso, e quindi le omettiamo.
18

<!-- pagina 19 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 4.9
Per un polinomio di secondo grado p(x) = ax2+bx+c le due radici complesse si trovano usando
la solita formula
x± = −b ±
√
∆
2a
.
Questa volta, ±
√
∆indica le due radici quadrate complesse di ∆, che esistono sempre, come
visto nella lezione scorsa.
Esempio 4.10
Le radici del polinomio x2 + 1 sono ±i. Le radici del polinomio x2 + (1 −i)x −i sono
x± = −1 + i ±
√
2i
2
=⇒x± = −1 + i ± (1 + i)
2
=⇒x+ = i, x−= −1.
4.E
Polinomi a coeﬃcienti reali
Sappiamo che un polinomio p(x) di grado n ha esattamente n soluzioni complesse contate con
molteplicità. Se p(x) ha coeﬃcienti reali, possiamo dire qualcosa di più sulle sue radici complesse.
Proposizione 4.11
Sia p(x) un polinomio a coeﬃcienti reali. Se z è una radice complessa di p(x), allora ¯z è anch’essa
radice di p(x).
Dimostrazione. Il polinomio è
p(x) = anxn + · · · + a1x + a0
e per ipotesi i coeﬃcienti an, . . . , a0 sono tutti reali. Se z è radice, allora
p(z) = anzn + · · · + a1z + a0 = 0.
Applicando il coniugio ad entrambi i membri troviamo
an¯zn + · · · + a1¯z + a0 = 0 = 0.
Siccome i coeﬃcienti sono reali, il coniugio di ai è sempre ai e quindi
an¯zn + · · · + a1¯z + a0 = 0.
In altre parole, anche ¯z è radice di p(x).
19

<!-- pagina 20 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
5
Spazi Vettoriali I
Il nostro scopo è studiare oggetti geometrici in Rn. È però utile adottare un punto di vista più
astratto e considerare tutti gli spazi che possiedono le stesse proprietà algebriche di Rn: questi
sono detti spazi vettoriali.
Questa astrazione permette di trattare in modo uniforme molti oggetti matematici, come gli insiemi
di soluzioni di sistemi lineari, gli spazi di funzioni e gli spazi di matrici.
5.A
Lo spazio euclideo
Sia n ≥1 un numero naturale.
Deﬁnizione 5.1
Lo spazio euclideo n-dimensionale è l’insieme
Rn = R × · · · × R
|
{z
}
n volte
.
I suoi elementi sono successioni (x1, . . . , xn) di n numeri reali.
In particolare, R2 è il piano cartesiano e R3 lo spazio cartesiano. L’elemento (0, . . . , 0) è detto
origine e viene indicato con 0 oppure O.
Un elemento x ∈Rn può essere interpretato sia come un punto, sia come un vettore che parte
dall’origine e termina in x. A seconda del contesto useremo, ad esempio, P, Q per i punti e v, w
per i vettori.
Scriveremo spesso un vettore in forma verticale:
x =



x1
...
xn


,
detta vettore colonna. I numeri x1, . . . , xn sono le coordinate di x.
Somma fra vettori
Lo spazio Rn è dotato di una somma deﬁnita componente per componente. Se
x =



x1
...
xn


,
y =



y1
...
yn


,
allora
x + y =



x1 + y1
...
xn + yn


.
20

<!-- pagina 21 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
In R2 questa operazione coincide geometricamente con la consueta regola del parallelogramma.
Prodotto per scalare
Dato x ∈Rn e uno scalare λ ∈R, deﬁniamo
λx =



λx1
...
λxn


.
Geometricamente, λx si ottiene allungando o accorciando x di un fattore |λ| e, se λ < 0, inver-
tendone il verso.
Figura 6. Somma di vettori in R2 e prodotto di un vettore per uno scalare.
Il numero reale λ è detto scalare; l’operazione x 7→λx è detta prodotto per scalare.
5.B
Spazi vettoriali
Deﬁnizione 5.2 (Gruppo)
Un gruppo è un insieme G dotato di un’operazione binaria, cioè di una funzione che associa ad
ogni coppia a, b di elementi in G un nuovo elemento di G che indichiamo con a ∗b. Il simbolo
∗indica l’operazione binaria. L’operazione deve soddisfare i seguenti tre assiomi:
1. ∃e ∈G : e ∗a = a ∗e = a, ∀a ∈G (esistenza dell’elemento neutro e),
2. a ∗(b ∗c) = (a ∗b) ∗c, ∀a, b, c ∈G (proprietà associativa),
3. ∀a ∈G, ∃a′ ∈G : a ∗a′ = a′ ∗a = e (esistenza dell’inverso).
Il gruppo G è commutativo se vale anche la proprietà commutativa
a ∗b = b ∗a, ∀a, b ∈G.
21

<!-- pagina 22 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Ad esempio, l’insieme Z dei numeri interi con l’operazione di somma è un gruppo commutativo.
Formano un gruppo commutativo anche gli insiemi numerici Q, R e C con l’operazione di somma.
Gli insiemi Q\{0}, R\{0}, e C\{0}, formano un gruppo commutativo anche con la moltiplicazione.
Notiamo invece che non sono gruppi:
- L’insieme N con la somma, sempre perché non è soddisfatto (3),
- L’insieme Z (o Z \ {0}) con la moltiplicazione, perché non è soddisfatto (3).
Negli insiemi numerici Z, Q, R e C ci sono in realtà due operazioni + e ·. Introduciamo adesso una
struttura algebrica che prevede la coesistenza di due operazioni binarie.
Deﬁnizione 5.3 (Campo)
Un campo è un insieme A dotato di due operazioni binarie + e · che soddisfano questi assiomi:
1. A è un gruppo commutativo con l’operazione + con elemento neutro 0A,
2. A \ {0A} è un gruppo commutativo con l’operazione · con elemento neutro 1A,
3. Vale la proprietà distributiva a · (b + c) = (a · b) + (a · c), ∀a, b, c ∈A.
Esempi di campi sono Q, R e C. Notiamo invece che Z non è un campo, perché ovviamente 2 non
ha un inverso per il prodotto dentro l’insieme Z.
Deﬁnizione 5.4 (Spazio vettoriale)
Fissiamo un campo K. Questo per noi è generalmente o il campo K = R dei numeri reali o il
campo K = C dei numeri complessi (però per la deﬁnizione può essere qualsiasi campo). Gli
elementi di K sono detti scalari. Uno spazio vettoriale su K è un insieme V di elementi, detti
vettori, dotato di due operazioni:
- un’operazione detta somma che associa a due vettori v, w ∈V un terzo vettore v + w ∈V ;
- un’operazione detta prodotto per scalare che associa ad un vettore v ∈V e ad uno scalare
λ ∈K un vettore λv ∈V .
Queste due operazioni devono soddisfare le stesse proprietà delle corrispondenti operazioni dello
spazio euclideo, cioè:
1. L’insieme V è un gruppo commutativo con la somma +,
2. λ(v + w) = λv + λw,
3. (λ + µ)v = λv + µv,
4. (λµ)v = λ(µv),
5. 1v = v.
Le proprietà devono valere per ogni v, w ∈V e ogni λ, µ ∈K.
22

<!-- pagina 23 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
L’elemento neutro del gruppo V è indicato con il simbolo 0 (o 0V ) ed è detto l’origine dello
spazio vettoriale V . Non va confuso con lo zero 0 del campo K. In questo corso il simbolo 0
può indicare varie cose diﬀerenti ed il signiﬁcato preciso sarà sempre chiaro dal contesto.
A partire da questi assiomi è subito possibile dimostrare un piccolo risultato.
Proposizione 5.5
Vale la relazione 0v = 0.
Come dicevamo, il simbolo 0 può indicare oggetti diversi: in questo enunciato, il primo 0 è
l’elemento neutro di K ed il secondo è l’origine di V .
Dimostrazione. Vale
0v = (0 + 0)v = 0v + 0v
e sempliﬁcando deduciamo che 0v = 0.
5.C
Esempi
Lo spazio K
Se (K, +, ·) è un campo, allora è anche uno spazio vettoriale su se stesso. Le proprietà di uno
spazio vettoriale seguono per questo motivo:
1. (K, +) è un gruppo commutativo per via della proprietà 1 di un campo.
2. λ(v + w) = λv + λw per via della proprietà distributiva di un campo.
3. (λ + µ)v = λv + µv: commutatività e distributività.
4. (λµ)v = λ(µv), per l’associatività della moltiplicazione del campo.
5. 1v = v, perché 1 è l’elemento neutro (per la moltiplicazione) nel campo.
Lo spazio Kn
L’esempio principale di spazio vettoriale su R è ovviamente lo spazio euclideo Rn già incontrato
precedentemente. Più in generale, è possibile deﬁnire per qualsiasi campo K uno spazio Kn.
Sia n ≥1 un numero naturale. Lo spazio Kn è l’insieme delle sequenze (x1, . . . , xn) di numeri in
K. Gli elementi v ∈Kn sono descritti generalmente come vettori colonna
v =



x1
...
xn


∈Kn
23

<!-- pagina 24 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
La somma e la moltiplicazione per scalare sono deﬁnite termine a termine esattamente come visto
sopra per Rn, cioè:



x1
...
xn


+



y1
...
yn


=



x1 + y1
...
xn + yn


,
λ



x1
...
xn


=



λx1
...
λxn


.
Facciamo alcuni esempi con dei vettori di C2 :
 1 + i
−2

+

3i
1 −i

=
 1 + 4i
−1 −i

,
(2 + i)

3
1 −i

=
 6 + 3i
3 −i

Si deve ancora controllare che questo ci dà veramente uno spazio vettoriale.
Per esempio, la
proprietà 2 della deﬁnizione possiamo controllare così:
λ(x + y) = λ



x1 + y1
...
xn + yn


=



λ(x1 + y1)
...
λ(xn + yn)



=



λx1 + λy1
...
λxn + λyn


=



λx1
...
λxn


+



λy1
...
λyn


= λx + λy
Abbiamo usato la deﬁnizione della somma e della moltiplicazione con uno scalare, poi la legge
distributiva nel campo (in ognuna delle n componenti del vettore), e poi di nuovo la deﬁnizione di
somma e di moltiplicazione con uno scalare.
Lo spazio delle successioni in K
Invece di usare vettori che hanno n componenti in K, possiamo anche studiare successioni inﬁnite,
che hanno un numero inﬁnito di componenti in K. Un elemento di questo insieme è allora una
successione (xn)n∈N per la quale ogni elemento xk è uno scalare in K. Somma e moltiplicazione
sono deﬁnite di nuovo componente per componente:
(xn)n∈N + (yn)n∈N = (xn + yn)n∈N,
λ(xn)n∈N = (λxn)n∈N.
Si veriﬁca che con queste operazioni otteniamo la struttura di uno spazio vettoriale.
Uno spazio delle funzioni [0, 1] →K
Mentre nell’esempio sopra associamo ad ogni n ∈N un numero xn nel campo K, possiamo anche
associare ad ogni numero reale x ∈[0, 1] un elemento f(x) ∈K.
Allora f : [0, 1] →K è
una funzione. Se deﬁniamo di nuovo la somma e la moltiplicazione con scalare punto per punto
(in [0, 1]), otteniamo la struttura di uno spazio vettoriale sull’insieme di queste funzioni.
Più
precisamente, deﬁniamo per due funzioni f, g e uno scalare λ le funzioni
(f + g)(x) = f(x) + g(x),
(λf)(x) = λf(x),
∀x ∈[0, 1].
24

<!-- pagina 25 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Lo spazio K[x] dei polinomi
Fissato un campo K, indichiamo con K[x] l’insieme di tutti i polinomi aventi coeﬃcienti in K.
Due polinomi possono essere sommati, e moltiplicando un polinomio per uno scalare otteniamo un
polinomio. Ad esempio:
 x3 −2x + 1

+
 4x4 + x −3

= 4x4 + x3 −x −2,
3
 x3 −2x

= 3x3 −6x.
L’insieme K[x] è quindi naturalmente equipaggiato con le due operazioni di uno spazio vettoriale.
Di nuovo, rimane da controllare tutti gli assiomi 1.–5. della deﬁnizione.
5.D
Esercizi
Esercizio 5.6
Per tutti gli esempi di spazi vettoriali dati sopra, veriﬁcare i 5 assiomi (come abbiamo controllato
l’assioma 2 nel caso dello spazio Kn).
Esercizio 5.7
Controllare che l’insieme Kk[x] di polinomi a coeﬃcienti in K che hanno grado ≤k è uno spazio
vettoriale.
Perché l’insieme dei polinomi che hanno grado esattamente k non è uno spazio
vettoriale se k ≥1?
Esercizio 5.8
Per il primo esempio, C è uno spazio vettoriale sul campo C. Dimostrare che è anche uno spazio
vettoriale su R.
Esercizio 5.9
Sia K = {0, 1} e deﬁniamo due operazioni nel seguente modo:
0 + 0 = 0,
0 + 1 = 1,
1 + 0 = 1,
1 + 1 = 0,
0 · 0 = 0,
0 · 1 = 0,
1 · 0 = 0,
1 · 1 = 1.
Dimostrare che (K, +, ·) è un campo.
Esercizio 5.10
Sia K = {0, 1, 2} trovare (in modo simile all’esercizio sopra) due operazioni + e · tali che
(K, +, ·) diventi un campo.
[Per chi è molto coraggioso: Provare a generalizzare questo a K = {0, 1, 2, . . . , p −1} dove p è
un numero primo.]
25

<!-- pagina 26 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
6
Spazi Vettoriali II
Nell’ultima lezione abbiamo introdotto gli spazi vettoriali e alcuni esempi. Continuiamo con un
altro esempio fondamentale per il corso.
Lo spazio delle matrici
Deﬁnizione 6.1
Sia come sempre K un campo ﬁssato. Una matrice con m righe e n colonne a coeﬃcienti in
K è una tabella rettangolare del tipo
A =



a11
· · ·
a1n
...
...
...
am1
· · ·
amn



in cui tutti gli mn coeﬃcienti aij appartengono a K. Diciamo brevemente che A è una matrice
m × n. Le sue righe sono indicate con A1, . . . , Am e le sue colonne con A1, . . . , An.
Ad esempio, le seguenti sono matrici a coeﬃcienti in R:


1
√
2
0
−5
7
π

,
 5
0
√
3

.
Due matrici A = (aij) e B = (bij) della stessa taglia si sommano componente per componente;
analogamente il prodotto per scalare è deﬁnito componente per componente:
(A + B)ij = aij + bij,
(λA)ij = λaij.
Indichiamo con M(m, n, K) l’insieme di tutte le matrici m×n a coeﬃcienti in K, con queste oper-
azioni. Quando il campo è sottinteso scriviamo M(m, n). Si veriﬁca facilmente che M(m, n, K) è
uno spazio vettoriale. Notiamo inoltre che una matrice m×1 è semplicemente un vettore colonna,
quindi M(m, 1, K) = Km.
6.A
Sottospazio vettoriale
Deﬁniamo adesso rigorosamente in che senso uno spazio vettoriale può contenerne un altro.
Deﬁnizione 6.2
Sia V uno spazio vettoriale su un campo K. Un sottospazio vettoriale di V è un sottoinsieme
W ⊂V che soddisfa i seguenti tre assiomi:
(1) 0 ∈W.
26

<!-- pagina 27 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
(2) Se v, v′ ∈W, allora anche v + v′ ∈W.
(3) Se v ∈W e λ ∈K, allora λv ∈W.
Le condizioni (2) e (3) dicono che W è chiuso rispetto alla somma e al prodotto per scalare.
Con le operazioni ereditate da V , ogni sottospazio W è quindi esso stesso uno spazio vettoriale.
Ogni spazio vettoriale V ha sempre il sottospazio banale {0} e il sottospazio totale V ; per ogni
sottospazio vale
{0} ⊂W ⊂V.
Un esempio già incontrato è Kk[x] ⊂K[x], formato dai polinomi di grado ≤k.
6.B
Matrici diagonali, triangolari, simmetriche e antisimmetriche
Ricordiamo che M(m, n, K) è lo spazio vettoriale delle matrici m × n a coeﬃcienti in K. Impo-
nendo opportune condizioni sui coeﬃcienti otteniamo vari sottospazi importanti.
Deﬁnizione 6.3
Una matrice n × n è detta quadrata. Una matrice A quadrata n × n è:
• diagonale se aij = 0,
∀i̸ = j;
• triangolare superiore se aij = 0,
∀i > j;
• triangolare inferiore se aij = 0,
∀i < j;
• triangolare se è triangolare inferiore o superiore;
• simmetrica se aij = aji,
∀i, j;
• antisimmetrica se aij = −aji,
∀i, j.
Esempio 6.4
Le matrici seguenti sono (in ordine) diagonale, triangolare superiore, triangolare inferiore, sim-
metrica e antisimmetrica:
 2
0
0
−1

,
 1
9
0
√
2

,
 −1
0
7
2

,
 −1
2
2
4

,

0
1
−1
0

.
Una stessa matrice può appartenere a più classi: per esempio
 0
0
0
1

è diagonale, triangolare superiore, triangolare inferiore e simmetrica. La matrice nulla appartiene
a tutte e cinque le classi.
27

<!-- pagina 28 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Gli elementi a11, a22, . . . , ann formano la diagonale principale. In una matrice antisimmetrica
gli elementi della diagonale principale sono necessariamente nulli, perché aii = −aii implica
aii = 0.
Indichiamo lo spazio delle matrici quadrate n × n con M(n, K), o più semplicemente M(n).
Indichiamo con
D(n),
T s(n),
T i(n),
S(n),
A(n)
i sottoinsiemi formati rispettivamente dalle matrici diagonali, triangolari superiori, triangolari infe-
riori, simmetriche e antisimmetriche.
Proposizione 6.5
I sottoinsiemi D(n), T s(n), T i(n), S(n), A(n) sono tutti sottospazi vettoriali di M(n).
Spiegazione. Per ciascuno dei cinque sottoinsiemi basta veriﬁcare che la matrice nulla appartiene
al sottoinsieme e che somma e prodotto per scalare preservano la proprietà che lo deﬁnisce. Per
esempio, se A, B sono simmetriche, allora (A + B)ij = Aij + Bij = Aji + Bji = (A + B)ji e
(λA)ij = λAij = λAji = (λA)ji.
6.C
Combinazioni lineari e sottospazio generato (Span)
Sia V uno spazio vettoriale e siano v1, . . . , vk ∈V .
Una combinazione lineare dei vettori
v1, . . . , vk è un vettore del tipo
v = λ1v1 + · · · + λkvk,
dove λ1, . . . , λk ∈K. Per esempio, in R3, se
v1 =


1
0
0

,
v2 =


0
1
0

,
allora
λ1v1 + λ2v2 =


λ1
λ2
0

,
quindi al variare di λ1, λ2 otteniamo precisamente il piano z = 0.
Deﬁnizione 6.6
Sia V uno spazio vettoriale e v1, . . . , vk ∈V dei vettori arbitrari. Il sottospazio generato da
v1, . . . , vk è il sottoinsieme di V formato da tutte le loro combinazioni lineari e viene indicato
con
Span(v1, . . . , vk).
28

<!-- pagina 29 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
In simboli:
Span(v1, . . . , vk) = {λ1v1 + · · · + λkvk | λ1, . . . , λk ∈K}.
Proposizione 6.7
Il sottoinsieme Span(v1, . . . , vk) è un sottospazio vettoriale di V .
Dimostrazione. Dobbiamo mostrare che W = Span(v1, . . . , vk) soddisfa i tre assiomi.
(1) 0 ∈W, infatti usando λ1 = · · · = λk = 0 troviamo
0v1 + · · · + 0vk = 0 ∈W.
(2) Se v, w ∈W, scriviamo
v = λ1v1 + · · · + λkvk,
w = µ1v1 + · · · + µkvk.
Allora
v + w = (λ1 + µ1)v1 + · · · + (λk + µk)vk ∈W.
(3) Se v ∈W e λ ∈K, allora
λv = (λλ1)v1 + · · · + (λλk)vk ∈W.
Esempio 6.8
Se v è un singolo vettore, allora
Span(v) = {λv | λ ∈K}.
Per esempio, in R2,
Span
 1
2

=
 t
2t

| t ∈R

,
che è la retta y = 2x.
6.D
Esercizi
Esercizio 6.9
Consideriamo il sottoinsieme W ⊂M(2, R) formato dalle matrici del tipo
 a
b
b
a

,
a, b ∈R.
29

<!-- pagina 30 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Dimostrare che W è un sottospazio vettoriale di M(2, R) e veriﬁcare che
W = Span
 1
0
0
1

,
 0
1
1
0

.
Esercizio 6.10
In R3 siano
v1 =


1
0
1

,
v2 =


0
1
1

.
Descrivere esplicitamente Span(v1, v2) e determinare quali dei vettori
u =


1
2
3

,
w =


1
2
4


appartengono a questo sottospazio.
30

<!-- pagina 31 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
7
Spazi Vettoriali III
Sappiamo dalla scuola che un punto, una retta e un piano hanno dimensione 0,1 e 2. In questa
lezione deﬁniamo la nozione di dimensione di uno spazio vettoriale (o di un suo sottospazio) in
modo rigoroso.
7.A
(In)dipendenza lineare
Deﬁnizione 7.1
Sia V uno spazio vettoriale su K e siano v1, . . . , vk ∈V alcuni vettori. Diciamo che questi
vettori sono linearmente dipendenti se esistono dei coeﬃcienti λ1, . . . , λk ∈K, non tutti nulli,
tali che
λ1v1 + · · · + λkvk = 0.
I vettori v1, . . . , vk sono linearmente indipendenti se non sono linearmente dipendenti. Questa
importante condizione può essere espressa nel modo seguente: dei vettori v1, . . . , vk sono linear-
mente indipendenti se e solo se
λ1v1 + · · · + λkvk = 0 =⇒λ1 = · · · = λk = 0.
In altre parole, l’unica combinazione lineare dei v1, . . . , vk che può dare il vettore nullo è quella
banale in cui tutti i coeﬃcienti λ1, . . . , λk sono nulli.
Se i vettori v1, . . . , vk sono linearmente dipendenti, allora è possibile esprimere uno di loro in
funzione degli altri. Infatti, per ipotesi esiste almeno un λi̸ = 0 e dopo aver diviso tutto per λi e
spostato gli addendi otteniamo
vi = −λ1
λi
v1 −· · · −λk
λi
vk
dove tra i vettori di destra ovviamente non compare vi. Quindi:
Proposizione 7.2
I vettori v1, . . . , vk sono dipendenti ⇐⇒uno di loro è esprimibile come combinazione lineare
degli altri.
I casi k = 1 e k = 2 sono facili da studiare. Da quanto abbiamo detto, segue facilmente che:
- un vettore v1 è dipendente ⇐⇒v1 = 0;
- due vettori v1, v2 sono dipendenti ⇐⇒sono multipli, cioè esiste un k ∈K tale che v1 = kv2
oppure v2 = kv1.
31

<!-- pagina 32 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 7.3
I vettori v1 =
 1
1

e v2 =
 −2
−2

di R2 sono dipendenti; w1 =
 1
2

e w2 =
 2
1

sono
indipendenti perché non sono multipli.
Il caso in cui ci siano tre (o più) vettori v1, v2, v3 è più complesso.
Esempio 7.4
I vettori
v1 =


1
1
0

,
v2 =


0
1
1

,
v3 =


1
0
−1


di R3 sono dipendenti, perché v1 −v2 −v3 = 0. Notiamo che a coppie i tre vettori sono sempre
indipendenti (non sono mai multipli), ma tutti e tre non lo sono, e questo non è certamente
un fatto che si vede immediatamente come nel caso k = 2. Infatti, ciascuno dei tre vettori
dipendenti v1, v2, v3 può essere scritto come combinazione degli altri due, infatti v1 = v2 + v3,
oppure v2 = v1 −v3, oppure v3 = v1 −v2.
Esempio 7.5
I vettori
e1 =


1
0
0

,
e2 =


0
1
0

,
e3 =


0
0
1


sono indipendenti: se una combinazione lineare produce il vettore nullo
λ1e1 + λ2e2 + λ3e3 = 0
allora riscriviamo entrambi i membri come vettori e scopriamo che
λ1


1
0
0

+ λ2


0
1
0

+ λ3


0
0
1

=


λ1
λ2
λ3

=


0
0
0

.
Da questo deduciamo che λ1 = λ2 = λ3 = 0. Quindi l’unica combinazione lineare di e1, e2, e3
che dà il vettore nullo è quella banale. Quindi i tre vettori e1, e2, e3 sono indipendenti.
Proposizione 7.6
Se v1, . . . , vk sono indipendenti, allora qualsiasi sottoinsieme di {v1, . . . , vk} è anch’esso formato
da vettori indipendenti.
Spiegazione. Se un sottoinsieme fosse dipendente, una sua combinazione lineare non banale nulla
si estenderebbe a una combinazione lineare non banale di tutti i vettori aggiungendo coeﬃcienti
nulli, contraddicendo l’indipendenza di v1, . . . , vk.
32

<!-- pagina 33 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
In particolare, ne deduciamo che se v1, . . . , vk sono indipendenti allora:
- i vettori vi sono tutti diversi da zero;
- i vettori vi sono a coppie non multipli.
Attenzione però: L’esempio sopra con v1, v2, v3 ∈R3 mostra che queste due condizioni sono nec-
essarie ma non suﬃcienti aﬃnché i vettori v1, . . . , vk siano indipendenti quando k ≥3.
7.B
Basi
Introduciamo adesso una delle deﬁnizioni più importanti del corso. Sia V uno spazio vettoriale.
Deﬁnizione 7.7
Una sequenza v1, . . . , vn ∈V di vettori è una base se sono soddisfatte entrambe queste con-
dizioni:
(1) i vettori v1, . . . , vn sono indipendenti;
(2) i vettori v1, . . . , vn generano V .
Ricordiamo che la seconda condizione vuol dire che V = Span (v1, . . . , vn), cioè qualsiasi vettore
di V è esprimibile come combinazione lineare dei vettori v1, . . . , vn. Facciamo adesso alcuni
esempi fondamentali.
Esempio 7.8
Gli elementi
e1 =





1
0
...
0




,
e2 =





0
1
...
0




,
. . .
en =





0
0
...
1





formano una base di Kn detta base canonica.
Controlliamo che i vettori e1, . . . , en sono indipendenti: Supponiamo di avere una combinazione
lineare nulla
λ1e1 + · · · + λnen = 0.
Questa tradotta in vettori diventa





λ1
λ2
...
λn




=





0
0
...
0





Ne deduciamo che λ1 = · · · = λn = 0 e quindi e1, . . . , en sono indipendenti.
33

<!-- pagina 34 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Controlliamo anche che i vettori e1, . . . , en generano Kn. Un generico vettore x ∈Kn si può
eﬀettivamente scrivere come combinazione lineare di e1, . . . , en nel modo seguente:
x =





x1
x2
...
xn




= x1





1
0
...
0




+ x2





0
1
...
0




+ · · · + xn





0
0
...
1




= x1e1 + x2e2 + · · · + xnen.
Esempio 7.9
Ricordiamo lo spazio Kn[x] dei polinomi di grado minore o uguale a n. Gli elementi 1, x, x2, . . . , xn
formano una base di Kn[x], detta base canonica.
Possiamo controllare che questi elementi formano veramente una base in modo simile all’esempio
precedente. Controlliamo prima che i vettori 1, x, . . . , xn sono indipendenti: se
λ0 · 1 + λ1x + · · · + λnxn = 0
allora chiaramente λ0 = · · · = λn = 0. D’altro canto, ciascun polinomio di grado minore o uguale
a n si scrive come p(x) = anxn + · · · + a1x + a0 e questa scrittura è già una combinazione
lineare dei vettori 1, x1, . . . , xn con coeﬃcienti a0, a1, . . . , an. Quindi gli elementi 1, x, . . . , xn
generano Kn[x].
7.C
Dimensione
Teorema 7.10
Se uno spazio vettoriale V ha una base formata da n vettori, allora ogni base di V contiene n
vettori.
Questo teorema è fondamentale, perché ci permette di deﬁnire in modo rigoroso un concetto in-
tuitivo, quello di dimensione.
Deﬁnizione 7.11
Se uno spazio vettoriale V ha una base v1, . . . , vn, diciamo che V ha dimensione n. Se V non
ammette una base ﬁnita, diciamo che ha dimensione ∞.
La deﬁnizione è ben posta proprio grazie al Teorema sopra: lo spazio vettoriale V ha tante basi,
ma hanno tutte lo stesso numero n di elementi.
Indichiamo la dimensione di uno spazio vettoriale V con il simbolo dim V . Possiamo calcolare la
dimensione degli spazi vettoriali dei quali abbiamo esibito una base. Troviamo in particolare:
dim Kn = n,
dim Kn[x] = n + 1.
34

<!-- pagina 35 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Ricordiamo che dim V = ∞se V non ammette una base ﬁnita. Per questo motivo, lo spazio K[x]
dei polinomi ha dimensione inﬁnita.
Il seguente teorema dice che dobbiamo solo controllare una delle due condizioni nella deﬁnizione
di una base se sappiamo già che abbiamo il numero di vettori corretto.
Teorema 7.12
Se dim V = n e {v1, . . . , vn} è un insieme di n vettori, allora v1, . . . , vn formano una base di
V se e solo se vale una delle due condizioni della deﬁnizione di base (mentre l’altra condizione
vale poi automaticamente).
7.D
Esercizi
Esercizio 7.13
Ricordiamo lo spazio M(m, n, K) delle matrici m × n a coeﬃcienti in K. Per ogni 1 ≤i ≤m
e 1 ≤j ≤n, indichiamo con eij la matrice m × n che ha tutti zeri ovunque, tranne un 1 nella
casella di riga i e colonna j. Ad esempio, nel caso delle matrici quadrate 2 × 2 troviamo:
e11 =
 1
0
0
0

,
e12 =
 0
1
0
0

,
e21 =
 0
0
1
0

,
e22 =
 0
0
0
1

Dimostrare che le matrici eij con 1 ≤i ≤m e 1 ≤j ≤n formano una base di M(m, n, K). In
particolare dim M(m, n, K) = mn.
Esercizio 7.14
Dimostrare che i vettori
 −1
1

e
 2
1

formano una base di R2.
Esercizio 7.15
Considera i vettori seguenti di R3 :
v1 =


1
1
2

,
v2 =


−1
1
−1

,
v3 =


1
5
4

,
v4 =


0
1
1


Mostra che v1, v2, v3 sono dipendenti e v1, v2, v4 indipendenti.
35

<!-- pagina 36 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
8
Matrici I
Ci ricordiamo che, per un campo K ﬁssato, M(m, n, K) è l’insieme di matrici con m righe e n
colonne a coeﬃcienti in K. Per due matrici A, B ∈M(m, n, K),
A =



a11
· · ·
a1n
...
...
...
am1
· · ·
amn


,
B =



b11
· · ·
b1n
...
...
...
bm1
· · ·
bmn


,
uno scalare λ ∈K, abbiamo deﬁnito
A + B =



a11 + b11
· · ·
a1n + b1n
...
...
...
am1 + bm1
· · ·
amn + bmn


,
λA =



λa11
· · ·
λa1n
...
...
...
λam1
· · ·
λamn


.
Ci ricordiamo che con queste operazioni, M(m, n, K) è uno spazio vettoriale su K di dimensione
mn (Esercizio 7.13). In questa lezione, studiamo altre operazioni sulle matrici.
8.A
Trasposta di una matrice
Deﬁnizione 8.1
La trasposta di una matrice A ∈M(m, n, K) è la matrice
tA ∈M(n, m, K)
deﬁnita scambiando righe e colonne, cioè:
 tA

ij = Aji.
Esempio 8.2
A =


2
1
−1
0
5
7


=⇒
tA =
 2
−1
5
1
0
7

Valgono le proprietà seguenti:
• t(A + B) = tA + tB,
t(λA) = λ(tA).
• Se A ∈M(n), allora anche tA ∈M(n).
• A ∈M(n) è simmetrica ⇐⇒tA = A, A ∈M(n) è antisimmetrica ⇐⇒tA = −A.
36

<!-- pagina 37 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
8.B
Rango di una matrice
Sia A una matrice m×n a coeﬃcienti in K. Ricordiamo che indichiamo con A1, . . . , An le colonne
di A. Ciascun Ai è un vettore in Km.
Deﬁnizione 8.3
Il rango di A (o rango per colonne di A) è la dimensione dello spazio
Span
 A1, . . . , An
⊂Km.
Viene comunemente indicato con rk(A).
Con un’osservazione di Lezione 7 otteniamo la seguente deﬁnizione alternativa.
Proposizione 8.4
Il rango di A è il massimo numero di colonne linearmente indipendenti di A.
Deﬁnizione 8.5
Deﬁniamo il rango per righe di A come la dimensione dello spazio generato dalle righe
Span (A1, . . . , Am) ⊂Kn.
In altre parole, il rango per righe di A è il rango della trasposta tA.
Proposizione 8.6
Per ogni matrice A il rango per righe è uguale al rango per colonne. Vale allora rk(tA) = rk(A).
8.C
Prodotto fra matrici
Deﬁnizione 8.7
Se A è una matrice m × n e B è una matrice n × p il prodotto AB è una nuova matrice m × p
deﬁnita nel modo seguente: l’elemento (AB)ij della nuova matrice AB è
(AB)ij =
n
X
k=1
AikBkj = Ai1B1j + · · · + AinBnj.
Questo tipo di prodotto fra matrici si chiama prodotto riga per colonna perché l’elemento
(AB)ij si ottiene facendo un opportuno prodotto fra la riga i-esima Ai di A e la colonna j-
esima Bj di B, come suggerito dalla Figura 7.
37

<!-- pagina 38 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Figura 7. Il prodotto riga per colonna AB.
Esempio 8.8
Siano
A =


1
2
−1
1
0
3

,
B =
 −1
2
0
1
3
0
3
0

allora otteniamo
AB =


1
2
−1
1
0
3

·
 −1
2
0
1
3
0
3
0

=


5
2
6
1
4
−2
3
−1
9
0
9
0

.
Possiamo fare il prodotto AB perché il numero di colonne di A è pari al numero di righe di B.
Vice-versa, non possiamo fare il prodotto BA perché il numero di colonne di B è 4, mentre il
numero di righe di A è 3.
Esempio 8.9
Se A è una matrice m × n e x è una matrice n × 1, cioè un vettore colonna x ∈Kn, allora il
prodotto Ax è una matrice m × 1, cioè un vettore colonna in Km. Ad esempio:


1
2
−1
1
0
3

·

1
−1

=


−1
−2
−3


Attenzione: Se A e B sono due matrici n×n, possiamo deﬁnire sia il prodotto AB che il prodotto
BA. In generale, questi due prodotti non sono uguali, allora il prodotto non è commutativo.
38

<!-- pagina 39 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 8.10
Se A =
 1
0
0
0

e B =
 0
1
0
0

, allora
AB =
 0
1
0
0

= B,
BA =
 0
0
0
0

= 0
allora AB̸ = BA.
Valgono invece le proprietà seguenti.
Proposizione 8.11
Per ogni A, B, C matrici per cui i prodotti e le somme abbiano senso e per ogni λ ∈K, abbiamo
(1) A(BC) = (AB)C (associatività),
(2) A(B + C) = AB + AC & (A + B)C = AC + BC (distributività),
(3) λ(AB) = (λA)B = A(λB).
8.D
Traccia di una matrice quadrata
Deﬁnizione 8.12
La traccia di una matrice quadrata A ∈M(n) è il numero
tr A = A11 + · · · + Ann.
Cioè, la traccia di A è la somma dei numeri presenti sulla diagonale principale di A.
Proposizione 8.13
Se A, B ∈M(n), vale la relazione tr(AB) = tr(BA).
Spiegazione. Basta scrivere
tr(AB) =
n
X
i,j=1
AijBji =
n
X
j,i=1
BjiAij = tr(BA).
8.E
Esercizi
Esercizio 8.14
Dimostrare che vale la relazione
t(AB) = tBtA.
39

<!-- pagina 40 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esercizio 8.15
Siano
A =


1
2
3
4
5
6

,
B =
 1
2
3
4
5
6

.
Calcolare AB e BA. Calcolare la traccia di AB e di BA.
Esercizio 8.16
Siano
A =


1
2
3
4
5
6
7
8
9

,
B =


1
0
1
0
1
0
1
0
1

,
C =


−1
0
0
0
0
−1
0
−1
0

.
Calcolare (AB)C, A(BC), (BA)C, e C(BA).
40

<!-- pagina 41 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
9
Matrici II
9.A
Determinante di una matrice quadrata
Deﬁnizione 9.1
Sia A una matrice quadrata n × n. Il determinante di A è il numero
det A =
X
σ∈Sn
sgn(σ)a1σ(1) · · · anσ(n).
Qui Sn indica l’insieme delle n! permutazioni di {1, . . . , n}, si veda la parte di matematica
discreta del corso. Quindi questa è una sommatoria su n! elementi. Il termine sgn(σ) = ±1
indica il segno della permutazione σ ed è 1 oppure −1 a seconda di σ. Se σ è un prodotto di k
trasposizioni (permutazioni che scambiano due elementi e lasciano tutti gli altri elementi), allora
sgn(σ) = (−1)k. In seguito indichiamo la permutazione σ con il simbolo [σ(1) · · · σ(n)].
La deﬁnizione di det A non è facile da decifrare: cerchiamo di comprenderla meglio esaminando i
casi n = 1, 2, 3.
Se n = 1 la matrice A è un numero A = (a11), l’insieme S1 contiene solo la permutazione id = [1],
che ha segno positivo, e otteniamo semplicemente
det A = a11.
Se n = 2 la matrice A è
A =
 a11
a12
a21
a22

,
l’insieme S2 contiene due permutazioni id = [1 2] e [2 1]. Queste sono l’identità (che ha segno 1)
e una trasposizione (che ha segno −1). Quindi
det A = a11a22 −a12a21.
Se n = 3 la matrice è
A =


a11
a12
a13
a21
a22
a23
a31
a32
a33

.
L’insieme S3 contiene sei permutazioni:
id = [1 2 3],
[1 3 2],
[3 2 1],
[2 1 3],
[2 3 1],
[3 1 2].
Le tre trasposizioni hanno segno −1 e le altre tre permutazioni +1 . Quindi
det A = a11a22a33 −a11a23a32 −a13a22a31 −a12a21a33 + a12a23a31 + a13a21a32.
41

<!-- pagina 42 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 9.2
Il determinante delle matrici seguenti
(3),

1
2
−1
4

,


1
2
1
2
1
2
−1
0
1


è rispettivamente: 3,
4 −(−2) = 6,
1 −0 −4 + (−4) + 0 −(−1) = −6.
Il calcolo del determinante di una matrice triangolare è particolarmente semplice: è il prodotto dei
valori sulla diagonale principale.
Proposizione 9.3
Sia A ∈M(n) una matrice triangolare superiore
A =





a11
a12
. . .
a1n
0
a22
. . .
a2n
...
...
...
...
0
0
. . .
ann





Vale
det A = a11a22 · · · ann.
Spiegazione. Nella formula del determinante, per una matrice triangolare superiore tutti i prodotti
sono nulli tranne quello corrispondente alla permutazione identità. Quindi det A = a11 · · · ann.
Lo stesso risultato vale per le matrici triangolari inferiori.
Introduciamo una matrice che avrà un ruolo fondamentale in tutto il corso.
Deﬁnizione 9.4
La matrice identità di taglia n × n è la matrice
In =





1
0
· · ·
0
0
1
· · ·
0
...
...
...
...
0
0
· · ·
1





i cui coeﬃcienti sono 1 sulla diagonale principale e 0 altrove.
Per adesso ci limitiamo a notare che la matrice identità In è diagonale e det (In) = 1.
Un’altra proprietà che segue direttamente dalla deﬁnizione è questa.
42

<!-- pagina 43 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Proposizione 9.5
Vale det
 tA

= det A.
9.B
Sviluppo di Laplace
Ci sono vari algoritmi che permettono di calcolare il determinante di una matrice più agevolmente
che con la cruda deﬁnizione. Uno di questi è noto come lo sviluppo di Laplace e funziona nel modo
seguente.
Sia A una matrice n×n con n ≥2. Indichiamo con Cij la sottomatrice (n−1)×(n−1) ottenuta
da A rimuovendo la i-esima riga e la j-esima colonna.
Teorema 9.6 (Sviluppo di Laplace)
Per ogni i ﬁssato vale l’uguaglianza
det A =
n
X
j=1
(−1)i+jaij det Cij.
Notiamo inoltre che grazie al fatto che det
 tA

= det A, è anche possibile usare lo sviluppo di
Laplace sulle colonne.
Corollario 9.7
Per ogni j ﬁssato vale l’uguaglianza
det A =
n
X
i=1
(−1)i+jaij det Cij.
Esempio 9.8
Per calcolare il determinante seguente, sviluppiamo lungo la prima riga (cioè prendiamo i = 1 )
e otteniamo
det


1
−1
0
2
−1
5
1
1
−1

=1 · det
 −1
5
1
−1

−(−1) · det
 2
5
1
−1

+ 0 · det
 2
−1
1
1

= −4 −7 + 0 = −11
43

<!-- pagina 44 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
È chiaramente conveniente sviluppare lungo una riga che contiene degli zeri.
Esempio 9.9
Sviluppando la matrice seguente sulla seconda colonna otteniamo:
det


1
0
1
2
0
1
π
3
√
7

= (−1) · 3 · det
 1
1
2
1

= 3
Nello sviluppo si deve sempre fare attenzione al segno (−1)i+j associato alla casella ij, che varia
come su di una scacchiera.
9.C
Proprietà del determinante
Proposizione 9.10
Se gli elementi di una riga (o colonna) di A sono tutti nulli, allora det(A) = 0.
Questa è una conseguenza diretta dello sviluppo di Laplace: basta calcolare il determinante svilup-
pando secondo la riga (o colonna) tutta nulla.
Proposizione 9.11
Se la matrice A′ si ottiene dalla matrice A moltiplicando tutti gli elementi di una riga (o colonna)
per il numero c, allora det (A′) = c · det(A).
Corollario 9.12
Dalla proposizione otteniamo subito
det(cA) = cn · det(A)
e in particolare
det(−A) = (−1)n · det(A)
9.D
Esercizi
Esercizio 9.13
Calcoliamo il determinante della seguente matrice
A =




2 + i
0
−5
0
3 −i
1
2i
0
4 + 4i
−2
−1
0
−1
2
i
1 −i
i



.
44

<!-- pagina 45 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esercizio 9.14
Calcoliamo il determinante della seguente matrice
B =




5i
4
√
2
0
√
2
5i
8
√
2
0
−
√
2
−5i
−4
√
2
−1
2
√
2
−10i
4
√
2
1
√
2



.
45

<!-- pagina 46 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
10
Matrici III
10.A
Altre proprietà del determinante
Proposizione 10.1
Sia A una matrice n × n.
(1) Se A′ è ottenuta da A scambiando due righe, allora abbiamo det (A′) = −det(A).
(2) Se A′ è ottenuta da A moltiplicando una riga di A per uno scalare λ, allora abbiamo
det (A′) = λ det(A).
(3) Se A′ è ottenuta da A aggiungendo ad una riga il multiplo di un’altra riga, allora abbiamo
det (A′) = det A.
Le identiche regole valgono anche per le colonne (invece delle righe).
Il processo di ottenere A′ da A in uno dei tre modi sopra si chiama una mossa di Gauss.
Spiegazione. La (1) segue, per induzione sull’ordine, sviluppando il determinante lungo una riga
non scambiata; la (2) è la Proposizione precedente. Per la (3), aggiungendo a una riga un multiplo
di un’altra, il termine aggiuntivo è il determinante di una matrice con due righe uguali e quindi è
nullo. Le regole per le colonne seguono applicando det(tA) = det A.
Esempio 10.2
Sia A la matrice
A =


1
2
3
4
5
6
7
8
9

.
Se togliamo la prima riga di A dalla seconda e dalla terza riga, otteniamo una nuova matrice
A′ =


1
2
3
3
3
3
6
6
6

.
Visto che si tratta di una mossa di Gauss del terzo tipo, allora det (A′) = det(A).
Ora possiamo togliere 2 volte la seconda riga dalla terza riga. Otteniamo allora la matrice
A′′ =


1
2
3
3
3
3
0
0
0


con det(A′′) = det (A′) = det(A). Visto che A′′ ha una riga con solo entrate 0, abbiamo
det(A′′) = 0 e allora anche la matrice A ha determinante 0.
46

<!-- pagina 47 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Una conseguenza di questa proposizione è la seguente proprietà.
Proposizione 10.3
det(A) = 0 se e solo se una riga (o una colonna) di A è combinazione lineare delle altre.
Infatti, supponiamo ad esempio che la prima riga di A sia combinazione lineare delle altre, cioè che
esistano dei numeri c2, . . . , cn tali che
A1 = c2A2 + · · · + cnAn.
Sia A′ la matrice che si ottiene da A sostituendo la prima riga con la riga nulla. Per la Proprietà
1, abbiamo che det (A′) = 0. Ora applicando ripetutamente il terzo tipo di mossa di Gauss come
nella proposizione sopra alla matrice A′, possiamo sommare alla sua prima riga prima c2A2 poi
c3A3 e così via ﬁno a cnAn senza che il determinante cambi. La matrice ﬁnale sarà esattamente
A. Pertanto det(A) = det (A′) = 0. La proposizione dice che vale anche l’altra direzione.
Includiamo un’altra proprietà senza dimostrazione.
Teorema 10.4 (Teorema di Binet)
Se A e B sono matrici quadrate dello stesso ordine allora
det(A · B) = det(A) · det(B).
Deﬁnizione 10.5
Una matrice quadrata A ∈M(n) è invertibile se esiste una matrice B ∈M(n) tale che
AB = In = BA.
Attenzione: solo una delle due identità non basta! Se esiste una tale matrice B, allora è unica
e si chiama l’inversa di A, denotata B = A−1.
Una conseguenza del Teorema di Binet è la seguente proprietà.
Corollario 10.6
Sia A una matrice quadrata invertibile. Allora
det
 A−1
=
1
det(A).
Spiegazione. Dal Teorema di Binet e da AA−1 = In otteniamo
1 = det(In) = det(A) det(A−1),
da cui la formula.
47

<!-- pagina 48 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
10.B
Cofattori di una matrice
Deﬁnizione 10.7
Consideriamo una matrice quadrata A. I suoi cofattori cofij := (−1)i+j det(Cij) formano una
matrice quadrata di ordine n
cof(A) = (cofij)
detta matrice dei cofattori di A.
Possiamo riscrivere lo sviluppo di Laplace lungo la i-esima riga:
det A =
n
X
j=1
aij cofij
∀i ∈{1, . . . , n}.
Dall’altro lato, dalla dimostrazione di (3) della prima proposizione in questa lezione sappiamo che
la somma dei prodotti degli elementi di una riga (o colonna) qualsiasi per i cofattori di un’altra
riga (o di un’altra colonna) è 0. In formule
0 =
n
X
j=1
aij cofkj
∀i, k ∈{1, . . . , n}, i̸ = k.
Abbiamo allora
Proposizione 10.8
A · t(cof(A)) = det(A) · In = t(cof(A)) · A.
Dimostrazione. Sia K = A · t(cof(A)). La sua entrata (i, j) è
kij =
X
ℓ
aiℓcofjℓ.
Se i = j, questo è lo sviluppo di Laplace di det(A) lungo la riga i. Se i̸ = j, è il determinante
della matrice ottenuta sostituendo la riga j con la riga i, quindi è nullo perché la matrice ha due
righe uguali. Dunque K = det(A)In. In modo analogo si dimostra t(cof(A))A = det(A)In.
10.C
L’inversa di una matrice
Proposizione 10.9
Sia A una matrice quadrata di ordine n ≥2. La matrice A è invertibile se e solo se det(A)̸ = 0.
Se A è invertibile, allora
A−1 =
1
det(A) · t(cof(A)).
Dimostrazione. Se A è invertibile allora esiste una matrice B tale che A · B = In. Per il Teorema
di Binet
det(A · B) = det(A) · det(B).
48

<!-- pagina 49 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
D’altra parte, det (In) = 1. Ne deduciamo che det(A) · det(B) = 1 e quindi det(A)̸ = 0.
Viceversa, sia ora A tale che det(A)̸ = 0. Deﬁniamo B :=
1
det(A) · t(cof(A)).
Per la proprietà precedente A · t(cof(A)) = det(A) · In = t(cof(A)) · A. Dato che det(A)̸ = 0
possiamo moltiplicare per
1
det(A) ottenendo A · B = In = B · A. Abbiamo così dimostrato che A
è invertibile e che la sua inversa è B.
10.D
Esercizi
Esercizio 10.10
Determinare per quali valori del parametro k ∈R la seguente matrice è invertibile.
A =
 k −5
3
−2
k

Per ogni k per cui la matrice risulta invertibile, trovare la matrice inversa.
Esercizio 10.11
Dimostrare che la matrice
B =


2
−1
0
−2
1
1
1
−1
3


è invertibile e calcolarne l’inversa.
Esercizio 10.12
Si calcoli l’inversa della matrice
C =
 2 −i
0
3
2 + i

49

<!-- pagina 50 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
11
Sistemi Lineari I
11.A
Deﬁnizioni
Deﬁnizione 11.1
Un sistema lineare è un insieme di k equazioni lineari in n variabili





a11x1 + · · · + a1nxn = b1,
...
ak1x1 + · · · + aknxn = bk.
I numeri aij sono i coeﬃcienti e i bi sono i termini noti del sistema. Sia i coeﬃcienti sia i
termini noti sia le variabili sono in un certo campo ﬁssato K. Possiamo raggruppare i coeﬃcienti
e i termini noti eﬃcacemente in una matrice k × n e un vettore colonna:
A =



a11
· · ·
a1n
...
...
...
ak1
· · ·
akn


,
b =



b1
...
bk


.
Parliamo della matrice dei coeﬃcienti e del vettore dei termini noti. Possiamo poi unire
tutto in un’unica matrice k × (n + 1) :
C = (A | b),
chiamata matrice completa.
Il nostro scopo è determinare l’insieme S ⊂Kn delle soluzioni del sistema. A questo scopo, notiamo
che esistono alcune mosse che cambiano la matrice C senza modiﬁcare l’insieme S delle soluzioni
del sistema.
Deﬁnizione 11.2
Le mosse che non cambiano l’insieme delle soluzioni sono le seguenti e sono note come mosse
di Gauss:
(I) Scambiare due righe.
(II) Moltiplicare una riga per un numero λ̸ = 0.
(III) Aggiungere ad una riga un’altra riga moltiplicata per λ qualsiasi.
Indicando con Ri la i-esima riga di C, possiamo scrivere le mosse così:
(I) Ri ←→Rj,
(II) Ri −→λRi, λ̸ = 0,
(III) Ri −→Ri + λRj.
50

<!-- pagina 51 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 11.3
Ecco qualche composizione di mosse di tipo (I), (II) e (III):


1
2
3
0
4
−2

R1↔R3
−→


4
−2
3
0
1
2

R1→1
2 R1
−→


2
−1
3
0
1
2

R2→R2+2R3
−→


2
−1
5
4
1
2

.
Torniamo al sistema lineare iniziale, determinato dalla matrice C = (A | b).
Proposizione 11.4
Le mosse di Gauss su C = (A | b) non cambiano l’insieme S ⊂Kn delle soluzioni del sistema
lineare.
Dimostrazione. La mossa (I) scambia due equazioni e questo chiaramente non tocca S. La mossa
(II) moltiplica un’equazione lineare
ai1x1 + · · · + ainxn = bi
per una costante λ̸ = 0, trasformandola quindi in
λai1x1 + · · · + λainxn = λbi.
Anche qui le soluzioni sono chiaramente le stesse di prima. L’eﬀetto della mossa (III) sulle equazioni
lineari corrispondenti alle righe i e j è il seguente: cambiamo le due equazioni
ai1x1 + · · · + ainxn = bi
aj1x1 + · · · + ajnxn = bj
con
(ai1 + λaj1) x1 + · · · + (ain + λajn) xn = bi + λbj
aj1x1 + · · · + ajnxn = bj
È facile convincersi che x ∈Kn è soluzione delle prime due se e solo se è soluzione delle seconde
due.
11.B
Algoritmo di Gauss
Introduciamo un algoritmo che può essere usato per risolvere qualsiasi sistema lineare. L’algoritmo
trasforma un’arbitraria matrice C in una matrice particolare detta a scalini.
Deﬁnizione 11.5
Sia C una matrice qualsiasi. Per ogni riga Ri di C, chiamiamo pivot il primo elemento non
nullo della riga. Una matrice a scalini è una matrice in cui tutte le righe nulle sono in fondo e il
pivot di ogni riga non nulla è strettamente più a destra del pivot della riga non nulla precedente.
51

<!-- pagina 52 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 11.6
Le seguenti matrici sono matrici a scalini:
 1
0
5
0
−1
−1

,


7
−2
9
0
0
1
0
0
0


mentre non sono matrici a scalini:


1
2
−1
4
0
6
0
7
0

,




0
8
0
1
0
0
0
0



.
L’algoritmo di Gauss è un algoritmo che trasforma qualsiasi matrice C in una matrice a scalini
usando le 3 mosse di Gauss descritte precedentemente. Funziona così:
(1) Se C11 = 0 e Ci1̸ = 0 per qualche i, scambiamo la prima riga con una riga in modo da ottenere
C11̸ = 0. Se invece Ci1 = 0 per ogni i, continuiamo dal punto (1) lavorando sulla sottomatrice
ottenuta togliendo soltanto la prima colonna.
(2) Per ogni riga Ri con i ≥2 e con Ci1̸ = 0 sostituiamo Ri con la riga
Ri −Ci1
C11
R1.
In questo modo la nuova riga Ri avrà Ci1 = 0.
(3) Abbiamo ottenuto Ci1 = 0 per ogni i ≥2.
Continuiamo dal punto (1) lavorando sulla
sottomatrice ottenuta togliendo la prima riga e la prima colonna.
Esempio 11.7
Partiamo dalla matrice
C =


0
1
1
0
1
1
2
−3
−1
2
1
1


Notiamo che C11 = 0. Quindi scambiamo R1 e R2 in modo da ottenere C11̸ = 0. Ad ogni
passaggio chiamiamo sempre la nuova matrice con la lettera C per semplicità. Otteniamo
C =


1
1
2
−3
0
1
1
0
−1
2
1
1

.
Ora notiamo che C31̸ = 0. Cambiamo R3 con R3 +R1 in modo da ottenere C31 = 0. Il risultato
52

<!-- pagina 53 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
è
C =


1
1
2
−3
0
1
1
0
0
3
3
−2


La prima riga e la prima colonna adesso sono a posto, quindi lavoriamo sul resto. Notiamo che
C32̸ = 0. Sostituiamo R3 con R3 −3R2 in modo da ottenere C32 = 0. Il risultato è
C =


1
1
2
−3
0
1
1
0
0
0
0
−2

.
Adesso la matrice è a scalini e l’algoritmo termina.
11.C
Algoritmo di Gauss–Jordan
Per un motivo che sarà chiaro in seguito, dopo aver ridotto la matrice a scalini, è a volte utile fare
delle ulteriori mosse di Gauss per fare in modo che tutti i numeri sopra i pivot siano nulli. Questo
è sempre possibile usando mosse di Gauss di tipo (III), aggiungendo la riga che contiene il pivot
(moltiplicata per una costante opportuna) alle righe precedenti.
Esempio 11.8
Nella matrice C ottenuta precedentemente abbiamo C12̸ = 0. Per ottenere C12 = 0 possiamo
sostituire R1 con R1 −R2. Il risultato è una nuova matrice
C =


1
0
1
−3
0
1
1
0
0
0
0
−2

.
Adesso notiamo che C14̸ = 0. Per ottenere C14 = 0 sostituiamo R1 con R1 −3
2R3 e otteniamo
inﬁne
C =


1
0
1
0
0
1
1
0
0
0
0
−2

.
Come ultimo ritocco, vedremo che sarà anche utile ottenere che tutti i pivot abbiano valore 1 . È
sempre possibile ottenere questo semplicemente con mosse di Gauss di tipo (II).
Esempio 11.9
Nel nostro esempio, i pivot C11 e C22 hanno già valore 1, però C34 = −2. Per ottenere C34 = 1
dividiamo la terza riga per −2 . Il risultato ﬁnale è
C =


1
0
1
0
0
1
1
0
0
0
0
1

.
53

<!-- pagina 54 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
L’algoritmo che abbiamo appena descritto si chiama algoritmo di Gauss–Jordan. Consiste in
due fasi:
(1) Trasformare la matrice a scalini tramite l’algoritmo di Gauss.
(2) Ottenere solo zeri sopra i pivot con mosse (III) e tutti i pivot uguali a 1 con mosse (II).
Facciamo un altro esempio di applicazione dell’algoritmo di Gauss–Jordan.
Sopra ogni freccia
indichiamo la mossa di Gauss corrispondente.
Esempio 11.10


1
−1
3
0
2
2
1
0
4

R3→R3−R1
−→


1
−1
3
0
2
2
0
1
1

R3→R3−1
2 R2
−→


1
−1
3
0
2
2
0
0
0


R1→R1+ 1
2 R2
−→


1
0
4
0
2
2
0
0
0

R2→1
2 R2
−→


1
0
4
0
1
1
0
0
0


11.D
Risoluzione di un sistema lineare
Mostriamo adesso come sia possibile descrivere esplicitamente lo spazio S ⊂Kn delle soluzioni di
un dato sistema lineare.
Il sistema è descritto da una matrice C = (A | b). Usando l’algoritmo di Gauss–Jordan, possiamo
trasformare C in una matrice a scalini, in cui ogni pivot ha valore 1 e tutti i numeri sopra i pivot
sono nulli. La matrice C sarà indicativamente di questo tipo:


0
1
?
0
0
?
?
0
0
0
1
0
?
?
0
0
0
0
1
?
?


Adesso guardiamo le colonne che contengono i pivot, che in questo esempio sono la seconda, la
quarta e la quinta. Ciascuna di queste colonne contiene un 1 al posto del pivot e 0 in tutte le altre
caselle. Ci sono due casi da considerare. Se la colonna dei termini noti b contiene un pivot, allora
la matrice è indicativamente di questo tipo:


0
1
?
0
0
?
?
0
0
0
1
0
?
?
0
0
0
0
0
0
1

.
La riga che contiene l’ultimo pivot rappresenta l’equazione 0 = 1 che chiaramente non può avere
soluzione. In questo caso l’insieme S delle soluzioni è vuoto, cioè S = ∅.
Consideriamo adesso il caso in cui l’ultima colonna non contenga pivot. La matrice C è indicati-
vamente di questo tipo:


0
1
a13
0
0
a16
b1
0
0
0
1
0
a26
b2
0
0
0
0
1
a36
b3

.
54

<!-- pagina 55 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Ricordiamo che ciascuna colonna corrisponde ad una variabile x1, . . . , xn, eccetto l’ultima che con-
tiene i termini noti. Adesso assegniamo un parametro t1, t2, . . . a ciascuna variabile che corrisponde
ad una colonna che non contiene un pivot. Nel nostro caso, scriviamo x1 = t1, x3 = t2 e x6 = t3.
Conseguentemente il sistema lineare è di questa forma:



x2 + a13t2 + a16t3 = b1
x4 + a26t3 = b2
x5 + a36t3 = b3.
Spostiamo a destra dell’uguale tutti i nuovi parametri e otteniamo:



x2 = b1 −a13t2 −a16t3
x4 = b2 −a26t3
x5 = b3 −a36t3
Al sistema aggiungiamo anche le equazioni corrispondenti alle assegnazioni dei parametri liberi, che
nel nostro caso sono x1 = t1, x3 = t2 e x6 = t3. Il risultato è un sistema del tipo:















x1 = t1
x2 = b1 −a13t2 −a16t3
x3 = t2
x4 = b2 −a26t3
x5 = b3 −a36t3
x6 = t3
Il sistema è risolto. I parametri t1, t2, . . . sono liberi e possono assumere qualsiasi valore in K, e le
variabili x1, . . . , xn dipendono da questi parametri liberi come indicato.
11.E
Esercizi
Esercizio 11.11
Risolvere il sistema lineare



x + y + 2z = 9
2x + 4y −3z = 1
3x + 6y −5z = 0.
[Soluzione: x = 1, y = 2, z = 3.]
55

<!-- pagina 56 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
12
Sistemi Lineari II
Nella lezione precedente abbiamo visto come risolvere un sistema lineare tramite l’algoritmo di
Gauss–Jordan. In questa lezione studiamo il problema in modo più teorico.
12.A
Il sistema omogeneo associato
Consideriamo un sistema di equazioni lineari





a11x1 + · · · + a1nxn = b1,
...
ak1x1 + · · · + aknxn = bk.
(12.1)
Deﬁnizione 12.1
Il sistema omogeneo associato è quello ottenuto semplicemente mettendo a zero tutti i termini
noti bi, cioè:





a11x1 + · · · + a1nxn = 0,
...
ak1x1 + · · · + aknxn = 0.
(12.2)
Scriviamo la matrice A = (aij) dei coeﬃcienti ed il vettore b = (bi) dei termini noti. La matrice
C = (A | b) rappresenta il sistema lineare iniziale, mentre (A | 0), oppure più semplicemente A,
rappresenta il sistema lineare omogeneo associato.
Sia S ⊂Kn l’insieme delle soluzioni del sistema lineare iniziale e S0 ⊂Kn l’insieme delle soluzioni
del sistema omogeneo associato.
Proposizione 12.2
Le soluzioni S0 ⊂Kn formano un sottospazio vettoriale di Kn.
Dimostrazione. Dobbiamo veriﬁcare i 3 assiomi di sottospazio per l’insieme S0 delle soluzioni.
(1) Il vettore 0 è soluzione, infatti per ogni equazione troviamo
ai10 + · · · + ain0 = 0.
Quindi 0 ∈S0.
(2) Se due vettori x e y sono soluzioni, allora anche x + y è soluzione. Infatti per ogni equazione
troviamo
ai1 (x1 + y1) + · · · + ain (xn + yn) =
ai1x1 + · · · + ainxn + ai1y1 + · · · + ainyn = 0 + 0 = 0.
(3) Se x è soluzione e λ ∈K è uno scalare, allora anche λx è soluzione. Infatti per ogni equazione
troviamo
ai1 (λx1) + · · · + ain (λxn) =
λ (ai1x1 + · · · + ainxn) = λ0 = 0.
Quindi S0 è un sottospazio vettoriale di Kn.
56

<!-- pagina 57 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
S invece non è un sottospazio perché non contiene l’origine – a meno che il sistema lineare iniziale
non sia già omogeneo e in questo caso S = S0.
I due insiemi S e S0 sono strettamente correlati:
Proposizione 12.3
Se S̸ = ∅, allora S è ottenuto prendendo una qualsiasi soluzione x ∈S e aggiungendo a questa
tutti i vettori di S0.
Per vedere che questa proposizione vale, prendiamo x ∈S una soluzione del sistema (12.1) e
x′ ∈S0 una soluzione del sistema omogeneo (12.2). Si vede facilmente che x + x′ è anch’essa
soluzione di (12.1) perché
ai1
 x1 + x′
1

+ · · · + ain
 xn + x′
n

= bi + 0 = bi.
Se invece x′′ è soluzione di (12.1), allora x′ = x′′ −x è soluzione di (12.2) perché
ai1
 x′′
1 −x1

+ · · · + ain
 x′′
n −xn

= bi −bi = 0.
e quindi le soluzioni di (12.1) si ottengono tutte precisamente aggiungendo ad un ﬁssato x ∈S le
soluzioni x′ ∈S0 di (12.2).
La soluzione x è a volte detta soluzione particolare. Le soluzioni di un sistema si ottengono
aggiungendo ad una soluzione particolare tutte le soluzioni del sistema omogeneo associato.
Esempio 12.4
Consideriamo il sistema in R3
(
x −y + z = 1
y −z = 2
Le soluzioni S0 del sistema omogeneo associato
(
x −y + z = 0
y −z = 0
sono precisamente i vettori del tipo


0
t
t


Le soluzioni in S sono tutte ottenute prendendo la soluzione particolare


3
0
−2

,
57

<!-- pagina 58 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
allora le soluzioni S sono del tipo


3
0
−2

+


0
t
t

=


3
t
t −2


al variare di t ∈R.
Deﬁnizione 12.5
Geometricamente, S è un sottospazio aﬃne: Sia V uno spazio vettoriale. Un sottospazio aﬃne
di V è un qualsiasi sottoinsieme del tipo
S = {x + v | v ∈W} =: x + W
dove x è un punto ﬁssato di V e W ⊂V è un sottospazio vettoriale. La dimensione di S è la
dimensione del sottospazio W.
12.B
Teorema di Rouché–Capelli
Il sistema (12.1) può essere riscritto nel modo
x1A1 + · · · + xnAn = b,
dove A1, . . . , An sono le colonne di A. A questo punto è chiaro che esistono soluzioni se e solo se
b è combinazione lineare delle colonne A1, . . . , An, con coeﬃcienti x1, . . . , xn, o in altre parole: Il
sistema (12.1) ha soluzioni se e solo se
b ∈Span
 A1, . . . , An
.
Ci ricordiamo che il rango di A è il massimo numero di colonne linearmente indipendenti di A.
Le mosse di Gauss non cambiano lo spazio generato dalle righe e quindi non cambiano il rango
(per righe). Possiamo applicare l’algoritmo di Gauss–Jordan per fare in modo che le k colonne
contenenti i pivot siano precisamente i primi k vettori e1, . . . , ek della base canonica di Km. Tutte
le altre colonne sono combinazioni lineari di questi. Concludiamo allora che il rango di A è il
numero di pivot in una sua (qualsiasi) riduzione a scalini. Passiamo al teorema più importante di
questa lezione.
Teorema 12.6 (Rouché–Capelli)
Il sistema (12.1) ha soluzioni se e solo se
rk(A | b) = rk(A).
In caso aﬀermativo, lo spazio delle soluzioni S ⊂Kn è un sottospazio aﬃne di dimensione
n −rk(A).
58

<!-- pagina 59 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Dimostrazione. Sappiamo che il sistema ha soluzioni se e solo se
b ∈Span
 A1, . . . , An
.
Questo accade, se e solo se
Span
 A1, . . . , An, b

= Span
 A1, . . . , An
e quindi se e solo se rk(A | b) = rk(A). Se ci sono soluzioni, sappiamo che la dimensione di S è
pari alla dimensione dello spazio S0 delle soluzioni del sistema lineare omogeneo associato. Dopo
aver eﬀettuato l’algoritmo di Gauss–Jordan, abbiamo già visto nella Lezione 11 che S0 è generato
da un numero di vettori indipendenti pari a n meno il numero di pivot, cioè n −rk(A). Quindi
dim S = dim S0 = n −rk(A).
Nel corollario seguente supponiamo che K sia un campo inﬁnito, come ad esempio Q, R e C.
Corollario 12.7
Il sistema (12.1) ha 0, 1 oppure ∞soluzioni. Più precisamente, le soluzioni sono
• 0 se rk(A | b) > rk A,
• 1 se rk(A | b) = rk A = n,
• ∞se rk(A | b) = rk A < n.
Corollario 12.8
Se A è una matrice quadrata (allora il numero di equazioni è uguale al numero di variabili), il
sistema Ax = b ha esattamente una soluzione se rk A = n ⇔det A̸ = 0. In questo caso A è
invertibile e la soluzione è x = A−1b.
Collegamento con l’informatica: programmazione lineare e metodo del simplesso
In un corso successivo di ottimizzazione si studiano problemi di programmazione lineare del
tipo
max{tcx | Ax = b, x ≥0}.
Il metodo del simplesso usa contemporaneamente molti concetti introdotti ﬁn qui. Se A ha m
righe e rango m, una base del simplesso è una scelta di m colonne linearmente indipendenti
di A. Esse formano una matrice quadrata AB invertibile. Ponendo uguali a zero le variabili
corrispondenti alle altre colonne, le variabili di base si ottengono risolvendo
ABxB = b,
cioè
xB = A−1
B b.
Le nozioni di indipendenza lineare, base, rango, matrice invertibile e soluzione di un sistema
lineare compaiono quindi tutte insieme in uno degli algoritmi fondamentali dell’ottimizzazione.
59

<!-- pagina 60 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 12.9
Consideriamo un sistema lineare dipendente da un parametro k ∈R
(
x + ky = 4 −k
kx + 4y = 4
a) Vogliamo sapere al variare di k ∈R se ci siano soluzioni e, in caso aﬀermativo, che dimensione
abbiano.
b) Vogliamo risolvere il sistema per k = 1.
Soluzione: a) Applichiamo l’algoritmo di Gauss su (A | b) :
 1
k
4 −k
k
4
4

→
 1
k
4 −k
0
4 −k2
4 −4k + k2

Per calcolare il rango è suﬃciente fermarsi qui, non è necessario proseguire con l’algoritmo di
Gauss–Jordan che è utile solo se vogliamo determinare precisamente le soluzioni. Notiamo che
4 −4k + k2 = (k −2)2. La matrice è ridotta a scalini per tutti i possibili valori di k ∈R e ci
sono sempre due pivot, tranne per k = 2 in cui ce n’è uno solo. Quindi il rango di (A | b) è 1
per k = 2 e 2 per k̸ = 2. La matrice dei coeﬃcienti A con le mosse di Gauss è diventata
 1
k
0
4 −k2

ed ha rango 1 per k = ±2 e rango 2 per k̸ = ±2. Quindi:
• Se k = −2, allora rk(A | b)̸ = rk(A) e non ci sono soluzioni.
• Se k = 2, allora rk(A | b) = rk(A) = 1, quindi le soluzioni formano un sottospazio aﬃne
di R2 di dimensione 2 −1 = 1, cioè una retta aﬃne. Ci sono inﬁnite soluzioni.
• Se k̸ = ±2, allora rk(A | b) = rk(A) = 2, quindi le soluzioni formano un sottospazio aﬃne
di R2 di dimensione 2 −2 = 0, cioè un punto. C’è una soluzione sola.
b) Per k = 1 abbiamo un’unica soluzione di
 1
k
4 −k
0
4 −k2
4 −4k + k2

=
 1
1
3
0
3
1

.
Notiamo prima (dalla seconda riga) che 3y = 1 e allora y = 1/3. Poi (dalla prima riga), si
ottiene x = 3 −y = 3 −1/3 = 8/3.
60

<!-- pagina 61 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
12.C
Esercizi
Esercizio 12.10
Quante soluzioni ha il sistema lineare con matrice completa


1
3
5
2
7
9
11
2
13
15
17
0

?
Esercizio 12.11
Trovare tutte le soluzioni del sistema lineare





2x −y −z = 3,
x −y + z = 2,
3x −y −3z = 4.
61

<!-- pagina 62 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
13
Sistemi Lineari III
Vogliamo adesso studiare qualche applicazione della teoria dei sistemi lineari.
Prima studiamo
alcune applicazioni di quanto imparato nella Lezione 7 sugli spazi vettoriali.
13.A
(In)dipendenza lineare
Sia V uno spazio vettoriale su K e siano v1, . . . , vk ∈V alcuni vettori. Ci ricordiamo che diciamo
che questi vettori sono linearmente dipendenti se esistono dei coeﬃcienti λ1, . . . , λk ∈K, non
tutti nulli, tali che
λ1v1 + · · · + λkvk = 0.
(13.1)
Invece v1, . . . , vk ∈V sono linearmente indipendenti se l’unica soluzione di (13.1) è λ1 = . . . =
λk = 0.
Esempio 13.1
Consideriamo tre vettori in R3,
v1 =


1
1
0

,
v2 =


0
1
1

,
v3 =


1
0
−1


Dobbiamo studiare allora le soluzioni di
λ1


1
1
0

+ λ2


0
1
1

+ λ3


1
0
−1

= 0
o equivalentemente il sistema lineare omogeneo



λ1 + λ3 = 0,
λ1 + λ2 = 0,
λ2 −λ3 = 0.
La matrice dei coeﬃcienti è
A =


1
0
1
1
1
0
0
1
−1

= (v1 | v2 | v3)
Abbiamo visto nell’ultima lezione che questo sistema ha un’unica soluzione se det A̸ = 0. Vedi-
amo però subito (sviluppo lungo la prima riga) che
det A = det
 1
0
1
−1

+ det
 1
1
0
1

= −1 + 1 = 0,
allora esiste un numero inﬁnito di soluzioni e i vettori sono linearmente dipendenti.
62

<!-- pagina 63 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Alternativamente usiamo mosse di Gauss:
A =


1
0
1
1
1
0
0
1
−1

A2→A2−A1
−→


1
0
1
0
1
−1
0
1
−1

A3→A3−A2
−→


1
0
1
0
1
−1
0
0
0


Vediamo allora che A ha rango 2 che di nuovo ci dice che esiste un numero inﬁnito di soluzioni
(λ1, λ2, λ3) e allora i vettori sono linearmente dipendenti.
Alternativamente, se A ha rango 2, vuol dire che Span(v1, v2, v3) ha dimensione 2, allora i vettori
sono linearmente dipendenti (perché se no, generano uno spazio di dimensione 3).
13.B
Spazio generato da vettori
Sia V uno spazio vettoriale su K e siano v1, . . . , vk ∈V alcuni vettori. Ci ricordiamo che questi
vettori sono generatori di V (Span(v1, . . . , vk) = V ) se ogni vettore v ∈V è combinazione lineare
di v1, . . . , vk. Questo vuol dire che dato qualsiasi v ∈V , esistono dei coeﬃcienti λ1, . . . , λk ∈K,
tali che
λ1v1 + · · · + λkvk = v.
(13.2)
Esempio 13.2
Consideriamo di nuovo tre vettori in R3,
w1 =


1
1
0

,
w2 =


0
1
1

,
w3 =


1
1
−1


Dato un qualsiasi vettore v =


a
b
c

, dobbiamo allora studiare le soluzioni di
λ1


1
1
0

+ λ2


0
1
1

+ λ3


1
1
−1

=


a
b
c


o equivalentemente il sistema lineare



λ1 + λ3 = a,
λ1 + λ2 + λ3 = b,
λ2 −λ3 = c.
La matrice dei coeﬃcienti è
A =


1
0
1
1
1
1
0
1
−1

= (w1 | w2 | w3)
63

<!-- pagina 64 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Visto che
det A = det
 1
1
1
−1

+ det
 1
1
0
1

= −2 + 1 = −1̸ = 0,
A è invertibile (e allora ha rango 3) e il sistema ha sempre una soluzione (per qualsiasi v). Allora
Span(w1, w2, w3) = R3.
Alternativamente usiamo mosse di Gauss:
A =


1
0
1
1
1
1
0
1
−1

A2→A2−A1
−→


1
0
1
0
1
0
0
1
−1

A3→A3−A2
−→


1
0
1
0
1
0
0
0
−1


Vediamo allora anche da questo che A ha rango 3, che vuol dire che Span(w1, w2, w3) ha dimen-
sione 3 e allora Span(w1, w2, w3) = R3 perché ogni altro sottospazio ha dimensione strettamente
minore di 3.
13.C
Basi
Ci ricordiamo che una sequenza v1, . . . , vn ∈V di vettori è una base se sono soddisfatte entrambe
queste condizioni:
(i) i vettori v1, . . . , vn sono indipendenti;
(ii) i vettori v1, . . . , vn generano V .
Ci ricordiamo anche che se sappiamo già che V ha dimensione n basta controllare una delle due
proprietà (l’altra segue automaticamente).
Esempio 13.3
v1, v2, v3 dell’Esempio 13.1 non formano una base di R3 perché non sono linearmente indipen-
denti. Invece w1, w2, w3 dell’Esempio 13.2 formano una base di R3 visto che sono generatori e
sono tre vettori (e R3 ha dimensione 3). Devono allora per forza essere linearmente indipendenti,
un fatto che si veriﬁca anche subito in modo diretto.
13.D
Coordinate
Proposizione 13.4
Sia V uno spazio vettoriale e sia v1, . . . , vn una base di V . Ogni vettore v ∈V si scrive in modo
unico come
v = λ1v1 + · · · + λnvn
Dimostrazione. Sappiamo che i v1, . . . , vn generano, quindi sicuramente v si può scrivere come
combinazione lineare dei v1, . . . , vn. Supponiamo che lo si possa fare in due modi diversi:
v = λ1v1 + · · · + λnvn = µ1v1 + · · · + µnvn.
64

<!-- pagina 65 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Spostando tutto a sinistra otteniamo
(λ1 −µ1) v1 + · · · + (λn −µn) vn = 0.
Siccome i vettori sono indipendenti, necessariamente µi = λi per ogni i.
Deﬁnizione 13.5
I coeﬃcienti λ1, . . . , λn sono le coordinate di v rispetto alla base v1, . . . , vn. Il vettore colonna
di coordinate è il vettore



λ1
...
λn


.
Esempio 13.6
Sia e1, e2, e3 la base canonica di R3. Sia v il vettore
v =


3
4
5

.
Le coordinate rispetto alla base canonica sono proprio i coeﬃcienti di v, visto che
3e1 + 4e2 + 5e3 = 3


1
0
0

+ 4


0
1
0

+ 5


0
0
1

=


3
4
5


Allora il vettore di coordinate di v è proprio il vettore v. Questo non è più vero se usiamo un’altra
base. Sia per esempio w1, w2, w3 la base dell’Esempio 13.2. Per trovare le coordinate di v in
questa base, dobbiamo risolvere il sistema lineare
λ1


1
1
0

+ λ2


0
1
1

+ λ3


1
1
−1

=


3
4
5


Abbiamo già visto in Esempio 13.2 che troviamo sempre un’unica soluzione perché det A = −1.
In particolare, il vettore di coordinate di v in questa base è
A−1


3
4
5

=


2
−1
1
−1
1
0
−1
1
−1




3
4
5

=


7
1
−4

.
Alternativamente possiamo risolvere il sistema con l’algoritmo di Gauss-Jordan.
65

<!-- pagina 66 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Collegamento con l’informatica: codici di correzione degli errori
L’algebra lineare permette di aggiungere informazione ridondante a un messaggio in modo da
riconoscere, e in alcuni casi correggere, errori di trasmissione.
Vediamo un modello molto
sempliﬁcato. Vogliamo trasmettere i quattro numeri
{2, −7, 8, −2}.
Aggiungiamo due numeri a, b e interpretiamo i sei numeri come coeﬃcienti del polinomio
s(x) = 2x5 −7x4 + 8x3 −2x2 + ax + b.
Scegliamo a, b imponendo due condizioni di controllo,
s(1) = s(2) = 0.
Otteniamo il sistema lineare
(
a + b = −1,
2a + b = −8,
che ha soluzione a = −7, b = 6. Trasmettiamo quindi
{2, −7, 8, −2, −7, 6}.
Chi riceve il messaggio ricostruisce il polinomio e controlla che s(1) = s(2) = 0. Se una delle
due uguaglianze non vale, sa che si è veriﬁcato un errore.
Le stesse due condizioni possono anche aiutare a correggere un singolo errore. Supponiamo,
per esempio, di ricevere
{2, −7, 8, 4, −7, 6},
cioè che il quarto numero sia stato alterato. Se non sappiamo quale posizione sia sbagliata,
possiamo sostituire a turno ciascun coeﬃciente con un’incognita k e imporre nuovamente s(1) =
s(2) = 0. Quando sostituiamo il quarto coeﬃciente otteniamo
(
k + 2 = 0,
4k + 8 = 0,
che ha l’unica soluzione k = −2. Per le altre posizioni il sistema risulta incompatibile. In questo
modo individuiamo la posizione dell’errore e ricostruiamo il dato corretto.
Aggiungendo più informazione ridondante possiamo correggere più errori. Per esempio, aggiun-
gendo quattro coeﬃcienti e imponendo
s(1) = s(2) = s(3) = s(4) = 0,
66

<!-- pagina 67 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
si ottiene un sistema lineare di quattro equazioni per i quattro coeﬃcienti aggiunti. Le quattro
condizioni forniscono poi abbastanza controlli per cercare e correggere, in questo modello, ﬁno
a due coeﬃcienti errati.
I codici di Reed–Solomon, usati tra l’altro nei QR code e in molti sistemi di memorizzazione
e trasmissione digitale, sfruttano idee algebriche strettamente collegate: si rappresentano i dati
mediante polinomi, si aggiunge ridondanza e si usano equazioni algebriche per localizzare e
correggere errori. I veri codici Reed–Solomon lavorano su campi ﬁniti, ma il semplice esempio
sopra mostra già il ruolo concreto di polinomi e sistemi lineari.
13.E
Esercizi
Esercizio 13.7
Riceviamo la sequenza di sei numeri
{1, −2, 3, 0, −1, 2}.
Sappiamo che i primi quattro numeri contengono l’informazione da trasmettere, mentre gli ultimi
due sono informazione ridondante per la correzione degli errori come spiegato sopra.
I sei numeri sono i coeﬃcienti del polinomio
s(x) = a5x5 + a4x4 + a3x3 + a2x2 + a1x + a0
e, se la trasmissione è corretta, devono valere le due condizioni
s(1) = s(2) = 0.
Sappiamo che durante la trasmissione esattamente uno dei sei numeri è stato modiﬁcato.
Determinare quale numero è sbagliato e trovare il suo valore corretto.
67

<!-- pagina 68 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
14
Applicazioni Lineari I
14.A
Deﬁnizione ed esempi
Deﬁnizione 14.1
Siano V e W due spazi vettoriali sullo stesso campo K. Un’applicazione lineare è una funzione
f : V −→W
tale che
(i) f(v + w) = f(v) + f(w) per ogni v, w ∈V ,
(ii) f(λv) = λf(v) per ogni v ∈V e λ ∈K.
Osservazioni: Notiamo prima che f(0) = f(0 · 0) = 0 · f(0) = 0. Quindi f deve mandare l’origine
di V nell’origine di W. [Attenzione: Qui abbiamo usato 0 in V , 0 in W, e 0 nel campo K.]
Notiamo anche, che se f : V →W è lineare ed un vettore v ∈V è espresso come combinazione
lineare di alcuni vettori di V ,
v = λ1v1 + · · · + λkvk
allora troviamo per la sua immagine
f(v) = f (λ1v1 + · · · + λkvk) = f (λ1v1) + · · · + f (λkvk)
= λ1f (v1) + · · · + λkf (vk) .
Vediamo quindi che f manda una qualsiasi combinazione lineare di vettori v1, . . . , vk in una com-
binazione lineare (con gli stessi coeﬃcienti) delle loro immagini f (v1) , . . . , f (vk).
Vediamo qualche esempio con K = R, V = W = R2.
Esempio 14.2
T : R2 →R2 deﬁnito da T
a
b

=
2a + b
a + 3b

. Per v =
a1
b1

, w =
a2
b2

∈R2, λ ∈R abbiamo
T(v + w) = T
a1
b1

+
a2
b2

= T
a1 + a2
b1 + b2

=
2 (a1 + a2) + (b1 + b2)
(a1 + a2) + 3 (b1 + b2)

=
2a1 + 2a2 + b1 + b2
a1 + a2 + 3b1 + 3b2

=
2a1 + b1
a1 + 3b1

+
2a2 + b2
a2 + 3b2

= T(v) + T(w)
e
T(λv) = T
λa1
λb1

=
2λa1 + λb1
λa1 + 3λb1

= λ
2a1 + b1
a1 + 3b1

= λT(v).
Allora T è lineare.
68

<!-- pagina 69 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 14.3
T : R2 →R2 deﬁnito da T
a
b

=

a + 2
a + b −1

. Abbiamo T(0) =
 2
−1
̸
= 0, allora T non è
lineare.
Esempio 14.4
T : R2 →R2 deﬁnito da T
a
b

=
 a2
a + b

. Sia per esempio v =
2
1

e w =
2
0

.
Abbiamo T(v + w) = T
4
1

=
16
5

, ma T(v) + T(w) =
4
3

+
4
2

=
8
5

.
Allora T non è lineare.
Le due applicazioni lineari del prossimo esempio funzionano con ogni spazio vettoriale.
Esempio 14.5
Dati due spazi vettoriali V, W qualsiasi su K, la funzione nulla è la funzione f : V →W che
è costantemente nulla, cioè tale che f(v) = 0 per ogni v. La funzione nulla è lineare: i due
assiomi di linearità per f sono soddisfatti in modo banale.
Dato uno spazio vettoriale V qualsiasi, la funzione identità è la funzione id : V →V che
manda ogni vettore in se stesso, cioè tale che id(v) = v∀v ∈V . La funzione identità è lineare:
anche qui i due assiomi sono ovviamente soddisfatti.
L’esempio più importante è il seguente.
Esempio 14.6
Prendiamo una matrice A = (aij) di taglia m × n e deﬁniamo
LA : Kn −→Km
usando il prodotto fra matrici e vettori: LA(x) = Ax. Nel dettaglio:
LA(x) = Ax =



a11
· · ·
a1n
...
...
...
am1
· · ·
amn


·



x1
...
xn


=



a11x1 + · · · + a1nxn
...
am1x1 + · · · + amnxn


.
La lettera L sta per "left" perché moltiplichiamo a sinistra per A. La linearità di LA discende
dalle proprietà delle matrici:
(i) LA (x + x′) = A (x + x′) = Ax + Ax′ = LA(x) + LA (x′),
(ii) LA(λx) = A(λx) = λAx = λLA(x).
69

<!-- pagina 70 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 14.7
Se nell’esempio precedente scegliamo esplicitamente la matrice A =
 2
1
1
3

, otteniamo la
funzione LA : R2 →R2 data da:
LA
 a
b

=
 2
1
1
3
  a
b

=
 2a + b
a + 3b

cioè, esattamente l’applicazione lineare dell’Esempio 14.2.
Collegamento con l’informatica: reti neurali
Una delle operazioni fondamentali di una rete neurale è la moltiplicazione matrice–vettore. Un
singolo strato usa tipicamente una trasformazione della forma
x 7−→Ax + b,
dove le entrate di A e di b sono parametri che vengono modiﬁcati durante l’addestramento. La
parte x 7→Ax è precisamente l’applicazione lineare LA studiata sopra; se b̸ = 0, la funzione
x 7→Ax + b non è lineare ma aﬃne. Gli strati di una rete neurale alternano trasformazioni di
questo tipo con operazioni non lineari. Per questo motivo matrici, vettori e applicazioni lineari
costituiscono il linguaggio di base con cui vengono descritti molti modelli di machine learning.
Esempio 14.8
Tr : M(n, K) →K è un’applicazione lineare. Ci ricordiamo che per
A =



a11
· · ·
...
...
ann


,
B =



b11
· · ·
...
...
bnn



abbiamo
A + B =



a11 + b11
· · ·
...
...
ann + bnn


.
Concludiamo allora Tr(A + B) = (a11 + b11) + · · · + (ann + bnn) = Tr(A) + Tr(B),
Analogamente, Tr(λA) = λa11 + · · · + λann = λ · Tr(A).
14.B
Nucleo e immagine
Deﬁnizione 14.9
Sia f : V →W un’applicazione lineare. Il nucleo di f è il sottoinsieme di V deﬁnito nel modo
70

<!-- pagina 71 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
seguente:
Ker f = {v ∈V | f(v) = 0}.
L’immagine di f è un sottoinsieme di W deﬁnito da
Im f = {w ∈W | ∃v ∈V con f(v) = w}.
Proposizione 14.10
Il nucleo Ker f è un sottospazio vettoriale di V , l’immagine Im f è un sottospazio di W.
Dimostrazione. Dobbiamo veriﬁcare i 3 assiomi di sottospazio. Per il nucleo abbiamo
(1) 0 ∈Ker f, perché f(0) = 0.
(2) v, w ∈Ker f ⇒v + w ∈Ker f, infatti f(v + w) = f(v) + f(w) = 0 + 0 = 0.
(3) v ∈Ker f, λ ∈K ⇒λv ∈Ker f, infatti f(λv) = λf(v) = λ0 = 0.
Per l’immagine
(1) 0 ∈Im f, perché f(0) = 0.
(2) f(v), f (v′) ∈Im f ⇒f(v) + f (v′) ∈Im f perché f(v) + f (v′) = f (v + v′).
(3) f(v) ∈Im f, λ ∈K ⇒λf(v) ∈Im f perché λf(v) = f(λv).
Proposizione 14.11
La funzione f : V →W è iniettiva ⇐⇒Ker f = {0}. La funzione f è suriettiva ⇐⇒Im f = W.
Dimostrazione. Dimostriamo la condizione per l’iniettività. La condizione per la suriettività è ovvia.
(⇒) Sappiamo già che f(0) = 0. Siccome f è iniettiva, v̸ = 0 ⇒f(v)̸ = 0. Quindi Ker f = {0}.
(⇐) Siano v, v′ ∈V diversi. Siccome Ker f = {0}, troviamo che v −v′̸ = 0 ⇒f(v) −f (v′) =
f (v −v′)̸ = 0, e quindi f(v)̸ = f (v′).
Collegamento con l’informatica: il nucleo come insieme di direzioni ammissibili
Supponiamo che un vettore x debba soddisfare un vincolo lineare
Ax = b.
Se vogliamo spostarci da x nella direzione y senza cambiare il vincolo, consideriamo x + ty.
Abbiamo
A(x + ty) = b + tAy.
Quindi A(x + ty) = b per ogni t precisamente quando Ay = 0, cioè quando
y ∈Ker A.
Il nucleo descrive dunque tutte le direzioni lungo le quali ci si può muovere mantenendo invariati
i vincoli di uguaglianza.
Questa interpretazione viene usata direttamente negli algoritmi di
ottimizzazione lineare.
71

<!-- pagina 72 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Osservazione: Se v1, . . . , vn sono generatori di V , allora f(v1), . . . , f(vn) sono generatori di Im f.
Infatti, sia w ∈Im f. Esiste allora v ∈V con f(v) = w. Visto che v1, . . . , vn sono generatori di
V , v può essere scritto come combinazione lineare v = λ1v1 + · · · + λnvn per qualche λ1, . . . , λn.
Quindi
w = f(λ1v1 + · · · + λnvn) = λ1f (v1) + · · · + λnf (vn) ∈Span (f (v1) , . . . , f (vn)) .
Siccome questo vale per ogni w, concludiamo che Im f = Span (f (v1) , . . . , f (vn)).
In particolare, se A è una matrice m×n, visto che e1, . . . , en generano Kn e Ai = LA (ei), questo
ci dice che l’immagine dell’applicazione LA : Kn →Km è precisamente lo spazio generato dalle
colonne:
Im LA = Span
 A1, . . . , An
.
Concludiamo che per ogni matrice A vale
rk(A) = dim Span
 A1, . . . , An
= dim Im LA.
14.C
Teorema della dimensione
Teorema 14.12 (Teorema della dimensione)
Sia f : V →W una funzione lineare. Se V ha dimensione ﬁnita n, allora
dim Ker f + dim Im f = n.
Idea della dimostrazione. Si prende una base v1, . . . , vk di Ker f e la si completa a una base
v1, . . . , vn di V . Allora f(vk+1), . . . , f(vn) formano una base di Im f, per cui dim Im f = n −k
e la formula segue.
Nel caso particolare di un’applicazione lineare LA : Kn →Km, abbiamo
Ker LA = {x ∈Kn | LA(x) = 0} = {x ∈Kn | Ax = 0} = S,
lo spazio delle soluzioni del sistema Ax = 0. Con l’osservazione sopra, il teorema della dimensione
diventa dim S = n −rk(A). Questo è semplicemente il teorema di Rouché–Capelli!
Corollario 14.13
Sia f : V →W un’applicazione lineare. Vale
dim Im f ≤dim V.
Inoltre:
(1) f iniettiva ⇐⇒dim Im f = dim V .
(2) f suriettiva ⇐⇒dim Im f = dim W.
Spiegazione. Dal Teorema della dimensione,
dim Im f = dim V −dim Ker f ≤dim V.
Inoltre f è iniettiva se e solo se Ker f = {0}, mentre è suriettiva se e solo se Im f = W.
72

<!-- pagina 73 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
14.D
Esercizi
Esercizio 14.14
Per ogni funzione fk sotto, controllare che fk è lineare, trovare Ker fk e Im fk e veriﬁcare il
teorema della dimensione.
1. f1 : R3 →R2, f1(x, y, z) = (x + y + z, 2x + 3y + 4z),
2. f2 : R2[x] →R, f2(p(x)) = p(1) + p(−1),
3. f3 : M2(R) →M2(R), f3(A) = A −tA.
Esercizio 14.15
Sia f : R4 →R3 l’applicazione lineare deﬁnita da
f(x1, x2, x3, x4) =


x1 + x2 + x3
x2 + x3 + x4
x1 −x4

.
1. Trovare una base di Ker f.
2. Determinare dim Im f usando il teorema della dimensione.
3. Trovare una base di Im f.
4. Stabilire se f è iniettiva e se è suriettiva.
73

<!-- pagina 74 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
15
Applicazioni Lineari II
15.A
Isomorﬁsmi
Deﬁnizione 15.1
Un’applicazione lineare f : V →W è un isomorﬁsmo se è biettiva.
[Ricordiamo che una
funzione f è biettiva se e solo se è contemporaneamente iniettiva e suriettiva.]
Diciamo che due spazi vettoriali V e W sullo stesso campo K sono isomorﬁse esiste un
isomorﬁsmo f : V →W.
Sappiamo che se f : V →W è biettiva, esiste un’inversa f−1 : W →V .
Proposizione 15.2
Se una funzione lineare f : V →W è biettiva, l’inversa f−1 : W →V è anch’essa lineare.
Proposizione 15.3
Sia f : V →W un’applicazione lineare.
(1) Se f è iniettiva, allora dim V ≤dim W. (Infatti dim V = dim Im f ≤dim W.)
(2) Se f è suriettiva, allora dim V ≥dim W. (Infatti dim V ≥dim Im f = dim W.)
(3) Se f è un isomorﬁsmo, allora dim V = dim W. (Dai due punti precedenti.)
Vale anche il vice-versa dell’ultimo punto:
Proposizione 15.4
Siano V e W due spazi vettoriali di dimensione ﬁnita. Allora
V e W sono isomorﬁ⇐⇒dim V = dim W.
In particolare, tutti gli spazi vettoriali su K di dimensione n sono isomorﬁa Kn.
La mappa V →Kn che manda ogni vettore x ∈V alle sue coordinate rispetto ad una base di V
è infatti l’isomorﬁsmo tra V e Kn. (Questo isomorﬁsmo dipende dalla scelta della base.)
15.B
Matrice associata ad un’applicazione lineare
Se ﬁssiamo una base B = {v1, . . . , vn} di uno spazio V , possiamo rappresentare qualsiasi vettore
v ∈V come un vettore colonna in Kn, quello delle sue coordinate. Denotiamo questo vettore
coordinate con [v]B ∈Kn.
Adesso facciamo lo stesso con le applicazioni lineari: ﬁssando opportune basi, possiamo rappre-
sentare qualsiasi applicazione lineare come una matrice.
74

<!-- pagina 75 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Deﬁnizione 15.5
Sia f : V →W un’applicazione lineare fra spazi vettoriali deﬁniti su K. Siano inoltre
B = {v1, . . . , vn} ,
C = {w1, . . . , wm}
due basi rispettivamente di V e di W. Sappiamo che
f (v1) = a11w1 + · · · + am1wm,
...
f (vn) = a1nw1 + · · · + amnwm.
per qualche insieme di coeﬃcienti aij ∈K. Deﬁniamo la matrice associata a f nelle basi B e C
come la matrice m × n
A = (aij)
che raggruppa questi coeﬃcienti, e la indichiamo con il simbolo
A = [f]B
C
La notazione A = [f]B
C ci ricorda che A dipende da f, da B e da C. Notiamo che “la base in
partenza” B sta in alto e “la base in arrivo” C sta in basso. Notiamo anche che la j-esima colonna
di A contiene le coordinate di f (vj) rispetto a C, cioè
Aj =



a1j
...
amj


= [f (vj)]C
Esempio 15.6
La matrice associata a LA rispetto alle basi canoniche di Kn e Km è proprio A. Infatti, per
costruzione f (ej) = a1je1 + · · · + amjem.
Esempio 15.7
Consideriamo l’applicazione lineare
f : R2[x] −→R2,
f(p) =

p(2)
p(−2)

che assegna ad ogni polinomio i suoi valori in 2 e in −2 . Scriviamo la matrice associata a f
nelle basi canoniche B =

1, x, x2	
di R2[x] e C = {e1, e2} di R2. Calcoliamo:
f(1) =
 1
1

,
f(x) =

2
−2

,
f
 x2
=
 4
4

.
75

<!-- pagina 76 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Quindi la matrice associata è
[f]B
C =
 1
2
4
1
−2
4

Esempio 15.8
Prendiamo l’applicazione lineare f e la base B come nell’esempio precedente, ma in arrivo
prendiamo la base
C′ =

1
−1

,
 0
1

invece della base canonica C. Dobbiamo calcolare le coordinate di ciascun vettore immagine
rispetto a C′. Risolvendo dei semplici sistemi lineari troviamo:
f(1) =
 1
1

= 1

1
−1

+ 2
 0
1

,
f(x) =

2
−2

= 2

1
−1

+ 0
 0
1

,
f
 x2
=
 4
4

= 4

1
−1

+ 8
 0
1

e la matrice associata diventa quindi
[f]B
C′ =
 1
2
4
2
0
8

Notiamo che dalla matrice associata possiamo facilmente calcolare l’immagine di qualsiasi vettore.
Sia f : V →W un’applicazione lineare e B = {v1, . . . , vn} e C = {w1, . . . , wm} basi di V e W.
Proposizione 15.9
Per ogni v ∈V troviamo
[f(v)]C = [f]B
C · [v]B.
Dimostrazione. Dato v = λ1v1 + · · · + λnvn, troviamo
f(v) = λ1f (v1) + · · · + λnf (vn)
e quindi
[f(v)]C = λ1 [f (v1)]C + · · · + λn [f (vn)]C = [f]B
C · [v]B
Per trovare le coordinate di f(v) rispetto a C è suﬃciente moltiplicare la matrice associata a f per
le coordinate di v rispetto a B.
76

<!-- pagina 77 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Osservazione: Se scriviamo x = [v]B, A = [f]B
C e y = [f(v)]C, allora
y = Ax = LA(x).
Questo vuol dire che, dopo aver scelto due basi per V e W, qualsiasi applicazione lineare V →W
può essere interpretata in coordinate come un’applicazione del tipo LA : Kn →Km. È suﬃciente
sostituire i vettori v e f(v) con le loro coordinate x e y, ed usare la matrice associata A.
Esempio 15.10
Nell’Esempio 15.8 sopra, abbiamo ottenuto la matrice associata
[f]B
C =
 1
2
4
1
−2
4

rispetto alle basi canoniche. Possiamo usare questa matrice per calcolare in coordinate l’immagine
di p(x) = 3x2 +5x+1 che ha come coordinate rispetto a B i suoi coeﬃcienti (in ordine inverso).
Quindi la sua immagine f(p) ha coordinate
 1
2
4
1
−2
4
 

1
5
3

=
 1 + 10 + 12
1 −10 + 12

=
 23
3

Veriﬁchiamo con la deﬁnizione di f che
f(p) =

p(2)
p(−2)

=
 23
3

.
Un esempio particolare, utile nel futuro è questo:
Proposizione 15.11
Sia B una qualsiasi base di uno spazio V di dimensione n. Troviamo
[id]B
B = In.
In generale, se V, W sono spazi vettoriali e f, g : V →W due applicazioni lineari, possiamo deﬁnire
f + g e λf (con λ ∈K) nel modo seguente:
(f + g)(v) = f(v) + g(v),
(λf)(v) = λf(v).
È facile controllare che con queste due operazioni, l’insieme di tutte le applicazioni lineari tra V e
W diventa uno spazio vettoriale.
77

<!-- pagina 78 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Teorema 15.12
Siano V, W due spazi vettoriali di dimensione ﬁnita con basi A = {v1, . . . , vn}, B = {w1, . . . , wm},
rispettivamente. Allora l’insieme delle applicazioni lineari f : V →W è uno spazio vettoriale, e
la mappa
f 7−→[f]A
B
dall’insieme delle applicazioni lineari f : V →W a M(m, n, K) è un isomorﬁsmo.
15.C
Esercizi
Esercizio 15.13
Consideriamo l’applicazione lineare
f : C2 −→C3,
f
 x
y

=


x −y
2x
y

.
Trovare la matrice associata a f rispetto alle basi
v1 =
 1
1

,
v2 =

1
−1

in partenza e
w1 =


1
1
0

,
w2 =


0
1
1

,
w3 =


1
0
1


in arrivo.
[Soluzione.
[f]A
B =


1/2
5/2
3/2
−1/2
−1/2
−1/2

= 1
2


1
5
3
−1
−1
−1

.]
78

<!-- pagina 79 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
16
Applicazioni Lineari III
16.A
Matrice di cambiamento di base
Deﬁnizione 16.1
Sia V uno spazio vettoriale e B = {v1, . . . , vn} e C = {w1, . . . , wn} due basi di V . La matrice
di cambiamento di base da B a C è la matrice
A = [id]B
C .
La colonna j-esima di A contiene le coordinate di vj rispetto a C:
Aj = [vj]C.
L’inversa
A−1 = [id]C
B
è la matrice di cambiamento di base da C a B.
Dalla Proposizione 15.10 ricaviamo:
Proposizione 16.2
Per ogni v ∈V vale
[v]C = A · [v]B.
Esercizio 16.3
Siano A = {e1, e2, e3} la base canonica di R3 e sia B = {w1, w2, w3} deﬁnita da
w1 =


1
2
3

,
w2 =


0
2
1

,
w3 =


0
1
1

.
Vogliamo trovare la matrice di cambiamento di base
A = [id]A
B.
Soluzione 1: Per costruzione A = (aij) dove gli aij sono soluzioni del sistema



e1 = a11w1 + a21w2 + a31w3
e2 = a12w1 + a22w2 + a32w3
e3 = a13w1 + a23w2 + a33w3.
Ad esempio, la prima equazione diventa


1
0
0

= a11


1
2
3

+ a21


0
2
1

+ a31


0
1
1

,
79

<!-- pagina 80 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
cioè



a11 = 1
2a11 + 2a21 + a31 = 0
3a11 + a21 + a31 = 0
=⇒



a11 = 1
a21 = 1
a31 = −4.
In modo simile si risolvono gli altri sistemi arrivando alla soluzione
A =


1
0
0
1
1
−1
−4
−1
2

.
Soluzione 2: Un modo alternativo di risolvere il problema è calcolare A−1. La j-esima colonna di
A−1 è il vettore [wj]A. Poiché A è la base canonica,
[wj]A = wj,
e quindi
A−1 =


1
0
0
2
2
1
3
1
1

.
Pertanto
A =


1
0
0
2
2
1
3
1
1


−1
=


1
0
0
1
1
−1
−4
−1
2

.
16.B
Composizione di applicazioni lineari
Oltre alle operazioni di somma e prodotto per scalare, possiamo comporre applicazioni lineari.
Proposizione 16.4
Se f : V →W e g : W →Z sono funzioni lineari, anche la composizione
g ◦f : V →Z
lo è.
Per le applicazioni di tipo LA la composizione corrisponde precisamente al prodotto fra matrici:
Proposizione 16.5
Siano A ∈M(k, m, K) e B ∈M(m, n, K). Consideriamo
LA : Km →Kk,
LB : Kn →Km.
Vale la relazione
LA ◦LB = LAB.
Spiegazione. Per ogni x ∈Kn,
LA(LB(x)) = A(Bx) = (AB)x = LAB(x),
per l’associatività del prodotto fra matrici.
80

<!-- pagina 81 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Proposizione 16.6
Siano f : U →V e g : V →W due applicazioni lineari. Siano B, C e D basi di U, V e W.
Troviamo
[g ◦f]B
D = [g]C
D[f]B
C .
Dimostrazione. Sia B = {v1, . . . , vn}. La colonna i-esima di [g ◦f]B
D è
[g (f (vi))]D = [g]C
D [f (vi)]C .
D’altra parte [f (vi)]C è la colonna i-esima di [f]B
C , e quindi concludiamo.
Corollario 16.7
La funzione f è un isomorﬁsmo se e solo se la matrice associata [f]B
C è invertibile, ed in questo
caso la sua inversa è

f−1C
B .
Dimostrazione. Se f è un isomorﬁsmo, allora
[f−1]C
B[f]B
C = In
e
[f]B
C [f−1]C
B = In,
quindi [f−1]C
B è l’inversa di [f]B
C . Viceversa, se A = [f]B
C è invertibile, per il teorema della Lezione
15 sulle matrici associate esiste un’applicazione lineare g : W →V tale che
[g]C
B = A−1.
Dalla formula per la matrice di una composizione segue che g = f−1.
Corollario 16.8
Sia f : V →W un’applicazione lineare. Siano B1, B2 due basi di V e C1, C2 due basi di W.
Applicando la Proposizione 16.6 troviamo
[f]B2
C2 = [idW ]C1
C2 · [f]B1
C1 · [idV ]B2
B1.
Questo corollario ci dice che per passare da [f]B1
C1 a [f]B2
C2 è suﬃciente moltiplicare a sinistra e a
destra per le matrici di cambiamento di base.
16.C
Endomorﬁsmi e similitudine fra matrici
Deﬁnizione 16.9
Sia V uno spazio vettoriale. Un endomorﬁsmo è un’applicazione lineare
f : V →V.
81

<!-- pagina 82 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Se ﬁssiamo una base B per V , ogni endomorﬁsmo f è rappresentato da una matrice
[f]B
B,
e la composizione corrisponde al prodotto:
[f ◦g]B
B = [f]B
B[g]B
B.
Se B e C sono due basi di V e
M = [id]B
C ,
allora
[f]B
B = M−1[f]C
CM.
Quindi le matrici che rappresentano lo stesso endomorﬁsmo rispetto a basi diverse sono legate da
una relazione del tipo
A = M−1BM.
Esempio 16.10
Consideriamo f : R2 →R2 dato da
f
 x
y

=
 x + y
−y

.
Rispetto alla base canonica
C = {e1, e2} ,
troviamo
[f]C
C =
 1
1
0
−1

.
Prendiamo adesso come base
B =
 1
0

,
 −1
2

.
La matrice di cambiamento di base da B a C è
M = [id]B
C =
 1
−1
0
2

,
e la sua inversa è
M−1 = [id]C
B =
 1
1/2
0
1/2

.
Quindi la matrice associata a f nella base B è
B
B = M−1[f]C
CM
=
 1
1/2
0
1/2
  1
1
0
−1
  1
−1
0
2

=
 1
0
0
−1

.
82

<!-- pagina 83 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Possiamo veriﬁcare direttamente il risultato: il primo vettore della base B viene mandato in se
stesso, mentre il secondo viene mandato nel suo opposto:
f
 1
0

=
 1
0

,
f
 −1
2

=

1
−2

.
Deﬁnizione 16.11
Sia M(n) l’insieme delle matrici quadrate n × n. Diciamo che due matrici A, B ∈M(n) sono
simili (o coniugate) se esiste una matrice invertibile M ∈M(n) tale che
A = M−1BM.
Se A e B sono simili scriviamo A ∼B.
L’interpretazione è che matrici simili descrivano lo stesso endomorﬁsmo ma in basi diverse.
Proposizione 16.12
La similitudine è una relazione di equivalenza in M(n).
L’insieme M(n) delle matrici quadrate è quindi partizionato in sottoinsiemi disgiunti formati da
matrici simili fra loro.
Proposizione 16.13
Se A ∼B allora
rk(A) = rk(B),
det(A) = det(B).
In particolare
A è invertibile ⇐⇒B è invertibile.
Spiegazione. Se A = M−1BM, il Teorema di Binet dà det A = det B. Inoltre la moltiplicazione
a sinistra o a destra per una matrice invertibile non cambia il rango, quindi rk(A) = rk(B).
16.D
Esercizi
Esercizio 16.14
Consideriamo l’endomorﬁsmo f : R2 →R2 deﬁnito da
f
 x
y

=
 2x + y
x + 2y

.
Siano
C = {e1, e2}
la base canonica e
B =
 1
1

,

1
−1

.
83

<!-- pagina 84 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
(1) Trovare la matrice
A = [f]C
C.
(2) Trovare la matrice di cambiamento di base
M = [id]B
C .
(3) Calcolare
[f]B
B
usando la formula di cambiamento di base.
(4) Veriﬁcare il risultato calcolando direttamente f(v1) e f(v2), dove B = {v1, v2}.
84

<!-- pagina 85 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
17
Autovalori e Autovettori I
17.A
Deﬁnizione ed esempi
Deﬁnizione 17.1
Sia T : V →V un endomorﬁsmo di uno spazio vettoriale V deﬁnito su un campo K. Un
autovettore di T è un vettore v̸ = 0 in V per cui
T(v) = λv
per qualche scalare λ ∈K che chiameremo autovalore di T relativo a v.
Notiamo che λ
può essere qualsiasi scalare, anche zero. D’altro canto, l’autovettore v non può essere zero per
deﬁnizione. In parole semplici, un autovettore è un vettore (diverso da zero) che viene mandato
da T in un multiplo di se stesso.
Esempio 17.2
Consideriamo l’endomorﬁsmo LA : R2 →R2 con
A =
 3
4
0
2

Poiché LA (e1) = 3e1, il vettore e1 è autovettore di LA con autovalore 3. Invece LA (e2) =
 4
2
̸
= λe2 per qualsiasi λ, allora e2 non è un autovettore.
Notiamo che LA
 −4
1

=
 −8
2

= 2
 −4
1

e quindi il vettore
 −4
1

è autovettore
con autovalore 2.
Osservazione. Come molte altre cose viste qui, autovettori e autovalori possono essere agevol-
mente studiati in coordinate rispetto ad una base. Sia T : V →V un endomorﬁsmo di uno spazio
vettoriale V . Siano B una base di V e A = [T]B
B la matrice associata. Sia v ∈V un vettore e
x = [v]B ∈Kn il vettore delle sue coordinate. Con la teoria delle ultime lezioni troviamo
T(v) = λv
⇐⇒
Ax = λx.
Allora l’equazione T(v) = λv corrisponde in coordinate a Ax = λx. Dobbiamo allora solo capire
bene il caso in cui l’endomorﬁsmo f è dato da LA.
Esempio 17.3
Sia LA : R2 →R2 con A = Rotϑ una rotazione di angolo ϑ̸ = 0, π. Ciascun vettore v ∈R2
diverso da zero viene ruotato di un angolo ϑ̸ = 0, π e quindi chiaramente la sua immagine LA(v)
non può essere un multiplo di v. L’endomorﬁsmo LA non ha autovettori.
85

<!-- pagina 86 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 17.4
Consideriamo l’endomorﬁsmo LA : R3 →R3 con
A =


1
1
−1
2
1
1
3
0
2


Notiamo che LA(e1) =


1
2
3

, allora e1 non è un autovettore. Invece per v =


0
1
1

troviamo
LA(v) = 2v, allora v è un autovettore con autovalore 2. Analogamente, per w =


0
3
3


troviamo LA(w) = 2w, allora anche w è un autovettore con autovalore 2. Notiamo che w = 3v.
Osservazione Sia f : V →V un endomorﬁsmo. Se v ∈V è autovettore per f con autovalore λ,
allora qualsiasi multiplo w = µv di v con µ̸ = 0 è anch’esso autovettore con lo stesso autovalore
λ, infatti
f(µv) = µf(v) = µλv = λ(µv).
Se v ∈V è autovettore, tutti i vettori non nulli nella retta Span(v) sono anche loro autovettori
con lo stesso autovalore λ.
17.B
Endomorﬁsmi e matrici diagonalizzabili.
Veniamo adesso al vero motivo per cui abbiamo introdotto autovettori e autovalori.
Deﬁnizione 17.5
Un endomorﬁsmo T : V →V è diagonalizzabile se V ha una base B = {v1, . . . , vn} composta
da autovettori per T.
Il termine "diagonalizzabile" è dovuto al fatto seguente, che è cruciale.
Proposizione 17.6
Sia B = {v1, . . . , vn} una base qualsiasi di V . La matrice associata A = [T]B
B è diagonale se e
solo se i vettori v1, . . . , vn sono tutti autovettori per T.
Infatti, il vettore vi è un autovettore ⇐⇒T (vi) = λivi per qualche λi ∈K se e solo se [T (vi)]B =
λiei. Questo capita per ogni i = 1, . . . , n se e solo se A è diagonale, con gli autovalori sulla
diagonale principale:
A =





λ1
0
· · ·
0
0
λ2
· · ·
0
...
...
...
...
0
0
· · ·
λn




.
86

<!-- pagina 87 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Abbiamo scoperto che un endomorﬁsmo T è diagonalizzabile se e solo se esiste una base B tale
che A = [T]B
B sia una matrice diagonale. Questo accade precisamente quando B è una base di
autovettori, e gli elementi sulla diagonale principale di A sono precisamente i loro autovalori. In
coordinate troviamo:
Deﬁnizione 17.7
Una matrice A ∈M(n, K) è diagonalizzabile se è simile ad una matrice diagonale D. Quindi
A è diagonalizzabile ⇐⇒esiste una matrice invertibile M tale che
D = M−1AM
è diagonale.
Il collegamento con la nozione di endomorﬁsmo diagonalizzabile è chiaramente molto forte:
Proposizione 17.8
Sia B una base di V . Un endomorﬁsmo T : V →V è diagonalizzabile ⇐⇒la matrice associata
A = [T]B
B è diagonalizzabile.
Dimostrazione. Se T è diagonalizzabile, esiste una base C di V per cui D = [T]C
C è diagonale; se
M = [id]C
B è la matrice di cambiamento di base da C a B otteniamo D = M−1AM.
D’altro canto, se D = M−1AM è diagonale per qualche M invertibile, sia C la base di V formata
da vettori le cui coordinate rispetto a B sono le colonne di M. Allora chiaramente M = [id]C
B e
quindi [T]C
C = M−1AM = D.
Esempio 17.9
L’endomorﬁsmo LA : R2 →R2 con A =
 3
4
0
2

già considerato nell’Esempio 17.2 è diago-
nalizzabile, perché come abbiamo notato precedentemente v1 =
 1
0

e v2 =
 −4
1

sono
entrambi autovettori e sono linearmente indipendenti, quindi formano una base. I loro autovalori
sono 3 e 2 . Prendendo B = {v1, v2} otteniamo quindi
[LA]B
B =
 3
0
0
2

Esempio 17.10
La rotazione di angolo ϑ considerata nell’Esempio 17.3 non è diagonalizzabile per ϑ̸ = 0, π
perché non ha autovettori. Per ϑ = 0 e ϑ = π la rotazione diventa rispettivamente f(v) = v e
f(v) = −v e quindi è diagonalizzabile (ogni vettore non nullo è autovettore in questi due casi).
87

<!-- pagina 88 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
17.C
Matrici diagonali
Perché preferiamo le matrici diagonali? Le preferiamo perché sono molto più maneggevoli. Notiamo
innanzitutto che il prodotto Ax tra una matrice diagonale A ed un vettore x è





λ1
0
. . .
0
0
λ2
. . .
0
...
...
...
...
0
0
. . .
λn










x1
x2
...
xn




=





λ1x1
λ2x2
...
λnxn




.
Inoltre il determinante di una matrice diagonale A è semplicemente il prodotto degli elementi sulla
diagonale principale: det A = λ1 · · · λn. Anche il prodotto fra matrici diagonali è molto semplice:





λ1
0
. . .
0
0
λ2
. . .
0
...
...
...
...
0
0
. . .
λn










µ1
0
. . .
0
0
µ2
. . .
0
...
...
...
...
0
0
. . .
µn




=





λ1µ1
0
. . .
0
0
λ2µ2
. . .
0
...
...
...
...
0
0
. . .
λnµn




.
In particolare, possiamo calcolare facilmente potenze come A100 :
A =





λ1
0
. . .
0
0
λ2
. . .
0
...
...
...
...
0
0
. . .
λn




=⇒Ak =





λk
1
0
. . .
0
0
λk
2
. . .
0
...
...
...
...
0
0
. . .
λk
n




.
Esempio 17.11
Prendiamo A =
 3
4
0
2

e calcoliamo A100. La matrice A non è diagonale, quindi calcolare una
potenza di A direttamente è estremamente dispendioso. Sappiamo però che A è diagonalizzabile:
dalla discussione svolta nell’Esempio 17.9 deduciamo che M−1AM = D =
 3
0
0
2

, dove
M = [id]B
C =
 1
−4
0
1

=⇒
M−1 = [id]C
B =
 1
4
0
1

Qui B =
 1
0

,
 −4
1

e C è la base canonica di R2. Quindi
A100 =
 MDM−1100 = MD100M−1
=
 1
−4
0
1
  3100
0
0
2100
  1
4
0
1

=
 1
−4
0
1
  3100
4 · 3100
0
2100

=
 3100
4 · (3100 −2100)
0
2100

88

<!-- pagina 89 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
17.D
Polinomio caratteristico
Come possiamo trovare autovalori & autovettori? Ci aiuta il concetto del polinomio caratteristico:
Deﬁnizione 17.12
Sia A ∈M(n, K). Il polinomio caratteristico di A = (aij) è deﬁnito nel modo seguente:
pA(λ) = det (A −λIn) = det





a11 −λ
a12
. . .
a1n
a21
a22 −λ
. . .
a2n
...
...
...
...
an1
an2
. . .
ann −λ





Osservazione. Questo è veramente un polinomio di grado n.
Osservazione. Se A e B sono matrici simili, allora pA(λ) = pB(λ). Infatti, se A = M−1BM per
qualche matrice invertibile M, usiamo λIn = λM−1M = M−1 (λIn) M per ottenere
pA(λ) = det (A −λIn) = det
 M−1BM −M−1λInM

= det
 M−1 (B −λIn) M

= det
 M−1
det (B −λIn) det(M)
= det (B −λIn) = pB(λ)
grazie al Teorema di Binet. Per un endomorﬁsmo T : V →V di uno spazio vettoriale V deﬁni-
amo allora il polinomio caratteristico pT (λ) come il polinomio caratteristico pA(λ) della matrice
associata A = [T]B
B rispetto ad una qualsiasi base B di V . La deﬁnizione non dipende dalla base
scelta perché il polinomio caratteristico è invariante per similitudine.
Proposizione 17.13
Gli autovalori di T sono precisamente le radici del polinomio caratteristico pT (λ).
Dimostrazione. Scegliamo una base B e scriviamo A = [T]B
B. Uno scalare λ ∈K è autovalore per
T se e solo se esiste un x ∈Kn non nullo tale che Ax = λx. I fatti seguenti sono tutti equivalenti:
∃x̸ = 0 tale che Ax = λx ⇐⇒∃x̸ = 0 tale che (A −λIn) x = 0
⇐⇒∃x̸ = 0 tale che x ∈ker (A −λIn) ⇐⇒A −λIn non è invertibile
⇐⇒det (A −λIn) = 0 ⇐⇒pA(λ) = 0.
Esempio 17.14
Prendiamo A =
 3
4
0
2

. Troviamo
pA(λ) = det (A −λIn) = det
 3 −λ
4
0
2 −λ

= (3 −λ)(2 −λ).
Le radici di questo polinomio sono esattamente λ = 2 e λ = 3.
89

<!-- pagina 90 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
18
Autovalori e Autovettori II
18.A
Autovettori con autovalori distinti
Abbiamo visto che un endomorﬁsmo T : V →V è diagonalizzabile se V ha una base B =
{v1, . . . , vn} composta da autovettori per T. Se vogliamo trovare una tale base, è utile notare
questo risultato:
Proposizione 18.1
Se v1, . . . , vk ∈V sono autovettori per T con autovalori λ1, . . . , λk distinti, allora sono linear-
mente indipendenti.
Dimostrazione. Procediamo per induzione su k. Se k = 1, il vettore v1 è indipendente semplice-
mente perché non è nullo (per deﬁnizione, un autovettore non è mai nullo).
Diamo per buono il caso k −1 e mostriamo il caso k. Supponiamo di avere una combinazione
lineare nulla
α1v1 + . . . + αkvk = 0.
Dobbiamo dimostrare che αi = 0 per ogni i. Applicando T otteniamo
α1T (v1) + . . . + αkT (vk) = α1λ1v1 + . . . + αkλkvk = T(0) = 0.
Moltiplicando la prima equazione per λk troviamo
α1λkv1 + . . . αkλkvk = 0
e prendendo la diﬀerenza tra queste due equazioni deduciamo che
α1 (λ1 −λk) v1 + . . . + αk−1 (λk−1 −λk) vk−1 = 0.
Questa è una combinazione lineare nulla di k −1 autovettori con autovalori distinti: per l’ipotesi
induttiva tutti i coeﬃcienti αi (λi −λk) devono essere nulli. Poiché λi̸ = λk, ne deduciamo che
αi = 0 per ogni i = 1, . . . , k −1 e con la prima equazione anche αk = 0.
Corollario 18.2
Se il polinomio caratteristico pT (λ) ha n radici distinte in K, l’endomorﬁsmo T è diagonalizzabile.
18.B
Autospazio
Deﬁnizione 18.3
Sia T : V →V un endomorﬁsmo. Per ogni autovalore λ di T deﬁniamo l’autospazio
Vλ = {v ∈V | T(v) = λv} = ker(T −λ id)
come l’insieme di tutti gli autovettori v con autovalore λ, più l’origine 0 ∈V (ricordiamo che
0 ∈V non è autovettore per deﬁnizione).
90

<!-- pagina 91 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Visto che per ogni endomorﬁsmo S : V →V , l’insieme ker(S) è un sottospazio di V , allora
l’autospazio Vλ è un sottospazio di V .
Deﬁnizione 18.4
Siano V1, . . . , Vk sottospazi di uno spazio vettoriale V . Diciamo che la loro somma è diretta se
ogni vettore
v ∈V1 + · · · + Vk
si può scrivere in modo unico nella forma
v = v1 + · · · + vk,
vi ∈Vi.
In questo caso scriviamo
V1 ⊕· · · ⊕Vk.
Equivalentemente, l’unica relazione v1+· · ·+vk = 0 con vi ∈Vi è quella in cui v1 = · · · = vk = 0.
Proposizione 18.5
Sia T : V →V un endomorﬁsmo e siano λ1, . . . , λk i suoi autovalori. I corrispettivi autospazi
sono sempre in somma diretta:
Vλ1 ⊕· · · ⊕Vλk
Spiegazione. Se un vettore non nullo appartenesse a uno degli autospazi e contemporaneamente
alla somma degli altri, otterremmo una relazione di dipendenza lineare fra autovettori con autoval-
ori distinti, in contraddizione con la Proposizione 18.1.
Corollario 18.6
L’endomorﬁsmo T è diagonalizzabile se e solo se
V = Vλ1 ⊕· · · ⊕Vλk.
Dimostrazione. Sappiamo già che gli autospazi sono in somma diretta, quindi dobbiamo mostrare
che V = Vλ1 + · · · + Vλk ⇐⇒esiste una base di autovettori per T.
(⇒) Unendo le basi degli Vλi otteniamo una base di autovettori per T.
(⇐) Ciascun vettore v è combinazione lineare di autovettori e quindi v ∈Vλ1 + · · · + Vλk.
18.C
Molteplicità algebrica e geometrica
Deﬁnizione 18.7
Sia T : V →V un endomorﬁsmo e sia λ un autovalore per T. La molteplicità algebrica ma(λ)
è la molteplicità di λ come radice del polinomio caratteristico pT . La molteplicità geometrica
mg(λ) è la dimensione dell’autospazio associato a λ, cioè
mg(λ) = dim Vλ.
91

<!-- pagina 92 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 18.8
Sia LA : R2 →R2 l’endomorﬁsmo dato da
A =
 1
1
0
1

Il polinomio caratteristico è pA(λ) = λ2 −2λ + 1 = (λ −1)2. Troviamo un solo autovalore
λ1 = 1, con molteplicità algebrica ma(1) = 2. D’altra parte,
mg(1) = dim V1 = dim ker (A −I2) = 2 −rk (A −I2) = 2 −rk
 0
1
0
0

= 2 −1 = 1.
Abbiamo quindi trovato in questo caso
ma(1) = 2,
mg(1) = 1.
L’esempio ci mostra che le due molteplicità possono essere diverse. In generale, la molteplicità
geometrica è un numero che sta sempre tra 1 e la molteplicità algebrica:
Teorema 18.9
Sia T : V →V un endomorﬁsmo. Per ogni autovalore λ0 di T valgono le disuguaglianze
1 ≤mg (λ0) ≤ma (λ0) .
Idea della dimostrazione. La prima disuguaglianza segue dall’esistenza di un autovettore non nullo.
Per la seconda, scegliamo una base di Vλ0 e completiamola a una base di V : nella matrice di T
compare allora un blocco diagonale λ0Img(λ0), quindi pT (λ) contiene il fattore (λ0 −λ)mg(λ0) e
mg(λ0) ≤ma(λ0).
18.D
Teorema di diagonalizzabilità.
Possiamo ﬁnalmente enunciare il teorema principale. Sia V uno spazio vettoriale di dimensione n
su K.
Teorema 18.10 (Teorema di diagonalizzabilità)
Un endomorﬁsmo T : V →V è diagonalizzabile se e solo se valgono entrambi i fatti seguenti:
(1) pT (λ) ha n radici in K, contate con molteplicità.
(2) ma(λ) = mg(λ) per ogni autovalore λ di T.
Dimostrazione. Sappiamo che gli autospazi sono in somma diretta e deﬁniamo il sottospazio W ⊂
V come la loro somma
W = Vλ1 ⊕· · · ⊕Vλk.
92

<!-- pagina 93 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Sappiamo che T è diagonalizzabile ⇐⇒W = V ⇐⇒dim W = n. Inoltre
dim W = dim Vλ1 + · · · + dim Vλk = mg (λ1) + · · · + mg (λk)
≤ma (λ1) + · · · + ma (λk) ≤n.
Nella prima disuguaglianza abbiamo usato che mg (λi) ≤ma (λi) e nella seconda che λ1, . . . , λk
sono radici del polinomio caratteristico, che ha grado n e quindi ha al più n radici contate con
molteplicità.
Chiaramente dim W = n se e solo se entrambe le disuguaglianze sono uguaglianze. La prima
disuguaglianza è un’uguaglianza precisamente quando mg (λi) = ma (λi) per ogni i, e la seconda
precisamente quando pT (λ) ha n radici in K, contate con molteplicità.
Esempio 18.11
Studiamo la diagonalizzabilità su R della matrice
A =


3
0
0
−4
−1
−8
0
0
3


Si vede facilmente che il polinomio caratteristico è
pA(λ) = (3 −λ)(−1 −λ)(3 −λ),
quindi ha radici λ1 = 3 con ma (λ1) = 2 e λ2 = −1 con ma (λ2) = 1. Tutte le radici di pA(λ)
sono reali, quindi A è diagonalizzabile se e solo se le molteplicità algebriche e geometriche di
ciascun autovalore coincidono. Per il secondo autovalore λ2 è facile: Teorema 18.9 implica che
mg (λ2) = ma (λ2) = 1 e quindi siamo a posto.
Dobbiamo concentrarci solo sull’autovalore λ1 che ha ma (λ1) = 2. Teorema 18.9 ci dice che
mg (λ1) può essere 1 oppure 2: nel primo caso A non è diagonalizzabile, nel secondo sì. Facciamo
i conti e troviamo
mg(3) = dim V3 = dim ker(A −3I3) = 3 −rk(A −3I3).
Nell’ultima uguaglianza abbiamo usato il teorema della dimensione (o Rouché-Capelli). Quindi
mg(3) = 3 −rk(A −3I3) = 3 −rk


0
0
0
−4
−4
−8
0
0
0

= 3 −1 = 2.
Abbiamo scoperto che ma (λ1) = mg (λ1) = 2 e quindi A è diagonalizzabile.
93

<!-- pagina 94 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 18.12
Studiamo la diagonalizzabilità su R della matrice
A =


3
k + 4
1
−1
−3
−1
0
0
2


al variare del parametro k ∈R. Si vede facilmente che il polinomio caratteristico è
pA(λ) = (2 −λ)
 λ2 + k −5

Se k > 5, il fattore λ2 + k −5 non ha radici reali: quindi pA(λ) ha una radice sola e A non è
diagonalizzabile.
Se k ≤5, il polinomio ha tre radici reali
λ1 = 2,
λ2 =
√
5 −k,
λ3 = −
√
5 −k.
Se le tre radici sono distinte, la matrice A è diagonalizzabile. Restano da considerare i casi in
cui le tre radici non sono distinte, cioè i casi k = 1 e k = 5. Questi due casi vanno analizzati
separatamente con le tecniche mostrate nell’esempio precedente.
Se k = 1, gli autovalori sono λ1 = 2, λ2 = 2 e λ3 = −2 e la matrice A è
A =


3
5
1
−1
−3
−1
0
0
2


Calcoliamo la molteplicità geometrica dell’autovalore 2:
mg(2) = 3 −rk


1
5
1
−1
−5
−1
0
0
0

= 3 −1 = 2.
Otteniamo mg(2) = 2 = ma(2) e quindi A è diagonalizzabile.
Se k = 5, gli autovalori sono λ1 = 2, λ2 = 0 e λ3 = 0 e la matrice A è
A =


3
9
1
−1
−3
−1
0
0
2


94

<!-- pagina 95 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
La molteplicità geometrica dell’autovalore 0 è mg(0) = 3 −rk(A) = 3 −2 = 1̸ = 2 = ma(0).
Quindi A non è diagonalizzabile.
Riassumendo, la matrice A è diagonalizzabile se e solo se k < 5.
18.E
Esercizi
Esercizio 18.13
Consideriamo la matrice
A =


2
1
1
0
3
0
0
0
3

.
(1) Calcolare il polinomio caratteristico di A e determinare gli autovalori.
(2) Trovare gli autospazi corrispondenti.
(3) Calcolare la molteplicità algebrica e geometrica di ogni autovalore.
(4) Stabilire se A è diagonalizzabile.
(5) In caso aﬀermativo, trovare una base di R3 formata da autovettori.
Esercizio 18.14
Consideriamo le due matrici
A =
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
2

,
B =


1
1
0
0
1
0
0
0
2

.
(1) Veriﬁcare che A e B hanno lo stesso polinomio caratteristico.
(2) Calcolare la molteplicità geometrica dell’autovalore 1 per entrambe le matrici.
(3) Stabilire quale delle due matrici è diagonalizzabile.
95

<!-- pagina 96 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
19
Prodotti Scalari I
In questo capitolo – a diﬀerenza dei precedenti – supporremo sempre che il campo sia K = R.
Useremo infatti sia l’ordine sui numeri reali sia la possibilità di estrarre la radice quadrata di un
numero positivo.
19.A
Deﬁnizioni
Deﬁnizione 19.1
Sia V uno spazio vettoriale reale. Un prodotto scalare su V è un’applicazione
V × V −→R
(v, w) 7−→⟨v, w⟩
che soddisfa i seguenti assiomi:
(1) ⟨v + v′, w⟩= ⟨v, w⟩+ ⟨v′, w⟩,
(2) ⟨λv, w⟩= λ⟨v, w⟩,
(3) ⟨v, w⟩= ⟨w, v⟩,
per ogni v, v′, w, w′ ∈V e ogni λ ∈R.
Da (1),(2),(3) segue anche
(4) ⟨v, w + w′⟩= ⟨v, w⟩+ ⟨v, w′⟩,
(5) ⟨v, λw⟩= λ⟨v, w⟩.
Gli assiomi (1),(2),(4),(5) dicono che il prodotto è bilineare, mentre l’assioma (3) dice che è
simmetrico. Notiamo inoltre che ⟨v, 0⟩= 0 per ogni v ∈V , infatti
⟨v, 0⟩= ⟨v, 0 + 0⟩= ⟨v, 0⟩+ ⟨v, 0⟩.
Quando vogliamo dare un nome al prodotto scalare, lo indichiamo con una lettera g : V × V →R
e scriviamo g(v, w) invece di ⟨v, w⟩.
Deﬁnizione 19.2
Un prodotto scalare su V è:
- degenere se esiste v̸ = 0 tale che ⟨v, w⟩= 0 per ogni w ∈V ;
- deﬁnito positivo se ⟨v, v⟩> 0 per ogni v ∈V non nullo.
Proposizione 19.3
Un prodotto scalare deﬁnito positivo non è degenere.
Spiegazione. Se fosse degenere, esisterebbe v̸ = 0 tale che ⟨v, w⟩= 0 per ogni w; prendendo
w = v avremmo ⟨v, v⟩= 0, contro la deﬁnita positività.
96

<!-- pagina 97 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 19.4
Consideriamo sullo spazio R2[x] dei polinomi a coeﬃcienti reali di grado ≤2 il prodotto scalare
⟨p, q⟩= p(0)q(0) + p(1)q(1) + p(2)q(2).
Questo prodotto scalare è deﬁnito positivo, infatti
⟨p, p⟩= p(0)2 + p(1)2 + p(2)2 > 0
per ogni polinomio non nullo p di grado ≤2, perché un tale polinomio non può annullarsi nei
tre valori distinti 0, 1, 2.
Il prodotto scalare
⟨p, q⟩= p(0)q(0) + p(1)q(1)
è invece degenere: per p(x) = x(1 −x) otteniamo ⟨p, q⟩= 0 per ogni q ∈R2[x].
Inﬁne,
⟨p, q⟩= p(0)q(0) + p(1)q(1) −p(2)q(2)
non è degenere, ma non è deﬁnito positivo: per p(x) = x −1 otteniamo
⟨p, p⟩= (−1)2 −12 = 0.
Deﬁnizione 19.5
Il prodotto scalare euclideo su Rn è deﬁnito come
⟨x, y⟩= tx y =
n
X
i=1
xiyi.
Ad esempio, in R2,
 1
3

,
 −2
1

= 1 · (−2) + 3 · 1 = 1.
Proposizione 19.6
Il prodotto scalare euclideo è un prodotto scalare deﬁnito positivo su Rn.
19.B
Matrici simmetriche
Abbiamo visto che una matrice quadrata determina un endomorﬁsmo di Rn. Analogamente, una
matrice simmetrica S ∈M(n, R) determina un prodotto scalare su Rn. Ricordiamo che
tS = S,
t(AB) = tB tA.
97

<!-- pagina 98 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Proposizione 19.7
Una matrice simmetrica S deﬁnisce un prodotto scalare gS su Rn ponendo
gS(x, y) = tx S y.
Dimostrazione. La bilinearità segue immediatamente dalle proprietà del prodotto fra matrici. In-
oltre
gS(x, y) = txSy = t txSy

= ty tSx = tySx = gS(y, x),
perché S è simmetrica.
Proposizione 19.8
Vale
gS(x, y) = txSy =
n
X
i,j=1
xiSijyj.
Infatti,
txSy =
n
X
i=1
xi(Sy)i =
n
X
i,j=1
xiSijyj.
Corollario 19.9
Per i vettori della base canonica vale
gS(ei, ej) = Sij.
Esempio 19.10
Per S = In otteniamo il prodotto scalare euclideo:
gIn(x, y) = txy = x1y1 + · · · + xnyn.
Esempio 19.11
La matrice
S =
 2
1
1
1

deﬁnisce su R2 il prodotto scalare
gS(x, y) = 2x1y1 + x1y2 + x2y1 + x2y2.
19.C
Matrice associata
Come per le applicazioni lineari, possiamo rappresentare un prodotto scalare mediante una matrice
dopo aver ﬁssato una base.
98

<!-- pagina 99 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Deﬁnizione 19.12
Sia V uno spazio vettoriale reale, sia
g : V × V −→R
un prodotto scalare e sia B = {v1, . . . , vn} una base di V . La matrice associata a g nella base
B è la matrice simmetrica
S = [g]B,
Sij = g(vi, vj).
Esempio 19.13
Se S ∈M(n, R) è simmetrica, la matrice associata a gS rispetto alla base canonica C è S stessa:
[gS]C = S.
Esempio 19.14
Consideriamo il prodotto scalare euclideo su R2 e la base
B =

v1 =
 1
0

, v2 =
 1
1

.
La matrice associata è
[g]B =
 g(v1, v1)
g(v1, v2)
g(v2, v1)
g(v2, v2)

=
 1
1
1
2

.
Proposizione 19.15
Se
v = λ1v1 + · · · + λnvn,
w = µ1v1 + · · · + µnvn,
allora
g(v, w) =
n
X
i,j=1
λiµjg(vi, vj).
Spiegazione. La formula segue direttamente dalla bilinearità di g.
Corollario 19.16
Per ogni v, w ∈V vale
g(v, w) = t[v]B [g]B [w]B.
99

<!-- pagina 100 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
20
Prodotti Scalari II
20.A
Cambiamento di base
Siano B = {v1, . . . , vn} e B′ = {v′
1, . . . , v′
n} due basi di V . Indichiamo con
S = [g]B,
S′ = [g]B′
le matrici associate allo stesso prodotto scalare g, e sia
M = [id]B′
B
la matrice di cambiamento di base da B′ a B. Poiché la colonna Mi è [v′
i]B, abbiamo
S′
ij = g(v′
i, v′
j) = tMiSMj.
Proposizione 20.1
Vale
S′ = tMSM.
Esempio 20.2
Per il prodotto scalare euclideo di R2, rispetto alla base
B =
 1
0

,
 1
1

,
abbiamo già trovato
S =
 1
1
1
2

.
La matrice di cambiamento di base è
M = [id]B
C =
 1
1
0
1

,
e infatti
S = tMI2M =
 1
1
1
2

.
20.B
Forme quadratiche
Un polinomio nelle variabili x1, . . . , xn è omogeneo se tutti i suoi monomi hanno lo stesso grado.
Ad esempio,
x1 + x2 −3x3,
2x1x2 −x2
3 + x1x3,
x3
1 −x2x2
3
sono omogenei rispettivamente di grado 1, 2, 3.
100

<!-- pagina 101 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Deﬁnizione 20.3
Una forma quadratica è un polinomio omogeneo di grado 2 nelle variabili x1, . . . , xn.
Proposizione 20.4
Ogni forma quadratica si scrive in modo unico come
q(x) = gS(x, x) =
n
X
i,j=1
xiSijxj
per un’opportuna matrice simmetrica S.
Dimostrazione. Una forma quadratica si scrive
q(x) =
X
1≤i≤j≤n
aijxixj.
Deﬁnendo
Sii = aii,
Sij = Sji = 1
2aij
per i < j,
otteniamo
q(x) =
n
X
i,j=1
Sijxixj = gS(x, x).
La costruzione determina S in modo unico.
Esempio 20.5
Le matrici simmetriche

1
−3
−3
0

,
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
−1

,


0
1
1
1
0
1
1
1
0


deﬁniscono rispettivamente le forme quadratiche
x2
1 −6x1x2,
x2
1 + x2
2 −x2
3,
2x1x2 + 2x2x3 + 2x3x1.
Viceversa,
q(x) = x2
1 + 4x1x2 −x2
2 + 4x2
3
è descritta dalla matrice
S =


1
2
0
2
−1
0
0
0
4

.
Indichiamo con
qS(x) = gS(x, x)
101

<!-- pagina 102 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
la forma quadratica deﬁnita dalla matrice simmetrica S. Per deﬁnizione,
gS deﬁnito positivo ⇐⇒qS(x) > 0
∀x̸ = 0.
Per il resto della lezione assumiamo sempre che il prodotto scalare sia deﬁnito positivo.
20.C
Norma
Deﬁnizione 20.6
Sia V uno spazio vettoriale munito di un prodotto scalare deﬁnito positivo. La norma di v ∈V
è
∥v∥=
p
⟨v, v⟩.
La norma va interpretata come la lunghezza del vettore.
Proposizione 20.7
Per ogni v, w ∈V e λ ∈R valgono:
(1) ∥v∥> 0 se v̸ = 0 e ∥0∥= 0,
(2) ∥λv∥= |λ|∥v∥,
(3) |⟨v, w⟩| ≤∥v∥∥w∥,
(4) ∥v + w∥≤∥v∥+ ∥w∥.
La (3) è la disuguaglianza di Cauchy–Schwarz e la (4) è la disuguaglianza triangolare.
Dimostrazione. I primi due punti seguono direttamente dalla deﬁnizione. Per esempio
∥λv∥=
p
λ2⟨v, v⟩= |λ|∥v∥.
Per Cauchy–Schwarz, se w = 0 non c’è nulla da dimostrare. Se w̸ = 0,
0 ≤
v −⟨v, w⟩
⟨w, w⟩w

2
= ∥v∥2 −⟨v, w⟩2
∥w∥2 .
Quindi
⟨v, w⟩2 ≤∥v∥2∥w∥2,
da cui segue (3).
Inﬁne,
∥v + w∥2 = ∥v∥2 + ∥w∥2 + 2⟨v, w⟩
≤∥v∥2 + ∥w∥2 + 2∥v∥∥w∥= (∥v∥+ ∥w∥)2,
che implica (4).
102

<!-- pagina 103 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 20.8
Per il prodotto scalare euclideo su Rn,
∥x∥=
q
x2
1 + · · · + x2n.
Esempio 20.9
Consideriamo il prodotto scalare gS su R2 deﬁnito da
S =
 2
1
1
1

.
La norma di x è
∥x∥=
q
2x2
1 + 2x1x2 + x2
2.
20.D
Distanze
Quando abbiamo una norma, possiamo deﬁnire immediatamente una distanza.
Se P, Q ∈V ,
poniamo
−−→
PQ = Q −P.
Deﬁnizione 20.10
La distanza fra P e Q è
d(P, Q) = ∥Q −P∥.
Proposizione 20.11
Per ogni P, Q, R ∈V :
(1) d(P, Q) > 0 se P̸ = Q e d(P, P) = 0,
(2) d(P, Q) = d(Q, P),
(3) d(P, R) ≤d(P, Q) + d(Q, R).
Spiegazione. Le prime due proprietà seguono da quelle della norma. Per la terza,
R −P = (Q −P) + (R −Q),
e quindi la disuguaglianza triangolare dà
d(P, R) ≤d(P, Q) + d(Q, R).
103

<!-- pagina 104 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
20.E
Angoli
Deﬁnizione 20.12
Sia V munito di un prodotto scalare deﬁnito positivo. L’angolo fra due vettori non nulli v, w ∈V
è il numero ϑ ∈[0, π] tale che
cos ϑ = ⟨v, w⟩
∥v∥∥w∥.
La deﬁnizione ha senso grazie alla disuguaglianza di Cauchy–Schwarz. Equivalentemente,
ϑ = arccos ⟨v, w⟩
∥v∥∥w∥.
L’angolo è acuto, retto oppure ottuso precisamente quando ⟨v, w⟩è rispettivamente positivo, nullo
oppure negativo.
Collegamento con l’informatica: embedding e similarità coseno
In molte applicazioni di intelligenza artiﬁciale un oggetto, per esempio una parola, un documento
o un’immagine, viene rappresentato da un vettore x ∈Rn, spesso chiamato embedding. Per
confrontare due rappresentazioni x e y si usa frequentemente la similarità coseno
sim(x, y) =
⟨x, y⟩
∥x∥∥y∥= cos ϑ.
Questa quantità dipende dall’angolo e non dalla lunghezza dei due vettori. Se gli embedding
sono normalizzati, cioè ∥x∥= ∥y∥= 1, la similarità coseno è semplicemente il prodotto scalare
⟨x, y⟩. Vettori che puntano in direzioni simili hanno similarità vicina a 1.
20.F
Esercizi
Esercizio 20.13
Su R2 consideriamo il prodotto scalare g(x, y) = 2x1y1 + x1y2 + x2y1 + 2x2y2.
1. Trovare la matrice associata a g rispetto alla base canonica e la forma quadratica cor-
rispondente.
2. Veriﬁcare che g è deﬁnito positivo.
3. Calcolare le norme di e1, e2 e l’angolo fra questi due vettori.
4. Trovare la matrice associata a g rispetto alla base
B =
 1
1

,

1
−1

.
104

<!-- pagina 105 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
21
Prodotti Scalari III
21.A
Vettori ortogonali e complemento ortogonale
Sia V munito di un prodotto scalare deﬁnito positivo. Due vettori v, w ∈V sono ortogonali se
⟨v, w⟩= 0.
Se entrambi sono non nulli, questo equivale a dire che formano un angolo retto.
Esempio 21.1
Nel prodotto scalare euclideo di R2, i vettori ortogonali a
 a
b
̸
= 0
soddisfano ax + by = 0 e formano quindi la retta
Span
 −b
a

.
Esempio 21.2
Rispetto al prodotto scalare euclideo di Rn, i vettori ei ed ej della base canonica sono ortogonali
per i̸ = j.
Deﬁnizione 21.3
Sia W ⊂V un sottospazio. Il complemento ortogonale di W è
W ⊥= {v ∈V | ⟨v, w⟩= 0 per ogni w ∈W}.
Proposizione 21.4
W ⊥è un sottospazio vettoriale di V .
Dimostrazione. Abbiamo 0 ∈W ⊥. Inoltre, se v, v′ ∈W ⊥e λ ∈R, per ogni w ∈W vale
⟨v + v′, w⟩= 0,
⟨λv, w⟩= 0.
Quindi v + v′ ∈W ⊥e λv ∈W ⊥.
21.B
Proiezione ortogonale
Sia w̸ = 0 e sia
U = Span(w).
Per v ∈V cerchiamo un vettore pw(v) ∈U tale che
v −pw(v) ∈U⊥.
Questo vettore è la proiezione ortogonale di v sulla retta U.
105

<!-- pagina 106 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Proposizione 21.5
Vale
pw(v) = ⟨v, w⟩
⟨w, w⟩w = ⟨v, w⟩
∥w∥2 w.
Dimostrazione. Poiché pw(v) ∈U, scriviamo pw(v) = kw. La condizione v −kw ∈U⊥equivale a
0 = ⟨v −kw, w⟩= ⟨v, w⟩−k⟨w, w⟩,
da cui
k = ⟨v, w⟩
⟨w, w⟩.
In particolare
v = pw(v) +
 v −pw(v)

,
con il primo termine in U e il secondo in U⊥. Poiché U ∩U⊥= {0},
V = U ⊕U⊥.
Il numero
⟨v, w⟩
⟨w, w⟩
è chiamato coeﬃciente di Fourier.
Proposizione 21.6
Sia
B = {v1, . . . , vn}
una base ortogonale di V . Per ogni v ∈V ,
v =
n
X
i=1
pvi(v) =
n
X
i=1
⟨v, vi⟩
⟨vi, vi⟩vi.
Dimostrazione. Scriviamo
v = λ1v1 + · · · + λnvn.
Facendo il prodotto scalare con vi e usando l’ortogonalità otteniamo
⟨v, vi⟩= λi⟨vi, vi⟩,
e quindi
λi = ⟨v, vi⟩
⟨vi, vi⟩.
106

<!-- pagina 107 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
21.C
Ortogonalizzazione di Gram–Schmidt
Le basi ortogonali sono particolarmente utili. L’algoritmo di Gram–Schmidt trasforma vettori
linearmente indipendenti v1, . . . , vk in vettori ortogonali w1, . . . , wk ponendo
w1 = v1
e, per i ≥2,
wi = vi −
i−1
X
j=1
pwj(vi) = vi −
i−1
X
j=1
⟨vi, wj⟩
⟨wj, wj⟩wj.
Ad ogni passo togliamo quindi a vi le sue componenti nelle direzioni già costruite.
Esempio 21.7
Ortogonalizziamo
v1 =


1
1
0

,
v2 =


0
1
1

,
v3 =


1
0
1


rispetto al prodotto scalare euclideo di R3.
Otteniamo
w1 = v1 =


1
1
0

,
w2 = v2 −⟨v2, w1⟩
⟨w1, w1⟩w1 =



−1
2
1
2
1


,
e
w3 = v3 −⟨v3, w1⟩
⟨w1, w1⟩w1 −⟨v3, w2⟩
⟨w2, w2⟩w2
=



2
3
−2
3
2
3


.
I vettori w1, w2, w3 sono ortogonali.
Per ottenere una base ortonormale, basta dividere ciascun vettore per la sua norma.
21.D
Decomposizione ortogonale e proiezione su un sottospazio
L’algoritmo di Gram–Schmidt permette di estendere la proiezione ortogonale da una retta a un
sottospazio qualsiasi. Sia V di dimensione ﬁnita e sia W ⊂V un sottospazio.
107

<!-- pagina 108 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Teorema 21.8 (Decomposizione ortogonale)
Vale
V = W ⊕W ⊥.
In altre parole, ogni v ∈V si scrive in modo unico come
v = w + z,
w ∈W,
z ∈W ⊥.
In particolare,
dim W + dim W ⊥= dim V.
Spiegazione. Sia w1, . . . , wk una base ortonormale di W, ottenibile con Gram–Schmidt. Poniamo
pW (v) =
k
X
i=1
⟨v, wi⟩wi.
Per ogni j,
⟨v −pW (v), wj⟩= 0,
quindi
pW (v) ∈W,
v −pW (v) ∈W ⊥.
Pertanto V = W + W ⊥. Inoltre W ∩W ⊥= {0}, perché un vettore nell’intersezione è ortogonale
a se stesso. La somma è dunque diretta e la decomposizione è unica.
Il vettore pW (v) è la proiezione ortogonale di v su W e, per una base ortonormale,
pW (v) =
k
X
i=1
⟨v, wi⟩wi.
Proposizione 21.9
Per ogni w ∈W vale
∥v −pW (v)∥≤∥v −w∥,
con uguaglianza se e solo se w = pW (v).
Spiegazione. I vettori
v −pW (v) ∈W ⊥,
pW (v) −w ∈W
sono ortogonali. Per il teorema di Pitagora,
∥v −w∥2 = ∥v −pW (v)∥2 + ∥pW (v) −w∥2,
da cui segue l’enunciato.
108

<!-- pagina 109 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
21.E
Minimi quadrati
Consideriamo un sistema lineare
Ax = b,
con A ∈M(m, n, R) e b ∈Rm. Se il sistema non ha soluzioni, possiamo cercare x in modo che
Ax sia il più vicino possibile a b.
Deﬁnizione 21.10
Una soluzione ai minimi quadrati di Ax = b è un vettore x0 ∈Rn tale che
∥Ax0 −b∥≤∥Ax −b∥
∀x ∈Rn.
Poniamo
W = Im LA = Span(A1, . . . , An).
Per la caratterizzazione della proiezione ortogonale, x0 è una soluzione ai minimi quadrati precisa-
mente quando
Ax0 = pW (b),
cioè quando
b −Ax0 ∈W ⊥.
Ora
y ∈W ⊥⇐⇒⟨y, Ax⟩= 0
∀x ⇐⇒tAy = 0.
Applicando questo a y = b −Ax0 otteniamo:
Teorema 21.11 (Equazioni normali)
Un vettore x0 ∈Rn è una soluzione ai minimi quadrati di Ax = b se e solo se
tAAx0 = tAb.
Queste sono dette equazioni normali.
Le equazioni normali hanno sempre almeno una soluzione, perché pW (b) ∈W = Im LA. Se le
colonne di A sono linearmente indipendenti, la soluzione è unica: in questo caso tAA è invertibile
e
x0 = (tAA)−1tAb.
Esempio 21.12
Vogliamo trovare la retta
y = a + bt
che approssima al meglio, nel senso dei minimi quadrati, i punti
(0, 1),
(1, 2),
(2, 2).
109

<!-- pagina 110 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Cerchiamo quindi a, b tali che


1
0
1
1
1
2


 a
b

≈


1
2
2

.
Le equazioni normali sono
 3
3
3
5
  a
b

=
 5
6

,
da cui
a = 7
6,
b = 1
2.
La retta cercata è
y = 7
6 + 1
2t.
Collegamento con l’informatica: regressione lineare
L’esempio precedente è precisamente una regressione lineare con una variabile. I dati osservati
vengono raccolti in un vettore b, mentre la matrice A contiene le caratteristiche usate per fare
la previsione. Il modello produce il vettore Ax e i parametri x vengono scelti minimizzando
∥Ax −b∥2.
Con più variabili esplicative si aggiungono semplicemente altre colonne alla matrice A. I minimi
quadrati sono quindi uno dei primi esempi in cui proiezioni ortogonali e sistemi lineari diventano
direttamente un metodo per apprendere un modello dai dati.
21.F
Esercizi
Esercizio 21.13
Trovare la soluzione ai minimi quadrati del sistema



x
=
1,
y
=
1,
x + y
=
3.
Scrivere il sistema nella forma Ax = b, risolvere le equazioni normali e veriﬁcare che il vettore
errore
b −Ax0
sia ortogonale alle colonne di A.
110

<!-- pagina 111 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
22
Lo Spazio Euclideo I
In queste lezioni usiamo sempre il prodotto scalare euclideo sullo spazio euclideo Rn.
22.A
Isometrie lineari del piano R2
In queste lezioni consideriamo soltanto isometrie lineari, cioè isometrie che ﬁssano l’origine.
Deﬁnizione 22.1
Una rotazione di angolo ϑ è la trasformazione LA : R2 →R2 determinata dalla matrice
A = Rotϑ, con
Rotϑ =
 cos ϑ
−sin ϑ
sin ϑ
cos ϑ

.
Proposizione 22.2
La trasformazione LA è eﬀettivamente una rotazione antioraria del piano di angolo ϑ intorno
all’origine.
Notiamo che la matrice Rotϑ ha sempre determinante cos2 ϑ + sin2 ϑ = 1.
Introduciamo un’altra classe di trasformazioni del piano, le riﬂessioni (ortogonali). Fissiamo un
angolo ϑ e consideriamo la retta vettoriale r che forma un angolo ϑ
2 con l’asse delle x.
Deﬁnizione 22.3
Una riﬂessione (ortogonale) rispetto alla retta r è la trasformazione LA : R2 →R2 determinata
dalla matrice A = Rifϑ, con
Rifϑ =
 cos ϑ
sin ϑ
sin ϑ
−cos ϑ

.
Proposizione 22.4
La trasformazione LA è eﬀettivamente una riﬂessione del piano rispetto a r.
Notiamo che la matrice Rifϑ ha sempre determinante −cos2 ϑ −sin2 ϑ = −1.
Osservazione: Sia s la retta ortogonale a r, cioè facente un angolo ϑ
2 + π
2 con l’asse x, e siano v1
e v2 vettori in direzione delle rette r e s, rispettivamente. La riﬂessione può essere rappresentata
più agevolmente rispetto alla base B = {v1, v2} in cui v1 ∈r e v2 ∈s. Poiché f (v1) = v1 e
f (v2) = −v2, la matrice associata alla riﬂessione rispetto alla base B è semplicemente
 1
0
0
−1

.
111

<!-- pagina 112 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Deﬁnizione 22.5
Siano V e W due spazi vettoriali dotati ciascuno di un prodotto scalare. Un’isometria è un
isomorﬁsmo T : V →W tale che
(1)
⟨v, w⟩= ⟨T(v), T(w)⟩
∀v, w ∈V.
Brevemente, un’isometria è un isomorﬁsmo che preserva il prodotto scalare. In realtà è suﬃciente
farlo per gli elementi di una base ﬁssata. Sia B = {v1, . . . , vn} una base di V .
Proposizione 22.6
Un isomorﬁsmo T è un’isometria se e solo se
(2)
⟨vi, vj⟩= ⟨T (vi) , T (vj)⟩
∀i, j.
Spiegazione. La condizione è necessaria per deﬁnizione. Viceversa, scrivendo due vettori arbitrari
come combinazioni lineari degli elementi della base, la bilinearità del prodotto scalare e la linearità
di T estendono l’uguaglianza dagli elementi della base a tutti i vettori.
Proposizione 22.7
Sia T : V →W un isomorﬁsmo fra spazi dotati di un prodotto scalare deﬁnito positivo. I fatti
seguenti sono equivalenti:
(1) T è un’isometria,
(2) T preserva la norma, cioè ∥T(v)∥= ∥v∥∀v ∈V ,
(3) T preserva la distanza, cioè d(v, w) = d(T(v), T(w)) ∀v, w ∈V .
Cerchiamo adesso di tradurre la deﬁnizione di isometria nel linguaggio concreto delle matrici.
Siano V e V ′ spazi vettoriali muniti di prodotti scalari g e g′ e di basi B e B′ rispettivamente.
Consideriamo un isomorﬁsmo T : V →V ′. Siano
S = [g]B,
S′ =

g′
B′ ,
A = [T]B
B′
le matrici associate a tutti gli attori in scena.
Proposizione 22.8
L’isomorﬁsmo T è un’isometria se e solo se
S = tAS′A.
Spiegazione.
Per la Proposizione precedente basta controllare gli elementi della base.
Poiché
Ai = [T(vi)]B′, abbiamo
(tAS′A)ij = t(Ai)S′Aj = g′(T(vi), T(vj)),
mentre Sij = g(vi, vj).
112

<!-- pagina 113 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Consideriamo il caso che ci sta più a cuore, quello di Rn munito del suo prodotto scalare euclideo.
Sia A ∈M(n) una matrice quadrata. Consideriamo l’endomorﬁsmo LA : Rn →Rn.
Corollario 22.9
L’endomorﬁsmo LA è un’isometria ⇐⇒tAA = In.
Deﬁnizione 22.10
Una matrice A ∈M(n) a coeﬃcienti reali tale che tAA = In è detta ortogonale.
Vogliamo adesso classiﬁcare completamente le isometrie del piano R2, dotato del prodotto scalare
euclideo. Per quanto appena visto, questo problema è equivalente a classiﬁcare le matrici ortogo-
nali 2 × 2. Le matrici ortogonali 2 × 2 possono essere descritte tutte facilmente:
Proposizione 22.11
Le matrici ortogonali in M(2) sono le seguenti:
Rotϑ =
 cos ϑ
−sin ϑ
sin ϑ
cos ϑ

,
Rifϑ =
 cos ϑ
sin ϑ
sin ϑ
−cos ϑ

al variare di ϑ ∈[0, 2π).
Dimostrazione. I vettori colonna A1 e A2 di una matrice ortogonale A devono formare una base
ortonormale. Scriviamo A1 come un generico vettore unitario
A1 =
 cos ϑ
sin ϑ

Il secondo vettore A2 deve essere ortogonale ad A1 ed unitario: ci sono solo due possibilità che
diﬀeriscono solo di un segno, e otteniamo così le matrici Rotϑ e Rifϑ.
Corollario 22.12
Le isometrie di R2 sono rotazioni e riﬂessioni.
22.B
Isometrie lineari dello spazio tridimensionale
Con un po’ più lavoro, ma in modo simile, si può dimostrare:
Teorema 22.13
Ogni isometria di R3 è una rotazione o un’antirotazione. Qui, un’antirotazione T : R3 →R3
è la composizione di una rotazione intorno ad un asse r e di una riﬂessione rispetto al piano
U = r⊥.
113

<!-- pagina 114 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
22.C
Prodotto vettoriale
Deﬁnizione 22.14
Consideriamo due vettori v, w ∈R3 :
v =


v1
v2
v3

,
w =


w1
w2
w3

.
Il prodotto vettoriale fra v e w è il vettore
v × w =


v2w3 −v3w2
v3w1 −v1w3
v1w2 −v2w1

.
Notiamo che
v × w =


d1
−d2
d3


dove di è il determinante del minore 2 × 2 ottenuto cancellando la i-esima riga dalla matrice
A =


v1
w1
v2
w2
v3
w3

.
Un metodo per tenere a mente la deﬁnizione di prodotto vettoriale è il seguente. Si ottiene il
prodotto vettoriale calcolando formalmente il determinante di questa "matrice":
v × w = det


v1
w1
e1
v2
w2
e2
v3
w3
e3


= det
 v2
w2
v3
w3

e1 −det
 v1
w1
v3
w3

e2 + det
 v1
w1
v2
w2

e3.
Questa è solo una regola mnemonica: quella matrice in realtà non è una vera matrice perché
e1, e2, e3 non sono numeri ma i vettori della base canonica.
Proposizione 22.15
Il vettore v × w è ortogonale sia a v che a w.
Dimostrazione. Si ottiene
⟨v × w, v⟩= det
 v2
w2
v3
w3

v1 −det
 v1
w1
v3
w3

v2 + det
 v1
w1
v2
w2

v3
= det


v1
w1
v1
v2
w2
v2
v3
w3
v3

= 0.
114

<!-- pagina 115 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
La seconda uguaglianza è lo sviluppo di Laplace sull’ultima colonna. Il determinante è nullo perché
la matrice ha due colonne uguali. Analogamente si trova ⟨v × w, w⟩= 0.
Proposizione 22.16
Il vettore v × w è nullo ⇐⇒v e w sono dipendenti.
Dimostrazione. Con la notazione in cima di questa pagina otteniamo
v × w = 0 ⇐⇒d1 = d2 = d3 = 0 ⇐⇒rkA ≤1 ⇐⇒v e w sono dipendenti.
Corollario 22.17
Se v e w sono indipendenti, la terna v, w, v × w è una base di R3.
115

<!-- pagina 116 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
23
Lo Spazio Euclideo II
23.A
Altre proprietà del prodotto vettoriale
Dimostriamo adesso alcune proprietà del prodotto vettoriale. Siano v, w ∈R3 due vettori qualsiasi.
Proposizione 23.1
Vale l’equazione ∥v × w∥2 + ⟨v, w⟩2 = ∥v∥2∥w∥2.
Dimostrazione. Troviamo
∥v × w∥2 =(v2w3 −v3w2)2 + (v1w3 −v3w1)2 + (v1w2 −v2w1)2
=(v2
1 + v2
2 + v2
3)(w2
1 + w2
2 + w2
3) −(v1w1 + v2w2 + v3w3)2
=∥v∥2∥w∥2 −⟨v, w⟩2.
Supponiamo che v e w siano indipendenti. I due vettori sono contenuti nel piano π = Span(v, w).
Indichiamo con P ⊂π il parallelogramma avente lati v e w. Si veda la Figura 8.
Figura 8. Il modulo ∥v × w∥è pari all’area del parallelogramma P con lati v e w contenuto nel
piano π = Span(v, w).
Proposizione 23.2
L’area di P è Area(P) = ∥v∥∥w∥sin ϑ.
Mostriamo che questa è anche uguale al modulo di v × w.
Corollario 23.3
Il modulo del prodotto vettoriale è
∥v × w∥= ∥v∥∥w∥sin ϑ = Area(P)
dove ϑ è l’angolo formato da v e w e P è il parallelogramma con lati v e w.
116

<!-- pagina 117 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Spiegazione. Dalla Proposizione 23.1 e da ⟨v, w⟩= ∥v∥∥w∥cos ϑ segue
∥v × w∥2 = ∥v∥2∥w∥2 sin2 ϑ,
e quindi la formula, poiché 0 ≤ϑ ≤π.
Se v e w sono dipendenti, allora v × w = 0. Se sono indipendenti, allora la direzione di v × w è
ortogonale al piano contenente v e w e il modulo di v × w è l’area di P. Queste due condizioni
determinano il vettore v × w a meno di segno: per scegliere il “verso giusto” è suﬃciente usare la
regola della mano destra mostrata nella Figura 9 e giustiﬁcata dalla proposizione seguente.
Figura 9. La regola della mano destra.
Proposizione 23.4
Se v e w sono indipendenti, la terna v, w, v × w è una base positiva di R3, cioè, la matrice
avente come colonne v, w, v × w ha determinante positivo.
Possiamo quindi deﬁnire geometricamente il prodotto vettoriale v × w di due vettori indipendenti
come l’unico vettore ortogonale ad entrambi, di lunghezza pari all’area del parallelogramma con
lati v e w, e orientato positivamente rispetto a v e w.
Dalla deﬁnizione seguono facilmente anche i fatti seguenti:
• v × w = −w × v per ogni v, w ∈R3
• il prodotto vettoriale × : R3 × R3 →R3 è bilineare. Come per il prodotto scalare, per
bilinearità intendiamo:
(v + v′) × w = v × w + v′ × w,
(λv) × w = λ(v × w),
v × (w + w′) = v × w + v × w′,
v × (λw) = λ(v × w).
C’è inﬁne una diﬀerenza fondamentale fra il prodotto vettoriale e altri prodotti, come quello fra
numeri o fra matrici: non è veriﬁcata la proprietà associativa! Infatti ad esempio:
(e1 × e2) × e2 = e3 × e2 = −e2 × e3 = −e1,
e1 × (e2 × e2) = e1 × 0 = 0.
117

<!-- pagina 118 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
23.B
Forma cartesiana e forma parametrica
Un sottospazio vettoriale di Rn che sia descritto come luogo di zeri di un sistema di equazioni lineari
omogenee è detto in forma cartesiana. Un sottospazio vettoriale di Rn descritto come sottospazio
generato da alcuni vettori è invece detto in forma parametrica. Qualsiasi sottospazio vettoriale
di Rn può essere descritto in entrambi i modi. Ad esempio, il piano W = {z = 0} in R3 può
essere descritto in forma cartesiana tramite l’equazione z = 0, oppure in forma parametrica come
il sottospazio generato dai due vettori e1 e e2. Otteniamo in questo modo:
W = Span(e1, e2) =


t


1
0
0

+ s


0
1
0

| s, t ∈R


=





t
s
0

| s, t ∈R



La forma parametrica è esplicita perché indica chiaramente come sono fatti i punti di W, al variare
di alcuni parametri (in questo caso t e s). La forma cartesiana è implicita perché descrive W come
luogo di soluzioni di un’equazione (o di un sistema di equazioni). In molti casi la forma parametrica
è preferibile proprio perché esplicita, ma può anche capitare che quella implicita sia più comoda, a
seconda del contesto.
23.C
Forma parametrica e cartesiana degli spazi aﬃni
Ci ricordiamo che l’insieme S di soluzioni di un sistema lineare geometricamente è sempre un
sottospazio aﬃne, cioè, un sottoinsieme di V del tipo
S = {x + v | v ∈W}
dove x è un punto ﬁssato di V e W ⊆V è un sottospazio vettoriale. Più precisamente, abbiamo
visto che le soluzioni S di un sistema di equazioni lineari formano l’insieme vuoto oppure un
sottospazio aﬃne di Rn. Infatti, se S̸ = ∅, allora
S = {x + v | v ∈S0}
dove x è un punto qualsiasi di S e S0 è l’insieme delle soluzioni del sistema lineare omogeneo
associato, che è sempre un sottospazio vettoriale. Per indicare un sottospazio aﬃne S, usiamo
semplicemente la scrittura
S = x + W = {x + v | v ∈W}.
Lo stesso sottospazio aﬃne può essere descritto in più modi diversi. Chiariamo subito quando due
scritture diﬀerenti descrivono lo stesso sottospazio:
Proposizione 23.5
Gli spazi aﬃni x + W e x′ + W ′ coincidono se e solo se W = W ′ e x −x′ ∈W.
118

<!-- pagina 119 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 23.6
Se W = Span
 1
1

in R2, le due rette aﬃni
r1 =
 1
0

+ W =
 t + 1
t

| t ∈R

r2 =

0
−1

+ W =

u
u −1

| u ∈R

sono in realtà la stessa retta di equazione y = x −1.
Deﬁnizione 23.7
Nella descrizione di uno spazio aﬃne S come x + W, lo spazio vettoriale W è determinato da
S ed è detto la giacitura di S e indicato con giac(S). Il punto x invece è un qualsiasi punto di
S. La dimensione di S è la dimensione della giacitura W.
Un sottospazio aﬃne di Rn può essere descritto in forma parametrica (cioè esplicita) come
S = x + Span(v1, ..., vk) = {x + t1v1 + . . . + tkvk | t1, . . . , tk ∈R},
dove i vettori v1, . . . , vk ∈Rn formano una base per la giacitura W. Qui ovviamente dim S = k.
In alternativa S può essere descritto in forma cartesiana (cioè implicita) come insieme di soluzioni
di un sistema lineare S = {x ∈Rn | Ax = b}. Qui A ∈M(m, n) e b ∈Rm. Sappiamo per il
Teorema di Rouché-Capelli che S̸ = ∅⇔rk A = rk(A|b) e in questo caso dim S = n −rk A.
Collegamento con l’informatica: classiﬁcatori lineari
Un iperpiano aﬃne in Rn può essere scritto nella forma
twx + b = 0.
Esso divide lo spazio nei due semispazi in cui twx + b è positivo oppure negativo. Un semplice
classiﬁcatore lineare assegna quindi a un vettore di dati x una delle due classi guardando il
segno di
twx + b.
Il vettore w è ortogonale all’iperpiano di separazione. Questa stessa geometria è alla base di
modelli classici di machine learning come il percettrone e le macchine a vettori di supporto nella
loro forma lineare.
I sottospazi aﬃni di R3 sono i punti, le rette, i piani, e R3 stesso. Un piano aﬃne π in R3 è
descritto da un’equazione
π = {ax + by + cz = d}
oppure da un punto e due vettori che generano la giacitura
π = {P0 + tv1 + sv2 | t, s ∈R}.
119

<!-- pagina 120 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Una retta aﬃne r in R3 è descritta da due equazioni dello stesso tipo di sopra, oppure più agevol-
mente in forma parametrica:
r = {P0 + tv | t ∈R}.
Per passare da coordinate cartesiane a parametriche si risolve il sistema Ax = b, ad esempio
usando l’algoritmo di Gauss-Jordan. A volte può servire fare l’opposto, cioè passare da coordinate
parametriche a cartesiane. Questo passaggio è particolarmente facile per i piani in R3. Sia
π = {P0 + tv1 + uv2}
un piano aﬃne in R3, dove v1, v2 ∈R3 sono vettori indipendenti. Calcoliamo il vettore v1 × v2.
Questo avrà tre coeﬃcienti a, b, c. Il piano π può essere descritto come
π = {ax + by + cz = d}
per un certo d ∈R che può essere trovato imponendo P0 ∈π.
Esempio 23.8
Consideriamo
π =





1
2
−3

+ t


1
0
1

+ s


2
−1
0





Troviamo


1
0
1

×


2
−1
0

=


1
2
−1


Quindi
π = {x + 2y −z = d}
per qualche d ∈R, che determiniamo imponendo


1
2
−3

∈π ⇒1 + 4 + 3 = d
e quindi d = 8. Abbiamo trovato un’equazione cartesiana per il piano: π = {x + 2y −z = 8}.
23.D
Intersezioni
Mentre sottospazi vettoriali devono sempre intersecarsi almeno nell’origine, sottospazi aﬃni pos-
sono non intersecarsi. Due sottospazi aﬃni S, S′ ⊂Rn sono incidenti se S ∩S′̸ = ∅. Se sono
incidenti, possiamo prendere x ∈S ∩S′ e scrivere entrambi come S = x + W, S′ = x + W ′. In
questo modo chiaramente otteniamo S ∩S′ = x + (W ∩W ′). Ne deduciamo in particolare che
l’intersezione (se non è vuota) è sempre uno spazio aﬃne.
Per calcolare l’intersezione di due spazi incidenti, dobbiamo in generale risolvere (sistemi di)
equazioni lineari, ma cosa dobbiamo fare precisamente dipende un po’ sulla forma (cartesiana
120

<!-- pagina 121 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
o parametrica) data per S e S′. Abbiamo visto sopra che possiamo cambiare fra le due forme, ma
è utile poter fare i calcoli anche in modo più diretto.
Esempio 23.9
Se S e S′ sono entrambi descritti in forma cartesiana, la loro intersezione S ∩S′ è descritta in
forma cartesiana semplicemente unendo le equazioni di S e S′. Ad esempio se S = {x + y = 1}
e S′ = {x−y +z = 3} sono due piani in R3, la loro intersezione S ∩S′ è l’insieme delle soluzioni
di
 x + y = 1
x −y + z = 3
Se S è descritto in forma cartesiana e S′ in forma parametrica, per trovare S ∩S′ è suﬃciente
sostituire il punto generico di S′ nelle equazioni di S e trovare i parametri che le soddisfano. Ad
esempio, se S = {x + y −z = 2} è un piano in R3 e
S′ =





1
−1
1

+ t


1
2
−3




=





1 + t
−1 + 2t
1 −3t





è una retta in R3, per trovare S∩S′ si sostituisce x = 1+t, y = −1+2t, z = 1−3t nell’equazione
che deﬁnisce S e si ottiene 1 + t −1 + 2t −1 + 3t = 2 ⇔t = 1/2 e quindi l’intersezione S ∩S′
è il punto
S ∩S′ =





3/2
0
−1/2




.
Se entrambi S e S′ sono in forma parametrica, si eguaglia il punto generico di S con quello di
S′ e si trova quali parametri risolvono il sistema. Questo procedimento può essere più laborioso
dei precedenti.
Vediamo adesso una condizione sulle giaciture che garantisce che i sottospazi si intersechino.
Proposizione 23.10
Se giac(S) + giac(S′) = Rn, allora i sottospazi S e S′ sono incidenti.
121

<!-- pagina 122 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
24
Lo Spazio Euclideo III
Ci ricordiamo che due sottospazi aﬃni S, S′ ⊂Rn sono incidenti se S ∩S′̸ = ∅. Se sono incidenti,
possiamo studiare l’angolo dell’intersezione. Se invece non sono incidenti, possiamo studiare la loro
distanza. In questa lezione impariamo esattamente questo.
24.A
Angoli fra sottospazi incidenti
Ci sono alcuni casi da considerare separatamente.
Deﬁnizione 24.1 (Angolo tra rette.)
Siano r e r′ due rette in R3 che si intersecano in un punto P. Abbiamo r = P + Span(v) e
r′ = P + Span (v′) e deﬁniamo l’angolo fra r e r′ come l’angolo ϑ formato da v e v′.
A seconda di come si scelgano i generatori v e v′ gli angoli possibili sono due: ϑ e π −ϑ. Possiamo
scegliere sempre un angolo acuto o retto (se ϑ è ottuso, prendiamo π −ϑ). Ci ricordiamo che
l’angolo tra v e v′ è dato dalla formula
cos ϑ = ⟨v, v′⟩
∥v∥∥v′∥.
Deﬁnizione 24.2 (Angolo tra retta e piano.)
Siano r una retta e π un piano che si intersecano in un punto P. Deﬁniamo l’angolo ϑ fra r e π
nel modo seguente. Trasliamo l’origine in modo che P = 0. A questo punto π è un sottospazio
vettoriale e deﬁniamo il vettore v′ = pπ(v) facendo la proiezione ortogonale di v su π. Se v′ = 0
poniamo ϑ = π
2 , altrimenti deﬁniamo ϑ come l’angolo fra v e v′.
In altre parole, se r non è ortogonale a π, proiettando r ortogonalmente su π otteniamo una retta
r′ ⊂π e deﬁniamo ϑ come l’angolo acuto fra r e r′.
Abbiamo visto che se v1, v2 è una base ortogonale per π (una base così possiamo sempre ottenere
con l’algoritmo di Gram-Schmidt), allora
pπ(v) = ⟨v, v1⟩
⟨v1, v1⟩v1 + ⟨v, v2⟩
⟨v2, v2⟩v2.
Esempio 24.3
Consideriamo π = {x + y −z = 0} ⊂R3 e il vettore e3. Cerchiamo prima una base ortogonale
per π e troviamo ad esempio
v1 =


1
1
2

,
v2 =


1
−1
0


A questo punto determiniamo la proiezione ortogonale su π di un generico vettore di R3 usando
122

<!-- pagina 123 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
l’osservazione precedente, in questo modo:
pπ


x
y
z

= x + y + 2z
6


1
1
2

+ x −y
2


1
−1
0

= 1
3


2x −y + z
−x + 2y + z
x + y + 2z


Quindi la matrice associata a pπ nella base canonica è
1
3


2
−1
1
−1
2
1
1
1
2


Usando questa matrice possiamo calcolare la proiezione ortogonale su π di qualsiasi vettore di
R3. In particolare
pπ(e3) = 1
3


1
1
2

,
e allora l’angolo fra e3 e π è
ϑ = arccos
*

1
1
2

,


0
0
1


+



1
1
2






0
0
1



= arccos 2
√
6 = arccos
√
6
3
≃0.615
che corrisponde a un angolo di ∼35.3◦.
Proposizione 24.4
L’angolo fra v e il piano π e l’angolo fra v e il vettore ortogonale a π che forma un angolo acuto
con v si sommano a π
2 .
Esempio 24.5
Nell’esempio di prima, possiamo calcolare l’angolo ϑ anche come π
2 −α, dove α è l’angolo fra
e3 e il vettore
n =


−1
−1
1


123

<!-- pagina 124 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
che è ortogonale a π. Allora
ϑ = π
2 −arccos
*

−1
−1
1

,


0
0
1


+



−1
−1
1






0
0
1



= π
2 −arccos 1
√
3 ≃1.570 −0.955 = 0.615.
Otteniamo allora lo stesso risultato.
Deﬁnizione 24.6 (Angolo tra piani.)
Siano π1 e π2 due piani che si intersecano in una retta r = π1 ∩π2. L’angolo (diedrale) fra π1 e
π2 è deﬁnito nel modo seguente: si prendono due rette s1 ⊂π1 e s2 ⊂π2 incidenti ed entrambe
ortogonali a r; l’angolo diedrale fra π1 e π2 è per deﬁnizione l’angolo α fra s1 e s2. Si ottengono
in realtà due angoli α e π −α e scegliamo come sempre quello acuto (o retto).
Proposizione 24.7
Siano v1 e v2 due vettori non nulli ortogonali a π1 e π2. L’angolo α fra π1 e π2 è uguale all’angolo
acuto (o retto) fra le rette generate da v1 e v2.
Usando la proposizione, è molto facile calcolare l’angolo fra due piani:
π1 = {a1x + b1y + c1z = d1} ,
π2 = {a2x + b2y + c2z = d2} .
Questo è semplicemente l’angolo acuto (o retto) fra le rette generate dai vettori dei coeﬃcienti.
Esempio 24.8
I piani π1 = {x + y −z = 3} e π2 = {x −y −z = 9} formano un angolo
ϑ = arccos
*

1
1
−1

,


1
−1
−1


+



1
1
−1






1
−1
−1



= arccos
1
√
3
√
3 = arccos 1
3 ≃1.230.
Questo corrisponde a un angolo di ∼70.5◦.
24.B
Distanze fra sottospazi disgiunti
Deﬁniamo inﬁne la distanza d (S, S′) fra due sottospazi aﬃni S e S′ di R3. Se sono incidenti, la
distanza è zero. Se i sottospazi sono disgiunti la distanza è positiva ed è deﬁnita in modo diverso
caso per caso.
124

<!-- pagina 125 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Deﬁnizione 24.9 (Distanza fra punti.)
Come già sappiamo, la distanza d(P, Q) fra due punti P, Q ∈R3 è deﬁnita usando la norma:
d(P, Q) = ∥−−→
PQ∥= ∥Q −P∥.
Deﬁnizione 24.10 (Distanza fra punto e retta.)
La distanza d(P, r) fra un punto P ed una retta r nello spazio è deﬁnita nel modo seguente.
Tracciamo come nella Figura 10 la perpendicolare s a r nel punto P e deﬁniamo
d(P, r) = d(P, Q)
dove Q = r ∩s.
Figura 10. La distanza fra P e la retta r è la lunghezza del segmento PQ ortogonale a r.
Se la retta r è espressa in forma parametrica r = {P0 + tv0} come nella Figura 10 (a destra), la
distanza si calcola facilmente usando il prodotto vettoriale.
Proposizione 24.11
Vale l’uguaglianza
d(P, r) = ∥v0 × v1∥
∥v0∥
dove v1 = −−→
P0P = P −P0.
Dimostrazione. L’area del parallelogramma mostrato nella Figura 10 può essere calcolata in due
modi: con il prodotto vettoriale ∥v0 × v1∥e come base per altezza ∥v0∥· d(P, Q). L’uguaglianza
∥v0 × v1∥= ∥v0∥· d(P, Q)
implica la formula per d(P, r) = d(P, Q).
125

<!-- pagina 126 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esempio 24.12
Consideriamo il punto P e la retta r seguenti:
P =


1
−2
3

,
r =





−1
0
1

+ t


3
2
1





La distanza fra P e r è
d(P, r) =



3
2
1

×


2
−2
2






3
2
1



=



6
−4
−10



√
14
= 2
√
38
√
14 = 2
7
√
133.
Deﬁnizione 24.13 (Distanza fra rette.)
La distanza d (r, r′) fra due rette r ed r′ disgiunte nel piano o nello spazio è deﬁnita nel modo
seguente. Le due rette r e r′ sono parallele o sghembe. In entrambi i casi troviamo una retta s
perpendicolare ad entrambe. Deﬁniamo quindi
d
 r, r′
= d
 P, P ′
dove P = r ∩s e P ′ = r′ ∩s.
Anche in questo caso, se r = {P0 + tv} e r′ = {P ′
0 + uv′} sono espresse in forma parametrica
la distanza si calcola facilmente. Se sono parallele, la distanza d (r, r′) è uguale a d (P0, r′) ed
applichiamo la Proposizione 24.11. Consideriamo il caso in cui le rette siano sghembe.
Figura 11. La distanza fra due rette sghembe è la lunghezza del segmento PP ′ ortogonale ad
entrambe.
126

<!-- pagina 127 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Proposizione 24.14
Se r e r′ sono sghembe, vale la formula
d
 r, r′
= |det (v |v′| v′′)|
∥v × v′∥
dove v′′ = −−−→
P0P ′
0 = P ′
0 −P0.
Dimostrazione. Ragioniamo come per la Proposizione 24.11. Il volume del parallelepipedo nella
Figura 11 (destra) generato da v, v′ e v′′ può essere calcolato in due modi: come |det (v |v′| v′′)|
e come area di base per altezza, cioè ∥v × v′∥· d. L’altezza d è proprio d = d (P, P ′) = d (r, r′) e
quindi si ottiene
det
 v
v′ v′′ = d
 r, r′
·
v × v′
che implica la formula per d (r, r′).
Esempio 24.15
Calcoliamo la distanza fra le rette sghembe
r =





2
−5
1

+ t


2
0
1




,
r′ =





1
1
0

+ u


−1
−2
3




.
Questa è
d
 r, r′
=

det


2
−1
−1
0
−2
6
1
3
−1






2
0
1

×


−1
−2
3



= |2(2 −18) + (−6 −2)|
p
22 + (−7)2 + (−4)2 =
40
√
69 = 40
69
√
69.
Deﬁnizione 24.16 (Distanza fra punto e piano.)
La distanza fra un punto P0 ed un piano π nello spazio è deﬁnita in modo simile a quanto già
visto: si traccia la perpendicolare s a π passante per P0 e si deﬁnisce
d (P0, π) = d (P0, Q)
con Q = s ∩π.
127

<!-- pagina 128 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Se
π = {ax + by + cz = d},
P0 =


x0
y0
z0


allora la distanza si calcola facilmente con una formula.
Proposizione 24.17
Vale
d (P0, π) = |ax0 + by0 + cz0 −d|
√
a2 + b2 + c2
.
Esempio 24.18
Consideriamo il piano ed il punto seguenti in R3 :
π = {2x −y + z = 4},
P0 =


2
1
−2

.
Applicando la formula troviamo
d (P0, π) = |2 · 2 −1 −2 −4|
√
6
=
√
6
2 .
128

<!-- pagina 129 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
25
Teorema Spettrale I
25.A
Prodotti hermitiani
In Lezione 19-21 abbiamo introdotto i prodotti scalari per spazi vettoriali reali. Mostriamo adesso
brevemente come sia possibile deﬁnire una nozione analoga anche per gli spazi vettoriali complessi:
questa estensione è nota con il nome di prodotto hermitiano.
Deﬁnizione 25.1
Sia V uno spazio vettoriale complesso. Un prodotto hermitiano su V è un’applicazione
V × V −→C
(v, w) 7−→⟨v, w⟩
che soddisfa i seguenti assiomi:
(1) ⟨v + v′, w⟩= ⟨v, w⟩+ ⟨v′, w⟩,
(2) ⟨λv, w⟩= λ⟨v, w⟩,
(3) ⟨v, w⟩= ⟨w, v⟩,
per ogni v, v′, w ∈V e ogni λ ∈C.
Notiamo immediatamente che l’assioma (3) diﬀerisce da quello analogo per i prodotti scalari per
la presenza di un coniugio. Il motivo di questo cambiamento sarà presto chiaro. Intanto da questi
assiomi deduciamo facilmente altre proprietà:
(4) ⟨v, w + w′⟩= ⟨v, w⟩+ ⟨v, w′⟩,
(5) ⟨v, λw⟩= ¯λ⟨v, w⟩,
(6) ⟨0, w⟩= ⟨v, 0⟩= 0,
per ogni v, w, w′ ∈V e λ ∈C.
Ad esempio, la proprietà (5) si mostra così:
⟨v, λw⟩= ⟨λw, v⟩= λ⟨w, v⟩= ¯λ⟨w, v⟩= ¯λ⟨v, w⟩.
Perché abbiamo inserito il coniugio in (3), che per adesso ha come unico eﬀetto quello di rendere
lievemente più complicati i passaggi algebrici? Lo abbiamo fatto essenzialmente per ottenere la
proprietà seguente:
(7) ⟨v, v⟩è un numero reale, per ogni v ∈V .
Per dimostrare ciò, notiamo che l’assioma (3) implica che ⟨v, v⟩= ⟨v, v⟩e quindi eﬀettivamente
⟨v, v⟩∈R. Il coniugio in (3) è un trucco per ottenere che ⟨v, v⟩sia un numero reale!
129

<!-- pagina 130 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Osservazione. Gli assiomi (1), (2) e (4) sono gli stessi dei prodotti scalari, mentre la proprietà
(5) è diﬀerente. Diciamo che il prodotto hermitiano è lineare a sinistra e antilineare a destra.
Unendo queste due proprietà, diciamo anche che un prodotto hermitiano è sesquilineare invece
che bilineare, dal latino sesqui che denota il numero 1,5. In un certo senso, un prodotto hermitiano
è lineare una volta e mezzo ma non due.
Visto che ⟨v, v⟩è un numero reale, è perfettamente sensato chiedere se questo numero sia positivo
o no. Possiamo quindi introdurre questa deﬁnizione, come abbiamo fatto nel caso reale.
Deﬁnizione 25.2
Un prodotto hermitiano è deﬁnito positivo se ⟨v, v⟩> 0 per ogni v̸ = 0.
In un prodotto hermitiano deﬁnito positivo si deﬁniscono in modo del tutto analogo al caso reale
molti dei concetti già visti precedentemente. La norma di un vettore è
∥v∥=
p
⟨v, v⟩.
Si possono quindi introdurre le nozioni di spazio ortogonale e di base ortonormale ed il procedi-
mento di Gram–Schmidt funziona anche in questo contesto.
Esempio 25.3
Se x ∈Cn è un vettore e più in generale A ∈M(m, n, C) è una matrice a coeﬃcienti complessi,
indichiamo con ¯x e ¯A il vettore o matrice ottenuto da x oppure A facendo il coniugio di ogni
singolo elemento. Il prodotto hermitiano euclideo su Cn è dato da
⟨x, y⟩= tx ¯y.
Questo è eﬀettivamente un prodotto hermitiano, analogo al prodotto scalare euclideo: notiamo
il coniugio presente sulla variabile y, grazie al quale risulta valido l’assioma (3), infatti
⟨y, x⟩= ty¯x = t¯yx = tx¯y = ⟨x, y⟩.
Come nel caso reale, il prodotto hermitiano euclideo è deﬁnito positivo, perché per ogni x ∈Cn
non nullo troviamo
⟨x, x⟩= tx¯x = x1¯x1 + · · · xn¯xn = |x1|2 + · · · + |xn|2 > 0.
25.B
Matrici hermitiane
Le matrici hermitiane giocano nei prodotti hermitiani lo stesso ruolo delle matrici simmetriche nei
prodotti scalari.
Deﬁnizione 25.4
Una matrice hermitiana è una matrice quadrata complessa H per cui
tH = ¯H.
130

<!-- pagina 131 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
In altre parole vale Hij = ¯Hji per ogni i, j.
Ad esempio, la matrice seguente è una matrice
hermitiana:

2
1 + i
1 −i
1

Notiamo che in una matrice hermitiana gli elementi Hii sulla diagonale devono necessariamente
essere reali, perché Hii = Hii per ogni i.
Osservazione. Una matrice quadrata a coeﬃcienti reali è hermitiana se e solo se è simmetrica.
Così come una matrice simmetrica S deﬁnisce un prodotto scalare gS su Rn, una matrice hermitiana
H determina un prodotto hermitiano gH su Cn nel modo seguente:
gH(x, y) = txH¯y.
Notiamo che eﬀettivamente l’assioma (3) è soddisfatto:
gH(x, y) = txH¯y = t  txH¯y

= t¯y tHx = t¯y ¯Hx = tyH¯x = gH(y, x).
La veriﬁca degli assiomi (1) e (2) è identica a quando visto per i prodotti scalari. Come per i
prodotti scalari vale
gH (ei, ej) = teiH¯ej = teiHej = Hij
dove e1, . . . , en è la base canonica di Cn.
25.C
Matrice associata
Come nel caso reale, se V è uno spazio vettoriale complesso munito di un prodotto hermitiano e
B = {v1, . . . , vn} è una base di V , possiamo deﬁnire la matrice associata H nel modo seguente:
Hij = ⟨vi, vj⟩
per ogni i, j. Abbiamo scelto la lettera H invece di S perché questa matrice non è simmetrica ma
bensì hermitiana: infatti per l’assioma (3) abbiamo
Hij = Hji.
Per ogni coppia di vettori v, w ∈V possiamo sempre scrivere
⟨v, w⟩= t[v]B · H · [w]B.
Questo fatto si dimostra esattamente come per un prodotto scalare, stando attenti alla sesquilin-
earità, cioè alla presenza di un coniugio nella proprietà (5).
Come per i prodotti scalari otteniamo allora che qualsiasi prodotto hermitiano su Cn è della forma
gH per qualche matrice hermitiana H.
131

<!-- pagina 132 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
25.D
Endomorﬁsmi autoaggiunti
Introduciamo in questo capitolo un’importante classe di endomorﬁsmi.
Indichiamo con V uno
spazio vettoriale reale dotato di un prodotto scalare deﬁnito positivo, oppure uno spazio vettoriale
complesso dotato di un prodotto hermitiano deﬁnito positivo.
Deﬁnizione 25.5
Un endomorﬁsmo T : V →V è autoaggiunto se
⟨T(v), w⟩= ⟨v, T(w)⟩
per ogni v, w ∈V .
Notiamo subito che questa deﬁnizione ricorda un po’ quella di isometria, in cui si chiede che
⟨v, w⟩= ⟨T(v), T(w)⟩. Ci sono eﬀettivamente delle analogie fra le due deﬁnizioni, ma anche delle
importanti diﬀerenze.
Come con le isometrie, cerchiamo subito di tradurre la deﬁnizione di endomorﬁsmo autoaggiunto
in una condizione concreta sulle matrici associate. Scegliamo una base ortonormale B di V . Sia
T : V →V un endomorﬁsmo e A = [T]B
B la sua matrice associata.
Proposizione 25.6
L’endomorﬁsmo T è autoaggiunto se e solo se la matrice A è hermitiana.
Dimostrazione. Per bilinearità (o sesquilinearità nel caso complesso), per veriﬁcare se T è autoag-
giunto è suﬃciente testare la condizione della deﬁnizione sugli elementi vi, vj della base B. Nel
caso complesso, ricaviamo
⟨T (vi) , vj⟩= t [T (vi)]B · In · [vj]B = tAiej = Aji,
⟨vi, T (vj)⟩= t [vi]B · In · [T (vj)]B = tei ¯Aj = Aij.
Quindi T è autoaggiunto se e solo se
Aji = Aij
per ogni i, j, in altre parole se e solo se A è hermitiana. Il caso reale è del tutto analogo (senza i
coniugi).
Prendendo la base canonica di Rn o Cn (che sono ortonormali!) otteniamo questo corollario.
Corollario 25.7
Sia A una matrice n × n. L’endomorﬁsmo LA : Cn →Cn è autoaggiunto rispetto al prodotto
hermitiano euclideo di Cn se e solo se la matrice A è hermitiana. Analogamente, se A è reale,
l’endomorﬁsmo LA : Rn →Rn è autoaggiunto rispetto al prodotto scalare euclideo di Rn se e
solo se la matrice A è simmetrica.
Osservazione. Le matrici hermitiane (o simmetriche) hanno un doppio ruolo in questo capitolo:
sia come matrici che rappresentano un prodotto hermitiano (o scalare), che come matrici che rap-
presentano un endomorﬁsmo autoaggiunto (rispetto ad una base ortonormale).
132

<!-- pagina 133 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Notiamo che la Proposizione 25.6 è valida solo se prendiamo una base B ortonormale, come mostra
questo esempio.
Esempio 25.8
Consideriamo R2 con il prodotto scalare euclideo. L’endomorﬁsmo LA deﬁnito dalla matrice
A =
 2
1
1
1

è autoaggiunto perché la matrice A è simmetrica e stiamo usando la base
canonica che è ortonormale.
Se scriviamo LA rispetto ad un’altra base ortonormale, ad esempio B =
 0
1

,
 −1
0

,
otteniamo una nuova matrice simmetrica:
A′ =

0
1
−1
0
  2
1
1
1
  0
−1
1
0

=

1
−1
−1
2

.
Questo è coerente con la Proposizione 25.6. Se però scriviamo A rispetto ad una base non
ortonormale, ad esempio B =
 −1
1

,
 1
0

, la nuova matrice associata può non essere
simmetrica. In questo caso otteniamo veramente
A′ =
 0
1
1
1
  2
1
1
1
  −1
1
1
0

=

0
1
−1
3

,
che non è una matrice simmetrica.
25.E
Sottospazi invarianti
Sia come sempre V uno spazio vettoriale complesso dotato di un prodotto hermitiano deﬁnito
positivo, oppure uno spazio reale dotato di un prodotto scalare deﬁnito positivo. Sia T : V →V
un endomorﬁsmo.
Deﬁnizione 25.9
Diciamo che un sottospazio U ⊂V è T-invariante se T(U) ⊂U, cioè T manda gli elementi di
U in U.
Proposizione 25.10
Sia T : V →V un endomorﬁsmo autoaggiunto e U ⊂V un sottospazio. Se T(U) ⊂U allora
T
 U⊥
⊂U⊥. In altre parole se U è T-invariante allora anche U⊥è T-invariante.
Dimostrazione. Prendiamo un vettore qualsiasi v ∈U⊥e dobbiamo dimostrare che T(v) ∈U⊥.
Per ogni vettore u ∈U otteniamo
⟨T(v), u⟩= ⟨v, T(u)⟩= 0
perché T(u) ∈U per ipotesi. Quindi T(v) è ortogonale a tutti i vettori u ∈U, in altre parole
T(v) ∈U⊥.
133

<!-- pagina 134 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
26
Teorema Spettrale II
Introduciamo oggi un risultato noto come teorema spettrale. Si tratta di uno degli enunciati più im-
portanti dell’algebra lineare, con varie implicazioni in diversi rami della scienza moderna. Il teorema
collega due importanti argomenti studiati in questo corso: la diagonalizzabilità degli endomorﬁsmi
e i prodotti scalari (o hermitiani) deﬁniti positivi.
La motivazione principale che sta dietro al teorema è la seguente considerazione: abbiamo visto
che gli endomorﬁsmi più semplici da studiare sono quelli diagonalizzabili, cioè quelli che hanno
una base di autovettori. In quali casi possiamo chiedere che questa base di autovettori sia anche
ortonormale? Il teorema spettrale risponde completamente a questa domanda: questo è possibile
precisamente per gli endomorﬁsmi autoaggiunti.
26.A
Il teorema spettrale
Teorema 26.1 (Teorema spettrale)
Un endomorﬁsmo T : V →V è autoaggiunto ⇐⇒ha una base ortonormale di autovettori e
tutti i suoi autovalori sono in R.
Dimostrazione. (⇐) Se T ha una base B ortonormale di autovettori, la matrice A = [T]B
B è
diagonale; poiché gli autovalori sono reali, la matrice A è diagonale con numeri reali sulla diago-
nale e quindi è chiaramente hermitiana. Per la Proposizione 25.6, l’endomorﬁsmo T è autoaggiunto.
(⇒) Dimostriamo il teorema innanzitutto nel caso complesso. Iniziamo veriﬁcando che tutti gli
autovalori di T sono reali: se λ è autovalore, allora c’è un autovettore v e T(v) = λv, quindi
λ⟨v, v⟩= ⟨λv, v⟩= ⟨T(v), v⟩= ⟨v, T(v)⟩= ⟨v, λv⟩= ¯λ⟨v, v⟩.
Poiché ⟨v, v⟩> 0, deduciamo che λ = ¯λ e quindi λ ∈R.
Dimostriamo adesso per induzione sulla dimensione n di V che T ha una base ortonormale di
autovettori. Il caso n = 1 è banale: tutti gli endomorﬁsmi di uno spazio di dimensione uno hanno
una base ortonormale di autovettori, formata da un elemento solo di norma uno.
Supponiamo il fatto vero per la dimensione n−1 e lo mostriamo per n. Poiché siamo sui complessi,
esiste sempre un autovettore v ∈V (per il Teorema Fondamentale dell’Algebra). La retta Span(v)
è chiaramente T-invariante e quindi anche lo spazio ortogonale U = Span(v)⊥è T-invariante per
la Proposizione 25.10, cioè vale T(U) ⊂U. La restrizione
T|U : U →U
è un endomorﬁsmo autoaggiunto di uno spazio vettoriale U di dimensione n−1. Per l’ipotesi indut-
tiva, esiste una base v2, . . . , vn ortonormale formata da autovettori per T|U. Aggiungendo il vettore
iniziale v, rinormalizzato in modo che abbia norma uno, otteniamo una base B = {v, v2, . . . , vn}
134

<!-- pagina 135 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
ortonormale formata da autovettori di T.
Abbiamo dimostrato il teorema spettrale nel caso complesso. Come importante conseguenza, noti-
amo che una matrice reale simmetrica S ha sempre tutti gli autovalori reali: infatti l’endomorﬁsmo
LS : Cn →Cn è autoaggiunto (rispetto al prodotto hermitiano euclideo) per la Proposizione 25.6
e quindi LS ha gli autovalori tutti reali e una base ortonormale di autovettori in Cn.
Resta inﬁne da dimostrare il teorema spettrale nel caso reale. Prendiamo una base ortonormale B
di V e poniamo
S = [T]B
B.
La matrice S è reale e simmetrica. Considerandola come matrice complessa, per il caso complesso
appena dimostrato tutti i suoi autovalori sono reali. Quindi il polinomio caratteristico di S ha una
radice λ ∈R. Poiché
det(S −λIn) = 0,
esiste un vettore reale non nullo v tale che Sv = λv. Abbiamo quindi un autovettore reale e
possiamo applicare la stessa dimostrazione per induzione usata nel caso complesso.
Vediamo adesso una versione del teorema spettrale nel caso reale con il linguaggio delle matrici.
Consideriamo lo spazio Rn con l’usuale prodotto scalare euclideo.
Corollario 26.2
Sia A una matrice n × n reale. Sono equivalenti i fatti seguenti:
(1) A è simmetrica;
(2) LA ha una base ortonormale di autovettori;
(3) esiste una matrice ortogonale M tale che
tMAM = M−1AM = D
sia una matrice diagonale.
Spiegazione. L’equivalenza (1) ⇐⇒(2) è il teorema spettrale. Una base ortonormale di autovet-
tori fornisce una matrice ortogonale M le cui colonne sono tali autovettori e per cui M−1AM è
diagonale; viceversa, le colonne di una tale M formano una base ortonormale di autovettori. Inoltre
M−1 = tM.
Collegamento con l’informatica: PCA e riduzione dimensionale
Una delle applicazioni più importanti del teorema spettrale nell’analisi dei dati è la Principal
Component Analysis (PCA). Supponiamo di avere dati centrati x1, . . . , xN ∈Rn e conside-
135

<!-- pagina 136 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
riamo la matrice
S = 1
N
N
X
i=1
xi txi.
La matrice S è simmetrica. Per il teorema spettrale possiede quindi una base ortonormale di
autovettori. Gli autovettori corrispondenti agli autovalori più grandi individuano le direzioni
lungo le quali i dati presentano la maggiore variabilità.
Proiettando i dati sul sottospazio
generato da poche di queste direzioni si ottiene una rappresentazione in dimensione più bassa
che conserva una parte importante dell’informazione. Questo è il principio matematico della
PCA.
26.B
Esercizi
Esercizio 26.3
Veriﬁca che la matrice A ha una base ortonormale di autovettori mentre la matrice B no:
A =
 3
1
1
1

,
B =
 3
1
0
1

.
Soluzione: Ovviamente A è simmetrica mentre B no, allora secondo il corollario sopra A ha una
base ortonormale di autovettori, invece B no. Vogliamo però veriﬁcare questo fatto adesso senza
usare il teorema spettrale.
Per A otteniamo autovalori λ1,2 = 2 ±
√
2 con autovettori v1,2 =

1 ±
√
2
1

. Notiamo che
⟨v1, v2⟩= 0, cioè i vettori sono ortogonali e dopo una normalizzazione diventano ortonormali.
Per B invece abbiamo autovalori λ1 = 3, λ2 = 1 con autovettori v1 =
 1
0

e v2 =
 −1
2

.
Notiamo che ⟨v1, v2⟩= −1, allora gli autovettori non sono ortogonali, cioè formano un angolo ϑ
diverso da π/2. Ogni autovettore con autovalore λ1 è un multiplo di v1 e ogni autovettore con
autovalore λ2 è un multiplo di v2 e allora ogni coppia di autovettori forma un angolo ϑ o π −ϑ.
In particolare è impossibile scegliere autovettori ortonormali.
Esercizio 26.4
Trovare una base ortonormale di autovettori per la matrice
A =


1
0
1
0
2
0
1
0
1

.
Soluzione: A è simmetrica, allora esiste una base ortonormale di autovettori.
136

<!-- pagina 137 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
pA(λ) = det(A −λI3) = det


1 −λ
0
1
0
2 −λ
0
1
0
1 −λ


= (2 −λ) det
 1 −λ
1
1
1 −λ

= (2 −λ)[(1 −λ)2 −1
|
{z
}
=λ2−2λ
]
= −λ(2 −λ)2
Troviamo allora λ1 = 0 con molteplicità algebrica = molteplicità geometrica = 1 e λ2 = 2 con
molteplicità algebrica = molteplicità geometrica = 2 (perché sappiamo già che A è diagonalizz-
abile).
(λ1I3 −A) x = 0 ⇔−Ax = 0 ⇔Ax = 0 ⇔


1
0
1
0
2
0
1
0
1




x1
x2
x3

=


0
0
0

,
Vλ1 = Span





1
0
−1




.
(λ2I3 −A) x = 0 ⇔


1
0
−1
0
0
0
−1
0
1




x1
x2
x3

=


0
0
0


Vλ2 = Span





1
0
1

,


0
1
0





Notiamo che i vettori nella deﬁnizione di Vλ2 sono già ortogonali (dobbiamo sceglierli in questo
modo o alternativamente usare l’algoritmo di Gram-Schmidt!). Invece l’autovettore in Vλ1 è sempre
automaticamente ortogonale a tutti i vettori in Vλ2.
Abbiamo allora una base {v1, v2, v3} di
autovettori ortogonali (ma non ancora ortonormali). Possiamo normalizzare v1, v2 :
w1 =
v1
p
⟨v1, v1⟩
= v1
√
2 =


1/
√
2
0
−1/
√
2

=


√
2/2
0
−
√
2/2


w2 =
v2
p
⟨v2, v2⟩
= v2
√
2 =


1/
√
2
0
1/
√
2

=


√
2/2
0
√
2/2


w3 = v3 =


0
1
0


Una base ortonormale di autovettori di A è data da {w1, w2, w3}.
137

<!-- pagina 138 -->
MDAG Parte II: Algebra Lineare e Geometria
Buzano e Radeschi
Esercizio 26.5
Calcolare la diagonalizzazione della seguente matrice:
A =


2
i
i
−i
1
0
−i
0
1

.
Soluzione: A è hermitiana, allora esiste una base ortonormale di autovettori. Troviamo che gli
autovalori sono λ1 = 0, λ2 = 1, λ3 = 3, ciascuno con molteplicità algebrica 1. Risolvendo i sistemi
lineari, troviamo gli autospazi Vk = Span(vk) con
v1 =


1
i
i

,
v2 =


0
1
−1

,
v3 =


2i
1
1

.
Notiamo che questi autovettori sono già ortogonali, dobbiamo solo normalizzarli. Troviamo poi
Λ = W −1AW con
W =


√
3/3
0
i
√
6/3
√
3i/3
√
2/2
√
6/6
√
3i/3
−
√
2/2
√
6/6

.
Notiamo anche che tW · W = I3 e allora W −1 = tW.
138
