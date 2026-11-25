# Capitolo 20: Laboratorio 7: Intervalli Semiaperti di Indici e Sottosequenze
## Dall'intervallo [0, len) all'intervallo [left, right)
Finora gli indici validi di un array di lunghezza `len` sono stati quelli dell'intervallo semiaperto [0, len) (capitolo 25 della teoria). Molti problemi però lavorano solo su una parte dell'array: le slide generalizzano quindi la nozione di spazio degli indici validi a un **sotto-intervallo** [left, right).

**Definizione.** Dato un array di lunghezza `len`, un **intervallo semiaperto di indici** [left, right) è l'insieme degli indici `i` con left ≤ i < right, dove deve valere 0 ≤ left ≤ right ≤ len. L'estremo sinistro è incluso, quello destro escluso. Il caso base è [left, right) = [0, len), cioè tutto l'array; in generale [left, right) ⊆ [0, len).

(In parole povere: l'estremo `left` è la prima casella che fa parte del pezzo, `right` è la prima casella che **non** ne fa più parte. Come in un righello, dove il segmento da 2 a 5 contiene le caselle 2, 3 e 4.)

![L'intervallo semiaperto [left, right) dentro l'array: left è incluso, right è escluso.](figure/lab/intervallo_semiaperto.png|15)

Le slide elencano le proprietà, prima per [0, len) e poi per il caso generale:

- il numero di elementi è `len`, e in generale `right - left`;
- l'intervallo è vuoto se `0 == len`, e in generale se `left == right`;
- un indice `i` appartiene all'intervallo se 0 ≤ i < len, e in generale se left ≤ i < right;
- se l'intervallo non è vuoto, il primo elemento è `a[0]` e l'ultimo `a[len - 1]`; in generale il primo è `a[left]` e l'ultimo `a[right - 1]`;
- deve sempre valere l'invariante `right >= left`, che si può controllare con `assert(right >= left);` (capitolo 34 della teoria).

Il vantaggio della forma semiaperta è che i conti tornano senza «+1» e «−1»: la lunghezza è una semplice differenza, un intervallo vuoto si scrive [x, x) per qualunque x, e due intervalli consecutivi [a, b) e [b, c) si incollano senza sovrapporsi in [a, c). Per esempio, in un array di 12 elementi l'intervallo [3, 7) contiene gli indici 3, 4, 5 e 6, cioè 7 − 3 = 4 elementi, il primo è `a[3]` e l'ultimo `a[6]`.

Per [0, len) le slide scrivono l'invariante come `assert(len >= 0);`, ma se `len` è un `size_t`, che non può essere negativo, la condizione è sempre vera e l'`assert` non controlla nulla (precisazione aggiunta). L'invariante utile è quello del caso generale, `right >= left`: con indici `size_t`, se fosse violato la lunghezza `right - left` non diventerebbe negativa ma un numero enorme.

Le slide accennano anche agli intervalli di **puntatori** [pLeft, pRight), con le stesse proprietà (numero di elementi `pRight - pLeft`, primo elemento `*pLeft`, ultimo `*(pRight - 1)`), ma avvertono che il corso non li tratterà.

## A che cosa servono gli intervalli
Gli esempi delle slide sono: individuare sotto-intervalli di un array con certe proprietà, cercare una sottosequenza dentro un array e la ricerca binaria (dicotomica). Il consiglio generale è che molti problemi diversi su indici, puntatori e intervalli seguono logiche comuni: conviene applicare in modo coerente un numero ridotto di schemi ricorrenti e consolidati, invece di inventare ogni volta una soluzione nuova. Le funzioni che seguono lo mostrano: sono tutte i soliti schemi (scansione, verifica universale, filtro, copia nello heap), con il ciclo che va da `left` a `right` invece che da 0 a `len`.

## Es 7: il file sottosequenze.c
L'esercizio chiede di implementare le funzioni dichiarate in `07_sottosequenze.c`, seguendo i commenti dei prototipi; il `main` stampa i risultati accanto a quelli attesi. Seguono soluzioni possibili (non nelle slide), controllate a mano su tutti i casi del `main`.

**stampa_sseq.** Stampa gli elementi di [left, right):

```c
void stampa_sseq(const size_t left, const size_t right, const int a[])
{
    assert(left <= right);
    for (size_t i = left; i < right; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}
```

**escludi_zeri_estremi.** Riceve l'intervallo per puntatore, inizializzato a [0, aLen), e lo restringe in modo che gli zeri all'inizio e alla fine ne restino fuori: gli elementi in [0, left) e in [right, aLen) devono essere tutti zeri. Si fa avanzare `left` finché punta a uno zero, poi si fa arretrare `right` finché l'ultimo elemento dell'intervallo, `a[right - 1]`, è uno zero:

```c
void escludi_zeri_estremi(size_t* pLeft, size_t* pRight, const int a[])
{
    assert(*pLeft <= *pRight);
    while (*pLeft < *pRight && a[*pLeft] == 0) {
        (*pLeft)++;                 // il primo elemento è zero: escluso
    }
    while (*pRight > *pLeft && a[*pRight - 1] == 0) {
        (*pRight)--;                // l'ultimo elemento è zero: escluso
    }
}
```

Le parentesi in `(*pLeft)++` sono quelle della domanda 3 del capitolo 17 di questo laboratorio: si incrementa il valore puntato, cioè l'estremo dell'intervallo, non il puntatore. Le guardie `*pLeft < *pRight` e `*pRight > *pLeft` vengono prima dell'accesso all'array, così grazie alla cortocircuitazione non si legge mai fuori dall'intervallo, e l'invariante left ≤ right resta vero. Sui tre casi del `main`:

- `{0, 0, 10, 15, 25, 0, 0, 0}`: `left` avanza fino a 2, `right` arretra da 8 a 5, e l'intervallo è [2, 5), con gli elementi 10 15 25;
- `{4, 7, 8}`: nessuno zero agli estremi, l'intervallo resta [0, 3);
- `{0, 0, 0, 0, 0}`: `left` avanza fino a 5, dove si ferma perché ha raggiunto `right`; il secondo ciclo non parte. L'intervallo è [5, 5), vuoto, come chiede il `main` con «[x, x)».

Il commento del prototipo, con «elementi tutti zeri» fuori dall'intervallo, sarebbe soddisfatto anche lasciando qualche zero dentro; il `main` mostra che si vuole l'intervallo più stretto possibile, ed è quello che fanno i due cicli.

**incrementa_sseq.** Aggiunge `k` a ogni elemento di [left, right). È la trasformazione del capitolo 17 di questo laboratorio, ristretta all'intervallo:

```c
void incrementa_sseq(const size_t left, const size_t right,
                     int a[], const int k)
{
    for (size_t i = left; i < right; i++) {
        a[i] += k;
    }
}
```

Nel `main` `a1` vale `{0, 0, 10, 15, 25, 0, 0, 0}`; dopo `incrementa_sseq(0, 8, a1, 5)` diventa 5 5 15 20 30 5 5 5, e dopo `incrementa_sseq(2, 6, a1, 100)` diventa 5 5 115 120 130 105 5 5, come atteso.

**test_sseq.** Restituisce `true` se tutti gli elementi di [left, right) sono pari e maggiori di `val`. È una verifica universale con sentinella:

```c
bool test_sseq(const size_t left, const size_t right,
               const int a[], const int val)
{
    bool tuttiOk = true;
    for (size_t i = left; i < right && tuttiOk; i++) {
        if (a[i] % 2 != 0 || a[i] <= val) {
            tuttiOk = false;        // controesempio: dispari oppure non maggiore
        }
    }
    return tuttiOk;
}
```

La condizione del controesempio è la negazione di «pari e maggiore di `val`», per De Morgan «dispari oppure non maggiore». Sulla `a1` modificata: in [3, 5) ci sono 120 e 130, pari e maggiori di 110, quindi 1; in [1, 7) il primo elemento è 5, dispari, quindi 0; in [2, 6) c'è 115, dispari (e comunque nessuno supera 200), quindi 0.

**copia_dispari_sseq.** Copia in `b[]`, di capacità `bCap`, gli elementi dispari di [left, right), e scrive in `*p_bLen` quanti ne ha copiati. È il filtro selettivo:

```c
void copia_dispari_sseq(const size_t left, const size_t right, const int a[],
                        size_t* p_bLen, const size_t bCap, int b[])
{
    size_t bLen = 0;
    for (size_t i = left; i < right && bLen < bCap; i++) {
        if (a[i] % 2 != 0) {
            b[bLen] = a[i];
            bLen++;
        }
    }
    *p_bLen = bLen;
}
```

Il test di disparità è `a[i] % 2 != 0` e non `a[i] % 2 == 1`: per un dispari negativo, come −3, in C il resto vale −1, e il secondo test lo scarterebbe. Risultati: in [1, 7) i dispari sono 5 115 105 5; in [0, 8) con capacità 6 sono 5 5 115 105 5 5; con capacità 4 la copia si ferma a 5 5 115 105.

Nel terzo test il `main` del codice iniziale stampa `stampa_sseq(0, b2Len, b1)`, cioè i primi quattro elementi di `b1` invece di `b2` (precisazione aggiunta). Il risultato stampato coincide per caso con quello atteso, perché `b1` contiene ancora i valori del test precedente, ma per controllare davvero la funzione va scritto `b2`.

**copia_sseq.** Copia gli elementi di [left, right) in un nuovo array allocato nello heap; se l'intervallo è vuoto restituisce `NULL` e mette `*p_bLen` a 0. La dimensione è nota subito, `right - left`:

```c
int* copia_sseq(const size_t left, const size_t right, const int a[],
                size_t* p_bLen)
{
    assert(left <= right);
    *p_bLen = 0;
    int* b = NULL;
    const size_t n = right - left;          // numero di elementi dell'intervallo
    if (n > 0) {
        b = malloc(n * sizeof(int));
        if (b != NULL) {
            for (size_t i = 0; i < n; i++) {
                b[i] = a[left + i];         // l'elemento i di b è il left + i di a
            }
            *p_bLen = n;
        }
    }
    return b;
}
```

I due array hanno indici diversi: `b` va da 0 a n, `a` da `left` a `right`, e il legame è `b[i] = a[left + i]`. Risultati: [2, 6) dà 115 120 130 105; [4, 4) è vuoto e dà `NULL` con lunghezza 0; [0, 1) dà 5; [0, 8) dà l'array intero.

**copia_prefisso_minori_di.** Copia in un nuovo array nello heap fino a `max_count` elementi di [0, right) che sono minori di `valore_cercato`; se non ne trova restituisce `NULL` con lunghezza 0. È lo schema conta, alloca, copia, con il limite `max_count` sia nel conteggio sia nella copia:

```c
int* copia_prefisso_minori_di(const size_t right, const int a[],
                              const int valore_cercato,
                              const size_t max_count,
                              size_t* p_bLen)
{
    *p_bLen = 0;
    int* b = NULL;
    // 1) calcolo della dimensione, al massimo max_count
    size_t count = 0;
    for (size_t i = 0; i < right && count < max_count; i++) {
        if (a[i] < valore_cercato) {
            count++;
        }
    }
    // 2) allocazione e 3) copia dei primi count elementi selezionati
    if (count > 0) {
        b = malloc(count * sizeof(int));
        if (b != NULL) {
            size_t j = 0;
            for (size_t i = 0; i < right && j < count; i++) {
                if (a[i] < valore_cercato) {
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

Risultati sulla `a1` modificata (5 5 115 120 130 105 5 5): in [0, 8) i minori di 120 sono 5, 5, 115, 105, 5, 5, ma con `max_count = 3` si copiano i primi tre, 5 5 115; in [0, 6) i minori di 10 sono 5 5; nessun elemento è minore di 0, quindi `NULL` con lunghezza 0; in [0, 3) i minori di 15 sono 5 5. Il nome «prefisso» si riferisce all'intervallo [0, right), che è un prefisso dell'array. Il commento potrebbe anche voler dire «fermati al primo elemento che non è minore»: sui casi del `main` le due letture danno gli stessi risultati, e la soluzione segue la lettura letterale del commento («fino a `max_count` elementi … che sono minori di `valore_cercato`»), da confrontare con eventuali chiarimenti in laboratorio.

## Riepilogo
- Un intervallo semiaperto [left, right) contiene gli indici left ≤ i < right; ha `right - left` elementi, è vuoto se `left == right`, il primo elemento è `a[left]` e l'ultimo `a[right - 1]`.
- L'invariante da controllare è 0 ≤ left ≤ right ≤ len; con indici `size_t`, `assert(len >= 0)` non controlla nulla.
- Le funzioni su un intervallo sono i soliti schemi con il ciclo `for (size_t i = left; i < right; i++)`.
- Per restringere un intervallo si spostano gli estremi passati per puntatore, `(*pLeft)++` e `(*pRight)--`, con le guardie prima dell'accesso all'array.

Il capitolo 21 usa gli stessi intervalli sulle stringhe, scrivendo da zero alcune funzioni di `<string.h>`.
