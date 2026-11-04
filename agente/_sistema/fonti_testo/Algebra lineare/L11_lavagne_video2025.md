# Algebra lineare, Lezione 11: Sistemi lineari I (lavagne dalla registrazione Webex del 17 ott 2025, prof. Radeschi)

Fonte: video della registrazione dell'anno scorso («Marco Radeschi-20251017 1502-1»), file `audio/algebra_L11_2025.mp4` (96 min 26 s, completo), trascrizione `trascrizioni/algebra_L11_2025.txt`.
Contenuto letto da 39 fotogrammi regolari (uno ogni 2,5 minuti, da 00:00 a 95:00; quello a 00:00 è nero, quindi 38 utili), più 9 fotogrammi intermedi aperti (55:30, 57:00, 90:30, 91:00, 91:30, 92:00, 95:40, 96:00, 96:20) e 3 ingrandimenti a piena risoluzione per controllare pedici e frazioni (59:08–59:26, 72:31, 80:00). La lavagna è in 4 pannelli (alto/basso, sinistra/destra) che vengono riempiti, fatti scorrere e cancellati; qui il contenuto è in ordine di comparsa.

Convenzioni:
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss, approssimati per eccesso: la scritta è già visibile a quel tempo).
- **[a voce]** indica ciò che è solo detto e non scritto; il tempo tra parentesi è quello dell'audio. Nella prima ora l'audio risulta in ritardo di 1–2 minuti rispetto ai fotogrammi (per esempio «0 = 1» è già scritto a 07:30, mentre nell'audio il commento arriva verso 08:20); dopo la pausa i due tempi coincidono quasi.
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali: sono ricostruite da una trascrizione automatica piena di errori.

## Titolo e definizione di sistema (00:00 – 03:30)
**LEZIONE 11: SISTEMI LINEARI I**
**Def.** Un sistema di k equaz. in n incognite è
Ⓢ { a₁,₁x₁ + a₁,₂x₂ + … + a₁,ₙxₙ = b₁ ; a₂,₁x₁ + a₂,₂x₂ + … + a₂,ₙxₙ = b₂ ; … ; a_k,₁x₁ + a_k,₂x₂ + … + a_k,ₙxₙ = b_k }
a_i,j = coefficienti, b_i = termini noti, x_i = incognite.

Il cerchietto Ⓢ a sinistra della graffa è il **nome del sistema** (non l'insieme delle soluzioni).

[a voce] (≈ 02:38) I coefficienti e i termini noti sono dati, sono numeri conosciuti; le x₁, …, xₙ sono i valori da trovare.

## Definizione di soluzione ed esempio (03:30 – 07:30)
**Def.** Dato Ⓢ, una **SOLUZIONE** di Ⓢ è l'assegn. di valori a x₁ … xₙ che soddisfino **TUTTE** le equazioni del sistema.

**Es.** { x₁ + x₂ + x₃ = 6 ; x₁ + x₂ − x₃ = 0 }
x₁ = 1, x₂ = 2, x₃ = 3 è una **SOLUZIONE**: { 1 + 2 + 3 = 6 ✓ ; 1 + 2 − 3 = 0 ✓ }

**Obiettivo:** calcolare **tutte** le soluz. di un sistema.

[a voce] (≈ 06:26) La soluzione (1, 2, 3) è «tirata fuori dal cappello»; non è l'unica, ce ne sono infinite. A volte invece le soluzioni possono non esserci.

[verifica] Tutte le soluzioni dell'esempio sono x₃ = 3, x₁ + x₂ = 3, cioè (3 − s, s, 3) con s ∈ ℝ: sono davvero infinite. Il docente non calcola questo insieme in lezione.

## Parentesi: l'equazione 0 = 1 (07:30)
Scritta sotto l'esempio, con un gesso di colore diverso secondo l'audio: se al sistema si aggiunge **0 = 1 ⟶ NO SOLUZ.**

[a voce] (≈ 08:20 – 09:27) Nessun valore di x₁, x₂, x₃ soddisfa l'ultima equazione. Nel processo di semplificazione ci si accorge che un sistema è impossibile perché sviluppa sempre un'equazione di questo tipo: se c'è, non ci sono soluzioni; e, in un certo senso, vale anche il contrario: un sistema senza soluzioni si può sempre riscrivere in modo che contenga un'equazione così.

## Idea e matrici associate (10:00 – 15:00)
**Idea:** manipolare il sistema, semplificandolo, ma mantenendo le stesse soluzioni.

[a voce] (≈ 09:27 – 10:33) È la stessa tecnica usata per il determinante nella lezione precedente: si semplifica la matrice con le mosse di Gauss finché il calcolo diventa facile, senza cambiare il risultato.

**Def.** Dato Ⓢ, definiamo:
1. La **MATRICE DEI COEFF.** A = ( a₁₁ … a₁ₙ ; a₂₁ … a₂ₙ ; … ; a_k1 … a_kn ) ∈ M(k, n)
2. Il **vettore dei termini noti** b = ( b₁ ; … ; b_k ) ∈ ℝᵏ
3. La **MATRICE COMPLETA** C = (A | b) = ( a₁₁ … a₁ₙ | b₁ ; … ; a_k1 … a_kn | b_k )

[a voce] (≈ 13:12 – 15:35) A ha tante righe quante equazioni e tante colonne quante incognite. La sbarra verticale in (A | b) è messa per ragioni puramente estetiche, per ricordare che l'ultima colonna è quella dei termini noti, e non ha alcuna funzione matematica.

## Esempio di matrici (15:00 – 20:00)
**Es.** Dato il sistema nell'esempio precedente, abbiamo
A = ( 1 1 1 ; 1 1 −1 ) ∈ M(2, 3), b = ( 6 ; 0 ), (A | b) = ( 1 1 1 | 6 ; 1 1 −1 | 0 ).

[a voce] (≈ 17:27 – 19:30) Osservazioni non scritte: (1) dare A e b dà le stesse informazioni che dare la matrice completa; (2) la matrice completa contiene tutte le informazioni per ricostruire il sistema, quindi si potrà parlare del «sistema dato da questa matrice», intendendo il sistema corrispondente; (3) ogni riga contiene i dati di un'equazione e ogni colonna quelli di una variabile: la prima colonna, (1, 1), contiene i coefficienti di x₁ nelle varie equazioni («ci servirà verso fine lezione»).

## Proposizione: le mosse di Gauss (20:00 – 27:30)
**Prop.** Dato un sistema Ⓢ, le seguenti operazioni non ne cambiano le soluzioni:
① Scambiare due righe (R_i ⟷ R_j)
② Moltiplicare una riga per un numero λ ≠ 0 (R_i ⟶ λR_i)
③ Aggiungere ad una riga il multiplo di un'altra (R_i ⟶ R_i + λR_j)
↳ **Oss.:** Queste sono le mosse di Gauss.

[a voce] (≈ 21:32 – 23:25) Scambiare due righe cambia solo l'ordine, il sistema resta lo stesso. λ deve essere diverso da zero: moltiplicando per 0 l'equazione diventa 0 = 0 e si cancella tutta l'informazione che conteneva. Moltiplicare per λ ≠ 0 non tocca le soluzioni, perché si può tornare indietro dividendo per λ.

[a voce] (≈ 24:04 – 24:42) Domanda di uno studente: si moltiplica tutta la riga, in tutti i termini, altrimenti si cambia il sistema.

La proposizione è enunciata senza dimostrazione scritta alla lavagna.

## Osservazione: righe del sistema e righe della matrice (27:30 – 32:00)
**Oss.** Con «Righe», nella proposizione, intendiamo sia le righe di Ⓢ, sia le righe di (A | b).

**Es.**
{ x₁ + x₂ + x₃ = 6 ; x₁ + x₂ − x₃ = 0 } —(R₁ → R₁ + R₂)→ { 2x₁ + 2x₂ = 6 ; x₁ + x₂ − x₃ = 0 }
↕ ↕
( 1 1 1 | 6 ; 1 1 −1 | 0 ) —(R₁ → R₁ + R₂)→ ( 2 2 0 | 6 ; 1 1 −1 | 0 )

(Le frecce doppie verticali collegano ogni sistema alla sua matrice completa.)

[a voce] (≈ 29:42 – 31:00) Fare una mossa sul sistema o sulla matrice completa è la stessa cosa. Strategia: si passa dal sistema alla matrice completa, si applicano le mosse in un ordine ben preciso fino a una matrice «semplice», si traduce di nuovo in sistema e lo si risolve.

## Pivot e matrici a scalini (32:30 – 35:00)
**Def.** Data una matrice C, per ogni riga definiamo il **PIVOT** come il primo el. ≠ 0, partendo da sinistra.

**Def.** Una matrice C è **A SCALINI** se:
– Il pivot di ogni riga è **STRETTAMENTE** a destra del pivot precedente
– le righe nulle sono al fondo

A = ( ①  2  3  4 ; 0  ⑤  6  7 ; 0  0  0  ⑧ ) (pivot cerchiati o riquadrati e scala disegnata sotto gli zeri).

[a voce] (≈ 35:49) «Strettamente» vuol dire che non possono esserci due pivot uno sopra l'altro. Il nome «a scalini» viene dalla forma degli zeri.

## Matrici a scalini ridotte (35:00 – 37:30)
**Def.** Matrice C a scalini è detta **RIDOTTA** se ogni pivot è = 1, e i valori sopra il pivot sono = 0.

**Es.** C = ( ① 0 0 4 ; 0 ① 0 3 ; 0 0 ① 5 ), C = ( ① 0 1 0 4 ; 0 ① 1 0 3 ; 0 0 0 ① 5 ).

Nel secondo esempio la terza colonna contiene 1, 1, 0 ma nessun pivot: gli zeri sono richiesti solo nelle colonne dei pivot.

## Risolvere sistemi con (A | b) a scalini (40:00 – 55:00)
**RISOLVERE SISTEMI CON (A | b) A SCALINI**

**① Matrice a scalini non ridotta (40:00 – 45:00)**
( ① 2 3 | 4 ; 0 ② 4 | 5 ; 0 0 ① | 1 ) ⟶ { **x** + 2y + 3z = 4 ; **2y** + 4z = 5 ; **z** = 1 }
(Le variabili dei pivot sono sottolineate.) Si risale dal basso:
z = 1
2y = 5 − 4z = 1 ⟶ y = ½
x = 4 − 2y − 3z = 4 − 1 − 3 = 0

[a voce] (≈ 41:56) Quando ci sono poche variabili si usano x, y, z invece di x₁, x₂, x₃. (≈ 42:39 – 43:48) Ogni equazione va risolta rispetto alla variabile del suo pivot, portando tutto il resto dall'altra parte, partendo dall'ultima equazione.

**② Matrice ridotta, soluzione unica (47:30)**
( 1 0 0 | 4 ; 0 1 0 | 3 ; 0 0 1 | 5 ) ⟶ { x = 4 ; y = 3 ; z = 5 }

**③ Matrice ridotta con una colonna senza pivot (50:00 – 55:00)**
( ① 0 1 0 | 4 ; 0 ① 1 0 | 3 ; 0 0 0 ① | 5 ) ⟷ { x + z = 4 ; y + z = 3 ; w = 5 } ⇝ x = 4 − z, y = 3 − z, w = 5, **z = libero!**
{ x = 4 − t ; y = 3 − t ; z = t ; w = 5 } t ∈ ℝ ⇝ **INFINITE SOLUZIONI, CHE DIPENDONO DA UN PARAMETRO**
(A 55:00 la terza colonna della matrice, quella di z, è riquadrata.)

[a voce] (≈ 50:53) A t si può dare qualunque valore (0, 1, π, 3 miliardi): ogni valore genera una soluzione.
[a voce] (≈ 52:40 – 53:04) Domanda di uno studente: cosa succede con una colonna di zeri? (La parola è storpiata nella trascrizione, il senso si ricava dalla risposta.) Risposta: la variabile corrispondente non compare mai, quindi le si può assegnare il valore che si vuole, e questo dà infinite soluzioni.
[a voce] (≈ 53:11 – 54:27) Il procedimento separa le variabili in due classi: quelle con pivot restano a sinistra dell'uguale, quelle senza pivot vanno a destra e sono libere di assumere qualunque valore. Il numero di parametri liberi è esattamente il numero di colonne senza pivot.

## Algoritmo di Gauss (55:30 – 67:30)
**ALGORITMI DI GAUSS & GAUSS-JORDAN**
**Gauss:** input: matrice C, output: matrice a scalini.

Diagramma di flusso scritto alla lavagna:
- rombo **C₁₁ ≠ 0?**
- **NO** ⟶ riquadro «**C₁ᵢ = primo elemento nonzero**» (il pedice è ripassato col gesso; si legge 1i) ⟶ riquadro **R₁ ⟷ Rᵢ** ⟶ si torna al rombo
- **SÌ** ⟶ riquadro «**Usare III mossa di Gauss per uccidere i termini sotto il pivot**» ⟶ riquadro «**Togliamo prima riga & colonna**» ⟶ si torna al rombo

**Esempio svolto a fianco:**
( 0 1 1 0 ; 1 1 2 −3 ; −1 2 1 1 ) (prima colonna riquadrata, 1 della seconda riga cerchiato)
—(R₁ ⟷ R₂)→ ( ① 1 2 −3 ; 0 1 1 0 ; −1 2 1 1 )
—(R₃ → R₃ + R₁)→ ( ① 1 2 −3 ; 0 ① 1 0 ; 0 3 3 −2 ) (sottomatrice ( 1 1 0 ; 3 3 −2 ) riquadrata, il 3 riquadrato a parte)
—(R₃ → R₃ − 3R₂)→ ( ① 1 2 −3 ; 0 ① 1 0 ; 0 0 0 ⊝2 ) (−2 cerchiato)

[a voce] (≈ 59:58) Correzione del docente: il primo elemento non zero si cerca **sulla colonna**, non sulla riga («se ho detto riga, scusa»).
[a voce] (≈ 60:00 – 60:35) Domanda di uno studente: se tutti gli elementi della colonna sono zero? Risposta: si salta tutto e si va avanti; il docente non complica il diagramma per questo caso, che quindi **non è scritto** nel diagramma.
[a voce] (≈ 62:01) La riga da aggiungere, a ogni passo, è sempre quella che contiene il pivot del momento.
[a voce] (≈ 66:53) Una macchina continuerebbe a ridursi ulteriormente finché non ha più senso; a questo punto si vede già che la matrice è a scalini.

## Algoritmo di Gauss-Jordan (67:30 – 80:00)
**Gauss Jordan:** input: Matrice a scalini; output: Matrice a scalini **RIDOTTA**.

Diagramma di flusso scritto alla lavagna:
- rombo **C'è un pivot?**
- **SÌ** ⟶ riquadro **Ultimo pivot** ⟶ riquadro «**III mossa per uccidere i valori sopra il pivot**» ⟶ riquadro «**Togliamo il pivot dalla lista**» ⟶ si torna al rombo
- **NO** ⟶ riquadro «**Usare II mossa per ridurre i pivot a 1**»

**Esempio svolto a fianco** (continua quello di Gauss; a ogni passo sono riquadrati i valori da uccidere):
( 1 1 2 −3 ; 0 1 1 0 ; 0 0 0 ⊝2 )
—(R₁ → R₁ − (3/2)R₃)→ ( 1 1 2 0 ; 0 ① 1 0 ; 0 0 0 ⊝2 )
—(R₁ → R₁ − R₂)→ ( ① 0 1 0 ; 0 ① 1 0 ; 0 0 0 ⊝2 )
—(R₃ → −½R₃)→ ( 1 0 1 0 ; 0 1 1 0 ; 0 0 0 1 )

[a voce] (≈ 70:16) «Uccidere» è il termine usato per «far diventare zero» («in matematica spesso si usano termini violenti»).
[a voce] (≈ 71:07 – 72:26) −3 − (3/2)(−2) = −3 + 3 = 0; la seconda e la terza riga restano uguali. La riga da sottrarre è sempre quella del pivot.
[a voce] (≈ 76:26 – 76:56) Ultima fase: si guarda quanto vale ogni pivot e si divide la sua riga per quel valore, se non è già 1. Qui i primi due valgono già 1 e la terza riga va divisa per −2.

## Risolvere un sistema lineare: la ricetta, primo esempio (80:00 – 90:00)
**RISOLVERE UN SISTEMA LINEARE**
{ y + z = 0 ; x + y + 2z = −3 ; −x + 2y + z = 1 }

**①** (A | b) = ( 0 1 1 | 0 ; 1 1 2 | −3 ; −1 2 1 | 1 )

**②** Gauss: ( 0 1 1 0 ; 1 1 2 −3 ; −1 2 1 1 ) ⇝ ( 1 1 2 | −3 ; 0 1 1 | 0 ; 0 0 0 | −2 )

**③a** Gauss Jordan: ( 1 1 2 | −3 ; 0 1 1 | 0 ; 0 0 0 | −2 ) ⇝ ( 1 0 1 | 0 ; 0 1 1 | 0 ; 0 0 0 | 1 )
{ **x** + z = 0 ; **y** + z = 0 ; **0** = 1 } ⇝ { x = −z ; y = −z ; 0 = 1 } ⟶ **NO SOLUZIONI**

**③b** { x + y + 2z = −3 ; y + z = 0 ; **0 = −2** } ⟶ **NO SOLUZIONI**

[a voce] (≈ 79:12 – 79:30) **Avvertimento sull'esame:** il primo passo, sempre, è scrivere la matrice completa: il docente dice che lo ripete sempre, ma poi all'esame davanti a un sistema si va nel panico e si comincia a usare un altro metodo (la frase esatta è storpiata nella trascrizione).
[a voce] (≈ 80:26 – 80:31) Non rifà i conti di Gauss e di Gauss-Jordan: la matrice è esattamente quella già ridotta nella sezione sugli algoritmi.
[a voce] (≈ 81:24) Dopo Gauss ci sono due scelte: continuare con Gauss-Jordan (③a) oppure riscrivere subito il sistema dalla matrice a scalini (③b). I due modi danno ovviamente lo stesso numero di soluzioni.
[a voce] (≈ 84:50 – 85:07) In ③a si risolve rispetto alle variabili dei due pivot; 0 = 1 vuol dire che il sistema è impossibile.
[a voce] (≈ 87:39 – 88:52) Qui si vede subito che non ci sono soluzioni. Senza quell'equazione, in ③b si sarebbero dovuti fare dei calcoli per risolvere il sistema, mentre in ③a sarebbe tutto più banale. I calcoli vanno fatti comunque: in ③a per applicare Gauss-Jordan, in ③b per risolvere il sistema. Di solito ③b (fermarsi a Gauss e risolvere il sistema) è un po' più veloce di tutto Gauss-Jordan.

## Secondo esempio: le prime due equazioni (90:00 – 96:26)
**Es.** { y + z = 0 ; x + y + 2z = −3 } ⟶ **①** (A | b) = ( 0 1 1 | 0 ; 1 1 2 | −3 )

**②** Gauss: ( ① 1 2 | −3 ; 0 ① 1 | 0 )

**③a** Gauss Jordan: ( ① [1] 2 −3 ; 0 ① 1 0 ) —(R₁ → R₁ − R₂)→ ( ① 0 1 | −3 ; 0 ① 1 | 0 )
⇝ { x + z = −3 ; y + z = 0 } ⇝ { x = −3 − z ; y = −z } ⇝ { x = −3 − t ; y = −t ; z = t }, t ∈ ℝ

**③b** { **x** + y + 2z = −3 ; **y** + z = 0 } : dall'ultima riga y = −z; poi x = −3 − y − 2z = −3 − z.

**Correzione del docente (≈ 90:50 – 91:30):** per ③a dice che Gauss-Jordan dà di nuovo le prime due righe della matrice ridotta del sistema precedente e comincia a scrivere ( 1 0 1 0 … ) (fotogramma a 91:00); poi nota che «c'è qualcosa di strano», dice che questa volta non è vero, cancella e rifà il conto (a 91:30 riparte da ( 1 1 2 … )). Il motivo, non detto esplicitamente nei tratti leggibili dell'audio, è che nel sistema precedente il −3 era stato ucciso usando la terza riga, che qui non c'è.
[verifica] Le righe sbagliate ( 1 0 1 | 0 ; 0 1 1 | 0 ) darebbero (−z, −z, z), che non è la soluzione: la riga x + y + 2z = −3 non sarebbe soddisfatta.

[a voce] (≈ 93:12) In ③a la variabile z è completamente libera, da cui il parametro t. (≈ 94:29) Il sistema di ③b è quello di partenza con le due equazioni scambiate, e si risolve partendo dal basso. (≈ 95:32 – 96:08) Le soluzioni sono le stesse di ③a; l'unica differenza è dove si fa il calcolo: in ③a nel passaggio R₁ → R₁ − R₂, in ③b dopo, per trovare le soluzioni.

La lezione finisce qui. Non arriva al sistema omogeneo associato.

## Controllo dei conti con SymPy
Rifatti con SymPy (`linsolve`, `rref`, operazioni elementari passo per passo). Tutti i risultati scritti alla lavagna sono corretti.
- Es. iniziale: 1 + 2 + 3 = 6, 1 + 2 − 3 = 0; insieme completo (3 − s, s, 3).
- R₁ → R₁ + R₂ sull'es. iniziale: ( 2 2 0 | 6 ; 1 1 −1 | 0 ), stesse soluzioni.
- Sistema ①: (0, ½, 1). Sistema ②: (4, 3, 5). Sistema ③: (4 − t, 3 − t, t, 5).
- Gauss: ( 1 1 2 −3 ; 0 1 1 0 ; 0 0 0 −2 ), ogni passaggio intermedio coincide.
- Gauss-Jordan: ( 1 0 1 0 ; 0 1 1 0 ; 0 0 0 1 ), coincide con `rref`; ogni passaggio intermedio coincide.
- Sistema a tre equazioni: insieme vuoto.
- Sistema a due equazioni: `rref` = ( 1 0 1 −3 ; 0 1 1 0 ); soluzioni (−3 − t, −t, t).

Errori e correzioni del docente: la partenza sbagliata di ③a nel secondo esempio (corretta da lui, nessuna traccia nel risultato finale); il lapsus «riga» per «colonna» nella ricerca del pivot (corretto a voce); il pedice C₁ᵢ, che per il primo elemento non zero **della prima colonna** dovrebbe essere Cᵢ₁ (non corretto alla lavagna).

## Punti illeggibili
Nessuna formula è rimasta illeggibile: [illeggibile] non compare. Il pedice di C₁ᵢ è ripassato col gesso: si legge 1i, e anche a voce il docente dice «C1i». Parte dell'audio resta persa nella trascrizione automatica: vedi sotto.

## Note sulla trascrizione audio
La trascrizione (`algebra_L11_2025.txt`) contiene lunghi tratti allucinati (ripetizioni di «modulo», «di Gauss, rango», «mappa lineare»), dovuti ai suggerimenti lessicali dati a Whisper: non sono parole del docente. Per le annotazioni [a voce] è stata fatta una ritrascrizione parziale senza suggerimenti (modello small, solo per questo lavoro; il risultato non è stato salvato fra i file del sistema) dei tratti 00:50–12:40, 17:13–24:05, 52:40–53:58, 59:00–60:00, 76:26–78:05, 79:30–80:35, 81:59–83:00, 84:00–85:37, 86:57–88:15, 90:50–91:30, 92:39–93:55. Restano non riascoltati gli altri tratti allucinati (fra cui 27:55–29:10, 30:55–31:55, 36:29–37:15, 43:09–43:50, 44:24–46:30, 46:49–49:40, 61:30–63:00, 64:40–66:55, 68:00–69:45, 70:16–71:10, 73:02–74:06): in questi potrebbero esserci commenti a voce non riportati qui. Fidarsi della lavagna per le formule.
