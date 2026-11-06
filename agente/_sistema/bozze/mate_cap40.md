# 40. La Parità di una Scrittura in Scambi
## Che cosa non cambia tra due scritture
Nel cap. 39 si è visto che una permutazione si scrive in tanti modi come composizione di scambi: (2 3) si scrive con uno scambio, ma anche con tre. Il numero di scambi quindi non è determinato dalla permutazione. Che cosa resta allora fisso? Per dirlo serve una definizione.

**Definizione.** Una scrittura s₁ ∘ … ∘ s_{k}, dove tutti gli s_{i} sono scambi, ha **parità pari** se k è pari e **parità dispari** se k è dispari. Due scritture, con k e h scambi, hanno **la stessa parità** se k e h sono entrambi pari o entrambi dispari.

(In parole povere: si contano le mosse elementari e si guarda solo se sono in numero pari o dispari, senza badare a quali siano.)

La definizione riguarda soltanto come sono scritte le espressioni, non se siano uguali come permutazioni.

**Esempio.** (2 3) e (1 3) ∘ (1 2) ∘ (1 3) hanno la stessa parità: una e tre mosse. Invece (1 2) ∘ (2 3) e (1 3) ∘ (1 2) ∘ (2 3) hanno parità diversa, perché usano due e tre scambi. Per dire questo non serve sapere se le due espressioni diano la stessa permutazione.

## L'inversa ha la stessa parità
Ogni scambio è l'inverso di se stesso, perché s² = id. L'inversa di una composizione di funzioni biettive, come ricordato a lezione, si ottiene invertendo ciascuna funzione e componendo nell'ordine opposto. Quindi:

(s₁ ∘ … ∘ s_{k})⁻¹ = s_{k}⁻¹ ∘ … ∘ s₁⁻¹ = s_{k} ∘ … ∘ s₁.

Si verifica direttamente: in (s₁ ∘ … ∘ s_{k}) ∘ (s_{k} ∘ … ∘ s₁) si ha s_{k} ∘ s_{k} = id, poi s_{k−1} ∘ s_{k−1} = id, e così via fino all'identità.

Per invertire una composizione di scambi basta quindi scrivere gli stessi scambi al contrario. Il numero di scambi è lo stesso, perciò **una scrittura e quella della sua inversa hanno la stessa parità**.

**Esempio.** Se π = (1 2) ∘ (2 3), allora π⁻¹ = (2 3) ∘ (1 2): due scambi in entrambi i casi.

## Il teorema
**Teorema (parità).** Se una permutazione si scrive in due modi come composizione di scambi, π = s₁ ∘ … ∘ s_{k} = t₁ ∘ … ∘ t_{h}, allora le due scritture hanno la stessa parità: k e h sono entrambi pari o entrambi dispari.

(In parole povere: il numero di mosse può cambiare, ma solo di un numero pari. Se una permutazione si ottiene con un numero dispari di scambi, non si riuscirà mai a ottenerla con un numero pari.)

Lo si vede nell'esempio di partenza. Uno scambio si può scrivere con 3, 5, 7, … scambi, aggiungendo coppie di scambi uguali, che si annullano. Il teorema dice che non si potrà mai scriverlo con 2, 4 o 6. L'esempio non è una dimostrazione: è solo un caso in cui il fenomeno si vede.

A lezione il teorema è soltanto enunciato: il tempo è finito prima della dimostrazione, che il docente rimanda.
