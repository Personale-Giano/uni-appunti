# Matematica discreta: appunti a mano di Emanuele confrontati con i capitoli del sito
(23 nov 2026. Trascrizioni in `_sistema/fonti_testo/Matematica discreta/`: `L11_appunti_27ott.md`, `L12_appunti_29ott.md`, `L14_appunti_10nov.md`, `L16_appunti_17nov.md`, `Tutorato1_appunti.md`. Capitoli letti da `quaderno-privato/contenuti/matematica-discreta.json`; nessuna modifica fatta al sito. Conti verificati con SymPy.)

## Scansioni senza contenuto
- **13 ottobre** («13 Ottobre/Quadretti.pdf», sarebbe la lezione 6): pagina a quadretti **bianca**, l'immagine incorporata è solo il modello del foglio. Nessuna trascrizione. La prima metà della lezione 6 resta scoperta, come già scritto in STATO.
- **19 novembre** («19 Novembre/Quadretti - Grande.pdf», lezione 17): anche questa è **bianca**. Il contenuto del 19 nov (unicità della fattorizzazione, infinità dei primi) si trova però in fondo alla scansione del 17 nov, pagina 2 (testo e foto della lavagna): l'ho trascritto in `L16_appunti_17nov.md`, con una nota.
- Le scansioni del 27 e 29 ott non hanno ancora una trascrizione. Quella del 29 ott è identica, a parte la compressione, a `fonti/Appunti/29 Ottobre .pdf`, che era già stato usato per i cap. 34-35.

## Lezione 11, 27 ottobre (cap. 32-33)
- **27 ott p. 1, potenza di un binomio**: (a + b)¹⁰ con gli «interruttori», C_k = (n su k) → **già presente** in cap32.2-32.4.
- **27 ott p. 1, definizione di permutazione, Sₙ, |Sₙ| = n!, le tre proprietà, composizione non commutativa** → **già presente** in cap32.7-32.27. Negli appunti la proprietà 2 («Se π ∈ Sₙ allora…») non è finita: nel capitolo c'è per intero (cap32.24).
- **27 ott p. 1, esempio n = 7: π, π⁻¹, la tabella «2 5 3 1 5» che non è una permutazione** → **già presente**, con gli stessi numeri, in cap32.31-32.36 e cap32.34.
- **27 ott p. 1, composizione σ ∘ π** → **in contrasto con cap32.43, ma l'errore è negli appunti.** Gli appunti scrivono le prime tre colonne «1 2 3 / 5 2 6 / 6 5 3». La riga di mezzo è σ(1), σ(2), σ(3); l'ultima è π⁻¹ applicata a quella riga, cioè π⁻¹ ∘ σ (è stata letta la riga di π⁻¹ al posto di quella di π). Con la convenzione del corso (da destra a sinistra) σ ∘ π = [6 1 7 5 2 3 4], come nel capitolo (SymPy). La riga «π ∘ σ» è lasciata senza conto: è [2 4 5 3 6 7 1], come in cap32.43.
- **27 ott p. 1, definizione di ciclo** → **già presente** in cap33.14-33.16. Negli appunti manca la condizione C(k) = k fuori da {i₁, …, i_ℓ}, che il capitolo ha (e che c'è negli appunti del 29 ott).
- **27 ott p. 2, cicli disgiunti e la proposizione C₁ ∘ C₂ = C₂ ∘ C₁** → **già presente** in cap33.29 e cap33.36-33.42. Negli appunti la dimostrazione è appena iniziata (i_r → i_{r+1}); il capitolo la dà completa, con i tre casi.

## Lezione 12, 29 ottobre (cap. 34-35)
- **29 ott p. 1, definizione di ciclo con c(t) = t ed esempio (4 1 2 5)** → **già presente** in cap34.2-34.3 (stesso esempio).
- **29 ott p. 1, formula dei cicli di lunghezza ℓ: (1/ℓ)·n!/(n − ℓ)!** → **già presente** in cap34.12 (controllata per n = 5, ℓ = 3 → 20 e n = 6, ℓ = 4 → 90).
- **29 ott p. 1, teorema di scomposizione «essenzialmente unica»** → **già presente** in cap34.17-34.19.
- **29 ott p. 1, definizione di tipo** → **già presente** in cap34.31. Negli appunti si legge «ℓ₁ = ℓ₂ ≥ ℓ₃»: va inteso ℓ₁ ≥ ℓ₂ ≥ … ≥ ℓ_k, come nel capitolo.
- **29 ott p. 1, «Fisso n: elencare i possibili tipi»** → **già presente** in cap34.36 (tipi di S₄).
- **29 ott p. 1, dimostrazione (P.1) e (P.2)** → **già presente** in cap35.3-35.9 (stesso insieme T e stesso schema t₁ → t₂ → …). Gli appunti si fermano all'esistenza; l'unicità è in cap35.14-35.25.

## Lezione 14, 10 novembre (cap. 39-44)
- **10 nov p. 1, ogni permutazione è composizione di scambi; (1 2 … ℓ) = (ℓ−1 ℓ) ∘ … ∘ (2 ℓ)(1 ℓ)** → **già presente** in cap39.12-39.13 e cap39.35. Formula verificata con SymPy per ℓ = 2, …, 6.
- **10 nov p. 1, NB: la scrittura in scambi non è unica** → **già presente** in cap39.41-39.43.
- **10 nov p. 1, teorema della parità** → **già presente** in cap40.14 e cap41.3.
- **10 nov p. 1, 1° passo: ridursi all'identità** → **già presente** in cap41.7-41.11. Piccola differenza di forma: gli appunti usano id = π⁻¹ ∘ π, il capitolo usa id = π ∘ π⁻¹. Si arriva comunque a k + ℓ scambi, quindi non c'è niente da correggere.
- **10 nov p. 1, osservazione: gli scambi con 1 sono nessuno oppure almeno due** → **già presente** in cap41.18-41.23.
- **10 nov p. 1, le trasformazioni per spostare gli 1 a destra** → **già presente** in cap41.26-41.30. Negli appunti la prima è scritta «(1 a)(5 c) = (b c)(1 a)»: «5» è una «b» scritta male, come dice la condizione {1, a} ∩ {b, c} = ∅ scritta lì accanto. Le tre uguaglianze sono verificate con SymPy.
- **10 nov p. 1, si ripete con 2, 3, …, n fino a zero scambi** → **già presente** in cap41.37-41.39.
- **10 nov p. 1, la parità dal tipo, esempio di tipo (3, 5, 6)** → **in contrasto con cap42.27, ma l'errore è negli appunti.** Gli appunti scrivono «2, 4, 5 = 2 scambi». Il totale è 2 + 4 + 5 = 11, quindi la permutazione è dispari, come in cap42.27. Inoltre, per la definizione del 29 ott, il tipo va scritto in ordine decrescente: (6, 5, 3).
- **10 nov p. 1, «In realtà non serve sapere il tipo»** → **già presente** in cap42.29-42.31.
- **10 nov p. 1, 𝒜ₙ, 𝒟ₙ e |𝒜ₙ| = |𝒟ₙ| = n!/2 con F e G** → **già presente** in cap42.34-42.44, ma con una **differenza di scrittura**: negli appunti del 2026 si compone a sinistra, F(π) = (1 2) ∘ π e G(σ) = (1 2) ∘ σ; il capitolo compone a destra, F(π) = π ∘ (1 2). Funzionano entrambe. Si può aggiungere una riga dopo **cap42.43**: «A lezione F e G sono state scritte come (1 2) ∘ π e (1 2) ∘ σ; la dimostrazione è identica».
- **10 nov p. 2, foto della lavagna: ℤ, addizione e moltiplicazione con le loro proprietà** → **già presente** in cap43.3-43.10. Alla lavagna la distributiva è scritta (a + b)x = ax + bx, nel capitolo a·(b + c) = a·b + a·c: è la stessa proprietà.
- **10 nov p. 2, foto: la struttura moltiplicativa è più complicata (1, 2, 4, 8, (−1)ⁿ)** → **già presente** in cap43.24-43.29. Nella foto non si legge bene il risultato di (−1)³ (sembra «= 1»): vale −1, come in cap43.28.
- **10 nov p. 2, foto: definizione di m | n, 3 | 12, 2 ∤ −7, relazione non simmetrica, quindi non di equivalenza** → **già presente** in cap44.2-44.8.
- **10 nov p. 2, foto: se d divide due tra a, b, s = a + b, divide anche il terzo, con dimostrazione in due casi** → **già presente** in cap44.11-44.18.
- **10 nov p. 2, foto: invertibili, irriducibili, primi** → **già presente** in cap44.22-44.28.

## Lezione 16, 17 novembre (cap. 46, 49-52), più la parte del 19 nov (cap. 53)
- **17 nov p. 1, divisione euclidea a = bq + r, 0 ≤ r < |b|** → **già presente** in cap46.3.
- **17 nov p. 1, «algoritmo per il calcolo del MCD»** (negli appunti c'è solo il titolo) → **già presente** nel cap. 49.
- **17 nov p. 1, identità di Bézout d = Aa + Bb** → **già presente** in cap50.3.
- **17 nov p. 1, equazioni ax + by = c a soluzioni intere: si risolvono se e solo se MCD(a, b) | c** → **già presente** in cap51.3 e cap51.10.
- **17 nov p. 1, esempio 12x + 9y = c** (solo l'equazione, senza conto) → **manca nel cap. 51** (blocco più vicino **cap51.11**). È solo uno spunto: MCD(12, 9) = 3, quindi ci sono soluzioni se e solo se 3 | c. Si può aggiungere come esempio veloce del criterio.
- **17 nov p. 1, «se r divide a e b, allora r divide ax + by qualunque siano x, y»** → **già presente** in cap51.13-51.15 (è la parte ⟹ della dimostrazione).
- **17 nov p. 1, esempio 6x + 10y = 8: si risolve 6x + 10y = 2 con x = 2, y = −1 e si moltiplica per 4** → **manca nel cap. 51** (blocco più vicino **cap51.20**, dove si dice di scrivere Bézout e moltiplicarla). **Aggiunta consigliata**: è l'esempio numerico più semplice del metodo, fatto a lezione nel 2026, e nel capitolo non c'è (cap51.33 usa 252 e 198). Conti: 6·2 + 10·(−1) = 2; 6·8 + 10·(−4) = 48 − 40 = 8. Negli appunti «x + by» sta per «ax + by».
- **17 nov p. 1, il «1° passo» ax₀ + by₀ = d ⟹ a(kx₀) + b(ky₀) = kd = c** → **già presente** in cap51.16-51.19.
- **17 nov p. 1, definizioni di irriducibile e primo, teorema «irriducibile ⟺ primo»** → **già presente** in cap47.4, cap47.9, cap52.31-52.32.
- **17 nov p. 1, dimostrazione «primo ⟹ irriducibile»** → **già presente** in cap47.16-47.22, con un'altra strada. Gli appunti fanno così: n | a, quindi a = kn, n = kbn, 1 = kb e b = k = ±1. Il capitolo passa invece per |n| ≤ |a| e |b| ≤ 1. La versione degli appunti è più corta e si potrebbe aggiungere come seconda dimostrazione dopo **cap47.22**, con una precisazione: il passaggio da n = kbn a 1 = kb richiede n ≠ 0, che è garantito da n ∉ {0, ±1}.
- **17 nov p. 1-2, dimostrazione «irriducibile ⟹ primo» con Bézout** → **già presente** in cap52.8-52.28: il capitolo la divide in lemma e corollario, gli appunti la fanno in un colpo solo. **Errori negli appunti**: «n non divide d» va letto «n non divide a»; il fatto che MCD(n, a) = 1 è affermato senza dirne il motivo (lo dà l'irriducibilità, come in cap52.25-52.27); a p. 2 le lettere A e B sono scambiate rispetto alla riga di prima. Il conto finale n(Ak + Bb) = b ⟹ n | b è giusto.
- **17 nov p. 2, teorema fondamentale dell'aritmetica** → **già presente** in cap53.3. Negli appunti l'ultimo fattore è scritto «pₙ»: è p_s, perché n è già il numero da fattorizzare.
- **17 nov p. 2, esistenza «per induzione: suppongo l'esistenza vera per tutti i numeri < |n|; n = ab con 1 < a, b < n»** → **già presente nella sostanza** in cap53.13-53.20, con una **differenza di forma**: nel 2026 a lezione l'esistenza è dimostrata con l'induzione forte, mentre il capitolo, scritto dagli appunti del docente, usa il minimo controesempio. Il cap53.20 dice già che le due cose sono lo stesso ragionamento. Si può aggiungere una riga dopo **cap53.20**: «A lezione la stessa dimostrazione è stata fatta per induzione forte».
- **17 nov p. 2, unicità: p₁ | q₁ ⋯ q_s, quindi p₁ divide un qⱼ; foto 1: si semplifica, si ripete, «1 = q_{r+1} ⋯ q_s», «siccome qⱼ > 1 questo significa che s = r»** → **già presente** in cap53.22-53.29. Negli appunti la riga «p₁ | q₁ ⟹ p₁ | q₁» va letta «⟹ p₁ = q₁».
- **17 nov p. 2, foto 2-3: infinità dei primi** → **già presente** in cap53.33-53.39, con una **differenza tra lezione 2026 e capitolo**. Alla lavagna il teorema è dimostrato così: si prende un qualsiasi insieme finito S = {p₁, …, p_k} di primi, si fa vedere che N = p₁ ⋯ p_k + 1 ha un fattore primo p fuori da S, e l'assurdo serve solo per escludere p = pᵢ. Il capitolo invece suppone fin dall'inizio che S contenga tutti i primi. Le due dimostrazioni sono equivalenti, ma la versione della lavagna non ha bisogno di partire dall'assurdo «i primi sono finiti».
- **17 nov p. 2, foto 2: esempi S = {2, 3, 5} → N = 31 e S = {2, 5, 11} → N = 111 = 3·37** → il primo è **già presente** in cap53.40; il secondo **manca nel cap. 53** (blocco più vicino **cap53.41**). **Aggiunta consigliata**: è l'esempio della lavagna per «N non è sempre primo, ma i suoi fattori primi stanno fuori da S» (3 e 37 non sono in S). Il capitolo lo spiega con 30031 = 59·509, un esempio che non viene dalla lezione. 111 = 3·37 è verificato.

## Tutorato 1 (scheda dell'11 nov, esercizi 2-4 e 7-12)
Il tutorato **non è usato in nessun capitolo**: nel JSON non ci sono la parola «tutorato», gli esercizi della scheda o i suoi numeri. Gli argomenti sono quelli dei cap. 2-4 (insiemi), 6 (partizioni), 8 (relazioni), 13-17 (immagine, controimmagine, rendere biettiva una funzione), 18 (composizione), 22-24 (scelte successive, disposizioni).
- **Tutorato p. 1, es. 2c: «A ∩ B = ∅ ⟹ 𝒫(A) ∩ 𝒫(B) = ∅»** → **errore negli appunti**: l'intersezione contiene sempre ∅, quindi è {∅}, come nella soluzione della scheda. Il fatto da cui dipende è **già presente** in cap4.50 (∅ ∈ 𝒫(A) per ogni A), ma la conseguenza sull'intersezione no. Si può aggiungere come «Trabocchetto d'esame» dopo **cap4.50**. Prima bisogna controllare le evidenziazioni, perché il capitolo è studiato.
- **Tutorato p. 1, es. 2b** → negli appunti l'uguaglianza è scritta «(A ∪ B) ∩ C = (B ∪ C) ∩ A», mentre la scheda chiede (A ∪ B) ∩ C = A ∪ (B ∩ C), che è falsa. È solo la trascrizione del testo: non c'è una risposta da controllare.
- **Tutorato p. 1, es. 3: le 5 partizioni di {1, 2, 3}** → corrette. Nel cap. 6 non c'è l'elenco completo per un insieme di 3 elementi.
- **Tutorato p. 1, es. 4: A = B ⟹ A ∩ C = B ∩ C; A ∪ C = B ∪ C e A ∩ C = B ∩ C ⟹ A = B** → svolgimento corretto (A = (A − C) ∪ (A ∩ C)), con una seconda prova elemento per elemento lasciata a metà.
- **Tutorato p. 2, es. 7: f(n) = n² − 3n + 5, f⁻¹({5}) = {0, 3}, f⁻¹({0}) = ∅** → corretto.
- **Tutorato p. 2, es. 8.1-8.2** → corretti (inversa m ↦ m/3; restrizione [0, +∞) → [2, +∞) con inversa √(y − 2)).
- **Tutorato p. 2, es. 8.3: f(x, y) = (x², x² + y²)** → **errore negli appunti**: il codominio è scritto ℝ²_{≥0}, ma l'immagine è I = {(a, b) : a ≥ 0, b ≥ a}. Per esempio (1, 0) ∈ ℝ²_{≥0} non è immagine di nulla, e √(b − a) non ha senso se b < a. È proprio il punto del cap. 17 («rendere biettiva cambiando il codominio»).
- **Tutorato p. 2, es. 9: g(x) = 3x + 4** → corretto.
- **Tutorato p. 3, es. 10** → riflessiva sì, simmetrica no; la transitività è lasciata in bianco (non vale, perché (−1, 1), (1, 0) ∈ R ma (−1, 0) ∉ R).
- **Tutorato p. 3, es. 11** → l'elenco di R è corretto (2x + 3y ≡ 0 mod 5 ⟺ x ≡ y mod 5), e la transitività 2x + 3z = 5(k + h − y) è corretta.
- **Tutorato p. 3, es. 12** → **errori negli appunti**. Punto 1: «5·4·7 = 140» è sbagliato; la riga sotto, (5 su 2)(7 su 1)·3! = 420, è giusta (manca il fattore che conta i posti sullo scaffale). Punto 2: «4·11·10 = 440» è sbagliato; è 12·11·10 − 8·7·6 = 984 (conteggio per complementare). Punto 3: 9·8·7 = 504, giusto.
- **Proposta**: un capitolo nuovo **54. Esercizi svolti: Tutorato 1** (come gli esercizi svolti dei cap. 55-58 di Algebra), che riprenda la scheda e segnali i tre errori qui sopra come trabocchetti (𝒫(A) ∩ 𝒫(B) = {∅}, codominio = immagine, ordine sullo scaffale e conteggio per complementare). Le soluzioni della scheda sono giuste: le ho ricontrollate tutte.

## Riepilogo
- Errori negli appunti (nessuno è nel sito): σ ∘ π del 27 ott (calcolato con π⁻¹); «2 scambi» per il tipo (3, 5, 6) (sono 11); «n non divide d» invece di a (17 nov); tutorato 2c, 8.3, 12.1 e 12.2.
- Contrasti veri tra appunti e capitoli: nessuno. Dove gli appunti e il capitolo sono diversi, sbagliano gli appunti.
- Differenze tra la lezione 2026 e le fonti dei capitoli (appunti del docente e registrazioni di Emanuele): F(π) = (1 2) ∘ π al posto di π ∘ (1 2) (cap. 42); esistenza nel teorema fondamentale per induzione forte invece del minimo controesempio (cap. 53); infinità dei primi dimostrata su un insieme finito qualsiasi S, con l'esempio S = {2, 5, 11} (cap. 53).
- Aggiunte proposte, in ordine di utilità: cap. 53 esempio N = 111 = 3·37 (dopo cap53.41) e la formulazione con S qualsiasi; cap. 51 esempio 6x + 10y = 8 (dopo cap51.20); capitolo nuovo sul Tutorato 1; trabocchetto 𝒫(A) ∩ 𝒫(B) = {∅} nel cap. 4 (dopo cap4.50); righe di raccordo nei cap. 42 e 53; seconda dimostrazione breve nel cap. 47. Prima di inserire qualcosa nei capitoli già studiati (1-15) bisogna controllare le evidenziazioni (`inserisci_blocchi_sito.py`).
