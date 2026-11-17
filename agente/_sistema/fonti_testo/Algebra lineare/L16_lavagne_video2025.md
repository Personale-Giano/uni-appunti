# Algebra lineare, Lezione 16: Applicazioni lineari III (lavagne dalla registrazione Webex del 2025, prof. Radeschi)

Fonte: video della registrazione Webex del 5 nov 2025, file `audio/algebra_L16_2025.mp4` (90 min 13 s, 1920×1080), trascrizione `trascrizioni/algebra_L16_2025.txt`. **La pausa è tagliata dal video**: a ≈ 48:22 il docente dice «manca un minuto all'inizio della pausa, ci fermiamo qua» e nella stessa riga della trascrizione riprende con «prima della pausa abbiamo definito…»; il fotogramma di 48:40 ha ancora le lavagne piene, quello di 49:00 le ha già tutte cancellate, con il riepilogo scritto in alto a sinistra. Non mancano altri pezzi: il video comincia con il titolo e finisce con i saluti (≈ 01:29:20).
Fotogrammi estratti ogni 20 s (271, da 00:00 a 90:00), in una cartella temporanea. La lavagna è in 4 pannelli scorrevoli (alto/basso, sinistra/destra). Sono stati aperti uno per ogni stato della lavagna, circa uno ogni 2-3 minuti (02:30, 04:40, 05:00, 06:40, 07:30, 09:40, 10:00, 11:40, 12:30, 14:20, 15:00, 17:30, 19:00, 20:00, 22:20, 22:30, 24:20, 25:00, 27:30, 30:00, 31:40, 32:30, 35:00, 36:00, 37:00, 37:30, 38:40, 40:00, 41:20, 42:30, 43:40, 45:00, 46:20, 47:30, 48:20, 48:40, 49:00, 49:20, 49:40, 50:00, 50:20, 51:00, 51:40, 52:30, 53:20, 54:20, 55:00, 55:20, 56:40, 57:30, 59:00, 60:00, 61:40, 62:30, 64:40, 65:00, 66:40, 67:30, 68:20, 69:20, 70:00, 71:40, 72:30, 73:40, 75:00, 76:00, 77:20, 77:30, 78:20, 79:00, 79:40, 80:00, 82:30, 83:20, 84:20, 85:00, 86:00, 86:40, 87:30, 88:20, 89:00, 89:40, 90:00), alcuni interi, altri come ritagli ingranditi dei pannelli con scritte piccole, altri ancora in tavole di 4 fotogrammi ridotti usate per controllare i momenti intermedi, controllando che ogni pannello fosse letto completo prima di essere cancellato o fatto scorrere.

Convenzioni (come per L14 e L15):
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss); coincidono con quelli dell'audio, perché la pausa è tagliata sia nel video sia nell'audio.
- **[a voce]** indica ciò che è solo detto e non scritto; tra parentesi il tempo dell'audio.
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali: la trascrizione automatica è piena di errori («base caronica / calorica / tanurica» = base canonica, «a primo / aprimo / apporimo» = A′, «via Vodopio» = da V a W, «endomorphismo»).
- Sulla lavagna le basi sono scritte con lettere corsive 𝒜, 𝒜′, ℬ, ℬ′, 𝒞; qui sono rese A, A′, B, B′, C. **Attenzione:** nella seconda metà le lettere A, B indicano a volte basi e a volte matrici (è segnalato dove serve).
- L'identità è scritta I_V (I_W per W). La matrice associata è [f]^A_B: **base di partenza in alto, base di arrivo in basso**. Le matrici numeriche sono scritte a volte con parentesi tonde e a volte quadre («in modo assolutamente casuale», dice il docente a ≈ 27:34); qui «( a b ; c d )» indica la matrice con righe (a b) e (c d), e «( a ; b )» il vettore colonna.

## Titolo e richiamo (00:00 – 04:00)
**LEZIONE 16: APPLICAZIONI LINEARI, III**
**Prev.**
· V sp. vettoriale, B = {v₁, …, vₙ} base
⇝ V ⟶ 𝕂ⁿ, v ⟼ [v]_B = ( a₁ ; ⋮ ; aₙ ) ← **VETTORE DELLE COORDINATE**, dove v = a₁v₁ + … + aₙvₙ.
· f : V → W lineare, A = {v₁, …, vₙ} ⊆ V, B = {w₁, …, wₘ} ⊆ W basi
⟹ [f]^A_B = ( [f(v₁)]_B | … | [f(vₙ)]_B ) ∈ M(m, n, 𝕂)
(una riga orizzontale) **Tali che** ① **[f(v)]_B = [f]^A_B · [v]_A** (riquadrato) ② L_A : 𝕂ⁿ → 𝕂ᵐ ⟹ [L_A]^{Canonica}_{Canonica} = A

[a voce] (≈ 00:07 – 02:23) Richiamo della volta scorsa: dato uno spazio vettoriale e una base, ogni vettore si traduce nel vettore colonna delle sue coordinate; data un'applicazione lineare e una scelta di basi in V e in W, le si associa la matrice associata, che «contiene tutta l'informazione di f». Due proprietà: ① permette di calcolare f come moltiplicazione matrice per vettore; ② per la moltiplicazione a sinistra L_A la matrice associata dalla base canonica alla base canonica è A stessa. In questo senso l'associazione «mappa lineare ⟼ matrice associata» è l'inversa di quella «matrice A ⟼ mappa L_A».
[a voce] (≈ 02:55 – 03:32) Il punto di oggi: sia la matrice associata sia il vettore delle coordinate **dipendono dalla scelta delle basi**. Quanto la scelta di una base influenza questi oggetti?

## La domanda e il disegno delle due persone (04:00 – 10:00)
**Q:** Date basi A, A′ ⊆ V, come differiscono [v]_A e [v]_A′?

Disegno (pannello sotto il titolo, poi fatto scorrere in alto):
- al centro la lettera V e un sistema di frecce che partono dallo stesso punto: v₁ orizzontale verso destra, v₂ verticale verso l'alto, il vettore v in diagonale verso l'alto a destra; lungo la stessa diagonale di v è segnato v₁′ (v₁′ coincide con v), e una freccia più corta v₂′ che punta in alto a sinistra;
- a sinistra un omino stilizzato con un fumetto: «A = {v₁, v₂}; v = v₁ + v₂ ⇝ [v]_B = ( 1 ; 1 )» (sulla lavagna il pedice è scritto B; dal contesto è la base A della prima persona);
- a destra un secondo omino con un fumetto: «A′ = {v₁′, v₂′}; v = v₁′ + 0·v₂′; [v]_B′ = ( 1 ; 0 )» (pedice scritto B′; dal contesto è la base A′).

[a voce] (≈ 04:26 – 05:40) Uno spazio vettoriale «non ha inizialmente nessuna coordinata». Persone diverse che guardano lo stesso spazio e vogliono comunicarsi un vettore scelgono ciascuna una base.
[a voce] (≈ 05:40 – 07:53) Per la prima persona il vettore è v₁ + v₂, quindi ha coordinate (1, 1); per la seconda lo stesso vettore è 1·v₁′ + 0·v₂′, quindi ha coordinate (1, 0). Stesso vettore, coordinate diverse. La domanda è come stabilire un metodo per tradurre le coordinate della prima persona in quelle della seconda.
[a voce] (≈ 07:53 – 09:39) «Piccola storia»: una sonda che doveva orbitare intorno a Marte («nel 1998, il Mars Orbiter») finì per schiantarsi perché due gruppi che collaboravano si passavano distanze in unità diverse (miglia e chilometri) senza convertirle: «non hanno effettuato il cambio di base», e una conversione tra unità «è letteralmente un cambio di base»; perdita di circa 300 milioni di dollari. «Evitiamo di fare lo stesso errore.» (Nota: il docente parla di agenzia americana ed europea; storicamente è il Mars Climate Orbiter, perso nel settembre 1999, e l'errore di unità fu tra la NASA e il costruttore Lockheed Martin. È solo un aneddoto, non materia d'esame.)

## Matrice del cambio di base (10:00 – 14:00)
Data V sp. vettoriale e A, A′ basi di V
chiamiamo **[I_V]^A_A′** la **MATRICE DEL CAMBIO DI BASE, DA A A A′**
**Osserviamo:** ∀v ∈ V
[v]_A′ = [I_V(v)]_A′ =(①) [I_V]^A_A′ · [v]_A
(sotto [I_V]^A_A′ una graffa: «Matrice cambio di base»; sopra l'uguale il numero ① cerchiato, cioè la proprietà ① del richiamo)

[a voce] (≈ 10:38) I_V è la mappa da V in V che manda ogni vettore in se stesso; se ne prende la matrice associata dalla base A alla base A′.
[a voce] (≈ 11:22 – 13:36) Perché si chiama così: è una versione speciale della proprietà ①, che vale sempre. Il vettore v si può scrivere come I_V(v), e la proprietà ① dà la formula. **Come sottolineato a lezione:** date due basi diverse, i vettori delle coordinate rispetto ad A′ e rispetto ad A «differiscono per la moltiplicazione per una matrice»; una volta nota questa matrice si traduce ogni vettore di coordinate in A nel vettore di coordinate in A′. È la risposta alla domanda Q.
[a voce] (≈ 13:36) «Capire come passare da una base all'altra è parecchio importante», quindi è importante saper calcolare queste matrici.

## Esempio in ℝ²: dalla base canonica ad A′ (14:00 – 23:20)
**Es:** V = ℝ², A = { e₁ = ( 1 ; 0 ), e₂ = ( 0 ; 1 ) }, A′ = { w₁ = ( 1 ; 1 ), w₂ = ( 1 ; 2 ) }
calcoliamo [I_V]^A_A′ = [ [I_V e₁]_A′ | [I_V e₂]_A′ ] = [ [e₁]_A′ , [e₂]_A′ ]

[e₁]_A′ = ( a ; b ) dove e₁ = a w₁ + b w₂
(sotto e₁, con una freccia) ( 1 ; 0 ) = a·( 1 ; 1 ) + b·( 1 ; 2 ) = ( a + b ; a + 2b ) ⇝ { a + b = 1 ; a + 2b = 0 }
{ b = −1 ; a = 2 } ⇝ [e₁]_A′ = ( 2 ; −1 ) ⇝ [I_V]^A_A′ = [ 2 ? ; −1 ? ]
(a 20:00 erano scritti [e₁]_A′ = ( −1 ; 2 ) e la prima colonna ( −1 ; 2 ), con a e b scambiati; corretto in ( 2 ; −1 ) su segnalazione di uno studente, a 22:20 è già giusto. I due punti interrogativi nella seconda colonna restano sulla lavagna.)

[e₂]_A′ = ( a ; b ) dove e₂ = a·w₁ + b w₂
(sotto e₂, con una freccia) ( 0 ; 1 ) = a ( 1 ; 1 ) + b ( 1 ; 2 ) = ( a + b ; a + 2b )
⇝ { a + b = 0 ; a + 2b = 1 }  b = 1, a = −1 ⟶ [e₂]_A′ = ( −1 ; 1 ) ⇝ **[I_V]^A_A′ = [ 2 −1 ; −1 1 ]**

[a voce] (≈ 14:58 – 16:15) La matrice del cambio di base ha tante colonne quanti sono gli elementi della base di partenza. Per ogni colonna: si prende un elemento della base di partenza, gli si applica la funzione (qui l'identità, quindi resta lui stesso) e se ne calcola il vettore delle coordinate nella base di arrivo.
[a voce] (≈ 18:43) «In generale ci troveremo davanti un sistema»: il docente ci tiene che i sistemi si risolvano «in maniera strutturata, usando metodi che funzionano»; questo è talmente piccolo che si fa a mano (seconda equazione meno la prima: b = −1; poi a = 2).
[a voce] (≈ 19:46 – 20:26) Scrive la colonna (−1, 2), uno studente lo corregge; «ovviamente questi non sono errori, sono solo dei modi per testare che state attenti».
[a voce] (≈ 21:35) Per la seconda colonna il membro di destra è lo stesso di prima, ( a + b ; a + 2b ); cambia solo il vettore a cui deve essere uguale.

[verifica] Con SymPy: e₁ = a w₁ + b w₂ ⟺ (a, b) = (2, −1); e₂ = a w₁ + b w₂ ⟺ (a, b) = (−1, 1). La matrice finale ( 2 −1 ; −1 1 ) è corretta.

## A cosa serve: le coordinate di (3, 7) nella base A′ (23:20 – 28:40)
(pannello di destra, in basso) Data [I_V]^A_A′ appena trovata, calcolare [( 3 ; 7 )]_A′

**RICORDIAMO** Per la base canonica A, [v]_A = v
⇝ [( 3 ; 7 )]_A = ( 3 ; 7 ) ⇝ [( 3 ; 7 )]_A′ = [I_V]^A_A′ · [( 3 ; 7 )]_A
= [ 2 −1 ; −1 1 ] · [ 3 ; 7 ] = ( −1 ; 4 )
⟶ ( 3 ; 7 ) = −w₁ + 4w₂

[a voce] (≈ 23:22) La matrice del cambio di base è quella che permette di convertire ogni vettore scritto in coordinate rispetto ad A nel vettore scritto in coordinate rispetto ad A′.
[a voce] (≈ 24:24 – 25:34) **Come sottolineato a lezione** («assolutamente da ricordare», «sarà estremamente utile anche in seguito»): la base canonica ha una proprietà molto speciale, che vale **solo** per lei: le coordinate di un vettore rispetto alla base canonica sono le entrate del vettore stesso.
[a voce] (≈ 26:12) Il docente si accorge di aver cancellato la formula [v]_A′ = [I_V]^A_A′ [v]_A e la ripete.
[a voce] (≈ 26:56) Il prodotto: 6 − 7 = −1 e −3 + 7 = 4.
[a voce] (≈ 28:09) Significato: (3, 7) è −1 volta il primo vettore di A′ più 4 volte il secondo; «uno può andare a controllare».

[verifica] ( 2 −1 ; −1 1 )·(3, 7) = (−1, 4); −w₁ + 4w₂ = (−1 + 4, −1 + 8) = (3, 7). ✓

## Osservazione importante: quando la base di arrivo è la canonica (28:40 – 34:30)
**OSSERVAZIONE IMPORTANTE:**
V = 𝕂ⁿ, con basi A = {v₁, …, vₙ}, C = {e₁, …, eₙ} ← CANONICA
[I_V]^A_C = [ [v₁]_C … [vₙ]_C ] = [ v₁ | … | vₙ ]
**Es.** Esempio precedente, [I_V]^A′_A = [ w₁ | w₂ ] = [ 1 1 ; 1 2 ]

[a voce] (≈ 28:42 – 29:56) Nell'esempio la base di **partenza** era la canonica, ma questo non ha semplificato i conti. Invece i conti «si semplificano drasticamente» quando è la base di **arrivo** a essere la canonica: «vi consiglio di ricordarla, perché semplifica i conti in maniera infinita».
[a voce] (≈ 31:13 – 32:21) Fin qui è solo la definizione; ma se la base di arrivo è la canonica, il vettore delle coordinate di un vettore è il vettore stesso. Quindi per la matrice del cambio di base **da una base qualunque alla canonica** basta prendere i vettori della base di partenza e metterli in colonna.
[a voce] (≈ 32:21 – 32:54) Obiezione possibile: quando mai capita un cambio da una base a caso alla canonica? Nel corso della lezione si vedranno modi per ricondursi a questa situazione anche nel caso più generale.
[a voce] (≈ 33:32 – 34:06) Nell'esempio precedente, la matrice da A′ alla canonica sarebbe stata immediata: w₁ e w₂ in colonna. Ma l'esercizio chiedeva l'altra (dalla canonica ad A′): per questo serve la proposizione che segue.

## L'inversa della matrice del cambio di base (34:30 – 39:00)
**PROP:** V sp vett, basi A, A′ ⟹ [I_V]^A_A′ è invertibile, e
( [I_V]^A_A′ )⁻¹ = [I_V]^A′_A
**Es:** Nell'esempio precedente,
[I_V]^A_A′ = ( [I_V]^A′_A )⁻¹ = ( [ 1 1 ; 1 2 ] )⁻¹ = (1/1) · [ 2 −1 ; −1 1 ]
(sopra la A in alto di [I_V]^A_A′ una freccia con scritto «canonica»; la matrice finale è sottolineata)

[a voce] (≈ 34:42 – 35:56) L'inversa della matrice del cambio di base da A ad A′ è la matrice del cambio di base «al contrario», da A′ ad A. Vale «sempre, sempre» (risposta a una domanda). Nessuna dimostrazione.
[a voce] (≈ 37:05 – 37:37) Richiamo: l'inversa di una matrice 2 × 2 è 1 diviso il determinante, per la matrice che si ottiene scambiando gli elementi sulla diagonale principale e cambiando segno a quelli sulla diagonale secondaria. Il risultato «è esattamente la matrice che avevamo calcolato».
[a voce] (≈ 38:09 – 38:42) Onestamente: con matrici 2 × 2 è velocissimo, con 3 × 3 bisogna invertire una matrice 3 × 3 ed è più laborioso; ma anche l'altro metodo (i sistemi) si complica, e «dei due secondo me questo rimane un pochettino più veloce». **Consiglio:** per un cambio di base dalla canonica a un'altra base può convenire agire così (scrivere la matrice facile e invertirla).
[a voce] (≈ 38:42 – 39:21) Fine della prima parte: le coordinate di un vettore rispetto a due basi sono legate dalla moltiplicazione per una matrice, la matrice del cambio di base.

[verifica] det ( 1 1 ; 1 2 ) = 1; ( 1 1 ; 1 2 )⁻¹ = ( 2 −1 ; −1 1 ), uguale alla matrice trovata con i due sistemi. ✓

## Seconda domanda e composizione di funzioni lineari (39:00 – 48:20)
**Q:** f : V → W lineare, A, A′ ⊆ V, B, B′ ⊆ W basi
(una freccia ondulata da f verso il basso) [f]^A_B , [f]^A′_B′ come sono legate tra loro?

**COMPOSIZIONE DI FUNZ. LINEARI**
V —f→ W —g→ U ⇝ V —g∘f→ U
(g∘f)(v) = g(f(v))
**PROP.** se f, g sono lineari ⟹ lo è anche g∘f
**PROP.** A ∈ M(m, n, 𝕂), B ∈ M(n, p, 𝕂) ⇝ AB ∈ M(m, p, 𝕂)
𝕂ᵖ —L_B→ 𝕂ⁿ —L_A→ 𝕂ᵐ    𝕂ᵖ —L_AB→ 𝕂ᵐ
(frecce ondulate collegano A a L_A, B a L_B e AB a L_AB)
Allora **L_AB = L_A ∘ L_B**
**Dim:** v ∈ 𝕂ᵖ ⇝ L_AB(v) = (AB)·v = A·(Bv) = L_A(Bv) = L_A(L_B(v)) ☒

[a voce] (≈ 40:34 – 41:08) Le due matrici sono associate alla stessa mappa, viste in basi diverse: «un qualche legame ci deve essere», perché entrambe sono traduzioni della stessa mappa e le proprietà della mappa devono scendere in proprietà delle matrici; «non possono essere due matrici a caso». Per capirlo serve la composizione.
[a voce] (≈ 41:38 – 42:16) La composizione è quella di Matematica discreta: prima f, poi g.
[a voce] (≈ 43:01) Nessuna dimostrazione che g∘f è lineare.
[a voce] (≈ 43:47 – 44:18) Si possono moltiplicare A e B perché il numero di colonne di A è uguale al numero di righe di B; AB ha tante righe quante A e tante colonne quante B.
[a voce] (≈ 45:55 – 46:34) **Come sottolineato a lezione:** questo risultato spiega perché la moltiplicazione tra matrici è definita nel modo in cui è definita. Presa da sola la definizione «sembra estremamente arbitraria»; diventa naturale quando si pensa a una matrice come alla mappa lineare che prende un vettore e lo moltiplica per la matrice: il prodotto di matrici è la composizione delle mappe corrispondenti.
[a voce] (≈ 46:34 – 47:50) «La dimostrazione è una riga, quindi la faccio»: si usa l'associatività del prodotto tra matrici.
[a voce] (≈ 48:22) «Manca un minuto all'inizio della pausa, ci fermiamo qua.» (Pausa tagliata.)

[verifica] A(Bv) = (AB)v (associatività): controllato in SymPy con le matrici 2 × 2 della lezione, ( 1 2 ; 2 1 ) e ( 1 1 ; 1 2 ), e un vettore simbolico (x, y).

## Dopo la pausa: riepilogo (49:00 – 50:10)
(pannello in alto a sinistra, tutte le altre lavagne cancellate)
· V sp vett, A = {v₁, …, vₙ}, A′ = {v₁′, …, vₙ′} basi
⇝ [I_V]^A_A′ = [ [v₁]_A′ … [vₙ]_A′ ] tc ∀v ∈ V, [v]_A′ = [I_V]^A_A′ [v]_A
· Se A′ = canonica, [I_V]^A_A′ = [ v₁ | … | vₙ ]
· ( [I_V]^A_A′ )⁻¹ = [I_V]^A′_A
(una riga orizzontale)
· L_A ∘ L_B = L_AB

[a voce] (≈ 48:22 – 49:29) Riassunto di prima della pausa: la matrice del cambio di base dà le coordinate di un vettore rispetto ad A′ sapendo quelle rispetto ad A; si è visto come calcolarla in alcuni casi.
[a voce] (≈ 49:29 – 50:12) Nella corrispondenza tra matrici e applicazioni lineari il prodotto di matrici diventa composizione; ora si fa «un passo oltre»: anche nel passaggio inverso, da applicazioni lineari a matrici, la composizione diventa moltiplicazione.

## La matrice associata a una composizione (50:10 – 55:40)
**PROP** V, W, U sp vett su 𝕂, A ⊆ V, B ⊆ W, C ⊆ U basi
V —f→ W —g→ U lineari (sotto V, W, U sono scritte le basi A, B, C)   V —g∘f→ U (sotto: A e C)
⟹ **[g∘f]^A_C = [g]^B_C · [f]^A_B**
(sotto, una riga orizzontale)

Diagramma (pannello in basso a destra, poi fatto scorrere in alto):
riga in alto: V —f→ W —g→ U, con un arco sopra da V a U etichettato g∘f; sotto V, W, U le basi A, B, C;
una linea orizzontale di separazione, attraversata da frecce ondulate verticali che scendono da V, da f, da W e da U;
riga in basso: 𝕂ⁿ —L_A→ 𝕂ᵐ —L_B→ 𝕂ᵖ, con un arco sotto da 𝕂ⁿ a 𝕂ᵖ etichettato L_BA (la scritta ha una correzione: una lettera cancellata prima di «BA»);
sotto: A = [f]^A_B   B = [g]^B_C
(**attenzione alle lettere:** a sinistra dell'uguale A e B sono le due **matrici**; negli indici A, B, C sono le **basi**. Con queste matrici la formula della Prop si legge [g∘f]^A_C = B·A.)
A destra del diagramma una riga verticale che divide in due il pannello.

[a voce] (≈ 52:09 – 52:40) **Come sottolineato a lezione** (qualcuno gli aveva scritto che in altri libri la notazione è diversa, con le basi sotto/sopra scambiate o in altro modo): la scelta di mettere la base di partenza sopra e quella di arrivo sotto **aiuta a ricordare questa formula**, perché nel prodotto [g]^B_C · [f]^A_B è «come se stessimo cancellando la base B»: la B in alto del primo fattore con la B in basso del secondo, e restano A sopra e C sotto.
[a voce] (≈ 52:40 – 55:07) Ripresa del parallelo «teoria / calcoli» della volta scorsa: una base associa a ogni spazio vettoriale astratto uno spazio concreto di vettori colonna, e a ogni mappa lineare la sua matrice associata. In questa corrispondenza le composizioni sopra vanno a finire in moltiplicazioni sotto: g∘f va a finire nella moltiplicazione per BA. «Se questo discorso vi aiuta a fissare il concetto, bene; se non vi aiuta, dimenticatelo.»
[a voce] Nessuna dimostrazione della Prop.

## Osservazione: cambio di base tra due basi non canoniche (55:40 – 64:00)
**Oss:** V = 𝕂ⁿ, B, B′ basi    V —I_V→ V —I_V→ V (sotto i tre V: B, C, B′; sotto C una freccia con scritto «canonica»)
[I_V]^B_B′
‖
[I_V ∘ I_V]^B_B′ = [I_V]^C_B′ · [I_V]^B_C = ( [I_V]^B′_C )⁻¹ · [I_V]^B_C
(sotto [I_V]^B′_C e sotto [I_V]^B_C una graffa con scritto «facile»; [I_V]^B_C ha una graffa anche nel passaggio precedente)

**Es.** ℝ², B = { ( 1 ; 1 ), ( 1 ; 2 ) }, B′ = { ( 0 ; 1 ), ( −1 ; 3 ) }. Calcolare [I_V]^B_B′
[I_V]^B_B′ = ( [I_V]^B′_C )⁻¹ · [I_V]^B_C = ( [ 0 −1 ; 1 3 ] )⁻¹ · [ 1 1 ; 1 2 ] = [ 3 1 ; −1 0 ] · [ 1 1 ; 1 2 ]
(il risultato è scritto nel pannello sotto, a destra della riga verticale, dopo una freccia) ↳ **[ 4 5 ; −1 −1 ]**

[a voce] (≈ 55:48 – 57:02) Si sa già che se la base di arrivo è la canonica la matrice è immediata, e se è la base di partenza a essere canonica «è quasi facile» (è l'inversa di una matrice facile). E se **nessuna delle due** è canonica? Ci si riconduce al caso di prima.
[a voce] (≈ 57:02 – 58:06) L'identità composta con l'identità è ancora l'identità; nel mezzo si sceglie la base canonica C, così I_V da B a B′ è la composizione di I_V da B a C con I_V da C a B′.
[a voce] (≈ 58:52 – 59:34) Il fattore [I_V]^B_C è facile (vettori di B in colonna); l'altro, [I_V]^C_B′, si scrive come l'inversa di [I_V]^B′_C, che è facile.
[a voce] (≈ 01:00:23 – 01:00:54) A una domanda: la base in mezzo è scelta dal docente, ed è la canonica apposta; con un'altra scelta la formula varrebbe lo stesso ma non aiuterebbe.
[a voce] (≈ 01:02:48 – 01:03:24) L'inversa: determinante 0 − (−1) = 1; poi il prodotto: 3·1 + 1·1 = 4, 3·1 + 1·2 = 5, −1 + 0 = −1, −1 + 0 = −1.

[verifica] ( 0 −1 ; 1 3 )⁻¹ = ( 3 1 ; −1 0 ) (det = 1); ( 3 1 ; −1 0 )·( 1 1 ; 1 2 ) = ( 4 5 ; −1 −1 ). Controllo diretto del significato: 4·(0, 1) − 1·(−1, 3) = (1, 1) e 5·(0, 1) − 1·(−1, 3) = (1, 2), cioè le colonne sono le coordinate dei vettori di B nella base B′. ✓

## Osservazione 2 e formula del cambio di base per una mappa (64:00 – 71:20)
**Oss 2:** V —f→ W   A, A′ ⊆ V, B, B′ ⊆ W
V —I_V→ V —f→ W —I_W→ W (sotto i quattro spazi le basi: A′, A, B, B′; sotto ancora, il percorso di un vettore: v ⟼ v ⟼ f(v) ⟼ f(v))
(a 66:40 è scritto «f = I_W ∘ f ∘ I_V», poi inglobato nella riga seguente)
**[f]^A′_B′** = [I_W ∘ f ∘ I_V]^A′_B′ = [I_W]^B_B′ · **[f]^A_B** · [I_V]^A′_A
(i due [f] sono cerchiati; sotto l'ultimo fattore, con un segno di uguale verticale: ( [I_V]^A_A′ )⁻¹)
**RIASSUMENDO:** (resta solo la parola; il riassunto è la Prop scritta nel pannello di destra)

**PROP:** V —f→ W, A, A′ ⊆ V, B, B′ ⊆ W
P = [I_V]^A_A′   Q = [I_W]^B_B′   cambi di base
⟹ **[f]^A′_B′ = Q · [f]^A_B · P⁻¹**
(sotto, una riga orizzontale)

[a voce] (≈ 01:03:59) «Finalmente quello che volevamo»: è la risposta alla seconda domanda Q.
[a voce] (≈ 01:05:32 – 01:06:09) La composizione I_W ∘ f ∘ I_V manda v in v, poi in f(v), poi in f(v): è ancora f. Ma le basi lungo il percorso sono A′, A, B, B′.
[a voce] (≈ 01:06:55 – 01:08:09) Una composizione di funzioni diventa un prodotto di matrici. **Come sottolineato a lezione:** le due matrici che interessano sono legate tra loro da moltiplicazioni per le matrici del cambio di base.
[a voce] (≈ 01:10:20 – 01:10:57) A una domanda: nella formula compariva la matrice del cambio di base da A′ ad A; si riscrive come inversa di quella da A ad A′ (formula di prima: scambiando l'ordine delle due basi si prende l'inversa), perché di solito interessa sapere come si passa «dalle basi vecchie alle basi nuove», e ha più senso scrivere così che viceversa.
[a voce] Nessun'altra dimostrazione oltre al conto dell'Oss 2.

## Esempio: [L_A]^B_B (71:20 – 78:40)
**Es.** A = ( 1 2 ; 2 1 ) ∈ M(2, 2, ℝ) ⇝ L_A : ℝ² → ℝ²
B = { ( 1 ; 1 ), ( 1 ; 2 ) }   Calcolare [L_A]^B_B
Ricordiamo che se C = { ( 1 ; 0 ), ( 0 ; 1 ) } è la base canonica,
allora [L_A]^C_C = A
⟹ [L_A]^B_B = [I]^C_B · [L_A]^C_C · [I]^B_C = ( [I]^B_C )⁻¹ · [L_A]^C_C · [I]^B_C
(alcuni indici C sono ripassati sopra una lettera precedente: il docente dice di aver chiamato per sbaglio «A» la base canonica e di averla corretta in C)
(pannello in basso a sinistra)
[L_A]^B_B = [ 1 1 ; 1 2 ]⁻¹ · [ 1 2 ; 2 1 ] · [ 1 1 ; 1 2 ] =
= [ 2 −1 ; −1 1 ] · [ 3 5 ; 3 4 ] = **[ 3 6 ; 0 −1 ]** (sottolineato)

(qui A è la **matrice** e B è la **base**.)

[a voce] (≈ 01:12:51 – 01:13:26) Perché questo tipo di problema è importante: per le mappe da uno spazio in se stesso spesso ci sono **basi speciali**, non necessariamente la canonica, che fanno capire particolarmente bene come funziona la mappa; ci saranno direzioni speciali, gli **autovettori**, lungo le quali la mappa è particolarmente semplice. (Anticipo della lezione 17.)
[a voce] (≈ 01:15:33 – 01:16:53) Tre cose rendono il conto facile: [L_A]^C_C è la matrice di partenza A; [I]^B_C ha la canonica come base di arrivo (vettori di B in colonna); [I]^C_B ha la canonica come base di partenza, quindi è l'inversa della precedente.
[a voce] (≈ 01:17:36) L'inversa di ( 1 1 ; 1 2 ) «l'avevamo calcolata»: ( 2 −1 ; −1 1 ). Poi prima il prodotto A·( 1 1 ; 1 2 ) = ( 3 5 ; 3 4 ), poi 6 − 3 = 3, 10 − 4 = 6, −3 + 3 = 0, −5 + 4 = −1.

[verifica] ( 1 2 ; 2 1 )·( 1 1 ; 1 2 ) = ( 3 5 ; 3 4 ); ( 2 −1 ; −1 1 )·( 3 5 ; 3 4 ) = ( 3 6 ; 0 −1 ). Controllo diretto: A·(1, 1) = (3, 3) = 3·(1, 1) + 0·(1, 2) e A·(1, 2) = (5, 4) = 6·(1, 1) − 1·(1, 2). ✓

## Endomorfismi e matrici simili (78:40 – 90:13)
(pannello a sinistra, sotto una riga orizzontale)
**ENDOMORFISMI**
Un **endomorfismo** (sottolineato) è una mappa lineare V —f→ V (sotto i due V la stessa base B)
se B ⊆ V ⇝ [f]^B_B   | Se B′ è un'altra base, qual è il rapporto tra [f]^B_B e [f]^B′_B′? (la domanda è poi delimitata da una riga ad angolo)

(pannello a destra, in alto)
Nella prop sopra, prendendo V = W, A = B, A′ = B′
⇝ P = Q, per cui
**[f]^B′_B′ = P · [f]^B_B · P⁻¹** (riquadrato; i due [f] sottolineati)   dove P = [I_V]^B_B′
Diremo che A, B ∈ M(n) sono **SIMILI** se
B = P A P⁻¹ per una qualche P ∈ M(n) invertibile
(qui A, B sono di nuovo **matrici**.)

(pannello a destra, in basso)
**PROP.** se A, B sono simili, allora:
① det A = det B
② tr A = tr B
③ rg(A) = rg(B)

[a voce] (≈ 01:19:50 – 01:21:05) Gli endomorfismi si possono pensare «in maniera dinamica», come trasformazioni di uno spazio in se stesso. Esempi detti a voce: V è lo spazio degli stati di un sistema (le posizioni di un braccio meccanico, la distribuzione di persone o di nuvole in una regione); a ogni istante lo stato cambia attraverso una trasformazione, ed è importante sapere cosa succede applicando la stessa trasformazione più e più volte, cioè sul lungo periodo.
[a voce] (≈ 01:21:05 – 01:21:35) Sono le mappe di cui si studieranno le proprietà dalla settimana prossima, attraverso **autovalori e autovettori**.
[a voce] (≈ 01:21:35 – 01:22:06) Per un endomorfismo spazio di partenza e di arrivo coincidono, quindi ha senso mettere la stessa base in partenza e in arrivo.
[a voce] (≈ 01:22:40 – 01:25:26) La risposta è un caso speciale della proposizione generale: con V = W, A = B e A′ = B′ le matrici P e Q sono la stessa.
[a voce] (≈ 01:25:26 – 01:26:33) La relazione è abbastanza speciale da meritare un nome: **similitudine**. Due matrici quadrate sono simili se una si ottiene dall'altra moltiplicando per una matrice invertibile P da una parte e per P⁻¹ dall'altra.
[a voce] (≈ 01:27:04 – 01:28:43) **Come sottolineato a lezione:** due matrici simili, «anche se in apparenza diverse», condividono tutta una serie di proprietà (determinante, traccia, rango), che dicono «non tanto qual è l'aspetto delle matrici ma qual è il loro comportamento». Non deve sorprendere: sono due rappresentazioni della stessa mappa, e le proprietà della mappa devono ritrovarsi nelle matrici associate.
[a voce] (≈ 01:28:43 – 01:29:20) «Direi che possiamo saltare le dimostrazioni.» Fine della lezione. Avviso: venerdì c'è lezione, il lunedì successivo no.

[verifica] Sull'esempio della lezione, A = ( 1 2 ; 2 1 ) e ( 3 6 ; 0 −1 ) sono simili (sono [L_A]^C_C e [L_A]^B_B): det = −3 per entrambe, traccia = 2 per entrambe, rango = 2 per entrambe. ✓

Non sono svolti alla lavagna: la dimostrazione della formula della composizione, la dimostrazione dell'invertibilità della matrice del cambio di base, le dimostrazioni sulle matrici simili; nessun esempio 3 × 3.

## Confronto con le dispense (sezione 16)
Solo alla lavagna (non nelle dispense):
- il disegno delle due persone con le due basi e l'aneddoto della sonda;
- l'esempio 2 × 2 con A′ = {(1, 1), (1, 2)}, svolto in due modi (i due sistemi; l'inversa della matrice «facile»), e il calcolo di [(3, 7)]_A′ = (−1, 4);
- l'«osservazione importante» scritta in modo esplicito ([I_V]^A_C = [v₁ | … | vₙ] se C è canonica) e l'Oss. sul cambio tra due basi non canoniche passando per la canonica, [I_V]^B_B′ = ([I_V]^B′_C)⁻¹ [I_V]^B_C, con l'esempio che dà ( 4 5 ; −1 −1 );
- il diagramma teoria/calcoli per la composizione;
- l'esempio [L_A]^B_B con A = ( 1 2 ; 2 1 ), risultato ( 3 6 ; 0 −1 );
- la proprietà **tr A = tr B** per matrici simili (le dispense, Prop. 16.13, hanno solo rango e determinante).

Solo nelle dispense (non alla lavagna):
- Esercizio 16.3, l'esempio 3 × 3 con w₁ = (1, 2, 3), w₂ = (0, 2, 1), w₃ = (0, 1, 1) (stessa idea dei due metodi);
- la dimostrazione della Prop. 16.6 (matrice della composizione);
- il Corollario 16.7: f è un isomorfismo ⟺ [f]^B_C è invertibile, e l'inversa è [f⁻¹]^C_B (alla lavagna c'è solo il caso dell'identità);
- per gli endomorfismi, [f∘g]^B_B = [f]^B_B [g]^B_B; l'Esempio 16.10 (f(x, y) = (x + y, −y), che nella base {(1, 0), (−1, 2)} diventa ( 1 0 ; 0 −1 ));
- la notazione A ∼ B, il nome «coniugate», la Prop. 16.12 (la similitudine è una relazione di equivalenza), «A invertibile ⟺ B invertibile» e la spiegazione con Binet della Prop. 16.13;
- l'Esercizio 16.14.

Differenze di notazione e di convenzione:
- dispense: identità «id», basi B e C, matrice del cambio di base [id]^B_C; lavagna: I_V, basi A e A′, [I_V]^A_A′.
- Prop. L_A∘L_B = L_AB: dispense con A ∈ M(k, m), B ∈ M(m, n); lavagna con A ∈ M(m, n), B ∈ M(n, p).
- formula generale: dispense (Cor. 16.8) [f]^{B₂}_{C₂} = [id_W]^{C₁}_{C₂} · [f]^{B₁}_{C₁} · [id_V]^{B₂}_{B₁}; lavagna [f]^A′_B′ = Q [f]^A_B P⁻¹ con P = [I_V]^A_A′, Q = [I_W]^B_B′ (è la stessa formula).
- endomorfismi: dispense [f]^B_B = M⁻¹ [f]^C_C M con M = [id]^B_C; lavagna [f]^B′_B′ = P [f]^B_B P⁻¹ con P = [I_V]^B_B′ (stessa relazione, con la matrice del cambio di base presa nel verso opposto).
- similitudine: dispense A = M⁻¹ B M; lavagna B = P A P⁻¹ (equivalenti).

## Controllo dei conti con SymPy
Script in cartella temporanea (`verifica_l16.py`). Tutti i risultati finali scritti alla lavagna sono corretti:
- [e₁]_A′ = (2, −1), [e₂]_A′ = (−1, 1), [I_V]^A_A′ = ( 2 −1 ; −1 1 ) = ( 1 1 ; 1 2 )⁻¹.
- [(3, 7)]_A′ = (−1, 4) e −w₁ + 4w₂ = (3, 7).
- ( 0 −1 ; 1 3 )⁻¹ = ( 3 1 ; −1 0 ); [I_V]^B_B′ = ( 4 5 ; −1 −1 ).
- A·( 1 1 ; 1 2 ) = ( 3 5 ; 3 4 ); [L_A]^B_B = ( 3 6 ; 0 −1 ); det, traccia e rango uguali a quelli di A.

Errori e sviste del docente (nessuna conseguenza sui risultati):
- [e₁]_A′ scritto prima ( −1 ; 2 ) (a e b scambiati), e così la prima colonna della matrice; corretto in ( 2 ; −1 ) su segnalazione di uno studente (≈ 19:46 – 20:26).
- nei fumetti del disegno le coordinate sono scritte [v]_B e [v]_B′ invece di [v]_A e [v]_A′.
- la matrice provvisoria [ 2 ? ; −1 ? ] nel pannello in alto a destra non viene completata lì (la matrice completa è nel pannello sotto).
- nel diagramma della composizione e negli ultimi pannelli le lettere A, B sono usate sia per le basi sia per le matrici; l'etichetta dell'arco in basso è corretta in L_BA.
- nell'esempio [L_A]^B_B la base canonica era stata scritta A negli indici ed è stata corretta in C.
- nella Prop. sull'inversa e nella definizione di matrice del cambio di base non è scritta l'ipotesi di dimensione finita (sottintesa: si parla di basi {v₁, …, vₙ}).
- a voce: l'aneddoto della sonda ha data e protagonisti imprecisi (vedi nota nella sezione del disegno).

## Punti di lettura incerta
Nessuna formula illeggibile. Letture incerte:
- i pedici [v]_B e [v]_B′ nei due fumetti del disegno (scritti piccoli; letti come B e B′ in tre fotogrammi diversi);
- la lettera cancellata prima di «BA» nell'etichetta L_BA del diagramma;
- la sigla «tc» (tale che) nella seconda riga del riepilogo dopo la pausa, la cui parte finale, [v]_A′ = [I_V]^A_A′ [v]_A, è in parte coperta dal proiettore e dal bordo del pannello (si legge a 53:20 e a 55:00);
- la fine della riga della Prop. sull'inversa («è invertibile, e») tocca il bordo del pannello; la formula prosegue nel pannello sotto;
- il proiettore copre a tratti l'angolo in alto a destra del pannello in alto a sinistra (fine del titolo, «C = {e₁, …, eₙ} ← CANONICA», «B, B′ ⊆ W» dell'Oss 2): tutte queste scritte sono state lette in altri fotogrammi, dopo lo scorrimento del pannello.

## Note sulla trascrizione audio
Trascrizione di qualità media: molte storpiature (base «caronica / calorica / tanurica / pedonica», «a primo / apporimo / a Corimo», «via Vodopio», «matricide», «maturice»), numeri delle matrici a volte letti male, ma l'ordine degli argomenti è chiaro e coincide con la lavagna. La pausa (≈ 48:22) è tagliata sia nel video sia nell'audio, quindi i tempi di audio e fotogrammi coincidono per tutta la lezione.
