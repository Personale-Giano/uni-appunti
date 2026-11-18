# 56. Esercizi Svolti: Rango e Sistemi Lineari con Parametro
## La seconda parte del foglio
Questo capitolo completa gli esercizi del secondo foglio del tutorato (16 novembre 2026) con gli esercizi 8-10; i primi sette sono nel cap. 55. Anche qui il foglio dà solo i testi: le soluzioni **non sono ufficiali**.

Il metodo è uno solo, la riduzione a scalini con le mosse di Gauss (cap. 39), usata in due modi:
- il **rango** di una matrice è il numero dei pivot della sua forma a scalini (cap. 42);
- per un **sistema** Ax = b si riduce la matrice completa (A | b) e si confrontano i due ranghi con il teorema di Rouché-Capelli (cap. 42): nessuna soluzione se rk(A | b) > rk(A); una sola se rk(A | b) = rk(A) = n, il numero delle incognite; infinite se rk(A | b) = rk(A) < n.

Con un parametro k si procede come nel cap. 43: k si tratta come un numero, e ci si ferma a distinguere i casi solo quando un candidato pivot contiene k e quindi può annullarsi.

## Esercizio 8: il rango di tre matrici
**Testo.** Calcolare il rango delle matrici

```
    ( 1  2  3 )        ( 1  2  3  0 )        ( 1  −1   2  3  −2   −1 )
A = ( 2  1  0 )    B = ( 1  1  0  1 )    C = ( 1  −1   0  0  −3    1 )
    ( 0  3  6 )        ( 2  0  1  0 )        ( 2  −2   0  1  −2   −3 )
                       ( 0  3  2  1 )        ( 1  −1  −2  0   8  −12 )
                       ( 3  2  4  1 )
```

Prima di cominciare conviene ricordare il limite del cap. 28: il rango non supera né il numero delle righe né quello delle colonne. Quindi rk(A) ≤ 3, rk(B) ≤ 4 (B ha 5 righe e 4 colonne) e rk(C) ≤ 4 (C ha 4 righe e 6 colonne).

**La matrice A.** Con R_{2} → R_{2} − 2R_{1}, poi R_{3} → R_{3} + R_{2}:

```
( 1  2  3 )      ( 1   2   3 )      ( 1   2   3 )
( 2  1  0 )  →   ( 0  −3  −6 )  →   ( 0  −3  −6 )
( 0  3  6 )      ( 0   3   6 )      ( 0   0   0 )
```

I pivot sono due (1 e −3): **rk(A) = 2**.

Controllo: rango 2 vuol dire che le tre colonne sono dipendenti, e infatti la terza è −(prima) + 2·(seconda): −(1, 2, 0) + 2(2, 1, 3) = (3, 0, 6). Di conseguenza det A = 0.

**La matrice B.** Primo passo: si azzera la prima colonna sotto il pivot, con R_{2} → R_{2} − R_{1}, R_{3} → R_{3} − 2R_{1} e R_{5} → R_{5} − 3R_{1} (la quarta riga ha già uno 0). Secondo passo: si azzera la seconda colonna sotto il pivot −1, con R_{3} → R_{3} − 4R_{2}, R_{4} → R_{4} + 3R_{2} e R_{5} → R_{5} − 4R_{2}.

```
( 1  2  3  0 )      ( 1   2   3  0 )      ( 1   2   3   0 )
( 1  1  0  1 )      ( 0  −1  −3  1 )      ( 0  −1  −3   1 )
( 2  0  1  0 )  →   ( 0  −4  −5  0 )  →   ( 0   0   7  −4 )
( 0  3  2  1 )      ( 0   3   2  1 )      ( 0   0  −7   4 )
( 3  2  4  1 )      ( 0  −4  −5  1 )      ( 0   0   7  −3 )
```

Terzo passo: si azzera la terza colonna sotto il pivot 7, con R_{4} → R_{4} + R_{3} e R_{5} → R_{5} − R_{3}. La quarta riga diventa nulla e va spostata in fondo, scambiandola con la quinta.

```
( 1   2   3   0 )      ( 1   2   3   0 )
( 0  −1  −3   1 )      ( 0  −1  −3   1 )
( 0   0   7  −4 )  →   ( 0   0   7  −4 )
( 0   0   0   0 )      ( 0   0   0   1 )
( 0   0   0   1 )      ( 0   0   0   0 )
```

I pivot sono quattro (1, −1, 7 e 1), uno in ogni colonna: **rk(B) = 4**, il massimo possibile per una matrice con 4 colonne. In altre parole le quattro colonne di B sono linearmente indipendenti (cap. 44). La riga nulla dice invece che le cinque righe sono dipendenti, e non poteva essere altrimenti: sono cinque vettori di ℝ⁴.

**La matrice C.** Primo passo: R_{2} → R_{2} − R_{1}, R_{3} → R_{3} − 2R_{1} e R_{4} → R_{4} − R_{1}.

```
( 1  −1   2  3  −2   −1 )      ( 1  −1   2   3  −2   −1 )
( 1  −1   0  0  −3    1 )  →   ( 0   0  −2  −3  −1    2 )
( 2  −2   0  1  −2   −3 )      ( 0   0  −4  −5   2   −1 )
( 1  −1  −2  0   8  −12 )      ( 0   0  −4  −3  10  −11 )
```

Nella seconda colonna, sotto la prima riga, ci sono solo zeri: lì non c'è nessun pivot e si passa alla terza colonna, dove il pivot è −2. Secondo passo: R_{3} → R_{3} − 2R_{2} e R_{4} → R_{4} − 2R_{2}. Terzo passo: R_{4} → R_{4} − 3R_{3}.

```
( 1  −1   2   3  −2   −1 )      ( 1  −1   2   3  −2  −1 )
( 0   0  −2  −3  −1    2 )  →   ( 0   0  −2  −3  −1   2 )
( 0   0   0   1   4   −5 )      ( 0   0   0   1   4  −5 )
( 0   0   0   3  12  −15 )      ( 0   0   0   0   0   0 )
```

I pivot sono tre (1, −2 e 1), nella prima, terza e quarta colonna: **rk(C) = 3**.

Controllo: la seconda colonna di C è l'opposto della prima, il che è coerente con il fatto che nella seconda colonna non è comparso nessun pivot. Inoltre l'ultima riga nulla dice che le quattro righe di C sono dipendenti.

**Riepilogo.** rk(A) = 2, rk(B) = 4, rk(C) = 3.

## Esercizio 9: quante soluzioni al variare di k
**Testo.** Stabilire, al variare del parametro reale k, quante soluzioni ha il sistema

```
 x +       2y +         z = 2
 x + (k + 2)y + (k² + 1)z = k + 2
2x +       4y +  (k + 2)z = 5
```

**Riduzione.** Si scrive la matrice completa e si azzera la prima colonna con R_{2} → R_{2} − R_{1} e R_{3} → R_{3} − 2R_{1}. Sono mosse sempre lecite, perché non si divide per niente che contenga k:

```
( 1    2       1    |   2   )      ( 1  2  1  | 2 )
( 1  k + 2  k² + 1  | k + 2 )  →   ( 0  k  k² | k )
( 2    4     k + 2  |   5   )      ( 0  0  k  | 1 )
```

I conti della seconda riga: (k + 2) − 2 = k, (k² + 1) − 1 = k², (k + 2) − 2 = k. Quelli della terza: 4 − 4 = 0, (k + 2) − 2 = k, 5 − 4 = 1.

I due candidati pivot della seconda e della terza riga sono entrambi k. Si annullano solo per k = 0, che è quindi l'unico valore da trattare a parte.

**Caso k ≠ 0.** I pivot sono tre (1, k e k), tutti nella parte dei coefficienti: rk(A) = rk(A | b) = 3, che è anche il numero delle incognite. Per Rouché-Capelli **c'è una sola soluzione**.

L'esercizio chiede solo il numero, ma la soluzione si trova in due righe risalendo dal basso. La terza riga dice kz = 1, cioè z = 1/k (si può dividere perché k ≠ 0). La seconda dice ky + k²z = k; dividendo per k, y + kz = 1, e poiché kz = 1 si ha y = 0. La prima dice x + 2y + z = 2, cioè x = 2 − 1/k. La soluzione è (x, y, z) = (2 − 1/k, 0, 1/k).

**Caso k = 0.** Si sostituisce k = 0 nella matrice ridotta:

```
( 1  2  1 | 2 )
( 0  0  0 | 0 )
( 0  0  0 | 1 )
```

La terza riga dice 0 = 1, che è impossibile. In termini di ranghi: la parte dei coefficienti ha una sola riga non nulla, quindi rk(A) = 1, mentre la matrice completa ne ha due, quindi rk(A | b) = 2. I ranghi sono diversi: **non c'è nessuna soluzione**.

**Risposta.** Per **k ≠ 0** il sistema ha **una sola soluzione**; per **k = 0** **non ne ha nessuna**. Non esiste alcun valore di k per cui le soluzioni siano infinite.

Controllo con il determinante (cap. 42): la matrice dei coefficienti ridotta è triangolare, e le mosse usate non cambiano il determinante (cap. 35), quindi det A = 1·k·k = k². È diverso da zero esattamente per k ≠ 0, cioè proprio quando la soluzione è unica. Controllo numerico per k = 1: la formula dà (1, 0, 1), e nel sistema 1 + 0 + 1 = 2, 1 + 0 + 2 = 3 = k + 2, 2 + 0 + 3 = 5.

## Esercizio 10: risolvere al variare di k
**Testo.** Risolvere, al variare di k ∈ ℝ, il sistema

```
 x + 2y + 2z = 1
 x + 4y + 3z = k + 1
−x + 2y + kz = 2
```

**Riduzione.** Con R_{2} → R_{2} − R_{1} e R_{3} → R_{3} + R_{1}, poi R_{3} → R_{3} − 2R_{2}:

```
(  1  2  2 |   1   )      ( 1  2    2   | 1 )      ( 1  2  2 |    1   )
(  1  4  3 | k + 1 )  →   ( 0  2    1   | k )  →   ( 0  2  1 |    k   )
( −1  2  k |   2   )      ( 0  4  k + 2 | 3 )      ( 0  0  k | 3 − 2k )
```

Nell'ultimo passo: 4 − 2·2 = 0, (k + 2) − 2·1 = k e 3 − 2·k = 3 − 2k. La matrice è a scalini per ogni k. I primi due pivot sono 1 e 2 e non dipendono da k; il terzo candidato è k. Di nuovo l'unico valore speciale è k = 0.

**Caso k ≠ 0.** Ci sono tre pivot nella parte dei coefficienti: rk(A) = rk(A | b) = 3 e la soluzione è unica. Si risale dal basso, e ora dividere per k è lecito.
- Terza riga: kz = 3 − 2k, quindi z = (3 − 2k)/k.
- Seconda riga: 2y + z = k, quindi 2y = k − (3 − 2k)/k = (k² + 2k − 3)/k e y = (k² + 2k − 3)/(2k).
- Prima riga: x = 1 − 2y − 2z = 1 − (k² + 2k − 3)/k − (6 − 4k)/k. Portando tutto a denominatore k, il numeratore è k − k² − 2k + 3 − 6 + 4k = −k² + 3k − 3, quindi x = (−k² + 3k − 3)/k.

**Per k ≠ 0 l'unica soluzione è**

```
x = (−k² + 3k − 3)/k      y = (k² + 2k − 3)/(2k)      z = (3 − 2k)/k
```

Il numeratore di y si scompone come (k + 3)(k − 1), quindi si può scrivere anche y = (k + 3)(k − 1)/(2k).

**Caso k = 0.** La matrice ridotta diventa

```
( 1  2  2 | 1 )
( 0  2  1 | 0 )
( 0  0  0 | 3 )
```

La terza riga dice 0 = 3: impossibile. Qui rk(A) = 2 e rk(A | b) = 3, quindi per Rouché-Capelli **per k = 0 il sistema non ha soluzioni**.

**Risposta.** Per **k ≠ 0** il sistema ha l'unica soluzione scritta sopra; per **k = 0** è impossibile. Anche in questo esercizio non c'è nessun valore di k con infinite soluzioni: succederebbe solo se, per lo stesso k, si annullassero insieme il pivot k e il termine noto 3 − 2k, ma per k = 0 il termine noto vale 3.

Controllo per k = 1: la formula dà x = (−1 + 3 − 3)/1 = −1, y = 0, z = 1. Nel sistema: −1 + 0 + 2 = 1; −1 + 0 + 3 = 2 = k + 1; 1 + 0 + 1 = 2. Controllo per k = 3: x = (−9 + 9 − 3)/3 = −1, y = (9 + 6 − 3)/6 = 2, z = (3 − 6)/3 = −1. Nel sistema: −1 + 4 − 2 = 1; −1 + 8 − 3 = 4 = k + 1; 1 + 4 − 3 = 2.

## Che cosa ricordare
I due esercizi con il parametro hanno la stessa struttura del cap. 43, e conviene fissare l'ordine dei passi:
1. si riduce a scalini la matrice completa tenendo k come un numero, usando solo mosse che non dividono per espressioni con k;
2. si guardano i candidati pivot che contengono k e si trovano i valori che li annullano: sono i casi speciali;
3. fuori dai casi speciali si contano i pivot e si applica Rouché-Capelli; se servono le soluzioni, si risale dal basso;
4. ogni caso speciale si tratta a parte, sostituendo il valore di k nella matrice ridotta e rileggendo i ranghi.

L'errore più frequente è fermarsi al punto 3 e dimenticare i valori speciali, oppure dividere per k senza aver prima escluso k = 0.
