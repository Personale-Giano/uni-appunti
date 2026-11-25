# 50. Le Proprietà delle Relazioni: Riflessiva, Simmetrica, Antisimmetrica, Transitiva
## Un ripasso con la lente d'ingrandimento
Nella seconda ora della lezione 24 (23 novembre 2026) il docente comincia la sezione 3.3 del libro con una serie di esercizi sulle relazioni. Sono concetti già visti nel corso di Matematica discreta (cap. 8 e 9 di quei riassunti), e il docente lo dice apertamente: gli esempi non hanno «la benché minima importanza», se non quella di ricordare con esattezza che cosa vuol dire ciascuna proprietà. In questo corso, spiega, si guardano domande molto più semplici che a Matematica, ma con un dettaglio maggiore, perché l'obiettivo è capire che cosa serve per **automatizzare** la risposta a domande del genere. Le parti tratte dalla lezione 2026 sono segnate «(lezione 2026)»; il resto viene dal libro (§3.3, pp. 141-146).

## Relazioni su un insieme e grafi diretti
**Definizione.** Una **relazione** (binaria) R da un insieme X a un insieme Y è un sottoinsieme del prodotto cartesiano X × Y. Se (x, y) ∈ R si scrive anche x R y e si dice che x è in relazione con y. Se X = Y, R si dice una **relazione su X**.

(In parole povere: una relazione è un elenco di coppie «chi è collegato a chi». Su X = {1, 2, 3} la relazione «minore di» è l'elenco {(1, 2), (1, 3), (2, 3)}.)

Una funzione da X a Y è una relazione particolare: quella in cui da ogni elemento di X parte esattamente una coppia (cap. 45). Una relazione su un insieme si può dare elencando le coppie, come fa il libro, oppure disegnando il suo **grafo diretto** (in inglese ~digraph~): si disegna un punto per ogni elemento di X e una freccia da x a y per ogni coppia (x, y) ∈ R. Una coppia della forma (x, x) diventa una freccia che parte da x e torna in x, chiamata **cappio** (in inglese ~loop~): il docente la descrive come una freccia che connette un elemento con se stesso. (lezione 2026) Il docente usa le due rappresentazioni come equivalenti: lo stesso esercizio lo guarda prima sull'insieme di coppie, poi sul disegno, che spesso aiuta a vedere subito la risposta.

L'esempio che accompagna tutto il capitolo è quello del libro (Esempio 3.3.5): la relazione R = {(a, a), (b, c), (c, b), (d, d)} sull'insieme X = {a, b, c, d}. Nel grafo, a e d hanno un cappio, mentre tra b e c ci sono due frecce, una per verso.

![Il grafo diretto della relazione R = {(a, a), (b, c), (c, b), (d, d)} su {a, b, c, d}: cappi in a e in d, due frecce opposte tra b e c.](figure/fond/relazione_abcd.png|7)

Per ogni proprietà, negli appunti proiettati in aula (lezione 2026) il docente scrive la definizione con i quantificatori e, accanto, la sua negazione, ottenuta con le leggi di De Morgan per i quantificatori (cap. 22): è la negazione che dice che cosa bisogna trovare per mostrare che la proprietà è falsa.

## Riflessiva
**Definizione.** Una relazione R su X è **riflessiva** se (x, x) ∈ R per ogni x ∈ X, cioè ∀x ∈ X (x, x) ∈ R.

(In parole povere: ogni elemento è in relazione con se stesso. Nel grafo, ogni punto ha il suo cappio. La relazione «ha la stessa età di» tra persone è riflessiva: ognuno ha la propria età.)

La negazione è ∃x ∈ X (x, x) ∉ R: basta un solo elemento senza cappio. (lezione 2026) La relazione R dell'esempio non è riflessiva: a e d sono in relazione con se stessi, ma b no, e nemmeno c. Il docente mostra anche il caso opposto, il grafo di una relazione riflessiva in cui tutti e quattro gli elementi hanno il cappio (è il grafo del cap. 51).

## Simmetrica
**Definizione.** Una relazione R su X è **simmetrica** se per ogni x, y ∈ X, da (x, y) ∈ R segue (y, x) ∈ R, cioè ∀x, y ∈ X ((x, y) ∈ R → (y, x) ∈ R).

(In parole povere: ogni freccia si può percorrere anche all'indietro. «È fratello o sorella di» è simmetrica: se Anna è sorella di Luca, Luca è fratello di Anna.)

La negazione è ∃x, y ∈ X ((x, y) ∈ R ∧ (y, x) ∉ R): una freccia senza la freccia di ritorno. (lezione 2026) La relazione R è simmetrica. Il docente controlla tutte le frecce: da b si va a c e si torna con (c, b), da c si va a b e si torna con (b, c); per i cappi in a e in d il controllo è banale, perché per tornare indietro si usa la freccia stessa. Come esempio di relazione non simmetrica cita l'ordine sui reali: da 0 si va a 1, perché 0 < 1, ma da 1 non si torna a 0, perché 1 non è minore di 0. Una relazione d'ordine, a meno che sia banale, ogni volta che collega due elementi distinti non consente di tornare indietro.

## Antisimmetrica
**Definizione.** Una relazione R su X è **antisimmetrica** se per ogni x, y ∈ X, da (x, y) ∈ R e (y, x) ∈ R segue x = y, cioè ∀x, y ∈ X ((x, y) ∈ R ∧ (y, x) ∈ R → x = y).

(In parole povere: si può andare da un punto a un altro e tornare indietro solo se si è rimasti fermi. «Ha un'età minore o uguale a quella di» non è antisimmetrica tra persone, perché due persone diverse della stessa età la soddisfano nei due versi; ≤ tra numeri invece sì.)

La negazione è ∃x, y ∈ X ((x, y) ∈ R ∧ (y, x) ∈ R ∧ x ≠ y): due elementi distinti collegati nei due versi. (lezione 2026) L'esempio tipico, dice il docente, sono gli ordini deboli come ≤ sui reali o sugli interi: se a ≤ b e b ≤ a, allora a = b; se invece a < b, non si può avere b ≤ a, perché da un elemento più grande non si torna a uno più piccolo. La relazione R dell'esempio **non** è antisimmetrica: si va da b a c e si torna da c a b, ma b ≠ c. In particolare R non è un ordine.

Il libro dà anche una forma equivalente, ottenuta per contrapposizione (cap. 36): R è antisimmetrica se per ogni x ≠ y almeno una delle coppie (x, y), (y, x) non sta in R. Nel grafo: tra due punti distinti c'è al più una freccia.

**Trabocchetto d'Esame.** «Antisimmetrica» non vuol dire «non simmetrica». La relazione {(a, a), (b, b), (c, c)} su {a, b, c} è simmetrica e antisimmetrica insieme (libro, Esempio 3.3.15): non ci sono coppie di elementi distinti, quindi la condizione dell'antisimmetria non viene mai messa alla prova. Al contrario, la relazione {(1, 2), (2, 1), (2, 3)} su {1, 2, 3} non è né simmetrica (manca (3, 2)) né antisimmetrica (1 e 2 sono collegati nei due versi) (esempio nostro).

## Transitiva
**Definizione.** Una relazione R su X è **transitiva** se per ogni x, y, z ∈ X, da (x, y) ∈ R e (y, z) ∈ R segue (x, z) ∈ R, cioè ∀x, y, z ∈ X ((x, y) ∈ R ∧ (y, z) ∈ R → (x, z) ∈ R).

(In parole povere: ogni volta che due frecce si possono percorrere una dopo l'altra, c'è anche la «scorciatoia» diretta. «È antenato di» è transitiva: l'antenato di un mio antenato è anche mio antenato.)

La negazione è ∃x, y, z ∈ X ((x, y) ∈ R ∧ (y, z) ∈ R ∧ (x, z) ∉ R). (lezione 2026) Il docente spiega la transitività sui disegni del cap. 51: se da 1 si va a 2 e da 2 a 3, nella relazione d'ordine ci si può andare anche in un passo solo, da 1 a 3. Le relazioni transitive, dice, sono **chiuse per composizione di frecce**: componendo due frecce si ottiene una freccia che sta già nella relazione.

La relazione R dell'esempio non è transitiva (libro, Esempio 3.3.19): (b, c) e (c, b) stanno in R, ma (b, b) no. Il docente in aula controlla solo le prime tre proprietà, come nei suoi appunti. Il libro osserva anche che nei controlli si possono saltare i casi con x = y o y = z, perché lì la conclusione è automaticamente vera: per esempio, se x = y, la coppia (x, z) è proprio la coppia (y, z), che sta in R per ipotesi.

## Esercizio riassuntivo
Per la relazione R = {(a, a), (b, c), (c, b), (d, d)} su {a, b, c, d}:
- riflessiva: **no**, b non ha il cappio, cioè (b, b) ∉ R;
- simmetrica: **sì**, l'unica freccia tra elementi distinti, da b a c, ha la freccia di ritorno, e i cappi sono simmetrici da soli;
- antisimmetrica: **no**, (b, c) e (c, b) stanno in R con b ≠ c;
- transitiva: **no**, (b, c) e (c, b) stanno in R ma (b, b) no.

**Come sottolineato a lezione.** Le proprietà valgono o non valgono «perfettamente»: non sono proprietà che devono essere soddisfatte in una certa percentuale, e basta un solo elemento o una sola coppia che non va per renderle false (registrazione 2025). Per mostrare che una proprietà è falsa basta quindi un controesempio, scelto guardando la negazione; per mostrare che è vera bisogna controllare tutti i casi.

## Riepilogo
- Una relazione su X è un insieme di coppie di elementi di X; il suo grafo diretto ha una freccia per ogni coppia e un cappio per ogni coppia (x, x).
- Riflessiva: un cappio su ogni punto. Simmetrica: ogni freccia ha quella di ritorno. Antisimmetrica: tra due punti distinti al più una freccia. Transitiva: per ogni cammino di due frecce c'è la freccia diretta.
- Ogni proprietà è un universale; la sua negazione è un esistenziale (De Morgan) e dice quale controesempio cercare.
- Antisimmetrica e non simmetrica sono cose diverse: una relazione può essere simmetrica e antisimmetrica insieme, o nessuna delle due.

Combinando queste proprietà si ottengono le relazioni d'ordine e le relazioni di equivalenza, l'argomento del prossimo capitolo.
