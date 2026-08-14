---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Electromagnetism
Ang electromagnetism ay ang pag-aaral ng mga electric at magnetic field at ang kanilang mga pakikipag-ugnayan. Pinag-isa ni Maxwell noong 1860s, ipinapaliwanag ng electromagnetism ang liwanag, kuryente, magnetism, radio waves, at ang istraktura ng mga atomo. Ito ang unang pangunahing puwersa na lubos na naunawaan sa matematika, at ang mga equation nito ay nagbigay inspirasyon sa espesyal na relativity at modernong field theory ni Einstein.
---

## Mga Electric Field
### Batas ng Coulomb
Ang puwersa sa pagitan ng dalawang puntong singil q₁ at q₂ na pinaghihiwalay ng distansya r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| pare-pareho | Halaga |
|----------|-------|
| ε₀ (pagpapahintulot ng libreng espasyo) | 8.854 × 10⁻¹² F/m |
| 1/4πε₀ (Coulomb constant k) | 8.988 × 10⁹ N·m²/C² |
### Depinisyon ng Electric Field
**E** = **F**/q (force per unit charge)
Para sa isang point charge Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Electric Field Lines
| Ari-arian | Panuntunan |
|----------|------|
| Direksyon | Ituro ang layo mula sa mga positibong singil, patungo sa negatibo |
| Densidad | Mas malapit na linya = mas malakas na field |
| pagtawid | Ang mga linya ng field ay hindi kailanman tumatawid |
| Mga konduktor | Ang mga linya ay nagtatagpo sa ibabaw nang patayo |
### Potensyal ng Elektrisidad (Voltage)
V = −∫ **E** · d**l** (ang potensyal na pagkakaiba ay ang negatibong line integral ng E)
**E** = −∇V (ang field ay ang negatibong gradient ng potensyal)
Para sa isang point charge: V = (1/4πε₀) · Q/r
| Konsepto | Formula | Yunit |
|---------|---------|------|
| Potensyal na enerhiya | U = qV | Joules |
| Electron-volt | 1 eV = 1.602 × 10⁻¹⁹ J | Yunit ng enerhiya |
| Equipotential ibabaw | Ibabaw kung saan ang V ay pare-pareho | Ang E ay patayo dito |
---

## Batas ni Gauss
### Pahayag
Ang kabuuang electric flux sa anumang saradong ibabaw ay katumbas ng nakapaloob na singil na hinati sa ε₀:
∮ **E** · d**A** = Q_enc / ε₀
Sa differential form: ∇ · **E** = ρ/ε₀
### Paggamit ng Gauss's Law
Ang batas ni Gauss ay pinaka-kapaki-pakinabang kapag pinahihintulutan ng symmetry ang E na ma-pull out sa integral.
| Symmetry | Gaussian Surface | Resulta |
|----------|-----------------|--------|
| Pabilog | Sphere | E = Q/(4πε₀r²) sa labas |
| Cylindrical (line charge) | Silindro | E = λ/(2πε₀r) |
| Planar (walang katapusang sheet) | Pillbox | E = σ/(2ε₀) |
| Sa pagitan ng parallel plates | Pillbox | E = σ/ε₀ |
---

## Mga Konduktor at Capacitor
### Mga Konduktor sa Electrostatic Equilibrium
| Ari-arian | Paliwanag |
|----------|-------------|
| E = 0 sa loob | Muling ayusin ang mga singil upang kanselahin ang panloob na field |
| Lahat ng charge sa ibabaw | Walang netong bayad sa loob |
| E patayo sa ibabaw | Walang tangential component (kung hindi man ay gumagalaw ang mga singil) |
| Equipotential sa buong | Parehong V kahit saan sa loob at sa ibabaw |
### Mga Kapasitor
Ang **capacitor** ay nag-iimbak ng enerhiya sa isang electric field sa pagitan ng dalawang konduktor.
| Configuration | Kapasidad |
|--------------|-------------|
| Parallel plates | C = ε₀A/d |
| Cylindrical | C = 2πε₀L / ln(b/a) |
| Pabilog | C = 4πε₀ab / (b−a) |
| Formula | Pagpapahayag |
|---------|------------|
| Charge-boltahe | Q = CV |
| Enerhiya na nakaimbak | U = ½CV² = ½Q²/C |
| Densidad ng enerhiya | u = ½ε₀E² |
| kumbinasyon ng serye | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Parallel na kumbinasyon | C_total = C₁ + C₂ + ... |
### Dielectrics
Ang pagpasok ng dielectric (insulating material) na may pare-parehong κ ay nagpapataas ng kapasidad: C = κC₀.
---

## Mga Magnetic Field
### Magnetic Force
**F** = q(**v** × **B**) (Lorentz force, magnetic component)
| Ari-arian | Pahayag |
|----------|-----------|
| Direksyon | Perpendicular sa parehong v at B (right-hand rule) |
| Tapos na ang trabaho | Zero (ang puwersa ay patayo sa bilis) |
| Pabilog na galaw | Radius r = mv/(qB) sa pare-parehong B field |
### Biot-Savart Law
Ang magnetic field dahil sa isang maliit na kasalukuyang elemento:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| pare-pareho | Halaga |
|----------|-------|
| μ₀ (permeability ng libreng espasyo) | 4π × 10⁻⁷ T·m/A |
### Batas ng Ampere
∮ **B** · d**l** = μ₀I_enc
Sa differential form: ∇ × **B** = μ₀**J**
**Mga Application:**
| Configuration | B field |
|--------------|---------|
| Mahabang straight wire | B = μ₀I/(2πr) |
| Solenoid (sa loob) | B = μ₀nI |
| Toroid (sa loob) | B = μ₀NI/(2πr) |
---

## Electromagnetic Induction
### Batas ni Faraday
Ang pagbabago ng magnetic flux ay nag-uudyok ng electromotive force (EMF):
EMF = −dΦ_B/dt
kung saan ang Φ_B = ∫ **B** · d**A** ay ang magnetic flux.
Sa differential form: ∇ × **E** = −∂**B**/∂t
**Lenz's law:** Ang induced EMF ay sumasalungat sa pagbabago sa flux (ang minus sign).
### Mga Aplikasyon ng Induction
| Application | Prinsipyo |
|-------------|-----------|
| Generator | Umiikot na coil sa B field → alternating EMF |
| Transpormer | Pagbabago ng kasalukuyang sa pangunahin → EMF sa pangalawang |
| Inductor | Sinasalungat ang mga pagbabago sa kasalukuyang: EMF = −L(dI/dt) |
| Eddy currents | Induced currents sa mga bulk conductor (pagpepreno, pag-init) |
### Induktor
| Formula | Pagpapahayag |
|---------|------------|
| Linkage ng pagkilos ng bagay | Φ = LI |
| Enerhiya na nakaimbak | U = ½LI² |
| kumbinasyon ng serye | L_kabuuan = L₁ + L₂ + ... |
| Parallel na kumbinasyon | 1/L_kabuuan = 1/L₁ + 1/L₂ + ... |
---

## Mga Equation ni Maxwell
Pinag-iisa ng mga equation ni Maxwell ang kuryente at magnetism sa isang teorya.
### Sa Integral Form
| Equation | Pangalan | Pahayag |
|----------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Batas ni Gauss (electric) | Electric flux = nakapaloob na singil |
| ∮ **B** · d**A** = 0 | Batas ni Gauss (magnetic) | Walang magnetic monopole |
| ∮ **E** · d**l** = −dΦ_B/dt | Batas ni Faraday | Ang pagpapalit ng B ay nag-uudyok sa E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Batas ng Ampere-Maxwell | Ang kasalukuyan at nagbabagong E ay gumagawa ng B |
### Sa Differential Form
| Equation | Pangalan | Pagpapahayag |
|----------|------|------------|
| Gauss (electric) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnetic) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampere-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### Ang Kasalukuyang Pag-aalis
Ang pangunahing karagdagan ni Maxwell: ang terminong μ₀ε₀ ∂**E**/∂t (displacement current). Tinitiyak nito ang pagtitipid ng singil at hinuhulaan ang mga electromagnetic wave.
---

## Mga Electromagnetic Waves
Sa vacuum (walang singil, walang agos), ang mga equation ni Maxwell ay nagbubunga ng mga wave equation:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Bilis ng liwanag:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Mga Katangian ng EM Waves
| Ari-arian | Paglalarawan |
|----------|-------------|
| Nakahalang | Ang E at B ay patayo sa isa't isa at sa direksyon ng pagpapalaganap |
| Sa yugto | Ang E at B ay umaabot sa maxima nang sabay-sabay |
| Magnitude ratio | E = cB |
| Pagbabago ng enerhiya | S = (1/μ₀)**E** × **B** (Poynting vector) |
| Intensity | I = ⟨S⟩ = E₀²/(2μ₀c) |
### Ang Electromagnetic Spectrum
| Uri | Haba ng daluyong | Dalas | Pinagmulan |
|------|-----------|-----------|--------|
| Radyo | > 1 m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 EHz | Mga prosesong nuklear |
---

## Mga Circuit ng AC
### Mga Bahagi ng Circuit ng RLC
| Bahagi | Boltahe-Kasalukuyang Relasyon | Impedance |
|-----------|-----------------------|-----------|
| Resistor (R) | V = IR | Z_R = R |
| Inductor (L) | V = L(dI/dt) | Z_L = jωL |
| Capacitor (C) | I = C(dV/dt) | Z_C = 1/(jωC) |
### Impedance at Resonance
Kabuuang impedance (serye ng RLC): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Resonance:** Kapag ωL = 1/ωC → ω₀ = 1/√(LC)
- Sa resonance: ang impedance ay minimum (= R), ang kasalukuyang ay maximum
- **Salik ng kalidad:** Q = ω₀L/R (kataliman ng resonance)
### Power sa AC Circuits
| Dami | Formula |
|----------|---------|
| Average na kapangyarihan | P_avg = V_rms · I_rms · cos φ |
| Power factor | cos φ = R/\|Z\| |
| RMS boltahe | V_rms = V₀/√2 |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng EM | Application |
|-----------|-------------|
| Mga equation ni Maxwell | Mga neural network na may kaalaman sa pisika, computational electromagnetics |
| Wave equation | Signal processing foundation, Fourier analysis motivation |
| Electromagnetic spectrum | Data ng sensor (mga infrared camera, radar, satellite imagery) |
| AC circuits / impedance | Pag-unawa sa hardware na nagpapatakbo ng ML (mga power supply, integridad ng signal) |
| Poynting vector | Daloy ng enerhiya sa wireless na komunikasyon (nauugnay sa IoT/edge ML) |
| Batas ni Gauss | Katulad sa divergence sa vector calculus, ginagamit sa fluid dynamics simulation |
| Mga Capacitor/inductors | Analog computing para sa mga neural network, neuromorphic hardware |
| Resonance | Disenyo ng filter, pagsusuri ng frequency-domain, mga paraan ng parang multo |
| Mga problema sa hangganan ng halaga | May hangganan na mga pamamaraan ng elemento, mga simulation na nakabatay sa mesh |
| Vector calculus (∇·, ∇×) | Mahahalagang kasangkapang pangmatematika na ginagamit sa buong teorya ng ML |
---

## Buod
| Batas | Ang Sabi Nito | Differential Form |
|-----|-------------|--------------------|
| Gauss (electric) | Ang mga singil ay lumilikha ng electric field divergence | ∇ · E = ρ/ε₀ |
| Gauss (magnetic) | Walang magnetic monopole | ∇ · B = 0 |
| Faraday | Ang pagpapalit ng B ay lumilikha ng curling E | ∇ × E = −∂B/∂t |
| Ampere-Maxwell | Ang kasalukuyang at nagbabagong E ay lumilikha ng curling B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
Ang electromagnetism ay ang pinakakumpleto at mahusay na nasubok na pisikal na teorya na nagawa kailanman. Ang mga equation nito — apat lang — ay naglalarawan ng lahat mula sa static na kuryente hanggang sa ilaw hanggang sa pag-uugali ng bawat electronic device na nagawa. Para sa mga data scientist, ang pag-unawa sa electromagnetism ay nagbibigay ng malalim na intuition para sa wave phenomena, vector calculus, at ang physics na sumasailalim sa lahat ng modernong computing hardware.