---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mga Dynamical na Sistema
Inilalarawan ng **dynamical system** kung paano umuunlad ang isang estado sa paglipas ng panahon ayon sa isang nakapirming panuntunan. Mula sa mga planetary orbit hanggang sa dynamics ng populasyon, mula sa mga pattern ng panahon hanggang sa pagsasanay sa mga neural network, ang teorya ng dynamical system ay nagbibigay ng wika at mga tool para sa pag-unawa kung paano nagbabago ang mga bagay. Sinasaklaw ng file na ito ang mga ordinaryong differential equation (ODEs), partial differential equation (PDEs), stability analysis, kaguluhan, at bifurcations.
---

## Ordinary Differential Equation (ODEs)
Iniuugnay ng isang ODE ang isang function sa mga derivative nito na may paggalang sa isang independiyenteng variable (karaniwang oras).
### Pag-uuri
| Ari-arian | Mga uri |
|----------|-------|
| **Utos** | Pinakamataas na derivative na kasalukuyan (1st order, 2nd order, atbp.) |
| **Linear vs Nonlinear** | Linear: y'' + p(t)y' + q(t)y = g(t); Nonlinear: kahit ano pa |
| **Homogeneous** | g(t) = 0 (walang sapilitang termino) |
| **Autonomous** | Walang tahasang pagdepende sa oras: dy/dt = f(y) |
| **Patuloy na coefficient** | p, q ay mga pare-pareho |
### Mga ODE sa Unang Order
**Pangkalahatang anyo:** dy/dt = f(t, y)
| Uri | Form | Paraan ng Solusyon |
|------|------|-----------------|
| Nahihiwalay | dy/dt = g(t)h(y) | Paghiwalayin at pagsamahin: ∫dy/h(y) = ∫g(t)dt |
| Linear na unang-order | dy/dt + p(t)y = q(t) | Integrating factor: μ(t) = e^(∫p dt) |
| Eksaktong | M(t,y)dt + N(t,y)dy = 0 na may ∂M/∂y = ∂N/∂t | Maghanap ng potensyal na function F(t,y) |
| Bernoulli | dy/dt + p(t)y = q(t)yⁿ | Palitan ang v = y^(1−n) sa linearise |
**Nagtrabahong Halimbawa (Integrating Factor):** Lutasin ang dy/dt + 2y = e^(−t), y(0) = 1.
- Integrating factor: μ(t) = e^(∫2 dt) = e^(2t)
- Multiply: d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- Pagsamahin: e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Paunang kundisyon: y(0) = 1 → 1 = 1 + C → C = 0
- Solusyon: y(t) = e^(−t)
### Mga Second-Order Linear ODE
**Pangkalahatang anyo:** ay'' + by' + cy = g(t)
**Homogeneous case** (g ​​= 0): Lutasin ang characteristic equation ar² + br + c = 0.
| Nakakadiskrimina | Mga ugat | Pangkalahatang Solusyon |
|-------------|-------|------------------|
| b² > 4ac (overdamped) | Dalawang magkaibang tunay na r₁, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (critically damped) | Paulit-ulit na tunay na ugat r | y = (C₁ + C₂t)e^(rt) |
| b² < 4ac (underdamped) | Mga kumplikadong ugat α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |
**Pisikal na interpretasyon:** Isang mass-spring-damper system mx'' + bx' + kx = 0.
- Overdamped: mabigat na pamamasa, walang oscillation (door closer)
- Critically damped: pinakamabilis na pagbabalik nang walang oscillation (target sa disenyo ng suspensyon ng kotse)
- Underdamped: oscillates na may nabubulok na amplitude (kuwerdas ng gitara)
### Sistema ng mga ODE
Maraming mga tunay na sistema ang nagsasangkot ng maraming mga variable na nakikipag-ugnayan:
dx/dt = f(x, y)
dy/dt = g(x, y)
Maaari itong isulat sa anyong vector: d**x**/dt = **F**(**x**)
**Linear system:** d**x**/dt = A**x**, kung saan ang A ay isang matrix.
Ang solusyon ay depende sa eigenvalues ​​ng A:
| Eigenvalues ​​| Pag-uugali |
|-------------|-----------|
| Parehong totoo, negatibo | Stable node (lahat ng trajectory ay nagtatagpo sa pinanggalingan) |
| Parehong totoo, positibo | Hindi matatag na node |
| Totoo, magkasalungat na mga palatandaan | Saddle point (hindi matatag) |
| Kumplikado, negatibong tunay na bahagi | Matatag na spiral (damped oscillation) |
| Kumplikado, positibong tunay na bahagi | Hindi matatag na spiral |
| Puro haka-haka | Gitna (mga saradong orbit) |
---

## Phase Portraits
Ang isang **phase portrait** ay nagpapakita ng mga trajectory ng isang dynamical system sa state space (nang walang tahasang paglutas).
### Mga Pangunahing Tampok
| Tampok | Paglalarawan |
|---------|-------------|
| **Fixed point (equilibrium)** | Kung saan ang dx/dt = 0 (walang galaw) |
| **Trajectory** | Path na sinusubaybayan ng system sa state space |
| **Nullcline** | Curve kung saan ang derivative ng isang component ay zero |
| **Limitahan ang cycle** | Isolated closed orbit (self-sustained oscillation) |
| **Basin of attraction** | Set ng mga paunang kundisyon na humahantong sa isang ibinigay na pang-akit |
| **Separatrix** | Hangganan sa pagitan ng iba't ibang basin ng atraksyon |
### Predator-Prey Model (Lotka-Volterra)
dx/dt = αx − βxy (biktima)
dy/dt = δxy − γy (mandaragit)
**Mga nakapirming puntos:**
1. (0, 0) — pagkalipol (saddle point)
2. (γ/δ, α/β) — magkakasamang buhay (gitna — mga saradong orbit)
Ang sistema ay nagpapakita ng mga panaka-nakang oscillations: dumarami ang biktima → dumarami ang mga mandaragit → bumababa ang biktima → bumababa ang mga mandaragit → umuulit ang cycle.
---

## Pagsusuri ng Katatagan
### Linear Stability
Para sa isang nakapirming puntong x*, linearise sa paligid nito: hayaan ang u = x − x*, pagkatapos du/dt ≈ J(x*)u kung saan ang J ay ang Jacobian matrix.
**Stability criterion:** Ang nakapirming punto ay:
- **Stable** kung ang lahat ng eigenvalues ng J ay may mga negatibong tunay na bahagi
- **Hindi matatag** kung ang anumang eigenvalue ay may positibong tunay na bahagi
- **Marginally stable** kung ang eigenvalues ay may zero real parts (kailangan ng nonlinear analysis)
### Lyapunov Stability
**Ang direktang pamamaraan ni Lyapunov** ay tumutukoy sa katatagan nang walang linearization.
Ang **Lyapunov function** V(x) ay nakakatugon sa:
1. V(x*) = 0 at V(x) > 0 para sa x ≠ x* (positive definite)
2. dV/dt ≤ 0 kasama ang mga trajectory (hindi tumataas)
| Kundisyon | Konklusyon |
|-----------|------------|
| dV/dt< 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt >0 | Hindi matatag |
**Nagtrabaho Halimbawa:** System dx/dt = −x + y², dy/dt = −y.
- Subukan ang V(x,y) = x² + y² (tulad ng enerhiya na function)
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Malapit sa pinanggalingan: dV/dt ≈ −2x² − 2y² < 0 (para sa maliit na y, nangingibabaw ang −2y²)
- Konklusyon: ang pinanggalingan ay lokal na asymptotically stable
---

## Teorya ng Chaos
Ang **Chaos** ay deterministiko ngunit hindi mahuhulaan: ang system ay sumusunod sa mga eksaktong panuntunan, ngunit ang mga maliliit na pagkakaiba sa mga paunang kundisyon ay humahantong sa napakakaibang mga resulta.
### Mga Kinakailangan para sa Chaos
| Ari-arian | Paglalarawan |
|----------|-------------|
| Deterministic | Walang randomness — pinamamahalaan ng mga eksaktong equation |
| Sensitibo sa mga paunang kundisyon | Ang mga kalapit na trajectory ay nag-iiba nang malaki |
| Bounded | Ang mga tilapon ay hindi nakatakas sa kawalang-hanggan |
| Hindi pana-panahon | Hindi kailanman umuulit nang eksakto |
### Ang Lorenz System
Ang klasikong halimbawa ng deterministikong kaguluhan:
dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy − βz
Sa karaniwang mga parameter σ = 10, ρ = 28, β = 8/3:
- Ang sistema ay may tatlong nakapirming puntos, lahat ay hindi matatag
- Ang mga tilapon ay umiikot sa isang nakapirming punto, pagkatapos ay biglang lumipat sa isa pa
- Ang resulta ay ang **Lorenz attractor** — isang kakaibang attractor na may fractal structure
**Lyapunov exponent:** Sinusukat ang rate ng divergence ng mga kalapit na trajectory.
- Positibong Lyapunov exponent → kaguluhan
- Para sa Lorenz system na may karaniwang mga parameter: pinakamalaking exponent ≈ 0.9 > 0
### Ang Logistic Map
Isang simpleng discrete system na nagpapakita ng kaguluhan:
x_{n+1} = rx_n(1 − x_n)
| Parameter r | Pag-uugali |
|-------------|-----------|
| 0 < r < 1 | Namatay ang populasyon (x → 0) |
| 1 < r < 3 | Matatag na nakapirming punto sa x = 1 − 1/r |
| 3 < r < 3.449 | Panahon-2 oscillation |
| 3.449 < r < 3.544 | Panahon-4 na oscillation |
| 3.544 < r < 3.570 | Panahon-8, 16, 32, ... (period-doubling cascade) |
| r ≈ 3.570 | Pagsisimula ng kaguluhan |
| 3.570 < r < 4 | Kadalasan ay magulo, na may panaka-nakang mga bintana |
| r = 4 | Ganap na magulo sa [0, 1] |
### Butterfly Effect
Ang sikat na pangalan para sa sensitibong pag-asa sa mga paunang kundisyon. Sa mga sistema ng lagay ng panahon (modelo ng Lorenz equation), ang isang butterfly na nagpapakpak ng mga pakpak nito sa Brazil ay maaaring magdulot ng buhawi sa Texas - hindi dahil sa butterfly ang sanhi nito, ngunit dahil ang maliliit na perturbation ay lumalaki nang malaki.
---

## Teorya ng Bifurcation
Ang **bifurcation** ay isang qualitative na pagbabago sa gawi ng system habang ang isang parameter ay iba-iba.
### Mga Uri ng Bifurcations
| Bifurcation | Normal na Anyo | Ano ang Mangyayari |
|-------------|-------------|--------------|
| **Saddle-node** | dx/dt = r − x² | Lumilitaw/nawawala ang dalawang nakapirming punto |
| **Transcritical** | dx/dt = rx − x² | Dalawang fixed point exchange stability |
| **Pitchfork (supercritical)** | dx/dt = rx − x³ | Ang isang stable point ay nahahati sa dalawang stable + isang unstable |
| **Pitchfork (subcritical)** | dx/dt = rx + x³ | Ang mga hindi matatag na sanga ay bumagsak (madalas na sakuna) |
| **Hopf** | 2D system | Ang nakapirming punto ay nagiging hindi matatag, lumilitaw ang ikot ng limitasyon |
### Diagram ng Bifurcation
Isang plot ng mga fixed point vs parameter value, na nagpapakita ng stability (solid = stable, dashed = unstable). Ang diagram ng bifurcation ng logistic na mapa ay nagpapakita ng period-double na ruta patungo sa kaguluhan at ang sikat na **Feigenbaum constant** δ ≈ 4.669 (universal ratio sa pagitan ng sunud-sunod na bifurcation interval).
---

## Mga Partial Differential Equation (PDE)
Ang mga PDE ay nagsasangkot ng mga function ng maramihang mga variable at ang kanilang mga bahagyang derivatives.
### Klasipikasyon ng Second-Order Linear PDEs
Para sa Au_xx + 2Bu_xy + Cu_yy + ... = 0:
| Uri | Kundisyon | Pag-uugali | Halimbawa |
|------|-----------|-----------|---------|
| **Elliptic** | B² − AC< 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC >0 | Ang pagpapalaganap ng alon, pinapanatili ang matalim na katangian | Wave equation: u_tt = c²u_xx |
### Ang Heat Equation
∂u/∂t = α ∂²u/∂x²
Mga modelo ng heat diffusion, pagkalat ng populasyon, pagpepresyo ng opsyon (Black-Scholes).
| Ari-arian | Pahayag |
|----------|-----------|
| Pagpapakinis | Ang mga solusyon ay nagiging maayos kaagad, kahit na mula sa hindi tuloy-tuloy na paunang data |
| Pinakamataas na prinsipyo | Ang pinakamataas na temperatura ay nangyayari sa hangganan o paunang oras |
| Time-reversibility | Hindi maibabalik — hindi maaaring tumakbo pabalik |
### Ang Wave Equation
∂²u/∂t² = c² ∂²u/∂x²
Mga modelo ng vibrating string, tunog, electromagnetic waves.
| Ari-arian | Pahayag |
|----------|-----------|
| Pagpapalaganap | Ang mga kaguluhan ay naglalakbay sa bilis c |
| Pagbabalik-tanaw | Time-reversible |
| solusyon sa d'Alembert | u(x,t) = f(x−ct) + g(x+ct) (superposisyon ng kaliwa/kanang alon) |
### Laplace's Equation
∇²u = ∂²u/∂x² + ∂²u/∂y² = 0
Ang mga solusyon (harmonic function) ay kumakatawan sa steady-state na temperatura, electrostatic potential, incompressible fluid flow.
| Ari-arian | Pahayag |
|----------|-----------|
| Mean value property | u(x₀) = average ng u sa anumang bilog na nakasentro sa x₀ |
| Pinakamataas na prinsipyo | Walang panloob na maxima o minima |
| Kakaiba | Ganap na tinutukoy ng mga kundisyon ng hangganan |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng DS | Application |
|-----------|-------------|
| Mga ODE | Mga Neural ODE (continuous-depth network), paulit-ulit na dynamics ng network |
| Pagsusuri ng katatagan | Pagsasanay dynamics ng gradient descent (ang pagkawala ay bumababa nang matatag?) |
| Lyapunov functions | Pagpapatunay ng tagpo ng mga algorithm sa pag-aaral, pagpapalakas ng katatagan ng pag-aaral |
| Kaguluhan | Pag-unawa sa pagiging sensitibo sa mga RNN (naglalaho/sumasabog na mga gradient), hula ng panahon |
| Bifurcation | Mga yugto ng paglipat sa pag-aaral (grokking), pagbabago ng rehimen sa dinamika ng pagsasanay |
| Mga PDE | Mga modelo ng pagsasabog (mga modelong nakabatay sa marka), mga neural network na may kaalaman sa pisika |
| Equation ng init | Mga proseso ng pagsasabog sa generative modelling, graph Laplacian smoothing |
| Wave equation | Pagproseso ng data ng seismic, pagmomodelo ng signal ng audio |
| Lotka-Volterra | Dinamika ng populasyon, epidemiology, nakikipagkumpitensyang mga ahente ng ML |
| Mga phase portrait | Nakikita ang pagkawala ng dynamics ng landscape, pag-unawa sa pagsasanay sa GAN |
---

## Buod
| Paksa | Pangunahing Ideya | Key Tool |
|-------|-----------|----------|
| Mga ODE | Mga function at ang kanilang mga derivative ng oras | Mga katangiang equation, pagsasama ng mga salik |
| Sistema ng mga ODE | Maramihang nakikipag-ugnayang variable | Eigenvalue analysis ng Jacobian |
| Mga phase portrait | Pagpapakita ng dinamika sa espasyo ng estado | Mga nakapirming puntos, nullclines, limit cycles |
| Katatagan | Babalik ba ang sistema sa ekwilibriyo? | Linearization, Lyapunov functions |
| Kaguluhan | Deterministic unpredictability | Lyapunov exponents, kakaiba attractors |
| Bifurcations | Mga pagbabago sa kalidad na may mga parameter | Mga normal na anyo, mga diagram ng bifurcation |
| Mga PDE | Mga function ng maramihang mga variable | Heat, wave, at Laplace equation |
Ang teorya ng dinamikong sistema ay ang matematika ng pagbabago. Ipinapaliwanag nito kung bakit umuusad ang ilang sistema, kung bakit nag-oocillate ang ilan, at kung bakit magulo ang pagkilos ng ilan. Para sa mga data scientist, nagbibigay ito ng mga tool para sa pag-unawa sa dynamics ng pagsasanay, pagdidisenyo ng mga matatag na algorithm, pagmomodelo ng time series, at pagbuo ng susunod na henerasyon ng mga modelo ng machine learning na may kaalaman sa physics.