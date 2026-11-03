---
name: moodle
description: Controlla il Moodle di Informatica UniTo (i-learn) per slide nuove, annunci, esami, registrazioni Webex dei corsi di Emanuele (canale B). Si usa con /moodle o quando chiede "ci sono slide nuove?", "annunci", "date degli esami", "scarica le slide".
---

# /moodle

Il sito è https://informatica.i-learn.unito.it. **Il login lo fa sempre Emanuele a mano nel browser pane**: non inserire mai username/password. Se il browser mostra la pagina di login, chiedigli di accedere e di avvisarti.

Corsi (id): Mate discreta P1 = 3829, Algebra P2 = 3831, Fondamenti B = 3747, Programmazione B = 3773. Dettagli nella memoria "moodle-unito".

## Procedura (sola lettura, senza chiedere)
1. Usa gli strumenti `mcp__Claude_Browser__*` (navigate + javascript_tool con `fetch` same-origin) per leggere ogni corso: elenco risorse (`a[href*="mod/resource"]`, `mod/folder`, `mod/page`, `mod/url`) e annunci (forum "Annunci").
2. Confronta con quello che c'è già in `_sistema/fonti/<materia>/` e con `STATO.md`. Riassumi a Emanuele **solo le novità**: file nuovi (nome, dimensione via HEAD), annunci (date esame, cambi aula/orario), registrazioni Webex nuove.
3. **Scaricare file richiede il suo ok esplicito** (nome, fonte, dimensione). Dopo l'ok: avvia il download dal browser (anchor con `download`), poi sposta il file da `C:\Users\admin\Downloads` a `_sistema/fonti/<materia>/` con il nome `L<n>_...` o `slide_...`.
4. Webex: le registrazioni si aprono senza password; il pulsante di download è l'icona accanto al titolo. Sono MP4 grandi: chiedi sempre prima.
5. Aggiorna l'elenco «Da riassumere» di `STATO.md` (lezioni nuove con le loro fonti) e, per audio/video scaricati, proponi `/trascrivi`.
