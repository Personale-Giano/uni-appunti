# 54. La Matrice Associata in Basi Diverse, Endomorfismi e Matrici Simili
## La formula del cambio di base per un'applicazione lineare
Il cap. 53 ha lasciato aperta una domanda: se f : V → W è lineare, B e B′ sono due basi di V e C e C′ due basi di W, che legame c'è tra [f]^{B}_{C} e [f]^{B′}_{C′}? Con la matrice di una composizione la risposta è un conto di una riga.

**Proposizione.** Sia f : V → W un'applicazione lineare, siano B, B′ basi di V e C, C′ basi di W, e siano

P = [I_{V}]^{B}_{B′},   Q = [I_{W}]^{C}_{C′}

le matrici del cambio di base dalle basi «vecchie» alle basi «nuove». Allora

[f]^{B′}_{C′} = Q · [f]^{B}_{C} · P^{−1}.

(In parole povere: per avere la matrice di f nelle basi nuove si prende quella nelle basi vecchie e la si moltiplica a sinistra e a destra per due «traduttori». Quello di destra riporta le coordinate nuove di V a quelle vecchie, quello di sinistra porta le coordinate vecchie di W a quelle nuove.)

**Dimostrazione (alla lavagna, registrazione 2025).** Comporre con l'identità non cambia una funzione: f = I_{W} ∘ f ∘ I_{V}, perché un vettore v va in v, poi in f(v), poi ancora in f(v). Si scelgono però basi diverse lungo il percorso: B′ in partenza, poi B, poi C, e infine C′.

![La funzione f preceduta e seguita dall'identità, con le basi usate a ogni passo e le tre matrici che ne risultano.](figure/alg/cambio_base_mappa.png|13)

Applicando due volte la formula della composizione (cap. 53), ogni freccia diventa una matrice e la composizione un prodotto, con la prima funzione applicata scritta più a destra:

[f]^{B′}_{C′} = [I_{W} ∘ f ∘ I_{V}]^{B′}_{C′} = [I_{W}]^{C}_{C′} · [f]^{B}_{C} · [I_{V}]^{B′}_{B}.

Il primo fattore è Q. L'ultimo è la matrice del cambio di base da B′ a B, cioè l'inversa di P = [I_{V}]^{B}_{B′} (cap. 53). ∎

Anche qui le basi «si cancellano» a coppie: C con C, B con B, e restano B′ in alto e C′ in basso. Se dim V = n e dim W = m, P è una matrice n × n e Q una matrice m × m, quindi il prodotto ha senso e dà una matrice m × n.

Le dispense scrivono la stessa formula senza dare un nome alle due matrici: con basi B_{1}, B_{2} di V e C_{1}, C_{2} di W,

[f]^{B_{2}}_{C_{2}} = [id_{W}]^{C_{1}}_{C_{2}} · [f]^{B_{1}}_{C_{1}} · [id_{V}]^{B_{2}}_{B_{1}},

e commentano che per passare da una matrice all'altra basta moltiplicare a sinistra e a destra per le matrici di cambiamento di base. A una domanda, il docente (registrazione 2025) spiega perché alla lavagna l'ultimo fattore è riscritto come P^{−1}: di solito interessa sapere come si passa «dalle basi vecchie alle basi nuove», e allora conviene che P e Q vadano tutte e due in quel verso.

## Un esempio: la stessa L_{A} in un'altra base
**Esempio dalla lavagna (registrazione 2025).** Sia A = ( 1 2 ; 2 1 ) ∈ M(2, 2, ℝ) e sia L_{A} : ℝ² → ℝ². Si vuole la matrice [L_{A}]^{B}_{B} con B = {(1, 1), (1, 2)}, usata sia in partenza sia in arrivo.

Sia E la base canonica di ℝ² (alla lavagna è chiamata C). Tre fatti rendono il conto facile:
- [L_{A}]^{E}_{E} = A, la matrice di partenza (cap. 50);
- [I_{V}]^{B}_{E} = ( 1 1 ; 1 2 ), perché la base di arrivo è la canonica e bastano i vettori di B in colonna (cap. 52);
- [I_{V}]^{E}_{B} è l'inversa della precedente, cioè ( 2 −1 ; −1 1 ), già calcolata nel cap. 52.

La formula, con E come base vecchia e B come base nuova in entrambi gli spazi, dà

[L_{A}]^{B}_{B} = [I_{V}]^{E}_{B} · [L_{A}]^{E}_{E} · [I_{V}]^{B}_{E} = ( 2 −1 ; −1 1 ) · ( 1 2 ; 2 1 ) · ( 1 1 ; 1 2 ).

Si moltiplicano prima le ultime due: ( 1 2 ; 2 1 ) · ( 1 1 ; 1 2 ) = ( 3 5 ; 3 4 ). Poi, per ( 2 −1 ; −1 1 ) · ( 3 5 ; 3 4 ), le quattro entrate sono 6 − 3 = 3, 10 − 4 = 6, −3 + 3 = 0, −5 + 4 = −1:

[L_{A}]^{B}_{B} = ( 3 6 ; 0 −1 ).

Il controllo si fa con il significato delle colonne: A·(1, 1) = (3, 3) = 3·(1, 1) + 0·(1, 2), e A·(1, 2) = (5, 4) = 6·(1, 1) − 1·(1, 2).

Il docente spiega perché questo tipo di esercizio è importante: per le funzioni da uno spazio in se stesso ci sono spesso **basi speciali**, non per forza la canonica, in cui si capisce particolarmente bene come agisce la funzione. Ci saranno direzioni speciali, gli **autovettori**, lungo le quali la funzione è molto semplice. Qui se ne vede un accenno: la prima colonna (3, 0) dice che il vettore (1, 1) viene mandato in 3 volte se stesso.

## Gli endomorfismi
**Definizione.** Sia V uno spazio vettoriale. Un **endomorfismo** di V è un'applicazione lineare f : V → V, cioè con lo stesso spazio in partenza e in arrivo.

(In parole povere: un endomorfismo è una trasformazione lineare di uno spazio in se stesso. I vettori non cambiano «casa», vengono solo spostati dentro lo stesso spazio.)

Per esempio L_{A} è un endomorfismo di 𝕂ⁿ quando A è quadrata. A lezione (registrazione 2025) il docente invita a pensare gli endomorfismi «in maniera dinamica»: V è lo spazio degli stati di un sistema (le posizioni di un braccio meccanico, la distribuzione di persone o di nuvole in una regione) e a ogni istante lo stato cambia attraverso la stessa trasformazione. Interessa allora che cosa succede applicandola più e più volte, cioè sul lungo periodo. Sono le funzioni che si studieranno nelle lezioni successive attraverso autovalori e autovettori.

Poiché spazio di partenza e di arrivo coincidono, ha senso usare **la stessa base** B da entrambe le parti: ogni endomorfismo è rappresentato da una matrice quadrata [f]^{B}_{B}. Se f e g sono due endomorfismi di V, la formula del cap. 53 con la stessa base ovunque dice che la composizione corrisponde al prodotto:

[f ∘ g]^{B}_{B} = [f]^{B}_{B} · [g]^{B}_{B}.

La domanda naturale è la solita: se B′ è un'altra base, che rapporto c'è tra [f]^{B}_{B} e [f]^{B′}_{B′}?

**Proposizione.** Sia f : V → V un endomorfismo, siano B e B′ due basi di V e sia P = [I_{V}]^{B}_{B′}. Allora

[f]^{B′}_{B′} = P · [f]^{B}_{B} · P^{−1}.

(In parole povere: cambiando base, la matrice di un endomorfismo viene «incorniciata» dalla matrice del cambio di base e dalla sua inversa: una da una parte, l'altra dall'altra.)

È il caso particolare della proposizione generale con W = V, C = B e C′ = B′: le due matrici P e Q diventano la stessa.

**Il verso delle due notazioni.** Le dispense scrivono la stessa relazione con la matrice del cambio di base presa nel verso opposto. Chiamano C la base in cui la matrice è nota e B quella in cui la si vuole, pongono M = [id]^{B}_{C} (dalla base nuova alla vecchia) e scrivono

[f]^{B}_{B} = M^{−1} · [f]^{C}_{C} · M.

Alla lavagna la matrice nota è in B, quella voluta in B′, e P = [I_{V}]^{B}_{B′} va dalla base vecchia alla nuova. Le due formule dicono la stessa cosa, con **M = P^{−1}**: in entrambe la matrice più a destra porta dalle coordinate nuove alle vecchie, e quella più a sinistra riporta alle nuove. Nei conti in 𝕂ⁿ la versione delle dispense è comoda quando la base vecchia è la canonica, perché allora M ha per colonne i vettori della base nuova e si scrive senza calcoli. È esattamente quello che si è fatto nell'esempio precedente, dove M = ( 1 1 ; 1 2 ) e P = M^{−1} = ( 2 −1 ; −1 1 ).

**Esempio 16.10.** Sia f : ℝ² → ℝ², f(x, y) = (x + y, −y). Nella base canonica E (C nelle dispense), f(e_{1}) = (1, 0) e f(e_{2}) = (1, −1), quindi

[f]^{E}_{E} = ( 1 1 ; 0 −1 ).

Si prende ora la base B = {(1, 0), (−1, 2)}. La matrice del cambio di base da B alla canonica ha i vettori di B in colonna, e la sua inversa si trova con la regola 2 × 2 (determinante 2):

M = [I_{V}]^{B}_{E} = ( 1 −1 ; 0 2 ),   M^{−1} = [I_{V}]^{E}_{B} = ( 1 1/2 ; 0 1/2 ).

Quindi [f]^{B}_{B} = M^{−1} · [f]^{E}_{E} · M. Prima ( 1 1 ; 0 −1 ) · ( 1 −1 ; 0 2 ) = ( 1 1 ; 0 −2 ), poi ( 1 1/2 ; 0 1/2 ) · ( 1 1 ; 0 −2 ), con entrate 1 + 0 = 1, 1 − 1 = 0, 0, −1:

[f]^{B}_{B} = ( 1 0 ; 0 −1 ).

Verifica diretta: f(1, 0) = (1, 0), il primo vettore di B resta fermo; f(−1, 2) = (1, −2) = −(−1, 2), il secondo va nel suo opposto. Nella base B la funzione si legge molto meglio che nella canonica: la matrice è diagonale. L'esempio è nelle dispense; a lezione non è svolto.

## Le matrici simili
La relazione tra due matrici dello stesso endomorfismo è abbastanza speciale, dice il docente, da meritare un nome.

**Definizione.** Due matrici quadrate A, B ∈ M(n) si dicono **simili** (o **coniugate**) se esiste una matrice invertibile P ∈ M(n) tale che

B = P A P^{−1}.

In questo caso si scrive A ∼ B.

(In parole povere: due matrici simili sono la stessa trasformazione raccontata in due basi diverse. I numeri dentro cambiano, ma quello che la matrice «fa» è lo stesso.)

Da qui in poi A e B sono due matrici, non più due basi. La forma B = PAP^{−1} è quella della lavagna (registrazione 2025); le dispense scrivono A = M^{−1}BM, e da loro vengono il nome «coniugate» e il simbolo ∼. Le due scritture sono equivalenti con M = P: moltiplicando B = PAP^{−1} a sinistra per P^{−1} e a destra per P si ottiene P^{−1}BP = A.

Per la proposizione precedente, due matrici che rappresentano lo stesso endomorfismo in basi diverse sono simili. Vale anche il viceversa (la verifica non è nelle dispense né in lezione): se B = PAP^{−1}, le colonne di P^{−1} formano una base B′ di 𝕂ⁿ (una matrice invertibile ha colonne indipendenti), P^{−1} = [I_{V}]^{B′}_{E} e quindi B = [L_{A}]^{B′}_{B′}, mentre A = [L_{A}]^{E}_{E}. Per esempio, dai conti di questo capitolo, ( 1 2 ; 2 1 ) ∼ ( 3 6 ; 0 −1 ) e ( 1 1 ; 0 −1 ) ∼ ( 1 0 ; 0 −1 ).

**Proposizione.** La similitudine è una relazione di equivalenza in M(n).

(In parole povere: «essere simili» si comporta come «essere uguali sotto un certo aspetto». Ogni matrice è simile a se stessa, la relazione vale nei due versi e si trasmette a catena.)

Le dispense la enunciano senza dimostrazione e a lezione non compare: la verifica che segue non è quindi né nelle dispense né in lezione. Le tre proprietà (Matematica discreta) si controllano così:
- **riflessiva**: A = I_{n} A I_{n}^{−1}, quindi A ∼ A;
- **simmetrica**: se B = PAP^{−1}, allora A = P^{−1}BP = (P^{−1}) B (P^{−1})^{−1}, quindi B ∼ A;
- **transitiva**: se B = PAP^{−1} e D = RBR^{−1}, allora D = RPAP^{−1}R^{−1} = (RP) A (RP)^{−1}, perché (RP)(P^{−1}R^{−1}) = I_{n}; quindi A ∼ D.

Di conseguenza M(n) è diviso in sottoinsiemi disgiunti, le classi di equivalenza, ciascuno formato da matrici simili fra loro.

## Che cosa hanno in comune due matrici simili
**Proposizione.** Se A e B sono matrici simili, allora:
1. det A = det B;
2. tr A = tr B;
3. rk(A) = rk(B).

In particolare, A è invertibile se e solo se B è invertibile.

(In parole povere: due matrici simili possono avere numeri completamente diversi, ma determinante, traccia e rango sono gli stessi. Sono quantità che appartengono alla trasformazione, non alla base scelta per scriverla.)

Alla lavagna (registrazione 2025) i punti sono tre, compresa la **traccia**, e il docente dice di saltare le dimostrazioni; le dispense riportano solo rango e determinante, aggiungono l'equivalenza sull'invertibilità e danno una breve spiegazione. I motivi sono questi, con B = PAP^{−1}:
1. per il teorema di Binet (cap. 36), det B = det P · det A · det(P^{−1}) = det A, perché det P · det(P^{−1}) = det(PP^{−1}) = det I_{n} = 1;
2. per la proprietà tr(XY) = tr(YX) (cap. 30), applicata a X = P e Y = AP^{−1}: tr B = tr(P · AP^{−1}) = tr(AP^{−1} · P) = tr A (verifica non presente nelle dispense né in lezione);
3. moltiplicare a sinistra o a destra per una matrice invertibile non cambia il rango, quindi rk(PAP^{−1}) = rk(A): è la spiegazione delle dispense, che lo usano come fatto noto. Il motivo è che L_{P} e L_{P^{−1}} sono isomorfismi di 𝕂ⁿ (cap. 53), e comporre con un isomorfismo, prima o dopo, non cambia la dimensione dell'immagine, cioè il rango (cap. 47).

Infine una matrice è invertibile se e solo se il determinante non è zero (cap. 36), e i due determinanti sono uguali.

**Come sottolineato a lezione (registrazione 2025).** Due matrici simili, «anche se in apparenza diverse», condividono queste proprietà, che dicono non tanto qual è l'aspetto delle matrici quanto qual è il loro comportamento. Non deve sorprendere: sono due rappresentazioni della stessa funzione, e le proprietà della funzione devono ritrovarsi in tutte le sue matrici.

Sui due esempi del capitolo: ( 1 2 ; 2 1 ) e ( 3 6 ; 0 −1 ) hanno entrambe determinante −3, traccia 2 e rango 2; ( 1 1 ; 0 −1 ) e ( 1 0 ; 0 −1 ) hanno entrambe determinante −1, traccia 0 e rango 2. È anche un modo rapido per controllare un cambio di base: se traccia o determinante non tornano, c'è un errore di conto.

**Attenzione.** La proposizione non si può rovesciare: due matrici con lo stesso determinante, la stessa traccia e lo stesso rango non sono per forza simili. Per esempio I_{2} e ( 1 1 ; 0 1 ) hanno entrambe determinante 1, traccia 2 e rango 2, ma l'unica matrice simile all'identità è l'identità stessa, perché P I_{2} P^{−1} = I_{2} per ogni P. (Osservazione aggiunta per chiarezza, non presente nelle dispense né in lezione.)

## Esercizio
Svolgimento non presente nelle dispense (che danno solo il testo) né in lezione.

**Esercizio 16.14.** Sia f : ℝ² → ℝ² l'endomorfismo f(x, y) = (2x + y, x + 2y). Siano E = {e_{1}, e_{2}} la base canonica (C nelle dispense) e B = {v_{1}, v_{2}} con v_{1} = (1, 1) e v_{2} = (1, −1). (1) Trovare A = [f]^{E}_{E}. (2) Trovare la matrice del cambio di base M = [I_{V}]^{B}_{E}. (3) Calcolare [f]^{B}_{B} con la formula del cambio di base. (4) Verificare il risultato calcolando direttamente f(v_{1}) e f(v_{2}).

(1) f(e_{1}) = (2, 1) e f(e_{2}) = (1, 2); nella base canonica le coordinate sono le entrate, quindi A = ( 2 1 ; 1 2 ).

(2) La base di arrivo è la canonica, quindi bastano i vettori di B in colonna: M = ( 1 1 ; 1 −1 ).

(3) Il determinante di M è −1 − 1 = −2, e la regola 2 × 2 dà M^{−1} = (1/(−2)) · ( −1 −1 ; −1 1 ) = ( 1/2 1/2 ; 1/2 −1/2 ). Poi AM = ( 2 1 ; 1 2 ) · ( 1 1 ; 1 −1 ) = ( 3 1 ; 3 −1 ), e infine M^{−1} · AM ha entrate 3/2 + 3/2 = 3, 1/2 − 1/2 = 0, 3/2 − 3/2 = 0, 1/2 + 1/2 = 1:

[f]^{B}_{B} = M^{−1} A M = ( 3 0 ; 0 1 ).

(4) f(v_{1}) = f(1, 1) = (3, 3) = 3v_{1} + 0·v_{2}, che dà la colonna (3, 0); f(v_{2}) = f(1, −1) = (1, −1) = 0·v_{1} + 1·v_{2}, che dà la colonna (0, 1). Il risultato è confermato. Come controllo ulteriore, A e [f]^{B}_{B} hanno lo stesso determinante, 4 − 1 = 3 = 3·1, e la stessa traccia, 2 + 2 = 4 = 3 + 1.

Anche qui, come nell'Esempio 16.10, nella base giusta la matrice è diagonale: ogni vettore di B viene mandato in un multiplo di se stesso. Trovare basi di questo tipo è il tema delle lezioni successive, dedicate ad autovalori e autovettori.
