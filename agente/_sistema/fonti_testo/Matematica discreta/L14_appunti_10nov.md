<!-- fonte: _sistema/fonti/Appunti/Mate_2026/10 Novembre/10 Novembre.pdf -->
# Matematica discreta, lezione 14 (10 novembre 2026): appunti a mano di Emanuele
(Trascrizione delle 2 pagine della scansione: la prima scritta a mano, la seconda fatta di sette foto della lavagna incollate. Formule in Unicode; tra parentesi quadre le mie note di lettura. Composizione da destra a sinistra.)

## Pagina 1

Sₙ ∋ π può essere scritta come composizione di SCAMBI (= cicli di lungh. 2) [nel foglio «(ciclo di lungh. ℓ)», con ℓ che sembra un 2].
**Infatti:** π si può scrivere come composizione di cicli e
(1 2 … ℓ) = (ℓ−1 ℓ) ∘ … ∘ (3 ℓ)(2 ℓ)(1 ℓ)
[Verificata con SymPy per ℓ = 2, …, 6.]

(NB) La scrittura in termini di scambi NON è unica.

**Teorema**
Se π = s_k ∘ … ∘ s₁ = t_ℓ ∘ … ∘ t₁ (sᵢ, tⱼ SCAMBI)
allora k e ℓ hanno la stessa parità.

**Dim**
**1° passo)** Mi riduco ad una proprietà della permutazione id.
π = s_k ∘ … ∘ s₁ = t_ℓ ∘ … ∘ t₁
id = π⁻¹ ∘ π = (t₁⁻¹ ∘ … ∘ t_{ℓ−1}⁻¹ ∘ t_ℓ⁻¹) ∘ (s_k ∘ … ∘ s₁)
(✱) → t₁ ∘ … ∘ t_ℓ ∘ s_k ∘ … ∘ s₁   [sottolineato:] k + ℓ scambi

**2° passo)** k + ℓ non può essere dispari.
Fissiamo l'attenzione sugli scambi che contengono 1.
**Osservazione:** di questi scambi o non ce n'è nessuno oppure ce ne sono almeno 2.
Infatti se fosse id = … (1 a) … [con 1 → 1 sotto «id»; una graffa sotto la parte a sinistra di (1 a): «1 non compare mai», 1 → a].

Ora voglio modificare (✱) in modo che tutti gli 1 presenti siano spostati verso destra:
- … (1 a)(5 c) … = (b c)(1 a), con {1, a} ∩ {b, c} = ∅ [«5 c» è chiaramente «b c»: lo dice la condizione scritta a fianco];
- (1 a)(a b) = (a b)(1 b);
- (1 a)(1 b) = (a b)(1 a);
- (1 a)(1 a) [a destra, separato: si cancellano].
[Le tre uguaglianze sono verificate con SymPy.]

Una volta eliminati gli scambi con 1 da (✱) passiamo agli scambi che contengono 2. Ripeto la procedura ed elimino 2. Itero la procedura con 3, 4, …, n. Alla fine il numero totale di scambi è ZERO.

Ricordiamo che un ciclo di lunghezza ℓ si scrive come prodotto di ℓ − 1 SCAMBI.
Se conosco il TIPO so calcolare subito la parità.

**es.** Se π ha tipo (3, 5, 6) ↓ 2, 4, 5 = 2 scambi
[ERRORE: gli scambi sono 2 + 4 + 5 = 11, quindi π è dispari. Inoltre, con la convenzione della lezione precedente, il tipo si scrive in ordine decrescente: (6, 5, 3).]
π = ( _3_ )( _5_ )( _6_ )   In realtà non serve sapere il TIPO.

𝒜ₙ = {permutazioni pari in Sₙ}
𝒟ₙ = {permutazioni dispari in Sₙ}
n! = |𝒜ₙ| + |𝒟ₙ|

F : 𝒜ₙ → 𝒟ₙ, π ↦ (1 2) ∘ π        G : 𝒟ₙ → 𝒜ₙ, σ ↦ (1 2) ∘ σ
π ↦F (1 2) ∘ π ↦G (1 2) ∘ (1 2) ∘ π [i due (1 2) barrati: si cancellano, resta π]
⟹ |𝒜ₙ| = |𝒟ₙ| = ½ n!

## Pagina 2 (foto della lavagna)

**Foto 1.** ARITMETICA
ℤ = {…, −3, −2, −1, 0, 1, 2, 3, …}
- ADDIZIONE a + b
- MOLTIPLICAZIONE a · b
⤷ SODDISFANO PROPRIETÀ

**Foto 2.** La struttura moltiplicativa di ℤ è molto più complicata.
1, 1·1 = 1, 1·1·1 = 1    |    2, 2² = 4, 2³ = 8, …
−1, (−1)·(−1) = 1, (−1)³ … [l'ultimo risultato è poco leggibile nella foto: sembra «= 1», ma (−1)³ = −1]

**Foto 3.**
- ASSOCIATIVA (+, ·)
- COMMUTATIVA (+, ·)
- ESISTONO ELEMENTI NEUTRI: 0 per +, 1 per ·
- Ogni x ∈ ℤ AMMETTE OPPOSTO: x + (−x) = 0
- DISTRIBUTIVA: (a + b)x = ax + bx

**Foto 4.** DEF: Siano m, n ∈ ℤ.
Diciamo che m DIVIDE n (n è MULTIPLO di m) se ∃ k ∈ ℤ t.c. n = k·m. Scriviamo m | n.
P. es.: 3 | 12 perché 3·4 = 12;  2 ∤ −7.
RELAZIONE NON SIMMETRICA ⟹ NON È EQUIVALENZA.

**Foto 5.** PROPOSIZIONE
Siano a, b ∈ ℤ e sia s = a + b.
Allora se d ∈ ℤ divide 2 tra {a, b, s}, allora divide anche il terzo.

**Foto 6.** Dim
Caso I: d | a, d | b. ∃ k, ℓ t.c. a = dk, b = dℓ.
s = a + b = dk + dℓ = d(k + ℓ) ⟹ d | s
Caso II: d | s, d | a. s = a + b ⟹ b = s − a (Caso I)

**Foto 7.** TERMINOLOGIA
- I numeri 1, −1 si dicono INVERTIBILI.
- Un numero n ∈ ℤ ∖ {0, 1, −1} lo chiamo IRRIDUCIBILE se ogni qualvolta n = ab allora o a o b è invertibile.
- Un numero n ∈ ℤ ∖ {0, 1, −1} si dice PRIMO se ogni qualvolta n | ab ⟹ n | a oppure n | b.
