<!--
---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teorya ng Kontrol
Ang teorya ng kontrol ay ang matematika ng paggawa ng mga system na kumilos sa paraang gusto mo sa kanila. Mula sa mga thermostat hanggang sa mga autopilot, mula sa mga robotic arm hanggang sa mga kemikal na reactor, ang mga control system ay nakadarama, nagpapasya, at kumikilos upang mapanatili ang nais na pag-uugali. Nagbibigay ang field ng mahigpit na tool para sa pagsusuri ng stability, performance, at robustness — mga konsepto na lumipat sa reinforcement learning, hyperparameter tuning, at adaptive system.
---

## Mga Pangunahing Konsepto
### Open-Loop vs Closed-Loop
| Uri | Paglalarawan | Halimbawa | Pakinabang |
|------|-------------|---------|-----------|
| **Open-loop** | Kontrolin ang pagkilos na hiwalay sa output | Timer ng washing machine | Simple, walang sensor na kailangan |
| **Closed-loop (feedback)** | Ang pagkilos ng kontrol ay nakasalalay sa output | Thermostat, cruise control | Tinatanggihan ang mga kaguluhan, matatag |
### Mga Elemento ng Block Diagram
| Elemento | Simbolo | Function |
|---------|--------|----------|
| **Halaman** | G(s) | Ang system na kinokontrol |
| **Controller** | C(s) | Kino-compute ang pagkilos ng kontrol |
| **Sensor** | H(s) | Sinusukat ang output |
| **Summing junction** | ⊕ | Error sa pagkalkula: r − y |
| **Sanggunian** | r(t) | Ninanais na output |
| **Error** | e(t) = r(t) − y(t) | Pagkakaiba sa pagitan ng ninanais at aktwal na |
| **Istorbo** | d(t) | Hindi gustong input na nakakaapekto sa planta |
### Closed-Loop Transfer Function
Para sa karaniwang negatibong feedback system:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s)
| Dami | Formula |
|----------|---------|
| Open-loop transfer function | L(s) = C(s)G(s)H(s) |
| Closed-loop transfer function | T(s) = L(s)/H(s) / (1 + L(s)) |
| Error sa paglilipat ng function | E(s)/R(s) = 1 / (1 + L(s)) |
| Pagkasensitibo | S(s) = 1 / (1 + L(s)) |
---

## Mga Pag-andar ng Paglipat
Ang **transfer function** H(s) = Y(s)/X(s) ay naglalarawan ng input-output na relasyon ng isang linear time-invariant (LTI) system sa Laplace domain.
### Mga Pamantayang Form
| System | Paglipat ng Function | Mga Parameter |
|--------|--------------------|------------|
| **First-order** | K/(τs + 1) | K = gain, τ = time constant |
| **Second-order** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = natural na dalas, ζ = damping ratio |
| **Integrator** | K/s | — |
| **Differentiator** | Ks | — |
| **Pag-antala** | e^{−sT_d} | T_d = pagkaantala ng oras |
### Gawi ng System ng Pangalawang Order
| Damping Ratio ζ | Pag-uugali | Mga Lokasyon ng Pole |
|-----------------|----------|----------------|
| ζ = 0 | Walang basang oscillation | Puro haka-haka |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Overdamped (mabagal, walang oscillation) | Totoo, naiiba |
### Mga Sukatan ng Pagganap (Step na Tugon)
| Sukatan | Formula (2nd order, underdamped) | Paglalarawan |
|---------|---------------------------------|------------|
| Oras ng pagtaas (t_r) | ≈ 1.8/ωₙ | Oras na para pumunta mula 10% hanggang 90% |
| Peak time (t_p) | π/(ωₙ√(1−ζ²)) | Oras sa unang maximum |
| Overshoot (M_p) | e^{−πζ/√(1−ζ²)} × 100% | Pinakamataas na peak sa itaas ng huling halaga |
| Oras ng pag-aayos (t_s) | ≈ 4/(ζωₙ) | Oras upang manatili sa loob ng 2% ng huling |
| Steady-state na error | Depende sa uri ng system | Pagkakaiba sa pagitan ng ninanais at aktwal bilang t → ∞ |
---

## Mga Controller ng PID
Ang **PID controller** ay ang pinakamalawak na ginagamit na controller sa industriya (higit sa 90% ng mga pang-industriyang controller).
### Formula ng PID
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
Sa domain ng Laplace: C(s) = K_p + K_i/s + K_d s
| Termino | Epekto | Sobra | Masyadong Maliit |
|------|--------|----------|------------|
| **Proporsyonal (K_p)** | Tumutugon sa kasalukuyang error | Oscillation, kawalang-tatag | Mabagal na tugon, malaking error |
| **Integral (K_i)** | Tinatanggal ang steady-state error | Overshoot, oscillation | Paulit-ulit na offset |
| **Derivative (K_d)** | Hinulaan ang error sa hinaharap (damping) | Pagpapalakas ng ingay | Mahina ang pagtanggi sa kaguluhan |
### Mga Paraan ng Pag-tune ng PID
| Paraan | Diskarte |
|--------|----------|
| **Ziegler-Nichols** | Taasan ang K_u hanggang sa oscillation; gamitin ang K_u at period P_u para magtakda ng mga nadagdag |
| **Cohen-Coon** | Batay sa mga parameter ng pagtugon sa hakbang (gain, time constant, dead time) |
| **IMC (Internal Model Control)** | Batay sa modelo ng proseso; nagbibigay ng magandang katatagan |
| **Auto-tuning** | Online na pagkakakilanlan + pag-tune (maraming modernong controller) |
| **Manwal** | Magsimula sa K_p lamang, magdagdag ng K_i upang alisin ang offset, magdagdag ng K_d para sa pamamasa |
### Mga Panuntunan ng Ziegler-Nichols
1. Itakda ang K_i = K_d = 0
2. Taasan ang K_p hanggang sa patuloy na oscillation: ultimate gain K_u, period P_u
3. Itakda ang mga nadagdag:
| Controller | K_p | K_i | K_d |
|-----------|-----|-----|-----|
| P | 0.5K_u | — | — |
| PI | 0.45K_u | 1.2K_u/P_u | — |
| PID | 0.6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Pagsusuri ng Katatagan
Ang isang system ay **stable** kung ang output nito ay mananatiling bounded para sa bounded inputs (BIBO stability).
### Pole-Based Stability
| Kundisyon | Katatagan |
|-----------|-----------|
| Lahat ng mga poste sa kaliwang kalahating eroplano (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Hindi matatag |
| Mga pole sa imaginary axis (Re(s) = 0) | Marginally stable (o hindi matatag para sa paulit-ulit) |
### Pamantayan ng Routh-Hurwitz
Tinutukoy ang katatagan nang hindi tahasan ang pagko-compute ng mga pole. Binubuo ang hanay ng Routh mula sa mga katangiang polynomial coefficient.
**Panuntunan:** Ang bilang ng mga pagbabago sa sign sa unang column ay katumbas ng bilang ng mga right-half-plane pole.
### Nyquist Stability Criterion
Ipino-plot ang open-loop frequency response L(jω) sa complex plane.
**Panuntunan:** Ang closed-loop system ay stable kung ang Nyquist plot ay pumapalibot sa punto (−1, 0) counter-clockwise ng ilang beses na katumbas ng bilang ng mga open-loop na hindi matatag na pole.
**Gain margin:** Magkano ang maaaring madagdagan bago ang kawalang-tatag (distansya mula sa plot hanggang −1 sa totoong axis).
**Phase margin:** Gaano karaming phase lag ang maaaring tumaas bago ang kawalang-tatag (anggulo mula sa plot hanggang unit circle sa gain crossover).
### Pagsusuri ng Bode Plot
Plot gain (dB) at phase (degrees) vs frequency (log scale).
| Sukatan | Kahulugan | Ninanais na Halaga |
|--------|-----------|--------------|
| **Gain margin (GM)** | Makakuha ng pagtaas upang maabot ang 0 dB sa phase = −180° | > 6 dB |
| **Phase margin (PM)** | Phase at gain crossover (0 dB) + 180° | > 45° |
| **Makakuha ng crossover** | Dalas kung saan nakakuha = 0 dB | — |
| **Phase crossover** | Dalas kung saan ang phase = −180° | — |
---

## Kinatawan ng Estado-Space
Para sa mga multi-input multi-output (MIMO) system, mas natural ang state-space form kaysa sa mga function ng paglilipat.
### Pamantayang Form
ẋ(t) = Ax(t) + Bu(t) (state equation)
y(t) = Cx(t) + Du(t) (output equation)
| Matrix | Pangalan | Mga sukat |
|--------|------|-----------|
| Isang | System/state matrix | n × n |
| B | Input matrix | n × m |
| C | Output matrix | p × n |
| D | Feedthrough matrix | p × m |
### Paglipat ng Function mula sa State-Space
G(s) = C(sI − A)⁻¹B + D
### Pagkontrol at Pagmamasid
| Ari-arian | Pagsubok | Ibig sabihin |
|----------|------|---------|
| **Nakokontrol** | Ranggo[C_B] = n (kung saan ang C_B = [B, AB, A²B, ...]) | Maaaring umiwas sa anumang estado |
| **Mapapansin** | Ranggo[O_B] = n (kung saan ang O_B = [C; CA; CA²; ...]) | Maaaring matukoy ang estado mula sa output |
Ang isang sistema ay dapat na nakokontrol upang maging matatag sa pamamagitan ng feedback, at mapapansin para sa pagtatantya ng estado.
### Feedback ng Estado
u = −Kx + r (buong feedback ng estado)
Closed-loop: ẋ = (A − BK)x + Br
**Paglalagay ng poste:** Piliin ang K upang ang A − BK ay may ninanais na eigenvalues ​​(pole).
---

## Pinakamainam na Kontrol
### Linear Quadratic Regulator (LQR)
Bawasan: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
kung saan ang Q ≥ 0 (gastos ng estado) at R > 0 (gastos sa pagkontrol).
**Solusyon:** u = −Kx kung saan ang K = R⁻¹BᵀP, at ang P ay nilulutas ang **algebraic Riccati equation:**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Pag-tune | Epekto |
|--------|--------|
| Dagdagan ang Q | Mas mabilis na tugon, mas maraming pagsisikap sa pagkontrol |
| Taasan ang R | Mas mabagal na tugon, mas kaunting pagsusumikap sa pagkontrol |
| Q ≫ R | Agresibong kontrol (tulad ng mataas na K_p) |
### Kalman Filter
Ang pinakamainam na estimator ng estado para sa mga linear system na may Gaussian noise.
**Modelo ng system:**
ẋ = Ax + Bu + w (process ingay w ~ N(0, Q))
y = Cx + v (pagsukat ng ingay v ~ N(0, R))
**Kalman filter equation:**
- Hula: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Update: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
Ang Kalman filter ay ang LQR dual — pinapaliit nito ang pagkakaiba-iba ng error sa pagtatantya.
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Teorya ng Kontrol | Application |
|----------------------|--------------------------|
| Kontrol ng feedback | Mga rate ng adaptive learning, stabilization ng pagsasanay |
| PID controllers | Hyperparameter tuning, temperatura control sa mga data center |
| Mga modelo ng state-space | Pagmomodelo ng serye ng oras, mga paulit-ulit na neural network |
| Kalman filter | Pagsubaybay, pagsasanib ng sensor, pagtatantya ng estado, pagtataya ng serye ng oras |
| LQR / pinakamainam na kontrol | Reinforcement learning (LQG control), robotics |
| Pagsusuri ng katatagan | Pagsasanay dynamics ng GANs, convergence ng RL algorithm |
| Pagkontrol/pagmamasid | Pag-unawa sa RNN expressiveness, system identification |
| Paglipat ng mga function | Pag-unawa sa mga CNN bilang mga linear na filter, frequency-domain analysis |
| Nyquist/Bode | Pagsusuri ng katatagan para sa mga adaptive system |
| Paglalagay ng poste | Pagdidisenyo ng dinamika ng mga natutunang sistema (Neural ODEs) |
---

## Buod
| Konsepto | Pangunahing Ideya | Key Tool |
|---------|-----------|----------|
| Feedback | Gamitin ang output upang itama ang input | Closed-loop transfer function |
| Paglipat ng function | Input-output na relasyon sa s-domain | G(s) = Y(s)/X(s) |
| Kontrol ng PID | Proporsyonal + Integral + Derivative | Pinakalawak na ginagamit na pang-industriya na controller |
| Katatagan | Bounded na output para sa bounded input | Routh-Hurwitz, Nyquist, Bode |
| State-space | Internal na representasyon ng estado | ẋ = Ax + Bu, y = Cx + Du |
| Kakayahang kontrolin | Maaari ba tayong makarating sa anumang estado? | Pagsusuri sa ranggo sa controllability matrix |
| Pagmamasid | Maaari ba nating ipahiwatig ang estado? | Rank test sa observability matrix |
| LQR | Pinakamainam na feedback ng estado | Riccati equation |
| Kalman filter | Pinakamainam na pagtatantya ng estado | Ikot ng hula-update |
Ang teorya ng kontrol ay ang matematika ng paggawa ng mga system na gawin ang gusto mo — mapagkakatiwalaan, matatag, at mahusay. Ang mga prinsipyo nito ng feedback, stability, at optimality ay napatunayang pangkalahatan, na lumilitaw sa mga larangan mula sa robotics hanggang sa reinforcement learning, mula sa economics hanggang biology. Para sa mga data scientist, ang control theory ay nagbibigay ng wika para sa pag-unawa sa mga adaptive system, pagdidisenyo ng mga stable na pamamaraan ng pagsasanay, at pagbuo ng mga matatalinong ahente na nakikipag-ugnayan sa mga dynamic na kapaligiran.