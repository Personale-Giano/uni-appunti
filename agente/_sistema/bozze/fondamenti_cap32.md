# 32. Dimostrazioni sugli Insiemi e Sottodimostrazioni
## Come si dimostra che due insiemi sono uguali
Il modo più comune è la **doppia inclusione**: si mostra che ogni elemento del lato sinistro sta nel lato destro, e viceversa. Contare gli elementi non basta, ricorda il docente nella registrazione 2025: {1, 2, 3} e {4, 5, 6} hanno lo stesso numero di elementi senza essere uguali. Le operazioni, in una riga: x ∈ A ∩ B vuol dire x ∈ A e x ∈ B; x ∈ A ∪ B vuol dire x ∈ A oppure x ∈ B; x ∈ A − B vuol dire x ∈ A e x ∉ B.

**Definizione.** Si chiama **espansione delle definizioni** (in inglese ~unfolding~) il passo in cui un simbolo viene sostituito con ciò che significa, fino a ottenere una formula di sola logica.

(In parole povere: è come aprire un foglio piegato più volte. Una formula su insiemi, una volta spiegata del tutto, diventa una frase con «e», «oppure» e «non», cioè logica proposizionale. L'immagine e il termine sono del docente, nella registrazione 2025.)

## Primo esempio: X ∩ (Y − Z) = (X ∩ Y) − (X ∩ Z)
**Proposizione.** Per tutti gli insiemi X, Y, Z vale X ∩ (Y − Z) = (X ∩ Y) − (X ∩ Z).

(In parole povere: una specie di proprietà distributiva. Togliere Z e poi intersecare con X dà lo stesso risultato che intersecare prima entrambi con X e poi togliere.)

Con un disegno ci si convince in fretta, dice il docente nella registrazione 2025, ma la prova logica è un oggetto diverso. Si espandono i due lati separatamente:

- x ∈ X ∩ (Y − Z) diventa: x ∈ X e x ∈ Y e x ∉ Z;
- x ∈ (X ∩ Y) − (X ∩ Z) diventa: x ∈ X e x ∈ Y e non è vero che (x ∈ X e x ∈ Z). Per De Morgan l'ultimo pezzo è: x ∉ X oppure x ∉ Z.

**Da sinistra a destra.** Si suppone x ∈ X, x ∈ Y, x ∉ Z. I primi due pezzi della tesi sono già tra le ipotesi. Resta la disgiunzione «x ∉ X oppure x ∉ Z»: per dimostrarla basta un lato, e il lato buono è x ∉ Z, che è un'ipotesi. L'altro lato, x ∉ X, sarebbe impossibile da ottenere. Il docente chiarisce il punto rispondendo a una proposta in aula: da un'affermazione non si può provare il suo contrario, altrimenti la logica sarebbe incoerente.

**Da destra a sinistra.** Si suppone x ∈ X, x ∈ Y e (x ∉ X oppure x ∉ Z). Serve x ∉ Z. Il lato x ∉ X della disgiunzione è escluso, perché contraddice l'ipotesi x ∈ X; resta solo l'altro. È il **sillogismo disgiuntivo** del cap. 19: da p ∨ q e ¬p si ricava q.

Le due inclusioni insieme danno l'uguaglianza.

Secondo il docente, a questo livello di dettaglio una persona non segue più il senso del ragionamento: è come ingrandire uno schermo fino a vedere i singoli quadratini e non più la lettera. Alla fine si è certi che i due lati sono uguali senza aver capito perché. Il suo riassunto: comprendere e controllare sono compiti diversi. Il disegno serve a capire, la prova serve a controllare, e solo la prova si può dare a una macchina.

## Sottodimostrazioni
Mentre si costruisce una prova può capitare di aver bisogno di un risultato intermedio. Allora ci si ferma, lo si dimostra a parte e si torna alla prova principale.

**Definizione.** Una **sottodimostrazione** è la dimostrazione di un risultato ausiliario, svolta all'interno di una dimostrazione più grande.

(In parole povere: è una funzione ausiliaria di un programma. La si scrive una volta a parte, e il programma principale si limita a chiamarla.)

## Il minimo di due numeri
**Definizione.** Se a e b sono reali, min{a, b} vale a se a < b, vale a se a = b, vale b se b < a.

(In parole povere: è il più piccolo dei due, oppure il valore comune se sono uguali. Bisogna spiegarlo per casi perché, dice il docente, noi crediamo di sapere cos'è il minimo, ma alla macchina va detto tutto. Esempio: min{2, 4} = 2.)

**Proposizione.** Per tutti i reali d, d₁, d₂, x: se d = min{d₁, d₂} e x ≤ d, allora x ≤ d₁ e x ≤ d₂.

(In parole povere: chi sta sotto il più piccolo sta sotto tutti e due.)

**L'idea a parole (registrazione 2025).** Con d₁ = 2 e d₂ = 5 il minimo è 2: se x ≤ 2 allora x sta anche sotto 5. Con −7 e 11 è lo stesso. Il minimo è uno dei due valori e l'altro è maggiore o uguale, quindi chi sta sotto il minimo sta sotto entrambi. È così che una persona si convince, ma un esempio aiuta a capire e non dimostra un enunciato universale.

**La struttura.** L'ipotesi è x ≤ d, la tesi è x ≤ d₁ e x ≤ d₂: manca il pezzo che collega d a d₁ e a d₂. Quel pezzo è la sottodimostrazione.

**Sottodimostrazione: d ≤ d₁ e d ≤ d₂.** Si guarda la definizione di minimo.

- Se d₁ ≤ d₂, allora d = d₁. Quindi d ≤ d₁, perché un numero è minore o uguale a sé stesso, e d = d₁ ≤ d₂.
- Se d₂ < d₁, allora d = d₂. Quindi d ≤ d₂ e d = d₂ < d₁, da cui d ≤ d₁.

Nella registrazione 2025 il docente svolge i tre casi della definizione uno per uno, ma il ragionamento è lo stesso. Osserva che i casi si chiudono da soli: una volta espansa la definizione, resta solo che ogni valore è minore o uguale a sé stesso (la proprietà riflessiva) e che il minore è uno dei casi del minore o uguale.

**Dimostrazione principale.** Siano d, d₁, d₂, x arbitrari, con d = min{d₁, d₂} e x ≤ d.

1. Da x ≤ d e d ≤ d₁, per la transitività (cap. 31), si ha x ≤ d₁.
2. Da x ≤ d e d ≤ d₂, per la transitività, si ha x ≤ d₂.
3. Unendo i due risultati con la regola di congiunzione si ottiene la tesi.

Per una macchina, nota il docente, il difficile è capire che bisogna passare da un valore intermedio; il resto è noioso ma non presenta difficoltà. Qui il valore intermedio era suggerito dal problema stesso.

## Due dimostrazioni dello stesso enunciato
**Proposizione.** Per tutti gli insiemi X, Y vale X ∪ (Y − X) = X ∪ Y.

(In parole povere: togliere X da Y e poi riaggiungere X non cambia nulla, perché ciò che si perde si recupera subito. Sul disegno a due cerchi: X dà la mezzaluna sinistra e la parte centrale, Y − X la mezzaluna destra, e insieme fanno tutta l'unione. Il disegno è quello della registrazione 2025.)

**Prima dimostrazione: doppia inclusione.**

- **Se x ∈ X ∪ (Y − X)**, allora x ∈ X oppure x ∈ Y − X. Nel primo caso x ∈ X ∪ Y subito. Nel secondo x ∈ Y, quindi di nuovo x ∈ X ∪ Y.
- **Se x ∈ X ∪ Y**, allora x ∈ X oppure x ∈ Y. Se x ∈ X, allora x ∈ X ∪ (Y − X) subito. Altrimenti x ∉ X, quindi x ∈ Y; dunque x ∈ Y − X, e di nuovo x sta nell'unione.

Nella prima inclusione i casi vengono dalla definizione di unione, e basta il fatto che un'unione contiene entrambi i suoi argomenti: il docente suggerisce che una macchina può tenere proprietà banali come X ⊆ X ∪ Y in un archivio da consultare.

Nella seconda inclusione entra una distinzione che non viene dalla definizione: **x ∈ X oppure x ∉ X**. È il **terzo escluso** (cap. 15): una proprietà o è vera o è falsa, e una terza possibilità non c'è. Nella registrazione 2025 uno studente chiede perché non considerare il caso «x non sta in X», e il docente risponde che ragionare per terzo escluso è un altro metodo di prova, usato in altre dimostrazioni.

**Seconda dimostrazione: leggi degli insiemi.** Si parte dal lato sinistro e si manipola come in algebra. Il libro usa qui le leggi degli insiemi della sezione 1.1: bastano la distributiva, il complemento e l'identità, con U insieme universo e X̄ = U − X:

X ∪ (Y − X) = X ∪ (Y ∩ X̄), perché Y − X = Y ∩ X̄;

X ∪ (Y ∩ X̄) = (X ∪ Y) ∩ (X ∪ X̄), per la legge distributiva;

(X ∪ Y) ∩ (X ∪ X̄) = (X ∪ Y) ∩ U, per la legge del complemento;

(X ∪ Y) ∩ U = X ∪ Y, per la legge dell'identità.

Non si parla più di elementi: le leggi diventano regole di calcolo. I due metodi hanno lo stesso valore: un enunciato si può dimostrare in molti modi.

Il capitolo seguente affronta il caso opposto: che cosa fare quando l'enunciato è falso.
