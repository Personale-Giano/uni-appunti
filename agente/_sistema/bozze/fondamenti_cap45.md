# 45. Le Funzioni: Definizione, Funzioni Iniettive, Suriettive e Biiettive
## Un argomento nuovo, visto da informatici
Con la lezione 23 si chiude la parte sulle tecniche di dimostrazione e comincia il capitolo 3 del libro: **funzioni, sequenze e relazioni**. Sono concetti già incontrati nel corso di Matematica discreta (nei riassunti di quella materia, le funzioni sono nei cap. 10-20). Il docente lo dice apertamente: è in buona parte un ripasso, ma fatto «dal punto di vista dell'informatico». Interessano soprattutto le funzioni tra insiemi **finiti**, le domande a cui si può rispondere con un procedimento meccanico e l'uso di questi concetti nelle basi di dati; i termini del libro sono in inglese, quindi bisogna conoscere anche quelli (registrazione 2025).

La registrazione 2026 della lezione non è ancora disponibile: questo capitolo e i tre successivi seguono la registrazione 2025, dove lo stesso argomento occupa la lezione 24 e l'inizio della 25, e il §3.1-3.2 del libro. Nel 2025 il docente salta alcune parti del §3.1: l'algoritmo di Luhn per la cifra di controllo delle carte di credito (lasciato ai corsi di sicurezza), le funzioni hash (lasciate al corso di architettura), i numeri pseudocasuali, le parti intere per eccesso e per difetto e i grafici cartesiani (lasciati ad analisi). Qui sono omesse o appena citate.

## Relazioni e funzioni
Una **relazione** tra due insiemi X e Y dice quali elementi di X sono collegati a quali elementi di Y. La si rappresenta con un **diagramma a frecce**: si disegnano i due insiemi e si traccia una freccia da x a y ogni volta che x è in relazione con y. In termini di insiemi, una relazione è un insieme di coppie (x, y) con x ∈ X e y ∈ Y.

Perché una relazione sia una funzione servono due richieste, che il docente tiene distinte (registrazione 2025). La prima è che sia **ovunque definita** (in inglese ~everywhere defined~): da ogni elemento di X esce **almeno** una freccia. La seconda è che sia **funzionale**, o univoca: da ogni elemento di X esce **al più** una freccia. Messe insieme dicono che da ogni elemento di X esce **esattamente** una freccia.

**Definizione.** Siano X e Y due insiemi. Una **funzione** f da X a Y, scritta f: X → Y, è un insieme di coppie (x, y) con x ∈ X e y ∈ Y tale che per ogni x ∈ X esiste una e una sola y ∈ Y con (x, y) ∈ f. Quella y si indica con f(x). L'insieme X è il **dominio** di f, l'insieme Y il **codominio**; l'insieme dei valori assunti, {f(x) : x ∈ X}, è l'**immagine** di f (in inglese ~range~) ed è contenuto nel codominio.

(In parole povere: una funzione è una macchinetta che a ogni elemento di partenza assegna uno e un solo risultato. Il distributore di bibite è una funzione se ogni tasto fa uscire esattamente una bibita: un tasto che non dà niente, o che ne dà due, rompe la regola. Che due tasti diano la stessa bibita, invece, è permesso.)

![Quattro diagrammi a frecce da X a Y: (a) e (b) non sono funzioni, (c) e (d) sì.](figure/fond/funzioni_frecce.png|16)

Nella figura, la (a) non è una funzione da {1, 2, 3, 4} a {p, q, r}, perché dal 4 non esce nessuna freccia: manca la prima richiesta. Il docente la chiama a volte **funzione parziale**: se si toglie il 4 dal dominio, cioè si tengono solo gli elementi che hanno un'immagine, diventa una funzione. La (b) non è una funzione perché dal 2 escono due frecce: manca la seconda richiesta. La (c) invece va bene: da ogni elemento esce una sola freccia, anche se il punto r ne riceve due e il punto q nessuna. La definizione non chiede di usare tutti gli elementi di Y, e nemmeno che X e Y abbiano lo stesso numero di elementi.

Il docente fa anche un esempio dove a mancare è la seconda richiesta. Se a ogni numero reale x ≥ 0 si associano i numeri y con y² = x, a 1 corrispondono due valori, 1 e −1: non è una funzione. Lo diventa se si tiene solo la soluzione non negativa, cioè la radice quadrata come la si usa di solito.

Una conseguenza della definizione, sottolineata dal libro: una regola come f(x) = x² **da sola** non definisce una funzione, perché non dice quali sono il dominio e il codominio. Come si vedrà tra poco, cambiando il codominio una stessa regola può avere proprietà diverse. (Dal libro anche il test per i grafici: un insieme di punti del piano è il grafico di una funzione se ogni retta verticale lo incontra al più in un punto. Il docente lascia i grafici ai corsi di analisi.)

**Le domande di un informatico.** Nella lezione successiva della registrazione 2025 il docente spiega perché queste due richieste interessano a chi lavora con i dati. In una base di dati, la corrispondenza che a una persona associa «la casa di cui è proprietaria» non è una funzione: una persona può non averne nessuna, oppure averne diverse, per esempio per eredità. La corrispondenza che dai dati anagrafici ricava il codice fiscale è una funzione, perché c'è un algoritmo che lo calcola. Il viaggio inverso, dal codice fiscale alla persona, sembra univoco, ma il docente avverte che due omonimi nati nello stesso giorno e nello stesso luogo avrebbero lo stesso codice: casi rarissimi, di cui chi scrive il programma deve tenere conto. Le domande sono sempre le stesse: dato un dato in ingresso, quanti dati in uscita si ottengono, zero, uno o più? E un dato in uscita da quanti dati in ingresso può venire?

## Un esempio con il resto: che giorno sarà
Tra le funzioni più usate in informatica ci sono quelle costruite con il resto della divisione.

**Definizione.** Se x è un intero e y un intero positivo, **x mod y** è il resto della divisione di x per y, cioè l'unico intero r con 0 ≤ r < y tale che x − r è un multiplo di y.

(In parole povere: il numero x mod y è quello che avanza quando si fanno con x gruppi da y il più possibile. Con 17 caramelle e sacchetti da 5 si riempiono 3 sacchetti e ne avanzano 2: 17 mod 5 = 2.)

Per y fissato, x ↦ x mod y è una funzione dagli interi a {0, 1, …, y − 1}: ogni intero ha uno e un solo resto. Il docente la usa con un problema che, dice, gli capita ogni anno quando prepara la relazione sull'insegnamento: in che giorno della settimana cadrà la stessa data l'anno dopo? I giorni si ripetono ogni 7, e 365 = 7 · 52 + 1, cioè 365 mod 7 = 1: dopo un anno non bisestile la stessa data si sposta avanti di un giorno. Nell'esempio della registrazione il 13 novembre 2025 è un giovedì e il 13 novembre 2026 un venerdì. Un esempio nostro con lo stesso conto: il 20 novembre 2026 è un venerdì, quindi il 20 novembre 2027 sarà un sabato, perché nel 2027 febbraio ha 28 giorni. Se in mezzo c'è un 29 febbraio i giorni sono 366, e 366 mod 7 = 2: la data si sposta di due giorni.

## Funzioni iniettive
**Definizione.** Una funzione f: X → Y è **iniettiva** (in inglese ~one-to-one~ o ~injective~) se per ogni x₁, x₂ ∈ X, da f(x₁) = f(x₂) segue x₁ = x₂.

(In parole povere: elementi diversi vanno sempre in elementi diversi; nel diagramma, su nessun punto di Y arrivano due frecce. La matricola universitaria è una funzione iniettiva dagli studenti ai numeri: due studenti diversi non hanno mai la stessa matricola.)

Il docente precisa che «one-to-one» e «injective» sono **sinonimi perfetti**, non due concetti diversi: il libro li usa tutti e due (registrazione 2025). Per contrapposizione (cap. 36) la condizione si può leggere anche così: se x₁ ≠ x₂ allora f(x₁) ≠ f(x₂). Nella figura sopra, la funzione (c) non è iniettiva perché f(1) = f(3) = r.

Scritta con i quantificatori, l'iniettività è fatta di **due universali** uno dentro l'altro, come fa notare il docente rispondendo a una domanda (registrazione 2025):

∀x₁ ∈ X ∀x₂ ∈ X (f(x₁) = f(x₂) → x₁ = x₂).

Con le leggi di De Morgan per i quantificatori (cap. 22) e la negazione dell'implicazione si ottiene che cosa vuol dire **non** essere iniettiva: ∃x₁ ∈ X ∃x₂ ∈ X (f(x₁) = f(x₂) ∧ x₁ ≠ x₂). Questo dà anche il metodo per le due risposte possibili (dai suggerimenti del libro):
- per **dimostrare** che f è iniettiva si prendono x₁ e x₂ qualunque, si suppone f(x₁) = f(x₂) e si deduce x₁ = x₂;
- per **confutarlo** basta un controesempio (cap. 33): due elementi diversi con la stessa immagine.

**Esempio: una dimostrazione.** Sia f: ℤ → ℤ con f(n) = 3n + 2. Si suppone f(n₁) = f(n₂), cioè 3n₁ + 2 = 3n₂ + 2. Togliendo 2 da entrambe le parti si ottiene 3n₁ = 3n₂, e dividendo per 3 si ottiene n₁ = n₂. Quindi f è iniettiva.

**Esempio: un controesempio cercato con un algoritmo.** Sia f(n) = 2ⁿ − n², dagli interi positivi agli interi. Il docente sceglie questo esempio, preso dal libro, perché la risposta in sé è banale: interessa il **modo** di cercarla (registrazione 2025). Il metodo più semplice è calcolare f(1), f(2), f(3), … in ordine e confrontare ogni nuovo valore con tutti i precedenti, fermandosi alla prima ripetizione. I valori sono f(1) = 2 − 1 = 1, f(2) = 4 − 4 = 0, f(3) = 8 − 9 = −1, f(4) = 16 − 16 = 0: già con n = 4 si trova f(2) = f(4), quindi f non è iniettiva. Il docente avverte che questo è solo un **semi-algoritmo**: se la ripetizione esiste prima o poi la trova, ma se non esiste continua a calcolare per sempre senza poterlo dire. Se nel dominio ci fosse anche lo 0, la ripetizione arriverebbe subito: f(0) = 1 − 0 = 1 = f(1). L'uguaglianza 2⁴ = 4² = 16, osserva ancora il docente, riguarda l'unica coppia di interi positivi distinti per cui si possono scambiare base ed esponente.

## Funzioni suriettive
**Definizione.** Una funzione f: X → Y è **suriettiva** (in inglese ~onto~ o ~surjective~) se per ogni y ∈ Y esiste x ∈ X con f(x) = y, cioè se l'immagine di f coincide con il codominio.

(In parole povere: ogni elemento del codominio viene raggiunto; nel diagramma, su ogni punto di Y arriva almeno una freccia. Assegnare ogni studente a un turno di laboratorio è una funzione dagli studenti ai turni, ed è suriettiva se nessun turno resta vuoto.)

«Onto» significa «sopra»: la funzione copre tutto il codominio (registrazione 2025). Con i quantificatori la suriettività è un **universale seguito da un esistenziale**, con il «per ogni» all'esterno e l'«esiste» all'interno (registrazione 2025):

∀y ∈ Y ∃x ∈ X f(x) = y.

L'ordine dei quantificatori conta, come nel cap. 25: x può dipendere da y. La negazione è ∃y ∈ Y ∀x ∈ X f(x) ≠ y: c'è un elemento del codominio che non è immagine di niente. Per dimostrare la suriettività si prende un y qualunque e si **costruisce** un x adatto; per confutarla si trova un y che non viene mai raggiunto.

**Esempio: una funzione non suriettiva.** Sia f(n) = 2n − 1 dagli interi positivi agli interi positivi. I valori sono f(1) = 1, f(2) = 3, f(3) = 5, …: sono i dispari, e nessun pari viene mai raggiunto. Per esempio 2 = 2n − 1 darebbe n = 3/2, che non è un intero. Quindi f non è suriettiva (esempio del libro ripreso dal docente, registrazione 2025). È invece iniettiva, con lo stesso conto dell'esempio di 3n + 2.

**Esempio: una dimostrazione.** Sia g: ℝ → ℝ con g(x) = 5x − 3. Dato un y reale qualunque, si cerca x con 5x − 3 = y, e risolvendo si trova x = (y + 3)/5. È un numero reale, e g((y + 3)/5) = (y + 3) − 3 = y. Quindi g è suriettiva. L'x scelto dipende da y, come permette l'ordine ∀y ∃x.

**Il codominio conta.** La stessa regola 2n − 1, presa con codominio l'insieme dei dispari positivi invece di tutti gli interi positivi, è suriettiva: ogni dispari positivo m si ottiene da n = (m + 1)/2. Per questo il libro dice «suriettiva su Y» (~onto Y~): la suriettività non è una proprietà della sola formula.

## Funzioni biiettive
**Definizione.** Una funzione che è sia iniettiva sia suriettiva si chiama **biiettiva**, o **biiezione** (in inglese ~bijection~).

(In parole povere: ogni elemento di Y riceve esattamente una freccia, quindi gli elementi di X e di Y sono accoppiati a due a due senza che nessuno resti escluso. Come un teatro esaurito in cui ogni spettatore ha il suo posto e nessun posto è vuoto o doppio.)

Nella figura sopra la funzione (d) è biiettiva. Quando X = Y è un insieme finito, una biiezione da X in sé è una **permutazione**, il termine usato dal docente e nel corso di Matematica discreta (in quei riassunti, cap. 32). Una biiezione tra due insiemi finiti dice anche che hanno lo **stesso numero di elementi**: è come contarli mettendoli in corrispondenza uno a uno (dal libro).

## Il principio dei cassetti
Il docente aggiunge un'osservazione che nel §3.1 del libro non c'è (nel corso di Matematica discreta è nel cap. 25 di quei riassunti): un diagramma a frecce mostra subito che, se Y ha meno elementi di X, due frecce devono per forza finire nello stesso punto (registrazione 2025).

**Proposizione (principio dei cassetti).** Siano X e Y insiemi finiti con |Y| < |X|. Allora nessuna funzione f: X → Y è iniettiva: esistono x₁ ≠ x₂ con f(x₁) = f(x₂).

(In parole povere: se si mettono più oggetti che cassetti, almeno un cassetto ne riceve due. Con 13 persone e 12 mesi, almeno due persone compiono gli anni nello stesso mese.)

Il nome inglese è ~pigeonhole principle~, «principio delle caselle dei piccioni»: se ci sono più piccioni che caselle, almeno due piccioni devono dividersi la stessa casella. Leggendolo per contrapposizione: se f: X → Y è iniettiva e gli insiemi sono finiti, allora |X| ≤ |Y|.

Il docente insiste sul fatto che il viceversa non vale. Avere lo stesso numero di elementi non basta per essere iniettiva: la funzione (c) della figura va da 3 elementi a 3 elementi e non lo è. E per insiemi infiniti il conto degli elementi non funziona più come ci si aspetta: una funzione iniettiva da X a Y può lasciare fuori dei punti di Y. Per esempio (esempio nostro) n ↦ 2n dai naturali ai naturali è iniettiva e lascia fuori tutti i dispari.

## Esercizi svolti
Gli esercizi 17-22 del §3.1 del libro chiedono, per sei funzioni da ℤ a ℤ, se sono iniettive, suriettive o entrambe. Le soluzioni sono nostre e i valori sono ricontrollati al computer su un intervallo di interi.

- **f(n) = n + 1: biiettiva.** Iniettiva: da n₁ + 1 = n₂ + 1 segue n₁ = n₂. Suriettiva: dato m, si prende n = m − 1, che è un intero, e f(m − 1) = m.
- **f(n) = n² − 1: né iniettiva né suriettiva.** Non è iniettiva perché f(−1) = f(1) = 0. Non è suriettiva perché i valori sono tutti ≥ −1: per esempio −2 non viene mai raggiunto.
- **f(n) = |n|: né iniettiva né suriettiva.** f(−3) = f(3) = 3, e nessun intero negativo è un valore assoluto.
- **f(n) = 2n: iniettiva, non suriettiva.** Da 2n₁ = 2n₂ segue n₁ = n₂; i valori sono solo pari, quindi 1 non è raggiunto.
- **f(n) = n³: iniettiva, non suriettiva.** Se n₁ ≠ n₂, per esempio n₁ < n₂, allora n₁³ < n₂³, perché il cubo cresce strettamente; quindi f(n₁) ≠ f(n₂). Non è suriettiva perché 2 non è il cubo di nessun intero (1³ = 1 e 2³ = 8).
- **f(n) = ⌈n/2⌉: suriettiva, non iniettiva.** Il simbolo ⌈x⌉ indica il più piccolo intero maggiore o uguale a x (definito nel libro; il docente lo lascia ad analisi): per esempio ⌈1/2⌉ = 1 e ⌈−3/2⌉ = −1. Non è iniettiva perché f(1) = ⌈1/2⌉ = 1 e f(2) = ⌈2/2⌉ = 1. È suriettiva: dato m, si prende n = 2m e si ha f(2m) = ⌈m⌉ = m.

Il caso di n³ mostra ancora che la risposta dipende da dominio e codominio: da ℝ a ℝ la stessa regola sarebbe suriettiva, perché ogni numero reale ha una radice cubica reale.

## Riepilogo
- Una funzione f: X → Y associa a ogni elemento di X esattamente un elemento di Y: almeno uno (ovunque definita) e al più uno (funzionale). Nel diagramma, da ogni punto di X esce una sola freccia.
- Iniettiva: ∀x₁ ∀x₂ (f(x₁) = f(x₂) → x₁ = x₂); su ogni punto di Y arriva al più una freccia.
- Suriettiva: ∀y ∃x f(x) = y; su ogni punto di Y arriva almeno una freccia; dipende dal codominio scelto.
- Biiettiva: iniettiva e suriettiva; su ogni punto di Y arriva esattamente una freccia.
- Principio dei cassetti: tra insiemi finiti, se il codominio ha meno elementi del dominio la funzione non è iniettiva.
- Per dimostrare l'iniettività si parte da f(x₁) = f(x₂); per la suriettività si costruisce, per un y qualunque, una controimmagine (un x con f(x) = y); per confutarle basta un controesempio.

Nel prossimo capitolo il diagramma a frecce si rovescia e si concatena: la funzione inversa e la composizione.
