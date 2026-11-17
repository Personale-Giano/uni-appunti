# Capitolo 41: I Limiti dello Stack e i Puntatori Appesi
## Perché lo stack non basta
Tutte le funzioni in C usano lo stack per gestire variabili e parametri (capitolo 30). Le variabili dichiarate dentro una funzione sono **automatiche**: nascono e muoiono insieme allo stack frame in cui sono dichiarate, cioè esistono solo finché il blocco in cui si trovano non ha finito di eseguire. Nessuno deve occuparsene, ed è il grande vantaggio dello stack; ma è anche il suo limite.

I limiti sono due. Il primo è lo spazio: lo stack ha una dimensione limitata, tipicamente pochi megabyte. Il secondo è la durata: molti problemi richiedono dati che **vivano più a lungo della funzione che li crea**, oppure dati la cui dimensione non è nota a priori. Con il solo stack questi problemi non si risolvono.

## Un problema «impossibile»
Si vuole scrivere una funzione `leggiArray` che legga da input un numero `n`, poi `n` interi, e infine restituisca al chiamante la sequenza letta. Il chiamante non conosce `n`: solo la funzione lo scopre leggendo l'input, quindi solo lei può creare un array della misura giusta. Viene naturale usare un VLA (capitolo 25) e restituirne l'indirizzo, comunicando la lunghezza con un parametro puntatore `out_n` (capitolo 32):

```c
#include <stdlib.h>
#include <stdio.h>

int* leggiArraySbagliato(size_t* out_n) {
    size_t n;
    scanf("%zu", &n);
    int a[n];    // VLA nello stack: vive quanto lo stack frame
    for (size_t i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    *out_n = n;
    return a;    // ERRORE: l'array a sparisce al ritorno
}

int main(void) {
    size_t aLen;
    int* a = leggiArraySbagliato(&aLen);
    for (size_t i = 0; i < aLen; i++)
        printf("a[%zu] = %d\n", i, a[i]);
}
```

Il tipo di ritorno è `int*` perché una funzione non può restituire un array intero: restituisce l'indirizzo del suo primo elemento, ed è quello che fa `return a;`. L'errore che interessa qui è nel `return`, e per capire perché bisogna guardare lo stack.

## Che cosa succede nello stack
Supponiamo che l'utente scriva `3` e poi `10 20 30`.

- In `main` vengono allocate `aLen` e `a`, entrambe non inizializzate.
- Alla chiamata si costruisce il record di attivazione di `leggiArraySbagliato` (capitolo 31): lo spazio per il valore di ritorno, di tipo `int*`, il parametro `out_n` che contiene l'indirizzo di `aLen`, i dati di controllo e la variabile locale `n`.
- Dopo la prima `scanf`, `n` vale 3. La dichiarazione `int a[n];` riserva **nello stesso stack frame** tre celle per `a[0]`, `a[1]`, `a[2]`.
- Il ciclo le riempie con 10, 20 e 30; `*out_n = n;` scrive 3 dentro `aLen`, che sta nel frame di `main`.
- `return a;` copia nel valore di ritorno l'indirizzo di `a[0]`.
- Al ritorno lo stack frame della funzione viene **deallocato**: `n`, `out_n` e le tre celle dell'array non esistono più. In `main` la variabile `a` riceve un indirizzo che punta dentro quell'area.

![leggiArraySbagliato con input 3 e 10 20 30: lo stack subito prima e subito dopo il return.](figure/prog/dangling_stack.png|15)

La lunghezza è arrivata a destinazione, perché `aLen` appartiene a `main` ed è ancora viva. I dati invece no: il puntatore restituito si riferisce a uno stack frame che è stato deallocato, e quell'area di memoria non è più valida.

## Il puntatore appeso
**Definizione.** Un **dangling pointer** (puntatore «appeso») è un puntatore che contiene l'indirizzo di un'area di memoria che non è più valida, per esempio una variabile locale di una funzione che è già ritornata.

(In parole povere: è come avere in tasca la chiave di una camera d'albergo dopo il check-out. La chiave ce l'hai ancora, ma la stanza non è più tua: può essere vuota, o esserci dentro qualcun altro.)

Nell'esempio il ciclo di stampa in `main` legge `a[0]`, `a[1]`, `a[2]` attraverso un puntatore appeso. Il comportamento non è definito: la chiamata a `printf` può costruire il proprio record di attivazione proprio nella zona appena liberata e sovrascrivere i vecchi valori, quindi il programma può stampare 10, 20 e 30 per caso, stampare numeri senza senso oppure interrompersi. Alcuni compilatori possono segnalare la riga del `return` con un avviso, che non va ignorato.

## La regola
Anche i VLA stanno nello stack, e scompaiono alla deallocazione dello stack frame in cui sono dichiarati. Vale quindi una regola senza eccezioni: **non si può mai ritornare un array, o un puntatore a una variabile locale, allocati nello stack frame della funzione che ritorna**.

Il verso opposto resta lecito: una funzione può ricevere e usare l'indirizzo di una variabile del **chiamante**, come `out_n` qui sopra o i parametri di `swap` (capitolo 32), perché il frame del chiamante è ancora vivo per tutta la durata della chiamata.

(In parole povere: si può prestare l'indirizzo di casa propria a chi si va a trovare, ma non si può lasciare come recapito una stanza che verrà demolita appena si esce.)

Per risolvere il problema di `leggiArray` serve un'area di memoria diversa, che non segua la gestione automatica dello stack: è lo heap, oggetto del prossimo capitolo.
