# Algebra lineare, Lezione 17: Autovalori e autovettori I (lavagne dalla registrazione Webex del 2025, prof. Radeschi)

Fonte: video della registrazione Webex del 7 nov 2025, file `audio/algebra_L17_2025.mp4` (84 min 31 s, 1920×1080). **La pausa è tagliata dal video**: nel fotogramma di 52:48 le lavagne sono ancora tutte piene (il docente indica «A = PDP⁻¹» del riassunto), in quello di 52:50 sono già tutte cancellate; dopo la pausa il docente riparte con «COME CALCOLARE AUTOVALORI» (≈ 54:40). Il video comincia con lo schermo nero e il titolo già scritto; finisce a 84:31 subito dopo l'esempio della rotazione (λ = ±i in ℂ), senza saluti visibili.
**Trascrizione audio:** al momento della stesura esiste solo un file parziale, `trascrizioni/algebra_L17_2025.part`, che arriva fino a ≈ 35:30. Le note [a voce] ci sono quindi solo per la prima metà della prima parte; dopo 35:30 la trascrizione è fatta **solo dalle lavagne**.
Fotogrammi estratti ogni 20 s (254, da 00:00 a 84:20), in una cartella temporanea. La lavagna è in 4 pannelli scorrevoli (alto/basso, sinistra/destra). **Sono stati letti tutti i 254 fotogrammi**, in 64 tavole di 4 fotogrammi consecutivi ridotti a metà (800×450), controllando per ogni pannello l'ultimo stato prima di cancellazioni e scorrimenti. Ritagli ingranditi a piena risoluzione per le scritte piccole a: 07:20, 09:00, 10:00, 11:20, 12:40, 15:40, 18:20, 19:20, 21:40, 26:40, 27:40, 31:40, 34:00, 36:20, 39:00, 42:20, 46:40, 50:40, 52:20, 52:40, 62:20, 64:20, 69:00, 73:20, 77:40, 84:20. Fotogrammi aggiuntivi: ogni 2 s da 52:40 a 53:00 (per localizzare il taglio della pausa), ogni 10 s a 1920 px da 75:30 a 76:40 (riquadro con p(t)), e a 84:25 e 84:30 (fine del video).

Convenzioni (come per L14 – L16):
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss); coincidono con quelli dell'audio, perché la pausa è tagliata sia nel video sia nell'audio.
- **[a voce]** indica ciò che è solo detto e non scritto; tra parentesi il tempo dell'audio (dalla trascrizione parziale, fiducia bassa: «autodutto» = autovettori, «indomorfismo / endomorphismo» = endomorfismo, «diavonata» = diagonale, «mille ronde» = mille volte).
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali.
- Sulla lavagna le basi sono scritte in corsivo (ℬ, 𝒞); qui B, C. La matrice associata è [f]^B_C: **base di partenza in alto, base di arrivo in basso** (come in L16). «( a b ; c d )» indica la matrice con righe (a b) e (c d), «( a ; b )» il vettore colonna; alcune matrici sono scritte con parentesi quadre, qui rese allo stesso modo. «[λ₁ ⋱ λₙ]» è la matrice diagonale con λ₁, …, λₙ sulla diagonale (alla lavagna: λ₁ in alto a sinistra, λₙ in basso a destra, puntini in mezzo, spazi vuoti per gli zeri).
- La variabile del polinomio caratteristico alla lavagna è **t**; le radici sono chiamate λ.

## Titolo e domanda (00:00 – 03:00)
**LEZIONE 17: AUTOVALORI & AUTOVETTORI** (titolo già scritto a 00:20; nei fotogrammi successivi la fine è coperta dal proiettore)
f : V ⟶ V   **Q:** Come agisce f?
Come agisce f∘f∘f∘f∘…∘f? (una graffa sotto la composizione, con scritto K: f composta K volte)

[a voce] (≈ 00:09 – 02:32) Concetto nuovo e fondamentale; prima di definirlo si vuole capire perché interessa. Si parte da un endomorfismo (mappa lineare da uno spazio in se stesso): ci si chiede che tipo di azione ha sullo spazio e che cosa succede applicando la stessa trasformazione più e più volte (richiamo alla fine di L16).

## Primo esempio: una matrice diagonale (03:00 – 07:40)
A = ( 1 0 ; 0 ½ )   L_A : ℝ² ⟶ ℝ²
L_A( x ; y ) = ( 1 0 ; 0 ½ )·( x ; y ) = ( x ; ½y )
Disegno (pannello sotto): assi cartesiani, etichetta ℝ²; un punto ( x ; y ) in alto, un segmento verticale che scende all'asse delle x (segnato x), e a metà del segmento il punto ( x ; y/2 ).
L_A ∘ L_A ∘ L_A ∘ L_A ∘ … ∘ L_A ( x ; y ) = ( x ; y/2¹⁰⁰⁰ ) (graffa sotto la composizione: 1000)

[a voce] (≈ 03:04 – 03:39) Si pensa a una matrice come alla mappa che prende un punto di coordinate (x, y) e lo manda nel prodotto della matrice per (x, y).
[a voce] (≈ 04:20 – 05:37) La mappa tiene la stessa coordinata x e divide per due la y: «schiaccia tutto il piano» verso l'asse delle x.
[a voce] (≈ 05:37 – 06:40) A ogni iterazione la y viene divisa per 2: y/2, y/4, y/8, …; dopo mille volte y/2¹⁰⁰⁰. Accenno: «al limite» la mappa diventa la proiezione sull'asse x (non lo si farà).
[a voce] (≈ 06:40 – 07:16) **Come sottolineato a lezione:** che cosa rendeva facile il calcolo? La matrice è **diagonale**, quindi manda x in un multiplo di x e y in un multiplo di y.

[verifica] ( 1 0 ; 0 ½ )·(x, y) = (x, y/2); ( 1 0 ; 0 ½ )¹⁰⁰⁰ = ( 1 0 ; 0 2⁻¹⁰⁰⁰ ). ✓

## Secondo esempio: ( 1 2 ; 2 1 ) nella base B = {(1, 1), (1, −1)} (07:40 – 22:40)
(pannello in basso a sinistra, separato da una riga orizzontale dal disegno precedente)
A = ( 1 2 ; 2 1 )   L_A : ℝ² ⟶ ℝ²
( x ; y ) ⟼ ( 1 2 ; 2 1 )·( x ; y ) = ( x + 2y ; 2x + y )

(pannello in basso a destra, poi fatto scorrere in alto)
B = { ( 1 ; 1 ), ( 1 ; −1 ) }   v₁ = ( 1 ; 1 ), v₂ = ( 1 ; −1 )
[L_A]^B_B = ( −1 · ; · +3 ) ⇝ L_A(v₁) = 3v₁ ; L_A(v₂) = −v₂ (stato a 12:40 – 20:40)
(**correzioni successive:** a 10:00 – 11:00 la matrice è scritta ( 1 · ; · −3 ) con L_A(v₁) = v₁, L_A(v₂) = −3v₂; a ≈ 11:00 – 11:40 il docente cancella e scrive ( −1 · ; · +3 ) con L_A(v₁) = 3v₁, L_A(v₂) = −v₂; a ≈ 21:00 cancella di nuovo i coefficienti delle due righe a destra e scrive L_A(v₁) = −v₁, L_A(v₂) = 3v₂, che resta fino alla cancellazione del pannello a ≈ 46:00. La matrice resta ( −1 · ; · +3 ).)

Disegno (sotto): assi cartesiani; la retta tratteggiata di v₁ (bisettrice) e il vettore v₁; il vettore v₂ verso il basso a destra; un vettore v = a v₁ + b v₂ (scritto accanto), con le sue componenti a lungo v₁ e b lungo v₂ segnate con tratteggi; un'altra retta per l'origine (direzione di v₂ prolungata in alto a sinistra) e, in alto a sinistra, il punto L_A v con un rettangolo che ne indica le componenti.
⇝ [v]_B = ( a ; b )

(pannello sotto)
[L_A v]_B = [L_A]^B_B [v]_B = ( −1 · ; · 3 )·( a ; b ) = ( −a ; 3b )
⟹ L_A v = −a v₁ + 3b v₂ (sotto −a una piccola graffa)
⟹ ( L_A ∘ L_A ∘ L_A ∘ … ∘ L_A )(v) = (−1)¹⁰⁰⁰ a v₁ + 3¹⁰⁰⁰ b v₂ (graffa sotto la composizione: 1000; sotto (−1)¹⁰⁰⁰ una graffa con scritto 1)

[a voce] (≈ 07:16 – 08:30) Stessa domanda per ( 1 2 ; 2 1 ): algebricamente la funzione è scritta, ma che cosa faccia geometricamente «non si capisce».
[a voce] (≈ 09:06 – 09:48) «Viene un oracolo» e suggerisce di non usare la base canonica ma la base {(1, 1), (1, −1)}; si calcola la matrice associata da B in B («sappiamo come farlo») e il docente dà il risultato.
[a voce] (≈ 10:35 – 11:39) Prima legge L_A(v₁) = v₁ e L_A(v₂) = −3v₂, poi «chiedo scusa, il −1 è +3»: L_A(v₁) = 3v₁, L_A(v₂) = −v₂.
[a voce] (≈ 11:39 – 13:17) Nella base canonica non si capisce che cosa faccia la matrice; scegliendo questi due vettori è come considerare un sistema di assi girato di 45 gradi. Un vettore si scrive a v₁ + b v₂.
[a voce] (≈ 13:17 – 15:56) Con la formula delle volte scorse le coordinate di L_A v in B si ottengono moltiplicando la matrice associata per [v]_B; ne viene che la prima coordinata cambia segno e la seconda viene triplicata: la mappa «riflette e poi allontana nella direzione di v₂».
[a voce] (≈ 16:27 – 18:15) Iterando mille volte: si continua a cambiare segno alla prima coordinata e a moltiplicare per 3 la seconda. Con le coordinate della base canonica non si sarebbe capito niente; con una base più adatta è facile descrivere la mappa e le sue iterate.
[a voce] (≈ 18:54 – 20:04) **Come sottolineato a lezione:** qui la base giusta è stata data da un oracolo; il punto della lezione di oggi e della prossima è **come trovarla**. La proprietà fondamentale di questa base è che in essa la matrice è diventata **diagonale**; trovare una tale base è il processo chiamato **diagonalizzazione**.
[a voce] (≈ 20:04 – 21:49) Uno studente fa notare un'incoerenza; il docente ammette di aver «fatto un pasticcio» confondendo v₁ con v₂ (e corregge le due righe L_A(v₁), L_A(v₂)); poi un'altra osservazione e «dimentichiamoci di questo esempio, perché se dovessi mettermi a correggere…»: «spero che sia passato il concetto più che i conti, che sono a quanto pare tutti sbagliati». Il concetto: per capire un endomorfismo conviene trovare una base in cui si esprime con una matrice diagonale.

[verifica] A·v₁ = (3, 3) = 3v₁ e A·v₂ = (−1, 1) = −v₂, quindi **[L_A]^B_B = ( 3 0 ; 0 −1 )**, non ( −1 0 ; 0 3 ) come è scritto. Di conseguenza [L_A v]_B = ( 3a ; −b ), L_A v = 3a v₁ − b v₂ e L_A¹⁰⁰⁰(v) = 3¹⁰⁰⁰ a v₁ + (−1)¹⁰⁰⁰ b v₂ = 3¹⁰⁰⁰ a v₁ + b v₂. Alla lavagna i due autovalori sono scambiati tra v₁ e v₂ in tutte le righe tranne lo stato intermedio «L_A(v₁) = 3v₁, L_A(v₂) = −v₂», che era giusto ed è stato «corretto» in quello sbagliato a ≈ 21:00. Anche la descrizione a voce («riflette rispetto a v₂ e allontana nella direzione di v₂») segue la versione sbagliata: in realtà la mappa triplica nella direzione di v₁ e ribalta nella direzione di v₂. Il docente stesso dichiara sbagliati i conti (≈ 21:17 – 21:49 e ≈ 28:11); il messaggio (in una base di autovettori la matrice è diagonale e le iterate si calcolano subito) resta valido.

## Definizione di autovettore e autovalore; esempi (22:40 – 29:00)
(pannello in basso a sinistra, cancellato a 22:40; poi fatto scorrere in alto a 26:40)
**Def:** T : V ⟶ V endomorfismo. Un **AUTOVETTORE** di T è un v ∈ V, v ≠ 0, t.c.
T(v) = λv per qualche λ ∈ 𝕂
λ è detto **AUTOVALORE** associato a v.
**Es:** ( 1 2 ; 2 1 )·( 1 ; 1 ) = ( 3 ; 3 ) = 3·( 1 ; 1 ) ⟹ L_A( 1 ; 1 ) = 3·( 1 ; 1 )
(sotto il prodotto, con una freccia: L_A(v))
⟹ ( 1 ; 1 ) è autovettore di L_A, con autovalore 3

(pannello in basso a sinistra, scritto a 27:00 – 28:20)
L_A( 1 ; −1 ) = ( 1 2 ; 2 1 )·( 1 ; −1 ) = ( −1 ; 1 ) = (−1)·( 1 ; −1 ) ⟹ L_A(w) = −w
(sotto i due ( 1 ; −1 ) una graffa con scritto w)
⟹ w è un autovettore, con autovalore −1

[a voce] (≈ 22:29 – 23:53) Il vettore deve essere **non nullo** («è importante»: non vogliamo il vettore 0); λ è uno scalare qualsiasi del campo.
[a voce] (≈ 25:10) «In questo momento non sappiamo come calcolare gli autovettori», ma si prova con (1, 1).
[a voce] (≈ 28:11 – 29:28) **Come sottolineato a lezione:** i conti dell'esempio di prima «erano completamente sbagliati», ma i vettori trovati sono proprio quelli della base scelta dall'oracolo e gli autovalori sono proprio i numeri che compaiono sulla diagonale: «non è un caso, sarà la norma».

[verifica] ( 1 2 ; 2 1 )·(1, 1) = (3, 3) = 3·(1, 1) ✓; ( 1 2 ; 2 1 )·(1, −1) = (−1, 1) = −(1, −1) ✓. SymPy: autovalori 3 (autovettore (1, 1)) e −1 (autovettore (−1, 1), multiplo di (1, −1)).

## Non tutti gli endomorfismi ammettono autovettori: la rotazione (29:00 – 34:20)
(sotto la riga orizzontale, nello stesso pannello)
**NON TUTTI GLI ENDOMORFISMI AMMETTONO AUTOVETTORI**
**Es:** Rot_{π/2} : ℝ² ⟶ ℝ²
( x ; y ) ⟼ ( −y ; x )
Disegno: assi cartesiani; il vettore ( x ; y ) nel primo quadrante, con il segmento verticale y e il segmento orizzontale x sull'asse; il vettore ( −y ; x ) nel secondo quadrante, con il segmento verticale x e il segmento −y sull'asse; una freccia curva tra i due (rotazione).
Rot_{π/2}( x ; y ) non è mai un multiplo di ( x ; y )

[a voce] (≈ 29:28 – 29:59) Quasi ogni matrice ammette autovettori, ma la definizione è molto specifica e ci sono matrici che non ne hanno.
[a voce] (≈ 30:33 – 31:46) La rotazione di 90 gradi manda (x, y) nel vettore con prima coordinata −y e seconda x; per definizione l'immagine di ogni vettore non nullo non è parallela al vettore di partenza.
[a voce] (≈ 33:01) «Qualunque rotazione» (di angolo diverso da 0 e π, sottinteso) non ammette autovettori.
[a voce] (≈ 33:36 – 34:09) Anticipo: considerando la mappa da ℂ² in ℂ² invece che da ℝ² in ℝ² avrebbe autovalori; con autovalori e autovettori «sarà quasi forzata la mano» a usare i numeri complessi (ripreso alla fine della lezione).

## Endomorfismi diagonalizzabili (34:20 – 42:40)
(pannello in basso a sinistra, il pannello con la definizione di autovettore viene cancellato a 33:40 – 34:00)
**Def:** Un endomorfismo T : V ⟶ V è **DIAGONALIZZABILE** se ∃ B base di autovettori di T
**PROP:** Se B = {v₁, …, vₙ} ⊆ V è una base di autovettori di T allora [T]^B_B è diagonale.
**Dim:** [T]^B_B = [ [T(v₁)]_B … [T(vₙ)]_B ] = [ [λ₁v₁]_B … [λₙvₙ]_B ] =
(sotto il secondo uguale una freccia verso l'alto con scritto T vᵢ = λᵢ vᵢ)

(pannello in basso a destra, dopo aver cancellato a 38:40 il pannello «[L_A v]_B = …»)
λ₁v₁ = λ₁v₁ + 0·v₂ + … + 0·vₙ ⇝ [λ₁v₁]_B = ( λ₁ ; 0 ; ⋮ ; 0 )
λ₂v₂ = 0·v₁ + λ₂v₂ + … + 0·vₙ ⇝ [λ₂v₂]_B = ( 0 ; λ₂ ; 0 ; ⋮ ; 0 )
(i coefficienti λ₁, 0, …, 0 e 0, λ₂, …, 0 sottolineati)
⇝ [T]^B_B = [ λ₁ 0 … 0 ; 0 λ₂ … 0 ; ⋮ ⋱ ; 0 0 … λₙ ] ☒
**Oss:** [T]^B_B ha sulla diagonale gli autovalori di v₁, …, vₙ

[a voce] (≈ 34:09 – 35:28) Si definisce un endomorfismo diagonalizzabile se esiste una base di autovettori; ha senso per la proposizione che segue: se B è una base di autovettori, la matrice associata da B a B è diagonale. (La trascrizione parziale si ferma qui; da questo punto niente note a voce.)

## Il viceversa; il caso T = L_A e la forma A = PDP⁻¹ (42:40 – 52:49)
(pannello in basso a sinistra, cancellato a 42:40 – 43:20)
Vale anche l'opposto della prop sopra.
**PROP:** Se T : V ⟶ V ammette base B = {v₁, …, vₙ} t.c. [T]^B_B = [λ₁ ⋱ λₙ] allora:
1) vᵢ sono autovettori
2) T vᵢ = λᵢ vᵢ
3) T è diagonalizzabile.

(pannello in basso a destra, dopo aver cancellato a 46:00 – 46:20 il pannello con B = {(1, 1), (1, −1)} e il disegno; poi fatto scorrere in alto)
**Caso speciale:** T = L_A : 𝕂ⁿ ⟶ 𝕂ⁿ (sottolineato)
L_A è diagonalizzabile ⟺ ∃ B = {v₁, …, vₙ} base t.c.
[L_A]^B_B = D = [λ₁ ⋱ λₙ]
**RICORDIAMO:** C = base canonica
A = [L_A]^C_C = [I_V]^B_C · [L_A]^B_B · [I]^C_B = [I_V]^B_C · [L_A]^B_B · ( [I]^B_C )⁻¹
(l'indice C in alto di [I]^C_B è ripassato/cerchiato)

(pannello sotto, scritto a 49:40 – 52:20)
= P·D·P⁻¹ dove
P = [I]^B_C = [ v₁ | … | vₙ ], e D = [λ₁ ⋱ λₙ]
**Riassumendo:**
**PROP:** A ∈ M(n) è diagonalizzabile (cioè L_A è diagonalizzabile)
⟺ A = P D P⁻¹ con P = [ v₁ … vₙ ] ← matrice degli autovettori
D = [λ₁ ⋱ λₙ] ← matrice degli autovalori («autoval» sottolineato)

(Nota: la definizione di «matrice diagonalizzabile» è data solo così, tra parentesi: A è diagonalizzabile se lo è L_A. Le due proposizioni sono senza dimostrazione scritta; il passaggio A = [I_V]^B_C [L_A]^B_B ([I]^B_C)⁻¹ usa la formula del cambio di base di L16 e [L_A]^C_C = A.)

[verifica] Con l'esempio della lezione: P = ( 1 1 ; 1 −1 ) (autovettori in colonna) e D = ( 3 0 ; 0 −1 ) danno P D P⁻¹ = ( 1 2 ; 2 1 ) = A. ✓ (Con D = ( −1 0 ; 0 3 ), come alla lavagna nel secondo esempio, non torna: serve l'ordine degli autovalori uguale a quello degli autovettori in P.)

## Dopo la pausa: come calcolare gli autovalori (52:50 – 64:40)
(tutte le lavagne cancellate; pannello in basso a sinistra, poi fatto scorrere in alto)
**COME CALCOLARE AUTOVALORI** (sottolineato)
v autovettore di L_A : 𝕂ⁿ ⟶ 𝕂ⁿ se v ≠ 0 e
L_A(v) = A v = λv
⇕
λ è un autovalore di A, se ∃ v ≠ 0 t.c. A v = λv = λ I v
⟺ ∃ v ≠ 0 t.c. (A − λI)·v = 0 ⟺ Ker(A − λI) = { v | (A − λI)v = 0 } ≠ {0}
⟺ A − λI non è invertibile

(pannello in basso a sinistra, poi fatto scorrere in alto)
⟺ det(A − λI) = 0
⇓ (freccia ondulata)
Introduciamo una funzione
p_A(t) = det(A − tI) ⟵ **POLINOMIO CARATTERISTICO DI A**
Dalla discussione sopra, λ è un autovalore di A
⟺ λ è una radice di p_A(t)

(53:00 – 54:40: lavagne vuote, il docente parla senza scrivere.)

## Esempio: autovalori di ( 1 2 ; 2 1 ) (64:40 – 69:20)
(pannello in basso a destra, poi fatto scorrere in alto)
**Es:** calcoliamo gli autovalori di A = ( 1 2 ; 2 1 )
① Calcolare p_A(t) = det(A − tI) = det( ( 1 2 ; 2 1 ) − t( 1 0 ; 0 1 ) ) =
= det( 1−t 2 ; 2 1−t ) = (1 − t)(1 − t) − 2·2
= t² − 2t + 1 − 4
= t² − 2t − 3 (sottolineato)
② Calcoliamo le radici: λ² − 2λ − 3 = 0 ⟹ λ = (2 ± √(4 + 12))/2 = (2 ± 4)/2 → −1, 3

[verifica] det(A − tI) = t² − 2t − 3 = (t − 3)(t + 1); radici 3 e −1, gli stessi autovalori trovati «a mano» con (1, 1) e (1, −1). ✓

## Osservazioni sul polinomio caratteristico: 2 × 2 e triangolari (69:20 – 77:00)
(pannello in basso a destra, poi fatto scorrere in alto)
**Oss** (la O cerchiata)
① A − tI = ( a₁₁−t … a₁ₙ ; a₂₂−t ; ⋮ ; aₙ₁ … aₙₙ−t ) se A = ( a₁₁ … a₁ₙ ; ⋮ ; aₙ₁ … aₙₙ )
(cioè si sottrae t sulla diagonale)
② Se A = ( a b ; c d ) ⟹ **p_A(t)** (riquadrato) = det( a−t b ; c d−t ) = (a − t)(d − t) − bc
= t² − (a + d)t + ad − bc
**= t² − (tr A)·t + det A** (riquadrato)

(pannello sotto, scritto a 73:00 – 76:40)
③ Se A = ( a₁₁ * ; 0 aₙₙ ) è triangolare (diagonale a₁₁ … aₙₙ, * sopra, 0 sotto)
⟹ A − tI = ( a₁₁−t * ; 0 aₙₙ−t ) — è ancora triangolare
⟹ p_A(t) = det(A − tI) = (a₁₁ − t)(a₂₂ − t) ⋯ (aₙₙ − t)
⟹ Gli autovalori di A sono a₁₁, …, aₙₙ
(a destra un riquadro grande, scritto a ≈ 75:40, che contiene solo: p(t) = (t − 3)(t − 2)(t − 5); il resto del riquadro resta vuoto; lettura dell'ultimo fattore incerta, vedi in fondo)

[verifica] det( a−t b ; c d−t ) = t² − (a + d)t + (ad − bc) ✓. Per una triangolare 3 × 3 generica SymPy dà det(A − tI) = (a₁₁ − t)(a₂₂ − t)(a₃₃ − t) ✓. Nell'esempio: tr = 2, det = 1 − 4 = −3, quindi t² − 2t − 3 ✓.

## Il grado di p_A; la rotazione ha autovalori solo in ℂ (77:00 – 84:31)
(pannello in basso a sinistra, dopo aver cancellato a ≈ 77:00 il pannello «COME CALCOLARE AUTOVALORI»; poi fatto scorrere in alto)
**Oss:** Se A ∈ M(n)
⟹ p_A(t) è un polinomio di grado n.
(una riga orizzontale)
**Es:** Rot : ℝ² ⟶ ℝ², ( x ; y ) ⟼ ( −y ; x )
[Rot]^C_C = [ [Rot(e₁)]_C [Rot(e₂)]_C ] = [ Rot(e₁) | Rot(e₂) ] (sotto la C in basso una freccia con scritto «canonica»)
Rot e₁ = Rot( 1 ; 0 ) = ( 0 ; 1 )
Rot e₂ = Rot( 0 ; 1 ) = ( −1 ; 0 ) ⇝ [Rot]^C_C = [ 0 −1 ; 1 0 ] = A

(pannello in basso a sinistra)
p_A(t) = det[ −t −1 ; 1 −t ] = t² + 1
⟹ autovalori di A: λ² + 1 = 0 → λ² = −1   NO SOLUZ in ℝ
MA λ = ±i in ℂ

(Il video si interrompe qui, a 84:31.)

[verifica] Rot(1, 0) = (0, 1), Rot(0, 1) = (−1, 0), quindi [Rot]^C_C = ( 0 −1 ; 1 0 ); det( −t −1 ; 1 −t ) = t² + 1, nessuna radice reale, radici ±i in ℂ. ✓ (Coerente con la discussione delle 29:00 – 34:20: nessun autovettore reale.)

Non sono svolti alla lavagna: il calcolo degli autovettori a partire dagli autovalori (cioè del nucleo di A − λI; si ricava solo che Ker(A − λI) ≠ {0}); la dimostrazione del viceversa e della Prop. «A diagonalizzabile ⟺ A = PDP⁻¹»; l'invarianza del polinomio caratteristico per similitudine; nessun esempio 3 × 3 numerico.

## Confronto con le dispense (sezione 17)
Solo alla lavagna (non nelle dispense):
- la motivazione con le iterate: ( 1 0 ; 0 ½ ) e (x, y) ⟼ (x, y/2¹⁰⁰⁰), poi ( 1 2 ; 2 1 ) nella base {(1, 1), (1, −1)} con L_A¹⁰⁰⁰ (esempio con i conti sbagliati, vedi sotto);
- gli esempi di autovettori (1, 1) (autovalore 3) e (1, −1) (autovalore −1) per ( 1 2 ; 2 1 ), e il calcolo del suo polinomio caratteristico t² − 2t − 3;
- la rotazione specifica di π/2, con la matrice ( 0 −1 ; 1 0 ) ricavata dalle immagini di e₁, e₂, il polinomio t² + 1 e gli autovalori ±i in ℂ;
- la catena di equivalenze scritta per esteso (λ autovalore ⟺ Ker(A − λI) ≠ {0} ⟺ A − λI non invertibile ⟺ det(A − λI) = 0);
- l'Oss. ② sul 2 × 2: p_A(t) = t² − (tr A)t + det A, e l'Oss. ③ sulle triangolari (autovalori = elementi diagonali);
- la scrittura A = P D P⁻¹ con P = [v₁ | … | vₙ] «matrice degli autovettori», ricavata dalla formula del cambio di base;
- il viceversa della Prop. scritto come proposizione separata con tre conclusioni (vᵢ autovettori, T vᵢ = λᵢ vᵢ, T diagonalizzabile).

Solo nelle dispense (non alla lavagna):
- Esempio 17.2 (A = ( 3 4 ; 0 2 ), autovettori e₁ con autovalore 3 e (−4, 1) con autovalore 2) e Esempio 17.4 (matrice 3 × 3, v = (0, 1, 1) e w = (0, 3, 3) con autovalore 2);
- l'osservazione che autovalori e autovettori si possono studiare in coordinate: T(v) = λv ⟺ Ax = λx con A = [T]^B_B e x = [v]_B;
- l'osservazione che i multipli non nulli di un autovettore sono autovettori con lo stesso autovalore (tutta la retta Span(v) tolto lo 0);
- la rotazione di angolo ϑ generico (ϑ ≠ 0, π) e l'Esempio 17.10 (per ϑ = 0, π la rotazione è ±id, diagonalizzabile);
- la Prop. 17.8 (T diagonalizzabile ⟺ [T]^B_B diagonalizzabile) con dimostrazione; gli Esempi 17.9 e 17.11 (A¹⁰⁰ per ( 3 4 ; 0 2 )); la sezione 17.C sui conti con le matrici diagonali (prodotto, determinante, potenze) — alla lavagna l'idea delle potenze c'è solo nella motivazione iniziale;
- l'invarianza del polinomio caratteristico per similitudine (con Binet) e la definizione di p_T per un endomorfismo; l'osservazione che p_A ha grado n c'è in entrambi;
- la Prop. 17.13 enunciata e dimostrata formalmente (alla lavagna è la «discussione sopra», con la stessa catena di equivalenze).

Differenze di notazione e di convenzione:
- variabile del polinomio caratteristico: dispense λ, p_A(λ) = det(A − λIₙ); lavagna t, p_A(t) = det(A − tI) (stesso segno: A − tI, non tI − A).
- Prop. 17.6 delle dispense è un «se e solo se» (B base qualsiasi: [T]^B_B diagonale ⟺ v₁, …, vₙ autovettori); alla lavagna sono due proposizioni separate (⟹ con dimostrazione, poi «vale anche l'opposto»).
- matrice diagonalizzabile: dispense Def. 17.7, A simile a una diagonale, D = M⁻¹AM; lavagna «A è diagonalizzabile (cioè L_A è diagonalizzabile) ⟺ A = PDP⁻¹» con P = [I]^B_C = [v₁ | … | vₙ]. È la stessa cosa con P = M (la M delle dispense è anch'essa [id]^B_C, Esempio 17.11).
- endomorfismo: dispense T o f indifferentemente; lavagna T nelle definizioni, f nella domanda iniziale.

## Controllo dei conti con SymPy
Script in cartella temporanea (`verifica_l17.py`). Risultati:
- ( 1 0 ; 0 ½ )·(x, y) = (x, y/2), ( 1 0 ; 0 ½ )¹⁰⁰⁰ = ( 1 0 ; 0 2⁻¹⁰⁰⁰ ): ✓.
- ( 1 2 ; 2 1 )·(x, y) = (x + 2y, 2x + y): ✓.
- A(1, 1) = 3(1, 1), A(1, −1) = −(1, −1): ✓ (esempi delle 25:00 – 28:40).
- **[L_A]^B_B con B = {(1, 1), (1, −1)} è ( 3 0 ; 0 −1 )**, non ( −1 0 ; 0 3 ) come alla lavagna; [L_A v]_B = (3a, −b), L_A¹⁰⁰⁰ v = 3¹⁰⁰⁰ a v₁ + b v₂ (lavagna: (−a, 3b) e (−1)¹⁰⁰⁰ a v₁ + 3¹⁰⁰⁰ b v₂): ✗.
- P D P⁻¹ = A con P = ( 1 1 ; 1 −1 ), D = ( 3 0 ; 0 −1 ): ✓.
- p_A(t) = t² − 2t − 3, radici −1 e 3, (2 ± √16)/2 = 3, −1: ✓.
- det( a−t b ; c d−t ) = t² − (a + d)t + ad − bc = t² − (tr A)t + det A: ✓.
- triangolare 3 × 3: det(A − tI) = (a₁₁ − t)(a₂₂ − t)(a₃₃ − t): ✓.
- Rot: [Rot]^C_C = ( 0 −1 ; 1 0 ), p(t) = t² + 1, nessun autovalore reale, ±i in ℂ: ✓.

Errori e sviste del docente:
- **secondo esempio (≈ 09:40 – 21:50):** la matrice associata a ( 1 2 ; 2 1 ) nella base {(1, 1), (1, −1)} è scritta prima ( 1 · ; · −3 ), poi ( −1 · ; · +3 ); quella giusta è ( 3 0 ; 0 −1 ). Le righe L_A(v₁) = 3v₁, L_A(v₂) = −v₂ (scritte a ≈ 11:20) erano giuste, ma a ≈ 21:00 vengono cambiate in L_A(v₁) = −v₁, L_A(v₂) = 3v₂ per accordarle alla matrice; di conseguenza sono sbagliati anche [L_A v]_B = (−a, 3b), L_A v = −a v₁ + 3b v₂ e la formula di L_A¹⁰⁰⁰ (v₁ e v₂ scambiati). Il docente lo riconosce a voce (≈ 20:40 – 21:49: «ho fatto un pasticcio… dimentichiamoci di questo esempio… i conti sono a quanto pare tutti sbagliati»; ≈ 28:11: «i conti lì erano completamente sbagliati»), ma **sulla lavagna l'errore resta** fino alla cancellazione dei pannelli (≈ 38:40 e ≈ 46:00). Chi ricopia l'esempio deve usare ( 3 0 ; 0 −1 ).
- nella formula A = [I_V]^B_C [L_A]^B_B [I]^C_B l'identità è scritta a volte I_V e a volte I (senza conseguenze).
- nella Prop. «Riassumendo» l'ordine di autovalori in D e autovettori in P deve corrispondere: non è scritto, ma è sottinteso (ed è proprio il punto sbagliato nel secondo esempio).
- nel titolo «NON TUTTI GLI ENDOMORFISMI AMMETTONO AUTOVETTORI» la parola «AUTOVETTORI» ha una lettera ripassata/corretta (non cambia il senso).
- a voce (≈ 33:01): «qualunque rotazione non ammette autovettori» va inteso per angoli diversi da 0 e π (le dispense lo precisano).

## Punti di lettura incerta
Nessuna formula importante illeggibile. Letture incerte:
- il riquadro a destra del pannello sulle triangolari (≈ 75:40 – 84:31) contiene solo «p(t) = (t − 3)(t − 2)(t − 5)»: l'ultimo fattore tocca il bordo del riquadro e potrebbe essere (t − 3); non si sa a che cosa servisse (il resto del riquadro è vuoto e la trascrizione audio non arriva fin lì); probabilmente un esempio detto a voce di polinomio caratteristico di una matrice triangolare con diagonale 3, 2, 5;
- il titolo: la fine «& AUTOVETTORI» è leggibile solo a 00:20 – 01:00, poi è coperta dal proiettore;
- nella matrice ( −1 · ; · +3 ) le posizioni fuori diagonale sono una macchia di cancellatura (si vedono il «−1» in alto a sinistra e il «+3» in basso a destra; gli zeri non sono scritti);
- nel disegno del secondo esempio (12:40 – 21:40) le lettere a e b accanto alle componenti di v sono piccole; la forma esatta del rettangolo che porta a L_A v è leggibile ma non è un disegno in scala;
- nella Dim della Prop. sulle basi di autovettori la scritta sotto il secondo uguale («T vᵢ = λᵢ vᵢ», con una freccia verso l'alto) è scritta piccola;
- nel disegno della rotazione l'etichetta sull'asse orizzontale sotto ( x ; y ) è letta «x» (scritta piccola, con un trattino sotto).

## Note sulla trascrizione audio
Al momento della stesura c'è solo il file parziale `algebra_L17_2025.part` (≈ 00:09 – 35:28): qualità media, con le solite storpiature («autodutto», «indomorfismo», «diavonata», «matavice / madrice», «2.000» per 2¹⁰⁰⁰). L'ordine degli argomenti coincide con la lavagna; è stata utile soprattutto per capire le correzioni del secondo esempio e la dichiarazione del docente che quei conti erano sbagliati. Per il resto della lezione (dalla Prop. sulle basi di autovettori in poi) le note [a voce] mancano: quando la trascrizione completa sarà pronta si possono aggiungere, in particolare per il riquadro con p(t) = (t − 3)(t − 2)(t − 5) e per quello che il docente dice sul viceversa e sulla forma A = PDP⁻¹.
