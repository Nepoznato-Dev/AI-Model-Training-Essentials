<!--
---
# Metadata
title: "Real Analysis"
description: "Sequences and series, limits, continuity, differentiability, Riemann and Lebesgue integration, metric spaces, uniform convergence, and measure theory"
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
    changes: "Initial deep-dive into real analysis"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [real-analysis, sequences, series, limits, continuity, integration, metric-spaces, measure-theory, convergence]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Real Analysis

Real analysis is the rigorous foundation of calculus. While introductory calculus teaches you how to compute derivatives and integrals, real analysis asks *why* these techniques work — and when they fail. It provides the precise definitions of limits, continuity, convergence, and integration that underpin probability theory, functional analysis, optimization, and the theoretical guarantees behind machine learning algorithms.

---

## Sequences and Series

### Sequences

A **sequence** is an ordered list of real numbers (aₙ)ₙ₌₁^∞. The central question is: does the sequence **converge** to a limit?

**Definition of convergence:** A sequence (aₙ) converges to L if for every ε > 0, there exists N such that for all n > N: |aₙ − L| < ε.

| Concept | Definition | Example |
|---------|------------|---------|
| **Convergent** | lim aₙ = L exists and is finite | aₙ = 1/n → 0 |
| **Divergent** | Does not converge | aₙ = (−1)ⁿ oscillates |
| **Divergent to ∞** | aₙ grows without bound | aₙ = n² → ∞ |
| **Bounded** | \|aₙ\| ≤ M for some M | Every convergent sequence is bounded |
| **Monotone** | Either always non-decreasing or non-increasing | aₙ = 1 − 1/n is increasing |
| **Cauchy sequence** | ∀ε > 0, ∃N: ∀m,n > N, \|aₘ − aₙ\| < ε | In ℝ, Cauchy ⟺ convergent |

**Key theorems:**
- **Monotone Convergence Theorem:** Every bounded monotone sequence converges
- **Bolzano-Weierstrass Theorem:** Every bounded sequence has a convergent subsequence
- **Completeness of ℝ:** Every Cauchy sequence in ℝ converges (this distinguishes ℝ from ℚ)

### Series

A **series** is the sum of a sequence: Σₙ₌₁^∞ aₙ. The series converges if the sequence of partial sums Sₙ = Σₖ₌₁ⁿ aₖ converges.

### Convergence Tests

| Test | Condition | Conclusion |
|------|-----------|------------|
| **Divergence test** | lim aₙ ≠ 0 | Series diverges |
| **Comparison test** | 0 ≤ aₙ ≤ bₙ and Σbₙ converges | Σaₙ converges |
| **Ratio test** | lim \|aₙ₊₁/aₙ\| = L | Converges if L < 1, diverges if L > 1 |
| **Root test** | lim sup \|aₙ\|^(1/n) = L | Converges if L < 1, diverges if L > 1 |
| **Integral test** | aₙ = f(n), f decreasing, positive | Σaₙ converges iff ∫f(x)dx converges |
| **Alternating series** | aₙ decreasing, lim aₙ = 0, alternating signs | Series converges |
| **Absolute convergence** | Σ\|aₙ\| converges | Σaₙ converges (and rearrangements give same sum) |
| **Conditional convergence** | Σaₙ converges but Σ\|aₙ\| diverges | Rearrangements can give any sum (Riemann) |

### Important Series

| Series | Sum | Condition |
|--------|-----|-----------|
| Geometric: Σ rⁿ | 1/(1−r) | \|r\| < 1 |
| p-series: Σ 1/nᵖ | Converges | p > 1 |
| Harmonic: Σ 1/n | Diverges (= ∞) | — |
| Exponential: Σ xⁿ/n! | eˣ | All x |
| Taylor for ln(1+x): Σ (−1)ⁿ⁺¹xⁿ/n | ln(1+x) | −1 < x ≤ 1 |

---

## Limits and Continuity

### Limits of Functions

**Definition:** lim_{x→c} f(x) = L means: for every ε > 0, there exists δ > 0 such that 0 < |x − c| < δ implies |f(x) − L| < ε.

This is the **ε-δ definition** — the rigorous version of "f(x) approaches L as x approaches c."

### Continuity

A function f is **continuous at c** if lim_{x→c} f(x) = f(c). Equivalently: for every ε > 0, there exists δ > 0 such that |x − c| < δ implies |f(x) − f(c)| < ε.

**Types of discontinuity:**

| Type | Description | Example |
|------|-------------|---------|
| Removable | Limit exists but ≠ f(c) | f(x) = sin(x)/x at x = 0 |
| Jump | Left and right limits exist but differ | Step function |
| Infinite | Limit is ±∞ | f(x) = 1/x² at x = 0 |
| Oscillating | Limit does not exist | f(x) = sin(1/x) at x = 0 |

### Key Theorems for Continuous Functions

| Theorem | Statement |
|---------|-----------|
| **Intermediate Value Theorem** | If f is continuous on [a,b] and f(a) < k < f(b), then ∃c ∈ (a,b): f(c) = k |
| **Extreme Value Theorem** | If f is continuous on [a,b], f attains its maximum and minimum on [a,b] |
| **Boundedness Theorem** | If f is continuous on [a,b], f is bounded on [a,b] |
| **Uniform Continuity** | f is uniformly continuous on [a,b] if f is continuous on [a,b] (Heine-Cantor) |

**Worked Example (IVT):** Show x³ + x − 1 = 0 has a solution in (0, 1).
- Let f(x) = x³ + x − 1. f is continuous (polynomial).
- f(0) = −1 < 0 and f(1) = 1 > 0.
- By IVT, ∃c ∈ (0,1): f(c) = 0.

---

## Differentiation

### Definition

f'(c) = lim_{h→0} (f(c+h) − f(c)) / h

If this limit exists, f is **differentiable** at c.

### Differentiability vs Continuity

| Relationship | Statement |
|--------------|-----------|
| Differentiable → Continuous | If f is differentiable at c, f is continuous at c |
| Continuous ↛ Differentiable | f(x) = \|x\| is continuous at 0 but not differentiable there |
| Nowhere differentiable | Weierstrass function: continuous everywhere, differentiable nowhere |

### Key Results

| Theorem | Statement |
|---------|-----------|
| **Mean Value Theorem** | If f is continuous on [a,b] and differentiable on (a,b), ∃c: f'(c) = (f(b)−f(a))/(b−a) |
| **Rolle's Theorem** | Special case of MVT when f(a) = f(b): ∃c: f'(c) = 0 |
| **L'Hôpital's Rule** | If lim f/g = 0/0 or ∞/∞, then lim f/g = lim f'/g' (when the latter exists) |
| **Taylor's Theorem** | f(x) = Σₖ₌₀ⁿ f⁽ᵏ⁾(a)/k! · (x−a)ᵏ + Rₙ(x) with explicit remainder |

---

## Integration

### Riemann Integration

The **Riemann integral** defines ∫ₐᵇ f(x)dx as the limit of Riemann sums.

**Construction:**
1. Partition [a,b] into subintervals: P = {x₀, x₁, ..., xₙ}
2. Choose sample points tᵢ ∈ [xᵢ₋₁, xᵢ]
3. Riemann sum: S(P,f) = Σᵢ f(tᵢ)(xᵢ − xᵢ₋₁)
4. If the limit of S(P,f) exists as the mesh → 0, f is Riemann integrable

**Riemann integrability criteria:**

| Condition | Integrable? |
|-----------|-------------|
| Continuous on [a,b] | Yes |
| Bounded with finitely many discontinuities | Yes |
| Monotone on [a,b] | Yes |
| Dirichlet function (1 on ℚ, 0 on irrationals) | No |

### The Fundamental Theorem of Calculus

| Part | Statement |
|------|-----------|
| **Part 1** | If f is continuous on [a,b], then F(x) = ∫ₐˣ f(t)dt is differentiable and F'(x) = f(x) |
| **Part 2** | If F' = f and f is Riemann integrable, then ∫ₐᵇ f(x)dx = F(b) − F(a) |

### Lebesgue Integration

The Riemann integral has limitations — it cannot integrate many functions that arise in analysis and probability. The **Lebesgue integral** extends integration to a much broader class of functions.

**Key idea:** Instead of partitioning the domain (x-axis), partition the range (y-axis).

| Aspect | Riemann Integral | Lebesgue Integral |
|--------|-----------------|-------------------|
| Approach | Partition domain (x-axis) | Partition range (y-axis) |
| Integrates | Continuous, piecewise continuous | Measurable functions |
| Limit theorems | Weak | Powerful (Dominated Convergence, Monotone Convergence) |
| Handles | "Nice" functions | Functions with dense discontinuities |
| Foundation of | Classical calculus | Modern probability theory |

**Lebesgue's criterion:** f is Riemann integrable on [a,b] iff f is bounded and continuous almost everywhere (the set of discontinuities has measure zero).

---

## Metric Spaces

A **metric space** generalises the notion of "distance" to abstract sets.

### Definition

A **metric space** (X, d) is a set X with a distance function d: X × X → ℝ satisfying:

| Axiom | Statement |
|-------|-----------|
| Non-negativity | d(x,y) ≥ 0 |
| Identity | d(x,y) = 0 iff x = y |
| Symmetry | d(x,y) = d(y,x) |
| Triangle inequality | d(x,z) ≤ d(x,y) + d(y,z) |

### Common Metric Spaces

| Space | Set | Metric | Application |
|-------|-----|--------|-------------|
| ℝⁿ with Euclidean | ℝⁿ | d(x,y) = √Σ(xᵢ−yᵢ)² | Standard geometry |
| ℝⁿ with Manhattan | ℝⁿ | d(x,y) = Σ\|xᵢ−yᵢ\| | Grid-based paths, LASSO |
| ℝⁿ with Chebyshev | ℝⁿ | d(x,y) = max\|xᵢ−yᵢ\| | Chess king distance |
| Discrete metric | Any set | d(x,y) = 1 if x≠y, 0 if x=y | Topology examples |
| Function space C[a,b] | Continuous functions | d(f,g) = max\|f(x)−g(x)\| | Approximation theory |
| Lᵖ space | p-integrable functions | d(f,g) = (∫\|f−g\|ᵖ)^(1/p) | Functional analysis, ML norms |

### Topological Concepts in Metric Spaces

| Concept | Definition | Example |
|---------|------------|---------|
| **Open ball** | B(x,r) = {y : d(x,y) < r} | Open interval (x−r, x+r) in ℝ |
| **Open set** | Every point has a ball contained in the set | (0,1) is open in ℝ |
| **Closed set** | Complement of an open set | [0,1] is closed in ℝ |
| **Closure** | Smallest closed set containing S | Closure of (0,1) = [0,1] |
| **Compact** | Every open cover has a finite subcover | In ℝⁿ: closed and bounded (Heine-Borel) |
| **Complete** | Every Cauchy sequence converges | ℝ is complete; ℚ is not |

---

## Uniform Convergence

A sequence of functions (fₙ) can converge in two ways:

| Type | Definition | Preserves Continuity? |
|------|------------|----------------------|
| **Pointwise** | ∀x: fₙ(x) → f(x) | No |
| **Uniform** | sup\|fₙ(x) − f(x)\| → 0 | Yes |

**Uniform convergence** is stronger: the rate of convergence is the same everywhere.

**Key theorems:**
- Uniform limit of continuous functions is continuous
- Uniform limit of Riemann-integrable functions is Riemann-integrable, and the integral of the limit equals the limit of the integrals
- **Weierstrass M-test:** If |fₙ(x)| ≤ Mₙ for all x and ΣMₙ converges, then Σfₙ converges uniformly

---

## Measure Theory

**Measure theory** generalises the concepts of length, area, and volume.

### Definition

A **measure** on a set X is a function μ: Σ → [0, ∞] (where Σ is a σ-algebra of subsets) satisfying:
- μ(∅) = 0
- **Countable additivity:** μ(∪ᵢ Aᵢ) = Σᵢ μ(Aᵢ) for disjoint Aᵢ

### Lebesgue Measure

The **Lebesgue measure** λ on ℝ extends the notion of length:

| Set | Lebesgue Measure |
|-----|-----------------|
| Interval [a,b] | b − a |
| Single point {x} | 0 |
| Finite set | 0 |
| Countable set (e.g., ℚ) | 0 |
| Cantor set | 0 (uncountable but measure zero) |
| [0,1] ∩ ℚ | 0 |
| [0,1] \ ℚ | 1 |

### Key Concepts

| Concept | Definition |
|---------|------------|
| **Almost everywhere (a.e.)** | A property holds except on a set of measure zero |
| **Measurable function** | Preimage of every open set is measurable |
| **Lebesgue integral** | Integral defined using measure theory |
| **Lᵖ spaces** | Spaces of functions with finite p-th power integral |

### Important Convergence Theorems

These theorems are why Lebesgue integration is preferred in advanced mathematics:

| Theorem | Statement |
|---------|-----------|
| **Monotone Convergence** | If fₙ ↑ f pointwise and fₙ ≥ 0, then ∫fₙ → ∫f |
| **Dominated Convergence** | If fₙ → f pointwise and \|fₙ\| ≤ g (integrable), then ∫fₙ → ∫f |
| **Fatou's Lemma** | ∫lim inf fₙ ≤ lim inf ∫fₙ |

These theorems allow exchanging limits and integrals — something that fails for Riemann integration in general.

---

## Relevance to Machine Learning and Data Science

| Analysis Concept | Application |
|-----------------|-------------|
| Limits and convergence | Understanding when iterative algorithms (gradient descent, EM) converge |
| Continuity | Activation functions must be continuous for backpropagation |
| Differentiability | Gradient-based optimization requires differentiable loss functions |
| Mean Value Theorem | Error bounds in numerical approximation, convergence proofs |
| Metric spaces | Distance functions in clustering (k-means, DBSCAN), nearest neighbours |
| Compactness | Existence proofs for optimal solutions, Heine-Borel in finite-dimensional optimization |
| Uniform convergence | Guaranteeing that approximations (neural network universal approximation) work everywhere |
| Measure theory | Foundation of modern probability (probability is a measure), expected values as Lebesgue integrals |
| Lebesgue integration | Expected value E[X] = ∫X dP is a Lebesgue integral |
| Lᵖ spaces | L¹ (LASSO), L² (Ridge), Lᵖ norms in regularization |
| Dominated Convergence | Proving consistency of estimators, interchanging limits in Bayesian inference |

---

## Summary

| Topic | Core Idea | Key Result |
|-------|-----------|------------|
| Sequences | Ordered lists of numbers | Convergence, Cauchy criterion, Bolzano-Weierstrass |
| Series | Infinite sums | Convergence tests, absolute vs conditional |
| Limits | Rigorous approach to "approaching" | ε-δ definition |
| Continuity | No breaks or jumps | IVT, Extreme Value Theorem |
| Differentiation | Instantaneous rate of change | Mean Value Theorem, Taylor's theorem |
| Riemann Integration | Area under curves | Fundamental Theorem of Calculus |
| Lebesgue Integration | Integration via measure | Dominated/Monotone Convergence |
| Metric Spaces | Abstract distance | Open/closed sets, compactness, completeness |
| Uniform Convergence | Convergence at same rate everywhere | Preserves continuity and integrability |
| Measure Theory | Generalised length/area/volume | Foundation of probability, Lebesgue measure |

Real analysis is where mathematics grows up. It replaces intuitive notions of "approaching," "continuous," and "area" with precise definitions that can be proved and generalised. For data scientists and ML engineers, analysis provides the theoretical guarantees: when does gradient descent converge? When is a loss function well-behaved? When can we exchange limits and expectations? These are not philosophical questions — they determine whether your algorithm works or fails silently.
