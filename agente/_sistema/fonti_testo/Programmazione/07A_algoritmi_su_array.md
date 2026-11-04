# 07A_algoritmi_su_array

<!-- pagina 1 -->
Programmazione I
Teoria
Elvio Amparore
A.A. 2026/27
Canale B
DIPARTIMENTO DI 
INFORMATICA
 
CORSO DI LAUREA 
TRIENNALE
Algoritmi su array
Ricerca, ﬁltro e ordinamento
1

<!-- pagina 2 -->
Algoritmi su array
• Esistono molti problemi tipici che coinvolgono dati 
sequenziali, come:
– cercare elementi
– ﬁltrare secondo un criterio
– ordinare le informazioni
• Questi algoritmi sono fondazionali nel senso che sono 
semplici da implementare, utilizzano i concetti visti ﬁnora 
(cicli, condizioni, variabili sentinella, ecc) e sono 
tipicamente alla base di algoritmi più complessi.
2

<!-- pagina 3 -->
Ricerca lineare
Ricerca, test di ipotesi per 
quantiﬁcazione esistenziale
3

<!-- pagina 4 -->
Ricerca lineare
• Immaginiamo uno sgabuzzino pieno di scatoloni numerati da 
0 a aLen-1
• Il nostro obiettivo è cercare se negli scatoloni abbiamo 
lasciato un oggetto (ad esempio un disco in vinile)
• Possiamo deﬁnire una strategia: aprire gli scatoloni uno per 
uno, in ordine, ﬁnché 
– troviamo il disco cercato
– oppure li abbiamo controllato tutti, e il disco non c’è
4

<!-- pagina 5 -->
Ricerca lineare
Ricerca lineare: deﬁnizione.
• Sia dato un array a di lunghezza aLen
• Si vuole scrivere un algoritmo che, dato un valore key, al 
termine dell’esecuzione abbia nella variabile i
– un indice valido, cioè i ∈ [0, aLen), tale che: a[i] == key
– oppure un valore sentinella i==aLen sse* key non è presente 
nell’array a
• Esempio:
int a[aLen] = {6, 12, 4, 9, -1};  // aLen==5
ricerca key==4 
→ termina con i==2   (indice valido)
ricerca key==20
→ termina con i==5   (valore sentinella)
5
* sse = se e solo se.

<!-- pagina 6 -->
Ricerca lineare
Per realizzare la ricerca servono due elementi fondamentali:
• memorizzazione del risultato: una variabile di controllo i, 
usato come indice per scorrere sequenzialmente l’array a; 
al termine, se la ricerca ha successo, i indica la posizione 
dell’elemento trovato
• logica della ricerca: una variabile sentinella booleana 
trovato, che regola l’esecuzione del ciclo e diventa true 
non appena key viene individuato
6

<!-- pagina 7 -->
Ricerca lineare
7
1.
bool trovato = false; // ipotesi iniziale: l'elemento cercato non esiste
2.
size_t i = 0;         // indice della scansione
3.
4.
while (i < aLen) {
5.
    // scorre gli elementi dell’array per trovare key
6.
    if (a[i] == key) {
7.
        trovato = true;
8.
        // trovato, l'ipotesi iniziale è sbagliata, mi fermo
9.
    }
10.
    else {
11.
        i++;
12.
    }
13.
}
Abbiamo memorizzato che l'elemento è stato 
trovato, ma possiamo fare di meglio: possiamo 
usare trovato per fermare il ciclo

<!-- pagina 8 -->
Ricerca lineare
8
1.
bool trovato = false; // ipotesi iniziale: l'elemento cercato non esiste
2.
size_t i = 0;         // indice della scansione
3.
4.
while (i < aLen && !trovato) {
5.
    // scorre gli elementi dell’array per trovare key
6.
    if (a[i] == key) {
7.
        trovato = true;
8.
        // trovato, l'ipotesi iniziale è sbagliata, mi fermo
9.
    }
10.
    else {
11.
        i++;
12.
    }
13.
}
14.
// al termine:
15.
//   - se trovato == true, i è l’indice della prima occorrenza
16.
//   - se trovato == false, i==aLen completato la scansione senza trovare occorrenze
i < aLen && !trovato
ﬁnché i è un indice valido, e non ho ancora 
trovato l’elemento, continua ad iterare.

<!-- pagina 9 -->
Ricerca lineare
• Formulazione logica della ricerca: 
∃i ∈ [0, aLen) : a[i]=key
“esiste almeno un indice i tale che a[i] è uguale a key”
• La ricerca lineare è la realizzazione algoritmica della 
quantiﬁcazione esistenziale su di un array
• Ogni volta che cerchiamo un elemento, stiamo 
rispondendo alla domanda: 
“Esiste un indice i che soddisfa la proprietà?”
9

<!-- pagina 10 -->
Quantificazione esistenziale - derivazione
Deriviamo l’algoritmo della quantiﬁcazione esistenziale come un test d’ipotesi
Formulazione: Dato un array a di lunghezza aLen e una condizione logica sugli 
elementi Cond(⋅), formuliamo due ipotesi
• Deﬁniamo un’ipotesi nulla (o iniziale) H₀: 
nessun elemento soddisfa Cond(⋅)
che possiamo tradurre in codice:  
exists ← false
• Deﬁniamo un’ipotesi alternativa (o di ricerca) H₁: 
esiste almeno un elemento che soddisfa Cond(⋅)
che possiamo tradurre in un algoritmo di scansione lineare che pone 
exists ← true  non appena trova un elemento che soddisfa Cond(⋅)
Le due ipotesi H₀ e H₁ si escludono a vicenda, quindi solo una può essere vera.
10

<!-- pagina 11 -->
Quantificazione esistenziale - derivazione
Deriviamo l’algoritmo della quantiﬁcazione esistenziale come un test d’ipotesi
Riscriviamo in formule (quantiﬁcate):
• Ipotesi nulla H₀: nessun elemento soddisfa Cond(⋅)
– H₀ : ∀i∈[0, aLen) :  ¬Cond(a[i])
• Ipotesi alternativa H₁: esiste almeno un elemento che soddisfa Cond(⋅)
– H₁ : ∃ i∈[0, aLen) : Cond(a[i])
11

<!-- pagina 12 -->
Quantificazione esistenziale - derivazione
12
Dove:
●AND aggregativo:  ⋀i∈[0,N)val[i] = val[0] ∧ val[1] ∧ … ∧ val[N-1]
●OR aggregativo:  
⋁i∈[0,N)val[i] = val[0] ∨ val[1] ∨ … ∨ val[N-1]
Quindi provare:  ∃ i∈[0, aLen) : Cond(a[i])
é equivalente a veriﬁcare: ⋁i∈[0,aLen)Cond(a[i]) =
Cond(a[0]) ∨ Cond(a[1]) ∨ … ∨ Cond(a[aLen-1])
Eliminazione della quantiﬁcazione. Il linguaggio di programmazione non ha 
un’operazione di quantiﬁcazione. Riscriviamo come operatori aggregativi
●Ipotesi nulla H₀: 
∀i∈[0, aLen) :  ¬Cond(a[i])   ⟺   ⋀i∈[0,aLen)¬Cond(a[i])
●Ipotesi alternativa H₁: 
∃ i∈[0, aLen) : Cond(a[i])   ⟺   ⋁i∈[0,aLen)Cond(a[i])

<!-- pagina 13 -->
Quantificazione esistenziale - derivazione
• Ipotesi nulla H₀: nessun elemento soddisfa Cond(⋅)
– H₀ : ∀i∈[0, aLen) :  ¬Cond(a[i]) ⟺ ⋀i∈[0,aLen)¬Cond(a[i])
• Ipotesi alternativa H₁: esiste almeno un elemento che soddisfa Cond(⋅)
– H₁ : ∃ i∈[0, aLen) : Cond(a[i]) ⟺ ⋁i∈[0,aLen)Cond(a[i])
13
Strategia di Decisione:
• Cerchiamo un controesempio ad H₀, che rende vera H₁. 
• Cerchiamo per scansione lineare sull’array a: non appena troviamo un indice i 
t.c. Cond(a[i]), allora falsiﬁchiamo H₀ e concludiamo H₁: esiste ← true
• Accetta H₀ se dopo aver esaminato tutti gli elementi, nessuno veriﬁca 
Cond(a[i]) 
Ipotesi iniziale (da falsiﬁcare). Adottiamo H₀ come ipotesi iniziale
esiste ← false
cioè assumiamo  ⋀i∈[0,aLen)¬Cond(a[i])

<!-- pagina 14 -->
Derivazione dell’algoritmo dalla forma matematica
14
1.
bool esiste = false;    // ipotesi iniziale: H0 (nessun elemento soddisfa Cond)
2.
size_t i = 0;
3.
4.
while (i < aLen) { // continua finché restano elementi
5.
    esiste = esiste || Cond(a[i]);   // realizza ⋁i∈[0,aLen)Cond(a[i])
6.
    i++;
7.
}
8.
// Stato finale:
9.
// - esiste == true  ⇒ H0 falsificata, H1 vera;
10.
// - esiste == false ⇒ nessun controesempio trovato nell’intero
11.
//                      dominio [0, aLen); quindi accetto H0
Questa forma è corretta ma non è ottimale: eseguiamo tutta la scansione 
dell’array, anche se potremmo fermarci non appena esiste diventa true.
Derivazione dell’algoritmo dalla forma matematica. Scriviamo una prima 
versione che assume inizialmente H₀ e realizza la formula per H₁

<!-- pagina 15 -->
Quantificazione esistenziale - derivazione
Ipotesi:
H₀ : ∀i∈[0, aLen) :  ¬Cond(a[i]) ⟺ ⋀i∈[0,aLen)¬Cond(a[i])
H₁ : ∃ i∈[0, aLen) : Cond(a[i]) ⟺ ⋁i∈[0,aLen)Cond(a[i])
Osservazione. Non ci serve un OR logico su tutti i valori Cond(a[i])
Possiamo cortocircuitare la valutazione dell’OR, ed interrompere non appena 
troviamo un valore i tale che Cond(a[i]). Riscriviamo:
⋁i∈[0,aLen)Cond(a[i])   =   ⋁i∈[0,iMin]Cond(a[i])    
dove iMin = min{ i∈[0,aLen) | Cond(a[i]) } // iMin primo indice che soddisfa 
Cond(a[i])
Derivazione ottimizzata dell’algoritmo dalla forma matematica.
Possiamo terminare la scansione lineare non appena determiniamo il più piccolo 
indice iMin tale che ⋁i∈[0,iMin]Cond(a[i]), se tale indice esiste.
15

<!-- pagina 16 -->
Derivazione dell’algoritmo dalla forma matematica
16
1.
bool esiste = false;    // ipotesi iniziale: H0 (nessun elemento soddisfa Cond)
2.
size_t i = 0;
3.
4.
// continua finché H0 non è falsificata, o l’array è finito
5.
while (i < aLen && !esiste) { 
6.
    esiste = esiste || Cond(a[i]);
7.
    if (!esiste)
8.
        i++;
9.
}
10.
// Stato finale:
11.
// - esiste == true  ⇒ H0 falsificata, H1 vera;
12.
// - esiste == false ⇒ nessun controesempio trovato nell’intero
13.
//                      dominio [0, aLen); quindi accetto H0
In alternativa possiamo riscrivere la catena di 
OR con un semplice assegnamento.

<!-- pagina 17 -->
Derivazione dell’algoritmo dalla forma matematica
17
1.
bool esiste = false;    // ipotesi iniziale: H0 (nessun elemento soddisfa Cond)
2.
size_t i = 0;
3.
4.
// continua finché H0 non è falsificata, o l’array è finito
5.
while (i < aLen && !esiste) { 
6.
    if (Cond(a[i])) {   // usiamo un semplice assegnamento a true al posto dell’OR
7.
        esiste = true;  // controesempio trovato ⇒ rigetto H0 ⇒ accetto H1
8.
                        // inoltre i = min indice tale che Cond(a[i])
9.
    }
10.
    else {
11.
        i++;
12.
    }
13.
}
14.
// Stato finale:
15.
// - esiste == true  ⇒ H0 falsificata, H1 vera;
16.
//                      l'elemento a[i] è il primo che soddisfa Cond
17.
// - esiste == false ⇒ nessun controesempio trovato nell’intero
18.
//                      dominio [0, aLen); quindi accetto H0

<!-- pagina 18 -->
Esempio: quantificazione esistenziale
18
1.
bool esistePari = false;    // ipotesi iniziale: H0 (nessun elemento pari)
2.
size_t i = 0;
3.
4.
while (i < aLen && !esistePari) {
5.
    if (a[i] % 2 == 0) {
6.
        esistePari = true;  // controesempio trovato: a[i] è pari
7.
    }
8.
    else {
9.
        i++;
10.
    }
11.
}
12.
// Stato finale:
13.
// - esistePari == true  ⇒ l'elemento a[i] è il primo elemento pari
14.
// - esistePari == false ⇒ non ci sono elementi pari nell’array
Esempio: esiste un elemento pari nell’array

<!-- pagina 19 -->
Specifica, ragionamento, strategia, codice
La ricerca lineare ci offre un esempio 
importante:
• il codice di per sé è breve
• ma contiene implicitamente un intero 
ragionamento logico, che realizza una 
strategia, la quale non è scritta 
esplicitamente nel codice
19
bool esiste = false;
size_t i = 0;
while (i < aLen && !esiste) {
    if (Cond(a[i])) {
        esiste = true;
    }
    else { i++; }
}
• Il codice mostra solo la dinamica operativa: come cambiano le 
variabili i ed esiste
• Ma non esplicita perché questo procedimento funziona, quali ipotesi 
lo rendono corretto, quali invarianti lo governano, né che cosa 
signiﬁchi funzionare correttamente

<!-- pagina 20 -->
20
Determinare se esiste un elemento che 
soddisfa Cond in a[0, aLen)
Speciﬁca: cosa deve fare il programma?
Inizialmente assumo che non ci sia.
Poi scansiono gli elementi uno ad uno ﬁno a 
trovarne uno che soddisfa Cond
Strategia/Algoritmo: come raggiungere 
l’obiettivo.
Imposto esiste a true sse 
∃ i∈[0, aLen) : Cond(a[i])
Quindi la variabile esiste assume il valore di 
una proposizione logica che equivale alla 
speciﬁca richiesta.
Ragionamento logico: perché la strategia 
è corretta?
bool esiste = false;
size_t i = 0;
while (i < aLen && !esiste) {
    if (Cond(a[i])) {
        esiste = true;
    }
    else { i++; }
}
Codice eseguibile: come si realizza 
operativamente.
Il codice è solo il livello più basso: la concretizzazione meccanica di un pensiero 
logico e di una speciﬁca. Il codice non ha gran parte delle giustiﬁcazioni razionali 
che rendono un algoritmo corretto.

<!-- pagina 21 -->
Proprietà ed invarianti
L’esempio ci mostra proprio come ogni iterazione di questo tipo 
implicitamente si basa su un invariante logico che non compare nel 
codice, ma che ne costituisce il fondamento razionale
Nella ricerca lineare vale1:
esiste == true  ⇒  ∃ j ∈ [0, i] : Cond(a[j])    per i ∈ [0, aLen)
• La correttezza parziale del programma deriva da questo 
invariante
• La terminazione e la correttezza totale completano il 
ragionamento
21
1 più avanti svilupperemo una forma più stretta di questo invariante.

<!-- pagina 22 -->
La “scomoda verità” del codice
• Il codice mostra come fare, non perché funziona
– Un programma è solo la forma operativa di un ragionamento logico
– Le ipotesi, le pre/post-condizioni e gli invarianti restano impliciti
– Senza il ragionamento sottostante, il codice è muto riguardo alla sua 
correttezza
• Commenti, assert e speciﬁche possono aiutare a rendere esplicito il 
ragionamento
• Programmare ≠ scrivere codice
Programmare = tradurre un pensiero in un processo eseguibile
• La logica, la strategia e la chiarezza del ragionamento sono 
l’elemento centrale. Il codice è solo la forma operativa ﬁnale
22

<!-- pagina 23 -->
Dalla ricerca di un elemento 
alla ricerca di una violazione
Veriﬁca di predicati, test di ipotesi 
per quantiﬁcazione universale, 
controesempi
23

<!-- pagina 24 -->
Verifica di proprietà
Vediamo un problema simile: vogliamo stabilire se tutti gli 
elementi di un array a soddisfano Cond(⋅)
• Proprietà:
∀ i ∈ [0, aLen) : Cond(a[i])
• Eliminazione della quantiﬁcazione via operatori 
aggregativi:
      ∀ i ∈ [0, aLen) : Cond(a[i]) ⟺ ⋀ i∈[0, aLen) Cond(a[i])
(AND “aggregativo” di tutti i valori booleani Cond(a[i]))
Deriviamo anche la veriﬁca di proprietà come test d’ipotesi
24

<!-- pagina 25 -->
Verifica di proprietà
Scegliamo le ipotesi in modo da poter falsiﬁcare rapidamente H₀ se 
compare un controesempio:
• H₀ (ipotesi iniziale): tutti soddisfano Cond
H₀: ∀ i∈[0, aLen) : Cond(a[i]) ⟺ ⋀ i∈[0, aLen) Cond(a[i])
(in codice: tutti ← true)
• H₁ (ipotesi di ricerca): esiste almeno un elemento che non 
soddisfa Cond
H₁: ∃ i∈[0, aLen) : ¬Cond(a[i])
(in codice: tutti ← false se troviamo un controesempio)
Strategia di decisione: Scansione lineare dell’array e cortocircuito: al 
primo indice i con !Cond(a[i]) falsiﬁchiamo H₀ ⇒ accettiamo H₁. Se la 
scansione termina senza violazioni, accettiamo H₀.
25

<!-- pagina 26 -->
Derivazione algoritmica test proprietà
Deriviamo il codice dalla formula con AND aggregativo
26
1.
bool tutti = true;               // H₀: tutti soddisfano Cond
2.
size_t i = 0;
3.
while (i < aLen) {
4.
    tutti = tutti && Cond(a[i]);  // realizza ⋀ i∈[0, aLen) Cond(a[i])
5.
    i++;
6.
}
7.
8.
// Finale:
9.
// - tutti == true  ⇒ H₀ vera (tutti soddisfano)
10.
// - tutti == false ⇒ esiste un controesempio (non tutti soddisfano)
Corretta ma non ottimale (scansiona sempre tutto l’array)

<!-- pagina 27 -->
Derivazione algoritmica test proprietà
Deriviamo il codice dalla formula con cortocircuito
27
1.
bool tutti = true;                // H₀: tutti soddisfano Cond
2.
size_t i = 0;
3.
while (i < aLen && tutti) {
4.
    if (!Cond(a[i])) {
5.
        // controesempio trovato ⇒ falsifica H₀ ⇒ accetta H₁
6.
        tutti = false;  // inoltre: i è il primo indice che NON verifica Cond
7.
    }
8.
    else { i++; }
9.
}
10.
11.
// Stato finale:
12.
// - tutti == true  && i == aLen  ⇒ H₀: ∀i Cond(a[i]) (ALL)
13.
// - tutti == false && 0 ≤ i < aLen ⇒ H₁: ∃i ¬Cond(a[i]);
14.
//                                        i è il primo controesempio
• Se tutti è true ⇒ nessun controesempio in [0, aLen); la proprietà è universale
• Se tutti è false ⇒ i è il primo indice tale che !Cond(a[i])

<!-- pagina 28 -->
Esempio quantificazione universale
Esempio: tutti i valori dell’array sono positivi
28
1.
bool tuttiPositivi = true; // ipotesi iniziale H0: tutti gli elementi sono positivi
2.
size_t i = 0;
3.
4.
// scorre gli elementi dell’array finché non trova un valore non positivo
5.
while (i < aLen && tuttiPositivi) {
6.
   if (a[i] <= 0) {
7.
       // basta un solo elemento ≤ 0 per falsificare l’ipotesi H0
8.
       tuttiPositivi = false;
9.
   }
10.
   else { i++; }
11.
}
12.
13.
// Al termine del ciclo:
14.
// - se tuttiPositivi == true  → H0: tutti gli elementi di a[0..aLen) sono > 0,
15.
//                                e i == aLen
16.
// - se tuttiPositivi == false → H1: esiste almeno un elemento ≤ 0; in tal caso
17.
//                                i è l’indice del primo elemento non positivo

<!-- pagina 29 -->
Casi limite delle quantificazioni
Array vuoti, domini vuoti e 
completezza delle funzioni
29

<!-- pagina 30 -->
Una funzione deve trattare tutti gli input
• Abbiamo deﬁnito una funzione che veriﬁca
∀ i ∈ [0, aLen) : Cond(a[i])
• Una funzione deve però fornire un risultato per tutti gli input che 
rispettano la sua speciﬁca, compresi i casi limite.
• Per aLen==N: Cond(a[0])∧Cond(a[1])∧⋯∧Cond(a[N−1])
• Per aLen==N-1:  una condizione in meno
…
• Per aLen==2: Cond(a[0])∧Cond(a[1])
• Per aLen==1: Cond(a[0])
• Per aLen==0: ????
Che cosa signiﬁca “tutti gli elementi soddisfano Cond” quando 
non ci sono elementi?
30

<!-- pagina 31 -->
Quantificazione universale sul dominio vuoto
• Per falsiﬁcare
∀ i ∈ [0, aLen) : Cond(a[i])
dobbiamo trovare almeno un controesempio nel dominio [0, aLen).
31
• Se aLen==0:
– il dominio [0, 0) è vuoto.
– non viene esaminato alcun elemento;
– non può esistere un controesempio.
∀ i ∈ [0, 0) : Cond(a[i]) == true
• Un enunciato universale sul dominio vuoto è vero, perché 
non esiste alcun possibile controesempio alla proprietà. 
Si dice vero per vacuità (vacuously true).

<!-- pagina 32 -->
Quantificazione universale sul dominio vuoto
Perché il ∀ sul dominio vuoto è vero?
Ci sono due modi equivalenti di leggerlo:
• una proprietà universale è falsa solo se esiste almeno un 
controesempio; nel dominio vuoto non può essercene nessuno;
• dire che tutti gli elementi soddisfano una condizione è comunque 
vero: non esiste alcun elemento che non la soddisﬁ (dato che 
l’insieme è vuoto).
32

<!-- pagina 33 -->
Quantificazione universale nel caso vacuo
Riprendiamo l’iterazione in tuttiPositivi:
33
1.
bool tuttiPositivi = true; // ipotesi iniziale H0: tutti gli elementi sono positivi
2.
size_t i = 0;
3.
4.
// scorre gli elementi dell’array finché non trova un valore non positivo
5.
while (i < aLen && tuttiPositivi) {
6.
   ... // nessuna iterazione
7.
}
8.
9.
// Al termine del ciclo:
10.
// - se tuttiPositivi == true  → H0: tutti gli elementi di a[0..aLen) sono > 0,
11.
//                                e i == aLen
12.
// - se tuttiPositivi == false → H1: esiste almeno un elemento ≤ 0; in tal caso
13.
//                                i è l’indice del primo elemento non positivo
Con aLen==0 non eseguiamo alcuna iterazione. Quindi tuttiPositivi parte 
true e rimane true, rispondendo correttamente al caso vacuo.
Quindi il caso vuoto non richiede una regola speciale: è già coperto dalla 
forma generale della quantiﬁcazione universale che abbiamo visto.

<!-- pagina 34 -->
Quantificazione esistenziale sul dominio vuoto
Vediamo il caso limite per la ricerca lineare / esistenziale:
Per
∃ i∈[0, aLen) : Cond(a[i]) 
serve trovare almeno un testimone che soddisﬁ Cond.
• Se aLen==0:
– il dominio [0, 0) è vuoto.
– non viene esaminato alcun elemento;
– non può esistere un testimone.
∃ i∈[0, aLen) : Cond(a[i]) == false
• Un enunciato esistenziale sul dominio vuoto è falso, perché non 
esiste alcun possibile testimone della proprietà. 
Si dice falso per assenza di testimoni.
34

<!-- pagina 35 -->
Esempio: quantificazione esistenziale
35
1.
bool esistePari = false;    // ipotesi iniziale: H0 (nessun elemento pari)
2.
size_t i = 0;
3.
4.
while (i < aLen && !esistePari) {
5.
    ... // nessuna iterazione
6.
}
7.
// Stato finale:
8.
// - esistePari == true  ⇒ l'elemento a[i] è il primo elemento pari
9.
// - esistePari == false ⇒ non ci sono elementi pari nell’array
Riprendiamo l’iterazione in esistePari:
Anche nel caso esistenziale con aLen==0 non eseguiamo alcuna 
iterazione. Quindi esistePari parte e rimane false, rispondendo 
correttamente.
Quindi il caso vuoto non richiede una regola speciale neanche per i test di 
ipotesi di tipo esistenziale.

<!-- pagina 36 -->
Quantificazione sul dominio vuoto
• Se il valore iniziale della variabile sentinella coincide con il risultato corretto 
sul dominio vuoto, allora per aLen == 0 il ciclo non esegue alcuna iterazione 
e la funzione calcola automaticamente la risposta corretta.
• Quando deﬁniamo una funzione dobbiamo sempre pensare come gestire i 
casi limite:
– In particolare, con array e intervalli, il dominio vuoto è un caso 
importante: una buona formulazione dell’algoritmo dovrebbe trattarlo 
naturalmente, senza richiedere eccezioni ad hoc.
36
quantiﬁcazione
dominio vuoto
perché
valore neutro / iniziale
∀ / AND
true
nessun controesempio
true
∃ / OR
false
nessun testimone
false

<!-- pagina 37 -->
Esercizi
tuttiPositivi: 
• prende in ingresso un array di interi a e la sua lunghezza aLen (se 
aLen>0 allora a!=NULL), più un puntatore size_t* ﬁrstBad (non NULL)
• Restituisce true se e solo se ∀i∈[0,aLen) a[i] > 0
• In uscita scrive in *ﬁrstBad l’indice del primo elemento che viola la 
proprietà (a[i] ≤ 0) oppure aLen se non vi sono violazioni
esistePari: 
• prende in ingresso un array di interi a e la sua lunghezza aLen (se 
aLen>0 allora a!=NULL), più un puntatore size_t* ﬁrstEven (non NULL)
• restituisce true se e solo se ∃i∈[0,aLen) con a[i] pari
• In uscita scrive in *ﬁrstEven l’indice del primo elemento pari trovato, 
oppure aLen se non esistono elementi pari
37

<!-- pagina 38 -->
38
1.
#include <assert.h>
2.
#include <stddef.h>
3.
#include <stdbool.h>
4.
#include <stdio.h>
5.
6.
bool tuttiPositivi(const int a[], size_t aLen, size_t *firstBad);
7.
8.
int main(void) {
9.
    // ---- Test tuttiPositivi ----
10.
    size_t idx;
11.
    // VUOTO: per convenzione ALL vero, indice sentinella
12.
    const int* v0 = NULL;
13.
    assert(tuttiPositivi(v0, 0, &idx) == true && idx == 0);
14.
    // TUTTI > 0
15.
    const int v1[] = {1, 2, 3};
16.
    assert(tuttiPositivi(v1, 3, &idx) == true && idx == 3);
17.
    // PRIMA VIOLAZIONE IN TESTA (<= 0)
18.
    const int v2[] = {0, 2, 3};
19.
    assert(tuttiPositivi(v2, 3, &idx) == false && idx == 0);
20.
    // VIOLAZIONE IN MEZZO
21.
    const int v3[] = {5, 4, -1, 7};
22.
    assert(tuttiPositivi(v3, 4, &idx) == false && idx == 2);
23.
    // VIOLAZIONE IN CODA
24.
    const int v4[] = {5, 4, 3, -9};
25.
    assert(tuttiPositivi(v4, 4, &idx) == false && idx == 3);
26.
}

<!-- pagina 39 -->
39
1.
#include <assert.h>
2.
#include <stddef.h>
3.
#include <stdbool.h>
4.
#include <stdio.h>
5.
6.
bool esistePari(const int a[], size_t aLen, size_t *firstEven);
7.
8.
int main(void) {
9.
    // ---- Test esistePari ----
10.
    size_t idx;
11.
    // VUOTO: ANY falso, indice sentinella
12.
    const int* w0 = NULL;
13.
    assert(esistePari(w0, 0, &idx) == false && idx == 0);
14.
    // NESSUN PARI
15.
    const int w1[] = {1, 3, 5, 7};
16.
    assert(esistePari(w1, 4, &idx) == false && idx == 4);
17.
    // PRIMO PARI IN TESTA
18.
    const int w2[] = {2, 3, 5};
19.
    assert(esistePari(w2, 3, &idx) == true && idx == 0);
20.
    // PARI IN MEZZO
21.
    const int w3[] = {1, 4, 5, 7};
22.
    assert(esistePari(w3, 4, &idx) == true && idx == 1);
23.
    // PARI IN CODA (inclusi negativi pari)
24.
    const int w4[] = {1, 3, -6};
25.
    assert(esistePari(w4, 3, &idx) == true && idx == 2);
26.
}

<!-- pagina 40 -->
Selezione
Estrazione condizionata di elementi, 
copia con ﬁltro, modello 
dimensione-capacità
40

<!-- pagina 41 -->
Selezione
Selezione*: deﬁnizione.
• Dato un array b di lunghezza bLen e una condizione logica sugli elementi 
Cond(⋅), la selezione copia in un altro array a tutti e soli gli elementi b[i] 
che soddisfano Cond(b[i]), mantenendo l’ordine degli elementi originali
a = [ b[i]  |  i∈[0,bLen) ∧ Cond(b[i]) ]
41
* Altri sinonimi: ﬁltraggio, estrazione condizionata, copia con ﬁltro.
18
30
9
a[0]
a[1]
a[2]
??
??
??
b[0]
b[1]
b[2]
18
30
9
a[0]
a[1]
a[2]
18
??
30
b[0]
b[1]
b[2]
NOTA: gli elementi 
selezionati e copiati da b 
ad a non condividono gli 
stessi indici

<!-- pagina 42 -->
Selezione
• Osservazioni:
– È necessario mantenere due indici:
○i ∈ [0, bLen) per eseguire la scansione lineare su b
○j per inserire in a gli elementi selezionati
– La dimensione ﬁnale di a è quindi uguale al numero di elementi di b 
che soddisfano Cond
42
* Altri sinonimi: ﬁltraggio, estrazione condizionata, copia con ﬁltro.
Selezione*: deﬁnizione.
• Dato un array b di lunghezza bLen e una condizione logica sugli elementi 
Cond(⋅), la selezione copia in un altro array a tutti e soli gli elementi b[i] 
che soddisfano Cond(b[i]), mantenendo l’ordine degli elementi originali
a = [ b[i]  |  i∈[0,bLen) ∧ Cond(b[i]) ]

<!-- pagina 43 -->
43
Consideriamo l’esempio nella memoria
• bLen=3, b inizializzato con { 18, 9, 30 }
• selezioniamo in b gli elementi maggiori o 
uguali a 18, e copiamo questi elementi in a
Codice
30
9
18
??
??
??
int b[bLen]
int a[bLen]
Indirizzi di memoria crescenti
word size
Selezione
18
30
9
a[0]
a[1]
a[2]
??
??
??
b[0]
b[1]
b[2]

<!-- pagina 44 -->
44
Consideriamo l’esempio nella memoria
• bLen=3, b inizializzato con { 18, 9, 30 }
• selezioniamo in b gli elementi maggiori o 
uguali a 18, e copiamo questi elementi in a
Selezione
18
30
9
a[0]
a[1]
a[2]
??
??
??
b[0]
b[1]
b[2]
18
30
9
a[0]
a[1]
a[2]
18
??
30
b[0]
b[1]
b[2]
Codice
30
9
18
??
30
18
int b[bLen]
int a[bLen]
Indirizzi di memoria crescenti
word size

<!-- pagina 45 -->
Dimensione e capacità
• Per la selezione abbiamo allocato a con capacità sufﬁciente a 
contenere ﬁno a bLen elementi; dopo la selezione solo una parte 
contiene elementi validi.
Separiamo quindi due concetti chiave:
• Capacità: numero massimo di elementi che l’array può contenere 
(3 nel precedente esempio)
• Dimensione effettiva: quanti elementi realmente validi sono stati 
copiati (nel nostro esempio j elementi alla ﬁne della scansione lineare)
Dopo la selezione:
– [0, j) intervallo semiaperto degli indici degli elementi validi in a
– [j, capacità) indici degli elementi non utilizzati
45

<!-- pagina 46 -->
6
Modello dimensione-capacità
46
Proprietà:
•
Dominio degli indici validi:  
[0, AMAX)
(non è cambiato)
•
Indici degli elementi inizializzati: 
[0, aLen)
(quindi per un indice i ad un elemento inizializzato vale: 
0 ≤ i < aLen
•
Indici degli elementi non-inizializzati (disponibili):
[aLen, AMAX)
Possiamo quindi alterare aLen per inserire o rimuovere elementi in fondo all’array, 
rispettando il vincolo:
0 ≤ aLen ≤ AMAX
17
21
-3
AMAX
aLen
0
1
2
8
19
3
4
7
??
5
??
??
7
8
??
NON VALIDO
9
10
Elementi:
Indici:
dimensione
aLen elementi 
(elementi inizializzati)
elementi 
non-inizializzati
(disponibili)
AMAX elementi 
(capacità massima)

<!-- pagina 47 -->
6
Modello dimensione-capacità
47
Possiamo quindi alterare aLen per inserire o rimuovere 
elementi in fondo all’array, rispettando il vincolo:
0 ≤ aLen ≤ AMAX
La lunghezza aLen può “scorrere” tutti i valori 
nell’intervallo [0, AMAX], si comporta come un cursore 
per il volume.
17
21
-3
AMAX
aLen
0
1
2
8
19
3
4
7
??
5
??
??
7
8
??
NON VALIDO
9
10
Elementi:
Indici:
dimensione
aLen elementi 
(elementi inizializzati)
elementi 
non-inizializzati
(disponibili)
AMAX elementi 
(capacità massima)

<!-- pagina 48 -->
Modello dimensione-capacità
48
Dichiarazione con capacità preﬁssata:
•
size_t aLen
dimensione
•
#deﬁne AMAX … capacità
•
int a[AMAX]
array
Dichiarazione con capacità variabile (VLA):
•
size_t aLen
dimensione
•
size_t aCap
capacità
•
int a[aCap]
array
6
17
21
-3
AMAX
aLen
0
1
2
8
19
3
4
7
??
5
??
??
7
8
??
NON VALIDO
9
10
Elementi:
Indici:
dimensione aLen 
elementi non-inizializzati
capacità AMAX

<!-- pagina 49 -->
Selezione con il modello dimensione/capacità
49
1.
// array b (sorgente)
2.
size_t bLen = ...
3.
int b[bLen] = ...
4.
// array a (destinazione)
5.
size_t aCap = bLen;
6.
int a[aCap];
7.
size_t aLen = 0; // gli elementi di a partono non-inizializzati
8.
9.
// SELEZIONE
10.
for (size_t i = 0; i < bLen && aLen < aCap; i++) {
11.
   if (Cond(b[i])) {   // seleziona da b
12.
       a[aLen] = b[i]; // copia da b ad a
13.
       aLen++;
14.
   }
15.
}
16.
// alla fine del ciclo aLen è il numero di elementi
17.
// selezionati in b e copiati in a

<!-- pagina 50 -->
Passaggio a funzione
Consideriamo il passaggio di un array con modello dimensione/capacità 
ad una funzione: quali parametri dobbiamo passare?
• Se la funzione chiamata non modiﬁca la dimensione:
const size_t aLen, int a[]
(come un array normale)
• Se la funzione altera la dimensione:
size_t *p_aLen, const size_t aCap, int a[]
Passando la lunghezza come puntatore p_aLen, la funzione chiamata 
può alterare la dimensione (rispettando 0 ≤ *p_aLen ≤ aCap) e 
“comunicare” attraverso un parametro puntatore (by-reference) la 
dimensione alla funzione chiamante. 
50

<!-- pagina 51 -->
Esercizio: selezione per intervalli
selectInRange:
• Dato un array sorgente b di lunghezza bLen, copiare in ordine in 
un array destinazione a tutti e soli gli elementi di b che 
appartengono all’intervallo chiuso [minVal, maxVal]. La 
dimensione ﬁnale dell’array a è il numero di elementi selezionati.
• Ritorna true se l’operazione è andata a buon ﬁne; false se aCap 
non è sufﬁciente a contenere tutte le occorrenze che soddisfano 
la condizione (in tal caso la funzione copia il più possibile ﬁno a 
saturare aCap, e segnala l’overﬂow logico col false).
bool selectInRange(size_t bLen, const int b[], 
                   size_t aCap, size_t *p_aLen, int a[], 
                   int minVal, int maxVal);
51

<!-- pagina 52 -->
Esercizio: selezione per intervalli
Traccia di implementazione:
• Inizializzare aLen = 0
• Per i = 0..bLen-1, se minVal ≤ b[i] ≤ maxVal e aLen < aCap, allora 
copia b[i] in a[aLen] e incrementa aLen
• A ﬁne scansione, assegna *p_aLen = aLen.
Per sapere se c’è stato overﬂow, si può usare una variabile sentinella 
overﬂow:
• se c’è spazio (aLen < aCap) copia da b ad a e incrementa aLen
• altrimenti mette overﬂow a true; usare i < bLen && !overﬂow 
come condizione di continuazione
52

<!-- pagina 53 -->
Esercizio: selezione per intervalli
Precondizioni
• Se bLen > 0 allora b != NULL
• a != NULL, p_aLen != NULL
• aCap è la capacità di a
• valore iniziale *p_aLen é irrilevante, impostato subito a 
zero
53

<!-- pagina 54 -->
Esercizio: selezione per intervalli
54
int main(void) {
     // Caso base: intervallo che non seleziona nulla
     const int b0[] = {5, 7, 9};
     int a0[3]; size_t a0Len;
     assert(selectInRange(3, b0, 3, &a0Len, a0, -2, 0) == true);
     assert(a0Len == 0);
     // Selezione piena, ordine preservato
     const int b1[] = {-3, 0, 2, 2, 8};
     int a1[5]; size_t a1Len;
     assert(selectInRange(5, b1, 5, &a1Len, a1, 0, 2) == true);
     // attesi: {0, 2, 2}
     assert(a1Len == 3 && a1[0]==0 && a1[1]==2 && a1[2]==2);
     // Overflow logico: aCap troppo piccolo
     const int b2[] = {1, 2, 3, 4};
     int a2[2]; size_t a2Len;
     bool ok = selectInRange(4, b2, 2, &a2Len, a2, 1, 4);
     // si copiano i primi due che soddisfano (ordine preservato), ma non tutti
     assert(ok == false);
     assert(a2Len == 2 && a2[0]==1 && a2[1]==2);
     // Array vuoto
     const int* b3 = NULL;
     int a3[1]; size_t a3Len=(size_t)-1; // verrà riscritto
     assert(selectInRange(0, b3, 1, &a3Len, a3, 10, 20) == true);
     assert(a3Len == 0);
}

<!-- pagina 55 -->
Test di ordinamento
Veriﬁca su coppie di elementi
55

<!-- pagina 56 -->
Verificare se un array è ordinato
• Consideriamo un array di interi:
a = [2,4,4,6,9]
• Vogliamo veriﬁcare se i suoi elementi sono disposti in ordine 
non decrescente:
2 ≤ 4 ≤ 4 ≤ 6 ≤ 9.
• Questa non è una proprietà che si può veriﬁcare prendendo 
singolarmente ciascun elemento:
L'ordinamento è una proprietà 
delle coppie di elementi adiacenti.
56

<!-- pagina 57 -->
Dagli indici degli elementi agli indici delle coppie
Finora abbiamo usato un indice per identiﬁcare un elemento:
i ∈ [0, aLen)   ⟷   a[i].
Per confrontare elementi adiacenti, usiamo convenzionalmente 
l'indice del secondo elemento della coppia:
i ∈ [1, aLen)   ⟷   (a[i-1], a[i]).
57
2
4
4
0
1
2
6
9
3
4
Elementi:
Indici elementi:
Indici coppie:
1
2
3
4
●[0, aLen) è lo spazio degli indici degli elementi.
●[1, aLen) è lo spazio degli indici delle coppie adiacenti.

<!-- pagina 58 -->
Quante coppie adiacenti?
Per N≥1 elementi abbiamo N-1 coppie adiacenti.
– 5 elementi → 4 coppie;
– 3 elementi → 2 coppie;
– 2 elementi → 1 coppia;
– 1 elemento → 0 coppie;
– 0 elementi → 0 coppie.
• Lo spazio degli indici delle coppie adiacenti i∈[1, aLen) è 
quindi coerente.
• Con N ≤ 1, non ci sono coppie.
• Non è un nuovo caso speciale: abbiamo già deﬁnito come 
si comporta un test d’ipotesi su un dominio vuoto.
58

<!-- pagina 59 -->
Ordinamento come proprietà universale
Diamo una formulazione precisa come test d’ipotesi.
• Un array è ordinato in senso non decrescente se tutte le 
coppie adiacenti sono nell'ordine corretto:
∀i∈[1, aLen) : a[i-1] ≤ a[i]
• Quindi il predicato sulle coppie è:
Cond(i) ≡ a[i-1] ≤ a[i].
• L'array non è ordinato se troviamo almeno un controesempio:
∃i∈[1, aLen) : a[i-1] > a[i].
59

<!-- pagina 60 -->
I casi limite vengono già dalla definizione
• Cosa succede con 0 o 1 elementi?
• Per aLen ≤ 1 non esiste alcuna coppia adiacente che 
possa violare l'ordinamento.
• Per la deﬁnizione di verità vacua, la proprietà ∀ è true
Un array vuoto, e un array con un solo elemento, 
sono ordinati.
• Il caso vacuo è quindi un caso limite che la deﬁnizione di 
ordinamento come proprietà ∀ tratta già correttamente, 
senza richiedere eccezioni particolari.
60

<!-- pagina 61 -->
Implementare il test di ordinamento
Implementiamo  ∀i∈[1, aLen) : Cond(i),   con: Cond(i) ≡ a[i−1]≤a[i].
61
1.
bool ordinatoNonDecr(size_t aLen, const int a[]) {
2.
    // All'inizio assumiamo che l'array sia ordinato.
3.
    bool ordinato = true;
4.
 
5.
    // i identifica la coppia adiacente (a[i - 1], a[i]).
6.
    size_t i = 1;
7.
8.
    // Verifica tutte le coppie, finché non trova un controesempio.
9.
    while (i < aLen && ordinato) {
10.
        if (a[i - 1] > a[i]) {
11.
            // La coppia viola l'ordinamento non decrescente.
12.
            ordinato = false;
13.
        } else {
14.
            // La coppia è ordinata: passa alla successiva.
15.
            i++;
16.
        }
17.
    }
18.
19.
    return ordinato;
20.
}

<!-- pagina 62 -->
Esecuzione test di ordinamento
Array ordinato
a = [2, 4, 4, 7]
ordinato = true
Scansione:
1. 2 ≤ 4 ✓
2. 4 ≤ 4 ✓
3. 4 ≤ 7 ✓
Non viene trovato alcun 
controesempio.
Risultato: ordinato == true
62
Array non ordinato
a = [2, 5, 3, 7]
ordinato = true
Scansione:
1. 2 ≤ 5 ✓
2. 5 ≤ 3 ×    pone:  ordinato = false
Trovato un controesempio, il ciclo 
termina
Risultato: ordinato == false

<!-- pagina 63 -->
La forma dell'intervallo conta
• L’intervallo i∈[1,aLen) si traduce direttamente in
63
1.
size_t i = 1;
2.
3.
while (i < aLen) {
4.
    ...
5.
    i++;
6.
}
1.
for (size_t i = 1; i < aLen; i++) {
2.
    ...
3.
}
e funziona naturalmente anche per aLen == 0 e aLen == 1.
NOTA: evitare invece una condizione come:  i <= aLen - 1
perché, essendo aLen di tipo size_t, quando aLen == 0 l'espressione aLen - 1 
va in wrap-around e produce un valore molto grande invece di -1.
La formulazione matematica con intervalli semiaperti porta quindi 
a una formulazione del codice semplice e robusta sui casi limite.

<!-- pagina 64 -->
Dal test al riordinamento
• Abbiamo imparato a riconoscere una violazione dell'ordinamento 
non decrescente. Ma ordinatoNonDecr si limita a rilevare il 
controesempio:
64
1.
if (a[i - 1] > a[i]) {
2.
     // La coppia viola l'ordinamento non decrescente.
3.
     ordinato = false;
4.
}
• Adesso sviluppiamo un’idea diversa: quando troviamo una coppia 
nell'ordine sbagliato, possiamo provare a correggerla scambiando i 
due elementi. 
• Questa è l'idea dell’algoritmo di ordinamento Bubble Sort.
– Il test di ordinamento ordinatoNonDecr usa il predicato locale a[i - 1] > a[i] 
per rilevare un controesempio.
– Il Bubble Sort usa lo stesso predicato locale, ma quando trova un 
controesempio prova a correggerlo scambiando i due elementi.

<!-- pagina 65 -->
Ordinamento di array
Algoritmo di ordinamento Bubble 
Sort (ordinamento a bolla)
65

<!-- pagina 66 -->
Bubble Sort
• Un algoritmo di ordinamento è una procedura che:
– prende in input un array di elementi appartenenti a un 
dominio ordinabile
– produce in output lo stesso array con gli elementi 
riorganizzati in un ordine preﬁssato (ad esempio crescente o 
decrescente)
• L’algoritmo bubble sort (ordinamento a bolla) è un 
algoritmo di ordinamento semplice e didattico, basato su 
confronti e scambi (swap) ripetuti tra coppie di elementi 
adiacenti di un array
66

<!-- pagina 67 -->
Definizione e obiettivi del bubble sort 
• Il bubble sort prende in input un array a di lunghezza aLen
• Manipola in-place l’array a (gli elementi di a vengono modiﬁcati 
tramite scambi, non si costruisce un altro array in cui copiare i dati)
• In uscita, gli elementi dell’array a sono ordinati.
Usiamo l’ordinamento non decrescente:
a[0] ≤ a[1] ≤ … ≤ a[aLen-1]
• Riprendiamo la proprietà di ordinamento appena usata in 
ordinatoNonDecr: tutte le coppie adiacenti dell'array sono ordinate 
(proprietà di ordine non decrescente dell’array):
∀i ∈ [1, aLen) : a[i-1] ≤ a[i]
67

<!-- pagina 68 -->
Strategia del Bubble Sort
• L’algoritmo bubble sort si svolge in fasi successive
• In ogni fase si esegue un ciclo di confronti e possibili scambi tra 
elementi adiacenti, che opera in questo modo:
– Per ciascun indice i ∈ [1, aLen)
• si confronta la coppia (a[i-1], a[i])
• se a[i-1] > a[i], i due elementi vengono scambiati (swap)
• Alla ﬁne di una fase:
– se è stato effettuato almeno uno scambio, abbiamo trovato e 
corretto almeno un controesempio; l’array è stato modiﬁcato e 
quindi si avvia una nuova fase
– se nessuno scambio è avvenuto, non abbiamo trovato alcun 
controesempio: tutte le coppie adiacenti soddisfano a[i-1] <= a[i], 
quindi l’array è ordinato e l’algoritmo termina
68

<!-- pagina 69 -->
69
6
2
-8
10
4
2
-8
6
4
10
-8
2
4
6
10
Prima fase
-8
2
6
4
10
-8
2
6
4
10
-8
2
4
6
10
-8
2
4
6
10
-8
2
4
6
10
-8
2
4
6
10
-8
2
4
6
10
-8
2
4
6
10
Seconda fase
Terza fase
2
6
-8
10
4
2
-8
6
10
4
2
-8
6
10
4
2
-8
6
4
10
ciclo di confronti e scambi
scambi effettuati ⇒ ripeti
scambi effettuati ⇒ ripeti
scambi non effettuati ⇒ 
array ordinato
Bubble sort: un esempio

<!-- pagina 70 -->
non fare nulla altrimenti
Test di confronto e scambio
• si confronta la coppia (a[i-1], a[i])
• se a[i-1] > a[i], i due elementi vengono scambiati (swap)
70
scambia se a[i-1] > a[i]
vali-1
vali
a[i-1]
a[i]
vali
vali-1
vali-1
vali
a[i-1]
a[i]
vali-1
vali
if (a[i-1] > a[i]) {
     swap(&a[i-1], &a[i]);
}
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

<!-- pagina 71 -->
Ciclo di confronti e possibili scambi
Per ciascun indice i ∈ [1, aLen) si esegue il 
test di confronto e possibile scambio. 
Memorizziamo se sono stati effettuati 
scambi, per decidere se effettuare una 
nuova fase.
71
Fase:
ciclo di confronti e scambi
ordinato = true; // ipotesi: nessun controesempio
// ciclo di confronti e scambi
for (size_t i = 1; i < aLen; i++) {
    if (a[i-1] > a[i]) {
        // controesempio trovato: correggiamolo
        swap(&a[i-1], &a[i]);
        ordinato = false;
    }
}

<!-- pagina 72 -->
scambi NON effettuati 
⇒ termina
scambi effettuati 
⇒ ripeti nuova fase
Iterazione sulle fasi
•
Se durante una fase sono stati effettuati degli scambi, è stato trovato e corretto un 
controesempio: ripetiamo la scansione sul nuovo stato dell'array. ⇒ ripeti una 
nuova fase ﬁnchè l’array non risulta ordinato
•
Altrimenti, vale:
a[0] ≤ a[1] ≤ … ≤ a[aLen-1]
quindi l’array è ordinato in modo non decrescente.
72
Fase:
ciclo di confronti e 
scambi
Fase:
ciclo di confronti e 
scambi
bool ordinato = false;
while (!ordinato) {
    // inizio nuova fase
    ordinato = true;
    ciclo di confronti e scambi
    
    // se troviamo un 
    // controesempio è necessaria
    // un'altra fase
}
•
La variabile ordinato è una variabile sentinella per l’uscita anticipata (early 
termination). Senza dovremmo effettuare aLen-1 fasi.

<!-- pagina 73 -->
#include <stdio.h>
#include <stdbool.h>
// funzione di scambio con passaggio per puntatore
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}
73
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
                swap(&a[i-1], &a[i]);
                // trovato e corretto un controesempio
                // sarà necessaria una nuova fase
                ordinato = false;
            }
        }
    }
}
#define LEN 5
int main(void) {
    int v[LEN] = {6, 2, -8, 10, 4};
    bubbleSort(LEN, v);
    printf("Array ordinato:\n");
    for (size_t i = 0; i < LEN; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");
}

<!-- pagina 74 -->
Bubble sort
74
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
                swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
Codice
-8
2
6
int v[LEN]
word size
main
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

<!-- pagina 75 -->
Bubble sort
75
Codice
-8
2
6
int v[LEN]
word size
size_t aLen
true
main
address-of v
3
int a[]
bool ordinato
control data
bubble
Sort
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
▶       ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
                swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

<!-- pagina 76 -->
Bubble sort
76
Codice
-8
2
6
int v[LEN]
word size
size_t aLen
main
address-of v
3
int a[]
1
size_t i
control data
bubble
Sort
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
▶       for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
                swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}
true
bool ordinato

<!-- pagina 77 -->
Bubble sort
77
Codice
-8
2
6
int v[LEN]
word size
size_t aLen
main
address-of v
3
int a[]
1
size_t i
control data
bubble
Sort
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
▶           if (a[i-1] > a[i]) {
                swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}
true
bool ordinato

<!-- pagina 78 -->
Bubble sort
78
Codice
-8
2
6
int v[LEN]
word size
size_t aLen
main
address-of v
3
int a[]
1
size_t i
control data
bubble
Sort
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
▶               swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}
true
bool ordinato

<!-- pagina 79 -->
Bubble sort
79
Codice
-8
2
6
int v[LEN]
word size
size_t aLen
main
address-of v
3
int a[]
1
size_t i
control data
address-of a[0]
address-of a[1]
control data
6
int* x
int* y
int temp
bubble
Sort
swap
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
▶               swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
▶   int temp = *x;
    *x = *y;
    *y = temp;
}
true
bool ordinato

<!-- pagina 80 -->
Bubble sort
80
Codice
-8
2
6 2
int v[LEN]
word size
size_t aLen
main
address-of v
3
int a[]
1
size_t i
control data
address-of a[0]
address-of a[1]
control data
6
int* x
int* y
int temp
bubble
Sort
swap
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
▶               swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
    int temp = *x;
▶   *x = *y;
    *y = temp;
}
true
bool ordinato

<!-- pagina 81 -->
Bubble sort
81
Codice
-8
2 6
6 2
int v[LEN]
word size
size_t aLen
main
address-of v
3
int a[]
1
size_t i
control data
address-of a[0]
address-of a[1]
control data
6
int* x
int* y
int temp
bubble
Sort
swap
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
▶               swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
                ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
▶   *y = temp;
}
true
bool ordinato

<!-- pagina 82 -->
Bubble sort
82
Codice
-8
2 6
6 2
int v[LEN]
word size
size_t aLen
true false
main
address-of v
3
int a[]
bool ordinato
1
size_t i
control data
bubble
Sort
#define LEN 3
int main(void) {
    int v[LEN] = {6, 2, -8};
▶   bubbleSort(LEN, v);
    ...
}
void bubbleSort(const size_t aLen, int a[]) {
    bool ordinato = false;
    while (!ordinato) {
        ordinato = true; // nuova fase
        // ciclo di confronti e scambi
        for (size_t i = 1; i < aLen; i++) {
            if (a[i-1] > a[i]) {
                swap(&a[i-1], &a[i]);
                // trovata coppia non ordinata
▶               ordinato = false;
            }
        }
    }
}
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

<!-- pagina 83 -->
Formulazione del test d’ipotesi d’ordine
• Possiamo interpretare l’algoritmo bubble sort come la combinazione di due 
componenti:
– Il ciclo di confronti e possibili scambi tra coppie di elementi adiacenti
– Un test d’ipotesi che veriﬁca la proprietà di ordine dell’array
• (H₀) Ipotesi iniziale della fase:  
∀i∈[1, aLen) : a[i-1] ≤ a[i]
L’array è già ordinato in senso non decrescente
→ corrisponde all’inizializzazione:   ordinato←true
• (H₁) Ipotesi alternativa:
∃i∈[1, aLen) : ¬(a[i-1] ≤ a[i])
Esiste almeno una coppia adiacente non in ordine
→ determinata tramite la scansione lineare su tutte le coppie adiacenti
• Quando durante una fase avviene almeno uno scambio, è stato trovato un 
controesempio a H₀ e l’array è stato modiﬁcato: occorre quindi una nuova 
fase sul nuovo stato. Se invece nessuno scambio avviene, l'intera scansione 
non ha trovato controesempi e H₀ è veriﬁcata. L’algoritmo termina.
83

<!-- pagina 84 -->
Considerazioni ed esercizio
• Esercizio: dopo ogni fase, gli elementi più grandi si sono 
spostati verso destra. Tracciando l’ultima posizione di swap 
(new_last), sappiamo che oltre quel punto gli elementi sono 
già in ordine; quindi la fase successiva può limitarsi a 
confrontare solo ﬁno a last == new_last.
84
