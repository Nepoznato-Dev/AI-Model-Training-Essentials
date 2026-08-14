---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Causal Inference

Causal inference is the science of determining whether one thing actually causes another — not just whether they're correlated. Correlation tells you that two variables move together. Causation tells you that changing one will change the other. This distinction matters enormously in medicine (does this drug work?), policy (does this intervention reduce poverty?), business (does this ad campaign increase sales?), and science (does this mechanism explain the phenomenon?).

---

## Correlation vs Causation

| Concept | Description | Example |
|---------|-------------|---------|
| **Correlation** | Two variables move together | Ice cream sales and drowning deaths both increase in summer |
| **Causation** | One variable directly affects another | Smoking causes lung cancer |
| **Confounding** | A third variable causes both | Hot weather causes both ice cream sales and swimming (and drowning) |
| **Reverse causation** | The effect actually causes the supposed cause | People buy health supplements because they're sick, not the other way around |
| **Spurious correlation** | Coincidental relationship | Per capita cheese consumption correlates with deaths by bedsheet entanglement |

---

## The Potential Outcomes Framework

### Rubin Causal Model

| Concept | Description |
|---------|-------------|
| **Potential outcomes** | For each unit, there's an outcome if treated Y(1) and an outcome if untreated Y(0) |
| **Treatment effect** | The difference: Y(1) - Y(0) for a given unit |
| **Fundamental problem** | We can never observe both Y(1) and Y(0) for the same unit — we can only see one |
| **Average Treatment Effect (ATE)** | The average of individual treatment effects across the population |
| **Counterfactual** | The unobserved outcome — what would have happened under the other condition |

### Key Assumptions

| Assumption | Meaning | How to Satisfy |
|-----------|--------|----------------|
| **Ignorability (unconfoundedness)** | Treatment assignment is independent of potential outcomes, given observed covariates | Randomisation; measure all confounders |
| **Positivity (overlap)** | Every unit has a non-zero probability of receiving either treatment | Check covariate overlap between groups |
| **SUTVA** (Stable Unit Treatment Value Assumption) | One unit's treatment doesn't affect another's outcome; treatment is consistent | No interference; no hidden versions of treatment |
| **Consistency** | The observed outcome equals the potential outcome under the received treatment | Well-defined treatment |

---

## Methods for Causal Inference

### Experimental Methods

| Method | Description | Strength | Limitation |
|--------|-------------|----------|------------|
| **Randomised controlled trial (RCT)** | Randomly assign units to treatment or control | Gold standard; eliminates confounding | Expensive; sometimes unethical; may not generalise |
| **A/B testing** | RCT in a business/tech context | Simple; rigorous | Short-term metrics; novelty effects; interference |
| **Switchback experiments** | Alternate treatment over time periods | Handles interference in marketplaces | Requires stable environment |

### Quasi-Experimental Methods

| Method | Description | Key Assumption |
|--------|-------------|----------------|
| **Difference-in-differences (DiD)** | Compare the change in outcomes between treated and control groups over time | Parallel trends: groups would have followed the same trajectory without treatment |
| **Regression discontinuity (RD)** | Compare units just above and just below a treatment cutoff | Units near the cutoff are comparable (as-if random) |
| **Instrumental variables (IV)** | Use a variable that affects treatment but not the outcome except through treatment | Instrument is correlated with treatment; affects outcome only through treatment |
| **Synthetic control** | Construct a weighted combination of control units to match the treated unit | Synthetic control accurately represents the treated unit's counterfactual |
| **Propensity score matching** | Match treated and control units with similar probabilities of treatment | All confounders are measured and included in the propensity model |

### Difference-in-Differences (Visualised)

| Period | Treated Group | Control Group | Difference |
|--------|--------------|---------------|------------|
| **Pre-treatment** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Post-treatment** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **DiD estimate** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |

---

## Directed Acyclic Graphs (DAGs)

DAGs are visual tools for encoding causal assumptions and identifying confounders.

### Basic Structures

| Structure | Pattern | Implication |
|-----------|---------|-------------|
| **Chain** | A → B → C | A and C are associated through B; controlling for B blocks the path |
| **Fork** | A ← B → C | A and C are confounded by B; controlling for B blocks the path |
| **Collider** | A → B ← C | A and C are independent; controlling for B opens the path (creates spurious association) |

### Rules for DAGs

| Rule | Description |
|------|-------------|
| **Backdoor criterion** | To estimate the causal effect of X on Y, block all backdoor paths (paths with an arrow into X) by conditioning on appropriate variables |
| **Front-door criterion** | If backdoor paths can't be blocked, use mediators: estimate X → M → Y in two stages |
| **Don't condition on colliders** | Controlling for a common effect opens a spurious path |
| **Don't condition on descendants of colliders** | Same problem as conditioning on the collider itself |

---

## Common Pitfalls

| Pitfall | Description | Example |
|---------|-------------|---------|
| **Omitted variable bias** | Failing to control for a confounder | Estimating education → earnings without controlling for ability |
| **Overcontrolling** | Conditioning on a mediator or collider | Controlling for job title when estimating education → earnings |
| **Selection bias** | Conditioning on a variable affected by treatment | Only analysing employed people when studying training → wages |
| **Immortal time bias** | Misclassifying person-time in cohort studies | Patients must survive long enough to receive treatment |
| **Regression to the mean** | Extreme values tend to move toward average | Sick patients improve after treatment regardless |
| **Post-treatment bias** | Conditioning on variables that occur after treatment | Controlling for adverse events when estimating drug efficacy |

---

## Tools and Libraries

| Tool | Language | Description |
|------|----------|-------------|
| **DoWhy** | Python | Microsoft library; DAG-based causal inference |
| **CausalML** | Python | Uber's library for uplift modelling and causal ML |
| **EconML** | Python | Double ML, causal forests, instrumental variables |
| **linearmodels** | Python | IV, panel data models, DiD |
| **MatchIt** | R | Propensity score matching |
| **dagitty** | R / web | DAG analysis; identify adjustment sets |
| **CausalImpact** | R / Python | Bayesian structural time series for causal inference |

---

## Summary

Causal inference is about moving beyond "what happened" to "what would have happened if things were different." The fundamental challenge is that we can never observe both the treated and untreated outcomes for the same unit — the counterfactual is always missing. Randomised experiments solve this by making treatment and control groups comparable. When randomisation isn't possible, quasi-experimental methods — DiD, regression discontinuity, instrumental variables, synthetic control — try to reconstruct the counterfactual from observational data. DAGs help make assumptions explicit and identify the right variables to control for. The key skill is thinking carefully about the data-generating process: what causes what, what's a confounder, what's a collider, and what would have happened under the alternative.
