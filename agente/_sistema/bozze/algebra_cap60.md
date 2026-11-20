# 60. Endomorfismi e Matrici Diagonalizzabili
## La definizione
Nel cap. 59 la base dell'oracolo per ( 1 2 ; 2 1 ) era fatta di due autovettori, e in quella base la matrice era diagonale. A lezione (registrazione 2025) il docente dà un nome agli endomorfismi per cui una base così esiste.

**Definizione.** Un endomorfismo T : V → V è **diagonalizzabile** se esiste una base B = {v_{1}, …, v_{n}} di V formata da autovettori di T.

(In parole povere: T è diagonalizzabile se si possono scegliere n direzioni indipendenti che T non fa girare, tante quante la dimensione dello spazio. Usando quelle direzioni come assi, T si limita ad allungare o accorciare ciascun asse per conto suo.)

Per esempio L_{A} con A = ( 1 2 ; 2 1 ) è diagonalizzabile: (1, 1) e (1, −1) sono autovettori (cap. 59) e sono linearmente indipendenti, perché non sono uno multiplo dell'altro; due vettori indipendenti in ℝ² formano una base (cap. 26). La rotazione Rot_{π/2} : ℝ² → ℝ² invece non è diagonalizzabile, perché non ha nessun autovettore reale (su ℂ le cose cambiano, cap. 61).

Il nome viene dal fatto seguente, «cruciale» nelle parole delle dispense, che a lezione è la ragione stessa della definizione.

## Base di autovettori e matrice diagonale
**Proposizione.** Sia T : V → V un endomorfismo e sia B = {v_{1}, …, v_{n}} una base di V formata da autovettori di T, con T(v_{i}) = λ_{i}v_{i}. Allora la matrice associata [T]^{B}_{B} è diagonale, e sulla diagonale ci sono gli autovalori:

[T]^{B}_{B} = diag(λ_{1}, λ_{2}, …, λ_{n}).

(In parole povere: se gli assi scelti sono autovettori, la matrice non ha niente fuori dalla diagonale, perché ogni asse viene mandato in un multiplo di se stesso e non «sporca» gli altri. Sulla diagonale si legge di quanto viene moltiplicato ciascun asse.)

Qui diag(λ_{1}, …, λ_{n}) indica la matrice diagonale con λ_{1}, …, λ_{n} sulla diagonale principale e zeri altrove (cap. 21); alla lavagna è disegnata con λ_{1} in alto a sinistra, λ_{n} in basso a destra e i puntini in mezzo.

**Dimostrazione (alla lavagna, registrazione 2025).** Per definizione di matrice associata (cap. 50), la i-esima colonna di [T]^{B}_{B} è il vettore delle coordinate [T(v_{i})]_{B}. Poiché v_{i} è un autovettore, T(v_{i}) = λ_{i}v_{i}, e il multiplo può cambiare da vettore a vettore. Resta da scrivere λ_{i}v_{i} come combinazione lineare di v_{1}, …, v_{n}, e c'è un modo ovvio:
- λ_{1}v_{1} = λ_{1}v_{1} + 0·v_{2} + … + 0·v_{n}, quindi [λ_{1}v_{1}]_{B} = (λ_{1}, 0, …, 0);
- λ_{2}v_{2} = 0·v_{1} + λ_{2}v_{2} + 0·v_{3} + … + 0·v_{n}, quindi [λ_{2}v_{2}]_{B} = (0, λ_{2}, 0, …, 0);
- e così via: la i-esima colonna ha λ_{i} al posto i e zeri altrove.

Mettendo in fila le colonne si ottiene la matrice diagonale diag(λ_{1}, …, λ_{n}). ∎

Il docente sottolinea l'osservazione finale: la matrice non è solo diagonale, ma ha sulla diagonale **gli autovalori** degli elementi della base, nello stesso ordine. Sono esattamente le matrici dell'inizio del cap. 59, quelle per cui è facilissimo capire che cosa fanno e come si iterano.

**Il viceversa.** A lezione (registrazione 2025) il docente aggiunge che «vale anche l'opposto»: se T ammette una base B = {v_{1}, …, v_{n}} tale che [T]^{B}_{B} = diag(λ_{1}, …, λ_{n}), allora
1. i vettori v_{i} sono autovettori;
2. T(v_{i}) = λ_{i}v_{i}, cioè gli elementi sulla diagonale sono gli autovalori corrispondenti;
3. T è diagonalizzabile.

Il motivo è la stessa lettura delle colonne fatta al contrario: la i-esima colonna (0, …, λ_{i}, …, 0) dice che T(v_{i}) = 0·v_{1} + … + λ_{i}v_{i} + … + 0·v_{n} = λ_{i}v_{i}, e v_{i} ≠ 0 perché fa parte di una base. Le dispense riuniscono le due direzioni in un solo enunciato (Proposizione 17.6): per una base B qualsiasi, [T]^{B}_{B} è diagonale **se e solo se** i vettori di B sono tutti autovettori di T. In sintesi:

T è diagonalizzabile   ⟺   esiste una base B di V tale che [T]^{B}_{B} è diagonale.

## Esempi
**Esempio 17.9.** Sia A = ( 3 4 ; 0 2 ) (Esempio 17.2 del cap. 59). I vettori v_{1} = (1, 0) e v_{2} = (−4, 1) sono autovettori, con autovalori 3 e 2, e sono linearmente indipendenti, quindi formano una base B di ℝ². Per la proposizione

[L_{A}]^{B}_{B} = ( 3 0 ; 0 2 ),

e L_{A} è diagonalizzabile.

**Esempio dalla lavagna (registrazione 2025).** Per A = ( 1 2 ; 2 1 ) e B = {(1, 1), (1, −1)} la proposizione ritrova la matrice del cap. 59: autovalori 3 e −1 nell'ordine dei vettori, quindi [L_{A}]^{B}_{B} = ( 3 0 ; 0 −1 ).

**Esempio 17.10.** La rotazione di un angolo θ ≠ 0, π non è diagonalizzabile su ℝ, perché non ha autovettori (cap. 59). Per θ = 0 e θ = π diventa f(v) = v e f(v) = −v: ogni base è fatta di autovettori, e la matrice in qualunque base è I_{2} oppure −I_{2}.

## Le matrici diagonalizzabili: A = PDP^{−1}
Il caso più importante è quello di T = L_{A} : 𝕂ⁿ → 𝕂ⁿ, con A ∈ M(n, 𝕂). Per definizione L_{A} è diagonalizzabile se e solo se esiste una base B = {v_{1}, …, v_{n}} di 𝕂ⁿ con [L_{A}]^{B}_{B} = D = diag(λ_{1}, …, λ_{n}). Alla lavagna (registrazione 2025) il docente traduce questa condizione in una formula sulla sola matrice A, con quello che si sa dai cap. 50-54.

Sia E la base canonica di 𝕂ⁿ (alla lavagna C). Da una parte [L_{A}]^{E}_{E} = A (cap. 50). Dall'altra, per la formula del cambio di base degli endomorfismi (cap. 54), con B come base «vecchia» ed E come base «nuova»,

A = [L_{A}]^{E}_{E} = [I_{V}]^{B}_{E} · [L_{A}]^{B}_{B} · ( [I_{V}]^{B}_{E} )^{−1}.

Il fattore centrale è D; il primo, chiamato P, è la matrice del cambio di base da B alla canonica, che si scrive senza conti mettendo in colonna i vettori di B (cap. 52). Quindi

A = P D P^{−1},   con   P = ( v_{1} | v_{2} | … | v_{n} )   e   D = diag(λ_{1}, …, λ_{n}).

**Proposizione.** Una matrice A ∈ M(n, 𝕂) è diagonalizzabile (cioè L_{A} è diagonalizzabile) se e solo se si può scrivere

A = P D P^{−1},

dove P = ( v_{1} | … | v_{n} ) è la **matrice degli autovettori**, che ha in colonna una base di autovettori, e D = diag(λ_{1}, …, λ_{n}) è la **matrice degli autovalori**, con λ_{i} autovalore di v_{i}.

(In parole povere: diagonalizzare una matrice vuol dire scriverla come «cambio di base, poi matrice diagonale, poi cambio di base all'indietro». P contiene le direzioni speciali e D i numeri per cui vengono moltiplicate.)

È la stessa cosa che dire, osserva il docente a voce, che A è diagonalizzabile se e solo se è **simile** a una matrice diagonale (cap. 54): A = PDP^{−1} è la definizione del cap. 54 di D ∼ A (con la matrice P), e la relazione è simmetrica. E in quel caso gli elementi sulla diagonale di D sono gli autovalori e le colonne di P sono gli autovettori.

Il «se» si vede così: se A = PDP^{−1} con P invertibile e D diagonale, le colonne di P sono indipendenti (una matrice invertibile ha colonne indipendenti, come già usato nel cap. 54), quindi formano una base B di 𝕂ⁿ con P = [I_{V}]^{B}_{E}, e il conto di sopra letto al contrario dà [L_{A}]^{B}_{B} = P^{−1}AP = D; per il viceversa della proposizione precedente, i vettori di B sono autovettori. Alla lavagna nessuna delle due direzioni è dimostrata per esteso.

**Le notazioni delle dispense.** Le dispense danno questa come definizione (Definizione 17.7): A è diagonalizzabile se è simile a una matrice diagonale, cioè se esiste M invertibile con

D = M^{−1} A M

diagonale. È la stessa condizione con M = P: moltiplicando A = PDP^{−1} a sinistra per P^{−1} e a destra per P si ottiene P^{−1}AP = D. Nell'Esempio 17.11 anche le dispense prendono M = [id]^{B}_{E} (con la canonica chiamata C), la matrice con gli autovettori in colonna. Il legame con gli endomorfismi è la Proposizione 17.8: se B è una base di V, l'endomorfismo T è diagonalizzabile se e solo se la matrice A = [T]^{B}_{B} è diagonalizzabile.

La dimostrazione delle dispense è quella appena vista in un'altra base. Se T è diagonalizzabile, c'è una base C con D = [T]^{C}_{C} diagonale, e con M = [id]^{C}_{B} la formula del cap. 54 dà D = M^{−1}AM. Viceversa, se D = M^{−1}AM è diagonale, si prende come C la base di V formata dai vettori che hanno per coordinate in B le colonne di M: allora M = [id]^{C}_{B} e [T]^{C}_{C} = M^{−1}AM = D.

**Esempio.** Per A = ( 1 2 ; 2 1 ), con gli autovettori (1, 1) e (1, −1) in colonna e gli autovalori nello stesso ordine,

P = ( 1 1 ; 1 −1 ),   D = ( 3 0 ; 0 −1 ),   P^{−1} = ( 1/2 1/2 ; 1/2 −1/2 ),

e infatti P D P^{−1} = ( 3 −1 ; 3 1 ) · ( 1/2 1/2 ; 1/2 −1/2 ) = ( 3/2 − 1/2  3/2 + 1/2 ; 3/2 + 1/2  3/2 − 1/2 ) = ( 1 2 ; 2 1 ) = A.

**Attenzione all'ordine.** L'ordine degli autovalori in D deve essere lo stesso degli autovettori nelle colonne di P: il primo autovalore è quello della prima colonna, e così via. Alla lavagna non è scritto, ma è sottinteso, ed è proprio il punto sbagliato nell'esempio del cap. 59. Con la stessa P e gli autovalori scambiati, D′ = ( −1 0 ; 0 3 ), si ottiene P D′ P^{−1} = ( 1 −2 ; −2 1 ), che è un'altra matrice. (Il conto con D′ è aggiunto per chiarezza.)

## Perché le matrici diagonali sono comode
Le dispense spiegano perché si preferiscono le matrici diagonali: sono molto più maneggevoli. Con D = diag(λ_{1}, …, λ_{n}):
- il prodotto per un vettore moltiplica ogni componente per il suo numero: D·(x_{1}, …, x_{n}) = (λ_{1}x_{1}, …, λ_{n}x_{n});
- il determinante è il prodotto della diagonale, det D = λ_{1} ⋯ λ_{n}, come per ogni matrice triangolare (cap. 32);
- il prodotto di due matrici diagonali è diagonale e si fa elemento per elemento: diag(λ_{1}, …, λ_{n}) · diag(μ_{1}, …, μ_{n}) = diag(λ_{1}μ_{1}, …, λ_{n}μ_{n});
- di conseguenza le potenze sono immediate: D^{k} = diag(λ_{1}^{k}, …, λ_{n}^{k}).

Per una matrice diagonalizzabile le potenze diventano facili anche se la matrice non è diagonale. Da A = PDP^{−1}, nel prodotto A^{k} = (PDP^{−1})(PDP^{−1}) ⋯ (PDP^{−1}) ogni P^{−1} si cancella con la P che lo segue (P^{−1}P = I_{n}), e resta

A^{k} = P D^{k} P^{−1}.

**Esempio 17.11.** Si vuole A^{100} per A = ( 3 4 ; 0 2 ). Calcolare cento prodotti sarebbe estremamente dispendioso, ma dall'Esempio 17.9 A è diagonalizzabile con

M = ( 1 −4 ; 0 1 ),   D = ( 3 0 ; 0 2 ),   M^{−1} = ( 1 4 ; 0 1 ),

dove M ha in colonna gli autovettori (1, 0) e (−4, 1) e la sua inversa si trova con la regola 2 × 2 (cap. 36; il determinante è 1). Quindi

A^{100} = M D^{100} M^{−1} = ( 1 −4 ; 0 1 ) · ( 3^{100} 0 ; 0 2^{100} ) · ( 1 4 ; 0 1 ).

Il prodotto delle ultime due è ( 3^{100} 4·3^{100} ; 0 2^{100} ), e moltiplicando a sinistra per M:

A^{100} = ( 3^{100}  4·(3^{100} − 2^{100}) ; 0  2^{100} ).

**Ritorno all'esempio iniziale.** Lo stesso metodo dà le iterate di ( 1 2 ; 2 1 ) della motivazione del cap. 59, questa volta nella base canonica (conto non presente nelle dispense né in lezione). Con P e D dell'esempio precedente,

A^{k} = P · diag(3^{k}, (−1)^{k}) · P^{−1} = (1/2) · ( 3^{k} + (−1)^{k}  3^{k} − (−1)^{k} ; 3^{k} − (−1)^{k}  3^{k} + (−1)^{k} ).

Per k = 1 si ritrova ( 1 2 ; 2 1 ), per k = 2 si ottiene ( 5 4 ; 4 5 ), che è proprio A·A.

Come ricorda il docente alla fine della prima parte della lezione (registrazione 2025), gli endomorfismi diagonalizzabili sono in qualche senso «speciali», particolarmente belli, e sapere se l'endomorfismo con cui si lavora è diagonalizzabile è importante. Ma per esserlo serve una base di autovettori, e resta la domanda: come si calcolano autovalori e autovettori? È il tema del capitolo successivo.
