# Combinazioni con ripetizione e binomiali

## Combinazioni con ripetizione {28, 55}
= Una **combinazione con ripetizione** di ordine k in un insieme di n elementi è una scelta di k elementi non ordinata in cui lo stesso elemento si può prendere più volte.
![caselle e separatori per x³y²z⁵ e per x²z⁸](figure/mate/ch28_caselle_separatori.png)
- **formula**: C^{r}_{n,k} = C_{k+n−1, n−1} = (k + n − 1)!/((n − 1)! · k!); la r non è un esponente
- trucco: k caselle per le scelte più **n − 1 separatori**, che occupano caselle proprie; si scelgono le n − 1 caselle dei separatori fra le k + n − 1
- monomi di grado 10 in x, y, z: C^{r}_{3,10} = C_{12,2} = 66
- 30 pasticcini scelti fra 20 tipi: C^{r}_{20,30} = C_{49,19}; k può superare n, perché si può ripetere
- per la simmetria lo stesso numero si scrive anche (n + k − 1 su k)
! Trabocchetto: i separatori sono n − 1 e non n: per separare 3 variabili bastano 2 sbarrette, quindi per i monomi la striscia ha 12 caselle e non 13.
> Vedi anche: Il quadro dei quattro conteggi, Binomio di Newton

## Il quadro dei quattro conteggi {28, 55}
= Per k scelte in un insieme di n elementi si fanno due domande: l'ordine conta? Le scelte si possono ripetere?
- ordinate: **disposizioni** (con ripetizione D^{r}_{n,k}, semplici D_{n,k}); con k = n gli ordinamenti, n!
- non ordinate: **combinazioni** (semplici C_{n,k}, con ripetizione C^{r}_{n,k})
```
                senza ripetizione    con ripetizione
ordinate        n!/(n − k)!          nᵏ
non ordinate    (n su k)             (k + n − 1 su n − 1)
```
! Trabocchetto: le formule sono la parte facile; l'errore tipico è rispondere male alle due domande (ordine? ripetizione?).
> Vedi anche: Combinazioni con ripetizione

## Casi banali e simmetria dei binomiali {29}
= Il **coefficiente binomiale** (n su k) = n!/(k!(n − k)!) conta i sottoinsiemi di k elementi di un insieme di n. Valgono (n su 0) = (n su n) = 1, (n su 1) = n e la **simmetria** (n su k) = (n su n − k).
- (n su 0) = 1: l'unico sottoinsieme vuoto; (n su n) = 1: si prende tutto; (n su 1) = n: un elemento qualunque
- simmetria: scegliere i k da tenere è come scegliere gli n − k da lasciare
- prova combinatoria: F(S) = A ∖ S va dai sottoinsiemi di k elementi a quelli di n − k; G(T) = A ∖ T è l'inversa, quindi F è biettiva
- serve calcolare solo metà riga: (32 su 26) = (32 su 6)
! Trabocchetto: F e G hanno la stessa espressione, ma sono funzioni diverse: dominio e codominio sono scambiati.
> Vedi anche: Formula di Stiefel

## Formula di Stiefel {30}
= Per n ≥ 1 e 1 ≤ k ≤ n vale (n − 1 su k − 1) + (n − 1 su k) = (n su k): ogni coefficiente è la somma dei due della riga sopra.
![i sottoinsiemi con x e quelli senza x](figure/mate/stiefel_tipi.png)
- esempio: (11 su 4) + (11 su 5) = 330 + 462 = 792 = (12 su 5)
- prova combinatoria: si fissa x ∈ A; i sottoinsiemi con x sono (n − 1 su k − 1), quelli senza x sono (n − 1 su k)
- i due tipi sono disgiunti e coprono tutto: si sommano
- con i fattoriali: denominatore comune k!(n − k)!, e k + (n − k) = n
! Trabocchetto: per k = n il secondo addendo (n − 1 su n) non ha senso con i fattoriali: si intende uguale a 0.
> Vedi anche: Triangolo di Tartaglia, Casi banali e simmetria dei binomiali

## Triangolo di Tartaglia {30}
= Tabella dei coefficienti binomiali: la riga n contiene (n su k) per k da 0 a n; ogni numero interno è la somma dei due che ha sopra.
![il triangolo fino a n = 6](figure/mate/tartaglia.png)
- ogni riga comincia e finisce con 1 ed è simmetrica
- oltre le Alpi si chiama **triangolo di Pascal**
- è il modo ricorsivo di calcolare i coefficienti per n e k non troppo grandi
! Trabocchetto: la prima riga è n = 0 e la prima posizione è k = 0: il 6 della riga 4 è (4 su 2), non (4 su 3).
> Vedi anche: Formula di Stiefel, Binomio di Newton

## Binomio di Newton {31, 32}
= Per ogni n ≥ 0: (a + b)^{n} = Σ_{k=0}^{n} (n su k) a^{n−k} b^{k}; il coefficiente di a^{n−k} b^{k} è (n su k).
- (a + b)^{4} = a^{4} + 4a^{3}b + 6a^{2}b^{2} + 4ab^{3} + b^{4}: una riga del triangolo
- perché: dagli n fattori (a + b) si prende a oppure b; a^{n−k} b^{k} compare tante volte quanti i modi di scegliere i k fattori da cui prendere b
- in ogni termine un esponente scende e l'altro sale: il grado totale è sempre n
- con a = b = 1: Σ_{k=0}^{n} (n su k) = 2^{n}, cioè i sottoinsiemi di un insieme di n elementi sono 2^{n}
! Trabocchetto: è una combinazione semplice, non con ripetizione: non si scelgono lettere a o b, si sceglie quali fattori (interruttori) vanno su b.
> Vedi anche: Triangolo di Tartaglia, Combinazioni con ripetizione

# Permutazioni e cicli

## Permutazione e tabella a due righe {32}
= Una **permutazione** di X è una funzione biettiva X → X; S_{n} è l'insieme delle permutazioni di {1, …, n} e |S_{n}| = n!.
- S_{3} ha 6 elementi: l'identità, tre scambi e i due giri 1 → 2 → 3 → 1 e 1 → 3 → 2 → 1
- **tabella a due righe**: sopra 1, …, n, sotto le immagini; la seconda riga contiene ogni numero una sola volta
- **inversa**: si scambiano le righe e si riordinano le colonne
- l'identità è neutra, ogni permutazione ha un'inversa, la composizione è associativa
```
π    = 1 2 3 4 5 6 7       π⁻¹ = 1 2 3 4 5 6 7
       3 4 6 1 2 5 7             4 5 1 2 6 3 7
```
! Trabocchetto: una seconda riga come 2 5 3 1 5 non è una permutazione: il 5 compare due volte, quindi la funzione non è iniettiva.
> Vedi anche: Composizione di permutazioni

## Composizione di permutazioni {32}
= σ ∘ π applica **prima π e poi σ**: si segue ogni numero attraverso le permutazioni, da destra a sinistra.
- **metodo a tre righe**: tabella di π, poi sotto ogni numero della seconda riga la sua immagine secondo σ; si tiene la prima e l'ultima riga
- la composizione di permutazioni è ancora una permutazione
- **non è commutativa** da n = 3 in poi: in S_{3}, (1 3) ∘ (2 3) e (2 3) ∘ (1 3) sono i due giri diversi
```
π        1 2 3 4 5 6 7
         3 4 6 1 2 5 7
σ = 5 2 6 1 3 7 4
σ(π(i))  6 1 7 5 2 3 4      σ ∘ π
π ∘ σ:   2 4 5 3 6 7 1      (diverso)
```
! Trabocchetto: sotto la seconda riga non si ricopia la seconda riga di σ: si scrive σ del numero che sta sopra.
> Vedi anche: Permutazione e tabella a due righe, Comporre cicli non disgiunti

## Ciclo e notazione compatta {33, 34}
= Un **ciclo** (i_{1} i_{2} … i_{ℓ}) manda ogni elemento nel successivo, l'ultimo nel primo, e lascia fermi gli altri; ℓ ≥ 2 è la **lunghezza**. Un 2-ciclo è uno scambio.
- la scrittura è circolare: (1 3 7) = (3 7 1) = (7 1 3); un ℓ-ciclo si scrive in ℓ modi
- **inverso**: stessi numeri in ordine inverso, (2 5 4 6)^{−1} = (6 4 5 2)
- **quanti ℓ-cicli in S_{n}**: (1/ℓ) · n!/(n − ℓ)!; i 4-cicli di S_{6} sono 360/4 = 90
- si divide per ℓ perché ogni ciclo compare ℓ volte, una per punto di partenza
! Trabocchetto: (4 1 2 5) e (1 5 4 2) muovono gli stessi numeri ma sono cicli diversi: conta chi segue chi.
> Vedi anche: Cicli disgiunti, Scomposizione in cicli disgiunti

## Cicli disgiunti {33, 34}
= Due cicli sono **disgiunti** se gli insiemi degli elementi che muovono non hanno elementi in comune; due cicli disgiunti **commutano**.
- (3 6 2 9) e (1 4 7 5) sono disgiunti; (3 2 6 9 1 4) e (5 7 6 8) no, per il 6
- prova della commutazione: si controlla un elemento del primo ciclo, uno del secondo e uno fuori da entrambi
- **a due a due disgiunti**: ogni coppia ha intersezione vuota
- in generale la composizione non commuta, ma per alcune coppie sì
! Trabocchetto: {1, 2}, {2, 3}, {1, 3} non hanno un elemento comune a tutti, ma non sono a due a due disgiunti.
> Vedi anche: Ciclo e notazione compatta, Scomposizione in cicli disgiunti

## Scomposizione in cicli disgiunti {34, 35}
= Ogni π ≠ id si scrive in modo **essenzialmente unico** come composizione di cicli a due a due disgiunti: i cicli sono determinati da π, cambia solo l'ordine.
- si parte da un numero spostato e si seguono le frecce finché il giro si chiude; poi un numero fuori dal giro, e così via
- il giro si richiude proprio sul primo numero perché π è **iniettiva**
- se i cicli sono k, allora 2k ≤ n
- è l'analogo della scomposizione di un intero in primi
```
π(1..12) = 7 9 11 1 6 2 5 4 12 3 10 8
1 → 7 → 5 → 6 → 2 → 9 → 12 → 8 → 4 → 1
3 → 11 → 10 → 3
π = (1 7 5 6 2 9 12 8 4) ∘ (3 11 10)
```
! Trabocchetto: il ciclo che contiene un numero non si sceglie: è a, π(a), π(π(a)), …, deciso da π.
> Vedi anche: Tipo di una permutazione, Cicli disgiunti

## Tipo di una permutazione {34, 35, 38}
= Il **tipo** di π ≠ id è la lista (ℓ_{1}, …, ℓ_{k}) delle lunghezze dei suoi cicli disgiunti, dalla più lunga alla più corta.
- la somma delle lunghezze è al più n; i numeri fissi non si scrivono
- tipi di S_{4}: (4), (3), (2, 2), (2) e l'identità, con 6, 8, 3, 6 e 1 permutazioni: in tutto 24
- elencare i tipi somiglia alle **partizioni** di un numero (Ramanujan), ma qui la somma può essere minore di n
- l'esempio con 12 elementi ha tipo (9, 3)
! Trabocchetto: il tipo si legge solo dalla scrittura in cicli disgiunti, mai dai cicli di partenza.
> Vedi anche: Comporre cicli non disgiunti, Periodo come mcm

## Comporre cicli non disgiunti {35}
= Se π è data come composizione di cicli che si toccano, si segue ogni numero da destra a sinistra attraverso tutti i cicli e si ricostruiscono i cicli disgiunti.
- si trova l'immagine di un numero, si riparte da quella fino a chiudere il giro, poi si passa a un numero non ancora toccato
- da cicli di certe lunghezze si arriva a lunghezze del tutto diverse
- (1 3) ∘ (1 2 3) = (1 2): un 3-ciclo e un 2-ciclo danno un 2-ciclo
```
π = (1 2 3) ∘ (3 4 5) ∘ (1 5)
1 → 5 → 3 → 1     π(1) = 1
2 → 2 → 2 → 3     π(2) = 3
3 → 3 → 4 → 4     π(3) = 4
4 → 4 → 5 → 5     π(4) = 5
5 → 1 → 1 → 2     π(5) = 2     π = (2 3 4 5), tipo (4)
```
! Trabocchetto: si applica per primo il ciclo più a destra; partire da sinistra dà un'altra permutazione.
> Vedi anche: Composizione di permutazioni, Tipo di una permutazione

# Potenze e periodo

## Potenze e periodo {36, 37}
= π^{k} è π applicata k volte; il **periodo** di π è il più piccolo intero p > 0 con π^{p} = id.
- le permutazioni di S_{n} sono finite, quindi le potenze si ripetono; la prima ripetizione è proprio l'identità
- π^{0} = id, π^{−k} = (π^{−1})^{k}; π^{−1} = π^{p−1}
- id, π, …, π^{p−1} sono tutte diverse, poi il blocco si ripete
- **π^{k} = π^{r}**, con r resto di k diviso p: periodo 7 dà π^{1000} = π^{6}, perché 1000 = 7 · 142 + 6
- notazione del docente: per(σ), e l'identità si scrive (1)
! Trabocchetto: con i numeri le potenze sono tutte diverse (2, 4, 8, …); con le permutazioni no, perché sono un numero finito.
> Vedi anche: Periodo di un ciclo, Periodo come mcm

## Periodo di un ciclo {37}
= Un ciclo di lunghezza ℓ ha periodo ℓ: è una manopola con ℓ posizioni, e ogni applicazione la fa scattare di una.
- (1 2) ha periodo 2; (1 2 3)^{2} = (1 3 2) ≠ id e (1 2 3)^{3} = id
- c^{k} = id esattamente quando k è multiplo di ℓ
- con k < ℓ scatti il numero 1 va in k + 1 ≠ 1
! Trabocchetto: (1 2 3)^{2} muove gli stessi tre elementi, ma è un ciclo diverso, non l'identità.
> Vedi anche: Potenze e periodo, Periodo come mcm

## Periodo come mcm {37}
= Se π = c_{1} ∘ … ∘ c_{r} in cicli disgiunti di lunghezze ℓ_{1}, …, ℓ_{r}, il periodo è **mcm(ℓ_{1}, …, ℓ_{r})**; dipende solo dal tipo.
- i cicli disgiunti commutano, quindi π^{m} = c_{1}^{m} ∘ … ∘ c_{r}^{m}
- π^{p} = id solo se ogni c_{i}^{p} = id, cioè ogni ℓ_{i} divide p
- (2 6 5 1) ∘ (1 4 3 6) = (1 4 3 5) ∘ (2 6): periodo mcm(4, 2) = 4
- (1 6 3 7 4) ∘ (3 2 5 1) = (1 7 4) ∘ (2 5 6 3): periodo 12, non 5 · 4 = 20
```
σ = (1 2)(1 4)(5 6 7)(1 3 2)     da destra a sinistra
σ = (1 3) ∘ (2 4) ∘ (5 6 7)      tipo (3, 2, 2)
per(σ) = mcm(3, 2, 2) = 6
```
! Trabocchetto: il periodo è il mcm, non il prodotto, e solo sui cicli disgiunti: (1 2) ∘ (1 3) = (1 3 2) ha periodo 3, non mcm(2, 2) = 2.
> Vedi anche: Comporre cicli non disgiunti, Periodi possibili in Sₙ

## Periodi possibili in Sₙ {38}
= Si elencano i tipi di S_{n} e per ciascuno si calcola il mcm: in S_{6} i periodi possibili sono 1, 2, 3, 4, 5, 6.
- tipi di S_{6}: (6), (5), (4), (4, 2), (3), (3, 3), (3, 2), (2), (2, 2), (2, 2, 2) e l'identità
- (3, 2) dà 6, (4, 2) dà 4, (3, 3) dà 3
- al contrario: periodo 8 richiede un ciclo di lunghezza 8, quindi 8 elementi
- periodo 10 basta in S_{7}: (1 2 3 4 5) ∘ (6 7), perché 10 = mcm(5, 2) e 5 + 2 = 7
! Trabocchetto: (2, 2) è un tipo di S_{6} anche se la somma è 4: gli altri due elementi restano fermi.
> Vedi anche: Periodo come mcm, Tipo di una permutazione

# Scambi e parità

## Scambio o trasposizione {39}
= Uno **scambio** o **trasposizione** è un ciclo di lunghezza 2, (a b): manda a in b, b in a e lascia fermo il resto.
- s^{2} = id e (a b) = (b a)
- in S_{n} gli scambi sono (n su 2) = n(n − 1)/2: 6 in S_{4}, 10 in S_{5} su 120 permutazioni
- il docente scrive spesso i prodotti senza ∘: (1 3)(1 2) = (1 3) ∘ (1 2)
! Trabocchetto: anche senza il simbolo ∘ il prodotto si legge da destra a sinistra.
> Vedi anche: Ciclo come composizione di scambi

## Ciclo come composizione di scambi {39}
= Un ciclo di lunghezza ℓ si scrive con **ℓ − 1 scambi**, tutti con lo stesso elemento.
- con l'ultimo elemento: (1 2 … ℓ) = (ℓ−1 ℓ) ∘ … ∘ (2 ℓ) ∘ (1 ℓ)
- con il primo, come negli appunti: (s_{1} … s_{ℓ}) = (s_{1} s_{ℓ}) ∘ … ∘ (s_{1} s_{3}) ∘ (s_{1} s_{2})
- (1 2 3) = (2 3) ∘ (1 3) = (1 3) ∘ (1 2)
```
(1 2 3 4) = (3 4) ∘ (2 4) ∘ (1 4)
          = (1 4) ∘ (1 3) ∘ (1 2)      tre scambi
```
! Trabocchetto: gli scambi sono ℓ − 1, non ℓ: un 4-ciclo ne vuole tre.
> Vedi anche: Scambio o trasposizione, Ogni permutazione è composizione di scambi

## Ogni permutazione è composizione di scambi {39}
= Ogni permutazione si scrive come composizione di scambi: è composizione di cicli, e ogni ciclo è composizione di scambi.
- anche l'identità, se n ≥ 2: (1 2) ∘ (1 2) = id
- difetto 1: gli scambi non sono disgiunti, quindi in generale non commutano
- difetto 2: la scrittura non è unica, (2 3) = (1 3) ∘ (1 2) ∘ (1 3)
- per questo gli scambi sono utili più in teoria che nei conti
! Trabocchetto: in (1 3) ∘ (1 2) ∘ (1 3) i due (1 3) non si cancellano: non commutano con (1 2).
> Vedi anche: Teorema della parità

## Teorema della parità {40, 41, 42}
= Una scrittura con k scambi ha **parità** pari o dispari secondo k. **Teorema**: due scritture della stessa permutazione hanno la stessa parità.
- il numero di scambi può cambiare, ma solo di un numero pari: 117 scambi non diventano mai 224
- inversa: (s_{1} ∘ … ∘ s_{k})^{−1} = s_{k} ∘ … ∘ s_{1}, stessi scambi in ordine inverso e stessa parità
- la parità di una scrittura si guarda senza sapere che permutazione dà
! Trabocchetto: (2 3) si scrive con 1 o 3 scambi, ma mai con 2 o 4.
> Vedi anche: Dimostrazione della parità, Permutazioni pari e dispari

## Dimostrazione della parità {41}
= Ci si riduce a dimostrare che l'identità non si scrive mai con un numero dispari di scambi; poi si tolgono gli scambi due alla volta.
- id = π ∘ π^{−1} = s_{1} ∘ … ∘ s_{k} ∘ t_{h} ∘ … ∘ t_{1}: basta che k + h sia pari
- **osservazione cruciale**: in una scrittura dell'identità gli scambi con 1 sono nessuno oppure almeno due
- si spostano a destra e si cancellano quelli con 1, poi con 2, 3, …; solo la regola 4 cambia il totale, di 2, fino a 0
a, b, c diversi tra loro e da 1; si legge da destra a sinistra.
```
1. (1 a)(b c) = (b c)(1 a)
2. (1 a)(a b) = (a b)(1 b)
3. (1 a)(1 b) = (a b)(1 a)     scambi con 1: uno in meno
4. (1 a)(1 a) = id             due scambi in meno
```
! Trabocchetto: la dimostrazione non è un metodo di calcolo: la parità si calcola dai cicli.
> Vedi anche: Teorema della parità, Parità dal tipo

## Permutazioni pari e dispari {42}
= Una permutazione è **pari** se si scrive con un numero pari di scambi, **dispari** se con un numero dispari; per il teorema è sempre una delle due e mai entrambe.
- l'identità è pari (zero scambi); ogni scambio è dispari
- un ciclo di lunghezza ℓ ha ℓ − 1 scambi: è **pari se ℓ è dispari**, dispari se ℓ è pari
- (1 2 3) è pari, perché è (2 3) ∘ (1 3)
! Trabocchetto: la parità di un ciclo è il contrario della sua lunghezza: si contano gli scambi, ℓ − 1, non gli elementi.
> Vedi anche: Parità della composizione, Parità dal tipo

## Parità della composizione {42}
= La composizione è pari se i fattori hanno la stessa parità, dispari se hanno parità diverse: si sommano i numeri di scambi.
- con più fattori: è pari se e solo se i fattori dispari sono in numero pari
- i cicli **non devono essere disgiunti**: basta sommare le parità dei singoli cicli
- in S_{9}: (2 4 7) ∘ (1 4 5 8 2) ∘ (5 2 7 6) ∘ (6 9 4 8 1 5) ha 2 + 4 + 3 + 5 = 14 scambi, quindi è pari; il risultato è (5 8 7 6 9)
```
pari ∘ pari = pari          pari ∘ dispari = dispari
dispari ∘ pari = dispari    dispari ∘ dispari = pari
```
! Trabocchetto: per il periodo servono i cicli disgiunti, per la parità no: il tipo di una composizione non si ricava dai tipi dei fattori.
> Vedi anche: Permutazioni pari e dispari, Periodo come mcm

## Parità dal tipo {42}
= Se π ha tipo (ℓ_{1}, …, ℓ_{r}), si scrive con p = (ℓ_{1} − 1) + … + (ℓ_{r} − 1) scambi: π è pari se e solo se p è pari.
- tipo (3, 5, 6): 2 + 4 + 5 = 11 scambi, dispari
- (1 4 9) ∘ (2 11 5 7 3) ∘ (8 12) ∘ (6 10 13) in S_{13}: tipo (5, 3, 3, 2), 4 + 2 + 2 + 1 = 9, dispari
- è il metodo di calcolo che il teorema della parità non dà
! Trabocchetto: non si sommano le lunghezze: per il tipo (3, 5, 6) si sommerebbe 14, pari, ed è sbagliato.
> Vedi anche: Permutazioni pari e dispari, Tipo di una permutazione

## Metà pari e metà dispari {42}
= Per n ≥ 2 le permutazioni pari A_{n} e quelle dispari D_{n} sono tante quante: |A_{n}| = |D_{n}| = n!/2.
- A_{n} e D_{n} sono una partizione di S_{n}; il libro le chiama 𝒫_{n} e 𝒟_{n}
- F: A_{n} → D_{n}, F(π) = π ∘ (1 2) aggiunge uno scambio; G: D_{n} → A_{n} con la stessa legge è l'inversa
- S_{5}: 60 pari e 60 dispari; S_{4}: 12 e 12
- per n = 1 c'è solo l'identità, pari: niente dispari
! Trabocchetto: π ∘ (1 2) e (1 2) ∘ π sono diverse (in S_{3}, con π = (1 2 3), danno (1 3) e (2 3)), ma entrambe vanno bene per contare.
> Vedi anche: Parità della composizione

# Interi e divisibilità

## Operazioni in ℤ {43}
= In ℤ somma e prodotto sono associativi e commutativi, con neutri 0 e 1, e vale la distributiva; l'opposto esiste per la somma, l'inverso per il prodotto solo per ±1.
- 2 · x = 1 non ha soluzioni intere: 1/2 sta in ℚ
- rispetto alla somma 1 **genera** ℤ: con 1 e gli opposti si ottiene tutto; con 2 solo i pari
- rispetto al prodotto nessun numero genera ℤ: per questo serve la divisibilità
- le permutazioni hanno una sola operazione, con neutro e inverse, ma non commutativa
! Trabocchetto: l'opposto vale solo per la somma: in ℤ gli unici numeri con inverso moltiplicativo sono 1 e −1.
> Vedi anche: Divisibilità

## Divisibilità {44, 45}
= m **divide** n, m | n, se esiste k ∈ ℤ con n = k · m; si dice che n è **multiplo** di m. ∤ vuol dire «non divide».
- 3 | 12, 2 ∤ −7, −4 | 20; i segni non contano: se a | b allora ±a | ±b
- ogni intero divide 0; 0 divide solo 0; ±1 dividono tutti, e sono i soli a farlo
- non è una relazione di equivalenza: non è simmetrica
- se n ≠ 0 e d | n, allora |d| ≤ |n|: i divisori di n sono finiti (18 ne ha 12: ±1, ±2, ±3, ±6, ±9, ±18)
! Trabocchetto: m | n è un'affermazione, non un numero: 3 | 12 è vera, 12/3 è il numero 4, e 12 | 3 è falsa.
> Vedi anche: Divisori di una somma, Massimo comun divisore

## Divisori di una somma {44, 45}
= In a + b = s, se d divide due dei tre numeri, divide anche il terzo.
- se d | a e d | b, allora d | a + b e d | a − b: a + b = d(k + l)
- 7 | 21 e 7 | 35 danno 7 | 56; 7 ∤ 22, altrimenti dividerebbe 22 − 21 = 1
- **prodotto**: se n | a, allora n | a · b per ogni b
! Trabocchetto: da n | a · b non segue n | a oppure n | b (6 | 2 · 3): vale solo per i primi.
> Vedi anche: Divisibilità, Irriducibili e primi

## Massimo comun divisore {45, 49}
= Per m, n non entrambi nulli, MCD(m, n) è il più grande intero che divide entrambi; si scrive anche (m, n).
- esiste perché i divisori comuni sono finiti e c'è sempre 1; quindi MCD(m, n) ≥ 1
- se n | m, MCD(m, n) = |n|: MCD(35, 7) = 7, MCD(24, −6) = 6, MCD(0, n) = |n|
- **metodo diretto**: max(D_{m} ∩ D_{n}); MCD(18, 21) = 3, MCD(15, −40) = 5, MCD(28, 100) = 4
- MCD(a, b) = MCD(|a|, |b|): si lavora con i positivi
! Trabocchetto: la scrittura (m, n) si confonde con coppie, cicli e tipi: nel dubbio si scrive MCD(m, n).
> Vedi anche: Algoritmo di Euclide, Divisibilità

## Irriducibili e primi {44, 47}
= ±1 sono gli **invertibili**. Per n ≠ 0, ±1: n è **irriducibile** se i suoi soli divisori sono ±1 e ±n; n è **primo** se n | a · b implica n | a oppure n | b.
- irriducibile: in ogni scrittura n = a · b un fattore è ±1; 7 sì, 10 = 2 · 5 no
- primo: 6 non lo è, perché 6 | 4 · 9 ma 6 ∤ 4 e 6 ∤ 9
- anche −2, −3, −5, −7 sono irriducibili
- **primo ⟹ irriducibile**: da n = a · b e n | a viene a = kn, quindi n = (kb)n e, semplificando n ≠ 0, kb = 1, b = ±1
- un riducibile non è primo: da 10 = 2 · 5 si ha 10 | 2 · 5 senza dividere i fattori
! Trabocchetto: il «primo» della scuola (solo 1 e se stesso come divisori) è qui l'irriducibile: finché non si dimostra l'equivalenza le due definizioni vanno tenute distinte.
> Vedi anche: Irriducibile implica primo, Divisori di una somma

# Divisione euclidea e basi

## Divisione euclidea {46}
= Per a, b ∈ ℤ con b ≠ 0 esistono e sono **unici** q e r con a = q · b + r e **0 ≤ r < |b|**.
- 47 = 9 · 5 + 2; anche 47 = 8 · 5 + 7 e 47 = 10 · 5 − 3 sono vere, ma 7 e −3 non sono resti
- b | a esattamente quando il resto è 0
- esistenza: si toglie b finché si può (induzione forte, perché da a si salta ad a − b)
- unicità: b · (q − q') = r' − r con 0 ≤ r' − r < b, quindi r' − r = 0
- serve anche per le potenze: periodo 7 dà π^{10000} = π^{4}, perché 10000 = 7 · 1428 + 4
! Trabocchetto: senza la condizione 0 ≤ r < |b| le scritture sono infinite: è lei che rende unico il resto.
> Vedi anche: Divisione con i negativi, Cambio di base

## Divisione con i negativi {46}
= Il resto è sempre tra 0 e |b| − 1: si divide fra i numeri senza segno e poi si aggiusta.
- a < 0, b > 0: se −a dà quoziente q e resto r ≠ 0, a dà quoziente −q − 1 e resto b − r; se r = 0, quoziente −q e resto 0
- b < 0: si divide per −b; il quoziente cambia segno, il resto resta
- alla fine si controlla che l'uguaglianza torni
```
 2575 =  14 · 183  + 13
−2575 =  14 · (−184) + 1
 2575 = −14 · (−183) + 13
−2575 = −14 · 184  + 1
```
! Trabocchetto: il resto di −2575 diviso 14 è 1, non 13 e nemmeno −13.
> Vedi anche: Divisione euclidea

## Notazione posizionale {48}
= In base b ≥ 2, n = c_{k} … c_{1} c_{0} vuol dire n = c_{k} · b^{k} + … + c_{1} · b + c_{0}, con cifre da 0 a b − 1.
- 67942 = 6 · 10^{4} + 7 · 10^{3} + 9 · 10^{2} + 4 · 10 + 2; i numeri romani non sono posizionali
- dalla base b alla base 10: (2102)_{3} = 54 + 9 + 0 + 2 = 65, (22)_{3} = 8
- con b ≥ 10 si usano lettere: A = 10, B = 11, …; (2BA7)_{13} = 4394 + 1859 + 130 + 7 = 6390
- in ogni base «10» è la base stessa: (10)_{2} = 2; gli zeri a sinistra non contano
! Trabocchetto: ogni cifra deve essere un simbolo solo, altrimenti in base 13 «10» sarebbe ambiguo.
> Vedi anche: Cambio di base

## Cambio di base {48, 46}
= Dalla base 10 alla base b: si divide per b, poi il quoziente per b, fino a quoziente 0; i resti letti **dall'ultimo al primo** sono le cifre.
- il primo resto è la cifra delle unità c_{0}, per l'unicità della divisione euclidea
- 45 = (101101)_{2}: 32 + 8 + 4 + 1
- si controlla con la definizione
```
587 = 3 · 195 + 2
195 = 3 · 65  + 0
 65 = 3 · 21  + 2
 21 = 3 · 7   + 0
  7 = 3 · 2   + 1
  2 = 3 · 0   + 2     587 = (210202)₃
```
! Trabocchetto: leggere i resti dall'alto dà (202012)_{3} = 545, non 587; e ci si ferma solo a quoziente 0, perché anche l'ultimo resto è una cifra.
> Vedi anche: Notazione posizionale, Divisione euclidea

# Euclide Bézout e diofantee

## Algoritmo di Euclide {49}
= Si divide a per b, poi il divisore per il resto, e così via fino a resto 0: l'**ultimo resto non nullo** è MCD(a, b).
- termina perché i resti sono naturali che scendono strettamente: |b| > r_{1} > r_{2} > … ≥ 0
- perché funziona: risalendo, r_{m} divide tutte le righe, quindi a e b; scendendo, ogni divisore comune divide r_{m}
- quindi ogni divisore comune non solo è ≤ MCD, ma lo divide
- MCD(3575, 654) = 1 con 7 divisioni; MCD(14575, 105) = 5
```
252 = 198 · 1 + 54
198 =  54 · 3 + 36
 54 =  36 · 1 + 18
 36 =  18 · 2 + 0      MCD(252, 198) = 18
```
! Trabocchetto: il MCD è l'ultimo resto non nullo, non l'ultimo resto (0) né l'ultimo quoziente; alla riga dopo passano divisore e resto.
> Vedi anche: Identità di Bézout, Massimo comun divisore

## Identità di Bézout {50}
= Se d = MCD(a, b), esistono A, B ∈ ℤ, non unici, con d = A · a + B · b: il MCD è una **combinazione lineare** di a e b.
- si trova risalendo l'algoritmo di Euclide dal basso, sostituendo un resto alla volta
- 252 e 198: 18 = 54 − 36 = 4 · 54 − 198 = 4 · 252 − 5 · 198
- se b | a basta A = 0 e B = ±1: 7 = 0 · 35 + 1 · 7
```
126 = 35 · 3 + 21      7 = 21 − 14
 35 = 21 · 1 + 14        = 21 − (35 − 21) = 2 · 21 − 35
 21 = 14 · 1 + 7         = 2 · (126 − 3 · 35) − 35
 14 =  7 · 2 + 0         = 2 · 126 − 7 · 35
```
! Trabocchetto: non calcolare i prodotti come 2 · 21 = 42 durante la risalita: si perde da dove viene il 21; e alla fine si controlla moltiplicando.
> Vedi anche: Algoritmo di Euclide, Infinite coppie di Bézout

## Infinite coppie di Bézout {50}
= Se d = A · a + B · b, allora per ogni k ∈ ℤ anche A' = A + (b/d) · k e B' = B − (a/d) · k vanno bene.
- quello che si guadagna con a si perde con b: (ab/d) · k − (ab/d) · k = 0
- b/d e a/d sono interi, perché d divide a e b
- 126 e 35: 7 = (2 + 5k) · 126 + (−7 − 18k) · 35; con k = 1, 7 = 7 · 126 − 25 · 35
- 252 e 198: A' = 4 + 11k, B' = −5 − 14k; con k = −1, 18 = −7 · 252 + 9 · 198
! Trabocchetto: ad A si aggiunge il multiplo di b/d, a B si toglie quello di a/d: i due numeri si incrociano.
> Vedi anche: Identità di Bézout, Risolvere una diofantea

## Equazioni diofantee lineari {51}
= Un'equazione **diofantea** cerca solo soluzioni intere. a · x + b · y = c ha soluzioni intere **se e solo se d = MCD(a, b) divide c**.
- ⟹: d divide a · x_{0} e b · y_{0}, quindi la somma c
- ⟸: da Bézout d = A · a + B · b, moltiplicando per c/d si ha una soluzione
- 6x + 24y = 7 e 3x + 12y = 1 non hanno soluzioni intere (reali sì, per esempio x = 1/3, y = 0 per la seconda)
- 12x + 9y = c: soluzioni se e solo se 3 | c; con d = 1 ci sono per ogni c
- geometria: la retta passa per un nodo della griglia degli interi solo se d | c
! Trabocchetto: se d ∤ c le soluzioni non ci sono proprio: non è questione di cercarle meglio.
> Vedi anche: Risolvere una diofantea, Identità di Bézout

## Risolvere una diofantea {51}
= Si calcola d, si controlla d | c, si scrive Bézout e lo si moltiplica per c/d; tutte le soluzioni sono x = x_{0} + (b/d) · k, y = y_{0} − (a/d) · k.
- 252x + 198y = 54: d = 18 e 54 = 18 · 3, quindi x_{0} = 4 · 3 = 12, y_{0} = −5 · 3 = −15
- tutte: x = 12 + 11k, y = −15 − 14k; con k = −1 la più semplice, (1, −1)
- 252x + 198y = 7: 18 ∤ 7, nessuna soluzione
- 6x + 10y = 8: da 2 = 2 · 6 − 10 si moltiplica per 4, (8, −4); tutte x = 8 + 5k, y = −4 − 3k
- che non ce ne siano altre il docente lo enuncia senza dimostrarlo
```
1. d = MCD(a, b) con Euclide
2. d ∤ c  →  nessuna soluzione
3. d = A · a + B · b  risalendo
4. x₀ = A · c/d,  y₀ = B · c/d
5. x = x₀ + (b/d)k,  y = y₀ − (a/d)k
```
! Trabocchetto: con x_{0} + b · k e y_{0} − a · k si ottengono soluzioni, ma non tutte quando d > 1: va diviso per d.
> Vedi anche: Equazioni diofantee lineari, Infinite coppie di Bézout

# Coprimi e teorema fondamentale

## Numeri coprimi {52}
= a e b, non entrambi nulli, sono **coprimi** se MCD(a, b) = 1: non hanno divisori comuni oltre a ±1.
- non serve che siano primi: 8 e 9 sono coprimi; anche 3575 e 654
- per i coprimi Bézout diventa A · a + B · b = 1
- a · x + b · y = c ha soluzioni per ogni c, perché 1 divide tutto
- 252 e 198 non sono coprimi: MCD 18
! Trabocchetto: coprimi non vuol dire primi: 8 e 9 lo sono senza essere primi.
> Vedi anche: Lemma del prodotto coprimo, Identità di Bézout

## Lemma del prodotto coprimo {52}
= Se MCD(n, a) = 1 e n | a · b, allora n | b.
- prova: A · n + B · a = 1, moltiplicato per b dà A · n · b + B · a · b = b, somma di due multipli di n
- 9 | 4 · 18 = 72 e 9 è coprimo con 4: quindi 9 | 18
- 6 | 4 · 3 senza dividere i fattori: il 2 viene dal 4, il 3 dal 3
! Trabocchetto: non basta che n non divida a: 6 ∤ 4, ma MCD(6, 4) = 2, e infatti 6 non divide nemmeno 3.
> Vedi anche: Numeri coprimi, Irriducibile implica primo

## Irriducibile implica primo {52}
= Se n è irriducibile, allora è primo; con il cap. 47 si ha **n primo ⟺ n irriducibile**.
- prova: se n | a · b e n ∤ a, d = MCD(n, a) è 1 oppure |n|; |n| è escluso, quindi d = 1 e per il lemma n | b
- in ℤ primi e irriducibili sono gli stessi: ±2, ±3, ±5, ±7, ±11, …
- per riconoscere un primo si guardano i divisori; nelle prove si usa la proprietà sui prodotti
- si estende a più fattori: se p | a_{1} · … · a_{k}, p divide uno degli a_{i}
- 13 | 1001 = 7 · 143 e 13 ∤ 7, quindi 13 | 143 = 11 · 13
! Trabocchetto: la proprietà sui prodotti è falsa per i riducibili già con due fattori: 6 | 4 · 3.
> Vedi anche: Irriducibili e primi, Teorema fondamentale dell'aritmetica

## Teorema fondamentale dell'aritmetica {53}
= Ogni n ≠ 0 si scrive in modo unico, a meno dell'ordine, come n = ±p_{1} · … · p_{s}, con p_{i} primi positivi, anche ripetuti.
- 354 = 2 · 3 · 59; 360 = 2^{3} · 3^{2} · 5; −12 = −(2 · 2 · 3)
- per ±1 il prodotto è vuoto, s = 0
- 1 non è primo: con 10 = 1 · 2 · 5 = 1 · 1 · 2 · 5 l'unicità salterebbe
! Trabocchetto: l'unicità vale a meno dell'ordine: 2 · 3 · 2 e 2 · 2 · 3 sono la stessa fattorizzazione; e solo con primi positivi, altrimenti 6 = 2 · 3 = (−2) · (−3).
> Vedi anche: Dimostrazione del teorema fondamentale, Infinità dei primi

## Dimostrazione del teorema fondamentale {53}
= **Esistenza**: minimo controesempio, o induzione forte. **Unicità**: un primo di una scrittura divide un fattore dell'altra e quindi gli è uguale.
- esistenza: il minimo n non fattorizzabile non è primo, quindi n = a · b con 1 < a, b < n, che si fattorizzano: assurdo
- unicità: p_{1} | q_{1} · … · q_{t}, quindi p_{1} | q_{i}, e q_{i} irriducibile dà p_{1} = q_{i}; si semplifica e si ripete; se avanzano dei q resta 1 = q_{s+1} · … · q_{t}, assurdo
- l'esistenza usa irriducibile ⟹ primo; l'unicità usa entrambe le facce dei primi
! Trabocchetto: l'esistenza è la parte facile; il punto cruciale, secondo il docente, è l'unicità.
> Vedi anche: Teorema fondamentale dell'aritmetica, Irriducibile implica primo

## Infinità dei primi {53}
= **Teorema di Euclide**: i primi sono infiniti; per ogni n c'è un primo più grande di n.
- dato un insieme finito di primi S = {p_{1}, …, p_{k}}, N = p_{1} · … · p_{k} + 1 ha un fattore primo p
- se p fosse in S dividerebbe N e il prodotto, quindi la differenza 1: assurdo
- {2, 3, 5} dà 31 e {2, 3, 5, 7} dà 211, primi
- {2, 5, 11} dà 111 = 3 · 37: 3 e 37 sono primi nuovi
! Trabocchetto: N non è sempre primo: con i primi fino a 13, N = 30031 = 59 · 509; la prova dice solo che i suoi fattori primi sono nuovi.
> Vedi anche: Teorema fondamentale dell'aritmetica

# Congruenze e classi resto

## Congruenza modulo n {54}
= Fissato il **modulo** n, a ≡ b (mod n) se **n divide a − b**: a e b cadono nello stesso punto di un quadrante con n posizioni.
- orologio: 16 ≡ 4 (mod 12); minuti: 85 ≡ 25 (mod 60)
- periodo 8: 12 ≡ 4 e −3 ≡ 5 (mod 8), come π^{12} = π^{4} e π^{−3} = π^{5}
- a ≡ 0 (mod n) vuol dire n | a; modulo 2, a ≡ b vuol dire stessa parità
- con n = 1 tutti i numeri sono congruenti: caso banale
! Trabocchetto: è n che divide la differenza: 7 e 1 non sono congruenti modulo 12, perché 12 ∤ 6, anche se 6 | 12.
> Vedi anche: Classi resto

## Classi resto {56}
= Per N ≥ 2, la **classe resto** [r]_{N} è l'insieme degli interi che divisi per N danno resto r; stessa classe vuol dire congruenti.
- [3]_{7} = {…, −18, −11, −4, 3, 10, 17, 24, …}; −4 = (−1) · 7 + 3
- [0]_{N} = Nℤ, i multipli di N; per N = 2 pari e dispari
- x, y nella stessa classe ⟺ N | x − y ⟺ [x]_{N} = [y]_{N}
- le N classi sono una **partizione** di ℤ, quindi la congruenza è una **relazione di equivalenza**
- riflessiva: N | 0; simmetrica: −k · N; transitiva: si sommano le differenze
! Trabocchetto: la divisibilità non è simmetrica, la congruenza sì: N resta fisso e la differenza cambia solo segno.
> Vedi anche: Congruenza modulo n, ℤ_N e rappresentanti

## ℤ_N e rappresentanti {56}
= ℤ_{N} = {[0], [1], …, [N − 1]} è l'insieme quoziente: ha N elementi, e ognuno è un insieme infinito di interi.
- ℤ_{N} ⊆ 𝒫(ℤ): i suoi elementi sono sottoinsiemi di ℤ
- una classe si nomina con un suo elemento qualunque, il **rappresentante**
- [−3]_{11} = [8]_{11} = [19]_{11} = [107]_{11}: tutti danno resto 8
- notazioni: [a]_{N}, [a] o, nel libro, ā
! Trabocchetto: 8 = −3 è falso, [8]_{11} = [−3]_{11} è vero: un numero non è la sua classe.
> Vedi anche: Classi resto, Somma e prodotto in ℤ_N

## Somma e prodotto in ℤ_N {57}
= [a] + [b] = [a + b] e [a] · [b] = [a · b]; sono **ben definite**: il risultato non dipende dai rappresentanti.
- in ℤ_{6}: [4] + [5] = [3], [4] · [5] = [2]
- prova: a' = a + kN, b' = b + k'N danno a' + b' e a' · b' che differiscono da a + b e a · b per multipli di N
- [2] = [8] e [5] = [11] in ℤ_{6}: 7 e 19 stanno in [1], 10 e 88 in [4]
- con le congruenze: se a ≡ b e c ≡ d, allora a + c ≡ b + d e ac ≡ bd; 17 · 9 ≡ 5 · (−3) = −15 ≡ 9 (mod 12)
! Trabocchetto: la buona definizione va dimostrata, non data per scontata: nel cap. 12 una regola simile non definiva una funzione.
> Vedi anche: Proprietà e tabelle di ℤ_N, ℤ_N e rappresentanti

## Proprietà e tabelle di ℤ_N {57}
= Somma e prodotto in ℤ_{N} ereditano da ℤ associativa, commutativa, neutri [0] e [1], opposto −[a] = [−a] e distributiva.
- (ℤ_{N}, +) è un gruppo commutativo; in ℤ_{6} l'opposto di [2] è [4]
- nella tabella della somma ogni riga è la precedente spostata di un posto
- nella tabella del prodotto di ℤ_{5} ogni riga non nulla contiene l'1; in ℤ_{6} le righe di 2, 3, 4 no
```
ℤ₆  ·  0 1 2 3 4 5
    2  0 2 4 0 2 4
    3  0 3 0 3 0 3
    4  0 4 2 0 4 2
    5  0 5 4 3 2 1
```
! Trabocchetto: in ℤ_{N} un prodotto può fare zero con fattori non nulli ([2] · [3] = [0] in ℤ_{6}) e non si può semplificare: [3] · [2] = [3] · [4] ma [2] ≠ [4].
> Vedi anche: Somma e prodotto in ℤ_N, Invertibili e divisori dello zero

## Invertibili e divisori dello zero {58}
= [a] è **invertibile** se esiste [b] con [a] · [b] = [1]; [a] ≠ [0] è un **divisore dello zero** se esiste [b] ≠ [0] con [a] · [b] = [0].
- in ℤ_{5}, [2]^{−1} = [3]; in ℤ_{6}, [2] · [3] = [0]
- in ℤ_{9}, [3] · [3] = [0]: [a] e [b] possono coincidere
- un divisore dello zero non è invertibile: da [a] · [b] = [0] si avrebbe [b] = [a]^{−1} · [0] = [0]
- ℤ_{10}: invertibili [1], [3], [7], [9], con [3]^{−1} = [7] e [9]^{−1} = [9]
! Trabocchetto: tra i reali solo lo 0 non ha inverso; in ℤ_{N} anche classi non nulle possono non averlo.
> Vedi anche: Teorema delle classi invertibili

## Teorema delle classi invertibili {58}
= Per [a] ≠ [0] in ℤ_{N}: se MCD(a, N) = 1, [a] è invertibile; se MCD(a, N) > 1, [a] è un divisore dello zero.
- caso 1: a · A + N · B = 1 letto in ℤ_{N} dà [a] · [A] = [1], perché [N] = [0]
- caso 2: a = d · s, N = d · t con 0 < t < N, quindi [a] · [t] = [s · N] = [0]
- il MCD con N non dipende dal rappresentante: è una proprietà della classe
- ℤ_{p} con p primo: tutte le classi non nulle sono invertibili; ℤ_{35}: divisori dello zero i multipli di 5 o 7, le altre 24 classi non nulle invertibili
```
ℤ₄  inv [1] [3]            zero-div [2]
ℤ₅  inv [1] [2] [3] [4]    nessuno
ℤ₆  inv [1] [5]            zero-div [2] [3] [4]
```
! Trabocchetto: le classi non nulle sono o invertibili o divisori dello zero, mai entrambe e mai nessuna delle due.
> Vedi anche: Invertibili e divisori dello zero, Inverso con Bézout

## Inverso con Bézout {58}
= Se MCD(a, N) = 1, si scrive a · A + N · B = 1 con Euclide risalito: [a]^{−1} = [A]; il coefficiente B non serve.
- con N piccolo basta cercare l'1 nella riga di [a] della tabella; con N grande serve Bézout
- 1219 · 654 − 223 · 3575 = 1, quindi [654]^{−1} = [1219] in ℤ_{3575}
- con le congruenze: esiste b con ab ≡ 1 (mod N) se e solo se MCD(a, N) = 1
- 4 non ha inverso modulo 6: 4b − 1 è sempre dispari
```
35 = 3 · 11 + 2      1 = 11 − 5 · 2
11 = 5 · 2  + 1        = 11 − 5 · (35 − 3 · 11)
                       = 16 · 11 − 5 · 35
[11]⁻¹ = [16] in ℤ₃₅     11 · 16 = 176 = 5 · 35 + 1
```
! Trabocchetto: A può uscire negativo o maggiore di N: si prende il resto; in ℤ_{7}, 3 · (−2) + 7 · 1 = 1 dà [3]^{−1} = [−2] = [5].
> Vedi anche: Teorema delle classi invertibili, Identità di Bézout
