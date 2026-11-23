# 55. Esercizi svolti: Tutorato 1
## La scheda del primo tutorato
Questo capitolo raccoglie i 14 esercizi della scheda del primo tutorato (11 novembre 2026). Sono divisi in quattro gruppi: insiemi (esercizi 1-6), funzioni (7-9), relazioni (10-11) e calcolo combinatorio (12-14). Ripassano la prima parte del corso, dai cap. 2-9 (insiemi, partizioni, relazioni) ai cap. 13-20 (funzioni) e 22-28 (contare).

I testi sono riformulati. Le soluzioni che seguono sono scritte qui con i metodi dei capitoli di teoria (**non sono soluzioni ufficiali**), e tutti i conti sono stati ricontrollati anche al calcolatore. La scheda riporta anche le sue soluzioni, e i risultati coincidono. Le note «Attenzione» segnalano gli errori più facili; alcuni compaiono anche negli appunti presi a mano durante il tutorato.

Per la differenza tra insiemi si usa il simbolo del corso, A ∖ B (cap. 4); la scheda scrive A − B.

## Esercizio 1: operazioni, prodotto cartesiano, insieme delle parti
**Testo.** Siano A = {1, c, ⋆}, B = {1, d, b} e C = ∅. Determinare A ∪ B, A ∩ B, A ∖ B e B ∖ A; il prodotto cartesiano A × B; gli insiemi delle parti 𝒫(A), 𝒫(C) e 𝒫(𝒫(C)); le cardinalità |A|, |𝒫(A)| e |A × B|.

**Unione, intersezione, differenze.** L'unico elemento comune è 1 (cap. 3, cap. 4):
- A ∪ B = {1, c, ⋆, d, b} (1 si scrive una volta sola);
- A ∩ B = {1};
- A ∖ B = {c, ⋆} e B ∖ A = {d, b}: come si vede, la differenza non è commutativa.

**Prodotto cartesiano.** A × B è l'insieme delle coppie ordinate (x, y) con x ∈ A e y ∈ B (cap. 3). Si fissa il primo elemento e si fa variare il secondo:

A × B = {(1, 1), (1, d), (1, b), (c, 1), (c, d), (c, b), (⋆, 1), (⋆, d), (⋆, b)}.

La coppia (1, 1) c'è: niente vieta che le due coordinate siano uguali.

**Insiemi delle parti.** I sottoinsiemi di A si elencano per numero di elementi: il vuoto, i tre singoletti, le tre coppie, A stesso (cap. 4):

𝒫(A) = {∅, {1}, {c}, {⋆}, {1, c}, {1, ⋆}, {c, ⋆}, {1, c, ⋆}}.

L'insieme vuoto ha un solo sottoinsieme, se stesso, quindi 𝒫(C) = 𝒫(∅) = {∅}. Questo insieme ha un elemento, e i suoi sottoinsiemi sono due: il vuoto e l'insieme intero {∅}. Quindi

𝒫(𝒫(C)) = 𝒫({∅}) = {∅, {∅}}.

**Cardinalità.** |A| = 3; |𝒫(A)| = 2^{3} = 8, per il teorema sulla cardinalità dell'insieme delle parti (cap. 4, dimostrato per induzione nel cap. 5); |A × B| = |A| · |B| = 3 · 3 = 9 (cap. 3). I conteggi tornano con gli elenchi scritti sopra.

**Attenzione.** ∅ e {∅} sono insiemi diversi (cap. 2): il primo non ha elementi, il secondo ne ha uno, l'insieme vuoto. Per questo |𝒫(∅)| = 2^{0} = 1 e |𝒫(𝒫(∅))| = 2^{1} = 2.

## Esercizio 2: vero o falso sugli insiemi
**Testo.** Dire se le seguenti affermazioni sono vere per tutti gli insiemi A, B, C, giustificando la risposta:
- a) se A ∩ C = B ∩ C, allora A = B;
- b) (A ∪ B) ∩ C = A ∪ (B ∩ C);
- c) A ∩ B = ∅ se e solo se 𝒫(A) ∩ 𝒫(B) = {∅}.

Un'affermazione «per tutti gli insiemi» è falsa appena c'è un controesempio; per dire che è vera serve invece una dimostrazione (cap. 2, quantificatori).

**a) Falsa.** Con A = {1, 2}, B = {1, 3} e C = {1} si ha A ∩ C = {1} = B ∩ C, ma A ≠ B. L'intersezione con C «non vede» gli elementi fuori da C, cioè 2 e 3, che sono proprio quelli in cui A e B differiscono. L'esercizio 4 mostra che, aggiungendo l'ipotesi sull'unione, l'implicazione diventa vera.

**b) Falsa.** Con gli stessi insiemi, (A ∪ B) ∩ C = {1, 2, 3} ∩ {1} = {1}, mentre A ∪ (B ∩ C) = {1, 2} ∪ {1} = {1, 2}.

Si può dire qualcosa di più. Un'inclusione vale sempre: se x ∈ (A ∪ B) ∩ C, allora x ∈ C e x sta in A oppure in B; se x ∈ A, allora x ∈ A ∪ (B ∩ C); se x ∈ B, allora x ∈ B ∩ C. Quindi (A ∪ B) ∩ C ⊆ A ∪ (B ∩ C). L'uguaglianza invece vale esattamente quando A ⊆ C. La formula giusta, sempre vera, è la distributività del cap. 3: (A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C).

**c) Vera.** Servono le due implicazioni.
1. (⟹) Gli elementi di 𝒫(A) ∩ 𝒫(B) sono gli insiemi X con X ⊆ A e X ⊆ B, cioè con X ⊆ A ∩ B. Quindi 𝒫(A) ∩ 𝒫(B) = 𝒫(A ∩ B). Se A ∩ B = ∅, questo è 𝒫(∅) = {∅}.
2. (⟸) Si supponga 𝒫(A) ∩ 𝒫(B) = {∅}. L'insieme A ∩ B è contenuto sia in A sia in B, quindi A ∩ B ∈ 𝒫(A) ∩ 𝒫(B) = {∅}. L'unico elemento di {∅} è ∅, perciò A ∩ B = ∅. ∎

**Attenzione.** È facile scrivere «se A ∩ B = ∅ allora 𝒫(A) ∩ 𝒫(B) = ∅», e l'errore compare anche negli appunti presi al tutorato. È falso per qualunque A e B: ∅ ∈ 𝒫(A) e ∅ ∈ 𝒫(B) sempre (cap. 4), quindi l'intersezione contiene almeno ∅ e non è mai vuota. Con l'esempio degli appunti, A = {1, 3} e B = {2, 5}, si ha 𝒫(A) ∩ 𝒫(B) = {∅}: un insieme con un elemento.

## Esercizio 3: le partizioni di un insieme con tre elementi
**Testo.** Determinare tutte le partizioni di A = {1, 2, 3}.

Una partizione di A è una famiglia di sottoinsiemi non vuoti, a due a due disgiunti, la cui unione è A (cap. 6). Conviene contarle secondo il numero di blocchi, che può essere 1, 2 o 3:
- un blocco: {{1, 2, 3}};
- due blocchi: uno ha un elemento e l'altro due; basta scegliere l'elemento isolato, quindi le partizioni sono tre: {{1}, {2, 3}}, {{2}, {1, 3}}, {{3}, {1, 2}};
- tre blocchi: {{1}, {2}, {3}}.

In tutto le partizioni di A sono **5**.

**Attenzione.** Due cose da non fare. La prima è aggiungere il vuoto: {∅, {1, 2, 3}} non è una partizione, perché i blocchi devono essere non vuoti (cap. 6, Esempio 3). La seconda è contare due volte la stessa partizione scritta in ordine diverso: {{1}, {2, 3}} e {{2, 3}, {1}} sono lo stesso insieme di blocchi. Ricordando il cap. 9, le 5 partizioni corrispondono alle 5 relazioni di equivalenza possibili su {1, 2, 3}.

## Esercizio 4: quando A ∩ C = B ∩ C basta
**Testo.** Siano A e B insiemi. Dimostrare che:
1. se A = B, allora A ∩ C = B ∩ C per ogni insieme C;
2. se esiste un insieme C con A ∪ C = B ∪ C e A ∩ C = B ∩ C, allora A = B.

**Punto 1.** Si sostituisce A con B nella definizione di intersezione (cap. 3): per ogni x,

x ∈ A ∩ C ⟺ (x ∈ A e x ∈ C) ⟺ (x ∈ B e x ∈ C) ⟺ x ∈ B ∩ C.

Quindi A ∩ C = B ∩ C. Un esempio con insiemi particolari non basterebbe, perché la frase riguarda tutti gli insiemi C.

**Punto 2, prima strada: spezzare A in due pezzi.** Ogni insieme si divide nella parte fuori da C e nella parte dentro C: A = (A ∖ C) ∪ (A ∩ C), e allo stesso modo B = (B ∖ C) ∪ (B ∩ C). Le parti dentro C sono uguali per ipotesi. Per le parti fuori da C si usa l'unione: un elemento sta in (A ∪ C) ∖ C se e solo se sta in A oppure in C, ma non in C, cioè se e solo se sta in A ∖ C. Quindi

A ∖ C = (A ∪ C) ∖ C = (B ∪ C) ∖ C = B ∖ C.

I due pezzi di A coincidono con i due pezzi di B, quindi A = B. ∎

**Punto 2, seconda strada: elemento per elemento.** Si dimostra A ⊆ B; l'inclusione B ⊆ A è uguale con i ruoli scambiati, e per la doppia inclusione (cap. 2) segue A = B. Sia x ∈ A. Ci sono due casi:
- se x ∈ C, allora x ∈ A ∩ C = B ∩ C, quindi x ∈ B;
- se x ∉ C, allora x ∈ A ∪ C = B ∪ C, quindi x ∈ B oppure x ∈ C; ma x ∉ C, perciò x ∈ B.

In entrambi i casi x ∈ B. ∎

**Attenzione.** Le due ipotesi servono entrambe. Senza l'unione si ricade nell'esercizio 2 a), falso. Senza l'intersezione l'implicazione è ancora falsa: con A = {1}, B = {2} e C = {1, 2} si ha A ∪ C = B ∪ C = {1, 2}, ma A ≠ B.

## Esercizio 5: appartenenza e inclusione
**Testo.** Siano A = {a, c, e, g} e B = {b, c, f, g}. Quali affermazioni sono vere? a) a ∈ A ∩ B; b) {c, g} = A ∩ B; c) {a, e} ⊆ A ∩ B; d) B ⊆ A; e) {b, f} ⊆ A ∪ B.

Si calcolano prima A ∩ B = {c, g} e A ∪ B = {a, b, c, e, f, g}. Allora:
- a) falsa: a ∈ A ma a ∉ B, quindi a ∉ A ∩ B;
- b) vera;
- c) falsa: {a, e} ⊆ A, ma a ed e non stanno in B;
- d) falsa: b ∈ B ma b ∉ A;
- e) vera: b e f stanno in B, quindi nell'unione.

Sono vere **b) ed e)**.

**Attenzione.** In a) si chiede se un elemento appartiene (∈), in c) ed e) se un insieme è contenuto (⊆): sono due domande diverse (cap. 2). Scrivere a ⊆ A ∩ B oppure {c, g} ∈ A ∩ B sarebbe un errore di notazione.

## Esercizio 6: ricoprimento ma non partizione
**Testo.** Sia X = {1, 2, 3, 4, 5, 6, 7, 8}. Quale di queste famiglie di sottoinsiemi è un ricoprimento di X ma non una partizione? a) {1, 2, 3}, {4, 5, 6}, {7, 8}; b) {1, 2, 3, 4}, {5, 6, 7, 8}; c) {1, 2, 3}, {3, 4, 5}, {6, 7, 8}; d) {1, 2}, {3, 4}, {5, 6}; e) {1, 2, 3, 4, 5, 6, 7, 8}.

Per ogni famiglia si controllano le due cose del cap. 6: l'unione è tutto X? I blocchi sono a due a due disgiunti?
- a) e b): l'unione è X e i blocchi sono disgiunti, quindi sono partizioni.
- c): l'unione è X, ma {1, 2, 3} ∩ {3, 4, 5} = {3} ≠ ∅. È un ricoprimento ma non una partizione.
- d): l'unione è {1, 2, 3, 4, 5, 6} ≠ X, perché mancano 7 e 8: non è nemmeno un ricoprimento.
- e): un solo blocco, X stesso, è una partizione (con un blocco solo).

La risposta è **c)**. È la stessa situazione dell'Esempio 2 del cap. 6, dove {1, 2, 3} e {3, 4, 5} si sovrappongono nell'elemento 3.

## Esercizio 7: immagine e controimmagine di un polinomio
**Testo.** Sia f : ℤ → ℤ, f(n) = n^{2} − 3n + 5. Calcolare f(0), f^{-1}({5}) e f^{-1}({0}). Dire se f è iniettiva, suriettiva, biettiva.

**f(0).** f(0) = 0 − 0 + 5 = 5.

**Controimmagine di {5}.** f^{-1}({5}) è l'insieme degli n ∈ ℤ con f(n) = 5 (cap. 13):

n^{2} − 3n + 5 = 5 ⟺ n^{2} − 3n = 0 ⟺ n(n − 3) = 0 ⟺ n = 0 oppure n = 3.

Entrambi sono interi, quindi f^{-1}({5}) = {0, 3}.

**Controimmagine di {0}.** L'equazione n^{2} − 3n + 5 = 0 ha discriminante Δ = 9 − 20 = −11 < 0: non ha soluzioni reali, e quindi nemmeno intere. Perciò f^{-1}({0}) = ∅.

**Proprietà.** f non è iniettiva, perché f(0) = f(3) = 5 con 0 ≠ 3; non è suriettiva, perché 0 non è immagine di nessun intero; quindi non è biettiva (cap. 14).

**Attenzione.** Il dominio è ℤ, quindi le soluzioni reali non bastano: devono essere intere. Per esempio f^{-1}({7}) = ∅ anche se l'equazione n^{2} − 3n + 5 = 7 ha soluzioni reali, perché sono (3 ± √17)/2, che non sono intere. Inoltre la controimmagine è sempre un insieme, anche quando è vuoto o ha un solo elemento: si scrive f^{-1}({0}) = ∅, non «f^{-1}({0}) non esiste».

## Esercizio 8: rendere biettive tre funzioni
**Testo.** Le funzioni seguenti non sono biettive. Spiegare perché, cambiare dominio e/o codominio in modo da ottenere una funzione biettiva e scriverne l'inversa:
1. f : ℤ → ℤ, f(n) = 3n;
2. f : ℝ → ℝ, f(x) = x^{2} + 2;
3. f : ℝ^{2} → ℝ^{2}, f(x, y) = (x^{2}, x^{2} + y^{2}).

Il metodo è quello del cap. 17: prima si riduce il codominio all'immagine, e la funzione diventa suriettiva; poi, se serve, si restringe il dominio per renderla iniettiva. Ogni volta si ottiene una funzione nuova, che si indica con f̄.

**1. f(n) = 3n.** È iniettiva: 3n_{1} = 3n_{2} implica n_{1} = n_{2}. Non è suriettiva: l'immagine è l'insieme dei multipli di 3, 3ℤ, e per esempio 1 non è raggiunto, perché 3n = 1 non ha soluzioni intere (come la funzione affine su ℤ del cap. 16). Basta cambiare il codominio:

f̄ : ℤ → 3ℤ, n ↦ 3n,  con inversa  f̄^{-1} : 3ℤ → ℤ, m ↦ m/3.

L'inversa ha senso perché ogni m ∈ 3ℤ è un multiplo di 3, quindi m/3 è intero.

**2. f(x) = x^{2} + 2.** Non è iniettiva, perché f(1) = f(−1) = 3. Non è suriettiva: x^{2} ≥ 0, quindi f(x) ≥ 2, e per esempio 0 non è raggiunto. L'immagine è esattamente [2, +∞): se y ≥ 2, allora x = √(y − 2) dà f(x) = y. Si riduce il codominio all'immagine e si tengono solo le x ≥ 0, come per x^{2} nel cap. 17:

f̄ : [0, +∞) → [2, +∞), x ↦ x^{2} + 2,  con inversa  f̄^{-1} : [2, +∞) → [0, +∞), y ↦ √(y − 2).

Controllo: f̄(√(y − 2)) = (y − 2) + 2 = y, e f̄^{-1}(x^{2} + 2) = √(x^{2}) = x, perché x ≥ 0.

**3. f(x, y) = (x^{2}, x^{2} + y^{2}).** Non è iniettiva: f(1, 0) = f(−1, 0) = (1, 1). Per capire se è suriettiva si calcola l'immagine. Se (a, b) = f(x, y), allora a = x^{2} ≥ 0 e b − a = y^{2} ≥ 0, cioè b ≥ a. Viceversa, se a ≥ 0 e b ≥ a, la coppia x = √a, y = √(b − a) dà f(x, y) = (a, a + (b − a)) = (a, b). Quindi l'immagine è

I = {(a, b) ∈ ℝ^{2} : a ≥ 0 e b ≥ a},

e f non è suriettiva: per esempio (−1, 0) ∉ I. Per l'iniettività si sceglie il segno di x e di y, e la scelta più semplice è x ≥ 0 e y ≥ 0, cioè il dominio ℝ^{2}_{≥0} = [0, +∞) × [0, +∞). Si ottiene

f̄ : ℝ^{2}_{≥0} → I, (x, y) ↦ (x^{2}, x^{2} + y^{2}),  con inversa  f̄^{-1} : I → ℝ^{2}_{≥0}, (a, b) ↦ (√a, √(b − a)).

Controllo: f̄^{-1}(x^{2}, x^{2} + y^{2}) = (√(x^{2}), √(y^{2})) = (x, y) per x, y ≥ 0, e f̄(√a, √(b − a)) = (a, b). Per esempio (2, 3) ↦ (4, 13) ↦ (√4, √9) = (2, 3).

**Attenzione.** Il codominio va calcolato, non indovinato. È facile prendere come codominio ℝ^{2}_{≥0}, lo stesso insieme del dominio, e l'errore compare anche negli appunti presi al tutorato. Ma con quel codominio la funzione non è suriettiva: la coppia (1, 0) ha entrambe le coordinate ≥ 0, eppure non è immagine di nulla, perché x^{2} = 1 e x^{2} + y^{2} = 0 non possono valere insieme. E la formula dell'inversa non ha senso, perché darebbe √(0 − 1). Il codominio giusto è l'immagine I, che richiede anche b ≥ a.

## Esercizio 9: trovare g da g ∘ f
**Testo.** Siano f(x) = 2x − 3 e g(x) = ax + b. Sapendo che (g ∘ f)(x) = 6x − 5, determinare g.

In g ∘ f si applica prima f e poi g (cap. 18): (g ∘ f)(x) = g(f(x)). Quindi

g(f(x)) = a(2x − 3) + b = 2ax − 3a + b.

Due polinomi di primo grado sono uguali per ogni x quando hanno gli stessi coefficienti. Confrontando con 6x − 5: 2a = 6, quindi a = 3; −3a + b = −5, quindi b = −5 + 9 = 4. Dunque **g(x) = 3x + 4**.

Controllo: g(f(x)) = 3(2x − 3) + 4 = 6x − 9 + 4 = 6x − 5.

**Attenzione.** Sbagliare l'ordine porta a un'altra risposta, sbagliata. Calcolando f(g(x)) = 2(ax + b) − 3 = 2ax + 2b − 3 e uguagliando a 6x − 5, si troverebbero a = 3 e b = −1, cioè g(x) = 3x − 1: questa g soddisfa f ∘ g = 6x − 5, non g ∘ f. La composizione non è commutativa (cap. 18).

## Esercizio 10: una relazione su tre elementi
**Testo.** Sia A = {−1, 0, 1} e sia R = {(−1, 1), (1, 0), (−1, −1), (1, 1), (0, 0)} ⊆ A × A. Scrivere A × A; dire se R è riflessiva, simmetrica, transitiva, e se è una relazione di equivalenza.

**Il prodotto cartesiano.** Ha 3 · 3 = 9 coppie:

A × A = {(−1, −1), (−1, 0), (−1, 1), (0, −1), (0, 0), (0, 1), (1, −1), (1, 0), (1, 1)}.

**Le proprietà** (cap. 8):
- **riflessiva**: sì, perché (−1, −1), (0, 0) e (1, 1) stanno in R;
- **simmetrica**: no, perché (−1, 1) ∈ R ma (1, −1) ∉ R;
- **transitiva**: no, perché (−1, 1) ∈ R e (1, 0) ∈ R, ma (−1, 0) ∉ R.

Non essendo simmetrica né transitiva, R **non è una relazione di equivalenza**. Per completezza, è invece antisimmetrica: le due coppie di elementi distinti, (−1, 1) e (1, 0), non hanno la coppia rovesciata in R.

**Attenzione.** Per la transitività bisogna guardare tutte le «catene» (x, y), (y, z) in R e controllare che ci sia anche (x, z). Basta una catena che non si chiude per rispondere no, ma la si deve trovare: qui l'unica è (−1, 1), (1, 0). Le catene che passano per una coppia (x, x) si chiudono sempre da sole e non servono.

## Esercizio 11: una relazione di equivalenza definita con i multipli di 5
**Testo.** Sia A = {1, 2, 3, 4, 5, 6} e sia R definita da x R y ⟺ 2x + 3y è un multiplo di 5. Verificare che R è una relazione di equivalenza.

**Riflessività.** Per ogni x ∈ A, 2x + 3x = 5x è un multiplo di 5, quindi x R x.

**Simmetria.** Si supponga x R y, cioè 2x + 3y = 5k con k ∈ ℤ. Bisogna far vedere che anche 2y + 3x è un multiplo di 5. Il trucco è scriverlo usando 2x + 3y:

2y + 3x = 5(x + y) − (2x + 3y) = 5(x + y) − 5k = 5(x + y − k).

Quindi y R x.

**Transitività.** Si supponga x R y e y R z: 2x + 3y = 5k e 2y + 3z = 5h, con k, h ∈ ℤ. Sommando le due uguaglianze si ha 2x + 5y + 3z = 5(k + h), cioè

2x + 3z = 5(k + h) − 5y = 5(k + h − y).

Siccome y è intero, k + h − y è intero: 2x + 3z è un multiplo di 5 e x R z. La relazione è riflessiva, simmetrica e transitiva, quindi **è di equivalenza**.

**Le coppie e le classi.** Provando tutte le coppie, R = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (1, 6), (6, 1)}. Il motivo si vede riscrivendo 2x + 3y = 2(x − y) + 5y: è un multiplo di 5 se e solo se 5 | 2(x − y), e siccome 5 è primo e non divide 2, se e solo se 5 | x − y (cap. 47 e 52). Quindi x R y vuol dire che x e y hanno lo stesso resto nella divisione per 5. In A gli unici elementi distinti con lo stesso resto sono 1 e 6, e le classi di equivalenza (cap. 9) sono {1, 6}, {2}, {3}, {4}, {5}: l'insieme quoziente ha 5 elementi.

**Attenzione.** Un controllo con numeri particolari (per esempio x = 1, y = 6, z = 1) è utile per vedere che i conti tornano, ma non dimostra la transitività: la dimostrazione deve valere per x, y, z qualsiasi, ed è il conto con k e h.

## Esercizio 12: libri sullo scaffale
**Testo.** In una biblioteca ci sono 5 libri di matematica, 4 di informatica e 3 di fisica, tutti diversi. Si scelgono 3 libri e si mettono in fila su uno scaffale. In quanti modi si può fare, se:
1. esattamente due libri sono di matematica?
2. almeno un libro è di informatica?
3. non ci sono libri di fisica?

I libri sono 12, tutti distinti, e l'ordine sullo scaffale conta: ogni risultato è una disposizione semplice di 3 libri tra 12 (cap. 24). In tutto le file possibili sono D_{12,3} = 12 · 11 · 10 = 1320.

**1. Esattamente due di matematica: 420.** Si procede per scelte successive (cap. 22): si scelgono i due libri di matematica tra 5, senza ordine, in (5 su 2) = 10 modi (cap. 26); il terzo libro non deve essere di matematica, quindi si sceglie tra gli altri 4 + 3 = 7; infine i tre libri scelti si mettono in fila in 3! = 6 modi (cap. 23). Il totale è

(5 su 2) · 7 · 3! = 10 · 7 · 6 = **420**.

Lo stesso numero si trova posto per posto: si sceglie in quale dei 3 posti va il libro non di matematica (3 modi), si riempiono in ordine gli altri due posti con libri di matematica (5 · 4 = 20 modi) e si sceglie il libro non di matematica (7 modi): 3 · 20 · 7 = 420.

**Attenzione.** Il conto 5 · 4 · 7 = 140, che compare negli appunti presi al tutorato, dimentica dove va il libro non di matematica: conta solo le file in cui è all'ultimo posto. Le posizioni possibili sono 3, e infatti 140 · 3 = 420. Inoltre «esattamente due» vuol dire che il terzo libro si sceglie tra i 7 non di matematica, non tra i 10 rimasti.

**2. Almeno uno di informatica: 984.** Conviene contare il contrario, come nel cap. 21 per i numeri non divisibili: si tolgono dal totale le file **senza** libri di informatica. Queste si fanno con gli 8 libri di matematica e fisica, quindi sono D_{8,3} = 8 · 7 · 6 = 336. Il risultato è

1320 − 336 = **984**.

Controllo per casi, sommando secondo il numero di libri di informatica (cap. 27: casi diversi si sommano):
- esattamente uno: 4 · (8 su 2) · 3! = 4 · 28 · 6 = 672;
- esattamente due: (4 su 2) · 8 · 3! = 6 · 8 · 6 = 288;
- tutti e tre: (4 su 3) · 3! = 4 · 6 = 24.

La somma è 672 + 288 + 24 = 984.

**Attenzione.** Il conto 4 · 11 · 10 = 440, che compare negli appunti, mette il libro di informatica al primo posto: conta solo le file che cominciano con un libro di informatica. Moltiplicare per i 3 posti non risolve, perché si ottiene 1320, cioè tutte le file: quelle con due o tre libri di informatica vengono contate due o tre volte (672 + 2 · 288 + 3 · 24 = 1320). Con «almeno uno» la strada sicura è il complementare.

**3. Nessun libro di fisica: 504.** Si tolgono i 3 libri di fisica e restano 9 libri, tra cui si dispongono 3 libri in fila: D_{9,3} = 9 · 8 · 7 = **504**.

## Esercizio 13: scegliere numeri divisibili e non divisibili per 4
**Testo.** In quanti modi si possono scegliere quattro numeri divisibili per 4 e tre numeri non divisibili per 4, tutti compresi tra 1 e 20?

Tra 1 e 20 i multipli di 4 sono 4, 8, 12, 16, 20, cioè 5; gli altri numeri sono 20 − 5 = 15. Si sceglie un insieme di numeri, quindi l'ordine non conta e si usano le combinazioni semplici (cap. 26). Le due scelte sono indipendenti e si moltiplicano (cap. 22):

(5 su 4) · (15 su 3) = 5 · (15 · 14 · 13)/(3 · 2 · 1) = 5 · 455 = **2275**.

**Attenzione.** Non si può rispondere (20 su 7): conterebbe anche le scelte con un numero sbagliato di multipli di 4. I due gruppi vanno scelti separatamente, ciascuno nel suo insieme.

## Esercizio 14: gli anagrammi di MATEMATICA
**Testo.** Quanti anagrammi, anche senza senso, ha la parola MATEMATICA? Quanti di questi cominciano e finiscono con la lettera A?

**Tutti gli anagrammi.** La parola ha 10 lettere: M compare 2 volte, A 3 volte, T 2 volte, E, I e C una volta. Per la formula degli anagrammi con lettere ripetute (cap. 23, dove c'è proprio questo esempio):

10!/(2! · 3! · 2!) = 3 628 800/24 = **151 200**.

**Quelli che cominciano e finiscono con A.** Si mettono due A al primo e all'ultimo posto. Restano da ordinare, nei posti centrali, le 8 lettere M, M, A, T, T, E, I, C, dove M e T compaiono 2 volte e le altre una:

8!/(2! · 2!) = 40 320/4 = **10 080**.

**Attenzione.** Le tre A sono uguali, quindi c'è un solo modo di mettere una A in testa e una in coda: non si moltiplica per 3 · 2 come se fossero A diverse. E nelle 8 lettere centrali la A rimasta compare una volta sola, quindi al denominatore non c'è più 3!.

## Riepilogo: quale formula usare per contare
La scheda si chiude con una tabella delle formule del calcolo combinatorio. Dato un insieme di n elementi distinti, per gruppi di k elementi:
- **disposizioni semplici** (l'ordine conta, niente ripetizioni): D_{n,k} = n!/(n − k)! (cap. 24);
- **disposizioni con ripetizione** (l'ordine conta, ripetizioni ammesse): n^{k} (cap. 24);
- **permutazioni** di n elementi, cioè ordinamenti di tutto l'insieme: n! (cap. 23);
- **permutazioni con ripetizione**, cioè anagrammi con frequenze n_{1}, …, n_{r}: n!/(n_{1}! · … · n_{r}!) (cap. 23);
- **combinazioni semplici** (l'ordine non conta, niente ripetizioni): (n su k) = n!/(k! (n − k)!) (cap. 26);
- **combinazioni con ripetizione** (l'ordine non conta, ripetizioni ammesse): (n + k − 1 su k), che per la simmetria dei coefficienti binomiali (cap. 29) è lo stesso numero (k + n − 1 su n − 1) scritto nel cap. 28.

Come sottolineato a lezione (cap. 24), le formule sono la parte facile: il lavoro vero è leggere il problema e chiedersi se l'ordine conta e se le scelte si possono ripetere. Gli esercizi 12 e 13 mostrano le altre due decisioni da prendere: se i casi si moltiplicano o si sommano (cap. 27) e se conviene contare il complementare (cap. 21).
