# 66. Prodotti Scalari Definiti da Matrici Simmetriche
## Da dove vengono gli altri prodotti scalari
Come anticipato dal docente (registrazione 2025), la domanda ora è: come sono fatti gli altri prodotti scalari, anche solo su ℝⁿ? La risposta: si costruiscono con le **matrici simmetriche**. È lo stesso schema già visto per le applicazioni lineari: una matrice quadrata A determina l'endomorfismo L_{A} di 𝕂ⁿ (cap. 46); allo stesso modo una matrice simmetrica S determinerà un prodotto scalare su ℝⁿ.

Si ricorda (cap. 21) che una matrice quadrata A ∈ M(n) è **simmetrica** se a_{ij} = a_{ji} per ogni i, j, cioè se è uguale alla sua trasposta: ᵗA = A (cap. 27). L'insieme delle matrici simmetriche n × n si indica con S(n). Per esempio ( 1 2 ; 2 3 ) e ( 2 1 ; 1 1 ) sono in S(2), mentre ( 1 2 ; 0 3 ) non è simmetrica. Servirà anche la regola della trasposta di un prodotto (cap. 30): ᵗ(AB) = ᵗB · ᵗA.

## Il prodotto scalare associato a una matrice simmetrica
**Definizione.** Sia S ∈ S(n) una matrice simmetrica. Si definisce la funzione g_{S} : ℝⁿ × ℝⁿ → ℝ ponendo

g_{S}(v, w) = ᵗv · S · w.

(In parole povere: è il prodotto euclideo ᵗv · w con una matrice S «infilata in mezzo». La matrice S fa da ricetta: dice con che peso combinare le coordinate dei due vettori.)

Il docente fa notare la somiglianza con il prodotto euclideo e controlla che le dimensioni tornino (registrazione 2025): ᵗv è una matrice 1 × n, S è n × n, w è n × 1. Il primo prodotto si può fare (n colonne contro n righe) e dà una matrice 1 × n; il secondo dà una matrice 1 × 1, cioè un numero.

Il docente scrive anche un'osservazione che apre una serie di paralleli con la teoria degli endomorfismi: la corrispondenza **S ↦ g_{S}** è l'analogo della corrispondenza **A ↦ L_{A}**. Il quadro completo dei paralleli è alla fine del cap. 67.

## È davvero un prodotto scalare
**Proposizione (Prop. 19.7).** Per ogni S ∈ S(n), la funzione g_{S} è un prodotto scalare su ℝⁿ.

**Dimostrazione (alla lavagna, registrazione 2025).** Le proprietà 1 e 2 si dimostrano esattamente come per il prodotto euclideo (cap. 65), perché dipendono solo dalle proprietà del prodotto fra matrici. Per esempio

g_{S}(v_{1} + v_{2}, w) = ᵗ(v_{1} + v_{2}) S w = (ᵗv_{1} + ᵗv_{2}) S w = ᵗv_{1} S w + ᵗv_{2} S w = g_{S}(v_{1}, w) + g_{S}(v_{2}, w),

e analogamente g_{S}(λv, w) = (λ ᵗv) S w = λ (ᵗv S w) = λ g_{S}(v, w).

Resta la proprietà 3, la simmetria, ed è l'unico punto in cui serve che S sia simmetrica. I passaggi sono:
1. g_{S}(v, w) = ᵗv S w, per definizione;
2. ᵗv S w = ᵗ(ᵗv S w), perché ᵗv S w è una matrice 1 × 1 e trasporre una matrice con una sola riga e una sola colonna non cambia nulla;
3. ᵗ(ᵗv S w) = ᵗw · ᵗS · ᵗ(ᵗv), per la regola della trasposta di un prodotto applicata a tre fattori: si traspongono tutti e si inverte l'ordine;
4. ᵗw · ᵗS · ᵗ(ᵗv) = ᵗw · S · v, perché la trasposta della trasposta è la matrice di partenza e perché **S è simmetrica**, cioè ᵗS = S;
5. ᵗw S v = g_{S}(w, v), per definizione.

Quindi g_{S}(v, w) = g_{S}(w, v).

Si noti il ruolo della simmetria di S: con una matrice qualsiasi A la funzione ᵗv A w sarebbe ancora lineare in entrambe le variabili, ma in generale non simmetrica. Per esempio con A = ( 0 1 ; 0 0 ) si ha ᵗe_{1} A e_{2} = 1 ma ᵗe_{2} A e_{1} = 0 (esempio aggiunto per chiarezza).

## Un esempio con S = ( 1 2 ; 2 3 )
**Esempio dalla lavagna (registrazione 2025).** Sia S = ( 1 2 ; 2 3 ) ∈ S(2). Si calcola g_{S}((1, 1), (2, 3)). Poiché il prodotto fra matrici è associativo, si può cominciare da dove si vuole; il docente comincia da S·w:

S · (2, 3) = (1·2 + 2·3, 2·2 + 3·3) = (8, 13),

e poi

g_{S}((1, 1), (2, 3)) = (1 1) · (8, 13) = 8 + 13 = 21.

Dopo la pausa il docente rifà il conto con due vettori **generici** v = (x_{1}, x_{2}) e w = (y_{1}, y_{2}):

g_{S}(v, w) = (x_{1} x_{2}) · ( 1 2 ; 2 3 ) · (y_{1}, y_{2}) = (x_{1} x_{2}) · (y_{1} + 2y_{2}, 2y_{1} + 3y_{2}),

e sviluppando con la distributività

g_{S}(v, w) = x_{1}y_{1} + 2x_{1}y_{2} + 2x_{2}y_{1} + 3x_{2}y_{2}.

Con questa formula il conto di prima si rifà subito: per x = (1, 1) e y = (2, 3) si trova 2 + 6 + 4 + 9 = 21.

Alla lavagna il docente cerchia con colori diversi i numeri 1, 2, 2, 3 nella matrice e nel risultato, per far vedere che **i coefficienti sono esattamente le entrate di S**: l'entrata in riga 1 e colonna 1 (cioè 1) è il coefficiente di x_{1}y_{1}; quella in riga 1 e colonna 2 (cioè 2) è il coefficiente di x_{1}y_{2}; quella in riga 2 e colonna 1 (ancora 2) è il coefficiente di x_{2}y_{1}; quella in riga 2 e colonna 2 (cioè 3) è il coefficiente di x_{2}y_{2}.

## La formula generale
**Proposizione (Prop. 19.8).** Se S ∈ S(n) ha entrate a_{ij} (alla lavagna; S_{ij} nelle dispense), allora

g_{S}((x_{1}, …, x_{n}), (y_{1}, …, y_{n})) = Σ_{i=1}^{n} Σ_{j=1}^{n} a_{ij} x_{i} y_{j}.

**Dimostrazione (dalle dispense).** La i-esima coordinata del vettore S·w è (S w)_{i} = Σ_{j=1}^{n} a_{ij} y_{j} (riga i di S per la colonna w). Quindi ᵗv S w = Σ_{i=1}^{n} x_{i} (S w)_{i} = Σ_{i=1}^{n} Σ_{j=1}^{n} x_{i} a_{ij} y_{j}.

In pratica, dice il docente (registrazione 2025), si scrivono tutti i termini della forma x_{i}y_{j}, con i e j che prendono tutti i valori da 1 a n, ciascuno moltiplicato per l'entrata che sta nella riga i e nella colonna j di S, e si somma tutto: è come un doppio ciclo «for i da 1 a n, for j da 1 a n». Per n = 2 i termini sono quattro, come nell'esempio; per n = 3 sono nove.

La formula si legge anche al contrario (osservazione aggiunta): un'espressione del tipo Σ a_{ij} x_{i} y_{j} con a_{ij} = a_{ji} è il prodotto scalare g_{S} della matrice simmetrica che ha quei coefficienti. Per esempio g(x, y) = 2x_{1}y_{1} + x_{1}y_{2} + x_{2}y_{1} + x_{2}y_{2} è g_{S} con S = ( 2 1 ; 1 1 ) (Esempio 19.11 delle dispense): il coefficiente 1 di x_{1}y_{2} va in riga 1 e colonna 2, quello di x_{2}y_{1} in riga 2 e colonna 1. Attenzione (aggiunta per chiarezza): se un'espressione ha un termine come 4x_{1}y_{2} ma nessun termine in x_{2}y_{1}, i coefficienti non sono simmetrici e non si tratta di un prodotto scalare.

## Due casi particolari
**Corollario (Cor. 19.9).** Per i vettori della base canonica vale g_{S}(e_{i}, e_{j}) = a_{ij}, l'entrata di S in riga i e colonna j.

Infatti e_{i} ha 1 in posizione i e 0 altrove, ed e_{j} ha 1 in posizione j: nella somma Σ a_{kl} x_{k} y_{l} resta solo il termine con k = i e l = j. Per S = ( 1 2 ; 2 3 ), per esempio, g_{S}(e_{1}, e_{2}) = 2 e g_{S}(e_{2}, e_{2}) = 3. Alla lavagna (registrazione 2025) lo stesso conto è fatto con i prodotti di matrici, nel cap. 67.

**Osservazione (alla lavagna ed Esempio 19.10).** Se S = I_{n} è l'identità, allora I_{n} · w = w e

g_{I_{n}}(v, w) = ᵗv I_{n} w = ᵗv · w = x_{1}y_{1} + … + x_{n}y_{n}.

Il prodotto scalare associato all'identità è il **prodotto scalare euclideo**. Nel parallelo con gli endomorfismi: come L_{I_{n}} è l'applicazione identica, g_{I_{n}} è il prodotto scalare «più semplice».

## Trabocchetto: non ogni matrice simmetrica dà un prodotto definito positivo
Per ogni matrice simmetrica S la funzione g_{S} è un prodotto scalare, ma **non è detto che sia definito positivo**. Alla lavagna l'esempio S = ( 1 2 ; 2 3 ) è correttamente chiamato «prodotto scalare» (nel corso un prodotto scalare è solo bilineare e simmetrico), ma alla lavagna non si osserva che non è definito positivo. Lo si vede con un conto (verifica non presente nelle dispense né in lezione): per v = (2, −1),

g_{S}(v, v) = 2² + 4·2·(−1) + 3·(−1)² = 4 − 8 + 3 = −1 < 0,

dove si è usata la formula g_{S}(v, v) = x_{1}² + 4x_{1}x_{2} + 3x_{2}², che si ottiene dalla formula generale ponendo y = x. Un vettore non nullo con «prodotto con se stesso» negativo: questo g_{S} non potrà servire a misurare lunghezze.

Invece la matrice delle dispense S = ( 2 1 ; 1 1 ) dà un prodotto scalare definito positivo (verifica aggiunta): g_{S}(v, v) = 2x_{1}² + 2x_{1}x_{2} + x_{2}² = x_{1}² + (x_{1} + x_{2})², che è una somma di quadrati, quindi ≥ 0, ed è zero solo se x_{1} = 0 e x_{1} + x_{2} = 0, cioè v = 0.

Come capire in generale quali matrici simmetriche danno prodotti definiti positivi è un problema delle lezioni successive (le dispense §20 lo collegano alle forme quadratiche). Per ora basta ricordare che la parola «prodotto scalare» da sola non garantisce la positività.

Il prossimo passo è il cammino inverso: dato un prodotto scalare qualsiasi su uno spazio V e una base, costruirne la matrice, come si faceva con la matrice associata a un'applicazione lineare.
