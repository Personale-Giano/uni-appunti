# 28. Le Quattro Forme dei Quantificatori Annidati
## Il quadro completo
I capitoli 25-27 hanno mostrato i quantificatori annidati su molti esempi: la somma di due positivi e x + y = 0 nel cap. 25, il programma che li decide nel cap. 26, minimo, massimo, numeri composti e primi nel cap. 27. Qui si mette ordine: con due variabili le forme sono quattro, e per ciascuna serve sapere esattamente quando è vera e quando è falsa. Gli esempi già svolti non si ripetono: basta ritrovarli al capitolo indicato.

**Definizione.** Una funzione proposizionale a due variabili P(x, y) ha come **dominio del discorso** un prodotto cartesiano X × Y: la x prende valori in X e la y in Y.

(In parole povere: il dominio è l'elenco di tutte le coppie che si possono provare. Se X e Y sono i reali, una coppia è un punto del piano; in un foglio di calcolo è una casella, riga x e colonna y.)

## Le quattro definizioni
**Definizione.** L'enunciato ∀x ∀y P(x, y) è **vero** se P(x, y) è vera per ogni coppia (x, y) del dominio. È **falso** se esiste almeno una coppia per cui P(x, y) è falsa.

(In parole povere: tutte le caselle devono andare bene; ne basta una sbagliata per smentirlo. Esempi: «la somma di due positivi è positiva» è vero; «x > 0 e y < 0 implicano x + y ≠ 0» è falso, come mostra la coppia x = 1, y = −1. Il cap. 25 lo fa con i segni di x e y scambiati.)

**Definizione.** L'enunciato ∀x ∃y P(x, y) è **vero** se per ogni x del dominio esiste almeno una y per cui P(x, y) è vera. È **falso** se esiste una x per cui P(x, y) è falsa con tutte le y.

(In parole povere: ogni riga deve contenere almeno una casella buona, e la casella può cambiare da riga a riga. Esempi nel cap. 25: x + y = 0 sui reali è vero, con y = −x; x > y sugli interi positivi è falso, per colpa di x = 1.)

**Definizione.** L'enunciato ∃x ∀y P(x, y) è **vero** se esiste una x per cui P(x, y) è vera con tutte le y. È **falso** se per ogni x esiste almeno una y per cui P(x, y) è falsa.

(In parole povere: deve esserci una riga fatta solo di caselle buone. Esempi nel cap. 27: x ≤ y sugli interi positivi è vero, con x = 1, il minimo; x ≥ y è falso, perché x + 1 smentisce qualunque x.)

**Definizione.** L'enunciato ∃x ∃y P(x, y) è **vero** se esiste almeno una coppia (x, y) per cui P(x, y) è vera. È **falso** se P(x, y) è falsa per ogni coppia.

(In parole povere: basta una casella buona in tutta la griglia. Esempi nel cap. 27: «xy = 6 con x, y > 1» è vero con 2 e 3; con 7 al posto di 6 è falso, perché 7 è primo.)

Conviene leggere le quattro definizioni in coppia. Nelle forme con i due quantificatori uguali conta solo se nella griglia ci sono caselle buone o cattive, non dove stanno. Le forme miste sono quelle delicate: ∀x ∃y permette di scegliere y dopo aver visto x, ∃x ∀y no, e per questo la seconda chiede molto di più (cap. 25).

## La negazione scambia le forme a coppie
Le leggi di De Morgan si applicano un quantificatore per volta, dall'esterno verso l'interno: i passaggi sono nel cap. 27. Il risultato per le quattro forme è questo:

- ¬(∀x ∀y P(x, y)) ≡ ∃x ∃y ¬P(x, y);
- ¬(∀x ∃y P(x, y)) ≡ ∃x ∀y ¬P(x, y);
- ¬(∃x ∀y P(x, y)) ≡ ∀x ∃y ¬P(x, y);
- ¬(∃x ∃y P(x, y)) ≡ ∀x ∀y ¬P(x, y).

Non c'è niente da imparare a memoria in più: ogni riga è la frase «è falso se…» della definizione corrispondente, scritta in simboli. La forma ∀∀ si scambia con ∃∃, la forma ∀∃ con ∃∀.

Spesso dentro i quantificatori c'è un'implicazione. In quel caso, arrivati al predicato, si usa ¬(p → q) ≡ p ∧ ¬q (cap. 18). Per esempio, la negazione di ∀x ∀y ((x > 0 ∧ y > 0) → x + y > 0) è ∃x ∃y (x > 0 ∧ y > 0 ∧ x + y ≤ 0): «esistono due positivi con somma non positiva». Poiché l'enunciato di partenza è vero, questa negazione è falsa.

## Il gioco logico
C'è un modo divertente di decidere un enunciato con più quantificatori: immaginarlo come una partita a due, tu contro un avversario (nel libro si chiama Farley; l'idea è attribuita ad André Berthiaume). Tu vuoi rendere vera P, lui vuole renderla falsa. Le regole sono poche:

- i quantificatori si leggono da sinistra a destra, uno per volta;
- su un ∀ sceglie il valore l'avversario, su un ∃ lo scegli tu;
- come mostra l'esempio, ciascuno vede le scelte già fatte;
- alla fine si valuta P: se è vera vinci tu, se è falsa vince lui.

**Proposizione.** Se tu hai un modo di vincere qualunque cosa faccia l'avversario, l'enunciato è vero; se è l'avversario ad avere un modo di vincere sempre, l'enunciato è falso.

(In parole povere: il ∀ è una sfida che subisci, perché il valore lo decide chi vuole farti perdere; l'∃ è una mossa tua, perché il valore lo scegli tu.)

**Esempio: ∀x ∃y (x + y = 0) sui reali.** L'avversario sceglie x; tu, che lo vedi, rispondi y = −x, e la somma fa 0. Vinci sempre, quindi l'enunciato è vero.

**Esempio: ∃x ∀y (x + y = 0) sui reali.** Ora scegli prima tu la x, e l'avversario risponde. Se hai scelto x = 0, lui prende y = 1 e la somma vale 1; se hai scelto x ≠ 0, lui prende y = 0 e la somma vale x, che non è 0. Vince sempre lui, quindi l'enunciato è falso. La formula è la stessa di prima: è cambiato solo chi muove per primo.

Perché il gioco funziona? Nel caso ∀x ∀y l'avversario sceglie entrambi i valori, quindi può vincere solo se esiste una coppia che rende P falsa, cioè un controesempio. Nel caso ∀x ∃y vinci se a ogni x sai opporre una y adatta, e perdi se esiste una x che rende P falsa con tutte le y: è proprio la definizione. Per le altre forme e per più variabili il libro afferma che il criterio resta valido, con le stesse regole, senza svolgere i dettagli.

## Come dimostrare o confutare
Da definizioni e gioco si ricava cosa fare in ciascuno degli otto casi:

- **∀x ∀y vero:** si ragiona con x e y arbitrari e si mostra che P vale.
- **∀x ∀y falso:** si trova una coppia con P falsa: bastano due valori.
- **∀x ∃y vero:** si fissa x arbitrario e si trova una y, che può dipendere da x, con P vera.
- **∀x ∃y falso:** si trova una sola x e poi, con y arbitraria, si mostra che P è sempre falsa.
- **∃x ∀y vero:** si trova una sola x e poi, con y arbitraria, si mostra che P è sempre vera.
- **∃x ∀y falso:** si fissa x arbitrario e si trova una y, che può dipendere da x, con P falsa.
- **∃x ∃y vero:** si trova una coppia con P vera: bastano due valori.
- **∃x ∃y falso:** si ragiona con x e y arbitrari e si mostra che P è falsa.

Solo due casi su otto si chiudono esibendo due valori; negli altri c'è sempre una parte «arbitraria», e lì serve un ragionamento, non una prova su esempi. Si riconosce anche la simmetria con la negazione: confutare ∀x ∃y è la stessa ricetta che dimostrare ∃x ∀y, con ¬P al posto di P.

Il secondo esempio del gioco si scrive così, seguendo la ricetta «∃x ∀y falso»: sia x un reale arbitrario; se x = 0 si sceglie y = 1, se x ≠ 0 si sceglie y = 0; in entrambi i casi x + y ≠ 0. Si noti che la y scelta dipende da x, ed è permesso.

Il capitolo seguente passa agli esercizi di ripasso su De Morgan, domini e ordine dei quantificatori.
