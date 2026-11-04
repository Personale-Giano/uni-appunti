# Capitolo 34: Le Asserzioni e assert.h
## Che cos'è un'asserzione
**Definizione.** Un'**asserzione** è un'affermazione, sotto forma di espressione booleana, che deve essere sempre vera se il programma è corretto. Se un'asserzione risulta falsa, il programma termina con un errore.

(In parole povere: è un cartello che scrivi nel codice per dire «qui deve valere questo, altrimenti ho sbagliato io»; se non vale, il programma si ferma subito e ti dice dove.)

Le asserzioni servono a rendere esplicite le ipotesi che il programmatore assume sullo stato delle variabili. Sono una **verifica di integrità delle assunzioni del codice**, non un controllo degli input dell'utente.

## assert in C
Il linguaggio C dispone di `assert`, definita in `<assert.h>`, che valuta un'espressione booleana:

```c
assert(expr);
```

Se `expr` è vera non accade nulla; se è falsa il programma termina mostrando l'espressione violata, il file e la linea in cui è fallita. Durante la compilazione le asserzioni si possono disattivare passando al compilatore l'opzione `-DNDEBUG`. (Tecnicamente `assert` è di solito una macro e non una funzione, proprio per poter segnalare il file e la linea esatti, ma nel corso questo dettaglio non si approfondisce.)

## Gli usi tipici
In tutti gli esempi va incluso `<assert.h>`, e `<stdbool.h>` dove si usa `bool`.

**Precondizione.** È una condizione che deve valere all'ingresso della funzione. Qui, se si deve leggere `a[]`, il puntatore deve essere valido:

```c
#include <assert.h>
#include <stddef.h>

void processa_array(size_t aLen, const int* a) {
    // se devo leggere a[], il puntatore dev'essere valido
    assert(aLen == 0 || a != NULL);
    // ...
}
```

**Invariante di ciclo.** È una condizione che vale a ogni iterazione, per esempio che l'indice resti entro i limiti:

```c
size_t conta_zeri(size_t aLen, const int* a) {
    size_t cnt = 0;
    for (size_t i = 0; i < aLen; ++i) {
        assert(i < aLen);  // i resta nel dominio [0, aLen)
        if (a[i] == 0)
            cnt++;
    }
    return cnt;
}
```

Qui l'asserzione è ovvia, perché la stessa condizione sta nel `for`: l'esempio serve a mostrare dove si mette un invariante. Diventa utile quando l'indice viene aggiornato in modi meno evidenti.

**Postcondizione.** È una condizione che deve valere all'uscita, cioè ciò che la funzione garantisce di aver ottenuto:

```c
void order_pair(int* a, int* b) {
    if (*a > *b) {
        int temp = *a;
        *a = *b;
        *b = temp;
    }
    assert(*a <= *b);  // post: la coppia è ordinata non decrescente
}
```

Una postcondizione può anche essere «forte» e dire tutto ciò che definisce il risultato. Per il massimo di due numeri non basta che `m` sia maggiore o uguale di entrambi: deve anche coincidere con uno dei due.

```c
int massimo(int a, int b) {
    int m;
    if (a > b) {
        m = a;
    }
    else {
        m = b;
    }
    // m non è minore di nessuno dei due valori
    assert(m >= a && m >= b);
    // m coincide con uno dei due valori di ingresso
    assert(m == a || m == b);
    return m;
}
```

**Coerenza tra argomenti.** Un'asserzione può legare tra loro più parametri:

```c
// usa *str solo se have_str è vero, altrimenti str deve essere NULL
void usa_stringa(bool have_str, const char* str) {
    assert(( have_str && str != NULL) ||
           (!have_str && str == NULL));
    // ...
}
```

(In parole povere: la precondizione è «cosa pretendo all'ingresso», l'invariante è «cosa resta vero a ogni giro», la postcondizione è «cosa garantisco all'uscita».)

## Quando usarle e quando no
Si usa `assert()` per esprimere verità che devono **sempre** valere nel codice: precondizioni, invarianti, postcondizioni, stati impossibili. Le espressioni non devono avere **effetti collaterali**: con `-DNDEBUG` le asserzioni spariscono, e con esse sparirebbe anche l'effetto.

Per gli **errori di input dell'utente** si fanno invece normali controlli che gestiscono l'errore, con messaggi o ripetendo l'input (capitolo 29). Un utente che scrive una lettera al posto di un numero non è un errore del programma: il programma deve gestirlo, non interrompersi.
