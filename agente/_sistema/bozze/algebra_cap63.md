# 63. Molteplicità e Teorema di Diagonalizzabilità
## Due modi di contare un autovalore
Il cap. 62 si è chiuso con ( 1 1 ; 0 1 ): un solo autovalore, 1, che però nel polinomio caratteristico (1 − t)^{2} compare «due volte», mentre il suo autospazio è solo una retta. Per descrivere questo scarto, a lezione (registrazione 2024) il docente associa a ogni autovalore due numeri.

**Definizione.** Sia T : V → V un endomorfismo e sia λ un autovalore di T (cioè una radice di p_{T}(t), cap. 61).
1. La **molteplicità geometrica** di λ è la dimensione del suo autospazio: m_{g}(λ) = dim V_{λ}.
2. La **molteplicità algebrica** di λ è la sua molteplicità come radice del polinomio caratteristico (cap. 12): m_{a}(λ) è il numero m tale che

p_{T}(t) = (t − λ)^{m} · q(t),   con q(λ) ≠ 0.

(In parole povere: la molteplicità algebrica conta quante volte λ compare come radice del polinomio; la molteplicità geometrica conta quante direzioni indipendenti vengono moltiplicate per λ. Per ( 1 1 ; 0 1 ) la prima vale 2 e la seconda 1.)

La scrittura con q(λ) ≠ 0 è quella della lavagna: dice che dal polinomio si possono tirare fuori m fattori (t − λ), ma non m + 1, che è la definizione di molteplicità del cap. 12. Le dispense scrivono ma(λ) e mg(λ) senza pedici. Se p_{T}(t) è scritto con fattori (λ − t), come succede con det(A − tI), non cambia niente: (λ − t)^{m} = (−1)^{m}(t − λ)^{m}.

Per una matrice A ∈ M(n, 𝕂), il teorema della dimensione (cap. 48) dà un modo rapido di calcolare la molteplicità geometrica senza risolvere il sistema: V_{λ} = Ker(A − λI_{n}), quindi

m_{g}(λ) = dim Ker(A − λI_{n}) = n − rk(A − λI_{n}).

**Esempio dalla lavagna (registrazione 2024; Esempio 18.8 delle dispense).** Sia A = ( 1 1 ; 0 1 ), su ℝ. La matrice è triangolare, quindi

p_{A}(t) = det( 1 − t  1 ; 0  1 − t ) = (1 − t)^{2}:

l'unico autovalore è 1, con m_{a}(1) = 2. Per la molteplicità geometrica il docente fa il conto in due modi.
- Risolvendo il sistema: V_{1} = {(x, y) ∈ ℝ² | (A − I_{2})(x, y) = (0, 0)}, con A − I_{2} = ( 0 1 ; 0 0 ). Il prodotto è (y, 0), quindi la condizione è y = 0 e V_{1} = {(x, 0) | x ∈ ℝ} = Span((1, 0)), che ha per base (1, 0). Dunque m_{g}(1) = 1.
- Con il teorema della dimensione: m_{g}(1) = dim Ker(A − I_{2}) = 2 − rk(A − I_{2}) = 2 − 1 = 1.

Quindi m_{a}(1) = 2 ≠ 1 = m_{g}(1): le due molteplicità possono essere diverse.

## La molteplicità geometrica non supera quella algebrica
**Teorema.** Sia T : V → V un endomorfismo. Per ogni autovalore λ_{0} di T

1 ≤ m_{g}(λ_{0}) ≤ m_{a}(λ_{0}).

(In parole povere: un autovalore ha sempre almeno una direzione, e mai più direzioni di quante volte compare come radice. L'autospazio può essere «troppo piccolo», mai «troppo grande».)

Alla lavagna (registrazione 2024) è scritta solo la disuguaglianza m_{g}(λ) ≤ m_{a}(λ), riquadrata e senza dimostrazione. Le dispense (Teorema 18.9) aggiungono la prima disuguaglianza e un'idea della dimostrazione.
- 1 ≤ m_{g}(λ_{0}): se λ_{0} è un autovalore, esiste un autovettore v ≠ 0 con T(v) = λ_{0}v, quindi V_{λ_{0}} ≠ {0} e ha dimensione almeno 1.
- m_{g}(λ_{0}) ≤ m_{a}(λ_{0}): sia m = m_{g}(λ_{0}). Si sceglie una base di V_{λ_{0}}, formata da m autovettori di autovalore λ_{0}, e la si completa a una base di V. Nella matrice di T rispetto a questa base, le prime m colonne sono quelle di λ_{0}v_{1}, …, λ_{0}v_{m}, cioè formano in alto a sinistra un blocco diagonale λ_{0}I_{m} con zeri sotto. Nel determinante di A − tI_{n} compare allora il fattore (λ_{0} − t)^{m}: per esempio sviluppando con Laplace (cap. 33) lungo la prima colonna, che ha un solo elemento non nullo, λ_{0} − t, e ripetendo m volte. Quindi (t − λ_{0})^{m} divide p_{T}(t), e la molteplicità di λ_{0} come radice è almeno m.

**Una conseguenza utile.** Se m_{a}(λ) = 1, allora per forza m_{g}(λ) = 1. Gli autovalori **semplici** (radici semplici del polinomio caratteristico) non danno mai problemi: il conto della molteplicità geometrica serve solo per quelli con m_{a}(λ) ≥ 2. Le dispense usano proprio questo nell'Esempio 18.11, più avanti.

## Il teorema di diagonalizzabilità
**Teorema (di diagonalizzabilità).** Sia V uno spazio vettoriale di dimensione n su 𝕂 e sia T : V → V un endomorfismo. T è diagonalizzabile se e solo se valgono entrambe le condizioni seguenti:
- (a) p_{T}(t) ha esattamente n radici in 𝕂, contate con molteplicità;
- (b) per ogni autovalore λ di T, m_{a}(λ) = m_{g}(λ).

(In parole povere: per essere diagonalizzabile servono due cose. Il polinomio caratteristico deve spezzarsi completamente in fattori di primo grado nel campo in cui si lavora, e ogni autovalore deve avere tante direzioni quante volte compare come radice.)

Alla lavagna (registrazione 2024) n = dim V è annotato come uguale al grado di p_{T}(t), e le parole «in 𝕂» sono state aggiunte dopo, con una freccia: sono essenziali, come mostra l'esempio della rotazione. Il teorema non è dimostrato a lezione; la dimostrazione è quella delle dispense.

**Dimostrazione (dalle dispense).** Siano λ_{1}, …, λ_{k} gli autovalori distinti di T. Per il cap. 62 gli autospazi sono in somma diretta; sia W = V_{λ_{1}} ⊕ … ⊕ V_{λ_{k}} la loro somma. Sempre per il cap. 62, T è diagonalizzabile se e solo se W = V, cioè se e solo se dim W = n. D'altra parte

dim W = m_{g}(λ_{1}) + … + m_{g}(λ_{k}) ≤ m_{a}(λ_{1}) + … + m_{a}(λ_{k}) ≤ n.

La prima disuguaglianza viene dal teorema precedente, applicato a ciascun autovalore. La seconda dal fatto che λ_{1}, …, λ_{k} sono radici di p_{T}(t), che ha grado n (cap. 61) e quindi al più n radici contate con molteplicità (cap. 13). Allora dim W = n se e solo se entrambe le disuguaglianze sono uguaglianze. La prima lo è esattamente quando m_{g}(λ_{i}) = m_{a}(λ_{i}) per ogni i, cioè la condizione (b); la seconda esattamente quando le radici in 𝕂, contate con molteplicità, sono n, cioè la condizione (a). ∎

Il teorema contiene come caso particolare il corollario del cap. 62: se ci sono n autovalori distinti, (a) vale e ciascuno ha m_{a} = 1, quindi anche m_{g} = 1 e (b) vale. E spiega l'esempio di prima: per ( 1 1 ; 0 1 ) la condizione (a) è verificata (due radici reali, contate con molteplicità), ma (b) no.

**Esempio.** Per A = ( 2 1 ; 1 2 ) del cap. 62 gli autovalori 1 e 3 sono semplici: (a) vale, e m_{a} = m_{g} = 1 per entrambi. Diagonalizzabile, come già visto. (Applicazione aggiunta per chiarezza; a lezione l'esempio è usato con il corollario del cap. 62.)

## Su ℝ o su ℂ: la rotazione
**Esempio dalla lavagna (registrazione 2024).** Sia A = ( 0 1 ; −1 0 ) ∈ M(2, ℝ), cioè L_{A} : ℝ² → ℝ², che il docente disegna come una rotazione. (È la rotazione di 90 gradi in senso **orario**: L_{A}(e_{1}) = (0, −1). Nel cap. 61, dalla registrazione 2025, c'era quella in senso antiorario, ( 0 −1 ; 1 0 ); i conti sono gli stessi.) È diagonalizzabile?

Con la formula delle 2 × 2 (cap. 61), tr A = 0 e det A = 1, quindi

p_{A}(t) = t^{2} − 0·t + 1 = t^{2} + 1.

Su ℝ l'equazione t^{2} = −1 non ha soluzioni: la condizione (a) fallisce, e **A non è diagonalizzabile su ℝ**. Su ℂ invece p_{A}(t) ha le due radici i e −i: A è una matrice 2 × 2 con 2 autovalori distinti, quindi per il corollario del cap. 62 **A è diagonalizzabile su ℂ**.

Gli autovettori complessi si trovano come sempre, risolvendo (A − λI_{2})v = 0 (conto non presente nelle dispense né in lezione, controllato con SymPy). Per λ = i, A − iI_{2} = ( −i 1 ; −1 −i ) e la prima equazione dice −ix + y = 0, cioè y = ix: V_{i} = Span((1, i)). Infatti A·(1, i) = (i, −1) = i·(1, i). Allo stesso modo V_{−i} = Span((1, −i)). Quindi, su ℂ,

A = P D P^{−1},   con   P = ( 1 1 ; i −i )   e   D = ( i 0 ; 0 −i ).

**Osservazione (alla lavagna, registrazione 2024).** Se 𝕂 = ℂ, la condizione (a) è **sempre** verificata, per il teorema fondamentale dell'algebra (cap. 13): un polinomio complesso di grado n ha esattamente n radici complesse, contate con molteplicità. Il resto dell'osservazione è aggiunto per chiarezza. Su ℂ, quindi, per decidere se una matrice è diagonalizzabile basta controllare la condizione (b). Su ℝ invece bisogna controllarle tutte e due, perché il polinomio può avere radici non reali.

## Come si studia la diagonalizzabilità
Mettendo insieme i cap. 61-63, lo studio di una matrice A ∈ M(n, 𝕂) segue sempre gli stessi passi (schema riassuntivo aggiunto per chiarezza; sono i passi degli esempi della lavagna e delle dispense):
1. si calcola p_{A}(t) = det(A − tI_{n}), con le scorciatoie del cap. 61 (traccia e determinante per le 2 × 2, prodotto della diagonale per le triangolari);
2. se ne cercano le radici in 𝕂 con le loro molteplicità algebriche; se sono meno di n, contate con molteplicità, A **non** è diagonalizzabile su 𝕂 (condizione a);
3. per ogni autovalore con m_{a}(λ) ≥ 2 si calcola m_{g}(λ) = n − rk(A − λI_{n}); se per uno di essi m_{g}(λ) < m_{a}(λ), A **non** è diagonalizzabile (condizione b); gli autovalori semplici si possono saltare;
4. se tutto torna, A è diagonalizzabile, e se serve una base di autovettori la si ottiene unendo basi degli autospazi V_{λ} = Ker(A − λI_{n}); con gli autovettori in colonna in P e gli autovalori nello stesso ordine in D, A = PDP^{−1} (cap. 60).

## Due esempi 3 × 3 dalle dispense
A lezione non ci sono esempi 3 × 3; le dispense ne svolgono due.

**Esempio 18.11.** Si studia su ℝ la diagonalizzabilità di A = ( 3 0 0 ; −4 −1 −8 ; 0 0 3 ). Sviluppando lungo la prima riga (cap. 33), che ha un solo elemento non nullo, e poi calcolando un determinante 2 × 2 triangolare, si trova

p_{A}(t) = (3 − t)(−1 − t)(3 − t),

con radici λ_{1} = 3, m_{a}(3) = 2, e λ_{2} = −1, m_{a}(−1) = 1. Tutte le radici sono reali, quindi (a) vale, e resta la condizione (b). Per λ_{2} = −1 non c'è niente da fare: è semplice, quindi m_{g}(−1) = m_{a}(−1) = 1. Per λ_{1} = 3 il teorema precedente lascia due possibilità, m_{g}(3) = 1 (non diagonalizzabile) oppure 2 (diagonalizzabile). Con il teorema della dimensione (o Rouché-Capelli, cap. 42):

m_{g}(3) = 3 − rk(A − 3I_{3}) = 3 − rk( 0 0 0 ; −4 −4 −8 ; 0 0 0 ) = 3 − 1 = 2.

Quindi m_{a}(3) = m_{g}(3) = 2 e A è diagonalizzabile. Una base di autovettori, che le dispense non scrivono (conto aggiunto, controllato con SymPy): V_{3} è dato dall'unica equazione −4x − 4y − 8z = 0, cioè x = −y − 2z, e ha base (−1, 1, 0), (−2, 0, 1); V_{−1} = Ker( 4 0 0 ; −4 0 −8 ; 0 0 4 ) dà x = 0 e z = 0, e ha base (0, 1, 0). Con P = ( −1 −2 0 ; 1 0 1 ; 0 1 0 ) e D = diag(3, 3, −1) si ha A = PDP^{−1}.

**Esempio 18.12 (con un parametro).** Si studia su ℝ, al variare di k ∈ ℝ, la matrice A = ( 3  k + 4  1 ; −1  −3  −1 ; 0  0  2 ). Sviluppando lungo l'ultima riga,

p_{A}(t) = (2 − t)·det( 3 − t  k + 4 ; −1  −3 − t ) = (2 − t)(t^{2} + k − 5),

perché (3 − t)(−3 − t) + (k + 4) = t^{2} − 9 + k + 4.
- Se k > 5, il fattore t^{2} + k − 5 non ha radici reali: p_{A}(t) ha una sola radice reale, la condizione (a) fallisce e A non è diagonalizzabile.
- Se k ≤ 5, le radici sono tre e reali: λ_{1} = 2, λ_{2} = √(5 − k), λ_{3} = −√(5 − k). Se sono distinte, A è diagonalizzabile per il corollario del cap. 62. Possono coincidere solo in due casi: √(5 − k) = 2, cioè k = 1, oppure √(5 − k) = 0, cioè k = 5.
- k = 1: gli autovalori sono 2, 2, −2 e A = ( 3 5 1 ; −1 −3 −1 ; 0 0 2 ). Allora m_{g}(2) = 3 − rk( 1 5 1 ; −1 −5 −1 ; 0 0 0 ) = 3 − 1 = 2 = m_{a}(2): diagonalizzabile.
- k = 5: gli autovalori sono 2, 0, 0 e A = ( 3 9 1 ; −1 −3 −1 ; 0 0 2 ). Allora m_{g}(0) = 3 − rk(A) = 3 − 2 = 1 ≠ 2 = m_{a}(0): non diagonalizzabile.

Riassumendo, A è diagonalizzabile se e solo se k < 5.

## Esercizi
Svolgimento non presente nelle dispense (che danno solo il testo) né in lezione; i conti sono controllati con SymPy.

**Esercizio 18.13.** Sia A = ( 2 1 1 ; 0 3 0 ; 0 0 3 ). (1) Calcolare il polinomio caratteristico e gli autovalori. (2) Trovare gli autospazi. (3) Calcolare le molteplicità algebrica e geometrica di ogni autovalore. (4) Stabilire se A è diagonalizzabile. (5) In caso affermativo, trovare una base di ℝ³ formata da autovettori.

(1) A è triangolare superiore, quindi p_{A}(t) = (2 − t)(3 − t)^{2} e gli autovalori sono 2 e 3, letti sulla diagonale.

(2) Per λ = 2: A − 2I_{3} = ( 0 1 1 ; 0 1 0 ; 0 0 1 ) dà y + z = 0, y = 0, z = 0, cioè y = z = 0 con x libero: V_{2} = Span((1, 0, 0)). Per λ = 3: A − 3I_{3} = ( −1 1 1 ; 0 0 0 ; 0 0 0 ) dà l'unica equazione −x + y + z = 0, cioè x = y + z: i vettori sono (y + z, y, z) = y(1, 1, 0) + z(1, 0, 1), e V_{3} = Span((1, 1, 0), (1, 0, 1)).

(3) m_{a}(2) = 1 e m_{g}(2) = 1; m_{a}(3) = 2 e m_{g}(3) = dim V_{3} = 2 (anche: 3 − rk(A − 3I_{3}) = 3 − 1 = 2).

(4) Le radici sono tutte reali e le molteplicità coincidono: per il teorema di diagonalizzabilità A è diagonalizzabile.

(5) Unendo le basi degli autospazi: B = {(1, 0, 0), (1, 1, 0), (1, 0, 1)}. Con P = ( 1 1 1 ; 0 1 0 ; 0 0 1 ) e D = diag(2, 3, 3) si ha A = PDP^{−1}; per controllo, P^{−1} = ( 1 −1 −1 ; 0 1 0 ; 0 0 1 ).

**Esercizio 18.14.** Siano A = ( 1 0 0 ; 0 1 0 ; 0 0 2 ) e B = ( 1 1 0 ; 0 1 0 ; 0 0 2 ). (1) Verificare che A e B hanno lo stesso polinomio caratteristico. (2) Calcolare la molteplicità geometrica dell'autovalore 1 per entrambe. (3) Stabilire quale delle due è diagonalizzabile.

(1) Sono entrambe triangolari con diagonale 1, 1, 2, quindi p_{A}(t) = p_{B}(t) = (1 − t)^{2}(2 − t).

(2) A − I_{3} = ( 0 0 0 ; 0 0 0 ; 0 0 1 ) ha rango 1, quindi m_{g}(1) = 3 − 1 = 2. B − I_{3} = ( 0 1 0 ; 0 0 0 ; 0 0 1 ) ha rango 2, quindi m_{g}(1) = 3 − 2 = 1.

(3) In entrambe m_{a}(1) = 2 e l'autovalore 2 è semplice. A è diagonalizzabile (è già diagonale, e infatti m_{g}(1) = 2 = m_{a}(1)); B no, perché m_{g}(1) = 1 < 2. È la versione 3 × 3 di I_{2} e ( 1 1 ; 0 1 ): lo stesso polinomio caratteristico non basta a rendere simili due matrici (cap. 61), e la differenza la fanno le molteplicità geometriche, che sono le stesse per matrici simili: se due matrici sono simili, M′ = PMP^{−1}, allora M′ − λI_{n} = P(M − λI_{n})P^{−1}, e matrici simili hanno lo stesso rango (cap. 54). (Quest'ultima osservazione è aggiunta per chiarezza.)

Con il teorema di diagonalizzabilità si chiude lo studio di autovalori e autovettori: dato un endomorfismo, ora si sa decidere se esiste una base in cui la sua matrice è diagonale, e trovarla quando c'è.
