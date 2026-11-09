# 46. Le Applicazioni Lineari: Definizione ed Esempi
## Funzioni che rispettano la struttura
Finora gli spazi vettoriali sono stati studiati uno alla volta. Il passo successivo è studiare le **funzioni tra spazi vettoriali** che rispettano le due operazioni, somma e prodotto per scalare. Sono le mappe lineari annunciate fin dal cap. 1. A lezione (registrazione 2024) il docente le presenta come il concetto fondamentale del corso: sono «il modo in cui gli spazi vettoriali comunicano tra di loro».

**Definizione.** Siano V e W due spazi vettoriali sullo stesso campo 𝕂. Un'**applicazione lineare** è una funzione f : V → W tale che:
- (i) f(v + w) = f(v) + f(w) per ogni v, w ∈ V;
- (ii) f(λv) = λf(v) per ogni v ∈ V e λ ∈ 𝕂.

(In parole povere: è indifferente fare prima le operazioni e poi applicare f, oppure applicare f e poi fare le operazioni. Sommare due vettori e trasformare il risultato dà lo stesso che trasformarli e poi sommarli.)

**Sinonimi e lettura delle condizioni (registrazione 2024).** Alla lavagna sono scritti insieme tre nomi equivalenti: **applicazione**, **mappa** o **trasformazione lineare**. Il docente fa notare che nelle due condizioni le operazioni non sono le stesse ai due lati dell'uguale: in f(v + w) la somma è quella di V, mentre in f(v) + f(w) è quella di W, perché f(v) e f(w) sono già vettori di W. Lo stesso vale per il prodotto per scalare. Alla lavagna lo segnala con un pedice: f(v_{1} +_{V} v_{2}) = f(v_{1}) +_{W} f(v_{2}).

## Un'unica condizione al posto di due
**Osservazione (registrazione 2024).** Le due condizioni della definizione equivalgono a un'unica condizione (qui lo scalare si chiama a, come alla lavagna):

f(v_{1} + a·v_{2}) = f(v_{1}) + a·f(v_{2}) per ogni v_{1}, v_{2} ∈ V e ogni a ∈ 𝕂.

Il docente dice che per verificare la linearità «avrete la scelta» fra controllare le due proprietà oppure soltanto questa. Che una funzione lineare la soddisfi segue subito da (i) e (ii). Il viceversa non è dimostrato a lezione: con v_{1} = v_{2} = 0 e a = 1 si ottiene f(0) = 2f(0), cioè f(0) = 0; poi con a = 1 si ritrova (i) e con v_{1} = 0 si ritrova (ii).

(In parole povere: invece di fare due verifiche, una per la somma e una per i multipli, se ne fa una sola che le contiene entrambe. È un po' più lunga da scrivere, ma si scrive una volta sola.)

## Due conseguenze immediate
**L'origine va nell'origine.** Usando (ii) con λ = 0 si ottiene f(0) = f(0 · 0) = 0 · f(0) = 0. Qui lo zero compare in tre ruoli diversi: il vettore nullo di V, il vettore nullo di W e lo zero del campo 𝕂. Un'applicazione lineare manda quindi sempre l'origine di V nell'origine di W, e questo dà un controllo rapidissimo: se f(0) ≠ 0, f non è lineare.

**Come sottolineato a lezione (registrazione 2024).** Il controllo dell'origine **non è un se e solo se**: una funzione che manda lo zero nello zero non è necessariamente lineare. Il docente consiglia comunque di farlo sempre per primo, perché è velocissimo: se l'origine non va nell'origine si ha subito la risposta, altrimenti «alla peggio» si è perso un po' di tempo.

**Le combinazioni lineari si conservano.** Se v = λ_{1}v_{1} + … + λ_{k}v_{k}, applicando più volte (i) e (ii):

f(v) = f(λ_{1}v_{1}) + … + f(λ_{k}v_{k}) = λ_{1}f(v_{1}) + … + λ_{k}f(v_{k}).

Un'applicazione lineare manda una combinazione lineare di vettori nella combinazione lineare **con gli stessi coefficienti** delle loro immagini.

## Esempi in ℝ²
Negli esempi seguenti 𝕂 = ℝ e V = W = ℝ², con i vettori scritti in colonna.

**Esempio (lineare).** Sia T(a, b) = (2a + b, a + 3b). Presi v = (a_{1}, b_{1}), w = (a_{2}, b_{2}) e λ ∈ ℝ:

T(v + w) = (2(a_{1} + a_{2}) + (b_{1} + b_{2}), (a_{1} + a_{2}) + 3(b_{1} + b_{2})) = (2a_{1} + b_{1}, a_{1} + 3b_{1}) + (2a_{2} + b_{2}, a_{2} + 3b_{2}) = T(v) + T(w),

T(λv) = (2λa_{1} + λb_{1}, λa_{1} + 3λb_{1}) = λ(2a_{1} + b_{1}, a_{1} + 3b_{1}) = λT(v).

Valgono entrambe le condizioni, quindi T è lineare.

**Esempio dalla lavagna (registrazione 2024), con la condizione unica.** Sia T : ℝ² → ℝ², T(x, y) = (3x + 2y, x). Presi (x, y), (x′, y′) ∈ ℝ² e a ∈ ℝ, si calcolano separatamente il lato sinistro L e il lato destro R di T((x, y) + a(x′, y′)) = T(x, y) + aT(x′, y′):

L = T(x + ax′, y + ay′) = (3(x + ax′) + 2(y + ay′), x + ax′) = (3x + 3ax′ + 2y + 2ay′, x + ax′),

R = (3x + 2y, x) + a(3x′ + 2y′, x′) = (3x + 2y + 3ax′ + 2ay′, x + ax′).

I due vettori coincidono, quindi T è lineare. Il docente avverte che in mezzo ai conti è facile perdersi, e indica che cosa ha reso lineare questa mappa: **ogni componente è una combinazione lineare di x e y**, un polinomio di grado 1 in x e y (cioè senza termine noto, altrimenti si ricade nell'esempio con il +1). Allo stesso modo una funzione da ℝ³ in ℝ³ con tutte le componenti combinazioni lineari di x, y e z è lineare.

**Esempio (non lineare, origine).** Sia T(a, b) = (a + 2, a + b − 1). Allora T(0, 0) = (2, −1) ≠ (0, 0), quindi T non è lineare. Le costanti aggiunte, il +2 e il −1, spostano l'origine.

**Esempio (non lineare, quadrato).** Sia T(a, b) = (a², a + b). Qui T(0, 0) = (0, 0), quindi il controllo sull'origine non basta. Con v = (2, 1) e w = (2, 0) si ha T(v + w) = T(4, 1) = (16, 5), mentre T(v) + T(w) = (4, 3) + (4, 2) = (8, 5). Poiché (16, 5) ≠ (8, 5), T non è lineare.

(In parole povere: la prova dell'origine scarta subito molte funzioni, ma passarla non basta. Per dimostrare che una funzione non è lineare serve un controesempio concreto.)

**Non esempi dalla lavagna (registrazione 2024).** Il docente ne mostra due, scegliendo ogni volta la verifica più comoda.
- f(x, y) = (x + 1, y²). Si ha f(0, 0) = (1, 0) ≠ (0, 0), quindi f non è lineare. Il «colpevole» è il +1: se compare un termine noto, la funzione non è lineare. Il criterio esatto è f(0) ≠ 0: un termine noto non nullo fa proprio questo, perché sposta l'immagine dell'origine.
- f(x, y) = (x, y²). Qui f(0, 0) = (0, 0), e il controllo dell'origine «non ci sta dicendo niente». Si usa allora la condizione (ii): f(a(x, y)) = f(ax, ay) = (ax, a²y²), mentre af(x, y) = (ax, ay²). Le seconde componenti sono diverse: con a = 2 si ottiene 4y² da una parte e 2y² dall'altra, e basta prendere y ≠ 0, per esempio (x, y) = (0, 1), che dà (0, 4) ≠ (0, 2). Qui il colpevole è il quadrato.

## Esempi che valgono in ogni spazio
**La funzione nulla** f : V → W, con f(v) = 0 per ogni v, è lineare: entrambe le condizioni diventano 0 = 0. A lezione (registrazione 2024) è chiamata **mappa nulla**.

**L'identità** id : V → V, con id(v) = v per ogni v, è lineare: le condizioni sono ovvie. Alla lavagna (registrazione 2024) è scritta anche id_{V} o I_{V}.

## L'esempio più importante: la moltiplicazione per una matrice
Sia A = (a_{ij}) una matrice m × n. Si definisce L_{A} : 𝕂ⁿ → 𝕂^{m} come L_{A}(x) = Ax, il prodotto riga per colonna del cap. 29:

L_{A}(x_{1}, …, x_{n}) = (a_{11}x_{1} + … + a_{1n}x_{n}, …, a_{m1}x_{1} + … + a_{mn}x_{n}).

La L sta per «left», perché si moltiplica a sinistra per A. La linearità discende dalle proprietà del prodotto di matrici: L_{A}(x + x′) = A(x + x′) = Ax + Ax′ = L_{A}(x) + L_{A}(x′) e L_{A}(λx) = A(λx) = λAx = λL_{A}(x).

**Alla lavagna (registrazione 2024)** la verifica è fatta in una riga sola con la condizione unica: L_{A}(x + ax′) = A(x + ax′) = Ax + A(ax′) = Ax + aAx′ = L_{A}(x) + aL_{A}(x′). Il primo passaggio usa la distributività del prodotto di matrici rispetto alla somma, il secondo il fatto che lo scalare si può portare fuori dal prodotto (il prodotto di matrici non è commutativo, ma il prodotto per scalare sì). Il docente fa notare anche le taglie: x è una matrice n × 1, il numero di colonne di A è uguale al numero di righe di x, e Ax è una matrice m × 1, cioè un vettore di 𝕂^{m}.

**Esempio.** Con A = ( 2 1 ; 1 3 ) si ottiene L_{A}(a, b) = (2a + b, a + 3b): è esattamente la prima funzione degli esempi in ℝ².

**Esempi dalla lavagna (registrazione 2024).**
- A = ( 1 0 2 ; 1 2 4 ) ∈ M(2, 3, ℝ) dà L_{A} : ℝ³ → ℝ²: ℝ³ perché A ha 3 colonne, ℝ² perché ha 2 righe. Riga per colonna, L_{A}(x, y, z) = (x + 2z, x + 2y + 4z); per esempio L_{A}(1, 1, 1) = (3, 7).
- A = ( 3 2 ; 1 0 ) dà L_{A}(x, y) = (3x + 2y, x): è proprio la funzione T dell'esempio dalla lavagna. I coefficienti di x e y in ogni componente sono esattamente le righe della matrice.

(In parole povere: ogni matrice m × n è una macchina che trasforma vettori con n componenti in vettori con m componenti, e lo fa sempre in modo lineare.)

**Anticipazione (registrazione 2024).** Il docente lo chiama «foreshadowing»: non si tratta di una classe speciale di funzioni, perché **ogni** applicazione lineare da ℝⁿ a ℝ^{m} si può scrivere come moltiplicazione per una matrice. Parlare di funzioni lineari da ℝⁿ a ℝ^{m} o di matrici m × n sarà quindi «la stessa cosa». In questa lezione è solo annunciato, non dimostrato.

**Collegamento con l'informatica: le reti neurali.** Una delle operazioni fondamentali di una rete neurale è la moltiplicazione matrice-vettore. Uno strato usa di solito una trasformazione x ↦ Ax + b, dove le entrate di A e di b sono parametri che cambiano durante l'addestramento. La parte x ↦ Ax è proprio L_{A}. Se b ≠ 0, invece, x ↦ Ax + b non è lineare ma **affine**, per lo stesso motivo dell'esempio non lineare con le costanti +2 e −1: sposta l'origine. Gli strati alternano trasformazioni di questo tipo con operazioni non lineari. Per questo matrici e applicazioni lineari sono il linguaggio di base di molti modelli di machine learning.

## La traccia
**Esempio.** La traccia tr : M(n, 𝕂) → 𝕂 (cap. 30) è lineare. La diagonale di A + B è fatta di a_{11} + b_{11}, …, a_{nn} + b_{nn}, quindi

tr(A + B) = (a_{11} + b_{11}) + … + (a_{nn} + b_{nn}) = tr(A) + tr(B),

e allo stesso modo tr(λA) = λa_{11} + … + λa_{nn} = λ tr(A). È un esempio in cui gli spazi di partenza e di arrivo sono diversi: matrici in partenza, numeri in arrivo.

## La derivata
**Esempio dalla lavagna (registrazione 2024).** Indichiamo con 𝕂[x]_{d} i polinomi di grado al massimo d. La **derivata** è la funzione D : 𝕂[x]_{d} → 𝕂[x]_{d−1} definita da

D(a_{d}x^{d} + … + a_{2}x² + a_{1}x + a_{0}) = d·a_{d}x^{d−1} + … + 2a_{2}x + a_{1}.

Ogni potenza x^{k} diventa k·x^{k−1}: il docente la descrive come se «prendesse un d da qua e lo spostasse al coefficiente», lasciando k − 1 come esponente; la derivata di x è 1 e quella di una costante è 0. Per chi non l'ha mai vista, a lezione si dice di prendere questa come definizione (la derivata si studia ad Analisi). Le due proprietà note della derivata, D(p_{1}(x) + p_{2}(x)) = D(p_{1}(x)) + D(p_{2}(x)) e D(λp(x)) = λD(p(x)), sono esattamente le due condizioni della definizione: **D è lineare**. Per esempio D(x³ + 2x) = 3x² + 2.

**Verifica (aggiunta, non svolta a lezione).** Se p = a_{d}x^{d} + … + a_{0} e q = b_{d}x^{d} + … + b_{0}, il coefficiente di x^{k−1} in D(p + q) è k(a_{k} + b_{k}) = ka_{k} + kb_{k}, cioè la somma dei coefficienti di x^{k−1} in D(p) e in D(q): quindi D(p + q) = D(p) + D(q). Allo stesso modo il coefficiente di x^{k−1} in D(λp) è k(λa_{k}) = λ(ka_{k}), quindi D(λp) = λD(p).

(In parole povere: derivare una somma è come sommare le derivate, e una costante davanti resta davanti. Quindi derivare è un'operazione lineare sui polinomi.)

Il prossimo capitolo associa a ogni applicazione lineare due sottospazi, il nucleo e l'immagine.
