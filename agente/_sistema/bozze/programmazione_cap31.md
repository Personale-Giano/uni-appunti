# Capitolo 31: Chiamata e Ritorno Passo per Passo, Record di Attivazione
## Le due fasi della chiamata
Una chiamata di funzione **non corrisponde a una singola istruzione elementare**, ma a una sequenza di operazioni coordinate: salvataggio dell'indirizzo di ritorno, aggiornamento di SP e FP, salto al nuovo indirizzo. Il corso la divide in due momenti.

**Definizione.** Il **prologo** è la preparazione dello stack frame e l'avvio della funzione chiamata; l'**epilogo** è la preparazione al ritorno e il ripristino dello stato del chiamante.

(In parole povere: il prologo è «apparecchiare la tavola» prima di iniziare, l'epilogo è «sparecchiare» e rimettere tutto com'era per chi aspettava.)

## La sequenza di chiamata
Seguiamo la chiamata dal punto di vista di chi chiama (il **chiamante**) e di chi viene chiamato (il **chiamato**):
1. il chiamante posiziona i **parametri** e lo spazio per il **valore di ritorno** sullo stack (o in registri);
2. salva il **successore del program counter**, cioè l'indirizzo dell'istruzione da cui riprendere, indicato con next(PC), e sposta PC all'inizio della funzione chiamata;
3. inizia il **prologo** della funzione: copia FP sullo stack, così il valore del chiamante non va perso;
4. imposta **FP = SP**: da qui inizia il nuovo stack frame;
5. riserva le variabili locali della funzione chiamata, spostando SP.

Da questo momento la funzione accede ai dati della chiamata tramite offset da FP: parametri e valore di ritorno a offset positivi, variabili locali a offset negativi.

![La disposizione del modello: sopra FP stanno i dati preparati dal chiamante e i dati di controllo, sotto FP le variabili locali del chiamato.](figure/prog/record_attivazione.png|13)

## Il ruolo del Frame Pointer
FP viene posto alla base dello stack frame della funzione attiva. Grazie a questo, parametri e variabili locali sono sempre accessibili tramite offset da FP, senza bisogno di conoscere l'indirizzo assoluto nello stack; anche se SP cambia durante l'esecuzione, gli offset rispetto a FP restano stabili; e una funzione può quindi essere eseguita **in qualunque posizione dello stack**.

**Definizione.** Una funzione è **rientrante** (~reentrant~) quando può essere eseguita in qualunque posizione dello stack, anche più volte contemporaneamente: ogni chiamata ha un frame distinto, quindi più attivazioni della stessa funzione non si disturbano.

(In parole povere: è come un modulo da compilare di cui ognuno ha la sua copia: dieci persone lo possono riempire insieme senza pasticciarsi a vicenda. È il requisito essenziale per la ricorsione.)

## La sequenza di ritorno
Il ritorno è il percorso inverso:
1. il **valore di ritorno** viene scritto;
2. inizia l'**epilogo**: si rilasciano tutte le variabili locali della funzione ponendo **SP = FP**;
3. si **ripristina FP** dallo stack, recuperando il valore salvato nel prologo;
4. si **ripristina il program counter**: l'esecuzione riprende nel chiamante subito dopo il punto in cui la chiamata era stata eseguita;
5. si **rimuovono i parametri**.

A questo punto lo stato è completamente ripristinato e il chiamante ha accesso al valore di ritorno. (Questo è l'ordine delle animazioni passo per passo delle slide; l'elenco riassuntivo a fianco nomina le stesse voci in un altro ordine.)

(In parole povere: ogni cosa salvata all'andata viene ripresa al ritorno, in ordine inverso, perché lo stack restituisce per primo l'ultimo dato messo.)

Le CPU reali introducono differenze nei dettagli (per esempio in x86 il valore di ritorno è tipicamente posto in un registro), ma la logica di base resta la stessa in tutte le architetture di tipo Von Neumann esteso.

## Record di attivazione e stack frame
Ciò che accade in una chiamata si può descrivere a due livelli di astrazione: un livello **logico**, indipendente dall'hardware, che considera cosa serve per gestire una chiamata; e un livello **implementativo**, che descrive come queste informazioni sono memorizzate nello stack.

**Definizione.** Il **record di attivazione** (~activation record~) è l'insieme logico dei dati necessari per l'esecuzione di una singola chiamata di funzione: i parametri, le variabili locali, l'eventuale valore di ritorno, i dati di controllo (indirizzo di ritorno e frame pointer precedente) e altri registri o informazioni di stato salvate.

(In parole povere: è tutto quello che serve a quella chiamata per lavorare e poi tornare indietro, il suo «contesto di esecuzione completo», a prescindere da dove sia messo in memoria.)

Lo **stack frame** è invece il livello implementativo (capitolo 30). Nel modello del corso comprende la **parte inferiore** del record di attivazione, delimitata da FP e SP e gestita dal codice della funzione attiva: le **variabili locali** (FP + offset negativi) appartengono allo stack frame, mentre **parametri, dati di controllo e valore di ritorno** (FP + offset positivi) stanno in un'area contigua ma **esterna** allo stack frame, gestita dal chiamante. Il libro di Paul Deitel non fa questa distinzione e usa solo «stack frame».

## Perché serve saperlo
Capire la meccanica della chiamata è fondamentale per padroneggiare le funzioni, e il docente segnala un **esercizio tipico d'esame**: rappresentare lo stato dello stack e dei registri **prima del ritorno di una funzione**. Per prepararlo conviene saper disegnare, dall'alto verso il basso:
- le variabili locali del chiamante, con i valori aggiornati fino a quel punto;
- lo spazio per il valore di ritorno e i parametri, con le copie degli argomenti;
- i dati di controllo, cioè next(PC) e il FP del chiamante;
- FP, le variabili locali del chiamato e infine SP.
