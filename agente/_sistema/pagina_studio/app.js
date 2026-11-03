/* Quaderno di ripasso v3: logica e rendering. DATA arriva da data.json; GEN (gen.js) è inserito dalla build.
   Lo stato S (v:2: qs, th, hist, cards, exams, probs, ts + days, act) e lo scheduling restano quelli della v2. */
let DATA = null;
const LS_KEY = 'quaderno-ripasso-v2';
const newState = () => ({ v: 2, qs: {}, th: {}, hist: [], cards: {}, exams: {}, probs: {}, days: [], act: {} });
let S = newState();
const fixS = () => { if (!Array.isArray(S.days)) S.days = []; if (!S.act || typeof S.act !== 'object') S.act = {}; };
try {
  const x = JSON.parse(localStorage.getItem(LS_KEY) || 'null');
  if (x && x.v === 2) S = Object.assign(S, x);
  else { const old = JSON.parse(localStorage.getItem('quaderno-ripasso-v1') || 'null'); if (old) { S.hist = old.hist || []; S.exams = old.exams || {}; } }
} catch (e) {}
fixS();
let SERVER = false, saveT = null;
const ONLINE = !/^(127\.0\.0\.1|localhost)$/.test(location.hostname); // sito su Vercel (con login) o Quaderno locale (serve.py)
/* Sincronizzazione con il server. SYNC è l'ultimo stato concordato: a ogni salvataggio si mandano anche gli id
   cambiati da allora (dirty) e il ts di SYNC (base). Se nel frattempo un altro dispositivo ha salvato, il server
   unisce i due stati invece di sovrascrivere (prima il telefono rimasto aperto cancellava il lavoro fatto sul PC). */
const SEZ = ['qs', 'cards', 'probs', 'th', 'exams'];
let SYNC = null;
const clone = o => JSON.parse(JSON.stringify(o));
const keepLocal = () => { try { localStorage.setItem(LS_KEY, JSON.stringify(S)); } catch (e) {} };
function dirtyIds() {
  const d = {};
  for (const k of SEZ) {
    const a = S[k] || {}, b = (SYNC && SYNC[k]) || {};
    const ids = Object.keys(a).filter(i => JSON.stringify(a[i]) !== JSON.stringify(b[i])).concat(Object.keys(b).filter(i => !(i in a)));
    if (ids.length) d[k] = ids;
  }
  return d;
}
function adoptServer(x) { // stato del server dentro S, senza perdere ciò che è cambiato qui dopo l'ultima sincronizzazione
  const mine = dirtyIds(), loc = S;
  S = Object.assign(newState(), clone(x)); fixS();
  for (const k of Object.keys(mine)) for (const id of mine[k]) { if (id in (loc[k] || {})) S[k][id] = loc[k][id]; else delete S[k][id]; }
  const seen = new Set(S.hist.map(h => JSON.stringify(h)));
  (loc.hist || []).forEach(h => { if (!seen.has(JSON.stringify(h))) S.hist.push(h); });
  S.days = Array.from(new Set(S.days.concat(loc.days || []))).sort();
  for (const [g, n] of Object.entries(loc.act || {})) S.act[g] = Math.max(S.act[g] || 0, n);
  SYNC = clone(x); keepLocal();
  return Object.keys(mine).length > 0;
}
function push(atExit) {
  const body = JSON.stringify({ stato: S, base: SYNC ? (SYNC.ts || 0) : 0, dirty: dirtyIds() });
  const sent = clone(S);
  return fetch('api/stato', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body, keepalive: !!atExit && body.length < 60000 })
    .then(r => r.ok ? r.json() : null)
    .then(j => {
      if (!j) return;
      if (j.stato) { if (adoptServer(j.stato)) save(); return; }
      SYNC = sent;
      if (j.ts) { SYNC.ts = j.ts; if (S.ts === sent.ts) { S.ts = j.ts; keepLocal(); } }
    })
    .catch(() => {});
}
const save = () => {
  S.ts = Date.now();
  keepLocal();
  if (SERVER) { clearTimeout(saveT); saveT = setTimeout(() => { saveT = null; push(false); }, 400); }
};
async function loadServerState() { // online: progressi dell'account; in locale (serve.py) anche in _sistema/progressi.json
  try {
    const r = await fetch('api/stato'); if (!r.ok) return; SERVER = true; const x = await r.json();
    if (x && x.v === 2 && (x.ts || 0) > (S.ts || 0)) { S = Object.assign(newState(), x); fixS(); keepLocal(); SYNC = clone(x); }
    else { SYNC = x && x.v === 2 ? clone(x) : null; if (S.ts) save(); }
  } catch (e) {}
}
// tornando sull'app (telefono, altra scheda) si riprendono le novità degli altri dispositivi; uscendo si salva subito
document.addEventListener('visibilitychange', () => {
  if (!SERVER) return;
  if (document.visibilityState === 'hidden') { if (saveT) { clearTimeout(saveT); saveT = null; push(true); } return; }
  fetch('api/stato').then(r => r.ok ? r.json() : null).then(x => {
    if (x && x.v === 2 && (x.ts || 0) > ((SYNC && SYNC.ts) || 0)) { if (adoptServer(x)) save(); if (typeof refreshAfterSync === 'function') refreshAfterSync(); }
  }).catch(() => {});
});
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const pad = n => String(n).padStart(2, '0');
const isoLocal = d => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
const todayStr = () => isoLocal(new Date());
const parseD = s => { const [y, m, d] = s.split('-').map(Number); return new Date(y, m - 1, d, 12); };
const addDays = (s, n) => { const d = parseD(s); d.setDate(d.getDate() + n); return isoLocal(d); };
const daysTo = s => Math.round((parseD(s) - parseD(todayStr())) / 864e5);
const itDate = s => s.split('-').reverse().join('/');
const say = t => { const l = $('#live'); if (l) { l.textContent = ''; setTimeout(() => { l.textContent = t; }, 30); } };
const RM = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
const raf2 = f => requestAnimationFrame(() => requestAnimationFrame(f));
/* Mini convertitore LaTeX -> HTML/Unicode per i quiz (nessuna libreria, funziona offline).
   Converte solo i comandi noti; i backslash di altro tipo (percorsi Windows, "\n" in C) restano com'e'. */
const TEXSYM = {
  wedge: '∧', land: '∧', vee: '∨', lor: '∨', neg: '¬', lnot: '¬', to: '→', rightarrow: '→', Rightarrow: '⇒', Leftrightarrow: '⟺',
  leftrightarrow: '↔', implies: '⟹', iff: '⟺', forall: '∀', exists: '∃', in: '∈', notin: '∉', subseteq: '⊆', supseteq: '⊇', subset: '⊂',
  cap: '∩', cup: '∪', times: '×', cdot: '·', ldots: '…', dots: '…', lambda: 'λ', sigma: 'σ', alpha: 'α', beta: 'β', gamma: 'γ',
  delta: 'δ', epsilon: 'ε', varepsilon: 'ε', pi: 'π', omega: 'ω', theta: 'θ', mu: 'μ', emptyset: '∅', leq: '≤', le: '≤', geq: '≥',
  ge: '≥', neq: '≠', ne: '≠', sim: '∼', mid: '∣', therefore: '∴', quad: '  ', qquad: '    ', oplus: '⊕', equiv: '≡', infty: '∞',
  approx: '≈', circ: '∘', setminus: '∖', Sigma: 'Σ', Delta: 'Δ'
};
const TEXBB = { R: 'ℝ', N: 'ℕ', Z: 'ℤ', Q: 'ℚ', C: 'ℂ' };
const TEXCAL = { P: '𝒫', A: '𝒜', C: '𝒞', F: 'ℱ', L: 'ℒ' };
const TEXRE = /\\[(\[]|\\(?:overline|wedge|land|lor|vee|neg|lnot|to|rightarrow|Rightarrow|Leftrightarrow|leftrightarrow|implies|iff|forall|exists|subseteq|supseteq|cap|cup|times|cdot|ldots|lambda|sigma|mathbf|mathbb|mathcal|frac|therefore|emptyset|leq|geq|neq|mid|text|sim|oplus|equiv|setminus|circ)(?![a-zA-Z])/;
function texGroup(s, i) {
  while (s[i] === ' ') i++;
  if (s[i] === '{') {
    let d = 1, j = i + 1;
    while (j < s.length && d) { if (s[j] === '{') d++; else if (s[j] === '}') d--; j++; }
    return [s.slice(i + 1, d ? j : j - 1), j];
  }
  if (s[i] === '\\') { const m = /^\\[a-zA-Z]+/.exec(s.slice(i)); if (m) return [m[0], i + m[0].length]; }
  return [s[i] || '', i + 1];
}
function texConv(s) {
  let o = '', i = 0;
  while (i < s.length) {
    const c = s[i];
    if (c === '\\') {
      if ('()[]'.includes(s[i + 1] || 'x')) { i += 2; continue; }
      const m = /^\\([a-zA-Z]+)/.exec(s.slice(i));
      if (!m) { o += c; i++; continue; }
      const n = m[1]; i += m[0].length;
      if (n === 'overline') { const [g, j] = texGroup(s, i); i = j; o += '<span class="ov">' + texConv(g) + '</span>'; }
      else if (n === 'mathbf' || n === 'textbf') { const [g, j] = texGroup(s, i); i = j; o += '<b>' + texConv(g) + '</b>'; }
      else if (n === 'mathbb') { const [g, j] = texGroup(s, i); i = j; o += TEXBB[g] || texConv(g); }
      else if (n === 'mathcal') { const [g, j] = texGroup(s, i); i = j; o += TEXCAL[g] || texConv(g); }
      else if (n === 'text' || n === 'mathrm') { const [g, j] = texGroup(s, i); i = j; o += texConv(g); }
      else if (n === 'frac') { const [a, j1] = texGroup(s, i); const [b, j2] = texGroup(s, j1); i = j2; const wrap = t => (t.length > 1 ? '(' + t + ')' : t); o += wrap(texConv(a)) + '/' + wrap(texConv(b)); }
      else if (n === 'not') { const [g, j] = texGroup(s, i); const sym = { '\\in': '∉', '\\subseteq': '⊄', '\\supseteq': '⊉', '\\equiv': '≢' }[g]; if (sym) { i = j; o += sym; } else o += '¬'; }
      else if (n === 'bf') { /* dichiarazione di grassetto: ignorata */ }
      else if (TEXSYM[n]) o += TEXSYM[n];
      else o += '\\' + n;
    } else if ((c === '_' || c === '^') && s[i + 1] === '{') {
      const [g, j] = texGroup(s, i + 1); i = j; o += (c === '_' ? '<sub>' : '<sup>') + texConv(g) + (c === '_' ? '</sub>' : '</sup>');
    } else if (c === '_' && /[A-Za-z0-9]/.test(s[i + 1] || '') && /[A-Za-z)]/.test(s[i - 1] || '')) {
      o += '<sub>' + s[i + 1] + '</sub>'; i += 2;
    } else if (c === '{' || c === '}') { i++; }
    else { o += c; i++; }
  }
  return o;
}
const tex = s => TEXRE.test(s) ? texConv(s) : s;
const tx = s => tex(esc(s));

function inline(s) { return tex(esc(s)).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/`(.+?)`/g, '<code>$1</code>'); }
/* disegni delle domande (scaricati dal sito esami): cliccando si aprono a grandezza intera */
const figs = l => (l && l.length) ? '<div class="figs">' + l.map(s => `<a href="${esc(s)}" target="_blank" rel="noopener"><img src="${esc(s)}" alt="Disegno della domanda" loading="lazy"></a>`).join('') + '</div>' : '';
function fmt(t) {
  let h = '', ul = false;
  for (const l of String(t).split('\n')) {
    if (/^\s*[-•]\s/.test(l)) { if (!ul) { h += '<ul>'; ul = true; } h += '<li>' + inline(l.replace(/^\s*[-•]\s/, '')) + '</li>'; }
    else { if (ul) { h += '</ul>'; ul = false; } if (l.trim()) h += '<p>' + inline(l) + '</p>'; }
  }
  return h + (ul ? '</ul>' : '');
}

/* ---------- icone, anelli, conteggi, toast ---------- */
const IC = {
  check: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
  arrow: '<svg class="arr" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  cal: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>',
  chev: '<svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
  flame: '<svg class="flame ${on}" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5c.5 3-1.5 4.5-3 6.5-1.6 2.100-2.500 3.500-2.500 5.500a5.500 5.500 0 0 0 11 0c0-2-1-3.300-2-4.500-.4 1.200-1 1.800-1.800 2C14.500 8.800 13.500 5 12 2.500z"/></svg>',
  clock: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.500 2M9 2.500h6"/></svg>',
  eye: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12s3.600-7 10-7 10 7 10 7-3.600 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  turn: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h14M13 6l6 6-6 6"/></svg>',
  book: '<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="14" y="8" width="38" height="48" rx="5"/><path d="M22 20h22M22 29h22M22 38h12"/></svg>',
  target: '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="22"/><circle cx="32" cy="32" r="11"/><path d="M32 32l16-16"/></svg>',
  chart: '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M10 52h44M16 44V30M30 44V18M44 44V36"/></svg>',
  sun: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.500v2.500M12 19v2.500M2.500 12H5M19 12h2.500M5.300 5.300l1.800 1.800M16.900 16.900l1.800 1.800M5.300 18.700l1.800-1.800M16.900 7.100l1.800-1.800"/></svg>',
  moon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.500A8.500 8.500 0 1 1 9.500 4a7 7 0 0 0 10.500 10.500z"/></svg>',
  auto: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.500"/><path d="M12 3.500v17a8.500 8.500 0 0 0 0-17z" fill="currentColor" stroke="none"/></svg>'
};
function ring(pct, size, sw, o = {}) {
  const r = (size - sw) / 2, c = 2 * Math.PI * r, p = Math.max(0, Math.min(1, pct));
  const id = o.id ? ` id="${o.id}"` : '';
  return `<div class="ring ${o.cls || ''}" style="width:${size}px;height:${size}px" role="img" aria-label="${esc(o.label || '')}"><svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}"><circle class="trk" cx="${size / 2}" cy="${size / 2}" r="${r}" stroke-width="${sw}"/><circle class="bar"${id} cx="${size / 2}" cy="${size / 2}" r="${r}" stroke-width="${sw}" stroke-dasharray="${c}" stroke-dashoffset="${o.instant ? c * (1 - p) : c}" data-c="${c}" ${o.instant ? '' : `data-off="${c * (1 - p)}"`}/></svg><div class="ring-c">${o.center || ''}</div></div>`;
}
function animateRings(root) { raf2(() => $$('.ring .bar[data-off]', root).forEach(b => { b.style.strokeDashoffset = b.dataset.off; })); }
function countUp(el, to, dur = 800, fmtFn) {
  const f = fmtFn || (v => String(v));
  if (RM.matches || !to) { el.textContent = f(to); return; }
  const t0 = performance.now(); el.textContent = f(0);
  const step = t => { const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3); el.textContent = f(Math.round(to * e)); if (k < 1) requestAnimationFrame(step); };
  requestAnimationFrame(step);
}
function countAll(root) { $$('[data-count]', root).forEach(el => countUp(el, +el.dataset.count, 800, el.dataset.suffix ? v => v + el.dataset.suffix : undefined)); }
function toast(msg) {
  const box = $('#toasts'); if (!box) return;
  while (box.children.length > 2) box.firstChild.remove();
  const t = document.createElement('div'); t.className = 'toast'; t.innerHTML = IC.check + '<span>' + esc(msg) + '</span>'; box.appendChild(t);
  setTimeout(() => { t.classList.add('out'); setTimeout(() => t.remove(), 320); }, 2200);
}
const IO = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); IO.unobserve(e.target); } }), { threshold: 0.25 }) : null;
const reveal = el => { if (IO) IO.observe(el); else el.classList.add('in'); };
const stagger = el => { Array.from(el.children).forEach((c, i) => c.style.setProperty('--i', i)); };

/* ---------- tema ---------- */
const THEME_KEY = 'quaderno-tema';
const getTheme = () => { try { return localStorage.getItem(THEME_KEY) || 'auto'; } catch (e) { return 'auto'; } };
const THEME_NAME = { auto: 'automatico', light: 'chiaro', dark: 'scuro' }, THEME_NEXT = { auto: 'light', light: 'dark', dark: 'auto' };
function applyTheme(p, animate) {
  const h = document.documentElement;
  if (animate && !RM.matches) { h.classList.add('theme-fade'); setTimeout(() => h.classList.remove('theme-fade'), 450); }
  if (p === 'auto') h.removeAttribute('data-theme'); else h.setAttribute('data-theme', p);
  try { localStorage.setItem(THEME_KEY, p); } catch (e) {}
  $('#theme-ic').innerHTML = IC[p === 'light' ? 'sun' : (p === 'dark' ? 'moon' : 'auto')];
  $('#theme-btn').setAttribute('aria-label', 'Tema: ' + THEME_NAME[p] + '. Tocca per passare a ' + THEME_NAME[THEME_NEXT[p]]);
  $$('#th-ctl button').forEach(b => b.setAttribute('aria-checked', String(b.dataset.th === p)));
  setTimeout(() => { const m = document.querySelector('meta[name="theme-color"]'); if (m) m.content = getComputedStyle(h).getPropertyValue('--bg').trim() || '#f5efe0'; }, 60);
}
$('#theme-btn').addEventListener('click', () => applyTheme(THEME_NEXT[getTheme()], true));
$$('#th-ctl button').forEach(b => b.addEventListener('click', () => applyTheme(b.dataset.th, true)));
try { window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (getTheme() === 'auto') applyTheme('auto'); }); } catch (e) {}
applyTheme(getTheme());

/* ---------- attività, serie, obiettivo ---------- */
const GOAL = 20;
function mark() { // registra un'attività di studio di oggi (per serie e obiettivo giornaliero)
  const t = todayStr(); if (!S.days.includes(t)) { S.days.push(t); S.days = S.days.slice(-240); }
  S.act[t] = (S.act[t] || 0) + 1;
  const ks = Object.keys(S.act).sort(); if (ks.length > 70) ks.slice(0, ks.length - 70).forEach(k => delete S.act[k]);
}
const studyDays = () => new Set(S.days.concat(S.hist.map(h => h.date)));
function streak() { const set = studyDays(); let d = todayStr(); if (!set.has(d)) d = addDays(d, -1); let n = 0; while (set.has(d)) { n++; d = addDays(d, -1); } return n; }
function actOn(d) { if (S.act[d]) return S.act[d]; return S.hist.filter(h => h.date === d).reduce((a, h) => a + (h.n || 0), 0); }
const todayCount = () => actOn(todayStr());

/* ---------- temi, esami, scadenze ---------- */
const themeOf = tags => { for (const t of DATA.priorita) if (tags.some(a => DATA.tagTema[a] === t)) return t; return tags.length ? (DATA.tagTema[tags[0]] || 'Altro') : 'Altro'; };
const themeWeak = t => Math.min(3, S.th[t] || 0);
const weakThemes = () => Object.entries(S.th).filter(e => e[1] > 0.4).sort((a, b) => b[1] - a[1]);
const examOf = m => S.exams[m] || (DATA.esami || {})[m] || '';
function capInterval(days, mat) { // a ridosso dell'esame gli intervalli si accorciano
  const e = examOf(mat); if (!e) return days; const left = daysTo(e); if (left < 0) return days;
  return Math.max(1, Math.min(days, Math.floor(left / 3)));
}
function bumpTheme(theme, ok) { S.th[theme] = Math.max(0, (S.th[theme] || 0) + (ok ? -0.5 : 1)); }
function chapterHint(theme, mat) { // dove ripassare il tema: capitoli calcolati dalla build sui riassunti (temiCap)
  const m = mat || 'Matematica discreta';
  const t = ((DATA.temiCap || {})[m] || {})[theme];
  if (!t) return (m === 'Matematica discreta' && DATA.temi[theme]) ? '<p class="hint">Tema non ancora nei riassunti: arriva con le prossime lezioni.</p>' : '';
  const slug = typeof RSLUG !== 'undefined' ? RSLUG[m] : '';
  const link = slug ? ` <a href="riassunti/${slug}.html#cap${t.n}">Apri il cap. ${t.n} &rarr;</a>` : '';
  return `<p class="hint">Rivedi: ${esc(m)}, ${esc(t.cap)} del riassunto.${link}</p>`;
}
const subjIdx = m => Math.max(0, Object.keys(DATA.materie).indexOf(m));

/* ---------- navigazione ---------- */
const TABS = ['oggi', 'quiz', 'problemi', 'schede'];
let current = 'oggi', pending = null;
function moveInd(instant) {
  const b = $('#t-' + current), ind = $('#seg-ind'); if (!b || !b.offsetWidth) return;
  if (instant) ind.style.transition = 'none';
  ind.style.width = b.offsetWidth + 'px'; ind.style.transform = `translateX(${b.offsetLeft}px)`;
  if (instant) { void ind.offsetWidth; ind.style.transition = ''; }
}
function showTab(name) {
  if (!TABS.includes(name)) name = 'oggi';
  const changed = name !== current;
  current = name;
  $$('.tab, .bn').forEach(b => { const on = b.dataset.tab === name; b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1; });
  moveInd(!DATA);
  try { localStorage.setItem('quaderno-tab', name); history.replaceState(null, '', '#' + name); } catch (e) {}
  if (!DATA) { pending = name; return; }
  TABS.forEach(t => {
    const sec = $('#tab-' + t), on = t === name, wasHidden = sec.hidden;
    sec.hidden = !on;
    if (on && wasHidden) { sec.classList.remove('enter'); void sec.offsetWidth; stagger(sec); const bn = $('#bento'); if (bn && t === 'oggi') stagger(bn); sec.classList.add('enter'); }
  });
  if (changed) window.scrollTo({ top: 0, behavior: 'auto' });
  if (name === 'oggi') renderOggi();
  if (name === 'quiz') setupQuiz();
  if (name === 'problemi') renderProbSetup();
  if (name === 'schede') renderCardSetup();
}
$$('.tab, .bn').forEach(b => {
  b.addEventListener('click', () => showTab(b.dataset.tab));
  b.addEventListener('keydown', e => {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    const i = TABS.indexOf(b.dataset.tab), n = TABS[(i + (e.key === 'ArrowRight' ? 1 : TABS.length - 1)) % TABS.length];
    showTab(n); const t = $(b.classList.contains('bn') ? `.bn[data-tab="${n}"]` : '#t-' + n); if (t) t.focus(); e.preventDefault();
  });
});
$('.brand').addEventListener('click', e => { e.preventDefault(); showTab('oggi'); });
window.addEventListener('resize', () => moveInd(true));
if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => moveInd(true));

/* ---------- Oggi ---------- */
const dueCards = (mat) => DATA.cards.filter(c => (!mat || mat === '*' || c.m === mat) && isDue(c));
let PLAN_INIT = false;
function renderOggi() {
  renderHero(); renderExams(); renderMaterie(); renderFreq(); renderDeboli(); renderStorico();
  if (DATA.piano) {
    const pc = $('#piano-card'); pc.hidden = false; $('#piano').innerHTML = fmt(DATA.piano);
    if (!PLAN_INIT) { PLAN_INIT = true; pc.open = window.matchMedia('(min-width: 960px)').matches; }
  }
}
function greeting() { const h = new Date().getHours(); return h < 5 ? 'Buonanotte' : (h < 13 ? 'Buongiorno' : (h < 18 ? 'Buon pomeriggio' : 'Buonasera')); }
function renderHero() {
  const nc = dueCards('*').length, nq = DATA.quiz.filter(q => { const s = S.qs[q.id]; return s && s.due <= todayStr(); }).length;
  const mm = Object.values(DATA.materie), done = mm.reduce((s, x) => s + x.studiati, 0), allc = mm.reduce((s, x) => s + x.capitoli, 0), pct = allc ? done / allc : 0, perc = Math.round(100 * pct), wk = weakThemes();
  const dl = new Date().toLocaleDateString('it-IT', { weekday: 'long', day: 'numeric', month: 'long' });
  const note = (nc + nq === 0 ? 'Niente in scadenza: la sessione ti propone domande nuove ed esercizi generati.' : 'Circa 20 minuti: prima le schede in scadenza, poi domande scelte tra i tuoi punti deboli e il peso all\'esame, poi qualche esercizio nuovo.');
  $('#sessione-card').innerHTML = `
    <div class="greet"><span class="hand">${greeting()} Emanuele</span><span class="date">${esc(dl)}</span></div>
    <div class="hero-main">
      ${ring(pct, 150, 12, { cls: perc >= 100 ? 'ok' : '', label: `Capitoli studiati in totale: ${done} su ${allc}, ${perc}%`, center: `<b data-count="${perc}" data-suffix="%">0%</b><span>${done} di ${allc}<br>capitoli studiati</span>` })}
      <div class="stats">
        <div class="stat"><span class="v mono" data-count="${nc}">0</span><span class="k">schede da ripassare</span></div>
        <div class="stat"><span class="v mono" data-count="${nq}">0</span><span class="k">domande da rivedere</span></div>
        ${wk.length ? `<div class="stat wide"><span class="k">Punto debole</span><span class="v">${esc(wk[0][0])}</span></div>` : ''}
      </div>
    </div>
    <div class="hero-act"><button class="btn xl" id="go-session">Inizia la sessione ${IC.arrow}</button><button class="btn ghost" id="go-5">Solo 5 minuti</button></div>
    <p class="hero-note">${note}</p>`;
  $('#go-session').addEventListener('click', () => startSession());
  $('#go-5').addEventListener('click', () => startSession(true));
  animateRings($('#sessione-card')); countAll($('#sessione-card'));
}
function renderStreak() {
  const n = streak(), set = studyDays(), today = todayStr();
  const now = parseD(today), dow = (now.getDay() + 6) % 7, start = addDays(today, -(dow + 28));
  let cells = '';
  for (let k = 0; k < 35; k++) {
    const d = addDays(start, k), fut = d > today, c = actOn(d), has = set.has(d);
    const l = fut ? 'fut' : (!has ? '' : (c >= 20 ? 'l4' : (c >= 12 ? 'l3' : (c >= 5 ? 'l2' : 'l1'))));
    const dt = parseD(d).toLocaleDateString('it-IT', { day: 'numeric', month: 'short' });
    cells += `<i class="${l} ${d === today ? 'today' : ''}" style="--k:${k}" title="${dt}: ${c || (has ? 1 : 0)} attività"></i>`;
  }
  const msg = n === 0 ? 'Inizia oggi: basta una scheda.' : (n < 3 ? 'Bella partenza, non spezzarla.' : (n < 7 ? 'Il ritmo si sta formando.' : 'Che costanza. Continua così.'));
  $('#serie-card').innerHTML = `<div class="streak-top">${IC.flame.replace('${on}', n ? 'on' : '')}<div><div class="streak-n mono" data-count="${n}">0</div><div class="streak-l">${n === 1 ? 'giorno di fila' : 'giorni di fila'}</div></div></div>
    <div class="heat-wrap" role="img" aria-label="Attività delle ultime cinque settimane: ${n} giorni di studio consecutivi"><div class="heat-days" aria-hidden="true"><span>L</span><span>M</span><span>M</span><span>G</span><span>V</span><span>S</span><span>D</span></div><div class="heat">${cells}</div></div>
    <p class="streak-note">${msg}</p>`;
  countAll($('#serie-card'));
}
function renderExams() {
  const mats = Object.keys(DATA.materie);
  $('#exams').innerHTML = mats.map((m, i) => {
    const d = examOf(m);
    if (!d) return `<button class="exam empty-d" data-m="${esc(m)}" style="--c:var(--s${i % 4})" aria-label="${esc(m)}: imposta la data d'esame"><span class="nm">${esc(m)}</span><span class="cd">${IC.cal}Imposta data</span></button>`;
    const left = daysTo(d);
    const cls = left < 0 ? '' : (left <= 14 ? 'soon' : (left <= 30 ? 'mid' : ''));
    const body = left >= 0 ? `<span class="cd"><b data-count="${left}">0</b><span>${left === 1 ? 'giorno' : 'giorni'}</span></span>` : '<span class="cd"><span class="pill bad">data passata</span></span>';
    return `<button class="exam ${cls}" data-m="${esc(m)}" style="--c:var(--s${i % 4})" aria-label="${esc(m)}: esame il ${itDate(d)}${left >= 0 ? ', tra ' + left + ' giorni' : ', data passata'}. Cambia data"><span class="nm">${esc(m)}</span>${body}<span class="dt">${itDate(d)}</span></button>`;
  }).join('');
  $$('#exams .exam').forEach(b => b.addEventListener('click', () => openDate(b.dataset.m)));
  countAll($('#exams'));
}
let dateFor = null;
function openDate(m) {
  dateFor = m; const dlg = $('#dlg-date'); dlg.returnValue = '';
  $('#date-sub').textContent = m + ': quando la inserisci, gli intervalli di ripasso si accorciano per arrivare pronto in tempo.';
  $('#date-in').value = examOf(m) || ''; dlg.showModal();
}
$('#date-form').addEventListener('submit', e => { // il pulsante Salva ha value="ok"; X ed Esc chiudono senza salvare
  if (!e.submitter || e.submitter.value !== 'ok' || !dateFor) return;
  const v = $('#date-in').value; S.exams[dateFor] = v; save(); renderExams(); renderHero(); toast(v ? 'Data d’esame salvata' : 'Data rimossa');
});
$('#date-clear').addEventListener('click', () => { if (dateFor) { S.exams[dateFor] = ''; save(); renderExams(); renderHero(); toast('Data rimossa'); } $('#dlg-date').close(); });
function renderMaterie() {
  const mats = Object.keys(DATA.materie); const openSet = new Set($$('#materie .subj.open').map(e => e.dataset.m));
  $('#materie').innerHTML = mats.map((m, i) => {
    const x = DATA.materie[m], pct = x.capitoli ? x.studiati / x.capitoli : 0, p = Math.round(100 * pct);
    const sq = (x.elenco || []).map((c, k) => `<button class="sq s${c.s}" style="--k:${k}" data-t="${esc(c.t)}" data-n="${c.n}" data-s="${c.s}" title="Cap. ${c.n}: ${esc(c.t)}" aria-label="Capitolo ${c.n}, ${c.s === 2 ? 'studiato' : (c.s === 1 ? 'studiato in parte' : 'da studiare')}: ${esc(c.t)}">${c.s === 2 ? '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.500l4.500 4.500L19 7.500"/></svg>' : c.n}</button>`).join('');
    const lst = (x.elenco || []).map(c => `<li class="s${c.s}"><i></i><span>${c.n}. ${esc(c.t)}</span></li>`).join('');
    return `<article class="subj ${openSet.has(m) ? 'open' : ''}" data-m="${esc(m)}" style="--c:var(--s${i % 4})">
      <button class="subj-head" aria-expanded="${openSet.has(m)}">${ring(pct, 56, 6, { cls: 'sm' + (pct >= 1 ? ' ok' : ''), label: p + '% studiato', center: `<b>${p}%</b>` })}<span><span class="nm">${esc(m)}</span><br><span class="sub">${x.studiati} di ${x.capitoli} capitoli studiati</span></span>${IC.chev}</button>
      <div class="squares" role="group" aria-label="Capitoli: verde studiato, arancio in parte">${sq}</div>
      <div class="sq-label" aria-live="polite">Tocca un quadratino per vedere il capitolo.</div>
      <div class="fold subj-more ${openSet.has(m) ? 'open' : ''}"><div class="fold-in"><div class="meta"><span><strong>Lezioni nei riassunti:</strong> ${esc(x.lezioni)}</span><span>${esc(x.prossimo)}</span></div><ol>${lst}</ol></div></div>
    </article>`;
  }).join('');
  $$('#materie .subj').forEach(card => {
    $('.subj-head', card).addEventListener('click', e => { const o = card.classList.toggle('open'); $('.fold', card).classList.toggle('open', o); e.currentTarget.setAttribute('aria-expanded', String(o)); });
    $$('.sq', card).forEach(b => b.addEventListener('click', () => {
      $$('.sq.on', card).forEach(s => s.classList.remove('on')); b.classList.add('on');
      const st = { 2: 'studiato', 1: 'in parte', 0: 'da studiare' }[b.dataset.s];
      $('.sq-label', card).innerHTML = `<b>Cap. ${b.dataset.n}</b> · ${esc(b.dataset.t)} · ${st}`;
    }));
  });
  animateRings($('#materie'));
}
function renderFreq() {
  const w = f => f[1] / 150 + f[2] / 30, max = Math.max(...DATA.freq.map(w));
  $('#freq').innerHTML = DATA.freq.slice().sort((a, b) => w(b) - w(a)).map((f, k) => {
    const p = Math.round(100 * w(f) / max);
    return `<div class="fr" style="--w:${p / 100};--k:${k}"><span class="nm">${esc(f[0])}</span><span class="pill ${f[3] ? 'good' : 'warn'}">${f[3] ? 'nei riassunti' : 'non ancora'}</span><div class="meter" role="img" aria-label="peso ${p}%"><i></i></div><span class="nums">quiz ${f[1]}/150 · problemi ${f[2]}/30</span></div>`;
  }).join('');
  $$('#freq .fr').forEach(reveal);
}
function renderDeboli() {
  const weak = weakThemes().slice(0, 6);
  $('#deboli').innerHTML = weak.length ? '<ul class="weak-list">' + weak.map(([k, v]) => `<li><span class="nm">${esc(k)}</span><span class="dots" role="img" aria-label="livello ${Math.min(3, Math.ceil(v))} su 3">${[1, 2, 3].map(i => `<i class="${v >= i - 0.5 ? 'on' : ''}"></i>`).join('')}</span><button class="btn ghost small" data-tr="${esc(k)}">Allena</button></li>`).join('') + '</ul>'
    : `<div class="empty">${IC.target}<p>Nessun errore registrato: ottimo inizio. Fai un quiz o un problema e qui compaiono i temi da rivedere.</p><button class="btn ghost small" id="weak-go">Fai un quiz</button></div>`;
  $$('[data-tr]').forEach(b => b.addEventListener('click', () => { showTab('quiz'); startQuiz(false, { topic: b.dataset.tr, n: 10, mode: '1' }); }));
  const g = $('#weak-go'); if (g) g.addEventListener('click', () => showTab('quiz'));
}
function sparkline(vals) {
  const W = 300, H = 64, n = vals.length, px = i => n === 1 ? W / 2 : 8 + i * (W - 16) / (n - 1), py = v => H - 8 - v * (H - 16);
  const pts = vals.map((v, i) => [px(i), py(v)]);
  const d = pts.map((p, i) => (i ? 'L' : 'M') + p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' ');
  const area = n > 1 ? d + ` L${pts[n - 1][0].toFixed(1)} ${H} L${pts[0][0].toFixed(1)} ${H} Z` : '';
  return `<svg class="spark" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" role="img" aria-label="Andamento delle ultime ${n} prove: ${vals.map(v => Math.round(v * 100) + '%').join(', ')}"><line class="gl" x1="0" x2="${W}" y1="${py(0.6)}" y2="${py(0.6)}"/>${area ? `<path class="ar" d="${area}"/>` : ''}${n > 1 ? `<path class="ln" pathLength="1" d="${d}"/>` : ''}${pts.map((p, i) => `<circle style="--k:${i}" cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="4"/>`).join('')}</svg>`;
}
function renderStorico() {
  const h = S.hist.slice(-12);
  $('#storico').innerHTML = h.length ? sparkline(h.map(x => x.n ? x.score / x.n : 0)) + '<ul class="hist-list">' + h.slice(-5).reverse().map(x => { const r = x.n ? x.score / x.n : 0; return `<li><span class="score ${r >= 0.8 ? 'g' : (r >= 0.5 ? 'o' : 'r')}">${x.score}/${x.n}</span><span>${esc(x.topic)}</span><span class="muted mono">${itDate(x.date)}</span></li>`; }).join('') + '</ul>'
    : `<div class="empty">${IC.chart}<p>Ancora nessuna prova su questo dispositivo. Dopo il primo quiz vedrai qui l'andamento.</p></div>`;
}

/* ---------- Quiz ---------- */
let Q = null, timer = null;
const MATS = ['Matematica discreta', 'Algebra lineare', 'Fondamenti Info', 'Programmazione'];
const SIM = { 'Matematica discreta': { n: 10, min: 30 }, 'Algebra lineare': { n: 10, min: 30 }, 'Fondamenti Info': { n: 9, min: 45 }, 'Programmazione': { n: 10, min: 30 } };
let QM = (() => { try { const m = localStorage.getItem('quaderno-qmat'); return MATS.includes(m) ? m : MATS[0]; } catch (e) { return MATS[0]; } })();
const quizPool = () => DATA.quiz.filter(q => q.m === QM);
const poolWeak = () => { const th = new Set(quizPool().map(q => q.theme)); return weakThemes().filter(e => th.has(e[0])); };
const cov = m => new Set((DATA.coperti || {})[m] || []);
const canGen = () => GEN.disponibile(QM, cov(QM));
let QT = new Set();
function setupQuiz() {
  if (!MATS.includes(QM)) QM = MATS[0];
  const pool = quizPool(), counts = {}; pool.forEach(q => counts[q.theme] = (counts[q.theme] || 0) + 1);
  $('#mat-pick').innerHTML = MATS.map((m, i) => { const n = DATA.quiz.filter(q => q.m === m).length; return `<button type="button" class="mp" role="radio" aria-checked="${m === QM}" data-m="${esc(m)}" style="--c:var(--s${i})"><span class="mp-n">${esc(m)}</span><span class="mp-c">${n} domande${GEN.disponibile(m, cov(m)) ? ' · + esercizi generati' : ''}</span></button>`; }).join('');
  $$('#mat-pick .mp').forEach(b => b.addEventListener('click', () => { QM = b.dataset.m; try { localStorage.setItem('quaderno-qmat', QM); } catch (e) {} setupQuiz(); }));
  const valid = new Set(['__gen__', ...Object.keys(counts)]); QT = new Set([...QT].filter(k => valid.has(k)));
  const chip = (v, t) => `<button type="button" class="tchip" data-v="${esc(v)}" aria-pressed="false">${esc(t)}</button>`;
  $('#q-topic').innerHTML = chip('', 'Tutti i temi (' + pool.length + ')') + (canGen() ? chip('__gen__', 'Esercizi generati') : '') + Object.keys(counts).sort().map(a => chip(a, `${a} (${counts[a]})`)).join('');
  const paint = () => $$('#q-topic .tchip').forEach(c => c.setAttribute('aria-pressed', String(c.dataset.v === '' ? QT.size === 0 : QT.has(c.dataset.v))));
  $$('#q-topic .tchip').forEach(c => c.addEventListener('click', () => { const v = c.dataset.v; if (v === '') QT.clear(); else if (QT.has(v)) QT.delete(v); else QT.add(v); paint(); }));
  paint();
  const w = poolWeak().length;
  $('#q-weak').hidden = !w;
  $('#pr-weak').disabled = !w;
  $('#pr-weak-s').textContent = w ? `Solo i temi dove sbagli (${w})` : 'Ancora nessun errore in questa materia';
  const nasc = (DATA.nascoste || {})[QM] || {}, nn = Object.values(nasc).reduce((x, y) => x + y, 0);
  $('#q-hidden').textContent = nn ? `Mostro solo gli argomenti già trattati nei riassunti. Non ancora disponibili: ${nn} domande su ${Object.keys(nasc).join(', ')} (compaiono da sole quando il Word le copre).` : 'Tutti gli argomenti presenti nel Word sono coperti.';
  const sm = SIM[QM]; $('#pr-exam-s').textContent = `${sm.n} domande a tempo, ${sm.min} minuti`;
  $('#pr-gen').disabled = !canGen(); $('#pr-gen-s').textContent = canGen() ? '10 nuovi, mai gli stessi' : 'Non ancora disponibili per questa materia';
  $('#pr-fast').disabled = !pool.length;
  $('#q-sub').textContent = pool.length ? `${QM}: ${pool.length} domande${pool.some(q => /^20\d\d-|^2[345]\d\d-/.test(q.id)) ? ' dalle prove 2024-2026 a 5 risposte' : ''}${canGen() ? ', più esercizi generati senza limite e verificati col computer' : ''}. Le soluzioni ufficiali in PDF hanno qualche errore: dove l'ho trovato lo segnalo.` : `${QM}: nessuna domanda disponibile.`;
  $('#q-min-l').hidden = $('#q-mode').value !== 'sim';
}
$('#q-mode').addEventListener('change', () => { $('#q-min-l').hidden = $('#q-mode').value !== 'sim'; });
$('#pr-fast').addEventListener('click', () => startQuiz(false, { topic: '', n: 5, mode: '1' }));
$('#pr-exam').addEventListener('click', () => startQuiz(false, { topic: '', n: SIM[QM].n, mode: 'sim', min: SIM[QM].min }));
$('#pr-weak').addEventListener('click', () => startQuiz(true, { n: 10, mode: '1' }));
$('#pr-gen').addEventListener('click', () => startQuiz(false, { topic: '__gen__', n: 10, mode: '1' }));
const NOSHUF = /nessun|precedent|tutte le|entrambe|nessuna/i;
function prepare(q) { // mescola le opzioni (tranne "nessuna delle precedenti") così non si impara la posizione
  if (q.gen || q.o.some(o => NOSHUF.test(o)) || /opzion|risposta [1-5]/i.test(q.q)) return Object.assign({}, q);
  const idx = shuffle([...q.o.keys()]);
  return Object.assign({}, q, { o: idx.map(i => q.o[i]), a: idx.indexOf(q.a - 1) + 1 });
}
function pickQuiz(n, { theme, weak, ignoreDue } = {}) {
  let pool = quizPool();
  if (weak) { const w = poolWeak().map(e => e[0]); pool = pool.filter(q => w.includes(q.theme)); }
  else if (theme && theme.length) { const ts = [].concat(theme); pool = pool.filter(q => ts.includes(q.theme)); }
  const today = todayStr();
  const scored = pool.map(q => {
    const s = S.qs[q.id]; let sc = s ? (s.due <= today ? 3 + Math.min(s.wrong || 0, 3) * 0.3 : -1) : 1.5;
    if (ignoreDue) sc = s && s.due > today ? 0 : 1;
    sc += themeWeak(q.theme) * 0.8 + (DATA.pesi[q.theme] ?? 0.4) * 1.2 + Math.random();
    return [sc, q];
  }).sort((a, b) => b[0] - a[0]);
  return scored.slice(0, n).map(x => x[1]);
}
function startQuiz(weak, opts = {}) {
  const raw = opts.topic !== undefined ? opts.topic : [...QT], topics = [].concat(raw).filter(Boolean), gen = topics.includes('__gen__'), themes = topics.filter(t => t !== '__gen__');
  const mode = opts.mode !== undefined ? opts.mode : $('#q-mode').value, n = opts.n || +$('#q-n').value;
  let list, label = themes.length ? themes.join(' + ') : 'tutti i temi';
  if (!opts.list) label = QM + ' · ' + (gen && !themes.length ? 'esercizi generati' : (weak ? 'punti deboli' : (gen ? label + ' + esercizi generati' : label)));
  if (opts.list) { list = opts.list; label = opts.label || label; }
  else if (gen && !themes.length) { list = GEN.many(n, QM, cov(QM)); }
  else if (weak) { list = pickQuiz(n, { weak: true }); }
  else if (gen) { const g = Math.ceil(n / 2); list = pickQuiz(n - g, { theme: themes, ignoreDue: mode === 'sim' }).concat(GEN.many(g, QM, cov(QM))); }
  else list = pickQuiz(n, { theme: themes, ignoreDue: mode === 'sim' });
  if (!list.length) { toast('Nessuna domanda disponibile per questa scelta'); return; }
  const sim = !opts.list && mode === 'sim';
  Q = { list: list.map(prepare), i: 0, score: 0, wrong: [], fb: opts.fb !== undefined ? opts.fb : (!sim && mode === '1'), label: sim ? 'simulazione · ' + label : label, t0: Date.now(), answered: false, sim, limit: sim ? (opts.min || +$('#q-min').value) * 60 : 0, onEnd: opts.onEnd || null };
  $('#quiz-setup').hidden = true; $('#quiz-run').hidden = false;
  quizFrame(); clearInterval(timer); timer = setInterval(tick, 1000);
  renderQ();
  window.scrollTo({ top: 0, behavior: 'auto' });
}
function quizFrame() {
  const n = Q.list.length;
  const timerHtml = Q.sim ? ring(1, 54, 5, { id: 'q-tbar', instant: true, label: 'Tempo rimasto', center: '<b id="q-time">00:00</b>' }) : `${IC.clock}<span class="tl" id="q-time">00:00</span>`;
  $('#quiz-run').innerHTML = `<div class="card qcard"><div class="prog" role="progressbar" aria-label="Avanzamento del quiz" aria-valuemin="0" aria-valuemax="${n}" aria-valuenow="0" id="q-progbox"><i id="q-prog"></i></div>
    <div class="q-in"><div class="q-top"><div class="q-meta"><span class="q-count" id="q-count"></span><span class="q-src" id="q-src"></span></div><div class="timer" id="q-timer" role="timer" aria-label="${Q.sim ? 'Tempo rimasto' : 'Tempo trascorso'}">${timerHtml}</div></div>
    <div id="qbody"></div><div id="q-fbk"></div>
    <div class="q-actions"><button class="btn" id="q-next" disabled>Avanti ${IC.arrow}</button>${Q.sim ? '<button class="btn ghost" id="q-stop">Consegna ora</button>' : ''}<span class="grow"></span><span class="q-keys"><span class="kbd">1</span>–<span class="kbd">${Math.max(...Q.list.map(q => q.o.length))}</span> rispondi · <span class="kbd">Invio</span> avanti</span><button class="btn ghost small" id="q-exit">Esci</button></div></div></div>`;
  $('#q-next').addEventListener('click', nextQ);
  if ($('#q-stop')) $('#q-stop').addEventListener('click', endQuiz);
  $('#q-exit').addEventListener('click', abortQuiz);
}
function abortQuiz() {
  if (!Q) return; clearInterval(timer); Q = null; setPhase(0);
  $('#quiz-run').hidden = true; $('#quiz-setup').hidden = false; setupQuiz();
}
function tick() {
  const el = $('#q-time'); if (!el || !Q) return; const s = Math.floor((Date.now() - Q.t0) / 1000);
  if (Q.sim) {
    const left = Q.limit - s; if (left <= 0) { endQuiz(); return; }
    el.textContent = pad(Math.floor(left / 60)) + ':' + pad(left % 60); $('#q-timer').classList.toggle('low', left < 120);
    const b = $('#q-tbar'); if (b) b.style.strokeDashoffset = (+b.dataset.c) * (1 - left / Q.limit);
  } else el.textContent = pad(Math.floor(s / 60)) + ':' + pad(s % 60);
}
function renderQ() {
  const q = Q.list[Q.i], n = Q.list.length; Q.answered = false;
  $('#q-count').textContent = `Domanda ${Q.i + 1} di ${n}`; $('#q-src').textContent = `${q.prova} · ${q.theme}`;
  $('#q-prog').style.setProperty('--p', (Q.i / n).toFixed(3)); $('#q-progbox').setAttribute('aria-valuenow', Q.i);
  $('#qbody').innerHTML = `<div class="q-slide"><div class="q-text">${fmt(q.q)}</div>${figs(q.img)}<div class="opts" role="group" aria-label="Risposte">${q.o.map((o, k) => `<button class="opt" data-k="${k + 1}"><span class="n">${k + 1}</span><span>${tx(o)}</span></button>`).join('')}</div></div>`;
  $('#q-fbk').innerHTML = '';
  $$('.opt').forEach(b => b.addEventListener('click', () => answer(+b.dataset.k)));
  const nx = $('#q-next'); nx.disabled = true; nx.innerHTML = (Q.i + 1 === n ? 'Vedi il risultato' : 'Avanti') + ' ' + IC.arrow;
  tick();
  const r = $('#quiz-run').getBoundingClientRect(); if (r.top < 0) window.scrollBy({ top: r.top - 80, behavior: RM.matches ? 'auto' : 'smooth' });
}
function nextQ() { if (!Q.answered) return; Q.i++; Q.i < Q.list.length ? renderQ() : endQuiz(); }
function answer(k) {
  if (!Q || Q.answered) return; Q.answered = true; const q = Q.list[Q.i]; const ok = k === q.a;
  if (ok) Q.score++; else Q.wrong.push(q);
  bumpTheme(q.theme, ok);
  if (!q.gen) { const s = S.qs[q.id] || { box: 0, wrong: 0 }; if (ok) { s.box = Math.min(s.box + 1, 4); s.due = addDays(todayStr(), capInterval([1, 3, 7, 14, 30][s.box], q.m)); } else { s.box = 0; s.wrong = (s.wrong || 0) + 1; s.due = todayStr(); } S.qs[q.id] = s; }
  mark(); save();
  $('#q-prog').style.setProperty('--p', ((Q.i + 1) / Q.list.length).toFixed(3));
  $('.opts').classList.add('answered');
  $$('.opt').forEach(b => { b.disabled = true; const n = +b.dataset.k; if (Q.fb) { if (n === q.a) b.classList.add('ok'); else if (n === k) b.classList.add('ko'); } else if (n === k) b.classList.add('sel'); });
  if (Q.fb) {
    $('#q-fbk').innerHTML = `<div class="fold" id="fold"><div class="fold-in"><div class="explain" style="display:grid;gap:10px;padding-top:2px"><div class="note ${ok ? 'ok' : 'bad'}"><strong>${ok ? 'Giusto.' : 'Sbagliato: la risposta è la ' + q.a + '.'}</strong> ${tx(q.s)}${figs(q.imgf)}${ok ? '' : chapterHint(q.theme, q.m)}</div>${q.w ? `<div class="note warn"><strong>Attenzione, possibile errore nella soluzione ufficiale:</strong> ${tx(q.w)}</div>` : ''}</div></div></div>`;
    raf2(() => { const f = $('#fold'); if (f) f.classList.add('open'); });
    say(ok ? 'Giusto' : 'Sbagliato, la risposta è la ' + q.a);
  } else say('Risposta registrata');
  const nx = $('#q-next'); nx.disabled = false; nx.focus({ preventScroll: true });
}
const MSG = [[100, 'Perfetto: nemmeno un errore.'], [80, 'Ottimo lavoro, sei in forma.'], [60, 'Buon risultato: restano pochi dettagli.'], [40, 'Si può migliorare: guarda gli errori qui sotto.'], [0, 'Si riparte da qui: ogni errore è un indizio.']];
function endQuiz() {
  if (!Q) return; clearInterval(timer);
  const n = Q.list.length, answered = Q.i + (Q.answered ? 1 : 0), s = Math.floor((Date.now() - Q.t0) / 1000);
  if (Q.sim && answered < n) Q.list.slice(answered).forEach(q => { Q.wrong.push(q); bumpTheme(q.theme, false); });
  S.hist.push({ date: todayStr(), score: Q.score, n, topic: Q.label }); S.hist = S.hist.slice(-30); mark(); save();
  const done = Q.onEnd; const q0 = Q; Q = null;
  const pct = n ? Math.round(100 * q0.score / n) : 0, msg = MSG.find(m => pct >= m[0])[1];
  $('#quiz-run').innerHTML = `<div class="card result" aria-live="polite">${pct >= 80 ? '<span class="stamp" aria-hidden="true">Ottimo!</span>' : ''}
    ${ring(pct / 100, 176, 14, { cls: pct >= 80 ? 'ok' : (pct < 40 ? 'low' : ''), label: `Punteggio ${q0.score} su ${n}, ${pct}%`, center: `<b id="res-score">0/${n}</b><span>${pct}%</span>` })}
    <p class="res-msg">${msg}</p>
    <p class="res-sub">in ${Math.floor(s / 60)} min ${s % 60} s · ${esc(q0.label)}${q0.sim && answered < n ? ' · ' + (n - answered) + ' senza risposta' : ''}</p>
    <div class="res-actions">${q0.wrong.length && !done ? '<button class="btn soft" id="q-redo">Rifai solo gli errori</button>' : ''}<button class="btn" id="q-again">${done ? 'Concludi la sessione' : 'Un altro quiz'}</button></div>
    ${q0.wrong.length ? '<div class="review"><h3>Da rivedere</h3>' + q0.wrong.map(q => `<details class="rev"><summary><span>${tx(String(q.q).split('\n')[0])}</span></summary><div class="rev-in"><div class="q-text" style="font-size:1rem">${fmt(q.q)}</div>${figs(q.img)}<div class="note ok"><strong>Risposta ${q.a}:</strong> ${esc(q.o[q.a - 1])}</div><p>${esc(q.s)}</p>${figs(q.imgf)}${chapterHint(q.theme, q.m)}${q.w ? '<p><em>Possibile errore nella soluzione ufficiale: ' + esc(q.w) + '</em></p>' : ''}</div></details>`).join('') + '</div>' : '<p class="res-sub">Nessun errore da rivedere.</p>'}</div>`;
  animateRings($('#quiz-run')); countUp($('#res-score'), q0.score, 900, v => v + '/' + n);
  $('#q-again').addEventListener('click', () => { $('#quiz-run').hidden = true; $('#quiz-setup').hidden = false; setupQuiz(); if (done) done(); });
  const rd = $('#q-redo'); if (rd) rd.addEventListener('click', () => startQuiz(false, { list: q0.wrong.slice(), label: 'errori da rifare', fb: true }));
  $('#q-again').focus({ preventScroll: true }); window.scrollTo({ top: 0, behavior: 'auto' });
}
$('#q-start').addEventListener('click', () => startQuiz(false));
$('#q-weak').addEventListener('click', () => startQuiz(true));

/* ---------- Problemi ---------- */
let P = null;
function renderProbSetup() {
  const cur = $('#p-topic').value, th = [...new Set(DATA.problemi.map(p => p.theme))].sort();
  $('#p-topic').innerHTML = '<option value="">Tutti i temi</option>' + th.map(t => `<option>${esc(t)}</option>`).join(''); if (cur) $('#p-topic').value = cur;
  const pool = probPool(); $('#p-count').textContent = `${pool.filter(p => !S.probs[p.id]).length} mai svolti su ${pool.length}`;
}
$('#p-topic').addEventListener('change', renderProbSetup);
const probPool = () => DATA.problemi.filter(p => !$('#p-topic').value || p.theme === $('#p-topic').value);
function pickProblem() {
  const sc = probPool().map(p => { const s = S.probs[p.id]; let v = !s ? 2 : (s.r === 0 ? 3 : (s.r === 1 ? 1 : -0.5)); v += themeWeak(p.theme) * 0.6 + (DATA.pesi[p.theme] || 0) + Math.random(); return [v, p]; }).sort((a, b) => b[0] - a[0]);
  return sc.length ? sc[0][1] : null;
}
$('#p-start').addEventListener('click', () => { const p = pickProblem(); if (!p) return; P = { p, t0: null, tt: null, sw: 0 }; $('#prob-setup').hidden = true; $('#prob-run').hidden = false; renderProb(); window.scrollTo({ top: 0, behavior: 'auto' }); });
function parseSubs(t) { // separa introduzione e sotto-domande a), b), c)
  const intro = [], subs = [];
  String(t).split('\n').forEach(l => { const m = l.match(/^\s*([a-z])\)\s*(.*)$/i); if (m) subs.push({ k: m[1], t: m[2] }); else if (l.trim()) { if (subs.length) subs[subs.length - 1].t += ' ' + l.trim(); else intro.push(l.trim()); } });
  return { intro, subs };
}
function subHtml(s) {
  let pt = ''; const tx = s.t.replace(/^\(\s*Punti\s*([\d.,]+)\s*\)\s*/i, (a, p) => { pt = p; return ''; });
  return `<div class="subq"><span class="lt" aria-hidden="true">${esc(s.k)}</span><div><div class="sr-only-l sr">Punto ${esc(s.k)}</div>${pt ? `<span class="pt">${esc(pt)} punti</span>` : ''}<div class="tx">${inline(tx)}</div></div></div>`;
}
function renderProb() {
  const p = P.p, { intro, subs } = parseSubs(p.testo); let meta = '';
  if (intro.length) { const mm = intro[0].match(/^\(\s*(Esame[^)]*)\)\s*(.*)$/i); if (mm) { meta = mm[1]; intro[0] = mm[2]; } }
  const sol = parseSubs(p.soluzione);
  const solHtml = sol.subs.length ? (sol.intro.length ? '<div class="sol-plain">' + fmt(sol.intro.join('\n')) + '</div>' : '') + sol.subs.map(subHtml).join('') : '<div class="sol-plain">' + fmt(p.soluzione) + '</div>';
  $('#prob-run').innerHTML = `<div class="prob">
    <article class="card p-card"><div class="p-top"><span class="pill">${esc(p.theme)}</span><span class="stopw"><button class="btn ghost small" id="p-sw" aria-pressed="false">${IC.clock} Cronometro</button><span class="tl mono" id="p-tl" hidden>00:00</span></span></div>
      ${meta ? `<div class="p-meta">${esc(meta)}</div>` : ''}${intro.filter(x => x).length ? `<div class="p-intro">${fmt(intro.join('\n'))}</div>` : ''}
      <div>${subs.length ? subs.map(subHtml).join('') : ''}</div>
      <p class="hint">Prova a svolgerlo su carta, poi guarda la soluzione. <span class="muted">${esc(p.id)}</span></p></article>
    <article class="card p-card sol-card" id="p-solcard" aria-live="polite"><div class="sol-ph" id="p-ph">${IC.book}<p>La soluzione compare qui, quando sei pronto.</p><button class="btn xl" id="p-show">${IC.eye.replace('<svg', '<svg class="eye"')} Mostra la soluzione</button></div>
      <div id="p-sol" hidden><div class="sol-h">Soluzione</div><div class="sol">${solHtml}</div>${p.concetti ? `<div class="note" style="margin-top:12px"><strong>Concetti:</strong> ${esc(p.concetti)}</div>` : ''}${chapterHint(p.theme)}</div></article>
    <div class="p-grades" id="p-grades" hidden><button class="grade g-bad" data-r="0"><b>Non sono riuscito</b><small>tornerà presto</small></button><button class="grade g-mid" data-r="1"><b>Con dubbi o errori</b><small>da riprovare</small></button><button class="grade g-good" data-r="2"><b>Svolto bene</b><small>per ora basta</small></button></div></div>
    <div class="row end" style="margin-top:12px"><button class="btn ghost small" id="p-exit">Torna all'elenco</button></div>`;
  $('#p-sw').addEventListener('click', () => {
    const b = $('#p-sw'), tl = $('#p-tl');
    if (P.tt) { clearInterval(P.tt); P.tt = null; b.setAttribute('aria-pressed', 'false'); return; }
    P.t0 = Date.now() - P.sw * 1000; tl.hidden = false; b.setAttribute('aria-pressed', 'true');
    const f = () => { P.sw = Math.floor((Date.now() - P.t0) / 1000); tl.textContent = pad(Math.floor(P.sw / 60)) + ':' + pad(P.sw % 60); }; f(); P.tt = setInterval(f, 1000);
  });
  $('#p-show').addEventListener('click', () => {
    const c = $('#p-solcard'); $('#p-ph').hidden = true; $('#p-sol').hidden = false; c.classList.add('shown'); $('#p-grades').hidden = false;
    if (P.tt) { clearInterval(P.tt); P.tt = null; $('#p-sw').setAttribute('aria-pressed', 'false'); }
    if (window.innerWidth < 900) setTimeout(() => c.scrollIntoView({ behavior: RM.matches ? 'auto' : 'smooth', block: 'start' }), 60);
  });
  $('#p-exit').addEventListener('click', closeProb);
  $$('#p-grades button').forEach(b => b.addEventListener('click', () => {
    const r = +b.dataset.r; S.probs[p.id] = { r, date: todayStr() }; bumpTheme(p.theme, r === 2); mark(); save();
    closeProb(); say('Registrato'); toast('Registrato');
  }));
}
function closeProb() { if (P && P.tt) clearInterval(P.tt); P = null; $('#prob-run').hidden = true; $('#prob-setup').hidden = false; renderProbSetup(); window.scrollTo({ top: 0, behavior: 'auto' }); }

/* ---------- Schede ---------- */
const STEPS = [0, 1, 3, 7, 14, 30];
let C = null, cardMat = '*';
const isDue = c => { const s = S.cards[c.id]; return !s || s.due <= todayStr(); };
function renderCardSetup() {
  const mats = ['*', ...Object.keys(DATA.materie)];
  $('#c-mat').innerHTML = mats.map(m => `<button class="cp" role="radio" aria-checked="${m === cardMat}" data-m="${esc(m)}">${m === '*' ? 'Tutte' : esc(m)}<span class="n">${DATA.cards.filter(c => (m === '*' || c.m === m) && isDue(c)).length}</span></button>`).join('');
  $$('#c-mat .cp').forEach(b => b.addEventListener('click', () => { cardMat = b.dataset.m; renderCardSetup(); }));
  const all = DATA.cards.filter(c => cardMat === '*' || c.m === cardMat), due = all.filter(isDue);
  $('#c-count').textContent = due.length ? `${due.length} da ripassare su ${all.length}` : `Nessuna in scadenza (${all.length} in totale)`; $('#c-start').disabled = !due.length;
}
$('#c-start').addEventListener('click', () => startCards(+$('#c-max').value));
function startCards(max, onEnd) {
  const mat = cardMat || '*';
  const due = shuffle(DATA.cards.filter(c => (mat === '*' || c.m === mat) && isDue(c) && !c.lungo)).concat(shuffle(DATA.cards.filter(c => (mat === '*' || c.m === mat) && isDue(c) && c.lungo))).slice(0, max);
  if (!due.length) { if (onEnd) onEnd(); return; }
  C = { q: due, i: 0, known: 0, redo: new Set(), onEnd, flipped: false };
  $('#cards-setup').hidden = true; $('#cards-run').hidden = false;
  $('#cards-run').innerHTML = `<div class="cr-head"><div class="cr-top"><span class="cr-count" id="c-count-l" aria-live="polite"></span><button class="btn ghost small" id="c-exit">Esci</button></div><div class="cr-bar" role="progressbar" aria-label="Avanzamento della sessione" aria-valuemin="0"><i id="c-prog"></i></div></div><div id="c-body"></div>`;
  $('#c-exit').addEventListener('click', abortCards);
  renderCard(); window.scrollTo({ top: 0, behavior: 'auto' });
}
function abortCards() { if (!C) return; C = null; setPhase(0); $('#cards-run').hidden = true; $('#cards-setup').hidden = false; renderCardSetup(); }
function fmtDays(n) { return n <= 1 ? 'domani' : (n < 14 ? `tra ${n} giorni` : (n < 30 ? `tra ${Math.round(n / 7)} settimane` : 'tra 1 mese')); }
function previewInterval(c, g) { // intervallo previsto per il voto g, senza toccare lo stato
  if (g === 0) return 'tra poco';
  const box = (S.cards[c.id] || { box: 0 }).box;
  const nb = g === 1 ? Math.max(1, box) : Math.min(box + (g === 3 ? 2 : 1), STEPS.length - 1);
  return fmtDays(g === 1 ? 1 : capInterval(STEPS[nb], c.m));
}
const GRADES = [{ g: 0, l: 'Da rivedere', c: 'g-bad' }, { g: 1, l: 'Difficile', c: 'g-mid' }, { g: 2, l: 'Bene', c: 'g-good' }, { g: 3, l: 'Facile', c: 'g-top' }];
function renderCard() {
  if (C.i >= C.q.length) {
    const cb = C.onEnd, k = C.known, n = C.q.length; C = null;
    $('#cards-run').innerHTML = `<div class="card fin"><div class="check"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.500l4.500 4.500L19 7.500"/></svg></div><h2>Sessione finita</h2><p>Sapevi <b class="mono">${k}</b> schede su <b class="mono">${n}</b>. Quelle sbagliate ricompaiono tra poco e poi domani.</p><div class="bar-k" style="--w:${n ? Math.round(100 * k / n) : 0}%" aria-hidden="true"><i></i></div><button class="btn xl" id="c-done">${cb ? 'Continua' : 'Torna alle schede'}</button></div>`;
    $('#c-done').addEventListener('click', () => { $('#cards-run').hidden = true; $('#cards-setup').hidden = false; renderCardSetup(); if (cb) cb(); }); $('#c-done').focus({ preventScroll: true }); return;
  }
  const c = C.q[C.i], n = C.q.length; C.flipped = false;
  $('#c-count-l').innerHTML = `<b>${C.i + 1}</b> di ${n}`; $('#c-prog').style.setProperty('--p', (C.i / n).toFixed(3));
  const pb = $('.cr-bar'); pb.setAttribute('aria-valuemax', n); pb.setAttribute('aria-valuenow', C.i);
  $('#c-body').innerHTML = `<div class="stage" id="c-stage" style="--c:var(--s${subjIdx(c.m) % 4})"><span class="swipe-badge l" id="sb-l" aria-hidden="true">Da rivedere</span><span class="swipe-badge r" id="sb-r" aria-hidden="true">Bene</span>
    <div class="swipe" id="c-swipe"><div class="flip" id="c-flip"><div class="face front" id="c-front"><span class="tape">${esc(c.m)}</span><div class="ft">${esc(c.t)}</div><div class="fb">${fmt(c.d)}${figs(c.img)}</div><span class="turn" aria-hidden="true">tocca per girare ${IC.turn}</span></div>
    <div class="face back" id="c-back" aria-hidden="true"><span class="tape">Risposta</span><div class="fb">${fmt(c.r)}${figs(c.imgf)}</div></div></div></div></div>
    <div class="cta-slot" style="margin-top:16px"><button class="btn xl" id="c-show">Mostra la risposta <span class="kbd kbd-only">Invio</span></button><div class="grades" id="c-grades" hidden role="group" aria-label="Quanto la sapevi?">${GRADES.map(x => `<button class="grade ${x.c}" data-g="${x.g}"><span class="kk kbd-only">${x.g + 1}</span><b>${x.l}</b><small>${previewInterval(c, x.g)}</small></button>`).join('')}</div></div>`;
  $('#c-show').addEventListener('click', showCardAnswer); $('#c-show').focus({ preventScroll: true });
  $('#c-flip').addEventListener('click', () => { if (!C.dragged) showCardAnswer(); });
  $$('#c-grades button').forEach(b => b.addEventListener('click', () => gradeCard(+b.dataset.g)));
  bindSwipe();
}
function showCardAnswer() {
  if (!C || !$('#c-show') || $('#c-show').hidden) return;
  C.flipped = true; $('#c-flip').classList.add('flipped'); $('#c-back').removeAttribute('aria-hidden'); $('#c-front').setAttribute('aria-hidden', 'true');
  $('#c-show').hidden = true; $('#c-grades').hidden = false; $('#c-grades button').focus({ preventScroll: true });
  $('#c-back').scrollTop = 0;
}
function previewCommit(dir) { const s = $('#c-swipe'); s.classList.remove('drag'); s.style.transform = `translateX(${dir * (window.innerWidth + 80)}px) rotate(${dir * 18}deg)`; s.style.opacity = '0'; }
function bindSwipe() { // trascinamento con il dito: destra = bene, sinistra = da rivedere; si può annullare tornando al centro
  const stage = $('#c-stage'), sw = $('#c-swipe'), bl = $('#sb-l'), br = $('#sb-r'); let sx = 0, sy = 0, id = null, drag = false, dx = 0;
  const setB = () => { const k = Math.min(1, Math.abs(dx) / 110); bl.style.opacity = dx < 0 ? k : 0; br.style.opacity = dx > 0 ? k : 0; };
  const reset = () => { sw.classList.remove('drag'); sw.style.transform = ''; bl.style.opacity = 0; br.style.opacity = 0; dx = 0; };
  stage.addEventListener('pointerdown', e => { if (e.pointerType !== 'touch' && e.pointerType !== 'pen') return; id = e.pointerId; sx = e.clientX; sy = e.clientY; drag = false; dx = 0; C.dragged = false; });
  stage.addEventListener('pointermove', e => {
    if (e.pointerId !== id || !C) return; dx = e.clientX - sx; const dy = e.clientY - sy;
    if (!drag) {
      if (Math.abs(dx) > 12 && Math.abs(dx) > Math.abs(dy) * 1.2 && C.flipped) { drag = true; C.dragged = true; sw.classList.add('drag'); try { stage.setPointerCapture(id); } catch (x) {} }
      else if (Math.abs(dy) > 16) { id = null; return; } else return;
    }
    sw.style.transform = `translateX(${dx}px) rotate(${dx / 24}deg)`; setB();
  });
  const end = e => {
    if (e.pointerId !== id) return; id = null; if (!drag) return; drag = false;
    if (e.type !== 'pointercancel' && Math.abs(dx) >= 110 && C) { const dir = dx > 0 ? 1 : -1; previewCommit(dir); setTimeout(() => { if (C) gradeCard(dir > 0 ? 2 : 0); }, 240); }
    else reset();
    setTimeout(() => { if (C) C.dragged = false; }, 50);
  };
  stage.addEventListener('pointerup', end); stage.addEventListener('pointercancel', end);
}
function gradeCard(g) {
  if (!C || !$('#c-grades') || $('#c-grades').hidden) return; const c = C.q[C.i];
  const s = S.cards[c.id] || { box: 0 };
  if (g === 0) { s.box = 0; s.due = todayStr(); if (!C.redo.has(c.id)) { C.redo.add(c.id); C.q.push(c); } }
  else { C.known++; s.box = g === 1 ? Math.max(1, s.box) : Math.min(s.box + (g === 3 ? 2 : 1), STEPS.length - 1); s.due = addDays(todayStr(), g === 1 ? 1 : capInterval(STEPS[s.box], c.m)); }
  S.cards[c.id] = s; mark(); save(); C.i++; renderCard();
}

/* ---------- Sessione di oggi ---------- */
function setPhase(p) {
  const el = $('#phase'); el.hidden = !p;
  $$('#phase li').forEach(li => { const n = +li.dataset.p; li.classList.toggle('on', n === p); li.classList.toggle('done', n < p); if (n === p) li.setAttribute('aria-current', 'step'); else li.removeAttribute('aria-current'); });
}
function startSession(short) {
  setPhase(1); cardMat = '*'; showTab('schede');
  const finishQuiz = () => { setPhase(3); showTab('oggi'); say('Sessione completata'); toast('Sessione completata'); setTimeout(() => { if (!$('#phase').hidden && $$('#phase li.on')[0] && $$('#phase li.on')[0].dataset.p === '3') setPhase(0); }, 4000); };
  const quizPhase = () => {
    setPhase(2); showTab('quiz');
    const list = pickQuiz(short ? 2 : 6, {}).concat((canGen() ? GEN.many(short ? 1 : 3, QM, cov(QM)) : []));
    startQuiz(false, { list, label: 'sessione di oggi', fb: true, onEnd: finishQuiz });
  };
  startCards(short ? 5 : 10, quizPhase);
}

/* ---------- impostazioni, salvataggio / spostamento progressi ---------- */
$('#set-btn').addEventListener('click', () => $('#dlg-set').showModal());
$$('.dlg').forEach(d => d.addEventListener('click', e => { if (e.target === d) d.close(); }));
$('#exp').addEventListener('click', () => {
  const t = $('#xfer'); t.hidden = false; t.value = JSON.stringify(S); t.select();
  try { navigator.clipboard.writeText(t.value).then(() => { $('#xfer-msg').textContent = 'Copiato negli appunti.'; toast('Copiato negli appunti'); }, () => { $('#xfer-msg').textContent = 'Seleziona il testo e copialo a mano.'; }); } catch (e) { $('#xfer-msg').textContent = 'Seleziona il testo e copialo a mano.'; }
});
$('#imp').addEventListener('click', () => {
  const t = $('#xfer'); if (t.hidden) { t.hidden = false; t.value = ''; t.focus(); $('#xfer-msg').textContent = 'Incolla qui il testo copiato dall’altro dispositivo e premi di nuovo Importa.'; return; }
  try { const x = JSON.parse(t.value); if (!x || x.v !== 2) throw 0; S = Object.assign(newState(), x); fixS(); save(); $('#xfer-msg').textContent = 'Progressi importati.'; toast('Progressi importati'); renderOggi(); }
  catch (e) { $('#xfer-msg').textContent = 'Testo non valido.'; }
});

/* ---------- scorciatoie da tastiera ---------- */
document.addEventListener('keydown', e => {
  const tag = (e.target && e.target.tagName) || ''; if (/INPUT|TEXTAREA|SELECT/.test(tag) || e.ctrlKey || e.metaKey || e.altKey || document.querySelector('dialog[open]')) return;
  if (Q && !$('#quiz-run').hidden) {
    if (/^[1-8]$/.test(e.key) && !Q.answered) { if (+e.key <= Q.list[Q.i].o.length) answer(+e.key); }
    else if ((e.key === 'Enter' || e.key === ' ') && Q.answered && document.activeElement !== $('#q-next')) { e.preventDefault(); nextQ(); }
  } else if (C && !$('#cards-run').hidden) {
    if ((e.key === 'Enter' || e.key === ' ') && $('#c-show') && !$('#c-show').hidden && document.activeElement !== $('#c-show')) { e.preventDefault(); showCardAnswer(); }
    else if (/^[1-4]$/.test(e.key) && $('#c-grades') && !$('#c-grades').hidden) gradeCard(+e.key - 1);
  }
});

/* ---------- avvio ---------- */
function boot(d) {
  DATA = d;
  $('#agg').textContent = itDate(DATA.oggi);
  if (SERVER) { const m = $('#xfer-p'); if (m) m.textContent = ONLINE ? 'I progressi sono salvati nel tuo account, quindi li ritrovi su ogni dispositivo. Qui puoi comunque copiarli a mano.' : 'I progressi sono salvati anche nel file progressi.json del computer, quindi restano cambiando browser. Qui puoi comunque copiarli a mano.'; }
  DATA.quiz.forEach(q => { if (!q.theme) q.theme = themeOf(q.args); });
  DATA.problemi.forEach(p => { p.theme = themeOf(p.args); });
  $('#skel').hidden = true; $('#bento').hidden = false;
  let first = (location.hash || '').replace('#', '') || pending;
  if (!TABS.includes(first)) { try { first = localStorage.getItem('quaderno-tab'); } catch (e) {} }
  current = '__none__'; showTab(TABS.includes(first) ? first : 'oggi'); moveInd(true);
}
$('#load-retry').addEventListener('click', () => location.reload());
loadServerState().then(() => fetch('data.json')).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }).then(boot).catch(err => {
  $('#skel').hidden = true; TABS.forEach(t => { $('#tab-' + t).hidden = true; });
  const e = $('#load-err'); e.hidden = false; $('#load-err-t').textContent = 'Non riesco a caricare i dati (' + err.message + '). Ricarica la pagina; ' + (ONLINE ? 'se resta così, esci e rientra (la sessione potrebbe essere scaduta).' : 'se resta così, controlla che il sito sia acceso (apri_quaderno.bat).');
});

$('#reset-btn').addEventListener('click', () => {
  const b = $('#reset-btn');
  if (!b.dataset.sure) { b.dataset.sure = '1'; b.textContent = 'Sicuro? Premi di nuovo per cancellare tutto'; setTimeout(() => { delete b.dataset.sure; b.textContent = 'Azzera tutti i progressi'; }, 5000); return; }
  delete b.dataset.sure; b.textContent = 'Azzera tutti i progressi';
  S = newState(); fixS(); save(); renderOggi(); toast('Progressi azzerati');
});

/* le barre dentro l'elenco ripiegabile partono quando lo apri (l'osservatore non scatta sugli elementi nascosti) */
$('#freq-card').addEventListener('toggle', () => { if ($('#freq-card').open) requestAnimationFrame(() => $$('#freq .fr').forEach((el, i) => setTimeout(() => el.classList.add('in'), i * 40))); });
