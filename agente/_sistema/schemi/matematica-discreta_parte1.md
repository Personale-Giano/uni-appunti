# Insiemi e operazioni

## Insieme {1, 7}
= Un **insieme** è una collezione ben determinata di oggetti distinti, gli **elementi**: per ogni oggetto si deve poter dire senza dubbi se c'è dentro oppure no.
- **criterio di oggettività**: «gli studenti presenti in aula» è un insieme, «gli attori bravi» no, perché «bravo» è un'opinione
- niente ripetizioni e ordine irrilevante: {a, b, c} = {b, a, c}
- **per elencazione** (estensionale): A = {a, b, c, 1, 6, 8}; **per proprietà** (intensionale): X = {x ∈ U | P(x)}, come B = {n ∈ ℕ | 1 ≤ n ≤ 10^{9}}
- x ∈ A: x appartiene ad A; x ∉ A: non appartiene
- insiemi numerici: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ; la matematica discreta lavora soprattutto su ℕ e ℤ
! Trabocchetto: una ripetizione nell'elenco non aggiunge elementi: {2, 1, 1} ha due elementi ed è uguale a {1, 2}.
> Vedi anche: Insieme vuoto e cardinalità, Sottoinsieme

## Insieme vuoto e cardinalità {2}
= L'**insieme vuoto** ∅ (o {}) è l'unico insieme senza elementi; la **cardinalità** |A| è il numero dei suoi elementi distinti.
- ne esiste uno solo: due scatole vuote non hanno nulla che le distingua
- |∅| = 0, |{a, b, c}| = 3; per gli insiemi infiniti, come ℕ, si scrive per ora |A| = ∞ (il cap. 25 li distingue)
- ∅ è sottoinsieme di qualunque insieme: non ha elementi che possano violare l'inclusione
- {∅} non è vuoto: è una scatola che contiene una scatola vuota, e ha un elemento
! Trabocchetto: |{∅}| = 1, non 0: ∅ ∈ {∅} come elemento.
> Vedi anche: Appartenenza e inclusione, Insieme delle parti

## Sottoinsieme {2}
= S ⊆ T se ogni elemento di S sta anche in T: ∀x ∈ S, x ∈ T.
- per negarlo basta un elemento: S ⊄ T vuol dire ∃x ∈ S tale che x ∉ T
- A ⊆ A e ∅ ⊆ A per ogni A; se S ⊆ T allora |S| ≤ |T|
- ∅ e A sono i sottoinsiemi **banali**; S è **proprio** se S ⊆ A e S ≠ A, come {1} in {1, 2}
- nei riassunti ⊂ è l'inclusione stretta, come in ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
! Trabocchetto: nel libro e negli esercizi d'esame ⊂ vuol dire ⊆: lì «A ⊂ A» è vera e si trova scritto «∅ ⊂ A».
> Vedi anche: Doppia inclusione, Appartenenza e inclusione

## Appartenenza e inclusione {2}
= ∈ lega un elemento a un insieme, ⊆ lega due insiemi: sono due livelli diversi, come scatole cinesi.
![A è un elemento di B, ma 1 non lo è](figure/mate/ch02_scatole_cinesi.png)
- con A = {1, 2} e B = {A, 3}: A ∈ B, ma 1 ∉ B e 2 ∉ B
- A ∈ B non implica A ⊆ B
- una graffa in più cambia l'oggetto: a è un elemento, {a} è l'insieme che contiene a
! Trabocchetto: gli elementi di un elemento non sono elementi: 1 ∈ A e A ∈ B non danno 1 ∈ B.
> Vedi anche: Sottoinsieme, Insieme vuoto e cardinalità

## Doppia inclusione {2, 3}
= Due insiemi sono uguali se hanno esattamente gli stessi elementi: A = B ⟺ (A ⊆ B ∧ B ⊆ A).
- prima inclusione: si prende x ∈ A qualunque e si deduce x ∈ B
- seconda inclusione: si prende y ∈ B qualunque e si deduce y ∈ A
- in alternativa una catena di ⟺ sulle definizioni: x ∈ (X ∩ Y) ∩ Z ⟺ (x ∈ X ∧ x ∈ Y) ∧ x ∈ Z ⟺ x ∈ X ∩ (Y ∩ Z)
! Trabocchetto: un diagramma di Venn dà l'intuizione ma non è una dimostrazione formale.
> Vedi anche: Unione e intersezione, Leggi di De Morgan

## Unione e intersezione {3}
= X ∩ Y = {x | x ∈ X ∧ x ∈ Y} tiene gli elementi comuni; X ∪ Y = {x | x ∈ X ∨ x ∈ Y} li mette tutti insieme, senza doppioni.
- tra {1, 2, 3} e {2, 3, 4}: intersezione {2, 3}, unione {1, 2, 3, 4}
- **disgiunti**: X ∩ Y = ∅, come pari e dispari
- per una famiglia {A_{i}}: l'unione chiede ∃i con x ∈ A_{i}, l'intersezione ∀i
- con A_{n} = (−1/n, 1/n), n ≥ 1: ⋃ A_{n} = (−1, 1) e ⋂ A_{n} = {0}; con B_{n} = (−n, n), n ≥ 1: ⋃ B_{n} = ℝ e ⋂ B_{n} = (−1, 1)
- intervalli: (a, b) esclude gli estremi, [a, b] li include
! Trabocchetto: ⋂ (−1/n, 1/n) non è vuota: 0 sta in tutti gli intervalli, ogni x ≠ 0 esce appena 1/n ≤ |x|.
> Vedi anche: Proprietà di unione e intersezione, Prodotto cartesiano

## Proprietà di unione e intersezione {3}
= Unione e intersezione sono **commutative** e **associative**, e ciascuna è **distributiva** rispetto all'altra.
- si dimostrano per doppia inclusione, usando le proprietà di ∧ e ∨
- distributività: da x ∈ (X ∪ Y) ∩ Z segue x ∈ Z e x ∈ X oppure x ∈ Y; nei due casi x ∈ X ∩ Z oppure x ∈ Y ∩ Z
```
X ∩ Y = Y ∩ X                 X ∪ Y = Y ∪ X
(X ∩ Y) ∩ Z = X ∩ (Y ∩ Z)     (X ∪ Y) ∪ Z = X ∪ (Y ∪ Z)
(X ∪ Y) ∩ Z = (X ∩ Z) ∪ (Y ∩ Z)
(X ∩ Y) ∪ Z = (X ∪ Z) ∩ (Y ∪ Z)
```
! Trabocchetto: nei numeri solo il prodotto distribuisce sulla somma; negli insiemi valgono **entrambe** le distributive.
> Vedi anche: Unione e intersezione, Doppia inclusione

## Prodotto cartesiano {3, 22}
= A × B = {(a, b) | a ∈ A ∧ b ∈ B}: tutte le **coppie ordinate** con il primo elemento in A e il secondo in B.
- {1, 2} × {a, b} = {(1, a), (1, b), (2, a), (2, b)}
- l'ordine conta: se a ≠ b, (a, b) ≠ (b, a)
- le coppie si dispongono in una griglia m × n: |A × B| = |A| · |B|
- ∅ × B = A × ∅ = ∅; con n insiemi si hanno le n-uple e |A_{1} × … × A_{n}| = |A_{1}| · … · |A_{n}|
! Trabocchetto: non è l'unione: A ∪ B mette insieme gli elementi, A × B costruisce oggetti nuovi, le coppie.
> Vedi anche: Metodo delle scelte successive, Relazione binaria

## Differenza e complementare {4}
= A ∖ B = {x | x ∈ A ∧ x ∉ B}; se S ⊆ A, A ∖ S si chiama **complementare** di S in A, 𝒞_{A}(S).
![la differenza non è commutativa](figure/mate/ch04_differenza.png)
- con A = {1, 2} e B = {2, 3}: A ∖ B = {1}, B ∖ A = {3}
- 𝒞_{A}(∅) = A, 𝒞_{A}(A) = ∅, 𝒞_{A}(𝒞_{A}(S)) = S
- S ∩ 𝒞_{A}(S) = ∅ e S ∪ 𝒞_{A}(S) = A
- la differenza si fa sempre, A ∖ B = A ∖ (A ∩ B); il complementare chiede S ⊆ A; esempio 𝒞_{ℝ}(ℚ) = irrazionali
! Trabocchetto: nel libro il complementare è 𝒞_{X}(A), con X l'universo: lettere scambiate, stessa definizione.
> Vedi anche: Leggi di De Morgan

## Leggi di De Morgan {4}
= Il complementare scambia unione e intersezione: 𝒞(S ∪ T) = 𝒞(S) ∩ 𝒞(T) e 𝒞(S ∩ T) = 𝒞(S) ∪ 𝒞(T).
![in ogni riga le due regioni azzurre coincidono](figure/mate/ch04_de_morgan.png)
- si dimostrano con la catena di ⟺ e le leggi logiche ¬(P ∨ Q) ⟺ ¬P ∧ ¬Q e ¬(P ∧ Q) ⟺ ¬P ∨ ¬Q
- valgono per famiglie qualunque: 𝒞(⋃ S_{i}) = ⋂ 𝒞(S_{i}), con ∃ e ∀ che si scambiano
- versione con la differenza, per insiemi qualunque: X ∖ (S ∪ T) = (X ∖ S) ∩ (X ∖ T) e X ∖ (S ∩ T) = (X ∖ S) ∪ (X ∖ T)
! Trabocchetto: 𝒞(S ∪ T) non è 𝒞(S) ∪ 𝒞(T): negando, anche l'operazione va scambiata.
> Vedi anche: Differenza e complementare, Doppia inclusione

## Insieme delle parti {4, 5}
= 𝒫(A) = {S | S ⊆ A}, scritto anche 2^{A}: i suoi elementi sono **tutti** i sottoinsiemi di A, compresi ∅ e A.
![𝒫({a, b, c}) ha 8 elementi](figure/mate/ch04_insieme_parti.png)
- ∅ ∈ 𝒫(A) e A ∈ 𝒫(A) per ogni A; 𝒫(∅) = {∅} ha un elemento
- se |A| = n allora |𝒫(A)| = 2^{n}: 1, 2, 4, 8 per n = 0, 1, 2, 3
- prova per induzione: i sottoinsiemi senza a_{n+1} sono 2^{n}, quelli con a_{n+1} altrettanti, 2^{n} + 2^{n} = 2^{n+1}
- 𝒫(A) ∩ 𝒫(B) = 𝒫(A ∩ B)
! Trabocchetto: con A = {1, 3} e B = {2, 5} si ha 𝒫(A) ∩ 𝒫(B) = {∅}, non ∅: due insiemi delle parti non sono mai disgiunti.
> Vedi anche: Principio di induzione, Insieme vuoto e cardinalità

# Naturali e induzione

## Assiomi di Peano {5}
= ℕ = {0, 1, 2, …} si caratterizza con lo 0 e una funzione **successore** S: ℕ → ℕ, con S(n) = n + 1, che soddisfano cinque assiomi.
- 0 ∈ ℕ; ogni n ha un unico successore S(n) ∈ ℕ
- il successore è iniettivo: m ≠ n ⟹ S(m) ≠ S(n)
- 0 non è successore di nessuno: S(n) ≠ 0
- **assioma di induzione**: se U ⊆ ℕ, 0 ∈ U e n ∈ U ⟹ S(n) ∈ U, allora U = ℕ
! Trabocchetto: i primi quattro non bastano: ℕ più una seconda catena …, −1′, 0′, 1′, … li soddisfa; il quinto dice che ogni naturale si raggiunge da 0.
> Vedi anche: Principio di induzione

## Principio di induzione {5}
= Per dimostrare P(n) per ogni n ≥ n_{0}: **base**, P(n_{0}) vera; **passo induttivo**, se P(n) è vera allora lo è P(n + 1).
![l'effetto domino](figure/mate/ch05_domino.png)
- nel passo P(n) è l'**ipotesi induttiva**, per un n generico; P(n + 1) è la **tesi induttiva**
- è l'effetto domino: la base fa cadere la prima tessera, il passo trascina tutte le altre
- discende dal quinto assioma con U = {n ∈ ℕ | P(n) è vera}
- la base può essere 0, 1 o un qualunque n_{0}: la proprietà vale per n ≥ n_{0}
! Trabocchetto: senza la base il passo non prova niente: la base va controllata sul primo valore del dominio.
> Vedi anche: Esempi di induzione, Assiomi di Peano

## Esempi di induzione {5}
= Nel passo si scrive il caso n + 1 come il caso n più un pezzo, e si usa l'ipotesi induttiva.
- 1^{2} + 2^{2} + … + n^{2} = n(n + 1)(2n + 1)/6 per n ≥ 1; base: 1 = 1 · 2 · 3/6
- n^{2} > 2n + 1 per n ≥ 3: base 9 > 7; passo (n + 1)^{2} = n^{2} + 2n + 1 > 4n + 2 ≥ 2(n + 1) + 1
- 2^{n} > n^{2} per n ≥ 5: base 32 > 25; passo 2^{n+1} = 2 · 2^{n} > 2n^{2} > n^{2} + 2n + 1
```
Passo dei quadrati:
n(n+1)(2n+1)/6 + (n+1)² = (n+1)(2n² + 7n + 6)/6
                        = (n+1)(n+2)(2n+3)/6     ← formula per n + 1
```
! Trabocchetto: la base giusta conta: n^{2} > 2n + 1 è falsa per n = 2 (4 < 5) e 2^{n} > n^{2} è falsa per n = 4 (16 = 16).
> Vedi anche: Principio di induzione, Insieme delle parti

# Ricoprimenti e partizioni

## Ricoprimento {6}
= Una famiglia di sottoinsiemi {A_{i}} di S è un **ricoprimento** di S se ⋃ A_{i} = S: i pezzi coprono tutto, anche sovrapponendosi.
![un ricoprimento di ℕ](figure/mate/ch06_ricoprimento.png)
- esempio su ℕ: A_{1} = {0, …, 1000}, A_{2} = {100, …, 10 000}, A_{3} = {n > 1000}
- A_{1} e A_{2} condividono i numeri da 100 a 1000: è permesso
- in ℝ gli intervalli [n, n + 1], n ∈ ℤ, sono un ricoprimento
! Trabocchetto: un ricoprimento non è per forza una partizione: i pezzi possono sovrapporsi.
> Vedi anche: Partizione

## Partizione {6}
= Una **partizione** di S è un ricoprimento con **blocchi** non vuoti e a due a due disgiunti: ogni elemento sta in uno e un solo blocco.
![3 sta in entrambi: non è una partizione](figure/mate/ch06_non_partizione.png)
- tre condizioni: ⋃ A_{i} = S, A_{i} ≠ ∅, A_{i} ∩ A_{j} = ∅ per i ≠ j
- pari e dispari sono una partizione di ℕ; {A, 𝒞_{S}(A)} lo è se A ≠ ∅ e A ≠ S
- {1, 2, 3} e {3, 4, 5} coprono {1, …, 5} ma non sono una partizione: si toccano in 3
- [n, n + 1] non sono una partizione di ℝ, perché n + 1 sta in due intervalli; [n, n + 1) sì
! Trabocchetto: {{1, 2}, {3, 4}, ∅} non è una partizione di {1, 2, 3, 4}: un blocco vuoto non è ammesso.
> Vedi anche: Ricoprimento, Insieme quoziente, Equivalenze e partizioni

## Insieme quoziente {7, 9}
= L'**insieme quoziente** Q (o S/R) ha come elementi i blocchi della partizione: ogni blocco diventa un unico oggetto.
![ogni blocco diventa un elemento di Q](figure/mate/ch07_insieme_quoziente.png)
- ogni blocco è un sottoinsieme di S, quindi Q ⊆ 𝒫(S)
- per pari e dispari Q = {P, D}: |Q| = 2 anche se P e D sono infiniti
- con una relazione di equivalenza R: S/R = {C_{x} | x ∈ S}, l'insieme delle classi
- nel libro la famiglia di blocchi si chiama 𝒜, per non confonderla con 𝒫(S)
! Trabocchetto: Q ⊆ 𝒫(S), non Q ⊆ S: gli elementi di Q sono insiemi di elementi di S.
> Vedi anche: Partizione, Equivalenze e partizioni, Funzioni notevoli

# Relazioni ed equivalenze

## Relazione binaria {8}
= Una **relazione binaria** su S è un sottoinsieme R ⊆ S × S; se (x, y) ∈ R si scrive x R y.
![la divisibilità su {1, 2, 3, 6} come grafo](figure/mate/ch08_relazione_divisibilita.png)
- ≤ su ℤ è {(m, n) | m ≤ n}: (1, 3) ∈ R, (2, −4) ∉ R
- divisibilità m | n: 3 | 9 vero, 3 | 5 falso
- sulle rette del piano: parallelismo ∥ e perpendicolarità ⊥
- si usa una coppia ordinata perché l'ordine conta: 3 ≤ 7 è vera, 7 ≤ 3 no
! Trabocchetto: x R y e y R x sono affermazioni diverse: la coppia (x, y) non è la coppia (y, x).
> Vedi anche: Proprietà delle relazioni, Prodotto cartesiano

## Proprietà delle relazioni {8}
= Quattro proprietà: **riflessiva** ∀x x R x; **simmetrica** x R y ⟹ y R x; **antisimmetrica** (x R y ∧ y R x) ⟹ x = y; **transitiva** (x R y ∧ y R z) ⟹ x R z.
- ≤ è riflessiva, antisimmetrica e transitiva, ma non simmetrica (2 ≤ 4, 4 ≰ 2)
- =, ∥ e ⊥ sono simmetriche; =, ≤, divisibilità e ∥ sono transitive
- ⊥ non è transitiva: r ⊥ s e s ⊥ t danno r ∥ t
- la divisibilità è antisimmetrica su ℕ, non su ℤ: 1 | −1 e −1 | 1 ma 1 ≠ −1
! Trabocchetto: le proprietà dipendono anche dall'insieme: la stessa regola può essere antisimmetrica su ℕ e non su ℤ.
> Vedi anche: Relazione di equivalenza, Relazione binaria

## Relazione di equivalenza {8}
= Una relazione è **di equivalenza** se è riflessiva, simmetrica e transitiva: due elementi sono «uguali sotto un certo punto di vista».
- esempi: = su qualunque insieme, il parallelismo tra rette, la congruenza tra figure, «avere la stessa parità» su ℤ
- ≤ non lo è: manca la simmetria
- la divisibilità non lo è: non è simmetrica
- per verificarla si controllano tutte e tre le proprietà; per smentirla basta che ne manchi una
! Trabocchetto: ⊥ è simmetrica ma non transitiva, quindi non è un'equivalenza: una proprietà sola non basta.
> Vedi anche: Classe di equivalenza, Proprietà delle relazioni

## Classe di equivalenza {9}
= La **classe di equivalenza** di x è C_{x} = [x] = x̄ = {y ∈ S | x R y}: tutti gli elementi equivalenti a x.
- x è il **rappresentante**; va bene qualunque altro elemento della classe
- con la stessa parità, la classe di 3 è l'insieme dei dispari: [3] = [5] = [7]
- x ∈ C_{x} per la riflessività, quindi nessuna classe è vuota
- ogni x sta nella propria classe, quindi l'unione delle classi è S
! Trabocchetto: [3] e [5] non sono due classi diverse: sono due nomi della stessa classe.
> Vedi anche: Equivalenze e partizioni, Funzioni sul quoziente

## Equivalenze e partizioni {9}
= Due classi di equivalenza o sono disgiunte o coincidono: C_{x} ∩ C_{y} = ∅ oppure C_{x} = C_{y}. Quindi le classi formano una partizione di S.
![stesso blocco ⟺ x R y](figure/mate/ch09_partizione_relazione.png)
- prova: se z sta in entrambe, x R z e y R z; simmetria e transitività danno x R y, poi C_{y} ⊆ C_{x} e viceversa
- S/R = {C_{x} | x ∈ S} ⊆ 𝒫(S) è l'insieme quoziente
- viceversa, da una partizione: x R y se e solo se x e y stanno nello stesso blocco
- relazioni di equivalenza su S e partizioni di S si corrispondono biunivocamente
! Trabocchetto: due classi non si sovrappongono mai solo in parte: un solo elemento comune le rende uguali.
> Vedi anche: Partizione, Insieme quoziente, Classe di equivalenza

# Funzioni

## Funzione {9, 10}
= Una **funzione** f: A → B è data da dominio A, codominio B e **grafico** Γ ⊆ A × B con ∀a ∈ A ∃! b ∈ B tale che (a, b) ∈ Γ; si scrive f(a) = b.
- **esistenza**: da ogni a parte una freccia; **unicità**: ne parte una sola (una retta verticale taglia il grafico in un punto)
- il dominio si assegna, non si calcola: 1/x è una funzione da ℝ ∖ {0} in ℝ, non da ℝ in ℝ
- non sono funzioni: n ↦ ±√n (due valori), √x da ℝ in ℝ (nessun valore per x < 0), x/2 da {1, 2, 3} in ℤ (1/2 ∉ ℤ)
- notazioni: f: A → B per dominio e codominio, x ↦ f(x) per il singolo elemento
! Trabocchetto: valori ripetuti sono ammessi (con A = {a, b, c, d}, f(a) = f(b) = 2 va bene): è vietato solo un elemento con due valori o con nessuno.
> Vedi anche: Uguaglianza di funzioni, Funzioni notevoli

## Uguaglianza di funzioni {10, 11}
= f = (A, B, Γ) e g = (A′, B′, Γ′) sono uguali solo se A = A′, B = B′ e Γ = Γ′.
![stesso grafico su {0, 1, 2}, diverse su ℝ](figure/mate/ch10_f_uguale_g.png)
- su {0, 1, 2} con codominio ℝ, f(x) = 3x^{2} − 1 e g(x) = x^{3} + 2x − 1 valgono entrambe −1, 2, 11: f = g
- espressioni diverse possono dare la stessa funzione
- la stessa espressione con dominio o codominio diversi dà funzioni diverse
- per iniettività e suriettività dominio e codominio vanno sempre dichiarati
! Trabocchetto: la sola formula non basta a dare una funzione: cambiando l'insieme di partenza o di arrivo cambiano anche le proprietà.
> Vedi anche: Funzione, Restrizione e successioni, Cambiare dominio e codominio

## Funzioni notevoli {11}
= Funzioni che ricorrono di continuo, descritte a parole ma sempre con dietro la tripla (A, B, Γ).
- **identità** id_{A}: A → A, id_{A}(a) = a; il grafico è la diagonale {(a, a) | a ∈ A}
- **costante** f_{β}: A → B, f_{β}(a) = β per ogni a
- **proiezioni** p_{1}: A × B → A, p_{1}(a, b) = a, e p_{2}(a, b) = b
- **inclusione canonica** j: S → A, j(s) = s, se S ⊆ A
- **funzione quoziente** q: X → X/∼, q(x) = [x]: suriettiva, e q(x) = q(y) ⟺ x ∼ y
! Trabocchetto: l'inclusione canonica coincide con id_{A} solo se S = A: altrimenti ha un altro dominio ed è un'altra funzione.
> Vedi anche: Funzione, Insieme quoziente, Restrizione e successioni

## Restrizione e successioni {11}
= Se S ⊆ A, la **restrizione** f|_{S}: S → B è f usata solo su S: f|_{S}(s) = f(s). Una **successione** è una funzione a: ℕ → ℝ, n ↦ a_{n}.
- f|_{S} ha gli stessi valori ma un dominio diverso, quindi è una funzione diversa da f
- f ≠ g può dare f|_{S} = g|_{S}: le due funzioni di Uguaglianza di funzioni, diverse su ℝ, coincidono ristrette a {0, 1, 2}
- una successione che parte da 1 ha dominio ℕ_{≥1}: formalmente è un'altra funzione
- esempio di successione: Fibonacci, 1, 1, 2, 3, 5, …
! Trabocchetto: restringere non conserva la diversità: due funzioni diverse possono diventare uguali.
> Vedi anche: Uguaglianza di funzioni, Cambiare dominio e codominio

## Funzioni sul quoziente {12}
= Una regola f([x]) = f̃(x) definita sui rappresentanti è **ben definita** solo se x ∼ y implica f̃(x) = f̃(y).
![stessa classe di partenza, due classi di arrivo](figure/mate/ch12_quoziente_non_ben_definita.png)
- ℕ diviso per numero di cifre: F([x]) = [2x] non va, perché [3] = [8] ma [6] ≠ [16]
- pari e dispari: G([x]) = (−1)^{x} va bene, perché x = y + 2n dà (−1)^{x} = (−1)^{y}
- pari e dispari: H([x]) = 3x verso ℤ non va, perché [0] = [2] ma 0 ≠ 6
- stesso controllo per ogni oggetto con più scritture: a/b ↦ b su ℚ non va, 1/2 = 2/4 dà 2 e 4
! Trabocchetto: davanti a una regola «sulla classe di x» la prima domanda è sempre se il risultato dipende dal rappresentante.
> Vedi anche: Classe di equivalenza, Funzioni notevoli

# Immagine e iniettività

## Immagine {13}
= L'**immagine** di S ⊆ A è f(S) = {f(s) | s ∈ S} ⊆ B; Im(f) = f(A) è l'immagine totale.
- con «raddoppia» e S = {1, 2, 3}: f(S) = {2, 4, 6}
- f(S) è un sottoinsieme del codominio, non di S
- ogni elemento ha una sola immagine
- se S ≠ ∅ allora f(S) ≠ ∅; f(∅) = ∅
- calcolarla vuol dire sostituire nell'espressione
! Trabocchetto: l'immagine di un insieme non vuoto non è mai vuota, la controimmagine sì.
> Vedi anche: Controimmagine e fibra, Funzione suriettiva

## Controimmagine e fibra {13}
= La **controimmagine** di T ⊆ B è f^{−1}(T) = {a ∈ A | f(a) ∈ T} ⊆ A; quella di un solo b, f^{−1}(b), è la **fibra** di b.
![per x² la controimmagine di [0, 4] è [−2, 2]](figure/mate/ch13_parabola.png)
- per x^{2} su ℝ: f^{−1}(b) = {−√b, √b} se b > 0, {0} se b = 0, ∅ se b < 0
- f^{−1}([−1, 4]) = f^{−1}([0, 4]) = [−2, 2]: la parte negativa non è mai raggiunta
- costante f_{β}: f_{β}^{−1}(T) è A se β ∈ T, ∅ altrimenti; p_{2}^{−1}(T) = A × T
- calcolarla vuol dire risolvere f(x) = y nell'incognita x
! Trabocchetto: f^{−1}(T) esiste per **ogni** funzione e f^{−1}(b) è un insieme, non un elemento: non vuol dire che f sia invertibile.
> Vedi anche: Immagine, Funzione inversa

## Funzione suriettiva {14}
= f: A → B è **suriettiva** se f(A) = B: ∀b ∈ B ∃a ∈ A con f(a) = b, cioè ogni fibra f^{−1}(b) è non vuota.
- in ogni elemento del codominio entra almeno una freccia
- per dimostrarla si risolve f(x) = y: 2x su ℝ è suriettiva con x = y/2
- per smentirla basta un y mai raggiunto: x^{2} su ℝ non dà −4
- log: ℝ_{>0} → ℝ è suriettivo; l'esponenziale da ℝ in ℝ no, non assume valori ≤ 0
! Trabocchetto: dipende dal codominio: la stessa espressione è suriettiva o no secondo l'insieme di arrivo.
> Vedi anche: Funzione iniettiva, Funzione biettiva, Cambiare dominio e codominio

## Funzione iniettiva {14, 16}
= f è **iniettiva** se elementi distinti hanno immagini distinte: a_{1} ≠ a_{2} ⟹ f(a_{1}) ≠ f(a_{2}), cioè |f^{−1}(b)| ≤ 1 per ogni b.
- forma comoda per dimostrarla: da f(x) = f(y) si deduce x = y
- 2n + 1 su ℤ è iniettiva: 2n_{1} + 1 = 2n_{2} + 1 dà n_{1} = n_{2}; ax + b con a ≠ 0 pure
- per smentirla basta una coppia: x^{2} su ℝ manda −1 e 1 in 1
- la proiezione p_{1}: A × B → A (B ≠ ∅) non è iniettiva, (1, 2) e (1, 5) vanno in 1, salvo |B| = 1
! Trabocchetto: l'iniettività dipende dal dominio, come la suriettività dal codominio: si guarda sempre l'insieme di partenza.
> Vedi anche: Funzione suriettiva, Funzione biettiva

## Funzione biettiva {14, 16}
= f è **biettiva** (corrispondenza biunivoca) se è iniettiva e suriettiva: ogni b ∈ B ha esattamente una controimmagine, |f^{−1}(b)| = 1.
![iniettiva, suriettiva, biettiva](figure/mate/ch14_tre_funzioni.png)
- le due condizioni sono indipendenti: si possono avere tutte e quattro le combinazioni
- biettive: id_{A}; x^{3} su ℝ; ax + b su ℝ con a ≠ 0; lo scambio (a, b) ↦ (b, a)
- p_{1}: A × B → A, con B ≠ ∅, è suriettiva ma in generale non iniettiva
! Trabocchetto: iniettiva non basta: 2n + 1 su ℤ è iniettiva, ma i pari non sono raggiunti.
> Vedi anche: Funzione inversa, Cambiare dominio e codominio

## Cambiare dominio e codominio {17, 14, 16}
= Riducendo il codominio a ciò che si raggiunge la funzione diventa suriettiva; restringendo il dominio in modo consistente diventa iniettiva.
![x²: da suriettiva a biettiva](figure/mate/ch17_x2_restrizione.png)
- x^{2}: ℝ → ℝ né iniettiva né suriettiva; ℝ → [0, +∞) suriettiva; [0, +∞) → [0, +∞) biettiva
- seno: ℝ → [−1, 1] suriettivo; [−π/2, π/2] → [−1, 1] biettivo; tangente: (−π/2, π/2) → ℝ biettiva
- ax + b con a ≠ 0 è biettiva su ℝ, ma su ℤ resta solo iniettiva: 2x + 1 = 2 dà x = 1/2 ∉ ℤ (biettiva solo per a = ±1)
- ogni ritocco dà una funzione diversa, con le stesse regole di calcolo
! Trabocchetto: gli elementi da scartare non si tolgono a caso: la scelta è convenzionale ma consistente, per esempio tutte le soluzioni negative.
> Vedi anche: Funzione biettiva, Funzione inversa, Restrizione e successioni

# Composizione e inversa

## Composizione di funzioni {15, 18}
= Con f: A → B e g: B → C, la **composizione** g ∘ f: A → C è (g ∘ f)(a) = g(f(a)): prima f, poi g.
- serve che il codominio di f coincida con il dominio di g
- **associativa**: h ∘ (g ∘ f) = (h ∘ g) ∘ f; **identità neutra**: f ∘ id_{A} = f = id_{B} ∘ f
- **non commutativa**: con f(x) = x^{2} e g(x) = x + 1, g ∘ f = x^{2} + 1 e f ∘ g = (x + 1)^{2}; in 1 danno 2 e 4
- con f: A → B e g: B → A, g ∘ f va da A in A e f ∘ g da B in B
- con una costante: g ∘ f_{β} = f_{g(β)}
! Trabocchetto: in g ∘ f si applica per prima f, anche se è scritta per seconda: si legge da destra a sinistra.
> Vedi anche: Composta iniettiva o suriettiva, Funzione inversa

## Composta iniettiva o suriettiva {19}
= Componendo si conservano iniettività e suriettività; dalla composta si risale all'iniettività della prima e alla suriettività della seconda.
![g ∘ f biettiva, f non suriettiva, g non iniettiva](figure/mate/ch19_controesempio.png)
- prova della prima: a_{1} ≠ a_{2} ⟹ f(a_{1}) ≠ f(a_{2}) ⟹ g(f(a_{1})) ≠ g(f(a_{2}))
- conseguenza: g ∘ f biettiva ⟹ f iniettiva e g suriettiva, e niente di più
- controesempio: f: {0} → {0, 1}, f(0) = 0, e g: {0, 1} → {0} costante
```
f, g iniettive    ⟹  g ∘ f iniettiva
f, g suriettive   ⟹  g ∘ f suriettiva
g ∘ f iniettiva   ⟹  f iniettiva    (la prima applicata)
g ∘ f suriettiva  ⟹  g suriettiva   (l'ultima applicata)
```
! Trabocchetto: g ∘ f iniettiva non dice niente su g, e g ∘ f suriettiva non dice niente su f.
> Vedi anche: Composizione di funzioni, Funzione inversa

## Funzione inversa {15, 19, 20}
= f: A → B è **invertibile** se esiste g: B → A con g ∘ f = id_{A} **e** f ∘ g = id_{B}. Questo succede se e solo se f è biettiva, e la g è unica: è l'**inversa** f^{−1}.
- f^{−1}(b) = a ⟺ f(a) = b: si rovescia il grafico
- esistenza: la suriettività dà una controimmagine, l'iniettività la rende unica
- unicità: g ∘ f ∘ h calcolata in due modi dà h = g
- esempi: x^{3} ha inversa ∛x; x^{2} su [0, +∞) ha inversa √x
- una sola composizione non basta: con π_{1}(m, n) = m e f(n) = (n, 0), π_{1} ∘ f = id_{ℤ} ma f ∘ π_{1} manda (m, n) in (m, 0)
! Trabocchetto: l'inversa f^{−1} esiste solo per le biettive; la controimmagine f^{−1}(T) per tutte. Se l'inversa c'è, i due insiemi coincidono.
> Vedi anche: Inversa di una composizione, Controimmagine e fibra, Funzione biettiva

## Inversa di una composizione {20}
= Se f: A → B e g: B → C sono biettive, anche g ∘ f lo è e (g ∘ f)^{−1} = f^{−1} ∘ g^{−1}.
- l'ordine si inverte: per tornare indietro si annulla prima l'ultima operazione
- (f^{−1})^{−1} = f, e f^{−1} è biettiva
- **cancellazione**: se f è suriettiva, g ∘ f = h ∘ f ⟹ g = h; se g è iniettiva, g ∘ f = g ∘ h ⟹ f = h
- per provare che f è biettiva basta costruire una g e controllare le due composizioni
! Trabocchetto: (g ∘ f)^{−1} non è g^{−1} ∘ f^{−1}: l'ultima funzione applicata è la prima da annullare.
> Vedi anche: Funzione inversa, Composizione di funzioni

## Operazione e sottoinsieme chiuso {20}
= Un'**operazione** su A è una funzione ∗: A × A → A, con a ∗ b immagine di (a, b); S ⊆ A è **chiuso** se a, b ∈ S implica a ∗ b ∈ S.
- la somma di reali è + : ℝ × ℝ → ℝ
- la composizione è un'operazione sulle funzioni da un insieme in sé stesso
- in ℤ con la somma i pari sono chiusi
! Trabocchetto: i dispari non sono chiusi rispetto alla somma: 1 + 1 = 2.
> Vedi anche: Composizione di funzioni

# Inclusione-esclusione

## Inclusione-esclusione per due insiemi {21}
= |A ∪ B| = |A| + |B| − |A ∩ B|: gli elementi comuni, contati due volte, si tolgono una volta.
![il contributo di ogni elemento](figure/mate/ch21_contributi_due.png)
- forma equivalente |A ∪ B| + |A ∩ B| = |A| + |B|: date tre quantità si ricava la quarta
- disgiunti: |A ∪ B| = |A| + |B|
- esami: 152 matematica, 144 fisica, 89 entrambi, almeno uno 152 + 144 − 89 = 207
- da 1 a 3000 né per 3 né per 5: 3000 − (1000 + 600 − 200) = 1600, perché D_{3} ∩ D_{5} = D_{15}
! Trabocchetto: |A ∪ B| = |A| + |B| è falsa in generale; e per «né… né» si toglie l'unione dal totale.
> Vedi anche: Inclusione-esclusione per tre insiemi

## Inclusione-esclusione per tre insiemi {21}
= |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|.
![un elemento del centro conta 3 − 3 + 1 = 1](figure/mate/ch21_venn3.png)
- il centro è contato 3 volte, tolto 3 volte, quindi va riaggiunto una volta
- Matrix: 129 = 109 + 76 + 55 − 52 − 44 − 28 + x, quindi x = 13 hanno visto tutti e tre i film
- da 1 a 660 divisibili per 5, 6 o 11: 132 + 110 + 60 − 22 − 12 − 10 + 2 = 260
- con più insiemi si alternano i segni; i termini sono 15 con 4 insiemi e 31 con 5
! Trabocchetto: per i multipli comuni serve il numero giusto: 5 e 6 sono coprimi, quindi D_{5} ∩ D_{6} = D_{30}.
> Vedi anche: Inclusione-esclusione per due insiemi

# Scelte successive e disposizioni

## Metodo delle scelte successive {22}
= Se una situazione si ottiene con k scelte successive, con n_{1} possibilità per la prima, n_{2} per la seconda e così via, le situazioni sono n_{1} · n_{2} · … · n_{k}.
- è il prodotto cartesiano: |A_{1} × … × A_{k}| = n_{1} · … · n_{k}
- menù con 12 panini, 5 bibite, 4 dolci: 12 · 5 · 4 = 240
- targhe con 3 lettere su 26 e 4 cifre: 26^{3} · 10^{4} = 175 760 000; PIN di 4 cifre: 10^{4} = 10 000
- le funzioni da A in B, con |A| = m e |B| = n, sono n^{m}: per ognuno degli m elementi si sceglie un valore tra n
- gli insiemi in cui si sceglie possono cambiare con le scelte precedenti: basta che a ogni livello il **numero** di scelte sia lo stesso
! Trabocchetto: le funzioni da A in B sono n^{m}, con la base n = |B| (i valori) e l'esponente m = |A| (gli elementi da sistemare).
> Vedi anche: Prodotto cartesiano, Quando si moltiplica e quando si somma

## Fattoriale e ordinamenti {23}
= Gli **ordinamenti** di un insieme con n elementi sono le biiezioni I_{n} → A, e sono n! = n · (n − 1) · … · 2 · 1, con 0! = 1.
![3 scelte, poi 2, poi 1](figure/mate/ch23_albero_permutazioni.png)
- n scelte per il primo posto, n − 1 per il secondo, …, 1 per l'ultimo
- n! = n · (n − 1)! per n ≥ 1: definizione ricorsiva
- 0! = 1 è una convenzione: c'è un solo modo di ordinare niente, e le formule non hanno casi a parte
- finale dei 100 metri con 8 atleti: 8! = 40 320 ordini d'arrivo
```
n   0  1  2  3   4    5    6     7      8
n!  1  1  2  6  24  120  720  5040  40320
```
! Trabocchetto: al secondo livello le scelte cambiano secondo il ramo (dopo a si sceglie tra b e c), ma il loro numero no: per questo si moltiplica.
> Vedi anche: Anagrammi, Disposizioni semplici

## Anagrammi {23}
= Una parola di lunghezza ℓ in cui i simboli ripetuti compaiono r_{1}, …, r_{k} volte ha ℓ!/(r_{1}! · … · r_{k}!) anagrammi.
- con lettere tutte diverse sono ℓ!: AGO 6, LUNA 24, PORTA 120
- ogni lettera ripetuta r volte divide per r!, perché scambiare le sue copie non cambia la parola
- la parola stessa conta come uno dei suoi anagrammi
```
ORO         3!/2!            = 3
POZZO       5!/(2! · 2!)     = 30
MATEMATICA  10!/(2! · 2! · 3!) = 151 200   (M, T due volte; A tre)
```
! Trabocchetto: ORO non ha 3! = 6 anagrammi ma 3: si divide per ogni lettera ripetuta, e le lettere singole non contano perché 1! = 1.
> Vedi anche: Fattoriale e ordinamenti

## Disposizioni con ripetizione {24}
= Una **disposizione con ripetizione** di ordine k è una scelta ordinata di k elementi di un insieme A di n elementi, anche uguali: D^{r}_{n,k} = n^{k}.
![4 scelte a ogni livello: 4, 16, 64, …](figure/mate/ch24_albero_ripetizione.png)
- è una funzione qualunque da I_{k} = {1, …, k} nell'insieme A dei n elementi tra cui si sceglie (i colori)
- la r in D^{r}_{n,k} sta per «ripetizione», non è un esponente
- falegname: 5 oggetti, 4 smalti, 4^{5} = 1024 colorazioni; 15 candidati con voti da 0 a 10: 11^{15} esiti
- gli oggetti sono distinguibili: con 5 sedie identiche l'ordine non conterebbe più
! Trabocchetto: la funzione va dagli oggetti ai colori (a ogni oggetto un colore), quindi 4^{5} e non 5^{4}: la base è il numero delle cose tra cui si sceglie.
> Vedi anche: Disposizioni semplici, Quale formula usare

## Disposizioni semplici {24}
= Una **disposizione semplice** di ordine k da n oggetti è una scelta ordinata di k elementi distinti: D_{n,k} = n · (n − 1) · … · (n − k + 1) = n!/(n − k)!.
![5 scelte, poi 4, poi 3: 60](figure/mate/ch24_albero_podio.png)
- è una funzione iniettiva da I_{k} in A: serve k ≤ n
- i fattori sono k: il primo è n, l'ultimo n − k + 1
- podio con 8 atleti: D_{8,3} = 8 · 7 · 6 = 336; con 12: 12 · 11 · 10 = 1320
- con k = n si ritrova n!/0! = n!, gli ordinamenti
! Trabocchetto: l'indizio è se le scelte si ripetono: un atleta non vince due medaglie (semplici), un colore serve più oggetti (con ripetizione).
> Vedi anche: Disposizioni con ripetizione, Combinazioni semplici, Principio dei cassetti

# Insiemi finiti e cassetti

## Insiemi equipollenti {25}
= A e B sono **equipollenti**, |A| = |B|, se esiste una biiezione A → B; |A| ≤ |B| se esiste una funzione iniettiva A → B.
![il posto di ogni coppia di ℕ × ℕ nella lista](figure/mate/ch25_diagonali.png)
- l'equipollenza è riflessiva (id_{A}), simmetrica (f^{−1}) e transitiva (composta di biiezioni)
- ℕ e i pari 2ℕ sono equipollenti con n ↦ 2n, anche se i pari sono una parte di ℕ
- ℕ × ℕ è equipollente a ℕ: si elencano le coppie per a + b crescente
- se A ⊆ B allora |A| ≤ |B|; x ↦ {x} dà |X| ≤ |𝒫(X)|
- **Schröder-Bernstein**: |A| ≤ |B| e |B| ≤ |A| danno |A| = |B|
! Trabocchetto: con gli infiniti una parte può essere grande quanto il tutto: ℕ e 2ℕ hanno la stessa cardinalità.
> Vedi anche: Insiemi finiti e infiniti, Insiemi numerabili

## Insiemi finiti e infiniti {25}
= A è **infinito** se esiste f: A → A iniettiva ma non suriettiva; è **finito** se ogni f: A → A iniettiva è anche suriettiva.
- ℕ è infinito: n ↦ n + 1 è iniettiva e lascia fuori lo 0
- per A finito e f: A → A: iniettiva ⟺ suriettiva ⟺ biettiva
- lo stesso vale per f: A → B se A e B finiti hanno lo stesso numero di elementi
- ogni insieme finito non vuoto è equipollente a un unico I_{n} = {1, …, n}, e si pone |A| = n
! Trabocchetto: su un insieme infinito iniettiva non implica suriettiva: n + 1 su ℕ non raggiunge 0.
> Vedi anche: Insiemi equipollenti, Principio dei cassetti

## Principio dei cassetti {25, 24}
= Se |A| > |B|, con A e B finiti, nessuna funzione A → B è iniettiva: con più piccioni che gabbie, una gabbia ha almeno due piccioni.
- la gabbia g contiene la fibra f^{−1}(g); se f non è iniettiva, una fibra ha più di un elemento
- compleanni: con più di 366 persone due festeggiano lo stesso giorno
- PIN: tra 10 001 smartphone due hanno lo stesso PIN di 4 cifre
- 5 punti a coordinate intere: le coppie di parità sono 4, quindi due punti hanno coordinate della stessa parità e punto medio intero
- per lo stesso motivo una disposizione semplice chiede k ≤ n
! Trabocchetto: 366 persone non bastano: i giorni sono 366 contando il 29 febbraio, ne servono più di 366.
> Vedi anche: Insiemi finiti e infiniti, Disposizioni semplici

## Insiemi numerabili {25}
= X è **numerabile** se è equipollente a ℕ, cioè se i suoi elementi si elencano in una successione a_{1}, a_{2}, a_{3}, …
- ℤ: 0, 1, −1, 2, −2, …; f(a) = −2a se a ≤ 0, f(a) = 2a − 1 se a > 0
- l'inversa è g(n) = (−1)^{n+1} · ⌊(n + 1)/2⌋, con ⌊x⌋ **parte intera**, il più grande intero ≤ x
- ℚ è numerabile, come ℕ × ℕ; ℝ e 𝒫(ℕ) no (Cantor: |X| < |𝒫(X)|, dimostrazione non richiesta)
- alcuni autori chiamano numerabili anche gli insiemi finiti; qui no
! Trabocchetto: con i negativi la parte intera scende: ⌊−√2⌋ = −2, non −1.
> Vedi anche: Insiemi equipollenti

# Combinazioni e problemi di conteggio

## Combinazioni semplici {26}
= Una **combinazione semplice** di ordine k da n oggetti è un sottoinsieme di k elementi: C_{n,k} = (n su k) = n!/(k!(n − k)!), il **coefficiente binomiale**.
![6 disposizioni, una sola combinazione {c, e, f}](figure/mate/ch26_riordinamenti.png)
- idea: si contano le scelte ordinate D_{n,k} e si divide per k!, i modi di riordinare gli stessi k elementi
- C_{n,0} = C_{n,n} = 1 (qui serve 0! = 1); C_{n,1} = n
- 3 oggetti fra 6: (6 · 5 · 4)/(3 · 2 · 1) = 20; si semplifica prima, la calcolatrice alla fine
- superenalotto, 6 numeri da 90: (90 · 89 · 88 · 87 · 86 · 85)/720 = 622 614 630
! Trabocchetto: «n su k» non è una frazione: si scrive tra parentesi tonde, senza barra.
> Vedi anche: Disposizioni semplici, Quale formula usare, Quando si moltiplica e quando si somma

## Quale formula usare {24, 26}
= Due domande decidono la formula: l'ordine conta? Le scelte si possono ripetere?
- leggere il problema è la parte difficile; le formule sono semplici
- ordine che conta: podio, colorare oggetti distinti, codici; ordine che non conta: coni gelato, sestine
- le combinazioni con ripetizione (pasticcini in una vaschetta) si fanno a parte, dal capitolo 28
```
                   ordine conta            ordine non conta
con ripetizione    D^r n,k = n^k           capitolo 28
senza ripetizione  D n,k = n!/(n−k)!       C n,k = n!/(k!(n−k)!)
tutti, k = n       n!  (ordinamenti)       1
```
! Trabocchetto: cioccolato, nocciola, pistacchio e pistacchio, cioccolato, nocciola sono lo stesso cono: lì si contano sottoinsiemi, non disposizioni.
> Vedi anche: Disposizioni con ripetizione, Disposizioni semplici, Combinazioni semplici

## Quando si moltiplica e quando si somma {27}
= Se a ogni passo il numero di scelte è sempre lo stesso, qualunque sia il percorso, si **moltiplica**; se è il numero di scelte a dipendere dal ramo, si conta ramo per ramo e poi si **somma**.
![i punti finali della gelateria si sommano](figure/mate/ch27_albero_gelato.png)
- scuola di ballo, 4 uomini su 10 e 4 donne su 12: C_{10,4} · C_{12,4} = 210 · 495 = 103 950
- squadra 4-4-2: C_{3,1} · C_{8,4} · C_{7,4} · C_{4,2} = 3 · 70 · 35 · 6 = 44 100
- gelateria, coni da 1, 2 o 3 gusti diversi su 15: 15 + 105 + 455 = 575
- metodo: capire che cosa si chiede, se l'ordine conta, spezzare in passi, rimettere insieme
```
passi indipendenti, stesso numero     →  MOLTIPLICO
  «e poi»:  uomini E donne,  C(10,4) · C(12,4)
casi alternativi, numeri diversi      →  SOMMO
  «oppure»: piccolo O medio O grande,  15 + 105 + 455
```
! Trabocchetto: nella scuola di ballo C_{22,8} è sbagliato: non si scelgono 8 persone qualsiasi fra 22, ma 4 da un gruppo e 4 dall'altro.
> Vedi anche: Metodo delle scelte successive, Combinazioni semplici
