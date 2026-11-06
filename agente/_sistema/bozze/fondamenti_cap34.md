# 34. Esercizi Riassuntivi su Regole e Dimostrazioni Dirette
## La domanda aperta d'esame
Non avendo il quiz di quest'anno, gli esercizi che seguono sono quelli svolti nella registrazione 2025. Lì il docente comincia spiegando com'è fatta la parte scritta dell'esame. Quelle che seguono sono le regole dette nel 2025: i numeri sono da verificare per quest'anno.

- L'esame ha una prima parte di **quiz** con risposte da selezionare e una **domanda aperta**, a cui si risponde con un breve testo scritto.
- La domanda aperta è riservata a chi ha preso almeno **24 punti su 27** ai quiz, vale **da 0 a 6 punti** e non ha penalità. Con i soli quiz, dice il docente, si arriva al massimo a 27, e di fatto intorno a 24, perché è impossibile non sbagliare nulla.
- Il tempo è limitato, si parla di **30 minuti**, quindi bisogna scegliere le parti più importanti. La risposta standard mostrata dopo la consegna può essere più dettagliata della propria: non è un problema, purché ci si concentri sull'essenziale e non si scrivano affermazioni chiaramente false.
- Nei quiz le risposte sbagliate tolgono punti solo all'interno della stessa domanda, che non scende sotto zero.

Perché esiste? Saper scrivere un breve testo tecnico che giustifichi una scelta, spiega il docente, è essenziale per un informatico, e l'unico modo per imparare è farlo. Nota anche che è poco popolare: in un appello di giugno l'ha affrontata un solo studente su 96, di solito circa il 10%, e secondo lui è un errore non provarci. Le risposte alle domande di prova non vengono corrette automaticamente: chi vuole un parere può scrivergli.

**Come si imposta la risposta.** Si guarda prima che cosa va dimostrato:

- un **universale falso** si confuta con un controesempio, spiegando perché lo è;
- un **universale vero** richiede una dimostrazione, perché i casi sono troppi per controllarli;
- un **esistenziale vero** si dimostra esibendo un esempio.

## Tre esercizi sull'insieme delle parti
**Definizione.** L'**insieme delle parti** P(X) di un insieme X è l'insieme di tutti i sottoinsiemi di X, compresi l'insieme vuoto e X stesso.

(In parole povere: è l'elenco di tutte le selezioni possibili fatte dentro X. Se X = {1, 2}, allora P(X) contiene ∅, {1}, {2} e {1, 2}.)

**Esercizio 1 (registrazione 2025): P(X ∪ Y) non è incluso in P(X) ∪ P(Y).** L'inclusione è un universale, quindi basta un controesempio. L'idea: un sottoinsieme di X ∪ Y può stare un po' in X e un po' in Y, senza stare tutto in uno dei due. Si prendono X = {2}, Y = {3} e Z = {2, 3}. Allora Z ∈ P(X ∪ Y), perché Z ⊆ X ∪ Y. Ma Z non è incluso in X né in Y, quindi Z ∉ P(X) ∪ P(Y). Questa è già una risposta completa.

Il docente spiega anche il modo meccanico di arrivarci, riscrivendo l'enunciato un passo alla volta: l'inclusione diventa «per ogni Z, se Z ∈ P(X ∪ Y) allora Z ∈ P(X) ∪ P(Y)»; l'unione diventa un «oppure»; ogni P diventa un'inclusione; infine si nega l'implicazione, che è falsa quando l'ipotesi è vera e la tesi falsa, e con De Morgan la tesi falsa diventa «Z non è incluso in X e Z non è incluso in Y».

**Esercizio 2 (registrazione 2025): P(X) ∪ P(Y) ⊆ P(X ∪ Y).** L'inclusione opposta invece è vera, quindi serve una dimostrazione. Sia Z ∈ P(X) ∪ P(Y). Per definizione di unione, Z ∈ P(X) oppure Z ∈ P(Y); per definizione di insieme delle parti, Z ⊆ X oppure Z ⊆ Y. Serve un lemma: **X ⊆ X ∪ Y e Y ⊆ X ∪ Y**. Infatti se x ∈ X allora «x ∈ X oppure x ∈ Y» è vera, perché una disgiunzione è vera se lo è un lato, e lo stesso per Y. In entrambi i casi Z ⊆ X ∪ Y, cioè Z ∈ P(X ∪ Y).

Uno studente chiede se X = {2}, Y = {3}, Z = {2, 3} sia un controesempio anche qui. No: quello Z non sta in P(X) ∪ P(Y), quindi l'ipotesi è falsa e l'implicazione è vera per difetto (cap. 16). Il docente aggiunge che un insieme è molto più piccolo dell'altro: in generale, la maggior parte dei sottoinsiemi di X ∪ Y non è inclusa né in X né in Y.

**Esercizio 3 (registrazione 2025): P(X ∩ Y) = P(X) ∩ P(Y).** Qui vale l'uguaglianza, e si può dimostrare con una catena di equivalenze, per ogni insieme Z:

- Z ∈ P(X) ∩ P(Y) se e solo se Z ∈ P(X) e Z ∈ P(Y), per definizione di intersezione;
- se e solo se Z ⊆ X e Z ⊆ Y, per definizione di insieme delle parti;
- se e solo se Z ⊆ X ∩ Y, perché essere sottoinsieme di entrambi vuol dire restare nella parte comune;
- se e solo se Z ∈ P(X ∩ Y), per definizione di insieme delle parti.

**Trabocchetto (registrazione 2025).** Una catena dimostra un'uguaglianza solo se **tutti** i passaggi sono equivalenze. L'equivalenza, come l'uguaglianza, è transitiva e si può percorrere nei due sensi; con un'implicazione o con un ≤ in mezzo non si è sicuri di poter tornare indietro. In pratica, per gli insiemi: se nella catena c'è anche un solo passaggio in un senso solo, si è dimostrata al massimo un'inclusione.

La confusione tra l'unione, dove vale una sola inclusione, e l'intersezione, dove valgono entrambe, mostra, dice il docente, quanto sia facile sbagliare in un linguaggio astratto. Per le uguaglianze tra insiemi il metodo di solito è la doppia inclusione; le prove non sono uniche, e tra numeri si usa di più una catena di uguaglianze algebriche.

## Le regole proposizionali che servono
Tutti questi esercizi, e quelli del cap. 32, si riducono a poche regole, che il docente richiama via via:

- per dimostrare **p ∨ q** basta dimostrare un lato;
- da **p ∨ q** e ¬p si ricava q (sillogismo disgiuntivo, cap. 19);
- **p ∧ q** è falsa se è falso anche un solo lato; per dimostrarla servono entrambi;
- ¬(p ∧ q) ≡ ¬p ∨ ¬q e ¬(p ∨ q) ≡ ¬p ∧ ¬q (De Morgan, cap. 15 e 18);
- un'implicazione si dimostra supponendo l'ipotesi e ricavando la tesi;
- un'implicazione è falsa solo quando l'ipotesi è vera e la tesi è falsa (cap. 16).

## La differenza simmetrica (registrazione 2025)
Il titolo della lezione di quest'anno non cita questo argomento.

**Definizione.** La **differenza simmetrica** di A e B è A Δ B = (A − B) ∪ (B − A).

(In parole povere: sono gli elementi che stanno in uno solo dei due. Il docente la spiega con un test medico: se A sono le persone che il test dichiara malate e B quelle malate davvero, A − B sono i falsi positivi, B − A i falsi negativi, e A Δ B è l'elenco di tutti gli errori del test.)

Un elemento sta in A Δ B quando sta in esattamente uno dei due insiemi, quindi la differenza simmetrica è la controparte insiemistica dello **xor** (cap. 13). Non sta in A Δ B quando sta in zero o in due degli insiemi, cioè in un numero pari.

**Proposizione.** Per tutti gli insiemi A, B vale A Δ B = (A ∪ B) − (A ∩ B).

(In parole povere: si prende tutto e si tolgono gli elementi comuni.)

Si dimostra per doppia inclusione. **Da sinistra a destra:** se x ∈ A − B, allora x ∈ A, quindi x ∈ A ∪ B; e x ∉ B, quindi la congiunzione «x ∈ A e x ∈ B» è falsa. Il caso x ∈ B − A è uguale, scambiando i ruoli. **Da destra a sinistra:** sia x ∈ A ∪ B e x ∉ A ∩ B. Se x ∈ A, non può stare in B, altrimenti starebbe nell'intersezione: quindi x ∈ A − B. Se x ∈ B, nello stesso modo x ∈ B − A.

**Proposizione.** Un elemento x sta in (A Δ B) Δ C se e solo se appartiene a un numero dispari degli insiemi A, B, C, cioè a uno oppure a tre.

(In parole povere: è lo xor di tre proposizioni, che è vero quando le vere sono in numero dispari. Lo stesso vale con dieci, e il docente lo presenta solo come pretesto per un ragionamento proposizionale.)

Il docente svolge la direzione da sinistra a destra, con due casi:

- se x ∈ A Δ B e x ∉ C, allora x sta in esattamente uno tra A e B e non in C: in totale uno;
- se x ∈ C e x ∉ A Δ B, allora x sta in zero o in due tra A e B, più C: in totale uno o tre.

L'altra direzione non viene svolta in aula, ma segue dagli stessi conti: se x ∉ C e sta in un numero dispari degli insiemi, sta in esattamente uno tra A e B, quindi x ∈ A Δ B; se x ∈ C, sta in zero o in due tra A e B, quindi x ∉ A Δ B. In entrambi i casi x ∈ (A Δ B) Δ C.

**Il quiz dei valori.** Con A sottoinsieme di un universo U:

- A Δ A = ∅, perché A − A è vuoto;
- A Δ (U − A) = U, perché ogni elemento sta in esattamente uno dei due;
- A Δ U = U − A, perché A − U è vuoto;
- A Δ ∅ = A, perché togliere il vuoto non toglie nulla, e il vuoto meno A è vuoto.

**Come si calcola A Δ B Δ A.** La differenza simmetrica è commutativa, A Δ B = B Δ A, e associativa, (A Δ B) Δ C = A Δ (B Δ C). Il docente usa queste due proprietà senza dimostrarle. Si possono dunque spostare gli argomenti: A Δ B Δ A = (A Δ A) Δ B = ∅ Δ B = B. La regola generale è che gli argomenti uguali si cancellano a due a due.

**Insiemi disgiunti.** Se A ∩ B è vuoto, dalla formula (A ∪ B) − (A ∩ B) si ottiene A Δ B = A ∪ B. Vale anche il contrario, per assurdo: se A ∩ B contenesse un elemento, questo starebbe nell'unione ma non in A Δ B, quindi A Δ B e A ∪ B sarebbero diversi. È un primo ragionamento per assurdo, l'argomento del cap. 35.
