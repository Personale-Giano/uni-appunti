# Capitolo 44: Memory Leak ed Errori Comuni con la Memoria Dinamica
## La gestione manuale
La memoria dinamica è gestita **solo tramite puntatori**: un blocco dello heap non ha un nome, e l'unico modo per raggiungerlo è l'indirizzo restituito da `malloc`. Ogni chiamata a `malloc` restituisce l'indirizzo di un blocco (~heap block~) che rimane allocato fino alla `free` corrispondente; se ci si dimentica di liberarlo, resta nello heap fino alla terminazione del programma.

**Definizione.** Un **memory leak** (perdita di memoria) è un blocco allocato e poi «dimenticato»: non è più referenziabile, perché nessun puntatore ne contiene l'indirizzo, ma non è stato deallocato.

(In parole povere: è un box in affitto di cui si è persa la chiave. Non lo si può più usare e nemmeno restituire, ma continua a risultare occupato.)

Ogni blocco allocato è una **responsabilità**: chi lo crea deve anche preoccuparsi che venga liberato. La corretta gestione dello heap in C dipende dall'attenzione e dalla disciplina del programmatore, non dal linguaggio. Una frase delle slide dice «chi semina malloc, raccoglie memory leak», dove si intende, ovviamente, una `malloc` senza la `free` corrispondente.

Gli errori tipici sono sei. Hanno in comune il fatto di essere spesso difficili da notare: spesso il programma sembra funzionare.

## Allocare senza liberare
```c
void f(void) {
    int* a = malloc(100 * sizeof(int));
    // uso dell'array
} // MEMORY LEAK: manca free(a)
```

Al ritorno di `f` la variabile locale `a` viene deallocata con lo stack frame, e con lei si perde l'unica copia dell'indirizzo; il blocco di 100 interi resta occupato fino al termine del programma. Se l'errore si ripete in un ciclo, la memoria si esaurisce progressivamente. Non c'è nessun crash immediato, solo una crescita della RAM usata dal programma. Per il C esistono strumenti di diagnosi, come **Valgrind**, che rintracciano i memory leak.

## Perdere l'indirizzo del blocco
```c
int* p = malloc(10 * sizeof(int));
p = malloc(20 * sizeof(int)); // MEMORY LEAK: il primo blocco è perso per sempre
```

Il puntatore è stato sovrascritto senza prima liberare il blocco a cui puntava. Il primo blocco rimane allocato ma irraggiungibile: è di nuovo un memory leak. La versione corretta chiama `free(p);` prima del secondo assegnamento.

## Usare un puntatore dopo free
```c
int* p = malloc(sizeof(int));
*p = 5;
free(p);
printf("%d\n", *p); // ERRORE: uso di memoria già liberata
```

Dopo la deallocazione `p` è un dangling pointer (capitolo 41): contiene l'indirizzo di una zona che non è più valida. L'accesso ha **comportamento indefinito**: il programma può apparentemente funzionare, produrre risultati errati, corrompere altri dati oppure terminare. Proprio perché è difficile da diagnosticare, conviene assegnare `NULL` ai puntatori deallocati:

```c
free(p); p = NULL; // evita l'uso accidentale del dangling pointer
```

Con `p` a `NULL` un uso successivo per errore non passa inosservato: il puntatore si può controllare con `p != NULL` o con una `assert` (capitolo 34), e sui sistemi comuni dereferenziarlo interrompe subito il programma invece di leggere dati sporchi in silenzio (formalmente anche dereferenziare `NULL` è comportamento indefinito). L'azzeramento protegge però solo quella variabile: altri puntatori che contengono l'indirizzo dello stesso blocco restano appesi.

## Deallocare due volte lo stesso blocco
```c
int* p = malloc(sizeof(int));
free(p);
free(p); // ERRORE: doppia free
```

La seconda `free` tenta di restituire allo heap una zona già restituita. L'effetto è un crash immediato oppure la corruzione della struttura interna dello heap, che si manifesta più tardi e lontano dalla causa. Anche qui il rimedio è azzerare il puntatore dopo la prima `free`. Il motivo è che `free(NULL)` è ammessa e non fa nulla (precisazione aggiunta): dopo `free(p); p = NULL;` una seconda `free(p);` diventa innocua.

## Fare assunzioni sugli indirizzi
```c
int* p1 = malloc(sizeof(int));
int* p2 = malloc(sizeof(int));
p1[0] = 10;
p1[1] = 20; // ERRORE: non sto accedendo a p2
```

Il blocco di `p1` contiene un solo `int`, quindi `p1[1]` è un accesso fuori dai limiti (capitolo 25), e non c'è alcuna garanzia che `p1` e `p2` siano adiacenti in memoria. La contiguità è garantita **dentro il blocco di una singola `malloc`**: chiamate diverse restituiscono blocchi che quasi sicuramente non sono contigui. La gestione interna dello heap è molto articolata e non fa parte del corso.

## Leggere memoria non inizializzata
```c
int* a = malloc(5 * sizeof(int));
printf("%d", a[0]); // ERRORE: a[0] non è stato inizializzato
```

`malloc` riserva il blocco ma non ne inizializza il contenuto. Prima di leggere un elemento bisogna assegnargli un valore; fino ad allora il suo valore è indeterminato, come per una variabile locale non inizializzata.

## Il quadro d'insieme
I sei errori si riducono a tre regole:

- **ogni blocco va liberato una volta sola**: zero volte è un memory leak (allocare senza liberare, perdere l'indirizzo), due volte è una doppia `free`;
- **dopo la `free` il blocco non si tocca più**, e il puntatore si azzera;
- **dentro il blocco valgono le regole degli array**: si resta negli indici validi e si scrive prima di leggere.

## Che cosa va nello heap e che cosa nello stack
In C è consuetudine allocare nello heap tutti i dati di dimensione non nota a priori: array, strutture, matrici e così via. Lo stack viene invece riservato a:

- variabili locali di piccole dimensioni;
- puntatori, indici, contatori;
- eventuali array di dimensione fissa o limitata.

Nei primi standard del C, quelli precedenti al C99, i VLA non esistevano (capitolo 25): anche per un piccolo array di dimensione variabile era necessario ricorrere allo heap.
