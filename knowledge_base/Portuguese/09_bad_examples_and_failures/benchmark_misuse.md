# Benchmark Misuse

## Overview

Benchmarks are standardized tests used to evaluate and compare model performance. Benchmark misuse occurs when benchmarks are applied incorrectly, interpreted improperly, or gamed in ways that don't reflect real-world performance. This leads to misleading conclusions, wasted resources, and models that fail in production.

## When to Reference This Document

- Selecting evaluation benchmarks
- Interpreting benchmark results
- Comparing model performance
- Designing evaluation strategies
- Avoiding common evaluation pitfalls

## Common Benchmark Misuse Patterns

### Training on Test Data

**Bad Example**:
```python
# Accidentally including test set in training
train_data = load_dataset("benchmark")
test_data = load_dataset("benchmark", split="test")

# Bug: concatenating train and test before splitting
all_data = pd.concat([train_data, test_data])
train_final, val_final = train_test_split(all_data, test_size=0.2)

# Model trained on test data!
# Reports 98% accuracy but this is data leakage

# Or worse: hyperparameter tuning on test set
for lr in [0.001, 0.01, 0.1]:
    model = train(train_data, lr=lr)
    # Evaluating on TEST set to choose hyperparameters
    accuracy = evaluate(model, test_data)  
    # This makes test set into validation set!
```

**Why It's Bad**:
- Inflated performance metrics
- Invalid comparisons with other work
- Model fails on truly unseen data
- Scientific misconduct (if intentional)

**Solution**: Strict data separation
```python
# Proper workflow
train_data = load_dataset("benchmark", split="train")
val_data = load_dataset("benchmark", split="validation")
test_data = load_dataset("benchmark", split="test")

# Train on train only
model = train(train_data)

# Tune hyperparameters on validation
best_lr = None
best_val_acc = 0
for lr in [0.001, 0.01, 0.1]:
    model = train(train_data, lr=lr)
    val_acc = evaluate(model, val_data)  # Validation set
    if val_acc > best_val_acc:
        best_lr = lr
        best_val_acc = val_acc

# Final evaluation on test (ONLY ONCE)
final_model = train(train_data, lr=best_lr)
test_acc = evaluate(final_model, test_data)  # Test set - final eval only

print(f"Test accuracy: {test_acc}")
# Never use test results to modify model
```

### Cherry-Picking Metrics

**Bad Example**:
```python
# Model has poor overall accuracy but high precision on one class
results = {
    "accuracy": 0.45,      # Don't report this
    "precision_class_0": 0.95,  # Report this!
    "recall_class_0": 0.30,     # Don't report this
    "f1_macro": 0.42,      # Don't report this
    "auc_roc": 0.55        # Don't report this
}

# Paper claims: "Our model achieves 95% precision!"
# Reality: Model predicts everything as class 0
```

**Why It's Bad**:
- Misleading performance claims
- Hides model weaknesses
- Cannot reproduce in practice
- Unethical reporting

**Solution**: Report comprehensive metrics
```python
def report_comprehensive_metrics(y_true, y_pred):
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_macro": precision_score(y_true, y_pred, average='macro'),
        "recall_macro": recall_score(y_true, y_pred, average='macro'),
        "f1_macro": f1_score(y_true, y_pred, average='macro'),
        "f1_weighted": f1_score(y_true, y_pred, average='weighted'),
        "auc_roc": roc_auc_score(y_true, y_pred_proba, multi_class='ovr'),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
        "per_class_f1": f1_score(y_true, y_pred, average=None).tolist()
    }
    
    # Also report baseline performance
    metrics["majority_baseline"] = max(Counter(y_true).values()) / len(y_true)
    
    return metrics

# All metrics must be reported, not just favorable ones
```

### Inappropriate Baselines

**Bad Example**:
```python
# Comparing sophisticated model to trivial baseline
our_model = LargeTransformerModel()
our_model.fit(complex_features)
our_accuracy = 0.72

# Baseline: random guessing
random_baseline = 0.50  # For binary classification

# Paper claims: "22% improvement over baseline!"
# Appropriate baseline would be:
# - Previous SOTA: 0.71
# - Simple logistic regression: 0.68
# - Industry standard: 0.70
```

**Why It's Bad**:
- Exaggerates contribution
- Misleads about actual improvement
- Wastes reader time
- Damages credibility

**Solution**: Use appropriate baselines
```python
def establish_baselines(dataset):
    baselines = {}
    
    # Majority class baseline
    baselines["majority"] = majority_class_accuracy(dataset)
    
    # Simple models
    baselines["logistic_regression"] = train_and_eval(
        LogisticRegression(), dataset
    )
    baselines["naive_bayes"] = train_and_eval(
        GaussianNB(), dataset
    )
    
    # Previous SOTA (from literature)
    baselines["previous_sota"] = 0.71  # Cite paper
    
    # Industry standard / heuristic
    baselines["industry_heuristic"] = run_industry_baseline(dataset)
    
    return baselines

# Compare against all relevant baselines
baselines = establish_baselines(dataset)
our_model_score = train_and_eval(our_model, dataset)

improvement_vs_sota = our_model_score - baselines["previous_sota"]
# Report: "2% absolute improvement over previous SOTA"
```

### Dataset Shift Ignored

**Bad Example**:
```python
# Benchmark trained and tested on same distribution
benchmark_data = load_from_single_source()

# Model achieves 95% on benchmark
# But real-world data has different distribution:
# - Different demographics
# - Different time period
# - Different data collection method
# - Different label definitions

# Model drops to 60% in production
```

**Why It's Bad**:
- Benchmark doesn't reflect reality
- False confidence in model
- Production failures
- Wasted deployment effort

**Solution**: Test for robustness and generalization
```python
def evaluate_robustness(model, datasets):
    results = {}
    
    # Original benchmark
    results["original"] = evaluate(model, benchmark_data)
    
    # Out-of-distribution tests
    results["temporal_shift"] = evaluate(model, data_from_different_time())
    results["geographic_shift"] = evaluate(model, data_from_different_region())
    results["demographic_shift"] = evaluate(model, data_from_different_demographic())
    
    # Robustness tests
    results["noise_robustness"] = evaluate(model, add_noise(benchmark_data))
    results["missing_values"] = evaluate(model, add_missing_values(benchmark_data))
    
    # Real-world pilot
    results["production_pilot"] = evaluate(model, production_data_sample())
    
    # Report all results, not just original benchmark
    return results

# Only deploy if model performs well across all conditions
```

### Multiple Testing Without Correction

**Bad Example**:
```python
# Trying 50 different model configurations
best_result = 0
for config in all_configurations:
    model = train(config)
    score = evaluate(model, test_set)
    if score > best_result:
        best_result = score
        best_config = config

# Report: "Our best model achieves 87% accuracy!"
# Problem: With 50 tries, getting 87% by chance is likely
# True performance on new data: 75%
```

**Why It's Bad**:
- Overfitting to test set through selection
- Inflated performance estimates
- Results don't generalize
- Statistical significance ignored

**Solution**: Proper statistical methodology
```python
# Option 1: Hold out a separate test set
train_val_data, final_test_data = split(data, test_size=0.2)

# Do all experimentation on train_val
best_config = hyperparameter_search(train_val_data)

# Evaluate ONLY ONCE on final_test
final_score = evaluate(best_config, final_test_data)

# Option 2: Cross-validation with correction
from sklearn.model_selection import cross_val_score
from statsmodels.stats.multitest import multipletests

scores = []
for fold in range(10):
    model = train_on_fold(fold)
    score = evaluate_on_fold(fold)
    scores.append(score)

mean_score = np.mean(scores)
std_score = np.std(scores)
confidence_interval = f"{mean_score:.3f} ± {1.96 * std_score/np.sqrt(len(scores)):.3f}"

# Option 3: Nested cross-validation
from sklearn.model_selection import GridSearchCV, cross_val_score

inner_cv = KFold(n_splits=5)  # For hyperparameter tuning
outer_cv = KFold(n_splits=5)  # For performance estimation

grid_search = GridSearchCV(model, param_grid, cv=inner_cv)
nested_scores = cross_val_score(grid_search, X, y, cv=outer_cv)
```

## Real-World Scenarios

### Scenario 1: NLP Model Comparison
Model A reports higher GLUE score than Model B, but GLUE doesn't include the specific task they actually need, leading to wrong model selection.

### Scenario 2: Computer Vision Benchmark
Model trained on ImageNet achieves 90% accuracy but fails on medical images due to domain shift not captured in benchmark.

### Scenario 3: Recommendation System
Offline benchmark shows 30% improvement, but online A/B test shows no improvement due to metric mismatch.

## Detection Patterns

Watch for these warning signs:
- Unusually high benchmark scores
- Missing baseline comparisons
- No confidence intervals reported
- Test set mentioned in training section
- Many models tried, only best reported
- Benchmark differs from use case

## Prevention Strategies

1. **Strict Data Separation**: Never train on test data
2. **Comprehensive Metrics**: Report all relevant metrics
3. **Appropriate Baselines**: Compare to meaningful alternatives
4. **Distribution Testing**: Evaluate on varied distributions
5. **Statistical Rigor**: Use proper statistical methods
6. **Real-World Validation**: Test in production-like conditions
7. **Transparent Reporting**: Disclose all experimental details

## Testing Checklist

- [ ] Is test set completely held out from training?
- [ ] Are all relevant metrics reported?
- [ ] Are baselines appropriate and fair?
- [ ] Has robustness to distribution shift been tested?
- [ ] Are confidence intervals provided?
- [ ] Is multiple testing accounted for?
- [ ] Does benchmark reflect real use case?

## Related Documents

- [[overfitting_examples]] - Overfitting to benchmarks
- [[bad_dataset_examples]] - Dataset issues affecting benchmarks
- [[misinformation_examples]] - Misleading benchmark claims
- [[code_smells]] - Signs of benchmark gaming in code
