<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/9 Novembre/9 Novembre .pdf -->
# Algebra lineare, lezione 14: Applicazioni lineari I (9 novembre 2026): appunti a mano di Emanuele
(Trascrizione delle 3 pagine del PDF, fatta il 23 nov 2026. Formule in Unicode; i vettori colonna in linea sono scritti (a ; b), con «;» tra le righe; le matrici più grandi riga per riga. Tra parentesi quadre le note di lettura. «Foto 11:59» e «Foto 12:48/49» rimandano a foto della lavagna che non sono nel PDF.)

## Pagina 1
**14. Applicazioni lineari**

**Def.** Siano V e W due spazi vettoriali sullo stesso campo 𝕂. Un'**applicazione lineare** è una funzione F : V → W tale che
(i) F(v + w) = F(v) + F(w)
(ii) F(λv) = λF(v)
∀ v, w ∈ V, ∀ λ ∈ 𝕂.

**Notiamo che:**
1. F(0_V) = F(0_𝕂 · 0_V) =⁽ⁱⁱ⁾ 0_𝕂 · F(0_V) = 0_W
   F manda l'origine di V nell'origine di W.

   v = λ_1 v_1 + … + λ_k v_k
   ⟹ F(v) = F(λ_1 v_1 + … + λ_k v_k)
   =⁽ⁱ⁾ F(λ_1 v_1) + … + F(λ_k v_k)
   =⁽ⁱⁱ⁾ λ_1 F(v_1) + … + λ_k F(v_k)
   F manda una combinazione lineare di v_1, …, v_k in una comb. lineare di F(v_1), …, F(v_k).

[linea tratteggiata blu]

**Esempio 1:** V = W = ℝ² (𝕂 = ℝ), F(a ; b) = (2a + b ; a + 3b).
(i) Siano v = (a_1 ; b_1), w = (a_2 ; b_2) ∈ V.
F(v + w) = F(a_1 + a_2 ; b_1 + b_2) = (2(a_1 + a_2) + (b_1 + b_2) ; (a_1 + a_2) + 3(b_1 + b_2))
=[prop. di 𝕂] ((2a_1 + b_1) + (2a_2 + b_2) ; (a_1 + 3b_1) + (a_2 + 3b_2))
= (2a_1 + b_1 ; a_1 + 3b_1) + (2a_2 + b_2 ; a_2 + 3b_2) = F(a_1 ; b_1) + F(a_2 ; b_2) = F(v) + F(w)
(ii) Sia v = (a ; b), λ ∈ ℝ ⟹ λv = (λa ; λb).
F(λv) = F(λa ; λb) = (2(λa) + (λb) ; (λa) + 3(λb)) = (λ(2a + b) ; λ(a + 3b)) = λ(2a + b ; a + 3b) = λF(v)
⟹ **F è lineare** [cerchiato].

**Esempio 2:** V = W = ℝ² (𝕂 = ℝ), F(a ; b) = (2a − 1 ; a + b + 3).
F(0 ; 0) = (−1 ; 3) ≠ (0 ; 0). F non manda 0_V in 0_W ⟹ F non è lineare.

**Esempio 3:** V = W = ℝ² (𝕂 = ℝ), F(a ; b) = (a² ; 2a + 3b).
[F(0 ; 0) = (0 ; 0)] → ✓
p.es. → v = (2 ; 1), w = (2 ; 2): F(v + w) = F(4 ; 3) = (16 ; 17)
F(v) + F(v) = F(2 ; 1) + F(2 ; 2) = (4 ; 7) = (4 ; 10) = (8 ; 17) ≠ (16 ; 17) = F(v + w)
[Nel foglio «F(v) + F(v)» va letto F(v) + F(w), e tra (4 ; 7) e (4 ; 10) c'è «=» al posto di «+». I numeri sono giusti: verificato con SymPy.]
F non è lineare.

**Esempio 4:** Siano V, W due spazi vettoriali qualsiasi (sullo stesso campo 𝕂). L'applicazione nulla è F : V → W, F(v) = 0_W ∀ v ∈ V. F è lineare.

**Esempio 5:** Sia V uno spazio vettoriale qualsiasi. L'applicazione d'identità è F : V → V, F(v) = v ∀ v ∈ V. F è lineare.

## Pagina 2
**Esempio 6:** Prendiamo una matrice m × n A = (a_ij) e definiamo L_A : 𝕂ⁿ → 𝕂ᵐ, L_A(x) = A · x.
«left» (molt. con A a sinistra):

```
x = ⎛ x_1 ⎞  ⟼  A · x = ⎛ a_11 … a_1n ⎞ ⎛ x_1 ⎞ = ⎛ a_11 x_1 + … + a_1n x_n ⎞
    ⎜  ⋮  ⎟             ⎜  ⋮       ⋮  ⎟ ⎜  ⋮  ⎟   ⎜            ⋮            ⎟
    ⎝ x_n ⎠             ⎝ a_m1 … a_mn ⎠ ⎝ x_n ⎠   ⎝ a_m1 x_1 + … + a_mn x_n ⎠
```

[in verde] guardare foto 11:59

**Esempio 7:** Tr : M(n) → 𝕂, A = (a_11 … ; … a_nn), Tr(A) = a_11 + … + a_nn. Tr è lineare.

**Esempio 8:** La derivata ℝ_4[x] → ℝ_3[x], p(x) ↦ p′(x) è lineare.

**Nucleo & immagine**

**Def.** Sia F : V → W un'applicazione lineare tra due spazi vettoriali. Il **nucleo** di F è
Ker(F) = {v ∈ V | F(v) = 0_W}  [in blu: «Kernel →»]
L'**immagine** di F è
Im(F) = {w ∈ V | ∃ v ∈ V con F(v) = w}
[Nel foglio «w ∈ V»: va letto w ∈ W.]

**Prop.**
(1) Ker(F) ⊆ V è un sottospazio di V
(2) Im(F) ⊆ W è un sottospazio di W

**Dim.**
(1) a) 0_V ∈ Ker(F). Infatti vale F(0_V) = 0_W per ogni applicazione lineare.
    b) v_1, v_2 ∈ Ker(F): F(v_1 + v_2) =⁽ⁱ⁾ F(v_1) + F(v_2) = 0_W + 0_W = 0_W [sotto l'uguale: v_1, v_2 ∈ Ker(F)] ⟹ v_1 + v_2 ∈ Ker(F)
    c) v ∈ Ker(F), λ ∈ 𝕂: F(λv) =⁽ⁱⁱ⁾ λ · F(v) = λ · 0_W = 0_W [sotto l'uguale: v ∈ Ker(F)] ⟹ λv ∈ Ker(F)
(2) a) 0_W ∈ Im(F), infatti F(0_V) = 0_W
    b) w_1, w_2 ∈ Im(F) ⟹ ∃ v_1, v_2 con F(v_1) = w_1, F(v_2) = w_2
[La dimostrazione di (2) si interrompe qui: manca la conclusione di b) e il punto c).]

**Prop.** F : V → W un'app. lineare.
1) F è iniettiva ⟺ Ker(F) = {0_V}
2) F è suriettiva ⟺ Im(F) = W

**Dim.**
1) «⟸» Siano v, v′ ∈ V con F(v) = F(v′)
   ⟹ F(v − v′) =⁽ⁱ⁾⁽ⁱⁱ⁾ F(v) − F(v′) = 0
   ⟹ v − v′ = 0 ⟺ v = v′  [a lato: Ker F = {0}]
1) «⟹» e 2) è semplice. ∎

## Pagina 3
**Teorema della dimensione**
Sia F : V → W un'appl. lineare. Allora dim Ker(F) + dim Im(F) = dim V.

**es.** V = ℝ³, W = ℝ² (𝕂 = ℝ), F(x ; y ; z) = (x ; y)  (F è lineare)
Ker(F) = {(0 ; 0 ; t) | t ∈ ℝ} = Span((0 ; 0 ; 1))  [a lato: sottospazio di ℝ³ di dimensione 1 («retta»)]
Im(F) = ℝ² = W (con dimensione 2)

[in verde] Foto 12:48/49 ~
