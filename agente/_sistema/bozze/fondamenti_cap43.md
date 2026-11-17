# 43. La Potenza Veloce e il suo Invariante
## Un invariante per un ciclo difficile
La seconda parte della lezione 21 è un esercizio sugli invarianti: la **potenza veloce**, annunciata alla fine del cap. 40. Il docente la svolge prima in modo informale e poi come quiz da completare. Negli esempi dei cap. 39 e 40 il ciclo era così semplice che la sua correttezza si vedeva a occhio, e l'invariante serviva solo a imparare il metodo. Qui succede il contrario: il codice è di poche righe, ma leggendolo non si capisce perché calcoli proprio una potenza, e l'invariante diventa lo strumento che lo spiega. Il docente avverte che è il momento più impegnativo di questa parte del corso e che lo si fa una volta sola, per mostrare che l'induzione ha applicazioni difficili e importanti; all'esame i problemi sono più facili (registrazione 2025).

Il codice e la prova di questo capitolo sono ricostruiti dalla registrazione 2025, dove la lezione ha lo stesso argomento: il testo del quiz non è disponibile, quindi i dettagli di scrittura (per esempio la forma esatta del test del `while`) possono differire da quelli visti in aula.

## Perché serve: esponenti enormi
Il ciclo del cap. 40 calcola aⁿ con n moltiplicazioni. Per gli esponenti piccoli va benissimo, ma la crittografia a chiave pubblica, che si usa senza accorgersene ogni volta che un telefono si collega a un servizio con dati sensibili, deve calcolare continuamente potenze in cui base ed esponente sono numeri di 2048 cifre binarie. Un numero così può arrivare a 2²⁰⁴⁸ − 1, che in base dieci ha 617 cifre e supera un 3 seguito da 616 zeri (registrazione 2025, anche per il conto delle cifre). Ripetere il prodotto tante volte quante dice l'esponente non è lento: è impossibile, perché un numero simile di operazioni non sta nell'universo. Nelle applicazioni reali a ogni passo si prende anche il resto modulo un terzo numero, per non far crescere i risultati; qui si lascia da parte e si studia solo la potenza.

## L'idea: quadrati successivi e cifre binarie
Il cap. 41 ha mostrato che con fattori tutti diversi le parentesi non fanno risparmiare niente. Con fattori tutti uguali invece un risultato già calcolato si può **riutilizzare**. Per b⁴ non servono tre prodotti: si calcola b² = b · b e poi b⁴ = b² · b², cioè due prodotti. Con un terzo si ottiene b⁸ = b⁴ · b⁴, con un quarto b¹⁶, e in generale b elevato a 2ᵏ si ottiene con k prodotti, ognuno il quadrato del precedente. Un esponente come 2²⁰⁴⁷ richiede così 2047 prodotti, un lavoro alla portata delle macchine già sessant'anni fa (registrazione 2025).

Se l'esponente non è una potenza di 2 lo si scompone in potenze di 2, cioè lo si scrive in binario (cap. 7). Per esempio 10 = 8 + 2, in binario 1010, quindi b¹⁰ = b⁸ · b². Si produce il «flusso» dei quadrati successivi b, b², b⁴, b⁸, … e si moltiplicano tra loro solo quelli che corrispondono a una cifra 1 dell'esponente, leggendo le cifre da destra a sinistra: per 1010 si salta b (cifra 0), si prende b² (cifra 1), si salta b⁴ (cifra 0), si prende b⁸ (cifra 1).

**Un richiamo: resto e quoziente intero.** Per un intero i ≥ 0, il **resto** `i % 2` vale 0 se i è pari e 1 se i è dispari; il **quoziente intero** `i / 2` è la metà di i arrotondata per difetto. Se i = 2 · i₀ allora `i % 2` vale 0 e `i / 2` vale i₀; se i = 2 · i₀ + 1 allora `i % 2` vale 1 e `i / 2` vale ancora i₀. Sul numero scritto in binario, `i % 2` legge l'ultima cifra e `i / 2` la cancella: con i = 5, in binario 101, il resto è 1 e il quoziente è 2, in binario 10; con i = 4, in binario 100, il resto è 0 e il quoziente è ancora 2.

Con queste due operazioni si esplorano le cifre binarie dell'esponente una alla volta, dall'ultima alla prima, senza doverlo convertire prima in binario.

## Il codice
Si vuole calcolare bⁿ, dove b è un numero reale qualunque e n un intero con n ≥ 0. Attenzione ai nomi: qui la base si chiama b, mentre `a` è una variabile di lavoro (nel cap. 40 a era la base).

```
ris = 1
i = n
a = b
while (i > 0) {
   if (i % 2 == 1) {
      ris = ris * a
   }
   a = a * a
   i = i / 2
}
```

Le variabili hanno tre compiti diversi (registrazione 2025):

- `ris` è un **accumulatore**: contiene i prodotti già fatti. Parte da 1, l'elemento neutro del prodotto, perché all'inizio non ne è stato fatto nessuno;
- `a` contiene i **quadrati successivi** di b: b, b², b⁴, b⁸, … All'inizio vale b, cioè a = b^{2^{0}}: attenzione, non b^{0};
- `i` è una copia di n che viene dimezzata a ogni giro: è un contatore particolare, che non scende di uno alla volta ma perde ogni volta l'ultima cifra binaria.

A ogni giro il corpo guarda l'ultima cifra di i; se è 1 moltiplica `ris` per il quadrato corrente; poi, in ogni caso, passa al quadrato successivo e cancella la cifra appena letta. L'`if` riguarda solo la prima assegnazione: le altre due vengono eseguite sempre.

**Esempio: b = 3 e n = 10.** In binario 10 è 1010. I valori delle variabili prima del ciclo e dopo ogni esecuzione del corpo sono:

- prima del ciclo: i = 10, a = 3, ris = 1;
- dopo 1 esecuzione (10 è pari, nessun prodotto in `ris`): i = 5, a = 9, ris = 1;
- dopo 2 esecuzioni (5 è dispari, ris = 1 · 9): i = 2, a = 81, ris = 9;
- dopo 3 esecuzioni (2 è pari): i = 1, a = 6561, ris = 9;
- dopo 4 esecuzioni (1 è dispari, ris = 9 · 6561): i = 0, a = 43 046 721, ris = 59 049.

Il ciclo si ferma con ris = 59 049 = 3¹⁰. In `ris` sono finiti proprio 3² = 9 e 3⁸ = 6561, come previsto dalla scomposizione 10 = 2 + 8.

## L'invariante
Per i cicli dei cap. 39 e 40 l'invariante diceva che cosa conteneva l'accumulatore. Qui non basta, perché in `ris` c'è solo una parte del risultato. L'idea del docente è che la potenza da calcolare, nel corso del calcolo, si divide in una **parte già calcolata**, che sta in `ris`, e in una **parte ancora da calcolare**, che è aⁱ (registrazione 2025).

**L'invariante** è: **ris · aⁱ = bⁿ e i ≥ 0**.

(In parole povere: quello che è già stato messo in `ris`, moltiplicato per quello che resta da fare, dà sempre il risultato finale. Nell'esempio, dopo due giri, 9 · 81² = 9 · 6561 = 59 049.)

La parte ris · aⁱ = bⁿ è quella della registrazione 2025. La parte i ≥ 0 è aggiunta qui per lo stesso motivo per cui il docente aggiunge i ≤ n negli invarianti dei cap. 39 e 40: con il test scritto come i > 0, è quella che all'uscita permette di concludere i = 0.

All'inizio tutta la potenza è «da calcolare» (ris = 1 e aⁱ = bⁿ); alla fine è tutta «calcolata» (i = 0, quindi aⁱ = 1). In mezzo i prodotti si spostano un po' alla volta da una parte all'altra.

## La prova dell'invariante
Si procede, come sempre, per induzione sul numero di esecuzioni del corpo del `while`.

**Caso base.** Non si è mai eseguito il corpo: i valori sono ris = 1, i = n, a = b. Sostituendoli nell'invariante si ottiene 1 · bⁿ = bⁿ, che è vero, e i = n ≥ 0, che è l'ipotesi sui valori in ingresso. Su b non c'è nessuna ipotesi.

**Caso induttivo.** Si suppone che l'invariante valga per i valori correnti di `ris`, `a` e `i`, e che il corpo venga eseguito un'altra volta: allora il test è vero, cioè i > 0. Il corpo si comporta in due modi diversi a seconda dell'ultima cifra di i, quindi si ragiona **per casi** (cap. 36): i pari oppure i dispari.

1. **Caso i pari.** Si scrive i = 2 · i₀. L'`if` non scatta, quindi `ris` non cambia; poi `a` diventa a · a = a² e `i` diventa i₀. Con i nuovi valori, la quantità dell'invariante è ris · (a²)^{i₀} = ris · a^{2 · i₀} = ris · aⁱ, per la proprietà della potenza di una potenza. Per ipotesi induttiva ris · aⁱ = bⁿ, quindi l'uguaglianza vale anche dopo il giro.
2. **Caso i dispari.** Si scrive i = 2 · i₀ + 1. L'`if` scatta e `ris` diventa ris · a; poi, come prima, `a` diventa a² e `i` diventa i₀, perché la divisione intera butta via il resto 1. Con i nuovi valori si ottiene (ris · a) · (a²)^{i₀} = ris · a · a^{2 · i₀} = ris · a^{2 · i₀ + 1} = ris · aⁱ, perché nel prodotto di potenze con la stessa base gli esponenti si sommano. Di nuovo, per ipotesi induttiva, questo vale bⁿ.

In tutti e due i casi il nuovo valore di i è i₀ ≥ 0, quindi anche la seconda parte si mantiene.

Il docente commenta così il caso dispari: la divisione intera «butta via» un 1 dall'esponente, ma quell'1 non va perso, perché il codice lo ha appena accumulato in `ris` con un prodotto in più. Le modifiche fatte da una parte si compensano dall'altra: l'invariante resta vero e intanto ci si avvicina all'obiettivo (registrazione 2025). Il ragionamento del caso pari, osserva, non funzionerebbe per i dispari. Raccomanda anche, come nel cap. 39, di non scrivere il secondo caso con un «copia e incolla» del primo.

## Dalla prova alla correttezza
**Proposizione.** Per ogni numero reale b e ogni intero n ≥ 0, il ciclo della potenza veloce termina, e quando termina `ris` contiene bⁿ.

(In parole povere: il codice, per quanto misterioso, fa davvero quello che deve. Con b = 2 e n = 13 restituisce 8192 = 2¹³ dopo soli quattro giri.)

**Dimostrazione.** Quando il ciclo termina il test i > 0 è falso, quindi i ≤ 0; con la parte i ≥ 0 dell'invariante si ottiene i = 0. L'altra parte dell'invariante diventa allora ris · a⁰ = bⁿ, cioè ris · 1 = bⁿ, cioè ris = bⁿ. Fin qui è la conclusione della registrazione 2025. La terminazione è aggiunta qui, come la parte i ≥ 0 dell'invariante: a ogni giro i > 0 viene sostituito da `i / 2`, che è un intero non negativo strettamente più piccolo di i, e una successione di interi non negativi non può scendere all'infinito.

Lo schema è quello dei cap. 39 e 40: l'invariante più la negazione del test danno il risultato. Con b = 0 la prova usa la convenzione 0⁰ = 1, come nel cap. 40.

**Correttezza parziale e totale.** Gli appunti del docente definiscono la correttezza parziale e totale così, sull'esempio della divisione intera; qui le stesse parole si applicano alla potenza veloce. La richiesta sui dati in ingresso (qui n ≥ 0) è la **condizione di ingresso**; ciò che deve valere alla fine (qui ris = bⁿ) è la **condizione di uscita**, quella che nel cap. 39 è chiamata postcondizione.

**Definizione.** Un programma è **parzialmente corretto** se, per ogni dato che soddisfa la condizione di ingresso, **se** il programma termina allora i dati in uscita soddisfano la condizione di uscita. È **totalmente corretto** se, per ogni dato che soddisfa la condizione di ingresso, il programma termina **e** i dati in uscita soddisfano la condizione di uscita.

(In parole povere: la correttezza parziale dice «se arriva in fondo, la risposta è giusta», ma non promette che arrivi in fondo. La correttezza totale promette tutte e due le cose. Un ciclo che gira per sempre è parzialmente corretto per qualunque condizione di uscita, ma non serve a niente.)

L'invariante dà la correttezza parziale; la terminazione è un ragionamento a parte, che di solito consiste nel trovare una quantità intera non negativa che diminuisce a ogni giro. Per la potenza veloce questa quantità è proprio i.

## Quanti giri fa il ciclo
A ogni giro i perde una cifra binaria, quindi il corpo viene eseguito tante volte quante sono le cifre binarie di n. Partendo da 1000 i valori di i sono 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0: dieci giri. Per un milione i giri sono 20, per un miliardo 30, contro il miliardo di giri del ciclo del cap. 40 (registrazione 2025). Per un esponente di 2048 cifre binarie sono 2048 giri.

Una precisazione aggiunta, sul conto dei prodotti: a ogni giro il ciclo eleva `a` al quadrato, e in più moltiplica `ris` una volta per ogni cifra 1 di n. Per n = 10 sono 4 quadrati e 2 prodotti in `ris`, cioè 6 moltiplicazioni in tutto, contro le 10 del ciclo del cap. 40, che ne fa una per giro. Nel cap. 40 i conti a mano davano 9 per il prodotto semplice e 4 per quello veloce: a mano non si fa il primo prodotto per 1 (quello che mette il primo fattore in `ris`), e nel conto veloce non si calcola l'ultimo quadrato, che il ciclo fa ma non usa.

**E se n è negativo?** L'ipotesi n ≥ 0 non è una vera limitazione, osserva il docente: se n < 0 si calcola b elevato a −n, che ha esponente positivo, e poi si prende il reciproco (registrazione 2025). Il reciproco esiste solo se b ≠ 0. Per esempio 2^{−3} = 1/2³ = 1/8.

## L'invariante vale solo a giro completo
L'invariante deve essere vero prima del ciclo e dopo ogni esecuzione **completa** del corpo, non dopo ogni singola istruzione. In mezzo al corpo può benissimo essere falso, e non è un problema: il docente lo dice esplicitamente nella lezione successiva della registrazione 2025. Qui si vede bene. Nell'esempio con b = 3 e n = 10, durante il primo giro, dopo `a = a * a` e prima di `i = i / 2`, le variabili valgono ris = 1, a = 9, i = 10, e 1 · 9¹⁰ = 3 486 784 401 non è 3¹⁰ = 59 049. L'uguaglianza torna vera solo quando anche i è stato dimezzato.

## Dal problema al codice controllato
Il docente chiude riassumendo tutto il percorso (registrazione 2025). Si parte da casi particolari (b², b⁴, b⁸) e si arriva a un algoritmo; poi lo si scrive, e il codice somiglia così poco all'idea di partenza che viene il dubbio che calcoli altro; allora lo si prova su casi semplici, poi su milioni di casi in automatico; ma l'unico controllo che dà una garanzia completa è il ragionamento, cioè l'invariante con la sua prova per induzione. Come nel cap. 39, la parte difficile è **trovare** l'invariante: una volta scritto ris · aⁱ = bⁿ, la prova è quasi meccanica.

Dopo la potenza veloce per la lezione 22 sono in programma due cicli semplici: la somma degli elementi di un vettore e la ricerca di uno zero.
