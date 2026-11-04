# 06B_chiamata_funzioni

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
Chiamata a funzione e 
ritorno
Chiamata di funzione nel modello di Von 
Neumann esteso.
1

<!-- pagina 2 -->
Dal modello di Von Neumann al problema delle funzioni
• Il modello di Von Neumann descrive una macchina con:
– memoria unica per dati e istruzioni
– unità di controllo sequenziale
– registri di base (PC, accumulatori)
• Nel modello originario:
– nei primi compilatori, le variabili venivano allocate a indirizzi 
ﬁssi, rendendo le funzioni non rientranti (non potevano 
essere eseguite più volte in parallelo o in modo ricorsivo)
• Questo approccio si rivelò presto troppo limitato per i 
linguaggi di programmazione di alto livello
2

<!-- pagina 3 -->
Lo stack per le funzioni
L’approccio basato su indirizzi ﬁssi e variabili pre-allocate è stato 
abbandonato già alla ﬁne degli anni ’50:
• Bauer e Samelson introducono l’idea di un control stack per gestire le 
chiamate annidate e allocare variabili a indirizzi relativi
• Nel 1958, Edsger Dijkstra formalizza l’uso dello stack come 
meccanismo generale per la ricorsione
• Nel 1961, il Burroughs B5000 realizza per la prima volta in hardware 
questo modello, con uno stack dedicato alle funzioni
• Le architetture moderne forniscono un registro di stack pointer (SP) e 
meccanismi che supportano efﬁcientemente le chiamate di funzione; 
un ulteriore registro può essere usato come frame pointer (FP).
Nel seguito descriveremo le chiamate di funzione attraverso un 
modello di Von Neumann esteso basato su stack frame, SP e FP.
3

<!-- pagina 4 -->
Modello per lo stack
• Per descrivere concretamente le chiamate di 
funzione adotteremo un modello di riferimento 
dello stack:
– lo stack cresce verso indirizzi di memoria decrescenti;
– SP indica il limite corrente dello stack;
– FP fornisce un riferimento stabile al frame della 
funzione attiva;
– rappresentiamo nello stack variabili locali, dati di 
controllo e, quando utile, parametri e valore di ritorno.
• È una convenzione del nostro modello: architetture e 
convenzioni di chiamata reali possono usare registri, 
omettere FP o organizzare diversamente il frame.
4
Direzione di crescita dello stack
Codice
Indirizzi di memoria crescenti
word size
FP
SP
funzione 1
funzione attiva
…
 
main

<!-- pagina 5 -->
Lo stack frame
• Ogni chiamata di funzione riserva una nuova 
regione dello stack, detta stack frame, per 
rappresentare i dati associati a quella 
chiamata.
– Ogni chiamata di funzione ha il proprio stack 
frame
– Chiamate annidate producono frame a loro volta 
impilati: ogni nuova chiamata aggiunge un 
nuovo frame sullo stack
– Al termine della funzione, lo stack frame viene 
rilasciato e la memoria torna disponibile
5
Codice
main
Indirizzi di memoria crescenti
word size
FP
SP
funzione 1
funzione attiva
…

<!-- pagina 6 -->
Lo stack frame
• Quando una funzione viene chiamata, la CPU 
alloca sullo stack uno spazio dedicato alle sue 
variabili e ai dati di supporto: questo spazio si 
chiama stack frame:
– Ogni chiamata di funzione crea un nuovo stack 
frame
– Al termine della funzione, lo stack frame viene 
rilasciato e la memoria torna disponibile
– Lo stack quindi cresce e si riduce a seconda delle 
chiamate di funzione annidate.
6
CPU
CPU
Unità di
controllo
ALU
Registri
R0
R1
IR
PC
SP
FP
• Abbiamo già visto che per gestire lo stack frame, la CPU usa due 
registri dedicati: Stack Pointer (SP) e Frame Pointer (FP)

<!-- pagina 7 -->
Stack Frame
Durante l’esecuzione del programma c’è sempre una funzione attiva, cioè quella il 
cui lo stack frame è in cima allo stack. La CPU deve poter accedere in modo 
ordinato ai dati di questa funzione (parametri e variabili locali) usando FP/SP
7
• Stack Pointer (SP)
–
Indica la cima dello stack*; nel nostro modello delimita la regione di 
memoria occupata nello stack.
–
SP viene aggiornato quando riserviamo o liberiamo spazio nello 
stack. Assumeremo che questo avviene quando le variabili locali 
entrano ed escono dalla visibilità.
• Frame Pointer (FP)
–
Indica l’inizio dello stack frame della funzione attiva
–
È un riferimento stabile per accedere ai dati della funzione.
Assumeremo questa convenzione:
•
i parametri si trovano a un offset positivo (es. FP+8, FP+12…)
•
le variabili locali a un offset negativo (es. FP-4, FP-8…)
–
A differenza di SP, rimane stabile durante la chiamata della funzione
* Convenzione graﬁca adottata: lo stack cresce verso indirizzi decrescenti; per questo, nelle ﬁgure, SP si sposta verso il 
basso quando il frame cresce.
Codice
main
Indirizzi di memoria crescenti
word size
FP
SP
funzione 1
funzione attiva
…

<!-- pagina 8 -->
Evoluzione dello stack: un esempio
• Il programma inizia da main()
• main() chiama sumSquares(2, 3)
• sumSquares() chiama due volte square() (prima con 2, poi con 3)
8
1.
#include <stdio.h>
2.
int square(int x) {
3.
    return x * x;
4.
}
5.
int sumSquares(int a, int b) {
6.
    return square(a) + square(b);
7.
}
8.
int main(void) {
9.
    int res = sumSquares(2, 3);
10.
    printf("Risultato: %d\n", res);
11.
    return 0;
12.
}
Codice
main
Indirizzi di memoria crescenti
word size
All’inizio il main è la funzione attiva, e il suo 
stack frame è in cima (il più basso nella 
nostra rappresentazione, dato che gli 
indirizzi crescono dal basso verso l’alto)
Ogni volta che una variabile locale viene 
dichiarata, SP si sposta (verso indirizzi più 
bassi) per riservarle spazio nello stack frame 
attivo. La regione dello stack compresa tra SP 
ed FP rappresenta l’area di memoria riservata 
alle variabili locali della funzione attiva.
Quando una variabile esce dalla visibilità, assumiamo che il suo spazio 
nello stack frame venga rilasciato, arretrando SP.
Al ritorno dalla funzione, tutto lo spazio riservato al suo frame viene 
rilasciato ripristinando SP.
FP
SP

<!-- pagina 9 -->
Evoluzione dello stack: un esempio
• Il programma inizia da main()
• main() chiama sumSquares(2, 3)
• sumSquares() chiama due volte square() (prima con 2, poi con 3)
9
Indirizzi di memoria crescenti
Codice
main
word size
FP
SP
Codice
main
word size
sum
Squares
FP
SP
Codice
main
word size
sum
Squares
square
FP
SP
Codice
main
word size
sum
Squares
FP
SP
Codice
main
word size
sum
Squares
square
FP
SP
Codice
main
word size
sum
Squares
FP
SP
Codice
main
word size
FP
SP

<!-- pagina 10 -->
Evoluzione dello stack: un esempio
• In qualsiasi momento vi è una singola funzione attiva (corrispondente allo 
stack frame attivo, in cima alla pila), ed una sequenza di funzioni sospese 
(corrispondenti agli stack frames sospesi, non in cima alla pila).
10
Indirizzi di memoria crescenti
Codice
main
word size
FP
SP
Codice
main
word size
sum
Squares
FP
SP
Codice
main
word size
sum
Squares
square
FP
SP
stack frame attivo
stack frames sospesi

<!-- pagina 11 -->
Accesso ai dati del frame tramite FP
• Nel modello di riferimento, FP rimane stabile 
durante l’esecuzione della funzione attiva, e 
quindi permette di referenziare i dati del frame 
mediante offset1 costanti da FP:
– Parametri e valore di ritorno: accessibili con 
offset positivi da FP (es. FP+8, FP+12, …)
– Variabili locali: allocate sotto FP, accessibili 
con offset negativi (es. FP-4, FP-8, …)
– Dati di controllo (FP precedente, return 
address): servono a gestire il ritorno dalla 
chiamata di funzione.
11
word size
retval
control 
data
params
Codice
Indirizzi di memoria crescenti
local 
variables
stack 
frame
FP
SP
1. offset (scostamento): distanza, espressa in byte, rispetto a un indirizzo di riferimento.

<!-- pagina 12 -->
Esempio: parametri, ritorno e variabili
12
word size
int r
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
1.
#include <stdio.h>
2.
3.
int sommaProdotto(int a, int b, int c) {
4.
    int somma = a + b + c;
5.
    int prodotto = a * b * c;
6.
▶   int risultato = somma + prodotto;
7.
    return risultato;
8.
}
9.
10.
int main(void) {
11.
    int x = 2, y = 3, z = 4;
12.
▶   int r = sommaProdotto(x, y, z);
13.
    printf("Risultato: %d\n", r);
14.
}
int x = 2
int y = 3
int z = 4
int a = 2
int b = 3
int c = 4
int somma = 9
int prodotto = 24
int risultato = 33
sommaProdotto
stack frame

<!-- pagina 13 -->
Chiamata e ritorno da funzioni
Vediamo più in dettaglio come funziona, passo passo, la chiamata di 
funzione e il ritorno da funzione:
• Quali dati di controllo servono per poter tornare correttamente al 
chiamante
• Come funziona il passaggio by-value dei parametri
• Come funziona (ad alto livello) il supporto hardware (SP/FP)
La chiamata di funzione si articola quindi in due fasi:
• Prologo: preparazione dello stack frame ed avvio della funzione 
chiamata
• Epilogo: preparazione al ritorno e ripristino dello stato del 
chiamante.
13

<!-- pagina 14 -->
14
local 
variables
word size
chiamata
PC
chiamante
stack frame 
chiamante
Chiamata di funzione
• Il chiamante posiziona i parametri e lo spazio 
per il valore di ritorno sullo stack (o in registri)
Indirizzi di memoria crescenti
• Salva il successore del program counter, e 
sposta PC all’inizio della funzione chiamata 
• Prologo della funzione. 
Copia FP sullo stack
• Imposta FP = SP ed inizia il nuovo stack frame
• Riserva le variabili locali della funzione chiamata
FP
SP
Seguiamo passo-passo la sequenza di chiamata:
• La funzione chiamata accede ai dati del proprio 
frame tramite offset da FP: nel nostro modello, 
i parametri e il valore di ritorno sono a offset 
positivi es. [FP+4], [FP+8]) e le variabili locali 
a offset negativi (es. [FP-0], [FP-4], [FP-8]).

<!-- pagina 15 -->
15
local 
variables
word size
retval
chiamata
params
PC
chiamante
stack frame 
chiamante
Chiamata di funzione
• Il chiamante posiziona i parametri e lo spazio 
per il valore di ritorno sullo stack (o in registri)
Indirizzi di memoria crescenti
• Salva il successore del program counter, e 
sposta PC all’inizio della funzione chiamata 
• Prologo della funzione. 
Copia FP sullo stack
• Imposta FP = SP ed inizia il nuovo stack frame
FP
SP
Seguiamo passo-passo la sequenza di chiamata:
SP
• Riserva le variabili locali della funzione chiamata
• La funzione chiamata accede ai dati del proprio 
frame tramite offset da FP: nel nostro modello, 
i parametri e il valore di ritorno sono a offset 
positivi es. [FP+4], [FP+8]) e le variabili locali 
a offset negativi (es. [FP-0], [FP-4], [FP-8]).

<!-- pagina 16 -->
16
local 
variables
word size
retval
next(PC)
chiamata
params
PC
chiamante
stack frame 
chiamante
Chiamata di funzione
• Il chiamante posiziona i parametri e lo spazio 
per il valore di ritorno sullo stack (o in registri)
Indirizzi di memoria crescenti
• Salva il successore del program counter, e 
sposta PC all’inizio della funzione chiamata 
• Prologo della funzione. 
Copia FP sullo stack
• Imposta FP = SP ed inizia il nuovo stack frame
FP
SP
Seguiamo passo-passo la sequenza di chiamata:
SP
PC
• Riserva le variabili locali della funzione chiamata
• La funzione chiamata accede ai dati del proprio 
frame tramite offset da FP: nel nostro modello, 
i parametri e il valore di ritorno sono a offset 
positivi es. [FP+4], [FP+8]) e le variabili locali 
a offset negativi (es. [FP-0], [FP-4], [FP-8]).

<!-- pagina 17 -->
17
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Chiamata di funzione
• Il chiamante posiziona i parametri e lo spazio 
per il valore di ritorno sullo stack (o in registri)
Indirizzi di memoria crescenti
• Salva il successore del program counter, e 
sposta PC all’inizio della funzione chiamata 
• Prologo della funzione. 
Copia FP sullo stack
• Imposta FP = SP ed inizia il nuovo stack frame
FP
SP
Seguiamo passo-passo la sequenza di chiamata:
SP
• Riserva le variabili locali della funzione chiamata
• La funzione chiamata accede ai dati del proprio 
frame tramite offset da FP: nel nostro modello, 
i parametri e il valore di ritorno sono a offset 
positivi es. [FP+4], [FP+8]) e le variabili locali 
a offset negativi (es. [FP-0], [FP-4], [FP-8]).

<!-- pagina 18 -->
18
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Chiamata di funzione
• Il chiamante posiziona i parametri e lo spazio 
per il valore di ritorno sullo stack (o in registri)
Indirizzi di memoria crescenti
• Salva il successore del program counter, e 
sposta PC all’inizio della funzione chiamata 
• Prologo della funzione. 
Copia FP sullo stack
• Imposta FP = SP ed inizia il nuovo stack frame
stack frame 
chiamato
FP
SP
Seguiamo passo-passo la sequenza di chiamata:
FP
• Riserva le variabili locali della funzione chiamata
• La funzione chiamata accede ai dati del proprio 
frame tramite offset da FP: nel nostro modello, 
i parametri e il valore di ritorno sono a offset 
positivi es. [FP+4], [FP+8]) e le variabili locali 
a offset negativi (es. [FP-0], [FP-4], [FP-8]).

<!-- pagina 19 -->
19
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Chiamata di funzione
• Il chiamante posiziona i parametri e lo spazio 
per il valore di ritorno sullo stack (o in registri)
Indirizzi di memoria crescenti
• Salva il successore del program counter, e 
sposta PC all’inizio della funzione chiamata 
• Prologo della funzione. 
Copia FP sullo stack
• Imposta FP = SP ed inizia il nuovo stack frame
local 
variables
stack frame 
chiamato
FP
SP
Seguiamo passo-passo la sequenza di chiamata:
SP
• Riserva le variabili locali della funzione chiamata
• La funzione chiamata accede ai dati del proprio 
frame tramite offset da FP: nel nostro modello, 
i parametri e il valore di ritorno sono a offset 
positivi es. [FP+4], [FP+8]) e le variabili locali 
a offset negativi (es. [FP-0], [FP-4], [FP-8]).

<!-- pagina 20 -->
20
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Chiamata di funzione
• Il chiamante posiziona i parametri e lo spazio 
per il valore di ritorno sullo stack (o in registri)
Indirizzi di memoria crescenti
• Salva il successore del program counter, e 
sposta PC all’inizio della funzione chiamata 
• Prologo della funzione. 
Copia FP sullo stack
• Imposta FP = SP ed inizia il nuovo stack frame
local 
variables
stack frame 
chiamato
FP
SP
Seguiamo passo-passo la sequenza di chiamata:
• Riserva le variabili locali della funzione chiamata
• La funzione chiamata accede ai dati del proprio 
frame tramite offset da FP: nel nostro modello, 
i parametri e il valore di ritorno sono a offset 
positivi es. [FP+4], [FP+8]) e le variabili locali 
a offset negativi (es. [FP-0], [FP-4], [FP-8]).

<!-- pagina 21 -->
21
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Il ruolo del Frame Pointer
Indirizzi di memoria crescenti
local 
variables
stack frame 
chiamato
FP
SP
Il Frame Pointer (FP) viene posto alla base dello 
stack frame della funzione attiva.
Grazie a questo:
• parametri e variabili locali sono sempre 
accessibili tramite offset da FP, senza bisogno di 
conoscere l’indirizzo assoluto nello stack
• anche se SP cambia durante l’esecuzione della 
funzione, gli offset rispetto a FP restano stabili.
• una funzione può quindi essere eseguita in 
qualunque posizione dello stack
La presenza di un frame distinto per ogni chiamata 
permette di avere contemporaneamente più 
attivazioni della stessa funzione, requisito essenziale 
per la rientranza e la ricorsione.

<!-- pagina 22 -->
22
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Ritorno da funzione
• Il valore di ritorno viene scritto.
Indirizzi di memoria crescenti
• Ripristina il program counter. L’esecuzione 
riprende nel chiamante subito dopo il punto in 
cui la chiamata era stata eseguita
• Ripristina FP dallo stack
• Rimozione dei parametri
local 
variables
• Epilogo della funzione. 
Rilascia tutte le variabili locali della funzione 
ponendo SP = FP
stack frame 
chiamato
SP
Seguiamo passo-passo la sequenza di ritorno:
• A questo punto lo stato è completamente 
ripristinato, e il chiamante ha accesso al valore 
di ritorno
FP

<!-- pagina 23 -->
23
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Ritorno da funzione
• Il valore di ritorno viene scritto.
Indirizzi di memoria crescenti
• Ripristina il program counter. L’esecuzione 
riprende nel chiamante subito dopo il punto in 
cui la chiamata era stata eseguita
• Ripristina FP dallo stack
• Rimozione dei parametri
local 
variables
• Epilogo della funzione. 
Rilascia tutte le variabili locali della funzione 
ponendo SP = FP
stack frame 
chiamato
SP
Seguiamo passo-passo la sequenza di ritorno:
• A questo punto lo stato è completamente 
ripristinato, e il chiamante ha accesso al valore 
di ritorno
FP

<!-- pagina 24 -->
24
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Ritorno da funzione
• Il valore di ritorno viene scritto.
Indirizzi di memoria crescenti
• Ripristina il program counter. L’esecuzione 
riprende nel chiamante subito dopo il punto in 
cui la chiamata era stata eseguita
• Ripristina FP dallo stack
• Rimozione dei parametri
• Epilogo della funzione. 
Rilascia tutte le variabili locali della funzione 
ponendo SP = FP
Seguiamo passo-passo la sequenza di ritorno:
• A questo punto lo stato è completamente 
ripristinato, e il chiamante ha accesso al valore 
di ritorno
FP
SP
stack frame 
chiamato
SP
local 
variables

<!-- pagina 25 -->
25
local 
variables
word size
retval
next(PC)
chiamata
params
PC
chiamante
stack frame 
chiamante
Ritorno da funzione
• Il valore di ritorno viene scritto.
Indirizzi di memoria crescenti
• Ripristina il program counter. L’esecuzione 
riprende nel chiamante subito dopo il punto in 
cui la chiamata era stata eseguita
• Ripristina FP dallo stack
• Rimozione dei parametri
Seguiamo passo-passo la sequenza di ritorno:
• A questo punto lo stato è completamente 
ripristinato, e il chiamante ha accesso al valore 
di ritorno
FP
SP
SP
FP
• Epilogo della funzione. 
Rilascia tutte le variabili locali della funzione 
ponendo SP = FP
FP addr

<!-- pagina 26 -->
26
local 
variables
word size
retval
chiamata
params
PC
chiamante
stack frame 
chiamante
Ritorno da funzione
• Il valore di ritorno viene scritto.
Indirizzi di memoria crescenti
• Ripristina il program counter. L’esecuzione 
riprende nel chiamante subito dopo il punto in 
cui la chiamata era stata eseguita
• Ripristina FP dallo stack
• Rimozione dei parametri
• Epilogo della funzione. 
Rilascia tutte le variabili locali della funzione 
ponendo SP = FP
Seguiamo passo-passo la sequenza di ritorno:
• A questo punto lo stato è completamente 
ripristinato, e il chiamante ha accesso al valore 
di ritorno
FP
SP
SP
PC
next(PC)

<!-- pagina 27 -->
27
local 
variables
word size
retval
chiamata
PC
chiamante
stack frame 
chiamante
Ritorno da funzione
• Il valore di ritorno viene scritto.
Indirizzi di memoria crescenti
• Ripristina il program counter. L’esecuzione 
riprende nel chiamante subito dopo il punto in 
cui la chiamata era stata eseguita
• Ripristina FP dallo stack
• Rimozione dei parametri
• Epilogo della funzione. 
Rilascia tutte le variabili locali della funzione 
ponendo SP = FP
Seguiamo passo-passo la sequenza di ritorno:
• A questo punto lo stato è completamente 
ripristinato, e il chiamante ha accesso al valore 
di ritorno
FP
SP
SP
params

<!-- pagina 28 -->
28
local 
variables
word size
retval
chiamata
PC
chiamante
stack frame 
chiamante
Ritorno da funzione
• Il valore di ritorno viene scritto.
Indirizzi di memoria crescenti
• Ripristina il program counter. L’esecuzione 
riprende nel chiamante subito dopo il punto in 
cui la chiamata era stata eseguita
• Ripristina FP dallo stack
• Rimozione dei parametri
• Epilogo della funzione. 
Rilascia tutte le variabili locali della funzione 
ponendo SP = FP
Seguiamo passo-passo la sequenza di ritorno:
• A questo punto lo stato è completamente 
ripristinato, e il chiamante ha accesso al valore 
di ritorno
FP
SP

<!-- pagina 29 -->
Chiamata e ritorno dalle funzioni
Il modello di chiamata descritto rende espliciti gli elementi logicamente 
necessari a una chiamata di funzione: contesto della funzione, indirizzo di 
ritorno, dati locali e ripristino del chiamante. 
• La chiamata di funzione non corrisponde quindi ad una singola istruzione 
elementare, ma a una sequenza di operazioni coordinate: salvataggio 
dell’indirizzo di ritorno, aggiornamento di SP/FP, salto al nuovo indirizzo, …
• In questo modello ogni chiamata crea un nuovo frame nello stack, che viene 
rimosso al termine della funzione. L’uso combinato di PC, SP e FP consente 
di gestire in modo chiaro i contesti di esecuzione
• NOTA: Le realizzazioni sulle CPU reali introducono differenze nei dettagli (ad 
esempio, in x86 il valore di ritorno è tipicamente posto in un registro), ma la 
logica di base del meccanismo resta la stessa in tutte le architetture di tipo 
Von Neumann esteso.
29

<!-- pagina 30 -->
30
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Record di attivazione e Stack Frame
local 
variables
stack frame 
chiamato
FP
SP
Possiamo descrivere ciò che accade in una 
chiamata di funzione a due diversi livelli di 
astrazione:
• un livello logico, indipendente dall’hardware, 
che considera cosa serve per gestire una 
chiamata di funzione
• un livello implementativo, che descrive come 
tali informazioni sono effettivamente 
memorizzate nello stack
In queste slide useremo record di attivazione per 
indicare l’insieme logico delle informazioni 
associate a una chiamata, e stack frame per la 
regione dello stack usata per rappresentarne una 
parte o la totalità.
record attivazione 
logico del chiamato
Indirizzi di memoria crescenti

<!-- pagina 31 -->
31
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Record di attivazione (definizione logica)
local 
variables
stack frame 
chiamato
FP
SP
Il record di attivazione (activation record) è l’insieme 
dei dati necessari per l’esecuzione di una singola 
chiamata di funzione:
• i parametri 
• le variabili locali
• eventuale valore di ritorno
• i dati di controllo, come
– indirizzo di ritorno al chiamante
– valore del frame pointer precedente
• altri registri o informazioni di stato salvate
È una deﬁnizione logica, indipendente dal modello 
macchina o dalla disposizione ﬁsica dei dati
In generale, un record di attivazione può essere 
pensato come un “contesto di esecuzione completo” 
di una funzione.
record attivazione 
logico del chiamato
Indirizzi di memoria crescenti

<!-- pagina 32 -->
32
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Stack frame (definizione implementativa)
local 
variables
stack frame 
chiamato
FP
SP
Lo stack frame è la porzione contigua di 
memoria nello stack dedicata a una funzione 
attiva.
Lo stack frame comprende la parte inferiore 
del record di attivazione, delimitata da FP e 
SP e gestita dal codice della funzione attiva
Nel nostro modello:
• Le variabili locali (FP + offset negativi) 
appartengono allo stack frame
• I parametri, i dati di controllo e il valore di 
ritorno (FP + offset positivi) rimangono in 
un’area contigua ma esterna allo stack 
frame, gestita dal chiamante
record attivazione 
logico del chiamato
Indirizzi di memoria crescenti

<!-- pagina 33 -->
33
local 
variables
word size
retval
next(PC)
chiamata
FP addr
params
PC
chiamante
stack frame 
chiamante
Record di attivazione e Stack Frame
local 
variables
stack frame 
chiamato
FP
SP
“An activation record is the block of storage used 
for the execution of a procedure.”
- Aho, Sethi, Ullman (Compilers, 1986)
“The stack frame consists of the function’s local 
storage and control information. Arguments are 
placed by the caller just above the frame.”
- Intel x86 ABI (System V)
Nota: Il libro di Paul Deitel non fa questa 
distinzione, e usa solo stack frame (pag. 192).
record attivazione 
logico del chiamato
Indirizzi di memoria crescenti

<!-- pagina 34 -->
Chiamata e ritorno dalle funzioni
• Comprendere la meccanica della chiamata di funzione è 
fondamentale per padroneggiare le funzioni
• Questo meccanismo consente la proprietà di 
indipendenza del codice: una funzione può essere 
eseguita in qualunque posizione dello stack, anche più 
volte contemporaneamente (rientrante, reentrant)
• Esercizio tipico d’esame: rappresentare lo stato dello 
stack e dei registri prima del ritorno di una funzione
34

<!-- pagina 35 -->
Passaggio per valore e per 
riferimento dei parametri
Passaggio (simulato) per 
riferimento, uso dei puntatori nel 
passaggio dei parametri
35

<!-- pagina 36 -->
Funzione per lo scambio di valori
Supponiamo di voler scrivere una 
funzione che scambia (swap) i valori 
di due variabili del chiamante.
Perchè questo codice non é corretto?
36
1.
#include <stdio.h>
2.
3.
void swapSbagliato(int a, int b) {
4.
    int tmp = a;
5.
    a = b;
6.
    b = tmp;
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
    swapSbagliato(x, y);
12.
    printf("x = %d, y = %d\n", x, y);
13.
    // stampa x=10, y=20: nulla è cambiato
14.
}
• In C i parametri sono sempre 
passati per valore. 
• La funzione riceve copie di x e y. 
• Scambiando le copie, i valori 
originali nel chiamante non 
cambiano.

<!-- pagina 37 -->
Il caso dello scambio “sbagliato”
37
word size
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
1.
#include <stdio.h>
2.
3.
void swapSbagliato(int a, int b) {
4.
    int tmp = a;
5.
    a = b;
6.
    b = tmp;
7.
}
8.
9.
int main(void) {
10.
▶   int x = 10, y = 20;
11.
    swapSbagliato(x, y);
12.
    printf("x = %d, y = %d\n", x, y);
13.
    // stampa x=10, y=20: nulla è cambiato
14.
}

<!-- pagina 38 -->
Il caso dello scambio “sbagliato”
38
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
int a = 10
int b = 20
1.
#include <stdio.h>
2.
3.
void swapSbagliato(int a, int b) {
4.
    int tmp = a;
5.
    a = b;
6.
    b = tmp;
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swapSbagliato(x, y);
12.
    printf("x = %d, y = %d\n", x, y);
13.
    // stampa x=10, y=20: nulla è cambiato
14.
}
La chiamata di funzione 
copia i valori di x ed y nei 
parametri attuali a e b

<!-- pagina 39 -->
Il caso dello scambio “sbagliato”
39
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
int a = 10
int b = 20
int tmp = 10
swapSbagliato
stack frame
1.
#include <stdio.h>
2.
3.
void swapSbagliato(int a, int b) {
4.
▶   int tmp = a;
5.
    a = b;
6.
    b = tmp;
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swapSbagliato(x, y);
12.
    printf("x = %d, y = %d\n", x, y);
13.
    // stampa x=10, y=20: nulla è cambiato
14.
}
swapSbagliato inizia ad 
eseguire con le sue copie 
a e b

<!-- pagina 40 -->
Il caso dello scambio “sbagliato”
40
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
int a = 10 20
int b = 20
int tmp = 10
swapSbagliato
stack frame
1.
#include <stdio.h>
2.
3.
void swapSbagliato(int a, int b) {
4.
    int tmp = a;
5.
▶   a = b;
6.
    b = tmp;
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swapSbagliato(x, y);
12.
    printf("x = %d, y = %d\n", x, y);
13.
    // stampa x=10, y=20: nulla è cambiato
14.
}

<!-- pagina 41 -->
Il caso dello scambio “sbagliato”
41
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
int a = 10 20
int b = 20 10
int tmp = 10
swapSbagliato
stack frame
1.
#include <stdio.h>
2.
3.
void swapSbagliato(int a, int b) {
4.
    int tmp = a;
5.
    a = b;
6.
▶   b = tmp;
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swapSbagliato(x, y);
12.
    printf("x = %d, y = %d\n", x, y);
13.
    // stampa x=10, y=20: nulla è cambiato
14.
}
swapSbagliato ha 
scambiato i valori delle 
copie a e b, mentre x ed y 
sono rimasti inalterati

<!-- pagina 42 -->
Il caso dello scambio “sbagliato”
42
word size
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
1.
#include <stdio.h>
2.
3.
void swapSbagliato(int a, int b) {
4.
    int tmp = a;
5.
    a = b;
6.
    b = tmp;
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
    swapSbagliato(x, y);
12.
▶   printf("x = %d, y = %d\n", x, y);
13.
    // stampa x=10, y=20: nulla è cambiato
14.
}
Al ritorno dalla funzione 
swapSbagliato i valori di 
x ed y non sono stati 
scambiati

<!-- pagina 43 -->
Il passaggio per valore
• Il passaggio dei parametri attuali avviene sempre per copia dei valori 
nei parametri formali
Esempio: a e b (parametri formali di swapSbagliato) ricevono i valori 10 e 20 
(parametri attuali o argomenti) copiati da x ed y. 
• La funzione swapSbagliato non può accedere direttamente alle 
variabili di un’altra funzione (main), perchè non gli sono visibili (out of 
scope)
Come risolvere?
• Invece di passare la copia dei valori, passiamo alla funzione gli indirizzi 
delle variabili da modiﬁcare
• Il passaggio degli indirizzi avviene per copia (non ha alcun impatto)
• La funzione riceve quindi dei puntatori, e per dereferenziamento con 
*puntatore modiﬁca i dati originali nel chiamante.
43

<!-- pagina 44 -->
Riassunto puntatori
• Dichiarazione e tipo
int* p; 
p è “puntatore a int” (contiene un indirizzo)
• Operatore di indirizzo &
p = &x; 
in p memorizzo l’indirizzo di x
• Dereferenziamento *
*p 
accede al valore a cui p punta (variabile puntata)
Esempio: *p = 42; // modiﬁca la variabile a cui p punta
• In sintesi: p = indirizzo, *p = valore puntato, &x = indirizzo di x
• Nota: non dereferenziare mai puntatori non inizializzati o NULL
44

<!-- pagina 45 -->
Scambio tramite puntatori
45
word size
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
1.
#include <stdio.h>
2.
3.
void swap(int* pA, int* pB) {
4.
    int tmp = *pA;  // legge il valore puntato da pA
5.
    *pA = *pB;    // scrive nella variabile puntata da pA
6.
    *pB = tmp;    // scrive nella variabile puntata da pB
7.
}
8.
9.
int main(void) {
10.
▶   int x = 10, y = 20;
11.
    swap(&x, &y);  // passo gli INDIRIZZI di x e y
12.
    printf("x = %d, y = %d\n", x, y); 
13.
    // stampa x=20, y=10: scambio riuscito
14.
}

<!-- pagina 46 -->
Scambio tramite puntatori
46
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
FP
SP
int x = 10
int y = 20
int* pA
int* pB
1.
#include <stdio.h>
2.
3.
void swap(int* pA, int* pB) {
4.
    int tmp = *pA;  // legge il valore puntato da pA
5.
    *pA = *pB;    // scrive nella variabile puntata da pA
6.
    *pB = tmp;    // scrive nella variabile puntata da pB
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swap(&x, &y);  // passo gli INDIRIZZI di x e y
12.
    printf("x = %d, y = %d\n", x, y); 
13.
    // stampa x=20, y=10: scambio riuscito
14.
}
La chiamata di funzione 
copia gli indirizzi &x ed &y 
nei parametri attuali pA e 
pB

<!-- pagina 47 -->
Scambio tramite puntatori
47
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
int x = 10
int y = 20
int* pA
int* pB
1.
#include <stdio.h>
2.
3.
void swap(int* pA, int* pB) {
4.
▶   int tmp = *pA;  // legge il valore puntato da pA
5.
    *pA = *pB;    // scrive nella variabile puntata da pA
6.
    *pB = tmp;    // scrive nella variabile puntata da pB
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swap(&x, &y);  // passo gli INDIRIZZI di x e y
12.
    printf("x = %d, y = %d\n", x, y); 
13.
    // stampa x=20, y=10: scambio riuscito
14.
}
swap inizia lo scambio 
usando il dereferenziamento 
di pA e pB
FP
SP
int tmp = 10
swap
stack frame

<!-- pagina 48 -->
Scambio tramite puntatori
48
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
int x = 10 20
int y = 20
int* pA
int* pB
1.
#include <stdio.h>
2.
3.
void swap(int* pA, int* pB) {
4.
    int tmp = *pA;  // legge il valore puntato da pA
5.
▶   *pA = *pB;    // scrive nella variabile puntata da pA
6.
    *pB = tmp;    // scrive nella variabile puntata da pB
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swap(&x, &y);  // passo gli INDIRIZZI di x e y
12.
    printf("x = %d, y = %d\n", x, y); 
13.
    // stampa x=20, y=10: scambio riuscito
14.
}
swap inizia lo scambio 
usando il dereferenziamento 
di pA e pB
FP
SP
int tmp = 10
swap
stack frame

<!-- pagina 49 -->
Scambio tramite puntatori
49
word size
control data
Codice
Indirizzi di memoria crescenti
main
stack frame
int x = 10 20
int y = 20 10
int* pA
int* pB
1.
#include <stdio.h>
2.
3.
void swap(int* pA, int* pB) {
4.
    int tmp = *pA;  // legge il valore puntato da pA
5.
    *pA = *pB;    // scrive nella variabile puntata da pA
6.
▶   *pB = tmp;    // scrive nella variabile puntata da pB
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
▶   swap(&x, &y);  // passo gli INDIRIZZI di x e y
12.
    printf("x = %d, y = %d\n", x, y); 
13.
    // stampa x=20, y=10: scambio riuscito
14.
}
FP
SP
int tmp = 10
swap
stack frame

<!-- pagina 50 -->
Scambio tramite puntatori
50
word size
Codice
Indirizzi di memoria crescenti
main
stack frame
int x = 10 20
int y = 20 10
1.
#include <stdio.h>
2.
3.
void swap(int* pA, int* pB) {
4.
    int tmp = *pA;  // legge il valore puntato da pA
5.
    *pA = *pB;    // scrive nella variabile puntata da pA
6.
    *pB = tmp;    // scrive nella variabile puntata da pB
7.
}
8.
9.
int main(void) {
10.
    int x = 10, y = 20;
11.
    swap(&x, &y);  // passo gli INDIRIZZI di x e y
12.
▶   printf("x = %d, y = %d\n", x, y); 
13.
    // stampa x=20, y=10: scambio riuscito
14.
}
FP
SP
Al ritorno dalla funzione 
swap i valori di x ed y 
sono stati scambiati

<!-- pagina 51 -->
Passaggio per riferimento (simulato)
• In alcuni linguaggi di programmazione (es. Pascal, C++, ma non nel C), 
esiste il passaggio per riferimento (by reference)
– La funzione riceve un riferimento alla variabile del chiamante 
(tipicamente implementato come un puntatore gestito implicitamente dal 
linguaggio), attraverso il quale può accedere e modiﬁcarne il valore.
• In C non esiste il passaggio by reference, é tutto by-value: la funzione 
riceve sempre una copia degli argomenti
• Per avere un effetto analogo al passaggio per riferimento, in C si passa 
l’indirizzo della variabile (cioè un puntatore)
• All’interno della funzione, usando * (dereferenziamento), si modiﬁca il 
contenuto della variabile originale
• Questo è il meccanismo che rende possibili funzioni come scanf, che 
devono modiﬁcare variabili dichiarate nel main o altrove
51

<!-- pagina 52 -->
Osservazioni
• Il passaggio per puntatore non cambia il fatto che in C i 
parametri sono passati solo per valore: quello che viene 
copiato è l’indirizzo
• Però passando un indirizzo la funzione chiamata può leggere 
e scrivere direttamente nella cella di memoria della variabile 
del chiamante (o di qualunque altra area indirizzabile: 
globale, heap, stack) e non è limitata al suo record di 
attivazione.
• Questo permette di oltrepassare le regole della visibilità e 
della visibilità locale imposte dallo stack
52

<!-- pagina 53 -->
Note sul passaggio parametri
Il passaggio degli array, il 
qualiﬁcatore const
53

<!-- pagina 54 -->
Passaggio di un array a funzione
In C un array “si comporta anche come un puntatore al suo 
primo elemento”. Possiamo quindi scrivere
int main() {
    int dati[SZ] = { … };
    fn(dati);
}
⋮
void fn(int* dati) { // oppure: void fn(int dati[]) { … }
    … 
}
L’esempio funziona ma una un problema.
54

<!-- pagina 55 -->
Passaggio di un array a funzione
• Il solo puntatore ai dati non è sufﬁciente a conoscere la dimensione 
dell’array 
• Di conseguenza, il passaggio di un array tipicamente comporta il 
passaggio di due parametri
int main() {
    int dati[SZ] = { … };
    fn(SZ, dati);
}
⋮
void fn(size_t datiLen, int dati[]) { 
    // posso accedere a dati nell’intervallo [0, datiLen)
}
55

<!-- pagina 56 -->
Passaggio di dati costanti
• Se una funzione non deve modiﬁcare l’array ricevuto, lo può qualiﬁcare 
come const (cioé in sola lettura).
• Il compilatore emette un errore se un dato const viene modiﬁcato 
oppure passato ad un’altra funzione che si aspetta dati non-const.
int main() {
    int dati[SZ] = { … };
    fn(SZ, dati);
}
⋮
void fn(size_t datiLen, const int dati[]) { 
    // posso accedere a dati in sola lettura
}
56

<!-- pagina 57 -->
Passaggio di dati costanti
• Per chiarire il contratto della funzione (che cosa modiﬁca e cosa no) è 
possibile dichiarare const tutte le variabili che vengono solo lette e mai 
scritte
int main() {
    int dati[SZ] = { … };
    fn(SZ, dati);
}
⋮
void fn(const size_t datiLen, const int dati[]) { 
    // posso accedere a dati in sola lettura
    // la funzione non cambia mai il valore datiLen
}
57

<!-- pagina 58 -->
Passaggio di stringhe
In C una stringa è un array di char terminato da '\0'
• Anche per le stringhe il parametro è un puntatore a char
• A differenza degli array, se la stringa segue la convenzione C di essere 
NUL-terminated, non serve passare la lunghezza: la funzione chiamata 
può scorrere la stringa per trovare il terminatore '\0'
void stampa(const char* s) {
    printf("%s\n", s);
}
⋮
stampa("ciao");     // stringa costante
stampa(buffer);     // array di char
• Le stringhe sono un caso particolare di array per il quale la terminazione 
si può autodeterminare cercando il terminatore '\0'
58

<!-- pagina 59 -->
Funzioni di libreria in <string.h>
Il C mette a disposizione molte funzioni standard per le stringhe
• size_t strlen(const char* str);
Ritorna la lunghezza della stringa (esclude '\0').
• int strcmp(const char* s1, const char* s2);
Confronta due stringhe in ordine lessicograﬁco (ordine del 
dizionario). Ritorna <0 se s1 precede s2, =0 se uguali, >0 se 
s1 segue s2.
• char* strncpy(char* dest, const char* src, size_t count);
Copia al più count caratteri (incluso terminatore) da src a 
dest.
59

<!-- pagina 60 -->
Asserzioni e <assert.h>
• Un’asserzione è un’affermazione (sotto forma di espressione 
booleana) che deve essere sempre vera se il programma è 
corretto
• Serve a rendere esplicite le ipotesi che il programmatore 
assume sullo stato delle variabili
• Se un’asserzione non risulta vera, allora il programma termina 
con un errore → Serve per una veriﬁca di integrità delle 
assunzioni del codice, non per controllare gli input dell’utente
60

<!-- pagina 61 -->
Asserzioni e <assert.h>
• Il linguaggio C dispone della funzione* assert, deﬁnita in 
<assert.h>, che valuta un’espressione booleana expr
assert(expr);
• se expr è true, non accade nulla;
• se expr è false, il programma termina mostrando:
– l’espressione violata,
– il ﬁle e la linea in cui è fallita.
Durante la compilazione le asserzioni possono essere disattivate 
passando al compilatore l’opzione -DNDEBUG
61
* assert è tipicamente una macro, non una funzione, così da poter segnalare il ﬁle e 
la linea esatta dell’errore, ma non vedremo questo dettaglio.

<!-- pagina 62 -->
Esempi di asserzioni
Pre-condizione su puntatori/lunghezze:
1.
#include <assert.h>
2.
#include <stddef.h>
3.
4.
void processa_array(size_t aLen, const int* a) {
5.
    // se devo leggere a[], il puntatore dev'essere valido
6.
    assert(aLen == 0 || a != NULL);   
7.
    // ... 
8.
}
62

<!-- pagina 63 -->
Esempi di asserzioni
Invariante di ciclo (indice entro limiti):
1.
#include <assert.h>
2.
#include <stddef.h>
3.
4.
size_t conta_zeri(size_t aLen, const int* a) {
5.
    size_t cnt = 0;
6.
    for (size_t i = 0; i < aLen; ++i) {
7.
        assert(i < aLen);  // i resta nel dominio [0, aLen)
8.
        if (a[i] == 0) 
9.
            cnt++;
10.
    }
11.
    return cnt;
12.
}
63

<!-- pagina 64 -->
Esempi di asserzioni
Post-condizione:
1.
#include <assert.h>
2.
3.
void order_pair(int* a, int* b) {
4.
    if (*a > *b) { 
5.
        int temp = *a; 
6.
        *a = *b; 
7.
        *b = temp; 
8.
    }
9.
    assert(*a <= *b);  // post: la coppia è ordinata non decrescente
10.
}
64

<!-- pagina 65 -->
Esempi di asserzioni
Post-condizioni forti (esempio: massimo tra due numeri)
1.
#include <assert.h>
2.
int massimo(int a, int b) {
3.
    int m;
4.
    // Calcola il massimo tra a e b
5.
    if (a > b) {
6.
        m = a;
7.
    } 
8.
    else {
9.
        m = b;
10.
    }
11.
    // Post-condizione: m non è minore di nessuno dei due valori
12.
    assert(m >= a && m >= b);
13.
    // Post-condizione: m coincide con uno dei due valori di ingresso
14.
    assert(m == a || m == b);
15.
    return m;
16.
}
65

<!-- pagina 66 -->
Esempi di asserzioni
Coerenza tra argomenti della funzione:
1.
#include <assert.h>
2.
#include <stdbool.h>
3.
// usa *str solo se have_str é vero, altrimenti str deve essere NULL
4.
void usa_stringa(bool have_str, const char* str) {
5.
    assert(( have_str && str != NULL) ||
6.
           (!have_str && str == NULL));
7.
    // ... 
8.
}
• Si usa assert() per esprimere verità che devono sempre valere nel 
codice (precondizioni, invarianti, postcondizioni, stati impossibili), 
senza effetti collaterali nelle espressioni
• Per gli errori di input dell’utente, invece, si fanno normali controlli 
che gestiscono eventuali errori (messaggi, ripetizione input, ecc…)
66
