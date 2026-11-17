# 46. La Divisione Euclidea
## Dividere con il resto
La divisione euclidea è la versione precisa della divisione con il resto che si impara alle elementari. La novità non è il calcolo, che resta quello di sempre, ma il fatto che si enuncia e si dimostra che cosa quel calcolo produce, anche quando i numeri sono negativi.

**Teorema (divisione euclidea).** Siano a, b ∈ ℤ con b ≠ 0. Allora esistono e sono unici due interi q e r tali che a = q · b + r, con 0 ≤ r < |b|. Il numero a si chiama **dividendo**, b **divisore**, q **quoziente** e r **resto**.

(In parole povere: il divisore b «ci sta» q volte in a, e avanza r. Il resto non è mai negativo ed è sempre più piccolo del divisore, preso senza segno.)

**Esempio.** Con a = 47 e b = 5 si ha 47 = 9 · 5 + 2: il quoziente è 9 e il resto è 2.

La condizione 0 ≤ r < |b| è parte essenziale dell'enunciato. Sono vere anche le uguaglianze 47 = 8 · 5 + 7 e 47 = 10 · 5 − 3, ma 7 e −3 non sono resti, perché 7 non è minore di 5 e −3 è negativo. Senza quella condizione le scritture sarebbero infinite; con quella condizione ce n'è una sola.

Il legame con il cap. 44 è immediato: b divide a esattamente quando il resto della divisione di a per b è 0. Se il resto è 0, infatti, a = q · b. Viceversa, se b | a, cioè a = c · b per qualche intero c, allora a = c · b + 0 è una scrittura con resto 0, e per l'unicità è l'unica possibile.

## Dimostrazione: l'esistenza
Ci si limita al caso a ≥ 0 e b > 0, che è quello della divisione di scuola; i casi con i segni negativi si riconducono a questo, come si vedrà negli esempi.

Si procede per **induzione su a**, in una variante dell'induzione del cap. 5: per dimostrare l'enunciato P(a) si suppone P(a') vera per ogni a' < a, e non soltanto per a − 1. È lecita perché equivale all'induzione ordinaria applicata all'enunciato «P vale per tutti i numeri da 0 fino ad a».
- Se a = 0 si prendono q = 0 e r = 0: infatti 0 = 0 · b + 0.
- Sia ora a > 0 e si supponga il teorema vero per ogni a' con 0 ≤ a' < a. Se a < b, il divisore non ci sta nemmeno una volta: si prendono q = 0 e r = a, perché a = 0 · b + a e 0 ≤ a < b. Se invece a ≥ b, si pone a' = a − b. Allora 0 ≤ a' perché a ≥ b, e a' < a perché b > 0; quindi per l'ipotesi induttiva esistono q' e r con a' = b · q' + r e 0 ≤ r < b. Siccome a' = a − b, si ricava a = b · q' + r + b = b · (q' + 1) + r. Basta quindi prendere q = q' + 1, con lo stesso resto r.

L'idea è quella di togliere b una volta alla volta finché ciò che rimane è più piccolo di b: ogni sottrazione fa aumentare di uno il quoziente, e quello che resta alla fine è il resto. Con 47 e 5 si toglie 5 per nove volte, 47, 42, 37, …, 7, 2, e ci si ferma a 2, che è minore di 5. Serve l'ipotesi su tutti i numeri più piccoli di a, e non solo su a − 1, perché da a si salta ad a − b.

## Dimostrazione: l'unicità
Si suppone b > 0; se b < 0 si ripete tutto con |b| al posto di b. Si supponga di avere due scritture, a = b · q + r = b · q' + r', con q, q' ∈ ℤ e i due resti compresi tra 0 e b − 1. A meno di scambiare i nomi si può supporre r ≤ r', cioè 0 ≤ r ≤ r' < b. Portando i termini con b da una parte e i resti dall'altra si ottiene:

b · (q − q') = r' − r.

Quindi b | r' − r. D'altra parte 0 ≤ r' − r < b. Ma un multiplo di b diverso da 0 è, in valore assoluto, almeno b (cap. 45), quindi l'unico multiplo di b tra 0 e b − 1 è 0. Dunque r' − r = 0, cioè r = r'.

A questo punto b · q + r = b · q' + r, quindi b · q = b · q', e siccome b ≠ 0 si conclude q = q'. ∎

## Quando ci sono numeri negativi
Il teorema vale per qualunque segno di a e di b, e il resto è **sempre** tra 0 e |b| − 1. Si parte dalla divisione tra i numeri senza segno e poi si aggiusta. Gli esempi usano tutti 2575 e 14, per cui la divisione in colonna dà quoziente 183 e resto 13: 2575 = 14 · 183 + 13.
- a = 2575, b = 14: è il caso di partenza, q = 183 e r = 13.
- a = −2575, b = 14: cambiando i segni si ottiene −2575 = 14 · (−183) − 13, ma −13 non è un resto. Si toglie e si aggiunge 14: −2575 = 14 · (−183) − 14 + 14 − 13 = 14 · (−184) + 1. Quindi q = −184 e r = 1.
- a = 2575, b = −14: basta spostare il segno sul quoziente, 2575 = (−14) · (−183) + 13. Quindi q = −183 e r = 13.
- a = −2575, b = −14: dal secondo caso, −2575 = 14 · (−184) + 1 = (−14) · 184 + 1. Quindi q = 184 e r = 1.

**Attenzione.** Quando il dividendo è negativo il resto non è quello della divisione tra i numeri positivi: il resto di −2575 diviso 14 è 1, non 13 e nemmeno −13. La regola, per a < 0 e b > 0, è questa: se la divisione di −a per b dà quoziente q e resto r ≠ 0, allora quella di a per b dà quoziente −q − 1 e resto b − r (qui −183 − 1 = −184 e 14 − 13 = 1). Se invece r = 0, il quoziente è −q e il resto rimane 0. Per b < 0 la regola è ancora più semplice: si divide a per −b, che è positivo, e da a = q · (−b) + r si ricava a = (−q) · b + r, cioè il quoziente cambia segno e il resto è lo stesso. Conviene sempre controllare alla fine che l'uguaglianza torni e che il resto sia tra 0 e |b| − 1.

## A che cosa serve
Il resto della divisione è già comparso con il periodo di una permutazione (cap. 37): se π ha periodo p, allora π^{k} = π^{r}, dove r è il resto della divisione di k per p. Nel cap. 37 l'esempio era con l'esponente 1000. Un altro esempio: se il periodo è 7, per calcolare π^{10000} si divide, 10000 = 7 · 1428 + 4, quindi π^{10000} = π⁴.

Un secondo esempio è la scrittura dei numeri in base 10: le cifre sono i resti di divisioni successive per 10. Da 24075 = 2407 · 10 + 5, poi 2407 = 240 · 10 + 7, 240 = 24 · 10 + 0, 24 = 2 · 10 + 4 e 2 = 0 · 10 + 2, si leggono le cifre 5, 7, 0, 4, 2, a partire da quella di destra.

Soprattutto, la divisione euclidea è lo strumento per studiare le proprietà aritmetiche degli interi: su di essa si basa il procedimento che calcola il massimo comun divisore (cap. 45) senza dover elencare i divisori.
