# 65. Il Prodotto Scalare Euclideo e un Prodotto Scalare sui Polinomi
## Il prodotto scalare euclideo di ℝⁿ
Il primo esempio della lavagna (registrazione 2025) è quello che il docente chiama «il più carino di tutti». In ℝⁿ si scrivono i vettori in colonna, v = (x_{1}, …, x_{n}) e w = (y_{1}, …, y_{n}).

**Definizione (Def. 19.5).** Il **prodotto scalare euclideo** su ℝⁿ è

⟨v, w⟩ = ᵗv · w = (x_{1} … x_{n}) · (y_{1}, …, y_{n}) = x_{1}y_{1} + x_{2}y_{2} + … + x_{n}y_{n} = Σ_{i=1}^{n} x_{i}y_{i}.

(In parole povere: si moltiplicano i due vettori coordinata per coordinata, la prima con la prima, la seconda con la seconda e così via, e si sommano i risultati. Un solo numero riassume «quanto i due vettori vanno d'accordo».)

La scrittura ᵗv · w merita una spiegazione, che il docente dà a voce. Il vettore colonna v è una matrice n × 1, quindi la sua trasposta ᵗv (cap. 27) è una matrice 1 × n, cioè un vettore riga. Il prodotto righe per colonne (cap. 29) di una matrice 1 × n per una n × 1 si può fare, perché il numero di colonne della prima è uguale al numero di righe della seconda, e dà una matrice 1 × 1, cioè **un numero**. Quel numero è proprio x_{1}y_{1} + … + x_{n}y_{n}. Scrivere il prodotto euclideo come ᵗv · w sarà comodo fra poco, perché permette di usare le proprietà del prodotto fra matrici.

**Esempio dalla lavagna (registrazione 2025).** In ℝ³ siano v = (1, 1, 2) e w = (−1, −1, 1). Allora

⟨v, w⟩ = 1·(−1) + 1·(−1) + 2·1 = −1 − 1 + 2 = 0.

Due vettori non nulli possono quindi avere prodotto scalare zero. Le dispense danno anche un esempio in ℝ²: ⟨(1, 3), (−2, 1)⟩ = 1·(−2) + 3·1 = 1.

## Che cosa misura: lunghezze e coseno
Accanto all'esempio il docente scrive in un riquadro (registrazione 2025)

⟨v, w⟩ = v • w = ‖v‖ · ‖w‖ · cos θ,

con un disegno di due frecce v e w e l'angolo θ fra loro. A voce spiega che in alcuni libri e nei corsi di fisica il prodotto euclideo si scrive v • w, e che quando i vettori si pensano come frecce lo si calcola anche come «lunghezza del primo vettore per lunghezza del secondo per il coseno dell'angolo compreso»: è così, per esempio, che si introduce il lavoro di una forza. Chi non l'ha mai visto, aggiunge, non si deve preoccupare: è un'anticipazione, e la lunghezza ‖v‖ e l'angolo θ verranno **definiti** proprio a partire dal prodotto scalare nella lezione successiva (dispense §20).

Già da qui però si intuisce il significato del segno. Le lunghezze ‖v‖ e ‖w‖ sono positive, quindi il segno di ⟨v, w⟩ è quello di cos θ: il prodotto scalare è positivo se l'angolo è acuto, nullo se è retto, negativo se è ottuso (dispense §20.E). Nell'esempio della lavagna ⟨v, w⟩ = 0: i vettori (1, 1, 2) e (−1, −1, 1) sono **perpendicolari**.

![Il prodotto scalare euclideo di v = (2, 0) con tre vettori w: positivo se l'angolo è acuto, nullo se è retto, negativo se è ottuso.](figure/alg/prodotto_scalare_angolo.png|15)

## L'euclideo è un prodotto scalare definito positivo
**Proposizione (Prop. 19.6).** Il prodotto scalare euclideo è un prodotto scalare definito positivo su ℝⁿ.

Le dispense la enunciano senza dimostrazione; alla lavagna (registrazione 2025) il docente la dimostra, perché è un buon modello di che cosa voglia dire «mostrare che qualcosa è un prodotto scalare».

**Dimostrazione.** Si ricorda che ⟨v, w⟩ = ᵗv · w.

Passo ① (è un prodotto scalare). Bisogna controllare le tre proprietà della definizione (cap. 64).
- a) Additività: ⟨v_{1} + v_{2}, w⟩ = ᵗ(v_{1} + v_{2}) · w = (ᵗv_{1} + ᵗv_{2}) · w = ᵗv_{1} · w + ᵗv_{2} · w = ⟨v_{1}, w⟩ + ⟨v_{2}, w⟩. Si sono usati il fatto che la trasposta di una somma è la somma delle trasposte e la distributività del prodotto fra matrici (cap. 30).
- b) Omogeneità: ⟨λv, w⟩ = ᵗ(λv) · w = (λ ᵗv) · w = λ (ᵗv · w) = λ⟨v, w⟩. Si sono usati ᵗ(λv) = λ ᵗv e il fatto che uno scalare si può portare fuori da un prodotto di matrici.
- c) Simmetria: ⟨v, w⟩ = x_{1}y_{1} + … + x_{n}y_{n} = y_{1}x_{1} + … + y_{n}x_{n} = ⟨w, v⟩, perché il prodotto fra numeri reali è commutativo. (Alla lavagna questo punto non è scritto; lo si aggiunge per completezza.)

Passo ② (è definito positivo). Sia v = (x_{1}, …, x_{n}). Allora

⟨v, v⟩ = x_{1}² + x_{2}² + … + x_{n}².

Ogni quadrato di un numero reale è ≥ 0, quindi anche la somma è ≥ 0. Inoltre una somma di numeri ≥ 0 è zero solo se ogni addendo è zero: ⟨v, v⟩ = 0 se e solo se x_{1} = x_{2} = … = x_{n} = 0, cioè v = 0. Quindi per ogni v ≠ 0 si ha ⟨v, v⟩ > 0.

È qui che serve davvero 𝕂 = ℝ: in ℂ un quadrato può essere negativo (i² = −1) e l'argomento crollerebbe.

**Esempio (aggiunto per chiarezza).** Per v = (1, −2, 2) si ha ⟨v, v⟩ = 1 + 4 + 4 = 9 > 0. Per v = (3, 4) in ℝ² si ha ⟨v, v⟩ = 9 + 16 = 25 = 5²: è il quadrato della lunghezza della freccia che va dall'origine al punto (3, 4), per il teorema di Pitagora. È il primo indizio di come il prodotto scalare servirà a misurare le lunghezze.

A lezione uno studente chiede se di prodotti scalari ce ne siano tanti. La risposta del docente (registrazione 2025): infiniti. «Prodotto scalare» è il nome di una **classe** di funzioni, quelle che soddisfano le tre proprietà; il prodotto euclideo è un esempio specifico dentro questa classe. Il capitolo 66 mostra come costruirne moltissimi altri su ℝⁿ.

## Un prodotto scalare sui polinomi
Un prodotto scalare non vive solo su ℝⁿ: si può definire su spazi vettoriali più astratti. Il secondo esempio della lavagna è sullo spazio ℝ_{2}[x] dei polinomi a coefficienti reali di grado al più 2 (cap. 10).

**Esempio 2 dalla lavagna (registrazione 2025) ed Esempio 19.4.** Su ℝ_{2}[x] si pone

⟨p, q⟩ = p(0)q(0) + p(1)q(1) + p(2)q(2).

In pratica si valutano i due polinomi in 0, 1 e 2, si moltiplicano i valori punto per punto e si sommano. Per esempio, con p(x) = 1 + x e q(x) = x² si ha p(0) = 1, p(1) = 2, p(2) = 3 e q(0) = 0, q(1) = 1, q(2) = 4, quindi

⟨1 + x, x²⟩ = 1·0 + 2·1 + 3·4 = 14

(esempio aggiunto per chiarezza). In un certo senso è il prodotto euclideo dei vettori (p(0), p(1), p(2)) e (q(0), q(1), q(2)) di ℝ³.

Il docente osserva che bisogna verificare le tre proprietà, ma che «non è troppo difficile» (registrazione 2025). La verifica, aggiunta per completezza: la valutazione in un punto rispetta somme e multipli: (p_{1} + p_{2})(a) = p_{1}(a) + p_{2}(a) e (λp)(a) = λp(a). Da qui seguono le proprietà 1 e 2, mentre la 3 viene da p(a)q(a) = q(a)p(a).

A voce il docente lascia anche un esercizio: far vedere che questo prodotto scalare è **definito positivo**. La soluzione è nelle dispense. Si ha

⟨p, p⟩ = p(0)² + p(1)² + p(2)² ≥ 0,

e la somma è zero solo se p(0) = p(1) = p(2) = 0, cioè se p si annulla in tre punti distinti. Ma un polinomio non nullo di grado al più 2 ha al massimo 2 radici (cap. 13). Quindi, se p ≠ 0, almeno uno dei tre valori è diverso da zero e ⟨p, p⟩ > 0.

Perché interessarsi di prodotti scalari fra polinomi? A lezione (registrazione 2025) il docente risponde che, una volta che c'è un prodotto scalare, si potrà parlare di **angolo** o di **distanza** fra due polinomi o fra due funzioni. Non è solo un gioco da matematici: su queste idee si basano la teoria dei segnali e alcune decomposizioni usate anche in informatica, costruite con i cosiddetti **polinomi ortogonali**, polinomi che formano fra loro un angolo di 90 gradi, come se fossero perpendicolari.

## Due varianti che non funzionano altrettanto bene
Le dispense completano l'Esempio 19.4 con due varianti, utili per vedere in azione le definizioni del cap. 64.

**Una variante degenere.** Su ℝ_{2}[x] si consideri ⟨p, q⟩ = p(0)q(0) + p(1)q(1), con solo due punti. È ancora un prodotto scalare (stesso ragionamento di prima), ma è **degenere**: il polinomio p(x) = x(1 − x) non è nullo e si annulla in 0 e in 1, quindi ⟨p, q⟩ = 0·q(0) + 0·q(1) = 0 per ogni q.

**Una variante non degenere ma non definita positiva.** Si consideri ⟨p, q⟩ = p(0)q(0) + p(1)q(1) − p(2)q(2). Le dispense affermano che non è degenere (giustificazione aggiunta: se ⟨p, q⟩ = 0 per ogni q, si sceglie q con valori (1, 0, 0) in 0, 1, 2, poi (0, 1, 0), poi (0, 0, 1), cosa possibile perché un polinomio di grado al più 2 si può far passare per tre punti con ascisse distinte; si ottiene p(0) = 0, p(1) = 0 e −p(2) = 0, quindi p ha tre radici e p = 0), ma non è definito positivo: per p(x) = x − 1 si ha p(0) = −1, p(1) = 0, p(2) = 1, quindi

⟨p, p⟩ = (−1)² + 0² − 1² = 0,

con p ≠ 0. È l'esempio promesso nel cap. 64 di un prodotto scalare non degenere che non è definito positivo.

Trabocchetto d'esame: per dimostrare che un prodotto scalare **non** è definito positivo basta trovare **un** vettore v ≠ 0 con ⟨v, v⟩ ≤ 0; per dimostrare che **è** degenere basta trovare **un** v ≠ 0 che fa zero con tutti. Le affermazioni contrarie (è definito positivo, non è degenere) richiedono invece un ragionamento che valga per ogni vettore.

Come anticipato dal docente a lezione, il prossimo passo è capire come sono fatti «gli altri» prodotti scalari di ℝⁿ: la risposta passa per le matrici simmetriche, ed è l'argomento del capitolo successivo.
