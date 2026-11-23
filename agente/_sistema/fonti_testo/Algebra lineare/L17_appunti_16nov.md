<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/16 Novembre/16 novembre.pdf -->
# Algebra lineare, lezione 17: Autovalori e autovettori I (16 novembre 2026): appunti a mano di Emanuele
(Trascrizione delle 3 pagine del PDF, fatta il 23 nov 2026. Vettori colonna in linea come (a ; b ; c); matrici riga per riga. Nelle pagine 1 e 2 sono incollate foto della lavagna, trascritte come tali. Tra parentesi quadre le note di lettura.)

## Pagina 1
**17. Autovalori e Autovettori**

**Def.** Sia F : V → V un endomorfismo di uno sp. vett. V su un campo 𝕂.
Un **autovettore** di F è un vettore v ∈ V con v ≠ 0 e **F(v) = λv** [riquadrato] ✱ per qualche λ ∈ 𝕂.
λ si chiama **autovalore** (associato a v).
[Nel foglio «con V ≠ 0»: va letto v ≠ 0.]

⚠ λ può essere 0, v non può essere 0.

**Oss.** Se B è una base di V, A = [F]^B_B, x = [v]_B, allora
[F(v)]_B = A · x;  F(v) = λv ⟺ A · x = λx  [freccia sotto A · x: L_A(x)]
L'unico caso che dobbiamo capire è quello dove f = L_A : 𝕂ⁿ → 𝕂ⁿ.
[Nel foglio 𝕂ⁿ → 𝕂ᵐ; per un endomorfismo è 𝕂ⁿ → 𝕂ⁿ.]

**es. 1** L_A : ℝ² → ℝ² con

```
A = ⎛ 3 4 ⎞
    ⎝ 0 2 ⎠
```

L_A(a ; b) = ( 3 4 ; 0 2 )(a ; b) = (3a + 4b ; 2b)
• v_1 = e_1 = (1 ; 0): L_A(e_1) = (3 ; 0) = 3(1 ; 0) = 3v_1
  v_1 è autovettore con autovalore λ_1 = 3
• v_2 = e_2 = (0 ; 1): L_A(e_2) = (4 ; 2) ≠ λ(0 ; 1) per ogni x
  v_2 no autovettore
• v_3 = (3 ; 1) ⟹ L_A(v_3) = (13 ; 2) ≠ λ(3 ; 1) per ogni x
  v_3 non è autovettore
• v_4 = e_4 = (−4 ; 1): L_A(−4 ; 1) = (−8 ; 2) = 2(−4 ; 1) per ogni x
  v_4 è autovettore con autovalore λ_4 = 2
[«per ogni x» va letto «per ogni λ»; «e_4» è solo un'etichetta: (−4 ; 1) non è un vettore della base canonica. Nella riga di v_4 «per ogni x» è di troppo. Conti verificati con SymPy.]

**es. 2** L_A : ℝ³ → ℝ³ con

```
    ⎛ 1 1 −1 ⎞
A = ⎜ 2 1  1 ⎟
    ⎝ 3 0  2 ⎠
```

• v_1 = e_1 = (1 ; 0 ; 0) ⟹ L_A(v_1) = (1 ; 2 ; 3) ∀ x  [≠ λv_1 per ogni λ]
  v_1 non è autovettore
• v_2 = e_2 = (0 ; 1 ; 1): L_A(v_2) = (0 ; 2 ; 2) = 2v_2
  v_2 è autovettore con autovalore λ_2 = 2
[«e_2» è un'etichetta sbagliata: (0 ; 1 ; 1) non è e_2 = (0 ; 1 ; 0). Il conto è giusto.]

**Notiamo:** Se v è un autovettore di F con autovalore λ allora μ · v (μ ≠ 0) è anche autovettore di F con autovalore λ:
F(μ · v) = μF(v) = μ(λv) = λ(μv)  [sotto il primo uguale: «F è lineare»; sotto il terzo: ✱, la definizione]

**es. 3** L_A : ℝ² → ℝ² con A Rot_θ (θ ∉ {0, π})

```
A = ⎛ cos θ  −sin θ ⎞
    ⎝ sin θ   cos θ ⎠
```

L_A(e_1) = (cos θ ; sin θ), L_A(e_2) = (−sin θ ; cos θ)
[Disegno: assi cartesiani, e_1 ed e_2, e i vettori Ae_1 e Ae_2 ruotati dell'angolo θ.]
[in verde] Se v ≠ 0 è un qualsiasi vettore, allora L_A(v) = A · v
[Foto della lavagna, a sinistra, con la scritta rossa «2 Foto 9:45»:]
A = ( cos θ  −sin θ ; sin θ  cos θ )
Se v ≠ 0 è un qualsiasi vettore, allora L_A(v) = A · v è ruotato di angolo θ.
Se θ ≠ 0, θ ≠ π, L_A(v) non è mai un multiplo di v
⟹ non ci sono autovettori
[Foto della lavagna, a destra:]
Endomorfismi (o matrici) diagonalizzabili
Def. Un endomorfismo f : V → V è **diagonalizzabile** se V ha una base B = {v_1, …, v_n} formata da autovettori di f.

## Pagina 2
**Prop.** Sia B = {v_1, …, v_n} una base di V. La matrice A = [F]^B_B di un endomorfismo F : V → V è diagonale se e solo se v_1, …, v_n sono autovettori di F.

**Dim.**
v_i autovettore ⟺ F(v_i) = λ_i v_i ⟺ [F(v_i)]_B = [λ_i v_i]_B = (0 ; λ_i ; 0) = λ_i e_i  [λ_i in i-esima posizione]
⟺ [F]^B_B = ( [F(v_1)]_B | … | [F(v_n)]_B ) = ( λ_1 e_1, …, λ_n e_n ) = diag(λ_1, …, λ_n)

Diagramma:
V,A —F→ V,A  con [F]^A_A = A
↓ M⁻¹         ↑ [id]^B_A = M  [freccia: «Cambio di base»]
V,B —→ V,B  con [F]^B_B = D  [freccia: «Diagonale»]
M⁻¹ = [id]^A_B  [freccia: «Cambio di base»]

A = M · D · M⁻¹ ⟺ D = M⁻¹ · A · M

**Def.** Una matrice A ∈ M(n, 𝕂) è **diagonalizzabile** se esiste una matrice M ∈ M(n, 𝕂) invertibile tale che M⁻¹ A M = D è diagonale.

**Prop.** F : V → V è un endomorfismo diagonalizzabile se e solo se A = [F]^B_B è diagonalizzabile (per una qualsiasi base B) ⟺ esiste una base C in cui [F]^C_C è diagonale.

Se A è la base canonica e B è la base formata da autovettori v_1, …, v_n → M = [id]^B_A = ( v_1 | … | v_n )

**esempio: → Foto 10:18** [foto piccola della lavagna, illeggibile in parte: si leggono M = [id]^B_A = (v_1 | v_2) = ( 1 −4 ; 0 1 ), det(M) = 1 ⟹ M⁻¹ = (1/det M) · ᵗCof(M), e l'inizio di una matrice]

M = [id]^B_A = ( v_1 | v_2 ) = ( 1 −4 ; 0 1 )
det(M) = 1 ⟹ M⁻¹ = (1/det M) · ᵗCof(M) = ᵗ( 1 0 ; 4 1 ) = ( 1 4 ; 0 1 )

```
D = M⁻¹ · A · M = ⎛ 1 4 ⎞ ⎛ 3 4 ⎞ ⎛ 1 −4 ⎞ = ⎛ 3 12 ⎞ ⎛ 1 −4 ⎞ = ⎛ 3 0 ⎞
                  ⎝ 0 1 ⎠ ⎝ 0 2 ⎠ ⎝ 0  1 ⎠   ⎝ 0  2 ⎠ ⎝ 0  1 ⎠   ⎝ 0 2 ⎠
```

[Nel foglio il prodotto delle prime due, ( 3 12 ; 0 2 ), è scritto sotto una graffa. Conti giusti, verificati con SymPy.]

**es. 3** Nell'es. 3 L_A : ℝ² → ℝ² con A = Rot_θ = ( cos θ  −sin θ ; sin θ  cos θ ) non ha autovettori (se 0 ≠ θ ≠ π). Allora A (o L_A) non è diagonalizzabile.

**Matrici Diagonali**
( λ_1 … 0 ; 0 … λ_n )(x_1 ; ⋮ ; x_n) = (λ_1 x_1 ; ⋮ ; λ_n x_n)  [freccia: diag(λ_1, …, λ_n)]

```
⎛ λ_1  0   0  ⎞ ⎛ μ_1      0  ⎞   ⎛ λ_1 μ_1        0     ⎞
⎜  0  λ_2  0  ⎟ ⎜     ⋱       ⎟ = ⎜          ⋱           ⎟
⎝  0   0  λ_n ⎠ ⎝  0      μ_n ⎠   ⎝    0        λ_n μ_n  ⎠
```

A = diag(λ_1, …, λ_n) ⟹ Aᵏ = A · … · A (k volte) = diag(λ_1ᵏ, …, λ_nᵏ)

**Esempio:** Calcolare A¹⁰⁰ per A = ( 3 4 ; 0 2 )
Metodo 1: A² = A · A = ( 3 4 ; 0 2 )( 3 4 ; 0 2 ) = ( 9 20 ; 0 4 )
  Continuo così → … A² · A² = A⁴ …
Metodo 2: A = M D M⁻¹ con D = ( 3 0 ; 0 2 ), M = ( 1 −4 ; 0 1 ), M⁻¹ = ( 1 4 ; 0 1 )
A¹⁰⁰ = (M D M⁻¹)(M D M⁻¹) ⋯ (M D M⁻¹) = M D (M⁻¹M) D (M⁻¹M) D … (M⁻¹M) D M⁻¹ = M D¹⁰⁰ M⁻¹
[i fattori M⁻¹M sono barrati, con la freccia «id»]

## Pagina 3
A¹⁰⁰ = M · D¹⁰⁰ · M⁻¹

```
      ⎛ 2 −4 ⎞ ⎛ 3¹⁰⁰    0  ⎞ ⎛ 1 4 ⎞   ⎛ 1 −4 ⎞ ⎛ 3¹⁰⁰  4·3¹⁰⁰ ⎞   ⎛ 3¹⁰⁰  4(3¹⁰⁰ − 2¹⁰⁰) ⎞
    = ⎝ 0  1 ⎠ ⎝   0   2¹⁰⁰ ⎠ ⎝ 0 1 ⎠ = ⎝ 0  1 ⎠ ⎝   0     2¹⁰⁰ ⎠ = ⎝   0        2¹⁰⁰      ⎠
```

[Nel primo fattore il primo elemento sembra un 2: è M = ( 1 −4 ; 0 1 ), come nel passaggio dopo. Risultato giusto, verificato con SymPy.]

**Domanda** Quando possiamo diagonalizzare una matrice? Come troviamo gli autovettori e autovalori?

**Def.** Sia A ∈ M(n, 𝕂). Il **polinomio caratteristico** di A è P_A(λ) = det(A − λI_n)

```
                  ⎛ a_11 − λ   a_12      …   a_1n     ⎞
A = (a_ij):  det  ⎜ a_21       a_22 − λ  …   a_2n     ⎟
                  ⎝ a_n1       a_n2      …   a_nn − λ ⎠
```

[Nel foglio «det(A · λI_n)»: va letto A − λI_n.]

**Osservazione**
1) P_A(λ) è un polinomio di grado n
2) Se A, B sono matrici simili (B = M⁻¹ · A · M), allora P_A(λ) = P_B(λ)

**Infatti**
P_B(λ) = det(B − λI_n)
= det(M⁻¹AM − λI_n)
= det(M⁻¹AM − λM⁻¹I_n M)
= det(M⁻¹(A − λI_n)M)
= (det M)⁻¹ · det(A − λI_n) · det M = P_A(λ)   [a margine: «Teorema di Brest»]
[«Brest» va letto Binet. Anche qui «A · λI_n» va letto A − λI_n.]

**Esempio:** A = ( 3 4 ; 0 2 ) la matrice dell'esempio
P_A(λ) = det( 3 − λ  4 ; 0  2 − λ ) = (3 − λ)(2 − λ)
⟹ le radici di A sono λ_1 = 3, λ_2 = 2 che sono esattamente gli autovalori trovati già prima.
[«le radici di A»: del polinomio P_A.]
