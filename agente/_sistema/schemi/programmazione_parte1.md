# Come funziona un calcolatore

## Algoritmo {2}
= Un **algoritmo** è una ricetta: passi chiari, uno dopo l'altro, che da un input danno un output e prima o poi finiscono.
- **Correttezza**: dà l'output giusto per ogni input ammissibile.
- **Terminazione**: si conclude dopo un numero finito di passi.
- Programma = Algoritmi + Strutture Dati (Wirth).
! Controlla la condizione prima di fare l'operazione: se sommi prima di controllare `i = n`, con n = 0 il ciclo non finisce più.
> Vedi anche: Accumulatore e contatore, Programmazione strutturata

## Programmazione strutturata {3, 19}
= Scrivere il programma a blocchi annidati, resi chiari dall'indentazione, invece di saltare a numeri di riga.
![Sequenza, selezione e iterazione](figure/prog/ch03_tre_strutture.png)
- Ogni algoritmo si scrive con tre sole strutture: **sequenza**, **selezione** (scelta), **iterazione** (ripetizione).
- **Pseudo-codice**: l'algoritmo in parole ordinate e rientrate; nessun computer lo esegue.
- **Diagramma di flusso**: blocchi e frecce che mostrano dove si decide e dove si ripete.
- In C: selezione con `if`, iterazione con `while`, `for` e `do-while`.
> Vedi anche: if e if-else, Il ciclo while

## Bit e byte {4}
= Il **bit** vale 0 o 1; 8 bit formano un **byte**; la **parola** è il blocco di byte su cui la CPU lavora in una volta.
- Con N bit si hanno 2^{N} combinazioni: un byte ha 2^{8} = 256 valori (da 0 a 255).
- Si usa il binario perché un circuito a due stati è facile, economico e stabile.
- Il byte è l'unità di indirizzamento: ogni byte della RAM ha un **indirizzo** progressivo, a partire da 0.
- Una parola è di 16, 32 o 64 bit (2, 4 o 8 byte): una CPU a 64 bit lavora su 8 byte alla volta.
> Vedi anche: Architettura di Von Neumann, Indirizzo e operatore &

## Architettura di Von Neumann {4, 3}
= Il modello dei calcolatori moderni: dati e istruzioni stanno nella stessa memoria e la CPU li elabora.
- **Programma memorizzato**: le istruzioni sono caricate in memoria, non realizzate con i collegamenti elettrici.
- **Memoria unificata** (istruzioni e dati nello stesso spazio) e **rappresentazione binaria** di tutto.
- Quattro blocchi: **RAM** (veloce, volatile), **CPU**, **bus di sistema** (porta indirizzi, dati, controlli), **storage secondario** (disco, SSD: lento ma permanente).
- La RAM ha un'area del programma (dall'indirizzo 0) e un'area dei dati.
> Vedi anche: CPU e ciclo fetch-decode-execute, Bit e byte

## CPU e ciclo fetch-decode-execute {4}
= La CPU ripete all'infinito: preleva un'istruzione, la decodifica, la esegue.
- **Unità di controllo** (coordina), **ALU** (calcoli e confronti), **registri** (piccole memorie velocissime).
- **Program Counter (PC)**: indirizzo della prossima istruzione; **Instruction Register (IR)**: l'istruzione in esecuzione.
- La CPU non calcola in RAM: carica i valori nei registri, li elabora con l'ALU, riscrive il risultato in RAM.
- Fetch: legge l'istruzione indicata dal PC e la mette nell'IR, il PC avanza; un salto sovrascrive il PC.
- È **deterministica** e non ha un concetto di «fine programma»: la terminazione va programmata.
> Vedi anche: Architettura di Von Neumann, Dal linguaggio macchina al C

# Dal sorgente all'eseguibile

## Dal linguaggio macchina al C {5, 3}
= Il **linguaggio macchina** è fatto di bit ed è l'unico che la CPU esegue; l'**assembly** gli dà nomi leggibili; il C è un linguaggio di alto livello.
- Ogni famiglia di CPU ha la sua **ISA** (x86, ARM, RISC-V): il codice macchina non è portabile.
- Ogni istruzione assembly corrisponde a una istruzione macchina; la traduce l'**assembler**.
- Limiti dell'assembly: prolisso, nomi poco chiari, salti a righe, non portabile.
- I linguaggi di **alto livello** (C, Python, Java) nascondono registri e indirizzi.
```
LOAD, R0, @A     // R0 <- contenuto della cella A
LOAD, R1, @B     // R1 <- contenuto della cella B
ADD, R0, R1      // l'ALU somma: R0 <- R0 + R1
STORE, R0, @A    // il risultato torna nella cella A
```
> Vedi anche: Il linguaggio C, Assegnamento

## Il linguaggio C {5, lab 3}
= Il C (Ritchie, 1972, per riscrivere Unix) è **compilato**, **imperativo**, **strutturato** e **fortemente tipizzato**.
![Il sorgente viene tradotto per intero prima dell'esecuzione](figure/prog/ch05_compilazione.png)
- Compilato: tutto il sorgente viene tradotto in codice macchina prima di eseguirlo.
- Strutturato: funzioni e blocchi tra graffe `{}`, niente salti a numeri di riga.
- Fortemente tipizzato: ogni variabile va dichiarata con il suo tipo.
- File `.c`: unità di compilazione; file `.h`: intestazioni con le dichiarazioni.
```c
#include <stdio.h>
int main(void) {
    printf("Buongiorno!\n");
    return 0;
}
```
> Vedi anche: Le fasi della compilazione, Tipi primitivi

## Le fasi della compilazione {lab 4}
= Dietro il comando `gcc` lavorano quattro programmi in fila: preprocessore, compilatore, assemblatore e linker.
- **Preprocessore** (`cpp`): gestisce gli `#include`; **compilatore** (`cc`): traduce in assembly; **assemblatore** (`as`): produce codice macchina.
- Il risultato è un **file oggetto** (`.o` o `.obj`): codice macchina ancora incompleto.
- Il **linker** (`ld`) unisce i file oggetto in un unico **eseguibile** (`.exe` o nessuna estensione).
- Il **disassemblatore** (`objdump -d eseguibile`) mostra l'assembly del programma, non il C di partenza.
> Vedi anche: I comandi di gcc, Il linguaggio C

## I comandi di gcc {lab 4, lab 5, lab 9, 15}
= Con `gcc` si compila, si collega o si fa tutto in un passo; `-o` dà il nome al file prodotto.
```
gcc -c sorgente.c -o oggetto.o      # solo compilazione
gcc oggetto1.o oggetto2.o -o prog   # collegamento
gcc -Wall -Werror prog.c -o prog    # tutto in un passo
./prog                              # Unix (Windows: prog)
gcc programma.c -lm                 # se si usa math.h
```
- **-c**: si ferma al file oggetto; senza `-c` si collega e si ottiene l'eseguibile.
- **-Wall** attiva gli avvertimenti (warning); **-Werror** li trasforma in errori.
- Su Windows i nomi diventano `oggetto.obj` e `prog.exe`; su Unix si lancia con `./`.
- `-lm` collega la libreria matematica (su Unix), in fondo al comando.
! All'esame e su Coderunner si compila con `-Wall -Werror`: anche un semplice warning blocca la compilazione.
> Vedi anche: Le fasi della compilazione, La libreria math.h

## La riga di comando {lab 2, lab 11}
= La **CLI** (shell, terminale, prompt dei comandi) è il modo di dare ordini al computer scrivendo righe di testo.
- Sintassi: `nome_comando opzioni argomenti`; le opzioni iniziano con `-` in Unix e con `/` in Windows.
- **Percorso assoluto**: dalla radice fino al file; **percorso relativo**: parte dalla cartella di lavoro. `.` è la cartella di lavoro, `..` quella che la contiene.
- Comandi (Windows / Unix): `cd`, `dir` / `ls`, `mkdir`, `copy` / `cp`, `ren` / `mv`, `del` / `rm`, `type` / `cat`.
- Input da file invece che da tastiera: `./media_seq < input01.txt` (Windows: `media_seq.exe < input01.txt`).
> Vedi anche: I comandi di gcc

# Tipi e variabili

## Tipi primitivi {6, lab 7}
= Il **tipo** dice come interpretare i bit: quanto spazio occupano, quali valori e quali operazioni sono ammessi.
- Un tipo ha nome, dimensione, dominio di valori, operazioni, rappresentazione interna e regole di conversione.
- Interi: `short` (2 byte), `int` (4), `long` (4 o 8), `long long` (8); `unsigned` toglie il segno e raddoppia i positivi.
- Reali: `float` (4 byte) e `double` (8); `char` (1 byte, caratteri ASCII).
- `bool` è in `<stdbool.h>`, `size_t` (intero senza segno per le dimensioni) in `<stddef.h>`.
- `sizeof` dà i byte di un tipo (si stampa con `%zu`); è garantito solo che `char ≤ short ≤ int ≤ long ≤ long long`.
> Vedi anche: Overflow e troncamento, printf e specificatori

## Overflow e troncamento {6}
= I tipi del C sono modelli **finiti** di ℤ e ℝ: hanno un numero fisso di bit.
```c
int x = 2147483647;  // massimo int a 32 bit
x = x + 1;           // OVERFLOW: tipicamente -2147483648
int y = 8.89;        // TRONCAMENTO: y vale 8
```
- **Overflow**: il risultato non sta nei bit; di solito si riparte dal minimo negativo, spesso senza segnalazione (per gli `int` con segno è indefinito).
- I reali hanno precisione finita: possibili errori di arrotondamento.
- **Troncamento**: un reale messo in un intero perde la parte frazionaria.
! Il troncamento non arrotonda: 8.89 diventa 8, non 9.
> Vedi anche: Conversioni implicite e promozione, Tipi primitivi

## Variabile {6}
= Una **variabile** è una porzione di memoria con un nome; ha quattro attributi: nome, tipo, indirizzo e valore.
![Nome, tipo, indirizzo e valore](figure/prog/ch06_variabile_quaterna.png)
- L'indirizzo lo sceglie il compilatore; il valore può cambiare durante l'esecuzione.
- Nome: lettere, cifre e `_`; non può iniziare con una cifra; maiuscole e minuscole sono diverse.
- Niente spazi o simboli (`!`, `@`, `#`, `$`, `%`), niente parole chiave (`int`, `if`, `return`…); da evitare anche nomi come `main` o `printf`.
- Il nome deve essere unico nel suo ambito di visibilità (scope).
> Vedi anche: Dichiarazione e inizializzazione, Indirizzo e operatore &

## Dichiarazione e inizializzazione {6, 7, 10}
= **Dichiarare** riserva lo spazio sullo stack; **inizializzare** è dare un valore nel momento della dichiarazione.
```c
int x;            // dichiarazione: valore indeterminato (?)
x = 10;           // assegnamento successivo
float y = 3.14f;  // inizializzazione contestuale
```
- Una variabile locale non inizializzata contiene i bit lasciati da prima: valore **indeterminato**, scritto «?» negli schemi.
- `&x` si può usare anche se `x` non è inizializzata: si usa l'indirizzo, non il valore.
- Conviene dare sempre un valore prima di usare una variabile.
! Leggere una variabile mai inizializzata (per esempio dopo una `scanf` fallita) dà un comportamento indefinito.
> Vedi anche: Stack con FP e SP, Il valore restituito da scanf

# Memoria, stack e assegnamento

## Stack con FP e SP {7}
= Lo **stack** (pila) è la parte dell'area dati che contiene le variabili locali, una dopo l'altra in ordine di dichiarazione.
![Lo stack dopo tre dichiarazioni](figure/prog/ch07_stack_fp_sp.png)
- Memoria del programma: **area codice** (istruzioni, dimensione fissa, il PC parte da `main`) e **area dati**.
- Nel modello del corso lo stack cresce verso indirizzi più bassi.
- **Frame Pointer (FP)**: base fissa; **Stack Pointer (SP)**: cima corrente. All'inizio coincidono.
- A ogni dichiarazione SP scende di quanti byte servono (−4 per un `int`); nessun valore viene scritto.
- Lo stack ha una capienza massima: se la si supera si ha lo **stack overflow** e il programma si interrompe.
> Vedi anche: Scope e lifetime, Dichiarazione e inizializzazione

## Scope e lifetime {7, 19, 20, 21}
= **Scope**: dove il nome di una variabile si può usare. **Lifetime**: quando la variabile esiste davvero in memoria.
![y esiste solo dentro il blocco del ciclo](figure/prog/ch20_scope_stack.png)
- Una variabile locale è visibile solo dentro le graffe `{ }` del blocco in cui è dichiarata, anche nei blocchi annidati.
- Nasce alla dichiarazione e muore all'uscita dal blocco (SP risale): per le locali scope e lifetime coincidono.
- In un ciclo, a ogni giro le variabili del blocco vengono allocate di nuovo e poi deallocate.
- La variabile dichiarata nell'intestazione del `for` esiste solo dentro il `for`.
! Usare dopo il ciclo una variabile dichiarata dentro il ciclo è un errore: va dichiarata fuori.
> Vedi anche: Stack con FP e SP, Il ciclo for

## Assegnamento {8}
= `variabile = espressione;` calcola prima il lato destro (**rvalue**) e poi copia il risultato nella cella del lato sinistro (**lvalue**).
![z = x + y diventa due LOAD, una ADD e una STORE](figure/prog/ch08_esecuzione_z.png)
- A sinistra serve una cella modificabile: `5 = x` non ha senso.
- Forme: inizializzazione, assegnamento successivo, multiplo (`a = b = c = 0;`), da input (`scanf`).
- Composti: `x += y` vale `x = x + y` (così anche `-=`, `*=`, `/=`, `%=`); `x++` e `x--` aggiungono o tolgono 1.
```c
int x = 5;
x += 3;   // 8
x %= 3;   // 2 (resto di 8 / 3)
x++;      // 3
```
> Vedi anche: Precedenza degli operatori, Scambio con variabile temporanea

## Precedenza degli operatori {lab 6}
= Come in matematica: prima `*`, `/` e `%`, poi `+` e `-`; a parità di precedenza si va da sinistra a destra.
- Le parentesi si valutano per prime, partendo dalle più interne.
- Nel dubbio, le parentesi tolgono ogni ambiguità.
```c
int x = 7 + 3 * 6 / 2 - 1;      // 18, poi 9, poi 15
int z = 2 % 2 + 2 * 2 - 2 / 2;  // 0 + 4 - 1 = 3
```
! a·x^{3} + 7 si scrive `a * x * x * x + 7`; `a * x * x * (x + 7)` somma 7 prima di moltiplicare e dà un'altra cosa.
> Vedi anche: Assegnamento, Divisione tra interi e cast

## Scambio con variabile temporanea {13, lab 7, lab 12}
= Per scambiare due variabili serve una terza variabile d'appoggio che conservi un valore prima che venga sovrascritto.
![Il 5 resta al sicuro in temp](figure/prog/ch13_swap_temp.png)
```c
int x = 5, y = 2, temp;
temp = x;   // salvo il vecchio x
x = y;      // ora posso sovrascrivere x
y = temp;   // recupero il valore salvato
```
- Come scambiare due tè con una tazza vuota: costa una sola variabile in più.
- Con quattro variabili (rotazione): `temp = v1; v1 = v2; v2 = v3; v3 = v4; v4 = temp;`.
- Serve anche in Fibonacci: con `n = m; m = n + m;` il vecchio `n` è già perso.
! L'ordine conta: con `x = y; temp = x; y = temp;` alla fine valgono tutti 2 e il 5 è perso.

# Input e output

## printf e specificatori {8, 14, 17, 24, lab 7}
= `printf` stampa una stringa di formato in cui gli **specificatori** `%…` vengono sostituiti dai valori.
- `%c` char, `%hd` short, `%d` int, `%ld` long, `%lld` long long, `%u` unsigned int.
- `%zu` size_t, `%td` ptrdiff_t, `%p` indirizzi, `%f` float e double.
- `bool` non ha uno specificatore suo: si usa `%d` (stampa 0 o 1).
- Larghezza: `%6d` occupa almeno 6 caratteri (spazi a sinistra), `%06d` riempie con zeri (7 diventa 000007).
```c
int x = 5, y = 2, z = 7;
printf("x, y e z valgono %d, %d e %d\n", x, y, z);
printf("[%6d] [%06d]\n", x, x);   // [     5] [000005]
```
> Vedi anche: float e double, scanf

## scanf {8, 10, 11, 14}
= `scanf` legge da tastiera, converte nel tipo indicato e scrive il valore nella variabile di cui riceve l'**indirizzo**.
```c
int x, y;
scanf("%d", &x);        // &x: dove scrivere il valore
scanf("%d%d", &x, &y);  // due valori, separati da spazi
```
- Serve `&` perché `scanf` deve sapere in quale cella scrivere.
- Ogni conversione vuole un puntatore al tipo giusto: `%d` vuole un `int*` (va bene anche un puntatore `pX = &x`).
- Si ferma quando l'utente preme INVIO.
- Per leggere un `double` serve `%lf`.
! Dimenticare `&` (`scanf("%d", y)`): `scanf` scrive all'indirizzo contenuto in `y` e il programma probabilmente si blocca.
> Vedi anche: Il valore restituito da scanf, Puntatore

## Il valore restituito da scanf {10, 18, lab 10, lab 11}
= `scanf` restituisce quanti valori è riuscita a leggere: può essere meno di quelli richiesti.
- Con `%d` e input `1234.56`: legge 1234, restituisce 1, «.56» resta da leggere.
- Con input `A`: restituisce 0 e la variabile non viene modificata.
- Buona pratica: controllare il valore restituito prima di usare le variabili lette.
- Grazie alla cortocircuitazione, se `scanf` fallisce la seconda condizione non viene valutata.
```c
int sum = 0, number;
while (1 == scanf("%d", &number) && number != 0) {
    sum += number;   // somma fino allo 0 finale
}
```
! Se `scanf` fallisce su una variabile non inizializzata, il suo valore resta indeterminato: non usarla.
> Vedi anche: scanf, Cortocircuitazione

## Errori tipici di compilazione {lab 6, lab 5, 11}
= Imparare a leggere i messaggi del compilatore (con `-Wall -Werror`) fa parte dell'imparare a programmare.
- Manca il `;` a fine istruzione: errore di compilazione.
- Variabile usata senza dichiararla: errore («'z' undeclared»).
- `printf("%d", &z)` stampa l'indirizzo invece del valore: avviso con `-Wall`, per il valore si scrive `z`.
> Vedi anche: scanf, Puntatore

# Indirizzi e puntatori

## Indirizzo e operatore & {9}
= L'**indirizzo** di una variabile è il numero (senza segno) del primo byte che occupa, come un numero civico; `&x` lo restituisce.
![Gli indirizzi di x, y e z sullo stack](figure/prog/ch09_indirizzi_xyz.png)
```c
int x = 5;
printf("x all'indirizzo %p vale %d\n", &x, x);
```
- `x` è il valore (il contenuto), `&x` è l'indirizzo (la posizione): cose diverse.
- Si stampa con `%p`, di solito in esadecimale; cambia tra piattaforme ed esecuzioni: mai usarlo nella logica.
- Le variabili dichiarate dopo hanno indirizzi più bassi (lo stack scende).
! `&` vuole qualcosa che sta in memoria: `&5` e `&(x + 1)` sono errori.
> Vedi anche: Puntatore, Stack con FP e SP

## Puntatore {11, 12, lab 7}
= Un **puntatore** è una variabile che contiene l'indirizzo di un'altra variabile (la variabile **puntata**).
![pX contiene l'indirizzo di x](figure/prog/ch11_puntatore.png)
```c
int x = 5;
int *pX = &x;     // pX contiene l'indirizzo di x
scanf("%d", pX);  // come scanf("%d", &x)
```
- Per ogni tipo `T` c'è il tipo `T*`, «puntatore a T»: se `x` è `int`, `&x` è `int*`.
- `int* pX` e `int *pX` sono equivalenti.
- Il puntatore è una variabile: ha un suo indirizzo (`&pX`) e occupa memoria.
- Occupa sempre la stessa quantità (8 byte su 64 bit, 4 su 32), qualunque sia il tipo puntato.
! `float f; int *p = &f;` mescola tipi incompatibili: warning, errore in GCC 14.
> Vedi anche: Dereferenziamento, NULL e puntatori non inizializzati

## Dereferenziamento {12}
= `*p` è la variabile puntata da `p`: si usa l'indirizzo per leggerla o modificarla.
```c
int x = 5;
int *pX = &x;
printf("%d\n", *pX);  // 5, come x
*pX = 10;             // ora x vale 10
```
- Se `p` ha tipo `T*`, allora `*p` ha tipo `T`.
- `&` e `*` si annullano: `*&pA` e `&*pA` valgono come `pA`.
- Usi di `*`: moltiplicazione, dichiarazione di un puntatore, dereferenziamento (il puntatore a puntatore non è nel corso).
! In `int *pX = &x;` l'asterisco dichiara il puntatore: l'indirizzo va in `pX`, non in `*pX`.
> Vedi anche: Aliasing, Puntatore

## Aliasing {12}
= **Aliasing**: la stessa variabile è raggiungibile da più nomi, il suo e quello di ogni puntatore che ne contiene l'indirizzo.
![Due puntatori alla stessa variabile](figure/prog/ch12_aliasing.png)
```c
int x = 5;
int *pX = &x;
int *pXbis = pX;  // stesso indirizzo
*pXbis = 1234;    // x, *pX, *pXbis valgono 1234
```
- `pX` e `pXbis` sono due variabili diverse con lo stesso valore (l'indirizzo di `x`).
- Una modifica fatta tramite un alias si vede da tutti gli altri.
- `scanf("%d", &x)`, `scanf("%d", pX)` e `scanf("%d", pXbis)` sono equivalenti.
> Vedi anche: Dereferenziamento

## NULL e puntatori non inizializzati {12}
= `NULL` è il valore che significa «questo puntatore non punta a niente».
```c
int *p = NULL;   // inizializzazione sicura
int *q;          // valore indeterminato
// *p = 10; e *q = 10; sono errori a tempo di esecuzione
```
- Si può dereferenziare solo un puntatore che contiene un indirizzo valido.
- `NULL` evita il valore casuale e serve come valore sentinella («non punta a nulla»).
- Dereferenziare un puntatore non inizializzato o `NULL` è un comportamento indefinito (di solito il programma termina con errore).
! `NULL` non rende sicuro il dereferenziamento: prima di usare `*p` il puntatore deve puntare a una variabile.
> Vedi anche: Puntatore, Dereferenziamento

# Numeri reali e conversioni

## float e double {14, lab 7}
= Tipi in virgola mobile (IEEE 754): `float` a 32 bit (circa 7 cifre giuste), `double` a 64 bit (circa 15-16 cifre).
- Intervalli: `float` da circa 10^{-38} a 10^{38}, `double` da circa 10^{-308} a 10^{308}. Sono approssimazioni.
- Operazioni `+ - * /`; il modulo `%` esiste solo per gli interi. Nel codice i decimali hanno il punto (`1.50`).
- Stampa: `%f` (6 decimali), `%e` (scientifica), `%g` (la più compatta); `%.3f` mostra 3 decimali arrotondando (2.5678 diventa 2.568).
- Lettura: `%f` per `float`, `%lf` per `double` (anche `%le`, `%lg`).
```c
double prezzo;
scanf("%lf", &prezzo);       // double: %lf
printf("%.2f\n", prezzo);    // in printf %f va bene per entrambi
```
! `scanf("%f", ...)` con un `double` scrive solo una parte degli 8 byte: il valore letto è sbagliato.
> Vedi anche: Divisione tra interi e cast, printf e specificatori

## La libreria math.h {15, lab 6, lab 10}
= `math.h` contiene le funzioni matematiche: `sqrt` (radice), `pow` (potenza), `sin`, `cos`…
```c
#include <math.h>
double r = sqrt(9.0);     // 3.0
double q = pow(9.0, 2);   // 81.0
```
- Lavorano in genere con `double` (ci sono versioni con suffisso `f` e `l`); un argomento `int` viene convertito.
- `abs()` (valore assoluto di un intero) è in `<stdlib.h>`; per i `double` c'è `fabs()` in `<math.h>`.
- La documentazione si consulta online, per esempio su cppreference.com.
! Su Unix serve `-lm` in fondo al comando (`gcc programma.c -lm`), altrimenti il collegamento fallisce con «undefined reference».
> Vedi anche: I comandi di gcc

## Conversioni implicite e promozione {16}
= Quando si mescolano tipi diversi il compilatore converte da solo (**casting implicito**), anche perdendo informazione senza avvisare.
```c
float f = 3.7;
int y = f;      // 3: parte frazionaria persa in silenzio
char c = 'A';
int k = c;      // 65, il codice ASCII
```
- `int` → `float`/`double`: di norma nessuna perdita.
- `float`/`double` → `int`: si perdono i decimali; `double` → `float`: si perde precisione.
- **Promozione**: in un'operazione il tipo più piccolo passa al più grande (`char + int` → `int`, `int + double` → `double`).
- Conversioni non compatibili (`int *p = x;` con `x` intero) sono segnalate dal compilatore.
> Vedi anche: Divisione tra interi e cast, Overflow e troncamento

## Divisione tra interi e cast {16, lab 6, lab 9}
= Se entrambi gli operandi sono interi, `/` fa la **divisione intera**; il **cast** `(tipo)espressione` forza una conversione.
![Dove si perde la parte frazionaria](figure/prog/ch16_conversioni_divisione.png)
```c
int x = 5, y = 2;
float a = x / y;         // 2.0: divisione fra interi
float b = x / (float)y;  // 2.5: x viene promosso a float
```
- `7 / 2` vale 3 e `7 % 2` vale 1.
- Il cast agisce solo sull'espressione subito a destra e non cambia il tipo della variabile.
- In alternativa si divide per un reale: `(x1 + x2 + x3) / 3.0`.
! `float z = x / y;` con `x`, `y` interi dà 2.000000: la frazione si perde nella divisione, prima dell'assegnamento.
> Vedi anche: Conversioni implicite e promozione, Somma e conteggio in un array

# Espressioni booleane

## Operatori relazionali e logici {17, 18, lab 8}
= Gli operatori **relazionali** confrontano due valori, quelli **logici** combinano condizioni; il risultato è 1 (vero) o 0 (falso).
![Tavole di verità di AND, OR e NOT](figure/prog/ch17_tavole_booleane.png)
- Relazionali: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- `&&` (AND): vero se lo sono entrambe; `||` (OR): vero se lo è almeno una; `!` (NOT): inverte.
- `&&` ha la precedenza su `||`; le condizioni lunghe si spezzano in variabili booleane con nomi chiari.
- **De Morgan**: `!(a && b)` equivale a `!a || !b`, e `!(a || b)` equivale a `!a && !b`.
! `=` assegna, `==` confronta: `if (x = y)` copia `y` in `x` ed è vero ogni volta che `y` non è 0.
> Vedi anche: Il tipo bool, Intervalli

## Il tipo bool {17}
= `bool` (da `<stdbool.h>`, C99) è il tipo delle variabili che valgono solo vero o falso, con le costanti `true` e `false`.
```c
#include <stdbool.h>
int voto = 25;
bool superato = voto >= 18;
printf("%d\n", superato);   // stampa 1
```
- Storicamente si usano gli interi: 0 è falso, qualunque valore diverso da 0 è vero.
- Una variabile `bool` può conservare il risultato di una condizione.
- Si stampa con `%d` (0 o 1); negli schemi di memoria occupa un bit.
> Vedi anche: Operatori relazionali e logici, Sentinelle e uscita dai cicli

## Intervalli {18, lab 8}
= In C «x sta tra min e max» si scrive con due confronti uniti da `&&`.
![I quattro tipi di intervallo in C](figure/prog/ch18_intervalli.png)
- Chiuso [min, max]: `min <= x && x <= max`.
- Semiaperto sinistro [min, max): `min <= x && x < max`, molto usato per gli indici.
- Aperto (min, max): `min < x && x < max`.
! `min <= x <= max` compila ma vale `(min <= x) <= max`: con min = 0, x = 20, max = 10 è vera; e `4 > 3 > 2` è falsa.
> Vedi anche: Operatori relazionali e logici, Il ciclo for

## Cortocircuitazione {18}
= Con `&&` e `||` il C smette di valutare appena il risultato è deciso (**short-circuit evaluation**, garantita dallo standard).
- `&&`: se la prima condizione è falsa, la seconda non viene valutata.
- `||`: se la prima condizione è vera, la seconda non viene valutata.
- Permette condizioni sicure: la parte pericolosa va a destra di un controllo.
```c
int numeratore = 10, divisore = 0;
bool ok = (divisore != 0) && (numeratore / divisore > 5);
// divisore è 0: la divisione non viene mai eseguita
```
! L'ordine conta: scrivendo prima la divisione e poi `divisore != 0`, la divisione per zero avviene davvero.
> Vedi anche: Il valore restituito da scanf, Operatori relazionali e logici

# Scelte con if

## if e if-else {19, 18}
= L'`if` esegue un blocco solo se la condizione è vera; con `else` si esegue un blocco diverso quando è falsa.
![Il flusso di if, if-else e if-else if-else](figure/prog/ch19_flusso_if.png)
```c
int batteria = 15;
if (batteria < 20) {
    printf("Batteria quasi scarica!\n");
} else {
    printf("Batteria sufficiente.\n");
}
```
- La condizione fra parentesi è un'espressione booleana: vera (diversa da 0) o falsa (0).
- Con `if-else` si esegue sempre uno dei due blocchi, mai entrambi.
- **Operatore ternario** per casi semplici: `int y = (x % 2 == 0) ? 100 : 200;`.
> Vedi anche: if-else if-else, Errori con if

## if-else if-else {19, lab 9}
= Generalizza l'`if-else` a più alternative: vince la prima condizione vera.
```c
char colore = 'G';   // R = rosso, G = giallo, V = verde
if (colore == 'R') { printf("Fermati!\n"); }
else if (colore == 'G') { printf("Attenzione, rallenta.\n"); }
else if (colore == 'V') { printf("Puoi passare.\n"); }
else { printf("Colore non valido!\n"); }
```
- Le condizioni si valutano in ordine; si esegue al più un blocco (esattamente uno se c'è l'`else` finale).
- L'`else` finale raccoglie tutti gli altri casi, anche le scelte non valide.
- Con intervalli semiaperti (`ora >= 6 && ora < 12`, poi `ora >= 12 && ora < 18`…) ogni valore cade in un solo ramo.
> Vedi anche: if e if-else, Intervalli

## Errori con if {lab 8}
= Due errori che di solito compilano senza errori (con `-Wall` un compilatore recente può avvisare dell'indentazione ingannevole) ma fanno eseguire istruzioni sempre.
```c
int voto = 10;
if (voto >= 18);              // il ; è un'istruzione vuota
printf("Esame passato.\n");   // eseguita SEMPRE
```
- Il `;` dopo la parentesi chiude l'`if`: la `printf` non ne fa parte.
- Senza graffe l'`if` (o l'`else`) controlla solo la prima istruzione che segue; l'indentazione non conta.
- Regola: mettere sempre i blocchi fra graffe, a meno che siano molto brevi ed evidenti.
! Un `else` senza graffe seguito da due `printf`: la seconda viene eseguita sempre, anche per chi ha passato l'esame.
> Vedi anche: if e if-else

## Emersione del massimo {lab 8, lab 9}
= Per trovare il massimo si parte da un candidato e lo si sostituisce ogni volta che se ne trova uno più grande.
```c
int a = 3, b = 7, c = 5;
int max = a;
if (b > max) { max = b; }
if (c > max) { max = c; }
printf("%d\n", max);
```
- Funziona con qualsiasi numero di variabili: con quattro si aggiunge `if (d > max) { max = d; }`.
- Lo stesso schema, con un ciclo, dà il massimo di un array.
! Gli `if` devono essere indipendenti, non `else if`: ogni valore va confrontato con il massimo trovato fin lì.
> Vedi anche: Massimo di un array

# Cicli

## Il ciclo while {20}
= `while (condizione) { … }` ripete il blocco finché la condizione è vera, controllandola prima di ogni giro.
![Il while che stampa i numeri da 0 a 9](figure/prog/ch20_flow_while.png)
```c
int i = 0;             // inizializzazione
while (i < 10) {       // condizione
    printf("%d\n", i);
    i++;               // aggiornamento
}
```
- **Terna**: inizializzazione, condizione, aggiornamento; l'aggiornamento può anche essere un decremento.
- Se la condizione è falsa fin dall'inizio, il blocco non viene mai eseguito.
- Può finire per una condizione di successo (indovinare un PIN), con la variabile inizializzata in modo che il primo controllo sia vero.
! Senza aggiornamento la condizione resta sempre vera: **ciclo infinito** (si interrompe con Ctrl+C).
> Vedi anche: Il ciclo for, Accumulatore e contatore

## Accumulatore e contatore {20, 2, lab 11}
= L'**accumulatore** costruisce un risultato giro dopo giro; il **contatore** conta quanti giri o quanti dati.
```c
int n = 5, i = 1, somma = 0;
while (i <= n) {
    somma = somma + i;   // 1, 3, 6, 10, 15
    i++;
}
```
- Per una somma l'accumulatore parte da 0, l'elemento neutro dell'addizione.
- Media: `somma / (float)count`, con il cast per evitare la divisione intera.
- Se non si è letto nessun dato, `count` è 0 e la media non è definita.
! Un accumulatore non inizializzato prima del ciclo falsa il risultato.
> Vedi anche: Il ciclo while, Somma e conteggio in un array

## Il ciclo for {21, lab 11}
= `for (inizializzazione; condizione; aggiornamento)` è un `while` compatto, adatto quando il numero di giri è noto.
```c
int n = 10;
for (int i = 0; i < 10; i++)     { }  // [0, 10)
for (int i = 0; i <= 40; i += 2) { }  // pari in [0, 40]
for (int i = n; i >= 0; i--)     { }  // da n a 0
```
- L'inizializzazione si esegue una volta; la condizione prima di ogni giro; l'aggiornamento dopo ogni giro.
- Equivale a `{ inizializzazione; while (condizione) { blocco; aggiornamento; } }`.
- `<` esclude l'estremo destro, `<=` lo include; `i -= 7` da 20 dà 20, 13, 6.
- Altri errori: aggiornamento mancante (infinito), cambiare `i` nel corpo, usare `i` dopo il `for`.
! **Off-by-one**: `for (int i = 0; i <= 10; i++)` fa 11 giri, non 10.
> Vedi anche: Il ciclo while, Cicli annidati, Scope e lifetime

## Cicli annidati {21, lab 12}
= Un ciclo dentro il blocco di un altro ciclo: per ogni giro dell'esterno, l'interno ricomincia da capo.
![L'ordine di visita delle 9 coppie](figure/prog/ch21_griglia.png)
```c
for (int r = 0; r < 3; r++) {
    for (int c = 0; c < 3; c++) {
        printf("(%d,%d) ", r, c);
    }
    printf("\n");
}
```
- Il ciclo interno gira «veloce», l'esterno «lento»: 3 × 3 = 9 coppie.
- `r` è visibile anche nel ciclo interno; `c` solo nell'interno.
- Nei pattern a righe l'esterno sceglie la riga, l'interno i caratteri di quella riga.
> Vedi anche: Il ciclo for

## Sentinelle e uscita dai cicli {22, 20, lab 11}
= Il **valore sentinella** è un input speciale che segnala la fine (−1, 0, un'altezza negativa); la **variabile sentinella** è un `bool` che controlla il ciclo.
```c
int sum = 0;
bool continua = true;           // variabile sentinella
while (continua) {
    int number;
    scanf("%d", &number);
    if (number == 0) { continua = false; }  // valore sentinella
    else { sum += number; }
}
```
- Spesso si usano insieme: il valore letto aggiorna la variabile che ferma il ciclo.
- La variabile sentinella chiarisce il motivo dell'uscita, utile se le condizioni sono più di una.
- `break` esce subito dal ciclo; `continue` salta al giro successivo (nel `for` l'aggiornamento si esegue comunque). Nel corso si evitano.
! Il valore sentinella non è un dato: non va sommato né contato.
> Vedi anche: Il ciclo do-while, Quantificatori su una sequenza

## Il ciclo do-while {22}
= `do { … } while (condizione);` esegue il blocco almeno una volta e controlla la condizione dopo.
![while controlla prima, do-while dopo](figure/prog/ch22_while_dowhile.png)
```c
int x, retval;
do {
    printf("Inserisci un numero [1,10]: ");
    retval = scanf("%d", &x);
} while (retval == 0 || !(1 <= x && x <= 10));
```
- Notare il `;` dopo la parentesi finale.
- Uso tipico: richiedere un numero finché è nell'intervallo (con input non numerico questo esempio non termina: la lettera resta da leggere).
- Scelta del ciclo: `for` se il numero di giri è noto, `while` se non lo è (può non girare mai), `do-while` se deve girare almeno una volta.
! Scrivere `!(1 <= x || x <= 10)` non controlla nulla: `1 <= x || x <= 10` è vera per ogni numero (prova con 15).
> Vedi anche: Il ciclo while, Il valore restituito da scanf

## Quantificatori su una sequenza {lab 12}
= «Tutti soddisfano la condizione?» e «Ne esiste almeno uno?» si risolvono con una variabile booleana aggiornata nel ciclo.
```c
bool tutti = true, esiste = false;
int n;
while (1 == scanf("%d", &n) && n != 0) {
    if (!(n > 0)) { tutti = false; }  // basta un controesempio
    if (n > 0) { esiste = true; }     // basta un esempio
}
```
- **Per ogni**: `tutti` parte vera e diventa falsa al primo numero che non va.
- **Esiste**: `esiste` parte falsa e diventa vera al primo numero che va.
- Se i dati sono già in memoria, la variabile si può mettere nella condizione del ciclo per fermarsi subito.
> Vedi anche: Sentinelle e uscita dai cicli

# Array statici

## Array statico {23}
= Un **array** è una fila di elementi dello stesso tipo in celle contigue, raggiunti con un **indice**; nell'**array statico** la lunghezza è decisa alla compilazione.
![Un array di 4 int in memoria](figure/prog/array_memoria.png)
```c
int numeri[4];     // 4 interi sullo stack
numeri[0] = 10;
numeri[1] = 20;    // numeri[2], numeri[3]: indeterminati
#define N 5
int voti[N] = {18, 24, 28, 30, 19};
int zeri[N] = {0}; // tutti a zero
```
- Dichiarazione `tipo nome[dimensione];`, accesso `nome[indice]`; sta sullo stack.
- Con la lista di valori si può omettere la lunghezza: `int voti[] = {18, 19, 24, 21, 30};`.
- Indici validi: da 0 a length − 1, cioè l'intervallo semiaperto [0, length).
- Senza inizializzatore gli elementi di un array locale sono indeterminati.
- Lunghezze e indici si scrivono con `size_t` (`%zu`); le dimensioni fisse con `#define`.
! In un array di 5 elementi la posizione 5 non esiste: l'ultima è 4 (in matematica si conta da 1, in C da 0).
> Vedi anche: Scansione di un array, Intervalli

## Scansione di un array {24, 23, lab 11}
= La **scansione** è un ciclo che visita tutti gli indici validi dell'array, in avanti o all'indietro.
```c
#include <stddef.h>   // size_t e ptrdiff_t
#define N 5
for (size_t i = 0; i < N; i++) { /* v[i] */ }
for (size_t i = N; i > 0; i--) { /* v[i-1] */ }
for (ptrdiff_t i = N - 1; i >= 0; i--) { /* v[i] */ }
```
- In avanti la condizione è `i < length`, non `i <= length`.
- All'indietro con `size_t` si va da length a 1 e si usa `v[i-1]`.
- Oppure si usa `ptrdiff_t`, intero con segno (in `<stddef.h>`, si stampa con `%td`).
! `size_t` è senza segno, non diventa mai negativo: con `size_t i` la condizione `i >= 0` è sempre vera e il ciclo non finisce.
> Vedi anche: Array statico, Somma e conteggio in un array

## Somma e conteggio in un array {24}
= Si scorre l'array aggiornando un accumulatore (per la somma) o un contatore (per gli elementi che soddisfano una condizione).
```c
#define N 5
int voti[N] = {18, 19, 24, 21, 30};
int somma = 0;
for (size_t i = 0; i < N; i++) {
    somma += voti[i];
}
printf("Media: %f\n", somma / (float)N);
```
- Accumulatore e contatore partono da 0.
- Conteggio: `if (temperature[i] > 22.0) { conta++; }` dentro la scansione.
- In matematica la media è (1/N)·Σ a_{i}.
! Senza il cast, `somma / N` è una divisione fra interi e perde i decimali.
> Vedi anche: Accumulatore e contatore, Divisione tra interi e cast

## Massimo di un array {24}
= Si prende il primo elemento come candidato e lo si aggiorna ogni volta che se ne trova uno più grande.
```c
#define N 6
int numeri[N] = {3, 7, 2, 9, 5, 1};
int max = numeri[0];
for (size_t i = 1; i < N; i++) {
    if (numeri[i] > max) { max = numeri[i]; }
}
```
- Il ciclo parte da 1, perché `numeri[0]` è già il candidato.
- **Invariante**: a ogni passo `max` è il massimo di [0, i); alla fine, di tutto [0, length).
! Funziona solo per array non vuoti: con lunghezza 0, `numeri[0]` è un accesso fuori dai limiti.
> Vedi anche: Emersione del massimo, Scansione di un array
