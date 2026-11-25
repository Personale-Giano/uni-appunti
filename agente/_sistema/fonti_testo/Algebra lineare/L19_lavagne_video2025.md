# Algebra lineare, Lezione 19: Prodotti scalari I (lavagne dalla registrazione Webex del 2025, prof. Radeschi)

Fonte: video della registrazione Webex del 17 nov 2025 linkata su Moodle per L19, file `audio/algebra_L19_2025.mp4` (95 min 55 s, 1920×1080). **La pausa è tagliata dal video**: nel fotogramma di 50:24 le lavagne sono ancora piene (esempio g_S((1, 1), (2, 3)) = 21 appena finito), in quello di 50:26 sono già tutte cancellate, con la tabella «ENDOMORFISMI | PRODOTTI SCALARI» appena iniziata e il riepilogo «S matrice simmetrica ⟹ g_S(v, w) = ᵗv S w». La trascrizione conferma: a ≈ 49:47 il docente annuncia «10 minuti di pausa, ci rivediamo alle 17:10» e a ≈ 50:26 riparte con «ripetiamo molto velocemente». A 36:40 – 36:54 il docente si toglie il maglione (nero → maglietta blu): **non** è un taglio, si vede nei fotogrammi ogni 2 s. Il video comincia con lo schermo nero (00:00) e il titolo già scritto a 00:20; finisce a 95:55 mentre il docente commenta la verifica con [v]_B e [w]_B, senza saluti visibili.
**Trascrizione audio:** `trascrizioni/algebra_L19_2025.txt` (Whisper, completa, ≈ 00:01 – 95:26, fiducia bassa). Le note [a voce] fino a ≈ 66:30 sono state scritte prima su un file parziale (`.part`, identico in quel tratto) e poi completate con la trascrizione intera.
Fotogrammi estratti ogni 20 s (288, da 00:00 a 95:40), in una cartella temporanea. La lavagna è in 4 pannelli scorrevoli (alto/basso, sinistra/destra). **Sono stati letti tutti i 288 fotogrammi**, in 72 tavole di 4 fotogrammi consecutivi ridotti a 800×450, controllando per ogni pannello l'ultimo stato prima di cancellazioni e scorrimenti. Ritagli ingranditi a piena risoluzione per le scritte piccole a: 04:00, 09:40, 19:40, 21:40, 27:00, 33:00, 35:40, 37:00, 48:20, 50:20, 56:40, 67:40, 83:40, 91:00, 91:40. Fotogrammi aggiuntivi ogni 2 s da 36:40 a 37:00 e da 50:20 a 50:40 (per localizzare il taglio della pausa).

Convenzioni (come per L14 – L17):
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss); coincidono con quelli dell'audio, perché la pausa è tagliata sia nel video sia nell'audio.
- **[a voce]** indica ciò che è solo detto e non scritto; tra parentesi il tempo dell'audio (dalla trascrizione parziale, fiducia bassa: «prodotto stalale / scalato / statale» = prodotto scalare, «endomorsisti / indomorfismi» = endomorfismi, «trasforza / trasfosto / trasporto» = trasposta, «eugideno / pideo / clideo» = euclideo, «sinimetria» = simmetria, «bineare» = bilineare).
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali.
- Sulla lavagna le basi sono scritte in corsivo (ℬ); qui B. «( a b ; c d )» indica la matrice con righe (a b) e (c d), «( a ; b )» il vettore colonna. Il prodotto scalare è scritto ⟨v, w⟩ con parentesi angolate; la trasposta con la t in alto a sinistra (ᵗv). S(n) = matrici simmetriche n × n (notazione già introdotta nel corso).

## Titolo e avvertenza sul campo (00:00 – 04:00)
**LEZIONE 19: PRODOTTI SCALARI I**
⚠ Oggi 𝕂 = ℝ (poiché possiamo parlare di «r > 0»)

[a voce] (≈ 00:01 – 01:08) Si lascia temporaneamente l'argomento autovalori e autovettori per un altro modo di vedere le matrici quadrate: forme e prodotti scalari.
[a voce] (≈ 01:08 – 01:45) «Non sembrerà», ma i prodotti scalari sono il modo per fare geometria nel senso vero della parola: serviranno a definire lunghezze di vettori, distanze tra punti, angoli, aree; tutto ciò che è misurabile deriva dalla nozione di prodotto scalare.
[a voce] (≈ 02:18 – 03:29) Fino alla volta scorsa conveniva usare i numeri complessi (ogni polinomio ha radici); oggi è «fondamentale» usare ℝ, perché i reali hanno un ordine: si può dire quando un numero è maggiore, minore o maggiore o uguale a zero. In ℂ non esiste un ordine che rispetti le proprietà di un ordine.

## Definizione di prodotto scalare (04:00 – 08:40)
(pannello in basso a sinistra, poi fatto scorrere in alto a ≈ 06:20)
**Def.** V sp. vett. su ℝ. Un **PRODOTTO SCALARE** (sottolineato) su V è una funzione
V × V ⟶ ℝ
(v, w) ⟼ ⟨v, w⟩
t.c.
1) ∀ v₁, v₂, w ∈ V, ⟨v₁ + v₂, w⟩ = ⟨v₁, w⟩ + ⟨v₂, w⟩
2) ∀ v, w ∈ V, λ ∈ ℝ, ⟨λv, w⟩ = λ·⟨v, w⟩
3) ⟨v, w⟩ = ⟨w, v⟩

[a voce] (≈ 04:47 – 05:44) Rischio di confusione: negli spazi vettoriali c'era il «prodotto per scalare» (uno scalare per un vettore); questo è diverso, si chiama prodotto scalare e prende **due vettori** e dà come risultato **un numero**.
[a voce] (≈ 06:37 – 07:51) La 1) è una specie di distributività rispetto alla prima componente, la 2) una sorta di associatività con gli scalari, la 3) è la proprietà di **simmetria**: scambiando l'ordine il risultato non cambia.

## Osservazioni: linearità e bilinearità (08:40 – 15:40)
(pannello in basso a sinistra, sotto la definizione)
**Oss.** ① PROPRIETÀ 1, 2 = «Il prodotto scalare è LINEARE RISP. alla prima variabile»
② Dalla proprietà 3, valgono anche
1') ⟨v, w₁ + w₂⟩ = ⟨v, w₁⟩ + ⟨v, w₂⟩
2') ⟨v, λw⟩ = λ⟨v, w⟩

(pannello in basso a destra, scritto a 11:40 – 15:20)
(Mostriamo che 2' vale:)
⟨v, λw⟩ =₃ ⟨λw, v⟩ =₂ λ·⟨w, v⟩ =₃ λ⟨v, w⟩
(sotto i primi due uguali i numeri 3 e 2, sopra il terzo un 3: la proprietà usata; a destra, sotto, un «= λ⟨v, w⟩» scritto prima e poi ricollegato)
**Oss.** 1', 2' = «⟨ , ⟩ è lineare anche rispetto alla seconda variabile»
⇕
PRODOTTI SCALARI SONO **BILINEARI**

[a voce] (≈ 08:22 – 09:25) Le proprietà 1 e 2 sono sostanzialmente quelle di un'applicazione lineare: si riassumono dicendo che il prodotto scalare è lineare rispetto alla prima variabile.
[a voce] (≈ 10:03 – 10:39) Poiché scambiare l'ordine degli argomenti non cambia nulla, ogni proprietà che vale per la prima componente vale anche per la seconda.
[a voce] (≈ 11:15 – 13:07) Si dimostra solo la 2'; «serve la proprietà 3»: si scambia, si porta fuori λ con la 2, si scambia di nuovo. Uno studente chiede se basta la proprietà 3: sì, permette di «portare fuori λ e rimetterlo nell'altro posto».
[a voce] (≈ 13:41 – 14:52) Essendo lineare rispetto sia alla prima sia alla seconda variabile, si dice che il prodotto scalare è **bilineare**.

[verifica] La 1' segue nello stesso modo: ⟨v, w₁ + w₂⟩ = ⟨w₁ + w₂, v⟩ = ⟨w₁, v⟩ + ⟨w₂, v⟩ = ⟨v, w₁⟩ + ⟨v, w₂⟩ (alla lavagna non è scritta).

## Esempio 1: il prodotto scalare euclideo (15:40 – 21:20)
(pannello in basso a destra, poi fatto scorrere in alto a ≈ 18:00)
**ESEMPIO** V = ℝⁿ, v = ( x₁ ; ⋮ ; xₙ ), w = ( y₁ ; ⋮ ; yₙ )
IL PRODOTTO SCALARE EUCLIDEO è
⟨v, w⟩ = ᵗv·w = (x₁ … xₙ)·( y₁ ; ⋮ ; yₙ ) = x₁y₁ + x₂y₂ + … + xₙyₙ
**es.** v = ( 1 ; 1 ; 2 ), w = ( −1 ; −1 ; 1 ) ∈ ℝ³
⟹ ⟨v, w⟩ = 1·(−1) + 1·(−1) + 2·(1) = 0
(a destra, riquadrato a ≈ 19:40 – 20:40:)
⟨v, w⟩ = v • w
= ‖v‖ ‖w‖·cos θ
(sotto, un piccolo disegno: due frecce v e w uscenti da un punto, con l'angolo θ tra loro)

[a voce] (≈ 15:56 – 17:10) È il prodotto scalare «più carino di tutti». ᵗv si pensa come una matrice con una sola riga: ᵗv·w è il prodotto di una matrice 1 × n per una n × 1, quindi una matrice 1 × 1, cioè un numero.
[a voce] (≈ 17:56 – 18:31) Ci sono infiniti prodotti scalari possibili; ora se ne considera uno specifico.
[a voce] (≈ 19:16 – 20:22) In alcuni libri (e nei corsi di fisica) il prodotto euclideo si scrive v • w; quando i vettori si vedono come frecce si scrive anche come «lunghezza del primo per lunghezza del secondo per il coseno dell'angolo compreso», per esempio quando si introduce il lavoro di una forza. Chi non l'ha mai visto non si preoccupi.

[verifica] (1, 1, 2)·(−1, −1, 1) = −1 − 1 + 2 = 0 ✓.

## Esempio 2: un prodotto scalare sui polinomi (21:20 – 25:00)
(pannello in basso a sinistra, dopo aver cancellato a ≈ 21:20 le osservazioni ① ②)
**ESEMPIO 2.** V = ℝ₂[x]
⟨p₁(x), p₂(x)⟩ = p₁(0)p₂(0) + p₁(1)p₂(1) + p₁(2)p₂(2)

[a voce] (≈ 21:31 – 22:41) Su uno spazio più astratto, lo spazio dei polinomi di grado ≤ 2 a coefficienti reali, un prodotto scalare è qualcosa che prende due polinomi e restituisce un numero; «bisogna far vedere, ma non è troppo difficile» che le tre proprietà valgono.
[a voce] (≈ 22:41 – 23:49) Con un prodotto scalare su spazi di polinomi o di funzioni si potrà parlare di angolo o distanza tra due polinomi: concetti usati in teoria dei segnali e in decomposizioni importanti anche in informatica (polinomi «ortogonali», cioè «a 90 gradi» tra loro).
[a voce] (≈ 24:37 – 25:16) Anticipo del piano: come gli endomorfismi corrispondono in modo biunivoco alle matrici quadrate, i prodotti scalari corrisponderanno alle **matrici simmetriche**.

## Degenere e definito positivo (25:00 – 28:20)
(stesso pannello, sotto una riga orizzontale)
**Def.** un prodotto scalare ⟨ , ⟩ è
· **DEGENERE** se ∃ v ∈ V t.c. ⟨v, w⟩ = 0 ∀ w ∈ V
· **DEFINITO POSITIVO** se ∀ v ∈ V, v ≠ 0, ⟨v, v⟩ > 0
(a 26:40 l'ultima V della riga «degenere» è scritta W, a 27:00 è già V)

[a voce] (≈ 25:16 – 26:46) Degenere: esiste almeno un vettore che dà prodotto nullo con tutti gli altri. Definito positivo: il prodotto di ogni vettore non nullo con se stesso è sempre maggiore di zero: «è qui che dobbiamo utilizzare il concetto di maggiore».
[a voce] (≈ 27:16 – 27:47) **Come sottolineato a lezione:** i prodotti scalari che davvero interessano per fare geometria sono quelli definiti positivi. I due esempi dati lo sono.

## Prop.: l'euclideo è definito positivo (28:20 – 36:40)
(pannello in basso a destra, dopo aver cancellato a ≈ 28:00 il pannello «Mostriamo che 2' vale»)
**Prop.** Il PRODOTTO SCALARE Euclideo è un prodotto scalare definito positivo
**Dim.** Ricordiamo v, w ∈ ℝⁿ ⇝ ⟨v, w⟩ = ᵗv w
① PRODOTTO SCALARE
a) ⟨v₁ + v₂, w⟩ = ᵗ(v₁ + v₂)·w = (ᵗv₁ + ᵗv₂)·w = ᵗv₁ w + ᵗv₂ w = ⟨v₁, w⟩ + ⟨v₂, w⟩
b) ⟨λv, w⟩ = ᵗ(λv)·w = (λ ᵗv)·w = λ·(ᵗv w) = λ⟨v, w⟩
② v = ( x₁ ; ⋮ ; xₙ ) ⇝ ⟨v, v⟩ = x₁² + x₂² + … + xₙ² ≥ 0 (sotto ciascun quadrato una graffa con «≥ 0»), e «= 0» ⟺ x₁ = … = xₙ = 0, cioè v = ( 0 ; ⋮ ; 0 )

[a voce] (≈ 29:24 – 32:14) a) usa che la trasposta di una somma è la somma delle trasposte e la distributività del prodotto fra matrici; b) che la trasposta di λv è λ ᵗv e l'associatività.
[a voce] (≈ 32:14 – 33:01) Domanda di uno studente: i prodotti scalari sono tanti? Sì, infiniti: «prodotto scalare» è una classe di funzioni, l'euclideo è un esempio specifico dentro questa classe.
[a voce] (≈ 33:39 – 35:24) ⟨v, v⟩ è la somma dei quadrati delle coordinate; in ℝ ogni quadrato è ≥ 0, quindi la somma è ≥ 0, ed è 0 solo se tutte le coordinate sono 0. Quindi per v ≠ 0 il prodotto è strettamente positivo.
[a voce] (≈ 35:24 – 35:40) **Esercizio lasciato:** «lascerò a voi il piacere» di far vedere che anche il prodotto scalare dell'Esempio 2 è definito positivo.

(Nota: la simmetria (proprietà 3) del prodotto euclideo non è scritta nella Dim.; per la dimostrazione analoga con S simmetrica, dopo la pausa, la 3) è invece dimostrata.)

[verifica] Additività e omogeneità di ᵗv w ✓ (SymPy, simbolica in ℝ²). ⟨v, v⟩ = Σ xᵢ² ✓.

## Matrici simmetriche e prodotto scalare g_S (36:40 – 43:20)
(pannello in basso a sinistra, dopo aver cancellato a ≈ 37:00 il pannello con l'Esempio 2 e le definizioni; il pannello «Lezione 19 / Def.» è fatto scorrere in alto)
**MATRICI SIMMETRICHE**
Ricordiamo A ∈ M(n) è SIMMETRICA se aᵢⱼ = aⱼᵢ ∀ i, j ⟷ ᵗA = A
**Def.** data S ∈ S(n) definiamo il prodotto scalare su ℝⁿ
g_S(v, w) = ᵗv · S · w
(sotto i tre fattori: 1×n, n×n, n×1)
**Oss.** S ⟶ g_S è analogo di A ⟶ L_A

[a voce] (≈ 36:07 – 36:50) Come sono fatti gli altri prodotti scalari, anche solo in ℝⁿ? Si costruiscono con le matrici simmetriche.
[a voce] (≈ 37:24 – 39:27) Ripasso chiesto alla classe; uno studente fa notare che è stato scritto due volte aᵢⱼ (corretto in aᵢⱼ = aⱼᵢ). S(n) era lo spazio delle matrici simmetriche n × n.
[a voce] (≈ 40:27 – 41:32) Somiglianza con l'euclideo: l'unica differenza è la matrice S in mezzo. Controllo delle dimensioni: 1 × n per n × n per n × 1 dà una matrice 1 × 1, cioè un numero.
[a voce] (≈ 41:32 – 42:45) Inizio di una serie di paralleli con la teoria precedente: la mappa che associa a S il prodotto scalare g_S è l'analogo della mappa che associava a ogni matrice n × n l'endomorfismo L_A.

## Prop.: g_S è un prodotto scalare (43:20 – 48:40)
(pannello in basso a destra, dopo aver cancellato a ≈ 43:00 il pannello dell'esempio euclideo; poi fatto scorrere in alto)
**Prop.** g_S è un prodotto scalare
**Dim.** · PROP 1, 2 sono uguali alla dim nel caso del prodotto Euclideo
· 3) g_S(v, w) = ᵗv S w = ᵗ(ᵗv S w) = ᵗw · ᵗS · ᵗ(ᵗv) = ᵗw · S · v = g_S(w, v)
(sotto «ᵗ(ᵗv S w)» una piccola punta ∧ e una riga; sotto il penultimo passaggio, con una freccia verso ᵗS = S: «S simmetrica»)

[a voce] (≈ 43:55 – 44:31) Le proprietà 1 e 2 sono dovute solo alle proprietà del prodotto fra matrici, come per l'euclideo.
[a voce] (≈ 45:22 – 47:32) ᵗv S w è una matrice 1 × 1: trasporla non cambia nulla («una riga, una colonna, le scambiamo, non fa niente»). La trasposta di un prodotto è il prodotto delle trasposte in ordine inverso; la trasposta della trasposta è la matrice di partenza; qui «ci serve che la matrice S sia simmetrica».

[verifica] Per S simmetrica 3 × 3 generica, ᵗv S w − ᵗw S v = 0 ✓.

## Esempio numerico con S = ( 1 2 ; 2 3 ) (48:40 – 50:24, poi taglio della pausa)
(pannello in basso a destra)
**Es.** S = ( 1 2 ; 2 3 ) ∈ S(2)
g_S(( 1 ; 1 ), ( 2 ; 3 )) = (1, 1)·(( 1 2 ; 2 3 )·( 2 ; 3 )) = (1, 1)·( 8 ; 13 ) = 21

[a voce] (≈ 49:16 – 49:47) Il prodotto fra matrici è associativo, quindi si può cominciare da dove si vuole: prima S·(2, 3) = (2 + 6, 4 + 9) = (8, 13), poi (1, 1)·(8, 13) = 8 + 13 = 21. Poi la pausa.

[verifica] S·(2, 3) = (8, 13); (1, 1)·(8, 13) = 21 ✓.

## Dopo la pausa: g_S per vettori generici (50:26 – 59:00)
(tutte le lavagne cancellate; pannello in basso a destra, poi fatto scorrere in alto)
S MATRICE SIMMETRICA ∈ M(n)
⟹ g_S(v, w) = ᵗv S w prodotto scalare su ℝⁿ
**Es.** S = ( 1 2 ; 2 3 )
g_S(( x₁ ; x₂ ), ( y₁ ; y₂ )) = (x₁, x₂)·( 1 2 ; 2 3 )·( y₁ ; y₂ ) = (x₁, x₂)·( y₁ + 2y₂ ; 2y₁ + 3y₂ ) = x₁y₁ + 2x₁y₂ + 2x₂y₁ + 3x₂y₂
(a ≈ 53:40 – 55:00 il docente cerchia con colori diversi i coefficienti 1, 2, 2, 3 nella matrice, nel vettore intermedio e nel risultato)
IN generale, data S = ( a₁₁ … a₁ₙ ; ⋮ ; aₙ₁ … aₙₙ )
⟹ g_S(( x₁ ; ⋮ ; xₙ ), ( y₁ ; ⋮ ; yₙ )) = Σ_{i=1}^{n} Σ_{j=1}^{n} aᵢⱼ xᵢ yⱼ
**Oss.** se S = Iₙ ⟹ g_S(v, w) = ᵗv Iₙ w = ᵗv·w
⟹ g_{Iₙ} è il prodotto scalare euclideo

[a voce] (≈ 50:26 – 52:40) Ripresa: per ogni matrice simmetrica si è introdotto un prodotto scalare; ora lo si calcola su due vettori generici, sviluppando con la distributività.
[a voce] (≈ 53:18 – 55:02) I coefficienti del risultato sono esattamente le entrate della matrice: l'entrata in riga i e colonna j diventa il coefficiente di xᵢ yⱼ (l'1 in alto a sinistra va con x₁y₁, il 2 in riga 1 colonna 2 con x₁y₂, il 2 in riga 2 colonna 1 con x₂y₁, il 3 con x₂y₂).
[a voce] (≈ 56:48 – 57:21) Si scrivono tutti i termini xᵢyⱼ con i e j qualunque, ciascuno con coefficiente l'entrata di riga i e colonna j, e si somma: «for i da 1 a n, for j da 1 a n».
[a voce] (≈ 58:00 – 58:35) Se S è l'identità, Iₙ·w = w e si ritrova ᵗv w: il prodotto scalare associato all'identità è l'euclideo.

[verifica] (x₁, x₂)·S·(y₁, y₂) = x₁y₁ + 2x₁y₂ + 2x₂y₁ + 3x₂y₂ ✓; g_S(eᵢ, eⱼ) = Sᵢⱼ per S simmetrica 3 × 3 generica ✓.

## Tabella dei paralleli ENDOMORFISMI | PRODOTTI SCALARI (50:26 – 95:55)
(pannello in alto a sinistra, intestazione e riga verticale già scritte a 50:26; righe aggiunte a 60:20 – 62:20, 66:40 – 67:00, 75:20 – 76:20, 77:40 – 80:40; a ≈ 77:40 e ≈ 91:20 le ultime righe passano nel pannello sotto)
| ENDOMORFISMI | PRODOTTI SCALARI |
|---|---|
| T: V → V, T lineare | g: V × V → ℝ, bilineare simmetrica |
| A ∈ M(n) ⇝ L_A: 𝕂ⁿ → 𝕂ⁿ | S ∈ S(n) ⇝ g_S: ℝⁿ × ℝⁿ → ℝ |
| A = Iₙ ⇝ L_{Iₙ} = I_{𝕂ⁿ} | S = Iₙ → g_S = prod. Euclideo |
| T: V → V, B base ⇝ [T]^B_B | g: V × V → ℝ, B = {v₁, …, vₙ} base ⟹ [g]_B ∈ S(n) |
| V = 𝕂ⁿ, B = {e₁, …, eₙ} ⟹ [L_A]^B_B = A | V = ℝⁿ, B = {e₁, …, eₙ} ⟹ [g_S]_B = S |
| T: V → V, B ⊆ V base ⟹ ∀ v ∈ V, [Tv]_B = [T]^B_B [v]_B | g: V × V → ℝ, B ⊆ V base ⟹ g(v, w) = ᵗ[v]_B [g]_B [w]_B |

[a voce] (≈ 59:46 – 61:38) Tempo di vedere i paralleli fra la teoria degli endomorfismi e quella dei prodotti scalari: un endomorfismo è una mappa da uno spazio in se stesso, un prodotto scalare una mappa da V × V in ℝ bilineare e simmetrica; una matrice n × n dà un endomorfismo, una matrice simmetrica un prodotto scalare; l'identità dà l'identità, rispettivamente il prodotto euclideo.
[a voce] (≈ 61:38 – 62:49) Per gli endomorfismi c'era anche la mappa inversa: da un endomorfismo e una base si ottiene la matrice associata. Si può fare lo stesso con i prodotti scalari.

## Matrice associata a un prodotto scalare (62:40 – 68:00)
(pannello in basso a destra, poi fatto scorrere in alto)
**Def.** (MATRICE ASSOCIATA) V sp. vett. su ℝ, g: V × V → ℝ prod. scalare, B = {v₁, …, vₙ} base di V
⇝ LA MATRICE associata a g nella base B è
S = [g]_B data da
Sᵢⱼ = g(vᵢ, vⱼ)
**Oss.** Sⱼᵢ = g(vⱼ, vᵢ) = g(vᵢ, vⱼ) = Sᵢⱼ ⟹ [g]_B ∈ S(n) (sopra [g]_B una S)

[a voce] (≈ 62:49 – 64:55) Dato un qualunque spazio vettoriale reale, un qualunque prodotto scalare e una base, si costruisce la matrice associata: l'entrata in riga i e colonna j è g(vᵢ, vⱼ). «Facciamo tutti i possibili prodotti scalari fra gli elementi della base e li mettiamo in una matrice.»
[a voce] (≈ 64:55 – 66:31) Per la proprietà 3 (simmetria) g(vⱼ, vᵢ) = g(vᵢ, vⱼ): la simmetria del prodotto scalare fa sì che la matrice associata sia simmetrica.

## Matrice associata a g_S nella base canonica (67:40 – 76:40)
(pannello in alto a destra, sotto l'Oss. precedente)
**Oss.** V = ℝⁿ, S ∈ S(n), B = {e₁, …, eₙ} base canonica
B = [g_S]_B = ? ⇝ (conti) ⇝ B = [g_S]_B = S
(la lettera B indica qui la matrice incognita, non la base; il «⇝ B = [g_S]_B = S» è scritto a ≈ 74:20 – 74:40)

(pannello in basso a sinistra, scritto a 69:20 – 73:40)
Bᵢⱼ = g_S(eᵢ, eⱼ) = ᵗeᵢ S eⱼ
= (0, …, 1, …, 0)·( S₁₁ … S₁ₙ ; ⋮ ; Sₙ₁ … Sₙₙ )·( 0 ; ⋮ ; 1 ; ⋮ ; 0 ) (l'1 della colonna in posizione j, con una freccia «j»; l'1 della riga in posizione i)
= (0, …, 1, 0, 0)·( S₁ⱼ ; S₂ⱼ ; ⋮ ; Sₙⱼ ) = Sᵢⱼ

[a voce] (≈ 67:13 – 69:10) Data S simmetrica si costruisce g_S; dato un prodotto scalare si costruisce la matrice associata: quanto vale la matrice associata a g_S nella base canonica? «Chiamiamola B.»
[a voce] (≈ 70:48 – 73:10) S·eⱼ estrae la j-esima colonna di S (gli altri elementi sono moltiplicati per 0); poi la riga ᵗeᵢ prende l'i-esimo elemento di quella colonna: Sᵢⱼ. Due matrici con le stesse entrate sono uguali.
[a voce] (≈ 73:44 – 76:32) **Come sottolineato a lezione:** partendo da S, costruendo g_S e prendendone la matrice nella base canonica si torna a S: le due costruzioni (matrice simmetrica → prodotto scalare, prodotto scalare → matrice associata) sono una l'inversa dell'altra, almeno con la base canonica. È l'analogo di [L_A]^C_C = A per gli endomorfismi.

[verifica] g_S(eᵢ, eⱼ) = Sᵢⱼ ✓ (è il Corollario 19.9 / Esempio 19.13 delle dispense).

## Prop.: g(v, w) = ᵗ[v]_B [g]_B [w]_B ed esempio (79:00 – 95:55)
(pannello in basso a destra, poi fatto scorrere in alto a ≈ 82:20)
**Prop.** g: V × V → ℝ, B = {v₁, …, vₙ} base di V
⟹ g(v, w) = ᵗ[v]_B · [g]_B · [w]_B
(riquadrata a ≈ 93:00 – 93:20)
**Es.** S = ( 1 2 ; 2 3 ) ⇝ g_S: ℝ² × ℝ² → ℝ
g_S(( x₁ ; x₂ ), ( y₁ ; y₂ )) = x₁y₁ + 2x₁y₂ + 2x₂y₁ + 3x₂y₂
Data la base B = { ( 0 ; 1 ), ( 1 ; 1 ) } calcoliamo [g_S]_B (sotto i due vettori: v₁, v₂)

(pannello in basso a destra, scritto a 83:20 – 88:20, poi fatto scorrere in alto)
[g_S]_B = ( g_S(v₁, v₁) g_S(v₁, v₂) ; g_S(v₂, v₁) g_S(v₂, v₂) ) = ( 3 5 ; 5 8 )
(una freccia da g_S(v₂, v₁) a g_S(v₁, v₂): sono uguali)
g_S(v₁, v₁) = g_S(( 0 ; 1 ), ( 0 ; 1 )) = 3 — con due strade indicate: «(0, 1)·( 1 2 ; 2 3 )·( 0 ; 1 )» oppure «usare formula dove x₁ = y₁ = 0 e x₂ = y₂ = 1»
g_S(v₁, v₂) = g_S(( 0 ; 1 ), ( 1 ; 1 )) = 0 + 0 + 2 + 3 = 5
g_S(v₂, v₂) = g_S(( 1 ; 1 ), ( 1 ; 1 )) = 1 + 2 + 2 + 3 = 8
(i risultati 3, 5, 8 cerchiati)

(pannello in basso a sinistra, scritto a 89:00 – 94:40, poi fatto scorrere in alto)
**Oss.** Nell'esempio precedente, con v = ( 2 ; 3 ), w = ( 1 ; 2 )
Calcoliamo g_S(v, w) = 2 + 2·4 + 2·3 + 3·6 = 34
[v]_B = ( 1 ; 2 ) v = ( 2 ; 3 ) = 1·( 0 ; 1 ) + 2·( 1 ; 1 )
[w]_B = ( 1 ; 1 ) w = ( 1 ; 2 ) = 1·( 0 ; 1 ) + 1·( 1 ; 1 )
⟹ g(v, w) = (1, 2)·( 3 5 ; 5 8 )·( 1 ; 1 ) = (1, 2)·( 8 ; 13 ) = 8 + 26 = 34
(il 34 in alto, scritto a ≈ 91:00, a 94:00 è trasformato in **36** e a 94:20 è di nuovo 34: vedi la nota a voce)

[a voce] (≈ 76:32 – 79:44) Ultima cosa: con la matrice associata si può calcolare il prodotto scalare, come per gli endomorfismi si calcolava [Tv]_B = [T]^B_B [v]_B: g(v, w) = vettore delle coordinate di v trasposto, per la matrice associata, per il vettore delle coordinate di w.
[a voce] (≈ 82:55 – 85:34) Con la base canonica non ci sarebbe stato nessun conto da fare; con B ogni entrata si può calcolare in due modi, con ᵗv₁ S v₁ oppure con la formula sostituendo x₁ = y₁ = 0, x₂ = y₂ = 1: «i due risultati devono venire uguali».
[a voce] (≈ 86:21 – 87:43) g_S(v₂, v₁) = g_S(v₁, v₂) per la simmetria del prodotto scalare, quindi non va ricalcolato.
[a voce] (≈ 93:31 – 94:08) Momento di confusione: «che venga 34 come prima? 36?»; qualcuno legge il risultato in alto come 36, il docente ritocca la cifra («mi fido, c'era qualche errore di sicuro»), poi il conto con le coordinate dà 8 + 26 = 34 e il 34 in alto viene ripristinato.
[a voce] (≈ 94:44 – 95:26) **Come sottolineato a lezione:** negli esercizi del corso questi conti sono sempre facili (matrici, numeri), ma nella «vita vera» la parte astratta, il calcolo di un prodotto scalare, coinvolge spesso integrali e può essere molto difficile, mentre il calcolo con le matrici è ciò che i computer fanno bene. Poi i saluti (non visibili nel video, che finisce a 95:55).

(La Prop. non è dimostrata alla lavagna.)

[verifica] g_S(v₁, v₁) = 3, g_S(v₁, v₂) = 5, g_S(v₂, v₂) = 8, quindi [g_S]_B = ( 3 5 ; 5 8 ) ✓; anche ᵗM S M con M = ( 0 1 ; 1 1 ) (colonne v₁, v₂) dà ( 3 5 ; 5 8 ) ✓ (formula del cambio di base, dispense §20, non fatta a lezione). g_S((2, 3), (1, 2)) = 2 + 8 + 6 + 18 = 34 ✓; [v]_B = (1, 2), [w]_B = (1, 1) ✓; (1, 2)·( 3 5 ; 5 8 )·(1, 1) = (1, 2)·(8, 13) = 34 ✓.

Non sono svolti alla lavagna: la verifica che il prodotto scalare sui polinomi soddisfa le proprietà e che è definito positivo (lasciata come esercizio a voce); la Prop. 19.3 (definito positivo ⟹ non degenere); esempi di prodotti scalari degeneri o non definiti positivi; la dimostrazione della Prop. g(v, w) = ᵗ[v]_B [g]_B [w]_B (c'è solo la verifica numerica); norma, distanza, angolo (solo il riquadro «= ‖v‖ ‖w‖ cos θ» nell'esempio euclideo).

## Confronto con le dispense (sezione 19)
Solo alla lavagna (non nelle dispense):
- la motivazione (lunghezze, distanze, angoli, aree; teoria dei segnali, polinomi ortogonali) e la spiegazione del perché 𝕂 = ℝ (ordine, «r > 0»): le dispense dicono solo che si usano l'ordine e la radice quadrata;
- la dimostrazione della 2' a partire da 1, 2, 3 (le dispense dicono solo «da (1), (2), (3) segue anche»);
- l'esempio euclideo (1, 1, 2)·(−1, −1, 1) = 0 e il riquadro ⟨v, w⟩ = v • w = ‖v‖ ‖w‖ cos θ (nelle dispense l'esempio è (1, 3)·(−2, 1) = 1 e il coseno arriva solo nella sez. 20.E);
- la dimostrazione della Prop. 19.6 (euclideo definito positivo), che le dispense enunciano senza dimostrazione;
- la dimostrazione esplicita della simmetria di g_S con la trasposta di una matrice 1 × 1 (nelle dispense è la stessa catena, scritta in una riga);
- l'esempio S = ( 1 2 ; 2 3 ) con g_S((1, 1), (2, 3)) = 21, la forma generale x₁y₁ + 2x₁y₂ + 2x₂y₁ + 3x₂y₂, la matrice associata nella base {(0, 1), (1, 1)} = ( 3 5 ; 5 8 ) e la verifica con v = (2, 3), w = (1, 2) (34 in due modi);
- la tabella dei paralleli endomorfismi | prodotti scalari;
- il calcolo di g_S(eᵢ, eⱼ) = Sᵢⱼ scritto con i vettori della base canonica.

Solo nelle dispense (non alla lavagna):
- l'osservazione ⟨v, 0⟩ = 0 e la notazione g(v, w) introdotta come nome alternativo di ⟨v, w⟩ (alla lavagna g compare direttamente con g_S e con la matrice associata);
- la Prop. 19.3 (un prodotto scalare definito positivo non è degenere) con la spiegazione;
- l'Esempio 19.4 completo: definito positivo sui polinomi con il motivo (un polinomio non nullo di grado ≤ 2 non si annulla in tre punti distinti), più i due prodotti p(0)q(0) + p(1)q(1) (degenere, con p = x(1 − x)) e p(0)q(0) + p(1)q(1) − p(2)q(2) (non degenere ma non definito positivo, con p = x − 1);
- l'Esempio 19.11 (S = ( 2 1 ; 1 1 ), g_S = 2x₁y₁ + x₁y₂ + x₂y₁ + x₂y₂) e l'Esempio 19.14 (euclideo nella base {(1, 0), (1, 1)}: ( 1 1 ; 1 2 ));
- la Prop. 19.15 (g(v, w) = Σ λᵢ μⱼ g(vᵢ, vⱼ), per bilinearità), da cui il Cor. 19.16, che alla lavagna è la Prop. finale senza dimostrazione.

Differenze di notazione e di convenzione:
- dispense: Sᵢⱼ nella formula Σ xᵢ Sᵢⱼ yⱼ; lavagna: aᵢⱼ (Σ aᵢⱼ xᵢ yⱼ) per l'entrata di S.
- lavagna: la matrice incognita nell'Oss. sulla base canonica è chiamata B, come la base; nelle dispense è [g_S]_C = S (Esempio 19.13), con C base canonica.
- la definizione di **degenere** alla lavagna è «∃ v ∈ V t.c. ⟨v, w⟩ = 0 ∀ w ∈ V», **senza v ≠ 0**; le dispense (Def. 19.2) scrivono «esiste v ≠ 0». Senza la condizione la definizione è vuota (v = 0 va sempre bene, perché ⟨0, w⟩ = 0), quindi va letta con v ≠ 0. Anche a voce (≈ 25:16 – 25:49) il docente dice «almeno un vettore» senza precisare.
- nelle dispense le proprietà dimostrate sono numerate (4), (5); alla lavagna 1', 2'.

## Controllo dei conti con SymPy
Script in cartella temporanea (`verifica_l19.py`). Risultati:
- (1, 1, 2)·(−1, −1, 1) = 0 ✓; (1, 3)·(−2, 1) = 1 (dispense) ✓.
- S = ( 1 2 ; 2 3 ): S·(2, 3) = (8, 13), g_S((1, 1), (2, 3)) = 21 ✓; g_S(x, y) = x₁y₁ + 2x₁y₂ + 2x₂y₁ + 3x₂y₂ ✓.
- [g_S]_B con B = {(0, 1), (1, 1)} = ( 3 5 ; 5 8 ) ✓ (anche come ᵗM S M).
- g_S((2, 3), (1, 2)) = 34; [v]_B = (1, 2), [w]_B = (1, 1); ᵗ[v]_B [g_S]_B [w]_B = 34 ✓.
- simmetria di g_S e g_S(eᵢ, eⱼ) = Sᵢⱼ per S simmetrica 3 × 3 generica ✓; additività e omogeneità del prodotto euclideo ✓.
- aggiunte per i capitoli (non in lezione): q_S(x) = x₁² + 4x₁x₂ + 3x₂², q_S(2, −1) = −1 < 0, quindi g_S con S = ( 1 2 ; 2 3 ) **non è definito positivo** (det S = −1, autovalori 2 ± √5); per S = ( 2 1 ; 1 1 ) q = x₁² + (x₁ + x₂)² ✓; euclideo nella base {(1, 0), (1, 1)} = ( 1 1 ; 1 2 ) ✓; esempi sui polinomi: x(1 − x) vale 0, 0, −2 in 0, 1, 2 e (x − 1) dà 1 + 0 − 1 = 0 ✓.

Errori e sviste del docente:
- **definizione di degenere (≈ 25:40 – 26:40)**: manca «v ≠ 0» (vedi sopra); a voce nessuna precisazione; la lavagna viene cancellata a ≈ 37:00 senza correzioni.
- nella Dim. della Prop. sull'euclideo l'ultimo termine di ⟨v, v⟩ sembra scritto «x_y²» invece di xₙ² (lettura incerta, scritto piccolo vicino al bordo).
- nell'Oss. sulla base canonica la matrice incognita è chiamata B come la base (solo notazione).
- **verifica finale (≈ 93:30 – 94:20)**: il risultato giusto g_S((2, 3), (1, 2)) = 34 viene per pochi secondi cambiato in 36 su indicazione dall'aula, poi ripristinato quando il conto con [v]_B, [w]_B dà 34. Il valore giusto è 34.
- nella Dim. dell'euclideo non è verificata la simmetria (proprietà 3), che è ovvia (xᵢyᵢ = yᵢxᵢ) ma andrebbe detta; per g_S è invece dimostrata.
- l'esempio S = ( 1 2 ; 2 3 ) è chiamato «prodotto scalare» ed è corretto, perché nel corso un prodotto scalare è solo bilineare e simmetrico; però **non** è definito positivo (q_S(2, −1) = −1): alla lavagna non è detto, e nella stessa lezione il docente aveva detto che i prodotti interessanti per la geometria sono quelli definiti positivi. Da segnalare nei capitoli.

## Punti di lettura incerta
Nessuna formula importante illeggibile. Letture incerte:
- l'ultimo quadrato in ⟨v, v⟩ = x₁² + x₂² + … (≈ 34:20 – 36:40): «x_y²» o «xₙ²», scritto piccolo; a voce (≈ 33:39 – 34:17) il docente dice «il prodotto della ennesima».
- a ≈ 36:07 uno studente segnala «un due» sbagliato e il docente ringrazia: non si capisce dalla lavagna a quale scritta si riferisca (forse a un pedice).
- il titolo: la fine «I» è leggibile solo a 00:20 – 06:00, poi è coperta dal proiettore; la riga «⚠ Oggi 𝕂 = ℝ (poiché possiamo parlare di "r > 0")» è leggibile per intero solo a 04:00 – 06:00.
- nella tabella dei paralleli, la colonna di destra è in parte coperta dal proiettore in molti fotogrammi; letta per intero a 61:40 – 62:20 e 67:40.
- nell'Oss. sulla base canonica il vettore riga (0, …, 1, …, 0) ha l'1 in posizione i indicata da una freccia piccola.

## Note sulla trascrizione audio
Trascrizione completa `algebra_L19_2025.txt` (≈ 00:01 – 95:26): qualità medio-bassa, con le solite storpiature (vedi convenzioni; inoltre «matrice di Parthens / barbensia» = matrice di partenza) e qualche frase ripetuta (≈ 07:51 – 08:22). L'ordine degli argomenti coincide con la lavagna; è stata utile per la motivazione iniziale, per la scelta di 𝕂 = ℝ, per l'annuncio del parallelo endomorfismi ↔ matrici quadrate / prodotti scalari ↔ matrici simmetriche, per la conferma del taglio della pausa, per l'esercizio lasciato sul prodotto dei polinomi, per il commento «le due costruzioni sono inverse» sulla base canonica e per spiegare il 36 comparso per pochi secondi nella verifica finale.
