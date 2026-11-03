---
name: ripasso
description: Materiali di ripasso per una materia o lezione (formulario di una pagina, esercizi svolti, flashcard Anki (.apkg), mappa dei concetti). Si usa con /ripasso <materia> [lezione] o quando Emanuele chiede "formulario", "flashcard", "Anki", "ripasso", "schema riassuntivo".
---

# /ripasso <materia> [lezione]

Leggi `CLAUDE.md` e `STILE.md`. Fonte dei contenuti: i riassunti del sito (`C:/Users/admin/Documents/GitHub/quaderno-privato/contenuti/<materia>.json`, campo `h` dei blocchi), `_sistema/fonti_testo/` e, per Matematica discreta, `_sistema/esami/`. Non inventare: ogni scheda deve essere supportata da una fonte.

## Cosa produrre (chiedi quali, se non è chiaro; default: flashcard + formulario)
1. **Flashcard Anki**: aggiungi schede a `_sistema/flashcard/<materia>.md` nel formato
   `## titolo` / `D: domanda` / `R: risposta` (una scheda = un concetto, risposta breve con elenchi `- ` se serve).
   Poi `python _sistema/scripts/anki_build.py "<materia>"` → `_sistema/anki/<materia>.apkg`; dì a Emanuele di importarlo con doppio clic in Anki (se non ha Anki: ankiweb.net o AnkiDroid, gratuiti). Non duplicare schede già presenti (gli ID sono stabili: reimportare aggiorna).
2. **Formulario di una pagina**: definizioni, formule, teoremi e "trabocchetti" della lezione/materia in `_sistema/esercizi/formulario_<materia>.md` (e, se richiesto, aggiunto come capitolo del sito con `aggiungi_capitolo_sito.py`, dopo `lint_bozza.py`).
3. **Esercizi svolti**: per Matematica discreta usa `genera_esercizi.py` e la banca d'esame (`/esame`); per le altre materie scrivi 5-10 esercizi tipo con soluzione passo-passo e **ricalcola ogni risultato** (SymPy/Python quando possibile) prima di mostrarli. Salva in `_sistema/esercizi/<materia>_L<n>.md`.
4. **Mappa concettuale**: diagramma Mermaid dei collegamenti tra i concetti (usa lo strumento di visualizzazione se disponibile).

## Regole
- Fai passare i materiali nuovi dal revisore (`revisore-riassunti`) se contengono matematica o dimostrazioni.
- Le schede scritte qui entrano anche nel Quaderno online: dopo la creazione lancia `python _sistema/scripts/pubblica_quaderno.py --push`. Le Definizioni/Proposizioni dei capitoli nuovi diventano schede da sole (`schede_dai_riassunti` in `costruisci_pagina_studio.py`): non duplicarle a mano.
- Commit e push di `uni-appunti` alla fine.
