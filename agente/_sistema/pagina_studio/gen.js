/* Generatore di domande d'esame: Matematica discreta (permutazioni, aritmetica modulare, ℤ_N, combinatoria, insiemi, funzioni),
   Algebra lineare (numeri complessi, matrici, rango, determinante, inversa), Fondamenti (binario, Hamming, memoria),
   Programmazione («Che cosa stampa?» calcolato da un mini-interprete del C).
   Ogni domanda ha 5 opzioni, una sola corretta, e una spiegazione. Collaudo: node test_gen.js */
const GEN = (() => {
  const ri = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  const pick = a => a[ri(0, a.length - 1)];
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = ri(0, i); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const gcd = (a, b) => (b ? gcd(b, a % b) : Math.abs(a));
  const lcm = (a, b) => (a / gcd(a, b)) * b;
  const phi = n => { let r = n, m = n; for (let p = 2; p * p <= m; p++) if (m % p === 0) { while (m % p === 0) m /= p; r -= r / p; } if (m > 1) r -= r / m; return r; };
  const mod = (a, n) => ((a % n) + n) % n;
  const powmod = (b, e, n) => { let r = 1, x = mod(b, n); while (e > 0) { if (e & 1) r = (r * x) % n; x = (x * x) % n; e = Math.floor(e / 2); } return r; };
  const inv = (a, n) => { for (let x = 1; x < n; x++) if ((a * x) % n === 1) return x; return null; };
  const factorial = n => (n <= 1 ? 1 : n * factorial(n - 1));
  const C = (n, k) => { let r = 1; for (let i = 1; i <= k; i++) r = (r * (n - k + i)) / i; return Math.round(r); };

  /* costruisce la domanda: la risposta giusta e distrattori (unici, diversi dalla giusta) */
  function build(o) {
    const seen = new Set([o.correct]);
    const wrong = [];
    for (const d of o.wrong) if (!seen.has(d)) { seen.add(d); wrong.push(d); }
    let guard = 0;
    while (wrong.length < 4 && guard++ < 200) { const d = o.filler(); if (!seen.has(d)) { seen.add(d); wrong.push(d); } }
    if (wrong.length < 4) return null;
    const opts = shuffle([o.correct, ...wrong.slice(0, 4)]);
    return { id: 'gen-' + Date.now().toString(36) + '-' + ri(1000, 9999), prova: 'Esercizio generato', args: [o.kind], theme: o.theme, q: o.q, o: opts, a: opts.indexOf(o.correct) + 1, s: o.s, gen: 1 };
  }

  /* ---------- permutazioni ---------- */
  const compose = (p, q) => q.map(x => p[x]); // (p∘q)(i) = p[q[i]], indici 0..n-1
  function cycleToPerm(cyc, n) { const p = [...Array(n).keys()]; for (let i = 0; i < cyc.length; i++) p[cyc[i]] = cyc[(i + 1) % cyc.length]; return p; }
  function cyclesOf(p) { const seen = new Set(), out = []; for (let i = 0; i < p.length; i++) { if (seen.has(i)) continue; const c = []; let x = i; while (!seen.has(x)) { seen.add(x); c.push(x); x = p[x]; } if (c.length > 1) out.push(c); } return out; }
  const cycTxt = cs => (cs.length ? cs.map(c => '(' + c.map(x => x + 1).join(' ') + ')').join('') : '(id)');
  const typeOf = p => cyclesOf(p).map(c => c.length).sort((a, b) => b - a);
  const typeTxt = t => '(' + (t.length ? t.join(', ') : '1') + ')';
  const orderOf = p => typeOf(p).reduce((a, l) => lcm(a, l), 1);
  const parityOf = p => (typeOf(p).reduce((s, l) => s + l - 1, 0) % 2 === 0 ? 'pari' : 'dispari');
  function randomProduct() {
    for (;;) {
      const n = ri(6, 9), k = ri(2, 3), cycs = [], perms = [];
      for (let i = 0; i < k; i++) { const len = ri(2, 4), pool = shuffle([...Array(n).keys()]).slice(0, len); cycs.push(pool); perms.push(cycleToPerm(pool, n)); }
      let p = perms[k - 1]; for (let i = k - 2; i >= 0; i--) p = compose(perms[i], p); // da destra a sinistra
      let wrongOrder = perms[0]; for (let i = 1; i < k; i++) wrongOrder = compose(perms[i], wrongOrder);
      if (cyclesOf(p).length >= 1) return { n, cycs, p, wrongOrder };
    }
  }
  const prodTxt = cycs => cycs.map(c => '(' + c.map(x => x + 1).join(' ') + ')').join('');
  const invP = p => { const q = []; p.forEach((x, i) => { q[x] = i; }); return q; };

  function q_perm() {
    const { n, cycs, p, wrongOrder } = randomProduct();
    const t = pick(['dec', 'tipo', 'pp', 'pot']);
    const head = `Sia π = ${prodTxt(cycs)} ∈ S${sub(n)} (le permutazioni si compongono da destra a sinistra).`;
    const dec = `Da destra a sinistra si ottiene π = ${cycTxt(cyclesOf(p))}.`;
    if (t === 'dec') {
      const correct = cycTxt(cyclesOf(p));
      // inverse in forma canonica (girare a mano un 2-ciclo darebbe la stessa permutazione scritta in un altro modo)
      const wrong = [cycTxt(cyclesOf(wrongOrder)), cycTxt(cyclesOf(invP(wrongOrder))), cycTxt(cyclesOf(invP(p)))];
      const filler = () => { const q = shuffle([...Array(n).keys()]); return cycTxt(cyclesOf(compose(cycleToPerm(q.slice(0, 3), n), cycleToPerm(q.slice(3, 5), n)))); };
      return build({ kind: 'permutazioni', theme: 'Permutazioni', q: head + ' La decomposizione di π in cicli disgiunti è:', correct, wrong, filler, s: dec + ' Un errore frequente è comporre da sinistra a destra, che dà ' + cycTxt(cyclesOf(wrongOrder)) + '.' });
    }
    if (t === 'tipo') {
      const ty = typeOf(p), correct = typeTxt(ty);
      const wrong = [typeTxt(typeOf(wrongOrder)), typeTxt(cycs.map(c => c.length).sort((a, b) => b - a)), typeTxt(ty.concat([2])), typeTxt(ty.map(x => x + 1))];
      const filler = () => typeTxt([ri(2, 5), ri(2, 4)].sort((a, b) => b - a));
      return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: head + ' Il tipo di π (i punti fissi non si contano) è:', correct, wrong, filler, s: dec + ' Il tipo è la lista delle lunghezze dei cicli: ' + typeTxt(ty) + '.' });
    }
    if (t === 'pp') {
      const per = orderOf(p), par = parityOf(p), other = par === 'pari' ? 'dispari' : 'pari';
      const correct = `è ${par} ed ha periodo ${per}`;
      const wrong = [`è ${other} ed ha periodo ${per}`, `è ${par} ed ha periodo ${typeOf(p).reduce((a, b) => a + b, 0)}`, `è ${other} ed ha periodo ${Math.max(...typeOf(p))}`, `è ${par} ed ha periodo ${Math.max(...typeOf(p))}`];
      const filler = () => `è ${pick(['pari', 'dispari'])} ed ha periodo ${ri(2, 30)}`;
      return build({ kind: 'parita', theme: 'Permutazioni', q: head + ' Allora π', correct, wrong, filler, s: dec + ` Il periodo è l'mcm delle lunghezze dei cicli (${typeTxt(typeOf(p))}) = ${per}; la parità si ottiene da Σ(lunghezza − 1) = ${typeOf(p).reduce((s, l) => s + l - 1, 0)}, quindi π è ${par}.` });
    }
    const x = ri(0, n - 1), k = ri(5, 40);
    let r = x; for (let i = 0; i < k; i++) r = p[r];
    const correct = String(r + 1);
    const wrong = [...Array(n).keys()].map(v => String(v + 1));
    return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: head + ` Allora π${sup(k)}(${x + 1}) =`, correct, wrong: shuffle(wrong), filler: () => String(ri(1, n)), s: dec + ` Il periodo è ${orderOf(p)}, quindi π${sup(k)} = π${sup(k % orderOf(p))}; seguendo la freccia da ${x + 1} si arriva a ${r + 1}.` });
  }

  /* ---------- aritmetica modulare ---------- */
  function q_cong() {
    const n = ri(20, 90); let a, b, d;
    do { a = ri(2, n - 1); d = gcd(a, n); } while (d === 1 && Math.random() < 0.6);
    b = Math.random() < 0.65 ? d * ri(1, Math.max(1, Math.floor((n - 1) / d))) : ri(1, n - 1);
    b = mod(b, n); if (b === 0) b = d;
    const sol = b % d === 0 ? d : 0;
    const correct = String(sol);
    const wrong = [0, 1, d, d + 1, 2 * d, Math.max(1, d - 1)].map(String);
    return build({ kind: 'aritmetica-modulare', theme: 'Aritmetica modulare e ℤ_N', q: `Quante soluzioni modulo ${n} ha la congruenza ${a}X ≡ ${b} mod ${n}?`, correct, wrong, filler: () => String(ri(0, 8)),
      s: `MCD(${a}, ${n}) = ${d}. ${b % d === 0 ? `Poiché ${d} divide ${b}, ci sono esattamente ${d} soluzioni modulo ${n}.` : `Poiché ${d} non divide ${b}, la congruenza non ha soluzioni.`}` });
  }
  function q_inverso() {
    let n, a; do { n = ri(15, 80); a = ri(2, n - 1); } while (gcd(a, n) !== 1);
    const x = inv(a, n), correct = String(x);
    const wrong = [n - x, n - a, mod(a + 1, n), Math.floor(n / 2)].map(String);
    return build({ kind: 'Z_N-moltiplicativo', theme: 'Aritmetica modulare e ℤ_N', q: `In ℤ${sub(n)} l'inverso moltiplicativo di [${a}] è`, correct, wrong, filler: () => String(ri(2, n - 1)), s: `${a}·${x} = ${a * x} = ${Math.floor((a * x) / n)}·${n} + 1 ≡ 1 mod ${n}, e MCD(${a}, ${n}) = 1, quindi [${a}]⁻¹ = [${x}].` });
  }
  function q_phi() {
    const ps = [2, 3, 5, 7, 11, 13]; let n;
    do { const k = ri(2, 3), f = shuffle(ps).slice(0, k); n = f.reduce((m, p) => m * (Math.random() < 0.3 ? p * p : p), 1); } while (n < 30 || n > 400);
    const target = pick(['phi', 'gen', 'inv']), v = phi(n), correct = String(v);
    const wrong = [n - 1, n / 2, v + 2, v - 2, Math.round(n / 3), v * 2].filter(x => Number.isInteger(x) && x > 0).map(String);
    const fa = (() => { let m = n, parts = []; for (let p = 2; p * p <= m; p++) if (m % p === 0) { let e = 0; while (m % p === 0) { m /= p; e++; } parts.push(e > 1 ? `${p}${sup(e)}` : `${p}`); } if (m > 1) parts.push(String(m)); return parts.join('·'); })();
    const base = `${n} = ${fa}, quindi φ(${n}) = ${v}.`;
    if (target === 'phi') return build({ kind: 'Z_N-moltiplicativo', theme: 'Aritmetica modulare e ℤ_N', q: `Sia φ la funzione di Eulero. Allora φ(${n}) =`, correct, wrong, filler: () => String(ri(8, n)), s: base });
    if (target === 'gen') return build({ kind: 'generatori', theme: 'Aritmetica modulare e ℤ_N', q: `Il numero dei generatori del gruppo additivo ℤ${sub(n)} è`, correct, wrong, filler: () => String(ri(8, n)), s: `I generatori di ℤ_N sono le classi coprime con N. ${base}` });
    return build({ kind: 'Z_N-moltiplicativo', theme: 'Aritmetica modulare e ℤ_N', q: `Il numero delle classi invertibili in (ℤ${sub(n)}, ·) è`, correct, wrong, filler: () => String(ri(8, n)), s: `Le classi invertibili sono quelle coprime con N. ${base}` });
  }
  function q_nongen() {
    const n = pick([60, 70, 72, 84, 90, 105, 80, 66, 50, 120]);
    const coprime = [], not = [];
    for (let k = 2; k < n; k++) (gcd(k, n) === 1 ? coprime : not).push(k);
    const bad = pick(not), good = shuffle(coprime).slice(0, 4);
    return build({ kind: 'generatori', theme: 'Aritmetica modulare e ℤ_N', q: `Quale delle seguenti classi non genera (ℤ${sub(n)}, +)?`, correct: `[${bad}]`, wrong: good.map(g => `[${g}]`), filler: () => `[${pick(coprime)}]`, s: `[k] genera ℤ_${n} se e solo se MCD(k, ${n}) = 1. Qui MCD(${bad}, ${n}) = ${gcd(bad, n)} ≠ 1, mentre gli altri valori sono coprimi con ${n}.` });
  }
  function q_pow() {
    const n = pick([7, 11, 13, 17, 19, 23, 25, 26, 27, 29, 31]); let a;
    do { a = ri(2, n - 1); } while (gcd(a, n) !== 1);
    const e = ri(40, 400), v = powmod(a, e, n), ord = phi(n);
    return build({ kind: 'aritmetica-modulare', theme: 'Aritmetica modulare e ℤ_N', q: `In ℤ${sub(n)} la classe [${a}]${sup(e)} è`, correct: `[${v}]`, wrong: [powmod(a, e % ord + 1, n), powmod(a, e, n) + 1, mod(a * (e % n), n), mod(e, n), powmod(a, ord - e % ord, n)].map(x => `[${mod(x, n)}]`), filler: () => `[${ri(1, n - 1)}]`,
      s: `Per Eulero [${a}]${sup(ord)} = [1] (φ(${n}) = ${ord}), quindi l'esponente si riduce modulo ${ord}: ${e} ≡ ${e % ord}, e [${a}]${sup(e % ord)} = [${v}].` });
  }
  function q_base2() {
    const v = ri(40, 200), bin = v.toString(2), flip = i => { const b = bin.split(''); b[i] = b[i] === '1' ? '0' : '1'; return b.join(''); };
    const wrong = [flip(ri(0, bin.length - 1)), flip(bin.length - 1), flip(ri(0, bin.length - 2)), (v + ri(1, 9)).toString(2), (v - ri(1, 9)).toString(2)];
    return build({ kind: 'base-2', theme: 'Binario', q: `Quale delle seguenti è la scrittura di ${v} in base 2?`, correct: bin, wrong, filler: () => ri(40, 200).toString(2), s: `${v} = ${bin.split('').map((c, i) => (c === '1' ? 2 ** (bin.length - 1 - i) : null)).filter(x => x !== null).join(' + ')} = ${bin}₂.` });
  }
  function q_conteggio() {
    const n1 = ri(4, 12), n2 = ri(4, 12), r = ri(2, Math.min(4, n1 - 1)), s = ri(2, Math.min(4, n2 - 1));
    const correct = `C(${n1}, ${r}) · C(${n2}, ${s})`;
    const wrong = [`C(${n1}, ${r}) + C(${n2}, ${s})`, `C(${n1 + n2}, ${r + s})`, `C(${n1}, ${s}) · C(${n2}, ${r})`, `(${n1}!/${r}!) · (${n2}!/${s}!)`];
    return build({ kind: 'combinazioni', theme: 'Combinatoria', q: `Siano A e B insiemi disgiunti con |A| = ${n1} e |B| = ${n2}. Quanti sono i sottoinsiemi di A ∪ B formati da ${r} elementi di A e ${s} di B?`, correct, wrong, filler: () => `C(${ri(5, 20)}, ${ri(2, 5)})`, s: `Si scelgono gli ${r} elementi di A in C(${n1}, ${r}) modi e, indipendentemente, i ${s} di B in C(${n2}, ${s}): principio moltiplicativo. Valore: ${C(n1, r) * C(n2, s)}.` });
  }
  function q_dispos() {
    const k = ri(3, 6), m = ri(4, 9), t = pick(['rip', 'sem']);
    if (t === 'rip') return build({ kind: 'disposizioni', theme: 'Combinatoria', q: `${k} amici ordinano ciascuno una pizza scegliendo tra ${m} tipi (anche uguali). Quanti sono gli ordini possibili?`, correct: `${m}${sup(k)}`, wrong: [`${k}${sup(m)}`, `${m}!/${m - k > 0 ? m - k : 1}!`, `C(${m}, ${k})`, `${m}·${k}`], filler: () => `${ri(2, 9)}${sup(ri(2, 7))}`, s: `Ognuno sceglie indipendentemente tra ${m} tipi: ${m}${sup(k)} = ${m ** k}.` });
    const kk = Math.min(k, m - 1);
    return build({ kind: 'disposizioni', theme: 'Combinatoria', q: `In quanti modi si possono far sedere ${kk} persone in una fila di ${m} sedie?`, correct: `${m}!/${m - kk}!`, wrong: [`${m}${sup(kk)}`, `${kk}!`, `C(${m}, ${kk})`, `${m}!`], filler: () => `${ri(5, 12)}!/${ri(2, 4)}!`, s: `Sono disposizioni semplici: ${m}·${m - 1}·…·${m - kk + 1} = ${m}!/${m - kk}!.` });
  }

  /* ---------- permutazioni: σ ∘ π (prima π, poi σ), tipo, periodo, conteggi in Sₙ ---------- */
  const permOf = (cs, n) => cs.reduce((p, c) => compose(cycleToPerm(c, n), p), [...Array(n).keys()]);
  function randCycles(n) { // 1 o 2 cicli disgiunti, lunghezze 2..4
    const pool = shuffle([...Array(n).keys()]), k = ri(1, 2), cs = []; let at = 0;
    for (let t = 0; t < k; t++) { const len = ri(2, 4); if (at + len > n) break; cs.push(pool.slice(at, at + len)); at += len; }
    return cs;
  }
  function q_sigmapi() {
    let n, cs, cp, S, P, SP;
    do { n = ri(5, 8); cs = randCycles(n); cp = randCycles(n); S = permOf(cs, n); P = permOf(cp, n); SP = compose(S, P); } while (!cyclesOf(SP).length);
    const PS = compose(P, S), t = pick(['dec', 'dec', 'val', 'tp']), K = 'Permutazioni';
    const head = `Siano σ = ${prodTxt(cs)} e π = ${prodTxt(cp)} in S${sub(n)}.`;
    const dec = `σ ∘ π si legge da destra a sinistra: a ogni numero si applica prima π, poi σ. Si ottiene σ ∘ π = ${cycTxt(cyclesOf(SP))}.`;
    if (t === 'dec') return build({ kind: 'permutazioni', theme: K, q: head + ' La decomposizione in cicli disgiunti di σ ∘ π (si applica prima π, poi σ) è:', correct: cycTxt(cyclesOf(SP)),
      wrong: [cycTxt(cyclesOf(PS)), cycTxt(cyclesOf(invP(SP))), cycTxt(cyclesOf(invP(PS))), cycTxt(cyclesOf(compose(SP, SP)))], filler: () => cycTxt(cyclesOf(permOf(randCycles(n), n))),
      s: dec + ` L'errore tipico è applicare prima σ: si otterrebbe π ∘ σ = ${cycTxt(cyclesOf(PS))}.` });
    if (t === 'val') {
      const moved = [...Array(n).keys()].filter(x => SP[x] !== x), x = pick(moved);
      return build({ kind: 'permutazioni', theme: K, q: head + ` Allora (σ ∘ π)(${x + 1}) =`, correct: String(SP[x] + 1), wrong: [PS[x], S[x], P[x], invP(SP)[x], x].map(v => String(v + 1)), filler: () => String(ri(1, n)),
        s: `Si applica prima π, poi σ: π(${x + 1}) = ${P[x] + 1} e σ(${P[x] + 1}) = ${SP[x] + 1}. Applicando per prima σ si otterrebbe (π ∘ σ)(${x + 1}) = ${PS[x] + 1}.` });
    }
    const ty = typeOf(SP), per = orderOf(SP), f = (tt, p) => `tipo ${typeTxt(tt)}, periodo ${p}`, both = typeOf(S).concat(typeOf(P)).sort((a, b) => b - a);
    return build({ kind: 'cicli-tipo-periodo', theme: K, q: head + ' Il tipo e il periodo di σ ∘ π (si applica prima π, poi σ) sono:', correct: f(ty, per),
      wrong: [f(ty, ty.reduce((a, b) => a + b, 0)), f(ty, ty.reduce((a, b) => a * b, 1)), f(both, per), f(ty, Math.max(...ty) + 1), f(both, both.reduce((a, l) => lcm(a, l), 1))], filler: () => f([ri(2, 6)], ri(2, 12)),
      s: dec + ` Il tipo è la lista delle lunghezze dei cicli, ${typeTxt(ty)}, e il periodo è il loro mcm: ${per}.` });
  }
  function tipiDi(n) { // tutti i tipi di Sₙ diversi dall'identità: lunghezze ≥ 2 in ordine decrescente, somma ≤ n
    const out = [], rec = (left, max, cur) => { if (cur.length) out.push(cur.slice()); for (let l = Math.min(max, left); l >= 2; l--) { cur.push(l); rec(left - l, l, cur); cur.pop(); } };
    rec(n, n, []); return out;
  }
  const mcmL = ty => ty.reduce((a, l) => lcm(a, l), 1);
  const molt = ty => { const m = {}; ty.forEach(l => { m[l] = (m[l] || 0) + 1; }); return Object.values(m); };
  const contaTipo = (ty, n) => factorial(n) / (ty.reduce((a, b) => a * b, 1) * molt(ty).reduce((a, m) => a * factorial(m), 1) * factorial(n - ty.reduce((a, b) => a + b, 0)));
  function q_tipoconta() {
    const n = ri(4, 8), tipi = tipiDi(n).filter(t => t.length <= 3 && Math.max(...t) <= 5), ty = pick(tipi), fixed = n - ty.reduce((a, b) => a + b, 0), v = contaTipo(ty, n);
    const pL = ty.reduce((a, b) => a * b, 1), pM = molt(ty).reduce((a, m) => a * factorial(m), 1), nf = factorial(n);
    const den = [...ty.map(String), ...molt(ty).filter(m => m > 1).map(m => m + '!'), ...(fixed > 1 ? [fixed + '!'] : [])].join('·');
    return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: `Quante sono le permutazioni di tipo ${typeTxt(ty)} in S${sub(n)}?`, correct: String(v),
      wrong: [nf / (pL * factorial(fixed)), nf / (pL * pM), nf / (pM * factorial(fixed)), nf / pL, nf / factorial(fixed), C(n, n - fixed)].filter(x => Number.isInteger(x)).map(String), filler: () => String(Math.random() < 0.5 ? v * ri(2, 4) : v + ri(1, 30)),
      s: `Si mettono in fila i ${n} numeri (${n}! modi) e si riempiono i cicli nell'ordine. Ogni ciclo di lunghezza ℓ si scrive in ℓ modi (si può partire da uno qualunque dei suoi elementi)${pM > 1 ? ', i cicli della stessa lunghezza si possono scambiare tra loro' : ''}${fixed > 1 ? ` e i ${fixed} punti fissi si possono mettere in qualunque ordine` : ''}: ${n}!/(${den}) = ${v}.` });
  }
  function q_periodo() {
    const t = pick(['tipo', 'tipo', 'max', 'conta']);
    if (t === 'tipo') {
      let ty; do { ty = Array.from({ length: ri(2, 3) }, () => ri(2, 6)).sort((a, b) => b - a); } while (ty.reduce((a, b) => a + b, 0) > 11);
      const n = ty.reduce((a, b) => a + b, 0) + ri(0, 2), v = mcmL(ty);
      return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: `Una permutazione di S${sub(n)} ha tipo ${typeTxt(ty)}. Il suo periodo è`, correct: String(v),
        wrong: [ty.reduce((a, b) => a * b, 1), ty.reduce((a, b) => a + b, 0), Math.max(...ty), n, ty.reduce((a, b) => a * b, 1) / gcd(ty[0], ty[1])].map(String), filler: () => String(ri(2, 40)),
        s: `Il periodo è il minimo comune multiplo delle lunghezze dei cicli: mcm(${ty.join(', ')}) = ${v}.` });
    }
    if (t === 'max') {
      const n = ri(5, 8), tipi = tipiDi(n), vals = [...new Set(tipi.map(mcmL))].sort((a, b) => b - a), v = vals[0], best = tipi.find(tt => mcmL(tt) === v);
      return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: `Qual è il periodo massimo di un elemento di S${sub(n)}?`, correct: String(v),
        wrong: [n, vals[1], n - 1, factorial(n), n * (n - 1)].map(String), filler: () => String(ri(2, 40)),
        s: `Il periodo è l'mcm delle lunghezze dei cicli, con somma delle lunghezze al più ${n}. Il massimo si ottiene con il tipo ${typeTxt(best)}: mcm(${best.join(', ')}) = ${v} (un solo ciclo di lunghezza ${n} dà solo ${n}).` });
    }
    const n = ri(4, 7), tipi = tipiDi(n), k = pick([...new Set(tipi.map(mcmL))]), giusti = tipi.filter(tt => mcmL(tt) === k), v = giusti.reduce((a, tt) => a + contaTipo(tt, n), 0);
    const somma = f => tipi.filter(f).reduce((a, tt) => a + contaTipo(tt, n), 0);
    return build({ kind: 'cicli-tipo-periodo', theme: 'Permutazioni', q: `Quanti elementi di periodo ${k} ci sono in S${sub(n)}?`, correct: String(v),
      wrong: [somma(tt => tt.length === 1 && tt[0] === k), somma(tt => Math.max(...tt) === k), somma(tt => tt.includes(k)), factorial(n) / k, somma(tt => k % mcmL(tt) === 0)].filter(x => Number.isInteger(x) && x > 0).map(String), filler: () => String(v + ri(1, 30)),
      s: `Hanno periodo ${k} le permutazioni il cui tipo ha mcm delle lunghezze uguale a ${k}: ${giusti.map(tt => `${typeTxt(tt)} → ${contaTipo(tt, n)}`).join('; ')}. In totale ${v}.` });
  }

  /* ---------- combinatoria: valori numerici (coefficienti binomiali, combinazioni con ripetizione, disposizioni) ---------- */
  const pw = (x, e) => (e === 1 ? x : x + sup(e));
  function q_binom() {
    const t = pick(['val', 'coef', 'crip', 'crip', 'disp']), K = 'Combinatoria', D = (n, k) => factorial(n) / factorial(n - k);
    if (t === 'val') {
      const n = ri(5, 12), k = ri(2, n - 2), v = C(n, k);
      return build({ kind: 'coefficienti-binomiali', theme: K, q: `Quanto vale il coefficiente binomiale (${n} su ${k}), cioè C(${n}, ${k})?`, correct: String(v), wrong: [D(n, k), C(n, k - 1), C(n + 1, k), C(n - 1, k), n * k].map(String), filler: () => String(v + ri(1, 40)),
        s: `C(${n}, ${k}) = ${n}!/(${k}!·${n - k}!) = (${[...Array(k).keys()].map(i => n - i).join('·')})/${k}! = ${D(n, k)}/${factorial(k)} = ${v}.` });
    }
    if (t === 'coef') {
      const n = ri(4, 10), k = ri(1, n - 1), v = C(n, k);
      return build({ kind: 'coefficienti-binomiali', theme: K, q: `Nello sviluppo di (a + b)${sup(n)}, il coefficiente di ${pw('a', k)}${pw('b', n - k)} è`, correct: String(v), wrong: [C(n + k - 1, k), D(n, k), n * k, C(n, k - 1), 2 ** k].map(String), filler: () => String(v + ri(1, 30)),
        s: `Per la formula del binomio di Newton il coefficiente di ${pw('a', k)}${pw('b', n - k)} è C(${n}, ${k}) = ${v}: si sceglie ${k === 1 ? `quale dei ${n} fattori dà` : `quali ${k} dei ${n} fattori danno`} la a (combinazioni semplici, non con ripetizione).` });
    }
    if (t === 'crip') {
      const n = ri(3, 7), k = ri(3, 8), v = C(k + n - 1, n - 1), mono = Math.random() < 0.4;
      const q = mono ? `Quanti sono i monomi di grado ${k} nelle ${n} variabili x₁, …, x${sub(n)} (con coefficiente 1)?` : `In una pasticceria ci sono ${n} tipi di pasticcini. Quanti vassoi diversi da ${k} pasticcini si possono comporre (l'ordine non conta e lo stesso tipo si può prendere più volte)?`;
      return build({ kind: 'combinazioni', theme: K, q, correct: String(v), wrong: [n ** k, C(n, k), C(k + n, k), C(k + n - 1, n), k ** n, D(n, Math.min(n, k))].filter(x => x > 0).map(String), filler: () => String(v + ri(1, 50)),
        s: `Sono combinazioni con ripetizione di ${k} elementi scelti fra ${n}: Cʳ = C(${k} + ${n} − 1, ${n} − 1) = C(${k + n - 1}, ${n - 1}) = ${v}.` });
    }
    const n = ri(5, 10), k = ri(2, 4), v = D(n, k);
    return build({ kind: 'disposizioni', theme: K, q: `In una gara con ${n} atleti, quante sono le possibili classifiche dei primi ${k} posti (senza ex aequo)?`, correct: String(v), wrong: [C(n, k), n ** k, factorial(k), n * k, D(n, k - 1)].map(String), filler: () => String(v + ri(1, 60)),
      s: `L'ordine conta e un atleta non può occupare due posti: disposizioni semplici, D = ${[...Array(k).keys()].map(i => n - i).join('·')} = ${v}.` });
  }

  function sub(n) { return String(n).split('').map(d => '₀₁₂₃₄₅₆₇₈₉'[d]).join(''); }
  function sup(n) { return String(n).split('').map(d => '⁰¹²³⁴⁵⁶⁷⁸⁹'[d]).join(''); }

  /* ---------- Algebra lineare: numeri complessi ---------- */
  const cx = (a, b) => { // testo di a + bi, con segni e coefficienti 1/0 sistemati
    const im = b === 0 ? '' : (Math.abs(b) === 1 ? 'i' : Math.abs(b) + 'i');
    if (b === 0) return String(a);
    if (a === 0) return (b < 0 ? '−' : '') + im;
    return `${a < 0 ? '−' + Math.abs(a) : a} ${b < 0 ? '−' : '+'} ${im}`;
  };
  const cxOpts = (a, b, extra) => [cx(a, -b), cx(-a, b), cx(-a, -b), cx(b, a), ...(extra || [])];
  const T = 'Numeri complessi';
  function q_cxmul() {
    const a = ri(-5, 5), b = ri(-5, 5) || 2, c = ri(-5, 5), d = ri(-5, 5) || 3, re = a * c - b * d, im = a * d + b * c;
    return build({ kind: 'numeri-complessi', theme: T, q: `Il prodotto (${cx(a, b)})·(${cx(c, d)}) è`, correct: cx(re, im), wrong: [cx(a * c + b * d, a * d - b * c), cx(a * c - b * d, a * d - b * c), cx(a * c + b * d, a * d + b * c), cx(re, -im), cx(a * c, b * d)], filler: () => cx(ri(-20, 20), ri(-20, 20)),
      s: `(${cx(a, b)})(${cx(c, d)}) = ${a * c} + ${a * d}i + ${b * c}i + ${b * d}i² = (${a * c} − ${b * d}) + (${a * d} + ${b * c})i = ${cx(re, im)}.` });
  }
  function q_cxdiv() {
    const x = ri(-4, 4), y = ri(-4, 4) || 1, c = ri(-3, 3) || 2, d = ri(-3, 3) || 1, re = x * c - y * d, im = x * d + y * c;
    return build({ kind: 'numeri-complessi', theme: T, q: `Il quoziente (${cx(re, im)}) / (${cx(c, d)}) è`, correct: cx(x, y), wrong: [cx(x, -y), cx(-x, y), cx(y, x), cx(-x, -y), cx(x + 1, y)], filler: () => cx(ri(-6, 6), ri(-6, 6)),
      s: `Si moltiplica numeratore e denominatore per il coniugato ${cx(c, -d)}: il denominatore diventa ${c * c + d * d} e il risultato è ${cx(x, y)} (verifica: (${cx(x, y)})(${cx(c, d)}) = ${cx(re, im)}).` });
  }
  function q_cxmod() {
    const tr = pick([[3, 4], [5, 12], [8, 15], [6, 8], [7, 24], [9, 12]]), sg = () => (Math.random() < 0.5 ? -1 : 1), a = tr[0] * sg(), b = tr[1] * sg(), n = a * a + b * b, m = Math.sqrt(n);
    return build({ kind: 'coniugato-modulo', theme: 'Coniugato e modulo', q: `Il modulo di z = ${cx(a, b)} è`, correct: String(m), wrong: [String(n), String(Math.abs(a) + Math.abs(b)), String(Math.abs(a * b)), `√${m}`, String(m + 1)], filler: () => String(ri(2, 30)),
      s: `|z| = √(${a}² + ${b}²) = √${n} = ${m}.` });
  }
  function q_cxinv() {
    const a = ri(-4, 4) || 2, b = ri(-4, 4) || 3, n = a * a + b * b, f = (x, y) => `(${cx(x, y)})/${n}`;
    return build({ kind: 'coniugato-modulo', theme: 'Coniugato e modulo', q: `L'inverso moltiplicativo di z = ${cx(a, b)} è`, correct: f(a, -b), wrong: [f(a, b), f(-a, b), f(-a, -b), `(${cx(a, -b)})/${Math.sqrt(n) % 1 ? n + 1 : n - 1}`, f(b, a)], filler: () => `(${cx(ri(-5, 5), ri(-5, 5))})/${ri(2, 30)}`,
      s: `1/z = z̄/|z|² = (${cx(a, -b)})/${n}, perché z·z̄ = a² + b² = ${n}.` });
  }
  function q_cxipow() {
    const n = ri(3, 99), r = n % 4, correct = ['1', 'i', '−1', '−i'][r];
    return build({ kind: 'potenze-radici', theme: 'Potenze e radici', q: `Il valore di i${sup(n)} è`, correct, wrong: ['1', 'i', '−1', '−i', '0'].filter(x => x !== correct), filler: () => String(ri(2, 9)),
      s: `Le potenze di i si ripetono con periodo 4 (i⁰ = 1, i¹ = i, i² = −1, i³ = −i): ${n} = 4·${Math.floor(n / 4)} + ${r}, quindi i${sup(n)} = ${correct}.` });
  }
  function q_cxsq() {
    const a = ri(-6, 6) || 3, b = ri(-6, 6) || 2, re = a * a - b * b, im = 2 * a * b;
    return build({ kind: 'numeri-complessi', theme: T, q: `(${cx(a, b)})² =`, correct: cx(re, im), wrong: [cx(a * a + b * b, im), cx(re, -im), cx(re, im + 2), cx(a * a, b * b), cx(a * a - b * b, a * b)], filler: () => cx(ri(-30, 30), ri(-30, 30)),
      s: `(a + bi)² = a² − b² + 2abi = ${re} + ${im}i ⟹ ${cx(re, im)}.` });
  }
  function q_cx1i() {
    const k = pick([4, 8, 12]), v = (-4) ** (k / 4);
    return build({ kind: 'potenze-radici', theme: 'Potenze e radici', q: `Quanto vale (1 + i)${sup(k)}?`, correct: String(v), wrong: [String(-v), String(2 ** k), String(2 ** (k / 2)), String(v * 2), '0'], filler: () => String(ri(-80, 80)),
      s: `(1 + i)² = 2i, quindi (1 + i)⁴ = (2i)² = −4 e (1 + i)${sup(k)} = (−4)${sup(k / 4)} = ${v}.` });
  }

  /* ---------- Algebra lineare: matrici, traccia, rango, determinante, mosse di Gauss, Binet, inversa ---------- */
  // Notazione del corso: A = ( 1 3 7 ; 1 5 5 ; 1 4 10 ) con le righe separate da «;», det A, ᵗA, rk(A), tr(A), Iₙ, A⁻¹, M(n).
  const nm = v => (v < 0 ? '−' + Math.abs(v) : String(v));
  const par = v => (v < 0 ? '(' + nm(v) + ')' : nm(v));
  const matTxt = M => '( ' + M.map(r => r.map(nm).join(' ')).join(' ; ') + ' )';
  const frac = (p, q) => { if (q < 0) { p = -p; q = -q; } const g = gcd(Math.abs(p), q) || 1; p /= g; q /= g; return q === 1 ? nm(p) : (p < 0 ? '−' : '') + Math.abs(p) + '/' + q; };
  const rmat = (m, n, lo, hi) => Array.from({ length: m }, () => Array.from({ length: n }, () => ri(lo, hi)));
  const det2 = M => M[0][0] * M[1][1] - M[0][1] * M[1][0];
  const minor = (M, i, j) => M.filter((_, r) => r !== i).map(r => r.filter((_, c) => c !== j));
  const det = M => (M.length === 1 ? M[0][0] : M[0].reduce((s, a, j) => s + (j % 2 ? -1 : 1) * a * det(minor(M, 0, j)), 0)); // Laplace lungo la 1ª riga
  const cof = (M, i, j) => ((i + j) % 2 ? -1 : 1) * det(minor(M, i, j));
  const mmul = (A, B) => A.map(r => B[0].map((_, j) => r.reduce((s, x, k) => s + x * B[k][j], 0)));
  const tr = A => A.reduce((s, r, k) => s + r[k], 0);
  function rank(M) { // eliminazione di Gauss senza frazioni
    const A = M.map(r => r.slice()), m = A.length, n = A[0].length; let rk = 0;
    for (let c = 0; c < n && rk < m; c++) {
      let p = rk; while (p < m && A[p][c] === 0) p++;
      if (p === m) continue;
      [A[rk], A[p]] = [A[p], A[rk]];
      for (let r = rk + 1; r < m; r++) { const f = A[r][c], g = A[rk][c]; if (f) A[r] = A[r].map((x, k) => x * g - A[rk][k] * f); }
      rk++;
    }
    return rk;
  }
  const TM = 'Matrici', TR = 'Rango', TD = 'Determinante', TI = 'Matrice inversa';
  const cap = s => s[0].toUpperCase() + s.slice(1);
  function laplaceTxt(M, verifica) { // spiegazione: sviluppo di Laplace lungo la riga o la colonna con più zeri
    let best = { z: -1 };
    for (let k = 0; k < 3; k++) {
      const zr = M[k].filter(x => x === 0).length, zc = M.filter(r => r[k] === 0).length;
      if (zr > best.z) best = { z: zr, row: true, k };
      if (zc > best.z) best = { z: zc, row: false, k };
    }
    const lin = `la ${best.k + 1}ª ${best.row ? 'riga' : 'colonna'}`;
    if (best.z === 3) return `${verifica ? 'Infatti l' : 'L'}a ${best.k + 1}ª ${best.row ? 'riga' : 'colonna'} è nulla, quindi det A = 0.`;
    const terms = [];
    for (let t = 0; t < 3; t++) {
      const i = best.row ? best.k : t, j = best.row ? t : best.k, x = M[i][j];
      if (x !== 0) terms.push([(i + j) % 2 ? '−' : '+', `${par(x)}·${par(det2(minor(M, i, j)))}`]);
    }
    const sum = terms.map(([sg, tt], n) => (n === 0 ? (sg === '−' ? '−' : '') : ` ${sg} `) + tt).join('');
    return `${verifica ? 'Verifica con lo sviluppo di Laplace' : 'Conviene sviluppare con Laplace'} lungo ${lin}${best.z ? ` (${best.z === 1 ? 'ha uno zero' : 'ha ' + best.z + ' zeri'})` : ''}, con i segni a scacchiera: det A = ${sum} = ${nm(det(M))}.`;
  }
  function det3mat(kind) {
    if (kind === 'tri') { // triangolare superiore o inferiore
      const M = rmat(3, 3, -4, 6), up = Math.random() < 0.5;
      for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) if (up ? j < i : j > i) M[i][j] = 0;
      for (let i = 0; i < 3; i++) if (M[i][i] === 0) M[i][i] = pick([-2, 2, 3]);
      return M;
    }
    if (kind === 'zeri') { // una riga o colonna con due zeri, a volte un altro zero
      const M = rmat(3, 3, -3, 5), k = ri(0, 2), row = Math.random() < 0.5;
      for (const t of shuffle([0, 1, 2]).slice(0, 2)) { if (row) M[k][t] = 0; else M[t][k] = 0; }
      if (Math.random() < 0.5) M[ri(0, 2)][ri(0, 2)] = 0;
      return M;
    }
    if (kind === 'dip') { // una riga combinazione lineare delle altre due: det A = 0
      const M = rmat(3, 3, -3, 4), [i, j, h] = shuffle([0, 1, 2]), a = pick([-2, -1, 1, 2]), b = pick([0, 1, -1]);
      M[h] = M[i].map((x, c) => a * x + b * M[j][c]);
      return M;
    }
    return rmat(3, 3, -2, 3);
  }
  function q_det2() {
    const M = rmat(2, 2, -5, 9), [[a, b], [c, d]] = M, v = det2(M);
    return build({ kind: 'determinante', theme: TD, q: `Sia A = ${matTxt(M)}. Allora det A =`, correct: nm(v), wrong: [a * d + b * c, b * c - a * d, a * b - c * d, a * c - b * d, a * d].map(nm), filler: () => nm(v + pick([-1, 1]) * ri(1, 9)),
      s: `Per una matrice 2 × 2 il determinante è il prodotto della diagonale principale meno quello dell'altra diagonale: ${par(a)}·${par(d)} − ${par(b)}·${par(c)} = ${nm(a * d)} − ${par(b * c)} = ${nm(v)}.` });
  }
  function q_det3() {
    const kind = pick(['tri', 'zeri', 'zeri', 'dip', 'gen']), M = det3mat(kind), v = det(M), [[a, b, c], [d, e, f], [g, h, i]] = M;
    const pre = kind === 'tri' ? `A è triangolare, quindi det A è il prodotto degli elementi sulla diagonale: ${par(a)}·${par(e)}·${par(i)} = ${nm(v)}. ` : kind === 'dip' ? 'Una riga di A è combinazione lineare delle altre due (righe linearmente dipendenti), quindi det A = 0. ' : '';
    return build({ kind: 'determinante', theme: TD, q: `Sia A = ${matTxt(M)}. Allora det A =`, correct: nm(v),
      wrong: [a * (e * i - f * h) + b * (d * i - f * g) + c * (d * h - e * g), -v, a * e * i, a * e * i + b * f * g + c * d * h, a + e + i, a * e * i - c * e * g].map(nm), filler: () => nm(v + pick([-1, 1]) * ri(1, 12)),
      s: kind === 'tri' ? pre.trim() : pre + laplaceTxt(M, kind === 'dip') });
  }
  function q_gauss() {
    const n = pick([3, 3, 4]), d = pick([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7]), k = ri(1, 3), mv = [];
    for (let t = 0; t < k; t++) { const [i, j] = shuffle([...Array(n).keys()]).slice(0, 2); mv.push({ ty: pick(['sw', 'mul', 'add']), i, j, lam: pick([-3, -2, 2, 3, 4, 5]), rc: Math.random() < 0.7 ? 'riga' : 'colonna' }); }
    const txt = m => (m.ty === 'sw' ? `si scambiano la ${m.i + 1}ª e la ${m.j + 1}ª ${m.rc}` : m.ty === 'mul' ? `si moltiplica la ${m.i + 1}ª ${m.rc} per ${nm(m.lam)}` : `alla ${m.i + 1}ª ${m.rc} si somma la ${m.j + 1}ª ${m.rc} moltiplicata per ${nm(m.lam)}`);
    const ok = { sw: -1, mul: l => l, add: () => 1 }, eff = (m, e) => (m.ty === 'sw' ? e.sw : m.ty === 'mul' ? e.mul(m.lam) : e.add(m.lam)), run = e => mv.reduce((p, m) => p * eff(m, e), d), v = run(ok);
    const wrong = [run({ ...ok, sw: 1 }), run({ ...ok, add: l => l }), run({ ...ok, mul: l => l ** n }), run({ ...ok, mul: () => 1 }), -v].map(nm);
    const lista = k === 1 ? 'la mossa: ' + txt(mv[0]) : 'le mosse, nell\'ordine: ' + mv.map((m, t) => `(${t + 1}) ${txt(m)}`).join('; ');
    const why = mv.map(m => `${txt(m)}: ${m.ty === 'sw' ? 'il determinante cambia segno' : m.ty === 'mul' ? `il determinante si moltiplica per ${nm(m.lam)}` : 'il determinante non cambia'}`).join('; ');
    return build({ kind: 'mosse-gauss', theme: TD, q: `Sia A ∈ M(${n}) con det A = ${nm(d)}. La matrice A′ si ottiene da A con ${lista}. Allora det A′ =`, correct: nm(v), wrong, filler: () => nm(v * pick([2, -2, 3]) + ri(-3, 3)),
      s: `${cap(why)}. Quindi det A′ = ${mv.some(m => m.ty !== 'add') ? `${nm(d)}${mv.filter(m => m.ty !== 'add').map(m => '·' + par(eff(m, ok))).join('')} = ${nm(v)}` : `det A = ${nm(v)}`}.` });
  }
  function q_detprop() {
    const n = pick([2, 3, 4]), x = pick([-4, -3, -2, -1, 2, 3, 4, 5]), y = pick([-3, -2, -1, 2, 3, 4, 6]), c = pick([-1, 2, -2, 3]), t = pick(['cA', 'cA', 'AB', 'AtB', 'A2B', 'cAB', 'Ainv', 'AinvB']);
    const cA = c === -1 ? '−A' : `${nm(c)}A`, cn = c ** n, V = z => (typeof z === 'string' ? z : nm(z));
    const head = t === 'cA' ? `Sia A ∈ M(${n}) con det A = ${nm(x)}.` : `Siano A, B ∈ M(${n}) con det A = ${nm(x)} e det B = ${nm(y)}.`;
    const binet = 'Per il Teorema di Binet det(A · B) = det A · det B';
    const T = {
      cA: [`det(${cA})`, cn * x, [c * x, c ** (n - 1) * x, -cn * x, c + x, n * c * x], `det(cA) = cⁿ · det A: ognuna delle ${n} righe è moltiplicata per ${nm(c)}, quindi det(${cA}) = ${par(c)}${sup(n)}·${par(x)} = ${nm(cn * x)}.`],
      AB: ['det(A · B)', x * y, [x + y, n * x * y, -x * y, x ** n * y, 2 * x * y], `${binet} = ${par(x)}·${par(y)} = ${nm(x * y)}.`],
      AtB: ['det(ᵗA · B)', x * y, [-x * y, x + y, n * x * y, x * x * y, 2 * x * y], `det(ᵗA) = det A, e per Binet det(ᵗA · B) = det(ᵗA) · det B = ${par(x)}·${par(y)} = ${nm(x * y)}.`],
      A2B: ['det(A² · B)', x * x * y, [2 * x * y, x * x + y, x * y, x * x * y * y, -x * x * y], `${binet}, quindi det(A² · B) = (det A)² · det B = ${par(x)}²·${par(y)} = ${nm(x * x * y)}.`],
      cAB: [`det(${cA} · B)`, cn * x * y, [c * x * y, -cn * x * y, c * c * x * y, cn * x + y, x * y], `${binet}, e det(${cA}) = ${par(c)}${sup(n)}·det A; quindi det(${cA} · B) = ${nm(cn)}·${par(x)}·${par(y)} = ${nm(cn * x * y)}.`],
      Ainv: ['det(A⁻¹)', frac(1, x), [nm(x), frac(-1, x), nm(-x), frac(1, x * x), frac(1, n * x)], `Da A · A⁻¹ = I${sub(n)} e Binet: det A · det(A⁻¹) = det(I${sub(n)}) = 1, quindi det(A⁻¹) = 1/det A = ${frac(1, x)}.`],
      AinvB: ['det(A⁻¹ · B)', frac(y, x), [frac(x, y), nm(x * y), frac(-y, x), frac(1, x * y), nm(y - x)], `${binet} e det(A⁻¹) = 1/det A, quindi det(A⁻¹ · B) = ${nm(y)}/${par(x)} = ${frac(y, x)}.`],
    }[t];
    return build({ kind: 'binet', theme: TD, q: `${head} Allora ${T[0]} =`, correct: V(T[1]), wrong: T[2].map(V), filler: () => nm((typeof T[1] === 'number' ? T[1] : x) * pick([2, -2, 3]) + ri(1, 5)), s: T[3] });
  }
  function q_prod() {
    const sq = Math.random() < 0.7, A = sq ? rmat(2, 2, -3, 5) : rmat(2, 3, -3, 4), B = sq ? rmat(2, 2, -3, 5) : rmat(3, 2, -3, 4);
    const P = mmul(A, B), i = ri(0, 1), j = ri(0, 1), v = P[i][j], K = A[0].length;
    const wrong = sq ? [mmul(B, A)[i][j], A[i][j] * B[i][j], A[i].reduce((s, a, k) => s + a * B[j][k], 0), A.reduce((s, r, k) => s + r[i] * B[k][j], 0), P[j][i]]
      : [P[j][i], A[i].reduce((s, a, k) => s + a * B[k][1 - j], 0), A[i][0] * B[0][j] + A[i][1] * B[1][j], A[1 - i].reduce((s, a, k) => s + a * B[k][j], 0)];
    const terms = [...Array(K).keys()].map(k => `${par(A[i][k])}·${par(B[k][j])}`).join(' + ');
    return build({ kind: 'matrici', theme: TM, q: `Siano A = ${matTxt(A)} e B = ${matTxt(B)}. L'entrata di posto (${i + 1}, ${j + 1}) del prodotto A · B è`, correct: nm(v), wrong: wrong.map(nm), filler: () => nm(v + pick([-1, 1]) * ri(1, 8)),
      s: `L'entrata di posto (${i + 1}, ${j + 1}) di A · B è il prodotto della ${i + 1}ª riga di A per la ${j + 1}ª colonna di B: ${terms} = ${nm(v)}.${sq ? ` Attenzione all'ordine: in B · A la stessa entrata vale ${nm(mmul(B, A)[i][j])}.` : ''}` });
  }
  function q_traccia() {
    if (Math.random() < 0.6) {
      const n = pick([3, 3, 4]), A = rmat(n, n, -5, 9), v = tr(A), all = A.flat().reduce((s, z) => s + z, 0);
      return build({ kind: 'matrici', theme: TM, q: `Sia A = ${matTxt(A)}. Allora tr(A) =`, correct: nm(v), wrong: [A.reduce((s, r, k) => s + r[n - 1 - k], 0), A.reduce((p, r, k) => p * r[k], 1), all, v - A[n - 1][n - 1], A[0].reduce((s, z) => s + z, 0)].map(nm), filler: () => nm(v + pick([-1, 1]) * ri(1, 9)),
        s: `La traccia è la somma delle entrate sulla diagonale principale (dall'alto a sinistra al basso a destra): ${A.map((r, k) => par(r[k])).join(' + ')} = ${nm(v)}.` });
    }
    const A = rmat(2, 2, -3, 5), B = rmat(2, 2, -3, 5), P = mmul(A, B), v = tr(P);
    return build({ kind: 'matrici', theme: TM, q: `Siano A = ${matTxt(A)} e B = ${matTxt(B)}. Allora tr(A · B) =`, correct: nm(v), wrong: [tr(A) * tr(B), tr(A) + tr(B), A[0][0] * B[0][0] + A[1][1] * B[1][1], -v, P[0][1] + P[1][0]].map(nm), filler: () => nm(v + pick([-1, 1]) * ri(1, 9)),
      s: `Servono solo le entrate diagonali di A · B: (A·B)₁₁ = ${nm(P[0][0])} e (A·B)₂₂ = ${nm(P[1][1])}, quindi tr(A · B) = ${nm(v)}. In generale tr(A · B) ≠ tr(A) · tr(B) (qui ${nm(tr(A) * tr(B))}).` });
  }
  function q_rango() {
    const [m, n] = pick([[2, 3], [3, 3], [3, 3], [3, 4]]);
    for (let tries = 0; tries < 60; tries++) {
      const r = ri(1, Math.min(m, n)), base = rmat(r, n, -3, 4);
      if (rank(base) !== r) continue;
      const rows = base.map(x => ({ v: x, c: null }));
      while (rows.length < m) { const c = Array.from({ length: r }, () => ri(-2, 2)); if (c.every(z => !z) && Math.random() < 0.8) c[0] = 1; rows.push({ v: [...Array(n).keys()].map(k => c.reduce((s, cc, t) => s + cc * base[t][k], 0)), c }); }
      if (rows.some(x => x.v.some(z => Math.abs(z) > 12))) continue;
      const order = shuffle([...Array(m).keys()]), pos = order.map((_, k) => order.indexOf(k)); // pos[t] = riga di A in cui finisce la t-esima riga costruita
      const M = order.map(k => rows[k].v), v = rank(M);
      const Ai = t => `A${sub(pos[t] + 1)}`, comb = c => c.map((cc, t) => [cc, Ai(t)]).filter(([cc]) => cc).map(([cc, a], k) => (cc < 0 ? (k ? ' − ' : '−') : (k ? ' + ' : '')) + (Math.abs(cc) === 1 ? '' : Math.abs(cc)) + a).join('');
      const deps = rows.map((x, t) => (x.c ? (x.c.every(z => !z) ? `${Ai(t)} è nulla` : `${Ai(t)} = ${comb(x.c)}`) : null)).filter(Boolean);
      const opts = m === 3 && n === 4 ? ['0', '1', '2', '3', '4'] : ['0', '1', '2', '3', m === n ? 'non è definito, perché det A = 0' : 'non è definito, perché A non è quadrata'];
      const s = deps.length ? `Indicando con A${sub(1)}, …, A${sub(m)} le righe: ${deps.join('; ')}. Le righe indipendenti sono ${v}, quindi rk(A) = ${v} (il rango per righe è uguale a quello per colonne).`
        : `Le ${m} righe sono linearmente indipendenti (con le mosse di Gauss si arriva a una matrice a scala senza righe nulle), quindi rk(A) = ${v}${m === n ? `; infatti det A = ${nm(det(M))} ≠ 0` : ''}. Il rango non supera mai il numero di righe né quello di colonne.`;
      return build({ kind: 'rango', theme: TR, q: `Sia A = ${matTxt(M)}. Allora rk(A) =`, correct: String(v), wrong: opts, filler: () => '0', s });
    }
    return null;
  }
  function q_inv() {
    if (Math.random() < 0.5) { // un'entrata di A⁻¹ = (1/det A) · ᵗcof(A)
      let A, d; do { A = rmat(2, 2, -4, 6); d = det2(A); } while (d === 0 || Math.abs(d) > 6);
      const i = ri(0, 1), j = ri(0, 1), cji = cof(A, j, i), cij = cof(A, i, j);
      return build({ kind: 'inversa', theme: TI, q: `Sia A = ${matTxt(A)}. L'entrata di posto (${i + 1}, ${j + 1}) di A⁻¹ è`, correct: frac(cji, d),
        wrong: [frac(cij, d), frac(-cji, d), nm(cji), A[i][j] ? frac(1, A[i][j]) : nm(-cji), cji ? frac(d, cji) : nm(d), frac(A[i][j], d)], filler: () => frac(ri(-6, 6), pick([1, 2, 3, 4, 5])),
        s: `det A = ${nm(d)} ≠ 0, quindi A è invertibile e A⁻¹ = (1/det A) · ᵗcof(A). Per la trasposta, l'entrata (${i + 1}, ${j + 1}) di A⁻¹ è il cofattore di posto (${j + 1}, ${i + 1}) diviso per det A: ${nm(cji)}/${par(d)}${`${nm(cji)}/${par(d)}` === frac(cji, d) ? '' : ' = ' + frac(cji, d)}. Per una 2 × 2: A⁻¹ = (1/det A) · ( d −b ; −c a ).` });
    }
    let M;
    if (Math.random() < 0.5) { M = rmat(2, 2, -4, 6); if (Math.random() < 0.45) { const k = pick([-2, -1, 2, 3]); M[1] = M[0].map(z => k * z); } }
    else M = det3mat(pick(['tri', 'zeri', 'dip', 'dip', 'gen']));
    const v = det(M), n = M.length, yes = z => `sì, perché det A = ${nm(z)} ≠ 0`, no0 = 'no, perché det A = 0';
    const sbagli = (n === 2 ? [M[0][0] * M[1][1] + M[0][1] * M[1][0], -v] : [M[0][0] * det2(minor(M, 0, 0)) + M[0][1] * det2(minor(M, 0, 1)) + M[0][2] * det2(minor(M, 0, 2)), M[0][0] * M[1][1] * M[2][2], -v]).filter(z => z !== 0).map(yes);
    const nessunaNulla = M.every(r => r.some(z => z !== 0)), haZero = M.some(r => r.includes(0));
    const wrong = v !== 0 ? [no0, ...sbagli, ...(haZero ? ["no, perché A ha un'entrata nulla"] : []), ...(v < 0 ? [`no, perché det A = ${nm(v)} è negativo`] : [])]
      : [...sbagli, ...(nessunaNulla ? ['sì, perché nessuna riga di A è nulla'] : []), ...(M.every((r, k) => r[k] !== 0) ? ['sì, perché la diagonale non contiene zeri'] : [])];
    return build({ kind: 'inversa', theme: TI, q: `La matrice A = ${matTxt(M)} è invertibile?`, correct: v ? yes(v) : no0, wrong, filler: () => yes(pick([-1, 1]) * ri(1, 30)),
      s: `A è invertibile se e solo se det A ≠ 0. ${n === 2 ? `det A = ${par(M[0][0])}·${par(M[1][1])} − ${par(M[0][1])}·${par(M[1][0])} = ${nm(v)}.` : laplaceTxt(M)} ${v ? `Quindi A è invertibile${v < 0 ? ' (il segno di det A non conta)' : ''}.` : 'Quindi A non è invertibile.'}` });
  }

  /* ---------- Fondamenti: binario, complemento a due, Hamming, memoria ---------- */
  const TF = 'Rappresentazione binaria';
  const bits = (v, n) => (v >>> 0).toString(2).padStart(n, '0').slice(-n);
  function q_bin2dec() {
    const v = ri(20, 255), b = v.toString(2);
    return build({ kind: 'binario', theme: TF, q: `Il numero binario ${b} vale in decimale`, correct: String(v), wrong: [v + 1, v - 1, v ^ 1, parseInt(b.split('').reverse().join(''), 2), v + ri(2, 9)].map(String), filler: () => String(ri(20, 255)),
      s: `${b}₂ = ${b.split('').map((c, i) => (c === '1' ? 2 ** (b.length - 1 - i) : null)).filter(x => x !== null).join(' + ')} = ${v}.` });
  }
  function q_hex() {
    const v = ri(32, 4095), h = v.toString(16).toUpperCase(), up = Math.random() < 0.5;
    if (up) return build({ kind: 'binario', theme: TF, q: `Il numero decimale ${v} in esadecimale è`, correct: h, wrong: [(v + 1).toString(16), (v - 1).toString(16), (v ^ 16).toString(16), (v + 16).toString(16)].map(x => x.toUpperCase()), filler: () => ri(32, 4095).toString(16).toUpperCase(), s: `${v} = ${h}₁₆ (si divide per 16 e si leggono i resti dal basso).` });
    return build({ kind: 'binario', theme: TF, q: `Il numero esadecimale ${h} vale in decimale`, correct: String(v), wrong: [v + 1, v - 1, v + 16, v - 16, v ^ 256].map(String), filler: () => String(ri(32, 4095)), s: `${h}₁₆ = ${[...h].map((c, i) => parseInt(c, 16) + '·16' + sup(h.length - 1 - i)).join(' + ')} = ${v}.` });
  }
  function q_c2() {
    const n = ri(1, 127), neg = Math.random() < 0.6, N = 8;
    if (neg) { const c = bits(256 - n, N); return build({ kind: 'complemento-eccesso', theme: TF, q: `In complemento a due su 8 bit, −${n} si scrive`, correct: c, wrong: ['1' + bits(n, 7), bits(~n & 255, N), bits(n, N), bits(256 - n + 1, N), bits(256 - n - 1, N)], filler: () => bits(ri(0, 255), N), s: `${n} = ${bits(n, N)}; si invertono i bit (${bits(~n & 255, N)}) e si somma 1: ${c}.` }); }
    const c = bits(ri(128, 255), N), v = parseInt(c, 2) - 256;
    return build({ kind: 'complemento-eccesso', theme: TF, q: `Il pattern ${c}, letto in complemento a due su 8 bit, rappresenta il numero`, correct: String(v), wrong: [String(parseInt(c, 2)), String(-(parseInt(c, 2) - 128)), String(v + 1), String(v - 1), String(-v)], filler: () => String(ri(-128, 127)), s: `Il bit più a sinistra è 1, quindi il numero è negativo: ${parseInt(c, 2)} − 256 = ${v}.` });
  }
  function q_hamming() {
    const n = ri(6, 10), x = ri(0, 2 ** n - 1), y = ri(0, 2 ** n - 1), a = bits(x, n), b = bits(y, n), d = [...a].filter((c, i) => c !== b[i]).length;
    return build({ kind: 'errori-hamming', theme: 'Compressione ed errori', q: `Qual è la distanza di Hamming tra ${a} e ${b}?`, correct: String(d), wrong: [d + 1, d - 1, d + 2, n - d, n].map(String).filter(x => +x >= 0), filler: () => String(ri(0, n)), s: `La distanza di Hamming è il numero di posizioni in cui i due pattern differiscono: ${d}.` });
  }
  function q_parita() {
    const n = 7, x = ri(0, 127), a = bits(x, n), ones = [...a].filter(c => c === '1').length, bit = ones % 2, correct = a + bit;
    return build({ kind: 'errori-hamming', theme: 'Compressione ed errori', q: `Aggiungendo in fondo un bit di parità pari al pattern ${a}, si ottiene`, correct, wrong: [a + (1 - bit), bits(x ^ 1, n) + bit, (1 - bit) + a, a.slice(1) + a[0] + bit], filler: () => bits(ri(0, 255), 8), s: `Il pattern contiene ${ones} uni; per avere un numero pari di uni complessivo il bit aggiunto è ${bit}: ${correct}.` });
  }
  function q_mem() {
    const k = ri(8, 20);
    if (Math.random() < 0.5) return build({ kind: 'memoria', theme: 'Circuiti e memoria', q: `Una memoria principale ha indirizzi di ${k} bit e celle da 1 byte. Quante celle ha?`, correct: `2${sup(k)} = ${2 ** k}`, wrong: [`${k}²`, `2·${k}`, `2${sup(k - 1)}`, `2${sup(k + 1)}`, `${k}!`].map(x => x), filler: () => `2${sup(ri(4, 24))}`, s: `Con ${k} bit si formano 2${sup(k)} indirizzi diversi, quindi ${2 ** k} celle.` });
    return build({ kind: 'memoria', theme: 'Circuiti e memoria', q: `Quanti bit servono per indirizzare ${2 ** k} celle di memoria?`, correct: String(k), wrong: [k + 1, k - 1, 2 ** k, k * 2, 2 ** (k - 1)].map(String), filler: () => String(ri(4, 30)), s: `Servono k bit con 2^k ≥ ${2 ** k}: k = ${k}.` });
  }

  /* ---------- Programmazione: «Che cosa stampa?» con un mini-interprete del C ----------
     Sottoinsieme: int, cast (float), puntatori a int, funzioni con parametri int / int *, if/else, while, do-while, for,
     operatori aritmetici, di confronto, logici (con cortocircuito), ++/--, composti, printf con soli %d.
     La risposta giusta è l'output del programma; le sbagliate sono l'output dello stesso programma eseguito con un
     «errore tipico» attivo (flag) o di una sua variante (es. < al posto di <=). */
  const C_OPS = ['++', '--', '+=', '-=', '*=', '/=', '%=', '==', '!=', '<=', '>=', '&&', '||', '+', '-', '*', '/', '%', '<', '>', '=', '!', '&', '(', ')', '{', '}', ';', ','];
  function cLex(src) {
    const t = []; let i = 0;
    while (i < src.length) {
      const ch = src[i];
      if (/\s/.test(ch)) { i++; continue; }
      if (src.startsWith('//', i)) { while (i < src.length && src[i] !== '\n') i++; continue; }
      if (/[0-9]/.test(ch)) { let j = i; while (/[0-9]/.test(src[j] || '')) j++; t.push({ k: 'num', v: +src.slice(i, j) }); i = j; continue; }
      if (/[A-Za-z_]/.test(ch)) { let j = i; while (/[A-Za-z0-9_]/.test(src[j] || '')) j++; t.push({ k: 'id', v: src.slice(i, j) }); i = j; continue; }
      if (ch === '"') { let j = i + 1, s = ''; while (j < src.length && src[j] !== '"') { if (src[j] === '\\') { s += src[j + 1] === 'n' ? '\n' : src[j + 1]; j += 2; } else s += src[j++]; } t.push({ k: 'str', v: s }); i = j + 1; continue; }
      const op = C_OPS.find(o => src.startsWith(o, i)); if (!op) throw new Error('C: carattere ' + ch);
      t.push({ k: 'op', v: op }); i += op.length;
    }
    t.push({ k: 'eof', v: '' }); return t;
  }
  function cParse(src) {
    const T = cLex(src), TYPES = ['int', 'float', 'void']; let p = 0;
    const is = (v, o = 0) => T[p + o].k !== 'str' && T[p + o].v === v;
    const eat = v => { if (!is(v)) throw new Error(`C: atteso ${v}, trovato ${T[p].v}`); return T[p++]; };
    const isType = (o = 0) => T[p + o].k === 'id' && TYPES.includes(T[p + o].v);
    const name = () => { if (T[p].k !== 'id') throw new Error('C: atteso un nome'); return T[p++].v; };
    function declarators(type) { const ds = []; for (;;) { let ptr = false; if (is('*')) { p++; ptr = true; } const n = name(); let init = null; if (is('=')) { p++; init = assign(); } ds.push({ name: n, ptr, type, init }); if (!is(',')) break; p++; } return { s: 'decl', ds }; }
    function stmt() {
      if (is('{')) { p++; const b = []; while (!is('}')) b.push(stmt()); p++; return { s: 'block', b }; }
      if (isType()) { const type = T[p++].v, d = declarators(type); eat(';'); return d; }
      if (is('if')) { p++; eat('('); const c = assign(); eat(')'); const th = stmt(); let el = null; if (is('else')) { p++; el = stmt(); } return { s: 'if', c, th, el }; }
      if (is('while')) { p++; eat('('); const c = assign(); eat(')'); return { s: 'while', c, b: stmt() }; }
      if (is('do')) { p++; const b = stmt(); eat('while'); eat('('); const c = assign(); eat(')'); eat(';'); return { s: 'do', c, b }; }
      if (is('for')) {
        p++; eat('('); let i = null;
        if (isType()) { const type = T[p++].v; i = declarators(type); } else if (!is(';')) i = { s: 'expr', e: assign() };
        eat(';'); const c = is(';') ? null : assign(); eat(';'); const st = is(')') ? null : assign(); eat(')');
        return { s: 'for', i, c, st, b: stmt() };
      }
      if (is('return')) { p++; const e = is(';') ? null : assign(); eat(';'); return { s: 'ret', e }; }
      const e = assign(); eat(';'); return { s: 'expr', e };
    }
    function assign() {
      const l = logor();
      if (T[p].k === 'op' && ['=', '+=', '-=', '*=', '/=', '%='].includes(T[p].v)) { const op = T[p++].v; return { e: 'asg', op, l, r: assign() }; }
      return l;
    }
    const bin = (next, ops) => () => { let l = next(); while (T[p].k === 'op' && ops.includes(T[p].v)) { const op = T[p++].v; l = { e: 'bin', op, l, r: next() }; } return l; };
    function unary() {
      if (T[p].k === 'op') {
        const v = T[p].v;
        if (v === '++' || v === '--') { p++; return { e: 'pre', op: v, x: unary() }; }
        if (['-', '+', '!', '*', '&'].includes(v)) { p++; return { e: 'un', op: v, x: unary() }; }
        if (v === '(' && isType(1)) { p++; const type = T[p++].v; eat(')'); return { e: 'cast', type, x: unary() }; }
      }
      let x = primary();
      for (;;) {
        if (is('++') || is('--')) { x = { e: 'post', op: T[p++].v, x }; continue; }
        if (is('(') && x.e === 'id') { p++; const args = []; if (!is(')')) for (;;) { args.push(assign()); if (!is(',')) break; p++; } eat(')'); x = { e: 'call', f: x.n, args }; continue; }
        return x;
      }
    }
    function primary() {
      const t = T[p++];
      if (t.k === 'num') return { e: 'num', v: t.v };
      if (t.k === 'str') return { e: 'str', v: t.v };
      if (t.k === 'id') return { e: 'id', n: t.v };
      if (t.v === '(') { const x = assign(); eat(')'); return x; }
      throw new Error('C: inatteso ' + t.v);
    }
    const mul = bin(unary, ['*', '/', '%']), add = bin(mul, ['+', '-']), rel = bin(add, ['<', '<=', '>', '>=']), eqq = bin(rel, ['==', '!=']), land = bin(eqq, ['&&']), logor = bin(land, ['||']);
    const funcs = {}, top = [];
    while (T[p].k !== 'eof') {
      if (isType() && T[p + 1].k === 'id' && is('(', 2)) { // definizione di funzione
        const ret = T[p].v, fname = T[p + 1].v, params = []; p += 3;
        if (is('void') && is(')', 1)) p++;
        while (!is(')')) { const type = T[p++].v; let ptr = false; if (is('*')) { p++; ptr = true; } params.push({ type, ptr, name: name() }); if (is(',')) p++; }
        p++; funcs[fname] = { ret, params, body: stmt() };
      } else top.push(stmt());
    }
    if (!funcs.main) funcs.main = { ret: 'int', params: [], body: { s: 'block', b: top } };
    return funcs;
  }
  /* flags degli errori tipici: realDiv (divisione tra interi creduta reale), floorDiv (arrotonda verso −∞ come in Python),
     noShort (niente cortocircuito), pyLogic (&& e || restituiscono un operando), swapIncr (confonde ++x e x++),
     noPostIncr (x++ non modifica x), byRef (il passaggio per valore modifica la variabile del chiamante),
     ptrCopy (&x punta a una copia: scrivere *p non modifica x), castNone (il cast non fa nulla), roundConv (float → int arrotonda) */
  function cRun(src, flags) {
    const F = flags || {}, funcs = cParse(src); let out = '', steps = 0;
    const tick = () => { if (++steps > 20000) throw new Error('C: troppi passi'); };
    const scope = parent => ({ vars: new Map(), parent });
    const look = (sc, n) => { for (let s = sc; s; s = s.parent) if (s.vars.has(n)) return s.vars.get(n); throw new Error('C: variabile non dichiarata ' + n); };
    const kindOf = d => (d.ptr ? 'p' : d.type === 'float' ? 'f' : 'i');
    const conv = (t, x) => { // conversione implicita (assegnamento, parametri, return) o esplicita (cast)
      if (t === 'p') { if (x.t !== 'p') throw new Error('C: atteso un puntatore'); return x; }
      if (x.t === 'p') throw new Error('C: puntatore usato come numero');
      if (t === 'f') return { t: 'f', v: Math.fround(x.v) };
      return { t: 'i', v: x.t === 'f' ? (F.roundConv ? Math.round(x.v) : Math.trunc(x.v)) | 0 : x.v };
    };
    const read = c => { if (c.v === undefined) throw new Error('C: variabile non inizializzata'); return { t: c.t, v: c.v }; };
    const store = (c, x) => { c.v = conv(c.t, x).v; return { t: c.t, v: c.v }; };
    const truth = x => (x.t === 'p' ? !!x.v : x.v !== 0);
    function arith(op, a, b) {
      if (a.t === 'p' || b.t === 'p') throw new Error('C: aritmetica sui puntatori');
      const fl = a.t === 'f' || b.t === 'f'; let v;
      if (op === '+') v = a.v + b.v; else if (op === '-') v = a.v - b.v; else if (op === '*') v = a.v * b.v;
      else if (op === '/') {
        if (b.v === 0) throw new Error('C: divisione per zero');
        if (!fl && F.realDiv) return { t: 'f', v: a.v / b.v };
        v = fl ? a.v / b.v : (F.floorDiv ? Math.floor(a.v / b.v) : Math.trunc(a.v / b.v));
      } else if (op === '%') {
        if (b.v === 0) throw new Error('C: divisione per zero');
        if (fl && !F.realDiv) throw new Error('C: % su float');
        v = !fl && F.floorDiv ? a.v - b.v * Math.floor(a.v / b.v) : a.v % b.v;
      }
      return fl ? { t: 'f', v: Math.fround(v) } : { t: 'i', v: v | 0 };
    }
    function lval(x, sc) {
      if (x.e === 'id') return look(sc, x.n);
      if (x.e === 'un' && x.op === '*') { const q = ev(x.x, sc); if (q.t !== 'p' || !q.v) throw new Error('C: * su un non puntatore'); return q.v; }
      throw new Error('C: assegnamento non valido');
    }
    function ev(x, sc) {
      tick();
      switch (x.e) {
        case 'num': return { t: 'i', v: x.v };
        case 'id': return read(look(sc, x.n));
        case 'asg': { const c = lval(x.l, sc), r = ev(x.r, sc); return store(c, x.op === '=' ? r : arith(x.op[0], read(c), r)); }
        case 'pre': case 'post': {
          const kind = F.swapIncr ? (x.e === 'pre' ? 'post' : 'pre') : x.e, c = lval(x.x, sc), old = read(c);
          if (kind === 'post' && F.noPostIncr) return old;
          const nv = store(c, arith(x.op[0], old, { t: 'i', v: 1 }));
          return kind === 'pre' ? nv : old;
        }
        case 'un': {
          if (x.op === '&') { if (x.x.e !== 'id') throw new Error('C: & senza variabile'); const c = look(sc, x.x.n); return { t: 'p', v: F.ptrCopy ? { t: c.t, v: c.v } : c }; }
          if (x.op === '*') return read(lval(x, sc));
          const v = ev(x.x, sc);
          if (x.op === '!') return { t: 'i', v: truth(v) ? 0 : 1 };
          if (v.t === 'p') throw new Error('C: segno su un puntatore');
          return x.op === '+' ? v : (v.t === 'f' ? { t: 'f', v: -v.v } : { t: 'i', v: -v.v | 0 });
        }
        case 'cast': { const v = ev(x.x, sc); return F.castNone ? v : conv(x.type === 'float' ? 'f' : 'i', v); }
        case 'bin': {
          if (x.op === '&&' || x.op === '||') {
            const l = ev(x.l, sc), lt = truth(l), and = x.op === '&&';
            if (!F.noShort && (and ? !lt : lt)) return F.pyLogic ? l : { t: 'i', v: lt ? 1 : 0 };
            const r = ev(x.r, sc);
            if (F.pyLogic) return and ? (lt ? r : l) : (lt ? l : r);
            return { t: 'i', v: (and ? lt && truth(r) : lt || truth(r)) ? 1 : 0 };
          }
          const l = ev(x.l, sc), r = ev(x.r, sc);
          if ('+-*/%'.includes(x.op)) return arith(x.op, l, r);
          const a = l.v, b = r.v, res = { '<': a < b, '<=': a <= b, '>': a > b, '>=': a >= b, '==': a === b, '!=': a !== b }[x.op];
          return { t: 'i', v: res ? 1 : 0 };
        }
        case 'call': {
          if (x.f === 'printf') {
            if (!x.args.length || x.args[0].e !== 'str') throw new Error('C: printf senza formato');
            let k = 1;
            out += x.args[0].v.replace(/%d/g, () => { if (k >= x.args.length) throw new Error('C: argomenti di printf'); const v = ev(x.args[k++], sc); if (v.t === 'p') throw new Error('C: %d con un puntatore'); return Number.isInteger(v.v) ? String(v.v) : String(Math.round(v.v * 1000) / 1000); });
            if (k !== x.args.length) throw new Error('C: argomenti di printf');
            return { t: 'i', v: 0 };
          }
          const fn = funcs[x.f]; if (!fn || fn === funcs.main) throw new Error('C: funzione ' + x.f);
          if (fn.params.length !== x.args.length) throw new Error('C: numero di argomenti');
          const fs = scope(null); // una funzione vede solo i suoi parametri e le sue variabili
          fn.params.forEach((pr, i) => {
            const a = x.args[i];
            if (F.byRef && !pr.ptr && a.e === 'id') { fs.vars.set(pr.name, look(sc, a.n)); return; }
            const c = { t: kindOf(pr), v: undefined }; store(c, ev(a, sc)); fs.vars.set(pr.name, c);
          });
          const r = exec(fn.body, fs);
          if (fn.ret === 'void') return { t: 'i', v: 0 };
          if (!r || !r.ret) throw new Error('C: manca il return');
          return conv(fn.ret === 'float' ? 'f' : 'i', r.ret);
        }
      }
      throw new Error('C: espressione non valida');
    }
    function exec(s, sc) { // restituisce { ret } dopo un return
      tick();
      switch (s.s) {
        case 'block': { const inner = scope(sc); for (const t of s.b) { const r = exec(t, inner); if (r) return r; } return null; }
        case 'decl': for (const d of s.ds) { const c = { t: kindOf(d), v: undefined }; if (d.init) store(c, ev(d.init, sc)); sc.vars.set(d.name, c); } return null;
        case 'expr': ev(s.e, sc); return null;
        case 'if': return truth(ev(s.c, sc)) ? exec(s.th, scope(sc)) : (s.el ? exec(s.el, scope(sc)) : null);
        case 'while': while (truth(ev(s.c, sc))) { const r = exec(s.b, scope(sc)); if (r) return r; } return null;
        case 'do': do { const r = exec(s.b, scope(sc)); if (r) return r; } while (truth(ev(s.c, sc))); return null;
        case 'for': { const fs = scope(sc); if (s.i) exec(s.i, fs); while (!s.c || truth(ev(s.c, fs))) { const r = exec(s.b, scope(fs)); if (r) return r; if (s.st) ev(s.st, fs); } return null; }
        case 'ret': return { ret: s.e ? ev(s.e, sc) : { t: 'i', v: 0 } };
      }
      throw new Error('C: istruzione non valida');
    }
    const msc = scope(null), body = funcs.main.body.b || [funcs.main.body];
    for (const t of body) if (exec(t, msc)) break;
    const vars = {}; for (const [k, c] of msc.vars) vars[k] = c.t === 'p' ? '&' : c.v;
    return { out, vars };
  }

  const TPo = 'Operatori', TPf = 'Controllo di flusso', TPp = 'Puntatori', TPv = 'Variabili e assegnamento', TPfun = 'Funzioni e parametri';
  // codice nella domanda: una riga per paragrafo, in `codice`, con i rientri come spazi non separabili
  const codeTxt = lines => lines.map(l => '`' + l.replace(/^ +/, s => ' '.repeat(s.length)) + '`').join('\n');
  function cOut(lines, flags) { try { const r = cRun(lines.join('\n'), flags); return { out: r.out.replace(/\s+/g, ' ').trim(), vars: r.vars }; } catch (e) { return null; } }
  function cQ(o) { // o: kind, theme, lines, prog, flags, variants, dec (ammette distrattori con decimali), s(vars, out)
    const r = cOut(o.lines); if (!r || !r.out) return null;
    const wrong = [];
    for (const f of o.flags || []) { const w = cOut(o.lines, f); if (w && w.out) wrong.push(w.out); }
    for (const v of o.variants || []) { const w = cOut(v); if (w && w.out) wrong.push(w.out); }
    const nums = r.out.split(' ');
    const filler = () => { const k = ri(0, nums.length - 1); return nums.map((x, i) => (i === k ? String(+x + pick([-2, -1, 1, 2, 10])) : x)).join(' '); };
    return build({ kind: o.kind, theme: o.theme, q: `Che cosa stampa il seguente ${o.prog ? 'programma' : 'frammento di codice'} C?\n` + codeTxt(o.lines), correct: r.out,
      wrong: wrong.filter(w => o.dec || !/\./.test(w)), filler, s: o.s(r.vars, r.out) });
  }
  const traccia = (lines, upto, vs) => { // valori delle variabili dopo le prime «upto» righe
    const r = cOut(lines.slice(0, upto).concat([`printf("${vs.map(() => '%d').join(' ')}\\n", ${vs.join(', ')});`])); if (!r) return null;
    const v = r.out.split(' '); return vs.map((n, i) => `${n} = ${v[i]}`).join(', ');
  };
  function q_cdiv() {
    const t = pick(['qr', 'qr', 'ricomp', 'media']);
    if (t === 'qr') {
      const b = ri(2, 9), a = ri(b + 1, 60) * (Math.random() < 0.3 ? -1 : 1), mk = e => [`int a = ${a}, b = ${b};`, `printf("%d %d\\n", ${e});`];
      return cQ({ kind: 'divisione-intera', theme: TPo, lines: mk('a / b, a % b'), flags: [{ realDiv: true }, { floorDiv: true }], variants: [mk('a % b, a / b')], dec: true,
        s: v => `Tra due int, / è la divisione intera, che tronca verso lo zero: ${a} / ${b} = ${Math.trunc(a / b)}; % è il resto, con il segno del dividendo: ${a} % ${b} = ${a % b}. Vale sempre (a / b) * b + a % b = a.` });
    }
    if (t === 'ricomp') {
      let a, b; do { a = ri(5, 40); b = ri(2, 9); } while (a % b === 0);
      const c = ri(2, 5), mk = (e1, e2) => [`int a = ${a}, b = ${b}, c = ${c};`, `int x = ${e1};`, `int y = ${e2};`, `printf("%d %d\\n", x, y);`];
      return cQ({ kind: 'divisione-intera', theme: TPo, lines: mk('a / b * c', 'a * c / b'), flags: [{ realDiv: true }], variants: [mk('a * c / b', 'a * c / b'), mk('a / (b * c)', 'a * c / b'), mk('a / b * c', 'a / b * c')],
        s: v => `* e / hanno la stessa precedenza e si valutano da sinistra a destra. x: prima ${a} / ${b} = ${Math.trunc(a / b)} (divisione intera), poi ·${c} = ${v.x}. y: prima ${a}·${c} = ${a * c}, poi / ${b} = ${v.y}. Con gli int l'ordine delle operazioni cambia il risultato.` });
    }
    const x = ri(1, 20), y = ri(1, 20), z = ri(1, 20), mk = (e1, e2) => [`int x = ${x}, y = ${y}, z = ${z};`, `int m = ${e1};`, `int k = ${e2};`, `printf("%d %d\\n", m, k);`];
    return cQ({ kind: 'divisione-intera', theme: TPo, lines: mk('(x + y + z) / 3', 'x + y + z / 3'), variants: [mk('(x + y + z) / 3', '(x + y + z) / 3'), mk('x + y + z / 3', 'x + y + z / 3'), mk('(x + y + z) / 3', 'x + y + z')],
      s: v => `m: la somma ${x + y + z} diviso 3 con la divisione intera dà ${v.m}. k: la divisione ha la precedenza sulla somma, quindi si divide solo z: ${z} / 3 = ${Math.trunc(z / 3)}, e k = ${x} + ${y} + ${Math.trunc(z / 3)} = ${v.k}.` });
  }
  function q_ccast() {
    const b = pick([2, 4, 8]); let a; do { a = ri(3, 40); } while (a % b === 0);
    const m = ri(2, 5), F = { int: 'a / b * m', castA: '(float)a / b * m', castP: '(float)(a / b) * m', castB: 'a / (float)b * m' };
    const keys = Object.keys(F), [k1, k2] = shuffle(keys.filter(k => k !== 'castB')).slice(0, 2).concat(Math.random() < 0.25 ? ['castB'] : []).slice(-2);
    const mk = (f1, f2) => [`int a = ${a}, b = ${b}, m = ${m};`, `int x = ${F[f1]};`, `int y = ${F[f2]};`, `printf("%d %d\\n", x, y);`];
    const variants = []; for (const f1 of keys) for (const f2 of keys) if (f1 !== k1 || f2 !== k2) variants.push(mk(f1, f2));
    const q = Math.trunc(a / b), r = a / b * m;
    const why = k => ({ int: `${F.int}: tutto tra interi, ${a} / ${b} = ${q}, poi ·${m} = ${q * m}`, castA: `${F.castA}: il cast vale solo per a, quindi la divisione è reale: ${a / b} · ${m} = ${r}`, castP: `${F.castP}: la divisione tra interi avviene prima del cast, ${a} / ${b} = ${q}, poi ·${m} = ${q * m}`, castB: `${F.castB}: basta un operando float perché la divisione sia reale: ${a / b} · ${m} = ${r}` }[k]);
    return cQ({ kind: 'conversioni-tipo', theme: TPo, lines: mk(k1, k2), flags: [{ castNone: true }, { roundConv: true }], variants: shuffle(variants),
      s: v => `Per x, ${why(k1)}; per y, ${why(k2)}. Assegnando un valore reale a una variabile int la parte decimale si tronca: x = ${v.x}, y = ${v.y}.` });
  }
  function q_cincr() {
    const vs = ['a', 'b'], [X, Y] = shuffle(vs), k = () => ri(2, 4);
    const T1 = (P, Q) => pick([`${P} = ${Q}++ + ${k()};`, `${P} = ++${Q} * ${k()};`, `${P} = ${Q}-- - ${k()};`, `${P} = --${Q} + ${k()};`, `${P} += ${Q}++;`, `${P} -= --${Q};`]);
    const T2 = (P, Q) => pick([`${P} += ${k()};`, `${P} -= ${Q};`, `${P} *= ${k()};`, `${P} %= ${k() + 1};`, `${P} /= ${k()};`, `${P} += ${Q} * ${k()};`, `${P}++;`, `--${P};`]);
    const st = [T1(X, Y), T2(Y, X), Math.random() < 0.5 ? T1(Y, X) : T2(X, Y)];
    const lines = [`int a = ${ri(1, 9)}, b = ${ri(1, 9)};`, ...st, 'printf("%d %d\\n", a, b);'];
    const rev = lines.map(l => l.replace(/^(\w) -= (.+);$/, '$1 = $2 - $1;'));
    return cQ({ kind: 'incremento-composti', theme: TPo, lines, flags: [{ swapIncr: true }, { noPostIncr: true }], variants: rev.join() !== lines.join() ? [rev] : [],
      s: () => `Riga per riga: ${st.map((x, i) => `${x} → ${traccia(lines, i + 2, vs)}`).join('; ')}. Con x++ si usa il valore vecchio di x e poi lo si incrementa; con ++x prima si incrementa e poi si usa il nuovo valore. x += e equivale a x = x + e.` });
  }
  function q_cshort() {
    const a = ri(0, 6), b = ri(0, 6), op = pick(['&&', '||']), corto = Math.random() < 0.65, want = op === '&&' ? !corto : corto;
    const Ls = [[`a > ${a - 1}`, true], [`a > ${a}`, false], [`a == ${a}`, true], [`a == ${a + 1}`, false], ['a != 0', a !== 0], [`a < ${a + 2}`, true], [`a >= ${a + 1}`, false]].filter(([, v]) => v === want);
    const L = pick(Ls)[0], R = pick([`b++ > ${ri(0, 6)}`, `++b > ${ri(0, 6)}`, `(b = ${ri(0, 9)})`, `b-- != 0`, `(b += ${ri(2, 5)}) > ${ri(3, 9)}`, `--b == ${ri(0, 5)}`]);
    const form = pick(['r', 'r', 'if']), decl = `int a = ${a}, b = ${b};`;
    const lines = form === 'r' ? [decl, `int r = ${L} ${op} ${R};`, 'printf("%d %d %d\\n", a, b, r);'] : [decl, `if (${L} ${op} ${R})`, '    a = a + 10;', 'else', '    a = a - 1;', 'printf("%d %d\\n", a, b);'];
    const lv = (cOut([decl, `printf("%d\\n", ${L});`]) || {}).out === '1', salta = op === '&&' ? !lv : lv;
    return cQ({ kind: 'cortocircuito', theme: TPo, lines, flags: form === 'r' ? [{ noShort: true }, { pyLogic: true }] : [{ noShort: true }],
      s: v => `${op === '&&' ? 'Con && la parte destra si valuta solo se la sinistra è vera' : 'Con || la parte destra si valuta solo se la sinistra è falsa'} (cortocircuito). Qui ${L} è ${lv ? 'vera' : 'falsa'}, quindi ${salta ? `${R} non viene eseguita e b resta ${b}` : `si valuta anche ${R}, che porta b a ${v.b}`}. ${form === 'r' ? `Un'espressione logica vale 1 (vera) o 0 (falsa): r = ${v.r}.` : `La condizione è ${v.a === a + 10 ? 'vera' : 'falsa'}, quindi a = ${v.a}.`}` });
  }
  function q_cloop() {
    const t = pick(['sum', 'sum', 'after', 'while2', 'cifre', 'dowhile']), other = c => ({ '<': '<=', '<=': '<', '>': '>=', '>=': '>' }[c]);
    if (t === 'sum') {
      const i0 = ri(0, 3), n = ri(i0 + 3, i0 + 7), cmp = pick(['<', '<=']), step = pick(['i++', 'i++', 'i += 2']), k = ri(2, 3);
      const body = pick(['s += i;', `s += ${k} * i;`, 's = s + i * i;', 'if (i % 2 == 0) s += i;', `s += i % ${k};`]);
      const mk = (c, start) => ['int s = 0;', `for (int i = ${start}; i ${c} ${n}; ${step})`, `    ${body}`, 'printf("%d\\n", s);'];
      const iv = (cOut([`for (int i = ${i0}; i ${cmp} ${n}; ${step})`, '    printf("%d ", i);']) || { out: '' }).out.split(' ').join(', ');
      return cQ({ kind: 'cicli', theme: TPf, lines: mk(cmp, i0), variants: [mk(other(cmp), i0), mk(cmp, i0 + 1), mk(cmp, i0 ? i0 - 1 : 1), mk(other(cmp), i0 + 1)],
        s: v => `i assume i valori ${iv} (con ${cmp} il valore ${n} è ${cmp === '<' ? 'escluso' : 'compreso'}); a ogni giro si esegue «${body}», e alla fine s = ${v.s}.` });
    }
    if (t === 'after') {
      const i0 = ri(0, 2), n = ri(3, 8), cmp = pick(['<', '<=']), k = ri(2, 5);
      const mk = (c, start, pr) => ['int i, c = 0;', `for (i = ${start}; i ${c} ${n}; i++)`, `    c += ${k};`, `printf("%d %d\\n", ${pr || 'i'}, c);`];
      return cQ({ kind: 'cicli', theme: TPf, lines: mk(cmp, i0), variants: [mk(cmp, i0, 'i - 1'), mk(other(cmp), i0), mk(cmp, i0 + 1), mk(other(cmp), i0, 'i - 1')],
        s: v => `Il ciclo termina quando la condizione i ${cmp} ${n} diventa falsa: all'uscita i = ${v.i}, il primo valore che non la soddisfa (non l'ultimo usato nel corpo). Il corpo è eseguito ${v.c / k} volte, quindi c = ${v.c}.` });
    }
    if (t === 'while2') {
      const N = ri(20, 200), d = pick([2, 2, 3]), th = pick([0, 1]);
      const mk = (c, h) => [`int n = ${N}, c = 0;`, `while (n ${c} ${h}) {`, `    n = n / ${d};`, '    c++;', '}', 'printf("%d %d\\n", n, c);'];
      const seq = (cOut([`int n = ${N};`, `while (n > ${th}) {`, `    n = n / ${d};`, '    printf("%d ", n);', '}']) || { out: '' }).out.split(' ').join(', ');
      return cQ({ kind: 'cicli', theme: TPf, lines: mk('>', th), variants: [mk('>=', th), mk('>', th ? 0 : 1)],
        s: v => `n / ${d} è la divisione intera: n assume i valori ${seq}, e il ciclo si ferma quando n > ${th} diventa falsa. Le divisioni fatte sono ${v.c}: n = ${v.n}, c = ${v.c}.` });
    }
    if (t === 'cifre') {
      const N = ri(100, 99999), mk = (c, h, swap) => [`int n = ${N}, s = 0, c = 0;`, `while (n ${c} ${h}) {`, ...(swap ? ['    n /= 10;', '    s += n % 10;'] : ['    s += n % 10;', '    n /= 10;']), '    c++;', '}', 'printf("%d %d\\n", s, c);'];
      return cQ({ kind: 'cicli', theme: TPf, lines: mk('>', 0), variants: [mk('>', 9), mk('>', 0, true)],
        s: v => `Il ciclo stacca le cifre da destra: n % 10 è l'ultima cifra e n /= 10 la toglie (divisione intera). Le cifre di ${N} sono ${String(N).split('').join(', ')}: s = ${v.s} e i giri sono c = ${v.c}.` });
    }
    const x = ri(0, 20), y = ri(0, 20), st = ri(2, 5);
    const mkDo = c => [`int i = ${x}, c = 0;`, 'do {', `    i += ${st};`, '    c++;', `} while (i ${c} ${y});`, 'printf("%d %d\\n", i, c);'];
    const mkWh = c => [`int i = ${x}, c = 0;`, `while (i ${c} ${y}) {`, `    i += ${st};`, '    c++;', '}', 'printf("%d %d\\n", i, c);'];
    return cQ({ kind: 'cicli', theme: TPf, lines: mkDo('<'), variants: [mkWh('<'), mkDo('<='), mkWh('<=')],
      s: v => `Il do-while esegue il corpo almeno una volta e controlla la condizione alla fine di ogni giro${x >= y ? ` (qui la condizione è falsa già all'inizio, ma il corpo viene eseguito lo stesso una volta)` : ''}: i parte da ${x}, aumenta di ${st} a ogni giro e i giri sono ${v.c}, quindi i = ${v.i}.` });
  }
  function q_cswap() {
    const [a, b, c] = shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]).slice(0, 3), three = Math.random() < 0.3;
    const V = three ? { ok: ['t = a;', 'a = b;', 'b = c;', 'c = t;'], inv: ['t = c;', 'c = b;', 'b = a;', 'a = t;'], noT: ['a = b;', 'b = c;', 'c = a;'], tardi: ['t = a;', 'a = b;', 'b = c;', 'c = a;'], nulla: [] }
      : { ok: ['t = a;', 'a = b;', 'b = t;'], ok2: ['t = b;', 'b = a;', 'a = t;'], noT: ['a = b;', 'b = a;'], tardi: ['t = a;', 'a = b;', 'b = a;'], tSbagliata: ['t = b;', 'a = b;', 'b = t;'], nulla: [] };
    const vs = three ? ['a', 'b', 'c'] : ['a', 'b'], key = pick(three ? ['ok', 'ok', 'inv', 'noT', 'tardi'] : ['ok', 'ok', 'ok2', 'noT', 'tardi', 'tSbagliata']);
    const mk = body => [three ? `int a = ${a}, b = ${b}, c = ${c}, t;` : `int a = ${a}, b = ${b}, t;`, ...body, `printf("${vs.map(() => '%d').join(' ')}\\n", ${vs.join(', ')});`];
    const lines = mk(V[key]), riuscito = ['ok', 'ok2', 'inv'].includes(key);
    return cQ({ kind: 'scambio-variabili', theme: TPv, lines, variants: Object.keys(V).filter(k => k !== key).map(k => mk(V[k])),
      s: () => `Riga per riga: ${V[key].map((x, i) => `${x} → ${traccia(lines, i + 2, vs)}`).join('; ')}. ${riuscito ? 'La variabile temporanea t conserva il valore che verrebbe sovrascritto, quindi lo scambio riesce.' : 'Il valore originale di una variabile viene sovrascritto prima di essere salvato, quindi lo scambio non riesce: per scambiare serve una variabile temporanea, usata nell\'ordine giusto.'}` });
  }
  function q_cvalue() {
    const v = ri(2, 9), w = ri(2, 9), k = ri(2, 5), t = pick(['stampa', 'ritorno', 'omonimo', 'ignora', 'scambia']), end = ['    return 0;', '}'];
    if (t === 'stampa') {
      const f = k === 2 ? 'raddoppia' : 'moltiplica';
      return cQ({ kind: 'passaggio-per-valore', theme: TPfun, prog: true, lines: [`void ${f}(int x) {`, `    x = x * ${k};`, '    printf("%d ", x);', '}', 'int main(void) {', `    int a = ${v};`, `    ${f}(a);`, '    printf("%d\\n", a);', ...end], flags: [{ byRef: true }],
        s: () => `In C i parametri si passano per valore: x riceve una copia di a. Dentro la funzione x diventa ${v * k} e viene stampato, ma la variabile a del main resta ${v}.` });
    }
    if (t === 'ritorno') return cQ({ kind: 'passaggio-per-valore', theme: TPfun, prog: true, lines: ['int incrementa(int x) {', `    x = x + ${k};`, '    return x;', '}', 'int main(void) {', `    int a = ${v}, b;`, '    b = incrementa(a);', '    printf("%d %d\\n", a, b);', ...end], flags: [{ byRef: true }],
      s: v2 => `La funzione lavora su una copia di a: restituisce ${v2.b}, che viene assegnato a b, mentre a resta ${v2.a}. L'unico modo di «far uscire» il risultato è il return (o un puntatore).` });
    if (t === 'omonimo') return cQ({ kind: 'passaggio-per-valore', theme: TPfun, prog: true, lines: ['void azzera(int a) {', '    a = 0;', '}', 'int main(void) {', `    int a = ${v};`, '    azzera(a);', `    a = a + ${k};`, '    printf("%d\\n", a);', ...end], flags: [{ byRef: true }],
      s: v2 => `Il parametro a di azzera è una variabile diversa dalla a del main, anche se ha lo stesso nome: azzera mette a 0 la sua copia, la a del main resta ${v} e poi diventa ${v} + ${k} = ${v2.a}.` });
    if (t === 'scambia') {
      const W = v === w ? w + 1 : w;
      const val = ['void scambia(int x, int y) {', '    int t = x;', '    x = y;', '    y = t;', '}', 'int main(void) {', `    int a = ${v}, b = ${W};`, '    scambia(a, b);', '    printf("%d %d\\n", a, b);', ...end];
      const ptr = ['void scambia(int *x, int *y) {', '    int t = *x;', '    *x = *y;', '    *y = t;', '}', 'int main(void) {', `    int a = ${v}, b = ${W};`, '    scambia(&a, &b);', '    printf("%d %d\\n", a, b);', ...end];
      return cQ({ kind: 'passaggio-per-valore', theme: TPfun, prog: true, lines: val, flags: [{ byRef: true }], variants: [ptr],
        s: () => `scambia riceve copie di a e b: scambia le copie x e y, che spariscono alla fine della funzione, e nel main a e b restano ${v} e ${W}. Per scambiare davvero servono i puntatori: scambia(&a, &b) con parametri int *x, int *y.` });
    }
    const L = ['int aggiungi(int x) {', `    x += ${k};`, '    return x * 2;', '}', 'int main(void) {', `    int a = ${v};`, '    aggiungi(a);', '    printf("%d ", a);', '    a = aggiungi(a);', '    printf("%d\\n", a);', ...end];
    return cQ({ kind: 'passaggio-per-valore', theme: TPfun, prog: true, lines: L, flags: [{ byRef: true }], variants: [L.map(l => (l === '    aggiungi(a);' ? '    a = aggiungi(a);' : l))],
      s: v2 => `La prima chiamata aggiungi(a) calcola ${(v + k) * 2} ma il valore restituito non viene salvato, e a (passata per valore) resta ${v}: si stampa ${v}. Con a = aggiungi(a) invece a diventa (${v} + ${k})·2 = ${v2.a}.` });
  }
  function q_cptr() {
    const v = ri(2, 9), w = ri(2, 9), k = ri(2, 5), t = pick(['agg', 'agg', 'scambia', 'alias', 'riassegna']), end = ['    return 0;', '}'];
    if (t === 'agg') return cQ({ kind: 'puntatori', theme: TPp, prog: true, lines: ['void aggiorna(int *p, int k) {', '    *p = *p + k;', '    k = 0;', '}', 'int main(void) {', `    int a = ${v}, k = ${w};`, '    aggiorna(&a, k);', '    printf("%d %d\\n", a, k);', ...end],
      flags: [{ ptrCopy: true }, { byRef: true }, { ptrCopy: true, byRef: true }],
      s: v2 => `aggiorna riceve l'indirizzo di a (&a): scrivendo *p si modifica proprio a, che diventa ${v} + ${w} = ${v2.a}. Il parametro k invece è una copia: k = 0 dentro la funzione non tocca la k del main, che resta ${v2.k}.` });
    if (t === 'scambia') {
      const W = v === w ? w + 1 : w;
      const ptr = ['void scambia(int *x, int *y) {', '    int t = *x;', '    *x = *y;', '    *y = t;', '}', 'int main(void) {', `    int a = ${v}, b = ${W};`, '    scambia(&a, &b);', '    printf("%d %d\\n", a, b);', ...end];
      return cQ({ kind: 'puntatori', theme: TPp, prog: true, lines: ptr, flags: [{ ptrCopy: true }], variants: [ptr.map(l => l.replace('*y = t;', '*y = *x;'))],
        s: () => `scambia riceve gli indirizzi di a e b: t conserva *x (cioè a), poi *x = *y copia b in a e *y = t mette in b il vecchio a. Nel main ora a = ${W} e b = ${v}.` });
    }
    if (t === 'alias') return cQ({ kind: 'puntatori', theme: TPp, lines: [`int a = ${v};`, 'int *p = &a;', `*p += ${k};`, 'a = a * 2;', 'printf("%d %d\\n", a, *p);'], flags: [{ ptrCopy: true }],
      s: v2 => `p contiene l'indirizzo di a, quindi *p e a sono la stessa variabile (alias): *p += ${k} porta a a ${v + k}, poi a = a * 2 dà ${v2.a}, e *p vale anch'esso ${v2.a}.` });
    const R = [`int a = ${v}, b = ${w};`, 'int *p = &a;', `*p = *p + ${k};`, 'p = &b;', '*p = *p * 2;', 'printf("%d %d\\n", a, b);'];
    return cQ({ kind: 'puntatori', theme: TPp, lines: R, flags: [{ ptrCopy: true }], variants: [R.filter(l => l !== 'p = &b;')],
      s: v2 => `Prima p punta ad a: *p = *p + ${k} porta a a ${v2.a}. Poi p = &b fa puntare p a b, quindi *p = *p * 2 raddoppia b: ${w}·2 = ${v2.b}. a non cambia più.` });
  }

  /* ---------- Matematica discreta: insiemi e funzioni (argomenti già trattati) ---------- */
  const lin = (a, b, v) => { // testo di a·v + b
    const A = a === 1 ? v : a === -1 ? '−' + v : (a < 0 ? '−' + Math.abs(a) : a) + v;
    if (a === 0) return String(b < 0 ? '−' + Math.abs(b) : b);
    if (b === 0) return A;
    return `${A} ${b < 0 ? '−' : '+'} ${Math.abs(b)}`;
  };
  function q_comp() {
    const a = pick([-3, -2, -1, 1, 2, 3, 4]), b = ri(-5, 5), c = pick([-3, -2, -1, 2, 3]), d = ri(-6, 6), A = c * a, B = c * b + d;
    return build({ kind: 'composizione', theme: 'Funzioni', q: `Siano f, g : ℤ → ℤ le funzioni f(n) = ${lin(a, b, 'n')} e g(n) = ${lin(c, d, 'n')}. Allora (g ∘ f)(n) =`, correct: lin(A, B, 'n'),
      wrong: [lin(A, a * d + b, 'n'), lin(A, c * b - d, 'n'), lin(c + a, B, 'n'), lin(A, c * b, 'n'), lin(A + 1, B, 'n')], filler: () => lin(ri(-12, 12) || 2, ri(-12, 12), 'n'),
      s: `(g ∘ f)(n) = g(f(n)) = ${c < 0 ? c : c}·(${lin(a, b, 'n')}) ${d < 0 ? '−' : '+'} ${Math.abs(d)} = ${lin(A, B, 'n')}. Si applica prima f, poi g (f ∘ g darebbe ${lin(A, a * d + b, 'n')}).` });
  }
  function q_invaff() {
    const a = pick([2, 3, 4, 5, -2, -3]), b = pick([-7, -5, -3, -1, 2, 4, 6]), x0 = ri(-6, 6), k = a * x0 + b;
    return build({ kind: 'iniettiva-suriettiva-inversa', theme: 'Funzioni', q: `Sia f : ℝ → ℝ la funzione biettiva f(x) = ${lin(a, b, 'x')}. Allora f⁻¹(${k < 0 ? '−' + Math.abs(k) : k}) =`, correct: String(x0).replace('-', '−'),
      wrong: [x0 + 1, x0 - 1, -x0, a * k + b, k - b].map(v => String(v).replace('-', '−')), filler: () => String(ri(-20, 20)).replace('-', '−'),
      s: `f⁻¹(k) è l'unico x con f(x) = k: ${lin(a, b, 'x')} = ${k} ⟹ x = (${k} ${b < 0 ? '+' : '−'} ${Math.abs(b)})/${a} = ${x0}.` });
  }
  function q_class() {
    const a = pick([-3, -2, -1, 1, 2, 3, 5, 0]), b = ri(-5, 5);
    const inj = a !== 0, sur = Math.abs(a) === 1;
    const lab = ['iniettiva e suriettiva', 'iniettiva ma non suriettiva', 'suriettiva ma non iniettiva', 'né iniettiva né suriettiva', 'non è una funzione'];
    const correct = inj ? (sur ? lab[0] : lab[1]) : lab[3];
    return build({ kind: 'iniettiva-suriettiva-inversa', theme: 'Funzioni', q: `La funzione f : ℤ → ℤ, f(n) = ${lin(a, b, 'n')}, è`, correct, wrong: lab.filter(x => x !== correct), filler: () => lab[ri(0, 4)],
      s: a === 0 ? `f è costante: due interi diversi hanno la stessa immagine (non iniettiva) e l'immagine è un solo valore (non suriettiva).` : (sur ? `f è iniettiva (da ${a}x + b = ${a}y + b segue x = y) e ogni intero m è immagine di ${a === 1 ? 'm − b' : 'b − m'}, intero: biettiva.` : `f è iniettiva, ma i valori assunti sono solo ${lin(a, b, 'n').replace('n', 'k')} con k intero: non si raggiunge ogni intero (si dividerebbe per ${Math.abs(a)} uscendo da ℤ), quindi non è suriettiva.`) });
  }
  function q_preim() {
    const k = ri(2, 6), m = ri(0, k - 1), correct = m === 0 ? `[−${k}, ${k}]` : `[−${k}, −${m}] ∪ [${m}, ${k}]`;
    return build({ kind: 'iniettiva-suriettiva-inversa', theme: 'Funzioni', q: `Sia f : ℝ → ℝ, f(x) = x². Allora f⁻¹([${m * m}, ${k * k}]) è`, correct, wrong: [`[${m}, ${k}]`, `[${m * m}, ${k * k}]`, `[−${k}, ${k}]`, `[${m}, ${k}] ∪ [${m * m}, ${k * k}]`, `[−${k * k}, −${m * m}] ∪ [${m * m}, ${k * k}]`], filler: () => `[−${ri(1, 9)}, ${ri(1, 9)}]`,
      s: `x² ∈ [${m * m}, ${k * k}] equivale a ${m} ≤ |x| ≤ ${k}, cioè x ∈ ${correct}: la controimmagine contiene sia i valori positivi sia i negativi.` });
  }
  function q_card() {
    const n = ri(2, 8), m = ri(2, 8);
    if (Math.random() < 0.5) return build({ kind: 'prodotto-cartesiano', theme: 'Insiemi', q: `Se |A| = ${n} e |B| = ${m}, quanti elementi ha il prodotto cartesiano A × B?`, correct: String(n * m), wrong: [n + m, n ** m, m ** n, n * m + n, n * m - 1].map(String), filler: () => String(ri(2, 70)), s: `Le coppie (a, b) sono ${n}·${m} = ${n * m}.` });
    return build({ kind: 'insiemi', theme: 'Insiemi', q: `Quanti sottoinsiemi (vuoto e insieme stesso compresi) ha un insieme di ${n} elementi?`, correct: String(2 ** n), wrong: [2 * n, n * n, 2 ** n - 1, 2 ** (n - 1), 2 ** (n + 1)].map(String), filler: () => String(ri(3, 300)), s: `Ogni elemento sta dentro o fuori dal sottoinsieme: 2${sup(n)} = ${2 ** n} scelte.` });
  }
  const stext = a => (a.length ? '{' + a.join(', ') + '}' : '∅');
  function q_setop() {
    const U = [1, 2, 3, 4, 5, 6, 7, 8, 9], A = U.filter(() => Math.random() < 0.5), B = U.filter(() => Math.random() < 0.5), op = pick(['∪', '∩', '∖']);
    if (!A.length || !B.length) return null;
    const f = { '∪': (x, y) => U.filter(v => x.includes(v) || y.includes(v)), '∩': (x, y) => U.filter(v => x.includes(v) && y.includes(v)), '∖': (x, y) => x.filter(v => !y.includes(v)) };
    const correct = stext(f[op](A, B));
    return build({ kind: 'operazioni-insiemi', theme: 'Insiemi', q: `Siano A = ${stext(A)} e B = ${stext(B)}. Allora A ${op} B =`, correct, wrong: [f['∪'](A, B), f['∩'](A, B), f['∖'](A, B), f['∖'](B, A), A.filter(v => !B.includes(v)).concat(B.filter(v => !A.includes(v))).sort((x, y) => x - y)].map(stext), filler: () => stext(U.filter(() => Math.random() < 0.4)),
      s: `${op === '∪' ? "A ∪ B contiene gli elementi che stanno in A o in B." : (op === '∩' ? "A ∩ B contiene gli elementi che stanno sia in A sia in B." : "A ∖ B contiene gli elementi di A che non stanno in B.")} Risultato: ${correct}.` });
  }

  const BYMAT = {
    'Matematica discreta': [q_comp, q_comp, q_invaff, q_class, q_class, q_preim, q_card, q_setop, q_setop,
      q_perm, q_perm, q_perm, q_cong, q_inverso, q_phi, q_nongen, q_pow, q_base2, q_conteggio, q_dispos,
      q_sigmapi, q_sigmapi, q_tipoconta, q_periodo, q_binom, q_binom],
    'Algebra lineare': [q_cxmul, q_cxdiv, q_cxmod, q_cxinv, q_cxipow, q_cxsq, q_cx1i,
      q_det2, q_det2, q_det3, q_det3, q_det3, q_gauss, q_gauss, q_detprop, q_detprop, q_prod, q_traccia, q_rango, q_rango, q_inv, q_inv],
    'Fondamenti Info': [q_bin2dec, q_hex, q_c2, q_c2, q_hamming, q_parita, q_mem, q_base2],
    'Programmazione': [q_cdiv, q_ccast, q_cincr, q_cincr, q_cshort, q_cshort, q_cloop, q_cloop, q_cloop, q_cswap, q_cvalue, q_cvalue, q_cptr, q_cptr],
  };
  const MAKERS = BYMAT['Matematica discreta'];
  /* covered = insieme dei temi già trattati nei Word (se omesso, tutti): le domande di temi non coperti vengono scartate */
  const make = (mat, covered) => {
    const ms = BYMAT[mat || 'Matematica discreta']; if (!ms) return null;
    for (let i = 0; i < 80; i++) { const q = pick(ms)(); if (q && (!covered || covered.has(q.theme))) { q.m = mat || 'Matematica discreta'; return q; } }
    return null;
  };
  const many = (n, mat, covered) => { const out = []; for (let i = 0; i < n * 6 && out.length < n; i++) { const q = make(mat, covered); if (q) out.push(q); } return out; };
  const disponibile = (mat, covered) => !!BYMAT[mat] && (!covered || BYMAT[mat].some(f => { for (let i = 0; i < 6; i++) { const q = f(); if (q && covered.has(q.theme)) return true; } return false; }));

  return { make, many, disponibile, _t: { gcd, lcm, phi, mod, powmod, inv, compose, cycleToPerm, cyclesOf, orderOf, parityOf, typeOf, C, factorial, MAKERS, BYMAT, cRun } };
})();
if (typeof module !== 'undefined') module.exports = GEN;
