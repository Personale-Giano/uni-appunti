# Capitolo 33: Array e Stringhe come Parametri, il Qualificatore const
## Passare un array a una funzione
In C un array «si comporta anche come un puntatore al suo primo elemento» (capitolo 25), quindi si può passare direttamente a una funzione, e il parametro si può scrivere in due modi equivalenti:

```c
void fn(int* dati);    // oppure:
void fn(int dati[]);
```

L'esempio funziona ma ha un problema: il solo puntatore ai dati **non basta a conoscere la dimensione** dell'array. Il parametro `int dati[]` è infatti un `int*`, quindi dentro la funzione `sizeof(dati)` dà la dimensione di un puntatore e non dell'array (precisazione aggiunta). Per questo il passaggio di un array comporta tipicamente il passaggio di **due parametri**, la lunghezza e l'array:

```c
void fn(size_t datiLen, int dati[]) {
    // posso accedere a dati nell'intervallo [0, datiLen)
}

int main(void) {
    int dati[SZ] = { 1, 2, 3 };   // SZ definita con #define
    fn(SZ, dati);
}
```

(In parole povere: alla funzione arriva solo «dove inizia» l'array, non «quanto è lungo». La lunghezza gliela devi dire tu, a parte.)

## Il qualificatore const
**Definizione.** Il qualificatore **const** dichiara un dato in sola lettura: il compilatore emette un errore se un dato `const` viene modificato oppure passato a un'altra funzione che si aspetta dati non `const` (in quest'ultimo caso gcc può limitarsi a un ~warning~, che con `-Werror` diventa comunque un errore).

(In parole povere: `const` è una promessa scritta nel codice, «questo non lo tocco», e il compilatore controlla che tu la mantenga.)

Se una funzione non deve modificare l'array ricevuto, lo si qualifica così. Per chiarire il **contratto** della funzione, cioè che cosa modifica e che cosa no, si possono dichiarare `const` tutte le variabili che vengono solo lette:

```c
void fn(const size_t datiLen, const int dati[]) {
    // posso accedere a dati in sola lettura
    // la funzione non cambia mai il valore datiLen
}
```

## Passare una stringa
In C una stringa è un array di `char` terminato da `'\0'` (capitolo 26), quindi anche per le stringhe il parametro è un puntatore a `char`. Ma c'è una differenza importante rispetto agli array generici: se la stringa rispetta la convenzione di essere terminata da NUL, **non serve passare la lunghezza**, perché la funzione può scorrerla fino a trovare il terminatore.

```c
void stampa(const char* s) {
    printf("%s\n", s);
}

// due chiamate, per esempio dentro main:
stampa("ciao");     // stringa costante
stampa(buffer);     // array di char
```

(In parole povere: la stringa porta con sé il segnale di fine, come una lettera che si chiude con la firma: per sapere dove finisce basta leggerla.)

## Alcune funzioni di string.h
La libreria standard mette a disposizione molte funzioni per le stringhe, dichiarate in `<string.h>`. Le tre viste a lezione sono:
- `size_t strlen(const char* str);` ritorna la lunghezza della stringa, escluso `'\0'`;
- `int strcmp(const char* s1, const char* s2);` confronta due stringhe in ordine lessicografico, cioè l'ordine del dizionario: ritorna un valore negativo se `s1` precede `s2`, zero se sono uguali, positivo se `s1` segue `s2`;
- `char* strncpy(char* dest, const char* src, size_t count);` copia al più `count` caratteri, incluso il terminatore, da `src` a `dest`.

Attenzione su `strncpy` (precisazione aggiunta, non presente nelle slide): se `src` ha `count` caratteri o più, il terminatore non viene copiato e `dest` resta senza `'\0'`, quindi conviene scegliere `count` tenendone conto.

Due stringhe **non si confrontano con** `==`: quell'operatore confronterebbe gli indirizzi, non i caratteri, e per questo esiste `strcmp` (precisazione aggiunta). Il `const` nei prototipi dice subito che queste funzioni non modificano le stringhe ricevute, tranne `dest` di `strncpy`.
