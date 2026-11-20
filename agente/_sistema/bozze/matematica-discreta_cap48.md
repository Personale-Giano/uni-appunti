# 48. La Notazione Posizionale e i Cambi di Base
## Le cifre e la loro posizione
Nel cap. 46 si è visto che le cifre di un numero scritto in base 10 sono i resti di divisioni successive per 10. Il docente riparte da qui per spiegare che cosa significhi davvero «scrivere un numero», e per far vedere che la base 10 non ha niente di speciale: lo stesso meccanismo funziona con qualunque base.

Quando si scrive 67942, ogni cifra vale in base al posto che occupa: il 6 non vale sei, ma sei decine di migliaia; il 4 vale quattro decine. In formule:

67942 = 6 · 10^{4} + 7 · 10^{3} + 9 · 10^{2} + 4 · 10^{1} + 2 · 10^{0}.

È questo il significato della **notazione posizionale**: un sistema di scrittura dei numeri in cui il valore di una cifra dipende dalla sua posizione. I numeri romani, per confronto, non sono posizionali: in XX ciascuna X vale dieci, qualunque sia il suo posto.

Le cifre si ritrovano con la divisione euclidea (cap. 46), dividendo per 10 e poi dividendo di nuovo il quoziente:
- 67942 = 10 · 6794 + 2;
- 6794 = 10 · 679 + 4;
- 679 = 10 · 67 + 9;
- 67 = 10 · 6 + 7;
- 6 = 10 · 0 + 6.

Ogni quoziente diventa il dividendo della divisione successiva, e ci si ferma quando il quoziente è 0. I resti, letti **in ordine inverso** (dall'ultimo al primo), sono 6, 7, 9, 4, 2: proprio le cifre di 67942.

## La definizione
**Definizione.** Sia b ≥ 2 un numero naturale, detto **base**, e sia C un insieme di simboli, detti **cifre**, che rappresentano i numeri 0, 1, …, b − 1. Si dice **notazione posizionale** in base b di un numero n ∈ ℕ una successione di cifre n = c_{k} c_{k−1} … c_{1} c_{0}, con c_{i} ∈ C per ogni i, tale che n = c_{k} · b^{k} + c_{k−1} · b^{k−1} + … + c_{1} · b + c_{0}.

(In parole povere: si scrive il numero come somma di potenze della base, ciascuna presa un certo numero di volte, da 0 a b − 1; le cifre dicono proprio quante volte. La cifra più a destra conta le unità, quella accanto conta i gruppi da b, poi i gruppi da b^{2}, e così via.)

In base 10 le cifre sono i dieci simboli 0, 1, …, 9 e la formula è quella vista per 67942. Quando possono nascere dubbi, la base si indica in pedice, per esempio (2102)_{3}: è una convenzione comoda, che si userà in questo capitolo. Gli zeri a sinistra non cambiano il valore, perché moltiplicano potenze della base per 0: (0101)_{2} e (101)_{2} sono lo stesso numero.

**Esempio.** In base 2 le cifre sono soltanto 0 e 1, e i primi numeri si scrivono così:
- (0)_{2} = 0 e (1)_{2} = 1;
- (10)_{2} = 1 · 2 + 0 = 2;
- (11)_{2} = 1 · 2 + 1 = 3;
- (100)_{2} = 1 · 2^{2} + 0 · 2 + 0 = 4;
- (101)_{2} = 1 · 2^{2} + 0 · 2 + 1 = 5.

Il «10» della base 2 vale dunque due: in qualunque base, 10 indica la base stessa, cioè una volta b più zero unità.

## Dalla base b alla base 10
Per sapere quale numero rappresenta una scrittura in base b basta applicare la definizione: si moltiplica ogni cifra per la potenza della base corrispondente alla sua posizione e si somma.

**Esempio.** In base 3 le cifre sono 0, 1, 2. Allora (22)_{3} = 2 · 3 + 2 = 8 e

(2102)_{3} = 2 · 3^{3} + 1 · 3^{2} + 0 · 3 + 2 = 54 + 9 + 0 + 2 = 65.

Se la base è minore di 10 si usano come cifre i soliti simboli 0, 1, …, b − 1. Se invece b ≥ 10 i simboli da 0 a 9 non bastano più, e per convenzione si continua con le lettere: A = 10, B = 11, C = 12, e così via. Serve un simbolo solo per ogni cifra, altrimenti la scrittura diventerebbe ambigua: in base 13, «1 0» potrebbe voler dire la cifra dieci oppure le due cifre 1 e 0.

**Esempio.** In base 13 la scrittura (2BA7)_{13} rappresenta il numero

2 · 13^{3} + 11 · 13^{2} + 10 · 13 + 7 = 4394 + 1859 + 130 + 7 = 6390.

## Dalla base 10 alla base b
Per il cammino inverso si usa lo stesso procedimento visto per le cifre decimali, dividendo per b invece che per 10: si divide il numero per b, poi si divide il quoziente per b, e si continua finché il quoziente è 0. I resti sono tutti tra 0 e b − 1, quindi sono cifre in base b, e letti dall'ultimo al primo danno la scrittura cercata.

**Esempio.** Si converte 587 in base 3:
- 587 = 3 · 195 + 2;
- 195 = 3 · 65 + 0;
- 65 = 3 · 21 + 2;
- 21 = 3 · 7 + 0;
- 7 = 3 · 2 + 1;
- 2 = 3 · 0 + 2.

Leggendo i resti dal basso verso l'alto si ottiene 587 = (210202)_{3}. Il controllo si fa con la definizione: 2 · 3^{5} + 1 · 3^{4} + 0 · 3^{3} + 2 · 3^{2} + 0 · 3 + 2 = 486 + 81 + 0 + 18 + 0 + 2 = 587.

Perché funziona? La prima divisione scrive n = b · q + c_{0}, quindi c_{0} è proprio la cifra delle unità: nella formula della definizione tutti gli addendi tranne c_{0} contengono un fattore b, e l'unicità della divisione euclidea (cap. 46) garantisce che il resto sia c_{0}. Il quoziente q è il numero che si ottiene togliendo l'ultima cifra, c_{k} … c_{1}; dividendolo di nuovo per b si trova c_{1}, e così via. Ecco perché i resti escono a partire dalla cifra di destra e vanno letti al contrario.

**Esempio.** In base 2 il numero 45 si converte con le divisioni per 2: 45 = 2 · 22 + 1, 22 = 2 · 11 + 0, 11 = 2 · 5 + 1, 5 = 2 · 2 + 1, 2 = 2 · 1 + 0, 1 = 2 · 0 + 1. Letti al contrario, i resti danno 45 = (101101)_{2}, e infatti 32 + 8 + 4 + 1 = 45.

**Attenzione.** L'errore più comune è leggere i resti nell'ordine in cui si trovano: per 587 si otterrebbe (202012)_{3}, che vale 545 e non 587. Il primo resto trovato è la cifra delle unità, quindi va scritto **per ultimo**, a destra. Un secondo errore è fermarsi troppo presto: le divisioni continuano finché il quoziente diventa 0, e anche l'ultimo resto (il 2 di 2 = 3 · 0 + 2) è una cifra.

La divisione euclidea, ripetuta più volte facendo diventare il quoziente il nuovo dividendo, ha dato le cifre di un numero in qualsiasi base. Lo stesso schema di divisioni successive, con un'altra regola per scegliere il numero da dividere, è il cuore dell'algoritmo di Euclide per il massimo comun divisore.
