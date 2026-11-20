# Capitolo 48: Operazioni sulle Matrici: Somma degli Elementi e Somma di Matrici
## La somma di tutti gli elementi
Il primo algoritmo sulle matrici è la generalizzazione della somma degli elementi di un array (capitolo 24). Data una matrice m di interi con rows righe e cols colonne, si vuole la somma di tutti i valori che contiene. Formalmente è una **sommatoria doppia**:

s = Σ_{i=0}^{rows−1} Σ_{j=0}^{cols−1} m[i][j]

La formula si traduce quasi parola per parola: «per tutte le righe i, e per tutte le colonne j, prendi il valore m[i][j] e sommalo a un accumulatore s». Quindi:
- si definisce una variabile accumulatore `s`, che contiene la somma parziale e parte da 0, l'elemento neutro della somma;
- per ogni riga (indice i) e per ogni colonna (indice j) si somma m[i][j] a s;
- alla fine l'accumulatore contiene la somma totale.

È una **scansione completa** della matrice: ogni elemento viene visitato esattamente una volta. Ogni Σ della formula diventa uno dei due cicli annidati.

## La funzione sommaMatrice
Nella versione per matrici a dimensione variabile le dimensioni arrivano come parametri (capitolo 47):

```c
#include <stdio.h>

#define ROWS 2
#define COLS 3
int sommaMatrice(const size_t rows, const size_t cols, const int m[rows][cols]);

int main(void) {
    int m[ROWS][COLS] = { {0,1,2}, {3,4,5} };

    int totale = sommaMatrice(ROWS, COLS, m);
    printf("La somma vale %d\n", totale); // Output: 15
}

int sommaMatrice(const size_t rows, const size_t cols, const int m[rows][cols]) {
    int s = 0; // accumulatore
    for (size_t i = 0; i < rows; i++) {        // ciclo righe
        for (size_t j = 0; j < cols; j++) {    // ciclo colonne
            s += m[i][j];                      // accumulo elemento
        }
    }
    return s;
}
```

Nella versione per matrici a dimensione fissa il parametro è `const int m[ROWS][COLS]` e i cicli usano direttamente ROWS e COLS:

```c
int sommaMatrice(const int m[ROWS][COLS]) {
    int s = 0; // accumulatore
    for (size_t i = 0; i < ROWS; i++) {        // ciclo righe
        for (size_t j = 0; j < COLS; j++) {    // ciclo colonne
            s += m[i][j];                      // accumulo elemento
        }
    }
    return s;
}
```

e la chiamata è semplicemente `sommaMatrice(m)`. Le due versioni danno lo stesso risultato, 0 + 1 + 2 + 3 + 4 + 5 = 15; la prima però funziona con matrici di qualunque dimensione, la seconda solo con matrici 2×3.

## Errori comuni
Gli errori tipici quando si lavora sulle matrici sono:
- **inizializzazione sbagliata** dell'accumulatore o degli indici, per esempio un accumulatore che non parte da 0 o un indice che non parte da 0;
- **righe e colonne scambiate negli indici**: scrivere `m[j][i]` invece di `m[i][j]` scambia il ruolo di righe e colonne. Oltre a dare un risultato sbagliato, se la matrice non è quadrata può portare ad accessi fuori dalla matrice. Per esempio, in una matrice 2×3, con i fino a 1 e j fino a 2, `m[j][i]` arriva a `m[2][…]`, ma la riga 2 non esiste;
- **accesso fuori intervallo**: in C non c'è alcun controllo sugli indici. Se i ≥ rows o j ≥ cols il comportamento è indefinito (~undefined behavior~, capitolo 25), con conseguenze imprevedibili: si leggono o si scrivono celle che non appartengono alla matrice, si corrompono altre variabili sullo stack, il programma può bloccarsi.

## Buone pratiche
Le slide raccomandano quattro abitudini:
- **usare `size_t` per gli indici**: è il tipo standard per dimensioni e indici di array, e non può essere negativo, il che previene errori di segno;
- **definire le dimensioni con simboli** invece che con «numeri magici»: con `#define ROWS 10` il codice è più leggibile e per cambiare la dimensione basta modificare una riga;
- **isolare la logica in funzioni riutilizzabili**: mettere il calcolo in una funzione come `sommaMatrice` evita di duplicare il codice e rende il programma più chiaro e più facile da provare;
- **usare `const` nei parametri** quando la matrice non deve essere modificata, come in `int sommaMatrice(size_t rows, size_t cols, const int m[rows][cols]);`. Il qualificatore impedisce modifiche accidentali agli elementi dentro la funzione e dichiara a chi legge che la funzione si limita a leggere i dati: è una forma di autodocumentazione (capitolo 33).

## La somma di due matrici
Un'operazione diversa riguarda due matrici: la somma elemento per elemento.

**Definizione.** Date due matrici A, B ∈ ℤ^{rows×cols} con le stesse dimensioni, la loro **somma** è la matrice C = A + B, delle stesse dimensioni, con elementi C_{ij} = A_{ij} + B_{ij} per ogni i ∈ [0, rows) e ogni j ∈ [0, cols).

(In parole povere: si sommano gli elementi che stanno nella stessa posizione, e il risultato va nella stessa posizione di una nuova matrice.)

Per esempio, se A ha righe 0, 1, 2 e 3, 4, 5 e B ha righe 6, 7, 8 e 9, 10, 11, allora C ha prima riga 0 + 6, 1 + 7, 2 + 8, cioè 6, 8, 10, e seconda riga 3 + 9, 4 + 10, 5 + 11, cioè 12, 14, 16.

L'algoritmo è una scansione contemporanea di A e B: due cicli annidati, per ogni riga i e per ogni colonna j si calcola C[i][j] = A[i][j] + B[i][j]. La stessa coppia (i, j) serve a raggiungere la stessa posizione nelle tre matrici.

```c
void sommaMatrici(size_t rows, size_t cols,
                  const int a[rows][cols],
                  const int b[rows][cols],
                        int c[rows][cols])
{
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < cols; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}
```

I tre parametri sono matrici contigue con le stesse dimensioni. `a` e `b` sono `const` perché sono dati in ingresso; `c` non è `const` perché la funzione ci scrive il risultato: è un parametro di uscita. Una funzione non può restituire una matrice con `return`, quindi il chiamante prepara la matrice risultato e la funzione la riempie, come per gli array passati come parametri (capitolo 33).

```c
#include <stdio.h>
#define ROWS 2
#define COLS 3

int main(void) {
    int m1[ROWS][COLS] = {{0,1,2}, {3,4,5}};
    int m2[ROWS][COLS] = {{6,7,8}, {9,10,11}};
    int s[ROWS][COLS];

    sommaMatrici(ROWS, COLS, m1, m2, s);

    printf("Matrice somma:\n");
    for (size_t i = 0; i < ROWS; i++) {
        for (size_t j = 0; j < COLS; j++) {
            printf("%2d ", s[i][j]);
        }
        printf("\n");
    }
}
```

L'uscita è `Matrice somma:` seguita dalle righe ` 6  8 10` e `12 14 16`. Lo specificatore `%2d` stampa ogni numero su almeno due caratteri, così le colonne restano allineate.

## Esercizi proposti
Le slide propongono tre esercizi, con il prototipo da rispettare. Le slide danno solo il prototipo; le soluzioni che seguono sono una proposta (non del docente), da provare al calcolatore.

**Trasposizione sul posto.** Data una matrice quadrata A ∈ ℤ^{n×n}, la sua **trasposta** è la matrice A^{T} con (A^{T})_{ij} = A_{ji}: le righe diventano colonne. Per esempio la trasposta della matrice con righe 1, 2, 3 / 4, 5, 6 / 7, 8, 9 ha righe 1, 4, 7 / 2, 5, 8 / 3, 6, 9. La diagonale principale (1, 5, 9) resta ferma, e gli elementi sopra e sotto la diagonale si scambiano. Va fatta **sul posto** (~in-place~), modificando la matrice stessa e scambiando A[i][j] con A[j][i]:

```c
// Trasposizione in-place di una matrice quadrata n×n
// Input:  matrice a[n][n]
// Output: la stessa matrice a viene modificata,
//         scambiando A[i][j] con A[j][i]
void trasponiMatrice(size_t n, int a[n][n]) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = i + 1; j < n; j++) {   // solo sopra la diagonale
            int tmp = a[i][j];
            a[i][j] = a[j][i];
            a[j][i] = tmp;
        }
    }
}
```

Il punto delicato è il ciclo interno, che parte da `j = i + 1`: si visitano solo le posizioni sopra la diagonale, e ognuna viene scambiata con la sua simmetrica. Se il ciclo interno partisse da 0, ogni coppia verrebbe scambiata due volte, una volta da (i, j) e una da (j, i), e la matrice tornerebbe uguale all'inizio. Lo scambio usa una variabile temporanea, come nello scambio di variabili del capitolo 13.

**Prodotto per uno scalare.** Dati una matrice A e un numero k, il prodotto kA è la matrice C con C[i][j] = k · A[i][j]:

```c
// Moltiplica ogni elemento della matrice per una costante scalare
// Input:  scalare k, matrice a[rows][cols]
// Output: matrice risultato c[rows][cols] con c[i][j] = k * a[i][j]
void prodottoScalareMatrice(size_t rows, size_t cols, int k,
                            const int a[rows][cols],
                                  int c[rows][cols]) {
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < cols; j++) {
            c[i][j] = k * a[i][j];
        }
    }
}
```

È la stessa struttura di `sommaMatrici`, con un solo ingresso matriciale.

**Prodotto di due matrici.** Date A ∈ ℤ^{m×n} e B ∈ ℤ^{n×p}, il prodotto C = A × B è una matrice m×p con elementi C_{ij} = Σ_{k=0}^{n−1} A_{ik} · B_{kj}: l'elemento di riga i e colonna j si ottiene moltiplicando la riga i di A per la colonna j di B, elemento per elemento, e sommando. Il prodotto esiste solo se il numero di colonne di A è uguale al numero di righe di B (n in entrambi i casi). Nell'esempio delle slide A ha righe 1, 2, 3 / 4, 5, 6 e B ha righe 7, 8 / 9, 10 / 11, 12; allora C_{00} = 1 · 7 + 2 · 9 + 3 · 11 = 58, C_{01} = 1 · 8 + 2 · 10 + 3 · 12 = 64, C_{10} = 4 · 7 + 5 · 9 + 6 · 11 = 139 e C_{11} = 4 · 8 + 5 · 10 + 6 · 12 = 154.

```c
// Calcola il prodotto di due matrici A (m×n) e B (n×p)
// Input:  A[m][n], B[n][p]
// Output: C[m][p] = A × B
void prodottoMatrici(size_t m, size_t n, size_t p,
                     const int a[m][n],
                     const int b[n][p],
                           int c[m][p]) {
    for (size_t i = 0; i < m; i++) {
        for (size_t j = 0; j < p; j++) {
            int s = 0;                       // accumulatore per c[i][j]
            for (size_t k = 0; k < n; k++) {
                s += a[i][k] * b[k][j];
            }
            c[i][j] = s;
        }
    }
}
```

Servono **tre** cicli annidati: due per scegliere la posizione (i, j) del risultato e un terzo, con indice k, per la sommatoria. Il terzo ciclo è una somma con accumulatore come quella di `sommaMatrice`, e l'accumulatore va azzerato per ogni nuovo elemento, cioè dentro il ciclo su j: se fosse inizializzato una volta sola fuori dai cicli, ogni elemento conterrebbe anche le somme di tutti i precedenti. Con il programma di prova delle slide (M = 2, N = 3, P = 2) la stampa è `58 64` e `139 154`.

## Riepilogo
- La somma degli elementi è una sommatoria doppia: un accumulatore che parte da 0 e due cicli annidati.
- Errori tipici: accumulatore o indici non inizializzati bene, `m[j][i]` al posto di `m[i][j]`, indici fuori intervallo (comportamento indefinito, il C non controlla).
- Buone pratiche: `size_t` per gli indici, dimensioni con `#define`, logica in funzioni, `const` per le matrici in sola lettura.
- La somma di matrici si fa elemento per elemento, con la matrice risultato passata come parametro di uscita non `const`.
- Trasposizione sul posto: si scambiano solo le posizioni sopra la diagonale; prodotto di matrici: tre cicli annidati, con l'accumulatore azzerato per ogni elemento.

Il capitolo 49 tratta la ricerca e la verifica di proprietà sulle matrici.
