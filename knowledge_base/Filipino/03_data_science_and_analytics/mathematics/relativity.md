---
# Metadata
title: "Relativity"
description: "Special relativity, Lorentz transformations, time dilation, length contraction, mass-energy equivalence, four-vectors, and introduction to general relativity"
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
    changes: "Initial deep-dive into relativity"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [relativity, special-relativity, general-relativity, lorentz-transformations, time-dilation, length-contraction, mass-energy, spacetime]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Relativity
Binago ng mga teorya ng relativity ni Einstein ang ating pag-unawa sa espasyo, oras, at grabidad. Ipinakita ng **Special relativity** (1905) na ang espasyo at oras ay hindi magkahiwalay ngunit hinabi sa iisang tela na tinatawag na spacetime, at ang bilis ng liwanag ay pareho para sa lahat ng mga nagmamasid. **General relativity** (1915) reimagined gravity hindi bilang isang puwersa kundi bilang ang curvature ng spacetime na dulot ng masa at enerhiya. Ang mga teoryang ito ay sumusuporta sa GPS navigation, particle accelerators, at ang ating pag-unawa sa mga black hole at sa ebolusyon ng uniberso.
---

## Mga Postula ng Espesyal na Relativity
Nagtayo si Einstein ng espesyal na relativity sa dalawang mapanlinlang na simpleng postulate:
| Postulate | Pahayag |
|-----------|-----------|
| **Principle of Relativity** | Ang mga batas ng pisika ay pareho sa lahat ng inertial (hindi nagpapabilis) na mga reference frame |
| **Katatagan ng c** | Ang bilis ng liwanag sa vacuum (c ≈ 3 × 10⁸ m/s) ay pareho para sa lahat ng mga nagmamasid, anuman ang kanilang galaw o galaw ng pinagmulan |
Ang dalawang postulate, pinagsama, ay nagbabalik sa mga siglo ng Newtonian intuition tungkol sa ganap na espasyo at oras.
---

## Mga Pagbabagong Lorentz
Ang **Lorentz transformations** ay nag-uugnay ng mga coordinate sa pagitan ng dalawang inertial frame na gumagalaw sa relatibong bilis v.
### Mga Equation ng Pagbabago
Para sa frame S' na gumagalaw sa bilis v kasama ang x-axis na may kaugnayan sa frame S:
| Dami | Pagbabagong-anyo |
|----------|----------------|
| x' | γ(x − vt) |
| t' | γ(t − vx/c²) |
| y' | y |
| z' | z |
kung saan γ (Lorentz factor) = 1/√(1 − v²/c²)
### Ang Lorentz Factor γ
| v/c | γ | Epekto |
|-----|---|--------|
| 0 | 1.0 | Walang relativistic effect (limitasyon ng Newtonian) |
| 0.1 | 1.005 | 0.5% pagwawasto |
| 0.5 | 1.155 | 15.5% pagwawasto |
| 0.9 | 2.294 | Makabuluhang pagluwang ng oras |
| 0.99 | 7.089 | Matinding epekto |
| 0.999 | 22.37 | Particle accelerator rehimen |
| → 1 | → ∞ | Imposible para sa malalaking bagay |
### Baliktad na Pagbabago
Upang pumunta mula sa S' pabalik sa S: palitan ang v ng −v.
---

## Pagluwang ng Oras
Mabagal ang paggalaw ng mga orasan.
Δt = γΔt₀
kung saan ang Δt₀ ay ang **tamang oras** (oras na sinusukat sa rest frame ng orasan).
**Nagtrabaho Halimbawa:** Isang muon na ginawa sa 10 km altitude ay bumibiyahe sa 0.998c. Ang rest-frame lifetime nito ay 2.2 μs.
- γ = 1/√(1 − 0.998²) ≈ 15.8
- Dilated lifetime: Δt = 15.8 × 2.2 μs = 34.8 μs
- Layo ng nilakbay: d = 0.998c × 34.8 μs ≈ 10.4 km
- Nang walang time dilation: d = 0.998c × 2.2 μs ≈ 0.66 km (hindi na makakarating sa lupa)
- **Reality:** Naabot ng mga muon ang ibabaw ng Earth — kinukumpirma ang paglawak ng oras sa eksperimentong paraan.
### Twin Paradox
Ang isang kambal ay naglalakbay nang napakabilis at bumalik. Mas bata sila sa stay-at-home twin. Hindi isang tunay na kabalintunaan — ang naglalakbay na kambal ay bumibilis (nagbabago ng mga inertial frame), sinisira ang simetrya.
---

## Haba ng Pag-urong
Ang mga gumagalaw na bagay ay pinaikli sa direksyon ng paggalaw.
L = L₀/γ
kung saan ang L₀ ay ang **wastong haba** (haba na sinusukat sa rest frame ng object).
| v/c | γ | Contraction factor L/L₀ |
|-----|---|----------------------|
| 0.5 | 1.15 | 87% |
| 0.9 | 2.29 | 44% |
| 0.99 | 7.09 | 14% |
| 0.999 | 22.4 | 4.5% |
**Mahalagang punto:** Ang pag-urong ng haba ay hindi isang optical illusion — ito ay isang tunay na pisikal na epekto na sinusukat ng mga nagmamasid sa relatibong paggalaw.
---

## Relativity ng Simultaneity
Ang mga kaganapan na sabay-sabay sa isang frame ay HINDI sabay-sabay sa isa pang frame na gumagalaw na may kaugnayan sa una.
**Ang eksperimento sa pag-iisip ng tren ni Einstein:** Tinamaan ng kidlat ang magkabilang dulo ng umaandar na tren. Ang isang tagamasid sa platform ay nakikita ang mga ito bilang sabay-sabay. Ang isang tagamasid sa tren (kumukilos patungo sa isang welga) ay unang nakikita ang front strike.
**Konklusyon:** Ang "Sabay-sabay" ay hindi ganap — depende ito sa frame of reference ng observer.
---

## Pagdaragdag ng Bilis
Ang mga bilis ay hindi lamang nagdaragdag sa espesyal na relativity.
### Relativistic Velocity Addition
Kung ang isang bagay ay gumagalaw sa bilis na u' sa frame S', at ang S' ay gumagalaw sa bilis v na may kaugnayan sa S:
u = (u' + v) / (1 + u'v/c²)
| Sitwasyon | Resulta |
|----------|--------|
| u' = c (liwanag) | u = c (pabagu-bago ang bilis ng liwanag) |
| u', v ≪ c | u ≈ u' + v (binabawasan sa karagdagan sa Galilea) |
| u' = 0.9c, v = 0.9c | u = 0.9945c (hindi kailanman lalampas sa c) |
---

## Mass-Energy Equivalence
E = mc²
| Konsepto | Formula | Ibig sabihin |
|---------|---------|---------|
| Lakas ng pahinga | E₀ = mc² | Enerhiya ng isang masa sa pamamahinga |
| Kabuuang enerhiya | E = γmc² | May kasamang kinetic energy |
| Kinetic energy | KE = (γ − 1)mc² | Bumababa sa ½mv² para sa v ≪ c |
| Momentum-enerhiya | E² = (pc)² + (mc²)² | Relativistic energy-momentum relation |
| Mga particle na walang masa | E = pc | Ang mga photon ay may enerhiya at momentum ngunit walang rest mass |
### Mga Halimbawa ng Nuclear Energy
| Reaksyon | Mass Depekto | Inilabas ang Enerhiya |
|----------|-------------|----------------|
| U-235 fission | 0.1% ng masa | ~200 MeV bawat fission |
| D-T fusion | 0.7% ng masa | 17.6 MeV bawat reaksyon |
| Matter-antimatter | 100% ng masa | 2mc² (kumpletong conversion) |
---

## Apat na Vector at Spacetime
### Minkowski Spacetime
Pinagsasama ng espesyal na relativity ang espasyo at oras sa 4D **Minkowski spacetime** na may mga coordinate (ct, x, y, z).
### Ang Spacetime Interval
ds² = −c²dt² + dx² + dy² + dz²
| Uri ng Pagitan | Kundisyon | Ibig sabihin |
|--------------|-----------|---------|
| **Timelike** | ds²< 0 | Events can be causally connected |
| **Lightlike (null)** | ds² = 0 | Connected by a light signal |
| **Spacelike** | ds² >0 | Ang mga kaganapan ay hindi makakaimpluwensya sa isa't isa |
Ang pagitan ng spacetime ay **invariant** — lahat ng nagmamasid ay sumasang-ayon sa halaga nito.
### Apat na Vector
| Apat na Vector | Mga Bahagi | Pabago-bagong Dami |
|-------------|-----------|-------------------|
| Posisyon | (ct, x, y, z) | pagitan ng spacetime |
| Bilis | γ(c, vₓ, vᵧ, v_z) | Tamang oras |
| Momentum | (E/c, pₓ, pᵧ, p_z) | Mass ng pahinga: m²c² = E²/c² − p² |
| Puwersa | dP/dτ | Wastong acceleration |
---

## Panimula sa General Relativity
### Ang Equivalence Principle
| Bersyon | Pahayag |
|---------|------------|
| **Mahina** | Gravitational mass = inertial mass (lahat ng bagay ay bumabagsak sa parehong bilis) |
| **Einstein** | Ang isang pare-parehong accelerating na frame ay lokal na hindi makilala sa isang gravitational field |
| **Malakas** | Ang lahat ng pisikal na batas (hindi lamang mekanika) ay lokal na pareho sa isang malayang bumabagsak na frame |
### Gravity bilang Curved Spacetime
Pangkalahatang relativity ng sentral na ideya: mass at energy curve spacetime, at ang mga bagay ay sumusunod sa mga posibleng tuwid na landas (geodesics) sa pamamagitan ng curved spacetime.
**Einstein field equation:**
G_μν + Λg_μν = (8πG/c⁴) T_μν
| Simbolo | Ibig sabihin |
|--------|---------|
| G_μν | Einstein tensor (nag-encode ng spacetime curvature) |
| Λ | Cosmological constant (dark energy) |
| g_μν | Metric tensor (naglalarawan ng geometry ng spacetime) |
| G | Gravitational constant ni Newton |
| T_μν | Stress-energy tensor (nilalaman ng bagay at enerhiya) |
**Buod ni John Wheeler:** "Spacetime ay nagsasabi sa bagay kung paano lumipat; ang matter ay nagsasabi sa spacetime kung paano mag-curve."
### Mga Hula ng General Relativity
| Hula | Paglalarawan | Nakumpirma? |
|-----------|-------------|------------|
| Gravitational time dilation | Ang mga orasan ay tumatakbo nang mas mabagal sa mas malakas na mga patlang ng gravitational | Oo (nangangailangan ng pagwawasto ang GPS) |
| Gravitational lensing | Ang liwanag ay yumuko sa mga malalaking bagay | Oo (Eddington 1919, Hubble images) |
| Gravitational redshift | Nawawalan ng enerhiya ang liwanag sa pag-akyat sa mga balon ng gravity | Oo (Pound-Rebka 1959) |
| Black hole | Mga rehiyon kung saan pinipigilan ng spacetime curvature ang liwanag na makatakas | Oo (LIGO, EHT 2019) |
| Gravitational waves | Ripples sa spacetime mula sa accelerating masa | Oo (LIGO 2015) |
| Ang precession ng perihelion ng Mercury | Dagdag na 43 arcsecond bawat siglo | Oo (ipinaliwanag ang anomalya mula noong 1859) |
| Pag-drag ng frame | Ang mga umiikot na masa ay nagha-drag ng spacetime sa paligid nila | Oo (Gravity Probe B 2011) |
### Schwarzschild Sukatan
Ang pinakasimpleng solusyon sa black hole (hindi umiikot, walang bayad):
ds² = −(1 − 2GM/rc²)c²dt² + (1 − 2GM/rc²)⁻¹dr² + r²dΩ²
**Schwarzschild radius:** r_s = 2GM/c²
| Bagay | Misa | r_s |
|--------|------|-----|
| Lupa | 6 × 10²⁴ kg | 9 mm |
| Araw | 2 × 10³⁰ kg | 3 km |
| Sgr A* (Milky Way center) | 4 × 10⁶ M☉ | 12 milyong km |
---

## Kaugnayan sa Machine Learning at Data Science
| Relativity Concept | Application |
|-------------------|-------------|
| Mga pagbabago sa Lorentz | Lorentz-equivariant neural network, symmetry-aware na mga modelo |
| Spacetime geometry | Geometric deep learning, manifold learning |
| Apat na vector | Tensor notation na ginagamit sa relativistic physics simulation |
| Gravitational time dilation | Mga pagwawasto ng GPS (mga serbisyong nakabatay sa lokasyon, geospatial ML) |
| Gravitational lensing | Astronomical data analysis, dark matter mapping |
| Pangkalahatang relativity | Physics-informed neural network para sa gravitational wave detection |
| Riemannian geometry | Natural gradient descent (information geometry), manifold optimization |
| Sukatan tensor | Tinutukoy ang mga distansya sa mga curved space — pangunahing sa manifold learning |
| Geodesics | Pinakamaikling landas sa mga manifold — ginagamit sa robotics, pag-embed ng graph |
| Tensor calculus | Foundation para sa pag-unawa sa mga high-dimensional na data manifold |
---

## Buod
| Konsepto | Pangunahing Ideya | Key Equation |
|---------|-----------|-------------|
| Espesyal na relativity | Ang espasyo at oras ay pinag-isa; c ay ganap | Mga pagbabago sa Lorentz |
| Pagluwang ng oras | Mabagal ang paggalaw ng mga orasan | Δt = γΔt₀ |
| Haba ng contraction | Ang mga gumagalaw na bagay ay nagpapaikli | L = L₀/γ |
| Mass-energy | Ang masa at enerhiya ay katumbas | E = mc² |
| Apat na vector | Pinag-isang mga paglalarawan ng spacetime | Invariant interval ds² |
| Prinsipyo ng equivalence | Gravity = acceleration locally | Pundasyon ng GR |
| Pangkalahatang relativity | Ang gravity ay curved spacetime | G_μν = (8πG/c⁴)T_μν |
| Geodesics | Ang mga bagay ay sumusunod sa mga tuwid na landas sa curved spacetime | Pinakamaikling landas sa manifold |
Binago ng relativity ang ating pag-unawa sa mga pinakapangunahing aspeto ng realidad — espasyo, oras, masa, enerhiya, at gravity. Ang mga mathematical tool nito — tensors, manifolds, geodesics, metric spaces — ay lumipat nang higit pa sa physics tungo sa machine learning, kung saan pinapagana nila ang geometric deep learning, natural gradient method, at iba't ibang algorithm ng pag-aaral.