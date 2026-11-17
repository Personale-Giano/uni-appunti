# 49. Gli Isomorfismi e il Vettore delle Coordinate
## Dimensioni e funzioni iniettive o suriettive
Il corollario del cap. 48 confronta la dimensione dell'immagine con quella dello spazio di partenza e di quello di arrivo. Con il teorema della dimensione se ne ricava subito un confronto diretto tra le dimensioni di V e di W, che è il primo passo verso le funzioni lineari biettive.

**Proposizione.** Sia f : V → W un'applicazione lineare, con V e W di dimensione finita.
1. Se f è iniettiva, allora dim V ≤ dim W, perché dim V = dim Im f ≤ dim W.
2. Se f è suriettiva, allora dim V ≥ dim W, perché dim V ≥ dim Im f = dim W.
3. Se f è biettiva, allora dim V = dim W, dai due punti precedenti.

(In parole povere: una funzione lineare iniettiva non può infilare uno spazio grande in uno più piccolo senza sovrapposizioni; una suriettiva non può riempire uno spazio più grande di quello da cui parte.)

Le due catene vengono dal cap. 48: se f è iniettiva il nucleo è {0}, quindi dim Im f = dim V; in ogni caso Im f è un sottospazio di W, quindi dim Im f ≤ dim W; se f è suriettiva Im f = W. A lezione (registrazione 2025) il docente lo collega a quanto visto a Matematica discreta: se c'è una funzione iniettiva da un insieme a un altro, l'insieme di partenza «di sicuro non è più grande» di quello di arrivo (per gli insiemi finiti: non ha più elementi). La dimostrazione, dice, è «facile facile», ed è scritta alla lavagna proprio con le due catene sopra.

Per esempio, nessuna applicazione lineare ℝ³ → ℝ² è iniettiva e nessuna applicazione lineare ℝ² → ℝ³ è suriettiva.

## Gli isomorfismi
Il caso in cui f è sia iniettiva sia suriettiva ha un nome proprio.

**Definizione.** Un'applicazione lineare f : V → W è un **isomorfismo** se è biettiva, cioè iniettiva e suriettiva insieme. Due spazi vettoriali V e W sullo stesso campo 𝕂 si dicono **isomorfi** se esiste un isomorfismo f : V → W.

(In parole povere: due spazi isomorfi sono «lo stesso spazio con nomi diversi». L'isomorfismo è un dizionario che traduce ogni vettore di V in uno e un solo vettore di W, rispettando somme e multipli.)

Come sottolineato a lezione (registrazione 2025), «isomorfi» vuol dire letteralmente «con la stessa forma»: per quanto riguarda il corso, due spazi isomorfi sono equivalenti in tutto e per tutto.

Una funzione biettiva ha sempre un'inversa f^{−1} : W → V (Matematica discreta: ogni elemento di W è colpito da uno e un solo elemento di V). A priori l'inversa è solo una funzione tra insiemi; per un isomorfismo conserva anche la struttura.

**Proposizione.** Se un'applicazione lineare f : V → W è biettiva, anche l'inversa f^{−1} : W → V è lineare.

(In parole povere: se il dizionario da V a W rispetta somme e multipli, anche quello all'indietro li rispetta. Si può tradurre nei due sensi senza perdere nulla.)

La dimostrazione non è svolta né nelle dispense né a lezione. Si può verificare così: dati w, w′ ∈ W, siano v = f^{−1}(w) e v′ = f^{−1}(w′). Poiché f è lineare, f(v + v′) = f(v) + f(v′) = w + w′, quindi f^{−1}(w + w′) = v + v′ = f^{−1}(w) + f^{−1}(w′). Allo stesso modo f(λv) = λw dà f^{−1}(λw) = λv = λf^{−1}(w).

Il docente propone di pensare gli isomorfismi proprio così: sono le applicazioni lineari che hanno un'applicazione lineare «che va al contrario», l'inversa.

## Due spazi sono isomorfi se e solo se hanno la stessa dimensione
Il terzo punto della prima proposizione dice che due spazi isomorfi hanno la stessa dimensione. Vale anche il viceversa.

**Proposizione.** Due spazi vettoriali V e W di dimensione finita sullo stesso campo sono isomorfi se e solo se dim V = dim W. In particolare, ogni spazio vettoriale su 𝕂 di dimensione n è isomorfo a 𝕂ⁿ.

(In parole povere: per gli spazi di dimensione finita conta solo un numero, la dimensione. Due spazi con la stessa dimensione sono, per l'algebra lineare, intercambiabili.)

A lezione (registrazione 2025) la proposizione non è dimostrata; il docente osserva che dice che «non ci sono tantissimi spazi vettoriali»: quelli di dimensione 1 sono tutti isomorfi tra loro, quelli di dimensione 2 pure, e così via. Per esempio ℝ_{2}[x], i polinomi di grado al massimo 2, ha dimensione 3 (cap. 26) ed è isomorfo a ℝ³ (alla lavagna questo spazio è scritto ℝ[x]_{2}: è lo stesso spazio, qui si tiene la scrittura del cap. 48); M(2, 2, ℝ) ha dimensione 4 ed è isomorfo a ℝ⁴, ma non a ℝ³.

Il resto della lezione serve, nelle parole del docente, a trasferire informazioni anche molto astratte su spazi vettoriali e applicazioni lineari in questioni concrete: vettori colonna di numeri e matrici, che un computer sa gestire molto bene.

## L'isomorfismo F_{B} definito da una base
L'isomorfismo tra uno spazio di dimensione n e 𝕂ⁿ si costruisce scegliendo una base. Alla lavagna (registrazione 2025) è l'«esempio importante di isomorfismo».

Sia V uno spazio vettoriale su 𝕂 e B = {v_{1}, …, v_{n}} una base di V. Qui e in seguito le basi si intendono **ordinate**: conta quale vettore è il primo, quale il secondo e così via, perché l'ordine decide l'ordine delle coordinate. Si definisce F_{B} : 𝕂ⁿ → V come

F_{B}(a_{1}, …, a_{n}) = a_{1}v_{1} + a_{2}v_{2} + … + a_{n}v_{n}.

F_{B} prende una lista di n numeri e restituisce la combinazione lineare dei vettori della base con quei coefficienti. È lineare (il docente dice che è facile controllarlo; basta notare che i coefficienti di una somma si sommano). In particolare F_{B}(e_{i}) = v_{i}: **F_{B} manda i vettori della base canonica di 𝕂ⁿ nei vettori della base scelta**. Per esempio F_{B}(e_{1}) = F_{B}(1, 0, …, 0) = 1·v_{1} + 0·v_{2} + … + 0·v_{n} = v_{1}.

**Proposizione.** Se B è una base di V, F_{B} : 𝕂ⁿ → V è un isomorfismo.

(In parole povere: con una base, le liste di n numeri e i vettori di V si corrispondono uno a uno. Ogni lista dà un vettore, e ogni vettore viene da una e una sola lista.)

A lezione la dimostrazione è lasciata come esercizio («è carino»), con questa traccia: le due proprietà di una base corrispondono esattamente alle due metà della biettività.
- **Generatori ⟹ suriettiva.** L'immagine di F_{B} è l'insieme delle combinazioni lineari di v_{1}, …, v_{n}, cioè Span(v_{1}, …, v_{n}) = V.
- **Indipendenti ⟹ iniettiva.** Il nucleo è fatto delle liste con a_{1}v_{1} + … + a_{n}v_{n} = 0; per l'indipendenza lineare l'unica è (0, …, 0), quindi Ker F_{B} = {0} (cap. 47).

## L'inversa: il vettore delle coordinate
Il docente chiede alla classe come si calcola l'inversa F_{B}^{−1} : V → 𝕂ⁿ. Dato v ∈ V, le entrate del vettore cercato devono dipendere da v. Poiché B è una base, v si scrive in modo unico come v = a_{1}v_{1} + … + a_{n}v_{n} (cap. 25), e F_{B} manda (a_{1}, …, a_{n}) proprio in v. Quindi F_{B}^{−1}(v) è la lista delle coordinate di v.

**Definizione.** Sia B = {v_{1}, …, v_{n}} una base di V e sia v = a_{1}v_{1} + … + a_{n}v_{n}. Il vettore colonna

[v]_{B} = (a_{1}, …, a_{n}) ∈ 𝕂ⁿ

si chiama **vettore delle coordinate** di v nella base B. La funzione v ↦ [v]_{B} è l'isomorfismo F_{B}^{−1} : V → 𝕂ⁿ.

(In parole povere: [v]_{B} è la «ricetta» di v scritta in colonna: quanti v_{1}, quanti v_{2}, e così via. È così che un vettore astratto diventa una lista di numeri.)

Come sottolineato a lezione (registrazione 2025), il simbolo [v]_{B} è «parecchio importante»: è ciò che permette di prendere vettori qualsiasi e farli diventare elementi di 𝕂ⁿ. Essendo F_{B}^{−1} lineare, vale [v + w]_{B} = [v]_{B} + [w]_{B} e [λv]_{B} = λ[v]_{B}.

Questo isomorfismo **dipende dalla base scelta**: basi diverse danno isomorfismi diversi, e lo stesso vettore ha coordinate diverse. Come si passi da una base all'altra è annunciato per la lezione successiva. Nella base canonica di 𝕂ⁿ, invece, le coordinate di un vettore sono le sue entrate (cap. 25), quindi il vettore delle coordinate coincide con il vettore stesso.

## Esempio: le coordinate di un polinomio
**Esempio dalla lavagna (registrazione 2025).** Sia V = ℝ_{2}[x] e B = {x², x + 1, 1} (a lezione il docente dice che è una base, senza verificarlo). Si cerca il vettore delle coordinate di p(x) = 3x² + 2x + 1. È un vettore di ℝ³: ℝ perché i coefficienti sono reali, 3 perché dim V = 3. Le sue entrate sono i numeri a, b, c tali che

p(x) = a·x² + b·(x + 1) + c·1 = ax² + bx + (b + c).

Raccogliendo le potenze di x e confrontando con 3x² + 2x + 1 (due polinomi sono uguali se hanno gli stessi coefficienti): a = 3, b = 2 e b + c = 1, quindi c = −1. Dunque

[p(x)]_{B} = (3, 2, −1).

Controllo: 3x² + 2(x + 1) − 1 = 3x² + 2x + 1. Nella base canonica {1, x, x²} lo stesso polinomio avrebbe coordinate (1, 2, 3): stesso vettore, base diversa, coordinate diverse.

Che B sia davvero una base si verifica in fretta: tre polinomi in uno spazio di dimensione 3, e generano, perché 1, x = (x + 1) − 1 e x² stanno nel loro Span (cap. 26).

**Come sottolineato a lezione (registrazione 2025).** Per comunicare un polinomio a un computer ci si può mettere d'accordo su una base e poi passare solo il vettore (3, 2, −1): chi lo riceve sa che rappresenta 3 volte il primo elemento della base, più 2 volte il secondo, meno una volta il terzo. È la stessa idea già vista nel cap. 25. Il capitolo successivo fa lo stesso con le applicazioni lineari: fissate due basi, ogni applicazione lineare diventa una matrice.
