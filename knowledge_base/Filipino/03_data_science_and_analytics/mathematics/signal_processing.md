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
# Pagproseso ng Signal
Ang pagpoproseso ng signal ay ang agham ng pagsusuri, pagbabago, at pag-synthesis ng mga signal — mga representasyon ng mga pisikal na dami na nag-iiba-iba sa paglipas ng panahon, espasyo, o dalas. Audio, mga larawan, video, data ng sensor, brain wave, mga presyo ng stock — lahat ay mga signal. Ang mga mathematical na tool ng pagpoproseso ng signal (Fourier transforms, filters, sampling theory) ay pundasyon sa machine learning, komunikasyon, medical imaging, at halos lahat ng field na gumagana sa data.
---

## Mga Senyales at Sistema
### Pag-uuri ng Signal
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Patuloy na oras** | Tinukoy para sa lahat ng t ∈ ℝ | Boltahe ng audio, temperatura |
| **Discrete-time** | Tinukoy sa mga integer na indeks n | Na-sample na audio, mga halaga ng pixel |
| **Analog** | Tuloy-tuloy sa oras at amplitude | Vinyl record groove |
| **Digital** | Discrete sa oras at quantised amplitude | MP3 file, JPEG na imahe |
| **Pana-panahon** | x(t + T) = x(t) para sa lahat ng t | Sine wave, square wave |
| **Aperiodic** | Walang umuulit na pattern | Pagsasalita, musika |
| **Deterministic** | Ganap na mahuhulaan | Sine wave |
| **Stochastic** | Naglalaman ng randomness | Ingay, mga presyo ng stock |
### System Properties
| Ari-arian | Kahulugan | Halimbawa |
|----------|-----------|---------|
| **Linear** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Low-pass na filter |
| **Time-invariant** | Shift sa input → parehong shift sa output | Anumang nakapirming filter |
| **Causal** | Ang output ay nakasalalay lamang sa kasalukuyan at nakaraang mga input | Real-time na sistema |
| **Matatag (BIBO)** | Bounded input → bounded output | Mahusay na disenyong filter |
| **Walang memorya** | Ang output ay nakasalalay lamang sa kasalukuyang input | Amplifier |
---

## Fourier Transform
Ang **Fourier transform** ay nagde-decompose ng signal sa mga constituent frequency nito.
### Patuloy na Fourier Transform
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Baliktad: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Fourier Transform Pares
| Domain ng Oras x(t) | Dalas ng Domain X(f) |
|-------------------|----------------------|
| Parihabang pulso | sync function |
| sync function | Parihabang pulso |
| Gaussian e^{−at²} | Gaussian (√(π/a))e^{−π²f²/a} |
| Dirac delta δ(t) | 1 (lahat ng frequency) |
| Complex exponential e^{j2πf₀t} | δ(f − f₀) |
| Cosine cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Mga Pangunahing Katangian
| Ari-arian | Domain ng Oras | Domain ng Dalas |
|----------|-------------|----------------|
| Linearity | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Paglipat ng oras | x(t − t₀) | X(f)e^{−j2πft₀} |
| Paglipat ng dalas | x(t)e^{j2πf₀t} | X(f − f₀) |
| Convolution | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Multiplikasyon | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Differentiation | dx/dt | j2πf X(f) |
| Parseval's theorem | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Convolution theorem:** Convolution in time = multiplication in frequency. Ito ang pinakamahalagang pag-aari — ginagawa nitong murang pagpaparami ang mga mamahaling operasyon ng convolution.
### Discrete Fourier Transform (DFT)
Para sa isang sequence x[0], x[1], ..., x[N−1]:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Ari-arian | Halaga |
|----------|-------|
| Input | N tunay o kumplikadong mga sample |
| Output | N complex frequency bins |
| Resolusyon ng dalas | f_s/N (kung saan ang f_s ay sampling rate) |
| dalas ng Nyquist | f_s/2 (maximum representable frequency) |
| Pagiging kumplikado | O(N²) direktang pagkalkula |
### Mabilis na Fourier Transform (FFT)
Kinakalkula ng **FFT** ang DFT sa O(N log N) sa halip na O(N²).
| N | O(N²) Mga Operasyon | O(N log N) Operations | Bilis |
|---|-----------------|----------------------|---------|
| 1,024 | 1,048,576 | 10,240 | 102× |
| 1,048,576 | 1.1 × 10¹² | 20,971,520 | 52,428× |
Ang FFT ay isa sa pinakamahalagang algorithm na naimbento. Nagbibigay-daan ito sa real-time na pagproseso ng audio, image compression (JPEG), wireless communication (OFDM), at spectral analysis.
---

## Laplace Transform
Ang **Laplace transform** ay nagpapalawak ng Fourier transform upang mahawakan ang mga hindi matatag na sistema at lumilipas na pagsusuri.
F(s) = ∫₀^∞ f(t) e^{−st} dt, kung saan s = σ + jω
### Mga Karaniwang Pagbabagong Laplace
| f(t) | F(s) | Rehiyon ng Convergence |
|------|------|----------------------|
| δ(t) (putok) | 1 | Lahat ng |
| u(t) (hakbang) | 1/s | Re(s) > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| tⁿu(t) | n!/s^{n+1} | Re(s) > 0 |
| kasalanan(ωt)u(t) | ω/(s²+ω²) | Re(s) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(s) > 0 |
### Koneksyon sa Fourier Transform
Kapag σ = 0 (s = jω), ang pagbabagong Laplace ay bumababa sa pagbabagong Fourier. Ang pagbabagong Laplace ay nagbibigay ng mas kumpletong larawan sa pamamagitan ng pagsasama ng impormasyon tungkol sa paglaki/pagkabulok (σ).
---

## Z-Transform
Ang **Z-transform** ay ang discrete-time na katumbas ng Laplace transform.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Mga Karaniwang Z-Transform
| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1 | Lahat ng z |
| u[n] (hakbang) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| kasalanan(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Relasyon sa Iba Pang Pagbabago
| Ibahin ang anyo | Domain | Variable |
|-----------|--------|----------|
| Fourier | Patuloy na dalas | f o ω |
| Laplace | Kumplikadong dalas | s = σ + jω |
| Z-transform | Kumplikadong dalas (discrete) | z = e^{sT} |
Ang bilog ng unit sa z-plane (|z| = 1) ay tumutugma sa Fourier transform.
---

## Mga filter
Ang mga filter ay pumipili sa pagpasa o pagharang ng ilang partikular na bahagi ng dalas.
### Mga Uri ng Filter
| Uri | pumasa | Mga bloke | Application |
|------|--------|--------|-------------|
| **Low-pass** | Mga mababang frequency | Mataas na frequency | Smoothing, anti-aliasing |
| **High-pass** | Mataas na frequency | Mga mababang frequency | Pag-detect ng gilid, pag-alis ng ingay |
| **Band-pass** | Isang hanay ng mga frequency | Sa labas ng saklaw | Pagpili ng channel (radyo) |
| **Band-stop (bingaw)** | Lahat maliban sa isang saklaw | Isang partikular na saklaw | Pag-alis ng hum ng linya ng kuryente |
### FIR vs IIR Filter
| Ari-arian | FIR (Finite Impulse Response) | IIR (Infinite Impulse Response) |
|-----------------------|--------------------------------|--------------------------------|
| Impulse response | May hangganan na tagal | Walang katapusang tagal |
| Katatagan | Palaging matatag | Maaaring hindi matatag |
| Yugto | Maaaring maging eksaktong linear | Sa pangkalahatan nonlinear phase |
| Feedback | Hindi | Oo |
| Pagkalkula | Higit pang mga coefficient ang kailangan | Mas kaunting coefficient para sa parehong roll-off |
| Disenyo | Windowing, Parks-McClellan | Butterworth, Chebyshev, elliptic |
| Paglipat ng function | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Mga Detalye ng Disenyo ng Filter
| Parameter | Paglalarawan |
|-----------|-------------|
| **Passband** | Saklaw ng dalas na dapat pumasa nang may kaunting pagkawala |
| **Stopband** | Saklaw ng dalas na dapat na bawasan |
| **Dalas ng cutoff** | Hangganan sa pagitan ng passband at stopband |
| **Ripple** | Variation sa passband (o stopband) gain |
| **Roll-off** | Rate ng attenuation (dB bawat oktaba o dekada) |
| **Transition band** | Rehiyon sa pagitan ng passband at stopband |
### Mga Karaniwang Disenyo ng Filter
| Disenyo | Mga Katangian | Use Case |
|--------|----------------|----------|
| **Butterworth** | Pinakamataas na flat passband, katamtamang roll-off | Pangkalahatang layunin |
| **Chebyshev Type I** | Ripple sa passband, mas matarik na roll-off | Kapag mahalaga ang roll-off |
| **Chebyshev Type II** | Ripple sa stopband, flat passband | Kapag mahalaga ang passband flatness |
| **Elliptic (Cauer)** | Ripple sa parehong, steepest roll-off | Kinakailangan ang minimum na order |
| **Bessel** | Linear phase (pinakamalaking flat na pagkaantala ng pangkat) | Pinapanatili ang hugis ng waveform |
---

## Teorya ng Sampling
### Nyquist-Shannon Sampling Theorem
Ang isang tuluy-tuloy na signal ay maaaring ganap na mabuo mula sa mga sample nito kung ang sampling rate ay lumampas sa dalawang beses sa maximum na dalas:
f_s > 2f_max
| Termino | Kahulugan |
|------|------------|
| **Sampling rate** (f_s) | Bilang ng mga sample bawat segundo |
| **Nyquist rate** | 2f_max (minimum na sampling rate) |
| **Dalas ng Nyquist** | f_s/2 (maximum representable frequency) |
| **Aliasing** | Ang mga mataas na frequency ay nagpapanggap bilang mababang frequency kapag f_s < 2f_max |
### Mga Karaniwang Sampling Rate
| Application | Rate | Dalas ng Nyquist |
|-------------|------|-------------------|
| Pagsasalita sa telepono | 8 kHz | 4 kHz |
| Audio CD | 44.1 kHz | 22.05 kHz |
| Propesyonal na audio | 48 kHz | 24 kHz |
| High-resolution na audio | 96 kHz | 48 kHz |
| Video (30 fps) | 30 Hz (temporal) | 15 Hz |
### Anti-Aliasing
Bago mag-sample, ang isang **anti-aliasing filter** (low-pass) ay nag-aalis ng mga frequency sa itaas ng f_s/2 upang maiwasan ang pag-alyas.
---

## Windowing
Kapag sinusuri ang isang may hangganang segment ng isang signal, tuwirang nagpaparami kami sa isang hugis-parihaba na window, na nagdudulot ng spectral leakage. **Mga pag-andar ng bintana** binabawasan ang pagtagas na ito.
### Karaniwang Windows
| Window | Pangunahing Lobe Lapad | Antas ng Side Lobe | Use Case |
|---------------------|----------------|-----------------|----------|
| Parihaba | Pinakamakitid | −13 dB | Kapag ang resolusyon ay pinakamahalaga |
| Hann | 2× parihaba | −31 dB | Pangkalahatang layunin |
| Hamming | 2× parihaba | −41 dB | Nabawasan ang pinakamalapit na side lobe |
| Blackman | 3× parihaba | −58 dB | Mataas na dynamic range |
| Kaiser | Madaling iakma | Naaayos (sa pamamagitan ng β) | Kapag ang trade-off ay tunable |
### Spectral Leakage
Ang pag-multiply ng signal sa isang window ay pinagsasama ang spectrum nito sa spectrum ng window. Ang mas malawak na mga pangunahing lobe ay nagbabawas ng resolusyon ng dalas; ang lower side lobes ay nagbabawas ng leakage.
---

## Mga wavelet
Ang **Wavelets** ay maliliit, naka-localize na parang wave na function na ginagamit para sa multi-resolution na pagsusuri ng signal.
### Wavelet Transform
Hindi tulad ng Fourier transform (na nagbibigay ng global frequency information), ang wavelet transform ay nagbibigay ng **time-frequency** localization.
| Ibahin ang anyo | Resolusyon sa Oras | Resolusyon ng Dalas |
|-------------------------|----------------|---------------------|
| Fourier | Wala (global) | Mahusay |
| Short-Time FT | Naayos (laki ng window) | Naayos |
| Wavelet | Variable (mahusay sa mataas na freq) | Variable (mabuti sa mababang freq) |
### Mga Karaniwang Pamilya ng Wavelet
| Pamilya | Mga Katangian | Application |
|--------|-----------|-------------|
| **Haar** | Pinakasimple, hindi tuloy-tuloy | Edge detection, mabilis na pagsusuri |
| **Daubechies** (dbN) | Compact na suporta, N nawawalang sandali | Compression, denoising |
| **Mga Symlet** | Halos simetriko Daubechies | Nabawasang phase distortion |
| **Mga Coiflet** | Idinisenyo para sa mga kondisyon ng sandali | Pagproseso ng signal |
| **Morlet** | Gaussian-windowed sinusoid | Pagsusuri ng dalas ng oras |
| **Sumbrero ng Mexico** | Pangalawang derivative ng Gaussian | Pag-detect ng feature |
### Mga Application ng Wavelets
| Application | Paano Nakakatulong ang Wavelets |
|-------------|--------------------|
| Pag-compress ng larawan (JPEG 2000) | Multi-resolution na representasyon, mas mahusay kaysa sa DCT para sa mga gilid |
| Denoising | Threshold maliit na wavelet coefficients (signal ay nasa malalaking coefficients) |
| Pag-detect ng feature | Edge detection, lumilipas na detection sa time series |
| Pagsusuri ng ECG | Pag-detect ng mga QRS complex, pag-uuri ng arrhythmia |
| Pagsusuri ng seismic | Pagkilala sa mga geological layer, pagpoproseso ng signal ng lindol |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto sa Pagproseso ng Signal | Application |
|--------------------------|-------------|
| Fourier transform | Spectral na feature para sa audio ML, frequency-domain analysis ng time series |
| FFT | Mabilis na convolution sa CNNs (spectral convolution), mahusay na ugnayan |
| Convolution theorem | Pag-unawa kung paano gumagana ang mga CNN (sila ay natutunan na mga filter) |
| Mga Filter | Preprocessing (smoothing, denoising), feature extraction |
| Sampling theorem | Pag-unawa sa discretization, pagpili ng mga rate ng sensor, pag-iwas sa aliasing |
| Windowing | STFT para sa audio ML (spectrograms), time-frequency analysis |
| Mga wavelet | Extract ng feature para sa time series, compression, denoising |
| Laplace/Z-transform | Control theory para sa robotics, pag-unawa sa katatagan ng system |
| Spectral analysis | EEG/fMRI analysis, vibration monitoring, predictive maintenance |
| Nyquist rate | Pagpili ng naaangkop na mga rate ng pangongolekta ng data para sa mga ML pipeline |
---

## Buod
| Tool | Domain | Pangunahing Pananaw |
|------|--------|--------------|
| Fourier Transform | Oras → Dalas | Ang mga signal ay mga kabuuan ng sinusoids |
| Laplace Transform | Oras → Kumplikadong dalas | Pinangangasiwaan ang mga lumilipas at katatagan |
| Z-Transform | Discrete time → Complex | Pagsusuri at disenyo ng digital na filter |
| FFT | Mahusay na DFT computation | O(N log N) sa halip na O(N²) |
| Mga Filter | Pagpili ng dalas | Ipasa ang kailangan mo, i-block ang hindi mo |
| Sampling Theorem | Continuous ↔ discrete | Sample nang mabilis, walang mawawala |
| Windowing | Trade-off ng dalas ng oras | Resolusyon ng balanse at pagtagas |
| Mga wavelet | Multi-resolution na pagsusuri | Lokal sa parehong oras at dalas |
Ang pagpoproseso ng signal ay nagbibigay ng mathematical na pundasyon para sa pag-unawa, pagsusuri, at pagmamanipula ng data. Ang bawat pipeline ng machine learning na gumagana sa time series, audio, mga larawan, o data ng sensor ay tahasang gumagamit ng mga konsepto sa pagpoproseso ng signal. Ang Fourier transform, sa partikular, ay arguably ang pinakamahalagang kasangkapan sa matematika pagkatapos ng calculus para sa sinumang data scientist.