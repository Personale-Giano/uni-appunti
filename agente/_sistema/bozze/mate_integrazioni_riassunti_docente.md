@@ dopo cap10.9
Prima di usare una regola come funzione bisogna quindi controllare che **abbia senso**: a ogni elemento del dominio deve associare un elemento del codominio, e uno solo. Tre regole che non superano il controllo:
- n ↦ ±√n da ℕ in ℝ: a ogni n > 0 assegna due valori;
- x ↦ √x da ℝ in ℝ: per x < 0 non assegna nessun valore;
- x ↦ x/2 da {1, 2, 3} in ℤ: a 1 assegnerebbe 1/2, che non sta nel codominio ℤ.

@@ dopo cap12.14
Il conto per esteso: se [x] = [y], allora x − y = 2n per qualche n ∈ ℤ, cioè x = y + 2n. Quindi (−1)^{x} = (−1)^{y + 2n} = (−1)^{y} · (−1)^{2n} = (−1)^{y}, perché (−1)^{2n} = 1.

@@ dopo cap12.18
## Lo schema generale e altri due esempi
In generale la situazione è questa: si ha una funzione f̃ definita su A, cioè sui rappresentanti, e si vuole definire una funzione f sull'insieme quoziente Q ponendo f([x]) = f̃(x). La definizione ha senso solo se x ∼ y implica f̃(x) = f̃(y).

Con le classi dei pari e dei dispari, la regola H([x]) = 3x non definisce una funzione verso ℤ: [0] = [2], ma 3 · 0 = 0 e 3 · 2 = 6.

Lo stesso controllo serve ogni volta che un elemento si può scrivere in più modi: due scritture dello stesso elemento devono dare lo stesso risultato. Per esempio la regola a/b ↦ b da ℚ in ℤ non è ben definita, perché 1/2 = 2/4, ma alla prima scrittura assegna 2 e alla seconda 4.

@@ dopo cap13.20
Per l'insieme vuoto, invece, f(∅) = ∅: non c'è nessun elemento di cui calcolare l'immagine.

@@ dopo cap15.19
Quando l'inversa esiste, però, le due letture del simbolo danno lo stesso insieme. Detta g = f^{-1} : B → A l'inversa, per ogni T ⊆ B l'immagine g(T) di T tramite g coincide con la controimmagine f^{-1}(T) di T tramite f: in entrambi i casi si ottengono gli elementi di A che f manda in T. Per questo usare lo stesso simbolo di solito non crea problemi: quale dei due significati si intende si capisce dal contesto.

@@ dopo cap20.6
Un esempio ancora più piccolo, dagli appunti del docente: A = {1}, B = {2, 3}, f(1) = 2 e g(2) = g(3) = 1. Allora g ∘ f = id_{A}, ma f ∘ g ≠ id_{B}, perché f(g(3)) = f(1) = 2 ≠ 3. Anche qui f non è suriettiva.

@@ dopo cap20.27
L'equivalenza tra biettiva e invertibile si usa nei due versi. Per mostrare che un'inversa esiste basta provare che f è iniettiva e suriettiva. Viceversa, per dimostrare che f è biettiva basta costruire una funzione g : B → A e controllare che g ∘ f e f ∘ g siano le identità.

@@ dopo cap20.32
## Operazioni su un insieme e sottoinsiemi chiusi
Le funzioni permettono di dire con precisione che cos'è un'operazione, come la somma o il prodotto.

**Definizione.** Un'**operazione** su un insieme non vuoto A è una funzione ∗ : A × A → A. L'immagine della coppia (a, b) si scrive a ∗ b.

(In parole povere: un'operazione prende due elementi di A, in un certo ordine, e ne restituisce uno che sta ancora in A.)

Per esempio la somma di numeri reali è la funzione + : ℝ × ℝ → ℝ che manda (a, b) in a + b. Anche la composizione è un'operazione, sull'insieme delle funzioni da un insieme in sé stesso: tornerà con le permutazioni del capitolo 32.

**Definizione.** Sia A un insieme con un'operazione ∗ e sia S ⊆ A. Si dice che S è **chiuso** rispetto a ∗ se a, b ∈ S implica a ∗ b ∈ S.

(In parole povere: S è chiuso se, facendo l'operazione tra due suoi elementi, non si esce mai da S.)

Per esempio, in ℤ con la somma, l'insieme dei pari è chiuso, perché la somma di due pari è pari. L'insieme dei dispari non lo è: 1 + 1 = 2.

@@ dopo cap25.4
L'equipollenza ha le proprietà di una relazione di equivalenza. È riflessiva: ogni insieme è equipollente a sé stesso, perché l'identità id_{A} è biettiva. È simmetrica: se f : A → B è biettiva, la sua inversa f^{-1} : B → A è a sua volta biettiva. È anche transitiva, come si vede qui sotto. Non la si può però chiamare relazione di equivalenza in senso stretto: una relazione è definita su un insieme, e qui servirebbe l'insieme di tutti gli insiemi, che porta a contraddizioni. Per lo stesso motivo, per un insieme qualunque si è definito solo che cosa vuol dire «avere la stessa cardinalità» di un altro, e non che cosa sia la sua cardinalità.

@@ dopo cap25.33
**Esempio (compleanni).** In un insieme X di più di 366 persone, due festeggiano il compleanno lo stesso giorno. Sia Y l'insieme dei giorni dell'anno, con |Y| = 366 contando il 29 febbraio, e sia f : X → Y la funzione che manda ogni persona nel giorno del suo compleanno. Poiché |X| > |Y|, f non può essere iniettiva: due persone diverse hanno lo stesso giorno.

**Esempio (punti medi).** Siano P_{1}, …, P_{5} cinque punti distinti del piano con coordinate intere, P_{i} = (x_{i}, y_{i}). Allora ce ne sono due il cui punto medio ha coordinate intere.

Il punto medio di P_{i} e P_{j} è ((x_{i} + x_{j})/2, (y_{i} + y_{j})/2): ha coordinate intere quando x_{i} + x_{j} e y_{i} + y_{j} sono entrambi pari. La somma di due interi è pari se e solo se i due numeri sono entrambi pari o entrambi dispari. A ogni punto si associa allora la coppia delle parità delle sue coordinate: f(P_{i}) = ([x_{i}], [y_{i}]), dove [a] è la classe di a modulo 2, cioè [0] se a è pari e [1] se a è dispari. Le coppie possibili sono 4: ([0], [0]), ([0], [1]), ([1], [0]) e ([1], [1]). I punti sono 5, più delle coppie, quindi f non è iniettiva: ci sono due punti diversi P_{i} e P_{j} con f(P_{i}) = f(P_{j}). Le loro coordinate hanno la stessa parità, e il loro punto medio ha coordinate intere.

@@ dopo cap25.36
Alcuni autori chiamano numerabili anche gli insiemi finiti, cioè tutti gli insiemi A con |A| ≤ |ℕ|. Qui numerabile vuol dire sempre equipollente a ℕ.

La biiezione tra ℤ e ℕ si può scrivere con una formula. Sia f : ℤ → ℕ definita da f(a) = −2a se a ≤ 0 e f(a) = 2a − 1 se a > 0. Manda 0, 1, −1, 2, −2 in 0, 1, 2, 3, 4: gli interi minori o uguali a zero vanno nei pari, quelli positivi nei dispari.

**Definizione.** La **parte intera** di un numero reale x, indicata con ⌊x⌋, è il più grande intero n tale che n ≤ x.

(In parole povere: è il numero arrotondato verso il basso, al primo intero che si incontra scendendo. Con i negativi bisogna stare attenti: si scende, non si toglie la parte dopo la virgola.)

Per esempio ⌊1/2⌋ = 0, ⌊√2⌋ = 1 perché 1 < √2 < 2, ⌊−√2⌋ = −2 perché −2 < −√2 < −1, e ⌊a⌋ = a se a è intero.

Con la parte intera l'inversa di f è g : ℕ → ℤ, g(n) = (−1)^{n+1} · ⌊(n + 1)/2⌋. Per n = 0, 1, 2, 3, 4 dà 0, 1, −1, 2, −2. In generale: se a ≤ 0, allora n = f(a) = −2a è pari e g(n) = −⌊−a + 1/2⌋ = −(−a) = a; se a > 0, allora n = 2a − 1 è dispari e g(n) = ⌊a⌋ = a. Quindi g ∘ f = id_{ℤ}. Controllare allo stesso modo che f ∘ g = id_{ℕ} è un esercizio lasciato dal docente.

@@ dopo cap25.37
Per l'insieme delle parti, solo come idea: si sa già che |X| ≤ |P(X)|, grazie alla funzione iniettiva x ↦ {x}. Se poi esistesse una funzione suriettiva f : X → P(X), si considera l'insieme S = {x ∈ X | x ∉ f(x)}. Per la suriettività S = f(x_{0}) per qualche x_{0} ∈ X. Ma se x_{0} ∈ S, per come è definito S si ha x_{0} ∉ f(x_{0}) = S; se invece x_{0} ∉ S = f(x_{0}), allora x_{0} soddisfa la condizione che definisce S e quindi x_{0} ∈ S. In entrambi i casi si arriva a una contraddizione. Quindi nessuna funzione da X in P(X) è suriettiva, e |X| < |P(X)|. In particolare P(ℕ) è un insieme non numerabile. Il docente precisa che la dimostrazione di questi teoremi non è richiesta.
