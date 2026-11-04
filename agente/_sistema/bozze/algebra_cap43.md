# 43. Sistemi con un Parametro ed Esercizi su Rouché-Capelli
## Un sistema che dipende da un parametro
Si consideri il sistema, con k ∈ ℝ:

x + ky = 4 − k,   kx + 4y = 4.

Si vuole sapere (a) al variare di k se ci sono soluzioni e, in caso affermativo, di che dimensione; (b) qual è la soluzione per k = 1.

**(a)** Si applica l'algoritmo di Gauss su (A | b). Con R_{2} → R_{2} − kR_{1}:

( 1 k | 4 − k ; k 4 | 4 ) → ( 1 k | 4 − k ; 0 4 − k² | 4 − 4k + k² ).

Per calcolare il rango basta fermarsi qui: Gauss-Jordan serve solo se si vogliono determinare precisamente le soluzioni. Si nota che 4 − 4k + k² = (k − 2)². La matrice è ridotta a scalini per tutti i valori di k, e ci sono sempre due pivot tranne per k = 2, dove ce n'è uno solo. Quindi rk(A | b) è 1 per k = 2 e 2 per k ≠ 2.

La matrice dei coefficienti è diventata ( 1 k ; 0 4 − k² ), che ha rango 1 per k = ±2 e rango 2 per k ≠ ±2. Si hanno allora tre casi:
- **k = −2**: rk(A | b) ≠ rk(A), quindi non ci sono soluzioni;
- **k = 2**: rk(A | b) = rk(A) = 1, quindi le soluzioni formano un sottospazio affine di ℝ² di dimensione 2 − 1 = 1, cioè una retta affine: ci sono infinite soluzioni;
- **k ≠ ±2**: rk(A | b) = rk(A) = 2, quindi le soluzioni formano un sottospazio affine di dimensione 2 − 2 = 0, cioè un punto: c'è una soluzione sola.

(In parole povere: si riduce a scalini lasciando k dentro, poi si guarda per quali valori di k un elemento sulla scala si annulla: quelli sono i casi speciali da trattare a parte.)

**(b)** Per k = 1 si ha ( 1 1 | 3 ; 0 3 | 1 ). Dalla seconda riga 3y = 1, cioè y = 1/3; dalla prima x = 3 − y = 3 − 1/3 = 8/3.

## Esercizi
**Esercizio 12.10.** Quante soluzioni ha il sistema con matrice completa ( 1 3 5 | 2 ; 7 9 11 | 2 ; 13 15 17 | 0 )?

Con R_{2} → R_{2} − 7R_{1} e R_{3} → R_{3} − 13R_{1} si ottiene ( 1 3 5 | 2 ; 0 −12 −24 | −12 ; 0 −24 −48 | −26 ), e con R_{3} → R_{3} − 2R_{2} si ottiene ( 1 3 5 | 2 ; 0 −12 −24 | −12 ; 0 0 0 | −2 ). L'ultima riga dice 0 = −2: rk(A) = 2 e rk(A | b) = 3, quindi **nessuna soluzione**.

**Esercizio 12.11.** Trovare tutte le soluzioni di 2x − y − z = 3, x − y + z = 2, 3x − y − 3z = 4.

Conviene scambiare le prime due righe per avere un 1 come primo pivot:

( 1 −1 1 | 2 ; 2 −1 −1 | 3 ; 3 −1 −3 | 4 ).

Con R_{2} → R_{2} − 2R_{1} e R_{3} → R_{3} − 3R_{1} si ottiene ( 1 −1 1 | 2 ; 0 1 −3 | −1 ; 0 2 −6 | −2 ), e con R_{3} → R_{3} − 2R_{2} l'ultima riga si annulla: ( 1 −1 1 | 2 ; 0 1 −3 | −1 ; 0 0 0 | 0 ). Quindi rk(A) = rk(A | b) = 2 e ci sono soluzioni con 3 − 2 = 1 parametro libero. La colonna di z non ha pivot: si pone z = t. Dalla seconda riga y = 3t − 1, dalla prima x = 2 + y − z = 2t + 1. Le soluzioni sono

(x, y, z) = (1, −1, 0) + t(2, 3, 1), al variare di t ∈ ℝ.

Si riconosce la struttura del cap. 41: (1, −1, 0) è una soluzione particolare e t(2, 3, 1) descrive le soluzioni del sistema omogeneo associato.
