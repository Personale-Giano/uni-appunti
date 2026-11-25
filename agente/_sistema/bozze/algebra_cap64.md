# 64. Il Prodotto Scalare: Definizione e Bilinearità
## Un argomento nuovo: misurare
Con la lezione 19 si lascia per il momento il tema di autovalori e autovettori (cap. 59-63) e si comincia un altro modo di guardare le matrici quadrate. Alla lavagna (registrazione 2025) il docente lo presenta con una promessa: dalla definizione «non sembrerà», ma i prodotti scalari sono lo strumento per fare geometria nel senso vero della parola. Serviranno a definire la **lunghezza** di un vettore, la **distanza** fra due punti, l'**angolo** fra due vettori, le aree: tutto ciò che si può misurare deriva dalla nozione di prodotto scalare.

C'è subito un'avvertenza, scritta alla lavagna con un segnale di pericolo: **oggi 𝕂 = ℝ**. Finora conveniva lavorare anche con i numeri complessi, perché in ℂ ogni polinomio ha radici e quindi autovalori se ne trovano sempre (cap. 61). Adesso invece è fondamentale restare nei numeri reali, perché servirà poter dire che un numero è **positivo**: ℝ ha un ordine (ha senso scrivere r > 0), mentre in ℂ non esiste un ordine che rispetti le proprietà abituali. Le dispense aggiungono un secondo motivo: servirà anche estrarre la radice quadrata di un numero positivo, per esempio per definire la lunghezza. In tutti i capitoli sui prodotti scalari gli spazi vettoriali sono quindi **spazi vettoriali reali**.

## La definizione
A voce il docente mette in guardia da una confusione di nomi. Quando si sono definiti gli spazi vettoriali (cap. 17) c'era il **prodotto per scalare**, che prende uno scalare e un vettore e restituisce un vettore. Il **prodotto scalare** è un'altra cosa: prende **due vettori** e restituisce **un numero reale**.

**Definizione.** Sia V uno spazio vettoriale su ℝ. Un **prodotto scalare** su V è una funzione

V × V → ℝ,   (v, w) ↦ ⟨v, w⟩

che soddisfa le tre proprietà seguenti:
1. ⟨v_{1} + v_{2}, w⟩ = ⟨v_{1}, w⟩ + ⟨v_{2}, w⟩ per ogni v_{1}, v_{2}, w ∈ V;
2. ⟨λv, w⟩ = λ⟨v, w⟩ per ogni v, w ∈ V e ogni λ ∈ ℝ;
3. ⟨v, w⟩ = ⟨w, v⟩ per ogni v, w ∈ V (**simmetria**).

(In parole povere: un prodotto scalare è una regola che a ogni coppia di vettori associa un numero, rispettando le somme e i multipli nel primo posto e senza badare all'ordine dei due vettori. Come una «stretta di mano» fra due vettori che produce un punteggio: ⟨v, w⟩ e ⟨w, v⟩ sono la stessa stretta di mano.)

Il docente suggerisce un modo per ricordarle (registrazione 2025): se si pensa a ⟨v, w⟩ come a un «prodotto» fra v e w, la proprietà 1 è una specie di **distributività** rispetto al primo fattore, la 2 una specie di **associatività** con gli scalari, la 3 è la proprietà di **simmetria** (l'analogo della commutatività). Come precisano le dispense, quando si vuole dare un nome al prodotto scalare lo si indica con una lettera, di solito g, e si scrive g(v, w) al posto di ⟨v, w⟩: le due scritture vogliono dire la stessa cosa.

Un esempio da tenere in mente subito, che il capitolo successivo studia per intero, è il prodotto scalare di ℝ² dato da ⟨(x_{1}, x_{2}), (y_{1}, y_{2})⟩ = x_{1}y_{1} + x_{2}y_{2}. Per esempio ⟨(1, 3), (−2, 1)⟩ = 1·(−2) + 3·1 = 1 (è l'esempio delle dispense).

## Linearità nella prima variabile
**Osservazione (registrazione 2025).** Le proprietà 1 e 2 sono esattamente le due condizioni che definiscono un'applicazione lineare (cap. 46). Se si fissa il secondo vettore w e si fa variare solo il primo, la funzione v ↦ ⟨v, w⟩ è un'applicazione lineare da V in ℝ. Il docente lo riassume con una frase scritta tra virgolette: il prodotto scalare è **lineare rispetto alla prima variabile**.

## La simmetria porta la linearità anche nella seconda variabile
Poiché scambiare l'ordine dei due vettori non cambia il risultato, ogni proprietà che vale nel primo posto vale anche nel secondo. Dalle proprietà 1, 2, 3 seguono quindi altre due regole:
- 1'. ⟨v, w_{1} + w_{2}⟩ = ⟨v, w_{1}⟩ + ⟨v, w_{2}⟩ per ogni v, w_{1}, w_{2} ∈ V;
- 2'. ⟨v, λw⟩ = λ⟨v, w⟩ per ogni v, w ∈ V e ogni λ ∈ ℝ.

**Dimostrazione della 2' (alla lavagna, registrazione 2025).** Si usano, nell'ordine, la simmetria, la proprietà 2 e di nuovo la simmetria:
1. ⟨v, λw⟩ = ⟨λw, v⟩, per la proprietà 3 (si scambiano i due vettori);
2. ⟨λw, v⟩ = λ⟨w, v⟩, per la proprietà 2 (ora λ moltiplica il primo vettore e si può portare fuori);
3. λ⟨w, v⟩ = λ⟨v, w⟩, di nuovo per la proprietà 3.

Mettendo insieme, ⟨v, λw⟩ = λ⟨v, w⟩. A lezione uno studente chiede se il trucco stia tutto nella simmetria: sì, è proprio la proprietà 3 che permette di spostare λ dal secondo posto al primo, portarlo fuori e rimettere i vettori in ordine.

La 1' si dimostra allo stesso modo (alla lavagna non è scritta): ⟨v, w_{1} + w_{2}⟩ = ⟨w_{1} + w_{2}, v⟩ = ⟨w_{1}, v⟩ + ⟨w_{2}, v⟩ = ⟨v, w_{1}⟩ + ⟨v, w_{2}⟩, usando la 3, poi la 1, poi ancora la 3.

**Definizione.** Una funzione V × V → ℝ che è lineare sia rispetto alla prima variabile (proprietà 1 e 2) sia rispetto alla seconda (proprietà 1' e 2') si dice **bilineare**. Quindi **i prodotti scalari sono bilineari**; e un prodotto scalare è, in breve, una funzione **bilineare e simmetrica** da V × V in ℝ.

(In parole povere: «bilineare» vuol dire lineare due volte, una per ciascun posto. Se si tiene fermo uno dei due vettori, il prodotto scalare si comporta come un'applicazione lineare dell'altro: somme e multipli «escono fuori» qualunque sia il posto in cui stanno.)

Un modo pratico per usare la bilinearità è «sviluppare» come si fa con i prodotti fra numeri. Per esempio, per due vettori qualsiasi u, v,

⟨u + 2v, 3u − v⟩ = 3⟨u, u⟩ − ⟨u, v⟩ + 6⟨v, u⟩ − 2⟨v, v⟩ = 3⟨u, u⟩ + 5⟨u, v⟩ − 2⟨v, v⟩,

dove nell'ultimo passaggio si è usata la simmetria ⟨v, u⟩ = ⟨u, v⟩ (esempio aggiunto per chiarezza).

**Osservazione (dalle dispense).** Il prodotto scalare di un vettore qualsiasi con il vettore nullo è zero: ⟨v, 0⟩ = 0 per ogni v ∈ V. Infatti 0 = 0 + 0, quindi per la 1'

⟨v, 0⟩ = ⟨v, 0 + 0⟩ = ⟨v, 0⟩ + ⟨v, 0⟩,

e sottraendo ⟨v, 0⟩ da entrambi i membri resta 0 = ⟨v, 0⟩. Per simmetria anche ⟨0, v⟩ = 0. È lo stesso ragionamento con cui si dimostra che un'applicazione lineare manda 0 in 0.

## Prodotti scalari degeneri e definiti positivi
Non tutti i prodotti scalari sono adatti a misurare. Il docente introduce subito due definizioni che li distinguono (registrazione 2025); qui il concetto di «maggiore di zero» entra davvero nella teoria, ed è il motivo per cui serve 𝕂 = ℝ.

**Definizione.** Un prodotto scalare ⟨ , ⟩ su V si dice:
- **degenere** se esiste un vettore v ∈ V, **v ≠ 0**, tale che ⟨v, w⟩ = 0 per ogni w ∈ V;
- **definito positivo** se ⟨v, v⟩ > 0 per ogni v ∈ V con v ≠ 0.

(In parole povere: è degenere se c'è un vettore non nullo «invisibile», che fa zero con chiunque, compreso se stesso. È definito positivo se ogni vettore non nullo, moltiplicato per se stesso, dà un numero strettamente positivo: è la condizione che servirà per dire che ogni vettore non nullo ha una lunghezza positiva.)

Attenzione a un dettaglio della lavagna (registrazione 2025): la definizione di degenere è scritta «se ∃ v ∈ V t.c. ⟨v, w⟩ = 0 ∀ w ∈ V», senza la condizione v ≠ 0, che c'è invece nelle dispense (Def. 19.2). La condizione è indispensabile: per l'osservazione precedente il vettore nullo soddisfa sempre ⟨0, w⟩ = 0, quindi senza «v ≠ 0» ogni prodotto scalare sarebbe degenere e la definizione non direbbe nulla.

Come sottolineato a lezione, i prodotti scalari che davvero interessano per fare geometria sono quelli **definiti positivi**. Le due proprietà sono legate.

**Proposizione 19.3.** Un prodotto scalare definito positivo non è degenere.

**Dimostrazione (dalla spiegazione delle dispense).** Per assurdo, sia ⟨ , ⟩ definito positivo e degenere. Essendo degenere, esiste v ≠ 0 tale che ⟨v, w⟩ = 0 per ogni w ∈ V. Scegliendo in particolare w = v si ottiene ⟨v, v⟩ = 0, mentre la definita positività, poiché v ≠ 0, richiede ⟨v, v⟩ > 0. Contraddizione.

Il viceversa invece è falso: esistono prodotti scalari non degeneri che non sono definiti positivi. Un esempio sui polinomi è nel capitolo successivo.

**Esempio (aggiunto per chiarezza).** Su ℝ² la funzione g((x_{1}, x_{2}), (y_{1}, y_{2})) = x_{1}y_{1} è un prodotto scalare: è simmetrica e, fissato uno dei due vettori, è lineare nell'altro. È degenere: il vettore e_{2} = (0, 1) è non nullo e g(e_{2}, w) = 0·y_{1} = 0 per ogni w = (y_{1}, y_{2}). Quindi, per la Proposizione 19.3, non è definito positivo; lo si vede anche direttamente, perché g(e_{2}, e_{2}) = 0.

Il capitolo successivo presenta i due esempi della lavagna, il prodotto scalare euclideo di ℝⁿ e un prodotto scalare sullo spazio dei polinomi di grado al più 2, e dimostra che il primo è definito positivo.
