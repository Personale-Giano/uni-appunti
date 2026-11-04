# Algebra lineare, Lezione 13: Sistemi lineari III, applicazioni a indipendenza, generatori, basi e codici correttori (lavagne dalla registrazione Webex del 27 ott 2025, prof. Radeschi)

Fonte: video della registrazione dell'anno scorso, file `audio/algebra_L13_2025.mp4` (100 min 10 s, completo; la pausa non è registrata), trascrizione `trascrizioni/algebra_L13_2025.txt`.
Contenuto letto da 41 fotogrammi regolari (uno ogni 2,5 minuti, da 00:00 a 100:00; quello a 00:00 è nero, quindi 40 utili), più 8 fotogrammi intermedi aperti (26:30, 36:30, 54:00, 61:00, 94:30, 97:00, 99:30, 100:05) e 24 ingrandimenti a piena risoluzione per controllare pedici e matrici (fra cui 12:30, 21:30, 27:00, 34:30, 36:30, 54:30, 55:00, 59:30, 63:30–63:45, 67:30, 72:30, 77:30, 82:30, 96:00, 99:30). La lavagna è in 4 pannelli (alto/basso, sinistra/destra) che vengono riempiti, fatti scorrere e cancellati; qui il contenuto è in ordine di comparsa.

Convenzioni:
- I tempi senza altra indicazione sono quelli dei fotogrammi (mm:ss, approssimati per eccesso: la scritta è già visibile a quel tempo).
- **[a voce]** indica ciò che è solo detto e non scritto; il tempo tra parentesi è quello dell'audio. I tempi dell'audio vanno da quasi coincidenti ad anticipati di 1–2 minuti rispetto ai fotogrammi.
- **[verifica]** indica un controllo fatto a posteriori con SymPy, non presente in lezione.
- Le parole del docente non sono citazioni letterali: sono ricostruite da una trascrizione automatica piena di errori.
- Sulla lavagna il rango è scritto rg(A) (nella L12 era rK); l'abbreviazione di «tale che» è scritta Tc (qui t.c.); il polinomio è p(x), a tratti P(x); il valore incognito nella correzione è una K maiuscola. Qui sono riportati così.

## Titolo e ripasso (00:00 – 07:30)
**LEZIONE 13: SISTEMI LINEARI, III**
**RICORDIAMO:** V sp. vettoriale, v₁ … v_k ∈ V sono
- lin. ind. se 0_V = a₁v₁ + … + aₙv_k ⟹ a₁ = 0 = … = a_k = 0
- generatori se ∀w ∈ V, w = a₁v₁ + … + a_kv_k
- una base se lin. ind. & generatori

**Q:** dati v₁ … v_k come determiniamo se sono lin. indip./gen.?

(La dicitura «v_k ∈ V sono» è coperta dal proiettore e si legge a 07:30, quando il pannello è abbassato. Nella prima riga è scritto aₙv_k: vedi errori.)

[a voce] (≈ 00:02 – 00:36) Iniziano i tutoraggi, divisi per canale; si può andare a quello che si preferisce, perché tutti fanno la stessa cosa.
[a voce] (≈ 01:09 – 01:44) Oggi si finisce di parlare di sistemi lineari e se ne vedono le applicazioni: alla teoria degli spazi vettoriali, rispondendo a domande lasciate in sospeso, e nella seconda parte al mondo vero.
[a voce] (≈ 04:36 – 05:18) Dati v₁ … v_k, si determina se sono indipendenti o generatori nel caso speciale in cui siano vettori di 𝕂ⁿ.

## Indipendenza lineare: dall'esempio al sistema (07:30 – 20:00)
**LIN. INDIP.**
**Es:** v₁ = ( 1 ; 0 ; −1 ), v₂ = ( 1 ; −1 ; 0 ), v₃ = ( 0 ; 1 ; −1 ) ∈ ℝ³. Sono l.i.?

[ **No:** v₁ − v₂ − v₃ = 0_V ] (fra parentesi quadre, a parte)

⇝ Consideriamo λ₁( 1 ; 0 ; −1 ) + λ₂( 1 ; −1 ; 0 ) + λ₃( 0 ; 1 ; −1 ) = ( 0 ; 0 ; 0 ) ⊛
e chiediamoci per quali valori di λ₁, λ₂, λ₃ vale ⊛? (una freccia va dal punto interrogativo a ⊛)

[ Se l'unica soluzione è per λ₁ = λ₂ = λ₃ = 0 ⟹ v₁, v₂, v₃ sono l.i.
altrimenti, v₁, v₂, v₃ non sono l.i. ] (riquadrato a 20:00)

⊛ ⇝ ( λ₁ + λ₂ ; −λ₂ + λ₃ ; −λ₁ − λ₃ ) = ( 0 ; 0 ; 0 ) ⟷ { λ₁ + λ₂ = 0 ; −λ₂ + λ₃ = 0 ; −λ₁ − λ₃ = 0 } ↗ **SISTEMA OMOGENEO**

(A | b) = ( 1 1 0 | 0 ; 0 −1 1 | 0 ; −1 0 −1 | 0 ) ⇝, con le graffe sotto le colonne: v₁, v₂, v₃

**Correzione del docente:** a 12:30 la prima componente è scritta λ₁ + λ₃; a 15:00 è già λ₁ + λ₂. A voce (≈ 12:13) dice «λ₁ per 1 più λ₂ per 1 più λ₃ per 0, quindi λ₁ + λ₂».

[a voce] (≈ 07:20 – 07:52) Esiste una combinazione lineare non banale, con coefficienti non tutti nulli, che dà zero: v₁ − v₂ − v₃. «Questo basterebbe» per rispondere di no.
[a voce] (≈ 09:31 – 10:54) Con λ₁ = λ₂ = λ₃ = 0 l'uguaglianza vale sempre; quindi due cose possono accadere: o questa è l'unica soluzione, e per definizione i vettori sono indipendenti, oppure ce ne sono altre, e non lo sono.
[a voce] (≈ 14:33) Il sistema è omogeneo: si ricorda che per un sistema omogeneo l'insieme delle soluzioni è uno spazio vettoriale.
[a voce] (≈ 15:49 – 16:27) I coefficienti di λ₁ sono esattamente gli elementi di v₁: la prima colonna è il vettore v₁, la seconda v₂, la terza v₃. **Quindi, con il senno di poi, si può saltare tutto** e scrivere subito il sistema prendendo i vettori e mettendoli in un'unica matrice. Più che calcolare le soluzioni, interessa sapere se c'è un'unica soluzione.

## Rouché-Capelli: il criterio «ogni colonna ha un pivot» (20:00 – 25:00)
Il sistema ha una unica sol ⟺ v₁ v₂ v₃ sono l.i.

**Rouché Capelli:**
Se ∃ soluzione ⟹ questa è unica ⟺ num di pivot = rg(A) = n num di colonne = n num di vettori
⇝ (freccia ondulata, poi riquadrato:)
**[ v₁ v₂ v₃ sono l.i. ⟺ Riducendo A = (v₁ | v₂ | v₃) a scalini, ogni colonna ha un pivot ]**

[a voce] (≈ 19:54 – 20:50) La soluzione è unica quando il rango della matrice dei coefficienti è uguale al numero n di variabili, cioè al numero di colonne di A, che in questo caso è il numero di vettori considerati. Il rango si calcola riducendo a scalini e contando i pivot.
[a voce] (≈ 21:20 – 21:53) **Ogni colonna ha al massimo un pivot** (uno o nessuno), quindi il numero di pivot è uguale al numero di colonne se e solo se ogni colonna ha un pivot.
[a voce] (≈ 22:38 – 23:08) «Questa la potete pensare come la risposta definitiva», non solo per questi tre vettori ma nel caso generale di vettori in 𝕂ᵐ.

## Il criterio applicato all'esempio (25:00 – 30:00)
**Nel nostro esempio**
( ① 1 0 | 0 ; 0 −1 1 | 0 ; [−1] 0 −1 | 0 ) —(R₃ → R₃ + R₁)→ ( ① 1 0 | 0 ; 0 ⊖1 1 | 0 ; 0 [1] −1 | 0 ) —(R₃ → R₃ + R₂)→ ( ① 1 0 | 0 ; 0 ⊖1 1 | 0 ; 0 0 0 | 0 )

(Il −1 da eliminare e poi l'1 da eliminare sono riquadrati, gli zeri e i pivot sono cerchiati, nell'ultima matrice la terza colonna è riquadrata.)
↑ **No pivot** ⟹ **v₁, v₂, v₃ NON SONO L.IND.**

[a voce] (≈ 26:05 – 26:40) Riducendo a scalini, ogni colonna ha un pivot? No, questa colonna non ce l'ha, quindi i vettori non sono indipendenti.
[a voce] (≈ 26:40 – 27:17, frase rovinata nella trascrizione) Aggiungendo altri vettori non c'è modo di inserire un pivot in quella colonna: conferma l'intuizione che, se tre vettori sono già dipendenti, aggiungere altra roba non migliora la situazione.

## Trovare la relazione di dipendenza (30:00 – 36:30)
Si riscrive il sistema dall'ultima matrice. Le variabili dei pivot λ₁ e −λ₂ sono sottolineate due volte:
{ **λ₁** + λ₂ = 0 ; **−λ₂** + λ₃ = 0 ; 0 = 0 } ⟶ { λ₂ = λ₃ ; λ₁ = −λ₂ = −λ₃ }

{ λ₁ = −t ; λ₂ = t ; λ₃ = t } ⇝ ( λ₁ ; λ₂ ; λ₃ ) = { ( −t ; t ; t ) | t ∈ ℝ } = Span( −1 ; 1 ; 1 )
(sotto il vettore, con un uguale verticale: t( −1 ; 1 ; 1 ))

⇝ Per λ₁ = −1, λ₂ = 1, λ₃ = 1 otteniamo: **[ −v₁ + v₂ + v₃ = 0 ]**

(A 35:00 è sottolineata la combinazione λ₁( … ) + λ₂( … ) + λ₃( … ) dell'equazione ⊛.)

[a voce] (≈ 27:17 – 27:51) Qui ci si può fermare, ma **«vi potrebbe venire richiesto» di trovare una relazione tra i vettori**, come quella scritta prima e «uscita dal nulla»: la si ritrova con questo sistema.
[a voce] (≈ 29:03 – 29:33) C'è un metodo standard che funziona sempre: per ogni equazione ci si ricorda delle variabili che corrispondono ai pivot e si risolve rispetto a quelle.
[a voce] (≈ 32:30) Ha preso l'equazione di partenza e ha scritto una delle soluzioni trovate: è, a meno del segno, la relazione di prima, che in questo caso si poteva vedere facilmente.
[a voce] (≈ 33:40 – 34:17) A t si può assegnare il valore che si preferisce: ogni valore di t risolve l'equazione.
[a voce] (≈ 34:17 – 35:26) **Riassunto:** dati dei vettori, per capire se sono indipendenti li si mette in un'unica grande matrice e si guarda se, riducendo a scalini, ogni colonna ha un pivot. Se ci sono colonne senza pivot sono dipendenti. Questo risponde già alla domanda.
[a voce] (≈ 35:26 – 35:56) Se venisse chiesto quali sono le dipendenze, teoricamente ci si chiede quali λ soddisfano l'equazione; in pratica si prende il sistema ridotto e lo si risolve (il seguito si perde nella trascrizione).

[verifica] Le due relazioni sono la stessa a meno del segno: −v₁ + v₂ + v₃ = −(v₁ − v₂ − v₃). `nullspace` di A = { (−1, 1, 1) }, rk A = 2, det A = 0.

## Generatori: l'esempio in ℝ² (37:30 – 47:30)
**GENERATORI**
**Es:** v₁ = ( 3 ; 2 ), v₂ = ( 1 ; 5 ), v₃ = ( −1 ; 7 ) ∈ ℝ²
Sono v₁, v₂, v₃ generatori?

v₁, v₂, v₃ sono generatori ⟺ ∀( a ; b ) ∈ ℝ² ∃ λ₁ λ₂ λ₃ t.c. **[ λ₁v₁ + λ₂v₂ + λ₃v₃ = ( a ; b ) ]** (riquadrato a 47:30)
(con una freccia verso l'uguaglianza:) = λ₁( 3 ; 2 ) + λ₂( 1 ; 5 ) + λ₃( −1 ; 7 )

⇝ ( 3λ₁ + λ₂ − λ₃ ; 2λ₁ + 5λ₂ + 7λ₃ ) = ( a ; b )
{ 3λ₁ + λ₂ − λ₃ = a ; 2λ₁ + 5λ₂ + 7λ₃ = b } ⟷ ( 3 1 −1 | a ; 2 5 7 | b ), con le graffe sotto le colonne: v₁, v₂, v₃

[a voce] (≈ 37:07) Le definizioni che riguardano l'essere linearmente indipendenti assomigliano a quelle corrispondenti per i generatori, ma sono «simili ma non uguali»; vedremo che anche qui sarà così.
[a voce] (≈ 38:59 – 39:40) La risposta potrebbe essere particolarmente semplice, ma lo scopo è una regola generale che si applichi sempre, nel caso di n vettori in 𝕂ᵐ.
[a voce] (≈ 40:23 – 41:06) A destra non c'è un vettore specifico ma un vettore che può assumere qualunque valore. Ma questo non impedisce di andare avanti (il seguito si perde).
[a voce] (≈ 43:25 – 44:34) a e b non sono incognite: sono numeri dati, che possono assumere qualunque valore. Se si riesce a trovare una coppia a, b per cui non c'è soluzione, quel vettore non è raggiunto da v₁, v₂, v₃.
[a voce] (≈ 45:51 – 46:35) Di nuovo, come prima, le colonne della matrice sono i vettori. Con il senno di poi ci si può evitare tutto il discorso: si affiancano i vettori in una matrice unica e ci si chiede se il sistema ammette soluzioni per qualunque valore inserito a destra.

## Rouché-Capelli, seconda forma, e l'esempio (47:30 – 55:00)
**ROUCHÉ CAPELLI:** Sia (A | b) sistema, che, in forma a scalini, sia (A′ | c) ⟹ Il sistema ha soluzione se e solo se **tutti i pivots stanno in A′**

**Nel nostro caso:**
( ③ 1 −1 | a ; [2] 5 7 | b ) —(R₂ → 3R₂ − 2R₁)→ ( ③ 1 −1 | a ; 0 ⑬ 23 | 3b − 2a ), con una parentesi sopra il blocco A′

⟹ ∀a, b, il sistema ha soluzione ⟹ v₁, v₂, v₃ generatori

**Riga aggiunta per il controesempio** (visibile da 55:00, tratti sottili): sotto la matrice sono scritti tre zeri piccoli, 0 0 0, e nell'ultima colonna un ⁎, a cui punta una freccia. Non sono parte del conto: rappresentano una riga nulla ipotetica.

[a voce] (≈ 47:17 – 49:07) Rouché-Capelli è scritto in una maniera leggermente diversa dalla volta scorsa, ma equivalente: il sistema ha soluzione se e solo se tutti i pivot stanno in A′, cioè **se non ci sono pivot nell'ultima colonna**.
[a voce] (≈ 50:26 – 51:01) «Non ho scelto bene i coefficienti». Usa 3 volte la seconda riga meno 2 volte la prima (nella trascrizione «la terza»; alla lavagna R₁) e «otteniamo lo stesso effetto». Il tratto in mezzo è perso: che il motivo sia evitare le frazioni è una deduzione, non è nella parte leggibile dell'audio.
[a voce] (≈ 52:16 – 53:26) I pivot sono tutti nella prima matrice, **indipendentemente dai valori di a e b**. Quindi per ogni scelta di a e b il sistema ha soluzione, cioè ogni vettore si scrive come combinazione lineare: v₁, v₂, v₃ sono generatori.
[a voce] (≈ 53:26 – 54:42) **Quando non funzionerebbe:** immaginiamo di ottenere, riducendo, una riga di tutti zeri nella matrice. Nell'ultima colonna ci sarebbe una qualche combinazione lineare di a e b. «Non mi metterò a farlo», ma il punto è che (la frase si perde; riprende a ≈ 55:24 con «non aveva soluzione»).

[verifica] 3·2 − 2·3 = 0, 3·5 − 2·1 = 13, 3·7 − 2·(−1) = 23, ultimo termine 3b − 2a. Risolvendo in funzione di λ₃: λ₁ = (5a − b + 12λ₃)/13, λ₂ = (−2a + 3b − 23λ₃)/13. rk A = 2. Non calcolato in lezione: tre vettori in ℝ² non sono mai indipendenti, e qui la terza colonna è senza pivot.

## Regola generale per i generatori (55:00 – 57:30)
**Dati v₁, …, vₙ ∈ 𝕂ᵐ e A = (v₁ | … | vₙ), allora**
**v₁ … vₙ sono generatori ⟺ Riducendo A a scalini ogni riga ha un pivot** (sottolineato)

(Sotto c'è una lunga riga di separazione.)

[a voce] (≈ 55:24 – 57:20) Riscrive a livello proprio algoritmico: i vettori sono generatori se e solo se, riducendo A a scalini, ogni riga ha un pivot, **o in altre parole non ci sono righe completamente nulle**.
[a voce] (≈ 57:20) Il confronto con la condizione per l'indipendenza è detto ma è rovinato nella trascrizione.

**Pausa.** Il docente annuncia dieci minuti di pausa (≈ 57:30). A 60:00 la lavagna è ancora identica, a 61:00 è già cancellata: la pausa è tagliata dal video.

## Basi e coordinate (61:00 – 67:30)
[a voce] (≈ 60:23 – 61:10) **Riepilogo:** per determinare se dei vettori in 𝕂ᵐ sono indipendenti o generatori, in entrambi i casi si crea la matrice e si guardano i pivot: **se ogni riga ha un pivot sono generatori, se ogni colonna ha un pivot sono linearmente indipendenti.**

**BASI**
Ricordiamo: v₁, … vₘ ∈ V base
⟹ ∀v ∈ V, v = a₁v₁ + … + aₙvₙ dove a₁, … aₙ **unici**
(a₁ … aₙ) = COORDINATE DI v, nella base v₁ … vₙ

**Nessuna dimostrazione dell'unicità è scritta alla lavagna**: è un richiamo.

**Es:** sia ( 1 ; 1 ; 0 ) = v₁, ( 0 ; 1 ; 1 ) = v₂, ( 1 ; 0 ; 1 ) = v₃ base di ℝ³
Dato v = ( 1 ; 2 ; 3 ), calcolare coordinate di v in {v₁, v₂, v₃}

⇝ ( 1 ; 2 ; 3 ) = λ₁( 1 ; 1 ; 0 ) + λ₂( 0 ; 1 ; 1 ) + λ₃( 1 ; 0 ; 1 ) ⟵ TROVARE λ₁ λ₂ λ₃
(freccia ondulata in giù) ↪ Sistema ( 1 0 1 | 1 ; 1 1 0 | 2 ; 0 1 1 | 3 ) ⟵ TROVARE **LA** SOLUZIONE DEL SISTEMA (LA sottolineato due volte)

**Correzione del docente:** la componente centrale di v₁ è un 1 scritto sopra una sbavatura, già a 63:45. Quello che c'era sotto non si vede (il docente copre con la mano). Nella trascrizione (≈ 63:11) si legge «1 1 anzi».

[a voce] (≈ 65:32 – 66:02) I coefficienti devono esistere ed essere unici, quindi ci si aspetta che il sistema abbia un'unica soluzione: è esattamente quella che si cerca.
[a voce] (≈ 66:02 – 66:36) «Vi chiedo di saltare un passaggio»: è il sistema la cui matrice ha come colonne i vettori dati e come termini noti le componenti del vettore noto.

## Due modi per trovare le coordinate (67:30 – 77:30)
**⇝ Due modi.**
**① Risolvere il sistema**
( ① 0 1 | 1 ; [1] 1 0 | 2 ; 0 1 1 | 3 ) —(R₂ → R₂ − R₁)→ ( ① 0 1 | 1 ; 0 ① −1 | 1 ; 0 [1] 1 | 3 ) —(R₃ → R₃ − R₂)→ ( ① 0 1 | 1 ; 0 ① −1 | 1 ; 0 0 ② | 2 )

(Sulla prima freccia il pedice dell'ultima R non si distingue; il conto è con R₁. Sotto i pivot gli zeri sono cerchiati.)

⇝ { λ₁ + λ₃ = 1 ; λ₂ − λ₃ = 1 ; 2λ₃ = 2 } ⟶ λ₃ = 1 ; λ₂ = 1 + λ₃ = 2 ; λ₁ = 1 − λ₃ = 0
⇝ ( 1 ; 2 ; 3 ) = 0( 1 ; 1 ; 0 ) + 2( 0 ; 1 ; 1 ) + 1·( 1 ; 0 ; 1 )
⟹ **LE COORD. DI ( 1 ; 2 ; 3 ) in v₁ v₂ v₃ sono (0, 2, 1)**

**② Riscriviamo il sistema come**
A x = b dove A = (v₁ | … | vₘ), x = ( λ₁ ; ⋮ ; λₘ ), b = ( b₁ ; ⋮ ; bₘ ), e sotto, con un uguale verticale: ( 1 0 1 ; 1 1 0 ; 0 1 1 ), ( λ₁ ; λ₂ ; λ₃ ), ( 1 ; 2 ; 3 )
Il sistema ha 1 soluz. ⟹ A è invertibile, e ⟹ **[ x = A⁻¹b ]** (riquadrato, A⁻¹ sottolineato due volte)

**Il calcolo con l'inversa non è fatto in lezione.**

[a voce] (≈ 71:49 – 72:22) Il modo alternativo: quando la matrice dei coefficienti è invertibile, cioè quando si sa di avere un'unica soluzione come in questo caso, perché si ha a che fare con una base, si riscrive il sistema come A x = b.
[a voce] (≈ 74:13 – 75:30) Non si risolve un sistema ma si calcola l'inversa; in entrambi i casi ci sono conti da fare. Per mancanza di tempo il secondo approccio lo lascia agli studenti.

[verifica] det A = 2, A⁻¹ = ½( 1 1 −1 ; −1 1 1 ; 1 −1 1 ), A⁻¹b = (0, 2, 1): i due modi coincidono.

## Codici correttori: l'idea ingenua (77:30 – 82:30)
Figura: un omino dice **CIAO** (nuvoletta) al suo computer; freccia ondulata a **3, 9, 1, 15** ⇝ (trasmissione con una ✱ che segna il disturbo) ⇝ **13, 9, 1, 15**; un secondo omino con computer legge **MIAO**.

Sotto, dal primo computer con freccia ondulata:
3, 9, 1, 15, 3, 9, 1, 15 ⇝ 3, 9, 1, 15, 13, 9, 1, 15 (a 80:00)
poi, aggiungendo una terza copia a sinistra e una a destra:
3, 9, 1, 15, 3, 9, 1, 15, 3, 9, 1, 15 ⇝ 3, 9, 1, 15 | 13, 9, 1, 15 | 3, 9, 1, 15 (a 82:30, con due sbarre verticali di separazione)

(Nella seconda copia la cifra 1 di 15 è confusa da un segno verticale e da una sbavatura: si legge quasi «5». Il senso, una sola lettera modificata, richiede 15.)

[a voce] (≈ 75:30 – 76:09) I codici correttori sono «una bellissima applicazione», un'applicazione alla vita vera: quando si trasmette un segnale di dati da una persona all'altra ci può essere un errore.
[a voce] (≈ 78:07 – 78:38) Serve un algoritmo che non mandi solo il messaggio, ma permetta al computer che riceve di determinare due cose: se c'è stato un errore e dove.
[a voce] (≈ 78:38 – 80:43) Un primo modo ingenuo è mandare il messaggio due volte. Supponendo per comodità, «cosa falsa», che ci sia al più un errore, il ricevente vede due messaggi diversi e capisce che c'è stato un errore, ma non dove. Allora lo si manda tre volte (il seguito si perde).
[a voce] (≈ 81:19 – 81:52) **Quattro richieste:** un algoritmo che (1) determini quando c'è stato un errore, (2) determini dove, (3) lo corregga ritrovando il messaggio giusto, (4) non riempia tutta la memoria per mandare un messaggio di quattro lettere.

## Algoritmo di Reed-Solomon: costruzione (82:30 – 87:30)
**Algoritmo di Reed-Solomon**
**Ciao** ⇝ 2, −7, 8, −2 ⇝ **2, −7, 8, −2, a, b** ⟵ scelti così:

(riquadro che racchiude il seguito)
2x⁵ − 7x⁴ + 8x³ − 2x² + ax + b = p(x)
chiediamo che p(1) = 0 = p(2), in altre parole
p(2) = 64 − 7·16 + 8·8 − 2·4 + 2a + b = 0 ⇝ { 2a + b = −8
p(1) = 2 − 7 + 8 − 2 + a + b = 0 ⇝ { a + b = −1
**[ a = −7, b = 6 ]** (riquadrato, con una freccia dal sistema)

(La codifica di Ciao in 2, −7, 8, −2 non è quella di prima, 3, 9, 1, 15: non è spiegata, sono numeri dati.)

[a voce] (≈ 81:52) Sul nome, «Reed-Solomon, credo sia Solomon».
[a voce] (≈ 84:12 – 84:53) Si leggono i numeri come coefficienti di un polinomio, e si chiede che p(1) e p(2) siano zero, cioè che abbia come radici 1 e 2.
[a voce] (≈ 87:16) Il mittente aggiunge a e b e risolve il sistema. Nella trascrizione si legge «a = −7 e b = 7», ma alla lavagna è b = 6, che è il valore giusto: non si può dire se sia un lapsus o un errore della trascrizione.

## Il ricevente: rilevare l'errore (87:30 – 92:30)
Figura: l'omino con **2, −7, 8, −2** e il computer ⇝ [ 2, −7, 8, −2, −7, 6 ] ⇝ [ 2, −7, 8, −2, −7, 6 ] ⇝ secondo omino.

**Caso ①** ⟶ P(x) = 2x⁵ − 7x⁴ + 8x³ − 2x² − 7x + 6
P(1) = 0 ? ✓   P(2) = 0 ? ✓ ⟶ **Messaggio corretto**

**Caso ②** [ 2, −7, 8, −2, −7, 6 ] ⟶ [ **3**, −7, 8, −2, −7, 6 ] ⟶ P(1) = 0 ? ✗   P(2) = 0 ? ✗ **ERRORE**

[a voce] (≈ 90:05 – 90:42) Nel caso corretto le due condizioni valgono perché a e b sono stati scelti apposta; esse permettono al ricevente di capire che il messaggio è arrivato bene. È un modo facile di controllare.

## Correggere: si prova posizione per posizione (92:30 – 100:10)
**Q:** l'errore può essere nel 2° termine?
↪ 3, K, 8, −2, −7, 6 ⇝ TROVARE K t.c. p(1) = p(2) = 0
p(1) = 0 ⟶ { 3 + K + 8 − 2 − 7 + 6 = 0 ⇝ K = −8
p(2) = 0 ⟶ { K = 12
⟶ **No SOLUZIONI** ⟹ L'errore NON era in posiz. 2

**Q:** 1° termine? ⇝ ( K, −7, 8, −2, −7, 6 ) (a 99:30 −7, 6 è sottolineato da una parentesi)
p(1) = 0 ⟶ { K = 2
p(2) = 0 ⟶ { K = 2 (le due equazioni sono cerchiate insieme)
⟶ **Soluz. esiste** ↪ L'errore era in posiz. 1, e il messaggio era (2, −7, 8, −2)

**Errore non corretto:** alla lavagna per il 2° termine p(2) = 0 dà K = 12. Il valore giusto è K = −9 (vedi verifica). La conclusione non cambia: −8 ≠ −9, quindi non ci sono soluzioni.

(L'ultimo segno di «posiz. 2» assomiglia più a un punto interrogativo che a un 2: il 2 viene dal contesto.)

[a voce] (≈ 92:55 – 93:30) Supponiamo che l'errore sia il secondo: il messaggio corretto sarebbe 3, K, 8, −2, −7, 6, con K che non sappiamo cosa sia.
[a voce] (≈ 94:39 – 95:20) Allo stesso modo si ottiene un'altra condizione da p(2) = 0, «ma a calcolarla» (si perde). Questo sistema non ha soluzione, quindi non c'è modo di scegliere K, quindi l'errore non era nella seconda posizione.
[a voce] (≈ 96:29 – 97:02) Per il primo termine si ottiene K = 2 da entrambe; «qui salto i conti».
[a voce] (≈ 97:02 – 97:33) Il fatto che esista una soluzione dice due cose: conferma che l'errore era in quella posizione e dà il messaggio corretto, 2, −7, 8, −2. Gli ultimi termini non interessano: sono termini ausiliari per il controllo.
[a voce] (≈ 98:09 – 98:46) Aggiungere due termini permette di determinare la presenza di un errore e correggerlo. Mettendo quattro termini aggiunti si potrebbe (il seguito si perde).
[a voce] (≈ 99:18 – 99:54) Un QR code riesce a essere letto anche se fino a un quarto non è leggibile, grazie a questo algoritmo.

La lezione finisce qui (≈ 99:54, «ci vediamo mercoledì»). Il docente prova solo le posizioni 2 e 1: non controlla le altre.

[verifica] Con il messaggio ricevuto: p(1) = 1, p(2) = 32. Sostituendo K a turno in ogni posizione, si ottiene da p(1) = 0 e da p(2) = 0:
- posizione 1: K = 2 e K = 2 (compatibili);
- posizione 2: K = −8 e K = −9 (p(2) = 144 + 16K);
- posizione 3: K = 7 e K = 4;
- posizione 4: K = −3 e K = −10;
- posizione 5: K = −8 e K = −23;
- posizione 6: K = 5 e K = −26.

## Controllo dei conti con SymPy
Rifatti con SymPy (`rref`, `rank`, `nullspace`, `inv`, `solve`, operazioni elementari passo per passo). Tutti i risultati scritti alla lavagna sono corretti, tranne K = 12.
- Indipendenza: R₃ + R₁ dà ( 0 1 −1 ); R₃ + R₂ dà la riga nulla; soluzioni t(−1, 1, 1); v₁ − v₂ − v₃ = 0 e −v₁ + v₂ + v₃ = 0.
- Generatori: R₂ → 3R₂ − 2R₁ dà ( 0 13 23 | 3b − 2a ); rk A = 2.
- Coordinate: R₂ − R₁ e R₃ − R₂ danno le matrici della lavagna; 0·v₁ + 2·v₂ + 1·v₃ = (1, 2, 3); A⁻¹b = (0, 2, 1).
- Reed-Solomon: 64 − 112 + 64 − 8 = 8 e 2 − 7 + 8 − 2 = 1, quindi 2a + b = −8 e a + b = −1; a = −7, b = 6; p(1) = p(2) = 0 per il messaggio inviato.
- Correzione: tabella sopra; K = 2 è l'unica posizione compatibile.

Errori e correzioni del docente:
- λ₁ + λ₃ corretto in λ₁ + λ₂ (corretto da lui, 12:30 → 15:00).
- Componente centrale di v₁ nell'esempio delle basi, riscritta sopra una sbavatura (corretta da lui, ≈ 63:30).
- aₙv_k al posto di a_kv_k nel ripasso iniziale (non corretto; nella riga dei generatori è giusto).
- K = 12 al posto di K = −9 (non corretto; nessuna conseguenza sulla conclusione).
- vₘ, λₘ, bₘ accanto a aₙ, vₙ nella parte sulle basi: stesso numero con due lettere (non corretto; nessuna conseguenza perché A è quadrata).
- ( λ₁ ; λ₂ ; λ₃ ) = { … | t ∈ ℝ }: un vettore uguagliato a un insieme (non corretto; è una scrittura abbreviata).
- Pedice dell'ultima R in R₂ → R₂ − R₁ non distinguibile (nessuna conseguenza).

## Punti illeggibili
Nessuna formula è rimasta illeggibile: [illeggibile] non compare. Restano quattro letture incerte, segnalate sopra: il valore coperto dalla sbavatura nella componente centrale di v₁ (quello corretto è 1); la cifra di 15 nella seconda copia di CIAO; il segno finale di «posiz. 2»; il pedice di R₁ nella prima mossa dell'esempio delle basi. I tre zeri sotto la matrice 2 × 3 e il ⁎ sono tratti sottili ma si leggono a 59:30. Il proiettore copre a tratti il pannello in alto a sinistra: ogni parte coperta è stata letta in un altro fotogramma, dopo lo scorrimento del pannello.

## Note sulla trascrizione audio
La trascrizione (`algebra_L13_2025.txt`) contiene lunghi tratti allucinati (ripetizioni di «modulo», «di Gauss, sott», «mappa lineare», «mappurata», «di Laplace», «rilassi», «un'altra», «il termine di Sarrus»), dovuti ai suggerimenti lessicali dati a Whisper: non sono parole del docente. Non è stata fatta alcuna ritrascrizione. Sono persi, fra gli altri, i tratti (tempi approssimati) 00:36–01:09, 03:50–04:36, 06:14–07:20, 08:00–09:31, 12:30–14:33, 15:05–15:49, 16:40–17:40, 19:15–19:54, 24:47–26:05, 28:10–29:03, 29:33–32:30, 33:10–34:17, 35:40–37:07, 37:44–38:59, 40:23–41:50, 43:40–44:20, 50:40–52:16, 54:50–55:24, 58:01–60:23, 64:52–65:50, 68:50–70:21, 70:30–71:49, 76:20–77:50, 80:20–81:19, 82:42–84:12, 85:20–86:50, 87:30–90:05, 91:51–92:55, 93:30–94:30, 95:52–96:29, 98:46–99:18: in questi potrebbero esserci commenti a voce non riportati qui. Fidarsi della lavagna per le formule.
