# Capitolo 18: Laboratorio 7: Modifiche ad Array Statici e ad Array nello Heap
## Es 1: il file modifica_array.c
Il primo esercizio chiede di aprire `01_modifica_array.c` del codice iniziale, leggere i prototipi con i loro commenti e implementare le cinque funzioni, seguendo la specifica. Il `main` è già scritto e stampa accanto a ogni risultato il valore atteso. Seguono soluzioni possibili (non nelle slide), controllate a mano su tutti i casi del `main`; ciascuna applica uno dei quattro schemi del capitolo 17 di questo laboratorio.

**stampa_array.** Stampa gli `aLen` elementi di `a[]`:

```c
void stampa_array(const size_t aLen, const int a[])
{
    for (size_t i = 0; i < aLen; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}
```

**copia_nonnegativi.** Copia in `b[]`, di capacità `bCap`, gli elementi di `a[]` maggiori o uguali a 0, e scrive in `*p_bLen` quanti ne ha copiati. È il filtro selettivo:

```c
void copia_nonnegativi(const size_t aLen, const int a[],
                       size_t* p_bLen, const size_t bCap, int b[])
{
    size_t bLen = 0;
    for (size_t i = 0; i < aLen && bLen < bCap; i++) {
        if (a[i] >= 0) {
            b[bLen] = a[i];
            bLen++;
        }
    }
    *p_bLen = bLen;
}
```

Il conteggio si fa in una variabile locale e si comunica al chiamante una volta sola, alla fine: si poteva anche lavorare direttamente su `*p_bLen`, ma così il codice è più leggibile. Con `a1 = {-73, 10, 77, -10, -41, 0, -58, 41, 78, 97}` e capacità 10 il risultato è `10 77 0 41 78 97`; con un buffer di capacità 3 la copia si ferma a `10 77 0`, come atteso dal `main`. Lo 0 viene copiato, perché la specifica chiede gli elementi «maggiori o uguali a 0».

**filtra_maggiori_di.** Rimuove sul posto gli elementi che non sono maggiori di `maggiori_di`, cioè tiene solo quelli strettamente maggiori, e aggiorna la lunghezza attraverso `p_aLen`. È la riduzione sul posto:

```c
void filtra_maggiori_di(size_t* p_aLen, int a[], const int maggiori_di)
{
    size_t j = 0;
    for (size_t i = 0; i < *p_aLen; i++) {
        if (a[i] > maggiori_di) {
            a[j] = a[i];
            j++;
        }
    }
    *p_aLen = j;
}
```

La lunghezza arriva per puntatore perché la funzione la cambia (capitolo 17 di questo laboratorio). Su `a1` con soglia 10 restano `77 41 78 97`: il 10 non è maggiore di 10 e viene scartato.

**duplica_pari.** Copia tutti gli elementi in `b[]`, con capacità `bCap`, scrivendo due volte quelli pari. È la duplicazione selettiva:

```c
void duplica_pari(const size_t aLen, const int a[],
                  size_t* p_bLen, const size_t bCap, int b[])
{
    size_t bLen = 0;
    for (size_t i = 0; i < aLen && bLen < bCap; i++) {
        b[bLen] = a[i];
        bLen++;
        if (a[i] % 2 == 0 && bLen < bCap) {
            b[bLen] = a[i];
            bLen++;
        }
    }
    *p_bLen = bLen;
}
```

Con `a4 = {63, 99, 56, 98, 59, 51, 57, 12, 10, 85}` e capacità 20 il risultato è `63 99 56 56 98 98 59 51 57 12 12 10 10 85`, 14 elementi; con capacità 10 si ferma a `63 99 56 56 98 98 59 51 57 12`, perché la seconda copia del 12 non trova più posto. Il test `a[i] % 2 == 0` funziona anche con i negativi, dato che in C, per esempio, −4 % 2 vale 0.

**array_equal.** Restituisce `true` se i due array hanno la stessa lunghezza e gli stessi elementi nelle stesse posizioni. È una verifica universale (capitolo 36 della teoria), con una condizione preliminare sulle lunghezze:

```c
bool array_equal(const size_t aLen, const int a[],
                 const size_t bLen, const int b[])
{
    bool uguali = (aLen == bLen);   // lunghezze diverse: già falso
    for (size_t i = 0; i < aLen && uguali; i++) {
        if (a[i] != b[i]) {
            uguali = false;
        }
    }
    return uguali;
}
```

Se le lunghezze sono diverse la sentinella parte già falsa e il ciclo non parte; altrimenti si ferma alla prima differenza. Nel `main`, dopo il filtro, `a1` vale `77 41 78 97`: il confronto con `{77, 41, 78, 97}` dà 1, quello con `a2` (6 elementi) dà 0, quello con `{77, 41, 0, 97}` dà 0 per la differenza nella terza posizione.

## Es 2: Regole trasformazione array
Sulla pagina Moodle c'è l'esercizio **Lab07-Es1 Regole trasformazione array**: bisogna leggere la specifica e il codice e completare la funzione `trasforma_array`; il `main` e le funzioni di lettura e scrittura sono già forniti. Le slide non riportano le regole, che stanno solo su Moodle; dal titolo è plausibile che sia un'applicazione dello schema di trasformazione del capitolo 17 di questo laboratorio, ma va verificato sulla specifica.

## Lo heap, in breve
La seconda metà del laboratorio riprende la memoria dinamica dei capitoli 42-45 della teoria. Lo heap è un'area di memoria gestita a mano dal programmatore: si alloca con funzioni di libreria (`malloc`, `calloc`, `realloc`) e si libera esplicitamente con `free`. Si dice dinamica perché non è fissata in compilazione, come le variabili globali o statiche, e non viene allocata automaticamente durante l'esecuzione, come lo stack: viene allocata e liberata su richiesta del programma. Le slide ripetono le regole già viste: `malloc(sz)` riserva `sz` byte contigui non inizializzati e restituisce `NULL` se non c'è memoria; un array di `n` interi richiede `n * sizeof(int)` byte; dopo `free(a)` conviene scrivere `a = NULL`; ogni `malloc` deve avere la sua `free`.

Il punto che serve per gli esercizi è il passaggio dal modello statico a quello dinamico (capitolo 45 della teoria). Quando la dimensione del risultato dipende dai dati, come nella selezione, con gli array statici si usa il modello dimensione-capacità; con lo heap si può invece allocare un array della misura esatta, in tre fasi:

- **calcolo della dimensione**: una prima scansione conta gli elementi che finiranno nel risultato, senza copiare nulla;
- **allocazione**: si riserva nello heap lo spazio esatto;
- **selezione e copia**: una seconda scansione copia gli elementi nella memoria allocata.

(In parole povere: prima si conta quante sedie servono, poi le si compra, poi si fanno sedere gli invitati. Niente sedie in più, niente invitati in piedi.)

La slide sulla selezione scrive il risultato come insieme, a = { b[i] | i ∈ [0, bLen) ∧ Cond(b[i]) }, ma si tratta di una sequenza che conserva ordine e ripetizioni; per questo il capitolo 45 della teoria usa le parentesi quadre (precisazione aggiunta).

## Es 3: il file modifica_array_memoria_dinamica.c
Il terzo esercizio chiede di implementare le funzioni di `03_modifica_array_memoria_dinamica.c`, che restituiscono array allocati nello heap. In tutte la lunghezza del risultato esce attraverso `p_bLen`, e il chiamante è responsabile di liberare la memoria: il `main` infatti chiama `free(b); b = NULL;` dopo ogni stampa. La funzione `stampa_array` è già scritta. Seguono soluzioni possibili (non nelle slide), controllate a mano sui casi del `main`.

**copia_nonnegativi.** Restituisce un nuovo array con gli elementi non negativi; se non ce ne sono restituisce `NULL` e mette `*p_bLen` a 0. È lo schema in tre fasi, come `selectCopy` del capitolo 45 della teoria:

```c
int* copia_nonnegativi(size_t aLen, const int a[],
                       size_t* p_bLen)
{
    *p_bLen = 0;
    int* b = NULL;

    // 1) calcolo della dimensione
    size_t count = 0;
    for (size_t i = 0; i < aLen; i++) {
        if (a[i] >= 0) {
            count++;
        }
    }
    // 2) allocazione
    if (count > 0) {
        b = malloc(count * sizeof(int));
        if (b != NULL) {
            // 3) selezione e copia
            size_t j = 0;
            for (size_t i = 0; i < aLen; i++) {
                if (a[i] >= 0) {
                    b[j] = a[i];
                    j++;
                }
            }
            *p_bLen = count;
        }
    }
    return b;
}
```

Le inizializzazioni `*p_bLen = 0` e `b = NULL` sono già la risposta del caso «nessun elemento»: se `count` resta 0 la funzione restituisce `NULL` con lunghezza 0, ed è proprio quello che il `main` verifica chiamando la funzione con `aLen = 0`. Sul caso normale il risultato è `10 77 0 41 78 97`, con lunghezza 6.

**trasforma_in_quadrati.** Restituisce un nuovo array, lungo quanto `a`, con i quadrati degli elementi. Qui la dimensione è nota subito, quindi la prima fase non serve:

```c
int* trasforma_in_quadrati(const size_t aLen, const int a[],
                           size_t* p_bLen)
{
    *p_bLen = 0;
    int* b = NULL;
    if (aLen > 0) {
        b = malloc(aLen * sizeof(int));
        if (b != NULL) {
            for (size_t i = 0; i < aLen; i++) {
                b[i] = a[i] * a[i];
            }
            *p_bLen = aLen;
        }
    }
    return b;
}
```

È lo schema di trasformazione, con la differenza che il risultato va in un array nuovo e `a` resta intatto (per questo è `const`). Con `{3, -4, 5, -6, 7}` il risultato è `9 16 25 36 49`. Il caso `aLen == 0` non è nella specifica; restituire `NULL` con lunghezza 0 è coerente con le altre funzioni. Con `int` a 32 bit il quadrato va in overflow se il valore assoluto supera 46340, e l'overflow di un intero con segno è comportamento indefinito (considerazione aggiunta).

**trova_indici_maggiori_di.** Restituisce un nuovo array con gli **indici** degli elementi maggiori di `valore_cercato`:

```c
int* trova_indici_maggiori_di(const size_t aLen, const int a[],
                              const int valore_cercato,
                              size_t* p_bLen)
{
    *p_bLen = 0;
    int* b = NULL;
    size_t count = 0;
    for (size_t i = 0; i < aLen; i++) {
        if (a[i] > valore_cercato) {
            count++;
        }
    }
    if (count > 0) {
        b = malloc(count * sizeof(int));
        if (b != NULL) {
            size_t j = 0;
            for (size_t i = 0; i < aLen; i++) {
                if (a[i] > valore_cercato) {
                    b[j] = (int)i;   // si copia l'indice, non il valore
                    j++;
                }
            }
            *p_bLen = count;
        }
    }
    return b;
}
```

La struttura è la stessa di `copia_nonnegativi`; cambia solo che nel risultato si scrive `i` invece di `a[i]`. Il prototipo vuole un array di `int`, mentre gli indici sono `size_t`: il cast esplicito rende visibile la conversione, che è sicura finché l'array ha meno di `INT_MAX` elementi. Con `a3 = {12, 5, 8, 20, 3, 7, 15, 1, 30, 4}` e `valore_cercato = 7` gli elementi maggiori sono 12, 8, 20, 15 e 30, e il risultato è `0 2 3 6 8`, lunghezza 5. Il 7 in posizione 5 non è maggiore di 7. (Nel `main` un commento dice «trova indici maggiori di 9», ma il valore usato è 7.)

**copia_univoci_se_adiacenti.** Copia gli elementi eliminando i duplicati adiacenti: di ogni gruppo di valori uguali consecutivi resta un solo rappresentante. Un elemento va copiato se è il primo dell'array oppure se è diverso dal precedente:

```c
int* copia_univoci_se_adiacenti(const size_t aLen, const int a[],
                              size_t* p_bLen)
{
    *p_bLen = 0;
    int* b = NULL;
    size_t count = 0;
    for (size_t i = 0; i < aLen; i++) {
        if (i == 0 || a[i] != a[i-1]) {
            count++;
        }
    }
    if (count > 0) {
        b = malloc(count * sizeof(int));
        if (b != NULL) {
            size_t j = 0;
            for (size_t i = 0; i < aLen; i++) {
                if (i == 0 || a[i] != a[i-1]) {
                    b[j] = a[i];
                    j++;
                }
            }
            *p_bLen = count;
        }
    }
    return b;
}
```

La condizione `i == 0 || a[i] != a[i-1]` sfrutta la cortocircuitazione (capitolo 18 della teoria): per `i == 0` la seconda parte non viene valutata, quindi non si legge mai `a[-1]`. Con `{5, 5, 10, 10, 10, 20, 20, 30, 5, 7}` il risultato è `5 10 20 30 5 7`, lunghezza 6: il secondo 5 viene tenuto perché il suo vicino precedente è 30, e la specifica elimina solo i duplicati adiacenti.

## Es 4: Funzioni su array con memoria dinamica
Sulla pagina Moodle c'è l'esercizio **Lab07-Es2 Funzioni su array (memoria dinamica)**: bisogna leggere la specifica e il codice e completare le funzioni richieste. Il testo non è nelle slide (che lo intitolano, per un refuso, «Trasformazione seguendo regole» come l'Es 2); dal titolo è plausibile che il ragionamento sia quello dell'Es 3: si conta, si alloca la misura esatta, si copia, e si restituisce la lunghezza attraverso un puntatore.

## Riepilogo
- Le funzioni su array statici che cambiano una lunghezza la ricevono per puntatore e la aggiornano alla fine; quelle che scrivono in un buffer controllano sempre la capacità.
- Le funzioni che restituiscono un array nello heap seguono lo schema conta, alloca, copia; se il risultato è vuoto restituiscono `NULL` con lunghezza 0.
- Chi riceve un array allocato nello heap deve liberarlo con `free` e azzerare il puntatore.
- Nei test sugli indici e sui vicini, la cortocircuitazione evita di leggere fuori dall'array.

Il capitolo 19 passa alle stringhe, con l'aritmetica dei puntatori.
