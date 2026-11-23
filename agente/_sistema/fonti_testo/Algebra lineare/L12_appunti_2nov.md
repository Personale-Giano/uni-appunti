<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/2 Novembre/2 Novembre.pdf -->
# Algebra lineare, lezione 12: Sistemi lineari II (2 novembre 2026): appunti a mano di Emanuele
(Trascrizione dell'unica pagina del PDF, fatta il 23 nov 2026. Formule in Unicode, matrici e sistemi riga per riga. Tra parentesi quadre le note di lettura. Il foglio si ferma a metà pagina: il resto della lezione non è negli appunti.)

## Pagina 1
**Sistemi Lineari 2 – Lezione 12**

Sia

```
      ⎧ a_11 x_1 + … + a_1n x_n = b_1
(*)   ⎨   ⋮
      ⎩ a_k1 x_1 + … + a_kn x_n = b_k
```

un sistema lin. con n variabili e k eq.

**Def.** Il **sistema omogeneo associato** a(*) è

```
      ⎧ a_11 x_1 + … + a_1n x_n = 0
(**)  ⎨   ⋮
      ⎩ a_k1 x_1 + … + a_kn x_n = 0
```

Ottenuto da (*) mettendo a 0 tutti i termini noti.

La matrice completa di (*) è C = (A | b), mentre la matrice completa di (**) è C = (A | 0) o semplicemente A.
Sia S l'insieme delle soluzioni di (*) e S_0 l'insieme delle sol. di (**).

**Prop.** S_0 ⊂ 𝕂ⁿ è un sottospazio.

**Dim.**
1) 0 = (0 ; ⋮ ; 0) ∈ S_0. La i-esima eq. è soddisfatta:
   a_i1 · 0 + a_i2 · 0 + … + a_in · 0 = 0 ✓ ⟹ 0 ∈ S_0.
2) Siano x = (x_1 ; ⋮ ; x_n) e y = (y_1 ; ⋮ ; y_n) ∈ S_0 ⟹ a_i1 x_1 + … + a_in x_n = 0 e a_i1 y_1 + … + a_in y_n = 0
   ⟹ a_i1 (x_1 + y_1) + … + a_in (x_n + y_n) = 0 + 0 = 0 ⟹ x + y = (x_1 + y_1 ; ⋮ ; x_n + y_n) ∈ S_0.
3) Sia x = (x_1 ; ⋮ ; x_n) ∈ S_0 e λ ∈ 𝕂
   ⟹ a_i1 x_1 + … + a_in x_n = 0
   ⟹ λ(a_i1 x_1 + … + a_in x_n) = a_i1 (λx_1) + … + a_in (λx_n) = λ · 0 = 0
   ⟹ λx ∈ S_0.
