<!-- fonte: _sistema/fonti/Appunti/Mate_2026/17 Novembre/17 Novembre.pdf -->
# Matematica discreta, lezione 16 (17 novembre 2026): appunti a mano di Emanuele
(Trascrizione delle 2 pagine della scansione. La seconda pagina continua con il teorema fondamentale dell'aritmetica e tre foto della lavagna (unicità della fattorizzazione e infinità dei primi): anche questa parte è della lezione 16 del 17 novembre (Moodle: perm5 = 12 nov, perm6 = 17 nov, che contiene proprio il teorema fondamentale). La scansione del 19 nov («19 Novembre/Quadretti - Grande.pdf») è una pagina bianca. Formule in Unicode; tra parentesi quadre le mie note di lettura.)

## Pagina 1

**Divisione Euclidea**
a, b (b ≠ 0)
a = bq + r     0 ≤ r < |b|

**Algoritmo per il calcolo del MCD**

**Identità di Bézout.** Se d = MCD(a, b) allora ∃ A, B t.c. d = Aa + Bb.

a, b numeri dati.
Vogliamo risolvere equazioni della forma [riquadrato in rosso] ax + by = c [freccia su c: «assegnato»] con la condizione che le soluzioni x, y siano intere.
Bézout ⟹ l'equazione si risolve se e soltanto se MCD(a, b) | c [graffa sotto MCD(a, b): «= d»].
12x + 9y = c

x + by   x, y ∈ ℤ   [sta per ax + by]

Se r è un divisore di a e b, r divide ax + by qualunque siano x, y.

Bézout: se c = d allora l'algoritmo permette di trovare una soluzione.
Cosa succede se c = k·d, |k| > 1?

6x + 10y = 8
Guardo a 6x + 10y = 2 [freccia su 2: «MCD»]
p. es. x = 2, y = −1
6(4·2) + 10(4·(−1)) = 4·2 = 8   [sopra: 8 e −4]
[Verificato: 6·2 + 10·(−1) = 2, 6·8 + 10·(−4) = 8.]

ax + by = c
**1° passo:**
Trovo una soluzione ax₀ + by₀ = d
a(kx₀) + b(ky₀) = kd = c

n ∉ {−1, 0, 1}
- n si dice IRRIDUCIBILE se dato n = ab allora o a o b sono ±1;
- n si dice primo se dato n | ab allora n | a oppure n | b.

**Teorema**
n è irriducibile se e soltanto se è primo.

**Dim:**
1) Supponiamo n primo.
Supponiamo n = ab.
Siccome n è primo, n divide uno tra a e b:
diciamo n | a ⟹ a = (kn) [cerchiato] per un certo k
n = ab = (kn)b = kbn
⟹ 1 = kb ⟹ b = k = ±1
⟹ n IRRIDUCIBILE

2) Supponiamo n IRRIDUCIBILE.
Voglio dimostrare che n è primo.
Supponiamo n | ab [sotto: ∃ ab = kn] e che n non divide d [sta per «a»: è il caso n ∤ a].
Affermo che MCD(n, a) = 1.
Bézout: ∃ A, B: An + Ba = 1.
Moltiplico a sx e a dx per b:

## Pagina 2

Aab + Bnb = b   [con le lettere scambiate rispetto alla riga sopra: qui A è il coefficiente di a e B quello di n]
Akn + Bbn = b
n(Ak + Bb) = b [sotto la parentesi: «intero»] ⟹ [riquadrato] n | b

**Teorema (Fondamentale dell'aritmetica)**
Sia n ∈ ℤ, n ∉ {0, 1, −1}.
Allora n si scrive in modo unico come prodotto n = ± p₁ ⋯ pₙ [sta per p_s] dove i pᵢ sono numeri primi positivi.

**Dim**
**esistenza:** esistono numeri irriducibili (2, 3, …).
Se n è irriducibile allora n = ±|n|.
Procedo per induzione.
Suppongo l'esistenza vera per tutti i numeri < |n|.
n ammette una scrittura n = ab dove 1 < a, b < n.
Per ipotesi induttiva
a = p₁ ⋯ p_r
b = q₁ ⋯ q_s
n = ab = p₁ ⋯ p_r q₁ ⋯ q_s

**Unicità**
Supponiamo n = p₁ ⋯ p_r = q₁ ⋯ q_s.
Consideriamo p₁:  p₁ | n = q₁ ⋯ q_s.
p₁ è primo ⟹ p₁ divide uno dei qⱼ (q₁).
p₁ | q₁ ⟹ p₁ | q₁ [verosimilmente p₁ = q₁, come nella foto 1]

[Tre foto della lavagna, collegate da frecce.]

**Foto 1 (due lavagne).**
p₁ p₂ ⋯ p_r = q₁ q₂ ⋯ q_s, con p₁ e q₁ barrati.
Ripeto il ragionamento per p₂ ⟹ p₂ = q₂
p₂ p₃ ⋯ p_r = q₂ q₃ ⋯ q_s, con p₂ e q₂ barrati.
Alla fine dell'iterazione: 1 = q_{r+1} ⋯ q_s.
Siccome qⱼ > 1, questo significa che s = r: p₁ = q₁, p₂ = q₂, …, p_r = q_r.

**Foto 2 (due lavagne).**
2, 3, 5, 7, 11, 13, 17, 19, …
TEOREMA: Esistono infiniti numeri primi.
DIM: Sia S un insieme finito di numeri primi, S = {p₁, …, p_k}.
Considero N = p₁ ⋯ p_k + 1 > 1.
P. es.: S = {2, 3, 5}, N = 31;  S = {2, 5, 11}, N = 111 = 3·37.
TFA ⟹ esiste un primo p | N.
Allora p ∉ S (cioè p ≠ pᵢ, i = 1, …, k).
[Verificato: 2·5·11 + 1 = 111 = 3·37, 2·3·5 + 1 = 31.]

**Foto 3 (due lavagne).** La lavagna in alto ripete quella della foto 1. In basso:
Se fosse p = pᵢ:
N = p₁ ⋯ p_k + 1
1 = N − p₁ ⋯ p_k: otterremmo p | 1, assurdo.

[In fondo alla pagina c'è una freccia «⟹» isolata; il resto è vuoto.]
