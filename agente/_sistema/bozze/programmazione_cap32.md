# Capitolo 32: Il Passaggio per Riferimento Simulato con i Puntatori
## Perché lo scambio non funziona
Vogliamo una funzione che scambi i valori di due variabili del chiamante, riusando lo schema con la variabile temporanea del capitolo 13. Il primo tentativo è questo:

```c
#include <stdio.h>

void swapSbagliato(int a, int b) {
    int tmp = a;
    a = b;
    b = tmp;
}

int main(void) {
    int x = 10, y = 20;
    swapSbagliato(x, y);
    printf("x = %d, y = %d\n", x, y);
    // stampa x=10, y=20: nulla è cambiato
}
```

Il motivo è quello del capitolo 28: in C i parametri sono **sempre passati per valore**. Seguendo lo stack si vede tutto. Alla chiamata i valori di `x` e `y` vengono copiati nei parametri formali `a` e `b`; `swapSbagliato` inizia a lavorare con le sue copie e scambia `a` e `b`; `x` e `y` restano inalterati; al ritorno il record di attivazione viene rimosso e lo scambio sparisce con esso. La funzione non può nemmeno accedere direttamente alle variabili di `main`, perché non le sono visibili (~out of scope~).

Una precisazione sui termini: `a` e `b` sono i **parametri formali**, mentre 10 e 20 sono gli argomenti, o parametri attuali (capitolo 28). In un paio di disegni delle slide `a` e `b` compaiono come «parametri attuali», ma la definizione corretta è questa.

## La soluzione: passare gli indirizzi
Invece di passare la copia dei valori, si passano alla funzione **gli indirizzi** delle variabili da modificare. Il passaggio dell'indirizzo avviene anch'esso per copia, ma questo non ha alcun impatto: la funzione riceve dei **puntatori** e, con il dereferenziamento `*puntatore`, modifica i dati originali nel chiamante.

Il riepilogo dei puntatori (capitoli 11 e 12): `int* p;` dichiara un puntatore a int, che contiene un indirizzo; `p = &x;` memorizza in `p` l'indirizzo di `x`; `*p` accede alla variabile puntata, quindi `*p = 42;` modifica la variabile a cui `p` punta. In sintesi: `p` è l'indirizzo, `*p` il valore puntato, `&x` l'indirizzo di `x`. Non si dereferenziano mai puntatori non inizializzati o `NULL`.

```c
#include <stdio.h>

void swap(int* pA, int* pB) {
    int tmp = *pA;  // legge il valore puntato da pA
    *pA = *pB;      // scrive nella variabile puntata da pA
    *pB = tmp;      // scrive nella variabile puntata da pB
}

int main(void) {
    int x = 10, y = 20;
    swap(&x, &y);   // passo gli INDIRIZZI di x e y
    printf("x = %d, y = %d\n", x, y);
    // stampa x=20, y=10: scambio riuscito
}
```

Passo per passo: la chiamata copia `&x` e `&y` nei parametri `pA` e `pB`; `int tmp = *pA;` legge 10 dalla cella di `x`; `*pA = *pB;` scrive 20 in `x`; `*pB = tmp;` scrive 10 in `y`. Al ritorno il record di attivazione di `swap` sparisce, ma le scritture sono avvenute nelle celle di `main`, quindi restano.

![Lo stesso scambio nei due casi: a sinistra si modificano le copie nei parametri; a destra i parametri puntano alle variabili di main.](figure/prog/scambio_valore_puntatori.png|14)

(In parole povere: invece di dare alla funzione una fotocopia dei tuoi fogli, le dai l'indirizzo di casa tua. L'indirizzo è copiato, ma con quello la funzione arriva ai fogli veri.)

## Passaggio per riferimento, simulato
**Definizione.** Nel **passaggio per riferimento** (~by reference~), presente in linguaggi come Pascal e C++ ma non in C, la funzione riceve un riferimento alla variabile del chiamante, tipicamente realizzato come un puntatore gestito in modo implicito dal linguaggio, e attraverso di esso può accedere alla variabile e modificarne il valore.

(In parole povere: è come se la funzione lavorasse direttamente sulla tua variabile, senza che tu debba scrivere `&` e `*`.)

In C **non esiste** il passaggio per riferimento: è tutto per valore, e la funzione riceve sempre una copia degli argomenti. Per avere un effetto analogo si passa l'indirizzo della variabile e, nella funzione, si usa il dereferenziamento: per questo si parla di passaggio per riferimento **simulato**. È il meccanismo che rende possibili funzioni come `scanf`, che devono modificare variabili dichiarate nel `main` o altrove, e spiega finalmente perché si scrive `scanf("%d", &x)`.

Due osservazioni conclusive:
- il passaggio per puntatore non cambia il fatto che in C i parametri sono passati solo per valore: quello che viene copiato è l'**indirizzo**;
- passando un indirizzo, la funzione chiamata può leggere e scrivere direttamente nella cella di memoria della variabile del chiamante, o di qualunque altra area indirizzabile, e non è limitata al suo record di attivazione. In questo modo si oltrepassano le regole della visibilità locale imposte dallo stack.
