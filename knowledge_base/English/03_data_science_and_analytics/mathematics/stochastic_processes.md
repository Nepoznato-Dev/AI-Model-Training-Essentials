<!--
---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Stochastic Processes

A **stochastic process** is a collection of random variables indexed by time (or space). While probability theory studies individual random events, stochastic processes study how randomness evolves over time. They model stock prices, queue lengths, disease spread, language generation, and the training dynamics of machine learning models.

---

## Foundations

### Definition

A stochastic process {X_t : t ∈ T} is a family of random variables defined on a common probability space. T is the **index set** (time):
- **Discrete-time:** T = {0, 1, 2, ...}
- **Continuous-time:** T = [0, ∞)

The **state space** S is the set of possible values X_t can take.

### Key Properties

| Property | Definition |
|----------|------------|
| **Stationarity** | Joint distribution of (X_{t₁}, ..., X_{tₖ}) same as (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Independence** | X_t independent of X_s for t ≠ s |
| **Ergodicity** | Time averages converge to ensemble averages |
| **Markov property** | Future depends only on present, not past |
| **Martingale** | Expected future value equals current value |

---

## Markov Chains

A **Markov chain** is a stochastic process where the future state depends only on the current state (memoryless property).

### Discrete-Time Markov Chains (DTMC)

P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}

The **transition matrix** P has entries p_{ij} = P(go to j | currently at i).

| Property | Statement |
|----------|-----------|
| Row sums | Each row sums to 1: Σⱼ p_{ij} = 1 |
| n-step transition | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Stationary distribution | πP = π (left eigenvector with eigenvalue 1) |

### Classification of States

| Term | Definition |
|------|------------|
| **Recurrent** | Chain returns to state i with probability 1 |
| **Transient** | Non-zero probability of never returning |
| **Absorbing** | p_{ii} = 1 (once entered, never left) |
| **Period** | GCD of return times; period 1 = aperiodic |
| **Communicating** | States i and j can reach each other |

### Stationary Distribution

For an irreducible, positive recurrent Markov chain, the stationary distribution π exists, is unique, and satisfies:

πP = π, Σᵢ πᵢ = 1

**Interpretation:** πᵢ = long-run proportion of time spent in state i.

**Worked Example:** Weather model with states {Sunny, Rainy}.
P = [[0.9, 0.1], [0.5, 0.5]] (rows: from Sunny, from Rainy)

Stationary distribution: πP = π
- π₁ = 0.9π₁ + 0.5π₂
- π₂ = 0.1π₁ + 0.5π₂
- π₁ + π₂ = 1
- Solving: π₁ = 5/6 ≈ 0.833, π₂ = 1/6 ≈ 0.167

### Convergence to Stationarity

For an irreducible, aperiodic, positive recurrent chain:
- Pⁿ → Π (matrix with all rows equal to π) as n → ∞
- **Mixing time:** Number of steps until distribution is close to π
- **Spectral gap:** 1 − |λ₂| (where λ₂ is the second-largest eigenvalue) determines mixing speed

### Continuous-Time Markov Chains (CTMC)

Transitions occur at random times governed by exponential distributions.

| Concept | Description |
|---------|-------------|
| **Rate matrix Q** | q_{ij} ≥ 0 for i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Transition probabilities** | P(t) = e^{Qt} (matrix exponential) |
| **Stationary distribution** | πQ = 0 |
| **Holding time** | Time in state i is Exp(−q_{ii}) |

---

## Random Walks

A **random walk** is a path formed by successive random steps.

### Simple Random Walk

X_n = X_{n-1} + Z_n, where Z_n ∈ {+1, −1} with probabilities p, q = 1−p.

| Property | p = 1/2 (symmetric) | p ≠ 1/2 (biased) |
|----------|---------------------|-------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Returns to origin? | Yes (with probability 1) | No (drifts away) |
| Recurrent? | Yes (in 1D and 2D) | No |

### Random Walk in Higher Dimensions

| Dimension | Recurrent? | Intuition |
|-----------|------------|-----------|
| 1D | Yes | "A drunk man always finds his way home" |
| 2D | Yes | "A drunk bird always finds its way home" |
| 3D+ | No | "A drunk sparrow never finds its way home" |

### Connection to Brownian Motion

Scaling a random walk: let S_n = ΣZ_i. Then as step size → 0 and steps → ∞:
S_{⌊nt⌋} / √n → B(t) (Brownian motion, by Donsker's theorem)

---

## Brownian Motion

**Brownian motion** (Wiener process) B(t) is the continuous-time limit of a random walk.

### Definition

B(t) satisfies:
1. B(0) = 0
2. B(t) has continuous paths
3. Independent increments: B(t) − B(s) is independent of B(s) − B(r) for r < s < t
4. B(t) − B(s) ~ N(0, t − s) (Gaussian increments)

### Key Properties

| Property | Statement |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = min(s, t) |
| Nowhere differentiable | Paths are continuous but have no derivative |
| Fractal dimension | Graph has Hausdorff dimension 3/2 |
| Markov property | Future depends only on current position |
| Martingale | E[B(t) | F_s] = B(s) for s < t |

### Geometric Brownian Motion

S(t) = S(0) exp((μ − σ²/2)t + σB(t))

This is the standard model for stock prices in the Black-Scholes framework.
- μ: drift (expected return)
- σ: volatility

---

## Poisson Processes

A **Poisson process** N(t) counts the number of events occurring in [0, t].

### Definition

N(t) ~ Poisson(λt), where λ is the rate (events per unit time).

| Property | Statement |
|----------|-----------|
| N(0) = 0 | — |
| Independent increments | Events in disjoint intervals are independent |
| Stationary increments | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Inter-arrival times | Exponentially distributed: T_i ~ Exp(λ) |

### Generalisations

| Variant | Description |
|---------|-------------|
| **Non-homogeneous** | Rate λ(t) varies with time |
| **Compound Poisson** | Each event has a random size: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Poisson random measure** | Points in space-time, not just time |
| **Multivariate** | Multiple event types with possible interactions |

---

## Martingales

A **martingale** is a fair game: the expected future value, given all current information, equals the current value.

### Definition

{X_n} is a martingale with respect to filtration {F_n} if:
1. X_n is F_n-measurable (adapted)
2. E[|X_n|] < ∞ (integrable)
3. E[X_{n+1} | F_n] = X_n (fair game)

| Variant | Condition | Interpretation |
|---------|-----------|----------------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Fair game |
| **Submartingale** | E[X_{n+1} | F_n] ≥ X_n | Favourable game (trending up) |
| **Supermartingale** | E[X_{n+1} | F_n] ≤ X_n | Unfavourable game (trending down) |

### Key Theorems

| Theorem | Statement |
|---------|-----------|
| **Optional stopping** | Under conditions, E[X_T] = E[X_0] for a stopping time T |
| **Convergence** | A bounded martingale converges almost surely |
| **Maximal inequality** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob's) |

---

## Monte Carlo Methods

**Monte Carlo methods** use random sampling to estimate deterministic quantities.

### Basic Idea

To estimate E[f(X)] where X ~ P:
1. Draw N samples: x₁, x₂, ..., x_N from P
2. Compute: Î = (1/N) Σᵢ f(xᵢ)
3. By the law of large numbers: Î → E[f(X)] as N → ∞

**Error:** Standard error = σ_f / √N, where σ_f² = Var[f(X)]

### Variance Reduction Techniques

| Technique | Idea | Speedup |
|-----------|------|---------|
| **Importance sampling** | Sample from Q instead of P, weight by P/Q | Can be dramatic |
| **Antithetic variates** | Use pairs (x, −x) to cancel variance | ~2x |
| **Control variates** | Subtract known-expectation function correlated with f | Varies |
| **Stratified sampling** | Divide domain, sample each stratum | Reduces variance |
| **Rao-Blackwell** | Condition on sufficient statistics | Always helps |

---

## Markov Chain Monte Carlo (MCMC)

MCMC constructs a Markov chain whose stationary distribution is the target distribution. After a "burn-in" period, samples approximate draws from the target.

### Metropolis-Hastings Algorithm

| Step | Action |
|------|--------|
| 1 | Current state: x_t |
| 2 | Propose: x* ~ q(x* \| x_t) (proposal distribution) |
| 3 | Acceptance ratio: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Accept with probability α: x_{t+1} = x* (accept) or x_t (reject) |

**Special case — Metropolis algorithm:** Symmetric proposal q(x*|x) = q(x|x*), so α = min(1, π(x*)/π(x_t)).

### Gibbs Sampling

A special case of Metropolis-Hastings where each variable is updated from its full conditional distribution.

For target π(x₁, x₂, ..., xₖ):
1. Sample x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Sample x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Continue for all variables
4. Repeat

| Property | Statement |
|----------|-----------|
| Always accepts | α = 1 (no rejection step) |
| Requires | Ability to sample from each full conditional |
| Convergence | Guaranteed for irreducible, aperiodic chains |

### MCMC Diagnostics

| Diagnostic | Purpose |
|-----------|---------|
| **Trace plot** | Visual check for mixing and stationarity |
| **Autocorrelation** | Measures sample dependence (want low autocorrelation) |
| **Gelman-Rubin (R̂)** | Compare multiple chains; R̂ < 1.05 suggests convergence |
| **Effective sample size** | N_eff = N / (1 + 2Σρₖ); accounts for autocorrelation |
| **Burn-in** | Discard initial samples before chain reaches stationarity |

---

## Relevance to Machine Learning and Data Science

| Stochastic Process | Application |
|-------------------|-------------|
| Markov chains | PageRank (random walk on web graph), text generation (n-gram models), MCMC |
| Random walks | Node2Vec and DeepWalk (graph embeddings), exploration in RL |
| Brownian motion | Stock price modelling, diffusion models in generative AI |
| Poisson processes | Modelling event arrivals (clicks, failures), queueing theory |
| Martingales | Financial mathematics, proving convergence of SGD (stochastic approximation) |
| Monte Carlo | Estimating expected values, Bayesian inference, reinforcement learning (policy evaluation) |
| MCMC (Metropolis-Hastings) | Bayesian posterior sampling, probabilistic programming (Stan, PyMC) |
| Gibbs sampling | Topic models (LDA), Bayesian networks, image denoising |
| MCMC diagnostics | Ensuring reliable inference from probabilistic models |

---

## Summary

| Process | State Space | Time | Key Property |
|---------|-------------|------|--------------|
| Markov chain | Discrete/continuous | Discrete/continuous | Memoryless (Markov property) |
| Random walk | ℤᵈ | Discrete | Sum of i.i.d. steps |
| Brownian motion | ℝ | Continuous | Gaussian increments, continuous paths |
| Poisson process | ℕ | Continuous | Counting process with exponential gaps |
| Martingale | ℝ | Discrete/continuous | Fair game (E[X_{t+1}|F_t] = X_t) |

Stochastic processes are the mathematics of randomness over time. They underpin modern Bayesian inference (MCMC), reinforcement learning (Markov decision processes), generative modelling (diffusion models), financial mathematics, and queueing theory. Understanding these processes gives you the tools to model uncertainty dynamically — not just as a snapshot, but as it evolves.
