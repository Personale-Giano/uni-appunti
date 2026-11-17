# videolib: video-spiegazione dai riassunti

Video che spiegano un argomento dei riassunti (Manim + Typst + edge-tts + ffmpeg), **solo su richiesta**.
Le regole di formato, copione, schermo e audio sono in `REGOLE_VIDEO.md` (vincolanti). Qui c'è l'API.

```
_sistema/video/
  videolib.py      libreria (voce, scena base, attrezzi, controlli, finalizzazione)
  fai_video.py     riga di comando: voce -> render -> controllo -> MP4
  copioni/         un file .py per video (testo parlato + azioni visive)
  cache_audio/     voce in cache per pezzo di testo (ignorata da git)
  qa/<slug>/       fotogrammi e report dell'ultimo render (ignorata da git)
  media/           file intermedi di Manim, cancellati a fine lavoro
agente/video/<materia>/<slug>.mp4 + .srt + _copione.py     (ignorata da git)
```

## Comandi

```bash
export PYTHONUTF8=1
PY=C:/Users/admin/AppData/Local/Programs/Python/Python312/python.exe
cd C:/Users/admin/Desktop/UNI/agente/_sistema/video
$PY fai_video.py copioni/<file>.py --solo-voce      # sintesi + controllo del copione (durate, parole/min)
$PY fai_video.py copioni/<file>.py --prova          # 854x480 a 15 fps, risultato in qa/<slug>_prova/
$PY fai_video.py copioni/<file>.py --solo id1,id2   # solo alcuni segmenti (prova)
$PY fai_video.py copioni/<file>.py                  # finale 1080p in agente/video/<materia>/
$PY fai_video.py copioni/<file>.py --voce it-IT-DiegoNeural --solo-voce   # confronto tra voci
```
`--verticale` forza il 9:16 (di norma lo decide `META["formato"]`). La voce richiede la rete; la sintesi
con le voci «Multilingual» è lenta la prima volta (2-4 minuti per un video di 5), poi è in cache.

Dopo ogni render: leggere `qa/<slug>/report.txt` e **guardare** `qa/<slug>/fotogrammi/foglio_NN.png`
(un fotogramma ogni 5 s, 3 s nel verticale, con sotto il tempo e le parole dette in quel momento) e
`qa/<slug>/NN_<id>.png` (fine di ogni segmento). `problema_<id>_N.png` = fotogramma di un errore automatico.

## Il copione

```python
from videolib import *

class Induzione(ScenaBase):
    META = dict(materia="fondamenti", slug="induzione", titolo="Il principio di induzione",
                formato="16:9",                       # oppure "9:16"
                voce="it-IT-GiuseppeMultilingualNeural", velocita=0)
    SEGMENTI = [
        Seg("aggancio", "La domanda",                 # id, titolo a schermo, testo PARLATO
            "Come fai a dimostrare che una proprietà vale per infiniti numeri? ..."),
        Seg("verifica", "Tocca a te",
            "In quale passaggio abbiamo usato l'ipotesi induttiva? [pausa 2.8] Nel secondo: ...",
            velocita=-5, pausa_dopo=1.5),
    ]

    def seg_aggancio(self, s):                        # un metodo seg_<id> per segmento
        d = self.testo("Vale per infiniti numeri?", 7, peso=BOLD)
        self.poni(d, 0.5, 0.78)                       # frazioni dell'area di contenuto
        self.play(FadeIn(d), run_time=0.4)
        f = formula(r"S_n = (n(n+1))/2", 8, ACCENTO)  # Typst, non LaTeX
        self.poni(f, 0.5, 0.4)
        self.alla("principio di induzione", Write(f)) # parte quando la voce dice quella frase
```

- **Testo parlato** (`Seg.testo`): solo parole, già normalizzate («enne più uno», «effe pi», «ics»),
  niente simboli né lettere isolate. `[pausa 2.5]` = silenzio. `velocita` = percentuale (−15 … +10).
- **Tempi**: `s.quando("frase", n=1)` e `s.fine_di("frase")` danno i secondi dall'inizio del segmento;
  `self.alla("frase", *animazioni, n=1, run_time=0.6)` aspetta la frase e anima;
  `self.fino_a("frase" | secondi, anticipo=0.15)` aspetta soltanto. Se la parola compare più volte
  nel segmento usare `n=2`. A fine metodo la scena aspetta da sola la fine dell'audio.
- I sottotitoli usano il testo parlato così com'è scritto nel copione.

## Scena base (`ScenaBase`)

| Metodo | Cosa fa |
|---|---|
| `self.testo(s, pct, colore, peso)` | testo (Segoe UI); `pct` = corpo in % dell'altezza; conta nel limite di 12 parole |
| `etichetta(s, pct, colore, peso, font)` | etichetta attaccata a un oggetto (non conta nelle 12 parole) |
| `formula(typst, pct, colore)`, `col(espr, colore)` | formula Typst; `col` colora una parte: `formula(f"S_n + {col('(n+1)', ACCENTO)}")` |
| `self.poni(m, fx, fy, larg=, alt=)`, `self.punto(fx, fy)` | posizione in frazioni dell'area (0,0 in basso a sinistra); `larg/alt` = ingombro massimo |
| `self.titolo_segmento(s)` | automatico a inizio segmento (in alto a sinistra) |
| `self.enunciato(m)`, `self.togli_enunciato()` | enunciato fisso in alto a destra (sotto il titolo nel 9:16) |
| `self.evidenzia(*m)`, `self.ripristina()` | tutto il resto al 35% di opacità / di nuovo pieno |
| `self.trasforma(a, b)` | la formula `a` diventa `b` (posizionare `b` prima) |
| `self.spunta(m)`, `self.croce(m)`, `riquadro(m, colore)` | segni da animare con `Create` |
| `self.pulisci(*tieni)`, `self.fissa(*m)` | toglie tutto tranne titolo, enunciato, oggetti fissati |
| `self.codice(src, pct, larg)` → `Codice` | codice C con numeri di riga; `self.play(c.riga(3))` sposta la barra |
| `TabellaTraccia(["i", "s"])` | `self.play(t.passo(0, 3))` aggiunge una riga |
| `Caselle([3, 1, 4], nome="a")` | array con indici; `a.imposta(i, v)`, `f = a.freccia(i, "i")`, `a.sposta(f, j)` |
| `Pila(larg, posti, alt_posto)` | stack verso il basso: `push(nome, valore, colore, alt, mostra)`, `pop(n)`, `imposta`, `attiva(*nomi)`, `puntatore("FP", colore, LEFT, livello)`, `sposta("FP", livello)` |
| `self.figura("fond/x.png", larg, alt)` | figura PNG/SVG da `_sistema/figure` |
| `self.foto(nome)` | salva il fotogramma corrente in `qa/` |

Colori: `SFONDO` grafite, `TESTO`, `TENUE`, `ACCENTO` (giallo: il punto d'attenzione), `VERDE` (vero/fatto),
`ROSSO` (errore), `AZZURRO`, `VIOLA`, `ARANCIO` (ruoli semantici: stesso oggetto, stesso colore in tutto il video).
Dimensioni di default in `F` (`F["corpo"]`, `F["grande"]`, `F["piccolo"]`), diverse per 16:9 e 9:16.

## Controlli automatici

- **Copione** (`controlla_copione`): parole/min per segmento, frasi oltre 22 parole, simboli o lettere isolate
  nel parlato, domanda entro 10 s (3,5 s nel verticale), domanda di verifica finale con `[pausa ≥ 2]` e
  risposta, durata totale (16:9: 2-8 minuti; 9:16: 55-95 s).
- **Schermo** (dopo ogni animazione): oggetti fuori dal quadro o dalla zona sicura, sovrapposizioni tra
  testi/formule/codice, testo sotto la dimensione minima (formule sotto il 4,5%), più di 12 parole di testo,
  schermo fermo oltre 12 s (8 s nel verticale), animazione in ritardo di più di 0,3 s sulla parola.
- **File**: traccia audio presente, durata audio = durata video, volume (−14 LUFS), tratto più lungo di
  schermo fermo misurato sui fotogrammi.

**Non** vede: un testo sopra una forma (freccia, tessera, riquadro), una formula resa male da Typst, lo
sfasamento tra voce e immagine quando l'aggancio è sulla parola sbagliata, la pronuncia. Per questo i
fotogrammi si guardano sempre.

## Problemi noti

- `Rotate(m)` insieme a `m.animate...` sullo stesso oggetto: vince l'ultima. Usare
  `m.animate(path_arc=...).rotate(...).set_color(...)`.
- Una parola usata come aggancio che compare due volte («Dieci», «Tre»): `n=2`.
- `Indicate(f[-5:])` su una formula dipende da quanti glifi produce Typst: controllare a video.
- Nel 9:16 il verticale è ricodificato da ffmpeg (sottotitoli bruciati): più lento.
- Copioni di collaudo: `copioni/demo_attrezzi.py` (codice, tabella, caselle, pila, figura).
