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
# Thermodynamics and Statistical Mechanics

Thermodynamics describes the macroscopic behaviour of systems in terms of temperature, pressure, and entropy — without knowing what atoms look like. Statistical mechanics explains thermodynamics from the bottom up: it derives macroscopic properties from the microscopic behaviour of vast numbers of particles. Together, they provide the deepest understanding of energy, entropy, and equilibrium — concepts that have migrated into information theory, machine learning, and beyond.

---

## Thermodynamic Variables and State

### State Variables

| Variable | Type | Unit | Description |
|----------|------|------|-------------|
| Temperature (T) | Intensive | Kelvin (K) | Average kinetic energy per particle |
| Pressure (P) | Intensive | Pascal (Pa) | Force per unit area |
| Volume (V) | Extensive | m³ | Space occupied |
| Internal energy (U) | Extensive | Joule (J) | Total microscopic energy |
| Entropy (S) | Extensive | J/K | Measure of disorder/microstates |
| Number of particles (N) | Extensive | moles or count | Amount of substance |

**Intensive** variables don't depend on system size; **extensive** variables do.

### Equation of State

For an ideal gas: PV = nRT = Nk_BT

| Constant | Value |
|----------|-------|
| R (gas constant) | 8.314 J/(mol·K) |
| k_B (Boltzmann constant) | 1.381 × 10⁻²³ J/K |
| N_A (Avogadro's number) | 6.022 × 10²³ /mol |

---

## The Laws of Thermodynamics

### Zeroth Law

If A is in thermal equilibrium with B, and B with C, then A is in thermal equilibrium with C.

**Meaning:** Temperature is well-defined and measurable.

### First Law (Energy Conservation)

ΔU = Q − W

| Symbol | Meaning |
|--------|---------|
| ΔU | Change in internal energy |
| Q | Heat added to system |
| W | Work done by system |

**Differential form:** dU = δQ − δW = δQ − PdV

| Process | Constraint | Consequence |
|---------|-----------|-------------|
| Isochoric | dV = 0 | W = 0, ΔU = Q |
| Isobaric | dP = 0 | W = PΔV |
| Isothermal | dT = 0 | ΔU = 0 (ideal gas), Q = W |
| Adiabatic | δQ = 0 | ΔU = −W |

### Second Law (Entropy)

**Clausius statement:** Heat cannot spontaneously flow from cold to hot.

**Kelvin-Planck statement:** No engine can convert all heat into work.

**Entropy statement:** For any process: ΔS_universe ≥ 0

| Process type | ΔS_universe |
|-------------|-------------|
| Reversible | = 0 |
| Irreversible (real) | > 0 |

**Entropy change:** dS = δQ_rev / T

### Third Law

As T → 0 K, the entropy of a perfect crystal approaches zero: lim_{T→0} S = 0

**Meaning:** Absolute zero is unattainable in finite steps.

---

## Entropy in Depth

### Thermodynamic Entropy

S is a state function. For a reversible process between states A and B:

ΔS = ∫_A^B δQ_rev / T

**Worked Example:** Entropy change when heating water from T₁ to T₂ at constant pressure.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)

### Statistical Entropy (Boltzmann)

S = k_B ln Ω

where Ω is the number of microstates consistent with the macrostate.

| Macrostate | Microstates (Ω) | Entropy |
|-----------|-----------------|---------|
| All gas in one half of box | Small | Low |
| Gas evenly distributed | Very large | High |
| Perfect crystal at 0 K | 1 | 0 |

**Connection:** The second law becomes statistical — systems evolve toward macrostates with more microstates simply because they're overwhelmingly more probable.

---

## Enthalpy and Free Energy

### Enthalpy

H = U + PV

Useful for processes at constant pressure (most chemistry and biology).

ΔH = Q_p (heat at constant pressure)

### Helmholtz Free Energy

F = U − TS

| Property | Statement |
|----------|-----------|
| Meaning | Maximum work extractable at constant T, V |
| Equilibrium | System minimises F at constant T, V |
| Relation to partition function | F = −k_BT ln Z |

### Gibbs Free Energy

G = H − TS = U + PV − TS

| Property | Statement |
|----------|-----------|
| Meaning | Maximum non-expansion work at constant T, P |
| Equilibrium | System minimises G at constant T, P |
| Spontaneity | ΔG < 0 → spontaneous; ΔG = 0 → equilibrium |
| Chemical reactions | ΔG = ΔH − TΔS determines direction |

### Summary of Thermodynamic Potentials

| Potential | Natural Variables | Differential | Minimised When |
|-----------|-------------------|-------------|----------------|
| U (internal energy) | S, V | dU = TdS − PdV | Isolated system |
| H (enthalpy) | S, P | dH = TdS + VdP | Constant P, adiabatic |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Constant T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Constant T, P |

---

## The Carnot Cycle

The **Carnot cycle** is the most efficient heat engine possible, operating between temperatures T_H (hot) and T_C (cold).

### Four Stages

| Stage | Process | What Happens |
|-------|---------|-------------|
| 1 → 2 | Isothermal expansion | Absorb heat Q_H from hot reservoir at T_H |
| 2 → 3 | Adiabatic expansion | Gas cools from T_H to T_C |
| 3 → 4 | Isothermal compression | Reject heat Q_C to cold reservoir at T_C |
| 4 → 1 | Adiabatic compression | Gas heats from T_C to T_H |

### Carnot Efficiency

η_Carnot = 1 − T_C/T_H

| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500 K | 300 K | 40% |
| 1000 K | 300 K | 70% |
| 300 K | 299 K | 0.33% |

**No real engine can exceed Carnot efficiency.** Real engines are always irreversible (friction, turbulence, finite temperature differences).

---

## Statistical Mechanics

### The Boltzmann Distribution

For a system in thermal equilibrium at temperature T, the probability of being in a microstate with energy E_i:

P(E_i) = (1/Z) e^{−E_i / k_BT}

where Z is the **partition function**:

Z = Σᵢ e^{−E_i / k_BT}

### The Partition Function

Z encodes all thermodynamic information about the system.

| Quantity | Formula |
|----------|---------|
| Helmholtz free energy | F = −k_BT ln Z |
| Average energy | ⟨E⟩ = −∂(ln Z)/∂β where β = 1/(k_BT) |
| Entropy | S = k_B(ln Z + β⟨E⟩) |
| Heat capacity | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Pressure | P = (1/β) ∂(ln Z)/∂V |

### Worked Example: Two-State System

A particle can be in state 0 (energy 0) or state 1 (energy ε).

Z = 1 + e^{−βε}

| Quantity | Result |
|----------|--------|
| P(state 0) | 1/(1 + e^{−βε}) |
| P(state 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| High T limit (β→0) | ⟨E⟩ → ε/2 (equal probability) |
| Low T limit (β→∞) | ⟨E⟩ → 0 (ground state) |

### Equipartition Theorem

Each quadratic degree of freedom contributes ½k_BT to the average energy.

| System | Degrees of Freedom | ⟨E⟩ |
|--------|-------------------|------|
| Monatomic gas (He) | 3 translational | (3/2)k_BT |
| Diatomic gas (N₂) at room T | 3 trans + 2 rot | (5/2)k_BT |
| Diatomic gas at high T | 3 trans + 2 rot + 1 vib | (7/2)k_BT |
| Solid (Einstein model) | 3 vibrational (per atom) | 3k_BT |

---

## Connection to Information Theory

### Shannon Entropy vs Thermodynamic Entropy

| Aspect | Shannon Entropy H(X) | Thermodynamic Entropy S |
|--------|---------------------|------------------------|
| Definition | −Σ pᵢ log pᵢ | k_B ln Ω (or −k_B Σ pᵢ ln pᵢ) |
| Maximum when | Uniform distribution | Thermal equilibrium |
| Measures | Uncertainty / information content | Number of accessible microstates |
| Units | Bits or nats | J/K |

**Gibbs entropy formula:** S = −k_B Σᵢ pᵢ ln pᵢ (identical in form to Shannon entropy)

### Maximum Entropy Principle

Both fields use the same principle: the distribution that best represents our state of knowledge is the one that maximises entropy subject to known constraints.

| Constraint | Resulting Distribution |
|-----------|----------------------|
| Known mean | Exponential distribution |
| Known mean and variance | Gaussian distribution |
| Known energy ⟨E⟩ | Boltzmann distribution |
| No constraints | Uniform distribution |

### Landauer's Principle

Erasing one bit of information dissipates at least k_BT ln 2 of energy as heat. This connects information processing directly to thermodynamics — computation has a fundamental energy cost.

---

## Relevance to Machine Learning and Data Science

| Thermo/StatMech Concept | Application |
|------------------------|-------------|
| Boltzmann distribution | Softmax function, energy-based models, simulated annealing |
| Partition function | Normalising constant in probabilistic models, intractable in general |
| Free energy | Variational inference (minimising variational free energy = minimising KL divergence) |
| Entropy | Regularisation, exploration in RL (maximum entropy RL), decision trees |
| Maximum entropy principle | MaxEnt classifiers, prior selection, distribution estimation |
| Simulated annealing | Global optimisation by gradually reducing "temperature" |
| Statistical mechanics | Understanding phase transitions in learning (grokking, double descent) |
| Equipartition | Understanding energy distribution in physical simulations |
| Landauer's principle | Fundamental limits of computation, reversible computing |
| Gibbs sampling | MCMC method directly inspired by statistical mechanics |
| Temperature (in softmax) | Controls randomness of predictions: P(i) ∝ exp(z_i/T) |

---

## Summary

| Law/Concept | Core Idea | Formula |
|------------|-----------|---------|
| Zeroth law | Temperature is well-defined | Transitivity of thermal equilibrium |
| First law | Energy is conserved | ΔU = Q − W |
| Second law | Entropy of universe increases | ΔS ≥ 0 |
| Third law | Absolute zero is unattainable | S → 0 as T → 0 |
| Boltzmann entropy | Entropy counts microstates | S = k_B ln Ω |
| Boltzmann distribution | Probability of energy states | P ∝ e^{−E/k_BT} |
| Partition function | Encodes all thermodynamic info | Z = Σ e^{−E_i/k_BT} |
| Free energy | Useful work available | F = U − TS, G = H − TS |
| Carnot efficiency | Maximum heat engine efficiency | η = 1 − T_C/T_H |

Thermodynamics and statistical mechanics are where physics meets information theory. The same entropy that governs heat engines governs data compression. The same Boltzmann distribution that describes gas molecules powers the softmax layer in every classifier. Understanding these connections gives you a unified view of physics, probability, and machine learning.
