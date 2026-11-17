# Regole per i video-spiegazione (ricerca del 17 nov 2026)

Sintesi operativa di due ricerche: strumenti (Manim, voci, skill esistenti) e formato (ricerca sull'apprendimento multimediale + pratica dei creator). [R] = evidenza di ricerca, [P] = pratica, [D] = valore di default ragionevole.

## Stack (installato)
- **Manim Community 0.22.1** con **Typst** (`MathTypst`, niente LaTeX), render Cairo su CPU. Python 3.12: `C:/Users/admin/AppData/Local/Programs/Python/Python312/python.exe`, sempre con `PYTHONUTF8=1`.
- **edge-tts 7.3.1**: voci `it-IT-DiegoNeural`, `it-IT-GiuseppeMultilingualNeural`, `it-IT-ElsaNeural`, `it-IT-IsabellaNeural`; con `boundary="WordBoundary"` dà i tempi di ogni parola. Serve la rete; servizio non ufficiale: audio in cache per segmento.
- **ffmpeg**: non è nel PATH; usare quello di `imageio_ffmpeg.get_ffmpeg_exe()` (ha i filtri `ass`, `subtitles`, `loudnorm`). **PyAV** e **faster-whisper** già presenti.
- Non installare: LaTeX/MiKTeX, ManimGL, manim-voiceover, torch/XTTS/WhisperX, server MCP per Manim (inutili: c'è la shell). Disco quasi pieno: svuotare `media/` dopo ogni video.
- Alternativa non installata (solo se serve per video «social» senza formule): Remotion (skill ufficiale `npx remotion skills add`, gratis per uso individuale) o HyperFrames.

## Evidenze di base
- Durata [R]: tempo mediano di visione ≤ 6 minuti qualunque sia la lunghezza; 0-3 minuti l'ingaggio più alto (Guo, Kim, Rubin 2014).
- Principi di Mayer [R]: contiguità temporale (parola e immagine insieme) e spaziale (etichetta attaccata all'oggetto), niente testo che ripete la voce (ridondanza), niente decorazioni (coerenza), segmenti brevi con titolo (segmentazione), un solo punto evidenziato (segnalazione), tono colloquiale in seconda persona.
- Concreto prima dell'astratto [P, 3Blue1Brown]. Esempi svolti [R]. Domanda di verifica finale [R].
- Musica durante la spiegazione: no [R].

## Formati
**(a) Concetto in 60-90 s, verticale 9:16** (un solo concetto, 170-220 parole): 0-3 s aggancio (domanda o risultato sorprendente già a schermo) · 3-10 domanda precisa · 10-35 esempio concreto con numeri · 35-50 definizione formale in una riga con gli stessi oggetti · 50-65 errore tipico · 65-75 riepilogo in una frase · 75-85 domanda di verifica, 2 s di pausa, risposta.

**(b) Spiegazione completa 3-8 min, 16:9** (massimo 8 minuti, deciso da Emanuele il 17 nov 2026; 3-7 segmenti da 40-80 s con titolo): aggancio e domanda (10 s) · obiettivo e termini chiave (15 s) · intuizione ed esempio concreto · definizione formale · esempio svolto · errore tipico · riepilogo in max 3 punti · 1-2 domande di verifica con pausa.

**(c) Esercizio svolto**: testo a schermo · cosa si chiede, cosa si sa · piano in 3-5 sotto-obiettivi con etichetta · un passo per segmento (15-30 s: etichetta, azione, motivo) · a metà un punto di previsione («quanto viene?», 2-3 s di pausa) · controllo del risultato · errore tipico · esercizio gemello lasciato allo spettatore.

## Copione parlato
- 140-160 parole/min (16:9), 150-170 (verticale), 100-120 sulle formule.
- Frasi: media 12-15 parole, massimo 22, al più una subordinata.
- Una idea nuova per segmento, al più 2 termini nuovi; ogni termine nuovo compare scritto nell'istante in cui è detto.
- Stessa parola per lo stesso concetto (mai sinonimi), ripetuta 3 volte: introduzione, esempio, riepilogo.
- Seconda persona («prendi», «ti chiedi»). Una domanda ogni 30-45 s, almeno una di previsione prima del risultato.
- **Testo parlato separato dal testo a schermo**: mai simboli al sintetizzatore. «x al quadrato», «a con i», «la somma per i da uno a enne», «enne più uno», «per ogni», «implica». Si legge solo la parte evidenziata. Codice: si dice cosa fa la riga, non la punteggiatura. Lettere isolate scritte come si pronunciano (enne, kappa, i, pi di enne).
- Pause: 0,3-0,5 s tra frasi, 0,8-1,2 s tra segmenti, 2-3 s dopo una domanda di verifica.

## Schermo
- Al più 3-4 elementi attivi; una formula o 10-12 righe di codice (16:9), 5-7 (verticale); al più 12 parole di testo non matematico per schermata.
- Testo minimo: 16:9 corpo ≥ 4,5% dell'altezza (formula/termine chiave 6-8%), mai sotto 3,5%; 9:16 corpo ≥ 2,6% (formule 3,5-5%), mai sotto 2,2%.
- Zone sicure 9:16 (prudenti): contenuto essenziale entro 15% dall'alto, 35% dal basso, 6% a sinistra, 18% a destra.
- Contrasto ≥ 4,5:1. Tema scuro grafite (`#1c1f26`), testo bianco sporco; 1 colore d'accento + 2-3 colori semantici fissi (stessa variabile, stesso colore per tutto il video). Mai significato affidato al solo colore.
- Un solo punto d'attenzione: il resto al 30-40% di opacità.
- Un cambiamento visivo significativo ogni 5-10 s (16:9) o 3-6 s (verticale); mai più di 12 s di schermo fermo mentre la voce parla.
- Si muove solo l'oggetto nominato, entro ±0,3 s dalla parola. Trasformare, non sostituire (la formula diventa la successiva).
- Sottotitoli: verticale → frasi di 3-6 parole su una riga, bruciate, sopra la zona inferiore coperta, mai sopra il contenuto; 16:9 → file `.srt` a parte (max 42 caratteri per riga, 2 righe).
- Vietati: zoom/rotazioni decorative, rimbalzi, lampi, immagini di repertorio, dissolvenze > 0,5 s.
- Audio finale: −14 LUFS, picco ≤ −1 dBTP, nessuna musica.

## Per materia
- **Dimostrazioni**: enunciato sempre visibile in alto, piccolo; prima un caso numerico (n = 3), poi il generale con la stessa disposizione; un passaggio logico per segmento con il «perché» detto a voce; colorare il termine che cambia; spuntare le ipotesi quando si usano; domanda finale «dove abbiamo usato l'ipotesi?».
- **Codice C**: codice a sinistra con la riga corrente evidenziata, tabella di traccia delle variabili a destra, memoria e puntatori come caselle e frecce; un'istruzione per passo; input piccoli (array di 4-5 elementi); punto di previsione prima dell'iterazione chiave; errore tipico (indice sfasato di uno, variabile non inizializzata); font monospazio (Consolas).
- **Psicologia (esperimenti)**: domanda di ricerca · procedura come linea del tempo con icone semplici · previsione dello spettatore · risultato con un solo grafico o numero · interpretazione · limite/critica · termine tecnico; autore e anno a schermo; distinguere a voce «risultato» e «interpretazione».

## Errori tipici dei video generati dall'AI e contromisure
| Errore | Contromisura |
|---|---|
| Testo sovrapposto o tagliato (il difetto n. 1) | fotogramma a fine di ogni animazione + controllo automatico degli ingombri + guardare i fotogrammi |
| Muro di testo | limite rigido di 12 parole per schermata |
| Voce monotona | sintesi per segmento, velocità diversa per segmento, domande, pause |
| Animazioni decorative | ogni animazione corrisponde a una frase del copione, altrimenti si toglie |
| Ritmo uniforme | durate dei segmenti diverse |
| Niente esempi | nessuna definizione senza un caso numerico prima |
| Errori di contenuto | revisione indipendente del copione contro la fonte prima del render |
| Voce e immagini fuori sincrono | prima l'audio, poi le animazioni pilotate dai tempi delle parole |

## Checklist di qualità
**Copione**: 1) un solo obiettivo dicibile in una frase; 2) domanda entro 10 s (3 s nel verticale); 3) esempio concreto prima della definizione; 4) max 1 idea nuova e 2 termini nuovi per segmento; 5) frasi ≤ 22 parole; 6) parole/min nell'intervallo; 7) nessun simbolo non normalizzato nel parlato; 8) termini chiave senza sinonimi, 3 volte; 9) errore tipico presente e spiegato; 10) domanda di verifica finale con pausa ≥ 2 s e risposta.
**Fotogrammi**: 11) nessuna sovrapposizione o testo tagliato; 12) testo sopra la dimensione minima; 13) contenuto dentro la zona sicura; 14) contrasto ≥ 4,5:1; 15) un solo elemento evidenziato; 16) ≤ 12 parole di testo non matematico; 17) nessuno schermo fermo oltre 12 s; 18) ogni elemento che si muove è nominato dalla voce entro ±0,3 s; 19) colori coerenti tra le scene; 20) sottotitoli ≤ 2 righe e mai sopra il contenuto; audio a −14 LUFS.

## Cosa si è imparato dai progetti «argomento → video Manim»
Piano per scene, poi codice per scena; controlli statici prima del render; render di prova a bassa qualità; massimo 3 giri di correzione per scena guardando i fotogrammi; regole di impaginazione fisse (griglia, margini) nella libreria invece che ripetute ogni volta; timeout per scena. Skill esistenti lette e non installate (presuppongono LaTeX, voce inglese o servizi a pagamento): adithya-s-k/manim_skill, Yusuke710/manim-skill, remotion-dev/skills, heygen-com/hyperframes.
