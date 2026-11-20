# Algebra lineare, Lezione 18: Autovalori e autovettori II (lavagne dalla registrazione Webex del 2024, prof. Radeschi)

Fonte: video della registrazione Webex del 15 nov 2024, file `audio/algebra_L18_2024.mp4` (100 min 48 s, 1600×900, risoluzione più bassa delle registrazioni 2025). **Trascrizione audio non disponibile** al momento della stesura (`trascrizioni/algebra_L18_2024.txt` non esiste ancora): questo file è ricavato **solo dalle lavagne**, quindi non ci sono note [a voce]; quando la trascrizione sarà pronta si potranno aggiungere.
**La pausa NON è tagliata dal video**: a 59:40 le lavagne sono quasi tutte cancellate e da 60:00 a ≈ 67:00 l'inquadratura resta sulle lavagne vuote (resta solo il pannello in alto a sinistra con Prop. e Cor. sugli autospazi). Durante la pausa, a ≈ 64:40, il docente aggiunge «distinti» al Corollario, e tra ≈ 65:20 e 66:20 scrive qualche segno nel pannello in basso a destra parlando con uno studente (vedi la sezione della pausa). La lezione riprende a ≈ 67:00 – 68:00 (a 68:40 si vede già «Def.»). Il primo fotogramma (00:00) è nero; dal secondo (00:20) le lavagne del richiamo sono già scritte. Il video finisce a 100:48 subito dopo la conclusione dell'ultimo esempio.
Fotogrammi estratti ogni 20 s (303, da 00:00 a 100:40), in una cartella temporanea. La lavagna è in 4 pannelli scorrevoli (alto/basso, sinistra/destra). Tutti i 303 fotogrammi sono stati guardati in 34 tavole di 9 fotogrammi ridotti (3×3, una ogni 3 minuti), per seguire gli scorrimenti e le cancellature; sono stati poi aperti come ritagli ingranditi dei pannelli, uno per ogni stato della lavagna prima che venisse cancellato o fatto scorrere: 01:00, 02:40, 03:20, 11:40, 14:40, 19:20, 26:20, 29:20, 30:00 (sinistra e destra), 34:40, 38:20, 41:40, 43:40, 47:20, 50:40, 55:40, 58:20, 64:40, 66:00, 66:40, 72:00, 74:20, 80:00, 85:20, 86:20, 88:20, 90:00, 92:40, 96:00, 98:00, 100:40 (sinistra e destra). Ogni pannello è stato letto completo prima di essere cancellato o fatto scorrere.

Convenzioni (come per L14 – L16):
- I tempi sono quelli dei fotogrammi (mm:ss), arrotondati a 20 s; la pausa non è tagliata, quindi dopo 60:00 i tempi includono i ≈ 7 minuti di pausa.
- **[a voce]**: nessuna nota di questo tipo, perché manca la trascrizione.
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Sulla lavagna le basi sono scritte con lettere corsive (ℬ); qui sono rese B. La matrice associata è [T]^B_B: **base di partenza in alto, base di arrivo in basso**. Il polinomio caratteristico è scritto P_A(t) (P maiuscola corsiva, variabile t), a volte P_T(t).
- Le matrici numeriche sono scritte a volte con parentesi tonde e a volte quadre; qui «( a b ; c d )» indica la matrice con righe (a b) e (c d), e «( a ; b )» il vettore colonna.
- «l.i.» = linearmente indipendenti; «diag'le» = diagonalizzabile; «aval» / «avett» = autovalore / autovettore (abbreviazioni della lavagna).

## Titolo e richiamo della lezione 17 (00:20 – 03:20)
(pannello in alto a sinistra; il titolo e la fine della prima riga sono in parte coperti dal proiettore, letti a 01:00 quando il pannello era abbassato)
**LEZIONE 18: AUTOVALORI/VETTORI II**
**Prev.** ① T : V → V ⇝ v ∈ V **AUTOVETTORE DI T** se T(v) = λv
(scritto prima «AUTOVALORE», poi «VALORE» cancellato e «VETT» scritto sopra)
A ∈ M(n) ⇝ v ∈ 𝕂ⁿ **AUTOVETTORE DI A**, se Av = λv
(anche qui «VALORE» cancellato, «ETTORE» scritto sopra)
② T **DIAG'LE** se ∃ B ⊆ V base, tc [T]^B_B = ( λ₁ ⋱ λₙ ) (matrice diagonale)
A **DIAG'LE** se ∃ P ∈ M(n) t.c. P A P⁻¹ = ( λ₁ ⋱ λₙ )
(una freccia curva parte dalle due righe) ⟺ ∃ **BASE DI AUTOVETTORI**

(pannello in basso a sinistra)
③ **Come trovo AUTOVALORI.**
P_A(t) = det(A − t I) **POLI. CARATTERISTICO**
λ autovalore di A ⟺ P_A(λ) = 0

(pannello in basso a destra, 02:20 – 03:20)
T : V → V ⇝ [T]^B_B = A
L_A : 𝕂ⁿ → 𝕂ⁿ ⇝ A
(frecce ondulate: a un endomorfismo con una base si associa una matrice, a una matrice la mappa L_A; questo pannello viene cancellato a ≈ 12:00)

Note di lettura:
- nella definizione di autovettore non è scritto v ≠ 0 (nelle dispense, Def. 17.1, sì);
- in ② non è scritto che P deve essere invertibile (è sottinteso da P⁻¹).

## Il polinomio caratteristico in casi speciali (08:20 – 15:20)
(a 07:40 – 08:40 i pannelli di sinistra scorrono; sotto ③ una riga orizzontale)
**P_A(t) in casi speciali:**
① A = ( a b ; c d ) ⇝ P_A(t) = det ( a−t b ; c d−t ) = (a − t)(d − t) − bc
= t² − dt − at + (ad − bc)
(sotto «− dt − at» una graffa con scritto «−(a + d) t», e una freccia da «tr A», scritto a sinistra; sotto «(ad − bc)» la scritta «det A»)

(pannello in basso a destra, ≈ 12:00, dopo aver cancellato il pannello del richiamo; la formula è riquadrata)
⇝ **P_A(t) = t² − (tr A) t + (det A)**

② A = ( a₁₁ … a₁ₙ ; ⋱ ⋮ ; 0 aₙₙ ) (triangolare superiore: «0» sotto la diagonale, una linea obliqua lungo la diagonale)
⇝ P_A(t) = det ( a₁₁−t … a₁ₙ ; ⋱ ⋮ ; 0 aₙₙ−t ) = (a₁₁ − t) ⋯ (aₙₙ − t)
(una freccia curva dal prodotto alla riga sotto)
**AUTOVALORI = elementi sulla diagonale**

[verifica] det ( a−t b ; c d−t ) = t² − (a + d)t + (ad − bc): coincide con t² − (tr A)t + det A. La formula vale per le 2 × 2 (per n × n il coefficiente di testa di det(A − tI) è (−1)ⁿ). Per una triangolare 3 × 3 di prova, ( 1 2 3 ; 0 4 5 ; 0 0 6 ), SymPy dà det(A − tI) = (1 − t)(4 − t)(6 − t). ✓

## Esempio: A = ( 2 1 ; 1 2 ), autovalori e autovettori (15:40 – 30:00)
(pannello in basso a destra, poi fatto scorrere in alto a ≈ 21:40)
**Es** A = ( 2 1 ; 1 2 )   **Autovalori? Autovett? Diag'le?**
(le tre domande sono sottolineate più tardi; «Diag'le?» è riquadrato a ≈ 43:40)
① P_A(t) = t² − 4t + 3 = (t − 1)(t − 3)
Radici: 1, 3 ⟹ Autovalori di A = 1, 3
② **λ = 1** (riquadrato)   v autovett con λ = 1 ⟺ Av = λ·v
Av − λv = 0 ⟺ (A − λI)·v = 0 (sotto v una lineetta: v è vettore)
A − 1I = ( 1 1 ; 1 1 ) (un pezzo cancellato con uno scarabocchio) se v = ( x ; y ) soddisfa (una freccia verso (A − λI)v = 0) allora
(a 30:00 una lunga parentesi quadra verticale raggruppa ① e ②)

(pannello sotto, poi in alto a destra)
[ 0 ; 0 ] = [ 1 1 ; 1 1 ] · [ x ; y ] = [ x + y ; x + y ] ⇝ { x + y = 0 ; x + y = 0 } (la seconda equazione barrata) ⇝ x = −y, y = libero
⇝ **AUTOVETTORI CON A VALORE 1** = { ( −y ; y ) | y ∈ 𝕂 } = Span ( −1 ; 1 )
(sotto ( −y ; y ) una graffa con scritto «y · ( −1 ; 1 )»)
**λ = 3** (sottolineato)   v = ( x ; y ) autovett. con A VAL = 3 ⟺ (A − 3I)v = 0

(pannello in basso a sinistra, 27:40 – 29:20, dopo aver cancellato il pannello ③)
A − 3I = [ −1 1 ; 1 −1 ] ⇝ [ 0 ; 0 ] = [ −1 1 ; 1 −1 ] [ x ; y ] = [ −x + y ; x − y ]
⇝ **AUTOVETT con (λ = 3)** = { ( x ; x ) | x ∈ 𝕂 } = Span ( 1 ; 1 )
(sotto ( x ; x ) una graffa con scritto «x · ( 1 ; 1 )»)

[verifica] P_A(t) = t² − 4t + 3 = (t − 1)(t − 3) (tr A = 4, det A = 3); A − I = ( 1 1 ; 1 1 ), nucleo Span(−1, 1); A − 3I = ( −1 1 ; 1 −1 ), nucleo Span(1, 1). ✓

## Esempio: la base di autovettori, A è diagonalizzabile (33:00 – 34:40)
(stesso pannello, sotto)
B = { ( 1 ; 1 ), ( −1 ; 1 ) } **BASE DI AUTOVETTORI DI A** (sopra «DI AUTOVETTORI», con una freccia, «di ℝ²») ⟹ **A diag'le**

[verifica] I due vettori sono indipendenti (det ( 1 −1 ; 1 1 ) = 2). Con P = ( 1 −1 ; 1 1 ) (autovettori in colonna) si ha P⁻¹ A P = ( 3 0 ; 0 1 ): diagonale con gli autovalori. ✓ (Alla lavagna non è scritta la matrice diagonale né la matrice P; il «perché» della conclusione è il punto ② del richiamo.)

## Autovettori con autovalori distinti (35:00 – 44:00)
(pannello in basso a sinistra, dopo aver cancellato il pannello del titolo a ≈ 35:00)
**PROP** T : V → V, v₁, …, v_k ∈ V autovettori di A
con a valori distinti
⟹ { v₁, …, v_k } sono l.i.
(una riga orizzontale)
**COR** T : V → V end. con n = dim V autovalori distinti
⟹ T diagonalizzabile
**"DIM"** (tra virgolette) A VAL λ₁, …, λₙ
(sotto ogni λᵢ una freccia ↳ vᵢ) ↳ v₁, …, ↳ vₙ avett. ⇝ { v₁, …, vₙ } l.i. (graffa sotto, freccia in giù) **base di autovett.** ☒

Note:
- nella Prop. è scritto «autovettori di **A**» anche se l'endomorfismo si chiama T (svista: va letto «di T»);
- nella riga del Cor. c'è un segno cancellato tra «con» e «n» (lettura incerta);
- la Prop. **non è dimostrata** alla lavagna; la «Dim» tra virgolette è solo quella del Corollario (n autovettori l.i. in uno spazio di dimensione n sono una base).
- 41:00 – 43:40: il docente indica di nuovo l'esempio di ( 2 1 ; 1 2 ) (due autovalori distinti in dimensione 2: il Cor. dà subito la diagonalizzabilità); nessuna scritta nuova a parte il riquadro su «Diag'le?».

## Autospazio e somma diretta (44:20 – 54:40)
(pannello in basso a destra, dopo aver cancellato l'esempio a ≈ 44:20; poi fatto scorrere in alto)
**Def.** T : V → V, λ autovalore
**AUTOSPAZIO DI λ** = { v ∈ V | Tv = λv }
V_λ = { v ∈ V | (T − λI)(v) = 0 }
= Ker (T − λI)
(una riga orizzontale)
**Def.** V ⊇ W₁, …, W_k sottospazi sono in **SOMMA DIRETTA** se
(pannello sotto)
0_V = w₁ + w₂ + … + w_k,  wᵢ ∈ Wᵢ
⟹ w₁ = 0_V = w₂ = … = w_k
(una riga orizzontale)
**PROP** Se V ⊇ W₁, …, W_k sotto sp. in somma diretta
tc ∀v = w₁ + w₂ + … + w_k,  wᵢ ∈ Wᵢ
⟹ Scelte basi B₁ ⊆ W₁, …, B_k ⊆ W_k
allora B = B₁ ∪ B₂ ∪ … ∪ B_k è base di V

Note:
- l'autospazio è scritto come insieme di **tutti** i v con Tv = λv, quindi contiene anche 0 (le dispense, Def. 18.3, lo dicono esplicitamente: «più l'origine»);
- la definizione di somma diretta è data direttamente nella forma «l'unica scrittura di 0 è quella banale» (nelle dispense, Def. 18.4, è la forma equivalente; la definizione principale è l'unicità della scrittura di ogni vettore);
- nella Prop. «tc ∀v = w₁ + … + w_k» va letto «tali che ogni v ∈ V si scrive come w₁ + … + w_k», cioè V = W₁ ⊕ … ⊕ W_k (la formulazione alla lavagna è abbreviata);
- nessuna dimostrazione della Prop.

## Gli autospazi sono in somma diretta; criterio di diagonalizzabilità (55:00 – 59:40)
(pannello in basso a sinistra, dopo aver cancellato il pannello dell'esempio λ = 3 a ≈ 54:40; poi fatto scorrere in alto)
**PROP** T : V → V endom, λ₁, …, λ_k (la fine della riga è vicina al proiettore; non si legge altro dopo λ_k)
⟹ V_λ₁, …, V_λk sono in somma diretta
**COR** T : V → V end, λ₁, …, λ_k autoval **distinti** («distinti», sottolineato, aggiunto durante la pausa, a ≈ 64:40)
⟹ T è diag ⟺ V = V_λ₁ + … + V_λk = { v₁ + … + v_k | vᵢ ∈ V_λᵢ }
⟺ dim V = dim V_λ₁ + … + dim V_λk
(sotto l'ultima riga una riga orizzontale, aggiunta a ≈ 72:00)

Note:
- nel Cor. λ₁, …, λ_k sono **tutti** gli autovalori di T (non è scritto, ma è necessario: se ne mancasse uno, la somma non potrebbe essere V);
- nessuna dimostrazione della Prop. né del Cor.

## Pausa (59:40 – ≈ 67:00, non tagliata)
A 58:40 – 59:40 il docente cancella tutti i pannelli tranne quello in alto a sinistra (Prop./Cor. sugli autospazi). Da 60:00 l'inquadratura resta sulle lavagne vuote.
- ≈ 64:40: aggiunge «distinti» nel Corollario (vedi sopra).
- ≈ 65:20 – 66:20, pannello in basso a destra, mentre parla con uno studente: W₁ … W_k, sotto ciascuno (con il segno ∪ ruotato, «contiene») B₁ … B_k, e sotto «Bᵢ ⊆ Wᵢ, i = 1, …, k» (è la Prop. sulle basi degli addendi di una somma diretta). Queste scritte vengono cancellate subito dopo.

## Molteplicità geometrica e algebrica (68:40 – 74:20)
(pannello in basso a sinistra, poi fatto scorrere in alto a ≈ 70:20)
**Def.** T : V → V, λ autovalore di T
[ ⟺ λ radice di P_A(t) ]
1) **LA MOLTEPLICITÀ GEOMETRICA** di λ
è m_g(λ) = dim V_λ
2) **LA MOLTEPLICITÀ ALGEBRICA** di λ
è m_a(λ) = molteplicità di λ, come radice di P_T(t)

(pannello in basso a destra)
cioè = m tale che P_T(t) = (t − λ)^m · q(t)
dove q(λ) ≠ 0
(una riga orizzontale)
**PROP:** m_g(λ) ≤ m_a(λ) (riquadrato)

Note:
- nella stessa definizione il polinomio è scritto una volta P_A(t) e una volta P_T(t) (per un endomorfismo T è il polinomio caratteristico di una qualunque matrice associata, come nelle dispense dopo la Prop. 17.13);
- la Prop. è scritta senza la prima disuguaglianza 1 ≤ m_g(λ) (che c'è nel Teorema 18.9 delle dispense) e senza dimostrazione.

## Teorema di diagonalizzabilità (74:40 – 80:40)
(pannello in basso a destra, poi fatto scorrere in alto a ≈ 78:40)
**TEOREMA DI DIAGONALIZZ.:** V sp. v. su 𝕂.
T : V → V è diagonalizzabile ⟺
a) P_T(t) ha esattamente n = dim V radici (sopra «radici», con una freccia, «in 𝕂», aggiunto più tardi: si vede da ≈ 82:20), contate con molteplicità
(sotto «dim V» un segno di uguale verticale e «deg P_T(t)»)
b) ∀λ autovalore, m_a(λ) = m_g(λ)

Nessuna dimostrazione. Il pannello resta visibile fino a 98:00 e viene cancellato a ≈ 98:20.

## Esempio: la rotazione A = ( 0 1 ; −1 0 ) (81:00 – 88:20)
(pannello in basso a sinistra, dopo aver cancellato Prop./Cor. sugli autospazi; poi fatto scorrere in alto a ≈ 85:40)
**Es.** A = [ 0 1 ; −1 0 ] ∈ M(2, ℝ) è diag? ⟷ L_A : ℝ² → ℝ²
(sotto ℝ² → ℝ² un piccolo disegno: due assi e un vettore ruotato, con una freccia curva: è una rotazione)
a) P_A(t) = t² − 0t + 1 = t² + 1 = 0 ↘ t² = −1
(lo «0» del termine in t è ripassato/cerchiato)
NO RADICI REALI ⟶ **A NO DIAG SU ℝ**
↳ Su ℂ, P_A(t) ha radici i, −i
A è 2 × 2 e ha 2 aval. distinti (graffa) ⟹ **A è diag'le su ℂ**

Note:
- la lettera «a)» rimanda alla condizione a) del Teorema: su ℝ è quella che fallisce;
- la conclusione su ℂ usa il Corollario delle 35:00 (n autovalori distinti ⟹ diagonalizzabile), non il Teorema.

[verifica] P_A(t) = t² + 1 (tr A = 0, det A = 1), radici ±i; su ℂ autovettori (−i, 1) per i e (i, 1) per −i; SymPy conferma che A è diagonalizzabile su ℂ. L_A(e₁) = (0, −1): è la rotazione di 90° in senso orario. ✓

## Osservazione: su ℂ la condizione a) vale sempre (88:40 – 90:00)
(pannello in basso a sinistra, poi fatto scorrere in alto)
**Oss:** se 𝕂 = ℂ allora la condizione ⓐ
è sempre verificata, per il
teorema fondam. dell'Algebra
(sottolineato)

## Esempio: A = ( 1 1 ; 0 1 ) non è diagonalizzabile (90:20 – 100:48)
(stesso pannello, sotto l'Oss.)
**ES.** A = [ 1 1 ; 0 1 ] è diag'le? (sotto, con una freccia, «su ℝ», aggiunto a ≈ 94:20)
P_A(t) = det [ 1−t 1 ; 0 1−t ] = (1 − t)² (l'esponente 2 cerchiato, con una freccia) ⟶ Aval = 1, m_a(1) = 2   (a) ✓

(pannello in basso a sinistra, 93:20 – 98:00, dopo aver cancellato l'esempio della rotazione)
**Calcoliamo** m_g(1) = dim V₁
V₁ = { ( x ; y ) ∈ ℝ² | (A − I)( x ; y ) = ( 0 ; 0 ) }
‖
Ker (A − I)      A − I = ( 0 1 ; 0 0 )
( 0 ; 0 ) = ( 0 1 ; 0 0 )( x ; y ) = ( y ; 0 ) ⇝ y = 0 ⟹ V₁ = { ( x ; 0 ) | x ∈ ℝ }
(sopra ( x ; 0 ) una graffa con scritto «x · ( 1 ; 0 )»)
= Span ( 1 ; 0 ) (graffa sotto ( 1 ; 0 ) con scritto «base»)
⟹ **dim V₁ = 1 = m_g(1)**

(pannello in basso a destra, 98:20 – 100:40, dopo aver cancellato il pannello del Teorema)
· **TEOR DIMENSIONE:**
dim Ker (A − I) = n − rg (A − I) = 2 − 1 = 1
(sotto n una graffa con «2»; sotto rg(A − I) una graffa)
⇝ Per λ = 1
m_a(λ) = 2 ≠ 1 = m_g(λ) ⟹ **A NON è diag'le**

Note: m_g(1) è calcolato in due modi (risolvendo il sistema e con il teorema della dimensione); il secondo è quello delle dispense (Esempio 18.8).

[verifica] P_A(t) = (t − 1)²; A − I = ( 0 1 ; 0 0 ) ha rango 1, nucleo Span(1, 0), quindi m_g(1) = 1 < 2 = m_a(1); SymPy conferma che A non è diagonalizzabile. ✓

Non sono svolti alla lavagna: la dimostrazione che autovettori con autovalori distinti sono indipendenti (Prop. 18.1 delle dispense), le dimostrazioni sulla somma diretta degli autospazi, del Corollario sugli autospazi, di m_g ≤ m_a e del Teorema di diagonalizzabilità; nessun esempio 3 × 3 e nessun esempio con parametro.

## Confronto con le dispense (sezione 18)
Solo alla lavagna (non nelle dispense della lezione 18):
- il richiamo della lezione 17 e il polinomio caratteristico «in casi speciali»: P_A(t) = t² − (tr A)t + det A per le 2 × 2 e, per le triangolari, autovalori = elementi sulla diagonale (nella sezione 17 delle dispense non ci sono né la formula con la traccia né il caso triangolare);
- l'esempio completo A = ( 2 1 ; 1 2 ): autovalori 1, 3, autospazi Span(−1, 1) e Span(1, 1), base di autovettori {(1, 1), (−1, 1)};
- la Prop. «se V = W₁ ⊕ … ⊕ W_k, unendo basi dei Wᵢ si ottiene una base di V» enunciata da sola (nelle dispense è usata solo dentro la dimostrazione del Cor. 18.6);
- nel Corollario sugli autospazi, la forma con le dimensioni dim V = dim V_λ₁ + … + dim V_λk (nelle dispense compare solo nella dimostrazione del Teorema 18.10);
- la definizione di molteplicità algebrica con la fattorizzazione P_T(t) = (t − λ)^m q(t), q(λ) ≠ 0;
- l'esempio della rotazione ( 0 1 ; −1 0 ): non diagonalizzabile su ℝ, diagonalizzabile su ℂ (autovalori ±i);
- l'Osservazione: su ℂ la condizione a) del Teorema vale sempre, per il teorema fondamentale dell'algebra;
- nell'esempio ( 1 1 ; 0 1 ), il calcolo esplicito dell'autospazio V₁ = Span(1, 0) prima di quello con il teorema della dimensione.

Solo nelle dispense (non alla lavagna):
- la dimostrazione per induzione della Prop. 18.1 e la «spiegazione» della Prop. 18.5;
- la definizione di somma diretta come unicità della scrittura, con la notazione V₁ ⊕ … ⊕ V_k (alla lavagna non compare il simbolo ⊕ e il Cor. è scritto con +);
- la prima disuguaglianza 1 ≤ m_g(λ) del Teorema 18.9 e l'idea della dimostrazione;
- la dimostrazione del Teorema di diagonalizzabilità 18.10;
- l'Esempio 18.11 (3 × 3, autovalori 3, 3, −1, diagonalizzabile), l'Esempio 18.12 (3 × 3 con parametro k: diagonalizzabile ⟺ k < 5), gli Esercizi 18.13 e 18.14.

Coincide con le dispense: l'esempio ( 1 1 ; 0 1 ) con m_a(1) = 2, m_g(1) = 1 è l'Esempio 18.8.

Differenze di notazione e di convenzione:
- dispense: endomorfismo T, polinomio p_T(λ) = det(A − λI) con variabile λ; lavagna: P_A(t) = det(A − tI) con variabile t, e λ per gli autovalori;
- dispense: Cor. 18.2 «p_T ha n radici distinte ⟹ diagonalizzabile»; lavagna: «T con n = dim V autovalori distinti ⟹ diagonalizzabile» (stesso contenuto);
- dispense: diagonalizzabile ⟺ D = M⁻¹ A M; lavagna (richiamo): P A P⁻¹ diagonale (equivalenti, con P = M⁻¹);
- dispense: m_a, m_g scritti ma(λ), mg(λ); lavagna m_a(λ), m_g(λ) con pedice.

## Controllo dei conti con SymPy
Script in cartella temporanea (`verifica_l18.py`). Tutti i risultati scritti alla lavagna sono corretti:
- det ( a−t b ; c d−t ) = t² − (a + d)t + (ad − bc).
- ( 2 1 ; 1 2 ): P_A(t) = t² − 4t + 3 = (t − 1)(t − 3); autospazi Span(−1, 1) (λ = 1) e Span(1, 1) (λ = 3); P⁻¹AP = ( 3 0 ; 0 1 ) con P = ( 1 −1 ; 1 1 ).
- ( 0 1 ; −1 0 ): P_A(t) = t² + 1, radici ±i, diagonalizzabile su ℂ e non su ℝ.
- ( 1 1 ; 0 1 ): P_A(t) = (t − 1)², rg(A − I) = 1, V₁ = Span(1, 0), m_g(1) = 1 ≠ 2 = m_a(1), non diagonalizzabile.

Errori e sviste del docente (nessuna conseguenza sui risultati):
- «AUTOVALORE» scritto al posto di «AUTOVETTORE» nelle due definizioni del richiamo, corretto subito sulla lavagna;
- nella Prop. sugli autovettori con autovalori distinti è scritto «autovettori di A» invece di «di T»;
- nella Def. di molteplicità il polinomio è scritto sia P_A(t) sia P_T(t);
- nella Prop. sulle basi la condizione V = W₁ ⊕ … ⊕ W_k è scritta in forma abbreviata («tc ∀v = w₁ + … + w_k»);
- nel Cor. sugli autospazi non è scritto che λ₁, …, λ_k sono **tutti** gli autovalori; «distinti» è aggiunto solo durante la pausa;
- nella definizione di autovettore del richiamo manca v ≠ 0 (e quindi, alla lettera, 0 sarebbe autovettore); nel richiamo ② manca «P invertibile»;
- in «A − 3I = [ −1 1 ; 1 −1 ]», nella prima copia il segno meno della prima entrata è molto sbiadito; la seconda copia e il risultato [ −x + y ; x − y ] confermano −1.

## Punti di lettura incerta
Nessuna formula illeggibile. Letture incerte:
- la fine della prima riga della Prop. «T : V → V endom, λ₁, …, λ_k» (55:00): il bordo del pannello e il proiettore coprono lo spazio dopo λ_k; non si vede se ci fosse scritto altro (per esempio «autovalori»);
- il segno cancellato tra «con» e «n = dim V» nel Corollario delle 37:00;
- il pezzo cancellato con uno scarabocchio dopo «A − 1I = ( 1 1 ; 1 1 )» (sembra un «⇒ se» riscritto);
- le scritte durante la pausa (≈ 65:20 – 66:20), parzialmente coperte dal docente e dallo studente;
- il momento esatto in cui è aggiunto «in 𝕂» nel Teorema (assente a 80:00, presente da ≈ 82:20);
- risoluzione 1600×900: le scritte piccole (pedici λᵢ, «tc», «e») sono state lette sui ritagli ingranditi e confrontate in più fotogrammi.

## Note sulla trascrizione audio
Non disponibile al momento della stesura: nessuna nota [a voce], nessun aneddoto, nessuna risposta a domande degli studenti. Da integrare quando `trascrizioni/algebra_L18_2024.txt` sarà pronta (in particolare: cosa dice il docente sulla «Dim» del Corollario, sull'esempio della rotazione, e la discussione con lo studente durante la pausa). Poiché la pausa non è tagliata nel video, bisognerà controllare se lo è nell'audio prima di allineare i tempi.
