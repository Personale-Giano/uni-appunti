# Algebra lineare, Lezione 12: Sistemi lineari II (lavagne dalla registrazione Webex del 20 ott 2025, prof. Radeschi)

Fonte: video della registrazione dell'anno scorso («Marco Radeschi-20251020 1600-1»), file `audio/algebra_L12_2025.mp4` (93 min 05 s, completo; la pausa non è registrata), trascrizione `trascrizioni/algebra_L12_2025.txt`.
Contenuto letto da 38 fotogrammi regolari (uno ogni 2,5 minuti, da 00:00 a 92:30; quello a 00:00 è nero, quindi 37 utili), più 6 fotogrammi intermedi aperti (60:50, 61:30, 61:50, 62:10, 92:45, 93:00) e 22 ingrandimenti a piena risoluzione per controllare pedici e matrici (fra cui 12:30, 20:00, 27:30, 40:00, 56:40, 61:40, 75:00, 80:02, 80:15, 92:40). La lavagna è in 4 pannelli (alto/basso, sinistra/destra) che vengono riempiti, fatti scorrere e cancellati; qui il contenuto è in ordine di comparsa.

Convenzioni:
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss, approssimati per eccesso: la scritta è già visibile a quel tempo).
- **[a voce]** indica ciò che è solo detto e non scritto; il tempo tra parentesi è quello dell'audio. I tempi dell'audio vanno da quasi coincidenti ad anticipati di 1–1,5 minuti rispetto ai fotogrammi (per esempio R₂ → R₂ − KR₁ è detta verso 83:30 e si vede scritta a 85:00).
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali: sono ricostruite da una trascrizione automatica piena di errori.
- Sulla lavagna il pedice del sistema omogeneo è una h minuscola (Sₕ; a voce «SH»), il rango è scritto rK e il parametro dell'ultimo esempio è una K maiuscola: qui sono riportati così.

## Titolo e ripasso «Previously» (00:00 – 02:30)
**LEZIONE 12: SISTEMI LINEARI II**
**Previously**
sistema Ⓢ { a₁₁x₁ + … + a₁ₙxₙ = b₁ ; ⋮ ; a_k1x₁ + … + a_knxₙ = b_k } ⟷ { Matrice dei coeff A = ( a₁₁ … ; ⋮ ) ; Vettore dei termini noti b = ( b₁ ; ⋮ ; b_k ) } ↕ Matrice completa (A | b)

(Il cerchietto Ⓢ e il tratto sotto il sistema compaiono a 12:30, quando il docente dà un nome al sistema.)

[a voce] (≈ 01:48 – 02:22) La prima cosa, come detto la volta scorsa, è riscrivere il sistema nella matrice completa.

## Esempio: tre equazioni, quattro incognite, due parametri liberi (02:30 – 12:30)
{ x + 2y − z + w = 3 ; y + 2z + 5w = 2 ; x + 3y + z + 6w = 5 } ⟷ ( ① 2 −1 1 | 3 ; 0 1 2 5 | 2 ; 1 3 1 6 | 5 ) (a 5:00 sono riquadrati i due elementi sotto il pivot, 0 e 1)

—(R₃ → R₃ − R₁)→ ( ① 2 −1 1 | 3 ; 0 ① 2 5 | 2 ; 0 [1] 2 5 | 2 ) (prima colonna riquadrata, 1 della terza riga riquadrato a parte)

—(R₃ → R₃ − R₂)→ ( ① 2 −1 1 | 3 ; 0 ① 2 5 | 2 ; 0 0 0 0 | 0 )

Si riscrive il sistema senza passare dalla forma ridotta. Le variabili dei pivot x e y sono segnate, 0 = 0 è **barrato**:
{ **x** + 2y − z + w = 3 ; **y** + 2z + 5w = 2 ; ~~0 = 0~~ }
y = 2 − 2z − 5w
x = 3 − 2y + z − w = 3 − 4 + 4z + 10w + z − w = −1 + 5z + 9w

{ x = −1 + 5t₁ + 9t₂ ; y = 2 − 2t₁ − 5t₂ ; z = t₁ ; w = t₂ } ⟶ **[ infinite soluzioni, che dipendono da 2 parametri liberi ]**

[a voce] (≈ 05:11 – 05:43) Dopo Gauss si può ridurre ulteriormente alla matrice a scalini ridotta, oppure riscrivere subito il sistema: «secondo me, in generale, quello che conviene fare in pratica» è riscrivere direttamente il sistema.
[a voce] (≈ 05:43 – 06:21) L'equazione 0 = 0 si può ignorare (la frase si interrompe nella trascrizione; alla lavagna è barrata).
[a voce] (≈ 09:09 – 09:53) z e w sono due parametri liberi: a t₁ e t₂ si danno i valori che si preferiscono; x e y sono dati in funzione di t₁ e t₂.
[a voce] (≈ 09:53 – 11:09) **Scopo della lezione:** anziché capire come risolvere un dato sistema, capire come leggere subito dal sistema (dalla matrice) se ci sono soluzioni, quante sono e qual è la struttura dello spazio delle soluzioni.

## Riscrivere un sistema: la forma A·x = b (12:30 – 22:30)
**RISCRIVERE UN SISTEMA.** Dato Ⓢ, scriviamo x = ( x₁ ; ⋮ ; xₙ ) il vettore delle incognite ⇝ una **SOLUZIONE** di Ⓢ è un vettore x ∈ 𝕂ⁿ le cui componenti soddisfino le eq.

**Oss.** Ⓢ si può pensare come
( a₁₁x₁ + … + a₁ₙxₙ ; ⋮ ; a_k1x₁ + … + a_knxₙ ) = ( b₁ ; ⋮ ; b_k ) = b ⊛
e il vettore a sinistra è (segno di uguale verticale sotto) **A · x**.

⇝ Ⓢ si può anche scrivere come **[ A · x = b ]** (riquadrato), con A ∈ M(k, n), x ∈ M(n, 1), b ∈ M(k, 1)
e una soluzione di Ⓢ è un x ∈ 𝕂ⁿ t.c. Ax = b.

Il segno ⊛ (aggiunto a 27:30 con una freccia, accanto a «= b») serve da etichetta per la forma vettoriale, ripresa nell'osservazione seguente.

[a voce] (≈ 15:39 – 17:28) A sinistra c'è un «vettore molto brutto». Finora non è cambiato nulla, ma il primo termine è una somma di prodotti: a₁₁ per x₁, a₁₂ per x₂ ecc., cioè gli elementi di una riga di A con gli elementi della colonna x, moltiplicati uno a uno e sommati. È la moltiplicazione fra matrici.
[a voce] (≈ 18:05 – 19:18) «Controlliamo che abbia grammaticalmente senso»: A ha k righe e n colonne; x è un vettore colonna con n elementi, cioè una matrice con n righe e una colonna; b ha k elementi, tanti quanti le equazioni, cioè k righe e una colonna.

## Forma per colonne (22:30 – 27:30)
**Oss.** Ⓢ scritto in forma vettoriale ⊛ si può anche scrivere come
( a₁₁x₁ ; ⋮ ; a_k1x₁ ) + ( a₁₂x₂ ; ⋮ ; a_k2x₂ ) + … + ( a₁ₙxₙ ; ⋮ ; a_knxₙ ) = ( b₁ ; ⋮ ; b_k )
⟺ x₁( a₁₁ ; ⋮ ; a_k1 ) + x₂( a₁₂ ; ⋮ ; a_k2 ) + … + xₙ( a₁ₙ ; ⋮ ; a_kn ) = ( b₁ ; ⋮ ; b_k )
⟺ **[ x₁A¹ + x₂A² + … + xₙAⁿ = b ]** (riquadrato)

[a voce] (≈ 22:45 – 24:37) Il vettore di sinistra si spezza in una somma: nel primo addendo si prendono i primi termini di tutte le righe, e così via. In ciascun vettore compare la stessa incognita in tutte le componenti, quindi si porta fuori. Correzione a voce (≈ 24:37): «x₂ che moltiplica a₂₁, scusate, a₁₂».
[a voce] (≈ 25:53 – 26:43) Sono due modi equivalenti di scrivere il sistema: il primo serve subito, il secondo nella parte successiva; chiede di tenerlo a mente.

## Lo spazio delle soluzioni: definizioni (27:30 – 32:30)
**LO SPAZIO DELLE SOLUZIONI DI UN SISTEMA LINEARE**
**Def.**
· Un sistema lineare (A | b) è **OMOGENEO** se b = 0.
· Dato (A | b), chiamiamo (A | 0) il **SISTEMA OMOGENEO ASSOCIATO**.
· Dato (A | b), chiamiamo
S = { soluzioni di (A | b) } = { x ∈ 𝕂ⁿ | Ax = b }
Sₕ = { soluzioni di (A | 0) } = { x ∈ 𝕂ⁿ | Ax = 0 }

[a voce] (≈ 28:43) Il sistema omogeneo associato si crea togliendo il b dato e mettendo uno zero; è un sistema nuovo (il seguito si perde nella trascrizione).

## Proposizione: struttura delle soluzioni (32:30 – 37:30)
**Prop.** Sia (A | b) sistema. Allora
① Sₕ = { sol di (A | 0) } è uno sp. vettoriale
② Se S ∋ x₀ ⟹ S = { x₀ + v | v ∈ Sₕ }

Sotto la proposizione c'è subito una riga di separazione e l'esempio: **nessuna dimostrazione è scritta alla lavagna.**

[a voce] (≈ 34:15 – 35:41) Se il sistema non omogeneo ammette almeno una soluzione, tutte le soluzioni del sistema originario si ottengono prendendo questa soluzione e aggiungendole una qualunque soluzione del sistema omogeneo associato. Subito dopo c'è un tratto perso della trascrizione (≈ 35:41 – 36:50): non si può escludere una giustificazione solo a voce.

## Esempio di prima: Sₕ come Span e S = x₀ + Sₕ (37:30 – 57:30)
**Es.** Esempio di prima. ( 1 2 −1 1 | 3 ; 0 1 2 5 | 2 ; 1 3 1 6 | 5 ) . sistema omog. assoc. ( 1 2 −1 1 | 0 ; 0 1 2 5 | 0 ; 1 3 1 6 | 0 )

**RISOLVIAMO (A | 0):**
( 1 2 −1 1 | 0 ; 0 1 2 5 | 0 ; 1 3 1 6 | 0 ) ⟶ ( 1̲ ② −1 1 | 0 ; 0 1̲ 2 5 | 0 ; 0 0 0 0 | 0 ) —(R₁ → R₁ − 2R₂)→ ( 1 0 −5 −9 | 0 ; 0 1 2 5 | 0 ; 0 0 0 0 | 0 )

(Sulla prima freccia non è scritta alcuna mossa: sono le stesse del primo esempio. Il 2 da uccidere è cerchiato, i pivot segnati.)

⟹ { x − 5z − 9w = 0 ; y + 2z + 5w = 0 } ⟹ { x = 5z + 9w ; y = −2z − 5w } ⟹ { x = 5t₁ + 9t₂ ; y = −2t₁ − 5t₂ ; z = t₁ ; w = t₂ }

⟹ Sₕ = { ( 5t₁ + 9t₂ ; −2t₁ − 5t₂ ; t₁ ; t₂ ) | t₁, t₂ ∈ 𝕂 } = ⊛

( 5t₁ ; −2t₁ ; t₁ ; 0 ) + ( 9t₂ ; −5t₁ ; 0 ; t₂ ) = t₁( 5 ; −2 ; 1 ; 0 ) + t₂( 9 ; −5 ; 0 ; 1 )
(una freccia collega questa riga al vettore riquadrato sopra)

**Refuso non corretto:** nel secondo vettore (visibile da 47:30 a 61:50) leggo −5t₁ alla seconda componente; dovrebbe essere −5t₂. Il passaggio successivo è giusto: t₂( 9 ; −5 ; 0 ; 1 ). Lo zero della terza componente è ripassato e ha una forma ambigua.

⊛ ⟹ Sₕ = { t₁( 5 ; −2 ; 1 ; 0 ) + t₂( 9 ; −5 ; 0 ; 1 ) | t₁, t₂ ∈ 𝕂 } = **Span{ ( 5 ; −2 ; 1 ; 0 ) , ( 9 ; −5 ; 0 ; 1 ) }**

(In questa riga la prima componente del secondo vettore è piccola e sbavata; si legge 9, come nella Span a fianco.)

**Soluzioni di (A | b) =**
{ x = −1 + 5t₁ + 9t₂ ; y = 2 − 2t₁ − 5t₂ ; z = t₁ ; w = t₂ } ⇝ S = { ( −1 + 5t₁ + 9t₂ ; 2 − 2t₁ − 5t₂ ; t₁ ; t₂ ) | t₁, t₂ } = { ( −1 ; 2 ; 0 ; 0 ) + ( 5t₁ + 9t₂ ; −2t₁ − 5t₂ ; t₁ ; t₂ ) | t₁, t₂ }

(A 55:00 il secondo vettore è riquadrato, così come il vettore identico nella riga di Sₕ.)

**S = { ( −1 ; 2 ; 0 ; 0 ) + v | v ∈ Sₕ }**

[a voce] (≈ 38:14) Il primo punto per risolvere un sistema è ridurlo a scalini; la riduzione è la stessa di prima, con zeri nell'ultima colonna.
[a voce] (≈ 39:26 – 40:34) Domanda di uno studente, apparentemente: i passaggi sono gli stessi di prima? Risposta: «ottimo punto»; le mosse di Gauss tengono separate la matrice a sinistra della barra e il vettore dei termini noti, quindi ripetendo le stesse mosse la matrice si trasforma nello stesso modo e nell'ultima colonna restano tutti zeri. È un discorso generale.
[a voce] (≈ 40:34) Nella trascrizione la mossa è detta «prima colonna meno due volte la seconda»; alla lavagna è R₁ → R₁ − 2R₂, cioè righe. Non si può dire se sia un lapsus del docente o un errore della trascrizione.
[a voce] (≈ 48:04 – 48:37) Gli oggetti di questo tipo sono combinazioni lineari, quindi l'insieme è lo Span dei due vettori: ogni soluzione del sistema omogeneo si trova come combinazione lineare, un multiplo del primo più un multiplo del secondo.
[a voce] (≈ 52:50 – 53:52) I vettori riquadrati sono esattamente le soluzioni del sistema omogeneo: sono gli stessi.
[a voce] (≈ 53:52 – 54:38) In questo esempio le soluzioni sono date da un vettore specifico, ( −1 ; 2 ; 0 ; 0 ), che è una soluzione, più i vettori di Sₕ.
[a voce] (≈ 54:38 – 55:15) **Quando serve:** se per qualche ragione viene data una soluzione, o a volte capita una soluzione facile da trovare mentre trovare le altre è più difficile, può convenire calcolare le soluzioni del sistema omogeneo associato: tutte le soluzioni sono la soluzione speciale trovata o data più le soluzioni del sistema omogeneo associato.

[verifica] ( −1 ; 2 ; 0 ; 0 ) è la soluzione che si ottiene con t₁ = t₂ = 0. I due generatori di Sₕ sono indipendenti, quindi dim Sₕ = 2 = n − rk(A) = 4 − 2.

## Geometricamente: sottospazi affini (57:30 – 61:50)
**GEOMETRICAMENTE:**
Figura: assi cartesiani in 𝕂ⁿ; una retta **Sₕ** per l'origine; una retta parallela con un'etichetta e una freccia: **S = { x₀ + v | v ∈ S₀ }**; una freccia dall'origine a un punto **x₀** della retta parallela.

**Def.** dato uno sp vettoriale V, un **sottospazi affine** è un sottoinsieme
S = { x₀ + v | v ∈ W } = x₀ + W
con x₀ fissato, W ⊆ V sottosp vettoriale.

(Scritto proprio «sottospazi affine», sottolineato, e S₀ nell'etichetta della figura, mentre tutto il resto della lezione usa Sₕ: vedi errori.)

[a voce] (≈ 56:50 – 57:28) Lo spazio delle soluzioni del sistema omogeneo associato passa per l'origine; S è dato da tutte queste soluzioni spostate di un vettore speciale.
[a voce] (≈ 58:56 – 59:31) Probabilmente avete già visto un insieme di questo tipo alle elementari con il nome di spazio affine. Gli spazi affini sono semplicemente spazi vettoriali spostati, non necessariamente passanti per l'origine.
[a voce] (≈ 60:41 – 61:22) Geometricamente i sottospazi affini sono versioni traslate di spazi vettoriali. La scrittura x₀ + W rende bene l'idea: si prende il sottospazio W e lo si sposta nella direzione di x₀.

La definizione di dimensione di un sottospazio affine non compare né alla lavagna né nelle parti leggibili dell'audio.

**Pausa.** Il docente annuncia dieci minuti di pausa (≈ 61:22). A 61:50 la lavagna è piena, a 62:10 è già cancellata e riscritta: la pausa è tagliata dal video.

## Esistenza delle soluzioni e rango (62:10 – 70:00)
(A | b) ⟷ **x₁A¹ + … + xₙAⁿ = b** (sottolineato)
⟹ Se una soluzione esiste, allora b ∈ Span(A¹, …, Aⁿ)
⟹ Span(A¹, …, Aⁿ, b) = Span(A¹, …, Aⁿ)
⟺ dim Span(A¹, …, Aⁿ, b) = dim Span(A¹, …, Aⁿ), con le graffe: il primo è rK(A | b), il secondo rK(A)
⟹ **PROP:** (A | b) ammette soluzione ⟺ rK(A | b) = rK(A) !

**Correzione del docente:** a 62:10 – 62:30 la prima riga è scritta con i pedici, x₁A₁ + … + xₙAₙ; a 65:00 è già x₁A¹ + … + xₙAⁿ. A voce (≈ 64:04 – 64:23): l'indice scritto in basso deve stare in alto, perché queste sono le colonne.

[a voce] (≈ 61:30) Nella prima parte si è visto che lo spazio delle soluzioni ha una bella struttura; ora «andremo a valutare» (la frase si perde nella trascrizione; da 63:30 si parla di quando la soluzione esiste).
[a voce] (≈ 64:53 – 65:25) Infilare b nello spazio generato non cambia lo spazio: tutto ciò che si raggiungeva con le colonne si continua a raggiungere; il contrario è ovvio.
[a voce] (≈ 66:04) La dimensione dello spazio generato dalle colonne è il rango di A, visto circa una settimana prima.
[a voce] (≈ 67:25 – 68:42) Così detto il risultato non è ancora molto utile, perché il rango finora non lo si sa calcolare. Le cose cambiano con la proposizione che segue.

## Calcolare il rango e contare i parametri (70:00 – 75:00)
**Prop:** ① Le mosse di Gauss (**su righe**, aggiunto sotto con una graffa) non cambiano il rango
② Se C è a scalini, rK C = num pivots

**Ricordiamo:** quando un sistema ammette soluzioni, queste dip. da tanti parametri liberi quanto sono le colonne di A senza pivot
↪ num parametri liberi = n − num pivots = n − rK(A)
(con «num incognite» e una freccia sopra n)

La proposizione è enunciata senza dimostrazione scritta alla lavagna.

[a voce] (≈ 69:20 – 70:39) **Ricetta:** per calcolare il rango si riduce a scalini e si contano i pivot. Quindi per sapere se un sistema ha soluzione si riduce per righe (A | b) con Gauss e si contano i pivot di A e di (A | b): se il numero è lo stesso, ci sono soluzioni.

## Teorema di Rouché-Capelli e corollario (75:00 – 80:00)
**TEOREMA DI ROUCHÉ CAPELLI:**
Dato un sistema (A | b) il sistema ammette
· **No soluzioni**, se rK(A | b) ≠ rK(A)
· **1 soluzione** se rK(A | b) = rK(A) = n
· **∞ soluzioni**, che dipendono da n − rK(A) parametri, quando rK(A | b) = rK(A) < n

**Cor:** supp che A sia una matrice quadrata, allora il sistema Ax = b ha 1 soluzione ⟺ rK(A | b) = rK(A) = n
⟺ A è invertibile
In questo caso, **x = A⁻¹ · b** (sottolineato)

[a voce] (≈ 74:19) Nel primo caso il rango di (A | b) è diverso, «in realtà maggiore», di quello di A. (Alla lavagna resta ≠.)
[a voce] (≈ 75:31 – 76:03) Il teorema non dice quali sono esattamente le soluzioni, ma permette di stabilire abbastanza velocemente se ci sono.
[a voce] (≈ 78:17) Se A è invertibile si moltiplica per l'inversa di A e si ottiene x = A⁻¹b.
[a voce] (≈ 78:17 – 79:04) Si finisce con un esempio che fa capire l'utilità del teorema quando non si ha un sistema specifico ma una famiglia di sistemi.

## Esempio: sistema con parametro (80:00 – 93:05)
**Es.** Sia dato il sistema { x + Ky = 4 − K ; Kx + 4y = 4 } **K parametro**
Al variare di K calcolare se ci sono soluzioni e quante.

① (A | b) = ( ① K | 4 − K ; [K] 4 | 4 ) (1 cerchiato, K sotto riquadrato)

② Gauss: —(R₂ → R₂ − KR₁)→ ( 1 K | 4 − K ; 0 4 − K² | 4 − 4K + K² )
(Sopra è annotato (A | b); il blocco delle prime due colonne è riquadrato ed etichettato A. L'ultimo termine, scritto piccolo, è ripetuto più chiaro sotto con una freccia: 4 − 4K + K².)

**Se 4 − K² ≠ 0** ⟹ rK A = 2 = rK(A | b) = n (n = 2)
⟹ ∃1 soluzione

**Se 4 − K² = 0** ⇝ K² = 4 ⇝ K = ∓2 ?

**K = 2**: ( ① 2 | 2 ; 0 0 | 0 ) ⟹ rK A = 1 = rK(A | b) < 2 = n
⟹ ∃ sol che dipendono da 2 − 1 = 1 parametro

**K = −2**: ( ① −2 | 6 ; 0 0 | ⑯ ) ⟹ rK A = 1 < 2 = rK(A | b)
⟹ **NO SOLUZIONI**

**Correzione del docente:** a 80:02 la prima equazione è scritta x + 4y = 4 − K; a 80:15 il 4 è cancellato e sostituito con K (si vede la sbavatura sotto la K). Nella trascrizione (≈ 79:45) si legge «x più 4y … k in questo momento, guardate, non è 4k»: la frase è storpiata, ma sembra la correzione a voce.

[a voce] (≈ 80:22 – 81:01) K è un numero: per ogni valore di K si ottiene un sistema diverso, quindi una famiglia di sistemi che dipendono dal parametro. Ci si chiede per quali valori ci sono soluzioni e quante.
[a voce] (≈ 81:01 – 81:47) **Avvertimento sull'esame:** uno, problemi di questo tipo ci sono anche all'esame; due, tendono a spaventare; tre, non devono spaventare.
[a voce] (≈ 81:47 – 82:55) Il parametro si tratta come se fosse un numero, e si fanno le cose di sempre: Rouché-Capelli, quindi prima la matrice completa, poi Gauss per ridurre a scalini e contare i pivot.
[a voce] (≈ 83:27 – 84:33) **Avvertimento sulle divisioni:** moltiplicare per K non dà problemi. L'errore più frequente è quando ci si trova a dover dividere per K o per qualcosa che contiene K: quando si divide per un numero bisogna assicurarsi che sia diverso da zero. Se capita di dover dividere per K, si separano due casi: se K = 0 si sostituisce e si risolve un sistema senza parametri; se K ≠ 0 si divide e si continua. In questo esempio serve solo moltiplicare.
[a voce] (≈ 85:55 – 86:35) Se 4 − K² ≠ 0 c'è un secondo pivot, e i due pivot di A sono anche pivot della matrice più grande (A | b), quindi i ranghi sono uguali.
[a voce] (≈ 88:58 – 89:42) Per K = 2 Rouché-Capelli dice che le soluzioni esistono perché i ranghi sono uguali, e dipendono da 2 − rk(A) = 1 parametro. Risponde a una domanda: ha semplicemente sostituito il valore di K nella matrice.
[a voce] (≈ 92:06 – 92:38) Il numero di parametri è solo l'osservazione che c'è una colonna senza pivot: una colonna senza pivot corrisponde a una variabile che si può sempre portare dall'altra parte dell'equazione e che diventa il parametro libero del sistema.

La lezione finisce qui (≈ 92:38 «possiamo fermarci qua»). Non calcola le soluzioni esplicite per nessun valore di K e non fa altri esercizi.

[verifica] Soluzioni non calcolate in lezione: per K ≠ ±2, x = 8/(K + 2), y = (2 − K)/(K + 2); per K = 2, (2 − 2s, s) con s ∈ ℝ; per K = −2 insieme vuoto. Si nota che 4 − 4K + K² = (K − 2)², e che det A = 4 − K².

## Controllo dei conti con SymPy
Rifatti con SymPy (`linsolve`, `rref`, `rank`, `nullspace`, operazioni elementari passo per passo). Tutti i risultati scritti alla lavagna sono corretti, tranne il refuso −5t₁ sotto indicato.
- Sistema 3 × 4: R₃ − R₁ dà ( 0 1 2 5 | 2 ); R₃ − R₂ dà la riga nulla; soluzioni (−1 + 5z + 9w, 2 − 2z − 5w, z, w), che sostituite danno 0 in tutte e tre le equazioni.
- Passaggio x = 3 − 2(2 − 2z − 5w) + z − w = −1 + 5z + 9w: corretto.
- (A | 0): ogni passaggio coincide; `rref` = ( 1 0 −5 −9 | 0 ; 0 1 2 5 | 0 ; 0 0 0 0 | 0 ).
- `nullspace` di A = { (5, −2, 1, 0), (9, −5, 0, 1) }, gli stessi vettori della lavagna; A·(5, −2, 1, 0) = A·(9, −5, 0, 1) = 0.
- A·(−1, 2, 0, 0) = (3, 2, 5) = b; x₀ + t₁v₁ + t₂v₂ coincide con la soluzione generale.
- rk A = rk(A | b) = 2, n − rk A = 2 parametri.
- Sistema con parametro: R₂ − KR₁ dà ( 0 , 4 − K² , K² − 4K + 4 ). K = 2: ( 1 2 | 2 ; 0 0 | 0 ), ranghi 1 e 1, soluzioni (2 − 2y, y). K = −2: ( 1 −2 | 6 ; 0 0 | 16 ), ranghi 1 e 2, insieme vuoto. K = 0, 1, 3: ranghi 2 e 2, una soluzione.

Errori e correzioni del docente:
- x₁A₁ + … + xₙAₙ corretto in x₁A¹ + … + xₙAⁿ (corretto da lui, 62:10 → 65:00).
- x + 4y corretto in x + Ky (corretto da lui, 80:02 → 80:15).
- «a₂₁» corretto in «a₁₂» (a voce, ≈ 24:37).
- −5t₁ al posto di −5t₂ nel secondo vettore della scomposizione (non corretto; nessuna conseguenza sul risultato).
- S₀ al posto di Sₕ nell'etichetta della figura (non corretto).
- «un sottospazi affine» per «un sottospazio affine» (non corretto).
- Nel teorema il primo caso è scritto rK(A | b) ≠ rK(A): è giusto, e a voce precisa che in realtà è maggiore.

## Punti illeggibili
Nessuna formula è rimasta illeggibile: [illeggibile] non compare. Restano due letture incerte, segnalate sopra: il pedice di −5t₁ (si legge 1; il valore corretto sarebbe 2) e la prima componente sbavata del secondo vettore nella riga ⊛ (si legge 9, confermato dalla Span a fianco). Il proiettore copre a tratti parti del pannello in alto a sinistra: ogni parte coperta è stata letta in un altro fotogramma, dopo lo scorrimento del pannello.

## Note sulla trascrizione audio
La trascrizione (`algebra_L12_2025.txt`) contiene lunghi tratti allucinati (ripetizioni di «modulo», «di Gauss, sott», «mappa lineare», «mapposito», «r3», «spazio», «v», «rangoli», «il termine di Sarrus»), dovuti ai suggerimenti lessicali dati a Whisper: non sono parole del docente. Non è stata fatta alcuna ritrascrizione. Sono persi, fra gli altri, i tratti 01:15–01:48, 03:58–05:30, 06:21–06:51, 08:29–09:00, 13:48–14:32, 15:06–15:39, 16:16–16:49, 19:18–20:46, 23:16–23:57, 28:43–29:50, 33:36–34:15, 35:41–37:42, 41:31–42:36, 43:42–45:19, 46:00–46:50, 47:31–48:04, 49:00–50:47, 51:18–53:30, 55:40–56:50, 57:28–58:19, 58:56–59:15, 61:40–63:25, 66:47–67:25, 69:59–70:30, 70:39–71:12, 74:57–75:50, 77:15–78:17, 85:20–86:20, 86:40–87:30, 87:55–88:50, 89:50–90:14, 90:20–92:06: in questi potrebbero esserci commenti a voce non riportati qui. Fidarsi della lavagna per le formule.
