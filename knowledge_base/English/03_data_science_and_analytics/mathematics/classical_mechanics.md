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

Classical mechanics describes the motion of objects under the influence of forces. From falling apples to orbiting planets, from vibrating strings to colliding particles, its principles govern the macroscopic world. Beyond its physical applications, classical mechanics gave birth to the calculus of variations, symplectic geometry, and the Hamiltonian framework that underpins quantum mechanics and modern optimization.

---

## Newtonian Mechanics

### Newton's Three Laws

| Law | Statement | Mathematical Form |
|-----|-----------|-------------------|
| **First (Inertia)** | An object remains at rest or in uniform motion unless acted upon by a force | If F_net = 0, then v = constant |
| **Second (F = ma)** | Force equals mass times acceleration | **F** = m**a** = m(d²**x**/dt²) |
| **Third (Action-Reaction)** | Every action has an equal and opposite reaction | **F**₁₂ = −**F**₂₁ |

### Free-Body Diagrams

A **free-body diagram** isolates an object and shows all forces acting on it.

**Common forces:**

| Force | Formula | Direction |
|-------|---------|-----------|
| Gravity (near Earth) | F = mg | Downward |
| Normal force | N | Perpendicular to surface |
| Friction (static) | f_s ≤ μ_s N | Opposes impending motion |
| Friction (kinetic) | f_k = μ_k N | Opposes motion |
| Spring (Hooke's law) | F = −kx | Restoring (toward equilibrium) |
| Tension | T | Along the string/rope |
| Drag | F_d = ½C_d ρAv² | Opposes velocity |

### Worked Example: Block on Incline

A block of mass m on a frictionless incline at angle θ.
- Forces: gravity (mg down), normal force (N perpendicular to surface)
- Decompose gravity: mg sin θ (along incline), mg cos θ (into surface)
- N = mg cos θ (no motion perpendicular to surface)
- Acceleration along incline: a = g sin θ

---

## Energy Methods

### Work and Kinetic Energy

**Work** done by a force: W = ∫ **F** · d**r**

**Work-Energy Theorem:** W_net = ΔKE = ½mv₂² − ½mv₁²

### Potential Energy

| Force | Potential Energy | Notes |
|-------|-----------------|-------|
| Gravity (near surface) | U = mgh | h = height above reference |
| Gravity (general) | U = −GMm/r | Zero at infinity |
| Spring | U = ½kx² | x = displacement from equilibrium |
| Electrostatic | U = kq₁q₂/r | Like charges: positive U |

### Conservation of Energy

If only conservative forces act: E = KE + PE = constant

½mv₁² + U₁ = ½mv₂² + U₂

**Worked Example:** A ball dropped from height h.
- Initial: KE = 0, PE = mgh
- Just before hitting ground: KE = ½mv², PE = 0
- Conservation: mgh = ½mv² → v = √(2gh)

### Power

P = dW/dt = **F** · **v** (rate of doing work)

---

## Momentum and Collisions

### Linear Momentum

**p** = m**v**

Newton's second law (alternative form): **F** = d**p**/dt

### Conservation of Momentum

If no external forces: total momentum is conserved.

| Collision Type | KE Conserved? | Momentum Conserved? |
|---------------|---------------|---------------------|
| **Elastic** | Yes | Yes |
| **Inelastic** | No | Yes |
| **Perfectly inelastic** | No (maximum loss) | Yes (objects stick together) |

**1D elastic collision:** Two masses m₁, m₂ with initial velocities u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)

### Angular Momentum

**L** = **r** × **p** = m(**r** × **v**)

Torque: **τ** = d**L**/dt = **r** × **F**

**Conservation:** If no external torque, angular momentum is conserved.

---

## Lagrangian Mechanics

The **Lagrangian** formulation replaces forces with energy, providing a more elegant and general framework.

### The Lagrangian

L = T − V (kinetic energy minus potential energy)

### Principle of Least Action (Hamilton's Principle)

The actual path taken by a system between times t₁ and t₂ minimises (more precisely, makes stationary) the **action**:

S = ∫_{t₁}^{t₂} L(q, q̇, t) dt

### Euler-Lagrange Equations

The condition δS = 0 yields:

d/dt(∂L/∂q̇) − ∂L/∂q = 0

for each generalised coordinate q.

**Worked Example:** Simple pendulum (length l, mass m, angle θ from vertical).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0

### Advantages of Lagrangian Mechanics

| Advantage | Explanation |
|-----------|-------------|
| Coordinate-independent | Works in any coordinate system |
| Handles constraints naturally | No need to compute constraint forces |
| Symmetry → conservation | Noether's theorem connects symmetries to conserved quantities |
| Generalises easily | To fields, relativity, quantum mechanics |

---

## Hamiltonian Mechanics

The **Hamiltonian** formulation is a reformulation of Lagrangian mechanics that uses positions and momenta (instead of positions and velocities).

### The Hamiltonian

H = Σᵢ pᵢq̇ᵢ − L = T + V (for most mechanical systems)

where pᵢ = ∂L/∂q̇ᵢ are the **generalised momenta**.

### Hamilton's Equations

q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ

These are 2n first-order ODEs (vs n second-order Euler-Lagrange equations).

**Worked Example:** Harmonic oscillator (mass m, spring constant k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (as expected)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (Hooke's law)

### Poisson Brackets

For functions f(q, p) and g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)

| Property | Statement |
|----------|-----------|
| Time evolution | df/dt = {f, H} + ∂f/∂t |
| Conservation | f is conserved iff {f, H} = 0 (and ∂f/∂t = 0) |
| Fundamental brackets | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |

**Connection to quantum mechanics:** Poisson brackets become commutators: {f, g} → (1/iℏ)[f̂, ĝ]

---

## Conservation Laws and Noether's Theorem

### Noether's Theorem

Every continuous symmetry of the Lagrangian corresponds to a conserved quantity.

| Symmetry | Conserved Quantity |
|----------|-------------------|
| Time translation invariance | Energy |
| Spatial translation invariance | Linear momentum |
| Rotational invariance | Angular momentum |
| Gauge invariance | Electric charge |

This is one of the deepest results in all of physics — it connects the geometry of spacetime to the fundamental conservation laws.

---

## Rigid Body Dynamics

A **rigid body** is an object where all internal distances remain fixed.

### Key Concepts

| Concept | Formula | Description |
|---------|---------|-------------|
| **Moment of inertia** | I = Σmᵢrᵢ² or I = ∫r² dm | Resistance to rotational acceleration |
| **Rotational KE** | KE = ½Iω² | Energy of rotation |
| **Angular momentum** | L = Iω | Rotational analogue of p = mv |
| **Torque** | τ = Iα | Rotational analogue of F = ma |

### Moments of Inertia (Common Shapes)

| Shape | Axis | I |
|-------|------|---|
| Solid sphere | Through centre | (2/5)MR² |
| Hollow sphere | Through centre | (2/3)MR² |
| Solid cylinder | Along axis | (1/2)MR² |
| Thin rod | Through centre, perpendicular | (1/12)ML² |
| Thin rod | Through end, perpendicular | (1/3)ML² |
| Disc | Through centre, perpendicular | (1/2)MR² |

---

## Orbital Mechanics

### Kepler's Laws

| Law | Statement |
|-----|-----------|
| **First (Ellipses)** | Planets move in ellipses with the Sun at one focus |
| **Second (Equal areas)** | A line from Sun to planet sweeps equal areas in equal times |
| **Third (Harmonic)** | T² ∝ a³ (period squared proportional to semi-major axis cubed) |

### Orbital Energy

E = ½mv² − GMm/r

| E | Orbit Type |
|---|-----------|
| E < 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E > 0 | Hyperbolic (unbound) |

### Escape Velocity

v_escape = √(2GM/R)

For Earth: v_escape ≈ 11.2 km/s

---

## Relevance to Machine Learning and Data Science

| Mechanics Concept | Application |
|------------------|-------------|
| Newton's laws | Physics engines in simulations, game AI, robotics |
| Energy methods | Energy-based models, Hopfield networks, Boltzmann machines |
| Lagrangian mechanics | Physics-informed neural networks, optimal control, trajectory optimization |
| Hamiltonian mechanics | Hamiltonian neural networks (HNNs), symplectic integrators for simulation |
| Conservation laws | Inductive biases in ML models, equivariant neural networks |
| Noether's theorem | Symmetry-aware machine learning, geometric deep learning |
| Rigid body dynamics | Robotics simulation, molecular dynamics, 3D animation |
| Orbital mechanics | Satellite positioning (GPS for location-based ML), space mission design |
| Phase space (Hamiltonian) | Understanding dynamical systems, attractor networks |
| Calculus of variations | Optimal transport, generative modelling (flow matching) |

---

## Summary

| Framework | Core Equation | Strength |
|-----------|--------------|----------|
| Newtonian | **F** = m**a** | Intuitive, direct force analysis |
| Lagrangian | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Coordinate-free, handles constraints |
| Hamiltonian | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Symplectic structure, connects to QM |
| Conservation laws | Noether's theorem | Deep symmetry-conservation connection |

Classical mechanics is not just about falling balls and swinging pendulums. Its mathematical frameworks — Lagrangian and Hamiltonian mechanics — are among the most influential ideas in all of science. They generalise to quantum mechanics, field theory, and even modern machine learning, where energy-based models and physics-informed neural networks draw directly on these centuries-old formulations.
