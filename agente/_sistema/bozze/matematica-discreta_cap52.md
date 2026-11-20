# 52. Numeri Coprimi: Ogni Irriducibile è Primo
## Numeri coprimi
**Definizione.** Due interi a, b non entrambi nulli si dicono **coprimi** se MCD(a, b) = 1.

(In parole povere: due numeri sono coprimi quando non hanno nessun divisore in comune, a parte 1 e −1. Non serve che siano primi loro stessi: 8 e 9 non sono primi, ma sono coprimi, perché i divisori positivi di 8 sono 1, 2, 4, 8, quelli di 9 sono 1, 3, 9, e l'unico in comune è 1.)

**Esempio.** Nel cap. 49 l'algoritmo di Euclide ha dato MCD(3575, 654) = 1: i due numeri sono coprimi, anche se nessuno dei due è primo. Invece 252 e 198 non sono coprimi, perché MCD(252, 198) = 18.

Per due numeri coprimi l'identità di Bézout (cap. 50) prende una forma particolarmente semplice: esistono A, B ∈ ℤ con A · a + B · b = 1. Di conseguenza, per il criterio del cap. 51, l'equazione diofantina lineare a · x + b · y = c ha soluzioni **per ogni** c ∈ ℤ, perché 1 divide qualunque numero. Per esempio 3575x + 654y = c ha soluzioni intere qualunque sia c.

## Quando n divide un prodotto
Nel cap. 45 si è visto che, in generale, da n | a · b non segue che n divida uno dei due fattori. Il docente lo ricorda con un esempio: 6 | 4 · 3, perché 4 · 3 = 12 = 6 · 2, ma 6 non divide 4 e non divide 3. Il 6 si «forma» prendendo il 2 dal 4 e il 3 dal 3. Se però n non ha niente in comune con uno dei fattori, non può prendere pezzi da lì, e deve dividere tutto l'altro.

**Proposizione.** Siano n, a, b ∈ ℤ. Se MCD(n, a) = 1 e n | a · b, allora n | b.

(In parole povere: se n divide un prodotto ma non ha nessun divisore in comune con il primo fattore, allora deve dividere tutto il secondo. Per esempio 9 divide 4 · 18 = 72, e 9 è coprimo con 4: quindi 9 divide 18.)

**Dimostrazione.**
1. Poiché MCD(n, a) = 1, per l'identità di Bézout esistono A, B ∈ ℤ con A · n + B · a = 1.
2. Moltiplicando per b si ottiene A · n · b + B · a · b = b.
3. Il primo addendo, A · n · b, è un multiplo di n. Il secondo, B · a · b, è un multiplo di a · b, e quindi di n, perché n | a · b (cap. 45).
4. Allora n divide la somma, cioè b (cap. 44). ∎

**Attenzione.** L'ipotesi MCD(n, a) = 1 non si può togliere: con 6 | 4 · 3 la conclusione fallisce proprio perché MCD(6, 4) = 2 e MCD(6, 3) = 3. E non basta che n non divida a: 6 non divide 4, ma non è coprimo con 4, e infatti non divide 3.

## Irriducibile implica primo
Con questa proposizione si può finalmente dimostrare l'implicazione che nel cap. 47 era rimasta in sospeso. Si ricordano le due definizioni (cap. 44 e 47), per n ≠ 0, ±1:
- n è **irriducibile** se i suoi soli divisori sono ±1 e ±n;
- n è **primo** se, ogni volta che n | a · b, allora n | a oppure n | b.

**Proposizione.** Se n è irriducibile, allora n è primo.

(In parole povere: un numero che non ha divisori oltre a ±1 e a ±n, se divide un prodotto, deve dividere uno dei due fattori. Per esempio 7 è irriducibile, e infatti se 7 divide a · b allora divide a oppure b: 7 | 4 · 21 e 7 | 21.)

Il docente la presenta come un **corollario** della proposizione precedente.

**Dimostrazione.**
1. Sia n irriducibile e si supponga n | a · b. Bisogna dimostrare che n | a oppure n | b. Se n | a non c'è niente da dimostrare; si supponga allora n ∤ a e si dimostri che n | b.
2. Sia d = MCD(n, a). Allora d | n e d | a.
3. Poiché n è irriducibile, i suoi divisori sono solo ±1 e ±n; e d è positivo (cap. 45). Quindi d = 1 oppure d = |n|.
4. Il caso d = |n| è impossibile: siccome d | a, si avrebbe |n| | a, e quindi n | a (i segni non contano, cap. 45), contro l'ipotesi n ∤ a. Dunque d = 1, cioè n e a sono coprimi.
5. Ora MCD(n, a) = 1 e n | a · b: per la proposizione precedente, n | b. ∎

Il docente scrive il passo 3 come «d = 1 o d = n», e poi barra d = n perché escluso da n ∤ a; scrivere |n| tiene conto anche degli irriducibili negativi, e per n > 0 è la stessa cosa.

## Primo e irriducibile coincidono
Nel cap. 47 si è dimostrato che ogni primo è irriducibile; ora si è dimostrato che ogni irriducibile è primo. La conclusione, che il docente riquadra in rosso, è:

n è primo ⟺ n è irriducibile.

Nei numeri interi le due definizioni individuano quindi gli stessi numeri: ±2, ±3, ±5, ±7, ±11, … Per questo, d'ora in poi, si può usare la proprietà più comoda a seconda del momento: per riconoscere un primo si guardano i suoi divisori (se ha solo ±1 e ±n è primo), mentre nelle dimostrazioni si usa spesso la proprietà sui prodotti (se p | a · b allora p | a oppure p | b). Si chiarisce anche il contrasto con la terminologia di scuola segnalato nel cap. 47: la definizione scolastica di primo, «divisibile solo per 1 e per se stesso», è in realtà quella di irriducibile, e per gli interi il risultato non cambia.

**Esempio.** Per vedere che 13 è primo basta controllare i divisori: i positivi sono solo 1 e 13, quindi 13 è irriducibile e dunque primo. Da qui, senza fare altri conti, si sa che se 13 | a · b allora 13 divide uno dei due fattori. Per esempio 13 | 1001 = 77 · 13 e 1001 = 7 · 143: siccome 13 non divide 7, deve dividere 143, e infatti 143 = 11 · 13.

**Attenzione.** La proprietà dei primi si estende a prodotti con più fattori: se p è primo e p | a_{1} · a_{2} · … · a_{k}, allora p divide almeno uno degli a_{i}. Basta applicarla più volte: p divide a_{1} oppure il prodotto a_{2} · … · a_{k}; nel secondo caso divide a_{2} oppure a_{3} · … · a_{k}; e così via. Per i numeri riducibili, invece, la proprietà è falsa già con due fattori, come mostra 6 | 4 · 3.

L'equivalenza tra primi e irriducibili è lo strumento che serve per il risultato più importante di questa parte del corso: ogni intero diverso da zero si scrive, a meno del segno, in un solo modo come prodotto di primi. È il teorema fondamentale dell'aritmetica.
