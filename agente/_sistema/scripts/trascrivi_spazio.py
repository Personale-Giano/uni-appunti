"""Trascrive le registrazioni di uno spazio separato (un altro corso) con faster-whisper, come trascrivi.py.

Uso:
    python trascrivi_spazio.py <cartella_audio> <cartella_uscita> --corso "Scienze dell'educazione" [--anteprima 180] [--model small] [--fast] [file ...]

--anteprima N: trascrive solo i primi N secondi di ogni file (in <uscita>/anteprima/), per capire materia e argomento.
I file già trascritti vengono saltati: si può rilanciare e riprende.
"""
import argparse
import sys
import time
from pathlib import Path

from faster_whisper import WhisperModel

EXT = {".m4a", ".mp3", ".wav", ".mp4", ".ogg", ".flac", ".aac", ".opus"}


def fmt(sec):
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60:02d}:{sec % 60:02d}"


SR = 16000
PEZZO = 600   # secondi: l'audio si decodifica e si trascrive a pezzi, altrimenti una lezione di 3 ore non sta in memoria


def pezzi(src, fino=None):
    """Audio mono 16 kHz a pezzi di PEZZO secondi: (inizio_in_secondi, array float32)."""
    import av
    import numpy as np
    c = av.open(str(src))
    rs = av.AudioResampler(format="flt", layout="mono", rate=SR)
    buf, n, t = [], 0, 0.0
    for frame in c.decode(audio=0):
        for fr in rs.resample(frame):
            a = fr.to_ndarray().reshape(-1)
            buf.append(a); n += len(a)
            if n >= PEZZO * SR:
                x = np.concatenate(buf); yield t, x[:PEZZO * SR]
                rest = x[PEZZO * SR:]; buf, n = [rest], len(rest); t += PEZZO
                if fino and t >= fino:
                    c.close(); return
    if n:
        yield t, np.concatenate(buf)
    c.close()


def trascrivi(model, src, dst, prompt, fast, fino=None):
    tmp = dst.with_suffix(".part")
    t0 = time.time()
    start, blocco = 0.0, []
    with tmp.open("w", encoding="utf-8") as f:
        for off, audio in pezzi(src, fino):
            if fino:
                audio = audio[:fino * SR]
            segments, _ = model.transcribe(audio, language="it", vad_filter=True, beam_size=1 if fast else 5,
                                           temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0], initial_prompt=prompt,
                                           condition_on_previous_text=False)
            for seg in segments:
                s, e = seg.start + off, seg.end + off
                if not blocco:
                    start = s
                blocco.append(seg.text.strip())
                if e - start >= 30:
                    f.write(f"[{fmt(start)}] {' '.join(blocco)}\n"); f.flush(); blocco = []
            print(f"{src.name}: {fmt(off + len(audio) / SR)} trascritti ({int(time.time() - t0)}s)", flush=True)
            if fino:
                break
        if blocco:
            f.write(f"[{fmt(start)}] {' '.join(blocco)}\n")
    tmp.replace(dst)
    print(f"  fatto in {int(time.time() - t0)}s -> {dst.name}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("uscita")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--corso", default="")
    ap.add_argument("--anteprima", type=int, default=0)
    ap.add_argument("--model", default="small")
    ap.add_argument("--fast", action="store_true")
    ap.add_argument("--thread", type=int, default=0)
    a = ap.parse_args()
    cart, out = Path(a.audio), Path(a.uscita)
    if a.anteprima:
        out = out / "anteprima"
    out.mkdir(parents=True, exist_ok=True)
    todo = [cart / f for f in a.files] if a.files else sorted(p for p in cart.iterdir() if p.suffix.lower() in EXT)
    todo = [p for p in todo if not (out / (p.stem + ".txt")).exists()]
    if not todo:
        print("Niente da trascrivere."); return
    prompt = f"Lezione universitaria in italiano, corso di laurea in {a.corso}." if a.corso else "Lezione universitaria in italiano."
    model = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=a.thread)
    for p in todo:
        trascrivi(model, p, out / (p.stem + ".txt"), prompt, a.fast or bool(a.anteprima), a.anteprima or None)


if __name__ == "__main__":
    sys.exit(main())
