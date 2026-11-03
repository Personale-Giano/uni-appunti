"""Collaudo di tutto il sistema in un colpo solo. Non modifica nulla (solo lettura / file temporanei).

Uso: python selftest.py
Stampa una riga per controllo: OK / ATTENZIONE / ERRORE e, alla fine, un riepilogo. Exit code 1 se c'e' almeno un ERRORE.
"""
import hashlib
import importlib
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
import sys as _s, pathlib as _pl
_s.path.insert(0, str(_pl.Path(__file__).resolve().parent))
from percorsi_word import trova as _trova  # noqa: E402
BASE = HERE.parent
AGENTE = BASE.parent
UNI = AGENTE.parent
PY = sys.executable
WORDS = {
    "Algebra lineare": "Riassunto Algebra lineare.docx",
    "Matematica discreta": "Riassunto Matematica discreta.docx",
    "Fondamenti Info": "Riassunto Fondamenti Informatica.docx",
    "Programmazione": "Riassunto Programmazione.docx",
    "Programmazione/Laboratorio": "Riassunto Laboratorio.docx",
}
results = []


def rec(level, name, detail=""):
    results.append((level, name, detail))
    print(f"[{level:^11}] {name}" + (f": {detail}" if detail else ""))


def run(script, *args, timeout=240):
    r = subprocess.run([PY, str(HERE / script), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    return r.returncode, (r.stdout + r.stderr).strip()


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    # 1. librerie
    for mod in ("faster_whisper", "docx", "pymupdf", "genanki", "sympy", "pypdf", "av"):
        try:
            m = importlib.import_module(mod)
            rec("OK", f"libreria {mod}", getattr(m, "__version__", ""))
        except Exception as e:  # noqa: BLE001
            rec("ERRORE", f"libreria {mod}", str(e)[:80])
    try:
        import av
        major = int(av.__version__.split(".")[0])
        rec("OK" if 14 <= major < 17 else "ATTENZIONE", "versione av compatibile con Whisper (14-16)", av.__version__)
    except Exception:  # noqa: BLE001
        pass
    # 2. Word
    for mat, fn in WORDS.items():
        p = _trova(UNI, '', fn)
        if not p.exists():
            rec("ERRORE", f"Word {mat}", "file mancante"); continue
        try:
            from docx import Document
            n = len(Document(str(p)).paragraphs)
            lock = p.with_name("~$" + p.name[2:])
            rec("OK" if not lock.exists() else "ATTENZIONE", f"Word {mat}", f"{n} paragrafi" + (" (file di blocco ~$ presente: aperto o residuo)" if lock.exists() else ""))
        except Exception as e:  # noqa: BLE001
            rec("ERRORE", f"Word {mat}", str(e)[:80])
    # 3. script con autotest
    code, out = run("genera_esercizi.py", "test")
    rec("OK" if code == 0 and "AUTOTEST OK" in out else "ERRORE", "generatore esercizi: riproduce gli esami veri", out.splitlines()[-1] if out else "")
    code, out = run("verifica_word.py")
    rec("OK" if code == 0 else "ATTENZIONE", "verifica_word su tutti i Word", "nessun errore" if code == 0 else "errori da correggere: lancia verifica_word.py")
    with tempfile.TemporaryDirectory() as _:
        code, out = run("anki_build.py")
        tot = sum(int(l.split(":")[1].split()[0]) for l in out.splitlines() if "schede ->" in l)
        rec("OK" if code == 0 and tot > 0 else "ERRORE", "costruzione mazzi Anki", f"{tot} schede")
    # 4. quiz banca
    ex = BASE / "esami"
    nq = sum(f.read_text(encoding="utf-8").count("\n## [") for f in ex.glob("quiz_*.md"))
    npb = sum(f.read_text(encoding="utf-8").count("\n## [") for f in ex.glob("prob_*.md"))
    rec("OK" if nq >= 140 and npb >= 28 else "ATTENZIONE", "banca esami", f"{nq} quiz, {npb} problemi")
    # 5. backup OneDrive e prova di ripristino
    dest = Path.home() / "OneDrive" / "UNI-backup" / "corrente"
    if not dest.exists():
        rec("ERRORE", "backup OneDrive", "cartella UNI-backup assente: lancia backup_onedrive.py")
    else:
        for mat, fn in WORDS.items():
            src, bk = _trova(UNI, '', fn), dest / mat / fn
            if not bk.exists():
                rec("ATTENZIONE", f"ripristino {mat}", "copia assente su OneDrive")
            elif sha(src) == sha(bk):
                rec("OK", f"ripristino {mat}", "la copia su OneDrive e' identica e leggibile")
            else:
                rec("ATTENZIONE", f"ripristino {mat}", "la copia OneDrive e' diversa (backup non aggiornato): lancia backup_onedrive.py")
    # 6. Whisper
    hub = Path.home() / ".cache" / "huggingface" / "hub"
    models = sorted(d.name.replace("models--Systran--faster-whisper-", "") for d in hub.glob("models--Systran--faster-whisper-*")) if hub.exists() else []
    rec("OK" if models else "ATTENZIONE", "modelli Whisper scaricati", ", ".join(models) or "nessuno")
    tr = BASE / "trascrizioni"
    done = sorted(f.stem for f in tr.glob("*.txt"))
    part = sorted(f.stem for f in tr.glob("*.part"))
    audio = sorted(f.stem for f in (BASE / "audio").glob("*") if f.is_file())
    rec("OK" if len(done) == len(audio) else "ATTENZIONE", "trascrizioni", f"{len(done)}/{len(audio)} complete" + (f", in corso: {', '.join(part)}" if part else ""))
    # 7. git
    g = subprocess.run(["git", "-C", str(UNI), "status", "--short"], capture_output=True, text=True)
    rec("OK" if not g.stdout.strip() else "ATTENZIONE", "git: modifiche non salvate", f"{len(g.stdout.splitlines())} file" if g.stdout.strip() else "tutto committato")
    g = subprocess.run(["git", "-C", str(UNI), "log", "origin/master..HEAD", "--oneline"], capture_output=True, text=True)
    rec("OK" if not g.stdout.strip() else "ATTENZIONE", "git: commit non inviati a GitHub", f"{len(g.stdout.splitlines())}" if g.stdout.strip() else "tutto inviato")
    # 8. convertitore delle bozze del sito: i casi che il 3 nov 2026 erano finiti sbagliati sul sito
    try:
        sys.path.insert(0, str(HERE))
        from aggiungi_capitolo_sito import parti_da_testo
        from migra_word import html_parti
        casi = [
            ("la tilde ~; e il punto", "la tilde ~; e il punto"),
            ("Σ_{σ ∈ S_{n}} sgn(σ)", "Σ<sub>σ ∈ Sn</sub> sgn(σ)"),
            ("5 \\* 3 e x^{2}", "5 * 3 e x<sup>2</sup>"),
            ("`a ~b~ **c**` fine", "<code>a ~b~ **c**</code> fine"),
            ('`printf("%d\\n", x)`', '<code>printf(&quot;%d\\n&quot;, x)</code>'),
            ("un ~corsivo~ e **grassetto**", "un <em>corsivo</em> e <strong>grassetto</strong>"),
        ]
        sbagliati = [(s, html_parti(parti_da_testo(s)), atteso) for s, atteso in casi if html_parti(parti_da_testo(s)) != atteso]
        rec("OK" if not sbagliati else "ERRORE", "convertitore bozze → sito",
            f"{len(casi)} casi di prova superati" if not sbagliati else "; ".join(f"{s!r} → {o!r} (atteso {a!r})" for s, o, a in sbagliati))
        from lint_bozza import controlla_contenuti
        prob = [r for r in controlla_contenuti() if "[evidenziato" not in r]
        rec("OK" if not prob else "ATTENZIONE", "controllo dei contenuti del sito",
            "nessun problema fuori dalle evidenziazioni" if not prob else f"{len(prob)} problemi: python lint_bozza.py --contenuti")
    except Exception as e:  # noqa: BLE001
        rec("ERRORE", "convertitore bozze → sito", str(e))
    # 9. Moodle
    rep = BASE / "moodle_report.md"
    rec("OK" if rep.exists() else "ATTENZIONE", "controllo Moodle eseguito almeno una volta", "report presente" if rep.exists() else "mai eseguito: premi Run now nell'attivita' pianificata")

    n_err = sum(1 for r in results if r[0] == "ERRORE")
    n_att = sum(1 for r in results if r[0] == "ATTENZIONE")
    print(f"\nRiepilogo: {len(results) - n_err - n_att} OK, {n_att} attenzione, {n_err} errori")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
