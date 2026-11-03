// Collaudo indipendente del generatore: ricalcola ogni risposta a forza bruta leggendo il testo della domanda.
const GEN = require('./gen.js');
const sup = { '⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4, '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9 };
const sub = { '₀': 0, '₁': 1, '₂': 2, '₃': 3, '₄': 4, '₅': 5, '₆': 6, '₇': 7, '₈': 8, '₉': 9 };
const num = (s, m) => Number([...s].map(c => m[c]).join(''));
const gcd = (a, b) => (b ? gcd(b, a % b) : a);
const pl = t => { t = t.replace(/−/g, '-').replace(/\s+/g, ''); const k = t.match(/^(-?\d*)n([+-]\d+)?$/); if (k) return [k[1] === '' ? 1 : (k[1] === '-' ? -1 : +k[1]), k[2] ? +k[2] : 0]; return [0, +t]; };
let bad = 0, n = 0; const kinds = {};
function fail(q, why) { bad++; if (bad < 8) console.log('ERRORE', why, JSON.stringify(q, null, 1)); }
function check(q) {
  const txt = q.q, ans = q.o[q.a - 1];
  if (new Set(q.o).size !== 5) return fail(q, 'opzioni duplicate');
  if (q.a < 1 || q.a > 5) return fail(q, 'indice');
  let m;
  if ((m = txt.match(/Quante soluzioni modulo (\d+) ha la congruenza (\d+)X ≡ (\d+) mod/))) {
    const N = +m[1], a = +m[2], b = +m[3]; let c = 0; for (let x = 0; x < N; x++) if ((a * x - b) % N === 0) c++;
    if (String(c) !== ans) return fail(q, 'cong ' + c);
  } else if ((m = txt.match(/In ℤ([₀-₉]+) l'inverso moltiplicativo di \[(\d+)\] è/))) {
    const N = num(m[1], sub), a = +m[2]; let x = 0; for (let k = 1; k < N; k++) if ((a * k) % N === 1) x = k;
    if (String(x) !== ans) return fail(q, 'inverso ' + x);
  } else if ((m = txt.match(/φ\((\d+)\) =/)) || (m = txt.match(/generatori del gruppo additivo ℤ([₀-₉]+)/)) || (m = txt.match(/classi invertibili in \(ℤ([₀-₉]+)/))) {
    const N = m[1][0] >= '0' && m[1][0] <= '9' ? +m[1] : num(m[1], sub); let c = 0; for (let k = 1; k <= N; k++) if (gcd(k, N) === 1) c++;
    if (String(c) !== ans) return fail(q, 'phi ' + c);
  } else if ((m = txt.match(/non genera \(ℤ([₀-₉]+), \+\)/))) {
    const N = num(m[1], sub), k = +ans.slice(1, -1);
    if (gcd(k, N) === 1) return fail(q, 'nongen');
    for (const o of q.o) if (o !== ans && gcd(+o.slice(1, -1), N) !== 1) return fail(q, 'nongen: distrattore non coprimo');
  } else if ((m = txt.match(/In ℤ([₀-₉]+) la classe \[(\d+)\]([⁰¹²³⁴⁵⁶⁷⁸⁹]+) è/))) {
    const N = num(m[1], sub), a = +m[2], e = num(m[3], sup); let r = 1; for (let i = 0; i < e; i++) r = (r * a) % N;
    if (`[${r}]` !== ans) return fail(q, 'pow ' + r);
  } else if ((m = txt.match(/scrittura di (\d+) in base 2/))) {
    if (parseInt(ans, 2) !== +m[1]) return fail(q, 'base2');
  } else if ((m = txt.match(/\|A\| = (\d+) e \|B\| = (\d+)\. Quanti .* (\d+) elementi di A e (\d+) di B/))) {
    const [n1, n2, r, s] = m.slice(1).map(Number); const C = (n, k) => { let t = 1; for (let i = 1; i <= k; i++) t = (t * (n - k + i)) / i; return t; };
    const m2 = ans.match(/C\((\d+), (\d+)\) · C\((\d+), (\d+)\)/); if (!m2 || C(+m2[1], +m2[2]) * C(+m2[3], +m2[4]) !== C(n1, r) * C(n2, s) || +m2[1] !== n1 || +m2[3] !== n2) return fail(q, 'conteggio');
  } else if ((m = txt.match(/Sia π = ((?:\([\d ]+\))+) ∈ S([₀-₉]+)/))) {
    const N = num(m[2], sub), cycles = [...m[1].matchAll(/\(([\d ]+)\)/g)].map(x => x[1].split(' ').map(Number));
    const apply = x => { for (let i = cycles.length - 1; i >= 0; i--) { const c = cycles[i], j = c.indexOf(x); if (j >= 0) x = c[(j + 1) % c.length]; } return x; }; // destra→sinistra
    const pi = [0]; for (let x = 1; x <= N; x++) pi[x] = apply(x);
    const cyc = []; const seen = new Set();
    for (let x = 1; x <= N; x++) { if (seen.has(x)) continue; const c = []; let y = x; while (!seen.has(y)) { seen.add(y); c.push(y); y = pi[y]; } if (c.length > 1) cyc.push(c); }
    const typ = cyc.map(c => c.length).sort((a, b) => b - a); const ord = typ.reduce((a, l) => (a / gcd(a, l)) * l, 1);
    const par = typ.reduce((s, l) => s + l - 1, 0) % 2 === 0 ? 'pari' : 'dispari';
    if (/decomposizione di π in cicli disgiunti/.test(txt)) {
      const exp = cyc.length ? cyc.map(c => '(' + c.join(' ') + ')').join('') : '(id)'; if (exp !== ans) return fail(q, 'dec ' + exp);
      if (new Set(q.o.map(o => permKey(o, N))).size !== 5) return fail(q, 'dec: due opzioni sono la stessa permutazione');
    }
    else if (/Il tipo di π/.test(txt)) { if ('(' + (typ.length ? typ.join(', ') : '1') + ')' !== ans) return fail(q, 'tipo'); }
    else if (/Allora π$/.test(txt)) { if (ans !== `è ${par} ed ha periodo ${ord}`) return fail(q, 'pp'); }
    else if ((m = txt.match(/Allora π([⁰¹²³⁴⁵⁶⁷⁸⁹]+)\((\d+)\) =/))) { const k = num(m[1], sup); let x = +m[2]; for (let i = 0; i < k; i++) x = pi[x]; if (String(x) !== ans) return fail(q, 'pot'); }
    else return fail(q, 'perm non riconosciuta');
  } else if ((m = txt.match(/(\d+) amici ordinano .* tra (\d+) tipi/))) {
    const k = +m[1], t = +m[2]; if (ans !== `${t}${[...String(k)].map(d => '⁰¹²³⁴⁵⁶⁷⁸⁹'[d]).join('')}`) return fail(q, 'rip');
  } else if ((m = txt.match(/far sedere (\d+) persone in una fila di (\d+) sedie/))) {
    if (ans !== `${m[2]}!/${m[2] - m[1]}!`) return fail(q, 'sem');
  } else if ((m = txt.match(/^Siano f, g : ℤ → ℤ le funzioni f\(n\) = (.*) e g\(n\) = (.*)\. Allora \(g ∘ f\)\(n\) =$/))) {
    const F = pl(m[1]), G = pl(m[2]), R = pl(ans); for (let n = -6; n <= 6; n++) if (G[0] * (F[0] * n + F[1]) + G[1] !== R[0] * n + R[1]) return fail(q, 'comp');
  } else if ((m = txt.match(/^Sia f : ℝ → ℝ la funzione biettiva f\(x\) = (.*)\. Allora f⁻¹\((.*)\) =$/))) {
    const F = pl(m[1].replace(/x/g, 'n')), k = +m[2].replace('−', '-'), v = +ans.replace('−', '-'); if (F[0] * v + F[1] !== k) return fail(q, 'invaff');
  } else if ((m = txt.match(/^La funzione f : ℤ → ℤ, f\(n\) = (.*), è$/))) {
    const F = pl(m[1]), a = F[0]; const exp = a === 0 ? 'né iniettiva né suriettiva' : (Math.abs(a) === 1 ? 'iniettiva e suriettiva' : 'iniettiva ma non suriettiva');
    let inj = true, img = new Set(); for (let n = -50; n <= 50; n++) { const v = a * n + F[1]; if (img.has(v)) inj = false; img.add(v); } let sur = true; for (let t = -20; t <= 20; t++) if (!img.has(t)) sur = false;
    const real = !inj ? (sur ? 'suriettiva ma non iniettiva' : 'né iniettiva né suriettiva') : (sur ? 'iniettiva e suriettiva' : 'iniettiva ma non suriettiva');
    if (ans !== real || ans !== exp) return fail(q, 'class ' + real);
  } else if ((m = txt.match(/^Sia f : ℝ → ℝ, f\(x\) = x²\. Allora f⁻¹\(\[(\d+), (\d+)\]\) è$/))) {
    const lo = +m[1], hi = +m[2], iv = ans.split(' ∪ ').map(t => t.match(/\[(−?\d+), (−?\d+)\]/).slice(1).map(v => +v.replace('−', '-')));
    for (let x = -40; x <= 40; x += 0.25) { const inA = iv.some(([p, r]) => x >= p && x <= r), real = x * x >= lo && x * x <= hi; if (inA !== real) return fail(q, 'preim x=' + x); }
  } else if ((m = txt.match(/^Se \|A\| = (\d+) e \|B\| = (\d+), quanti elementi ha il prodotto cartesiano A × B\?$/))) { if (+ans !== m[1] * m[2]) return fail(q, 'prod'); }
  else if ((m = txt.match(/^Quanti sottoinsiemi \(vuoto e insieme stesso compresi\) ha un insieme di (\d+) elementi\?$/))) { if (+ans !== 2 ** +m[1]) return fail(q, 'parti'); }
  else if ((m = txt.match(/^Siano A = (.*) e B = (.*)\. Allora A (∪|∩|∖) B =$/))) {
    const ps = t => t === '∅' ? [] : t.replace(/[{}]/g, '').split(', ').map(Number), A = ps(m[1]), B = ps(m[2]); const U = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    const r = m[3] === '∪' ? U.filter(v => A.includes(v) || B.includes(v)) : m[3] === '∩' ? U.filter(v => A.includes(v) && B.includes(v)) : A.filter(v => !B.includes(v));
    if (ans !== (r.length ? '{' + r.join(', ') + '}' : '∅')) return fail(q, 'setop');
  } else if ((m = txt.match(/^Siano σ = ((?:\([\d ]+\))+) e π = ((?:\([\d ]+\))+) in S([₀-₉]+)\. (.*)$/))) {
    const N = num(m[3], sub), sg = applyCycles(m[1]), pi = applyCycles(m[2]), sp = x => sg(pi(x)), rest = m[4]; // σ ∘ π: prima π, poi σ
    const cyc = cyclesOfFn(sp, N), typ = cyc.map(c => c.length).sort((a, b) => b - a);
    if (/^La decomposizione in cicli disgiunti di σ ∘ π/.test(rest)) {
      if (ans !== cyc.map(c => '(' + c.join(' ') + ')').join('')) return fail(q, 'σ∘π dec');
      if (new Set(q.o.map(o => permKey(o, N))).size !== 5) return fail(q, 'σ∘π: due opzioni sono la stessa permutazione');
    } else if ((m = rest.match(/^Allora \(σ ∘ π\)\((\d+)\) =$/))) { if (+ans !== sp(+m[1])) return fail(q, 'σ∘π val'); }
    else if (/^Il tipo e il periodo di σ ∘ π/.test(rest)) { if (ans !== `tipo (${typ.join(', ')}), periodo ${orderByPowers(sp, N)}`) return fail(q, 'σ∘π tp'); }
    else return fail(q, 'σ∘π non riconosciuta');
  } else if ((m = txt.match(/^Quante sono le permutazioni di tipo \(([\d, ]+)\) in S([₀-₉]+)\?$/))) {
    if (+ans !== (SN(num(m[2], sub)).tipi.get(m[1]) || 0)) return fail(q, 'conta tipo');
  } else if ((m = txt.match(/^Una permutazione di S([₀-₉]+) ha tipo \(([\d, ]+)\)\. Il suo periodo è$/))) {
    const N = num(m[1], sub), ls = m[2].split(', ').map(Number); let at = 1; const cs = ls.map(l => { const c = []; for (let k = 0; k < l; k++) c.push(at++); return c; });
    if (at - 1 > N) return fail(q, 'tipo troppo lungo per Sₙ');
    if (+ans !== orderByPowers(applyCycles(cs.map(c => '(' + c.join(' ') + ')').join('')), N)) return fail(q, 'periodo tipo');
  } else if ((m = txt.match(/^Qual è il periodo massimo di un elemento di S([₀-₉]+)\?$/))) { if (+ans !== SN(num(m[1], sub)).max) return fail(q, 'periodo max'); }
  else if ((m = txt.match(/^Quanti elementi di periodo (\d+) ci sono in S([₀-₉]+)\?$/))) { if (+ans !== (SN(num(m[2], sub)).ordini.get(+m[1]) || 0)) return fail(q, 'conta periodo'); }
  else if ((m = txt.match(/^Quanto vale il coefficiente binomiale \((\d+) su (\d+)\), cioè C\((\d+), (\d+)\)\?$/))) {
    const N = +m[1], K = +m[2]; let c = 0; for (let s = 0; s < 1 << N; s++) { let b = 0; for (let x = s; x; x >>= 1) b += x & 1; if (b === K) c++; }
    if (m[3] !== m[1] || m[4] !== m[2] || +ans !== c) return fail(q, 'binomiale');
  } else if ((m = txt.match(/^Nello sviluppo di \(a \+ b\)([⁰¹²³⁴⁵⁶⁷⁸⁹]+), il coefficiente di a([⁰¹²³⁴⁵⁶⁷⁸⁹]*)b([⁰¹²³⁴⁵⁶⁷⁸⁹]*) è$/))) {
    const N = num(m[1], sup), ea = m[2] ? num(m[2], sup) : 1, eb = m[3] ? num(m[3], sup) : 1; let P = [1]; // coefficienti di (a + b)^N per moltiplicazioni successive, indice = esponente di a
    for (let k = 0; k < N; k++) { const Q = Array(P.length + 1).fill(0); P.forEach((c, i) => { Q[i] += c; Q[i + 1] += c; }); P = Q; }
    if (ea + eb !== N || +ans !== P[ea]) return fail(q, 'binomio di Newton');
  } else if ((m = txt.match(/^In una pasticceria ci sono (\d+) tipi di pasticcini\. Quanti vassoi diversi da (\d+) pasticcini/)) || (m = txt.match(/^Quanti sono i monomi di grado (\d+) nelle (\d+) variabili/))) {
    const [n_, k_] = /monomi/.test(txt) ? [+m[2], +m[1]] : [+m[1], +m[2]]; const ms = (n, k) => (n === 1 || k === 0 ? 1 : [...Array(k + 1).keys()].reduce((s, j) => s + ms(n - 1, k - j), 0)); // quanti del primo tipo, poi il resto
    if (+ans !== ms(n_, k_)) return fail(q, 'combinazioni con ripetizione');
  } else if ((m = txt.match(/^In una gara con (\d+) atleti, quante sono le possibili classifiche dei primi (\d+) posti/))) {
    const N = +m[1], K = +m[2], rec = (used, k) => (k === 0 ? 1 : [...Array(N).keys()].filter(x => !(used & (1 << x))).reduce((s, x) => s + rec(used | (1 << x), k - 1), 0));
    if (+ans !== rec(0, K)) return fail(q, 'disposizioni gara');
  } else return fail(q, 'domanda non riconosciuta: ' + txt);
}
// ---- strumenti indipendenti per le permutazioni (numeri 1..N) ----
function applyCycles(txt) { // prodotto di cicli, composto da destra a sinistra
  const cs = [...txt.matchAll(/\(([\d ]+)\)/g)].map(x => x[1].split(' ').map(Number));
  return x => { for (let i = cs.length - 1; i >= 0; i--) { const j = cs[i].indexOf(x); if (j >= 0) x = cs[i][(j + 1) % cs[i].length]; } return x; };
}
function cyclesOfFn(f, N) { const seen = new Set(), out = []; for (let x = 1; x <= N; x++) { if (seen.has(x)) continue; const c = []; let y = x; while (!seen.has(y)) { seen.add(y); c.push(y); y = f(y); } if (c.length > 1) out.push(c); } return out; }
function orderByPowers(f, N) { let k = 1, g = f; const id = h => { for (let x = 1; x <= N; x++) if (h(x) !== x) return false; return true; }; while (!id(g)) { const h = g; g = x => f(h(x)); k++; if (k > 1000) return -1; } return k; }
function permKey(o, N) { if (o === '(id)') return [...Array(N).keys()].map(x => x + 1).join(','); const f = applyCycles(o); return [...Array(N).keys()].map(x => f(x + 1)).join(','); }
const SNc = {};
function SN(n) { // tutte le permutazioni di Sₙ: conteggi per tipo e per periodo, periodo massimo
  if (SNc[n]) return SNc[n];
  const tipi = new Map(), ordini = new Map(); let max = 1; const a = [...Array(n).keys()];
  const visit = () => {
    const seen = new Array(n).fill(false), ls = []; for (let i = 0; i < n; i++) { if (seen[i]) continue; let l = 0, j = i; while (!seen[j]) { seen[j] = true; j = a[j]; l++; } if (l > 1) ls.push(l); }
    ls.sort((x, y) => y - x); const key = ls.join(', '); tipi.set(key, (tipi.get(key) || 0) + 1);
    let k = 1; const pw = a.slice(); for (;;) { if (pw.every((v, i) => v === i)) break; for (let i = 0; i < n; i++) pw[i] = a[pw[i]]; k++; }
    ordini.set(k, (ordini.get(k) || 0) + 1); if (k > max) max = k;
  };
  const heap = k => { if (k === 1) return visit(); heap(k - 1); for (let i = 0; i < k - 1; i++) { const j = k % 2 ? 0 : i; [a[j], a[k - 1]] = [a[k - 1], a[j]]; heap(k - 1); } }; // algoritmo di Heap
  heap(n); return (SNc[n] = { tipi, ordini, max });
}
for (let i = 0; i < 6000; i++) { const q = GEN.make(); if (!q) { fail({ q: 'null' }, 'null'); continue; } n++; kinds[q.args[0]] = (kinds[q.args[0]] || 0) + 1; check(q); }
console.log(`${n} domande generate, ${bad} errori`, kinds);

// ---------- Algebra lineare e Fondamenti ----------
const supd = s => Number([...s].map(c => '⁰¹²³⁴⁵⁶⁷⁸⁹'.indexOf(c)).join(''));
const pc = s => { // "3 − 2i", "−i", "5", "i" -> [re, im]
  s = s.replace(/−/g, '-').replace(/\s+/g, '').replace(/^\(|\)$/g, '');
  const m = s.match(/^(-?\d+)?(?:([+-])(\d*)i)?$/); if (m && (m[1] !== undefined || m[2])) return [m[1] ? +m[1] : 0, m[2] ? (m[2] === '-' ? -1 : 1) * (m[3] === '' ? 1 : +m[3]) : 0];
  const k = s.match(/^(-?)(\d*)i$/); if (k) return [0, (k[1] ? -1 : 1) * (k[2] === '' ? 1 : +k[2])];
  throw new Error('cx? ' + s);
};
const mul = (p, q) => [p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0]];
const eq = (p, q) => Math.abs(p[0] - q[0]) < 1e-9 && Math.abs(p[1] - q[1]) < 1e-9;
function checkAlg(q) {
  const t = q.q, ans = q.o[q.a - 1]; let m;
  if (new Set(q.o).size !== 5) return fail(q, 'alg opzioni duplicate');
  if ((m = t.match(/^Il prodotto \((.*)\)·\((.*)\) è$/))) { if (!eq(mul(pc(m[1]), pc(m[2])), pc(ans))) return fail(q, 'mul'); }
  else if ((m = t.match(/^Il quoziente \((.*)\) \/ \((.*)\) è$/))) { if (!eq(mul(pc(ans), pc(m[2])), pc(m[1]))) return fail(q, 'div'); }
  else if ((m = t.match(/^Il modulo di z = (.*) è$/))) { const z = pc(m[1]); if (Math.abs(Math.hypot(z[0], z[1]) - +ans) > 1e-9) return fail(q, 'mod'); }
  else if ((m = t.match(/^L'inverso moltiplicativo di z = (.*) è$/))) { const mm = ans.match(/^\((.*)\)\/(\d+)$/); const w = pc(mm[1]); w[0] /= +mm[2]; w[1] /= +mm[2]; if (!eq(mul(pc(m[1]), w), [1, 0])) return fail(q, 'inv'); }
  else if ((m = t.match(/^Il valore di i([⁰¹²³⁴⁵⁶⁷⁸⁹]+) è$/))) { let z = [1, 0]; for (let i = 0; i < supd(m[1]); i++) z = mul(z, [0, 1]); if (!eq(z, pc(ans === '0' ? '0' : ans))) return fail(q, 'ipow'); }
  else if ((m = t.match(/^\((.*)\)² =$/))) { const z = pc(m[1]); if (!eq(mul(z, z), pc(ans))) return fail(q, 'sq'); }
  else if ((m = t.match(/^Quanto vale \(1 \+ i\)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)\?$/))) { let z = [1, 0]; for (let i = 0; i < supd(m[1]); i++) z = mul(z, [1, 1]); if (!eq(z, [+ans.replace('−', '-'), 0])) return fail(q, '1+i'); }
  else if ((m = t.match(/^Sia A = \(([^()]*)\)\. Allora det A =$/))) { if (leib(pm(m[1])) !== pn(ans)) return fail(q, 'det'); }
  else if ((m = t.match(/^Sia A = \(([^()]*)\)\. Allora tr\(A\) =$/))) { const A = pm(m[1]); if (A.reduce((s, r, i) => s + r[i], 0) !== pn(ans)) return fail(q, 'traccia'); }
  else if ((m = t.match(/^Siano A = \(([^()]*)\) e B = \(([^()]*)\)\. Allora tr\(A · B\) =$/))) { const P = mm(pm(m[1]), pm(m[2])); if (P.reduce((s, r, i) => s + r[i], 0) !== pn(ans)) return fail(q, 'traccia AB'); }
  else if ((m = t.match(/^Siano A = \(([^()]*)\) e B = \(([^()]*)\)\. L'entrata di posto \((\d), (\d)\) del prodotto A · B è$/))) { if (mm(pm(m[1]), pm(m[2]))[m[3] - 1][m[4] - 1] !== pn(ans)) return fail(q, 'prodotto'); }
  else if ((m = t.match(/^Sia A = \(([^()]*)\)\. Allora rk\(A\) =$/))) { if (String(rankMinori(pm(m[1]))) !== ans) return fail(q, 'rango ' + rankMinori(pm(m[1]))); }
  else if ((m = t.match(/^Sia A = \(([^()]*)\)\. L'entrata di posto \((\d), (\d)\) di A⁻¹ è$/))) { const X = invF(pm(m[1])); if (!X || Math.abs(X[m[2] - 1][m[3] - 1] - pf(ans)) > 1e-9) return fail(q, 'inversa'); }
  else if ((m = t.match(/^La matrice A = \(([^()]*)\) è invertibile\?$/))) {
    const d = leib(pm(m[1])), k = ans.match(/^sì, perché det A = (−?\d+) ≠ 0$/);
    if (d === 0 ? ans !== 'no, perché det A = 0' : !(k && pn(k[1]) === d)) return fail(q, 'invertibile');
  } else if ((m = t.match(/^Sia A ∈ M\((\d)\) con det A = (−?\d+)\. La matrice A′ si ottiene da A con (?:la mossa: |le mosse, nell'ordine: )(.*)\. Allora det A′ =$/))) {
    const n = +m[1], d = pn(m[2]); let R; do { R = rnd(n); } while (leib(R) === 0);
    let A = R.map(r => r.slice());
    for (const mv of m[3].split(/; (?=\(\d\) )/).map(s => s.replace(/^\(\d\) /, ''))) {
      let k, col = false; const T = M => M[0].map((_, j) => M.map(r => r[j]));
      if ((k = mv.match(/^si scambiano la (\d)ª e la (\d)ª (riga|colonna)$/))) { col = k[3] === 'colonna'; if (col) A = T(A); [A[k[1] - 1], A[k[2] - 1]] = [A[k[2] - 1], A[k[1] - 1]]; }
      else if ((k = mv.match(/^si moltiplica la (\d)ª (riga|colonna) per (−?\d+)$/))) { col = k[2] === 'colonna'; if (col) A = T(A); A[k[1] - 1] = A[k[1] - 1].map(x => x * pn(k[3])); }
      else if ((k = mv.match(/^alla (\d)ª (riga|colonna) si somma la (\d)ª (riga|colonna) moltiplicata per (−?\d+)$/))) { if (k[2] !== k[4] || k[1] === k[3]) return fail(q, 'mossa incoerente'); col = k[2] === 'colonna'; if (col) A = T(A); A[k[1] - 1] = A[k[1] - 1].map((x, j) => x + pn(k[5]) * A[k[3] - 1][j]); }
      else return fail(q, 'mossa non riconosciuta: ' + mv);
      if (col) A = T(A);
    }
    if (leib(A) * d !== pn(ans) * leib(R)) return fail(q, 'mosse di Gauss'); // det A′/det A misurato su una matrice vera
  } else if ((m = t.match(/^(?:Sia A ∈ M\((\d)\) con det A = (−?\d+)|Siano A, B ∈ M\((\d)\) con det A = (−?\d+) e det B = (−?\d+))\. Allora det\((.*)\) =$/))) {
    const n = +(m[1] || m[3]), A = conDet(n, pn(m[2] || m[4])), B = m[5] ? conDet(n, pn(m[5])) : null;
    const fatt = f => { const k = f.match(/^(−|−?\d+)?(ᵗ)?([AB])(²|⁻¹)?$/); if (!k) return null; let X = k[3] === 'A' ? A : B; if (k[2]) X = X[0].map((_, j) => X.map(r => r[j])); if (k[4] === '²') X = mm(X, X); if (k[4] === '⁻¹') X = invF(X); const c = k[1] === undefined ? 1 : k[1] === '−' ? -1 : pn(k[1]); return X.map(r => r.map(x => c * x)); };
    const fs = m[6].split(' · ').map(fatt); if (fs.some(f => !f)) return fail(q, 'espressione non riconosciuta');
    const v = leib(fs.reduce((P, X) => mm(P, X))); if (Math.abs(v - pf(ans)) > 1e-6 * Math.max(1, Math.abs(v))) return fail(q, 'proprietà det ' + v);
  }
  else return fail(q, 'alg non riconosciuta: ' + t);
}
// ---- strumenti indipendenti per le matrici ----
const pn = s => +String(s).replace(/−/g, '-');
const pf = s => { const k = String(s).replace(/−/g, '-').split('/'); return k.length === 2 ? +k[0] / +k[1] : +k[0]; };
const pm = s => s.trim().split(' ; ').map(r => r.trim().split(' ').map(pn));
const mm = (A, B) => A.map(r => B[0].map((_, j) => r.reduce((s, x, k) => s + x * B[k][j], 0)));
function leib(A) { // determinante con la definizione: somma su tutte le permutazioni, con il segno
  const n = A.length; let tot = 0; const p = [...Array(n).keys()];
  const rec = k => { if (k === n) { let inv = 0; for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) if (p[i] > p[j]) inv++; tot += (inv % 2 ? -1 : 1) * p.reduce((s, c, r) => s * A[r][c], 1); return; } for (let i = k; i < n; i++) { [p[k], p[i]] = [p[i], p[k]]; rec(k + 1); [p[k], p[i]] = [p[i], p[k]]; } };
  rec(0); return Math.abs(tot) < 1e-12 ? 0 : tot;
}
function rankMinori(A) { // il massimo k tale che una sottomatrice k × k abbia determinante non nullo
  const m = A.length, n = A[0].length, sub = (k, from, cnt) => { const out = []; const rec = (s, cur) => { if (cur.length === k) { out.push(cur.slice()); return; } for (let i = s; i < cnt; i++) { cur.push(i); rec(i + 1, cur); cur.pop(); } }; rec(0, []); return out; };
  for (let k = Math.min(m, n); k >= 1; k--) for (const rs of sub(k, 0, m)) for (const cs of sub(k, 0, n)) if (leib(rs.map(r => cs.map(c => A[r][c]))) !== 0) return k;
  return 0;
}
function invF(A) { // Gauss-Jordan in virgola mobile
  const n = A.length, M = A.map((r, i) => [...r.map(Number), ...[...Array(n).keys()].map(j => (i === j ? 1 : 0))]);
  for (let c = 0; c < n; c++) { let p = c; for (let r = c + 1; r < n; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r; if (Math.abs(M[p][c]) < 1e-12) return null; [M[c], M[p]] = [M[p], M[c]]; const d = M[c][c]; M[c] = M[c].map(x => x / d); for (let r = 0; r < n; r++) if (r !== c) { const f = M[r][c]; M[r] = M[r].map((x, j) => x - f * M[c][j]); } }
  return M.map(r => r.slice(n));
}
const rnd = n => Array.from({ length: n }, () => Array.from({ length: n }, () => Math.floor(Math.random() * 11) - 5));
function conDet(n, d) { // matrice intera «casuale» con determinante d: triangolare con diagonale (d, 1, …, 1), poi mosse che non cambiano det
  let A; do { A = Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => (i === j ? (i ? 1 : d) : j > i ? Math.floor(Math.random() * 5) - 2 : 0))); for (let t = 0; t < 6; t++) { const i = Math.floor(Math.random() * n), j = (i + 1 + Math.floor(Math.random() * (n - 1))) % n, c = Math.floor(Math.random() * 3) - 1; A[i] = A[i].map((x, k) => x + c * A[j][k]); } } while (leib(A) !== d);
  return A;
}
const tc = s => { const v = s.replace(/−/g, '-'); return +v; };
function checkFond(q) {
  const t = q.q, ans = q.o[q.a - 1]; let m;
  if (new Set(q.o).size !== 5) return fail(q, 'fond opzioni duplicate');
  if ((m = t.match(/^Il numero binario ([01]+) vale in decimale$/))) { if (parseInt(m[1], 2) !== +ans) return fail(q, 'bin2dec'); }
  else if ((m = t.match(/^Il numero decimale (\d+) in esadecimale è$/))) { if (parseInt(ans, 16) !== +m[1] || ans !== ans.toUpperCase()) return fail(q, 'dec2hex'); }
  else if ((m = t.match(/^Il numero esadecimale ([0-9A-F]+) vale in decimale$/))) { if (parseInt(m[1], 16) !== +ans) return fail(q, 'hex2dec'); }
  else if ((m = t.match(/^In complemento a due su 8 bit, −(\d+) si scrive$/))) { const v = parseInt(ans, 2); if (ans.length !== 8 || ((v + +m[1]) & 255) !== 0) return fail(q, 'c2 neg'); }
  else if ((m = t.match(/^Il pattern ([01]{8}), letto in complemento a due su 8 bit, rappresenta il numero$/))) { let v = parseInt(m[1], 2); if (v > 127) v -= 256; if (v !== tc(ans)) return fail(q, 'c2 pos'); }
  else if ((m = t.match(/^Qual è la distanza di Hamming tra ([01]+) e ([01]+)\?$/))) { let d = 0; for (let i = 0; i < m[1].length; i++) if (m[1][i] !== m[2][i]) d++; if (d !== +ans) return fail(q, 'hamming'); }
  else if ((m = t.match(/^Aggiungendo in fondo un bit di parità pari al pattern ([01]+), si ottiene$/))) { const ones = [...ans].filter(c => c === '1').length; if (!ans.startsWith(m[1]) || ans.length !== m[1].length + 1 || ones % 2 !== 0) return fail(q, 'parita'); }
  else if ((m = t.match(/^Una memoria principale ha indirizzi di (\d+) bit e celle da 1 byte\. Quante celle ha\?$/))) { if (!ans.endsWith('= ' + 2 ** +m[1])) return fail(q, 'celle'); }
  else if ((m = t.match(/^Quanti bit servono per indirizzare (\d+) celle di memoria\?$/))) { if (2 ** +ans !== +m[1]) return fail(q, 'bit indirizzi'); }
  else if ((m = t.match(/scrittura di (\d+) in base 2/))) { if (parseInt(ans, 2) !== +m[1]) return fail(q, 'base2'); }
  else return fail(q, 'fond non riconosciuta: ' + t);
}
// ---------- Programmazione: un secondo interprete del C, scritto in modo indipendente (Pratt + chiusure) ----------
function runC(src) {
  const toks = [], re = /\s+|\/\/[^\n]*|(\d+)|([A-Za-z_]\w*)|("(?:\\.|[^"\\])*")|(\+\+|--|[+\-*/%]=|==|!=|<=|>=|&&|\|\||[-+*/%<>=!&(){};,])/y;
  while (re.lastIndex < src.length) { const k = re.exec(src); if (!k) throw Error('lessico'); if (k[1]) toks.push(['n', +k[1]]); else if (k[2]) toks.push(['w', k[2]]); else if (k[3]) toks.push(['s', JSON.parse(k[3])]); else if (k[4]) toks.push(['o', k[4]]); }
  let p = 0, out = '', passi = 0; const pk = (o = 0) => toks[p + o] || ['e', ''], isO = (v, o) => pk(o)[0] === 'o' && pk(o)[1] === v, isW = (v, o) => pk(o)[0] === 'w' && pk(o)[1] === v, isT = o => ['int', 'float', 'void'].some(w => isW(w, o));
  const want = v => { if (pk()[1] !== v) throw Error('atteso ' + v + ' trovato ' + pk()[1]); p++; };
  const I = n => ({ t: 'I', v: n | 0 }), Fl = n => ({ t: 'F', v: Math.fround(n) });
  const toInt = x => (x.t === 'F' ? I(Math.trunc(x.v)) : x), get = r => { if (r.v === undefined) throw Error('non inizializzata'); return { t: r.t, v: r.v }; };
  const put = (r, x) => { if (r.t === 'P') { if (x.t !== 'P') throw Error('tipo'); r.v = x.v; } else if (r.t === 'F') r.v = Math.fround(x.v); else { if (x.t === 'P') throw Error('tipo'); r.v = toInt(x).v; } return get(r); };
  const ar = (op, a, b) => {
    if (a.t === 'P' || b.t === 'P') throw Error('puntatori');
    if (a.t === 'F' || b.t === 'F') { if (op === '%') throw Error('% float'); return Fl({ '+': a.v + b.v, '-': a.v - b.v, '*': a.v * b.v, '/': a.v / b.v }[op]); }
    if ((op === '/' || op === '%') && b.v === 0) throw Error('div 0');
    const q = a.v / b.v; return I({ '+': a.v + b.v, '-': a.v - b.v, '*': Math.imul(a.v, b.v), '/': q < 0 ? Math.ceil(q) : Math.floor(q), '%': a.v - b.v * (q < 0 ? Math.ceil(q) : Math.floor(q)) }[op]);
  };
  const tick = () => { if (++passi > 50000) throw Error('ciclo infinito?'); };
  const BP = { '=': 2, '+=': 2, '-=': 2, '*=': 2, '/=': 2, '%=': 2, '||': 4, '&&': 5, '==': 9, '!=': 9, '<': 10, '<=': 10, '>': 10, '>=': 10, '+': 12, '-': 12, '*': 13, '/': 13, '%': 13 };
  const FN = {};
  function E(min) { // restituisce { ev(env) → valore, lv(env) → cella }
    let L = pre();
    for (;;) {
      const t = pk();
      if (t[0] === 'o' && (t[1] === '++' || t[1] === '--')) { p++; const X = L, op = t[1][0]; L = { ev: e => { tick(); const r = X.lv(e), o = get(r); put(r, ar(op, o, I(1))); return o; } }; continue; }
      if (t[0] !== 'o' || !(t[1] in BP) || BP[t[1]] <= min) return L;
      const op = t[1]; p++;
      const X = L, R = E(BP[op] === 2 ? BP[op] - 1 : BP[op]);
      if (BP[op] === 2) L = { ev: e => { tick(); const r = X.lv(e), v = R.ev(e); return put(r, op === '=' ? v : ar(op[0], get(r), v)); } };
      else if (op === '&&') L = { ev: e => (X.ev(e).v && R.ev(e).v ? I(1) : I(0)) };
      else if (op === '||') L = { ev: e => (X.ev(e).v || R.ev(e).v ? I(1) : I(0)) };
      else if ('+-*/%'.includes(op)) L = { ev: e => { tick(); return ar(op, X.ev(e), R.ev(e)); } };
      else L = { ev: e => { const a = X.ev(e).v, b = R.ev(e).v; return I(op === '<' ? a < b : op === '<=' ? a <= b : op === '>' ? a > b : op === '>=' ? a >= b : op === '==' ? a === b : a !== b); } };
    }
  }
  function pre() {
    const t = pk();
    if (t[0] === 'o') {
      if (t[1] === '(' && isT(1)) { p++; const ty = pk()[1]; p++; want(')'); const X = pre(); return { ev: e => { const v = X.ev(e); return ty === 'float' ? Fl(v.v) : toInt(v); } }; }
      if (t[1] === '(') { p++; const X = E(0); want(')'); return X; }
      p++; const X = pre();
      if (t[1] === '++' || t[1] === '--') return { ev: e => { tick(); const r = X.lv(e); return put(r, ar(t[1][0], get(r), I(1))); } };
      if (t[1] === '-') return { ev: e => { const v = X.ev(e); return v.t === 'F' ? Fl(-v.v) : I(-v.v); } };
      if (t[1] === '!') return { ev: e => I(!X.ev(e).v) };
      if (t[1] === '&') return { ev: e => ({ t: 'P', v: X.lv(e) }) };
      if (t[1] === '*') { const lv = e => { const q = X.ev(e); if (q.t !== 'P') throw Error('*'); return q.v; }; return { ev: e => get(lv(e)), lv }; }
      throw Error('prefisso ' + t[1]);
    }
    p++;
    if (t[0] === 'n') return { ev: () => I(t[1]) };
    if (t[0] === 's') return { ev: () => { throw Error('stringa'); }, s: t[1] };
    if (t[0] !== 'w') throw Error('primario');
    if (isO('(')) { // chiamata
      p++; const args = []; while (!isO(')')) { args.push(E(1)); if (isO(',')) p++; } p++;
      if (t[1] === 'printf') return { ev: e => { tick(); let k = 1; out += args[0].s.replace(/%d/g, () => { const v = args[k++].ev(e); if (v.t !== 'I') throw Error('%d non intero'); return String(v.v); }); if (k !== args.length) throw Error('argomenti printf'); return I(0); } };
      return { ev: e => {
        tick(); const f = FN[t[1]], env = Object.create(null); if (!f || f.ps.length !== args.length) throw Error('funzione');
        f.ps.forEach((pp, i) => { const c = { t: pp.ptr ? 'P' : 'I', v: undefined }; put(c, args[i].ev(e)); env[pp.n] = c; });
        const r = f.body(env); if (f.ret === 'void') return I(0); if (!r) throw Error('return'); return toInt(r.v);
      } };
    }
    const n = t[1], lv = e => { if (!(n in e)) throw Error('non dichiarata ' + n); return e[n]; };
    return { ev: e => get(lv(e)), lv };
  }
  function decl() { // dopo il tipo: [*]nome [= expr] {, ...}
    const ty = pk()[1]; p++; const ds = [];
    for (;;) { let ptr = false; if (isO('*')) { p++; ptr = true; } const n = pk()[1]; p++; let X = null; if (isO('=')) { p++; X = E(1); } ds.push([n, ptr, X]); if (!isO(',')) break; p++; }
    return e => { for (const [n, ptr, X] of ds) { const c = { t: ptr ? 'P' : ty === 'float' ? 'F' : 'I', v: undefined }; if (X) put(c, X.ev(e)); e[n] = c; } };
  }
  function S() { // istruzione → funzione(env) che restituisce { v } se c'è un return
    tick();
    if (isO('{')) { p++; const b = []; while (!isO('}')) b.push(S()); p++; return e => { const f = Object.create(e); for (const s of b) { const r = s(f); if (r) return r; } }; }
    if (isT()) { const d = decl(); want(';'); return e => { d(e); }; }
    if (isW('if')) { p++; want('('); const c = E(0); want(')'); const a = S(); let b = null; if (isW('else')) { p++; b = S(); } return e => (c.ev(e).v ? a(Object.create(e)) : b ? b(Object.create(e)) : undefined); }
    if (isW('while')) { p++; want('('); const c = E(0); want(')'); const b = S(); return e => { while (c.ev(e).v) { tick(); const r = b(Object.create(e)); if (r) return r; } }; }
    if (isW('do')) { p++; const b = S(); want('while'); want('('); const c = E(0); want(')'); want(';'); return e => { do { tick(); const r = b(Object.create(e)); if (r) return r; } while (c.ev(e).v); }; }
    if (isW('for')) {
      p++; want('('); let init = null; if (isT()) init = decl(); else if (!isO(';')) { const x = E(0); init = e => { x.ev(e); }; } want(';');
      const c = isO(';') ? null : E(0); want(';'); const st = isO(')') ? null : E(0); want(')'); const b = S();
      return e => { const f = Object.create(e); if (init) init(f); while (!c || c.ev(f).v) { tick(); const r = b(Object.create(f)); if (r) return r; if (st) st.ev(f); } };
    }
    if (isW('return')) { p++; const x = isO(';') ? null : E(0); want(';'); return e => ({ v: x ? x.ev(e) : I(0) }); }
    const x = E(0); want(';'); return e => { x.ev(e); };
  }
  const top = [];
  while (p < toks.length) {
    if (isT() && pk(1)[0] === 'w' && isO('(', 2)) {
      const ret = pk()[1], n = pk(1)[1]; p += 3; const ps = [];
      if (isW('void') && isO(')', 1)) p++;
      while (!isO(')')) { p++; let ptr = false; if (isO('*')) { p++; ptr = true; } ps.push({ n: pk()[1], ptr }); p++; if (isO(',')) p++; }
      p++; FN[n] = { ret, ps, body: S() };
    } else top.push(S());
  }
  const env = Object.create(null);
  if (FN.main) FN.main.body(env); else for (const s of top) if (s(env)) break;
  return out.replace(/\s+/g, ' ').trim();
}
// casi noti (semantica del C99): servono a controllare entrambi gli interpreti
const GOLD = [
  ['int a = -17, b = 5;\nprintf("%d %d\\n", a / b, a % b);', '-3 -2'],
  ['int a = 7, b = 4, m = 2;\nint x = (float)a / b * m;\nint y = (float)(a / b) * m;\nprintf("%d %d\\n", x, y);', '3 2'],
  ['int a = 19, b = 8, m = 5;\nint y = a / (float)b * m;\nprintf("%d\\n", y);', '11'],
  ['int a = 5, b;\nb = a++ * 2;\nprintf("%d %d\\n", a, b);', '6 10'],
  ['int a = 5, b;\nb = ++a * 2;\nprintf("%d %d\\n", a, b);', '6 12'],
  ['int a = 0, b = 3;\nint r = a && b++;\nprintf("%d %d\\n", r, b);', '0 3'],
  ['int a = 2, b = 3;\nint r = a || ++b;\nprintf("%d %d\\n", r, b);', '1 3'],
  ['int a = 1, b = 5;\nint r = a > 0 || (b = 0);\nprintf("%d %d\\n", r, b);', '1 5'],
  ['int a = 1, b = 5;\nint r = a > 3 || (b = 0);\nprintf("%d %d\\n", r, b);', '0 0'],
  ['int i, c = 0;\nfor (i = 0; i < 5; i++)\n    c += 2;\nprintf("%d %d\\n", i, c);', '5 10'],
  ['int s = 0;\nfor (int i = 1; i <= 4; i++)\n    s += i;\nprintf("%d\\n", s);', '10'],
  ['int i = 10, c = 0;\ndo {\n    i += 3;\n    c++;\n} while (i < 5);\nprintf("%d %d\\n", i, c);', '13 1'],
  ['int n = 37, c = 0;\nwhile (n > 0) {\n    n = n / 2;\n    c++;\n}\nprintf("%d %d\\n", n, c);', '0 6'],
  ['int x = 1, y = 2, z = 9;\nint k = x + y + z / 3;\nprintf("%d\\n", k);', '6'],
  ['int a = -7;\na %= 3;\nprintf("%d\\n", a);', '-1'],
  ['int a = 9, b = 9;\na = b++ + 4;\nb /= 2;\na %= 5;\nprintf("%d %d\\n", a, b);', '3 5'],
  ['int a = 4, b = 9, t;\nt = a;\na = b;\nb = t;\nprintf("%d %d\\n", a, b);', '9 4'],
  ['void f(int x) {\n    x = 9;\n}\nint main(void) {\n    int a = 1;\n    f(a);\n    printf("%d\\n", a);\n    return 0;\n}', '1'],
  ['void f(int *p) {\n    *p = 9;\n}\nint main(void) {\n    int a = 1;\n    f(&a);\n    printf("%d\\n", a);\n    return 0;\n}', '9'],
  ['int a = 3;\nint *p = &a;\n*p += 2;\na = a * 2;\nprintf("%d %d\\n", a, *p);', '10 10'],
];
for (const [src, exp] of GOLD) {
  let a, b; try { a = GEN._t.cRun(src).out.replace(/\s+/g, ' ').trim(); } catch (e) { a = 'ERRORE ' + e.message; } try { b = runC(src); } catch (e) { b = 'ERRORE ' + e.message; }
  if (a !== exp || b !== exp) fail({ q: src, gen: a, test: b }, 'caso noto del C: atteso ' + exp);
}
// le «misconcezioni» del generatore fanno davvero l'errore che dichiarano
const MIS = [[GOLD[0][0], { realDiv: true }, '-3.4 -2'], [GOLD[0][0], { floorDiv: true }, '-4 3'], [GOLD[5][0], { noShort: true }, '0 4'], [GOLD[3][0], { swapIncr: true }, '6 12'], [GOLD[17][0], { byRef: true }, '9'], [GOLD[18][0], { ptrCopy: true }, '1'], [GOLD[1][0], { castNone: true }, '2 2']];
for (const [src, f, exp] of MIS) { const o = GEN._t.cRun(src, f).out.replace(/\s+/g, ' ').trim(); if (o !== exp) fail({ q: src, flags: f, out: o }, 'flag di errore tipico'); }
const progKinds = {};
function checkProg(q) {
  const lines = q.q.split('\n'), ans = q.o[q.a - 1];
  if (new Set(q.o).size !== 5) return fail(q, 'prog opzioni duplicate');
  if (!/^Che cosa stampa il seguente (frammento di codice|programma) C\?$/.test(lines[0])) return fail(q, 'prog intestazione');
  if (!lines.slice(1).every(l => /^`.+`$/.test(l) && !l.slice(1, -1).includes('`'))) return fail(q, 'prog riga di codice non racchiusa');
  const src = lines.slice(1).map(l => l.slice(1, -1).replace(/\u00a0/g, ' ')).join('\n');
  let out; try { out = runC(src); } catch (e) { return fail(q, 'prog: il secondo interprete non esegue il codice: ' + e.message); }
  if (out !== ans) return fail(q, `prog: stampa ${out}, non ${ans}`);
  if (/\*\*/.test(src)) return fail(q, 'prog: ** verrebbe preso per grassetto');
  progKinds[q.theme + ' / ' + q.args[0]] = (progKinds[q.theme + ' / ' + q.args[0]] || 0) + 1;
}
// temi ammessi per materia (devono coincidere con quelli registrati nella build)
const TEMI = {
  'Matematica discreta': ['Permutazioni', 'Aritmetica modulare e ℤ_N', 'Binario', 'Combinatoria', 'Funzioni', 'Insiemi'],
  'Algebra lineare': ['Numeri complessi', 'Coniugato e modulo', 'Potenze e radici', 'Matrici', 'Rango', 'Determinante', 'Matrice inversa'],
  'Fondamenti Info': ['Rappresentazione binaria', 'Compressione ed errori', 'Circuiti e memoria', 'Binario'],
  'Programmazione': ['Operatori', 'Controllo di flusso', 'Variabili e assegnamento', 'Funzioni e parametri', 'Puntatori'],
};
let na = 0, nf = 0, np = 0;
const temaOk = (q, mat) => { if (!TEMI[mat].includes(q.theme)) fail(q, 'tema inatteso per ' + mat + ': ' + q.theme); if (q.m !== mat) fail(q, 'materia mancante'); };
for (let i = 0; i < 6000; i++) { const q = GEN.make('Algebra lineare'); if (!q) { fail({ q: 'null' }, 'alg null'); continue; } na++; temaOk(q, 'Algebra lineare'); checkAlg(q); }
for (let i = 0; i < 4000; i++) { const q = GEN.make('Fondamenti Info'); if (!q) { fail({ q: 'null' }, 'fond null'); continue; } nf++; temaOk(q, 'Fondamenti Info'); checkFond(q); }
for (let i = 0; i < 6000; i++) { const q = GEN.make('Programmazione'); if (!q) { fail({ q: 'null' }, 'prog null'); continue; } np++; temaOk(q, 'Programmazione'); checkProg(q); }
for (let i = 0; i < 500; i++) temaOk(GEN.make('Matematica discreta'), 'Matematica discreta');
// ogni generatore deve produrre domande (un modello di codice che non compila darebbe sempre null, in silenzio)
for (const [mat, ms] of Object.entries(GEN._t.BYMAT)) for (const f of new Set(ms)) { let ok = 0; for (let i = 0; i < 200; i++) if (f()) ok++; if (ok < 150) fail({ q: f.name }, `${mat}: ${f.name} produce solo ${ok}/200 domande`); }
// copertura: con i soli temi coperti la generazione rispetta il filtro
{ const cov = new Set(['Puntatori']); for (let i = 0; i < 300; i++) { const q = GEN.make('Programmazione', cov); if (!q || q.theme !== 'Puntatori') { fail(q || { q: 'null' }, 'filtro copertura'); break; } } }
console.log('Programmazione:', progKinds);
console.log(`Algebra: ${na}, Fondamenti: ${nf}, Programmazione: ${np} domande generate; errori totali ${bad}; Programmazione generabile: ${GEN.disponibile('Programmazione')}`);
process.exit(bad ? 1 : 0);
