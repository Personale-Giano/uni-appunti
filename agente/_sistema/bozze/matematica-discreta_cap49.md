# 49. L'Algoritmo di Euclide per il Massimo Comun Divisore
## Il problema
Nel cap. 45 il massimo comun divisore è stato calcolato con il metodo diretto: si elencano i divisori dei due numeri, si prendono quelli comuni e si sceglie il più grande. Con numeri come 3575 e 654 il metodo diventa faticoso, perché bisogna trovare tutti i divisori di entrambi. L'**algoritmo euclideo** (o algoritmo di Euclide) arriva al massimo comun divisore senza elencare nessun divisore: usa soltanto una serie di divisioni euclidee (cap. 46).

## Un esempio prima della regola
Il docente parte da un esempio: calcolare MCD(3575, 654). Si divide il numero più grande per il più piccolo; poi si divide il divisore per il resto appena trovato; poi il nuovo divisore per il nuovo resto, e così via finché il resto diventa 0.
- 3575 = 654 · 5 + 305;
- 654 = 305 · 2 + 44;
- 305 = 44 · 6 + 41;
- 44 = 41 · 1 + 3;
- 41 = 3 · 13 + 2;
- 3 = 2 · 1 + 1;
- 2 = 1 · 2 + 0.

A ogni riga il divisore e il resto «scalano» di un posto: il divisore diventa il nuovo dividendo, il resto diventa il nuovo divisore. La regola, che il docente scrive in rosso, è questa: **l'ultimo resto non nullo è il massimo comun divisore**. Qui l'ultimo resto non nullo è 1, quindi MCD(3575, 654) = 1.

**Esempio.** Per MCD(14575, 105):
- 14575 = 105 · 138 + 85;
- 105 = 85 · 1 + 20;
- 85 = 20 · 4 + 5;
- 20 = 5 · 4 + 0.

L'ultimo resto non nullo è 5, quindi MCD(14575, 105) = 5. Bastano quattro divisioni, mentre con il metodo diretto si sarebbero dovuti trovare tutti i divisori di 14575.

## La regola generale
Siano a, b ∈ ℤ con b ≠ 0. Si scrivono le divisioni successive, chiamando q_{1}, q_{2}, … i quozienti e r_{1}, r_{2}, … i resti:
- a = b · q_{1} + r_{1}, con 0 ≤ r_{1} < |b|;
- b = r_{1} · q_{2} + r_{2}, con 0 ≤ r_{2} < r_{1};
- r_{1} = r_{2} · q_{3} + r_{3}, con 0 ≤ r_{3} < r_{2};
- e così via, fino a r_{m−2} = r_{m−1} · q_{m} + r_{m};
- r_{m−1} = r_{m} · q_{m+1}, cioè la divisione con resto 0.

**Teorema (algoritmo euclideo).** Siano a, b ∈ ℤ con b ≠ 0. Le divisioni successive descritte sopra terminano dopo un numero finito di passi, e l'ultimo resto non nullo r_{m} è il massimo comun divisore: r_{m} = MCD(a, b).

(In parole povere: si continua a dividere il vecchio divisore per il vecchio resto; prima o poi il resto diventa 0, e il resto della riga appena sopra è il MCD.)

L'algoritmo finisce sempre perché i resti sono numeri naturali sempre più piccoli: |b| > r_{1} > r_{2} > r_{3} > … ≥ 0. Una successione di naturali che scende strettamente non può andare avanti per sempre, quindi dopo al massimo |b| passi si arriva a un resto 0. Se già il primo resto è 0, cioè b | a, l'ultimo resto non nullo è |b| stesso, e in effetti MCD(a, b) = |b| (cap. 45).

## Perché funziona
La dimostrazione del docente ha due parti: prima si fa vedere che r_{m} è un divisore comune di a e b, poi che ogni divisore comune divide r_{m}. Lo strumento è sempre la proposizione sui divisori di una somma (cap. 44): in a + b = s, se d divide due dei tre numeri, divide anche il terzo.

**Dimostrazione.**
1. Prima parte, r_{m} divide a e b (si risale dal basso). L'ultima riga, r_{m−1} = r_{m} · q_{m+1}, dice che r_{m} | r_{m−1}.
2. Nella penultima riga, r_{m−2} = r_{m−1} · q_{m} + r_{m}, il numero r_{m} divide entrambi gli addendi (divide r_{m−1}, quindi anche r_{m−1} · q_{m}, e divide se stesso), quindi divide la somma r_{m−2}.
3. Nella terzultima riga, r_{m−3} = r_{m−2} · q_{m−1} + r_{m−1}, il numero r_{m} divide r_{m−2} e r_{m−1}, quindi divide r_{m−3}.
4. Risalendo riga per riga si arriva alle prime due, b = r_{1} · q_{2} + r_{2} e a = b · q_{1} + r_{1}, e si trova r_{m} | b e r_{m} | a.
5. Seconda parte, ogni divisore comune divide r_{m} (si scende dall'alto). Sia d un intero con d | a e d | b. Dalla prima riga, r_{1} = a − b · q_{1}: d divide a e b · q_{1}, quindi divide r_{1}.
6. Dalla seconda riga, r_{2} = b − r_{1} · q_{2}: d divide b e r_{1}, quindi divide r_{2}. Proseguendo verso il basso si trova d | r_{3}, …, d | r_{m}.
7. Da d | r_{m} segue |d| ≤ r_{m} (cap. 45: un divisore non supera in valore assoluto il numero che divide), quindi in particolare d ≤ r_{m}.

Dunque r_{m} è un divisore comune di a e b, e nessun altro divisore comune lo supera: è il massimo comun divisore. ∎

La seconda parte dice anche qualcosa in più di quanto serva: ogni divisore comune di a e b non è soltanto minore o uguale al MCD, ma lo **divide**.

## Un esercizio svolto
**Esempio.** Si calcola MCD(252, 198). Il docente, il 17 novembre, comincia dividendo il più piccolo per il più grande: 198 = 252 · 0 + 198. È un passo lecito, che però si limita a scambiare i due numeri; il 19 novembre lo stesso esercizio parte direttamente dalla divisione del più grande per il più piccolo:
- 252 = 198 · 1 + 54;
- 198 = 54 · 3 + 36;
- 54 = 36 · 1 + 18;
- 36 = 18 · 2 + 0.

L'ultimo resto non nullo è 18, quindi MCD(252, 198) = 18. Un controllo conferma il risultato: 252 = 18 · 14 e 198 = 18 · 11, e 14 e 11 non hanno divisori comuni oltre a ±1.

**Attenzione.** Il MCD è l'ultimo resto **non nullo**, non l'ultimo resto (che è 0) e nemmeno l'ultimo quoziente. Nell'esempio di 3575 e 654 l'ultima riga è 2 = 1 · 2 + 0: il MCD è 1, il resto della riga prima, e non il quoziente 2. Inoltre i numeri da portare alla riga successiva sono il **divisore** e il **resto**, non il dividendo e il quoziente.

I segni non creano problemi: siccome n | −n e −n | n, i divisori di n e di −n sono gli stessi, e quindi MCD(a, b) = MCD(|a|, |b|), e conviene sempre lavorare con i numeri positivi. Per esempio MCD(−252, 198) = MCD(252, 198) = 18.

Le divisioni dell'algoritmo non servono solo a trovare il MCD: lette all'indietro, permettono di scriverlo come combinazione dei due numeri di partenza. È l'identità di Bézout, che si ottiene proprio ripercorrendo queste righe dal basso verso l'alto.
