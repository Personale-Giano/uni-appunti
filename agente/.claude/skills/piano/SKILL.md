---
name: piano
description: Piano di ripasso giornaliero o settimanale per Emanuele, basato su cosa ha già studiato (evidenziazioni), argomenti deboli (registro errori), date degli esami e copertura dei programmi. Si usa con /piano o quando chiede "cosa studio oggi", "piano di ripasso", "organizzami lo studio".
---

# /piano [oggi|settimana]

Leggi `CLAUDE.md`, `STATO.md` (tabella «Situazione»), `_sistema/errori.md`, `_sistema/progressi.json` (progressi del Quaderno online, esportati dal database da `pubblica_quaderno.py` / `node scripts/esporta_stato.js` nel repo del sito: errori per tema `th`, problemi `probs`, domande `qs`, schede `cards`, date d'esame `exams`, giorni di studio `days`), `_sistema/evid_export.json` (evidenziazioni), `_sistema/moodle_report.md` (date d'esame e annunci, se presenti) e `_sistema/esami/MAPPA_ESAMI.md`.

## Regole di priorità
1. Esami imminenti (date nel report Moodle o dette da Emanuele): materia con l'esame più vicino prima.
2. Argomenti deboli: quelli con più errori in `errori.md`.
3. Capitoli **non studiati** (meno di 3 paragrafi evidenziati sul sito): da leggere e evidenziare; indicare quali, con il link `https://quaderno-privato.vercel.app/riassunti/<slug>.html#cap<N>`.
4. Ripasso a intervalli dei capitoli studiati: le schede del Quaderno (anche quelle generate dalle definizioni) hanno già le scadenze.
5. Per Matematica discreta: pesare gli argomenti per frequenza d'esame (MAPPA_ESAMI.md): permutazioni e combinatoria valgono molto più di insiemi e funzioni.
6. Programmazione: «studiato» non basta, l'esame è al PC: almeno un esercizio di laboratorio a settimana.

## Output (breve, in italiano)
**Oggi** (max 90 minuti, 3 blocchi):
- Blocco 1 (30'): lettura/studio di un capitolo non studiato (nome del capitolo e link).
- Blocco 2 (30'): `/esame quiz <argomento debole>` oppure 15 flashcard Anki del mazzo indicato.
- Blocco 3 (30'): un esercizio/problema (`/esame problema`) o scrittura/revisione del prossimo capitolo con `/riassunto`.
**Settimana**: tabella giorno → materia → attività, con almeno 1 giorno di recupero libero.
Chiudi con una riga: "Cosa c'è di nuovo da fare per tenere il sistema aggiornato" (es. lezioni senza riassunto, audio da trascrivere, novità Moodle).

## Regole
- Non inventare date d'esame: se mancano, dillo e chiedile.
- Se Emanuele segna un blocco come fatto o sbagliato, aggiorna `_sistema/errori.md` e `STATO.md`.
