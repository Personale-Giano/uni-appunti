# Capitolo 51: Restituire una Matrice da una Funzione: il Tipo Intermedio e leggiMatrice
## Il problema
L'obiettivo è una funzione che faccia per le matrici quello che `leggiArray` fa per gli array (capitolo 43). La funzione deve:

- leggere da input le dimensioni `rows` e `cols`;
- allocare la matrice nello heap (capitolo 50);
- leggere gli elementi;
- restituire al chiamante sia la matrice sia le sue dimensioni.

Con un array la chiamata era semplice: la funzione restituiva un `int*` e scriveva la lunghezza attraverso un puntatore.

```c
size_t n;
int *a = leggiArray(&n);   // OK
```

Per analogia, con una matrice si vorrebbe scrivere:

```c
size_t rows, cols;
int (*m)[cols] = leggiMatrice(&rows, &cols);   // ERRORE
```

Questa dichiarazione però contiene una dipendenza che il C non può risolvere: il tipo del puntatore restituito, `int (*)[cols]`, dipende da `cols`, e `cols` è noto solo dopo che `leggiMatrice` è tornata.

L'ostacolo si vede da due lati (precisazione aggiunta). Dal lato del chiamante, il tipo di `m` contiene `cols`, e quel tipo viene fissato quando si arriva alla dichiarazione, mentre `cols` riceve il suo valore solo durante la chiamata. Dal lato della funzione, il prototipo di `leggiMatrice` dovrebbe dichiarare come tipo di ritorno un puntatore a matrice con righe di `cols` interi, ma `cols` non è un parametro della funzione: è un valore che la funzione stessa calcolerà leggendolo da input, quindi non c'è modo di scriverlo nell'intestazione.

## Il tipo intermedio
Il linguaggio obbliga quindi a separare il lavoro in due fasi:

- prima si ottengono un puntatore «intermedio», `rows` e `cols`;
- poi si usa `cols`, ormai noto, per definire il tipo preciso del puntatore a matrice.

Il tipo intermedio si dichiara con `typedef`:

```c
typedef int (*int_matrix_ptr_t)[];
```

**Definizione.** La parola chiave `typedef` dà un **nome nuovo a un tipo**: la dichiarazione si scrive come quella di una variabile, e il nome che compare al posto della variabile diventa il nome del tipo. Con `typedef int (*int_matrix_ptr_t)[];` il nome `int_matrix_ptr_t` indica il tipo «puntatore a matrice di interi con righe di lunghezza non specificata».

(In parole povere: è un soprannome. Invece di riscrivere ogni volta la formula `int (*)[]`, si scrive `int_matrix_ptr_t`; e il tipo che quel soprannome indica è un puntatore a matrice di cui non si dice quanto sono lunghe le righe.)

Le slide avvertono che `typedef` non verrà approfondito oltre: il costrutto sarà ripreso in modo sistematico in Programmazione II. Il suffisso `_t` nel nome è solo una convenzione, la stessa di `size_t`.

Con il tipo intermedio il prototipo della funzione si può finalmente scrivere:

```c
int_matrix_ptr_t leggiMatrice(size_t* out_rows,
                              size_t* out_cols);
```

Il tipo intermedio è necessario perché puntatore e dimensioni vengono restituiti separatamente: la lunghezza delle righe il chiamante la conosce solo dopo il ritorno di `leggiMatrice`.

Resta da capire perché il trucco funziona (precisazione aggiunta). Le parentesi quadre vuote rendono la riga un array di lunghezza non specificata, e il C considera un puntatore a `int[]` compatibile con un puntatore a `int[cols]`, qualunque sia `cols`: per questo l'indirizzo passa da un tipo all'altro senza cast. In cambio, con il solo puntatore intermedio non si possono usare gli indici: per calcolare `p[i]` bisognerebbe sapere di quanti byte saltare per passare da una riga all'altra, ed è proprio l'informazione che manca. Il puntatore intermedio serve solo a trasportare l'indirizzo.

## Ricevere la matrice
A questo punto il chiamante ha tutti gli elementi. Prima riceve le dimensioni e il puntatore intermedio:

```c
size_t rows, cols;
int_matrix_ptr_t p = leggiMatrice(&rows, &cols);
```

Poi, quando `cols` ha il suo valore, dichiara un puntatore con il tipo preciso della matrice e gli assegna l'indirizzo:

```c
int (*m)[cols] = p;
```

Da qui in poi `m` si usa normalmente con `m[i][j]` e si può passare alle funzioni già viste, per esempio `stampaMatrice(rows, cols, m)` (capitolo 47). Il `main` completo delle slide è:

```c
int main(void) {
    size_t rows, cols;
    int_matrix_ptr_t p = leggiMatrice(&rows, &cols);

    if (p != NULL) {
        int (*m)[cols] = p;   // puntatore a matrice

        stampaMatrice(rows, cols, m);

        free(m);              // rilascia la memoria heap
        m = p = NULL;
    }
}
```

Il controllo `p != NULL` esclude il caso in cui l'allocazione non sia riuscita. Dopo l'assegnamento `p` e `m` contengono lo stesso indirizzo: sono due puntatori allo stesso blocco (**aliasing**, capitolo 12). Per questo la `free` si chiama una volta sola, su uno dei due (chiamarla su entrambi sarebbe la doppia `free` del capitolo 44), e poi si azzerano **tutti e due** i puntatori: azzerarne uno solo lascerebbe l'altro appeso. L'assegnamento `m = p = NULL;` si legge da destra: prima `p` diventa `NULL`, poi lo stesso valore viene copiato in `m`.

## La funzione leggiMatrice
L'implementazione delle slide:

```c
typedef int (*int_matrix_ptr_t)[];  // dichiarazione del tipo intermedio

int_matrix_ptr_t leggiMatrice(size_t* out_rows, size_t* out_cols) {
    *out_rows = *out_cols = 0;
    size_t rows, cols;
    scanf("%zu%zu", &rows, &cols);  // leggi dimensioni
    int (*m)[cols] = malloc(rows * cols * sizeof(int));  // allocazione

    if (m != NULL) {
        for (size_t i = 0; i < rows; i++) {
            for (size_t j = 0; j < cols; j++) {
                scanf("%d", &m[i][j]);  // inizializzazione
            }
        }
        *out_rows = rows;
        *out_cols = cols;
    }
    return m;
}
```

Passo per passo:

- la prima riga mette subito a 0 le due dimensioni del chiamante: se qualcosa va storto, il chiamante riceve una matrice 0 × 0, come per `selectCopy` del capitolo 45;
- le dimensioni vengono lette in due variabili locali; da questo momento `cols` è noto **dentro** la funzione, e quindi qui si può dichiarare `m` con il suo tipo preciso `int (*)[cols]`, come nel capitolo 50;
- se l'allocazione riesce, due cicli annidati leggono gli elementi riga per riga, nello stesso ordine in cui stanno in memoria; `&m[i][j]` è l'indirizzo dell'elemento, di tipo `int*`, come vuole `scanf`;
- solo alla fine, quando la matrice è pronta, le dimensioni vengono comunicate al chiamante;
- `return m;` restituisce l'indirizzo del blocco convertendolo nel tipo intermedio: è la stessa conversione tra puntatori compatibili vista sopra, nell'altro verso.

Se `malloc` fallisce, la funzione restituisce `NULL` con le dimensioni a 0, e il `main` non entra nell'`if`. Come in `leggiArray`, al ritorno sparisce lo stack frame della funzione con le variabili `rows`, `cols` e `m`, ma il blocco nello heap resta, e da quel momento è responsabilità del chiamante liberarlo (capitolo 45).

![Dopo il ritorno di leggiMatrice: nello stack di main le dimensioni e i due puntatori p e m, che indicano lo stesso blocco nello heap.](figure/prog/leggi_matrice_heap.png|15)

Per esempio, con l'input `2 3` seguito da `1 2 3 4 5 6`, la funzione alloca un blocco di 2 · 3 · `sizeof(int)` byte, lo riempie e restituisce l'indirizzo; il `main` riceve `rows = 2` e `cols = 3` e stampa:

```
[ 1 2 3 ]
[ 4 5 6 ]
```

Come `leggiArray` nel capitolo 43, anche questa versione è essenziale e non controlla il risultato di `scanf` (precisazione aggiunta). Se la lettura delle dimensioni fallisce, `rows` e `cols` restano non inizializzate e la `malloc` riceve un valore indeterminato; una versione più robusta controllerebbe che `scanf` restituisca 2 prima di allocare.

## Riepilogo
- Una funzione non può dichiarare come tipo di ritorno `int (*)[cols]` se `cols` viene calcolato al suo interno, e il chiamante non conosce `cols` prima del ritorno.
- La soluzione è un tipo intermedio, `typedef int (*int_matrix_ptr_t)[];`, cioè un puntatore a matrice con righe di lunghezza non specificata, compatibile con qualunque `int (*)[cols]`.
- La funzione restituisce il puntatore intermedio e scrive `rows` e `cols` attraverso parametri puntatore; il chiamante poi dichiara `int (*m)[cols] = p;` e usa `m[i][j]`.
- Dentro `leggiMatrice` la matrice si dichiara subito con il tipo preciso, perché lì `cols` è già stato letto.
- Alla fine il chiamante libera il blocco con una sola `free` e azzera tutti i puntatori che lo indicavano.

Il capitolo 52 raccoglie le soluzioni del docente degli esercizi sulle matrici svolti a lezione.
