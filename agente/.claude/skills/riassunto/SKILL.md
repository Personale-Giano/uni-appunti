---
name: riassunto
description: Crea il riassunto di una lezione universitaria (Algebra lineare, Matematica discreta, Fondamenti Info, Programmazione, Laboratorio) come nuovi capitoli dei riassunti sul sito di Emanuele (il Quaderno online). Si usa con /riassunto <materia> <lezione> o quando chiede di "fare il riassunto della lezione N", "aggiungere la lezione", "gli appunti di oggi".
---

# /riassunto <materia> <lezione>

Sostituisce il flusso NotebookLM di Emanuele. Lavora nella cartella `UNI\agente`. Leggi sempre prima `CLAUDE.md`, `STILE.md`, `STATO.md`.
I riassunti vivono nel sito (repo privato `quaderno-privato`, `contenuti/<materia>.json`); i Word sono archiviati in `UNI\_archivio_word` e non si usano più.

## 1. Preparazione (senza chiedere nulla)
1. Da `STATO.md` ricava: materia, prossima numerazione, ultima lezione riassunta, eccezioni (capitoli tolti, lezioni che Emanuele fa da solo).
2. Raccogli le fonti della lezione:
   - cache di testo `_sistema/fonti_testo/<materia>/` (leggila SEMPRE prima dei PDF): PDF con testo già estratti, appunti a mano già trascritti `L<n>_appunti_<data>.md`;
   - fonti originali `_sistema/fonti/<materia>/` e `_sistema/fonti/Appunti/` (appunti a mano mandati da Emanuele, spesso con nomi come «28 Ottobre.pdf» o «Algebra lunedì.pdf»: riconosci materia e lezione dal contenuto e dall'orario `_sistema/orario_lezioni_B.txt`, ma attenzione: nelle ore MDAG l'orario non distingue bene Algebra e Mate discreta);
   - trascrizioni audio `_sistema/trascrizioni/` (fiducia più bassa: sbagliano termini e formule) e le frasi «da esame» in `_sistema/trascrizioni/da_esame/`.
   Gli appunti a mano scansionati: leggili con Read (senza `pages`) e salva SUBITO la trascrizione in `_sistema/fonti_testo/<materia>/L<n>_appunti_<data>.md` (prima riga `<!-- fonte: <percorso del PDF> -->`), così non si rileggono. Poi `python _sistema/scripts/estrai_fonti.py`.
   Se mancano fonti in `_sistema/fonti`, cerca in `C:\Users\admin\Downloads` SOLO per nome pertinente (materia, "lezione", data) e copiale, mai altro. Audio nuovi: `/trascrivi`.
3. Rileggi gli ultimi 2 capitoli della materia (dal JSON) per imitare struttura, lunghezza e tono.

## 2. Elenco macro-argomenti (primo e unico checkpoint)
Presenta SOLO:
- i macro-argomenti della lezione, incrociando appunti + audio + dispense/libro (nota se il docente ha detto cose non nel libro, o viceversa);
- la proposta di capitoli con titolo e numero (continuando dall'ultimo capitolo del sito);
- contraddizioni tra fonti o punti da verificare.
Poi ATTENDI l'ok di Emanuele. Non scrivere capitoli prima. (Se Emanuele ha già detto «procedi» o ha chiesto più lezioni insieme, presenta l'elenco e prosegui.)

## 3. Un capitolo alla volta
1. Scrivi la bozza in `_sistema/bozze/<materia>_cap<N>.md` **solo con lo strumento Write** (mai con heredoc, `python -c` o stringhe di shell: in questa shell `\\` diventa `\` e i `\n` del C diventano a capo veri).
   Sintassi: `# N. Titolo` (Programmazione/Laboratorio: `# Capitolo N: Titolo`), `## Sottotitolo`, `- elenco`, `**grassetto**`, `~corsivo~` (tilde attaccata al testo; **mai** `*corsivo*`), `` `codice` `` (dentro non valgono altri marcatori), `^{apice}`, `_{pedice}` (anche annidati: `Σ_{σ ∈ S_{n}}`), `\*` e `\~` letterali, blocchi ``` per il codice, `![didascalia](figure/nome.png|larghezza_cm)`.
   Rispetta `STILE.md`: via di mezzo tra discorsivo ed elenchi, **dopo ogni definizione il paragrafo «(In parole povere: …)»**, un esempio per concetto, niente «questo Word» / «le fonti dicono», rimandi solo a capitoli che esistono.
   **Figure**: dove un disegno chiarisce (funzioni con frecce, Venn, grafici, piano complesso, matrici, stack) generale con `_sistema/scripts/figure_math.py` o uno script `figure_<materia>N.py`, aprile con Read per controllarle e inseriscile nella bozza. Poche ma utili.
2. Controllo automatico: `python _sistema/scripts/lint_bozza.py <materia> _sistema/bozze/<bozza>.md`. Gli ERRORI si correggono sempre; gli AVVISI si valutano.
3. Revisore: lancia il subagente `revisore-riassunti` passandogli la bozza, le fonti usate, `STILE.md` **e il testo convertito** (`python _sistema/scripts/aggiungi_capitolo_sito.py <materia> <bozza> --anteprima`), così vede anche gli errori di conversione. Non dirgli cosa pensi sia giusto. Applica le correzioni confermate; i dubbi li riporti a Emanuele.
4. Mostra a Emanuele il capitolo (solo testo) con in fondo una riga "Revisione: N correzioni applicate, M punti da verificare".
5. Dopo il suo ok (o "procedi"): `python _sistema/scripts/aggiungi_capitolo_sito.py <materia> <bozza>.md` (materia: algebra | matematica-discreta | fondamenti | programmazione | laboratorio). Lo script rifà il controllo e si ferma se ci sono errori (`--forza` solo se sono voluti).
6. Pubblica: `python _sistema/scripts/pubblica_quaderno.py --push` (commit e push del repo del sito e `vercel deploy --prod` da questo PC: 2-4 minuti). Un capitolo nuovo parte senza evidenziazioni: le fa Emanuele dal sito. Le schede si generano da sole dalle Definizioni/Proposizioni/Teoremi del capitolo (blocchi che iniziano con `**Definizione.**`, `**Proposizione.**`, `**Teorema (nome).**`): scrivile così.
7. Aggiorna `STATO.md` (tabella: capitoli, prossimo numero, ultima lezione; elenco «Da riassumere»).

## 4. Chiusura lezione
Quando tutti i capitoli sono dentro: aggiungi 5-10 domande tipo esame verificate alla banca della materia (`_sistema/esami/banca_<materia>.md`, formato delle domande già presenti; i calcoli rifatti con Python/SymPy), poi proponi (senza farli) formulario e flashcard con `/ripasso`. Fai commit e push di `uni-appunti` (repo pubblico: niente dati personali).

## Cose da non fare
- Non inventare dimostrazioni o esempi non supportati: se li aggiungi per chiarezza, devono essere verificabili (controlla i calcoli).
- Non toccare i capitoli esistenti per correggere refusi senza dirlo: le correzioni si propongono a parte. Non cambiare mai testo DENTRO o PRIMA di un paragrafo evidenziato (le evidenziazioni sono intervalli di caratteri: si sposterebbero). `python _sistema/scripts/lint_bozza.py --contenuti` elenca i problemi del sito e segna quelli evidenziati.
- Le evidenziazioni sono di Emanuele (database del sito): mai modificarle.
