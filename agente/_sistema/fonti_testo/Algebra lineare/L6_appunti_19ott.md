<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/19 Ottobre/19 Ottobre.pdf -->
# Algebra lineare, lezione 6: Spazi vettoriali II (19 ottobre 2026): appunti a mano di Emanuele
(Trascrizione delle 3 pagine della scansione. Matrici scritte per righe, separate da «;». Le parti indicate «foto» rimandano a foto della lavagna che non sono nella scansione. Tra parentesi quadre le mie note di lettura. Gli evidenziatori gialli sono segnalati.)

## Pagina 1

**Spazi Vettoriali (Parte 2)**

**Ci ricordiamo:** V insieme
+ : V × V → V, (v, w) ↦ v + w
· : 𝕂 × V → V, (λ, v) ↦ λv   [freccia su 𝕂: «campo»]
+ «tante» proprietà

es. 𝕂, 𝕂ⁿ, succ. in 𝕂, [0, 1] → 𝕂 funzioni, 𝕂[x], ecc.

es. Lo spazio delle matrici:
**Def.** Sia 𝕂 un campo fissato.
Una **matrice** con m righe e n colonne è una «tabella rettangolare» della forma
A = ( a₁₁ a₁₂ … a₁ₙ ; a₂₁ … ; ⋮ ; a_m1 … a_mn )  con aᵢⱼ ∈ 𝕂 (1 ≤ i ≤ m, 1 ≤ j ≤ n)
⚠ aᵢⱼ denota l'elemento nella i-esima riga e j-esima colonna.
⚠ Prima denotiamo le righe e poi le colonne.
Denotiamo l'insieme delle matrici di questo tipo con M(m, n, 𝕂) [frecce: m righe, n colonne].
Un elemento A ∈ M(m, n, 𝕂) chiamiamo una matrice m × n.

es.
( 1, 2, 3 ; 4, 5, 6 ; 7, 8, 9 ) ∈ M(3, 3, ℕ)
[ℕ non è un campo: va letta come M(3, 3, ℝ) (o ℚ).]
( 1 7 √2 ; 3 π i ) ∈ M(2, 3, ℂ)
(1, 7, −2) = (1 7 −2) ∈ M(1, 3, ℝ)
(7, √2, π) [colonna] ∈ M(4, 1, ℝ) = ℝ³ → 3 righe (solo quando c'è una sola colonna)
[ERRORE: la colonna ha 3 entrate, quindi è in M(3, 1, ℝ) = ℝ³; «4» è una svista.]

Se A, B sono due matrici m × n (stessa taglia) allora (A + B)ᵢⱼ = aᵢⱼ + bᵢⱼ.
es. foto 11:33
Se λ ∈ 𝕂 allora λA è la matrice con entrate (λA)ᵢⱼ = λ·aᵢⱼ.
foto 11:35

**Prop:** M(m, n, 𝕂) è uno spazio vettoriale su 𝕂.

**Sottospazio Vettoriale**
**Def:** Sia V uno spazio vettoriale.
Un sottospazio di V è un sottoinsieme W ⊆ V con 3 proprietà:
1. 0 = 0_V ∈ W   [0_W = 0_V]
2. Se v, w ∈ W ⟹ v + w ∈ W   [sotto «v + w»: def. in V]
3. Se v ∈ W, λ ∈ 𝕂 ⟹ λv ∈ W   [sotto «λv»: def. in V]

## Pagina 2

es. V = ℝ³ = {(a, b, c) | a, b, c ∈ ℝ}
W₁ = {(a, b, 0) | a, b ∈ ℝ}
W₂ = {(a, b, 1) | a, b ∈ ℝ}
W₁, W₂ sono sottoinsiemi di V. Sono sottospazi?
Per W₁:
1) 0 = (0, 0, 0) ∈ W₁ ✓
2) Se v = (a, b, 0), w = (c, d, 0) ∈ W₁ ⟹ v + w = (a + c, b + d, 0) ∈ W₁ ✓
3) Se v = (a, b, 0), λ ∈ ℝ → λv = (λa, λb, 0) ∈ W ✓
} → W₁ è un sottospazio di V = ℝ³
Per W₂: foto 11:50 ~ **NO** [cerchiato]

es. 𝕂_k[x] = {polinomi in 𝕂[x] con grado ≤ k} è un sottospazio di 𝕂[x].

es. Matrici diagonali, triangolari, simmetriche e antisimmetriche.
**Def:** Una matrice n × n (# righe = # colonne) è detta **quadrata**. Per una tale matrice A diciamo che A è:
- **Diagonale:** se aᵢⱼ = 0 ∀ i ≠ j.  A = ( a₁₁ 0 0 ; 0 a₂₂ 0 ; 0 0 a₃₃ ) è diagonale [diagonale evidenziata in giallo].
- **Triangolare superiore:** se aᵢⱼ = 0 ∀ i > j.  A = ( a₁₁ a₁₂ a₁₃ ; a₂₂ a₂₃ ; a₃₃ ) tr. sup. [triangolo evidenziato in giallo; a destra un quadrato con il triangolo disegnato al contrario, con la freccia «no»]. [Nel foglio la seconda riga è scritta «a₂₁ a₂₃»: sta per a₂₂ a₂₃.]
- **Triangolare inferiore:** se aᵢⱼ = 0 ∀ i < j.
- **Triangolare:** se è o tr. sup. o tr. inf.
- **Simmetrica:** se aᵢⱼ = aⱼᵢ ∀ i, j.
- **Antisimmetrica:** se aᵢⱼ = −aⱼᵢ ∀ i, j.

es.
( 1 0 ; 0 −1 ) diag.
( 1 2 ; 0 3 ) è triangolare sup.
( 7 0 ; √2 −1 ) tr. inf.
( 1 √2 ; √2 3 ) simmetrica
( 0 π ; −π 0 ) antisimmetrica
( 0 0 ; 0 1 ) è diag, tr. sup, tr. inf, simm, ma non anti-simm!
( 0 0 ; 0 0 ) è simm e anti-simm.
( 1 2 ; 3 4 ) non è diag, triang, simm, antisimm.

## Pagina 3

**Notazione**
Gli elementi a₁₁, a₂₂, a₃₃, …, aₙₙ formano la diagonale (principale).
M(n) = M(n, 𝕂) = M(n, n, 𝕂) = {matrici quadrate}
D(n) = {matrici diag in M(n)}
Tˢ(n) = {matrici tr. sup. in M(n)}
Tⁱ(n) = {matrici tr. inf. in M(n)}
S(n) = {matrici simm. in M(n)}
A(n) = {matrici antisimm. in M(n)}

**Prop.** D(n), Tˢ(n), Tⁱ(n), S(n), A(n) sono sottospazi di M(n).

**Combinazioni lineari e sottospazio generato**
Sia V uno spazio vettoriale e v₁, v₂, …, v_k alcuni vettori in V.
Una combinazione lineare di v₁, …, v_k è un vettore v = λ₁v₁ + λ₂v₂ + … + λ_kv_k per qualche λ₁, …, λ_k ∈ 𝕂.
es. foto 12:6 [12:06], 12:11

[Il resto della pagina è vuoto.]
