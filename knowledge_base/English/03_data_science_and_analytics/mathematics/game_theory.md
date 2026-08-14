<!--
---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Game Theory

Game theory is the mathematics of strategic interaction — situations where your outcome depends not just on your own choices, but on the choices of others. From pricing wars between companies to nuclear arms races, from online auctions to evolutionary biology, game theory provides the tools for analysing conflict and cooperation. It has become increasingly relevant to machine learning through multi-agent reinforcement learning, generative adversarial networks (GANs), and mechanism design for online platforms.

---

## Strategic-Form Games

### Definition

A **strategic-form (normal-form) game** consists of:
- A set of players N = {1, 2, ..., n}
- Strategy sets S₁, S₂, ..., Sₙ for each player
- Payoff functions u₁, u₂, ..., uₙ mapping strategy profiles to real numbers

### Example: Prisoner's Dilemma

| | Cooperate (C) | Defect (D) |
|---|---------------|------------|
| **Cooperate (C)** | (−1, −1) | (−3, 0) |
| **Defect (D)** | (0, −3) | (−2, −2) |

| Analysis | Result |
|----------|--------|
| Dominant strategy | Defect (D dominates C for both players) |
| Nash equilibrium | (D, D) with payoff (−2, −2) |
| Social optimum | (C, C) with payoff (−1, −1) |
| Dilemma | Individual rationality leads to collective irrationality |

### More Classic Games

**Battle of the Sexes:**
| | Opera | Football |
|---|-------|----------|
| Opera | (2, 1) | (0, 0) |
| Football | (0, 0) | (1, 2) |

Two Nash equilibria: (Opera, Opera) and (Football, Football).

**Chicken (Hawk-Dove):**
| | Hawk | Dove |
|---|------|------|
| Hawk | (−10, −10) | (5, 0) |
| Dove | (0, 5) | (1, 1) |

Two Nash equilibria: (Hawk, Dove) and (Dove, Hawk).

---

## Dominant Strategies

| Concept | Definition |
|---------|------------|
| **Strictly dominant** | Strategy sᵢ gives higher payoff than any other strategy, regardless of opponents' choices |
| **Weakly dominant** | Strategy sᵢ gives at least as high a payoff as any other, and strictly higher for some opponent profiles |
| **Dominated strategy** | A strategy that is never a best response |

**Iterated elimination of dominated strategies:**
1. Remove any strictly dominated strategies
2. Repeat until no more can be removed
3. If one strategy profile remains, it is the unique Nash equilibrium

---

## Nash Equilibrium

A **Nash equilibrium** is a strategy profile where no player can improve their payoff by unilaterally changing their strategy.

### Definition

(s₁*, s₂*, ..., sₙ*) is a Nash equilibrium if for every player i:

uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) for all sᵢ ∈ Sᵢ

### Finding Nash Equilibria (2×2 Games)

**Best response method:**
1. For each column, underline player 1's best response
2. For each row, underline player 2's best response
3. Cells where both are underlined are Nash equilibria

### Existence (Nash's Theorem)

Every finite game has at least one Nash equilibrium (possibly in mixed strategies).

### Mixed Strategies

A **mixed strategy** is a probability distribution over pure strategies.

| Concept | Definition |
|---------|------------|
| Mixed strategy σᵢ | Probability distribution over Sᵢ |
| Mixed strategy NE | No player can improve expected payoff by changing their mixture |
| Support | Set of pure strategies played with positive probability |

**Worked Example: Matching Pennies**
| | Heads | Tails |
|---|-------|-------|
| Heads | (1, −1) | (−1, 1) |
| Tails | (−1, 1) | (1, −1) |

No pure strategy NE. Mixed NE: both play H and T with probability ½ each.

---

## Minimax Theorem

### Zero-Sum Games

In a **zero-sum game**, one player's gain is exactly the other's loss: u₁ + u₂ = 0.

### Von Neumann's Minimax Theorem

For every finite two-player zero-sum game:

max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)

The **maximin** (best worst-case for player 1) equals the **minimax** (best worst-case for player 2). This common value is the **value of the game**.

### Solving Zero-Sum Games

For a 2×2 zero-sum game with matrix:
| | L | R |
|---|---|---|
| T | a | b |
| B | c | d |

Player 1's optimal mixed strategy: play T with probability p = (d−c)/((a−b)+(d−c))
Game value: v = (ad−bc)/((a−b)+(d−c))

---

## Extensive-Form Games

Games with sequential moves are represented as **game trees**.

### Key Concepts

| Concept | Definition |
|---------|------------|
| **Game tree** | Tree showing all possible sequences of moves |
| **Information set** | Set of nodes a player cannot distinguish |
| **Perfect information** | Every information set is a singleton (all moves observable) |
| **Subgame perfect NE** | Nash equilibrium in every subgame |
| **Backward induction** | Solve from the end of the tree backwards |

### Zermelo's Theorem

In finite, perfect-information, two-player games with no chance: either one player has a winning strategy, or both can force a draw (e.g., chess).

---

## Cooperative Games

In **cooperative games**, players can form binding agreements and coalitions.

### Characteristic Function

A cooperative game is defined by a **characteristic function** v: 2^N → ℝ, where v(S) is the value coalition S can achieve.

| Property | Definition |
|----------|------------|
| **Superadditive** | v(S ∪ T) ≥ v(S) + v(T) for disjoint S, T |
| **Convex** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) for S ⊂ T |

### The Core

The **core** is the set of allocations where no coalition can improve by breaking away:

Core = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) for all S ⊂ N}

The core may be empty — in which case no stable allocation exists.

### Shapley Value

The **Shapley value** provides a unique fair allocation based on marginal contributions:

φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]

| Property | Statement |
|----------|-----------|
| Efficiency | Σ φᵢ = v(N) (all value is distributed) |
| Symmetry | Equal contributors get equal payoffs |
| Dummy player | Non-contributors get zero |
| Additivity | φ(v + w) = φ(v) + φ(w) |

**Interpretation:** Each player's Shapley value is their average marginal contribution across all possible orderings of coalition formation.

### Worked Example

Three players: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.

| Player | Marginal contributions (averaged over orderings) | Shapley value |
|--------|--------------------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56.7 | 37.5 |
| 2 | (100+50+60+60+50+0)/6 | 27.5 |
| 3 | (100+70+60+70+60+0)/6 | 35.0 |

(Calculated precisely using the Shapley formula for each permutation.)

---

## Mechanism Design

**Mechanism design** is "inverse game theory" — instead of analysing given games, design games that produce desired outcomes.

### The Revelation Principle

Any mechanism that achieves a desired outcome can be replaced by a **direct revelation mechanism** where truth-telling is a Nash equilibrium.

### Auction Theory

| Auction Type | Rules | Revenue Equivalence |
|-------------|-------|---------------------|
| **First-price sealed-bid** | Highest bidder wins, pays their bid | All standard auctions yield same expected revenue |
| **Second-price sealed-bid (Vickrey)** | Highest bidder wins, pays second-highest bid | (under independent private values) |
| **English (ascending)** | Price rises; first to accept wins | — |
| **Dutch (descending)** | Price falls; first to accept wins | — |

### Vickrey Auction (Second-Price)

**Dominant strategy:** Bid your true value.

| Property | Statement |
|----------|-----------|
| Truthful bidding | Weakly dominant strategy |
| Efficiency | Item goes to highest-value bidder |
| Revenue | Same expected revenue as first-price (Revenue Equivalence Theorem) |

### Optimal Auction Design (Myerson)

The revenue-maximising auction:
- Allocates to the bidder with highest **virtual valuation**
- Sets a reserve price
- Virtual valuation: ψ(v) = v − (1−F(v))/f(v)

---

## Connections to Machine Learning

### Generative Adversarial Networks (GANs)

GANs are a two-player game between a generator G and a discriminator D:

min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]

| Game Theory Concept | GAN Equivalent |
|--------------------|-----------------|
| Two-player zero-sum game | Generator vs discriminator |
| Nash equilibrium | G generates real data, D outputs ½ everywhere |
| Minimax | The GAN objective function |
| Mode collapse | Failure to reach equilibrium |

### Multi-Agent Reinforcement Learning (MARL)

| Concept | MARL Application |
|---------|-----------------|
| Nash equilibrium | Stable policies in multi-agent settings |
| Minimax | Robust policies against adversarial opponents |
| Cooperative games | Coalition formation, task allocation |
| Shapley value | Credit assignment (which agent contributed what?) |
| Mechanism design | Designing incentives in multi-agent systems |
| Fictitious play | Learning algorithm converging to Nash equilibrium |

### Other ML Connections

| Application | Game Theory Tool |
|-------------|-----------------|
| Ad auction design (Google, Facebook) | Mechanism design, auction theory |
| Marketplace design (Uber, Airbnb) | Matching theory, mechanism design |
| Adversarial robustness | Zero-sum games between attacker and defender |
| Fair division | Shapley value, envy-free allocation |
| Federated learning | Cooperative game theory for contribution measurement |
| Recommendation systems | Mechanism design for truthful preference elicitation |

---

## Summary

| Concept | Core Idea | Key Result |
|---------|-----------|------------|
| Strategic-form games | Players, strategies, payoffs | Game matrix representation |
| Dominant strategies | Best regardless of others | Iterated elimination |
| Nash equilibrium | No profitable unilateral deviation | Exists in every finite game |
| Mixed strategies | Randomise over actions | Nash's existence theorem |
| Minimax | Best worst-case (zero-sum) | Von Neumann's minimax theorem |
| Extensive-form | Sequential moves | Backward induction, subgame perfection |
| Cooperative games | Binding coalitions | Core, Shapley value |
| Mechanism design | Design games for outcomes | Revelation principle, optimal auctions |
| Auction theory | Selling via competition | Revenue equivalence, Vickrey auction |

Game theory is the mathematics of strategic thinking. In a world increasingly populated by interacting AI agents, automated marketplaces, and adversarial systems, game theory provides the essential toolkit for predicting behaviour, designing mechanisms, and building robust multi-agent systems. For data scientists, it explains how GANs work, how online auctions generate billions in revenue, and how to build AI systems that perform well in competitive environments.
