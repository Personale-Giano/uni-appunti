# esercizi_riassuntivi_conn_quant

<!-- pagina 1 -->
Alcuni esempi relativi a formalizzazione,
connettivi proposizionali e quantiﬁcatori
Felice Cardone
felice.cardone@unito.it
Spesso il signiﬁcato di una proposizione A può essere spiegato meglio dicendo
che cosa la contraddice. Ecco una serie di esempi in cui si cerca di trovare
una proposizione equivalente a ¬A.
Inizio con un esempio aritmetico, relativo a un qualsiasi insieme numerico
(naturali, interi, razionali, reali). La negazione di 2 < 5 è 2 ≥5 e non 2 > 5:
bisogna considerare il caso in cui 2 = 5, che pur non essendo equivalente alla
negazione di 2 < 5, è incompatibile con essa.
La negazione di 2 < 5 e 3 > 1 è 2 ≥5 oppure 3 ≤1. Questo segue da una
delle due leggi di de Morgan:
¬(A ∧B) ≡¬A ∨¬B
¬(A ∨B) ≡¬A ∧¬B
Come esercizio si dimostri che queste equivalenze sono vere, cioè che
|= ¬(A ∧B) ↔¬A ∨¬B
|= ¬(A ∨B) ↔¬A ∧¬B
cosa che può essere dimostrata facendo vedere che
|= ¬(A ∧B) →¬A ∨¬B
|= ¬(A ∨B) →¬A ∧¬B
|= ¬A ∨¬B →¬(A ∧B)
|= ¬A ∧¬B →¬(A ∨B)
1

<!-- pagina 2 -->
o, in maniera equivalente, che
¬(A ∧B) |= ¬A ∨¬B
¬(A ∨B) |= ¬A ∧¬B
¬A ∨¬B |= ¬(A ∧B)
¬A ∧¬B |= ¬(A ∨B)
infatti |= A →B e A |= B sono equivalenti.
‘Qualche numero primo è pari’ può essere tradotta in formule usando un
funzioni proposizionali Primo(x) e Pari(x):
∃x (Primo(x) ∧Pari(x)
La negazione di questa proposizione ha allora la forma
∀x (¬Primo(x) ∨¬Pari(x))
che è equivalente a
∀x (Primo(x) →¬Pari(x))
perché, in generale, A →B ≡¬A ∨B (dimostrare come esercizio).
Usando ancora la funzione proposizionale Primo(x), traduciamo in una for-
mula la proposizione ‘Ci sono numeri primi minori di 17’, che diventa:
∃x (Primo(x) ∧x < 17)
La sua negazione ha la forma:
∀x (¬Primo(x) ∨¬(x < 17))
che è equivalente a
∀x (Primo(x) →x ≥17)
Consideriamo ora
Tutti i numeri > 5 sono anche > 3.
La sua traduzione è:
∀x (x > 5 →x > 3)
e la sua negazione diventa:
∃x ¬(x > 5 →x > 3)
2

<!-- pagina 3 -->
che è equivalente a
∃x (x > 5 ∧¬(x > 3))
perché, in generale, ¬(A →B) ≡A ∧¬B (dimostrare come esercizio).
Questo esempio ed il prossimo sono più complicati, e motivano anche l’uso
della formalizzazione delle proposizioni (cioè la loro traduzione in formule
della logica dei predicati) per poterle trasformare in formule equivalenti che
a loro volta verranno lette come proposizioni. Supponiamo di voler dire che,
dati insiemi A e B,
per ogni elemento x di A esiste almeno un elemento y di B per
cui x < y.
La sua formalizzazione è un esempio di utilizzo di quantiﬁcatori ristretti,
della forma ∀x ∈A . . . e ∃x ∈B . . . che si traducono, rispettivamente, come
∀x (x ∈A →. . .) e ∃x (x ∈A ∧. . .):
∀x ∈A ∃y ∈B x < y
o, in forma non abbreviata
∀x (x ∈A →∃y (y ∈B ∧x < y))
La negazione di questa formula ha una forma che può essere ottenuta dopo
alcune trasformazioni:
¬∀x (x ∈A →∃y (y ∈B ∧x < y)) ≡
≡∃x ¬(x ∈A →∃y (y ∈B ∧x < y))
≡∃x (x ∈A ∧¬(∃y (y ∈B ∧x < y))
≡∃x (x ∈A ∧∀y ¬(y ∈B ∧x < y))
≡∃x (x ∈A ∧∀y (y̸ ∈B ∨x ≥y))
≡∃x (x ∈A ∧∀y (y ∈B →x ≥y))
che si può leggere
c’è un elemento di A che segue ogni elemento di B.
Nelle stesse circostanze, la proposizione
C’è un elemento di A che è minore di ogni elemento di B
3

<!-- pagina 4 -->
si traduce come
∃x ∈A ∀y ∈B x < y
o, equivalentemente:
∃x (x ∈A ∧∀y(y ∈B →x < y))
La sua negazione diventa:
¬(∃x (x ∈A ∧∀y(y ∈B →x < y)) ≡
≡∀x ¬(x ∈A ∧∀y (y ∈B →x < y))
≡∀x (x̸ ∈A ∨¬(∀y (y ∈B →x < y))
≡∀x (x ∈A →∃y ¬(y ∈B →x < y))
≡∀x (x ∈A →∃y (y ∈B ∧x ≥y))
usando alcune equivalenze proposizionali e tra quantiﬁcatori menzionate
prima.
Osserviamo che si possono deﬁnire funzioni proposizionali usando quantiﬁ-
catori. Per esempio, possiamo deﬁnire una funzione proposizionale Pari(x),
già utilizzata prima, come segue
Pari(x)
def
= ∃n(x = 2 ∗n)
Allora la negazione ¬Pari(x) dovrà tenere conto della forma logica di questa
deﬁnizione, e sarà equivalente a ¬∃n(x = 2 ∗n) che, per motivi aritmetici,
quando x è intero equivale a ∃n(x = 2 ∗n + 1).
Consideriamo ora un altro esempio, in cui bisogna decidere quali delle for-
mule elencate sotto sono vere nella situazione illustrata dal disegno:
•
1
•
in
B
•
•
1 µ
^
•
+
•
µ
A
;
>
•
@
>
•
a
b
•
> •
_µ
ARB
4

<!-- pagina 5 -->
∀x∀y∀z (xRy ∧xRz →∃u(yRu ∧zRu))
(1)
∃x∀y yRx
(2)
∀x ∈A∃y ∈B xRy
(3)
∀x ∈B∃y ∈A yRx
(4)
∀x ∈A∀y ∈A∃z ∈B (xRz ∨yRz)
(5)
5
