# Capitolo 52: Esercizi Svolti sulle Matrici: le Soluzioni del Docente
## Da dove vengono
Dopo la lezione sulle matrici il docente ha pubblicato le soluzioni, con i test, di tre esercizi: i due lasciati alla fine delle slide sulla verifica di proprietà (capitolo 49) e il prodotto di matrici (capitolo 48). Il codice è riportato qui con piccoli adattamenti di formato. I due esercizi di verifica hanno la stessa idea di fondo: la proprietà da verificare sulla matrice è una quantificazione su una quantificazione («per ogni riga esiste…», «esiste una riga in cui per ogni…»), e il docente la scompone in **due funzioni**: una che lavora su un array, e una che la applica a ogni riga della matrice.

## Esercizio 1: tutte le righe hanno un elemento nell'intervallo
Il testo: scrivere una funzione che riceve una matrice di interi M e restituisce `true` se tutte le righe hanno almeno un elemento con valore nell'intervallo [minVal, maxVal]. In formule la proprietà è

∀ i ∈ [0, rows): ∃ j ∈ [0, cols): minVal ≤ M[i][j] ≤ maxVal

cioè un «per ogni» fuori e un «esiste» dentro. Il «per ogni» riguarda le righe; l'«esiste» riguarda gli elementi di una singola riga, ed è una ricerca lineare su un array (capitolo 35). Per esempio, nella matrice con righe 7, 8, 1, −2 / −3, −1, −5, 0 / 10, 99, 13, 42 e con l'intervallo [0, 10] la risposta è `true`: la prima riga contiene 7, la seconda 0, la terza 10. Con l'intervallo [7, 8] la risposta è `false`, perché la seconda riga non contiene né 7 né 8.

La parte interna diventa una funzione sugli array:

```c
// esisteElemInIntervalloInArray
// Input: array a di lunghezza aLen
//        minVal, maxVal : estremi dell'intervallo (si assume minVal <= maxVal)
// Output:
//  true  se esiste almeno un a[i] tale che minVal <= a[i] <= maxVal
//  false altrimenti
bool esisteElemInIntervalloInArray(size_t aLen, const int a[aLen],
                                   int minVal, int maxVal)
{
    // array a può essere NULL ma solo se ha lunghezza zero
    assert(aLen == 0 || a != NULL);
    // intervallo di valori [minVal, maxVal] deve essere coerente
    assert(minVal <= maxVal);

    bool esisteElem = false; // H0: non esiste alcun elemento valido
    for (size_t i = 0; i < aLen && !esisteElem; i++) {
        if (minVal <= a[i] && a[i] <= maxVal) {
            esisteElem = true; // H1: trovato
        }
    }
    return esisteElem;
}
```

È la ricerca lineare con la sentinella nella condizione del ciclo: l'ipotesi iniziale H₀ è «non esiste», e la si abbandona al primo elemento che cade nell'intervallo. La condizione `minVal <= a[i] && a[i] <= maxVal` è l'appartenenza a un intervallo chiuso scritta come congiunzione di due confronti (capitolo 18). Le due `assert` sono le precondizioni (capitolo 34): l'array può essere `NULL` solo se è vuoto, e l'intervallo deve avere senso.

La parte esterna scorre le righe e chiama la funzione su ciascuna:

```c
// tutteRigheConElemInIntervallo
//  Verifica se, per TUTTE le righe di una matrice m[rows][cols],
//   esiste almeno un elemento nell'intervallo [minVal, maxVal].
bool tutteRigheConElemInIntervallo(size_t rows, size_t cols,
                                   const int m[rows][cols],
                                   int minVal, int maxVal)
{
    // intervallo di valori [minVal, maxVal] deve essere coerente
    assert(minVal <= maxVal);
    // m può essere NULL solo se non verrà dereferenziata (rows==0 oppure cols==0)
    assert((rows == 0 || cols == 0) || m != NULL);

    // H0: tutte le righe hanno almeno un elemento nell'intervallo
    bool tutteRighe = true;
    for (size_t i = 0; i < rows && tutteRighe; i++) {
        if (!esisteElemInIntervalloInArray(cols, m[i], minVal, maxVal)) {
            // trovata una riga che smentisce l'affermazione
            tutteRighe = false;
        }
    }
    return tutteRighe;
}
```

Qui lo schema è la verifica universale (capitolo 36): si suppone vero che tutte le righe vadano bene, e la prima riga senza elementi nell'intervallo fa cadere l'ipotesi. L'argomento `m[i]` è la riga `i`, un array di `cols` interi, che si passa a una funzione sugli array insieme alla sua lunghezza `cols`, esattamente come nel capitolo 47.

I casi limite seguono dalla logica dei quantificatori sul dominio vuoto (capitolo 37):

- con `rows == 0` la risposta è `true`: un «per ogni» su un insieme vuoto di righe è vero in modo vacuo, e infatti il ciclo non parte e `tutteRighe` resta `true`;
- con `cols == 0` e `rows > 0` la risposta è `false`: ogni riga è vuota, e in un array vuoto non esiste alcun elemento nell'intervallo; la prima chiamata restituisce `false` e la verifica si ferma.

È il comportamento rovesciato rispetto a `existsRowAllZeros` del capitolo 49, dove senza colonne la risposta era vera: lì il quantificatore interno era un «per ogni», qui è un «esiste».

## I test dell'esercizio 1
Il `main` del docente prova separatamente le due funzioni con delle `assert`, dentro due blocchi tra graffe. Per la funzione sugli array, con `a1 = {1, 5, 9}`:

- intervallo [4, 6]: `true`, per il 5;
- intervallo [10, 20]: `false`;
- intervallo [5, 5], con gli estremi coincidenti: `true`, perché l'intervallo è chiuso;
- array vuoto, `esisteElemInIntervalloInArray(0, NULL, 0, 100)`: `false`.

Per la funzione sulle matrici, con la matrice 3 × 4 dell'esempio sopra: [7, 8] dà `false`, [0, 10] dà `true`, [100, 200] dà `false`; poi i due casi limite `tutteRigheConElemInIntervallo(2, 0, NULL, -1, 1)`, che dà `false`, e `tutteRigheConElemInIntervallo(0, 3, NULL, -100, 100)`, che dà `true`; infine una matrice 2 × 3 con righe 5, 1, 2 e 0, −1, 1 e l'intervallo [1, 1], in cui ogni riga contiene esattamente un 1: `true`. Se tutte le `assert` passano, il programma stampa `Tutti i test sono passati.`

## Esercizio 2: esiste una riga in ordine non decrescente
Il testo: scrivere una funzione che riceve una matrice di interi M e restituisce `true` se esiste almeno una riga in cui tutte le coppie di elementi adiacenti sono in ordine non decrescente. In formule:

∃ i ∈ [0, rows): ∀ j ∈ [1, cols): M[i][j−1] ≤ M[i][j]

Questa volta l'«esiste» è fuori e il «per ogni» è dentro, e il «per ogni» è il test di ordinamento di un array con gli indici delle coppie (capitolo 39). La funzione sugli array:

```c
// arrayInOrdineNonDecr
// Verifico se l'array a[0..aLen) è ordinato in modo non decrescente
//        a[j-1] <= a[j]    per ogni j in [1, aLen)
bool arrayInOrdineNonDecr(size_t aLen, const int a[])
{
    // array a può essere NULL ma solo se ha lunghezza zero
    assert(aLen == 0 || a != NULL);

    // H0: assumiamo ordinato finché non troviamo un controesempio
    bool ordinato = true;

    // j scorre le coppie adiacenti (a[j-1], a[j]), con j in [1, aLen)
    for (size_t j = 1; j < aLen && ordinato; j++) {
        if (a[j-1] > a[j]) {
            ordinato = false; // H1: controesempio trovato
        }
    }
    return ordinato;
}
```

L'indice `j` parte da 1 e indica il secondo elemento della coppia `(a[j-1], a[j])`: così non si esce mai dall'array e con `aLen` uguale a 0 o a 1 il ciclo non parte, e l'array risulta ordinato. Il controesempio è una coppia con `a[j-1] > a[j]`; elementi uguali vanno bene, perché si chiede l'ordine **non decrescente**. La funzione sulle matrici:

```c
// esisteRigaInOrdineNonDecr
// Verifica se ESISTE almeno una riga della matrice m[rows][cols]
//   che sia ordinata in modo non decrescente.
bool esisteRigaInOrdineNonDecr(size_t rows, size_t cols,
                               const int m[rows][cols])
{
    // m può essere NULL solo se non verrà dereferenziata (rows==0 oppure cols==0)
    assert((rows == 0 || cols == 0) || m != NULL);

    // H0: ipotesi iniziale: non esiste riga ordinata
    bool esisteRigaOrdinata = false;

    for (size_t i = 0; i < rows && !esisteRigaOrdinata; i++) {
        // verifichiamo se la riga i-esima è ordinata
        if (arrayInOrdineNonDecr(cols, m[i])) {
            esisteRigaOrdinata = true;   // trovata riga in ordine
        }
    }
    return esisteRigaOrdinata;
}
```

È una ricerca lineare sulle righe, che si ferma alla prima riga ordinata. I casi limite: con `rows == 0` la risposta è `false` (non esistono righe), con `cols == 0` e `rows > 0` è `true` (ogni riga è vuota, e un array vuoto è ordinato in modo vacuo). Sono gli stessi di `existsRowAllZeros`, che ha la stessa forma «esiste-per ogni».

I test del docente: per gli array, `{-3, -3, 0, 5, 7, 7, 9}` è ordinato (i duplicati sono ammessi), `{5, 4, 3, 2, 1}` no, `{1, 2, 2, 0, 4}` no (la coppia 2, 0 viola l'ordine), `{42}` sì e l'array vuoto sì. Per le matrici, in una 3 × 5 con righe 3, 1, 2, 2, 8 / −5, −5, −1, 0, 7 / 10, 9, 8, 7, 6 solo la seconda riga è ordinata, e la risposta è `true`; una 2 × 4 con righe 2, 1, 1, 1 e 7, 6, 6, 6 dà `false`; una 1 × 1 dà `true`; infine `(0, 3, NULL)` dà `false` e `(2, 0, NULL)` dà `true`.

## Perché due funzioni
In `existsRowAllZeros` (capitolo 49) i due test d'ipotesi erano scritti uno dentro l'altro, con due cicli annidati nella stessa funzione. Le soluzioni del docente mostrano l'alternativa: il test interno diventa una funzione su un array, e la funzione sulla matrice resta un solo ciclo sulle righe. I vantaggi sono quelli della scomposizione in funzioni (capitolo 29):

- ogni funzione ha un solo quantificatore, e quindi un solo schema da controllare (ricerca lineare o verifica universale);
- la funzione sugli array si può provare da sola, con i suoi test, prima di usarla sulle righe;
- la stessa funzione si riusa altrove: `arrayInOrdineNonDecr` serve anche per un array qualsiasi, non solo per le righe di una matrice;
- non c'è il rischio, visto nel capitolo 49, di dimenticare di reinizializzare la sentinella interna a ogni riga: ogni chiamata parte con la sua variabile locale nuova.

(In parole povere: invece di scrivere un ciclo dentro un ciclo, si scrive prima una funzione che risponde alla domanda su una riga sola, e poi si fa la stessa domanda a tutte le righe una dopo l'altra.)

## I blocchi di test
I due `main` sono organizzati in **blocchi**: ogni gruppo di test è racchiuso tra graffe, e le variabili dichiarate dentro un blocco esistono solo lì. Nel secondo `main` il docente definisce le lunghezze con `#define` (`A1_LEN`, `A2_LEN`, …). Le graffe limitano le variabili ma non le `#define`, che il preprocessore elabora prima della compilazione ignorando i blocchi: una seconda `#define` con lo stesso nome e un valore diverso, anche in un altro blocco, sarebbe una ridefinizione (precisazione aggiunta).

I file del docente iniziano con gli `#include` necessari: oltre a `<stdio.h>` e `<stddef.h>` (per `size_t`), servono `<stdbool.h>` per il tipo `bool` e `<assert.h>` per le `assert`.

## Il prodotto di matrici nella versione del docente
Per il prodotto di matrici il capitolo 48 propone una soluzione con un accumulatore locale `s`. Quella del docente usa direttamente l'elemento del risultato come accumulatore:

```c
// Calcola il prodotto di due matrici A (m×n) e B (n×p)
// Input:  A[m][n], B[n][p]
// Output: C[m][p] = A × B
void prodottoMatrici(size_t m, size_t n, size_t p,
                     const int a[m][n],
                     const int b[n][p],
                           int c[m][p])
{
    // ciclo per le m righe di C
    for (size_t i = 0; i < m; i++) {
        // ciclo interno per le p colonne di C
        for (size_t j = 0; j < p; j++) {
            // somma dei prodotti della riga i-esima di A
            // con la colonna j-esima di B
            c[i][j] = 0; // accumulatore sommatoria
            for (size_t k = 0; k < n; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}
```

Le due versioni sono equivalenti: in entrambe l'accumulatore viene azzerato per ogni nuovo elemento `(i, j)`, appena prima del ciclo su `k`, che è il punto delicato già discusso nel capitolo 48. Con le matrici di prova del docente, A con righe 1, 2, 3 / 4, 5, 6 e B con righe 7, 8 / 9, 10 / 11, 12, il programma stampa `Matrice prodotto:` seguito dalle righe 58 64 e 139 154.

## Riepilogo
- «Tutte le righe hanno un elemento in [minVal, maxVal]» è ∀ i ∃ j: verifica universale sulle righe, ricerca lineare dentro ogni riga.
- «Esiste una riga in ordine non decrescente» è ∃ i ∀ j: ricerca lineare sulle righe, test di ordinamento dentro ogni riga.
- Il docente scompone ogni proprietà in una funzione sugli array, chiamata su `m[i]` con lunghezza `cols`, e in una funzione sulla matrice con un solo ciclo.
- Casi limite: senza righe, il «per ogni» è vero e l'«esiste» è falso; senza colonne, decide il quantificatore interno.
- Nel prodotto di matrici si può accumulare direttamente in `c[i][j]`, purché lo si azzeri prima di ogni sommatoria.
