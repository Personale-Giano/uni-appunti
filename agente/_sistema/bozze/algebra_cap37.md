# 37. Esercizi sull'Inversa di una Matrice
## Il metodo in tre passi
Gli esercizi 10.10, 10.11 e 10.12 si risolvono sempre con lo stesso metodo in tre passi:
1. si calcola il **determinante**: se è 0 la matrice **non è invertibile**; se è diverso da 0, lo è;
2. si calcolano i **cofattori** cof_{ij} = (−1)^{i+j} det(C_{ij}) e si scrive la matrice cof(A);
3. si traspone e si divide per il determinante: **A^{-1} = (1 / det A) · ᵗcof(A)** (cap. 36).

**In parole povere:** prima si controlla che l'inversa esista, poi la si costruisce con la formula.

Nota: gli esercizi propongono solo i testi; gli svolgimenti qui sotto applicano la formula del capitolo precedente.

## Esercizio 10.10: una matrice con un parametro
**Testo.** Determinare per quali valori di k ∈ R la matrice A = ( k−5 3 ; −2 k ) è invertibile e, per questi valori, trovare l'inversa.

**Svolgimento.** Il determinante è
det A = (k − 5) · k − 3 · (−2) = k² − 5k + 6 = (k − 2)(k − 3).
La matrice è invertibile se e solo se det A ≠ 0, cioè **per k ≠ 2 e k ≠ 3**.

Per questi valori si usa la formula del caso 2 × 2 (cap. 36): si scambiano gli elementi della diagonale principale, si cambia segno agli altri due e si divide per il determinante:
**A^{-1} = (1 / (k² − 5k + 6)) · ( k −3 ; 2 k−5 ).**

## Esercizio 10.11: una matrice 3 × 3
**Testo.** Dimostrare che B = ( 2 −1 0 ; −2 1 1 ; 1 −1 3 ) è invertibile e calcolarne l'inversa.

**Determinante.** Sviluppando lungo la prima riga (segni + − +, il terzo elemento è 0):
det B = 2 · det( 1 1 ; −1 3 ) − (−1) · det( −2 1 ; 1 3 ) + 0 = 2 · 4 + 1 · (−7) = 8 − 7 = **1 ≠ 0**.
Dunque B è invertibile (e, poiché i cofattori sono interi e si divide per det B = 1, l'inversa avrà solo numeri interi).

**Cofattori.**
- cof₁₁ = + det( 1 1 ; −1 3 ) = 4; cof₁₂ = − det( −2 1 ; 1 3 ) = 7; cof₁₃ = + det( −2 1 ; 1 −1 ) = 1;
- cof₂₁ = − det( −1 0 ; −1 3 ) = 3; cof₂₂ = + det( 2 0 ; 1 3 ) = 6; cof₂₃ = − det( 2 −1 ; 1 −1 ) = 1;
- cof₃₁ = + det( −1 0 ; 1 1 ) = −1; cof₃₂ = − det( 2 0 ; −2 1 ) = −2; cof₃₃ = + det( 2 −1 ; −2 1 ) = 0.

Quindi cof(B) = ( 4 7 1 ; 3 6 1 ; −1 −2 0 ) e, trasponendo e dividendo per det B = 1,
**B^{-1} = ( 4 3 −1 ; 7 6 −2 ; 1 1 0 ).**

Verifica: la prima riga di B per la prima colonna di B^{-1} dà 2 · 4 + (−1) · 7 + 0 · 1 = 1, e per la seconda colonna 2 · 3 + (−1) · 6 + 0 = 0, come deve essere per l'identità.

## Esercizio 10.12: una matrice con numeri complessi
**Testo.** Calcolare l'inversa di C = ( 2−i 0 ; 3 2+i ).

**Svolgimento.** Il determinante è (2 − i)(2 + i) − 0 · 3 = 4 − i² = 4 + 1 = **5 ≠ 0**. Con la formula del caso 2 × 2: si scambiano gli elementi della diagonale principale (2 − i e 2 + i) e si cambia segno agli altri (0 e 3):
**C^{-1} = (1 / 5) · ( 2+i 0 ; −3 2−i ) = ( (2+i)/5 0 ; −3/5 (2−i)/5 ).**

Verifica: il prodotto della prima riga di C per la prima colonna di C^{-1} è (2 − i)(2 + i)/5 + 0 = 1, e quello della seconda riga per la prima colonna è 3 · (2 + i)/5 + (2 + i) · (−3)/5 = 0, come deve essere.

Come si vede, la formula funziona uguale con i numeri complessi: bastano le regole del calcolo con i e il fatto che (2 − i)(2 + i) = 5.
