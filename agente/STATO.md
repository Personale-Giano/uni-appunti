# Stato dei riassunti (aggiornato il 4 nov 2026)

I riassunti vivono nel sito (`quaderno-privato/contenuti/<materia>.json`, https://quaderno-privato.vercel.app). Questa pagina dice solo **dove siamo** e **cosa manca**; la storia completa fino al 3 nov 2026 è in `_sistema/archivio/STATO_storico_fino_3nov2026.md` (fonti usate per ogni capitolo, decisioni, correzioni).

## Situazione
| Materia | Capitoli sul sito | Prossimo n. | Ultima lezione riassunta | Studiati (≥3 paragrafi evidenziati o segnati a mano) |
|---|---|---|---|---|
| Algebra lineare (Buzano/Radeschi) | 45 | **46** | L13 Sistemi lineari III, 4 nov (cap. 38-45: Gauss-Jordan, Rouché-Capelli, applicazioni) | 1-13 |
| Matematica discreta (Mori) | 40 | **41** | L13 permutazioni, 3 nov (cap. 37-40: periodo come mcm, scambi, parità; il teorema della parità è solo enunciato) | 1-15 |
| Fondamenti Info (Berardi) | 35 | **36** | L17 prove per contraddizione, 5 nov (cap. 28-35) | 1-27 |
| Programmazione I (Amparore) | 40 | **41** | slide 06B chiamata di funzione (cap. 30-34) e 07A algoritmi su array (cap. 35-40), lezioni fino al 4 nov | 1-29 (13 e 27-29 segnati a mano); da studiare 30-40 |
| Laboratorio di Programmazione | 14 | **15** | Lab05A array e stringhe (cap. 13-14) | nessuno |

La colonna «Studiati» la aggiorna il piano serale da `_sistema/evid_export.json` (le evidenziazioni le fa solo Emanuele, dal sito).

## Da riassumere
- **Fondamenti L13-L17** (26, 29, 30 ott, 2 e 5 nov): cap. 28-35 scritti il 6 nov da titoli Moodle 2026, libro (§1.6, 2.1, 2.2, note riformulate in `fonti_testo/Fondamenti Info/libro_parte2_*_note.md`, non pubblicate) e registrazioni 2025, senza appunti né registrazioni 2026. Il materiale solo 2025 è segnato nei capitoli. Se arrivano appunti 2026, confrontare. Prossima: L18 (2025: fine §2.2).
- **Algebra L11-L13 (30 ott, 2 e 4 nov)**: cap. 38-45 scritti dalle dispense (Sistemi lineari I-III) e integrati il 4 nov con lavagne e audio delle registrazioni 2025 (`fonti_testo/Algebra lineare/L11-13_lavagne_video2025.md`, 17, 20 e 27 ott 2025); le aggiunte sono segnate «registrazione 2025» nei capitoli. Da confermare, senza audio né appunti 2026, che quest'anno il docente abbia seguito lo stesso ordine. In `fonti/Algebra lineare/` anche `Foglio_1.pdf` ed `esami/` (appelli 2023-26 con soluzioni, 30 PDF: ancora da analizzare per una mappa d'esame).
- **Registrazioni Fondamenti 2025** L13-L36 tutte in `audio/fondamenti_L*_2025.mp4` (corrispondenza con i nomi Webex in `_sistema/registrazioni_mappa.txt`). Prima di riassumere le lezioni successive servono i capitoli del libro. L13-L36 tutte trascritte con il trascrittore corretto il 5 nov (quelle del 3-5 nov erano rovinate da `hotwords`). **L23: dal minuto 70 l'audio è silenzio assoluto**, quindi la seconda parte della lezione non ha trascrizione.
- **Trascrizioni più vecchie con almeno il 5% di frasi ripetute** (mai rifatte; i capitoli relativi esistono già): Algebra L2A, L2B (19%), L4B, L6A (11%), L6B, L8B; Fondamenti L8 (11%), L10, L12; Mate L5_B (16%), L7_B, L10 (12%). Si possono rifare con `trascrivi.py <file> --fast --rifai`.
- **Mate discreta**: L13 (3 nov) fatta dalla sola registrazione di Emanuele (`trascrizioni/mate_L13.txt`, con chiacchiere vicine al microfono: non pubblicarla); manca la dimostrazione del teorema della parità, rimandata. Non c'è lezione MDAG giovedì 5 e venerdì 6 nov. Calendario vero: `fonti/Matematica discreta/ProspettoCorsoB.pdf` (su Moodle aggiornato il 29 ott: ripristinata la lezione del 12 nov). L'orario `orario_lezioni_B.txt` sbaglia le ore MDAG.
- **Programmazione**: i cap. 30-40 e Lab 13-14 sono scritti dalle sole slide. Non usate le registrazioni Webex del 27-28 ott e 3-4 nov (si possono aggiungere con un ok). I 4 quiz del Lab05 su Moodle non sono stati letti: nei capitoli sono citati solo per nome. Su Moodle `03D_decisioni.pdf` è diverso dalla copia locale (169 byte in più, 20 ott): da confrontare.
- Appunti in `_sistema/fonti/Appunti/` senza trascrizione in `fonti_testo`: «Algebra luendi.pdf», «Discreata martedi.pdf», «28 Ottobre.pdf», «29 Ottobre .pdf» (già usati per i cap. di Algebra 31-37 e Mate 32-36, ma la trascrizione non è salvata).

## Eccezioni permanenti (non «correggerle»)
- **Programmazione**: il vecchio cap. 20 (errori comuni/visibilità con if) l'ha tolto Emanuele il 14 ott, «inutile per lui»: non reinserirlo (`bozze/programmazione_cap20_vecchio_non_inserito.md`). Il cap. 20 attuale è il while.
- **Fondamenti**: sez. 1.8 (Python) e 2.3 omesse dal docente; il capitolo «Regole di inferenza per gli enunciati quantificati» è stato tolto su richiesta (`bozze/fondamenti_cap25_tolto_ex23.md`).
- **Matematica discreta**: la prima metà della lezione 6 non è coperta (né audio né appunti). Nel libro l'esempio dei film dà 23, il calcolo giusto è 13.
- **Laboratorio**: le soluzioni degli esercizi sono dedotte e verificate, non sono nelle slide.
- **Slide di Programmazione corrette nei capitoli** (4 nov 2026): 06B chiama `a` e `b` «parametri attuali» (sono formali) e dà offset diversi (scritti solo come positivi e negativi); 07A inizializza VLA con `= {...}`, non valido in C; Lab05A pp. 14-15 dice che dopo il `for` con sentinella `a[i]` è il primo elemento e che `i == len` basta (in realtà è `a[i-1]`, si legge la sentinella); sul sito queste correzioni sono segnalate come «precisazione aggiunta». Il compilatore C non è installato su questo PC: il codice è controllato a mano e con simulazioni in Python.
- **Refusi lasciati perché dentro paragrafi evidenziati** (cambiarli sposterebbe le evidenziazioni): Algebra cap. 3 «i² = -1  i⁴ =1»; Mate cap. 11 «es: f(a) = a»; asterischi al posto del corsivo in Fondamenti cap. 13, 16-19 e Programmazione cap. 18; «contrapositivo» in Fondamenti cap. 24. `python _sistema/scripts/lint_bozza.py --contenuti` li elenca con «[evidenziato: lasciare]».
- Convenzione permutazioni: composizione da destra a sinistra.

## Ultimi lavori
- 6 nov 2026: esponenti sistemati in Mate cap. 36 e Algebra cap. 14. Il cap. 14 sul sito ha paragrafi che la bozza non ha: non usare `--sostituisci` con la bozza vecchia.
- 6 nov 2026: Mate cap. 37-40 e Fondamenti cap. 28-35 scritti, revisionati e pubblicati.
- 6 nov 2026: scaricate da Moodle le dispense di Algebra del 30 ott (prima 8 ott) e il prospetto MDAG del 29 ott (ripristinato giovedì 12 nov; una lezione MD in meno nella settimana 30 nov - 4 dic). Nelle dispense: spiegazione di Prop. 6.5 riscritta per componenti, nuova Def. 10.5, quindi slittano i numeri del cap. 10 (esercizi ora 10.10-10.12, aggiornati nel cap. 37; cap. 36 con l'avvertimento sulle due identità). Le dispense dicono che una sola identità «non basta»: per le matrici quadrate in realtà basta, e il cap. 36 lo spiega.
- 5 nov 2026: tolto `hotwords` da `trascrivi.py` dopo un confronto sugli stessi tratti audio; aggiunta l'opzione `--rifai`; rifatte Algebra L11-13 e Fondamenti L13-L36. Algebra cap. 38-45 ricontrollati sul testo nuovo dal revisore (41 attribuzioni al docente: corrette quelle imprecise) e integrati nei cap. 38, 39, 40, 42, 44 e 45 con sei spiegazioni del docente che mancavano. Le note sull'audio perso in `L11-13_lavagne_video2025.md` si riferiscono alle trascrizioni vecchie. Controllato sulle dispense (p. 67) «fino a due coefficienti errati» del cap. 45: è corretto.
- 4 nov 2026: Algebra cap. 38-45 sostituiti con la versione integrata dalle lavagne 2025 (`aggiungi_capitolo_sito.py --sostituisci`, che rifiuta i capitoli con evidenziazioni).
- 3 nov 2026: rilettura completa dei 141 capitoli e 34 correzioni (registro in `_sistema/scripts/_correzioni_sito_3nov*.py`); nuovo controllo automatico delle bozze (`lint_bozza.py`), convertitore corretto (pedici annidati, tilde, codice), Whisper con glossario per materia, Quaderno con schede dalle definizioni, suggerimenti «Rivedi cap. N» per tutte le materie, progressi sincronizzati tra dispositivi ed esportati sul PC.
