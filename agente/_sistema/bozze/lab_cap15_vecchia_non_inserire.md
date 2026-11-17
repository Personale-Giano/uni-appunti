# Capitolo 15: Laboratorio 6: Progettare Funzioni, Numeri Primi, Funzioni Iterative e Cambio Monete
## Come si definisce una funzione
Il laboratorio 6, «Funzioni», mette in pratica i capitoli 27-33 della teoria. Le funzioni permettono di dividere il programma in blocchi di codice separati, ciascuno con un compito specifico. Per ogni sotto-compito di un programma bisogna decidere tre cose: un **nome** chiaro e conciso, i **parametri** in ingresso necessari per svolgere il compito (che possono anche mancare) e il **tipo di ritorno**, cioè il tipo del dato che la funzione restituisce (anche questo facoltativo: se non restituisce nulla il tipo è `void`). Lo schema delle slide è:

```c
tipo_di_ritorno nome_funzione(param1, param2, ...) {
    <codice della funzione>
}
```

Nello schema i parametri sono scritti senza tipo, ma in C ciascun parametro va dichiarato con tipo e nome, per esempio `int n` (precisazione aggiunta). La prima riga, terminata da un punto e virgola invece che dal corpo, è il **prototipo**: si scrive prima del `main()` per annunciare al compilatore che la funzione esiste, e la definizione completa può stare dopo (capitolo 27 della teoria). È lo schema usato in `primi.c` e `funzioni_iterative.c` del codice iniziale, dove i prototipi in cima hanno dei `???` al posto di tipi e parametri.

(In parole povere: progettare una funzione vuol dire rispondere a tre domande: come la chiamo, cosa le devo dare, cosa mi restituisce. Il prototipo è la risposta scritta in una riga.)

## Quattro esercizi di progettazione
Le slide propongono quattro compiti, e per ciascuno chiedono quale nome usare, quali parametri in ingresso e quale tipo di ritorno. Le risposte che seguono sono proposte nostre, ragionate: le slide non le danno.

**Esercizio 1: saluta l'utente.** La funzione scrive sul terminale «Buongiorno!». Non ha bisogno di dati e non deve calcolare niente, quindi non ha parametri né valore di ritorno: `void saluta(void);`. È la quarta delle forme di funzione del capitolo 27 della teoria.

**Esercizio 2: determina se un numero è primo.** La risposta è sì o no, quindi il tipo di ritorno naturale è `bool` (da `<stdbool.h>`); serve un solo parametro, il numero: `bool verifica_primalita(int n);`. Un nome che comincia con un verbo, o una domanda come `is_primo`, rende chiaro che il risultato è vero o falso.

**Esercizio 3: ricerca in un array.** La funzione conta le occorrenze del numero `n` in un array di interi `a[]`. Il risultato è un conteggio, che non può essere negativo: un buon tipo è `size_t`. I parametri sono l'array, il valore cercato e, cosa da non dimenticare, la lunghezza dell'array, perché la funzione da sola non può conoscerla (capitolo 16 di questo laboratorio): `size_t conta_occorrenze(size_t len, const int a[], int n);`. Il `const` dice che la funzione legge l'array senza modificarlo.

**Esercizio 4: indici di una sequenza in input.** La funzione legge da input una sequenza di interi positivi e, se non ci sono errori, restituisce la media e la varianza. Qui la difficoltà è che i risultati sono tre: l'esito (tutto bene o errore), la media e la varianza, mentre una funzione C restituisce al massimo un valore (capitolo 28 della teoria). Una soluzione è restituire l'esito come `bool` e consegnare media e varianza attraverso due puntatori, con il passaggio per riferimento simulato del capitolo 32 della teoria: `bool statistiche_sequenza(double* media, double* varianza);`. Non servono parametri di ingresso, perché i dati arrivano dalla tastiera.

## Verifica esaustiva di primalità
Un numero naturale n > 1 è primo se è divisibile soltanto per se stesso e per 1. La domanda «n è primo?» diventa quindi «esiste un divisore d di n con 2 ≤ d < n?», e la verifica esaustiva prova tutti i candidati. Per 7 nessuno fra 2, 3, 4, 5 e 6 è un divisore, quindi 7 è primo. Per 9, il 2 non è un divisore ma il 3 sì: a quel punto la risposta è già nota, i candidati da 4 a 8 non vanno controllati e 9 non è primo.

(In parole povere: per sapere se un numero è primo si cerca un divisore «intruso»; appena se ne trova uno ci si ferma, se non se ne trova nessuno il numero è primo.)

È una quantificazione esistenziale (capitolo 35 della teoria) con la sentinella nella condizione del ciclo, lo schema già visto nel capitolo 14 di questo laboratorio.

## Il programma primi.c
Si deve completare `primi.c` dichiarando e implementando una funzione `verifica_primalita`, che prende un intero maggiore di 1 e restituisce un valore che indica se è primo, e poi usarla nel `main()` per stampare tutti i primi minori di 100. Alla domanda delle slide su quale sia il tipo appropriato da restituire, il commento del codice iniziale risponde da solo: la funzione «ritorna true se n è primo, false altrimenti», e ritorna sempre `false` per n < 2, quindi il tipo è `bool`. Una soluzione proposta, verificata simulandone la logica (non nelle slide):

```c
#include <stdio.h>
#include <stdbool.h>

// Prototipo della funzione:
bool verifica_primalita(int n);

int main(void) {
    // stampa i numeri primi minori di 100
    for (int n = 2; n < 100; n++) {
        if (verifica_primalita(n))
            printf("%d ", n);
    }
    printf("\n");
}

// ritorna true se n è primo, false altrimenti
// ritorna sempre false per qualsiasi n < 2
bool verifica_primalita(int n) {
    bool primo = (n >= 2);
    for (int d = 2; d < n && primo; d++) {
        if (n % d == 0)
            primo = false;
    }
    return primo;
}
```

La sentinella `primo` parte già falsa se n < 2, e allora il ciclo non parte nemmeno; altrimenti diventa falsa al primo divisore trovato e il ciclo si ferma. C'è un solo `return`, alla fine, come raccomandato nel capitolo 28 della teoria. L'output è l'elenco atteso dalle slide, 25 numeri:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

Considerazione nostra: basterebbe provare i divisori con d · d ≤ n, perché se n = a · b uno dei due fattori è al massimo √n; per 97 si proverebbe fino a 9 invece che fino a 96. Le slide chiedono però la verifica esaustiva.

## Le funzioni iterative
Il file `funzioni_iterative.c` contiene un `main()` già completo, da non modificare, che chiama tre funzioni e stampa accanto a ogni risultato il valore atteso. Il `main()` stampa i risultati con `%3d`, quindi le prime due funzioni devono restituire un `int`. Le soluzioni seguenti sono proposte nostre, verificate simulandone la logica su tutti i valori attesi del `main()`.

**esponenziale.** Data una base b e un esponente e ≥ 0, restituisce b elevato a e. Si parte da 1 e si moltiplica per b, e volte:

```c
int esponenziale(int b, int e) {
    int risultato = 1;
    for (int i = 0; i < e; i++) {
        risultato *= b;
    }
    return risultato;
}
```

Partire da 1 sistema da solo il caso e = 0: il ciclo non viene eseguito e il risultato è 1, compreso `esponenziale(0, 0)`, per cui il `main()` si aspetta proprio 1 (è la convenzione 0^{0} = 1). Gli altri casi danno 729, 125, 4, 1, 0, 1 e 5, come atteso. La libreria `<math.h>`, inclusa nel file, ha `pow`, ma lavora con i `double`: qui si chiede di scrivere il ciclo.

**prodotto_multipli.** Presi tre interi non negativi n, m e q, restituisce il prodotto degli interi fra n e m, estremi inclusi, che sono multipli di q:

```c
int prodotto_multipli(int n, int m, int q) {
    int prodotto = 1;
    for (int i = n; i <= m; i++) {
        if (i % q == 0)
            prodotto *= i;
    }
    return prodotto;
}
```

Il prodotto parte da 1, l'elemento neutro della moltiplicazione, come la somma parte da 0. Le verifiche: per (3, 6, 2) i multipli di 2 sono 4 e 6, prodotto 24; per (1, 30, 10) sono 10, 20 e 30, prodotto 6000; per (27, 42, 8) sono 32 e 40, prodotto 1280. Precisazione aggiunta: il testo ammette q non negativo, ma con q = 0 l'espressione `i % q` è una divisione per zero, che in C ha comportamento indefinito; bisogna assumere q > 0. Se nessun numero dell'intervallo è multiplo di q, la funzione restituisce 1, il prodotto vuoto. Con n = 0, invece, il risultato è 0, perché 0 è multiplo di ogni q.

**stampa_al_rovescio.** Preso un intero n ≥ 0, stampa i valori da n a 0. Non restituisce niente, quindi è `void`:

```c
void stampa_al_rovescio(int n) {
    for (int i = n; i >= 0; i--) {
        printf("%d", i);
        if (i > 0)
            printf(" ");   // spazio solo tra un numero e il successivo
    }
    printf("\n");
}
```

Per 5 stampa `5 4 3 2 1 0`, per 0 stampa `0`, e la riga non finisce con uno spazio. Il contatore deve avere il segno: il ciclo finisce quando `i` diventa -1, e un `size_t` non può farlo (si veda la sezione su `size_t` e `ptrdiff_t` più avanti). I prototipi da mettere al posto dei `???` in cima al file sono le prime righe delle tre funzioni seguite dal punto e virgola, per esempio `int esponenziale(int b, int e);`.

## Il cambio monete
Si scrive un programma `monete.c` che chiede un numero naturale `cent`, interpretato in centesimi, e stampa il più piccolo cambio in monete. I tagli sono già nel codice iniziale:

```c
#define NUM_TAGLI 6
const int tagli_monete[NUM_TAGLI] = {1,2,5,10,20,50};
```

Per 95 centesimi l'output è «1 da 50 cent», «2 da 20 cent», «1 da 5 cent». Gli altri esempi delle slide sono 120 (2 da 50, 1 da 20), 367 (7 da 50, 1 da 10, 1 da 5, 1 da 2) e 473 (9 da 50, 1 da 20, 1 da 2, 1 da 1). Come si vede, i tagli che non servono non vengono stampati.

La strategia è partire dal taglio più grande e prenderne il più possibile, poi passare al successivo con quello che resta. Il suggerimento delle slide è una funzione **cambio_taglio**, che prende un ammontare in centesimi e un taglio, calcola quante volte x può sottrarre il taglio dall'ammontare, stampa «x da t cent» e ritorna il resto, cioè l'ammontare iniziale meno x · t. Nel `main()` la si chiama più volte, aggiornando man mano la somma rimanente.

(In parole povere: è come pagare con le monete più grosse che si hanno in tasca, finché si può, e poi scendere a quelle più piccole per il resto.)

Una soluzione proposta, verificata simulandone la logica sui quattro esempi delle slide (non nelle slide):

```c
#include <stdio.h>
#include <stddef.h>   // per ptrdiff_t

int cambio_taglio(int ammontare, int taglio);

int main(void) {
    // Chiedi all'utente la somma da convertire
    int cent;
    printf("Scrivere l'ammontare da convertire in monete: ");
    scanf("%d", &cent);

    // Definiamo i tagli delle monete
#   define NUM_TAGLI 6
    const int tagli_monete[NUM_TAGLI] = {1,2,5,10,20,50};

    // dal taglio più grande al più piccolo
    for (ptrdiff_t i = NUM_TAGLI - 1; i >= 0; i--) {
        cent = cambio_taglio(cent, tagli_monete[i]);
    }
}

// stampa quante monete di valore taglio servono e ritorna il resto
int cambio_taglio(int ammontare, int taglio) {
    int x = ammontare / taglio;   // quante volte si può sottrarre taglio
    if (x > 0)
        printf("%d da %d cent\n", x, taglio);
    return ammontare - x * taglio;
}
```

Contare quante volte si può sottrarre il taglio equivale a fare la divisione intera: per 95 e il taglio 50, x = 95 / 50 = 1 e il resto è 45. Si potrebbe anche scrivere un `while (ammontare >= taglio)` che sottrae e conta, con lo stesso risultato. L'`if (x > 0)` serve per non stampare righe come «0 da 10 cent», che negli esempi non compaiono. Il `main()` non tocca la variabile `cent` direttamente: è la funzione a restituire il nuovo valore, perché il parametro `ammontare` è una copia (passaggio per valore, capitolo 28 della teoria).

Considerazione nostra: scegliere ogni volta il taglio più grande non dà il cambio minimo per qualunque insieme di tagli, ma con 1, 2, 5, 10, 20 e 50 sì; lo abbiamo controllato confrontando il risultato con il minimo vero per tutti gli importi da 0 a 1000.

## size_t e ptrdiff_t nei cicli che scendono a zero
Il secondo suggerimento delle slide riguarda proprio il ciclo del `main()`. Il tipo `size_t` è unsigned, quindi non può rappresentare valori negativi, e un ciclo come questo non funziona:

```c
for (size_t i = N - 1; i >= 0; i--) { ... }   // SBAGLIATO
```

La condizione `i >= 0` è sempre vera: quando `i` vale 0 e si esegue `i--`, il valore non diventa -1 ma il più grande `size_t` rappresentabile, e il ciclo continua leggendo fuori dall'array. Nei casi in cui servono indici che possono diventare negativi, come i cicli che decrementano fino a zero, si usa **ptrdiff_t**, il tipo intero con segno per gli indici definito in `<stddef.h>` (capitolo 24 della teoria); il suo specificatore di `printf` è `%td`.

(In parole povere: un contatore senza segno è come un contachilometri che, sotto lo zero, torna al numero più alto invece di diventare negativo; per contare all'indietro fino a zero serve un contatore che sappia andare sotto zero.)

## Esercizio: Statistiche sequenze
Sulla pagina Moodle c'è l'esercizio **Lab06-Es1 Statistiche sequenze**: si deve completare il programma in modo che passi tutti i test proposti. Le slide pongono due domande: quali parametri deve avere la funzione `leggi_sequenza` e che cosa deve restituire al chiamante. Il testo sta su Moodle, quindi la risposta va cercata nella specifica; il ragionamento è lo stesso dell'esercizio 4 di progettazione, quando i risultati sono più d'uno.

Le slide aggiungono una nota: per questo esercizio non servono gli array, perché somma, somma dei quadrati e massimo si possono calcolare mentre si leggono i valori. Considerazione nostra: la somma dei quadrati serve per la varianza, che si può ottenere come media dei quadrati meno il quadrato della media, σ^{2} = (Σx_{i}^{2})/n − (Σx_{i}/n)^{2}; per esempio per 2, 4, 4, 4, 5, 5, 7, 9 la media è 5 e la varianza è 29 − 25 = 4. Quale formula della varianza usare (divisione per n o per n − 1) va verificato nel testo su Moodle.

Il prossimo capitolo affronta il passaggio di array e stringhe alle funzioni.
