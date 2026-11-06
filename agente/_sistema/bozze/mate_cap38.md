# 38. Quali Periodi Sono Possibili in Sₙ
## Dal tipo alla tabella dei periodi
Poiché il periodo dipende solo dal tipo (cap. 37), si può rispondere a una domanda nuova: fissato n, **quali periodi possono avere le permutazioni di n elementi?** Basta elencare tutti i tipi possibili e calcolare per ciascuno il minimo comune multiplo. Per n grande sarebbe un lavoro lunghissimo, ma per n piccolo si fa abbastanza in fretta.

## L'esempio di S₆
I tipi sono gli elenchi in ordine non crescente di interi maggiori di 1 la cui somma è al massimo 6: gli elementi fissi non si scrivono nel tipo, perché si toglie sempre l'1. Con l'identità, che ha periodo 1, si ottiene questa tabella:

- identità: periodo 1;
- (2): periodo 2;
- (3): periodo 3;
- (4): periodo 4;
- (5): periodo 5;
- (6): periodo 6;
- (4, 2): periodo mcm(4, 2) = 4;
- (3, 3): periodo mcm(3, 3) = 3;
- (3, 2): periodo mcm(3, 2) = 6;
- (2, 2, 2): periodo 2;
- (2, 2): periodo 2.

I periodi possibili in S₆ sono quindi **1, 2, 3, 4, 5, 6**, e non ce ne sono altri. Per esempio, non esiste una permutazione di 6 elementi con periodo 8, perché 8 non compare nella tabella.

Attenzione al tipo (2, 2): la somma è 4 e non 6, ma è comunque un tipo di S₆. A lezione viene chiarito proprio questo punto: i due elementi rimanenti sono semplicemente lasciati fermi, e sarebbe (2, 2, 1, 1) se non si togliessero gli 1.

## Ragionare al contrario
La stessa idea si può usare nell'altra direzione: dato un periodo, **qual è il minimo numero di elementi che serve?** Bisogna trovare un tipo con quel minimo comune multiplo e con la somma più piccola possibile.

**Esempio: periodo 8.** Un ciclo di lunghezza 8 ha periodo 8, quindi 8 elementi bastano. Ne bastano meno? Se il minimo comune multiplo delle lunghezze è 8, ogni lunghezza divide 8, quindi vale 2, 4 o 8. Se nessuna fosse 8, sarebbero tutte al massimo 4 e il minimo comune multiplo non supererebbe 4. Serve dunque un ciclo di lunghezza 8, cioè proprio 8 elementi: né in S₆ né in S₇ c'è una permutazione di periodo 8.

**Esempio: periodo 10.** Qui non serve un ciclo di lunghezza 10, perché 10 = mcm(5, 2) e 5 + 2 = 7. Basta prendere in S₇ un ciclo di lunghezza 5 e, con gli altri due elementi, un ciclo di lunghezza 2. Per esempio (1 2 3 4 5) ∘ (6 7) ha periodo 10.

Questo è un fatto generale in matematica: lo stesso risultato si può usare in una direzione o nell'altra, a seconda dell'informazione che si ha e di quella che si cerca.
