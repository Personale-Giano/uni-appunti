# Capitolo 30: Lo Stack Frame e il Modello della Chiamata di Funzione
## Dal modello di Von Neumann al problema delle funzioni
Il modello di Von Neumann (capitolo 4) descrive una macchina con una memoria unica per dati e istruzioni, un'unità di controllo sequenziale e pochi registri di base, come il PC e gli accumulatori. Da solo però non dice come si gestiscono le funzioni. Nei primi compilatori le variabili venivano allocate a **indirizzi fissi**, e questo rendeva le funzioni **non rientranti**: non potevano essere eseguite più volte in parallelo o in modo ricorsivo, perché due esecuzioni avrebbero usato le stesse celle. Per i linguaggi di alto livello questo limite si rivelò presto troppo stretto.

L'approccio a indirizzi fissi fu abbandonato già alla fine degli anni '50, e la soluzione è lo **stack**:
- Bauer e Samelson introducono l'idea di un ~control stack~ per gestire le chiamate annidate e allocare le variabili a indirizzi relativi;
- nel 1958 Edsger Dijkstra formalizza l'uso dello stack come meccanismo generale per la ricorsione;
- nel 1961 il Burroughs B5000 realizza per la prima volta in hardware questo modello, con uno stack dedicato alle funzioni;
- le architetture moderne forniscono un registro di stack pointer (SP) e meccanismi che rendono efficienti le chiamate; un ulteriore registro può fare da frame pointer (FP).

Il corso descrive le chiamate con un **modello di Von Neumann esteso**, basato su stack frame, SP e FP. È una convenzione del corso: le architetture e le convenzioni di chiamata reali possono usare registri, omettere FP o organizzare il frame in modo diverso, ma la logica resta la stessa.

## Il modello dello stack
Le regole di riferimento riprendono quelle del capitolo 7:
- lo stack cresce verso **indirizzi di memoria decrescenti**;
- **SP** indica il limite corrente dello stack; si aggiorna quando si riserva o si libera spazio, cioè, nel modello, quando le variabili locali entrano ed escono dalla visibilità;
- **FP** indica l'inizio dello stack frame della funzione attiva e **rimane stabile** per tutta la chiamata;
- nello stack si rappresentano le variabili locali, i dati di controllo e, quando serve, i parametri e il valore di ritorno.

**Definizione.** Lo **stack frame** è la porzione contigua di memoria nello stack dedicata a una funzione attiva: ogni chiamata di funzione riserva un nuovo frame, e al termine della funzione il frame viene rilasciato e la memoria torna disponibile.

(In parole povere: ogni chiamata si prende un pezzetto di stack tutto suo; quando la funzione finisce, quel pezzetto viene restituito.)

Lo stack quindi cresce e si riduce seguendo le chiamate annidate, perché ogni nuova chiamata impila un nuovo frame sopra ai precedenti. In ogni momento c'è **una sola funzione attiva**, quella il cui frame è in cima alla pila, e una sequenza di **funzioni sospese**, i cui frame stanno sotto e aspettano di riprendere.

## Un esempio: main, sumSquares e square
Il programma seguente permette di seguire l'evoluzione dello stack: `main()` chiama `sumSquares(2, 3)`, e `sumSquares()` chiama due volte `square()`, prima con 2 e poi con 3.

```c
#include <stdio.h>
int square(int x) {
    return x * x;
}
int sumSquares(int a, int b) {
    return square(a) + square(b);
}
int main(void) {
    int res = sumSquares(2, 3);
    printf("Risultato: %d\n", res);
    return 0;
}
```

All'inizio è attivo `main`. Ogni variabile locale dichiarata sposta SP verso indirizzi più bassi per riservarle spazio, e la regione compresa tra SP ed FP è l'area delle variabili locali della funzione attiva. Quando una variabile esce dalla visibilità il suo spazio viene rilasciato arretrando SP; al ritorno dalla funzione viene rilasciato tutto il frame.

![L'evoluzione dello stack: main chiama sumSquares, che chiama square due volte. Gli stati 3 e 5 hanno tre frame, uno attivo e due sospesi.](figure/prog/stack_evoluzione.png|16)

Si noti che le due chiamate a `square` occupano la stessa zona di stack, ma una dopo l'altra: quando parte la seconda, il frame della prima è già stato rilasciato.

## Accedere ai dati della chiamata tramite FP
Poiché FP rimane stabile mentre la funzione è attiva, i dati della chiamata si raggiungono con **offset costanti** da FP, dove un offset (scostamento) è la distanza in byte rispetto a un indirizzo di riferimento:
- i **parametri** e il **valore di ritorno** si trovano a offset **positivi** da FP;
- le **variabili locali** sono allocate sotto FP, a offset **negativi**;
- i **dati di controllo** (il FP precedente e l'indirizzo di ritorno) servono a gestire il ritorno dalla chiamata.

I valori numerici degli offset dipendono dalla dimensione dei dati, e nel corso servono solo come esempio: quello che conta è il segno. SP invece può cambiare durante l'esecuzione, per questo non è un buon punto di riferimento. Quali di questi dati appartengano davvero allo stack frame si precisa nel capitolo 31, con il record di attivazione.

(In parole povere: FP è un punto fermo nel frame. Da lì «verso l'alto» trovi quello che ti ha passato il chiamante, «verso il basso» le tue variabili.)

## Un esempio con parametri, ritorno e variabili
```c
#include <stdio.h>

int sommaProdotto(int a, int b, int c) {
    int somma = a + b + c;
    int prodotto = a * b * c;
    int risultato = somma + prodotto;
    return risultato;
}

int main(void) {
    int x = 2, y = 3, z = 4;
    int r = sommaProdotto(x, y, z);
    printf("Risultato: %d\n", r);
}
```

Subito dopo l'esecuzione di `int risultato = somma + prodotto;`, partendo dagli indirizzi più alti lo stack contiene: `x = 2`, `y = 3`, `z = 4` di `main`; la cella per il valore di ritorno, indicata come `r` perché riceverà il risultato assegnato a `r`; poi i parametri `a = 2`, `b = 3`, `c = 4`; poi i dati di controllo. Qui si trova FP, e sotto ci sono le locali di `sommaProdotto`: `somma = 9`, `prodotto = 24`, `risultato = 33`. Infine SP. Si vede bene che `a`, `b` e `c` sono celle diverse da `x`, `y` e `z`: contengono copie dei loro valori.

Il prossimo capitolo segue passo per passo come si costruisce e come si smonta questa struttura.
