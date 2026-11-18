# 15. Equivalenze, Tautologie e Contraddizioni
## Una tautologia dimostrata con il ragionamento
Che **¬p ∨ q ∨ p** sia una tautologia si può vedere anche senza tavola, con una catena di formule equivalenti. Servono due proprietà della disgiunzione:
- **commutatività**: p ∨ q equivale a q ∨ p, perché la disgiunzione è vera quando almeno un argomento è vero, e l'ordine non conta;
- **associatività**: (p ∨ q) ∨ r equivale a p ∨ (q ∨ r), cioè le parentesi si possono spostare.

I passaggi, partendo da (¬p ∨ q) ∨ p:
1. per la commutatività, (¬p ∨ q) ∨ p equivale a (q ∨ ¬p) ∨ p;
2. per l'associatività, equivale a q ∨ (¬p ∨ p);
3. la parte tra parentesi, ¬p ∨ p, è il terzo escluso scritto nell'altro ordine, quindi è sempre vera: si ottiene q ∨ vero;
4. una disgiunzione con un argomento vero è vera.

Il risultato è vero qualunque sia il valore di q: la formula è una tautologia, come già visto con la tavola.

## Un'equivalenza che semplifica una formula
Quando è vera **(p ∧ q) ∨ (¬p ∨ q)**? La tavola di verità mostra che ha gli stessi valori di ¬p ∨ q, che è più corta: è vera in tutti i casi tranne quello con p vera e q falsa.

```
p q | p∧q  ¬p∨q | (p∧q) ∨ (¬p∨q)
1 1 |  1     1  |       1
1 0 |  0     0  |       0
0 1 |  0     1  |       1
0 0 |  0     1  |       1
```

Le colonne di ¬p ∨ q e della formula intera coincidono: le due formule sono equivalenti. Il motivo si vede anche a parole: p ∧ q è vera solo quando q è vera, e in quel caso ¬p ∨ q è già vera. Il pezzo p ∧ q non aggiunge quindi nessun caso nuovo e si può togliere.
