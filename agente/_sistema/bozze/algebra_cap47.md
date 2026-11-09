# 47. Nucleo e Immagine di un'Applicazione Lineare
## Due insiemi associati a f
**Definizione.** Sia f : V → W un'applicazione lineare. Il **nucleo** di f è il sottoinsieme di V

Ker f = {v ∈ V | f(v) = 0},

e l'**immagine** di f è il sottoinsieme di W

Im f = {w ∈ W | esiste v ∈ V con f(v) = w}.

(In parole povere: il nucleo raccoglie i vettori che f «schiaccia» sullo zero; l'immagine raccoglie tutti i vettori che f riesce a raggiungere. Il primo vive nello spazio di partenza, il secondo in quello di arrivo.)

**A lezione (registrazione 2024).** Il simbolo Ker viene dall'inglese «kernel», che vuol dire nucleo; il docente descrive il nucleo come l'insieme dei vettori che «vengono uccisi» da f. L'immagine è la stessa nozione già vista a Matematica discreta per funzioni qualsiasi: alla lavagna Im f = {w ∈ W | w = f(v) per un qualche v ∈ V}.

**Esempio.** Per L_{A}(a, b) = (a + b, 2a + 2b), cioè A = ( 1 1 ; 2 2 ), il nucleo è dato da a + b = 0, cioè dai vettori t(1, −1). L'immagine è fatta dai vettori (s, 2s), con s = a + b: è la retta generata da (1, 2).

## Sono sottospazi
**Proposizione.** Il nucleo Ker f è un sottospazio vettoriale di V e l'immagine Im f è un sottospazio vettoriale di W.

(In parole povere: non sono insiemi qualsiasi. Contengono lo zero e restano chiusi rispetto a somme e multipli, quindi hanno una dimensione e delle basi.)

**Dimostrazione.** Si verificano le tre condizioni di sottospazio (cap. 20).

Per il nucleo:
1. 0 ∈ Ker f, perché f(0) = 0 (cap. 46).
2. Se v, w ∈ Ker f, allora f(v + w) = f(v) + f(w) = 0 + 0 = 0, quindi v + w ∈ Ker f.
3. Se v ∈ Ker f e λ ∈ 𝕂, allora f(λv) = λf(v) = λ0 = 0, quindi λv ∈ Ker f.

Per l'immagine:
1. 0 ∈ Im f, perché 0 = f(0).
2. Se f(v) e f(v′) stanno in Im f, anche la loro somma ci sta, perché f(v) + f(v′) = f(v + v′).
3. Se f(v) ∈ Im f e λ ∈ 𝕂, allora λf(v) = f(λv) ∈ Im f.

A lezione (registrazione 2024) questa proposizione è solo enunciata, insieme alla successiva, e alla lavagna Ker f e Im f sono detti «sottospazi lineari».

## Nucleo e iniettività
**Proposizione.** Un'applicazione lineare f : V → W è iniettiva se e solo se Ker f = {0}. È suriettiva se e solo se Im f = W.

(In parole povere: per sapere se f è iniettiva basta guardare chi va a finire sullo zero. Se ci va solo lo zero, nessuna coppia di vettori diversi viene mai confusa.)

**Dimostrazione.** La condizione per la suriettività è la definizione stessa di funzione suriettiva. Per l'iniettività:
- (⇒) Si sa già che f(0) = 0. Se f è iniettiva, nessun altro vettore può avere immagine 0, quindi Ker f = {0}.
- (⇐) Siano v ≠ v′. Allora v − v′ ≠ 0 e, poiché il nucleo contiene solo lo zero, f(v) − f(v′) = f(v − v′) ≠ 0. Quindi f(v) ≠ f(v′).

Il punto è che, per una funzione lineare, f(v) = f(v′) equivale a f(v − v′) = 0: confrontare due vettori si riduce a guardare un solo vettore nel nucleo. Per una funzione qualsiasi non è così.

**Come sottolineato a lezione (registrazione 2024).** La condizione per la suriettività «quasi non è neanche tanto una proposizione», ma la definizione stessa, e vale per ogni funzione. Quella per l'iniettività, invece, **vale soltanto per le applicazioni lineari**. A lezione è dimostrata solo questa parte, in forma diretta (registrazione 2024): per (⇒) un v ∈ Ker f ha f(v) = 0_{W} = f(0_{V}), stessa immagine dello zero, quindi v = 0_{V}; per (⇐) si parte da f(v_{1}) = f(v_{2}), si ottiene f(v_{1} − v_{2}) = 0_{W}, quindi v_{1} − v_{2} ∈ Ker f = {0_{V}} e v_{1} = v_{2}.

**Collegamento con l'informatica: le direzioni ammissibili.** Sia x un vettore che deve rispettare un vincolo lineare Ax = b, e ci si voglia spostare da x in una direzione y senza violarlo, cioè considerando x + ty. Poiché A(x + ty) = b + tAy, il vincolo resta valido per ogni t esattamente quando Ay = 0, cioè quando y sta nel nucleo di L_{A}. Il nucleo descrive quindi tutte le direzioni in cui ci si può muovere mantenendo invariati i vincoli di uguaglianza, ed è usato così negli algoritmi di ottimizzazione lineare. È la stessa struttura del cap. 41: le soluzioni di Ax = b sono una soluzione particolare più le soluzioni del sistema omogeneo associato.

## L'immagine è generata dalle immagini dei generatori
**Osservazione.** Se v_{1}, …, v_{n} generano V, allora f(v_{1}), …, f(v_{n}) generano Im f.

Sia infatti w ∈ Im f, cioè w = f(v) per qualche v. Poiché i v_{i} generano V, si può scrivere v = λ_{1}v_{1} + … + λ_{n}v_{n}, e quindi

w = f(λ_{1}v_{1} + … + λ_{n}v_{n}) = λ_{1}f(v_{1}) + … + λ_{n}f(v_{n}) ∈ Span(f(v_{1}), …, f(v_{n})).

Vale per ogni w, quindi Im f = Span(f(v_{1}), …, f(v_{n})).

**Alla lavagna (registrazione 2024)** il passaggio è scritto in forma più generale, per vettori qualsiasi: poiché f manda combinazioni lineari in combinazioni lineari con gli stessi coefficienti (cap. 46), f(Span(v_{1}, …, v_{n})) = Span(f(v_{1}), …, f(v_{n})). Quando v_{1}, …, v_{n} sono generatori, Span(v_{1}, …, v_{n}) = V e l'insieme a sinistra è proprio Im f.

## Il caso delle matrici
Per L_{A} : 𝕂ⁿ → 𝕂^{m}, i vettori della base canonica e_{1}, …, e_{n} generano 𝕂ⁿ, e L_{A}(e_{i}) = Ae_{i} è la i-esima colonna A^{i} di A. Quindi l'immagine è lo **spazio generato dalle colonne**:

Im L_{A} = Span(A^{1}, …, A^{n}),

e per la definizione di rango del cap. 28

**rk(A) = dim Span(A^{1}, …, A^{n}) = dim Im L_{A}.**

(In parole povere: le colonne di A sono le immagini dei vettori e_{1}, …, e_{n}; tutto ciò che L_{A} raggiunge è una loro combinazione. Il rango misura quanto è «grande» lo spazio che A riesce a raggiungere.)

**Perché L_{A}(e_{i}) è la i-esima colonna (registrazione 2024).** Alla lavagna il docente parte da un'osservazione sul prodotto di matrici: se A = (A^{1} | … | A^{n}) e x = (x_{1}, …, x_{n}), allora

L_{A}(x) = Ax = x_{1}A^{1} + x_{2}A^{2} + … + x_{n}A^{n},

cioè Ax è la combinazione lineare delle colonne con i coefficienti dati dalle componenti di x. Se x = e_{i}, che ha 1 al posto i e 0 altrove, restano solo i termini 0·A^{1}, …, 1·A^{i}, …, 0·A^{n}, quindi L_{A}(e_{i}) = A^{i}. (Alla lavagna le colonne sono scritte con il pedice, A_{1}, …, A_{n}, e il rango con rg A.)

**Esempio.** Con A = ( 1 2 ; 3 4 ) e x = (5, 6) si ha Ax = 5(1, 3) + 6(2, 4) = (17, 39), lo stesso risultato del prodotto riga per colonna.

**Come sottolineato a lezione (registrazione 2024).** Il rango di una matrice si può pensare come la dimensione dell'immagine di L_{A}; il docente aggiunge che questo si può generalizzare, chiamando rango di una qualunque applicazione lineare la dimensione della sua immagine.

**Esempio.** Con A = ( 1 1 ; 2 2 ) le due colonne sono uguali, quindi Im L_{A} = Span((1, 2)) e rk(A) = 1, come trovato all'inizio del capitolo.
