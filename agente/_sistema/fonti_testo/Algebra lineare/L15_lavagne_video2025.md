# Algebra lineare, Lezione 15: Applicazioni lineari II (lavagne dalla registrazione Webex del 2025, prof. Radeschi)

Fonte: video della registrazione 2025 linkata per L15, file `audio/algebra_L15_2025.mp4` (95 min, 1920×1080), trascrizione `trascrizioni/algebra_L15_2025.txt`. **La pausa è tagliata dal video**: a ≈ 52:23 il docente annuncia dieci minuti di pausa e subito dopo dice «Ok, riprendiamo»; tra il fotogramma di 52:40 e quello di 54:00 le lavagne sono già state cancellate e riscritte con il riepilogo.
Fotogrammi estratti ogni 20 s (285, da 00:00 a 95:00), in una cartella temporanea. La lavagna è in 4 pannelli scorrevoli (alto/basso, sinistra/destra). I duplicati (stessa lavagna, cambia solo la posizione del docente) sono stati scartati confrontando i pannelli; sono stati aperti uno per ogni stato della lavagna, circa uno ogni 2-3 minuti (01:00, 04:00, 07:00, 10:00, 13:00, 15:00, 18:00, 20:00, 23:00, 25:00, 28:00, 31:00, 34:00, 37:00, 40:00, 42:00, 44:00, 47:00, 50:00, 52:00, 52:40 ritagliato, 54:00, 55:00, 58:00, 61:00, 64:00, 66:00, 68:00, 71:00, 74:00, 77:00, 80:00, 82:00, 84:00, 87:00, 90:00, 93:00, 95:00), controllando che ogni pannello fosse letto completo prima di essere cancellato o fatto scorrere.

Convenzioni (come per L14):
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss); qui coincidono quasi con quelli dell'audio, salvo dopo la pausa tagliata.
- **[a voce]** indica ciò che è solo detto e non scritto; tra parentesi il tempo dell'audio.
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali: la trascrizione automatica è piena di errori («isomofilio», «vittoriali», «Samofi» = isomorfi).
- Sulla lavagna le colonne di A hanno l'**apice**: A = (A¹ | … | Aⁿ) (come nelle dispense e nei capitoli). L'identità è scritta I_V. I polinomi di grado ≤ 2 sono scritti ℝ[x]₂.

## Titolo e richiamo (00:00 – 04:00)
**LEZIONE 15: APPLICAZIONI LINEARI II**
**Prev.** f : V → W lineare. Allora
- dim Im f ≤ dim V, dim W
- f iniettiva ⟺ dim Im f = dim V
- f suriettiva ⟺ dim Im f = dim W

[a voce] (≈ 00:00 – 01:40) Richiamo della volta scorsa: applicazione lineare, nucleo e immagine; l'immagine ha dimensione minore o uguale sia a quella del dominio sia a quella del codominio, con l'uguaglianza nei due casi. Il punto di oggi sono le applicazioni lineari sia iniettive sia suriettive, gli **isomorfismi**.

## Corollario sulle dimensioni (04:00 – 07:00)
**Cor:** f : V → W lineare. Allora
1) f è iniettiva ⟹ dim V ≤ dim W
2) f è suriettiva ⟹ dim V ≥ dim W
**Dim:** 1) f iniettiva ⟹ dim V = dim Im f ≤ dim W
2) f suriettiva ⟹ dim V ≥ dim Im f = dim W ☒
→ **Oss:** dal risultato precedente, se f : V → W è biettiva ⟹ dim V = dim W

[a voce] (≈ 02:33 – 03:16) Collegamento con Matematica discreta: se c'è una funzione iniettiva da un insieme a un altro, l'insieme di partenza «di sicuro non è più grande» di quello d'arrivo.
[a voce] (≈ 03:16) «La dimostrazione è facile facile»: è una conseguenza del richiamo.

## Isomorfismi (07:00 – 15:00)
**Def** Una f : V → W lineare & biettiva è detta **ISOMORFISMO**.
Se V, W ammettono un isomorfismo f : V → W ⟹ V, W sono detti **ISOMORFI**.
**Prop:** se f : V → W è un isomorfismo (= lineare + biettiva) ⟹ f⁻¹ : W → V è anch'essa una mappa lineare (con «lineare» sottolineato)
**Oss:** L'osservazione precedente si può riscrivere come:
V, W sp vettoriali isomorfi ⟹ dim V = dim W
In realtà vale anche l'opposto
**Prop:** V, W sp vett sono isomorfi ⟺ dim V = dim W
(In particolare, dim V = n ⟹ V isomorfo a 𝕂ⁿ)

[a voce] (≈ 07:28) «Isomorfi» vuol dire letteralmente «con la stessa forma»: per quanto riguarda il corso, i due spazi sono equivalenti in tutto e per tutto.
[a voce] (≈ 07:28 – 08:57) Richiamo da Matematica discreta: una funzione biettiva collega ogni punto del codominio con un unico punto del dominio, e quindi ha un'inversa, che per ora è solo una funzione tra insiemi.
[a voce] (≈ 09:42) Gli isomorfismi si possono pensare come mappe lineari che hanno una mappa lineare «che va al contrario», l'inversa.
[a voce] (≈ 12:16) La proposizione ⟺ **non viene dimostrata** («implicitamente» si avranno gli strumenti); serve per decidere quando due spazi sono isomorfi. Dice che «non ci sono tantissimi spazi vettoriali»: quelli di dimensione 1 sono tutti isomorfi tra loro, quelli di dimensione 2 pure, e così via.
[a voce] (≈ 13:56 – 15:02) Programma della giornata: particolari isomorfismi permettono di trasferire informazioni anche molto astratte in questioni concrete, vettori colonna di numeri, cosa che un computer sa fare molto bene («a programmazione state usando le matrici»). La lezione è un tentativo di tradurre spazi vettoriali e applicazioni lineari in vettori e matrici.
[a voce] Nessuna dimostrazione della Prop. su f⁻¹.

## Esempio importante di isomorfismo: F_B (15:00 – 25:00)
**ESEMPIO IMPORTANTE DI ISOMORFISMO**
V sp vettoriale su 𝕂, B = {v₁, …, vₙ} base di V
Allora definiamo 𝕂ⁿ —F_B→ V, F_B( a₁ ; ⋮ ; aₙ ) = a₁v₁ + a₂v₂ + … + aₙvₙ
[ F_B(e₁) = F_B( 1 ; 0 ; ⋮ ; 0 ) = v₁, …, F_B(e_i) = v_i … ] (tra parentesi quadre)
**Prop:** se B è una base, F_B è un isomorfismo
**OSS:** F_B⁻¹ : V → 𝕂ⁿ, F_B⁻¹(v) = ( a₁ ; ⋮ ; aₙ ) = [v]_B ← **VETTORE DELLE COORDINATE DI v NELLA BASE B**
(sotto: v = a₁v₁ + a₂v₂ + … + aₙvₙ, con i coefficienti sottolineati)

[a voce] (≈ 16:14) La mappa dipende dalla scelta della base.
[a voce] (≈ 16:47) «È facile controllare che è lineare.»
[a voce] (≈ 18:45) F_B manda i vettori della base canonica nei vettori della base scelta.
[a voce] (≈ 19:32 – 20:06) **Esercizio proposto** («vi invito a farlo, è carino»): il fatto che v₁, …, vₙ siano generatori si traduce nella suriettività di F_B (l'immagine è Span(v₁, …, vₙ)); il fatto che siano linearmente indipendenti nell'iniettività. Le due condizioni di base danno esattamente l'isomorfismo.
[a voce] (≈ 20:43 – 22:39) Domanda alla classe: come si calcola l'inversa? Le entrate del vettore dipendono da v: si scrive v in modo unico come combinazione della base (proprietà delle basi) e i coefficienti sono le coordinate di v.
[a voce] (≈ 23:45 – 24:30) Il simbolo [v]_B è «parecchio importante»: F_B⁻¹ è quella che permette di prendere vettori e farli diventare elementi di 𝕂ⁿ.

## Esempio: coordinate di un polinomio (25:00 – 32:00)
**Es.** V = ℝ[x]₂, B = { x², x + 1, 1 }
p(x) = 3x² + 2x + 1
[p(x)]_B = ( a ; b ; c ) ∈ ℝ³
p(x) = a x² + b(x + 1) + c·1 = ax² + bx + (b + c)
= 3x² + 2x + 1 ⟹ a = 3, b = 2, b + c = 1 → c = −1
[p(x)]_B = ( 3 ; 2 ; −1 )

[a voce] (≈ 25:16) Lo spazio ha dimensione 3; il docente dice che i tre polinomi dati sono una base (senza verificarlo).
[a voce] (≈ 28:06 – 28:44) Si raccolgono le potenze di x; due polinomi sono uguali se hanno gli stessi coefficienti.
[a voce] (≈ 29:27 – 30:33) Per comunicare un polinomio a un computer ci si mette d'accordo su una base e si passa il vettore (3, 2, −1): il computer sa che rappresenta 3 volte il primo elemento della base più 2 volte il secondo meno una volta il terzo.
[a voce] (≈ 30:33 – 31:37) A una domanda di uno studente rispiega il raccoglimento b(x + 1) + c = bx + (b + c).
[a voce] (≈ 32:23 – 32:55) **Come sottolineato a lezione:** ogni spazio vettoriale (di dimensione n) è isomorfo a 𝕂ⁿ, e per ogni base si trova un isomorfismo; l'isomorfismo **dipende dalla base**, basi diverse danno isomorfismi diversi. Come si traducono l'uno nell'altro sarà argomento «della volta prossima».

[verifica] a x² + b(x + 1) + c = 3x² + 2x + 1 ⟺ (a, b, c) = (3, 2, −1). La lettura «x + 1» (e non «x − 1») nel secondo elemento della base è confermata da «b(x+1)» e da b + c = 1.

## Matrice associata: definizione (34:00 – 44:00)
**MATRICE ASSOCIATA**
**Ricordiamo** A ∈ M(m, n, 𝕂) ⇝ L_A : 𝕂ⁿ → 𝕂ᵐ
A = (A¹ | … | Aⁿ), x = ( x₁ ; ⋮ ; xₙ ) ⟹ L_A x = A·x = x₁A¹ + x₂A² + … + xₙAⁿ
**Def.** Siano V, W sp vett su 𝕂, con basi B = {v₁, …, vₙ} ⊆ V, C = {w₁, …, wₘ} ⊆ W
Data f : V → W lineare, definiamo la **MATRICE ASSOCIATA** a f, dalla base B alla base C è
[f]^B_C ∈ M(m, n, 𝕂) data da
[f]^B_C = ( [f(v₁)]_C | [f(v₂)]_C | … | [f(vₙ)]_C )

[a voce] (≈ 36:20) Data una matrice si ottiene una mappa lineare; ora si vuole il viceversa: a una mappa lineare associare una matrice che ne contenga «tutte le informazioni».
[a voce] (≈ 37:39) n è la dimensione di V, m quella di W.
[a voce] (≈ 39:03) «Purtroppo» non basta la mappa: bisogna fissare delle basi.
[a voce] (≈ 39:39) La matrice ha tante righe quanto la dimensione di W e tante colonne quanto la dimensione di V. Si definisce colonna per colonna: si mandano i vettori della base di partenza in W con f e se ne calcolano le coordinate nella base di arrivo.
[a voce] (≈ 41:14) Il docente ammette che la definizione può sembrare «caotica» e passa subito a un esempio.

## Esempio di matrice associata (44:00 – 52:40)
**Es:** f : ℝ[x]₂ → ℝ², f(p(x)) = ( p(1) ; p(−1) )
B = { 1, x, x² }, C = { e₁ = ( 1 ; 0 ), e₂ = ( 0 ; 1 ) }. Calcolare [f]^B_C
[f]^B_C ∈ M(2, 3); [f]^B_C = ( [f(1)]_C | [f(x)]_C | [f(x²)]_C )
1 ⟶ f(1) = ( 1 ; 1 ) ⟶ [f(1)]_C = ( a ; b ) = ( 1 ; 1 )
( 1 ; 1 ) = a e₁ + b e₂ = a( 1 ; 0 ) + b( 0 ; 1 ) = ( a ; b )
x ⟶ f(x) = ( 1 ; −1 ) ⟶ [f(x)]_C = ( a ; b ) = ( 1 ; −1 ), sotto: = a e₁ + b e₂ = ( a ; b )
x² ⟶ f(x²) = ( 1 ; 1 ) ⟹ [f(x²)]_C = [( 1 ; 1 )]_C = ( 1 ; 1 )
⇝ **[f]^B_C = ( 1 1 1 ; 1 −1 1 )** (a 52:40)

[a voce] (≈ 42:54) La mappa valuta il polinomio in 1 e in −1. Per cominciare si prendono le basi canoniche.
[a voce] (≈ 44:43 – 45:17) Domanda alla classe sulle taglie: righe = dim del codominio (2), colonne = dim del dominio (3).
[a voce] (≈ 46:26 – 46:58) Il polinomio costante 1 vale 1 sia in 1 sia in −1.
[a voce] (≈ 51:37) f(x²) = (1, 1) è lo stesso vettore di f(1), quindi la colonna è la stessa.
[a voce] (≈ 52:23) Pausa di 10 minuti (tagliata nel video).

**Differenza con le dispense:** le dispense (Es. 15.7) usano f(p) = (p(2), p(−2)), con matrice ( 1 2 4 ; 1 −2 4 ); a lezione 2025 l'esempio è con 1 e −1.
[verifica] Con SymPy: f(1) = (1, 1), f(x) = (1, −1), f(x²) = (1, 1); matrice ( 1 1 1 ; 1 −1 1 ).

## Dopo la pausa: riepilogo e L_A (54:00 – 68:00)
f : V → W lineare, B = {v₁, …, vₙ} ⊆ V, C = {w₁, …, wₘ} ⊆ W basi
⇝ [f]^B_C = ( [f(v₁)]_C | … | [f(vₙ)]_C ), con le frecce: **BASE DI PARTENZA** → B (in alto), **BASE DI ARRIVO** → C (in basso)

**Oss** A ∈ M(m, n, 𝕂) ⇝ L_A : 𝕂ⁿ → 𝕂ᵐ, x = ( x₁ ; ⋮ ; xₙ ) ⟶ L_A x = Ax = x₁A¹ + … + xₙAⁿ
B = {e₁, …, eₙ}, C = {e₁, …, eₘ} ⇝ [L_A]^B_C ∈ M(m, n, 𝕂)
(a 58:00 e 61:00 è scritto C = {e₁, …, eₙ}; a 66:00 è corretto in {e₁, …, eₘ})
[L_A]^B_C = ( [L_A e₁]_C | … | [L_A eₙ]_C ) = ( A¹ | A² | … | Aⁿ ) = A
e₁ ⟶ L_A e₁ = A¹ ⇝ [L_A e₁]_C = L_A e₁ = A¹ (sotto l'uguale una freccia)
perché in 𝕂ᵐ: ( a₁ ; ⋮ ; aₘ ) = a₁e₁ + a₂e₂ + … + aₘeₘ ⟹ [( a₁ ; ⋮ ; aₘ )]_C = ( a₁ ; ⋮ ; aₘ ) ← BASE CAN
(sulla lavagna l'ultimo pedice è scritto aₙ, e 𝕂ⁿ al posto di 𝕂ᵐ)
[L_A e₂]_C = L_A e₂ = A² (sotto l'uguale: «C canonica»)
**RIASSUMENDO** se A ∈ M(m, n), B = base can di 𝕂ⁿ, C = base can di 𝕂ᵐ
⟹ L_A : 𝕂ⁿ → 𝕂ᵐ ha matrice associata **[L_A]^B_C = A**

[a voce] (≈ 53:34) Nella notazione la base di partenza B si mette sopra, quella di arrivo C sotto.
[a voce] (≈ 55:52) [L_A]^B_C ha le stesse dimensioni di A.
[a voce] (≈ 58:48 – 59:22) Lo scopo dell'esempio: la costruzione, che può sembrare «super random, super arbitraria», è proprio l'operazione inversa di quella che manda una matrice A nella mappa L_A.
[a voce] (≈ 59:58 – 01:01:43) **Come sottolineato a lezione** (richiamo): tra tutte le basi di 𝕂ᵐ la base canonica è «la più speciale», perché le coordinate di un vettore sono le sue entrate; è una proprietà che ha solo la base canonica.
[a voce] (≈ 01:05:43 – 01:06:16) È la prima di una serie di evidenze che queste matrici hanno proprietà speciali.

[verifica] Per A simbolica 2 × 3: A·e_j = A^j per ogni j; quindi la matrice associata nelle basi canoniche è A.

## Calcolare l'immagine con la matrice (68:00 – 78:00)
**PROP** f : V → W lineare, B = {v₁, …, vₙ} ⊆ V, C = {w₁, …, wₘ} ⊆ W basi
⟹ ∀v ∈ V, **[f(v)]_C = [f]^B_C · [v]_B** (riquadrato)
**Es:** f : ℝ[x]₂ → ℝ², B = {1, x, x²}, C = {e₁, e₂}
supponiamo di sapere che [f]^B_C = ( 1 1 1 ; 1 −1 1 )
Calcolare f(x² + 1)
f(x² + 1) ∈ ℝ²
[f(x² + 1)]_C = [f]^B_C · [x² + 1]_B
[x² + 1]_B = ( a ; b ; c ) = ( 1 ; 0 ; 1 ) dove x² + 1 = a·1 + b x + c x² (con le frecce: b = 0, a = 1, c = 1)
[f(x² + 1)]_C = ( 1 1 1 ; 1 −1 1 )·( 1 ; 0 ; 1 ) = ( 2 ; 2 ) (cerchiati) ⟹ f(x² + 1) = 2e₁ + 2e₂ = ( 2 ; 2 )

[a voce] (≈ 01:06:48) La proposizione **non viene dimostrata** a lezione (nelle dispense la dimostrazione c'è, Prop. 15.9).
[a voce] (≈ 01:08:35 – 01:09:12) Due strade: calcolare prima f(v) e poi le coordinate, oppure calcolare prima le coordinate di v e poi moltiplicare per la matrice. «Ricordatevi questa formula.»
[a voce] (≈ 01:09:45) Nell'esempio la mappa «non è data»: si conosce solo la matrice associata (è la stessa trovata prima).
[a voce] (≈ 01:15:26) Nella base canonica il vettore delle coordinate è uguale al vettore stesso, quindi f(x² + 1) = (2, 2).
[a voce] (≈ 01:16:00) Uno studente segnala un errore: nella scrittura x² + 1 = a·1 + bx + c·x³ «è sfuggito un cubo», doveva essere x²; il docente corregge (a 77:00 si legge x²).
[a voce] (≈ 01:16:32 – 01:17:02) A una domanda rispiega perché c = 1: il coefficiente di x² è c da una parte e 1 dall'altra.

[verifica] [x² + 1]_B = (1, 0, 1); ( 1 1 1 ; 1 −1 1 )(1, 0, 1) = (2, 2); controllo diretto con f(p) = (p(1), p(−1)): (2, 2). ✓

## Teoria e calcoli (78:00 – 86:00)
Diagramma (pannello in basso a sinistra):
TEORIA: V (sp vett di dim n, B base) —f→ W (dim = m, base C); A = [f]^B_C
linea ondulata di separazione; frecce verticali V ↓ 𝕂ⁿ e W ↓ 𝕂ᵐ; una freccia ondulata da f verso L_A
CALCOLI: 𝕂ⁿ —L_A→ 𝕂ᵐ

Esempio (pannello sotto):
V = { f : ℝ → ℝ | f(t + 1) = f(t) }
T : V → V, T(f) = ∫₀¹ K(t, s) f(s) ds
(accanto, una freccia ondulata da V verso un vettore colonna ( a ; ⋮ ; a ) di numeri)

[a voce] (≈ 01:17:45 – 01:18:16) Da una parte l'universo teorico, dove vivono gli spazi vettoriali astratti; dall'altra il mondo pratico delle macchine e del calcolo.
[a voce] (≈ 01:18:58 – 01:21:29) Una base trasforma vettori astratti in «stringhe di numeri» (array); una mappa lineare astratta diventa L_A con A = [f]^B_C. «Dovete pensare alle matrici come mappe lineari», che prendono un vettore e lo trasformano in un altro moltiplicandolo per la matrice.
[a voce] (≈ 01:22:41 – 01:23:54) Esempio dalla teoria dei segnali: V spazio delle funzioni periodiche di periodo 1 e T che manda f nell'integrale con un nucleo K(t, s). Comunicare oggetti così a un computer non è facile, ma fissata una base si traducono in stringhe di numeri e la mappa in una moltiplicazione per una matrice. **È solo un'illustrazione**: lo spazio delle funzioni periodiche non ha dimensione finita, e il docente non entra nei dettagli (non nelle dispense).

## Identità, Hom(V, W) e l'isomorfismo con le matrici (86:00 – 95:00)
**PROP:** V sp vett, I_V : V → V
⟹ ∀ base B di V, [I_V]^B_B = I_n ∈ M(n, n, 𝕂)
**Def:** V, W sp vettoriali, sia Hom(V, W) = { f : V → W | f lineare }
**PROP:** f, g ∈ Hom(V, W) allora
- f + g : V → W, (f + g)(v) = f(v) + g(v), è lineare (cioè f + g ∈ Hom(V, W))
- λ ∈ 𝕂, λf : V → W, (λf)(v) = λ·(f(v)), è lineare (cioè λf ∈ Hom(V, W))
- Hom(V, W) è uno sp vettoriale rispetto alle operazioni sopra
**PROP:** Date V, W sp vettoriali su 𝕂, B = {v₁, …, vₙ} ⊆ V, C = {w₁, …, wₘ} ⊆ W basi. Allora
Hom(V, W) ⟶ M(m, n, 𝕂), (f : V → W) ↦ [f]^B_C
è un **ISOMORFISMO**

[a voce] (≈ 01:25:29 – 01:26:06) La mappa identità va nella matrice identità, per ogni base fissata (la stessa base in partenza e in arrivo); sarà importante la volta prossima, parlando di composizione di funzioni.
[a voce] (≈ 01:27:07) Hom(V, W) è l'insieme che ha come elementi le mappe lineari da V a W.
[a voce] Nessuna dimostrazione delle tre proposizioni.
[a voce] (≈ 01:34:04 – 01:34:37) Lettura: fissate una base di V e una di W, a ogni mappa lineare corrisponde una matrice e a ogni matrice una mappa lineare, in modo biunivoco; ogni matrice dà la moltiplicazione a sinistra, quindi «ogni mappa lineare è una mappa di moltiplicazione a sinistra». Fine della lezione (≈ 01:34:37).

Non sono svolti esercizi con basi di arrivo non canoniche (nelle dispense: Es. 15.8 ed Esercizio 15.13).

## Controllo dei conti con SymPy
Script in cartella temporanea (`verifica_l15.py`). Tutti i risultati scritti alla lavagna sono corretti:
- [3x² + 2x + 1]_B = (3, 2, −1) con B = {x², x + 1, 1}.
- f(p) = (p(1), p(−1)) in basi canoniche: ( 1 1 1 ; 1 −1 1 ); f(x² + 1) = (2, 2) sia con la matrice sia direttamente.
- [L_A]^{can}_{can} = A.
- Dispense: ( 1 2 4 ; 1 −2 4 ), con C′: ( 1 2 4 ; 2 0 8 ); p = 3x² + 5x + 1 ↦ (23, 3); Esercizio 15.13: ½( 1 5 ; 3 −1 ; −1 −1 ).

Errori e sviste del docente (nessuna conseguenza sui risultati):
- C = {e₁, …, eₙ} come base di arrivo di 𝕂ᵐ (corretto in eₘ a 66:00); nella riga «base can» il vettore generico di 𝕂ᵐ ha pedici fino a n.
- x² + 1 = a·1 + bx + c·x³, corretto in x² su segnalazione di uno studente.
- Nel corollario e nella Prop. ⟺ non è scritta l'ipotesi di dimensione finita (nelle dispense c'è per la Prop. 15.4).

## Punti illeggibili
Nessuna formula illeggibile. Letture incerte: il vettore colonna accanto all'esempio delle funzioni periodiche (84:00), scritto con entrate tutte uguali «a» o con puntini; il proiettore copre a tratti la parte alta del pannello in alto a sinistra (titolo, «Ricordiamo … L_A : 𝕂ⁿ → 𝕂ᵐ»), letta in altri fotogrammi dopo lo scorrimento.

## Note sulla trascrizione audio
Trascrizione di qualità media: molte storpiature («isomofilio», «Samofi», «spazi vittoriali», «basica anonica» = base canonica, «HOM» corretto), ma l'ordine degli argomenti è chiaro e coincide con la lavagna. La pausa (≈ 52:23) è tagliata sia nel video sia nell'audio.
