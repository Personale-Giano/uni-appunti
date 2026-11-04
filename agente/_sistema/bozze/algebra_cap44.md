# 44. Applicazioni: Indipendenza, Generatori, Basi e Coordinate
## Rileggere gli spazi vettoriali con i sistemi
La lezione 13 applica la teoria dei sistemi a quanto visto sugli spazi vettoriali (cap. 23-26). Dipendenza lineare, generatori e coordinate si riducono tutti allo stesso gesto: scrivere un sistema che ha come colonne i vettori e studiarlo.

## Indipendenza lineare
I vettori v_{1}, …, v_{k} sono **linearmente dipendenti** se esistono coefficienti λ_{1}, …, λ_{k} ∈ 𝕂, non tutti nulli, tali che λ_{1}v_{1} + … + λ_{k}v_{k} = 0; sono **linearmente indipendenti** se l'unica soluzione di questa equazione è λ_{1} = … = λ_{k} = 0.

(In parole povere: per sapere se i vettori sono indipendenti si risolve un sistema omogeneo che ha i vettori come colonne: se ha soltanto la soluzione nulla, lo sono.)

**Esempio.** Siano in ℝ³ i vettori v_{1} = (1, 1, 0), v_{2} = (0, 1, 1), v_{3} = (1, 0, −1). L'equazione diventa il sistema omogeneo λ_{1} + λ_{3} = 0, λ_{1} + λ_{2} = 0, λ_{2} − λ_{3} = 0, con matrice A = (v_{1} | v_{2} | v_{3}) = ( 1 0 1 ; 1 1 0 ; 0 1 −1 ).

Questo sistema ha un'unica soluzione se det A ≠ 0 (cap. 42). Sviluppando lungo la prima riga:

det A = det( 1 0 ; 1 −1 ) + det( 1 1 ; 0 1 ) = −1 + 1 = 0,

quindi esistono infinite soluzioni e **i vettori sono linearmente dipendenti**.

In alternativa si usano le mosse di Gauss: con R_{2} → R_{2} − R_{1} e R_{3} → R_{3} − R_{2} si ottiene ( 1 0 1 ; 0 1 −1 ; 0 0 0 ). A ha rango 2, il che dice di nuovo che ci sono infinite soluzioni (λ_{1}, λ_{2}, λ_{3}). Lo si può leggere anche così: rango 2 vuol dire che Span(v_{1}, v_{2}, v_{3}) ha dimensione 2, quindi i vettori sono dipendenti, perché altrimenti genererebbero uno spazio di dimensione 3.

## Spazio generato
I vettori v_{1}, …, v_{k} sono **generatori** di V, cioè Span(v_{1}, …, v_{k}) = V, se ogni v ∈ V è combinazione lineare di essi: per ogni v esistono λ_{1}, …, λ_{k} ∈ 𝕂 tali che λ_{1}v_{1} + … + λ_{k}v_{k} = v.

**Esempio.** Siano w_{1} = (1, 1, 0), w_{2} = (0, 1, 1), w_{3} = (1, 1, −1). Dato un qualsiasi v = (a, b, c), si studia il sistema λ_{1} + λ_{3} = a, λ_{1} + λ_{2} + λ_{3} = b, λ_{2} − λ_{3} = c, con matrice A = (w_{1} | w_{2} | w_{3}) = ( 1 0 1 ; 1 1 1 ; 0 1 −1 ). Poiché

det A = det( 1 1 ; 1 −1 ) + det( 1 1 ; 0 1 ) = −2 + 1 = −1 ≠ 0,

A è invertibile, ha rango 3 e il sistema ha sempre una soluzione, per qualsiasi v. Quindi Span(w_{1}, w_{2}, w_{3}) = ℝ³.

Con le mosse di Gauss: R_{2} → R_{2} − R_{1} e R_{3} → R_{3} − R_{2} danno ( 1 0 1 ; 0 1 0 ; 0 0 −1 ). A ha rango 3, cioè Span(w_{1}, w_{2}, w_{3}) ha dimensione 3, e allora coincide con ℝ³, perché ogni altro sottospazio ha dimensione strettamente minore di 3.

(In parole povere: se la matrice con i vettori come colonne ha rango massimo, quei vettori raggiungono tutto lo spazio.)

## Basi
Una sequenza v_{1}, …, v_{n} ∈ V è una **base** se i vettori sono indipendenti e generano V; se si sa già che V ha dimensione n, basta controllare **una** delle due proprietà, perché l'altra segue automaticamente (cap. 26).

(In parole povere: una base ha esattamente i vettori che servono per raggiungere tutto lo spazio, nessuno di troppo.)

**Esempio.** I vettori v_{1}, v_{2}, v_{3} di sopra **non** formano una base di ℝ³, perché non sono indipendenti. I vettori w_{1}, w_{2}, w_{3} invece la formano: sono generatori e sono tre, ed ℝ³ ha dimensione 3. Devono quindi per forza essere indipendenti, cosa che si verifica anche subito in modo diretto.

## Coordinate
**Proposizione.** Sia v_{1}, …, v_{n} una base di V. Ogni vettore v ∈ V si scrive in modo unico come v = λ_{1}v_{1} + … + λ_{n}v_{n}.

**Dimostrazione.** I vettori generano, quindi v si può scrivere come loro combinazione lineare. Se lo si potesse fare in due modi, λ_{1}v_{1} + … + λ_{n}v_{n} = μ_{1}v_{1} + … + μ_{n}v_{n}, spostando tutto a sinistra si avrebbe (λ_{1} − μ_{1})v_{1} + … + (λ_{n} − μ_{n})v_{n} = 0. Poiché i vettori sono indipendenti, μ_{i} = λ_{i} per ogni i.

**Definizione.** I coefficienti λ_{1}, …, λ_{n} sono le **coordinate** di v rispetto alla base v_{1}, …, v_{n}, e il vettore colonna (λ_{1}, …, λ_{n}) è il **vettore colonna di coordinate**.

(In parole povere: le coordinate sono la «ricetta» per costruire v con i vettori della base: quante dosi di ciascuno. Se cambia la base, cambia la ricetta, non il vettore.)

**Esempio.** Sia v = (3, 4, 5). Rispetto alla base canonica le coordinate sono proprio i coefficienti di v, perché 3e_{1} + 4e_{2} + 5e_{3} = (3, 4, 5). Rispetto alla base w_{1}, w_{2}, w_{3} si deve invece risolvere λ_{1}w_{1} + λ_{2}w_{2} + λ_{3}w_{3} = v. La soluzione è unica perché det A = −1, e il vettore di coordinate è

A^{-1}v = ( 2 −1 1 ; −1 1 0 ; −1 1 −1 ) · (3, 4, 5) = (7, 1, −4).

Controllo: 7(1, 1, 0) + 1(0, 1, 1) − 4(1, 1, −1) = (3, 4, 5). In alternativa si può risolvere il sistema con Gauss-Jordan.
