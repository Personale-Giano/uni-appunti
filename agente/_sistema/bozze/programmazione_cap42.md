# Capitolo 42: Lo Heap e l'Allocazione Dinamica con malloc e free
## Lo heap
**Definizione.** Lo **heap** è un'area di memoria gestita manualmente dal programmatore: l'allocazione avviene chiamando funzioni di libreria (`malloc`, `calloc`, `realloc`) e la deallocazione è esplicita, con la funzione `free`.

(In parole povere: lo stack è un tavolo che viene sparecchiato da solo alla fine di ogni funzione; lo heap è un magazzino in cui si prende uno scaffale quando serve e lo si tiene finché non lo si restituisce di persona.)

**Definizione.** La memoria dello heap si dice **memoria dinamica** perché non è fissata a ~compile-time~, come quella delle variabili globali o statiche, e non è allocata automaticamente a ~runtime~, come lo stack: viene allocata e liberata «su richiesta» dal programma durante l'esecuzione.

(In parole povere: è memoria «a domanda». Il programma decide mentre gira quanta gliene serve e per quanto tempo.)

Il termine risale agli anni '70, quando «dinamico» voleva dire «allocato a runtime», in contrasto con «statico», cioè allocato a compile-time; oggi si direbbe piuttosto ~on-demand~ o «gestito dal programma». Tra gli esempi di memoria fissata a compile-time le slide citano le stringhe letterali e gli «array const»: vale per le stringhe letterali e per gli array globali, mentre un array `const` dichiarato dentro una funzione resta una normale variabile locale nello stack (precisazione aggiunta).

## I segmenti della memoria
Il modello della memoria visto finora distingueva l'area del codice e l'area dati, con lo stack nella parte alta dell'area dati (capitolo 7). Ora l'area dati si precisa: oltre allo stack contiene i dati statici e lo heap. Nel modello generale, semplificato, la memoria è divisa in quattro **segmenti** distinti:

- **Code segment**: contiene le istruzioni del programma;
- **Data segment**: contiene le variabili globali e statiche;
- **Heap**: l'area della memoria dinamica; per convenzione si assume che cresca verso l'alto, cioè verso gli indirizzi crescenti;
- **Stack**: l'area delle variabili automatiche, che cresce verso il basso.

![Il modello semplificato della memoria con i quattro segmenti.](figure/prog/segmenti_memoria.png|14)

Codice e dati statici sono fissi per tutta l'esecuzione, mentre stack e heap condividono lo spazio libero che sta in mezzo, crescendo l'uno verso l'altro.

## Allocare: malloc
```c
#include <stdlib.h>
void* malloc(size_t sz);
```

**Definizione.** La funzione `malloc`, dichiarata in `<stdlib.h>`, alloca `sz` byte **contigui** nello heap e restituisce un puntatore al primo byte del blocco allocato. Se la memoria non è disponibile restituisce `NULL`. I byte del blocco **non sono inizializzati**.

(In parole povere: si chiede «mi servono tot byte», e `malloc` risponde con l'indirizzo in cui cominciano, oppure con `NULL` se non ce ne sono. Dentro si trova quello che c'era prima: valori sporchi.)

Il tipo di ritorno `void*` è un puntatore a una zona di memoria a cui non è ancora stato assegnato un tipo. Il tipo si dà assegnando il risultato a un puntatore del tipo voluto, oppure con un cast, che in C non è necessario:

```c
int* a = malloc(n * sizeof(int));
if (a == NULL) {
    printf("Memoria insufficiente\n");
}
```

Dopo l'assegnamento il blocco si usa attraverso `a` come una sequenza di `int`. Il controllo `a == NULL` va fatto prima di usare il blocco, perché dereferenziare il puntatore nullo è un errore (capitolo 12).

## Liberare: free
```c
#include <stdlib.h>
void free(void* ptr);
```

**Definizione.** La funzione `free` libera il blocco di memoria allocato da `malloc` il cui indirizzo è `ptr`. Il puntatore deve essere stato ottenuto da `malloc` (o da `calloc` e `realloc`), oppure essere `NULL`, nel qual caso `free` non fa nulla. Dopo la chiamata l'indirizzo contenuto in `ptr` non è più utilizzabile.

(In parole povere: è la restituzione dello scaffale al magazzino. Da quel momento può essere dato a qualcun altro.)

Dopo `free(a);` la variabile `a` contiene ancora il vecchio indirizzo, cioè è diventata un dangling pointer (capitolo 41). Per questo è buona pratica azzerarla subito:

```c
free(a);
a = NULL;
```

La regola da ricordare è: **ogni `malloc` deve avere una `free` corrispondente**.

## Un esempio nel modello della memoria
```c
int* p1 = malloc(20);
int* p2 = malloc(32);
double* p3 = malloc(16);
free(p2); p2 = NULL;
char* p4 = malloc(20);
free(p1); p1 = NULL;
```

I quattro puntatori `p1`, `p2`, `p3`, `p4` sono variabili locali di `main` e stanno nello stack; i blocchi a cui puntano stanno nello heap. Le prime tre `malloc` creano tre blocchi di 20, 32 e 16 byte, e a ogni passo un puntatore in più passa da non inizializzato a un indirizzo valido. La `free(p2)` restituisce il secondo blocco, lasciando un «buco» tra il primo e il terzo, e `p2` viene azzerato. La successiva `malloc(20)` può riutilizzare quello spazio: nel modello il quarto blocco viene collocato proprio nel buco. Infine `free(p1)` libera il primo blocco.

![Lo heap dopo ciascuna delle sei istruzioni dell'esempio.](figure/prog/heap_blocchi.png|16)

Alla fine restano allocati i blocchi di `p3` e `p4`, mentre `p1` e `p2` valgono `NULL`. Si vedono due differenze rispetto allo stack: i blocchi si possono liberare **in qualunque ordine**, non solo dall'ultimo al primo, e lo heap non resta compatto, perché si formano zone libere in mezzo a zone occupate. Dove finisca esattamente ogni blocco lo decide `malloc`: la figura è un modello, non una garanzia.

## Allocare un array nello heap
Un array è una sequenza di valori dello stesso tipo memorizzati in posizioni contigue di memoria (capitolo 23). La dimensione in byte di un'area contigua con `n` elementi di tipo `int` è quindi `n * sizeof(int)`, ed è questo il numero da passare a `malloc`:

```c
int* a = malloc(n * sizeof(int));
```

Per esempio, con `n = 3` e `int` di 4 byte si chiedono 12 byte, che bastano per `a[0]`, `a[1]` e `a[2]`. Scrivere `malloc(n)` sarebbe sbagliato: riserverebbe `n` byte, non `n` interi.

In C l'allocazione dinamica è al livello più elementare possibile: si riservano sequenze contigue e non inizializzate di byte, che poi vanno inizializzate esplicitamente. Sugli elementi si lavora con la solita notazione `a[i]`, che vale anche per i puntatori (capitolo 25). Con questi strumenti il problema di `leggiArray` si può finalmente risolvere, come mostra il prossimo capitolo.
