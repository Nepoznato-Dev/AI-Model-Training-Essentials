---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Statistics and Probability

Probability and statistics are the mathematical foundations of data science, machine learning, and scientific research. Probability tells you how likely events are; statistics tells you how to draw conclusions from data. Together, they turn uncertainty into quantifiable, manageable knowledge.

---

## Probability Theory

### Core Concepts

| Concept | Description | Example |
|---------|-------------|---------|
| **Sample Space** | Set of all possible outcomes | Rolling a die: {1, 2, 3, 4, 5, 6} |
| **Event** | A subset of the sample space | Rolling an even number: {2, 4, 6} |
| **Probability** | Number between 0 and 1 measuring likelihood | P(rolling 6) = 1/6 |
| **Conditional Probability** | P(A|B): probability of A given B has occurred | P(rain | cloudy) |
| **Independence** | Events where one doesn't affect the other | Coin flips are independent |

### Probability Rules

| Rule | Formula | Use Case |
|------|---------|----------|
| **Addition Rule** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Probability of A or B |
| **Multiplication Rule** | P(A ∩ B) = P(A) × P(B|A) | Probability of A and B |
| **Complement Rule** | P(not A) = 1 − P(A) | Probability of event not occurring |
| **Law of Total Probability** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Partitioning by mutually exclusive events |
| **Bayes' Theorem** | P(A|B) = P(B|A) × P(A) / P(B) | Updating beliefs with evidence |

### Probability Distributions

| Distribution | Type | Key Parameters | Use Case |
|-------------|------|----------------|----------|
| **Normal (Gaussian)** | Continuous | Mean (μ), Standard deviation (σ) | Natural phenomena, measurement errors |
| **Binomial** | Discrete | n (trials), p (probability) | Success/failure counts |
| **Poisson** | Discrete | λ (rate) | Rare events over time/space |
| **Exponential** | Continuous | λ (rate) | Time between events |
| **Uniform** | Both | a, b (bounds) | Equally likely outcomes |
| **Chi-Square** | Continuous | k (degrees of freedom) | Goodness-of-fit tests |
| **t-Distribution** | Continuous | ν (degrees of freedom) | Small sample inference |

### Key Properties of Distributions

| Property | Description |
|----------|-------------|
| **Mean (Expected Value)** | Center of mass of the distribution: E[X] = Σ xᵢ × P(xᵢ) |
| **Variance** | Spread around the mean: Var(X) = E[(X − μ)²] |
| **Standard Deviation** | Square root of variance; same units as data |
| **Skewness** | Asymmetry of the distribution |
| **Kurtosis** | "Tailedness" — how heavy the tails are |

---

## Statistical Inference

### Descriptive vs. Inferential Statistics

| | Descriptive | Inferential |
|---|-------------|-------------|
| **Purpose** | Summarize and describe data | Draw conclusions about a population from a sample |
| **Tools** | Mean, median, mode, standard deviation, charts | Hypothesis tests, confidence intervals, regression |
| **Scope** | Only the data you have | Generalizing beyond your sample |

### Hypothesis Testing Framework

| Step | Description |
|------|-------------|
| 1. **State hypotheses** | Null hypothesis (H₀): no effect; Alternative (H₁): effect exists |
| 2. **Choose significance level** | α = 0.05 (conventional) |
| 3. **Select test** | Based on data type, sample size, and assumptions |
| 4. **Calculate test statistic** | Depends on the test chosen |
| 5. **Find p-value** | Probability of observing the data if H₀ is true |
| 6. **Make decision** | If p < α, reject H₀; otherwise, fail to reject H₀ |

### Common Statistical Tests

| Test | When to Use | What It Compares |
|------|-------------|-----------------|
| **t-test** | Compare means of 1–2 groups | Group mean(s) to a value or to each other |
| **Chi-square test** | Categorical data | Observed vs. expected frequencies |
| **ANOVA** | Compare means of 3+ groups | Between-group vs. within-group variance |
| **Mann-Whitney U** | Non-parametric alternative to t-test | Rank distributions of two groups |
| **Pearson correlation** | Linear relationship between two continuous variables | r value from −1 to +1 |
| **Spearman correlation** | Monotonic relationship (rank-based) | ρ value for ordinal or non-normal data |

### Confidence Intervals

A confidence interval gives a range of plausible values for a population parameter:

- **95% CI for mean** (known σ): x̄ ± 1.96 × (σ / √n)
- **Interpretation**: "We are 95% confident the true population mean lies within this interval"
- **Wider CI** = more uncertainty (smaller sample, higher variability, or higher confidence level)

---

## Regression Analysis

### Types of Regression

| Type | Dependent Variable | Use Case |
|------|-------------------|----------|
| **Linear Regression** | Continuous | Predicting house prices, sales |
| **Logistic Regression** | Binary (0/1) | Classification: spam detection, disease diagnosis |
| **Polynomial Regression** | Continuous (curved) | Growth curves, non-linear trends |
| **Multiple Regression** | Continuous (2+ predictors) | Controlling for confounders |
| **Ridge / Lasso** | Continuous (regularized) | Preventing overfitting, feature selection |

### Linear Regression Basics

The model: **y = β₀ + β₁x + ε**

| Component | Meaning |
|-----------|---------|
| β₀ (intercept) | Value of y when x = 0 |
| β₁ (slope) | Change in y for a one-unit change in x |
| ε (error term) | Unexplained variation |

**Key metrics:**
- **R² (coefficient of determination)**: Proportion of variance explained by the model (0 to 1)
- **Adjusted R²**: R² penalized for number of predictors
- **RMSE**: Root mean squared error — average prediction error in same units as y

### Assumptions of Linear Regression

| Assumption | What It Means | How to Check |
|-----------|--------------|--------------|
| **Linearity** | Relationship between X and Y is linear | Scatter plots |
| **Independence** | Observations are independent | Study design |
| **Homoscedasticity** | Constant variance of residuals | Residual plots |
| **Normality** | Residuals are normally distributed | Q-Q plot, Shapiro-Wilk test |
| **No multicollinearity** | Predictors aren't highly correlated | VIF (Variance Inflation Factor) |

---

## Bayesian Statistics

### Frequentist vs. Bayesian

| | Frequentist | Bayesian |
|---|-------------|----------|
| **Probability means** | Long-run frequency | Degree of belief |
| **Parameters are** | Fixed but unknown | Random variables with distributions |
| **Uses** | p-values, confidence intervals | Posterior distributions, credible intervals |
| **Strengths** | Objective, well-established | Incorporates prior knowledge, intuitive interpretation |

### Bayes' Theorem in Practice

**Posterior = (Likelihood × Prior) / Evidence**

Example — medical testing:
- Disease prevalence: 1% (prior)
- Test sensitivity: 95% (true positive rate)
- Test specificity: 90% (true negative rate)
- If you test positive: P(disease | positive) = (0.95 × 0.01) / (0.95 × 0.01 + 0.10 × 0.99) ≈ 8.8%

This counterintuitive result — most positive results are false positives when the disease is rare — is the **base rate fallacy**, and it shows why Bayesian thinking matters.

---

## Practical Tips

- **Always visualize your data** before running any statistical test
- **Check assumptions** — violations can invalidate results
- **Effect size matters** — a statistically significant result may be practically meaningless
- **Correlation is not causation** — even strong correlations may have confounders
- **Multiple comparisons** inflate false positive rates — apply corrections (Bonferroni, FDR)
- **Report confidence intervals**, not just p-values

---

## Why This Matters

Statistics is the backbone of scientific research, business analytics, and machine learning. Without it, you can't tell signal from noise, identify real effects from random fluctuations, or make predictions with quantified uncertainty. Whether you're analyzing A/B tests, training ML models, or reading research papers, statistical literacy is essential.
