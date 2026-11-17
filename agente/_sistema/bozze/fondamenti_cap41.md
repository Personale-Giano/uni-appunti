# 41. La Forma Forte dell'Induzione
## Assumere tutti i casi precedenti
Nell'induzione del cap. 37, per provare il caso n + 1 si assume soltanto il caso immediatamente precedente, n. A volte questo non basta: per ottenere il caso n serve un caso più piccolo, ma non necessariamente quello subito prima. La sezione 2.5 del libro introduce per questo la **forma forte dell'induzione**, che permette di assumere **tutti** i casi precedenti. Per convenzione, nella forma forte il caso da provare si chiama n, non n + 1.

**Definizione.** Sia S(n) una funzione proposizionale il cui dominio sono gli interi maggiori o uguali a n₀. La **forma forte dell'induzione matematica** afferma che, se S(n₀) è vera e se, per ogni n > n₀, il fatto che S(k) sia vera per ogni k con n₀ ≤ k < n implica che S(n) è vera, allora S(n) è vera per ogni intero n ≥ n₀.

(In parole povere: per far cadere una tessera del domino si può contare non solo su quella subito prima, ma su tutte quelle già cadute. Per dimostrare il caso 10 si può usare il caso 9, ma anche il 7, il 5 o il 3, quello che fa comodo.)

Nella condizione n₀ ≤ k < n, la disuguaglianza k < n dice che k è un predecessore **qualsiasi** di n; la disuguaglianza n₀ ≤ k garantisce che k stia nel dominio {n₀, n₀ + 1, n₀ + 2, …}. Nella registrazione 2025 il docente la enuncia così: se una proprietà vale per n₀ e, tutte le volte che vale per n₀, n₀ + 1, …, n, vale anche per n + 1, allora vale per tutti gli interi maggiori o uguali a n₀. Le due forme dell'induzione sono logicamente equivalenti (il libro lo lascia per esercizio): la forma forte non dimostra niente di più, ma dà più materiale nel passo induttivo. Un'avvertenza pratica: se il passo usa il caso n − p, si devono provare a parte p casi iniziali, come nell'esempio 2.5.1 qui sotto.

## Esempio 2.5.1: i francobolli da 2 e da 5
**Proposizione.** Ogni affrancatura da 4 centesimi in su si può ottenere usando soltanto francobolli da 2 e da 5 centesimi.

(In parole povere: con due soli tipi di francobolli, da 2 e da 5, si compone qualunque cifra da 4 in su. Restano fuori solo 1 e 3: con 5 si va subito oltre, e con i 2 si fanno solo i pari.)

Il docente racconta l'esempio in euro, «un tempo si usavano i francobolli», e comincia dai casi piccoli (registrazione 2025): 4 = 2 + 2, 5 = 5, 6 = 2 + 2 + 2, 7 = 5 + 2, 8 = 2 + 2 + 2 + 2. Nota che sono tutte scomposizioni **isolate**: nessuna usa la precedente. Ed è il punto: partendo dalla scomposizione di n non sempre si arriva a quella di n + 1. Per esempio 12 = 6 francobolli da 2, e da lì non si arriva a 13 senza un francobollo da 1, che non c'è. Per 13 conviene invece partire da un caso più piccolo.

**L'idea del libro.** Per fare n centesimi basta saper fare n − 2 e aggiungere un francobollo da 2. Con la forma forte si può assumere il caso k = n − 2, ma solo se k sta nel dominio, cioè 4 ≤ n − 2: serve n ≥ 6. Il caso n = 5 non è coperto e va provato a parte.

**Dimostrazione.**

1. **Passi base (n = 4 e n = 5).** 4 = 2 + 2, cioè due francobolli da 2; 5 è un francobollo da 5.
2. **Passo induttivo.** Sia n ≥ 6 e si supponga che ogni affrancatura di k centesimi, con 4 ≤ k < n, si possa ottenere. Poiché 4 ≤ n − 2 < n, per ipotesi induttiva si sa fare n − 2; aggiungendo un francobollo da 2 si ottiene n.

**Più passi base.** In generale, se il passo induttivo usa il caso n − p, i casi n₀, n₀ + 1, …, n₀ + p − 1 non hanno un predecessore a distanza p nel dominio e diventano tutti passi base: sono p. Qui p = 2 e i passi base sono 4 e 5.

**La strada del docente (registrazione 2025).** A lezione la prima idea che viene è un'altra: togliere un francobollo da 5. Per n ≥ 9 si ha n − 5 ≥ 4, un caso già trattato, e basta aggiungere un 5. Per esempio 9 = 5 + 4 = 5 + 2 + 2; 12 = 5 + 7 = 5 + 5 + 2. Funziona, ma per n da 4 a 8 il caso n − 5 sarebbe sotto 4, fuori dal dominio: questi cinque valori sono quindi casi base, da provare uno per uno. È la regola dei p passi base con p = 5.

**Una formula diretta.** Ragionando sui casi, a lezione si arriva anche a una regola che non ha bisogno dell'induzione: se n è pari si usano n/2 francobolli da 2; se n è dispari (e n ≥ 5) si usa un francobollo da 5 e (n − 5)/2 da 2, perché n − 5 è pari. Per esempio 23 = 5 + 9 · 2. Il docente osserva che è una formula **per casi**, che un informatico scrive con un `if`, senza bisogno di un ciclo. Spesso, commenta, l'induzione è il modo in cui si comincia a ragionare su un problema; poi si scoprono soluzioni più dirette.

**Il minimo numero di francobolli (registrazione 2025, lezione successiva).** La formula diretta non è la più economica: per 25 dà un 5 e dieci 2, cioè 11 francobolli, mentre ne bastano 5 da 5. Per usarne il meno possibile conviene usare più 5 che si può: si divide n per 5, n = 5q + r con 0 ≤ r ≤ 4. Se r è pari si usano q francobolli da 5 e r/2 da 2; se r è dispari (1 o 3) se ne usa uno in meno da 5, cioè q − 1, e (r + 5)/2 da 2. Per esempio 72 = 14 · 5 + 2 · 1, 71 = 13 · 5 + 2 · 3, 73 = 13 · 5 + 2 · 4. Il caso q = 0 con r dispari non si presenta, perché sarebbe n = 1 o n = 3.

## Esempio 2.5.4: quante moltiplicazioni per un prodotto
Per calcolare il prodotto a₁a₂···aₙ bisogna mettere delle parentesi, esplicite o implicite, che dicono in che ordine fare le moltiplicazioni. Per n = 4, per esempio, (a₁a₂)(a₃a₄) calcola a₁a₂ e a₃a₄ e poi il loro prodotto: 3 moltiplicazioni. Ma si potrebbe anche fare ((a₁a₂)a₃)a₄, oppure a₁(a₂(a₃a₄)), e altre ancora: con quattro fattori i modi sono cinque, e crescono rapidamente con n.

**Perché interessa (registrazione 2025).** Il docente lo presenta come un problema di chi scrive un compilatore: se un'espressione contiene molti prodotti, riorganizzando le parentesi (lo permette la proprietà associativa) si risparmia qualcosa? La risposta è no, ed è un risultato **negativo**: l'unica utilità è smettere di cercare un'ottimizzazione che non esiste. Diverso è il caso dei fattori tutti uguali, cioè delle potenze, dove riutilizzare i risultati fa risparmiare moltissimo (cap. 40).

**Proposizione.** Comunque si mettano le parentesi nel prodotto a₁a₂···aₙ, per calcolarlo servono esattamente n − 1 moltiplicazioni.

(In parole povere: il numero di moltiplicazioni è sempre il numero di fattori meno uno, in qualunque ordine le si faccia. Con 10 fattori ne servono 9, punto.)

**Dimostrazione.** Per induzione forte su n, con n₀ = 1.

1. **Passo base (n = 1).** Il «prodotto» del solo a₁ richiede 0 moltiplicazioni, e 0 = 1 − 1.
2. **Passo induttivo.** Sia n > 1 e si supponga che, per ogni k con 1 ≤ k < n, un prodotto di k fattori richieda k − 1 moltiplicazioni comunque si mettano le parentesi. Si guarda l'**ultima** moltiplicazione eseguita: ha la forma (a₁···a_{t})(a_{t+1}···aₙ) per qualche t con 1 ≤ t < n. Il primo gruppo ha t fattori, il secondo n − t, ed entrambi i numeri sono compresi tra 1 e n − 1. Per ipotesi induttiva il primo gruppo richiede t − 1 moltiplicazioni e il secondo n − t − 1, qualunque siano le parentesi al loro interno. Contando anche l'ultima, il totale è
   (t − 1) + (n − t − 1) + 1 = n − 1.

Nella (a₁a₂)(a₃a₄) l'ultima moltiplicazione ha t = 2: 1 + 1 + 1 = 3.

**Perché serve la forma forte.** Non si sa in anticipo dove cada la divisione: con n = 10 i due gruppi possono essere 3 e 7, oppure 5 e 5, 6 e 4, 1 e 9. Serve quindi l'ipotesi per **tutti** i valori da 1 a 9, non solo per 9 (registrazione 2025). A lezione il docente, sommando (m − 1) + (n − m − 1), ottiene prima n − 2 e si chiede dove sia finita una moltiplicazione: manca proprio quella che unisce i due gruppi.

## Il principio del buon ordinamento
**Definizione.** La **proprietà del buon ordinamento** degli interi non negativi afferma che ogni insieme **non vuoto** di interi non negativi ha un elemento minimo.

(In parole povere: in un gruppo di numeri naturali, anche infinito, ce n'è sempre uno più piccolo di tutti. Tra i pari maggiori di 7 il minimo è 8. Con i negativi non funziona: tra gli interi negativi non c'è un minimo, perché sotto −1000 c'è −1001.)

Il libro la dichiara equivalente alle due forme dell'induzione. Nella registrazione 2025 il docente aggiunge alcune precisazioni:

- il punto di partenza si può spostare: ogni insieme non vuoto di interi maggiori o uguali a −3 ha un minimo, mentre senza un limite inferiore il minimo può mancare;
- di solito la si usa nelle prove per assurdo: per provare una proprietà su tutti i naturali si suppone che sia falsa per qualcuno, si prende il **più piccolo** numero per cui è falsa e si mostra che ce ne sarebbe uno ancora più piccolo, una contraddizione;
- il difetto di queste prove è che non dicono perché la proprietà vale né come trovare l'oggetto di cui si parla: sapere che una cosa «non può non esistere» non è come avere un programma che la trova.

Un quiz di ripasso su Moodle chiede la formulazione corretta e completa di questo principio, che nel quiz si chiama **principio del minimo**: «ogni sottoinsieme non vuoto A di ℕ contiene un x tale che nessun y < x appartiene ad A». Le risposte sbagliate del quiz mostrano i punti da non dimenticare: senza «non vuoto» l'enunciato è falso, perché l'insieme vuoto non ha minimo; limitarsi agli insiemi **finiti** è troppo poco, perché il principio interessa proprio per quelli infiniti.

## Che cosa resta fuori
Della sezione 2.5 non fanno parte della lezione gli esempi 2.5.2 e 2.5.3 (successioni definite da c_{⌊n/2⌋}) e la dimostrazione del teorema del quoziente e del resto: nella registrazione 2025 il docente lo salta perché è già stato visto a Matematica discreta. La lezione si chiude con un esercizio sui triomini, nel cap. 42.
