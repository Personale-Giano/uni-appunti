# Capitolo 35: La Ricerca Lineare e la Quantificazione Esistenziale
## Algoritmi su array
Cercare elementi, filtrare secondo un criterio e ordinare le informazioni sono problemi tipici sui dati sequenziali. I loro algoritmi sono **fondazionali**: semplici da implementare, usano i concetti visti finora (cicli, condizioni, variabili sentinella) e sono alla base di algoritmi più complessi.

## L'idea della ricerca lineare
Immaginiamo uno sgabuzzino pieno di scatoloni numerati da 0 a aLen-1, e di voler sapere se in uno di essi abbiamo lasciato un disco in vinile. La strategia è aprire gli scatoloni uno per uno, in ordine, finché troviamo il disco oppure li abbiamo controllati tutti e il disco non c'è.

**Definizione.** Dato un array `a` di lunghezza `aLen` e un valore `key`, la **ricerca lineare** è l'algoritmo che al termine lascia nella variabile `i` un indice valido, cioè i ∈ [0, aLen), tale che `a[i] == key`, oppure il valore sentinella `i == aLen` se e solo se `key` non è presente nell'array.

(In parole povere: guardi gli elementi uno alla volta; alla fine `i` è la posizione di quello cercato, oppure un numero «fuori dall'array» che vuol dire «non c'è».)

Per esempio, con `int a[] = {6, 12, 4, 9, -1};` (quindi `aLen == 5`), la ricerca di `key == 4` termina con `i == 2`, mentre la ricerca di `key == 20` termina con `i == 5`, il valore sentinella.

Servono due elementi: una **variabile di controllo** `i`, che scorre l'array e alla fine indica la posizione trovata, e una **variabile sentinella** booleana `trovato`, che diventa vera non appena `key` viene individuato e regola il ciclo. `trovato` non può limitarsi a registrare il risultato, ma va usata nella condizione del ciclo: altrimenti, dopo la scoperta, `i` non verrebbe più incrementato e il ciclo non si fermerebbe mai.

```c
bool trovato = false; // ipotesi iniziale: l'elemento cercato non esiste
size_t i = 0;         // indice della scansione

while (i < aLen && !trovato) {
    // scorre gli elementi dell'array per trovare key
    if (a[i] == key) {
        trovato = true;
        // trovato, l'ipotesi iniziale è sbagliata, mi fermo
    }
    else {
        i++;
    }
}
// al termine:
//   - se trovato == true, i è l'indice della prima occorrenza
//   - se trovato == false, i == aLen: scansione completata senza occorrenze
```

La condizione `i < aLen && !trovato` si legge: finché `i` è un indice valido e non ho ancora trovato l'elemento, continua a iterare. Si noti che `i++` sta nell'`else`: quando l'elemento viene trovato `i` non si muove, e resta sulla posizione giusta.

## La ricerca come quantificazione esistenziale
La formulazione logica della ricerca è ∃i ∈ [0, aLen) : a[i] = key, cioè «esiste almeno un indice i tale che a[i] è uguale a key» (Fondamenti, cap. 22). La ricerca lineare è quindi la **realizzazione algoritmica della quantificazione esistenziale** su un array: ogni volta che cerchiamo un elemento rispondiamo alla domanda «esiste un indice che soddisfa la proprietà?».

## Derivare l'algoritmo come test d'ipotesi
L'algoritmo si può ricavare dalla logica. Dato un array e una condizione Cond(⋅) sugli elementi, si formulano due ipotesi che si escludono a vicenda:
- **ipotesi nulla H₀** (o iniziale): nessun elemento soddisfa Cond, cioè H₀ : ∀i∈[0, aLen) : ¬Cond(a[i]). In codice: `esiste = false`;
- **ipotesi alternativa H₁** (o di ricerca): almeno un elemento soddisfa Cond, cioè H₁ : ∃i∈[0, aLen) : Cond(a[i]). In codice: una scansione che pone `esiste = true` non appena trova un tale elemento.

(In parole povere: parti dall'idea «non c'è» e cerchi un esempio che la smentisca. Appena lo trovi hai finito; se li guardi tutti e non lo trovi, avevi ragione.)

Il linguaggio di programmazione non ha un'operazione di quantificazione, quindi la si riscrive con gli **operatori aggregativi**: l'AND e l'OR estesi a tutti i valori, ⋀ e ⋁. Provare ∃i∈[0, aLen) : Cond(a[i]) equivale a verificare ⋁_{i∈[0, aLen)} Cond(a[i]) = Cond(a[0]) ∨ Cond(a[1]) ∨ … ∨ Cond(a[aLen-1]). Questa formula si traduce direttamente in codice:

```c
bool esiste = false;    // ipotesi iniziale: H0 (nessun elemento soddisfa Cond)
size_t i = 0;

while (i < aLen) {      // continua finché restano elementi
    esiste = esiste || Cond(a[i]);
    i++;
}
```

Qui e nel seguito `Cond(a[i])` è uno **pseudocodice** per una condizione qualunque sull'elemento. Questa forma è corretta ma non ottimale: esegue tutta la scansione anche se potrebbe fermarsi non appena `esiste` diventa vero.

Non serve infatti l'OR di tutti i valori: la valutazione si può **cortocircuitare**, fermandosi al primo indice che soddisfa Cond. In formule, ⋁_{i∈[0, aLen)} Cond(a[i]) = ⋁_{i∈[0, iMin]} Cond(a[i]), dove iMin = min{ i∈[0, aLen) | Cond(a[i]) } è il primo indice che soddisfa la condizione, se esiste. Riscrivendo la catena di OR con un semplice assegnamento si ottiene la forma finale:

```c
bool esiste = false;    // ipotesi iniziale: H0 (nessun elemento soddisfa Cond)
size_t i = 0;

// continua finché H0 non è falsificata, o l'array è finito
while (i < aLen && !esiste) {
    if (Cond(a[i])) {
        esiste = true;  // trovato: rigetto H0, accetto H1
                        // inoltre i è il minimo indice tale che Cond(a[i])
    }
    else {
        i++;
    }
}
// Stato finale:
// - esiste == true  : H0 falsificata, H1 vera; a[i] è il primo che soddisfa Cond
// - esiste == false : nessun elemento trovato in [0, aLen); accetto H0
```

Un esempio concreto, «esiste un elemento pari nell'array?»:

```c
bool esistePari = false;    // ipotesi iniziale: H0 (nessun elemento pari)
size_t i = 0;

while (i < aLen && !esistePari) {
    if (a[i] % 2 == 0) {
        esistePari = true;  // a[i] è pari
    }
    else {
        i++;
    }
}
// - esistePari == true  : a[i] è il primo elemento pari
// - esistePari == false : non ci sono elementi pari nell'array
```
