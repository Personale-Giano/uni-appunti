# 55. Esercizi Svolti: Sottospazi, Indipendenza, Basi e Coordinate
## Il secondo foglio del tutorato
Questo capitolo e il successivo raccolgono gli esercizi del secondo foglio del tutorato (16 novembre 2026). Il foglio propone solo i testi: le soluzioni che seguono usano i metodi dei capitoli precedenti e **non sono soluzioni ufficiali**.

Qui si trovano gli esercizi 1-7, che riguardano sottospazi, indipendenza lineare, basi e coordinate. Gli strumenti sono sempre gli stessi tre:
- per decidere se un insieme è un **sottospazio** si controllano le tre condizioni del cap. 20: contiene lo zero, è chiuso per la somma, è chiuso per il prodotto per scalare. Se anche una sola fallisce, non è un sottospazio, e basta un controesempio;
- per **indipendenza e generatori** si scrive la matrice con i vettori in colonna e la si riduce a scalini (cap. 39): un pivot in ogni colonna vuol dire indipendenti, un pivot in ogni riga vuol dire generatori (cap. 44);
- per le **coordinate** rispetto a una base si risolve il sistema lineare che ha i vettori della base come colonne e il vettore dato come termine noto (cap. 25 e 44).

## Esercizio 1: le matrici antisimmetriche 3 × 3
**Testo.** Nello spazio V = M(3, ℝ) delle matrici reali 3 × 3 si considera l'insieme W delle matrici antisimmetriche, cioè quelle con ᵗA = −A. Mostrare che W è un sottospazio vettoriale di V e calcolarne la dimensione.

**W è un sottospazio.** Si controllano le tre condizioni del cap. 20, usando due proprietà della trasposta (cap. 27): ᵗ(A + B) = ᵗA + ᵗB e ᵗ(λA) = λ·ᵗA.
1. La matrice nulla sta in W: la sua trasposta è ancora la matrice nulla, che è uguale al proprio opposto.
2. Se A e B stanno in W, cioè ᵗA = −A e ᵗB = −B, allora ᵗ(A + B) = ᵗA + ᵗB = −A − B = −(A + B). Quindi anche A + B sta in W.
3. Se A sta in W e λ ∈ ℝ, allora ᵗ(λA) = λ·ᵗA = λ·(−A) = −(λA). Quindi anche λA sta in W.

Le tre condizioni valgono, dunque **W è un sottospazio di M(3, ℝ)**. È il sottospazio che nel cap. 21 si chiama A(3).

**La dimensione.** Per calcolare una dimensione si cerca una base e si contano i suoi elementi (cap. 26). Conviene prima capire com'è fatta una matrice di W. La condizione ᵗA = −A, scritta entrata per entrata, dice a_{ji} = −a_{ij}. Sulla diagonale (i = j) diventa a_{ii} = −a_{ii}, quindi a_{ii} = 0. Fuori dalla diagonale, ogni entrata sotto è l'opposto di quella simmetrica sopra. Restano libere solo le tre entrate sopra la diagonale, che si chiamano a, b, c:

```
    (  0   a   b )
A = ( −a   0   c )
    ( −b  −c   0 )
```

Questa matrice si spezza in tre pezzi, uno per ogni lettera:

```
      (  0  1  0 )       (  0  0  1 )       ( 0   0  0 )
A = a·( −1  0  0 ) + b·(  0  0  0 ) + c·( 0   0  1 )
      (  0  0  0 )       ( −1  0  0 )       ( 0  −1  0 )
```

Si chiamino N_{1}, N_{2}, N_{3} le tre matrici di destra, nell'ordine. Sono antisimmetriche, e formano una base di W:
- **generano** W, perché ogni matrice antisimmetrica è della forma a·N_{1} + b·N_{2} + c·N_{3}, come appena visto;
- sono **linearmente indipendenti**, perché a·N_{1} + b·N_{2} + c·N_{3} è la matrice A scritta sopra, ed è la matrice nulla solo se a = b = c = 0.

La base ha tre elementi, quindi **dim W = 3**.

Controllo: M(3, ℝ) ha dimensione 9 (cap. 26). La condizione ᵗA = −A azzera le 3 entrate della diagonale e lega le 3 entrate sotto la diagonale a quelle sopra: delle 9 entrate ne restano libere 9 − 3 − 3 = 3.

## Esercizio 2: sei sottoinsiemi di polinomi
**Testo.** Per ciascuno dei seguenti sottoinsiemi di ℝ_{2}[x], lo spazio dei polinomi reali di grado al più 2, stabilire se è un sottospazio; quando lo è, trovarne la dimensione.
1. I polinomi p(x) con p(1) = 0.
2. I polinomi p(x) con p(0) = 1.
3. I polinomi ax² + bx + c con a = c e b = 0.
4. I polinomi ax² + bx + c con b > 0.
5. I polinomi della forma (1 + t)x² + tx, al variare di t ∈ ℝ.
6. I polinomi della forma (t + s)x² − tx − s, al variare di s, t ∈ ℝ.

Il primo controllo da fare è sempre il più veloce: lo zero dello spazio, che qui è il polinomio nullo, appartiene all'insieme? Se non c'è, l'insieme non è un sottospazio e l'esercizio è finito.

**Insieme 1: p(1) = 0.** È un sottospazio.
1. Il polinomio nullo vale 0 in ogni punto, quindi anche in x = 1.
2. Se p(1) = 0 e q(1) = 0, allora (p + q)(1) = p(1) + q(1) = 0 + 0 = 0.
3. Se p(1) = 0 e λ ∈ ℝ, allora (λp)(1) = λ·p(1) = λ·0 = 0.

Per la dimensione si scrive p(x) = ax² + bx + c. La condizione p(1) = 0 è a + b + c = 0, cioè c = −a − b. Sostituendo:

p(x) = ax² + bx − a − b = a(x² − 1) + b(x − 1).

Quindi ogni polinomio dell'insieme è combinazione lineare di x² − 1 e x − 1, che stanno nell'insieme perché si annullano in 1. I due polinomi sono indipendenti, perché hanno grado diverso e quindi nessuno dei due è multiplo dell'altro. Formano una base: **è un sottospazio di dimensione 2**.

**Insieme 2: p(0) = 1.** Il polinomio nullo vale 0 in x = 0, non 1: non appartiene all'insieme. **Non è un sottospazio.**

**Insieme 3: a = c e b = 0.** I polinomi dell'insieme sono quelli della forma ax² + a = a(x² + 1), al variare di a ∈ ℝ. L'insieme è quindi Span(x² + 1), e uno Span è sempre un sottospazio (cap. 22). È generato da un solo polinomio non nullo, che da solo è indipendente (cap. 24): **è un sottospazio di dimensione 1**.

**Insieme 4: b > 0.** Il polinomio nullo ha b = 0, e 0 > 0 è falso: non appartiene all'insieme. **Non è un sottospazio.** Si vede anche dal prodotto per scalare: x sta nell'insieme (b = 1), ma (−1)·x = −x no (b = −1).

**Insieme 5: (1 + t)x² + tx.** Il polinomio nullo ha tutti i coefficienti nulli, quindi servirebbe un t con 1 + t = 0 e insieme t = 0: impossibile, perché la prima chiede t = −1 e la seconda t = 0. Il polinomio nullo non appartiene all'insieme: **non è un sottospazio.**

Qui serve attenzione, perché a prima vista l'insieme sembra «parametrizzato da t» come uno Span. La differenza si vede riscrivendo (1 + t)x² + tx = x² + t(x² + x): c'è un pezzo fisso, x², che non è moltiplicato per il parametro. L'insieme è Span(x² + x) spostato di x², e uno Span spostato non passa per lo zero.

**Insieme 6: (t + s)x² − tx − s.** Si raccolgono i due parametri:

(t + s)x² − tx − s = t(x² − x) + s(x² − 1).

Stavolta non c'è nessun pezzo fisso: l'insieme è esattamente Span(x² − x, x² − 1), quindi è un sottospazio (cap. 22). I due generatori sono indipendenti: se t(x² − x) + s(x² − 1) è il polinomio nullo, il coefficiente di x dà −t = 0 e il termine noto dà −s = 0. Formano una base: **è un sottospazio di dimensione 2**.

Un'osservazione in più: x² − x e x² − 1 si annullano entrambi in x = 1, quindi l'insieme 6 è contenuto nell'insieme 1. Hanno tutti e due dimensione 2, e un sottospazio contenuto in un altro della stessa dimensione coincide con esso: **gli insiemi 1 e 6 sono lo stesso sottospazio**, descritto in due modi diversi (una volta con una condizione, una volta con dei generatori, i due modi del cap. 22).

**Riepilogo.** Sono sottospazi gli insiemi 1 (dimensione 2), 3 (dimensione 1) e 6 (dimensione 2). Non lo sono gli insiemi 2, 4 e 5, e in tutti e tre i casi manca il polinomio nullo.

## Esercizio 3: indipendenti, generatori o base?
**Testo.** Per ciascuna delle tre famiglie di vettori, stabilire se i vettori sono linearmente indipendenti, se generano lo spazio indicato e se ne formano una base.
1. In ℝ²: v_{1} = (−1, −1), v_{2} = (2, 0), v_{3} = (3, 1).
2. In ℝ³: v_{1} = (1, 1, 2), v_{2} = (0, 1, −1), v_{3} = (3, 1, 6).
3. In ℝ⁴: v_{1} = (1, 1, 2, 3), v_{2} = (0, 1, −1, 0), v_{3} = (3, 1, 8, 9).

In tutti e tre i casi si mettono i vettori in colonna e si riduce a scalini con le mosse di Gauss.

**Famiglia 1.** Con R_{2} → R_{2} − R_{1}:

```
( −1  2  3 )      ( −1   2   3 )
( −1  0  1 )  →   (  0  −2  −2 )
```

I pivot sono due (−1 e −2), uno per riga. Ogni riga ha un pivot, quindi i vettori **generano ℝ²**. La terza colonna invece non ha pivot, quindi **non sono indipendenti**. Si poteva dire subito: ℝ² ha dimensione 2 e tre vettori in uno spazio di dimensione 2 sono sempre dipendenti. Non essendo indipendenti, **non sono una base**.

La relazione di dipendenza si trova cercando v_{3} = a·v_{1} + b·v_{2}: la seconda componente dà −a = 1, cioè a = −1; la prima dà −a + 2b = 3, cioè b = 1. Quindi v_{3} = −v_{1} + v_{2}. Controllo: −(−1, −1) + (2, 0) = (1, 1) + (2, 0) = (3, 1).

**Famiglia 2.** Con R_{2} → R_{2} − R_{1} e R_{3} → R_{3} − 2R_{1}, poi R_{3} → R_{3} + R_{2}:

```
( 1   0  3 )      ( 1   0   3 )      ( 1  0   3 )
( 1   1  1 )  →   ( 0   1  −2 )  →   ( 0  1  −2 )
( 2  −1  6 )      ( 0  −1   0 )      ( 0  0  −2 )
```

I pivot sono tre (1, 1 e −2): ce n'è uno in ogni colonna e uno in ogni riga. I vettori sono **indipendenti**, **generano ℝ³** e quindi **sono una base di ℝ³**.

Controllo con il determinante (sviluppo lungo la prima riga, cap. 33): det = 1·(1·6 − 1·(−1)) − 0 + 3·(1·(−1) − 1·2) = 7 − 9 = −2 ≠ 0.

**Famiglia 3.** Con R_{2} → R_{2} − R_{1}, R_{3} → R_{3} − 2R_{1} e R_{4} → R_{4} − 3R_{1}, poi R_{3} → R_{3} + R_{2}:

```
( 1   0  3 )      ( 1   0   3 )      ( 1  0   3 )
( 1   1  1 )  →   ( 0   1  −2 )  →   ( 0  1  −2 )
( 2  −1  8 )      ( 0  −1   2 )      ( 0  0   0 )
( 3   0  9 )      ( 0   0   0 )      ( 0  0   0 )
```

I pivot sono solo due. La terza colonna non ha pivot, quindi i vettori **non sono indipendenti**; ci sono righe nulle, quindi **non generano ℝ⁴** (del resto tre vettori non possono generare uno spazio di dimensione 4). **Non sono una base.** Lo spazio che generano ha dimensione 2, il numero dei pivot.

La relazione di dipendenza si legge dalla matrice ridotta, risolvendo il sistema omogeneo: la seconda riga dà λ_{2} − 2λ_{3} = 0 e la prima λ_{1} + 3λ_{3} = 0. Con λ_{3} = −1 si ha λ_{1} = 3 e λ_{2} = −2, cioè v_{3} = 3v_{1} − 2v_{2}. Controllo: 3(1, 1, 2, 3) − 2(0, 1, −1, 0) = (3, 3 − 2, 6 + 2, 9) = (3, 1, 8, 9).

**Riepilogo.** Famiglia 1: generatori, non indipendenti, non base. Famiglia 2: indipendenti, generatori, base. Famiglia 3: né indipendenti né generatori, non base.

## Esercizio 4: tre polinomi di grado al più 3
**Testo.** In ℝ_{3}[x], lo spazio dei polinomi reali di grado al più 3, si considerano f(x) = 2x³ − x² + x − 1, g(x) = x² + x e h(x) = x³ + x − 2. Sono linearmente indipendenti? Formano una base di ℝ_{3}[x]?

**Dai polinomi ai vettori.** Un polinomio di ℝ_{3}[x] è determinato dai suoi quattro coefficienti, che sono le sue coordinate rispetto alla base canonica 1, x, x², x³ (cap. 26). Si scrive ogni polinomio come colonna, con i coefficienti in quest'ordine (termine noto in alto, coefficiente di x³ in basso):

f ↔ (−1, 1, −1, 2),   g ↔ (0, 1, 1, 0),   h ↔ (−2, 1, 0, 1).

Una combinazione a·f + b·g + c·h è il polinomio nullo esattamente quando la stessa combinazione delle tre colonne è il vettore nullo, perché due polinomi sono uguali quando hanno gli stessi coefficienti. Il problema è diventato uguale a quelli dell'esercizio 3.

**Riduzione.** Con R_{2} → R_{2} + R_{1}, R_{3} → R_{3} − R_{1} e R_{4} → R_{4} + 2R_{1}; poi R_{3} → R_{3} − R_{2}; infine R_{4} → R_{4} + R_{3}:

```
( −1  0  −2 )      ( −1  0  −2 )      ( −1  0  −2 )      ( −1  0  −2 )
(  1  1   1 )  →   (  0  1  −1 )  →   (  0  1  −1 )  →   (  0  1  −1 )
( −1  1   0 )      (  0  1   2 )      (  0  0   3 )      (  0  0   3 )
(  2  0   1 )      (  0  0  −3 )      (  0  0  −3 )      (  0  0   0 )
```

I pivot sono tre (−1, 1 e 3), uno in ogni colonna: **f, g, h sono linearmente indipendenti**.

**Non sono una base.** ℝ_{3}[x] ha dimensione 3 + 1 = 4 (cap. 26) e tutte le basi di uno spazio hanno lo stesso numero di elementi: una base di ℝ_{3}[x] ha quattro polinomi, e qui ce ne sono solo tre. Lo dice anche la riduzione: l'ultima riga è nulla, quindi non c'è un pivot in ogni riga e i tre polinomi non generano. **{f, g, h} non è una base di ℝ_{3}[x]**: genera un sottospazio di dimensione 3.

Controllo senza matrici: da a·f + b·g + c·h = 0 il coefficiente di x³ dà 2a + c = 0 e il termine noto dà −a − 2c = 0. Dalla prima c = −2a; sostituendo nella seconda, −a + 4a = 3a = 0, quindi a = 0 e c = 0. Il coefficiente di x² dà −a + b = 0, quindi b = 0.

## Esercizio 5: verificare una base di ℝ³
**Testo.** Dati v_{1} = (1, 0, 4), v_{2} = (3, 0, 1) e v_{3} = (0, 1, 2), verificare che B = {v_{1}, v_{2}, v_{3}} è una base di ℝ³.

**Svolgimento.** I vettori sono tre e ℝ³ ha dimensione 3: per la proposizione del cap. 26 basta controllare **una** delle due proprietà, e l'altra segue. Si controlla l'indipendenza. Con R_{3} → R_{3} − 4R_{1}, poi scambiando la seconda e la terza riga:

```
( 1  3  0 )      ( 1    3  0 )      ( 1    3  0 )
( 0  0  1 )  →   ( 0    0  1 )  →   ( 0  −11  2 )
( 4  1  2 )      ( 0  −11  2 )      ( 0    0  1 )
```

Lo scambio serve perché dopo il primo passo, nella seconda colonna, la seconda riga ha uno 0 e non può fare da pivot. I pivot sono tre (1, −11 e 1), uno in ogni colonna: i vettori sono indipendenti. Tre vettori indipendenti in uno spazio di dimensione 3 sono una base: **B è una base di ℝ³**.

Controllo con il determinante, sviluppato lungo la seconda riga, che ha due zeri (cap. 33). L'unico elemento non nullo è l'1 in posizione (2, 3), con segno (−1)^{2+3} = −1:

det = −1·det( 1 3 ; 4 1 ) = −(1·1 − 3·4) = −(−11) = 11 ≠ 0.

Il determinante è diverso da zero, quindi la matrice ha rango 3 (cap. 42), come trovato.

## Esercizio 6: coordinate in una base di ℝ³
**Testo.** I vettori v_{1} = (1, 0, 1), v_{2} = (0, 1, 2), v_{3} = (2, 1, 0) formano una base di ℝ³. Calcolare il vettore delle coordinate di v = (0, 9, −2) rispetto a questa base.

**Svolgimento.** Le coordinate sono i numeri λ_{1}, λ_{2}, λ_{3} con λ_{1}v_{1} + λ_{2}v_{2} + λ_{3}v_{3} = v (cap. 25). Componente per componente, questo è il sistema

```
λ₁        + 2λ₃ =  0
      λ₂  +  λ₃ =  9
λ₁ + 2λ₂        = −2
```

La matrice completa ha i vettori della base come colonne e v come colonna dei termini noti (cap. 44). Con R_{3} → R_{3} − R_{1}, poi R_{3} → R_{3} − 2R_{2}:

```
( 1  0  2 |  0 )      ( 1  0   2 |  0 )      ( 1  0   2 |   0 )
( 0  1  1 |  9 )  →   ( 0  1   1 |  9 )  →   ( 0  1   1 |   9 )
( 1  2  0 | −2 )      ( 0  2  −2 | −2 )      ( 0  0  −4 | −20 )
```

Si risale dal basso. La terza riga dice −4λ_{3} = −20, cioè λ_{3} = 5. La seconda dice λ_{2} + λ_{3} = 9, cioè λ_{2} = 4. La prima dice λ_{1} + 2λ_{3} = 0, cioè λ_{1} = −10.

**Il vettore delle coordinate di v è (−10, 4, 5)**, cioè v = −10v_{1} + 4v_{2} + 5v_{3}.

Controllo: −10(1, 0, 1) + 4(0, 1, 2) + 5(2, 1, 0) = (−10 + 10, 4 + 5, −10 + 8) = (0, 9, −2).

I tre pivot nella parte dei coefficienti confermano anche che v_{1}, v_{2}, v_{3} sono davvero una base, e per questo la soluzione è unica.

## Esercizio 7: coordinate in una base di polinomi
**Testo.** I polinomi p_{1}(x) = x − 1, p_{2}(x) = x + 1, p_{3}(x) = x² + x formano una base di ℝ_{2}[x]. Calcolare il vettore delle coordinate di p(x) = 3x² + 5x − 1 rispetto a questa base.

**Svolgimento.** Si cercano a, b, c con a·p_{1} + b·p_{2} + c·p_{3} = p. Il metodo è lo stesso dell'esercizio 6; cambia solo il modo di ottenere il sistema, che per i polinomi si ricava confrontando i coefficienti. Si sviluppa il primo membro e si raccoglie per potenze di x:

a(x − 1) + b(x + 1) + c(x² + x) = c·x² + (a + b + c)·x + (−a + b).

Due polinomi sono uguali quando hanno gli stessi coefficienti, quindi il confronto con 3x² + 5x − 1 dà

```
          c =  3     (coefficiente di x²)
a + b + c   =  5     (coefficiente di x)
−a + b      = −1     (termine noto)
```

La prima equazione dà subito c = 3. La seconda diventa a + b = 2. Sommandola alla terza si elimina a: 2b = 1, cioè b = 1/2. Infine a = 2 − b = 3/2.

**Il vettore delle coordinate di p è (3/2, 1/2, 3)**, cioè p = (3/2)p_{1} + (1/2)p_{2} + 3p_{3}.

Controllo: (3/2)(x − 1) + (1/2)(x + 1) + 3(x² + x) = 3x² + (3/2 + 1/2 + 3)x + (−3/2 + 1/2) = 3x² + 5x − 1.

Attenzione all'ordine: le coordinate seguono l'ordine dei vettori della base, p_{1}, p_{2}, p_{3}, non quello delle potenze di x. Rispetto alla base canonica 1, x, x² lo stesso polinomio avrebbe coordinate (−1, 5, 3): il polinomio è lo stesso, la base è diversa e quindi le coordinate cambiano (cap. 52).

Il capitolo successivo conclude il foglio con gli esercizi 8-10, sul rango e sui sistemi lineari con un parametro.
