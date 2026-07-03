<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 機器學習 Evaluation 和 Workflow

A practical 指南 to 這 ML lifecycle — from problem framing to production monitoring — 與 a focus on metrics, validation, 和 debugging.

---

## 這 ML Workflow (CRISP-ML)

1. **商業 Understanding**: Define 這 objective 和 success criteria.
2. **資料 Understanding**: Explore 可用 資料, identify quality issues.
3. **資料 Preparation**: Clean, transform, 和 split 資料.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess 效能 against metrics.
6. **部署**: Serve 這 model 在 production.
7. **Monitoring**: Track drift, 效能, 和 anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## 資料 Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit 這 model parameters.
- **Validation set** (~15%): Used to tune hyperparameters 和 select model variants.
- **Test set** (~15%): Used only once at 這 very end to estimate generalisation 效能.

**Important:** 這 test set must be kept completely untouched until final evaluation to avoid 資料 leakage.

### Cross-Validation (k-fold)
為 small datasets, use k-fold cross-validation: split 資料 into k folds, train on k-1, validate on 這 remaining, 和 repeat k times. Average 這 效能. k=5 or k=10 is common.

### Stratified Splitting
為 classification 與 imbalanced classes, use stratified splits to preserve class proportions 在 each subset.

### Time-Based Splitting
為 time-series 資料, split chronologically (train on past, test on 未來) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used 為 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean 的 precision 和 recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under 這 ROC curve; tradeoff between TPR 和 FPR | General classifier 效能 independent 的 threshold |
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
| **RMSE** (Root Mean Squared Error) | Square root 的 MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient 的 Determination) | Proportion 的 variance explained | None directly, but sensitive to outliers indirectly |

### Ranking 和 Retrieval Metrics
- **Precision@k**: Fraction 的 relevant items among top-k recommendations.
- **Recall@k**: Fraction 的 all relevant items that appear 在 top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts 為 position relevance.
- **Hit Rate**: Whether a relevant item appears 在 這 top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" 這 model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap 與 參考 translations (precision-focused).
- **ROUGE**: Recall-oriented overlap 為 summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms 和 stems.

---

## Evaluation Pitfalls

### 資料 Leakage
Occurs when information from 這 test set inadvertently influences training.
- **Prevent:** Never use test 資料 為 feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training 資料 but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify 架構, or collect more 資料.

### Underfitting
Model performs poorly on both training 和 validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced 資料
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
這 relationship between features 和 target changes over time.
- **Mitigate:** Retrain periodically, monitor 效能, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations 的 a predefined set 的 hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search 為 high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model 的 這 objective function 和 selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps 為 distributed tuning.

**Suggested search ranges 為 common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number 的 layers (NN) | 2 to 6 |
| Number 的 neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection 和 Validation

1. **Baseline model**: Start 與 a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural 網路).
3. **Cross-validate** each candidate on 這 validation set.
4. **Compare metrics** (與 confidence intervals) 和 select 這 best candidate.
5. **Final evaluation** on 這 held-out test set.
6. **Error analysis**: Look at 範例 這 model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) 和 feed insights back into 資料 preparation or feature engineering.

---

## 部署 和 Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes 的 資料 offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time 與 low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **效能 monitoring**: Track accuracy/F1 over time on live 資料 (when ground truth is 可用).
- **資料 drift**: Monitor changes 在 input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes 在 這 relationship between inputs 和 outputs.
- **Prediction drift**: Track 這 distribution 的 predicted outputs.
- **Latency 和 throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging 和 Alerting
- Log all prediction requests 和 responses (與 anonymisation).
- Set alerts 為:
  - Significant drop 在 效能.
  - High percentage 的 missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning 和 Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store 和 version models, metadata, 和 evaluation results.
- Store 這 training code 和 資料 version (via DVC or Git LFS) alongside 這 model.

---

## Practical Workflow Checklist

- [ ] Problem framed 和 success metric defined.
- [ ] 資料 exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained 和 validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] 部署 plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (資料 card, model card) completed.