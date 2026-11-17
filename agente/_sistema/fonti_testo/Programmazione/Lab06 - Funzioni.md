# Lab06 - Funzioni

<!-- pagina 1 -->
A.A. 2026/27
Programmazione I
Laboratorio
DIPARTIMENTO DI 
INFORMATICA
CORSO DI LAUREA 
TRIENNALE
Funzioni
Lezione nº 6

<!-- pagina 2 -->
Come definire le funzioni in C
Permettono di dividere il programma in blocchi di codice 
separati, che svolgono compiti specifici.
Per ogni sotto-compito di un programma, ci serve:
• definire un nome chiaro e conciso
• definire quali parametri in ingresso sono necessari per 
svolgere il compito (opzionali)
• definire quali dati restituisce (opzionale)
2
tipo_di_ritorno nome_funzione(param1, param2, …) {
<codice della funzione>
}

<!-- pagina 3 -->
Esercizio 1: saluta l’utente
Vogliamo scrivere una funzione che scrive sul terminale un 
messaggio di saluto: “Buongiorno!”
• Quale nome usiamo?
• Quali parametri in ingresso?
• Quale tipo di ritorno?
3

<!-- pagina 4 -->
Esercizio 2: determina se un numero è primo
Vogliamo scrivere una funzione che determina se un 
numero positivo n è un numero primo.
• Quale nome usiamo?
• Quali parametri in ingresso?
• Quale tipo di ritorno?
4

<!-- pagina 5 -->
Esercizio 3: ricerca in un array
Vogliamo scrivere una funzione che conta le occorrenze del 
numero n in un array di interi a[].
• Quale nome usiamo?
• Quali parametri in ingresso?
• Quale tipo di ritorno?
5

<!-- pagina 6 -->
Esercizio 4: indici di una sequenza in input
Vogliamo scrivere una funzione che legge da input una 
sequenza di numeri interi positivi, e se non ci sono errori
restituisce la media e la varianza.
• Quale nome usiamo?
• Quali parametri in ingresso?
• Quale tipo di ritorno?
6

<!-- pagina 7 -->
Verifica (esaustiva) di primalità
Come determinare se un numero naturale n>1 è primo? 
Un numero n è primo se è divisibile soltanto da se stesso e da 1.
⇒cerchiamo se esiste un divisore d di n, con 2 ≤ d < n
7
7 è primo?
diventa:
●2 è un divisore di 7?  No.
●3 è un divisore di 7?  No.
●4 è un divisore di 7?  No.
●5 è un divisore di 7?  No.
●6 è un divisore di 7?  No.
Allora 7 è primo.
9 è primo?
diventa:
●2 è un divisore di 9?  No.
●3 è un divisore di 9?  Si.
●4 è un divisore di 9?  -
●5 è un divisore di 9?  -
●6 è un divisore di 9?  -
●7 è un divisore di 9?  -
●8 è un divisore di 9?  -
Allora 9 non è primo.

<!-- pagina 8 -->
Numeri primi
Completare il programma primi.c dichiarando ed 
implementando una funzione verifica_primalita che deve 
prendere come argomento un numero intero maggiore di 1 
e restituisce un valore appropriato per indicare se è primo 
(qual è il tipo appropriato da restituire?).
Usare la funzione verifica_primalita nel main per trovare e 
stampare tutti i numeri primi minori di 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 
43 47 53 59 61 67 71 73 79 83 89 97
8

<!-- pagina 9 -->
Funzioni iterative
Aprire il file funzioni_iterative.c fornito come codice iniziale, 
leggere il main (già completato, non da modificare) ed 
implementare le funzioni richieste:
• Scrivere una funzione esponenziale che, dati in ingresso 
una base b e un esponente e (come parametri), 
restituisce il valore di b elevato ad e. Assumere e≥0.
• Scrivere una funzione prodotto_multipli che prende 
come parametri tre interi non-negativi n, m e q
restituisce il prodotto di tutti gli interi compresi tra n e m
(estremi inclusi) che sono multipli di q.
• Scrivere una funzione stampa_al_rovescio che prende in 
ingresso un intero n≥0 stampa a video i valori da n a 0.
9

<!-- pagina 10 -->
Cambio monete
Scrivere un programma monete.c che chiede all'utente 
un numero naturale cent (interpretato come in 
centesimi), e successivamente stampa a video il più 
piccolo cambio in monete. I tagli delle monete sono:
10
Esempio: se l'utente chiede il cambio di cent=95 centesimi, il 
programma scriverà in output:
1 da 50 cent
2 da 20 cent
1 da 5 cent
#define NUM_TAGLI 6
const int tagli_monete[NUM_TAGLI] = {1,2,5,10,20,50};

<!-- pagina 11 -->
Cambio monete
11
Suggerimento 1: scrivere una funzione cambio_taglio
che prende in input un ammontare in centesimi ed un 
taglio di una moneta, calcola quante volte può sottrarre 
il taglio di quella moneta dall’ammontare, stampa "x da 
t cent" in output, e ritorna il resto (l’ammontare 
iniziale meno x*t). Nel main chiamare cambio_taglio più 
volte, aggiornando man mano la somma rimanente.
Suggerimento 2: il tipo size_t è unsigned, quindi non può 
rappresentare valori negativi. Un ciclo for con condizione:
for (size_t i=N-1; i>=0; i--) { … }
non funzionerà, in quanto i>=0 è sempre vero!
Nei casi in cui serve rappresentare indici negativi (es: cicli che 
decrementano fino a zero) usate il tipo ptrdiff_t.

<!-- pagina 12 -->
Cambio monete
Esempio esecuzione 1:
Scrivere l'ammontare da convertire in monete: 120
2 da 50 cent
1 da 20 cent
12
Esempio esecuzione 2:
Scrivere l'ammontare da convertire in monete: 367
7 da 50 cent
1 da 10 cent
1 da 5 cent
1 da 2 cent
Esempio esecuzione 3:
Scrivere l'ammontare da convertire in monete: 473
9 da 50 cent
1 da 20 cent
1 da 2 cent
1 da 1 cent

<!-- pagina 13 -->
Statistiche su sequenze
Sulla pagina Moodle trovate un esercizio con nome
Completate il programma, assicurandovi che passi tutti i 
test proposti.
Quali parametri deve avere la funzione leggi_sequenza?
Cosa deve restituire al chiamante?
NOTA: non servono gli array per questo esercizio, in quanto 
somma, somma dei quadrati e massimo possono essere 
calcolati mentre vengono letti i valori della sequenza.
13
Lab06-Es1 Statistiche sequenze

<!-- pagina 14 -->
Passaggio di array
Possiamo passare un array ad una funzione approfittando 
del fatto che un array è (anche) un puntatore.
int dati[SZ] = { … };
fn(dati);
⋮
void fn(int *dati) { … }
oppure:
void fn(int dati[]) { … }
DOMANDA: Qual è il problema?
14

<!-- pagina 15 -->
Passaggio di array
Possiamo passare un array ad una funzione approfittando 
del fatto che un array è (anche) un puntatore.
int dati[SZ] = { … };
fn(dati);
⋮
void fn(int *dati) { … }
oppure:
void fn(int dati[]) { … }
DOMANDA: Qual è il problema?
15
Il problema è che la funzione riceve il puntatore al primo elemento, 
ma non riceve la dimensione dell’array.

<!-- pagina 16 -->
Funzioni su arrays
Sulla pagina Moodle trovate un esercizio con nome
Completate il programma, assicurandovi che passi tutti i 
test proposti.
16
Lab06-Es2 Funzioni su arrays

<!-- pagina 17 -->
Funzioni su stringhe nella libreria del C
Il linguaggio C dispone di molte funzioni per gestire le 
stringhe, nell’header <string.h>. Ne vediamo alcune:
•
size_t strlen(const char* str)
Ritorna la lunghezza in caratteri (terminatore escluso) della stringa str.
•
int strcmp(const char* s1, const char* s2)
Compara le due stringhe in modo lessicografico, e ritorna: 
–
un valore negativo se s1 precede s2 (in ordine lessicografico);
–
0 se s1 è uguale, carattere per carattere, ad s2;
–
un valore positivo se s1 segue s2 (in ordine lessicografico).
L’ordine lessicografico è l’ordine del dizionario.
•
char* strncpy(char* dest, const char* src, size_t count)
Copia al più count caratteri (terminatore incluso) dalla stringa src nella 
stringa dst.
17

<!-- pagina 18 -->
Vocali
Scrivere un programma vocali.c che legge dallo standard input 
una parola (usare %s con scanf) e svolge le seguenti operazioni:
1. Stampa “1” se ci sono delle vocali, altrimenti stampa “0”. Per 
fare questo scrivere due funzioni:
a. is_vowel che ritorna un booleano per determinare se un 
singolo carattere è una vocale. Consideriamo vocali i 
seguenti caratteri: AEIOUaeiou
b. esistono_vocali che prende in input una stringa e ritorna 
un booleano per indicare se esistono vocali nella stringa.
2. Stampa le sole vocali presenti nella parola in input. Per fare 
questo, scrivere una funzione stampa_vocali.
DOMANDA: serve ancora passare la dimensione come per gli 
array?
18

<!-- pagina 19 -->
Funzioni su stringhe
Sulla pagina Moodle trovate un esercizio con nome
Completate il programma, assicurandovi 
che passi tutti i test proposti.
19
Lab06-Es3 Palindroma

<!-- pagina 20 -->
Scale e Serpi
Scale e serpi è un gioco da tavolo 
tradizionale di origine Indiana, diffuso anche 
in occidente in versione semplificata. È un 
gioco di percorso con i dadi, simile al Gioco 
dell’Oca.
20
Lab06-Es4 Scale e serpi
Leggere l’esercizio su Moodle. Il codice del gioco (lancio dei 
dadi, posizione dei giocatori) è già parzialmente 
implementato. Scrivere la funzione che determina come 
muovere un giocatore lungo il percorso del tabellone.
