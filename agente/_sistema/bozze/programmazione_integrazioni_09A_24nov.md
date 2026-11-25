@@ dopo cap47.21
Nella versione delle slide del 24 novembre la frase è attenuata: la prima dimensione si può omettere perché il linguaggio lo consente, e «tipicamente» il corso non userà questo approccio. La forma `int (*m)[cols]` torna infatti, come puntatore a una matrice allocata nello heap, nel capitolo 50.

@@ dopo cap48.35
Nella versione delle slide del 24 novembre il `main` non stampa più la matrice con i due cicli, ma chiama la funzione `stampaMatrice` del capitolo 47, `stampaMatrice(ROWS, COLS, s);`, e lo stesso fa il programma di prova del prodotto di matrici. I numeri stampati sono gli stessi; con la `stampaMatrice` del capitolo 47 ogni riga comparirebbe tra parentesi quadre. Nella slide del prodotto la chiamata è scritta `stampaMatrice(M, P, s);`, ma lì la matrice risultato si chiama `prod`: va letta `stampaMatrice(M, P, prod);` (precisazione aggiunta).

@@ dopo cap48.46
La soluzione del docente del prodotto di matrici, pubblicata dopo la lezione, è riportata nel capitolo 52: invece della variabile `s` usa direttamente `c[i][j]` come accumulatore, azzerandolo prima del ciclo su `k`, con lo stesso risultato.

@@ dopo cap49.85
Le soluzioni del docente dei due esercizi, con i test, sono nel capitolo 52.
