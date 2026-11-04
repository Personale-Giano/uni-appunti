# 41. Il Sistema Omogeneo Associato e la Struttura delle Soluzioni
## Il sistema omogeneo associato
Dopo aver visto come si risolve un sistema con Gauss-Jordan, la lezione 12 studia il problema in modo più teorico. Si consideri il sistema

a_{11}x_{1} + … + a_{1n}x_{n} = b_{1}, … , a_{k1}x_{1} + … + a_{kn}x_{n} = b_{k}.

**Definizione.** Il **sistema omogeneo associato** è quello ottenuto mettendo a zero tutti i termini noti b_{i}: a_{11}x_{1} + … + a_{1n}x_{n} = 0, … , a_{k1}x_{1} + … + a_{kn}x_{n} = 0.

(In parole povere: stesse equazioni, stessi coefficienti, ma a destra dell'uguale ci sono solo zeri.)

La matrice C = (A | b) rappresenta il sistema iniziale, mentre (A | 0), o più semplicemente A, rappresenta il sistema omogeneo associato. Si indicano con S ⊂ 𝕂ⁿ le soluzioni del sistema iniziale e con S_{0} ⊂ 𝕂ⁿ quelle del sistema omogeneo associato.

## Le soluzioni omogenee formano un sottospazio
**Proposizione.** Le soluzioni S_{0} ⊂ 𝕂ⁿ formano un sottospazio vettoriale di 𝕂ⁿ.

(In parole povere: sommando due soluzioni di un sistema omogeneo o moltiplicandone una per un numero, si ottiene ancora una soluzione.)

**Dimostrazione.** Si verificano le tre condizioni di sottospazio (cap. 20).
1. Il vettore 0 è soluzione: per ogni equazione a_{i1}·0 + … + a_{in}·0 = 0. Quindi 0 ∈ S_{0}.
2. Se x e y sono soluzioni lo è anche x + y: per ogni equazione a_{i1}(x_{1} + y_{1}) + … + a_{in}(x_{n} + y_{n}) = (a_{i1}x_{1} + … + a_{in}x_{n}) + (a_{i1}y_{1} + … + a_{in}y_{n}) = 0 + 0 = 0.
3. Se x è soluzione e λ ∈ 𝕂, anche λx è soluzione: a_{i1}(λx_{1}) + … + a_{in}(λx_{n}) = λ(a_{i1}x_{1} + … + a_{in}x_{n}) = λ·0 = 0.

S invece **non è un sottospazio**, perché non contiene l'origine, a meno che il sistema iniziale non sia già omogeneo: in quel caso S = S_{0}.

## Il legame tra S e S_{0}
**Proposizione.** Se S ≠ ∅, allora S si ottiene prendendo una qualsiasi soluzione x ∈ S e aggiungendole tutti i vettori di S_{0}.

(In parole povere: per conoscere tutte le soluzioni basta trovarne una sola e sommarle tutte le soluzioni del sistema con zeri a destra.)

Il motivo è questo. Se x ∈ S e x′ ∈ S_{0}, allora x + x′ è ancora soluzione del sistema iniziale, perché a_{i1}(x_{1} + x′_{1}) + … + a_{in}(x_{n} + x′_{n}) = b_{i} + 0 = b_{i}. Viceversa, se x″ è un'altra soluzione del sistema iniziale, allora x′ = x″ − x è soluzione del sistema omogeneo, perché a_{i1}(x″_{1} − x_{1}) + … + a_{in}(x″_{n} − x_{n}) = b_{i} − b_{i} = 0. Quindi le soluzioni si ottengono tutte, e precisamente, aggiungendo a un x ∈ S fissato le soluzioni x′ ∈ S_{0}. La soluzione x si chiama a volte **soluzione particolare**. (In parole povere: una soluzione qualsiasi, presa come punto di partenza.)

**Esempio.** Si consideri in ℝ³ il sistema x − y + z = 1, y − z = 2. Le soluzioni del sistema omogeneo associato x − y + z = 0, y − z = 0 sono i vettori del tipo (0, t, t). Prendendo la soluzione particolare (3, 0, −2), le soluzioni sono

(3, 0, −2) + (0, t, t) = (3, t, t − 2), al variare di t ∈ ℝ.

## I sottospazi affini
Geometricamente S è una versione spostata di S_{0}.

**Definizione.** Sia V uno spazio vettoriale. Un **sottospazio affine** di V è un qualsiasi sottoinsieme del tipo S = {x + v | v ∈ W} =: x + W, dove x è un punto fissato di V e W ⊂ V è un sottospazio vettoriale. La **dimensione** di S è la dimensione del sottospazio W.

(In parole povere: si prende un sottospazio, che passa sempre per l'origine, e lo si trasla senza ruotarlo: per esempio una retta parallela a una che passa per l'origine.)

![Le soluzioni di x + 2y = 2 sono la retta delle soluzioni di x + 2y = 0 spostata di una soluzione particolare.](figure/alg/soluzioni_affini.png|8.5)
