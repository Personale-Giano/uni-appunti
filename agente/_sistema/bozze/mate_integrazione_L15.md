@@ dopo cap49.2
Nel riepilogo all'inizio della lezione del 19 novembre il docente osserva che l'algoritmo può richiedere poche divisioni o parecchie, ma è comunque più veloce che passare dalla scrittura dei due numeri come prodotto di primi. Quella strada, tra l'altro, a questo punto del corso non è ancora autorizzata, perché la scomposizione in primi non è ancora stata dimostrata: arriverà solo con il teorema fondamentale dell'aritmetica (cap. 53).

@@ dopo cap51.20
A lezione il docente presenta questo criterio come una rilettura dell'identità di Bézout. Fissati a e b, ci si chiede per quali termini noti c l'equazione a · x + b · y = c si risolve negli interi. Se r è un divisore comune di a e b, allora r divide a · x e b · y qualunque siano x e y, e quindi divide anche la somma: il primo membro è sempre un multiplo di r, in particolare di d. Se c non è un multiplo di d non ci sono soluzioni, e il docente precisa che non è questione di bravura: le soluzioni non ci sono proprio. Se invece c = d, la soluzione la dà l'algoritmo di Euclide risalito all'indietro. Resta il caso in cui c è un multiplo k · d di d con k diverso da 1, e lì basta moltiplicare, come nel passo 6 della dimostrazione.

@@ dopo cap51.48
A lezione la soluzione x = 2, y = −1 di 6x + 10y = 2 (lo stesso risultato dell'algoritmo appena visto) il docente la trova a occhio: con numeri così piccoli, osserva, di solito una soluzione si trova per tentativi, mentre con numeri grandi è meglio usare l'algoritmo, che è più sicuro. Con la formula della sezione seguente (conto nostro, con b/d = 5 e a/d = 3) tutte le soluzioni di 6x + 10y = 8 sono x = 8 + 5k, y = −4 − 3k; per k = −1 si trova x = 3, y = −1, e infatti 18 − 10 = 8.

Il docente aggiunge una lettura geometrica. I punti del piano cartesiano con entrambe le coordinate intere, come (0, 0), (1, 0), (0, 1), (0, 2), formano una griglia, e cercare le soluzioni intere vuol dire cercare i punti in cui la retta a · x + b · y = c passa per un nodo della griglia. Il criterio dice che questo succede solo quando il termine noto è un multiplo del MCD; altrimenti la retta è messa in modo da non toccare mai nessun punto della griglia.

@@ dopo cap52.29
A voce, il 19 novembre, il docente lo dimostra tutto in una volta, usando direttamente l'identità di Bézout. Per giustificare che MCD(n, a) = 1 osserva che, siccome n è irriducibile, i suoi soli divisori positivi (per n > 0) sono 1 e n stesso; 1 è sempre un divisore comune, e n non lo è, perché n ∤ a. Poi aggiunge una raccomandazione: davanti a due numeri con massimo comun divisore 1 bisogna avere un «riflesso pavloviano» e pensare subito all'identità di Bézout. Il conto procede così (qui A moltiplica a e B moltiplica n, al contrario del passo 1 della proposizione precedente).
1. Per Bézout esistono A, B ∈ ℤ con A · a + B · n = 1.
2. Moltiplicando a sinistra e a destra per b si ottiene A · a · b + B · n · b = b.
3. Siccome n | a · b, si può scrivere a · b = k · n per un certo k ∈ ℤ; sostituendo, A · k · n + B · n · b = b.
4. Raccogliendo n (la proprietà distributiva usata al contrario): n · (A · k + B · b) = b.
5. Non si sa chi siano A, B e k, ma sono interi, quindi A · k + B · b è un intero: n moltiplicato per un intero dà b, cioè n | b. ∎

**Esempio.** Un controllo con i numeri (conto nostro): n = 7, a = 4, b = 21. Si ha 7 | 4 · 21 = 84 = 12 · 7 e 7 ∤ 4. Bézout per 4 e 7 dà 2 · 4 + (−1) · 7 = 1, cioè A = 2 e B = −1. Moltiplicando per 21: 2 · 84 + (−1) · 7 · 21 = 168 − 147 = 21. Con k = 12 si ha A · k + B · b = 24 − 21 = 3, e infatti 21 = 7 · 3.

@@ dopo cap52.32
A lezione il docente lo enuncia come un unico teorema: n è irriducibile se e solo se è primo. Il teorema, dice, chiarisce la differenza tra i due concetti dicendo che non c'è nessuna differenza: le due definizioni descrivono esattamente lo stesso insieme di numeri, e tenerle entrambe serve perché nel teorema fondamentale dell'aritmetica (cap. 53) si usano tutte e due. Sul controllo dell'irriducibilità aggiunge una precisazione: quando n = a · b con fattori non invertibili, a e b sono più piccoli di n in valore assoluto, quindi «basta» controllare che nessun numero più piccolo di n sia un suo fattore; ma quel «basta» va preso tra virgolette, perché quando n è grande provare tutti i numeri più piccoli non è un controllo efficiente dal punto di vista del calcolo.

@@ dopo cap53.5
A lezione il teorema è enunciato per n ≠ 0, 1, −1 (negli appunti del docente per n ≠ 0, con il prodotto vuoto per ±1), con i primi che possono anche ripetersi: per esempio 27 = 3 · 3 · 3. Il docente spiega anche perché 1 non si considera primo. Nella classificazione del corso 1 è invertibile e fa categoria a sé; se la definizione non escludesse ±1, però, soddisferebbe la condizione di irriducibilità, perché si scrive solo come 1 · 1 o (−1) · (−1), e in ogni scrittura un fattore è invertibile. Il motivo della convenzione è l'unicità: se 1 fosse primo, si potrebbe scrivere 10 = 2 · 5, ma anche 10 = 1 · 2 · 5 = 1 · 1 · 2 · 5 = 1 · 1 · 1 · 2 · 5, e l'unicità salterebbe. Si dovrebbe allora precisare ogni volta di guardare la scrittura senza gli 1; è molto più semplice stabilire che 1 non è primo, e allora la scrittura è davvero unica.

@@ dopo cap53.48
A lezione il docente premette che, siccome primi e irriducibili sono gli stessi numeri, si può dimostrare l'esistenza della scrittura come prodotto di irriducibili, che è la stessa cosa: è quello che fanno i passi 1 e 3 della dimostrazione per induzione forte qui sopra. Alla fine commenta che l'esistenza è la parte facile: il punto cruciale della dimostrazione è far vedere che la scrittura è unica.

@@ dopo cap53.34
Un altro modo di dirlo, come osserva il docente: per ogni n esiste un primo più grande di n.

@@ dopo cap53.55
Il docente ricorda che sui numeri primi c'è una letteratura enorme, con moltissimi problemi ancora aperti. Per esempio, quanti sono i primi più piccoli di un numero fissato, come 10^{700}, si sa soltanto in modo approssimato (asintoticamente).

Sono questioni che non riguardano il corso; però da qualche decennio gli algoritmi per trovare primi grandi e per scomporre rapidamente un numero in primi sono diventati importanti anche in pratica: le procedure per il commercio elettronico e lo scambio di informazioni riservate si basano in un modo o nell'altro sui numeri primi, e anche il decoder che riceve una partita di calcio a pagamento decodifica il segnale facendo conti con i primi. Il docente accenna alla possibilità di mostrare, verso la fine del corso, un esempio molto semplice di scambio di informazioni riservate basato sui primi.
