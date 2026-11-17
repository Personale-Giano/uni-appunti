# 35. La Dimostrazione della Scomposizione in Cicli e Come Trovare il Tipo
## L'idea della dimostrazione
Si dimostra il teorema del capitolo precedente: ogni permutazione π ≠ id si scrive come composizione di cicli a due a due disgiunti. La dimostrazione è esattamente la generalizzazione del procedimento a «frecce» visto nel capitolo 33: si parte da un numero, si seguono le frecce e si osserva che il percorso si richiude.

**Passo 1: trovare un primo ciclo.** Si considera l'insieme T dei numeri che la permutazione **sposta effettivamente**:
T = { x ∈ {1, …, n} : π(x) ≠ x }.
Non si guardano i numeri lasciati fermi. Poiché π non è l'identità, c'è almeno un x con π(x) ≠ x, quindi **T non è vuoto**; inoltre è finito, perché è un sottoinsieme di {1, …, n}.

Si sceglie a piacere un elemento di T e lo si chiama t₁. Si segue il suo percorso: t₂ = π(t₁), t₃ = π(t₂), e così via. Si può andare avanti all'infinito incontrando sempre numeri nuovi? No: i numeri sono solo n, quindi a un certo punto si incontra un numero già incontrato prima; sia t_j il primo elemento che si ripete. Ora, dove si può richiudere il percorso? Se fosse j > 1, il numero t_j sarebbe immagine di due elementi diversi (il suo predecessore t_{j−1} e l'elemento che lo ha raggiunto la seconda volta, che è diverso da t_{j−1} perché t_j è il primo che si ripete), ma questo è impossibile perché **π è iniettiva**. Quindi il percorso si può richiudere solo nell'**unico elemento che finora non ha ricevuto nessuna freccia, cioè t₁**. Dunque a un certo punto la freccia torna a t₁, e si ottiene un ciclo C₁ = (t₁ t₂ … t_ℓ) «dentro» π. Il passaggio usa in modo essenziale che π sia iniettiva.

**Passo 2: gli altri cicli.** Dall'insieme T si tolgono tutti gli elementi del ciclo trovato, ottenendo T \ {t₁, …, t_ℓ}. Possono succedere due cose.
- Se questo insieme è **vuoto**, gli unici elementi spostati da π sono quelli di C₁, quindi **π = C₁** e il teorema è dimostrato.
- Se **non è vuoto**, si sceglie un elemento s₁ di quell'insieme e si ripete lo stesso discorso: si segue s₁, π(s₁) = s₂, π(s₂) = s₃, … e il percorso si richiude su s₁, dando un secondo ciclo C₂.

**Il secondo ciclo è disgiunto dal primo.** Sia s_j il primo elemento del percorso che cade in C₁ (j > 1, perché s₁ è stato scelto fuori da C₁) e sia s_j = t_i. Allora s_{j−1} non sta in C₁, mentre t_{i−1} sta in C₁ (con t₀ := t_ℓ): sono due elementi diversi con la stessa immagine, e questo è impossibile per l'iniettività.

**Passo 3: il procedimento finisce.** Si toglie anche C₂ e si riprende: se l'insieme resta non vuoto, si trova un terzo ciclo C₃, e così via. Perché si arriva alla fine? Si ponga T₁ = T \ {t₁, …, t_ℓ}, poi T₂ = T₁ \ {s₁, s₂, …}, e così via. Il numero di elementi dell'insieme ancora da considerare **diminuisce davvero a ogni passo**: |T| > |T₁| > |T₂| > …, e un numero naturale non può decrescere per sempre. Dopo un numero finito di passi l'insieme diventa vuoto, e a quel punto ogni elemento di T sta in uno e un solo ciclo costruito, e i cicli sono a due a due disgiunti. Quindi la loro composizione manda ogni x ∈ T in π(x) e lascia fermi gli altri numeri, cioè coincide con π. ∎

Questa dimostrazione costruisce la scrittura, cioè prova l'**esistenza**; l'unicità è dimostrata subito sotto.

(In parole povere: si prende un numero spostato e si segue il suo giro fino a chiuderlo; poi se ne prende uno fuori da quel giro e si fa lo stesso, e così via finché non restano più numeri spostati.)

## L'unicità
Resta da dimostrare che la scrittura è «essenzialmente unica» (cap. 34): i cicli che compaiono sono sempre gli stessi, e può cambiare soltanto l'ordine in cui sono scritti. Negli appunti del docente il teorema è enunciato proprio così: ogni permutazione si scrive **in modo unico, a meno dell'ordine**, come **prodotto di cicli disgiunti** (il docente dice «prodotto» per la composizione e «decomposizione» per la scomposizione). Negli appunti la dimostrazione dell'unicità è data solo per cenni: l'idea è quella del passo 4 qui sotto, e gli altri passaggi sono stati completati per renderla leggibile.

Nel cap. 34 la scomposizione è scritta C_{k} ∘ … ∘ C₁, qui C₁ ∘ … ∘ C_{k}: è la stessa cosa, perché i cicli disgiunti commutano e l'ordine in cui si scrivono non conta.

**Un'osservazione che serve.** Sia π = C₁ ∘ … ∘ C_{k} una scrittura in cicli a due a due disgiunti e sia a un elemento del ciclo C₁. Allora **π(a) = C₁(a)**: l'immagine di a secondo π è l'elemento che segue a dentro il suo ciclo. Infatti gli altri cicli non contengono a, quindi lo lasciano fermo; e non contengono nemmeno C₁(a), che è un altro elemento di C₁, quindi lasciano fermo anche quello. L'unico ciclo che agisce davvero su a è C₁. Lo stesso ragionamento vale per un elemento di qualunque altro ciclo della scrittura.

**Dimostrazione.** Si ragiona per assurdo. Si supponga che π abbia due scritture diverse in cicli disgiunti,

π = C₁ ∘ … ∘ C_{k} = C'₁ ∘ … ∘ C'_{h},

dove diverse vuol dire che non contengono gli stessi cicli. «Stesso ciclo» va inteso come stessa permutazione, a prescindere dal punto di partenza della scrittura: (3 11 10) e (11 10 3) sono lo stesso ciclo (cap. 34).
1. Gli elementi che compaiono nei cicli sono gli stessi nelle due scritture: sono esattamente i numeri spostati da π. Infatti un ciclo ha lunghezza almeno 2 (cap. 34), quindi manda ogni suo elemento in un elemento diverso, e per l'osservazione π fa lo stesso; i numeri che non stanno in nessun ciclo, invece, restano fermi. Quindi ogni elemento di un ciclo della prima scrittura sta anche in un ciclo della seconda, e viceversa.
2. Poiché le due scritture non contengono gli stessi cicli, in una delle due c'è un ciclo che nell'altra manca. Riordinando i cicli e, se serve, scambiando i nomi delle due scritture, si può supporre che sia C₁. Si prende un suo elemento e si chiama C'₁ il ciclo della seconda scrittura che lo contiene: C₁ e C'₁ sono **cicli diversi con un elemento in comune**.
3. Si percorrono i due cicli partendo dall'elemento comune. Se a ogni passo il successivo fosse lo stesso in entrambi, i due giri sarebbero identici e i due cicli coinciderebbero. Quindi c'è un elemento comune a dopo il quale i due cicli si separano: C₁ = (… a b …) e C'₁ = (… a b' …), con b ≠ b'.
4. Per l'osservazione, applicata alla prima scrittura, π(a) = C₁(a) = b. Applicata alla seconda, π(a) = C'₁(a) = b'. Ma π è una funzione e a ha una sola immagine: b = b', contro b ≠ b'.

L'assurdo mostra che due scritture diverse non possono esistere. ∎

(In parole povere: il ciclo in cui si trova un numero a non si può scegliere, perché è il percorso a, π(a), π(π(a)), … ed è deciso da π. Due scritture in cicli disgiunti devono quindi contenere gli stessi giri.)

**Esempio.** Nella permutazione di 12 elementi del prossimo paragrafo si ha π(3) = 11, π(11) = 10 e π(10) = 3. In qualunque scrittura in cicli disgiunti, il ciclo che contiene 3 deve mandare 3 in 11, 11 in 10 e 10 in 3: è per forza (3 11 10), comunque si sia arrivati alla scrittura.

## Un esempio con 12 elementi
Sia π la permutazione di {1, …, 12} (scritta a caso) definita da: π(1) = 7, π(2) = 9, π(3) = 11, π(4) = 1, π(5) = 6, π(6) = 2, π(7) = 5, π(8) = 4, π(9) = 12, π(10) = 3, π(11) = 10, π(12) = 8.

Si parte da 1 (uno qualsiasi va bene) e si seguono le frecce: 1 va in 7, 7 va in 5, 5 va in 6, 6 va in 2, 2 va in 9, 9 va in 12, 12 va in 8, 8 va in 4, 4 torna in 1. Primo ciclo: **(1 7 5 6 2 9 12 8 4)**, di lunghezza 9.

Si tolgono questi numeri: restano 3, 10, 11. Si parte da 3: 3 va in 11, 11 va in 10, 10 torna in 3. Secondo ciclo: **(3 11 10)**, di lunghezza 3.

Non resta niente da considerare, quindi π è la composizione di questi due cicli disgiunti, e ha **tipo (9, 3)**.

## Come si trova il tipo
Come si determina il tipo, quando la permutazione è data come composizione di cicli che non sono disgiunti? Il procedimento con la tabella (una riga per ogni ciclo, poi si cancellano le righe intermedie tenendo la prima e l'ultima) funziona sempre ma è lungo. C'è una **scorciatoia**, che richiede un po' di pratica: non si scrive nessuna tabella, ma si segue direttamente un numero attraverso tutte le funzioni, **da destra a sinistra**, perché si stanno componendo funzioni: si applica prima la funzione più a destra, poi quella alla sua sinistra, e così via. Si ottiene l'immagine di un numero, poi si riparte da quell'immagine per seguire il ciclo, finché non si richiude; poi si passa a un numero non ancora toccato.

**Esempio** (calcolato apposta per mostrare il metodo). Sia π = (1 2 3) ∘ (3 4 5) ∘ (1 5) in S₅: si applica prima (1 5), poi (3 4 5), poi (1 2 3).
- 1 → 5 (con (1 5)) → 3 (con (3 4 5)) → 1 (con (1 2 3)): π(1) = 1.
- 2 → 2 → 2 → 3: π(2) = 3.
- 3 → 3 → 4 → 4: π(3) = 4.
- 4 → 4 → 5 → 5: π(4) = 5.
- 5 → 1 → 1 → 2: π(5) = 2.

Quindi π = (2 3 4 5): un solo ciclo di lunghezza 4, con 1 fisso. Il tipo è **(4)**, anche se i cicli di partenza erano due di lunghezza 3 e uno di lunghezza 2 (e non erano disgiunti).

**Un altro esempio** (anche questo calcolato apposta). (1 3) ∘ (1 2 3): 1 → 2 → 2; 2 → 3 → 1; 3 → 1 → 3. Il risultato è (1 2): una composizione di un 3-ciclo e di un 2-ciclo che dà un 2-ciclo.

Come sottolineato a lezione, la situazione è molto «caotica»: si parte da cicli di certe lunghezze e si finisce con cicli di lunghezze del tutto diverse, e non c'è altro modo di trovare il tipo che fare il calcolo. Il tipo si legge sempre dalla scrittura in cicli **disgiunti**, non da quella di partenza. Nell'esempio fatto a lezione si partiva da tre cicli e si finiva con un ciclo di lunghezza 4 e uno di lunghezza 3, quindi con tipo (4, 3).

Anche nel calcolo conviene verificare sempre il risultato, perché è facile sbagliare.

Il capitolo successivo si chiede che cosa succede ripetendo più volte una stessa permutazione.
