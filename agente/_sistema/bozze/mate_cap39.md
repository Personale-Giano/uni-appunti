# 39. Gli Scambi: Scrivere Ogni Permutazione con Mosse Elementari
## Un gioco da mille dollari
Finora le permutazioni sono state scritte con i cicli disgiunti. Ma ci sono proprietà che i cicli non mostrano, e che appaiono solo guardando le permutazioni da un altro punto di vista.

Il docente lo introduce con il **gioco del 15**, un antenato del cubo di Rubik: un quadrato di plastica con tessere numerate da 1 a 15 e un posto vuoto, che permette di farle scorrere. Racconta che intorno al 1880, negli Stati Uniti, il gioco diventò una mania perché un giornale promise mille dollari, una cifra notevole per l'epoca, a chi fosse riuscito a tornare alla posizione iniziale partendo dalla configurazione con tutti i numeri in ordine e gli ultimi due scambiati: 1, 2, …, 13, 15, 14. Nessuno incassò il premio, perché si è dimostrato che è impossibile.

Muovere le tessere vuol dire permutare i numeri, quindi l'impossibilità viene da una proprietà delle permutazioni che non è ancora stata vista. Per arrivarci servono gli scambi.

## Gli scambi
**Definizione.** Uno **scambio** è un ciclo di lunghezza 2, cioè una permutazione (a b) che manda a in b, b in a e lascia fermo tutto il resto.

(In parole povere: si prendono due elementi e si fa cambiare loro di posto. È la mossa più semplice che si possa fare su un mazzo di carte.)

Se s è uno scambio, allora **s² = id**: scambiando due volte gli stessi elementi tutto torna a posto. Inoltre (a b) e (b a) sono lo stesso scambio.

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
