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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
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

# Optics and Waves

Waves are everywhere: sound, light, water, radio signals, quantum probability amplitudes, stock market fluctuations, and the vibrations of neural network activations. Optics — the study of light — is the most well-developed wave science, and its mathematical tools (Fourier analysis, interference, diffraction) apply to every wave phenomenon. Understanding waves is essential for signal processing, image analysis, communications, and the physical layer of all modern technology.

---

## The Wave Equation

### General Wave Equation

The one-dimensional wave equation:

∂²u/∂t² = c² ∂²u/∂x²

where u(x,t) is the wave displacement and c is the wave speed.

### General Solution (d'Alembert)

u(x,t) = f(x − ct) + g(x + ct)

where f is a right-travelling wave and g is a left-travelling wave.

### Key Wave Parameters

| Parameter | Symbol | Unit | Description |
|-----------|--------|------|-------------|
| Amplitude | A | varies | Maximum displacement |
| Wavelength | λ | metres | Distance between consecutive crests |
| Frequency | f or ν | Hertz (Hz) | Cycles per second |
| Period | T = 1/f | seconds | Time for one complete cycle |
| Wave number | k = 2π/λ | rad/m | Spatial frequency |
| Angular frequency | ω = 2πf | rad/s | Temporal frequency |
| Wave speed | c = fλ = ω/k | m/s | Speed of propagation |

### Sinusoidal Wave

u(x,t) = A sin(kx − ωt + φ)

where φ is the phase constant.

### Wave Speed in Different Media

| Wave Type | Medium | Speed Formula |
|-----------|--------|---------------|
| String | Tension T, linear density μ | c = √(T/μ) |
| Sound | Bulk modulus B, density ρ | c = √(B/ρ) |
| Sound (ideal gas) | γ, R, T, M | c = √(γRT/M) |
| EM wave | Permittivity ε, permeability μ | c = 1/√(με) |
| EM wave (vacuum) | ε₀, μ₀ | c = 3 × 10⁸ m/s |

---

## Superposition and Interference

### Principle of Superposition

When two or more waves overlap, the resultant displacement is the sum of individual displacements:

u_total = u₁ + u₂ + ... + uₙ

This holds for linear wave equations.

### Interference of Two Waves

Two waves with same frequency and amplitude, phase difference Δφ:

u_total = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)

| Phase Difference | Result | Intensity |
|-----------------|--------|-----------|
| Δφ = 0, 2π, 4π, ... | **Constructive** (amplitude = 2A) | 4I₀ (maximum) |
| Δφ = π, 3π, 5π, ... | **Destructive** (amplitude = 0) | 0 (minimum) |
| Δφ = π/2 | Partial | 2I₀ |

### Conditions for Interference

| Condition | Type | Path Difference |
|-----------|------|-----------------|
| Constructive | Bright fringe | ΔL = mλ (m = 0, 1, 2, ...) |
| Destructive | Dark fringe | ΔL = (m + ½)λ |

---

## Young's Double-Slit Experiment

Light passes through two narrow slits separated by distance d, creating an interference pattern on a screen at distance L.

### Fringe Positions

| Fringe | Position on Screen |
|--------|-------------------|
| Bright (maxima) | y_m = mλL/d |
| Dark (minima) | y_m = (m + ½)λL/d |
| Fringe spacing | Δy = λL/d |

This experiment proved the wave nature of light (Thomas Young, 1801) and later became central to quantum mechanics (wave-particle duality).

---

## Diffraction

**Diffraction** is the bending and spreading of waves around obstacles and through openings.

### Single-Slit Diffraction

Light through a slit of width a produces a pattern of bright and dark fringes.

| Feature | Condition |
|---------|-----------|
| Central maximum | Widest and brightest; width = 2λL/a |
| Minima (dark fringes) | a sin θ = mλ (m = ±1, ±2, ...) |
| Secondary maxima | Approximately between minima; much dimmer |

### Diffraction Grating

N equally spaced slits (spacing d) produce very sharp maxima:

d sin θ = mλ (m = 0, 1, 2, ...)

| Property | Effect |
|----------|--------|
| More slits (larger N) | Sharper, brighter maxima |
| Resolving power | R = mN (can distinguish close wavelengths) |
| Applications | Spectroscopy, wavelength measurement |

### Rayleigh Criterion (Resolution Limit)

Two point sources are just resolvable when the central maximum of one falls on the first minimum of the other:

θ_min = 1.22 λ/D

where D is the aperture diameter.

| System | λ | D | θ_min |
|--------|---|---|-------|
| Human eye | 550 nm | 5 mm | 1.3 × 10⁻⁴ rad (~0.01°) |
| Hubble Space Telescope | 550 nm | 2.4 m | 2.8 × 10⁻⁷ rad |
| Radio telescope (Arecibo) | 21 cm | 305 m | 8.4 × 10⁻⁴ rad |

---

## Polarisation

**Polarisation** describes the orientation of the electric field oscillation in a transverse wave.

### Types of Polarisation

| Type | Description |
|------|-------------|
| **Linear** | E oscillates in a fixed plane |
| **Circular** | E rotates in a circle (right or left handed) |
| **Elliptical** | E traces an ellipse (most general) |
| **Unpolarised** | Random mixture of all polarisations (most natural light) |

### Malus's Law

When polarised light passes through a polariser at angle θ to the polarisation direction:

I = I₀ cos²θ

| Angle θ | Transmitted Intensity |
|---------|----------------------|
| 0° | 100% (I₀) |
| 30° | 75% |
| 45° | 50% |
| 60° | 25% |
| 90° | 0% (completely blocked) |

### Polarisation by Reflection (Brewster's Angle)

Light reflected at Brewster's angle is completely polarised:

tan θ_B = n₂/n₁

| Interface | n₁ | n₂ | θ_B |
|-----------|----|----|-----|
| Air → glass | 1.0 | 1.5 | 56.3° |
| Air → water | 1.0 | 1.33 | 53.1° |
| Glass → diamond | 1.5 | 2.42 | 58.1° |

---

## Geometric Optics

Geometric (ray) optics treats light as rays that travel in straight lines, bending at interfaces.

### Snell's Law (Refraction)

n₁ sin θ₁ = n₂ sin θ₂

| Material | Refractive Index n |
|----------|-------------------|
| Vacuum | 1.000 |
| Air | 1.0003 |
| Water | 1.33 |
| Glass (crown) | 1.52 |
| Glass (flint) | 1.62 |
| Diamond | 2.42 |

### Total Internal Reflection

When light travels from denser to less dense medium, beyond the **critical angle**:

θ_c = arcsin(n₂/n₁)

All light is reflected — this is how optical fibres work.

### Thin Lens Equation

1/f = 1/d_o + 1/d_i

| Quantity | Meaning |
|----------|---------|
| f | Focal length |
| d_o | Object distance |
| d_i | Image distance |
| M = −d_i/d_o | Magnification |

| Lens Type | f | Image |
|-----------|---|-------|
| Converging (convex) | Positive | Real (if d_o > f) or virtual |
| Diverging (concave) | Negative | Always virtual, upright, reduced |

### Mirror Equation

Same form as lens equation: 1/f = 1/d_o + 1/d_i, where f = R/2 for spherical mirrors.

---

## Fourier Optics

Fourier optics treats imaging and diffraction as Fourier transform operations.

### Key Principle

The far-field diffraction pattern of an aperture is the **Fourier transform** of the aperture function.

| Aperture | Diffraction Pattern (Fourier Transform) |
|----------|----------------------------------------|
| Single slit | sinc function |
| Circular aperture | Airy disk (J₁(r)/r) |
| Rectangular aperture | 2D sinc |
| Grating | Discrete delta functions |

### Optical Fourier Transform

A lens performs a 2D Fourier transform: placing an object at the front focal plane produces its Fourier transform at the back focal plane.

### Applications

| Application | How Fourier Optics Helps |
|-------------|-------------------------|
| Image filtering | Place masks at the Fourier plane to block/pass spatial frequencies |
| Edge detection | High-pass filtering in the Fourier plane |
| Pattern recognition | Correlation via Fourier transforms |
| Holography | Recording and reconstructing wavefronts |
| Optical computing | Performing Fourier transforms at the speed of light |

---

## Sound and Acoustics

### Sound Wave Properties

| Property | Typical Range | Unit |
|----------|--------------|------|
| Frequency | 20 − 20,000 (human hearing) | Hz |
| Speed (air, 20°C) | 343 | m/s |
| Speed (water) | 1,480 | m/s |
| Speed (steel) | 5,960 | m/s |
| Intensity threshold | 10⁻¹² | W/m² |

### Decibel Scale

β = 10 log₁₀(I/I₀) dB, where I₀ = 10⁻¹² W/m²

| Sound | Intensity (W/m²) | Level (dB) |
|-------|-------------------|------------|
| Threshold of hearing | 10⁻¹² | 0 |
| Rustling leaves | 10⁻¹¹ | 10 |
| Normal conversation | 10⁻⁶ | 60 |
| Rock concert | 1 | 120 |
| Threshold of pain | 10 | 130 |
| Jet engine | 100 | 140 |

### Doppler Effect

Observed frequency when source and observer move relative to each other:

f' = f(v ± v_o)/(v ∓ v_s)

| Scenario | Effect |
|----------|--------|
| Source approaching | Higher frequency (blue shift for light) |
| Source receding | Lower frequency (red shift for light) |
| Applications | Radar, medical ultrasound, astronomy (redshift of galaxies) |

---

## Relevance to Machine Learning and Data Science

| Wave/Optics Concept | Application |
|---------------------|-------------|
| Wave equation | Physics-informed neural networks, seismic data analysis, audio processing |
| Fourier analysis | Foundation of signal processing, spectral analysis, feature extraction |
| Fourier transform | CNNs implicitly perform local Fourier analysis; FFT used in data preprocessing |
| Interference | Analog computing, optical neural networks |
| Diffraction | Image formation models, deblurring algorithms, computational photography |
| Polarisation | Remote sensing, material classification, satellite imagery analysis |
| Geometric optics | Camera models in computer vision, ray tracing for synthetic data generation |
| Lens equation | Camera calibration, depth estimation, 3D reconstruction |
| Fourier optics | Optical computing, diffractive deep neural networks (D²NN) |
| Doppler effect | Radar signal processing, medical imaging (Doppler ultrasound), velocity estimation |
| Decibel scale | Audio feature engineering, speech recognition preprocessing |
| Sampling theory | Nyquist-Shannon theorem connects wave theory to digital signal processing |

---

## Summary

| Topic | Core Idea | Key Equation |
|-------|-----------|-------------|
| Wave equation | Waves propagate at speed c | ∂²u/∂t² = c²∂²u/∂x² |
| Superposition | Waves add linearly | u = u₁ + u₂ |
| Interference | Phase determines reinforcement | Δφ = 2πΔL/λ |
| Diffraction | Waves bend around obstacles | a sin θ = mλ (single slit) |
| Polarisation | Orientation of oscillation | Malus's law: I = I₀cos²θ |
| Geometric optics | Light as rays | Snell's law: n₁sinθ₁ = n₂sinθ₂ |
| Fourier optics | Imaging as Fourier transform | Far field = FT of aperture |
| Doppler effect | Frequency shift from motion | f' = f(v ± v_o)/(v ∓ v_s) |

Waves are the universal language of oscillating systems. Whether you're processing audio signals, analysing time series, designing image recognition systems, or building physics simulations, the mathematics of waves — superposition, Fourier analysis, interference, diffraction — provides the essential toolkit. Optics, as the most mature wave science, offers both the theoretical foundation and practical techniques that permeate modern data science.
