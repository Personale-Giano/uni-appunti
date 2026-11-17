# 40. L'Invariante della Potenza
## Un secondo ciclo, lo stesso schema
La lezione 20 riprende gli invarianti di ciclo con un secondo esempio: il ciclo che calcola la potenza aⁿ con n moltiplicazioni. Il codice e la prova qui sotto sono quelli del quiz «Lezione 20: prove per induzione. Calcolo di a^n» su Moodle, proposto come prova da completare. Lo schema è identico a quello del fattoriale (cap. 39): si trova un invariante, lo si prova per induzione sul numero di esecuzioni del corpo, e alla fine lo si usa insieme alla condizione falsa del `while`. In fondo al capitolo lo stesso schema è applicato a un terzo ciclo, quello che calcola il quadrato di un numero, ripreso dagli appunti del docente.

## Il codice e l'invariante
Sia a una variabile che contiene un numero reale qualunque e n una variabile che contiene un intero n ≥ 0 (indicati con le stesse lettere).

```
i = 0
ris = 1
while (i < n) {
   i = i + 1
   ris = ris * a
}
```

L'idea è semplice: `ris` parte da 1 e viene moltiplicato per a una volta a ogni giro, mentre i conta i giri fatti. Dopo i giri, in `ris` c'è a moltiplicato per sé stesso i volte.

**L'invariante** è: **i ≤ n e ris = aⁱ**.

(In parole povere: in ogni momento `ris` contiene la potenza di a con esponente uguale al numero di moltiplicazioni già fatte, e il contatore non ha superato n. Con a = 3 e n = 4, dopo due giri i = 2 e ris = 9 = 3².)

Il quiz divide la prova in due esercizi, uno per ciascuna parte della congiunzione: conviene fare lo stesso, perché le due parti si provano con argomenti diversi.

## Prima parte: ris = aⁱ
Si procede per induzione sul numero di esecuzioni del corpo del `while`, scegliendo a ogni passo un valore i₀ per il contatore.

**Caso base.** Non si è mai eseguito il corpo: i valori sono i = 0 e ris = 1. Per la definizione di potenza a⁰ = 1, quindi con i₀ = 0 vale i = i₀ e ris = a^{i₀}.

**Caso induttivo.** Si suppone che dopo un certo numero di esecuzioni sia i = i₀ e ris = a^{i₀}, e che il corpo venga eseguito un'altra volta. Si eseguono nell'ordine i = i + 1 e ris = ris · a: si ottiene i = i₀ + 1 e ris = a^{i₀} · a. Per la definizione di potenza a^{i₀+1} = a^{i₀} · a, quindi, scegliendo come nuovo valore di i₀ il vecchio i₀ + 1, i nuovi valori soddisfano di nuovo i = i₀ e ris = a^{i₀}.

Qui, a differenza del fattoriale, l'ordine delle due istruzioni del corpo non conta: `ris = ris * a` non usa i.

**L'overflow.** Il quiz scrive «se questo calcolo non produce overflow». In matematica a^{i₀} · a è sempre a^{i₀+1}; in una variabile della macchina il prodotto può uscire dall'intervallo rappresentabile (cap. 8), e allora l'uguaglianza non vale più. La prova è corretta per i numeri, il programma lo è finché i valori ci stanno.

**Il caso a = 0.** Per a = 0 e n = 0 il ciclo restituisce 1. È coerente con la convenzione 0⁰ = 1, che è quella usata dalla definizione a⁰ = 1 nel caso base.

## Seconda parte: i ≤ n
**Caso base.** Prima del ciclo i = 0, e poiché per ipotesi n ≥ 0, vale i ≤ n.

**Caso induttivo.** Si suppone i ≤ n e che il corpo venga eseguito: allora il test i < n è vero. L'unica istruzione che tocca i è i = i + 1; da i < n, trattandosi di interi, segue i + 1 ≤ n, quindi per il nuovo valore di i vale ancora i ≤ n.

È lo stesso argomento del cap. 39: l'invariante da solo direbbe solo i ≤ n, che non basta; è il test del `while`, vero perché il corpo viene eseguito, a garantire che l'incremento non porti oltre n.

## Dalla prova alla correttezza
Quando il ciclo termina, il test i < n è falso, quindi i ≥ n. Con i ≤ n si ottiene i = n, e la prima parte dell'invariante diventa ris = aⁿ: il ciclo ha calcolato la potenza.

Per esempio, con a = 2 e n = 5, dopo 0, 1, 2, 3, 4, 5 esecuzioni del corpo le coppie (i, ris) sono (0, 1), (1, 2), (2, 4), (3, 8), (4, 16), (5, 32): a ogni passo ris = 2ⁱ. Alla fine il test 5 < 5 è falso e ris = 32 = 2⁵. Il ciclo termina sempre: i parte da 0, cresce di 1 a ogni giro e dopo n giri vale n. Nei termini del cap. 39, la funzione di terminazione è n − i: è un numero naturale per la parte i ≤ n dell'invariante e diminuisce di 1 a ogni giro.

**L'ipotesi n ≥ 0.** Serve al caso base della seconda parte. Con n negativo il ciclo non parte e restituisce 1, che non è aⁿ (per esempio 2^{−1} = 1/2): come nel cap. 39, senza l'ipotesi sui valori in ingresso l'invariante non vale e il risultato è sbagliato.

## La versione del libro
Tra gli esercizi della sezione 2.4 il libro propone lo stesso calcolo con il contatore che parte da 1 (Esercizio 45). Il codice qui sotto è ricostruito dalla soluzione che il libro ne dà, perché il testo dell'esercizio non è tra le pagine disponibili:

```
i = 1
pow = 1
while (i <= n) {
   pow = pow * a
   i = i + 1
}
```

Qui l'invariante è **i ≤ n + 1 e pow = a^{i−1}**, con n ≥ 0: il contatore è sempre «uno avanti» rispetto al numero di moltiplicazioni fatte. (Il libro scrive solo pow = a^{i−1}; la parte i ≤ n + 1 serve per concludere, come i ≤ n nel ciclo del quiz.) All'inizio i = 1 ≤ n + 1 perché n ≥ 0, e pow = 1 = a⁰ = a^{1−1}; se l'invariante vale e i ≤ n, il corpo dà pow = a^{i−1} · a = aⁱ e poi aumenta i di 1, quindi vale di nuovo pow = a^{i−1} e i ≤ n + 1. All'uscita il test i ≤ n è falso, cioè i > n, e con i ≤ n + 1 si ottiene i = n + 1: allora pow = aⁿ. Come per la variante del fattoriale nel cap. 39, cambiare il punto di partenza del contatore cambia la formula dell'invariante, non l'idea.

## Un terzo ciclo: il quadrato
Gli appunti del docente, dopo la divisione intera (cap. 39), usano la stessa tecnica su un ciclo che calcola il quadrato di un numero naturale N senza fare nemmeno una moltiplicazione tra variabili: solo somme e un raddoppio. Questa volta, dice il docente, l'invariante non serve a controllare un programma già scritto ma a **costruirlo**: prima si decide che cosa deve restare vero, poi si scrive il corpo in modo che lo conservi.

La condizione di ingresso è N ≥ 0. Si usano due variabili: X, un contatore che sale da 0 a N, e Y, che conterrà il risultato. La condizione di uscita è Y = X · X e X = N, cioè Y = N · N. L'invariante scelto è la prima metà della condizione di uscita:

**Y = X · X**

L'idea è far salire X di 1 alla volta tenendo sempre in Y il quadrato del valore corrente di X. Quando X passa a X + 1, il quadrato passa da X · X a (X + 1) · (X + 1) = X · X + 2 · X + 1: per rimettere a posto Y basta quindi aggiungergli 2 · X + 1. Da qui il codice:

```
X = 0
Y = 0
while (X < N) {
   Y = Y + 2 * X + 1
   X = X + 1
}
```

Come nei cicli precedenti conviene aggiungere all'invariante la parte **X ≤ N**: gli appunti la usano nella conclusione («sempre X ≤ N») senza metterla nella formula.

**Vale all'inizio.** Prima del ciclo X = 0 e Y = 0, quindi Y = 0 = 0 · 0 = X · X. Inoltre X = 0 ≤ N per la condizione di ingresso.

**Si conserva.** Si suppone Y = X · X e che il corpo venga eseguito un'altra volta. Indicando con Y' e X' i valori nuovi, Y' = Y + 2 · X + 1 = X · X + 2 · X + 1 [ipotesi induttiva] = (X + 1) · (X + 1) = X' · X', perché X' = X + 1. Per la seconda parte: se il corpo viene eseguito il test X < N è vero, quindi X' = X + 1 ≤ N.

Qui l'ordine delle due istruzioni conta: Y va aggiornato **prima** di X, perché la formula 2 · X + 1 usa il valore vecchio del contatore. Se si incrementasse prima X, l'aggiunta giusta sarebbe 2 · X − 1 con il valore nuovo (osservazione aggiunta: è la stessa attenzione al valore vecchio e nuovo vista per il fattoriale nel cap. 39).

**All'uscita dà la postcondizione.** Quando il ciclo si ferma il test X < N è falso, cioè X ≥ N; con X ≤ N si ottiene X = N, e l'invariante diventa Y = N · N.

**La terminazione.** Negli appunti la quantità che scende è N − X, che decresce strettamente a ogni iterazione: è la funzione di terminazione del cap. 39. È un numero naturale per la parte X ≤ N, diminuisce di 1 a ogni giro, e quindi dopo N giri il ciclo si ferma. Il programma è totalmente corretto.

Per esempio, con N = 4 le coppie (X, Y) sono (0, 0), (1, 1), (2, 4), (3, 9), (4, 16): a ogni passo Y = X · X, e N − X vale 4, 3, 2, 1, 0. Le quantità aggiunte a Y sono 1, 3, 5, 7: il ciclo calcola il quadrato di N sommando i primi N numeri dispari.

## La stessa induzione su una definizione ricorsiva
Un quiz di ripasso delle lezioni 19-22 propone la stessa idea senza ciclo. La funzione f è definita da due equazioni: f(x, 0) = 1 e f(x, n) = x · f(x, n − 1) per n > 0. Si dimostra per induzione su n ∈ ℕ che f(x, n) = xⁿ per ogni x.

- **Caso base.** f(x, 0) = 1 per la prima equazione, e 1 = x⁰ per le proprietà delle potenze.
- **Passo induttivo.** Per un qualsiasi n > 0 si assume l'ipotesi induttiva «per ogni x, f(x, n − 1) = x^{n−1}» e si prova «per ogni x, f(x, n) = xⁿ»: f(x, n) = x · f(x, n − 1) [seconda equazione] = x · x^{n−1} [ipotesi induttiva] = xⁿ [proprietà delle potenze].

Il passo induttivo ha la forma ∀n > 0 (P(n − 1) → P(n)) vista nel cap. 37. Il ciclo e la definizione ricorsiva fanno le stesse moltiplicazioni: l'invariante del ciclo e la prova sulla definizione sono due modi di scrivere lo stesso ragionamento.

Gli appunti del docente fanno lo stesso passaggio per il quadrato. La funzione q è definita dalle clausole q(0) = 0 e q(n + 1) = q(n) + 2 · n + 1, e si dimostra per induzione che q(n) = n · n per ogni n: nel caso base q(0) = 0 = 0 · 0; nel passo induttivo q(n + 1) = q(n) + 2 · n + 1 [definizione] = n · n + 2 · n + 1 [ipotesi induttiva] = (n + 1) · (n + 1) [proprietà algebriche]. È lo stesso conto del passo «si conserva» del ciclo del quadrato. Le clausole servono anche a calcolare: q(3) = q(2) + 5 = q(1) + 3 + 5 = q(0) + 1 + 3 + 5 = 9.

## Si può fare con meno moltiplicazioni?
Il ciclo fa esattamente n moltiplicazioni. Nella registrazione 2025 il docente anticipa che, quando i fattori sono tutti uguali, si può fare molto meglio riutilizzando i risultati già calcolati: per a⁸ basta calcolare a² = a · a, poi a⁴ = a² · a², poi a⁸ = a⁴ · a⁴, cioè 3 moltiplicazioni invece di 7. Un esempio aggiunto: a¹⁰ = a² · a⁸ ne richiede 4 invece di 9. È l'idea della **potenza veloce**, su cui si basa la crittografia a chiave pubblica, che calcola continuamente potenze con esponenti enormi. Nella registrazione 2025 il docente la presenta con il suo invariante nella lezione successiva. Il cap. 41 mostra invece che, con fattori diversi, nessun modo di mettere le parentesi fa risparmiare moltiplicazioni.
