# Il determinante

## Determinante {31}
= Il **determinante** è un numero associato a una matrice **quadrata**: la somma di tutti i prodotti che prendono un elemento per riga e uno per colonna, ciascuno con il segno della permutazione delle colonne.
![tre dei sei termini del determinante 3 × 3](figure/alg/det_permutazioni.png)
- det A = Σ_{σ ∈ S_{n}} sgn(σ) · a_{1σ(1)} ··· a_{nσ(n)}; le **permutazioni** di {1, …, n} sono n!, metà con segno + e metà con segno − (per n ≥ 2)
- **segno**: sgn(σ) = (−1)^{k} se σ è prodotto di k **trasposizioni** (scambi di due elementi); conta solo se k è pari o dispari
- n = 1: det(a_{11}) = a_{11}; n = 2: det A = a_{11}a_{22} − a_{12}a_{21}, diagonale principale meno l'altra diagonale
- esempio 2 × 2: det( 1 2 ; −1 4 ) = 4 − (−2) = 6; per n = 3 i termini sono sei
```
( 1  2  1 )
( 2  1  2 )
(−1  0  1 )
det = a₁₁a₂₂a₃₃ − a₁₁a₂₃a₃₂ − a₁₃a₂₂a₃₁ − a₁₂a₂₁a₃₃ + a₁₂a₂₃a₃₁ + a₁₃a₂₁a₃₂
    = 1·1·1 − 1·2·0 − 1·1·(−1) − 2·2·1 + 2·2·(−1) + 1·2·0
    = 1 − 0 + 1 − 4 − 4 + 0 = −6
```
! Trabocchetto: la definizione non si usa per calcolare: con n = 4 i termini sono già 24 e con n = 5 sono 120.
> Vedi anche: Sviluppo di Laplace, Determinante di triangolari e trasposta

## Determinante di triangolari e trasposta {32}
= Per una matrice **triangolare** (superiore o inferiore) il determinante è il prodotto degli elementi sulla diagonale principale; per ogni matrice quadrata det(ᵗA) = det A.
- motivo: l'unico termine senza zeri è quello della permutazione identità, che ha segno +
- esempio: det( 2 5 1 ; 0 3 4 ; 0 0 −1 ) = 2 · 3 · (−1) = −6
- la **matrice identità** I_{n} è diagonale, quindi det(I_{n}) = 1
- con la trasposta righe e colonne si scambiano i ruoli: ogni proprietà del determinante vera per le righe vale anche per le colonne
! Trabocchetto: davanti a una triangolare si moltiplicano gli elementi della diagonale, senza sviluppare: all'esame di settembre il determinante per gli autovalori era proprio di una triangolare.
> Vedi anche: Determinante, Scorciatoie per il polinomio caratteristico

## Sviluppo di Laplace {33}
= Si sceglie una riga (o una colonna) e si somma, per ogni suo elemento, elemento × determinante della sottomatrice **C_{ij}** ottenuta cancellando la sua riga e la sua colonna, con il segno (−1)^{i+j}.
![i segni (−1)^(i+j) formano una scacchiera con + in alto a sinistra](figure/alg/laplace_scacchiera.png)
- lungo la riga i: det A = Σ_{j} (−1)^{i+j} · a_{ij} · det C_{ij}; lungo una colonna vale lo stesso, perché det(ᵗA) = det A
- qualunque riga o colonna si scelga il risultato è lo stesso: è un buon controllo dei conti
- conviene la riga o la colonna con più zeri: i termini con a_{ij} = 0 spariscono
- esempio: in ( 1 0 1 ; 2 0 1 ; π 3 √7 ) si sviluppa lungo la seconda colonna e resta solo il 3, in riga 3 e colonna 2
```
det = −3 · det( 1 1 ) = −3 · (1 − 2) = 3
              ( 2 1 )
```
! Trabocchetto: il segno dipende dalla casella, non dal posto nella somma: il 3 in riga 3, colonna 2 ha segno − perché 3 + 2 = 5 è dispari.
> Vedi anche: Proprietà del determinante, Inversa con i cofattori

## Proprietà del determinante {34}
= Una riga (o colonna) nulla dà determinante 0; moltiplicare **una** riga (o colonna) per c moltiplica il determinante per c, quindi un fattore comune a una riga si porta fuori.
- esempio: se det A = −6 e si moltiplica la seconda riga per 3, il nuovo determinante è −18
- tutta la matrice per c: det(cA) = c^{n} · det A, perché le righe sono n; in particolare det(−A) = (−1)^{n} · det A
- metodo, dal peggiore al migliore: definizione con tutte le permutazioni; prima riga senza guardare la matrice; riga o colonna con più zeri, dopo aver portato fuori i fattori comuni
- esercizio 9.14: portando fuori 5i, 4√2 e √2 da tre colonne, det B = 40i · det D con D di soli interi, e alla fine det B = −480i
! Trabocchetto: moltiplicare tutta la matrice per c moltiplica il determinante per c^{n}, non per c: A e −A hanno lo stesso determinante se sono 2 × 2, opposto se sono 3 × 3.
> Vedi anche: Sviluppo di Laplace, Mosse di Gauss sul determinante

## Mosse di Gauss sul determinante {35}
= Tre mosse su righe o colonne: lo **scambio** cambia il segno, **moltiplicare** una riga per λ moltiplica il determinante per λ, **aggiungere** a una riga un multiplo di un'altra non lo cambia.
- sulle colonne: C_{i} ↔ C_{j}, C_{i} → λC_{i}, C_{i} → C_{i} + λC_{j} con j ≠ i
- la terza mossa è la più utile: crea zeri senza cambiare il determinante, poi si sviluppa con Laplace
- se una mossa produce una riga o una colonna nulla, det = 0: in ( 1 3 7 ; 1 3 5 ; 1 3 10 ) basta C_{2} → C_{2} − 3C_{1}
```
( 1 3  7 )   C₂ → C₂ − 3C₁   ( 1 0  0 )
( 1 5  5 )   C₃ → C₃ − 7C₁   ( 1 2 −2 )
( 1 4 10 )                   ( 1 1  3 )
det = 1 · det( 2 −2 ; 1 3 ) = 6 + 2 = 8
```
! Trabocchetto: non confondere C_{i}, la i-esima colonna, con C_{ij}, la sottomatrice dello sviluppo di Laplace.
> Vedi anche: Determinante nullo e dipendenza lineare, Mosse di Gauss sulle righe

## Determinante nullo e dipendenza lineare {35}
= Una matrice quadrata ha det A = 0 se e solo se una sua riga (o colonna) è combinazione lineare delle altre, cioè se righe (o colonne) sono linearmente dipendenti.
- perché: si parte dalla matrice con quella riga nulla, che ha det 0, e con la terza mossa si aggiungono i multipli delle altre righe senza cambiare il determinante
- il viceversa (det = 0 ⇒ righe dipendenti) fa parte dell'enunciato ma nel corso non è dimostrato
- se le righe sono davvero indipendenti il determinante è diverso da zero
```
( 1 2 3 )      ( 1 2 3 )      ( 1 2 3 )
( 4 5 6 )  →   ( 3 3 3 )  →   ( 3 3 3 )    riga nulla: det = 0
( 7 8 9 )      ( 6 6 6 )      ( 0 0 0 )
```
> Vedi anche: Mosse di Gauss sul determinante, Significato geometrico del determinante

## Significato geometrico del determinante {35}
= Il **valore assoluto** del determinante misura lo spazio occupato dalle colonne: in ℝ² l'area del parallelogramma che hanno per lati, in ℝ³ il volume del parallelepipedo.
- in ℝ²: Area(P) = |det A| con A = (A¹ | A²); in ℝ³: Vol(P) = |det A|
- colonne dipendenti, sulla stessa retta o sullo stesso piano: area o volume 0, come det = 0
- la terza mossa «inclina» il parallelogramma senza cambiarne base e altezza: det( 1 1 ; 0 2 ) = det( 1 2 ; 0 2 ) = 2
! Trabocchetto: l'area è |det A|, non det A: il determinante può essere negativo, l'area no.
> Vedi anche: Determinante nullo e dipendenza lineare

# La matrice inversa

## Matrice inversa {36}
= A ∈ M(n) è **invertibile** se esiste B ∈ M(n) con A · B = B · A = I_{n}; B è unica, si chiama **inversa** e si scrive A^{−1}.
- I_{n} è l'elemento neutro del prodotto: A · I_{n} = I_{n} · A = A
- A è invertibile se e solo se det A ≠ 0
- per le matrici quadrate basta una delle due uguaglianze: da A · B = I_{n} segue anche B · A = I_{n}
- serve per i sistemi quadrati: se det A ≠ 0, Ax = b ha l'unica soluzione x = A^{−1}b
> Vedi anche: Teorema di Binet, Inversa con i cofattori, Teorema di Rouché-Capelli

## Teorema di Binet {36, 54, 58}
= Per A, B ∈ M(n) vale det(A · B) = det A · det B: il determinante di un prodotto è il prodotto dei determinanti.
- se A è invertibile: det A · det(A^{−1}) = det(I_{n}) = 1, quindi det A ≠ 0 e det(A^{−1}) = 1 / det A
- il determinante di un prodotto non richiede di calcolare il prodotto
- esercizio del tutorato: A 5 × 5 triangolare superiore con det A = 2 e B triangolare inferiore con det B = 9 danno det(AB) = 18 leggendo solo le diagonali
- per matrici simili: det(PAP^{−1}) = det P · det A · det(P^{−1}) = det A
! Trabocchetto: la traccia non si comporta così: nell'esercizio tr A = 6 e tr B = 9, ma tr(AB) = 7, non 54; vale solo tr(AB) = tr(BA).
> Vedi anche: Matrice inversa, Matrici simili

## Inversa con i cofattori {36, 37, 58}
= Se det A ≠ 0, A^{−1} = (1 / det A) · ᵗcof(A), dove il **cofattore** di posto (i, j) è cof_{ij} = (−1)^{i+j} · det C_{ij}.
- tre passi: determinante (se è 0 non c'è inversa), matrice dei cofattori cof(A), trasposta divisa per det A
- funziona perché A · ᵗcof(A) = det A · I_{n}: sulla diagonale c'è lo sviluppo di Laplace, fuori il determinante di una matrice con due righe uguali
- con i cofattori Laplace diventa det A = Σ_{j} a_{ij} · cof_{ij}
- controllo finale: A · A^{−1} = I_{n}
```
A = ( 1 0 1 )   det A = −6   cof(A) = (  0  3 −6 )
    ( 0 2 1 )                         (  0 −3  0 )
    ( 3 0 0 )                         ( −2 −1  2 )

A⁻¹ = (1/(−6)) · ᵗcof(A) = (   0    0   1/3 )
                           ( −1/2  1/2  1/6 )
                           (   1    0  −1/3 )
```
! Trabocchetto: l'errore più frequente è dimenticare la trasposta: nella prima riga di A^{−1} vanno cof_{11}, cof_{21}, cof_{31}, cioè la prima colonna di cof(A).
> Vedi anche: Sviluppo di Laplace, Inversa di una matrice 2 × 2

## Inversa di una matrice 2 × 2 {36, 37}
= Per A = ( a b ; c d ) con ad − bc ≠ 0 si scambiano gli elementi della diagonale principale, si cambia segno agli altri due e si divide per il determinante.
```
A⁻¹ = 1/(ad − bc) · (  d  −b )
                    ( −c   a )
```
- esercizio 10.10: ( k−5 3 ; −2 k ) ha det = k² − 5k + 6 = (k − 2)(k − 3), quindi è invertibile per k ≠ 2 e k ≠ 3, con inversa (1/(k² − 5k + 6)) · ( k −3 ; 2 k−5 )
- con un parametro: prima si escludono i valori che annullano il determinante, poi si scrive l'inversa
- vale anche con i complessi: ( 2−i 0 ; 3 2+i ) ha det 5 e inversa (1/5) · ( 2+i 0 ; −3 2−i )
! Trabocchetto: b e c restano al loro posto e cambiano solo segno: si scambiano soltanto a e d.
> Vedi anche: Inversa con i cofattori

# Sistemi lineari e algoritmo di Gauss

## Sistema lineare e matrice completa {38, 41}
= Un **sistema lineare** è un insieme di k equazioni lineari in n variabili; si scrive con la **matrice dei coefficienti** A, il vettore dei **termini noti** b e la **matrice completa** C = (A | b).
- in forma compatta Ax = b, con A ∈ M(k, n), x ∈ 𝕂ⁿ e b ∈ 𝕂^{k}
- ogni riga di C è un'equazione, ogni colonna una variabile, l'ultima colonna contiene i termini noti
- una **soluzione** soddisfa tutte le equazioni insieme; S ⊂ 𝕂ⁿ è l'insieme delle soluzioni
- all'esame il primo passo è sempre scrivere la matrice completa
```
 x +  y + 2z = 9          ( 1 1  2 | 9 )
2x + 4y − 3z = 1    →     ( 2 4 −3 | 1 )     soluzione (1, 2, 3)
3x + 6y − 5z = 0          ( 3 6 −5 | 0 )
```
! Trabocchetto: una soluzione trovata non è per forza l'unica: (1, 2, 3) risolve x_{1} + x_{2} + x_{3} = 6, x_{1} + x_{2} − x_{3} = 0, ma lo fanno tutti i (3 − s, s, 3).
> Vedi anche: Mosse di Gauss sulle righe, Sistema omogeneo associato

## Mosse di Gauss sulle righe {38}
= Tre operazioni sulle righe di C = (A | b) che non cambiano l'insieme delle soluzioni: (I) scambiare due righe, (II) moltiplicare una riga per λ ≠ 0, (III) aggiungere a una riga un multiplo di un'altra.
- si scrivono R_{i} ↔ R_{j}, R_{i} → λR_{i}, R_{i} → R_{i} + λR_{j} con j ≠ i
- sono le cose che si fanno a mano con le equazioni: cambiare l'ordine, moltiplicarne una, sommarle
- ogni mossa vale per tutta la riga, termine noto compreso
- rispetto al determinante: qui si usano solo le righe, perché ogni riga è un'equazione e ogni colonna una variabile
! Trabocchetto: moltiplicando una riga per 0 l'equazione diventa 0 = 0 e si perde una condizione: per questo nella mossa (II) serve λ ≠ 0.
> Vedi anche: Algoritmo di Gauss, Mosse di Gauss sul determinante

## Matrice a scalini {39}
= Il **pivot** di una riga è il suo primo elemento non nullo; una matrice è **a scalini** se le righe nulle sono in fondo e ogni pivot sta **strettamente** più a destra di quello della riga non nulla precedente.
![una matrice a scalini con i pivot in rosso](figure/alg/matrice_scalini.png)
- è **ridotta** se in più ogni pivot vale 1 e sopra i pivot ci sono solo zeri
- a scalini: ( 1 0 5 ; 0 −1 −1 ) e ( 7 −2 9 ; 0 0 1 ; 0 0 0 ); ridotta: ( 1 0 0 4 ; 0 1 0 3 ; 0 0 1 5 )
- non a scalini: ( 1 2 −1 ; 4 0 6 ; 0 7 0 ), perché sotto il primo pivot c'è un 4
! Trabocchetto: ( 0 8 ; 0 1 ; 0 0 ; 0 0 ) non è a scalini: i due pivot stanno uno sopra l'altro, nella stessa colonna.
> Vedi anche: Algoritmo di Gauss, Algoritmo di Gauss-Jordan

## Algoritmo di Gauss {39}
= Porta qualsiasi matrice a scalini, una colonna alla volta: un elemento non nullo in cima, con la mossa (III) si azzera tutto ciò che sta sotto, poi si tolgono quella riga e quella colonna e si ripete sul resto.
- se C_{11} = 0 si scambia la prima riga con una che ha un elemento non nullo nella prima colonna; una colonna tutta nulla si salta
- per azzerare: R_{i} → R_{i} − (C_{i1}/C_{11}) R_{1}
```
( 0 1 1  0 )   R₁ ↔ R₂        ( 1 1 2 −3 )
( 1 1 2 −3 )   R₃ → R₃ + R₁   ( 0 1 1  0 )
(−1 2 1  1 )                  ( 0 3 3 −2 )

R₃ → R₃ − 3R₂             →   ( 1 1 2 −3 )
                              ( 0 1 1  0 )
                              ( 0 0 0 −2 )
```
! Trabocchetto: nell'ultimo passo si usa la riga del pivot corrente, R_{2}: con R_{3} − 3R_{1} il primo elemento diventerebbe −3 e si perderebbe lo zero appena ottenuto.
> Vedi anche: Matrice a scalini, Algoritmo di Gauss-Jordan

## Algoritmo di Gauss-Jordan {39}
= Dopo Gauss si risale: con la mossa (III) si azzera anche **sopra** i pivot, con la (II) si rendono i pivot uguali a 1. Il risultato è una matrice a scalini **ridotta**.
- Gauss scende e azzera sotto i pivot, Jordan risale e azzera sopra
- ordine del diagramma della lezione: dall'ultimo pivot verso il primo, e solo alla fine si divide ogni riga per il suo pivot; nell'esempio della lezione i due ordini danno la stessa matrice
- dalla ridotta le soluzioni si leggono subito
```
( 1 −1 3 )      ( 1 0 4 )
( 0  2 2 )  →   ( 0 1 1 )
( 1  0 4 )      ( 0 0 0 )
```
! Trabocchetto: se si toglie un'equazione la forma ridotta va ricalcolata, non ricopiata: un termine noto poteva essere stato azzerato proprio con la riga tolta.
> Vedi anche: Matrice a scalini, Parametri liberi

## Parametri liberi {40}
= Dalla matrice a scalini: se c'è un pivot nella colonna dei termini noti il sistema è impossibile; altrimenti ogni variabile **senza pivot** diventa un **parametro libero** e le altre si ricavano.
- pivot nei termini noti: una riga dice 0 = 1 (o 0 = −2) e S = ∅
- numero di parametri = colonne senza pivot, esclusa quella dei termini noti
- due strade con le stesse soluzioni: Gauss-Jordan e lettura diretta, oppure solo Gauss e risalita dal basso (di solito più veloce)
- una colonna di A tutta nulla: quella variabile non compare mai ed è libera
```
( 1 2 −1 1 | 3 )      ( 1 2 −1 1 | 3 )
( 0 1  2 5 | 2 )  →   ( 0 1  2 5 | 2 )
( 1 3  1 6 | 5 )      ( 0 0  0 0 | 0 )
z = t₁, w = t₂:  y = 2 − 2t₁ − 5t₂,  x = −1 + 5t₁ + 9t₂
```
! Trabocchetto: una riga 0 = 0 si ignora e non rende impossibile il sistema: lo rende impossibile solo una riga 0 = numero non nullo.
> Vedi anche: Algoritmo di Gauss-Jordan, Teorema di Rouché-Capelli

# Rouché-Capelli e applicazioni

## Sistema omogeneo associato {41}
= Un sistema è **omogeneo** se b = 0; il **sistema omogeneo associato** ad Ax = b è Ax = 0, con gli stessi coefficienti e solo zeri a destra.
- le soluzioni S_{0} dell'omogeneo formano un **sottospazio** di 𝕂ⁿ: contengono 0 e sono chiuse per somme e multipli
- si risolve con le stesse mosse di (A | b): l'ultima colonna resta sempre zero
- esempio: per il sistema dei parametri liberi, S_{0} = Span((5, −2, 1, 0), (9, −5, 0, 1))
- se il sistema è già omogeneo, S = S_{0}
! Trabocchetto: se b ≠ 0 l'insieme S delle soluzioni non è un sottospazio: non contiene l'origine.
> Vedi anche: Soluzione particolare e sottospazio affine, Nucleo e immagine

## Soluzione particolare e sottospazio affine {41}
= Se S ≠ ∅, tutte le soluzioni si ottengono da una qualsiasi soluzione x₀, la **soluzione particolare**, aggiungendole le soluzioni dell'omogeneo associato: S = x₀ + S₀.
![le soluzioni di x + 2y = 2 sono la retta di x + 2y = 0 spostata della soluzione particolare x₀ = (2, 0), indicata con x nella figura](figure/alg/soluzioni_affini.png)
- perché: x₀ + x′ con x′ ∈ S₀ risolve ancora Ax = b, e due soluzioni differiscono per un elemento di S₀
- un **sottospazio affine** è x₀ + W con W sottospazio: un sottospazio traslato, di dimensione dim W
- esempio: x − y + z = 1, y − z = 2 ha S_{0} = {(0, t, t)} e S = (3, 0, −2) + (0, t, t) = (3, t, t − 2)
- è comodo quando una soluzione è già data o facile da indovinare: basta calcolare S_{0}
! Trabocchetto: la soluzione particolare non è unica: se ne può prendere una qualsiasi, e S non cambia.
> Vedi anche: Sistema omogeneo associato, Teorema di Rouché-Capelli

## Rango con le mosse di Gauss {42, 56}
= Il **rango** di una matrice è il numero di pivot di una qualsiasi sua riduzione a scalini.
- motivo: le mosse sulle righe non cambiano lo spazio generato dalle righe, quindi nemmeno il rango
- esempio: ( 1 0 1 ; 1 1 0 ; 0 1 −1 ) → ( 1 0 1 ; 0 1 −1 ; 0 0 0 ): due pivot, rango 2
- per un sistema: Gauss su (A | b), poi si contano i pivot di A e quelli di (A | b)
- se in una colonna sotto le righe già sistemate ci sono solo zeri, lì non c'è pivot e si passa alla colonna dopo
! Trabocchetto: per calcolare il rango si usano le mosse sulle righe, e si contano i pivot, non le righe della matrice.
> Vedi anche: Teorema di Rouché-Capelli, Nucleo e immagine, Rango, Limiti al rango

## Teorema di Rouché-Capelli {42}
= Ax = b ha soluzioni se e solo se rk(A | b) = rk(A); in tal caso S è un sottospazio affine di dimensione n − rk(A), dove n è il numero di **incognite**.
![i tre casi del sistema con parametro: una soluzione, nessuna, infinite](figure/alg/rouche_tre_casi.png)
- equivale a b ∈ Span(A^{1}, …, A^{n}): b deve essere combinazione lineare delle colonne di A
- n − rk(A) è il numero di parametri liberi
- su un campo infinito: 0 soluzioni se rk(A | b) > rk(A), 1 se rk(A | b) = rk(A) = n, ∞ se rk(A | b) = rk(A) < n
- A quadrata: soluzione unica se e solo se rk A = n, cioè det A ≠ 0, e allora x = A^{−1}b
! Trabocchetto: un sistema lineare non ha mai esattamente due o tre soluzioni: o nessuna, o una, o infinite.
> Vedi anche: Rango con le mosse di Gauss, Teorema della dimensione, Sistemi con un parametro

## Sistemi con un parametro {43, 56}
= Il parametro k si tratta come un numero: si riduce a scalini (A | b) lasciando k dentro, si cercano i valori di k che annullano un candidato pivot e li si studia a parte.
- sommare a una riga un multiplo di un'altra, anche con coefficiente k, è sempre lecito
- esempio: x + ky = 4 − k, kx + 4y = 4; con R_{2} → R_{2} − kR_{1} il pivot è 4 − k² e il termine noto (k − 2)²
- k = −2: rk(A) = 1 e rk(A | b) = 2, nessuna soluzione; k = 2: ranghi 1 e 1, una retta (x = 2 − 2t, y = t); k ≠ ±2: una sola soluzione, per k = 1 è (8/3, 1/3)
- per ogni caso speciale si sostituisce il valore di k nella matrice ridotta e si rileggono i ranghi
```
( 1 k | 4 − k )      ( 1    k    |   4 − k  )
( k 4 |   4   )  →   ( 0  4 − k² | (k − 2)² )
```
! Trabocchetto: dividere per k o per un'espressione con k vuol dire supporla non nulla: il valore che la annulla va trattato a parte, e dimenticarlo è l'errore più frequente.
> Vedi anche: Teorema di Rouché-Capelli, Rango con le mosse di Gauss

## Indipendenza e generatori con i pivot {44, 55}
= Si mettono i vettori **in colonna** e si riduce a scalini: un pivot in **ogni colonna** vuol dire linearmente indipendenti, un pivot in **ogni riga** vuol dire generatori.
- base: tutte e due le cose; se si sa già che dim V = n e i vettori sono n, ne basta una
- la relazione di dipendenza si trova risolvendo il sistema omogeneo: per u_{1} = (1, 0, −1), u_{2} = (1, −1, 0), u_{3} = (0, 1, −1) esce −u_{1} + u_{2} + u_{3} = 0
- con una matrice quadrata si può usare il determinante: det ≠ 0 vuol dire rango massimo
- g_{1} = (3, 2), g_{2} = (1, 5), g_{3} = (−1, 7) generano ℝ²: dopo Gauss, per ogni v = (a, b) tutti i pivot stanno nei coefficienti
```
( 1  1  0 )      ( 1  1  0 )
( 0 −1  1 )  →   ( 0 −1  1 )    terza colonna senza pivot:
(−1  0 −1 )      ( 0  0  0 )    u₁, u₂, u₃ dipendenti
```
! Trabocchetto: il determinante funziona solo con matrici quadrate, il criterio dei pivot anche con quelle rettangolari, come i tre vettori di ℝ² (matrice 2 × 3).
> Vedi anche: Rango con le mosse di Gauss, Coordinate con un sistema

## Coordinate con un sistema {44}
= Le **coordinate** di v rispetto a una base v_{1}, …, v_{n} sono gli unici λ_{1}, …, λ_{n} con v = λ_{1}v_{1} + … + λ_{n}v_{n}: si trovano risolvendo il sistema che ha i vettori della base in colonna e v come termine noto.
- esempio: base c_{1} = (1, 1, 0), c_{2} = (0, 1, 1), c_{3} = (1, 0, 1) e v = (1, 2, 3)
- in alternativa le coordinate sono A^{−1}v, con A la matrice dei vettori della base in colonna
```
( 1 0 1 | 1 )      ( 1 0  1 | 1 )
( 1 1 0 | 2 )  →   ( 0 1 −1 | 1 )    λ₃ = 1, λ₂ = 2, λ₁ = 0
( 0 1 1 | 3 )      ( 0 0  2 | 2 )
```
! Trabocchetto: cambiando base cambia la «ricetta», non il vettore: (3, 4, 5) ha coordinate (3, 4, 5) nella base canonica e (7, 1, −4) nella base w_{1} = (1, 1, 0), w_{2} = (0, 1, 1), w_{3} = (1, 1, −1).
> Vedi anche: Vettore delle coordinate, Matrice del cambio di base, Coordinate in una base

## Codici correttori di errori {45}
= Al messaggio si aggiungono numeri di controllo: tutti i numeri diventano i coefficienti di un polinomio s(x), e quelli aggiunti si scelgono in modo che s(1) = s(2) = 0.
- messaggio {2, −7, 8, −2}: s(x) = 2x⁵ − 7x⁴ + 8x³ − 2x² + ax + b; il sistema a + b = −1, 2a + b = −8 dà a = −7, b = 6
- **rilevare**: chi riceve controlla s(1) = s(2) = 0; se una delle due non vale c'è un errore
- **correggere** un errore: si sostituisce a turno ogni coefficiente con un'incognita k; solo per la posizione sbagliata il sistema è compatibile
- ricevuto {2, −7, 8, 4, −7, 6}: nella quarta posizione k + 2 = 0 e 4k + 8 = 0 danno k = −2, nelle altre il sistema è incompatibile
- è l'idea dei codici di Reed-Solomon (QR code), che però lavorano su campi finiti
! Trabocchetto: mandare il messaggio due volte mostra che c'è un errore ma non dove; tre volte lo corregge a maggioranza, ma il messaggio diventa tre volte più lungo.
> Vedi anche: Parametri liberi

# Applicazioni lineari

## Applicazione lineare {46}
= f : V → W, tra spazi sullo stesso campo, è **lineare** se f(v + w) = f(v) + f(w) e f(λv) = λf(v): rispetta somma e prodotto per scalare.
- le due condizioni equivalgono a una sola: f(v_{1} + a·v_{2}) = f(v_{1}) + a·f(v_{2})
- conseguenze: f(0) = 0 e f(λ_{1}v_{1} + … + λ_{k}v_{k}) = λ_{1}f(v_{1}) + … + λ_{k}f(v_{k})
- controllo rapido: se f(0) ≠ 0 non è lineare; T(a, b) = (a + 2, a + b − 1) dà T(0, 0) = (2, −1)
- sono lineari la mappa nulla, l'identità, la traccia, la derivata sui polinomi e ogni funzione con componenti combinazioni lineari delle variabili, senza termine noto
! Trabocchetto: f(0) = 0 non basta: T(a, b) = (a², a + b) manda 0 in 0, ma T(4, 1) = (16, 5) mentre T(2, 1) + T(2, 0) = (8, 5).
> Vedi anche: Moltiplicazione per una matrice, Nucleo e immagine

## Moltiplicazione per una matrice {46}
= Ogni A ∈ M(m, n) dà l'applicazione lineare L_{A} : 𝕂ⁿ → 𝕂^{m}, L_{A}(x) = Ax: n colonne, quindi 𝕂ⁿ in partenza; m righe, quindi 𝕂^{m} in arrivo.
- è lineare per la distributività del prodotto: A(x + ax′) = Ax + aAx′
- i coefficienti di ogni componente sono le righe di A: ( 3 2 ; 1 0 ) dà L_{A}(x, y) = (3x + 2y, x)
- esempio: A = ( 1 0 2 ; 1 2 4 ) dà L_{A} : ℝ³ → ℝ², L_{A}(x, y, z) = (x + 2z, x + 2y + 4z), e L_{A}(1, 1, 1) = (3, 7)
- ogni applicazione lineare 𝕂ⁿ → 𝕂^{m} è una L_{A}: funzioni lineari e matrici sono la stessa cosa
! Trabocchetto: x ↦ Ax + b con b ≠ 0, come in uno strato di una rete neurale, non è lineare ma **affine**: sposta l'origine.
> Vedi anche: Applicazione lineare, Matrice associata

## Nucleo e immagine {47}
= Il **nucleo** Ker f = {v ∈ V | f(v) = 0} sta nello spazio di partenza; l'**immagine** Im f = {f(v) | v ∈ V} sta in quello di arrivo. Sono entrambi sottospazi.
- se v_{1}, …, v_{n} generano V, allora Im f = Span(f(v_{1}), …, f(v_{n}))
- per L_{A}: L_{A}(e_{i}) è la i-esima colonna A^{i}, quindi Im L_{A} = Span(A^{1}, …, A^{n}) e rk(A) = dim Im L_{A}
- Ker L_{A} = {x | Ax = 0} = S_{0}, le soluzioni del sistema omogeneo
- esempio: A = ( 1 1 ; 2 2 ) ha Ker L_{A} = Span((1, −1)) e Im L_{A} = Span((1, 2)), quindi rango 1
- Ax è la combinazione delle colonne con le componenti di x: con A = ( 1 2 ; 3 4 ) e x = (5, 6), 5(1, 3) + 6(2, 4) = (17, 39)
! Trabocchetto: Ker f è fatto di vettori di V, Im f di vettori di W: per L_{A} : ℝ³ → ℝ² il nucleo sta in ℝ³ e l'immagine in ℝ².
> Vedi anche: Nucleo e iniettività, Teorema della dimensione, Sistema omogeneo associato

## Nucleo e iniettività {47}
= Un'applicazione **lineare** f è iniettiva se e solo se Ker f = {0}; è suriettiva se e solo se Im f = W.
- motivo: f(v) = f(v′) equivale a f(v − v′) = 0, quindi due vettori si confondono solo se la loro differenza sta nel nucleo
- (⇒) se f è iniettiva, un v nel nucleo ha la stessa immagine di 0, quindi v = 0; (⇐) è il punto sopra
- la condizione sulla suriettività è la definizione stessa e vale per ogni funzione
- per sapere se f è iniettiva basta guardare chi finisce sullo zero
! Trabocchetto: il criterio del nucleo vale solo per le applicazioni lineari, non per funzioni qualsiasi.
> Vedi anche: Nucleo e immagine, Iniettività e suriettività con le dimensioni

## Teorema della dimensione {48}
= Se V ha dimensione finita n e f : V → W è lineare, allora dim Ker f + dim Im f = n.
- più grande è il nucleo, più piccola è l'immagine: le dimensioni di partenza si dividono tra le due
- idea: una base di Ker f si completa a una base di V; le immagini dei vettori aggiunti formano una base di Im f
- esempio: la proiezione f(x, y, z) = (x, y) ha Ker f = asse z, di dimensione 1, e Im f = ℝ²: 1 + 2 = 3
- per L_{A} : 𝕂ⁿ → 𝕂^{m} diventa dim S_{0} = n − rk(A): è Rouché-Capelli per i sistemi omogenei
- esercizio 14.15: f : ℝ⁴ → ℝ³ con rk(A) = 2 ha Ker f con base (0, −1, 1, 0), (1, −1, 0, 1) e Im f con base (1, 0, 1), (1, 1, 0)
! Trabocchetto: n è la dimensione dello spazio di partenza, non di quello di arrivo: per f : ℝ⁴ → ℝ³ la somma fa 4, non 3.
> Vedi anche: Nucleo e immagine, Teorema di Rouché-Capelli, Iniettività e suriettività con le dimensioni

## Iniettività e suriettività con le dimensioni {48, 49}
= Per f : V → W lineare, con dimensioni finite: dim Im f ≤ dim V; f è **iniettiva** se e solo se dim Im f = dim V, **suriettiva** se e solo se dim Im f = dim W.
- di conseguenza: iniettiva ⇒ dim V ≤ dim W; suriettiva ⇒ dim V ≥ dim W; biettiva ⇒ dim V = dim W
- nessuna applicazione lineare ℝ³ → ℝ² è iniettiva, nessuna ℝ² → ℝ³ è suriettiva
- bastano uguaglianze tra numeri interi, «senza toccare la funzione»
! Trabocchetto: dim V ≥ dim W non basta per la suriettività: la f : ℝ⁴ → ℝ³ dell'esercizio 14.15 ha dim Im f = 2 < 3, quindi non è suriettiva (e nemmeno iniettiva).
> Vedi anche: Teorema della dimensione, Isomorfismi

## Isomorfismi {49, 53}
= Un **isomorfismo** è un'applicazione lineare biettiva; V e W sono **isomorfi** se ne esiste uno: «lo stesso spazio con nomi diversi».
- l'inversa f^{−1} di un isomorfismo è ancora lineare
- due spazi di dimensione finita sono isomorfi se e solo se hanno la stessa dimensione; ogni spazio di dimensione n è isomorfo a 𝕂ⁿ
- ℝ_{2}[x], di dimensione 3, è isomorfo a ℝ³; M(2, 2, ℝ), di dimensione 4, è isomorfo a ℝ⁴ ma non a ℝ³
- (con dim V = dim W) f è un isomorfismo se e solo se la matrice [f]^{B}_{C} è invertibile, e ([f]^{B}_{C})^{−1} = [f^{−1}]^{C}_{B}
! Trabocchetto: nella matrice dell'inversa le basi si scambiano di posto: [f^{−1}]^{C}_{B}, con C in alto e B in basso.
> Vedi anche: Vettore delle coordinate, Matrice associata

## Vettore delle coordinate {49, 55}
= Fissata una base ordinata B = {v_{1}, …, v_{n}} di V, il **vettore delle coordinate** [v]_{B} = (a_{1}, …, a_{n}) raccoglie i coefficienti di v = a_{1}v_{1} + … + a_{n}v_{n}.
- F_{B} : 𝕂ⁿ → V, F_{B}(a_{1}, …, a_{n}) = a_{1}v_{1} + … + a_{n}v_{n}, è un isomorfismo, e v ↦ [v]_{B} è la sua inversa
- base che genera ⇒ F_{B} suriettiva; base indipendente ⇒ F_{B} iniettiva
- è lineare: [v + w]_{B} = [v]_{B} + [w]_{B} e [λv]_{B} = λ[v]_{B}
- esempio: in ℝ_{2}[x] con B = {x², x + 1, 1}, 3x² + 2x + 1 = 3x² + 2(x + 1) − 1, quindi [p]_{B} = (3, 2, −1); nella base canonica {1, x, x²} sarebbe (1, 2, 3)
! Trabocchetto: le coordinate seguono l'ordine dei vettori della base, non quello delle potenze di x: cambiando l'ordine della base cambiano le coordinate.
> Vedi anche: Coordinate con un sistema, Matrice associata

# Matrice associata e cambio di base

## Matrice associata {50}
= Fissate una base B = {v_{1}, …, v_{n}} di V e una base C di W, la **matrice associata** [f]^{B}_{C} ha come j-esima colonna le coordinate di f(v_{j}) nella base C.
- [f]^{B}_{C} = ( [f(v_{1})]_{C} | … | [f(v_{n})]_{C} ): base di partenza in alto, base di arrivo in basso
- righe = dim W, colonne = dim V
- nelle basi canoniche [L_{A}]^{E}_{E} = A: la matrice associata rovescia la costruzione A ↦ L_{A}
- cambiando base cambia la matrice: f(p) = (p(2), p(−2)) ha ( 1 2 4 ; 1 −2 4 ) con arrivo canonico e ( 1 2 4 ; 2 0 8 ) con C′ = {(1, −1), (0, 1)}
```
f(p) = (p(1), p(−1)),  B = {1, x, x²},  C = {e₁, e₂}
f(1) = (1, 1)    f(x) = (1, −1)    f(x²) = (1, 1)
matrice associata:  ( 1  1  1 )
                    ( 1 −1  1 )
```
! Trabocchetto: le immagini si mettono in **colonna**, non in riga, e scritte nella base di arrivo: con una base di arrivo non canonica serve un piccolo sistema per ogni colonna.
> Vedi anche: Calcolare con la matrice associata, Matrice del cambio di base

## Calcolare con la matrice associata {51}
= Per ogni v ∈ V vale [f(v)]_{C} = [f]^{B}_{C} · [v]_{B}: le coordinate dell'immagine sono la matrice per le coordinate del vettore.
![fissate le basi l'applicazione f diventa la moltiplicazione per la matrice associata](figure/alg/teoria_calcoli.png)
- in coordinate ogni f : V → W è una L_{A} : 𝕂ⁿ → 𝕂^{m}: i vettori diventano array di numeri, le applicazioni lineari matrici
- esempio: con [f]^{B}_{C} = ( 1 1 1 ; 1 −1 1 ) e [x² + 1]_{B} = (1, 0, 1) si ottiene (2, 2) = f(x² + 1)
- **identità**: [I_{V}]^{B}_{B} = I_{n} per ogni base B, purché la base sia la stessa in partenza e in arrivo
- f : ℝ_{2}[x] → ℝ_{1}[x] con [f]^{B}_{C} = ( 1 0 2 ; 0 5 3 ) e C = {1, x}: f(a + bx + cx²) = (a + 2c) + (5b + 3c)x
! Trabocchetto: il prodotto dà le coordinate, non il vettore: se l'arrivo è fatto di polinomi, (a + 2c, 5b + 3c) va ritradotto nella base C.
> Vedi anche: Matrice associata, Lo spazio Hom

## Lo spazio Hom {51}
= Hom(V, W) è l'insieme delle applicazioni lineari da V a W; con somma e multiplo punto per punto, (f + g)(v) = f(v) + g(v) e (λf)(v) = λf(v), è uno spazio vettoriale.
- f + g e λf sono ancora lineari; il vettore nullo di Hom(V, W) è la mappa nulla
- fissate le basi, f ↦ [f]^{B}_{C} è un isomorfismo Hom(V, W) → M(m, n, 𝕂)
- quindi dim Hom(V, W) = mn, con n = dim V e m = dim W
- in sintesi: «ogni mappa lineare è una mappa di moltiplicazione a sinistra»
! Trabocchetto: in M(m, n) le righe sono m = dim W e le colonne n = dim V, non il contrario.
> Vedi anche: Calcolare con la matrice associata, Isomorfismi

## Matrice del cambio di base {52}
= La **matrice del cambio di base** da B a B′ è [I_{V}]^{B}_{B′}: la sua j-esima colonna contiene le coordinate del j-esimo vettore di B (base vecchia) nella base B′ (base nuova).
![lo stesso v = (3, 7) ha coordinate (3, 7) nella base canonica e (−1, 4) nella base w₁ = (1, 1), w₂ = (1, 2)](figure/alg/cambio_base_vettore.png)
- formula del cambio di coordinate: [v]_{B′} = [I_{V}]^{B}_{B′} · [v]_{B}
- è invertibile e ([I_{V}]^{B}_{B′})^{−1} = [I_{V}]^{B′}_{B}: il dizionario al contrario è la matrice inversa
- esempio: E canonica e B′ = {w_{1}, w_{2}} = {(1, 1), (1, 2)}: e_{1} = 2w_{1} − w_{2} ed e_{2} = −w_{1} + w_{2}
```
da E a B′:  (  2 −1 )     (  2 −1 ) · ( 3 ) = ( −1 )
            ( −1  1 )     ( −1  1 )   ( 7 )   (  4 )
```
! Trabocchetto: [I_{V}]^{B}_{B′} non è la matrice identità: lo è soltanto [I_{V}]^{B}_{B}, con la stessa base in alto e in basso.
> Vedi anche: Cambio di base verso la canonica, Cambio di base tra due basi qualsiasi

## Cambio di base verso la canonica {52}
= In 𝕂ⁿ la matrice del cambio di base da una base B alla canonica E non costa niente: ha per colonne i vettori di B, [I_{V}]^{B}_{E} = (v_{1} | … | v_{n}).
- motivo: nella base canonica le coordinate di un vettore sono le sue entrate, e questo vale solo per lei
- il verso opposto è l'inversa, [I_{V}]^{E}_{B} = ([I_{V}]^{B}_{E})^{−1}: di solito più veloce che risolvere un sistema per colonna
- esempio: B = {(1, 1), (1, 2)} dà ( 1 1 ; 1 2 ), con inversa ( 2 −1 ; −1 1 ) = [I_{V}]^{E}_{B}
- esercizio 16.3: per w_{1} = (1, 2, 3), w_{2} = (0, 2, 1), w_{3} = (0, 1, 1) si cerca [I_{V}]^{E}_{B}, che è l'inversa della matrice con i w in colonna
```
da B a E:  ( 1 0 0 )      da E a B:  (  1  0  0 )
           ( 2 2 1 )                 (  1  1 −1 )
           ( 3 1 1 )                 ( −4 −1  2 )
```
! Trabocchetto: i vettori della base in colonna danno il cambio **da** B **alla** canonica; per andare dalla canonica a B bisogna invertire.
> Vedi anche: Matrice del cambio di base, Cambio di base tra due basi qualsiasi

## Composizione e prodotto di matrici {53}
= La composizione di applicazioni lineari è lineare e diventa il prodotto delle matrici: L_{A} ∘ L_{B} = L_{AB} e [g ∘ f]^{B}_{D} = [g]^{C}_{D} · [f]^{B}_{C}.
![sopra le applicazioni e la loro composizione, sotto le matrici e il loro prodotto](figure/alg/composizione_teoria_calcoli.png)
- (g ∘ f)(v) = g(f(v)): prima f, poi g; serve che l'arrivo di f sia la partenza di g
- la base di mezzo C «si cancella»: C in alto nel primo fattore, C in basso nel secondo
- è il motivo per cui il prodotto riga per colonna è definito proprio così
- esempio: A = ( 1 2 ; 2 1 ) e B = ( 1 1 ; 1 2 ) danno AB = ( 3 5 ; 3 4 ), mentre BA = ( 3 3 ; 5 4 )
- endomorfismi, con la stessa base ovunque: [f ∘ g]^{B}_{B} = [f]^{B}_{B} · [g]^{B}_{B}
! Trabocchetto: la matrice di f, che agisce per prima, sta a **destra**: [g ∘ f] = [g] · [f], e scambiando i fattori si ottiene in generale un'altra matrice.
> Vedi anche: Cambio di base tra due basi qualsiasi, Matrice associata in basi diverse

## Cambio di base tra due basi qualsiasi {53}
= Se nessuna delle due basi di 𝕂ⁿ è la canonica, si passa per la canonica: [I_{V}]^{B}_{B′} = ([I_{V}]^{B′}_{E})^{−1} · [I_{V}]^{B}_{E}.
- ricetta: si scrivono in colonna le due basi, si inverte la matrice della base di **arrivo** e la si moltiplica, a sinistra, per quella della base di partenza
- viene da I_{V} = I_{V} ∘ I_{V}, con la base canonica nel passaggio intermedio
- controllo: le colonne sono le coordinate dei vettori di B nella base B′, e infatti 4·(0, 1) − (−1, 3) = (1, 1)
```
B = {(1, 1), (1, 2)}     B′ = {(0, 1), (−1, 3)}
( 0 −1 )⁻¹ = (  3 1 )    (  3 1 ) · ( 1 1 ) = (  4  5 )
( 1  3 )     ( −1 0 )    ( −1 0 )   ( 1 2 )   ( −1 −1 )
```
! Trabocchetto: si inverte la matrice della base di arrivo B′, non quella di partenza, e il fattore invertito sta a sinistra.
> Vedi anche: Cambio di base verso la canonica, Composizione e prodotto di matrici

## Matrice associata in basi diverse {54}
= Con P = [I_{V}]^{B}_{B′} e Q = [I_{W}]^{C}_{C′}, i cambi di base dalle basi vecchie alle nuove, vale [f]^{B′}_{C′} = Q · [f]^{B}_{C} · P^{−1}.
![f preceduta e seguita dall'identità con le basi usate a ogni passo](figure/alg/cambio_base_mappa.png)
- si dimostra scrivendo f = I_{W} ∘ f ∘ I_{V}, con le basi B′, B, C, C′ lungo il percorso, e usando due volte la formula della composizione
- P^{−1} = [I_{V}]^{B′}_{B} riporta le coordinate nuove di V a quelle vecchie, Q porta quelle vecchie di W alle nuove
- le basi si cancellano a coppie e restano B′ in alto e C′ in basso
- se dim V = n e dim W = m, P è n × n e Q è m × m
! Trabocchetto: le matrici si scrivono da destra a sinistra, nell'ordine in cui agiscono: a destra va P^{−1}, non P.
> Vedi anche: Endomorfismi e cambio di base, Composizione e prodotto di matrici

## Endomorfismi e cambio di base {54}
= Un **endomorfismo** è un'applicazione lineare f : V → V; con la stessa base in partenza e in arrivo, passando da B a B′ vale [f]^{B′}_{B′} = P · [f]^{B}_{B} · P^{−1}, con P = [I_{V}]^{B}_{B′}.
- dispense: M = [I_{V}]^{B′}_{B}, dalla base nuova alla vecchia, e [f]^{B′}_{B′} = M^{−1} · [f]^{B}_{B} · M, con M = P^{−1}
- in 𝕂ⁿ con base vecchia canonica conviene la versione delle dispense: M ha in colonna i vettori della base nuova
- esempio: A = ( 1 2 ; 2 1 ) e B = {(1, 1), (1, 2)} danno [L_{A}]^{B}_{B} = ( 3 6 ; 0 −1 )
- esempio 16.10: f(x, y) = (x + y, −y) e B = {(1, 0), (−1, 2)}; nella base B la matrice diventa diagonale
```
M = ( 1 −1 )   M⁻¹ = ( 1 1/2 )   M⁻¹ · ( 1  1 ) · M = ( 1  0 )
    ( 0  2 )         ( 0 1/2 )         ( 0 −1 )       ( 0 −1 )
```
! Trabocchetto: lavagna e dispense prendono la matrice del cambio di base in versi opposti; in entrambe la matrice più a destra porta dalle coordinate nuove alle vecchie.
> Vedi anche: Matrice associata in basi diverse, Matrici simili

## Matrici simili {54, 61}
= A, B ∈ M(n) sono **simili** (A ∼ B) se esiste P invertibile con B = P A P^{−1}: sono lo stesso endomorfismo scritto in due basi diverse.
- la similitudine è una relazione di equivalenza
- matrici simili hanno stesso determinante, stessa traccia e stesso rango, quindi sono invertibili insieme; hanno anche lo stesso polinomio caratteristico
- esempi: ( 1 2 ; 2 1 ) ∼ ( 3 6 ; 0 −1 ) (det −3, traccia 2, rango 2) e ( 1 1 ; 0 −1 ) ∼ ( 1 0 ; 0 −1 )
- controllo rapido di un cambio di base: se traccia o determinante non tornano c'è un errore di conto
! Trabocchetto: non vale il viceversa: I_{2} e ( 1 1 ; 0 1 ) hanno stessi determinante, traccia e rango, ma l'unica matrice simile a I_{2} è I_{2}.
> Vedi anche: Endomorfismi e cambio di base, Teorema di Binet, Polinomio caratteristico

# Autovettori e diagonalizzabilità

## Autovettori e autovalori {59}
= Un **autovettore** di un endomorfismo T è un vettore v **≠ 0** con T(v) = λv per qualche λ ∈ 𝕂; λ è l'**autovalore** associato. È una direzione che T non fa girare.
![a sinistra la y si dimezza a ogni passo, a destra la componente lungo v₁ si triplica e quella lungo v₂ si ribalta](figure/alg/autovettori_iterate.png)
- per A = ( 1 2 ; 2 1 ): A(1, 1) = (3, 3), autovalore 3; A(1, −1) = (−1, 1), autovalore −1
- i multipli non nulli μv di un autovettore sono autovettori con lo stesso λ: si pensa a direzioni, non a singoli vettori
- l'autovalore può essere 0: gli autovettori di autovalore 0 sono i vettori non nulli di Ker T, per esempio (1, −1) per ( 1 1 ; 1 1 )
- in coordinate: T(v) = λv ⟺ Ax = λx, con A = [T]^{B}_{B} e x = [v]_{B}
- per ( 3 4 ; 0 2 ): e_{2} non è autovettore, (−4, 1) sì, con autovalore 2
! Trabocchetto: v = 0 non è mai un autovettore (lo sarebbe per ogni λ), mentre λ = 0 è un autovalore lecito.
> Vedi anche: Rotazione senza autovettori, Endomorfismo diagonalizzabile, Autospazio

## Rotazione senza autovettori {59, 61, 63}
= La rotazione di 90° di ℝ², (x, y) ↦ (−y, x), non ha autovettori reali: ogni vettore non nullo finisce su un vettore perpendicolare.
![ogni vettore blu va in un vettore rosso perpendicolare](figure/alg/rotazione_senza_autovettori.png)
- matrice nella base canonica ( 0 −1 ; 1 0 ), con p_{A}(t) = t^{2} + 1: nessuna radice reale
- vista da ℂ² in ℂ² gli autovalori ci sono, i e −i; per la rotazione oraria ( 0 1 ; −1 0 ) (stessi conti) gli autospazi sono V_{i} = Span((1, i)) e V_{−i} = Span((1, −i))
- ogni rotazione di θ ≠ 0, π: p_{A}(t) = t^{2} − 2cos θ · t + 1 ha discriminante −4sin^{2}θ < 0
- θ = 0 e θ = π danno I_{2} e −I_{2}: ogni vettore non nullo è autovettore
! Trabocchetto: conta il campo: la stessa matrice non è diagonalizzabile su ℝ (fallisce la condizione (a)), ma lo è su ℂ, con due autovalori distinti.
> Vedi anche: Teorema di diagonalizzabilità, Polinomio caratteristico

## Endomorfismo diagonalizzabile {60}
= T : V → V è **diagonalizzabile** se esiste una base di V fatta di autovettori di T; equivalentemente, se esiste una base B con [T]^{B}_{B} diagonale.
- se T(v_{i}) = λ_{i}v_{i}, allora [T]^{B}_{B} = diag(λ_{1}, …, λ_{n}): gli autovalori, nello stesso ordine dei vettori della base
- viceversa, se [T]^{B}_{B} è diagonale, i vettori di B sono autovettori e la diagonale contiene i loro autovalori
- esempio: ( 3 4 ; 0 2 ) nella base B = {(1, 0), (−4, 1)} diventa diag(3, 2)
- T è diagonalizzabile se e solo se lo è una sua matrice [T]^{B}_{B}, in una base qualsiasi
- nella base di autovettori T si limita ad allungare o accorciare ciascun asse, e le iterate diventano facili
> Vedi anche: Diagonalizzare una matrice, Autovettori e autovalori

## Diagonalizzare una matrice {60}
= A ∈ M(n, 𝕂) è diagonalizzabile se e solo se A = P D P^{−1}, con P = (v_{1} | … | v_{n}) che ha in colonna una base di autovettori e D = diag(λ_{1}, …, λ_{n}).
- P è il cambio di base dalla base di autovettori alla canonica: A è simile alla matrice diagonale D
- dispense: D = M^{−1} A M, con M = P
- potenze: A^{k} = P D^{k} P^{−1}, con D^{k} = diag(λ_{1}^{k}, …, λ_{n}^{k})
- esempio: A = ( 3 4 ; 0 2 ), M = ( 1 −4 ; 0 1 ) e D = diag(3, 2) danno A^{100} = ( 3^{100} 4·(3^{100} − 2^{100}) ; 0 2^{100} )
```
( 1 2 )   ( 1  1 )   ( 3  0 )   ( 1/2  1/2 )
( 2 1 ) = ( 1 −1 ) · ( 0 −1 ) · ( 1/2 −1/2 )
```
! Trabocchetto: l'ordine degli autovalori in D deve seguire quello degli autovettori in P: con la stessa P e D′ = diag(−1, 3) si ottiene ( 1 −2 ; −2 1 ), un'altra matrice.
> Vedi anche: Endomorfismo diagonalizzabile, Matrici simili, Teorema di diagonalizzabilità

# Polinomio caratteristico e diagonalizzabilità

## Polinomio caratteristico {61}
= Il **polinomio caratteristico** di A ∈ M(n, 𝕂) è p_{A}(t) = det(A − tI_{n}) (nelle dispense p_{A}(λ) = det(A − λI_{n})); λ ∈ 𝕂 è un autovalore se e solo se p_{A}(λ) = 0.
- catena: Av = λv con v ≠ 0 ⟺ Ker(A − λI_{n}) ≠ {0} ⟺ A − λI_{n} non invertibile ⟺ det(A − λI_{n}) = 0
- ha grado n con coefficiente di testa (−1)^{n}: al massimo n autovalori
- termine noto p_{A}(0) = det A: 0 è autovalore se e solo se A non è invertibile
- matrici simili hanno lo stesso polinomio caratteristico; per un endomorfismo, p_{T}(t) si calcola su una sua matrice in una base qualsiasi
- esempio: per ( 1 2 ; 2 1 ), p_{A}(t) = (1 − t)^{2} − 4 = t^{2} − 2t − 3 = (t − 3)(t + 1): autovalori 3 e −1
! Trabocchetto: lo stesso polinomio caratteristico non rende simili due matrici: la proposizione non si inverte.
> Vedi anche: Scorciatoie per il polinomio caratteristico, Matrici simili, Autospazio

## Scorciatoie per il polinomio caratteristico {61}
= Per una 2 × 2 p_{A}(t) = t^{2} − (tr A)·t + det A; per una triangolare p_{A}(t) = (a_{11} − t) ··· (a_{nn} − t), e gli autovalori si leggono sulla diagonale.
- A − tI_{n} è A con t tolto sulla diagonale: non serve rifare il prodotto per l'identità
- 2 × 2: λ_{1} + λ_{2} = tr A e λ_{1}λ_{2} = det A; per ( 2 1 ; 1 2 ), t^{2} − 4t + 3 = (t − 1)(t − 3)
- triangolari: ( 1 0 0 ; 1 2 0 ; 2 1 3 ) ha autovalori 1, 2, 3; ( 3 4 ; 0 2 ) ha autovalori 3 e 2
- le altre si sviluppano con Laplace: per ( 1 1 −1 ; 2 1 1 ; 3 0 2 ) esce p_{A}(t) = (2 − t)(t^{2} − 2t + 2), con l'unico autovalore reale 2
! Trabocchetto: la formula con traccia e determinante vale solo per n = 2; già per n = 3 il coefficiente di testa è (−1)^{3} = −1.
> Vedi anche: Polinomio caratteristico, Determinante di triangolari e trasposta

## Autospazio {62}
= L'**autospazio** di un autovalore λ è V_{λ} = {v | T(v) = λv} = Ker(T − λI): tutti gli autovettori di autovalore λ più il vettore nullo. È un sottospazio.
![gli autospazi di ( 2 1 ; 1 2 ): su V₃ si triplica, su V₁ si resta fermi, e₁ cambia direzione](figure/alg/autospazi_2112.png)
- per una matrice si risolve il sistema omogeneo (A − λI_{n})x = 0
- dim V_{λ} = n − rk(A − λI_{n}), dal teorema della dimensione
- esempio: per A = ( 2 1 ; 1 2 ), A − I_{2} = ( 1 1 ; 1 1 ) dà V_{1} = Span((−1, 1)) e A − 3I_{2} = ( −1 1 ; 1 −1 ) dà V_{3} = Span((1, 1))
- in ℝ², con autospazi che sono rette, due vettori dello stesso V_{λ} sono multipli e quindi dipendenti: se ne prende uno per autospazio; in generale si uniscono le basi degli autospazi
! Trabocchetto: 0 sta nell'autospazio ma non è un autovettore: gli autovettori sono i vettori **non nulli** di V_{λ}.
> Vedi anche: Autovalori distinti, Molteplicità algebrica e geometrica

## Autovalori distinti {62}
= Autovettori con autovalori **distinti** sono linearmente indipendenti; quindi, se dim V = n e T ha n autovalori distinti in 𝕂, T è diagonalizzabile.
- dimostrazione per induzione: si applica T alla combinazione nulla, si sottrae λ_{k} volte la combinazione e l'ultimo termine sparisce
- n autovettori indipendenti in dimensione n formano una base, fatta di autovettori
- esempi: ( 2 1 ; 1 2 ) (1 e 3), ( 1 2 ; 2 1 ) (3 e −1), ( 3 4 ; 0 2 ) (3 e 2), ( 1 0 0 ; 1 2 0 ; 2 1 3 ) (1, 2 e 3)
- su ℂ, pescando una matrice a caso, con probabilità 1 ha n autovalori distinti: «quasi ogni matrice è diagonalizzabile»
! Trabocchetto: la condizione è sufficiente, non necessaria: I_{2} ha il solo autovalore 1 ed è diagonalizzabile, perché è già diagonale.
> Vedi anche: Somma diretta e autospazi, Teorema di diagonalizzabilità

## Somma diretta e autospazi {62}
= W_{1}, …, W_{k} sono in **somma diretta**, W_{1} ⊕ … ⊕ W_{k}, se l'unico modo di scrivere 0 = w_{1} + … + w_{k} con w_{i} ∈ W_{i} è quello con tutti i w_{i} = 0.
- due sottospazi sono in somma diretta se e solo se W_{1} ∩ W_{2} = {0}
- se V = W_{1} ⊕ … ⊕ W_{k}, unendo basi dei W_{i} si ottiene una base di V, e dim V = dim W_{1} + … + dim W_{k}
- gli autospazi di autovalori distinti sono sempre in somma diretta
- quindi T è diagonalizzabile ⟺ dim V_{λ1} + … + dim V_{λk} = dim V, sommando su **tutti** gli autovalori
- ( 1 1 ; 0 1 ): unico autovalore 1 e V_{1} = Span((1, 0)), di dimensione 1 < 2: non diagonalizzabile
! Trabocchetto: con tre o più sottospazi non bastano le intersezioni a due a due: in ℝ² gli assi e Span((1, 1)) si toccano solo nell'origine, ma (1, 0) + (0, 1) + (−1, −1) = 0.
> Vedi anche: Autovalori distinti, Molteplicità algebrica e geometrica

## Molteplicità algebrica e geometrica {63}
= La **molteplicità algebrica** m_{a}(λ) è quante volte λ è radice di p_{T}(t); la **molteplicità geometrica** m_{g}(λ) = dim V_{λ} è quante direzioni indipendenti vengono moltiplicate per λ.
- m_{a}(λ) = m se p_{T}(t) = (t − λ)^{m} · q(t) con q(λ) ≠ 0
- per una matrice: m_{g}(λ) = n − rk(A − λI_{n})
- vale sempre 1 ≤ m_{g}(λ) ≤ m_{a}(λ): un autospazio può essere troppo piccolo, mai troppo grande
- se m_{a}(λ) = 1, allora m_{g}(λ) = 1: gli autovalori semplici non danno problemi
```
A = ( 1 1 )   p(t) = (1 − t)²             m_a(1) = 2
    ( 0 1 )   A − I₂ = ( 0 1 ; 0 0 ), rango 1   m_g(1) = 2 − 1 = 1
```
! Trabocchetto: m_{a}(λ) si legge sul polinomio, m_{g}(λ) va calcolata sull'autospazio: possono essere diverse, come per ( 1 1 ; 0 1 ).
> Vedi anche: Autospazio, Teorema di diagonalizzabilità

## Teorema di diagonalizzabilità {63}
= T : V → V, con dim V = n, è diagonalizzabile se e solo se (a) p_{T}(t) ha n radici **in 𝕂**, contate con molteplicità, e (b) m_{a}(λ) = m_{g}(λ) per ogni autovalore λ.
- due modi di fallire: la rotazione su ℝ fallisce la (a); ( 1 1 ; 0 1 ), su ℝ come su ℂ, fallisce la (b)
- su ℂ la (a) vale sempre, per il teorema fondamentale dell'algebra: basta controllare la (b)
- passi: p_{A}(t), radici e m_{a}, poi m_{g}(λ) = n − rk(A − λI_{n}) solo se m_{a} ≥ 2; es. 18.11: ( 3 0 0 ; −4 −1 −8 ; 0 0 3 ) ha m_{g}(3) = 2 = m_{a}(3), diagonalizzabile
- esempio 18.12, su ℝ con parametro: p_{A}(t) = (2 − t)(t^{2} + k − 5); per k > 5 fallisce la (a), per k = 5 la (b) (m_{g}(0) = 1 < 2): diagonalizzabile se e solo se k < 5
! Trabocchetto: radici tutte reali non bastano, serve m_{g} = m_{a} per ogni autovalore multiplo: ( 1 0 0 ; 0 1 0 ; 0 0 2 ) è diagonalizzabile, ( 1 1 0 ; 0 1 0 ; 0 0 2 ) no, con lo stesso polinomio.
> Vedi anche: Molteplicità algebrica e geometrica, Diagonalizzare una matrice, Rotazione senza autovettori
