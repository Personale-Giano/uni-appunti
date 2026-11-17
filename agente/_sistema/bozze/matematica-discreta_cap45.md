# 45. Altre Proprietà della Divisibilità e il Massimo Comun Divisore
## Sottrazione e ordine in ℤ
Prima di tornare alla divisibilità servono due nozioni che finora sono state usate senza dirlo. La prima è la **sottrazione**, che non è una terza operazione: è l'addizione con l'opposto, a − b = a + (−b). La seconda è l'ordine, che si definisce a partire dai numeri naturali ℕ = {0, 1, 2, …}.

**Definizione.** Dati a, b ∈ ℤ, si dice che **a ≥ b** se a − b ∈ ℕ, cioè se esiste c ∈ ℕ tale che a = b + c.

(In parole povere: il numero a è maggiore o uguale a b quando per arrivare da b ad a bisogna aggiungere un numero naturale, cioè non bisogna mai tornare indietro.)

**Esempio.** 3 ≥ −2, perché 3 − (−2) = 5 è un numero naturale. Invece non è vero che −7 ≥ −2, perché −7 − (−2) = −5 non è un naturale.

Nel seguito comparirà spesso anche il valore assoluto |n|, cioè n senza il segno: |5| = 5 e |−5| = 5.

## Altre proprietà della divisibilità
Si ricorda la definizione del cap. 44, scritta con le lettere che si useranno d'ora in poi: a **divide** b, e si scrive a | b, se esiste c ∈ ℤ tale che a · c = b. Si dice anche che a è un **divisore** di b, oppure che b è un **multiplo** di a.

**Esempio.** I segni non danno fastidio: 2 | 6 perché 6 = 2 · 3; 2 | −6 perché −6 = 2 · (−3); −2 | 6 perché 6 = (−2) · (−3); −2 | −6 perché −6 = (−2) · 3.

Dalla definizione si ricavano subito alcune proprietà, che si aggiungono a quelle del cap. 44:
- **i segni non contano**: se a | b, allora ±a | ±b, con qualunque scelta dei due segni, come nell'esempio;
- ogni numero divide se stesso e il suo opposto: n | n, perché n = n · 1, e n | −n;
- n | 0 per ogni n ∈ ℤ, perché 0 = n · 0, e 0 è l'unico multiplo di 0;
- 1 e −1 dividono ogni intero, e sono i soli a farlo: se m | n per ogni n ∈ ℤ, in particolare m | 1, quindi m · c = 1 per qualche intero c; allora |m| · |c| = 1, e due interi positivi con prodotto 1 valgono entrambi 1: dunque |m| = 1, cioè m = ±1;
- se n | a e n | b, allora n | a + b e n | a − b: infatti, se a = n · x e b = n · y, allora a + b = n · (x + y) e a − b = n · (x − y). È il punto 1 della proposizione sui divisori di una somma (cap. 44).

L'ultima proprietà riguarda il prodotto, ed è quella che servirà per parlare di numeri primi.

**Proposizione.** Se n | a, allora n | a · b per ogni b ∈ ℤ. Non vale invece, in generale, l'implicazione «se n | a · b, allora n | a oppure n | b»: n può dividere un prodotto senza dividere nessuno dei due fattori.

(In parole povere: un multiplo di n, moltiplicato per qualsiasi cosa, resta un multiplo di n. Ma un multiplo di n può nascere anche dal prodotto di due numeri che multipli di n non sono.)

Infatti, se a = n · x, allora a · b = n · (x · b). Per la seconda affermazione basta un controesempio: 6 | 2 · 3 (infatti 2 · 3 = 6), ma 6 non divide 2 e non divide 3. I numeri n per cui l'implicazione «se n | a · b, allora n | a oppure n | b» vale sempre sono proprio quelli che nel cap. 44 sono stati chiamati primi.

## I divisori di un numero sono in numero finito
**Proposizione.** Sia n ∈ ℤ con n ≠ 0. Se d | n, allora |d| ≤ |n|. Di conseguenza l'insieme dei divisori di n è un insieme finito.

(In parole povere: un divisore non può essere «più grande» del numero che divide, quindi i divisori di n vanno cercati solo tra −|n| e |n|.)

Infatti, se n = d · c, il numero c non è 0 (altrimenti sarebbe n = 0), quindi |c| ≥ 1 e |n| = |d| · |c| ≥ |d|. I divisori di n stanno allora tutti tra −|n| e |n|, e gli interi in questo intervallo sono in numero finito.

**Esempio.** I divisori di 18 sono ±1, ±2, ±3, ±6, ±9, ±18: dodici in tutto, e nessuno supera 18 in valore assoluto. L'ipotesi n ≠ 0 serve davvero: ogni intero divide 0, quindi 0 ha infiniti divisori.

## Il massimo comun divisore
Si prendono ora due interi m e n **non entrambi nulli** e si guarda l'insieme dei loro divisori comuni, { d ∈ ℤ : d | m e d | n }. Questo insieme non è vuoto, perché contiene sempre 1 e −1. Inoltre è finito: almeno uno tra m e n è diverso da 0, e i suoi divisori sono in numero finito. Un insieme finito e non vuoto di interi ha un massimo, quindi ha senso la definizione seguente.

**Definizione.** Siano m, n ∈ ℤ non entrambi nulli. Il **massimo comun divisore** di m e n è il più grande intero che divide sia m sia n: MCD(m, n) = max { d ∈ ℤ : d | m e d | n }. Si scrive anche, più brevemente, (m, n).

(In parole povere: si elencano i numeri che dividono tutti e due, e si prende il più grande. È il «pezzo» più grande con cui si riescono a misurare esattamente sia m sia n.)

Due osservazioni seguono subito dalla definizione.
- MCD(m, n) > 0, qualunque sia il segno di m e di n: tra i divisori comuni c'è sempre 1, quindi il massimo vale almeno 1.
- Se n | m, allora MCD(m, n) = |n|. Infatti |n| divide sia n sia m, e nessun divisore di n supera |n|. Per esempio MCD(35, 7) = 7 e MCD(24, −6) = 6. In particolare MCD(0, n) = |n| per ogni n ≠ 0, perché n | 0.

**Attenzione.** La scrittura breve (m, n) è la stessa delle coppie ordinate e somiglia a quella dei cicli e del tipo di una permutazione. È il contesto a dire di che cosa si sta parlando; nel dubbio conviene scrivere MCD(m, n).

## Come si calcola: il metodo diretto
Il primo modo di calcolare il massimo comun divisore è applicare la definizione alla lettera. Si scrivono l'insieme D_{m} dei divisori di m e l'insieme D_{n} dei divisori di n, si prende l'intersezione e se ne cerca il massimo: MCD(m, n) = max(D_{m} ∩ D_{n}).

**Esempio.** Per calcolare MCD(18, 21):
- D_{18} = { ±1, ±2, ±3, ±6, ±9, ±18 };
- D_{21} = { ±1, ±3, ±7, ±21 };
- D_{18} ∩ D_{21} = { ±1, ±3 }, il cui massimo è 3.

Quindi MCD(18, 21) = 3.

Poiché il massimo è sempre positivo, ci si può limitare ai divisori positivi. Per MCD(15, −40): i divisori positivi di 15 sono 1, 3, 5, 15, quelli di −40 sono 1, 2, 4, 5, 8, 10, 20, 40; quelli comuni sono 1 e 5, quindi MCD(15, −40) = 5. Allo stesso modo MCD(28, 100) = 4.

Il metodo diretto funziona bene con numeri piccoli, ma diventa sempre più laborioso man mano che i numeri crescono, perché obbliga a trovare tutti i divisori. Serve un procedimento che dia il massimo comun divisore senza elencarli, e lo strumento su cui si basa è la divisione con il resto: è l'argomento del prossimo capitolo.
