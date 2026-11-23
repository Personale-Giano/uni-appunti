# 08A_memoria_dinamica

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
Memoria Dinamica
Gestione non automatica della memoria, 
lo heap e le funzioni malloc/free

<!-- pagina 2 -->
Perché lo stack non basta
• Tutte le funzioni in C usano lo stack per gestire variabili e 
parametri
• Le variabili sono automatiche e seguono la durata dello stack 
frame in cui sono dichiarate: esistono solo ﬁnché il blocco 
(scope) in cui sono dichiarate non completa
• Lo stack ha dimensione limitata (tipicamente pochi MB) e 
viene gestito in modo automatico
• Molti problemi richiedono dati che vivano più a lungo della 
funzione che li dichiara, o di dimensione non nota a priori
2

<!-- pagina 3 -->
Un problema “impossibile”
Problema: Scrivere una funzione leggiArray che legga da input un 
numero n, poi n interi, e inﬁne restituisca la sequenza letta al chiamante
• Il chiamante non sa quale sia la dimensione n, solo la funzione 
leggiArray lo conosce e può allocare l’array
• Ma se leggiArray alloca l’array sullo stack, l’array viene deallocato al 
ritorno
3
1.
int* leggiArraySbagliato(size_t* out_n) {
2.
    size_t n;
3.
    scanf("%zu", &n);
4.
    int a[n];    // VLA su stack (vita limitata al frame)
5.
    for (size_t i = 0; i < n; ++i) 
6.
        scanf("%d", &a[i]);
7.
    *out_n = n;
8.
    return a;    // ERRORE: l’array a sparisce al ritorno
9.
}

<!-- pagina 4 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
▶   size_t aLen;
15.
    int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
4
Codice
??
word size
size_t aLen
main
Indirizzi di memoria crescenti
>./leggi_array_sb

<!-- pagina 5 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
5
Codice
??
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
??
main
int* a

<!-- pagina 6 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
▶   size_t n;
6.
    scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
6
Codice
??
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
??
int* a
main
address-of aLen
??
control data
retval
leggi
Array
Sbagliato
size_t* out_n
size_t n
int*

<!-- pagina 7 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
▶   scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
7
Codice
??
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
3
??
int* a
main
address-of aLen
3
control data
retval
leggi
Array
Sbagliato
size_t* out_n
size_t n
int*

<!-- pagina 8 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
▶   int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
8
Codice
??
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
3
??
int* a
main
address-of aLen
3
control data
retval
leggi
Array
Sbagliato
size_t* out_n
size_t n
int*
a[2] = ??
a[1] = ??
a[0] = ??
int a[3]

<!-- pagina 9 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
▶   for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
9
Codice
??
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
3
??
int* a
main
address-of aLen
3
control data
retval
leggi
Array
Sbagliato
size_t* out_n
size_t n
int*
a[2] = ??
a[1] = ??
a[0] = ??
int a[3]
size_t i
0

<!-- pagina 10 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
▶   *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
10
Codice
?? 3
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
3
10 20 30
??
int* a
main
address-of aLen
3
control data
retval
leggi
Array
Sbagliato
size_t* out_n
size_t n
int*
a[2] = ?? 30
a[1] = ?? 20
a[0] = ?? 10
int a[3]

<!-- pagina 11 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
▶   return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
11
Codice
?? 3
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
3
10 20 30
??
int* a
main
address-of aLen
3
control data
address-of a
leggi
Array
Sbagliato
size_t* out_n
size_t n
int*
a[2] = ?? 30
a[1] = ?? 20
a[0] = ?? 10
int a[3]

<!-- pagina 12 -->
Ritorno di puntatori sullo stack
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArraySbagliato(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int a[n]; // su stack (vita limitata al frame)
8.
    for (size_t i = 0; i < n; ++i)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a; // ERRORE
12.
}
13.
int main(void) {
14.
    size_t aLen;
15.
▶   int* a = leggiArraySbagliato(&aLen);
16.
    for (size_t i = 0; i < aLen; i++)
17.
        printf("a[%zu] = %d\n", i, a[i]);
18.
}
12
Codice
?? 3
word size
size_t aLen
Indirizzi di memoria crescenti
>./leggi_array_sb
3
10 20 30
dangling-ptr
int* a
main
??
??
??
Il puntatore ritornato appartiene ad 
uno stack frame che è stato deallocato 
al ritorno della funzione. L’area di 
memoria non è più valida.

<!-- pagina 13 -->
I limiti dello stack
• Se una funzione ritorna un puntatore a una variabile locale che si 
trovava nel suo stack frame, l’indirizzo non è più valido dopo il 
return (lo stack frame è stato deallocato)
• Si dice che il puntatore “rimane appeso” (dangling pointer)
• Anche gli array VLA sono sullo stack, e scompaiono alla 
deallocazione dello stack frame dove sono dichiarati
• Quindi non si può mai ritornare un array o un puntatore ad una 
variabile locale allocata nello stack frame della funzione 
ritornante
• Serve un’area di memoria diversa, che non segue la gestione 
automatica dello stack
13

<!-- pagina 14 -->
Lo heap e la gestione dinamica
• Lo heap è un’area di memoria gestita manualmente dal 
programmatore
• L’allocazione avviene tramite funzioni di libreria (malloc, calloc, 
realloc)
• La deallocazione è esplicita (free)
Questa area di memoria si dice dinamica✽ perché:
• non è ﬁssata a compile-time come le variabili globali o statiche 
(stringhe letterali, array const, …);
• non è allocata automaticamente a runtime come lo stack;
• ma viene allocata e liberata “su richiesta” dal programma durante 
l’esecuzione.
14
✽ Negli anni ’70, quando il termine dinamico è stato scelto, voleva dire “allocato a runtime”, in contrasto 
con statico, cioè allocato a compile-time. Oggi diremmo piuttosto “on-demand” o “gestito dal programma”.

<!-- pagina 15 -->
Malloc/free nel modello della memoria
Modello generale (sempliﬁcato) della memoria: 
suddividiamo i seguenti segmenti distinti
• Code segment: contiene le istruzioni del 
programma
• Data segment: contiene variabili globali e 
statiche
• Heap: area di memoria dinamica, per convenzione 
assumiamo che cresca verso l’alto
• Stack: area delle variabili automatiche, cresce 
verso il basso
Codice e dati statici sono ﬁssi per tutta l’esecuzione, 
stack e heap condividono lo spazio libero
15
Codice
word size
Indirizzi di memoria crescenti
stack
heap
FP
SP
memoria 
libera
Data

<!-- pagina 16 -->
Allocazione nello heap
#include <stdlib.h>
void* malloc(size_t sz);
• La funzione malloc(), deﬁnita in <stdlib.h>, alloca sz byte contigui 
nello heap, e restituisce un puntatore al primo byte del blocco allocato
• Se la memoria non è disponibile, malloc restituisce NULL
• I byte sono non inizializzati
• void* è un puntatore a una zona di memoria a cui non è ancora stato 
assegnato un tipo. Il tipo si dà tramite assegnamento o cast
Esempio:
1. int* a = malloc(n * sizeof(int));
2. if (a == NULL) {
3.    printf("Memoria insufficiente\n");
4. }
16

<!-- pagina 17 -->
Deallocazione dallo heap
#include <stdlib.h>
void free(void* ptr);
• Libera la memoria allocata da malloc()
• Dopo la free, l’indirizzo ptr non è più utilizzabile: é buona pratica 
azzerarlo
Esempio:
1. free(a);
2. a = NULL;
Regola: ogni malloc deve avere un free corrispondente
17

<!-- pagina 18 -->
Allocazione e deallocazione dallo heap
Vediamo un esempio dal punto di vista del modello della memoria:
int main(void) {
    ...
1.
    int* p1 = malloc(20);
2.
    int* p2 = malloc(32);
3.
    double* p3 = malloc(16);
4.
    free(p2); p2 = NULL;
5.
    char* p4 = malloc(20);
6.
    free(p1); p1 = NULL;
    ...
}
18

<!-- pagina 19 -->
Malloc/free nel modello della memoria
19
Codice
word size
heap block 1
heap
memoria 
libera
Data
int* p1 = 
 malloc(20);
address
int* p1
??
int* p2
??
double* p3
??
char* p4
Codice
word size
heap block 1
memoria 
libera
Data
int* p2 = 
 malloc(32);
address
address
??
??
heap block 2
Codice
word size
heap block 1
memoria 
libera
Data
double* p3 = 
 malloc(16);
address
address
address
??
heap block 2
heap block 3
Codice
word size
heap block 1
memoria 
libera
Data
free(p2);
p2 = NULL;
address
NULL
address
??
heap block 3
Codice
word size
heap block 1
memoria 
libera
Data
char* p4 = 
 malloc(20);
address
NULL
address
address
heap block 4
heap block 3
Codice
word size
memoria 
libera
Data
free(p1);
p1 = NULL;
NULL
NULL
address
address
heap block 4
heap block 3

<!-- pagina 20 -->
Allocazione di un array nello heap
int* a = malloc(n * sizeof(int));
Consideriamo l’allocazione di un array di n elementi di tipo intero:
• Un array è una sequenza di valori dello stesso tipo memorizzati 
in posizioni contigue di memoria
• Quindi la dimensione in byte di un area di memoria contigua con n 
elementi di tipo int è
n * sizeof(int)
• Nel linguaggio C l’allocazione di memoria dinamica è al livello più 
elementare possibile: si riservano sequenze contigue e non 
inizializzate di bytes, poi si devono inizializzare esplicitamente
20

<!-- pagina 21 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n *sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
▶   size_t aLen;
16.
    int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
21
Codice
??
word size
size_t aLen
main
Indirizzi di memoria crescenti
>./leggi_array

<!-- pagina 22 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
22
Codice
??
??
word size
size_t aLen
main
int* a
Indirizzi di memoria crescenti
>./leggi_array

<!-- pagina 23 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
▶   size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
23
Codice
??
??
word size
size_t aLen
main
address-of aLen
int* a
??
size_t* out_n
control data
Indirizzi di memoria crescenti
retval
size_t n
int*
leggi
Array
>./leggi_array

<!-- pagina 24 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
▶   scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
24
Codice
??
??
word size
size_t aLen
main
address-of aLen
int* a
3
size_t* out_n
control data
Indirizzi di memoria crescenti
retval
size_t n
int*
leggi
Array
>./leggi_array
3

<!-- pagina 25 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
▶   int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
25
Codice
??
??
3 * sizeof(int) 
bytes
word size
size_t aLen
main
address-of aLen
int* a
3
size_t* out_n
control data
leggi
Array
Indirizzi di memoria crescenti
retval
size_t n
address
??
??
??
int*
int* a
>./leggi_array
3

<!-- pagina 26 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
▶   for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
26
Codice
??
??
3 * sizeof(int) 
bytes
word size
size_t aLen
main
address-of aLen
int* a
3
size_t* out_n
control data
Indirizzi di memoria crescenti
retval
size_t n
address
??
??
??
size_t i
0
int*
int* a
leggi
Array
>./leggi_array
3

<!-- pagina 27 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
▶   *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
27
Codice
??
??
3 * sizeof(int) 
bytes
word size
size_t aLen
main
address-of aLen
int* a
3
size_t* out_n
control data
Indirizzi di memoria crescenti
retval
size_t n
address
?? 10
?? 20
?? 30
int*
int* a
leggi
Array
>./leggi_array
3
10 20 30

<!-- pagina 28 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
▶   return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
28
Codice
?? 3
??
3 * sizeof(int) 
bytes
word size
size_t aLen
main
address-of aLen
int* a
3
size_t* out_n
control data
Indirizzi di memoria crescenti
retval=address
size_t n
address
10
20
30
int*
int* a
leggi
Array
>./leggi_array
3
10 20 30

<!-- pagina 29 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
▶   int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
29
Codice
3
address
3 * sizeof(int) 
bytes
word size
size_t aLen
main
int* a
Indirizzi di memoria crescenti
10
20
30
>./leggi_array
3
10 20 30

<!-- pagina 30 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
    int* a = leggiArray(&aLen);
17.
▶   for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
30
Codice
3
address
3 * sizeof(int) 
bytes
word size
size_t aLen
main
int* a
Indirizzi di memoria crescenti
10
20
30
size_t i
0
>./leggi_array
3
10 20 30

<!-- pagina 31 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
    int* a = leggiArray(&aLen);
17.
▶   for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
    free(a); a = NULL;
20.
}
31
Codice
3
address
3 * sizeof(int) 
bytes
word size
size_t aLen
main
int* a
Indirizzi di memoria crescenti
10
20
30
size_t i
3
>./leggi_array
3
10 20 30
a[0] = 10
a[1] = 20
a[2] = 30

<!-- pagina 32 -->
Malloc/free nel modello della memoria
1.
#include <stdlib.h>
2.
#include <stdio.h>
3.
4.
int* leggiArray(size_t* out_n) {
5.
    size_t n;
6.
    scanf("%zu", &n);
7.
    int* a = malloc(n * sizeof(int));
8.
    for (size_t i = 0; i < n; i++)
9.
        scanf("%d", &a[i]);
10.
    *out_n = n;
11.
    return a;
12.
}
13.
14.
int main(void) {
15.
    size_t aLen;
16.
    int* a = leggiArray(&aLen);
17.
    for (size_t i = 0; i < aLen; i++)
18.
        printf("a[%zu] = %d\n", i, a[i]);
19.
▶   free(a); a = NULL;
20.
}
32
Codice
3
NULL
word size
size_t aLen
main
int* a
Indirizzi di memoria crescenti
>./leggi_array
3
10 20 30
a[0] = 10
a[1] = 20
a[2] = 30

<!-- pagina 33 -->
Gestione manuale della memoria dinamica
• La memoria dinamica è gestita solo tramite puntatori
• Ogni chiamata a malloc() restituisce l’indirizzo di un blocco di memoria 
(heap block) nello heap, che rimane allocato ﬁno alla corrispondente 
free()
• Se ci si dimentica di liberarlo, il blocco resta nello heap ﬁno alla 
terminazione del programma
• Un blocco allocato e poi “dimenticato” (non più referenziabile, ma non 
deallocato) costituisce una perdita di memoria (memory leak)
“Chi semina malloc()s*, raccoglie memory leaks”
• Ogni blocco allocato è una responsabilità: chi lo crea deve anche 
liberarlo. La corretta gestione dello heap nel linguaggio C è quindi 
legata all’attenzione e alla disciplina del programmatore
33
* malloc senza free corrispondente, ovviamente.

<!-- pagina 34 -->
Errori comuni
Allocare senza liberare:
1.
void f(void) {
2.
    int* a = malloc(100 * sizeof(int));
3.
    // uso dell’array
4.
} // MEMORY LEAK: manca free(a)
• Il blocco resta occupato ﬁno al termine del programma
• Se l’errore si ripete in un ciclo, la memoria progressivamente si 
esaurisce
• Difﬁcile da notare: nessun crash immediato, ma crescita della RAM 
usata dal programma
Per il linguaggio C esistono strumenti di diagnosi (es: Valgrind) che 
possono essere usati per rintracciare i memory leaks
34

<!-- pagina 35 -->
Errori comuni
Usare un puntatore dopo free():
1.
int* p = malloc(sizeof(int));
2.
*p = 5;
3.
free(p);
4.
printf("%d\n", *p); // ERRORE: uso di memoria già liberata
• Dopo la deallocazione, p è un dangling pointer: contiene l’indirizzo di 
una zona di memoria che non è più valida
• L’accesso ha comportamento indeﬁnito: il programma può 
apparentemente funzionare, produrre risultati errati, corrompere dati 
oppure terminare.
• Difﬁcile da diagnosticare, quindi è buona pratica assegnare NULL ai 
puntatori deallocati
free(p); p = NULL; // evita l’uso accidentale del dangling pointer
35

<!-- pagina 36 -->
Errori comuni
Deallocare due volte lo stesso blocco:
1.
int* p = malloc(sizeof(int));
2.
free(p);
3.
free(p); // ERRORE: doppia free
• La seconda free() tenta di restituire allo heap una zona già restituita
• Effetto: crash immediato o corruzione della struttura interna dello heap
• Di nuovo, è buona pratica assegnare NULL ai puntatori deallocati
free(p); p = NULL; // evita l’uso accidentale del dangling pointer
36

<!-- pagina 37 -->
Errori comuni
Fare assunzioni sugli indirizzi della memoria allocata:
1.
int* p1 = malloc(sizeof(int));
2.
int* p2 = malloc(sizeof(int));
3.
p1[0] = 10;
4.
p1[1] = 20; // ERRORE: non sto accedendo a p2, non c’è alcuna garanzia
5.
            // che p1 e p2 siano adiacenti in memoria
• La garanzia di contiguità della memoria allocata è per una singola 
malloc: chiamate multiple a malloc non garantiscono che i puntatori 
ritornati siano contigui (sono quasi sicuramente NON contigui)
• La gestione dello heap è molto articolata (non la tratteremo)
37

<!-- pagina 38 -->
Errori comuni
Perdere l’indirizzo del blocco prima di liberarlo:
1.
int* p = malloc(10 * sizeof(int));
2.
p = malloc(20 * sizeof(int)); // MEMORY LEAK il primo blocco è perso per sempre
• Il puntatore originale è stato sovrascritto senza deallocarlo
• Il blocco iniziale rimane allocato ma irraggiungibile: memory leak
Accedere a memoria non inizializzata
1.
int* a = malloc(5 * sizeof(int));
2.
printf("%d", a[0]); // ERRORE: a[0] non è stato inizializzato
• malloc() riserva il blocco di memoria ma non ne inizializza il contenuto. 
Prima di leggere un elemento dobbiamo assegnargli un valore; ﬁno ad 
allora il suo valore è indeterminato.
38

<!-- pagina 39 -->
Considerazioni
• In C, è consuetudine allocare nello heap tutti i dati di 
dimensione non nota a priori (array, strutture, matrici, ecc.)
• Lo stack viene invece riservato a:
– variabili locali di piccole dimensioni
– puntatori, indici, contatori
– eventuali array di dimensione ﬁssa o limitata
• Nei primi standard del C (antecedenti al C99) i VLA non 
esistevano, quindi anche per piccoli array di dimensione 
variabile era necessario ricorrere allo heap
39

<!-- pagina 40 -->
Selezione con copia nello heap
Tecniche per l’uso della memoria 
dinamica su array
40

<!-- pagina 41 -->
Dal modello statico al modello dinamico
• Alcuni problemi (come selezionare gli elementi che 
soddisfano una condizione) dipendono dai dati: la 
dimensione del risultato non è un parametro noto a priori.
• Negli array statici la dimensione è nota in compilazione o 
ﬁssata all’inizio. Per gestire quindi selezioni abbiamo 
introdotto il modello dimensione / capacità:
int a[CAP]; size_t aLen;  // 0 ≤ aLen ≤ CAP
• Con lo heap possiamo riformulare il problema della 
selezione in una forma più semplice
41

<!-- pagina 42 -->
Selezione
• La selezione è un problema prototipale di costruzione di una 
nuova sequenza “ﬁltrata”
• Selezione: Dato un array b di lunghezza bLen e una condizione 
logica sugli elementi Cond(⋅), la selezione copia in un altro array 
a tutti e soli gli elementi b[i] che soddisfano Cond(b[i]), 
mantenendo l’ordine degli elementi originali. Formalmente
a = { b[i] | i∈[0,bLen) ∧ Cond(b[i]) }
• La dimensione dell’array a non è nota senza prima una scansione 
lineare degli elementi di b
• Serve quindi un algoritmo che calcola aLen e alloca un array della 
misura esatta
42

<!-- pagina 43 -->
Un approccio in tre fasi
Per risolvere il problema della selezione serve un algoritmo articolato 
in tre fasi logiche, ciascuna con uno scopo preciso
1. Calcolo della dimensione: Si scorre l’array di partenza b senza 
effettuare copie, contando quanti elementi soddisfano Cond(b[i]). Il 
risultato count è la lunghezza esatta del nuovo array che conterrà 
solo gli elementi selezionati
2. Allocazione: alloca nello heap un array a di count elementi
3. Selezione e copia: si ripete la scansione dell’array sorgente b, e per 
ogni elemento b[i] che veriﬁca Cond(b[i]), lo si copia nella prima 
posizione libera dell’array a (serve quindi un indice di copia j per a)
Alla ﬁne, a contiene esattamente e nell’ordine originale tutti gli 
elementi selezionati. 
43

<!-- pagina 44 -->
Un approccio in tre fasi
44
(1) Calcolo della dimensione.
Stabilisce quanto spazio serve ma non 
produce ancora il risultato
(2) Allocazione.
Riserva lo spazio nello heap
(3) Selezione e copia.
Realizza la selezione e la copia nella 
memoria allocata

<!-- pagina 45 -->
Selezione e copia in tre fasi
Traduciamo in C il ragionamento a tre fasi
• selectCopy: copia in un nuovo array heap gli elementi di b 
che soddisfano una condizione Cond(b[i]) con lo schema a tre 
fasi: conta, alloca, seleziona
– Input: array b di lunghezza bLen
– Output: ritorna array a allocato nello heap, di lunghezza *out_len
– Caso limite: Se non ci sono elementi selezionati, ritorna NULL e 
mette *out_len a zero.
• Il chiamante è responsabile dell’array restituito e deve 
liberarne la memoria con free() quando non serve più
45

<!-- pagina 46 -->
Selezione e 
copia in tre 
fasi
1.
int* selectCopy(size_t bLen, const int b[], size_t* out_len) {
2.
    assert(bLen == 0 || b != NULL);
3.
    assert(out_len != NULL);
4.
    *out_len = 0;
5.
    int* a = NULL;
6.
7.
    // 1) Calcolo della dimensione
8.
    size_t count = 0;
9.
    for (size_t i = 0; i < bLen; i++)
10.
        if (Cond(b[i]))
11.
            count++;
12.
13.
    // 2) Allocazione
14.
    if (count > 0) {
15.
        a = malloc(count * sizeof(int));
16.
        if (a != NULL) {
17.
            // 3) Selezione e copia
18.
            size_t j = 0;
19.
            for (size_t i = 0; i < bLen; i++) {
20.
                if (Cond(b[i])) {
21.
                    a[j] = b[i];
22.
                    j++;
23.
                }
24.
            }
25.
            assert(count == j);
26.
            *out_len = count;
27.
        }
28.
    }
29.
    return a;
30.
}
46

<!-- pagina 47 -->
Selezione e 
copia in tre 
fasi
1.
#include <stdio.h>
2.
#include <stdbool.h>
3.
#include <stddef.h>
4.
#include <stdlib.h>
5.
#include <assert.h>
6.
7.
// Predicato
8.
bool Cond(int x) { return x % 2 == 0; }
9.
10.
// Prototipo
11.
int* selectCopy(size_t bLen, const int b[], size_t* out_len);
12.
13.
int main(void) {
14.
    #define B_LEN 5
15.
    const int b[B_LEN] = {12, 1, 3, 4, 8};
16.
17.
    size_t aLen = 0;
18.
    int* a = selectCopy(B_LEN, b, &aLen);
19.
20.
    // Stampa del risultato
21.
    printf("Selezionati %zu elementi:\n", aLen);
22.
    for (size_t i = 0; i < aLen; i++) {
23.
        printf("a[%zu] = %d\n", i, a[i]);
24.
    }
25.
26.
    // Responsabilità della memoria: il chiamante libera l’array
27.
    free(a); a = NULL;
28.
}
47

<!-- pagina 48 -->
Responsabilità della memoria (ownership)
• Quando una funzione alloca memoria dinamica con malloc, 
diventa responsabile della gestione del blocco
• La funzione può trasferire la responsabilità al chiamante, 
restituendo il puntatore al blocco allocato
• Il chiamante, a sua volta, può trasferire la responsabilità di 
gestione del blocco
• Per evitare perdite di memoria, l’ultimo punto del codice che 
usa il blocco ne dovrà rilasciare la memoria con free() quando il 
blocco non serve più
• Si parla di responsabilità della memoria (ownership): una 
memoria allocata deve sempre avere un corrispondente punto 
del programma che ha la responsabilità di deallocarla
48

<!-- pagina 49 -->
Un esempio dalla libreria: strdup
• La funzione di libreria strdup (in <string.h>) crea una copia in 
memoria heap di una stringa (terminatore incluso), e restituisce il 
puntatore al chiamante
• Il chiamante è proprietario e ha la responsabilità di deallocare il 
blocco con free
49
1.
#include <stdio.h>
2.
#include <string.h>
3.
#include <stdlib.h>
4.
5.
int main(void) {
6.
    const char* src = "Programmazione 1";
7.
    char* copy = strdup(src);  // copia nello heap
8.
    assert(copy != NULL);
9.
    printf("Originale: %s\nCopia: %s\n", src, copy);
10.
    free(copy); copy = NULL; // il chiamante è responsabile della deallocazione
11.
}

<!-- pagina 50 -->
Considerazioni
• Più avanti (Programmazione II, Algoritmi) la memoria 
dinamica verrà usata in modo sistematico per costruire 
strutture dati dinamiche (liste, alberi, graﬁ), cioè 
strutture a dimensione variabile e con organizzazione 
della memoria non contigua
50
