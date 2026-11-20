# 61. Il Polinomio Caratteristico
## Prima gli autovalori, poi gli autovettori
Il cap. 60 ha mostrato che per diagonalizzare serve una base di autovettori; resta da capire come trovarli senza un oracolo. A lezione (registrazione 2025) il docente annuncia il metodo: la domanda vera sarebbe come calcolare autovettori e autovalori, ma si procede in due tempi. **Prima** si calcolano gli autovalori; **poi**, conoscendo gli autovalori, si trovano gli autovettori. Questo capitolo è dedicato al primo passo, il cap. 62 al secondo.

Per l'osservazione del cap. 59 basta studiare una matrice quadrata A ∈ M(n, 𝕂), cioè L_{A} : 𝕂ⁿ → 𝕂ⁿ. Il docente riscrive la definizione mettendo in luce l'autovalore invece dell'autovettore: λ ∈ 𝕂 è un autovalore di A se esiste v ≠ 0 tale che Av = λv. Scrivendo λv come λ I_{n} v e portando tutto a sinistra, alla lavagna si ottiene una catena di equivalenze:

λ è autovalore di A
⟺ esiste v ≠ 0 tale che (A − λI_{n})v = 0
⟺ Ker(A − λI_{n}) = {v ∈ 𝕂ⁿ | (A − λI_{n})v = 0} ≠ {0}
⟺ A − λI_{n} non è invertibile
⟺ det(A − λI_{n}) = 0.

Il primo passaggio è solo algebra: Av = λI_{n}v equivale ad Av − λI_{n}v = 0, cioè (A − λI_{n})v = 0. Il secondo riscrive la definizione di nucleo (cap. 47): esiste un vettore non nullo che va in 0 se e solo se il nucleo non è solo lo zero. Il terzo usa un fatto sulle matrici quadrate, che il docente richiama: le matrici invertibili sono esattamente quelle con nucleo nullo, cioè quelle per cui il sistema omogeneo ha la sola soluzione 0 (il motivo, non ripetuto a lezione: per il teorema della dimensione, cap. 48, una matrice quadrata con nucleo nullo ha rango n, e quindi è invertibile). L'ultimo è il criterio del determinante (cap. 36): una matrice quadrata è invertibile se e solo se il suo determinante è diverso da zero.

## La definizione
L'ultima condizione suggerisce di considerare det(A − tI_{n}) come funzione di una variabile t.

**Definizione.** Sia A = (a_{ij}) ∈ M(n, 𝕂). Il **polinomio caratteristico** di A è

p_{A}(t) = det(A − tI_{n}) = det( a_{11} − t  a_{12}  …  a_{1n} ; a_{21}  a_{22} − t  …  a_{2n} ; … ; a_{n1}  a_{n2}  …  a_{nn} − t ).

(In parole povere: si prende la matrice, si toglie t a ogni elemento della diagonale e se ne calcola il determinante. Viene un'espressione in t, e gli autovalori sono i valori di t che la fanno diventare zero.)

Alla lavagna la variabile è t e le radici si chiamano λ; le dispense usano direttamente λ e scrivono p_{A}(λ) = det(A − λI_{n}). Il segno è lo stesso in entrambi: A − tI, non tI − A.

**Proposizione.** Sia A ∈ M(n, 𝕂). Uno scalare λ ∈ 𝕂 è un autovalore di A se e solo se è una radice del polinomio caratteristico, cioè p_{A}(λ) = 0.

(In parole povere: per trovare gli autovalori non si cercano più vettori a tentativi; si risolve un'equazione in una sola incognita, p_{A}(t) = 0.)

La dimostrazione è la catena di equivalenze di sopra, che alle dispense (Proposizione 17.13) serve allo stesso modo. Come sottolineato a lezione (registrazione 2025), è il momento in cui torna utile tutto quello che si è fatto sui polinomi e sulle loro radici nelle prime settimane (cap. 10-13): «adesso ci serve tutto quello».

## Il primo esempio: ( 1 2 ; 2 1 )
**Esempio dalla lavagna (registrazione 2025).** Si calcolano gli autovalori della matrice della motivazione, A = ( 1 2 ; 2 1 ), in due passi.

① Il polinomio caratteristico. Si toglie t sulla diagonale e si calcola il determinante 2 × 2 (prodotto della diagonale principale meno prodotto della secondaria):

p_{A}(t) = det( 1 − t  2 ; 2  1 − t ) = (1 − t)(1 − t) − 2·2 = t^{2} − 2t + 1 − 4 = t^{2} − 2t − 3.

② Le radici. Si risolve λ^{2} − 2λ − 3 = 0 con la formula delle equazioni di secondo grado (cap. 13):

λ = (2 ± √(4 + 12))/2 = (2 ± 4)/2,   cioè λ = 3 oppure λ = −1.

Infatti t^{2} − 2t − 3 = (t − 3)(t + 1). Come sottolineato a lezione, sono esattamente gli autovalori che erano comparsi «dal nulla» nell'esempio iniziale del cap. 59, con gli autovettori (1, 1) e (1, −1).

## Il caso 2 × 2: traccia e determinante
Il docente fa due osservazioni che valgono sempre. La prima: A − tI_{n} è uguale ad A tranne sulla diagonale, dove a ogni elemento si toglie t, quindi non serve rifare ogni volta il prodotto per l'identità. La seconda riguarda le matrici 2 × 2, ripresa anche all'inizio della lezione successiva (registrazione 2024): per A = ( a b ; c d ),

p_{A}(t) = det( a − t  b ; c  d − t ) = (a − t)(d − t) − bc = t^{2} − (a + d)t + (ad − bc).

Il coefficiente di t è l'opposto della somma degli elementi sulla diagonale, cioè −tr A (la traccia, cap. 30), e il termine noto è il determinante. Quindi, per ogni matrice 2 × 2,

p_{A}(t) = t^{2} − (tr A)·t + det A.

(In parole povere: per una 2 × 2 il polinomio caratteristico si scrive a occhio, senza calcolare alcun determinante con t dentro. Basta sommare la diagonale e calcolare il determinante della matrice.)

Per ( 1 2 ; 2 1 ): tr A = 2 e det A = 1 − 4 = −3, quindi t^{2} − 2t − 3, come sopra. Per A = ( 2 1 ; 1 2 ), l'esempio della lezione successiva (registrazione 2024): tr A = 4 e det A = 3, quindi p_{A}(t) = t^{2} − 4t + 3 = (t − 1)(t − 3), con autovalori 1 e 3. La formula vale solo per n = 2: in generale il coefficiente di testa di det(A − tI_{n}) è (−1)^{n}, come si vede più avanti.

## Le matrici triangolari
La terza osservazione (alla lavagna sia nel 2025 sia nel 2024) riguarda le matrici triangolari. Se A è triangolare superiore, con a_{11}, …, a_{nn} sulla diagonale e zeri sotto, anche A − tI_{n} è triangolare superiore: togliere t sulla diagonale non tocca gli zeri. E il determinante di una matrice triangolare è il prodotto degli elementi sulla diagonale (cap. 32). Quindi

p_{A}(t) = (a_{11} − t)(a_{22} − t) ⋯ (a_{nn} − t).

**Proposizione.** Se A ∈ M(n, 𝕂) è triangolare (superiore o inferiore), i suoi autovalori sono gli elementi a_{11}, a_{22}, …, a_{nn} sulla diagonale.

(In parole povere: per una matrice triangolare gli autovalori non si calcolano, si leggono sulla diagonale.)

Per le triangolari inferiori il ragionamento è identico, «non cambia assolutamente niente», dice il docente. Il motivo per cui le radici si leggono subito è quello che chiede alla classe: un polinomio già scritto come prodotto di fattori (t − a) ha come radici proprio quei numeri a, perché un prodotto è nullo se e solo se lo è un fattore; per esempio (t − 3)(t − 2)(t − 5) ha radici 2, 3 e 5 (esempio detto a voce e scritto in un riquadro alla lavagna, registrazione 2025). Il segno non conta: (a − t) e (t − a) hanno la stessa radice a.

**Esempio.** La matrice triangolare superiore ( 1 2 3 ; 0 4 5 ; 0 0 6 ) del cap. 21 ha polinomio caratteristico (1 − t)(4 − t)(6 − t) e quindi autovalori 1, 4 e 6. Anche ( 3 4 ; 0 2 ) del cap. 59 è triangolare: p_{A}(t) = (3 − t)(2 − t), autovalori 3 e 2, come nell'Esempio 17.14 delle dispense. (Il primo esempio è aggiunto per chiarezza.)

Il cap. 32 riportava che all'esame di settembre si dovevano calcolare gli autovalori di una matrice 3 × 3, e che il determinante necessario era proprio quello di una matrice triangolare: ecco perché.

## Il grado del polinomio caratteristico
**Proposizione.** Se A ∈ M(n, 𝕂), il polinomio caratteristico p_{A}(t) è davvero un polinomio, e ha grado esattamente n.

(In parole povere: una matrice 2 × 2 dà un polinomio di secondo grado, una 3 × 3 uno di terzo grado, e così via. Quindi una matrice n × n ha al massimo n autovalori.)

Il docente lo spiega così (registrazione 2025): il determinante di A − tI_{n} è una somma di prodotti di elementi della matrice, ciascuno dei quali è un numero oppure un'espressione del tipo a_{ii} − t; quindi è un polinomio in t. Tra quei prodotti c'è quello degli elementi della diagonale, (a_{11} − t) ⋯ (a_{nn} − t), che contiene il termine (−t)^{n}, e nessun altro prodotto contiene n fattori con t. Il grado è quindi n, e il coefficiente di testa è (−1)^{n}.

Due conseguenze, la seconda aggiunta per chiarezza (non presente nelle dispense né in lezione):
- per il cap. 13 un polinomio di grado n ha al massimo n radici, contate con molteplicità: **una matrice n × n ha al massimo n autovalori**;
- il termine noto è p_{A}(0) = det(A − 0·I_{n}) = det A. In particolare 0 è un autovalore se e solo se det A = 0, cioè se e solo se A non è invertibile, in accordo con il cap. 59 (autovettori di autovalore 0 = vettori non nulli del nucleo).

**Esempio.** Per la matrice 3 × 3 dell'Esempio 17.4 (cap. 59), A = ( 1 1 −1 ; 2 1 1 ; 3 0 2 ), il polinomio caratteristico è di terzo grado:

p_{A}(t) = (2 − t)(t^{2} − 2t + 2).

Il fattore t^{2} − 2t + 2 ha discriminante 4 − 8 = −4 < 0, quindi su ℝ l'unico autovalore è 2, quello dell'autovettore (0, 1, 1) trovato nel cap. 59. (Calcolo non presente nelle dispense né in lezione, controllato con SymPy; si può verificare sviluppando con Laplace, cap. 33.)

## La rotazione: autovalori solo in ℂ
**Esempio dalla lavagna (registrazione 2025).** Il docente chiude la lezione con la rotazione di 90 gradi del cap. 59, Rot(x, y) = (−y, x), per verificare con il polinomio caratteristico che non ha autovalori reali. La matrice associata nella base canonica E (alla lavagna C) ha per colonne le immagini di e_{1} ed e_{2}, perché nella base canonica le coordinate di un vettore sono il vettore stesso (cap. 52):

Rot(e_{1}) = Rot(1, 0) = (0, 1),   Rot(e_{2}) = Rot(0, 1) = (−1, 0),   quindi   A = [Rot]^{E}_{E} = ( 0 −1 ; 1 0 ).

Il polinomio caratteristico è

p_{A}(t) = det( −t  −1 ; 1  −t ) = t^{2} + 1,

e gli autovalori sarebbero i λ con λ^{2} = −1. Nei numeri reali **non ci sono soluzioni**: la rotazione non ha autovalori reali, e quindi nemmeno autovettori, come anticipato geometricamente. Ma se si pensa la stessa matrice come mappa da ℂ² in ℂ², le soluzioni ci sono: λ = i e λ = −i.

**Come sottolineato a lezione (registrazione 2025).** «Diventa importante sapere in quale campo stiamo lavorando»: la stessa matrice ha autovalori su ℂ ma non su ℝ. È qui che si vede l'importanza dei coefficienti complessi: con coefficienti complessi, dice il docente, il polinomio caratteristico ha sempre soluzioni, quindi ci sono sempre autovalori, e di conseguenza autovettori. Il motivo, che a lezione non è nominato, è il teorema fondamentale dell'algebra (cap. 13).

Lo stesso conto vale per la rotazione di un angolo θ qualsiasi, la cui matrice nella base canonica è ( cos θ  −sin θ ; sin θ  cos θ ) (le dispense la studiano più avanti; qui la si usa solo per questo controllo, non presente nelle dispense né in lezione). Con la formula delle 2 × 2, tr A = 2cos θ e det A = cos^{2}θ + sin^{2}θ = 1, quindi

p_{A}(t) = t^{2} − 2cos θ · t + 1,

con discriminante 4cos^{2}θ − 4 = −4sin^{2}θ. È negativo, cioè non ci sono autovalori reali, tranne quando sin θ = 0, cioè θ = 0 o θ = π: proprio i due casi del cap. 59 in cui la rotazione è I_{2} o −I_{2}.

## Matrici simili hanno lo stesso polinomio caratteristico
**Proposizione.** Se A e B sono matrici simili, allora p_{A}(t) = p_{B}(t).

(In parole povere: cambiando base la matrice cambia, ma il polinomio caratteristico no. Quindi gli autovalori appartengono alla trasformazione, non alla base usata per scriverla.)

**Dimostrazione (dalle dispense).** Sia A = M^{−1}BM con M invertibile (è la scrittura delle dispense; nella convenzione del cap. 54 si ha B = PAP^{−1} con P = M). Poiché tI_{n} = t M^{−1}M = M^{−1}(tI_{n})M, si ha A − tI_{n} = M^{−1}BM − M^{−1}(tI_{n})M = M^{−1}(B − tI_{n})M, e per il teorema di Binet (cap. 36)

p_{A}(t) = det(M^{−1}) · det(B − tI_{n}) · det(M) = det(B − tI_{n}) = p_{B}(t),

perché det(M^{−1}) · det(M) = det(M^{−1}M) = det I_{n} = 1. ∎

Alla lavagna questa proprietà non compare. È lo stesso argomento con cui il cap. 54 ha mostrato che matrici simili hanno lo stesso determinante; anzi, il fatto che abbiano la stessa traccia e lo stesso determinante, per le 2 × 2, è proprio un caso particolare, perché sono i due coefficienti di p_{A}. Sui due esempi del cap. 54: ( 1 2 ; 2 1 ) e ( 3 6 ; 0 −1 ) hanno entrambe polinomio (t − 3)(t + 1); ( 1 1 ; 0 −1 ) e ( 1 0 ; 0 −1 ) hanno entrambe (t − 1)(t + 1).

**Il polinomio caratteristico di un endomorfismo.** Grazie alla proposizione, per un endomorfismo T : V → V si può definire il **polinomio caratteristico** p_{T}(t) come quello di una matrice associata A = [T]^{B}_{B}, rispetto a una base B qualsiasi: due matrici associate a T sono simili (cap. 54), quindi il risultato non dipende dalla base scelta. Gli autovalori di T sono le radici di p_{T}(t), perché coincidono con quelli di una sua matrice (cap. 59). Alla lavagna, nella lezione successiva, compare indifferentemente P_{A}(t) o P_{T}(t), con la P maiuscola.

(In parole povere: il polinomio caratteristico di una trasformazione si calcola su una sua matrice qualsiasi; tanto, qualunque base si scelga, il risultato è lo stesso.)

**Attenzione.** Come per traccia e determinante (cap. 54), la proposizione non si inverte: I_{2} e ( 1 1 ; 0 1 ) hanno lo stesso polinomio caratteristico (1 − t)^{2}, ma non sono simili. Il cap. 63 spiega che cosa le distingue.

Conoscere gli autovalori è il primo passo. Il secondo è trovare, per ogni autovalore λ, tutti gli autovettori corrispondenti, cioè risolvere (A − λI_{n})v = 0: è il tema del capitolo successivo.
