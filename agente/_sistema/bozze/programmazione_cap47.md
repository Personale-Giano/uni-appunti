# Capitolo 47: Passare una Matrice a una Funzione
## Tre casi diversi
Per scrivere programmi ben organizzati e riutilizzabili non basta dichiarare e usare le matrici nel `main`: bisogna poterle passare alle funzioni (capitoli 27-29). Il C lo permette, ma con modalità che dipendono da come è stata definita la matrice. Le slide distinguono tre casi:
- matrici con **dimensioni fisse**, note in compilazione;
- matrici con **dimensioni variabili**, note solo durante l'esecuzione, possibili dal C99 grazie ai VLA (capitolo 25);
- passaggio di **singole righe**, come se fossero array monodimensionali.

## Matrici e puntatori
Per capire che cosa riceve una funzione conviene sapere che tipo hanno le varie espressioni costruite a partire da una matrice. Una matrice è un **array di array**, contigui in memoria. Con

```c
#define ROWS 2
#define COLS 3
int m[ROWS][COLS];
```

si ha:
- `m` ha tipo `int [ROWS][COLS]`, ed è convertibile in `int (*)[COLS]`, cioè in un puntatore alla prima riga, un array di COLS interi (capitolo 46);
- `m[i]` è la riga i-esima, un array di COLS interi, di tipo `int [COLS]`; si può usare come array della riga i ed è convertibile in `int*`;
- `m[i][j]` è il valore dell'elemento di riga i e colonna j, di tipo `int`;
- `&m[i][j]` è l'indirizzo di quell'elemento, di tipo `int*`.

La scrittura `int (*m)[COLS]` va letta con attenzione: le parentesi dicono che `m` è un puntatore, e quello a cui punta è un array di COLS interi. Senza parentesi, `int *m[COLS]` dichiarerebbe tutt'altro: un array di COLS puntatori a `int` (precisazione aggiunta).

## Matrici a dimensione fissa
Se le dimensioni sono note in compilazione, si definiscono con `#define` e il prototipo della funzione le riporta entrambe:

```c
void fn(int m[ROWS][COLS]); // prototipo
fn(mat);                    // chiamata
```

Nella chiamata si scrive solo il nome della matrice, come per gli array (capitolo 33): non viene copiata la matrice, la funzione riceve l'indirizzo della prima riga e lavora sugli elementi originali.

Nel prototipo `ROWS` serve a documentare la forma attesa, ma la prima dimensione non fa parte del tipo del parametro e si può omettere. Le due forme seguenti sono equivalenti alla precedente, purché il numero di righe arrivi come parametro a parte:

```c
void fn2(const size_t rows, int m[][COLS]);
void fn3(const size_t rows, int (*m)[COLS]);
```

Il corso però non userà questo approccio.

La prima dimensione si può omettere e la seconda no per il motivo visto nel capitolo 46: per calcolare l'indirizzo di m[i][j] serve sapere quanti elementi ha ogni riga, cioè COLS, mentre il numero di righe non serve. È la stessa ragione per cui un parametro array `int a[]` non ha bisogno della lunghezza tra le parentesi (precisazione aggiunta).

## Matrici a dimensione variabile (C99)
Dal C99 si possono dichiarare matrici con numero di righe e di colonne deciso durante l'esecuzione, come i VLA unidimensionali (capitolo 25):

```c
size_t rows = 4, cols = 5;
int mat[rows][cols];
```

Per passare una matrice così a una funzione, i parametri devono includere anche le dimensioni, e devono venire **prima** della matrice, perché la dichiarazione `m[rows][cols]` le usa:

```c
void fn(const size_t rows, const size_t cols, int m[rows][cols]);
fn(rows, cols, mat);        // chiamata
```

Anche qui il prototipo può non specificare la prima dimensione del parametro `m`:

```c
void fn2(const size_t rows, const size_t cols, int m[][cols]);
void fn3(const size_t rows, const size_t cols, int (*m)[cols]);
```

Questa forma è la più generale: la stessa funzione funziona con matrici di qualunque dimensione, anche con quelle a dimensione fissa, alle quali basta passare ROWS e COLS come argomenti. Nei capitoli successivi le funzioni sulle matrici sono scritte quasi tutte così.

## Passare una riga sola
Poiché una matrice è un array di array, l'indice di riga dà un array monodimensionale: `mat[i]` è un array di COLS interi, di tipo `int[COLS]`.

```c
int mat[ROWS][COLS];
mat[i];    // è un array di COLS interi, tipo: int[COLS]
```

Questo array si può passare direttamente a una funzione che lavora su vettori monodimensionali. Le firme che seguono sono alternative, da non dichiarare insieme:

```c
void fn_su_array(int a[COLS]);   // COLS documenta la lunghezza attesa
void fn_su_array(int a[]);       // sintassi equivalente
fn_su_array(mat[i]);             // i ∈ [0, ROWS)
```

Se la funzione deve ricevere anche la lunghezza del vettore, come le funzioni sugli array del capitolo 33, si passa COLS:

```c
void fn_su_array(const size_t aLen, int a[]);
fn_su_array(COLS, mat[i]);       // qui aLen = COLS
```

In questo modo tutte le funzioni già scritte per gli array, per esempio la somma o la ricerca lineare (capitoli 24 e 35), si possono applicare a una riga della matrice senza riscriverle.

## Un esempio: stampaMatrice
La stampa riga per riga del capitolo 46 diventa una funzione riutilizzabile:

```c
// stampaMatrice
// Stampa gli elementi di una matrice di interi m[rows][cols].
// Ogni riga della matrice è visualizzata tra parentesi quadre,
// Parametri:
//   rows, cols – dimensioni della matrice
//   m          – matrice da visualizzare
void stampaMatrice(size_t rows, size_t cols, const int m[rows][cols]) {
    for (size_t i = 0; i < rows; i++) {
        // INIZIO RIGA
        printf("[ ");
        for (size_t j = 0; j < cols; j++) {
            printf("%d ", m[i][j]);   // stampa elementi della riga
        }
        // FINE RIGA
        printf("]\n");
    }
}
```

Le dimensioni arrivano come parametri e vengono prima della matrice; il parametro è `const` perché la funzione legge soltanto, come i parametri array del capitolo 33. Chiamata con `stampaMatrice(2, 3, m)` sulla matrice con righe 0, 1, 2 e 3, 4, 5, produce le due righe `[ 0 1 2 ]` e `[ 3 4 5 ]`.

## Riepilogo
- Una matrice è un array di array: `m[i]` è una riga, di tipo `int[COLS]`; `m` si converte in un puntatore alla prima riga, di tipo `int (*)[COLS]`.
- Con dimensioni fisse il parametro si scrive `int m[ROWS][COLS]`; la prima dimensione si potrebbe omettere, la seconda no.
- Con dimensioni variabili (C99) le dimensioni si passano come parametri, prima della matrice: `void fn(size_t rows, size_t cols, int m[rows][cols])`.
- Una singola riga `mat[i]` si passa a qualunque funzione che lavora su array, insieme alla lunghezza COLS.
- Come per gli array, la matrice non viene copiata e si usa `const` quando la funzione deve solo leggere.

Il capitolo 48 usa questi strumenti per le prime operazioni sulle matrici.
