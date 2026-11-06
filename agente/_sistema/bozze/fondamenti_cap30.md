# 30. Il Mondo di Tarski
## Che cos'è
Il titolo della lezione di quest'anno non cita questo argomento. Tutto il capitolo viene dalla seconda ora della registrazione 2025, in cui il docente mostra dal vivo un programma dell'Università di Stanford per l'insegnamento della logica. Il programma è a pagamento e gli studenti non vi accedono; gli esempi, dice il docente, sono ricopiati nelle sue dispense. Il nome ricorda **Alfred Tarski**, logico del secolo scorso che ha studiato il valore di verità delle formule.

**Definizione.** Un **mondo di Tarski** è un dominio finito di oggetti costruito a piacere. Nel programma è una scacchiera 8 × 8 su cui si dispongono solidi geometrici: cubi, tetraedri (piramidi a base triangolare) e dodecaedri (12 facce), in tre formati, piccolo, medio e grande. Si scrivono poi formule che descrivono la scena, e il programma dice se sono vere o false.

(In parole povere: è un mondo giocattolo in cui una macchina controlla se una descrizione scritta con i quantificatori corrisponde davvero a quello che c'è sulla scacchiera.)

Il docente ammette che la domanda, così, non ha alcuna importanza, ma la considera il germe di un problema vero: mostrare una scena a una macchina, darle una descrizione e chiederle se è corretta. Il problema davvero difficile sarebbe far trovare alla macchina una descrizione significativa, e lì si è molto indietro. Qui la descrizione la diamo noi, e la macchina la controlla con la sola definizione dei quantificatori, cosa facile in un mondo finito e piccolo.

## Le formule
Le formule che seguono sono riportate a parole nella registrazione e qui scritte con predicati italiani, tenendo i nomi LeftOf e FrontOf che il docente legge dallo schermo:

- **Formula 1:** ∀x (Cubo(x) → ∃y (Tet(y) ∧ LeftOf(x, y)));
- **Formula 2:** ∀x (Cubo(x) → ∃y (Tet(y) ∧ LeftOf(x, y) ∧ FrontOf(x, y)));
- **Formula 3:** ∀x (Dod(x) → Grande(x));
- **Formula 4:** ∃x (Dod(x) ∧ Grande(x)).

**Definizione.** **LeftOf(x, y)** vuol dire che x sta in una colonna più vicina al bordo sinistro rispetto a y. **FrontOf(x, y)** vuol dire che x sta in una riga più vicina al bordo inferiore rispetto a y.

(In parole povere: LeftOf(x, y) dice che y è più a destra di x. FrontOf(x, y) dice che, guardando la scacchiera dal bordo inferiore, si incontra prima x e poi y: y è più indietro. Il docente stesso ammette che il nome «front of» non è chiarissimo.)

**La scacchiera dell'esempio (registrazione 2025).** Le posizioni sono ricostruite da ciò che il docente dice a voce, scritte come (colonna, riga) contando dal bordo sinistro e dal bordo inferiore. Due cubi: A in (2, 3) e B in (4, 2). Due piramidi: P₁ in (3, 4) e P₂ in (5, 3). Ci sono poi due dodecaedri, uno grande e uno piccolo.

## Formula 1: ogni cubo ha una piramide alla sua destra
Si legge «per ogni cubo c'è una piramide tale che il cubo stia alla sua sinistra». Si controllano tutti i cubi, perché la quantificazione esterna è universale. Il cubo A sta a sinistra di P₁; il cubo B no, perché P₁ è nella colonna 3 e lui nella 4, ma sta a sinistra di P₂. Quindi la formula è **vera**.

Attenzione a che cosa non dice: non chiede che ogni cubo stia a sinistra di tutte le piramidi, cosa falsa qui, e non chiede piramidi diverse per cubi diversi.

- **Togliendo P₁** la formula resta vera: P₂ va bene per entrambi i cubi. Vale anzi una proprietà più forte: esiste una piramide che sta a destra di tutti i cubi, scelta senza sapere quale cubo verrà preso.
- **Togliendo P₂** (e rimettendo P₁) la formula diventa **falsa**: B non ha più nessuna piramide alla sua destra.

## Formula 2: a destra e più indietro
La formula 2 chiede di più: per ogni cubo una piramide che stia sia a destra sia più indietro. Geometricamente, ogni cubo ha il suo rettangolo, fatto dalle colonne più a destra e dalle righe più lontane dal bordo inferiore, e lì deve cadere una piramide.

- **All'inizio è vera:** P₁ è nel rettangolo di A, P₂ in quello di B.
- **Togliendo P₁ diventa falsa,** mentre la formula 1 resta vera. P₂ è a destra di A ma sulla sua stessa riga, quindi A non è di fronte a P₂: il cubo A resta spaiato.
- **Spostando P₂** in un punto che cade nel rettangolo di entrambi, per esempio (5, 4), la formula torna **vera**. Rimettendola dov'era, torna falsa.

È, dice il docente, il problema dell'ora precedente: trovare un y che vada bene per tutti gli x a volte è possibile, a volte no (cap. 29).

La formula 2 è più forte della 1: una piramide a destra e più indietro è in particolare a destra. Quindi se la formula 1 è falsa, a maggior ragione lo è la 2. Il docente lo mostra su un'altra disposizione, in cui un cubo non ha piramidi a destra.

## Formule 3 e 4: i dodecaedri
La formula 3 dice che **tutti i dodecaedri sono grandi**, la formula 4 che **c'è un dodecaedro grande**. Nella scena di partenza la 3 è falsa, per colpa di quello piccolo, e la 4 è vera. Da qui il docente fa alcuni esperimenti.

- **Aggiungere un dodecaedro grande** non rende vera la formula 3: aumenta la percentuale dei grandi, ma la formula li chiede proprio tutti, e quello piccolo resta piccolo.
- **Togliere quello piccolo**, lasciando un solo dodecaedro, grande: le formule 3 e 4 sono entrambe vere. Con un solo oggetto ∀ ed ∃ dicono la stessa cosa: quell'unico oggetto ha la proprietà. Di solito il ∀ è una richiesta molto più forte dell'∃, ma con un oggetto solo coincidono.
- **Togliere anche l'ultimo:** la formula 4 è **falsa**, e la formula 3 è **vera**.

Le formule 1 e 2 non parlano di dodecaedri, quindi nessuno di questi cambiamenti le tocca.

## Il caso paradossale: nessun dodecaedro
Perché la formula 3 è vera se non ci sono dodecaedri? Conviene chiedersi che cosa vorrebbe dire che è falsa: dovrebbe esistere un dodecaedro non grande. Ma se non ci sono dodecaedri non ce n'è neanche uno che possa smentirla. È l'implicazione vera per difetto del cap. 16: per ogni oggetto x l'ipotesi Dod(x) è falsa, quindi l'implicazione è vera.

**Proposizione.** Una quantificazione universale su un insieme vuoto, qui quello dei dodecaedri, è sempre vera, una esistenziale è sempre falsa. Il dominio, cioè la scacchiera, resta non vuoto. In particolare, su un insieme vuoto il ∀ non implica l'∃.

(In parole povere: se in classe non c'è nessuno, «tutti i presenti hanno il libro» è vero, perché nessuno lo smentisce, mentre «c'è un presente con il libro» è falso. Nella vita di tutti i giorni diremmo che la prima frase non ha senso.)

Il docente insiste sul punto: nel nostro linguaggio diremmo che l'affermazione non ha senso, ma nella logica ogni affermazione ha un valore di verità, a volte banale. La definizione dei quantificatori è rigida e non si sovrappone alla perfezione con il nostro modo di parlare. È un caso estremo: già con due o più oggetti il rapporto si rovescia, e l'∃ torna a essere la richiesta più facile da soddisfare.

## L'implicazione vista in due modi
A chiusura, rispondendo a una domanda, il docente riprende le due riscritture dell'implicazione già viste nel cap. 18. **A → B** si può scrivere:

- come **negazione di una congiunzione**, ¬(A ∧ ¬B): non è vero che l'ipotesi è vera e la tesi è falsa, cioè si esclude l'unico caso che la smentisce;
- come **disgiunzione**, ¬A ∨ B: l'ipotesi è falsa oppure la tesi è vera, che copre i tre casi in cui è vera.

Si passa dall'una all'altra con De Morgan e la doppia negazione; scegliere quale usare, dice, è una questione di stile.

(In parole povere: «se A allora B» vuol dire «non può succedere che A sia vero e B falso».)

Con questo si chiude il capitolo 1 della seconda parte del corso; il prossimo passo sono le dimostrazioni.
