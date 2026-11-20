# 50. L'Identità di Bézout
## L'enunciato
L'algoritmo di Euclide (cap. 49) trova il massimo comun divisore di due numeri con una catena di divisioni. Quella catena contiene però più informazione del solo risultato: ripercorrendola all'indietro si scopre che il MCD si può sempre ottenere combinando i due numeri di partenza con moltiplicazioni per interi e somme.

**Teorema (identità di Bézout).** Siano a, b ∈ ℤ non entrambi nulli e sia d = MCD(a, b). Allora esistono due interi A, B, non unici, tali che d = A · a + B · b.

(In parole povere: prendendo un certo numero di volte a e un certo numero di volte b, con il permesso di usare anche numeri negativi cioè di togliere, si riesce a ottenere esattamente il MCD. Per esempio con 126 e 35 si arriva a 7 così: due volte 126 meno sette volte 35, cioè 252 − 245 = 7.)

**Definizione.** Dati a, b ∈ ℤ, si chiama **combinazione lineare** (a coefficienti interi) di a e b ogni numero della forma A · a + B · b, con A, B ∈ ℤ.

(In parole povere: è quello che si ottiene sommando un certo numero di copie di a e un certo numero di copie di b, dove «un numero negativo di copie» vuol dire togliere. Per esempio 3 · 10 + (−2) · 4 = 22 è una combinazione lineare di 10 e 4.)

L'identità di Bézout dice quindi che il MCD è una combinazione lineare dei due numeri. Il docente sottolinea che i coefficienti A e B **non sono unici**: ne esistono infinite coppie, e l'algoritmo di Euclide ne trova una.

## La dimostrazione: risalire l'algoritmo
**Dimostrazione.** Si scrivono le divisioni dell'algoritmo di Euclide con le notazioni del cap. 49, a = b · q_{1} + r_{1}, b = r_{1} · q_{2} + r_{2}, …, fino a r_{m−2} = r_{m−1} · q_{m} + r_{m}, dove r_{m} = d è l'ultimo resto non nullo.
1. Dalla penultima divisione si ricava il MCD: d = r_{m} = r_{m−2} − q_{m} · r_{m−1}. Questa è già una combinazione lineare, ma di r_{m−2} e r_{m−1}.
2. La divisione precedente, r_{m−3} = r_{m−2} · q_{m−1} + r_{m−1}, permette di scrivere r_{m−1} = r_{m−3} − q_{m−1} · r_{m−2}. Sostituendo, d = r_{m−2} − q_{m} · (r_{m−3} − q_{m−1} · r_{m−2}) = −q_{m} · r_{m−3} + (1 + q_{m} · q_{m−1}) · r_{m−2}, e ora d è combinazione lineare di r_{m−3} e r_{m−2}.
3. Con la riga ancora precedente si scrive r_{m−2} come combinazione di r_{m−4} e r_{m−3}, e si sostituisce di nuovo.
4. A ogni passo i due numeri della combinazione salgono di una riga. Risalendo fino alle prime due divisioni si arriva a scrivere d come combinazione lineare di a e b. ∎

Al passo 2 il coefficiente di r_{m−3} è −q_{m}: il pedice m va tenuto, perché i quozienti delle varie righe sono in generale diversi.

Quando l'algoritmo è brevissimo la risalita è immediata. Se b | a, allora d = |b| e basta prendere A = 0 e B = ±1, per esempio MCD(35, 7) = 7 = 0 · 35 + 1 · 7. Se c'è una sola divisione con resto non nullo, allora d = r_{1} = a − q_{1} · b, cioè A = 1 e B = −q_{1}.

## Il procedimento in pratica
**Esempio.** Calcolare MCD(126, 35) e scrivere l'identità di Bézout. L'algoritmo di Euclide dà:
- 126 = 35 · 3 + 21;
- 35 = 21 · 1 + 14;
- 21 = 14 · 1 + 7;
- 14 = 7 · 2 + 0.

Quindi MCD(126, 35) = 7. Ora si risale. Dalla terza riga, 7 = 21 − 14. Dalla seconda, 14 = 35 − 21, e sostituendo:
7 = 21 − (35 − 21) = −35 + 2 · 21.
Dalla prima, 21 = 126 − 35 · 3, e sostituendo:
7 = −35 + 2 · (126 − 35 · 3) = 2 · 126 + (−1 − 6) · 35 = 2 · 126 + (−7) · 35.
Dunque A = 2 e B = −7. Controllo: 2 · 126 − 7 · 35 = 252 − 245 = 7.

Il trucco è non calcolare mai, durante la risalita, i prodotti numerici come 2 · 21: i numeri 126, 35, 21, … si lasciano scritti come simboli e si raccolgono soltanto i loro coefficienti. Se si scrive 2 · 21 = 42 si perde l'informazione su da dove veniva quel 21.

**Esempio.** Lo stesso procedimento per 252 e 198, di cui nel cap. 49 si è trovato MCD(252, 198) = 18 con le divisioni 252 = 198 · 1 + 54, 198 = 54 · 3 + 36, 54 = 36 · 1 + 18. Si cerca 18 = 252 · A + 198 · B:
- dalla penultima riga, 18 = 54 − 36;
- dalla terzultima, 36 = 198 − 54 · 3, quindi 18 = 54 − (198 − 54 · 3) = 54 · 4 − 198;
- dalla prima, 54 = 252 − 198, quindi 18 = (252 − 198) · 4 − 198 = 252 · 4 − 198 · 5.

Dunque A = 4 e B = −5. Controllo: 1008 − 990 = 18.

**Attenzione.** Durante la risalita si sostituiscono soltanto i **resti**, uno alla volta: a ogni passo si prende il resto con l'indice più alto rimasto nell'espressione e lo si ricava dalla riga in cui compare come resto; il dividendo e il divisore della prima riga, cioè a e b, non si sostituiscono mai, perché sono quelli a cui si vuole arrivare. Alla fine conviene sempre fare il controllo moltiplicando: un errore di segno è facilissimo e il controllo lo scopre subito.

## Infinite coppie di coefficienti
La coppia trovata con l'algoritmo non è l'unica. Partendo da 7 = 2 · 126 + (−7) · 35 e preso un qualsiasi k ∈ ℤ, il docente scrive

7 = (2 + 5k) · 126 + (−7 − 18k) · 35.

Funziona perché, sviluppando, i due termini in più si cancellano: 5 · 126 · k = 630k e 18 · 35 · k = 630k, il primo con il segno più e il secondo con il segno meno. Per k = 1, per esempio, si ottiene 7 = 7 · 126 + (−25) · 35, e infatti 882 − 875 = 7.

**Proposizione.** Siano a, b ∈ ℤ non entrambi nulli, d = MCD(a, b), e sia d = A · a + B · b. Allora per ogni k ∈ ℤ, posto A' = A + (b/d) · k e B' = B − (a/d) · k, si ha ancora d = A' · a + B' · b. In particolare le coppie che soddisfano l'identità di Bézout sono infinite (a k diversi corrispondono coppie diverse, perché a/d e b/d non sono entrambi nulli).

(In parole povere: si aggiunge un pezzo ad A e se ne toglie uno a B, scelti in modo che quello che si guadagna con a sia esattamente quello che si perde con b. Il risultato non cambia, e siccome k si può scegliere in infiniti modi, le coppie sono infinite.)

I numeri b/d e a/d sono interi, perché d divide sia a sia b: quindi A' e B' sono davvero interi. La verifica è un conto:

A' · a + B' · b = A · a + (ab/d) · k + B · b − (ab/d) · k = A · a + B · b = d.

Nell'esempio, con a = 126, b = 35 e d = 7, si ha b/d = 5 e a/d = 18, che sono proprio i numeri usati sopra. Per 252 e 198, con d = 18, b/d = 11 e a/d = 14: le coppie sono A' = 4 + 11k e B' = −5 − 14k, e per k = −1 si trova 18 = (−7) · 252 + 9 · 198, cioè −1764 + 1782 = 18.

Che la combinazione lineare A · a + B · b possa valere d è il cuore della questione. Ci si può chiedere, più in generale, quali numeri c si ottengano come combinazione lineare di a e b, cioè per quali c l'equazione a · x + b · y = c abbia soluzioni intere: è il problema delle equazioni diofantine lineari.
