# 39. Gli Invarianti di Ciclo: il Ciclo del Fattoriale
## Perché un informatico ha bisogno dell'induzione
Un programma che gira bene su qualche prova non è ancora un programma corretto. Nella registrazione 2025 il docente insiste su questo punto: quando si affidano a una macchina vite e beni, la tolleranza per l'errore è zero, e anche mille programmi banali devono essere tutti senza errori, non 999 su mille. Il modo di controllare un ciclo, dice, procede per gradi: prima si guarda se il codice è plausibile, poi lo si prova su qualche caso, e se sopravvive a questi controlli ci si ragiona sopra per essere sicuri che funzioni in **tutti** gli infiniti casi possibili. L'ultimo controllo è l'unico che dà una garanzia, e si fa con un'induzione. È l'esempio 2.4.8 del libro, il centro della lezione 19.

## L'invariante di un ciclo
**Definizione.** Un **invariante di ciclo** è un enunciato sulle variabili di un programma che è vero subito prima che il ciclo cominci e che, se è vero prima di un'esecuzione del corpo del ciclo, resta vero subito dopo.

(In parole povere: è una «fotografia» della situazione che rimane valida in ogni istante del ciclo, all'inizio, a ogni giro e alla fine, anche se le variabili cambiano. È come dire, mentre si mettono in fila delle monete, «quelle già sistemate sono in ordine»: è vero all'inizio (nessuna moneta) e resta vero a ogni moneta aggiunta.)

Per un ciclo `while (condizione) { corpo }` l'invariante deve valere subito prima della prima valutazione della condizione e ogni volta che il corpo è stato eseguito. Il docente parla solo di cicli `while` per semplicità, ma l'idea vale per ogni ciclo (`for`, `do-while`, …).

**Perché è un'induzione.** Si dimostra per induzione sul **numero di esecuzioni del corpo**:

- **passo base**: l'invariante vale prima di eseguire il corpo anche una sola volta, cioè con i valori iniziali delle variabili;
- **passo induttivo**: se l'invariante vale e la condizione è vera (quindi il corpo viene eseguito un'altra volta), allora l'invariante vale anche dopo quell'esecuzione.

Il libro osserva una differenza con il cap. 37: un ciclo che termina fa un numero finito di giri, quindi qui si dimostra una successione **finita** di enunciati; i passi della prova però sono gli stessi.

**A che cosa serve.** Quando il ciclo si ferma valgono due cose insieme: l'invariante, che è vero sempre, e la **negazione della condizione** del `while`, perché è proprio quella a fermarlo. Un buon invariante è uno da cui, insieme alla condizione falsa, si deduce che il ciclo ha fatto il suo compito. Gli invarianti veri sono tantissimi e quasi tutti inutili (registrazione 2025): serve quello che descrive l'idea del ciclo.

## Esempio 2.4.8: il ciclo del fattoriale
Si vuole dimostrare che, quando il ciclo seguente termina, la variabile `fact` contiene n!.

```
i = 1
fact = 1
while (i < n) {
   i = i + 1
   fact = fact * i
}
```

L'affermazione «alla fine `fact` vale n!» è quella che il docente chiama **postcondizione**: una condizione che deve valere dopo l'esecuzione del ciclo (registrazione 2025).

**Plausibilità prima di tutto.** Uno studente chiede perché il ciclo si fermi a i < n e non a i ≤ n. Il docente fa notare l'ordine delle istruzioni: i viene incrementato **prima** della moltiplicazione, quindi quando i vale n − 1 il corpo porta i a n e moltiplica per n. Le moltiplicazioni vengono fatte per 2, 3, …, n, ed è giusto fermarsi lì. Con l'incremento messo dopo il prodotto, la condizione giusta sarebbe invece i ≤ n (si vede sotto).

**L'invariante.** Il libro usa fact = i!. Il docente lo scrive con una parte in più (registrazione 2025):

**i ≤ n e fact = i!**

La seconda parte dice che in `fact` c'è il prodotto degli interi da 1 a i; la prima che l'indice non scappa oltre n. Si suppone n ≥ 1.

## La prova dell'invariante
**Passo base (zero esecuzioni del corpo).** Prima del ciclo i = 1 e fact = 1. Allora fact = 1 = 1! = i!, e i = 1 ≤ n perché n ≥ 1.

**Passo induttivo.** Si suppone che dopo un certo numero di esecuzioni l'invariante valga, con i = i₀ e fact = i₀!, e che il corpo venga eseguito un'altra volta.

- **La parte i ≤ n.** Qui il docente segnala la prima difficoltà: se i fosse proprio n, dopo l'incremento varrebbe n + 1 e la parte i ≤ n sarebbe falsa. Ma se il corpo viene eseguito, la condizione i₀ < n è vera, quindi i₀ ≤ n − 1 (sono interi) e dopo l'incremento i = i₀ + 1 ≤ n. Il test del `while` dà un'informazione in più rispetto all'invariante, ed è proprio quella che serve.
- **La parte fact = i!.** Il corpo fa prima i = i₀ + 1 e poi fact = fact · i. Il punto delicato è che nella moltiplicazione `fact` ha ancora il valore **vecchio**, i₀!, mentre i ha già il valore **nuovo**, i₀ + 1. Quindi il nuovo valore di `fact` è i₀! · (i₀ + 1) = (i₀ + 1)!, per definizione di fattoriale. È proprio i! con il nuovo valore di i.

L'invariante quindi si mantiene. Il docente raccomanda di non fare «copia e incolla» del passo base nel passo induttivo: i valori sono diversi ed è facile sbagliare (registrazione 2025).

## Dalla prova alla correttezza
Quando il ciclo termina, la condizione i < n è falsa, quindi vale i ≥ n. Insieme alla parte i ≤ n dell'invariante si ottiene i = n, e allora l'altra parte, fact = i!, diventa fact = n!. Il ciclo ha calcolato il fattoriale.

Si vede perché il docente aggiunge i ≤ n all'invariante: con il solo fact = i!, come nel libro, all'uscita si saprebbe soltanto che i ≥ n, e non che `fact` contiene proprio n!. Il libro scrive «il ciclo termina quando i = n», ed è esattamente il fatto che la parte i ≤ n giustifica.

Per esempio, con n = 4 il corpo si esegue tre volte (in generale n − 1 volte) e le variabili valgono:

- prima del ciclo: i = 1, fact = 1 = 1!;
- dopo 1 esecuzione: i = 2, fact = 2 = 2!;
- dopo 2 esecuzioni: i = 3, fact = 6 = 3!;
- dopo 3 esecuzioni: i = 4, fact = 24 = 4!.

A ogni passo fact = i! e i ≤ 4; alla fine il test 4 < 4 è falso e fact = 24 = 4!. Questo elenco è una prova su un caso, non una dimostrazione: è il genere di controllo di plausibilità che viene prima del ragionamento.

**L'ipotesi n ≥ 1 non è inutile (registrazione 2025).** Senza di essa il passo base cade, perché i = 1 ≤ n diventa falso. Il docente lo fa vedere: con n = 0 il ciclo non parte e restituisce fact = 1, che per caso è proprio 0!; con n = −1 o −2 il ciclo termina lo stesso e restituisce 1, ma il fattoriale dei negativi non esiste, quindi il risultato non ha senso.

**La terminazione.** Il libro e il docente si concentrano su che cosa vale quando il ciclo termina. Che termini davvero, nel caso n ≥ 1, si vede a parte: i parte da 1 e cresce di 1 a ogni giro, quindi dopo n − 1 giri vale n e il test diventa falso.

## Come la scrive il quiz del corso
Tra i quiz della lezione 19 su Moodle c'è questa prova da completare: si procede «per induzione sul numero di esecuzioni del corpo del while»; nel **caso base** non si è mai eseguito il corpo, i valori sono i = 1 e fact = 1, si sceglie i₀ = 1 e, poiché 1! = 1, vale i = i₀ e fact = i₀!; nel **caso induttivo** si suppone i = i₀ e fact = i₀!, si eseguono nell'ordine i = i + 1 e fact = fact · i, si ottiene i = i₀ + 1 e fact = i₀! · (i₀ + 1), e per la definizione (i₀ + 1)! = i₀! · (i₀ + 1) si conclude i = i₀ + 1 e fact = (i₀ + 1)!. Il quiz aggiunge un'ipotesi che a lezione non si nomina: che il prodotto **non produca overflow**, cioè che il risultato stia nella variabile (con gli interi della macchina, 13! supera già 2³¹ − 1).

## Una variante dello stesso ciclo
Con l'incremento dopo il prodotto il ciclo diventa:

```
i = 1
fact = 1
while (i <= n) {
   fact = fact * i
   i = i + 1
}
```

Qui `fact` contiene il prodotto degli interi **prima** di i, e l'invariante giusto è fact = (i − 1)! insieme a i ≤ n + 1, con n ≥ 0. All'inizio fact = 1 = 0!; a ogni giro fact diventa (i − 1)! · i = i! e poi i aumenta di 1; all'uscita i > n e i ≤ n + 1 danno i = n + 1, quindi fact = n!. Questa versione funziona anche per n = 0 (il ciclo non parte e fact = 1 = 0!). L'esempio mostra che l'invariante dipende dai dettagli del codice: spostare una riga cambia la formula.

## Trovare l'invariante e provarlo
Il docente distingue due difficoltà (registrazione 2025). **Trovare** l'invariante è difficile, anche per una macchina: bisogna catturare in una formula l'idea che si ha in mente («moltiplico gli interi da 1 in su e porto i avanti fino a n, senza superarlo»). **Provarlo**, una volta trovato, di solito è più facile, perché l'invariante nasce proprio per descrivere che cosa fa il ciclo. In un gruppo di lavoro, aggiunge, ci deve sempre essere qualcuno che fa questo controllo ragionato: non basta essersi convinti che il codice funziona.

Il prossimo capitolo applica lo stesso schema al ciclo che calcola una potenza.
