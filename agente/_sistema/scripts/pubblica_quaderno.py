"""Prepara (e, con --push, pubblica) il Quaderno online: ricostruisce la pagina dai Word, quiz, problemi e schede,
converte i riassunti e copia tutto nella cartella protected/ del repo privato quaderno-privato.
Vercel pubblica da solo ogni volta che il repo riceve un nuovo commit.

Uso:  python pubblica_quaderno.py [--repo CARTELLA] [--push] [--no-build]
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
BASE = SCRIPTS.parent
PAG = BASE / "pagina_studio"
REPO_DEFAULT = Path.home() / "Documents" / "GitHub" / "quaderno-privato"

IC_LIBRO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 19V5.5M8.5 7.5h7M8.5 11h5"/></svg>'
IC_ESCI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h3M16 8l4 4-4 4M20 12H9"/></svg>'

# voce "Riassunti" nel menu (schermi grandi), nella barra in basso (telefono) e pulsante Esci
TABLINK = f'<a class="tablink" href="riassunti/">{IC_LIBRO}<span>Riassunti</span></a>'
BNLINK = f'<a class="bnlink" href="riassunti/">{IC_LIBRO}<span>Riassunti</span></a>'
ESCI = f'<button class="icon-btn" id="logout-btn" title="Esci (__QUSER__)" aria-label="Esci">{IC_ESCI}</button>'
CSS_EXTRA = """<style>
.seg .tablink{position:relative;z-index:1;display:inline-flex;align-items:center;gap:8px;text-decoration:none;color:var(--muted);font:600 .98rem var(--font-body);min-height:44px;padding:0 18px;border-radius:10px;white-space:nowrap;transition:color .2s}
.seg .tablink svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.seg .tablink:hover{color:var(--accent)}
.seg .tablink::before{content:"";position:absolute;left:-2px;top:12px;bottom:12px;width:1px;background:var(--line)}
.icon-btn svg{fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.subj-read{display:inline-flex;align-items:center;gap:6px;margin:0 16px 12px;padding:6px 12px;border-radius:99px;background:var(--accent-soft);color:var(--accent);font:700 .84rem var(--font-body);text-decoration:none}
.subj-read:hover{filter:brightness(.95)}
.sq-label a{font-weight:700;color:var(--accent)}
@media (min-width:720px) and (max-width:1060px){.brand-name{display:none}.seg .tab,.seg .tablink{padding-inline:13px}.topbar-in{gap:8px}}
@media (max-width:719px){
  .sq{width:40px!important;height:40px!important}
  .subj-read{min-height:44px;margin-bottom:14px}
  .chips-pick > *,.tchip{min-height:44px}
  .bn span,.bnlink span{font-size:.75rem}
  .bottomnav{grid-template-columns:repeat(5,1fr)!important}
  .bnlink{appearance:none;border:0;background:none;color:var(--muted);font:600 .72rem var(--font-body);min-height:56px;display:grid;justify-items:center;align-content:center;gap:3px;border-radius:14px;text-decoration:none;position:relative}
  .bnlink svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .bnlink:active{transform:scale(.96)}
}
</style>"""
# meta per usare il Quaderno come app dalla schermata Home del telefono, e per non finire sui motori di ricerca
PWA = ('<meta name="robots" content="noindex,nofollow,noarchive">'
       '<link rel="manifest" href="/manifest.webmanifest"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
       '<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes">'
       '<meta name="apple-mobile-web-app-title" content="Quaderno">')
RSLUG = ('const RSLUG = {"Algebra lineare":"algebra","Matematica discreta":"matematica-discreta","Fondamenti Info":"fondamenti",'
         '"Programmazione":"programmazione","Programmazione, Laboratorio":"laboratorio"};')
# l'avanzamento (capitoli studiati) non è più nel file dei dati: viene dalle evidenziazioni sul database, lette all'avvio
MERGE_AV = r"""
async function mergeAv(d) {
  try {
    const r = await fetch('/api/avanzamento', { credentials: 'same-origin' }); if (!r.ok) return d; const j = await r.json();
    const inv = { 'Algebra lineare': 'algebra', 'Matematica discreta': 'matematica-discreta', 'Fondamenti Info': 'fondamenti', 'Programmazione': 'programmazione' };
    const rng = l => { if (!l.length) return 'nessuno'; const p = []; let a = l[0]; for (let i = 0; i < l.length; i++) { if (i + 1 === l.length || l[i + 1] !== l[i] + 1) { p.push(a === l[i] ? String(a) : a + '-' + l[i]); a = l[i + 1]; } } return p.join(', '); };
    Object.keys(d.materie).forEach(m => {
      const x = j[inv[m]]; if (!x) return;
      const el = x.capitoli.map(c => ({ n: c.num, t: c.titolo.replace(/^\s*(?:Capitolo\s+)?\d+\s*[.:]?\s*/, ''), s: c.s, hl: c.hl, tot: c.tot }));
      const mm = d.materie[m]; mm.capitoli = el.length; mm.studiati = el.filter(c => c.s === 2).length; mm.elenco = el;
      const done = el.filter(c => c.s === 2).map(c => c.n), part = el.filter(c => c.s === 1).map(c => c.n), todo = el.filter(c => c.s === 0).map(c => c.n);
      mm.prossimo = 'Studiati: ' + rng(done) + '.' + (part.length ? ' In parte: ' + rng(part) + '.' : '') + (todo.length ? ' Da studiare: ' + rng(todo) + '.' : ' Tutto studiato.');
    });
  } catch (e) {}
  return d;
}
"""
LOGOUT_JS = ("<script>document.addEventListener('DOMContentLoaded',function(){var b=document.getElementById('logout-btn');"
             "if(b)b.addEventListener('click',function(){fetch('/api/logout',{method:'POST'}).then(function(){location.href='/login.html'})})});</script>")


def sostituisci(html, vecchio, nuovo, nome, regex=False):
    if regex:
        html, k = re.subn(vecchio, lambda m: nuovo(m) if callable(nuovo) else nuovo, html, count=1)
    else:
        k = html.count(vecchio)
        html = html.replace(vecchio, nuovo, 1)
    assert k >= 1, f"{nome}: punto di aggancio non trovato in index.html"
    return html


def adatta(html):
    # memoria del browser separata per utente (sullo stesso computer possono entrare più persone)
    html = sostituisci(html, r"const LS_KEY = '([^']+)';", lambda m: f"const LS_KEY = '{m.group(1)}:__QUSER__';", "LS_KEY", regex=True)
    html = sostituisci(html, r"\$\{greeting\(\)\} Emanuele", "${greeting()} __QNOME__", "saluto", regex=True)
    # "Riassunti" come voce del menu (schermi grandi) e della barra in basso (telefono)
    html = sostituisci(html, r"(Schede</button>\s*)(</nav>)", lambda m: m.group(1) + TABLINK + m.group(2), "menu", regex=True)
    html = sostituisci(html, r"(<span>Schede</span></button>\s*)(</nav>)", lambda m: m.group(1) + BNLINK + m.group(2), "barra in basso", regex=True)
    # pulsante Esci accanto al tema e alle impostazioni
    html = sostituisci(html, '<div class="tools">', '<div class="tools">' + ESCI, "strumenti")
    # link ai riassunti dalle carte delle materie e dai quadratini dei capitoli
    html = sostituisci(html, "let DATA = null;", "let DATA = null; " + RSLUG + MERGE_AV, "RSLUG")
    html = sostituisci(html, ".then(boot).catch(err => {", ".then(mergeAv).then(boot).catch(err => {", "avvio con avanzamento")
    html = sostituisci(html, '<div class="squares" role="group"',
                       '<a class="subj-read" href="riassunti/${RSLUG[m] || \'\'}.html">Leggi il riassunto &rarr;</a><div class="squares" role="group"', "carta materia")
    html = sostituisci(html, "${esc(b.dataset.t)} · ${st}`;",
                       "${esc(b.dataset.t)} · ${st} · <a href=\"riassunti/${RSLUG[card.dataset.m] || ''}.html#cap${b.dataset.n}\">Leggi</a>`;", "etichetta capitolo")
    html = sostituisci(html, "</style>", "</style>" + CSS_EXTRA, "stile")
    # la pagina costruita è un frammento (niente <head>/<body>): meta noindex all'inizio, script di uscita in fondo
    if "robots" not in html.lower():
        html = PWA + chr(10) + html
    return html + chr(10) + LOGOUT_JS + chr(10)


def controlli(repo, dest):
    """Prima di pubblicare: pagine non vuote e nessun capitolo in meno rispetto all'ultima versione pubblicata
    (protegge da un Word aperto a metà o danneggiato)."""
    p = []
    for nome, minimo in (("index.html", 100_000), ("data.json", 100_000)):
        f = dest / nome
        if not f.exists() or f.stat().st_size < minimo:
            p.append(f"{nome} mancante o troppo piccolo")
    for slug in ("algebra", "matematica-discreta", "fondamenti", "programmazione", "laboratorio"):
        f = dest / "riassunti" / f"{slug}.html"
        if not f.exists():
            p.append(f"riassunti/{slug}.html mancante"); continue
        ora = f.read_text(encoding="utf-8").count('<section class="cap"')
        r = subprocess.run(["git", "-C", str(repo), "show", f"HEAD:protected/riassunti/{slug}.html"], capture_output=True, text=True, encoding="utf-8")
        prima = r.stdout.count('<section class="cap"') if r.returncode == 0 else 0
        if ora == 0:
            p.append(f"{slug}: nessun capitolo")
        elif ora < prima:
            p.append(f"{slug}: {ora} capitoli, prima erano {prima}")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(REPO_DEFAULT))
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--no-build", action="store_true")
    ap.add_argument("--force", action="store_true", help="pubblica anche se i controlli non passano")
    a = ap.parse_args()
    repo = Path(a.repo)
    if not (repo / "vercel.json").exists():
        print("Repo del sito non trovato:", repo); return 1
    py = sys.executable
    if not a.no_build:
        # evidenziazioni attuali dal database: servono al Quaderno locale (avanzamento, piano); se non è raggiungibile si va avanti
        # e i progressi online di Emanuele (quiz, schede, errori, date d'esame): li leggono il piano serale e /esame
        for js in ("esporta_evid.js", "esporta_stato.js"):
            e = subprocess.run(["node", str(repo / "scripts" / js)], capture_output=True, text=True, encoding="utf-8", cwd=str(repo))
            print((e.stdout or e.stderr).strip().splitlines()[0] if (e.stdout or e.stderr).strip() else f"{js}: nessun output")
        # --diff: scrive evidenziazioni_oggi.md (sottolineature nuove dall'ultima volta), usato dal piano serale
        r = subprocess.run([py, "-X", "utf8", str(SCRIPTS / "costruisci_pagina_studio.py"), "--diff"], capture_output=True, text=True, encoding="utf-8")
        if r.returncode:
            print(r.stdout, r.stderr); return 1
        print((r.stdout.strip().splitlines() or ["build ok"])[0])
        # errori di scrittura rimasti nei riassunti (formule troncate, markdown, \n spezzati): solo avviso
        sys.path.insert(0, str(SCRIPTS))
        from lint_bozza import controlla_contenuti
        avvisi = [x for x in controlla_contenuti(repo) if "[evidenziato" not in x]
        if avvisi:
            print(f"AVVISO: {len(avvisi)} possibili errori nei riassunti (python lint_bozza.py --contenuti):")
            for x in avvisi[:10]:
                print("  -", x)
    dest = repo / "protected"
    if dest.exists():
        # svuota il contenuto senza dipendere dalla cartella stessa (Windows la blocca se un'altra finestra ci è dentro)
        for f in dest.iterdir():
            if f.is_dir():
                shutil.rmtree(f, ignore_errors=True)
            else:
                f.unlink()
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "index.html").write_text(adatta((PAG / "index.html").read_text(encoding="utf-8")), encoding="utf-8")
    shutil.copy2(PAG / "data.json", dest / "data.json")
    if (PAG / "img").exists():
        shutil.copytree(PAG / "img", dest / "img")
    r = subprocess.run([py, "-X", "utf8", "-W", "ignore", str(SCRIPTS / "riassunti_html.py"), str(dest), str(repo / "contenuti")], capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip())
    if r.returncode:
        print(r.stderr); return 1
    tot = sum(f.stat().st_size for f in dest.rglob("*") if f.is_file()) / 1048576
    print(f"protected/ pronta: {tot:.1f} MB")
    # Spazi separati (Quaderni di chi fa un altro corso): contenuti in spazi_contenuti/<nome>/ con spazio.json,
    # pagine generate in protected/_spazi/<nome>/. Chi li vede lo decide il campo "spazio" dell'utente (scripts/utenti.js spazio).
    spazi_cont = repo / "spazi_contenuti"
    if spazi_cont.exists():
        for sc in sorted(x for x in spazi_cont.iterdir() if x.is_dir() and (x / "spazio.json").exists()):
            sd = dest / "_spazi" / sc.name   # dentro protected/: vedi lib/spazi.js del sito
            if sd.exists():
                shutil.rmtree(sd, ignore_errors=True)
            sd.mkdir(parents=True, exist_ok=True)
            r = subprocess.run([py, "-X", "utf8", "-W", "ignore", str(SCRIPTS / "riassunti_html.py"), str(sd), str(sc)], capture_output=True, text=True, encoding="utf-8")
            if r.returncode:
                print(f"spazio {sc.name}: errore\n{r.stderr}"); return 1
            print(f"spazio {sc.name}: " + (r.stdout.strip().replace("\n", "; ") or "nessuna materia per ora"))
    problemi = controlli(repo, dest)
    if problemi and not a.force:
        print("\nCONTROLLI NON SUPERATI (non pubblico):")
        for x in problemi:
            print(" -", x)
        print("Se sono voluti, rilancia con --force.")
        return 2
    if a.push:
        g = lambda *x: subprocess.run(["git", "-C", str(repo), *x], capture_output=True, text=True, encoding="utf-8")
        g("add", "-A")
        # ultimo commit pubblicato davvero su Vercel: se un deploy è fallito, la sera dopo si ripubblica anche senza modifiche
        segno = repo / ".git" / "ultimo_deploy"
        ultimo = segno.read_text(encoding="utf-8").strip() if segno.exists() else ""
        modifiche = bool(g("status", "--porcelain").stdout.strip())
        if not modifiche and not a.force and ultimo == g("rev-parse", "HEAD").stdout.strip():
            print("Nessuna modifica da pubblicare."); return 0
        p = None
        if modifiche:
            msg = "Aggiornamento contenuti\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
            g("commit", "-q", "-m", msg)
            p = g("push", "-q")
            print("Salvato su GitHub." if p.returncode == 0 else "Push non riuscito: " + p.stderr.strip())
        else:
            print("Nessuna modifica nuova, ma l'ultimo commit non risulta pubblicato: ripubblico.")
        # Dal 30 ott 2026 il repo e' nell'organizzazione Personale-Giano: sul piano Hobby Vercel non collega
        # repo privati di organizzazione, quindi il sito si pubblica da questo PC con il CLI di Vercel.
        d = subprocess.run("vercel deploy --prod --yes", cwd=str(repo), shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if d.returncode == 0:
            segno.write_text(g("rev-parse", "HEAD").stdout.strip(), encoding="utf-8")
            print("Pubblicato su Vercel: https://quaderno-privato.vercel.app")
        else:
            print("Pubblicazione su Vercel non riuscita:", (d.stderr or d.stdout).strip()[-400:])
        return (p.returncode if p else 0) or d.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
