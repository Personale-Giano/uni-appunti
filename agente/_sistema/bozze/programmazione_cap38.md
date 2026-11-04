# Capitolo 38: La Selezione e il Modello Dimensione-Capacità
## La selezione
**Definizione.** Dato un array `b` di lunghezza `bLen` e una condizione Cond(⋅), la **selezione** (o filtraggio, estrazione condizionata, copia con filtro) copia in un altro array `a` tutti e soli gli elementi `b[i]` che soddisfano Cond(b[i]), mantenendo l'ordine originale: a = [ b[i] | i∈[0, bLen) ∧ Cond(b[i]) ].

(In parole povere: è come passare un mazzo di carte e tenere, nello stesso ordine, solo quelle che ti interessano.)

Per esempio, con `bLen = 3`, `b = { 18, 9, 30 }` e la condizione «maggiore o uguale a 18», in `a` finiscono 18 e 30. Gli elementi copiati **non conservano gli stessi indici**: 30 sta in `b[2]` ma finisce in `a[1]`. Servono quindi **due indici**: `i ∈ [0, bLen)` per la scansione di `b`, e `j` per inserire in `a` (nel codice qui sotto `j` è la variabile `aLen`). La dimensione finale di `a` è il numero di elementi di `b` che soddisfano Cond.

## Dimensione e capacità
Nell'esempio `a` è stato allocato per contenere fino a `bLen` elementi, ma dopo la selezione solo una parte è valida. Bisogna quindi separare due concetti.

**Definizione.** La **capacità** di un array è il numero massimo di elementi che può contenere; la **dimensione effettiva** è quanti elementi validi contiene in quel momento.

(In parole povere: la capacità è quanti posti ha la sala, la dimensione è quante persone sono sedute adesso.)

Con una capacità `AMAX` e una dimensione `aLen` valgono queste proprietà:
- gli indici **validi** sono [0, AMAX);
- gli indici degli elementi **inizializzati** sono [0, aLen), quindi per un indice di un elemento inizializzato vale 0 ≤ i < aLen;
- gli indici degli elementi **non inizializzati**, cioè disponibili, sono [aLen, AMAX).

![Il modello dimensione-capacità con AMAX = 10 e aLen = 6.](figure/prog/dimensione_capacita.png|15)

Si può quindi alterare `aLen` per inserire o rimuovere elementi **in fondo** all'array, rispettando il vincolo 0 ≤ aLen ≤ AMAX. La lunghezza si comporta come un cursore del volume, che può scorrere tutti i valori dell'intervallo [0, AMAX].

Il modello si dichiara in due modi:
- con **capacità prefissata**: `size_t aLen` per la dimensione, `#define AMAX ...` per la capacità, `int a[AMAX]` per l'array;
- con **capacità variabile** (VLA): `size_t aLen` per la dimensione, `size_t aCap` per la capacità, `int a[aCap]` per l'array.

## La selezione con il modello
```c
// array b (sorgente): bLen elementi già presenti
// array a (destinazione)
size_t aCap = bLen;
int a[aCap];
size_t aLen = 0; // gli elementi di a partono non inizializzati

// SELEZIONE
for (size_t i = 0; i < bLen && aLen < aCap; i++) {
    if (Cond(b[i])) {   // seleziona da b
        a[aLen] = b[i]; // copia da b ad a
        aLen++;
    }
}
// alla fine del ciclo aLen è il numero di elementi selezionati e copiati
```

`aLen` indica sempre la prima posizione libera. Nelle slide `b` è scritto schematicamente come `int b[bLen] = ...`: un array a lunghezza variabile però non si può inizializzare così in C, quindi `b` va riempito con un ciclo oppure dichiarato con dimensione costante (precisazione aggiunta).

## Passare il modello a una funzione
Quali parametri servono dipende da ciò che fa la funzione:
- se **non modifica la dimensione**, come per un array normale: `const size_t aLen, int a[]`;
- se **altera la dimensione**: `size_t *p_aLen, const size_t aCap, int a[]`.

Passando la lunghezza come puntatore `p_aLen`, la funzione può cambiare la dimensione, rispettando 0 ≤ \*p_aLen ≤ aCap, e comunicarla al chiamante (capitolo 32).

(In parole povere: se la funzione aggiunge o toglie elementi, deve poter aggiornare il «contatore» del chiamante, quindi le serve il suo indirizzo.)

## Esercizio: selezione per intervalli
**selectInRange** copia in ordine in `a` tutti e soli gli elementi di `b` che appartengono all'intervallo chiuso [minVal, maxVal]. La dimensione finale di `a` è il numero di elementi selezionati. Ritorna `true` se l'operazione è andata a buon fine, `false` se `aCap` non basta a contenere tutte le occorrenze: in quel caso copia il più possibile fino a saturare `aCap` e segnala il problema, un **overflow logico**, con il `false`.

```c
bool selectInRange(size_t bLen, const int b[],
                   size_t aCap, size_t *p_aLen, int a[],
                   int minVal, int maxVal);
```

Le precondizioni sono: se `bLen > 0` allora `b != NULL`; `a != NULL` e `p_aLen != NULL`; `aCap` è la capacità di `a`; il valore iniziale di `*p_aLen` è irrilevante, perché viene impostato subito a zero.

La traccia di implementazione usa una variabile sentinella `overflow`: per ogni elemento nell'intervallo, se c'è spazio lo copia e incrementa `aLen`, altrimenti mette `overflow` a vero, e usa `i < bLen && !overflow` come condizione del ciclo. A fine scansione assegna `*p_aLen = aLen`. Una possibile soluzione (non presente nelle slide):

```c
bool selectInRange(size_t bLen, const int b[],
                   size_t aCap, size_t *p_aLen, int a[],
                   int minVal, int maxVal) {
    size_t aLen = 0;
    bool overflow = false;
    for (size_t i = 0; i < bLen && !overflow; i++) {
        if (minVal <= b[i] && b[i] <= maxVal) {
            if (aLen < aCap) {
                a[aLen] = b[i];
                aLen++;
            }
            else {
                overflow = true;
            }
        }
    }
    *p_aLen = aLen;
    return !overflow;
}
```

Le prove fornite coprono i casi significativi: `{5, 7, 9}` con intervallo [-2, 0] non seleziona nulla e dà `true` con `aLen == 0`; `{-3, 0, 2, 2, 8}` con [0, 2] dà `true` e `{0, 2, 2}`, con l'ordine preservato; `{1, 2, 3, 4}` con [1, 4] e `aCap == 2` dà `false` e copia `{1, 2}`; un array vuoto dà `true` con `aLen == 0`.
