# 51. Le Equazioni Diofantine Lineari
## Soluzioni reali e soluzioni intere
Siano a, b, c ∈ ℤ con b ≠ 0, e si consideri l'equazione a · x + b · y = c. Se si cercano le soluzioni reali, la risposta è nota dalla geometria analitica: le coppie (x, y) che la soddisfano sono i punti di una retta del piano cartesiano, e quindi sono infinite. Il docente fa notare che il problema diventa molto più difficile se ci si interessa soltanto alle soluzioni **intere**, cioè ai punti della retta che hanno entrambe le coordinate in ℤ: può darsi che non ce ne sia nessuno.

**Definizione.** Un'equazione di cui si cercano le soluzioni intere si dice **equazione diofantina** (o diofantea). In particolare, dati a, b, c ∈ ℤ con b ≠ 0, l'equazione a · x + b · y = c, con le incognite x, y ∈ ℤ, si dice **equazione diofantina lineare**.

(In parole povere: è un'equazione in cui le frazioni e i numeri con la virgola non valgono come risposta. Per esempio 2x + 4y = 6 ha la soluzione intera x = 1, y = 1, mentre la coppia x = 0,5, y = 1,25 risolve l'equazione ma non conta.)

## Non sempre ci sono soluzioni
**Esempio.** L'equazione 6x + 24y = 7 non ha soluzioni intere. Se (x_{0}, y_{0}) fosse una soluzione, si avrebbe 6x_{0} + 24y_{0} = 7. Ma 6x_{0} è un multiplo di 6, e anche 24y_{0} = 6 · 4y_{0} è un multiplo di 6; quindi la loro somma è un multiplo di 6 (cap. 44). Si otterrebbe 6 | 7, che è assurdo.

Allo stesso modo l'equazione 3x + 12y = 1, che il docente scrive come esempio alla fine della lezione del 17 novembre, non ha soluzioni intere: il primo membro è sempre un multiplo di 3, e 1 non lo è. Come numeri reali, invece, le soluzioni sono infinite: per esempio x = 1/3, y = 0.

L'ostacolo, nei due esempi, è un divisore comune di a e b che non divide c. Viceversa, l'identità di Bézout (cap. 50) dice che, se d = MCD(a, b), l'equazione a · x + b · y = d ha sempre una soluzione: i coefficienti A, B dell'identità. Mettendo insieme le due osservazioni si ottiene il criterio completo.

## Il criterio: d | c
**Proposizione.** Siano a, b, c ∈ ℤ con b ≠ 0 e sia d = MCD(a, b). L'equazione diofantina lineare a · x + b · y = c ha soluzioni intere se e solo se d | c.

(In parole povere: si calcola il MCD dei due coefficienti; se divide il termine noto le soluzioni intere ci sono, altrimenti non ce n'è nemmeno una.)

**Dimostrazione.**
1. (⟹) Si supponga che (x_{0}, y_{0}) sia una soluzione, cioè a · x_{0} + b · y_{0} = c.
2. Poiché d | a, anche d | a · x_{0}; poiché d | b, anche d | b · y_{0} (cap. 45: un divisore di un fattore divide il prodotto).
3. Allora d divide la somma a · x_{0} + b · y_{0}, che è c (cap. 44). Quindi d | c.
4. (⟸) Si supponga d | c, cioè c = d · z per qualche z ∈ ℤ.
5. Per l'identità di Bézout esistono A, B ∈ ℤ con a · A + b · B = d.
6. Moltiplicando per z si ottiene a · (A · z) + b · (B · z) = d · z = c.
7. Quindi x_{0} = A · z, y_{0} = B · z è una soluzione. ∎

La dimostrazione non si limita a dire che le soluzioni esistono: dice anche come trovarne una. Si scrive l'identità di Bézout e la si moltiplica per z = c/d.

## Tutte le soluzioni
Il docente aggiunge che, se l'equazione a · x + b · y = c ha una soluzione (x_{0}, y_{0}), allora ne ha infinite, e si possono ottenere tutte con la formula

x = x_{0} + (b/d) · k,   y = y_{0} − (a/d) · k,   con k ∈ ℤ.

I numeri b/d e a/d sono interi, perché d divide a e b, quindi le coppie della formula sono davvero coppie di interi. Che siano soluzioni si verifica con lo stesso conto fatto per le infinite coppie di Bézout (cap. 50):

a · x + b · y = a · x_{0} + (ab/d) · k + b · y_{0} − (ab/d) · k = a · x_{0} + b · y_{0} = c.

A lezione il docente ha verificato soltanto questo, cioè che le coppie della formula sono soluzioni; che non ce ne siano altre è stato enunciato («si può provare») ma non dimostrato. All'esame conviene quindi saper usare la formula e saperne verificare le soluzioni con questo conto.

**Attenzione.** Nella formula si divide per d, non si usano a e b così come sono: x = x_{0} + b · k, y = y_{0} − a · k dà ancora soluzioni, ma non tutte, perché salta quelle intermedie quando d > 1. Inoltre i segni sono opposti: alla x si aggiunge il multiplo di b/d, alla y si toglie il multiplo di a/d. È facile scambiare a/d e b/d: il coefficiente di k nella x è quello che accompagna y nell'equazione.

## Un esercizio completo
Il docente riprende l'esercizio su 252 e 198, di cui si conoscono già il MCD e l'identità di Bézout (cap. 49 e 50):

MCD(252, 198) = 18,   252 · 4 + 198 · (−5) = 18.

**Esempio.** Sono i punti (b) e (c) dell'esercizio, il cui punto (a) è il calcolo del MCD e dell'identità di Bézout. (b) Determinare una soluzione intera dell'equazione 252x + 198y = 54. (c) Dire se l'equazione 252x + 198y = 7 ha soluzioni intere.

Per il criterio, l'equazione 252x + 198y = c ha soluzioni intere se e solo se 18 | c.
- Caso (b): c = 54 = 18 · 3, quindi le soluzioni ci sono. Moltiplicando per 3 l'identità di Bézout si ottiene 252 · (4 · 3) + 198 · (−5 · 3) = 18 · 3, cioè 252 · 12 + 198 · (−15) = 54. Una soluzione è x_{0} = 12, y_{0} = −15. Controllo: 3024 − 2970 = 54.
- Caso (c): 18 non divide 7, quindi l'equazione non ha soluzioni intere.

Con la formula si trovano anche tutte le altre soluzioni di (b): qui b/d = 198/18 = 11 e a/d = 252/18 = 14, quindi

x = 12 + 11k,   y = −15 − 14k,   con k ∈ ℤ.

Per k = −1 si ottiene la soluzione più semplice, x = 1, y = −1: in effetti 252 − 198 = 54, cosa che si poteva anche notare a occhio. Il procedimento con Bézout, però, funziona sempre, anche quando la soluzione non si vede.

Riassumendo, per risolvere a · x + b · y = c:
1. si calcola d = MCD(a, b) con l'algoritmo di Euclide;
2. si controlla se d | c: se no, non ci sono soluzioni e ci si ferma;
3. si scrive l'identità di Bézout d = A · a + B · b risalendo l'algoritmo;
4. si moltiplica per c/d e si ottiene la soluzione x_{0} = A · (c/d), y_{0} = B · (c/d);
5. se servono tutte le soluzioni, si usa la formula con b/d e a/d.

Il criterio ha un caso particolare molto importante: quando d = 1 il termine noto è sempre divisibile per d, e l'equazione ha soluzioni qualunque sia c. I numeri con MCD uguale a 1 hanno un nome e proprietà notevoli, che portano a chiudere il discorso tra primi e irriducibili rimasto aperto nel cap. 47.
