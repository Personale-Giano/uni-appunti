# Capitolo 37: I Casi Limite delle Quantificazioni e il Dominio Vuoto
## Una funzione deve trattare tutti gli input
Una funzione deve fornire un risultato per **tutti** gli input che rispettano la sua specifica, compresi i casi limite. Per ∀i ∈ [0, aLen) : Cond(a[i]), con aLen == N si ha Cond(a[0]) ∧ … ∧ Cond(a[N−1]); con aLen == 2 si ha Cond(a[0]) ∧ Cond(a[1]); con aLen == 1 solo Cond(a[0]). E con aLen == 0? Che cosa significa «tutti gli elementi soddisfano Cond» quando non ci sono elementi?

## Il quantificatore universale sul dominio vuoto
Per falsificare ∀i ∈ [0, aLen) : Cond(a[i]) bisogna trovare almeno un controesempio nel dominio [0, aLen). Se aLen == 0 il dominio [0, 0) è vuoto, non viene esaminato alcun elemento e non può esistere un controesempio.

**Definizione.** Un enunciato universale su un dominio vuoto è **vero per vacuità** (~vacuously true~), perché non esiste alcun possibile controesempio alla proprietà.

(In parole povere: «tutti i miei fratelli marziani sono alti» è vero se di fratelli marziani non ne hai: nessuno può smentirlo.)

Lo si può leggere in due modi equivalenti: una proprietà universale è falsa solo se esiste almeno un controesempio, e nel dominio vuoto non può essercene nessuno; oppure, dire che tutti gli elementi soddisfano una condizione resta vero perché non esiste alcun elemento che non la soddisfi. È lo stesso «vero per difetto» già incontrato con l'implicazione in Fondamenti (cap. 16).

Riprendendo il ciclo `tuttiPositivi` del capitolo 36, con `aLen == 0` non si esegue alcuna iterazione: `tuttiPositivi` parte vero e resta vero, che è la risposta corretta. Il caso vuoto **non richiede una regola speciale**.

## Il quantificatore esistenziale sul dominio vuoto
Per ∃i ∈ [0, aLen) : Cond(a[i]) serve trovare almeno un **testimone** che soddisfi Cond. Se aLen == 0 il dominio è vuoto, non viene esaminato alcun elemento e non può esistere un testimone.

**Definizione.** Un enunciato esistenziale su un dominio vuoto è **falso per assenza di testimoni**, perché non esiste alcun elemento che possa soddisfare la proprietà.

(In parole povere: «esiste un mio fratello marziano alto» è falso se di fratelli marziani non ne hai: non c'è nessuno da mostrare.)

Anche qui con `aLen == 0` il ciclo `esistePari` non esegue iterazioni: la sentinella parte falsa e resta falsa, rispondendo correttamente.

## La regola generale
Se il valore iniziale della variabile sentinella coincide con il risultato corretto sul dominio vuoto, per `aLen == 0` il ciclo non esegue alcuna iterazione e la funzione calcola da sola la risposta giusta:
- **∀ / AND**: sul dominio vuoto è `true` (nessun controesempio), valore iniziale `true`;
- **∃ / OR**: sul dominio vuoto è `false` (nessun testimone), valore iniziale `false`.

Quando si definisce una funzione bisogna sempre pensare ai casi limite, e con array e intervalli il dominio vuoto è un caso importante: una buona formulazione dell'algoritmo lo tratta naturalmente, senza eccezioni ad hoc.

## Esercizi: tuttiPositivi ed esistePari
**tuttiPositivi** prende un array di interi `a`, la sua lunghezza `aLen` (se `aLen > 0` allora `a != NULL`) e un puntatore `size_t* firstBad` non `NULL`. Restituisce `true` se e solo se ∀i∈[0, aLen) a[i] > 0, e scrive in `*firstBad` l'indice del primo elemento che viola la proprietà, oppure `aLen` se non ci sono violazioni.

**esistePari** ha la stessa forma, con `size_t* firstEven`. Restituisce `true` se e solo se ∃i∈[0, aLen) con a[i] pari, e scrive in `*firstEven` l'indice del primo pari trovato, oppure `aLen` se non ce ne sono.

Sono fornite delle prove con `assert`, che coprono il caso vuoto, l'assenza di violazioni e la violazione in testa, in mezzo e in coda:

```c
size_t idx;
// VUOTO: ALL vero, indice sentinella
const int* v0 = NULL;
assert(tuttiPositivi(v0, 0, &idx) == true && idx == 0);
// TUTTI > 0
const int v1[] = {1, 2, 3};
assert(tuttiPositivi(v1, 3, &idx) == true && idx == 3);
// PRIMA VIOLAZIONE IN TESTA (<= 0)
const int v2[] = {0, 2, 3};
assert(tuttiPositivi(v2, 3, &idx) == false && idx == 0);
// VIOLAZIONE IN MEZZO
const int v3[] = {5, 4, -1, 7};
assert(tuttiPositivi(v3, 4, &idx) == false && idx == 2);
// VIOLAZIONE IN CODA
const int v4[] = {5, 4, 3, -9};
assert(tuttiPositivi(v4, 4, &idx) == false && idx == 3);
```

Per `esistePari` le prove sono analoghe: `esistePari(NULL, 0, &idx)` dà `false` con `idx == 0`; `{1, 3, 5, 7}` dà `false` con `idx == 4`; `{2, 3, 5}` dà `true` con `idx == 0`; `{1, 4, 5, 7}` dà `true` con `idx == 1`; `{1, 3, -6}` dà `true` con `idx == 2`, perché anche i negativi possono essere pari.

Una possibile soluzione (ricavata dallo schema del capitolo 36, non presente nelle slide). Si noti che `i` si comunica al chiamante tramite il puntatore, come visto nel capitolo 32:

```c
bool tuttiPositivi(const int a[], size_t aLen, size_t *firstBad) {
    bool tutti = true;
    size_t i = 0;
    while (i < aLen && tutti) {
        if (a[i] <= 0) {
            tutti = false;
        }
        else {
            i++;
        }
    }
    *firstBad = i;   // primo elemento che viola, oppure aLen
    return tutti;
}
```

Per `esistePari` basta partire da `false`, usare il test `a[i] % 2 == 0` e continuare con `i < aLen && !esiste`.
