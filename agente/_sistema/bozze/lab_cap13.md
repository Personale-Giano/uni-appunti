# Capitolo 13: Laboratorio 5: Array, Questionari e Somma Selettiva
## Gli array in laboratorio
Il laboratorio 5, «Array e stringhe», mette in pratica i capitoli 23-26 della teoria. Un **array** è una sequenza di variabili dello stesso tipo, indicizzate da un intero non negativo. Gli indici partono da 0 e il loro tipo è `size_t`, che è senza segno ed è il tipo raccomandato dallo standard C per dimensioni e indici. Lo specificatore di `printf` e `scanf` per `size_t` è `%zu`. In questa prima fase si usano array dichiarati sullo stack, con dimensione prefissata.

Per scrivere codice che usa un array bisogna conoscerne la dimensione. Si hanno due possibilità: una `#define` che la specifica e che si usa ovunque serva l'array, oppure una variabile che la contiene, e allora si lavora sempre con una coppia **numero di elementi, puntatore all'inizio dei dati**. Sugli elementi si opera tipicamente con i cicli.

(In parole povere: un array non sa quanto è lungo; la lunghezza te la devi ricordare tu, in una costante o in una variabile, e portartela sempre dietro.)

## Il programma array.c
Il programma `array.c` del codice iniziale mostra i modi di dichiarare e riempire un array:

```c
#define N 5

int arr[N];                          // array di 5 elementi interi
int values[N] = { 23, 56, 12, -6, 31 };  // lista di inizializzazione
int values2[N] = { 100 };            // i rimanenti N-1 valori sono 0
int values3[] = { 0, 1, 2, 3 };      // la dimensione si ricava: 4 elementi
```

Poi somma elemento per elemento `values` e `values2` in `arr`, e stampa una tabella con due colonne allineate grazie alle larghezze minime di `%6zu` e `%7d`:

```c
puts("Indice  Valore");
for (size_t i = 0; i < N; i++) {
    printf("%6zu %7d\n", i, arr[i]);
}
```

Infine chiede all'utente una dimensione e dichiara un array a lunghezza variabile (VLA, capitolo 25): `size_t sz; scanf("%zu", &sz); int inseriti[sz];`, riempiendolo con un ciclo di `scanf("%d", &inseriti[i])`.

La parte da completare alla fine del `main()` chiede di calcolare e stampare la somma degli elementi di `inseriti[]`. Con un accumulatore (soluzione nostra, non nelle slide):

```c
int somma = 0;
for (size_t i = 0; i < sz; i++) {
    somma += inseriti[i];
}
printf("Somma: %d\n", somma);
```

## Il programma questionari.c
A 20 soggetti è stato chiesto di rispondere a una domanda con un voto da 1 a 5 stelle. Le risposte sono:

```c
#define NUM_RISP 20
const int risposte[NUM_RISP] = {
    1, 2, 5, 4, 3,  5, 2, 1, 3, 1,
    4, 3, 3, 3, 2,  3, 3, 2, 2, 5
};
```

Si deve completare `questionari.c` in modo che calcoli le frequenze delle 5 risposte possibili, accumulandole in un array `frequenze[]` prima di stamparle. Un possibile output è:

```
Stelle  Frequenza
1          3   ###
2          5   #####
3          7   #######
4          2   ##
5          3   ###
```

L'idea chiave è usare il **valore della risposta come indice**: la risposta `r` incrementa la casella `r - 1`, perché le stelle vanno da 1 a 5 e gli indici da 0 a 4. Una possibile soluzione (non nelle slide):

```c
int frequenze[5] = { 0 };   // tutte le frequenze partono da zero

for (size_t i = 0; i < NUM_RISP; i++) {
    frequenze[risposte[i] - 1]++;
}

puts("Stelle  Frequenza");
for (size_t s = 0; s < 5; s++) {
    printf("%zu %10d   ", s + 1, frequenze[s]);
    for (int k = 0; k < frequenze[s]; k++) {
        printf("#");
    }
    printf("\n");
}
```

(In parole povere: hai cinque scatole, una per ogni voto. Per ogni risposta metti un gettone nella scatola giusta, senza dover cercare: il voto stesso ti dice quale scatola.)

## Esercizio: Somma selettiva
Sulla pagina Moodle c'è l'esercizio **Lab05-Es1 Somma selettiva**: si deve leggere la specifica e scrivere il codice. La domanda posta dalle slide è se si possa fare a meno di memorizzare la sequenza letta in un array. Il testo dell'esercizio sta su Moodle, quindi la risposta va cercata nella specifica: in generale l'array è necessario solo se i valori servono più di una volta o in un ordine diverso da quello di lettura (considerazione nostra).
