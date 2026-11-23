Tavole di Verità
Lezione 7 di Fondamenti 
12 Ottobre 2026

Disgiunzione indicata con: , ||, vel, or, oppure, o





Negazione indicata con: non x, not x, ¬x, ~x, !


Congiunzione indicata con: &, , e, et, and, &&



Disgiunzione esclusiva indicata con: xor, aut



Attraverso le tavole di verità possiamo controllare se due affermazioni sono equivalenti, cioè se hanno gli stessi valori di verità purché le loro proposizioni atomiche abbiano gli stessi valori.

Un altro uso delle tavole di verità: controllare se una affermazione è sempre vera, per esempio nel model-checking (questo esempio non fa parte del corso).
Le formule proposizionali possono essere provate equivalenti anche con il ragionamento. Come esempio di ragionamento proviamo che le seguenti proposizioni sono equivalenti:
~(p v q) vera
= p v q falsa
= p, q sono falsi
= ~p, ~q sono vere
= (~p & ~q) è vera


Un esempio di tavola di verità: controlliamo che (p v q) & ~p   = ~p & q




Un altro esempio di tautologia: ~p v p è tautologia e viene chiamata “terzo escluso”
Tautologia del Terzo Escluso

Un altro esempio di ragionamento. Proviamo che (~p v q) v p è una tautologia provando che le seguenti proposizioni sono equivalenti: 
(~p v q) v p = (per commutatività del v) 
(q v ~p) v p = (per associatività del v)
q v (~p v p) = (perché (~p v p) è una tautologia, come abbiamo appena visto)
q v Vero      = (per definizione v)
Vero
Proviamo che (~p v q) v p è una tautologia usando invece una tavola di verità:





Un altro esempio: quando:
(p & q) v (~p v q)
è vero? Questa affermazione equivale a (~p v q), come possiamo controllare scrivendo la tavola di verità

Tavola di verità di (~p v q) e di (p & q) v (~p v q)
