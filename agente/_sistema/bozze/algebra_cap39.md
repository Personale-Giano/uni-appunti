# 39. Gli Algoritmi di Gauss e di Gauss-Jordan
## Le matrici a scalini
L'idea è usare le mosse di Gauss per portare la matrice in una forma in cui il sistema si legge quasi da solo.

**Definizione.** Per ogni riga R_{i} di una matrice C, il **pivot** è il primo elemento non nullo della riga. Una **matrice a scalini** è una matrice in cui tutte le righe nulle sono in fondo e il pivot di ogni riga non nulla è strettamente più a destra del pivot della riga non nulla precedente.

(In parole povere: leggendo dall'alto verso il basso, ogni riga comincia con più zeri della precedente, così gli elementi non nulli disegnano una scala che scende verso destra.)

![Una matrice a scalini: i pivot sono in rosso e la linea segna gli scalini.](figure/alg/matrice_scalini.png|8.5)

Per esempio sono a scalini ( 1 0 5 ; 0 −1 −1 ) e ( 7 −2 9 ; 0 0 1 ; 0 0 0 ). Non lo sono invece ( 1 2 −1 ; 4 0 6 ; 0 7 0 ), perché sotto il primo pivot c'è un 4, e ( 0 8 ; 0 1 ; 0 0 ; 0 0 ), perché il pivot della seconda riga sta nella stessa colonna di quello della prima: «strettamente più a destra» vuol dire proprio che non ci sono mai due pivot uno sopra l'altro. Alla lavagna (registrazione 2025) l'esempio è ( 1 2 3 4 ; 0 5 6 7 ; 0 0 0 8 ).

**Definizione.** Una matrice a scalini è **ridotta** se ogni pivot è uguale a 1 e tutti i valori sopra i pivot sono uguali a 0.

(In parole povere: è la versione più pulita possibile: nelle colonne dei pivot c'è un 1 e tutto il resto è zero, quindi il sistema si legge a occhio.)

Per esempio (lavagna, registrazione 2025) sono ridotte ( 1 0 0 4 ; 0 1 0 3 ; 0 0 1 5 ) e ( 1 0 1 0 4 ; 0 1 1 0 3 ; 0 0 0 1 5 ).

## L'algoritmo di Gauss
L'**algoritmo di Gauss** trasforma qualsiasi matrice C in una matrice a scalini usando le tre mosse. Funziona così:
1. Se C_{11} = 0 e C_{i1} ≠ 0 per qualche i, si scambia la prima riga con quella riga, in modo da ottenere C_{11} ≠ 0. Se invece C_{i1} = 0 per ogni i, si ricomincia dal punto 1 lavorando sulla sottomatrice ottenuta togliendo soltanto la prima colonna.
2. Per ogni riga R_{i} con i ≥ 2 e C_{i1} ≠ 0, si sostituisce R_{i} con R_{i} − (C_{i1}/C_{11}) R_{1}. In questo modo la nuova riga ha C_{i1} = 0.
3. Ora C_{i1} = 0 per ogni i ≥ 2. Si ricomincia dal punto 1 lavorando sulla sottomatrice ottenuta togliendo la prima riga e la prima colonna.

(In parole povere: si sistema una colonna alla volta: si mette un numero non nullo in cima, lo si usa per azzerare tutto ciò che sta sotto, poi si dimentica quella riga e quella colonna e si ripete sul resto.)

Nella registrazione 2025 lo schema è un diagramma di flusso: «C_{11} ≠ 0?»; se no, si scambia R_{1} con la riga del primo elemento non nullo della colonna; se sì, si usa la mossa (III) per «uccidere» i termini sotto il pivot, si tolgono la prima riga e la prima colonna e si ricomincia. La riga che si aggiunge è sempre quella del pivot su cui si sta lavorando. A voce aggiunge che una colonna tutta nulla si salta: nel diagramma questo caso non è scritto.

**Esempio.** Partiamo da C = ( 0 1 1 0 ; 1 1 2 −3 ; −1 2 1 1 ). Poiché C_{11} = 0, si scambiano R_{1} e R_{2}:

( 1 1 2 −3 ; 0 1 1 0 ; −1 2 1 1 ).

Ora C_{31} ≠ 0: con R_{3} → R_{3} + R_{1} si ottiene C_{31} = 0:

( 1 1 2 −3 ; 0 1 1 0 ; 0 3 3 −2 ).

La prima riga e la prima colonna sono a posto, quindi si lavora sul resto. Poiché C_{32} ≠ 0, con R_{3} → R_{3} − 3R_{2} si ottiene:

( 1 1 2 −3 ; 0 1 1 0 ; 0 0 0 −2 ).

La matrice è a scalini e l'algoritmo termina.

## L'algoritmo di Gauss-Jordan
Dopo la riduzione a scalini è utile fare altre mosse, per ottenere altre due cose: **zeri sopra i pivot**, con mosse di tipo (III), aggiungendo alle righe precedenti la riga del pivot moltiplicata per una costante opportuna; e **tutti i pivot uguali a 1**, con mosse di tipo (II).

**Definizione.** L'**algoritmo di Gauss-Jordan** consiste in due fasi: (1) trasformare la matrice a scalini con l'algoritmo di Gauss; (2) ottenere solo zeri sopra i pivot con mosse (III) e tutti i pivot uguali a 1 con mosse (II). Il risultato è una matrice a scalini ridotta.

(In parole povere: Gauss scende e azzera sotto i pivot; Jordan risale e azzera anche sopra, poi divide ogni riga per il suo pivot. Alla fine ogni colonna con un pivot ha un 1 e zeri in tutte le altre caselle.)

Nella registrazione 2025 il nome «Gauss-Jordan» indica solo la seconda fase, che parte da una matrice già a scalini, e il diagramma di flusso fissa un ordine: **si parte dall'ultimo pivot**, si azzera sopra con la mossa (III), si toglie quel pivot dalla lista e si passa al precedente; solo quando i pivot sono finiti si usa la mossa (II) per renderli uguali a 1.

Continuando l'esempio: nella matrice ottenuta C_{12} ≠ 0, quindi con R_{1} → R_{1} − R_{2} si ha ( 1 0 1 −3 ; 0 1 1 0 ; 0 0 0 −2 ). Poi C_{14} ≠ 0, quindi con R_{1} → R_{1} − (3/2)R_{3} si ha ( 1 0 1 0 ; 0 1 1 0 ; 0 0 0 −2 ). Infine i pivot C_{11} e C_{22} valgono già 1, mentre C_{34} = −2: dividendo la terza riga per −2 si arriva a

( 1 0 1 0 ; 0 1 1 0 ; 0 0 0 1 ).

Seguendo invece l'ordine del diagramma si parte dal pivot −2: R_{1} → R_{1} − (3/2)R_{3}, poi R_{1} → R_{1} − R_{2}, infine R_{3} → −½R_{3}. Il risultato è la stessa matrice.

**Un altro esempio.** Sopra ogni freccia c'è la mossa usata:

( 1 −1 3 ; 0 2 2 ; 1 0 4 ) → (R_{3} → R_{3} − R_{1}) → ( 1 −1 3 ; 0 2 2 ; 0 1 1 ) → (R_{3} → R_{3} − ½R_{2}) → ( 1 −1 3 ; 0 2 2 ; 0 0 0 ) → (R_{1} → R_{1} + ½R_{2}) → ( 1 0 4 ; 0 2 2 ; 0 0 0 ) → (R_{2} → ½R_{2}) → ( 1 0 4 ; 0 1 1 ; 0 0 0 ).

La seconda fase serve perché la matrice finale permette di scrivere subito le soluzioni, come si vede nel prossimo capitolo.
