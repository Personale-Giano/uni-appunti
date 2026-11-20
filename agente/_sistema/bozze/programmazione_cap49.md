# Capitolo 49: Ricerca e Verifica di Proprietà sulle Matrici
## La ricerca del massimo con selezione
Il problema unisce due schemi già visti sugli array: la ricerca del massimo (capitolo 24) e la selezione degli elementi che soddisfano una condizione (capitolo 38).
- **Input**: una matrice `m` di interi, di dimensione rows × cols, di cui si considerano solo gli elementi strettamente positivi, cioè con m[i][j] > 0.
- **Output**: la posizione (iMax, jMax) dell'elemento positivo di valore massimo. Se un elemento positivo esiste, la funzione restituisce `true`. Se non ci sono elementi strettamente positivi, deve segnalarlo restituendo `false` e assegnando iMax = rows e jMax = cols, **valori sentinella** fuori dall'intervallo degli indici.

Per esempio, nella matrice con righe 0, −1, 2 e 3, 5, 4 il massimo positivo è 5, in posizione (1, 1).

## La formalizzazione
Sia m una matrice di interi con rows righe e cols colonne. Si definisce l'insieme degli **indici validi**, cioè delle posizioni degli elementi positivi:

P = { (i, j) | m[i][j] > 0 }

Ci sono due casi:
- **caso 1**, nessun elemento positivo: P = ∅, e allora (i_{max}, j_{max}) = (rows, cols);
- **caso 2**, esistono elementi positivi: (i_{max}, j_{max}) ∈ P è tale che m[i_{max}][j_{max}] = max_{(i,j) ∈ P} m[i][j].

Se il massimo compare più volte, le slide non dicono quale posizione scegliere; il codice qui sotto restituisce la prima che incontra nell'ordine di scansione per righe, perché aggiorna solo con un valore strettamente maggiore (precisazione aggiunta).

## Dalla formulazione alla soluzione
La strategia:
- si scandisce la matrice con due cicli annidati, i sulle righe e j sulle colonne;
- durante la scansione si tiene traccia del valore massimo trovato fino a quel punto, per decidere se l'elemento visitato lo supera;
- all'inizio gli indici iMax e jMax hanno i valori sentinella e una variabile booleana `esistePos` vale `false`, perché non si sa ancora se la matrice contiene elementi positivi;
- per ogni elemento m[i][j], se m[i][j] > 0 e m[i][j] > max, si aggiornano max = m[i][j], iMax = i, jMax = j ed esistePos = true;
- alla fine, se esiste almeno un positivo, (iMax, jMax) è la posizione del massimo; altrimenti restano i valori sentinella impostati all'inizio.

```c
// Ricerca del massimo positivo in una matrice
// Restituisce la posizione (iMax, jMax) tramite parametri puntatore.
// Se non esiste alcun elemento > 0, assegna le posizioni (rows, cols).
// Ritorna true se esiste un elemento > 0 nella matrice, false altrimenti
bool ricercaMaxPos(size_t rows, size_t cols, const int m[rows][cols],
                   size_t *iMax, size_t *jMax)
{
    int max = 0;                // valore sentinella per il massimo
    *iMax = rows;               // valori sentinella iniziali per le posizioni
    *jMax = cols;
    bool esistePos = false;     // non abbiamo ancora iniziato la scansione

    for (size_t i = 0; i < rows; i++) { // ciclo esterno sulle righe
        for (size_t j = 0; j < cols; j++) { // ciclo interno sulle colonne
            if (m[i][j] > 0 && m[i][j] > max) {
                max = m[i][j];
                *iMax = i;
                *jMax = j;
                esistePos = true; // trovato un elemento positivo
            }
        }
    }
    return esistePos;
}
```

Sulla matrice dell'esempio: 0 e −1 non sono positivi; 2 lo è e supera max = 0, quindi max = 2 e la posizione è (0, 2); poi 3 supera 2, posizione (1, 0); poi 5, posizione (1, 1); infine 4 non supera 5. La funzione restituisce `true` con iMax = 1 e jMax = 1.

## Osservazioni sul codice
Le slide sottolineano alcuni punti:
- la condizione di selezione (valore positivo) e il superamento del massimo sono tradotti in un'unica condizione, `m[i][j] > 0 && m[i][j] > max`;
- `max` parte da 0 perché si considerano solo elementi positivi. Non sarebbe un'inizializzazione adatta per la ricerca del massimo in un array o in una matrice qualunque: se tutti gli elementi fossero negativi, nessuno supererebbe lo 0 (nel capitolo 24 il massimo parte dal primo elemento);
- al primo elemento positivo `esistePos` diventa `true`;
- `const` chiarisce che la funzione non modifica la matrice;
- la scelta dei valori sentinella (rows, cols) è logica: sono indici fuori intervallo, che non possono essere confusi con una posizione vera;
- i parametri puntatore `*iMax` e `*jMax` permettono di restituire più valori dalla funzione, come nel passaggio per riferimento simulato del capitolo 32.

Una precisazione aggiunta: poiché max non scende mai sotto 0, se m[i][j] > max allora m[i][j] è già positivo, e la prima parte della condizione sarebbe superflua. Tenerla scritta però rende esplicita la selezione e fa funzionare il codice anche se si cambia il valore iniziale di max.

## La verifica di una proprietà
Il secondo tipo di problema chiede se tutti gli elementi della matrice hanno una certa proprietà: è la quantificazione universale del capitolo 36, estesa alle matrici.
- **Input**: una matrice `m` di interi, di dimensione rows × cols, e una proprietà logica Cond(x) che, dato un elemento x della matrice, può essere vera o falsa.
- **Output**: `true` se tutti gli elementi della matrice verificano Cond, `false` altrimenti.

Per esempio, con Cond(x) = «x è pari», cioè `x % 2 == 0`, la matrice con righe 2, 4 e 6, 8 dà `true`; la matrice con righe 2, 3 e 6, 8 dà `false`, perché 3 non è pari.

Le slide impostano il problema come un **test d'ipotesi**:
- **ipotesi nulla** (o iniziale) H₀: tutti gli elementi soddisfano la proprietà, ∀(i, j): Cond(m[i][j]) è vera;
- **ipotesi alternativa** (o di ricerca) H₁: esiste almeno un elemento che viola la proprietà, ∃(i, j): Cond(m[i][j]) è falsa.

Con una scansione della matrice si **rifiuta H₀** appena si trova una violazione; se si arriva in fondo senza trovarne, si **accetta H₀**.

## La strategia e il codice
- Si suppone all'inizio che H₀ sia vera: una variabile sentinella booleana `tuttiOk` parte da `true`.
- Si scandisce la matrice con due cicli annidati, controllando Cond(m[i][j]) a ogni passo.
- Se la condizione non è rispettata si pone `tuttiOk = false`, e la ricerca si può interrompere.
- Alla fine si restituisce `tuttiOk`.

```c
// Verifica che tutti gli elementi della matrice siano pari
bool verificaTuttiPari(size_t rows, size_t cols, const int m[rows][cols]) {
    bool tuttiOk = true; // Assumiamo H0 inizialmente vera, tutti soddisfano
    for (size_t i = 0; i < rows && tuttiOk; i++) {
        for (size_t j = 0; j < cols && tuttiOk; j++) {
            if (m[i][j] % 2 != 0) {
                tuttiOk = false; // violazione trovata, H0 rifiutata
            }
        }
    }
    return tuttiOk; // H0 accettata
}
```

L'interruzione si ottiene mettendo `&& tuttiOk` nella condizione di **tutti e due** i cicli: appena `tuttiOk` diventa `false` il ciclo interno si ferma, e al controllo successivo si ferma anche quello esterno. Se la guardia fosse solo nel ciclo interno, il ciclo esterno passerebbe comunque alle righe successive, senza però visitarne gli elementi: il risultato sarebbe giusto, ma con giri inutili.

```c
int main(void) {
    int m[2][3] = { {2,4,6}, {8,10,12} };
    if (verificaTuttiPari(2, 3, m)) {
        printf("Tutti gli elementi sono pari\n");
    } else {
        printf("Esiste almeno un elemento dispari\n");
    }
}
```

Qui tutti gli elementi sono pari e viene stampato `Tutti gli elementi sono pari`.

## Esiste una riga di zeri?
L'ultimo esempio combina i due quantificatori. Sia M ∈ ℤ^{rows×cols}. Si definisce la proprietà di una riga

RowZero(i) ⟺ ∀ j ∈ [0, cols): M_{ij} = 0

(la riga i contiene solo zeri), e ci si chiede se

∃ i ∈ [0, rows): RowZero(i),

cioè se esiste almeno una riga fatta solo di zeri. Un «esiste» fuori, un «per ogni» dentro.

Le slide fanno notare i casi limite, che seguono dalla logica dei quantificatori sul dominio vuoto (capitolo 37):
- se rows = 0 la formula è falsa: non ci sono righe, quindi non ne esiste nessuna con la proprietà;
- se cols = 0 (e rows > 0) la formula è vera: ogni riga è «tutta di zeri» in modo vacuo, perché non ha elementi e quindi non ha controesempi.

Il prototipo richiesto è:

```c
// existsRowAllZeros
// Input:  rows righe, cols colonne, matrice m[rows][cols] (sola lettura)
// Output: true  se esiste almeno una riga i tale che
//               per tutti i,j : m[i][j]==0.
//         false altrimenti
bool existsRowAllZeros(size_t rows, size_t cols, const int m[rows][cols]);
```

Nel commento della slide «per tutti i,j» va letto «per ogni j»: la riga i è fissata dall'«esiste», e il «per ogni» riguarda solo le colonne (precisazione aggiunta).

La soluzione delle slide:

```c
bool existsRowAllZeros(size_t rows, size_t cols, const int m[rows][cols]) {
    bool esisteRiga = false;      // ipotesi H0: non ci sono righe di tutti zeri
    for (size_t i = 0; i < rows && !esisteRiga; ++i) {
        bool allZero = true;      // ipotesi H0b: la riga i è tutta a zeri
        for (size_t j = 0; j < cols && allZero; ++j) {
            if (m[i][j] != 0) {   // trovato un elemento ≠ 0 nella riga i
                allZero = false;  // H1b: la riga i NON è tutta a zeri
            }
        }
        if (allZero) { // trovata riga tutta zero
            esisteRiga = true;    // H1: esiste riga di soli zeri
        }
    }
    return esisteRiga;
}
```

## Due test d'ipotesi annidati
La struttura logica è fatta di due test, uno dentro l'altro:
1. **ipotesi esterna**, sulla matrice intera. La sentinella è `bool esisteRiga = false`, che rappresenta H₀: «non esiste alcuna riga tutta a zero». Si scandiscono le righe; se se ne trova una tutta a zero si pone `esisteRiga = true` e ci si ferma, grazie alla guardia `i < rows && !esisteRiga`. È lo schema della ricerca lineare (capitolo 35).
2. **ipotesi interna**, sulla riga corrente. La sentinella è `bool allZero = true`, che rappresenta H₀ᵇ: «la riga i è tutta a zero». Si scandiscono gli elementi della riga; alla prima cella con m[i][j] ≠ 0 si pone `allZero = false` e il ciclo interno si interrompe, grazie alla guardia `j < cols && allZero`. È lo schema della verifica universale.

La variabile `allZero` è dichiarata **dentro** il ciclo esterno: ogni riga ricomincia con l'ipotesi di essere tutta a zero. Se fosse dichiarata una volta sola fuori, dopo la prima riga con un elemento diverso da zero resterebbe `false` per sempre.

Alla fine:
- se `esisteRiga == false` (il valore iniziale), H₀ è confermata: per ogni riga i esiste almeno un j con m[i][j] ≠ 0, cioè ∀ i ∈ [0, rows): (∃ j ∈ [0, cols): m[i][j] ≠ 0);
- se `esisteRiga == true`, H₀ è falsificata: il test interno ha trovato una riga di zeri, cioè ∃ i ∈ [0, rows): (∀ j ∈ [0, cols): m[i][j] = 0).

Le due formule sono una la negazione dell'altra, per le leggi di De Morgan sui quantificatori: negare «esiste una riga in cui tutti sono zero» dà «in ogni riga esiste un elemento diverso da zero».

I casi limite funzionano senza codice apposito: con rows = 0 il ciclo esterno non parte e la funzione restituisce `false`; con cols = 0 il ciclo interno non parte, `allZero` resta `true` e la prima riga basta a restituire `true`.

## I test
Le slide accompagnano la funzione con un `main` di prova basato su `assert` (capitolo 34):
- una matrice 3×4 con la riga 1 tutta di zeri: risultato `true`;
- una matrice 2×3 con righe 0, 1, 0 e 2, 0, 3, senza righe di zeri: `false`;
- una matrice 1×3 tutta di zeri: `true`;
- una matrice 3×1 con righe 5, 0, 7: la riga 1 ha un solo elemento, ed è zero: `true`;
- il caso con zero righe, `existsRowAllZeros(0, 0, NULL)`: `false`. Una matrice VLA con zero righe non si può dichiarare, quindi la prova passa `NULL`; la funzione non lo legge mai, perché il ciclo esterno non parte.

I test coprono un caso positivo, un caso negativo e alcuni casi limite di forma della matrice; il caso con zero colonne, discusso sopra, non è tra le prove.

## Esercizi
Le slide lasciano due esercizi da svolgere:
- scrivere una funzione che riceve una matrice di interi M e restituisce `true` se **tutte** le righe hanno almeno un elemento con valore nell'intervallo [minVal, maxVal];
- scrivere una funzione che riceve una matrice di interi M e restituisce `true` se **esiste** almeno una riga in cui tutte le coppie di elementi adiacenti sono in ordine non decrescente.

Il primo è un «per ogni» fuori e un «esiste» dentro, lo schema rovesciato rispetto a `existsRowAllZeros`; il secondo è un «esiste» fuori e, dentro, il test di ordinamento di una riga (capitolo 39).

## Riepilogo
- Ricerca del massimo con selezione: una sola condizione `m[i][j] > 0 && m[i][j] > max`, valori sentinella (rows, cols) se non ci sono positivi, posizione restituita con parametri puntatore.
- Verifica di proprietà come test d'ipotesi: si suppone H₀ («tutti soddisfano») e la si rifiuta alla prima violazione; la guardia `&& tuttiOk` va in entrambi i cicli.
- «Esiste una riga di zeri» = ∃ i ∀ j: due test annidati, con la sentinella interna reinizializzata a ogni riga.
- Casi limite: senza righe la risposta è falsa, senza colonne è vera in modo vacuo.
