# Capitolo 19: Laboratorio 7: Stringhe e Aritmetica dei Puntatori: Codifica ed Elimina Vocali
## Scorrere una stringa con un puntatore
Le stringhe sono array di `char` terminati per convenzione dal carattere `'\0'` (capitolo 26 della teoria). Per questo si manipolano facilmente con l'aritmetica dei puntatori: invece di un indice `i` e di `s[i]`, si usa un puntatore che parte dal primo carattere, si legge il carattere corrente con `*p` e si avanza con `p++`, finché non si incontra il terminatore. La funzione riceve la stringa come puntatore, per esempio `void funzione(const char* pStr)`, e la scorre in uno dei due modi delle slide. Nella slide il parametro si chiama `pStrInput` e nei cicli `pStr`; qui si usa sempre `pStr`, come se fosse il parametro stesso:

```c
while (*pStr != '\0') {
    /* usa *pStr */
    pStr++;
}

for ( ; *pStr != '\0'; pStr++) {
    /* usa *pStr */
}
```

Nel `for` la parte di inizializzazione è vuota, perché il puntatore arriva già pronto come parametro. Il parametro è una copia dell'indirizzo (passaggio per valore, capitolo 28 della teoria): farlo avanzare non sposta nulla nel chiamante, che continua ad avere il puntatore all'inizio della stringa.

(In parole povere: invece di dire «guarda la lettera numero i», si tiene il dito sulla lettera corrente e lo si sposta di una lettera alla volta, finché il dito non arriva al segno di fine.)

Il codice iniziale ne contiene già un esempio, la funzione `convertToUppercase` di `05_codifica.c`, che usa `toupper` di `<ctype.h>` (capitolo 14 di questo laboratorio):

```c
void convertToUppercase(char *pStr) {
    while (*pStr != '\0') {
        *pStr = toupper(*pStr);
        pStr++;
    }
}
```

Qui il parametro non è `const`, perché la funzione modifica la stringa sul posto: `*pStr = ...` scrive nel carattere puntato.

## Es 5: codifica e decodifica
L'esercizio chiede di completare `05_codifica.c` con due funzioni. La prima, `codifica`, modifica sul posto le lettere maiuscole della stringa spostandole di una posizione nell'alfabeto: A→B, B→C, …, Y→Z, e Z→A, ricominciando dall'inizio; tutti gli altri caratteri restano come sono. Per esempio `"ABC"` diventa `"BCD"`. La seconda, `decodifica`, fa la trasformazione inversa.

(In parole povere: è il cifrario più semplice possibile, ogni lettera viene sostituita dalla successiva, con l'alfabeto chiuso ad anello; per decifrare si torna indietro di una lettera.)

Una soluzione possibile (non nelle slide):

```c
// implementazione di codifica()
void codifica(char *pStr) {
    while (*pStr != '\0') {
        if (*pStr >= 'A' && *pStr <= 'Z') {   // solo le maiuscole
            if (*pStr == 'Z') {
                *pStr = 'A';                  // si ricomincia dall'inizio
            } else {
                *pStr = *pStr + 1;            // lettera successiva
            }
        }
        pStr++;
    }
}

// implementazione di decodifica()
void decodifica(char *pStr) {
    for ( ; *pStr != '\0'; pStr++) {
        if (*pStr >= 'A' && *pStr <= 'Z') {
            if (*pStr == 'A') {
                *pStr = 'Z';
            } else {
                *pStr = *pStr - 1;            // lettera precedente
            }
        }
    }
}
```

Le due funzioni usano apposta le due forme di ciclo viste sopra. Il test `*pStr >= 'A' && *pStr <= 'Z'` è l'appartenenza a un intervallo di codici (capitolo 18 della teoria), e `*pStr + 1` funziona perché nel codice ASCII le lettere maiuscole hanno codici consecutivi, da 65 a 90; al posto del test si poteva usare `isupper(*pStr)` di `<ctype.h>`, già incluso. Un'alternativa senza `if` interno usa il resto della divisione: `*pStr = 'A' + (*pStr - 'A' + 1) % 26;` per codificare e `*pStr = 'A' + (*pStr - 'A' + 25) % 26;` per decodificare, dove aggiungere 25 equivale a togliere 1 senza mai scendere sotto zero. Per esempio `"ZAINO"` diventa `"ABJOP"`.

Il `main` del codice iniziale converte prima in maiuscolo la frase `"<ctype> si usa per trasformare i char."`, ottenendo `<CTYPE> SI USA PER TRASFORMARE I CHAR.`, ne salva una copia in `code` con `strncpy`, poi la codifica e la decodifica. Con le funzioni sopra le ultime stampe sono:

```
Stringa dopo la codifica:
 <DUZQF> TJ VTB QFS USBTGPSNBSF J DIBS.
Stringa dopo la decodifica:
 <CTYPE> SI USA PER TRASFORMARE I CHAR.
Decodifica con successo? 1
```

L'ultima riga confronta con `strcmp` la stringa decodificata con la copia: 1 vuol dire che la decodifica ha restituito esattamente il testo di partenza. Spazi, parentesi angolari e punto non sono lettere e restano invariati.

## Elimina vocali: l'idea dei due puntatori
Il secondo problema è una funzione `elimina_vocali` che prende una stringa ed elimina **sul posto** tutte le vocali, compattando i caratteri rimanenti in una stringa uguale o più corta. Per esempio `elimina_vocali("informazione")` ottiene `"nfrmzn"`.

È la riduzione sul posto del capitolo 17 di questo laboratorio, scritta con i puntatori invece che con gli indici. Le slide usano due puntatori aggiuntivi, `pSrc` e `pDst`, entrambi inizializzati a `pStr`, cioè al primo carattere:

- `pSrc` (sorgente) scorre tutta la stringa, un carattere alla volta;
- `pDst` (destinazione) riceve una copia di `*pSrc` e avanza **soltanto** quando il carattere rispetta il criterio di mantenimento, cioè quando non è una vocale;
- alla fine si scrive il terminatore nella posizione di `pDst`, che può trovarsi prima della posizione del terminatore originale.

(In parole povere: un dito legge tutte le lettere, l'altro scrive solo le consonanti, sempre più a sinistra o allo stesso punto del primo. Quando il primo dito arriva alla fine, il secondo mette il punto finale dove si trova.)

![elimina_vocali su "informazione": prima e dopo, con le posizioni finali di pSrc e pDst.](figure/lab/elimina_vocali.png|15)

Dopo l'eliminazione l'array contiene `nfrmzn`, poi il nuovo terminatore, poi i vecchi caratteri `zione` e il vecchio terminatore. Quei residui non fanno più parte della stringa, perché ogni funzione sulle stringhe si ferma al primo `'\0'`.

## Es 6: la funzione elimina_vocali
Sulla pagina Moodle c'è l'esercizio **Lab07-Es3 Elimina vocali**, con la specifica da leggere e il codice da scrivere; il testo non è nelle slide. Una soluzione possibile (non nelle slide) del problema descritto sopra, che riusa la funzione `is_vowel` del capitolo 16 di questo laboratorio:

```c
// elimina sul posto tutte le vocali dalla stringa pStr
void elimina_vocali(char* pStr) {
    char* pDst = pStr;                       // prossima posizione in cui scrivere
    for (char* pSrc = pStr; *pSrc != '\0'; pSrc++) {
        if (!is_vowel(*pSrc)) {              // criterio di mantenimento
            *pDst = *pSrc;
            pDst++;
        }
    }
    *pDst = '\0';                            // nuovo terminatore
}
```

Su `"informazione"`: la `i` iniziale viene saltata; la `n` viene copiata nella posizione 0, e `pDst` avanza; la `f` va nella posizione 1; la `o` viene saltata; e così via. Alla fine `pDst` indica la posizione 6, dove si scrive il terminatore: la stringa è `"nfrmzn"`. Vale sempre che `pDst` non supera `pSrc`, quindi non si sovrascrive mai un carattere non ancora letto. Se la stringa non contiene vocali, ogni carattere viene ricopiato su se stesso; se contiene solo vocali, `pDst` resta all'inizio e il risultato è la stringa vuota.

La funzione modifica la stringa, quindi va chiamata su un array di `char`, come `char s[] = "informazione"; elimina_vocali(s);` (precisazione aggiunta). Chiamarla direttamente su una stringa letterale, come nell'esempio scritto nelle slide, vorrebbe dire modificare una costante, che è comportamento indefinito (capitolo 26 della teoria). Quali caratteri contino come vocali (solo minuscole o anche maiuscole, lettere accentate) va controllato sulla specifica di Moodle; `is_vowel` del capitolo 16 considera `AEIOUaeiou`.

## Riepilogo
- Una stringa si scorre con un puntatore: `*p` legge il carattere corrente, `p++` avanza, il ciclo si ferma su `'\0'`.
- `codifica` sposta ogni maiuscola alla lettera successiva, con Z→A; `decodifica` fa il contrario, con A→Z; gli altri caratteri restano invariati.
- `elimina_vocali` è una riduzione sul posto con due puntatori: `pSrc` legge tutto, `pDst` scrive solo i caratteri da tenere, e alla fine riceve il terminatore.
- Le funzioni che modificano una stringa hanno un parametro `char*` senza `const` e vanno chiamate su array modificabili.

Il capitolo 20 introduce gli intervalli semiaperti di indici e li usa per lavorare su sottoparti di un array.
