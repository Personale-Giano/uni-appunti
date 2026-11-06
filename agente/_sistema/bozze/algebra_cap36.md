# 36. L'Inversa di una Matrice: Teorema di Binet e Cofattori
## Che cosa vuol dire «inversa»
Se A e B sono matrici n × n, anche il prodotto A · B è una matrice n × n. La matrice **identità** I_{n} (1 sulla diagonale, 0 altrove) è l'elemento neutro del prodotto: per ogni matrice A ∈ M(n) vale **A · I_{n} = I_{n} · A = A**.

**Definizione.** Una matrice A ∈ M(n) è detta **invertibile** se esiste una matrice B ∈ M(n) tale che **A · B = B · A = I_{n}**. In tal caso B si chiama **inversa** di A e si indica con **A^{-1}**.

**In parole povere:** l'inversa è la matrice che «annulla» A, come 1/3 annulla il 3 nella moltiplicazione dei numeri: moltiplicando A per la sua inversa si torna all'identità.

**Attenzione:** la definizione chiede entrambe le uguaglianze A · B = I_{n} e B · A = I_{n}, e se una tale B esiste è unica. Per le matrici quadrate, in realtà, una sola delle due garantisce l'altra: se A · B = I_{n}, per il Teorema di Binet det A ≠ 0, quindi per il teorema della formula dell'inversa, più avanti in questo capitolo, esiste C = (1/det A) · ᵗcof(A) con C · A = I_{n}, e allora B = (C · A) · B = C · (A · B) = C.

Il capitolo risponde a due domande: **quando** una matrice è invertibile, e **come** si calcola la sua inversa.

## Quando è invertibile: il Teorema di Binet
**Teorema (Binet).** Per ogni A, B ∈ M(n) vale **det(A · B) = det A · det B.**

(Il teorema si usa senza dimostrarlo.) **In parole povere:** il determinante di un prodotto è il prodotto dei determinanti.

**Conseguenza.** Se A è invertibile, esiste A^{-1} con A · A^{-1} = I_{n}. Prendendo i determinanti e usando det(I_{n}) = 1 (cap. 32):
det A · det(A^{-1}) = det(A · A^{-1}) = det(I_{n}) = 1.
Quindi **det A ≠ 0** e **det(A^{-1}) = 1 / det A.**

Una matrice invertibile ha dunque determinante diverso da zero. Vale anche il viceversa, come si vede costruendo l'inversa.

## I cofattori
**Definizione.** Data A ∈ M(n), il **cofattore** di posto (i, j) è
**cof_{ij} = (−1)^{i+j} · det(C_{ij})**,
dove C_{ij} è la sottomatrice ottenuta da A cancellando la riga i e la colonna j (cap. 33). La matrice **cof(A)**, che ha come elemento di posto (i, j) il cofattore cof_{ij}, si chiama **matrice dei cofattori** di A.

**In parole povere:** un cofattore è il determinante della sottomatrice che resta tagliando una riga e una colonna, preso con il segno «a scacchiera» (+ − + …) della sua casella. Con i cofattori lo sviluppo di Laplace si riscrive in modo più breve: det A = Σ_{j=1}^{n} a_{ij} · cof_{ij}, per ogni riga i.

## La formula dell'inversa
**Teorema.** Se A ∈ M(n), con n ≥ 2, ha det A ≠ 0, allora A è invertibile e
**A^{-1} = (1 / det A) · ᵗcof(A).**

**Perché funziona.** Si dimostra che A · ᵗcof(A) = det A · I_{n}: l'elemento di posto (i, i) di questo prodotto è proprio lo sviluppo di Laplace di det A lungo la riga i; l'elemento di posto (i, j) con i ≠ j è lo sviluppo del determinante di una matrice con due righe uguali, quindi vale 0. Dividendo per det A (che è diverso da zero) si ottiene A · B = I_{n}, con B = (1/det A) · ᵗcof(A), e analogamente B · A = I_{n}.

**In parole povere:** per invertire una matrice si calcola la matrice dei cofattori, la si trasforma nella trasposta e si divide tutto per il determinante.

Insieme al paragrafo precedente: **A è invertibile se e solo se det A ≠ 0.**

## Il caso 2 × 2
Per A = ( a b ; c d ) i cofattori sono cof₁₁ = d, cof₁₂ = −c, cof₂₁ = −b, cof₂₂ = a, quindi cof(A) = ( d −c ; −b a ) e, trasponendo,
**A^{-1} = (1 / (ad − bc)) · ( d −b ; −c a ).**

Nel caso 2 × 2 si può fare velocemente: si **scambiano i due elementi della diagonale principale**, si **cambia il segno** a quelli dell'altra diagonale e si divide per il determinante ad − bc.

## Un esempio completo
Sia A = ( 1 0 1 ; 0 2 1 ; 3 0 0 ).

**È invertibile?** Si calcola il determinante sviluppando lungo la terza riga, che ha due zeri: l'unico elemento non nullo è 3, in riga 3 e colonna 1 (3 + 1 = 4 pari, segno +), con sottomatrice ( 0 1 ; 2 1 ), che ha determinante −2. Quindi det A = 3 · (−2) = **−6 ≠ 0**: A è invertibile.

**I nove cofattori:**
- cof₁₁ = + det( 2 1 ; 0 0 ) = 0;
- cof₁₂ = − det( 0 1 ; 3 0 ) = −(−3) = 3;
- cof₁₃ = + det( 0 2 ; 3 0 ) = −6;
- cof₂₁ = − det( 0 1 ; 0 0 ) = 0;
- cof₂₂ = + det( 1 1 ; 3 0 ) = −3;
- cof₂₃ = − det( 1 0 ; 3 0 ) = 0;
- cof₃₁ = + det( 0 1 ; 2 1 ) = −2;
- cof₃₂ = − det( 1 1 ; 0 1 ) = −1;
- cof₃₃ = + det( 1 0 ; 0 2 ) = 2.

Dunque cof(A) = ( 0 3 −6 ; 0 −3 0 ; −2 −1 2 ).

**L'inversa.** Trasponendo si ha ᵗcof(A) = ( 0 0 −2 ; 3 −3 −1 ; −6 0 2 ), e quindi
A^{-1} = (1 / (−6)) · ( 0 0 −2 ; 3 −3 −1 ; −6 0 2 ) = ( 0 0 1/3 ; −1/2 1/2 1/6 ; 1 0 −1/3 ).

Verifica: moltiplicando A per questa matrice si ottiene I₃.

Il capitolo successivo applica la formula agli esercizi della dispensa.
