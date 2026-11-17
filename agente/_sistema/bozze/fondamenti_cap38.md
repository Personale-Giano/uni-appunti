# 38. Altri Esempi di Induzione: Somma Geometrica, Divisibilità, Sottoinsiemi e Triomini
## Lo schema è sempre lo stesso
Il cap. 37 ha dato il principio di induzione e i primi esempi su somme e disuguaglianze. La sezione 2.4 del libro prosegue con quattro esempi molto diversi tra loro: una somma con un punto di partenza diverso da 1, una divisibilità, un conteggio di sottoinsiemi e un problema di tassellazione. Lo schema non cambia mai: passo base sul valore più piccolo, poi passo induttivo che collega il caso n al caso n + 1. Del gruppo, nella registrazione 2025 il docente svolge a lezione solo la tassellazione; gli altri tre sono del libro.

## La somma geometrica
**Definizione.** Una **somma geometrica** è una somma della forma a + ar + ar² + … + arⁿ.

(In parole povere: ogni termine si ottiene dal precedente moltiplicando per lo stesso numero r. Se a ≠ 0 e r ≠ 0 il rapporto tra due termini vicini, ar^{i+1}/arⁱ, vale sempre r. Esempio: 3 + 6 + 12 + 24 ha a = 3 e r = 2.)

**Proposizione.** Se r ≠ 1, per ogni n ≥ 0 vale a + ar + ar² + … + arⁿ = a(r^{n+1} − 1)/(r − 1).

(In parole povere: non serve sommare i termini uno per uno, c'è una formula chiusa. Per 3 + 6 + 12 + 24 (n = 3) dà 3 · (2⁴ − 1)/(2 − 1) = 3 · 15 = 45, e infatti 3 + 6 + 12 + 24 = 45.)

**Dimostrazione.** Qui il dominio è {n | n ≥ 0}, quindi il passo base è n = 0 (cap. 37, base diversa da 1).

1. **Passo base (n = 0).** A sinistra c'è il solo termine a; a destra a(r¹ − 1)/(r − 1) = a. Uguali.
2. **Passo induttivo.** Si suppone la formula vera per n e si aggiunge il termine successivo ar^{n+1}, scritto con lo stesso denominatore:
   a + … + arⁿ + ar^{n+1} = a(r^{n+1} − 1)/(r − 1) + ar^{n+1}(r − 1)/(r − 1) = (ar^{n+1} − a + ar^{n+2} − ar^{n+1})/(r − 1) = a(r^{n+2} − 1)/(r − 1),
   che è la formula con n + 1 al posto di n.

**Il caso a = 1, r = 2.** Con a = 1 e r = 2 si ottiene 1 + 2 + 2² + … + 2ⁿ = (2^{n+1} − 1)/(2 − 1) = 2^{n+1} − 1. Per esempio 1 + 2 + 4 + 8 = 15 = 2⁴ − 1. In binario (cap. 7) è un fatto familiare: il numero formato da n + 1 cifre tutte uguali a 1 vale 2^{n+1} − 1, cioè uno in meno di 1 seguito da n + 1 zeri.

## Una divisibilità: 5ⁿ − 1 è multiplo di 4
**Proposizione.** Per ogni n ≥ 1, 5ⁿ − 1 è divisibile per 4.

(In parole povere: togliendo 1 a una potenza di 5 si ottiene sempre un multiplo di 4. Per esempio 5 − 1 = 4, 25 − 1 = 24 = 4 · 6, 125 − 1 = 124 = 4 · 31.)

Si usa un fatto che il libro lascia per esercizio: se p e q sono divisibili per k, anche p + q lo è (se p = k · a e q = k · b, allora p + q = k(a + b)).

**Dimostrazione.**

1. **Passo base (n = 1).** 5¹ − 1 = 4, divisibile per 4.
2. **Passo induttivo.** Si suppone 5ⁿ − 1 divisibile per 4. Il libro mostra come si trova la strada: si scrive 5^{n+1} − 1 come (5ⁿ − 1) più un pezzo «da determinare»; se anche quel pezzo è multiplo di 4, la somma lo è. Poiché 5^{n+1} − 1 = 5 · 5ⁿ − 1 = 4 · 5ⁿ + 5ⁿ − 1, il pezzo cercato è 4 · 5ⁿ. Quindi 5^{n+1} − 1 = (5ⁿ − 1) + 4 · 5ⁿ è somma di due multipli di 4: il primo per ipotesi induttiva, il secondo perché contiene il fattore 4.

Anche qui il passo induttivo consiste nel ritrovare il caso n dentro il caso n + 1: è lo stesso trucco di Sₙ₊₁ = Sₙ + (n + 1) nel cap. 37.

## Quanti sono i sottoinsiemi di un insieme
**Definizione.** L'**insieme potenza** P(X) di un insieme X è l'insieme di tutti i sottoinsiemi di X.

(In parole povere: è l'elenco di tutti i modi di scegliere alcuni elementi di X, compresi «nessuno» e «tutti». Per X = {a, b} è P(X) = {∅, {a}, {b}, {a, b}}.)

**Teorema.** Se X ha n elementi, P(X) ha 2ⁿ elementi, per ogni n ≥ 0.

(In parole povere: un insieme di n elementi ha 2ⁿ sottoinsiemi. Per X = {a, b} sono quattro: ∅, {a}, {b}, {a, b}, e 2² = 4.)

**Dimostrazione.** Per induzione su n.

1. **Passo base (n = 0).** X è vuoto, e il suo unico sottoinsieme è ∅. Quindi |P(X)| = 1 = 2⁰.
2. **Passo induttivo.** Si suppone che ogni insieme con n elementi abbia 2ⁿ sottoinsiemi, e si prende X con n + 1 elementi. Si sceglie un elemento x ∈ X. I sottoinsiemi di X si dividono in due gruppi della stessa grandezza: quelli che contengono x e quelli che non lo contengono. Infatti ogni sottoinsieme S che contiene x si accoppia con un solo sottoinsieme che non lo contiene, S senza x, e viceversa. Sia Y l'insieme X senza x: ha n elementi, quindi per ipotesi induttiva |P(Y)| = 2ⁿ. Ma i sottoinsiemi di Y sono esattamente i sottoinsiemi di X che non contengono x, cioè metà di tutti. Quindi |P(X)| = 2 · |P(Y)| = 2 · 2ⁿ = 2^{n+1}.

Con X = {a, b, c} e x = a, il libro mostra l'accoppiamento: {a} con ∅, {a, b} con {b}, {a, c} con {c}, {a, b, c} con {b, c}. Sono 4 + 4 = 8 = 2³ sottoinsiemi.

## Il problema dei triomini
**Definizione.** Un **triomino** (destro) è una figura formata da tre quadrati uniti per i lati a forma di L. Più in generale, un **polimino di ordine s** è formato da s quadrati uniti per i lati. **Tassellare** una figura con i triomini vuol dire coprirla esattamente, senza sovrapposizioni e senza sporgere. Una **scacchiera deficiente** è una scacchiera quadrata a cui manca un quadrato.

(In parole povere: il triomino è il pezzo a L del Tetris, ma fatto di tre quadratini invece che di quattro. Tassellare è come piastrellare un pavimento senza tagliare né sovrapporre le piastrelle; la scacchiera deficiente è un pavimento con un quadratino già occupato, per esempio da una colonna.)

I polimini sono stati introdotti da Solomon Golomb nel 1954 e sono diventati un classico della matematica ricreativa; gli unici polimini di ordine 3 sono il triomino e tre quadrati in fila. Il libro cita Golomb proprio per i polimini e presenta il risultato seguente come la sua prova induttiva; il nome «teorema di Golomb» è usato qui per comodità.

**Perché ci vuole il buco (registrazione 2025).** Il docente parte dalla domanda più naturale: si può tassellare una scacchiera 2 × 2, 4 × 4, 8 × 8 con i triomini? No, e per un motivo di area: ogni triomino copre 3 quadrati, mentre 4, 16, 64 non sono divisibili per 3. Il meglio che si può sperare è coprire tutto lasciando un solo quadrato libero. Per esempio una 4 × 4 deficiente si copre con 5 triomini, perché 5 · 3 = 15 = 16 − 1. A lezione mostra che il buco si può spostare negli angoli ruotando e ribaltando i triomini, e si chiede se si possa mettere **ovunque**: per rispondere in generale serve un ragionamento.

**Teorema (Golomb).** Per ogni k ≥ 1, ogni scacchiera deficiente 2ᵏ × 2ᵏ si può tassellare con triomini, qualunque sia il quadrato mancante.

(In parole povere: su una scacchiera di lato 2, 4, 8, 16, … si può scegliere a piacere la casella da lasciare vuota, e il resto si riempie sempre con pezzi a L.)

**Dimostrazione.** Per induzione su k.

1. **Passo base (k = 1).** Una 2 × 2 deficiente è essa stessa un triomino: basta ruotarlo per lasciare libero il quadrato voluto.
2. **Passo induttivo.** Si suppone di saper tassellare ogni 2ᵏ × 2ᵏ deficiente, comunque sia messo il buco, e si prende una 2^{k+1} × 2^{k+1} deficiente.
   - La si divide in quattro quadranti 2ᵏ × 2ᵏ. Il quadrato mancante sta in uno di essi, che quindi è una 2ᵏ × 2ᵏ deficiente e si tassella per ipotesi induttiva.
   - Gli altri tre quadranti sono completi. Si mette un triomino T al centro della scacchiera, girato in modo da coprire un quadrato di ciascuno di questi tre quadranti, proprio nei loro angoli che si toccano al centro.
   - Considerando «mancanti» i quadrati coperti da T, ognuno dei tre quadranti diventa una 2ᵏ × 2ᵏ deficiente, che si tassella per ipotesi induttiva.

   Le quattro tassellazioni più T coprono tutta la scacchiera tranne il buco scelto.

![A sinistra una 4 × 4 deficiente tassellata con 5 triomini; a destra una 8 × 8 deficiente divisa in quattro quadranti, con il triomino centrale in arancione.](figure/fond/induzione_golomb.png|14)

**Come lo racconta il docente (registrazione 2025).** Riempiendo i quattro quadranti per ipotesi induttiva restano **quattro** buchi, uno per quadrante; il problema è farne sparire tre, perché tre quadrati sono esattamente un triomino. Ma stanno in scacchiere diverse: la soluzione è scegliere i tre buchi dei quadranti completi tutti attaccati alla croce centrale, così un solo triomino li copre. Nota anche che il libro chiama k l'esponente mentre lui a lezione usa n: sono variabili locali, il nome non conta.

**Una prova che è anche un metodo.** Per il docente il punto più interessante è che questa prova è **costruttiva**: non dice solo che la tassellazione esiste, dice come trovarla. Descritta così, diventa direttamente un programma ricorsivo (si tassella la scacchiera grande tassellando le quattro piccole), e il programma è garantito dalla prova. Problemi di questo tipo non sono solo giochi: il libro cita il **problema del layout VLSI** (very large scale integration), cioè disporre i componenti di un chip nel rettangolo di area minima, con componenti modellati come rettangoli e figure a L, più vincoli come la vicinanza dei componenti collegati tra loro.

**Per curiosità (dal libro).** Se una scacchiera n × n deficiente si tassella, 3 deve dividere n² − 1. Chu ha dimostrato che il viceversa vale per ogni n ≠ 5: per n ≠ 5, una n × n deficiente si tassella con triomini se e solo se 3 divide n² − 1. Alcune 5 × 5 deficienti si tassellano e altre no, a seconda di dove sta il buco.

Nel cap. 42 si torna ai triomini con l'esercizio 39 del libro, che tassella una figura a L e dà una seconda prova del teorema di Golomb. Prima, però, l'uso dell'induzione che interessa di più a un informatico: gli invarianti di ciclo.
