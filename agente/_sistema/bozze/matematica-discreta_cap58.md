# 58. Le Classi Resto Invertibili e il Calcolo dell'Inverso con Bézout
## Classi invertibili e divisori dello zero
(Lezione del 19 nov ricostruita dal libro, cap. 7.)

Nel cap. 57 si è visto, guardando le tabelle, che in ℤ_{N} non tutte le classi hanno un inverso rispetto alla moltiplicazione: in ℤ_{6}, per esempio, nella riga del 2 non compare mai l'1. Tra i razionali o i reali l'unico numero senza inverso è lo 0; in ℤ_{N}, invece, oltre a [0] anche alcune classi non nulle restano senza inverso, come mostra pure la tabella di ℤ_{10}. Servono quindi due nomi.

**Definizione.** Una classe [a] ∈ ℤ_{N} si dice **invertibile** se esiste una classe [b] ∈ ℤ_{N} tale che [a] · [b] = [1]. In tal caso [b] si chiama l'**inversa** di [a] e si scrive [b] = [a]^{−1}.

(In parole povere: una classe è invertibile se c'è un'altra classe che, moltiplicata per lei, dà 1, proprio come 1/2 «disfa» la moltiplicazione per 2 tra i razionali. In ℤ_{5}, [2] è invertibile perché [2] · [3] = [6] = [1].)

**Definizione.** Una classe [a] ≠ [0] di ℤ_{N} si dice un **divisore dello zero** (o, più brevemente, uno 0-divisore) se esiste una classe [b] ≠ [0] tale che [a] · [b] = [0].

(In parole povere: un divisore dello zero è una classe non nulla che, moltiplicata per un'altra classe non nulla, dà zero: una cosa impossibile tra i numeri interi. In ℤ_{6}, [2] è un divisore dello zero perché [2] · [3] = [6] = [0].)

**Esempio.** Alcuni casi concreti:
- In ℤ_{10}, [4] è un divisore dello zero, perché [4] · [5] = [20] = [0]; per lo stesso motivo lo è anche [5].
- Può anche succedere che [a] e [b] siano la stessa classe: in ℤ_{9}, [3] è un divisore dello zero, perché [3] · [3] = [9] = [0].
- Nella tabella di ℤ_{10} le sole classi invertibili sono [1], [3], [7] e [9]: solo nelle loro righe compare 1. Gli inversi si leggono nella tabella: [3] · [7] = [21] = [1] e [9] · [9] = [81] = [1], quindi [3]^{−1} = [7], [7]^{−1} = [3], [9]^{−1} = [9], e naturalmente [1]^{−1} = [1].

Le due cose si escludono.

**Proposizione.** Un divisore dello zero non è invertibile.

(In parole povere: se una classe può «finire a zero» moltiplicata per qualcosa di non nullo, non c'è modo di disfare la moltiplicazione per lei.)

**Dimostrazione.** Per assurdo, sia [a] invertibile e sia [a] · [b] = [0] con [b] ≠ [0]. Moltiplicando a sinistra per [a]^{−1} e usando l'associativa del prodotto (cap. 57):
[b] = [1] · [b] = ([a]^{−1} · [a]) · [b] = [a]^{−1} · ([a] · [b]) = [a]^{−1} · [0] = [0],
contro l'ipotesi [b] ≠ [0]. ∎

## Il teorema: decide il massimo comun divisore
Il risultato centrale dice che non ci sono altre possibilità: ogni classe non nulla è invertibile oppure è un divisore dello zero, e quale dei due casi si presenta lo decide il massimo comun divisore (cap. 45) tra un rappresentante e il modulo.

**Teorema (classi invertibili).** Sia [a] ≠ [0] una classe non nulla di ℤ_{N}. Allora:
- se MCD(a, N) = 1, la classe [a] è invertibile;
- se MCD(a, N) > 1, la classe [a] è un divisore dello zero.

(In parole povere: per sapere se [a] ha un inverso modulo N basta guardare se a e N hanno fattori in comune. Se sono coprimi, l'inverso c'è; se hanno un fattore comune, [a] moltiplicata per qualcosa di non nullo dà zero.)

**Dimostrazione.** Si trattano i due casi.
1. Sia MCD(a, N) = 1. Per l'identità di Bézout (cap. 50) esistono due interi A e B tali che a · A + N · B = 1. Si legge questa uguaglianza in ℤ_{N}, prendendo le classi dei due membri e usando le operazioni del cap. 57:
[1] = [a · A + N · B] = [a] · [A] + [N] · [B] = [a] · [A] + [0] · [B] = [a] · [A],
perché [N] = [0]. Quindi [a] è invertibile e la sua inversa è [A].
2. Sia MCD(a, N) = d > 1. Siccome d divide a e N, si scrive a = d · s e N = d · t con s, t ∈ ℤ. Si ha 0 < t < N (perché d > 1), quindi [t] ≠ [0]. D'altra parte
[a] · [t] = [d · s · t] = [s · (d · t)] = [s · N] = [s] · [N] = [s] · [0] = [0].
Dunque [a] è un divisore dello zero. ∎

(Nel caso 2 si prendono implicitamente il rappresentante a e il modulo N positivi; è lecito, perché ogni classe ha un rappresentante tra 0 e N − 1, cap. 56.)

Messo insieme con la proposizione precedente, il teorema dice che le classi non nulle di ℤ_{N} si dividono esattamente in due gruppi che non si sovrappongono: le invertibili, con MCD(a, N) = 1, e i divisori dello zero, con MCD(a, N) > 1.

**Attenzione.** Il teorema è enunciato su un rappresentante a, ma deve essere una proprietà della classe: se si cambiasse rappresentante, il MCD con N potrebbe cambiare? No. Se [a'] = [a], allora a' = a + k · N per qualche k ∈ ℤ, e ogni divisore comune di a e N divide anche a' (proprietà della divisibilità del cap. 44 e 45); allo stesso modo, siccome a = a' − k · N, ogni divisore comune di a' e N divide a. Quindi MCD(a, N) = 1 se e solo se MCD(a', N) = 1. È, ancora una volta, un controllo di buona definizione come quelli del cap. 12 e del cap. 57.

## Gli invertibili di ℤ₄, ℤ₅, ℤ₆ e ℤ₃₅
Il teorema permette di elencare invertibili e divisori dello zero senza scrivere la tabella: basta calcolare MCD(a, N) per a = 1, …, N − 1. Gli elenchi seguenti (nostri, a parte ℤ_{35} che è l'esempio del libro) si possono confrontare con le tabelle del cap. 57.
- ℤ_{4}: invertibili [1] e [3], con [1]^{−1} = [1] e [3]^{−1} = [3] (infatti 3 · 3 = 9 ≡ 1); divisore dello zero [2], perché MCD(2, 4) = 2 e [2] · [2] = [0].
- ℤ_{5}: tutte le classi non nulle sono invertibili, perché 1, 2, 3, 4 sono coprimi con 5: [1]^{−1} = [1], [2]^{−1} = [3], [3]^{−1} = [2], [4]^{−1} = [4] (infatti 2 · 3 = 6 ≡ 1 e 4 · 4 = 16 ≡ 1). Non ci sono divisori dello zero.
- ℤ_{6}: invertibili [1] e [5], con [5]^{−1} = [5] (infatti 5 · 5 = 25 ≡ 1); divisori dello zero [2], [3] e [4], perché MCD(2, 6) = 2, MCD(3, 6) = 3, MCD(4, 6) = 2 (per esempio [2] · [3] = [0] e [4] · [3] = [0]).
- ℤ_{35}, esempio del libro (35 = 5 · 7): i divisori dello zero sono le classi dei multipli di 5 o di 7, cioè [5], [7], [10], [14], [15], [20], [21], [25], [28], [30]; tutte le altre 24 classi non nulle, da [1], [2], [3], [4], [6], [8], [9], [11] fino a [33], [34], sono invertibili.

Un'osservazione nostra sugli esempi: in ℤ_{5} ogni classe non nulla è invertibile perché 5 è primo, e un primo è coprimo con tutti i numeri da 1 a p − 1, che non può dividere. Lo stesso vale per ogni modulo primo: in ℤ_{p}, con p primo, tutte le classi non nulle sono invertibili, mentre se N non è primo, scrivendo N = d · t con 1 < d, t < N, la classe [d] è un divisore dello zero.

Ci sono poi tre fatti sulle classi invertibili: [1] è invertibile; l'inversa di una classe invertibile è invertibile (la sua inversa è la classe di partenza); il prodotto di due classi invertibili è invertibile. (Osservazione nostra: se [a] e [b] sono invertibili, [b]^{−1} · [a]^{−1} è l'inversa di [a] · [b].) Per questo le classi invertibili, con la moltiplicazione, formano un gruppo, detto **gruppo moltiplicativo** di ℤ_{N} e indica con ℤ_{N}^{×}. (Per esempio ℤ_{10}^{×} = {[1], [3], [7], [9]}.)

## Calcolare l'inverso con Bézout
La dimostrazione del teorema non dice soltanto che l'inverso esiste: dice anche come trovarlo. Se MCD(a, N) = 1, si scrive l'identità di Bézout a · A + N · B = 1 con l'algoritmo di Euclide, come nel cap. 49 e 50, e il coefficiente di a dà l'inverso: [a]^{−1} = [A]. Il coefficiente B di N non serve.

**Esempio.** (esempio nostro) Calcolare l'inverso di [11] in ℤ_{35}. Siccome MCD(11, 35) = 1, l'inverso esiste. L'algoritmo di Euclide dà:
- 35 = 3 · 11 + 2;
- 11 = 5 · 2 + 1.

Si risale sostituendo i resti, come nel cap. 50:
1 = 11 − 5 · 2 = 11 − 5 · (35 − 3 · 11) = 16 · 11 − 5 · 35.
Quindi A = 16 e [11]^{−1} = [16] in ℤ_{35}. Controllo: 11 · 16 = 176 = 5 · 35 + 1, quindi [11] · [16] = [176] = [1].

**Esempio.** Nel cap. 49 si è calcolato con l'algoritmo di Euclide MCD(654, 3575) = 1; il libro (p. 138) ne dà l'identità di Bézout 1219 · 654 − 223 · 3575 = 1. Leggendola modulo 3575, il termine con 3575 sparisce, e quindi [654]^{−1} = [1219] in ℤ_{3575}. (Controllo: 1219 · 654 = 797226 = 223 · 3575 + 1.)

Bézout funziona per qualunque modulo, ma quando N è piccolo è più rapido cercare l'1 nella riga di [a] della tabella del prodotto, come si è fatto sopra per ℤ_{10} e ℤ_{5}. Bézout diventa indispensabile quando N è grande e la tabella non si può scrivere.

**Attenzione.** Il coefficiente A trovato con Bézout può essere negativo o maggiore di N: non è un problema, perché [A] è una classe e si può sostituire A con il suo resto nella divisione per N. Per esempio (nostro), in ℤ_{7}, dall'identità 3 · (−2) + 7 · 1 = 1 si ricava [3]^{−1} = [−2] = [5], e infatti 3 · 5 = 15 = 2 · 7 + 1.

## Lo stesso risultato con le congruenze
Nel linguaggio delle congruenze del cap. 54 il teorema diventa: per ogni a ∈ ℤ esiste b ∈ ℤ con a · b ≡ 1 (mod N) se e solo se MCD(a, N) = 1. Il «se» è il caso 1 della dimostrazione. Per il «solo se» il caso 2 copre le classi [a] ≠ [0], perché un divisore dello zero non è invertibile; se invece [a] = [0], allora a · b ≡ 0 (mod N), e 0 ≢ 1 perché N ≥ 2. Più direttamente (osservazione nostra): se a · b ≡ 1 (mod N), allora a · b − 1 = k · N per qualche k, cioè a · b − N · k = 1, e ogni divisore comune di a e N divide 1.

**Esempio.** (esempio nostro) 3 · 5 = 15 ≡ 1 (mod 7), mentre non esiste nessun b con 4 · b ≡ 1 (mod 6), perché MCD(4, 6) = 2: 4 · b − 1 è sempre dispari, e quindi non è mai un multiplo di 6.

Con questo si chiude il quadro della lezione: la congruenza modulo N è una relazione di equivalenza (cap. 56), le sue classi formano ℤ_{N}, su cui somma e prodotto sono ben definiti (cap. 57), e le classi invertibili sono esattamente quelle coprime con il modulo, con l'inverso che si calcola con l'identità di Bézout. Proprio Bézout e l'algoritmo di Euclide, visti nel cap. 49 e 50, diventano così lo strumento pratico per fare le divisioni in ℤ_{N}.
