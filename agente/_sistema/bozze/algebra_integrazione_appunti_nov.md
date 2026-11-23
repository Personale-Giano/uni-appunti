@@ dopo cap44.15
**Esempio dalla lavagna (lezione 2026).** Siano v_{1} = (1, 5, 3), v_{2} = (1, −1, 1), v_{3} = (3, 3, 5) (altri vettori, non quelli del primo esempio). Per sapere se sono linearmente indipendenti si imposta λ_{1}v_{1} + λ_{2}v_{2} + λ_{3}v_{3} = 0 (alla lavagna i coefficienti si chiamano x_{1}, x_{2}, x_{3}) e si distinguono due casi: ① l'unica soluzione è quella nulla, e i vettori sono indipendenti; ② esiste un'altra soluzione, e sono dipendenti. A lezione l'esempio si ferma qui; il resto è aggiunto e controllato con SymPy.

Con il criterio dei pivot si riduce A = (v_{1} | v_{2} | v_{3}) = ( 1 1 3 ; 5 −1 3 ; 3 1 5 ). Con R_{2} → R_{2} − 5R_{1} e R_{3} → R_{3} − 3R_{1} si ottiene ( 1 1 3 ; 0 −6 −12 ; 0 −2 −4 ); la terza riga è un terzo della seconda, quindi con R_{3} → R_{3} − (1/3)R_{2} diventa nulla e resta ( 1 1 3 ; 0 −6 −12 ; 0 0 0 ). La terza colonna non ha pivot: si è nel caso ②, i vettori sono **dipendenti**. Dalle righe, λ_{1} + λ_{2} + 3λ_{3} = 0 e −6λ_{2} − 12λ_{3} = 0, cioè λ_{2} = −2λ_{3} e λ_{1} = −λ_{3}: le soluzioni sono t(−1, −2, 1). Con t = 1 si ottiene −v_{1} − 2v_{2} + v_{3} = 0, cioè v_{3} = v_{1} + 2v_{2}. Controllo: (1, 5, 3) + 2·(1, −1, 1) = (3, 3, 5).

@@ dopo cap48.5
**Esempio dalla lavagna (lezione 2026).** Sia f : ℝ³ → ℝ² la proiezione f(x, y, z) = (x, y), che è lineare. Il nucleo è fatto dei vettori con x = y = 0: Ker f = {(0, 0, t) | t ∈ ℝ} = Span((0, 0, 1)), l'asse z, un sottospazio di ℝ³ di dimensione 1 (una «retta»). L'immagine è tutto ℝ², perché ogni (a, b) è f(a, b, 0): dim Im f = 2. Il teorema torna: 1 + 2 = 3 = dim ℝ³. È l'esempio più semplice possibile: la proiezione dimentica una coordinata, e la direzione che va persa è proprio il nucleo.

@@ dopo cap49.50
**Esempio dalla lavagna (lezione 2026).** In V = ℝ_{2}[x] si prende B = {1, x + 1, x² + x} e si calcola F_{B}^{−1}(p(x)) = [p(x)]_{B} per p(x) = x² + 2x + 1. Se [p(x)]_{B} = (a, b, c), deve essere

x² + 2x + 1 = a·1 + b(x + 1) + c(x² + x) = c·x² + (b + c)x + (a + b).

Confrontando i coefficienti: c = 1 (coefficiente di x²); b + c = 2, quindi b = 1; a + b = 1, quindi a = 0. Dunque

[p(x)]_{B} = (0, 1, 1).

Controllo: (x + 1) + (x² + x) = x² + 2x + 1. Rispetto all'esempio precedente qui si legge subito solo c: x compare in due elementi della base, e il sistema si risolve «a cascata», dal grado più alto al più basso. (Che B sia una base si vede come sopra: 1, x = (x + 1) − 1 e x² = (x² + x) − x stanno nel suo Span; osservazione aggiunta.)

@@ dopo cap51.19
**Esempio dalla lavagna (lezione 2026).** Sia f : ℝ_{2}[x] → ℝ_{1}[x] l'applicazione lineare che, rispetto alle basi B = {1, x, x²} e C = {1, x}, ha matrice

[f]^{B}_{C} = ( 1 0 2 ; 0 5 3 ) ∈ M(2, 3).

Si vuole f(a + bx + cx²) per un polinomio qualsiasi. Le coordinate di p(x) = a + bx + cx² nella base B sono i suoi coefficienti, [p(x)]_{B} = (a, b, c): è il caso speciale della base canonica. Per la proposizione

[f(p(x))]_{C} = ( 1 0 2 ; 0 5 3 ) · (a, b, c) = (a + 2c, 5b + 3c).

Rispetto agli esempi precedenti c'è un passo in più: lo spazio di arrivo è fatto di polinomi, quindi le coordinate trovate vanno ritradotte nella base C = {1, x}:

f(a + bx + cx²) = (a + 2c)·1 + (5b + 3c)·x = (a + 2c) + (5b + 3c)x.

Per esempio f(x²) = 2 + 3x, che si legge nella terza colonna della matrice, e f(1 + x + x²) = 3 + 8x. (Questi due casi sono aggiunti per chiarezza.)

@@ dopo cap52.59
**Esempio dalla lavagna (lezione 2026): un cambio di base tra polinomi.** In V = ℝ_{1}[x] si prendono B = {1, 1 + x} e B′ = {1 + x, 2 + x}. Si vogliono A = [I_{V}]^{B}_{B′} (alla lavagna [id]^{B}_{B′}), le coordinate di x nelle due basi e il controllo A[x]_{B} = [x]_{B′}. Qui non si può usare la scorciatoia della base canonica: a lezione ogni colonna si ricava risolvendo un sistema (con la composizione del cap. 53 si potrebbe aggirare).

- Prima colonna, [1]_{B′}. Da 1 = a(1 + x) + b(2 + x) = (a + 2b) + (a + b)x si ha a + b = 0 e a + 2b = 1, quindi b = 1 e a = −1 (a lezione questo conto è solo impostato).
- Seconda colonna, [1 + x]_{B′} = (1, 0), perché 1 + x è il primo vettore di B′.

Quindi

A = [I_{V}]^{B}_{B′} = ( −1 1 ; 1 0 ).

Le coordinate di x: da x = a(1 + x) + b(2 + x) = (a + 2b) + (a + b)x si ha a + b = 1 e a + 2b = 0, quindi b = −1, a = 2 e [x]_{B′} = (2, −1); da x = c·1 + d(1 + x) si ha d = 1 e c = −1, quindi [x]_{B} = (−1, 1). Controllo della formula del cambio di coordinate:

A · [x]_{B} = ( −1 1 ; 1 0 ) · (−1, 1) = (1 + 1, −1) = (2, −1) = [x]_{B′}.

Per la proposizione sull'inversa, nel verso opposto [I_{V}]^{B′}_{B} = A^{−1} = ( 0 1 ; 1 1 ): infatti 1 + x = 0·1 + 1·(1 + x) e 2 + x = 1·1 + 1·(1 + x) (controllo aggiunto).

@@ dopo cap59.31
**Alla lavagna (lezione 2026)** l'Esempio 17.2 ha anche un «non esempio»: per v = (3, 1) si ha A·v = (9 + 4, 2) = (13, 2), che non è un multiplo di (3, 1) per nessun λ (servirebbe insieme 3λ = 13 e λ = 2). Quindi (3, 1) non è un autovettore.

@@ dopo cap59.46
**Alla lavagna (lezione 2026).** La rotazione di un angolo θ qualsiasi (θ ∉ {0, π}) è scritta con la sua matrice nella base canonica,

A = Rot_{θ} = ( cos θ  −sin θ ; sin θ  cos θ ),

le cui colonne sono le immagini dei vettori della base canonica: L_{A}(e_{1}) = (cos θ, sin θ), cioè e_{1} ruotato di θ, e L_{A}(e_{2}) = (−sin θ, cos θ), cioè e_{2} ruotato di θ. Il docente lo mostra con un disegno dei due vettori ruotati e conclude come sopra: per ogni v ≠ 0, L_{A}(v) = A·v è v ruotato di un angolo θ; se θ ≠ 0 e θ ≠ π non è mai un multiplo di v, quindi non ci sono autovettori. Per θ = π/2 si ritrova Rot_{π/2}(x, y) = (−y, x), con matrice ( 0 −1 ; 1 0 ) (collegamento aggiunto; è la matrice del cap. 61).

@@ dopo cap60.60
**Alla lavagna (lezione 2026)** il docente verifica anche per esteso che M diagonalizza A, con la scrittura delle dispense D = M^{−1}AM. Poiché det M = 1, M^{−1} è la trasposta della matrice dei cofattori (cap. 36), M^{−1} = ( 1 4 ; 0 1 ), e

D = M^{−1} A M = ( 1 4 ; 0 1 ) · ( 3 4 ; 0 2 ) · ( 1 −4 ; 0 1 ) = ( 3 12 ; 0 2 ) · ( 1 −4 ; 0 1 ) = ( 3 0 ; 0 2 ) = diag(3, 2),

che è proprio la matrice diagonale trovata con la proposizione nell'Esempio 17.9. Quindi

@@ dopo cap61.40
**Esempio dalla lavagna (lezione 2026).** Il primo esempio 3 × 3 della lezione è una triangolare **inferiore**:

A = ( 1 0 0 ; 1 2 0 ; 2 1 3 ),   p_{A}(t) = det( 1 − t  0  0 ; 1  2 − t  0 ; 2  1  3 − t ) = (1 − t)(2 − t)(3 − t).

Gli autovalori 1, 2 e 3 si leggono sulla diagonale, come dice la proposizione. Gli autovettori di questa matrice sono nel cap. 62, le molteplicità nel cap. 63.

@@ dopo cap62.39
**Esempio dalla lavagna (lezione 2026).** Per la matrice 3 × 3 triangolare del cap. 61, A = ( 1 0 0 ; 1 2 0 ; 2 1 3 ), gli autovalori 1, 2, 3 sono distinti e n = 3, quindi per il corollario A è diagonalizzabile (applicazione aggiunta). Alla lavagna si cercano gli autovettori di λ = 3: v = (x, y, z) è autovettore se Av = 3v, cioè (A − 3I_{3})v = 0, con

A − 3I_{3} = ( −2 0 0 ; 1 −1 0 ; 2 1 0 ).

Il sistema è −2x = 0, x − y = 0, 2x + y = 0, quindi x = 0, y = 0 e z libero:

V_{3} = {(0, 0, z) | z ∈ ℝ} = Span((0, 0, 1)).

Gli autovettori di autovalore 3 sono i vettori non nulli di questa retta: lo zero sta nell'autospazio, ma non è un autovettore. Gli altri due autospazi, non calcolati a lezione, si trovano allo stesso modo (conto aggiunto, controllato con SymPy): A − I_{3} = ( 0 0 0 ; 1 1 0 ; 2 1 2 ) dà x + y = 0 e 2x + y + 2z = 0, quindi V_{1} = Span((−2, 2, 1)); A − 2I_{3} = ( −1 0 0 ; 1 0 0 ; 2 1 1 ) dà x = 0 e y + z = 0, quindi V_{2} = Span((0, −1, 1)). Con gli autovettori in colonna e gli autovalori nello stesso ordine (cap. 60):

P = ( −2 0 0 ; 2 −1 0 ; 1 1 1 ),   D = diag(1, 2, 3),   A = P D P^{−1}.

@@ dopo cap63.24
**Esempio dalla lavagna (lezione 2026).** Per A = ( 1 0 0 ; 1 2 0 ; 2 1 3 ) dei cap. 61-62, p_{A}(t) = (1 − t)(2 − t)(3 − t) = −(t − 1)(t − 2)(t − 3), quindi ogni autovalore ha m_{a} = 1. A lezione le molteplicità sono raccolte in una tabella:

- λ = 3: m_{a}(3) = 1 e m_{g}(3) = dim V_{3} = 1, perché V_{3} = Ker(A − 3I_{3}) = Span((0, 0, 1)) (cap. 62): è l'unica molteplicità geometrica scritta alla lavagna;
- λ = 1 e λ = 2: m_{a} = 1, mentre la casella di m_{g} è vuota negli appunti; si ricava senza conti dalla conseguenza appena vista, 1 ≤ m_{g} ≤ m_{a} = 1, quindi m_{g}(1) = m_{g}(2) = 1. Lo conferma il cap. 62, dove V_{1} e V_{2} risultano due rette.
