# 49. Dimostrare Espandendo le Definizioni: il Doppio Rovesciamento di una Stringa
## Una proprietà ovvia, vista da una macchina
(lezione 2026) La lezione 24 del 23 novembre 2026 riprende le stringhe del cap. 48 da un punto di vista nuovo. Che una parola letta due volte allo specchio torni quella di partenza lo sappiamo per esperienza: per esempio (assi^{R})^{R} = (issa)^{R} = assi. Il docente pone però la domanda in un altro modo: **come può dedurlo una macchina?** Una macchina non ha la nostra esperienza; vede soltanto delle formule che definiscono una trasformazione sulle stringhe, e deve ricavare la proprietà da quelle formule. Il metodo che usa il docente si chiama **espansione delle definizioni** seguita da un calcolo algebrico, e secondo lui è il modo più comune per controllare proprietà semplici come questa.

## Le stringhe come funzioni e la rovesciata
Per poter fare i conti bisogna scrivere le stringhe come funzioni, nello stesso spirito delle sequenze del cap. 47. (lezione 2026) Negli appunti che il docente proietta in aula una stringa è una funzione α: [1, n] → X per qualche intero n ≥ 0, che è la sua lunghezza; [1, n] indica l'insieme degli indici {1, 2, …, n}. Per n = 0 l'insieme degli indici è vuoto e la stringa è λ (precisazione nostra). Il carattere di posto i è α(i).

**Definizione.** Sia α: [1, n] → X una stringa di lunghezza n. La sua **rovesciata** α^{R} è la stringa della stessa lunghezza n definita da α^{R}(i) = α(n + 1 − i) per ogni i ∈ [1, n].

(In parole povere: il carattere che la rovesciata mette al primo posto è l'ultimo di α, quello al secondo posto è il penultimo, e così via. La formula n + 1 − i è il «contatore all'indietro»: quando i va da 1 a n, n + 1 − i va da n a 1.)

**Esempio.** Per α = assi si ha n = 4, quindi α^{R}(i) = α(5 − i). Allora α^{R}(1) = α(4) = i, α^{R}(2) = α(3) = s, α^{R}(3) = α(2) = s, α^{R}(4) = α(1) = a, e α^{R} = issa. La definizione ha senso perché, se 1 ≤ i ≤ n, anche 1 ≤ n + 1 − i ≤ n: l'indice calcolato cade sempre dentro la stringa (osservazione nostra).

## La dimostrazione: espandere le definizioni
**Proposizione.** Per ogni stringa α vale (α^{R})^{R} = α.

(In parole povere: leggere una parola allo specchio e poi rileggere allo specchio il risultato restituisce la parola di partenza.)

Prima di tutto bisogna dire che cosa vuol dire la tesi. Due stringhe sono uguali quando hanno la stessa lunghezza e lo stesso carattere in ogni posizione, cioè quando sono la stessa funzione. La rovesciata ha la stessa lunghezza n della stringa di partenza, quindi anche (α^{R})^{R} ha lunghezza n. (lezione 2026) Il docente riscrive allora la tesi così: per ogni i ∈ [1, n], (α^{R})^{R}(i) = α(i). Fissato un indice i qualunque, i passi sono tre.
- **Primo passo: si espande la rovesciata esterna.** (α^{R})^{R} è la rovesciata della stringa α^{R}, che ha lunghezza n. Applicando la definizione a questa stringa si ottiene (α^{R})^{R}(i) = α^{R}(n + 1 − i).
- **Secondo passo: si espande la rovesciata interna, con un'istanza.** La definizione dice che α^{R}(k) = α(n + 1 − k) per **ogni** k ∈ [1, n]. Qui serve con k = n + 1 − i, che è un indice lecito perché sta in [1, n], come osservato nell'esempio sopra: si scrive l'espressione n + 1 − i al posto di k e si ottiene α^{R}(n + 1 − i) = α(n + 1 − (n + 1 − i)).
- **Terzo passo: si semplifica con l'algebra.** n + 1 − (n + 1 − i) = n + 1 − n − 1 + i = i: il primo n + 1 è sommato e il secondo è sottratto, quindi si cancellano, e il «meno meno i» diventa «più i». Quindi (α^{R})^{R}(i) = α(i), che è la tesi.

Sul suo schermo il docente scrive il passaggio intermedio come (α(n + 1 − i))^{R}, una scrittura abbreviata (lettura nostra) per dire «applica la definizione di rovesciata nell'indice n + 1 − i»; la forma precisa è quella del primo passo, α^{R}(n + 1 − i).

## L'istanza e le parentesi
(lezione 2026) Nel secondo passo il docente cambia apposta il nome della variabile: scrive la definizione di α^{R} con k invece che con i, perché vale per qualunque intero k di [1, n], non necessariamente per l'indice i di cui si sta parlando. Poi si sostituisce a k il valore richiesto dal calcolo. Questa operazione si chiama **istanza**: quando una proprietà vale per tutti i k e interessa sapere che cosa succede per un k particolare, magari dato da un'espressione, si prende quella proprietà e si scrive l'espressione al posto di k. Il docente sottolinea che, anche se la prima volta richiede un po' di attenzione, è un metodo del tutto meccanico.

**Trabocchetto d'Esame.** L'espressione va sostituita **tutta intera, tra parentesi**. In aula il docente fa la sostituzione con un copia e incolla e dimentica le parentesi, scrivendo α(n + 1 − n + 1 − i); è uno studente a correggerlo. Senza parentesi il conto cambia: n + 1 − n + 1 − i = 2 − i, che non è i. Come ricorda il docente, senza le parentesi l'espressione non ha il significato corretto.

## Perché farlo, se è ovvio
(lezione 2026) Per noi questa dimostrazione risponde a un bisogno che non sentiamo, perché l'esperienza ci anticipa già il risultato. Per la macchina invece il fatto che la formula, applicata due volte, riporti alla stringa di partenza non fa parte di nessuna esperienza. Il docente osserva che un'intelligenza artificiale che esplora il web troverebbe probabilmente una pagina di qualche corso di programmazione che lo spiega; ma questo darebbe soltanto una **risposta plausibile**. Se si vuole dalla macchina una **risposta certa**, bisogna farle fare proprio questi calcoli. Dimostrazioni di questo tipo, aggiunge più avanti nella lezione, rientrano da molto tempo nella deduzione automatica: sono problemi banali, risolti con metodi meccanici.

Il metodo si riassume in pochi passi, che valgono per molte proprietà semplici:
- scrivere esplicitamente la tesi (per le stringhe: stessa lunghezza e stesso carattere in ogni posizione);
- espandere le definizioni, dalla più esterna alla più interna;
- quando una definizione va applicata a un'espressione, farne un'istanza, sostituendo l'espressione tra parentesi;
- semplificare con l'algebra fino ad arrivare alla tesi.

## Prima applicazione: il rovesciamento è una biiezione
(lezione 2026) Subito dopo il docente rifà l'esercizio del cap. 48 sulla biiettività di f(α) = α^{R}: con la proposizione appena dimostrata diventa facile (suriettività con β = α^{R}, iniettività rovesciando di nuovo α^{R} = β^{R}, e f⁻¹ = f). I dettagli della lezione 2026 sono nel cap. 48.

## Esercizio: la rovesciata di una concatenazione
**Esercizio (nostro).** Dimostrare con lo stesso metodo che (αβ)^{R} = β^{R}α^{R}. Per esempio con α = ro e β = ma: (roma)^{R} = amor, e β^{R}α^{R} = am · or = amor.

**Soluzione (nostra; l'uguaglianza è stata controllata al computer su tutte le stringhe su {a, b} fino alla lunghezza 4).** Siano |α| = n e |β| = m. Serve prima la concatenazione scritta come funzione: αβ ha lunghezza n + m e (αβ)(i) = α(i) se 1 ≤ i ≤ n, mentre (αβ)(i) = β(i − n) se n < i ≤ n + m. È la regola che il docente descrive a parole: il primo carattere della seconda stringa va al posto n + 1, l'ultimo al posto n + m. Le due stringhe da confrontare hanno entrambe lunghezza n + m; si fissa i ∈ [1, n + m] e si espande (αβ)^{R}(i) = (αβ)(n + m + 1 − i). Ci sono due casi.
- Se 1 ≤ i ≤ m, allora n + m + 1 − i > n, e si cade nella parte di β: (αβ)(n + m + 1 − i) = β(m + 1 − i) = β^{R}(i). A destra, poiché i ≤ m = |β^{R}|, anche (β^{R}α^{R})(i) = β^{R}(i).
- Se m < i ≤ n + m, allora n + m + 1 − i ≤ n, e si cade nella parte di α: (αβ)(n + m + 1 − i) = α(n + 1 − (i − m)) = α^{R}(i − m). A destra, poiché i > m, (β^{R}α^{R})(i) = α^{R}(i − m).
In tutti e due i casi i caratteri coincidono, quindi (αβ)^{R} = β^{R}α^{R}. Il ragionamento per casi è quello del cap. 36.

## Riepilogo
- Una stringa di lunghezza n è una funzione α: [1, n] → X; la rovesciata è α^{R}(i) = α(n + 1 − i), con la stessa lunghezza.
- Per dimostrare (α^{R})^{R} = α si scrive la tesi carattere per carattere, si espandono le due rovesciate e si semplifica: n + 1 − (n + 1 − i) = i.
- Un'istanza sostituisce un'espressione al posto di una variabile quantificata universalmente; l'espressione va messa tra parentesi.
- Il metodo (espansione delle definizioni più algebra) è meccanico: è quello che serve a una macchina per avere una risposta certa e non solo plausibile.
- Con (α^{R})^{R} = α la biiettività del rovesciamento è immediata, e il rovesciamento è l'inversa di se stesso.

Nella seconda ora della lezione il docente passa alle proprietà delle relazioni, l'argomento del prossimo capitolo.
