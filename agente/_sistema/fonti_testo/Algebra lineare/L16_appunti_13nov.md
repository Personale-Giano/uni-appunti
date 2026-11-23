<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/13 Novembre/13 Novembre .pdf -->
# Algebra lineare, lezione 16: Applicazioni lineari III (13 novembre 2026): appunti a mano di Emanuele
(Trascrizione delle 2 pagine del PDF, fatta il 23 nov 2026. Vettori colonna in linea come (a ; b); matrici riga per riga. Indici delle matrici associate: base di partenza in alto, base di arrivo in basso, scritto [f]^B_C. Tra parentesi quadre le note di lettura.)

## Pagina 1
**Lezione 16: APPLICAZIONI LINEARI**

V sp. vettoriale, B = {v_1, …, v_n} base → F_B: V → 𝕂ⁿ, v ↦ [v]_B
V —f→ W lineare, B = {v_1, …, v_n} ⊆ V, C = {w_1, …, w_m} ⊆ W ⇝ [f]^B_C ∈ M(m, n, 𝕂)
[f]^B_C = ( [f(v_1)]_C , … , [f(v_n)]_C )
[In alto «F_B» con la freccia V → 𝕂ⁿ: è in realtà F_B⁻¹, che manda v in [v]_B.]

**Idea** cosa succede se cambio base?
① Date basi B e B′ di uno stesso sp. vett. V, e preso v ∈ V, qual è la relazione tra [v]_B e [v]_B′? →  [freccia sotto: «Cambio di base»]

Ricordiamo f : V_B → W_C, e v ∈ V allora [f(v)]_C = [f]^B_C · [v]_C
[«[v]_C»: va letto [v]_B.]
—————————————
Applichiamo questo a: id : V_B → V_B′ ⟹ [v]_B′ = [id(v)]_B′ = [id]^B_B′ · [v]_B
[[id]^B_B′ riquadrato in rosso: «Matrice del cambio di base»]

**Prop.** Date due basi B, B′ di V, sia A = [id]^B_B′. Allora ∀ v ∈ V, [v]_B′ = A · [v]_B.
Inoltre, A ∈ M(n) è invertibile, e [id]^B′_B = ([id]^B_B′)⁻¹ = A⁻¹.

**es.** ℝ[x], B = {1, 1 + x}, B′ = {1 + x, 2 + x}
[Lo spazio è quello dei polinomi di grado ≤ 1, ℝ_1[x].]
1) Calcolare [id]^B_B′ = A
2) Calcolare [x]_B, [x]_B′, A[x]_B

① [id]^B_B′ = ( [id(1)]_B′  [id(1 + x)]_B′ ) = ( [1]_B′ | [1 + x]_B′ ) = ( a c ; b d )
   1 = a(1 + x) + b(2 + x)
[Il conto della prima colonna non è proseguito; i numeri della matrice compaiono nella riga finale.]
② [x]_B′ = (a ; b)
   x = a(1 + x) + b(2 + x) = (a + 2b) + (a + b)x
   { a + b = 1 ; a + 2b = 0 } ⇝ { b = −1 ; a + b = 1 ⟹ a = 2 }
   [x]_B = (c ; d): x = c · 1 + d(1 + x) ⟹ [x]_B = (−1 ; 1)

```
                 ⎛ −1 1 ⎞ ⎛ −1 ⎞   ⎛  2 ⎞
[id]^B_B′ [x]_B = ⎝  1 0 ⎠ ⎝  1 ⎠ = ⎝ −1 ⎠ = [x]_B
```

[L'ultimo «[x]_B» va letto [x]_B′: il risultato (2 ; −1) coincide con [x]_B′ trovato sopra. Tutti i numeri sono giusti, verificati con SymPy.]

**Oss.**
1. Dato B = {v_1, …, v_n}, B′ = {v_1′, …, v_n′} di V ⟹ [id]^B_B′ = ( [v_1]_B′ | … | [v_n]_B′ )
2. Se V = 𝕂ⁿ e B′ = {e_1, …, e_n} allora (ricordiamo) (a_1 ; ⋮ ; a_n) = a_1 e_1 + … + a_n e_n, cioè [(a_1 ; ⋮ ; a_n)]_B′ = (a_1 ; ⋮ ; a_n)
   ⟹ [id]^B_B′ = ( v_1 | … | v_n )
   [frecce: B = «qualunque base v_1, …, v_n»; B′ = «Base Canonica»]

**Esercizio.** In ℝ², calcolare [Id]^B_B′ con B = {(1 ; 0), (0 ; 1)}, B′ = {(1 ; 1), (0 ; 1)}

```
                           ⎛ 1 0 ⎞⁻¹   ⎛  1 0 ⎞
[id]^B_B′ = ([id]^B′_B)⁻¹ = ⎝ 1 1 ⎠   = ⎝ −1 1 ⎠
```

[sotto il pedice B di [id]^B′_B, in rosso: «Canonica»]

## Pagina 2
V, B = {v_1, …, v_n}, B′ ⟹ [id]^B_B′ = ( [v_1]_B′ … [v_n]_B )
[L'ultima colonna va letta [v_n]_B′.]

**Composizione**
Ricordiamo V —f→ W —g→ U, con la freccia composta g ∘ f : V → U
g ∘ f(v) = g(f(v))

**Prop.** Se f, g sono lineari ⟹ g ∘ f è lineare.

**Prop.** Siano A ∈ M(m, n), B ∈ M(n, p) ⇝ AB ∈ M(m, p)
𝕂ᵖ —L_B→ 𝕂ⁿ —L_A→ 𝕂ᵐ, con la freccia composta L_AB
Allora L_AB = L_A ∘ L_B

**Dim.**
L_A · L_B(v) = L_A(L_B v) = A(Bv) =[associativa] (AB) · v = L_AB(v)
[«L_A · L_B» va letto L_A ∘ L_B.]

**Prop.**
[In blu: A = {u_1, …, u_p}, B = {v_1, …, v_n}, C = {w_1, …, w_m}: qui A, B, C sono basi.]
Diagramma:
U_A —f→ V_B —g→ W_C, con la freccia composta g ∘ f in alto
↓        ↓        ↓
𝕂ᵖ —L_A→ 𝕂ⁿ —L_B→ 𝕂ᵐ, con la freccia composta L_AB in basso
A = [f]^A_B, B = [g]^B_C (qui A e B sono matrici)
Allora **[g ∘ f]^A_C = [g]^B_C · [f]^A_B** [riquadrato in rosso]
[Nel diagramma la freccia composta in basso è etichettata L_AB; con A = [f] applicata per prima dovrebbe essere L_BA, coerentemente con la formula riquadrata, che è giusta. Inoltre le lettere A e B indicano sia basi sia matrici.]

**Applicazioni**
**Prop.** f : V_B → W_C è un isomorfismo se e solo se [f]^B_C è invertibile. In tal caso, f⁻¹ : W_C → V_B ha [f⁻¹]^C_B = ([f]^B_C)⁻¹.

**es.** Calcolare in ℝ² la matrice [id]^B_B′, B = {(1 ; 0), (1 ; 1)}, B′ = {(1 ; 1), (0 ; 1)}
ℝ²_B —id→ ℝ²_C —id→ ℝ²_B′  [sotto C: «Canonica»; a lato: id ∘ id = id]

```
[id]^B_B′ = [id]^C_B′ · [id]^B_C = ([id]^B′_C)⁻¹ [id]^B_C

            ⎛ 1 0 ⎞⁻¹ ⎛ 1 1 ⎞   ⎛  1 0 ⎞ ⎛ 1 1 ⎞   ⎛  1 1 ⎞
          = ⎝ 1 1 ⎠   ⎝ 0 1 ⎠ = ⎝ −1 1 ⎠ ⎝ 0 1 ⎠ = ⎝ −1 0 ⎠
```

② Sia V —f→ W lineare, B, B′ ⊆ V basi, C, C′ ⊆ W basi: [f]^B_C, [f]^B′_C′ ⇝ Che rapporto hanno?
V_B′ —id_V→ V_B —f→ W_C —id_W→ W_C′

**Oss.**
id_W ∘ f ∘ id_V = f
[f]^B′_C′ = [id_W ∘ f ∘ id_V]^B′_C′ = [id_W]^C_C′ · [f]^B_C · [id_V]^B′_B

**Prop.**
Date basi B, B′ in V sia P_V = [id]^B_B′ matrice cambio di base.
Date C, C′ ⊆ W basi, sia P_W = [id]^C_C′. Allora, data V —f→ W con A = [f]^B_C, A′ = [f]^B′_C′ ⟹ **A′ = P_W · A P_V⁻¹**

**Endomorfismi**
**Def.** Endomorfismo di V = f : V → V lineare.
f endomorfismo, B ⊆ V ⇝ [f]^B_B = A ∈ M(n)  [freccia verde: n = dim V]
B′ ⊆ V altra base → [f]^B′_B′ = A′

**Prop.:** [Il foglio finisce qui: l'enunciato non è scritto.]
