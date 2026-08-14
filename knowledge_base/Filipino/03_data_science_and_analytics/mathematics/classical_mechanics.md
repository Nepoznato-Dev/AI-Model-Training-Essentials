---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Classical Mechanics
Ang klasikal na mekanika ay naglalarawan ng paggalaw ng mga bagay sa ilalim ng impluwensya ng mga puwersa. Mula sa mga bumabagsak na mansanas hanggang sa nag-oorbit na mga planeta, mula sa nanginginig na mga string hanggang sa nagbabanggaan na mga particle, ang mga prinsipyo nito ay namamahala sa macroscopic na mundo. Higit pa sa mga pisikal na aplikasyon nito, ang mga klasikal na mekanika ay nagsilang ng calculus ng mga variation, symplectic geometry, at ang Hamiltonian framework na sumasailalim sa quantum mechanics at modernong optimization.
---

## Newtonian Mechanics
### Tatlong Batas ni Newton
| Batas | Pahayag | Anyo ng Matematika |
|-----|-----------|--------------------|
| **Una (Inertia)** | Ang isang bagay ay nananatili sa pahinga o sa pare-parehong paggalaw maliban kung kumilos sa pamamagitan ng isang puwersa | Kung F_net = 0, kung gayon v = pare-pareho |
| **Ikalawa (F = ma)** | Ang puwersa ay katumbas ng mass times acceleration | **F** = m**a** = m(d²**x**/dt²) |
| **Ikatlo (Aksyon-Reaksyon)** | Ang bawat aksyon ay may pantay at kasalungat na reaksyon | **F**₁₂ = −**F**₂₁ |
### Free-Body Diagram
Ang **free-body diagram** ay naghihiwalay ng isang bagay at nagpapakita ng lahat ng pwersang kumikilos dito.
**Mga karaniwang puwersa:**
| Puwersa | Formula | Direksyon |
|-------|---------|-----------|
| Gravity (malapit sa Earth) | F = mg | Pababa |
| Normal na puwersa | N | Patayo sa ibabaw |
| Friction (static) | f_s ≤ μ_s N | Sinasalungat ang nalalapit na mosyon |
| Friction (kinetic) | f_k = μ_k N | Sumasalungat sa mosyon |
| Spring (Batas ni Hooke) | F = −kx | Pagpapanumbalik (patungo sa ekwilibriyo) |
| Tensyon | T | Kasama ang string/lubid |
| I-drag | F_d = ½C_d ρAv² | Sumasalungat sa bilis |
### Nagtrabaho Halimbawa: Block on Incline
Isang bloke ng mass m sa isang frictionless incline sa anggulo θ.
- Mga pwersa: gravity (mg pababa), normal na puwersa (N patayo sa ibabaw)
- Decompose gravity: mg sin θ (sa kahabaan ng incline), mg cos θ (sa ibabaw)
- N = mg cos θ (walang paggalaw na patayo sa ibabaw)
- Pagpapabilis sa kahabaan ng incline: a = g sin θ
---

## Mga Paraan ng Enerhiya
### Trabaho at Kinetic Energy
**Trabaho** na ginawa ng puwersa: W = ∫ **F** · d**r**
**Work-Energy Theorem:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Potensyal na Enerhiya
| Puwersa | Potensyal na Enerhiya | Mga Tala |
|-------|-----------------|-------|
| Gravity (malapit sa ibabaw) | U = mgh | h = taas sa itaas ng sanggunian |
| Gravity (pangkalahatan) | U = −GMm/r | Zero sa infinity |
| Spring | U = ½kx² | x = displacement mula sa ekwilibriyo |
| Electrostatic | U = kq₁q₂/r | Tulad ng mga singil: positibong U |
### Pagtitipid ng Enerhiya
Kung ang mga konserbatibong pwersa lamang ay kumikilos: E = KE + PE = pare-pareho
½mv₁² + U₁ = ½mv₂² + U₂
**Nagtrabaho Halimbawa:** Isang bola ang nahulog mula sa taas h.
- Inisyal: KE = 0, PE = mgh
- Bago tumama sa lupa: KE = ½mv², PE = 0
- Konserbasyon: mgh = ½mv² → v = √(2gh)
### Kapangyarihan
P = dW/dt = **F** · **v** (rate ng paggawa)
---

## Momentum at Pagbangga
### Linear Momentum
**p** = m**v**
Pangalawang batas ni Newton (alternatibong anyo): **F** = d**p**/dt
### Conservation of Momentum
Kung walang mga panlabas na puwersa: ang kabuuang momentum ay pinananatili.
| Uri ng banggaan | KE Conserved? | Napanatili ang Momentum? |
|--------------|----------------|---------------------|
| **Nababanat** | Oo | Oo |
| **Hindi nababanat** | Hindi | Oo |
| **Ganap na hindi nababanat** | Hindi (maximum na pagkawala) | Oo (magkadikit ang mga bagay) |
**1D elastic collision:** Dalawang masa m₁, m₂ na may mga paunang bilis u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Angular Momentum
**L** = **r** × **p** = m(**r** × **v**)
Torque: **τ** = d**L**/dt = **r** × **F**
**Conservation:** Kung walang external torque, angular momentum ay mapangalagaan.
---

## Lagrangian Mechanics
Pinapalitan ng **Lagrangian** formulation ang mga puwersa ng enerhiya, na nagbibigay ng mas elegante at pangkalahatang framework.
### Ang Lagrangian
L = T − V (kinetic energy minus potensyal na enerhiya)
### Prinsipyo ng Pinakamaliit na Pagkilos (Ang Prinsipyo ni Hamilton)
Ang aktwal na landas na tinatahak ng isang system sa pagitan ng mga oras na t₁ at t₂ ay nagpapaliit (mas tiyak, ginagawang nakatigil) ang **action**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Euler-Lagrange Equation
Ang kundisyon δS = 0 ay nagbubunga:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
para sa bawat pangkalahatang coordinate q.
**Nagtrabaho Halimbawa:** Simpleng pendulum (haba l, mass m, angle θ mula patayo).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Mga Bentahe ng Lagrangian Mechanics
| Pakinabang | Paliwanag |
|-----------|-------------|
| Coordinate-independent | Gumagana sa anumang coordinate system |
| Natural na humahawak sa mga hadlang | Hindi na kailangang kalkulahin ang mga puwersa ng pagpilit |
| Symmetry → konserbasyon | Ang teorama ni Noether ay nag-uugnay ng mga simetriko sa mga natipid na dami |
| Madaling nag-generalise | Sa mga field, relativity, quantum mechanics |
---

## Hamiltonian Mechanics
Ang **Hamiltonian** formulation ay isang reformulation ng Lagrangian mechanics na gumagamit ng mga posisyon at momenta (sa halip na mga posisyon at bilis).
### Ang Hamiltonian
H = Σᵢ pᵢq̇ᵢ − L = T + V (para sa karamihan ng mga mekanikal na sistema)
kung saan ang pᵢ = ∂L/∂q̇ᵢ ay ang **generalized momenta**.
### Mga Equation ni Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Ito ay 2n first-order ODEs (vs n second-order Euler-Lagrange equation).
**Nagtrabaho Halimbawa:** Harmonic oscillator (mass m, spring constant k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (gaya ng inaasahan)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (batas ni Hooke)
### Mga Bracket ng Poisson
Para sa mga function f(q, p) at g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Ari-arian | Pahayag |
|----------|-----------|
| Ebolusyon ng oras | df/dt = {f, H} + ∂f/∂t |
| Conservation | f ay pinananatili kung {f, H} = 0 (at ∂f/∂t = 0) |
| Mga pangunahing bracket | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Koneksyon sa quantum mechanics:** Ang mga Poisson bracket ay nagiging mga commutator: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Conservation Laws at Noether's Theorem
### Noether's Theorem
Ang bawat tuluy-tuloy na simetrya ng Lagrangian ay tumutugma sa isang conserved na dami.
| Symmetry | Natitipid na Dami |
|----------|--------------------|
| Invariance ng pagsasalin ng oras | Enerhiya |
| Invariance ng spatial na pagsasalin | Linear momentum |
| Rotational invariance | Angular na momentum |
| Gauge invariance | singilin ng kuryente |
Isa ito sa pinakamalalim na resulta sa lahat ng pisika — ikinokonekta nito ang geometry ng spacetime sa mga pangunahing batas sa konserbasyon.
---

## Rigid Body Dynamics
Ang **matibay na katawan** ay isang bagay kung saan nananatiling maayos ang lahat ng panloob na distansya.
### Mga Pangunahing Konsepto
| Konsepto | Formula | Paglalarawan |
|---------|---------|-------------|
| **Moment of inertia** | I = Σmᵢrᵢ² o I = ∫r² dm | Paglaban sa rotational acceleration |
| **Paikot na KE** | KE = ½Iω² | Enerhiya ng pag-ikot |
| **Angular momentum** | L = Iω | Rotational analogue ng p = mv |
| **Torque** | τ = Iα | Rotational analogue ng F = ma |
### Mga Sandali ng Inertia (Mga Karaniwang Hugis)
| Hugis | Axis | ako |
|-------|------|---|
| Solid na globo | Sa pamamagitan ng center | (2/5)MR² |
| Hollow sphere | Sa pamamagitan ng center | (2/3)MR² |
| Solid na silindro | Kasama ang axis | (1/2)MR² |
| Manipis na pamalo | Sa pamamagitan ng gitna, patayo | (1/12)ML² |
| Manipis na pamalo | Sa pamamagitan ng dulo, patayo | (1/3)ML² |
| Disc | Sa pamamagitan ng gitna, patayo | (1/2)MR² |
---

## Orbital Mechanics
### Mga Batas ni Kepler
| Batas | Pahayag |
|-----|-----------|
| **Una (Ellipses)** | Ang mga planeta ay gumagalaw sa mga ellipse kasama ang Araw sa isang focus |
| **Ikalawa (Pantay na mga lugar)** | Ang isang linya mula sa Araw patungo sa planeta ay nagwawalis ng pantay na mga lugar sa pantay na oras |
| **Ikatlo (Harmonic)** | T² ∝ a³ (period squared proportional sa semi-major axis cubed) |
### Orbital Energy
E = ½mv² − GMm/r
| E | Uri ng Orbit |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hyperbolic (unbound) |
### Bilis ng Pagtakas
v_escape = √(2GM/R)
Para sa Earth: v_escape ≈ 11.2 km/s
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Mekanika | Application |
|------------------|-------------|
| Mga batas ni Newton | Physics engine sa simulation, laro AI, robotics |
| Mga pamamaraan ng enerhiya | Mga modelong nakabatay sa enerhiya, mga network ng Hopfield, mga makinang Boltzmann |
| Lagrangian mechanics | Mga neural network na may kaalaman sa pisika, pinakamainam na kontrol, pag-optimize ng trajectory |
| Hamiltonian mechanics | Hamiltonian neural network (HNNs), symplectic integrators para sa simulation |
| Mga batas sa konserbasyon | Mga inductive bias sa mga modelo ng ML, mga katumbas na neural network |
| Ang teorama ni Noether | Symmetry-aware machine learning, geometric deep learning |
| Rigid body dynamics | Robotics simulation, molecular dynamics, 3D animation |
| Mekanika ng orbital | Satellite positioning (GPS para sa location-based ML), space mission design |
| Phase space (Hamiltonian) | Pag-unawa sa mga dynamical system, mga network ng pang-akit |
| Calculus ng mga variation | Pinakamainam na transportasyon, generative modeling (flow matching) |
---

## Buod
| Balangkas | Core Equation | Lakas |
|-----------|--------------|----------|
| Newtonian | **F** = m**a** | Intuitive, direktang pagsusuri ng puwersa |
| Lagrangian | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Walang coordinate, humahawak ng mga hadlang |
| Hamiltonian | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Symplectic na istraktura, kumokonekta sa QM |
| Mga batas sa konserbasyon | Ang teorama ni Noether | Malalim na symmetry-conservation na koneksyon |
Ang klasikal na mekanika ay hindi lamang tungkol sa pagbagsak ng mga bola at pagtatayon ng mga pendulum. Ang mga mathematical framework nito — Lagrangian at Hamiltonian mechanics — ay kabilang sa mga pinaka-maimpluwensyang ideya sa lahat ng agham. Nag-generalize ang mga ito sa quantum mechanics, field theory, at maging sa modernong machine learning, kung saan ang mga modelong nakabatay sa enerhiya at mga neural network na may kaalaman sa pisika ay direktang gumuguhit sa mga pormulasyon na ito sa mga siglong gulang na.