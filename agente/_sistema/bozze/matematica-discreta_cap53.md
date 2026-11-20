# 53. Il Teorema Fondamentale dell'Aritmetica e l'Infinità dei Primi
## L'enunciato
Il cap. 52 si è chiuso con l'equivalenza tra primi e irriducibili. Con questo strumento si dimostra il risultato che fa dei numeri primi i «mattoni» degli interi (è un'immagine, non un termine tecnico): ogni intero diverso da zero si ottiene moltiplicando dei primi, e in un solo modo.

**Teorema (fondamentale dell'aritmetica).** Ogni numero n ∈ ℤ con n ≠ 0 si fattorizza in modo unico come n = ± p_{1} · p_{2} · … · p_{s}, dove p_{1}, …, p_{s} sono numeri primi positivi. L'unicità va intesa a meno dell'ordine dei fattori.

(In parole povere: ogni numero si smonta in un prodotto di primi, e il risultato dello smontaggio è sempre lo stesso, comunque lo si faccia: cambia al massimo l'ordine in cui si scrivono i pezzi. Per esempio 12 = 2 · 2 · 3, e qualunque strada si segua si trovano sempre due 2 e un 3.)

Qualche precisazione sull'enunciato. Il segno ± serve per i numeri negativi: −12 = −(2 · 2 · 3). I primi si prendono positivi perché altrimenti l'unicità sarebbe falsa per motivi banali: 6 = 2 · 3 = (−2) · (−3). L'ordine dei fattori non conta: 2 · 3 · 2 e 2 · 2 · 3 sono la stessa fattorizzazione. Infine per n = ±1 il prodotto è **vuoto**, cioè s = 0: per convenzione il prodotto di zero fattori vale 1.

**Esempio.** Per fattorizzare 354 si divide ripetutamente per il più piccolo primo possibile, annotando i divisori in una colonna, come fa il docente:
- 354 : 2 = 177;
- 177 : 3 = 59;
- 59 : 59 = 1.

Quindi 354 = 2 · 3 · 59 (e 59 è primo: i suoi divisori positivi sono solo 1 e 59). Quando un primo si ripete si raccolgono i fattori uguali in potenze: per esempio 360 = 2 · 2 · 2 · 3 · 3 · 5 = 2^{3} · 3^{2} · 5.

## Dimostrazione dell'esistenza
Basta dimostrare il teorema per n > 0: se n < 0, si fattorizza −n, che è positivo, e si cambia il segno davanti.

**Dimostrazione (esistenza).** Si procede per assurdo.
1. Si supponga che non tutti i numeri naturali n > 0 siano fattorizzabili. Allora l'insieme dei naturali positivi non fattorizzabili non è vuoto, e quindi ha un **minimo**: sia n il più piccolo naturale positivo che non si fattorizza.
2. n > 1, perché 1 è il prodotto vuoto di primi, quindi è fattorizzabile.
3. n non è primo: altrimenti sarebbe già fattorizzato, come prodotto di un solo primo, n = p_{1}.
4. Siccome primo e irriducibile sono la stessa cosa (cap. 52), n non è irriducibile: quindi n = a · b con a, b non invertibili. Si possono prendere a e b positivi (n > 0, e se fossero entrambi negativi basta cambiare il segno a tutti e due); non essendo invertibili, sono a ≥ 2 e b ≥ 2, e quindi n = a · b ≥ 2a > a e allo stesso modo n > b. Dunque 1 < a < n e 1 < b < n.
5. Per la minimalità di n, i numeri a e b, che sono più piccoli di n, si fattorizzano: a = p_{1} · … · p_{s} e b = q_{1} · … · q_{t}, con i p_{i} e i q_{j} primi.
6. Ma allora n = a · b = p_{1} · … · p_{s} · q_{1} · … · q_{t} si fattorizza, contro l'ipotesi. ∎

Il passo 1 usa una proprietà dei numeri naturali: ogni sottoinsieme non vuoto di ℕ ha un minimo. È lo stesso ragionamento di un'induzione (cap. 5) raccontato al contrario: invece di salire da 1 in su, si suppone che esista un controesempio, si prende il più piccolo e si mostra che non può esistere, perché i numeri più piccoli di lui funzionano tutti.

## Dimostrazione dell'unicità
**Dimostrazione (unicità).** Sia n > 0 (per n < 0 il segno è fissato dal segno di n, e si ragiona su −n; per n = 1 il prodotto è vuoto). Si supponga che n abbia due fattorizzazioni in primi positivi, n = p_{1} · … · p_{s} = q_{1} · … · q_{t}, e, a meno di scambiare i nomi, che t ≥ s.
1. p_{1} divide n, cioè p_{1} | q_{1} · … · q_{t}. Siccome p_{1} è primo, divide almeno uno dei fattori (cap. 52, proprietà estesa a più fattori): esiste un indice i con p_{1} | q_{i}. Riordinando i q si può supporre i = 1, cioè p_{1} | q_{1}.
2. Ma q_{1} è primo, quindi irriducibile: i suoi divisori sono solo ±1 e ±q_{1}. Poiché p_{1} ≠ ±1 ed entrambi sono positivi, p_{1} = q_{1}.
3. Semplificando p_{1} = q_{1} da entrambi i lati (si può, perché è diverso da 0) si ottiene p_{2} · … · p_{s} = q_{2} · … · q_{t}.
4. Ripetendo lo stesso ragionamento si trova p_{2} = q_{2}, p_{3} = q_{3}, …, p_{s} = q_{s}.
5. A questo punto ci sono due casi. Se s = t, le due fattorizzazioni coincidono. Se s < t, dopo aver semplificato tutti i p rimane 1 = q_{s+1} · … · q_{t}, quindi q_{t} | 1: è assurdo, perché q_{t} è primo e quindi diverso da ±1.

Dunque s = t e i fattori sono gli stessi, al più in ordine diverso. ∎

Il docente barra con una grande croce la riga del caso s < t: indica che quel caso non può presentarsi, perché porta all'assurdo q_{t} | 1.

**Attenzione.** Nell'unicità sono usate entrambe le facce dei primi. Al passo 1 serve la proprietà «se p divide un prodotto, divide un fattore» (la definizione di primo); al passo 2 serve «i soli divisori sono ±1 e ±p» (la definizione di irriducibile), che per un primo vale grazie all'implicazione primo ⟹ irriducibile del cap. 47. L'implicazione opposta, irriducibile ⟹ primo (cap. 52), serve invece nell'esistenza, al passo 4. Il teorema nel suo insieme usa quindi l'equivalenza completa.

## I numeri primi sono infiniti
Il docente chiude la lezione con il teorema di Euclide. È un risultato antichissimo: compare già negli Elementi, l'opera di Euclide.

**Teorema (Euclide).** I numeri primi sono infiniti.

(In parole povere: per quanti primi si siano già trovati, ce n'è sempre almeno un altro. Non esiste «il primo più grande».)

**Dimostrazione.** Per assurdo, si supponga che i primi positivi siano solo un numero finito: p_{1} = 2, p_{2} = 3, …, p_{k}.
1. Si considera il numero N = p_{1} · p_{2} · … · p_{k} + 1.
2. N > 1, quindi per il teorema fondamentale dell'aritmetica (esistenza) N si fattorizza, e in particolare è divisibile per almeno un primo. Siccome i primi sono solo p_{1}, …, p_{k}, esiste un indice i con p_{i} | N.
3. D'altra parte p_{i} divide anche il prodotto p_{1} · … · p_{k}, perché ne è uno dei fattori.
4. Allora p_{i} divide la differenza N − p_{1} · … · p_{k} = 1 (cap. 44). Ma p_{i} | 1 è assurdo, perché un primo è diverso da ±1. ∎

**Esempio.** Con i primi 2, 3, 5 si ottiene N = 2 · 3 · 5 + 1 = 31, che è primo; con 2, 3, 5, 7 si ottiene 211, anch'esso primo.

**Attenzione.** La dimostrazione **non** dice che N = p_{1} · … · p_{k} + 1 sia sempre primo. Dice soltanto che N non è divisibile per nessuno dei primi della lista, quindi i suoi fattori primi sono primi nuovi. Per esempio, con i primi fino a 13, N = 2 · 3 · 5 · 7 · 11 · 13 + 1 = 30031 = 59 · 509 non è primo; ma 59 e 509 sono primi che non comparivano nella lista, ed è proprio questo che serve per l'assurdo.

Con il teorema fondamentale dell'aritmetica e l'infinità dei primi si completa il quadro della divisibilità in ℤ costruito a partire dal cap. 44: divisori e massimo comun divisore, divisione euclidea, algoritmo di Euclide e identità di Bézout, equazioni diofantine, e infine i primi, con cui si costruiscono per moltiplicazione, in un solo modo, tutti gli interi diversi da zero.
