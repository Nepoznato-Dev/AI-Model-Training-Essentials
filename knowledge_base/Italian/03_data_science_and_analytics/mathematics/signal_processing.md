<!--
---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
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
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Elaborazione del segnale
L'elaborazione del segnale è la scienza che analizza, modifica e sintetizza i segnali, rappresentazioni di quantità fisiche che variano nel tempo, nello spazio o nella frequenza. Audio, immagini, video, dati dei sensori, onde cerebrali, prezzi delle azioni: sono tutti segnali. Gli strumenti matematici di elaborazione del segnale (trasformate di Fourier, filtri, teoria del campionamento) sono fondamentali per l'apprendimento automatico, le comunicazioni, l'imaging medico e praticamente ogni campo che funziona con i dati.
---

## Segnali e Sistemi
### Classificazione dei segnali
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Tempo continuo** | Definito per tutti i t ∈ ℝ | Tensione audio, temperatura |
| **Tempo discreto** | Definito agli indici interi n | Audio campionato, valori dei pixel |
| **Analogico** | Continuo nel tempo e nell'ampiezza | Scanalatura del disco in vinile |
| **Digitale** | Discreti nel tempo e in ampiezza quantizzata | File MP3, immagine JPEG |
| **Periodico** | x(t + T) = x(t) per ogni t | Onda sinusoidale, onda quadra |
| **Aperiodico** | Nessuno schema ripetuto | Discorso, musica |
| **Deterministico** | Completamente prevedibile | Onda sinusoidale |
| **Stocastico** | Contiene casualità | Rumore, prezzi delle azioni |
### Proprietà del sistema
| Immobile | Definizione | Esempio |
|----------|-----------|---------|
| **Lineare** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Filtro passa basso |
| **Invariante nel tempo** | Spostamento nell'input → stesso spostamento nell'output | Qualsiasi filtro fisso |
| **Causale** | L'output dipende solo dagli input presenti e passati | Sistema in tempo reale |
| **Stabile (BIBO)** | Ingresso limitato → uscita limitata | Filtro ben progettato |
| **Senza memoria** | L'output dipende solo dall'ingresso corrente | Amplificatore |
---

## Trasformata di Fourier
La **trasformata di Fourier** decompone un segnale nelle sue frequenze costituenti.
### Trasformata continua di Fourier
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Inverso: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Coppie di trasformata di Fourier
| Dominio del tempo x(t) | Dominio della frequenza X(f) |
|-------------------|---------------------|
| Impulso rettangolare | funzione sin |
| funzione sin | Impulso rettangolare |
| Gaussiano e^{−at²} | Gaussiano (√(π/a))e^{−π²f²/a} |
| Delta di Dirac δ(t) | 1 (tutte le frequenze) |
| Esponenziale complesso e^{j2πf₀t} | δ(f − f₀) |
| Coseno cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Proprietà chiave
| Immobile | Dominio temporale | Dominio della frequenza |
|----------|-------------|-----------|
| Linearità | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Spostamento temporale | x(t − t₀) | X(f)e^{−j2πft₀} |
| Spostamento di frequenza | x(t)e^{j2πf₀t} | X(f − f₀) |
| Convoluzione | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Moltiplicazione | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Differenziazione | dx/dt | j2πf X(f) |
| Teorema di Parseval | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Teorema di convoluzione:** Convoluzione nel tempo = moltiplicazione in frequenza. Questa è la proprietà più importante: trasforma costose operazioni di convoluzione in moltiplicazioni economiche.
### Trasformata discreta di Fourier (DFT)
Per una sequenza x[0], x[1], ..., x[N−1]:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Immobile | Valore |
|----------|-------|
| Ingresso | N campioni reali o complessi |
| Uscita | N contenitori di frequenza complessi |
| Risoluzione di frequenza | f_s/N (dove f_s è la frequenza di campionamento) |
| Frequenza Nyquist | f_s/2 (massima frequenza rappresentabile) |
| Complessità | Calcolo diretto O(N²) |
### Trasformata veloce di Fourier (FFT)
La **FFT** calcola la DFT in O(N log N) anziché O(N²).
| N | O(N²) Operazioni | O(N log N) Operazioni | Accelera |
|---|------------|---------------------||---------|
| 1.024 | 1.048.576| 10.240| 102× |
| 1.048.576| 1,1×10¹²| 20.971.520| 52.428× |
La FFT è uno degli algoritmi più importanti mai inventati. Consente l'elaborazione audio in tempo reale, la compressione delle immagini (JPEG), la comunicazione wireless (OFDM) e l'analisi spettrale.
---

## Trasformata di Laplace
La **trasformata di Laplace** estende la trasformata di Fourier per gestire sistemi instabili e analisi transitorie.
F(s) = ∫₀^∞ f(t) e^{−st} dt, dove s = σ + jω
### Trasformate di Laplace comuni
| f(t) | F(s) | Regione di Convergenza |
|------|------|----------------------|
| δ(t) (impulso) | 1| Tutto s |
| u(t) (passo) | 1/s | Re(s) > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| tⁿu(t) | n!/s^{n+1} | Re(s) > 0 |
| peccato(ωt)u(t) | ω/(s²+ω²) | Re(s) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(s) > 0 |
### Connessione alla trasformata di Fourier
Quando σ = 0 (s = jω), la trasformata di Laplace si riduce alla trasformata di Fourier. La trasformata di Laplace fornisce un quadro più completo includendo informazioni sulla crescita/decadimento (σ).
---

## Trasformazione Z
La **trasformata Z** è l'equivalente in tempo discreto della trasformata di Laplace.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Trasformazioni Z comuni
| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1| Tutti z |
| u[n] (passo) | z/(z−1) | \|z\| >1|
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| sin(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| >1|
### Relazione con altre trasformazioni
| Trasforma | Dominio | Variabile |
|-----------|--------|----------|
| Fourier | Frequenza continua | f o ω |
| Laplace | Frequenza complessa | s = σ + jω |
| Trasformata Z | Frequenza complessa (discreta) | z = e^{sT} |
Il cerchio unitario nel piano z (|z| = 1) corrisponde alla trasformata di Fourier.
---

## Filtri
I filtri lasciano passare o bloccano selettivamente determinati componenti di frequenza.
### Tipi di filtro
| Digitare | Passa | Blocchi | Applicazione |
|------|--------|--------|-------------|
| **Passabasso** | Basse frequenze | Alte frequenze | Smoothing, anti-aliasing |
| **Passa alto** | Alte frequenze | Basse frequenze | Rilevamento dei bordi, rimozione del rumore |
| **Passbanda** | Una gamma di frequenze | Fuori portata | Selezione canale (radio) |
| **Band-stop (tacca)** | Tutto tranne un intervallo | Una gamma specifica | Rimozione del ronzio della linea elettrica |
### Filtri FIR e IIR
| Immobile | FIR (risposta all'impulso finita) | IIR (risposta all'impulso infinita) |
|----------|------------------------------|--------------------------------|
| Risposta all'impulso | Durata finita | Durata infinita |
| Stabilità | Sempre stabile | Può essere instabile |
| Fase | Può essere esattamente lineare | Fase generalmente non lineare |
| Feedback | No | Sì |
| Calcolo | Sono necessari più coefficienti | Meno coefficienti per lo stesso roll-off |
| Progettazione | Finestre, Parks-McClellan | Butterworth, Chebyshev, ellittico |
| Funzione di trasferimento | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Specifiche di progettazione del filtro
| Parametro | Descrizione |
|-----------|-------------|
| **Banda passante** | Gamma di frequenze che dovrebbe passare con una perdita minima |
| **Stopband** | Gamma di frequenze che dovrebbe essere attenuata |
| **Frequenza di taglio** | Confine tra banda passante e banda stop |
| **Ondulazione** | Variazione del guadagno della banda passante (o banda stop) |
| **Roll-off** | Tasso di attenuazione (dB per ottava o decade) |
| **Banda di transizione** | Regione tra banda passante e banda stop |
### Disegni di filtri comuni
| Progettazione | Caratteristiche | Caso d'uso |
|--------|----------------|----------|
| **Butterworth** | Banda passante massimamente piatta, roll-off moderato | Scopo generale |
| **Chebyshev Tipo I** | Ondulazione nella banda passante, roll-off più ripido | Quando il roll-off conta |
| **Chebyshev Tipo II** | Ondulazione nella banda ferma, banda passante piatta | Quando la planarità della banda passante è importante |
| **Ellittico (Cauer)** | Ondulazione in entrambi, roll-off più ripido | Ordine minimo necessario |
| **Bessel** | Fase lineare (ritardo di gruppo massimamente piatto) | Conservazione della forma d'onda |
---

## Teoria del campionamento
### Teorema del campionamento di Nyquist-Shannon
Un segnale continuo può essere perfettamente ricostruito dai suoi campioni se la frequenza di campionamento supera il doppio della frequenza massima:
f_s > 2f_max
| Termine | Definizione |
|------|-----------|
| **Frequenza di campionamento** (f_s) | Numero di campioni al secondo |
| **Tariffa Nyquist** | 2f_max (frequenza di campionamento minima) |
| **Frequenza Nyquist** | f_s/2 (massima frequenza rappresentabile) |
| **Aliasing** | Le alte frequenze si mascherano da basse frequenze quando f_s < 2f_max |
### Tariffe di campionamento comuni
| Applicazione | Vota | Frequenza Nyquist |
|-------------|------|-------------|
| Discorso telefonico | 8kHz | 4kHz |
| CD audio | 44,1kHz | 22,05kHz |
| Audio professionale | 48kHz | 24kHz |
| Audio ad alta risoluzione | 96kHz | 48kHz |
| Video (30 fps) | 30 Hz (temporale) | 15 Hz |
### Antialiasing
Prima del campionamento, un **filtro anti-aliasing** (passa-basso) rimuove le frequenze superiori a f_s/2 per prevenire l'aliasing.
---

## Finestre
Quando analizziamo un segmento finito di un segnale, moltiplichiamo implicitamente per una finestra rettangolare, causando una perdita spettrale. Le **funzioni finestra** riducono questa perdita.
### Finestre comuni
| Finestra | Larghezza del lobo principale | Livello del lobo laterale | Caso d'uso |
|--------|----------------|-----------|----------|
| Rettangolare | Più stretto | −13dB| Quando la risoluzione conta di più |
| Hann | 2× rettangolare | −31dB| Scopo generale |
| Hamming | 2× rettangolare | −41dB | Lobo laterale più vicino ridotto |
| Uomo Nero | 3× rettangolare | −58dB | Gamma dinamica elevata |
| Kaiser | Regolabile | Regolabile (tramite β) | Quando il compromesso è sintonizzabile |
### Perdita spettrale
Moltiplicando un segnale per una finestra si convolge il suo spettro con lo spettro della finestra. I lobi principali più ampi riducono la risoluzione della frequenza; i lobi laterali inferiori riducono le perdite.
---

## Ondine
Le **Wavelet** sono piccole funzioni simili a onde localizzate utilizzate per l'analisi del segnale multi-risoluzione.
### Trasformata wavelet
A differenza della trasformata di Fourier (che fornisce informazioni sulla frequenza globale), la trasformata wavelet fornisce la localizzazione **tempo-frequenza**.
| Trasforma | Risoluzione temporale | Risoluzione di frequenza |
|-----------|----------------|---------------------|
| Fourier | Nessuno (globale) | Eccellente |
| FT a breve termine | Fisso (dimensione della finestra) | Risolto |
| Ondina | Variabile (buono alle alte frequenze) | Variabile (buono a bassa frequenza) |
### Famiglie Wavelet comuni
| Famiglia | Proprietà | Applicazione |
|--------|-----------|-----|
| **Haar** | Semplicissimo, discontinuo | Rilevamento dei bordi, analisi rapida |
| **Daubechies** (dbN) | Appoggio compatto, N momenti evanescenti | Compressione, denoising |
| **Simlet** | Daubechies quasi simmetrici | Distorsione di fase ridotta |
| **Coiflets** | Progettato per le condizioni del momento | Elaborazione del segnale |
| **Morlet** | Sinusoide con finestra gaussiana | Analisi tempo-frequenza |
| **Cappello messicano** | Derivata seconda della gaussiana | Rilevamento delle funzionalità |
### Applicazioni delle wavelet
| Applicazione | Come aiutano le wavelet |
|-------------|-------------|
| Compressione delle immagini (JPEG 2000) | Rappresentazione multi-risoluzione, migliore della DCT per i bordi |
| Denoising | Soglia coefficienti wavelet piccoli (il segnale è in coefficienti grandi) |
| Rilevamento delle funzionalità | Rilevamento dei fronti, rilevamento transitorio nelle serie temporali |
| Analisi ECG | Rilevazione dei complessi QRS, classificazione delle aritmie |
| Analisi sismica | Identificazione degli strati geologici, elaborazione dei segnali sismici |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto di elaborazione del segnale | Applicazione |
|--------------------|-------------|
| Trasformata di Fourier | Caratteristiche spettrali per audio ML, analisi nel dominio della frequenza di serie temporali |
| FFT | Convoluzione veloce nelle CNN (convoluzione spettrale), correlazione efficiente |
| Teorema di convoluzione | Capire come funzionano le CNN (sono filtri appresi) |
| Filtri | Preelaborazione (smooting, denoising), estrazione di feature |
| Teorema del campionamento | Comprendere la discretizzazione, scegliere le frequenze dei sensori, evitare l'aliasing |
| Finestre | STFT per audio ML (spettrogrammi), analisi tempo-frequenza |
| Ondine | Estrazione di caratteristiche per serie temporali, compressione, denoising |
| Trasformata di Laplace/Z | Teoria del controllo per la robotica, comprensione della stabilità del sistema |
| Analisi spettrale | Analisi EEG/fMRI, monitoraggio delle vibrazioni, manutenzione predittiva |
| Tasso di Nyquist | Scelta delle velocità di raccolta dati appropriate per le pipeline ML |
---

## Riepilogo
| Strumento | Dominio | Approfondimento chiave |
|------|--------|-----|
| Trasformata di Fourier | Ora → Frequenza | I segnali sono somme di sinusoidi |
| Trasformata di Laplace | Tempo → Frequenza complessa | Gestisce i transitori e la stabilità |
| Trasformazione Z | Tempo discreto → Complesso | Analisi e progettazione di filtri digitali |
| FFT | Calcolo DFT efficiente | O(N log N) invece di O(N²) |
| Filtri | Selezione della frequenza | Passa ciò che ti serve, blocca ciò che non ti serve |
| Teorema del campionamento | Continuo ↔ discreto | Campiona abbastanza velocemente, non perdi nulla |
| Finestre | Compromesso tempo-frequenza | Risoluzione dell'equilibrio e perdite |
| Ondine | Analisi multirisoluzione | Locale sia nell'orario che nella frequenza |
L'elaborazione del segnale fornisce le basi matematiche per comprendere, analizzare e manipolare i dati. Ogni pipeline di machine learning che funziona con serie temporali, audio, immagini o dati di sensori utilizza implicitamente concetti di elaborazione del segnale. La trasformata di Fourier, in particolare, è probabilmente lo strumento matematico più importante dopo il calcolo per qualsiasi scienziato dei dati.