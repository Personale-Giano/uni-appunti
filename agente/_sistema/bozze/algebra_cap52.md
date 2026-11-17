# 52. La Matrice del Cambio di Base
## Lo stesso vettore, coordinate diverse
I cap. 49-51 hanno costruito due «traduzioni» in numeri: fissata una base B = {v_{1}, …, v_{n}} di V, ogni vettore v diventa il vettore delle coordinate [v]_{B} ∈ 𝕂ⁿ; fissate una base B di V e una base C di W, ogni applicazione lineare f : V → W diventa la matrice associata [f]^{B}_{C}. A lezione (registrazione 2025) il docente richiama alla lavagna le due proprietà che serviranno di continuo: [f(v)]_{C} = [f]^{B}_{C} · [v]_{B} (cap. 51) e, per le basi canoniche, la matrice associata a L_{A} è A stessa (cap. 50). Poi pone il problema della lezione: sia le coordinate sia la matrice associata **dipendono dalla base scelta**. Quanto cambiano se si cambia base?

La prima domanda riguarda i vettori: date due basi B e B′ dello stesso spazio V, che legame c'è tra [v]_{B} e [v]_{B′}?

**Alla lavagna (registrazione 2025)** il docente disegna due persone che guardano lo stesso piano V. Uno spazio vettoriale, dice, «non ha inizialmente nessuna coordinata»: chi vuole comunicare un vettore deve prima scegliere una base. La prima persona sceglie B = {v_{1}, v_{2}} e vede v = v_{1} + v_{2}, quindi per lei [v]_{B} = (1, 1). La seconda sceglie B′ = {v_{1}′, v_{2}′}, con v_{1}′ proprio uguale a v, e vede v = 1·v_{1}′ + 0·v_{2}′, quindi [v]_{B′} = (1, 0). Il vettore è lo stesso, le coordinate no. Serve un metodo per tradurre le coordinate dell'una in quelle dell'altra.

![Lo stesso vettore v = (3, 7) ha coordinate (3, 7) nella base canonica e (−1, 4) nella base w₁ = (1, 1), w₂ = (1, 2): è l'esempio svolto più avanti.](figure/alg/cambio_base_vettore.png|13)

Per far capire che non è una questione da poco, il docente racconta (registrazione 2025) di una sonda spaziale andata perduta perché due gruppi di lavoro si passavano delle distanze in unità di misura diverse, senza convertirle. Una conversione tra unità di misura, osserva, «è letteralmente un cambio di base». È solo un aneddoto, non materia d'esame.

## La definizione
**Definizione.** Sia V uno spazio vettoriale di dimensione n e siano B = {v_{1}, …, v_{n}} e B′ = {v_{1}′, …, v_{n}′} due basi di V. La **matrice del cambio di base da B a B′** è la matrice associata all'identità I_{V} : V → V, con B come base di partenza e B′ come base di arrivo:

[I_{V}]^{B}_{B′} = ( [v_{1}]_{B′} | [v_{2}]_{B′} | … | [v_{n}]_{B′} ) ∈ M(n, n, 𝕂).

(In parole povere: è il «dizionario» che traduce dalla lingua B alla lingua B′. Si costruisce scrivendo ogni vettore della base vecchia B con la base nuova B′, e mettendo in colonna i numeri trovati.)

Le colonne vengono dalla definizione di matrice associata (cap. 50): la j-esima colonna è [I_{V}(v_{j})]_{B′}, e l'identità lascia fermo v_{j}. Quindi la j-esima colonna contiene le coordinate di v_{j}, il j-esimo vettore della base **di partenza**, rispetto alla base **di arrivo**. Come sempre, la base di partenza sta in alto e quella di arrivo in basso.

Sulla notazione: le dispense chiamano «id» l'identità e C la seconda base, e scrivono [id]^{B}_{C} («matrice di cambiamento di base»); alla lavagna (registrazione 2025) le due basi si chiamano A e A′ e la matrice è [I_{V}]^{A}_{A′}. Sono lo stesso oggetto. Qui si scrive I_{V}, come nel cap. 51, e si usano B e B′ per due basi dello stesso spazio, tenendo C per le basi dello spazio di arrivo W, come nei cap. 50-51. Attenzione a non confonderla con [I_{V}]^{B}_{B}, che è la matrice identità I_{n} (cap. 51): quando le due basi sono diverse, la matrice dell'identità **non** è la matrice identità.

## La formula del cambio di coordinate
**Proposizione.** Siano B e B′ due basi di V. Per ogni v ∈ V vale

[v]_{B′} = [I_{V}]^{B}_{B′} · [v]_{B}.

(In parole povere: per passare dalle coordinate vecchie a quelle nuove basta una moltiplicazione matrice per vettore. La matrice è sempre la stessa, qualunque sia il vettore da tradurre.)

**Dimostrazione.** È la proposizione del cap. 51, [f(v)]_{C} = [f]^{B}_{C} · [v]_{B}, applicata a f = I_{V} con base di arrivo B′. Poiché I_{V}(v) = v:

[v]_{B′} = [I_{V}(v)]_{B′} = [I_{V}]^{B}_{B′} · [v]_{B}. ∎

Come sottolineato a lezione (registrazione 2025), questa è la risposta alla prima domanda: le coordinate di uno stesso vettore rispetto a due basi diverse «differiscono per la moltiplicazione per una matrice». Nota la matrice, si traduce qualunque vettore. Per questo, dice il docente, è importante saper calcolare queste matrici.

## Un esempio in ℝ²
**Esempio dalla lavagna (registrazione 2025).** In V = ℝ² si prendono la base canonica E = {e_{1}, e_{2}} e la base B′ = {w_{1}, w_{2}}, con w_{1} = (1, 1) e w_{2} = (1, 2). Si vuole la matrice del cambio di base dalla canonica a B′:

[I_{V}]^{E}_{B′} = ( [e_{1}]_{B′} | [e_{2}]_{B′} ).

La matrice ha tante colonne quanti sono i vettori della base di partenza. Per ogni colonna si prende un vettore della base di partenza, gli si applica la funzione (qui l'identità, quindi resta com'è) e se ne calcolano le coordinate nella base di arrivo.

- Prima colonna. Si cercano a, b con e_{1} = a w_{1} + b w_{2}, cioè (1, 0) = a(1, 1) + b(1, 2) = (a + b, a + 2b). Il sistema è a + b = 1, a + 2b = 0. Sottraendo la prima equazione dalla seconda si trova b = −1, e poi a = 2. Quindi [e_{1}]_{B′} = (2, −1).
- Seconda colonna. Il membro di destra è lo stesso, cambia solo il vettore a cui deve essere uguale: (0, 1) = (a + b, a + 2b), cioè a + b = 0, a + 2b = 1. Si trova b = 1 e a = −1. Quindi [e_{2}]_{B′} = (−1, 1).

Il risultato è

[I_{V}]^{E}_{B′} = ( 2 −1 ; −1 1 ).

Alla lavagna la prima colonna era stata scritta (−1, 2), con a e b scambiati, ed è stata corretta su segnalazione di uno studente. Il docente nota anche che in generale ogni colonna richiede un sistema, da risolvere «in maniera strutturata» con i metodi dei cap. 39-40; questo è così piccolo che si fa a mano.

**A che cosa serve.** Con la matrice appena trovata si calcolano le coordinate di (3, 7) nella base B′. Il punto di partenza è una proprietà della base canonica che il docente chiede di ricordare, perché vale **solo** per lei: le coordinate di un vettore rispetto alla base canonica sono le entrate del vettore stesso, [v]_{E} = v (cap. 50). Quindi [(3, 7)]_{E} = (3, 7) e

[(3, 7)]_{B′} = [I_{V}]^{E}_{B′} · [(3, 7)]_{E} = ( 2 −1 ; −1 1 ) · (3, 7) = (6 − 7, −3 + 7) = (−1, 4).

Significa che (3, 7) = −w_{1} + 4w_{2}, e infatti −(1, 1) + 4(1, 2) = (−1 + 4, −1 + 8) = (3, 7). È la situazione della figura di questo capitolo.

## Quando la base di arrivo è la canonica
Nell'esempio la base canonica era quella di **partenza**, e questo non ha risparmiato nessun conto: sono serviti due sistemi. Le cose cambiano del tutto quando la canonica è la base di **arrivo**.

**Proposizione.** Sia V = 𝕂ⁿ, sia B = {v_{1}, …, v_{n}} una base qualsiasi e sia E = {e_{1}, …, e_{n}} la base canonica. Allora la matrice del cambio di base da B alla canonica ha per colonne i vettori di B:

[I_{V}]^{B}_{E} = ( v_{1} | v_{2} | … | v_{n} ).

(In parole povere: tradurre da una base qualsiasi alla base canonica non costa niente. Si prendono i vettori della base e si scrivono uno accanto all'altro, senza risolvere alcun sistema.)

Infatti la j-esima colonna è [v_{j}]_{E}, e nella base canonica le coordinate di un vettore sono il vettore stesso. Alla lavagna (registrazione 2025) questa è l'«osservazione importante» della lezione, con la base canonica chiamata C; nelle dispense compare solo dentro la seconda soluzione dell'Esercizio 16.3. Il docente consiglia di ricordarla perché «semplifica i conti in maniera infinita».

Nell'esempio precedente, la matrice nel verso opposto a quello richiesto si scrive subito:

[I_{V}]^{B′}_{E} = ( w_{1} | w_{2} ) = ( 1 1 ; 1 2 ).

Si potrebbe obiettare che un cambio di base verso la canonica capita di rado. Il resto della lezione mostra invece che ci si può sempre ricondurre a questo caso; il primo passo è la proposizione seguente.

## L'inversa della matrice del cambio di base
**Proposizione.** Siano B e B′ due basi di V. La matrice del cambio di base da B a B′ è invertibile, e la sua inversa è la matrice del cambio di base da B′ a B:

( [I_{V}]^{B}_{B′} )^{−1} = [I_{V}]^{B′}_{B}.

(In parole povere: il dizionario al contrario è la matrice inversa. Se una matrice traduce da B a B′, la sua inversa traduce da B′ a B.)

Nelle dispense questa proprietà è scritta dentro la definizione; alla lavagna (registrazione 2025) è una proposizione a parte, che vale «sempre» e non viene dimostrata. Si dimostra con la formula del cambio di coordinate. Siano M = [I_{V}]^{B}_{B′} e M′ = [I_{V}]^{B′}_{B}. Tradurre un vettore da B a B′ e poi di nuovo da B′ a B restituisce le coordinate di partenza: M′(M[v]_{B}) = M′[v]_{B′} = [v]_{B}. Ogni x ∈ 𝕂ⁿ è il vettore delle coordinate di qualche v, quindi (M′M)x = x per ogni x; con x = e_{j} si legge che la j-esima colonna di M′M è e_{j}, cioè M′M = I_{n}. Scambiando i ruoli delle due basi si ottiene anche MM′ = I_{n}, quindi M′ = M^{−1}. Il capitolo successivo ritrova lo stesso risultato per un'altra via, con la matrice di una composizione.

**Esempio dalla lavagna (registrazione 2025).** La matrice dell'esempio in ℝ² si ritrova senza sistemi: la base di partenza è la canonica, quindi è l'inversa della matrice «facile».

[I_{V}]^{E}_{B′} = ( [I_{V}]^{B′}_{E} )^{−1} = ( 1 1 ; 1 2 )^{−1} = (1/1) · ( 2 −1 ; −1 1 ) = ( 2 −1 ; −1 1 ).

Si è usata la regola per l'inversa di una matrice 2 × 2 (cap. 36): il determinante è 1·2 − 1·1 = 1, si scambiano gli elementi della diagonale principale e si cambia segno agli altri due. È la stessa matrice trovata con i due sistemi.

Il docente è onesto sul confronto tra i due metodi: con matrici 2 × 2 l'inversa è immediata; con matrici 3 × 3 invertire è più laborioso, ma anche i sistemi diventano più pesanti, e secondo lui l'inversa resta un po' più veloce. Il consiglio è quindi: per un cambio di base **dalla canonica a un'altra base**, scrivere la matrice facile (i vettori della base in colonna) e invertirla.

## Un esempio 3 × 3 svolto nei due modi
**Esercizio 16.3.** In ℝ³ siano E = {e_{1}, e_{2}, e_{3}} la base canonica e B = {w_{1}, w_{2}, w_{3}} con w_{1} = (1, 2, 3), w_{2} = (0, 2, 1), w_{3} = (0, 1, 1). Trovare la matrice del cambio di base A = [I_{V}]^{E}_{B}. (Nelle dispense la base canonica si chiama A e la matrice cercata è [id]^{A}_{B}; a lezione l'esercizio non è svolto.)

**Primo modo: i sistemi.** La j-esima colonna di A contiene i numeri a_{1j}, a_{2j}, a_{3j} con e_{j} = a_{1j}w_{1} + a_{2j}w_{2} + a_{3j}w_{3}. In componenti, a w_{1} + b w_{2} + c w_{3} = (a, 2a + 2b + c, 3a + b + c), quindi per e_{1} = (1, 0, 0) il sistema è

a = 1,   2a + 2b + c = 0,   3a + b + c = 0.

Con a = 1 restano 2b + c = −2 e b + c = −3; sottraendo, b = 1, e poi c = −4. La prima colonna è (1, 1, −4). Allo stesso modo, per e_{2} = (0, 1, 0): a = 0, 2b + c = 1, b + c = 0, da cui b = 1 e c = −1; per e_{3} = (0, 0, 1): a = 0, 2b + c = 0, b + c = 1, da cui b = −1 e c = 2. Mettendo in colonna:

A = ( 1 0 0 ; 1 1 −1 ; −4 −1 2 ).

**Secondo modo: l'inversa.** La matrice nel verso opposto, da B alla canonica, ha per colonne i vettori di B:

A^{−1} = [I_{V}]^{B}_{E} = ( 1 0 0 ; 2 2 1 ; 3 1 1 ).

Il suo determinante, sviluppato lungo la prima riga (cap. 33), è 1·(2·1 − 1·1) = 1, quindi è invertibile, e invertendola (cap. 36) si ritrova

A = ( 1 0 0 ; 2 2 1 ; 3 1 1 )^{−1} = ( 1 0 0 ; 1 1 −1 ; −4 −1 2 ).

Controllo sulla prima colonna: w_{1} + w_{2} − 4w_{3} = (1, 2 + 2 − 4, 3 + 1 − 4) = (1, 0, 0) = e_{1}.

Il capitolo successivo introduce la composizione di applicazioni lineari: serve a ritrovare la formula dell'inversa da un punto di vista più generale e a trattare il caso in cui nessuna delle due basi è la canonica.
