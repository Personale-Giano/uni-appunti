# Capitolo 21: Laboratorio 7: Funzioni sulle Stringhe senza string.h e Sottosequenze con Errori
## Es 8: il file my_string.c
L'ultimo esercizio di codice del laboratorio chiede di implementare le funzioni di `08_my_string.c` **senza usare** le funzioni di `<string.h>`: il file stesso avverte di non includerlo. Alcuni prototipi hanno dei `???` al posto del tipo di ritorno o dei parametri, che vanno scelti. Le funzioni che scrivono una stringa ricevono la destinazione come intervallo [dstStart, dstStart + strLen): `dstStart` è l'inizio del buffer, `strLen` il numero di `char` disponibili, terminatore compreso. Dai test del `main` si capisce che è proprio così: in un buffer di 10 `char` ci stanno al massimo 9 caratteri più il `'\0'`.

Seguono soluzioni possibili (non nelle slide), controllate a mano su tutti i casi del `main`. Usano gli indici, come le funzioni del capitolo 20 di questo laboratorio; in tutte la posizione di scrittura `k` resta sotto `strLen − 1` finché si copiano caratteri, così l'ultima casella resta libera per il terminatore.

**my_concat.** Copia nel buffer i caratteri di `str1` seguiti da quelli di `str2`, poi il terminatore; se lo spazio finisce, la copia si interrompe:

```c
void my_concat(char* dstStart, const size_t strLen,
               const char* str1, const char* str2)
{
    if (strLen > 0) {          // senza spazio non si scrive nemmeno il terminatore
        size_t k = 0;          // prossima posizione libera nel buffer
        for (size_t i = 0; str1[i] != '\0' && k < strLen - 1; i++) {
            dstStart[k] = str1[i];
            k++;
        }
        for (size_t i = 0; str2[i] != '\0' && k < strLen - 1; i++) {
            dstStart[k] = str2[i];
            k++;
        }
        dstStart[k] = '\0';
    }
}
```

Il controllo `strLen > 0` serve per il caso del `main` `my_concat(buffer1, 0, s1, s2)`, che «non deve rompersi, né copiare nulla»: con zero posti non c'è spazio neppure per il terminatore, e in più `strLen - 1` su un `size_t` uguale a 0 darebbe il valore massimo invece di −1. Con `"Prog"` e `"rammazione"` in 20 `char` il risultato è `Programmazione` (14 caratteri); in 10 `char` è `Programma`, cioè 9 caratteri più il terminatore.

**my_equal.** Restituisce `true` se le due stringhe sono identiche carattere per carattere. I `???` del prototipo diventano `bool my_equal(const char* s1, const char* s2);`:

```c
bool my_equal(const char* s1, const char* s2)
{
    size_t i = 0;
    while (s1[i] != '\0' && s1[i] == s2[i]) {
        i++;
    }
    return s1[i] == s2[i];   // uguali solo se finiscono insieme
}
```

Il ciclo avanza finché i caratteri coincidono e `s1` non è finita. All'uscita ci sono due possibilità: o si è trovata una differenza, e allora `s1[i] != s2[i]`, o `s1` è finita, e allora le stringhe sono uguali solo se anche `s2` finisce lì. Non si esce mai da `s2`: se `s2` finisse prima di `s1`, il suo `'\0'` sarebbe diverso dal carattere corrispondente di `s1` e il ciclo si fermerebbe. Così `"melagrana"` e `"mela"` danno `false` (in posizione 4, `'g'` contro `'\0'`), e lo stesso con le due stringhe scambiate; `""` e `""` danno `true`.

**n_uplica_lettere.** Copia nel buffer ogni carattere di `str` ripetuto `N` volte, poi il terminatore, fermandosi se lo spazio finisce:

```c
void n_uplica_lettere(char* dstStart, const size_t strLen,
                      const char* str, const size_t N)
{
    if (strLen > 0) {
        size_t k = 0;
        for (size_t i = 0; str[i] != '\0' && k < strLen - 1; i++) {
            for (size_t r = 0; r < N && k < strLen - 1; r++) {
                dstStart[k] = str[i];
                k++;
            }
        }
        dstStart[k] = '\0';
    }
}
```

Il controllo sullo spazio sta in **tutti e due** i cicli, perché il buffer si può riempire a metà delle ripetizioni di una lettera. Risultati: `"aBc"` con N = 3 dà `aaaBBBccc`; `"XyZ"` con N = 4 in 10 `char` dà `XXXXyyyyZ`, perché dopo 9 caratteri resta solo il posto del terminatore; la stringa vuota dà la stringa vuota; con N = 0 il ciclo interno non scrive niente e il risultato è vuoto; `"mela"` con N = 2 dà `mmeellaa`.

Per quest'ultimo caso il `main` del codice iniziale indica come atteso `mmeella`, con una sola `a` finale (precisazione aggiunta). È un refuso del valore atteso: ogni lettera va ripetuta due volte, e gli 8 caratteri di `mmeellaa` stanno nel buffer di 10 `char` insieme al terminatore, quindi la copia non viene interrotta.

**my_strlen.** Restituisce la lunghezza della stringa, terminatore escluso, come `strlen` (capitolo 16 di questo laboratorio). Il prototipo diventa `size_t my_strlen(const char* str);`:

```c
size_t my_strlen(const char* str)
{
    size_t len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}
```

L'indice del terminatore è proprio la lunghezza: `""` dà 0, `"programmazione-1"` dà 16, `"banana"` dà 6, `"a"` dà 1. Il tipo di ritorno è `size_t` perché una lunghezza non è mai negativa, e il `main` la stampa con `%2zu` (lo specificatore dei `size_t`, su almeno due caratteri).

**startswith.** Restituisce `true` se `str` inizia con `prefix`; la stringa vuota è prefisso di ogni stringa. Il prototipo diventa `bool startswith(const char* str, const char* prefix);`:

```c
bool startswith(const char* str, const char* prefix)
{
    size_t i = 0;
    while (prefix[i] != '\0' && str[i] == prefix[i]) {
        i++;
    }
    return prefix[i] == '\0';   // il prefisso è stato confrontato tutto
}
```

Si confrontano i caratteri finché il prefisso non finisce; la risposta è sì se il ciclo è arrivato al terminatore di `prefix`. Come in `my_equal`, se `str` finisce prima, il suo `'\0'` è diverso dal carattere del prefisso e il ciclo si ferma. Con `("programma", "programmazione")` il ciclo si ferma in posizione 9, dove `str` è finita e `prefix` ha ancora la `'z'`: `false`. Con prefisso vuoto il ciclo non parte e la risposta è `true`, come chiede la nota del commento.

**contains.** Restituisce `true` se `str` contiene la sottostringa `sub`, e scrive in `*left` e `*right` l'intervallo semiaperto della prima occorrenza: `*left` è l'indice del primo carattere di `str` che fa parte di `sub`, `*right` quello del primo carattere che non ne fa più parte. Se `sub` non c'è, il `main` si aspetta `false` con l'intervallo [0, 0). La stringa vuota è contenuta in ogni stringa.

```c
bool contains(const char* str, const char* sub,
              size_t* left, size_t* right)
{
    const size_t strLen = my_strlen(str);
    const size_t subLen = my_strlen(sub);
    *left = *right = 0;
    bool trovata = false;
    for (size_t i = 0; i + subLen <= strLen && !trovata; i++) {
        if (startswith(str + i, sub)) {     // sub inizia nella posizione i?
            trovata = true;
            *left = i;
            *right = i + subLen;
        }
    }
    return trovata;
}
```

È una ricerca lineare (capitolo 35 della teoria) sulle posizioni di partenza possibili, che riusa `startswith`: `str + i` è il puntatore al carattere in posizione `i`, cioè la parte di `str` che comincia lì, e l'aritmetica dei puntatori del capitolo 19 di questo laboratorio permette di passarla come una stringa a sé. Fermandosi alla prima posizione buona si ottiene la prima occorrenza. La condizione `i + subLen <= strLen` esclude le partenze troppo vicine alla fine, dove `sub` non può entrare; è scritta come somma e non come `i <= strLen - subLen` perché, con i `size_t`, la sottrazione darebbe un numero enorme invece di un valore negativo quando `sub` è più lunga di `str`, e il ciclo leggerebbe fuori dalla stringa.

Risultati: `"prog"` in `"programmazione"` dà `true` con [0, 4); `"programmazione"` in `"stringhe"` dà `false` con [0, 0), perché il ciclo non parte nemmeno; la stringa vuota dà `true` con [0, 0), sia in `"programmazione"` sia in `""`; `"azione"` in `"programmazione"` dà `true` con [8, 14), dato che la `a` di «azione» è il carattere di indice 8 e la sottostringa ha 6 caratteri.

(In parole povere: si appoggia la parola cercata sotto il testo, partendo dalla prima lettera, e la si fa scorrere di una posizione alla volta finché non combacia; l'intervallo dice dove combacia.)

## Es 9: Sottosequenze con errori
Sulla pagina Moodle c'è l'esercizio **Lab07-Es4 Sottosequenze con errori**; la slide ne dà solo la definizione di base, e il testo completo va letto su Moodle.

**Definizione.** Due sequenze `a[]` e `b[]` della stessa lunghezza `len` sono **in match con al più n errori** se le coppie di elementi nelle stesse posizioni sono uguali, tranne al più `n` coppie di elementi diversi.

(In parole povere: si mettono le due sequenze una sopra l'altra e si contano le colonne in cui i numeri non coincidono; se le colonne sbagliate sono al massimo n, le sequenze «si somigliano abbastanza».)

Nell'esempio della slide `a` = 0, 3, 2, 4, 3 e `b` = 0, 3, 1, 4, 5: le posizioni 0, 1 e 3 coincidono, le posizioni 2 e 4 no, quindi le sequenze sono in match con 2 errori; sono in match «con al più n errori» per ogni n ≥ 2, e non lo sono per n = 0 o n = 1.

Una funzione possibile per la sola definizione (non nelle slide; la firma richiesta su Moodle può essere diversa) conta le posizioni diverse, fermandosi appena gli errori superano `n`:

```c
// true se a[] e b[], lunghi len, differiscono in al più n posizioni
bool match_con_errori(size_t len, const int a[], const int b[], size_t n)
{
    size_t errori = 0;
    for (size_t i = 0; i < len && errori <= n; i++) {
        if (a[i] != b[i]) {
            errori++;
        }
    }
    return errori <= n;
}
```

È un conteggio (capitolo 24 della teoria) con una sentinella nella condizione del ciclo: quando `errori` supera `n` la risposta è già «no» e non serve guardare il resto. Sull'esempio, con `n = 2` si contano 2 errori e la risposta è `true`; con `n = 1` il ciclo si ferma subito dopo il secondo errore, in posizione 4, e la risposta è `false`. Il titolo dell'esercizio parla di sottosequenze: è probabile che la funzione vada applicata a sotto-intervalli di un array più lungo, per esempio cercando una posizione `i` in cui `[i, i + len)` sia in match con `b`, ma come vadano usati gli intervalli lo dice solo la specifica su Moodle (da verificare).

## Riepilogo
- Le funzioni che scrivono una stringa in un buffer di `strLen` `char` scrivono al massimo `strLen − 1` caratteri e poi il terminatore; con `strLen == 0` non scrivono niente.
- `my_equal` e `startswith` avanzano finché i caratteri coincidono; la risposta dipende da dove si sono fermate. Non escono mai dalle stringhe, perché un terminatore interrompe il confronto.
- `my_strlen` conta i caratteri prima di `'\0'`; `contains` è una ricerca lineare delle posizioni di partenza, con `startswith(str + i, sub)`.
- Con i `size_t` conviene scrivere `i + subLen <= strLen` invece di sottrarre, e controllare `strLen > 0` prima di calcolare `strLen - 1`.
- Due sequenze sono in match con al più n errori se differiscono in al più n posizioni: è un conteggio che si può interrompere appena supera n.
