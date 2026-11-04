# Capitolo 14: Laboratorio 5: Stringhe, Quantificazioni e Funzioni sui Caratteri
## Le stringhe
Nel linguaggio C il testo è un array di elementi di tipo `char`. Lettere, cifre e simboli sono **caratteri**, e corrispondono a codici numerici convenzionali descritti da degli standard; quello fondamentale è l'**ASCII** (si legge «àski»), con 128 caratteri. Alcuni codici da conoscere: `'\0'` è 0 (NUL, il terminatore), `'\t'` è 9 (tabulazione), `'\n'` è 10 (a capo), `'\r'` è 13, lo spazio è 32, `'0'` è 48, `'A'` è 65 e `'a'` è 97.

Il C supporta tre codifiche per il testo: ~single-byte~ con `char`, che va bene per ASCII e Latin-1; ~wide~ con `wchar_t`; ~multi-byte~, sempre con `char` ma con un'interpretazione più elaborata. Nel corso si usa solo il testo single-byte.

Una stringa ha una differenza fondamentale rispetto agli array generici: per convenzione è terminata dal carattere `'\0'`, detto **terminatore** o NUL (capitolo 26 della teoria). Così «ciao» è un array di 5 elementi di tipo `char`, e si può dichiarare in tre modi:

```c
char txt[] = { 'c', 'i', 'a', 'o', '\0' };
char txt[] = "ciao";
const char* txt = "ciao";   // il compilatore ha aggiunto il NUL
```

(In parole povere: una stringa è una fila di lettere con un segnale di «stop» in fondo; chi la legge va avanti finché non trova lo stop.)

## Il programma stringhe.c
Il programma `stringhe.c` del codice iniziale mostra le operazioni di base. Le stringhe si stampano con `%s` e si modificano come array:

```c
char lettera = 'A';
char testoA[] = "testo";
testoA[1] = 'E';      // cambia 'e' in 'E'
testoA[4] = lettera;  // cambia 'o' in 'A'
testoA[3] = '\0';     // termina la stringa dopo 3 caratteri
printf("La stringa A adesso e': %s\n", testoA);   // stampa tEs
```

L'ultima `printf` stampa `tEs`: i caratteri dopo il primo terminatore restano in memoria, ma per la stringa non esistono più.

Per leggere una stringa si riserva lo spazio per il terminatore e si limita la lettura:

```c
#define MAX_CH  20
char testo_input[MAX_CH + 1];   // 20 caratteri + 1 per il terminatore
scanf("%20s", testo_input);
```

`scanf` si ferma a uno spazio, un a capo o una tabulazione, oppure dopo 20 caratteri. Il programma suggerisce di provare con una parola singola, con più parole e con una parola di più di 20 caratteri.

I caratteri sono anche numeri, quindi si possono stampare con `%d` e fare operazioni semplici. Cifre e lettere appaiono in sequenza, e questo permette di passare da cifre a numeri e viceversa:

```c
char cifra = '7';
int num_cifra = cifra - '0';   // '0'-'0'==0, '1'-'0'==1, ...: qui 7
char cifra_i = '0' + i;        // da un valore alla cifra corrispondente
```

(In parole povere: `'7'` non è il numero 7 ma il codice 55; togliendo il codice di `'0'`, cioè 48, si ottiene proprio 7.)

## Il programma alfabeto.c
Si deve scrivere `alfabeto.c`, che crea un array di 27 caratteri, inizializza con un ciclo `for` i primi 26 con le lettere dalla `'A'` alla `'Z'`, inserisce il terminatore e stampa la stringa con `printf`. Una possibile soluzione (non nelle slide), che sfrutta il fatto che le lettere sono in sequenza:

```c
#include <stdio.h>

int main(void) {
    char alfabeto[27];
    for (size_t i = 0; i < 26; i++) {
        alfabeto[i] = 'A' + i;
    }
    alfabeto[26] = '\0';
    printf("%s\n", alfabeto);
}
```

## Esercizio: Montagne
Sulla pagina Moodle c'è l'esercizio **Lab05-Es2 Montagne**: si deve leggere la specifica, compresi i suggerimenti, e scrivere il codice. Il testo sta su Moodle.

## Quantificazioni con una sentinella
Il laboratorio riprende i due schemi delle quantificazioni (capitoli 35 e 36 della teoria), in forma di `for` su un array `a` di lunghezza `len`, dove «Cond» è uno pseudocodice per una condizione qualunque. Per la domanda «tutti gli elementi soddisfano Cond?»:

```c
bool tutti = true;
for (size_t i = 0; i < len && tutti; i++) {
    if (!Cond(a[i]))
        tutti = false;
}
```

Per la domanda «esiste almeno un elemento che soddisfa Cond?»:

```c
bool esiste = false;
for (size_t i = 0; i < len && !esiste; i++) {
    if (Cond(a[i]))
        esiste = true;
}
```

In entrambi i casi il ciclo termina per due motivi: si è scorso tutto l'array, oppure la sentinella ha cambiato valore. Le variabili `tutti` ed `esiste` sono **variabili sentinella**, e la risposta si legge sempre da loro.

Attenzione a due dettagli (precisazione aggiunta: le slide dicono altro). Le slide leggono il risultato da `i == len` e aggiungono che, quando la sentinella cambia, `a[i]` è il primo elemento che fa cambiare la risposta. In questa forma con il `for` non è così: dopo il corpo viene eseguito comunque `i++`, quindi l'elemento è `a[i-1]`, e se è l'ultimo dell'array si arriva a `i == len` anche con la sentinella già cambiata. Inoltre `i`, dichiarata nel `for`, non è visibile fuori dal ciclo. Se serve la posizione si usa la forma con `while` e `i++` nell'`else` del capitolo 35 della teoria, dove `i` resta sull'elemento trovato.

## Le funzioni sui caratteri: ctype.h
La libreria del C ha diverse funzioni per classificare e manipolare i caratteri, definite in `<ctype.h>`:
- `isalpha(ch)`: il carattere è alfabetico, cioè una lettera?
- `isdigit(ch)`: è una cifra?
- `isalnum(ch)`: è alfanumerico?
- `islower(ch)` e `isupper(ch)`: è una lettera minuscola? maiuscola?
- `isspace(ch)`: è uno spazio, una tabulazione o un ritorno a capo?
- `ispunct(ch)`: è un carattere di punteggiatura?
- `tolower(ch)`: se il carattere è alfabetico ritorna la forma minuscola, altrimenti lo ritorna inalterato;
- `toupper(ch)`: come `tolower`, ma ritorna la forma maiuscola.

Nelle slide i prototipi sono scritti in forma semplificata, per esempio `bool isalpha(char ch)` e `char tolower(char ch)`; nella libreria vera parametro e risultato sono di tipo `int`, e i test ritornano un valore diverso da zero per dire «vero», non necessariamente 1. Si scrive quindi `if (isalpha(ch))`, senza confrontare il risultato con `true` (precisazione aggiunta).

(In parole povere: invece di ricordarti i codici ASCII e scrivere `ch >= 'a' && ch <= 'z'`, chiedi direttamente alla libreria «è una lettera minuscola?».)

## Esercizi: Passwords e Indovina chi?
**Lab05-Es3 Passwords**: sulla pagina Moodle si legge la specifica, facendo attenzione a quali sono le cinque proprietà da calcolare per ciascuna password in input. **Lab05-Es4 Indovina chi?** è un esercizio extra, ispirato al gioco da tavolo ~Guess Who?~, inventato da Theo e Ora Coster nel 1980 in Gran Bretagna con l'azienda MB. I testi stanno su Moodle.
