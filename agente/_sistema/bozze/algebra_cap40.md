# 40. Risolvere un Sistema Lineare: Parametri Liberi
## Dalla matrice alle soluzioni
Si può ora descrivere esplicitamente l'insieme S ⊂ 𝕂ⁿ delle soluzioni. Il sistema è descritto da C = (A | b): con l'algoritmo di Gauss-Jordan si trasforma C in una matrice a scalini in cui ogni pivot vale 1 e tutti i numeri sopra i pivot sono nulli. Indicativamente, con ? per un numero qualsiasi, la matrice ha questa forma:

( 0 1 ? 0 0 ? | ? ; 0 0 0 1 0 ? | ? ; 0 0 0 0 1 ? | ? ).

Si guardano le colonne che contengono i pivot, qui la seconda, la quarta e la quinta: ciascuna ha un 1 al posto del pivot e 0 in tutte le altre caselle. Ci sono due casi.

**La ricetta della lavagna (registrazione 2025):**
1. Si scrive la matrice completa C = (A | b).
2. Si applica Gauss: C diventa a scalini.
3. Da qui ci sono due strade che danno le stesse soluzioni: (a) si continua con Gauss-Jordan e si legge il risultato; (b) ci si ferma a Gauss, si riscrive il sistema e si risolve risalendo dal basso.

**All'esame**, raccomanda il docente, il primo passo è sempre scrivere la matrice completa, senza farsi prendere dal panico.

I calcoli vanno fatti comunque, ma secondo il docente di solito la strada (b) è un po' più veloce di tutto Gauss-Jordan, e in pratica conviene riscrivere subito il sistema.

## Primo caso: un pivot nei termini noti
Se la colonna dei termini noti b contiene un pivot, la matrice è di questo tipo:

( 0 1 ? 0 0 ? | 0 ; 0 0 0 1 0 ? | 0 ; 0 0 0 0 0 0 | 1 ).

L'ultima riga rappresenta l'equazione **0 = 1**, che chiaramente non può avere soluzione. In questo caso **S = ∅**.

(In parole povere: se a forza di semplificare si arriva a «0 = 1», le equazioni di partenza si contraddicevano: nessun valore le soddisfa tutte.)

**Esempio dalla lavagna (registrazione 2025).** Il sistema y + z = 0, x + y + 2z = −3, −x + 2y + z = 1 ha come matrice completa quella ridotta nel cap. 39. Con la strada (a) si arriva a ( 1 0 1 | 0 ; 0 1 1 | 0 ; 0 0 0 | 1 ), cioè 0 = 1; con la strada (b) ci si ferma a ( 1 1 2 | −3 ; 0 1 1 | 0 ; 0 0 0 | −2 ), cioè 0 = −2. In entrambi i casi **non ci sono soluzioni**.

## Secondo caso: nessun pivot nei termini noti
Se l'ultima colonna non contiene pivot, la matrice è di questo tipo:

( 0 1 a_{13} 0 0 a_{16} | b_{1} ; 0 0 0 1 0 a_{26} | b_{2} ; 0 0 0 0 1 a_{36} | b_{3} ).

Ogni colonna corrisponde a una variabile x_{1}, …, x_{n}, eccetto l'ultima. Si assegna allora un parametro t_{1}, t_{2}, … a ciascuna variabile la cui colonna **non** contiene un pivot.

**Definizione.** I **parametri liberi** t_{1}, t_{2}, … sono i valori assegnati alle variabili che non corrispondono a una colonna con un pivot; possono assumere qualsiasi valore in 𝕂, e le altre variabili dipendono da essi.

(In parole povere: le variabili senza pivot si possono scegliere come si vuole; una volta scelte, quelle con il pivot sono obbligate.)

Il caso più semplice viene da una domanda nella registrazione 2025: se in A c'è una colonna tutta nulla, la variabile corrispondente non compare mai e può assumere qualsiasi valore. Se il sistema ha soluzioni, quindi, ne ha infinite.

Nell'esempio si scrive x_{1} = t_{1}, x_{3} = t_{2}, x_{6} = t_{3}, e il sistema diventa

x_{2} + a_{13}t_{2} + a_{16}t_{3} = b_{1},   x_{4} + a_{26}t_{3} = b_{2},   x_{5} + a_{36}t_{3} = b_{3}.

Spostando i parametri a destra dell'uguale e aggiungendo le assegnazioni dei parametri liberi si ottiene il risultato:
- x_{1} = t_{1};
- x_{2} = b_{1} − a_{13}t_{2} − a_{16}t_{3};
- x_{3} = t_{2};
- x_{4} = b_{2} − a_{26}t_{3};
- x_{5} = b_{3} − a_{36}t_{3};
- x_{6} = t_{3}.

Il sistema è risolto: le variabili x_{1}, …, x_{n} dipendono dai parametri liberi come indicato. Il numero di parametri liberi è il numero di colonne senza pivot, esclusa quella dei termini noti.

**Tre esempi dalla lavagna (registrazione 2025)**, tutti con matrice già a scalini:
- ( 1 2 3 | 4 ; 0 2 4 | 5 ; 0 0 1 | 1 ) non è ridotta, quindi si risale dal basso: z = 1; poi 2y + 4 = 5, cioè y = ½; poi x + 1 + 3 = 4, cioè x = 0. Soluzione unica (0, ½, 1).
- ( 1 0 0 | 4 ; 0 1 0 | 3 ; 0 0 1 | 5 ) è ridotta e si legge subito: soluzione unica (4, 3, 5).
- ( 1 0 1 0 | 4 ; 0 1 1 0 | 3 ; 0 0 0 1 | 5 ), con variabili x, y, z, w, ha la colonna di z senza pivot, quindi z è libera: (x, y, z, w) = (4 − t, 3 − t, t, 5). Sono infinite soluzioni che dipendono da un parametro.

## Esempi svolti
**Dalla lavagna (registrazione 2025): due parametri liberi.** Risolvere x + 2y − z + w = 3, y + 2z + 5w = 2, x + 3y + z + 6w = 5.

Con R_{3} → R_{3} − R_{1} e poi R_{3} → R_{3} − R_{2}:

( 1 2 −1 1 | 3 ; 0 1 2 5 | 2 ; 1 3 1 6 | 5 ) → ( 1 2 −1 1 | 3 ; 0 1 2 5 | 2 ; 0 1 2 5 | 2 ) → ( 1 2 −1 1 | 3 ; 0 1 2 5 | 2 ; 0 0 0 0 | 0 ).

L'ultima riga è 0 = 0 e si può ignorare. Si riscrive il sistema senza passare dalla forma ridotta: y = 2 − 2z − 5w e x = 3 − 2y + z − w = −1 + 5z + 9w. Le colonne di z e w non hanno pivot, quindi con z = t_{1} e w = t_{2}:

x = −1 + 5t_{1} + 9t_{2},   y = 2 − 2t_{1} − 5t_{2},   z = t_{1},   w = t_{2}.

Sono infinite soluzioni che dipendono da 2 parametri liberi.

**Dalla lavagna (registrazione 2025): solo le prime due equazioni.** Risolvere solo y + z = 0, x + y + 2z = −3, cioè le prime due equazioni del sistema impossibile visto sopra. Gauss dà ( 1 1 2 | −3 ; 0 1 1 | 0 ) e R_{1} → R_{1} − R_{2} dà ( 1 0 1 | −3 ; 0 1 1 | 0 ), quindi x = −3 − t, y = −t, z = t.

Il docente comincia a copiare le righe ( 1 0 1 | 0 ; 0 1 1 | 0 ) dalla forma ridotta di prima, si accorge che non va bene e rifà il conto. Nei tratti leggibili della registrazione non ne dice il motivo, ma si vede dai conti del cap. 39: lì il −3 era stato azzerato usando la terza riga, che qui non c'è. Togliendo un'equazione, la forma ridotta va ricalcolata e non si ricopia.

**Esercizio 11.11.** Risolvere il sistema x + y + 2z = 9, 2x + 4y − 3z = 1, 3x + 6y − 5z = 0.

Con R_{2} → R_{2} − 2R_{1} e R_{3} → R_{3} − 3R_{1}:

( 1 1 2 | 9 ; 0 2 −7 | −17 ; 0 3 −11 | −27 ).

Con R_{3} → R_{3} − (3/2)R_{2} la terza riga diventa ( 0 0 −½ | −3/2 ):

( 1 1 2 | 9 ; 0 2 −7 | −17 ; 0 0 −½ | −3/2 ).

La matrice è a scalini e ogni colonna delle variabili ha un pivot, quindi non ci sono parametri liberi. Dall'ultima riga z = 3; dalla seconda 2y − 21 = −17, cioè y = 2; dalla prima x + 2 + 6 = 9, cioè x = 1. Controllo nella terza equazione: 3 + 12 − 15 = 0.

Nel prossimo capitolo si studiano i sistemi in modo più teorico, per capire la struttura dell'insieme S.
