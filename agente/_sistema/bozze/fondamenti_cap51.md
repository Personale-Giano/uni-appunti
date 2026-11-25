# 51. Relazioni d'Ordine e Relazioni di Equivalenza
## Ordini: riflessivi, antisimmetrici, transitivi
Le proprietà del cap. 50, combinate, danno i due tipi di relazione più usati. Il primo serve a confrontare gli elementi. (lezione 2026) Nella lezione 24 del 23 novembre 2026 il docente distingue l'ordine **debole**, come ≤, dall'ordine **stretto**, come <, e lavora con quello debole, che è quello che il libro chiama ordine parziale.

**Definizione.** Una relazione R su un insieme X è una **relazione d'ordine** (nel libro ~partial order~, ordine parziale) se è riflessiva, antisimmetrica e transitiva. Per un ordine si scrive spesso x ≼ y al posto di (x, y) ∈ R.

(In parole povere: un ordine dice «chi viene prima di chi» senza contraddizioni: ognuno viene prima o insieme a se stesso, due elementi diversi non possono venire ciascuno prima dell'altro, e se a viene prima di b e b prima di c, a viene prima di c. Come ≤ tra i numeri.)

L'esempio più semplice è ≤ sugli interi: x ≤ x per ogni x, da x ≤ y e y ≤ x segue x = y, e da x ≤ y e y ≤ z segue x ≤ z. Il libro aggiunge la divisibilità sugli interi positivi (Esempio 3.3.21): ogni numero divide se stesso, se x divide y e y divide x allora x = y, e se x divide y e y divide z allora x divide z. Il grafo diretto di un ordine si riconosce, come osserva il docente (lezione 2026): una volta che ci si sposta su un elemento distinto non si torna più indietro, non importa quanti passi si facciano. Da 1 si va a 2, e da lì a 3 e a 4, ma a 1 non si torna mai.

## Ordini totali e ordini parziali
**Definizione.** Due elementi x e y sono **confrontabili** rispetto a un ordine ≼ se x ≼ y oppure y ≼ x. Un ordine in cui due elementi qualunque sono confrontabili si chiama **ordine totale**; altrimenti l'ordine è **non totale**.

(In parole povere: un ordine è totale quando non ci sono «pareggi impossibili da decidere»: presi due elementi, si sa sempre quale viene prima. Gli interi sono così; due telefoni confrontati su prezzo e batteria spesso no, se uno costa meno ma l'altro dura di più.)

(lezione 2026) Il docente scrive la totalità sugli interi così: dati due interi x e y, vale x < y oppure x = y oppure x > y. Sul grafo vuol dire che, presi due punti qualunque, da uno dei due si può andare all'altro con una freccia; non si chiede che sia il primo a essere più piccolo del secondo, solo che i due siano confrontabili, e se i due punti coincidono basta il cappio.

L'esempio che mostra è quello del libro (Esempio 3.3.4): la relazione x ≤ y su {1, 2, 3, 4}, con i cappi su tutti i punti e le frecce 1 → 2, 1 → 3, 1 → 4, 2 → 3, 2 → 4, 3 → 4. È una descrizione completa dell'ordine, anche se il disegno a prima vista sembra «stranissimo»: per 1 e 4 c'è la freccia da 1 a 4, per 3 e 2 la freccia da 2 a 3. Togliendo tutti i cappi si ottiene il grafo dell'ordine stretto <. (In aula il docente la chiama per un momento «maggiore o uguale»; le frecce però vanno dal numero più piccolo al più grande, e la relazione del libro è x ≤ y.)

![(a) Il grafo di x ≤ y su {1, 2, 3, 4}, un ordine totale; (b) una relazione di equivalenza su {1, …, 6} con classi {1, 3, 5}, {2, 6}, {4}; (c) l'uguaglianza su {a, b, c}, che è insieme un ordine e un'equivalenza.](figure/fond/ordine_equivalenza.png|16)

**Esempio (lezione 2026): l'inclusione.** Sull'insieme dei sottoinsiemi di {a, b, c}, che sono otto (∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}), l'inclusione ⊆ è un ordine: ogni insieme è incluso in se stesso (riflessività); se A ⊆ B e B ⊆ A allora A = B, la proprietà della doppia inclusione (antisimmetria); se A ⊆ B e B ⊆ C allora A ⊆ C (transitività). Ma **non è totale**: {a} non è incluso in {b} e {b} non è incluso in {a}, quindi {a} e {b} non sono confrontabili. Allo stesso modo la divisibilità non è totale: 2 non divide 3 e 3 non divide 2.

**Perché all'informatica interessano gli ordini parziali.** (lezione 2026) Gli ordini della matematica, come quelli sui numeri, sono spesso totali; la maggior parte degli ordini che interessano l'informatica invece no. Quando si chiede di migliorare una situazione che dipende da tanti parametri, un cambiamento può migliorarne alcuni e peggiorarne altri, e si arriva a una situazione non confrontabile con quella di prima. Se si ordinano le scelte che una macchina può fare in base all'obiettivo che le è stato dato, mettendo più in alto quelle che avvicinano di più all'obiettivo, quest'ordine tipicamente non è totale: ci possono essere due scelte tali che nessuna delle due è un miglioramento rispetto all'altra.

## Relazioni di equivalenza
**Definizione.** Una relazione R su X è una **relazione di equivalenza** se è riflessiva, simmetrica e transitiva.

(In parole povere: un'equivalenza dice «chi è dello stesso tipo di chi», senza badare a chi viene prima: ognuno è del suo stesso tipo, se a è come b allora b è come a, e se a è come b e b è come c allora a è come c. «Ha lo stesso colore di» tra palline colorate è un'equivalenza.)

(lezione 2026) Il docente le confronta con gli ordini: in comune hanno la riflessività e la transitività, ma al posto dell'antisimmetria c'è la simmetria. Un'equivalenza è una relazione che non guarda l'ordine tra due elementi.

**Esempio (lezione 2026).** Il docente mostra il grafo di una relazione di equivalenza su {1, 2, 3, 4, 5, 6} con classi {1, 3, 5}, {2, 6} e {4} (appunti del docente, figura (b) qui sopra) e controlla le tre proprietà:
- riflessività: ogni elemento ha il suo cappio;
- simmetria: se da 3 si va a 1 si torna da 1 a 3, se da 3 si va a 5 si torna da 5 a 3, se da 2 si va a 6 si torna da 6 a 2; da 3 non si va a 2, e quindi non serve neanche poter tornare;
- transitività: da 3 si va a 5 e da 5 a 1, e la freccia da 3 a 1, che fa lo stesso spostamento in un passo solo, c'è già.

Gli elementi risultano divisi in gruppi, le **classi di equivalenza**: in ciascuna ci sono gli elementi che si raggiungono l'uno dall'altro. Dentro una classe ci si può spostare liberamente e si può sempre tornare dove si è già stati, ma non si passa mai a un'altra classe. È la partizione associata a un'equivalenza vista nel corso di Matematica discreta (cap. 7-9 di quei riassunti). Gli ordini, nota il docente, sono anch'essi chiusi per composizione di frecce, ma con una differenza: in un ordine non si torna mai indietro, a meno di restare sullo stesso elemento.

## Una relazione può essere un ordine e un'equivalenza?
(lezione 2026) Verso la fine della lezione il docente pone una domanda «banale»: esiste una relazione che sia sia d'ordine sia di equivalenza? La risposta è sì, ma solo una, e stupidissima. Il motivo per cui conviene porsi lo stesso la domanda è il punto di vista delle macchine: una macchina non ha la nozione di relazione «importante». Nelle definizioni non c'è nessun metro per valutare l'interesse di una relazione per noi, sono tutte sullo stesso piano, e se si pone la domanda a una macchina la risposta arriva comunque, per quanto banale sia.

**Proposizione.** Sia R una relazione su un insieme X. R è sia una relazione d'ordine sia una relazione di equivalenza se e solo se R è l'uguaglianza su X, cioè R = {(x, x) : x ∈ X}.

(In parole povere: l'unico modo di essere insieme un ordine e un'equivalenza è non collegare mai due elementi diversi, e collegare ciascuno con se stesso.)

**Dimostrazione** (del docente, completata nel verso facile). Una relazione che è sia d'ordine sia di equivalenza deve essere riflessiva e transitiva, e questo non è un problema, perché lo sono entrambe. Ma deve essere anche simmetrica e antisimmetrica insieme.
- Se a R b, per simmetria b R a, e allora per antisimmetria a = b. Quindi R collega ogni elemento al più con se stesso: R ⊆ {(x, x) : x ∈ X}.
- Per riflessività ogni elemento è in relazione con se stesso, quindi {(x, x) : x ∈ X} ⊆ R. Per doppia inclusione, R è esattamente l'uguaglianza.
- Viceversa, l'uguaglianza è riflessiva, simmetrica e antisimmetrica (non ci sono coppie di elementi distinti) e transitiva (da x = y e y = z segue x = z), quindi è un ordine e un'equivalenza (precisazione nostra).
In aula il docente mostra la stessa soluzione graficamente, con il disegno del libro (Esempio 3.3.15): tre elementi a, b, c, ciascuno con il cappio e nessun'altra freccia (figura (c)). Se da un punto si andasse a un altro, si dovrebbe poter tornare indietro per simmetria, e allora per antisimmetria i due punti dovrebbero essere uguali.

**L'uguaglianza come «zero» degli ordini.** (lezione 2026) Come ordine, l'uguaglianza non confronta mai due elementi distinti: collega ogni elemento solo con se stesso, perché lo chiede la definizione. È la più piccola relazione d'ordine possibile, quella che non ordina niente; negli appunti del docente si legge che è un ordine non totale appena ci sono almeno due elementi distinti. Se si cerca una relazione che orienti le scelte di una macchina, l'uguaglianza vuol dire che di miglioramenti non banali («b è meglio di a») non se n'è ancora trovato nessuno. Ha la stessa importanza dello zero nei numeri non negativi, o della stringa vuota per dire che un campo di testo è ancora vuoto: indica la mancanza di qualcosa.

## Riepilogo
- Ordine (parziale): riflessivo, antisimmetrico, transitivo, come ≤ o l'inclusione. Totale se due elementi qualunque sono confrontabili: ≤ sugli interi sì, l'inclusione e la divisibilità no.
- Negli ordini, una volta passati a un elemento distinto non si torna più indietro; in informatica gli ordini sono quasi sempre parziali.
- Equivalenza: riflessiva, simmetrica, transitiva; divide l'insieme in classi, dentro le quali ci si muove liberamente.
- La sola relazione che è insieme ordine ed equivalenza è l'uguaglianza: simmetria più antisimmetria obbligano a collegare ogni elemento solo con se stesso.

Nell'ultima parte della lezione il docente usa un grafo di frecce per un esercizio sui quantificatori, svolto nel prossimo capitolo.
