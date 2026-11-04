# Lab05A - Array e stringhe

<!-- pagina 1 -->
A.A. 2026/27
Programmazione I
Laboratorio
DIPARTIMENTO DI 
INFORMATICA
CORSO DI LAUREA 
TRIENNALE
Array e stringhe
Lezione nº 5

<!-- pagina 2 -->
Array di dati
Un array di variabili è una sequenza di tante variabili dello 
stesso tipo, indicizzate tramite un numero intero non-negativo.
• Il tipo dell’indice è il size_t;
The C standard says size_t represents an unsigned integral type 
and is recommended for any variable representing an array’s 
size or subscripts. (pag. 247, Deitel)
• Gli indici partono da 0.
In questa prima fase useremo array dichiarati sullo stack, che 
hanno una dimensione prefissata (vedrete più avanti un altro 
modo di dichiarare array).
REMINDER: lo specificatore di conversione usato da 
printf/scanf per il tipo size_t è %zu.
2

<!-- pagina 3 -->
Array
Aprire il programma array.c , leggere con attenzione il 
codice, e completare la parte mancante alla fine del main().
3

<!-- pagina 4 -->
Scrivere codice che usa gli array
Serve sapere qual è la dimensione dell’array.
In questa prima fase avremo:
• Una #define che specifica la dimensione, che viene 
usata ovunque si usa l’array.
• Oppure una variabile che contiene la dimensione 
dell’array. Servirà quindi avere una coppia:
<numero elementi,  puntatore all’inizio dei dati>
Tipicamente si opera sugli elementi dell’array tramite cicli.
4

<!-- pagina 5 -->
Questionari
Ad un campione di 20 soggetti è stato somministrato un questionario, 
con una domanda che richiede una risposta da 1 a 5 stelle.
Risposta:  ★★★☆☆
Le risposte ottenute dai 20 questionari hanno questi valori:
#define NUM_RISP 20
int risposte[NUM_RISP] = {
1, 2, 5, 4, 3,  5, 2, 1, 3, 1, 
4, 3, 3, 3, 2,  3, 3, 2, 2, 5 
};
5
Un possibile output è:
Stelle  Frequenza
1          3   ###
2          5   #####
3          7   #######
4          2   ##
5          3   ###
Completare il programma 
questionari.c in modo che calcoli le 
frequenze delle 5 risposte possibili, 
e ne stampi un sommario. 
Usare un array frequenze[] per 
accumulare le frequenze delle 5 
possibili risposte, prima di 
stamparle.

<!-- pagina 6 -->
Somma selettiva
Sulla pagina Moodle trovate un esercizio con nome
Leggere la specifica e scrivere il codice.
DOMANDA: 
• possiamo fare a meno di memorizzare la sequenza letta 
in un array?
6
Lab05-Es1 Somma selettiva

<!-- pagina 7 -->
Array di caratteri: le stringhe
Nel linguaggio C il testo è un tipo di dato memorizzato 
come un array di elementi di tipo char.
• Lettere, cifre, simboli sono rappresentati come unità 
elementari, dette caratteri. 
• Il tipo char è il tipo che rappresenta un carattere. 
• Un array di caratteri forma una stringa di testo.
• I caratteri corrispondono a codici numerici convenzionali, 
descritti da degli standard. Lo standard fondamentale è 
l’ASCII1.
• Abbiamo già usato il testo sotto forma di letterali di 
testo non modificabili (text literals), scrivendo i caratteri 
tra i doppi apici (“”).
7
1 American Standard Code for Information Interchange. Si legge ‘àski’.

<!-- pagina 8 -->
I 128 caratteri dell’ASCII
8
0 NUL
16 DLE
32
48
0
64
@
80
P
96
`
112
p
1 SOH
17 DC1
33
!
49
1
65
A
81
Q
97
a
113
q
2 STX
18 DC2
34
"
50
2
66
B
82
R
98
b
114
r
3 ETX
19 DC3
35
#
51
3
67
C
83
S
99
c
115
s
4 EOT
20 DC4
36
$
52
4
68
D
84
T
100
d
116
t
5 ENQ
21 NAK
37
%
53
5
69
E
85
U
101
e
117
u
6 ACK
22 SYN
38
&
54
6
70
F
86
V
102
f
118
v
7 BEL
23 ETB
39
55
7
71
G
87
W
103
g
119
w
8
BS
24 CAN
40
(
56
8
72
H
88
X
104
h
120
x
9
HT
25 EM
41
)
57
9
73
I
89
Y
105
i
121
y
10
LF
26 SUB
42
*
58
:
74
J
90
Z
106
j
122
z
11
VT
27 ESC
43
+
59
;
75
K
91
[
107
k
123
{
12
FF
28
FS
44
,
60
<
76
L
92
\
108
l
124
|
13 CR
29 GS
45
-
61
=
77
M
93
]
109
m
125
}
14 SO
30
RS
46
.
62
>
78
N
94
^
110
n
126
~
15
SI
31
US
47
/
63
?
79
O
95
_
111
o
127 DEL
Terminatore: 
NUL
→‘\0’
Line feed:
LF
→‘\n’
Horizontal tab: 
HT →‘\t’
Carriage return:
CR →‘\r’

<!-- pagina 9 -->
Testo in programmazione 1
Il linguaggio C supporta 3 codifiche per il testo:
• single-byte: char, va bene per ASCII e Latin-1
• wide: wchar_t
• multi-byte: sempre char ma con interpretazione più 
elaborata per identificare i caratteri
Nel corso di Programmazione 1 useremo solo il testo 
single-byte, per semplicità, e non considereremo le altre 
codifiche.
13

<!-- pagina 10 -->
Terminatore della stringa
Una stringa ha una differenza fondamentale rispetto agli 
array generici: per convenzione è terminata dal carattere 
‘\0’, detto terminatore o NUL.
Ad esempio la stringa di testo “ciao” è un array di 5 
elementi di tipo char con questi valori.
14
‘c’
‘i’
‘a’
‘o’
‘\0’
Una stringa di testo sarà quindi dichiarata come array:
char txt[] = { ‘c’, ‘i’, ‘a’, ‘o’, ‘\0’ };
char txt[] = “ciao”;
oppure come puntatore
const char* txt = “ciao”; // il compilatore ha aggiunto il NUL

<!-- pagina 11 -->
Stringhe
Aprire il programma stringhe.c , leggere con attenzione il 
codice, e provare ad eseguirlo.
15

<!-- pagina 12 -->
Alfabeto
Scrivere un programma alfabeto.c che crea un array di 27 
caratteri.
• Il programma inizializza con un ciclo for i primi 26 
caratteri con le lettere progressive dell’alfabeto dalla 
‘A’ fino alla ‘Z’.
• Inserisce il terminatore della stringa.
• Stampa la stringa ottenuta con printf.
16

<!-- pagina 13 -->
Montagne
Sulla pagina Moodle trovate un esercizio con nome
Leggere la specifica e scrivere il codice. 
Leggere con attenzione i suggerimenti.
17
Lab05-Es2 Montagne

<!-- pagina 14 -->
Quantificazione universale
Supponiamo che stiamo scrivendo un programma che opera su di 
un array a[i] di lunghezza len, e vogliamo rispondere a questa 
domanda:
Tutti gli elementi dell’array soddisfano una condizione Cond?
Come possiamo fare?
18
bool tutti = true;
for (size_t i=0; i<len && tutti; i++) {
if (! Cond valutata su a[i] )
tutti = false;
}
Il ciclo termina sotto due condizioni
•
i==len
⇒tutti gli elementi soddisfano Cond
•
tutti==false
⇒non tutti gli elementi soddisfano Cond. 
In questo caso l’elemento a[i] è il primo che non soddisfa.
Variabile sentinella
(sentinel variable)

<!-- pagina 15 -->
Quantificazione esistenziale
Supponiamo che stiamo scrivendo un programma che opera su di 
un array a[i] di lunghezza len, e vogliamo rispondere a questa 
domanda:
Esiste almeno un elemento dell’array
che soddisfa una condizione Cond?
19
bool esiste = false;
for (size_t i=0; i<len && !esiste; i++) {
if (Cond valutata su a[i])
esiste = true;
}
Il ciclo termina sotto due condizioni
•
i==len
⇒non esiste un elemento che soddisfa Cond
•
esiste==true
⇒esiste almeno un elemento che soddisfa Cond. 
In questo caso l’elemento a[i] è il primo che soddisfa.

<!-- pagina 16 -->
Funzioni base per i caratteri
La libreria del linguaggio C dispone di diverse funzioni per classificare la 
natura dei caratteri, e manipolarli.
Sono definite includendo l’header <ctype.h>
20
Nome
Descrizione
bool isalpha(char ch)
Controlla se il carattere è alfabetico (cioè una lettera).
bool isdigit(char ch)
Controlla se il carattere è una cifra (cioè un numero).
bool isalnum(char ch)
Controlla se il carattere è alfanumerico.
bool islower(char ch)
Controlla se il carattere è una lettera minuscola.
bool isupper(char ch)
Controlla se il carattere è una lettera maiuscola.
bool isspace(char ch)
Controlla se il carattere è uno spazio, una tabulazione o 
un ritorno a capo.
bool ispunct(char ch)
Controlla se è un carattere di punteggiatura tra i seguenti:
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
char tolower(char ch)
Se il carattere è alfabetico, ritorna la forma minuscola, 
altrimenti ritorna il carattere in input inalterato.
char toupper(char ch)
Come tolower ma ritorna la forma maiuscola.

<!-- pagina 17 -->
Passwords
21
Sulla pagina Moodle trovate un esercizio con nome
Leggere la specifica e scrivere il codice. 
Leggere con attenzione quali sono le cinque proprietà da 
calcolare per ciascuna password in input.
Lab05-Es3 Passwords

<!-- pagina 18 -->
Indovina Chi?
Indovina Chi? è un famoso gioco da tavolo inventato da 
Theo e Ora Coster nel 1980 in Gran Bretagna dall'azienda 
MB con il nome Guess Who?
Sulla pagina Moodle trovate un esercizio con nome
completate l’esercizio descritto.
22
Lab05-Es4 Indovina chi?
ESERCIZIO EXTRA
