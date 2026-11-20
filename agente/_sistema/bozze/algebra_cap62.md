# 62. Autospazi e Autovettori di Autovalori Distinti
## Dagli autovalori agli autovettori: l'autospazio
Il cap. 61 ha insegnato a trovare gli autovalori come radici del polinomio caratteristico. Il secondo passo è trovare, per ciascun autovalore λ, tutti i vettori v con T(v) = λv. Per il cap. 59, su ℝ o su ℂ, ce ne sono sempre infiniti (tutti i multipli non nulli di un autovettore), e conviene raccoglierli in un unico insieme.

**Definizione.** Sia T : V → V un endomorfismo e sia λ un autovalore di T. L'**autospazio** di λ è

V_{λ} = {v ∈ V | T(v) = λv} = {v ∈ V | (T − λI)(v) = 0} = Ker(T − λI),

dove I = I_{V} è l'identità di V.

(In parole povere: l'autospazio di λ è il «magazzino» di tutti gli autovettori con autovalore λ, a cui si aggiunge lo zero. Per ( 1 2 ; 2 1 ) l'autospazio di 3 è l'intera retta dei multipli di (1, 1).)

Le due scritture coincidono perché T(v) = λv equivale a T(v) − λv = 0, cioè (T − λI)(v) = 0. Alla lavagna (registrazione 2024) l'autospazio è scritto come insieme di **tutti** i v con Tv = λv, quindi contiene anche il vettore nullo; le dispense precisano che è l'insieme degli autovettori di autovalore λ «più l'origine», perché 0 non è un autovettore per definizione.

La seconda scrittura ha una conseguenza importante: T − λI è un'applicazione lineare (combinazione lineare di T e dell'identità) e il nucleo di un'applicazione lineare è sempre un sottospazio (cap. 47). Quindi **V_{λ} è un sottospazio vettoriale di V**, e ha senso parlare della sua dimensione e di una sua base. Per una matrice A ∈ M(n, 𝕂) si ha V_{λ} = Ker(A − λI_{n}), cioè lo spazio delle soluzioni del sistema omogeneo (A − λI_{n})x = 0, che si risolve con i metodi dei cap. 39-41 e che per il cap. 48 ha dimensione n − rk(A − λI_{n}).

## Un esempio completo: ( 2 1 ; 1 2 )
**Esempio dalla lavagna (registrazione 2024).** Sia A = ( 2 1 ; 1 2 ). Si vogliono autovalori, autovettori, e sapere se A è diagonalizzabile.

① Gli autovalori. Con la formula delle 2 × 2 (cap. 61), tr A = 4 e det A = 3, quindi p_{A}(t) = t^{2} − 4t + 3 = (t − 1)(t − 3). Gli autovalori sono 1 e 3.

② Gli autovettori di λ = 1. Un vettore v = (x, y) è autovettore con autovalore 1 se e solo se (A − 1·I_{2})v = 0, con A − I_{2} = ( 1 1 ; 1 1 ):

(0, 0) = ( 1 1 ; 1 1 ) · (x, y) = (x + y, x + y).

Le due equazioni sono uguali, e ne resta una sola: x + y = 0, cioè x = −y con y libero. Quindi

V_{1} = {(−y, y) | y ∈ 𝕂} = {y·(−1, 1) | y ∈ 𝕂} = Span((−1, 1)).

③ Gli autovettori di λ = 3. Si risolve (A − 3I_{2})v = 0, con A − 3I_{2} = ( −1 1 ; 1 −1 ):

(0, 0) = ( −1 1 ; 1 −1 ) · (x, y) = (−x + y, x − y),

cioè y = x con x libero, e

V_{3} = {(x, x) | x ∈ 𝕂} = {x·(1, 1) | x ∈ 𝕂} = Span((1, 1)).

④ La diagonalizzabilità. Alla lavagna il docente conclude: B = {(1, 1), (−1, 1)} è una **base di ℝ² fatta di autovettori** di A, quindi A è diagonalizzabile. I due vettori sono indipendenti perché det( 1 −1 ; 1 1 ) = 2 ≠ 0 (controllo aggiunto). Con le notazioni del cap. 60 (scritte qui per completezza, alla lavagna non compaiono), mettendo gli autovettori in colonna e gli autovalori nello stesso ordine:

P = ( 1 −1 ; 1 1 ),   D = ( 3 0 ; 0 1 ),   A = P D P^{−1}.

Infatti P^{−1} = (1/2)·( 1 1 ; −1 1 ) e P D P^{−1} = ( 3 −1 ; 3 1 ) · (1/2)·( 1 1 ; −1 1 ) = (1/2)·( 4 2 ; 2 4 ) = ( 2 1 ; 1 2 ).

![Gli autospazi di ( 2 1 ; 1 2 ): sulla retta V₃ ogni vettore viene triplicato, sulla retta V₁ resta fermo; un vettore fuori dalle due rette, come e₁, cambia direzione.](figure/alg/autospazi_2112.png|10)

Allo stesso modo per ( 1 2 ; 2 1 ) del cap. 59 (conto aggiunto per chiarezza): A − 3I_{2} = ( −2 2 ; 2 −2 ) dà y = x, e A + I_{2} = ( 2 2 ; 2 2 ) dà y = −x, quindi V_{3} = Span((1, 1)) e V_{−1} = Span((1, −1)). La base dell'oracolo non era magia: è fatta di un vettore per ciascun autospazio.

## Autovettori con autovalori distinti sono indipendenti
Nell'esempio, il fatto che (1, 1) e (−1, 1) fossero indipendenti si è controllato qui con un determinante. In realtà non c'era bisogno: autovettori di autovalori diversi sono sempre indipendenti.

**Proposizione.** Sia T : V → V un endomorfismo. Se v_{1}, …, v_{k} ∈ V sono autovettori di T con autovalori λ_{1}, …, λ_{k} **distinti**, allora v_{1}, …, v_{k} sono linearmente indipendenti.

(In parole povere: direzioni che vengono allungate di fattori diversi non possono «dipendere» l'una dall'altra. Per esempio nessuna combinazione di un vettore che si triplica può produrre un vettore che resta fermo.)

Alla lavagna (registrazione 2024) la proposizione è solo enunciata (con scritto, per una svista, «autovettori di A» invece che di T); la dimostrazione è quella delle dispense.

**Dimostrazione (dalle dispense).** Per induzione su k (cap. 13). Se k = 1, v_{1} è indipendente perché non è nullo: un autovettore non lo è mai, per definizione.

Si suppone vero il caso k − 1 e si dimostra il caso k. Sia α_{1}v_{1} + … + α_{k}v_{k} = 0 una combinazione lineare nulla; bisogna mostrare che tutti gli α_{i} sono 0.
1. Applicando T, per linearità e perché T(v_{i}) = λ_{i}v_{i}: α_{1}λ_{1}v_{1} + … + α_{k}λ_{k}v_{k} = T(0) = 0.
2. Moltiplicando invece la combinazione di partenza per λ_{k}: α_{1}λ_{k}v_{1} + … + α_{k}λ_{k}v_{k} = 0.
3. Sottraendo la seconda uguaglianza dalla prima, l'ultimo termine si cancella: α_{1}(λ_{1} − λ_{k})v_{1} + … + α_{k−1}(λ_{k−1} − λ_{k})v_{k−1} = 0.
4. Questa è una combinazione lineare nulla di k − 1 autovettori con autovalori distinti: per l'ipotesi induttiva tutti i coefficienti α_{i}(λ_{i} − λ_{k}) sono nulli. Poiché λ_{i} ≠ λ_{k} per i < k, ne segue α_{i} = 0 per ogni i = 1, …, k − 1.
5. La combinazione di partenza si riduce ad α_{k}v_{k} = 0, e poiché v_{k} ≠ 0 anche α_{k} = 0. ∎

**Corollario.** Sia T : V → V un endomorfismo, con dim V = n. Se T ha n autovalori distinti (cioè se p_{T}(t) ha n radici distinte in 𝕂), allora T è diagonalizzabile.

(In parole povere: se in dimensione n si trovano n autovalori tutti diversi, la diagonalizzabilità è garantita senza altri conti. Ogni autovalore regala una direzione, e le direzioni sono automaticamente indipendenti.)

**«Dimostrazione» (alla lavagna, registrazione 2024, tra virgolette).** Siano λ_{1}, …, λ_{n} gli autovalori e, per ciascuno, v_{i} un autovettore di autovalore λ_{i}. Per la proposizione {v_{1}, …, v_{n}} sono linearmente indipendenti; sono n vettori indipendenti in uno spazio di dimensione n, quindi sono una base (cap. 26), ed è una base di autovettori. ∎

Il docente torna sull'esempio di ( 2 1 ; 1 2 ): due autovalori distinti, 1 e 3, in dimensione 2, quindi il corollario dà subito la diagonalizzabilità, senza calcolare gli autovettori. Lo stesso vale per ( 1 2 ; 2 1 ) (autovalori 3 e −1) e per ( 3 4 ; 0 2 ) (autovalori 3 e 2, letti sulla diagonale).

**Attenzione.** Il corollario dà una condizione **sufficiente**, non necessaria. La matrice identità I_{2} ha un solo autovalore, 1 (p(t) = (1 − t)^{2}), eppure è diagonalizzabile: è già diagonale, e ogni base di ℝ² è fatta di autovettori. Quando gli autovalori distinti sono meno di n servono altri strumenti, che arrivano nel resto del capitolo e nel cap. 63. (Esempio aggiunto per chiarezza.)

## Somma di sottospazi e somma diretta
Per dire quando gli autovettori bastano a fare una base serve un linguaggio nuovo. Se W_{1}, …, W_{k} sono sottospazi di V, la loro **somma** è l'insieme dei vettori che si ottengono sommando un vettore per ciascuno:

W_{1} + … + W_{k} = {w_{1} + … + w_{k} | w_{i} ∈ W_{i}}.

Alla lavagna (registrazione 2024) questa scrittura compare dentro il corollario sugli autospazi più avanti; è un sottospazio di V, perché somme e multipli di vettori di questa forma sono ancora di questa forma.

(In parole povere: la somma di due sottospazi è tutto ciò che si ottiene prendendo un pezzo da ciascuno e sommando. Per esempio la somma di due rette diverse per l'origine nel piano è tutto il piano.)

**Definizione.** Siano W_{1}, …, W_{k} sottospazi di V. Si dice che sono in **somma diretta** se l'unico modo di scrivere il vettore nullo come

0 = w_{1} + w_{2} + … + w_{k},   con w_{i} ∈ W_{i},

è quello banale, w_{1} = w_{2} = … = w_{k} = 0. In questo caso la somma si scrive W_{1} ⊕ … ⊕ W_{k}.

(In parole povere: i sottospazi sono in somma diretta se non si «sovrappongono» in modo nascosto: nessun pezzo preso da uno può essere compensato da pezzi presi dagli altri fino a dare zero.)

Alla lavagna la definizione è data direttamente in questa forma. Le dispense (Definizione 18.4) partono da un'altra, equivalente: ogni vettore v ∈ W_{1} + … + W_{k} si scrive **in modo unico** come v = w_{1} + … + w_{k} con w_{i} ∈ W_{i}. Le due sono la stessa cosa, con un conto di una riga (non presente nelle dispense né in lezione): se v = w_{1} + … + w_{k} = w_{1}′ + … + w_{k}′ sono due scritture, sottraendo si ottiene 0 = (w_{1} − w_{1}′) + … + (w_{k} − w_{k}′) con w_{i} − w_{i}′ ∈ W_{i}, e questa scrittura di 0 è banale se e solo se le due scritture di v coincidono. Il simbolo ⊕ si usa nelle dispense; alla lavagna non compare.

**Esempio.** In ℝ² le due rette degli assi, W_{1} = Span(e_{1}) e W_{2} = Span(e_{2}), sono in somma diretta: a e_{1} + b e_{2} = (a, b) = 0 solo se a = b = 0, e ℝ² = W_{1} ⊕ W_{2}. In ℝ³ invece il piano W_{1} = {z = 0} e il piano W_{2} = {y = 0} non lo sono: si intersecano lungo l'asse x, e (1, 0, 0) + (−1, 0, 0) = 0 è una scrittura non banale dello zero, con il primo vettore in W_{1} e il secondo in W_{2}. (Esempi aggiunti per chiarezza.)

**Proposizione.** Se V = W_{1} ⊕ … ⊕ W_{k}, cioè i sottospazi sono in somma diretta e ogni v ∈ V si scrive come w_{1} + … + w_{k} con w_{i} ∈ W_{i}, e si scelgono basi B_{1} di W_{1}, …, B_{k} di W_{k}, allora B = B_{1} ∪ B_{2} ∪ … ∪ B_{k} è una base di V. In particolare dim V = dim W_{1} + … + dim W_{k}.

(In parole povere: se lo spazio si spezza in pezzi «indipendenti», basta prendere una base di ciascun pezzo e metterle insieme. Per esempio una base dell'asse x e una dell'asse y danno una base del piano.)

Alla lavagna (registrazione 2024) è solo enunciata, e compare di nuovo scritta durante la pausa, mentre il docente parla con uno studente; nelle dispense compare dentro la dimostrazione del corollario sugli autospazi. Il motivo è questo (verifica non presente nelle dispense né in lezione). B **genera** V: ogni v è una somma w_{1} + … + w_{k}, e ogni w_{i} è combinazione dei vettori di B_{i}. B è **indipendente**: data una combinazione nulla dei vettori di B, si raggruppano i termini che vengono da ciascun B_{i}; il gruppo i-esimo è un vettore u_{i} ∈ W_{i}, e u_{1} + … + u_{k} = 0. Per la somma diretta ogni u_{i} = 0, e poiché B_{i} è indipendente tutti i coefficienti del gruppo i-esimo sono zero.

## Gli autospazi sono in somma diretta
**Proposizione.** Sia T : V → V un endomorfismo e siano λ_{1}, …, λ_{k} i suoi autovalori distinti. Allora gli autospazi V_{λ_{1}}, …, V_{λ_{k}} sono in somma diretta:

V_{λ_{1}} ⊕ … ⊕ V_{λ_{k}}.

(In parole povere: autospazi di autovalori diversi non si mescolano mai. Combinando vettori presi da autospazi diversi non si torna a zero, a meno di prendere tutti zeri.)

**Spiegazione (dalle dispense).** Sia 0 = w_{1} + … + w_{k} con w_{i} ∈ V_{λ_{i}}, e supponiamo che alcuni w_{i} non siano nulli. Quelli non nulli sono autovettori con autovalori distinti, e la loro somma è zero: è una combinazione lineare nulla con tutti i coefficienti uguali a 1, contro la proposizione sugli autovettori di autovalori distinti. Quindi tutti i w_{i} sono nulli. ∎

Alla lavagna (registrazione 2024) la proposizione non è dimostrata.

**Corollario.** Sia T : V → V un endomorfismo e siano λ_{1}, …, λ_{k} **tutti** i suoi autovalori, **distinti**. Allora

T è diagonalizzabile   ⟺   V = V_{λ_{1}} + … + V_{λ_{k}}   ⟺   dim V = dim V_{λ_{1}} + … + dim V_{λ_{k}}.

(In parole povere: T è diagonalizzabile esattamente quando gli autospazi, messi insieme, riempiono tutto lo spazio. Per controllarlo basta sommare le loro dimensioni e vedere se si arriva a dim V.)

Alla lavagna (registrazione 2024) il corollario non è dimostrato, e la parola «distinti» è stata aggiunta durante la pausa; che i λ_{i} debbano essere tutti gli autovalori non è scritto, ma è necessario: se ne mancasse uno, mancherebbe il suo autospazio. Le dispense (Corollario 18.6) scrivono la condizione come V = V_{λ_{1}} ⊕ … ⊕ V_{λ_{k}}, che è la stessa cosa perché la somma è comunque diretta.

**Dimostrazione (dalle dispense, completata).** Gli autospazi sono in somma diretta, quindi basta capire quando la loro somma è tutto V.
- (⟸) Se V = V_{λ_{1}} ⊕ … ⊕ V_{λ_{k}}, unendo basi dei singoli autospazi si ottiene una base di V (proposizione precedente), e i suoi vettori sono autovettori: T è diagonalizzabile.
- (⟹) Se esiste una base di autovettori, ogni v ∈ V è combinazione lineare di autovettori; raggruppando quelli dello stesso autovalore, v diventa una somma di vettori degli autospazi, quindi v ∈ V_{λ_{1}} + … + V_{λ_{k}}.

L'ultima equivalenza, con le dimensioni, viene dalla proposizione sulle basi: la somma diretta degli autospazi ha dimensione dim V_{λ_{1}} + … + dim V_{λ_{k}}, ed è un sottospazio di V; è uguale a V se e solo se ha la stessa dimensione. ∎

**Esempio.** Per ( 2 1 ; 1 2 ): dim V_{1} + dim V_{3} = 1 + 1 = 2 = dim ℝ², diagonalizzabile. Per A = ( 1 1 ; 0 1 ) invece (aggiunto qui come anticipazione; è svolto alla lavagna nella stessa lezione e ripreso nel cap. 63) l'unico autovalore è 1, letto sulla diagonale, e A − I_{2} = ( 0 1 ; 0 0 ) dà l'equazione y = 0, quindi V_{1} = Span((1, 0)) ha dimensione 1 < 2: gli autovettori stanno tutti sull'asse x, non bastano a fare una base del piano, e A **non** è diagonalizzabile.

L'ultimo esempio mostra che il problema, quando gli autovalori sono pochi, è che un autospazio può essere «troppo piccolo». Il capitolo successivo misura questo fenomeno con due numeri, la molteplicità algebrica e la molteplicità geometrica di un autovalore, e arriva al teorema che decide in ogni caso se un endomorfismo è diagonalizzabile.
