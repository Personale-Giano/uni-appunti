<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/18 Novembre/Quadretti - Grande.pdf -->
# Algebra lineare, lezione 18: Autovalori e autovettori II (18 novembre 2026): appunti a mano di Emanuele
(Trascrizione delle 4 pagine del PDF «Quadretti - Grande.pdf», che è la lezione del 18 nov; fatta il 23 nov 2026. Vettori colonna in linea come (a ; b ; c); matrici riga per riga. Tra parentesi quadre le note di lettura. «es. in Foto 12:52» rimanda a una foto della lavagna che non è nel PDF.)

## Pagina 1
**Lezione 18: Autovalori e Autovettori II**

A ∈ M(n) → Un **Autovettore** è v ∈ 𝕂ⁿ, v ≠ 0 t.c. Av = λv  [freccia su λ: «Autovalore associato»]

**Prop.** λ è un a.val. di A sse è una radice di P_A(t) = det(A − tI)  [freccia: «Pol. di grado n»]

**es.**

```
    ⎛ 1 0 0 ⎞
A = ⎜ 1 2 0 ⎟     calcoliamo autoval. (e 1 autovettore)
    ⎝ 2 1 3 ⎠

                        ⎛ 1−t   0    0  ⎞
P_A(t) = det(A − tI) = det ⎜  1   2−t   0  ⎟ = (1 − t)(2 − t)(3 − t)      Autovalori: 1, 2, 3
                        ⎝  2    1   3−t ⎠
```

[Nel foglio l'elemento centrale sembra «2t»: il segno meno è appena visibile; il prodotto finale è quello giusto.]

[in blu] **Per A ∈ M(n) triangolare, gli autovalori sono gli elementi sulla diagonale**

per λ = 3 ⟹ Autovettori?
v = (x ; y ; z) t.c. Av = 3v ⟷ (A − 3I_3) · v = 0

```
⎛ −2  0 0 ⎞ ⎛ x ⎞      ⎧ −2x      = 0        x = 0
⎜  1 −1 0 ⎟ ⎜ y ⎟  →   ⎨ x − y    = 0   →    y = 0
⎝  2  1 0 ⎠ ⎝ z ⎠      ⎩ 2x + y   = 0        z = z → Valore libero
```

→ Autovettori = {(0 ; 0 ; z) | z ∈ ℝ, z ≠ 0} = Span((0 ; 0 ; 1))
[A rigore lo Span contiene anche lo zero, che non è un autovettore. Conti verificati con SymPy: gli autospazi sono V_1 = Span((−2 ; 2 ; 1)), V_2 = Span((0 ; −1 ; 1)), V_3 = Span((0 ; 0 ; 1)); negli appunti c'è solo V_3.]

A è **diagonalizzabile** se:
• ∃ base di autovettore
• A è simile a D = diag(λ_1, …, λ_n) → [nota di Emanuele:] «Matr diagonale/triangolare, non ricordo»
[È diagonale: A è diagonalizzabile se e solo se è simile a una matrice diagonale (cap. 60).]

**Prop.** Siano v_1, …, v_k autovettori di A, con autovalori distinti ⟹ v_1, …, v_k sono linearmente indipendenti.

**Corollario** Sia A ∈ M(n) con n autovalori distinti ⟹ A è diagonalizzabile.

**Dim.** Siano λ_1, …, λ_n autovalori distinti.
λ_i ⇝ scegliamo un autovett. v_i ∈ 𝕂ⁿ ⇝ B = {v_1, …, v_n} ⊆ 𝕂ⁿ → è lin. ind. per la prop. precedente ⟹ B è una base di autovettori.

## Pagina 2
**Molteplicità di una matrice**
data A ∈ M(n), e λ autovalore di A, definiamo L'**AUTOSPAZIO** di A con autovalore λ, come:
V = Ker(A − λI) = {v ∈ 𝕂ⁿ | (A − λI) · v = 0} = {autovettori di A autovalore λ} ∪ {0}
[«V =» va letto V_λ =.]

V_λ è uno spazio vettoriale
- La **molteplicità Geometrica** di λ come m_g(λ) = dim V_λ
- La **molteplicità Algebrica** di λ come m_a(λ) = molteplicità di λ come radice di P_A(t)

**Oss.** m_a(λ) = massimo k t.c. (t − λ)ᵏ divide P_A(t)

**es.** nell'esempio precedente

```
    ⎛ 1 0 0 ⎞
A = ⎜ 1 2 0 ⎟        P_A(t) = (1 − t)(2 − t)(3 − t) = −(t − 1)(t − 2)¹(t − 3)
    ⎝ 2 1 3 ⎠
```

| λ | m_g(λ) | m_a(λ) |
|---|---|---|
| 1 | | 1 |
| 2 | | 1 |
| 3 | m_g(3) = dim V_3 = 1 | 1 |

λ = 3 → Ker(A − 3I_3) = Span((0 ; 0 ; 1)) = V_3
[Le caselle m_g(1) e m_g(2) sono vuote nel foglio: valgono 1, perché 1 ≤ m_g ≤ m_a = 1 (pagina 3).]

**es.** A = ( 1 1 ; 0 1 ) → Autovalori: 1  [freccia: «Compare 2 volte»]
P_A(t) = det( 1−t  1 ; 0  1−t ) = (1 − t)² ⟶ m_a(1) = 2
m_g(1) = dim Ker(A − 1I) = {y ∈ ℝ² | ( 0 1 ; 0 0 )(x ; y) = (0 ; 0)}  [freccia su A − I = ( 0 1 ; 0 0 )]
{ y = 0 ; 0 = 0 } ⟹ y = 0, x = x ⟹ V_1 = {(x ; 0) | x ∈ ℝ} = Span((1 ; 0))  [sotto: x(1 ; 0)]
m_g(1) = dim V_1 = 1;  m_g(1) = 1 ≠ 2
[«{y ∈ ℝ² | …}» va letto {v ∈ ℝ² | …}, e «m_g(1) = dim Ker(…) = {…}» uguaglia una dimensione a un insieme: la dimensione è quella dell'insieme scritto. «1 ≠ 2» confronta m_g(1) con m_a(1).]

A ∈ M(n) → λ autovalore di A se P_A(λ) = 0

## Pagina 3
**Oss.** m_g(λ) = dim Ker(A − λI) = n − dim Im(A − λI)  [freccia: «teor. della dim»]
↳ = n − rg(A − λI)  [freccia su n: «num righe e colonne di A»]

**Prop.** λ autovalore di A ⟹ 1 ≤ m_g(λ) ≤ m_a(λ)
In particolare, se m_a(λ) = 1 ⟹ m_g(λ) = 1

**Def.** Sia V sp. vettoriale, e V_1, …, V_m ⊆ V sottospazi. Diremo che V_1, …, V_m sono in **somma diretta**, e scriveremo V = V_1 + V_2 + … + V_m, se ∀ v si può scrivere in modo unico come:
v = v_1 + v_2 + … + v_m dove v_i ∈ V_i
[Negli appunti la somma diretta è scritta con «+» invece di ⊕, qui e nelle due proposizioni seguenti; il simbolo ⊕ compare solo a pagina 4.]

**Prop.** Se V = V_1 + … + V_m allora
1) dim V = dim V_1 + dim V_2 + … + dim V_m
2) Date basi B_1 ⊆ V_1, …, B_m ⊆ V_m allora ⟹ B = B_1 ∪ … ∪ B_m è base di V
[Nel foglio «B_1 ∈ V_1, B_m ∈ V_m»: sono basi, cioè sottoinsiemi.]

**Prop.** Siano λ_1, …, λ_n autovalori distinti di A ∈ M(n) e sia W ∈ 𝕂ⁿ,
W = V_λ1 + … + V_λm = {v ∈ 𝕂ⁿ | v = v_1 + … + v_m}
Allora W = V_λ1 + … + V_λm
[Letta così la proposizione sembra una tautologia: la tesi è che la somma degli autospazi è diretta, W = V_λ1 ⊕ … ⊕ V_λm. Inoltre gli autovalori sono λ_1, …, λ_m (non λ_n), W ⊆ 𝕂ⁿ e i v_i stanno in V_λi.]

**Cor.** A ∈ M(n) è diagonalizzabile sse 𝕂ⁿ = V_λ1 + … + V_λm  [λ_1 … λ_m autovalori di A]
[Anche qui la somma è diretta, ⊕.]

**Prop.** A ∈ M(n) con autovalori λ_1, …, λ_m. Allora A è diagonalizzabile sse:
1) P_A(t) ha esattamente n radici contate con moltepl. (m_a(λ_1) + … + m_a(λ_m) = n)
2) ∀ λ_i, m_g(λ_i) = m_a(λ_i)

## Pagina 4
**Dim:** ① + ② ⟹ m_g(λ_1) + … + m_g(λ_m) = n
⟹ 𝕂ⁿ = V_λ1 ⊕ … ⊕ V_λm ⟹ Prendiamo B_i ⊆ V_λi e prendiamo B = B_1 ∪ B_2 ∪ … ∪ B_m ⊆ 𝕂ⁿ base di autovettori
[È solo la direzione «⟸» del teorema.]
—————————————
**es.** in Foto 12:52
[Fine degli appunti.]
