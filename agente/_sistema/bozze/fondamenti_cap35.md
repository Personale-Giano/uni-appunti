# 35. La Dimostrazione per Assurdo
## L'idea
Quando la strada diretta del cap. 31 non porta da nessuna parte, c'è un'altra possibilità: supporre che la tesi sia falsa e arrivare a una situazione impossibile. A lezione il docente la chiama **prova per contraddizione**, ed è lo stesso metodo che si dice **dimostrazione per assurdo**. Si è già accennata nel cap. 24.

**Definizione.** Una **contraddizione** è una proposizione della forma r ∧ ¬r, cioè sempre falsa (cap. 15).

(In parole povere: è affermare una cosa e il suo contrario insieme, come «piove e non piove». È sempre falsa, perché uno dei due lati è falso.)

**Definizione.** Una **dimostrazione per assurdo**, o **indiretta**, di p → q consiste nel supporre p vera e q falsa e nel dedurne una contraddizione.

(In parole povere: si fa finta che la tesi sia sbagliata e si vede dove si va a finire. Se si finisce in un'impossibilità, la tesi non poteva essere sbagliata. Rispetto alla dimostrazione diretta si ha un'ipotesi in più da usare: ¬q.)

## Perché funziona
L'implicazione p → q è falsa in un solo caso: p vera e q falsa. Se si dimostra che quel caso porta a una contraddizione, quel caso non può verificarsi, e l'implicazione è vera. In formule, p → q è equivalente a (p ∧ ¬q) → (r ∧ ¬r). Il libro lo verifica con una tavola di verità a otto righe; il ragionamento è breve: r ∧ ¬r è sempre falsa, quindi la formula di destra è falsa esattamente quando p ∧ ¬q è vera, cioè p vera e q falsa, come p → q.

**Dalla lavagna (registrazione 2025).** Il docente lo scrive anche in forma più nuda: per provare A si può provare ¬A → falso. Le due formule hanno la stessa tavola di verità: se A è vera, ¬A è falsa e falso → falso è vera; se A è falsa, ¬A è vera e vero → falso è falsa.

Due domande vengono spontanee, e nella registrazione 2025 il docente risponde a entrambe.

- **Perché assumo ¬q, se non è vero?** Non lo si assume perché lo si crede vero: lo si assume per escluderlo. Si lavora su una possibilità che alla fine verrà scartata.
- **Che cosa me ne faccio di dedurre il falso?** Non è lo scopo: serve per esclusione, per togliere l'unica possibilità che resta contro la tesi.

Secondo lui, il singolo ragionamento non lascia dubbi, mentre la regola generale all'inizio suona davvero strana.

## Prima un esempio diretto
**Esempio dalla lavagna (registrazione 2025).** Il quadrato di un dispari è dispari. Sia n = 2k + 1. Allora n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1. Con h = 2k² + 2k si ha n² = 2h + 1, quindi n² è dispari. La lettera è diversa da k perché sono valori diversi (cap. 31): con n = 7 si ha k = 3 e h = 24, infatti 49 = 2 · 24 + 1. Il docente sottolinea che la prova diretta dà una formula per calcolare h. L'esempio seguente non darà niente del genere.

## Esempio: se n² è pari allora n è pari
**Proposizione.** Per ogni intero n, se n² è pari allora n è pari.

(In parole povere: un quadrato pari viene sempre da un numero pari. Per esempio 16 viene da 4 e 144 viene da 12; 49 è dispari, e l'ipotesi non si applica.)

Per la via diretta si parte da n² = 2k₁, e non si vede come arrivare a n = 2k₂. Si ragiona allora per assurdo.

1. Si suppone n² pari e n non pari.
2. Un intero non pari è dispari: si usa che ogni intero è pari o dispari, e mai entrambe le cose.
3. Quindi n è dispari, e per l'esempio precedente anche n² è dispari.
4. Ma n² è pari per ipotesi: n² è insieme pari e non pari, cioè una contraddizione.

Quindi il caso «n² pari e n non pari» è impossibile, e l'implicazione è vera. Nella registrazione 2025 uno studente obietta che nessuno ha detto che n non è pari: appunto, risponde il docente, è la possibilità che si vuole escludere.

## Esempio: se x + y ≥ 2 allora x ≥ 1 oppure y ≥ 1
**Proposizione.** Per tutti i reali x, y, se x + y ≥ 2 allora x ≥ 1 oppure y ≥ 1.

(In parole povere: due numeri entrambi sotto 1 non possono arrivare a 2 sommati.)

**Prove su esempi (registrazione 2025).** Il docente prova coppie con somma 2: −3 e 5, −0,5 e 2,5, 0,9 e 1,1. Uno dei due è sempre almeno 1. Una coppia come 0,5 e 0,7 non è un controesempio, anche se sono entrambi sotto 1: la somma è 1,2, quindi l'ipotesi è falsa e l'implicazione è vera per difetto. Gli esempi servono solo a vedere che la proprietà resiste; poi serve un ragionamento, perché i reali sono infiniti.

**Dimostrazione per assurdo.** Si suppone x + y ≥ 2 e che la tesi sia falsa. La tesi è una disgiunzione, quindi per De Morgan:

¬(x ≥ 1 ∨ y ≥ 1) ≡ ¬(x ≥ 1) ∧ ¬(y ≥ 1) ≡ (x < 1) ∧ (y < 1).

Il passaggio finale è la negazione di un confronto (cap. 29). Sommando x < 1 e y < 1 si ottiene x + y < 2, che è in contraddizione con x + y ≥ 2.

**Quale dei due?** La prova dice che uno dei due è almeno 1, ma non quale: per saperlo bisogna controllare. Con due casi non è un problema, ma il docente avverte (registrazione 2025) che con una disgiunzione di cento affermazioni, ciascuna costosa da controllare, diventa un'informazione molto povera.

## Esempio: √2 è irrazionale
**Teorema (irrazionalità di √2).** Il numero √2 non è razionale.

(In parole povere: nessuna frazione elevata al quadrato dà esattamente 2. Si può approssimare √2 con frazioni quanto si vuole, senza mai arrivarci.)

Qui la via diretta non ha nemmeno un punto di partenza: «non è una frazione» non dà niente su cui lavorare. L'assurdo invece dà un'equazione da manipolare.

1. Si suppone √2 = p/q, con p e q interi non entrambi pari, cioè frazione ridotta ai minimi termini.
2. Si eleva al quadrato: 2 = p²/q², cioè 2q² = p².
3. Quindi p² è pari, e per l'esempio precedente p è pari: p = 2k.
4. Si sostituisce: 2q² = (2k)² = 4k², cioè q² = 2k².
5. Quindi q² è pari, e per l'esempio precedente q è pari.
6. Allora p e q sono entrambi pari, in contraddizione con il punto 1.

Il titolo della lezione di quest'anno include questo esempio. Nella registrazione 2025 il docente salta la prova, citata da uno studente come esempio già visto nei corsi di matematica, ma ne commenta il valore. Sapere che √2 è irrazionale non dà una formula: dà un'informazione negativa, cioè che è inutile cercare una frazione esatta, e che bisogna ripiegare su una soluzione approssimata.

## Esempio: 26 carte e un seme con almeno 7
**Proposizione.** Comunque si prendano 26 carte da un mazzo di 52, con 4 semi da 13 carte, esiste un seme di cui se ne hanno almeno 7.

(In parole povere: nel bridge, dove ogni coppia di giocatori riceve 26 carte, la coppia ha sempre almeno 7 carte di qualche seme. Non di tutti i semi: ne servirebbero almeno 28, 7 per seme, e anche così non sarebbe garantito.)

Si scrive S per l'insieme delle carte e S(Su) per il numero di carte del seme Su in S. L'enunciato è: per ogni S, se |S| = 26, allora esiste un seme Su con S(Su) ≥ 7.

La tesi falsa si ottiene con De Morgan generalizzate (cap. 22), portando la negazione dentro l'∃:

¬(∃ Su con S(Su) ≥ 7) ≡ ∀ Su, S(Su) < 7.

Quindi di ogni seme ci sono al massimo 6 carte. Poiché i semi sono 4, le carte sono al massimo 6 · 4 = 24, in contraddizione con |S| = 26.

Nella registrazione 2025 il docente scrive la tesi come una disgiunzione di quattro casi, almeno 7 cuori, oppure quadri, oppure fiori, oppure picche, e con De Morgan ottiene una congiunzione di quattro negazioni. È lo stesso calcolo, perché un ∃ su un dominio finito è una disgiunzione (cap. 23).

**Nota sul libro.** Nel libro questo esempio si trova sotto il titolo della contrapposizione, ma viene richiesto e svolto per assurdo, come a lezione. La **dimostrazione per contrapposizione** è il caso particolare in cui, da ¬q, si deduce proprio ¬p, provando così ¬q → ¬p, equivalente a p → q (cap. 17). Infatti qui da «al massimo 6 per seme» si deduce |S| ≠ 26, cioè la negazione dell'ipotesi; lo stesso capita negli altri esempi con un'ipotesi. Il metodo della contrapposizione verrà trattato per conto suo.

**Variazioni (registrazione 2025).** Rispondendo alle domande in aula, il docente nota che:

- bastano **25 carte**: qualunque numero maggiore di 24 va bene, e 26 viene solo dal bridge;
- non bastano **13 carte**: si potrebbe avere 4, 4, 4 e 1;
- con un mazzo di 54 carte con **2 jolly** servono **27 carte**: al peggio se ne hanno 24 di seme e i 2 jolly, cioè 26.

Si noti che la prova non dice quale seme ha le 7 carte. Per trovarlo bisogna contare; e dopo aver escluso tre semi, il quarto è per forza quello giusto.

## Che cosa dà e che cosa non dà
**Il limite del metodo (registrazione 2025).** Una prova per assurdo di «esiste un x con la proprietà» dice che x non può non esserci, ma non dice come trovarlo. Per un programma può non bastare: il docente la considera spesso un passo intermedio, che conferma di essere sulla strada giusta e lascia poi da cercare una spiegazione più informativa. Si usa comunque, perché tante volte non si sa fare altro. All'opposto, una prova che x non esiste dà almeno un'informazione utile: è inutile cercarlo.

I prossimi metodi di dimostrazione, a partire dalla contrapposizione, non sono ancora stati trattati a lezione.
