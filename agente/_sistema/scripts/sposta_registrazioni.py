"""Sposta le registrazioni Webex finite da Downloads ad _sistema/audio con il nome <materia>_L<n>_2025.mp4.
Un file è «finito» se non cresce più da almeno 90 secondi. La mappa dice a quale lezione corrisponde ogni registrazione
(data e ora nel nome del file Webex). Stampa quanti ne mancano; con --attendi continua finché non sono arrivati tutti.

Uso: python sposta_registrazioni.py [--attendi]
"""
import shutil
import sys
import time
from pathlib import Path

DOWNLOADS = Path.home() / "Downloads"
AUDIO = Path(__file__).resolve().parent.parent / "audio"
MAPPA = Path(__file__).resolve().parent.parent / "registrazioni_mappa.txt"


def mappa():
    """Righe del tipo: Marco Radeschi-20251017 1502-1 = algebra_L11_2025"""
    out = {}
    for r in MAPPA.read_text(encoding="utf-8").splitlines():
        if "=" in r:
            a, b = r.split("=", 1)
            out[a.strip()] = b.strip()
    return out


def giro():
    mancanti = []
    for chiave, nome in mappa().items():
        dest = AUDIO / f"{nome}.mp4"
        if dest.exists():
            continue
        src = DOWNLOADS / f"Sala riunioni personale di {chiave}.mp4"
        if not src.exists() or time.time() - src.stat().st_mtime < 90:
            mancanti.append(nome)
            continue
        shutil.move(str(src), str(dest))
        print(f"spostato {nome}.mp4 ({dest.stat().st_size // 1048576} MB)", flush=True)
    return mancanti


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    while True:
        m = giro()
        if not m or "--attendi" not in sys.argv:
            print("mancano:", ", ".join(m) if m else "nessuno", flush=True)
            break
        time.sleep(30)
