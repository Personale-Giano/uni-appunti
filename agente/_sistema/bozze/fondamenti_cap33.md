# 33. Confutare un Enunciato: Controesempi, Errori Comuni e il Paradosso del Bevitore
## Il controesempio
Per confutare ∀x P(x) basta un solo elemento del dominio che renda P(x) falsa: il **controesempio** già incontrato nel cap. 21. Il lavoro è giustificarlo: mostrarlo e far vedere perché rende falsa la proprietà.

**Esempio: 2^{n} + 1 è sempre primo?** L'enunciato è: per ogni n ∈ ℤ⁺, 2^{n} + 1 è primo. I primi tentativi vanno bene: n = 1 dà 3, n = 2 dà 5. Ma n = 3 dà 2³ + 1 = 9 = 3 · 3, che non è primo. L'enunciato è falso, anche se poi n = 4 dà 17, che è primo: un ∀ non si salva con altri esempi favorevoli.

**La fortuna non è garantita (registrazione 2025).** Il docente osserva che qui si è stati fortunati: il primo controesempio è piccolo. In generale potrebbe essere enorme, oltre le risorse disponibili anche con una macchina. Lo stesso problema, dice, sta dietro alla crittografia a chiave pubblica: chi prova tutte le chiavi prima o poi trova quella giusta, ma le chiavi hanno più di 2000 cifre binarie, cioè più di 600 cifre decimali. Sapere che un valore esiste non vuol dire poterlo trovare.

## Quando non si sa se è vero o falso
Spesso non si sa da che parte stare. Il consiglio è cominciare provando a dimostrare: se si riesce, si è finito; se ci si blocca, **il punto in cui ci si blocca può indicare il controesempio**. Viceversa, se i controesempi falliscono, il motivo del fallimento può guidare la dimostrazione. La stessa idea si è già vista per le regole di inferenza nel cap. 24.

**Esempio: (A ∩ B) ∪ C = A ∩ (B ∪ C) è vera per tutti gli insiemi?** Sembra una proprietà associativa, ma mescola due operazioni. Si tenta la prima inclusione, espandendo le definizioni:

- x ∈ (A ∩ B) ∪ C vuol dire: (x ∈ A e x ∈ B) oppure x ∈ C;
- x ∈ A ∩ (B ∪ C) vuol dire: x ∈ A e (x ∈ B oppure x ∈ C).

Si ragiona per casi. Se x ∈ A e x ∈ B, la tesi segue subito. Se invece x ∈ C, bisognerebbe dedurre x ∈ A, e questo è impossibile: A e C sono insiemi qualunque. Qui la prova si blocca, e il blocco dice che cosa cercare: **un elemento che stia in C ma non in A**.

Un controesempio è A = {1, 2, 3}, B = {2, 3, 4}, C = {3, 4, 5}. Si ha A ∩ B = {2, 3}, quindi (A ∩ B) ∪ C = {2, 3, 4, 5}. Si ha B ∪ C = {2, 3, 4, 5}, quindi A ∩ (B ∪ C) = {2, 3}. I due insiemi sono diversi.

**Esempio dalla lavagna (registrazione 2025).** Il docente segue il suggerimento del blocco nel modo più semplice possibile: A e B vuoti, C = {0}. Il lato sinistro vale {0}, il destro è vuoto. Aggiunge che una macchina può fare i due tentativi in parallelo, dimostrare e cercare un controesempio, e che il primo può aiutare il secondo. Qui, secondo lui, i controesempi sono così frequenti che quasi tutti gli insiemi scelti a caso lo sono.

## Come si scrive una dimostrazione
Sono consigli del libro, utili anche per la domanda aperta d'esame (cap. 34).

- **Costruire:** scrivere ipotesi e conclusione, poi richiamare il significato dei termini; «n è pari» si traduce in n = 2k. Per due insiemi uguali, mostrare entrambe le inclusioni.
- **Capire:** provare valori specifici. Aiutano a capire, ma non dimostrano un enunciato universale.
- **Confutare:** presentare il controesempio e dire perché rende falsa la proprietà.
- **Scrivere:** riportare l'enunciato, segnalare dove inizia la dimostrazione, usare frasi complete, che possono contenere simboli, e chiudere dichiarando la conclusione.
- **Annunciare:** dire al lettore che cosa si sta per provare, soprattutto la direzione di un'inclusione.
- **Giustificare:** indicare il motivo di ogni deduzione, per esempio «per definizione di unione».

## Tre errori comuni
**Primo errore: lo stesso simbolo per quantità diverse.** Una falsa dimostrazione che il prodotto di due pari è un quadrato: m = 2k e n = 2k, quindi mn = (2k)², quindi mn = a² con a = 2k. L'errore è nel primo passo: i due numeri pari vanno scritti m = 2k₁ e n = 2k₂, e nulla dice che k₁ e k₂ siano uguali (cap. 31). L'enunciato, del resto, è falso: con m = 2 e n = 4 si ha mn = 8, che non è un quadrato.

**Secondo errore: dimostrare con casi particolari.** Verificare che con m = 11 e n = 4 la somma 15 sia dispari prova l'enunciato del cap. 31 solo per quei due valori. Un caso particolare può suggerire che un enunciato sia vero, non dimostrarlo.

**Terzo errore: dare per vero ciò che si deve provare.** Si vuole dimostrare che, se m e m + n sono pari, anche n è pari. Una falsa dimostrazione comincia scrivendo m = 2k₁ e n = 2k₂, e arriva a n = (m + n) − m = (2k₁ + 2k₂) − 2k₁ = 2k₂. Scrivere n = 2k₂ all'inizio vuol dire già supporre che n sia pari, cioè la tesi. Questo errore si chiama **ragionamento circolare**.

(In parole povere: è come dimostrare di avere ragione partendo dall'affermazione «ho ragione». I conti possono anche tornare, ma non provano niente.)

L'enunciato però è vero, e una dimostrazione corretta è breve: per ipotesi m = 2k₁ e m + n = 2h, con h intero; allora n = (m + n) − m = 2h − 2k₁ = 2(h − k₁), che è pari. Questa volta n = 2(h − k₁) è la conclusione, non il punto di partenza.

## Il paradosso del bevitore
Il principio che segue viene dalla registrazione 2025, dove il docente lo chiama «principio del bevitore» (~drinker principle~) e lo presenta come un esempio di umorismo inglese: serve a far vedere che il linguaggio della logica, pur ricalcato su quello umano, ha delle differenze.

**Teorema (principio del bevitore).** In un dominio non vuoto, per qualunque proprietà P, esiste un x tale che se P(x) è vera allora P(y) è vera per ogni y. In simboli: ∃x (P(x) → ∀y P(y)).

(In parole povere: in ogni pub non vuoto c'è una persona tale che, se lei beve, bevono tutti. Sembra la promessa di un capo a cui tutti obbediscono, ma non lo è: l'implicazione materiale non chiede nessun legame tra lei e gli altri.)

Nel linguaggio comune la frase è quasi sempre falsa: di solito in un pub ciascuno beve per conto proprio, e solo in casi particolari, come un brindisi a una festa, una persona trascina tutti. Eppure, con il significato logico dell'implicazione (cap. 16), la formula è vera sempre.

**Dimostrazione.** Il dominio è non vuoto: il docente ricorda che i domini del discorso si suppongono tali. Si ragiona per casi, a seconda che ∀y P(y) sia vera o falsa.

- **Tutti hanno la proprietà.** Si sceglie un x qualunque: la tesi dell'implicazione è vera, quindi l'implicazione è vera.
- **Non tutti ce l'hanno.** Allora esiste un a con P(a) falsa. Si sceglie x = a: l'ipotesi è falsa, quindi l'implicazione è vera per difetto.

In entrambi i casi si è trovato l'x richiesto. A parole: se c'è qualcuno che non beve, «il bevitore» è lui; se bevono tutti, va bene chiunque.

Come sottolinea il docente, il principio è vero ma non dà alcuna informazione: è banale, e dipende in modo essenziale dal fatto che l'implicazione sia materiale. A una domanda se valga anche l'equivalenza, risponde che con un x scelto in modo particolare si può ottenere, ma è un discorso da corso di logica del terzo anno, e lo lascia lì.

Il capitolo seguente raccoglie gli esercizi riassuntivi su queste tecniche.
