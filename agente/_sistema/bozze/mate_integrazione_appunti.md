@@ dopo cap4.50
**Trabocchetto d'esame (tutorato 2026).** Siccome ∅ ∈ 𝒫(A) per ogni insieme A, due insiemi delle parti non sono mai disgiunti: l'insieme vuoto sta sempre nella loro intersezione. Più precisamente 𝒫(A) ∩ 𝒫(B) = 𝒫(A ∩ B), perché un insieme X è contenuto sia in A sia in B se e solo se è contenuto in A ∩ B. Quindi, se A ∩ B = ∅, si ottiene 𝒫(A) ∩ 𝒫(B) = 𝒫(∅) = {∅}, che ha un elemento, e **non** l'insieme vuoto. Per esempio, con A = {1, 3} e B = {2, 5} si ha 𝒫(A) = {∅, {1}, {3}, {1, 3}} e 𝒫(B) = {∅, {2}, {5}, {2, 5}}: l'unico elemento in comune è ∅, quindi 𝒫(A) ∩ 𝒫(B) = {∅}. Scrivere «𝒫(A) ∩ 𝒫(B) = ∅» è l'errore tipico.

@@ dopo cap42.43
**Come scritto a lezione (lezione 2026).** Le due funzioni sono state scritte componendo lo scambio a sinistra: F(π) = (1 2) ∘ π e G(σ) = (1 2) ∘ σ. La dimostrazione è identica. Se π = τ_{1} ∘ … ∘ τ_{k} con k pari, allora (1 2) ∘ π = (1 2) ∘ τ_{1} ∘ … ∘ τ_{k} si scrive con k + 1 scambi ed è dispari; inoltre G(F(π)) = (1 2) ∘ (1 2) ∘ π = π e F(G(σ)) = σ, perché (1 2) ∘ (1 2) = id. Le due versioni danno funzioni diverse, perché la composizione non è commutativa: in S₃, con π = (1 2 3), si ha π ∘ (1 2) = (1 3) ma (1 2) ∘ π = (2 3). Sono però biettive tutte e due, e per contare basta una qualsiasi delle due.

@@ dopo cap47.22
**Un'altra dimostrazione (lezione 2026).** A lezione la stessa proposizione è stata dimostrata senza passare dai valori assoluti. Sia n primo e sia n = a · b.
1. Come sopra, n | a · b, quindi n | a oppure n | b; si supponga n | a.
2. Allora a = k · n per un certo k ∈ ℤ.
3. Sostituendo, n = a · b = k · n · b = (k · b) · n.
4. Poiché n ≠ 0 (nella definizione di primo n ∉ {0, 1, −1}), si può semplificare n e si ottiene 1 = k · b.
5. Un prodotto di due interi vale 1 solo se i due fattori sono entrambi 1 o entrambi −1, perché gli unici invertibili di ℤ sono ±1 (cap. 44). Quindi b = ±1. ∎

Il punto delicato è il passo 4: da n = (k · b) · n si ricava 1 = k · b solo perché n ≠ 0. Con n = 0 il passo non funzionerebbe: il conto direbbe 0 = 0 e non darebbe nessuna informazione.

@@ dopo cap51.20
**Esempio (lezione 2026).** A lezione compare l'equazione 12x + 9y = c: MCD(12, 9) = 3, quindi ci sono soluzioni se e solo se 3 | c. Per esempio (esempi nostri): con c = 6 le soluzioni ci sono, per esempio x = 2, y = −2 (infatti 24 − 18 = 6); con c = 4 non ce ne sono, perché 12x + 9y è sempre un multiplo di 3 e 4 non lo è.

**Esempio (lezione 2026).** Si risolve 6x + 10y = 8. Qui d = MCD(6, 10) = 2 e 2 | 8, con z = 8/2 = 4, quindi le soluzioni ci sono. Prima si risolve l'equazione con il MCD a destra, 6x + 10y = 2. L'identità di Bézout si trova con l'algoritmo di Euclide (10 = 6 · 1 + 4, 6 = 4 · 1 + 2, 4 = 2 · 2 + 0), risalendo: 2 = 6 − 4 = 6 − (10 − 6) = 6 · 2 − 10. Quindi x = 2, y = −1 risolve 6x + 10y = 2, e infatti 12 − 10 = 2. Moltiplicando per 4:

6 · (4 · 2) + 10 · (4 · (−1)) = 4 · 2, cioè 6 · 8 + 10 · (−4) = 8.

Una soluzione è x_{0} = 8, y_{0} = −4. Controllo: 48 − 40 = 8.

@@ dopo cap53.20
**La stessa dimostrazione per induzione forte (lezione 2026).** A lezione la dimostrazione procede per induzione, supponendo vera la proprietà per tutti i numeri più piccoli (**induzione forte**), e non solo per il numero precedente. Sia n > 1.
1. Se n è irriducibile, allora è primo (cap. 52) ed è già fattorizzato, con un solo fattore: n = p_{1}. È il caso del più piccolo numero da considerare, n = 2, ma anche di 3, 5, 7, ….
2. Ipotesi induttiva: ogni m con 1 < m < n si fattorizza in primi.
3. Se n non è irriducibile, allora n = a · b con 1 < a < n e 1 < b < n, con lo stesso conto del passo 4 della dimostrazione precedente.
4. Per l'ipotesi induttiva a = p_{1} · … · p_{r} e b = q_{1} · … · q_{s}, quindi n = a · b = p_{1} · … · p_{r} · q_{1} · … · q_{s} si fattorizza. ∎

L'induzione forte non è il principio di induzione del cap. 5 così com'è, ma si giustifica con il minimo controesempio usato sopra: se la proprietà fallisse per qualche n, ci sarebbe un minimo n in cui fallisce; per tutti i numeri più piccoli varrebbe, e i passi 1-4 di questa dimostrazione la farebbero valere anche per n. Le due dimostrazioni sono quindi la stessa, scritta in due modi.

@@ dopo cap53.41
**Esempio (lezione 2026).** Alla lavagna il docente prende due insiemi di primi. Con S = {2, 3, 5} si ha N = 2 · 3 · 5 + 1 = 31, che è primo. Con S = {2, 5, 11} si ha N = 2 · 5 · 11 + 1 = 111 = 3 · 37, che non è primo; ma 3 e 37 non stanno in S, ed è proprio quello che dice la dimostrazione.

**La dimostrazione vista a lezione (lezione 2026).** A lezione il teorema è stato dimostrato senza supporre all'inizio che i primi siano finiti. Si prende un **qualsiasi** insieme finito di primi positivi S = {p_{1}, …, p_{k}}, non per forza i primi k, e si fa vedere che esiste un primo fuori da S.
1. Si considera N = p_{1} · … · p_{k} + 1, che è maggiore di 1.
2. Per il teorema fondamentale dell'aritmetica (esistenza), esiste un primo positivo p con p | N.
3. Se fosse p = p_{i} per qualche i, p dividerebbe sia N sia il prodotto p_{1} · … · p_{k}, quindi anche la differenza N − p_{1} · … · p_{k} = 1 (cap. 44): p | 1, assurdo.
4. Quindi p ∉ S. ∎

Nessun insieme finito di primi li contiene tutti, cioè i primi sono infiniti. In questa versione l'assurdo serve solo al passo 3, per escludere p = p_{i}. Le due dimostrazioni sono equivalenti: quella sopra applica lo stesso ragionamento all'insieme di «tutti» i primi, supposto finito.
