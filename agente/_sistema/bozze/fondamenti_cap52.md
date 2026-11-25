# 52. Esercizio: i Quantificatori su un Grafo di Frecce
## Il quiz e il disegno
Gli ultimi dieci minuti circa della lezione 24 (23 novembre 2026) sono dedicati a un quiz che il docente proietta dalla piattaforma d'esame del corso; il testo è di Cardone, docente del corso A (registrazione 2025). Esercizi di questo tipo, dice il docente, si trovano sul sito d'esame del corso e ci si può esercitare a rispondere. Nella registrazione 2025 lo stesso quiz era stato svolto in una lezione successiva, con le stesse risposte. Serve a ripassare il significato dei quantificatori annidati (cap. 25 e 28) e il linguaggio delle immagini e controimmagini (cap. 45).

Il testo fissa un dominio D = {1, 2, …, 10}, una relazione binaria R su D e due sottoinsiemi A e B di D, disegnati come rettangoli: A = {6, 7, 8} e B = {3, 4, 5}. C'è una freccia da a a b se e solo se vale a R b. Le frecce sono dodici:
- 3 → 1, 4 → 2, 5 → 2 (dai punti di B verso l'alto);
- 6 → 3, 6 → 4, 7 → 4, 7 → 2, 8 → 5 (dai punti di A);
- 9 → 6, 9 → 7, 9 → 10, 10 → 8 (dal basso).

![Il grafo del quiz: dieci punti, il sottoinsieme A = {6, 7, 8} e il sottoinsieme B = {3, 4, 5}; una freccia da a a b vuol dire a R b.](figure/fond/grafo_dieci_punti.png|11)

Il docente comincia descrivendo il disegno. Non ci sono cicli: seguendo le frecce non si torna mai al punto di partenza, e per questo la relazione «sembra» un ordine stretto non totale; il docente dice che la sua chiusura transitiva, cioè la relazione che si ottiene aggiungendo tutte le scorciatoie, è una relazione d'ordine (stretto). (Precisazione nostra: R da sola non è transitiva, perché ci sono 9 → 6 e 6 → 3 ma non 9 → 3, quindi non è un ordine.) Gli elementi di A hanno frecce verso B, quelli di B hanno frecce che escono verso 1 e 2, e sotto A ci sono 9 e 10, che mandano frecce verso A. È una relazione irregolare, di cui non è facile dare una descrizione semplice: per una macchina, ricorda il docente, le proprietà espresse con i quantificatori sono l'unico modo di descrivere che cosa fa una relazione.

## Prima pagina: quantificatori su A e su B
Il quiz chiede quali delle formule seguenti sono vere.

**1. ∀x ∈ A ∀y ∈ A ∃z ∈ B (x R z ∨ y R z): vera.** Dati due elementi qualunque di A, c'è un elemento z di B in cui va almeno uno dei due. Il docente osserva che vale molto di più: tutti gli elementi di A hanno qualche immagine in B, quindi basta prendere come z un'immagine di x.

**2. ∀x ∈ A ∃y ∈ B x R y: vera.** È la proprietà più forte appena usata: ogni elemento di A ha almeno un'immagine in B. Si controlla elemento per elemento: 6 va in 3 e in 4, 7 va in 4, 8 va in 5. Il docente si ferma un momento sul 7, che ha un'immagine in B (il 4) e una fuori (il 2): non è un controesempio, perché la formula chiede solo che ci sia **almeno** un'immagine in B. Non chiede che sia unica, né che tutte le immagini stiano in B.

**3. ∀x ∈ A ∀y ∈ A ∃z ∈ B (x R z ∧ y R z): falsa.** Qui si chiede che due elementi qualunque di A abbiano un'immagine **comune** in B, cioè che le loro frecce «si incontrino» in un punto di B. Per 6 e 7 è vero: si incontrano in 4. Ma 7 e 8 sono un controesempio: in B, 7 va solo in 4 e 8 va solo in 5. (Anche 6 e 8 sono un controesempio: 6 va in 3 e 4, 8 in 5.) La formula è troppo forte; ne vale una versione più debole: esistono due elementi **distinti** di A con un'immagine comune in B, cioè 6 e 7 con il 4. Detto con il linguaggio del cap. 45: la relazione R ristretta alle frecce che vanno da A a B **non è iniettiva**, nel senso che due elementi diversi di A, 6 e 7, hanno la stessa immagine 4. Nella registrazione 2025 il docente chiama questa proprietà **confluenza**: due cammini diversi si ritrovano in un passo solo nello stesso punto.

**4. ∀x ∈ B ∃y ∈ A y R x: vera.** Ogni elemento di B è immagine di qualche elemento di A, cioè ha una controimmagine in A: 3 è immagine di 6, 4 è immagine sia di 6 sia di 7, 5 è immagine di 8. Al 5 basta una sola controimmagine, perché la formula non ne chiede di più. È la **suriettività** (su B) della relazione ristretta ad A × B, la proprietà vista e rivista nel cap. 45.

**Trabocchetto d'Esame.** Le formule 1 e 3 differiscono solo per ∨ e ∧, ma la prima è vera e la seconda falsa. Inoltre la formula 2 implica la 1, mentre la 1 non dice nulla sulla 3: da una formula più debole non si deduce una più forte. Nelle formule con ∀x ∀y nessuno chiede che x e y siano diversi: anche il caso x = y va controllato (qui è sempre facile, perché ogni elemento di A ha un'immagine in B).

## Seconda pagina: quantificatori su tutto il dominio
Il disegno è lo stesso, ma ora le variabili variano su tutto D, i dieci punti. Qui le formule sono numerate da 5 a 7 per continuità; sullo schermo, nella seconda pagina del quiz, sono la 1, la 2 e la 3.

**5. ∃x ∀y y R x: falsa.** Si chiede un punto x che sia immagine di **tutti** i punti, compreso se stesso (nessuno chiede y ≠ x). Il docente usa un criterio rapido: con dieci punti, un punto immagine di tutti dovrebbe ricevere dieci frecce, e basta contare le punte delle frecce senza controllare tutti i punti. Il punto che ne riceve di più è il 2, con tre frecce (da 4, 5 e 7). Quindi nessun punto è immagine di tutti; il 2, per esempio, non è immagine di 1 né di se stesso, perché nel disegno non ci sono cappi.

**6. ∃x ∀y ¬(y R x): vera.** Si chiede un punto che non sia immagine di nessuno, cioè su cui arrivano **zero** frecce. Il 9 va bene: da lui partono tre frecce ma non ne arriva nessuna. Tutti i punti di A e di B, e anche 1 e 2 sopra B, sono punti d'arrivo di qualche freccia. (In aula il docente dice che va bene «anche il 10»; ma sul 10 arriva la freccia da 9, quindi il 9 è l'unico punto senza frecce entranti.)

**7. ∀x ∀y ∀z (x R y ∧ x R z → ∃u (y R u ∧ z R u)): falsa.** Nel 2026 il docente arriva alle 11 e la lascia da finire agli studenti. Nella registrazione 2025 la risolve: è falsa, con l'esempio x = 9, y = 7, z = 10, perché da 7 e da 10 i due cammini si ritrovano in 2 solo dopo tre passi, non in uno. La formula dice: se da un punto x partono due frecce, verso y e verso z, allora i due cammini si ritrovano in un passo solo in un punto u. È di nuovo la confluenza, questa volta su tutto il dominio. Per mostrare che è falsa basta una terna che rende vera l'ipotesi e falsa la conclusione; oltre a quella del docente, eccone due nostre (controllate al computer su tutte le terne):
- x = 3, y = z = 1: l'ipotesi 3 R 1 ∧ 3 R 1 è vera, ma da 1 non parte nessuna freccia, quindi non esiste u con 1 R u;
- un controesempio con y ≠ z: x = 9, y = 6, z = 10. Da 9 si va sia in 6 sia in 10, ma 6 va in 3 e 4, mentre 10 va solo in 8: i due cammini non si ritrovano in un passo.
La terna x = 9, y = 6, z = 7 invece soddisfa la conclusione (6 e 7 si ritrovano in 4); ma per una formula universale non basta che funzioni qualche caso.

## Come si affrontano questi quiz
Dalla correzione del docente si ricava un modo di procedere:
- leggere la formula da sinistra a destra e tradurla in una frase sul disegno («ogni punto di A ha una freccia verso B», «c'è un punto su cui non arrivano frecce»);
- per un ∀ bisogna controllare tutti i casi, e basta un controesempio per renderlo falso; per un ∃ basta un testimone;
- l'ordine dei quantificatori conta: ∀x ∃y permette a y di dipendere da x, ∃y ∀x no (cap. 25);
- contare le frecce entranti e uscenti spesso risponde subito: «immagine di tutti» vuol dire tante frecce entranti quanti sono i punti, «immagine di nessuno» zero frecce entranti.

## Riepilogo
- Con D = {1, …, 10}, A = {6, 7, 8} e B = {3, 4, 5}: sono vere le formule 1, 2, 4 e 6; sono false la 3, la 5 e la 7.
- La 2 dice che ogni elemento di A ha un'immagine in B; la 4 che la relazione ristretta ad A × B è suriettiva su B; la 3 fallisce perché la restrizione non garantisce un'immagine comune (7 e 8).
- Un punto immagine di tutti dovrebbe ricevere dieci frecce; il 9 non ne riceve nessuna.
- La confluenza (due frecce dallo stesso punto si ritrovano in un passo) è falsa: basta x = 3, y = z = 1, perché da 1 non esce nessuna freccia.
