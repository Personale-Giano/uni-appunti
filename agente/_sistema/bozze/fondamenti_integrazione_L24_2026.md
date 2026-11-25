@@ dopo cap45.67
(lezione 2026) Nella lezione 24 il docente torna sul problema dei nomi. Le funzioni biiettive sono dette, in italiano, **relazioni uno a uno**, mentre l'inglese ~one-to-one~, che sembra la stessa espressione, vuol dire iniettiva. È una pessima situazione, commenta, quando la stessa frase cambia significato cambiando lingua. Il suo consiglio è di non usare «uno a uno», che è ambiguo e porta a confondersi, e di dire invece **iniettiva** e **biiettiva**, che hanno lo stesso significato in italiano e in inglese.

@@ dopo cap47.57
(lezione 2026) Nella parte registrata della lezione 24 non compaiono somme e prodotti: dopo le stringhe il docente passa alle relazioni (cap. 50). Questa sezione resta quindi solo dal libro.

@@ dopo cap47.77
(lezione 2026) Nemmeno la lezione 24 tratta le sottosequenze: nella parte registrata il docente riprende la rovesciata e la concatenazione di stringhe (cap. 48 e 49) e poi passa alle relazioni (cap. 50). La sezione resta quindi basata sulla registrazione 2025 e sul libro.

@@ dopo cap48.60
**Le stringhe nella lezione 24.** (lezione 2026) La registrazione della lezione 24 (23 novembre 2026) parte verso le 9:31 (orologio sullo schermo proiettato), già nel mezzo delle stringhe. Negli appunti che il docente proietta, una stringa è una funzione α: [1, n] → X per qualche intero n ≥ 0, che è la sua lunghezza, e X\* è l'insieme di tutte le stringhe su X, con la stringa vuota λ: per X = {a, b}, X\* = {λ, a, b, ab, ba, aa, bb, aab, …}. Il docente si concentra sulla rovesciata, definita con una formula sugli indici, e dimostra che rovesciare due volte riporta alla stringa di partenza espandendo le definizioni: questa parte è nel cap. 49. Poi rifà i due esercizi del libro che seguono qui sotto, il rovesciamento e la concatenazione. Le sottostringhe non compaiono nella parte registrata.

@@ dopo cap48.22
(lezione 2026) Il docente descrive anche come cambiano gli indici: se la prima stringa ha n elementi, il primo elemento della seconda diventa l'elemento di posto n + 1, e se la seconda ne ha m, il suo ultimo elemento finisce al posto n + m. Concatenando una stringa di lunghezza 10 e una di lunghezza 20 se ne ottiene una di lunghezza 30, e l'ultima lettera della seconda ha adesso il posto 30. È, dice, il modo più comune di combinare dei testi: scriverli in fila. Con le stringhe scritte come funzioni (cap. 49), se |α| = n e |β| = m, questo vuol dire (αβ)(i) = α(i) per 1 ≤ i ≤ n e (αβ)(i) = β(i − n) per n < i ≤ n + m (formula nostra).

@@ dopo cap48.26
(lezione 2026) Nella lezione 24 il docente dimostra questo fatto partendo dalla formula della rovesciata, α^{R}(i) = α(n + 1 − i), con un'espansione delle definizioni: è il cap. 49.

@@ dopo cap48.37
(lezione 2026) Nella lezione 24 il docente svolge l'esercizio subito dopo aver dimostrato che (α^{R})^{R} = α (cap. 49), e con quel risultato in mano lo annuncia come facile. Espande prima la definizione di biiezione in tre richieste, che controlla in quest'ordine: f è una funzione, f è suriettiva, f è iniettiva. Che f sia una funzione lo dice la definizione stessa, che fornisce per ogni stringa α esattamente un'immagine.

@@ dopo cap48.39
(lezione 2026) Nel 2026 l'iniettività la dimostra il docente stesso, con le stesse parole proiettate sullo schermo: espandendo la definizione di f si ottiene α^{R} = β^{R}, e per provare la tesi basta applicare di nuovo R: (α^{R})^{R} = (β^{R})^{R}, dunque α = β. Aggiunge che per un problema così banale ci sono tutta una serie di metodi meccanici: rientra da molto tempo nella deduzione automatica.

@@ dopo cap48.40
(lezione 2026) Nel 2026 i nomi sono scambiati: data una stringa α, il docente cerca una stringa β tale che f(β) = β^{R} = α. Dice che la scelta è banale, perché si è appena dimostrato che rovesciando due volte si torna al punto di partenza: basta scegliere β = α^{R}. In altre parole, come controimmagine basta prendere sempre la stringa ribaltata.

@@ dopo cap48.41
(lezione 2026) Nella lezione 24 il docente lo chiede alla classe: quanto vale f⁻¹(α)? Dopo qualche risposta sbagliata, risponde lui: f⁻¹(α) = α^{R}, cioè l'inversa è la funzione stessa. Di solito f⁻¹ applicata dopo f dà l'identità, cioè fa tornare al valore di partenza; qui a far tornare al valore di partenza è f stessa. Dire che f è l'inversa di se stessa è solo un altro modo di dire che, applicandola due volte, si torna al punto di partenza. È un caso particolare, sottolinea: di solito non è così.

@@ dopo cap48.43
**La concatenazione nella lezione 2026.** (lezione 2026) Il docente chiama g questa funzione, g(α, β) = αβ, e parte da un esempio: g(«atto», «re») = «attore». È iniettiva? No, e lo mostra con due coppie diverse che danno lo stesso risultato: g(«to», «re») = «tore» = g(«t», «ore»). Ci sono tanti modi di scomporre una stringa come concatenazione di due stringhe: una stringa di lunghezza 30 si ottiene in 31 modi diversi, dalla coppia (stringa vuota, tutti i 30 caratteri) fino alla coppia (tutti i 30 caratteri, stringa vuota). In generale una stringa di lunghezza n si ottiene in n + 1 modi, quindi, appena n non è zero, in più di un modo. Anche la suriettività è per il docente una domanda banale: per ottenere γ basta prendere (λ, γ) oppure (γ, λ). Sono domande, conclude, che servono solo a vedere se si è capita bene la definizione.
**Una stringa può essere iniettiva?** (lezione 2026) A una domanda di uno studente il docente risponde distinguendo due livelli. Una stringa è a sua volta una funzione, dagli indici alle lettere, quindi ha senso chiedersi se è iniettiva: lo è quando nessuna lettera compare due volte, cioè quando è quella che nel linguaggio comune si chiama una parola senza ripetizioni. «attore» non lo è, perché la t è sia l'elemento di indice 2 sia quello di indice 3; «re» lo è; «roma» lo è, «ramarro» no (ripete la r e la a). Ma nell'esercizio la domanda riguarda l'operazione di concatenazione, non il suo risultato: è come non confondere l'addizione 2 + 2 con 4, perché l'addizione è un'operazione che prende numeri e dà numeri, e il 4 è solo il suo risultato. Anche concatenando due stringhe senza lettere in comune, con un risultato iniettivo, l'operazione resta non iniettiva.
Che ci siano funzioni che si applicano a funzioni, aggiunge, non è un divertimento dell'insegnante per tormentare l'allievo: una stringa è una funzione, perché se le si chiede il carattere di un certo posto lo restituisce, ma è anche un dato per funzioni più complesse. Rovesciamento e concatenazione sono solo due delle innumerevoli operazioni sulle stringhe, che sono tutto sommato le operazioni più comuni dell'informatica: prendono un testo e lo trasformano in un altro testo, oppure ne estraggono informazioni, numeri, messaggi.

@@ dopo cap48.59
(lezione 2026) Anche nel 2026, nella seconda ora della lezione 24, il docente passa alle proprietà delle relazioni: riflessività, simmetria, antisimmetria e transitività sono nel cap. 50, ordini ed equivalenze nel cap. 51, e l'esercizio sui quantificatori con un grafo di frecce che chiude la lezione nel cap. 52.
