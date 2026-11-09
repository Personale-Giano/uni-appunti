# Algebra lineare, Lezione 14: Applicazioni lineari I (lavagne dalla registrazione Webex del 30 ott 2024, prof. Radeschi)

Fonte: video della registrazione del 2024, file `audio/algebra_L14_2024.mp4` (107 min, completo; **la pausa è registrata nel video**, 48:30 – 57:30 circa, ma l'audio in quel tratto è vuoto), trascrizione `trascrizioni/algebra_L14_2024.txt`.
Contenuto letto da 43 fotogrammi regolari (uno ogni 2,5 minuti, da 00:00 a 105:00; quello a 00:00 è nero, quindi 42 utili), più fotogrammi intermedi estratti apposta: 12 durante la pausa (ogni 45 s da 48:15 a 56:30), di cui aperti 6 (48:15, 51:15, 53:30, 54:15, 55:45, 56:30), e 4 sulla fine (105:30 – 107:00), di cui aperti 2 (106:00, 107:00). La lavagna è in 4 pannelli (alto/basso, sinistra/destra) che vengono riempiti, fatti scorrere e cancellati; qui il contenuto è in ordine di comparsa.

Convenzioni:
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss, approssimati per eccesso: la scritta è già visibile a quel tempo).
- **[a voce]** indica ciò che è solo detto e non scritto; il tempo tra parentesi è quello dell'audio. I tempi dell'audio sono anticipati di circa 1–2 minuti rispetto ai fotogrammi.
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali: sono ricostruite da una trascrizione automatica piena di errori.
- Sulla lavagna il rango è scritto rg(A); le colonne di A sono scritte con il **pedice**, A₁, …, Aₙ (nei capitoli si usa A^{i}); «tale che» è abbreviato Tc (qui t.c.); le parentesi delle matrici sono a volte tonde, a volte quadre. Qui sono riportati così.

## Titolo, avviso e definizione (00:00 – 07:30)
**LEZIONE 14: APPLICAZIONI LINEARI**
⚠ **CORSO C:** NO LEZIONE Mer 6 ⇝ LEZIONE VEN 8 15:00 – 17:00

**Def** V, W sp vettoriali su 𝕂, una **APPLICAZIONE/MAPPA/TRASFORMAZIONE LINEARE** è una funzione f : V → W t.c.
- ① ∀v₁, v₂ ∈ V: f(v₁ +_V v₂) = f(v₁) +_W f(v₂)
- ② ∀v ∈ V, ∀a ∈ 𝕂: f(a ·_V v) = a ·_W f(v)

(I pedici V e W sotto i segni di somma e di prodotto sono piccoli; a voce dice che la somma a sinistra è scritta in verde.)

[a voce] (≈ 00:00 – 00:33) Il corso C non avrà lezione mercoledì della settimana dopo; la lezione è recuperata venerdì dalle 15 alle 17.
[a voce] (≈ 00:33 – 01:44) Si passa al concetto fondamentale del corso: le applicazioni lineari sono «il modo in cui gli spazi vettoriali comunicano tra di loro».
[a voce] (≈ 01:44 – 02:33) Applicazione lineare, mappa lineare e trasformazione lineare sono sinonimi. È la funzione che fa «la cosa più semplice» dal punto di vista degli spazi vettoriali: manda somme in somme e prodotti per scalare in prodotti per scalare.
[a voce] (≈ 03:12 – 05:26) Per ogni proprietà si possono fare due cose: prima operare in V e poi mandare in W, oppure mandare in W e poi operare lì. La proprietà dice che le due strade danno lo stesso risultato. A sinistra la somma (o il prodotto) è quella di V, a destra quella di W.

## Tre osservazioni (07:30 – 15:00)
**Oss** ① Le propr di una mappa lineare equivalenti a
⊛ f(v₁ + a·v₂) = f(v₁) + a·f(v₂) ∀v₁, v₂ ∈ V, ∀a ∈ 𝕂
(il simbolo ⊛ è aggiunto a 20:00, quando l'esempio lo richiama)

② f lineare ⟹ f(0_V) = f(0·v) = 0·f(v) = 0_W (sotto: v ∈ V, f(v) ∈ W)
⟹ **f(0_V) = 0_W**

③ f : V → W, v₁ … vₙ ∈ V
f(a₁v₁ + … + aₙvₙ) =① f(a₁v₁) + … + f(aₙvₙ) =② a₁f(v₁) + … + aₙf(vₙ)
⇝ f **MANDA COMB LIN** di v₁ … vₙ **in COMB LIN DI** f(v₁) … f(vₙ), **con gli stessi coefficienti**
(a 15:00 sono sottolineati v₁, vₙ a sinistra e f(v₁), f(vₙ) a destra)

[a voce] (≈ 05:57 – 06:37) Se viene data una funzione e viene chiesto di controllare che sia una mappa lineare, bisogna controllare che queste due proprietà valgano.
[a voce] (≈ 06:37 – 08:32) In alternativa le due proprietà si riassumono in una sola, ⊛: «avrete la scelta» di controllare le due proprietà o soltanto questa.
[a voce] (≈ 08:32 – 09:48) Lo 0 dentro f(0·v) è lo scalare 0, il numero zero; la linearità permette di portarlo fuori.
[a voce] (≈ 09:48 – 10:54) **Non è un se e solo se**: una funzione che manda lo zero nello zero non è necessariamente lineare. È però un modo veloce di controllare: se una funzione non manda lo zero nello zero, di sicuro non è lineare.
[a voce] (≈ 13:19 – 14:00) «Manda» vuol dire che l'immagine di una combinazione lineare di v₁ … vₙ è una combinazione lineare di f(v₁) … f(vₙ), con gli stessi coefficienti.

## Un esempio lineare (15:00 – 27:30)
**ESEMPIO** T : ℝ² → ℝ², T( x ; y ) = ( 3x + 2y ; x ) è lin?
⊛ ∀( x ; y ), ( x′ ; y′ ) ∈ ℝ², ∀a ∈ ℝ verificare che
T( ( x ; y ) + a( x′ ; y′ ) ) =? T( x ; y ) + a T( x′ ; y′ ), con le graffe: L a sinistra, R a destra

L = T( x + ax′ ; y + ay′ ) = ( 3(x + ax′) + 2(y + ay′) ; x + ax′ ) = ( 3x + 3ax′ + 2y + 2ay′ ; x + ax′ )
R = ( 3x + 2y ; x ) + a( 3x′ + 2y′ ; x′ ) = ( 3x + 2y + 3ax′ + 2ay′ ; x + ax′ )
(a 27:30 due archi collegano i due risultati e accanto all'uguaglianza ⊛ c'è un ✓)

[a voce] (≈ 15:12 – 15:44) Chiede per alzata di mano se gli studenti preferiscono vedere prima un esempio o un non esempio; poi chiede se controllare le due proprietà o la sola ⊛, e sceglie ⊛: «leggermente più lunga» ma fa risparmiare tempo.
[a voce] (≈ 19:03 – 19:35) Il modo più semplice è calcolare separatamente il lato sinistro e il lato destro e controllare che siano uguali.
[a voce] (≈ 25:37 – 26:44) **Che cosa rende lineare questa mappa:** in mezzo ai conti è facile perdersi; il punto è che ogni componente è una combinazione lineare di x e y, un polinomio di grado 1 in x e y.
[a voce] (≈ 26:44 – 27:15) Allo stesso modo una funzione da ℝ³ in ℝ³ le cui componenti sono tutte combinazioni lineari di x, y e z sarà lineare.

[verifica] L − R = 0 in modo simbolico; entrambi valgono ( 3x + 2y + 3ax′ + 2ay′ ; x + ax′ ).

## Due non esempi (27:30 – 37:30)
**NON-ESEMPI.**
f : ℝ² → ℝ², f( x ; y ) = ( x + 1 ; y² ) è lineare?
① f( 0 ; 0 ) = ( 1 ; 0 ) ≠ ( 0 ; 0 ) ⟹ **f NON è lineare**
(riga di separazione)
f : ℝ² → ℝ², f( x ; y ) = ( x ; y² ) è lineare?
[ f( 0 ; 0 ) = ( 0 ; 0² ) = ( 0 ; 0 ) ] (fra parentesi quadre)

② f( a( x ; y ) ) =? a f( x ; y ) ∀a ∈ ℝ, ∀( x ; y ) ∈ ℝ², con le graffe L e R
L = f( ax ; ay ) = ( ax ; a²y² )
R = a·( x ; y² ) = ( ax ; ay² )
L e R uniti da una graffa con **≠** (a 37:30)

[a voce] (≈ 28:34 – 29:05) **Consiglio del docente:** «una cosa che io vi consiglio sempre di fare», perché è molto veloce, è controllare anzitutto se l'origine viene mandata nell'origine: se non succede, già si sa che la funzione non può essere lineare.
[a voce] (≈ 29:47 – 30:21) Il «colpevole» della non linearità è il +1, il termine noto: se ci sono termini noti la funzione non è lineare.
[a voce] (≈ 30:54 – 31:26) Ripete: una mappa che manda l'origine nell'origine non è necessariamente lineare; «alla peggio» si perde un po' di tempo.
[a voce] (≈ 31:26 – 32:40) Per la seconda funzione il controllo dell'origine «non ci sta dicendo niente». Nessuna delle proprietà vale; sceglie la più semplice da guardare, la seconda della definizione.
[a voce] (≈ 34:23 – 35:28) I due vettori non sono uguali: nella seconda componente compare a·y² da una parte e a²y² dall'altra. Per esempio con a = 2 si ottiene 2y² contro 4y².
[a voce] (≈ 35:28 – 36:08) Il colpevole qui è il termine elevato al quadrato: quando compare un quadrato, la funzione non è lineare.

[verifica] f(0, 0) = (1, 0) per la prima. Per la seconda f(ax, ay) = (ax, a²y²), a·f(x, y) = (ax, ay²); con a = 2: (2x, 4y²) contro (2x, 2y²). Il controesempio numerico con a = 2 è detto solo a voce, senza scegliere un vettore: serve y ≠ 0, per esempio (x, y) = (0, 1) dà (0, 4) ≠ (0, 2).

## Esempi importanti: mappa nulla, identità, L_{A} (37:30 – 48:30)
**ESEMPI IMPORTANTI**
① **ESEMPI BANALI**
ⓐ T : V → W, T(v) = 0_W è lineare (MAPPA NULLA)
ⓑ T : V → V, T(v) = v è lineare; T IDENTITÀ, T = id_V = I_V

② A ∈ M(m, n, 𝕂), A = [ a₁₁ … a₁ₙ ; ⋮ ; aₘ₁ … aₘₙ ]
⇝ (freccia ondulata) L_A : 𝕂ⁿ → 𝕂ᵐ
L_A[ x₁ ; ⋮ ; xₙ ] = A·[ x₁ ; ⋮ ; xₙ ] = [ a₁₁x₁ + a₁₂x₂ + … + a₁ₙxₙ ; ⋮ ; aₘ₁x₁ + aₘ₂x₂ + … + aₘₙxₙ ]
(sotto, uno schema delle taglie:) m[ A ]n · [ x ]n = [ Ax ]m (con x sotto il vettore colonna)

**L_A è lineare.**
L_A(x + a·x′) = A·(x + ax′) =distr Ax + A(ax′)
= Ax + a·Ax′
= L_A(x) + aL_A(x′) ✓

(A destra, alla stessa altezza di «= Ax + a·Ax′», c'è anche «= L_A(x) + aL_A(x)»: scritto prima del passaggio intermedio, senza l'apice sul secondo x; la riga finale sotto, con ✓, è quella corretta.)

[a voce] (≈ 36:08 – 37:03) Dopo esempi molto specifici, «classi di esempi molto importanti»; si comincia con quelli «tra virgolette banali».
[a voce] (≈ 37:35 – 38:55) La mappa che manda ogni vettore nello zero a volte si chiama mappa nulla; quella che manda ogni vettore in se stesso si chiama identità e a volte si scrive id_V.
[a voce] (≈ 39:28 – 40:43) La «classe di esempi fondamentali» sono le mappe lineari definite da matrici: una matrice m × n produce una mappa da 𝕂ⁿ a 𝕂ᵐ, che prende vettori colonna con n elementi e dà vettori colonna con m elementi.
[a voce] (≈ 41:21 – 42:35) Un vettore colonna si può pensare come una matrice n × 1; il numero di colonne di A è uguale al numero di righe di x, quindi si possono moltiplicare e si ottiene una matrice con m righe e una colonna.
[a voce] (≈ 43:38 – 44:16) La L sta per «left», perché si moltiplica a sinistra per A.
[a voce] (≈ 45:58 – 47:49) Usa la distributività del prodotto di matrici rispetto alla somma e il fatto che il prodotto per scalare commuta con il prodotto di matrici (mentre il prodotto di matrici non è commutativo): la a si porta fuori.

## La pausa (48:30 – 57:30)
[a voce] (≈ 48:26) Dieci minuti di pausa. Da qui a ≈ 57:48 l'audio è vuoto.

Il video invece prosegue: il docente resta alla lavagna con alcuni studenti e scrive, nel pannello in basso a sinistra (da 50:00), un esempio aggiuntivo:
L_A : ℝⁿ → 𝕂ᵐ | A = [ 1 2 3 ; 3 1 0 ]
L_A(x) = Ax, x = ( x₁ ; ⋮ ; xₙ )
L_A : ℝ³ → ℝ², L_A( x ; y ; z ) = [ 1 2 3 ; 3 1 0 ]·( x ; y ; z ) = ( x + 2y + 3z ; 3x + y )
L_A( 1 ; 1 ; 2 ) = ( 9 ; 4 )

A 55:00, nel pannello sotto, ci sono segni a margine di una spiegazione sul secondo non esempio: si legge «f( ☺ ; △ ) = ( ☺ ; △² )» (una faccina e un triangolo al posto di x e y; lettura incerta) e sotto «f( ax ; ay )». A 56:30 tutto questo è cancellato.

**Questo esempio non è nell'audio e non è detto alla classe**: è una spiegazione a pochi studenti durante la pausa.

[verifica] [ 1 2 3 ; 3 1 0 ]·(1, 1, 2) = (1 + 2 + 6, 3 + 1 + 0) = (9, 4). La terza componente del vettore (2) e la prima riga di A sono le letture compatibili con il risultato scritto.

## Esempi espliciti di L_{A} e la derivata (57:30 – 70:00)
**2.1** A = ( 1 0 2 ; 1 2 4 ) ∈ M(2, 3, ℝ)
⇝ L_A : ℝ³ → ℝ²
L_A( x ; y ; z ) = ( 1 0 2 ; 1 2 4 )( x ; y ; z ) = ( x + 2z ; x + 2y + 4z )
L_A( 1 ; 1 ; 1 ) = ( 3 ; 7 )

**2.2** A = ( 3 2 ; 1 0 ) ∈ M(2, 2, ℝ)
⇝ L_A : ℝ² → ℝ²
L_A( x ; y ) = ( 3 2 ; 1 0 )( x ; y ) = ( 3x + 2y ; x )

**③** D : 𝕂[x]_d → 𝕂[x]_{d−1}
D(a_dx^d + … + a₂x² + a₁x + a₀) = a_d d x^{d−1} + … + a₂2x + a₁ + 0
D(p₁(x) + p₂(x)) = D(p₁(x)) + D(p₂(x))
D(λp(x)) = λ·D(p(x))   } ⟶ **D è lineare!**

[a voce] (≈ 58:22) «Tutto questo sembra molto complicato», ma «di complicato non c'è niente»: un esempio di questo esempio, con una matrice inventata.
[a voce] (≈ 59:16 – 59:51) ℝ³ perché 3 è il numero di colonne, ℝ² perché 2 è il numero di righe.
[a voce] (≈ 01:01:13 – 01:01:45) Questa mappa è «delle più esplicite che possiamo immaginare»: è proprio della forma detta prima, con componenti che sono combinazioni lineari di x, y e z.
[a voce] (≈ 01:02:53 – 01:03:33) Con A = ( 3 2 ; 1 0 ) si ritrova la prima mappa lineare vista, T( x ; y ) = ( 3x + 2y ; x ): i coefficienti di x e y in ogni componente sono esattamente le righe della matrice.
[a voce] (≈ 01:03:33 – 01:04:48) **Anticipazione** («foreshadowing»): ogni mappa lineare da ℝⁿ a ℝᵐ si può scrivere come moltiplicazione per una matrice; questa non è una classe speciale ma tutte le funzioni lineari. «Lo faremo presto»: parlare di funzioni lineari da ℝⁿ a ℝᵐ o di matrici m × n «è la stessa cosa».
[a voce] (≈ 01:04:48 – 01:06:47) La derivata, vista forse alle superiori, è una mappa lineare: abbassa il grado di 1; x^d diventa d·x^{d−1}, «come se prendesse un d da qua e lo spostasse al coefficiente»; la derivata di x è 1, quella di una costante è 0. Chi non l'ha mai vista prenda questa come definizione.
[a voce] (≈ 01:07:19 – 01:08:36) La derivata sarà vista il semestre dopo, ad Analisi. Le due proprietà (derivata della somma, derivata di una costante per una funzione) sono esattamente le due proprietà di una mappa lineare.

[verifica] 2.1: L_A(x, y, z) = (x + 2z, x + 2y + 4z), L_A(1, 1, 1) = (3, 7). Non calcolato in lezione: rk = 2, Ker L_A = Span((−2, −1, 1)), 1 + 2 = 3. 2.2: det = −2, rk = 2. D: con polinomi generici di grado 3, D(p + q) = D(p) + D(q) e D(λp) = λD(p).

## Nucleo, immagine e prima proposizione (70:00 – 80:00)
**Def:** Sia f : V → W lineare, definiamo
- **NUCLEO** di f, Ker f ⊆ V: Ker f = { v ∈ V | f(v) = 0_W }
- **IMMAGINE** di f, Im f ⊆ W: Im f = { w ∈ W | w = f(v) per un qualche v ∈ V }

**PROP:**
1. f lineare ⟹ Ker f ⊆ V, Im f ⊆ W **sono sottospazi lineari**
2. f è suriettiva ⟺ Im f = W
3. f è iniettiva ⟺ Ker f = {0_V}

**DIM ③.** Supp f iniettiva, e sia v ∈ Ker f
⟹ f(v) = 0_W = f(0_V). Ma f iniettiva ⟹ v = 0 (la fine della riga è tagliata dal bordo del pannello)
Ora, supp che Ker f = {0_V}, e siano v₁, v₂ ∈ V t.c. f(v₁) = f(v₂) ⟹ 0_W = f(v₁) − f(v₂) =(f lin) f(v₁ − v₂)
⟹ v₁ − v₂ ∈ Ker f = {0_V} ⟹ v₁ − v₂ = 0 ⟹ v₁ = v₂ ☒

[a voce] (≈ 01:10:09 – 01:10:42) Il nome Ker viene dall'inglese/tedesco «kernel»; sono i vettori «che vengono uccisi» da f, mandati in zero.
[a voce] (≈ 01:11:20) L'immagine è quella già vista a Matematica discreta: l'insieme dei vettori di W colpiti da qualche elemento di V.
[a voce] (≈ 01:13:42 – 01:14:37) Il punto 2 «quasi non è neanche tanto una proposizione», è la definizione di suriettività e vale per ogni funzione. Il punto 3 dà «una bella nozione di iniettività» e **vale soltanto per le mappe lineari**.
[a voce] (≈ 01:14:37) **Dimostra solo il punto 3**; i punti 1 e 2 non sono dimostrati.
[a voce] (≈ 01:20:27) «Abbiamo fatto una dimostrazione e non è morto nessuno».

## Immagine e generatori, il caso di L_{A} (80:00 – 95:00)
**RICORDIAMO** f : V → W lin
⟹ f(a₁v₁ + … + aₙvₙ) = a₁f(v₁) + … + aₙf(vₙ)
⟹ f(Span(v₁ … vₙ)) = Span(f(v₁) … f(vₙ))
**PROP:** Se v₁ … vₙ ∈ V sono generatori ⟹ Im(f) = Span(f(v₁), …, f(vₙ))

**Nel caso di f = L_A**
**Oss:** A = [ A₁ | … | Aₙ ], x = [ x₁ ; ⋮ ; xₙ ] ∈ 𝕂ⁿ, L_A : 𝕂ⁿ → 𝕂ᵐ
⟹ L_A(x) = Ax = x₁A₁ + x₂A₂ + … + xₙAₙ
In particolare, se x = e_i = [ 0 ; 0 ; 1 ; 0 ] (1 al posto i, indicato con una freccia)
⟹ L_A(e_i) = 0A₁ + 0A₂ + … + 1·A_i + 0A_{i+1} + … + 0Aₙ = A_i

e₁ … eₙ ∈ 𝕂ⁿ base ⟹ generatori
⟹ Im(L_A) = Span(L_A(e₁) … L_A(eₙ)) = Span(A₁ … Aₙ)
⟹ **[ dim Im(L_A) = dim Span(A₁ … Aₙ) = rg A ]** (riquadrato a 95:00)

[a voce] (≈ 01:21:49 – 01:23:13) «Lo metterò sotto forma di proposizione, ma in realtà» è quanto detto all'inizio: f manda combinazioni lineari in combinazioni lineari, quindi lo span di v₁ … vₙ nello span delle immagini.
[a voce] (≈ 01:25:39 – 01:26:48) Osservazione «che forse avrete già fatto» parlando di moltiplicazione di matrici: Ax si scrive come x₁A₁ + … + xₙAₙ, pensando le colonne come vettori.
[a voce] (≈ 01:28:39) In altre parole L_A manda l'i-esimo vettore della base canonica nell'i-esima colonna.
[a voce] (≈ 01:31:45 – 01:32:31) «Domanda per voi: che cos'è questo? Questo è il rango»: per definizione il rango è la dimensione dello span delle colonne.
[a voce] (≈ 01:32:31 – 01:33:07) Il rango di una matrice si può pensare come la dimensione dell'immagine; «uno lo può generalizzare» e dire che il rango di una qualunque mappa lineare è la dimensione della sua immagine.

[verifica] Con una matrice simbolica 3 × 4: A·e_i = A_i per ogni i, e Ax = x₁A₁ + … + x₄A₄ identicamente.

## Teorema della dimensione e corollario (95:00 – 102:30)
**TEOREMA DELLA DIMENSIONE**
f : V → W lineare ⟹ **dim Ker f + dim Im f = dim V**
**COR:** dim Im f ≤ dim V, e inoltre
① dim Im f = dim V ⟺ f iniettiva
② dim Im f = dim W ⟺ f suriettiva

**Dim:** ① dim Im f = dim V ⟺ dim Ker f = 0 ⟺ Ker f = {0} ⟺ f iniettiva
② dim Im f = dim W ⟺ Im f = W ⟺ f suriett. (sotto, con una freccia verso il primo uguale: Im f ⊆ W) ☒

**Il teorema non è dimostrato**: è dimostrato solo il corollario. L'ipotesi «V di dimensione finita» non è scritta.

[a voce] (≈ 01:34:18) I due spazi «non sono indipendenti»: il teorema dice qual è il rapporto tra le loro dimensioni.
[a voce] (≈ 01:35:07) A una domanda di uno studente ripete che cos'è Ker: kernel vuol dire nucleo in inglese.
[a voce] (≈ 01:37:27 – 01:38:04) Questo dà buoni metodi per verificare iniettività o suriettività **«senza andare neanche a toccare la funzione»**, solo con uguaglianze tra numeri interi, e «a volte può essere estremamente utile».
[a voce] (≈ 01:38:04 – 01:38:46) Programma: dare un'idea di come si dimostrano i due punti e mostrare come Rouché-Capelli discenda dal teorema.
[a voce] (≈ 01:40:38 – 01:41:08) Un sottospazio ha la stessa dimensione dello spazio grande se e solo se coincide con esso.

## Il caso di L_{A} e Rouché-Capelli (102:30 – 107:00)
**NEL CASO di L_A**, A ∈ M(m, n, 𝕂)
L_A : 𝕂ⁿ → 𝕂ᵐ
dim Im L_A = rg(A), dim 𝕂ⁿ = n = colonne di A
Ker(L_A) = { x = ( x₁ ; ⋮ ; xₙ ) ∈ 𝕂ⁿ | Ax = 0 } = S₀ = spazio delle soluzioni del sistema (A | 0)
(sotto Ax = 0 il sistema { a₁₁x₁ + … + a₁ₙxₙ = 0 ; ⋮ ; aₘ₁x₁ + … + aₘₙxₙ = 0 })

**Teo della dimensione**
dim Ker L_A + dim Im L_A = dim 𝕂ⁿ
dim S₀ + rg(A) = n ⇝ **dim S₀ = n − rg(A)**, con una graffa sotto e la scritta **Rouché-Capelli** ☒

[a voce] (≈ 01:44:44) Un elemento del nucleo è una soluzione di un sistema omogeneo: il nucleo è lo spazio delle soluzioni del sistema.
[a voce] (≈ 01:46:08 – 01:46:39) La dimensione di S₀ è il numero di colonne di A meno il rango di A: «e questo è Rouché-Capelli».

La lezione finisce qui (≈ 01:46:39 – 01:47:12, «ci vediamo lunedì prossimo»). Non sono svolti esercizi su nucleo e immagine.

[verifica] Per le tre matrici della lezione (2.1, 2.2, quella della pausa) dim Ker + rk = numero di colonne: 1 + 2 = 3, 0 + 2 = 2, 1 + 2 = 3. Ker della matrice della pausa: Span((3/5, −9/5, 1)), cioè Span((3, −9, 5)).

## Controllo dei conti con SymPy
Rifatti con SymPy (calcolo simbolico di L e R, `rank`, `nullspace`, `det`, `diff`). Tutti i risultati scritti alla lavagna sono corretti.
- T( x ; y ) = ( 3x + 2y ; x ): L = R.
- Non esempi: f(0, 0) = (1, 0); (ax, a²y²) ≠ (ax, ay²) per a = 2, y ≠ 0.
- 2.1: (x + 2z, x + 2y + 4z), L_A(1, 1, 1) = (3, 7). 2.2: (3x + 2y, x).
- Pausa: (x + 2y + 3z, 3x + y), L_A(1, 1, 2) = (9, 4).
- Derivata lineare; A·e_i = A_i; Ax = Σ x_iA_i; teorema della dimensione sulle tre matrici.

Errori e correzioni del docente:
- «= L_A(x) + aL_A(x)» senza apice nel secondo argomento (scritto a destra prima del passaggio intermedio; la riga finale «= L_A(x) + aL_A(x′) ✓» è corretta; nessuna conseguenza).
- Nella pausa «L_A : ℝⁿ → 𝕂ᵐ» mescola ℝ e 𝕂 (nessuna conseguenza).
- Nel teorema della dimensione manca l'ipotesi che V abbia dimensione finita (nelle dispense c'è).
- D : 𝕂[x]_d → 𝕂[x]_{d−1}: per d = 0 l'arrivo non ha senso; il docente non lo discute (nessuna conseguenza per l'esempio).

## Punti illeggibili
Nessuna formula è rimasta illeggibile: [illeggibile] non compare. Restano letture incerte, segnalate sopra: l'esponente di y² nella seconda funzione dei non esempi è poco visibile a 32:30 (ma f(0;0) = (0;0²), R e l'audio lo confermano); la fine della riga «Ma f iniettiva ⟹ v = 0», tagliata dal bordo; i simboli (faccina e triangolo) scritti durante la pausa; il vettore (1 ; 1 ; 2) della pausa, la cui componente centrale è piccola (la lettura è confermata dal risultato (9 ; 4)). Il proiettore copre a tratti la parte alta del pannello in alto a sinistra (per esempio la fine di «T( x ; y ) = ( 3x + 2y ; x )» e di «APPLICAZIONE/MAPPA/TRASFORMAZIONE»): ogni parte coperta è stata letta in un altro fotogramma, dopo lo scorrimento del pannello.

## Note sulla trascrizione audio
La trascrizione (`algebra_L14_2024.txt`) è di buona qualità rispetto alla L13: storpiature (vdoppio = W, «Rusce Cappelli», «inettiva», «nuclear», qualche carattere estraneo) ma pochi tratti allucinati. Il tratto 48:26 – 57:48 è vuoto per la pausa. Restano frasi rovinate intorno a 01:14:37 (enunciato sui punti 1-2 della proposizione) e 01:13:09 («Zerdo più è l'elemento netto di V doppio»), dove probabilmente il docente richiama che 0_W sta in Im f. Fidarsi della lavagna per le formule.
