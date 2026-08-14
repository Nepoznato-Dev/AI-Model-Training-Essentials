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
# Signal Processing

Signal processing is the science of analysing, modifying, and synthesising signals — representations of physical quantities varying over time, space, or frequency. Audio, images, video, sensor data, brain waves, stock prices — all are signals. The mathematical tools of signal processing (Fourier transforms, filters, sampling theory) are foundational to machine learning, communications, medical imaging, and virtually every field that works with data.

---

## Signals and Systems

### Signal Classification

| Type | Description | Example |
|------|-------------|---------|
| **Continuous-time** | Defined for all t ∈ ℝ | Audio voltage, temperature |
| **Discrete-time** | Defined at integer indices n | Sampled audio, pixel values |
| **Analog** | Continuous in time and amplitude | Vinyl record groove |
| **Digital** | Discrete in time and quantised amplitude | MP3 file, JPEG image |
| **Periodic** | x(t + T) = x(t) for all t | Sine wave, square wave |
| **Aperiodic** | No repeating pattern | Speech, music |
| **Deterministic** | Completely predictable | Sine wave |
| **Stochastic** | Contains randomness | Noise, stock prices |

### System Properties

| Property | Definition | Example |
|----------|-----------|---------|
| **Linear** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Low-pass filter |
| **Time-invariant** | Shift in input → same shift in output | Any fixed filter |
| **Causal** | Output depends only on present and past inputs | Real-time system |
| **Stable (BIBO)** | Bounded input → bounded output | Well-designed filter |
| **Memoryless** | Output depends only on current input | Amplifier |

---

## Fourier Transform

The **Fourier transform** decomposes a signal into its constituent frequencies.

### Continuous Fourier Transform

X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt

Inverse: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df

### Fourier Transform Pairs

| Time Domain x(t) | Frequency Domain X(f) |
|-------------------|----------------------|
| Rectangular pulse | sinc function |
| sinc function | Rectangular pulse |
| Gaussian e^{−at²} | Gaussian (√(π/a))e^{−π²f²/a} |
| Dirac delta δ(t) | 1 (all frequencies) |
| Complex exponential e^{j2πf₀t} | δ(f − f₀) |
| Cosine cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |

### Key Properties

| Property | Time Domain | Frequency Domain |
|----------|-------------|-----------------|
| Linearity | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Time shift | x(t − t₀) | X(f)e^{−j2πft₀} |
| Frequency shift | x(t)e^{j2πf₀t} | X(f − f₀) |
| Convolution | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Multiplication | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Differentiation | dx/dt | j2πf X(f) |
| Parseval's theorem | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |

**Convolution theorem:** Convolution in time = multiplication in frequency. This is the most important property — it turns expensive convolution operations into cheap multiplications.

### Discrete Fourier Transform (DFT)

For a sequence x[0], x[1], ..., x[N−1]:

X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1

| Property | Value |
|----------|-------|
| Input | N real or complex samples |
| Output | N complex frequency bins |
| Frequency resolution | f_s/N (where f_s is sampling rate) |
| Nyquist frequency | f_s/2 (maximum representable frequency) |
| Complexity | O(N²) direct computation |

### Fast Fourier Transform (FFT)

The **FFT** computes the DFT in O(N log N) instead of O(N²).

| N | O(N²) Operations | O(N log N) Operations | Speedup |
|---|------------------|----------------------|---------|
| 1,024 | 1,048,576 | 10,240 | 102× |
| 1,048,576 | 1.1 × 10¹² | 20,971,520 | 52,428× |

The FFT is one of the most important algorithms ever invented. It enables real-time audio processing, image compression (JPEG), wireless communication (OFDM), and spectral analysis.

---

## Laplace Transform

The **Laplace transform** extends the Fourier transform to handle unstable systems and transient analysis.

F(s) = ∫₀^∞ f(t) e^{−st} dt, where s = σ + jω

### Common Laplace Transforms

| f(t) | F(s) | Region of Convergence |
|------|------|----------------------|
| δ(t) (impulse) | 1 | All s |
| u(t) (step) | 1/s | Re(s) > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| tⁿu(t) | n!/s^{n+1} | Re(s) > 0 |
| sin(ωt)u(t) | ω/(s²+ω²) | Re(s) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(s) > 0 |

### Connection to Fourier Transform

When σ = 0 (s = jω), the Laplace transform reduces to the Fourier transform. The Laplace transform provides a more complete picture by including information about growth/decay (σ).

---

## Z-Transform

The **Z-transform** is the discrete-time equivalent of the Laplace transform.

X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}

### Common Z-Transforms

| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1 | All z |
| u[n] (step) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| sin(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |

### Relationship to Other Transforms

| Transform | Domain | Variable |
|-----------|--------|----------|
| Fourier | Continuous frequency | f or ω |
| Laplace | Complex frequency | s = σ + jω |
| Z-transform | Complex frequency (discrete) | z = e^{sT} |

The unit circle in the z-plane (|z| = 1) corresponds to the Fourier transform.

---

## Filters

Filters selectively pass or block certain frequency components.

### Filter Types

| Type | Passes | Blocks | Application |
|------|--------|--------|-------------|
| **Low-pass** | Low frequencies | High frequencies | Smoothing, anti-aliasing |
| **High-pass** | High frequencies | Low frequencies | Edge detection, noise removal |
| **Band-pass** | A range of frequencies | Outside the range | Channel selection (radio) |
| **Band-stop (notch)** | Everything except a range | A specific range | Power line hum removal |

### FIR vs IIR Filters

| Property | FIR (Finite Impulse Response) | IIR (Infinite Impulse Response) |
|----------|-------------------------------|--------------------------------|
| Impulse response | Finite duration | Infinite duration |
| Stability | Always stable | Can be unstable |
| Phase | Can be exactly linear | Generally nonlinear phase |
| Feedback | No | Yes |
| Computation | More coefficients needed | Fewer coefficients for same roll-off |
| Design | Windowing, Parks-McClellan | Butterworth, Chebyshev, elliptic |
| Transfer function | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |

### Filter Design Specifications

| Parameter | Description |
|-----------|-------------|
| **Passband** | Frequency range that should pass with minimal loss |
| **Stopband** | Frequency range that should be attenuated |
| **Cutoff frequency** | Boundary between passband and stopband |
| **Ripple** | Variation in passband (or stopband) gain |
| **Roll-off** | Rate of attenuation (dB per octave or decade) |
| **Transition band** | Region between passband and stopband |

### Common Filter Designs

| Design | Characteristics | Use Case |
|--------|----------------|----------|
| **Butterworth** | Maximally flat passband, moderate roll-off | General purpose |
| **Chebyshev Type I** | Ripple in passband, steeper roll-off | When roll-off matters |
| **Chebyshev Type II** | Ripple in stopband, flat passband | When passband flatness matters |
| **Elliptic (Cauer)** | Ripple in both, steepest roll-off | Minimum order needed |
| **Bessel** | Linear phase (maximally flat group delay) | Preserving waveform shape |

---

## Sampling Theory

### Nyquist-Shannon Sampling Theorem

A continuous signal can be perfectly reconstructed from its samples if the sampling rate exceeds twice the maximum frequency:

f_s > 2f_max

| Term | Definition |
|------|------------|
| **Sampling rate** (f_s) | Number of samples per second |
| **Nyquist rate** | 2f_max (minimum sampling rate) |
| **Nyquist frequency** | f_s/2 (maximum representable frequency) |
| **Aliasing** | High frequencies masquerading as low frequencies when f_s < 2f_max |

### Common Sampling Rates

| Application | Rate | Nyquist Frequency |
|-------------|------|-------------------|
| Telephone speech | 8 kHz | 4 kHz |
| Audio CD | 44.1 kHz | 22.05 kHz |
| Professional audio | 48 kHz | 24 kHz |
| High-resolution audio | 96 kHz | 48 kHz |
| Video (30 fps) | 30 Hz (temporal) | 15 Hz |

### Anti-Aliasing

Before sampling, an **anti-aliasing filter** (low-pass) removes frequencies above f_s/2 to prevent aliasing.

---

## Windowing

When analysing a finite segment of a signal, we implicitly multiply by a rectangular window, causing spectral leakage. **Window functions** reduce this leakage.

### Common Windows

| Window | Main Lobe Width | Side Lobe Level | Use Case |
|--------|----------------|-----------------|----------|
| Rectangular | Narrowest | −13 dB | When resolution matters most |
| Hann | 2× rectangular | −31 dB | General purpose |
| Hamming | 2× rectangular | −41 dB | Reduced nearest side lobe |
| Blackman | 3× rectangular | −58 dB | High dynamic range |
| Kaiser | Adjustable | Adjustable (via β) | When trade-off is tunable |

### Spectral Leakage

Multiplying a signal by a window convolves its spectrum with the window's spectrum. Wider main lobes reduce frequency resolution; lower side lobes reduce leakage.

---

## Wavelets

**Wavelets** are small, localised wave-like functions used for multi-resolution signal analysis.

### Wavelet Transform

Unlike the Fourier transform (which gives global frequency information), the wavelet transform gives **time-frequency** localisation.

| Transform | Time Resolution | Frequency Resolution |
|-----------|----------------|---------------------|
| Fourier | None (global) | Excellent |
| Short-Time FT | Fixed (window size) | Fixed |
| Wavelet | Variable (good at high freq) | Variable (good at low freq) |

### Common Wavelet Families

| Family | Properties | Application |
|--------|-----------|-------------|
| **Haar** | Simplest, discontinuous | Edge detection, quick analysis |
| **Daubechies** (dbN) | Compact support, N vanishing moments | Compression, denoising |
| **Symlets** | Nearly symmetric Daubechies | Reduced phase distortion |
| **Coiflets** | Designed for moment conditions | Signal processing |
| **Morlet** | Gaussian-windowed sinusoid | Time-frequency analysis |
| **Mexican Hat** | Second derivative of Gaussian | Feature detection |

### Applications of Wavelets

| Application | How Wavelets Help |
|-------------|-------------------|
| Image compression (JPEG 2000) | Multi-resolution representation, better than DCT for edges |
| Denoising | Threshold small wavelet coefficients (signal is in large coefficients) |
| Feature detection | Edge detection, transient detection in time series |
| ECG analysis | Detecting QRS complexes, arrhythmia classification |
| Seismic analysis | Identifying geological layers, earthquake signal processing |

---

## Relevance to Machine Learning and Data Science

| Signal Processing Concept | Application |
|--------------------------|-------------|
| Fourier transform | Spectral features for audio ML, frequency-domain analysis of time series |
| FFT | Fast convolution in CNNs (spectral convolution), efficient correlation |
| Convolution theorem | Understanding how CNNs work (they are learned filters) |
| Filters | Preprocessing (smoothing, denoising), feature extraction |
| Sampling theorem | Understanding discretisation, choosing sensor rates, avoiding aliasing |
| Windowing | STFT for audio ML (spectrograms), time-frequency analysis |
| Wavelets | Feature extraction for time series, compression, denoising |
| Laplace/Z-transform | Control theory for robotics, understanding system stability |
| Spectral analysis | EEG/fMRI analysis, vibration monitoring, predictive maintenance |
| Nyquist rate | Choosing appropriate data collection rates for ML pipelines |

---

## Summary

| Tool | Domain | Key Insight |
|------|--------|-------------|
| Fourier Transform | Time → Frequency | Signals are sums of sinusoids |
| Laplace Transform | Time → Complex frequency | Handles transients and stability |
| Z-Transform | Discrete time → Complex | Digital filter analysis and design |
| FFT | Efficient DFT computation | O(N log N) instead of O(N²) |
| Filters | Frequency selection | Pass what you need, block what you don't |
| Sampling Theorem | Continuous ↔ discrete | Sample fast enough, lose nothing |
| Windowing | Time-frequency trade-off | Balance resolution and leakage |
| Wavelets | Multi-resolution analysis | Local in both time and frequency |

Signal processing provides the mathematical foundation for understanding, analysing, and manipulating data. Every machine learning pipeline that works with time series, audio, images, or sensor data implicitly uses signal processing concepts. The Fourier transform, in particular, is arguably the most important mathematical tool after calculus for any data scientist.
