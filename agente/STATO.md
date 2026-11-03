# Stato dei riassunti (aggiornato il 3 nov 2026)

I riassunti vivono nel sito (`quaderno-privato/contenuti/<materia>.json`, https://quaderno-privato.vercel.app). Questa pagina dice solo **dove siamo** e **cosa manca**; la storia completa fino al 3 nov 2026 è in `_sistema/archivio/STATO_storico_fino_3nov2026.md` (fonti usate per ogni capitolo, decisioni, correzioni).

## Situazione
| Materia | Capitoli sul sito | Prossimo n. | Ultima lezione riassunta | Studiati (≥3 paragrafi evidenziati o segnati a mano) |
|---|---|---|---|---|
| Algebra lineare (Buzano/Radeschi) | 37 | **38** | L10 Matrici III, 28 ott (cap. 31-37: determinante, Laplace, Gauss, inversa) | 1-13 |
| Matematica discreta (Mori) | 36 | **37** | L12 permutazioni, 29 ott (cap. 32-36: cicli, tipo, periodo) | 1-15 |
| Fondamenti Info (Berardi) | 27 | **28** | L12 quantificatori annidati, 23 ott | tutti (1-27) |
| Programmazione I (Amparore) | 29 | **30** | slide 06A funzioni (cap. 27-29) | tutti (1-29; 13 e 27-29 segnati a mano) |
| Laboratorio di Programmazione | 12 | **13** | Lab04 iterazioni | nessuno |

La colonna «Studiati» la aggiorna il piano serale da `_sistema/evid_export.json` (le evidenziazioni le fa solo Emanuele, dal sito).

## Da riassumere
- **Fondamenti L13-L16** (26, 29, 30 ott, 2 nov): le fa Emanuele da solo in un'altra chat. Fonti: solo registrazioni 2025 (L13 trascritta, L14 parziale, L15 no); il docente ha nascosto le registrazioni 2026. Bozze tolte dal sito: `_sistema/bozze/fondamenti_cap28-30.md`.
- **MDAG 30 ott, 2 nov, 3 nov** (Algebra o Mate discreta: l'orario delle ore MDAG non è affidabile): nessuna fonte ancora (né audio né appunti).
- **Programmazione 3 nov** (e le slide dopo 06A): servono le slide da Moodle (login scaduto dal 31 ott: lo rifà Emanuele nel browser pane).
- Appunti in `_sistema/fonti/Appunti/` senza trascrizione in `fonti_testo`: «Algebra luendi.pdf», «Discreata martedi.pdf», «28 Ottobre.pdf», «29 Ottobre .pdf» (già usati per i cap. di Algebra 31-37 e Mate 32-36, ma la trascrizione non è salvata).

## Eccezioni permanenti (non «correggerle»)
- **Programmazione**: il vecchio cap. 20 (errori comuni/visibilità con if) l'ha tolto Emanuele il 14 ott, «inutile per lui»: non reinserirlo (`bozze/programmazione_cap20_vecchio_non_inserito.md`). Il cap. 20 attuale è il while.
- **Fondamenti**: sez. 1.8 (Python) e 2.3 omesse dal docente; il capitolo «Regole di inferenza per gli enunciati quantificati» è stato tolto su richiesta (`bozze/fondamenti_cap25_tolto_ex23.md`).
- **Matematica discreta**: la prima metà della lezione 6 non è coperta (né audio né appunti). Nel libro l'esempio dei film dà 23, il calcolo giusto è 13.
- **Laboratorio**: le soluzioni degli esercizi sono dedotte e verificate, non sono nelle slide.
- **Refusi lasciati perché dentro paragrafi evidenziati** (cambiarli sposterebbe le evidenziazioni): Algebra cap. 3 «i² = -1  i⁴ =1»; Mate cap. 11 «es: f(a) = a»; asterischi al posto del corsivo in Fondamenti cap. 13, 16-19 e Programmazione cap. 18; «contrapositivo» in Fondamenti cap. 24. `python _sistema/scripts/lint_bozza.py --contenuti` li elenca con «[evidenziato: lasciare]».
- Convenzione permutazioni: composizione da destra a sinistra.

## Ultimi lavori
- 3 nov 2026: rilettura completa dei 141 capitoli e 34 correzioni (registro in `_sistema/scripts/_correzioni_sito_3nov*.py`); nuovo controllo automatico delle bozze (`lint_bozza.py`), convertitore corretto (pedici annidati, tilde, codice), Whisper con glossario per materia, Quaderno con schede dalle definizioni, suggerimenti «Rivedi cap. N» per tutte le materie, progressi sincronizzati tra dispositivi ed esportati sul PC.
