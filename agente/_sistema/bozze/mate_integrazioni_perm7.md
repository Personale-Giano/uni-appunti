@@ dopo cap54.11
Negli appunti del docente (pubblicati su Moodle come «Appunti Lezione 7») gli esempi di partenza sono tre: i **giorni della settimana**, che si contano modulo 7; le **ore del giorno**, che si contano modulo 24 (osservazione nostra: è l'orologio di 24 ore, mentre sopra si è usato quello di 12); e le potenze di una permutazione. Per le permutazioni il docente scrive il ragionamento in generale. Se σ ∈ S_{n} ha periodo per(σ) = k, cioè k è il minimo intero > 0 con σ^{k} = (1) (l'identità, che sopra si è scritta id), le potenze
σ^{0} = (1), σ^{1} = σ, σ^{2}, …, σ^{k−1}
sono quelle «nuove», e da lì in poi si ripetono: σ^{k} = (1), σ^{k+1} = σ^{k} ∘ σ = σ, σ^{k+2} = σ^{2}, e così via. La sua conclusione è che le potenze di σ si contano **modulo k**, cioè modulo il periodo: è la stessa cosa vista sopra con la permutazione π di periodo 8.

@@ dopo cap54.13
Negli appunti il docente scioglie il dubbio della registrazione: il modulo è un intero **N ≥ 2**, indicato con la lettera maiuscola (da qui in poi N al posto di n). La lettura «n maggiore di zero» data sopra va quindi corretta in N ≥ 2: il caso N = 1 resta escluso perché banale (vedi sotto). È la stessa scelta del libro, che si segue dal cap. 56.

@@ dopo cap54.17
Negli appunti la congruenza modulo N si legge «**a congruo a b modulo N**» e si scrive a ≡ b mod N (senza parentesi), oppure in forma più compatta a ≡_{N} b. La relazione così definita su ℤ si chiama **relazione di congruenza modulo N**. Per dire che due numeri non sono congruenti si usa il simbolo barrato ≢: per esempio 3 ≢ 4 mod 2 si legge «3 non congruo a 4 modulo 2».

@@ dopo cap54.29
**Esempio.** Gli esempi degli appunti del docente:
- 8 ≡ 1 mod 7, infatti 7 | 8 − 1 = 7;
- 1 ≡ −1 mod 2, infatti 2 | 1 − (−1) = 2;
- 5 ≡ −7 mod 2, 3, 4, 6 e 12, perché 5 − (−7) = 5 + 7 = 12, e i moduli N ≥ 2 che dividono 12 sono esattamente 2, 3, 4, 6 e 12;
- 5 ≡ −19 mod 12, perché 5 + 19 = 24 = 2 · 12;
- 3 ≢ 4 mod 2, perché 3 − 4 = −1 non è divisibile per 2.
L'esempio con 5 e −7 mostra che la stessa coppia di numeri può essere congruente rispetto a più moduli: sono proprio i divisori (maggiori di 1) della differenza.

@@ dopo cap56.4
Il docente, negli appunti della lezione, tratta gli stessi argomenti di questo capitolo, ma in un ordine diverso dal libro: prima dimostra direttamente che la congruenza è una relazione di equivalenza, poi definisce la classe di un intero qualsiasi come classe di equivalenza, e solo alla fine collega le classi con i resti. Le sue definizioni, i suoi esempi e la sua dimostrazione sono aggiunti nei punti giusti del capitolo, indicati come contributi del docente.

@@ dopo cap56.26
## La classe di un intero qualsiasi
Il docente parte dalla congruenza invece che dai resti. Siccome la congruenza modulo N è una relazione di equivalenza (lo si dimostra più avanti in questo capitolo), ogni intero ha la sua classe di equivalenza, nel senso del cap. 9.

**Definizione.** Fissato il modulo N ≥ 2, per ogni a ∈ ℤ la **classe di resto di a modulo N** (la classe resto del libro) è la sua classe di equivalenza rispetto alla congruenza:
[a]_{N} = {b ∈ ℤ | a ≡ b mod N}.
Si scrive anche [a] oppure ā, quando il modulo è chiaro.

(In parole povere: la classe di a raccoglie tutti i numeri che «cadono nello stesso punto» di a su un quadrante con N posizioni. Con N = 7 e i giorni della settimana, la classe di un lunedì contiene tutti i lunedì, passati e futuri.)

Qui a può essere un intero qualsiasi, anche negativo o più grande di N, mentre nella definizione del libro data sopra il pedice è un resto r tra 0 e N − 1. Le due definizioni danno le stesse classi: lo dice la proposizione qui sotto.

Il docente osserva subito che a ≡ b mod N vuol dire N | b − a, cioè b = a + kN per qualche k ∈ ℤ. Quindi
[a]_{N} = {a + kN | k ∈ ℤ} = {…, a − 2N, a − N, a, a + N, a + 2N, …}:
la classe di a si ottiene partendo da a e aggiungendo o togliendo N quante volte si vuole.

**Esempio.** Gli esempi degli appunti, con N = 5:
- [0]_{5} = {5k | k ∈ ℤ} = {…, −20, −15, −10, −5, 0, 5, 10, 15, …}, e questa classe si può chiamare anche [−5]_{5} o [20]_{5};
- [1]_{5} = {…, −19, −14, −9, −4, 1, 6, 11, …}, dove per esempio −19 = 1 − 20, −14 = 1 − 15, −9 = 1 − 10;
- [2]_{5} = {…, −18, −13, −8, −3, 2, 7, 12, …};
- [3]_{5} = {…, −17, −12, −7, −2, 3, 8, 13, …};
- [4]_{5} = {…, −16, −11, −6, −1, 4, 9, 14, …}.
Andando avanti non si trova niente di nuovo: [5]_{5} = [0]_{5}, [6]_{5} = [1]_{5}, e così via. Ci sono esattamente 5 classi di resto modulo 5.

**Proposizione.** Fissato il modulo N, per ogni a ∈ ℤ si ha [a]_{N} = [r]_{N}, dove r è il resto della divisione di a per N.

(In parole povere: per sapere in quale classe sta un numero basta dividerlo per N e guardare il resto.)

**Dimostrazione.** (dagli appunti del docente)
1. Per la divisione euclidea (cap. 46), a = N · q + r con 0 ≤ r < N.
2. Quindi a − r = N · q, cioè N | a − r.
3. Questo vuol dire a ≡ r mod N, e due interi congruenti hanno la stessa classe: [a]_{N} = [r]_{N}. ∎

**Corollario.** Ci sono esattamente N classi resto modulo N: [0]_{N}, [1]_{N}, …, [N − 1]_{N}.

Ogni classe è una di queste, per la proposizione; e sono tutte diverse, perché due resti distinti r, s tra 0 e N − 1 hanno differenza compresa tra −(N − 1) e N − 1 e diversa da 0, quindi non divisibile per N (osservazione nostra). Per questo il docente scrive |ℤ_{N}| = N.

@@ dopo cap56.33
Negli appunti il docente ricorda il fatto generale del cap. 9: data una relazione di equivalenza su un insieme X, le classi di equivalenza formano una **partizione** di X, cioè sono non vuote, a due a due disgiunte, e la loro unione è tutto X. Per le classi resto la partizione si scrive con il simbolo ⊔ di **unione disgiunta** (un'unione di insiemi che non hanno elementi in comune):
ℤ = [0]_{N} ⊔ [1]_{N} ⊔ … ⊔ [N − 1]_{N}.

@@ dopo cap56.45
Il docente, negli appunti della lezione, dimostra il fatto (che chiama semplicemente «Fatto») proprio con questa verifica diretta, prima di parlare di classi e di partizioni: quindi la verifica diretta riportata sopra è anche quella del docente. Per la transitiva scrive a − c = (a − b) + (b − c): i due addendi sono multipli di N, quindi lo è anche la somma.

@@ dopo cap56.62
Anche il docente, negli appunti, usa tutte e tre le scritture [a]_{N}, [a] e ā, e per le operazioni del cap. 57 preferisce la barra.

@@ dopo cap56.63
**Definizione.** Ogni elemento di una classe resto si dice **rappresentante** della classe. Il rappresentante a con 0 ≤ a < N si dice **rappresentante canonico** della classe.

(In parole povere: una classe si può chiamare con il nome di uno qualunque dei suoi numeri, ma tra tutti ce n'è uno «ufficiale», il più piccolo non negativo, cioè il resto della divisione per N.)

**Esempio.** Dagli appunti del docente: −19, −4, 1 e 6 sono rappresentanti di [1]_{5}, e il canonico è 1. La classe [10]_{5} ha rappresentante canonico 0, perché 10 = 5 · 2 + 0. La classe [−7]_{5} ha rappresentante canonico 3, perché −7 = 5 · (−2) + 3. (Osservazione nostra) Attenzione al segno: il resto della divisione euclidea non è mai negativo. −7 ≡ 3 (mod 5), e −2 è un altro rappresentante della stessa classe, ma non è il canonico; 2 non appartiene a [−7]_{5}.

@@ dopo cap57.2
Il docente, negli appunti della lezione, tratta le operazioni come in questo capitolo, ma con la notazione ā al posto di [a]_{N}: la sua definizione dell'addizione è ā + b̄ = [a + b]_{N} (nel manoscritto una sola barra lunga sopra a + b), e quella della moltiplicazione è ā b̄ = [ab]_{N} (barra lunga sopra ab). I suoi esempi e le sue dimostrazioni sono aggiunti qui sotto.

@@ dopo cap57.19
Negli appunti il docente fa il conto dell'addizione con la divisibilità invece che con k e k': da N | a − a' e N | b − b' segue che N divide anche la somma (a − a') + (b − b') = (a + b) − (a' + b'), quindi a + b ≡ a' + b' mod N, cioè le due somme hanno la stessa classe.

@@ dopo cap57.20
Per la moltiplicazione il conto degli appunti è quello appena fatto, con a' = a + kN e b' = b + hN e il termine finale scritto come N · c con c = ah + bk + hkN ∈ ℤ.

@@ dopo cap57.21
**Esempio.** Gli esempi degli appunti del docente:
- [2]_{2} + [9]_{2} = [11]_{2} = [1]_{2}; con i rappresentanti canonici la stessa somma è [0]_{2} + [1]_{2} = [1]_{2};
- [−5]_{7} + [6]_{7} = [−5 + 6]_{7} = [1]_{7}; siccome [−5]_{7} = [2]_{7}, si può anche fare [2]_{7} + [6]_{7} = [2 + 6]_{7} = [8]_{7}, e infatti [8]_{7} = [1]_{7}: rappresentanti diversi, stessa classe;
- [3]_{8} + [7]_{8} = [10]_{8} = [2]_{8}, dove 2 è il rappresentante canonico;
- [3]_{5} · [7]_{5} = [3 · 7]_{5} = [21]_{5} = [1]_{5}.

@@ dopo cap57.24
**Esempio.** Un esercizio degli appunti: calcolare modulo 7 l'espressione ((3̄ + 5̄)(2̄ − 6̄)) · 3̄. Conviene ridursi al rappresentante canonico a ogni passo: 3̄ + 5̄ = 8̄ = 1̄; 2̄ − 6̄ è la classe di −4, cioè 3̄ (la sottrazione vuol dire sommare l'opposto, −6̄ = classe di −6, come nella proposizione più avanti) (spiegazione nostra). Quindi
((3̄ + 5̄)(2̄ − 6̄)) · 3̄ = (1̄ · 3̄) · 3̄ = 3̄ · 3̄ = 9̄ = 2̄.
Controllo con gli interi: (3 + 5) · (2 − 6) · 3 = 8 · (−4) · 3 = −96 = 7 · (−14) + 2, e il resto è proprio 2.

@@ dopo cap57.34
Negli appunti il docente dimostra come esempio proprio l'associativa della somma, con gli stessi passaggi, scritti nel verso opposto: a ogni uguaglianza indica se si usa la definizione di somma di classi di resto oppure la proprietà associativa in ℤ. Per l'opposto scrive −ā = [−a]_{N}, perché ā + [−a]_{N} = [a + (−a)]_{N} = 0̄.

@@ dopo cap58.2
Gli appunti del docente arrivano solo all'inizio di questo capitolo, fino all'osservazione sulle classi invertibili riportata qui sotto, dopo la definizione di classe invertibile. Gli appunti si fermano qui: divisori dello zero, teorema con il MCD e calcolo dell'inverso con Bézout restano ricostruiti dal libro.

@@ dopo cap58.5
L'osservazione degli appunti del docente parte dagli interi. In ℤ i soli numeri invertibili rispetto alla moltiplicazione sono 1 e −1: per ogni altro intero a ≠ 0 il reciproco 1/a non è intero, e 0 non ha reciproco. In ℤ_{N} le classi 1̄ e [−1]_{N} = [N − 1]_{N} (per N ≥ 3 sono diverse) sono certamente invertibili, perché 1 · 1 = 1 e (−1) · (−1) = 1, quindi ciascuna è l'inversa di sé stessa (giustificazione nostra). Ma, a differenza di ℤ, possono non essere le sole: l'esempio del docente è proprio quello di ℤ_{5} appena visto, dove [2]_{5} = [3]_{5}^{−1} e [3]_{5} = [2]_{5}^{−1}.
