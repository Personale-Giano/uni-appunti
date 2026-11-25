# 67. La Matrice Associata a un Prodotto Scalare
## Il cammino inverso
Il cap. 66 ha mostrato come una matrice simmetrica S produca un prodotto scalare g_{S} su ℝⁿ. Per gli endomorfismi c'era anche il cammino inverso, ricorda il docente a lezione (registrazione 2025): dato un endomorfismo T e una base B, si costruisce la matrice associata [T]^{B}_{B} (cap. 50). Con i prodotti scalari si può fare la stessa cosa, e anzi la costruzione è più semplice.

**Definizione (Def. 19.12).** Sia V uno spazio vettoriale reale, sia g : V × V → ℝ un prodotto scalare e sia B = {v_{1}, …, v_{n}} una base di V. La **matrice associata a g nella base B** è la matrice n × n

S = [g]_{B}   con entrate   S_{ij} = g(v_{i}, v_{j}).

(In parole povere: si prendono tutti i vettori della base, si calcolano tutti i prodotti scalari possibili fra loro, a due a due, e si mettono in una tabella: nella riga i e colonna j va il prodotto scalare dell'i-esimo vettore con il j-esimo.)

Per n = 2, con B = {v_{1}, v_{2}}, la matrice è

[g]_{B} = ( g(v_{1}, v_{1})  g(v_{1}, v_{2}) ; g(v_{2}, v_{1})  g(v_{2}, v_{2}) ).

Rispetto alla matrice di un'applicazione lineare c'è una differenza: qui non si calcolano immagini e poi coordinate, si calcolano direttamente dei numeri. E c'è una sola base, non una di partenza e una di arrivo (osservazioni aggiunte per chiarezza).

**Osservazione (alla lavagna, registrazione 2025).** La matrice associata è sempre **simmetrica**. Infatti, per la proprietà 3 del prodotto scalare,

S_{ji} = g(v_{j}, v_{i}) = g(v_{i}, v_{j}) = S_{ij},

quindi [g]_{B} ∈ S(n). Come dice il docente, è la simmetria del prodotto scalare a rendere simmetrica la matrice. In pratica (osservazione aggiunta) questo dimezza i conti: basta calcolare le entrate sulla diagonale e quelle sopra, le altre si copiano.

**Esempio (Esempio 19.14 delle dispense).** Su ℝ² con il prodotto scalare euclideo si consideri la base B = {v_{1} = (1, 0), v_{2} = (1, 1)}. Si ha g(v_{1}, v_{1}) = 1, g(v_{1}, v_{2}) = 1·1 + 0·1 = 1, g(v_{2}, v_{2}) = 1 + 1 = 2, quindi

[g]_{B} = ( 1 1 ; 1 2 ).

Lo stesso prodotto scalare, quello euclideo, ha matrice I_{2} nella base canonica e matrice ( 1 1 ; 1 2 ) in questa base: come per le applicazioni lineari, **la matrice dipende dalla base scelta**.

## Nella base canonica si ritrova S
**Proposizione (Esempio 19.13; alla lavagna, registrazione 2025).** Sia S ∈ S(n) e sia C = {e_{1}, …, e_{n}} la base canonica di ℝⁿ. Allora la matrice associata a g_{S} nella base canonica è S stessa:

[g_{S}]_{C} = S.

**Dimostrazione (alla lavagna).** Per definizione di matrice associata, l'entrata (i, j) di [g_{S}]_{C} è g_{S}(e_{i}, e_{j}) = ᵗe_{i} S e_{j}. Il docente fa il conto con le matrici:
1. S · e_{j} è la **j-esima colonna** di S, cioè (S_{1j}, S_{2j}, …, S_{nj}): nel prodotto righe per colonne ogni riga di S viene moltiplicata per e_{j}, che ha 1 solo in posizione j, quindi di ogni riga sopravvive solo l'entrata della colonna j;
2. ᵗe_{i} · (S_{1j}, …, S_{nj}) prende l'**i-esimo elemento** di quella colonna, perché ᵗe_{i} è la riga (0, …, 1, …, 0) con l'1 in posizione i: il risultato è S_{ij}.

Quindi [g_{S}]_{C} e S hanno le stesse entrate in ogni posizione, e due matrici con le stesse entrate sono uguali. È il Corollario 19.9 del cap. 66, letto come affermazione sulla matrice associata.

Come sottolineato a lezione (registrazione 2025), il significato è che le due costruzioni viste finora sono **una l'inversa dell'altra**, almeno con la base canonica: partendo da una matrice simmetrica S si costruisce g_{S}, e prendendo la matrice di g_{S} nella base canonica si torna a S. È l'analogo del fatto, visto per gli endomorfismi, che la matrice di L_{A} nella base canonica è A (cap. 50).

## Calcolare il prodotto scalare con le coordinate
L'ultima cosa che il docente vuole mostrare è che con la matrice associata si può **calcolare** il prodotto scalare di due vettori qualsiasi. Per gli endomorfismi c'era la formula [T(v)]_{B} = [T]^{B}_{B} · [v]_{B} (cap. 51); per i prodotti scalari la formula analoga è la seguente.

**Proposizione (Cor. 19.16; alla lavagna, registrazione 2025).** Sia g un prodotto scalare su V e sia B una base di V. Allora per ogni v, w ∈ V

g(v, w) = ᵗ[v]_{B} · [g]_{B} · [w]_{B},

dove [v]_{B} e [w]_{B} sono i vettori delle coordinate di v e w nella base B (cap. 25).

(In parole povere: per calcolare il prodotto scalare di due vettori basta conoscere le loro coordinate e la tabella dei prodotti scalari fra i vettori della base. Si fa «riga delle coordinate di v, per la tabella, per la colonna delle coordinate di w».)

Alla lavagna la proposizione è solo enunciata e poi verificata su un esempio. Le dispense la ricavano dalla bilinearità.

**Dimostrazione (dalle dispense, Prop. 19.15).** Siano B = {v_{1}, …, v_{n}}, v = λ_{1}v_{1} + … + λ_{n}v_{n} e w = μ_{1}v_{1} + … + μ_{n}v_{n}, cioè [v]_{B} = (λ_{1}, …, λ_{n}) e [w]_{B} = (μ_{1}, …, μ_{n}). Per la bilinearità (cap. 64) si può sviluppare come un prodotto di due somme:

g(v, w) = g(Σ_{i} λ_{i}v_{i}, Σ_{j} μ_{j}v_{j}) = Σ_{i=1}^{n} Σ_{j=1}^{n} λ_{i} μ_{j} g(v_{i}, v_{j}) = Σ_{i=1}^{n} Σ_{j=1}^{n} λ_{i} S_{ij} μ_{j},

con S = [g]_{B}. Per la formula generale del cap. 66 (Prop. 19.8), l'ultima somma è esattamente ᵗ[v]_{B} · S · [w]_{B}.

Nel caso V = ℝⁿ, g = g_{S} e B = C base canonica, le coordinate di un vettore sono il vettore stesso e [g_{S}]_{C} = S: la proposizione ridà la definizione g_{S}(v, w) = ᵗv S w.

## Un esempio completo
**Esempio dalla lavagna (registrazione 2025).** Sia S = ( 1 2 ; 2 3 ), con prodotto scalare (cap. 66)

g_{S}((x_{1}, x_{2}), (y_{1}, y_{2})) = x_{1}y_{1} + 2x_{1}y_{2} + 2x_{2}y_{1} + 3x_{2}y_{2}.

Si calcola la matrice associata nella base B = {v_{1} = (0, 1), v_{2} = (1, 1)}. Il docente osserva che con la base canonica non ci sarebbe nessun conto da fare (la matrice sarebbe S), mentre qui servono tre prodotti scalari; ogni entrata si può calcolare in due modi, con il prodotto ᵗv_{i} S v_{j} oppure sostituendo nella formula, e «i due risultati devono venire uguali». Con la formula:
- g_{S}(v_{1}, v_{1}): x_{1} = y_{1} = 0 e x_{2} = y_{2} = 1, quindi restano solo i termini senza x_{1} e y_{1}: 3·1·1 = 3;
- g_{S}(v_{1}, v_{2}): x_{1} = 0, x_{2} = 1, y_{1} = y_{2} = 1, quindi 0 + 0 + 2·1·1 + 3·1·1 = 5;
- g_{S}(v_{2}, v_{1}) = g_{S}(v_{1}, v_{2}) = 5 per simmetria, senza rifare il conto;
- g_{S}(v_{2}, v_{2}): tutte le coordinate valgono 1, quindi 1 + 2 + 2 + 3 = 8.

Quindi

[g_{S}]_{B} = ( 3 5 ; 5 8 ).

**Verifica della proposizione (alla lavagna).** Siano v = (2, 3) e w = (1, 2). Il calcolo diretto con la formula dà

g_{S}(v, w) = 2·1 + 2·2·2 + 2·3·1 + 3·3·2 = 2 + 8 + 6 + 18 = 34.

Ora con le coordinate. Si ha (2, 3) = 1·(0, 1) + 2·(1, 1), quindi [v]_{B} = (1, 2); e (1, 2) = 1·(0, 1) + 1·(1, 1), quindi [w]_{B} = (1, 1). Allora

ᵗ[v]_{B} · [g_{S}]_{B} · [w]_{B} = (1 2) · ( 3 5 ; 5 8 ) · (1, 1) = (1 2) · (8, 13) = 8 + 26 = 34.

I due risultati coincidono. Alla lavagna, per qualche secondo, qualcuno dall'aula legge il primo risultato come 36 e il docente ritocca la cifra; poi la riporta a 34 quando il secondo conto ha dato 34: il valore giusto è **34**.

![I vettori v = (2, 3) e w = (1, 2) scritti nella base v₁ = (0, 1), v₂ = (1, 1): le loro coordinate (1, 2) e (1, 1) sono ciò che serve per calcolare il loro prodotto scalare con la matrice ( 3 5 ; 5 8 ).](figure/alg/coordinate_base_b.png|9)

Una curiosità che collega l'esempio a quanto visto prima: le matrici ( 1 2 ; 2 3 ) e ( 3 5 ; 5 8 ) sono diverse, ma rappresentano **lo stesso** prodotto scalare in due basi diverse. Come si passa dall'una all'altra in generale, con la matrice del cambio di base, è il primo argomento della lezione successiva (dispense §20.A).

## A che cosa serve, secondo il docente
In chiusura (registrazione 2025) il docente mette in guardia da un'impressione sbagliata. Negli esercizi del corso i prodotti scalari sono sempre dati da formule semplici e i conti si fanno in un attimo. Nella «vita vera» calcolare direttamente un prodotto scalare può essere molto difficile (spesso coinvolge integrali), mentre il calcolo con le matrici è proprio ciò che i computer sanno fare bene. Per questo è utile poter ridurre il prodotto scalare a una matrice: basta calcolare una volta i prodotti fra i vettori della base, poi tutto il resto è algebra delle matrici.

## Il quadro dei paralleli
Durante la seconda parte della lezione il docente costruisce alla lavagna (registrazione 2025) una tabella a due colonne, una riga alla volta, che riassume i paralleli fra endomorfismi e prodotti scalari:
- **oggetto**: T : V → V lineare | g : V × V → ℝ bilineare simmetrica;
- **da una matrice**: A ∈ M(n) ⇝ L_{A} : 𝕂ⁿ → 𝕂ⁿ | S ∈ S(n) ⇝ g_{S} : ℝⁿ × ℝⁿ → ℝ;
- **l'identità**: A = I_{n} ⇝ L_{I_{n}} = applicazione identica di 𝕂ⁿ | S = I_{n} ⇝ g_{S} = prodotto scalare euclideo;
- **matrice associata**: T e una base B ⇝ [T]^{B}_{B} | g e una base B = {v_{1}, …, v_{n}} ⇝ [g]_{B} ∈ S(n);
- **base canonica**: [L_{A}]^{C}_{C} = A | [g_{S}]_{C} = S;
- **calcolo con le coordinate**: [T(v)]_{B} = [T]^{B}_{B} [v]_{B} | g(v, w) = ᵗ[v]_{B} [g]_{B} [w]_{B}.

Trabocchetto d'esame: nella formula degli endomorfismi la matrice moltiplica **una** colonna di coordinate e il risultato è un **vettore**; in quella dei prodotti scalari la matrice sta **in mezzo** fra una riga e una colonna di coordinate e il risultato è un **numero**. E [g]_{B} è sempre simmetrica, mentre [T]^{B}_{B} può essere qualsiasi.
