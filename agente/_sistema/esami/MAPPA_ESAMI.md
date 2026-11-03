# Mappa degli esami di Matematica discreta (a.a. 2023/24, 2024/25, 2025/26)

Fonti: 15 prove da 10 quiz (150 domande, in `quiz_*.md`) e 15 sessioni da 2 problemi (30 problemi svolti, in `prob_*.md`). Tutte le prove sono comuni ai corsi A, B, C. Formato: **quiz** di 10 domande a 5 risposte + **2 problemi** con sottopunti a/b/c e punteggi (regole in `fonti/Matematica discreta/regole_esame.pdf`). Il voto finale è unico con Algebra (12 CFU), ma le due prove sono separate.

## Frequenza degli argomenti
| Argomento | Quiz (su 150) | Problemi (su 30) | Nei riassunti? (3 nov 2026) |
|---|---|---|---|
| Aritmetica modulare (congruenze, Eulero) | 21 | **10** | non ancora |
| Z_N moltiplicativo (inversi, φ di Eulero) | 16 | **9** | non ancora |
| Omomorfismi tra gruppi | 1 | **9** | non ancora |
| Coefficienti binomiali + combinatoria | 5 + 10 | **8 + 7** | sì (cap. 21-31) |
| Permutazioni: cicli, tipo, periodo | **24 + 24** | 6 + 8 | sì (cap. 32-36; manca il periodo come mcm) |
| Parità delle permutazioni | 6 | 6 | non ancora |
| MCD / algoritmo di Euclide | 1 | 7 | non ancora |
| Disposizioni / combinazioni | 7 + 5 | 6 + 6 | sì (cap. 24, 26-28) |
| Sottogruppi, gruppi, generatori | 7 + 9 + 13 | 5 + 3 + 3 | non ancora |
| Nucleo e immagine | 0 | 5 | non ancora |
| Z_N additivo | 13 | 2 | non ancora |
| Funzioni, composizione, iniettiva/suriettiva | 15 + 11 + 7 | 2 + 1 + 1 | sì (cap. 10-20) |
| Appartenenza e inclusione, ⊆ vs ∈ | **17** | 0 | sì (cap. 1-2) |
| Prodotto cartesiano, operazioni sugli insiemi, insiemi | 12 + 9 + 8 | 2 + 2 | sì (cap. 1-4) |
| Base 2 (e altre basi) | 8 | 1 | non in Mate discreta (c'è in Fondamenti, cap. 6) |
| Partizioni | 2 | 0 | sì (cap. 6-7) |
| Relazioni, classi di equivalenza, induzione | **0** | **0** | sì (cap. 5, 7-9) |

## Cosa si capisce
1. **Gli argomenti dei primi capitoli (relazioni di equivalenza, induzione, partizioni) non sono mai usciti negli esami di questi tre anni**: servono come base teorica, ma non sono la priorità per i punti. Appartenenza/inclusione e funzioni invece escono spesso nei quiz (17 e 15 volte).
2. **Quasi tutto l'esame è su permutazioni, aritmetica modulare e Z_N, gruppi e omomorfismi, combinatoria.** Al 3 nov 2026 combinatoria (cap. 21-31) e permutazioni (cap. 32-36) sono nei riassunti ma non ancora studiati: sono la priorità per i punti. Aritmetica modulare, Z_N, gruppi, omomorfismi, parità e MCD arriveranno con le prossime lezioni.
3. I problemi sono molto ripetitivi: la stessa struttura (permutazione data come prodotto di cicli → cicli disgiunti, tipo, periodo, parità; poi quante permutazioni hanno quel tipo; poi sottogruppo ciclico) ritorna in decine di sessioni. Per questo il generatore di esercizi (`scripts/genera_esercizi.py`) li riproduce con soluzioni verificate.
4. Le soluzioni ufficiali in PDF **contengono errori** (segnalati con "ATTENZIONE" nei file `prob_*.md`): non fidarsi ciecamente quando si ripassa.

## Strategia di studio suggerita (da confermare con le lezioni)
1. Appena si arriva a permutazioni, Z_N e gruppi: fare i capitoli del Word con la stessa cura, poi esercitarsi con `/esame` fino a risolvere i problemi tipo senza guardare.
2. Fino ad allora: tenere vivi appartenenza/inclusione e funzioni con le flashcard Anki (mazzo "Matematica discreta", che include i quiz degli esami).
3. Convenzione da ricordare: la composizione di permutazioni si fa **da destra a sinistra** (il ciclo più a destra agisce per primo).
