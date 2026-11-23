<!-- fonte: _sistema/fonti/Appunti/Algebra_2026/4 Novembre/4 Novembre.pdf -->
# Algebra lineare, lezione 13: Sistemi lineari III (4 novembre 2026): appunti a mano di Emanuele
(Trascrizione dell'unica pagina del PDF, fatta il 23 nov 2026. Il foglio non ha il numero di lezione: è la lezione 13 per data e contenuto (Rouché-Capelli ripreso, poi applicazioni all'indipendenza lineare, cap. 42 e 44). Gli appunti occupano solo il primo quinto della pagina e l'esempio resta senza conclusione.)

## Pagina 1
**Teorema di Rouché Capelli**
Sistema di eq. lineari A x = b con n incognite. Allora:
- il sistema ammette soluzione ⟺ rg(A) = rg(A|b)
- Se una sol. esiste, dipende da n − rg(A) parametri

A lato:
- rg(A) ≠ rg(A|b) ⇝ NO SOLUZIONI
- rg(A) = rg(A|b) = n ⇝ 1 SOL
- rg(A) = rg(A|b) < n ⇝ ∞ SOL

**Indipendenza lineare**

**Es.**

```
       ⎛ 1 ⎞        ⎛  1 ⎞        ⎛ 3 ⎞
v_1 =  ⎜ 5 ⎟ , v_2 = ⎜ −1 ⎟ , v_3 = ⎜ 3 ⎟     l.i.?
       ⎝ 3 ⎠        ⎝  1 ⎠        ⎝ 5 ⎠
```

x_1 · v_1 + x_2 · v_2 + x_3 · v_3 = 0_V → 2 casi:
① L'unica soluzione è x_1 = 0, x_2 = 0, x_3 = 0
② ∃ altra soluzione

[Fine degli appunti: l'esempio non è concluso. Verifica fatta con SymPy: la matrice (v_1 | v_2 | v_3) ha rango 2 e v_3 = v_1 + 2v_2, quindi i tre vettori sono linearmente dipendenti (caso ②, soluzioni t(−1, −2, 1)).]
