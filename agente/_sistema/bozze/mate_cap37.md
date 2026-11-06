# 37. Il Periodo di un Ciclo e di una Permutazione
## Il problema: trovare il periodo senza calcolare tutte le potenze
Nel cap. 36 si è visto che la successione delle potenze di una permutazione π è periodica: id, π, π², …, π^{p−1} sono tutte diverse e π^{p} = id, dove p è il periodo. Questo è già utile. Se per esempio π ha periodo 7 e serve π^{1000}, non occorre comporre mille volte: basta il resto della divisione di 1000 per 7, che è 6, perché 1000 = 7 · 142 + 6 e quindi π^{1000} = π⁶. Il legame con il resto della divisione sarà ripreso con l'aritmetica modulare.

Resta aperta la domanda: **data π, come si calcola il periodo senza mettersi a calcolare π², π³, … fino a trovare l'identità?** La risposta usa in modo essenziale la scomposizione in cicli disgiunti, e arriva in due passi: prima il periodo di un ciclo, poi quello di una permutazione qualsiasi.

## Il periodo di un ciclo
Si comincia dai casi piccoli. Per un ciclo di lunghezza 2, c = (1 2), il quadrato scambia due volte gli stessi elementi, quindi c² = id e il periodo è 2. Per un ciclo di lunghezza 3, c = (1 2 3), si calcola c² = (1 3 2), che non è l'identità: usa gli stessi tre elementi, ma è un ciclo diverso. Poi c³ = (1 3 2) ∘ (1 2 3) = id, quindi il periodo è 3. Il sospetto è che il periodo sia proprio la lunghezza.

**Proposizione.** Un ciclo di lunghezza ℓ ha periodo ℓ.

(In parole povere: un ciclo è una manopola con ℓ posizioni. Ogni volta che lo si applica, la manopola scatta di una posizione. Per riportare tutto com'era bisogna fare un giro completo, cioè ℓ scatti.)

**Dimostrazione.** Si può chiamare il ciclo c = (1 2 … ℓ) e immaginare i numeri disposti in cerchio, come su un orologio. Applicare c vuol dire far ruotare tutto di uno scatto: 1 va in 2, 2 va in 3, …, ℓ − 1 va in ℓ, ℓ torna in 1. Applicarlo due volte vuol dire far fare due scatti, e così via. Dopo ℓ scatti ogni numero è tornato al suo posto, quindi c^{ℓ} = id. Se invece k < ℓ, dopo k scatti il numero 1 si trova in k + 1, che è diverso da 1: il giro non è completo, quindi c^{k} ≠ id. Dunque ℓ è il più piccolo esponente positivo che dà l'identità.

Poiché la successione delle potenze è periodica, c^{k} = id esattamente quando k è un **multiplo di ℓ**: si ottiene l'identità a ℓ, 2ℓ, 3ℓ, … e solo lì.

## Due cicli disgiunti: la potenza si distribuisce
Sia ora π = c₁ ∘ c₂ con c₁ e c₂ cicli disgiunti, di lunghezze ℓ₁ e ℓ₂. Il punto chiave è che **i cicli disgiunti commutano** (cap. 33). Per il quadrato, usando anche l'associatività:

π² = (c₁ ∘ c₂) ∘ (c₁ ∘ c₂) = c₁ ∘ (c₂ ∘ c₁) ∘ c₂ = c₁ ∘ (c₁ ∘ c₂) ∘ c₂ = c₁² ∘ c₂².

È lo stesso passaggio che si fa con i numeri, (xy)² = x²y²: lì non ci si pensa più, ma funziona perché il prodotto di numeri è commutativo. Qui la composizione in generale non commuta, e vale solo perché i due cicli sono disgiunti. Ripetendo il trucco, ogni volta che un c₁ è fuori posto lo si scambia con il c₂ che lo precede, finché tutti i c₁ stanno a sinistra e tutti i c₂ a destra. Quindi, per ogni k > 0:

**π^{k} = c₁^{k} ∘ c₂^{k}.**

Per induzione: se vale per k, allora π^{k+1} = π^{k} ∘ π = c₁^{k} ∘ c₂^{k} ∘ c₁ ∘ c₂ = c₁^{k+1} ∘ c₂^{k+1}, perché c₂^{k} e c₁ commutano.

## Dalle potenze al periodo
Sia p il periodo di π, quindi c₁^{p} ∘ c₂^{p} = id. Una potenza di un ciclo muove solo elementi di quel ciclo, e li manda in elementi dello stesso ciclo. Le due potenze spostano quindi elementi diversi, perché c₁ e c₂ sono disgiunti: ciò che viene spostato dall'una è lasciato fermo dall'altra, e nessuna delle due può rimettere a posto quello che l'altra ha spostato. L'unica possibilità è che siano **entrambe** l'identità: c₁^{p} = id e c₂^{p} = id.

Per quanto visto sui cicli, questo vuol dire che p è multiplo sia di ℓ₁ sia di ℓ₂. Viceversa, ogni multiplo comune di ℓ₁ e ℓ₂ dà l'identità. Il periodo è il più piccolo esponente positivo con questa proprietà, quindi è il **minimo comune multiplo** di ℓ₁ e ℓ₂.

Con più cicli il meccanismo è lo stesso: i cicli sono a due a due disgiunti, quindi commutano e la potenza si distribuisce su tutti.

**Teorema (periodo di una permutazione).** Se π ≠ id e π = c₁ ∘ … ∘ c_{r} è la scomposizione in cicli disgiunti (cap. 34), con lunghezze ℓ₁, …, ℓ_{r}, allora π^{m} = c₁^{m} ∘ … ∘ c_{r}^{m} per ogni m > 0, e il periodo di π è il minimo comune multiplo mcm(ℓ₁, …, ℓ_{r}). L'identità ha periodo 1.

(In parole povere: ogni ciclo gira per conto suo, con il suo ritmo. Tutto torna a posto la prima volta che tutti i cicli hanno completato un numero intero di giri, come due lancette che si ritrovano allineate.)

Il risultato mette insieme tre cose: il teorema di scomposizione in cicli disgiunti, il fatto che i cicli disgiunti commutano e il periodo dei cicli. Poiché la scomposizione è unica a meno dell'ordine, le lunghezze sono determinate da π. Inoltre nell'enunciato compaiono solo le lunghezze, non i numeri scritti dentro i cicli: **il periodo di una permutazione dipende solo dal suo tipo**.

## Due esempi
In pratica il calcolo è meccanico, purché il primo passo sia sempre lo stesso: **estrarre i cicli disgiunti**. Sui cicli che non sono disgiunti il teorema non si può applicare: in generale non commutano e salta tutto il discorso.

**Esempio.** Sia π = (2 6 5 1) ∘ (1 4 3 6). I due cicli hanno elementi in comune, quindi non si possono usare direttamente le loro lunghezze. Componendo da destra a sinistra: 1 va in 4, 4 va in 3, 3 va in 5 (passando per 6), 5 torna in 1. Poi 2 va in 6, 6 torna in 2 (passando per 1). Dunque π = (1 4 3 5) ∘ (2 6), di tipo (4, 2), e il periodo è mcm(4, 2) = **4**.

**Esempio.** Sia π = (1 6 3 7 4) ∘ (3 2 5 1). Sarebbe sbagliato dire che il periodo è 5 · 4 = 20: l'1 e il 3 stanno in entrambi i cicli. Si estraggono i cicli disgiunti: 1 va in 7, 7 va in 4, 4 torna in 1. Poi 2 va in 5, 5 va in 6, 6 va in 3, 3 torna in 2. Dunque π = (1 7 4) ∘ (2 5 6 3), di tipo (4, 3), e il periodo è mcm(4, 3) = **12**. Con questo metodo non serve calcolare le prime dodici potenze.

Per esercitarsi, il consiglio del docente è di scrivere una permutazione a caso e calcolarne il periodo, una decina di volte: una volta capito che cosa fare, è un esercizio meccanico.
