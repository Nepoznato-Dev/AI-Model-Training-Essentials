---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
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
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Information Theory

Information theory, founded by Claude Shannon in 1948, quantifies information itself. How much does a message tell you? How much can you compress data? How fast can you communicate over a noisy channel? These questions have precise mathematical answers. Beyond communication, information theory has become foundational to machine learning — cross-entropy is the default loss function for classification, KL divergence measures distribution similarity, and mutual information drives feature selection.

---

## Entropy

**Entropy** measures the average uncertainty or "surprise" of a random variable.

### Shannon Entropy (Discrete)

For a discrete random variable X with probability mass function p(x):

H(X) = −Σₓ p(x) log₂ p(x)

Units: **bits** (when using log₂) or **nats** (when using ln).

| Distribution | Entropy | Intuition |
|-------------|---------|-----------|
| Fair coin (p = 0.5, 0.5) | 1 bit | Maximum uncertainty for binary outcome |
| Biased coin (p = 0.9, 0.1) | 0.469 bits | Less surprising — mostly heads |
| Deterministic (p = 1, 0) | 0 bits | No uncertainty at all |
| Fair die (6 sides) | 2.585 bits | More outcomes = more uncertainty |
| Uniform over n outcomes | log₂(n) bits | Maximum entropy for n outcomes |

### Properties of Entropy

| Property | Statement |
|----------|-----------|
| Non-negativity | H(X) ≥ 0 |
| Maximum | H(X) ≤ log₂(\|X\|) with equality for uniform distribution |
| Chain rule | H(X, Y) = H(X) + H(Y \| X) |
| Conditioning reduces | H(X \| Y) ≤ H(X) |
| Concavity | H is a concave function of the probability distribution |

### Differential Entropy (Continuous)

For a continuous random variable X with density p(x):

h(X) = −∫ p(x) log p(x) dx

Unlike discrete entropy, differential entropy can be **negative**.

| Distribution | Differential Entropy |
|-------------|---------------------|
| Uniform on [a,b] | log(b − a) |
| Normal N(μ, σ²) | (1/2) log(2πeσ²) |
| Exponential(λ) | 1 − ln(λ) |

---

## Joint, Conditional, and Mutual Information

### Joint Entropy

H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)

Measures total uncertainty of the pair (X, Y).

### Conditional Entropy

H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)

Measures remaining uncertainty about Y after observing X.

### Mutual Information

I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]

Measures how much knowing X tells you about Y (and vice versa).

| Property | Statement |
|----------|-----------|
| Non-negativity | I(X; Y) ≥ 0 |
| Symmetry | I(X; Y) = I(Y; X) |
| Relation to entropy | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Relation to joint | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Independence | I(X; Y) = 0 iff X and Y are independent |
| Self-information | I(X; X) = H(X) |

### Visual: The Entropy Diagram

```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## KL Divergence

The **Kullback-Leibler (KL) divergence** measures how different one distribution is from another.

D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]

| Property | Statement |
|----------|-----------|
| Non-negativity | D_KL(P \|\| Q) ≥ 0 (Gibbs' inequality) |
| Identity | D_KL(P \|\| Q) = 0 iff P = Q |
| Asymmetry | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) in general |
| Not a metric | Fails symmetry and triangle inequality |

**Interpretation:** D_KL(P || Q) is the extra number of bits needed to encode data from P using a code optimised for Q.

### Relationship to Other Quantities

| Relationship | Formula |
|-------------|---------|
| Cross-entropy | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Mutual information | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| Conditional KL | D_KL(P(Y\|X) \|\| Q(Y\|X)) averaged over X |

---

## Cross-Entropy

**Cross-entropy** between distributions P and Q:

H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)

### Cross-Entropy as a Loss Function

In classification, P is the true distribution (one-hot encoded label) and Q is the model's predicted distribution.

**Binary cross-entropy (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]

**Categorical cross-entropy:**
L = −Σᵢ yᵢ log(ŷᵢ)

| Scenario | y (true) | ŷ (predicted) | Loss |
|----------|----------|---------------|------|
| Correct, confident | 1 | 0.95 | 0.051 |
| Correct, uncertain | 1 | 0.55 | 0.598 |
| Wrong, confident | 1 | 0.05 | 2.996 |
| Wrong, uncertain | 1 | 0.45 | 0.799 |

Minimising cross-entropy is equivalent to minimising KL divergence from the true distribution — which is why it works so well as a loss function.

---

## Channel Capacity

### Communication Channel Model

```
X → [Channel] → Y
```

- X: input random variable
- Y: output random variable
- Channel: defined by conditional probabilities p(y|x)

### Shannon's Noisy Channel Coding Theorem

For a channel with capacity C, if the transmission rate R < C, there exists a coding scheme that achieves arbitrarily small error probability. If R > C, reliable communication is impossible.

**Channel capacity:**
C = max_{p(x)} I(X; Y)

### Important Channel Examples

| Channel | Description | Capacity |
|---------|-------------|----------|
| **Binary symmetric (BSC)** | Flips each bit with probability p | 1 − H(p) bits |
| **Binary erasure (BEC)** | Erases each bit with probability ε | 1 − ε bits |
| **Gaussian (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bits |
| **Noiseless binary** | Perfect transmission | 1 bit |

---

## Source Coding and Compression

### Source Coding Theorem

The average number of bits needed to encode a source is bounded below by its entropy:
L ≥ H(X)

An optimal code achieves L ≈ H(X).

### Huffman Coding

A **prefix-free** code that assigns shorter codes to more probable symbols.

| Symbol | Probability | Huffman Code | Length |
|--------|-------------|-------------|--------|
| A | 0.5 | 0 | 1 |
| B | 0.25 | 10 | 2 |
| C | 0.125 | 110 | 3 |
| D | 0.125 | 111 | 3 |

Average length: 0.5(1) + 0.25(2) + 0.125(3) + 0.125(3) = 1.75 bits/symbol
Entropy: H = 1.75 bits/symbol (optimal in this case!)

### Lossless vs Lossy Compression

| Type | Principle | Examples | Limit |
|------|-----------|----------|-------|
| **Lossless** | Remove statistical redundancy | ZIP, PNG, FLAC | Entropy rate H(X) |
| **Lossy** | Remove perceptually irrelevant information | JPEG, MP3, H.264 | Rate-distortion function R(D) |

**Rate-distortion theory:** For lossy compression with maximum distortion D, the minimum rate is R(D) = min I(X; X̂) subject to E[d(X, X̂)] ≤ D.

---

## Connections to Other Fields

### Information Theory and Thermodynamics

| Concept | Information Theory | Thermodynamics |
|---------|-------------------|----------------|
| Entropy | Shannon entropy H(X) | Boltzmann entropy S = k_B ln W |
| Maximum entropy | Uniform distribution | Thermal equilibrium |
| KL divergence | Distribution difference | Free energy difference |
| Mutual information | Shared information | Correlations in physical systems |

The mathematical forms are identical — Shannon deliberately borrowed the term "entropy" from statistical mechanics.

### Information Theory and Statistics

| Concept | Application |
|---------|-------------|
| Maximum likelihood | Equivalent to minimising KL divergence from empirical to model distribution |
| Fisher information | Curvature of KL divergence; lower bound on estimator variance (Cramér-Rao) |
| Minimum description length (MDL) | Model selection by minimising total encoding length |
| AIC / BIC | Approximate KL-based model selection criteria |

---

## Relevance to Machine Learning and Data Science

| IT Concept | ML Application |
|-----------|----------------|
| Cross-entropy loss | Default classification loss (binary and multi-class) |
| KL divergence | VAE loss (regularisation term), distribution matching, distillation |
| Mutual information | Feature selection (MIFS), representation learning (InfoMax), disentanglement |
| Entropy | Decision tree splitting criterion (information gain), exploration in RL (maximum entropy RL) |
| Channel capacity | Communication complexity, understanding generalisation bounds |
| Source coding | Data compression for storage and transmission, efficient encoding |
| Maximum entropy | MaxEnt classifiers, prior selection in Bayesian inference |
| Rate-distortion | Understanding trade-offs in lossy compression, quantisation in neural networks |
| Fisher information | Natural gradient descent, understanding parameter sensitivity |
| MDL / AIC / BIC | Model selection, preventing overfitting |

---

## Summary

| Quantity | Formula (discrete) | Meaning |
|----------|-------------------|---------|
| Entropy H(X) | −Σ p(x) log p(x) | Average uncertainty |
| Joint entropy H(X,Y) | −Σ p(x,y) log p(x,y) | Total uncertainty of pair |
| Conditional entropy H(Y\|X) | H(X,Y) − H(X) | Remaining uncertainty about Y given X |
| Mutual information I(X;Y) | H(X) − H(X\|Y) | Information shared between X and Y |
| KL divergence D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | "Distance" between distributions |
| Cross-entropy H(P,Q) | −Σ P(x) log Q(x) | Encoding cost using wrong distribution |
| Channel capacity C | max I(X;Y) | Maximum reliable communication rate |

Information theory provides the fundamental limits of what can be learned, compressed, and communicated. For machine learning practitioners, it explains why cross-entropy works as a loss function, how to measure the quality of learned representations, and how to think about the trade-off between model complexity and data fit. Shannon's insights from 1948 remain as relevant to modern AI as they are to telecommunications.
