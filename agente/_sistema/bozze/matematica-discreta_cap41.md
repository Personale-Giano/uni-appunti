# 41. La Dimostrazione del Teorema della Parità
## Dove eravamo rimasti
Nel cap. 39 si è visto che ogni permutazione si scrive come composizione di scambi, ma in tanti modi diversi; nel cap. 40 è stato enunciato il teorema che mette ordine in questa libertà.

**Teorema (parità).** Se π = s₁ ∘ … ∘ s_{k} = t₁ ∘ … ∘ t_{h}, dove tutti gli s_{i} e i t_{j} sono scambi, allora k e h hanno la stessa parità: sono entrambi pari o entrambi dispari.

(In parole povere: una stessa permutazione può richiedere 3 mosse o 7 mosse, ma mai 3 in un modo e 4 in un altro.)

Il docente sottolinea il prezzo della semplificazione: usare solo mosse elementari rende la scrittura semplice da un lato, ma la fa diventare non unica dall'altro. Il teorema dice che sotto questa non unicità resta qualcosa di fisso. La dimostrazione è divisa in due passi: il primo è tecnico e trasforma l'enunciato in una proprietà dell'identità; il secondo, quello importante, dimostra quella proprietà.

## Primo passo: ridursi all'identità
L'identità si può sempre scrivere come id = π ∘ π⁻¹. L'idea è usare una delle due scritture per π e l'altra per π⁻¹:

id = π ∘ π⁻¹ = (s₁ ∘ … ∘ s_{k}) ∘ (t₁ ∘ … ∘ t_{h})⁻¹ = s₁ ∘ … ∘ s_{k} ∘ t_{h}⁻¹ ∘ … ∘ t₁⁻¹.

L'ultimo passaggio usa la regola per l'inversa di una composizione (cap. 20, e per gli scambi cap. 40): si invertono i fattori e se ne rovescia l'ordine. Fin qui non si è usato nulla di particolare: questo passaggio, come fa notare il docente, è vero qualunque cosa siano gli s e i t. Ora invece si usa in modo essenziale che i t_{j} sono scambi, e ogni scambio coincide con il proprio inverso (scambiare di nuovo a e b riporta tutto a posto). Quindi:

id = s₁ ∘ … ∘ s_{k} ∘ t_{h} ∘ … ∘ t₁.

A destra c'è una scrittura dell'identità come composizione di **k + h scambi**.

Perché questo basta? Due numeri hanno la stessa parità esattamente quando la loro somma è pari: pari + pari e dispari + dispari danno un numero pari, mentre pari + dispari dà un numero dispari. Quindi per dimostrare il teorema basta dimostrare che **l'identità non si può scrivere come composizione di un numero dispari di scambi**: allora k + h è pari, e k e h hanno la stessa parità.

## Secondo passo: l'idea di togliere due alla volta
Come si dimostra che una quantità di oggetti non è dispari? Il docente ricorda l'idea di togliere gli oggetti a due a due: se da un mucchio di oggetti se ne tolgono due alla volta e alla fine non ne resta nessuno, il totale era pari; se ne resta uno, era dispari.

L'idea è quindi manipolare la scrittura id = r₁ ∘ … ∘ r_{m} (con m = k + h e tutti gli r_{i} scambi) con delle trasformazioni che non cambiano la permutazione e che lasciano invariato il numero di scambi oppure lo diminuiscono esattamente di due. Se così facendo si arriva a non avere più nessuno scambio, m era pari.

## L'osservazione cruciale
Si fissa l'attenzione sugli scambi della scrittura che contengono il numero 1.

**Osservazione.** In una scrittura dell'identità come composizione di scambi, gli scambi che contengono 1 sono **nessuno oppure almeno due**: non può essercene uno solo.

Infatti, supponiamo che ci sia un solo scambio (1 a) che contiene 1, con prima e dopo altri scambi in cui 1 non compare. L'uguaglianza tra la scrittura e l'identità è un'uguaglianza tra funzioni, quindi le due devono mandare 1 nello stesso elemento; l'identità manda 1 in 1. Seguiamo invece 1 nella composizione, da destra a sinistra:
- gli scambi a destra di (1 a) non contengono 1, quindi lo lasciano fermo;
- lo scambio (1 a) manda 1 in a;
- negli scambi successivi a può essere spostato in qualcos'altro, e poi in qualcos'altro ancora, ma per tornare a 1 servirebbe uno scambio che contiene 1, e non ce ne sono più.

Quindi la composizione manda 1 in un elemento diverso da 1, e non può essere l'identità. Contraddizione.

Il docente insiste che questa è l'osservazione che fa funzionare tutta la dimostrazione: senza di essa ci si potrebbe ritrovare con un solo scambio contenente 1 e non si saprebbe più come proseguire.

## Le quattro trasformazioni elementari
Le trasformazioni agiscono su due scambi vicini e lasciano tutti gli altri come sono. Con a, b, c numeri diversi da 1 e diversi tra loro (le uguaglianze si verificano seguendo ogni elemento da destra a sinistra, come nel cap. 39):

1. **Scambi disgiunti**: (1 a) ∘ (b c) = (b c) ∘ (1 a). Due cicli disgiunti commutano (cap. 33), quindi lo scambio con 1 passa a destra.
2. **Scambi con un elemento in comune diverso da 1**: (1 a) ∘ (a b) = (a b) ∘ (1 b). Verifica: a sinistra 1 va in a, a va in b, b va in a e poi in 1; a destra 1 va in b e poi in a, b va in 1, a va in b. Lo scambio con 1 non è più lo stesso, ma ora sta a destra.
3. **Due scambi diversi con 1**: (1 a) ∘ (1 b) = (a b) ∘ (1 a). Verifica: a sinistra 1 va in b, b va in 1 e poi in a, a va in 1; a destra 1 va in a e poi in b, b va in a, a va in 1 e poi resta fermo. Qui lo stesso scambio (1 a) passa da sinistra a destra, ma soprattutto gli scambi che contengono 1 scendono di uno.
4. **Due scambi uguali con 1**: (1 a) ∘ (1 a) = id, quindi i due scambi si cancellano.

Le prime tre trasformazioni sostituiscono due scambi con due scambi: il totale non cambia. La quarta toglie due scambi: il totale scende esattamente di due. Nessuna aumenta il numero degli scambi che contengono 1.

## La procedura
Si usano le trasformazioni 1 e 2 per spostare verso destra tutti gli scambi che contengono 1, finché non si ritrovano tutti vicini in fondo alla scrittura. A quel punto gli ultimi due sono della forma (1 a) ∘ (1 b) oppure (1 a) ∘ (1 a):
- nel primo caso si applica la trasformazione 3 e gli scambi con 1 scendono di uno; il nuovo scambio (a b) sta a sinistra, quello con 1 rimane in fondo;
- nel secondo caso si applica la trasformazione 4 e gli scambi con 1 scendono di due.

Si ripete. Dopo ogni trasformazione la scrittura è ancora uguale all'identità, quindi per l'osservazione cruciale gli scambi con 1 non possono mai essere uno solo. Quando ne restano due, vicini in fondo, devono per forza essere uguali: se fossero (1 a) ∘ (1 b) con a ≠ b, la trasformazione 3 ne lascerebbe uno solo, il che è impossibile. Si applica allora la trasformazione 4 e gli scambi con 1 spariscono del tutto.

Poi si fissa l'attenzione su 2 e si ripete esattamente lo stesso discorso, con 2 al posto di 1. Gli scambi con 1 non rientrano più: ogni trasformazione sostituisce due scambi con altri che coinvolgono gli stessi elementi, e 1 non c'era. Poi si passa a 3, a 4, e così via fino a n. Alla fine non resta nessuno scambio: la scrittura è diventata quella vuota, cioè l'identità senza scambi.

## La conclusione
L'unico passo in cui il numero totale degli scambi cambia è la trasformazione 4, e lo fa scendere di due. Si è partiti da m = k + h scambi e si è arrivati a 0 togliendone due alla volta: quindi m è pari. Dunque l'identità non si scrive mai con un numero dispari di scambi, k + h è pari, e k e h hanno la stessa parità. ∎

Come fa notare il docente, durante la procedura non si tiene traccia di che cosa succede agli altri elementi mentre si sistemano quelli con 1: sarebbe troppo complicato, e in realtà non interessa.

**Esempio.** Dal cap. 39, (2 3) = (1 3) ∘ (1 2) ∘ (1 3); componendo a sinistra con (2 3) si ottiene una scrittura dell'identità con quattro scambi:

id = (2 3) ∘ (1 3) ∘ (1 2) ∘ (1 3).

Gli scambi con 1 sono tre (come previsto, non uno solo), già vicini in fondo.
- Agli ultimi due, (1 2) ∘ (1 3), si applica la trasformazione 3 con a = 2 e b = 3: diventano (2 3) ∘ (1 2). La scrittura è (2 3) ∘ (1 3) ∘ (2 3) ∘ (1 2): sempre quattro scambi, ma quelli con 1 sono scesi a due.
- Lo scambio (1 3) non è vicino a (1 2): lo si sposta a destra con la trasformazione 2, (1 3) ∘ (3 2) = (3 2) ∘ (1 2). La scrittura è (2 3) ∘ (2 3) ∘ (1 2) ∘ (1 2).
- I due scambi con 1 rimasti in fondo sono uguali, come doveva essere: si cancellano (trasformazione 4). Resta (2 3) ∘ (2 3), con due scambi.
- Passando al numero 2, anche questi due si cancellano: zero scambi.

Il totale è passato da 4 a 2 a 0, togliendo due alla volta.

## Un teorema che non dà un algoritmo
Il docente avverte che questa è una dimostrazione teorica: dimostra il teorema, ma non è il modo per calcolare in pratica la parità di una permutazione. Per quello c'è una strada molto più semplice, che passa per i cicli e la scrittura di un ciclo con gli scambi: è l'argomento del prossimo capitolo.
