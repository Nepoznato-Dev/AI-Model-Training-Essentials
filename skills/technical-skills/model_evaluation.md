---
# Metadata
title: "Model Evaluation"
description: "Systematically assessing machine learning model performance using appropriate metrics, validation strategies, and evaluation frameworks."
category: "Technical Skills"
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
    changes: "Initial skill creation"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2026-08-10"
reviewed_by: "Technical Skills Team"
next_review: "2027-02-10"

# Classification
tags: [model-evaluation, metrics, cross-validation, benchmarking, error-analysis, ml-assessment]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Model Evaluation

The systematic process of assessing how well a machine learning model performs using appropriate metrics, validation strategies, and diagnostic techniques.

## Overview

Model evaluation is the bridge between training a model and trusting it in production. A model that scores well on training data but poorly on unseen data is useless — and worse, a model that appears good by one metric may be failing critically by another. Evaluation is not a single step but a discipline that spans metric selection, validation strategy, error analysis, fairness assessment, and ongoing monitoring.

Choosing the wrong metric or validation strategy can give false confidence. Accuracy on imbalanced data hides poor minority-class performance. A single train-test split may produce lucky or unlucky results. And metrics that look good in aggregate can mask severe failures on specific subpopulations.

This skill provides a structured framework for evaluating models rigorously: selecting the right metrics for the task, designing validation strategies that produce reliable estimates, diagnosing failure modes, and communicating results clearly to stakeholders.

## Core Competencies

- Selecting evaluation metrics appropriate to the task, data distribution, and business objective
- Designing validation strategies (holdout, k-fold, stratified, temporal) that produce reliable performance estimates
- Performing error analysis to identify systematic failure patterns
- Evaluating model fairness across demographic or categorical subgroups
- Comparing models using statistical significance tests rather than point estimates
- Communicating evaluation results with appropriate caveats and confidence intervals
- Setting up evaluation pipelines that run automatically with each experiment

## When to Use

- After training any model, before deploying or comparing it against baselines
- When choosing between multiple model architectures or hyperparameter configurations
- When stakeholders ask "how good is the model?" and you need a rigorous answer
- When debugging unexpected model behavior or poor production performance
- When preparing model documentation (model cards) for governance or compliance
- When validating that a model meets predefined quality gates or SLAs

## Framework/Methodology

### Phase 1: Metric Selection

Match metrics to your task type and business objective:

**Classification:**

| Metric | Use When | Avoid When |
|--------|----------|------------|
| Accuracy | Classes are balanced, all errors cost the same | Data is imbalanced |
| Precision | False positives are costly (e.g., spam detection) | False negatives are more costly |
| Recall | False negatives are costly (e.g., disease screening) | False positives are more costly |
| F1 Score | Need balance between precision and recall | Asymmetric cost structure |
| ROC-AUC | Need threshold-independent ranking evaluation | Only care about one operating point |
| PR-AUC | Positive class is rare and important | Classes are balanced |

**Regression:**

| Metric | Use When | Avoid When |
|--------|----------|------------|
| MAE | Errors should be interpretable in original units | Need to penalize large errors |
| MSE / RMSE | Large errors are disproportionately bad | Units need to be interpretable (use MAE) |
| R² | Need to communicate variance explained | Comparing across datasets |
| MAPE | Relative error matters more than absolute | Target values can be zero or near-zero |

**Ranking / Retrieval:**

| Metric | Use When |
|--------|----------|
| NDCG | Ranking quality across all positions matters |
| Precision@K | Only top-K results are shown to users |
| Recall@K | Need to find as many relevant items as possible |
| MRR | First correct result is what matters |

**Key principle:** The metric must align with the business cost of errors. A model with 95% accuracy that misses all fraud cases in the 5% minority class is worse than a model with 85% accuracy that catches 70% of fraud.

### Phase 2: Validation Strategy

| Strategy | When to Use | Key Property |
|----------|-------------|--------------|
| Simple holdout | Large dataset (>100K samples), quick iteration | Fast, but estimate has higher variance |
| K-fold cross-validation | Medium dataset, need reliable estimate | More robust estimate, K× slower |
| Stratified K-fold | Imbalanced classes | Preserves class ratios in each fold |
| Time-series split | Temporal data, avoid future leakage | Train on past, validate on future |
| Group K-fold | Data has natural groups (patients, users) | No group appears in both train and validation |
| Nested CV | Need unbiased estimate AND hyperparameter tuning | Outer loop for evaluation, inner for tuning |

**Critical rule:** Your validation strategy must mirror how the model will be used. If the model predicts future events, validate on future data. If it predicts across user groups, validate with group-aware splits.

### Phase 3: Error Analysis

After computing aggregate metrics, investigate where the model fails:

1. **Confusion matrix** — For classification, identify which classes are confused with which
2. **Error buckets** — Group errors by input characteristics (length, category, source, time period)
3. **Worst examples** — Sort by prediction confidence; examine cases where the model was confident but wrong
4. **Subgroup analysis** — Compute metrics separately for each demographic or categorical subgroup
5. **Calibration check** — Does a predicted probability of 0.8 actually correspond to 80% correctness?

### Phase 4: Statistical Comparison

When comparing two models, never rely on a single number:

- **Paired t-test** on k-fold scores — tests whether mean performance differs significantly
- **Wilcoxon signed-rank test** — non-parametric alternative when normality is questionable
- **Bootstrap confidence intervals** — resample test set to get confidence bounds on any metric
- **McNemar's test** — for comparing classification models on the same test set (uses the confusion matrix of disagreements)

A 0.5% accuracy improvement with p=0.3 is not a real improvement. Always report confidence intervals or p-values alongside metric differences.

## Practical Templates

### Template 1: Evaluation Report Structure

```markdown
# Model Evaluation Report: [Model Name]

## Summary
| Metric | This Model | Baseline | Δ | p-value |
|--------|-----------|----------|---|---------|
| [metric] | [value ± CI] | [value] | [delta] | [p] |

## Validation Setup
- Strategy: [k-fold / holdout / time-series split]
- Test set size: [N]
- Data period: [date range]
- Preprocessing version: [commit hash]

## Subgroup Performance
| Subgroup | N | Metric | vs. Overall |
|----------|---|--------|-------------|
| [group A] | [n] | [val] | [+/- delta] |

## Error Analysis
- Most common failure mode: [description]
- Confident but wrong examples: [count]
- Calibration: [well-calibrated / overconfident / underconfident]

## Recommendation
[Deploy / Iterate / Retrain with X]
```

### Template 2: Quick Evaluation Script (Python)

```python
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model(model, X, y, n_splits=5):
    """Run stratified k-fold evaluation with detailed reporting."""
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    # Cross-validation scores
    scores = cross_val_score(model, X, y, cv=skf, scoring="f1_weighted")
    print(f"F1 (weighted): {scores.mean():.4f} ± {scores.std():.4f}")
    print(f"95% CI: [{scores.mean() - 1.96*scores.std():.4f}, "
          f"{scores.mean() + 1.96*scores.std():.4f}]")
    
    # Fit on full data for detailed analysis
    model.fit(X, y)
    y_pred = model.predict(X)
    
    print("\nClassification Report:")
    print(classification_report(y, y_pred))
    
    return scores

def compare_models(scores_a, scores_b, metric_name="Metric"):
    """Paired t-test between two models' cross-validation scores."""
    from scipy.stats import ttest_rel
    t_stat, p_value = ttest_rel(scores_a, scores_b)
    delta = scores_a.mean() - scores_b.mean()
    print(f"{metric_name}: A={scores_a.mean():.4f}, B={scores_b.mean():.4f}, "
          f"Δ={delta:+.4f}, p={p_value:.4f}")
    if p_value < 0.05:
        print("  → Statistically significant difference")
    else:
        print("  → No significant difference detected")
```

### Template 3: Subgroup Fairness Check

```python
def subgroup_analysis(y_true, y_pred, groups, metric_fn):
    """Compute metrics for each subgroup and compare to overall."""
    overall = metric_fn(y_true, y_pred)
    print(f"Overall: {overall:.4f}\n")
    print(f"{'Subgroup':<20} {'N':>6} {'Metric':>8} {'Δ Overall':>10}")
    print("-" * 48)
    for group in sorted(set(groups)):
        mask = [g == group for g in groups]
        g_true = [y for y, m in zip(y_true, mask) if m]
        g_pred = [y for y, m in zip(y_pred, mask) if m]
        g_score = metric_fn(g_true, g_pred)
        delta = g_score - overall
        flag = " ⚠" if abs(delta) > 0.05 else ""
        print(f"{group:<20} {len(g_true):>6} {g_score:>8.4f} {delta:>+10.4f}{flag}")
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Using accuracy on imbalanced data | Masks poor performance on minority class | Use F1, PR-AUC, or per-class metrics |
| Data leakage in validation | Overly optimistic performance estimates | Ensure no future or target information leaks into features |
| Evaluating on the training set | Measures memorization, not generalization | Always use a held-out test set never seen during training |
| Reporting only one metric | Hides important failure modes | Report at minimum: overall metric + per-class or subgroup metrics |
| Ignoring confidence intervals | Cannot tell if differences between models are real | Always report CI or p-values when comparing models |
| Using a single train-test split | Result may be lucky or unlucky | Use k-fold cross-validation for reliable estimates |

## Best Practices

1. **Define your evaluation strategy before training.** Knowing what you're optimizing for prevents metric shopping after seeing results.
2. **Always establish a baseline.** A dummy classifier, a heuristic, or the previous model gives context for whether your new model's score is meaningful.
3. **Report variance, not just mean.** A model with 90% ± 3% is more reliable than one with 91% ± 8%.
4. **Analyze errors, not just metrics.** A single confusing matrix or a handful of worst-case examples often reveals more than an aggregate number.
5. **Validate the validation.** Check that your test set distribution matches the production distribution. A test set from last year may not represent next month's data.
6. **Automate evaluation.** Every experiment should produce the same evaluation report with no manual steps. This prevents inconsistency and makes comparison reliable.
7. **Communicate uncertainty to stakeholders.** "The model is 92% accurate" is misleading. "The model achieves 92% ± 1.5% F1, with known lower performance on subgroup X" is honest and actionable.

## Tools & Resources

- [scikit-learn Evaluation Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) - Comprehensive metric implementations and scoring utilities
- [Evidently AI](https://www.evidentlyai.com/) - Open-source model monitoring and evaluation reports
- [DeepEval](https://github.com/confident-ai/deepeval) - Evaluation framework for LLM outputs
- [Ragas](https://github.com/explodinggradients/ragas) - Evaluation framework specifically for RAG systems
- [Classification Report Visualizer (Yellowbrick)](https://www.scikit-yb.org/en/latest/api/classifier/classification_report.html) - Visual classification reports
- [An Introduction to Evaluation Metrics](https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-61e04c1e2dd3) - Practical guide to choosing metrics

## Example Application

**Scenario**: A healthcare team builds a model to detect diabetic retinopathy from retinal images. The dataset has 95% negative cases and 5% positive. The team reports 97% accuracy and prepares for deployment.

**Application**:

1. *Metric audit* — Accuracy is misleading here. A model that predicts "negative" for every image achieves 95% accuracy. The team switches to recall (sensitivity) as the primary metric because missing a positive case (false negative) is clinically dangerous.

2. *Validation redesign* — The original random split allowed images from the same patient in both train and test. The team switches to group k-fold (grouped by patient ID) to prevent data leakage.

3. *Subgroup analysis* — Performance is computed separately for different image quality levels and patient demographics. The model achieves 89% recall on high-quality images but only 61% on low-quality images — a critical gap since clinic images are often low quality.

4. *Statistical comparison* — The new model (89% recall) is compared to the existing screening protocol (78% recall by human clinicians) using McNemar's test. p < 0.01 confirms the improvement is significant.

5. *Calibration* — The model's predicted probabilities are checked against actual outcomes. The model is overconfident (predicts 0.99 frequently), so the team applies temperature scaling before deployment.

**Outcome**: The evaluation reveals that the "97% accurate" model actually has serious gaps. After redesigning the evaluation, the team deploys with appropriate caveats: 89% recall overall, with a flagged subgroup (low-quality images) requiring human review. The model card documents these limitations clearly.

## Success Indicators

You know you've mastered model evaluation when:

- You can justify your choice of metric in terms of business or clinical cost of errors
- Your validation strategy mirrors the actual deployment scenario (temporal, grouped, or stratified as needed)
- You always report confidence intervals or variance alongside point estimates
- Your error analysis identifies specific, actionable failure patterns — not just "it fails sometimes"
- You check subgroup performance before declaring a model ready
- Your evaluation pipeline runs automatically and produces consistent reports
- Stakeholders understand the model's limitations because you communicated them clearly

## Related Skills

- [Algorithm Design](algorithm_design.md) - Understanding algorithms helps in selecting appropriate evaluation approaches
- [Data Analysis](../data-skills/data_analysis.md) - Statistical analysis skills underpin rigorous evaluation
- [MLOps](../devops-skills/mlops.md) - Evaluation integrates into production monitoring and retraining pipelines
- [Debugging](../behavior-skills/debugging.md) - Error analysis is a form of systematic debugging
