<!-- 
This file was automatically translated from English to Japanese.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 機械学習 Evaluation と Workflow

A practical ガイド to その ML lifecycle — from problem framing to production monitoring — と a focus on metrics, validation, と debugging.

---

## その ML Workflow (CRISP-ML)

1. **ビジネス Understanding**: Define その objective と success criteria.
2. **データ Understanding**: Explore 利用可能 データ, identify quality issues.
3. **データ Preparation**: Clean, transform, と split データ.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess パフォーマンス against metrics.
6. **デプロイ**: Serve その model で production.
7. **Monitoring**: Track drift, パフォーマンス, と anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## データ Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit その model parameters.
- **Validation set** (~15%): Used to tune hyperparameters と select model variants.
- **Test set** (~15%): Used only once at その very end to estimate generalisation パフォーマンス.

**Important:** その test set must be kept completely untouched until final evaluation to avoid データ leakage.

### Cross-Validation (k-fold)
のために small datasets, use k-fold cross-validation: split データ into k folds, train on k-1, validate on その remaining, と repeat k times. Average その パフォーマンス. k=5 or k=10 is common.

### Stratified Splitting
のために classification と imbalanced classes, use stratified splits to preserve class proportions で each subset.

### Time-Based Splitting
のために time-series データ, split chronologically (train on past, test on 未来) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used のために |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean の precision と recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under その ROC curve; tradeoff between TPR と FPR | General classifier パフォーマンス independent の threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced datasets |

**Definitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

### Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root の MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient の Determination) | Proportion の variance explained | None directly, but sensitive to outliers indirectly |

### Ranking と Retrieval Metrics
- **Precision@k**: Fraction の relevant items among top-k recommendations.
- **Recall@k**: Fraction の all relevant items that appear で top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts のために position relevance.
- **Hit Rate**: Whether a relevant item appears で その top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" その model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap と リファレンス translations (precision-focused).
- **ROUGE**: Recall-oriented overlap のために summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms と stems.

---

## Evaluation Pitfalls

### データ Leakage
Occurs when information from その test set inadvertently influences training.
- **Prevent:** Never use test データ のために feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training データ but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify アーキテクチャ, or collect more データ.

### Underfitting
Model performs poorly on both training と validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced データ
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
その relationship between features と target changes over time.
- **Mitigate:** Retrain periodically, monitor パフォーマンス, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations の a predefined set の hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search のために high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model の objective function と selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps のために distributed tuning.

**Suggested search ranges のために common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number の layers (NN) | 2 to 6 |
| Number の neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection と Validation

1. **Baseline model**: Start と a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural ネットワーク).
3. **Cross-validate** each candidate on その validation set.
4. **Compare metrics** (と confidence intervals) と select その best candidate.
5. **Final evaluation** on その held-out test set.
6. **Error analysis**: Look at 例 その model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) と feed insights back into データ preparation or feature engineering.

---

## デプロイ と Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes の データ offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time と low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **パフォーマンス monitoring**: Track accuracy/F1 over time on live データ (when ground truth is 利用可能).
- **データ drift**: Monitor changes で input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes で その relationship between inputs と outputs.
- **Prediction drift**: Track その distribution の predicted outputs.
- **Latency と throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging と Alerting
- Log all prediction requests と responses (と anonymisation).
- Set alerts のために:
  - Significant drop で パフォーマンス.
  - High percentage の missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning と Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store と version models, metadata, と evaluation results.
- Store その training code と データ version (via DVC or Git LFS) alongside その model.

---

## Practical Workflow Checklist

- [ ] Problem framed と success metric defined.
- [ ] データ exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained と validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] デプロイ plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (データ card, model card) completed.