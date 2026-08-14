<!--
---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Dynamical Systems

A **dynamical system** describes how a state evolves over time according to a fixed rule. From planetary orbits to population dynamics, from weather patterns to training neural networks, dynamical systems theory provides the language and tools for understanding how things change. This file covers ordinary differential equations (ODEs), partial differential equations (PDEs), stability analysis, chaos, and bifurcations.

---

## Ordinary Differential Equations (ODEs)

An ODE relates a function to its derivatives with respect to a single independent variable (usually time).

### Classification

| Property | Types |
|----------|-------|
| **Order** | Highest derivative present (1st order, 2nd order, etc.) |
| **Linear vs Nonlinear** | Linear: y'' + p(t)y' + q(t)y = g(t); Nonlinear: anything else |
| **Homogeneous** | g(t) = 0 (no forcing term) |
| **Autonomous** | No explicit time dependence: dy/dt = f(y) |
| **Constant coefficients** | p, q are constants |

### First-Order ODEs

**General form:** dy/dt = f(t, y)

| Type | Form | Solution Method |
|------|------|-----------------|
| Separable | dy/dt = g(t)h(y) | Separate and integrate: ∫dy/h(y) = ∫g(t)dt |
| Linear first-order | dy/dt + p(t)y = q(t) | Integrating factor: μ(t) = e^(∫p dt) |
| Exact | M(t,y)dt + N(t,y)dy = 0 with ∂M/∂y = ∂N/∂t | Find potential function F(t,y) |
| Bernoulli | dy/dt + p(t)y = q(t)yⁿ | Substitute v = y^(1−n) to linearise |

**Worked Example (Integrating Factor):** Solve dy/dt + 2y = e^(−t), y(0) = 1.
- Integrating factor: μ(t) = e^(∫2 dt) = e^(2t)
- Multiply: d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- Integrate: e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Initial condition: y(0) = 1 → 1 = 1 + C → C = 0
- Solution: y(t) = e^(−t)

### Second-Order Linear ODEs

**General form:** ay'' + by' + cy = g(t)

**Homogeneous case** (g = 0): Solve the characteristic equation ar² + br + c = 0.

| Discriminant | Roots | General Solution |
|-------------|-------|------------------|
| b² > 4ac (overdamped) | Two distinct real r₁, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (critically damped) | Repeated real root r | y = (C₁ + C₂t)e^(rt) |
| b² < 4ac (underdamped) | Complex roots α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |

**Physical interpretation:** A mass-spring-damper system mx'' + bx' + kx = 0.
- Overdamped: heavy damping, no oscillation (door closer)
- Critically damped: fastest return without oscillation (car suspension design target)
- Underdamped: oscillates with decaying amplitude (guitar string)

### Systems of ODEs

Many real systems involve multiple interacting variables:

dx/dt = f(x, y)
dy/dt = g(x, y)

This can be written in vector form: d**x**/dt = **F**(**x**)

**Linear systems:** d**x**/dt = A**x**, where A is a matrix.

Solution depends on eigenvalues of A:

| Eigenvalues | Behaviour |
|-------------|-----------|
| Both real, negative | Stable node (all trajectories converge to origin) |
| Both real, positive | Unstable node |
| Real, opposite signs | Saddle point (unstable) |
| Complex, negative real part | Stable spiral (damped oscillation) |
| Complex, positive real part | Unstable spiral |
| Pure imaginary | Centre (closed orbits) |

---

## Phase Portraits

A **phase portrait** visualises the trajectories of a dynamical system in state space (without solving explicitly).

### Key Features

| Feature | Description |
|---------|-------------|
| **Fixed point (equilibrium)** | Where dx/dt = 0 (no motion) |
| **Trajectory** | Path traced by the system in state space |
| **Nullcline** | Curve where one component's derivative is zero |
| **Limit cycle** | Isolated closed orbit (self-sustained oscillation) |
| **Basin of attraction** | Set of initial conditions leading to a given attractor |
| **Separatrix** | Boundary between different basins of attraction |

### Predator-Prey Model (Lotka-Volterra)

dx/dt = αx − βxy (prey)
dy/dt = δxy − γy (predator)

**Fixed points:**
1. (0, 0) — extinction (saddle point)
2. (γ/δ, α/β) — coexistence (centre — closed orbits)

The system exhibits periodic oscillations: prey increases → predators increase → prey decreases → predators decrease → cycle repeats.

---

## Stability Analysis

### Linear Stability

For a fixed point x*, linearise around it: let u = x − x*, then du/dt ≈ J(x*)u where J is the Jacobian matrix.

**Stability criterion:** The fixed point is:
- **Stable** if all eigenvalues of J have negative real parts
- **Unstable** if any eigenvalue has positive real part
- **Marginally stable** if eigenvalues have zero real parts (need nonlinear analysis)

### Lyapunov Stability

**Lyapunov's direct method** determines stability without linearisation.

A **Lyapunov function** V(x) satisfies:
1. V(x*) = 0 and V(x) > 0 for x ≠ x* (positive definite)
2. dV/dt ≤ 0 along trajectories (non-increasing)

| Condition | Conclusion |
|-----------|------------|
| dV/dt < 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt > 0 | Unstable |

**Worked Example:** System dx/dt = −x + y², dy/dt = −y.
- Try V(x,y) = x² + y² (energy-like function)
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Near origin: dV/dt ≈ −2x² − 2y² < 0 (for small y, the −2y² dominates)
- Conclusion: origin is locally asymptotically stable

---

## Chaos Theory

**Chaos** is deterministic yet unpredictable: the system follows exact rules, but tiny differences in initial conditions lead to vastly different outcomes.

### Requirements for Chaos

| Property | Description |
|----------|-------------|
| Deterministic | No randomness — governed by exact equations |
| Sensitive to initial conditions | Nearby trajectories diverge exponentially |
| Bounded | Trajectories don't escape to infinity |
| Non-periodic | Never repeats exactly |

### The Lorenz System

The classic example of deterministic chaos:

dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy − βz

With standard parameters σ = 10, ρ = 28, β = 8/3:
- The system has three fixed points, all unstable
- Trajectories orbit one fixed point, then suddenly switch to the other
- The result is the **Lorenz attractor** — a strange attractor with fractal structure

**Lyapunov exponent:** Measures the rate of divergence of nearby trajectories.
- Positive Lyapunov exponent → chaos
- For Lorenz system with standard parameters: largest exponent ≈ 0.9 > 0

### The Logistic Map

A simple discrete system that exhibits chaos:
x_{n+1} = rx_n(1 − x_n)

| Parameter r | Behaviour |
|-------------|-----------|
| 0 < r < 1 | Population dies out (x → 0) |
| 1 < r < 3 | Stable fixed point at x = 1 − 1/r |
| 3 < r < 3.449 | Period-2 oscillation |
| 3.449 < r < 3.544 | Period-4 oscillation |
| 3.544 < r < 3.570 | Period-8, 16, 32, ... (period-doubling cascade) |
| r ≈ 3.570 | Onset of chaos |
| 3.570 < r < 4 | Mostly chaotic, with periodic windows |
| r = 4 | Fully chaotic on [0, 1] |

### Butterfly Effect

The popular name for sensitive dependence on initial conditions. In weather systems (modelled by Lorenz equations), a butterfly flapping its wings in Brazil could set off a tornado in Texas — not because the butterfly causes it, but because tiny perturbations grow exponentially.

---

## Bifurcation Theory

A **bifurcation** is a qualitative change in system behaviour as a parameter is varied.

### Types of Bifurcations

| Bifurcation | Normal Form | What Happens |
|-------------|-------------|--------------|
| **Saddle-node** | dx/dt = r − x² | Two fixed points appear/disappear |
| **Transcritical** | dx/dt = rx − x² | Two fixed points exchange stability |
| **Pitchfork (supercritical)** | dx/dt = rx − x³ | One stable point splits into two stable + one unstable |
| **Pitchfork (subcritical)** | dx/dt = rx + x³ | Unstable branches collapse (often catastrophic) |
| **Hopf** | 2D system | Fixed point becomes unstable, limit cycle appears |

### Bifurcation Diagram

A plot of fixed points vs parameter value, showing stability (solid = stable, dashed = unstable). The logistic map's bifurcation diagram reveals the period-doubling route to chaos and the famous **Feigenbaum constant** δ ≈ 4.669 (universal ratio between successive bifurcation intervals).

---

## Partial Differential Equations (PDEs)

PDEs involve functions of multiple variables and their partial derivatives.

### Classification of Second-Order Linear PDEs

For Au_xx + 2Bu_xy + Cu_yy + ... = 0:

| Type | Condition | Behaviour | Example |
|------|-----------|-----------|---------|
| **Elliptic** | B² − AC < 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC > 0 | Wave propagation, preserves sharp features | Wave equation: u_tt = c²u_xx |

### The Heat Equation

∂u/∂t = α ∂²u/∂x²

Models heat diffusion, population spread, option pricing (Black-Scholes).

| Property | Statement |
|----------|-----------|
| Smoothing | Solutions become smooth instantly, even from discontinuous initial data |
| Maximum principle | Maximum temperature occurs at boundary or initial time |
| Time-reversibility | Irreversible — cannot run backwards |

### The Wave Equation

∂²u/∂t² = c² ∂²u/∂x²

Models vibrating strings, sound, electromagnetic waves.

| Property | Statement |
|----------|-----------|
| Propagation | Disturbances travel at speed c |
| Reversibility | Time-reversible |
| d'Alembert solution | u(x,t) = f(x−ct) + g(x+ct) (superposition of left/right waves) |

### Laplace's Equation

∇²u = ∂²u/∂x² + ∂²u/∂y² = 0

Solutions (harmonic functions) represent steady-state temperature, electrostatic potential, incompressible fluid flow.

| Property | Statement |
|----------|-----------|
| Mean value property | u(x₀) = average of u over any circle centred at x₀ |
| Maximum principle | No interior maxima or minima |
| Uniqueness | Determined entirely by boundary conditions |

---

## Relevance to Machine Learning and Data Science

| DS Concept | Application |
|-----------|-------------|
| ODEs | Neural ODEs (continuous-depth networks), recurrent network dynamics |
| Stability analysis | Training dynamics of gradient descent (is the loss decreasing stably?) |
| Lyapunov functions | Proving convergence of learning algorithms, reinforcement learning stability |
| Chaos | Understanding sensitivity in RNNs (vanishing/exploding gradients), weather prediction |
| Bifurcation | Phase transitions in learning (grokking), regime changes in training dynamics |
| PDEs | Diffusion models (score-based generative models), physics-informed neural networks |
| Heat equation | Diffusion processes in generative modelling, graph Laplacian smoothing |
| Wave equation | Seismic data processing, audio signal modelling |
| Lotka-Volterra | Population dynamics, epidemiology, competing ML agents |
| Phase portraits | Visualising loss landscape dynamics, understanding GAN training |

---

## Summary

| Topic | Core Idea | Key Tool |
|-------|-----------|----------|
| ODEs | Functions and their time derivatives | Characteristic equations, integrating factors |
| Systems of ODEs | Multiple interacting variables | Eigenvalue analysis of Jacobian |
| Phase portraits | Visualising dynamics in state space | Fixed points, nullclines, limit cycles |
| Stability | Will the system return to equilibrium? | Linearisation, Lyapunov functions |
| Chaos | Deterministic unpredictability | Lyapunov exponents, strange attractors |
| Bifurcations | Qualitative changes with parameters | Normal forms, bifurcation diagrams |
| PDEs | Functions of multiple variables | Heat, wave, and Laplace equations |

Dynamical systems theory is the mathematics of change. It explains why some systems settle down, why some oscillate, and why some behave chaotically. For data scientists, it provides tools for understanding training dynamics, designing stable algorithms, modelling time series, and building the next generation of physics-informed machine learning models.
