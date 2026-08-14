---
# Metadata
title: "Physics"
description: "Fundamental forces, mechanics, thermodynamics, electromagnetism, relativity, quantum mechanics"
category: "Natural Sciences"
subcategory: "Physical Sciences"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from science_and_nature.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [physics, forces, energy, thermodynamics, electromagnetism, relativity, quantum-mechanics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Physics

Physics asks the most fundamental question in science: how does matter and energy behave? Everything else — chemistry, biology, engineering — builds on the answers. Physics ranges from the subatomic scale (quantum mechanics) to the cosmic scale (general relativity), and its principles underpin all other natural sciences.

---

## The Four Fundamental Forces

Every interaction in the universe comes down to four forces. Everything you have ever felt — the ground under your feet, the warmth of the sun, the magnet on your fridge — is one of these at work.

| Force | Relative Strength | Range | What It Does | Mediating Particle |
|-------|-------------------|-------|-------------|-------------------|
| **Strong nuclear** | 1 (strongest) | Subatomic (~10⁻¹⁵ m) | Holds protons and neutrons together in atomic nuclei | Gluon |
| **Electromagnetic** | ~1/137 | Infinite | Governs electricity, magnetism, light, and chemistry | Photon |
| **Weak nuclear** | ~10⁻⁶ | Subatomic (~10⁻¹⁸ m) | Responsible for radioactive decay | W and Z bosons |
| **Gravity** | ~10⁻³⁹ (weakest) | Infinite | Pulls masses together; shapes the cosmos | Graviton (hypothetical) |

Gravity is absurdly weak compared to the others — a tiny fridge magnet overpowers the gravitational pull of the entire Earth. But gravity has infinite range and never cancels out, so on cosmic scales it dominates.

---

## Classical Mechanics

Classical mechanics (Newtonian mechanics) describes the motion of macroscopic objects at speeds far below the speed of light. It is sufficient for everyday engineering — bridges, cars, projectiles, planets in orbit.

### Newton's Three Laws

| Law | Statement | Implication |
|-----|-----------|-------------|
| **First (Inertia)** | An object at rest stays at rest; an object in motion stays in motion — unless acted on by a net external force | Defines the concept of an inertial reference frame |
| **Second (F = ma)** | Net force equals mass times acceleration | Quantifies how forces change motion |
| **Third (Action-Reaction)** | For every action, there is an equal and opposite reaction | Forces always come in pairs |

### Key Quantities

| Quantity | Symbol | Unit | Formula |
|----------|--------|------|---------|
| **Velocity** | v | m/s | Displacement / time |
| **Acceleration** | a | m/s² | Change in velocity / time |
| **Force** | F | Newtons (N) | m × a |
| **Momentum** | p | kg·m/s | m × v |
| **Kinetic energy** | KE | Joules (J) | ½mv² |
| **Potential energy** | PE | Joules (J) | mgh (gravitational) |
| **Work** | W | Joules (J) | F × d × cos(θ) |
| **Power** | P | Watts (W) | W / t |

Conservation of momentum and conservation of energy are among the most powerful tools in physics — they apply to collisions, explosions, orbits, and virtually every mechanical interaction.

---

## Thermodynamics

Three laws govern energy. They are absolute — no known process violates them.

### The Three Laws

| Law | Statement | Consequence |
|-----|-----------|-------------|
| **First law** | Energy cannot be created or destroyed, only transformed | Total energy in a closed system is constant |
| **Second law** | Entropy (disorder) in a closed system always increases | Heat flows from hot to cold; no engine is 100% efficient; time has a direction |
| **Third law** | Absolute zero (−273.15°C / 0 K) is unreachable | As temperature approaches zero, entropy approaches a minimum |

### Practical Implications

- Coffee cools down because heat disperses into the surroundings (second law).
- A car engine converts about 25% of gasoline energy into motion; the rest becomes waste heat.
- Refrigerators and air conditioners move heat from cold to hot — but they require external work to do so (they don't violate the second law).
- Perpetual motion machines are impossible under these laws.

---

## Electricity and Magnetism

Electricity and magnetism are two faces of the same force: electromagnetism. Moving charges create magnetic fields; changing magnetic fields create electric currents. This relationship powers most of modern technology.

### Core Concepts

| Concept | Symbol | Unit | What It Means |
|---------|--------|------|---------------|
| **Voltage** | V | Volts (V) | The "pressure" pushing charges through a circuit |
| **Current** | I | Amperes (A) | How many charges flow past a point per second |
| **Resistance** | R | Ohms (Ω) | How much a material opposes the flow of current |
| **Power** | P | Watts (W) | Rate of energy transfer (P = V × I) |

**Ohm's Law** (V = I × R) is the foundation of circuit analysis. If you know any two values, you can calculate the third.

**Electromagnetic induction** — discovered by Faraday — is how power plants generate electricity. Spin a magnet inside a coil of wire, and you get current. That is essentially what every turbine does, whether driven by steam (coal, nuclear), water (hydroelectric), or wind.

### Maxwell's Equations (Conceptual)

James Clerk Maxwell unified electricity and magnetism into four equations:

| Equation | What It Says |
|----------|-------------|
| **Gauss's law (electric)** | Electric charges produce electric fields; field lines begin and end on charges |
| **Gauss's law (magnetic)** | There are no magnetic monopoles; magnetic field lines always form closed loops |
| **Faraday's law** | A changing magnetic field produces an electric field (basis of generators) |
| **Ampère-Maxwell law** | Electric currents and changing electric fields produce magnetic fields |

These equations predicted electromagnetic waves — which turned out to be light. Maxwell showed that visible light, radio waves, X-rays, and microwaves are all the same phenomenon at different frequencies.

---

## Relativity

Einstein's two theories of relativity fundamentally changed our understanding of space, time, and energy.

### Special Relativity (1905)

| Principle | Description |
|-----------|-------------|
| **Speed of light is constant** | Light travels at ~300,000 km/s in all reference frames, regardless of the observer's motion |
| **Time dilation** | Moving clocks tick slower relative to a stationary observer |
| **Length contraction** | Moving objects are shortened in the direction of motion |
| **Mass-energy equivalence** | E = mc² — a small amount of mass contains an enormous amount of energy |

E = mc² is why the sun shines (fusion converts a tiny fraction of mass into energy) and how nuclear weapons work.

### General Relativity (1915)

General relativity extends special relativity to include gravity. Mass curves spacetime, and that curvature is what we experience as gravity. Key predictions — all confirmed:

- **Gravitational lensing**: Massive objects bend light around them
- **Gravitational time dilation**: Clocks tick slower in stronger gravitational fields (GPS satellites must correct for this)
- **Gravitational waves**: Ripples in spacetime from accelerating massive objects (first detected by LIGO in 2015)
- **Black holes**: Regions where spacetime curvature is so extreme that nothing, not even light, can escape

---

## Quantum Mechanics

At the subatomic scale, the rules change completely. Quantum mechanics is the most precisely tested theory in all of science, and it is deeply counterintuitive.

### Core Principles

| Principle | Description |
|-----------|-------------|
| **Wave-particle duality** | Particles (electrons, photons) behave as both waves and particles depending on how they are measured |
| **Superposition** | A quantum system can exist in multiple states simultaneously until measured |
| **Uncertainty principle** | You cannot simultaneously know both the exact position and exact momentum of a particle (Heisenberg) |
| **Entanglement** | Two particles can be correlated so that measuring one instantly determines the state of the other, regardless of distance |
| **Quantization** | Energy comes in discrete packets (quanta), not continuous values |

### Why It Matters

- **Semiconductors**: The entire electronics industry relies on quantum behavior of electrons in silicon
- **Lasers**: Based on stimulated emission of photons (a quantum process)
- **MRI machines**: Use nuclear magnetic resonance, a quantum phenomenon
- **Quantum computing**: Exploits superposition and entanglement to solve certain problems exponentially faster than classical computers
- **Chemistry**: Chemical bonding itself is a quantum phenomenon — electrons occupying molecular orbitals

---

## Energy

Energy comes in many forms — kinetic (motion), potential (stored), thermal (heat), chemical, electrical, nuclear — but it always obeys one rule: it cannot be created or destroyed, only transformed. This is the first law of thermodynamics, and it is absolute.

The second law is less cheerful: every energy transformation loses some energy as waste heat. No process is 100% efficient.

| Energy Source | Type | Efficiency | Key Limitation |
|---------------|------|-----------|----------------|
| **Coal** | Non-renewable | ~33-40% | CO₂ emissions, air pollution |
| **Natural gas** | Non-renewable | ~40-60% (combined cycle) | Methane leaks, still emits CO₂ |
| **Nuclear fission** | Non-renewable (fuel-limited) | ~33-37% | Waste storage, public opposition |
| **Solar PV** | Renewable | ~15-22% | Intermittent, requires storage |
| **Wind** | Renewable | ~35-45% | Intermittent, location-dependent |
| **Hydroelectric** | Renewable | ~85-90% | Geography-limited, ecosystem impact |
| **Geothermal** | Renewable | ~10-23% | Location-limited (tectonic hotspots) |

---

## Summary

Physics is the foundation of all natural science. The four fundamental forces govern every interaction in the universe. Classical mechanics describes the everyday world of motion and forces. Thermodynamics sets absolute limits on energy conversion. Electromagnetism unifies electricity, magnetism, and light. Relativity reveals that space and time are a single fabric, curved by mass. Quantum mechanics governs the subatomic world and underpins modern technology from semiconductors to MRI machines. What unifies all of physics is the commitment to mathematical precision and experimental verification — every claim is tested against measurement, and every theory is provisional.
