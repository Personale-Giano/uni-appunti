# 54. L'Aritmetica Modulare e le Congruenze Modulo n
## Un'aritmetica diversa
Con il teorema fondamentale dell'aritmetica e l'infinità dei primi (cap. 53) il docente chiude la parte sull'aritmetica degli interi. Il suo commento è che, in fondo, non si è visto nulla di veramente nuovo: si sono messi in una forma più precisa fatti che in realtà si conoscevano già, anche se in modo più empirico.

Da qui in poi l'argomento resta l'aritmetica, ma di un tipo diverso. Anche questa non dovrebbe essere una novità assoluta: è l'aritmetica che si fa ogni giorno leggendo l'orologio. L'obiettivo è, come sempre, fare le cose per bene.

## L'aritmetica dell'orologio
Su un orologio con le dodici ore i conti hanno un aspetto strano. Se sono le 9 di sera e ci si chiede che ora sarà fra 7 ore, si fa 9 + 7 = 16; ma l'orologio non segna 16, segna 4. Passato il 12, il conto è ricominciato: nell'aritmetica dell'orologio il 12 è come se fosse 0. Un'espressione come «9 + 7 = 4», assurda tra i numeri interi, sull'orologio ha senso.

Sull'orologio si possono fare anche le moltiplicazioni: il docente chiede che ore si fanno se passano 8 periodi di 6 ore ciascuno. Il conto (nostro) è 8 · 6 = 48, e 48 = 4 · 12: sono quattro giri completi del quadrante, quindi la lancetta delle ore torna esattamente dove era partita.

Lo stesso succede con i minuti, dove il conto ricomincia a 60 invece che a 12. Se sono le dieci meno un quarto, cioè le 9:45, fra 40 minuti saranno le 10:25: sui minuti si legge 45 + 40 = 25, perché 45 + 40 = 85, e arrivati a 60 il conto riparte da 0.

## Lo stesso fenomeno con le permutazioni
Il docente fa notare che questo tipo di aritmetica è già comparso nel corso, senza che ci si fermasse a guardarlo: con le potenze di una permutazione (cap. 36 e 37). Sia π una permutazione di periodo 8, cioè con π^{8} = id e nessuna potenza positiva più piccola uguale all'identità. Per la regola delle potenze π^{5} ∘ π^{7} = π^{12}; ma π^{12} = π^{8} ∘ π^{4} = π^{4}. Guardando soltanto gli esponenti, si è scritto «5 + 7 = 4»: superato 8, il conto ricomincia.

Funziona anche al contrario, con gli esponenti negativi. Si ha π^{−3} = π^{5}, perché π^{−3} = π^{−3} ∘ id = π^{−3} ∘ π^{8} = π^{5}; e infatti la differenza tra 5 e −3 è proprio 8, il periodo. È la stessa regola del cap. 37 (e del cap. 46), per cui una potenza di π si può calcolare usando, al posto dell'esponente, il resto della sua divisione per il periodo.

Il filo comune è che si tratta dell'aritmetica dei fenomeni periodici, quelli in cui dopo un po' il conto ricomincia. Sull'orologio ricomincia a 12 per le ore e a 60 per i minuti, ma potrebbe ricominciare da qualunque altro numero, a seconda del fenomeno che si studia.

## Il modulo
Questa aritmetica non si chiama «aritmetica periodica»: il nome tecnico è **aritmetica modulare**. Per farla si fissa prima un numero intero n maggiore di zero, detto il **modulo**: è il numero a partire dal quale il conto ricomincia. Per le ore dell'orologio n = 12, per i minuti n = 60, per le potenze di una permutazione n è il periodo della permutazione. La condizione precisa su n non si sente bene nella registrazione, che lì è disturbata: «maggiore di zero» è la lettura più prudente. Il caso n = 1, come si vedrà tra poco, è poco interessante.

## La congruenza modulo n
Il primo passo, spiega il docente, è introdurre una **relazione** tra i numeri interi, nel senso del cap. 8, che dipende dalla scelta del modulo n.

**Definizione.** Sia n il modulo fissato. Due interi a, b ∈ ℤ si dicono **congruenti modulo n** se n divide la differenza a − b. Si scrive a ≡ b (mod n).

(In parole povere: due numeri a e b sono congruenti modulo n se cadono nello stesso punto di un quadrante con n posizioni: per passare dall'uno all'altro si fanno solo giri completi, cioè a − b è un multiplo di n. Per esempio 16 e 4 sono congruenti modulo 12: sette ore dopo le 9 di sera la lancetta segna 4, non 16.)

Il simbolo ≡ è un segno di uguale fatto con tre linee invece di due. Un'osservazione nostra: ricorda l'uguaglianza, ma non è un'uguaglianza tra numeri, perché 16 e 4 restano numeri diversi; dice solo che, rispetto al modulo n, cadono nello stesso punto.

**Esempio.** Gli esempi della lezione, riscritti con il simbolo (conto nostro):
- 16 ≡ 4 (mod 12), perché 16 − 4 = 12 e 12 | 12: è il conto «9 + 7 = 4» dell'orologio;
- 85 ≡ 25 (mod 60), perché 85 − 25 = 60: è il conto dei minuti «45 + 40 = 25»;
- 12 ≡ 4 (mod 8), perché 12 − 4 = 8: sono gli esponenti di π^{12} = π^{4} per una permutazione di periodo 8;
- −3 ≡ 5 (mod 8), perché −3 − 5 = −8 e 8 | −8: sono gli esponenti di π^{−3} = π^{5}.

**Esempio.** Altri casi per prendere confidenza con la definizione (esempi nostri):
- −1 ≡ 11 (mod 12), perché −1 − 11 = −12 è un multiplo di 12: un'ora prima delle 12 sono le 11;
- 7 e 2 non sono congruenti modulo 4, perché 7 − 2 = 5 e 4 non divide 5;
- a ≡ 0 (mod n) vuol dire n | a − 0, cioè n | a: per esempio 48 ≡ 0 (mod 12), che è il conto degli 8 periodi di 6 ore;
- modulo 2, a ≡ b vuol dire che a − b è pari, cioè che a e b sono entrambi pari o entrambi dispari: 7 ≡ 1 (mod 2), mentre 7 e 4 non sono congruenti modulo 2.

**Attenzione.** Nella definizione è n che divide la differenza, e non il contrario: per 16 ≡ 4 (mod 12) si controlla 12 | 12, e per −3 ≡ 5 (mod 8) si controlla 8 | −8. Per esempio (osservazione nostra) 7 e 1 non sono congruenti modulo 12: la differenza 6 divide 12, ma 12 non divide 6 (e infatti le 7 e l'1 sono ore diverse sull'orologio).

## Il caso n = 1
La definizione fa capire subito, osserva il docente, perché il modulo n = 1 è poco interessante: 1 divide qualunque differenza di numeri interi, quindi con n = 1 tutti i numeri sono congruenti tra loro. Una relazione che è sempre soddisfatta non distingue niente, e non se ne ricava nulla di interessante. Una relazione è utile proprio perché a volte è soddisfatta e a volte no.

La lezione si ferma qui, appena data la definizione. Il docente ha annunciato che da qui in poi si studierà bene questa aritmetica modulare: le proprietà della relazione di congruenza, nel linguaggio del cap. 8, e il modo di fare i conti con le congruenze non sono ancora stati trattati.
