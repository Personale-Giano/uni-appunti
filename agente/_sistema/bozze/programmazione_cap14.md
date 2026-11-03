# Capitolo 14: Numeri Reali in C: float, double e Formati di Stampa
## I tipi per i numeri reali
Nel calcolo scientifico e in moltissime applicazioni pratiche (grafica, simulazioni, elaborazione di dati) occorre lavorare con numeri reali, cioè con valori che hanno una parte intera e una parte frazionaria. In C sono rappresentati principalmente da due tipi: **float**, tipicamente a 32 bit, e **double**, tipicamente a 64 bit. Hanno entrambi una codifica in virgola mobile, che segue lo standard IEEE 754, argomento che si vedrà nel corso di Fondamenti dell'Informatica. Come già osservato nel capitolo 6, sono modelli finiti dei numeri reali: i due tipi si distinguono proprio per la **precisione** e per l'**intervallo** di valori che riescono a rappresentare.
- **float**: 32 bit (4 byte), circa 7 cifre decimali di precisione, valori da circa 10^{-38} a circa 10^{38}. È adatto quando serve risparmiare memoria o per calcoli meno critici.
- **double**: 64 bit (8 byte), circa 15-16 cifre decimali, valori da circa 10^{-308} a circa 10^{308}. È il tipo per i calcoli scientifici e per le applicazioni che richiedono alta precisione.

Sui numeri reali valgono le quattro operazioni aritmetiche: addizione (+), sottrazione (-), moltiplicazione (*) e divisione (/). Non c'è invece l'operatore modulo (%), che in C è definito solo per gli interi: esiste una funzione di libreria con questo scopo, chiamata fmod, ma il corso non la userà.

## float e double in memoria
Vediamo un primo esempio. Il programma calcola la divisione tra due variabili reali e stampa i tre valori:

```c
int main(void) {
    float x = 5, y = 2, z;
    z = x / y;
    printf("La var x vale %f\n", x);
    printf("La var y vale %f\n", y);
    printf("La var z vale %f\n", z);
}
```

L'output è `La var x vale 5.000000`, `La var y vale 2.000000` e `La var z vale 2.500000`. Poiché gli operandi sono reali, la divisione mantiene la parte frazionaria: 5 / 2 dà 2.5. In memoria ciascuna delle tre variabili float occupa 4 byte. Se si sostituisce float con **double** il risultato stampato è identico, ma ogni variabile occupa 8 byte (64 bit). I due tipi si possono anche mescolare: se x e y sono float e z è un double, la divisione tra x e y dà comunque 2.5, che viene memorizzato in una variabile da 8 byte.

![float e double in memoria: stesse operazioni, ma 4 byte per ogni float e 8 byte per ogni double.](figure/prog/ch14_float_double_memoria.png|12)

## Stampare i numeri reali: %f, %e e %g
Per stampare un numero reale con printf si usano tre specificatori di conversione, che differiscono per la notazione. Prendiamo come esempio `double z = 2.5;`:
- **%f**: notazione decimale fissa, con 6 cifre decimali di default (2.500000). È la scelta per la rappresentazione "naturale" di un numero reale.
- **%e**: notazione scientifica o esponenziale (2.500000e+00). È utile per numeri molto grandi o molto piccoli.
- **%g**: formato adattivo, che sceglie tra %f e %e quello più compatto ed elimina gli zeri inutili (2.5). Si usa quando serve una stampa leggibile e compatta, senza preoccuparsi della notazione; stampa al più 6 cifre significative.

Come per gli interi, dove `%6d` fissa la larghezza minima del campo (capitolo 8), anche qui si può controllare la formattazione: scrivendo un punto e un numero tra il simbolo % e la lettera, come in `%.3f`, si indica la **precisione**, cioè quante cifre decimali stampare. Con la stessa variabile z:

```c
printf("z vale %f\n", z);      // z vale 2.500000
printf("z vale %.3f\n", z);    // z vale 2.500
printf("z vale %.3e\n", z);    // z vale 2.500e+00
```

Con `%.3f` la stampa si ferma al terzo decimale (più precisamente il valore viene arrotondato: 2.5678 con `%.3f` diventa 2.568); con `%.3e` la notazione esponenziale mostra tre decimali. Gli specificatori di printf sono descritti nel manuale della libreria C di GNU (sezione sull'output formattato), a cui conviene abituarsi a ricorrere.

## Leggere i double con scanf
In printf lo specificatore **%f** va bene sia per i float sia per i double, ed è quello usato negli esempi precedenti. Con scanf la distinzione invece conta: per leggere un **double** non si possono usare %f, %e e %g, ma gli specificatori con la lettera l, cioè **%lf**, **%le** e **%lg**. La ragione sta nel funzionamento di scanf, che scrive direttamente nella memoria all'indirizzo passato (&x, capitolo 9) e deve sapere quanti byte occupa la variabile: 8 per un double, 4 per un float. Usare %f con un double significherebbe scriverne solo una parte, con un valore letto sbagliato. La tabella dei tipi del corso riporta coerentemente %f per il float e %lf per il double.

In sintesi, per i numeri reali si stampa con %f, %e o %g (a seconda della notazione che si vuole) e si legge con %f, %e o %g per un float e con %lf, %le o %lg per un double.

I numeri reali sono approssimati, e le conversioni tra i tipi numerici possono far perdere informazione: è il tema del capitolo 16. Il prossimo capitolo introduce invece le funzioni matematiche della libreria math.h.
