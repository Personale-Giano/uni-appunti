<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/28 Ottobre/28 Ottobre.pdf -->
# Algebra lineare, lezione 10: Matrici III (28 ottobre 2026): appunti a mano di Emanuele
(Trascrizione delle 3 pagine della scansione. Il contenuto è lo stesso di `_sistema/fonti/Appunti/28 Ottobre.pdf`, già usato per i cap. 34-37 ma mai trascritto: le due scansioni differiscono solo per la compressione. Matrici scritte per righe, separate da «;»; Aʲ è la j-esima colonna. Tra parentesi quadre le mie note di lettura. I conti sono verificati con SymPy.)

## Pagina 1

**Lez 10 Matrici 3**

**Determinante** A ∈ M(n)
⟹ det A = Σ_{σ ∈ Sₙ} sgn(σ) a_{1σ(1)} ⋯ a_{nσ(n)}
det( a b ; c d ) = ad − bc,   det( a₁₁ 0 ; ⋱ ; a_n1 aₙₙ ) = a₁₁ a₂₂ ⋯ aₙₙ [triangolare inferiore]

**Sviluppo di Laplace** [titolo verde; la formula sotto è in realtà la proprietà del fattore comune su una colonna]
det(A¹ | λAⁱ | Aⁿ) = λ det(A¹ | Aⁱ | Aⁿ)

det( 5i 4√2 0 √2 ; 5i 8√2 0 −√2 ; −5i −4√2 −1 2√2 ; −10i 4√2 1 √2 ) = 5i · 4 · √2 · √2 · det( 1 1 0 1 ; 1 2 0 −1 ; −1 −1 −1 2 ; −2 1 1 1 )
[sotto le colonne 1, 2 e 4: 5i(1, 1, −1, −2), 4√2(1, 2, −1, 1), √2(1, −1, 2, 1)]
[A destra la scacchiera dei segni: + − + ; − + − ; + − + ; … −]
= 40i ( −1 · det( 1 1 1 ; 1 2 −1 ; −2 1 1 ) + ( −1 det( 1 1 1 ; 1 2 −1 ; −1 −1 2 ) ) )
[Il conto si ferma qui. I due determinanti 3 × 3 valgono 9 e 3, quindi il risultato è 40i · (−9 − 3) = −480i (verificato).]

**Interpretazione Geometrica**
In ℝ²: A ∈ M(2), A = (A¹ | A²), A¹, A² ∈ ℝ².
[Disegno: parallelogramma P di lati A¹ e A².] Area(P) = |det A|

In ℝ³: A ∈ M(3), A = (A¹ | A² | A³), A¹, A², A³ ∈ ℝ³.
[Disegno: parallelepipedo tratteggiato in rosso di spigoli A¹, A², A³; a sinistra «Contenuto in un parallelepipedo».] |det A| = Vol(P)

**Proprietà del Determinante**
Sia A una M(n):
1) Se A′ è ottenuta da A scambiando due righe/colonne ⟹ det A′ = −det A
2) Se A′ è ottenuta da A moltiplicando una riga o colonna per λ ∈ 𝕂 ⟹ det A′ = λ det A
3) Se A′ è ottenuta da A aggiungendo ad una riga/colonna il multiplo di un'altra ⟹ det A′ = det A
⤷ det(A¹ | … | Aⁱ + λAʲ | … | Aⁿ) = det(A¹ | … | Aⁿ)   [sotto: i-esima colonna]

## Pagina 2

es. A = ( 1 1 ; 0 2 ) [colonne A¹, A²] →(C₂ → C₂ + C₁) ( 1 2 ; 0 2 )
det( 1 1 ; 0 2 ) = det( 1 2 ; 0 2 ), cioè Vol(P₁) = Vol(P₂)
[Disegno: i parallelogrammi P₁ (lati A¹, A²) e P₂ (lati A¹, A¹ + A²), con stessa base e stessa altezza.]

Le 3 TRASFORMAZIONI SOPRA SI CHIAMANO MOSSE DI GAUSS:
1) Cᵢ ⟷ Cⱼ   2) Cᵢ → λCᵢ   3) Cᵢ → Cᵢ + λCⱼ (j ≠ i)

[Freccia dalla 3:] **Prop:** Se A ∈ M(n) ha delle colonne linearmente dipendenti ⟷ det A = 0.
es. A = ( 1 3 7 ; 1 3 5 ; 1 3 10 ): det( 1 3 7 ; 1 3 5 ; 1 3 10 ) = det( 1 0 7 ; 1 0 5 ; 1 0 10 ) = 0
[↑ C₂ = C₂ − 3C₁; ↘ colonna di 0 → det = 0]

In generale la 3ª mossa di Gauss può introdurre zeri.
es. det( 1 3 7 ; 1 5 5 ; 1 4 10 ) =(C₂ − 3C₁) det( 1 0 7 ; 1 2 5 ; 1 1 10 ) =(C₃ = C₃ − 7C₁) det( 1 0 0 ; 1 2 −2 ; 1 1 3 ) = 1 · det( 2 −2 ; 1 3 ) = 6 − (−2) = 8 ✓

**Inversa di una matrice**
A, B ∈ M(n) ⟹ A·B ∈ M(n).    Iₙ = ( 1 ⋯ 0 ; ⋱ ; 0 ⋯ 1 ) matrice identità
**Prop:** ∀ A ∈ M(n): A·Iₙ = Iₙ·A = A

**Def:** Dato A ∈ M(n), A è detta INVERTIBILE se ∃ B ∈ M(n) t.c. AB = BA = Iₙ.
In tal caso, B è detta INVERSA di A e B = A⁻¹.

1. Quand'è che A è invertibile?
**Prop. (Teorema di Binet)** ∀ A, B ∈ M(n), det(AB) = (det A)·(det B).
Supponiamo che A sia invertibile ⟹ ∃ A⁻¹ t.c. A·A⁻¹ = Iₙ
(det A)(det A⁻¹) = det(A·A⁻¹) = det(Iₙ) = 1 ⟹ det A ≠ 0, e det A⁻¹ = 1/det A

2. Come calcoliamo l'inversa?
**Def.** Data A ∈ M(n), definiamo i cofattori di A: cofᵢⱼ, 1 ≤ i, j ≤ n
cofᵢⱼ = (−1)^{i+j} · det(Cᵢⱼ)   [Cᵢⱼ: ottenuta da A cancellando riga i e colonna j]
La matrice dei cofattori è cof(A) ∈ M(n) t.c. cof(A)ᵢⱼ = cofᵢⱼ.

**Teorema**
Se A ∈ M(n) ha det ≠ 0 allora è invertibile: [riquadrato in rosso] A⁻¹ = (1/det A) · ᵗcof(A)
es. A = ( a b ; c d ):
1) cof(A) = ( d −c ; −b a )
2) A⁻¹ = (1/det A) · ᵗcof(A) = (1/(ad − bc)) · ᵗ( d −c ; −b a ) = (1/(ad − bc)) ( d −b ; −c a )
→ Si può fare velocemente scambiando i 2 sulla diag. princ. e cambiando il segno della diag. secondaria.

## Pagina 3

es. A = ( 1 0 1 ; 0 2 1 ; 3 0 0 ). Calcoliamo cof(A) e A⁻¹.
Invertibile? → calcolo det A: det A = +3·(−2) = −6 ≠ 0
cof(A) = ( cof₁₁ cof₁₂ … ; … cof₃₃ ) → cof(A) = ( 0 3 −6 ; 0 3 0 ; −2 −1 2 )
A⁻¹ = (1/(−6)) · ᵗcof(A) = −(1/6) · ( 0 0 −2 ; 3 3 1 ; −6 0 2 )

cof₁₁ = + det( 2 1 ; 0 0 ) = 0
cof₁₂ = − det( 0 1 ; 3 0 ) = +3
cof₁₃ = + det( 0 2 ; 3 0 ) = −6
cof₂₁ = − det( 0 1 ; 0 0 ) = 0
cof₂₂ = + det( 1 1 ; 3 0 ) = −3
cof₂₃ = − det( 1 0 ; 3 0 ) = 0
cof₃₁ = + det( 0 1 ; 2 1 ) = −2
cof₃₂ = − det( 1 1 ; 0 1 ) = −1
cof₃₃ = + det( 1 0 ; 0 2 ) = 2

[ERRORI DI COPIATURA: i nove cofattori sono giusti, ma nella matrice cof(A) il cof₂₂ è scritto 3 invece di −3, e nella trasposta la seconda riga è scritta (3, 3, 1) invece di (3, −3, −1). Giusti (SymPy): cof(A) = ( 0 3 −6 ; 0 −3 0 ; −2 −1 2 ), ᵗcof(A) = ( 0 0 −2 ; 3 −3 −1 ; −6 0 2 ), A⁻¹ = ( 0 0 1/3 ; −1/2 1/2 1/6 ; 1 0 −1/3 ).]

[Il resto della pagina è vuoto.]
