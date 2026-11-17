# 42. Permutazioni Pari e Dispari
## La parità diventa una proprietà della permutazione
Il teorema della parità (cap. 41) dice che tutte le scritture di una stessa permutazione come composizione di scambi hanno la stessa parità. Allora ha senso attribuire la parità direttamente alla permutazione, senza dover specificare quale scrittura si usa.

**Definizione.** Una permutazione π ∈ Sₙ si dice **pari** se si può scrivere come composizione di un numero pari di scambi, **dispari** se si può scrivere come composizione di un numero dispari di scambi.

(In parole povere: si mescola il mazzo facendo cambiare posto a due carte alla volta e si contano le mosse. Il numero di mosse dipende da come si procede, ma se è pari una volta lo sarà sempre: la permutazione è pari.)

Ogni permutazione è o pari o dispari, e mai tutte e due: almeno una scrittura esiste (cap. 39) e, per il teorema, scritture con un numero pari e con un numero dispari di scambi non possono convivere. Come ha detto il docente, se una permutazione si scrive con 117 scambi, non si riuscirà mai a scriverla con 224: per quanto ci si ingegni, la parità non cambia.

**Esempio.** L'identità è pari: per n ≥ 2 si scrive (1 2) ∘ (1 2), e in ogni caso la si considera composizione di zero scambi, come la scrittura vuota a cui si arriva nel cap. 41. Ogni scambio è dispari.

## La parità di un ciclo
Dal cap. 39, un ciclo di lunghezza ℓ si scrive come composizione di ℓ − 1 scambi. La lunghezza e il numero di scambi differiscono di uno, e togliendo uno a un numero pari si ottiene un dispari (e viceversa). Quindi:

**Proposizione.** Un ciclo di lunghezza ℓ è **pari se ℓ è dispari** ed è **dispari se ℓ è pari**.

(In parole povere: la parità di un ciclo è il contrario della sua lunghezza. Un ciclo di 3 elementi è pari, uno scambio, che ha lunghezza 2, è dispari.)

**Attenzione.** È facile confondersi: (1 2 3) ha lunghezza dispari ma è una permutazione pari, perché è (2 3) ∘ (1 3), cioè due scambi. Prima di rispondere, contare sempre gli scambi, non gli elementi.

## Pari e dispari nella composizione
La parità si comporta molto bene rispetto alla composizione. Se π₁ si scrive con j scambi e π₂ con k scambi, mettendo le due scritture una dopo l'altra si ottiene una scrittura di π₁ ∘ π₂ con j + k scambi. Quindi la parità della composizione segue le regole della somma di numeri pari e dispari:

**Proposizione.** La composizione di due permutazioni è pari se le due hanno la stessa parità, dispari se hanno parità diverse.

È una tabellina molto piccola, perché ci sono solo due casi per ciascuna permutazione:
- pari ∘ pari = pari;
- pari ∘ dispari = dispari;
- dispari ∘ pari = dispari;
- dispari ∘ dispari = pari.

(In parole povere: si sommano i numeri di mosse, e la somma di due numeri è pari esattamente quando sono entrambi pari o entrambi dispari.)

Il docente ha anticipato che questa stessa tabella si ritroverà più avanti in una situazione completamente diversa.

Per l'associatività la regola si estende a più fattori: una composizione è pari se e solo se i fattori dispari sono in numero pari.

## Calcolare la parità dal tipo
Il teorema del cap. 41 non dà un metodo di calcolo, ma la proposizione sui cicli sì. Se π ha tipo (ℓ₁, ℓ₂, …, ℓ_{r}), cioè è composizione di cicli disgiunti di quelle lunghezze (cap. 35), sostituendo ogni ciclo con ℓ_{i} − 1 scambi si ottiene una scrittura di π con

p = (ℓ₁ − 1) + (ℓ₂ − 1) + … + (ℓ_{r} − 1)

scambi. Quindi **π è pari se e solo se p è pari**.

**Esempio (dalla lezione).** Se π ha tipo (3, 5, 6), il ciclo di lunghezza 3 si scrive con 2 scambi, quello di lunghezza 5 con 4 e quello di lunghezza 6 con 5: in tutto 2 + 4 + 5 = 11 scambi. Quindi π è dispari.

**Esempio.** π = (1 4 9) ∘ (2 11 5 7 3) ∘ (8 12) ∘ (6 10 13) ∈ S₁₃ ha tipo (5, 3, 3, 2), e (5 − 1) + (3 − 1) + (3 − 1) + (2 − 1) = 9 è dispari: π è dispari.

## Non servono i cicli disgiunti
Per la parità c'è una scorciatoia ulteriore. La regola della composizione vale per qualsiasi composizione, quindi non serve che i cicli siano disgiunti: se la permutazione è data come composizione di cicli qualunque, basta sommare le parità dei singoli cicli, senza calcolare prima la scomposizione in cicli disgiunti.

**Esempio.** In S₉ la permutazione (2 4 7) ∘ (1 4 5 8 2) ∘ (5 2 7 6) ∘ (6 9 4 8 1 5) è composizione di cicli, non disgiunti, di lunghezze 3, 5, 4 e 6. Questi cicli si scrivono con 2, 4, 3 e 5 scambi, in tutto 14: la permutazione è pari. (Per controllo: facendo il conto, il risultato è il ciclo (5 8 7 6 9), di lunghezza 5, che è davvero pari.)

Il docente fa notare la differenza con il periodo. Per calcolare il periodo la strada maestra passa dal tipo: si scrive la scomposizione in cicli disgiunti, si legge il tipo e si calcola il periodo (cap. 37). Il tipo però si comporta molto male rispetto alla composizione: conoscendo i tipi di due permutazioni non si riesce a ricavare il tipo della loro composizione, bisogna calcolarla. La parità invece si comporta benissimo, e se interessa solo quella si risparmiano due passaggi.

## Quante sono le permutazioni pari
Fissato n, tra le n! permutazioni di Sₙ sono di più quelle pari o quelle dispari? Il docente chiama **Aₙ** l'insieme delle permutazioni pari (osservando che la ragione del nome è un po' strana) e **Dₙ** quello delle dispari; il libro le chiama 𝒫ₙ e 𝒟ₙ. Ogni permutazione è pari o dispari e non tutte e due, quindi Aₙ e Dₙ formano una partizione di Sₙ (cap. 6) e

|Aₙ| + |Dₙ| = n!.

**Proposizione.** Se n ≥ 2, le permutazioni pari e quelle dispari di Sₙ sono lo stesso numero: |Aₙ| = |Dₙ| = n!/2.

(In parole povere: esattamente metà dei mescolamenti si fa con un numero pari di mosse e metà con un numero dispari.)

**Dimostrazione.** Come si trasforma con sicurezza un numero pari in un numero dispari? Aggiungendo uno. Allo stesso modo, una permutazione pari diventa dispari aggiungendo uno scambio alla sua scrittura. Siccome n ≥ 2, lo scambio (1 2) esiste, e si può definire

F : Aₙ → Dₙ,  F(π) = π ∘ (1 2).

Se π si scrive con un numero pari di scambi, π ∘ (1 2) si scrive con uno scambio in più, quindi è dispari: F è ben definita.

Per dimostrare che F è biettiva il docente usa una scorciatoia: invece di controllare iniettività e suriettività, cerca la funzione inversa, perché le funzioni biettive sono esattamente quelle invertibili (cap. 20). Si definisce

G : Dₙ → Aₙ,  G(σ) = σ ∘ (1 2),

che è ben definita per lo stesso motivo. Allora G(F(π)) = π ∘ (1 2) ∘ (1 2) = π, perché lo scambio è l'inverso di se stesso, e allo stesso modo F(G(σ)) = σ. Quindi F e G sono una l'inversa dell'altra, perciò sono biettive. Una biezione tra insiemi finiti esiste solo se hanno lo stesso numero di elementi (cap. 25), quindi |Aₙ| = |Dₙ|, e siccome la somma è n!, ciascuno vale n!/2. ∎

**Come sottolineato a lezione.** F e G hanno esattamente la stessa espressione: prendono una permutazione e la compongono con (1 2). Eppure non sono la stessa funzione, perché dominio e codominio sono scambiati. Dare una funzione vuol dire dare tre cose, dominio, codominio e legge (cap. 10), e due funzioni sono uguali solo se coincidono tutte e tre.

Il caso n = 1 è escluso perché lì l'unica permutazione è l'identità, che è pari: non c'è nessuna permutazione dispari, e la formula n!/2 non avrebbe senso.

**Esempio.** In S₅ ci sono 5! = 120 permutazioni: 60 pari e 60 dispari. In S₄ sono 24: 12 pari e 12 dispari.

Con questo il discorso sulle permutazioni è concluso, e si passa all'aritmetica.
