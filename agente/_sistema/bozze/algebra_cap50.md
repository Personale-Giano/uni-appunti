# 50. La Matrice Associata a un'Applicazione Lineare
## Da una matrice a una funzione, e ritorno
Dai cap. 46 e 47 si sa che una matrice A ∈ M(m, n, 𝕂) produce un'applicazione lineare L_{A} : 𝕂ⁿ → 𝕂^{m}. Se A = (A^{1} | … | A^{n}) e x = (x_{1}, …, x_{n}), allora

L_{A}(x) = Ax = x_{1}A^{1} + x_{2}A^{2} + … + x_{n}A^{n}.

A lezione (registrazione 2025) il docente lo richiama alla lavagna e annuncia l'obiettivo: fare il cammino inverso, cioè associare a un'applicazione lineare tra due spazi qualsiasi una matrice che ne contenga «tutte le informazioni». Con il cap. 49 si sa già rappresentare un vettore v con le sue coordinate [v]_{B} ∈ 𝕂ⁿ; ora si fa lo stesso con le funzioni. Purtroppo, osserva il docente, la sola funzione non basta: bisogna fissare una base nello spazio di partenza e una in quello di arrivo.

## La definizione
**Definizione.** Sia f : V → W un'applicazione lineare tra spazi vettoriali su 𝕂, e siano B = {v_{1}, …, v_{n}} una base di V e C = {w_{1}, …, w_{m}} una base di W. Ogni immagine f(v_{j}) si scrive nella base C:

f(v_{1}) = a_{11}w_{1} + … + a_{m1}w_{m},   …,   f(v_{n}) = a_{1n}w_{1} + … + a_{mn}w_{m}.

La matrice m × n A = (a_{ij}) che raccoglie questi coefficienti è la **matrice associata** a f nelle basi B e C (o «dalla base B alla base C»), e si indica con **A = [f]^{B}_{C}**.

(In parole povere: la matrice associata è la «carta d'identità» di f. Si guarda dove f manda ciascun vettore della base di partenza, lo si scrive con la base di arrivo, e quei numeri si mettono in colonna, una colonna per vettore.)

La j-esima colonna di A contiene le coordinate di f(v_{j}) rispetto a C, cioè A^{j} = [f(v_{j})]_{C}. Alla lavagna (registrazione 2025) la definizione è scritta direttamente per colonne:

[f]^{B}_{C} = ( [f(v_{1})]_{C} | [f(v_{2})]_{C} | … | [f(v_{n})]_{C} ).

Nella notazione la **base di partenza** B sta in alto e la **base di arrivo** C sta in basso; la matrice dipende da tutte e tre le cose: f, B e C. Le colonne sono tante quanti i vettori della base di partenza (n = dim V), e ciascuna ha tante entrate quanti i vettori della base di arrivo (m = dim W): **righe = dim W, colonne = dim V**. Il docente ammette che la definizione può sembrare «caotica» e passa subito a un esempio.

## L'esempio della lezione
**Esempio dalla lavagna (registrazione 2025).** Sia f : ℝ_{2}[x] → ℝ², f(p) = (p(1), p(−1)): a ogni polinomio associa i suoi valori in 1 e in −1. Si prendono le basi canoniche B = {1, x, x²} e C = {e_{1}, e_{2}}. Prima di calcolare, il docente chiede alla classe le taglie: due righe, perché dim ℝ² = 2, e tre colonne, perché dim ℝ_{2}[x] = 3. Quindi [f]^{B}_{C} ∈ M(2, 3) e

[f]^{B}_{C} = ( [f(1)]_{C} | [f(x)]_{C} | [f(x²)]_{C} ).

- Prima colonna. Il polinomio costante 1 vale 1 sia in 1 sia in −1, quindi f(1) = (1, 1). Le sue coordinate in C sono i numeri a, b con (1, 1) = a e_{1} + b e_{2} = a(1, 0) + b(0, 1) = (a, b): dunque [f(1)]_{C} = (1, 1).
- Seconda colonna. f(x) = (1, −1), e allo stesso modo [f(x)]_{C} = (1, −1).
- Terza colonna. f(x²) = (1², (−1)²) = (1, 1), lo stesso vettore di f(1), quindi la stessa colonna.

Il risultato è

[f]^{B}_{C} = ( 1 1 1 ; 1 −1 1 ).

## Lo stesso tipo di funzione con un'altra base di arrivo
Nella base canonica le coordinate sono le entrate stesse, quindi le colonne si leggono subito. Con una base di arrivo diversa bisogna risolvere un piccolo sistema per ogni colonna. Le dispense lo mostrano con una variante dell'esempio (valori in 2 e −2 invece che in 1 e −1); a lezione questo secondo esempio non è svolto.

**Esempio.** Sia f : ℝ_{2}[x] → ℝ², f(p) = (p(2), p(−2)). Con le basi canoniche B = {1, x, x²} e C = {e_{1}, e_{2}}:

f(1) = (1, 1),   f(x) = (2, −2),   f(x²) = (4, 4),   quindi   [f]^{B}_{C} = ( 1 2 4 ; 1 −2 4 ).

Si tiene B e si prende in arrivo C′ = {(1, −1), (0, 1)}. Ora ogni immagine va scritta come combinazione dei vettori di C′. Da (s, t) = α(1, −1) + β(0, 1) = (α, β − α) si ricava α = s e β = s + t, quindi

f(1) = (1, 1) = 1·(1, −1) + 2·(0, 1),   f(x) = (2, −2) = 2·(1, −1) + 0·(0, 1),   f(x²) = (4, 4) = 4·(1, −1) + 8·(0, 1),

e [f]^{B}_{C′} = ( 1 2 4 ; 2 0 8 ). La funzione è la stessa, ma cambiando base cambia la matrice.

## La matrice associata a L_{A} nelle basi canoniche
**Proposizione.** Sia A ∈ M(m, n, 𝕂), e siano B = {e_{1}, …, e_{n}} la base canonica di 𝕂ⁿ e C = {e_{1}, …, e_{m}} la base canonica di 𝕂^{m}. Allora la matrice associata a L_{A} : 𝕂ⁿ → 𝕂^{m} è proprio A: [L_{A}]^{B}_{C} = A.

(In parole povere: se si parte da una matrice, si costruisce la funzione «moltiplica per A» e poi se ne calcola la matrice associata con le basi più semplici, si ritrova la matrice di partenza. Le due costruzioni sono una l'inversa dell'altra.)

**Dimostrazione (alla lavagna, registrazione 2025).** Per definizione [L_{A}]^{B}_{C} = ( [L_{A}e_{1}]_{C} | … | [L_{A}e_{n}]_{C} ), una matrice con le stesse dimensioni di A. Si calcola una colonna alla volta.
1. L_{A}e_{1} = 1·A^{1} + 0·A^{2} + … + 0·A^{n} = A^{1}, la prima colonna di A; in generale L_{A}e_{j} = A^{j} (cap. 47).
2. Nella base canonica di 𝕂^{m} le coordinate di un vettore sono le sue entrate: (a_{1}, …, a_{m}) = a_{1}e_{1} + … + a_{m}e_{m}, quindi [L_{A}e_{j}]_{C} = L_{A}e_{j} = A^{j}.
3. Le colonne sono dunque A^{1}, A^{2}, …, A^{n}, cioè [L_{A}]^{B}_{C} = (A^{1} | A^{2} | … | A^{n}) = A. ∎

**Come sottolineato a lezione (registrazione 2025).** Lo scopo di questo esempio è mostrare che la definizione di matrice associata, che può sembrare «super arbitraria», è esattamente l'operazione inversa di quella che manda una matrice A nella funzione L_{A}. Il docente richiama anche che la base canonica è «la più speciale» tra le basi di 𝕂^{m}: è l'unica in cui le coordinate di ogni vettore sono le sue entrate. Ed è, dice, la prima di una serie di prove che queste matrici hanno proprietà speciali.

Per esempio, con A = ( 3 2 ; 1 0 ) si ha L_{A}(x, y) = (3x + 2y, x) (cap. 46), e infatti L_{A}(e_{1}) = (3, 1) e L_{A}(e_{2}) = (2, 0) sono le colonne di A.

Il capitolo successivo mostra a che cosa serve la matrice associata: calcolare le immagini con un prodotto riga per colonna.
