# Algebra lineare: appunti a mano di novembre 2026 confrontati con i capitoli del sito

Scritto il 23 nov 2026. Fonti confrontate: le trascrizioni `fonti_testo/Algebra lineare/L12_appunti_2nov.md` … `L18_appunti_18nov.md` (7 lezioni, 16 pagine) e i capitoli 41-54 e 59-63 di `quaderno-privato/contenuti/algebra.json` (versione del 20 nov). Il sito e i capitoli NON sono stati modificati. Tutti i conti degli appunti sono stati rifatti con SymPy (`scratchpad/alg_appunti_nov/verifica.py`).

**Numeri di lezione.** Confermati dal contenuto e dai titoli scritti da Emanuele: 2 nov = L12 («Sistemi Lineari 2 – Lezione 12», cap. 41-42), 4 nov = L13 (senza titolo; Rouché-Capelli e indipendenza, cap. 42 e 44), 9 nov = L14 («14. Applicazioni lineari», cap. 46-48), 11 nov = L15 («Lezione 15 Applicazioni lineari 2», cap. 48-51), 13 nov = L16 («Lezione 16», cap. 52-54), 16 nov = L17 («17. Autovalori e Autovettori», cap. 59-61), 18 nov = L18 («Lezione 18: Autovalori e Autovettori II», cap. 61-63). Il calendario dello STATO torna.

**Legenda.** «manca» = da aggiungere (con il blocco dopo cui andrebbe); «già presente» = nel capitolo c'è, eventualmente con un altro esempio; «in contrasto» = il capitolo dice qualcosa che per la lezione 2026 non è più vero o non coincide. Nessuno di questi capitoli ha evidenziazioni (STATO: studiati 1-13), ma prima di inserire conviene ricontrollare `evid_export.json` e usare `inserisci_blocchi_sito.py`.

---

## L12, 2 novembre (cap. 41)

- **Appunti 2 nov p. 1** → definizione del sistema omogeneo associato (**), matrice completa C = (A | b) e (A | 0) «o semplicemente A», insiemi S e S_0 → **già presente** in cap41.7-11 (stessa notazione S_0 delle dispense; la lavagna 2025 usava S_h).
- **Appunti 2 nov p. 1** → Prop. «S_0 ⊂ 𝕂ⁿ è un sottospazio» con la dimostrazione in tre punti (0 ∈ S_0, somma, multipli) → **già presente**, identica, in cap41.11-16.
- Gli appunti si fermano qui (mezza pagina). Non c'è niente su S = x + S_0, sottospazi affini, colonne e rango, Rouché-Capelli (cap41.18-42.31): non si può dire se nel 2026 il docente li abbia fatti il 2 nov o il 4 nov. L'unica traccia è l'inizio della L13, che riparte da Rouché-Capelli.

## L13, 4 novembre (cap. 42 e 44)

- **Appunti 4 nov p. 1** → enunciato di Rouché-Capelli con «dipende da n − rg(A) parametri» e i tre casi (nessuna, 1, ∞ soluzioni) → **già presente** in cap42.14, 42.17 e 42.22-25. Nel 2026 la lezione 13 si apre ripetendo il teorema: è coerente con quanto dice cap42.17 sulla L13 della serie 2025.
- **Appunti 4 nov p. 1** → **esempio di indipendenza** v_1 = (1, 5, 3), v_2 = (1, −1, 1), v_3 = (3, 3, 5), impostato come x_1v_1 + x_2v_2 + x_3v_3 = 0 con la distinzione «① solo la soluzione nulla / ② esiste un'altra soluzione» → **manca nel capitolo 44** (blocco più vicino **cap44.12**, prima dell'esempio u_1, u_2, u_3 della lavagna 2025, oppure dopo cap44.15). Negli appunti l'esempio non è concluso; con SymPy: rango 2, v_3 = v_1 + 2v_2, quindi dipendenti (soluzioni t(−1, −2, 1)). La relazione v_3 = v_1 + 2v_2 è un bel controllo da scrivere.
- Gli appunti finiscono qui: generatori, basi, coordinate e codici di correzione (cap44.16-45.23) non compaiono.

## L14, 9 novembre (cap. 46-48)

- **Appunti 9 nov p. 1** → definizione di applicazione lineare con (i) e (ii) → **già presente** in cap46.3-5. Nel 2026 non c'è traccia della «condizione unica» f(v_1 + a v_2) = … né dei sinonimi, che vengono dalla lavagna 2024 (cap46.7-12).
- **Appunti 9 nov p. 1** → «Notiamo che»: F(0_V) = F(0_𝕂 · 0_V) = 0_𝕂 · F(0_V) = 0_W, con i pedici dei tre zeri, e F manda combinazioni lineari in combinazioni lineari → **già presente** in cap46.14 e 46.16-18. (Il passaggio con 0_𝕂 · 0_V scritto con i pedici è più esplicito del cap46.14, che lo dice a parole: facoltativo.)
- **Appunti 9 nov p. 1** → Esempio 1, F(a, b) = (2a + b, a + 3b), verifica completa di (i) e (ii) → **già presente**, con gli stessi numeri e passaggi, in cap46.21-24 (è l'esempio delle dispense; nel 2024 la lavagna usava T(x, y) = (3x + 2y, x)).
- **Appunti 9 nov p. 1** → Esempio 2, F(a, b) = (2a − 1, a + b + 3), F(0, 0) = (−1, 3) ≠ 0 → **già presente** come idea in cap46.29 e 46.33 (altri numeri: (a + 2, a + b − 1) e (x + 1, y²)). Nessuna aggiunta necessaria; al più una riga «a lezione 2026: …».
- **Appunti 9 nov p. 1** → Esempio 3, F(a, b) = (a², 2a + 3b), F(0) = 0 ma con v = (2, 1), w = (2, 2): F(v + w) = (16, 17) ≠ (8, 17) = F(v) + F(w) → **già presente** come idea in cap46.30 (dispense: (a², a + b) con v = (2, 1), w = (2, 0)). Variante numerica del 2026; conto giusto.
- **Appunti 9 nov p. 1** → Esempi 4 e 5, applicazione nulla e identità → **già presente** in cap46.36-37.
- **Appunti 9 nov p. 2** → Esempio 6, L_A(x) = A·x con la spiegazione di «left» → **già presente** in cap46.39-41.
- **Appunti 9 nov p. 2** → Esempio 7, la traccia Tr : M(n) → 𝕂 → **già presente** in cap46.51-53.
- **Appunti 9 nov p. 2** → Esempio 8, la derivata ℝ_4[x] → ℝ_3[x] → **già presente** in cap46.55-59 (scritta per grado d qualsiasi). Si potrebbe citare il caso d = 4 del 2026, ma non serve.
- **Appunti 9 nov p. 2** → definizioni di nucleo («Kernel») e immagine → **già presente** in cap47.2-7.
- **Appunti 9 nov p. 2** → Prop. «Ker F e Im F sono sottospazi» **con dimostrazione alla lavagna** (per il nucleo completa, per l'immagine solo i punti a e l'inizio di b) → **già presente** in cap47.10-20, ma **in contrasto con cap47.21**: «A lezione (registrazione 2024) questa proposizione è solo enunciata». Nel 2026 il docente l'ha dimostrata. Proposta: aggiungere a cap47.21 una frase «Nella lezione 2026 la dimostrazione è stata svolta alla lavagna, come sopra».
- **Appunti 9 nov p. 2** → Prop. «F iniettiva ⟺ Ker F = {0}, F suriettiva ⟺ Im F = W», dimostrata solo la parte (⟸) dell'iniettività (da F(v) = F(v′) a v − v′ ∈ Ker F); «(⟹) e 2) è semplice» → **già presente** in cap47.23-29, con la stessa dimostrazione della lavagna 2024 (cap47.29).
- **Appunti 9 nov p. 3** → teorema della dimensione, enunciato → **già presente** in cap48.2-5.
- **Appunti 9 nov p. 3** → **esempio della proiezione** F : ℝ³ → ℝ², F(x, y, z) = (x, y): Ker F = Span((0, 0, 1)), «retta» di dimensione 1, Im F = ℝ² di dimensione 2, e 1 + 2 = 3 → **manca nel capitolo 48** (blocco più vicino **cap48.6**, da mettere prima dell'esempio con A = ( 1 0 2 ; 1 2 4 ), perché è più semplice). Conti verificati.
- Non compare negli appunti il collegamento con Rouché-Capelli (cap48.7-13): nel 2024 era «il punto d'arrivo della lezione». Il corollario su iniettività e suriettività compare invece all'inizio della L15 (foto della lavagna dell'11 nov).

## L15, 11 novembre (cap. 48-51)

- **Appunti 11 nov p. 1, foto 1 e 3 della lavagna** → dal teorema della dimensione: dim Im f ≤ dim V con «=» sse Ker f = 0 sse f iniettiva; Im f ⊆ W, dim Im f ≤ dim W con «=» sse f suriettiva; poi «se f è iniettiva dim V ≤ dim W, se è suriettiva dim V ≥ dim W» → **già presente** in cap48.15-21 e cap49.3-8. Nel 2026 questa parte apre la L15 (nel 2024 il corollario stava in L14): l'ordine dei cap. 48-49 va bene così.
- **Appunti 11 nov p. 1, foto 3** → Def. di isomorfismo; poi Prop. «l'inversa di un isomorfismo è lineare», Def. di spazi isomorfi, Oss. «isomorfi ⟹ dim V = dim W» → **già presente** in cap49.6, 49.12, 49.15-16.
- **Appunti 11 nov p. 1** → «un esempio fondamentale»: F_B : 𝕂ⁿ → V, F_B(λ) = λ_1v_1 + … + λ_nv_n, lineare, suriettiva perché i v_i generano, **iniettiva dimostrata** (Ker F_B = {0} per l'indipendenza), F_B⁻¹(v) = [v]_B «vettore delle coordinate» → **già presente** in cap49.28-40. Piccolo **contrasto con cap49.33**: «A lezione la dimostrazione è lasciata come esercizio» (2025); nel 2026 la parte sull'iniettività è scritta negli appunti, quindi probabilmente svolta alla lavagna. Proposta: una frase in cap49.33.
- **Appunti 11 nov p. 1** → **esempio delle coordinate di un polinomio**: ℝ_2[x], B = {1, x + 1, x² + x}, p(x) = x² + 2x + 1; dal confronto dei coefficienti c = 1, b + c = 2, a + b = 1 si ottiene [p(x)]_B = (0, 1, 1) → **manca nel capitolo 49** (blocco più vicino **cap49.49**, dopo l'esempio 2025 con B = {x², x + 1, 1}). Conti verificati. È utile perché la base non contiene 1 e x separati e il sistema va risolto «a cascata».
- **Appunti 11 nov p. 1** → la proposizione «V e W isomorfi ⟺ dim V = dim W» (cap49.20-25) **non compare** negli appunti.
- **Appunti 11 nov p. 2** → definizione della matrice associata [f]^B_C (coefficienti a_ij delle f(v_j) nella base C, matrice per colonne) e la ricetta in 3 passi (prendere i v_i, calcolare f(v_i), calcolare [f(v_i)]_C) → **già presente** in cap50.6-12 (la ricetta è detta a parole in cap50.9 e cap52.22).
- **Appunti 11 nov p. 2** → Prop. [f(v)]_C = [f]^B_C · [v]_B → **già presente** in cap51.3-9.
- **Appunti 11 nov p. 2** → **esercizio con la sola matrice**: f : ℝ_2[x] → ℝ_1[x], B = {1, x, x²}, C = {1, x}, [f]^B_C = ( 1 0 2 ; 0 5 3 ); calcolare f(a + bx + cx²). Si ottiene [f(p)]_C = (a + 2c, 5b + 3c), quindi f(a + bx + cx²) = (a + 2c) + (5b + 3c)x; nota di Emanuele: [p]_B = (a, b, c) è il «caso speciale» della base canonica → **manca nel capitolo 51** (blocco più vicino **cap51.19**, dopo i due esempi con arrivo ℝ²). Differenza utile rispetto ai capitoli: lo spazio di arrivo è di polinomi, quindi alla fine le coordinate (a + 2c, 5b + 3c) vanno ritradotte in un polinomio. Conto verificato; negli appunti l'ultima riga ha perso il «+».
- Non compaiono negli appunti: la matrice di L_A nelle basi canoniche (cap50.28-36), la matrice dell'identità (cap51.24-28), lo spazio Hom(V, W) e il teorema Hom(V, W) ≅ M(m, n) (cap51.29-43). Potrebbero essere stati fatti senza essere annotati; da verificare se arriva la registrazione 2026.

## L16, 13 novembre (cap. 52-54)

- **Appunti 13 nov p. 1** → richiamo di F_B⁻¹ : v ↦ [v]_B e della matrice associata; «Idea: cosa succede se cambio base?» → **già presente** in cap52.2-4.
- **Appunti 13 nov p. 1** → applicando [f(v)]_C = [f]^B_C [v]_B a id : V_B → V_B′ si ottiene [v]_B′ = [id]^B_B′ [v]_B, «matrice del cambio di base» → **già presente** in cap52.7-17 (nel capitolo l'identità si scrive I_V; negli appunti, come nelle dispense, id).
- **Appunti 13 nov p. 1** → Prop. «[v]_B′ = A[v]_B, A invertibile, [id]^B′_B = A⁻¹» (un solo enunciato) → **già presente** in cap52.13-14 e 52.41-44 (nel capitolo sono due proposizioni; cap52.44 nota che nelle dispense stanno insieme, come negli appunti 2026).
- **Appunti 13 nov p. 1** → **esempio nei polinomi**: ℝ_1[x], B = {1, 1 + x}, B′ = {1 + x, 2 + x}; A = [id]^B_B′ = ( −1 1 ; 1 0 ), [x]_B′ = (2, −1), [x]_B = (−1, 1) e controllo A[x]_B = (2, −1) = [x]_B′ → **manca nel capitolo 52** (blocco più vicino **cap52.30**, dopo l'esempio in ℝ²). È l'unico esempio di cambio di base fuori da 𝕂ⁿ, quindi senza scorciatoia della base canonica, e contiene il controllo della formula. Conti verificati. Negli appunti la prima colonna non è calcolata per esteso (1 = a(1 + x) + b(2 + x) dà a = −1, b = 1) e il risultato finale è scritto «= [x]_B» invece di [x]_B′.
- **Appunti 13 nov p. 1** → Oss. 1: le colonne di [id]^B_B′ sono [v_j]_B′; Oss. 2: se B′ è la base canonica di 𝕂ⁿ, [id]^B_B′ = (v_1 | … | v_n) → **già presente** in cap52.8-10 e 52.33-36.
- **Appunti 13 nov p. 1** → **esercizio** in ℝ²: dalla canonica a B′ = {(1, 1), (0, 1)}, [id]^E_B′ = ( 1 0 ; 1 1 )⁻¹ = ( 1 0 ; −1 1 ) → **già presente** come metodo in cap52.45-48 (con B′ = {(1, 1), (1, 2)}). Variante numerica, facoltativa.
- **Appunti 13 nov p. 2** → composizione, g ∘ f lineare, Prop. L_AB = L_A ∘ L_B con la dimostrazione in una riga (associatività) → **già presente** in cap53.6-22.
- **Appunti 13 nov p. 2** → Prop. [g ∘ f]^A_C = [g]^B_C · [f]^A_B, con basi chiamate A, B, C e il diagramma a due piani → **già presente** in cap53.28-38 (cap53.36 dice che alla lavagna 2025 le basi erano A, B, C: lo stesso nel 2026). Nel diagramma degli appunti la freccia in basso è etichettata L_AB; il cap53.38 dice correttamente L_BA (vedi errori).
- **Appunti 13 nov p. 2** → Prop. «f è un isomorfismo ⟺ [f]^B_C invertibile, e [f⁻¹]^C_B = ([f]^B_C)⁻¹» → **già presente** in cap53.44-49, ma **in contrasto con cap53.43**: «a lezione compare solo nel caso dell'identità» (2025). Nel 2026 è stata enunciata in generale, sotto il titolo «Applicazioni». Proposta: una frase in cap53.43.
- **Appunti 13 nov p. 2** → **esempio di cambio di base tra due basi non canoniche passando per la canonica**: B = {(1, 0), (1, 1)}, B′ = {(1, 1), (0, 1)}, [id]^B_B′ = ( 1 0 ; 1 1 )⁻¹ ( 1 1 ; 0 1 ) = ( 1 1 ; −1 0 ) → **già presente** come metodo in cap53.54-63 (lavagna 2025: B = {(1, 1), (1, 2)}, B′ = {(0, 1), (−1, 3)}). Variante numerica, conto verificato (controllo: (1, 0) = 1·(1, 1) − 1·(0, 1)). Facoltativa.
- **Appunti 13 nov p. 2** → seconda domanda, id_W ∘ f ∘ id_V = f, [f]^B′_C′ = [id_W]^C_C′ [f]^B_C [id_V]^B′_B, Prop. A′ = P_W A P_V⁻¹ con P_V = [id]^B_B′, P_W = [id]^C_C′ → **già presente** in cap54.3-11: stessa formula, il capitolo chiama P e Q quelle che gli appunti chiamano P_V e P_W. Si potrebbe citare la notazione P_V, P_W in cap54.4 (facoltativo).
- **Appunti 13 nov p. 2** → Def. di endomorfismo, [f]^B_B ∈ M(n) con n = dim V, e l'inizio di «B′ altra base → [f]^B′_B′ = A′; Prop.:» (non finita) → **già presente** in cap54.29-36.
- Non compaiono: l'esempio [L_A]^B_B con A = ( 1 2 ; 2 1 ) (cap54.16-27), le matrici simili e le loro proprietà (cap54.49-78). Le matrici simili sono però usate negli appunti del 16 nov, con la scrittura delle dispense B = M⁻¹AM (cap54.55 la riporta già).

## L17, 16 novembre (cap. 59-61)

- **Appunti 16 nov p. 1** → definizione di autovettore e autovalore, «⚠ λ può essere 0, v non può essere 0» → **già presente** in cap59.20-24. Nel 2026 la lezione parte subito dalla definizione: mancano negli appunti le motivazioni 2025 (matrice ( 1 0 ; 0 1/2 ), oracolo per ( 1 2 ; 2 1 ), cap59.2-17).
- **Appunti 16 nov p. 1** → Oss. in coordinate: F(v) = λv ⟺ Ax = λx, «l'unico caso che dobbiamo capire è f = L_A» → **già presente** in cap59.37-40.
- **Appunti 16 nov p. 1** → es. 1, A = ( 3 4 ; 0 2 ): e_1 autovettore (λ = 3), e_2 no, **v_3 = (3, 1) no** (L_A(v_3) = (13, 2)), v_4 = (−4, 1) autovettore (λ = 2) → **già presente** in cap59.31 (Esempio 17.2 delle dispense), tranne il «non esempio» (3, 1), che **manca** (blocco **cap59.31**: basta una frase). Conti verificati.
- **Appunti 16 nov p. 1** → es. 2, A = ( 1 1 −1 ; 2 1 1 ; 3 0 2 ): e_1 no, v = (0, 1, 1) autovettore con λ = 2 → **già presente** in cap59.32 (Esempio 17.4). Negli appunti v è chiamato per errore «e_2».
- **Appunti 16 nov p. 1** → i multipli non nulli di un autovettore sono autovettori, con il conto F(μv) = λ(μv) → **già presente** in cap59.33-35.
- **Appunti 16 nov p. 1** → es. 3, **rotazione di un angolo θ qualsiasi** (θ ∉ {0, π}) con la matrice A = ( cos θ −sin θ ; sin θ cos θ ), le colonne L_A(e_1) = (cos θ, sin θ), L_A(e_2) = (−sin θ, cos θ), un disegno, e la foto della lavagna: «L_A(v) è ruotato di angolo θ; se θ ≠ 0, π non è mai un multiplo di v ⟹ non ci sono autovettori» → **già presente** come enunciato in cap59.46, ma la matrice della rotazione e il disegno con Ae_1, Ae_2 **mancano nel capitolo 59** (blocco più vicino **cap59.46**). **In contrasto con cap61.58**, che presenta quella matrice come «non presente nelle dispense né in lezione» (riferito al 2025): nel 2026 il docente l'ha scritta alla lavagna. Nel 2025 c'era solo Rot_π/2 (cap59.42-45).
- **Appunti 16 nov p. 1, foto della lavagna** → Def. di endomorfismo (o matrice) diagonalizzabile: esiste una base di autovettori → **già presente** in cap60.3.
- **Appunti 16 nov p. 2** → Prop. «[F]^B_B è diagonale ⟺ v_1, …, v_n sono autovettori» con la dimostrazione per colonne → **già presente** in cap60.8-22 (il capitolo separa le due direzioni; gli appunti 2026, come la Prop. 17.6 delle dispense, le uniscono).
- **Appunti 16 nov p. 2** → diagramma con base canonica A e base di autovettori B, M = [id]^B_A, A = MDM⁻¹ ⟺ D = M⁻¹AM; Def. di matrice diagonalizzabile con M⁻¹AM = D; Prop. «F diagonalizzabile ⟺ [F]^B_B diagonalizzabile ⟺ esiste C con [F]^C_C diagonale»; M = (v_1 | … | v_n) → **già presente** in cap60.31-45. Nel 2026 il docente usa la scrittura delle dispense (M, D = M⁻¹AM), non quella della lavagna 2025 (P, A = PDP⁻¹): cap60.42-44 spiega già l'equivalenza.
- **Appunti 16 nov p. 2, foto 10:18** → **esempio svolto D = M⁻¹AM** per A = ( 3 4 ; 0 2 ): M = ( 1 −4 ; 0 1 ), det M = 1, M⁻¹ = ᵗCof(M) = ( 1 4 ; 0 1 ), poi M⁻¹A = ( 3 12 ; 0 2 ) e D = ( 3 0 ; 0 2 ) → **manca come conto nel capitolo 60**: cap60.25-26 scrive [L_A]^B_B = ( 3 0 ; 0 2 ) solo applicando la proposizione. Blocco più vicino **cap60.26** (o dopo cap60.60, dove M⁻¹ è già data). Conti verificati.
- **Appunti 16 nov p. 2** → es. 3 ripreso: la rotazione (θ ≠ 0, π) non è diagonalizzabile → **già presente** in cap60.29.
- **Appunti 16 nov p. 2** → matrici diagonali: D·x, prodotto di diagonali, potenze Aᵏ = diag(λ_iᵏ) → **già presente** in cap60.51-55.
- **Appunti 16 nov p. 2** → calcolo di A¹⁰⁰ per A = ( 3 4 ; 0 2 ): **Metodo 1** «a forza bruta», A² = ( 9 20 ; 0 4 ), «continuo così… A²·A² = A⁴…» → **manca nel capitolo 60** (cap60.58 dice solo che cento prodotti sono «estremamente dispendiosi»; blocco **cap60.58**: una frase con A² = ( 9 20 ; 0 4 ) rende concreto il confronto). **Metodo 2**, A = MDM⁻¹ con la cancellazione dei M⁻¹M → **già presente** in cap60.56-63.
- **Appunti 16 nov p. 3** → A¹⁰⁰ = ( 3¹⁰⁰ 4(3¹⁰⁰ − 2¹⁰⁰) ; 0 2¹⁰⁰ ) → **già presente**, stesso risultato, in cap60.61-63 (verificato con SymPy).
- **Appunti 16 nov p. 3** → «Domanda: quando possiamo diagonalizzare? come troviamo autovalori e autovettori?» e Def. del polinomio caratteristico P_A(λ) = det(A − λI_n) → **già presente** in cap60.67 e cap61.12-15. Nel 2026 la variabile è λ, come nelle dispense (la lavagna 2025 usava t); il segno A − λI è lo stesso.
- **Appunti 16 nov p. 3** → Oss. 1: P_A ha grado n → **già presente** in cap61.42-44.
- **Appunti 16 nov p. 3** → Oss. 2: **matrici simili hanno lo stesso polinomio caratteristico**, con la dimostrazione alla lavagna (λI_n = λM⁻¹I_nM, poi Binet) → **già presente** come dimostrazione in cap61.62-66, ma **in contrasto con cap61.67**: «Alla lavagna questa proprietà non compare» (2025). Nel 2026 è alla lavagna, con la stessa dimostrazione delle dispense. Proposta: correggere cap61.67 in «Nella lezione 2025 non compare; nel 2026 sì, con questa dimostrazione».
- **Appunti 16 nov p. 3** → esempio A = ( 3 4 ; 0 2 ): P_A(λ) = (3 − λ)(2 − λ), radici 3 e 2 «esattamente gli autovalori trovati prima» → **già presente** in cap61.39. Nel 2026 il primo esempio di polinomio caratteristico è questo (2025: ( 1 2 ; 2 1 ), cap61.19-25).
- Non compaiono negli appunti 2026: la catena di equivalenze λ autovalore ⟺ det(A − λI) = 0 (cap61.3-9, ma l'enunciato è all'inizio della L18), la formula t² − (tr A)t + det A (cap61.26-32), le triangolari (arrivano nella L18), la rotazione su ℂ (cap61.51-60).

## L18, 18 novembre (cap. 61-63)

- **Appunti 18 nov p. 1** → richiamo della definizione; Prop. «λ è autovalore ⟺ è radice di P_A(t) = det(A − tI)», polinomio di grado n → **già presente** in cap61.16 e 61.42. Nel 2026 la variabile torna a essere t.
- **Appunti 18 nov p. 1** → **esempio 3 × 3 triangolare inferiore** A = ( 1 0 0 ; 1 2 0 ; 2 1 3 ): P_A(t) = (1 − t)(2 − t)(3 − t), autovalori 1, 2, 3; autovettori di λ = 3 da (A − 3I_3)v = 0, cioè −2x = 0, x − y = 0, 2x + y = 0, quindi x = y = 0, z libero: Span((0, 0, 1)) → **manca** (blocco più vicino **cap61.39** per gli autovalori letti sulla diagonale di una triangolare *inferiore*, oppure **cap62.8/62.23** per l'autospazio). **In contrasto con cap63.51**: «A lezione non ci sono esempi 3 × 3» (2024). Conti verificati; con SymPy gli altri due autospazi sono V_1 = Span((−2, 2, 1)) e V_2 = Span((0, −1, 1)), utili se si vuole completare l'esempio fino ad A = PDP⁻¹ (3 autovalori distinti, quindi diagonalizzabile).
- **Appunti 18 nov p. 1** → «Per A ∈ M(n) triangolare gli autovalori sono gli elementi sulla diagonale» → **già presente** in cap61.33-38.
- **Appunti 18 nov p. 1** → A diagonalizzabile se esiste una base di autovettori ⟺ A è simile a D = diag(λ_1, …, λ_n); Emanuele annota «diagonale/triangolare, non ricordo» → **già presente** in cap60.3 e 60.40: è **diagonale**. (Vale la pena dirglielo: è un dubbio scritto sul foglio.)
- **Appunti 18 nov p. 1** → Prop. autovettori di autovalori distinti sono indipendenti; Corollario n autovalori distinti ⟹ diagonalizzabile, con la dimostrazione (un autovettore per autovalore, n vettori indipendenti = base) → **già presente** in cap62.26-38 (stessa «dimostrazione» della lavagna 2024, cap62.38).
- **Appunti 18 nov p. 2** → Def. di autospazio V_λ = Ker(A − λI) = {autovettori} ∪ {0}, sottospazio; m_g(λ) = dim V_λ; m_a(λ) = molteplicità come radice → **già presente** in cap62.3-8 e cap63.3-8.
- **Appunti 18 nov p. 2** → Oss. «m_a(λ) = massimo k tale che (t − λ)ᵏ divide P_A(t)» → **già presente** nella sostanza in cap63.6-8 (lì con q(λ) ≠ 0 e «m fattori ma non m + 1»). La formulazione «massimo k che divide» è più diretta: si può aggiungere come riga in cap63.8 (facoltativo).
- **Appunti 18 nov p. 2** → **tabella λ / m_g / m_a** per la matrice 3 × 3 dell'esempio: m_a = 1 per 1, 2, 3; m_g(3) = dim V_3 = 1 → **manca** (va con l'esempio 3 × 3 sopra; blocco più vicino **cap63.16**, prima del teorema m_g ≤ m_a, o come esempio di cap63.24 «se m_a = 1 allora m_g = 1»). Nel foglio m_g(1) e m_g(2) sono in bianco: valgono 1.
- **Appunti 18 nov p. 2** → esempio A = ( 1 1 ; 0 1 ): m_a(1) = 2, V_1 = Span((1, 0)), m_g(1) = 1 ≠ 2 → **già presente** in cap63.11-16 (stesso esempio della lavagna 2024).
- **Appunti 18 nov p. 3** → Oss. m_g(λ) = n − dim Im(A − λI) = n − rg(A − λI) per il teorema della dimensione → **già presente** in cap63.9-10.
- **Appunti 18 nov p. 3** → Prop. 1 ≤ m_g(λ) ≤ m_a(λ) e «in particolare m_a = 1 ⟹ m_g = 1» → **già presente** in cap63.18-24. Piccola differenza: cap63.21 dice che alla lavagna 2024 c'era solo m_g ≤ m_a; nel 2026 c'è la catena completa con la conseguenza, che cap63.24 attribuisce alle dispense. Proposta: una frase in cap63.21.
- **Appunti 18 nov p. 3** → Def. di **somma diretta** come scrittura **unica di ogni v** = v_1 + … + v_m → **già presente** in cap62.46-50, ma **in contrasto con cap62.50**: «Alla lavagna la definizione è data direttamente in questa forma» (cioè con lo zero, 2024) e «il simbolo ⊕ … alla lavagna non compare». Nel 2026 il docente ha dato la forma delle dispense (unicità per ogni v), e ⊕ compare negli appunti (p. 4). Proposta: aggiornare cap62.50.
- **Appunti 18 nov p. 3** → Prop. somma diretta ⟹ dim V = Σ dim V_i e unione di basi = base → **già presente** in cap62.52-54.
- **Appunti 18 nov p. 3** → Prop. gli autospazi di autovalori distinti sono in somma diretta → **già presente** in cap62.56-60 (negli appunti l'enunciato è scritto male, vedi errori).
- **Appunti 18 nov p. 3** → Cor. A diagonalizzabile ⟺ 𝕂ⁿ = V_λ1 ⊕ … ⊕ V_λm → **già presente** in cap62.61-68.
- **Appunti 18 nov p. 3** → teorema di diagonalizzabilità con le condizioni (1) n radici contate con molteplicità e (2) m_g = m_a → **già presente** in cap63.26-29.
- **Appunti 18 nov p. 4** → **dimostrazione (direzione ⟸)**: da (1) + (2) Σ m_g(λ_i) = n, quindi 𝕂ⁿ = ⊕ V_λi, e unendo basi degli autospazi si ha una base di autovettori → **già presente** nella sostanza in cap63.31-33 (dimostrazione delle dispense, completa), ma **in contrasto con cap63.30**: «Il teorema non è dimostrato a lezione» (2024). Nel 2026 almeno questa direzione è stata fatta alla lavagna. Proposta: una frase in cap63.30.
- **Appunti 18 nov p. 4** → «es. in Foto 12:52» → l'esempio finale è solo in una foto che non è nel PDF. **Da chiedere a Emanuele** (potrebbe essere un 3 × 3 con m_g < m_a o la rotazione su ℂ).
- Non compaiono negli appunti 2026: l'esempio ( 2 1 ; 1 2 ) (cap62.9-22) e la rotazione ( 0 1 ; −1 0 ) su ℝ e su ℂ (cap63.36-43), entrambi della lavagna 2024.

---

## Errori negli appunti (conti verificati con SymPy)

Nessun conto numerico è sbagliato: tutti i risultati finali tornano. Ci sono però refusi di notazione che, ripassando dal foglio, possono confondere.

| Dove | Scritto | Giusto |
|---|---|---|
| 9 nov p. 1, es. 3 | «F(v) + F(v)» e «(4 ; 7) = (4 ; 10)» | F(v) + F(w), e (4 ; 7) + (4 ; 10) = (8 ; 17) |
| 9 nov p. 2 | Im(F) = {w ∈ V \| …} | w ∈ W |
| 9 nov p. 2 | dimostrazione «Im F sottospazio» interrotta al punto b | manca la chiusura per somma e per multipli |
| 11 nov p. 2 | «C = {w_1, …, w_n}» nella ricetta | w_m |
| 11 nov p. 2, ultima riga | f(a + bx + cx²) = (a + 2c)(5b + 3c)·x | (a + 2c) + (5b + 3c)x |
| 13 nov p. 1 | «Ricordiamo [F(v)]_C = [F]^B_C · [v]_C» | · [v]_B |
| 13 nov p. 1, esempio | «[id]^B_B′ [x]_B = (2 ; −1) = [x]_B» | = [x]_B′ |
| 13 nov p. 1 | «V → 𝕂ⁿ, v ↦ [v]_B» chiamata F_B | è F_B⁻¹ |
| 13 nov p. 2, prima riga | [id]^B_B′ = ([v_1]_B′ … [v_n]_B) | [v_n]_B′ |
| 13 nov p. 2, dim. | L_A · L_B(v) | L_A ∘ L_B |
| 13 nov p. 2, diagramma | freccia composta in basso «L_AB», con L_A applicata per prima | L_BA (la formula riquadrata [g ∘ f] = [g][f] è giusta); inoltre A e B indicano sia basi sia matrici |
| 16 nov p. 1 | «Un autovettore … v ∈ V con V ≠ 0» | v ≠ 0 |
| 16 nov p. 1 | f = L_A : 𝕂ⁿ → 𝕂ᵐ | 𝕂ⁿ → 𝕂ⁿ (endomorfismo) |
| 16 nov p. 1, es. 1 | «per ogni x»; «v_4 = e_4 = (−4 ; 1)» | per ogni λ; (−4, 1) non è un vettore della base canonica |
| 16 nov p. 1, es. 2 | «v_2 = e_2 = (0 ; 1 ; 1)» | e_2 = (0, 1, 0); il vettore (0, 1, 1) va bene ma non è e_2 |
| 16 nov p. 3 | det(A · λI_n) (due volte) | det(A − λI_n) |
| 16 nov p. 3 | primo fattore di A¹⁰⁰ scritto «( 2 −4 ; 0 1 )» | M = ( 1 −4 ; 0 1 ) (il passaggio dopo usa quella giusta) |
| 16 nov p. 3 | «Teorema di Brest» | teorema di Binet |
| 16 nov p. 3 | «le radici di A» | le radici di P_A |
| 18 nov p. 1 | «2t» sulla diagonale di A − tI | 2 − t |
| 18 nov p. 1 | «A è simile a D … diagonale/triangolare, non ricordo» | diagonale |
| 18 nov p. 2 | «V = Ker(A − λI)» | V_λ |
| 18 nov p. 2 | m_g(1) = dim Ker(A − I) = {y ∈ ℝ² \| …} | {v ∈ ℝ² \| …}, e una dimensione non è un insieme |
| 18 nov p. 3 | somma diretta scritta V_1 + … + V_m | V_1 ⊕ … ⊕ V_m (con + la Prop. sugli autospazi diventa «W = W») |
| 18 nov p. 3 | «λ_1, …, λ_n autovalori distinti … W ∈ 𝕂ⁿ … v = v_1 + … + v_m» | λ_1, …, λ_m; W ⊆ 𝕂ⁿ; v_i ∈ V_λi; tesi: la somma è diretta |
| 18 nov p. 3 | «B_1 ∈ V_1» | B_1 ⊆ V_1 |

## In che cosa la lezione 2026 differisce dalle registrazioni 2024/2025 usate per i capitoli

1. **Esempi nuovi** (in nessuna fonte usata finora: né dispense né lavagne 2024/2025): indipendenza di (1, 5, 3), (1, −1, 1), (3, 3, 5) (L13); proiezione ℝ³ → ℝ² (L14); coordinate di x² + 2x + 1 nella base {1, x + 1, x² + x} (L15); f : ℝ_2[x] → ℝ_1[x] data solo dalla matrice ( 1 0 2 ; 0 5 3 ) (L15); cambio di base nei polinomi {1, 1 + x} → {1 + x, 2 + x} (L16); cambio di base {(1, 0), (1, 1)} → {(1, 1), (0, 1)} (L16); A = ( 1 0 0 ; 1 2 0 ; 2 1 3 ) con autospazio e tabella delle molteplicità (L18). Varianti numeriche di esempi già presenti: F(a, b) = (2a − 1, a + b + 3) e (a², 2a + 3b) (L14).
2. **Esempi delle dispense al posto di quelli della lavagna.** Nel 2026 il docente segue più da vicino le dispense: in L14 usa (2a + b, a + 3b) (non (3x + 2y, x) del 2024); in L17 usa ( 3 4 ; 0 2 ) e la 3 × 3 dell'Esempio 17.4 (non la motivazione con ( 1 0 ; 0 1/2 ) e l'«oracolo» per ( 1 2 ; 2 1 ) del 2025); la diagonalizzazione è scritta D = M⁻¹AM come nelle dispense (non A = PDP⁻¹ come alla lavagna 2025); la somma diretta è definita con l'unicità della scrittura (dispense 18.4), non con lo zero (lavagna 2024).
3. **Dimostrazioni fatte nel 2026 che nel 2024/2025 erano solo enunciate**: Ker e Im sottospazi (L14, contro cap47.21); iniettività di F_B (L15, contro cap49.33); stesso polinomio caratteristico per matrici simili (L17, contro cap61.67); direzione ⟸ del teorema di diagonalizzabilità (L18, contro cap63.30). Enunciati generali che nel 2025 erano solo nel caso particolare: isomorfismo ⟺ matrice invertibile (L16, contro cap53.43); 1 ≤ m_g ≤ m_a con la conseguenza m_a = 1 ⟹ m_g = 1 (L18, cap63.21).
4. **Rotazione di angolo θ generale** con la matrice ( cos θ −sin θ ; sin θ cos θ ) alla lavagna (L17), contro cap61.58 «non presente … in lezione»; nel 2025 c'era solo Rot_π/2. Negli appunti 2026 manca invece la rotazione su ℂ (cap61.51-57 e cap63.36-43).
5. **Un esempio 3 × 3 a lezione** (L18), contro cap63.51 «A lezione non ci sono esempi 3 × 3».
6. **Ordine.** Il corollario su iniettività/suriettività e dim V ≤ dim W apre la L15 (nel 2024 chiudeva la L14); nel 2026 la L14 non arriva al collegamento con Rouché-Capelli (cap48.7-13), che negli appunti non c'è. In L17 il polinomio caratteristico arriva già alla fine (nel 2025 la catena di equivalenze era il centro della seconda parte); in L18 si parte dall'enunciato «autovalore ⟺ radice di P_A».
7. **Notazioni.** Basi chiamate A, B, C nella composizione (come lavagna 2025); P_V e P_W per i cambi di base (capitolo: P e Q); identità scritta id (capitolo: I_V); variabile del polinomio caratteristico λ in L17 e t in L18.

## Aggiunte proposte, in ordine di importanza

1. **cap61 (dopo cap61.39) o cap62 (dopo cap62.23)**: esempio 3 × 3 triangolare inferiore ( 1 0 0 ; 1 2 0 ; 2 1 3 ), autovalori 1, 2, 3 e autospazio V_3 = Span((0, 0, 1)); poi in **cap63 (dopo cap63.16 o in cap63.24)** la tabella m_a/m_g. Correggere di conseguenza cap63.51.
2. **cap51 (dopo cap51.19)**: f : ℝ_2[x] → ℝ_1[x] data dalla matrice ( 1 0 2 ; 0 5 3 ), f(a + bx + cx²) = (a + 2c) + (5b + 3c)x.
3. **cap52 (dopo cap52.30)**: cambio di base nei polinomi B = {1, 1 + x}, B′ = {1 + x, 2 + x}, con A = ( −1 1 ; 1 0 ) e il controllo A[x]_B = [x]_B′ = (2, −1).
4. **cap49 (dopo cap49.49)**: coordinate di x² + 2x + 1 nella base {1, x + 1, x² + x} = (0, 1, 1).
5. **cap48 (prima di cap48.6)**: proiezione (x, y, z) ↦ (x, y), Ker = asse z, Im = ℝ², 1 + 2 = 3.
6. **cap59 (in cap59.46)**: matrice della rotazione di angolo θ e colonne L_A(e_1), L_A(e_2), come alla lavagna 2026; aggiornare cap61.58.
7. **cap60 (cap60.26 e cap60.58)**: il conto esplicito D = M⁻¹AM = ( 3 0 ; 0 2 ) con M⁻¹ = ( 1 4 ; 0 1 ), e A² = ( 9 20 ; 0 4 ) come «metodo 1».
8. **cap44 (vicino a cap44.12)**: (1, 5, 3), (1, −1, 1), (3, 3, 5) dipendenti, v_3 = v_1 + 2v_2.
9. **Frasi «nel 2026» da aggiornare** (contrasti): cap47.21, cap49.33, cap53.43, cap61.67, cap62.50, cap63.21, cap63.30, cap63.51, cap61.58.
10. Minori: non esempio (3, 1) in cap59.31; «m_a = massimo k con (t − λ)ᵏ | P_A» in cap63.8.

Da chiedere a Emanuele: le foto della lavagna citate negli appunti (9 nov 11:59 e 12:48/49, 16 nov 10:18 intera, 18 nov 12:52), che contengono almeno un esempio non trascritto.
