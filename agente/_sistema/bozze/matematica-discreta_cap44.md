# 44. Divisibilità, Numeri Irriducibili e Numeri Primi
## La divisibilità
**Definizione.** Siano m, n ∈ ℤ. Si dice che **m divide n** (o che m è un **divisore** di n, o che n è **divisibile** per m), e si scrive **m | n**, se esiste un numero intero k tale che n = k · m.

(In parole povere: dire che m | n significa che n si ottiene moltiplicando m per un intero, cioè quando la divisione n : m «viene giusta», senza resto e senza virgola.)

**Esempio.** 3 | 12, perché 12 = 4 · 3. Invece 2 non divide −7: non esiste nessun intero k con 2k = −7, perché 2 · (−3) = −6 e 2 · (−4) = −8. Il libro aggiunge −4 | 20, perché 20 = (−5) · (−4): i divisori possono anche essere negativi.

Due conseguenze immediate della definizione, segnalate dal libro: ogni intero divide 0 (perché 0 = 0 · n), mentre 0 divide soltanto 0; e 1 e −1 dividono qualsiasi n, perché n = n · 1 = (−n) · (−1).

## Non è una relazione di equivalenza
La divisibilità è una **relazione** in ℤ, nel senso del cap. 8: m e n sono in relazione se m | n. Il docente fa notare che **non è una relazione di equivalenza**, perché non è simmetrica: 3 | 12, ma 12 non divide 3. Quindi tutto il discorso sulle classi di equivalenza e sull'insieme quoziente (cap. 9) qui non si applica.

**Attenzione.** «m | n» è un'affermazione, vera o falsa, e non un numero: non va confusa con la frazione m/n. Per esempio 3 | 12 è vera, mentre 12/3 è il numero 4. E l'ordine conta: 3 | 12 è vera, 12 | 3 è falsa.

## Divisori di una somma
**Proposizione.** Siano a, b ∈ ℤ e s = a + b. Se un intero d divide due dei tre numeri a, b, s, allora divide anche il terzo. In particolare:
1. se d divide entrambi gli addendi a e b, allora divide la somma s;
2. se d divide la somma s e uno degli addendi, allora divide anche l'altro addendo.

(In parole povere: in una somma a + b = s, se due dei tre numeri sono multipli di d, lo è per forza anche il terzo.)

Il docente la presenta come una proposizione che sembra innocua, ma che torna utile in moltissime situazioni. La dimostrazione è un esercizio di applicazione della definizione.

**Dimostrazione.**
1. Se d | a e d | b, esistono interi k e l con a = d · k e b = d · l. Allora, per la proprietà distributiva, s = a + b = d · k + d · l = d · (k + l). Quindi s è d moltiplicato per l'intero k + l, cioè d | s.
2. Se d | s e d | a, da s = a + b si ricava b = s − a = s + (−a). Ora d divide entrambi gli addendi s e −a (se a = d · k, allora −a = d · (−k)), quindi per il punto 1 divide la loro somma, che è b. ∎

**Esempio.** 7 | 21 e 7 | 35, quindi 7 | 56 = 21 + 35. E siccome 7 | 56 e 7 | 21, anche 7 | 35 = 56 − 21. Al contrario, 7 non divide 22 = 21 + 1: se lo dividesse, dividendo anche 21 dovrebbe dividere 1, e non è così.

## Invertibili, irriducibili e primi
A fine lezione il docente introduce una terminologia che, avverte, sembra fare a pugni con quella usata di solito a scuola: il perché si capirà più avanti.

**Definizione.** I numeri 1 e −1 si dicono **invertibili**.

(In parole povere: sono gli unici interi che hanno un inverso dentro ℤ, perché 1 · 1 = 1 e (−1) · (−1) = 1. Ogni altro intero diverso da 0 ha un inverso solo fuori da ℤ: l'inverso di 2 è 1/2.)

Un intero si può sempre scrivere come prodotto usando un invertibile: 10 = 10 · 1, 7 = (−7) · (−1). Sono scritture banali, che non dicono nulla. La domanda interessante è se un numero si possa spezzare in un prodotto in cui nessuno dei due fattori è invertibile.

**Definizione.** Sia n ∈ ℤ con n ≠ 0, 1, −1. Si dice che n è **irriducibile** se, ogni volta che n = a · b con a, b ∈ ℤ, almeno uno tra a e b è invertibile. Altrimenti n si dice **riducibile**.

(In parole povere: un numero n è irriducibile quando l'unico modo di scriverlo come prodotto è quello banale, n = n · 1 oppure n = (−n) · (−1). Non si riesce a «ridurlo» in due pezzi più piccoli.)

**Esempio.** 7 è irriducibile: gli unici modi di scriverlo come prodotto sono 7 · 1, 1 · 7, (−7) · (−1) e (−1) · (−7), e in tutti c'è un fattore invertibile. Invece 10 = 2 · 5 è riducibile, e lo è anche −10 = 2 · (−5).

**Definizione.** Sia n ∈ ℤ con n ≠ 0, 1, −1. Si dice che n è **primo** se, ogni volta che n divide un prodotto a · b, allora n divide a oppure n divide b.

(In parole povere: un numero primo non può dividere un prodotto «di nascosto»: se divide a · b, deve dividere almeno uno dei due fattori.)

**Esempio.** 6 non è primo: 6 divide 36 = 4 · 9, ma non divide né 4 né 9. Allo stesso modo, nel libro, 6 | 30 = 3 · 10 ma 6 non divide né 3 né 10.

La definizione di primo è stata data proprio a fine lezione, e il confronto tra le due nozioni è rimandato alla lezione successiva. Per ora conviene notare soltanto che le due definizioni sono diverse: irriducibile parla di come n si scrive come prodotto, primo parla di come n divide i prodotti. Che cosa le leghi, e perché questa terminologia sembri in contrasto con quella di scuola, è proprio quello che resta da capire.
