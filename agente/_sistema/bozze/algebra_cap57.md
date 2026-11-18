# 57. Esercizi Svolti: Numeri Complessi
## Il primo foglio del tutorato
Questo capitolo e il successivo raccolgono gli esercizi del primo foglio del tutorato (1 novembre 2026). Gli argomenti sono quelli della prima parte del corso. Il foglio propone solo i testi: le soluzioni che seguono usano i metodi dei capitoli precedenti e **non sono soluzioni ufficiali**.

Qui si trovano gli esercizi 1-3, sui numeri complessi. Gli strumenti sono tre:
- in **forma algebrica** a + bi si fanno bene somme, prodotti e inversi; per l'inverso si usa z^{-1} = z̄ / |z|^{2} (cap. 5);
- in **forma polare** z = r e^{iθ} si fanno bene prodotti e potenze: i moduli si moltiplicano e gli argomenti si sommano (cap. 8), quindi z^{n} = r^{n} e^{inθ} (cap. 9);
- le **radici n-esime** di z_{0} = r_{0} e^{iθ_{0}} sono sempre n, e si trovano con la formula w_{k} = ⁿ√r_{0} · e^{i(θ_{0}/n + 2kπ/n)}, per k = 0, 1, …, n − 1 (cap. 9).

Per gli argomenti si usa la convenzione θ ∈ [0, 2π), la stessa del cap. 7.

## Esercizio 1: ricavare z da un'equazione e calcolare (3 + i)z^{-1}
**Testo.** Il numero complesso z soddisfa (1 + i)·z·(1 − i) = 6 + 4i. Calcolare (3 + i)·z^{-1}.

**Primo passo: trovare z.** Il primo membro è un prodotto di tre numeri complessi. In ℂ il prodotto è commutativo e associativo (cap. 4), quindi i fattori si possono riordinare e si possono moltiplicare prima i due che non contengono z:

(1 + i)(1 − i) = 1 − i^{2} = 1 + 1 = 2.

Non è un caso che venga un numero reale: 1 − i è il coniugato di 1 + i, e un numero per il suo coniugato dà il quadrato del modulo (cap. 5), qui 1^{2} + 1^{2} = 2. L'equazione diventa 2z = 6 + 4i, e dividendo per 2 si ottiene **z = 3 + 2i**.

**Secondo passo: l'inverso di z.** Con la formula del cap. 5 servono il coniugato e il quadrato del modulo: z̄ = 3 − 2i e |z|^{2} = 3^{2} + 2^{2} = 13. Quindi

z^{-1} = z̄ / |z|^{2} = (3 − 2i)/13.

**Terzo passo: il prodotto.** Si moltiplicano i numeratori, ricordando che i^{2} = −1:

(3 + i)(3 − 2i) = 9 − 6i + 3i − 2i^{2} = 9 − 3i + 2 = 11 − 3i.

Quindi **(3 + i)·z^{-1} = (11 − 3i)/13 = 11/13 − (3/13)i**.

Controllo: moltiplicando il risultato per z si deve ritrovare 3 + i. Infatti (11 − 3i)(3 + 2i) = 33 + 22i − 9i − 6i^{2} = 39 + 13i, e (39 + 13i)/13 = 3 + i.

## Esercizio 2: forma polare e una potenza
**Testo.** Scrivere in coordinate polari il numero z = ½(−√3 + i), poi calcolare z^{10}·z̄ e scriverlo nella forma a + bi.

**Forma polare.** Per prima cosa si legge la forma algebrica: z = −√3/2 + (1/2)i, cioè a = −√3/2 e b = 1/2. Il modulo è

r = √(a^{2} + b^{2}) = √(3/4 + 1/4) = √1 = 1.

Per l'argomento serve attenzione al quadrante, come avverte il trabocchetto del cap. 7. La parte reale è negativa e la parte immaginaria è positiva: il punto sta nel **secondo quadrante**, quindi l'angolo deve essere compreso fra π/2 e π. Il rapporto b/a vale (1/2)/(−√3/2) = −1/√3, e arctan(−1/√3) = −π/6, che è un angolo del quarto quadrante: da solo è sbagliato. Poiché a < 0 si aggiunge π:

θ = −π/6 + π = 5π/6.

Controllo con seno e coseno (cap. 7): cos(5π/6) = −√3/2 = a/r e sen(5π/6) = 1/2 = b/r. Quindi

**z = cos(5π/6) + i sen(5π/6) = e^{i·5π/6}**, con modulo 1 e argomento 5π/6.

**Il calcolo di z^{10}·z̄.** In forma algebrica bisognerebbe moltiplicare z per se stesso dieci volte; in forma polare bastano due regole. La potenza moltiplica l'argomento per 10 (cap. 9), e il modulo resta 1^{10} = 1:

z^{10} = e^{i·50π/6} = e^{i·25π/3}.

L'angolo 25π/3 supera il giro completo, e si riduce togliendo multipli di 2π: 25π/3 = 24π/3 + π/3 = 8π + π/3, e 8π sono quattro giri interi. Quindi z^{10} = e^{i·π/3}.

Il coniugato ha lo stesso modulo e argomento opposto (cap. 8): z̄ = e^{−i·5π/6}. Nel prodotto gli argomenti si sommano:

z^{10}·z̄ = e^{i(π/3 − 5π/6)} = e^{i(2π/6 − 5π/6)} = e^{−i·π/2}.

L'angolo −π/2 è lo stesso di 3π/2 (differiscono di un giro) e indica il punto più in basso della circonferenza unitaria: cos(−π/2) = 0 e sen(−π/2) = −1. Quindi

**z^{10}·z̄ = −i**, cioè a = 0 e b = −1.

**Una strada più corta.** Poiché z·z̄ = |z|^{2} = 1 (cap. 5), si può scrivere z^{10}·z̄ = z^{9}·(z·z̄) = z^{9}. L'argomento di z^{9} è 9·5π/6 = 15π/2 = 6π + 3π/2, quindi z^{9} = e^{i·3π/2} = −i: lo stesso risultato.

Controllo in forma algebrica: z^{10} = e^{i·π/3} = 1/2 + (√3/2)i e z̄ = −√3/2 − (1/2)i. Il prodotto è

(1/2 + (√3/2)i)(−√3/2 − (1/2)i) = −√3/4 − (1/4)i − (3/4)i − (√3/4)i^{2} = −√3/4 + √3/4 − i = −i.

## Esercizio 3: radici quarte, terze e quinte
**Testo.** Calcolare:
1. le radici quarte di z_{0} = −i;
2. le radici terze di z_{0} = 8;
3. le radici quinte di z_{0} = ½(−√3 + i).

Il procedimento è sempre lo stesso (cap. 9): si scrive z_{0} in forma polare, si prende la radice n-esima reale del modulo, si divide l'argomento per n e poi si aggiunge ogni volta 2π/n, fermandosi dopo n radici. Come ricorda il cap. 9, in ℂ «le radici n-esime» sono un insieme di n numeri e vanno elencate tutte.

**Radici quarte di −i.** Il numero −i sta sul semiasse immaginario negativo, a distanza 1 dall'origine: r_{0} = 1 e θ_{0} = 3π/2 (cap. 7, caso a = 0 e b < 0). Quindi −i = e^{i·3π/2}. Con n = 4 il modulo delle radici è ⁴√1 = 1 e gli angoli sono

θ_{0}/4 + 2kπ/4 = 3π/8 + kπ/2, per k = 0, 1, 2, 3.

Per sommare conviene scrivere π/2 = 4π/8: gli angoli sono 3π/8, 7π/8, 11π/8 e 15π/8. Le quattro radici sono

- **w_{0} = e^{i·3π/8}**;
- **w_{1} = e^{i·7π/8}**;
- **w_{2} = e^{i·11π/8}**;
- **w_{3} = e^{i·15π/8}**.

Controllo: elevando alla quarta l'argomento si moltiplica per 4. Per w_{0} si ottiene 4·3π/8 = 3π/2, proprio l'argomento di −i. Per w_{1} si ottiene 4·7π/8 = 7π/2 = 2π + 3π/2, di nuovo 3π/2 dopo aver tolto un giro; per w_{2} e w_{3} si trovano 11π/2 = 4π + 3π/2 e 15π/2 = 6π + 3π/2.

![Le quattro radici quarte di −i: i vertici di un quadrato inscritto nella circonferenza di raggio 1, ruotato di 3π/8.](figure/alg/es_radici_quarte_meno_i.png|8)

Sul piano le radici sono i vertici di un quadrato. Si passa da una alla successiva ruotando di π/2, cioè moltiplicando per i = e^{i·π/2}: w_{1} = i·w_{0}, w_{2} = −w_{0} e w_{3} = −i·w_{0}. Gli angoli non sono fra quelli di cui si ricordano a memoria seno e coseno, quindi la forma polare è la risposta naturale; con la calcolatrice, w_{0} = cos(3π/8) + i sen(3π/8) ≈ 0,383 + 0,924i.

**Radici terze di 8.** È l'esempio svolto nel cap. 9, e qui lo si ripercorre. Il numero 8 sta sul semiasse reale positivo: r_{0} = 8 e θ_{0} = 0, cioè 8 = 8 e^{i·0}. Con n = 3 il modulo delle radici è ³√8 = 2 e gli angoli sono 0 + 2kπ/3, cioè 0, 2π/3 e 4π/3. Questa volta gli angoli sono notevoli, perché cos(2π/3) = cos(4π/3) = −1/2, sen(2π/3) = √3/2 e sen(4π/3) = −√3/2, e conviene dare anche la forma algebrica:

- **w_{0} = 2 e^{i·0} = 2**;
- **w_{1} = 2 e^{i·2π/3} = 2(−1/2 + (√3/2)i) = −1 + i√3**;
- **w_{2} = 2 e^{i·4π/3} = 2(−1/2 − (√3/2)i) = −1 − i√3**.

Controllo in forma algebrica per w_{1}: (−1 + i√3)^{2} = 1 − 2i√3 + 3i^{2} = −2 − 2i√3, e poi (−2 − 2i√3)(−1 + i√3) = 2 − 2i√3 + 2i√3 − 6i^{2} = 2 + 6 = 8. Per w_{2}, che è il coniugato di w_{1}, il conto è lo stesso con i segni di i scambiati e dà ancora 8.

Da notare che in ℝ il numero 8 ha una sola radice terza, 2; in ℂ ne ha tre, e le altre due sono una la coniugata dell'altra.

**Radici quinte di ½(−√3 + i).** Il numero è lo z dell'esercizio 2, di cui si conosce già la forma polare: z_{0} = e^{i·5π/6}, con r_{0} = 1 e θ_{0} = 5π/6. È qui che un errore sull'argomento si pagherebbe: partendo da −π/6 invece che da 5π/6 si troverebbero le radici quinte di un altro numero, √3/2 − (1/2)i.

Con n = 5 il modulo delle radici è ⁵√1 = 1 e gli angoli sono

θ_{0}/5 + 2kπ/5 = π/6 + 2kπ/5, per k = 0, 1, 2, 3, 4.

Per sommare le frazioni si porta tutto a denominatore 30: π/6 = 5π/30 e 2π/5 = 12π/30. Gli angoli sono quindi 5π/30, 17π/30, 29π/30, 41π/30 e 53π/30, e le cinque radici sono

- **w_{0} = e^{i·π/6} = √3/2 + (1/2)i**;
- **w_{1} = e^{i·17π/30}**;
- **w_{2} = e^{i·29π/30}**;
- **w_{3} = e^{i·41π/30}**;
- **w_{4} = e^{i·53π/30}**.

Solo w_{0} ha un angolo notevole, e per questo è l'unica scritta anche nella forma a + bi. Tutti gli angoli sono minori di 2π = 60π/30, quindi rispettano la convenzione scelta.

Controllo: elevando alla quinta l'argomento si moltiplica per 5. Per w_{0}: 5·π/6 = 5π/6. Per w_{1}: 5·17π/30 = 17π/6 = 2π + 5π/6. Per w_{2}: 29π/6 = 4π + 5π/6. Per w_{3}: 41π/6 = 6π + 5π/6. Per w_{4}: 53π/6 = 8π + 5π/6. In tutti i casi, tolti i giri interi, resta 5π/6, l'argomento di z_{0}.

![Le cinque radici quinte di ½(−√3 + i): i vertici di un pentagono regolare inscritto nella circonferenza di raggio 1, con il primo vertice all'angolo π/6.](figure/alg/es_radici_quinte.png|8)

**Riepilogo.** Radici quarte di −i: e^{i·3π/8}, e^{i·7π/8}, e^{i·11π/8}, e^{i·15π/8}. Radici terze di 8: 2, −1 + i√3, −1 − i√3. Radici quinte di ½(−√3 + i): e^{i·π/6}, e^{i·17π/30}, e^{i·29π/30}, e^{i·41π/30}, e^{i·53π/30}.

## Che cosa ricordare
Nei tre esercizi tornano sempre le stesse scelte, e conviene fissarle:
1. per somme, inversi e controlli si lavora in forma algebrica; per potenze e radici si passa alla forma polare;
2. prima di calcolare un argomento si guarda in quale quadrante sta il punto: se la parte reale è negativa, ad arctan(b/a) va aggiunto π;
3. dopo una potenza l'angolo va riportato in [0, 2π) togliendo i giri interi;
4. le radici n-esime sono n, hanno tutte lo stesso modulo e angoli distanziati di 2π/n; per controllarle basta moltiplicare l'argomento per n e ritrovare quello di partenza, a meno di giri interi.

Il capitolo successivo prosegue con gli esercizi 4-10 del foglio, sulle matrici.
