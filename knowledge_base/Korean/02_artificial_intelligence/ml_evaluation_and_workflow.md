<!-- 
This file was automatically translated from English to Korean.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기계 학습 Evaluation 와 Workflow

A practical 가이드 to 그 ML lifecycle — from problem framing to production monitoring — 와 함께 a focus on metrics, validation, 와 debugging.

---

## 그 ML Workflow (CRISP-ML)

1. **비즈니스 Understanding**: Define 그 objective 와 success criteria.
2. **데이터 Understanding**: Explore 사용 가능 데이터, identify quality issues.
3. **데이터 Preparation**: Clean, transform, 와 split 데이터.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess 성능 against metrics.
6. **배포**: Serve 그 model 에서 production.
7. **Monitoring**: Track drift, 성능, 와 anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## 데이터 Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit 그 model parameters.
- **Validation set** (~15%): Used to tune hyperparameters 와 select model variants.
- **Test set** (~15%): Used only once at 그 very end to estimate generalisation 성능.

**Important:** 그 test set must be kept completely untouched until final evaluation to avoid 데이터 leakage.

### Cross-Validation (k-fold)
위한 small datasets, use k-fold cross-validation: split 데이터 into k folds, train on k-1, validate on 그 remaining, 와 repeat k times. Average 그 성능. k=5 or k=10 is common.

### Stratified Splitting
위한 classification 와 함께 imbalanced classes, use stratified splits to preserve class proportions 에서 each subset.

### Time-Based Splitting
위한 time-series 데이터, split chronologically (train on past, test on 미래) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used 위한 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean 의 precision 와 recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under 그 ROC curve; tradeoff between TPR 와 FPR | General classifier 성능 independent 의 threshold |
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
| **RMSE** (Root Mean Squared Error) | Square root 의 MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient 의 Determination) | Proportion 의 variance explained | None directly, but sensitive to outliers indirectly |

### Ranking 와 Retrieval Metrics
- **Precision@k**: Fraction 의 relevant items among top-k recommendations.
- **Recall@k**: Fraction 의 all relevant items that appear 에서 top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts 위한 position relevance.
- **Hit Rate**: Whether a relevant item appears 에서 그 top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" 그 model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap 와 함께 참조 translations (precision-focused).
- **ROUGE**: Recall-oriented overlap 위한 summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms 와 stems.

---

## Evaluation Pitfalls

### 데이터 Leakage
Occurs when information from 그 test set inadvertently influences training.
- **Prevent:** Never use test 데이터 위한 feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training 데이터 but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify 아키텍처, or collect more 데이터.

### Underfitting
Model performs poorly on both training 와 validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced 데이터
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
그 relationship between features 와 target changes over time.
- **Mitigate:** Retrain periodically, monitor 성능, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations 의 a predefined set 의 hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search 위한 high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model 의 그 objective function 와 selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps 위한 distributed tuning.

**Suggested search ranges 위한 common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number 의 layers (NN) | 2 to 6 |
| Number 의 neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection 와 Validation

1. **Baseline model**: Start 와 함께 a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural 네트워크).
3. **Cross-validate** each candidate on 그 validation set.
4. **Compare metrics** (와 함께 confidence intervals) 와 select 그 best candidate.
5. **Final evaluation** on 그 held-out test set.
6. **Error analysis**: Look at 예시 그 model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) 와 feed insights back into 데이터 preparation or feature engineering.

---

## 배포 와 Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes 의 데이터 offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time 와 함께 low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **성능 monitoring**: Track accuracy/F1 over time on live 데이터 (when ground truth is 사용 가능).
- **데이터 drift**: Monitor changes 에서 input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes 에서 그 relationship between inputs 와 outputs.
- **Prediction drift**: Track 그 distribution 의 predicted outputs.
- **Latency 와 throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging 와 Alerting
- Log all prediction requests 와 responses (와 함께 anonymisation).
- Set alerts 위한:
  - Significant drop 에서 성능.
  - High percentage 의 missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning 와 Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store 와 version models, metadata, 와 evaluation results.
- Store 그 training code 와 데이터 version (via DVC or Git LFS) alongside 그 model.

---

## Practical Workflow Checklist

- [ ] Problem framed 와 success metric defined.
- [ ] 데이터 exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained 와 validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] 배포 plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (데이터 card, model card) completed.