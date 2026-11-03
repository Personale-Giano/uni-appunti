"""Copia skill, comandi e subagenti di `agente/.claude` in `~/.claude` (livello utente), cosi' /riassunto,
/esame, /ripasso, /moodle, /trascrivi e il revisore funzionano da QUALSIASI cartella, non solo da `UNI\\agente`.

I percorsi relativi (`_sistema/...`, `CLAUDE.md`, `STILE.md`, `STATO.md`) nei file copiati vengono resi
assoluti. Rilanciare questo script dopo ogni modifica a `agente/.claude` (e' idempotente).

Uso: python installa_globale.py
"""
import re
import shutil
import sys
from pathlib import Path

AGENTE = Path(__file__).resolve().parent.parent.parent
SRC = AGENTE / ".claude"
DST = Path.home() / ".claude"
ABS = AGENTE.as_posix()          # es. C:/Users/admin/Desktop/UNI/agente


def absolutize(text: str) -> str:
    text = re.sub(r"(?<![\w/\\.])_sistema[/\\]", f"{ABS}/_sistema/", text)   # anche _sistema\scripts\...
    text = re.sub(r"(?<![\w/\\.`])(?<![/\\])\b(CLAUDE|STILE|STATO|COPERTURA)\.md\b", rf"{ABS}/\1.md", text)
    for nome in ("CLAUDE", "STILE", "STATO", "COPERTURA"):
        text = text.replace(f"`{nome}.md`", f"`{ABS}/{nome}.md`")
    text = text.replace("python _sistema", f"python {ABS}/_sistema")
    # il repo del sito citato per nome: percorso completo
    text = re.sub(r"(?<![\w/\\])quaderno-privato/contenuti", "C:/Users/admin/Documents/GitHub/quaderno-privato/contenuti", text)
    return text


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    n = 0
    for sub in ("skills", "agents", "commands"):
        base = SRC / sub
        if not base.exists():
            continue
        for f in base.rglob("*"):
            if f.is_dir() or f.suffix != ".md":
                continue
            rel = f.relative_to(SRC)
            out = DST / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            body = absolutize(f.read_text(encoding="utf-8"))
            if out.exists() and out.read_text(encoding="utf-8") == body:
                continue
            out.write_text(body, encoding="utf-8")
            n += 1
            print("installato:", rel.as_posix())
    print(f"{n} file aggiornati in {DST}" if n else "Gia' aggiornato.")


if __name__ == "__main__":
    main()
