---
description: Trascrive gli audio nuovi delle lezioni (Whisper, locale, in background)
---

Trascrivi gli audio delle lezioni.

1. Se in `C:\Users\admin\Downloads` ci sono audio universitari non ancora in `_sistema/audio` (nomi con "lezione", "algebra", "mate-discreta", "fondamenti", "programmazione", "01B_architettura"), copiali in `_sistema/audio` con il nome `<materia>_L<n>[_A|_B].<ext>`. Non toccare altri audio.
2. Lancia in background (`run_in_background`) dalla cartella `UNI\agente` (non da `UNI\`):
   `C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe _sistema\scripts\trascrivi.py $ARGUMENTS`
   (senza argomenti trascrive tutti i nuovi; il modello di default è `small`; `--model medium` è più preciso ma molto più lento su CPU).
3. Dì a Emanuele quanti file e la stima del tempo (circa 1-2 volte la durata dell'audio su CPU), e che può continuare a lavorare: ti arriverà la notifica a fine lavoro.
4. Prima di lanciare, controlla che `_sistema/glossario.txt` contenga i termini tecnici dei corsi (aiutano Whisper a scriverli bene) e aggiungi quelli nuovi.
5. A fine lavoro leggi le prime righe di ogni trascrizione per controllare la qualità e segnala i termini tecnici sbagliati più frequenti (aggiungili a `_sistema/glossario.txt` e, se serve, ritrascrivi). Le trascrizioni sono una fonte di fiducia più bassa delle dispense: possono sbagliare termini e formule dette a voce.
