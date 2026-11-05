# Frasi del docente da tenere d'occhio: fondamenti_L31_2025

Estratte automaticamente dalla trascrizione (possibili errori di riconoscimento). Il timestamp serve per riascoltare il punto.

## esame (9)
- **[12:26]** Questo circuito da solo può sommare quante cifre vogliamo, semplicemente basta fargli ripetere il suo compito e per quanto riguarda il resto che prima gestivamo spostando da un circuito all'altro perché ci mancava la possibilità di ricordare il
  - contesto: è un nuovo riporto. resto del calcolo precedente.
- **[20:33]** Ed ecco che un solo circuito ha svolto il compito di 32 nello stesso tempo perché comunque i 32 circuiti non potevano lavorare in parallelo, ciascuno doveva aspettare il risultato del precedente.
  - contesto: da sé stesso ma nell'istante precedente un uno, riceve da sé stesso ma nell'istante precedente fa la somma modulo 2 non c'è sorpresa, risultato è 1, resto 0. E quindi notate come in realtà non è che abbiamo
- **[21:11]** scoperto come svolgere compiti nuovi aggiungendo questa memoria temporanea, però abbiamo scoperto come migliorare il modo con cui veniva svolto un compito precedente, dove prima venivano stampati 32 o 64 circuiti, ne stampiamo solo più una.
  - contesto: E quindi notate come in realtà non è che abbiamo Abbiamo tutte le caratteristiche di prima, per usare l'ultimo resto come messaggio di overflow bisogna fare qualche lavoro in più, Ma comunque, diciamo, nel caso che non ci sia overflow, cioè che non ci sia un r
- **[21:49]** questi circuiti svolgono lo stesso compito dei 32 precedenti ma occupano spazio 1.
  - contesto: Abbiamo tutte le caratteristiche di prima, per usare l'ultimo resto come messaggio di overflow bisogna fare qualche lavoro in più, Ma comunque, diciamo, nel caso che non ci sia overflow, cioè che non ci sia un resto che va perduto, Questo significa che consuma
- **[32:51]** Magari per curiosità potremmo vederlo purché resti chiaro che non fa parte dell'epogama di esami.
  - contesto: questo libro non lo dice e quindi non mi sono neanche occupato io di cercarlo e di sapere come si fa. Allora, ritorniamo a noi e diciamo come rappresentiamo una macchina con memoria.
- **[47:32]** Beh, se sono in sigma 0, A e B verranno trasformati in 0 o 1, perché non idea se questa macchina in realtà sia una macchina vera che svolge un compito, poi se diciamo che avremmo cambiato
  - contesto: E intanto cosa dico all'esterno? i nomi e la bianorresa è riconoscibile, oppure se sia semplicemente una scelta casuale ed è quasi impossibile dirlo perché se io nel nocario, nel circuito che fa l'addizione, vi tolgo i nomi, vi metto dei nomi a caso, voi non m
- **[01:24:53]** l'ultima volta attraverso la S, il circuito mi dice la S è stata l'ultimo gate che ha ricevuto un numero, al compito di ricordarsi che cosa ha avvenuto nel passato, ma non tutto il passato, solo l'ultima volta che un 1 è arrivato a uno dei due gate e mi dice quale dei due.
  - contesto: Se io gli fornisco un uno attraverso la S e uno zero attraverso la R, il circuito mi dice che l'uno è stato fornito Non è in in grado di fornire una risposta se arrivano due uno simultaneamente alle due gate.
- **[01:36:43]** Quando suogliamo qualunque compito e ci viene detto memoria insufficente cosa facciamo se quel compito è importante e spostiamo i dati su un altro computer con più capacità e rinanciamo, magari salviamo anche lo stato del calcolo, questo lo può fare un ricercatore, e riprendiamo oppure più banalmente affittiamo, se siamo facendo i calcoli su internet,
  - contesto: Invece i veri computer hanno una memoria potenzialmente infinita, non ce ne rendiamo conto, abbiamo l'impressione di avere una memoria limitata ma non è così. fermiamo il calcolo, teniamo buono lo stato, affittiamo più spazio di memoria e lo riprendiamo al cal
- **[01:38:27]** adatta a svolgere un certo compito, non può semplicemente fermarsi, salvare lo stato, aspettare un incremento di memoria e poi riprendere il calcolo, perché proprio il suo algoritmo è immaginato per un insieme di stati rigido e non modificabile.
  - contesto: Questa è una macchina, è stata finita e non può farlo, una macchina è stata finita e ha una memoria rigida e quindi quando questa memoria non è Ovviamente noi possiamo definire un'altra macchina per questo scopo che richiede una memoria più ampia ma non sarà p

## attenzione (8)
- **[33:55]** L'output in questo caso sarà, attenzione, non gli output locali, cioè non i dati che stanno temporaneamente in memoria e che aiutano a fare i calcoli.
  - contesto: Finché vogliamo solo capire l'algoritmo che fa il circuito, non ne abbiamo ancora bisogno e poi ci saranno gli output. Questi sono dati locali, però output si rende qualcosa che va fuori il circuito, non qualcosa che il circuito tiene lì e usa per fare i calco
- **[38:59]** Qui non possiamo ancora leggere attenzione questo diagramma, impareremo a farlo in queste lezioni e quindi ci vuole uno Stato e nel caso unissime di Stati saranno solo due, nel caso di un addizionatore saranno il No Carrier e il Carrier.
  - contesto: circuito e non del dettaglio con cui è rappresentata quell'idea. Dunque allora eravamo qua quindi questo stiamo soltanto commentando la definizione,
- **[40:09]** E poi naturalmente questa macchina deve produrre un flusso in uscita, nel caso del ledder sarà il flusso delle cifre del risultato dell'addizione, quindi non solo si prende un flusso in ingresso, di input in ingresso, quindi attenzione i non non è tutto l'input, è solo l'input fornito all'istante t, nell'istante t più uno viene
  - contesto: ma adesso ti interessa solo che sono un insieme. fornito un altro input, poi t più 2 etc.
- **[45:19]** Ecco immaginiamo questa macchina, attenzione, non è l'addizione, è una macchina generica, più semplice dell'addizione, non ha il vincolo di fare qualcosa, semplicemente serve per descrivere l'idea di input output stati, nuovo stato, nuovo output stati iniziali.
  - contesto: del genere. Questi sei elementi descrivono una macchina e forniscono una tabella fatta così.
- **[45:54]** Poi come input riceve abi, attenzione cosa vuol dire un flusso di lettere abi, quindi il libro come esempio dice, immaginate che la macchina riceva ab, ab, ab, ab che cosa restituisceà e che cosa restituisce Cake uno adesso non so se la macchina sia proprio quella di quella
  - contesto: di solito lo stato iniziale viene chiamato sigma0. tabella o sia un'altra comunque dice immaginiamo che la macchina che vi ho appena descritto riceva questo flusso di input cosa restituisceьюi che costitui che questo perché perché le regole per il prossimo sta
- **[01:09:59]** Allora questo vuol dire che la prima A diventa 0, la seconda diventa 0 poi B diventa 1 attenzione però fino qua io ero nel, quindi in oro la fase
  - contesto: Le A diventano 0 e le B diventano 1. nello stato iniziale sigma0, puoi cercare sigma ovviamente bisogna dedicarci un tempo considerabile, eccolo qua.
- **[01:25:37]** Attenzione però è anche possibile che io cambi il contenuto di una memoria, cioè ho dei comandi di sovra scrittura.
  - contesto: Se io continuo a fornire 1 a s continua a dirmi, s è stato l'ultimo circuito che ha ricevuto un 1. Posso dire a s questa volta mando 0, r mando 1.
- **[01:44:01]** Qui x primo è la negazione, attenzione, x più x primo uguale a 1 e x per x primo uguale a 0 sono vere nelle algebre di bull, tutte vene richiesto, non basta che siano vere per vero o falso.
  - contesto: fatto che abbiate ben capito cos'è una tavola di verità, cos'è una proprietà distributiva, cos'è l'idenpotenza e così via. Sì, se in realtà sono addirittura di solito prese come assiome, questo viene chiamato terzo escluso e si legge x oppure non x uguale

## errore tipico (6)
- **[01:21:59]** Semplicemente ha tre comandi possibili, poi c'è un quarto che non è previsto e che produrrebbe un errore, i tre comandi previsti sono doppio ricevere doppio zero, zero uno o uno zero.
  - contesto: finiti. In altre parole viene prevista la possibilità che arrivi il primo zero fa riferimento alla S,
- **[01:24:53]** In questo caso produce un errore.
  - contesto: Non è in in grado di fornire una risposta se arrivano due uno simultaneamente alle due gate. Quindi allora se io gli chiedo che cosa è ricevuto, qual è gate ricevuto
- **[01:30:17]** Se cerchiamo di scrivere nelle memorie vere due valori contraddittori, per esempio abbiamo una macchina parallela e tutti e due cercano di scrivere lo stesso valore, viene fuori un qualche errore.
  - contesto: contemporaneamente le due richieste, 11 e 10 zero, il flip flop non è affidabile. Un Bonhard era ferma uno delle due macchine parallele e lascia scrivere l'altra, ma comunque qualche errore dovrà venire fuori se noi tentiamo di mandare due valori contraddittor
- **[01:30:17]** Un Bonhard era ferma uno delle due macchine parallele e lascia scrivere l'altra, ma comunque qualche errore dovrà venire fuori se noi tentiamo di mandare due valori contraddittori nella stessa
  - contesto: Se cerchiamo di scrivere nelle memorie vere due valori contraddittori, per esempio abbiamo una macchina parallela e tutti e due cercano di scrivere lo stesso valore, viene fuori un qualche errore. memoria.
- **[01:34:02]** altri forniscono un valore ma è sbagliato.
  - contesto: Alcuni impazziscono e oscillano tre due valori, Non è certamente quello che abbiamo richiesto perché abbiamo fatto una richiesta contraddittoria che non si può esaudire, quindi il fatto che venga una risposta in realtà è persino peggio, che non è un messaggio 
- **[01:34:02]** Non è certamente quello che abbiamo richiesto perché abbiamo fatto una richiesta contraddittoria che non si può esaudire, quindi il fatto che venga una risposta in realtà è persino peggio, che non è un messaggio di errore, perché viene una risposta sbagliata senza che ci sia consapevolezza che ha avvenuto un errore.
  - contesto: altri forniscono un valore ma è sbagliato. Qui

## da ricordare (8)
- **[10:42]** Vi ricordate delle efficienza delle manchine.
  - contesto: Già solo una memoria che mantenga per un'unità di tempo un bit consente miglioramenti nottevoli. Vi ricordate e avevamo accennato al fatto che i circuiti
- **[10:42]** Vi ricordate e avevamo accennato al fatto che i circuiti
  - contesto: Vi ricordate delle efficienza delle manchine. combinatori, quelli privi di memoria che possono solo trasformare dei bit ma non possono ricordarli anche per un istante, consentivano comunque di eseguire l'addizione.
- **[21:49]** che rappresento un fattore importante di logorio.
  - contesto: e anche a questione che evidentemente il calore poi si disperte bisogna aumentare il lavoro di raffreddamento, ma soprattutto questo calore compromette la vita dei circuiti nel... Ed ecco che quindi abbiamo visto come le macchine fornite di...
- **[30:29]** Come possibile ottenerla appunto si introduce una nozione di automi che sostanzialmente ignora il problema pur importante di come realizzare le memorie e si limita ad escrivere come le memorie vengono usate e questo si chiama macchina stati finiti e
  - contesto: non siamo ancora in grado di leggerla, ma certamente questa è una descrizione completa di come si realizza un circuito per l'addizione. nei casi particolari poi che interesseranno più a noi si chiamerà autumni.
- **[37:16]** 64 cifre binarie e non se le ricorda, però si ricorda se c'era un riporto oppure no, ma per ricordarsi qualcosa, uno non deve scrivere come si ricorda, per caritare questo ovviamente è un aspetto essenziale se non sapessimo come poi il circuito, non lo costruire ma se vogliamo solo sapere cosa fa il l'addizionatore, cioè che algoritmo usa, allora ci basta ricordarci che
  - contesto: Questi due stati è tutto ciò che deve sapere del passato, quindi l'addizionatore si diceva un flusso 8, 16, 32, l'architettura è cambiata nel tempo, l'addizionatore può essere in due stati.
- **[01:08:05]** scusate, quindi devo mettere in carica il portamento e non è importante, dovrebbe bastare la carica.
  - contesto: qui però siamo ancora prima, stiamo semplicemente vedendo una macchina stati finiti come primo esempio ed è scritta da queste due matrici, una per il prossimo stato e l'altra per il... Cosa dicevo?
- **[01:35:30]** Ne manca una molto importante, quale non si nota subito ma è una lacuna nottevole, non viene messa di proposito
  - contesto: No, chiaramente ne manca una. perché sarebbe molto difficile da descrivere, ci sono descrizioni ovviamente ma non sono semplici come sono più complesse diciamo di quella che abbiamo vista adesso, qual è la lacuna principale qui di questa definizione.
- **[01:36:43]** Quando suogliamo qualunque compito e ci viene detto memoria insufficente cosa facciamo se quel compito è importante e spostiamo i dati su un altro computer con più capacità e rinanciamo, magari salviamo anche lo stato del calcolo, questo lo può fare un ricercatore, e riprendiamo oppure più banalmente affittiamo, se siamo facendo i calcoli su internet,
  - contesto: Invece i veri computer hanno una memoria potenzialmente infinita, non ce ne rendiamo conto, abbiamo l'impressione di avere una memoria limitata ma non è così. fermiamo il calcolo, teniamo buono lo stato, affittiamo più spazio di memoria e lo riprendiamo al cal

## esercizio (4)
- **[01:34:53]** bisogna fare esercizi in cui uno si prende una descrizione così e prova a disegnarla.
  - contesto: Qui Io non ho un buon software per disegnare, quindi non so come farli fare.
- **[01:35:30]** Magari adesso ci limitiamo a fare esercizi per non perdere tempo.
  - contesto: delle macchine stati finiti, li vediamo nella prossima lezione. Ecco, solo una domanda.
- **[01:41:51]** sui sommi il prodotto come sono nelle algebre di bull, dove rappresentano disgiunzione e congiunzione, in questo caso la commutatività c'è, è molto strano, provate a fare la tavola la di verità, non ricordo se poi se noi avevamo provato a fare questa tavola di verità e certamente è una proprietà di cui è difficile convincersi, però è vera.
  - contesto: Questa propietà qui è valida, tensione, leggetela bene, sì è vera, quella paradossale che non c'è, quindi se questa è la somma e questo è il prodotto e questa sarebbe una proprietà falsa, non è vero che la somma distribuisce sul prodotto, però noi qui parliamo
- **[01:48:09]** questo esercizio, in realtà è di esposito, non è mio.
  - contesto: Sì, credo che ci sia una semplificazione drastica, se ricordo Faccia parte del vecchio corso di architetture.
