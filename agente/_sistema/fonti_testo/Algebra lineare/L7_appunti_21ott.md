<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/21 Ottobre/21 Ottobre.pdf -->
# Algebra lineare, lezione 7: Spazi vettoriali III (21 ottobre 2026): appunti a mano di Emanuele
(Trascrizione delle 2 pagine della scansione. I vettori colonna sono scritti (x, y). Le parti indicate «foto» rimandano a foto della lavagna che non sono nella scansione. Tra parentesi quadre le mie note di lettura. Gli evidenziatori sono segnalati.)

## Pagina 1

**Lezione 7 SPAZI VETTORIALI**

v₁, …, vₙ ∈ V ⟹ Span(v₁, …, vₙ) = {v = a₁v₁ + … + aₙvₙ} è un sottosp. vett. di V.
**Def.** [in alto a destra] Span(vᵢ): insieme di tutti i multipli dei vettori di vᵢ.
[Impreciso: lo Span è l'insieme delle combinazioni lineari, non dei soli multipli dei singoli vettori.]

**es. In ℝ²**
{(1, 2), (2, 4)} → Span(v₁, v₂) = {v = a(1, 2) + b(2, 4)}
= {v = (a + 2b, 2a + 4b) | a, b ∈ ℝ} = {v = (a + 2b)(1, 2)} = Span((1, 2))
[sopra e sotto il vettore: a + 2b = (a + 2b)·1, 2a + 4b = (a + 2b)·2]
[Disegno: piano cartesiano con la retta per (1, 2) e (2, 4) e il punto −(1, 2); tutto il riquadro tratteggiato in rosso è etichettato «Span(w₁, w₂)», una retta verde è etichettata «Span(v)».]

**es. 2**
{(1, 0), (0, 1)} [w₁, w₂] → Span(w₁, w₂) = {v = a(1, 0) + b(0, 1) | a, b ∈ ℝ} = {v = (a + b·0, a·0 + b·1) = (a, b) | a, b ∈ ℝ} = ℝ²

⚠ Nel caso {v₁, v₂} sopra: 2·v₁ − v₂ = 0_{ℝ²} = (0, 0).

v = a w₁ + b w₂   [a w₁ sottolineato in rosso]
[Disegno: assi con w₁ e w₂; il vettore v ottenuto andando di a·w₁ sull'asse orizzontale e poi di b in verticale.]

**Def:** dati {v₁, …, vₙ} si dicono:
1) **Linearmente indipendenti** se a₁v₁ + … + aₙvₙ = 0_V ⟹ a₁ = a₂ = … = aₙ [manca «= 0»]
2) **Generatori** se Span(v₁, …, vₙ) = V ⟷ ∀ v ∈ V, v = a₁v₁ + … + aₙvₙ per qualche a₁, …, aₙ ∈ 𝕂
3) **Base** se è sia l.i. (1) che ins. gen. (2)

es. In ℝ²:
| | è lin. ind. | è ins. generatori? | è una base? |
|---|---|---|---|
| {v₁, v₂} | NO | NO | NO |
| {w₁, w₂} | SÌ | SÌ | SÌ |

## Pagina 2

**Notazione**
Se {v₁, …, vₙ} non sono linearmente indipendenti, saranno linearmente **dipendenti** [«dipendenti» evidenziato in giallo].

**Prop.** Se {v₁, …, vₙ} è una base di V allora ∀ v ∈ V, v = a₁v₁ + … + aₙvₙ dove a₁, …, aₙ sono unici.

**Prop.** {v₁, …, vₙ} ∈ V sono lin. dipendenti se e solo se ∃ vᵢ tale che vᵢ = a₁v₁ + … + a_{i−1}v_{i−1} + a_{i+1}v_{i+1} + … + aₙvₙ.

**Fatti:**
- {v₁} è l.i. sse v₁ ≠ 0_V
- {v₁, v₂} è l.i. sse v₁ ≠ c·v₂ e v₂ ≠ c·v₁

**Teorema**
V spaz. vett. su 𝕂, {v₁, …, vₙ}, {w₁, …, w_m} basi ⟹ n = m.

⟹ **Def.**
Dato V spaz. vett. su 𝕂 chiamiamo DIMENSIONE di V, dim V, il numero di elementi di una base.
Diremo che V ha dimensione finita se ∃ base con finiti elementi.

**Esempi Importanti:**
① 𝕂ⁿ = {(a₁, …, aₙ) | a₁, …, aₙ ∈ 𝕂}
Prendiamo e₁ = (1, 0, …, 0), e₂ = (0, 1, 0, …, 0), eₙ = (0, …, 0, 1).

**Osservazione.**
a₁e₁ + a₂e₂ + … + aₙeₙ = a₁(1, 0, …, 0) + a₂(0, 1, …, 0) + … + aₙ(0, …, 0, 1) = (a₁, a₂, …, aₙ)
[a₂ evidenziato in viola in entrambi i punti; nel foglio il «+» prima di aₙeₙ è scritto «−»]
I coefficienti della comb. lineare = componenti del vettore risultante.

es. foto 12:40

[Il resto della pagina è vuoto.]
