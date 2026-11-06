# 31. Sistemi Matematici e Dimostrazione Diretta
## Perché dimostrazioni così semplici
Comincia il secondo capitolo della seconda parte del corso: le dimostrazioni. Nella registrazione 2025 il docente spiega subito la differenza con i corsi di matematica. Lì le dimostrazioni servono perché il risultato è difficile e importante. Qui gli esempi sono volutamente semplici, a volte banali, perché interessa come è fatta una prova: attraverso quali tappe passa, come si può controllare o cercare in modo automatico. Lo scopo finale sono prove sui programmi, per esempio che un ciclo svolga davvero il suo compito. Per questo le prove di Fondamenti sono più lunghe di quelle viste altrove: mostrano dettagli che di solito si danno per scontati.

## Sistemi matematici
**Definizione.** Un **sistema matematico** è fatto di **assiomi**, affermazioni accettate come vere senza dimostrazione; di **definizioni**, che introducono concetti nuovi a partire da quelli già presenti; e di **termini non definiti**, privi di una definizione esplicita, il cui senso è fissato dagli assiomi.

(In parole povere: è come un gioco da tavolo. Gli assiomi sono le regole che non si discutono, le definizioni danno un nome alle situazioni, i termini non definiti sono i pezzi: nessuno spiega che cosa sia un pedone, si sa solo come si muove.)

Due esempi. Nella **geometria euclidea** punto e retta sono termini non definiti; un assioma dice che per due punti distinti passa esattamente una retta, e una definizione dice che due angoli sono supplementari se la loro somma è 180°. Nei **numeri reali** un assioma dice che xy = yx, e la moltiplicazione è un termine non definito. Un altro assioma dice che esiste un sottoinsieme P di ℝ chiuso per somma e prodotto, tale che per ogni reale x vale esattamente una tra x ∈ P, x = 0 e −x ∈ P: gli elementi di P si **definiscono** reali positivi. Sempre per definizione, |x| è x se x è positivo o nullo, altrimenti è −x.

**Definizione.** Un **teorema** è una proposizione di cui è stata dimostrata la verità. Un **lemma** è un teorema poco interessante di per sé, che serve a dimostrarne altri. Un **corollario** è un teorema che si ricava facilmente da un altro. Una **dimostrazione** è l'argomentazione che stabilisce la verità di un teorema.

(In parole povere: il teorema è il piatto principale, il lemma un ingrediente preparato prima, il corollario ciò che si ottiene quasi gratis alla fine. La dimostrazione è la ricetta che garantisce il risultato.)

Per esempio, sui reali sono teoremi x · 0 = 0 e la **transitività**: se x ≤ y e y ≤ z allora x ≤ z (servirà nel cap. 32). È un lemma che, se n è un intero positivo, n − 1 è un intero positivo oppure vale 0. In geometria, se in un triangolo due lati sono uguali lo sono anche gli angoli opposti; il corollario è che ogni triangolo equilatero è anche equiangolo.

## La dimostrazione diretta
**Definizione.** Una **dimostrazione diretta** di un enunciato della forma «per ogni x₁, …, xₙ, se p allora q» procede così: si prendono x₁, …, xₙ arbitrari, si suppone p vera e si deduce q usando assiomi, definizioni, teoremi già dimostrati e regole di inferenza.

(In parole povere: si parte dall'ipotesi e si cammina dritti verso la tesi, senza trucchi. Prendere elementi arbitrari vuol dire non scegliere un caso comodo: il ragionamento deve valere per tutti.)

Perché basta il caso in cui p è vera? Perché se p è falsa l'implicazione è vera per difetto (cap. 16), e non c'è niente da fare. Nella registrazione 2025 il docente la descrive come la prova di tipo più semplice: non usa tecniche particolari, si limita a combinare regole partendo dall'ipotesi per arrivare alla conclusione.

**Definizione.** Un intero n è **pari** se n = 2k per qualche intero k; è **dispari** se n = 2k + 1 per qualche intero k.

(In parole povere: pari vuol dire che si divide in due gruppi uguali, dispari che ne avanza uno. Dietro la definizione c'è un ∃: dire che 12 è pari vuol dire che un k adatto esiste, cioè k = 6, perché 12 = 2 · 6; e −21 è dispari con k = −11, perché −21 = 2(−11) + 1.)

## Un esempio per intero: dispari più pari
Si vuole dimostrare che, per tutti gli interi m e n, **se m è dispari e n è pari, allora m + n è dispari**. Il libro consiglia di scrivere per prima cosa ipotesi e conclusione, e poi di colmare il vuoto tra le due.

**Primo passo: gli esempi (registrazione 2025).** Il docente parte da qui: 7 + 10 = 17 è dispari, −1 + 12 = 11 è dispari. Esempi casuali, anche molti, convincono ma non dimostrano nulla. Immaginando che questa sia una delle migliaia di proprietà su cui si regge un programma, e che la si voglia far controllare a una macchina, serve qualcosa di più.

**Secondo passo: scrivere l'enunciato in logica (registrazione 2025).** Prima di dimostrare bisogna dargli un significato unico. «Pari» e «dispari» non sono ingredienti di base, si esprimono con un ∃:

∀m ∀n ( (∃k₁ (m = 2k₁ + 1) ∧ ∃k₂ (n = 2k₂)) → ∃k (m + n = 2k + 1) )

**Trabocchetto: le variabili locali (registrazione 2025).** Si potrebbe scrivere k per tutti e tre: la logica lo permette, perché ogni quantificatore riguarda solo la formula che lo segue. Ma quei k sono valori **diversi**, e il docente raccomanda nomi diversi per non confondersi. Il paragone che fa è con Programmazione: una variabile k locale a una funzione f e una k locale a una funzione g non hanno nulla a che vedere l'una con l'altra.

Attenzione invece a scrivere un solo esistenziale davanti a tutta la congiunzione, ∃k (m = 2k + 1 ∧ n = 2k). Qui k è lo stesso per entrambi, e la formula dice che m e n sono consecutivi, a distanza 1, come 21 e 20 con k = 10. È tutt'altra affermazione: −1 e 12 sono a distanza 13.

(In parole povere: due persone che hanno «un numero di telefono» non hanno necessariamente lo stesso. Se servono due valori che possono essere diversi, servono due nomi.)

**Terzo passo: la dimostrazione.** Si prendono m e n arbitrari, con m dispari e n pari.

1. Per definizione esistono due interi k₁ e k₂ con m = 2k₁ + 1 e n = 2k₂.
2. Si sommano le due uguaglianze: m + n = (2k₁ + 1) + 2k₂.
3. Riordinando e raccogliendo il 2, per le proprietà associativa, commutativa e distributiva: m + n = 2(k₁ + k₂) + 1.
4. Si pone k = k₁ + k₂, che è un intero. Allora m + n = 2k + 1, quindi m + n è dispari.

Con m = 15 e n = 4 si ha k₁ = 7 e k₂ = 2, che infatti sono diversi; la somma è 19 = 2 · 9 + 1, con k = 9. Con m = −1 e n = 12, l'esempio della lavagna, k₁ = −1, k₂ = 6 e k = 5: 11 = 2 · 5 + 1.

## Assumere un esiste e dimostrare un esiste
Il punto più istruttivo è che i tre ∃ non si trattano allo stesso modo, e il docente, nella registrazione 2025, lo fa notare.

- **Un ∃ nell'ipotesi si usa.** Sapere che esiste un k₁ vuol dire poter immaginare che qualcuno ce lo abbia dato: non sappiamo quanto vale, ma gli diamo un nome e andiamo avanti con la prova.
- **Un ∃ nella tesi si costruisce.** Il k di m + n dobbiamo trovarlo noi, con una formula a partire dai dati del problema. Qui è semplicemente la somma k₁ + k₂, ma non è sempre così facile.

(In parole povere: nell'ipotesi l'esiste è un regalo che ricevi a scatola chiusa; nella tesi è un compito che devi svolgere.)

Secondo il docente, nessun corso di matematica mostrerebbe questa prova a questo livello di dettaglio: è come passarla al microscopio. Quello da ricordare non è la formula della somma, ma il metodo.

L'errore di usare lo stesso simbolo per quantità diverse torna tra gli errori comuni del cap. 33. Nel cap. 32 si applica lo stesso metodo agli insiemi, dove compaiono anche le sottodimostrazioni.
