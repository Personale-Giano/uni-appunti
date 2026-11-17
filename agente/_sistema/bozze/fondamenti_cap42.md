# 42. Esercizio 39: Tassellare una L con i Triomini
## Il problema
La lezione 20 si chiude con l'esercizio 39 di p. 98 del libro, un'altra tassellazione con i triomini del cap. 38. Questa volta la figura da coprire non è una scacchiera con un buco, ma una **L**. Il testo dell'esercizio non è tra le pagine disponibili del libro: qui è ricostruito dalla soluzione dell'esercizio 40, che lo usa, e dalla registrazione 2025, dove il docente lo presenta alla fine della stessa lezione.

**Definizione.** Per ogni n ≥ 0, chiamiamo **L di ordine n** la figura formata da tre quadrati 2ⁿ × 2ⁿ disposti a L: equivalentemente, un quadrato 2^{n+1} × 2^{n+1} a cui è stato tolto il quadrante 2ⁿ × 2ⁿ in alto a destra.

(In parole povere: è la forma del triomino, ma ingrandita. La L di ordine 0 è proprio un triomino (tre quadratini); quella di ordine 1 è un quadrato 4 × 4 senza l'angolo 2 × 2; quella di ordine 2 è un 8 × 8 senza l'angolo 4 × 4.)

**Proposizione.** Per ogni n ≥ 0 la L di ordine n si può tassellare con triomini.

(In parole povere: con tanti pezzi a L piccoli si costruisce un pezzo a L grande quanto si vuole, purché il lato raddoppi a ogni passo. L'area della L di ordine n è 3 · 4ⁿ, quindi servono esattamente 4ⁿ triomini: 1, 4, 16, 64, …)

Qui il buco non c'è: l'area 3 · 4ⁿ è già un multiplo di 3, quindi l'argomento dell'area del cap. 38 non impedisce niente.

## Il caso piccolo, a lezione
Il docente parte dalla L di ordine 1, il 4 × 4 senza l'angolo 2 × 2 in alto a destra, e chiede alla classe dove mettere i triomini (registrazione 2025). Con le indicazioni di uno studente ne bastano quattro: uno nell'angolo in basso a sinistra, uno nell'angolo in basso a destra, uno nell'angolo in alto a sinistra, e i tre quadratini rimasti, attorno al centro, formano esattamente un quarto triomino. Commenta che, prima, con un triomino mancava un quadrato 1 × 1 per fare un quadrato 2 × 2; adesso, ruotando i triomini e senza sovrapporli, si ottiene la stessa forma con il lato doppio, a cui manca un 2 × 2.

## La dimostrazione per induzione
1. **Passo base (n = 0).** La L di ordine 0 è un triomino: si tassella con un solo pezzo. (Il docente parte da n = 1, il caso con quattro triomini appena visto.)
2. **Passo induttivo.** Si suppone di saper tassellare la L di ordine n, in qualunque orientazione (basta ruotare la tassellazione), e si considera la L di ordine n + 1, cioè un quadrato di lato 2^{n+2} senza il quadrante in alto a destra. La si divide in **quattro L di ordine n**:
   - nel quadrante in basso a sinistra, una L di ordine n a cui manca l'angolo rivolto verso il centro;
   - nel quadrante in basso a destra e in quello in alto a sinistra, due L di ordine n ruotate, ciascuna senza l'angolo rivolto verso il centro;
   - al centro, una quarta L di ordine n che copre esattamente i tre angoli lasciati liberi dalle prime tre.

   Ognuna delle quattro L si tassella per ipotesi induttiva; insieme coprono tutta la L di ordine n + 1 senza sovrapposizioni.

![La L di ordine 0, 1 e 2: ognuna è formata da quattro copie della precedente, tre negli angoli e una al centro.](figure/fond/induzione_L_triomini.png|14)

È lo stesso disegno del caso piccolo, con le L di ordine n al posto dei triomini: tre negli angoli e una al centro. Il numero dei triomini quadruplica a ogni passo, da 4ⁿ a 4 · 4ⁿ = 4^{n+1}, come l'area.

**Come lo dice il docente (registrazione 2025).** Per passare dall'8 × 8 senza un 4 × 4 al caso successivo non si ricomincia da capo: si prende la soluzione già trovata, la si tratta come se fosse un solo triomino di lato doppio, e la si copia quattro volte, traslandola e ruotandola. A una macchina, dice, si può spiegare proprio così: tenere in memoria la soluzione precedente e generare la nuova con quattro trasformazioni delle coordinate, che è geometria cartesiana. La prova per induzione e il procedimento di costruzione sono la stessa cosa, come per il teorema di Golomb nel cap. 38. Il docente aggiunge che problemi come questo stanno a metà tra i videogiochi, dove la grafica li rende naturali, e la progettazione dei circuiti, dove le forme da incastrare hanno vincoli in più.

## Una seconda prova del teorema di Golomb
Nell'esercizio successivo (il 40) il libro usa questo risultato per ridimostrare il teorema di Golomb del cap. 38: per ogni n ≥ 1, ogni scacchiera deficiente 2ⁿ × 2ⁿ si tassella con triomini. L'induzione è su n.

- **Passo base (n = 1).** La 2 × 2 deficiente è un triomino.
- **Passo induttivo (da 2ⁿ a 2^{n+1}).** Si suppone che ogni 2ⁿ × 2ⁿ deficiente si tasselli. Si divide una 2^{n+1} × 2^{n+1} deficiente in quattro quadranti 2ⁿ × 2ⁿ. Il quadrante che contiene il buco è una 2ⁿ × 2ⁿ deficiente e si tassella per ipotesi induttiva. Gli altri tre quadranti formano, insieme, una L di ordine n (eventualmente ruotata), che si tassella per l'esercizio 39.

Rispetto alla prova del cap. 38 non serve il triomino centrale: il lavoro che faceva lui è nascosto dentro la tassellazione della L. Le due prove sono diverse ma entrambe costruttive, e danno entrambe un programma ricorsivo.

**Verifica sui primi casi.** Per n = 1 la L è un 4 × 4 senza un 2 × 2 e servono 4 triomini; per n = 2 è un 8 × 8 senza un 4 × 4 e ne servono 16; le tassellazioni nella figura sono costruite esattamente con la regola del passo induttivo.

Nella registrazione 2025 la lezione successiva torna agli invarianti di ciclo con la potenza veloce, annunciata nel cap. 40.
