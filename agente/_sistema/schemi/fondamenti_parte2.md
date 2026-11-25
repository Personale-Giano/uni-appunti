# Quantificatori annidati

## Quantificatori annidati {25, 28, 29}
= Più quantificatori in fila, uno dentro la zona d'azione dell'altro: il significato di y può dipendere dal valore scelto per x. Con due variabili le forme sono quattro.
![tre versioni di «x ama y»](figure/fond/amore_quantificatori.png)
- due quantificatori **uguali** consecutivi dicono solo «per ogni coppia» (∀x ∀y) o «esiste una coppia» (∃x ∃y)
- quelli **diversi** sono delicati: ∀x ∃y L(x, y) «ognuno ama qualcuno», ∃x ∀y L(x, y) «c'è qualcuno che ama tutti», ∃y ∀x L(x, y) «c'è qualcuno amato da tutti»
- il dominio di P(x, y) è un prodotto cartesiano X × Y: ogni coppia è una casella, riga x e colonna y
- in ∀x ∃y la y si sceglie dopo aver visto x e può cambiare da riga a riga; per questo ∃x ∀y chiede molto di più
- regola del docente: la scelta fatta dopo sfrutta i dati forniti prima; quella fatta prima deve andare bene per tutte le scelte successive
```
∀x ∀y  vera: tutte le caselle buone      falsa: una coppia cattiva
∀x ∃y  vera: ogni riga ha una buona      falsa: una riga tutta cattiva
∃x ∀y  vera: una riga tutta buona        falsa: ogni riga ha una cattiva
∃x ∃y  vera: una casella buona           falsa: tutte cattive
```
! Trabocchetto: i quantificatori diversi non commutano: sugli interi ∀x ∃y (y > x) è vera, ∃y ∀x (y > x) è falsa (basta x = y).
> Vedi anche: Il dominio decide la verità, Negare i quantificatori annidati, Predicato e dominio

## Il dominio decide la verità {25, 27, 29}
= La stessa formula può essere vera su un dominio e falsa su un altro: queste formule descrivono proprietà di un insieme di numeri.
- ∀m ∃n (m < n), «non c'è un massimo»: vera su ℤ, ℤ⁺ e ℝ; falsa su {1, …, 10}, perché sopra 10 non c'è niente
- ∃x ∀y (x ≤ y), «c'è un minimo»: vera su ℤ⁺ con x = 1, falsa su ℝ con y = x − 1
- ∀x ∃y (x + y = 0): falsa su ℤ⁺, vera su ℝ con y = −x
- ∀x ∃y (x = y²), «ogni x ha una radice»: vera sui reali positivi e sui complessi, falsa su ℝ, ℤ, ℚ⁺ e ℚ
! Trabocchetto: ∃x ∀y (xy < 1) è vera su ℝ (x = 0) ma falsa sui reali non nulli: la negazione ∀x ∃y (xy ≥ 1) vale con y = 1/x.
> Vedi anche: Quantificatori annidati, Negare i quantificatori annidati

## Negare i quantificatori annidati {27, 28, 29}
= Si applica De Morgan un quantificatore per volta, dall'esterno verso l'interno: ogni ∀ diventa ∃ e viceversa, e alla fine si nega il predicato.
- si continua finché i ¬ stanno solo davanti ai predicati; davanti a un'implicazione si usa ¬(p → q) ≡ p ∧ ¬q
- confronti: ¬(a < b) è a ≥ b, ¬(a > b) è a ≤ b, ¬(a ≤ b) è a > b, ¬(a ≥ b) è a < b
- negare un confronto è **involutivo**: due volte riporta al punto di partenza
- esempio: ¬∀x ∃y (x > y) ≡ ∃x ∀y (x ≤ y), da «non c'è un minimo» a «c'è un minimo»
```
¬∀x ∀y P ≡ ∃x ∃y ¬P        ¬∀x ∃y P ≡ ∃x ∀y ¬P
¬∃x ∀y P ≡ ∀x ∃y ¬P        ¬∃x ∃y P ≡ ∀x ∀y ¬P
```
! Trabocchetto: negando «minore» compare l'uguale: ¬(a < b) è a ≥ b, non a > b.
> Vedi anche: Quantificatori annidati, De Morgan per i quantificatori

## Dimostrare o confutare un annidato {28, 29}
= Ogni forma ha la sua ricetta: solo due casi su otto si chiudono esibendo due valori, negli altri serve un ragionamento su valori arbitrari.
- **∀∀ falsa** o **∃∃ vera**: bastano due valori; **∀∀ vera** o **∃∃ falsa**: x e y arbitrari e un ragionamento
- **∀x ∃y vera**: x arbitrario e una y, che può dipendere da x, con P vera; **∀x ∃y falsa**: una sola x e P falsa con y arbitraria
- **∃x ∀y vera**: una sola x e P vera con y arbitraria; **∃x ∀y falsa**: x arbitrario e una y, anche dipendente da x, con P falsa
- **gioco logico**: si leggono i quantificatori da sinistra; sul ∀ sceglie l'avversario, sull'∃ scegli tu; se hai sempre un modo di vincere, la formula è vera
- esempio: ∃x ∀y (x + y = 0) su ℝ è falsa: se x = 0 l'avversario prende y = 1, se x ≠ 0 prende y = 0
! Trabocchetto: un esempio favorevole non dimostra un ∀: su un dominio infinito i casi non si possono controllare tutti.
> Vedi anche: Quantificatori annidati, Controesempio

## Decidere i quantificatori con un programma {26}
= Su un dominio finito D = {d_{1}, …, d_{n}} una formula con due quantificatori si decide con due cicli annidati.
- ∀x ∀y P: doppio for, `return false` appena P è falsa, `return true` solo fuori dai due cicli
- ∀x ∃y P si scompone in ∀x Q(x), con Q(x) = ∃y P(x, y): in Q la y è **legata**, la x è **libera**
- Q diventa una **funzione** `ex(x)`: il suo return esce solo dalla funzione, non da tutto il programma
- con k quantificatori su n elementi i controlli sono n^{k}: esponenziale nel numero di quantificatori
```
ex(x) {
  for y = 1 to n
    if (P(x, y) == true) return true;
  return false; }
for x = 1 to n
  if (ex(x) == false) return false;
return true;
```
! Trabocchetto: con `return true` appena P è vera, dentro il doppio for, si decide ∃x ∃y e non ∀x ∃y: il return esce da tutto.
> Vedi anche: Quantificatori annidati, Quantificatori su un dominio finito

## Mondo di Tarski e insieme vuoto {30}
= Un **mondo di Tarski** è un dominio finito costruito a piacere, una scacchiera 8 × 8 con cubi, tetraedri e dodecaedri, in cui una macchina controlla se una formula descrive la scena.
- ∀x (Cubo(x) → ∃y (Tet(y) ∧ LeftOf(x, y))): ogni cubo ha una piramide alla sua destra, non per forza la stessa
- aggiungendo ∧ FrontOf(x, y) la formula diventa più forte: se è falsa quella con il solo LeftOf, lo è anche l'altra
- ∀x (Dod(x) → Grande(x)) «tutti i dodecaedri sono grandi»; ∃x (Dod(x) ∧ Grande(x)) «c'è un dodecaedro grande»
- **senza dodecaedri** la prima è vera e la seconda falsa: un universale sull'insieme vuoto è sempre vero, un esistenziale sempre falso
- con un solo oggetto ∀ ed ∃ dicono la stessa cosa
! Trabocchetto: sull'insieme vuoto il ∀ non implica l'∃: in un'aula vuota «tutti i presenti hanno il libro» è vero.
> Vedi anche: Implicazione materiale, Ricerca del primo zero, Monotonia di una sequenza

# Dimostrazione diretta e insiemi

## Dimostrazione diretta {31}
= Per «per ogni x, se p allora q» si prendono elementi **arbitrari**, si suppone p vera e si deduce q con assiomi, definizioni, teoremi e regole di inferenza.
- **sistema matematico**: **assiomi** (veri senza dimostrazione), **definizioni** e **termini non definiti** (come punto e retta); **teorema** è una proposizione dimostrata, **lemma** un teorema che serve per altri, **corollario** uno che si ricava facilmente
- basta il caso p vera: se p è falsa l'implicazione è vera per difetto
- **pari**: n = 2k per qualche intero k; **dispari**: n = 2k + 1; dietro la definizione c'è un ∃
- un ∃ nell'**ipotesi** si usa, dandogli un nome; un ∃ nella **tesi** si costruisce, trovandolo con una formula
```
Ipotesi: m dispari, n pari  →  m = 2k₁ + 1, n = 2k₂
Passi:   m + n = (2k₁ + 1) + 2k₂ = 2(k₁ + k₂) + 1
Tesi:    con k = k₁ + k₂, intero, m + n = 2k + 1 è dispari
```
! Trabocchetto: con la stessa k, m = 2k + 1 e n = 2k dice che m e n sono consecutivi: valori diversi vogliono nomi diversi.
> Vedi anche: Errori comuni nelle dimostrazioni, Regole di inferenza, Implicazione materiale

## Doppia inclusione {32, 34}
= Due insiemi sono uguali se ogni elemento del primo sta nel secondo e viceversa; si **espandono le definizioni** (~unfolding~) fino ad avere solo logica.
- x ∈ A ∩ B: x ∈ A e x ∈ B; x ∈ A ∪ B: x ∈ A oppure x ∈ B; x ∈ A − B: x ∈ A e x ∉ B
- esempio: X ∩ (Y − Z) = (X ∩ Y) − (X ∩ Z), con De Morgan e il **sillogismo disgiuntivo** (da p ∨ q e ¬p segue q)
- per dimostrare p ∨ q basta un lato; per p ∧ q servono entrambi
- in alternativa si calcola con le leggi degli insiemi: X ∪ (Y − X) = X ∪ (Y ∩ X̄) = (X ∪ Y) ∩ (X ∪ X̄) = (X ∪ Y) ∩ U = X ∪ Y
! Trabocchetto: contare gli elementi non basta: {1, 2, 3} e {4, 5, 6} hanno tre elementi ciascuno ma sono diversi.
> Vedi anche: Insieme delle parti, Controesempio, Leggi di De Morgan

## Sottodimostrazione {32}
= Una **sottodimostrazione** dimostra a parte un risultato intermedio dentro una prova più grande, come una funzione ausiliaria di un programma.
- enunciato: se d = min{d_{1}, d_{2}} e x ≤ d, allora x ≤ d_{1} e x ≤ d_{2}
- manca il collegamento tra d e d_{1}, d_{2}: la sottodimostrazione prova d ≤ d_{1} e d ≤ d_{2}, per casi sulla definizione di minimo
- poi la **transitività** e la regola di congiunzione chiudono la prova
- per una macchina il difficile è capire che serve un valore intermedio
```
Sotto:      se d₁ ≤ d₂: d = d₁ ≤ d₂;   se d₂ < d₁: d = d₂ < d₁
            quindi d ≤ d₁ e d ≤ d₂
Principale: x ≤ d ≤ d₁ e x ≤ d ≤ d₂   (transitività)
```
> Vedi anche: Dimostrazione diretta

## Controesempio {33, 34}
= Per confutare ∀x P(x) basta un elemento che renda P falsa; va mostrato e va spiegato perché la smentisce.
- 2^{n} + 1 è sempre primo? n = 1 e n = 2 danno 3 e 5, ma n = 3 dà 9 = 3 · 3
- se non si sa se è vero, si prova a dimostrare: il punto in cui ci si blocca indica dove cercare il controesempio
- (A ∩ B) ∪ C = A ∩ (B ∪ C)? la prova si blocca su x ∈ C: serve un elemento in C ma non in A, per esempio A = B = ∅ e C = {0}
- all'esame: universale falso, controesempio spiegato; universale vero, dimostrazione; esistenziale vero, un esempio
! Trabocchetto: dopo un controesempio, altri esempi favorevoli (n = 4 dà 17, primo) non salvano il ∀.
> Vedi anche: Errori comuni nelle dimostrazioni, Doppia inclusione, Cercare un controesempio

## Errori comuni nelle dimostrazioni {33}
= Tre errori tipici: lo stesso simbolo per quantità diverse, i casi particolari al posto della prova, la tesi data per vera.
- «m = 2k e n = 2k, quindi mn = (2k)² è un quadrato» è sbagliato: servono k_{1} e k_{2}, e infatti 2 · 4 = 8 non è un quadrato
- verificare che 11 + 4 = 15 è dispari prova l'enunciato solo per quei due valori
- **ragionamento circolare**: per provare «se m e m + n sono pari, n è pari» non si può partire da n = 2k_{2}
- prova giusta: m = 2k_{1} e m + n = 2h, quindi n = 2h − 2k_{1} = 2(h − k_{1})
! Trabocchetto: nel ragionamento circolare i conti tornano lo stesso, ma non provano niente.
> Vedi anche: Dimostrazione diretta, Controesempio

## Paradosso del bevitore {33}
= In un dominio non vuoto, per ogni proprietà P, vale ∃x (P(x) → ∀y P(y)): in ogni pub c'è uno tale che, se beve lui, bevono tutti.
- si dimostra per casi, secondo che ∀y P(y) sia vera o falsa
- se tutti hanno P, va bene qualunque x: la tesi dell'implicazione è vera
- se qualcuno non ha P, si sceglie proprio lui: l'ipotesi è falsa e l'implicazione è vera per difetto
- è vero ma non dà informazione: dipende dal fatto che l'implicazione è **materiale**
! Trabocchetto: non dice che c'è un capo che trascina gli altri: l'implicazione non chiede nessun legame tra x e gli altri.
> Vedi anche: Dimostrazione per casi

## Insieme delle parti {34, 38}
= L'**insieme delle parti** P(X) contiene tutti i sottoinsiemi di X, compresi ∅ e X: per X = {1, 2} è {∅, {1}, {2}, {1, 2}}.
- P(X ∪ Y) ⊆ P(X) ∪ P(Y) è falsa: con X = {2} e Y = {3}, Z = {2, 3} sta a sinistra ma non a destra
- P(X) ∪ P(Y) ⊆ P(X ∪ Y) è vera, con il lemma X ⊆ X ∪ Y e Y ⊆ X ∪ Y
- P(X ∩ Y) = P(X) ∩ P(Y) con una catena di «se e solo se»: Z ⊆ X e Z ⊆ Y equivale a Z ⊆ X ∩ Y
- se X ha n elementi, P(X) ne ha 2ⁿ, per induzione; base n = 0: l'unico sottoinsieme di ∅ è ∅, e 2⁰ = 1
- passo: X ha n + 1 elementi; si fissa x ∈ X; Y = X senza x ha n elementi, quindi 2ⁿ sottoinsiemi senza x, e altrettanti con x (S con x si accoppia con S senza x): 2 · 2ⁿ = 2^{n+1}, per {a, b, c} 4 + 4 = 8
! Trabocchetto: una catena dimostra un'uguaglianza solo se **tutti** i passaggi sono equivalenze; con un passo a senso unico si ha al più un'inclusione.
> Vedi anche: Doppia inclusione, Principio di induzione

## Differenza simmetrica {34}
= A Δ B = (A − B) ∪ (B − A): gli elementi che stanno in uno solo dei due insiemi, la controparte insiemistica dello **xor**.
- vale A Δ B = (A ∪ B) − (A ∩ B), per doppia inclusione
- x ∈ (A Δ B) Δ C se e solo se x sta in un numero dispari tra A, B e C
- A Δ A = ∅, A Δ ∅ = A, A Δ U = U − A, A Δ (U − A) = U
- è commutativa e associativa: gli argomenti uguali si cancellano a due a due, A Δ B Δ A = B
- A Δ B = A ∪ B esattamente quando A ∩ B = ∅
> Vedi anche: Doppia inclusione

# Assurdo, contrapposizione e casi

## Dimostrazione per assurdo {35}
= Per provare p → q si suppongono p vera e q falsa e si deduce una **contraddizione** r ∧ ¬r, che è sempre falsa.
- funziona perché p → q è falsa solo con p vera e q falsa: se quel caso porta all'assurdo, non può capitare; in breve, per provare A basta provare ¬A → falso
- ¬q non si assume perché lo si crede vero, ma per escluderlo
- **√2 è irrazionale**: da √2 = p/q, con p e q non entrambi pari, segue 2q² = p², quindi p pari, p = 2k; allora q² = 2k² e anche q è pari, contraddizione
- **tesi con «oppure» o «esiste»**: la si nega con De Morgan; se x + y ≥ 2 allora x ≥ 1 oppure y ≥ 1, perché x < 1 e y < 1 darebbero x + y < 2
- 26 carte di un mazzo da 52 con 4 semi: un seme ne ha almeno 7, perché con al più 6 per seme sarebbero al più 24; la prova non dice quale seme
```
Tesi:     se n² è pari allora n è pari
Assurdo:  n² pari e n non pari, quindi n dispari, n = 2k + 1
          n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1 è dispari
Contraddizione: n² è pari e non pari
```
! Trabocchetto: una prova per assurdo di «esiste un x» dice che x non può mancare, ma non come trovarlo.
> Vedi anche: Dimostrazione per contrapposizione, Leggi di De Morgan, De Morgan per i quantificatori

## Dimostrazione per contrapposizione {35, 36}
= Per provare p → q si dimostra la **contrapposta** ¬q → ¬p: si suppone falsa la tesi e si deduce che è falsa l'ipotesi.
- funziona perché p → q e ¬q → ¬p hanno la stessa tavola di verità
- per assurdo si cerca una contraddizione qualsiasi; per contrapposizione il traguardo è fissato, ¬p
- è il caso speciale dell'assurdo in cui si arriva a ¬p senza usare p
- **razionale**: x = p/q con p, q interi e q ≠ 0; **irrazionale**: non razionale
```
Tesi:         se x² è irrazionale allora x è irrazionale
Contrapposta: se x è razionale allora x² è razionale
x = p/q con q ≠ 0  →  x² = p²/q², con q² ≠ 0
```
! Trabocchetto: non confonderla con la **conversa** q → p, che non è equivalente: la contrapposta scambia **e** nega.
> Vedi anche: Dimostrazione per assurdo, Conversa e contrapposta

## Dimostrazione per casi {36}
= Se l'ipotesi si spezza in p_{1} ∨ … ∨ p_{n}, si dimostrano una per una p_{1} → q, …, p_{n} → q.
- vale (p_{1} ∨ … ∨ p_{n}) → q ≡ (p_{1} → q) ∧ … ∧ (p_{n} → q)
- un «oppure», anche nascosto in una definizione come quella di |x|, suggerisce i casi
- **dimostrazione esaustiva**: casi finiti e pochi, controllati tutti; 2m² + 3n² = 40 non ha soluzioni intere positive perché m ≤ 4 e n ≤ 3 lasciano 12 coppie, e nessuna dà 40
- ridurre l'infinito al finito: così sono stati dimostrati il teorema dei quattro colori e la congettura di Keplero
```
Tesi:  x ≤ |x| per ogni reale x
Caso x ≥ 0:  |x| = x, quindi x ≤ |x|
Caso x < 0:  |x| = −x > 0, quindi x < 0 < |x|
```
! Trabocchetto: i casi vanno dimostrati **tutti**, perché non si sa in anticipo in quale si cadrà.
> Vedi anche: Paradosso del bevitore

## Dimostrazione di equivalenza {36}
= Per «p se e solo se q» si dimostrano le due implicazioni p → q e q → p, perché p ↔ q ≡ (p → q) ∧ (q → p).
- le due direzioni si annunciano: da sinistra a destra, poi da destra a sinistra
- si può scrivere come catena: n dispari ⟺ n = 2k + 1 ⟺ n − 1 = 2k ⟺ n − 1 pari
- la catena è corretta solo se **ogni anello** vale nei due versi
```
n dispari ⟹ n − 1 pari:   n = 2k + 1, quindi n − 1 = 2k
n − 1 pari ⟹ n dispari:   n − 1 = 2h, quindi n = 2h + 1
```
! Trabocchetto: x = 2 ⟹ x² = 4 è vera, ma non il contrario (x = −2): scrivere x = 2 ⟺ x² = 4 è un errore.
> Vedi anche: Dimostrazione per contrapposizione, Dimostrazione diretta

# Induzione

## Principio di induzione {37}
= Se S(1) è vera (**passo base**) e per ogni n ≥ 1 S(n) implica S(n + 1) (**passo induttivo**), allora S(n) vale per ogni intero positivo n.
- è un domino: cade la prima tessera, e ogni tessera fa cadere la successiva
- nel passo induttivo S(n), l'**ipotesi induttiva**, si suppone per un n qualsiasi: non si sa che è vera
- con base n_{0}: si prova S(n_{0}) e S(n) → S(n + 1) per ogni n ≥ n_{0}; il passo base è sempre sul valore più piccolo
- su ℕ si scrive anche P(0) e ∀n > 0 (P(n − 1) → P(n))
```
Base:   S(1) vera
Passo:  suppongo S(n), dimostro S(n + 1)
Tesi:   S(n) vera per ogni n ≥ 1
```
! Trabocchetto: ∀n ∈ ℕ (P(n − 1) → P(n)) è sbagliato: per n = 0 compare P(−1), che non ha senso.
> Vedi anche: Induzione forte, Invariante di ciclo

## Somme per induzione {37}
= Il trucco del passo induttivo è ritrovare la somma fino a n dentro la somma fino a n + 1.
![ogni nuovo dispari aggiunge una squadra lungo due lati](figure/fond/induzione_dispari_quadrati.png)
- 1 + 2 + … + n = n(n + 1)/2: da 1 a 10 fa 55
- 1 + 3 + … + (2n − 1) = n²: la formula si trova calcolando i primi casi, 1, 4, 9, 16
- il dispari di posto n è 2n − 1, quello di posto n + 1 è 2n + 1
```
Base:     S₁ = 1 = 1 · 2/2
Passo:    Sₙ₊₁ = Sₙ + (n + 1) = n(n + 1)/2 + 2(n + 1)/2 = (n + 1)(n + 2)/2
Dispari:  1 + 3 + … + (2n − 1) + (2n + 1) = n² + 2n + 1 = (n + 1)²
```
! Trabocchetto: anche un milione di casi controllati al computer non danno la certezza: serve la prova.
> Vedi anche: Principio di induzione, Somma geometrica

## Disuguaglianza del fattoriale {37}
= Il **fattoriale** è n! = n(n − 1) ··· 2 · 1 per n ≥ 1, con 0! = 1, e vale (n + 1)! = (n + 1) · n!. Per ogni n ≥ 1 si ha n! ≥ 2^{n−1}.
- per n da 1 a 6: n! vale 1, 2, 6, 24, 120, 720 e 2^{n−1} vale 1, 2, 4, 8, 16, 32
- prima la «roadmap»: scrivere base e passo, poi fare i conti
- il primo passo è un **unfolding** di (n + 1)!, per far comparire n!
```
Base:   1! = 1 ≥ 2⁰ = 1
Passo:  (n + 1)! = (n + 1) · n!     [definizione]
               ≥ (n + 1) · 2ⁿ⁻¹     [ipotesi induttiva]
               ≥ 2 · 2ⁿ⁻¹ = 2ⁿ      [n ≥ 1, quindi n + 1 ≥ 2]
```
! Trabocchetto: l'ultimo ≥ usa n ≥ 1: è l'ipotesi sul dominio che rende n + 1 ≥ 2.
> Vedi anche: Principio di induzione, Invariante del fattoriale

## Somma geometrica {38}
= Una **somma geometrica** è a + ar + ar² + … + arⁿ; se r ≠ 1 vale a(r^{n+1} − 1)/(r − 1), per ogni n ≥ 0.
- esempio: 3 + 6 + 12 + 24 = 3 · (2⁴ − 1)/(2 − 1) = 45
- il dominio parte da 0, quindi il passo base è n = 0: a = a(r¹ − 1)/(r − 1)
- con a = 1 e r = 2: 1 + 2 + … + 2ⁿ = 2^{n+1} − 1, come il binario fatto di n + 1 cifre uguali a 1
```
Passo:  a(rⁿ⁺¹ − 1)/(r − 1) + arⁿ⁺¹(r − 1)/(r − 1)
      = (arⁿ⁺¹ − a + arⁿ⁺² − arⁿ⁺¹)/(r − 1)
      = a(rⁿ⁺² − 1)/(r − 1)
```
! Trabocchetto: la formula vale solo per r ≠ 1: con r = 1 il denominatore r − 1 è zero.
> Vedi anche: Somme per induzione

## Divisibilità per induzione {38}
= Per ogni n ≥ 1, 5ⁿ − 1 è divisibile per 4: 4, 24, 124, …
- si usa che, se p e q sono divisibili per k, anche p + q lo è
- si scrive il caso n + 1 come il caso n più un pezzo da determinare, che deve essere multiplo di 4
- è lo stesso trucco delle somme: ritrovare il caso n dentro il caso n + 1
```
Base:   5¹ − 1 = 4
Passo:  5ⁿ⁺¹ − 1 = 5 · 5ⁿ − 1 = (5ⁿ − 1) + 4 · 5ⁿ
        multiplo di 4 per ipotesi induttiva + multiplo di 4
```
> Vedi anche: Principio di induzione, Somme per induzione

## Triomini sulla scacchiera deficiente {38, 42}
= Un **triomino** è una L di tre quadrati; una **scacchiera deficiente** è una scacchiera quadrata a cui manca un quadrato. **Teorema di Golomb**: ogni 2^{k} × 2^{k} deficiente si tassella con triomini, ovunque sia il buco.
![a sinistra una 4 × 4 deficiente con 5 triomini, a destra il passo induttivo sulla 8 × 8](figure/fond/induzione_golomb.png)
- il buco serve: 4, 16, 64 non sono multipli di 3, mentre 16 − 1 = 15 = 5 · 3
- base k = 1: la 2 × 2 deficiente è un triomino; passo: quattro quadranti, quello con il buco per ipotesi induttiva, e un triomino al centro copre un quadrato di ciascuno degli altri tre, che diventano deficienti
- **L di ordine n**: tre quadrati 2ⁿ × 2ⁿ a L, tassellata con 4ⁿ triomini; base: un triomino; passo: quattro L di ordine n, tre negli angoli e una al centro
- seconda prova di Golomb: il quadrante con il buco per ipotesi induttiva, gli altri tre insieme formano una L
- le prove sono **costruttive**: danno direttamente un programma ricorsivo
![le L di ordine 0, 1 e 2](figure/fond/induzione_L_triomini.png)
! Trabocchetto: il triomino centrale va messo negli angoli che si toccano al centro dei tre quadranti **senza** buco.
> Vedi anche: Principio di induzione

## Induzione forte {41}
= Nel passo si possono assumere **tutti** i casi precedenti: se S(n_{0}) è vera e, per ogni n > n_{0}, S(k) per ogni n_{0} ≤ k < n implica S(n), allora S(n) vale per ogni n ≥ n_{0}.
- è equivalente all'induzione semplice, ma dà più materiale nel passo
- se il passo usa il caso n − p, servono p passi base
- francobolli da 2 e da 5 fanno ogni cifra da 4 in su: basi 4 = 2 + 2 e 5 = 5, poi n si fa da n − 2 aggiungendo un 2, per n ≥ 6
- comunque si mettano le parentesi, a_{1}a_{2}···a_{n} richiede n − 1 moltiplicazioni: l'ultima divide in gruppi di t e n − t fattori, e (t − 1) + (n − t − 1) + 1 = n − 1
- lì serve la forma forte perché non si sa dove cade la divisione
! Trabocchetto: da 12 = sei francobolli da 2 non si arriva a 13 aggiungendo un francobollo (servirebbe da 1): il caso n − 1 non basta, serve n − 2.
> Vedi anche: Principio di induzione, Potenza veloce

## Buon ordinamento {41, 39}
= **Proprietà del buon ordinamento**, o **principio del minimo**: ogni insieme **non vuoto** di interi non negativi ha un elemento minimo.
- è equivalente alle due forme dell'induzione
- si usa per assurdo: si prende il più piccolo numero per cui la proprietà è falsa e se ne trova uno ancora più piccolo
- conseguenza: in ℕ non esiste una discesa infinita n_{0} > n_{1} > n_{2} > …, cioè l'ordine è **ben fondato**
- con gli interi con segno non vale: tra i negativi non c'è un minimo
! Trabocchetto: senza «non vuoto» è falso, perché ∅ non ha minimo; limitarlo agli insiemi finiti è troppo poco.
> Vedi anche: Terminazione e correttezza totale

# Invarianti di ciclo

## Invariante di ciclo {39, 43}
= Un **invariante di ciclo** è un enunciato sulle variabili vero subito prima del ciclo e che, se vale prima di un'esecuzione del corpo, vale anche dopo.
- si prova per induzione sul **numero di esecuzioni del corpo**
- all'uscita valgono insieme l'invariante e la **negazione della condizione** del while: devono dare la **postcondizione**
- vale a giro completo: a metà corpo può essere falso
- gli invarianti veri sono tantissimi e quasi tutti inutili; trovare quello giusto è difficile, provarlo di solito è più facile
```
Base:    vale con i valori iniziali (zero esecuzioni)
Passo:   vale + condizione vera  ⇒  vale dopo il corpo
Uscita:  invariante + condizione falsa  ⇒  postcondizione
```
! Trabocchetto: nel passo induttivo non fare copia e incolla del passo base: i valori delle variabili sono diversi.
> Vedi anche: Invariante del fattoriale, Terminazione e correttezza totale

## Invariante del fattoriale {39}
= Il ciclo che porta fact a n! ha invariante **i ≤ n e fact = i!**, con n ≥ 1.
- base: i = 1 e fact = 1 = 1!, e i ≤ n perché n ≥ 1
- passo: il corpo gira solo se i₀ < n, quindi il nuovo i ≤ n; fact diventa i₀! · (i₀ + 1) = (i₀ + 1)!
- uscita: i ≥ n e i ≤ n danno i = n, quindi fact = n!; con n = 4 le coppie (i, fact) sono (1, 1), (2, 2), (3, 6), (4, 24)
- variante con il prodotto prima dell'incremento e `i <= n`: invariante fact = (i − 1)! e i ≤ n + 1, vale anche per n = 0
```c
int i = 1, fact = 1;
while (i < n) {
    i = i + 1;
    fact = fact * i;   // fact vecchio, i nuovo
}
```
! Trabocchetto: con il solo fact = i!, all'uscita si sa soltanto i ≥ n, e non che fact contiene proprio n!.
> Vedi anche: Invariante di ciclo, Disuguaglianza del fattoriale

## Invariante della divisione intera {39}
= Togliendo D da X finché si può, q conta le sottrazioni e r è ciò che resta; l'invariante è **X = q · D + r e r ≥ 0**.
- condizione di ingresso X ≥ 0 e D > 0; condizione di uscita X = q · D + r con r < D
- passo: (q + 1) · D + (r − D) = q · D + r = X; e r − D ≥ 0 perché il corpo gira solo se r ≥ D
- con X = 14 e D = 3 le coppie (q, r) sono (0, 14), (1, 11), (2, 8), (3, 5), (4, 2): quoziente 4, resto 2
```c
int q = 0, r = X;
while (r >= D) {
    r = r - D;
    q = q + 1;
}
```
! Trabocchetto: con D = 0 l'invariante si prova lo stesso, ma r non scende mai e il ciclo non termina.
> Vedi anche: Terminazione e correttezza totale

## Terminazione e correttezza totale {39, 41, 43}
= Un ciclo termina se c'è una **funzione di terminazione** T: un numero naturale che diminuisce strettamente a ogni esecuzione del corpo.
- funziona perché l'ordine di ℕ è **ben fondato**: niente discese infinite; che T resti naturale lo garantisce di solito l'invariante
- esempi: T = r nella divisione intera, n − i nel fattoriale e nella potenza, N − X nel quadrato, i nella potenza veloce
- **parzialmente corretto**: per ogni dato che soddisfa la condizione di ingresso, **se** termina, l'uscita soddisfa la condizione di uscita
- **totalmente corretto**: termina **e** l'uscita è giusta; l'invariante dà la parziale, la terminazione completa la totale
! Trabocchetto: un ciclo che gira per sempre è parzialmente corretto per qualunque condizione di uscita, ma non serve a niente.
> Vedi anche: Buon ordinamento, Invariante di ciclo

## Invariante della potenza {40}
= Il ciclo che moltiplica ris per a n volte ha invariante **i ≤ n e ris = a^{i}**, con n ≥ 0.
- base: i = 0 e ris = 1 = a⁰; passo: ris diventa a^{i₀} · a = a^{i₀+1}
- i ≤ n si mantiene grazie al test i < n; all'uscita i = n e ris = aⁿ
- con a = 2 e n = 5 le coppie (i, ris) sono (0, 1), (1, 2), (2, 4), (3, 8), (4, 16), (5, 32)
- versione del libro con il contatore da 1: invariante pow = a^{i−1} e i ≤ n + 1
- stessa prova senza ciclo: f(x, 0) = 1 e f(x, n) = x · f(x, n − 1) danno, per induzione, f(x, n) = xⁿ
```c
int i = 0;
double ris = 1;
while (i < n) {
    i = i + 1;
    ris = ris * a;
}
```
! Trabocchetto: con n negativo il ciclo non parte e restituisce 1, che non è aⁿ: senza n ≥ 0 il risultato è sbagliato.
> Vedi anche: Potenza veloce, Invariante del fattoriale

## Invariante del quadrato {40}
= Per calcolare N · N con sole somme si sceglie prima l'invariante **Y = X · X**, insieme a X ≤ N, e poi si scrive il corpo che lo conserva.
- passando da X a X + 1 il quadrato cresce di 2 · X + 1, quindi Y = Y + 2 · X + 1
- all'uscita X = N, quindi Y = N · N; con N = 4 le coppie (X, Y) sono (0, 0), (1, 1), (2, 4), (3, 9), (4, 16)
- il ciclo somma i primi N dispari: 1, 3, 5, 7
- stessa prova su una definizione ricorsiva: q(0) = 0 e q(n + 1) = q(n) + 2 · n + 1 danno q(n) = n · n
```c
int X = 0, Y = 0;
while (X < N) {
    Y = Y + 2 * X + 1;
    X = X + 1;
}
```
! Trabocchetto: Y va aggiornato **prima** di X, perché 2 · X + 1 usa il valore vecchio; incrementando prima X servirebbe 2 · X − 1.
> Vedi anche: Invariante della potenza, Somme per induzione

## Potenza veloce {43}
= Calcola bⁿ con i quadrati successivi b, b², b⁴, b⁸, … e mette in ris solo quelli che corrispondono a una cifra 1 dell'esponente in binario.
- `i % 2` legge l'ultima cifra binaria di i, `i / 2` la cancella
- invariante **ris · a^{i} = bⁿ e i ≥ 0**: la parte già calcolata per la parte ancora da calcolare
- passo per casi: con i = 2i₀ ris non cambia; con i = 2i₀ + 1 ris raccoglie il fattore a che la divisione «butta via»
- i giri sono le cifre binarie di n: 10 per 1000, 20 per un milione, 30 per un miliardo
- b = 3, n = 10: (i, a, ris) = (10, 3, 1), (5, 9, 1), (2, 81, 9), (1, 6561, 9), (0, 43 046 721, 59 049)
```c
double ris = 1, a = b;
int i = n;
while (i > 0) {
    if (i % 2 == 1)
        ris = ris * a;
    a = a * a;
    i = i / 2;
}
```
! Trabocchetto: l'invariante vale solo a giro completo: dopo `a = a * a` e prima di `i = i / 2` si ha 1 · 9^{10} = 3 486 784 401, non 3^{10} = 59 049.
> Vedi anche: Invariante della potenza, Terminazione e correttezza totale

## Somma degli elementi di un vettore {44}
= Con sum = v[0] e i = 1, l'invariante è **sum = v[0] + … + v[i − 1] e 1 ≤ i ≤ n**, con n ≥ 1.
- in sum ci sono gli elementi di indice da 0 a i − 1, non da 0 a i
- passo: il test dà i < n, quindi v[i] esiste e i + 1 ≤ n
- uscita: i ≥ n e i ≤ n danno i = n, quindi sum contiene tutti gli elementi
- passaggi leciti: **indebolire** (da 1 < i + 1 a 1 ≤ i + 1) e **sostituire uguali con uguali** (v[i] come v[(i + 1) − 1])
```c
int sum = v[0];
int i = 1;
while (i < n) {
    sum = sum + v[i];
    i = i + 1;
}
```
! Trabocchetto: quando i vale n non è più un indice ma il segnale di fine: leggere v[n] vuol dire uscire dal vettore.
> Vedi anche: Invariante di ciclo, Ricerca del primo zero

## Ricerca del primo zero {44}
= Il ciclo cerca il primo zero di v; l'invariante ha tre parti: **0 ≤ i ≤ n**, **v[0], …, v[i − 1] diversi da 0**, **se found è true allora i < n e v[i] = 0**.
- base: la seconda parte è un universale sull'insieme vuoto, quindi vera; la terza ha la premessa falsa, quindi vera
- passo per casi: v[i] = 0 cambia solo found, v[i] ≠ 0 cambia solo i
- uscita: per De Morgan vale i ≥ n oppure found = true
- found false: i = n e nel vettore non ci sono zeri; found true: v[i] è il primo zero
```c
int i = 0;
bool found = false;   // serve stdbool.h
while (i < n && found == false) {
    if (v[i] == 0) found = true;
    else i = i + 1;
}
```
! Trabocchetto: nel caso found = true, i < n va ricavato dalla terza parte dell'invariante, non dall'intuizione «in quel giro i non è cresciuto».
> Vedi anche: Mondo di Tarski e insieme vuoto, Somma degli elementi di un vettore

# Funzioni

## Funzione {45}
= Una **funzione** f: X → Y associa a ogni x ∈ X **esattamente una** y ∈ Y, indicata con f(x): da ogni punto di X esce una sola freccia.
![(a) e (b) non sono funzioni, (c) e (d) sì](figure/fond/funzioni_frecce.png)
- **ovunque definita**: da ogni x esce almeno una freccia; **funzionale**: ne esce al più una
- X è il **dominio**, Y il **codominio**; l'**immagine** {f(x) : x ∈ X} è contenuta nel codominio
- non serve usare tutti i punti di Y, e due x possono avere la stessa immagine
- esempio: x mod y, il resto della divisione, con 17 mod 5 = 2 e 365 mod 7 = 1
! Trabocchetto: la regola f(x) = x² da sola non definisce una funzione: servono anche dominio e codominio.
> Vedi anche: Funzione iniettiva, Funzione suriettiva

## Funzione iniettiva {45}
= f è **iniettiva** (~one-to-one~) se da f(x_{1}) = f(x_{2}) segue x_{1} = x_{2}: su ogni punto di Y arriva al più una freccia.
- in simboli ∀x_{1} ∀x_{2} (f(x_{1}) = f(x_{2}) → x_{1} = x_{2}); negata, ∃x_{1} ∃x_{2} (f(x_{1}) = f(x_{2}) ∧ x_{1} ≠ x_{2})
- per dimostrarla si suppone f(x_{1}) = f(x_{2}) e si deduce x_{1} = x_{2}: 3n_{1} + 2 = 3n_{2} + 2 dà n_{1} = n_{2}
- per confutarla basta un controesempio: per 2ⁿ − n² si ha f(2) = f(4) = 0
- cercare la ripetizione calcolando f(1), f(2), … è solo un **semi-algoritmo**: se la ripetizione non c'è, non si ferma mai
! Trabocchetto: funzionale guarda i punti di X, iniettiva i punti di Y: sono due condizioni diverse.
> Vedi anche: Funzione suriettiva, Funzione biiettiva

## Funzione suriettiva {45}
= f è **suriettiva** (~onto~) se ogni y ∈ Y è immagine di qualche x: l'immagine coincide con il codominio.
- in simboli ∀y ∃x f(x) = y, con x che può dipendere da y; negata, ∃y ∀x f(x) ≠ y
- per dimostrarla si prende y qualunque e si costruisce x: per g(x) = 5x − 3 si prende x = (y + 3)/5
- per confutarla si trova un y mai raggiunto: 2n − 1 sugli interi positivi non dà mai i pari
- dipende dal codominio: 2n − 1 verso i dispari positivi è suriettiva
! Trabocchetto: ~one-to-one~ vuol dire iniettiva, non suriettiva: suriettiva nel libro si dice ~onto~.
> Vedi anche: Funzione iniettiva, Funzione biiettiva

## Funzione biiettiva {45}
= Una **biiezione** è iniettiva e suriettiva: ogni punto di Y riceve esattamente una freccia.
- da un insieme finito in sé stesso è una **permutazione**; tra insiemi finiti dice che hanno lo stesso numero di elementi
- da ℤ a ℤ: n + 1 è biiettiva; 2n e n³ iniettive ma non suriettive; ⌈n/2⌉ suriettiva ma non iniettiva; n² − 1 e |n| nessuna delle due
- **principio dei cassetti**: tra insiemi finiti con |Y| < |X|, nessuna f: X → Y è iniettiva (13 persone, 12 mesi)
- per contrapposizione: se f è iniettiva tra insiemi finiti, |X| ≤ |Y|
! Trabocchetto: lo stesso numero di elementi non basta per l'iniettività, e con insiemi infiniti n ↦ 2n è iniettiva ma lascia fuori i dispari.
> Vedi anche: Funzione inversa

## Funzione inversa {46}
= Se f: X → Y è biiettiva, la **funzione inversa** f⁻¹: Y → X rovescia le frecce: f⁻¹(y) = x esattamente quando f(x) = y.
![a sinistra f e f⁻¹, a destra la composizione f ∘ g](figure/fond/inversa_composizione.png)
- rovesciando le frecce si ha una funzione **se e solo se** f è biiettiva; anche f⁻¹ è biiettiva
- f non iniettiva: da un punto escono due frecce rovesciate; non suriettiva: da un punto non ne esce nessuna
- con una formula si ricava x da y = f(x): 4x + 2 ha inversa (y − 2)/4, e infatti f(1) = 6, f⁻¹(6) = 1
- f = {(1, c), (2, a), (3, b)} dà f⁻¹ = {(c, 1), (a, 2), (b, 3)}; 2^{x} da ℝ a ℝ⁺ ha inversa log_{2} y
! Trabocchetto: f⁻¹ non è 1/f.
> Vedi anche: Composizione di funzioni, Funzione biiettiva

## Composizione di funzioni {46}
= Con g: X → Y e f: Y → Z, la **composizione** è (f ∘ g)(x) = f(g(x)): prima g, poi f.
- sul diagramma si seguono tutti i cammini: g = {(1, b), (2, c), (3, b)} e f = {(a, w), (b, u), (c, v)} danno f ∘ g = {(1, u), (2, v), (3, u)}
- l'ordine conta: con f(x) = x + 3 e g(x) = x² si ha f(g(1)) = 4 e g(f(1)) = 16
- composta di iniettive è iniettiva, di suriettive è suriettiva, di biiezioni è una biiezione
- f ∘ g iniettiva ⇒ g iniettiva; f ∘ g suriettiva ⇒ f suriettiva; non vale il contrario
! Trabocchetto: in f ∘ g si applica per prima g, anche se è scritta per seconda.
> Vedi anche: Funzione inversa

## Funzione caratteristica {46}
= Per X ⊆ U, la **funzione caratteristica** C_{X}: U → {0, 1} vale 1 se x ∈ X e 0 se x ∉ X.
- per un informatico rappresenta un insieme con un piccolo programma booleano, anche se l'insieme è infinito
- C_{X ∪ Y}(x) = C_{X}(x) + C_{Y}(x) per ogni x se e solo se X ∩ Y = ∅
- se x ∈ X ∩ Y la somma fa 2, mentre C_{X ∪ Y} vale solo 0 o 1
- con i pari e i dispari su ℤ l'uguaglianza vale: la somma fa sempre 1
! Trabocchetto: in C il test per i dispari è «resto diverso da zero»: -3 % 2 vale -1, non 1.
> Vedi anche: Funzione

# Sequenze

## Sequenza {47}
= Una **sequenza** è una funzione il cui dominio è un insieme di interi; s_{n} è l'elemento di **indice** n. È finita o infinita secondo il dominio.
- si rappresenta con una tabella, una formula o un programma
- taxi: C_{n} = 3 + 1,2(n − 1) euro per n chilometri, quindi C_{10} = 13,80
- l'indice è una **variabile locale**: u_{n} = n² − 1 e u_{m} = m² − 1 sono la stessa sequenza
- il dominio può contenere negativi: y_{n} = 3ⁿ per −2 ≤ n ≤ 2 dà 1/9, 1/3, 1, 3, 9
- Σ_{i=m}^{n} a_{i} e Π_{i=m}^{n} a_{i} sono somma e prodotto dei termini: con a_{i} = 2i − 1, da 1 a 4, fanno 16 e 105
! Trabocchetto: s_{n−1} ha senso solo se n − 1 sta nel dominio: con n ≥ 0, solo per n ≥ 1.
> Vedi anche: Formula diretta e ricorrenza, Stringa

## Formula diretta e ricorrenza {47}
= La **formula diretta** dà s_{n} a partire da n; l'**equazione di ricorrenza** lo dà a partire dai termini precedenti.
- s_{n} = 2ⁿ + 4 · 3ⁿ per n ≥ 0 dà 5, 14, 40, 116, e soddisfa s_{n} = 5s_{n−1} − 6s_{n−2} per n ≥ 2
- si dimostra sostituendo e scrivendo tutto con 2^{n−2} e 3^{n−2}
- per tutta la tabella conviene la ricorrenza (due prodotti e una sottrazione a termine); per un valore isolato con n grande, la formula diretta
- esercizio: r_{n} = 3 · 2ⁿ − 4 · 5ⁿ (−1, −14, −88) soddisfa r_{n} = 7r_{n−1} − 10r_{n−2}
```
5sₙ₋₁ − 6sₙ₋₂ = 5 · 2ⁿ⁻¹ + 20 · 3ⁿ⁻¹ − 6 · 2ⁿ⁻² − 24 · 3ⁿ⁻²
              = (10 − 6) · 2ⁿ⁻² + (60 − 24) · 3ⁿ⁻²
              = 4 · 2ⁿ⁻² + 36 · 3ⁿ⁻² = 2ⁿ + 4 · 3ⁿ = sₙ
```
! Trabocchetto: finché non è dimostrata, la ricorrenza è una domanda: non la si può usare come ipotesi.
> Vedi anche: Sequenza, Potenza veloce

## Monotonia di una sequenza {47}
= Per ogni i < j del dominio: **crescente** se s_{i} < s_{j}, **decrescente** se s_{i} > s_{j}, **non decrescente** se s_{i} ≤ s_{j}, **non crescente** se s_{i} ≥ s_{j}.
- non decrescente si dice anche **debolmente crescente**
- con indici consecutivi basta controllare i vicini, s_{i} e s_{i+1}
- 10, 10, 20, 20, 30, 30 è non decrescente; 100, 90, 90, 74, 74, 74, 30 è non crescente, ma non (strettamente) decrescente
- con un solo elemento valgono tutte e quattro: sono universali su un insieme vuoto di coppie
- 2ⁿ − n² è decrescente su {1, 2, 3} (1, 0, −1) e crescente per n ≥ 3 (−1, 0, 7, 28, …)
! Trabocchetto: «non decrescente» non è la negazione di «decrescente»: 1, 0, −1, 0 non ha nessuna delle quattro proprietà.
> Vedi anche: Mondo di Tarski e insieme vuoto, Sequenza

# Stringhe

## Stringa {48}
= Una **stringa** su un alfabeto finito X è una sequenza finita di elementi di X: contano le lettere e il loro ordine.
- la **stringa vuota** λ non ha elementi; X* sono tutte le stringhe, compresa λ, e X⁺ quelle non vuote
- X* è infinito se X ha almeno una lettera, ma ogni strato di lunghezza fissata è finito: su {0, 1} quelle lunghe al più 3 sono 15
- la **lunghezza** |α| è il numero di caratteri, e |λ| = 0
- gli indici possono partire da 0 o da 1: si sceglie una numerazione e la si rispetta
! Trabocchetto: in b²a³c l'esponente non è una potenza ma una ripetizione di lettere: |b^{20}a⁵ba| = 27.
> Vedi anche: Concatenazione e rovesciata, Sequenza

## Concatenazione e rovesciata {48}
= La **concatenazione** αβ è α seguita da β; la **rovesciata** α^{R} è α letta da destra a sinistra.
- αλ = λα = α e |αβ| = |α| + |β|
- l'ordine conta: con α = ro e β = ma si ha αβ = roma e βα = maro
- la concatenazione è un **operatore binario** su X*: prende due stringhe e restituisce una stringa
- (α^{R})^{R} = α; le stringhe con α = α^{R}, come radar, sono i palindromi
! Trabocchetto: la concatenazione non mette spazi in mezzo: uno spazio è un carattere da concatenare.
> Vedi anche: Rovesciamento e concatenazione come funzioni, Sottostringa e sottosequenza

## Sottostringa e sottosequenza {48, 47}
= β è **sottostringa** di α se α = γβδ, con γ e δ anche vuote: è un pezzo **contiguo**. Una **sottosequenza** tiene alcuni termini nello stesso ordine, anche non contigui.
- in banana, nan è una sottostringa (γ = ba, δ = a); bnn è solo una sottosequenza
- dai dispari 1, 3, 5, … tenendo i termini di posto dispari si ha 1, 5, 9, 13, …, con k-esimo termine 4k − 3
- le sottostringhe di babc sono 10: λ, a, b, c, ba, ab, bc, bab, abc, babc
- le sottostringhe servono, per esempio, a contare quante volte una parola compare in un testo
! Trabocchetto: 5, 1, 9 non è una sottosequenza dei dispari: gli elementi ci sono, ma l'ordine è cambiato.
> Vedi anche: Stringa, Sequenza

## Rovesciamento e concatenazione come funzioni {48}
= Il rovesciamento α ↦ α^{R} su X* è una biiezione; la concatenazione (α, β) ↦ αβ da X* × X* a X* è suriettiva ma non iniettiva.
- rovesciamento iniettivo: da α^{R} = β^{R}, rovesciando ancora, α = β
- rovesciamento suriettivo: dato β si sceglie il testimone α = β^{R} e si verifica (β^{R})^{R} = β; è un'**involuzione**, inversa di sé stessa
- concatenazione suriettiva con la coppia (γ, λ), che va bene anche per γ = λ
- non iniettiva: f(a, b) = ab = f(ab, λ), con due coppie diverse
- su {a, b}, α ↦ αab e α ↦ αα sono iniettive ma non suriettive
! Trabocchetto: per la suriettività non si ricava α dalla tesi α^{R} = β: si sceglie il testimone, poi si verifica che funziona.
> Vedi anche: Funzione biiettiva, Funzione suriettiva

## Stringa come funzione {49}
= Una stringa di lunghezza n ≥ 0 è una funzione α : [1, n] → X, con α(i) il carattere di posto i; la rovesciata è α^{R}(i) = α(n + 1 − i), della stessa lunghezza.
- n + 1 − i è il «contatore all'indietro»: per i da 1 a n va da n a 1, quindi resta dentro [1, n]
- per n = 0 gli indici sono vuoti e la stringa è λ
- esempio: α = assi, n = 4, α^{R}(1) = α(4) = i, …, α^{R} = issa
- due stringhe sono uguali se hanno la stessa lunghezza e lo stesso carattere in ogni posizione
- concatenazione: (αβ)(i) = α(i) per i ≤ n e β(i − n) per n < i ≤ n + m
> Vedi anche: Concatenazione e rovesciata, Espandere le definizioni

## Espandere le definizioni {49}
= Per dimostrare (α^{R})^{R} = α si **espandono le definizioni** e si fa algebra: è un metodo meccanico, quello che serve a una macchina per una risposta certa e non solo plausibile.
- tesi carattere per carattere: per ogni i ∈ [1, n], (α^{R})^{R}(i) = α(i)
- rovesciata esterna: (α^{R})^{R}(i) = α^{R}(n + 1 − i)
- rovesciata interna, come **istanza** di α^{R}(k) = α(n + 1 − k) con k = n + 1 − i: α(n + 1 − (n + 1 − i)) = α(i)
- ricetta: scrivere la tesi, espandere dalla definizione più esterna, fare le istanze, semplificare
- con lo stesso metodo, per casi, (αβ)^{R} = β^{R}α^{R}: (roma)^{R} = amor = am · or
! Trabocchetto: l'espressione va sostituita tutta, tra parentesi: n + 1 − n + 1 − i fa 2 − i, non i.
> Vedi anche: Stringa come funzione, Rovesciamento e concatenazione come funzioni, Dimostrazione diretta

# Relazioni

## Relazione e grafo diretto {50}
= Una **relazione** R da X a Y è un sottoinsieme di X × Y; si scrive x R y se (x, y) ∈ R. Se X = Y è una relazione su X.
![il grafo di R = {(a, a), (b, c), (c, b), (d, d)}: cappi in a e d, due frecce opposte tra b e c](figure/fond/relazione_abcd.png)
- **grafo diretto**: un punto per elemento e una freccia da x a y per ogni coppia (x, y)
- una coppia (x, x) è un **cappio** (loop), una freccia che torna nel punto
- una funzione è una relazione in cui da ogni elemento di X parte esattamente una coppia
- elenco di coppie e disegno sono equivalenti: il disegno spesso fa vedere subito la risposta
> Vedi anche: Proprietà delle relazioni, Funzione

## Proprietà delle relazioni {50}
= Le quattro proprietà sono universali; la loro negazione (De Morgan) dice quale controesempio cercare.
- **riflessiva** ∀x (x, x) ∈ R: un cappio su ogni punto; no se un x non ha il cappio
- **simmetrica** ∀x, y ((x, y) ∈ R → (y, x) ∈ R): ogni freccia ha il ritorno
- **antisimmetrica** ∀x, y ((x, y) ∈ R ∧ (y, x) ∈ R → x = y): tra punti distinti al più una freccia
- **transitiva** ∀x, y, z ((x, y) ∈ R ∧ (y, z) ∈ R → (x, z) ∈ R): per ogni cammino di due frecce c'è la scorciatoia
- R = {(a, a), (b, c), (c, b), (d, d)}: non riflessiva (b), simmetrica, non antisimmetrica (b ≠ c), non transitiva ((b, b) ∉ R)
- valgono o non valgono «perfettamente»: un solo controesempio le rende false
! Trabocchetto: antisimmetrica non vuol dire «non simmetrica»: {(a, a), (b, b), (c, c)} è entrambe, {(1, 2), (2, 1), (2, 3)} nessuna delle due.
> Vedi anche: Relazione e grafo diretto, De Morgan per i quantificatori, Controesempio

## Relazione d'ordine {51}
= Una **relazione d'ordine** (ordine parziale, x ≼ y) è riflessiva, antisimmetrica e transitiva; è **totale** se due elementi qualunque sono **confrontabili**, x ≼ y oppure y ≼ x.
![(a) ≤ su {1, 2, 3, 4}, (b) un'equivalenza con classi {1, 3, 5}, {2, 6}, {4}, (c) l'uguaglianza su {a, b, c}](figure/fond/ordine_equivalenza.png)
- esempi: ≤ sugli interi (totale); divisibilità sui positivi e ⊆ sui sottoinsiemi di {a, b, c} (non totali)
- {a} e {b} non sono confrontabili per ⊆, 2 e 3 non lo sono per la divisibilità
- nel grafo, passati a un elemento distinto non si torna più indietro; senza i cappi di ≤ resta l'ordine stretto <
- in informatica gli ordini sono quasi sempre parziali: una scelta può migliorare alcuni parametri e peggiorarne altri
! Trabocchetto: «ordine» non vuol dire «ordine totale»: l'inclusione è un ordine anche se due insiemi possono non essere confrontabili.
> Vedi anche: Proprietà delle relazioni, Relazione di equivalenza, Doppia inclusione

## Relazione di equivalenza {51}
= Una **relazione di equivalenza** è riflessiva, simmetrica e transitiva: rispetto a un ordine, la simmetria prende il posto dell'antisimmetria.
- divide l'insieme in **classi di equivalenza**: dentro una classe ci si muove liberamente, ma non si passa mai a un'altra
- esempio: su {1, …, 6} le classi {1, 3, 5}, {2, 6}, {4}; da 3 a 5 e da 5 a 1 c'è già la freccia da 3 a 1
- l'unica relazione che è insieme ordine ed equivalenza è l'**uguaglianza** {(x, x) : x ∈ X}
- dimostrazione: se a R b, per simmetria b R a, per antisimmetria a = b; la riflessività dà tutti i cappi, e si chiude per doppia inclusione
- l'uguaglianza è l'ordine più piccolo, che non ordina niente: non totale appena ci sono due elementi distinti
> Vedi anche: Relazione d'ordine, Doppia inclusione

## Quantificatori su un grafo di frecce {52}
= Nei quiz d'esame su un grafo si traduce ogni formula in una frase sul disegno, poi si cerca un testimone (∃) o un controesempio (∀).
![D = {1, …, 10}, A = {6, 7, 8}, B = {3, 4, 5}: una freccia da a a b vuol dire a R b](figure/fond/grafo_dieci_punti.png)
- ∀x ∈ A ∃y ∈ B x R y, «ogni punto di A ha una freccia verso B»: vera (6 → 3, 7 → 4, 8 → 5)
- ∀x ∈ A ∀y ∈ A ∃z ∈ B (x R z ∧ y R z), «immagine comune in B»: falsa con 7 e 8
- ∃x ∀y y R x vorrebbe dieci frecce entranti: falsa; ∃x ∀y ¬(y R x) vale con il 9, che non riceve frecce
- **confluenza** ∀x ∀y ∀z (x R y ∧ x R z → ∃u (y R u ∧ z R u)): falsa, per esempio con x = 3 e y = z = 1, da cui non esce nessuna freccia
- contare le frecce entranti e uscenti spesso risponde subito
! Trabocchetto: con ∨ al posto di ∧ la formula sull'immagine comune diventa vera; e in ∀x ∀y anche il caso x = y va controllato.
> Vedi anche: Quantificatori annidati, Dimostrare o confutare un annidato, Funzione suriettiva
