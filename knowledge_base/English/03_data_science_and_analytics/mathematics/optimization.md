---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Optimization

Optimization is the mathematics of finding the best solution from a set of feasible solutions. It asks: given a function and constraints, what input minimises (or maximises) the output? Optimization is the engine of machine learning — training a model means minimising a loss function. It appears in operations research, economics, engineering design, and virtually every quantitative field.

---

## Problem Formulation

A general **optimization problem** has the form:

Minimise f(x)
Subject to: gᵢ(x) ≤ 0 (inequality constraints), hⱼ(x) = 0 (equality constraints)

| Term | Meaning |
|------|---------|
| **Objective function** f(x) | The quantity to minimise (or maximise) |
| **Decision variables** x | The values we can control |
| **Feasible region** | Set of all x satisfying all constraints |
| **Global minimum** | Feasible x* with f(x*) ≤ f(x) for all feasible x |
| **Local minimum** | Feasible x* with f(x*) ≤ f(x) for all feasible x in some neighbourhood |
| **Convex problem** | f is convex, feasible region is convex set (local min = global min) |

---

## Linear Programming (LP)

When both the objective and all constraints are **linear**, the problem is a linear program.

### Standard Form

Minimise cᵀx
Subject to: Ax ≤ b, x ≥ 0

where c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.

### Properties

| Property | Statement |
|----------|-----------|
| Convexity | LP is always a convex problem |
| Optimal solution | Always at a vertex (corner point) of the feasible polytope |
| Existence | If feasible region is bounded and non-empty, optimal solution exists |
| Multiple optima | If two vertices are optimal, every point on the edge between them is also optimal |

### The Simplex Method

The **simplex method** (Dantzig, 1947) moves along edges of the feasible polytope from vertex to vertex, always improving the objective, until reaching the optimum.

| Property | Value |
|----------|-------|
| Worst-case time | O(2ⁿ) (exponential — rare in practice) |
| Average-case time | Polynomial for most practical problems |
| Key idea | Move to adjacent vertex with better objective value |

**Algorithm (overview):**
1. Start at a basic feasible solution (vertex of the polytope)
2. Choose an entering variable (one that improves the objective)
3. Choose a leaving variable (maintain feasibility)
4. Pivot: move to the new vertex
5. Repeat until no improving direction exists

### Interior Point Methods

Alternative to simplex: approach the optimum from inside the feasible region.

| Property | Value |
|----------|-------|
| Worst-case time | Polynomial (O(n³·⁵) for some variants) |
| Practical performance | Competitive with simplex on large problems |
| Key idea | Follow a "central path" through the interior |

### Worked LP Example

**Problem:** A factory produces chairs (x₁) and tables (x₂).
- Profit: $30 per chair, $50 per table
- Wood: 2x₁ + 4x₂ ≤ 100 (board feet available)
- Labour: x₁ + 3x₂ ≤ 60 (hours available)
- Maximise: 30x₁ + 50x₂

**Solution (graphical method for 2 variables):**
- Vertices of feasible region: (0,0), (30,0), (40,10), (0,20)
- Evaluate objective at each vertex:
  - (0,0): profit = 0
  - (30,0): profit = 900
  - (40,10): profit = 1700 ← optimal
  - (0,20): profit = 1000
- **Optimal:** x₁ = 40 chairs, x₂ = 10 tables, profit = $1700

---

## Convex Optimization

A problem is **convex** if the objective function is convex and the feasible region is a convex set.

### Convex Sets and Functions

| Concept | Definition |
|---------|------------|
| **Convex set** | For any x, y in the set and t ∈ [0,1]: tx + (1−t)y is also in the set |
| **Convex function** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) for all t ∈ [0,1] |
| **Strictly convex** | Inequality is strict for t ∈ (0,1) and x ≠ y |

**Key property:** For convex optimization, every local minimum is a global minimum.

### Common Convex Functions

| Function | Convex? | Where |
|----------|---------|-------|
| ax + b (linear) | Yes (and concave) | Everywhere |
| x² | Yes | ℝ |
| eˣ | Yes | ℝ |
| −log(x) | Yes | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Yes | ℝⁿ |
| max(f₁, f₂) if f₁, f₂ convex | Yes | Intersection of domains |

### Gradient Descent

The most fundamental optimization algorithm in machine learning.

**Update rule:** x_{k+1} = x_k − α∇f(x_k)

where α > 0 is the **learning rate** (step size).

| Variant | Update Rule | Advantage |
|---------|-------------|-----------|
| **Batch GD** | x ← x − α∇f(x) | Stable convergence |
| **Stochastic GD (SGD)** | x ← x − α∇fᵢ(x) (one sample) | Fast per iteration, escapes local minima |
| **Mini-batch SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Balance between batch and stochastic |
| **Momentum** | v ← βv − α∇f(x); x ← x + v | Accelerates through flat regions |
| **Adam** | Adaptive learning rates per parameter | Works well out of the box for deep learning |
| **RMSprop** | Scale learning rate by running average of gradient magnitude | Good for RNNs |

### Convergence Rates

| Method | Convex f | Strongly Convex f |
|--------|----------|-------------------|
| Gradient descent | O(1/k) | O((1−μ/L)ᵏ) (linear) |
| SGD | O(1/√k) | O(1/k) |
| Accelerated GD (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |

where k = iteration count, μ = strong convexity parameter, L = Lipschitz constant.

### Choosing the Learning Rate

| Strategy | Description |
|----------|-------------|
| Fixed α | Simple but may diverge (too large) or converge slowly (too small) |
| Line search | Find α that minimises f(x − α∇f(x)) along the gradient direction |
| Decay schedules | α_t = α₀ / (1 + βt) or α_t = α₀ · βᵗ |
| Warmup | Start small, increase, then decay (common in transformer training) |
| Adaptive (Adam) | Per-parameter learning rates based on gradient statistics |

---

## Constrained Optimization

### Lagrange Multipliers

For the problem: minimise f(x) subject to h(x) = 0.

**Lagrangian:** L(x, λ) = f(x) + λh(x)

At the optimum: ∇ₓL = 0 and ∇_λL = 0 (which gives h(x) = 0).

**Worked Example:** Minimise f(x,y) = x² + y² subject to x + y = 1.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Constraint: x + y = 1 → −λ = 1 → λ = −1
- Solution: x = 1/2, y = 1/2, f = 1/2

### KKT Conditions

The **Karush-Kuhn-Tucker (KKT) conditions** generalise Lagrange multipliers to inequality constraints.

For: minimise f(x) subject to gᵢ(x) ≤ 0, hⱼ(x) = 0.

**Lagrangian:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)

**KKT conditions** (necessary for optimality):

| Condition | Equation |
|-----------|----------|
| Stationarity | ∇ₓL = 0 |
| Primal feasibility | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Dual feasibility | λᵢ ≥ 0 |
| Complementary slackness | λᵢgᵢ(x) = 0 for all i |

**Complementary slackness** means: if constraint gᵢ is not active (gᵢ(x) < 0), then λᵢ = 0 (the constraint doesn't affect the solution).

For convex problems satisfying Slater's condition, KKT conditions are both necessary and sufficient.

---

## Duality

Every optimization problem (the **primal**) has an associated **dual** problem.

### Weak and Strong Duality

| Concept | Statement |
|---------|-----------|
| **Dual function** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Dual problem** | Maximise g(λ, ν) subject to λ ≥ 0 |
| **Weak duality** | Dual optimal ≤ Primal optimal (always holds) |
| **Strong duality** | Dual optimal = Primal optimal (holds for convex problems with Slater's condition) |
| **Duality gap** | Primal optimal − Dual optimal (zero under strong duality) |

### Why Duality Matters

| Application | How Duality Helps |
|-------------|-------------------|
| Lower bounds | Dual gives a certificate of how good the primal solution is |
| SVMs | The dual of the SVM problem leads to the kernel trick |
| Sensitivity analysis | Dual variables measure how much the optimum changes if constraints are relaxed |
| Decomposition | Large problems can be split into smaller subproblems via the dual |

---

## Integer Programming

When some or all variables must be **integers**, the problem becomes much harder (NP-hard in general).

### Types

| Type | Description |
|------|-------------|
| Pure IP | All variables must be integers |
| Mixed IP (MIP) | Some variables integer, some continuous |
| Binary IP | Variables restricted to {0, 1} |

### Solution Methods

| Method | Idea |
|--------|------|
| **Branch and bound** | Split into subproblems, solve LP relaxations, prune |
| **Cutting planes** | Add linear constraints to tighten the LP relaxation |
| **Branch and cut** | Combine branch-and-bound with cutting planes |
| **Heuristics** | Greedy, local search, simulated annealing for approximate solutions |

---

## Heuristic and Metaheuristic Methods

When exact optimization is intractable, heuristics find good (not necessarily optimal) solutions.

| Method | Key Idea | Best For |
|--------|----------|----------|
| **Gradient descent** | Follow the steepest descent | Smooth, differentiable functions |
| **Newton's method** | Use second-order (curvature) information | Smooth, well-conditioned problems |
| **Simulated annealing** | Accept worse solutions with decreasing probability | Global optimization, combinatorial |
| **Genetic algorithms** | Evolve a population using selection, crossover, mutation | Multi-objective, non-differentiable |
| **Particle swarm** | Agents explore space, influenced by best-known positions | Continuous, non-convex |
| **Bayesian optimization** | Build surrogate model, use acquisition function | Expensive black-box functions (hyperparameter tuning) |

### Newton's Method for Optimization

**Update rule:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)

where H is the Hessian matrix (matrix of second derivatives).

| Property | Value |
|----------|-------|
| Convergence rate | Quadratic (near optimum) |
| Per-iteration cost | O(n³) for Hessian inversion |
| Requires | Twice differentiable, positive definite Hessian |
| Quasi-Newton (BFGS) | Approximate Hessian from gradients | O(n²) per iteration |

---

## Relevance to Machine Learning and Data Science

| Optimization Concept | Application |
|---------------------|-------------|
| Gradient descent | Training neural networks, logistic regression, any differentiable model |
| SGD and variants | Large-scale ML (mini-batch training), online learning |
| Adam, RMSprop | Default optimizers for deep learning |
| Convex optimization | SVMs, logistic regression, LASSO, Ridge (guaranteed global optimum) |
| Lagrange multipliers | Constrained learning, fair ML, resource allocation |
| KKT conditions | Deriving SVM dual, understanding constraint activity |
| Duality | SVM kernel trick, sensitivity analysis, decomposition methods |
| Linear programming | Resource allocation, portfolio optimization, network flow |
| Integer programming | Feature selection (binary), scheduling, combinatorial problems |
| Bayesian optimization | Hyperparameter tuning (Optuna, Hyperopt) |
| Newton/quasi-Newton | Second-order methods for small-to-medium problems (L-BFGS) |

---

## Summary

| Method | Problem Type | Guarantees | Scale |
|--------|-------------|------------|-------|
| Simplex | Linear programming | Exact optimum | Millions of variables |
| Interior point | Convex (LP, QP, SOCP) | Exact optimum | Large scale |
| Gradient descent | Smooth unconstrained | Converges to local min | Very large (deep learning) |
| SGD | Large-scale empirical risk | Converges (with decay) | Massive datasets |
| Newton / BFGS | Smooth, twice-differentiable | Quadratic convergence | Small-to-medium |
| KKT / Lagrange | Constrained (convex) | Exact under conditions | Medium |
| Branch and bound | Integer programming | Exact optimum | Small-to-medium |
| Heuristics | Any (non-convex, combinatorial) | No guarantee | Varies |

Optimization is arguably the most important mathematical tool in machine learning. Every model you train — from linear regression to large language models — involves solving an optimization problem. Understanding when a problem is convex (guaranteed global optimum), when gradient descent will converge, and how to handle constraints gives you the theoretical foundation to design, debug, and improve learning algorithms.
