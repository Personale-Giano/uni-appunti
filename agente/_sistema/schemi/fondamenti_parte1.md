# Memoria e circuiti

## Circuiti sequenziali e flip-flop {1, 5}
= Un **circuito sequenziale** ricorda il passato: la sua uscita dipende dagli ingressi di adesso e dallo **stato** interno.
- Nei **circuiti combinatori** conta solo l'ingresso del momento.
- La memoria nasce dal **ciclo di retroazione** (feedback): il segnale gira in tondo e tiene dentro un bit.
- Il **flip-flop** memorizza un bit: un impulso scrive 1, un altro scrive 0; con ingressi 00 conserva il valore.
- Si usa come scatola nera (**astrazione**), senza pensare alle porte logiche interne.
- È memoria **volatile**: se si stacca l'alimentazione il bit sparisce.
! Gli ingressi 11 (scrivi 1 e scrivi 0 insieme) sono un comando non lecito: il flip-flop diventa instabile.
> Vedi anche: Operazioni booleane e porte logiche, Memoria principale

## Operazioni booleane e porte logiche {5, 13}
= Operazioni sui valori 0 (falso) e 1 (vero), realizzate in hardware dalle **porte logiche**, in cui 0 e 1 sono due livelli di tensione.
![Le porte AND, OR, XOR e NOT con le tavole](figure/fond/ch05_porte_logiche.png)
- **AND**: 1 solo se entrambi gli ingressi sono 1 (interruttori in serie).
- **OR**: 1 se almeno un ingresso è 1 (interruttori in parallelo).
- **XOR**: 1 se gli ingressi sono diversi (gli interruttori della scala).
- **NOT**: un solo ingresso, lo inverte.
- Collegando porte si ottengono i flip-flop, quindi la memoria.
> Vedi anche: Circuiti sequenziali e flip-flop, Congiunzione disgiunzione e negazione

## Memoria principale {5}
= Una lunga fila di **celle** da un **byte** (8 bit), ciascuna con un **indirizzo** numerico che parte da 0.
![celle numerate e i bit della cella 3](figure/fond/ch05_celle_memoria.png)
- **MSB** (bit più significativo) è il bit a sinistra, quello che pesa di più; **LSB** è quello a destra.
- Due operazioni: **lettura** (guarda il contenuto senza cambiarlo) e **scrittura** (sovrascrive la cella).
- **RAM**: si accede a qualsiasi cella nello stesso tempo; la **DRAM** tiene i bit come cariche che si scaricano e richiede il **refresh**.
! In informatica 1 KB = 2^{10} = 1024 byte, non 1000 (e 1 MB = 1024 KB, 1 GB = 1024 MB).
> Vedi anche: Notazione esadecimale, Dischi magnetici

## Dischi magnetici {3}
= La **memoria di massa** (o secondaria) è non volatile, capiente ed economica; l'**HDD** ha piatti rotanti con accesso diretto ai dati.
![Tracce concentriche, settori e testina](figure/fond/ch03_hdd_tracce_settori.png)
- **Tracce** concentriche divise in **settori** (quantità fissa di dati); tracce alla stessa distanza su più piatti formano un **cilindro**.
- **Tempo di accesso** = **tempo di ricerca** (seek: la testina va sulla traccia) + **latenza di rotazione** (il settore arriva sotto la testina).
- **Zoned-bit recording**: le tracce esterne hanno più settori; la **velocità di trasferimento** dice quanto in fretta scorrono i dati trovati.
! Le tracce dell'HDD sono cerchi concentrici, non una spirale: la spirale è dei CD e DVD.
> Vedi anche: Dischi ottici e memorie flash, Memoria principale

## Dischi ottici e memorie flash {3}
= I **dischi ottici** si leggono con un laser; le **memorie flash** (SSD, schede SD) non hanno parti meccaniche.
![In un CD i dati stanno su un'unica traccia a spirale](figure/fond/ch03_cd_spirale.png)
- CD, DVD e Blu-ray hanno un'unica traccia a **spirale** dal centro verso l'esterno: ottimi per flussi continui, meno per l'accesso casuale.
- CD circa 600-700 MB; DVD alcuni GB (più strati); Blu-ray 25-50 GB.
- Flash: gli elettroni restano intrappolati per anni senza corrente; accesso quasi istantaneo, silenziose, resistenti agli urti.
- Si cancella a grandi blocchi e ogni scrittura consuma un po' le celle: il **wear-leveling** distribuisce le scritture su tutte le celle.
> Vedi anche: Dischi magnetici

# Basi e conversioni

## Notazione esadecimale {2, 4}
= La base 16 è un'abbreviazione dei bit: ogni cifra esadecimale sta per un blocco di 4 bit (2^{4} = 16 combinazioni).
![10110101 diviso in due blocchi da 4 bit](figure/fond/ch02_blocchi_esadecimale.png)
- Simboli 0-9 e A = 10, B = 11, C = 12, D = 13, E = 14, F = 15 (F = 1111, A = 1010).
- Binario → esadecimale: blocchi da 4 bit partendo da destra; esadecimale → binario: ogni cifra diventa 4 bit.
- Usi: colori RGB, indirizzi di memoria, prefisso `0x` (`0xFF` = 255).
- A 16 bit: 1010 0100 1100 1000 → A4C8.
! Dentro il calcolatore i dati restano sempre in binario: l'esadecimale è solo una scrittura comoda per chi programma.
> Vedi anche: Da binario a decimale, Immagini bitmap e vettoriali

## Da binario a decimale {7}
= Nella **notazione posizionale** in base 2 ogni posizione verso sinistra pesa il doppio: 1, 2, 4, 8, 16, 32…
- Il valore è la somma dei pesi delle posizioni che contengono 1.
- Il peso della cifra più a destra è 2^{0} = 1.
```
100101 = 32 + 4 + 1 = 37
   101 =  4 + 1     = 5
```
> Vedi anche: Da decimale a binario, Punto radice

## Da decimale a binario {7}
= **Divisioni successive** per 2: si annotano i resti finché il quoziente diventa 0, poi si leggono dal basso verso l'alto.
![13 diventa 1101](figure/fond/ch07_divisioni_successive.png)
- Il primo resto è l'LSB, l'ultimo è l'MSB.
- I resti possono essere solo 0 o 1.
! Leggere i resti nell'ordine in cui escono dà il numero al contrario: si leggono dall'ultimo al primo.
> Vedi anche: Da binario a decimale

## Addizione binaria {7}
= Si somma colonna per colonna da destra, come in decimale, con quattro casi e il riporto.
![11010 + 11011 = 110101 con i riporti](figure/fond/ch07_somma_binaria.png)
- 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1.
- 1 + 1 = 10: scrivo 0 e riporto 1.
- 1 + 1 + 1 (con il riporto) = 11: scrivo 1 e riporto 1.
- Controllo: 26 + 27 = 53.
> Vedi anche: Somma e overflow in complemento a due

## Punto radice {7}
= Il **punto radice** è la virgola del binario: a destra ci sono le potenze negative di 2.
- Pesi dopo il punto: 2^{-1} = 1/2, 2^{-2} = 1/4, 2^{-3} = 1/8…
- Per sommare numeri con il punto si incolonnano i punti radice.
```
101.101 = 4 + 1 + 1/2 + 1/8 = 5 5/8 = 5,625
```
> Vedi anche: Virgola mobile a 8 bit, Da binario a decimale

# Interi e complemento a due

## Complemento a due {8}
= Rappresentazione degli interi con segno su un numero **fisso** di bit; il bit di sinistra è il **bit di segno** (0 non negativo, 1 negativo).
![I 16 valori a 4 bit sul cerchio](figure/fond/ch08_complemento_a_due.png)
- A 4 bit: da 0000 (0) a 0111 (+7); 1111 è −1 e si scende fino a 1000 = −8.
- Con n bit l'intervallo è da −2^{n−1} a +2^{n−1} − 1: asimmetrico, perché lo zero sta tra i non negativi.
- Vantaggio: somma e sottrazione usano un solo circuito di addizione.
! A 4 bit +8 non esiste: il massimo è +7, mentre il minimo è −8.
> Vedi anche: Copia e complementa, Somma e overflow in complemento a due

## Copia e complementa {8}
= Per cambiare segno: da destra si copiano i bit fino al primo 1 compreso, poi si invertono tutti gli altri.
```
+6 = 0110
     ..10   copio fino al primo 1
     10..   inverto il resto
−6 = 1010
```
- Vale nei due versi: da positivo a negativo e da negativo a positivo.
- Esempio: +5 = 0101 diventa −5 = 1011.
> Vedi anche: Complemento a due

## Somma e overflow in complemento a due {8}
= Si somma come in binario puro tenendo la lunghezza fissa; A − B diventa A + (−B).
```
 7 − 5:  0111 + 1011 = 1 0010 → 0010 = +2
 5 + 4:  0101 + 0100 = 1001   → −7 (overflow)
```
- Il riporto che esce dalla colonna di sinistra si ignora.
- **Overflow**: il risultato non sta nei bit.
- Si riconosce dal segno: due positivi danno un negativo, oppure due negativi danno un positivo.
- La somma di due numeri di segno opposto non va mai in overflow.
! Il riporto che si butta via non è overflow: in 7 − 5 c'è un riporto ma il risultato +2 è giusto.
> Vedi anche: Copia e complementa, Addizione binaria

## Notazione in eccesso {8, 9}
= Si elencano le combinazioni in ordine crescente e lo zero è la prima che inizia con 1; sopra ci sono i positivi, sotto i negativi.
- A 4 bit lo zero è 1000 (che in binario puro vale 8): **Excess-8**. A 3 bit lo zero è 100: **Excess-4**.
- Valore vero = valore in binario puro − eccesso: in Excess-8, 1011 vale 11 − 8 = 3.
- Si usa per l'esponente della virgola mobile.
> Vedi anche: Virgola mobile a 8 bit, Complemento a due

# Virgola mobile

## Virgola mobile a 8 bit {9}
= La **virgola mobile** è la notazione scientifica in binario: si salvano le cifre significative e la posizione del punto radice.
- Modello del corso su un byte: 1 bit di **segno**, 3 bit di **esponente** in Excess-4, 4 bit di **mantissa**.
- Il punto radice si intende all'estrema sinistra della mantissa; l'esponente dice di quante posizioni spostarlo.
```
0 110 1010   segno +, esponente 110 = 6 − 4 = 2
             .1010 × 2^2 = 10.10 = 2 1/2
```
> Vedi anche: Notazione in eccesso, Errore di troncamento

## Standard IEEE 754 {9}
= Gli standard dei calcolatori reali per la virgola mobile.
- **Singola precisione** (32 bit): 1 segno, 8 esponente (Excess-127), 23 mantissa; circa 7 cifre decimali, da 10^{−37} a 10^{38}.
- **Doppia precisione** (64 bit): 1 segno, 11 esponente (Excess-1023), 52 mantissa; circa 15 cifre decimali.
> Vedi anche: Virgola mobile a 8 bit

## Errore di troncamento {9}
= Se un numero richiede più cifre di quante ne stanno nella mantissa, quelle in eccesso vengono buttate (**errore di troncamento** o di arrotondamento).
- 2 5/8 = 10.101 richiede 5 cifre: la mantissa tiene 1010 e si salva 01101010, cioè 2 1/2.
- Molte frazioni decimali sono periodiche in binario: 0,1 non si rappresenta esattamente.
- Per i soldi si lavora con interi in complemento a due (gli importi in centesimi).
> Vedi anche: Somma in virgola mobile, Virgola mobile a 8 bit

## Somma in virgola mobile {9}
= Per i troncamenti l'addizione in virgola mobile non è associativa: (A + B) + C può essere diverso da A + (B + C).
- Per allineare gli esponenti la mantissa del numero piccolo scorre a destra e le sue cifre possono uscire.
- 2 1/2 + 1/8 = 2 5/8 non entra in 4 cifre di mantissa: resta 2 1/2.
```
(2 1/2 + 1/8) + 1/8 = 2 1/2   (sbagliato)
2 1/2 + (1/8 + 1/8) = 2 3/4   (giusto)
```
! Sommare prima il numero grande e poi i piccoli fa sparire i piccoli.
> Vedi anche: Errore di troncamento

# Testo, immagini e suoni

## Codifica del testo {4, 6}
= Ogni simbolo diventa una sequenza di bit fissata da un codice: **ASCII**, estensioni ISO, **Unicode**.
- ASCII: 7 bit, 2^{7} = 128 simboli dell'inglese; poi portato a 8 bit con uno 0 iniziale.
- Le estensioni ISO aggiungono accenti e simboli europei, ma 256 combinazioni non bastano per cinese o giapponese né per testi multilingue.
- Unicode dà un codice a ogni simbolo del mondo (fino a 21 bit); con **UTF-8** l'ASCII resta in 1 byte, gli altri simboli usano da 16 a 32 bit.
- **File di testo puro**: solo caratteri; un documento di **word processing** contiene anche codici per la formattazione.
> Vedi anche: Numeri in binario o come testo

## Numeri in binario o come testo {6}
= Salvare i numeri come caratteri spreca spazio: per questo i numeri si memorizzano in notazione binaria.
- 25 come testo occupa 2 byte ('2' e '5'): con 16 bit di caratteri si arriva al massimo a 99.
- Gli stessi 16 bit in binario rappresentano ogni intero da 0 a 65 535.
> Vedi anche: Codifica del testo, Da binario a decimale

## Immagini bitmap e vettoriali {4, 6}
= Una **bitmap** divide l'immagine in **pixel** e salva il colore di ognuno; la **grafica vettoriale** salva le forme geometriche da disegnare.
- Bianco e nero: 1 bit per pixel (fax); scala di grigi: 1 byte, 256 sfumature.
- **RGB**: 1 byte per rosso, verde e blu, 3 byte (24 bit) per pixel, oltre 16,7 milioni di colori; si scrive con 6 cifre esadecimali.
- Alternativa: **luminanza** (quanto è chiaro) e due **crominanze** (la tinta), sfruttate dalla compressione.
- La vettoriale si ingrandisce senza sgranare: font TrueType e PostScript, disegni CAD.
! Ingrandire una bitmap la rende sgranata (zoom digitale): i pixel diventano visibili.
> Vedi anche: Notazione esadecimale, Formati multimediali compressi

## Campionamento audio e MIDI {6}
= Il **campionamento** misura l'ampiezza dell'onda sonora a intervalli regolari; il **MIDI** salva invece lo spartito.
![Misure dell'onda a intervalli costanti](figure/fond/ch06_campionamento.png)
- Telefono: 8 000 campioni al secondo (8 kHz).
- CD: 44 100 campioni al secondo, 16 bit per canale: un secondo stereo supera il milione di bit.
- MIDI: strumento, nota, intensità e durata; una nota di clarinetto di 2 s occupa 3 byte invece di circa 2,8 milioni di bit (2 s a 44,1 kHz, stereo).
! Il file MIDI è minuscolo, ma il suono finale dipende dal sintetizzatore che lo suona.
> Vedi anche: Formati multimediali compressi

# Compressione ed errori

## Compressione lossless e lossy {10}
= Comprimere vuol dire riscrivere un file in modo più corto, per occupare meno spazio e trasmetterlo più in fretta.
- **Lossless** (senza perdita): il file decompresso è identico all'originale; obbligatoria per testi, programmi, dati finanziari.
- **Lossy** (con perdita): butta via dettagli poco percepibili e comprime molto di più; va bene per immagini, audio, video.
- Le velocità di trasmissione si misurano in bps, Kbps, Mbps, Gbps.
! La perdita del lossy è irreversibile: quello che si è buttato non si recupera.
> Vedi anche: Tecniche di compressione generica

## Tecniche di compressione generica {10}
= Metodi che sfruttano ripetizioni, frequenze o somiglianze nei dati.
- **Run-length encoding**: una lunga serie di valori uguali diventa «quale valore e quante volte» (lossless).
- **Codici di Huffman**: codice breve ai simboli frequenti, lungo a quelli rari (in inglese 'e' corta, 'z' lunga).
- **Codifica relativa** (differenziale): si salvano solo le differenze dall'unità precedente, come tra fotogrammi.
- **Codifica a dizionario**: il messaggio diventa una sequenza di indici del dizionario.
- **LZW**: il dizionario parte dai simboli base e cresce durante la codifica; chi decomprime lo ricostruisce da solo, senza riceverlo.
```
xyx xyx xyx xyx   con x = 1, y = 2, spazio = 3
→ 121 3 poi xyx diventa la voce 4 → 121343434
```
> Vedi anche: Compressione lossless e lossy, Formati multimediali compressi

## Formati multimediali compressi {10}
= Standard specifici per immagini, video e audio.
- **GIF**: palette di al massimo 256 colori (24 bit ciascuno), 1 byte per pixel, più LZW; colore trasparente, animazioni semplici.
- **JPEG**: standard per le fotografie (baseline, lossy); primo passo: media della crominanza su quadrati 2×2, perché l'occhio è più sensibile alla luminanza.
- **TIFF**: foto ad alta fedeltà non compresse, con i metadati.
- **MPEG**: solo i fotogrammi chiave (I-frame) sono completi, gli altri sono differenze; **MP3** toglie i suoni coperti per mascheramento temporale e in frequenza.
! GIF è lossy sulle foto con sfumature fuori palette, ma lossless sulle grafiche semplici.
> Vedi anche: Tecniche di compressione generica, Immagini bitmap e vettoriali

## Bit di parità {11}
= Un bit in più scelto in modo che il numero di 1 sia sempre dispari (**parità dispari**) o sempre pari (**parità pari**); se all'arrivo il conto non torna, c'è un errore.
```
dati 1101 (tre 1)
parità dispari → aggiungo 0
parità pari    → aggiungo 1
```
- Le RAM ad alta affidabilità hanno celle da 9 bit: 8 di dati più la parità, controllata a ogni lettura.
- Per blocchi lunghi (settori dei dischi) si usano **checksum** e **CRC**.
! La parità non vede un numero pari di errori: con due bit invertiti il conteggio torna.
> Vedi anche: Distanza di Hamming

## Distanza di Hamming {11}
= La **distanza di Hamming** tra due stringhe di bit della stessa lunghezza è il numero di posizioni in cui differiscono.
![Con distanza minima 3 un errore si corregge e due si rilevano](figure/fond/ch11_distanza_hamming.png)
- 1011 e 1001 hanno distanza 1; 1011 e 0100 hanno distanza 4.
- I **codici correttori** scelgono parole legali molto distanti tra loro: con un errore la parola ricevuta resta più vicina all'originale.
- Distanza minima 3: rileva fino a 2 errori e ne corregge 1. Distanza minima 5: rileva fino a 4 errori e ne corregge 2.
! La parità rileva soltanto; un codice correttore capisce anche dove sta l'errore e lo ripara senza ritrasmissione.
> Vedi anche: Bit di parità

# Connettivi e tavole

## Proposizione {12, 20}
= Una **proposizione** è una frase vera oppure falsa, ma non entrambe; conta che il valore esista, anche se non lo conosciamo.
- Le **proposizioni atomiche** sono i mattoncini: interessa solo il loro **valore di verità** (detto anche **valore booleano**).
- Non sono proposizioni: domande, ordini (anche `x = 3` in un programma) e affermazioni con parametri come x + 4 = 6.
- Si indicano con **variabili proposizionali** p, q, r; si scrive p: 1 + 1 = 3 (falsa).
> Vedi anche: Congiunzione disgiunzione e negazione, Predicato e dominio

## Congiunzione disgiunzione e negazione {13}
= I **connettivi** combinano valori di verità; il valore della frase composta dipende solo da quelli delle parti.
![Tavole di and, or, xor, equivalenza e not](figure/fond/logica_connettivi.png)
- **Congiunzione** p ∧ q («p e q»): vera solo se entrambe sono vere.
- **Disgiunzione** p ∨ q («p o q»): **inclusiva**, falsa solo se entrambe sono false.
- **Negazione** ¬p («non p»): scambia vero e falso.
- Altre notazioni: ¬ come `!`, ∧ come `&&`, ∨ come `||`; nei linguaggi hanno lo stesso significato.
! In logica «or» è sempre inclusivo: con p e q entrambe vere, p ∨ q è vera.
> Vedi anche: Xor ed equivalenza, Precedenza dei connettivi

## Xor ed equivalenza {13, 18}
= L'**equivalenza** (test di uguaglianza, `==`) vale 1 quando i due valori sono uguali; lo **xor** (disgiunzione esclusiva, aut) è la sua negazione.
```
p q | equiv  xor
1 1 |   1     0
1 0 |   0     1
0 1 |   0     1
0 0 |   1     0
```
- Lo xor è vero quando esattamente una delle due è vera, non quando lo sono entrambe.
- L'equivalenza tra valori è il connettivo bicondizionale p ↔ q.
> Vedi anche: Bicondizionale, Congiunzione disgiunzione e negazione

## Precedenza dei connettivi {13, 16}
= Senza parentesi si valuta prima ¬, poi ∧, poi ∨ e per ultima l'implicazione →.
```
p = 0, q = 1, r = 0
¬p ∨ q ∧ r  =  (¬p) ∨ (q ∧ r)  =  1 ∨ 0  =  1
p ∨ q → ¬r  significa  (p ∨ q) → (¬r)
```
- Come in algebra la moltiplicazione viene prima della somma.
- Parentesi in più non sono mai sbagliate.
> Vedi anche: Tavola di verità, Implicazione materiale

## Tavola di verità {14, 15}
= Elenco di tutte le combinazioni dei valori delle proposizioni atomiche, con il valore della formula per ciascuna.
![La tavola di (p ∨ q) ∧ ¬p a passi](figure/fond/logica_formula.png)
- Con n proposizioni atomiche le righe sono 2^{n}: 2, 4, 8…
- Si calcola una colonna per ogni sottoformula.
- Serve a confrontare formule (e circuiti): (p ∨ q) ∧ ¬p ha la stessa tavola di ¬p ∧ q, più corta.
- Limite: le righe crescono in modo esponenziale; con 1000 proposizioni sono 2^{1000}, più di 10^{300}.
! Ogni caso va elencato una e una sola volta: un caso mancante rende sbagliato il confronto.
> Vedi anche: Formule equivalenti, Tautologia e contraddizione

# Equivalenze e leggi

## Formule equivalenti {15, 18}
= Due formule sono **equivalenti** (P ≡ Q) se hanno la stessa tavola di verità: si possono scambiare l'una con l'altra.
- P ≡ Q vale esattamente quando P ↔ Q è una tautologia.
```
p q | ¬p∨q  (p∧q)∨(¬p∨q)
1 1 |  1         1
1 0 |  0         0
0 1 |  1         1
0 0 |  1         1
```
- Quindi (p ∧ q) ∨ (¬p ∨ q) ≡ ¬p ∨ q: il pezzo p ∧ q non aggiunge casi.
! Prima di sostituire la condizione di un ciclo con una più leggibile bisogna essere sicuri che sia equivalente.
> Vedi anche: Tavola di verità, Leggi di De Morgan

## Tautologia e contraddizione {15, 16}
= Una **tautologia** è sempre vera (solo 1 nell'ultima colonna); una **contraddizione** è sempre falsa.
- La negazione di una tautologia è una contraddizione, e viceversa.
- **Terzo escluso**: p ∨ ¬p è una tautologia.
- ¬p ∨ q ∨ p e (p → q) ∨ (q → p) sono tautologie.
- (p ∨ q) ∧ ¬p non è né l'una né l'altra: è vera in una sola riga.
> Vedi anche: Formule equivalenti, Doppia negazione e proprietà della disgiunzione

## Leggi di De Morgan {15, 18}
= Negare una congiunzione dà la disgiunzione delle negazioni, e viceversa.
![Le colonne di ¬(p ∨ q) e ¬p ∧ ¬q coincidono](figure/fond/logica_demorgan.png)
- ¬(p ∧ q) ≡ ¬p ∨ ¬q.
- ¬(p ∨ q) ≡ ¬p ∧ ¬q.
- Sono **duali**: scambiando vero/falso e ∧/∨ (la negazione resta uguale) una diventa l'altra.
- In Java: `!(x >= 10 && x <= 20)` equivale a `x < 10 || x > 20`.
! Portando dentro la negazione si scambiano anche ∧ e ∨: ¬(p ∧ q) non è ¬p ∧ ¬q.
> Vedi anche: De Morgan per i quantificatori, Implicazione come disgiunzione

## Doppia negazione e proprietà della disgiunzione {15, 18}
= Leggi semplici che servono per riscrivere le formule passo per passo.
- **Doppia negazione**: ¬¬p ≡ p.
- **Commutatività**: p ∨ q ≡ q ∨ p.
- **Associatività**: (p ∨ q) ∨ r ≡ p ∨ (q ∨ r).
```
(¬p ∨ q) ∨ p ≡ (q ∨ ¬p) ∨ p   commutatività
             ≡ q ∨ (¬p ∨ p)   associatività
             ≡ q ∨ vero ≡ vero → tautologia
```
! Nel linguaggio comune «non è proprio falso» è più debole di «vero»; in logica ¬¬p è esattamente p.
> Vedi anche: Tautologia e contraddizione, Formule equivalenti

# Implicazione

## Implicazione materiale {16}
= p → q («p implica q») è falsa solo quando l'**ipotesi** p è vera e la **tesi** q è falsa.
![Unica riga falsa: ipotesi vera e tesi falsa](figure/fond/logica_implicazione.png)
- È **materiale**: guarda solo i valori di verità, non c'è nessuna relazione di causa.
- Con ipotesi falsa è **vera per difetto** (vacuously true), qualunque sia la tesi.
- Se la tesi è vera, l'implicazione è vera; vale 1 esattamente quando p ≤ q (test d'ordine).
! x > 0 → x · x > 0 è vera anche per x = 0 e x = −1: l'ipotesi è falsa, quindi l'implicazione è vera per difetto.
> Vedi anche: Conversa e contrapposta, Implicazione come disgiunzione

## Conversa e contrapposta {17}
= Data p → q, la **conversa** è q → p (ruoli scambiati), la **contrapposta** è ¬q → ¬p (scambiati e negati).
![p → q e ¬q → ¬p hanno la stessa tavola](figure/fond/logica_contrapposta.png)
- La contrapposta è equivalente all'implicazione: p → q ≡ ¬q → ¬p.
- La conversa non è equivalente: i valori cambiano quando p e q sono diversi.
- Con p: 1 > 2 (falsa) e q: 4 < 8 (vera), p → q è vera e q → p è falsa.
- Scambiare un'implicazione con la sua conversa è l'errore più frequente: vedi la scheda Affermazione della conclusione.
> Vedi anche: Condizione necessaria e sufficiente, Affermazione della conclusione

## Condizione necessaria e sufficiente {17}
= «A è **sufficiente** per B» significa A → B; «A è **necessaria** per B» significa B → A.
- Si legge p → q anche come: «q se p», «p solo se q», «p è sufficiente per q», «q è necessaria per p».
- Se fallisce una condizione necessaria, fallisce ciò di cui è condizione.
- Tour Eiffel → Francia: andare alla Tour Eiffel è sufficiente per visitare la Francia, visitare la Francia è necessario.
! «p solo se q» è p → q, non q → p: il «solo se» introduce la tesi.
> Vedi anche: Conversa e contrapposta, Bicondizionale

## Bicondizionale {18}
= p ↔ q («p se e solo se») è vera quando p e q hanno lo stesso valore: è il test di uguaglianza.
- p ↔ q ≡ (p → q) ∧ (q → p): due implicazioni opposte.
- p è condizione necessaria e sufficiente per q.
- Si prova con la tavola o con l'antisimmetria: p ≤ q e q ≤ p danno p = q.
> Vedi anche: Xor ed equivalenza, Formule equivalenti

## Implicazione come disgiunzione {18}
= p → q ≡ ¬p ∨ q: un'implicazione è vera se l'ipotesi è falsa oppure la tesi è vera.
```
¬(p → q) ≡ p ∧ ¬q            unico caso falso
p → q ≡ ¬¬(p → q) ≡ ¬(p ∧ ¬q) ≡ ¬p ∨ q   De Morgan + doppia negazione
```
- In Java l'implicazione non serve come operatore: si scrive `!p || q`.
- Bastano negazione e congiunzione per realizzare l'implicazione.
! La negazione di un'implicazione è una congiunzione: né p → ¬q né ¬p → ¬q, ma p ∧ ¬q.
> Vedi anche: Implicazione materiale, Leggi di De Morgan

# Regole di inferenza

## Argomento valido {19, 24}
= Un **argomento** è una serie di **ipotesi** (premesse) seguita da una **conclusione**; è **valido** se, ogni volta che le ipotesi sono tutte vere, è vera anche la conclusione.
- Si scrive p₁, p₂, …, p_{n} / ∴ q (∴ = «quindi»), oppure con ⊢ («allora si ricava»).
- Valido significa che (p₁ ∧ … ∧ p_{n}) → q non è mai falsa.
- Conta la forma, non il contenuto: due argomenti con la stessa forma sono validi o non validi insieme.
- Un argomento non valido si chiama **fallacia**.
! Valido non vuol dire che la conclusione è vera: dice solo che chi accetta le ipotesi deve accettare la conclusione.
> Vedi anche: Regole di inferenza, Verificare una regola

## Regole di inferenza {19}
= Argomenti validi già noti, da usare come mattoni in un ragionamento più lungo.
![Le sette regole: premesse sopra la riga, conclusione sotto](figure/fond/logica_regole_inferenza.png)
- **Modus ponens**: p → q, p ∴ q. **Modus tollens**: p → q, ¬q ∴ ¬p.
- **Addizione**: p ∴ p ∨ q. **Semplificazione**: p ∧ q ∴ p. **Congiunzione**: p, q ∴ p ∧ q.
- **Sillogismo ipotetico**: p → q, q → r ∴ p → r. **Sillogismo disgiuntivo**: p ∨ q, ¬p ∴ q.
```
p ∨ q, r, r → ¬q      (bug nel modulo 17 o 81)
r, r → ¬q  ∴ ¬q       modus ponens
p ∨ q, ¬q  ∴ p        sillogismo disgiuntivo
```
> Vedi anche: Argomento valido, Affermazione della conclusione

## Affermazione della conclusione {19, 24}
= La fallacia p → q, q ∴ p: è lo stesso errore di scambiare un'implicazione con la sua conversa.
![Modus ponens valido a sinistra, fallacia a destra](figure/fond/logica_argomenti_tavole.png)
- Controesempio: p falsa e q vera; le ipotesi sono vere e la conclusione è falsa.
- «Se piove, la strada è bagnata; la strada è bagnata; quindi piove»: no, può essere passata la spazzatrice.
! Somiglia al modus ponens ma parte dalla tesi: da q non si torna a p.
> Vedi anche: Conversa e contrapposta, Regole di inferenza

## Verificare una regola {24}
= Quattro strade: tavola di verità, dimostrazione, ricerca di un controesempio, riscrittura in una forma nota.
- **Tavola**: si guardano solo le righe con tutte le premesse vere; in ognuna la conclusione deve essere vera. Sicura, ma lunga.
- **Dimostrazione**: catena di modus ponens; per ricavare un'implicazione se ne assume l'ipotesi.
- **Riscrittura**: ¬r → ¬p, r ⊢ p diventa p → r, r ⊢ p, cioè l'affermazione della conclusione.
```
p → r, p → q ⊢ p → (r ∧ q)     valida
assumo p: r (MP), q (MP), quindi r ∧ q
```
! Le righe con almeno una premessa falsa non contano: lì la regola non promette niente.
> Vedi anche: Cercare un controesempio, Argomento valido

## Cercare un controesempio {24}
= Per una regola non valida basta una scelta di valori con premesse tutte vere e conclusione falsa.
![Tavole di p→r, r→q ⊢ q e di ¬r→¬p, r ⊢ p: la riga rossa è il controesempio](figure/fond/regole_tavole.png)
- Si ragiona all'indietro: si fissa la conclusione falsa e si sceglie il resto per rendere vere le premesse.
- La verità viaggia da sinistra a destra lungo le frecce, la falsità da destra a sinistra (contrapposta).
```
p → r, r → q ⊢ q      (manca la premessa p)
q = 0 → r = 0 → p = 0: premesse vere, conclusione falsa
p → (r ∨ q), r → ¬q ⊢ p → r
p = 1, r = 0, q = 1: premesse vere, conclusione falsa
```
! Trovato il candidato, va sempre ricontrollato sostituendo i valori in tutte le premesse.
> Vedi anche: Verificare una regola, Affermazione della conclusione

# Predicati e quantificatori

## Predicato e dominio {20}
= Un **predicato** (funzione proposizionale) P(x) diventa una proposizione per ogni x del **dominio del discorso** D.
- «n è dispari» non è una proposizione: P(1) è vera, P(2) è falsa (dominio ℤ⁺).
- **Variabile libera**: non ancora assegnata. **Variabile legata**: ha un valore o sta sotto un quantificatore.
- Un enunciato con variabili libere non ha valore di verità; senza variabili libere è una proposizione.
- x² − x − 6 = 0 su ℝ è vero solo per x = 3 e x = −2.
! Il dominio va sempre fissato: «π è un numero dispari» non ha senso, perché si parla di interi.
> Vedi anche: Proposizione, Quantificatore universale

## Quantificatore universale {21}
= ∀x P(x) («per ogni x») è vero se P(x) è vera per ogni x del dominio, falso se è falsa anche per un solo x.
![∀ e ∃ con tutti veri, alcuni veri, tutti falsi](figure/fond/logica_quantificatori_dominio.png)
- Un x che rende P(x) falsa è un **controesempio**; per smentire un ∀ ne basta uno.
- Per dimostrarlo si prende x **arbitrario** in D e si ragiona solo con il simbolo x.
- Il dominio conta: ∀x (x² ≥ 0) è vero su ℝ e falso su ℂ (x = i: x² = −1 non è ≥ 0; ≥ ha senso solo per i reali).
! Verificare P(x) per qualche valore particolare non dimostra ∀x P(x).
> Vedi anche: Quantificatore esistenziale, Quantificatori su un dominio finito

## Quantificatore esistenziale {22}
= ∃x P(x) («esiste x») è vero se P(x) è vera per almeno un x del dominio, falso se è falsa per ogni x.
- Per dimostrarlo basta un esempio: ∃x (x/(x² + 1) = 2/5) su ℝ è vero con x = 2.
- Non chiede unicità: va bene anche se P vale per molti x, o per tutti.
- Per smentirlo bisogna mostrare ∀x ¬P(x): per ogni x reale 1/(x² + 1) ≤ 1, quindi ∃x (1/(x² + 1) > 1) è falso.
! Un solo valore che rende P(x) falsa non smentisce un ∃.
> Vedi anche: Quantificatore universale, De Morgan per i quantificatori

## Quantificatori su un dominio finito {21, 22, 23}
= Su un dominio finito {d₁, …, d_{n}} un quantificatore si decide con un ciclo.
```
// ∀x P(x)                // ∃x P(x)
for i = 1 to n            for i = 1 to n
    if (¬P(d_i))              if (P(d_i))
        return false              return true
return true               return false
```
- ∀ si ferma al primo falso (controesempio); se è vero deve controllare tutti gli elementi.
- ∃ si ferma al primo vero; se è falso deve controllare tutti gli elementi.
! Per ∀: errore d'esame è un `else return true` o il `return true` dentro il ciclo; così si copia solo il valore di P(d₁). Il return finale va fuori dal for.
> Vedi anche: Quantificatore universale, Quantificatore esistenziale

## De Morgan per i quantificatori {22, 23}
= Portare la negazione dentro un quantificatore lo scambia con l'altro.
- ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).
- ∀ e ∃ sono **duali** come ∧ e ∨: su D = {1, 2, 3, 4}, ∀x P(x) è P(1) ∧ P(2) ∧ P(3) ∧ P(4) e ∃x P(x) è P(1) ∨ … ∨ P(4).
- «Non tutti», «non ogni» = ∃x ¬P(x); «nessuno», «non esiste alcun» = ∀x ¬P(x).
- P(n) = «n divide 10» su ℤ⁺: ∃n P(n) vero, ∀n P(n) falso (n = 3), ¬∀n P(n) vero.
! La negazione di «ogni x ha P» non è «nessun x ha P», ma «qualche x non ha P».
> Vedi anche: Leggi di De Morgan, Quantificatore esistenziale

## Quantificatori e insiemi annidati {23}
= Se gli x con P sono un sottoinsieme di quelli con Q, allora ∀x (P(x) → Q(x)) è vero.
![P dentro Q dentro D](figure/fond/insiemi_annidati.png)
- D: iscritti a un'università italiana; Q: iscritti a Torino; P: iscritti a Informatica a Torino.
- ∀x (P(x) → Q(x)) vero; ∀x (Q(x) → P(x)) falso (uno studente di Legge a Torino).
- ∀x (P(x) ∨ Q(x)) falso (uno studente di Milano); ∃x (P(x) ∧ Q(x)) e ∃x (P(x) ∨ Q(x)) veri.
! Il controesempio deve stare nel dominio: lo studente di Milano è in D, ed è lui a rendere falso ∀x (P(x) ∨ Q(x)).
> Vedi anche: Quantificatore universale, Implicazione materiale
