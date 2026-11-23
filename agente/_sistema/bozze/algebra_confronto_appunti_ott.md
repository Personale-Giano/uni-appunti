# Algebra lineare: appunti a mano di ottobre confrontati con i capitoli del sito
(23 nov 2026. Trascrizioni in `_sistema/fonti_testo/Algebra lineare/`: `L5_appunti_14ott.md`, `L6_appunti_19ott.md`, `L7_appunti_21ott.md`, `L9_appunti_26ott.md`, `L10_appunti_28ott.md`. Capitoli letti da `quaderno-privato/contenuti/algebra.json`; nessuna modifica fatta al sito. Conti verificati con SymPy.)

**Fonti dei capitoli.** I cap. 14-26 (L5-L7) vengono dalle dispense e dalle lavagne delle registrazioni 2025 (`L5-L7_lavagne_video2025.md`, 1, 6 e 8 ott 2025). Per queste lezioni, quindi, gli appunti del 2026 sono una fonte nuova. I cap. 31-37 (L9-L10) vengono invece anche da `fonti/Appunti/Algebra luendi.pdf` e `28 Ottobre.pdf`: il secondo è identico, a parte la compressione, alla scansione `Algebra_2026/28 Ottobre/28 Ottobre.pdf` trascritta qui. Molte voci di L9-L10 risultano quindi «già presenti».

Negli appunti di L5-L7 diverse parti sono indicate solo come «foto hh:mm» (foto della lavagna che non sono nella scansione): le quattro proprietà della somma, le proprietà 5-7, l'esempio di somma di matrici, il controllo di W₂, gli esempi di combinazione lineare. Non ho potuto confrontarle.

## Lezione 5, 14 ottobre (cap. 14-18)
- **14 ott p. 1, definizione di ℝⁿ ed esempi n = 1, 2, 3 (con il punto P(1, 2, 3))** → **già presente** in cap14.6-14.18.
- **14 ott p. 1, somma e moltiplicazione per ℝ come funzioni + : ℝⁿ × ℝⁿ → ℝⁿ e · : ℝ × ℝⁿ → ℝⁿ** → **già presente** in cap15.4-15.10 e cap17.6-17.7.
- **14 ott p. 1, definizione di spazio vettoriale su un campo 𝕂 (proprietà 1-8, la 8 è 1·v = v)** → **già presente** in cap16.3-16.10 e cap17.5-17.10. **Svista negli appunti**: la moltiplicazione per scalare è scritta «(a, v) ↦ v·w», ma è a·v.
- **14 ott p. 1, Def ①-② gruppo e gruppo commutativo/abeliano** → **già presente** in cap16.21-16.27.
- **14 ott p. 1, Def ③ vettori e scalari** → **già presente** in cap15.16 e cap17.5.
- **14 ott p. 1, Def ④ (Proposizione): 0_V è unico e 0·v = 0_V; −v è unico e −v = (−1)·v** → **manca in parte nel cap. 18** (blocco più vicino **cap18.3-18.5**). Le formule 0·v = 0_V e (−1)·v = −v ci sono (cap18.4-18.5, con dimostrazione). Manca l'**unicità** dello zero e dell'opposto, che nel 2026 è nell'enunciato e che le lavagne 2025 non hanno. **Aggiunta consigliata** dopo cap18.5: «Lo zero 0_V e l'opposto di ogni vettore sono unici», con la dimostrazione in due righe (se 0 e 0′ sono neutri, 0 = 0 + 0′ = 0′; se u e u′ sono opposti di v, u = u + (v + u′) = (u + v) + u′ = u′). Questa dimostrazione non è negli appunti: va segnata come aggiunta nostra, oppure presa dalle dispense se c'è.
- **14 ott p. 1, «d'ora in poi v + w e a·v per le operazioni in V» ed esempio ℝⁿ** → **già presente** in cap17.22.

## Lezione 6, 19 ottobre (cap. 17-22)
- **19 ott p. 1, richiamo ed esempi di spazi: 𝕂, 𝕂ⁿ, successioni in 𝕂, funzioni [0, 1] → 𝕂, 𝕂[x]** → **già presente** in cap17.22-17.25 e cap18.17-18.26. Le successioni e le funzioni su [0, 1] sono in cap18.26, dove sono attribuite alle dispense.
- **19 ott p. 1, definizione di matrice, aᵢⱼ, «prima le righe e poi le colonne», M(m, n, 𝕂)** → **già presente** in cap19.5-19.13.
- **19 ott p. 1, esempi di matrici** → **già presente** in cap19.15-19.19, con esempi in parte diversi (2026: ( 1 7 √2 ; 3 π i ) ∈ M(2, 3, ℂ) e la riga (1, 7, −2), che c'è anche nel cap19.17). **Errori negli appunti**: «( 1 2 3 ; 4 5 6 ; 7 8 9 ) ∈ M(3, 3, ℕ)» non va bene, perché ℕ non è un campo (si scrive M(3, 3, ℝ)); la colonna (7, √2, π) è scritta «∈ M(4, 1, ℝ) = ℝ³», ma ha 3 entrate, quindi è in M(3, 1, ℝ). Nel capitolo è giusto (cap19.18: M(m, 1, 𝕂) = 𝕂ᵐ).
- **19 ott p. 1, somma (A + B)ᵢⱼ = aᵢⱼ + bᵢⱼ, prodotto (λA)ᵢⱼ = λaᵢⱼ, M(m, n, 𝕂) spazio vettoriale** → **già presente** in cap19.22-19.29.
- **19 ott p. 1, definizione di sottospazio (0_W = 0_V; operazioni definite in V)** → **già presente** in cap20.3-20.10.
- **19 ott p. 2, W₁ = {(a, b, 0)} è un sottospazio, W₂ = {(a, b, 1)} no** → **già presente**, con gli stessi insiemi e la stessa verifica, in cap20.13-20.25.
- **19 ott p. 2, 𝕂_k[x] (grado ≤ k) è un sottospazio di 𝕂[x]** → **già presente** in cap20.35.
- **19 ott p. 2, matrici quadrate, diagonali, triangolari superiori e inferiori, simmetriche, antisimmetriche** → **già presente** in cap21.2-21.9.
- **19 ott p. 2, «Triangolare: se è o tr. sup. o tr. inf.»** → **manca nel cap. 21** (blocco più vicino **cap21.7**). Si può aggiungere dopo cap21.9, con un trabocchetto che negli appunti non c'è: l'insieme delle matrici triangolari (superiori **o** inferiori) **non** è un sottospazio, perché per esempio ( 1 1 ; 0 0 ) + ( 0 0 ; 1 0 ) = ( 1 1 ; 1 0 ) non è triangolare. È per questo che la proposizione (cap21.31) elenca Tˢ(n) e Tⁱ(n) separati. Il controesempio va segnato come nostro.
- **19 ott p. 2, esempi 2 × 2** → **già presente** in cap21.18-21.23 (con matrici diverse) e cap21.26-21.28. Due esempi del 2026 non ci sono:
  - «( 0 0 ; 0 1 ) è diagonale, triangolare superiore e inferiore, simmetrica, **ma non antisimmetrica!**»: cap21.26 ha la stessa matrice, ma senza il «non antisimmetrica» (per cui basta notare che sulla diagonale c'è un 1, cap21.27). Si può completare con una frase dopo **cap21.26**;
  - «( 1 2 ; 3 4 ) non è niente di tutto questo»: **manca** (blocco più vicino **cap21.26**). Utile come contro-esempio.
- **19 ott p. 3, notazione: diagonale principale, M(n) = M(n, 𝕂) = M(n, n, 𝕂), D(n), Tˢ(n), Tⁱ(n), S(n), A(n), che sono sottospazi** → **già presente** in cap21.2-21.3, cap21.29, cap21.31. Negli appunti si scrive Tˢ, Tⁱ con l'indice in alto, nel capitolo Ts, Ti: è la stessa notazione.
- **19 ott p. 3, combinazione lineare λ₁v₁ + … + λ_kv_k** → **già presente** in cap22.5-22.7. **Differenza 2026/2025**: nel 2026 le combinazioni lineari cominciano alla fine della lezione 6, nel 2025 all'inizio della 7. Per il capitolo non cambia niente.

## Lezione 7, 21 ottobre (cap. 22-26)
- **21 ott p. 1, Span(v₁, …, vₙ) è un sottospazio di V** → **già presente** in cap22.11-22.21. **Imprecisione negli appunti**: la definizione «Span(vᵢ): insieme di tutti i multipli dei vettori vᵢ» è sbagliata se presa alla lettera. Lo Span contiene tutte le combinazioni lineari, non solo i multipli di ciascun vettore; è giusta la riga sopra, {a₁v₁ + … + aₙvₙ}. Il capitolo è corretto (cap22.12).
- **21 ott p. 1, esempio: in ℝ², Span((1, 2), (2, 4)) = {(a + 2b)(1, 2)} = Span((1, 2)), con il disegno della retta; ⚠ 2v₁ − v₂ = 0** → **manca nel cap. 22-23** (blocchi più vicini **cap22.16**, dove compare solo Span((1, 2)), e **cap23.7-23.9**, dove la ridondanza è spiegata con un altro esempio). **Differenza 2026/2025**: alla lezione 2026 il docente ha usato questo esempio (due vettori multipli: lo Span è una retta, non il piano), mentre il capitolo usa quello della lezione 2025 (v₁ = (1, 0), v₂ = (−1, 0), v₃ = (0, 1)). **Aggiunta consigliata** dopo cap22.16: è l'esempio più semplice di «due vettori che generano solo una retta», e prepara la dipendenza lineare. Conti verificati: a(1, 2) + b(2, 4) = (a + 2b)(1, 2), 2(1, 2) − (2, 4) = (0, 0).
- **21 ott p. 1, es. 2: Span((1, 0), (0, 1)) = ℝ² e il disegno v = a w₁ + b w₂** → **già presente nella sostanza** in cap23.16 e cap25.13 (coordinate di (3, 2) nella base canonica).
- **21 ott p. 1, definizioni di linearmente indipendenti, generatori, base** → **già presente** in cap23.19-23.25. **Svista negli appunti**: l'indipendenza è scritta «⟹ a₁ = a₂ = … = aₙ», senza «= 0». Nel capitolo è giusta.
- **21 ott p. 1, tabella: {v₁, v₂} = {(1, 2), (2, 4)} non è l.i., non genera, non è una base; {w₁, w₂} lo è** → **manca** in questa forma (blocco più vicino **cap23.27**, che riassume gli esempi del 2025). Si può aggiungere insieme all'esempio qui sopra: la tabella a tre colonne (l.i.? generatori? base?) è un buono schema di ripasso.
- **21 ott p. 2, «se non sono l.i. sono linearmente dipendenti»** → **già presente** in cap23.21.
- **21 ott p. 2, base ⟹ coefficienti unici** → **già presente** in cap25.3-25.7.
- **21 ott p. 2, dipendenti ⟺ un vᵢ è combinazione degli altri** → **già presente** in cap24.2-24.3.
- **21 ott p. 2, «fatti»: {v₁} l.i. ⟺ v₁ ≠ 0; {v₁, v₂} l.i. ⟺ nessuno è multiplo dell'altro** → **già presente** in cap24.9-24.10.
- **21 ott p. 2, teorema: due basi hanno lo stesso numero di elementi; definizione di dimensione e di dimensione finita** → **già presente** in cap26.2-26.4.
- **21 ott p. 2, esempio 𝕂ⁿ con e₁, …, eₙ; osservazione «i coefficienti della combinazione lineare sono le componenti del vettore»** → **già presente** in cap26.10-26.15 (la frase è cap26.15). Svista negli appunti: un segno «−» al posto di «+» davanti ad aₙeₙ.
- **Differenza di calendario 2026/2025**: nel 2026 la lezione 7 arriva fino alla dimensione e alla base canonica (cap. 26); nel 2025 le stesse cose erano divise in modo diverso. Per i capitoli non cambia niente.

## Lezione 9, 26 ottobre (cap. 31-33)
- **26 ott p. 1, definizione del determinante con Sₙ e sgn(σ) = (−1)ᵏ, trasposizione, notazione [σ(1) … σ(n)]** → **già presente** in cap31.5-31.15. **Svista negli appunti**: il titolo «Il determinante di una radice quadrata» sta per «di una matrice quadrata».
- **26 ott p. 1, casi n = 1, 2, 3 e la formula 3 × 3** → **già presente** in cap31.17-31.22 (con gli stessi sei termini). **Errori negli appunti**: nella matrice 2 × 2 l'entrata in alto a destra è scritta a₂₁ (è a₁₂); la permutazione [2, 1] è chiamata «id» (è lo scambio σ, con sgn = −1).
- **26 ott p. 1, esempio 2 × 2: det( 3 1 ; 2 4 ) = 10** → giusto; nel capitolo c'è un altro esempio (cap31.24, det( 1 2 ; −1 4 ) = 6). Non serve aggiungerlo.
- **26 ott p. 1, esempio 3 × 3: det( 1 2 1 ; 2 1 2 ; −1 0 1 ) = 1 − 4 + 1 + 0 − 4 + 0 = −6** → **già presente** in cap31.24-31.25 (stessa matrice, stesso risultato; SymPy: −6).
- **26 ott p. 1, determinante di una triangolare = prodotto della diagonale; det(ᵗA) = det A** → **già presente** in cap32.6-32.7 e cap32.16.
- **26 ott p. 1, teorema dello sviluppo di Laplace lungo una riga, definizione di Cᵢⱼ** → **già presente** in cap33.3-33.7.
- **26 ott p. 1-2, esempio sviluppato lungo la 1ª e la 3ª riga** → **già presente** in cap33.15-33.21 (stessa matrice; il capitolo aggiunge la 2ª colonna). **Errore di copiatura negli appunti**: la sottomatrice C₁₂ è scritta ( −2 2 ; 1 1 ), che ha det −4; quella giusta è ( 2 2 ; −1 1 ), con det 4, che è il valore usato nel conto. Il risultato finale −6 è giusto, e nel capitolo (cap33.17) la matrice è giusta.

## Lezione 10, 28 ottobre (cap. 34-36)
- **28 ott p. 1, richiamo: det 2 × 2 = ad − bc, det della triangolare inferiore** → **già presente** in cap31.19 e cap32.6.
- **28 ott p. 1, det(A¹ | λAⁱ | Aⁿ) = λ det(A¹ | Aⁱ | Aⁿ)** → **già presente** in cap34.5. Negli appunti è scritta sotto il titolo «Sviluppo di Laplace», ma è la proprietà del fattore comune su una colonna.
- **28 ott p. 1, determinante 4 × 4 con 5i e √2** → **già presente**, come esercizio 9.14, in cap34.29-34.36. Gli appunti si fermano a 40i(−det(…) − det(…)); i due 3 × 3 valgono 9 e 3, quindi det = 40i·(−12) = −480i, come nel capitolo (SymPy).
- **28 ott p. 1, interpretazione geometrica: Area(P) = |det A| in ℝ², Vol(P) = |det A| in ℝ³** → **già presente** in cap35.22-35.28.
- **28 ott p. 1, le tre proprietà (scambio, multiplo, somma del multiplo di un'altra colonna)** → **già presente** in cap35.3-35.5.
- **28 ott p. 2, esempio ( 1 1 ; 0 2 ) → C₂ → C₂ + C₁ → ( 1 2 ; 0 2 ), stessa area (P₁ e P₂)** → **già presente** in cap35.29 (entrambi i det valgono 2).
- **28 ott p. 2, mosse di Gauss Cᵢ ↔ Cⱼ, Cᵢ → λCᵢ, Cᵢ → Cᵢ + λCⱼ** → **già presente** in cap35.6.
- **28 ott p. 2, colonne dipendenti ⟺ det A = 0, con l'esempio ( 1 3 7 ; 1 3 5 ; 1 3 10 )** → **già presente** in cap35.16-35.18 (stessa matrice; det = 0).
- **28 ott p. 2, la 3ª mossa introduce zeri: det( 1 3 7 ; 1 5 5 ; 1 4 10 ) = 8** → **già presente** in cap35.11-35.15 (stesso conto; SymPy: 8).
- **28 ott p. 2, identità Iₙ, A·Iₙ = Iₙ·A = A, matrice invertibile, inversa** → **già presente** in cap36.2-36.5.
- **28 ott p. 2, teorema di Binet e det(A⁻¹) = 1/det A** → **già presente** in cap36.8-36.12.
- **28 ott p. 2, cofattori, cof(A), A⁻¹ = (1/det A)·ᵗcof(A), caso 2 × 2 e regola veloce** → **già presente** in cap36.15-36.28.
- **28 ott p. 3, esempio A = ( 1 0 1 ; 0 2 1 ; 3 0 0 )** → **già presente** in cap36.30-36.45 (stessa matrice, cofattori giusti). **Errori di copiatura negli appunti**: i nove cofattori sono giusti, ma nella matrice cof(A) il cof₂₂ è scritto 3 invece di −3, e nella trasposta la seconda riga è (3, 3, 1) invece di (3, −3, −1). Quindi la A⁻¹ degli appunti è sbagliata nella seconda riga. Quella giusta è ( 0 0 1/3 ; −1/2 1/2 1/6 ; 1 0 −1/3 ), come in cap36.44 (SymPy). Da segnalare a Emanuele: chi ripassa dagli appunti trova un'inversa sbagliata.

## Riepilogo
- Errori negli appunti (il sito è giusto in tutti i casi): M(3, 3, ℕ) e M(4, 1, ℝ) per una colonna di 3 entrate (19 ott); Span come «multipli» e «a₁ = … = aₙ» senza «= 0» (21 ott); a₂₁ al posto di a₁₂ e «id = [2, 1]» (26 ott); C₁₂ copiata male (26 ott, risultato giusto); cof₂₂ e la seconda riga dell'inversa (28 ott, **risultato sbagliato**).
- Contrasti veri tra appunti e capitoli: nessuno.
- Differenze tra lezione 2026 e fonti dei capitoli (lavagne 2025): esempio Span((1, 2), (2, 4)) e tabella l.i./generatori/base (2026) al posto dell'esempio v₁ = (1, 0), v₂ = (−1, 0), v₃ = (0, 1) (2025); unicità di 0_V e −v nell'enunciato (2026); «triangolare» generica e gli esempi ( 0 0 ; 0 1 ) non antisimmetrica e ( 1 2 ; 3 4 ) (2026); ordine diverso tra le lezioni 6 e 7.
- Aggiunte proposte, in ordine di utilità: cap. 22 esempio Span((1, 2), (2, 4)) = Span((1, 2)) con 2v₁ − v₂ = 0 (dopo cap22.16), e la tabella in cap. 23 (dopo cap23.27); cap. 18 unicità di zero e opposto (dopo cap18.5); cap. 21 «triangolare» con il trabocchetto «non è un sottospazio» (dopo cap21.9) e i due esempi dopo cap21.26. Prima di inserire qualcosa nei cap. 1-13, che sono studiati, bisogna controllare le evidenziazioni; i cap. 14-26 per ora non risultano studiati.
