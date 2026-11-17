# 47. Ogni Numero Primo è Irriducibile
## Irriducibile: due modi di dirlo
Nel cap. 44 sono state date, una dopo l'altra, le definizioni di numero irriducibile e di numero primo, e il confronto era rimasto in sospeso. Ora ci sono gli strumenti per fare il primo passo. Si comincia riscrivendo la definizione di irriducibile con il linguaggio dei divisori.

Ogni intero n ≠ 0, ±1 ha almeno i quattro divisori 1, −1, n e −n (cap. 45). Un numero è irriducibile quando non ne ha altri.

**Proposizione.** Sia n ∈ ℤ con n ≠ 0, 1, −1. Allora n è irriducibile se e solo se gli unici divisori di n sono ±1 e ±n. In altre parole: se n = a · b, allora a = ±1 oppure b = ±1.

(In parole povere: un numero irriducibile non si lascia dividere da niente, a parte i divisori che ha qualunque numero.)

Le due formulazioni dicono la stessa cosa. Se n = a · b, allora a è un divisore di n; se i divisori sono solo ±1 e ±n, o a = ±1, oppure a = ±n e allora, semplificando n ≠ 0 in n = (±n) · b, si ottiene b = ±1: in ogni caso un fattore è invertibile, come chiede la definizione del cap. 44. Viceversa, se d è un divisore di n, allora n = d · c per qualche intero c; se n è irriducibile uno dei due fattori è ±1, quindi d = ±1 oppure c = ±1, e in questo secondo caso n = ±d, cioè d = ±n.

**Esempio.** Sono irriducibili 2, 3, 5, 7 e anche −2, −3, −5, −7: i divisori di −7 sono soltanto 1, −1, 7, −7. Invece 6 è riducibile, perché oltre a ±1 e ±6 ha i divisori ±2 e ±3; e infatti 6 = 2 · 3, con nessuno dei due fattori invertibile.

## Primo: la definizione, di nuovo
**Definizione.** Sia n ∈ ℤ con n ≠ 0, 1, −1. Si dice che n è **primo** se per ogni a, b ∈ ℤ vale: se n | a · b, allora n | a oppure n | b.

(In parole povere: quando un numero primo divide un prodotto, divide già uno dei due fattori. Non può «formarsi» mettendo insieme pezzi di a e pezzi di b.)

Conviene leggerla accanto alla proposizione del cap. 45: per qualunque n, se n | a allora n | a · b. I numeri primi sono quelli per cui vale anche il percorso inverso, dal prodotto a uno dei fattori: se n | a · b, allora n | a oppure n | b.

**Esempio.** 7 è primo: per esempio 7 | 84 = 4 · 21, e in effetti 7 | 21. Un esempio però non basta, perché la definizione riguarda tutti i prodotti possibili: per ora lo si accetta, e si capirà come giustificarlo quando sarà chiaro il legame con gli irriducibili. Invece per dire che un numero non è primo basta un solo prodotto che vada storto: 6 non è primo, perché 6 | 2 · 3 (infatti 2 · 3 = 6), ma 6 non divide 2 e non divide 3.

## Primo implica irriducibile
**Proposizione.** Se n è primo, allora n è irriducibile.

(In parole povere: un numero che non divide mai un prodotto «di nascosto» non si può nemmeno spezzare in due fattori veri.)

**Dimostrazione.** Sia n primo e si supponga n = a · b, con a, b ∈ ℤ. Bisogna far vedere che uno dei due fattori è ±1.
1. Ogni numero divide se stesso, quindi n | n = a · b.
2. Poiché n è primo, n | a oppure n | b. Si supponga n | a; nell'altro caso il ragionamento è lo stesso, con a e b scambiati.
3. Da n | a segue |n| ≤ |a| (cap. 45: un divisore non supera in valore assoluto il numero che divide; qui a ≠ 0, perché n ≠ 0).
4. D'altra parte n = a · b dà |n| = |a| · |b|. Sostituendo, |a| · |b| ≤ |a|, e dividendo per |a|, che è positivo, |b| ≤ 1.
5. Il numero b non è 0, perché n ≠ 0. Quindi |b| = 1, cioè b = ±1.

Dunque in ogni scrittura n = a · b uno dei fattori è invertibile: n è irriducibile. ∎

**Esempio.** La proposizione si può leggere anche al contrario: un numero riducibile non è primo. Lo mostra la dimostrazione stessa: se n = a · b e n dividesse a si ricaverebbe b = ±1, e se dividesse b si ricaverebbe a = ±1; quindi, quando nessuno dei due fattori è invertibile, n divide a · b senza dividere né a né b. La scomposizione fornisce dunque il prodotto che serve. Da 6 = 2 · 3 si ha 6 | 2 · 3 con 6 che non divide né 2 né 3. Da 10 = 2 · 5 si ha 10 | 2 · 5 con 10 che non divide né 2 né 5.

## E il viceversa?
Vale anche l'implicazione opposta: se n è irriducibile, allora n è primo. La dimostrazione però è rimandata. Per ora la situazione è questa:
- primo ⟹ irriducibile: dimostrato in questo capitolo;
- irriducibile ⟹ primo: vero, ma ancora da dimostrare.

Il contrasto con la terminologia di scuola c'è già adesso: lì si chiama primo un numero che ha come divisori solo 1 e se stesso, cioè proprio la proprietà che qui si chiama irriducibilità. Quando anche la seconda implicazione sarà dimostrata, in ℤ «primo» e «irriducibile» indicheranno gli stessi numeri, e si vedrà che per gli interi il cambio di nome non cambia nulla. Le due definizioni restano comunque diverse, e fino a quando il viceversa non è dimostrato vanno tenute distinte: per provare che un numero è irriducibile si guardano i suoi divisori, per provare che è primo si guardano i prodotti che divide. Inoltre qui contano anche i numeri negativi: −2, −3, −5, −7 sono irriducibili quanto 2, 3, 5, 7.
