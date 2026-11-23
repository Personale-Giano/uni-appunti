<!-- fonte: _sistema/fonti/Appunti/Mate_2026/tutorato/Tutorato 1 scheda.pdf -->
# Matematica discreta, tutorato 1: appunti a mano di Emanuele sulla scheda del tutorato
(Trascrizione delle 3 pagine della scansione. Non è una lezione, quindi non ha numero: è lo svolgimento a mano della scheda `fonti/Matematica discreta/TUTORATO_1_MATEMATICA_DISCRETA.pdf` (datata 11 novembre 2026, testo in `fonti_testo/Matematica discreta/TUTORATO_1_MATEMATICA_DISCRETA.md`). I numeri degli esercizi sono quelli della scheda. Formule in Unicode; tra parentesi quadre le mie note di lettura e i confronti con le soluzioni della scheda.)

## Pagina 1

**Tutorato 1**

**2)** a) Falsa.
b) (A ∪ B) ∩ C = (B ∪ C) ∩ A [nella scheda il punto b) è «(A ∪ B) ∩ C = A ∪ (B ∩ C)», falsa]
c) A ∩ B = ∅ ⟹ 𝒫(A) ∩ 𝒫(B) = ∅ ✓ → A = {1, 3}, B = {2, 5}
[ERRORE: 𝒫(A) ∩ 𝒫(B) contiene sempre ∅, quindi non è mai vuoto; la scheda dice correttamente 𝒫(A) ∩ 𝒫(B) = {∅}.]

**3)** A = {1, 2, 3}
- {{1}, {2}, {3}}
- {{1}, {2, 3}}
- {{1, 3}, {2}}
- {{1, 2}, {3}}
- {{1, 2, 3}}
[Le 5 partizioni, come nella scheda.]

**4)** A, B
a) Se A = B → ∀ C ⟹ A ∩ C = B ∩ C
[Tentativo barrato con una grande croce rossa: A = {1, 2}, B = {1, 2}, C = {2, 3}, A ∩ C = {2}, B ∩ C = {2}.]
x ∈ A ∩ C ⟺ (x ∈ A e x ∈ C) ⟺ (x ∈ B e x ∈ C) ⟺ x ∈ B ∩ C

b) C | A ∪ C = B ∪ C e A ∩ C = B ∩ C
A = (A − C) ∪ (A ∩ C)
B = (B − C) ∪ (B ∩ C)
(A ∪ C) − C = (B ∪ C) − C ⟹ A − C = B − C → A = B
[Diagramma di Venn: due cerchi A e C sovrapposti, con le due zone di A indicate.]

Sia x ∈ A ⟹ x ∈ B?
C ⟶ x ∈ C ⟹ A ∩ C = B ∩ C, allora x ∈ B
  ⟶ x ∉ C ⟹ A ∪ C = B ∪ C ⟹ (A ∪ C) − C = (B ∪ C) − C

Sia x ∈ A
? x ∈ B
- x ∈ C → x ∈ A ∩ C, allora x ∈ C → se x ∈ C e A ∩ C = B ∩ C, se x ∈ B ∩ C allora x ∈ B
- x ∉ C:
  x ∈ A ∪ C     x ∈ (A ∪ C) − C
  A ∪ C = B ∪ C … [non finito]

## Pagina 2

[Esercizio 7, senza numero]
f : ℤ → ℤ
f(n) = n² − 3n + 5
? f(0), f⁻¹({5}), f⁻¹({0})
f(0) = 5
f(x) = ⋯ = 5 ⟹ n² − 3n + 5 = 5 [il 5 barrato con la freccia: −5 da entrambi i lati]
n² − 3n = 0 → n(n − 3) → n = +3, n = 0
f⁻¹({5}) = {0, 3}
f⁻¹({0}) ⟹ n² − 3n + 5 = 0
(+3 ± √(9 − 20))/2 → (+3 ± √(−11))/2 → IMP → f⁻¹({0}) = ∅

**8)** 1) Iniettiva, no suriettiva.   f̄ : ℤ → 3ℤ ✓
f̄⁻¹ : 3ℤ → ℤ → m ↦ m/3
2) f : ℝ → ℝ, f(x) = x² + 2
f̄ : ℝ_[0, +∞) → ℝ_[2, +∞)
f̄⁻¹ : ℝ_[2, +∞) → ℝ_[0, +∞)
f̄⁻¹ = √(y − 2)
3) f : ℝ² → ℝ², f(x, y) = (x², x² + y²)   [riquadrati: NO SURI, NO INI]
f̄ : ℝ²_{≥0} → ℝ²_{≥0}
f̄⁻¹ : ℝ²_{≥0} → ℝ²_{≥0}, f̄⁻¹(a, b) = (√a, √(b − a))
[ERRORE: il codominio di f̄ non può essere ℝ²_{≥0}: per esempio (1, 0) non è immagine di nulla, e √(b − a) non è definita se b < a. Il codominio giusto è l'immagine I = {(a, b) : a ≥ 0, b ≥ a}, come nella scheda.]

**9)** f(x) = 2x − 3
g(x) = ax + b
(g ∘ f)(x) = 6x − 5 = g(f(x))   [un primo tentativo è cancellato]
g(x) = ?
a? b?
g(2x − 3) = a(2x − 3) + b = 2ax − 3a + b = 6x − 5 → 2a = 6 → a = 3;  −3a + b = −5 → b = 4
[In grande:] **g(x) = 3x + 4**

## Pagina 3

**10)** Sia A = {−1, 0, 1}, R = {(−1, 1), (1, 0), (−1, −1), (1, 1), (0, 0)} ⊆ A × A
1) A × A = {(−1, −1), (−1, 0), (−1, 1), (0, −1), (0, 0), (0, 1), (1, −1), (1, 0), (1, 1)}
2) R? Rifl. ✓   Simm. ✗   Trans. [lasciato in bianco; la scheda: non transitiva, (−1, 1), (1, 0) ∈ R ma (−1, 0) ∉ R]

**11)** A = {1, 2, 3, 4, 5, 6}
R: xRy ⟺ 2x + 3y è un multiplo di 5
R = {(1, 6), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (6, 1)} [sotto, un punto interrogativo]
Riflessiva ✓, Simm. ✓, Transitiva
[Elenco verificato: 2x + 3y ≡ 0 (mod 5) ⟺ x ≡ y (mod 5).]
x y z / 1 2 3     xRy: 1 2     yRz: 2 3
Trans?
x, y, z
2x + 3y = 5k   (xRy)
2y + 3z = 5h   (yRz)   } IMPOSTARE →
(2x + 3y) + (2y + 3z) = 5k + 5h → 2x + 5y + 3z = 5(k + h) → 2x + 3z = 5(k + h) − 5y → [evidenziato] 2x + 3z = 5(k + h − y)
[Prova numerica a fianco, con x = 1, z = 1, k = 4, h = 3, y = 6:] 2 + 3 = 5(4 + 3 − 6) → 5 = 5 (cerchiato)

**12)** 5 m(atematica), 4 i(nformatica), 3 F(isica): diversi.   3 libri:
1 – 2 mate?   2 – 1 info   3 – no Fisica
1) 5·4·7 = 140
2) 4·11·10 = 440
3) 9·8·7 = 504
(5 su 2)(7 su 1)·3! → 10·7·3! = 420
1 info [non finito]
[ERRORI: il punto 1 è 420 (lo dà la riga sotto, come la scheda): 5·4·7 = 140 conta le coppie ordinate di libri di matematica per il terzo libro, ma non i posti sullo scaffale. Il punto 2 è 12·11·10 − 8·7·6 = 984, non 4·11·10 = 440 (che fissa il libro di informatica al primo posto e conta più volte le terne con due libri di informatica). Il punto 3, 504, è giusto. Conti verificati.]
