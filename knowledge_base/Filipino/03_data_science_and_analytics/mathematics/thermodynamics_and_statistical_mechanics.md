---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Thermodynamics at Statistical Mechanics
Inilalarawan ng Thermodynamics ang macroscopic na pag-uugali ng mga system sa mga tuntunin ng temperatura, presyon, at entropy — nang hindi nalalaman kung ano ang hitsura ng mga atomo. Ipinapaliwanag ng statistic mechanics ang thermodynamics mula sa ibaba pataas: nakukuha nito ang mga macroscopic na katangian mula sa microscopic na pag-uugali ng napakaraming particle. Magkasama, nagbibigay sila ng pinakamalalim na pag-unawa sa enerhiya, entropy, at equilibrium — mga konsepto na lumipat sa teorya ng impormasyon, machine learning, at higit pa.
---

## Thermodynamic Variable at Estado
### Mga Variable ng Estado
| Variable | Uri | Yunit | Paglalarawan |
|----------|------|------|-------------|
| Temperatura (T) | Intensive | Kelvin (K) | Average na kinetic energy bawat particle |
| Presyon (P) | Intensive | Pascal (Pa) | Puwersa bawat unit area |
| Dami (V) | Malawak | m³ | Sinakop ang espasyo |
| Panloob na enerhiya (U) | Malawak | Joule (J) | Kabuuang mikroskopikong enerhiya |
| Entropy (S) | Malawak | J/K | Pagsukat ng kaguluhan/microstates |
| Bilang ng mga particle (N) | Malawak | mga nunal o bilang | Dami ng substance |
Ang **Intensive** na mga variable ay hindi nakadepende sa laki ng system; **malawak** ang mga variable.
### Equation ng Estado
Para sa perpektong gas: PV = nRT = Nk_BT
| pare-pareho | Halaga |
|----------|-------|
| R (gas constant) | 8.314 J/(mol·K) |
| k_B (Boltzmann constant) | 1.381 × 10⁻²³ J/K |
| N_A (numero ni Avogadro) | 6.022 × 10²³ /mol |
---

## Ang Mga Batas ng Thermodynamics
### Zeroth Law
Kung ang A ay nasa thermal equilibrium kasama ang B, at ang B na may C, kung gayon ang A ay nasa thermal equilibrium na may C.
**Kahulugan:** Ang temperatura ay mahusay na tinukoy at nasusukat.
### Unang Batas (Pagtitipid ng Enerhiya)
ΔU = Q − W
| Simbolo | Ibig sabihin |
|--------|---------|
| ΔU | Pagbabago sa panloob na enerhiya |
| Q | Idinagdag ang init sa system |
| W | Gawaing ginawa ng system |
**Differential form:** dU = δQ − δW = δQ − PdV
| Proseso | Paghadlang | Bunga |
|---------|-----------|-------------|
| Isochoric | dV = 0 | W = 0, ΔU = Q |
| Isobaric | dP = 0 | W = PΔV |
| Isothermal | dT = 0 | ΔU = 0 (ideal na gas), Q = W |
| Adiabatic | δQ = 0 | ΔU = −W |
### Pangalawang Batas (Entropy)
**Pahayag ni Clausius:** Ang init ay hindi maaaring kusang dumaloy mula sa malamig hanggang sa mainit.
**Salaysay ng Kelvin-Planck:** Walang makina ang maaaring gawing trabaho ang lahat ng init.
**Entropy statement:** Para sa anumang proseso: ΔS_universe ≥ 0
| Uri ng proseso | ΔS_universe |
|-------------|-------------|
| Nababaligtad | = 0 |
| Hindi maibabalik (totoo) | > 0 |
**Pagbabago sa entropy:** dS = δQ_rev / T
### Ikatlong Batas
Habang T → 0 K, ang entropy ng perpektong kristal ay lumalapit sa zero: lim_{T→0} S = 0
**Kahulugan:** Ang absolute zero ay hindi makakamit sa mga may hangganang hakbang.
---

## Entropy sa Lalim
### Thermodynamic Entropy
Ang S ay isang function ng estado. Para sa isang nababalikang proseso sa pagitan ng mga estado A at B:
ΔS = ∫_A^B δQ_rev / T
**Nagtrabaho Halimbawa:** Nagbabago ang entropy kapag nag-iinit ng tubig mula T₁ hanggang T₂ sa pare-parehong presyon.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Statistical Entropy (Boltzmann)
S = k_B ln Ω
kung saan ang Ω ay ang bilang ng mga microstate na pare-pareho sa macrostate.
| Macrostate | Mga Microstate (Ω) | Entropy |
|-----------|-----------------|---------|
| Lahat ng gas sa isang kalahati ng kahon | Maliit | Mababa |
| Pantay na ipinamahagi ang gas | Napakalaki | Mataas |
| Perpektong kristal sa 0 K | 1 | 0 |
**Koneksyon:** Nagiging istatistika ang pangalawang batas — ang mga system ay umuusbong patungo sa mga macrostate na may mas maraming microstate dahil lang sa napakalaking posibilidad ng mga ito.
---

## Enthalpy at Libreng Enerhiya
### Enthalpy
H = U + PV
Kapaki-pakinabang para sa mga proseso sa palaging presyon (karamihan sa kimika at biology).
ΔH = Q_p (init sa pare-parehong presyon)
### Libreng Enerhiya ng Helmholtz
F = U − TS
| Ari-arian | Pahayag |
|----------|-----------|
| Ibig sabihin | Pinakamataas na trabaho na maaaring makuha sa pare-parehong T, V |
| Ekwilibriyo | Binabawasan ng system ang F sa pare-parehong T, V |
| Kaugnayan sa partition function | F = −k_BT ln Z |
### Libreng Enerhiya ng Gibbs
G = H − TS = U + PV − TS
| Ari-arian | Pahayag |
|----------|-----------|
| Ibig sabihin | Pinakamataas na hindi pagpapalawak na trabaho sa pare-parehong T, P |
| Ekwilibriyo | Binabawasan ng system ang G sa pare-parehong T, P |
| Spontanity | ΔG < 0 → kusang-loob; ΔG = 0 → ekwilibriyo |
| Mga reaksiyong kemikal | Tinutukoy ng ΔG = ΔH − TΔS ang direksyon |
### Buod ng Thermodynamic Potentials
| Potensyal | Mga Natural na Variable | Pagkakaiba | Pinaliit Kapag |
|------------|--------------------|-------------|----------------|
| U (panloob na enerhiya) | S, V | dU = TdS − PdV | Nakahiwalay na sistema |
| H (enthalpy) | S, P | dH = TdS + VdP | Constant P, adiabatic |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Constant T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Constant T, P |
---

## Ang Ikot ng Carnot
Ang **Carnot cycle** ay ang pinakamabisang heat engine na posible, na tumatakbo sa pagitan ng mga temperaturang T_H (mainit) at T_C (malamig).
### Apat na Yugto
| Yugto | Proseso | Ano ang Mangyayari |
|-------|---------|-------------|
| 1 → 2 | Isothermal expansion | Sipsipin ang init Q_H mula sa mainit na reservoir sa T_H |
| 2 → 3 | Adiabatic expansion | Lumalamig ang gas mula T_H hanggang T_C |
| 3 → 4 | Isothermal compression | Tanggihan ang init Q_C sa malamig na reservoir sa T_C |
| 4 → 1 | Adiabatic compression | Umiinit ang gas mula T_C hanggang T_H |
### Carnot Efficiency
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500 K | 300 K | 40% |
| 1000 K | 300 K | 70% |
| 300 K | 299 K | 0.33% |
**Walang tunay na makina ang maaaring lumampas sa kahusayan ng Carnot.** Ang mga tunay na makina ay palaging hindi maibabalik (friction, turbulence, may hangganang pagkakaiba sa temperatura).
---

## Mekanika ng Istatistika
### Ang Boltzmann Distribution
Para sa isang sistema sa thermal equilibrium sa temperatura T, ang posibilidad na nasa isang microstate na may enerhiya E_i:
P(E_i) = (1/Z) e^{−E_i / k_BT}
kung saan ang Z ay ang **partition function**:
Z = Σᵢ e^{−E_i / k_BT}
### Ang Partition Function
Ini-encode ng Z ang lahat ng thermodynamic na impormasyon tungkol sa system.
| Dami | Formula |
|----------|---------|
| Helmholtz libreng enerhiya | F = −k_BT ln Z |
| Average na enerhiya | ⟨E⟩ = −∂(ln Z)/∂β kung saan β = 1/(k_BT) |
| Entropy | S = k_B(ln Z + β⟨E⟩) |
| Kapasidad ng init | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Presyon | P = (1/β) ∂(ln Z)/∂V |
### Nagtrabaho Halimbawa: Two-State System
Ang isang particle ay maaaring nasa state 0 (energy 0) o state 1 (energy ε).
Z = 1 + e^{−βε}
| Dami | Resulta |
|----------|--------|
| P(estado 0) | 1/(1 + e^{−βε}) |
| P(estado 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Mataas na limitasyon sa T (β→0) | ⟨E⟩ → ε/2 (pantay na posibilidad) |
| Mababang limitasyon sa T (β→∞) | ⟨E⟩ → 0 (ground state) |
### Equipartition Theorem
Ang bawat parisukat na antas ng kalayaan ay nag-aambag ng ½k_BT sa average na enerhiya.
| System | Mga Degree ng Kalayaan | ⟨E⟩ |
|--------|--------------------|------|
| Monatomic gas (Siya) | 3 pagsasalin | (3/2)k_BT |
| Diatomic gas (N₂) sa silid T | 3 trans + 2 mabulok | (5/2)k_BT |
| Diatomic gas sa mataas na T | 3 trans + 2 mabulok + 1 vib | (7/2)k_BT |
| Solid (modelo ng Einstein) | 3 vibrational (bawat atom) | 3k_BT |
---

## Koneksyon sa Teorya ng Impormasyon
### Shannon Entropy vs Thermodynamic Entropy
| Aspeto | Shannon Entropy H(X) | Thermodynamic Entropy S |
|--------|---------------------|----------------------|
| Kahulugan | −Σ pᵢ log pᵢ | k_B ln Ω (o −k_B Σ pᵢ ln pᵢ) |
| Maximum kapag | Unipormeng pamamahagi | Thermal equilibrium |
| Mga Panukala | Kawalang-katiyakan / nilalaman ng impormasyon | Bilang ng mga naa-access na microstate |
| Mga Yunit | Bits o nats | J/K |
**Gibbs entropy formula:** S = −k_B Σᵢ pᵢ ln pᵢ (kapareho ng anyo sa Shannon entropy)
### Pinakamataas na Prinsipyo ng Entropy
Ang parehong mga patlang ay gumagamit ng parehong prinsipyo: ang pamamahagi na pinakamahusay na kumakatawan sa aming estado ng kaalaman ay ang isa na nagpapalaki ng entropy na napapailalim sa mga kilalang hadlang.
| Paghadlang | Nagreresultang Pamamahagi |
|------------|----------------------|
| Kilalang ibig sabihin | Exponential distribution |
| Kilalang ibig sabihin at pagkakaiba | Gaussian distribution |
| Kilalang enerhiya ⟨E⟩ | Pamamahagi ng Boltzmann |
| Walang mga hadlang | Unipormeng pamamahagi |
### Prinsipyo ng Landauer
Ang pagbura ng isang piraso ng impormasyon ay nakakawala ng hindi bababa sa k_BT ln 2 ng enerhiya bilang init. Ikinokonekta nito ang pagpoproseso ng impormasyon nang direkta sa thermodynamics - ang pagkalkula ay may pangunahing halaga ng enerhiya.
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Thermo/StatMech | Application |
|------------------------|-------------|
| Pamamahagi ng Boltzmann | Softmax function, mga modelong nakabatay sa enerhiya, kunwa ng pagsusubo |
| Pag-andar ng partisyon | Pag-normalize ng pare-pareho sa mga probabilistikong modelo, hindi maaalis sa pangkalahatan |
| Libreng enerhiya | Variational inference (minimising variational free energy = minimizing KL divergence) |
| Entropy | Regularisasyon, paggalugad sa RL (maximum entropy RL), mga puno ng desisyon |
| Pinakamataas na prinsipyo ng entropy | MaxEnt classifier, naunang pagpili, pagtatantya ng pamamahagi |
| Simulated pagsusubo | Global optimization sa pamamagitan ng unti-unting pagbabawas ng "temperatura" |
| Mekanika ng istatistika | Pag-unawa sa mga phase transition sa pag-aaral (grokking, double descent) |
| Equipartition | Pag-unawa sa pamamahagi ng enerhiya sa mga pisikal na simulation |
| Prinsipyo ng Landauer | Mga pangunahing limitasyon ng pag-compute, reversible computing |
| Gibbs sampling | Ang pamamaraan ng MCMC ay direktang inspirasyon ng mga istatistikal na mekanika |
| Temperatura (sa softmax) | Kinokontrol ang randomness ng mga hula: P(i) ∝ exp(z_i/T) |
---

## Buod
| Batas/Konsepto | Pangunahing Ideya | Formula |
|------------|-----------|---------|
| Zeroth batas | Ang temperatura ay mahusay na tinukoy | Transitivity ng thermal equilibrium |
| Unang batas | Ang enerhiya ay natipid | ΔU = Q − W |
| Pangalawang batas | Tumataas ang entropy ng uniberso | ΔS ≥ 0 |
| Ikatlong batas | Ang ganap na zero ay hindi matamo | S → 0 bilang T → 0 |
| Boltzmann entropy | Ang entropy ay nagbibilang ng mga microstate | S = k_B ln Ω |
| Pamamahagi ng Boltzmann | Probability ng mga estado ng enerhiya | P ∝ e^{−E/k_BT} |
| Pag-andar ng partisyon | Ine-encode ang lahat ng termodinamikong impormasyon | Z = Σ e^{−E_i/k_BT} |
| Libreng enerhiya | Magagamit na kapaki-pakinabang na trabaho | F = U − TS, G = H − TS |
| Carnot na kahusayan | Pinakamataas na kahusayan ng makina ng init | η = 1 − T_C/T_H |
Thermodynamics at statistical mechanics ay kung saan ang pisika ay nakakatugon sa teorya ng impormasyon. Ang parehong entropy na namamahala sa mga heat engine ay namamahala sa compression ng data. Ang parehong pamamahagi ng Boltzmann na naglalarawan sa mga molekula ng gas ay nagpapagana sa softmax layer sa bawat classifier. Ang pag-unawa sa mga koneksyon na ito ay nagbibigay sa iyo ng pinag-isang pagtingin sa physics, probabilidad, at machine learning.