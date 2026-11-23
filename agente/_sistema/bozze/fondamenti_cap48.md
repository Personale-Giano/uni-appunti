# 48. Le Stringhe: Lunghezza, Concatenazione e Sottostringhe
## Sequenze di lettere
Un corso di matematica, osserva il docente, considera le sequenze di lettere un caso particolare senza grande interesse; per un informatico sono invece fondamentali, perché i testi si rappresentano così, come si è già visto a Programmazione (registrazione 2025). Le parole su un alfabeto sono già comparse come anagrammi (Matematica discreta, cap. 23 di quei riassunti): qui si ripassano con i termini del libro, che sono in inglese.

**Definizione.** Sia X un insieme finito, detto **alfabeto**. Una **stringa** su X è una sequenza finita di elementi di X.

(In parole povere: una stringa è una parola scritta con le lettere di un alfabeto fissato, dove contano sia le lettere sia il loro ordine. Su {a, …, z} «roma» e «mora» usano le stesse lettere ma sono stringhe diverse.)

Gli alfabeti tipici sono le lettere dell'alfabeto inglese, per semplicità, oppure l'insieme dei caratteri ASCII, che è quello che il docente ha in mente di solito; le stringhe sull'alfabeto {0, 1} sono le **stringhe di bit**, con cui un computer rappresenta dati e istruzioni. Come ogni sequenza, una stringa è una funzione dall'insieme dei suoi indici alle lettere dell'alfabeto: per esempio la stringa baac sull'alfabeto {a, b, c} ha x₁ = b, x₂ = a, x₃ = a, x₄ = c. Per scriverla di solito si mettono semplicemente le lettere in fila.

Da dove partono gli indici? Il docente fa notare che il libro dice solo «sequenza finita» e non sceglie: una stringa di n caratteri si può numerare da 0 a n − 1, come in C, oppure da 1 a n, come in altri linguaggi, o perfino da 100 in poi. La stringa è sempre la stessa, perché si passa da una numerazione all'altra spostando gli indici; ma una numerazione va scelta e poi rispettata (registrazione 2025). Negli esempi qui sotto si parte da 1, come nel libro.

## La stringa vuota e l'insieme di tutte le stringhe
**Definizione.** La **stringa vuota** (o nulla) è la stringa senza elementi: come sequenza ha per dominio l'insieme vuoto. Il libro la indica con **λ**. Se X è un alfabeto, **X\*** è l'insieme di tutte le stringhe su X, compresa λ, e **X⁺** è l'insieme delle stringhe non vuote.

(In parole povere: la stringa λ è quella che si ottiene non scrivendo niente, come una casella di testo vuota in un modulo. X\* è il «vocabolario» di tutte le parole possibili con quell'alfabeto, anche quelle senza senso, più la parola vuota.)

Il docente descrive X\* per lunghezze: c'è la stringa vuota, poi tutte le stringhe di lunghezza 1, che sono le lettere dell'alfabeto, poi tutte quelle di lunghezza 2, cioè tutte le coppie di lettere, anche ripetute (su ASCII, anche una parentesi graffa aperta seguita da una chiusa è una stringa di lunghezza 2), poi quelle di lunghezza 3 e così via senza fine. Per questo **X\* è infinito anche se l'alfabeto è finito**, purché abbia almeno una lettera: ci sono stringhe di ogni lunghezza (registrazione 2025). Ogni singolo strato invece è finito. Con l'alfabeto {0, 1} le stringhe di lunghezza al più 3 sono 1 + 2 + 4 + 8 = 15; con 26 lettere le stringhe di lunghezza 2 sono 26 · 26 = 676.

## Lunghezza e «potenze»
**Definizione.** La **lunghezza** di una stringa α, indicata con |α|, è il numero dei suoi elementi.

(In parole povere: la lunghezza |α| è il numero di caratteri, quello che conta un contatore di caratteri. |roma| = 4.)

La stringa vuota ha lunghezza 0, perché il suo insieme di indici è vuoto (registrazione 2025).

Le ripetizioni si abbreviano con un esponente: bbaaac si scrive b²a³c. Il docente mette in guardia da una possibile confusione: qui l'esponente **non** è una potenza numerica. b²⁰ non è «il valore di b elevato alla 20», perché le lettere non hanno un valore; è solo la lettera b scritta venti volte. La notazione è presa in prestito dalle potenze perché ripetere una lettera somiglia a ripetere un fattore, ma si usa solo in informatica (registrazione 2025). Per esempio |b²⁰a⁵ba| = 20 + 5 + 1 + 1 = 27, il conto fatto in aula; allo stesso modo |c²a¹⁰b| = 2 + 10 + 1 = 13.

## Concatenazione e rovesciamento
**Definizione.** La **concatenazione** di due stringhe α e β, scritta αβ, è la stringa formata da α seguita da β.

(In parole povere: si incollano due parole una dopo l'altra. Concatenando «porta» e «chiavi» si ottiene «portachiavi».)

Il docente sottolinea che la concatenazione non inserisce nessuno spazio in mezzo: se serve uno spazio, è un carattere che va concatenato esplicitamente (registrazione 2025). Alcune proprietà, che seguono subito dalla definizione:
- la stringa vuota non cambia niente: αλ = λα = α;
- la lunghezza si somma: |αβ| = |α| + |β|;
- l'ordine conta: con α = ro e β = ma si ha αβ = roma ma βα = maro.

Il libro osserva che la concatenazione è un **operatore binario** su X\* nel senso del cap. 46: prende due stringhe e restituisce una stringa.

**Definizione.** La **rovesciata** (o inversa) di una stringa α, indicata dal libro con α^{R}, è la stringa che si ottiene leggendo α da destra a sinistra.

(In parole povere: è la parola letta allo specchio. La rovesciata di abbc è cbba, quella di «roma» è «amor».)

Rovesciare due volte riporta alla stringa di partenza: (α^{R})^{R} = α. È il fatto su cui si regge il primo esercizio qui sotto. Le stringhe che non cambiano rovesciandole, cioè quelle con α = α^{R} come «radar», si chiamano palindromi (dagli esercizi del libro).

## Sottostringhe e sottosequenze
**Definizione.** Una stringa β è una **sottostringa** di una stringa α se esistono due stringhe γ e δ (eventualmente vuote) tali che α = γβδ.

(In parole povere: una sottostringa è un pezzo **contiguo** di α, una parola che compare dentro un testo. γ è quello che sta prima del pezzo, δ quello che sta dopo.)

**Esempio.** In α = banana, la stringa nan è una sottostringa: basta prendere γ = ba e δ = a. Invece bnn non è una sottostringa, perché in banana le lettere b, n, n non sono mai una di seguito all'altra; è però una **sottosequenza** nel senso del cap. 47, ottenuta tenendo la prima, la terza e la quinta lettera.

È la distinzione annunciata nel capitolo precedente. Il docente ripete che la terminologia non è la stessa in tutti i libri, e anche lui ne usa abitualmente una diversa; nel corso si segue il libro (registrazione 2025):
- in una **sottosequenza** si possono buttare via degli elementi anche in mezzo, a costo di avere indici non più consecutivi;
- in una **sottostringa** si tengono indici consecutivi: è un testo più breve che compare dentro un testo più lungo.

Il motivo per cui le sottostringhe interessano, dice il docente, è che servono a formulare problemi concreti, per esempio contare quante volte una parola compare in un testo: per farlo bisogna aver capito che cosa vuol dire che una parola «compare», cioè che le sue lettere si trovano consecutive. Nell'esempio della registrazione una parola di un testo del libro occupa gli indici da 9 a 18 del testo, e quell'intervallo di indici consecutivi è la sottostringa.

**Esercizio (libro, esercizio 147; soluzione nostra).** Le sottostringhe di babc sono: λ (con γ = λ e δ = babc, per esempio), le lettere a, b, c, poi ba, ab, bc, poi bab, abc e infine babc stessa. Sono 10 in tutto. La b compare due volte in babc, ma come sottostringa si conta una volta sola, perché è la stessa stringa.

## Esercizio: il rovesciamento è una biiezione
Il docente svolge in aula questo esempio del libro, avvertendo che la proprietà non è importante in sé: è un pretesto per ripassare insieme i concetti di stringa, di rovesciata e di biiezione (registrazione 2025). Sia X un alfabeto e sia f: X\* → X\* la funzione f(α) = α^{R}. Si vuole dimostrare che f è una biiezione.

**f è una funzione.** Per ogni stringa c'è esattamente una rovesciata: quella che si ottiene leggendola da destra a sinistra.

**f è iniettiva.** Si prendono due stringhe α e β e si suppone che abbiano la stessa immagine, cioè α^{R} = β^{R}. Bisogna dedurre α = β. L'idea, suggerita in aula da uno studente, è applicare f a entrambi i membri: dall'uguaglianza si ottiene (α^{R})^{R} = (β^{R})^{R}, e poiché rovesciare due volte riporta al punto di partenza, α = β.

**f è suriettiva.** Si prende una stringa β qualunque e bisogna trovare α con f(α) = β, cioè α^{R} = β. Qui il docente si sofferma su che cosa vuol dire dimostrare un esistenziale (registrazione 2025): α **lo si sceglie**, ed è una scelta libera, ma poi bisogna pagare il prezzo e dimostrare che la scelta soddisfa l'obiettivo; se non lo soddisfa, il tentativo è fallito. Non si può invece usare l'obiettivo α^{R} = β per ricavare α: è la tesi, e non la si può usare nella prova. Tutto quello che si ha a disposizione sono β e la funzione f, e il tentativo più naturale è applicare f a β: si sceglie α = β^{R}. Il controllo riesce: f(α) = (β^{R})^{R} = β. Quindi ogni β ha una controimmagine, e f è suriettiva.

Il docente aggiunge due osservazioni. La controimmagine trovata è l'unica, ma lo si sa solo ora, dopo aver dimostrato l'iniettività. E una funzione che applicata due volte riporta al punto di partenza, cioè con f(f(α)) = α per ogni α, si chiama **involuzione**: nel linguaggio del cap. 46, f è l'inversa di se stessa.

## Esercizio: la concatenazione è suriettiva ma non iniettiva
Anche questo esempio del libro è svolto in aula come ripasso delle definizioni: una volta posta bene la domanda, dice il docente, la risposta è immediata (registrazione 2025). Sia f: X\* × X\* → X\* la funzione che a una coppia di stringhe associa la loro concatenazione, f(α, β) = αβ.

**f è suriettiva.** Data una stringa γ qualunque bisogna trovare una coppia (α, β) con αβ = γ. Di coppie adatte ce ne sono molte: una stringa di 10 caratteri si può spezzare in 11 modi, prendendo davanti 0, 1, …, 10 caratteri. Ma bisogna scegliere una coppia che vada bene per **ogni** γ, anche per la stringa vuota, che non ha un primo carattere da staccare. La scelta che funziona sempre è (γ, λ): f(γ, λ) = γλ = γ.

**f non è iniettiva.** Qui il docente segnala una difficoltà nel formulare la domanda: gli elementi del dominio sono **coppie** di stringhe, quindi l'iniettività chiede che da f(α, β) = f(α′, β′) segua (α, β) = (α′, β′), cioè α = α′ e β = β′. Non è così: lo stesso testo si può spezzare in due punti diversi. Per esempio f(a, b) = ab = f(ab, λ), ma le coppie (a, b) e (ab, λ) sono diverse. Basta questo controesempio per concludere.

**Una domanda dagli studenti.** Alla fine dell'esercizio, nella registrazione 2025, uno studente chiede come si scrivono le due proprietà con i quantificatori. Il docente risponde che l'iniettività è fatta di due universali uno dentro l'altro, mentre la suriettività è un universale con dentro un esistenziale, come nel cap. 45. È l'esistenziale della suriettività che, nelle dimostrazioni, obbliga a scegliere un testimone: β^{R} per il rovesciamento, (γ, λ) per la concatenazione.

## Altri due esercizi del libro
Gli esercizi 155 e 156 del §3.2 usano le stesse idee; le soluzioni sono nostre, controllate al computer su tutte le stringhe su {a, b} fino alla lunghezza 5. In entrambi X = {a, b}.

- **f(α) = αab è iniettiva ma non suriettiva.** Iniettiva: se αab = βab, le due stringhe hanno la stessa lunghezza, quindi |α| = |β|, e togliendo gli ultimi due caratteri resta α = β. Non suriettiva: ogni immagine finisce con ab ed è lunga almeno 2, quindi λ, a, ba non sono immagini di niente.
- **g(α) = αα è iniettiva ma non suriettiva.** Iniettiva: se αα = ββ, allora 2|α| = 2|β|, quindi |α| = |β|; le prime metà delle due stringhe uguali sono uguali, cioè α = β. Non suriettiva: le immagini hanno tutte lunghezza pari, quindi a non è raggiunta; e nemmeno ab, che pure ha lunghezza pari, perché le sue due metà sono diverse.

## Riepilogo
- Una stringa su un alfabeto finito X è una sequenza finita di elementi di X; l'ordine conta. La numerazione degli indici (da 0 o da 1) va scelta e rispettata.
- λ è la stringa vuota, di lunghezza 0; X\* è l'insieme di tutte le stringhe compresa λ, ed è infinito se X non è vuoto; X⁺ esclude λ.
- |α| è il numero di caratteri; b²⁰ indica la lettera b ripetuta venti volte, non una potenza numerica.
- La concatenazione αβ incolla le due stringhe senza spazi; λ è neutra, le lunghezze si sommano, l'ordine conta.
- Sottostringa: pezzo contiguo, α = γβδ. Sottosequenza: alcuni elementi tenuti nello stesso ordine, anche non contigui.
- Il rovesciamento α ↦ α^{R} è una biiezione (ed è l'inversa di se stesso); la concatenazione da X\* × X\* a X\* è suriettiva ma non iniettiva.
- Per dimostrare la suriettività si sceglie un testimone e poi si verifica che funziona: la scelta è libera, la verifica è obbligatoria.

Nella registrazione 2025 la lezione successiva prosegue con le proprietà delle relazioni (§3.3 del libro): riflessiva, simmetrica, antisimmetrica, transitiva.
