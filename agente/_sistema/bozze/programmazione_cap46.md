# Capitolo 46: Le Matrici in C: Dichiarazione, Accesso e Memoria
## Perché servono dati a più dimensioni
Un array è una sequenza di valori disposti lungo una sola dimensione, per esempio le temperature dei giorni di una settimana. Molti problemi reali però hanno più dimensioni: tempo, spazio, categorie. Le slide ne mostrano alcuni esempi:
- una **tabella dei voti** studenti × materie (Anna, Luca e Giulia in Matematica discreta, Fondamenti e Programmazione 1), su cui si calcolano medie per studente, medie per materia e confronti;
- un'**immagine in scala di grigi** di 5×5 pixel, dove ogni numero è un'intensità (0 = nero, 255 = bianco): serve una struttura a due dimensioni per mantenere la forma dell'immagine;
- una tabella delle **vendite** prodotto × mese, da cui si estraggono andamenti nel tempo o confronti tra prodotti;
- una **mappa delle altitudini** 5×5, da cui si leggono le altezze lungo un percorso;
- le **reti neurali**, che si vedranno nei corsi di Apprendimento automatico e Reti neurali, dove i pesi tra uno strato e l'altro sono tabelle di numeri.

## La matrice in matematica
**Definizione.** Fissato un insieme di valori T (per esempio ℤ, ℕ, ℝ, i booleani o i caratteri) e due dimensioni finite rows ∈ ℕ e cols ∈ ℕ, una **matrice** M è un elemento di T^{rows×cols}, cioè dell'insieme di tutte le tabelle di valori di tipo T con rows righe e cols colonne.

(In parole povere: una matrice è una tabella rettangolare di valori tutti dello stesso tipo, organizzata in righe e colonne.)

Per esempio, con T = ℤ, rows = 2 e cols = 3, una matrice M ∈ ℤ^{2×3} ha elementi a_{00}, a_{01}, a_{02} nella prima riga e a_{10}, a_{11}, a_{12} nella seconda. Il primo indice è la riga, il secondo la colonna, e tutti e due partono da 0, come gli indici degli array in C. Una matrice concreta è quella con prima riga 0, 1, 2 e seconda riga 3, 4, 5, che negli esempi di questo capitolo e dei successivi torna continuamente.

## Dichiarare una matrice
In C una matrice M ∈ T^{rows×cols} corrisponde a un **array a due dimensioni**, contiguo in memoria, i cui elementi, tutti dello stesso tipo T, sono disposti **per righe** (in inglese ~row-major order~). È simile a un array unidimensionale, ma per raggiungere un elemento servono due indici.

La dichiarazione di una matrice statica, cioè allocata sullo stack (capitolo 7), ha la sintassi:

```c
data_type m[ROWS][COLS]; // matrice di ROWS righe e COLS colonne
```

Si può anche inizializzare, scrivendo tra graffe le righe una dopo l'altra, ciascuna a sua volta tra graffe:

```c
int m[2][3] = { {0,1,2}, {3,4,5} };
```

## Accedere agli elementi
Per leggere o scrivere un elemento si usa la sintassi `m[i][j]`, dove:
- `i` è l'**indice di riga**, valido nell'intervallo semiaperto [0, ROWS);
- `j` è l'**indice di colonna**, valido nell'intervallo semiaperto [0, COLS).

```c
#define ROWS 2
#define COLS 3
int m[ROWS][COLS] = { {0,1,2}, {3,4,5} };
printf("%d", m[1][2]); // stampa 5
```

`m[1][2]` è l'elemento della riga 1 e della colonna 2, cioè l'ultimo della seconda riga: 5. Le dimensioni sono definite con `#define`, come negli array (capitolo 23), così il codice resta leggibile e si modifica in un punto solo.

## Come sta una matrice in memoria
La memoria fisica è lineare, una sequenza di celle una dopo l'altra. Per semplicità si può pensare una matrice come un array lineare in cui **le righe sono concatenate una dopo l'altra**: prima tutti gli elementi della riga 0, poi tutti quelli della riga 1, e così via. Il C conserva la struttura algebrica della matrice, ma la «appiattisce» sulla memoria imponendo un ordine di scansione per righe.

Nell'esempio delle slide la matrice `int m[2][3]` inizia all'indirizzo 0x3E8 e, con interi da 4 byte, gli elementi occupano:
- m[0][0] a 0x3E8, m[0][1] a 0x3EC, m[0][2] a 0x3F0 (riga 0);
- m[1][0] a 0x3F4, m[1][1] a 0x3F8, m[1][2] a 0x3FC (riga 1).

![La matrice int m[2][3] vista come tabella e come sequenza di celle in memoria, riga dopo riga.](figure/prog/matrice_memoria.png|14)

Poiché gli elementi sono disposti in fila per righe, l'indirizzo dell'elemento `m[i][j]` si calcola con la formula:

base(m) + (i · COLS + j) × sizeof(T) byte

dove base(m) è l'indirizzo del primo elemento m[0][0], cioè l'inizio della zona contigua che contiene la matrice, e i · COLS + j è la posizione dell'elemento (i, j) nella sequenza lineare: prima di lui ci sono i righe complete, ciascuna di COLS elementi, più i j elementi che lo precedono nella sua riga. Per m[1][2]: 1 · 3 + 2 = 5, quindi l'indirizzo è 0x3E8 + 5 × 4 = 0x3E8 + 20 = 0x3FC, come nell'elenco sopra.

La formula mostra anche perché, per calcolare l'indirizzo, serve conoscere COLS, il numero di colonne, mentre il numero di righe non interviene: tornerà utile nel capitolo 47, quando si passano le matrici alle funzioni.

Nella maggior parte delle espressioni il nome `m` viene convertito in un puntatore alla prima riga, `&m[0]`, come il nome di un array viene convertito in un puntatore al suo primo elemento (capitolo 25).

## Due cicli annidati
Per visitare tutti gli elementi di una matrice servono di solito **due cicli annidati**:
- il ciclo esterno, con indice `i`, scorre le righe;
- il ciclo interno, con indice `j`, scorre le colonne della riga `i`.

Il principio chiave è che **ogni indice ha il suo ciclo**. La struttura tipica è:

```c
for (size_t i = 0; i < ROWS; i++) {      // ciclo esterno
    for (size_t j = 0; j < COLS; j++) {  // ciclo interno
        // uso m[i][j]
    }
}
```

Per ogni valore di `i` il ciclo interno ricomincia da `j = 0` e arriva fino a COLS − 1; solo quando ha finito la riga si passa alla riga successiva. Gli elementi vengono quindi visitati nello stesso ordine in cui stanno in memoria.

Il programma seguente stampa ogni elemento con i suoi indici:

```c
#define ROWS 2
#define COLS 3
int main(void) {
    int m[ROWS][COLS] = {{0,1,2}, {3,4,5}};
    for (size_t i = 0; i < ROWS; i++) {
        for (size_t j = 0; j < COLS; j++) {
            printf("m[%zu][%zu] vale %d\n", i, j, m[i][j]);
        }
    }
}
```

L'uscita è: `m[0][0] vale 0`, `m[0][1] vale 1`, `m[0][2] vale 2`, `m[1][0] vale 3`, `m[1][1] vale 4`, `m[1][2] vale 5`, una riga di testo per elemento. Lo specificatore `%zu` serve a stampare valori di tipo `size_t`.

## Stampare la matrice come tabella
Con una piccola modifica la matrice si stampa con la sua forma, una riga di testo per ogni riga della matrice. Basta aggiungere istruzioni prima e dopo il ciclo interno: quello che sta prima viene eseguito all'inizio di ogni riga, quello che sta dopo alla fine.

```c
#define ROWS 2
#define COLS 3
int main(void) {
    int m[ROWS][COLS] = {{0,1,2}, {3,4,5}};
    for (size_t i = 0; i < ROWS; i++) {
        // INIZIO RIGA
        printf("[ ");
        for (size_t j = 0; j < COLS; j++) {
            // stampa elementi della riga
            printf("%d ", m[i][j]);
        }
        // FINE RIGA
        printf("]\n");
    }
}
```

L'uscita è:

```
[ 0 1 2 ]
[ 3 4 5 ]
```

Il `\n` è dopo la parentesi chiusa, fuori dal ciclo interno: si va a capo una volta per riga, non una volta per elemento.

## Riepilogo
- Una matrice è una tabella di valori dello stesso tipo, con rows righe e cols colonne: un elemento di T^{rows×cols}.
- In C si dichiara con `data_type m[ROWS][COLS];` e si inizializza riga per riga con graffe annidate.
- `m[i][j]` è l'elemento di riga i ∈ [0, ROWS) e colonna j ∈ [0, COLS).
- In memoria le righe sono una dopo l'altra (row-major); l'indirizzo di m[i][j] è base(m) + (i · COLS + j) × sizeof(T).
- Per visitare tutti gli elementi servono due cicli annidati, uno per indice: il ciclo esterno sulle righe, quello interno sulle colonne.

Il capitolo 47 mostra come passare una matrice a una funzione.
