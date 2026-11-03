"""Trascrive gli audio delle lezioni con faster-whisper (CPU, italiano).

Uso:
    python trascrivi.py                 # tutti gli audio in _sistema/audio non ancora trascritti
    python trascrivi.py algebra_L1.m4a  # un solo file
    python trascrivi.py --model medium  # modello piu' accurato (piu' lento)

Output: _sistema/trascrizioni/<nome>.txt con un blocco ogni ~30 secondi: [mm:ss] testo
I file gia' trascritti vengono saltati, quindi lo script si puo' rilanciare e riprende.
"""
import argparse
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

BASE = Path(__file__).resolve().parent.parent
AUDIO = BASE / "audio"
OUT = BASE / "trascrizioni"
EXT = {".m4a", ".mp3", ".wav", ".mp4", ".ogg", ".flac"}

# Termini del corso: aiutano Whisper a scrivere correttamente il lessico tecnico.
# Il prompt iniziale vale solo per la prima finestra di 30 s (con condition_on_previous_text=False faster-whisper
# lo azzera) ed è limitato a ~224 token: per questo i termini della materia vanno anche in `hotwords`,
# che faster-whisper (>= 1.0) ripete in ogni finestra.
PROMPT = "Lezione universitaria di {materia} in italiano, corso di laurea in Informatica."
# prefisso del nome del file audio -> (nome della materia, sezione di glossario.txt)
MATERIE = {
    "algebra": ("algebra lineare e geometria", "# Algebra e Geometria"),
    "mate": ("matematica discreta", "# Matematica discreta"),
    "fondamenti": ("fondamenti dell'informatica", "# Fondamenti dell'informatica"),
    "prog": ("programmazione in C", "# Programmazione"),
    "lab": ("programmazione in C, laboratorio", "# Programmazione"),
}
MAX_HOTWORDS = 60


def glossario() -> dict:
    """Sezioni di `glossario.txt` -> elenco dei termini."""
    g = BASE / "glossario.txt"
    sez, cur = {}, None
    if g.exists():
        for riga in g.read_text(encoding="utf-8").splitlines():
            if riga.startswith("# "):
                cur = riga.strip(); sez.setdefault(cur, []); continue
            if cur and riga.strip():
                sez[cur] += [t.strip() for t in riga.split(",") if t.strip()]
    return sez


def suggerimenti(src: Path) -> tuple:
    """(initial_prompt, hotwords) per la materia del file, riconosciuta dal prefisso del nome."""
    chiave = next((k for k in MATERIE if src.stem.lower().startswith(k)), None)
    if not chiave:
        return PROMPT.format(materia="informatica"), None
    nome, sezione = MATERIE[chiave]
    termini = glossario().get(sezione, [])
    # i termini aggiunti per ultimi (lezioni recenti) contano di più: si tengono quelli in coda
    return PROMPT.format(materia=nome), ", ".join(termini[-MAX_HOTWORDS:]) or None


def fmt(sec: float) -> str:
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60:02d}:{sec % 60:02d}"


def transcribe(model: WhisperModel, src: Path, fast: bool = False) -> None:
    dst = OUT / (src.stem + ".txt")
    tmp = dst.with_suffix(".part")
    t0 = time.time()
    prompt, hotwords = suggerimenti(src)
    segments, info = model.transcribe(
        str(src),
        language="it",
        vad_filter=True,
        beam_size=1 if fast else 5,
        # fast: niente "temperature fallback" (ripetizioni della decodifica sui tratti rumorosi, che possono bloccare per ore)
        temperature=0.0 if fast else [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        initial_prompt=prompt,
        hotwords=hotwords,
        condition_on_previous_text=False,
    )
    print(f"{src.name}: durata {fmt(info.duration)}", flush=True)
    block_start, block = 0.0, []
    with tmp.open("w", encoding="utf-8") as f:
        for seg in segments:
            if not block:
                block_start = seg.start
            block.append(seg.text.strip())
            if seg.end - block_start >= 30:
                f.write(f"[{fmt(block_start)}] {' '.join(block)}\n")
                f.flush()
                block = []
                done = seg.end / info.duration * 100
                print(f"  {done:5.1f}%  ({int(time.time() - t0)}s)", end="\r", flush=True)
        if block:
            f.write(f"[{fmt(block_start)}] {' '.join(block)}\n")
    tmp.replace(dst)
    print(f"\n  fatto in {int(time.time() - t0)}s -> {dst.name}", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--model", default="small", help="tiny|base|small|medium|large-v3 (default small)")
    ap.add_argument("--fast", action="store_true", help="decodifica semplice (beam 1, senza fallback): 3-5 volte piu' veloce, quasi uguale")
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    if args.files:
        todo = [AUDIO / f if not Path(f).is_absolute() else Path(f) for f in args.files]
    else:
        todo = sorted(p for p in AUDIO.iterdir() if p.suffix.lower() in EXT)
    todo = [p for p in todo if not (OUT / (p.stem + ".txt")).exists()]
    if not todo:
        print("Niente da trascrivere.")
        return

    print(f"Carico il modello '{args.model}' (la prima volta lo scarica)...", flush=True)
    model = WhisperModel(args.model, device="cpu", compute_type="int8", cpu_threads=0)
    for p in todo:
        if not p.exists():
            print(f"manca: {p}", file=sys.stderr)
            continue
        transcribe(model, p, fast=args.fast)
    # frasi "da esame / attenzione / errore" con timestamp, per i capitoli (prima girava solo a mano)
    import subprocess
    subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "frasi_docente.py")], check=False)


if __name__ == "__main__":
    main()
