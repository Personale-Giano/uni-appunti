# Capitolo 36: Dal Ragionamento al Codice, la Quantificazione Universale
## Specifica, strategia, ragionamento, codice
La ricerca lineare offre un esempio importante: il codice è breve, ma contiene implicitamente un intero ragionamento logico che non è scritto da nessuna parte. Il codice mostra solo la **dinamica operativa**, cioè come cambiano `i` ed `esiste`, ma non dice perché il procedimento funziona, quali ipotesi lo rendono corretto, né che cosa significhi funzionare correttamente. Si possono distinguere quattro livelli:
- **specifica**, cosa deve fare il programma: determinare se esiste un elemento che soddisfa Cond in a[0, aLen);
- **strategia**, come raggiungere l'obiettivo: inizialmente assumo che non ci sia, poi scansiono gli elementi uno a uno fino a trovarne uno che soddisfa Cond;
- **ragionamento logico**, perché la strategia è corretta: `esiste` diventa vero se e solo se ∃i∈[0, aLen) : Cond(a[i]), quindi la variabile assume il valore di una proposizione equivalente alla specifica;
- **codice eseguibile**, come si realizza operativamente.

Il codice è solo il livello più basso, la concretizzazione meccanica di un pensiero logico e di una specifica.

## Proprietà e invarianti
Ogni iterazione di questo tipo si basa su un **invariante** logico che non compare nel codice ma ne costituisce il fondamento razionale.

**Definizione.** Un **invariante** di ciclo è una proprietà logica che resta vera prima e dopo ogni iterazione del ciclo. Nella ricerca lineare vale: `esiste == true` ⟹ ∃j ∈ [0, i] : Cond(a[j]), per i ∈ [0, aLen). (Più avanti il corso ne svilupperà una forma più stretta.)

(In parole povere: è una frase che puoi ripetere a ogni giro senza mai mentire. Qui dice: «se ho detto che esiste, allora l'ho visto davvero tra gli elementi già guardati».)

La **correttezza parziale** del programma deriva da questo invariante; la **terminazione** e la **correttezza totale** completano il ragionamento.

Il docente la chiama la «scomoda verità» del codice: il codice mostra come fare, non perché funziona. Ipotesi, pre e postcondizioni e invarianti restano impliciti, e senza il ragionamento sottostante il codice è muto riguardo alla propria correttezza. Commenti, `assert` (capitolo 34) e specifiche aiutano a renderlo esplicito. In sintesi: **programmare non è scrivere codice, è tradurre un pensiero in un processo eseguibile**.

## Dalla ricerca di un elemento alla ricerca di una violazione
Un problema simile è stabilire se **tutti** gli elementi di un array soddisfano Cond, cioè ∀i ∈ [0, aLen) : Cond(a[i]). Eliminando il quantificatore si ottiene l'AND aggregativo: ⋀_{i∈[0, aLen)} Cond(a[i]) = Cond(a[0]) ∧ Cond(a[1]) ∧ … ∧ Cond(a[aLen-1]).

Anche questa verifica si deriva come test d'ipotesi, scegliendo le ipotesi in modo da poter falsificare rapidamente H₀ se compare un **controesempio** (Fondamenti, cap. 21):
- **H₀** (ipotesi iniziale): tutti soddisfano Cond, cioè ∀i∈[0, aLen) : Cond(a[i]). In codice: `tutti = true`;
- **H₁** (ipotesi di ricerca): esiste almeno un elemento che non soddisfa Cond, cioè ∃i∈[0, aLen) : ¬Cond(a[i]). In codice: `tutti = false` se si trova un controesempio.

(In parole povere: per dire «tutti» parti fiducioso e cerchi chi ti smentisce: ne basta uno.)

La traduzione diretta dell'AND aggregativo è corretta ma non ottimale, perché scansiona sempre tutto l'array:

```c
bool tutti = true;               // H0: tutti soddisfano Cond
size_t i = 0;
while (i < aLen) {
    tutti = tutti && Cond(a[i]);
    i++;
}
```

Con il cortocircuito ci si ferma al primo controesempio:

```c
bool tutti = true;               // H0: tutti soddisfano Cond
size_t i = 0;
while (i < aLen && tutti) {
    if (!Cond(a[i])) {
        // controesempio trovato: falsifica H0, accetta H1
        tutti = false;           // inoltre: i è il primo indice che NON verifica Cond
    }
    else { i++; }
}
// Stato finale:
// - tutti == true  && i == aLen   : H0, vale Cond(a[i]) per ogni i
// - tutti == false && 0 <= i < aLen : H1, i è il primo controesempio
```

Un esempio concreto, «tutti i valori dell'array sono positivi»:

```c
bool tuttiPositivi = true; // ipotesi iniziale H0: tutti gli elementi sono positivi
size_t i = 0;

// scorre gli elementi finché non trova un valore non positivo
while (i < aLen && tuttiPositivi) {
    if (a[i] <= 0) {
        // basta un solo elemento <= 0 per falsificare H0
        tuttiPositivi = false;
    }
    else { i++; }
}
// - tuttiPositivi == true  : tutti gli elementi sono > 0, e i == aLen
// - tuttiPositivi == false : esiste un elemento <= 0; i è l'indice del primo
```

Le due forme, esistenziale e universale, sono speculari: cambiano il valore iniziale della sentinella e il senso del test, mentre lo schema resta lo stesso.
