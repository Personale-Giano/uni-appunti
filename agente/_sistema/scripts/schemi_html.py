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


IC = {
    "cerca": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>',
    "warn": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5 2.8 19.5h18.4z"/><path d="M12 10v4.2M12 17v.1"/></svg>',
    "libro": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 19V5.5"/></svg>',
    "link": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>',
    "tema": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor" stroke="none"/></svg>',
    "lista": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01"/></svg>',
    "comp": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h10M4 17h7"/></svg>',
    "esp": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8 9h8M8 13h8M8 17h5"/></svg>',
}


def scheda_html(s, slug, imgdir):
    sid = ident(s["titolo"])
    chips = ""
    for c in s["caps"]:
        lab = c.lower().startswith("lab")
        n = re.sub(r"\D", "", c)
        dest = "laboratorio" if (lab or slug == "laboratorio") else slug
        chips += f'<a class="cap" href="../riassunti/{dest}.html#cap{n}" title="Rileggi nel riassunto">{"Lab " if lab else "Cap. "}{n}</a>'
    defn, corpo, lis = "", "", []

    def chiudi():
        nonlocal corpo, lis
        if lis:
            corpo += '<ul class="pts">' + "".join(f"<li>{x}</li>" for x in lis) + "</ul>"; lis = []
    for p in s["parti"]:
        if p[0] == "li":
            lis.append(p[1]); continue
        chiudi()
        if p[0] == "def" and not defn and not corpo:
            defn = f'<p class="def">{p[1]}</p>'
        elif p[0] in ("def", "p"):
            corpo += f"<p>{p[1]}</p>"
        elif p[0] == "warn":
            corpo += f'<div class="warn">{IC["warn"]}<p>{p[1]}</p></div>'
        elif p[0] == "code":
            corpo += f'<pre><code>{codice_html(p[2])}</code></pre>'
        elif p[0] == "fig":
            blob = p[2].read_bytes()
            nome = hashlib.sha1(blob).hexdigest()[:14] + p[2].suffix.lower()
            (imgdir / nome).write_bytes(blob)
            alt = html.escape(p[1] or s["titolo"], quote=True)
            corpo += (f'<figure><button class="zoom" type="button" aria-label="Ingrandisci la figura"><img src="img/{nome}" alt="{alt}" loading="lazy"></button>'
                      + (f"<figcaption>{html.escape(p[1])}</figcaption>" if p[1] else "") + "</figure>")
        elif p[0] == "see":
            corpo += '<div class="see">' + IC["link"] + "".join(f'<a href="#{ident(t)}">{html.escape(t)}</a>' for t in p[1]) + "</div>"
    chiudi()
    return (f'<article class="sc" id="{sid}"><header><h3>{inl(s["titolo"])}</h3><span class="caps">{chips}</span></header>'
            f'{defn}<div class="more">{corpo}</div></article>')


CSS = r"""
:root{--bg:#f4f6fb;--bar:rgba(244,246,251,.9);--surface:#fff;--surface-2:#eef1f7;--ink:#151b2e;--muted:#5a6479;--line:#dbe1ec;--accent:#2744a8;
--warn:#b54708;--warn-bg:#fff4e6;--code:#f3f5fa;--shadow:0 1px 0 rgba(28,37,66,.05),0 10px 26px -16px rgba(28,37,66,.3);
--font-display:'Bricolage Grotesque','Segoe UI Variable Display','Segoe UI',system-ui,sans-serif;--font-body:'Source Sans 3','Segoe UI',system-ui,'Cambria Math','Segoe UI Symbol',sans-serif;
--font-mono:'JetBrains Mono',ui-monospace,'Cascadia Mono',Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f131b;--bar:rgba(15,19,27,.9);--surface:#181d28;--surface-2:#1f2633;--ink:#e9edf5;--muted:#9ba6ba;--line:#2b3444;--accent:#8fadff;--warn:#ffb066;--warn-bg:#2a2117;--code:#121721;--shadow:0 1px 0 rgba(0,0,0,.3),0 12px 28px -16px rgba(0,0,0,.65)}}
:root[data-theme=dark]{--bg:#0f131b;--bar:rgba(15,19,27,.9);--surface:#181d28;--surface-2:#1f2633;--ink:#e9edf5;--muted:#9ba6ba;--line:#2b3444;--accent:#8fadff;--warn:#ffb066;--warn-bg:#2a2117;--code:#121721;--shadow:0 1px 0 rgba(0,0,0,.3),0 12px 28px -16px rgba(0,0,0,.65)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-padding-top:84px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 var(--font-body)}
body,.mcard{--mc:var(--mcl)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) body,:root:not([data-theme=light]) .mcard{--mc:var(--mcd)}}
:root[data-theme=dark] body,:root[data-theme=dark] .mcard{--mc:var(--mcd)}
a{color:var(--accent)}button,input,select{font:inherit;color:inherit}
svg{fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.mc-soft{background:color-mix(in srgb,var(--mc) 13%,var(--surface))}
/* barra in alto */
.top{position:sticky;top:0;z-index:20;background:var(--bar);backdrop-filter:saturate(1.4) blur(10px);-webkit-backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--line)}
.top-in{max-width:100rem;margin:0 auto;padding:.6rem 1.25rem;display:flex;align-items:center;gap:.75rem}
.back{display:inline-flex;align-items:center;gap:.3rem;text-decoration:none;font-weight:600;color:var(--muted);white-space:nowrap;min-height:44px}
.back:hover{color:var(--ink)}
.ttl{display:flex;flex-direction:column;line-height:1.1;min-width:0}
.ttl small{font:700 .7rem var(--font-body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.ttl b{font:700 1.15rem var(--font-display);color:var(--mc);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.search{flex:1;max-width:34rem;margin-left:auto;display:flex;align-items:center;gap:.5rem;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:0 .75rem;min-height:44px;box-shadow:var(--shadow);transition:border-color .2s}
.search:focus-within{border-color:var(--mc)}
.search svg{width:19px;height:19px;color:var(--muted);flex:none}
.search input{border:0;background:none;outline:0;flex:1;min-width:0;padding:.55rem 0;font-size:1rem}
.search input::-webkit-search-cancel-button{cursor:pointer}
.search .n{color:var(--muted);font-size:.8rem;white-space:nowrap}
.ib{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:12px;border:1px solid var(--line);background:var(--surface);cursor:pointer;color:var(--muted);flex:none}
.ib:hover{color:var(--ink)}.ib svg{width:20px;height:20px}
.ib[aria-pressed=true]{color:var(--mc);border-color:var(--mc)}
select.ib{width:auto;padding:0 .6rem;font-size:.9rem;color:var(--ink)}
/* struttura */
.wrap{max-width:100rem;margin:0 auto;display:grid;grid-template-columns:15.5rem minmax(0,1fr);gap:2rem;padding:0 1.25rem}
.side{position:sticky;top:76px;align-self:start;max-height:calc(100vh - 92px);overflow:auto;padding:1.25rem 0 2rem;scrollbar-width:none}
.side::-webkit-scrollbar{display:none}
.side h4{margin:0 0 .5rem .6rem;font:700 .72rem var(--font-body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.side a{display:flex;justify-content:space-between;gap:.5rem;padding:.42rem .6rem;border-radius:9px;text-decoration:none;color:var(--muted);font-weight:600;font-size:.93rem;line-height:1.25}
.side a span{font:600 .75rem var(--font-mono);opacity:.75;padding-top:.15rem}
.side a:hover{color:var(--ink);background:var(--surface-2)}
.side a.on{color:var(--mc);background:color-mix(in srgb,var(--mc) 12%,transparent)}
main{padding:1.25rem 0 5rem;min-width:0}
.hero{margin:.2rem 0 1.4rem}
.hero h1{margin:0;font:800 clamp(1.6rem,3vw,2.2rem)/1.1 var(--font-display);letter-spacing:-.01em}
.hero p{margin:.4rem 0 0;color:var(--muted);max-width:46rem}
.gr{margin:0 0 2.2rem}
.gr>h2{display:flex;align-items:center;gap:.6rem;margin:0 0 .9rem;font:700 1.25rem var(--font-display)}
.gr>h2::before{content:"";width:10px;height:10px;border-radius:3px;background:var(--mc);flex:none}
.gr>h2 small{font:600 .78rem var(--font-mono);color:var(--muted);background:var(--surface-2);border-radius:99px;padding:.1rem .5rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(20rem,1fr));gap:1rem;align-items:start}
/* scheda */
.sc{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1rem 1.1rem 1.05rem;box-shadow:var(--shadow);transition:box-shadow .3s,transform .2s}
.sc::before{content:"";position:absolute;left:0;top:14px;bottom:14px;width:4px;border-radius:0 4px 4px 0;background:var(--mc)}
.sc.flash{box-shadow:0 0 0 3px var(--mc),var(--shadow)}
.sc header{display:flex;align-items:flex-start;justify-content:space-between;gap:.6rem;margin-bottom:.55rem}
.sc h3{margin:0;font:700 1.08rem/1.25 var(--font-display);letter-spacing:-.005em}
.caps{display:flex;gap:.3rem;flex-wrap:wrap;justify-content:flex-end;flex:none;max-width:45%}
.cap{font:600 .72rem var(--font-mono);text-decoration:none;color:var(--mc);border:1px solid color-mix(in srgb,var(--mc) 45%,transparent);border-radius:99px;padding:.12rem .5rem;white-space:nowrap}
.cap:hover{background:color-mix(in srgb,var(--mc) 12%,transparent)}
.def{margin:0;padding:.6rem .8rem;border-radius:11px;background:color-mix(in srgb,var(--mc) 11%,var(--surface));font-weight:500;line-height:1.5}
.more>*:first-child{margin-top:.65rem}
.more p{margin:.5rem 0}
.pts{list-style:none;margin:.6rem 0;padding:0;display:grid;gap:.35rem}
.pts li{position:relative;padding-left:1.1rem;line-height:1.45}
.pts li::before{content:"";position:absolute;left:.15rem;top:.62em;width:6px;height:6px;border-radius:2px;background:color-mix(in srgb,var(--mc) 70%,var(--surface))}
.warn{display:flex;gap:.55rem;align-items:flex-start;margin:.7rem 0 0;padding:.55rem .7rem;border-radius:11px;background:var(--warn-bg);color:var(--ink);font-size:.95rem}
.warn svg{width:18px;height:18px;color:var(--warn);flex:none;margin-top:.12rem}
.warn p{margin:0}
pre{margin:.6rem 0;padding:.6rem .75rem;background:var(--code);border:1px solid var(--line);border-radius:11px;overflow-x:auto;font:500 12.8px/1.5 var(--font-mono);scrollbar-width:thin}
code{font:500 .86em var(--font-mono);background:var(--code);border:1px solid var(--line);border-radius:5px;padding:0 .25em}
pre code{background:none;border:0;padding:0;font-size:inherit}
.cm{color:var(--muted);font-style:italic}
figure{margin:.65rem 0 .2rem;text-align:center}
.zoom{all:unset;cursor:zoom-in;display:block;border-radius:10px;overflow:hidden;background:#fff;border:1px solid var(--line)}
.zoom img{display:block;max-width:100%;max-height:200px;margin:0 auto;object-fit:contain}
figcaption{margin-top:.3rem;font-size:.8rem;color:var(--muted)}
.see{display:flex;flex-wrap:wrap;align-items:center;gap:.35rem;margin-top:.7rem}
.see svg{width:16px;height:16px;color:var(--muted)}
.see a{font-size:.82rem;font-weight:600;text-decoration:none;color:var(--ink);background:var(--surface-2);border-radius:99px;padding:.15rem .6rem}
.see a:hover{color:var(--mc)}
/* modo compatto: solo titolo e definizione, tocco per aprire */
body.compatto .more{display:none}
body.compatto .sc{cursor:pointer}
body.compatto .sc.aperta .more{display:block}
body.compatto .sc:not(.aperta) header::after{content:"+";position:absolute;right:1rem;bottom:.7rem;font:700 1rem var(--font-mono);color:var(--muted)}
body.compatto .grid{grid-template-columns:repeat(auto-fill,minmax(17rem,1fr))}
mark{background:color-mix(in srgb,#ffd43b 70%,transparent);color:inherit;border-radius:3px;padding:0 1px}
.vuoto{color:var(--muted);padding:3rem 0;text-align:center}
#lb{position:fixed;inset:0;z-index:50;background:rgba(5,8,14,.82);display:none;place-items:center;padding:1rem;cursor:zoom-out}
#lb.on{display:grid}#lb img{max-width:100%;max-height:100%;background:#fff;border-radius:12px}
#gsel{display:none}
/* indice delle materie */
.idx{max-width:62rem;margin:0 auto;padding:2rem 1.25rem}
.idx h1{margin:.2rem 0;font:800 2.2rem var(--font-display)}
.idx p{color:var(--muted)}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(16rem,1fr));gap:1rem;margin-top:1.4rem}
.mcard{display:block;text-decoration:none;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.1rem 1.2rem;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:transform .2s}
.mcard:hover{transform:translateY(-2px)}
.mcard::before{content:"";position:absolute;inset:0 auto 0 0;width:5px;background:var(--mc)}
.mcard b{display:block;font:700 1.15rem var(--font-display);color:var(--mc)}
.mcard span{color:var(--muted);font-size:.9rem}
.mcard.off{opacity:.5;pointer-events:none}
.mcard{--mc:var(--mcl)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .mcard{--mc:var(--mcd)}}
:root[data-theme=dark] .mcard{--mc:var(--mcd)}
@media (max-width:999px){.wrap{grid-template-columns:minmax(0,1fr);gap:0}.side{display:none}#gsel{display:inline-grid;max-width:10rem}#mats{display:none}.back span{display:none}.ttl{flex:0 1 auto;min-width:0}.search{min-width:0}}
@media (max-width:719px){
 .top-in{flex-wrap:wrap;padding:.45rem .8rem;gap:.45rem}.search{order:9;flex-basis:100%;max-width:none;margin:0}
 .back span{display:none}.back{min-width:28px}.ttl{flex:1}.ttl b{font-size:1rem}#mats{display:none}
 .ib{width:40px;height:40px}#gsel{width:7rem;max-width:7rem;height:40px}
 .wrap{padding:0 .8rem}.grid,body.compatto .grid{grid-template-columns:minmax(0,1fr)}
 html{scroll-padding-top:118px}.hero{margin-bottom:1rem}.hero h1{font-size:1.4rem}.hero p{display:none}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
@media print{.top,.side,#lb{display:none}.wrap{display:block}.sc{box-shadow:none;break-inside:avoid}}
"""

FONTI = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=JetBrains+Mono:wght@500;600&family=Source+Sans+3:wght@400;500;600;700&display=swap">')
JS_TEMA = ("(function(){try{var t=localStorage.getItem('quaderno-tema');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);"
           "if(localStorage.getItem('schemi-compatto')==='1')document.documentElement.classList.add('pre-comp')}catch(e){}})();")
JS_TEMA_BTN = r"""
(function(){var tb=document.getElementById('theme'),root=document.documentElement;if(!tb)return;
function get(){try{return localStorage.getItem('quaderno-tema')||'auto'}catch(e){return 'auto'}}
function lab(){var t=get();tb.title={auto:'Tema: automatico',light:'Tema: chiaro',dark:'Tema: scuro'}[t];tb.setAttribute('aria-label',tb.title)}
lab();tb.addEventListener('click',function(){var n={auto:'light',light:'dark',dark:'auto'}[get()]||'auto';try{localStorage.setItem('quaderno-tema',n)}catch(e){}
if(n==='auto')root.removeAttribute('data-theme');else root.setAttribute('data-theme',n);lab()})})();
"""
JS = r"""
(function(){
var q=document.getElementById('q'),cnt=document.getElementById('cnt'),cards=[].slice.call(document.querySelectorAll('.sc')),grs=[].slice.call(document.querySelectorAll('.gr'));
function norm(s){return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase()}
cards.forEach(function(c){c._t=norm(c.textContent)});
function filtra(){var v=norm(q.value.trim()),parole=v.split(/\s+/).filter(Boolean),n=0;
 cards.forEach(function(c){var ok=parole.every(function(p){return c._t.indexOf(p)>=0});c.hidden=!ok;if(ok)n++;
   if(document.body.classList.contains('compatto'))c.classList.toggle('aperta',!!parole.length&&ok&&n<=3)});
 grs.forEach(function(g){g.hidden=!g.querySelector('.sc:not([hidden])')});
 cnt.textContent=parole.length?(n+(n===1?' scheda':' schede')):'';
 document.getElementById('vuoto').hidden=n>0;spia();
 try{history.replaceState(null,'',parole.length?'#q='+encodeURIComponent(q.value.trim()):location.pathname)}catch(e){}}
q.addEventListener('input',filtra);
document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus()}if(e.key==='Escape'&&document.activeElement===q){q.value='';filtra();q.blur()}});
function vai(id){var el=document.getElementById(id);if(!el)return;if(el.hidden){q.value='';filtra()}el.classList.add('aperta');el.scrollIntoView({block:'start',behavior:'smooth'});el.classList.add('flash');setTimeout(function(){el.classList.remove('flash')},1600)}
document.addEventListener('click',function(e){
 var a=e.target.closest('a[href^="#s-"]');if(a){e.preventDefault();vai(a.getAttribute('href').slice(1));try{history.replaceState(null,'',a.getAttribute('href'))}catch(x){}return}
 var z=e.target.closest('.zoom');if(z){var lb=document.getElementById('lb');lb.querySelector('img').src=z.querySelector('img').src;lb.classList.add('on');return}
 var c=e.target.closest('.sc');if(c&&document.body.classList.contains('compatto')&&!e.target.closest('a,pre,button')){c.classList.toggle('aperta')}});
document.getElementById('lb').addEventListener('click',function(){this.classList.remove('on')});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.getElementById('lb').classList.remove('on')});
/* modo compatto */
var cb=document.getElementById('comp');
function setComp(on){document.body.classList.toggle('compatto',on);cb.setAttribute('aria-pressed',String(on));cb.title=on?'Mostra le schede complete':'Mostra solo le definizioni';cb.setAttribute('aria-label',cb.title);
 cb.innerHTML=on?cb.dataset.esp:cb.dataset.comp;try{localStorage.setItem('schemi-compatto',on?'1':'0')}catch(e){}}
setComp(document.documentElement.classList.contains('pre-comp'));
cb.addEventListener('click',function(){setComp(!document.body.classList.contains('compatto'));cards.forEach(function(c){c.classList.remove('aperta')})});
/* argomento corrente nell'indice laterale */
var links=[].slice.call(document.querySelectorAll('.side a'));
function spia(){var y=window.scrollY+120,cur=null;grs.forEach(function(g){if(!g.hidden&&g.offsetTop<=y)cur=g.id});links.forEach(function(l){l.classList.toggle('on',l.getAttribute('href')==='#'+cur)})}
window.addEventListener('scroll',spia,{passive:true});spia();
var gs=document.getElementById('gsel');gs.addEventListener('change',function(){if(gs.value){document.getElementById(gs.value).scrollIntoView({block:'start',behavior:'smooth'});gs.value=''}});
var ms=document.getElementById('mats');if(ms)ms.addEventListener('change',function(){location.href=ms.value});
var h=decodeURIComponent(location.hash.slice(1));if(h.indexOf('q=')===0){q.value=h.slice(2);filtra()}else if(h.indexOf('s-')===0)setTimeout(function(){vai(h)},60);
})();
"""


def pagina(titolo, corpo):
    return ('<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="robots" content="noindex,nofollow,noarchive"><meta name="color-scheme" content="light dark">'
            '<meta name="theme-color" media="(prefers-color-scheme:light)" content="#f4f6fb"><meta name="theme-color" media="(prefers-color-scheme:dark)" content="#0f131b">'
            '<link rel="manifest" href="/manifest.webmanifest"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
            f'<title>{html.escape(titolo)}</title>{FONTI}<script>{JS_TEMA}</script><style>{CSS}</style></head>{corpo}</html>')


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
    for slug, nome, gruppi in pronte:
        cl, cd = COLORI[slug]
        nsch = sum(len(g["schede"]) for g in gruppi)
        side = "".join(f'<a href="#g{i}">{html.escape(g["titolo"])}<span>{len(g["schede"])}</span></a>' for i, g in enumerate(gruppi))
        gopt = '<option value="">Argomenti</option>' + "".join(f'<option value="g{i}">{html.escape(g["titolo"])}</option>' for i, g in enumerate(gruppi))
        sez = "".join(f'<section class="gr" id="g{i}"><h2>{html.escape(g["titolo"])}<small>{len(g["schede"])}</small></h2>'
                      f'<div class="grid">{"".join(scheda_html(s, slug, imgdir) for s in g["schede"])}</div></section>' for i, g in enumerate(gruppi))
        mats = ""
        if len(pronte) > 1:
            opz = "".join(f'<option value="{s}.html"{" selected" if s == slug else ""}>{html.escape(n)}</option>' for s, n, _ in pronte)
            mats = f'<select class="ib" id="mats" aria-label="Cambia materia">{opz}</select>'
        top = ('<header class="top"><div class="top-in"><a class="back" href="../" aria-label="Torna al Quaderno">&larr;<span>Quaderno</span></a>'
               f'<div class="ttl"><small>Schemi</small><b>{html.escape(nome)}</b></div>'
               f'<label class="search">{IC["cerca"]}<input id="q" type="search" placeholder="Cerca un concetto…" aria-label="Cerca un concetto" autocomplete="off" enterkeyhint="search"><span class="n" id="cnt"></span></label>'
               f'<select class="ib" id="gsel" aria-label="Vai a un argomento">{gopt}</select>{mats}'
               f'<button class="ib" id="comp" type="button" aria-pressed="false" data-comp=\'{IC["comp"]}\' data-esp=\'{IC["esp"]}\'>{IC["comp"]}</button>'
               f'<button class="ib" id="theme" type="button">{IC["tema"]}</button></div></header>')
        corpo = (f'<body style="--mcl:{cl};--mcd:{cd}">{top}<div class="wrap"><nav class="side" aria-label="Argomenti"><h4>Argomenti</h4>{side}</nav>'
                 f'<main><div class="hero"><h1>Ripasso lampo</h1><p>{nsch} concetti in {len(gruppi)} argomenti: definizione in breve, punti chiave, esempio ed errore tipico. '
                 'Cerca una parola, oppure usa il pulsante accanto alla ricerca per vedere solo le definizioni. I numeri sulle schede riaprono il capitolo del riassunto.</p></div>'
                 f'{sez}<p class="vuoto" id="vuoto" hidden>Nessuna scheda trovata. Prova con un\'altra parola.</p></main></div>'
                 f'<div id="lb" role="dialog" aria-label="Figura ingrandita"><img alt=""></div><script>{JS}{JS_TEMA_BTN}</script></body>')
        (base / f"{slug}.html").write_text(pagina(f"Schemi · {nome}", corpo), encoding="utf-8")
        print(f"schemi {nome}: {len(gruppi)} gruppi, {nsch} schede")
    pronti = {s for s, _, _ in pronte}
    cards = ""
    for slug, nome in MATERIE:
        cl, cd = COLORI[slug]
        g = next((x[2] for x in pronte if x[0] == slug), None)
        sub = f"{sum(len(x['schede']) for x in g)} schede · {len(g)} argomenti" if g else "in preparazione"
        cards += f'<a class="mcard{"" if slug in pronti else " off"}" href="{slug}.html" style="--mcl:{cl};--mcd:{cd}"><b>{html.escape(nome)}</b><span>{sub}</span></a>'
    idx = ('<body style="--mcl:#2744a8;--mcd:#8fadff"><header class="top"><div class="top-in"><a class="back" href="../">&larr;<span>Quaderno</span></a>'
           '<div class="ttl"><small>Quaderno</small><b>Schemi</b></div><span style="flex:1"></span>'
           f'<button class="ib" id="theme" type="button">{IC["tema"]}</button></div></header>'
           '<div class="idx"><h1>Schemi</h1><p>Ripasso lampo: quando stai studiando un capitolo avanzato e non ricordi un concetto passato, cercalo qui e rinfrescalo in pochi secondi.</p>'
           f'<div class="mgrid">{cards}</div><p style="margin-top:1.6rem;font-size:.85rem">Aggiornato il {datetime.now().strftime("%d/%m/%Y")}.</p></div>'
           f'<script>{JS_TEMA_BTN}</script></body>')
    (base / "index.html").write_text(pagina("Schemi", idx), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
