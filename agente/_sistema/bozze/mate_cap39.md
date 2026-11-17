# 39. Gli Scambi: Scrivere Ogni Permutazione con Mosse Elementari
## Un gioco da mille dollari
Finora le permutazioni sono state scritte con i cicli disgiunti. Ma ci sono proprietà che i cicli non mostrano, e che appaiono solo guardando le permutazioni da un altro punto di vista.

Il docente lo introduce con il **gioco del 15**, un antenato del cubo di Rubik: un quadrato di plastica con tessere numerate da 1 a 15 e un posto vuoto, che permette di farle scorrere. Racconta che intorno al 1880, negli Stati Uniti, il gioco diventò una mania perché un giornale promise mille dollari, una cifra notevole per l'epoca, a chi fosse riuscito a tornare alla posizione iniziale partendo dalla configurazione con tutti i numeri in ordine e gli ultimi due scambiati: 1, 2, …, 13, 15, 14. Nessuno incassò il premio, perché si è dimostrato che è impossibile.

Muovere le tessere vuol dire permutare i numeri, quindi l'impossibilità viene da una proprietà delle permutazioni che non è ancora stata vista. Per arrivarci servono gli scambi.

## Gli scambi
**Definizione.** Uno **scambio**, detto anche **trasposizione**, è un ciclo di lunghezza 2, cioè una permutazione (a b) che manda a in b, b in a e lascia fermo tutto il resto.

(In parole povere: si prendono due elementi e si fa cambiare loro di posto. È la mossa più semplice che si possa fare su un mazzo di carte.)

Se s è uno scambio, allora **s² = id**: scambiando due volte gli stessi elementi tutto torna a posto. Inoltre (a b) e (b a) sono lo stesso scambio.

I due nomi indicano lo stesso oggetto. Negli appunti del docente si trova quasi sempre **trasposizione**, e la composizione di più trasposizioni è chiamata **prodotto di trasposizioni**, scritto spesso senza il simbolo ∘: (1 3)(1 2) vuol dire (1 3) ∘ (1 2), sempre da leggere da destra a sinistra. In questi capitoli si continua a dire «scambio» e a scrivere ∘.

**Quante sono le trasposizioni.** Uno scambio è individuato dai due elementi che scambia, e l'ordine in cui li si scrive non conta, perché (a b) = (b a). Le trasposizioni di S_{n} sono quindi tante quanti i sottoinsiemi di 2 elementi di {1, …, n}, cioè il coefficiente binomiale (n su 2) = n!/(2! · (n − 2)!) = n(n − 1)/2 (cap. 26). Per esempio in S₄ sono (4 · 3)/2 = 6 e in S₅ sono (5 · 4)/2 = 10. È lo stesso numero che dà la formula del cap. 34 per i cicli di lunghezza 2: (1/2) · n!/(n − 2)! = n(n − 1)/2. Il confronto con il totale è istruttivo: le permutazioni di S_{n} sono n!, un numero che cresce rapidissimamente, mentre le trasposizioni crescono solo come un polinomio di secondo grado in n. In S₅ sono 10 su 120, eppure, come si vedrà fra poco, bastano per ottenere tutte le altre.

## Ogni ciclo si scrive con gli scambi
**Proposizione.** Ogni ciclo di lunghezza ℓ si scrive come composizione di ℓ − 1 scambi:

(1 2 … ℓ) = (ℓ−1 ℓ) ∘ … ∘ (3 ℓ) ∘ (2 ℓ) ∘ (1 ℓ).

Come sempre la composizione si legge da destra a sinistra: prima si scambia 1 con ℓ, poi 2 con ℓ, poi 3 con ℓ, e così via fino a ℓ − 1 con ℓ.

(In parole povere: un intero giro della manopola si ottiene anche con una serie di mosse elementari, tutte con lo stesso elemento ℓ.)

**Verifica.** Le due espressioni sono funzioni biettive sullo stesso insieme: per mostrare che sono uguali basta controllare che facciano la stessa cosa su ogni elemento.
Per ℓ = 2 il ciclo è già uno scambio; sia quindi ℓ ≥ 3.
- Il numero 1: il primo scambio lo manda in ℓ, il secondo manda ℓ in 2, e 2 non compare più. Quindi 1 va in 2.
- Un numero k con 1 < k < ℓ: non compare negli scambi prima di (k ℓ). Quello scambio lo manda in ℓ, il successivo (k+1 ℓ) manda ℓ in k + 1, e k + 1 non compare più. Quindi k va in k + 1; per k = ℓ − 1 l'ultimo scambio lo manda direttamente in ℓ.
- Il numero ℓ: il primo scambio lo manda in 1, e 1 non compare più. Quindi ℓ va in 1.

È proprio il ciclo di partenza. Il numero di scambi è ℓ − 1, perché ci sono 1, 2, …, ℓ − 1 accoppiati con ℓ.

**Esempio.** (1 2 3) = (2 3) ∘ (1 3): 1 va in 3 e poi in 2; 2 va in 3; 3 va in 1. I due scambi sono ℓ − 1 = 2.

## Un'altra scomposizione, con gli scambi sul primo elemento
Negli appunti del docente il ciclo è scomposto in un altro modo: l'elemento che compare in tutti gli scambi è il **primo** del ciclo, non l'ultimo. Per un ciclo qualsiasi (s₁ s₂ … s_{ℓ}) la formula è

(s₁ s₂ … s_{ℓ}) = (s₁ s_{ℓ}) ∘ … ∘ (s₁ s₄) ∘ (s₁ s₃) ∘ (s₁ s₂).

Si legge sempre da destra a sinistra: prima si scambia s₁ con s₂, poi s₁ con s₃, poi s₁ con s₄, e così via fino a s₁ con s_{ℓ}. Gli scambi sono ancora ℓ − 1, uno per ciascuno degli elementi s₂, …, s_{ℓ}.

Il controllo è lo stesso di prima, elemento per elemento. Il primo scambio manda s₁ in s₂, e s₂ non compare più: quindi s₁ va in s₂. Un elemento s_{i} con 1 < i < ℓ viene toccato per la prima volta da (s₁ s_{i}), che lo manda in s₁; subito dopo (s₁ s_{i+1}) manda s₁ in s_{i+1}, che non compare più: quindi s_{i} va in s_{i+1}. Infine s_{ℓ} compare solo nell'ultimo scambio, che lo manda in s₁. È il ciclo di partenza.

Questa formula e quella della proposizione **non sono due risultati diversi**: sono due scritture diverse dello stesso ciclo, con lo stesso numero di scambi. Nella prima l'elemento comune a tutti gli scambi è l'ultimo, nella seconda è il primo, e gli scambi che compaiono sono diversi.

**Esempio.** Per il ciclo (1 2 3 4) la proposizione dà (3 4) ∘ (2 4) ∘ (1 4), la formula del docente dà (1 4) ∘ (1 3) ∘ (1 2). Si controllano entrambe, da destra a sinistra.
- (3 4) ∘ (2 4) ∘ (1 4): 1 va in 4, poi 4 va in 2, e 2 resta fermo: 1 va in 2. Il 2 resta fermo, poi va in 4, poi 4 va in 3: 2 va in 3. Il 3 resta fermo due volte e poi va in 4: 3 va in 4. Il 4 va in 1 e poi resta fermo: 4 va in 1.
- (1 4) ∘ (1 3) ∘ (1 2): 1 va in 2 e poi resta fermo: 1 va in 2. Il 2 va in 1, poi 1 va in 3, e 3 resta fermo: 2 va in 3. Il 3 resta fermo, poi va in 1, poi 1 va in 4: 3 va in 4. Il 4 resta fermo due volte e poi va in 1: 4 va in 1.

In tutti e due i casi si ottiene 1 → 2 → 3 → 4 → 1, cioè (1 2 3 4), con tre scambi. Allo stesso modo, per il ciclo dell'esempio precedente, (1 2 3) = (2 3) ∘ (1 3) = (1 3) ∘ (1 2). Si vede già qui che uno stesso ciclo si scrive con gli scambi in più di un modo: è il secondo dei due problemi discussi più avanti.

## Ogni permutazione si scrive con gli scambi
Mettendo insieme i pezzi: ogni permutazione è composizione di cicli (cap. 34) e ogni ciclo è composizione di scambi. Quindi:

**Teorema.** Ogni permutazione si può scrivere come composizione di scambi.

(In parole povere: anche il mazzo di carte mescolato nel modo più furioso si può ottenere partendo dal mazzo iniziale e facendo cambiare posto a due carte alla volta, un numero sufficiente di volte.)

L'identità, che non ha cicli, rientra anch'essa se n ≥ 2: (1 2) ∘ (1 2) = id.

## Due problemi
È una scrittura molto semplice, perché usa soltanto un tipo di mossa. A differenza di quella in cicli disgiunti, però, ha due difetti.

**Gli scambi non sono disgiunti.** Nella formula per il ciclo, due scambi qualsiasi hanno sempre ℓ in comune, quindi in generale non commutano e non si può manipolare l'espressione spostando i termini.

**La scrittura non è unica.** Per esempio:

(2 3) = (1 3) ∘ (1 2) ∘ (1 3).

Controllo, leggendo da destra a sinistra: 2 resta fermo, poi va in 1, poi in 3; 3 va in 1, poi in 2, poi resta fermo; 1 va in 3 e poi torna in 1. Quindi 2 e 3 si scambiano e 1 resta fermo. Attenzione: non si possono cancellare i due (1 3), perché non commutano con (1 2). A sinistra c'è uno scambio, a destra ce ne sono tre, ed è la stessa permutazione.

Se un numero intero avesse due scomposizioni diverse in fattori primi salterebbero moltissimi risultati, e qui succede qualcosa di simile. Per questo il docente dice che gli scambi sono utili più dal punto di vista concettuale che pratico: confrontando due successioni di scambi, non si vede a occhio se danno la stessa permutazione.

Questo non significa che la scrittura con gli scambi vada abbandonata: sotto la non unicità c'è una struttura, ed è il tema del prossimo capitolo.
