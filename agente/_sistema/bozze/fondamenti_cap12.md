# 12. Logica Proposizionale: Proposizioni e Valori di Verità
## Da dove si riparte
Con questa lezione comincia la seconda parte del libro. La sezione sulla teoria degli insiemi (1.1) viene saltata perché si incontra in dettaglio nel corso di Matematica discreta, e così era stata saltata la sezione su Python nella prima parte: il testo era pensato come un libro unico che comprendeva anche programmazione e matematica discreta, mentre qui sono corsi separati. La terminologia degli insiemi verrà richiamata più avanti, quando servirà. Si parte quindi dalla sezione 1.2, la **logica proposizionale**.

## Che cos'è la logica proposizionale
La logica proposizionale studia il modo più semplice di combinare affermazioni. Si parte da un insieme di **proposizioni atomiche**: affermazioni di cui non si analizza il contenuto, ma a cui si sa assegnare un **valore di verità**, vero o falso. Possono essere affermazioni sul mondo esterno ("c'è un'automobile", "è giorno", "la temperatura è sopra una certa soglia"), nel caso di un'applicazione informatica in cui una macchina rileva queste informazioni. Da questo punto in poi non ci si chiede più come si ottengono i valori di verità, ma come si **combinano** tra loro.

Una proposizione è dunque una frase che è vera oppure falsa, ma non entrambe. Il libro la dimostra con una serie di frasi da classificare:
- "I soli interi positivi che dividono 7 sono 1 e 7": è **vera**, e si verifica provando che 2, 3, 4, 5 e 6 non dividono 7 (è un altro modo di dire che 7 è primo);
- "Alfred Hitchcock ha vinto l'Oscar per la regia nel 1940 con ~Rebecca~": è **falsa**; si controlla su un archivio o chiedendolo a internet, ed è ~Rebecca~ ad aver vinto l'Oscar come miglior film, mentre per la regia vinse un altro regista;
- "Per ogni intero positivo n esiste un numero primo più grande di n": è **vera**, ed è il teorema di Euclide (i numeri primi sono infiniti): un'affermazione complessa che per la logica proposizionale ha comunque un valore di verità;
- "La Terra è l'unico pianeta dell'universo che contiene vita": non sappiamo se è vera o falsa e magari non lo sapremo mai, ma ha **un valore di verità** anche se ignoto. La logica proposizionale copre anche questi casi, in cui si suppone soltanto che il valore esista.

## Che cosa non è una proposizione
Non tutte le frasi sono proposizioni. Il linguaggio contiene anche:
- **domande**, che chiedono un'informazione: non descrivono come stanno le cose;
- **ordini**, come "compra due biglietti per il concerto": lo scopo non è descrivere il mondo ma cambiarlo. In programmazione è così anche `x = 3`, che è un'istruzione imperativa, un ordine al compilatore di assegnare alla variabile x il valore 3;
- **affermazioni con parametri**, come l'equazione x + 4 = 6: il suo valore di verità dipende da x. Con x = 2 è vera, con x = 0 è falsa. Finché ai parametri non è assegnato un valore, non è una proposizione.

## Le variabili proposizionali
Per indicare le proposizioni si usano variabili come p, q e r, un po' come in algebra si usano le lettere per i numeri. Si può anche **definire** una variabile con una proposizione, scrivendo per esempio `p: 1 + 1 = 3`, cioè "p è la proposizione 1 + 1 = 3" (che è falsa).

## Perché si parla di valori booleani
I valori di verità si chiamano anche **valori booleani**, dal nome di George Boole, il primo a trattare la logica proposizionale in modo scientifico: la logica proposizionale esisteva da mille anni, ma fino ad allora era una parte della filosofia. Per un informatico le affermazioni composte con i connettivi sono il primo compito da affidare ai **circuiti** (visti nelle prime settimane del corso, capitoli 1 e 5 di questo riassunto): una formula di logica proposizionale si può realizzare con un circuito, ma anche scrivere e studiare su carta.

La logica proposizionale si usa di fatto, anche senza dirlo, in tutte le dimostrazioni di matematica. Come ha sottolineato il docente, qui l'interesse è la base per il ragionamento automatico: si studieranno affermazioni più semplici di quelle di un corso di matematica, ma con più dettaglio, perché poi bisogna spiegare alle macchine come ragionare.

Il prossimo capitolo presenta i connettivi con cui si combinano le proposizioni.
