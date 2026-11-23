# 47. Le Sequenze: Indici, Formule e Monotonia
## Dalle tariffe del taxi alla definizione
Il §3.2 del libro apre con le tariffe di un taxi, un esempio che secondo il docente vale la pena di leggere (registrazione 2025). Ne costruiamo uno con numeri nostri. Un taxi chiede 3 euro per il primo chilometro e 1,20 euro per ogni chilometro successivo. Il costo di una corsa di n chilometri è allora Cₙ = 3 + 1,2(n − 1): il primo chilometro costa 3 euro, e gli altri n − 1 costano 1,20 euro l'uno. I primi valori sono C₁ = 3, C₂ = 4,20, C₃ = 5,40, e per dieci chilometri C₁₀ = 3 + 1,2 · 9 = 13,80 euro.

Il docente osserva che, come funzione dai chilometri al costo, questa è iniettiva, perché a percorsi diversi corrispondono costi diversi (i costi crescono), ma non è suriettiva sui numeri reali: non esiste una corsa che costi π euro. È l'esempio con cui il libro introduce le sequenze.

**Definizione.** Una **sequenza** (o successione) s è una funzione il cui dominio D è un sottoinsieme degli interi. Invece di s(n) si scrive di solito sₙ, e n si chiama **indice**. Se D è finito la sequenza è **finita**, altrimenti è **infinita**.

(In parole povere: una sequenza è un elenco numerato. L'indice dice la posizione, sₙ è l'elemento che sta in quella posizione: come i numeri di una fila di armadietti, dove dentro l'armadietto n c'è sₙ.)

La sequenza del taxi, se si considerano solo le corse da 1 a 10 chilometri, ha dominio {1, 2, …, 10} ed è finita. Quasi sempre, osserva il docente, le sequenze hanno per dominio tutti gli interi positivi o tutti i naturali (gli interi positivi più lo zero), e sono quindi potenzialmente infinite. Gli elementi invece non devono essere per forza numeri: possono essere lettere di un alfabeto, e allora la sequenza è una stringa, l'argomento del prossimo capitolo (registrazione 2025).

**Tre modi di rappresentare una sequenza.** Dal punto di vista dell'informatica, insiste il docente, la domanda è come memorizzare e calcolare una sequenza (registrazione 2025):
- con una **tabella** che elenca indici e valori, come nel libro per le tariffe: si può fare solo per sequenze finite, e conviene solo se non sono troppo lunghe, perché la tabella occupa memoria;
- con una **formula** che dà sₙ a partire da n, come Cₙ = 3 + 1,2(n − 1): non sempre esiste, e a volte esiste ma non la si conosce;
- più in generale con un **programma** che riceve l'indice n e restituisce sₙ.

Le stesse sequenze si studiano in analisi con altri obiettivi, come l'andamento o il limite; in informatica interessa spesso quanto costa calcolarle.

## Notazioni e il nome dell'indice
La sequenza intera si indica con s oppure con {sₙ}; sₙ da solo indica l'elemento di indice n, che esiste solo se n sta nel dominio. Quando il dominio è {k, k + 1, k + 2, …} si scrive {sₙ}_{n=k}^{∞}: per esempio {sₙ}_{n=0}^{∞} ha per dominio tutti i naturali. Quando il dominio è finito, {i, i + 1, …, j}, si scrive {sₙ}_{n=i}^{j}.

**Esempio.** Sia s la sequenza dei numeri pari positivi, 2, 4, 6, 8, …, indicizzata dagli interi positivi. La legge generale è sₙ = 2n: s₁ = 2, s₂ = 4, s₃ = 6 (esempio del libro ripreso dal docente).

**Esempio con indici negativi.** Il dominio può contenere anche lo zero e dei negativi. Sia yₙ = 3ⁿ per −2 ≤ n ≤ 2: gli elementi sono y₋₂ = 1/9, y₋₁ = 1/3, y₀ = 1, y₁ = 3, y₂ = 9. Il docente fa lo stesso con xₙ = 1/2ⁿ per −1 ≤ n ≤ 4, che dà 2, 1, 1/2, 1/4, 1/8, 1/16: per avere 2 come primo elemento l'indice deve partire da −1, perché 1/2^{−1} = 2.

**L'indice è una variabile locale.** Su questo punto il docente si ferma più del libro (registrazione 2025). Il nome dell'indice lo sceglie chi scrive e vale solo dentro la sequenza: uₙ = n² − 1 per n ≥ 0 e uₘ = m² − 1 per m ≥ 0 sono **la stessa sequenza**, scritta con due nomi diversi. È come una variabile locale di una funzione in un programma (il cap. 31 fa lo stesso paragone per le variabili di una dimostrazione): ha senso solo lì, e se fuori dalla sequenza compare una m, non è la stessa m. Per lo stesso motivo, una volta nota la formula di sₙ, la formula di sᵢ, di sₙ₋₁ o di sₙ₋₂ si ottiene sostituendo all'indice l'espressione voluta. Il docente aggiunge una condizione che il libro non sottolinea: sₙ₋₁ ha senso solo se n − 1 sta nel dominio, quindi, con dominio n ≥ 0, solo per n ≥ 1; sₙ₋₂ solo per n ≥ 2.

## Formula diretta e formula di ricorrenza
L'esempio svolto in aula è quello del libro: la sequenza

sₙ = 2ⁿ + 4 · 3ⁿ, per n ≥ 0.

Sostituendo si ottiene s₀ = 1 + 4 = 5, s₁ = 2 + 12 = 14, s₂ = 4 + 36 = 40, s₃ = 8 + 108 = 116. Le formule spostate sono sₙ₋₁ = 2^{n−1} + 4 · 3^{n−1} (per n ≥ 1) e sₙ₋₂ = 2^{n−2} + 4 · 3^{n−2} (per n ≥ 2).

**Proposizione.** Per ogni n ≥ 2 vale sₙ = 5sₙ₋₁ − 6sₙ₋₂.

(In parole povere: ogni elemento si può calcolare dai due che lo precedono, con due moltiplicazioni e una sottrazione, senza calcolare potenze. Per esempio s₂ = 5 · 14 − 6 · 5 = 70 − 30 = 40, come con la formula.)

**Dimostrazione.** Il docente avverte che, finché non è dimostrata, l'uguaglianza è una **domanda**, non un fatto: non la si può usare come ipotesi. Si prende allora il membro di destra, si sostituiscono le formule di sₙ₋₁ e sₙ₋₂ e si semplifica, scrivendo tutto in termini di 2^{n−2} e 3^{n−2} (registrazione 2025):

5sₙ₋₁ − 6sₙ₋₂ = 5 · 2^{n−1} + 20 · 3^{n−1} − 6 · 2^{n−2} − 24 · 3^{n−2}.

Poiché 2^{n−1} = 2 · 2^{n−2} e 3^{n−1} = 3 · 3^{n−2}, il primo termine diventa 10 · 2^{n−2} e il secondo 60 · 3^{n−2}. Raccogliendo: (10 − 6) · 2^{n−2} + (60 − 24) · 3^{n−2} = 4 · 2^{n−2} + 36 · 3^{n−2}. Infine 4 · 2^{n−2} = 2² · 2^{n−2} = 2ⁿ e 36 · 3^{n−2} = 4 · 3² · 3^{n−2} = 4 · 3ⁿ, quindi il membro di destra vale 2ⁿ + 4 · 3ⁿ = sₙ.

È un conto del tutto meccanico, commenta il docente: è il tipo di verifica che oggi un programma di calcolo simbolico sa fare da solo, anche se su problemi simili non sempre si comporta bene. Bisogna solo fare attenzione che i fattori 5 e −6 moltiplicano tutta la parentesi.

**Perché interessa a un informatico.** La verifica usa l'algebra, ma la motivazione viene dal costo del calcolo (registrazione 2025). Con la formula diretta ogni elemento richiede due potenze: con la potenza veloce del cap. 43 sono circa log₂ n prodotti ciascuna, più un prodotto e una somma. Se però si deve produrre **tutta la tabella** s₀, s₁, s₂, … in ordine, conviene la **formula di ricorrenza** sₙ = 5sₙ₋₁ − 6sₙ₋₂: una volta calcolati s₀ e s₁ con la formula diretta, ogni nuovo elemento costa due prodotti e una sottrazione, perché i due precedenti sono già stati calcolati. Per un valore isolato, con n grande, conviene invece la formula diretta: la ricorrenza obbligherebbe a calcolare tutti i valori prima di lui. Sono due formule utili in situazioni diverse, e a scegliere tra le due è proprio l'attenzione al costo. Le formule di ricorrenza torneranno nel corso di algoritmi; il libro le riprende nel suo capitolo 7.

**Esercizio (libro, esercizi 121-128; soluzione nostra).** Sia rₙ = 3 · 2ⁿ − 4 · 5ⁿ per n ≥ 0. I primi valori sono r₀ = 3 − 4 = −1, r₁ = 6 − 20 = −14, r₂ = 12 − 100 = −88. Si dimostra che rₙ = 7rₙ₋₁ − 10rₙ₋₂ per n ≥ 2. Con lo stesso metodo, si scrive tutto in termini di 2^{n−2} e 5^{n−2}:
- parte con il 2: 7 · 3 · 2^{n−1} − 10 · 3 · 2^{n−2} = (42 − 30) · 2^{n−2} = 12 · 2^{n−2} = 3 · 2ⁿ;
- parte con il 5: 7 · (−4) · 5^{n−1} − 10 · (−4) · 5^{n−2} = (−140 + 40) · 5^{n−2} = −100 · 5^{n−2} = −4 · 5ⁿ.

La somma è 3 · 2ⁿ − 4 · 5ⁿ = rₙ. Controllo numerico: 7 · (−14) − 10 · (−1) = −98 + 10 = −88 = r₂.

## Sequenze crescenti e decrescenti
**Definizione.** Una sequenza s è:
- **crescente** se per ogni i, j del dominio con i < j vale sᵢ < sⱼ;
- **decrescente** se per ogni i, j del dominio con i < j vale sᵢ > sⱼ;
- **non decrescente** se per ogni i, j del dominio con i < j vale sᵢ ≤ sⱼ;
- **non crescente** se per ogni i, j del dominio con i < j vale sᵢ ≥ sⱼ.

(In parole povere: crescente vuol dire che salendo con l'indice i valori salgono sempre; non decrescente vuol dire che non scendono mai, ma possono fermarsi per un po'. Come una scala con dei pianerottoli: si sale o si resta in piano, ma non si torna mai giù.)

Nel libro «crescente» è sempre in senso stretto. Il docente segnala che la non decrescenza si trova spesso chiamata **debolmente crescente**, dove «debolmente» vuol dire che è ammesso anche l'uguale, e lo stesso per **debolmente decrescente**; i termini inglesi del libro sono ~increasing~, ~decreasing~, ~nondecreasing~, ~nonincreasing~ (registrazione 2025).

**Esempio (con numeri nostri).** La sequenza 50, 40, 40, 25, 25, 25, 10 è non crescente: non sale mai, e quando scende non torna indietro. Non è decrescente, perché ha dei tratti fermi (s₂ = s₃ = 40). È lo stesso tipo di esempio usato dal docente, con i numeri del libro.

Attenzione: «non decrescente» **non** è la negazione di «decrescente». La sequenza 1, 0, −1, 0 non è decrescente (l'ultimo passo sale) e non è nemmeno non decrescente (i primi passi scendono): non ha nessuna delle quattro proprietà.

**Il caso di un solo elemento.** Una sequenza con un solo elemento, per esempio la sequenza che ha come unico termine 100, è crescente, decrescente, non crescente e non decrescente **tutte insieme**. Il docente lo spiega con i quantificatori: le quattro definizioni sono affermazioni universali sulle coppie di indici i < j, e con un solo indice di coppie non ce ne sono. Un universale su un insieme vuoto è sempre vero (cap. 30 e cap. 44). Sono casi degeneri, ma bisogna saperli riconoscere: se si chiede una risposta a un computer, è proprio lì che arrivano le risposte strane (registrazione 2025).

**Basta guardare i vicini (dal libro).** Se il dominio è fatto di interi consecutivi, per vedere che s è crescente basta controllare che sᵢ < sᵢ₊₁ per ogni coppia di indici vicini; lo stesso per le altre tre proprietà, con il simbolo corrispondente. Il libro lo lascia come esercizio (4), da fare per induzione: da sᵢ < sᵢ₊₁ < sᵢ₊₂ < … si arriva a sᵢ < sⱼ per ogni j > i.

**Esercizio (libro, esercizi 5-9; soluzione nostra).** La sequenza sₙ = 2ⁿ − n², già incontrata nel cap. 45, su domini diversi:
- D = {0, 1}: valori 1, 1. È non crescente e non decrescente, ma né crescente né decrescente;
- D = {0, 1, 2, 3}: valori 1, 1, 0, −1. È solo non crescente;
- D = {1, 2, 3}: valori 1, 0, −1. È decrescente, e quindi anche non crescente;
- D = {1, 2, 3, 4}: valori 1, 0, −1, 0. Nessuna delle quattro;
- D = {n ∈ ℤ : n ≥ 3}: valori −1, 0, 7, 28, 79, … È crescente, e quindi anche non decrescente. Per dimostrarlo basta guardare i vicini: sₙ₊₁ − sₙ = 2ⁿ⁺¹ − (n + 1)² − 2ⁿ + n² = 2ⁿ − 2n − 1, e per n ≥ 3 vale 2ⁿ ≥ 2n + 2 (per induzione: 2³ = 8 = 2 · 3 + 2, e se 2ⁿ ≥ 2n + 2 allora 2ⁿ⁺¹ ≥ 4n + 4 ≥ 2(n + 1) + 2). Quindi sₙ₊₁ − sₙ ≥ 1 > 0.

## Sottosequenze
**Definizione.** Una **sottosequenza** di una sequenza s è una sequenza che si ottiene da s scegliendo alcuni suoi termini e lasciandoli **nello stesso ordine** in cui compaiono in s. I termini scelti non devono essere consecutivi. Se n₁ < n₂ < n₃ < … sono gli indici scelti, la sottosequenza si scrive {s_{nₖ}}.

(In parole povere: si cancellano alcuni elementi dell'elenco e si tengono gli altri, senza spostarli. Da una playlist si possono togliere dei brani, ma quelli che restano si ascoltano nell'ordine originale.)

**Esempio.** Dalla sequenza dei dispari tₙ = 2n − 1, cioè 1, 3, 5, 7, 9, 11, 13, …, si tengono il primo, il terzo, il quinto termine e così via: si ottiene 1, 5, 9, 13, 17, … Gli indici scelti sono nₖ = 2k − 1, e il k-esimo termine della sottosequenza è t_{nₖ} = 2(2k − 1) − 1 = 4k − 3 (libro, esercizi 109-112; soluzione nostra). Il docente fa l'esempio analogo di tenere solo gli elementi di indice pari, s₂, s₄, s₆, …, buttando via quelli di indice dispari. Invece 5, 1, 9 non è una sottosequenza dei dispari: gli elementi ci sono, ma l'ordine è cambiato.

Nella notazione s_{nₖ} la lettera n non è più l'indice di s: è essa stessa una sequenza, quella degli indici scelti, e il suo indice è k. Il libro ammette che è un abuso di notazione, mantenuto per tradizione.

Il docente avverte che su questo termine i libri non sono d'accordo: alcuni chiedono che i termini di una sottosequenza siano consecutivi, altri no. Nel corso si segue il libro: nella sottosequenza i termini possono essere sparsi, mentre quando servono termini consecutivi si parlerà di **sottostringa**, nel prossimo capitolo (registrazione 2025).

## Somme e prodotti
Questa sezione è solo dal libro: nella registrazione 2025 il docente non la tratta, ma la notazione ricorre continuamente.

**Definizione.** Se {aᵢ}_{i=m}^{n} è una sequenza, si scrive Σ_{i=m}^{n} aᵢ = aₘ + aₘ₊₁ + … + aₙ per la somma dei suoi termini e Π_{i=m}^{n} aᵢ = aₘ · aₘ₊₁ · … · aₙ per il loro prodotto. La lettera i è l'**indice**, m il **limite inferiore**, n il **limite superiore**.

(In parole povere: Σ è un modo compatto per dire «somma tutti i termini dal numero m al numero n», Π lo stesso per il prodotto. È un ciclo for scritto in matematica, con i come contatore.)

**Esempio.** Con aᵢ = 2i − 1: Σ_{i=1}^{4} aᵢ = 1 + 3 + 5 + 7 = 16 e Π_{i=1}^{4} aᵢ = 1 · 3 · 5 · 7 = 105. Anche qui l'indice è una variabile locale: cambiando nome e limiti insieme, per esempio con i = j + 1, la stessa somma si scrive Σ_{j=0}^{3} (2j + 1), che dà ancora 1 + 3 + 5 + 7.

## Riepilogo
- Una sequenza è una funzione con dominio un insieme di interi; sₙ è l'elemento di indice n. Si rappresenta con una tabella, una formula o un programma.
- L'indice è una variabile locale: si può rinominare, e sₙ₋₁ ha senso solo se n − 1 sta nel dominio.
- Per sₙ = 2ⁿ + 4 · 3ⁿ vale la ricorrenza sₙ = 5sₙ₋₁ − 6sₙ₋₂ (n ≥ 2): si dimostra sostituendo e riscrivendo tutto con 2^{n−2} e 3^{n−2}. La ricorrenza conviene per produrre tutta la tabella (calcolati s₀ e s₁ con la formula diretta, ogni nuovo elemento costa due prodotti e una sottrazione), la formula diretta per un valore isolato.
- Crescente, decrescente, non decrescente (debolmente crescente), non crescente: affermazioni universali sulle coppie i < j; con un solo elemento sono tutte vere.
- Una sottosequenza tiene alcuni termini nello stesso ordine, non necessariamente consecutivi.
- Σ e Π indicano somma e prodotto dei termini tra due limiti.
