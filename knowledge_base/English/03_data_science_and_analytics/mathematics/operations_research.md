<!--
---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Operations Research

Operations research (OR) is the application of mathematical methods to decision-making. Born during World War II for military logistics, it now optimises supply chains, schedules airlines, routes delivery fleets, manages inventories, and allocates resources across every industry. OR provides the mathematical toolkit for making the best possible decisions under constraints.

---

## Linear Programming Formulations

### Standard Form

Minimise cᵀx
Subject to: Ax = b, x ≥ 0

### Common LP Formulations

**Product Mix:**
- Decision variables: xⱼ = quantity of product j to produce
- Objective: maximise profit Σ pⱼxⱼ
- Constraints: resource limits Σ aᵢⱼxⱼ ≤ bᵢ

**Diet Problem:**
- Decision variables: xⱼ = amount of food j to buy
- Objective: minimise cost Σ cⱼxⱼ
- Constraints: nutritional requirements Σ nᵢⱼxⱼ ≥ rᵢ

**Blending Problem:**
- Decision variables: xⱼ = proportion of ingredient j in blend
- Objective: minimise cost
- Constraints: quality requirements (octane rating, strength, etc.)

### Worked Example: Production Planning

A factory makes products A and B.
- A requires 2 hours labour, 1 kg material; profit $30
- B requires 1 hour labour, 3 kg material; profit $40
- Available: 40 hours labour, 30 kg material

**Formulation:**
- Maximise: 30x_A + 40x_B
- Subject to: 2x_A + x_B ≤ 40 (labour)
- x_A + 3x_B ≤ 30 (material)
- x_A, x_B ≥ 0

**Solution:** Vertices of feasible region: (0,0), (20,0), (18,4), (0,10)
- (0,0): profit = 0
- (20,0): profit = 600
- (18,4): profit = 700 ← optimal
- (0,10): profit = 400

---

## Transportation Problem

Moving goods from m sources to n destinations at minimum cost.

### Formulation

- Decision variables: xᵢⱼ = quantity shipped from source i to destination j
- Objective: minimise Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Subject to: Σⱼ xᵢⱼ = sᵢ (supply constraints)
- Σᵢ xᵢⱼ = dⱼ (demand constraints)
- xᵢⱼ ≥ 0

### Solution Methods

| Method | Description | Quality of Initial Solution |
|--------|-------------|---------------------------|
| **Northwest Corner** | Start top-left, allocate greedily | Feasible but often poor |
| **Vogel's Approximation** | Consider penalty costs | Better initial solution |
| **MODI / Stepping Stone** | Improve initial solution iteratively | Finds optimal |

### Worked Example

| | D1 | D2 | D3 | Supply |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Demand | 40 | 30 | 30 | 100 |

---

## Assignment Problem

Assigning n workers to n jobs (one-to-one) to minimise total cost.

### Formulation

- Decision variables: xᵢⱼ ∈ {0, 1} (1 if worker i assigned to job j)
- Minimise: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Subject to: Σⱼ xᵢⱼ = 1 (each worker gets one job)
- Σᵢ xᵢⱼ = 1 (each job gets one worker)

### Hungarian Algorithm

| Property | Value |
|----------|-------|
| Time complexity | O(n³) |
| Optimal? | Yes |
| Approach | Matrix reduction + minimum cover |

**Steps:**
1. Subtract row minimums from each row
2. Subtract column minimums from each column
3. Cover all zeros with minimum number of lines
4. If lines = n, optimal assignment found among zeros
5. Otherwise, adjust matrix and repeat

---

## Network Flow Optimization

### Minimum Cost Flow

Given a network with capacities and costs on edges, find the flow that satisfies demands at minimum cost.

**Formulation:**
- Minimise: Σ cᵢⱼxᵢⱼ
- Subject to: flow conservation at each node
- Capacity constraints: 0 ≤ xᵢⱼ ≤ uᵢⱼ

### Shortest Path as Network Flow

The shortest path problem is a special case of minimum cost flow (send 1 unit from s to t).

### Applications

| Application | Network Model |
|-------------|--------------|
| Supply chain | Nodes = warehouses, edges = shipping routes |
| Communication | Nodes = routers, edges = links with bandwidth |
| Traffic | Nodes = intersections, edges = roads with capacity |
| Project management | CPM/PERT networks |

---

## Dynamic Programming

**Dynamic programming (DP)** solves complex problems by breaking them into overlapping subproblems.

### Bellman's Principle of Optimality

An optimal policy has the property that whatever the initial state and decision, the remaining decisions must constitute an optimal policy for the resulting state.

### Key Elements

| Element | Description |
|---------|-------------|
| **Stage** | Decision point (time step, item index) |
| **State** | Information needed to make a decision |
| **Decision** | Choice made at each stage |
| **Recurrence** | Optimal value at stage n in terms of stage n−1 |

### Classic DP Problems

| Problem | Recurrence | Complexity |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) with memoisation |
| **Knapsack** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Shortest path** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) or O(E log V) |
| **Edit distance** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+cost) | O(mn) |
| **Longest common subsequence** | L(i,j) = L(i−1,j−1)+1 if match, else max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Matrix chain multiplication** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |

### Worked Example: 0/1 Knapsack

Items: {weight: value} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Capacity W = 7.

V(i, w) = max value using first i items with capacity w

| i\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |

Optimal: V(4, 7) = 23 (items 1 and 4: weight 2+5=7, value 12+11=23).

---

## Queueing Theory

Queueing theory studies waiting lines — how long they are, how long you wait, and how to reduce both.

### Kendall's Notation

A/B/c/K/N/D where:
- A = arrival process (M = Markovian/Poisson, D = deterministic, G = general)
- B = service process (same options)
- c = number of servers
- K = capacity (default ∞)
- N = population (default ∞)
- D = discipline (FIFO, LIFO, Priority)

### M/M/1 Queue (Single Server)

| Metric | Formula |
|--------|---------|
| Utilisation | ρ = λ/μ |
| Average number in system | L = ρ/(1−ρ) |
| Average time in system | W = 1/(μ−λ) |
| Average number in queue | L_q = ρ²/(1−ρ) |
| Average waiting time | W_q = ρ/(μ−λ) |

where λ = arrival rate, μ = service rate, ρ = utilisation.

### M/M/c Queue (Multiple Servers)

| Metric | Formula |
|--------|---------|
| Utilisation | ρ = λ/(cμ) |
| Probability of waiting (Erlang C) | P_w = complex formula involving ρ and c |
| Average queue length | L_q = P_w · ρ/(1−ρ) |

### Little's Law

L = λW (average number in system = arrival rate × average time)

This holds for ANY queueing system, regardless of arrival/service distributions.

### Application Examples

| Scenario | Queue Model |
|----------|-------------|
| Call centre | M/M/c (c agents) |
| Web server requests | M/M/1 or M/G/1 |
| Hospital emergency | M/G/c with priorities |
| Manufacturing line | Network of queues |
| Computer CPU scheduling | M/M/1 processor sharing |

---

## Inventory Models

### Economic Order Quantity (EOQ)

The optimal order quantity that minimises total inventory costs.

Q* = √(2DS/H)

| Variable | Meaning |
|----------|---------|
| D | Annual demand |
| S | Ordering cost per order |
| H | Holding cost per unit per year |
| Q* | Optimal order quantity |

**Total cost at Q*:** TC = √(2DSH)

### Extensions

| Model | Extension |
|-------|-----------|
| **EOQ with discounts** | Quantity discounts change the cost function |
| **Production order quantity** | Items produced gradually, not delivered all at once |
| **(s, Q) model** | Reorder Q units when inventory drops to level s |
| **(s, S) model** | Order up to S when inventory drops to s |
| **Newsvendor model** | Single-period, uncertain demand |

### Newsvendor Model

Optimal order quantity for single-period perishable inventory:

P(D ≤ Q*) = c_u / (c_u + c_o)

where c_u = underage cost (lost profit) and c_o = overage cost (waste).

---

## Scheduling

### Job Shop Scheduling

| Notation | Meaning |
|----------|---------|
| n/m/J/C_max | n jobs, m machines, job shop, minimise makespan |
| Flow shop | All jobs visit machines in same order |
| Job shop | Each job has its own machine sequence |
| Open shop | No ordering constraints |

### Priority Rules

| Rule | Description | Effect |
|------|-------------|--------|
| FCFS | First come, first served | Fair, but not optimal |
| SPT | Shortest processing time first | Minimises average completion |
| EDD | Earliest due date first | Minimises maximum lateness |
| CR | Critical ratio (due date remaining / processing time) | Balanced |
| LPT | Longest processing time first | Good for makespan on parallel machines |

### Johnson's Algorithm (2-Machine Flow Shop)

For n jobs on 2 machines, minimising makespan:
1. Find the job with shortest processing time
2. If it's on machine 1, schedule it first; if on machine 2, schedule it last
3. Remove that job and repeat

Optimal for 2 machines; NP-hard for 3+ machines.

---

## Relevance to Machine Learning and Data Science

| OR Concept | Application |
|-----------|-------------|
| Linear programming | Resource allocation, portfolio optimisation, ad budget allocation |
| Transportation/assignment | Logistics, ride-sharing matching, task assignment |
| Network flow | Supply chain optimisation, data centre traffic routing |
| Dynamic programming | Sequence alignment (bioinformatics), Viterbi algorithm (HMMs), RL (Bellman equation) |
| Queueing theory | Server capacity planning, latency modelling, cloud resource allocation |
| Inventory models | Demand forecasting integration, supply chain ML |
| Scheduling | ML pipeline orchestration, GPU job scheduling, hyperparameter search scheduling |
| Integer programming | Feature selection (binary), model selection, network design |

---

## Summary

| Topic | Core Problem | Key Method |
|-------|-------------|------------|
| LP Formulations | Optimise linear objective with constraints | Simplex, interior point |
| Transportation | Ship goods at minimum cost | MODI, stepping stone |
| Assignment | Match workers to jobs | Hungarian algorithm |
| Network Flow | Route flow through a network | Min-cost flow algorithms |
| Dynamic Programming | Overlapping subproblems | Bellman's principle, memoisation |
| Queueing Theory | Waiting line analysis | M/M/1, Little's law |
| Inventory | When and how much to order | EOQ, newsvendor |
| Scheduling | Sequence jobs on machines | Priority rules, Johnson's algorithm |

Operations research transforms decision-making from art to science. By formulating real-world problems mathematically, OR provides provably optimal (or near-optimal) solutions to logistics, scheduling, resource allocation, and planning problems that affect every industry. For data scientists, OR methods complement machine learning: while ML predicts, OR prescribes — and together, they form the foundation of intelligent decision systems.
