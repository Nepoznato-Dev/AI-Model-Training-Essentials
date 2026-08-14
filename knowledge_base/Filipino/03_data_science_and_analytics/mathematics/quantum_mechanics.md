---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Quantum Mechanics
Ang quantum mechanics ay ang teorya ng physics sa pinakamaliit na sukat - mga atom, electron, photon, at ang mga pangunahing particle ng kalikasan. Pinapalitan nito ang deterministikong mundo ng klasikal na mekanika ng mga probabilities, superpositions, at entanglement. Sa kabila ng pagiging counterintuitive nito, ang quantum mechanics ay ang pinakatumpak na nasubok na teorya sa lahat ng agham. Ngayon, ang mga prinsipyo nito ay nagiging direktang nauugnay sa pag-compute sa pamamagitan ng mga quantum computer, na nangangako na malutas ang ilang mga problema nang mas mabilis kaysa sa mga klasikal na makina.
---

## Makasaysayang Pagganyak
### Mga Pagkabigo ng Classical Physics
| Problema | Klasikal na Hula | Pagmamasid | Resolusyon |
|---------|---------------------|-------------|-----------|
| Radiation ng itim na katawan | Ultraviolet catastrophe (walang katapusang enerhiya sa maikling λ) | May hangganan ang peak wavelength | Planck: ang enerhiya ay binibilang (E = nhν) |
| Photoelectric effect | Ang KE ay nakasalalay sa intensity, hindi frequency | Ang KE ay nakasalalay sa dalas | Einstein: binibilang ang liwanag (photon, E = hν) |
| Atomic spectra | Patuloy na emission spectrum | Mga discrete spectral na linya | Bohr: ang mga electron ay sumasakop sa mga quantised orbit |
| Electron diffraction | Hindi nagdi-diffract ang mga particle | Ang mga electron ay gumagawa ng mga pattern ng interference | de Broglie: ang mga particle ay may wavelength λ = h/p |
### Mga Key Constant
| pare-pareho | Simbolo | Halaga |
|----------|--------|-------|
| Ang pare-pareho ni Planck | h | 6.626 × 10⁻³⁴ J·s |
| Binawasan ang pare-pareho ng Planck | ℏ = h/2π | 1.055 × 10⁻³⁴ J·s |
| Bilis ng liwanag | c | 3.0 × 10⁸ m/s |
| Electron mass | m_e | 9.109 × 10⁻³¹ kg |
| singilin sa elementarya | e | 1.602 × 10⁻¹⁹ C |
| Bohr radius | isang₀ | 5.292 × 10⁻¹¹ m |
---

## Wave-Particle Duality
### de Broglie Wavelength
Ang bawat particle na may momentum p ay may nauugnay na wavelength:
λ = h/p = h/(mv)
| Particle | Karaniwang λ | Napapansing Pag-uugali ng Alon? |
|----------|-----------|-------------|
| Electron (100 eV) | 0.12 nm | Oo (crystal diffraction) |
| Proton | 0.003 nm | Oo (neutron scattering) |
| Baseball (40 m/s) | 10⁻³⁴ m | Hindi (napakaliit para makita) |
### Double-Slit na Eksperimento
Ang quintessential quantum experiment:
1. Mga particle ng apoy (mga electron, photon) nang paisa-isa sa dalawang hiwa
2. Ang bawat particle ay dumarating sa isang punto sa detector
3. Sa paglipas ng panahon, lumilitaw ang isang pattern ng interference — na para bang ang bawat particle ay dumaan sa magkabilang hiwa nang sabay-sabay
4. Kung susukatin mo kung aling hiwa ang dumaan sa particle, mawawala ang interference pattern
**Konklusyon:** Ang mga bagay na kuwantum ay hindi purong mga particle o purong alon. Nagpapakita ang mga ito ng pag-uugaling parang alon kapag hindi napagmamasdan at pag-uugaling parang butil kapag sinusukat.
---

## Ang Wavefunction
### Depinisyon
Ang **wavefunction** ψ(x, t) ay ganap na naglalarawan ng isang quantum system. Ito ay isang complex-valued function na ang squared modulus ay nagbibigay ng probability density:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalisasyon
Ang kabuuang posibilidad ay dapat katumbas ng 1:
∫ |ψ(x)|² dx = 1 (sa lahat ng espasyo)
### Ipinanganak na Panuntunan
Ang posibilidad ng paghahanap ng particle sa pagitan ng x at x + dx:
P(x hanggang x+dx) = |ψ(x)|² dx
Para sa isang pangkalahatang nakikita na may eigenstates φₙ:
P(pagsusukat ng eigenvalue aₙ) = |⟨φₙ|ψ⟩|²
---

## Ang Schrodinger Equation
### Time-Dependant Schrodinger Equation
iℏ ∂ψ/∂t = Ĥψ
kung saan ang Ĥ ay ang **Hamiltonian operator** (total energy operator).
### Time-Independent Schrodinger Equation
Para sa mga nakatigil na estado (energy eigenstates):
Ĥψ = Eψ
Ito ay isang equation ng eigenvalue: ang pinapayagang mga energies E ay ang mga eigenvalues ​​ng Ĥ.
### Particle sa isang Kahon (Infinite Square Well)
Ang pinakasimpleng quantum system: particle na nakakulong sa 0 < x < L.
| Dami | Resulta |
|----------|--------|
| Mga wavefunction | ψₙ(x) = √(2/L) sin(nπx/L) |
| Mga antas ng enerhiya | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Ground state | n = 1, E₁ = h²/(8mL²) |
| Zero-point na enerhiya | E₁ > 0 (ang particle ay hindi maaaring ganap na patahimik) |
| Quantum number | n = 1, 2, 3, ... (positive integers lang) |
### Quantum Harmonic Oscillator
V(x) = ½mω²x²
| Dami | Resulta |
|----------|--------|
| Mga antas ng enerhiya | Eₙ = (n + ½)ℏω |
| Zero-point na enerhiya | E₀ = ½ℏω |
| Spacing | ΔE = ℏω (uniporme) |
| Mga wavefunction | Hermite polynomial × Gaussian |
---

## Operator at Obserbasyon
Sa quantum mechanics, ang bawat pisikal na nakikita ay tumutugma sa isang **Hermitian operator**.
### Mga Pangunahing Operator
| Mapapansin | Operator (puwang sa posisyon) | Eigenvalues ​​|
|-----------|------------------------|-------------|
| Posisyon | x̂ = x | Lahat ng tunay na x |
| Momentum | p̂ = −iℏ ∂/∂x | Lahat ng tunay na p |
| Enerhiya (Hamiltonian) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (discrete para sa bound states) |
| Angular na momentum | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Paikutin | Ŝ = (ℏ/2)σ (Pauli matrices) | ±ℏ/2 (para sa spin-½) |
### Mga Halaga ng Inaasahan
Ang average na resulta ng pagsukat ng nakikitang A sa estado ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Commutation Relations
[Â, B̂] = ÂB̂ − B̂Â
| Commutator | Resulta | Kahalagahan |
|-----------|--------|-------------|
| [x̂, p̂] | iℏ | Ang posisyon at momentum ay hindi magkatugma |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Ang mga bahagi ng angular momentum ay hindi tugma |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Pauli matrices (spin component) |
Kung [Â, B̂] = 0, ang mga observable ay maaaring masukat nang sabay-sabay (magbahagi ng eigenstates).
---

## Prinsipyo ng Kawalang-katiyakan
### Prinsipyo ng Kawalang-katiyakan ng Heisenberg
Δx · Δp ≥ ℏ/2
Sa pangkalahatan, para sa alinmang dalawang naoobserbahang A at B:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Uncertainty Relations
| Pares | Relasyon | Interpretasyon |
|------|----------|----------------|
| Posisyon-momentum | ΔxΔp ≥ ℏ/2 | Hindi maaaring malaman ang parehong eksaktong |
| Enerhiya-oras | ΔEΔt ≥ ℏ/2 | Ang mga panandaliang estado ay may hindi tiyak na enerhiya |
| Angular na momentum | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Hindi maaaring malaman ang lahat ng mga bahagi nang sabay-sabay |
**Mahalaga:** Ang kawalan ng katiyakan ay hindi tungkol sa kaguluhan sa pagsukat — isa itong pangunahing katangian ng mga quantum state. Ang isang particle ay walang tiyak na posisyon at momentum nang sabay-sabay.
---

## Quantum States at Superposition
### Dirac Notation (Bra-Ket)
| Simbolo | Pangalan | Ibig sabihin |
|--------|------|---------|
| \|ψ⟩ | Ket | Vector ng estado (vector ng column) |
| ⟨ψ\| | Bra | Conjugate transpose (row vector) |
| ⟨φ\|ψ⟩ | Panloob na produkto | Amplitude para sa ψ na matatagpuan sa estado φ |
| \|ψ\|² | Norm squared | Probability |
### Prinsipyo ng Superposisyon
Kung ang \|ψ₁⟩ at \|ψ₂⟩ ay valid na quantum states, ang anumang linear na kumbinasyon ay valid din:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

kung saan |α|² + |β|² = 1 (normalisasyon).
**Pagsukat:** Kapag sinusukat, ang system ay "mag-collapse" sa \|ψ₁⟩ na may probabilidad |α|² o \|ψ₂⟩ na may probabilidad |β|².
### Qubits
Ang **qubit** ay isang quantum bit: isang dalawang antas na quantum system.
\|ψ⟩ = α\|0⟩ + β\|1⟩, kung saan |α|² + |β|² = 1
| Kinatawan | \|0⟩ | \|1⟩ |
|--------------|------|------|
| Paikutin | Paikutin ↑ | Paikutin pababa ↓ |
| Polarisasyon ng photon | Pahalang | Patayo |
| Antas ng enerhiya | Ground state | Nasasabik na estado |
| Circuit | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Bloch sphere:** Ang anumang qubit state ay maaaring isulat bilang:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
kung saan θ ∈ [0, π] at φ ∈ [0, 2π). Ang espasyo ng estado ay isang globo.
---

## Pagkasalimuot
Dalawang qubit ang **nakakabit** kapag ang kanilang pinagsamang estado ay hindi maaaring isulat bilang isang produkto ng mga indibidwal na estado.
### Bell States (Maximally Entangled)
| Estado | Pagpapahayag | Pangalan |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Estado ng kampana |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Estado ng kampana |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Estado ng kampana |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Singlet state |
### Mga Katangian ng Pagkagambala
| Ari-arian | Paglalarawan |
|----------|-------------|
| Kaugnayan | Ang pagsukat ng isang qubit ay agad na tumutukoy sa isa pa, anuman ang distansya |
| Walang komunikasyon | Hindi maaaring gumamit ng entanglement nang mag-isa upang magpadala ng impormasyon nang mas mabilis kaysa sa liwanag |
| Monogamy | Kung ang A ay lubos na nakasalikop sa B, hindi ito maaaring makasali sa C |
| Fragility | Ang pakikipag-ugnayan sa kapaligiran ay sumisira sa gusot (decoherence) |
### EPR Paradox at Bell's Theorem
Nagtalo sina Einstein, Podolsky, at Rosen na ang quantum mechanics ay dapat na hindi kumpleto (mga nakatagong variable). Ipinakita ni Bell na ang anumang lokal na nakatagong teorya ng variable ay nakakatugon sa ilang mga hindi pagkakapantay-pantay. Ang mga eksperimento ay lumalabag sa hindi pagkakapantay-pantay ng Bell — pagkumpirma ng quantum mechanics at pag-alis ng mga lokal na nakatagong variable.
---

## Quantum Gates
Ang mga quantum gate ay mga unitary operation sa mga qubit.
### Single-Qubit Gates
| Gate | Matrix | Epekto |
|------|--------|--------|
| **Pauli-X** (HINDI) | [[0,1],[1,0]] | Bit flip: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + phase flip |
| **Pauli-Z** | [[1,0],[0,−1]] | Phase flip: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Lumilikha ng superposisyon: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Phase** (S) | [[1,0],[0,i]] | π/2 pag-ikot sa paligid ng Z |
| **T gate** | [[1,0],[0,e^{iπ/4}]] | π/4 pag-ikot sa paligid ng Z |
| **Pag-ikot** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | Pag-ikot ng θ sa paligid ng X axis |
### Dalawang-Qubit Gate
| Gate | Paglalarawan | Epekto |
|------|-------------|--------|
| **CNOT** | Kinokontrol-HINDI | I-flip ang target kung ang kontrol ay \|1⟩ |
| **CZ** | Kinokontrol-Z | Inilapat ang Z sa target kung ang kontrol ay \|1⟩ |
| **SWAP** | Palitan ng mga qubit | \|ab⟩ → \|ba⟩ |
### Lumilikha ng Entanglement
Ilapat ang H sa qubit 1, pagkatapos ay CNOT na may qubit 1 bilang kontrol:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Quantum Algorithms
| Algorithm | Bilis | Application |
|-----------|---------|-------------|
| **Shor's** | Exponential (factoring) | Sinisira ang RSA encryption |
| **Grover's** | Quadratic (paghahanap) | Hindi nakabalangkas na paghahanap sa O(√N) |
| **VQE** | Heuristic | Paghahanap ng ground state energies (chemistry, materials) |
| **QAOA** | Heuristic | Kombinatoryal na pag-optimize |
| **HHL** | Exponential (sa ilalim ng mga kundisyon) | Paglutas ng mga linear system |
| **Quantum simulation** | Exponential | Simulating quantum system (orihinal na motibasyon ni Feynman) |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Quantum | Application |
|----------------|------------|
| Qubits at superposisyon | Quantum machine learning, quantum-enhanced sampling |
| Pagkagambala | Quantum communication, quantum key distribution (QKD) |
| Quantum gates | Quantum circuit na disenyo para sa mga subroutine ng ML |
| Algorithm ni Grover | Quadratic speedup para sa pag-optimize na nakabatay sa paghahanap |
| Algorithm ni Shor | Banta sa kasalukuyang cryptography; nag-uudyok sa post-quantum crypto |
| Quantum simulation | Pagtuklas ng droga, agham ng materyales, simulation ng kimika |
| Variational algorithm (VQE, QAOA) | Near-term quantum ML sa mga NISQ device |
| Ipinanganak na panuntunan | Mga probabilistikong kinalabasan na kahalintulad sa sampling mula sa mga distribusyon |
| Mga produkto ng tensor | Multi-qubit system (exponential state space — parehong matematika sa multi-linear algebra sa ML) |
| Unitary matrice | Quantum analogues ng orthogonal transformations |
---

## Buod
| Konsepto | Pangunahing Ideya | Key Equation |
|---------|-----------|-------------|
| Dalalidad ng wave-particle | Ang bagay ay may mga katangian ng alon | λ = h/p |
| Wavefunction | Kumpletong paglalarawan ng quantum state | P(x) = \|ψ(x)\|² |
| Schrodinger equation | Paano umuunlad ang mga estado ng quantum | iℏ ∂ψ/∂t = Ĥψ |
| Mga Operator | Ang mga Observable ay mga operator ng Hermitian | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Kawalang-katiyakan | Mga pangunahing limitasyon sa sabay-sabay na kaalaman | ΔxΔp ≥ ℏ/2 |
| Superposisyon | Maaaring idagdag ang mga estado | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Pagkagambala | Hindi mapaghihiwalay na magkasanib na estado | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Quantum gates | Unitary operations sa qubits | H, CNOT, at unibersal na gate set |
Hinahamon ng quantum mechanics ang ating pinakamalalim na intuwisyon tungkol sa realidad — mga particle na mga alon, mga bagay sa dalawang lugar nang sabay-sabay, mga ugnayang sumasalungat sa klasikal na paliwanag. Gayunpaman ang matematika nito ay tumpak at ang mga hula nito ay walang kaparis sa katumpakan. Para sa mga data scientist, ang quantum mechanics ay nagiging direktang nauugnay sa pamamagitan ng quantum computing, na nangangako na magbabago ng optimization, cryptography, simulation, at potensyal na machine learning mismo.