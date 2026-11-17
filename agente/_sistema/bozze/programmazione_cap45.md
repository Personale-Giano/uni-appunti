# Capitolo 45: La Selezione con Copia nello Heap e la Responsabilità della Memoria
## Dal modello statico al modello dinamico
Alcuni problemi dipendono dai dati: la dimensione del risultato non è un parametro noto a priori. Il caso tipico è la **selezione** (capitolo 38), che dato un array `b` di lunghezza `bLen` e una condizione Cond(⋅) copia in un altro array `a` tutti e soli gli elementi `b[i]` che soddisfano Cond(b[i]), mantenendo l'ordine originale: a = [ b[i] | i∈[0, bLen) ∧ Cond(b[i]) ]. È il prototipo dei problemi in cui si costruisce una nuova sequenza «filtrata».

Con gli array nello stack la dimensione è nota in compilazione o fissata al momento della dichiarazione, e per gestire la selezione si è introdotto il modello dimensione-capacità, `int a[CAP]; size_t aLen;` con 0 ≤ aLen ≤ CAP: si riserva spazio per il caso peggiore e se ne usa una parte. Con lo heap il problema si riformula in modo più semplice: si alloca un array **della misura esatta**. La misura però non si conosce senza una scansione lineare di `b`, quindi serve un algoritmo che prima calcoli `aLen` e poi allochi.

## Un approccio in tre fasi
L'algoritmo è articolato in tre fasi logiche, ciascuna con uno scopo preciso:

- **calcolo della dimensione**: si scorre `b` senza copiare nulla, contando quanti elementi soddisfano Cond(b[i]). Il risultato `count` è la lunghezza esatta del nuovo array. Questa fase stabilisce quanto spazio serve, ma non produce ancora il risultato;
- **allocazione**: si riserva nello heap un array `a` di `count` elementi;
- **selezione e copia**: si ripete la scansione di `b` e ogni elemento che verifica la condizione viene copiato nella prima posizione libera di `a`. Serve quindi un secondo indice `j`, l'indice di copia.

Alla fine `a` contiene esattamente, e nell'ordine originale, tutti gli elementi selezionati.

![Le tre fasi su b = {12, 1, 3, 4, 8} con la condizione «è pari».](figure/prog/select_copy_fasi.png|14)

## La funzione selectCopy
`selectCopy` traduce in C lo schema «conta, alloca, seleziona». Riceve l'array `b` di lunghezza `bLen` e restituisce un array allocato nello heap, la cui lunghezza viene scritta in `*out_len`. Caso limite: se non ci sono elementi selezionati ritorna `NULL` e mette `*out_len` a zero.

```c
int* selectCopy(size_t bLen, const int b[], size_t* out_len) {
    assert(bLen == 0 || b != NULL);
    assert(out_len != NULL);
    *out_len = 0;
    int* a = NULL;

    // 1) Calcolo della dimensione
    size_t count = 0;
    for (size_t i = 0; i < bLen; i++)
        if (Cond(b[i]))
            count++;

    // 2) Allocazione
    if (count > 0) {
        a = malloc(count * sizeof(int));
        if (a != NULL) {
            // 3) Selezione e copia
            size_t j = 0;
            for (size_t i = 0; i < bLen; i++) {
                if (Cond(b[i])) {
                    a[j] = b[i];
                    j++;
                }
            }
            assert(count == j);
            *out_len = count;
        }
    }
    return a;
}
```

Le due `assert` iniziali sono le precondizioni (capitolo 34). L'inizializzazione `*out_len = 0;` e `a = NULL;` prepara subito la risposta del caso limite: se `count` resta a zero non si alloca nulla e la funzione restituisce quei valori. La terza `assert` controlla una proprietà interna: le due scansioni applicano la stessa condizione agli stessi elementi, quindi gli elementi copiati devono essere tanti quanti quelli contati, purché la condizione dia sempre la stessa risposta sullo stesso elemento. La lunghezza viene comunicata solo dopo che la copia è andata a buon fine.

Rispetto alla selezione del capitolo 38 non c'è più il controllo `aLen < aCap` e non può verificarsi un overflow logico: l'array ha per costruzione la misura giusta. In cambio `b` viene scandito due volte.

Va notato che la funzione ritorna `NULL` con `*out_len == 0` in due situazioni diverse: quando nessun elemento soddisfa la condizione e quando `malloc` fallisce. Il chiamante non può distinguerle, ma in entrambe può usare il risultato in sicurezza come sequenza vuota; così però l'errore di allocazione passa inosservato (precisazione aggiunta).

## Il programma completo
```c
#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include <assert.h>

// Predicato
bool Cond(int x) { return x % 2 == 0; }

// Prototipo
int* selectCopy(size_t bLen, const int b[], size_t* out_len);

int main(void) {
    #define B_LEN 5
    const int b[B_LEN] = {12, 1, 3, 4, 8};

    size_t aLen = 0;
    int* a = selectCopy(B_LEN, b, &aLen);

    // Stampa del risultato
    printf("Selezionati %zu elementi:\n", aLen);
    for (size_t i = 0; i < aLen; i++) {
        printf("a[%zu] = %d\n", i, a[i]);
    }

    // Responsabilità della memoria: il chiamante libera l'array
    free(a); a = NULL;
}
```

La definizione di `selectCopy` va scritta dopo `main`, oppure al posto del prototipo. Gli elementi pari di `b` sono 12, 4 e 8: la prima fase calcola `count = 3`, la seconda alloca `3 * sizeof(int)` byte, la terza copia con `j` che passa da 0 a 3. Il programma stampa:

```
Selezionati 3 elementi:
a[0] = 12
a[1] = 4
a[2] = 8
```

Se `b` non contenesse numeri pari, `selectCopy` ritornerebbe `NULL` con `aLen == 0`: il ciclo di stampa non verrebbe eseguito e l'ultima riga chiamerebbe `free(NULL)`, che è ammessa e non fa nulla. Il codice di `main` è quindi corretto anche nel caso limite, senza controlli aggiuntivi.

## La responsabilità della memoria
`selectCopy` alloca un blocco ma non lo libera: lo consegna al chiamante, che deve chiamare `free` quando l'array non serve più. È uno schema generale.

**Definizione.** La **responsabilità della memoria** (~ownership~) è il principio per cui ogni blocco di memoria allocato deve sempre avere un corrispondente punto del programma che ha la responsabilità di deallocarlo.

(In parole povere: ogni blocco ha sempre un «proprietario», quello che alla fine deve fare la `free`. La proprietà si può passare di mano, ma non può restare senza nessuno e non può finire a due persone insieme.)

Le regole sono queste:

- quando una funzione alloca memoria dinamica con `malloc`, diventa responsabile della gestione del blocco;
- la funzione può **trasferire** la responsabilità al chiamante, restituendo il puntatore al blocco allocato;
- il chiamante, a sua volta, può trasferirla ad altri;
- per evitare perdite di memoria, l'ultimo punto del codice che usa il blocco deve rilasciarlo con `free` quando non serve più.

Nei capitoli precedenti la responsabilità passa da `leggiArray` a `main` (capitolo 43); qui passa da `selectCopy` a `main`. Se nessuno la raccoglie si ha un memory leak; se la raccolgono in due si ha una doppia `free` (capitolo 44). Per questo la specifica di una funzione che restituisce memoria dinamica deve dire esplicitamente chi deve liberarla.

## Un esempio dalla libreria: strdup
La funzione di libreria `strdup`, dichiarata in `<string.h>`, crea nello heap una copia di una stringa, terminatore incluso (capitolo 26), e restituisce il puntatore al chiamante. Il chiamante diventa proprietario della copia e ha la responsabilità di deallocarla con `free`.

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

int main(void) {
    const char* src = "Programmazione 1";
    char* copy = strdup(src);  // copia nello heap
    assert(copy != NULL);
    printf("Originale: %s\nCopia: %s\n", src, copy);
    free(copy); copy = NULL; // il chiamante è responsabile della deallocazione
}
```

La stringa ha 16 caratteri, quindi il blocco allocato è di 17 byte, uno in più per il terminatore `'\0'`. Il programma stampa `Originale: Programmazione 1` e, a capo, `Copia: Programmazione 1`. Nel listato delle slide manca `#include <assert.h>`, necessario per usare `assert`: qui è stato aggiunto (precisazione aggiunta). Inoltre `strdup` è entrata nello standard del C solo con il C23; prima era un'estensione, comunque disponibile sui sistemi più diffusi.

## Che cosa viene dopo
Più avanti, nei corsi di Programmazione II e di Algoritmi, la memoria dinamica verrà usata in modo sistematico per costruire **strutture dati dinamiche** come liste, alberi e grafi: strutture a dimensione variabile, con un'organizzazione della memoria non contigua, in cui i singoli pezzi sono blocchi dello heap collegati tra loro da puntatori.
