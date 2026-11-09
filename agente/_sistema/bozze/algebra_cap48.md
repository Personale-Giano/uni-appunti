# 48. Il Teorema della Dimensione ed Esercizi
## Il teorema
**Teorema (della dimensione).** Sia f : V → W un'applicazione lineare. Se V ha dimensione finita n, allora

dim Ker f + dim Im f = n.

(In parole povere: le n dimensioni dello spazio di partenza si dividono in due parti. Quelle che f schiaccia sullo zero formano il nucleo; quelle che sopravvivono diventano l'immagine. Più grande è il nucleo, più piccola è l'immagine.)

**Idea della dimostrazione.** Si prende una base v_{1}, …, v_{k} di Ker f e la si completa a una base v_{1}, …, v_{n} di V. Allora f(v_{k+1}), …, f(v_{n}) formano una base di Im f. Quindi dim Im f = n − k, e la formula segue. La dimostrazione completa non viene svolta: che quei vettori generino Im f viene dall'osservazione del cap. 47, perché f(v_{1}) = … = f(v_{k}) = 0. A lezione (registrazione 2024) il teorema è enunciato senza dimostrazione, e senza scrivere l'ipotesi che V abbia dimensione finita; il docente osserva che nucleo e immagine «non sono indipendenti»: il teorema dice qual è il legame tra le loro dimensioni.

**Esempio dalla lavagna (registrazione 2024), completato.** Per A = ( 1 0 2 ; 1 2 4 ) e L_{A}(x, y, z) = (x + 2z, x + 2y + 4z) (cap. 46) a lezione si calcola solo L_{A}(1, 1, 1) = (3, 7). Il teorema si può controllare così. Il nucleo è dato da x + 2z = 0 e x + 2y + 4z = 0; sottraendo, 2y + 2z = 0, quindi y = −z e x = −2z: Ker L_{A} = Span((−2, −1, 1)), di dimensione 1. Le colonne (1, 1) e (0, 2) sono già indipendenti, quindi rk(A) = 2 e Im L_{A} = ℝ². Controllo: 1 + 2 = 3 = dim ℝ³.

## Il collegamento con Rouché-Capelli
Per L_{A} : 𝕂ⁿ → 𝕂^{m}, il nucleo è

Ker L_{A} = {x ∈ 𝕂ⁿ | Ax = 0} = S_{0},

lo spazio delle soluzioni del sistema omogeneo Ax = 0 (cap. 41). Poiché dim Im L_{A} = rk(A) (cap. 47), il teorema della dimensione diventa

dim S_{0} = n − rk(A),

che è proprio il teorema di Rouché-Capelli per i sistemi omogenei (cap. 42).

**Alla lavagna (registrazione 2024)** questo è il punto d'arrivo della lezione, scritto in tre righe: dim Im L_{A} = rk(A) e dim 𝕂ⁿ = n, il numero di colonne di A; Ker L_{A} = {x ∈ 𝕂ⁿ | Ax = 0} = S_{0}, lo spazio delle soluzioni del sistema (A | 0); quindi dim S_{0} + rk(A) = n, cioè dim S_{0} = n − rk(A), «e questo è Rouché-Capelli». Il docente insiste che un elemento del nucleo è esattamente una soluzione del sistema omogeneo: scrivere Ax = 0 vuol dire chiedere che tutte le componenti a_{i1}x_{1} + … + a_{in}x_{n} siano nulle.

## Conseguenze per iniettività e suriettività
**Corollario.** Sia f : V → W un'applicazione lineare, con V di dimensione finita. Allora dim Im f ≤ dim V. Inoltre:
- (1) f è iniettiva se e solo se dim Im f = dim V;
- (2) f è suriettiva se e solo se dim Im f = dim W.

(In parole povere: un'applicazione lineare non può «allargare» lo spazio: l'immagine è al massimo grande quanto la partenza. È iniettiva quando non perde dimensioni, suriettiva quando riempie tutto l'arrivo.)

**Dimostrazione.** Dal teorema, dim Im f = dim V − dim Ker f ≤ dim V. A lezione (registrazione 2024), a differenza del teorema, il corollario è dimostrato con due catene di equivalenze:
- (1) dim Im f = dim V ⟺ dim Ker f = 0 (dal teorema) ⟺ Ker f = {0} (uno spazio ha dimensione 0 solo se contiene solo lo zero) ⟺ f iniettiva (cap. 47);
- (2) dim Im f = dim W ⟺ Im f = W ⟺ f suriettiva. Il passaggio centrale usa Im f ⊆ W: una base del sottospazio è fatta di dim W vettori indipendenti di W, quindi è una base di W (cap. 26).

**Come sottolineato a lezione (registrazione 2024).** Questo corollario dà buoni metodi per verificare iniettività o suriettività «senza andare neanche a toccare la funzione»: bastano uguaglianze tra numeri interi, le dimensioni, e il docente aggiunge che a volte può essere estremamente utile.

Per esempio, una funzione lineare ℝ³ → ℝ² non può essere iniettiva, perché Im f è un sottospazio di ℝ², quindi dim Im f ≤ 2 < 3 = dim ℝ³. Una funzione lineare ℝ² → ℝ³ non può essere suriettiva, perché l'immagine ha dimensione al massimo 2 < 3.

## Esercizi
Svolgimenti non presenti nelle dispense né in lezione.

**Esercizio 14.14.** Per ogni funzione verificare che è lineare, trovare nucleo e immagine e controllare il teorema della dimensione.

**1.** f_{1} : ℝ³ → ℝ², f_{1}(x, y, z) = (x + y + z, 2x + 3y + 4z). È L_{A} con A = ( 1 1 1 ; 2 3 4 ), quindi è lineare. Il nucleo è dato dal sistema x + y + z = 0, 2x + 3y + 4z = 0. Con R_{2} → R_{2} − 2R_{1} la seconda equazione diventa y + 2z = 0, cioè y = −2z, e dalla prima x = −y − z = z. Quindi Ker f_{1} = Span((1, −2, 1)), di dimensione 1. La matrice ha due pivot, quindi rk(A) = 2 e Im f_{1} è un sottospazio di ℝ² di dimensione 2, cioè tutto ℝ². Controllo: 1 + 2 = 3 = dim ℝ³.

**2.** f_{2} : ℝ_{2}[x] → ℝ, dove ℝ_{2}[x] sono i polinomi di grado al massimo 2, f_{2}(p(x)) = p(1) + p(−1). È lineare perché valutare in un punto rispetta somme e multipli: (p + q)(1) = p(1) + q(1) e (λp)(1) = λp(1), e lo stesso in −1. Con p(x) = a + bx + cx² si ha p(1) + p(−1) = (a + b + c) + (a − b + c) = 2a + 2c. Il nucleo è dato da a = −c: sono i polinomi bx + c(x² − 1), quindi Ker f_{2} = Span(x, x² − 1), di dimensione 2. L'immagine è tutto ℝ, perché per esempio, per il polinomio costante 1, f_{2}(1) = 1 + 1 = 2 ≠ 0 e un sottospazio non nullo di ℝ è ℝ. Controllo: 2 + 1 = 3 = dim ℝ_{2}[x].

**3.** f_{3} : M(2, ℝ) → M(2, ℝ), f_{3}(A) = A − ᵗA. È lineare perché la trasposta lo è: ᵗ(A + B) = ᵗA + ᵗB e ᵗ(λA) = λᵗA. Infatti f_{3}(A + B) = (A + B) − ᵗ(A + B) = (A − ᵗA) + (B − ᵗB) = f_{3}(A) + f_{3}(B), e f_{3}(λA) = λA − ᵗ(λA) = λ(A − ᵗA) = λf_{3}(A). Il nucleo è fatto delle matrici con A = ᵗA, cioè delle simmetriche S(2), di dimensione 3. L'immagine è fatta di matrici antisimmetriche, perché ᵗ(A − ᵗA) = ᵗA − A = −(A − ᵗA). Non è nulla: con A = ( 0 1 ; 0 0 ) si ottiene ( 0 1 ; −1 0 ). Le antisimmetriche 2 × 2 sono i multipli di questa matrice, quindi Im f_{3} = A(2), di dimensione 1. Controllo: 3 + 1 = 4 = dim M(2, ℝ).

**Esercizio 14.15.** Sia f : ℝ⁴ → ℝ³, f(x_{1}, x_{2}, x_{3}, x_{4}) = (x_{1} + x_{2} + x_{3}, x_{2} + x_{3} + x_{4}, x_{1} − x_{4}). Trovare una base di Ker f, la dimensione e una base di Im f, e stabilire se f è iniettiva o suriettiva.

La matrice è A = ( 1 1 1 0 ; 0 1 1 1 ; 1 0 0 −1 ). Con R_{3} → R_{3} − R_{1} e poi R_{3} → R_{3} + R_{2} la terza riga si annulla: ( 1 1 1 0 ; 0 1 1 1 ; 0 0 0 0 ). Quindi rk(A) = 2.

**1.** Le colonne di x_{3} e x_{4} non hanno pivot: si pone x_{3} = s e x_{4} = t. Dalla seconda riga x_{2} = −s − t, dalla prima x_{1} = −x_{2} − x_{3} = t. Le soluzioni sono s(0, −1, 1, 0) + t(1, −1, 0, 1), quindi una base di Ker f è (0, −1, 1, 0), (1, −1, 0, 1).

**2.** Per il teorema della dimensione, dim Im f = 4 − dim Ker f = 4 − 2 = 2.

**3.** L'immagine è generata dalle colonne. Le colonne con i pivot, la prima e la seconda, sono indipendenti, quindi una base di Im f è (1, 0, 1), (1, 1, 0).

**4.** f non è iniettiva, perché il nucleo non è {0}. Non è suriettiva, perché dim Im f = 2 < 3 = dim ℝ³.
