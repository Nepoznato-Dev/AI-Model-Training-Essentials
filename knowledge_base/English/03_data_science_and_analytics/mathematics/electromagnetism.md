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

Electromagnetism is the study of electric and magnetic fields and their interactions. Unified by Maxwell in the 1860s, electromagnetism explains light, electricity, magnetism, radio waves, and the structure of atoms. It was the first fundamental force to be fully understood mathematically, and its equations inspired Einstein's special relativity and modern field theory.

---

## Electric Fields

### Coulomb's Law

The force between two point charges q₁ and q₂ separated by distance r:

**F** = (1/4πε₀) · (q₁q₂/r²) · r̂

| Constant | Value |
|----------|-------|
| ε₀ (permittivity of free space) | 8.854 × 10⁻¹² F/m |
| 1/4πε₀ (Coulomb constant k) | 8.988 × 10⁹ N·m²/C² |

### Electric Field Definition

**E** = **F**/q (force per unit charge)

For a point charge Q: **E** = (1/4πε₀) · (Q/r²) · r̂

### Electric Field Lines

| Property | Rule |
|----------|------|
| Direction | Point away from positive charges, toward negative |
| Density | Closer lines = stronger field |
| Crossing | Field lines never cross |
| Conductors | Lines meet surface perpendicularly |

### Electric Potential (Voltage)

V = −∫ **E** · d**l** (potential difference is the negative line integral of E)

**E** = −∇V (field is the negative gradient of potential)

For a point charge: V = (1/4πε₀) · Q/r

| Concept | Formula | Unit |
|---------|---------|------|
| Potential energy | U = qV | Joules |
| Electron-volt | 1 eV = 1.602 × 10⁻¹⁹ J | Energy unit |
| Equipotential surface | Surface where V is constant | E is perpendicular to it |

---

## Gauss's Law

### Statement

The total electric flux through any closed surface equals the enclosed charge divided by ε₀:

∮ **E** · d**A** = Q_enc / ε₀

In differential form: ∇ · **E** = ρ/ε₀

### Using Gauss's Law

Gauss's law is most useful when symmetry allows E to be pulled out of the integral.

| Symmetry | Gaussian Surface | Result |
|----------|-----------------|--------|
| Spherical | Sphere | E = Q/(4πε₀r²) outside |
| Cylindrical (line charge) | Cylinder | E = λ/(2πε₀r) |
| Planar (infinite sheet) | Pillbox | E = σ/(2ε₀) |
| Between parallel plates | Pillbox | E = σ/ε₀ |

---

## Conductors and Capacitors

### Conductors in Electrostatic Equilibrium

| Property | Explanation |
|----------|-------------|
| E = 0 inside | Charges rearrange to cancel internal field |
| All charge on surface | No net charge in interior |
| E perpendicular at surface | No tangential component (otherwise charges move) |
| Equipotential throughout | Same V everywhere inside and on surface |

### Capacitors

A **capacitor** stores energy in an electric field between two conductors.

| Configuration | Capacitance |
|--------------|-------------|
| Parallel plates | C = ε₀A/d |
| Cylindrical | C = 2πε₀L / ln(b/a) |
| Spherical | C = 4πε₀ab / (b−a) |

| Formula | Expression |
|---------|------------|
| Charge-voltage | Q = CV |
| Energy stored | U = ½CV² = ½Q²/C |
| Energy density | u = ½ε₀E² |
| Series combination | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Parallel combination | C_total = C₁ + C₂ + ... |

### Dielectrics

Inserting a dielectric (insulating material) with constant κ increases capacitance: C = κC₀.

---

## Magnetic Fields

### Magnetic Force

**F** = q(**v** × **B**) (Lorentz force, magnetic component)

| Property | Statement |
|----------|-----------|
| Direction | Perpendicular to both v and B (right-hand rule) |
| Work done | Zero (force is perpendicular to velocity) |
| Circular motion | Radius r = mv/(qB) in uniform B field |

### Biot-Savart Law

The magnetic field due to a small current element:

d**B** = (μ₀/4π) · I(d**l** × r̂) / r²

| Constant | Value |
|----------|-------|
| μ₀ (permeability of free space) | 4π × 10⁻⁷ T·m/A |

### Ampere's Law

∮ **B** · d**l** = μ₀I_enc

In differential form: ∇ × **B** = μ₀**J**

**Applications:**
| Configuration | B field |
|--------------|---------|
| Long straight wire | B = μ₀I/(2πr) |
| Solenoid (inside) | B = μ₀nI |
| Toroid (inside) | B = μ₀NI/(2πr) |

---

## Electromagnetic Induction

### Faraday's Law

A changing magnetic flux induces an electromotive force (EMF):

EMF = −dΦ_B/dt

where Φ_B = ∫ **B** · d**A** is the magnetic flux.

In differential form: ∇ × **E** = −∂**B**/∂t

**Lenz's law:** The induced EMF opposes the change in flux (the minus sign).

### Applications of Induction

| Application | Principle |
|-------------|-----------|
| Generator | Rotating coil in B field → alternating EMF |
| Transformer | Changing current in primary → EMF in secondary |
| Inductor | Opposes changes in current: EMF = −L(dI/dt) |
| Eddy currents | Induced currents in bulk conductors (braking, heating) |

### Inductors

| Formula | Expression |
|---------|------------|
| Flux linkage | Φ = LI |
| Energy stored | U = ½LI² |
| Series combination | L_total = L₁ + L₂ + ... |
| Parallel combination | 1/L_total = 1/L₁ + 1/L₂ + ... |

---

## Maxwell's Equations

Maxwell's equations unify electricity and magnetism into a single theory.

### In Integral Form

| Equation | Name | Statement |
|----------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Gauss's law (electric) | Electric flux = enclosed charge |
| ∮ **B** · d**A** = 0 | Gauss's law (magnetic) | No magnetic monopoles |
| ∮ **E** · d**l** = −dΦ_B/dt | Faraday's law | Changing B induces E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Ampere-Maxwell law | Current and changing E produce B |

### In Differential Form

| Equation | Name | Expression |
|----------|------|------------|
| Gauss (electric) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnetic) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampere-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |

### The Displacement Current

Maxwell's key addition: the term μ₀ε₀ ∂**E**/∂t (displacement current). This ensures charge conservation and predicts electromagnetic waves.

---

## Electromagnetic Waves

In vacuum (no charges, no currents), Maxwell's equations yield wave equations:

∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²

**Speed of light:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s

### Properties of EM Waves

| Property | Description |
|----------|-------------|
| Transverse | E and B are perpendicular to each other and to propagation direction |
| In phase | E and B reach maxima simultaneously |
| Magnitude ratio | E = cB |
| Energy flux | S = (1/μ₀)**E** × **B** (Poynting vector) |
| Intensity | I = ⟨S⟩ = E₀²/(2μ₀c) |

### The Electromagnetic Spectrum

| Type | Wavelength | Frequency | Source |
|------|-----------|-----------|--------|
| Radio | > 1 m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | > 30 EHz | Nuclear processes |

---

## AC Circuits

### RLC Circuit Components

| Component | Voltage-Current Relation | Impedance |
|-----------|------------------------|-----------|
| Resistor (R) | V = IR | Z_R = R |
| Inductor (L) | V = L(dI/dt) | Z_L = jωL |
| Capacitor (C) | I = C(dV/dt) | Z_C = 1/(jωC) |

### Impedance and Resonance

Total impedance (series RLC): Z = R + j(ωL − 1/ωC)

|ω| = √(R² + (ωL − 1/ωC)²)

**Resonance:** When ωL = 1/ωC → ω₀ = 1/√(LC)
- At resonance: impedance is minimum (= R), current is maximum
- **Quality factor:** Q = ω₀L/R (sharpness of resonance)

### Power in AC Circuits

| Quantity | Formula |
|----------|---------|
| Average power | P_avg = V_rms · I_rms · cos φ |
| Power factor | cos φ = R/\|Z\| |
| RMS voltage | V_rms = V₀/√2 |

---

## Relevance to Machine Learning and Data Science

| EM Concept | Application |
|-----------|-------------|
| Maxwell's equations | Physics-informed neural networks, computational electromagnetics |
| Wave equation | Signal processing foundation, Fourier analysis motivation |
| Electromagnetic spectrum | Sensor data (infrared cameras, radar, satellite imagery) |
| AC circuits / impedance | Understanding hardware that runs ML (power supplies, signal integrity) |
| Poynting vector | Energy flow in wireless communication (relevant to IoT/edge ML) |
| Gauss's law | Analogous to divergence in vector calculus, used in fluid dynamics simulations |
| Capacitors/inductors | Analog computing for neural networks, neuromorphic hardware |
| Resonance | Filter design, frequency-domain analysis, spectral methods |
| Boundary value problems | Finite element methods, mesh-based simulations |
| Vector calculus (∇·, ∇×) | Essential mathematical tools used throughout ML theory |

---

## Summary

| Law | What It Says | Differential Form |
|-----|-------------|-------------------|
| Gauss (electric) | Charges create electric field divergence | ∇ · E = ρ/ε₀ |
| Gauss (magnetic) | No magnetic monopoles | ∇ · B = 0 |
| Faraday | Changing B creates curling E | ∇ × E = −∂B/∂t |
| Ampere-Maxwell | Current and changing E create curling B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |

Electromagnetism is the most complete and well-tested physical theory ever constructed. Its equations — just four — describe everything from static electricity to light to the behaviour of every electronic device ever built. For data scientists, understanding electromagnetism provides deep intuition for wave phenomena, vector calculus, and the physics that underlies all modern computing hardware.
