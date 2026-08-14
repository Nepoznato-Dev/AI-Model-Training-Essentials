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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
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

Quantum mechanics is the theory of physics at the smallest scales — atoms, electrons, photons, and the fundamental particles of nature. It replaces the deterministic world of classical mechanics with probabilities, superpositions, and entanglement. Despite its counterintuitive nature, quantum mechanics is the most precisely tested theory in all of science. Today, its principles are becoming directly relevant to computing through quantum computers, which promise to solve certain problems exponentially faster than classical machines.

---

## Historical Motivation

### Failures of Classical Physics

| Problem | Classical Prediction | Observation | Resolution |
|---------|---------------------|-------------|------------|
| Black-body radiation | Ultraviolet catastrophe (infinite energy at short λ) | Finite peak wavelength | Planck: energy is quantised (E = nhν) |
| Photoelectric effect | KE depends on intensity, not frequency | KE depends on frequency | Einstein: light is quantised (photons, E = hν) |
| Atomic spectra | Continuous emission spectrum | Discrete spectral lines | Bohr: electrons occupy quantised orbits |
| Electron diffraction | Particles don't diffract | Electrons produce interference patterns | de Broglie: particles have wavelength λ = h/p |

### Key Constants

| Constant | Symbol | Value |
|----------|--------|-------|
| Planck's constant | h | 6.626 × 10⁻³⁴ J·s |
| Reduced Planck's constant | ℏ = h/2π | 1.055 × 10⁻³⁴ J·s |
| Speed of light | c | 3.0 × 10⁸ m/s |
| Electron mass | m_e | 9.109 × 10⁻³¹ kg |
| Elementary charge | e | 1.602 × 10⁻¹⁹ C |
| Bohr radius | a₀ | 5.292 × 10⁻¹¹ m |

---

## Wave-Particle Duality

### de Broglie Wavelength

Every particle with momentum p has an associated wavelength:

λ = h/p = h/(mv)

| Particle | Typical λ | Observable Wave Behaviour? |
|----------|-----------|---------------------------|
| Electron (100 eV) | 0.12 nm | Yes (crystal diffraction) |
| Proton | 0.003 nm | Yes (neutron scattering) |
| Baseball (40 m/s) | 10⁻³⁴ m | No (far too small to detect) |

### Double-Slit Experiment

The quintessential quantum experiment:
1. Fire particles (electrons, photons) one at a time at two slits
2. Each particle lands at a single point on the detector
3. Over time, an interference pattern emerges — as if each particle passed through both slits simultaneously
4. If you measure which slit the particle goes through, the interference pattern disappears

**Conclusion:** Quantum objects are neither purely particles nor purely waves. They exhibit wave-like behaviour when unobserved and particle-like behaviour when measured.

---

## The Wavefunction

### Definition

The **wavefunction** ψ(x, t) completely describes a quantum system. It is a complex-valued function whose squared modulus gives the probability density:

P(x) = |ψ(x)|² = ψ*(x)ψ(x)

### Normalisation

The total probability must equal 1:

∫ |ψ(x)|² dx = 1 (over all space)

### Born Rule

The probability of finding the particle between x and x + dx:

P(x to x+dx) = |ψ(x)|² dx

For a general observable with eigenstates φₙ:
P(measuring eigenvalue aₙ) = |⟨φₙ|ψ⟩|²

---

## The Schrodinger Equation

### Time-Dependent Schrodinger Equation

iℏ ∂ψ/∂t = Ĥψ

where Ĥ is the **Hamiltonian operator** (total energy operator).

### Time-Independent Schrodinger Equation

For stationary states (energy eigenstates):

Ĥψ = Eψ

This is an eigenvalue equation: the allowed energies E are the eigenvalues of Ĥ.

### Particle in a Box (Infinite Square Well)

The simplest quantum system: particle confined to 0 < x < L.

| Quantity | Result |
|----------|--------|
| Wavefunctions | ψₙ(x) = √(2/L) sin(nπx/L) |
| Energy levels | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Ground state | n = 1, E₁ = h²/(8mL²) |
| Zero-point energy | E₁ > 0 (particle cannot be perfectly still) |
| Quantum number | n = 1, 2, 3, ... (positive integers only) |

### Quantum Harmonic Oscillator

V(x) = ½mω²x²

| Quantity | Result |
|----------|--------|
| Energy levels | Eₙ = (n + ½)ℏω |
| Zero-point energy | E₀ = ½ℏω |
| Spacing | ΔE = ℏω (uniform) |
| Wavefunctions | Hermite polynomials × Gaussian |

---

## Operators and Observables

In quantum mechanics, every physical observable corresponds to a **Hermitian operator**.

### Key Operators

| Observable | Operator (position space) | Eigenvalues |
|-----------|--------------------------|-------------|
| Position | x̂ = x | All real x |
| Momentum | p̂ = −iℏ ∂/∂x | All real p |
| Energy (Hamiltonian) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (discrete for bound states) |
| Angular momentum | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Spin | Ŝ = (ℏ/2)σ (Pauli matrices) | ±ℏ/2 (for spin-½) |

### Expectation Values

The average result of measuring observable A on state ψ:

⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx

### Commutation Relations

[Â, B̂] = ÂB̂ − B̂Â

| Commutator | Result | Significance |
|-----------|--------|-------------|
| [x̂, p̂] | iℏ | Position and momentum are incompatible |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Angular momentum components are incompatible |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Pauli matrices (spin components) |

If [Â, B̂] = 0, the observables can be measured simultaneously (share eigenstates).

---

## Uncertainty Principle

### Heisenberg Uncertainty Principle

Δx · Δp ≥ ℏ/2

More generally, for any two observables A and B:

ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|

### Uncertainty Relations

| Pair | Relation | Interpretation |
|------|----------|----------------|
| Position-momentum | ΔxΔp ≥ ℏ/2 | Cannot know both precisely |
| Energy-time | ΔEΔt ≥ ℏ/2 | Short-lived states have uncertain energy |
| Angular momentum | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Cannot know all components simultaneously |

**Important:** Uncertainty is not about measurement disturbance — it is a fundamental property of quantum states. A particle does not have a definite position and momentum simultaneously.

---

## Quantum States and Superposition

### Dirac Notation (Bra-Ket)

| Symbol | Name | Meaning |
|--------|------|---------|
| \|ψ⟩ | Ket | State vector (column vector) |
| ⟨ψ\| | Bra | Conjugate transpose (row vector) |
| ⟨φ\|ψ⟩ | Inner product | Amplitude for ψ to be found in state φ |
| \|ψ\|² | Norm squared | Probability |

### Superposition Principle

If \|ψ₁⟩ and \|ψ₂⟩ are valid quantum states, then any linear combination is also valid:

\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

where |α|² + |β|² = 1 (normalisation).

**Measurement:** When measured, the system "collapses" to \|ψ₁⟩ with probability |α|² or \|ψ₂⟩ with probability |β|².

### Qubits

A **qubit** is a quantum bit: a two-level quantum system.

\|ψ⟩ = α\|0⟩ + β\|1⟩, where |α|² + |β|² = 1

| Representation | \|0⟩ | \|1⟩ |
|---------------|------|------|
| Spin | Spin up ↑ | Spin down ↓ |
| Photon polarisation | Horizontal | Vertical |
| Energy level | Ground state | Excited state |
| Circuit | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |

**Bloch sphere:** Any qubit state can be written as:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩

where θ ∈ [0, π] and φ ∈ [0, 2π). The state space is a sphere.

---

## Entanglement

Two qubits are **entangled** when their joint state cannot be written as a product of individual states.

### Bell States (Maximally Entangled)

| State | Expression | Name |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Bell state |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Bell state |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Bell state |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Singlet state |

### Properties of Entanglement

| Property | Description |
|----------|-------------|
| Correlation | Measuring one qubit instantly determines the other, regardless of distance |
| No communication | Cannot use entanglement alone to send information faster than light |
| Monogamy | If A is maximally entangled with B, it cannot be entangled with C |
| Fragility | Interaction with environment destroys entanglement (decoherence) |

### EPR Paradox and Bell's Theorem

Einstein, Podolsky, and Rosen argued that quantum mechanics must be incomplete (hidden variables). Bell showed that any local hidden variable theory satisfies certain inequalities. Experiments violate Bell inequalities — confirming quantum mechanics and ruling out local hidden variables.

---

## Quantum Gates

Quantum gates are unitary operations on qubits.

### Single-Qubit Gates

| Gate | Matrix | Effect |
|------|--------|--------|
| **Pauli-X** (NOT) | [[0,1],[1,0]] | Bit flip: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + phase flip |
| **Pauli-Z** | [[1,0],[0,−1]] | Phase flip: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Creates superposition: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Phase** (S) | [[1,0],[0,i]] | π/2 rotation around Z |
| **T gate** | [[1,0],[0,e^{iπ/4}]] | π/4 rotation around Z |
| **Rotation** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | Rotation by θ around X axis |

### Two-Qubit Gates

| Gate | Description | Effect |
|------|-------------|--------|
| **CNOT** | Controlled-NOT | Flips target if control is \|1⟩ |
| **CZ** | Controlled-Z | Applies Z to target if control is \|1⟩ |
| **SWAP** | Exchange qubits | \|ab⟩ → \|ba⟩ |

### Creating Entanglement

Apply H to qubit 1, then CNOT with qubit 1 as control:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩

---

## Quantum Algorithms

| Algorithm | Speedup | Application |
|-----------|---------|-------------|
| **Shor's** | Exponential (factoring) | Breaks RSA encryption |
| **Grover's** | Quadratic (search) | Unstructured search in O(√N) |
| **VQE** | Heuristic | Finding ground state energies (chemistry, materials) |
| **QAOA** | Heuristic | Combinatorial optimization |
| **HHL** | Exponential (under conditions) | Solving linear systems |
| **Quantum simulation** | Exponential | Simulating quantum systems (Feynman's original motivation) |

---

## Relevance to Machine Learning and Data Science

| Quantum Concept | Application |
|----------------|-------------|
| Qubits and superposition | Quantum machine learning, quantum-enhanced sampling |
| Entanglement | Quantum communication, quantum key distribution (QKD) |
| Quantum gates | Quantum circuit design for ML subroutines |
| Grover's algorithm | Quadratic speedup for search-based optimisation |
| Shor's algorithm | Threat to current cryptography; motivates post-quantum crypto |
| Quantum simulation | Drug discovery, materials science, chemistry simulation |
| Variational algorithms (VQE, QAOA) | Near-term quantum ML on NISQ devices |
| Born rule | Probabilistic outcomes analogous to sampling from distributions |
| Tensor products | Multi-qubit systems (exponential state space — same math as multi-linear algebra in ML) |
| Unitary matrices | Quantum analogues of orthogonal transformations |

---

## Summary

| Concept | Core Idea | Key Equation |
|---------|-----------|-------------|
| Wave-particle duality | Matter has wave properties | λ = h/p |
| Wavefunction | Complete description of quantum state | P(x) = \|ψ(x)\|² |
| Schrodinger equation | How quantum states evolve | iℏ ∂ψ/∂t = Ĥψ |
| Operators | Observables are Hermitian operators | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Uncertainty | Fundamental limits on simultaneous knowledge | ΔxΔp ≥ ℏ/2 |
| Superposition | States can be added | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Entanglement | Non-separable joint states | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Quantum gates | Unitary operations on qubits | H, CNOT, and universal gate sets |

Quantum mechanics challenges our deepest intuitions about reality — particles that are waves, objects in two places at once, correlations that defy classical explanation. Yet its mathematics is precise and its predictions are unmatched in accuracy. For data scientists, quantum mechanics is becoming directly relevant through quantum computing, which promises to transform optimisation, cryptography, simulation, and potentially machine learning itself.
