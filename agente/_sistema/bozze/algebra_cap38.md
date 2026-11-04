# 38. I Sistemi Lineari: Definizioni e Mosse di Gauss
## Che cos'è un sistema lineare
Con le matrici a disposizione si può affrontare uno dei problemi centrali dell'algebra lineare: risolvere più equazioni lineari insieme. È l'argomento delle lezioni 11, 12 e 13 (Sistemi Lineari I, II e III).

**Definizione.** Un **sistema lineare** è un insieme di k equazioni lineari in n variabili:
a_{11}x_{1} + … + a_{1n}x_{n} = b_{1}, … , a_{k1}x_{1} + … + a_{kn}x_{n} = b_{k}.
I numeri a_{ij} sono i **coefficienti** e i b_{i} sono i **termini noti**; coefficienti, termini noti e variabili stanno tutti in uno stesso campo 𝕂 fissato.

(In parole povere: è una lista di condizioni, ognuna fatta solo di variabili moltiplicate per numeri e sommate tra loro, senza x², xy o simili. Risolvere vuol dire trovare i valori che le soddisfano tutte insieme.)

I dati si raggruppano in una matrice k × n e in un vettore colonna: A = (a_{ij}) è la **matrice dei coefficienti** e b = (b_{1}, …, b_{k}), scritto in colonna, è il **vettore dei termini noti**. Si può poi unire tutto in un'unica matrice k × (n + 1), C = (A | b), chiamata **matrice completa**. Per esempio, il sistema x + y + 2z = 9, 2x + 4y − 3z = 1, 3x + 6y − 5z = 0 ha

C = ( 1 1 2 | 9 ; 2 4 −3 | 1 ; 3 6 −5 | 0 ).

(In parole povere: la matrice completa è il sistema scritto senza le lettere: ogni riga è un'equazione, ogni colonna una variabile, e l'ultima colonna contiene i termini noti.)

**Definizione.** Una **soluzione** del sistema è un'assegnazione di valori alle variabili x_{1}, …, x_{n} che soddisfa **tutte** le equazioni. Lo scopo è determinare l'insieme S ⊂ 𝕂ⁿ delle soluzioni.

(In parole povere: non basta che i numeri vadano bene per una sola equazione: devono andare bene per tutte nello stesso momento.)

**Esempio dalla lavagna (registrazione 2025).** Il sistema x_{1} + x_{2} + x_{3} = 6, x_{1} + x_{2} − x_{3} = 0 ha come soluzione x_{1} = 1, x_{2} = 2, x_{3} = 3, perché 1 + 2 + 3 = 6 e 1 + 2 − 3 = 0. Il docente osserva a voce che non è l'unica e che ce ne sono infinite; facendo il conto, sono tutti i vettori (3 − s, s, 3). Qui

A = ( 1 1 1 ; 1 1 −1 ),   b = ( 6 ; 0 ),   C = ( 1 1 1 | 6 ; 1 1 −1 | 0 ).

La sbarra in (A | b) è solo una comodità grafica per ricordare dove finiscono i coefficienti.

## Le mosse di Gauss
Esistono alcune operazioni che cambiano la matrice C senza modificare l'insieme S delle soluzioni.

**Definizione.** Le **mosse di Gauss** sulle righe di C (R_{i} è la i-esima riga) sono:
- (I) scambiare due righe: R_{i} ↔ R_{j};
- (II) moltiplicare una riga per un numero λ ≠ 0: R_{i} → λR_{i};
- (III) aggiungere a una riga un'altra riga moltiplicata per un λ qualsiasi: R_{i} → R_{i} + λR_{j}, con j ≠ i.

(In parole povere: sono le stesse cose che si fanno a mano con le equazioni: cambiare l'ordine, moltiplicare tutta un'equazione per un numero, sommare un'equazione a un'altra.)

Sono le mosse già incontrate per il determinante (cap. 35), con due differenze: qui nella mossa (II) serve λ ≠ 0, e si usano le **righe**, perché ogni riga è un'equazione mentre ogni colonna corrisponde a una variabile.

Un esempio di composizione di mosse dei tre tipi:

( 1 2 ; 3 0 ; 4 −2 ) → (R_{1} ↔ R_{3}) → ( 4 −2 ; 3 0 ; 1 2 ) → (R_{1} → ½R_{1}) → ( 2 −1 ; 3 0 ; 1 2 ) → (R_{2} → R_{2} + 2R_{3}) → ( 2 −1 ; 5 4 ; 1 2 ).

**Esempio dalla lavagna (registrazione 2025).** Una mossa sulla matrice è la stessa mossa fatta sulle equazioni. Nel sistema di prima, R_{1} → R_{1} + R_{2} somma le due equazioni:

2x_{1} + 2x_{2} = 6, x_{1} + x_{2} − x_{3} = 0   corrisponde a   ( 2 2 0 | 6 ; 1 1 −1 | 0 ).

La strategia è quindi: si passa dal sistema alla matrice, si fanno le mosse sulla matrice, e alla fine si torna al sistema, che ha le stesse soluzioni ma è più semplice.

## Perché le mosse non cambiano le soluzioni
**Proposizione.** Le mosse di Gauss su C = (A | b) non cambiano l'insieme S ⊂ 𝕂ⁿ delle soluzioni del sistema lineare.

(In parole povere: dopo una mossa il sistema ha un aspetto diverso, ma i numeri che lo risolvono sono esattamente gli stessi: si può semplificarlo senza perdere né aggiungere soluzioni.)

**Dimostrazione.** La mossa (I) scambia due equazioni, e questo chiaramente non tocca S. La mossa (II) moltiplica un'equazione a_{i1}x_{1} + … + a_{in}x_{n} = b_{i} per una costante λ ≠ 0, trasformandola in λa_{i1}x_{1} + … + λa_{in}x_{n} = λb_{i}: anche qui le soluzioni sono le stesse di prima. Qui serve λ ≠ 0: moltiplicando per 0 l'equazione diventerebbe 0 = 0 e si perderebbe una condizione.

La mossa (III) cambia le due equazioni

a_{i1}x_{1} + … + a_{in}x_{n} = b_{i},   a_{j1}x_{1} + … + a_{jn}x_{n} = b_{j}

con

(a_{i1} + λa_{j1})x_{1} + … + (a_{in} + λa_{jn})x_{n} = b_{i} + λb_{j},   a_{j1}x_{1} + … + a_{jn}x_{n} = b_{j}.

Se x è soluzione delle prime due, sommando alla prima la seconda moltiplicata per λ si vede che è soluzione delle altre due; viceversa, se è soluzione delle seconde due, basta sottrarre λ volte la seconda equazione dalla prima per tornare al sistema di partenza. Quindi x ∈ 𝕂ⁿ è soluzione delle prime due se e solo se è soluzione delle seconde due.
