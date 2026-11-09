# 36. Contrapposizione, Dimostrazione per Casi ed Equivalenze
## Gli ultimi metodi della sezione 2.2
Il cap. 35 ha introdotto la dimostrazione per assurdo. Questa lezione chiude la sezione 2.2 del libro con altri quattro esempi, e ognuno porta con sé un metodo: la **contrapposizione**, la **dimostrazione per casi**, nella forma particolare della **dimostrazione esaustiva**, e la **dimostrazione di equivalenza**. Come nei capitoli precedenti, i risultati sono volutamente semplici: nella registrazione 2025 il docente ripete quasi a ogni esempio che la proprietà non interessa, interessa la tecnica.

## La dimostrazione per contrapposizione
**Definizione.** Una **dimostrazione per contrapposizione** di p → q consiste nel dimostrare la contrapposta ¬q → ¬p: si suppone che la tesi sia falsa e si deduce che è falsa l'ipotesi.

(In parole povere: invece di camminare dall'ipotesi alla tesi, si cammina all'indietro, dalla tesi falsa all'ipotesi falsa. Funziona perché p → q e ¬q → ¬p hanno la stessa tavola di verità (cap. 17): «se piove, la strada è bagnata» e «se la strada è asciutta, non piove» dicono la stessa cosa.)

Attenzione a non confonderla con la conversa q → p, che scambia le due parti senza negarle e non è equivalente all'implicazione di partenza (cap. 17). La contrapposta fa due cose insieme: scambia **e** nega.

## Contrapposizione o assurdo?
Per assurdo (cap. 35) si suppongono p e ¬q e si cerca una contraddizione **qualsiasi** r ∧ ¬r; per contrapposizione si suppone solo ¬q e il traguardo è fissato in partenza, ¬p: è una dimostrazione diretta (cap. 31) della contrapposta. Se un assurdo arriva proprio a ¬p, la contraddizione è p ∧ ¬p, e se p non è stata usata strada facendo, la prova è proprio una contrapposizione: per questo il libro la chiama caso speciale dell'assurdo. Il contrario non vale come forma di prova: un assurdo in cui p viene usato durante il ragionamento non è una dimostrazione diretta di ¬q → ¬p.

## Numeri razionali e irrazionali
**Definizione.** Un numero reale x è **razionale** se si può scrivere x = p/q con p e q interi e q ≠ 0; è **irrazionale** se non è razionale.

(In parole povere: razionale vuol dire «frazione». Sono razionali 0,75 = 3/4 e anche −5 = −5/1. Irrazionale vuol dire soltanto «non è una frazione»: √2 del cap. 35 è l'esempio tipico.)

Nella registrazione 2025 il docente osserva che «irrazionale» non è una definizione diretta: dice che cosa il numero non è, e non dà niente di concreto su cui lavorare.

## Esempio: se x² è irrazionale, anche x lo è
**Proposizione.** Per ogni reale x, se x² è irrazionale allora x è irrazionale.

(In parole povere: il quadrato di una frazione è ancora una frazione, quindi un quadrato che non è una frazione non può venire da una frazione. Non vale il contrario: √2 è irrazionale, ma il suo quadrato, 2, è razionale.)

**Perché non la via diretta.** L'ipotesi dice soltanto che x² non è una frazione, e la tesi che x non lo è. Come osserva il docente (registrazione 2025), le due informazioni sembrano scollegate: da «x² non è una frazione» non si ricava nessuna formula per x.

**La contrapposta.** Scritto in logica, l'enunciato ha due negazioni: ¬(x² razionale) → ¬(x razionale). La contrapposta scambia le due parti e le nega: ¬¬(x razionale) → ¬¬(x² razionale). Qui, negando entrambe le parti, le negazioni spariscono per la doppia negazione (cap. 18), e resta un enunciato tutto in positivo: se x è razionale, allora x² è razionale.

**Dimostrazione.** Si prende un reale x arbitrario e lo si suppone razionale.

1. Per definizione esistono due interi p e q, con q ≠ 0, tali che x = p/q.
2. Elevando al quadrato: x² = p²/q².
3. p² e q² sono interi, e q² ≠ 0 perché il prodotto di interi non nulli non è nullo. Quindi x² è un quoziente di interi con denominatore non nullo, cioè è razionale.

Per esempio, x = 3/4 dà x² = 9/16, e x = −5/2 dà x² = 25/4. Il docente la definisce una prova che sta in una riga; a lezione usa lettere diverse per le due frazioni, x = c/d e x² = a/b, con a = c² e b = d², perché le lettere dentro i due «esiste» sono variabili locali e non c'è motivo che coincidano (registrazione 2025).

Si vede anche la regola del cap. 31: l'∃ dell'ipotesi si usa (ci viene data la frazione c/d), quello della tesi si costruisce (la frazione a/b la troviamo noi).

**Correzione al libro.** Il libro scrive x = p/q «per qualche intero p e q» senza richiedere q ≠ 0. La condizione va aggiunta: con q = 0 la frazione non ha senso, e al passo 3 serve sapere che q² ≠ 0 per concludere che x² è razionale.

**La stessa prova per assurdo.** Il libro la lascia come esercizio: supponendo x² irrazionale e x razionale, gli stessi tre passi danno x² razionale, e si ha la contraddizione; ma poiché l'ipotesi «x² irrazionale» non viene usata strada facendo, la prova è proprio una contrapposizione.

## La dimostrazione per casi
**Definizione.** Una **dimostrazione per casi** si usa quando l'ipotesi si spezza in più casi, cioè p ≡ p₁ ∨ p₂ ∨ … ∨ pₙ. Invece di dimostrare (p₁ ∨ p₂ ∨ … ∨ pₙ) → q, si dimostrano una per una le implicazioni p₁ → q, p₂ → q, …, pₙ → q.

(In parole povere: per sapere che «in bici o a piedi arrivo in ritardo» basta mostrare che in bici arrivo in ritardo e che a piedi arrivo in ritardo. L'esempio del libro è l'ipotesi «x è un numero reale», che si divide nei casi x ≥ 0 e x < 0.)

**Proposizione.** Per tutte le proposizioni p₁, …, pₙ e q vale (p₁ ∨ p₂ ∨ … ∨ pₙ) → q ≡ (p₁ → q) ∧ (p₂ → q) ∧ … ∧ (pₙ → q).

(In parole povere: dire che uno qualsiasi dei casi porta alla tesi è lo stesso che dire che ciascun caso ci porta.)

Non serve una tavola con 2ⁿ⁺¹ righe: basta distinguere tre situazioni.

- **q vera.** Tutte le implicazioni, a sinistra e a destra, hanno la tesi vera, quindi sono vere entrambe le formule.
- **q falsa e tutti i pᵢ falsi.** Tutte le implicazioni hanno l'ipotesi falsa e sono vere per difetto (cap. 16): di nuovo entrambe vere.
- **q falsa e almeno un pⱼ vero.** A sinistra la disgiunzione è vera e la tesi falsa, quindi l'implicazione è falsa. A destra la congiunzione contiene pⱼ → q, che è falsa, quindi è falsa anche lei.

Nella registrazione 2025 il docente sottolinea che i casi vanno dimostrati **tutti**, perché non si sa in anticipo in quale si andrà a cadere; e che il numero di casi lo decide l'ipotesi: se una definizione avesse dieci casi, la prova ne avrebbe dieci.

**Definizione.** Una **dimostrazione esaustiva** è una dimostrazione per casi in cui i casi sono finiti e abbastanza pochi da poterli controllare tutti, uno per uno.

(In parole povere: è come aprire un lucchetto da tre cifre provando tutte le combinazioni. Sono mille, noioso ma fattibile; con un lucchetto da cento cifre non lo sarebbe più.)

## Esempio: 2m² + 3n² = 40 non ha soluzioni
**Proposizione.** Non esistono interi positivi m e n tali che 2m² + 3n² = 40.

(In parole povere: comunque si scelgano due interi positivi, il doppio del quadrato del primo più il triplo del quadrato del secondo non fa mai esattamente 40.)

**Il problema degli infiniti casi (registrazione 2025).** L'idea immediata è affidare il calcolo a una macchina, provando tutte le coppie m, n. Ma gli interi sono infiniti, e il programma non finirebbe mai: il fatto di non finire sarebbe proprio la prova che la soluzione non c'è, ma in nessun momento si saprebbe che non finirà. La domanda giusta, dice il docente, è un'altra: serve davvero controllarli tutti?

**La riduzione.** No, perché i due addendi sono positivi e nessuno dei due può superare il totale.

1. Da 2m² ≤ 40 segue m² ≤ 20. Poiché 5² = 25, deve essere m ≤ 4.
2. Da 3n² ≤ 40 segue n² ≤ 40/3 ≈ 13,3. Poiché 4² = 16, deve essere n ≤ 3.
3. Restano 4 · 3 = 12 coppie, che si controllano tutte.

Per n = 1 si ottengono 5, 11, 21, 35 (m = 1, 2, 3, 4); per n = 2, 14, 20, 30, 44; per n = 3, 29, 35, 45, 59.

Nessuno vale 40: nove sono più piccoli e tre più grandi (44, 45 e 59). Per m > 4 il solo addendo 2m² vale almeno 50, per n > 3 il solo 3n² vale almeno 48: la somma supera 40. La prova è finita.

**Ridurre l'infinito al finito (registrazione 2025).** Per il docente è il concetto interessante dell'esempio: spesso si riesce a dimostrare che, se un controesempio esiste, deve stare in un sottoinsieme finito, e allora il controllo si affida a una macchina. Così è stato dimostrato il **teorema dei quattro colori** (bastano quattro colori per colorare una carta geografica con le regioni confinanti di colori diversi), riducendolo a un insieme critico di carte nell'ordine delle migliaia, e la **congettura di Keplero** sulla disposizione più densa di sfere uguali, ridotta a un numero molto grande di casi. In entrambi nessun essere umano ha potuto seguire la prova per intero: non sono ragionamenti difficili, ma calcoli troppo numerosi per una persona.

## Esempio: x ≤ |x|
Il valore assoluto è definito per casi (cap. 31): |x| = x se x ≥ 0, e |x| = −x se x < 0. Per questo una prova che lo riguarda si divide spontaneamente negli stessi due casi.

**Proposizione.** Per ogni numero reale x vale x ≤ |x|.

(In parole povere: il valore assoluto di un numero non è mai più piccolo del numero stesso. Per i positivi e lo zero è uguale, per i negativi è più grande: |3| = 3, mentre |−2| = 2 è maggiore di −2.)

**Dimostrazione.** Ogni reale x soddisfa x ≥ 0 oppure x < 0.

- **Caso 1: x ≥ 0.** Per definizione |x| = x, quindi in particolare x ≤ |x|.
- **Caso 2: x < 0.** Per definizione |x| = −x, e −x > 0 perché x è negativo. Si ha quindi x < 0 < |x|, e per la transitività dell'ordine x < |x|, dunque anche x ≤ |x|.

In entrambi i casi vale la tesi. Nella registrazione 2025 il docente fa notare che nel primo caso vale l'uguaglianza e nel secondo la disuguaglianza stretta, ma la tesi chiede solo ≤. Aggiunge che una persona si convincerebbe con un paio di esempi, |3| e |−2|; una prova verificabile, invece, deve ragionare in astratto usando solo regole già verificate.

Il libro ne ricava una regola pratica: un enunciato con un «oppure» si presta spesso a una dimostrazione per casi. Qui l'«oppure» è nascosto nella definizione del valore assoluto.

## La dimostrazione di equivalenza
**Definizione.** Una **dimostrazione di equivalenza** di un enunciato «p se e solo se q» consiste nel dimostrare le due implicazioni p → q e q → p, usando l'equivalenza p ↔ q ≡ (p → q) ∧ (q → p) (cap. 18).

(In parole povere: «se e solo se» è un'implicazione a doppio senso, quindi si percorre la strada due volte, all'andata e al ritorno. Il docente le chiama implicazione da sinistra a destra e implicazione da destra a sinistra (registrazione 2025).)

## Esempio: n è dispari se e solo se n − 1 è pari
**Proposizione.** Per ogni intero n, n è dispari se e solo se n − 1 è pari.

(In parole povere: un numero è dispari esattamente quando quello che lo precede è pari. Per esempio 7 è dispari e 6 è pari; −3 è dispari e −4 è pari.)

Si usano le definizioni di pari e dispari del cap. 31, che contengono un ∃. Si prende n intero arbitrario.

- **Da sinistra a destra: n dispari ⟹ n − 1 pari.** Per ipotesi esiste un intero k con n = 2k + 1. Bisogna trovare un intero h con n − 1 = 2h. Sottraendo 1 si ottiene n − 1 = (2k + 1) − 1 = 2k, quindi basta prendere h = k.
- **Da destra a sinistra: n − 1 pari ⟹ n dispari.** Per ipotesi esiste un intero h con n − 1 = 2h. Aggiungendo 1 a entrambi i membri, n = 2h + 1, quindi n è dispari.

Il libro usa la stessa lettera k in tutte e due le direzioni; il docente usa una lettera diversa nella seconda, per non confondersi. Agli studenti che propongono di controllare prima qualche caso ricorda che un numero finito di esempi convince, ma non dà certezza (registrazione 2025).

**Una catena di «se e solo se».** Il libro mostra che la stessa prova si può scrivere in un colpo solo:

n dispari ⟺ n = 2k + 1 per qualche intero k ⟺ n − 1 = 2k per qualche intero k ⟺ n − 1 pari.

Letta da sinistra a destra dà la prima implicazione, letta da destra a sinistra dà la seconda. La forma è compatta, ma corretta solo se **ogni anello** vale in entrambi i versi.

**Attenzione.** In una catena di ⟺ basta un anello che vale in un verso solo per rovinare tutto. Un esempio aggiunto: x = 2 ⟹ x² = 4 è vera, ma x² = 4 ⟹ x = 2 è falsa (x = −2), quindi scrivere x = 2 ⟺ x² = 4 è un errore. Quando non si è sicuri, conviene separare le due direzioni, come consiglia il libro, annunciando ciascuna: [p → q] e poi [q → p].

## Che cosa resta fuori
Della sezione 2.2 sono stati omessi l'esempio 2.2.8, che rifà per casi la prova delle 26 carte del cap. 35, e tutto ciò che segue dall'esempio 2.2.10 in poi; è omessa anche la sezione 2.3 sulla Risoluzione. Nella registrazione 2025 la lezione successiva comincia le dimostrazioni per induzione.
