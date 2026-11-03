# UNI: riassunti e Quaderno di ripasso di Informatica (UniTo, canale B, 1° anno 2026/27)

Emanuele studia su un sito privato, il **Quaderno** (https://quaderno-privato.vercel.app): riassunti delle 5 materie con le sue evidenziazioni, quiz, problemi d'esame, schede a ripetizione spaziata. Claude trasforma le fonti delle lezioni (appunti a mano, slide, dispense, libri, audio trascritti) in capitoli di riassunto e tiene aggiornato il sistema. Aprire Claude Code in `C:\Users\admin\Desktop\UNI\agente`. La versione di questo file fino al 3 nov 2026 è in `_sistema/archivio/CLAUDE_fino_3nov2026.md`.

## Dove sta cosa
- **Riassunti**: `C:\Users\admin\Documents\GitHub\quaderno-privato\contenuti\<materia>.json` (algebra, matematica-discreta, fondamenti, programmazione, laboratorio): capitoli e blocchi con id stabili (`cap26.12`), figure in `contenuti/img/`. I vecchi Word sono in `UNI\_archivio_word\`: archivio di sola lettura, non si usano più.
- **Evidenziazioni**: le fa SOLO Emanuele dal sito (account `emanuele`, amministratore); stanno su Upstash e si esportano in `_sistema/evid_export.json` (`node scripts/esporta_evid.js` nel repo del sito; lo fa già `pubblica_quaderno.py`). Un capitolo è «studiato» con almeno 3 paragrafi evidenziati o se segnato a mano dal sito. Mai modificarle; mai cambiare testo dentro o prima di un paragrafo evidenziato (sono intervalli di caratteri: si sposterebbero).
- **Progressi del Quaderno** (quiz, schede, problemi, errori per tema, date d'esame): per utente su Upstash; quelli di Emanuele si esportano in `_sistema/progressi.json` (`node scripts/esporta_stato.js`, lo fa già `pubblica_quaderno.py`). Li leggono `/piano` e `/esame`.
- `STATO.md`: a che punto è ogni materia, cosa manca, eccezioni. Aggiornarlo dopo ogni capitolo. `STILE.md`: stile da imitare (e registro delle correzioni di Emanuele).
- `_sistema/fonti/<materia>/` e `_sistema/fonti/Appunti/`: fonti originali. `_sistema/fonti_testo/<materia>/`: **cache di testo** (leggere SEMPRE prima questa; appunti a mano trascritti `L<n>_appunti_<data>.md`; `DA_TRASCRIVERE.txt`).
- `_sistema/audio/` → `_sistema/trascrizioni/` (Whisper, con glossario per materia in `_sistema/glossario.txt`); `trascrizioni/da_esame/`: frasi «da esame» del docente.
- `_sistema/bozze/`: bozze dei capitoli. `_sistema/backup/`: copie dei JSON prima di ogni modifica.
- `_sistema/esami/`: banche quiz e problemi (Mate discreta: 150 quiz, 30 problemi, `MAPPA_ESAMI.md`; Fondamenti: `fondamenti_quiz.md`, `FONDAMENTI_MAPPA.md`; `banca_algebra.md`, `banca_programmazione.md`). Le soluzioni ufficiali contengono errori noti (righe «ATTENZIONE»).
- `_sistema/flashcard/` → `_sistema/anki/` (mazzi Anki); `_sistema/errori.md` (registro errori delle simulazioni); `_sistema/piano_oggi.md` (piano serale); `_sistema/moodle_report.md` / `moodle_log.md`.
- `_sistema/archivio/`: versioni vecchie di STATO, CLAUDE, COPERTURA.

## Regole ferree
1. Un capitolo alla volta; prima l'elenco dei macro-argomenti e dei capitoli, attendere l'ok, poi i capitoli. La numerazione continua da quella del sito.
2. Fonti in ordine di fiducia: dispense/libro > schede > appunti a mano > trascrizioni audio. Se due fonti si contraddicono, dirlo, non scegliere in silenzio.
3. Non inventare. Se un dato non è nelle fonti, segnalarlo come «da verificare».
4. Ogni capitolo passa da `lint_bozza.py` e dal revisore (subagente `revisore-riassunti`) prima di andare sul sito.
5. Lingua: italiano. Pronomi per Emanuele: lui/neutro, non assumere altro.
6. File in `~/Downloads` non universitari: non toccarli e non leggerli.
7. Python: `C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe`. Le bozze e i file con backslash si scrivono con lo strumento Write/Edit, **mai con heredoc o `python -c` nella shell** (in questa shell `\\` diventa `\` e `\n` diventa un a capo vero).
8. Convenzione permutazioni (Mate discreta): composizione da destra a sinistra.
9. Repo Git in `UNI\` = `Personale-Giano/uni-appunti`, **pubblico**: dopo un lavoro concluso `git add -A && git commit && git push`, ma niente password, token, dati personali o file con copyright non necessari (esclusioni in `.git/info/exclude`: audio, fonti, backup, progressi, evidenziazioni). Il repo del sito `quaderno-privato` è **privato** e si pubblica solo con `pubblica_quaderno.py`.

## Comandi
- `/riassunto <materia> <lezione>`: flusso completo (`.claude/skills/riassunto/SKILL.md`).
- `/trascrivi`: audio nuovi con Whisper locale, in background.
- `/ripasso <materia> [lezione]`: formulario, esercizi svolti, flashcard, mappa.
- `/esame [quiz|problema|completo|fondamenti|algebra|programmazione] [argomento]`: simulazione con correzione e registro errori.
- `/piano [oggi|settimana]`: piano di ripasso. `/moodle`: novità su Moodle (il login lo fa SEMPRE Emanuele).
- Skill e revisore sono installati anche in `~/.claude`: dopo ogni modifica a `agente/.claude` rilanciare `python _sistema/scripts/installa_globale.py`.

## Script principali (`_sistema/scripts/`)
- `aggiungi_capitolo_sito.py <materia> <bozza.md> [--anteprima|--dry-run|--forza]`: bozza → capitolo nel JSON (con backup e controllo automatico). Sintassi della bozza nel docstring e nella skill riassunto.
- `lint_bozza.py <materia> <bozza.md>` / `lint_bozza.py --contenuti`: errori di scrittura (formule troncate, markdown rimasto, `\n` spezzati, «Word», rimandi sbagliati, stile).
- `pubblica_quaderno.py --push`: esporta evidenziazioni e progressi, ricostruisce Quaderno e riassunti, controlla, fa commit/push del repo del sito e `vercel deploy --prod` da questo PC (sul piano Hobby Vercel non collega repo privati di organizzazione). Ripubblica da solo se un deploy precedente era fallito.
- `costruisci_pagina_studio.py [--diff]`: dati del Quaderno (quiz visibili solo se l'argomento è nei riassunti, schede scritte a mano + schede generate da Definizioni/Proposizioni dei capitoli nuovi, «Rivedi cap. N» per tema); `--diff` scrive `evidenziazioni_oggi.md`. Date d'esame: in `ESAMI` nello script o inserite da Emanuele nel Quaderno.
- `trascrivi.py`, `frasi_docente.py`, `estrai_fonti.py`, `figure_math.py` e `figure_*.py`, `genera_esercizi.py` (esercizi di Mate verificati con SymPy), `anki_build.py`, `selftest.py` (collaudo di tutto, da lanciare se qualcosa non torna), `misura_stile.py`.
- Generatore di esercizi del Quaderno: `_sistema/pagina_studio/gen.js` (collaudo `node _sistema/pagina_studio/test_gen.js`, 0 errori). Quaderno locale (alternativa offline): `apri_quaderno.bat` → http://127.0.0.1:8765.
- Repo del sito: utenti con `node scripts/utenti.js add|passwd|admin|del|list` (le password le digita Emanuele nel suo terminale: mai crearle o digitarle per lui); backup progressi `node scripts/backup_stati.js`. Dettagli nel README del repo.

## Automatismi (attività pianificate dell'app, prompt in `C:\Users\admin\.claude\scheduled-tasks\`)
- `moodle-controllo-giornaliero-2` (mattina): legge i 4 corsi su Moodle, scarica in automatico **solo i PDF nuovi ≤ 25 MB** (autorizzazione permanente di Emanuele, 8 ott 2026, limitata a questo), elenca il resto senza scaricare, riassume gli annunci. Se il login è scaduto si ferma: mai inserire password. Webex, video, zip, docx/pptx: mai scaricati senza un nuovo ok.
- `pubblica-quaderno-sera` (~19:00): `pubblica_quaderno.py --push` e poi il piano di domani (fasi 2-4 di `piano-ripasso-giornaliero/SKILL.md`) in `_sistema/piano_oggi.md`, che il Quaderno mostra solo se è di ieri o di oggi.

## Stile e feedback
Quando Emanuele corregge lo stile («troppo bullet», «più discorsivo», ecc.) aggiungere SUBITO una riga alla sezione «Correzioni di Emanuele» di `STILE.md`. Figure: se utili si inseriscono senza chiedere (regola del 13 ott 2026), sempre aperte con Read prima e controllate dal revisore.
