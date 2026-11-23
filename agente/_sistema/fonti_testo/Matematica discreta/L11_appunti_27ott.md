<!-- fonte: _sistema/fonti/Appunti/Mate_2026/27 ottobre/27 Ottobre.pdf -->
# Matematica discreta, lezione 11 (27 ottobre 2026): appunti a mano di Emanuele
(Trascrizione delle 2 pagine della scansione. Formule in Unicode; tra parentesi quadre le mie note di lettura. Le permutazioni a due righe sono scritte «prima riga / seconda riga».)

## Pagina 1

**Potenza di un binomio**

(a + b)¹⁰ = (a + b) ⋯ (a + b)  [graffa sopra: 10 fattori]
[Sotto il primo e l'ultimo fattore è disegnato un interruttore (cerchio con una tacca), con i puntini in mezzo; sotto, «a³b⁷».]
A destra, separato da una riga verticale: C_k aᵏ bⁿ⁻ᵏ, con C_k = (n su k).

**Permutazioni**

Sia X insieme ≠ ∅. Una **permutazione** su/in X è una funzione biettiva f : X → X.
Siamo interessati a studiare le permutazioni esclusivamente nel caso X è FINITO (|X| = n).
Di fatto usiamo X = Iₙ = {1, 2, …, n}.

**Notazione**
Sₙ = permutazioni di {1, …, n}.
es. n = 3 → {1, 2, 3}:
1 → 3
2 → 1
3 → 2
[A destra:] Siccome permutare è un po' come riordinare, |Sₙ| = n!.

② In quanto funzioni biettive, le permutazioni si possono comporre. Il risultato è ancora una permutazione.

**Proprietà**
1. Id ∈ Sₙ
2. Se π ∈ Sₙ allora [frase non finita; sottintesa l'esistenza dell'inversa]
3. La composizione è associativa.
[riga orizzontale]
In generale la composizione non è commutativa.

**es.** n = 7
π: 1 2 3 4 5 6 7 / 3 4 6 1 2 5 7
π(1) = 3
π(2) = 4
π(3) = 6

π⁻¹: 1 2 3 4 5 6 7 / 4 5 1 2 6 3 7

[A destra, separato da una riga verticale:] 1 2 3 4 5 / 2 5 3 1 5 (i due 5 sottolineati) → **NON è permutazione** (non iniettiva) [in rosso].

[Riga di trattini orizzontali]

σ = 1 2 3 4 5 6 7 / 5 2 6 1 3 7 4

π ∘ σ  [scritto e lasciato senza calcolo]

σ ∘ π → colonne: 1 2 3 / 5 2 6 / 6 5 3
[Il calcolo è interrotto dopo tre colonne. La riga di mezzo, 5 2 6, è σ(1), σ(2), σ(3); l'ultima riga, 6 5 3, è π⁻¹ applicata a 5, 2, 6 (cioè π⁻¹ ∘ σ), non σ ∘ π: con la composizione da destra a sinistra σ ∘ π ha seconda riga 6 1 7 5 2 3 4 (verificato con SymPy).]

**Def.** Una permutazione C ∈ Sₙ si chiama **CICLO** se esiste un sottoinsieme {i₁, …, i_ℓ} ⊂ Iₙ t.c.
C(i₁) = i₂   C(i_{ℓ−1}) = i_ℓ
C(i₂) = i₃   C(i_ℓ) = i₁
[La condizione C(k) = k fuori dal sottoinsieme non è scritta.]

## Pagina 2

C₁ → {i₁ … i_ℓ}
C₂ → {j₁ … j_k}

**Def.** Due cicli C₁ e C₂ si dicono **disgiunti** se {i₁ … i_ℓ} ∩ {j₁ … j_k} = ∅.

**Proposizione**
Siano C₁, C₂ ∈ Sₙ due cicli disgiunti, allora:
C₁ ∘ C₂ = C₂ ∘ C₁

[Inizio di dimostrazione:]
C₁ = (i₁ … i_ℓ)
C₂ = (j₁ … j_k)      {i₁ … i_ℓ} ∩ {j₁ … j_k} = ∅
C₂ ∘ C₁                                  C₁ ∘ C₂
i_r → i_{r+1} (freccia etichettata C₁)
j_s → (freccia etichettata C₂) [non completato]

[Il resto della pagina è vuoto.]
