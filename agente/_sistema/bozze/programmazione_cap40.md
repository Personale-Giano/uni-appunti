# Capitolo 40: L'Ordinamento con Bubble Sort
## Che cos'è un algoritmo di ordinamento
**Definizione.** Un **algoritmo di ordinamento** è una procedura che prende in input un array di elementi di un dominio ordinabile e produce in output lo stesso array con gli elementi riorganizzati in un ordine prefissato, per esempio crescente o decrescente.

(In parole povere: una ricetta per mettere in fila le cose, come ordinare un mazzo di carte dalla più bassa alla più alta.)

**Definizione.** Il **Bubble Sort** (ordinamento a bolla) è un algoritmo di ordinamento semplice e didattico, basato su confronti e scambi ripetuti tra coppie di elementi adiacenti. Prende un array `a` di lunghezza `aLen` e lo manipola **in-place**: gli elementi vengono modificati tramite scambi, senza costruire un altro array in cui copiare i dati.

(In parole povere: guardi le coppie di vicini da sinistra a destra e scambi quelle fuori posto; i valori grandi «salgono» verso destra come bolle, e ripeti finché nessuno è più fuori posto.)

In uscita gli elementi sono in ordine non decrescente, a[0] ≤ a[1] ≤ … ≤ a[aLen-1], cioè vale la proprietà ∀i ∈ [1, aLen) : a[i-1] ≤ a[i] del capitolo 39.

## La strategia
L'algoritmo si svolge in **fasi** successive. In ogni fase si esegue un ciclo di confronti e possibili scambi: per ciascun indice i ∈ [1, aLen) si confronta la coppia (a[i-1], a[i]) e, se a[i-1] > a[i], i due elementi vengono scambiati. Alla fine di una fase:
- se è stato fatto almeno uno scambio, si è trovato e corretto almeno un controesempio: l'array è stato modificato e si avvia una nuova fase;
- se non è avvenuto nessuno scambio, non c'è alcun controesempio: tutte le coppie adiacenti soddisfano a[i-1] ≤ a[i], l'array è ordinato e l'algoritmo termina.

![Il Bubble Sort su {6, 2, -8, 10, 4}. In rosso le coppie scambiate, in verde quelle confrontate e lasciate come sono. Nella terza fase non ci sono scambi.](figure/prog/bubble_fasi.png|15)

## Il codice
Il confronto con scambio riusa la funzione `swap` con i puntatori del capitolo 32. Una fase memorizza se ha fatto scambi in una variabile sentinella, e l'iterazione sulle fasi continua finché l'array non risulta ordinato:

```c
#include <stdio.h>
#include <stdbool.h>

// funzione di scambio con passaggio per puntatore
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
                swap(&a[i-1], &a[i]);
                // trovato e corretto un controesempio:
                // sarà necessaria una nuova fase
                ordinato = false;
            }
        }
    }
}

#define LEN 5
int main(void) {
    int v[LEN] = {6, 2, -8, 10, 4};
    bubbleSort(LEN, v);
    printf("Array ordinato:\n");
    for (size_t i = 0; i < LEN; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");
}
```

La variabile `ordinato` è una sentinella per l'**uscita anticipata** (~early termination~): senza di essa si dovrebbero effettuare sempre `aLen-1` fasi. Il programma stampa `Array ordinato:` e, a capo, `-8 2 4 6 10`.

## Lo stack durante l'esecuzione
Con `v = {6, 2, -8}` lo stack mette insieme tutto quello che si è visto sulle chiamate. Nel momento in cui `swap` sta scambiando i primi due elementi, partendo dagli indirizzi più alti si trovano: l'array `v` di `main`; il record di attivazione di `bubbleSort`, con `aLen = 3`, `a` (che contiene l'indirizzo di `v`: un array passato a funzione non viene copiato), i dati di controllo, le locali `ordinato` e `i = 1`; il record di attivazione di `swap`, con `x` e `y` che contengono gli indirizzi di `a[0]` e `a[1]`, i dati di controllo e la locale `temp = 6`.

Le assegnazioni `*x = *y;` e `*y = temp;` scrivono direttamente nelle celle di `v`, due livelli più su nello stack: è per questo che l'ordinamento resta anche dopo il ritorno. Dopo la prima fase `v` vale {2, -8, 6}, dopo la seconda {-8, 2, 6}, e la terza non fa scambi.

## Bubble Sort come test d'ipotesi
L'algoritmo si può leggere come la combinazione di due componenti: il ciclo di confronti e possibili scambi, e un test d'ipotesi che verifica la proprietà di ordine:
- **H₀** (ipotesi iniziale della fase): ∀i∈[1, aLen) : a[i-1] ≤ a[i], l'array è già ordinato. Corrisponde all'inizializzazione `ordinato = true`;
- **H₁** (ipotesi alternativa): ∃i∈[1, aLen) : ¬(a[i-1] ≤ a[i]), esiste almeno una coppia adiacente non in ordine. Si determina con la scansione su tutte le coppie.

Quando durante una fase avviene almeno uno scambio, si è trovato un controesempio a H₀ e l'array è stato modificato: serve una nuova fase sul nuovo stato. Se nessuno scambio avviene, l'intera scansione non ha trovato controesempi, H₀ è verificata e l'algoritmo termina.

## Esercizio
Dopo ogni fase gli elementi più grandi si sono spostati verso destra. Tracciando l'**ultima posizione di scambio** della fase (`new_last`) si sa che oltre quel punto gli elementi sono già in ordine, quindi la fase successiva può limitarsi a confrontare le coppie solo fino a lì: se `last` è il limite delle coppie da confrontare, a ogni nuova fase si pone `last = new_last`. L'esercizio chiede di modificare `bubbleSort` in questo modo.
