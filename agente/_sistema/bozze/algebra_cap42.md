# 42. Il Teorema di Rouché-Capelli
## Il sistema letto con le colonne
Il sistema si può riscrivere usando le colonne A^{1}, …, A^{n} di A. Il passaggio, come alla lavagna della registrazione 2025, è questo: il vettore con componenti a_{i1}x_{1} + … + a_{in}x_{n} si spezza in una somma di n vettori, il primo con tutti i termini in x_{1}, il secondo con tutti quelli in x_{2} e così via. In ciascuno la stessa incognita compare in ogni componente, quindi si porta fuori:

x_{1}( a_{11} ; … ; a_{k1} ) + x_{2}( a_{12} ; … ; a_{k2} ) + … + x_{n}( a_{1n} ; … ; a_{kn} ) = b,   cioè   x_{1}A^{1} + … + x_{n}A^{n} = b.

È un altro modo di scrivere A · x = b (cap. 41).

A questo punto è chiaro che esistono soluzioni se e solo se b è **combinazione lineare delle colonne**, con coefficienti x_{1}, …, x_{n}: il sistema ha soluzioni se e solo se

b ∈ Span(A^{1}, …, A^{n}).

(In parole povere: risolvere il sistema vuol dire chiedersi se il vettore b si può costruire mescolando le colonne di A, e con quali dosi.)

## Il rango con le mosse di Gauss
Il **rango** di A è il massimo numero di colonne linearmente indipendenti di A (cap. 28). Le mosse di Gauss non cambiano lo spazio generato dalle righe, quindi non cambiano il rango (per righe, che coincide con quello per colonne). Con l'algoritmo di Gauss-Jordan si può fare in modo che le r colonne con i pivot siano precisamente i primi r vettori e_{1}, …, e_{r} della base canonica di 𝕂^{k}, e tutte le altre colonne sono combinazioni lineari di questi. Si conclude che **il rango di A è il numero di pivot in una sua qualsiasi riduzione a scalini**.

(In parole povere: per calcolare il rango basta ridurre la matrice a scalini e contare gli scalini.)

Per esempio ( 1 0 1 ; 1 1 0 ; 0 1 −1 ) si riduce a ( 1 0 1 ; 0 1 −1 ; 0 0 0 ): ha due pivot, quindi rango 2.

Attenzione: valgono le mosse **sulle righe**. La ricetta della lavagna (registrazione 2025) è: si fa Gauss su (A | b) e si contano i pivot di A e quelli di (A | b).

## Il teorema
**Teorema (Rouché-Capelli).** Il sistema ha soluzioni se e solo se rk(A | b) = rk(A). In caso affermativo, lo spazio delle soluzioni S ⊂ 𝕂ⁿ è un sottospazio affine di dimensione n − rk(A).

(In parole povere: se aggiungere la colonna dei termini noti non aumenta il rango, b «non porta niente di nuovo» e il sistema si può risolvere. Le soluzioni hanno poi tanti gradi di libertà quante sono le variabili meno il rango.)

Nella registrazione 2025 il teorema è scritto con i parametri: il numero di parametri liberi è n − numero di pivot = n − rk(A), dove n è il numero di incognite. Nella lezione 13 della stessa serie compare anche una seconda forma: se (A | b) si riduce a scalini in (A′ | c), il sistema ha soluzioni se e solo se **tutti i pivot stanno in A′**, cioè nessun pivot è nell'ultima colonna.

**Dimostrazione.** Il sistema ha soluzioni se e solo se b ∈ Span(A^{1}, …, A^{n}). Questo accade se e solo se Span(A^{1}, …, A^{n}, b) = Span(A^{1}, …, A^{n}). Le dimensioni di questi due spazi sono rk(A | b) e rk(A), e il primo contiene il secondo: sono uguali se e solo se rk(A | b) = rk(A).

Se ci sono soluzioni, la dimensione di S è pari alla dimensione di S_{0}, lo spazio delle soluzioni del sistema omogeneo associato. Dopo l'algoritmo di Gauss-Jordan, come visto nel cap. 40, S_{0} è generato da un numero di vettori indipendenti pari a n meno il numero di pivot, cioè n − rk(A). Quindi dim S = dim S_{0} = n − rk(A).

## Quante soluzioni ha un sistema
Nel corollario seguente 𝕂 è un campo infinito, come ℚ, ℝ e ℂ.

**Corollario.** Il sistema ha 0, 1 oppure ∞ soluzioni. Più precisamente le soluzioni sono:
- **0** se rk(A | b) > rk(A);
- **1** se rk(A | b) = rk(A) = n;
- **∞** se rk(A | b) = rk(A) < n.

(In parole povere: un sistema lineare non può avere esattamente due o tre soluzioni: o nessuna, o una, o infinite.)

![I tre casi nel sistema con parametro del cap. 43, per tre valori di k: due rette che si incontrano, due rette parallele, una retta sola.](figure/alg/rouche_tre_casi.png|16)

**Corollario.** Se A è una matrice quadrata, quindi con tante equazioni quante variabili, il sistema Ax = b ha esattamente una soluzione se e solo se rk A = n, cioè se e solo se det A ≠ 0. In questo caso A è invertibile e la soluzione è x = A^{-1}b.

(In parole povere: con tante equazioni quante incognite, basta calcolare il determinante: se non è zero la soluzione c'è ed è una sola.)

Qui i sistemi si collegano con il determinante e l'inversa (cap. 31-36).

## Collegamento con l'informatica: la programmazione lineare
In un corso successivo di ottimizzazione si studiano i problemi di **programmazione lineare** del tipo max{ ᵗcx | Ax = b, x ≥ 0 }. Il **metodo del simplesso** usa insieme molti concetti visti fin qui. Se A ha m righe e rango m, una ~base~ del simplesso è una scelta di m colonne linearmente indipendenti di A, che formano una matrice quadrata A_{B} invertibile. Ponendo uguali a zero le variabili corrispondenti alle altre colonne, le variabili di base si ottengono risolvendo A_{B}x_{B} = b, cioè x_{B} = A_{B}^{-1}b. Indipendenza lineare, base, rango, matrice invertibile e soluzione di un sistema compaiono quindi tutti insieme in uno degli algoritmi fondamentali dell'ottimizzazione.
