# Capitolo 50: Le Matrici nello Heap: Puntatori a Matrici e Allocazione
## Perché allocare una matrice nello heap
Le matrici viste nei capitoli 46-49 sono tutte variabili locali: stanno nello stack frame della funzione che le dichiara, anche quando sono VLA con dimensioni decise durante l'esecuzione. Valgono quindi per le matrici gli stessi limiti degli array visti nel capitolo 41: la loro vita finisce con la funzione, e una funzione non può creare una matrice e consegnarla al chiamante. Per gli array la soluzione è stata lo heap (capitoli 42 e 43). La versione delle slide del 24 novembre aggiunge una sezione, «Matrici nello heap», che fa lo stesso passo per le matrici: prima serve un modo per indicare una matrice con un puntatore, poi la si alloca con una sola `malloc`.

## Una matrice è un array di righe
Si consideri una matrice VLA:

```c
size_t rows = 3, cols = 4;
int m[rows][cols];
```

Come già visto nel capitolo 47, una matrice è un array di righe, e ogni riga è a sua volta un array di `cols` interi, di tipo `int[cols]`. Nelle espressioni il nome `m` viene convertito in un puntatore alla prima riga, cioè a un oggetto di tipo `int[cols]`. Il tipo di questo puntatore si scrive

```c
int (*)[cols]
```

e niente impedisce di dichiarare esplicitamente una variabile di questo tipo.

**Definizione.** Un **puntatore a matrice** è una variabile dichiarata come `int (*p)[cols];`, che si legge: «`p` è un puntatore a uno o più array di `cols` elementi di tipo `int`». Se `p` punta alla prima riga di una matrice, gli elementi si raggiungono con la solita notazione `p[i][j]`.

(In parole povere: un normale `int*` indica una singola casella; un `int (*)[cols]` indica un'intera riga di `cols` caselle. Avanzare di uno con questo puntatore vuol dire saltare alla riga successiva, non alla casella successiva.)

Le parentesi intorno a `*p` sono indispensabili: come già notato nel capitolo 47, `int *p[cols]` dichiarerebbe invece un array di `cols` puntatori a `int`. Le slide indicano proprio la forma `int (*p)[cols]` come quella che si userà per rappresentare una matrice allocata nello heap.

## Perché p[i][j] funziona
La notazione `p[i][j]` funziona per la stessa ragione per cui `a[i]` funziona con un `int*` (capitolo 25). L'espressione `p[i]` vuol dire `*(p + i)`, e l'aritmetica dei puntatori avanza di `i` oggetti del tipo puntato: qui l'oggetto puntato è un'intera riga, quindi `p + i` è l'indirizzo della riga `i`, che si trova `i · cols · sizeof(int)` byte dopo l'inizio. Poi `[j]` sceglie il `j`-esimo intero dentro quella riga. Il risultato è la formula del capitolo 46, base + (i · cols + j) × sizeof(int) (precisazione aggiunta).

Per esempio, con `cols = 4` e interi da 4 byte, `p + 1` sta 16 byte dopo `p` e `p + 2` sta 32 byte dopo; l'elemento `p[2][1]` è il numero 2 · 4 + 1 = 9 della sequenza, cioè sta 36 byte dopo l'inizio. Si vede anche perché nel tipo compare `cols` e non `rows`: per fare il salto da una riga all'altra bisogna sapere quanto è lunga una riga, mentre il numero di righe non serve.

## Allocare una matrice con una sola malloc
Una matrice di rows × cols interi contiene rows · cols elementi contigui (capitolo 46). Per allocarla nello heap basta quindi un unico blocco di `rows * cols * sizeof(int)` byte, e il suo indirizzo si assegna a un puntatore a matrice:

```c
size_t rows = 3, cols = 4;
int (*m)[cols] = malloc(rows * cols * sizeof(int));
```

Il risultato di `malloc` è un `void*` (capitolo 42), che viene convertito senza cast nel tipo di `m`, `int (*)[cols]`: `m` punta alla prima di `rows` righe, ciascuna di `cols` interi. La matrice mantiene la stessa organizzazione in memoria già vista per le matrici nello stack, una riga dopo l'altra, e si usa normalmente con `m[i][j]`.

![La matrice 3 × 4 nello heap: nello stack c'è solo il puntatore m, il blocco contiene le tre righe una dopo l'altra, e m + 1 salta un'intera riga.](figure/prog/matrice_heap.png|15)

Quando la matrice non serve più si libera il blocco e si azzera il puntatore, con la regola del capitolo 42, «ogni `malloc` deve avere una `free` corrispondente»:

```c
free(m);
m = NULL;
```

Basta una sola `free`, perché il blocco è uno solo. Rispetto alla matrice nello stack, l'organizzazione in memoria resta la stessa; secondo le slide, lo heap cambia la **durata** della matrice e la **modalità** con cui viene allocata e rilasciata. La matrice vive finché non si chiama `free`, indipendentemente dalla funzione in cui è stata creata.

## Un esempio completo
Il programma seguente (non nelle slide, costruito con i pezzi delle slide e la funzione `stampaMatrice` del capitolo 47) alloca una matrice 3 × 4, la riempie con i numeri da 0 a 11 nell'ordine di memoria e la stampa:

```c
#include <stdio.h>
#include <stdlib.h>

void stampaMatrice(size_t rows, size_t cols, const int m[rows][cols]);

int main(void) {
    size_t rows = 3, cols = 4;
    int (*m)[cols] = malloc(rows * cols * sizeof(int));
    if (m != NULL) {
        for (size_t i = 0; i < rows; i++) {
            for (size_t j = 0; j < cols; j++) {
                m[i][j] = i * cols + j;   // posizione nella sequenza lineare
            }
        }
        stampaMatrice(rows, cols, m);
        free(m);
        m = NULL;
    }
}
```

L'uscita è:

```
[ 0 1 2 3 ]
[ 4 5 6 7 ]
[ 8 9 10 11 ]
```

La definizione di `stampaMatrice` è quella del capitolo 47, da scrivere dopo `main`. Tre osservazioni. Il controllo `m != NULL` va fatto prima di usare il blocco, come per gli array (capitolo 42): la slide della `malloc` non lo mostra, ma la funzione `leggiMatrice` del capitolo 51 lo fa. Il valore `i * cols + j` è un `size_t` che viene convertito in `int` nell'assegnamento, senza problemi finché è piccolo. Soprattutto, `stampaMatrice` riceve `m` senza alcuna modifica: un parametro scritto `const int m[rows][cols]` è in realtà un puntatore a matrice, cioè alla prima di una serie di righe di `cols` interi (capitolo 47), quindi alla funzione non importa se la matrice sta nello stack o nello heap. Tutte le funzioni dei capitoli 47-49 funzionano anche con le matrici allocate dinamicamente.

## Matrice nello stack e matrice nello heap
Il confronto tra le due forme riassume il capitolo:

- `int m[rows][cols];` riserva la matrice nello stack frame; la memoria viene liberata in automatico al ritorno della funzione;
- `int (*m)[cols] = malloc(rows * cols * sizeof(int));` riserva la matrice nello heap; nello stack c'è solo il puntatore `m`, e la memoria resta occupata fino a `free(m)`;
- in entrambi i casi gli elementi sono contigui, disposti per righe, e si raggiungono con `m[i][j]`;
- in entrambi i casi `m`, nelle espressioni, è un puntatore alla prima riga, di tipo `int (*)[cols]`.

(In parole povere: la tabella è identica, cambia solo chi la tiene in vita. Nello stack la butta via il sistema quando la funzione finisce; nello heap resta finché il programmatore non la restituisce con `free`.)

## Riepilogo
- Una matrice è un array di righe; un puntatore alla prima riga ha tipo `int (*)[cols]` e si dichiara con `int (*p)[cols];`, con le parentesi.
- Con un puntatore a matrice si usa normalmente `p[i][j]`: `p + i` salta `i` righe intere, per questo nel tipo serve `cols`.
- Una matrice nello heap si alloca con una sola `malloc(rows * cols * sizeof(int))` e si libera con una sola `free`.
- La forma in memoria non cambia; cambiano la durata e la gestione, che diventano manuali.
- Le funzioni scritte per le matrici con parametro `m[rows][cols]` accettano anche le matrici nello heap.

Il capitolo 51 affronta l'ultimo passo: scrivere una funzione che legge una matrice, la alloca nello heap e la restituisce al chiamante.
