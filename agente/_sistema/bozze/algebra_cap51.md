# 51. Calcolare con la Matrice Associata e lo Spazio Hom(V, W)
## L'immagine di un vettore con un prodotto
Una volta nota la matrice associata, l'immagine di qualsiasi vettore si calcola con un prodotto riga per colonna.

**Proposizione.** Sia f : V → W un'applicazione lineare e siano B = {v_{1}, …, v_{n}} e C = {w_{1}, …, w_{m}} basi di V e di W. Per ogni v ∈ V vale

[f(v)]_{C} = [f]^{B}_{C} · [v]_{B}.

(In parole povere: per sapere dove va un vettore basta moltiplicare la matrice per le coordinate del vettore. Il risultato sono le coordinate dell'immagine nella base di arrivo.)

**Dimostrazione.** Se v = λ_{1}v_{1} + … + λ_{n}v_{n}, cioè [v]_{B} = (λ_{1}, …, λ_{n}), per linearità f(v) = λ_{1}f(v_{1}) + … + λ_{n}f(v_{n}). Passando alle coordinate rispetto a C, che sono lineari (cap. 49):

[f(v)]_{C} = λ_{1}[f(v_{1})]_{C} + … + λ_{n}[f(v_{n})]_{C} = λ_{1}A^{1} + … + λ_{n}A^{n} = A · [v]_{B},

dove A = [f]^{B}_{C}: una combinazione delle colonne di A con coefficienti λ_{1}, …, λ_{n} è proprio il prodotto di A per il vettore (λ_{1}, …, λ_{n}) (cap. 47). ∎

A lezione (registrazione 2025) la proposizione è enunciata senza dimostrazione, con la formula riquadrata alla lavagna e l'invito a ricordarla. Il docente la legge come due strade che portano allo stesso risultato: calcolare prima f(v) e poi le sue coordinate in C, oppure calcolare prima le coordinate di v e poi moltiplicarle per la matrice.

## Due esempi
**Esempio dalla lavagna (registrazione 2025).** Sia f : ℝ_{2}[x] → ℝ² un'applicazione lineare di cui **non** si conosce la formula, ma solo la matrice associata nelle basi canoniche B = {1, x, x²} e C = {e_{1}, e_{2}}:

[f]^{B}_{C} = ( 1 1 1 ; 1 −1 1 )

(è la matrice trovata nel cap. 50). Si vuole f(x² + 1), un vettore di ℝ². Per la proposizione [f(x² + 1)]_{C} = [f]^{B}_{C} · [x² + 1]_{B}.

Le coordinate di x² + 1 nella base B sono i numeri a, b, c con x² + 1 = a·1 + b·x + c·x². Confrontando i coefficienti: c = 1 (coefficiente di x²), b = 0 (non c'è il termine in x), a = 1 (termine noto). Quindi [x² + 1]_{B} = (1, 0, 1) e

[f(x² + 1)]_{C} = ( 1 1 1 ; 1 −1 1 ) · (1, 0, 1) = (1 + 0 + 1, 1 − 0 + 1) = (2, 2).

Queste sono le coordinate di f(x² + 1) nella base canonica, quindi f(x² + 1) = 2e_{1} + 2e_{2} = (2, 2): nella base canonica il vettore delle coordinate coincide con il vettore stesso. Controllo con la funzione del cap. 50, f(p) = (p(1), p(−1)): f(x² + 1) = (1 + 1, 1 + 1) = (2, 2). Alla lavagna era scappato «c·x³» al posto di c·x², corretto su segnalazione di uno studente.

**Esempio.** Con [f]^{B}_{C} = ( 1 2 4 ; 1 −2 4 ), la matrice della funzione f(p) = (p(2), p(−2)) del cap. 50, si calcola l'immagine di p(x) = 3x² + 5x + 1. Rispetto a B = {1, x, x²} le coordinate sono i coefficienti in ordine di grado crescente, (1, 5, 3). Quindi

[f(p)]_{C} = ( 1 2 4 ; 1 −2 4 ) · (1, 5, 3) = (1 + 10 + 12, 1 − 10 + 12) = (23, 3).

Controllo con la definizione: p(2) = 12 + 10 + 1 = 23 e p(−2) = 12 − 10 + 1 = 3.

## Teoria e calcoli
**Osservazione.** Se si scrive x = [v]_{B}, y = [f(v)]_{C} e A = [f]^{B}_{C}, la proposizione dice y = Ax = L_{A}(x). Una volta scelte le basi, quindi, ogni applicazione lineare V → W si legge in coordinate come una L_{A} : 𝕂ⁿ → 𝕂^{m}: basta sostituire i vettori con le loro coordinate e usare la matrice associata.

![Fissate le basi, l'applicazione f tra spazi astratti (sopra) diventa, in coordinate, la moltiplicazione per la matrice associata A (sotto).](figure/alg/teoria_calcoli.png|11)

**Alla lavagna (registrazione 2025)** il docente riassume la lezione con questo disegno. Sopra la linea ondulata c'è l'universo **teorico**, dove vivono gli spazi vettoriali, anche molto astratti; sotto c'è il mondo pratico **dei calcoli** e delle macchine. Una base di V (dim V = n) trasforma i vettori astratti in vettori di 𝕂ⁿ, cioè in array di n numeri; una base di W (dim W = m) fa lo stesso con 𝕂^{m}; e l'applicazione lineare f diventa L_{A}, con A = [f]^{B}_{C}. In sintesi: i vettori diventano array di numeri e le applicazioni lineari diventano matrici. Il docente insiste che bisogna abituarsi a pensare le matrici come applicazioni lineari, che prendono un vettore e lo trasformano in un altro moltiplicandolo per la matrice.

Come illustrazione (non nelle dispense), cita la teoria dei segnali: lo spazio V delle funzioni f : ℝ → ℝ periodiche di periodo 1, cioè con f(t + 1) = f(t), e trasformazioni come T(f)(t) = ∫_{0}^{1} K(t, s) f(s) ds. Comunicare oggetti del genere a un computer non è facile, ma se si fissa una base si traducono in stringhe di numeri e la trasformazione in una moltiplicazione per una matrice. Lo spazio delle funzioni periodiche non ha dimensione finita, e a lezione l'esempio resta solo un'idea, senza dettagli.

## La matrice dell'identità
Un caso utile in seguito.

**Proposizione.** Sia V uno spazio di dimensione n e sia I_{V} : V → V l'identità. Per ogni base B di V vale [I_{V}]^{B}_{B} = I_{n} ∈ M(n, n, 𝕂).

(In parole povere: se in partenza e in arrivo si usa la stessa base, la funzione che non cambia nulla ha come matrice la matrice identità.)

Infatti I_{V}(v_{j}) = v_{j} = 0·v_{1} + … + 1·v_{j} + … + 0·v_{n} ha coordinate e_{j}, quindi la j-esima colonna è e_{j}. Attenzione: serve la **stessa** base in partenza e in arrivo. Come sottolineato a lezione (registrazione 2025), questo fatto sarà particolarmente importante parlando di composizione di funzioni.

## Lo spazio delle applicazioni lineari
**Definizione.** Dati due spazi vettoriali V e W su 𝕂, si indica con **Hom(V, W)** l'insieme delle applicazioni lineari da V a W:

Hom(V, W) = {f : V → W | f lineare}.

(In parole povere: Hom(V, W) è il «contenitore» di tutte le funzioni lineari da V a W. I suoi elementi non sono vettori nel senso solito, ma funzioni.)

Il nome Hom(V, W) è quello scritto alla lavagna (registrazione 2025); le dispense parlano solo di «insieme delle applicazioni lineari tra V e W». Date f, g ∈ Hom(V, W) e λ ∈ 𝕂, la somma e il multiplo si definiscono punto per punto:

(f + g)(v) = f(v) + g(v),   (λf)(v) = λf(v).

**Proposizione.** Se f, g ∈ Hom(V, W) e λ ∈ 𝕂, allora f + g e λf sono ancora lineari, cioè stanno in Hom(V, W). Con queste due operazioni Hom(V, W) è uno spazio vettoriale.

(In parole povere: le funzioni lineari si possono sommare e moltiplicare per un numero, e il risultato è ancora una funzione lineare. Quindi anche le funzioni lineari formano uno spazio vettoriale.)

La proposizione non è dimostrata né a lezione né nelle dispense («è facile controllare»). La linearità di f + g, per esempio, segue da (f + g)(v + w) = f(v + w) + g(v + w) = f(v) + f(w) + g(v) + g(w) = (f + g)(v) + (f + g)(w) e da (f + g)(λv) = f(λv) + g(λv) = λf(v) + λg(v) = λ(f + g)(v). Per λf allo stesso modo: (λf)(v + w) = λ(f(v) + f(w)) = (λf)(v) + (λf)(w) e (λf)(μv) = λμf(v) = μ(λf)(v). Il vettore nullo di Hom(V, W) è la mappa nulla.

**Teorema.** Siano V e W spazi vettoriali di dimensione finita su 𝕂, con basi B = {v_{1}, …, v_{n}} e C = {w_{1}, …, w_{m}}. La funzione

Hom(V, W) → M(m, n, 𝕂),   f ↦ [f]^{B}_{C}

è un isomorfismo.

(In parole povere: scelte le basi, applicazioni lineari e matrici sono la stessa cosa. A ogni applicazione corrisponde una sola matrice e viceversa, e sommare le funzioni corrisponde a sommare le matrici.)

Nelle dispense le due basi si chiamano A e B; qui si tiene B e C come nel resto del capitolo. Non è dimostrato. Come conseguenza, per il cap. 49 Hom(V, W) ha dimensione mn, come M(m, n, 𝕂) (cap. 26).

**Come sottolineato a lezione (registrazione 2025).** La lettura finale del docente è questa: fissate una base di V e una di W, a ogni applicazione lineare corrisponde una matrice e a ogni matrice un'applicazione lineare, in modo biunivoco; e poiché ogni matrice agisce come moltiplicazione a sinistra, «ogni mappa lineare è una mappa di moltiplicazione a sinistra». È l'anticipazione del cap. 46 («parlare di funzioni lineari o di matrici è la stessa cosa»), ora diventata un teorema.

## Esercizio
Svolgimento non presente nelle dispense (che danno solo il risultato) né in lezione.

**Esercizio 15.13.** Sia f : ℂ² → ℂ³, f(x, y) = (x − y, 2x, y). Trovare la matrice associata a f rispetto alle basi v_{1} = (1, 1), v_{2} = (1, −1) in partenza e w_{1} = (1, 1, 0), w_{2} = (0, 1, 1), w_{3} = (1, 0, 1) in arrivo.

Si calcolano le immagini della base di partenza: f(v_{1}) = (0, 2, 1) e f(v_{2}) = (2, 2, −1). Poi si scrive ciascuna come a w_{1} + b w_{2} + c w_{3} = (a + c, a + b, b + c).

Per f(v_{1}): a + c = 0, a + b = 2, b + c = 1. Sommando le tre equazioni 2(a + b + c) = 3, quindi a + b + c = 3/2, e per differenza a = 3/2 − 1 = 1/2, b = 3/2 − 0 = 3/2, c = 3/2 − 2 = −1/2.

Per f(v_{2}): a + c = 2, a + b = 2, b + c = −1. Anche qui a + b + c = 3/2, quindi a = 3/2 − (−1) = 5/2, b = 3/2 − 2 = −1/2, c = 3/2 − 2 = −1/2.

Le due colonne danno

[f]^{B}_{C} = ( 1/2 5/2 ; 3/2 −1/2 ; −1/2 −1/2 ) = ½ ( 1 5 ; 3 −1 ; −1 −1 ),

con B = {v_{1}, v_{2}} e C = {w_{1}, w_{2}, w_{3}}. Controllo sulla prima colonna: ½w_{1} + 3/2·w_{2} − ½w_{3} = (½ − ½, ½ + 3/2, 3/2 − ½) = (0, 2, 1) = f(v_{1}).
