# 13. I Connettivi: And, Or, Not, Xor ed Equivalenza
## Combinare le proposizioni
Un **connettivo** è un'operazione che prende uno o più valori di verità in ingresso e ne restituisce uno in uscita. Sono gli stessi che i circuiti elementari realizzano (porte and, or, xor e not, già visti nel capitolo 5: qui si guardano con la tavola di verità), e alcuni erano già stati anticipati. Il valore di verità della proposizione composta è sempre determinato dai valori di verità delle sue componenti. Nelle tavole che seguono si indicano il vero con **1** e il falso con **0**.

## La congiunzione (and)
La **congiunzione** p ∧ q si legge "p e q": è vera quando **entrambe** le proposizioni sono vere, e falsa se almeno una è falsa. Esempio del libro: "un decennio è di 10 anni e un millennio è di 100 anni" è falsa, perché la seconda parte è falsa.

## La disgiunzione (or) e il caso dell'xor
La **disgiunzione** p ∨ q si legge "p o q" ed è la disgiunzione **inclusiva**: è vera se è vera p, oppure è vera q, **oppure lo sono entrambe**. È falsa solo quando sono false tutte e due. Esempio del libro: "un millennio è di 100 anni o un millennio è di 1000 anni" è vera, perché basta la seconda parte.

Esiste anche la disgiunzione **esclusiva** (l'~aut~ del latino, **xor** in inglese), vera solo quando una delle due è vera e l'altra è falsa; non lo è quando sono vere entrambe. Nel parlato "o" può avere l'uno o l'altro significato, mentre in logica quando si scrive "or" si intende quella inclusiva.

Un esempio del docente: "piove e fa freddo". Se oggi non piove ma fa freddo (dove si fissa la soglia, per esempio, a 20 gradi), la **congiunzione è falsa**, perché la prima parte è falsa, mentre la **disgiunzione "piove o fa freddo" è vera**, perché la seconda parte è vera. Le frasi vanno poi sempre interpretate in un contesto.

La logica si occupa della **forma** delle proposizioni e dei rapporti tra loro, non del loro argomento: perciò "3 < 5 oppure Parigi è la capitale dell'Inghilterra" è ammessa ed è vera, perché 3 < 5 è vera.

## La negazione (not)
La **negazione** ¬p si legge "non p" e **scambia** il valore di verità: è vera quando p è falsa e viceversa. Esempio del libro: se p è "π è stato calcolato con un milione di cifre decimali nel 1954" (falsa: ci si arrivò solo nel 1973), ¬p è vera.

## Equivalenza e xor
L'**equivalenza** (o **uguaglianza** tra booleani) è vera quando i due valori sono **uguali**, falsa quando sono diversi. In programmazione corrisponde al test di uguaglianza (`==` in C++ e Java). Lo **xor** è la sua negazione: è vero quando i due valori sono **diversi**. L'equivalenza vale 0 nei due casi intermedi (valori diversi) e 1 nel primo e nell'ultimo (valori uguali); lo xor ha la tavola opposta.

## Le tavole di questi connettivi
Con l'ordine del libro (prima il vero, 1, poi il falso, 0) le tavole sono:

```
p q | p∧q  p∨q  xor  equiv
1 1 |  1    1    0    1
1 0 |  0    1    1    0
0 1 |  0    1    1    0
0 0 |  0    0    0    1

p | ¬p
1 | 0
0 | 1
```

## Notazioni diverse per lo stesso connettivo
Lo stesso connettivo si scrive in modi diversi a seconda del libro e del linguaggio: sono solo **sinonimi**, non hanno tavole di verità diverse. Se una notazione non è nota conviene chiedere che cosa significa.
- **Negazione**: "non" (italiano), ~not~ (inglese), il simbolo ¬, la tilde \~; nei linguaggi di programmazione (C, C++, Java) il punto esclamativo `!`.
- **Congiunzione**: "e", ~et~ (latino), ~and~, il simbolo ∧, la "e commerciale" &; in Java si scrive con la doppia `&&`.
- **Disgiunzione**: "o" e "oppure", ~vel~ (latino), ~or~, il simbolo ∨; in Java con la doppia barra verticale `||`.

Nei linguaggi di programmazione "and", "or" e "not" sono definiti esattamente come in logica (esempi del libro): per esempio `x < 10 && y > 4` è vera quando x è minore di 10 **e** y è maggiore di 4, `x < 10 || y > 4` quando vale almeno una delle due, e `!(x < 10)` quando x è maggiore o uguale a 10.

## La precedenza degli operatori
Quando una formula contiene ¬, ∧ e ∨ senza parentesi, si valuta **prima ¬, poi ∧, poi ∨**: è la **precedenza degli operatori**, come in algebra la moltiplicazione e la divisione si fanno prima di somma e sottrazione. Esempio del libro: con p falsa, q vera e r falsa, quanto vale ¬p ∨ q ∧ r? Si valuta prima ¬p, che è vera; poi q ∧ r, che è falsa; infine l'intera formula, vera ∨ falsa, che è **vera**.

## L'implicazione si rimanda
Manca ancora l'**implicazione**. Il docente l'ha rimandata alla prossima lezione, perché è il primo caso in cui la definizione logica si discosta da quella del linguaggio naturale. Finora congiunzione, disgiunzione, negazione ed equivalenza corrispondono abbastanza bene a quello che si intende nel parlato; con l'implicazione invece si possono creare confusioni, e sarà dedicata una lezione alle tavole di verità che la comprendono.

Nel prossimo capitolo si vede come si costruisce una tavola di verità per formule più complesse.
