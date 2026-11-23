<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/26 Ottobre/26 Ottobre.pdf -->
# Algebra lineare, lezione 9: Matrici II (26 ottobre 2026): appunti a mano di Emanuele
(Trascrizione delle 2 pagine della scansione. Matrici scritte per righe, separate da «;». Tra parentesi quadre le mie note di lettura. I conti sono verificati con SymPy.)

## Pagina 1

**Matrici Parte 2**

Il determinante di una radice quadrata [sic: matrice quadrata]

**Def.** Sia A una matrice quadrata (n × n). Allora il determinante di A è
det = Σ_{σ ∈ Sₙ} sgn(σ) · a_{1σ(1)} · a_{2σ(2)} ⋯ a_{nσ(n)}
[A destra: A = (aᵢⱼ), con le frecce «i-esima riga», «j-esima colonna».]
dove Sₙ è l'insieme delle [sopra: n!] permutazioni σ di {1, 2, 3, …, n}
e sgn(σ) = ±1 è il **segno** della permutazione: se σ è composizione di k trasposizioni, allora sgn(σ) = (−1)ᵏ.
[Freccia da «trasposizioni»:] Una permutazione che [scambia] 2 elementi e lascia tutti gli altri invariati.

Scriviamo σ come [σ(1) σ(2) … σ(n)].

[riga orizzontale]

n = 1: A = (a₁₁), det A = a₁₁
n = 2: A = ( a₁₁ a₂₁ ; a₂₁ a₂₂ ) [sic: in alto a destra va a₁₂]
Le 2 permutazioni di {1, 2} sono:
- id = [1, 2]: σ(1) = 1, σ(2) = 2, sgn(id) = +1
- id = [2, 1] [sic: è σ = [2, 1], non l'identità]: σ(1) = 2, σ(2) = 1, sgn(id) = −1
det A = a₁₁a₂₂ − a₁₂a₂₁

esempio: A = ( 3 1 ; 2 4 ) ⟹ det A = 3·4 − 1·2 = 10 ✓

n = 3: A = ( a₁₁ a₁₂ a₁₃ ; a₂₁ a₂₂ a₂₃ ; a₃₁ a₃₂ a₃₃ )
3! = 6 permutazioni:
id = [1, 2, 3] → sgn(σ) = +1
[2 1 3], [3 2 1], [1 3 2] → trasposiz. sgn(σ) = −1
[2 3 1], [3 1 2] ⟹ sgn(σ) = +1
det A = a₁₁a₂₂a₃₃ − a₁₂a₂₁a₃₃ − a₁₃a₂₂a₃₁ − a₁₁a₂₃a₃₂ + a₁₂a₂₃a₃₁ + a₁₃a₂₁a₃₂

**Esempio:** A = ( 1 2 1 ; 2 1 2 ; −1 0 1 )
det A = 1 − 4 − (−1) + 0 + (−4) + 0 [= −6 ✓]

**Prop.** Se A ∈ M(n) è una matrice triangolare (superiore) [disegno: quadrato con a₁₁ … a₁ₙ in alto, zeri sotto la diagonale, aₙₙ in basso a destra]:
det A = a₁₁ a₂₂ ⋯ aₙₙ

**2 Prop.** det(ᵗA) = det(A)

**Sviluppo di Laplace**
**Teorema:** Per ogni i fissato:
det A = Σ_{j=1}^{n} (−1)^{i+j} · aᵢⱼ det Cᵢⱼ
dove Cᵢⱼ è la matrice (n−1) × (n−1) ottenuta cancellando i-esima riga e j-esima colonna.

**Es.** A = ( 1 2 1 ; 2 1 2 ; −1 0 1 )
Sviluppo lungo la 1ª riga (i = 1):
det A = (−1)²·a₁₁·det C₁₁ + (−1)³ a₁₂ det C₁₂ + (−1)⁴ a₁₃ det C₁₃
= 1·det( 1 2 ; 0 1 ) − 2 det( −2 2 ; 1 1 ) + 1·det( 2 1 ; −1 0 ) = 1 − 2·4 + 1 = −6
[La seconda sottomatrice è scritta male: C₁₂ = ( 2 2 ; −1 1 ), con det = 4 (quello usato nel conto); la matrice scritta, ( −2 2 ; 1 1 ), avrebbe det −4. Il risultato −6 è giusto.]

## Pagina 2

Sviluppo lungo la 3ª riga:
det A = (−1) det( 2 1 ; 1 2 ) + 0 + 1·det( 1 2 ; 2 1 ) = −3 − 3 = −6 ✓

[Il resto della pagina è vuoto.]
