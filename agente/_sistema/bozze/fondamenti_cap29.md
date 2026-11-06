# 29. Esercizi su De Morgan, Domini e Ordine dei Quantificatori
## Perché questi esercizi
La lezione chiude il capitolo sui connettivi e i quantificatori con esercizi di ripasso sulle lezioni precedenti. Non essendoci appunti di quest'anno, gli esercizi che seguono sono quelli svolti alla lavagna nella registrazione 2025, ricavati dalla lista di quiz a risposta chiusa che il docente indica sul sito d'esame. Per il docente non sono difficili: sono un pretesto per controllare di ricordare bene la definizione di verità.

## De Morgan: un controesempio da guardare due volte
La negazione di ∃x ∀y (xy < 1) è stata calcolata nel cap. 27 e dà ∀x ∃y (xy ≥ 1). Nella registrazione 2025 il docente aggiunge un'osservazione: la formula negata è falsa perché nasce negando una formula vera, ma lo si vede anche direttamente. Se fosse vera per tutti gli x lo sarebbe anche per x = 0, e servirebbe un y con 0 · y ≥ 1, cioè 0 ≥ 1. Quindi x = 0 è un **controesempio** per la formula negata, ed è lo stesso valore che rendeva vera la formula di partenza. Le trasformazioni di De Morgan, fatte in modo meccanico come le farebbe una macchina, non cambiano il valore di verità.

Il motivo per togliere le negazioni è pratico, dice il docente: per noi è già difficile immaginare quando capita qualcosa, e ancora di più quando non capita.

## La negazione di un confronto
Una domanda di uno studente, nella registrazione 2025: perché negando «minore» compare anche l'uguale? Dati due numeri a e b i casi possibili sono tre: a < b, a = b, a > b. Negare a < b vuol dire prendere tutti i casi in cui è falso, cioè gli altri due, che insieme si scrivono **a ≥ b**. Il ragionamento è quello già visto per x > y nel cap. 27; applicato a tutti i confronti dà:

- ¬(a < b) è a ≥ b;
- ¬(a > b) è a ≤ b;
- ¬(a ≤ b) è a > b;
- ¬(a ≥ b) è a < b.

**Definizione.** Un'operazione è **involutiva** se, applicata due volte, riporta al punto di partenza.

(In parole povere: è come girare una chiave avanti e poi indietro. La negazione di un confronto lo è: la negazione di «minore» è «maggiore o uguale», e la negazione di questo torna a essere «minore». Il segno di uguale compare e scompare a ogni passaggio.)

Il docente nota che serve anche in programmazione, quando si deve scrivere il test opposto di quello che si è escluso.

## Quiz con x² + y²
**Esempio dalla lavagna (registrazione 2025).** Siano x e y numeri reali.

- **∀x ∀y (x² + y² = 9)** è falsa: con x = 100 si ha 10000 + y², che non può valere 9.
- **∀x ∃y (x² + y² = 9)** è falsa: per lo stesso x = 100 non esiste nessun y reale. Sarebbe vera nei complessi, perché y = √(9 − x²) lì esiste sempre.
- **∃x ∀y (x² + y² = 9)** è falsa: con y = 100 nessun x reale va bene.
- **∃x ∃y (x² + y² = 9)** è vera: per esempio x = 0, y = 3. I valori sono infiniti, tutti i punti della circonferenza di raggio 3 con centro nell'origine, ma ne bastava uno.
- **∀x ∀y (x² + y² ≥ 0)** è vera: i quadrati non sono mai negativi.
- **∀x ∃y (x² + y² ≥ 0)** è vera: è implicata dalla precedente.
- **∃x ∀y (x² + y² ≥ 0)** è vera per lo stesso motivo: qualunque x va bene.

(In parole povere: «= 9» chiede di colpire proprio un valore, «≥ 0» è gratis. Per questo la prima famiglia è quasi tutta falsa e la seconda tutta vera.)

## Quiz con x² < y + 1
**Esempio dalla lavagna (registrazione 2025).** Sempre su x e y reali.

- **∀x ∀y (x² < y + 1)** è falsa: con x = 10 e y = 0 si ottiene 100 < 1.
- **∀x ∃y (x² < y + 1)** è vera: basta y = x², perché x² < x² + 1.
- **∃x ∀y (x² < y + 1)** è falsa: con y = −1 si ha y + 1 = 0, e dovrebbe valere x² < 0. Il valore y = −1 è un controesempio qualunque sia x.
- **∃y ∀x (x² < y + 1)** è falsa: dato y si sceglie x uguale al massimo tra 1 e y + 1; allora x² ≥ x ≥ y + 1.
- **∀y ∃x (x² < y + 1)** è falsa, anche se sembrava più promettente: con y = −1 servirebbe di nuovo x² < 0.

Il docente sottolinea che già il controesempio y = −1 è un ragionamento: tutti i casi non si potrebbero controllare, perché sono infiniti. Aggiunge anche che, pur senza nulla di difficile, ogni volta che rivede questo quiz ci deve pensare.

## Il quiz della radice: ∀x ∃y (x = y²)
Scritta in simboli non si riconosce subito, ma la formula dice «ogni x ha una radice quadrata». **Esempio dalla lavagna (registrazione 2025).** La risposta dipende in modo essenziale dal dominio:

- sui **reali positivi** è vera: la radice esiste sempre;
- sui **reali** è falsa: −1 non ha radice reale;
- sui **complessi** è vera: la radice di −1 è i;
- sugli **interi** è falsa: 2 non ha radice intera;
- sui **razionali positivi** è falsa: √2 esiste, ma nessuna frazione la esprime esattamente; ci si può solo avvicinare quanto si vuole;
- sui **razionali** è falsa: qui anche −1 non ha radice.

La dimostrazione che √2 non è razionale si trova nel cap. 35. Sulla notazione, il docente precisa: un «+» in alto su un insieme di numeri, come in ℤ⁺ o ℚ⁺, indica di norma i soli valori positivi, senza lo zero; ma non tutti i libri rispettano questa convenzione.

## L'ordine dei quantificatori
Una domanda in aula, sempre nella registrazione 2025, porta sull'ordine. Sugli interi **∀x ∃y (y > x)** è vera: dato x basta il successore. **∃y ∀x (y > x)** è falsa: bisognerebbe scegliere y prima di sapere con quale x verrà confrontato, e x = y + 1 lo smentisce sempre; anzi basta x = y, perché y dovrebbe essere più grande di sé stesso.

**La regola del docente (registrazione 2025):** la scelta fatta dopo sfrutta i dati forniti prima; la scelta fatta prima deve andare bene qualunque siano le scelte fatte dopo.

(In parole povere: è il gioco del cap. 28. Se chi deve scegliere y vede già x, può adattarsi; se sceglie al buio, deve avere una risposta buona contro tutti.)

Lo stesso vale per x² < y + 1. Con «per ogni x c'è un y» si guarda quanto è grande x² e si sceglie y di conseguenza. Con «c'è un y per ogni x» si deve fissare y senza conoscere x: anche un miliardo non basta, se x è il doppio. Non c'è un y che vada bene per tutti gli x, anche se per ogni x c'è un y che va bene.

Lo scambio si può fare in due modi, e il docente li distingue: spostando i quantificatori con le loro variabili (da ∀x ∃y a ∃y ∀x) oppure lasciando le variabili in ordine e scambiando solo i simboli (da ∀x ∃y a ∃x ∀y). In entrambi i casi il significato cambia, ma in modo diverso. Nel secondo caso (y > x) si ottiene ∃x ∀y (y > x), falsa anche questa: con y = x diventa x > x. La sua conclusione è che il significato è molto fragile: basta cambiare un dettaglio e cambia tutto, tranne quando una legge come De Morgan garantisce il contrario.

## Una curiosità: le macchine e i ragionamenti
Nella registrazione 2025 il docente spiega perché il corso guarda esempi così semplici: serve a capire che difficoltà ha una macchina a stabilire la verità di un'affermazione con quantificatori, che su un dominio infinito non si può controllare caso per caso. Controllare che 7 sia primo richiederebbe in principio tutti i naturali; con un ragionamento semplice bastano i numeri minori di 7. Finché non si sa qualcosa di più sull'affermazione, un quantificatore chiede un lavoro infinito, e per ridurlo a un lavoro finito serve comunque un ragionamento.

Una macchina può fare ragionamenti rigorosi? Il problema, dice il docente, è che la rappresentazione esplicita è molto più grande di ciò di cui siamo consapevoli. Un'immagine di un milione di punti, a tre byte per punto, occupa 24 milioni di cifre binarie, e noi la riassumiamo in una frase. Per le prove logiche il rapporto è più basso: circa 45 anni fa una prova scritta a parole, spiegata a una macchina, diventava dieci o venti volte più lunga; l'ultima misura che il docente ricorda, di circa cinque anni fa, dà circa quattro volte. Le prove che interessano l'informatica, come la correttezza di un ciclo, sono piccole, e con quel fattore diventano quasi trattabili.

Esistono già programmi, i **proof assistant**, che aiutano a controllare prove di questo tipo (in parole povere: controllano che ogni passaggio di una prova sia valido). Provare un programma su milioni di esempi casuali è una selezione potente, ma alcuni errori capitano in situazioni che nessuno ha ancora immaginato: per coprire tutti i casi serve un ragionamento con i quantificatori.

Il capitolo seguente applica le stesse idee a un piccolo mondo di figure geometriche.
