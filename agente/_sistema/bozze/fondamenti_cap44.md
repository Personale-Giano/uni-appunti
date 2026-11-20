# 44. Invarianti su un Vettore: la Somma degli Elementi e la Ricerca di uno Zero
## Due cicli che si sanno già scrivere
La lezione 22 è dedicata a due esercizi sugli invarianti, più semplici della potenza veloce del cap. 43. Il docente lo spiega così: dimostrare con un invariante la correttezza di un ciclo difficile vorrebbe dire anticipare il corso di algoritmi; a Fondamenti interessa solo capire il metodo. Il prezzo è che i cicli sono pezzi di codice che si sa già essere corretti: non sono interessanti in sé, servono come esempi (registrazione 2025).

La lezione 22 di quest'anno non è registrata: su Moodle il docente la sostituisce con quella del 2025, che ha lo stesso argomento. Gli esercizi sono svolti in aula come quiz Moodle; codice e formule qui sono ricostruiti dalla spiegazione orale e possono differire in qualche dettaglio.

In tutti e due gli esercizi v è un vettore di n elementi con indici da 0 a n − 1, come in C e in Java. L'unica ipotesi sui valori in ingresso è **n ≥ 1**: se il vettore non avesse elementi, la sua dichiarazione verrebbe rifiutata e il codice non partirebbe nemmeno.

## La somma degli elementi di un vettore
Il ciclo deve mettere nella variabile sum la somma di tutti gli elementi di v, ciascuno preso esattamente una volta.

```
sum = v[0]
i = 1
while (i < n) {
   sum = sum + v[i]
   i = i + 1
}
```

sum è un accumulatore. i conta quanti elementi sono già stati sommati: all'inizio uno, v[0]; quando i arriva a n sono stati sommati tutti. i serve solo durante il calcolo e alla fine non interessa più.

i ha due significati diversi. Finché vale tra 1 e n − 1 è un indice del vettore. Quando vale n non è un indice, ma un segnale che il lavoro è finito: usarlo per leggere v[n] vorrebbe dire leggere un elemento che non esiste. A seconda del linguaggio, il programma va avanti con un valore sbagliato senza accorgersene (il caso peggiore) oppure si ferma con un errore di indice fuori intervallo (registrazione 2025).

## Quale invariante scegliere
L'invariante deve descrivere che cosa c'è in sum dopo un numero qualunque di esecuzioni del corpo: zero, alcune o tutte. Si prova con un caso. Con n = 10, all'inizio i = 1 e sum = v[0]. Dopo un'esecuzione del corpo i = 2 e sum = v[0] + v[1]. Se i vale 7, sono stati sommati 7 elementi, quelli di indice da 0 a 6, e restano da sommare quelli da 7 a 9. In sum ci sono quindi gli elementi di indice da 0 a i − 1, non da 0 a i. L'invariante è:

**sum = v[0] + v[1] + … + v[i − 1] e 1 ≤ i ≤ n.**

La seconda parte dice in quale intervallo si muove i: parte da 1 e arriva al massimo a n. Il docente avverte che senza questa parte alcuni passi della prova non si riescono a fare.

Le verifiche da fare sono tre, come nei cap. 39 e 40:
- l'invariante è vero prima della prima esecuzione del corpo (caso base);
- se è vero prima di un'esecuzione del corpo, è vero anche dopo (caso induttivo);
- quando il ciclo finisce, l'invariante insieme al test falso dice che il ciclo ha fatto il suo compito.

## La prova per la somma
**Caso base.** Dopo le due assegnazioni iniziali sum = v[0] e i = 1. Sostituendo i = 1 nell'invariante, la somma va da v[0] a v[1 − 1] = v[0], quindi diventa sum = v[0], che è vero per come si è assegnato sum. La seconda parte diventa 1 ≤ 1 ≤ n: 1 ≤ 1 è vero, e 1 ≤ n è l'ipotesi sui valori in ingresso.

**Caso induttivo.** Si suppone vero l'invariante e si esegue il corpo un'altra volta; per un while questo succede solo se il test è vero, quindi i < n. Allora v[i] è un elemento che esiste, perché i è tra 1 e n − 1, e la prima assegnazione si può fare. Qui i indica il valore all'inizio del giro; alla fine del giro varrà i + 1. Dopo la prima assegnazione:

sum = v[0] + … + v[i − 1] + v[i].

Il docente riscrive l'ultimo addendo come v[(i + 1) − 1]. Non cambia niente, perché (i + 1) − 1 e i sono lo stesso numero, ma così la formula somiglia di più a quella che si vuole ottenere. Dopo la seconda assegnazione i diventa i + 1. Per l'intervallo: da 1 ≤ i segue 1 < i + 1, quindi anche 1 ≤ i + 1; da i < n, poiché tra due interi diversi la distanza è almeno 1, segue i + 1 ≤ n. Quindi vale:

sum = v[0] + … + v[(i + 1) − 1] e 1 ≤ i + 1 ≤ n,

che è l'invariante con i + 1 al posto di i, cioè l'invariante scritto con i nuovi valori delle variabili. Durante l'esecuzione del corpo, tra la prima e la seconda istruzione, l'invariante non vale: non è un problema, perché si controlla solo a giro completo (cap. 43).

**Uscita dal ciclo.** Quando il ciclo finisce, il test i < n è falso, quindi i ≥ n. L'invariante dice anche i ≤ n: l'unica possibilità rimasta è i = n. Sostituendo i = n nell'invariante si ottiene sum = v[0] + … + v[n − 1], cioè la somma di tutti gli elementi, e 1 ≤ n ≤ n, una parte che non serve più e si può lasciare cadere. La prima parte è esattamente ciò che si voleva.

## Due passaggi che sembrano strani
Nella prova ci sono due passaggi che a un essere umano sembrano curiosi, ma che sono corretti. Il docente li chiama «paradossi della logica»: la logica prende spunto dal linguaggio comune, ma non coincide con esso (registrazione 2025).

**Indebolire un'affermazione.** Da 1 < i + 1 si è passati a 1 ≤ i + 1. Si perde informazione, perché prima si sapeva che i + 1 è strettamente maggiore di 1 e dopo non più, ma la verità si conserva: dire «minore o uguale» non esclude il «minore». Una macchina che controlla la prova vede solo che, se la prima formula è vera, anche la seconda lo è. Si butta via un'informazione quando in quel momento non serve.

**Sostituire uguali con uguali.** Se un'affermazione è vera e al posto di un'espressione se ne scrive un'altra con lo stesso valore, l'affermazione resta vera. Così v[i] è diventato v[(i + 1) − 1], come un'affermazione su n · n resta vera scrivendo n² al posto di n · n. Il motivo per cui conviene farlo si vede solo dopo: è un tentativo di avvicinarsi alla formula da dimostrare. Secondo il docente anche molti programmi che cercano dimostrazioni fanno così: provano piccole modifiche e tengono quelle che fanno somigliare la formula a un pezzo dell'obiettivo (registrazione 2025).

Il docente insiste che in queste prove molte scelte, come l'invariante o la riscrittura di v[i], vengono dall'intuito e non si sanno spiegare fino in fondo. Per questo sono difficili da affidare a una macchina, che deve provare tanti tentativi. In un programma ci sono migliaia di cicli, quasi tutti varianti di cicli noti. Le prove su esempi, anche milioni di esempi casuali, sono il controllo più usato, ma per i cicli cruciali la certezza si ottiene solo con un ragionamento.

## La ricerca del primo zero
Il secondo ciclo controlla se nel vettore v c'è uno zero. Se c'è, risponde sì e dà l'indice del primo zero; se non c'è, risponde no, e in quel caso il valore dell'indice non conta.

```
i = 0
found = false
while (i < n && found == false) {
   if (v[i] == 0) {
      found = true
   } else {
      i = i + 1
   }
}
```

i conta gli elementi già controllati: all'inizio nessuno. found dice se uno zero è già stato trovato: all'inizio no. Il ciclo va avanti finché i non è arrivato a n e finché non si è trovato uno zero. A ogni giro guarda il primo elemento non ancora controllato, v[i]: se è zero cambia found e lascia i com'è, così i resta l'indice dello zero; altrimenti cambia i e lascia found com'è.

Il test contiene found == false, cioè il contrario di ciò che interessa, perché trovare uno zero deve far finire il ciclo: si va avanti finché found è falso.

## L'invariante e la correttezza
Insieme all'invariante serve scrivere che cosa vuol dire che il ciclo è corretto, cioè la condizione di uscita (la postcondizione del cap. 39), e non è così immediato. Le risposte possibili sono due:
- se alla fine found è false, nessun elemento del vettore è zero: v[0], v[1], …, v[n − 1] sono tutti diversi da 0. Il valore di i non fa parte della risposta e qui non conta;
- se alla fine found è true, i è un indice vero del vettore, cioè 0 ≤ i < n, v[i] = 0, e v[0], …, v[i − 1] sono tutti diversi da 0, così lo zero trovato è il primo.

La condizione di uscita è la congiunzione delle due implicazioni «se found è false allora …» e «se found è true allora …».

L'invariante ha tre parti:
- **0 ≤ i ≤ n**;
- **v[0], …, v[i − 1] sono tutti diversi da 0**: gli elementi già controllati non sono zeri, perché altrimenti il ciclo si sarebbe già fermato;
- **se found è true, allora i < n e v[i] = 0.**

La terza parte è la più difficile da trovare. Esprime il fatto che found diventa true solo in un punto del codice, il primo ramo dell'if, quando si è appena scoperto che v[i] è zero, e che da lì in poi i non cambia più. Il docente ammette che è un'idea che lo ha guidato, non un criterio che saprebbe applicare in modo meccanico.

## La prova per la ricerca
**Caso base.** Dopo le assegnazioni iniziali i = 0 e found = false.
- 0 ≤ 0 ≤ n è vero, perché n ≥ 1.
- La seconda parte dice che gli elementi di indice da 0 a −1 non sono zeri. Ma non esistono indici tra 0 e −1: è un'affermazione universale sull'insieme vuoto, e per le regole dei quantificatori è vera (cap. 30). Per smentirla bisognerebbe trovare un elemento dell'insieme vuoto che non ha la proprietà, e non ce ne sono. Nel linguaggio comune un'affermazione del genere non ha molto senso, ma in logica le affermazioni universali sull'insieme vuoto sono tutte vere e quelle esistenziali tutte false.
- La terza parte è un'implicazione con la premessa found = true falsa, perché found vale false: un'implicazione con la premessa falsa è vera, qualunque sia la conclusione (cap. 16).

Due delle tre parti sono vere per motivi che il docente chiama paradossali, ma che seguono dalle definizioni: queste definizioni sono state scelte perché rendono le prove più semplici.

**Caso induttivo.** Si suppone vero l'invariante e si esegue il corpo. Il test è una congiunzione, quindi se il corpo viene eseguito sono vere entrambe le sue parti: i < n e found = false. Il corpo è un solo if, e si ragiona per casi (cap. 36).

In entrambi i casi v[i] esiste, perché 0 ≤ i < n.

1. Caso v[i] = 0. Si esegue found = true, e i non cambia. Le prime due parti dell'invariante non contengono found e i non è cambiato: erano vere e restano vere. La terza è un'implicazione: ora la premessa found = true è vera, quindi deve essere vera la conclusione. Lo è: i < n valeva per il test del while e i non è cambiato, e v[i] = 0 è appena stato controllato dall'if. Il docente osserva che in pratica questo caso è raro: se si cerca uno zero, magari bisogna guardare centomila elementi prima di trovarlo.
2. Caso v[i] ≠ 0. Si esegue i = i + 1, e found non cambia. Prima parte: da 0 ≤ i < n segue 0 ≤ i + 1 ≤ n. Seconda parte: v[0], …, v[i − 1] erano diversi da 0 e ora si sa che anche v[i] lo è, quindi sono diversi da 0 tutti gli elementi da v[0] a v[i], cioè fino al nuovo valore di i meno 1. Terza parte: found era false per il test del while e non è cambiato, quindi la premessa dell'implicazione è falsa e l'implicazione è vera.

**Uscita dal ciclo.** Quando il ciclo finisce, il test i < n && found == false è falso. Per le leggi di De Morgan (cap. 15) la negazione di una congiunzione è la disgiunzione delle negazioni: vale i ≥ n oppure found = true. In generale potrebbero valere entrambe, come nota il docente; qui l'invariante lo esclude, perché con found = true dà i < n. Sono i due modi in cui il ciclo può finire: l'indice è arrivato in fondo, oppure si è trovato uno zero prima. Restano da dimostrare le due implicazioni della condizione di uscita.

- Se found è false, allora found = true è falsa, quindi deve valere i ≥ n. Con la prima parte dell'invariante, i ≤ n, si ottiene i = n. Sostituendo i = n nella seconda parte: v[0], …, v[n − 1] sono tutti diversi da 0, cioè nel vettore non ci sono zeri.
- Se found è true, la terza parte dell'invariante dà i < n e v[i] = 0. La prima parte dà 0 ≤ i, quindi i è un indice vero del vettore. La seconda parte dice che v[0], …, v[i − 1] non sono zeri, quindi v[i] è il primo zero.

Nella registrazione l'ultimo passaggio, i < n nel caso found = true, è quello su cui ci si ferma di più. L'intuizione è chiara: si è usciti perché found è diventato true, e in quel giro i non è stato incrementato. Per una prova che si possa controllare in modo meccanico, però, l'argomento deve venire dalle formule, e qui viene dalla terza parte dell'invariante. Il docente chiude con questa osservazione: anche quando non si hanno veri dubbi su un ciclo, comunicarlo a una macchina passo per passo non è così facile.

**Una precisazione aggiunta sulla terminazione.** L'invariante dà la correttezza parziale (cap. 43). Il ciclo termina, al massimo dopo n giri: a ogni giro o i cresce di 1, e i non può superare n, oppure found diventa true, e allora il test successivo è falso. Lo stesso vale per il ciclo della somma, dove i cresce di 1 a ogni giro da 1 fino a n.

## Riepilogo
- Somma degli elementi: con sum = v[0] e i = 1, l'invariante è sum = v[0] + … + v[i − 1] e 1 ≤ i ≤ n; all'uscita i ≥ n e i ≤ n danno i = n, quindi sum contiene la somma di tutti gli elementi.
- Ricerca del primo zero: l'invariante ha tre parti, 0 ≤ i ≤ n, gli elementi da v[0] a v[i − 1] non sono zeri, e se found è true allora i < n e v[i] = 0.
- La condizione di uscita della ricerca è una congiunzione di due implicazioni: se found è false non ci sono zeri; se è true, i è l'indice del primo zero.
- Nella prova servono regole che sembrano strane ma seguono dalle definizioni: un universale sull'insieme vuoto è vero, un'implicazione con la premessa falsa è vera, indebolire un'affermazione ne conserva la verità, sostituire un'espressione con una uguale non cambia il valore di verità.
- All'uscita dal while vale la negazione del test: con un test composto da una congiunzione, per De Morgan si ottiene una disgiunzione, e si ragiona sui due casi.
- La parte difficile resta scegliere l'invariante, in particolare l'intervallo dell'indice e, nella ricerca, la terza parte sull'implicazione.
