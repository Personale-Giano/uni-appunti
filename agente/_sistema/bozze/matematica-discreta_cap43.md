# 43. I Numeri Interi e le Loro Operazioni
## Si comincia l'aritmetica
Con questa lezione inizia l'argomento che, come ha annunciato il docente, occuperà in diverse forme tutta la parte finale del corso: l'**aritmetica**. Si parte da cose note, ma guardate da un punto di vista più formale e critico.

L'aritmetica, almeno all'inizio, è lo studio dell'insieme ℤ dei **numeri interi**: i numeri naturali e i loro opposti, …, −2, −1, 0, 1, 2, …. A lezione il docente ha ricordato che i naturali sono dati in modo assiomatico (cap. 5), mentre gli interi si possono costruire a partire dai naturali con le tecniche della teoria degli insiemi. La costruzione non si fa nel corso, perché sarebbe troppo collaterale: chi è curioso la trova in appendice al libro o cercando «costruzione dei numeri interi».

## Le due operazioni e le loro proprietà
I numeri interi non vengono da soli: arrivano con due operazioni, l'**addizione** a + b e la **moltiplicazione** a · b. Le loro proprietà sono quelle imparate a scuola, ma conviene elencarle con cura, perché saranno la base per tutto il discorso successivo. Per ogni a, b, c ∈ ℤ:
- **associativa**: (a + b) + c = a + (b + c) e (a · b) · c = a · (b · c);
- **commutativa**: a + b = b + a e a · b = b · a;
- **elementi neutri**: 0 per l'addizione e 1 per la moltiplicazione, cioè a + 0 = a e a · 1 = a;
- **opposto**: per ogni a esiste −a con a + (−a) = 0;
- **distributiva**: a · (b + c) = a · b + a · c.

Le prime tre proprietà sono «doppie»: valgono allo stesso modo per l'addizione e per la moltiplicazione. La quarta invece vale solo per l'addizione. In ℤ, in generale, non esiste un numero che moltiplicato per un dato numero dia 1: per esempio non esiste nessun intero x con 2 · x = 1, perché 1/2 non è un intero ma un razionale. È uno dei motivi per cui ci si allarga da ℤ a ℚ e poi a ℝ. Restando in ℤ, però, i soli numeri con un «inverso moltiplicativo» sono 1 e −1, perché 1 · 1 = 1 e (−1) · (−1) = 1.

Queste prime quattro proprietà riguardano una operazione alla volta; la distributiva è l'unica che le mette in relazione.

**Esempio.** 3 · (4 + 5) = 3 · 9 = 27 e 3 · 4 + 3 · 5 = 12 + 15 = 27.

## La stessa lista altrove
Il docente fa notare che, pensate in astratto, queste sono proprietà che si sono già viste altrove.
- Nelle **permutazioni** c'è una sola operazione, la composizione: è associativa, ha un elemento neutro (l'identità) e ogni permutazione ha un'inversa (cap. 32). Non è però commutativa.
- Nelle **matrici** n × n ci sono somma e prodotto: valgono proprietà molto simili, con piccole modifiche. La commutativa vale per la somma ma non per il prodotto, e per avere l'inversa di una matrice rispetto al prodotto serve una condizione.

L'elenco di riferimento è sempre questo: nei vari oggetti matematici alcune proprietà valgono e altre no, ma la lista da controllare è la stessa.

## Rispetto alla somma ℤ è semplice
Fare aritmetica vuol dire capire la struttura di ℤ rispetto alle due operazioni. Rispetto alla somma la struttura è molto semplice: partendo da 0 e da 1, e permettendo di prendere gli opposti, si ottiene tutto ℤ:

2 = 1 + 1, 3 = 1 + 1 + 1, …, −2 = (−1) + (−1), −3 = (−1) + (−1) + (−1), …

Si dice che 1 **genera** ℤ rispetto alla somma: partendo da 1 si ha tutto. Lo stesso funziona partendo da −1 (si ottengono prima i negativi e poi, con gli opposti, i positivi). Con un altro numero invece no: partendo da 2 si ottengono 2, 4, 6, … e i loro opposti, cioè solo una parte di ℤ; 3, per esempio, non si ottiene mai.

(In parole povere: con mattoncini da 1 e la possibilità di toglierli si costruisce qualsiasi numero intero; con mattoncini da 2 si costruiscono solo i numeri pari.)

## Rispetto al prodotto ℤ è complicato
Con la moltiplicazione lo stesso gioco non funziona, ed è qui che la cosa diventa interessante. Moltiplicando ripetutamente un solo numero per se stesso:
- partendo da 1 si ottiene sempre 1 · 1 · … · 1 = 1, e non si va da nessuna parte;
- partendo da 2 si ottengono le potenze 2, 4, 8, 16, …, e si perdono moltissimi numeri, sempre di più man mano che si va avanti;
- partendo da −1 si oscilla: (−1)² = 1, (−1)³ = −1, e così via, tra −1 e 1.

Nessun numero, da solo, genera ℤ moltiplicativamente. La struttura moltiplicativa di ℤ è molto più complicata di quella additiva, e la nozione che diventa importante per studiarla è quella di **divisibilità**, l'argomento del prossimo capitolo.
