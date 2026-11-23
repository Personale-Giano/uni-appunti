# 56. La Congruenza come Relazione di Equivalenza e l'Insieme delle Classi Resto
## Dalla congruenza alle classi
(Lezione del 19 nov ricostruita dal libro, cap. 7.)

Nel cap. 54 si è data la definizione di **congruenza modulo n**: a ≡ b (mod n) se n divide a − b. Da qui in poi il modulo si indica con la lettera maiuscola N, e si prende N ≥ 2: con N = 1, come già visto nel cap. 54, tutti i numeri sono congruenti tra loro e non c'è niente di interessante. (È coerente con il «n maggiore di zero» del cap. 54: N = 1 è solo il caso banale.)

Il programma di questo capitolo è mettere insieme la congruenza con la teoria delle relazioni di equivalenza e delle partizioni dei cap. 7, 8 e 9: si vedrà che i numeri interi, modulo N, si dividono in N «squadre», e che l'insieme di queste squadre è un insieme nuovo, ℤ_{N}, su cui nei prossimi capitoli si faranno i conti.

## Le classi resto
Si parte dalla divisione euclidea (cap. 46): dividendo un intero n per N si ottiene un resto r, che è uno dei numeri 0, 1, …, N − 1. Si raggruppano allora gli interi a seconda del resto.

**Definizione.** Sia N ≥ 2 il modulo. Per ogni r ∈ {0, 1, …, N − 1} si chiama **classe resto** di r modulo N l'insieme
[r]_{N} = {n ∈ ℤ tali che la divisione di n per N ha resto r} ⊆ ℤ.

(In parole povere: si mettono nello stesso cassetto tutti i numeri che, divisi per N, danno lo stesso resto. Con N = 12 sono le ore dell'orologio: nel cassetto del 4 finiscono 4, 16, 28, … ma anche −8, perché sono tutte «le 4».)

**Esempio.** È l'esempio del libro: con N = 7 e r = 3,
[3]_{7} = {…, −18, −11, −4, 3, 10, 17, 24, …}.
Si passa da un elemento al successivo aggiungendo 7. Per i negativi bisogna ricordare che nella divisione euclidea il resto è sempre tra 0 e N − 1: per esempio −4 = (−1) · 7 + 3, quindi il resto di −4 diviso 7 è 3, e −4 ∈ [3]_{7}.

Due casi particolari:
- [0]_{N} = {…, −2N, −N, 0, N, 2N, …} è l'insieme dei multipli di N, che si indica anche con Nℤ;
- per N = 2 le classi resto sono due: [0]_{2} è l'insieme dei numeri pari e [1]_{2} quello dei dispari. Le classi resto generalizzano quindi la divisione degli interi in pari e dispari, che è l'esempio di partizione del cap. 6 e 7.

## Stessa classe vuol dire congruenti
Il collegamento con il cap. 54 è il fatto seguente.

**Proposizione.** Due interi x, y stanno nella stessa classe resto modulo N se e solo se N | x − y, cioè se e solo se x ≡ y (mod N).

(In parole povere: «dare lo stesso resto diviso N» e «differire per un multiplo di N» sono la stessa cosa detta in due modi.)

**Dimostrazione.** Si dimostrano i due versi.
1. (⟹) Se x e y stanno entrambi in [r]_{N}, la divisione euclidea dà x = q · N + r e y = q' · N + r, con lo stesso resto r. Sottraendo, x − y = (q · N + r) − (q' · N + r) = (q − q') · N, che è un multiplo di N.
2. (⟸) Se N | x − y, si scrive x − y = k · N con k ∈ ℤ, cioè x = k · N + y. Sia y = q · N + r la divisione euclidea di y per N. Sostituendo, x = k · N + q · N + r = (k + q) · N + r, con 0 ≤ r < N. Per l'unicità di quoziente e resto (cap. 46), r è anche il resto della divisione di x per N: quindi x e y stanno nella stessa classe [r]_{N}. ∎

**Esempio.** (esempio nostro) Modulo 4: 17 = 4 · 4 + 1 e −3 = (−1) · 4 + 1 hanno lo stesso resto 1, e infatti 17 − (−3) = 20 = 5 · 4. Invece 17 e 7 hanno resti 1 e 3, e 17 − 7 = 10 non è multiplo di 4.

La conseguenza pratica è che
a ≡ b (mod N) se e solo se [a]_{N} = [b]_{N}.
Per questo tutta la teoria che si costruisce sulle classi resto si può riscrivere parola per parola nel linguaggio delle congruenze, e viceversa.

## Le classi resto formano una partizione di ℤ
**Proposizione.** Fissato N ≥ 2, le classi resto [r]_{N}, per r = 0, 1, …, N − 1, formano una partizione di ℤ.

(In parole povere: ogni intero finisce in uno e un solo cassetto, e nessun cassetto resta vuoto.)

**Dimostrazione.** Bisogna controllare le tre condizioni della definizione di partizione (cap. 6).
1. Nessuna classe è vuota: r stesso sta in [r]_{N}, perché r = 0 · N + r con 0 ≤ r < N.
2. Le classi ricoprono ℤ: dato n ∈ ℤ, sia r il resto della divisione di n per N; allora n ∈ [r]_{N}.
3. Classi distinte sono disgiunte: se un intero n stesse in [r]_{N} e in [s]_{N} con r ≠ s, la divisione di n per N avrebbe due resti diversi, contro l'unicità di quoziente e resto della divisione euclidea (cap. 46). Quindi [r]_{N} ∩ [s]_{N} = ∅. ∎

## La congruenza è una relazione di equivalenza
Il primo argomento del sommario si ottiene ora quasi gratis. Nel cap. 9 si è visto che una partizione e una relazione di equivalenza sono due facce della stessa cosa: data una partizione di S, la relazione «x e y stanno nello stesso blocco» è una relazione di equivalenza, e le sue classi di equivalenza sono proprio i blocchi. Per la proposizione «stessa classe vuol dire congruenti», la relazione «x e y stanno nella stessa classe resto» è esattamente la congruenza modulo N.

**Proposizione.** Fissato N ≥ 2, la congruenza modulo N è una relazione di equivalenza su ℤ: per ogni a, b, c ∈ ℤ,
- (riflessiva) a ≡ a (mod N);
- (simmetrica) se a ≡ b (mod N), allora b ≡ a (mod N);
- (transitiva) se a ≡ b (mod N) e b ≡ c (mod N), allora a ≡ c (mod N).

(In parole povere: ogni numero è congruente a se stesso, la congruenza vale nei due sensi, e si può concatenare. Sull'orologio: se due ore segnano lo stesso punto del quadrante, e la seconda segna lo stesso punto di una terza, anche la prima e la terza coincidono.)

Nel libro (proposizione 7.21) simmetrica e transitiva sono dette «ovvie»: traducono il fatto che le classi resto formano una partizione. Per abituarsi al ragionamento con la divisibilità conviene però verificarle anche direttamente dalla definizione (verifica nostra), usando le proprietà della divisibilità del cap. 44 e 45.

**Dimostrazione.** (verifica diretta, nostra)
1. Riflessiva: a − a = 0 = 0 · N, quindi N | a − a.
2. Simmetrica: se N | a − b, cioè a − b = k · N, allora b − a = (−k) · N, quindi N | b − a.
3. Transitiva: se a − b = k · N e b − c = h · N, sommando si ottiene a − c = (a − b) + (b − c) = (k + h) · N, quindi N | a − c. ∎

**Esempio.** (esempio nostro) Modulo 4: 17 ≡ 5, perché 17 − 5 = 12 = 3 · 4, e 5 ≡ −3, perché 5 − (−3) = 8 = 2 · 4. Per la transitiva allora 17 ≡ −3 (mod 4), e infatti 17 − (−3) = 20 = 5 · 4.

**Attenzione.** La divisibilità non è simmetrica (cap. 8), la congruenza sì: qui il divisore N resta fisso, e scambiando a e b la differenza cambia solo di segno.

## L'insieme quoziente delle classi resto
Essendo la congruenza una relazione di equivalenza, le sue classi di equivalenza sono le classi resto, e si può formare l'insieme quoziente (cap. 9).

**Definizione.** L'insieme quoziente di ℤ rispetto alla congruenza modulo N, cioè l'insieme delle classi resto modulo N, si indica con ℤ_{N}:
ℤ_{N} = {[0]_{N}, [1]_{N}, …, [N − 1]_{N}}.

(In parole povere: ℤ_{N} è l'insieme dei cassetti, non dei numeri. Ha esattamente N elementi, uno per ogni resto possibile; ciascun elemento è però un insieme infinito di interi.)

**Esempio.** I primi casi:
- ℤ_{2} = {[0]_{2}, [1]_{2}}, cioè {pari, dispari};
- ℤ_{3} = {[0]_{3}, [1]_{3}, [2]_{3}};
- ℤ_{4} = {[0]_{4}, [1]_{4}, [2]_{4}, [3]_{4}}, e così via.

Come in ogni insieme quoziente, ℤ_{N} è un sottoinsieme di 𝒫(ℤ): i suoi elementi sono sottoinsiemi di ℤ (cap. 7 e 9).

## Rappresentanti e notazione
Come per qualunque classe di equivalenza (cap. 9), una classe resto si può nominare con uno qualsiasi dei suoi elementi, che ne è un **rappresentante**: non serve usare per forza il resto r tra 0 e N − 1. Per esempio
… = [−3]_{11} = [8]_{11} = [19]_{11} = … = [107]_{11} = …,
perché −3, 8, 19 e 107 divisi per 11 danno tutti resto 8 (107 = 9 · 11 + 8, −3 = (−1) · 11 + 8). In generale, per la proposizione «stessa classe vuol dire congruenti», [a]_{N} = [b]_{N} esattamente quando a ≡ b (mod N).

Quando il modulo è chiaro dal contesto il pedice si omette e si scrive [a], oppure, come fa il libro, ā (la classe di a con una barra sopra, la stessa notazione x̄ dei cap. 9 e 12). Nel seguito dei riassunti si usa [a]_{N} o [a].

**Attenzione.** Va tenuta distinta la differenza tra un numero e la sua classe. Il numero 8 è un intero; [8]_{11} è un insieme infinito di interi, ed è lo stesso insieme di [−3]_{11}. Scrivere 8 = −3 sarebbe falso, mentre [8]_{11} = [−3]_{11} è vero, e si può dire anche con la congruenza: 8 ≡ −3 (mod 11).

Si sono così costruiti dei nuovi oggetti, le classi resto, e un insieme nuovo, ℤ_{N}, con N elementi. Per farne un'aritmetica bisogna saper sommare e moltiplicare le classi: è l'argomento del prossimo capitolo, dove si incontrerà di nuovo il problema, già visto nel cap. 12, delle definizioni che dipendono dal rappresentante.
