# 57. Somma e Prodotto tra Classi Resto: Operazioni Ben Definite
## Sommare delle classi
(Lezione del 19 nov ricostruita dal libro, cap. 7.)

Nel cap. 56 si è costruito l'insieme ℤ_{N} delle classi resto modulo N. Per farne un'aritmetica, come quella dell'orologio del cap. 54, servono due operazioni
+ : ℤ_{N} × ℤ_{N} → ℤ_{N} e · : ℤ_{N} × ℤ_{N} → ℤ_{N}.
Per non moltiplicare i simboli, i nomi restano quelli di sempre, somma (o addizione) e prodotto (o moltiplicazione), e anche i segni + e ·. La strada più naturale è passare dai rappresentanti e usare le operazioni di ℤ.

**Definizione.** In ℤ_{N} si definiscono:
- l'**addizione** [a] + [b] = [a + b];
- la **moltiplicazione** [a] · [b] = [a · b],
per ogni [a], [b] ∈ ℤ_{N}.

(In parole povere: per sommare due cassetti si pesca un numero da ciascuno, si fa la somma normale e si guarda in quale cassetto cade il risultato; lo stesso per il prodotto. Sull'orologio: le 9 più 7 ore fanno le 16, che sono «le 4».)

Conviene fare attenzione al fatto che nella stessa uguaglianza il segno + compare con due ruoli. In [a] + [b] si sommano due classi: è l'operazione che si sta introducendo. In [a + b] si sommano due interi, e la classe si prende solo dopo, sul risultato. Lo stesso vale per il segno ·.

**Esempio.** (esempio nostro) In ℤ_{6}: [4] + [5] = [9] = [3], perché 9 = 1 · 6 + 3; [4] · [5] = [20] = [2], perché 20 = 3 · 6 + 2.

## Il problema della buona definizione
La definizione nasconde un problema, lo stesso già incontrato nel cap. 12 con le funzioni sull'insieme quoziente. Per calcolare [a] + [b] si è scelto un rappresentante a della prima classe e un rappresentante b della seconda; ma ogni classe ha infiniti rappresentanti (cap. 56). Se scegliendo rappresentanti diversi si ottenesse una classe diversa, la «definizione» non darebbe un unico risultato, e quindi non definirebbe un'operazione. Finché non si è fatto questo controllo, quella di sopra è solo una proposta di definizione.

**Proposizione.** L'addizione e la moltiplicazione in ℤ_{N} sono ben definite: il risultato non dipende dai rappresentanti scelti, ma solo dalle classi.

(In parole povere: comunque si peschino i numeri dai due cassetti, la somma, e anche il prodotto, finisce sempre nello stesso cassetto. Sull'orologio, dire «le 4» o «le 16» non cambia l'ora che si ottiene aggiungendo 7 ore.)

**Dimostrazione.** Siano a' e b' altri rappresentanti delle stesse classi: [a'] = [a] e [b'] = [b]. Per il cap. 56 questo vuol dire N | a' − a e N | b' − b, cioè esistono k, k' ∈ ℤ con
a' = a + k · N e b' = b + k' · N.
1. Addizione: a' + b' = (a + k · N) + (b + k' · N) = (a + b) + (k + k') · N. La differenza tra a' + b' e a + b è (k + k') · N, un multiplo di N; quindi [a' + b'] = [a + b], cioè [a'] + [b'] = [a] + [b].
2. Moltiplicazione: a' · b' = (a + k · N) · (b + k' · N) = a · b + a · k' · N + b · k · N + k · k' · N^{2} = a · b + (b · k + a · k' + k · k' · N) · N. Anche qui la differenza tra a' · b' e a · b è un multiplo di N; quindi [a' · b'] = [a · b], cioè [a'] · [b'] = [a] · [b]. ∎

**Esempio.** (esempio nostro) In ℤ_{6} si ha [2] = [8] e [5] = [11]. Con i primi rappresentanti: 2 + 5 = 7 e 2 · 5 = 10. Con i secondi: 8 + 11 = 19 e 8 · 11 = 88. Le classi coincidono: 19 − 7 = 12 = 2 · 6, quindi [19] = [7] = [1]; 88 − 10 = 78 = 13 · 6, quindi [88] = [10] = [4].

Nel linguaggio delle congruenze la stessa proposizione dice: se a ≡ b (mod N) e c ≡ d (mod N), allora
a + c ≡ b + d (mod N) e a · c ≡ b · d (mod N).
È la regola che permette di fare i conti con le congruenze sostituendo un numero con un altro a esso congruente, per esempio con il suo resto, prima di sommare o moltiplicare. (Esempio nostro: per calcolare 17 · 9 modulo 12 si sostituisce 17 con 5 e 9 resta 9, oppure, ancora più comodo, si usa 9 ≡ −3: 17 · 9 ≡ 5 · (−3) = −15 ≡ 9 (mod 12). Infatti 17 · 9 = 153 = 12 · 12 + 9.)

**Attenzione.** Il controllo non è una formalità: nel cap. 12 si è visto un esempio di regola sulle classi che non definisce una funzione. Qui tutto funziona perché la congruenza è compatibile con somma e prodotto: è la dimostrazione appena fatta a garantirlo, non l'aspetto «naturale» della definizione.

## Le proprietà delle operazioni
Una volta controllato che le operazioni sono ben definite, se ne studiano le proprietà. Il metodo è sempre lo stesso: si scrivono le classi con i rappresentanti, si usa la proprietà corrispondente di ℤ (cap. 43) e si torna alle classi.

**Proposizione.** L'addizione in ℤ_{N} è associativa e commutativa, ha elemento neutro [0], e ogni classe [a] ha come opposto −[a] = [−a].

(In parole povere: la somma tra cassetti si comporta come la somma tra numeri interi: l'ordine non conta, il cassetto dello 0 non cambia niente, e per ogni cassetto ce n'è uno che sommato dà 0.)

**Dimostrazione.** Per ogni [a], [b], [c] ∈ ℤ_{N}:
1. associativa: ([a] + [b]) + [c] = [a + b] + [c] = [(a + b) + c] = [a + (b + c)] = [a] + [b + c] = [a] + ([b] + [c]), perché l'associativa vale in ℤ;
2. neutro: [0] + [a] = [0 + a] = [a], e allo stesso modo [a] + [0] = [a];
3. opposto: [a] + [−a] = [a − a] = [0];
4. commutativa: [a] + [b] = [a + b] = [b + a] = [b] + [a], perché la commutativa vale in ℤ. ∎

**Esempio.** (esempio nostro) In ℤ_{6} l'opposto di [2] è [−2] = [4], perché [2] + [4] = [6] = [0]. Sull'orologio: l'opposto delle 2 sono le 10, perché 2 + 10 = 12.

**Proposizione.** La moltiplicazione in ℤ_{N} è associativa e commutativa e ha elemento neutro [1]. Vale inoltre la proprietà distributiva: [a] · ([b] + [c]) = [a] · [b] + [a] · [c].

(In parole povere: anche il prodotto tra cassetti segue le regole solite, compresa la regola che «moltiplicare una somma» si fa moltiplicando ogni addendo.)

**Dimostrazione.** Come per l'addizione, si usano le proprietà del prodotto in ℤ:
1. associativa: ([a] · [b]) · [c] = [(a · b) · c] = [a · (b · c)] = [a] · ([b] · [c]);
2. neutro: [1] · [a] = [1 · a] = [a];
3. commutativa: [a] · [b] = [a · b] = [b · a] = [b] · [a];
4. distributiva: [a] · ([b] + [c]) = [a] · [b + c] = [a · (b + c)] = [a · b + a · c] = [a · b] + [a · c] = [a] · [b] + [a] · [c]. ∎

Nel linguaggio dei gruppi, usato nel libro, la prima proposizione dice che (ℤ_{N}, +) è un gruppo commutativo (abeliano). Inoltre ogni classe si ottiene sommando [1] con se stesso: [r] = [1] + [1] + … + [1], con r addendi.

## Le tabelle di ℤ₄, ℤ₅ e ℤ₆
Per un modulo piccolo le due operazioni si possono scrivere per intero in una tabella, come quella del libro per il prodotto in ℤ_{10}. Per leggerle meglio si scrive solo il rappresentante tra 0 e N − 1, senza parentesi: all'incrocio della riga a e della colonna b c'è a + b, oppure a · b. Le tabelle seguenti (nostre) sono di ℤ_{4}, ℤ_{5} e ℤ_{6}.

```
ℤ₄    +  | 0 1 2 3        ·  | 0 1 2 3
     ----+--------       ----+--------
      0  | 0 1 2 3        0  | 0 0 0 0
      1  | 1 2 3 0        1  | 0 1 2 3
      2  | 2 3 0 1        2  | 0 2 0 2
      3  | 3 0 1 2        3  | 0 3 2 1
```

```
ℤ₅    +  | 0 1 2 3 4      ·  | 0 1 2 3 4
     ----+----------     ----+----------
      0  | 0 1 2 3 4      0  | 0 0 0 0 0
      1  | 1 2 3 4 0      1  | 0 1 2 3 4
      2  | 2 3 4 0 1      2  | 0 2 4 1 3
      3  | 3 4 0 1 2      3  | 0 3 1 4 2
      4  | 4 0 1 2 3      4  | 0 4 3 2 1
```

```
ℤ₆    +  | 0 1 2 3 4 5    ·  | 0 1 2 3 4 5
     ----+------------   ----+------------
      0  | 0 1 2 3 4 5    0  | 0 0 0 0 0 0
      1  | 1 2 3 4 5 0    1  | 0 1 2 3 4 5
      2  | 2 3 4 5 0 1    2  | 0 2 4 0 2 4
      3  | 3 4 5 0 1 2    3  | 0 3 0 3 0 3
      4  | 4 5 0 1 2 3    4  | 0 4 2 0 4 2
      5  | 5 0 1 2 3 4    5  | 0 5 4 3 2 1
```

Qualche cosa si legge subito. Le tabelle dell'addizione sono tutte uguali nella forma: ogni riga è la precedente spostata di un posto, e lo 0 compare in ogni riga una volta sola, il che dice che ogni classe ha un opposto. Le tabelle sono simmetriche rispetto alla diagonale, perché le operazioni sono commutative.

Le tabelle della moltiplicazione invece sono molto diverse tra loro. In ℤ_{5} ogni riga, a parte quella dello 0, contiene tutte le classi, e quindi anche l'1. In ℤ_{6}, invece, le righe del 2, del 3 e del 4 non contengono l'1, e contengono lo 0 fuori dalla prima colonna: per esempio [2] · [3] = [6] = [0], anche se né [2] né [3] è la classe nulla. Nella tabella di ℤ_{10} succede lo stesso, con [4] · [5] = [0], e non vale nemmeno la legge di cancellazione: [2] · [4] = [8] = [7] · [4], ma [2] ≠ [7]. (In ℤ_{6} succede lo stesso, esempio nostro: [3] · [2] = [0] = [3] · [4], ma [2] ≠ [4].)

**Attenzione.** In ℤ un prodotto è zero solo se uno dei fattori è zero, e da a · c = b · c con c ≠ 0 si può semplificare c. In ℤ_{N} queste due regole possono essere false: prima di «semplificare» una classe in un'uguaglianza tra classi bisogna sapere che quella classe ha un inverso.

Quali classi di ℤ_{N} hanno un inverso rispetto al prodotto, e perché in ℤ_{5} ce l'hanno tutte (tranne lo 0) e in ℤ_{6} no, è l'argomento del prossimo capitolo.
