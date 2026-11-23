# 46. La Funzione Inversa e la Composizione di Funzioni
## Rovesciare le frecce
Il cap. 45 ha descritto una funzione con il suo diagramma a frecce. Le due operazioni di questo capitolo hanno anch'esse una lettura grafica molto semplice, ed è quella su cui insiste il docente: l'**inversa** si ottiene rovesciando le frecce, la **composizione** percorrendo due diagrammi uno dopo l'altro (registrazione 2025). Sul diagramma sono operazioni immediate; il docente avverte che, quando la funzione è data da un programma invece che da un disegno, calcolare l'inversa può essere un problema serio di algoritmi.

Rovesciare le frecce di una funzione non dà sempre una funzione. Il docente lo spiega guardando le due richieste del cap. 45:
- se f **non è iniettiva**, su qualche punto di Y arrivano due frecce; rovesciandole, da quel punto ne escono due, e la seconda richiesta (al più una freccia) cade;
- se f **non è suriettiva**, qualche punto di Y non riceve frecce; rovesciando, da quel punto non ne esce nessuna, e cade la prima richiesta (almeno una freccia).

Se invece f è biiettiva, su ogni punto di Y arriva esattamente una freccia, e rovesciandole ne esce esattamente una: si ottiene una funzione.

**Definizione.** Sia f: X → Y una funzione biiettiva. La **funzione inversa** di f è la funzione f⁻¹: Y → X formata dalle coppie rovesciate, f⁻¹ = {(y, x) : (x, y) ∈ f}. In altre parole, f⁻¹(y) = x esattamente quando f(x) = y.

(In parole povere: la funzione f⁻¹ fa la strada di f al contrario. Se f porta ogni studente al suo numero di matricola, f⁻¹ dalla matricola risale allo studente; funziona solo perché ogni matricola appartiene a uno e un solo studente.)

**Proposizione.** Sia f: X → Y una funzione. L'insieme delle coppie rovesciate {(y, x) : (x, y) ∈ f} è una funzione da Y a X se e solo se f è biiettiva; in questo caso anche f⁻¹ è biiettiva.

(In parole povere: si può tornare indietro senza ambiguità solo se ogni punto di arrivo è raggiunto, e da una sola strada. Una funzione che manda due studenti nello stesso turno non permette di dire, dal turno, chi era lo studente.)

**Dimostrazione.** L'insieme rovesciato è una funzione da Y a X se per ogni y ∈ Y c'è una e una sola x con (y, x) nell'insieme, cioè con f(x) = y. «Almeno una x» per ogni y è la suriettività di f; «al più una x» per ogni y è l'iniettività di f (nella forma del libro: ogni elemento dell'immagine proviene da un solo elemento del dominio). Quindi l'insieme rovesciato è una funzione esattamente quando f è suriettiva e iniettiva. Infine f⁻¹ è a sua volta biiettiva: è suriettiva perché ogni x ∈ X è f⁻¹(f(x)); è iniettiva perché da f⁻¹(y₁) = f⁻¹(y₂) = x segue y₁ = f(x) = y₂.

Il «se e solo se» è come lo enuncia il docente (registrazione 2025); il libro afferma solo che l'inversa di una biiezione è una biiezione, e ne lascia la dimostrazione come esercizio (116). La dimostrazione qui sopra è nostra.

![A sinistra la funzione f e la sua inversa, a destra una composizione f ∘ g ottenuta seguendo le frecce.](figure/fond/inversa_composizione.png|16)

**Esempio su un insieme finito.** Sia f: {1, 2, 3} → {a, b, c} con f = {(1, c), (2, a), (3, b)}, la parte sinistra della figura. È biiettiva: ogni lettera riceve una sola freccia. Rovesciando le coppie si ottiene f⁻¹ = {(c, 1), (a, 2), (b, 3)}, cioè f⁻¹(a) = 2, f⁻¹(b) = 3, f⁻¹(c) = 1.

**Esempio con una formula.** Sia f: ℝ → ℝ con f(x) = 4x + 2 (esercizio 43 del libro, soluzione nostra). È biiettiva, con gli stessi conti del cap. 45 per 5x − 3. Per trovare f⁻¹ si parte da f⁻¹(y) = x, che vuol dire y = f(x) = 4x + 2, e si ricava x: x = (y − 2)/4. Quindi f⁻¹(y) = (y − 2)/4. Controllo: f(1) = 6 e f⁻¹(6) = (6 − 2)/4 = 1.

Il docente ricorda che molte inverse si incontrano nei corsi di analisi, per esempio quella dell'esponenziale, che è il logaritmo (registrazione 2025). Il libro lo mostra con f(x) = 2ˣ da ℝ ai reali positivi ℝ⁺: è biiettiva e l'inversa è f⁻¹(y) = log₂ y, perché y = 2ˣ significa per definizione x = log₂ y. Il codominio va scelto con cura: da ℝ a tutto ℝ la stessa regola non sarebbe suriettiva, perché 2ˣ non è mai negativo né zero, e l'inversa non esisterebbe.

**Una precisazione aggiunta.** Dalla definizione segue che andare e tornare riporta al punto di partenza: f⁻¹(f(x)) = x per ogni x ∈ X e f(f⁻¹(y)) = y per ogni y ∈ Y. Nel corso di Matematica discreta questa coppia di uguaglianze è la definizione stessa di inversa (in quei riassunti, cap. 20). Attenzione alla notazione: f⁻¹ non è 1/f. Il libro usa lo stesso simbolo anche per la **controimmagine di un sottoinsieme** f⁻¹(B) = {x ∈ X : f(x) ∈ B} di un sottoinsieme B ⊆ Y, che esiste per ogni funzione, anche non biiettiva.

## La composizione
Se due funzioni si possono applicare una dopo l'altra, l'uscita della prima diventa l'ingresso della seconda.

**Definizione.** Siano g: X → Y e f: Y → Z due funzioni, con il codominio di g uguale al dominio di f. La **composizione** di f con g è la funzione f ∘ g: X → Z definita da (f ∘ g)(x) = f(g(x)).

(In parole povere: è una catena di montaggio a due stazioni. Il pezzo passa prima dalla stazione g e poi dalla stazione f, e chi guarda da fuori vede solo il pezzo che entra e quello che esce.)

Attenzione all'ordine di scrittura: in f ∘ g si applica **prima g**, anche se è scritta per seconda, e poi f. Si legge da destra a sinistra, come in f(g(x)).

**Seguire tutti i cammini.** Sul diagramma la composizione si ottiene percorrendo tutti i cammini da X a Z: per ogni x si segue la freccia di g fino a Y e poi quella di f fino a Z (registrazione 2025). È un vero algoritmo, osserva il docente, e permette di costruire la tabella della composizione dalle due tabelle di partenza. Nella parte destra della figura, con X = {1, 2, 3}, Y = {a, b, c}, Z = {u, v, w}:

- g = {(1, b), (2, c), (3, b)} e f = {(a, w), (b, u), (c, v)};
- 1 va in b e poi in u; 2 va in c e poi in v; 3 va in b e poi in u;
- quindi f ∘ g = {(1, u), (2, v), (3, u)}.

Non tutte le frecce vengono usate. Nessuna freccia di g arriva in a, quindi la freccia di f da a a w non pesa sul risultato, e w non è immagine di niente: f ∘ g non è suriettiva, anche se f da sola è biiettiva. Il docente fa notare lo stesso fenomeno sull'esempio del libro.

**L'ordine conta.** Siano f(x) = x + 3 e g(x) = x², entrambe da ℝ a ℝ. Allora (f ∘ g)(x) = x² + 3, mentre (g ∘ f)(x) = (x + 3)². Già con x = 1 si ottiene f(g(1)) = 4 e g(f(1)) = 16: le due composizioni sono funzioni diverse.

**Esempio: sconto e buono.** Un negozio applica uno sconto del 10% e accetta anche un buono da 5 euro, e permette di usarli tutti e due. Lo sconto è la funzione S(p) = 0,9p, il buono la funzione B(p) = p − 5, dove p è il prezzo in euro. Usando prima il buono e poi lo sconto si paga (S ∘ B)(p) = 0,9(p − 5) = 0,9p − 4,5; usando prima lo sconto e poi il buono si paga (B ∘ S)(p) = 0,9p − 5. Per un articolo da 80 euro sono 67,50 euro contro 67 euro. In generale, con uno sconto in percentuale r e un buono di c euro, la differenza tra i due ordini è r · c, sempre a favore dello sconto applicato per primo: lo sconto in percentuale conviene farlo agire sul prezzo pieno. (L'esempio del libro ha numeri diversi e arriva alla stessa conclusione. Il suo esercizio 53 chiede invece di mostrare che conviene sempre usare prima il buono: il conto fatto qui mostra che il testo dell'esercizio è sbagliato.)

## Composizione e proprietà delle funzioni
Questa sezione viene dagli esercizi 80-87 del §3.1 del libro; nella registrazione 2025 il docente non ci si sofferma. Le dimostrazioni sono nostre (nel corso di Matematica discreta lo stesso argomento è nel cap. 19 di quei riassunti). Siano g: X → Y e f: Y → Z.

**Proposizione.** Se f e g sono iniettive, anche f ∘ g è iniettiva. Se f e g sono suriettive, anche f ∘ g è suriettiva. Quindi la composizione di due biiezioni è una biiezione.

(In parole povere: se nessuna delle due stazioni della catena confonde due pezzi diversi, non li confonde nemmeno la catena intera; e se ognuna delle due raggiunge tutto, anche la catena raggiunge tutto.)

**Dimostrazione.** Iniettività: si suppone f(g(x₁)) = f(g(x₂)). Poiché f è iniettiva, g(x₁) = g(x₂); poiché g è iniettiva, x₁ = x₂. Suriettività: sia z ∈ Z qualunque. Poiché f è suriettiva esiste y ∈ Y con f(y) = z; poiché g è suriettiva esiste x ∈ X con g(x) = y. Allora (f ∘ g)(x) = f(y) = z.

Valgono anche due implicazioni «all'indietro», con dimostrazioni di una riga:
- se f ∘ g è iniettiva, allora **g** è iniettiva: da g(x₁) = g(x₂) segue f(g(x₁)) = f(g(x₂)), quindi x₁ = x₂;
- se f ∘ g è suriettiva, allora **f** è suriettiva: ogni z ∈ Z è f(g(x)) per qualche x, quindi è l'immagine secondo f dell'elemento g(x) di Y.

Le implicazioni inverse non valgono: da f ∘ g iniettiva non segue che f sia iniettiva, e da f ∘ g suriettiva non segue che g sia suriettiva. Basta un esempio piccolo per vederlo. Siano X = {1}, Y = {a, b}, Z = {u}, g(1) = a, f(a) = f(b) = u. La composizione f ∘ g manda 1 in u ed è biiettiva da {1} a {u}; eppure f non è iniettiva (f(a) = f(b)) e g non è suriettiva (b non è raggiunto).

## Operatori unari e binari
Il libro chiude il §3.1 con due nomi per funzioni di uso molto frequente; il docente non li riprende nella registrazione 2025, ma il secondo servirà per le stringhe.

**Definizione.** Un **operatore binario** su un insieme X è una funzione da X × X a X; un **operatore unario** su X è una funzione da X a X.

(In parole povere: un operatore binario prende due oggetti dello stesso tipo e ne restituisce uno ancora di quel tipo, come la somma che da due numeri dà un numero. Un operatore unario ne prende uno e ne restituisce uno, come il cambio di segno.)

La somma è un operatore binario sugli interi positivi: la somma di due interi positivi è ancora un intero positivo. La sottrazione invece **non** lo è, perché 2 − 5 = −3 esce dall'insieme. Sulle proposizioni, ∧ e ∨ sono operatori binari e ¬ è un operatore unario (cap. 13).

## Riepilogo
- Rovesciando le frecce di f si ottiene una funzione se e solo se f è biiettiva: la non iniettività fa uscire due frecce da un punto, la non suriettività lascia punti senza frecce.
- f⁻¹(y) = x esattamente quando f(x) = y; con una formula si ricava x dall'equazione y = f(x). Esempi: 4x + 2 ha inversa (y − 2)/4; 2ˣ da ℝ a ℝ⁺ ha inversa log₂ y.
- (f ∘ g)(x) = f(g(x)): prima g, poi f. Sul diagramma si seguono tutti i cammini; frecce di f che partono da punti non raggiunti da g non contano.
- In generale f ∘ g ≠ g ∘ f.
- La composizione conserva iniettività e suriettività; da f ∘ g iniettiva segue g iniettiva, da f ∘ g suriettiva segue f suriettiva.

Nel prossimo capitolo una funzione speciale: la sequenza, che ha per dominio un insieme di interi.
