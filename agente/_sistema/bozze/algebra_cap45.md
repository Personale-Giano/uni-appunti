# 45. Collegamento con l'Informatica: i Codici di Correzione degli Errori
## Informazione ridondante
L'algebra lineare permette di aggiungere **informazione ridondante** a un messaggio in modo da riconoscere e, in alcuni casi, correggere errori di trasmissione. L'idea è la stessa dei bit di parità visti in Fondamenti (cap. 11), ma realizzata con polinomi (cap. 10-13) e sistemi lineari. Si veda un modello molto semplificato.

(In parole povere: oltre al messaggio si spedisce qualche numero «di controllo», calcolato in modo che chi riceve possa accorgersi se qualcosa è cambiato per strada.)

**L'idea ingenua (lavagna, registrazione 2025).** Si scrive CIAO come 3, 9, 1, 15. Per un disturbo arriva 13, 9, 1, 15 e chi riceve legge MIAO, senza accorgersi di nulla. Mandando il messaggio due volte si vede che c'è un errore, ma non dove. Un buon metodo deve rilevare l'errore, localizzarlo e correggerlo, senza occupare troppa memoria. Da qui in poi il messaggio è una sequenza di numeri qualsiasi, senza una codifica in lettere.

Si vogliono trasmettere i quattro numeri {2, −7, 8, −2}. Si aggiungono due numeri a, b e si interpretano i sei numeri come coefficienti di un polinomio:

s(x) = 2x⁵ − 7x⁴ + 8x³ − 2x² + ax + b.

Si scelgono a e b imponendo due **condizioni di controllo**, s(1) = s(2) = 0. Si ottiene il sistema lineare a + b = −1, 2a + b = −8, che ha soluzione a = −7, b = 6. Si trasmette quindi {2, −7, 8, −2, −7, 6}.

## Rilevare un errore
Chi riceve il messaggio ricostruisce il polinomio e controlla che s(1) = s(2) = 0. Se una delle due uguaglianze non vale, sa che si è verificato un errore.

## Correggere un errore
Le stesse due condizioni possono aiutare a **correggere** un singolo errore. Si supponga di ricevere {2, −7, 8, 4, −7, 6}, cioè che il quarto numero sia stato alterato. Se non si sa quale posizione sia sbagliata, si sostituisce a turno ciascun coefficiente con un'incognita k e si impone di nuovo s(1) = s(2) = 0. Sostituendo il quarto coefficiente si ottiene

k + 2 = 0,   4k + 8 = 0,

che ha l'unica soluzione k = −2. Per le altre posizioni il sistema risulta incompatibile. In questo modo si individua la posizione dell'errore e si ricostruisce il dato corretto.

(In parole povere: si prova a dare la colpa a un numero alla volta; solo per il numero davvero sbagliato le due condizioni si possono soddisfare insieme.)

**Esempio dalla lavagna (registrazione 2025).** Si riceve {3, −7, 8, −2, −7, 6}. Qui s(1) = 1 e s(2) = 32, quindi c'è un errore. Si prova posizione per posizione:
- nel secondo numero: s(1) = 0 dà k = −8, s(2) = 0 dà k = −9. Non sono compatibili. (Alla lavagna il secondo valore è scritto 12, che è un errore di conto: la conclusione non cambia.)
- nel primo numero: entrambe le condizioni danno k = 2.

L'esistenza della soluzione dice due cose: l'errore era nel primo numero e il messaggio giusto è {2, −7, 8, −2}. Gli ultimi due numeri sono ausiliari e alla fine si scartano. In lezione si provano solo queste due posizioni; rifacendo il conto per le altre quattro, il sistema è sempre incompatibile.

Aggiungendo più informazione ridondante si possono correggere più errori. Per esempio, aggiungendo quattro coefficienti e imponendo s(1) = s(2) = s(3) = s(4) = 0 si ottiene un sistema lineare di quattro equazioni nei quattro coefficienti aggiunti: le quattro condizioni forniscono abbastanza controlli per cercare e correggere, in questo modello, fino a due coefficienti errati.

I codici di **Reed-Solomon**, usati tra l'altro nei QR code e in molti sistemi di memorizzazione e trasmissione digitale, sfruttano idee algebriche strettamente collegate: si rappresentano i dati mediante polinomi, si aggiunge ridondanza e si usano equazioni algebriche per localizzare e correggere gli errori. I veri codici Reed-Solomon lavorano su campi finiti, ma il semplice esempio mostra già il ruolo concreto di polinomi e sistemi lineari. Grazie a questa ridondanza, dice il docente, un QR code si legge anche se fino a un quarto non è leggibile.

## Esercizio
**Esercizio 13.7.** Si riceve la sequenza {1, −2, 3, 0, −1, 2}. I primi quattro numeri contengono l'informazione, gli ultimi due sono ridondanti, e i sei numeri sono i coefficienti di s(x) = a_{5}x⁵ + a_{4}x⁴ + a_{3}x³ + a_{2}x² + a_{1}x + a_{0}. Se la trasmissione è corretta deve valere s(1) = s(2) = 0. Si sa che esattamente uno dei sei numeri è stato modificato. Determinare quale numero è sbagliato e trovare il suo valore corretto.

Svolgimento. Con i numeri ricevuti s(1) = 1 − 2 + 3 + 0 − 1 + 2 = 3 e s(2) = 32 − 32 + 24 + 0 − 2 + 2 = 24, quindi c'è un errore. Se il coefficiente sbagliato è a_{j} e la sua correzione è un valore δ da sommargli, s(1) cambia di δ e s(2) di δ · 2^{j}. Servono quindi 3 + δ = 0 e 24 + δ · 2^{j} = 0, da cui δ = −3 e 2^{j} = 8, cioè j = 3. Il numero sbagliato è a_{3}, il terzo della sequenza, che vale 3: il suo valore corretto è 3 − 3 = **0**. Controllo con {1, −2, 0, 0, −1, 2}: s(1) = 1 − 2 − 1 + 2 = 0 e s(2) = 32 − 32 − 2 + 2 = 0.
