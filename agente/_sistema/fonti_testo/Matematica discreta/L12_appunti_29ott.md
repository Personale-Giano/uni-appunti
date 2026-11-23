<!-- fonte: _sistema/fonti/Appunti/Mate_2026/29 Ottobre/29 Ottobre .pdf -->
# Matematica discreta, lezione 12 (29 ottobre 2026): appunti a mano di Emanuele
(Trascrizione della pagina unica della scansione. Il contenuto è lo stesso di `_sistema/fonti/Appunti/29 Ottobre .pdf`, già usato per i cap. 34-35 ma mai trascritto: le due scansioni differiscono solo per la compressione. Formule in Unicode; tra parentesi quadre le mie note di lettura.)

## Pagina 1

**Permutazione**
f : Iₙ → Iₙ

Un ciclo c è una permutazione di questo tipo:
{i₁ … i_ℓ} ⊂ Iₙ
t.c.  c(i₁) = i₂ … c(i_ℓ) = i₁        c(t) = t  ∀ t ∉ {i₁ … i_ℓ}

Esempio: (4 1 2 5)
4 → 1
1 → 2
2 → 5
5 → 4

**Formula:**
I cicli in Sₙ di lunghezza ℓ sono (1/ℓ) · n!/(n − ℓ)!

**Teorema**
Sia π ∈ Sₙ, π ≠ id.
Allora esiste una scrittura essenzialmente unica
π = C_k ∘ … ∘ C₁
dove Cᵢ è un ciclo (∀ i) e i Cᵢ sono a due a due disgiunti.

**Definizione** [una freccia la collega alla scrittura del teorema]
Sia π ≠ id una permutazione e sia π = C_k ∘ … ∘ C₁ la sua scrittura.
Sia ℓᵢ = LUNGH(Cᵢ).
Posso sempre far sì che ℓ₁ ≥ ℓ₂ ≥ ℓ₃ [il primo simbolo sembra «=»; il senso è ℓ₁ ≥ ℓ₂ ≥ … ≥ ℓ_k].
La sequenza (ℓ₁, ℓ₂, …, ℓ_k) si chiama il **tipo** di π.
Fisso n: elencare i possibili tipi.

**Dimostrazione:**
(P.1) T = {x ∈ Iₙ | π(x) ≠ x} ≠ ∅     |T| < ∞
Scelgo t = t₁ come [elemento di T] e so che c'è un ciclo C₁ = (t₁ … t_ℓ).
[A destra lo schema: t₁ →π t₂ →π t₃ →π t₄ →π t₅ …, con una freccia π che torna in t₁; «Ho un ciclo (t₁, t₂, …, t_ℓ)».]

(P.2) T ∖ {t₁, t₂, …, t_ℓ}:
- = ∅ ⟹ π = C₁
- ≠ ∅ scelgo s ∈ T, e rifaccio lo stesso discorso.

[Il resto della pagina è vuoto. Manca la dimostrazione dell'unicità.]
