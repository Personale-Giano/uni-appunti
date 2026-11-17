# 37. Il Principio di Induzione Matematica
## Perché rivederla a Fondamenti
Con la lezione 19 comincia la seconda metà del corso e la sezione 2.4 del libro: l'**induzione matematica**, un metodo di prova che si incontra già a Matematica discreta. Nella registrazione 2025 il docente spiega perché la si riprende qui. Gli enunciati che interessano a un informatico (somme, conteggi, proprietà dei cicli) sono quasi sempre provabili per induzione; inoltre esiste un uso tutto informatico, l'**invariante di un ciclo** (cap. 39), che a un corso di matematica interessa poco, mentre è specifico dell'informatica: serve a garantire che un programma calcoli davvero quello che deve. Secondo lui la maggior parte delle prove matematiche contiene un'induzione nascosta che non viene dichiarata: qui la si usa in modo esplicito e consapevole.

## L'idea: i blocchi sul tavolo
Il libro parte da un'immagine. Su un tavolo infinitamente lungo ci sono dei blocchi numerati 1, 2, 3, … e si sa che:

- il primo blocco è marcato con una X;
- per ogni n, se il blocco n è marcato, allora è marcato anche il blocco n + 1.

Allora tutti i blocchi sono marcati. Il blocco 1 lo è per la prima condizione; il blocco 2 perché il blocco 1 lo è (seconda condizione con n = 1); il blocco 3 perché lo è il 2 (n = 2), e così via. Anche un blocco non disegnato, come il 6, è marcato: basta sapere che lo è il 5 e usare n = 5. Il docente la descrive come un'etichetta che si propaga partendo dal primo blocco con tanti salti di lunghezza uno (registrazione 2025).

## Il primo esempio: la somma dei primi n interi
Sia Sₙ = 1 + 2 + … + n la somma dei primi n interi positivi. La formula Sₙ = n(n + 1)/2, per n ≥ 1, è in realtà una fila infinita di uguaglianze: S₁ = 1 · 2/2 = 1, S₂ = 2 · 3/2 = 3, S₃ = 3 · 4/2 = 6, e così via. Per esempio la somma dei numeri da 1 a 10 è 10 · 11/2 = 55. Ogni uguaglianza è un «blocco», e si vuole mostrare che sono tutte vere.

- **Il primo blocco.** S₁ = 1 e 1 · 2/2 = 1.
- **Il passaggio da un blocco al successivo.** Si suppone vera l'uguaglianza n, cioè Sₙ = n(n + 1)/2, e si dimostra la n + 1, cioè Sₙ₊₁ = (n + 1)(n + 2)/2.

Il trucco è collegare l'enunciato n all'enunciato n + 1: Sₙ è contenuta in Sₙ₊₁, nel senso che Sₙ₊₁ = 1 + 2 + … + n + (n + 1) = Sₙ + (n + 1). Allora

Sₙ₊₁ = Sₙ + (n + 1) = n(n + 1)/2 + 2(n + 1)/2 = (n + 1)(n + 2)/2.

A lezione il docente la richiama soltanto, perché è l'esempio che di solito si fa per primo a Matematica discreta e il libro lo svolge per intero (registrazione 2025).

## Il principio di induzione
**Definizione.** Sia S(n) una funzione proposizionale il cui dominio sono gli interi positivi. Il **principio di induzione matematica** afferma che, se S(1) è vera (**passo base**) e se, per ogni n ≥ 1, S(n) vera implica S(n + 1) vera (**passo induttivo**), allora S(n) è vera per ogni intero positivo n. Nel passo induttivo l'ipotesi S(n) si chiama **ipotesi induttiva**.

(In parole povere: è una fila di domino. Se cade il primo, e ogni tessera che cade fa cadere la successiva, cadono tutte. Il passo base fa cadere il primo; il passo induttivo garantisce che ogni tessera trascina quella dopo.)

Nel passo induttivo non si sa che S(n) è vera: lo si **suppone** per un n qualsiasi e si **dimostra** S(n + 1). Scritto in logica (cap. 21), il passo induttivo è un unico enunciato universale, ∀n ≥ 1 (S(n) → S(n + 1)), e la conclusione è ∀n ≥ 1 S(n). Il termine «ipotesi induttiva» lo usa anche il docente, che a lezione indica sempre il passaggio in cui la si usa (registrazione 2025).

Se il dominio parte da 0, come i numeri naturali ℕ, la stessa idea si scrive con P(0) come passo base e ∀n > 0 (P(n − 1) → P(n)) come passo induttivo: un quiz di ripasso su Moodle chiede proprio di riconoscere questa forma. Scrivere ∀n ∈ ℕ (P(n − 1) → P(n)) non va bene, perché per n = 0 si parlerebbe di P(−1), che non ha senso; scrivere «per qualche n > 0» non basta, perché il passo deve valere per tutti.

**Base diversa da 1.** Se si vuole provare S(n₀), S(n₀ + 1), … con un punto di partenza n₀ diverso da 1, il passo base diventa S(n₀) e il passo induttivo «per ogni n ≥ n₀, se S(n) è vera allora S(n + 1) è vera». Il passo base riguarda sempre il valore **più piccolo** del dominio. Il docente insiste che ci deve essere un primo elemento: sugli interi con segno, che scendono senza fine, l'induzione non si può fare, e serve un parametro che non scenda sotto un certo valore (registrazione 2025, già alla fine della lezione 18).

## Il fattoriale
**Definizione.** Il **fattoriale** di un intero n ≥ 0 è n! = 1 se n = 0, e n! = n(n − 1)(n − 2) ··· 2 · 1 se n ≥ 1.

(In parole povere: il fattoriale n! è il prodotto di tutti gli interi da 1 a n. Per convenzione 0! = 1. Per esempio 0! = 1! = 1, 3! = 3 · 2 · 1 = 6 e 6! = 720.)

Una proprietà che si usa in continuazione è (n + 1)! = (n + 1) · n!: il fattoriale di n + 1 si ottiene da quello di n con una sola moltiplicazione.

## Esempio: n! ≥ 2ⁿ⁻¹
**Proposizione.** Per ogni n ≥ 1 vale n! ≥ 2^{n−1}.

(In parole povere: il fattoriale cresce almeno come le potenze di 2. Per n = 1, …, 6 i fattoriali sono 1, 2, 6, 24, 120, 720 e le potenze 2^{n−1} sono 1, 2, 4, 8, 16, 32.)

**Prima il piano (registrazione 2025).** Il docente comincia scrivendo che cosa si deve provare, prima di fare qualunque conto: una «roadmap». Il passo base è la tesi con n = 1, cioè 1! ≥ 2⁰. Il passo induttivo è: supposto n! ≥ 2^{n−1}, provare la stessa tesi con n + 1 al posto di n, cioè (n + 1)! ≥ 2^{(n+1)−1} = 2ⁿ.

**Dimostrazione.**

1. **Passo base (n = 1).** 1! = 1 e 2⁰ = 1, quindi 1! ≥ 2⁰.
2. **Passo induttivo.** Si suppone n! ≥ 2^{n−1} per un n ≥ 1 e si prova (n + 1)! ≥ 2ⁿ con una catena di uguaglianze e disuguaglianze:
   (n + 1)! = (n + 1) · n! [definizione di fattoriale] ≥ (n + 1) · 2^{n−1} [ipotesi induttiva] ≥ 2 · 2^{n−1} [perché n ≥ 1, quindi n + 1 ≥ 2] = 2ⁿ [proprietà delle potenze].

Per la transitività di ≥, la catena prova (n + 1)! ≥ 2ⁿ.

Il docente commenta i singoli passi (registrazione 2025). Il primo è un **unfolding**: si sostituisce (n + 1)! con la sua definizione per far comparire n!, l'unica cosa su cui l'ipotesi induttiva dice qualcosa. Poi si usa l'ipotesi induttiva, e a quel punto manca un fattore 2: basta sapere che n + 1 ≥ 2. In un prodotto di numeri positivi, sostituire un fattore con uno più piccolo fa scendere il risultato: è ciò che autorizza i due ≥. Uno studente propone di partire dalle due estremità e «incontrarsi a metà strada» passando per 2 · n!: è la stessa prova riordinata, e secondo il docente è proprio il criterio che usano spesso sia le persone sia le macchine, cioè trovare un valore intermedio B con A ≥ B e B ≥ C.

**Prova intuitiva e prova rigorosa.** Il docente osserva che una persona si convince anche senza induzione: n! = n · (n − 1) ··· 2 · 1 contiene n − 1 fattori maggiori o uguali a 2 (tutti tranne l'1), quindi vale almeno 2^{n−1}. Questo ragionamento spiega **perché** la proprietà è vera, ma si appoggia al significato e non si sa ancora spiegare a una macchina; la prova per induzione fa perdere di vista il motivo, ma ogni passo è controllabile, anche in automatico (registrazione 2025).

La stima, aggiunge, è grossolana: dice solo che il fattoriale cresce in fretta, e a lezione accenna a una formula più precisa «con la radice di due pi greco». Qualche numero aggiunto per dare l'idea: 2⁹⁹ ≈ 6,3 · 10²⁹ (un numero di 30 cifre), mentre 100! ≈ 9,3 · 10¹⁵⁷. La formula più precisa è quella di Stirling, n! ≈ √(2πn) · (n/e)ⁿ: per n = 10 dà circa 3 598 696, contro il valore vero 3 628 800.

## Come si trova la formula: la somma dei dispari
Una prova per induzione richiede di conoscere la formula in anticipo. Il libro suggerisce una tecnica semplice: calcolare i primi casi e cercare uno schema. Per la somma dei primi n dispari 1 + 3 + … + (2n − 1), con n = 1, 2, 3, 4 si ottiene:

- n = 1: 1;
- n = 2: 1 + 3 = 4;
- n = 3: 1 + 3 + 5 = 9;
- n = 4: 1 + 3 + 5 + 7 = 16.

Sono quadrati, quindi si congettura 1 + 3 + … + (2n − 1) = n². A lezione si fanno i conti fino a 25 = 5², e il docente aggiunge che un programma potrebbe controllarne un milione: il dubbio diventa piccolissimo, ma senza un ragionamento non si ha la certezza (registrazione 2025).

![Le somme 1, 1 + 3, 1 + 3 + 5, 1 + 3 + 5 + 7 disposte come quadrati: ogni dispari è una «squadra» aggiunta lungo due lati.](figure/fond/induzione_dispari_quadrati.png|14)

Nel 2025 la lezione 19 si ferma a questi conti: il disegno e la prova che seguono sono dell'inizio della lezione successiva.

**La spiegazione con il disegno (registrazione 2025).** Gli antichi la spiegavano così: si parte da un quadratino; per passare dal quadrato 1 × 1 al 2 × 2 si aggiungono tre quadratini lungo due lati e nell'angolo; per passare dal 2 × 2 al 3 × 3 se ne aggiungono 2 + 2 + 1 = 5; in generale dal quadrato n × n al (n + 1) × (n + 1) se ne aggiungono n + n + 1 = 2n + 1, cioè il dispari successivo. Per il docente il disegno è il modo migliore per **capire**, ma ha due difetti: si fonda su impressioni, e non si sa far controllare da una macchina.

**Proposizione.** Per ogni n ≥ 1 vale 1 + 3 + … + (2n − 1) = n².

(In parole povere: sommando i primi n numeri dispari si ottiene sempre un quadrato perfetto. Per esempio la somma dei primi 100 dispari è 100² = 10 000.)

**Dimostrazione.**

1. **Passo base (n = 1).** La somma del solo primo dispari è 1 = 1².
2. **Passo induttivo.** Si suppone 1 + 3 + … + (2n − 1) = n² e si aggiunge il dispari successivo. Il primo problema è sapere quanto vale: l'n-esimo dispari è 2n − 1, quindi quello di posto n + 1 è 2(n + 1) − 1 = 2n + 1. Allora
   1 + 3 + … + (2n − 1) + (2n + 1) = n² + 2n + 1 = (n + 1)²,
   dove l'ultimo passaggio è il quadrato di un binomio.

**Il conteggio dei dispari (registrazione 2025).** A lezione la formula del dispari di posto n + 1 crea qualche confusione, perché con la scrittura 2n + 1 l'indice n conta il posto **precedente** (il primo dispari, 1, si ottiene con n = 0). Il docente allora rinumera dal posto 1: il dispari di posto n è 2n − 1, e lo verifica con una piccola induzione (2 · 1 − 1 = 1; e se il dispari di posto n è 2n − 1, quello dopo, due unità più avanti, è 2n + 1 = 2(n + 1) − 1). La prova che la somma dei primi n dispari vale n², svolta qui sopra, è l'Esercizio 1 del libro.

Il prossimo capitolo raccoglie gli altri esempi della sezione 2.4, che mostrano come l'induzione non serva solo per somme e disuguaglianze.
