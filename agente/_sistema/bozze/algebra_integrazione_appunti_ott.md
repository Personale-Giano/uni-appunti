@@ dopo cap18.5
- Lo zero 0_{V} è **unico**, e ogni vettore v ha **un solo** opposto −v.

@@ dopo cap18.12
**Alla lavagna (lezione 2026)** l'unicità fa parte dell'enunciato della proposizione. La dimostrazione è di due righe (aggiunta per chiarezza). Se 0_{V} e 0′ sono entrambi elementi neutri, allora 0_{V} = 0_{V} + 0′ = 0′: nel primo uguale si usa che 0′ è neutro, nel secondo che lo è 0_{V} (con la commutatività). Se u e u′ sono entrambi opposti di v, allora u = u + 0_{V} = u + (v + u′) = (u + v) + u′ = 0_{V} + u′ = u′, per l'associatività. Per questo ha senso parlare dello zero e dell'opposto, con l'articolo determinativo.

@@ dopo cap21.7
- **triangolare** se è triangolare superiore oppure triangolare inferiore (definizione data alla lavagna nella lezione 2026);

@@ dopo cap21.26
**Alla lavagna (lezione 2026)** lo stesso esempio è completato: ( 0 0 ; 0 1 ) **non è antisimmetrica**, perché sulla diagonale c'è un 1 (si veda subito sotto). All'opposto, ( 1 2 ; 3 4 ) non appartiene a nessuna classe: non è diagonale né triangolare (il 2 sta sopra la diagonale e il 3 sotto), non è simmetrica (2 ≠ 3) e non è antisimmetrica (2 ≠ −3, e la diagonale non è nulla).

@@ dopo cap21.37
**Trabocchetto d'Esame.** Le triangolari superiori T_{s}(n) formano un sottospazio, e così le triangolari inferiori T_{i}(n). Invece l'insieme delle matrici **triangolari**, cioè superiori **oppure** inferiori (T_{s}(n) ∪ T_{i}(n)), **non** è un sottospazio: contiene la matrice nulla ed è chiuso per multipli, ma non per somma. Per esempio ( 1 1 ; 0 0 ) è triangolare superiore e ( 0 0 ; 1 0 ) è triangolare inferiore, ma la loro somma ( 1 1 ; 1 0 ) non è né l'una né l'altra. Per questo la proposizione elenca T_{s}(n) e T_{i}(n) separatamente. (Controesempio aggiunto, non presente a lezione.)

@@ dopo cap22.16
**Esempio dalla lavagna (lezione 2026).** In ℝ² siano v₁ = (1, 2) e v₂ = (2, 4). Allora

Span(v₁, v₂) = { a(1, 2) + b(2, 4) | a, b ∈ ℝ } = { (a + 2b, 2a + 4b) | a, b ∈ ℝ } = { (a + 2b)·(1, 2) | a, b ∈ ℝ } = Span((1, 2)).

Il passaggio chiave è raccogliere a + 2b: la prima entrata è (a + 2b)·1 e la seconda (a + 2b)·2. Due vettori, quindi, ma lo Span è solo la retta y = 2x dell'esempio precedente, non tutto il piano: v₂ = 2v₁ non aggiunge nessuna direzione nuova. Il docente lo segnala scrivendo la relazione 2v₁ − v₂ = (0, 0), che è il segno tipico dei vettori linearmente dipendenti (cap. 23). Invece Span((1, 0), (0, 1)) = { (a, b) | a, b ∈ ℝ } = ℝ².

@@ dopo cap23.27
**Alla lavagna (lezione 2026)** il confronto è fatto con {v₁, v₂} = {(1, 2), (2, 4)} del cap. 22 (qui chiamati u₁, u₂ per non confonderli con i vettori sopra) e con {e₁, e₂} = {(1, 0), (0, 1)} (alla lavagna w₁, w₂), riassunti in una tabella:

- {u₁, u₂}: linearmente indipendenti? No, perché 2u₁ − u₂ = 0. Generatori di ℝ²? No, lo Span è solo la retta y = 2x. Base? No.
- {e₁, e₂}: linearmente indipendenti? Sì. Generatori di ℝ²? Sì. Base? Sì.

Le tre domande (l.i.? generatori? base?) sono uno schema utile per ogni insieme di vettori: la terza risposta è «sì» solo se lo sono le prime due.
