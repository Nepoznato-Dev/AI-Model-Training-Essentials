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
# Optics at Waves
Ang mga alon ay nasa lahat ng dako: tunog, ilaw, tubig, mga signal ng radyo, mga amplitude ng posibilidad ng dami, pagbabagu-bago ng stock market, at mga vibrations ng mga pag-activate ng neural network. Ang mga optika — ang pag-aaral ng liwanag — ay ang pinaka mahusay na binuo na agham ng alon, at ang mga kasangkapang pangmatematika nito (Fourier analysis, interference, diffraction) ay nalalapat sa bawat wave phenomenon. Ang pag-unawa sa mga alon ay mahalaga para sa pagpoproseso ng signal, pagsusuri ng imahe, komunikasyon, at pisikal na layer ng lahat ng modernong teknolohiya.
---

## Ang Wave Equation
### Pangkalahatang Wave Equation
Ang one-dimensional wave equation:
∂²u/∂t² = c² ∂²u/∂x²
kung saan ang u(x,t) ay ang wave displacement at c ay ang wave speed.
### Pangkalahatang Solusyon (d'Alembert)
u(x,t) = f(x − ct) + g(x + ct)
kung saan ang f ay isang right-travelling wave at g ay isang left-travelling wave.
### Mga Key Wave Parameter
| Parameter | Simbolo | Yunit | Paglalarawan |
|-----------|--------|------|-------------|
| Amplitude | Isang | nag-iiba | Pinakamataas na displacement |
| Haba ng daluyong | λ | metro | Distansya sa pagitan ng magkasunod na crest |
| Dalas | f o ν | Hertz (Hz) | Mga cycle bawat segundo |
| Panahon | T = 1/f | segundo | Oras para sa isang kumpletong cycle |
| Wave number | k = 2π/λ | rad/m | Spatial frequency |
| Angular na dalas | ω = 2πf | rad/s | Temporal na dalas |
| Bilis ng alon | c = fλ = ω/k | m/s | Bilis ng pagpapalaganap |
### Sinusoidal Wave
u(x,t) = Isang kasalanan(kx − ωt + φ)
kung saan ang φ ay ang phase constant.
### Bilis ng Wave sa Iba't ibang Media
| Uri ng Wave | Katamtaman | Formula ng Bilis |
|-----------|--------|----------------|
| String | Tensyon T, linear density μ | c = √(T/μ) |
| Tunog | Bulk modulus B, density ρ | c = √(B/ρ) |
| Tunog (ideal na gas) | γ, R, T, M | c = √(γRT/M) |
| EM wave | Permittivity ε, permeability μ | c = 1/√(με) |
| EM wave (vacuum) | ε₀, μ₀ | c = 3 × 10⁸ m/s |
---

## Superposisyon at Panghihimasok
### Prinsipyo ng Superposisyon
Kapag nag-overlap ang dalawa o higit pang mga alon, ang resultang displacement ay ang kabuuan ng mga indibidwal na displacement:
u_total = u₁ + u₂ + ... + uₙ
Ito ay humahawak para sa mga linear wave equation.
### Interference ng Dalawang Alon
Dalawang wave na may parehong frequency at amplitude, phase difference Δφ:
u_total = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Pagkakaiba ng Phase | Resulta | Intensity |
|-----------------|--------|-----------|
| Δφ = 0, 2π, 4π, ... | **Nakabubuo** (amplitude = 2A) | 4I₀ (maximum) |
| Δφ = π, 3π, 5π, ... | **Nakakasira** (amplitude = 0) | 0 (minimum) |
| Δφ = π/2 | Bahagyang | 2I₀ |
### Mga Kundisyon para sa Panghihimasok
| Kundisyon | Uri | Path Pagkakaiba |
|-----------|------|-----------------|
| Nakabubuo | Maliwanag na palawit | ΔL = mλ (m = 0, 1, 2, ...) |
| Mapangwasak | Madilim na palawit | ΔL = (m + ½)λ |
---

## Double-Slit Experiment ni Young
Dumadaan ang liwanag sa dalawang makitid na hiwa na pinaghihiwalay ng distansya d, na lumilikha ng pattern ng interference sa isang screen sa layo na L.
### Mga Fringe na Posisyon
| Palawit | Posisyon sa Screen |
|--------|--------------------|
| Maliwanag (maxima) | y_m = mλL/d |
| Madilim (minima) | y_m = (m + ½)λL/d |
| Fringe spacing | Δy = λL/d |
Pinatunayan ng eksperimentong ito ang wave nature ng liwanag (Thomas Young, 1801) at kalaunan ay naging sentro ng quantum mechanics (wave-particle duality).
---

## Diffraction
Ang **Diffraction** ay ang pagyuko at pagkalat ng mga alon sa paligid ng mga hadlang at sa pamamagitan ng mga bukana.
### Single-Slit Diffraction
Ang liwanag sa pamamagitan ng isang hiwa ng lapad ay gumagawa ng isang pattern ng maliwanag at madilim na mga palawit.
| Tampok | Kundisyon |
|---------|------------|
| Central maximum | Pinakamalawak at pinakamaliwanag; lapad = 2λL/a |
| Minima (madilim na palawit) | isang kasalanan θ = mλ (m = ±1, ±2, ...) |
| Pangalawang maxima | Humigit-kumulang sa pagitan ng minima; mas malabo |
### Diffraction Grating
Ang N pantay na pagitan ng mga hiwa (spacing d) ay gumagawa ng napakatalim na maxima:
d sin θ = mλ (m = 0, 1, 2, ...)
| Ari-arian | Epekto |
|----------|--------|
| Higit pang mga hiwa (mas malaking N) | Mas matalas, mas maliwanag na maxima |
| Kapangyarihan sa paglutas | R = mN (maaaring makilala ang malapit na wavelength) |
| Mga Application | Spectroscopy, pagsukat ng wavelength |
### Rayleigh Criterion (Limit sa Resolusyon)
Ang dalawang puntong pinagmumulan ay malulutas lamang kapag ang gitnang maximum ng isa ay bumaba sa unang minimum ng isa pa:
θ_min = 1.22 λ/D
kung saan ang D ay ang diameter ng aperture.
| System | λ | D | θ_min |
|--------|---|---|-------|
| Mata ng tao | 550 nm | 5 mm | 1.3 × 10⁻⁴ rad (~0.01°) |
| Hubble Space Telescope | 550 nm | 2.4 m | 2.8 × 10⁻⁷ rad |
| Teleskopyo ng radyo (Arecibo) | 21 cm | 305 m | 8.4 × 10⁻⁴ rad |
---

## Polarisasyon
Inilalarawan ng **Polarization** ang oryentasyon ng electric field oscillation sa isang transverse wave.
### Mga Uri ng Polarisasyon
| Uri | Paglalarawan |
|------|-------------|
| **Linear** | E oscillates sa isang nakapirming eroplano |
| **Pabilog** | E umiikot sa isang bilog (kanan o kaliwang kamay) |
| **Elliptical** | E trace isang ellipse (pinaka pangkalahatan) |
| **Unpolarised** | Random na pinaghalong lahat ng polarisasyon (pinaka natural na liwanag) |
### Batas ni Malus
Kapag ang polarized light ay dumaan sa isang polariser sa anggulo θ sa direksyon ng polarization:
I = I₀ cos²θ
| Anggulo θ | Nailipat na Intensity |
|---------|----------------------|
| 0° | 100% (I₀) |
| 30° | 75% |
| 45° | 50% |
| 60° | 25% |
| 90° | 0% (ganap na hinarang) |
### Polarization ayon sa Reflection (Brewster's Angle)
Ang liwanag na naaaninag sa anggulo ng Brewster ay ganap na nakapolarized:
tan θ_B = n₂/n₁
| Interface | n₁ | n₂ | θ_B |
|-----------|----|----|-----|
| Hangin → salamin | 1.0 | 1.5 | 56.3° |
| Hangin → tubig | 1.0 | 1.33 | 53.1° |
| Salamin → brilyante | 1.5 | 2.42 | 58.1° |
---

## Geometric Optik
Tinatrato ng geometric (ray) na optika ang liwanag bilang mga sinag na naglalakbay sa mga tuwid na linya, na nakayuko sa mga interface.
### Snell's Law (Refraction)
n₁ sin θ₁ = n₂ sin θ₂
| Materyal | Repraktibo Index n |
|----------|--------------------|
| Vacuum | 1.000 |
| Hangin | 1.0003 |
| Tubig | 1.33 |
| Salamin (korona) | 1.52 |
| Salamin (flint) | 1.62 |
| brilyante | 2.42 |
### Kabuuang Panloob na Pagninilay
Kapag ang liwanag ay naglalakbay mula sa mas siksik patungo sa hindi gaanong siksik na daluyan, lampas sa **kritikal na anggulo**:
θ_c = arcsin(n₂/n₁)
Ang lahat ng liwanag ay nasasalamin — ito ay kung paano gumagana ang mga optical fiber.
### Manipis na Lens Equation
1/f = 1/d_o + 1/d_i
| Dami | Ibig sabihin |
|----------|---------|
| f | Focal length |
| d_o | Layo ng bagay |
| d_i | Layo ng larawan |
| M = −d_i/d_o | Pagpapalaki |
| Uri ng Lens | f | Larawan |
|-----------|---|-------|
| Converging (matambok) | Positibong | Totoo (kung d_o > f) o virtual |
| Diverging (malukong) | Negatibo | Palaging virtual, patayo, nabawasan |
### Mirror Equation
Parehong anyo ng equation ng lens: 1/f = 1/d_o + 1/d_i, kung saan f = R/2 para sa mga spherical na salamin.
---

## Fourier Optik
Tinatrato ng Fourier optics ang imaging at diffraction bilang Fourier transform operations.
### Pangunahing Prinsipyo
Ang far-field diffraction pattern ng isang aperture ay ang **Fourier transform** ng aperture function.
| Aperture | Pattern ng Diffraction (Fourier Transform) |
|----------|--------------------------------------|
| Isang biyak | sync function |
| Pabilog na siwang | Airy disk (J₁(r)/r) |
| Parihabang siwang | 2D simula |
| Grating | Mga discrete delta function |
### Optical Fourier Transform
Ang isang lens ay nagsasagawa ng 2D Fourier transform: ang paglalagay ng isang bagay sa front focal plane ay gumagawa ng Fourier transform nito sa back focal plane.
### Mga Application
| Application | Paano Nakakatulong ang Fourier Optics |
|-------------|------------------------|
| Pag-filter ng larawan | Maglagay ng mga maskara sa Fourier plane para harangan/ipasa ang mga spatial frequency |
| Pag-detect ng gilid | High-pass filtering sa Fourier plane |
| Pagkilala sa pattern | Ang ugnayan sa pamamagitan ng Fourier transforms |
| Holography | Pagre-record at muling pagtatayo ng mga wavefront |
| Optical computing | Ang pagsasagawa ng Fourier transforms sa bilis ng liwanag |
---

## Tunog at Acoustics
### Mga Katangian ng Sound Wave
| Ari-arian | Karaniwang Saklaw | Yunit |
|----------|--------------|------|
| Dalas | 20 − 20,000 (pakinig ng tao) | Hz |
| Bilis (hangin, 20°C) | 343 | m/s |
| Bilis (tubig) | 1,480 | m/s |
| Bilis (bakal) | 5,960 | m/s |
| Intensity threshold | 10⁻¹² | W/m² |
### Sukat ng Decibel
β = 10 log₁₀(I/I₀) dB, kung saan I₀ = 10⁻¹² W/m²
| Tunog | Intensity (W/m²) | Antas (dB) |
|-------|-------------------|------------|
| Threshold ng pagdinig | 10⁻¹² | 0 |
| Kumakaluskos na mga dahon | 10⁻¹¹ | 10 |
| Normal na pag-uusap | 10⁻⁶ | 60 |
| Rock concert | 1 | 120 |
| Threshold ng sakit | 10 | 130 |
| Jet engine | 100 | 140 |
### Epekto ng Doppler
Naobserbahang dalas kapag gumagalaw ang pinagmulan at tagamasid sa isa't isa:
f' = f(v ± v_o)/(v ∓ v_s)
| Sitwasyon | Epekto |
|----------|--------|
| Papalapit na pinagmulan | Mas mataas na frequency (blue shift para sa liwanag) |
| Umuurong ang pinagmulan | Mas mababang frequency (red shift para sa liwanag) |
| Mga Application | Radar, medikal na ultratunog, astronomiya (redshift ng mga kalawakan) |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Wave/Optics | Application |
|---------------------|-------------|
| Wave equation | Mga neural network na may kaalaman sa pisika, pagsusuri ng data ng seismic, pagproseso ng audio |
| Fourier na pagsusuri | Foundation ng signal processing, spectral analysis, feature extraction |
| Fourier transform | Ang mga CNN ay tahasang nagsasagawa ng lokal na pagsusuri sa Fourier; FFT na ginamit sa data preprocessing |
| Panghihimasok | Analog computing, optical neural network |
| Diffraction | Mga modelo ng pagbuo ng imahe, mga algorithm sa pag-deblur, computational photography |
| Polariseysyon | Remote sensing, pag-uuri ng materyal, pagsusuri ng satellite imagery |
| Geometric na optika | Mga modelo ng camera sa computer vision, ray tracing para sa synthetic data generation |
| Equation ng lens | Pag-calibrate ng camera, depth estimation, 3D reconstruction |
| Fourier optika | Optical computing, diffractive deep neural network (D²NN) |
| Doppler effect | Pagproseso ng signal ng radar, medical imaging (Doppler ultrasound), velocity estimation |
| Sukat ng desibel | Audio feature engineering, speech recognition preprocessing |
| Teorya ng sampling | Ang Nyquist-Shannon theorem ay nag-uugnay sa wave theory sa digital signal processing |
---

## Buod
| Paksa | Pangunahing Ideya | Key Equation |
|-------|-----------|-------------|
| Wave equation | Ang mga alon ay dumadami sa bilis c | ∂²u/∂t² = c²∂²u/∂x² |
| Superposisyon | Ang mga alon ay nagdaragdag ng linearly | u = u₁ + u₂ |
| Panghihimasok | Tinutukoy ng phase ang reinforcement | Δφ = 2πΔL/λ |
| Diffraction | Ang mga alon ay yumuko sa mga hadlang | isang kasalanan θ = mλ (iisang hiwa) |
| Polariseysyon | Oryentasyon ng oscillation | Batas ni Malus: I = I₀cos²θ |
| Geometric na optika | Banayad na parang sinag | Batas ni Snell: n₁sinθ₁ = n₂sinθ₂ |
| Fourier optika | Imaging bilang Fourier transform | Malayong field = FT ng aperture |
| Doppler effect | Paglipat ng dalas mula sa paggalaw | f' = f(v ± v_o)/(v ∓ v_s) |
Ang mga alon ay ang unibersal na wika ng mga oscillating system. Nagpoproseso ka man ng mga signal ng audio, nagsusuri ng serye ng oras, nagdidisenyo ng mga sistema ng pagkilala ng imahe, o nagtatayo ng mga simulation ng pisika, ang matematika ng mga alon — superposisyon, pagsusuri ng Fourier, interference, diffraction — ay nagbibigay ng mahalagang toolkit. Ang optika, bilang pinaka-mature na agham ng alon, ay nag-aalok ng parehong teoretikal na pundasyon at praktikal na mga diskarte na tumatagos sa modernong data science.