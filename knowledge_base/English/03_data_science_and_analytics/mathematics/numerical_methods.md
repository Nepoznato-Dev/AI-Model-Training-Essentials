---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
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

# Numerical Methods

Numerical methods are the bridge between mathematical theory and practical computation. While pure mathematics proves that solutions exist, numerical methods actually compute approximate answers to finite precision. Every machine learning model, physics simulation, and data analysis pipeline ultimately relies on numerical computation. Understanding these methods — their accuracy, stability, and limitations — is essential for building reliable software.

---

## Floating-Point Arithmetic

Computers represent real numbers with finite precision. The **IEEE 754 standard** defines how floating-point numbers are stored and manipulated.

### IEEE 754 Formats

| Format | Bits | Exponent | Mantissa | Approximate Decimal Digits | Range |
|--------|------|----------|----------|---------------------------|-------|
| Half (fp16) | 16 | 5 | 10 | 3.3 | ±6.5 × 10⁴ |
| Single (fp32) | 32 | 8 | 23 | 7.2 | ±3.4 × 10³⁸ |
| Double (fp64) | 64 | 11 | 52 | 15.9 | ±1.8 × 10³⁰⁸ |

### Machine Epsilon

**Machine epsilon** (ε_mach) is the smallest number such that 1 + ε_mach > 1 in floating-point.

| Format | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9.8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1.2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2.2 × 10⁻¹⁶ |

### Common Pitfalls

| Pitfall | Example | Consequence |
|---------|---------|-------------|
| **Catastrophic cancellation** | Computing (1 + x) − 1 for small x | Loss of significant digits |
| **Absorption** | 10⁸ + 1 = 10⁸ in fp32 | Small values lost in large sums |
| **Non-associativity** | (a + b) + c ≠ a + (b + c) | Sum order matters |
| **Division by near-zero** | 1 / 10⁻³⁰⁰ → overflow | Infinity or NaN |

### Mitigation Strategies

| Strategy | Description |
|----------|-------------|
| **Kahan summation** | Compensated summation to reduce absorption error |
| **Kahan-Babuska-Neumaier** | Improved version of Kahan summation |
| **Sorted summation** | Sum small numbers first to avoid absorption |
| **Double-double arithmetic** | Use pairs of doubles for extended precision |
| **Conditioning analysis** | Understand if the problem itself amplifies errors |

---

## Root Finding

Finding x such that f(x) = 0.

### Bisection Method

| Property | Value |
|----------|-------|
| Requires | f continuous, f(a) and f(b) have opposite signs |
| Convergence | Linear (error halves each step) |
| Guaranteed? | Yes — always converges |
| Iterations for d digits | ≈ d / log₁₀(2) ≈ 3.32d |

**Algorithm:**
1. Start with interval [a, b] where f(a) · f(b) < 0
2. Compute midpoint c = (a + b) / 2
3. If f(c) = 0 or |b − a| < tolerance, stop
4. If f(a) · f(c) < 0, set b = c; else set a = c
5. Repeat

### Newton-Raphson Method

| Property | Value |
|----------|-------|
| Requires | f differentiable, f'(x) ≠ 0 at root |
| Convergence | Quadratic (near root) |
| Guaranteed? | No — may diverge or cycle |
| Update rule | x_{n+1} = x_n − f(x_n) / f'(x_n) |

**Worked Example:** Find √2 by solving f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1.5
- x₁ = 1.5 − (2.25 − 2) / 3 = 1.5 − 0.0833 = 1.4167
- x₂ = 1.4167 − (2.0069 − 2) / 2.8333 = 1.4142
- x₃ = 1.41421356... (correct to 8 decimal places)

### Secant Method

Like Newton's method but approximates the derivative:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))

| Property | Value |
|----------|-------|
| Convergence | Superlinear (order ≈ 1.618, the golden ratio) |
| Requires | Two initial guesses (no derivative needed) |

### Comparison of Root-Finding Methods

| Method | Convergence | Derivative Needed? | Guaranteed? | Cost per Step |
|--------|-------------|-------------------|-------------|---------------|
| Bisection | Linear (1) | No | Yes | 1 function eval |
| Newton-Raphson | Quadratic (2) | Yes | No | 2 function evals |
| Secant | Superlinear (1.618) | No | No | 1 function eval |
| Brent's method | Superlinear | No | Yes | Varies |

**Brent's method** combines bisection (guaranteed convergence) with secant/inverse quadratic interpolation (fast convergence). It is the default root-finder in most numerical libraries.

---

## Numerical Integration (Quadrature)

Computing ∫ₐᵇ f(x) dx approximately.

### Methods

| Method | Formula | Error | Order |
|--------|---------|-------|-------|
| **Rectangle (midpoint)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Trapezoidal** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **Simpson's 1/3** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Simpson's 3/8** | Uses 4 equally spaced points | O(h⁴) | 4 |
| **Gaussian quadrature** | Optimal node placement | O(h²ⁿ) | n points |

### Composite Rules

For n subintervals of width h = (b−a)/n:

| Rule | Composite Formula | Error |
|------|-------------------|-------|
| Composite Trapezoidal | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Composite Simpson's | h/3[f(a) + 4Σf(odd) + 2Σf(even) + f(b)] | O(h⁴) |

**Worked Example:** Approximate ∫₀¹ e^(−x²) dx using composite trapezoidal with n = 4.
- h = 0.25, points: 0, 0.25, 0.5, 0.75, 1
- f(0) = 1, f(0.25) = 0.9394, f(0.5) = 0.7788, f(0.75) = 0.5698, f(1) = 0.3679
- T = 0.25[1/2 + 0.9394 + 0.7788 + 0.5698 + 0.3679/2] = 0.25[1/2 + 2.2880 + 0.1840] = 0.7430
- True value: ≈ 0.7468 (error ≈ 0.5%)

### Adaptive Quadrature

Automatically subdivides intervals where the function varies rapidly, using fewer points where it's smooth. This is what `scipy.integrate.quad` uses (based on QUADPACK).

---

## Interpolation

Estimating values between known data points.

### Methods

| Method | Description | Smoothness | Oscillation |
|--------|-------------|------------|-------------|
| **Nearest neighbour** | Use closest data point | Discontinuous | None |
| **Linear** | Connect points with straight lines | C⁰ (continuous) | None |
| **Polynomial (Lagrange)** | Single polynomial through all points | C^∞ | Severe for many points (Runge's phenomenon) |
| **Cubic spline** | Piecewise cubic, smooth at joints | C² | Minimal |
| **Radial basis function** | Weighted sum of radial kernels | Depends on kernel | Low |

### Lagrange Interpolation

Given n+1 points (x₀, y₀), ..., (xₙ, yₙ), the unique polynomial of degree ≤ n passing through all points:

P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)

**Runge's phenomenon:** High-degree polynomial interpolation at equally spaced points can oscillate wildly near the edges. Mitigated by using Chebyshev nodes or splines.

### Cubic Splines

Piecewise cubic polynomials that are C² continuous (continuous second derivatives).

| Type | Boundary Condition |
|------|-------------------|
| Natural spline | S''(x₀) = S''(xₙ) = 0 |
| Clamped spline | S'(x₀) and S'(xₙ) specified |
| Not-a-knot | Third derivative continuous at x₁ and xₙ₋₁ |

---

## ODE Solvers

Solving ordinary differential equations dy/dt = f(t, y) numerically.

### Euler's Method

The simplest ODE solver.

**Update:** y_{n+1} = y_n + h · f(t_n, y_n)

| Property | Value |
|----------|-------|
| Order | 1 (error per step: O(h²), global: O(h)) |
| Stability | Conditionally stable (small h required) |
| Cost | 1 function evaluation per step |

### Runge-Kutta Methods

| Method | Order | Stages | Notes |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Simplest |
| **Midpoint** | 2 | 2 | Better accuracy |
| **Heun's (RK2)** | 2 | 2 | Predictor-corrector |
| **Classic RK4** | 4 | 4 | Standard workhorse |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Adaptive step size (used in ode45) |

### Classic RK4 (4th-order Runge-Kutta)

k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6

| Property | Value |
|----------|-------|
| Order | 4 (global error: O(h⁴)) |
| Cost | 4 function evaluations per step |
| Stability | Much better than Euler |
| Usage | Default for non-stiff ODEs |

### Stiff ODEs

A **stiff** ODE has components that vary on vastly different time scales. Explicit methods (Euler, RK4) require impractically small step sizes.

| Method | Type | Stability |
|--------|------|-----------|
| Implicit Euler | Implicit | A-stable (unconditionally stable) |
| Backward Differentiation Formula (BDF) | Implicit | A-stable (up to order 5) |
| Implicit Runge-Kutta | Implicit | L-stable variants exist |
| LSODA | Automatic | Switches between stiff/non-stiff |

---

## Numerical Stability and Conditioning

### Condition Number

The **condition number** measures how much the output of a problem changes relative to small changes in the input.

For a linear system Ax = b: κ(A) = ||A|| · ||A⁻¹||

| κ(A) | Interpretation |
|-------|---------------|
| ≈ 1 | Well-conditioned |
| 10³ | Mildly sensitive |
| 10⁸ | Ill-conditioned (lose ~8 digits of accuracy) |
| → ∞ | Singular (no unique solution) |

### Stability of Algorithms

An algorithm is **numerically stable** if small perturbations in input lead to small perturbations in output (relative to the condition number of the problem).

| Algorithm | Stable? | Notes |
|-----------|---------|-------|
| Gaussian elimination with partial pivoting | Yes | Standard approach |
| Computing eigenvalues via QR | Yes | Backward stable |
| Naive summation (large + small first) | No | Use Kahan summation |
| Computing variance as E[X²] − (E[X])² | Potentially no | Use Welford's online algorithm |

### Welford's Online Algorithm

Numerically stable computation of running mean and variance:

```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

This avoids the catastrophic cancellation that occurs in the naive two-pass formula.

---

## Relevance to Machine Learning and Data Science

| Numerical Method | Application |
|-----------------|-------------|
| Floating-point (fp16/fp32/bf16) | Mixed-precision training, model quantisation, memory efficiency |
| Root finding | Maximum likelihood estimation (finding where gradient = 0) |
| Numerical integration | Bayesian inference (computing marginal likelihoods), expected values |
| Interpolation | Smoothing, imputation, surrogate models, activation functions |
| ODE solvers | Neural ODEs, continuous-time RNNs, population dynamics, physics-informed ML |
| Condition number | Understanding numerical issues in linear regression, normal equations |
| Stable summation | Computing loss functions, batch normalisation statistics |
| RK4 / adaptive solvers | Simulating dynamical systems, training continuous-depth networks |

---

## Summary

| Topic | Core Idea | Key Method |
|-------|-----------|------------|
| Floating-point | Finite precision representation | IEEE 754, Kahan summation |
| Root finding | Solve f(x) = 0 | Bisection, Newton-Raphson, Brent's |
| Numerical integration | Approximate ∫f(x)dx | Trapezoidal, Simpson's, Gaussian quadrature |
| Interpolation | Estimate between data points | Cubic splines, Lagrange, RBF |
| ODE solvers | Solve dy/dt = f(t,y) | Euler, RK4, adaptive methods |
| Stability | Sensitivity to rounding errors | Condition number, stable algorithms |

Numerical methods are where mathematics meets reality. No computer can represent most real numbers exactly, no derivative is computed symbolically in practice, and no integral is evaluated in closed form for real-world problems. Understanding numerical methods lets you choose the right algorithm, predict its accuracy, and avoid the subtle bugs that arise from finite-precision arithmetic.
