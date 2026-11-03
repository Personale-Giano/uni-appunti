# Stile dei riassunti (ricavato dai Word esistenti e dalle correzioni di Emanuele)

## Impostazione
- Via di mezzo tra discorsivo ed elenchi: **non wall of text, non solo bullet**. Paragrafi di 3-6 righe che spiegano il perché, elenchi solo quando c'è davvero una lista (proprietà, passi, casi). Correzione ripetuta di Emanuele: "troppo bullet point, stile leggermente più discorsivo".
- Tono: italiano formale ma chiaro, da manuale universitario; spiega il ragionamento, non solo la definizione.
- Un esempio concreto per ogni concetto importante (come nei capitoli esistenti: `z = 2+5i`, `A = {1,2}`, `x = 2^31-1`).

## Struttura di un capitolo
1. Titolo capitolo numerato: `N. Titolo` (grassetto rosso nel Word).
2. Sezioni con sottotitolo (grassetto arancione).
3. Dentro: definizione in forma discorsiva con i termini chiave in **grassetto**, proprietà in elenco, esempio svolto, dimostrazione quando fatta a lezione (passi numerati con la motivazione di ogni passaggio).
4. Casi a rischio: sezione "Trabocchetto d'Esame" o nota "Come sottolineato a lezione" quando il docente lo ha detto (compare in Algebra e Mate discreta).
5. Chiusura con il collegamento al capitolo successivo o la motivazione ("Come sottolineato a lezione… serve l'argomento successivo").

## Formattazione (bozze per il sito)
- `# N. Titolo` per il capitolo, `## Sottotitolo` per le sezioni. **grassetto** per i termini chiave, ~corsivo~ (tilde) per i termini presentati e le variabili esplicative: mai `*corsivo*` con un asterisco.
- Definizioni e risultati con l'etichetta in grassetto all'inizio del paragrafo: `**Definizione.**`, `**Proposizione.**`, `**Teorema (Binet).**`: da lì il Quaderno genera le schede di ripasso.
- Elenchi con `- `. Formule in testo con simboli Unicode (ℕ ℤ ℚ ℝ ℂ ∈ ⊆ ∪ ∩ ∀ ∃ ⟹ ⟺), apici e pedici con `^{}` e `_{}`. Mai un paragrafo che finisce con «=»: la formula va scritta per intero.
- Programmazione: il codice C in blocchi ``` (e `codice` in linea), con i `\n` scritti come tali.
- Numerazione continuativa: il primo capitolo nuovo riprende dal numero successivo a quello sul sito. Rimandi solo a capitoli che esistono; mai «questo Word».

## Cose da evitare
- Frasi di NotebookLM tipo "come ricordato nell'audio", "Le fonti forniscono": non vanno nel testo. Scrivere "a lezione" solo se il docente l'ha davvero detto.
- Rimandi a "fonti"/"documento"; numeri di citazione; emoji.
- Terminologia incoerente: usare quella del docente (es. "ricoprimento", "insieme quoziente", "campo", "scalare").

## Correzioni di Emanuele (registro: aggiungere una riga a ogni feedback)
- 1 ott 2026 (Algebra, NotebookLM): "troppo bullet point, non fare neanche un wall of text: elenchi solo quando servono, stile leggermente più discorsivo".
- 5 ott 2026: i capitoli nuovi devono replicare struttura, tono e numerazione dei precedenti; un capitolo per volta; prima l'elenco dei macro-argomenti.
- 7 ott 2026 (Fondamenti): "meno tutto a bullet point, stile un po' più discorsivo in generale".
- 19 ott 2026 (regola permanente, tutte le materie): dopo ogni **definizione** scrivere subito una parentesi «In parole povere: …» con la spiegazione molto più comprensibile (1-3 frasi, linguaggio quotidiano, un esempio banale o un'immagine mentale).
