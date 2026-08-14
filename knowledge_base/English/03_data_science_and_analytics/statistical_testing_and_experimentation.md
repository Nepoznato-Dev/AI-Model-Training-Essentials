<!--
---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Statistical Testing and Experimentation

Statistics is the grammar of science. It gives you the tools to distinguish real patterns from random noise, to measure whether a change actually improved things, and to make decisions under uncertainty. This file covers the core concepts of hypothesis testing, experimental design, and the common pitfalls that trip people up.

---

## The Hypothesis Testing Framework

Every statistical test follows the same logic:

1. **State the null hypothesis (H₀)**: There is no effect / no difference.
2. **State the alternative hypothesis (H₁)**: There is an effect / a difference.
3. **Choose a significance level (α)**: Usually 0.05 (5% chance of false positive).
4. **Collect data and compute a test statistic**.
5. **Calculate the p-value**: Probability of observing this result (or more extreme) if H₀ is true.
6. **Make a decision**: If p < α, reject H₀ (statistically significant). Otherwise, fail to reject H₀.

### Key Concepts

| Concept | Meaning | Common Misconception |
|---------|---------|---------------------|
| **p-value** | P(data \| H₀ is true) | NOT "the probability that H₀ is true" |
| **α (significance level)** | Threshold for rejecting H₀ | Not a measure of effect importance |
| **Statistical significance** | Result unlikely due to chance alone | Does NOT mean practically significant |
| **Effect size** | Magnitude of the observed effect | Separate from p-value; a tiny effect can be significant with large N |
| **Power** | Probability of correctly rejecting a false H₀ | Typically aim for 80%+ |
| **Confidence interval** | Range of plausible values for the parameter | A 95% CI doesn't mean "95% probability the true value is in this range" |

---

## Types of Errors

| | H₀ is True | H₀ is False |
|---|-----------|------------|
| **Reject H₀** | Type I Error (false positive) | ✅ Correct (true positive) |
| **Fail to reject H₀** | ✅ Correct (true negative) | Type II Error (false negative) |

| Error | Symbol | Meaning |
|-------|--------|---------|
| **Type I** | α | Concluding there's an effect when there isn't |
| **Type II** | β | Missing a real effect |

---

## Choosing the Right Test

| Scenario | Test | Assumptions |
|----------|------|-------------|
| Compare means of 2 groups | **t-test** (independent) | Normal distribution, equal variance |
| Compare means of paired observations | **Paired t-test** | Differences are normally distributed |
| Compare means of 3+ groups | **ANOVA** | Normal distribution, equal variance |
| Compare categorical distributions | **Chi-square test** | Sufficient sample size per cell |
| Compare distributions (non-parametric) | **Mann-Whitney U** | No normality assumption |
| Compare 3+ groups (non-parametric) | **Kruskal-Wallis** | No normality assumption |
| Test correlation | **Pearson** (linear) or **Spearman** (monotonic) | Pearson: normality; Spearman: rank-based |
| Test if data follows a distribution | **Kolmogorov-Smirnov** | Continuous data |

### Parametric vs Non-Parametric

| | Parametric | Non-Parametric |
|---|-----------|---------------|
| **Assumptions** | Data follows a specific distribution (usually normal) | No distribution assumption |
| **Power** | Higher when assumptions met | Lower, but more robust |
| **When to use** | Large samples, approximately normal data | Small samples, skewed data, ordinal data |

---

## Specific Tests in Detail

### t-Test

Compares the means of two groups.

| Variant | Use Case |
|---------|----------|
| **Independent t-test** | Two separate groups (treatment vs control) |
| **Paired t-test** | Same group measured twice (before vs after) |
| **One-sample t-test** | Compare a sample mean to a known value |

```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Analysis of Variance)

Compares means across 3 or more groups. Tests whether at least one group mean differs from the rest.

| Type | Design |
|------|--------|
| **One-way ANOVA** | One independent variable with 3+ levels |
| **Two-way ANOVA** | Two independent variables; tests interaction effects |
| **Repeated Measures ANOVA** | Same subjects measured under different conditions |

If ANOVA is significant, follow up with **post-hoc tests** (Tukey's HSD) to find which specific groups differ.

### Chi-Square Test

Tests whether two categorical variables are independent.

| Use Case | Example |
|----------|---------|
| **Test of independence** | Is gender associated with product preference? |
| **Goodness of fit** | Does a die roll follow a uniform distribution? |

**Rule of thumb**: each cell should have an expected count of at least 5.

---

## A/B Testing

A/B testing is the application of hypothesis testing to business decisions — typically comparing a control (A) with a variant (B).

### Design Process

| Step | Description |
|------|-------------|
| **1. Define hypothesis** | "Changing button colour from blue to green will increase click-through rate" |
| **2. Choose metric** | Primary: click-through rate. Secondary: conversion rate, revenue. |
| **3. Calculate sample size** | Based on minimum detectable effect, power (80%), and significance (5%) |
| **4. Randomise** | Randomly assign users to control and treatment |
| **5. Run experiment** | Collect data until target sample size is reached |
| **6. Analyse** | Compare metrics using appropriate statistical test |
| **7. Decide** | Implement if statistically and practically significant |

### Sample Size Calculation

The sample size you need depends on:

| Factor | Effect on Sample Size |
|--------|----------------------|
| **Smaller effect to detect** | Need more samples |
| **Higher power** | Need more samples |
| **Lower significance level** | Need more samples |
| **Higher variance** | Need more samples |

### Common A/B Testing Mistakes

| Mistake | Why It's Wrong |
|---------|---------------|
| **Peeking early** | Checking results daily inflates false positive rate |
| **Multiple metrics without correction** | Testing 20 metrics at α=0.05 → expect 1 false positive by chance |
| **Stopping before target N** | Underpowered test can't detect real effects |
| **Ignoring seasonality** | Running a test over a holiday period vs normal week |
| **Non-random assignment** | Selection bias (e.g., assigning new users to treatment) |
| **Confusing significance with importance** | A 0.1% lift can be statistically significant but not worth shipping |

---

## Multiple Comparisons

When you run many tests simultaneously, the chance of at least one false positive increases dramatically.

| Number of Tests | Probability of ≥1 False Positive (at α=0.05) |
|----------------|----------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |

### Corrections

| Method | How It Works | When to Use |
|--------|-------------|-------------|
| **Bonferroni** | Divide α by number of tests (α/n) | Conservative; few comparisons |
| **Holm-Bonferroni** | Step-down procedure; less conservative | General use |
| **Benjamini-Hochberg (FDR)** | Controls false discovery rate | Many tests; exploratory analysis |

---

## Effect Size

P-values tell you *whether* an effect exists. Effect size tells you *how big* it is.

| Measure | For | Interpretation |
|---------|-----|---------------|
| **Cohen's d** | Difference between two means | 0.2 = small, 0.5 = medium, 0.8 = large |
| **Pearson's r** | Correlation | 0.1 = small, 0.3 = medium, 0.5 = large |
| **η² (eta-squared)** | ANOVA | 0.01 = small, 0.06 = medium, 0.14 = large |
| **Odds Ratio** | Categorical outcomes | 1.0 = no effect; >1 or <1 = effect |

**Always report effect size alongside p-values.** A result can be statistically significant but practically meaningless.

---

## Bayesian vs Frequentist

| Aspect | Frequentist | Bayesian |
|--------|------------|----------|
| **Probability** | Long-run frequency of events | Degree of belief |
| **Parameters** | Fixed but unknown | Random variables with distributions |
| **Uses** | p-values, confidence intervals, hypothesis tests | Posterior distributions, credible intervals |
| **Prior** | No prior beliefs incorporated | Explicit prior distribution |
| **Interpretation** | "If we repeated this experiment many times..." | "Given the data, the probability that..." |
| **Strengths** | Objective, well-established, simple | Intuitive interpretation, incorporates prior knowledge |
| **Weaknesses** | p-values widely misunderstood | Choice of prior can be subjective |

---

## Causal Inference Basics

Correlation is not causation. But sometimes you need to know *whether X caused Y*, not just whether they're associated.

| Method | Description | When to Use |
|--------|-------------|-------------|
| **Randomised experiments** | Gold standard; random assignment eliminates confounders | When you can randomise |
| **Difference-in-Differences (DiD)** | Compare changes over time between treatment and control | Policy changes, natural experiments |
| **Regression Discontinuity (RDD)** | Exploit a cutoff threshold | Scholarships, eligibility thresholds |
| **Instrumental Variables (IV)** | Use an instrument that affects treatment but not outcome directly | When randomisation isn't possible |
| **Propensity Score Matching** | Match treated and control units on observed characteristics | Observational studies |

---

## Common Statistical Mistakes

| Mistake | Description |
|---------|-------------|
| **p-hacking** | Trying many analyses until you find p < 0.05 |
| **HARKing** | Hypothesising After Results are Known |
| **Survivorship bias** | Only looking at successes (e.g., successful companies) |
| **Simpson's paradox** | Trend reverses when data is aggregated vs split by group |
| **Base rate neglect** | Ignoring prior probability when interpreting results |
| **Ecological fallacy** | Inferring individual behaviour from group-level data |
| **Confounding** | A third variable explains the observed relationship |
| **Overfitting** | Model captures noise, not signal |

---

## Summary

Statistical testing is about making decisions under uncertainty with intellectual honesty. Always state your hypotheses before collecting data. Choose the right test for your data type. Report effect sizes, not just p-values. Correct for multiple comparisons. And remember: statistical significance is not the same as practical significance.
