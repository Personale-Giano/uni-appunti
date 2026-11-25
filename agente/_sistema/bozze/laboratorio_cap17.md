# Capitolo 17: Laboratorio 7: Domande sui Puntatori e Schemi di Modifica degli Array
## Tre domande sui puntatori
Il laboratorio 7, «Operazioni su array», riprende i temi dei capitoli 32-45 della teoria: puntatori, array passati alle funzioni, modello dimensione-capacità, selezione e memoria dinamica. Si apre con tre domande di riscaldamento sui puntatori, con la soluzione nelle slide.

**Domanda 1.** Che cosa definisce questo codice?

```c
int* countPtr, count;
```

Definisce due variabili di tipo diverso: `countPtr` è un puntatore a dati di tipo `int`, mentre `count` è un semplice `int`. L'asterisco, anche se è scritto attaccato a `int`, appartiene solo al primo nome: per avere due puntatori bisognerebbe scrivere `int *p1, *p2;` (precisazione aggiunta). Nessuna delle due variabili è inizializzata; per inizializzarle si può scrivere, per esempio:

```c
int* countPtr = NULL, count = 0;
```

(In parole povere: in una dichiarazione con più nomi, la stellina vale solo per il nome che le sta subito dopo. Per non sbagliare conviene dichiarare un puntatore per riga, precisazione aggiunta.)

**Domanda 2.** Che cosa fa questo codice?

```c
int count = 3;
int* pC = &count;
int* pC2 = &pC;
printf("%d %d\n", count, pC);
```

Contiene due errori. Il primo è nella terza riga: `&pC` è l'indirizzo di un puntatore, quindi non è un puntatore a `int` ma un **doppio puntatore**, di tipo `int**`, e non si può assegnare a un `int*` (il compilatore segnala tipi di puntatore incompatibili). Il secondo è nella `printf`: per stampare il valore a cui punta `pC` bisogna dereferenziarlo con l'operatore `*` (capitolo 12 della teoria), altrimenti con `%d` si passa un indirizzo dove è atteso un intero. La riga corretta è

```c
printf("%d %d\n", count, *pC);
```

che stampa `3 3`. Se davvero servisse una variabile che contiene l'indirizzo di `pC`, andrebbe dichiarata così: `int** pC2 = &pC;`. I doppi puntatori però non fanno parte del programma visto finora (precisazione aggiunta).

**Domanda 3.** Che cosa fa questo codice?

```c
size_t* p;
*p++;
(*p)++;
*p += 1;
*(p++);
```

La risposta delle slide divide le quattro istruzioni in due gruppi:

- `*p++;` e `*(p++);` incrementano il **puntatore** `p`;
- `(*p)++;` e `*p += 1;` incrementano il **valore puntato** da `p`.

Il motivo è la precedenza degli operatori: l'incremento postfisso `++` lega più forte del `*`, quindi `*p++` vuol dire `*(p++)`: si incrementa `p` e si dereferenzia il suo vecchio valore, che poi non viene usato. Per incrementare il dato puntato servono le parentesi, `(*p)++`, oppure l'assegnamento composto `*p += 1`, dove il `*` si applica prima del `+=`.

(In parole povere: `*p++` sposta la freccia, `(*p)++` cambia il numero nella casella indicata dalla freccia.)

Nel frammento della slide `p` non è inizializzato, quindi nessuna delle quattro righe si potrebbe eseguire davvero: dereferenziare un puntatore che non punta a nulla è comportamento indefinito (precisazione aggiunta). La domanda riguarda solo il significato delle espressioni.

## Il file 00_puntatori.c
Il codice iniziale contiene `00_puntatori.c`, che prova le quattro espressioni su un puntatore vero: `size_t index = 2; size_t* p = &index;`. I commenti del file spiegano che `*p++;` incrementa il puntatore perché `++` ha priorità maggiore di `*`, e che il compilatore dà un avviso del tipo «expression result unused» (risultato dell'espressione non usato): l'avviso è un campanello d'allarme, perché il codice probabilmente non fa quello che si voleva. Dopo `p = &index;` il file usa `(*p)++;`, che porta `index` a 3, e `*p += 1;`, che lo porta a 4; queste due stampe mostrano i valori 3 e 4 e l'indirizzo di `index`, che non cambia.

Dopo `*p++;` e dopo `*(p++);` il file stampa `*p`, ma a quel punto `p` punta subito dopo `index`, fuori dalla variabile (precisazione aggiunta). Leggere lì è comportamento indefinito (capitolo 25 della teoria): il valore stampato è quello che si trova per caso in memoria, e non va preso come risultato.

## Il modello dimensione-capacità
La seconda parte riprende il **modello dimensione-capacità** del capitolo 38 della teoria. Un array statico ha una capacità fissa, `AMAX` elementi, ma ne usa solo una parte: i primi `aLen`, quelli inizializzati. Nell'esempio delle slide l'array ha capacità 10 e contiene 17, 21, −3, 8, 19, 7: `aLen` vale 6, e le posizioni da 6 a 9 sono disponibili ma non inizializzate. Le proprietà sono due:

- gli indici validi sono quelli in [0, aLen), cioè un indice `i` di un elemento inizializzato rispetta 0 ≤ i < aLen;
- gli elementi memorizzabili rispettano 0 ≤ aLen ≤ AMAX: `aLen` può crescere o diminuire, ma la capacità resta `AMAX`.

Le dichiarazioni sono di due tipi:

```c
// capacità prefissata
#define AMAX 10
int a[AMAX];
size_t aLen;

// capacità variabile (VLA)
size_t aCap = ...;
int a[aCap];
size_t aLen;
```

Quando l'array si passa a una funzione, le slide distinguono due casi. Se la funzione non cambia la dimensione, riceve dimensione e capacità per valore: `const size_t aLen, const size_t aCap, int a[]`. Se invece la funzione può cambiare la dimensione (senza cambiare la capacità), riceve la dimensione **per puntatore**: `size_t *p_aLen, const size_t aCap, int a[]`. Così può aggiornare `*p_aLen`, rispettando 0 ≤ `*p_aLen` ≤ aCap, e il cambiamento arriva alla funzione chiamante, con il passaggio per riferimento simulato del capitolo 32 della teoria.

(In parole povere: la capacità è il numero di posti del parcheggio, la dimensione il numero di auto parcheggiate. Una funzione che fa entrare o uscire auto deve poter aggiornare il contatore delle auto del chiamante, quindi le serve il suo indirizzo.)

## Quattro schemi di modifica
Le slide presentano quattro schemi ricorrenti, tutti su un array `a[]` di lunghezza `aLen`. Nelle figure delle slide l'array di esempio è 0, 3, 2, 4, 3 e il criterio seleziona 3, 4 e 3 (per esempio Cond(x) = x ≥ 3: le slide non lo scrivono).

**Trasformazione.** Si applica una funzione `tr` a ogni elemento, sul posto:

```c
for (size_t i = 0; i < aLen; i++) {
    a[i] = tr(a[i]);
}
```

La lunghezza non cambia; dopo il ciclo l'array contiene tr(0), tr(3), tr(2), tr(4), tr(3).

**Filtro selettivo.** Si copiano in un altro array `b[]`, di capacità `BMAX`, gli elementi che rispettano il criterio `Cond`:

```c
size_t bLen = 0;
for (size_t iA = 0; iA < aLen && bLen < BMAX; iA++) {
    if (Cond(a[iA])) {
        b[bLen] = a[iA];   // copia a[iA] in b
        bLen++;
    }
}
// alla fine del ciclo bLen è il numero di elementi copiati in b
```

È la selezione del capitolo 38 della teoria: `bLen` fa da indice di scrittura e da contatore, e la condizione `bLen < BMAX` impedisce di scrivere oltre la capacità. Sull'esempio `b` riceve 3, 4, 3 e `bLen` vale 3.

**Riduzione sul posto** (in inglese ~in-place removal~). Si tengono nello stesso array solo gli elementi che rispettano `Cond`, compattandoli verso l'inizio:

```c
size_t j = 0;
for (size_t i = 0; i < aLen; i++) {
    if (Cond(a[i])) {
        a[j] = a[i];   // copia a[i] in a[j]
        j++;
    }
}
// alla fine del ciclo j è il numero di elementi rimasti
aLen = j;
```

Due indici scorrono lo stesso array: `i` legge tutti gli elementi, `j` indica la prossima posizione in cui scrivere e avanza solo quando un elemento viene tenuto. Vale sempre j ≤ i, quindi la scrittura non cancella mai un elemento non ancora letto. Sull'esempio: lo 0 viene scartato; il 3 in posizione 1 viene copiato in posizione 0; il 2 viene scartato; il 4 va in posizione 1; l'ultimo 3 va in posizione 2. Alla fine `j` vale 3 e l'array contiene 3, 4, 3, 4, 3, di cui solo i primi tre sono validi: gli ultimi due sono residui, fuori dal nuovo intervallo [0, aLen).

(In parole povere: è come stringere una fila di persone dopo che alcune se ne sono andate. Chi resta avanza verso la testa della fila, e alla fine si sposta il cartello «fine della fila».)

**Duplicazione selettiva.** Si copiano in `b[]` tutti gli elementi di `a[]`, ma quelli che rispettano `Cond` vengono copiati due volte:

```c
size_t bLen = 0;
for (size_t iA = 0; iA < aLen && bLen < BMAX; iA++) {
    b[bLen] = a[iA];   // copia a[iA] in b
    bLen++;
    if (Cond(a[iA]) && bLen < BMAX) {
        b[bLen] = a[iA];   // copia una seconda volta a[iA] in b
        bLen++;
    }
}
// alla fine del ciclo bLen è il numero di elementi copiati in b
```

Il controllo `bLen < BMAX` compare due volte, perché dopo la prima copia il buffer potrebbe essersi riempito. Nell'esempio delle slide, con `BMAX` uguale a 5, `b` diventa 0, 3, 3, 2, 4: la seconda copia del 4 e l'ultimo 3 non trovano posto e non vengono copiati.

## Riepilogo
- In `int* countPtr, count;` solo `countPtr` è un puntatore; `&pC` di un `int*` è un `int**`; per leggere il dato puntato serve `*`.
- `*p++` incrementa il puntatore, `(*p)++` e `*p += 1` incrementano il valore puntato.
- Nel modello dimensione-capacità vale 0 ≤ aLen ≤ AMAX; una funzione che cambia la dimensione la riceve per puntatore.
- I quattro schemi: trasformazione (un ciclo che riscrive `a[i]`), filtro (due indici su due array, con il limite di capacità), riduzione sul posto (due indici sullo stesso array), duplicazione (fino a due scritture per elemento, ognuna controllata).

Il capitolo 18 applica questi schemi agli esercizi del laboratorio, prima con array statici e poi con array nello heap.
