# Schemi riassuntivi: formato

Gli schemi sono la sezione «Schemi» del Quaderno online. Servono per un **ripasso lampo**: mentre Emanuele studia un capitolo avanzato e non ricorda un concetto passato, apre lo schema, lo trova con la ricerca e in 20-30 secondi se lo rinfresca. Non sono riassunti: sono schede da colpo d'occhio.

Ogni materia ha un file `_sistema/schemi/<slug>.md` (slug: programmazione, laboratorio, algebra, matematica-discreta, fondamenti). Lo converte `scripts/schemi_html.py`, chiamato da `pubblica_quaderno.py`.

## Sintassi

```
# Nome del gruppo (macro-argomento, es. «Puntatori e memoria»)

## Nome del concetto {11, 12}
= Definizione semplificata: una o due frasi, parole semplici.
![didascalia breve](figure/prog/ch11_puntatore.png)
- concetto principale in una frase
- altro concetto principale
```c
int x = 5;
int *p = &x;   // p contiene l'indirizzo di x
```
! Trabocchetto: l'errore tipico, in una frase.
> Vedi anche: Dereferenziamento, Alias
```

- `# ...` apre un **gruppo**: 4-10 concetti legati fra loro. I gruppi seguono l'ordine del corso.
- `## Concetto {N, M}` apre una **scheda**. Tra graffe vanno i capitoli dei riassunti dove il concetto è spiegato: `{11}`, `{11, 12}`, `{lab 4}`, `{27, lab 15}`. Il primo numero diventa il link «Rileggi nel cap. N».
- `= ...` è la **definizione semplificata**: al massimo una per scheda, sempre la prima riga dopo il titolo, se c'è.
- `- ...` sono i **concetti principali**: da 2 a 5 punti, ognuno una frase breve.
- La riga ```` ```c ```` apre un **mini-esempio di codice** (anche ```` ``` ```` senza linguaggio). Al massimo 3-8 righe, commenti brevi.
- `![didascalia](percorso.png)` inserisce una **figura**: il percorso è relativo a `_sistema/`. Si possono riusare le figure dei riassunti in `figure/prog/` eccetera.
- `! ...` è il **trabocchetto o errore tipico**, che diventa un riquadro arancione. Al massimo uno per scheda.
- `> Vedi anche: A, B` elenca **altre schede** con quel titolo esatto, che diventano link.
- Dentro il testo valgono `**grassetto**`, `` `codice` ``, `~corsivo~`, `^{apice}` e `_{pedice}`, come nelle bozze.
- Una schema per **concetto**, non per capitolo: un capitolo può dare 1-4 schede, e una scheda può raccogliere più capitoli.

## Regole di contenuto

- Tutto deve essere già nei riassunti del Quaderno: non si aggiungono cose nuove. Ogni affermazione e ogni codice devono essere corretti (il codice C deve compilare se completato con il `main`).
- Brevità: una scheda si legge in 20-30 secondi. Niente paragrafi lunghi, niente dimostrazioni.
- Il linguaggio è semplice, ma i termini tecnici del corso restano, scritti in grassetto la prima volta.
- Le figure si mettono solo dove aiutano davvero a capire a colpo d'occhio, ad esempio memoria, stack, frecce dei puntatori o flusso dei cicli.
