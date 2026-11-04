# Capitolo 39: Il Test di Ordinamento e gli Indici delle Coppie
## Una proprietà delle coppie
Dato l'array a = [2, 4, 4, 6, 9], vogliamo verificare se è in ordine **non decrescente**: 2 ≤ 4 ≤ 4 ≤ 6 ≤ 9. Non è una proprietà che si possa verificare guardando un elemento alla volta: l'ordinamento è una proprietà delle **coppie di elementi adiacenti**.

Finora un indice identificava un elemento: i ∈ [0, aLen) ⟷ a[i]. Per confrontare elementi adiacenti si usa per convenzione l'indice del **secondo elemento della coppia**: i ∈ [1, aLen) ⟷ (a[i-1], a[i]). Quindi [0, aLen) è lo spazio degli indici degli elementi e [1, aLen) è lo spazio degli indici delle coppie adiacenti.

![Gli indici degli elementi e quelli delle coppie adiacenti.](figure/prog/indici_coppie.png|11)

Per N ≥ 1 elementi ci sono N-1 coppie: 5 elementi danno 4 coppie, 2 elementi una coppia, 1 elemento nessuna. Con 0 elementi le coppie sono ancora 0, quindi lo spazio [1, aLen) è coerente, e non serve un nuovo caso speciale: si sa già come si comporta un test d'ipotesi su un dominio vuoto (capitolo 37).

## L'ordinamento come proprietà universale
**Definizione.** Un array è **ordinato in senso non decrescente** se tutte le coppie adiacenti sono nell'ordine corretto: ∀i∈[1, aLen) : a[i-1] ≤ a[i].

(In parole povere: ogni elemento è minore o uguale al suo vicino di destra. Gli uguali sono ammessi, per questo si dice «non decrescente» e non «crescente».)

Il predicato sulle coppie è Cond(i) ≡ a[i-1] ≤ a[i]. L'array **non** è ordinato se si trova almeno un controesempio: ∃i∈[1, aLen) : a[i-1] > a[i].

I casi limite discendono dalla definizione: per aLen ≤ 1 non esiste alcuna coppia che possa violare l'ordinamento, e la proprietà ∀ è vera per vacuità. **Un array vuoto e un array con un solo elemento sono ordinati**, senza eccezioni particolari.

## Il codice
```c
bool ordinatoNonDecr(size_t aLen, const int a[]) {
    // All'inizio assumiamo che l'array sia ordinato.
    bool ordinato = true;

    // i identifica la coppia adiacente (a[i - 1], a[i]).
    size_t i = 1;

    // Verifica tutte le coppie, finché non trova un controesempio.
    while (i < aLen && ordinato) {
        if (a[i - 1] > a[i]) {
            // La coppia viola l'ordinamento non decrescente.
            ordinato = false;
        } else {
            // La coppia è ordinata: passa alla successiva.
            i++;
        }
    }

    return ordinato;
}
```

Due esecuzioni. Con a = [2, 4, 4, 7]: 2 ≤ 4, 4 ≤ 4, 4 ≤ 7, nessun controesempio, il risultato è `true`. Con a = [2, 5, 3, 7]: 2 ≤ 5 va bene, 5 ≤ 3 è falso e pone `ordinato = false`, il ciclo termina e il risultato è `false`.

## La forma dell'intervallo conta
L'intervallo i∈[1, aLen) si traduce direttamente in `for (size_t i = 1; i < aLen; i++)` e funziona naturalmente anche per `aLen == 0` e `aLen == 1`.

Bisogna invece evitare una condizione come `i <= aLen - 1`. Essendo `aLen` di tipo `size_t`, cioè senza segno, quando `aLen == 0` l'espressione `aLen - 1` va in **wrap-around** e produce un valore molto grande invece di -1: il ciclo partirebbe e leggerebbe fuori dall'array.

(In parole povere: i numeri senza segno non vanno sotto zero, «ripartono dal fondo» come un contachilometri che torna indietro da 0 a 999999.)

La formulazione matematica con intervalli semiaperti porta quindi a un codice semplice e robusto sui casi limite.

## Dal test al riordinamento
`ordinatoNonDecr` si limita a **rilevare** il controesempio. L'idea nuova è provare a **correggerlo**: quando si trova una coppia nell'ordine sbagliato, si scambiano i due elementi. Il predicato locale `a[i - 1] > a[i]` resta lo stesso, ma cambia cosa si fa dopo. Questa è l'idea dell'algoritmo Bubble Sort, oggetto del prossimo capitolo.
