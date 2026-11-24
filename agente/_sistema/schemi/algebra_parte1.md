# Introduzione, insiemi numerici e campi

## Vettori e mappe lineari {1}
= Un **vettore** è un elemento qualsiasi di uno **spazio vettoriale**: un insieme in cui gli elementi si sommano e si moltiplicano per un numero, lo **scalare**.
- la somma corrisponde alla regola del parallelogramma; il prodotto per scalare allunga, accorcia o inverte il verso
- una **mappa lineare** è una funzione fra spazi vettoriali che rispetta somma e prodotto per scalare
- trasformare una somma dà la somma delle trasformate, e lo stesso con i multipli: ruotare o ingrandire un'immagine
- in informatica input e output sono array di numeri, cioè vettori; i pesi delle reti neurali sono coefficienti di mappe lineari, alternate a funzioni non lineari; spesso un segnale si ripulisce dal rumore con una mappa lineare
! Trabocchetto: un vettore non è per forza una freccia: può essere una matrice, un polinomio, una funzione.
> Vedi anche: Spazio vettoriale, Lo spazio ℝⁿ

## Insiemi numerici {2, 3}
= ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ: ogni ampliamento nasce per fare un'operazione che prima non si poteva fare.
- ℕ = {0, 1, 2, …}; ℤ per sottrarre; ℚ = {a/b | a, b ∈ ℤ, b ≠ 0} per dividere
- ℝ colma i «buchi» dei razionali; ℂ risolve equazioni senza soluzioni reali, come x² + 1 = 0
- un reale è il punto d'arrivo di approssimazioni razionali sempre più precise: π come 3; 3,1; 3,14; …
- così si calcola anche 2^{π}: con 2^{3,1}, 2^{3,14}, 2^{3,141}, …
! Trabocchetto: i razionali sembrano riempire la retta, ma √2, la diagonale del quadrato di lato 1, non è un rapporto di interi.
> Vedi anche: Campo, Forma algebrica

## Campo {2, 4, 16, 17}
= Un **campo** 𝕂 è un insieme con somma e prodotto che rispettano le 9 proprietà dell'aritmetica: dentro si fanno le quattro operazioni, divisione solo per numeri non nulli, senza uscire.
- somma: commutativa, associativa, neutro 0, opposto −a; prodotto: commutativo, associativo, neutro 1, inverso a^{−1} per a ≠ 0
- la nona è la **distributiva**: a·(b + c) = a·b + a·c
- con i gruppi: (𝕂, +) e (𝕂 ∖ {0}, ·) sono gruppi commutativi, legati dalla distributiva
- ℚ, ℝ e ℂ sono campi; ℕ no (mancano opposti e inversi), ℤ no (1/2 ∉ ℤ)
- gli elementi del campo sono gli **scalari** degli spazi vettoriali; nel corso di solito 𝕂 = ℝ oppure ℂ
! Trabocchetto: ℤ ha gli opposti ma non è un campo: gli manca l'inverso di 2.
> Vedi anche: Gruppo, ℂ è un campo non ordinato

# Numeri complessi in forma algebrica

## Forma algebrica {3}
= Un **numero complesso** è z = a + bi con a, b ∈ ℝ e i² = −1: a = Re(z) è la **parte reale**, b = Im(z) la **parte immaginaria**.
- b = 0: z = a è reale, quindi ℝ ⊂ ℂ; a = 0 e b ≠ 0: z = bi è un **immaginario puro**
- somma per parti: (a + bi) + (c + di) = (a + c) + (b + d)i
- prodotto con la distributiva e i² = −1: (a + bi)(c + di) = (ac − bd) + (ad + bc)i
- esempio: (1 + i)(1 + i) = 1 + 2i + i² = 2i; e i⁴ = 1
! Trabocchetto: la parte immaginaria è il numero reale b, non bi: Im(3 + 2i) = 2.
> Vedi anche: Insiemi numerici, Piano di Argand-Gauss, Coniugato

## ℂ è un campo non ordinato {4}
= Somma e prodotto di ℂ rispettano le 9 proprietà, quindi ℂ è un campo; però non esiste un ordine compatibile con le operazioni.
- neutri 0 = 0 + 0i e 1 = 1 + 0i; opposto −z = −a − bi; inverso per ogni z ≠ 0
- in un campo ordinato il quadrato di un elemento non nullo è positivo, ma i² = −1 renderebbe positivo −1
- i complessi si confrontano solo con = e ≠; si possono ordinare grandezze reali associate, come i moduli o le parti reali
! Trabocchetto: z₁ > z₂ o «z è positivo» non hanno senso in ℂ: si confrontano |z₁| e |z₂|.
> Vedi anche: Campo, Modulo

## Coniugato {5, 6, 8}
= Il **coniugato** di z = a + bi è z̄ = a − bi: stessa parte reale, parte immaginaria cambiata di segno.
- nel piano è il simmetrico di z rispetto all'asse reale; il coniugato di 2 + 3i è 2 − 3i
- applicato due volte riporta a z; z = z̄ se e solo se z è reale
- z · z̄ = (a + bi)(a − bi) = a² + b² = |z|²: sempre un reale ≥ 0
- in forma polare: se z = r e^{iθ}, allora z̄ = r e^{−iθ}, stesso modulo e angolo opposto
! Trabocchetto: z · z̄ dà |z|², non |z|: per 3 + 4i fa 25, non 5.
> Vedi anche: Modulo, Inverso di un numero complesso

## Modulo {5, 6, 8, 9}
= Il **modulo** di z = a + bi è |z| = √(a² + b²): la distanza del punto (a, b) dall'origine, per Pitagora.
- è un reale ≥ 0, ed è 0 solo per z = 0
- esempio: |3 + 4i| = √(9 + 16) = 5
- |z₁z₂| = |z₁| · |z₂| e |zⁿ| = |z|ⁿ
- a differenza dei complessi, i moduli si possono confrontare: |z₁| < |z₂|
! Trabocchetto: nella formula entra la parte immaginaria b, non bi: si sommano i quadrati, √(9 + 16), mai √(9 − 16).
> Vedi anche: Coniugato, Piano di Argand-Gauss, Prodotto in forma polare

## Inverso di un numero complesso {5, 8}
= Per z ≠ 0, da z · z̄ = |z|² segue z^{−1} = z̄ / |z|² = (a − bi)/(a² + b²).
![coniugato: stesso modulo, angolo −θ; inverso: modulo 1/r, angolo −θ](figure/alg/ch08_coniugato_inverso.png)
- z = 2 + 5i: |z|² = 4 + 25 = 29, z̄ = 2 − 5i, quindi z^{−1} = 2/29 − (5/29)i
- verifica: (2 + 5i)(2/29 − (5/29)i) = 1
- in forma polare: (r e^{iθ})^{−1} = (1/r) e^{−iθ}, modulo inverso e argomento opposto
- divisione, per z₂ ≠ 0: z₁/z₂ = (r₁/r₂) e^{i(θ₁ − θ₂)}, si dividono i moduli e si sottraggono gli angoli
! Trabocchetto: lo zero non ha inverso: |0|² = 0 e la divisione per |z|² non si può fare.
> Vedi anche: Coniugato, ℂ è un campo non ordinato

## Piano di Argand-Gauss {6}
= Il complesso z = a + bi si identifica con il punto (a, b) di ℝ², o con la freccia dall'origine al punto (a, b).
- asse orizzontale (Re): i reali; asse verticale (Im): i numeri bi
- la somma è quella dei vettori, con la regola del parallelogramma: (a, b) + (c, d) = (a + c, b + d)
- coniugato = riflessione rispetto all'asse reale; modulo = lunghezza della freccia
- il prodotto (a, b) · (c, d) = (ac − bd, ad + bc) in coordinate cartesiane non ha un significato chiaro: lo spiega la forma polare
! Trabocchetto: il prodotto non si fa componente per componente: (a, b) · (c, d) non è (ac, bd).
> Vedi anche: Forma polare ed esponenziale, Prodotto in forma polare

# Forma polare e radici n-esime

## Forma polare ed esponenziale {7}
= Un punto P ≠ O si individua con la distanza r = |OP| e l'angolo θ, in radianti e in senso antiorario dal semiasse reale positivo: z = r(cos θ + i sen θ) = r e^{iθ}.
- dalle polari alle cartesiane: a = r cos θ, b = r sen θ; viceversa r = √(a² + b²), cos θ = a/r, sen θ = b/r
- e^{iθ} è solo un simbolo per cos θ + i sen θ: al variare di θ dà i punti della circonferenza di raggio 1
- e^{iπ} = −1, da cui l'identità di Eulero e^{iπ} + 1 = 0; e^{2πi} = 1
- esempi: −5 = 5e^{iπ}; 2e^{iπ/4} = 2(√2/2 + i√2/2) = √2 + i√2
! Trabocchetto: r₁e^{iθ₁} e r₂e^{iθ₂} (con r > 0) sono lo stesso numero se e solo se r₁ = r₂ e θ₂ = θ₁ + 2kπ, con k ∈ ℤ: angoli diversi possono dare lo stesso punto.
> Vedi anche: Argomento e quadrante, Prodotto in forma polare, Radici n-esime

## Argomento e quadrante {7, 9}
= L'**argomento** Arg(z) è l'angolo θ di z ≠ 0; è definito a meno di multipli di 2π, quindi si dichiara un intervallo, [0, 2π) oppure (−π, π].
![quale formula usare per θ a seconda del quadrante](figure/alg/ch07_quadranti.png)
- per z = 0 l'argomento non è definito: l'origine non ha una direzione
- con θ ∈ [0, 2π): a > 0 e b ≥ 0 dà arctan(b/a); a > 0 e b < 0 dà arctan(b/a) + 2π; a < 0 dà arctan(b/a) + π
- se a = 0: θ = π/2 per b > 0 e θ = 3π/2 per b < 0
- z = −1 + i: r = √2 e arctan(1/(−1)) = −π/4; poiché a < 0, θ = −π/4 + π = 3π/4, nel secondo quadrante
! Trabocchetto: arctan(b/a) dà solo angoli fra −π/2 e π/2: con a < 0 da solo sbaglia quadrante; conviene controllare con un disegno.
> Vedi anche: Forma polare ed esponenziale, Radici n-esime

## Prodotto in forma polare {8, 6}
= Con z₁ = r₁e^{iθ₁} e z₂ = r₂e^{iθ₂} si ha z₁z₂ = (r₁r₂) e^{i(θ₁ + θ₂)}: i moduli si moltiplicano, gli angoli si sommano.
- viene da e^{i(θ₁ + θ₂)} = e^{iθ₁} · e^{iθ₂}, con le formule di addizione di seno e coseno
- |z₁z₂| = |z₁| · |z₂| e Arg(z₁z₂) = Arg(z₁) + Arg(z₂), a meno di multipli di 2π
- geometricamente, moltiplicare per z₂ ruota di θ₂ e riscala di un fattore r₂
- esempio: 1 + i = √2 e^{iπ/4}, quindi (1 + i)² = 2e^{iπ/2} = 2i, come con 1 + 2i + i² = 2i
! Trabocchetto: gli angoli si sommano, non si moltiplicano; sono i moduli a moltiplicarsi.
> Vedi anche: Potenze e De Moivre, Inverso di un numero complesso

## Potenze e De Moivre {9}
= Se z = r e^{iθ} e n ≥ 1: zⁿ = rⁿ e^{inθ} = rⁿ(cos nθ + i sen nθ), la **formula di De Moivre**.
- |zⁿ| = |z|ⁿ: il modulo si eleva alla n
- Arg(zⁿ) = n · Arg(z): l'angolo si moltiplica per n, a meno di multipli di 2π
- esempio: (1 + i)^{2000} = (√2)^{2000} e^{i·2000π/4} = 2^{1000} e^{i·500π} = 2^{1000}
- in forma cartesiana lo stesso conto sarebbe impraticabile
! Trabocchetto: l'angolo nθ va ridotto togliendo i giri completi: 500π = 250 · 2π, quindi e^{i·500π} = 1.
> Vedi anche: Prodotto in forma polare, Radici n-esime

## Radici n-esime {9, 7}
= w è una **radice n-esima** di z₀ se wⁿ = z₀. Per z₀ = r₀e^{iθ₀} ≠ 0 le radici sono esattamente n, tutte distinte: w_{k} = ⁿ√r₀ · e^{i(θ₀/n + 2kπ/n)}, per k = 0, 1, …, n − 1.
- condizione sul modulo: rⁿ = r₀, quindi r = ⁿ√r₀, la radice reale positiva
- condizione sull'angolo: nθ = θ₀ + 2kπ, quindi θ = θ₀/n + 2kπ/n; gli altri valori di k ridanno le stesse radici
- stanno sulla circonferenza di raggio ⁿ√r₀ a passo 2π/n: sono i vertici di un poligono regolare con n lati
! Trabocchetto: in ℂ «la radice n-esima» non è un numero solo ma l'insieme delle n soluzioni: vanno elencate tutte.
> Vedi anche: Esempi di radici n-esime, Argomento e quadrante, Potenze e De Moivre

## Esempi di radici n-esime {9}
= I tre esempi del corso: le radici terze di 8, le soluzioni di z³ = −8 e le radici n-esime dell'unità.
![le radici terze di 8: un triangolo equilatero di raggio 2](figure/alg/ch09_radici_di_8.png)
- z³ = 8 = 8e^{i0}: modulo ³√8 = 2 e angoli 0, 2π/3, 4π/3, quindi 2, −1 + i√3, −1 − i√3
- z³ = −8 = 8e^{iπ}: modulo 2 e angoli π/3, π, 5π/3, quindi 1 + i√3, −2, 1 − i√3, lo stesso triangolo ruotato di π/3
- zⁿ = 1: z_{k} = e^{i·2kπ/n}, k = 0, …, n − 1, un poligono regolare di raggio 1 con un vertice in 1; per n = 6 un esagono
! Trabocchetto: per −8 l'angolo di partenza è θ₀ = π, non 0: partendo da 0 si trovano le radici di 8.
> Vedi anche: Radici n-esime

# Polinomi

## Monomi e polinomi {10}
= Un **monomio** è un coefficiente per delle variabili, su cui si usano solo somma, sottrazione e prodotto (esponenti naturali); un **polinomio** è una somma di monomi.
- sono monomi 4x, −2xy² e √5·x⁴ (√5 è solo un numero); non lo sono sin(x), x/y e √x
- grado di un monomio: la somma degli esponenti (−2xy² ha grado 3); di un polinomio: il massimo grado dei suoi monomi
- in una variabile: p(x) = a_{n}xⁿ + … + a₁x + a₀ con a_{n} ≠ 0 ha grado n; un polinomio di grado 0 è un numero
- il **polinomio zero**, p(x) ≡ 0, non ha nessun coefficiente diverso da zero
- ℝ[x] e ℂ[x] sono gli insiemi dei polinomi a coefficienti reali e complessi
! Trabocchetto: la radice va bene sul coefficiente (√5·x⁴ è un monomio) ma non sulla variabile (√x non lo è).
> Vedi anche: Polinomi di grado al più k, Divisione con resto

## Polinomi di grado al più k {10, 18, 20}
= ℝ_{k}[x], o in generale 𝕂_{k}[x], è l'insieme dei polinomi di grado **minore o uguale** a k, compreso il polinomio nullo.
- è chiuso per somma: nella somma il grado può scendere, ma non salire
- (2x² − x + 2) + (−2x² + 3x − 1) = 2x + 1: due polinomi di grado 2 danno grado 1, e si resta in ℝ₂[x]
- è un sottospazio dello spazio 𝕂[x] di tutti i polinomi
- i polinomi di grado **esattamente** k non formano uno spazio: x² + (−x² + x) = x, e lo zero non ha grado k
! Trabocchetto: con «grado = k» la somma esce dall'insieme: x⁵ + x e −x⁵ + x² hanno grado 5, la somma x² + x ha grado 2.
> Vedi anche: Monomi e polinomi, Sottospazio vettoriale, Basi canoniche

## Divisione con resto {11}
= Dati p(x) e d(x) ≠ 0 esistono, unici, q(x) e r(x) con p(x) = d(x) · q(x) + r(x) e grado di r < grado di d.
- è la condizione sul grado a rendere unico il risultato, come 44 = 6 · 7 + 2 e non 6 · 5 + 14
- si procede come nella divisione in colonna fra interi, guardando solo i monomi di grado massimo
- d(x) **divide** p(x), e si scrive d(x) | p(x), se il resto è zero: (x − 1) | (x² − 1) = (x − 1)(x + 1)
```
(x⁴ − 2x³ + 2x² + x − 1) : (x² − 1)
x⁴ : x² = x²      resta  −2x³ + 3x² + x − 1
−2x³ : x² = −2x   resta  3x² − x − 1
3x² : x² = 3      resta  −x + 2    (grado 1 < 2: stop)
q = x² − 2x + 3,  r = −x + 2
```
! Trabocchetto: ci si ferma solo quando il grado del resto è minore del grado del divisore.
> Vedi anche: Radice di un polinomio, Monomi e polinomi

## Radice di un polinomio {12, 11}
= a è una **radice** di p(x) se p(a) = 0; e p(a) = 0 se e solo se (x − a) divide p(x).
- dimostrazione: p(x) = (x − a)q(x) + r₀, con r₀ costante perché il grado di r è minore di 1; poi p(a) = r₀
- quindi il resto della divisione per (x − a) è proprio p(a): trovare una radice equivale a trovare un fattore
- x² − 5x + 6: p(2) = 0 e infatti p(x) = (x − 2)(x − 3); p(4) = 2 ≠ 0 e (x − 4) non divide p
! Trabocchetto: il fattore è (x − a), con il meno: la radice 2 dà il fattore (x − 2), non (x + 2).
> Vedi anche: Divisione con resto, Molteplicità

## Molteplicità {12}
= La **molteplicità** di una radice a è il massimo k tale che (x − a)^{k} divide p(x); è sempre almeno 1.
![x³ − 2x² + x = (x − 1)²x: la radice doppia 1 tocca l'asse senza attraversarlo](figure/alg/ch12_radice_doppia.png)
- si divide per (x − a) e si controlla se a è ancora radice del quoziente
- x³ − 1 = (x − 1)(x² + x + 1) e il quoziente in 1 vale 3 ≠ 0: la radice 1 ha molteplicità 1
- x³ − 2x² + x = (x − 1)² · x: 1 ha molteplicità 2, 0 ha molteplicità 1
- **contate con molteplicità**, le radici di questo polinomio di grado 3 sono 2 + 1 = 3
! Trabocchetto: dopo la prima divisione va controllato il quoziente: fermandosi subito una radice doppia viene contata una volta sola.
> Vedi anche: Radice di un polinomio, Al più n radici

## Al più n radici {13}
= Un polinomio di grado n ≥ 1 ha al massimo n radici, contate con molteplicità.
- si dimostra per **induzione** sul grado; caso base n = 1: ax + b ha l'unica radice −b/a
- passo: se p di grado n + 1 ha una radice a, allora p(x) = (x − a)q(x) con q di grado n, che ha al più n radici
- un prodotto è nullo se e solo se lo è un fattore: le radici di p sono a più quelle di q
- il grado 0 è escluso: una costante non nulla non ha radici, il polinomio zero ne ha infinite
! Trabocchetto: «al massimo n» ammette anche zero radici: in ℝ, x² + 1 non ne ha.
> Vedi anche: Molteplicità, Teorema fondamentale dell'algebra

## Equazioni di secondo grado {13}
= Per ax² + bx + c, con a, b, c reali e a ≠ 0, decide il **discriminante** Δ = b² − 4ac.
- Δ > 0: due radici reali distinte, x = (−b ± √Δ)/(2a)
- Δ = 0: una sola radice, −b/(2a), di molteplicità 2
- Δ < 0: nessuna radice reale; in ℂ però ±√Δ esistono sempre, e le radici complesse sono due
- complemento non svolto a lezione: x² + (1 − i)x − i ha Δ = (1 − i)² + 4i = 2i, ±√Δ = ±(1 + i) e radici i e −1
! Trabocchetto: Δ < 0 vuol dire nessuna radice **reale**, non nessuna radice: in ℂ un polinomio di grado 2 ne ha sempre due.
> Vedi anche: Teorema fondamentale dell'algebra, Radici n-esime

## Teorema fondamentale dell'algebra {13}
= Un polinomio a coefficienti complessi di grado n ≥ 1 ha **esattamente** n radici complesse, contate con molteplicità.
- nel corso si enuncia soltanto, senza dimostrazione
- x² + 1 non ha radici reali, ma ha le due radici complesse i e −i: i² = (−i)² = −1
- è il motivo principale per cui si introducono i complessi: il numero giusto di radici, il grado, si ottiene solo in ℂ
- complemento non svolto a lezione: se p ha coefficienti reali e z è una radice, anche z̄ è una radice
! Trabocchetto: «esattamente n» vale in ℂ; in ℝ resta solo «al più n».
> Vedi anche: Al più n radici, Equazioni di secondo grado

# ℝⁿ e spazi vettoriali

## Lo spazio ℝⁿ {14}
= ℝⁿ = ℝ × … × ℝ (n copie) è l'insieme delle n-uple (x₁, …, x_{n}) di numeri reali, scritte in colonna: i suoi elementi sono i **vettori** e x_{i} è la i-esima **componente**.
- l'**origine** è il vettore 0 = (0, …, 0)
- ℝ² è il piano cartesiano, ℝ³ lo spazio; per n più grande non si disegna, ma si calcola allo stesso modo
- tre modi di vedere un vettore: n-upla (per i conti), punto, freccia dall'origine al punto
- «n-dimensionale» per ora è solo un nome: la dimensione si definisce più avanti, e vale davvero n
> Vedi anche: Somma e prodotto per scalare, Dimensione

## Somma e prodotto per scalare {15}
= In ℝⁿ si somma componente per componente, v + w = (x₁ + y₁, …, x_{n} + y_{n}), e si moltiplica per uno scalare ogni componente, a·v = (ax₁, …, ax_{n}).
![somma con il parallelogramma; 2v e −v](figure/alg/ch15_somma_prodotto.png)
- (3, 1) + (1, 2) = (4, 3): il vertice del parallelogramma opposto all'origine
- 2·(3, 1) = (6, 2) ha lunghezza doppia; −v = (−3, −1) ha verso opposto
- un multiplo resta sulla retta della freccia: cambia la lunghezza e, con uno scalare negativo, il verso
- lo **scalare** è un elemento di un campo scelto prima; in ℝⁿ è un numero reale
! Trabocchetto: con a negativo la lunghezza diventa |a| volte quella di v, e il verso si inverte.
> Vedi anche: Lo spazio ℝⁿ, Le otto proprietà di ℝⁿ

## Le otto proprietà di ℝⁿ {16}
= Per u, v, w ∈ ℝⁿ e a, b ∈ ℝ valgono otto proprietà: le prime quattro riguardano la sola somma, le altre legano somma e prodotto per scalare.
```
1. (u + v) + w = u + (v + w)     5. a·(b·v) = (ab)·v
2. 0 + v = v + 0 = v             6. (a + b)·v = a·v + b·v
3. v + (−v) = (−v) + v = 0       7. a·(v + w) = a·v + a·w
4. u + v = v + u                 8. 1·v = v
```
- 0_{ℝⁿ} = (0, …, 0) è il vettore nullo, da non confondere con il numero 0; l'opposto è −v = (−x₁, …, −x_{n})
- nella 5 «ab» è un prodotto fra numeri; nella 8 l'1 è il neutro del prodotto in ℝ
- la commutatività è tenuta separata per i contesti in cui l'ordine conta
- sono proprio le proprietà che definiscono uno spazio vettoriale
! Trabocchetto: nella 6 i due «+» sono diversi: a sinistra si sommano numeri, a destra vettori.
> Vedi anche: Gruppo, Spazio vettoriale

## Gruppo {16}
= Un **gruppo** è un insieme G con un'operazione binaria ⋆ associativa, con un elemento neutro e con un inverso per ogni elemento.
- neutro: e ⋆ a = a ⋆ e = a; inverso: a ⋆ a′ = a′ ⋆ a = e, che per la somma si chiama **opposto**
- **abeliano**, o commutativo, se vale anche a ⋆ b = b ⋆ a
- gruppi abeliani: (ℝⁿ, +), (ℤ, +), ℚ, ℝ e ℂ con la somma; ℚ ∖ {0}, ℝ ∖ {0} e ℂ ∖ {0} con il prodotto
- non sono gruppi (ℕ, +), senza opposti, e (ℤ, ·), dove 2 non ha inverso
- i gruppi di permutazioni non sono abeliani: l'ordine conta
! Trabocchetto: con il prodotto si toglie lo zero, che non ha inverso: il gruppo è ℝ ∖ {0}, non ℝ.
> Vedi anche: Campo, Le otto proprietà di ℝⁿ

## Spazio vettoriale {17}
= Fissato un campo 𝕂, uno **spazio vettoriale** su 𝕂 è un insieme V con una somma V × V → V e un prodotto per scalare 𝕂 × V → V che rispettano le otto proprietà di ℝⁿ.
- (V, +) è un gruppo abeliano (proprietà 1-4), più le proprietà 5-8 con scalari in 𝕂
- per comunicarlo servono **quattro ingredienti**: l'insieme V, il campo 𝕂, la somma, il prodotto per scalare
- prima si sceglie il campo, poi l'insieme e le operazioni
- lo zero 0_{V} è l'origine dello spazio, diverso dallo zero di 𝕂
> Vedi anche: Esempi di spazi vettoriali, Zero e opposto, Gruppo

## Esempi di spazi vettoriali {17, 18}
= Gli esempi base sono 𝕂ⁿ, i polinomi 𝕂[x], le funzioni, ogni campo su sé stesso e ℂ su ℝ.
- 𝕂ⁿ: n-uple con entrate in 𝕂 e le operazioni di ℝⁿ; in ℂ²: (2 + i)·(3, 1 − i) = (6 + 3i, 3 − i)
- 𝕂[x]: si sommano i coefficienti dello stesso grado; (x³ − 2x + 1) + (4x⁴ + x − 3) = 4x⁴ + x³ − x − 2 e 3·(x³ − 2x) = 3x³ − 6x
- funzioni f: ℝ → ℝ, punto per punto: (f + g)(x) = f(x) + g(x) e (a·f)(x) = a·f(x)
- 𝕂 è uno spazio vettoriale su sé stesso (𝕂¹ = 𝕂); con due campi uno dentro l'altro, il più grande è spazio vettoriale sul più piccolo: ℂ su ℝ
! Trabocchetto: cambiando campo la somma non cambia: cambia solo per quali scalari si può moltiplicare.
> Vedi anche: Spazio vettoriale, Matrice, Polinomi di grado al più k

## Zero e opposto {18}
= In ogni spazio vettoriale 0·v = 0_{V} e (−1)·v = −v: lo zero e l'opposto si trovano moltiplicando per 0 e per −1.
- 0·v = (0 + 0)·v = 0·v + 0·v, e semplificando 0·v = 0_{V}
- v + (−1)·v = (1 + (−1))·v = 0·v = 0_{V}
- lo zero è unico, e ogni vettore ha un solo opposto
- in ℝ[x]: 0·(x + 1) è il polinomio nullo; l'opposto di p ha tutti i coefficienti cambiati di segno
! Trabocchetto: in 0·v = 0_{V} i due zeri sono diversi: a sinistra lo zero del campo, a destra quello dello spazio.
> Vedi anche: Spazio vettoriale, Le otto proprietà di ℝⁿ

## Matrice {19}
= Una **matrice** m × n su 𝕂 è una tabella di elementi di 𝕂 con m righe e n colonne; a_{ij} è l'entrata in riga i e colonna j. M(m, n, 𝕂) è l'insieme di tutte le matrici m × n.
![l'entrata aᵢⱼ sta nella i-esima riga e nella j-esima colonna](figure/alg/matrice_indici.png)
- somma e prodotto per scalare entrata per entrata: (A + B)_{ij} = a_{ij} + b_{ij} e (λA)_{ij} = λa_{ij}, solo fra matrici della stessa taglia
- M(m, n, 𝕂) è uno spazio vettoriale: lo zero è la matrice nulla, l'opposto è −A = (−1)·A
```
( 2 3 )   ( −1 1 )   ( 1 4 )
( 1 1 ) + (  0 1 ) = ( 1 2 )
( 0 5 )   (  1 4 )   ( 1 9 )
```
! Trabocchetto: prima la riga, poi la colonna: a_{12} sta in riga 1 e colonna 2; in Excel è il contrario, C2 è colonna C e riga 2.
> Vedi anche: Matrici quadrate speciali, Trasposta, Basi canoniche

# Sottospazi

## Sottospazio vettoriale {20}
= W ⊆ V è un **sottospazio** se 0 ∈ W, se è chiuso per somma (w₁ + w₂ ∈ W) e se è chiuso per prodotto per scalare (λw ∈ W).
![W₁ (z = 0) è un sottospazio, W₂ (z = 1) no](figure/alg/sottospazi_piani.png)
- con le operazioni di V un sottospazio è a sua volta uno spazio vettoriale, con lo stesso zero di V
- ci sono sempre il **banale** {0} e il **totale** V, e {0} ⊆ W ⊆ V
- W₁ = {(a, b, 0)} è un sottospazio di ℝ³; W₂ = {(a, b, 1)} no: non contiene 0, la somma ha terza componente 2, e 2·(1, 1, 1) = (2, 2, 2) esce
- regola pratica: per costruire sottospazi si impone che qualcosa sia **zero**, non uguale a 1
! Trabocchetto: lo zero deve stare nel sottospazio: un piano che non passa per l'origine non è mai un sottospazio.
> Vedi anche: Esempi e controesempi di sottospazi, Span

## Esempi e controesempi di sottospazi {20}
= Nel piano la retta per l'origine è un sottospazio, parabola e semiretta no; fra i polinomi lo è «grado al più d», non «grado esattamente 5».
![parabola e semiretta non sono sottospazi, la retta y = x sì](figure/alg/sottospazi_esempi_piano.png)
- parabola {(x, x²)}: (1, 1) c'è, ma ½·(1, 1) = (½, ½) no, perché (½)² = ¼
- semiretta {(x, 0) | x ≥ 0}: (−1)·(1, 0) = (−1, 0) esce
- retta {(x, x)}: (a, a) + (b, b) = (a + b, a + b) e λ(a, a) = (λa, λa) restano dentro
- 𝕂_{d}[x] è un sottospazio di 𝕂[x]; i polinomi di grado esattamente 5 no
! Trabocchetto: contenere lo zero non basta: parabola e semiretta passano per l'origine ma non sono chiuse per multipli.
> Vedi anche: Sottospazio vettoriale, Polinomi di grado al più k

## Matrici quadrate speciali {21}
= In una matrice quadrata n × n, dello spazio M(n), la **diagonale principale** è a₁₁, …, a_{nn}; le classi speciali si definiscono rispetto a essa.
- **diagonale**: a_{ij} = 0 per i ≠ j; **triangolare superiore**: a_{ij} = 0 per i > j (zeri sotto); **triangolare inferiore**: a_{ij} = 0 per i < j (zeri sopra)
- **simmetrica**: a_{ij} = a_{ji}; **antisimmetrica**: a_{ij} = −a_{ji}, quindi diagonale nulla, perché a_{ii} = −a_{ii} dà a_{ii} = 0
- una matrice può stare in più classi; la matrice nulla sta in tutte e, in ℝ e ℂ, è l'unica sia simmetrica sia antisimmetrica
```
( 0 0 )  diagonale, triangolare sup. e inf., simmetrica;
( 0 1 )  non antisimmetrica (c'è un 1 sulla diagonale)
( 1 2 )  nessuna classe: 2 sopra e 3 sotto la diagonale,
( 3 4 )  2 ≠ 3 e 2 ≠ −3
```
! Trabocchetto: i > j vuol dire sotto la diagonale, perché l'indice di riga è più grande: a₃₁ sta sotto.
> Vedi anche: Sottospazi di matrici quadrate, Trasposta

## Sottospazi di matrici quadrate {21}
= D(n), Ts(n), Ti(n), S(n) e A(n), cioè diagonali, triangolari superiori, triangolari inferiori, simmetriche e antisimmetriche, sono sottospazi di M(n).
- si verificano le tre condizioni: la matrice nulla sta nella classe, somma e multipli conservano la proprietà
- simmetriche: a_{ij} + b_{ij} = a_{ji} + b_{ji} e λa_{ij} = λa_{ji}
- invece l'insieme delle triangolari, Ts(n) ∪ Ti(n), contiene la nulla ed è chiuso per multipli, ma non per somma:
```
( 1 1 )   ( 0 0 )   ( 1 1 )
( 0 0 ) + ( 1 0 ) = ( 1 0 )
sup.      inf.      né sup. né inf.
```
! Trabocchetto: Ts(n) e Ti(n) sono sottospazi, ma le «triangolari», superiori oppure inferiori, non lo sono: per questo si elencano separate.
> Vedi anche: Matrici quadrate speciali, Sottospazio vettoriale

# Combinazioni lineari e basi

## Combinazione lineare {22}
= Una **combinazione lineare** di v₁, …, v_{k} è un vettore λ₁v₁ + … + λ_{k}v_{k}, con scalari λ_{i} ∈ 𝕂 qualunque, anche nulli o negativi.
- è una ricetta: un po' di ciascun vettore, poi si somma; il risultato resta nello spazio
- esempio: 3v₁ + 2v₂ − 7v₃ è una combinazione lineare di v₁, v₂, v₃
- in ℝ³ con (1, 0, 0) e (0, 1, 0): λ₁v₁ + λ₂v₂ = (λ₁, λ₂, 0), che al variare dei λ dà il piano z = 0
- con tutti i coefficienti nulli si ottiene il vettore nullo: è la combinazione **banale**
> Vedi anche: Span, Indipendenza lineare

## Span {22}
= Lo **Span** di v₁, …, v_{k} è l'insieme di tutte le loro combinazioni lineari, Span(v₁, …, v_{k}) = {λ₁v₁ + … + λ_{k}v_{k} | λ_{i} ∈ 𝕂}, ed è sempre un sottospazio.
- costruisce i sottospazi per inclusione, invece di imporre condizioni
- un vettore non nullo genera una retta per l'origine: Span((1, 2)) = {(t, 2t) | t ∈ ℝ}, la retta y = 2x
- Span((1, 2), (2, 4)) = {(a + 2b)·(1, 2)} = Span((1, 2)): (2, 4) non aggiunge direzioni
- Span((1, 0, 1), (0, 1, 1)) = {(a, b, a + b)}, il piano z = x + y: (1, 2, 3) ci sta, (1, 2, 4) no
! Trabocchetto: due vettori non generano per forza un piano: se uno è multiplo dell'altro lo Span è una retta.
> Vedi anche: Combinazione lineare, Insieme di generatori, Sottospazio vettoriale

## Insieme di generatori {23, 24}
= v₁, …, v_{n} sono un **insieme di generatori** di V se Span(v₁, …, v_{n}) = V: ogni v ∈ V si scrive come a₁v₁ + … + a_{n}v_{n} in almeno un modo.
![v₁, v₂, v₃ generano ℝ² ma v₂ = −v₁ è di troppo; w da solo genera solo una retta](figure/alg/generatori_ridondanti.png)
- (1, 0), (−1, 0), (0, 1) generano ℝ²: (x, y) = x·v₁ + 0·v₂ + y·v₃
- però (5, 6) = 5v₁ + 0v₂ + 6v₃ = 0v₁ − 5v₂ + 6v₃: più scritture segnalano un vettore ridondante
- aggiungendo vettori a un insieme di generatori si ha ancora un insieme di generatori
! Trabocchetto: generare non chiede che la scrittura sia unica: l'unicità arriva solo con una base.
> Vedi anche: Span, Indipendenza lineare, Base

## Indipendenza lineare {23, 24}
= v₁, …, v_{n} sono **linearmente indipendenti** se a₁v₁ + … + a_{n}v_{n} = 0 solo con a₁ = … = a_{n} = 0, cioè solo con la combinazione banale; altrimenti sono **dipendenti**.
- dipendenti se e solo se uno di loro è combinazione lineare degli altri: si divide per un coefficiente non nullo
- (1, 0), (−1, 0), (0, 1) sono dipendenti: v₁ + v₂ + 0·v₃ = 0
- un sottoinsieme di un insieme indipendente è indipendente: agli indipendenti piace essere piccoli, ai generatori grandi
- se sono indipendenti, sono tutti non nulli e a coppie non multipli
! Trabocchetto: con tre o più vettori «a coppie non multipli» non basta: (1, 1, 0), (0, 1, 1), (1, 0, −1) sono dipendenti, perché v₁ − v₂ − v₃ = 0.
> Vedi anche: Casi particolari di dipendenza, Verificare l'indipendenza, Base

## Casi particolari di dipendenza {24}
= Con uno o due vettori, o con il vettore nullo nell'insieme, l'indipendenza si decide subito.
- un insieme che contiene 0 è dipendente: 0·v₁ + 0·v₂ + 1·0 = 0 ha un coefficiente non nullo
- un solo vettore: {v} è indipendente se e solo se v ≠ 0
- due vettori: dipendenti se e solo se uno è multiplo dell'altro, v₁ = a·v₂ oppure v₂ = a·v₁
- se un vettore è multiplo di un altro, tutto l'insieme è dipendente: {v₁, 2v₁, v₃}
! Trabocchetto: «multiplo» vuol dire per uno scalare: x e x² non sono multipli, perché nessun numero trasforma x in x².
> Vedi anche: Indipendenza lineare

## Verificare l'indipendenza {24, 26}
= Si impone a₁v₁ + … + a_{n}v_{n} = 0 e si risolve il sistema nelle incognite a_{i}: se l'unica soluzione è quella nulla, i vettori sono indipendenti.
- (2, 1) e (0, 1): a(2, 1) + b(0, 1) = (2a, a + b) = (0, 0) dà a = 0 e poi b = 0, quindi indipendenti
- v₁ = (1, 1, 2), v₂ = (−1, 1, −1), v₃ = (1, 5, 4): v₃ = 3v₁ + 2v₂, cioè 3v₁ + 2v₂ − v₃ = 0, quindi dipendenti
- v₁, v₂ e v₄ = (0, 1, 1): a − b = 0, a + b + c = 0, 2a − b + c = 0 danno solo a = b = c = 0, quindi indipendenti
- per la dipendenza basta esibire una relazione con coefficienti non tutti nulli
! Trabocchetto: trovare la soluzione nulla non prova niente, perché c'è sempre: bisogna mostrare che è l'unica.
> Vedi anche: Indipendenza lineare, Base

## Base {23, 26}
= Una **base** di V è un insieme di vettori linearmente indipendenti che generano V: un kit completo e senza sprechi.
- {(1, 0), (0, 1)} è una base di ℝ²; {(1, 0), (−1, 0), (0, 1)} genera ma non è indipendente; {(1, 1)} è indipendente ma non genera
- se dim V = n, n vettori indipendenti **oppure** generatori sono già una base
- (−1, 1) e (2, 1) non sono multipli, quindi sono indipendenti; e dim ℝ² = 2, quindi sono una base
- schema per ogni insieme: l.i.? generatori? base? La terza risposta è sì solo se lo sono le prime due
! Trabocchetto: «basta una condizione» vale solo se i vettori sono esattamente n = dim V.
> Vedi anche: Coordinate in una base, Dimensione, Indipendenza lineare, Insieme di generatori

## Coordinate in una base {25}
= Se {v₁, …, v_{n}} è una base, ogni v ∈ V si scrive in **un solo modo** come v = a₁v₁ + … + a_{n}v_{n}: gli a_{i} sono le **coordinate** di v nella base.
- esistenza: i vettori generano; unicità: da due scritture, sottraendo, (a₁ − b₁)v₁ + … + (a_{n} − b_{n})v_{n} = 0, e l'indipendenza dà a_{i} = b_{i}
- fissata una base, per comunicare un vettore bastano le sue coordinate
- (3, 2) = 3·(1, 0) + 2·(0, 1): nella base canonica le coordinate sono le entrate
- uno spazio ha in genere moltissime basi: ℝ² ne ha infinite
! Trabocchetto: coordinate = entrate solo nella base canonica: con altre basi sono in generale numeri diversi.
> Vedi anche: Base, Basi canoniche

## Dimensione {26, 28}
= Se V ha una base di n vettori, ogni altra base ha n vettori (teorema non dimostrato): n è la **dimensione** dim V. Se non ci sono basi finite, V ha dimensione infinita.
- per calcolarla si trova una base, la più semplice possibile, e se ne contano gli elementi
- in uno spazio di dimensione n, più di n vettori sono sempre dipendenti
- dim 𝕂ⁿ = n, dim 𝕂_{d}[x] = d + 1, dim M(m, n, 𝕂) = m·n
- 𝕂[x] e lo spazio delle funzioni hanno dimensione infinita
! Trabocchetto: dim 𝕂_{d}[x] è d + 1, non d: la base 1, x, …, x^{d} parte dall'esponente 0.
> Vedi anche: Basi canoniche, Base, Limiti al rango

## Basi canoniche {26}
= Le basi più naturali: in 𝕂ⁿ i vettori e_{i} con un 1 al posto i e 0 altrove; nei polinomi 1, x, …, x^{d}; nelle matrici le E_{ij}, con un 1 al posto (i, j) e 0 altrove.
- (a₁, …, a_{n}) = a₁e₁ + … + a_{n}e_{n}, e la combinazione è nulla solo se tutti gli a_{i} sono nulli
- un polinomio di grado al più d è già una combinazione di 1, x, …, x^{d}; è nullo solo con tutti i coefficienti nulli
- le E_{ij} sono tante quante le posizioni, m·n; in 2 × 2 sono quattro:
```
( 1 0 )  ( 0 1 )  ( 0 0 )  ( 0 0 )
( 0 0 )  ( 0 0 )  ( 1 0 )  ( 0 1 )
```
> Vedi anche: Dimensione, Coordinate in una base

# Operazioni sulle matrici

## Trasposta {27}
= La **trasposta** di A ∈ M(m, n, 𝕂) è ᵗA ∈ M(n, m, 𝕂), con (ᵗA)_{ij} = A_{ji}: le righe di A diventano le colonne di ᵗA.
![la trasposta di una matrice 3 × 2 è una 2 × 3](figure/alg/trasposta_esempio.png)
- ᵗ(ᵗA) = A, ᵗ(A + B) = ᵗA + ᵗB, ᵗ(λA) = λ·ᵗA
- A quadrata è simmetrica se e solo se ᵗA = A, antisimmetrica se e solo se ᵗA = −A
- colonne con gli apici, A^{1}, …, A^{n} (vettori di 𝕂^{m}), e A = (A^{1} | … | A^{n}); righe con i pedici, A_{1}, …, A_{m}
! Trabocchetto: un solo pedice (A_{i}) indica una riga intera, due pedici (A_{ij}) una singola entrata; e l'apice di A^{j} non è una potenza.
> Vedi anche: Rango, Matrici quadrate speciali, Proprietà del prodotto

## Rango {28}
= Il **rango** di A è rk(A) = dim Span(A^{1}, …, A^{n}), la dimensione dello spazio generato dalle colonne: misura quanto A è lontana dalla matrice nulla.
- rk(A) è il massimo numero di colonne linearmente indipendenti
- rk(A) = rk(ᵗA): il massimo numero di righe indipendenti è uguale a quello di colonne indipendenti
- calcolo: si tolgono una alla volta le colonne che dipendono dalle altre; il rango è il numero di colonne rimaste
- rk(0) = 0, e la matrice nulla è l'unica di rango 0; rk(I_{n}) = n, perché le colonne sono e₁, …, e_{n}
```
( 1 1 )
( 1 1 )   due colonne uguali (1, 1, 1): rango 1
( 1 1 )
```
> Vedi anche: Limiti al rango, Trasposta, Dimensione

## Limiti al rango {28}
= Per A ∈ M(m, n, 𝕂) vale rk(A) ≤ min(m, n): il rango non supera né il numero di colonne né quello di righe.
- rk(A) ≤ n perché le colonne sono n; rk(A) ≤ m perché rk(A) = rk(ᵗA)
- motivo generale: in uno spazio di dimensione n, m > n vettori sono sempre dipendenti
- una matrice con mille colonne e due righe ha rango al più 2; il limite però non dice quanto vale il rango
```
( 3 1 2 )   colonne (3, 1), (1, 0), (2, 1) in 𝕂²
( 1 0 1 )   (3, 1) = (1, 0) + (2, 1): rango 2, non 3
```
! Trabocchetto: colonne che non si assomigliano non sono per questo indipendenti: tre vettori di 𝕂² sono sempre dipendenti.
> Vedi anche: Rango, Dimensione

## Prodotto fra matrici {29}
= Se A ∈ M(m, n) e B ∈ M(n, p), il prodotto AB ∈ M(m, p) ha entrate (AB)_{ij} = A_{i1}B_{1j} + … + A_{in}B_{nj} = Σ_{k=1}^{n} A_{ik}B_{kj}: è il prodotto **riga per colonna**.
![l'entrata (1, 1) di AC viene dalla riga 1 di A e dalla colonna 1 di C](figure/alg/prodotto_riga_colonna.png)
- si può fare solo se le colonne di A sono tante quante le righe di B; il risultato ha le righe di A e le colonne di B
- la sommatoria è un ciclo for su k da 1 a n
- matrice per vettore: A di taglia m × n per x ∈ 𝕂ⁿ dà Ax ∈ 𝕂^{m}; le matrici 1 × 1 si identificano con i numeri
```
(  1 2 )            ( −1 )
( −1 1 ) · (  1 ) = ( −2 )
(  0 3 )   ( −1 )   ( −3 )
```
! Trabocchetto: una 2 × 3 per una 2 × 2 non si può fare: 3 colonne contro 2 righe.
> Vedi anche: Proprietà del prodotto, Prodotto non commutativo

## Proprietà del prodotto {30}
= Il prodotto fra matrici è associativo, distributivo e compatibile con gli scalari; la trasposta ne inverte l'ordine.
- associativa: A(BC) = (AB)C
- distributiva: A(B + C) = AB + AC e (A + B)C = AC + BC
- con uno scalare: λ(AB) = (λA)B = A(λB)
- con la trasposta: ᵗ(AB) = ᵗB · ᵗA
- le taglie vanno scelte in modo che ogni somma e ogni prodotto abbiano senso
! Trabocchetto: ᵗ(AB) è ᵗB · ᵗA, non ᵗA · ᵗB: l'ordine dei fattori si inverte.
> Vedi anche: Prodotto fra matrici, Prodotto non commutativo, Trasposta

## Prodotto non commutativo {30}
= In generale AB ≠ BA: può esistere uno solo dei due prodotti, i due possono avere taglie diverse, oppure essere diversi pur avendo la stessa taglia.
- A colonna (1, 2) e B riga (0, 3): AB è la 2 × 2 con righe (0, 3) e (0, 6), BA è la 1 × 1 (6)
- stessa taglia, prodotti diversi:
```
A = ( 1 0 )   B = ( 0 1 )   AB = ( 0 1 ) = B   BA = ( 0 0 ) = 0
    ( 0 0 )       ( 0 0 )        ( 0 0 )            ( 0 0 )
```
! Trabocchetto: anche fra matrici quadrate della stessa taglia l'ordine dei fattori conta: AB e BA possono essere diverse.
> Vedi anche: Proprietà del prodotto, Traccia

## Traccia {30}
= La **traccia** di una matrice quadrata è la somma delle entrate della diagonale principale: tr(A) = A₁₁ + A₂₂ + … + A_{nn} = Σ_{k=1}^{n} A_{kk}.
- è definita solo per le matrici quadrate
- tr(AB) = tr(BA) per A, B ∈ M(n), anche quando AB ≠ BA: nella prova si scambiano le due somme
- A = (1 2; 3 4; 5 6) e B = (1 2 3; 4 5 6): AB è 3 × 3 e BA è 2 × 2, ma tr(AB) = 9 + 26 + 51 = 86 = 22 + 64 = tr(BA)
```
(  3  0  1 )
( −1 −2 −3 )   tr = 3 − 2 + 5 = 6
(  4  0  5 )
```
! Trabocchetto: si usa la diagonale principale, quella dall'alto a sinistra al basso a destra, non l'altra.
> Vedi anche: Prodotto non commutativo, Matrici quadrate speciali
