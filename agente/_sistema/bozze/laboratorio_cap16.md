# Capitolo 16: Laboratorio 6: Array e Stringhe come Parametri, string.h e Vocali
## Passare un array a una funzione
Si può passare un array a una funzione approfittando del fatto che un array è (anche) un puntatore al suo primo elemento. Il parametro si può scrivere in due modi equivalenti:

```c
int dati[SZ] = { ... };
fn(dati);
...
void fn(int* dati) { ... }
// oppure:
void fn(int dati[]) { ... }
```

Precisazione aggiunta: a rigore l'array non «è» un puntatore, e i fatti in gioco sono due. Nella chiamata `fn(dati)` il nome `dati` viene convertito nel puntatore al primo elemento, `&dati[0]` (capitolo 25 della teoria): per questo il passaggio funziona. Nella dichiarazione della funzione, invece, il C converte il tipo di un parametro scritto come array in un puntatore: per questo `int dati[]` è un `int*` e le due forme del parametro sono la stessa cosa (capitolo 33 della teoria).

La domanda delle slide è quale sia il problema di questo codice. La risposta: la funzione riceve il puntatore al primo elemento, ma non riceve la **dimensione** dell'array. Dentro `fn` non c'è modo di sapere quanti elementi si possono leggere, e anche `sizeof(dati)` darebbe la dimensione di un puntatore, non dell'array (precisazione aggiunta). Per questo, come spiegato nel capitolo 33 della teoria, il passaggio di un array comporta tipicamente due parametri, la lunghezza e l'array, per esempio `void fn(size_t datiLen, const int dati[])`, con il `const` se la funzione deve solo leggere.

(In parole povere: alla funzione arriva l'indirizzo della prima casella, non il numero di caselle; è come ricevere l'indirizzo di una via senza sapere quanti numeri civici ha.)

Un esempio è la funzione dell'esercizio 3 di progettazione del capitolo 15 di questo laboratorio, che conta le occorrenze di `n` nell'array. Una soluzione possibile (non nelle slide), che scorre gli indici nell'intervallo [0, len):

```c
size_t conta_occorrenze(size_t len, const int a[], int n) {
    size_t conta = 0;
    for (size_t i = 0; i < len; i++) {
        if (a[i] == n)
            conta++;
    }
    return conta;
}
```

Nel `main()` la si chiama passando la dimensione insieme all'array, per esempio `conta_occorrenze(SZ, dati, 7)`, e il risultato si stampa con `%zu`. È lo schema del conteggio del capitolo 24 della teoria, chiuso dentro una funzione.

## Esercizio: Funzioni su arrays
Sulla pagina Moodle c'è l'esercizio **Lab06-Es2 Funzioni su arrays**: si deve completare il programma, assicurandosi che passi tutti i test proposti. Le slide non dicono altro: il testo sta su Moodle.

## Le funzioni di string.h
Il C dispone di molte funzioni per gestire le stringhe, dichiarate nell'header `<string.h>`. Le slide ne presentano tre, le stesse del capitolo 33 della teoria:
- `size_t strlen(const char* str)`: ritorna la lunghezza in caratteri della stringa `str`, terminatore escluso; per esempio `strlen("ciao")` vale 4, anche se l'array occupa 5 `char`;
- `int strcmp(const char* s1, const char* s2)`: confronta le due stringhe in ordine lessicografico (definito sotto) e ritorna un valore negativo se `s1` precede `s2`, 0 se sono uguali carattere per carattere, un valore positivo se `s1` segue `s2`; per esempio `strcmp("cane", "casa")` è negativo, perché al terzo carattere `'n'` viene prima di `'s'`;
- `char* strncpy(char* dest, const char* src, size_t count)`: copia al più `count` caratteri, terminatore incluso, dalla stringa `src` alla stringa `dest`.

(In parole povere: la funzione `strlen` conta le lettere, `strcmp` dice chi viene prima sul dizionario, `strncpy` copia una stringa in un'altra senza superare un numero massimo di caratteri.)

**Definizione.** L'**ordine lessicografico** fra due stringhe è l'ordine del dizionario: si confrontano i caratteri nella stessa posizione partendo dal primo, e alla prima differenza viene prima la stringa con il carattere di codice minore; se una stringa finisce prima dell'altra ed è uguale al suo inizio, viene prima la più corta.

(In parole povere: è il modo in cui si cercano le parole sul vocabolario: «cane» viene prima di «casa» perché alla terza lettera la n viene prima della s, e «ca» viene prima di «cane». In C conta il codice ASCII, quindi le maiuscole vengono prima delle minuscole: `strcmp("Zeta", "alfa")` è negativo.)

Tre precisazioni aggiunte. La slide chiama la destinazione `dst` nella descrizione e `dest` nel prototipo: è lo stesso parametro. Più importante, «terminatore incluso» vale solo se il terminatore rientra nei `count` caratteri: se `src` ha `count` caratteri o più, `strncpy` non copia il terminatore e `dest` resta senza `'\0'`; è prudente copiare al più la capacità di `dest` meno uno e poi scrivere il terminatore a mano. Infine il risultato di `strcmp` si confronta con 0, per esempio `if (strcmp(s1, s2) == 0)`, e due stringhe non si confrontano mai con `==`, che confronterebbe gli indirizzi.

## Il programma vocali.c
Si scrive un programma `vocali.c` che legge dallo standard input una parola, con `%s` e `scanf`, e svolge due operazioni. Per prima cosa stampa «1» se nella parola ci sono vocali, altrimenti «0»; per farlo si scrivono due funzioni: `is_vowel`, che ritorna un booleano per dire se un singolo carattere è una vocale (sono vocali i caratteri `AEIOUaeiou`), ed `esistono_vocali`, che prende una stringa e ritorna un booleano per dire se contiene almeno una vocale. Poi stampa le sole vocali presenti nella parola, con una funzione `stampa_vocali`.

Una soluzione possibile (non nelle slide):

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX_CH 100

bool is_vowel(char ch);
bool esistono_vocali(const char* s);
void stampa_vocali(const char* s);

int main(void) {
    char parola[MAX_CH + 1];        // + 1 per il terminatore
    scanf("%100s", parola);
    printf("%d\n", esistono_vocali(parola));
    stampa_vocali(parola);
}

// true se ch è una delle vocali AEIOUaeiou
bool is_vowel(char ch) {
    const char vocali[] = "AEIOUaeiou";
    bool vocale = false;
    for (size_t i = 0; vocali[i] != '\0' && !vocale; i++) {
        if (ch == vocali[i])
            vocale = true;
    }
    return vocale;
}

// true se la stringa s contiene almeno una vocale
bool esistono_vocali(const char* s) {
    bool esiste = false;
    for (size_t i = 0; s[i] != '\0' && !esiste; i++) {
        if (is_vowel(s[i]))
            esiste = true;
    }
    return esiste;
}

// stampa solo le vocali di s
void stampa_vocali(const char* s) {
    for (size_t i = 0; s[i] != '\0'; i++) {
        if (is_vowel(s[i]))
            printf("%c", s[i]);
    }
    printf("\n");
}
```

Con la parola `Programmazione` il programma stampa `1` e poi `oaaioe`; con `psst` stampa `0` e una riga vuota.

Sia `esistono_vocali` sia `is_vowel` sono quantificazioni esistenziali con sentinella (capitolo 14 di questo laboratorio): la seconda risponde alla domanda «esiste una vocale dell'elenco uguale a `ch`?». Le funzioni `esistono_vocali` e `stampa_vocali` non riscrivono il test sulle vocali ma chiamano `is_vowel`, ed è proprio il senso di scomporre il problema in funzioni (capitolo 29 della teoria). I parametri sono `const char*` perché le funzioni leggono la parola senza modificarla. In `printf("%d\n", ...)` il `bool` viene promosso a `int` e vale 1 o 0, esattamente l'output richiesto.

Precisazione aggiunta: la slide dice solo di usare `%s`, ma senza limite una parola lunga sfora l'array. Per questo la `scanf` ha la larghezza massima 100, uguale a `MAX_CH`, come nella lettura con larghezza massima del capitolo 14 di questo laboratorio.

## Serve passare la dimensione?
La domanda delle slide è se per le stringhe serva ancora passare la dimensione, come per gli array. Le slide pongono solo la domanda; considerazione aggiunta: la risposta è no. Una stringa ben formata porta con sé il terminatore `'\0'`, e la funzione può scorrerla finché non lo incontra. Nel codice sopra i cicli hanno infatti la condizione `s[i] != '\0'` al posto di `i < len`, e i prototipi di `strlen` e `strcmp` ricevono solo il puntatore (`strncpy` ha `count`, ma per limitare la copia, non per sapere dove finisce `src`). È la differenza fondamentale fra stringhe e array generici già vista nei capitoli 26 e 33 della teoria: un array di `int` non ha un valore che ne segni la fine, una stringa sì. Vale solo se la stringa è davvero terminata: per questo le precauzioni su `scanf` con larghezza massima e su `strncpy` sono importanti.

(In parole povere: per un array la funzione deve sapere quante caselle contare; per una stringa basta andare avanti finché non si trova il cartello di «fine».)

## Esercizio: Palindroma
Sulla pagina Moodle c'è l'esercizio **Lab06-Es3 Palindroma**, nella sezione delle funzioni su stringhe: si deve completare il programma, assicurandosi che passi tutti i test proposti. Le slide non ne riportano il testo; il nome dice che si tratta di riconoscere le parole palindrome, che si leggono uguali nei due versi, come «anna» o «radar» (considerazione aggiunta, da verificare sulla specifica).

## Esercizio extra: Scale e serpi
**Scale e serpi** è un gioco da tavolo tradizionale di origine indiana, diffuso anche in occidente in versione semplificata: è un gioco di percorso con i dadi, simile al Gioco dell'Oca. Sulla pagina Moodle c'è l'esercizio **Lab06-Es4 Scale e serpi**, segnato nelle slide come esercizio extra: il codice del gioco, cioè il lancio dei dadi e la posizione dei giocatori, è già parzialmente implementato, e si deve scrivere la funzione che determina come muovere un giocatore lungo il percorso del tabellone. Il testo, con le regole precise, sta su Moodle.
