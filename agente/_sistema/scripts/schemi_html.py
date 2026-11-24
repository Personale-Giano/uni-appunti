"""Pagine «Schemi» del Quaderno online: schede di ripasso lampo (definizione semplificata, figura, punti chiave,
mini-codice, trabocchetto) scritte in _sistema/schemi/<slug>*.md secondo _sistema/schemi/FORMATO.md.

Uso: python schemi_html.py <cartella_uscita>        (es. <repo>/protected)
     python schemi_html.py --controlla               (solo controllo dei file .md)
Scrive: <uscita>/schemi/index.html, <uscita>/schemi/<slug>.html, <uscita>/schemi/img/
"""
import hashlib
import html
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
BASE = SCRIPTS.parent
SCHEMI = BASE / "schemi"
sys.path.insert(0, str(SCRIPTS))
from aggiungi_capitolo_sito import parti_da_testo  # noqa: E402
from migra_word import html_parti  # noqa: E402

MATERIE = [("programmazione", "Programmazione"), ("laboratorio", "Programmazione, Laboratorio"),
           ("algebra", "Algebra lineare"), ("matematica-discreta", "Matematica discreta"), ("fondamenti", "Fondamenti dell'Informatica")]
COLORI = {"algebra": ("#2744a8", "#8fadff"), "matematica-discreta": ("#b8302c", "#ff9188"), "fondamenti": ("#16703f", "#70dca2"),
          "programmazione": ("#b25a0a", "#ffb866"), "laboratorio": ("#7a4fb5", "#c3a6ff")}


def inl(t):
    return html_parti(parti_da_testo(t.strip()))


def ident(t):
    s = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return "s-" + (re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "x")


def leggi(slug):
    """Gruppi e schede dai file <slug>.md o <slug>_parte*.md (in ordine di nome)."""
    files = sorted(SCHEMI.glob(f"{slug}.md")) + sorted(SCHEMI.glob(f"{slug}_parte*.md"))
    gruppi, errori = [], []
    for f in files:
        gr = sc = None
        in_code, lang, codice = False, "", []
        for k, raw in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            riga = raw.rstrip()
            dove = f"{f.name}:{k}"
            if riga.lstrip().startswith("```"):
                if in_code:
                    if sc is None:
                        errori.append(f"{dove}: codice fuori da una scheda")
                    else:
                        sc["parti"].append(("code", lang, "\n".join(codice)))
                    codice = []
                else:
                    lang = riga.strip()[3:].strip()
                in_code = not in_code
                continue
            if in_code:
                codice.append(raw.rstrip("\n"))
                continue
            if not riga.strip():
                continue
            if riga.startswith("# "):
                gr = {"titolo": riga[2:].strip(), "schede": []}
                gruppi.append(gr); sc = None
                continue
            if riga.startswith("## "):
                if gr is None:
                    errori.append(f"{dove}: scheda prima di un gruppo"); gr = {"titolo": "Altro", "schede": []}; gruppi.append(gr)
                m = re.match(r"^##\s+(.*?)\s*(?:\{([^}]*)\})?\s*$", riga)
                caps = [c.strip() for c in (m.group(2) or "").split(",") if c.strip()]
                for c in caps:
                    if not re.fullmatch(r"(lab\s*)?\d+", c):
                        errori.append(f"{dove}: capitolo non valido «{c}»")
                sc = {"titolo": m.group(1).strip(), "caps": caps, "parti": []}
                gr["schede"].append(sc)
                continue
            if sc is None:
                errori.append(f"{dove}: riga fuori da una scheda: {riga[:60]}"); continue
            try:
                if riga.startswith("= "):
                    sc["parti"].append(("def", inl(riga[2:])))
                elif re.match(r"^\s*[-*] ", riga):
                    sc["parti"].append(("li", inl(re.sub(r"^\s*[-*] ", "", riga))))
                elif riga.startswith("! "):
                    sc["parti"].append(("warn", inl(re.sub(r"^(Trabocchetto|Attenzione|Errore tipico)\s*:\s*", "", riga[2:].strip(), flags=re.I))))
                elif riga.startswith("> "):
                    t = re.sub(r"^>\s*(Vedi anche:\s*)?", "", riga)
                    sc["parti"].append(("see", [x.strip() for x in t.split(",") if x.strip()]))
                elif re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", riga.strip()):
                    m = re.match(r"^!\[(.*?)\]\((.+?)\)\s*$", riga.strip())
                    p = m.group(2).split("|")[0].strip()
                    img = Path(p) if Path(p).is_absolute() else BASE / p
                    if not img.exists():
                        errori.append(f"{dove}: figura non trovata {p}")
                    else:
                        sc["parti"].append(("fig", m.group(1).strip(), img))
                else:
                    sc["parti"].append(("p", inl(riga)))
            except ValueError as e:
                errori.append(f"{dove}: {e}")
        if in_code:
            errori.append(f"{f.name}: blocco ``` non chiuso")
    titoli = {s["titolo"] for g in gruppi for s in g["schede"]}
    for g in gruppi:
        for s in g["schede"]:
            for p in s["parti"]:
                if p[0] == "see":
                    for t in p[1]:
                        if t not in titoli:
                            errori.append(f"{slug}: «Vedi anche» verso una scheda che non esiste: «{t}» (in «{s['titolo']}»)")
    return gruppi, errori


def codice_html(c):
    out = []
    for r in c.split("\n"):
        e = html.escape(r)
        for m in re.finditer(r"//", e):
            if e.count("&quot;", 0, m.start()) % 2 == 0:
                e = e[:m.start()] + f'<span class="cm">{e[m.start():]}</span>'
                break
        out.append(e)
    return "\n".join(out)


def scheda_html(s, slug, imgdir):
    sid = ident(s["titolo"])
    chips = ""
    for c in s["caps"]:
        lab = c.lower().startswith("lab")
        n = re.sub(r"\D", "", c)
        dest = "laboratorio" if (lab or slug == "laboratorio") else slug
        chips += f'<a class="cap" href="../riassunti/{dest}.html#cap{n}" title="Rileggi nel riassunto">{"Lab " if lab else "Cap. "}{n}</a>'
    corpo, lis = "", []

    def chiudi():
        nonlocal corpo, lis
        if lis:
            corpo += "<ul>" + "".join(f"<li>{x}</li>" for x in lis) + "</ul>"; lis = []
    for p in s["parti"]:
        if p[0] == "li":
            lis.append(p[1]); continue
        chiudi()
        if p[0] == "def":
            corpo += f'<p class="def">{p[1]}</p>'
        elif p[0] == "p":
            corpo += f"<p>{p[1]}</p>"
        elif p[0] == "warn":
            corpo += f'<p class="warn"><b>Attenzione</b> {p[1]}</p>'
        elif p[0] == "code":
            corpo += f'<pre><code>{codice_html(p[2])}</code></pre>'
        elif p[0] == "fig":
            blob = p[2].read_bytes()
            nome = hashlib.sha1(blob).hexdigest()[:14] + p[2].suffix.lower()
            (imgdir / nome).write_bytes(blob)
            alt = html.escape(p[1] or s["titolo"], quote=True)
            corpo += f'<figure><img src="img/{nome}" alt="{alt}" loading="lazy">' + (f"<figcaption>{html.escape(p[1])}</figcaption>" if p[1] else "") + "</figure>"
        elif p[0] == "see":
            corpo += '<p class="see">Vedi anche: ' + ", ".join(f'<a href="#{ident(t)}">{html.escape(t)}</a>' for t in p[1]) + "</p>"
    chiudi()
    return (f'<article class="sc" id="{sid}"><header><h3>{inl(s["titolo"])}</h3><span class="caps">{chips}</span></header>{corpo}</article>')


CSS = r"""
:root{--bg:#fbfaf7;--fg:#1d2330;--mut:#667085;--lin:#e3e0d8;--acc:#1f4e9c;--card:#fff;--cod:#f3f1ec;--bar:#fbfaf7e8;--warn:#b54708;--warnbg:#fff4e5;--defbg:#eef3fd;--mc:var(--mcl)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14171d;--fg:#e3e6ec;--mut:#98a1b3;--lin:#2a2f3a;--acc:#8fb4ff;--card:#1a1e26;--cod:#11141a;--bar:#14171de8;--warn:#ffb066;--warnbg:#2b2116;--defbg:#1b2436;--mc:var(--mcd)}}
:root[data-theme=dark]{--bg:#14171d;--fg:#e3e6ec;--mut:#98a1b3;--lin:#2a2f3a;--acc:#8fb4ff;--card:#1a1e26;--cod:#11141a;--bar:#14171de8;--warn:#ffb066;--warnbg:#2b2116;--defbg:#1b2436;--mc:var(--mcd)}
*{box-sizing:border-box}html{scroll-padding-top:120px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--acc)}button,input,select{font:inherit;color:inherit}
.top{position:sticky;top:0;z-index:20;background:var(--bar);backdrop-filter:blur(8px);border-bottom:1px solid var(--lin)}
.top-in{max-width:96rem;margin:0 auto;padding:.5rem 1rem;display:flex;align-items:center;gap:.6rem;flex-wrap:wrap}
.back{text-decoration:none;font-weight:600;white-space:nowrap}
.mat{font-weight:800;color:var(--mc);white-space:nowrap}
.grow{flex:1}
.search{display:flex;align-items:center;gap:.4rem;background:var(--card);border:1px solid var(--lin);border-radius:10px;padding:0 .6rem;min-height:40px;flex:1 1 16rem;max-width:30rem}
.search svg{width:18px;height:18px;fill:none;stroke:var(--mut);stroke-width:2;stroke-linecap:round}
.search input{border:0;background:none;outline:0;flex:1;min-width:0;padding:.45rem 0}
.search .n{color:var(--mut);font-size:.8rem;white-space:nowrap}
select,.ibtn{background:var(--card);border:1px solid var(--lin);border-radius:10px;min-height:40px;padding:0 .6rem;cursor:pointer}
.chips{max-width:96rem;margin:0 auto;padding:0 1rem .5rem;display:flex;gap:.4rem;overflow-x:auto;scrollbar-width:thin}
.chips a{flex:none;text-decoration:none;color:var(--fg);background:var(--card);border:1px solid var(--lin);border-radius:99px;padding:.25rem .7rem;font-size:.82rem;font-weight:600;white-space:nowrap}
.chips a:hover{border-color:var(--mc);color:var(--mc)}
main{max-width:96rem;margin:0 auto;padding:1rem 1rem 4rem}
.intro{color:var(--mut);margin:.2rem 0 1rem;max-width:52rem}
.gr>h2{font-size:1.15rem;margin:1.6rem 0 .7rem;color:var(--mc);display:flex;align-items:baseline;gap:.5rem}
.gr>h2 small{color:var(--mut);font-weight:600;font-size:.8rem}
.cols{columns:20rem;column-gap:.9rem}
.sc{break-inside:avoid;background:var(--card);border:1px solid var(--lin);border-top:3px solid var(--mc);border-radius:12px;padding:.7rem .85rem .75rem;margin:0 0 .9rem;transition:box-shadow .3s}
.sc.flash{box-shadow:0 0 0 3px var(--mc)}
.sc header{display:flex;align-items:flex-start;gap:.5rem;justify-content:space-between}
.sc h3{margin:0 0 .35rem;font-size:1.02rem;line-height:1.25}
.caps{display:flex;gap:.25rem;flex-wrap:wrap;justify-content:flex-end}
.cap{font-size:.72rem;font-weight:700;text-decoration:none;background:var(--defbg);border-radius:6px;padding:.1rem .4rem;white-space:nowrap}
.sc p{margin:.35rem 0}
.def{background:var(--defbg);border-radius:8px;padding:.4rem .6rem;font-weight:500}
.sc ul{margin:.35rem 0;padding-left:1.15rem}.sc li{margin:.15rem 0}
.warn{background:var(--warnbg);border-left:3px solid var(--warn);border-radius:6px;padding:.35rem .55rem;font-size:.92rem}
.warn b{color:var(--warn);margin-right:.25rem}
pre{background:var(--cod);border:1px solid var(--lin);border-radius:8px;padding:.45rem .6rem;margin:.4rem 0;overflow-x:auto;font:12.5px/1.45 ui-monospace,Consolas,"Cascadia Mono",monospace}
code{font-family:ui-monospace,Consolas,"Cascadia Mono",monospace;font-size:.9em;background:var(--cod);border-radius:4px;padding:0 .2em}
pre code{background:none;padding:0;font-size:inherit}
.cm{color:var(--mut);font-style:italic}
figure{margin:.4rem 0;text-align:center}
figure img{max-width:100%;max-height:210px;border-radius:6px;background:#fff;cursor:zoom-in}
figcaption{font-size:.78rem;color:var(--mut)}
.see{font-size:.85rem;color:var(--mut)}
.vuoto{color:var(--mut);padding:2rem 0;text-align:center}
#lb{position:fixed;inset:0;z-index:50;background:#000c;display:none;place-items:center;padding:1rem;cursor:zoom-out}
#lb.on{display:grid}#lb img{max-width:100%;max-height:100%;background:#fff;border-radius:8px}
mark{background:#ffe066;color:#000;border-radius:2px}
.idx{max-width:60rem;margin:0 auto;padding:1.5rem 1rem}
.idx h1{margin:.2rem 0}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:.8rem;margin-top:1rem}
.mcard{display:block;text-decoration:none;color:var(--fg);background:var(--card);border:1px solid var(--lin);border-top:4px solid var(--mc);border-radius:12px;padding:1rem}
.mcard b{display:block;font-size:1.05rem;color:var(--mc)}.mcard span{color:var(--mut);font-size:.88rem}
.mcard.off{opacity:.55;pointer-events:none}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .mcard,:root:not([data-theme=light]) body{--mc:var(--mcd)}}
:root[data-theme=dark] .mcard,:root[data-theme=dark] body{--mc:var(--mcd)}
body{--mc:var(--mcl)}.mcard{--mc:var(--mcl)}
@media (max-width:719px){.top-in{padding:.45rem .75rem}.search{order:5;flex-basis:100%;max-width:none}.cols{columns:1}main{padding:.6rem .75rem 4rem}html{scroll-padding-top:150px}}
@media print{.top,.chips,#lb{display:none}.sc{border-color:#999}}
"""

JS_TEMA = ("(function(){try{var t=localStorage.getItem('quaderno-tema');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t)}catch(e){}})();")
JS = r"""
(function(){
var q=document.getElementById('q'),cnt=document.getElementById('cnt'),cards=[].slice.call(document.querySelectorAll('.sc')),grs=[].slice.call(document.querySelectorAll('.gr'));
function norm(s){return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase()}
cards.forEach(function(c){c._t=norm(c.textContent);c._h=c.querySelector('h3').innerHTML});
function filtra(){var v=norm(q.value.trim()),parole=v.split(/\s+/).filter(Boolean),n=0;
 cards.forEach(function(c){var ok=parole.every(function(p){return c._t.indexOf(p)>=0});c.hidden=!ok;if(ok)n++;
   var h=c.querySelector('h3');h.innerHTML=c._h;});
 grs.forEach(function(g){g.hidden=!g.querySelector('.sc:not([hidden])')});
 cnt.textContent=parole.length?(n+(n===1?' scheda':' schede')):'';
 document.getElementById('vuoto').hidden=n>0;
 try{history.replaceState(null,'',parole.length?'#q='+encodeURIComponent(q.value.trim()):location.pathname)}catch(e){}}
q.addEventListener('input',filtra);
document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus()}if(e.key==='Escape'&&document.activeElement===q){q.value='';filtra();q.blur()}});
function vai(id){var el=document.getElementById(id);if(!el)return;if(el.hidden){q.value='';filtra()}el.scrollIntoView({block:'start'});el.classList.add('flash');setTimeout(function(){el.classList.remove('flash')},1600)}
document.addEventListener('click',function(e){var a=e.target.closest('a[href^="#s-"]');if(a){e.preventDefault();vai(a.getAttribute('href').slice(1));try{history.replaceState(null,'',a.getAttribute('href'))}catch(x){}}
 var im=e.target.closest('figure img');if(im){var lb=document.getElementById('lb');lb.querySelector('img').src=im.src;lb.classList.add('on')}});
document.getElementById('lb').addEventListener('click',function(){this.classList.remove('on')});
var h=decodeURIComponent(location.hash.slice(1));if(h.indexOf('q=')===0){q.value=h.slice(2);filtra()}else if(h)setTimeout(function(){vai(h)},50);
var tb=document.getElementById('theme'),root=document.documentElement;
function lab(){var t='auto';try{t=localStorage.getItem('quaderno-tema')||'auto'}catch(e){}tb.textContent={auto:'Tema: auto',light:'Tema: chiaro',dark:'Tema: scuro'}[t]||'Tema'}
lab();tb.addEventListener('click',function(){var t='auto';try{t=localStorage.getItem('quaderno-tema')||'auto'}catch(e){}var n={auto:'light',light:'dark',dark:'auto'}[t]||'auto';try{localStorage.setItem('quaderno-tema',n)}catch(e){}if(n==='auto')root.removeAttribute('data-theme');else root.setAttribute('data-theme',n);lab()});
var ms=document.getElementById('mats');if(ms)ms.addEventListener('change',function(){location.href=ms.value});
})();
"""
IC_CERCA = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>'


def pagina(titolo, corpo, style=""):
    return ('<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="robots" content="noindex,nofollow,noarchive"><meta name="color-scheme" content="light dark">'
            '<link rel="manifest" href="/manifest.webmanifest"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
            f'<title>{html.escape(titolo)}</title><script>{JS_TEMA}</script><style>{CSS}</style></head>{corpo}</html>')


def main(argv):
    solo_controllo = "--controlla" in argv
    pronte, tutti_errori = [], []
    for slug, nome in MATERIE:
        gruppi, err = leggi(slug)
        tutti_errori += err
        if gruppi:
            pronte.append((slug, nome, gruppi))
    for e in tutti_errori:
        print("ERRORE:", e)
    if solo_controllo:
        for slug, nome, g in pronte:
            print(f"{nome}: {len(g)} gruppi, {sum(len(x['schede']) for x in g)} schede")
        return 1 if tutti_errori else 0
    if tutti_errori:
        return 1
    base = Path(argv[1]) / "schemi"
    imgdir = base / "img"
    imgdir.mkdir(parents=True, exist_ok=True)
    opzioni = "".join(f'<option value="{s}.html">{html.escape(n)}</option>' for s, n, _ in pronte)
    for slug, nome, gruppi in pronte:
        cl, cd = COLORI[slug]
        nsch = sum(len(g["schede"]) for g in gruppi)
        chips = "".join(f'<a href="#g{i}">{html.escape(g["titolo"])}</a>' for i, g in enumerate(gruppi))
        sez = "".join(f'<section class="gr" id="g{i}"><h2>{html.escape(g["titolo"])}<small>{len(g["schede"])}</small></h2>'
                      f'<div class="cols">{"".join(scheda_html(s, slug, imgdir) for s in g["schede"])}</div></section>' for i, g in enumerate(gruppi))
        top = ('<header class="top"><div class="top-in"><a class="back" href="../">&larr; Quaderno</a>'
               f'<span class="mat">Schemi · {html.escape(nome)}</span>'
               f'<label class="search">{IC_CERCA}<input id="q" type="search" placeholder="Cerca un concetto ( / )" aria-label="Cerca un concetto" autocomplete="off"><span class="n" id="cnt"></span></label>'
               + (f'<select id="mats" aria-label="Cambia materia">{opzioni.replace(f"value=\"{slug}.html\"", f"value=\"{slug}.html\" selected")}</select>' if len(pronte) > 1 else "")
               + f'<button class="ibtn" id="theme" type="button">Tema</button></div><nav class="chips" aria-label="Argomenti">{chips}</nav></header>')
        corpo = (f'<body style="--mcl:{cl};--mcd:{cd}">{top}<main><p class="intro">{nsch} schede per ripassare al volo un concetto: '
                 'definizione semplice, punti chiave, esempio ed errore tipico. Il numero in alto a destra di ogni scheda porta al capitolo del riassunto.</p>'
                 f'{sez}<p class="vuoto" id="vuoto" hidden>Nessuna scheda trovata. Prova con un\'altra parola.</p></main>'
                 f'<div id="lb"><img alt=""></div><script>{JS}</script></body>')
        (base / f"{slug}.html").write_text(pagina(f"Schemi · {nome}", corpo), encoding="utf-8")
        print(f"schemi {nome}: {len(gruppi)} gruppi, {nsch} schede")
    pronti = {s for s, _, _ in pronte}
    cards = ""
    for slug, nome in MATERIE:
        cl, cd = COLORI[slug]
        g = next((x[2] for x in pronte if x[0] == slug), None)
        sub = f"{sum(len(x['schede']) for x in g)} schede" if g else "in preparazione"
        cards += (f'<a class="mcard{"" if slug in pronti else " off"}" href="{slug}.html" style="--mcl:{cl};--mcd:{cd}"><b>{html.escape(nome)}</b><span>{sub}</span></a>')
    idx = ('<body><header class="top"><div class="top-in"><a class="back" href="../">&larr; Quaderno</a><span class="mat">Schemi</span><span class="grow"></span>'
           '<button class="ibtn" id="theme" type="button">Tema</button></div></header>'
           '<div class="idx"><h1>Schemi</h1><p class="intro">Ripasso lampo: quando stai studiando un capitolo avanzato e non ricordi un concetto passato, cercalo qui e rinfrescalo in pochi secondi.</p>'
           f'<div class="grid">{cards}</div><p class="intro" style="margin-top:1.5rem">Aggiornato il {datetime.now().strftime("%d/%m/%Y")}.</p></div>'
           '<script>(function(){var tb=document.getElementById("theme"),root=document.documentElement;function lab(){var t="auto";try{t=localStorage.getItem("quaderno-tema")||"auto"}catch(e){}tb.textContent={auto:"Tema: auto",light:"Tema: chiaro",dark:"Tema: scuro"}[t]}lab();tb.onclick=function(){var t="auto";try{t=localStorage.getItem("quaderno-tema")||"auto"}catch(e){}var n={auto:"light",light:"dark",dark:"auto"}[t];try{localStorage.setItem("quaderno-tema",n)}catch(e){}if(n==="auto")root.removeAttribute("data-theme");else root.setAttribute("data-theme",n);lab()}})();</script></body>')
    (base / "index.html").write_text(pagina("Schemi", idx), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
