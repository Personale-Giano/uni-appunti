# 53. Composizione di Applicazioni Lineari e Prodotto di Matrici
## La seconda domanda
Il cap. 52 ha risposto alla domanda sui vettori: cambiando base, le coordinate cambiano per la moltiplicazione con la matrice del cambio di base. La seconda domanda della lezione (registrazione 2025) riguarda le applicazioni lineari: data f : V → W, due basi B e B′ di V e due basi C e C′ di W, come sono legate le matrici [f]^{B}_{C} e [f]^{B′}_{C′}?

Un legame, osserva il docente, ci deve essere: sono due traduzioni in numeri della stessa funzione, e le proprietà della funzione devono ritrovarsi in entrambe; «non possono essere due matrici a caso». Per trovarlo serve prima uno strumento, la composizione. La risposta completa arriva nel capitolo successivo.

## La composizione di applicazioni lineari
Oltre a sommarle e a moltiplicarle per uno scalare (cap. 51), le applicazioni lineari si possono comporre. La composizione è quella di Matematica discreta.

**Definizione.** Date due applicazioni f : V → W e g : W → U, la **composizione** di f e g è la funzione g ∘ f : V → U definita da

(g ∘ f)(v) = g(f(v)).

(In parole povere: si fa prima f e poi g, una dopo l'altra.)

Si può fare solo se lo spazio di arrivo di f è lo spazio di partenza di g.

**Proposizione.** Se f : V → W e g : W → U sono applicazioni lineari, anche la composizione g ∘ f : V → U è lineare.

(In parole povere: fare una dopo l'altra due trasformazioni che rispettano somme e multipli dà ancora una trasformazione che rispetta somme e multipli.)

Né le dispense né la lezione la dimostrano. La verifica è breve: usando prima la linearità di f e poi quella di g,

(g ∘ f)(v + v′) = g(f(v) + f(v′)) = g(f(v)) + g(f(v′)),   (g ∘ f)(λv) = g(λf(v)) = λ g(f(v)).

## Comporre le L_{A} vuol dire moltiplicare le matrici
**Proposizione.** Siano A ∈ M(m, n, 𝕂) e B ∈ M(n, p, 𝕂), e siano L_{B} : 𝕂^{p} → 𝕂ⁿ e L_{A} : 𝕂ⁿ → 𝕂^{m} le applicazioni lineari corrispondenti. Allora

L_{A} ∘ L_{B} = L_{AB}.

(In parole povere: moltiplicare un vettore prima per B e poi per A è lo stesso che moltiplicarlo una volta sola per la matrice AB. Il prodotto di matrici è la composizione delle funzioni.)

Le dimensioni tornano: il prodotto AB si può fare perché le colonne di A sono quante le righe di B, e AB ∈ M(m, p, 𝕂) dà una funzione 𝕂^{p} → 𝕂^{m}, proprio come la composizione. Le dispense enunciano lo stesso fatto con A ∈ M(k, m, 𝕂) e B ∈ M(m, n, 𝕂): cambiano solo i nomi delle dimensioni.

**Dimostrazione.** Per ogni v ∈ 𝕂^{p}:

L_{AB}(v) = (AB)·v = A·(Bv) = L_{A}(Bv) = L_{A}(L_{B}(v)).

Il secondo passaggio è la proprietà associativa del prodotto fra matrici (cap. 30), con il vettore v visto come matrice p × 1. ∎

A lezione (registrazione 2025) il docente la svolge perché «è una riga». **Come sottolineato a lezione**, questo risultato spiega perché il prodotto fra matrici è definito proprio in quel modo. Presa da sola, la regola riga per colonna del cap. 29 «sembra estremamente arbitraria»; diventa naturale quando si pensa a una matrice come alla funzione che prende un vettore e lo moltiplica per la matrice. Il prodotto è fatto apposta perché corrisponda alla composizione.

**Esempio.** Qui A e B sono matrici, non basi. Con le due matrici usate nella lezione, A = ( 1 2 ; 2 1 ) e B = ( 1 1 ; 1 2 ), si ha L_{B}(x, y) = (x + y, x + 2y) e quindi

L_{A}(L_{B}(x, y)) = ( (x + y) + 2(x + 2y), 2(x + y) + (x + 2y) ) = (3x + 5y, 3x + 4y).

D'altra parte le entrate di AB sono 1·1 + 2·1 = 3, 1·1 + 2·2 = 5, 2·1 + 1·1 = 3, 2·1 + 1·2 = 4, cioè AB = ( 3 5 ; 3 4 ), e L_{AB}(x, y) = (3x + 5y, 3x + 4y): la stessa funzione. L'ordine conta: BA = ( 3 3 ; 5 4 ) è un'altra matrice, perché L_{B} ∘ L_{A} è un'altra funzione (cap. 30).

## La matrice associata a una composizione
Dopo la pausa il docente fa «un passo oltre»: anche partendo da applicazioni lineari qualsiasi, e passando alle matrici associate, la composizione diventa un prodotto.

**Proposizione.** Siano f : V → W e g : W → U applicazioni lineari, e siano B, C, D basi di V, W, U. Allora

[g ∘ f]^{B}_{D} = [g]^{C}_{D} · [f]^{B}_{C}.

(In parole povere: la matrice di «prima f, poi g» è il prodotto delle due matrici, scritte nell'ordine inverso: a destra quella di f, che agisce per prima. In mezzo ci deve essere la stessa base C, usata come arrivo per f e come partenza per g.)

**Dimostrazione.** Sia B = {v_{1}, …, v_{n}}. Si confrontano le due matrici colonna per colonna.
1. Per definizione di matrice associata (cap. 50), la j-esima colonna di [g ∘ f]^{B}_{D} è [g(f(v_{j}))]_{D}.
2. Per la proposizione del cap. 51 applicata a g e al vettore f(v_{j}) ∈ W, vale [g(f(v_{j}))]_{D} = [g]^{C}_{D} · [f(v_{j})]_{C}.
3. Il vettore [f(v_{j})]_{C} è la j-esima colonna di [f]^{B}_{C}. E, per la regola riga per colonna (cap. 29), la j-esima colonna di un prodotto di matrici si ottiene moltiplicando la prima matrice per la j-esima colonna della seconda.
4. Quindi le due matrici hanno le stesse colonne, cioè sono uguali. ∎

La dimostrazione è quella delle dispense; a lezione la proposizione è solo enunciata. Le dispense chiamano gli spazi U, V, W nell'ordine, alla lavagna (registrazione 2025) sono V, W, U con basi A, B, C: qui si tengono gli spazi della lavagna e le basi B, C, D. Se dim V = n, dim W = m e dim U = p, le matrici sono [f]^{B}_{C} ∈ M(m, n), [g]^{C}_{D} ∈ M(p, m) e il prodotto sta in M(p, n), come deve essere per una funzione da V a U.

**Come sottolineato a lezione (registrazione 2025).** In altri libri la base di partenza e quella di arrivo si scrivono in posizioni diverse. La scelta del corso, partenza in alto e arrivo in basso, aiuta a ricordare la formula: nel prodotto [g]^{C}_{D} · [f]^{B}_{C} è «come se si cancellasse» la base di mezzo, la C in alto del primo fattore con la C in basso del secondo, e restano B in alto e D in basso.

![Sopra, le applicazioni lineari e la loro composizione; sotto, in coordinate, le matrici associate e il loro prodotto.](figure/alg/composizione_teoria_calcoli.png|12)

Il docente riprende qui il disegno «teoria / calcoli» del cap. 51. Le basi associano a ogni spazio astratto uno spazio concreto di vettori colonna, e a ogni applicazione lineare la sua matrice; in questa corrispondenza le composizioni di sopra diventano prodotti di sotto. Alla lavagna le due matrici si chiamano A = [f] e B = [g], e l'arco in basso è L_{BA}: la matrice di f sta a destra. Chi trova utile il disegno lo tenga, dice il docente; chi no, lo dimentichi.

**Esempio.** Sia f : ℝ_{2}[x] → ℝ², f(p) = (p(1), p(−1)), con [f]^{B}_{E} = ( 1 1 1 ; 1 −1 1 ) rispetto a B = {1, x, x²} e alla base canonica E di ℝ² (cap. 50), e sia g = L_{A} : ℝ² → ℝ² con A = ( 1 2 ; 2 1 ), per cui [g]^{E}_{E} = A. Allora

[g ∘ f]^{B}_{E} = ( 1 2 ; 2 1 ) · ( 1 1 1 ; 1 −1 1 ) = ( 3 −1 3 ; 3 1 3 ).

Controllo sulla seconda colonna: f(x) = (1, −1) e g(1, −1) = (1 − 2, 2 − 1) = (−1, 1). (Esempio non presente nelle dispense né in lezione.)

## Isomorfismi e matrici invertibili
La formula della composizione ha una prima conseguenza, che le dispense enunciano come corollario e che a lezione compare solo nel caso dell'identità.

**Proposizione.** Sia f : V → W un'applicazione lineare e siano B e C basi di V e di W. Allora f è un isomorfismo se e solo se la matrice [f]^{B}_{C} è invertibile, e in questo caso

( [f]^{B}_{C} )^{−1} = [f^{−1}]^{C}_{B}.

(In parole povere: una funzione lineare si può «fare al contrario» esattamente quando la sua matrice si può invertire. E la matrice della funzione inversa è l'inversa della matrice, con le due basi scambiate.)

**Dimostrazione.** Se f è un isomorfismo, V e W hanno la stessa dimensione n (cap. 49) e l'inversa f^{−1} : W → V è lineare. Poiché f^{−1} ∘ f = I_{V} e f ∘ f^{−1} = I_{W}, la formula della composizione e la matrice dell'identità (cap. 51) danno

[f^{−1}]^{C}_{B} · [f]^{B}_{C} = [I_{V}]^{B}_{B} = I_{n},   [f]^{B}_{C} · [f^{−1}]^{C}_{B} = [I_{W}]^{C}_{C} = I_{n}.

Quindi [f^{−1}]^{C}_{B} è l'inversa di [f]^{B}_{C}. Viceversa, sia A = [f]^{B}_{C} invertibile (in particolare quadrata). Per il teorema del cap. 51 ogni matrice è la matrice associata di una e una sola applicazione lineare: esiste g : W → V con [g]^{C}_{B} = A^{−1}. Allora [g ∘ f]^{B}_{B} = A^{−1}A = I_{n} = [I_{V}]^{B}_{B}, e poiché applicazioni con la stessa matrice coincidono, g ∘ f = I_{V}; allo stesso modo f ∘ g = I_{W}. Dunque f è biettiva e g = f^{−1}. ∎

**L'inversa del cambio di base.** Applicata all'identità, questa proposizione dà di nuovo, per un'altra via, la formula dell'inversa del cap. 52. L'identità I_{V} è un isomorfismo ed è l'inversa di se stessa; con base di partenza B e base di arrivo B′ si ottiene che [I_{V}]^{B}_{B′} è invertibile e

( [I_{V}]^{B}_{B′} )^{−1} = [I_{V}]^{B′}_{B}.

## Cambio di base tra due basi qualsiasi
Dal cap. 52 si sa che in 𝕂ⁿ la matrice del cambio di base è immediata se la base di arrivo è la canonica, ed è «quasi facile» se la canonica è la base di partenza (è l'inversa di una matrice facile). Resta il caso in cui **nessuna** delle due basi è la canonica. L'osservazione che segue è solo alla lavagna (registrazione 2025).

**Osservazione.** Siano B e B′ due basi di V = 𝕂ⁿ e sia E la base canonica (alla lavagna C). L'identità composta con l'identità è ancora l'identità, I_{V} = I_{V} ∘ I_{V}; mettendo la base canonica nel passaggio intermedio, la formula della composizione dà

[I_{V}]^{B}_{B′} = [I_{V}]^{E}_{B′} · [I_{V}]^{B}_{E} = ( [I_{V}]^{B′}_{E} )^{−1} · [I_{V}]^{B}_{E}.

I due fattori finali sono entrambi «facili»: [I_{V}]^{B}_{E} ha per colonne i vettori di B, e [I_{V}]^{B′}_{E} ha per colonne i vettori di B′. La ricetta è quindi: scrivere in colonna le due basi, invertire la matrice della base di **arrivo** e moltiplicarla, a sinistra, per la matrice della base di partenza.

A una domanda il docente precisa che la base di mezzo la sceglie chi fa il conto: la formula varrebbe con qualsiasi base, ma solo con la canonica i due fattori si scrivono senza fatica.

**Esempio dalla lavagna (registrazione 2025).** In ℝ² siano B = {(1, 1), (1, 2)} e B′ = {(0, 1), (−1, 3)}. Le due matrici facili sono

[I_{V}]^{B}_{E} = ( 1 1 ; 1 2 ),   [I_{V}]^{B′}_{E} = ( 0 −1 ; 1 3 ).

La seconda ha determinante 0·3 − (−1)·1 = 1, e con la regola del cap. 36 la sua inversa è ( 3 1 ; −1 0 ). Quindi

[I_{V}]^{B}_{B′} = ( 3 1 ; −1 0 ) · ( 1 1 ; 1 2 ) = ( 4 5 ; −1 −1 ),

dove le quattro entrate sono 3·1 + 1·1 = 4, 3·1 + 1·2 = 5, −1 + 0 = −1, −1 + 0 = −1.

Il risultato si controlla con il significato delle colonne: devono essere le coordinate dei vettori di B nella base B′. Infatti 4·(0, 1) − 1·(−1, 3) = (1, 1) e 5·(0, 1) − 1·(−1, 3) = (1, 2).

Con la formula della composizione e le matrici del cambio di base si può ora rispondere alla seconda domanda: è l'argomento del capitolo successivo.
