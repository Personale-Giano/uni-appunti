<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/14 Ottobre/14 Ottobre.pdf -->
# Algebra lineare, lezione 5: Spazi vettoriali I (14 ottobre 2026): appunti a mano di Emanuele
(Trascrizione della pagina unica della scansione. I vettori colonna sono scritti (x₁, …, xₙ). Le parti indicate «foto» rimandano a foto della lavagna che non sono nella scansione. Tra parentesi quadre le mie note di lettura.)

## Pagina 1

**L5 Spazi Vettoriali**

**Lo Spazio Euclideo**
**Def:** Lo spazio Euclideo n-dimensionale è ℝⁿ = {(x₁, …, xₙ) | x₁, …, xₙ ∈ ℝ}.
es. n = 1 → ℝ¹ = {(x) | x ∈ ℝ} = ℝ
n = 2 → ℝ² = {(x, y) | x, y ∈ ℝ}
ℝ² ∋ (x, y) ⟷ [disegno: punto nel piano con le coordinate x e y tratteggiate]
n = 3 → ℝ³ = {(x, y, z) | x, y, z ∈ ℝ} ∋ (1, 2, 3) ⟷ [disegno: assi x, y, z e il parallelepipedo che individua P(1, 2, 3)]

**Operazioni in ℝⁿ**
SOMMA: date v = (x₁, …, xₙ), w = (y₁, …, yₙ) definiamo v + w = (x₁ + y₁, …, xₙ + yₙ) → la somma è una funzione + : ℝⁿ × ℝⁿ → ℝⁿ, (v, w) ↦ v + w.
MOLTIPLICAZIONE PER ℝ: v = (x₁, …, xₙ) ∈ ℝⁿ, a ∈ ℝ ⟹ a·v = a(x₁, …, xₙ) = (ax₁, …, axₙ).
La moltiplicazione è una funzione · : ℝ × ℝⁿ → ℝⁿ, (a, v) ↦ a·v.

**Def:** Dato un campo 𝕂, uno spazio VETTOR. su 𝕂 è un insieme V con operazioni + : V × V → V, (v, w) ↦ v + w, e · : 𝕂 × V → V, (a, v) ↦ v·w [sic: sta per a·v], tali che:
[In rosso:] 4 Proprietà: foto 11:37 + 5, 6, 7 foto 11:43
8) ∀ v ∈ V, 1·v = v

**NOTAZIONI / DEFINIZIONI**
**Def ①:** Un insieme V con + : V × V → V che soddisfi le prop. 1, 2, 3 è detto **gruppo**.
**Def ②:** Se un gruppo soddisfa la prop. 4 è detto **commutativo / abeliano**.
**Def ③:** Dato V spazio vettoriale su 𝕂 ⟹ i v ∈ V sono chiamati VETTORI, gli a ∈ 𝕂 sono chiamati SCALARI.
**Def ④: Proposizione.** V sp. vettoriale su 𝕂.
- 0_V è UNICO, e ∀ v ∈ V 0·v = 0_V.
- ∀ v ∈ V, −v è UNICO, e −v = (−1)·v.

[In rosso:] D'ora in poi useremo notazioni v + w, a·v per le operazioni in V.

**Esempi:**
ℝⁿ con le operazioni +, · definite prima, [fine della pagina]
