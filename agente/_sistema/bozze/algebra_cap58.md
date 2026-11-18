# 58. Esercizi Svolti: Matrici, Indipendenza Lineare, Determinante e Inversa
## La seconda parte del primo foglio
Questo capitolo completa gli esercizi del primo foglio del tutorato (1 novembre 2026) con gli esercizi 4-10; i primi tre, sui numeri complessi, sono nel cap. 57. Anche qui il foglio dà solo i testi: le soluzioni **non sono ufficiali**.

Gli esercizi toccano quasi tutto quello che il corso dice sulle matrici, e gli strumenti sono questi:
- il **prodotto riga per colonna** (cap. 29) e la **traccia**, cioè la somma degli elementi della diagonale principale, con la proprietà tr(AB) = tr(BA) (cap. 30);
- il **determinante**: per le matrici triangolari è il prodotto degli elementi sulla diagonale (cap. 32), e per un prodotto vale il teorema di Binet, det(AB) = det A · det B (cap. 36);
- l'**indipendenza lineare** e i **generatori**: si scrivono i vettori in colonna, si riduce a scalini con le mosse di Gauss (cap. 39) e si contano i pivot; un pivot in ogni colonna vuol dire indipendenti, un pivot in ogni riga vuol dire generatori (cap. 44);
- l'**inversa**: esiste quando det A ≠ 0 e si calcola con i cofattori, A^{-1} = (1 / det A) · ᵗcof(A) (cap. 36 e 37).

## Esercizio 4: traccia e determinante di un prodotto 5 × 5
**Testo.** Calcolare la traccia e il determinante di AB, dove

```
    ( 1  2   3   0  1 )        (  1   0   0  0  0 )
    ( 0  1  −2  −1  0 )        (  1   1   0  0  0 )
A = ( 0  0   2   2  1 )    B = ( −1   2   1  0  0 )
    ( 0  0   0   1  1 )        (  1  −1  −1  3  0 )
    ( 0  0   0   0  1 )        (  1   0   1  1  3 )
```

Prima di fare conti conviene guardare le matrici, come raccomanda il cap. 34. A ha solo zeri sotto la diagonale: è **triangolare superiore**. B ha solo zeri sopra la diagonale: è **triangolare inferiore** (cap. 21). Il prodotto AB ha 25 entrate, ma l'esercizio non le chiede tutte.

**Il determinante.** Per il teorema di Binet non serve calcolare AB: basta moltiplicare i due determinanti. E il determinante di una matrice triangolare è il prodotto degli elementi sulla diagonale (cap. 32):

det A = 1·1·2·1·1 = 2,   det B = 1·1·1·3·3 = 9.

Quindi **det(AB) = det A · det B = 2·9 = 18**.

**La traccia.** Per la traccia servono solo i cinque elementi diagonali di AB. L'elemento di posto (i, i) è la riga i di A per la colonna i di B (cap. 29). Anche qui gli zeri aiutano: la riga i di A comincia con i − 1 zeri e la colonna i di B pure, quindi i prodotti da fare sono pochi.
- Posto (1, 1): riga (1, 2, 3, 0, 1) per colonna (1, 1, −1, 1, 1): 1·1 + 2·1 + 3·(−1) + 0·1 + 1·1 = 1 + 2 − 3 + 0 + 1 = 1.
- Posto (2, 2): riga (0, 1, −2, −1, 0) per colonna (0, 1, 2, −1, 0): 1·1 + (−2)·2 + (−1)·(−1) = 1 − 4 + 1 = −2.
- Posto (3, 3): riga (0, 0, 2, 2, 1) per colonna (0, 0, 1, −1, 1): 2·1 + 2·(−1) + 1·1 = 2 − 2 + 1 = 1.
- Posto (4, 4): riga (0, 0, 0, 1, 1) per colonna (0, 0, 0, 3, 1): 1·3 + 1·1 = 4.
- Posto (5, 5): riga (0, 0, 0, 0, 1) per colonna (0, 0, 0, 0, 3): 1·3 = 3.

Quindi **tr(AB) = 1 − 2 + 1 + 4 + 3 = 7**.

**Due errori da evitare.** La traccia non si comporta come il determinante: non esiste una regola «traccia del prodotto uguale prodotto delle tracce». Qui tr A = 1 + 1 + 2 + 1 + 1 = 6 e tr B = 1 + 1 + 1 + 3 + 3 = 9, e 6·9 = 54 non c'entra niente con 7. Non vale nemmeno moltiplicare fra loro gli elementi diagonali corrispondenti e sommare: verrebbe 1·1 + 1·1 + 2·1 + 1·3 + 1·3 = 10. Gli elementi diagonali di AB dipendono anche dagli elementi fuori diagonale di A e di B, come si vede dai conti sopra.

Controllo: la matrice completa, calcolata entrata per entrata, è

```
     ( 1   8   4   1  3 )
     ( 2  −2  −1  −3  0 )
AB = ( 1   2   1   7  3 )
     ( 2  −1   0   4  3 )
     ( 1   0   1   1  3 )
```

La diagonale è 1, −2, 1, 4, 3, come trovato. Si vede anche che AB non è triangolare: per il determinante la strada di Binet era davvero la più corta.

## Esercizio 5: matrici 2 × 2 indipendenti o dipendenti
**Testo.** In M(2, ℝ) si considerano le sei matrici

```
A = ( 0  −1 )    B = ( −1  0 )    C = ( 1  −1 )
    ( 1   0 )        (  1  0 )        ( 0   0 )

D = ( 0  1 )     E = (  1  0 )    F = ( 0  0 )
    ( 0  1 )         ( −1  0 )        ( 1  1 )
```

Stabilire se l'insieme {B, C, D} è linearmente indipendente, e lo stesso per {A, C, E, F}.

**Dalle matrici ai vettori.** Una matrice 2 × 2 è determinata dalle sue quattro entrate, che sono le sue coordinate rispetto alla base canonica E_{11}, E_{12}, E_{21}, E_{22} di M(2, ℝ) (cap. 26). Si scrive quindi ogni matrice come una colonna di quattro numeri, leggendo le entrate riga per riga:

A ↔ (0, −1, 1, 0),   B ↔ (−1, 0, 1, 0),   C ↔ (1, −1, 0, 0),   D ↔ (0, 1, 0, 1),   E ↔ (1, 0, −1, 0),   F ↔ (0, 0, 1, 1).

Una combinazione lineare di matrici è la matrice nulla esattamente quando la stessa combinazione delle colonne è il vettore nullo, perché somma e prodotto per scalare si fanno entrata per entrata (cap. 19). È lo stesso passaggio fatto per i polinomi nell'esercizio 4 del cap. 55.

**L'insieme {B, C, D}.** Si mettono le tre colonne in una matrice 4 × 3 e si riduce. Con R_{3} → R_{3} + R_{1}; poi R_{3} → R_{3} + R_{2}; infine R_{4} → R_{4} − R_{3}:

```
( −1   1  0 )      ( −1   1  0 )      ( −1   1  0 )      ( −1   1  0 )
(  0  −1  1 )  →   (  0  −1  1 )  →   (  0  −1  1 )  →   (  0  −1  1 )
(  1   0  0 )      (  0   1  0 )      (  0   0  1 )      (  0   0  1 )
(  0   0  1 )      (  0   0  1 )      (  0   0  1 )      (  0   0  0 )
```

I pivot sono tre (−1, −1 e 1), uno in ogni colonna: **{B, C, D} è linearmente indipendente**.

Controllo senza Gauss: se bB + cC + dD è la matrice nulla, l'entrata (2, 1) dà b = 0, perché solo B ha un numero diverso da zero in quel posto; l'entrata (2, 2) dà d = 0, perché lì solo D non è nulla; l'entrata (1, 1) dà −b + c = 0, quindi c = 0.

**L'insieme {A, C, E, F}.** Le colonne sono quattro e la matrice è 4 × 4. Il primo elemento della prima riga è 0, quindi si comincia scambiando la prima e la seconda riga. Poi R_{3} → R_{3} + R_{1}; poi R_{3} → R_{3} + R_{2}; infine R_{4} → R_{4} − R_{3}:

```
(  0   1   1  0 )      ( −1  −1   0  0 )      ( −1  −1   0  0 )
( −1  −1   0  0 )  →   (  0   1   1  0 )  →   (  0   1   1  0 )
(  1   0  −1  1 )      (  1   0  −1  1 )      (  0  −1  −1  1 )
(  0   0   0  1 )      (  0   0   0  1 )      (  0   0   0  1 )
```

```
       ( −1  −1  0  0 )      ( −1  −1  0  0 )
  →    (  0   1  1  0 )  →   (  0   1  1  0 )
       (  0   0  0  1 )      (  0   0  0  1 )
       (  0   0  0  1 )      (  0   0  0  0 )
```

I pivot sono solo tre, nella prima, seconda e quarta colonna. La terza colonna non ha pivot: **{A, C, E, F} è linearmente dipendente**.

La relazione di dipendenza si legge dalla matrice ridotta, risolvendo il sistema omogeneo nelle incognite λ_{1}, λ_{2}, λ_{3}, λ_{4} (i coefficienti di A, C, E, F). La terza riga dà λ_{4} = 0; la seconda λ_{2} + λ_{3} = 0; la prima −λ_{1} − λ_{2} = 0. Con λ_{3} = 1 si ha λ_{2} = −1 e λ_{1} = 1, cioè

A − C + E = 0, ovvero A = C − E.

Controllo: C − E ha entrate (1 − 1, −1 − 0, 0 − (−1), 0 − 0) = (0, −1, 1, 0), che sono proprio le entrate di A. La matrice F non entra nella relazione: è l'unica delle quattro con l'entrata (2, 2) diversa da zero, quindi il suo coefficiente è obbligato a essere 0. Sono A, C, E a essere dipendenti fra loro, e aggiungere F non può rimediare (cap. 44).

## Esercizio 6: la tabella dei quattro insiemi di polinomi
**Testo.** In ℝ_{2}[x] sono dati i polinomi p_{1}(x) = x² − 1, p_{2}(x) = x − 1, p_{3}(x) = x² − x e p_{4}(x) = x + 1. Per ciascuno degli insiemi {p_{1}, p_{2}, p_{3}}, {p_{1}, p_{2}, p_{3}, p_{4}}, {p_{1}, p_{2}} e {p_{1}, p_{2}, p_{4}} dire se è linearmente indipendente, se è un insieme di generatori di ℝ_{2}[x] e se è una base.

**Una sola riduzione per tutti.** Lo spazio ℝ_{2}[x] ha dimensione 3, con base canonica 1, x, x² (cap. 26). Si scrive ogni polinomio come colonna dei suoi coefficienti, con il termine noto in alto e il coefficiente di x² in basso:

p_{1} ↔ (−1, 0, 1),   p_{2} ↔ (−1, 1, 0),   p_{3} ↔ (0, −1, 1),   p_{4} ↔ (1, 1, 0).

Si mettono tutte e quattro le colonne in una matrice e si riduce. Con R_{3} → R_{3} + R_{1}, poi R_{3} → R_{3} + R_{2}:

```
( −1  −1   0  1 )      ( −1  −1   0  1 )      ( −1  −1   0  1 )
(  0   1  −1  1 )  →   (  0   1  −1  1 )  →   (  0   1  −1  1 )
(  1   0   1  0 )      (  0  −1   1  1 )      (  0   0   0  2 )
```

Le mosse di Gauss lavorano sulle righe, quindi ogni colonna viene trasformata per conto suo. Per studiare un insieme più piccolo basta allora guardare, nella matrice ridotta, solo le colonne dei suoi polinomi: è la riduzione che si sarebbe ottenuta partendo da quelle sole colonne.

**{p_{1}, p_{2}, p_{3}}.** Le prime tre colonne ridotte sono (−1, 0, 0), (−1, 1, 0) e (0, −1, 0): due pivot e una riga nulla. La terza colonna non ha pivot, quindi **non sono indipendenti**; c'è una riga senza pivot, quindi **non generano**; **non sono una base**. La relazione è p_{3} = p_{1} − p_{2}: infatti (x² − 1) − (x − 1) = x² − x.

C'è anche un modo di vederlo senza conti: tutti e tre i polinomi si annullano in x = 1, quindi stanno nel sottospazio dei polinomi con p(1) = 0, che ha dimensione 2 (cap. 55, esercizio 2). Tre vettori in uno spazio di dimensione 2 sono per forza dipendenti, e non possono generare tutto ℝ_{2}[x] perché ogni loro combinazione si annulla ancora in 1.

**{p_{1}, p_{2}, p_{3}, p_{4}}.** Nella matrice ridotta completa i pivot sono tre (−1, 1 e 2), nella prima, seconda e quarta colonna. Ogni riga ha un pivot, quindi **generano** ℝ_{2}[x]. La terza colonna non ha pivot, quindi **non sono indipendenti**: del resto quattro vettori in uno spazio di dimensione 3 non lo sono mai. **Non sono una base.**

**{p_{1}, p_{2}}.** Le prime due colonne ridotte sono (−1, 0, 0) e (−1, 1, 0): due pivot, uno per colonna, quindi **sono indipendenti** (hanno grado diverso, e nessuno dei due è multiplo dell'altro). La terza riga è nulla, quindi **non generano**: due vettori non bastano per uno spazio di dimensione 3. **Non sono una base** di ℝ_{2}[x]; lo sono del sottospazio dei polinomi che si annullano in 1.

**{p_{1}, p_{2}, p_{4}}.** Le colonne prima, seconda e quarta della matrice ridotta sono (−1, 0, 0), (−1, 1, 0) e (1, 1, 2): tre pivot, uno in ogni colonna e uno in ogni riga. **Sono indipendenti, generano e sono una base** di ℝ_{2}[x].

Controllo: se generano, devono produrre i tre polinomi della base canonica. Infatti p_{4} − p_{2} = 2, quindi 1 = (p_{4} − p_{2})/2; p_{4} + p_{2} = 2x, quindi x = (p_{4} + p_{2})/2; infine x² = p_{1} + 1 = p_{1} + (p_{4} − p_{2})/2.

**La tabella compilata.**

```
Insieme               Linearmente indipendente   Generatore   Base
{p₁, p₂, p₃}                     no                  no        no
{p₁, p₂, p₃, p₄}                 no                  sì        no
{p₁, p₂}                         sì                  no        no
{p₁, p₂, p₄}                     sì                  sì        sì
```

Le quattro righe mostrano i quattro casi possibili. In uno spazio di dimensione 3 un insieme con meno di tre vettori non può generare e uno con più di tre non può essere indipendente (cap. 26 e 28: il numero di vettori indipendenti, e quello che serve per generare, si confrontano con la dimensione); con esattamente tre vettori le due proprietà valgono insieme oppure mancano insieme, come nella prima e nell'ultima riga.

## Esercizio 7: due tracce e un determinante con numeri complessi
**Testo.** Date le matrici

```
    ( 1 + i    −1   )        ( −1   i  )        ( 1  2 )
A = (  −4     1 + i )    B = (  1   3i )    C = ( 3  4 )
```

calcolare tr(AB), tr(BA) e det(AC).

Le regole sono le stesse delle matrici reali; in più bisogna solo ricordare che i^{2} = −1 (cap. 3).

**tr(AB).** Servono i due elementi diagonali di AB:
- posto (1, 1): riga (1 + i, −1) per colonna (−1, 1): (1 + i)·(−1) + (−1)·1 = −1 − i − 1 = −2 − i;
- posto (2, 2): riga (−4, 1 + i) per colonna (i, 3i): (−4)·i + (1 + i)·3i = −4i + 3i + 3i^{2} = −3 − i.

Quindi **tr(AB) = (−2 − i) + (−3 − i) = −5 − 2i**.

**tr(BA).** Per la proposizione del cap. 30 il risultato è già noto: tr(BA) = tr(AB) = −5 − 2i. Vale comunque la pena rifare il conto, perché è un controllo vero: gli elementi diagonali di BA sono diversi da quelli di AB.
- posto (1, 1): riga (−1, i) per colonna (1 + i, −4): (−1)·(1 + i) + i·(−4) = −1 − i − 4i = −1 − 5i;
- posto (2, 2): riga (1, 3i) per colonna (−1, 1 + i): 1·(−1) + 3i·(1 + i) = −1 + 3i + 3i^{2} = −4 + 3i.

Quindi **tr(BA) = (−1 − 5i) + (−4 + 3i) = −5 − 2i**, uguale a tr(AB) come previsto.

Per completezza, le due matrici intere sono

```
AB = ( −2 − i   −1 − 2i )        BA = ( −1 − 5i      i     )
     (  5 + i   −3 − i  )             (  1 − 11i   −4 + 3i )
```

Sono matrici diverse (il prodotto non è commutativo, cap. 30), ma con la stessa traccia.

**det(AC).** Con il teorema di Binet bastano due determinanti 2 × 2 (cap. 31):

det A = (1 + i)·(1 + i) − (−1)·(−4) = (1 + 2i + i^{2}) − 4 = 2i − 4 = −4 + 2i,

det C = 1·4 − 2·3 = −2.

Quindi **det(AC) = det A · det C = (−4 + 2i)·(−2) = 8 − 4i**.

Controllo con il prodotto esplicito: AC = ( −2 + i  −2 + 2i ; −1 + 3i  −4 + 4i ), dove per esempio l'entrata (1, 1) è (1 + i)·1 + (−1)·3 = −2 + i. Il suo determinante è

(−2 + i)(−4 + 4i) − (−2 + 2i)(−1 + 3i) = (4 − 12i) − (−4 − 8i) = 8 − 4i.

## Esercizio 8: due matrici che si comportano come 1 e i
**Testo.** In M(2, ℝ) siano I = ( 1 0 ; 0 1 ) la matrice identità e J = ( 0 1 ; −1 0 ). Verificare che I·I = I, I·J = J e J·J = −I, e poi che per ogni a, b, c, d ∈ ℝ vale

(aI + bJ)·(cI + dJ) = (ac − bd)I + (ad + bc)J,

cioè la stessa regola del prodotto di due numeri complessi a + bi e c + di.

**Le tre uguaglianze.** Le prime due non richiedono conti: la matrice identità è l'elemento neutro del prodotto (cap. 36), quindi I·I = I e I·J = J. Per lo stesso motivo vale anche J·I = J, che servirà fra poco. La terza si calcola riga per colonna:

```
J·J = (  0  1 ) · (  0  1 ) = (   0·0 + 1·(−1)      0·1 + 1·0  ) = ( −1   0 ) = −I
      ( −1  0 )   ( −1  0 )   ( (−1)·0 + 0·(−1)   (−1)·1 + 0·0 )   (  0  −1 )
```

**La regola del prodotto.** Si sviluppa il prodotto con la proprietà distributiva e si portano fuori gli scalari (proprietà 2 e 3 del cap. 30). Bisogna solo non cambiare l'ordine dei fattori matrice, perché il prodotto fra matrici in generale non è commutativo:

(aI + bJ)·(cI + dJ) = ac·(I·I) + ad·(I·J) + bc·(J·I) + bd·(J·J).

Ora si sostituiscono le uguaglianze appena verificate, I·I = I, I·J = J·I = J e J·J = −I:

(aI + bJ)·(cI + dJ) = ac·I + ad·J + bc·J − bd·I = **(ac − bd)I + (ad + bc)J**.

Controllo con le matrici scritte per esteso: aI + bJ è la matrice ( a b ; −b a ), e

```
(  a  b ) · (  c  d ) = (   ac − bd      ad + bc )
( −b  a )   ( −d  c )   ( −(ad + bc)     ac − bd )
```

che è proprio la matrice (ac − bd)I + (ad + bc)J: sulla diagonale c'è ac − bd, fuori diagonale ad + bc con i due segni opposti.

**Il collegamento con ℂ.** Nel cap. 3 il prodotto di due numeri complessi è (a + bi)(c + di) = (ac − bd) + (ad + bc)i, e si ottiene usando una sola regola speciale, i^{2} = −1. Qui è successa la stessa cosa: l'unica regola speciale usata è J·J = −I. La matrice I fa la parte del numero 1 e la matrice J fa la parte di i: la corrispondenza

a + bi ↔ aI + bJ = ( a b ; −b a )

trasforma somme in somme e prodotti in prodotti. Le matrici della forma aI + bJ sono quindi una copia di ℂ costruita con soli numeri reali, dentro M(2, ℝ).

Due conseguenze si possono controllare subito. La prima: fra queste matrici il prodotto è commutativo, perché la formula trovata non cambia scambiando (a, b) con (c, d); è un'eccezione rispetto alle matrici in generale. La seconda: det(aI + bJ) = a·a − b·(−b) = a² + b², che è il quadrato del modulo di a + bi (cap. 5). Il determinante è diverso da zero esattamente quando a + bi ≠ 0, cioè una matrice aI + bJ non nulla è sempre invertibile (cap. 36), così come in ℂ ogni numero non nullo ha un inverso (cap. 4).

Con i cap. 21 e 22: le matrici aI + bJ formano il sottospazio Span(I, J) di M(2, ℝ), che ha dimensione 2 perché I e J non sono una multipla dell'altra, e J è una matrice antisimmetrica. Anche ℂ è uno spazio vettoriale su ℝ (cap. 18), e ha a sua volta dimensione 2: ogni numero complesso si scrive in un solo modo come a·1 + b·i, quindi 1 e i sono una base.

## Esercizio 9: una base delle matrici antisimmetriche 3 × 3
**Testo.** Trovare una base dello spazio A(3) delle matrici antisimmetriche 3 × 3 e calcolarne la dimensione.

L'esercizio coincide con la seconda parte dell'esercizio 1 del cap. 55, dove è svolto per intero; qui si riporta solo la traccia del ragionamento. Una matrice è antisimmetrica se a_{ij} = −a_{ji} per ogni i, j (cap. 21). Con i = j si ottiene a_{ii} = −a_{ii}, quindi la diagonale è nulla; fuori dalla diagonale, ogni entrata sotto è l'opposto di quella simmetrica sopra. Restano libere le tre entrate sopra la diagonale:

```
    (  0   a   b )
A = ( −a   0   c )
    ( −b  −c   0 )
```

Separando i tre parametri, A = a·N_{1} + b·N_{2} + c·N_{3}, con

```
     (  0  1  0 )        (  0  0  1 )        ( 0   0  0 )
N₁ = ( −1  0  0 )   N₂ = (  0  0  0 )   N₃ = ( 0   0  1 )
     (  0  0  0 )        ( −1  0  0 )        ( 0  −1  0 )
```

Le tre matrici generano A(3), perché ogni matrice antisimmetrica si scrive così, e sono indipendenti, perché a·N_{1} + b·N_{2} + c·N_{3} è la matrice nulla solo con a = b = c = 0. Quindi **{N_{1}, N_{2}, N_{3}} è una base di A(3) e dim A(3) = 3**.

## Esercizio 10: per quali k la matrice è invertibile, e la sua inversa
**Testo.** Stabilire per quali valori di k la matrice

```
    ( 1  1  0 )
A = ( 0  2  2 )
    ( k  0  3 )
```

è invertibile. Per questi valori calcolare A^{-1} e verificare che A·A^{-1} = I_{3}.

Si seguono i tre passi del cap. 37: determinante, cofattori, trasposta divisa per il determinante.

**Primo passo: il determinante.** Si sviluppa lungo la prima riga, che ha uno zero (segni + − +, cap. 33):

det A = 1·det( 2 2 ; 0 3 ) − 1·det( 0 2 ; k 3 ) + 0 = 1·(6 − 0) − 1·(0 − 2k) = 6 + 2k.

La matrice è invertibile se e solo se det A ≠ 0 (cap. 36). Poiché 6 + 2k = 2(k + 3) si annulla solo per k = −3, **A è invertibile per ogni k ≠ −3**.

Per k = −3 la matrice non è invertibile, e si vede anche il perché: la terza riga (−3, 0, 3) è −3 volte la prima più 3/2 volte la seconda, infatti −3·(1, 1, 0) + (3/2)·(0, 2, 2) = (−3, −3 + 3, 3). Le righe sono dipendenti e il determinante è nullo (cap. 35).

**Secondo passo: i cofattori.** Da qui in poi k ≠ −3. Ogni cofattore è cof_{ij} = (−1)^{i+j} · det(C_{ij}), dove C_{ij} si ottiene cancellando la riga i e la colonna j. Il parametro k si tratta come un numero qualsiasi.
- cof_{11} = + det( 2 2 ; 0 3 ) = 6;
- cof_{12} = − det( 0 2 ; k 3 ) = −(0 − 2k) = 2k;
- cof_{13} = + det( 0 2 ; k 0 ) = 0 − 2k = −2k;
- cof_{21} = − det( 1 0 ; 0 3 ) = −3;
- cof_{22} = + det( 1 0 ; k 3 ) = 3;
- cof_{23} = − det( 1 1 ; k 0 ) = −(0 − k) = k;
- cof_{31} = + det( 1 0 ; 2 2 ) = 2;
- cof_{32} = − det( 1 0 ; 0 2 ) = −2;
- cof_{33} = + det( 1 1 ; 0 2 ) = 2.

Un primo controllo: con i cofattori della prima riga lo sviluppo di Laplace è det A = 1·cof_{11} + 1·cof_{12} + 0·cof_{13} = 6 + 2k, come trovato.

**Terzo passo: trasporre e dividere.** La matrice dei cofattori e la sua trasposta sono

```
         (  6   2k  −2k )               (   6   −3   2 )
cof(A) = ( −3    3    k )     ᵗcof(A) = (  2k    3  −2 )
         (  2   −2    2 )               ( −2k    k   2 )
```

Dividendo per il determinante si ottiene, **per k ≠ −3**,

```
           1       (   6   −3   2 )
A⁻¹ = ────────── · (  2k    3  −2 )
        2k + 6     ( −2k    k   2 )
```

L'errore più frequente a questo punto è dimenticare la trasposta: nella prima riga dell'inversa ci sono i cofattori della prima **colonna** di cof(A), cioè cof_{11}, cof_{21}, cof_{31}.

**Verifica di A·A^{-1} = I_{3}.** Conviene moltiplicare prima A per ᵗcof(A), senza frazioni, e dividere alla fine. Ogni riga di A si moltiplica per le tre colonne di ᵗcof(A), che sono (6, 2k, −2k), (−3, 3, k) e (2, −2, 2):
- riga (1, 1, 0): 6 + 2k;   −3 + 3 = 0;   2 − 2 = 0;
- riga (0, 2, 2): 4k − 4k = 0;   6 + 2k;   −4 + 4 = 0;
- riga (k, 0, 3): 6k − 6k = 0;   −3k + 3k = 0;   2k + 6.

Quindi

```
              ( 2k + 6     0        0    )
A · ᵗcof(A) = (   0      2k + 6     0    ) = (2k + 6) · I₃
              (   0        0      2k + 6 )
```

e dividendo per 2k + 6, che è diverso da zero perché k ≠ −3, si ottiene **A·A^{-1} = I_{3}**. È esattamente l'uguaglianza A · ᵗcof(A) = det A · I_{n} su cui si basa la formula dell'inversa (cap. 36): sulla diagonale compare il determinante, fuori diagonale solo zeri.

Controllo con un valore: per k = 0 la formula dà A^{-1} = (1/6)·( 6 −3 2 ; 0 3 −2 ; 0 0 2 ). La matrice A con k = 0 è triangolare superiore, e anche la sua inversa lo è; la prima riga di A per la prima colonna dell'inversa dà (1·6 + 1·0 + 0·0)/6 = 1, e per la terza colonna (1·2 + 1·(−2) + 0·2)/6 = 0.

## Che cosa ricordare
Negli esercizi di questo capitolo il risparmio di conti viene sempre dallo stesso gesto: guardare la matrice prima di calcolare.
1. Il determinante di un prodotto non richiede il prodotto: basta Binet. Se le matrici sono triangolari, i determinanti si leggono sulla diagonale.
2. Per la traccia di un prodotto servono solo gli elementi diagonali, ma vanno calcolati davvero, riga per colonna: non c'è una regola che li ricavi dalle tracce dei fattori. Vale però tr(AB) = tr(BA), utile come controllo.
3. Matrici e polinomi si studiano come vettori di numeri, scrivendo in colonna le coordinate rispetto alla base canonica; poi si contano i pivot.
4. Per l'inversa con un parametro, prima si escludono i valori che annullano il determinante, poi si calcolano i cofattori tenendo il parametro come un numero; alla fine si traspone e si verifica con il prodotto.
