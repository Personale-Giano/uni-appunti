# 59. Autovalori e Autovettori
## Che cosa fa un endomorfismo applicato molte volte
Il cap. 54 ha introdotto gli **endomorfismi**, le applicazioni lineari f : V → V da uno spazio in se stesso, con l'invito a pensarli «in maniera dinamica»: una trasformazione che si applica allo stesso spazio più e più volte. A lezione (registrazione 2025) il docente apre l'argomento nuovo proprio con le due domande lasciate in sospeso: come agisce f sullo spazio? E come agisce f ∘ f ∘ … ∘ f, cioè f composta k volte? Prima di dare le definizioni, dice, conviene capire perché interessano.

**Primo esempio dalla lavagna (registrazione 2025).** Sia A = ( 1 0 ; 0 1/2 ) e sia L_{A} : ℝ² → ℝ². Si pensa alla matrice come a una mappa che prende il punto (x, y) e lo manda nel prodotto A·(x, y):

L_{A}(x, y) = ( 1 0 ; 0 1/2 ) · (x, y) = (x, y/2).

La mappa lascia com'è la coordinata x e dimezza la y: «schiaccia tutto il piano» verso l'asse delle x. Applicandola di nuovo la y si dimezza ancora, e dopo mille applicazioni il punto (x, y) è finito in (x, y/2^{1000}). Infatti la potenza di una matrice diagonale si fa elemento per elemento: A^{1000} = ( 1 0 ; 0 1/2^{1000} ). Il docente accenna che, al limite, la mappa diventa la proiezione sull'asse x, senza approfondire.

Come sottolineato a lezione, che cosa rendeva il calcolo così facile? Il fatto che la matrice è **diagonale**: manda il primo vettore della base canonica in un multiplo di se stesso (e_{1} ↦ e_{1}) e il secondo in un multiplo di se stesso (e_{2} ↦ e_{2}/2). Le due direzioni degli assi non si mescolano mai.

## Un esempio meno ovvio: ( 1 2 ; 2 1 )
**Esempio dalla lavagna (registrazione 2025).** Sia ora A = ( 1 2 ; 2 1 ), cioè L_{A}(x, y) = (x + 2y, 2x + y). La formula è esplicita, ma che cosa faccia la mappa dal punto di vista geometrico, dice il docente, «non si capisce». Allora «viene un oracolo» e suggerisce di non usare la base canonica ma la base

B = {v_{1}, v_{2}},   v_{1} = (1, 1),   v_{2} = (1, −1).

La matrice associata [L_{A}]^{B}_{B} si calcola come nel cap. 54, ed è anche facile leggerla dalle immagini dei due vettori: A·v_{1} = (1 + 2, 2 + 1) = (3, 3) = 3v_{1} e A·v_{2} = (1 − 2, 2 − 1) = (−1, 1) = −v_{2}. Le coordinate in B sono quindi (3, 0) e (0, −1), e

[L_{A}]^{B}_{B} = ( 3 0 ; 0 −1 ).

Alla lavagna la matrice è stata scritta con i due numeri della diagonale scambiati; il docente stesso ha poi dichiarato sbagliati quei conti, spiegando che contava il concetto. Qui si riporta la versione corretta.

Scegliere v_{1} e v_{2} è come prendere un sistema di assi girato di 45 gradi. Un vettore qualsiasi si scrive v = a v_{1} + b v_{2}, cioè [v]_{B} = (a, b), e con la formula del cap. 51

[L_{A}(v)]_{B} = [L_{A}]^{B}_{B} · [v]_{B} = ( 3 0 ; 0 −1 ) · (a, b) = (3a, −b),

cioè L_{A}(v) = 3a v_{1} − b v_{2}. Nelle nuove coordinate la mappa si descrive con una frase: **triplica** la componente lungo v_{1} e **ribalta** quella lungo v_{2}. E le iterate si calcolano subito: dopo mille applicazioni

(L_{A} ∘ L_{A} ∘ … ∘ L_{A})(v) = 3^{1000} a v_{1} + (−1)^{1000} b v_{2} = 3^{1000} a v_{1} + b v_{2}.

![Sinistra: la matrice ( 1 0 ; 0 ½ ) schiaccia il piano verso l'asse x. Destra: ( 1 2 ; 2 1 ) letta nella base v₁ = (1, 1), v₂ = (1, −1): la componente lungo v₁ si triplica, quella lungo v₂ cambia segno.](figure/alg/autovettori_iterate.png|14)

Come sottolineato a lezione (registrazione 2025), con le coordinate della base canonica non si sarebbe capito niente; con una base più adatta la mappa e tutte le sue iterate diventano facili. La proprietà fondamentale della base dell'oracolo è che in essa la matrice è diventata **diagonale**, e trovare una base del genere si chiama **diagonalizzazione**. Qui la base è stata regalata; il punto di questa lezione e della successiva è imparare a **trovarla**.

## La definizione
I vettori dell'oracolo hanno una proprietà precisa: ciascuno viene mandato in un multiplo di se stesso. È la definizione centrale di tutto l'argomento.

**Definizione.** Sia T : V → V un endomorfismo di uno spazio vettoriale V sul campo 𝕂. Un **autovettore** di T è un vettore v ∈ V, **v ≠ 0**, tale che

T(v) = λv   per qualche λ ∈ 𝕂.

Lo scalare λ si chiama **autovalore** di T associato (o relativo) a v.

(In parole povere: un autovettore è una direzione che T non fa girare. Il vettore può allungarsi, accorciarsi, ribaltarsi o perfino schiacciarsi a zero, ma resta sulla sua retta; l'autovalore dice di quanto viene moltiplicato.)

Il docente insiste su due dettagli (registrazione 2025). Il vettore deve essere **non nullo**, «è importante»: senza questa condizione 0 sarebbe autovettore di ogni endomorfismo, con qualunque λ, perché T(0) = 0 = λ·0. L'autovalore invece può essere **qualsiasi** scalare, anche zero. Per esempio, per A = ( 1 1 ; 1 1 ) si ha A·(1, −1) = (0, 0) = 0·(1, −1): il vettore (1, −1) è autovettore con autovalore 0. In generale gli autovettori con autovalore 0 sono esattamente i vettori non nulli del nucleo Ker T (cap. 47), perché T(v) = 0·v vuol dire T(v) = 0. (L'esempio numerico è aggiunto per chiarezza.)

Per una matrice quadrata A ∈ M(n, 𝕂) si parla di autovettori e autovalori **di A** intendendo quelli di L_{A} : 𝕂ⁿ → 𝕂ⁿ: v ∈ 𝕂ⁿ, v ≠ 0, è autovettore di A se Av = λv.

## Primi esempi
**Esempio dalla lavagna (registrazione 2025).** «In questo momento non sappiamo come calcolare gli autovettori», dice il docente, ma si può provare con i vettori dell'oracolo. Per A = ( 1 2 ; 2 1 ):
- A·(1, 1) = (3, 3) = 3·(1, 1), quindi (1, 1) è autovettore di L_{A} con autovalore 3;
- A·(1, −1) = (−1, 1) = (−1)·(1, −1), quindi w = (1, −1) è autovettore con autovalore −1.

Come sottolineato a lezione, i vettori trovati sono proprio quelli della base scelta dall'oracolo, e gli autovalori sono proprio i numeri sulla diagonale di [L_{A}]^{B}_{B}: «non è un caso, sarà la norma». Il capitolo successivo lo dimostra.

**Esempio 17.2.** Sia A = ( 3 4 ; 0 2 ). Poiché A·e_{1} = (3, 0) = 3e_{1}, il vettore e_{1} è autovettore di L_{A} con autovalore 3. Invece A·e_{2} = (4, 2), che non è un multiplo di e_{2} = (0, 1) per nessun λ (la prima entrata dovrebbe essere 0): e_{2} non è un autovettore. Però A·(−4, 1) = (−12 + 4, 2) = (−8, 2) = 2·(−4, 1), quindi (−4, 1) è autovettore con autovalore 2. Come si arrivi a un vettore come (−4, 1) senza tirare a indovinare si vedrà nei cap. 61 e 62.

**Esempio 17.4.** In ℝ³ sia A = ( 1 1 −1 ; 2 1 1 ; 3 0 2 ). Si ha A·e_{1} = (1, 2, 3), la prima colonna, che non è un multiplo di e_{1}: e_{1} non è autovettore. Per v = (0, 1, 1) invece A·v = (1 − 1, 1 + 1, 0 + 2) = (0, 2, 2) = 2v: v è autovettore con autovalore 2. Anche w = (0, 3, 3) lo è, con lo stesso autovalore: A·w = (0, 6, 6) = 2w. Non è una coincidenza, perché w = 3v.

**Osservazione (i multipli di un autovettore).** Se v è autovettore di T con autovalore λ, ogni multiplo w = μv con μ ≠ 0 è ancora autovettore con lo stesso autovalore:

T(μv) = μT(v) = μλv = λ(μv).

Quindi un autovettore non viene mai da solo: tutti i vettori non nulli della retta Span(v) sono autovettori con autovalore λ. Per questo è più corretto pensare a **direzioni** speciali piuttosto che a singoli vettori. Per esempio, per ( 1 2 ; 2 1 ) anche (−1, 1) = −(1, −1) è autovettore con autovalore −1 (esempio aggiunto per chiarezza).

## Autovalori e autovettori in coordinate
Le dispense osservano che, come molte altre cose, autovettori e autovalori si possono studiare in coordinate. Sia B una base di V, sia A = [T]^{B}_{B} e sia x = [v]_{B} il vettore delle coordinate di v. Per la formula del cap. 51, [T(v)]_{B} = A x, mentre [λv]_{B} = λx; e due vettori sono uguali se e solo se hanno le stesse coordinate (cap. 49). Quindi

T(v) = λv   ⟺   A x = λ x.

(In parole povere: per cercare autovalori e autovettori di un endomorfismo qualsiasi basta scegliere una base e cercare quelli della sua matrice. Gli autovalori sono gli stessi; gli autovettori di T sono i vettori che hanno come coordinate gli autovettori di A.)

Per questo d'ora in poi basta capire bene il caso T = L_{A}, cioè gli autovalori e gli autovettori di una matrice quadrata.

## Non tutti gli endomorfismi hanno autovettori
**Esempio dalla lavagna (registrazione 2025).** Il docente avverte che quasi ogni matrice ha autovettori, ma la definizione è molto specifica e ci sono eccezioni. La più semplice è la rotazione di 90 gradi in senso antiorario:

Rot_{π/2} : ℝ² → ℝ²,   (x, y) ↦ (−y, x).

Per come è fatta una rotazione, l'immagine di un vettore non nullo non è mai parallela al vettore di partenza: (−y, x) è sempre perpendicolare a (x, y). Quindi nessun vettore non nullo viene mandato in un suo multiplo, e Rot_{π/2} **non ha autovettori** (né autovalori).

![La rotazione di 90°: ogni vettore (blu) viene mandato in un vettore perpendicolare (rosso), quindi nessuno resta sulla propria retta.](figure/alg/rotazione_senza_autovettori.png|9)

L'argomento geometrico si può controllare con un conto (verifica non presente nelle dispense né in lezione). Se (−y, x) = λ(x, y) con λ ∈ ℝ, allora −y = λx e x = λy. Sostituendo la prima nella seconda, x = λy = λ(−λx) = −λ^{2}x, cioè (1 + λ^{2})x = 0. Poiché 1 + λ^{2} > 0 per ogni λ reale, x = 0, e poi y = −λx = 0. L'unica soluzione è il vettore nullo, che non è un autovettore.

Lo stesso vale per qualunque rotazione di un angolo θ diverso da 0 e da π: ogni vettore non nullo viene girato e non può finire su un suo multiplo. Per θ = 0 e θ = π invece la rotazione è rispettivamente f(v) = v e f(v) = −v, e **ogni** vettore non nullo è autovettore, con autovalore 1 o −1 (Esempio 17.10 delle dispense).

A lezione (registrazione 2025) il docente anticipa che la stessa mappa, vista da ℂ² in ℂ² invece che da ℝ² in ℝ², gli autovalori li avrebbe: con autovalori e autovettori «sarà quasi forzata la mano» a usare i numeri complessi. Il conto si fa nel cap. 61.

Restano due domande, che sono il programma dei prossimi capitoli: per quali endomorfismi esiste una base fatta di autovettori, come quella dell'oracolo? E come si trovano autovalori e autovettori senza un oracolo? Il capitolo successivo comincia dalla prima, spiegando perché una base di autovettori rende diagonale la matrice.
