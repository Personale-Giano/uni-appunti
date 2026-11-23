<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/11 Novembre/11 Novembre .pdf -->
# Algebra lineare, lezione 15: Applicazioni lineari II (11 novembre 2026): appunti a mano di Emanuele
(Trascrizione delle 2 pagine del PDF, fatta il 23 nov 2026. Vettori colonna in linea come (a ; b ; c); matrici riga per riga. Nella pagina 1 sono incollate tre foto della lavagna, trascritte qui come tali. Tra parentesi quadre le note di lettura.)

## Pagina 1
**Lezione 15 APPLICAZIONI LINEARI 2**

f : V → W **Lineare** se f(v + w) = f(v) + f(w), f(λv) = λf(v).
Es.: A ∈ M(m, n, 𝕂) ⇝ L_A : 𝕂ⁿ → 𝕂ᵐ, L_A(v) = A · v.

**Teorema della dimensione:** f : V → W

[Foto della lavagna 1]
⟹ dim Im f + dim Ker f = dim V
⟹ (ramo 1) dim Im f ≤ dim V, e «=» sse Ker f = 0 sse f iniettiva
⟹ (ramo 2) Im f ⊆ W: dim Im f ≤ dim W, e «=» sse Im f = W sse f suriettiva

[Foto della lavagna 2]
LEZIONE 15: APPLICAZIONI LINEARI II
f : V → W LINEARE se f(v + w) = f(v) + f(w), f(λv) = λf(v)
Es.: A ∈ M(m, n; 𝕂) ⇝ L_A : 𝕂ⁿ → 𝕂ᵐ, L_A(v) = Av

[Foto della lavagna 3]
⟹ • Se f è iniettiva, allora dim V = dim Im f ≤ dim W ⟹ dim V ≤ dim W
   • Se f è suriettiva, dim W = dim Im f ≤ dim V ⟹ dim V ≥ dim W
Def. un **ISOMORFISMO** è f : V → W lineare biettiva.

[Fine delle foto]

**Ricordiamo** Funzioni biettive hanno un inversa f⁻¹ : W → V.
**Prop.** Dato f : V → W isomorfismo, l'inversa f⁻¹ è anch'essa lineare.
**Def.** Dato un isomorfismo f : V → W, diciamo che V, W sono **isomorfi**.
**Oss.** Dalle disuguaglianze sopra, se V, W sono isomorfi allora { dim V ≤ dim W ; dim V ≥ dim W } ⟹ dim V = dim W.

**Un esempio fondamentale**
Sia V sp. vett. su 𝕂, e sia B = {v_1, …, v_n} base.
F_B : 𝕂ⁿ → V, F_B(λ_1 ; ⋮ ; λ_n) = λ_1 v_1 + … + λ_n v_n
- F_B è lineare
- F_B è suriettiva, perché v_1, …, v_n generatori
- F_B è iniettiva (ovvero Ker F_B = {0}):
  (λ_1 ; ⋮ ; λ_n) ∈ Ker F_B ⟺ 0 = F_B(λ_1 ; ⋮ ; λ_n) = λ_1 v_1 + … + λ_n v_n
  (v_1, …, v_n sono l. ind.) ⟹ (λ_1 ; ⋮ ; λ_n) = (0 ; ⋮ ; 0)
⟹ F_B è un isomorfismo, e F_B⁻¹ : V → 𝕂ⁿ, F_B⁻¹(v) = (λ_1 ; ⋮ ; λ_n) = [v]_B  dove v = λ_1 v_1 + … + λ_n v_n
[frecce: [v]_B = «vettore delle coordinate di v risp. a B»; λ_1, …, λ_n = «coordinate di v risp. a B»]

**Esempio.** ℝ_2[x], B = {1, x + 1, x² + x}, p(x) = x² + 2x + 1, calcolare F_B⁻¹(p(x)) = [p(x)]_B.
[p(x)]_B = (a ; b ; c) dove x² + 2x + 1 = a · 1 + b(x + 1) + c(x² + x) = c · x² + (b + c)x + (a + b)
[frecce che collegano i coefficienti]
⟹ { c = 1 ; b + c = 2 ⟹ b = 1 ; a + b = 1 ⟹ a = 0 } ⟹ [p(x)]_B = (0 ; 1 ; 1)

## Pagina 2
**Matrice Associata**

Sia f : V → W lineare tra sp. vett. su 𝕂.
Siano B = {v_1, …, v_n} ⊆ V, C = {w_1, …, w_m} ⊆ W basi.
f(v_1) = a_11 w_1 + … + a_m1 w_m
 ⋮
f(v_n) = a_1n w_1 + … + a_mn w_m
[accanto: f(v_i) ∈ W]

Definiamo [f]^B_C ∈ M(m, n, 𝕂) **MATRICE ASSOC.** a f, da B a C, nel seguente modo:

```
          ⎡ a_11  a_12  …  a_1n ⎤
[f]^B_C = ⎢  ⋮     ⋮         ⋮  ⎥ = ( [f(v_1)]_C | … | [f(v_n)]_C )
          ⎣ a_m1  a_m2  …  a_mn ⎦
```

Date basi B = {v_1, …, v_n} ⊆ V, C = {w_1, …, w_n} ⊆ W e f : V → W, per calcolare [f]^B_C deve:
[«C = {w_1, …, w_n}»: va letto w_m; «deve» = si deve]
1. prendere v_1, …, v_n
2. calcolare f(v_i)
3. calcolare [f(v_i)]_C

**Prop.** f : V → W lin., B ⊆ V, C ⊆ W basi ⟹ ∀ v ∈ V, [f(v)]_C = [f]^B_C · [v]_B

**es.** Sia f : ℝ_2[x] → ℝ_1[x] t.c. risp. a B = {1, x, x²}, C = {1, x},

```
          ⎛ 1 0 2 ⎞
[f]^B_C = ⎝ 0 5 3 ⎠  ∈ M(2, 3)
```

Calcolare f(a + bx + cx²) = ?  [sotto a + bx + cx²: «p(x)»]
Dalla formula: [f(p(x))]_C = [f]^B_C · [p(x)]_B
[p(x)]_B = (a ; b ; c) dove p(x) = a · 1 + b · x + c · x²
↳ Caso speciale che avviene nella base canonica

```
              ⎛ 1 0 2 ⎞ ⎛ a ⎞   ⎛ a + 2c  ⎞
[f(p(x))]_C = ⎝ 0 5 3 ⎠ ⎜ b ⎟ = ⎝ 5b + 3c ⎠
                        ⎝ c ⎠
```

f(p(x)) = (a + 2c) · 1 + (5b + 3c) · x
f(a + bx + cx²) = (a + 2c)(5b + 3c) · x
[Nell'ultima riga manca il «+»: va letto (a + 2c) + (5b + 3c)x, come nella riga sopra.]
