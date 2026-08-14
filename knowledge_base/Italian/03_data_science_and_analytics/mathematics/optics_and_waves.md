---
# Metadata
title: "Optics and Waves"
description: "Wave equation, superposition, interference, diffraction, polarization, geometric optics, Fourier optics, and applications to signal processing and imaging"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into optics and waves"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optics, waves, wave-equation, interference, diffraction, polarization, geometric-optics, fourier-optics]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "electromagnetism.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Ottica e onde
Le onde sono ovunque: suono, luce, acqua, segnali radio, ampiezze di probabilità quantistica, fluttuazioni del mercato azionario e vibrazioni delle attivazioni della rete neurale. L’ottica – lo studio della luce – è la scienza ondulatoria più sviluppata e i suoi strumenti matematici (analisi di Fourier, interferenza, diffrazione) si applicano a ogni fenomeno ondulatorio. Understanding waves is essential for signal processing, image analysis, communications, and the physical layer of all modern technology.
---

## L'equazione delle onde
### Equazione generale delle onde
L’equazione d’onda unidimensionale:
∂²u/∂t² = c² ∂²u/∂x²
dove u(x,t) è lo spostamento dell'onda e c è la velocità dell'onda.
### Soluzione Generale (d'Alembert)
u(x,t) = f(x − ct) + g(x + ct)
dove f è un'onda che viaggia verso destra e g è un'onda che viaggia verso sinistra.
### Parametri dell'onda chiave
| Parametro | Simbolo | Unità | Descrizione |
|-----------|--------|------|-------------|
| Ampiezza | A | varia | Cilindrata massima |
| Lunghezza d'onda | λ | metri | Distanza tra creste consecutive |
| Frequenza | f o ν | Hertz (Hz) | Cicli al secondo |
| Periodo | T = 1/f | secondi | Tempo per un ciclo completo |
| Numero d'onda | k = 2π/λ | rad/m | Frequenza spaziale |
| Frequenza angolare | ω = 2πf | rad/s | Frequenza temporale |
| Velocità dell'onda | c = fλ = ω/k | m/s | Velocità di propagazione |
### Onda sinusoidale
u(x,t) = A sin(kx − ωt + φ)
dove φ è la costante di fase.
### Velocità delle onde in diversi mezzi
| Tipo d'onda | Medio | Formula della velocità |
|-----------|--------|---------------|
| Stringa | Tensione T, densità lineare μ | c = √(T/μ) |
| Suono | Modulo di massa B, densità ρ | c = √(B/ρ) |
| Suono (gas ideale) | γ, R, T, M | c = √(γRT/M) |
| Onda EM | Permittività ε, permeabilità μ | c = 1/√(με) |
| Onda EM (vuoto) | ε₀, μ₀ | c = 3 × 10⁸ m/s |
---

## Sovrapposizione e interferenza
### Principio di sovrapposizione
Quando due o più onde si sovrappongono, lo spostamento risultante è la somma dei singoli spostamenti:
u_totale = u₁ + u₂ + ... + uₙ
Ciò vale per le equazioni delle onde lineari.
### Interferenza di due onde
Due onde con la stessa frequenza e ampiezza, differenza di fase Δφ:
u_totale = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Differenza di fase | Risultato | Intensità |
|-----------------|--------|-----------|
| Δφ = 0, 2π, 4π, ... | **Costruttivo** (ampiezza = 2A) | 4I₀ (massimo) |
| Δφ = π, 3π, 5π, ... | **Distruttivo** (ampiezza = 0) | 0 (minimo) |
| Δφ = π/2 | Parziale | 2I₀ |
### Condizioni di interferenza
| Condizione | Digitare | Differenza di percorso |
|-----------|------|-----------|
| Costruttivo | Frangia brillante | ΔL = mλ (m = 0, 1, 2, ...) |
| Distruttivo | Frangia scura | ΔL = (m + ½)λ |
---

## Esperimento della doppia fenditura di Young
La luce passa attraverso due strette fenditure separate dalla distanza d, creando una figura di interferenza su uno schermo alla distanza L.
### Posizioni marginali
| Frangia | Posizione sullo schermo |
|--------|-----|
| Luminoso (massimi) | y_m = mλL/d |
| Scuro (minimo) | y_m = (m + ½)λL/d |
| Spaziatura delle frange | Δy = λL/d |
Questo esperimento dimostrò la natura ondulatoria della luce (Thomas Young, 1801) e in seguito divenne centrale per la meccanica quantistica (dualismo onda-particella).
---

## Diffrazione
La **diffrazione** è la flessione e la diffusione delle onde attorno agli ostacoli e attraverso le aperture.
### Diffrazione da una singola fenditura
La luce che passa attraverso una fessura di larghezza a produce un disegno di frange chiare e scure.
| Caratteristica | Condizione |
|---------|-----------|
| Massimo centrale | Il più ampio e luminoso; larghezza = 2λL/a |
| Minimi (frange scure) | a sin θ = mλ (m = ±1, ±2, ...) |
| Massimi secondari | Approssimativamente tra i minimi; molto più fioco |
### Reticolo di diffrazione
N fenditure equidistanti (spaziatura d) producono massimi molto netti:
d sin θ = mλ (m = 0, 1, 2, ...)
| Immobile | Effetto |
|----------|--------|
| Più fessure (N più grande) | Massimi più nitidi e luminosi |
| Potere risolutivo | R = mN (può distinguere lunghezze d'onda vicine) |
| Applicazioni | Spettroscopia, misurazione della lunghezza d'onda |
### Criterio Rayleigh (limite di risoluzione)
Due sorgenti puntiformi sono risolvibili solo quando il massimo centrale di una cade sul primo minimo dell'altra:
θ_min = 1,22 λ/D
dove D è il diametro dell'apertura.
| Sistema | λ | D | θ_min |
|--------|---|---|-------|
| Occhio umano | 550nm| 5mm| 1,3 × 10⁻⁴ rad (~0,01°) |
| Telescopio spaziale Hubble | 550nm| 2,4 metri| 2,8 × 10⁻⁷rad |
| Radiotelescopio (Arecibo) | 21cm| 305 mt | 8,4 × 10⁻⁴ rad |
---

## Polarizzazione
La **Polarizzazione** descrive l'orientamento dell'oscillazione del campo elettrico in un'onda trasversale.
### Tipi di polarizzazione
| Digitare | Descrizione |
|------|-------------|
| **Lineare** | E oscilla su un piano fisso |
| **Circolare** | E ruota in cerchio (destro o mancino) |
| **Ellittica** | E traccia un'ellisse (più generale) |
| **Non polarizzato** | Miscela casuale di tutte le polarizzazioni (la maggior parte della luce naturale) |
### Legge di Malus
Quando la luce polarizzata passa attraverso un polarizzatore con un angolo θ rispetto alla direzione di polarizzazione:
I = I₀ cos²θ
| Angolo θ | Intensità trasmessa |
|---------|----------------------|
| 0°| 100% (I₀) |
| 30°| 75% |
| 45°| 50% |
| 60°| 25% |
| 90°| 0% (completamente bloccato) |
### Polarizzazione per riflessione (angolo di Brewster)
La luce riflessa nell'angolo di Brewster è completamente polarizzata:
marrone chiaro θ_B = n₂/n₁
| Interfaccia | n₁ | n₂ | θ_B |
|-----------|----|----|-----|
| Aria → vetro | 1.0 | 1,5 | 56,3°|
| Aria → acqua | 1.0 | 1.33| 53,1°|
| Vetro → diamante | 1,5 | 2.42 | 58,1°|
---

## Ottica geometrica
L'ottica geometrica (a raggi) tratta la luce come raggi che viaggiano in linea retta, piegandosi alle interfacce.
### Legge di Snell (rifrazione)
n₁ peccato θ₁ = n₂ peccato θ₂
| Materiale | Indice di rifrazione n |
|----------|-------------|
| Vuoto | 1.000|
| Aria | 1.0003 |
| Acqua | 1.33|
| Vetro (corona) | 1,52 |
| Vetro (selce) | 1,62 |
| Diamante | 2.42 |
### Riflessione interna totale
Quando la luce viaggia da un mezzo più denso a uno meno denso, oltre l'**angolo critico**:
θ_c = arcoseno(n₂/n₁)
Tutta la luce viene riflessa: ecco come funzionano le fibre ottiche.
### Equazione della lente sottile
1/f = 1/d_o + 1/d_i
| Quantità | Significato |
|----------|---------|
| f | Lunghezza focale |
| d_o | Distanza oggetto |
| d_i | Distanza immagine |
| M = −d_i/d_o | Ingrandimento |
| Tipo di obiettivo | f | Immagine |
|-----------|---|-------|
| Convergente (convesso) | Positivo | Reale (se d_o > f) o virtuale |
| Divergente (concavo) | Negativo | Sempre virtuale, verticale, ridotto |
### Equazione dello specchio
Stessa forma dell'equazione della lente: 1/f = 1/d_o + 1/d_i, dove f = R/2 per specchi sferici.
---

## Ottica di Fourier
L'ottica di Fourier tratta l'imaging e la diffrazione come operazioni di trasformata di Fourier.
### Principio chiave
Il modello di diffrazione del campo lontano di un'apertura è la **trasformata di Fourier** della funzione di apertura.
| Apertura | Modello di diffrazione (trasformata di Fourier) |
|----------|----------------------------------------|
| Fessura singola | funzione sin |
| Apertura circolare | Disco d'aria (J₁(r)/r) |
| Apertura rettangolare | Sincronizzazione 2D |
| Grattugia | Funzioni delta discrete |
### Trasformata ottica di Fourier
Una lente esegue una trasformata di Fourier 2D: posizionando un oggetto sul piano focale anteriore si produce la sua trasformata di Fourier sul piano focale posteriore.
### Applicazioni
| Applicazione | Come aiuta l'ottica di Fourier |
|-------------|-------------------------|
| Filtraggio delle immagini | Posiziona le maschere sul piano di Fourier per bloccare/passare le frequenze spaziali |
| Rilevamento dei bordi | Filtraggio passa-alto nel piano di Fourier |
| Riconoscimento di modelli | Correlazione tramite trasformate di Fourier |
| Olografia | Registrazione e ricostruzione dei fronti d'onda |
| Calcolo ottico | Eseguire la trasformata di Fourier alla velocità della luce |
---

## Suono e Acustica
### Proprietà delle onde sonore
| Immobile | Gamma tipica | Unità |
|----------|--------------|------|
| Frequenza | 20 − 20.000 (udito umano) | Hz |
| Velocità (aria, 20°C) | 343| m/s |
| Velocità (acqua) | 1.480| m/s |
| Velocità (acciaio) | 5.960| m/s |
| Soglia di intensità | 10⁻¹² | W/m² |
### Scala dei decibel
β = 10 log₁₀(I/I₀) dB, dove I₀ = 10⁻¹² W/m²
| Suono | Intensità (W/m²) | Livello (dB) |
|-------|-------------|------------|
| Soglia uditiva | 10⁻¹² | 0|
| Foglie fruscianti | 10⁻¹¹ | 10|
| Conversazione normale | 10⁻⁶ | 60|
| Concerto rock | 1| 120|
| Soglia del dolore | 10| 130|
| Motore a reazione | 100| 140|
### Effetto Doppler
Frequenza osservata quando la sorgente e l'osservatore si muovono l'uno rispetto all'altro:
f' = f(v ± v_o)/(v ∓ v_s)
| Scenario | Effetto |
|----------|--------|
| Fonte in avvicinamento | Frequenza più alta (spostamento verso il blu per la luce) |
| Fonte sfuggente | Frequenza più bassa (spostamento verso il rosso per la luce) |
| Applicazioni | Radar, ecografia medica, astronomia (redshift delle galassie) |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto di onda/ottica | Applicazione |
|---------------------|-------------|
| Equazione delle onde | Reti neurali informate dalla fisica, analisi dei dati sismici, elaborazione audio |
| Analisi di Fourier | Fondamenti di elaborazione del segnale, analisi spettrale, estrazione di caratteristiche |
| Trasformata di Fourier | Le CNN eseguono implicitamente l'analisi locale di Fourier; FFT utilizzata nella preelaborazione dei dati |
| Interferenza | Calcolo analogico, reti neurali ottiche |
| Diffrazione | Modelli di formazione delle immagini, algoritmi di deblurring, fotografia computazionale |
| Polarizzazione | Telerilevamento, classificazione dei materiali, analisi di immagini satellitari |
| Ottica geometrica | Modelli di telecamere in visione artificiale, ray tracing per la generazione di dati sintetici |
| Equazione della lente | Calibrazione della fotocamera, stima della profondità, ricostruzione 3D |
| Ottica di Fourier | Calcolo ottico, reti neurali profonde diffrattive (D²NN) |
| Effetto Doppler | Elaborazione del segnale radar, imaging medicale (ecografia Doppler), stima della velocità |
| Scala decibel | Ingegneria delle funzionalità audio, preelaborazione del riconoscimento vocale |
| Teoria del campionamento | Il teorema di Nyquist-Shannon collega la teoria delle onde all'elaborazione del segnale digitale |
---

## Riepilogo
| Argomento | Idea fondamentale | Equazione chiave |
|-------|-----------|-------------|
| Equazione delle onde | Le onde si propagano con velocità c| ∂²u/∂t² = c²∂²u/∂x² |
| Sovrapposizione | Le onde si sommano linearmente | u = u₁ + u₂ |
| Interferenza | La fase determina il rinforzo | Δφ = 2πΔL/λ |
| Diffrazione | Le onde si piegano attorno agli ostacoli | a sin θ = mλ (fenditura singola) |
| Polarizzazione | Orientamento dell'oscillazione | Legge di Malus: I = I₀cos²θ |
| Ottica geometrica | Luce come raggi | Legge di Snell: n₁sinθ₁ = n₂sinθ₂ |
| Ottica di Fourier | Immaginare come trasformata di Fourier | Campo lontano = FT di apertura |
| Effetto Doppler | Spostamento di frequenza dal movimento | f' = f(v ± v_o)/(v ∓ v_s) |
Le onde sono il linguaggio universale dei sistemi oscillanti. Che tu stia elaborando segnali audio, analizzando serie temporali, progettando sistemi di riconoscimento di immagini o costruendo simulazioni fisiche, la matematica delle onde (sovrapposizione, analisi di Fourier, interferenza, diffrazione) fornisce gli strumenti essenziali. L'ottica, in quanto scienza delle onde più matura, offre sia le basi teoriche che le tecniche pratiche che permeano la moderna scienza dei dati.