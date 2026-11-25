# Array e puntatori

## Il nome dell'array come puntatore {25}
= Array e puntatore sono oggetti diversi, ma in un'espressione il **nome dell'array** viene convertito nel puntatore al suo primo elemento.
- `v` diventa un `int*` che punta a `v[0]`; `&v[i]` è l'indirizzo dell'elemento i
- **aritmetica dei puntatori**: `v[i]` equivale a `*(v + i)`
- `v + i` avanza di i · sizeof(tipo) byte, non di i byte
- `sizeof(v)` dà la dimensione dell'intero array: l'array resta un `int[5]`
```c
int v[5] = {10, 20, 30, 40, 50};
printf("%d\n", v[2]);     // 30
printf("%d\n", *(v+2));   // 30, equivalente
```
> Vedi anche: Puntatore, Array come parametro

## Variable Length Array (VLA) {25, 38, 41}
= Un **VLA** (dal C99) è un array nello stack la cui lunghezza si decide a runtime, per esempio leggendola in input.
- rispetto agli array statici cambia solo la dichiarazione
- una volta creato, la lunghezza non cambia più
- vive nello stack frame della funzione: sparisce al suo ritorno
```c
size_t len;
scanf("%zu", &len);
int v[len];    // lunghezza decisa a runtime
```
! Trabocchetto: un VLA non si può inizializzare con le graffe: va riempito con un ciclo.
> Vedi anche: Array statico, Puntatore appeso (dangling pointer)

## Errori con gli array {25}
= Gli array non si assegnano, non si copiano e non si confrontano direttamente, e il C non controlla gli indici.
- `b = a;` è un errore: un array non è assegnabile
- `a == b` compila ma confronta gli indirizzi, non gli elementi
- per copiare serve un ciclo che copia gli elementi uno a uno
- un indice fuori da [0, length) dà **comportamento indefinito**: risultati errati, memoria corrotta o crash
```c
int a[3] = {1, 2, 3};
int b[3];
for (size_t i = 0; i < 3; i++)
    b[i] = a[i];     // copia corretta
```
! Trabocchetto: `if (a == b)` non confronta gli elementi, ma i due indirizzi.

## Il valore come indice (frequenze) {lab 13}
= Per contare le frequenze di valori piccoli si usa il **valore stesso come indice** di un array di contatori.
- le risposte da 1 a 5 stelle vanno nelle caselle da 0 a 4: la risposta r incrementa la casella `r - 1`
- `int frequenze[5] = { 0 };` azzera tutto: i valori non elencati nella lista valgono 0
- un array non sa quanto è lungo: la dimensione sta in una `#define` o in una variabile da portarsi dietro
```c
int frequenze[5] = { 0 };
for (size_t i = 0; i < NUM_RISP; i++) {
    frequenze[risposte[i] - 1]++;
}
```

# Stringhe

## Stringa e terminatore {26, lab 14}
= In C una **stringa** è un array di `char` chiuso dal carattere `'\0'`, il **terminatore** (NUL).
![la stringa "ciao": 4 lettere, 5 caselle](figure/prog/stringa_terminatore.png)
- `"ciao"` occupa 5 `char`: le 4 lettere più `'\0'`
- `char txt[] = "ciao";` crea un array modificabile; il NUL lo aggiunge il compilatore
- `const char* txt = "ciao";` punta a un **letterale stringa**, che non si può modificare
- si scorre fino al terminatore, con un indice o con un puntatore che avanza
```c
char parola[] = "ciao";
for (size_t i = 0; parola[i] != '\0'; i++) {
    printf("%c\n", parola[i]);
}
```
! Trabocchetto: scrivendo `'\0'` a metà, la stringa finisce lì: i caratteri dopo restano in memoria ma non vengono più stampati.

## Leggere una stringa con scanf {26, lab 14}
= `%s` legge una **parola**: si ferma al primo spazio, tab o a capo.
- davanti all'array non si scrive `&`: il nome è già convertito in `char*`
- si limita sempre la lunghezza: `%19s` per un array di 20 `char`, così resta posto per `'\0'`
- per una frase con spazi si usa la **maschera di scansione** `" %49[^\n]"`, che legge fino all'a capo
```c
char nome[20];             // 19 caratteri + '\0'
scanf("%19s", nome);       // senza &
char frase[50];
scanf(" %49[^\n]", frase); // frase con spazi
```
! Trabocchetto: `scanf("%s", &nome)` è sbagliato: `&nome` ha tipo `char (*)[20]`, non `char*`.

## Errori comuni con le stringhe {26}
= Le funzioni sulle stringhe contano sul `'\0'`, e i letterali stringa non si modificano.
- senza terminatore `printf` con `%s` scorre fuori dall'array: comportamento indefinito
- `char nome[4] = {'A', 'n', 'n', 'a'};` è sbagliato: servono 5 caselle, oppure `char nome[] = "Anna";`
- modificare un letterale stringa è comportamento indefinito; un array di `char` invece si modifica
```c
char* s = "ciao";
s[0] = 'm';      // ERRORE: letterale non modificabile
char t[] = "ciao";
t[0] = 'm';      // ok: "miao"
```
! Trabocchetto: una parola di n lettere vuole un array di n + 1 `char`.

## Caratteri come numeri e ctype.h {lab 14, 26}
= Ogni `char` è un codice numerico **ASCII**; cifre e lettere sono in sequenza, quindi ci si può fare aritmetica.
- codici utili: `'\0'` = 0, `'\n'` = 10, spazio = 32, `'0'` = 48, `'A'` = 65, `'a'` = 97
- `cifra - '0'` dà il valore della cifra; `'A' + i` dà la lettera di posto i
- `<ctype.h>`: `isalpha`, `isdigit`, `isalnum`, `islower`, `isupper`, `isspace`, `ispunct`, `tolower`, `toupper`
- i test ritornano un valore diverso da zero per «vero»: si scrive `if (isalpha(ch))`
```c
char cifra = '7';
int num = cifra - '0';     // 7, cioè 55 - 48
char c = toupper('a');     // 'A'
```
! Trabocchetto: non confrontare il risultato di `isalpha` con `true`: non è detto che valga 1.

## Le funzioni di string.h {33, lab 16}
= `<string.h>` dichiara le funzioni sulle stringhe; il corso ne usa tre.
- `strlen(s)`: lunghezza senza `'\0'`, quindi `strlen("ciao")` vale 4
- `strcmp(s1, s2)`: negativo se s1 viene prima, 0 se uguali, positivo se viene dopo
- **ordine lessicografico**: si confrontano i caratteri uno a uno per codice ASCII, quindi `"Zeta"` viene prima di `"alfa"`
- `strncpy(dest, src, count)`: copia al più count caratteri; se src ne ha count o più, dest resta senza `'\0'`
```c
if (strcmp(s1, s2) == 0) {
    printf("uguali\n");
}
```
! Trabocchetto: due stringhe non si confrontano con `==`, che confronta gli indirizzi.

# Funzioni

## Funzione e prototipo {27, lab 15}
= Una **funzione** è un blocco di codice con un nome, che riceve **parametri**, esegue istruzioni e può restituire un **valore di ritorno**.
- **prototipo**: la prima riga seguita da `;`, annuncia nome, tipi dei parametri e tipo di ritorno
- **definizione**: il corpo con le istruzioni, deve rispettare il prototipo
- **chiamata**: usa la funzione passandole i valori effettivi
- progettarla vuol dire scegliere nome, parametri e tipo di ritorno (`void` se non restituisce nulla)
- a differenza della funzione matematica può avere effetti collaterali e rispondere diversamente con gli stessi argomenti
```c
float square(float x);        // prototipo
int main(void) {
    float r = square(3.14f);  // chiamata
}
float square(float x) {       // definizione
    return x * x;
}
```

## Le quattro forme di funzione {27}
= Combinando presenza o assenza di parametri e di valore di ritorno si hanno quattro forme.
- con ritorno e parametri: `int max(int a, int b)`
- con ritorno, senza parametri: `int leggiNumero(void)`
- senza ritorno, con parametri: `void stampaQuadrato(float x)`
- senza ritorno né parametri: `void saluto(void)`, per i messaggi di servizio
- il nome di una funzione è l'indirizzo della sua prima istruzione, nell'area codice
> Vedi anche: Funzione e prototipo

## Passaggio per valore {28}
= In C gli argomenti si passano sempre **per valore**: la funzione riceve una copia.
- **parametro formale**: la variabile scritta nella definizione (`x` in `int square(int x)`)
- **argomento** o parametro attuale: il valore passato nella chiamata (`5` in `square(5)`)
- gli argomenti vanno ai parametri in ordine: il primo al primo, il secondo al secondo
- modificare il parametro cambia solo la copia; per cambiare il chiamante serve un puntatore
```c
void incr(int x) { x++; }   // modifica solo la copia
int a = 1;
incr(a);                    // a vale ancora 1
```
! Trabocchetto: `max(10, 3.5)` con parametri `int` non dà errore: 3.5 viene troncato a 3 per conversione implicita.
> Vedi anche: Passaggio per riferimento simulato

## Return ed errori comuni con le funzioni {28}
= Una funzione non `void` deve arrivare a un `return` su ogni percorso; una funzione `void` può ometterlo.
- si restituisce al massimo un valore; per averne di più servono parametri puntatore
- buona pratica: un solo `return`, alla fine
- prototipo e definizione devono avere gli stessi tipi, e la chiamata il giusto numero di argomenti
- nei prototipi i nomi dei parametri sono facoltativi: `float potenza(float, int);`
```c
int square(int x) {
    x * x;        // ERRORE: manca return
}
```
! Trabocchetto: il `return` dimenticato di solito dà solo un warning: non va ignorato.
> Vedi anche: Parametri di uscita

## Divide et impera {29}
= Si scompone il problema in sottoproblemi più semplici, e ogni sottoproblema diventa una funzione.
- passi: individuare il problema, dividerlo, una funzione per pezzo, ricombinare
- benefici: leggibilità, riutilizzo, manutenzione, testabilità
- una funzione, un compito (**SRP**), con nomi chiari: verbi per le azioni
- si separano le funzioni di input, di calcolo e di output
- **top-down** parte dal `main()`, **bottom-up** dalle funzioni elementari
```c
int main(void) {
    float r = leggiRaggio();
    float c = circonferenza(r);
    float a = area(r);
    stampaRisultati(r, c, a);
}
```

# Stack frame e chiamate

## Stack frame {30}
= Lo **stack frame** è la porzione contigua di stack riservata a una funzione attiva: nasce con la chiamata e viene rilasciato al ritorno.
![main chiama sumSquares, che chiama due volte square](figure/prog/stack_evoluzione.png)
- lo stack cresce verso indirizzi decrescenti
- **SP** segna il limite corrente dello stack e si sposta quando si riserva o si libera spazio
- **FP** segna l'inizio del frame attivo e resta fermo per tutta la chiamata
- una sola funzione è attiva, quella in cima; le altre sono sospese sotto
- le due chiamate a square usano la stessa zona, una dopo l'altra
- nel dettaglio del modello il frame vero e proprio sono le sole locali tra FP e SP: vedi Record di attivazione
> Vedi anche: Record di attivazione, Stack con FP e SP

## Chiamata e ritorno: prologo ed epilogo {31}
= Una chiamata è una sequenza di passi: il **prologo** prepara il frame, l'**epilogo** ripristina lo stato del chiamante.
- chiamata: parametri e spazio per il ritorno sullo stack, si salva `next(PC)` e si salta alla funzione
- prologo: si salva il FP del chiamante, si pone FP = SP, si riservano le locali spostando SP
- ritorno: si scrive il valore, SP = FP, si ripristinano FP e PC, si tolgono i parametri
- quello che si salva all'andata si riprende al ritorno, in ordine inverso
- grazie agli offset da FP la funzione è **rientrante**: più attivazioni non si disturbano, e serve per la ricorsione

## Record di attivazione {31, 30}
= Il **record di attivazione** è l'insieme logico dei dati di una chiamata: parametri, locali, valore di ritorno e dati di controllo.
![sopra FP i dati messi dal chiamante, sotto le locali del chiamato](figure/prog/record_attivazione.png)
- rispetto a FP: parametri e valore di ritorno a offset positivi, locali a offset negativi
- dati di controllo: l'indirizzo di ritorno `next(PC)` e il FP del chiamante
- nel modello del corso lo **stack frame** è solo la parte delle locali, tra FP e SP
- esercizio d'esame: disegnare stack e registri subito prima del ritorno
! Trabocchetto: i parametri sono celle diverse dagli argomenti del chiamante: ne contengono solo le copie.

# Passaggio per riferimento

## Passaggio per riferimento simulato {32}
= In C il passaggio per riferimento non esiste: lo si **simula** passando l'indirizzo della variabile e dereferenziandolo nella funzione.
![a sinistra cambiano solo le copie, a destra i puntatori scrivono in x e y](figure/prog/scambio_valore_puntatori.png)
- anche l'indirizzo passa per copia, ma con lui si arriva alla cella vera
- le scritture restano dopo il ritorno, perché sono avvenute nel frame del chiamante
- è il motivo per cui si scrive `scanf("%d", &x)`
```c
void swap(int* pA, int* pB) {
    int tmp = *pA;
    *pA = *pB;
    *pB = tmp;
}
// chiamata: swap(&x, &y);
```
! Trabocchetto: `swapSbagliato(int a, int b)` scambia solo le copie: x e y restano come prima.
> Vedi anche: Passaggio per valore, Parametri di uscita, Scambio con variabile temporanea

## Parametri di uscita {32, 28, 37, 41, lab 15}
= Con `return` esce un solo valore; gli altri risultati si consegnano attraverso **parametri puntatore**.
- schema tipico: l'esito come `bool` con `return`, i dati attraverso i puntatori
- la funzione scrive nella variabile del chiamante con `*out = ...`
- anche un indice o un valore sentinella si comunica così, per esempio `*firstBad = aLen`
```c
bool statistiche_sequenza(double* media, double* varianza);
// nel chiamante:
double m, v;
bool ok = statistiche_sequenza(&m, &v);
```
! Trabocchetto: prestare alla funzione l'indirizzo di una variabile del chiamante va bene; restituire l'indirizzo di una locale no.

## Array come parametro {33, lab 16}
= Un array si passa con il nome: la funzione riceve il puntatore al primo elemento, **non la lunghezza**.
- come parametro, `int dati[]` e `int* dati` sono la stessa cosa
- per questo si passano due parametri: la lunghezza e l'array
- l'array non viene copiato: la funzione lavora sugli elementi originali
- le **stringhe** fanno eccezione: il `'\0'` segna la fine, la lunghezza non serve
```c
size_t conta_occorrenze(size_t len, const int a[], int n) {
    size_t conta = 0;
    for (size_t i = 0; i < len; i++)
        if (a[i] == n) conta++;
    return conta;
}
```
! Trabocchetto: dentro la funzione `sizeof(dati)` dà la dimensione di un puntatore, non dell'array.
> Vedi anche: Il nome dell'array come puntatore, Il qualificatore const

## Il qualificatore const {33}
= `const` dichiara un dato in **sola lettura**: il compilatore dà errore se lo si modifica.
- nei parametri scrive il **contratto** della funzione: cosa modifica e cosa no
- `const int dati[]` e `const char* s`: la funzione legge soltanto
- nei prototipi di `string.h` dice che l'unica stringa modificata è `dest` di `strncpy`
- passare un dato `const` a una funzione che lo vuole non `const` è un errore (gcc può dare solo un warning)
```c
void stampa(const char* s) {
    printf("%s\n", s);
}
```

# Asserzioni

## assert {34}
= Un'**asserzione** è un'espressione booleana che deve essere sempre vera se il programma è corretto; se è falsa il programma si ferma.
- `assert(expr);` da `<assert.h>`: se expr è falsa mostra l'espressione, il file e la linea
- si disattivano compilando con `-DNDEBUG`
- controllano le ipotesi del programmatore, non gli input dell'utente
- un input sbagliato si gestisce con un messaggio o ripetendo la lettura
! Trabocchetto: niente effetti collaterali dentro `assert`: con `-DNDEBUG` sparirebbero insieme all'asserzione.

## Precondizioni invarianti e postcondizioni {34}
= Gli usi tipici di `assert`: cosa si pretende all'ingresso, cosa resta vero a ogni giro, cosa si garantisce all'uscita.
- **precondizione**: vale all'ingresso, per esempio `assert(aLen == 0 || a != NULL);`
- **invariante di ciclo**: vale a ogni iterazione, per esempio `assert(i < aLen);`
- **postcondizione**: vale all'uscita, e può essere «forte», cioè dire tutto il risultato
- un'asserzione può anche legare tra loro più parametri
```c
int massimo(int a, int b) {
    int m = (a > b) ? a : b;
    assert(m >= a && m >= b);   // non è minore di nessuno
    assert(m == a || m == b);   // ed è uno dei due
    return m;
}
```

# Ricerca e quantificatori

## Ricerca lineare {35}
= La **ricerca lineare** guarda gli elementi uno alla volta: alla fine `i` è la posizione di `key`, oppure `aLen` (sentinella) se non c'è.
- la sentinella `trovato` sta nella condizione del ciclo
- `i++` sta nell'`else`: quando trova, i resta sull'elemento
- è la quantificazione esistenziale ∃i ∈ [0, aLen) : a[i] = key
```c
bool trovato = false;
size_t i = 0;
while (i < aLen && !trovato) {
    if (a[i] == key) trovato = true;
    else i++;
}
```
! Trabocchetto: se `trovato` non è nella condizione, dopo la scoperta i non avanza più e il ciclo non finisce.

## Quantificazione esistenziale {35, lab 14, lab 15}
= «Esiste un elemento che soddisfa Cond?» si risolve come **test d'ipotesi**: si parte da H₀ «nessuno» e si cerca un testimone.
- sentinella iniziale `esiste = false`
- condizione `i < aLen && !esiste`: ci si ferma al primo testimone
- equivale all'OR aggregativo Cond(a[0]) ∨ … ∨ Cond(a[aLen-1]), valutato con cortocircuito
- esempio: per n > 1, n è primo se non esiste un divisore d con 2 ≤ d < n
```c
bool esiste = false;
for (size_t i = 0; i < aLen && !esiste; i++) {
    if (Cond(a[i]))
        esiste = true;
}
```
! Trabocchetto: nel `for` dopo il corpo si esegue comunque `i++`, quindi l'elemento trovato è `a[i-1]`; se serve la posizione si usa il `while` con `i++` nell'`else`.
> Vedi anche: Quantificatori su una sequenza, Sentinelle e uscita dai cicli

## Quantificazione universale {36, lab 14}
= «Tutti gli elementi soddisfano Cond?» si verifica partendo da H₀ «tutti» e cercando un **controesempio**: ne basta uno.
- sentinella iniziale `tutti = true`
- condizione `i < aLen && tutti`: ci si ferma al primo controesempio
- equivale all'AND aggregativo Cond(a[0]) ∧ … ∧ Cond(a[aLen-1])
- è speculare all'esistenziale: cambiano il valore iniziale e il senso del test
```c
bool tutti = true;
size_t i = 0;
while (i < aLen && tutti) {
    if (a[i] <= 0) tutti = false;   // controesempio
    else i++;
}
```
> Vedi anche: Quantificazione esistenziale, Dominio vuoto, Quantificatori su una sequenza, Sentinelle e uscita dai cicli

## Invariante di ciclo {36}
= Un **invariante di ciclo** è una proprietà logica vera prima e dopo ogni iterazione: spiega perché il ciclo funziona.
- nella ricerca: esiste == true ⟹ ∃j ∈ [0, i] : Cond(a[j])
- dà la **correttezza parziale**; con la terminazione si arriva alla correttezza totale
- quattro livelli: specifica, strategia, ragionamento logico, codice
- il codice mostra come, non perché: commenti, `assert` e specifiche rendono esplicito il ragionamento

## Dominio vuoto {37}
= Con `aLen == 0` non ci sono elementi: il «per ogni» è **vero per vacuità**, l'«esiste» è **falso per assenza di testimoni**.
- ∀ e AND: vero sul vuoto, sentinella iniziale `true`
- ∃ e OR: falso sul vuoto, sentinella iniziale `false`
- se il valore iniziale coincide con la risposta sul vuoto, il ciclo non parte e la risposta è già giusta
- non serve un caso speciale: un buon algoritmo tratta il vuoto da solo

## size_t e wrap-around {39, 24, lab 15}
= `size_t` è **senza segno**: sotto lo zero non va a -1 ma riparte dal valore più grande (**wrap-around**).
- con `aLen == 0`, `aLen - 1` è un numero enorme: `i <= aLen - 1` legge fuori dall'array
- si scrive invece `i < aLen`, con l'intervallo semiaperto
- per contare all'indietro fino a 0 si usa `ptrdiff_t`, con segno, da `<stddef.h>` (formato `%td`)
```c
for (ptrdiff_t i = N - 1; i >= 0; i--) {
    printf("%d\n", a[i]);
}
```
! Trabocchetto: `for (size_t i = N - 1; i >= 0; i--)` non finisce mai, perché `i >= 0` è sempre vero.

# Selezione e ordinamento

## Selezione {38}
= La **selezione** (filtraggio) copia in un altro array tutti e soli gli elementi che soddisfano Cond, nell'ordine originale.
- due indici: `i` scorre la sorgente b, `aLen` è la prima posizione libera di a
- gli elementi cambiano indice: con b = {18, 9, 30} e Cond «≥ 18», il 30 sta in b[2] e finisce in a[1]
- alla fine `aLen` è il numero di elementi copiati
- se la capacità non basta si segnala un **overflow logico**, per esempio ritornando `false` (come in selectInRange, cap. 38)
```c
size_t aLen = 0;
for (size_t i = 0; i < bLen && aLen < aCap; i++) {
    if (Cond(b[i])) {
        a[aLen] = b[i];
        aLen++;
    }
}
```
> Vedi anche: Modello dimensione-capacità, Selezione con copia nello heap

## Modello dimensione-capacità {38}
= La **capacità** è quanti elementi l'array può contenere, la **dimensione** quanti ne contiene davvero adesso.
![capacità AMAX, dimensione aLen e posti liberi](figure/prog/dimensione_capacita.png)
- indici validi [0, AMAX), elementi inizializzati [0, aLen), posti liberi [aLen, AMAX)
- vincolo: 0 ≤ aLen ≤ AMAX
- si dichiara con `#define AMAX`, `int a[AMAX]` e `size_t aLen`, oppure come VLA con `size_t aCap`
- funzione che non cambia la dimensione: `const size_t aLen, int a[]`
- funzione che la cambia: `size_t *p_aLen, const size_t aCap, int a[]`

## Test di ordinamento {39}
= Un array è **ordinato non decrescente** se ogni coppia adiacente è in ordine: ∀i ∈ [1, aLen) : a[i-1] ≤ a[i].
![indici degli elementi e indici delle coppie](figure/prog/indici_coppie.png)
- è una proprietà delle **coppie**: l'indice i indica la coppia (a[i-1], a[i])
- N elementi hanno N-1 coppie; con aLen ≤ 1 l'array è ordinato per vacuità
- schema universale: `ordinato = true`, stop al primo `a[i-1] > a[i]`
```c
bool ordinato = true;
size_t i = 1;
while (i < aLen && ordinato) {
    if (a[i - 1] > a[i]) ordinato = false;
    else i++;
}
```
> Vedi anche: size_t e wrap-around, Bubble Sort

## Bubble Sort {40}
= Il **Bubble Sort** ordina **in-place** con fasi di confronti e scambi tra vicini, finché una fase non fa più scambi.
![le tre fasi del Bubble Sort su 6, 2, -8, 10, 4](figure/prog/bubble_fasi.png)
- in ogni fase, per i ∈ [1, aLen), se `a[i-1] > a[i]` i due si scambiano
- la sentinella `ordinato` dà l'**uscita anticipata**: fase senza scambi, array ordinato
- è un test d'ipotesi ripetuto: H₀ «già ordinato», ogni scambio corregge un controesempio
- i valori grandi «salgono» verso destra come bolle
```c
bool ordinato = false;
while (!ordinato) {
    ordinato = true;                    // nuova fase
    for (size_t i = 1; i < aLen; i++)
        if (a[i-1] > a[i]) { swap(&a[i-1], &a[i]); ordinato = false; }
}
```
> Vedi anche: Passaggio per riferimento simulato, Test di ordinamento

# Heap e memoria dinamica

## Puntatore appeso (dangling pointer) {41}
= Un **dangling pointer** contiene l'indirizzo di una memoria non più valida, per esempio di una locale di una funzione già ritornata.
![il VLA muore con lo stack frame: a in main punta a un'area che non esiste più](figure/prog/dangling_stack.png)
- le variabili locali sono **automatiche**: nascono e muoiono con il loro stack frame
- limiti dello stack: spazio di pochi megabyte e durata legata alla funzione
- leggerlo è comportamento indefinito: può perfino stampare i valori giusti per caso
- regola senza eccezioni: mai ritornare un array o un puntatore a una locale, VLA compresi
```c
int* leggiArraySbagliato(size_t* out_n) {
    size_t n;
    scanf("%zu", &n);
    int a[n];                  // VLA nello stack
    for (size_t i = 0; i < n; ++i) scanf("%d", &a[i]);
    *out_n = n;
    return a;                  // ERRORE: a muore al ritorno
}
```

## Segmenti della memoria {42, 44}
= Nel modello del corso la memoria ha quattro segmenti: codice, dati statici, **heap** e **stack**.
![i quattro segmenti: stack e heap crescono l'uno verso l'altro](figure/prog/segmenti_memoria.png)
- code segment: le istruzioni; data segment: le variabili globali e statiche
- heap: la **memoria dinamica**, cresce verso l'alto ed è gestita a mano
- stack: le variabili automatiche, cresce verso il basso
- nello heap vanno i dati di dimensione non nota a priori; nello stack le locali piccole, puntatori, indici e array di misura fissa

## malloc {42}
= `malloc(sz)`, da `<stdlib.h>`, riserva sz byte contigui nello heap e restituisce l'indirizzo del primo, oppure `NULL` se non c'è memoria.
- ritorna un `void*`: lo si assegna a un puntatore del tipo voluto, il cast non serve
- per un array di n interi: `malloc(n * sizeof(int))`
- i byte **non sono inizializzati**
- si controlla `NULL` prima di usare il blocco
```c
int* a = malloc(n * sizeof(int));
if (a == NULL) {
    printf("Memoria insufficiente\n");
}
```
! Trabocchetto: `malloc(n)` riserva n byte, non n interi.

## free {42}
= `free(ptr)` restituisce allo heap un blocco ottenuto da `malloc`; `free(NULL)` non fa nulla.
![malloc e free passo per passo: al passo 5 il nuovo blocco riusa il buco](figure/prog/heap_blocchi.png)
- ogni `malloc` deve avere la sua `free`
- dopo la `free` il puntatore è un dangling pointer: si azzera subito
- i blocchi si liberano in qualunque ordine, e nello heap restano buchi
- dove finisce un blocco lo decide `malloc`: la figura è solo un modello
```c
free(a);
a = NULL;
```

## Restituire un array dallo heap {43}
= Una funzione può restituire un array se lo alloca con `malloc`: il blocco nello heap sopravvive al ritorno.
![dopo il ritorno il frame non c'è più, il blocco nello heap sì](figure/prog/leggi_array_heap.png)
- la locale `a` è solo un puntatore e muore, ma il blocco resta
- sugli elementi si scrive sempre `a[i]`, come per un array
- il blocco vale fino alla `free`, in qualunque funzione ci si trovi
- chi riceve il puntatore deve chiamare `free` quando ha finito
```c
int* leggiArray(size_t* out_n) {
    size_t n;
    scanf("%zu", &n);
    int* a = malloc(n * sizeof(int));  // semplificato: qui andrebbe controllato a != NULL (cap. 43)
    for (size_t i = 0; i < n; i++) scanf("%d", &a[i]);
    *out_n = n;
    return a;     // ok: il blocco vive nello heap
}
```
> Vedi anche: Puntatore appeso (dangling pointer), Responsabilità della memoria

## Memory leak {44}
= Un **memory leak** è un blocco allocato e mai liberato, che nessun puntatore raggiunge più.
- capita uscendo da una funzione senza `free`: muore la locale con l'unica copia dell'indirizzo
- capita sovrascrivendo il puntatore prima della `free`
- non c'è crash, solo RAM che cresce; strumenti come Valgrind li trovano
```c
int* p = malloc(10 * sizeof(int));
p = malloc(20 * sizeof(int));  // LEAK: il primo blocco è perso
```
! Trabocchetto: il programma sembra funzionare: un leak non dà errori visibili.

## Errori con la memoria dinamica {44}
= Oltre ai leak ci sono altri errori tipici, spesso invisibili finché il programma non si rompe altrove.
- **uso dopo free**: leggere `*p` dopo `free(p)` è comportamento indefinito
- **doppia free**: crash o heap corrotto; con `p = NULL` la seconda `free` diventa innocua
- **assunzioni sugli indirizzi**: due `malloc` non danno blocchi contigui, e `p1[1]` su un blocco da un `int` è fuori dai limiti
- **memoria non inizializzata**: `malloc` non azzera, si scrive prima di leggere
- regola: ogni blocco si libera una volta sola, e poi non si tocca più
```c
free(p);
p = NULL;     // evita uso dopo free e doppia free
```
! Trabocchetto: azzerare p protegge solo p: altri puntatori allo stesso blocco restano appesi.

## Selezione con copia nello heap {45}
= Per allocare un risultato della misura esatta, la selezione si fa in tre fasi: **conta, alloca, copia**.
![i pari di 12, 1, 3, 4, 8: si contano, si alloca, si copiano](figure/prog/select_copy_fasi.png)
- fase 1: si contano i b[i] che soddisfano Cond (count)
- fase 2: `malloc(count * sizeof(int))`
- fase 3: seconda scansione di b, copia con l'indice j
- niente overflow logico, ma b si scorre due volte
- se count è 0 si ritorna `NULL` con lunghezza 0, e la `free(NULL)` finale resta corretta
> Vedi anche: Selezione, Responsabilità della memoria

## Responsabilità della memoria {45}
= **Ownership**: ogni blocco allocato deve avere un punto del programma responsabile di liberarlo.
- chi chiama `malloc` diventa responsabile del blocco
- può passare la responsabilità restituendo il puntatore, come fanno leggiArray e selectCopy verso main
- l'ultimo punto che usa il blocco chiama `free`
- nessun responsabile è un leak, due responsabili una doppia free
- la specifica deve dire chi libera: `strdup`, da `<string.h>`, copia una stringa nello heap e la libera il chiamante
```c
char* copy = strdup("Programmazione 1");  // 17 byte nello heap
assert(copy != NULL);
printf("%s\n", copy);
free(copy); copy = NULL;
```

# Matrici

## Matrice: dichiarazione e accesso {46}
= Una **matrice** è una tabella di valori dello stesso tipo, con righe e colonne; in C è un array a due dimensioni.
- si dichiara `int m[ROWS][COLS];` e si inizializza riga per riga: `{ {0,1,2}, {3,4,5} }`
- `m[i][j]`: riga i ∈ [0, ROWS), colonna j ∈ [0, COLS)
- per visitarla servono due cicli annidati: l'esterno sulle righe, l'interno sulle colonne
- l'a capo messo dopo il ciclo interno scatta una volta per riga
```c
int m[2][3] = { {0,1,2}, {3,4,5} };
for (size_t i = 0; i < 2; i++) {
    for (size_t j = 0; j < 3; j++)
        printf("%d ", m[i][j]);
    printf("\n");
}
```

## Matrice in memoria {46}
= In memoria le righe stanno una dopo l'altra (**row-major**): la matrice è appiattita in una fila.
![la matrice 2×3 come tabella e come fila in memoria](figure/prog/matrice_memoria.png)
- indirizzo di `m[i][j]` = base(m) + (i · COLS + j) × sizeof(T)
- esempio: `m[1][2]` sta a 0x3E8 + 5 × 4 = 0x3FC
- per il calcolo serve COLS, non ROWS
- il nome `m` si converte nel puntatore alla prima riga, `&m[0]`

## Passare una matrice a una funzione {47}
= Si passa il nome della matrice: la funzione riceve il puntatore alla prima riga e lavora sugli originali.
- `m` ha tipo `int [ROWS][COLS]`, convertibile in `int (*)[COLS]`; `m[i]` è una riga `int[COLS]`
- dimensioni fisse: `void fn(int m[ROWS][COLS]);`
- dimensioni variabili (C99): `void fn(size_t rows, size_t cols, int m[rows][cols]);`, con le dimensioni **prima** della matrice
- la prima dimensione si può omettere, la seconda no; `const` se la funzione legge soltanto
```c
void stampaMatrice(size_t rows, size_t cols, const int m[rows][cols]) {
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < cols; j++) printf("%d ", m[i][j]);
        printf("\n");
    }
}
```
! Trabocchetto: `int (*m)[COLS]` è un puntatore a una riga; `int *m[COLS]` è un array di puntatori.

## Passare una riga {47}
= Una riga `mat[i]` è un array di COLS elementi, quindi si passa a qualunque funzione sugli array.
- ha tipo `int[COLS]` e si converte in `int*`
- si passa insieme alla sua lunghezza: `fn_su_array(COLS, mat[i]);`
- così somma, conteggio e ricerca già scritti per gli array si riusano sulle righe
> Vedi anche: Array come parametro

## Somma degli elementi di una matrice {48}
= La somma di tutti gli elementi è una sommatoria doppia: un accumulatore che parte da 0 e due cicli annidati.
- ogni Σ della formula diventa un ciclo
- buone pratiche: `size_t` per gli indici, dimensioni con `#define`, logica in funzioni, `const` in sola lettura
- errori tipici: accumulatore o indici che non partono da 0, `m[j][i]` al posto di `m[i][j]`, indici fuori intervallo
```c
int s = 0;
for (size_t i = 0; i < rows; i++)
    for (size_t j = 0; j < cols; j++)
        s += m[i][j];
```
! Trabocchetto: `m[j][i]` su una matrice non quadrata può uscire: in una 2×3 arriva a una riga 2 che non esiste.

## Somma di matrici {48}
= Si sommano gli elementi nella stessa posizione: C[i][j] = A[i][j] + B[i][j], con le stesse dimensioni.
- la stessa coppia (i, j) raggiunge la stessa posizione nelle tre matrici
- a e b sono `const` (ingresso), c no: è un **parametro di uscita**
- una funzione non restituisce una matrice: il chiamante la prepara e la funzione la riempie
```c
void sommaMatrici(size_t rows, size_t cols, const int a[rows][cols],
                  const int b[rows][cols], int c[rows][cols]) {
    for (size_t i = 0; i < rows; i++)
        for (size_t j = 0; j < cols; j++)
            c[i][j] = a[i][j] + b[i][j];
}
```

## Trasposta sul posto {48}
= La **trasposta** di una matrice quadrata n×n scambia A[i][j] con A[j][i]: le righe diventano colonne.
- vale solo per una matrice quadrata, modificata sul posto (in-place)
- la diagonale principale resta ferma
- il ciclo interno parte da `j = i + 1`, cioè solo sopra la diagonale
- lo scambio usa una variabile temporanea
```c
for (size_t i = 0; i < n; i++)
    for (size_t j = i + 1; j < n; j++) {   // solo sopra la diagonale
        int tmp = a[i][j];
        a[i][j] = a[j][i];
        a[j][i] = tmp;
    }
```
! Trabocchetto: se il ciclo interno partisse da 0, ogni coppia verrebbe scambiata due volte e la matrice tornerebbe com'era.
> Vedi anche: Scambio con variabile temporanea

## Prodotto di matrici {48}
= Il **prodotto** righe per colonne di A (m×n) e B (n×p) dà C (m×p), con C[i][j] = somma su k di A[i][k] · B[k][j].
- esiste solo se le colonne di A sono tante quante le righe di B
- tre cicli annidati: i e j scelgono la posizione, k fa la sommatoria
- l'accumulatore `s = 0` si azzera per ogni elemento, dentro il ciclo su j
```c
for (size_t i = 0; i < m; i++)
    for (size_t j = 0; j < p; j++) {
        int s = 0;                          // azzerato per ogni c[i][j]
        for (size_t k = 0; k < n; k++)
            s += a[i][k] * b[k][j];
        c[i][j] = s;
    }
```
! Trabocchetto: con `s` inizializzato una volta sola fuori dai cicli, ogni elemento conterrebbe anche le somme dei precedenti.

## Massimo positivo in una matrice {49}
= Si cerca il massimo tra i soli elementi positivi e se ne restituisce la posizione con due puntatori.
- un'unica condizione: `m[i][j] > 0 && m[i][j] > max`
- si parte da `max = 0` e dai **valori sentinella** `*iMax = rows`, `*jMax = cols`, fuori dagli indici
- ritorna `true` se esiste almeno un positivo
- a parità di massimo resta la prima posizione nella scansione per righe
```c
if (m[i][j] > 0 && m[i][j] > max) {
    max = m[i][j];
    *iMax = i;
    *jMax = j;
    esistePos = true;
}
```
! Trabocchetto: `max = 0` va bene solo qui: per un massimo qualunque si parte dal primo elemento, altrimenti con tutti negativi nessuno supera lo 0.

## Verificare una proprietà su tutta la matrice {49}
= È la quantificazione universale sulle matrici: si parte da `tuttiOk = true` e ci si ferma alla prima violazione.
- la guardia `&& tuttiOk` va in **entrambi** i cicli
- con la guardia solo nel ciclo interno il risultato è giusto, ma l'esterno fa giri inutili
```c
bool tuttiOk = true;
for (size_t i = 0; i < rows && tuttiOk; i++)
    for (size_t j = 0; j < cols && tuttiOk; j++)
        if (m[i][j] % 2 != 0)
            tuttiOk = false;   // violazione: H0 rifiutata
```
> Vedi anche: Quantificazione universale

## Esiste una riga di zeri {49}
= ∃i ∀j : m[i][j] = 0, cioè un «esiste» fuori sulle righe e un «per ogni» dentro sulle colonne: due test d'ipotesi annidati.
- esterno: `esisteRiga = false` con guardia `!esisteRiga`, come la ricerca lineare
- interno: `allZero = true` per ogni riga, con guardia `allZero`, come la verifica universale
- casi limite: con rows = 0 è falso; con cols = 0 (e rows > 0) è vero per vacuità
- la negazione, per De Morgan: in ogni riga esiste un elemento diverso da 0
```c
bool esisteRiga = false;
for (size_t i = 0; i < rows && !esisteRiga; ++i) {
    bool allZero = true;                 // riparte a ogni riga
    for (size_t j = 0; j < cols && allZero; ++j)
        if (m[i][j] != 0) allZero = false;
    if (allZero) esisteRiga = true;
}
```
! Trabocchetto: se `allZero` fosse dichiarata fuori dal ciclo esterno, dopo la prima riga non nulla resterebbe `false` per sempre.

# Matrici nello heap

## Puntatore a matrice {50}
= Un **puntatore a matrice** `int (*p)[cols]` punta a una o più righe di cols interi: è il tipo in cui si converte il nome di una matrice.
- se p punta alla prima riga, gli elementi si raggiungono con il solito `p[i][j]`
- `p + i` salta i righe intere, cioè i · cols · sizeof(int) byte: per questo nel tipo serve cols e non rows
- `p[i][j]` sta a base + (i · cols + j) × sizeof(int), la formula row-major
- esempio: con cols = 4 e int da 4 byte, `p + 1` sta 16 byte dopo p e `p[2][1]` 36 byte dopo
```c
size_t rows = 3, cols = 4;
int m[rows][cols];
int (*p)[cols] = m;    // puntatore alla prima riga
p[2][1] = 7;           // come m[2][1]
```
! Trabocchetto: senza parentesi `int *p[cols]` è un array di cols puntatori a int, non un puntatore a matrice.
> Vedi anche: Matrice in memoria, Passare una matrice a una funzione

## Matrice nello heap {50}
= Una matrice rows × cols si alloca nello heap con **una sola malloc** di rows · cols · sizeof(int) byte, assegnata a un puntatore a matrice.
![nello stack c'è solo il puntatore m, nello heap le tre righe una dopo l'altra](figure/prog/matrice_heap.png)
- la forma in memoria non cambia (righe contigue), si usa sempre `m[i][j]`
- cambiano durata e gestione: vive fino alla `free`, in qualunque funzione ci si trovi
- un solo blocco, quindi una sola `free`, poi `m = NULL`
- le funzioni con parametro `m[rows][cols]` (capitoli 47-49) la accettano così com'è
```c
int (*m)[cols] = malloc(rows * cols * sizeof(int));
if (m != NULL) {
    m[1][2] = 5;
    free(m);
    m = NULL;
}
```
! Trabocchetto: si controlla `m != NULL` prima di usare il blocco, come per gli array.
> Vedi anche: Puntatore a matrice, malloc, free

## Il tipo intermedio int_matrix_ptr_t {51}
= Una funzione non può restituire `int (*)[cols]` se cols lo legge lei stessa: si restituisce un **tipo intermedio**, puntatore a righe di lunghezza non specificata.
- `typedef int (*int_matrix_ptr_t)[];`: **typedef** dà un nome nuovo a un tipo, il suffisso `_t` è solo una convenzione
- un puntatore a `int[]` è compatibile con qualunque `int (*)[cols]`: l'indirizzo passa da un tipo all'altro senza cast
- due fasi: prima si ricevono puntatore intermedio, rows e cols; poi, con cols noto, si dichiara il tipo preciso
```c
size_t rows, cols;
int_matrix_ptr_t p = leggiMatrice(&rows, &cols);
int (*m)[cols] = p;    // ora cols è noto: tipo preciso
```
! Trabocchetto: con il solo puntatore intermedio `p[i][j]` non si può scrivere: manca la lunghezza delle righe, serve solo a trasportare l'indirizzo.
> Vedi anche: Leggere una matrice nello heap

## Leggere una matrice nello heap {51}
= leggiMatrice legge le dimensioni, alloca la matrice nello heap, legge gli elementi e restituisce il puntatore intermedio, con le dimensioni in uscita.
![dopo il ritorno p e m, nello stack di main, indicano lo stesso blocco nello heap](figure/prog/leggi_matrice_heap.png)
- prima riga: `*out_rows = *out_cols = 0`, così se qualcosa va storto il chiamante riceve una 0 × 0
- dentro la funzione cols è già letto: m si dichiara subito con il tipo preciso `int (*m)[cols]`
- le dimensioni si comunicano solo alla fine, a matrice pronta; se la malloc fallisce si ritorna `NULL`
- il blocco sopravvive al ritorno e la responsabilità di liberarlo passa al chiamante
```c
if (p != NULL) {
    int (*m)[cols] = p;
    stampaMatrice(rows, cols, m);
    free(m);           // una sola free
    m = p = NULL;      // azzerati tutti e due
}
```
! Trabocchetto: p e m sono alias dello stesso blocco: `free` su entrambi è una doppia free, e azzerarne uno solo lascia l'altro appeso.
> Vedi anche: Il tipo intermedio int_matrix_ptr_t, Restituire un array dallo heap, Responsabilità della memoria

## Quantificatori annidati in due funzioni {52}
= Le soluzioni del docente spezzano una proprietà «per ogni riga esiste…» o «esiste una riga in cui per ogni…» in **due funzioni**: una su un array, una che la chiama su ogni riga `m[i]`.
- ∀i ∃j (tutte le righe hanno un elemento in [minVal, maxVal]): verifica universale sulle righe, ricerca lineare dentro
- ∃i ∀j (esiste una riga in ordine non decrescente): ricerca lineare sulle righe, test di ordinamento dentro
- casi limite: rows = 0 rende vero il «per ogni» e falso l'«esiste»; con cols = 0 (e rows > 0) decide il quantificatore interno
- vantaggi: un solo schema per funzione, test separati, nessuna sentinella interna da reinizializzare a ogni riga
- nel prodotto di matrici il docente accumula direttamente in `c[i][j]`, azzerato prima del ciclo su k
```c
bool tutteRighe = true;
for (size_t i = 0; i < rows && tutteRighe; i++) {
    if (!esisteElemInIntervalloInArray(cols, m[i], minVal, maxVal))
        tutteRighe = false;
}
```
> Vedi anche: Esiste una riga di zeri, Passare una riga, Prodotto di matrici

# Schemi su array e stringhe

## Domande sui puntatori {lab 17}
= Tre trabocchetti del laboratorio 7: la stellina nelle dichiarazioni multiple, il puntatore a puntatore e la precedenza di `*` e `++`.
- `int* countPtr, count;`: solo countPtr è un puntatore, count è un `int`; un puntatore per riga evita l'equivoco
- `&pC`, con pC di tipo `int*`, è un `int**`: non si assegna a un `int*`
- per stampare il dato puntato serve `*pC`: `printf("%d", pC)` passa un indirizzo
- `*p++` e `*(p++)` incrementano il puntatore; `(*p)++` e `*p += 1` il valore puntato
```c
size_t index = 2;
size_t* p = &index;
(*p)++;     // index vale 3
*p += 1;    // index vale 4
```
! Trabocchetto: `++` postfisso lega più forte di `*`: `*p++` sposta la freccia, e dopo `*p` legge fuori dalla variabile.
> Vedi anche: Puntatore, Dereferenziamento, Precedenza degli operatori

## Schemi di modifica degli array {lab 17, lab 18}
= Quattro schemi ricorrenti su un array a di lunghezza aLen: **trasformazione**, **filtro selettivo**, **riduzione sul posto** e **duplicazione selettiva**.
- trasformazione: `a[i] = tr(a[i])` per ogni i, la lunghezza non cambia
- filtro: copia in b gli elementi con Cond, con `bLen < BMAX` nel ciclo (è la selezione)
- riduzione sul posto: tiene in a solo gli elementi con Cond, con due indici sullo stesso array
- duplicazione: copia tutto in b, due volte gli elementi con Cond
- una funzione che cambia la lunghezza la riceve per puntatore, `size_t* p_aLen`, e la aggiorna alla fine
```c
size_t bLen = 0;
for (size_t i = 0; i < aLen && bLen < BMAX; i++) {
    b[bLen] = a[i];  bLen++;
    if (Cond(a[i]) && bLen < BMAX) { b[bLen] = a[i];  bLen++; }
}
```
! Trabocchetto: nella duplicazione il controllo `bLen < BMAX` va ripetuto prima della seconda copia: il buffer può riempirsi a metà.
> Vedi anche: Selezione, Riduzione sul posto, Modello dimensione-capacità

## Riduzione sul posto {lab 17, lab 18}
= La **riduzione sul posto** (in-place removal) compatta verso l'inizio dello stesso array gli elementi da tenere: i legge tutto, j scrive solo quelli che rispettano Cond.
- j avanza solo quando un elemento viene tenuto, e alla fine è la nuova lunghezza: `aLen = j`
- vale sempre j ≤ i: la scrittura non cancella mai un elemento non ancora letto
- dopo [0, aLen) restano dei residui, che non fanno più parte dell'array
- esempio: 0, 3, 2, 4, 3 con Cond «≥ 3» diventa 3, 4, 3 (più i residui 4, 3)
```c
void filtra_maggiori_di(size_t* p_aLen, int a[], const int maggiori_di) {
    size_t j = 0;
    for (size_t i = 0; i < *p_aLen; i++)
        if (a[i] > maggiori_di) { a[j] = a[i]; j++; }
    *p_aLen = j;
}
```
> Vedi anche: Schemi di modifica degli array, Elimina vocali con due puntatori

## Scorrere una stringa con un puntatore {lab 19}
= Una stringa si scorre con un puntatore: `*pStr` è il carattere corrente, `pStr++` avanza, ci si ferma su `'\0'`.
- due forme: `while (*pStr != '\0') { …; pStr++; }` oppure `for ( ; *pStr != '\0'; pStr++)`
- il parametro è una copia dell'indirizzo: farlo avanzare non sposta il puntatore del chiamante
- se la funzione modifica la stringa il parametro è `char*`, senza `const`
- codifica: ogni maiuscola diventa la successiva e Z torna ad A, gli altri caratteri restano; decodifica fa il contrario
```c
void codifica(char *pStr) {
    for ( ; *pStr != '\0'; pStr++)
        if (*pStr >= 'A' && *pStr <= 'Z') {
            if (*pStr == 'Z') *pStr = 'A';
            else *pStr = *pStr + 1;
        }
}
```
! Trabocchetto: senza il caso a parte per la Z, `'Z' + 1` non è una lettera ma `'['`, il codice ASCII 91.
> Vedi anche: Caratteri come numeri e ctype.h, Stringa e terminatore

## Elimina vocali con due puntatori {lab 19}
= elimina_vocali è una riduzione sul posto scritta con i puntatori: pSrc legge ogni carattere, pDst scrive solo quelli da tenere e alla fine riceve il terminatore.
![elimina_vocali su "informazione": prima e dopo, con le posizioni finali di pSrc e pDst](figure/lab/elimina_vocali.png)
- pDst non supera mai pSrc, quindi non si sovrascrive un carattere non ancora letto
- `"informazione"` diventa `"nfrmzn"`; i residui dopo il nuovo `'\0'` non contano più
- senza vocali ogni carattere si ricopia su se stesso; con solo vocali resta la stringa vuota
```c
void elimina_vocali(char* pStr) {
    char* pDst = pStr;
    for (char* pSrc = pStr; *pSrc != '\0'; pSrc++)
        if (!is_vowel(*pSrc)) { *pDst = *pSrc; pDst++; }
    *pDst = '\0';                   // nuovo terminatore
}
```
! Trabocchetto: va chiamata su un array, `char s[] = "informazione";`: modificare una stringa letterale è comportamento indefinito.
> Vedi anche: Riduzione sul posto, Scorrere una stringa con un puntatore

## Intervallo semiaperto di indici {lab 20}
= Un **intervallo semiaperto** [left, right) contiene gli indici left ≤ i < right, con 0 ≤ left ≤ right ≤ len: left incluso, right escluso.
![l'intervallo [left, right) dentro l'array](figure/lab/intervallo_semiaperto.png)
- ha right − left elementi, è vuoto se left == right, primo elemento `a[left]`, ultimo `a[right - 1]`
- [a, b) e [b, c) si incollano senza sovrapporsi in [a, c); il caso base è [0, len)
- le funzioni su un intervallo sono i soliti schemi con `for (size_t i = left; i < right; i++)`; copiandolo in un nuovo array, `b[i] = a[left + i]`
- per restringerlo si passano gli estremi per puntatore, `(*pLeft)++` e `(*pRight)--`, con la guardia prima dell'accesso
```c
while (*pLeft < *pRight && a[*pLeft] == 0)
    (*pLeft)++;                 // zero iniziale escluso
while (*pRight > *pLeft && a[*pRight - 1] == 0)
    (*pRight)--;                // zero finale escluso
```
! Trabocchetto: con indici `size_t` l'invariante da controllare è `assert(right >= left)`: se è violato right − left non è negativo ma enorme, e `assert(len >= 0)` non controlla nulla.
> Vedi anche: Intervalli, size_t e wrap-around

## Funzioni sulle stringhe senza string.h {lab 21}
= Nel laboratorio 7 si riscrivono a mano lunghezza, confronto, prefisso, ricerca di una sottostringa e concatenazione in un buffer.
- `my_strlen`: l'indice del terminatore è la lunghezza; ritorna `size_t`
- `my_equal` e `startswith` avanzano finché i caratteri coincidono: un `'\0'` interrompe il confronto, quindi non si esce mai dalle stringhe
- `contains`: ricerca lineare delle partenze con `startswith(str + i, sub)`; la prima occorrenza è [i, i + subLen)
- in un buffer di strLen char si scrivono al massimo strLen − 1 caratteri più il `'\0'`; con strLen = 0 niente
```c
bool startswith(const char* str, const char* prefix) {
    size_t i = 0;
    while (prefix[i] != '\0' && str[i] == prefix[i])
        i++;
    return prefix[i] == '\0';    // prefisso confrontato tutto
}
```
! Trabocchetto: con i `size_t` si scrive `i + subLen <= strLen`, non `i <= strLen - subLen`, e si controlla `strLen > 0` prima di `strLen - 1`: le sottrazioni andrebbero in wrap-around.
> Vedi anche: Le funzioni di string.h, Intervallo semiaperto di indici, size_t e wrap-around
