# 09A_matrici

<!-- pagina 1 -->
Programmazione I
Teoria
Elvio Amparore
A.A. 2026/27
Canale B
DIPARTIMENTO DI 
INFORMATICA
 
CORSO DI LAUREA 
TRIENNALE
Matrici
Array multidimensionali, algoritmi per 
gestire dati su più dimensioni
1

<!-- pagina 2 -->
Dati multidimensionali: perché servono?
• Un array (unidimensionale) può rappresentare una sequenza di valori (es. 
temperature di una settimana)
• Ma molti problemi reali hanno più dimensioni: tempo, spazio, categorie.
2
Studente
Matematica 
Discreta
Fondamenti 
dell’informatica
Programmazione 1
Anna
28
30
27
Luca
25
24
30
Giulia
30
29
30
Studenti × Materie (tabella voti)
Permette di calcolare medie per studente, per 
materia, confronti.
X / Y
0
1
2
3
4
0
0
0
0
0
0
1
0
80
120
80
0
2
0
120
255
120
0
3
0
80
120
80
0
4
0
0
0
0
0
 Immagine in scala di grigi (5×5 pixel)
Numero = intensità (0=nero, 255=bianco)
Una struttura 2D è essenziale per 
mantenere la forma dell’immagine.

<!-- pagina 3 -->
Dati multidimensionali: perché servono?
• Un array (unidimensionale) può rappresentare una sequenza di valori (es. 
temperature di una settimana)
• Ma molti problemi reali hanno più dimensioni: tempo, spazio, categorie.
3
Vendite (Prodotto × Mese)
Si possono estrarre trend temporali 
o confrontare prodotti.
Mappa altitudini (5×5)
Altezze lungo un 
percorso
Prodotto
Gennaio
Febbraio
Marzo
Pane
120
140
135
Pasta
200
210
190
Latte
150
160
155
Y\X
0
1
2
3
4
0
210
215
220
230
240
1
200
205
210
225
235
2
190
195
200
210
220
3
180
185
188
195
205
4
170
172
175
180
190

<!-- pagina 4 -->
Dati multidimensionali: perché servono?
• Un array (unidimensionale) può rappresentare una sequenza di valori (es. 
temperature di una settimana)
• Ma molti problemi reali hanno più dimensioni: tempo, spazio, categorie.
4
+
+
⋅
=
⋅
=
x₁ x₂
h₁ h₂ h₃
o₁ o₂
WH
WO
bH
bO
x₂
x₁
h₂
h₁
h₃
o₂
o₁
Input
layer
Hidden
layer
Output
layer
Reti neurali
(le vedrete in Apprendimento 
Automatico e in Reti Neurali)
Vediamo ora come rappresentare 
questi dati multidimensionali nel 
linguaggio C

<!-- pagina 5 -->
Le matrici: definizione algebrica
In algebra lineare una matrice è una tabella rettangolare di numeri, 
organizzata in righe e colonne.
• Sia T un insieme di valori (es. ℤ, ℕ, ℝ, bool, char, ...)
• Fissiamo due dimensioni ﬁnite:
rows ∈ ℕ,   cols ∈ ℕ
• Una matrice M è un elemento di Trows✕cols, cioè dell’insieme di 
tutte le tabelle di valori di tipo T con rows righe e cols colonne
Esempio:  T = ℤ,   rows = 2,   cols = 3
5

<!-- pagina 6 -->
Le matrici
• In C, una matrice M ∈ Trows✕cols corrisponde a un array a due 
dimensioni contiguo in memoria, i cui elementi, tutti dello stesso 
tipo T, sono disposti in ordine di riga (row-major order)
• Simile ad un array unidimensionale, ma richiede più indici per 
accedere agli elementi
• Dichiarazione matrice statica (allocata sullo stack)
6
data_type m[ROWS][COLS]; // matrice di ROWS righe e COLS colonne
SINTASSI
• Dichiarazione con inizializzazione
int m[2][3] = { {0,1,2}, {3,4,5} };
SINTASSI

<!-- pagina 7 -->
Accesso agli elementi
• Per accedere agli elementi usiamo la sintassi
m[i][j]
• Con
– i indice di riga, valido nell’intervallo semiaperto [0, ROWS)
– j indice di colonna, valido nell’intervallo semiaperto [0, COLS)
7
printf("%d", m[1][2]); // stampa 5
#define ROWS 2
#define COLS 3
int m[ROWS][COLS] = { {0,1,2}, {3,4,5} };

<!-- pagina 8 -->
Rappresentazione in memoria
• Per semplicità, si può pensare alla rappresentazione in memoria 
di una matrice m come ad un array lineare in cui le righe sono 
concatenate una dopo l’altra (row-major order)
8
0
2
1
3
5
4
Riga 0
Riga 1
m[0][0]
m[0][1]
m[0][2]
m[1][0]
m[1][1]
m[1][2]
0x3E8
0x3EC
0x3F0
0x3F4
0x3F8
0x3FC
• La realizzazione implementativa del C conserva la struttura 
algebrica, ma la “appiattisce” su di uno spazio lineare (la memoria 
ﬁsica), imponendo un ordine di scansione (per righe).
• Nella maggior parte delle espressioni, m viene convertito in un 
puntatore alla prima riga &m[0].

<!-- pagina 9 -->
9
0
2
1
3
5
4
Riga 0
Riga 1
m[0][0]
m[0][1]
m[0][2]
m[1][0]
m[1][1]
m[1][2]
0x3E8
0x3EC
0x3F0
0x3F4
0x3F8
0x3FC
int m[2][3] = { {0,1,2}, {3,4,5} };
0
2
1
3
5
4
Riga 0
Riga 1
Colonna 1
Colonna 2
Colonna 0
int m[2][3]
Codice
5
m[1][2]@0x3FC
4
2
3
1
0
m[1][1]@0x3F8
m[1][0]@0x3F4
m[0][2]@0x3F0
m[0][1]@0x3EC
m[0][0]@0x3E8
word size
Rappresentazione in memoria

<!-- pagina 10 -->
10
int m[2][3]
Codice
5
m[1][2]@0x3FC
4
2
3
1
0
m[1][1]@0x3F8
m[1][0]@0x3F4
m[0][2]@0x3F0
m[0][1]@0x3EC
m[0][0]@0x3E8
word size
Rappresentazione in memoria
Poiché una matrice è realizzata come una sequenza 
lineare di celle ordinate per righe, allora l’indirizzo 
dell’elemento m[i][j] è calcolata con la formula:
base(m) + (i*COLS + j) × sizeof(T) bytes
dove:
●base(m) = indirizzo del primo elemento m[0][0], 
cioè l'inizio della regione contigua che contiene 
gli elementi.
●(i*COLS + j) é l’elemento nella sequenza lineare 
che corrisponde all’elemento (i,j) nella matrice

<!-- pagina 11 -->
Cicli annidati per le matrici
• Tipicamente per scorrere tutti gli elementi di una matrice servono 
due cicli annidati:
– ciclo esterno con indice i → scorre le righe
– ciclo interno con indice j → scorre le colonne della riga i
• Principio chiave: ogni indice ha il suo ciclo
• Struttura tipica
11
1.
for (size_t i = 0; i < ROWS; i++) {      // ciclo esterno
2.
    for (size_t j = 0; j < COLS; j++) {  // ciclo interno
3.
        // uso m[i][j]
4.
    }
5.
}

<!-- pagina 12 -->
Cicli annidati per le matrici
1. #define ROWS 2
2. #define COLS 3
3. int main(void) {
4.    int m[ROWS][COLS] = {{0,1,2}, {3,4,5}};
5.    for (size_t i = 0; i < ROWS; i++) {
6.        for (size_t j = 0; j < COLS; j++) {
7.            printf ("m[%zu][%zu] vale %d\n", 
8.                    i, j, m[i][j]);
9.        }
10.    }
11. }
12
int m[2][3]
Codice
5
m[1][2]@0x3FC
4
2
3
1
0
m[1][1]@0x3F8
m[1][0]@0x3F4
m[0][2]@0x3F0
m[0][1]@0x3EC
m[0][0]@0x3E8
word size
m[0][0] vale 0
m[0][1] vale 1
m[0][2] vale 2
m[1][0] vale 3
m[1][1] vale 4
m[1][2] vale 5

<!-- pagina 13 -->
Cicli annidati per le matrici
13
int m[2][3]
Codice
5
m[1][2]@0x3FC
4
2
3
1
0
m[1][1]@0x3F8
m[1][0]@0x3F4
m[0][2]@0x3F0
m[0][1]@0x3EC
m[0][0]@0x3E8
word size
[ 0 1 2 ]
[ 3 4 5 ]
1. #define ROWS 2
2. #define COLS 3
3. int main(void) {
4.    int m[ROWS][COLS] = {{0,1,2}, {3,4,5}};
5.    for (size_t i = 0; i < ROWS; i++) {
6.        // INIZIO RIGA     
7.        printf("[ ");                      
8.        for (size_t j = 0; j < COLS; j++) {
9.            // stampa elementi della riga
10.            printf("%d ", m[i][j]);
11.        }
12.        // FINE RIGA
13.        printf("]\n");
14.    }
15. }

<!-- pagina 14 -->
Passaggio di matrici come 
parametri di funzioni
Sintassi, considerazioni
14

<!-- pagina 15 -->
• Per scrivere programmi ben organizzati e riutilizzabili, non è sufﬁciente 
dichiarare e usare le matrici nel main, serve poterle passare a funzioni
• Il linguaggio C consente questo passaggio, ma con modalità che 
dipendono da come è stata deﬁnita la matrice
• Consideriamo tre casi distinti:
– Matrici a dimensioni ﬁsse (note a compile-time)
– Matrici a dimensioni variabili (note a runtime, con C99 e VLA)
– Passaggio di singole righe come se fossero array monodimensionali
Passaggio di matrici come parametri
15

<!-- pagina 16 -->
Matrici e puntatori
Una matrice è un array di array contigui in memoria. Supponiamo:
#define ROWS 2
#define COLS 3
int m[ROWS][COLS];
16
Signiﬁcato
Tipo
m
puntatore alla prima riga 
(array di COLS int)
int [ROWS][COLS]
  → convertibile a int(*)[COLS]
m[i]
riga i-esima, cioè array di COLS int
(si può usare come array della riga i)
int[COLS] 
  → convertibile a int*
m[i][j]
valore dell’elemento alla riga i, colonna j int
&m[i][j]
indirizzo dell’elemento (i,j)
int*

<!-- pagina 17 -->
Matrici a dimensione fissa (compile-time)
• Se le dimensioni della matrice sono note a tempo di 
compilazione, possiamo deﬁnirle con #deﬁne
• Per passare la matrice a una funzione, il prototipo deve 
includere le dimensioni:
void fn(int m[ROWS][COLS]); // prototipo
fn(mat);                    // chiamata
• ROWS documenta la forma attesa, ma la prima dimensione 
non fa parte del tipo del parametro e può essere omessa (non 
useremo questo approccio):
void fn2(const size_t rows, int m[][COLS]);
void fn3(const size_t rows, int (*m)[COLS]);
17

<!-- pagina 18 -->
Matrici a dimensione variabile (runtime, C99)
• Dal C99 è possibile dichiarare matrici i cui valori di righe e colonne 
sono determinati a tempo di esecuzione
• Deﬁnizione:
size_t rows = 4, cols = 5;
int mat[rows][cols];
• Per passare questa matrice a una funzione, i parametri devono 
includere anche le dimensioni:
void fn(const size_t rows, const size_t cols, int m[rows][cols]); 
fn(rows, cols, mat);        // chiamata
• Anche in questo caso il prototipo potrebbe non speciﬁcare la prima 
dimensione dell’argomento m:
void fn2(const size_t rows, const size_t cols, int m[][cols]);
void fn3(const size_t rows, const size_t cols, int (*m)[cols]);
18

<!-- pagina 19 -->
Array delle righe
• Abbiamo detto che una matrice è un array di array: l’indice della riga 
restituisce un array monodimensionale corrispondente a quella riga
int mat[ROWS][COLS];
mat[i];    // è un array di COLS interi, tipo: int[COLS]
• Questo array può essere passato direttamente a funzioni che operano su 
vettori monodimensionali:
void fn_su_array(int a[COLS]);   // COLS documenta la lunghezza attesa
void fn_su_array(int a[]);       // sintassi equivalente
fn_su_array(mat[i]);             // i ∈ [0, ROWS)
• Se la funzione deve ricevere anche la lunghezza del vettore:
void fn_su_array(const size_t aLen, int a[]);
fn_su_array(COLS, mat[i]);       // qui aLen = COLS
19

<!-- pagina 20 -->
Esempio: funzione sulle matrici
1.
// stampaMatrice
2.
// Stampa gli elementi di una matrice di interi m[rows][cols].
3.
// Ogni riga della matrice è visualizzata tra parentesi quadre,
4.
// Parametri:
5.
//   rows, cols – dimensioni della matrice
6.
//   m          – matrice da visualizzare
7.
void stampaMatrice(size_t rows, size_t cols, const int m[rows][cols]) {
8.
    for (size_t i = 0; i < rows; i++) {
9.
        // INIZIO RIGA    
10.
        printf("[ ");                     
11.
        for (size_t j = 0; j < cols; j++) {
12.
            printf("%d ", m[i][j]);   // stampa elementi della riga
13.
        }
14.
        // FINE RIGA
15.
        printf("]\n");
16.
    }
17.
}
20

<!-- pagina 21 -->
Operazioni su matrici
Somma, ricerca, veriﬁca proprietà
21

<!-- pagina 22 -->
Somma degli elementi della matrice
• Consideriamo una matrice m di interi, con rows righe e 
cols colonne
• Calcoliamo la somma di tutti i valori contenuti nella 
matrice
22
• Formalmente vogliamo calcolare una sommatoria doppia

<!-- pagina 23 -->
Somma degli elementi della matrice
• Procediamo quindi a tradurre in codice: 
“per tutte le righe i, e per tutte le colonne j, 
prendi il valore m[i][j] e sommalo ad un accumulatore s”
Quindi:
• Deﬁniamo una variabile accumulatore s che funge da somma 
parziale, inizialmente pari a 0 (il valore neutro della somma)
■per ogni riga (indice i)
■per ogni colonna (indice j)
■sommare m[i][j] alla somma parziale s
• Al termine, l’accumulatore conterrà la somma totale
• Questo schema è una scansione completa della matrice
• Scriviamo una funzione sommaMatrice
23

<!-- pagina 24 -->
Somma degli elementi della matrice
24
1.
#include <stdio.h>
2.
3.
#define ROWS 2
4.
#define COLS 3
5.
int sommaMatrice(const size_t rows, const size_t cols, const int m[rows][cols]);
6.
7.
int main(void) {
8.
    int m[ROWS][COLS] = { {0,1,2}, {3,4,5} };
9.
10.
    int totale = sommaMatrice(ROWS, COLS, m);
11.
    printf("La somma vale %d\n", totale); // Output: 15
12.
}
13.
14.
int sommaMatrice(const size_t rows, const size_t cols, const int m[rows][cols]) {
15.
    int s = 0; // accumulatore
16.
    for (size_t i = 0; i < rows; i++) {        // ciclo righe
17.
        for (size_t j = 0; j < cols; j++) {    // ciclo colonne
18.
            s += m[i][j];                      // accumulo elemento
19.
        }
20.
    }
21.
    return s;
22.
}
Versione per matrici a 
dimensione variabile

<!-- pagina 25 -->
Somma degli elementi della matrice
25
1.
#include <stdio.h>
2.
3.
#define ROWS 2
4.
#define COLS 3
5.
int sommaMatrice(const int m[ROWS][COLS]);
6.
7.
int main(void) {
8.
    int m[ROWS][COLS] = { {0,1,2}, {3,4,5} };
9.
10.
    int totale = sommaMatrice(m);
11.
    printf("La somma vale %d\n", totale); // Output: 15
12.
}
13.
14.
int sommaMatrice(const int m[ROWS][COLS]) {
15.
    int s = 0; // accumulatore
16.
    for (size_t i = 0; i < ROWS; i++) {        // ciclo righe
17.
        for (size_t j = 0; j < COLS; j++) {    // ciclo colonne
18.
            s += m[i][j];                      // accumulo elemento
19.
        }
20.
    }
21.
    return s;
22.
}
Versione per matrici a 
dimensione ﬁssa

<!-- pagina 26 -->
Considerazioni ed errori comuni
Errori comuni operando sulle matrici:
• Inizializzazione errata dell’accumulatore o degli indici
• Invertire riga e colonna negli indici. 
Usare m[j][i] al posto di m[i][j] scambia il ruolo di righe e colonne. 
Questo, oltre a causare errori logici, può portare anche ad accessi fuori 
dalla matrice
• Accesso fuori intervallo. 
In C non esiste controllo sugli indici: se i ≥ rows o j ≥ cols, l’accesso 
genera Undeﬁned Behavior con conseguenze impredicibili: 
leggere/scrivere celle non appartenenti alla matrice, corrompere altre 
variabili sullo stack, causare crash, …
26

<!-- pagina 27 -->
Buone pratiche nell’uso delle matrici
• Usare size_t per gli indici.
È il tipo standard per rappresentare dimensioni e indici di array. Inoltre previene 
errori di segno (non può essere negativo)
• Deﬁnire le dimensioni con simboli invece che con numeri magici.
Deﬁnire ROWS, COLS come costanti rende il codice più leggibile e modiﬁcabile
 
#define ROWS 10
• Isolare la logica in funzioni riutilizzabili.
Incapsulare il calcolo in una funzione sommaMatrice evita duplicazioni di codice, 
e migliora chiarezza e testabilità del programma
• Usare const nei parametri se la matrice non deve essere modiﬁcata.
int sommaMatrice(size_t rows, size_t cols, const int m[rows][cols]);
Il qualiﬁcatore const impedisce modiﬁche accidentali agli elementi della matrice 
all’interno della funzione. Inoltre rende esplicito che la funzione esegue solo 
lettura dei dati (autodocumentazione)
27

<!-- pagina 28 -->
Somma di matrici
Operazione su più matrici, somma di 
elementi in posizioni corrispondenti
28

<!-- pagina 29 -->
Somma di matrici: definizione
Date due matrici A e B di uguali dimensioni:
29
la somma di matrici è una nuova matrice C = A + B, della stessa 
dimensione degli addendi, e i cui elementi sono deﬁniti come:
Ogni elemento della matrice risultato C è la somma, elemento 
per elemento, di A e B.

<!-- pagina 30 -->
Somma di matrici: esempio
Siano
30
Allora:

<!-- pagina 31 -->
Somma di matrici: schema dell algoritmo
Per realizzare la somma di matrici, ci serve quindi una 
scansione delle matrici A e B per accedere agli elementi 
nelle medesime posizioni.
●Due cicli annidati:
●per ogni riga (indice i)
●per ogni colonna (indice j)
●C[i][j] = A[i][j] + B[i][j]
Ogni coppia (i, j) è usata per accedere alle medesime 
posizioni nelle tre matrici.
Traduciamo in C questo schema
31

<!-- pagina 32 -->
Somma di matrici
1.
void sommaMatrici(size_t rows, size_t cols,
2.
                  const int a[rows][cols],
3.
                  const int b[rows][cols],
4.
                        int c[rows][cols])
5.
{
6.
    for (size_t i = 0; i < rows; i++) {
7.
        for (size_t j = 0; j < cols; j++) {
8.
            c[i][j] = a[i][j] + b[i][j];
9.
        }
10.
    }
11.
}
32
• I parametri a, b e c sono matrici contigue di eguali dimensioni
• L’uso di const chiarisce che a e b sono in input, mentre c 
(non-const) è scritta come output.

<!-- pagina 33 -->
Somma di matrici
1.
#include <stdio.h>
2.
#define ROWS 2
3.
#define COLS 3
4.
5.
int main(void) {
6.
    int m1[ROWS][COLS] = {{0,1,2}, {3,4,5}};
7.
    int m2[ROWS][COLS] = {{6,7,8}, {9,10,11}};
8.
    int s[ROWS][COLS];
9.
10.
    sommaMatrici(ROWS, COLS, m1, m2, s);
11.
12.
    printf("Matrice somma:\n");
13.
    for (size_t i = 0; i < ROWS; i++) {
14.
        for (size_t j = 0; j < COLS; j++) {
15.
            printf("%2d ", s[i][j]);
16.
        }
17.
        printf("\n");
18.
    }
19.
}
33
Matrice somma:
6  8  10
12 14 16

<!-- pagina 34 -->
Esercizi: trasposizione
Trasposizione in-place di una matrice quadrata:
Calcoliamo AT dato A:
34
Esempio:

<!-- pagina 35 -->
Esercizi: trasposizione
Trasposizione in-place di una matrice quadrata:
Seguiamo quindi questo prototipo
35
// Trasposizione in-place di una matrice quadrata n×n
// Input:  matrice a[n][n]
// Output: la stessa matrice a viene modificata, 
//         scambiando A[i][j] con A[j][i]
void trasponiMatrice(size_t n, int a[n][n]);

<!-- pagina 36 -->
Esercizi: prodotto scalare-matrice
Prodotto scalare di una matrice per una costante:
Dati una matrice A ed un valore scalare k:
36
Calcoliamo il prodotto kA cioè una nuova matrice C
// Moltiplica ogni elemento della matrice per una costante scalare
// Input:  scalare k, matrice a[rows][cols]
// Output: matrice risultato c[rows][cols] con c[i][j] = k * a[i][j]
void prodottoScalareMatrice(size_t rows, size_t cols, int k,
                            const int a[rows][cols], 
                                  int c[rows][cols]);

<!-- pagina 37 -->
Esercizi: prodotto matrice-matrice
Prodotto matrice⨉matrice:
Date le matrici rettangolari A e B, deﬁniamo C
37
dove gli elementi di C sono deﬁniti come

<!-- pagina 38 -->
Esercizi: prodotto matrice-matrice
Prodotto matrice⨉matrice:
Esempio:
38
Otteniamo il prodotto:

<!-- pagina 39 -->
Esercizi: prodotto matrice-matrice
Prodotto matrice⨉matrice:
Seguiamo questo prototipo:
39
// Calcola il prodotto di due matrici A (m×n) e B (n×p)
// Input:  A[m][n], B[n][p]
// Output: C[m][p] = A × B
void prodottoMatrici(size_t m, size_t n, size_t p,
                     const int a[m][n],
                     const int b[n][p],
                           int c[m][p]);

<!-- pagina 40 -->
Esercizi: prodotto matrice-matrice
Prodotto matrice⨉matrice: test.
40
1.
void prodottoMatrici(size_t m, size_t n, size_t p, const int a[m][n],
2.
                     const int b[n][p], int c[m][p]);
3.
4.
#define M 2
5.
#define N 3
6.
#define P 2
7.
int main(void) {
8.
    int m1[M][N] = {{1,2,3}, {4,5,6}};
9.
    int m2[N][P] = {{7,8}, {9,10}, {11,12}};
10.
    int prod[M][P];
11.
12.
    prodottoMatrici(M, N, P, m1, m2, prod);
13.
    printf("Matrice prodotto:\n");
14.
    for (size_t i = 0; i < M; i++) {
15.
        for (size_t j = 0; j < P; j++) {
16.
            printf("%2d ", prod[i][j]);
17.
        }
18.
        printf("\n");
19.
    }
20.
}

<!-- pagina 41 -->
Ricerca del massimo con 
selezione
Selezione elementi in una matrice
41

<!-- pagina 42 -->
Ricerca del massimo con selezione
Deﬁniamo un problema di ricerca su matrici con selezione.
• Input: Una matrice m di interi, di dimensione rows × cols, della 
quale si considerano solo gli elementi strettamente positivi 
(m[i][j] > 0)
• Output: La posizione (iMax, jMax) dell’elemento positivo di valore 
massimo nella matrice.  Se tale elemento esiste, ritorna true.
Se non esistono elementi strettamente positivi, allora la funzione 
deve segnalare l’assenza ritornando false e assegnando:
iMax = rows, jMax = cols   (valori sentinella fuori intervallo)
• Esempio:
m = { {0, -1, 2}, 
      {3,  5, 4} } → massimo = 5 in posizione (1,1)
42

<!-- pagina 43 -->
Ricerca del massimo con selezione
Formalizzazione matematica. Sia m matrice di interi con 
rows righe e cols colonne.
43
Deﬁniamo l’insieme degli indici validi:
• Caso 1: nessun elemento positivo
• Caso 2: esistono elementi positivi

<!-- pagina 44 -->
Dalla formulazione alla soluzione
• Scandire la matrice con due cicli annidati (i righe, j colonne)
• Durante la scansione teniamo traccia del valore massimo, per decidere 
se l’elemento visitato supera il massimo trovato ﬁno a quel punto
• Inizializziamo gli indici iMax e jMax con i valori sentinella, e esistePos a 
false (all’inizio non sappiamo se la matrice contiene elementi positivi)
• Per ogni elemento m[i][j]:
■Se m[i][j] > 0 && m[i][j] > max
■aggiorna max = m[i][j],  aggiorna iMax = i, jMax = j  e esistePos = true
• Al termine: se esiste almeno un positivo, (iMax, jMax) allora è la posizione 
del massimo; altrimenti restano i valori sentinella (rows, cols) impostati 
inizialmente
44

<!-- pagina 45 -->
Ricerca del massimo con selezione
45
1.
// Ricerca del massimo positivo in una matrice
2.
// Restituisce la posizione (iMax, jMax) tramite parametri puntatore.
3.
// Se non esiste alcun elemento > 0, assegna le posizioni (rows, cols).
4.
// Ritorna true se esiste un elemento > 0 nella matrice, false altrimenti
5.
bool ricercaMaxPos(size_t rows, size_t cols, const int m[rows][cols],
6.
                   size_t *iMax, size_t *jMax)
7.
{
8.
    int max = 0;                // valore sentinella per il massimo
9.
    *iMax = rows;               // valori sentinella iniziali per le posizioni
10.
    *jMax = cols;
11.
    bool esistePos = false;     // non abbiamo ancora iniziato la scansione
12.
13.
    for (size_t i = 0; i < rows; i++) { // ciclo esterno sulle righe
14.
        for (size_t j = 0; j < cols; j++) { // ciclo interno sulle colonne
15.
            if (m[i][j] > 0 && m[i][j] > max) {
16.
                max = m[i][j];
17.
                *iMax = i;
18.
                *jMax = j;
19.
                esistePos = true; // trovato un elemento positivo
20.
            }
21.
        }
22.
    }
23.
    return esistePos;
24.
}

<!-- pagina 46 -->
Considerazioni
• In questo caso possiamo tradurre la condizione di selezione (valore 
positivo) e il superamento del massimo in un’unica condizione
m[i][j] > 0 && m[i][j] > max
• max è inizializzato a 0 perché consideriamo solo elementi positivi (ma 
0 non sarebbe una inizializzazione adatta per una ricerca del massimo 
in un array/matrice qualunque)
• Al primo elemento positivo, esistePos viene impostato a true
• const chiarisce che la funzione non modiﬁchi la matrice
• La scelta dei valori sentinella (rows, cols) è logica: rappresentano indici 
fuori intervallo
• L’uso di parametri puntatore (*iMax, *jMax) permette di restituire più 
valori dalla funzione
46

<!-- pagina 47 -->
Verifica proprietà
Condizioni su tutti gli elementi della 
matrice
47

<!-- pagina 48 -->
Verifica di proprietà
Deﬁniamo un problema di veriﬁca di proprietà su matrici.
• Input. 
– Una matrice m di interi, di dimensione rows × cols
– Una proprietà logica Cond(x) che, dato un elemento x della 
matrice, può essere vera o falsa
• Output. Un valore booleano:
– true se tutti gli elementi della matrice veriﬁcano la proprietà 
Cond(.)
– false altrimenti
Esempio: se Cond(x) è “x è pari”  (x % 2 == 0):
48
→ true
→ false (perché 3 non è pari).

<!-- pagina 49 -->
Verifica di proprietà
Deﬁniamo il problema come un test d’ipotesi.
• Ipotesi nulla (o iniziale) H₀: Tutti gli elementi soddisfano la 
proprietà:
∀(i,j) : Cond(m[i][j]) è true
• Ipotesi alternativa (o di ricerca) H₁: Esiste almeno un elemento che 
viola la proprietà:
∃(i,j) : Cond(m[i][j]) è false
• Il problema diventa quindi un test logico: tramite scansione lineare 
su matrice riﬁutiamo H₀ se esiste almeno una violazione, altrimenti 
se arriviamo in fondo alla scansione accettiamo H₀ (tutti gli elementi 
soddisfano la proprietà)
49

<!-- pagina 50 -->
Strategia di soluzione
• Si ipotizza inizialmente che H₀ sia vera 
→ impostiamo una variabile sentinella booleana 
tuttiOK = true;
• Si scansiona la matrice con due cicli annidati
– Ad ogni passo si veriﬁca Cond(m[i][j])
• Se la condizione non è rispettata, impostiamo
tuttiOK = false 
e si può interrompere la ricerca
• Alla ﬁne si restituisce il valore di tuttiOK
50

<!-- pagina 51 -->
Verifica di proprietà
1.
// Verifica che tutti gli elementi della matrice siano pari
2.
bool verificaTuttiPari(size_t rows, size_t cols, const int m[rows][cols]) {
3.
    bool tuttiOk = true; // Assumiamo H0 inizialmente vera, tutti soddisfano
4.
    for (size_t i = 0; i < rows && tuttiOk; i++) {
5.
        for (size_t j = 0; j < cols && tuttiOk; j++) {
6.
            if (m[i][j] % 2 != 0) {
7.
                tuttiOk = false; // violazione trovata, H0 rifiutata
8.
            }
9.
        }
10.
    }
11.
    return tuttiOk; // H0 accettata
12.
}
51
1.
int main(void) {
2.
    int m[2][3] = { {2,4,6}, {8,10,12} };
3.
    if (verificaTuttiPari(2, 3, m)) {
4.
        printf("Tutti gli elementi sono pari\n");
5.
    } else {
6.
        printf("Esiste almeno un elemento dispari\n");
7.
    }
8.
}

<!-- pagina 52 -->
Esercizi: esiste riga di zeri
Veriﬁca della proprietà: esiste una riga di soli zeri.
Sia M una matrice di interi
52
Deﬁniamo la proprietà
Veriﬁchiamo se
Casi limiti (logica):
• se rows=0 la formula è falsa (non esistono righe)
• se cols=0 la formula è vera (ogni riga ha vacuamente “tutti zeri”, non 
avendo elementi e quindi non avendo controesempi)

<!-- pagina 53 -->
Esercizi: esiste riga di zeri
Veriﬁca della proprietà: esiste una riga di soli zeri.
Seguiamo questo prototipo
53
// existsRowAllZeros
// Input:  rows righe, cols colonne, matrice m[rows][cols] (sola lettura)
// Output: true  se esiste almeno una riga i tale che 
//               per tutti i,j : m[i][j]==0.
//         false altrimenti
bool existsRowAllZeros(size_t rows, size_t cols, const int m[rows][cols]);

<!-- pagina 54 -->
Esercizi: esiste riga di zeri - test
54
#include <assert.h>
#include <stdio.h>
#include <stddef.h>   // size_t
#include <stdbool.h>  // bool
int main(void) {
    // Caso 1: esiste una riga tutta zero (riga 1)
    #define R1 3
    #define C1 4
    int m1[R1][C1] = { {1, 0, 2, 0},
                       {0, 0, 0, 0},  // tutta zeri
                       {5, 6, 0, 7} };
    assert(existsRowAllZeros(R1, C1, m1) == true);
    // Caso 2: nessuna riga tutta zero
    #define R2 2
    #define C2 3
    int m2[R2][C2] = { {0, 1, 0}, {2, 0, 3} };
    assert(existsRowAllZeros(R2, C2, m2) == false);
    // Caso 3: matrice 1x3 tutta zero → true
    #define R3 1
    #define C3 3
    int m3[R3][C3] = { {0, 0, 0} };
    assert(existsRowAllZeros(R3, C3, m3) == true);
    // Caso 4: matrice 3x1 con una riga zero → true
    #define R4 3
    #define C4 1
    int m4[R4][C4] = { {5}, {0}, {7} }; // una riga con tutta zeri (un solo elemento)
    assert(existsRowAllZeros(R4, C4, m4) == true);
    // Caso 5: matrice 0xN (nessuna riga) — non istanziabile come VLA 0,
    assert(existsRowAllZeros(0, 0, NULL) == false);
}

<!-- pagina 55 -->
Esercizi: esiste riga di zeri
55
1.
// existsRowAllZeros
2.
// Input:  rows righe, cols colonne, matrice m[rows][cols] (sola lettura)
3.
// Output: true  se esiste almeno una riga i tale che per tutti i,j : m[i][j]==0
4.
//         false altrimenti
5.
bool existsRowAllZeros(size_t rows, size_t cols, const int m[rows][cols]) {
6.
    bool esisteRiga = false;      // ipotesi H0: non ci sono righe di tutti zeri
7.
    for (size_t i = 0; i < rows && !esisteRiga; ++i) {
8.
        bool allZero = true;      // ipotesi H0b: la riga i è tutta a zeri
9.
        for (size_t j = 0; j < cols && allZero; ++j) {
10.
            if (m[i][j] != 0) {   // trovato un elemento ≠ 0 nella riga i
11.
                allZero = false;  // H1b: la riga i NON è tutta a zeri 
12.
            }
13.
        }
14.
        if (allZero) { // trovata riga tutta zero
15.
            esisteRiga = true;    // H1: esiste riga di soli zeri
16.
        }
17.
    }
18.
    return esisteRiga;
19.
}

<!-- pagina 56 -->
Struttura logica: 2 test d’ipotesi annidati
1. Ipotesi esterna (sulla matrice intera)
– Variabile sentinella: bool esisteRiga = false
– Interpretazione H₀: “non esiste alcuna riga tutta a zero”
– Procedura di confutazione: si scansionano le righe; se si trova una 
riga tutta a zero, si pone esisteRiga = true e si termina 
(short-circuit grazie alla guardia: i < rows && !esisteRiga)
2. Ipotesi interna (sulla riga corrente)
– Variabile sentinella: bool allZero = true
– Interpretazione H₀ᵇ: “la riga i-esima è tutta a zero”
– Procedura di confutazione: si scansionano gli elementi della riga; 
alla prima cella m[i][j] != 0, si pone allZero = false e si interrompe il 
ciclo interno (short-circuit grazie alla guardia: j < cols && allZero)
56

<!-- pagina 57 -->
Struttura logica: correttezza
Al termine:
• Ipotesi H₀ veriﬁcata: 
– esisteRiga == false (il valore iniziale)
– allora per ogni riga i esiste almeno un j con m[i][j] != 0
∀ i ∈ [0, rows) : ( ∃ j ∈ [0, cols) : m[i][j] ≠ 0 )
• Ipotesi H₀ falsiﬁcata: 
– esisteRiga == true (trovata riga di zeri con il test d’ipotesi interno)
– allora esiste almeno una riga i con m[i][j] == 0 per tutti gli 
indici j
∃ i ∈ [0, rows) : ( ∀ j ∈ [0, cols) : m[i][j] = 0 )
57

<!-- pagina 58 -->
Esercizi
Esercizio: scrivere una funzione che prende in input una 
matrice di interi M e ritorni true se tutte le righe hanno 
almeno un elemento il cui valore è compreso nell’intervallo 
[minVal, maxVal]
Esercizio: scrivere una funzione che prende in input una 
matrice di interi M e ritorni true se esiste almeno una riga 
per la quale tutte le coppie di elementi adiacenti appaiono 
in ordine non decrescente
58
