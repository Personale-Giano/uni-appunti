# 36. Le Potenze di una Permutazione e il Periodo
## Una domanda: che cosa succede ripetendo la stessa permutazione
Il teorema di scomposizione serve a rispondere a domande come questa. Sia π ≠ id una permutazione. Si può applicare la composizione allo stesso oggetto: si parte dall'identità, poi si prende π, poi **π ∘ π**, che si indica con **π²**, poi π² ∘ π = π³, poi π⁴, π⁵ e così via (si ricorda l'immagine del mazzo di carte: si mescola, poi si rimescola nello stesso modo, e ancora).

(In parole povere: la potenza π^{k} è la permutazione che si ottiene applicando k volte di seguito la stessa permutazione.)

La domanda è se, andando avanti a calcolare potenze, si ottengano sempre permutazioni diverse, mai viste prima.

## Le potenze devono ripetersi
No. Il numero n è fissato, e le permutazioni di n elementi sono in tutto n!, un numero finito. Quindi la successione delle potenze non può dare sempre permutazioni nuove: a un certo punto deve capitare che una potenza sia uguale a una calcolata prima, cioè **π^{N} = π^{m} con m < N**.

Con i numeri non sarebbe così: le potenze di 2 (2, 4, 8, 16, …) sono tutte diverse. Con le permutazioni, che sono in numero finito, no.

## Esponenti negativi
Le permutazioni sono funzioni biettive e quindi hanno un'inversa. Si può prolungare la successione delle potenze anche verso sinistra, con esponenti negativi: per convenzione π⁰ = id, **π⁻¹** è l'inversa di π e π⁻² è l'inversa di π². Si osserva che **π⁻² = (π⁻¹)²**: infatti, componendo π² = π ∘ π con π⁻¹ ∘ π⁻¹ si cancellano a coppie π e π⁻¹ e si ottiene l'identità, che è l'elemento neutro, quindi π⁻¹ ∘ π⁻¹ è proprio l'inversa di π ∘ π. In generale **l'inversa di una potenza è la potenza con l'esponente cambiato di segno**, come con i numeri. Si può quindi estendere la successione con π⁻¹, π⁻², π⁻³, … e così via. (In parole povere: π⁻¹ è la permutazione che «disfa» π, e π⁻ᵏ è «disfare k volte».)

## Il periodo
Ora si parte dall'uguaglianza π^{N} = π^{m}, con N > m, e si compone ad entrambi i lati con l'inversa di π^{m}, cioè π⁻ᵐ:
π^{N} ∘ π⁻ᵐ = π^{m} ∘ π⁻ᵐ.
A destra si ottiene l'identità. A sinistra si ha π applicata N volte e poi π⁻¹ applicata m volte: si cancellano m coppie e resta **π^{N−m}**. Dunque
**π^{N−m} = id**, con 0 < N − m ≤ N.

Se N è il primo esponente per cui c'è una ripetizione, e fosse π^{N} = π^{m} con m ≥ 1, allora π^{N−m} = id = π⁰ sarebbe una ripetizione precedente: assurdo. Quindi m = 0: **la prima ripetizione che capita è proprio quella dell'identità**. La successione è fatta così: id, π, π², …, fino a un certo π^{p−1}, tutte diverse, e al passo successivo π^{p} = id. (Sono tutte diverse perché, se fosse π^{i} = π^{j} con 0 ≤ i < j < p, componendo con π^{−i} si avrebbe π^{j−i} = id con 0 < j − i < p, contro la minimalità di p.)

**Definizione.** Il più piccolo intero positivo p tale che π^{p} = id si chiama il **periodo** di π.

(In parole povere: il periodo è il numero di volte che bisogna ripetere la permutazione per tornare al punto di partenza, cioè all'identità.)

**Esempio.** Per lo scambio che scambia 1 e 2 (e lascia fermi gli altri elementi), π² = id: si scambia, poi si scambia di nuovo e si torna alla situazione iniziale. Quindi il suo periodo è 2.

## Perché si chiama «periodo»
Dopo π^{p} = id, la successione ricomincia: π^{p+1} = π^{p} ∘ π = π (si compone con l'identità, che non cambia niente), poi π^{p+2} = π², e così via fino a π^{2p} = π^{p} ∘ π^{p} = id. La successione delle potenze **è periodica**: ripete sempre lo stesso blocco di permutazioni, id, π, …, π^{p−1}. Anche verso sinistra: π^{−1} = π^{p−1} (perché π^{p−1} ∘ π = π^{p} = id), e la successione con esponenti negativi ripete lo stesso blocco. Il nome viene da questa idea di qualcosa che si ripete.

## Una domanda aperta
La lezione si chiude con una domanda lasciata per dopo: **come si calcola il periodo** di una permutazione? Probabilmente gli strumenti da usare sono il tipo e la scomposizione in cicli disgiunti, ma la risposta è rimandata alla lezione successiva.

Un'osservazione: per una permutazione che è un solo ciclo di lunghezza ℓ, il periodo è esattamente ℓ.
