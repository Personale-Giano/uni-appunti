# Capitolo 43: Restituire un Array Allocato nello Heap
## leggiArray con malloc
Il problema «impossibile» del capitolo 41 si risolve cambiando la riga che alloca l'array e aggiungendo la `free` in `main`: l'array non si dichiara più come VLA nello stack, ma si alloca nello heap con `malloc` (capitolo 42).

```c
#include <stdlib.h>
#include <stdio.h>

int* leggiArray(size_t* out_n) {
    size_t n;
    scanf("%zu", &n);
    int* a = malloc(n * sizeof(int));
    for (size_t i = 0; i < n; i++)
        scanf("%d", &a[i]);
    *out_n = n;
    return a;
}

int main(void) {
    size_t aLen;
    int* a = leggiArray(&aLen);
    for (size_t i = 0; i < aLen; i++)
        printf("a[%zu] = %d\n", i, a[i]);
    free(a); a = NULL;
}
```

Rispetto alla versione sbagliata, dentro la funzione `a` non è più un array ma un **puntatore**: una variabile locale che contiene l'indirizzo di un blocco che sta altrove. Il resto del codice non cambia, perché `a[i]` e `&a[i]` si scrivono allo stesso modo.

## L'esecuzione passo per passo
Con lo stesso input di prima, `3` e poi `10 20 30`:

- in `main` vengono allocate nello stack `aLen` e `a`, non inizializzate;
- la chiamata costruisce il record di attivazione di `leggiArray`: valore di ritorno, parametro `out_n` con l'indirizzo di `aLen`, dati di controllo, variabile locale `n`;
- dopo la prima `scanf`, `n` vale 3;
- `malloc(n * sizeof(int))` riserva **nello heap** un blocco di `3 * sizeof(int)` byte, non inizializzati, e ne restituisce l'indirizzo, che finisce nella variabile locale `a`. Nello stack frame c'è solo il puntatore; i tre interi sono nello heap;
- il ciclo scrive 10, 20 e 30 nel blocco, e `*out_n = n;` mette 3 in `aLen`;
- `return a;` copia nel valore di ritorno **l'indirizzo del blocco**;
- al ritorno lo stack frame di `leggiArray` viene deallocato: spariscono `n`, `out_n` e la variabile locale `a`. Il blocco nello heap invece **resta dov'è**, e il suo indirizzo viene assegnato alla variabile `a` di `main`.

![La memoria dopo il ritorno di leggiArray: il puntatore nello stack di main, i dati nello heap.](figure/prog/leggi_array_heap.png|14)

Il ciclo di stampa legge quindi dati validi, e il programma stampa:

```
a[0] = 10
a[1] = 20
a[2] = 30
```

L'ultima riga di `main`, `free(a); a = NULL;`, restituisce il blocco allo heap e azzera il puntatore.

## Che cosa è cambiato
In entrambe le versioni la funzione restituisce un indirizzo e in entrambe la variabile locale `a` muore al ritorno. La differenza sta in **dove vivono i dati puntati**: nella versione sbagliata erano nello stack frame della funzione, che viene demolito; qui sono in un blocco dello heap, la cui vita non dipende da nessuno stack frame. Un blocco allocato con `malloc` rimane valido finché non viene chiamata la `free` corrispondente, in qualunque funzione ci si trovi.

(In parole povere: la funzione non consegna più un biglietto con scritto «guarda nella mia stanza», che intanto è stata sgomberata, ma la chiave di un box in affitto che resta al chiamante.)

Questo ha un prezzo: nessuno libera il blocco in automatico. La funzione `leggiArray` lo crea, ma è `main` che lo usa e che quindi deve chiamare `free` quando ha finito. Dimenticarsene non dà errori visibili, ma lascia il blocco occupato fino alla fine del programma: è il problema dei ~memory leak~ del capitolo 44.

## Due casi lasciati scoperti
Il codice dell'esempio è volutamente essenziale, e non controlla due situazioni (precisazione aggiunta).

La prima è il fallimento dell'allocazione: se `malloc` restituisce `NULL`, il ciclo di lettura scrive attraverso il puntatore nullo. Una versione più robusta controlla il risultato e, se l'allocazione non riesce, comunica al chiamante una sequenza vuota:

```c
int* leggiArray(size_t* out_n) {
    size_t n;
    scanf("%zu", &n);
    int* a = malloc(n * sizeof(int));
    if (a == NULL) {
        *out_n = 0;
        return NULL;
    }
    for (size_t i = 0; i < n; i++)
        scanf("%d", &a[i]);
    *out_n = n;
    return a;
}
```

In questo caso `main` trova `aLen == 0`, non esegue il ciclo di stampa e chiama `free(NULL)`, che per lo standard del C non fa nulla.

La seconda è `n == 0`: la chiamata `malloc(0)` può restituire `NULL` oppure un indirizzo che non va dereferenziato, a seconda del sistema. In entrambi i casi i due cicli non eseguono iterazioni e la `free` finale resta corretta, quindi il programma funziona anche sulla sequenza vuota.
