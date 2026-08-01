<!-- 
This file was automatically translated from English to Korean.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기계 학습 평가와 워크플로

문제 정의부터 프로덕션 모니터링까지 이어지는 ML 수명주기를 실무 관점에서 정리한 가이드입니다. 특히 metrics, validation, debugging에 중점을 둡니다.

---

## ML 워크플로 (CRISP-ML)

1. **비즈니스 이해**: 목표와 성공 기준을 정의합니다.
2. **데이터 이해**: 사용 가능한 데이터를 탐색하고 품질 문제를 파악합니다.
3. **데이터 준비**: 데이터를 정제하고 변환한 뒤 분할합니다.
4. **모델링**: 모델을 학습시키고 hyperparameters를 조정합니다.
5. **평가**: 정해진 metrics를 기준으로 성능을 평가합니다.
6. **배포**: 모델을 프로덕션 환경에 서비스합니다.
7. **모니터링**: drift, 성능 저하, 이상 징후를 추적합니다.

이 과정은 한 번으로 끝나는 선형 절차가 아니라, 평가 결과에 따라 앞선 단계를 반복해서 돌아보는 순환형 과정입니다.

---

## 데이터 분할

### Train / Validation / Test Split
- **Training set** (~70%): 모델 파라미터를 학습하는 데 사용합니다.
- **Validation set** (~15%): hyperparameters를 조정하고 모델 변형을 선택하는 데 사용합니다.
- **Test set** (~15%): 일반화 성능을 추정하기 위해 마지막에 한 번만 사용합니다.

**중요:** 데이터 leakage를 막기 위해 test set은 최종 평가 전까지 완전히 손대지 않아야 합니다.

### Cross-Validation (k-fold)
데이터셋이 작다면 k-fold cross-validation을 사용합니다. 데이터를 k개의 fold로 나누고, k-1개로 학습한 뒤 나머지 1개로 검증하는 과정을 k번 반복합니다. 마지막에는 성능을 평균냅니다. 보통 k=5 또는 k=10을 많이 사용합니다.

### Stratified Splitting
클래스 불균형이 있는 classification 문제에서는 각 subset에서 클래스 비율이 유지되도록 stratified split을 사용합니다.

### Time-Based Splitting
시계열 데이터는 무작위로 섞지 말고 시간 순서대로 분할해야 합니다. 즉, 과거 데이터로 학습하고 미래 데이터로 테스트합니다.

---

## 평가 지표

### Classification Metrics

| Metric | 측정 내용 | 적합한 사용 상황 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | 클래스가 균형 잡힌 데이터셋 |
| **Precision** | TP / (TP + FP) | false positive 비용이 큰 경우 (예: spam detection) |
| **Recall** | TP / (TP + FN) | false negative 비용이 큰 경우 (예: cancer screening) |
| **F1-score** | precision과 recall의 조화평균 | 불균형 데이터셋, 단일 수치 평가 |
| **AUC-ROC** | ROC curve 아래 면적; TPR과 FPR의 균형 | threshold와 무관하게 분류기 전반 성능을 볼 때 |
| **AUC-PR** | Precision-Recall curve 아래 면적 | 매우 불균형한 데이터셋 |

**정의:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

### Regression Metrics

| Metric | 측정 내용 | 이상치 민감도 |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | 제곱 오차의 평균 | 높음 |
| **RMSE** (Root Mean Squared Error) | MSE의 제곱근 (target과 같은 단위) | 높음 |
| **MAE** (Mean Absolute Error) | 절대 오차의 평균 | 낮음 |
| **R²** (Coefficient of Determination) | 설명되는 분산의 비율 | 직접적이진 않지만 간접적으로 이상치에 민감 |

### Ranking and Retrieval Metrics
- **Precision@k**: 상위 k개 추천 항목 중 관련 있는 항목의 비율
- **Recall@k**: 전체 관련 항목 가운데 상위 k개 안에 포함된 비율
- **NDCG** (Normalised Discounted Cumulative Gain): 순위 위치에 따른 관련도를 반영
- **Hit Rate**: 관련 항목이 상위 k개 안에 하나라도 등장하는지 여부

### Generative / LLM Metrics
- **Perplexity**: hold-out 텍스트를 모델이 얼마나 "낯설게" 느끼는지 나타내는 값으로, 낮을수록 좋습니다.
- **BLEU**: 참조 번역과의 n-gram 중첩 정도를 보는 지표로, precision 중심입니다.
- **ROUGE**: 요약 평가에 자주 쓰이는 recall 중심 중첩 지표입니다.
- **BERTScore**: 문맥 임베딩을 이용한 의미적 유사도 지표로, BLEU보다 더 견고한 경우가 많습니다.
- **METEOR**: WordNet 동의어와 어간을 활용해 정렬합니다.

---

## 평가 시 흔한 함정

### 데이터 Leakage
test set의 정보가 의도치 않게 학습 과정에 스며들 때 발생합니다.
- **예방:** feature engineering, normalisation, hyperparameter tuning에 test 데이터를 절대 사용하지 않습니다.
- **탐지:** 점수가 지나치게 높게 나오면 leakage를 의심해야 합니다.

### Overfitting
학습 데이터에서는 성능이 좋지만 validation/test에서는 성능이 떨어지는 상태입니다.
- **완화:** regularisation을 적용하고, early stopping을 사용하며, 아키텍처를 단순화하거나 데이터를 더 수집합니다.

### Underfitting
학습 데이터와 검증 데이터 모두에서 성능이 낮은 상태입니다.
- **완화:** 더 복잡한 모델을 사용하거나, feature를 추가하거나, regularisation을 줄입니다.

### 불균형 데이터
- **완화:** class weight 적용, oversampling(SMOTE), undersampling, 또는 accuracy 대신 F1, AUC-PR 같은 적절한 지표를 사용합니다.

### Temporal Drift (Concept Drift)
시간이 지나면서 feature와 target의 관계가 달라지는 현상입니다.
- **완화:** 주기적으로 재학습하고, 성능을 모니터링하며, drift detection 알고리즘을 사용합니다.

---

## Hyperparameter Tuning

- **Grid Search**: 미리 정한 hyperparameter 조합을 전부 시도합니다. 단순하지만 계산 비용이 큽니다.
- **Random Search**: 분포에서 무작위 조합을 뽑아 탐색합니다. 고차원 공간에서는 grid search보다 효율적인 경우가 많습니다.
- **Bayesian Optimisation**: 목적 함수를 확률적으로 모델링하고, 더 유망한 hyperparameter를 지능적으로 선택합니다. 대표 라이브러리로 Optuna, Hyperopt, scikit-optimise가 있습니다.
- **Automated Tuning**: Optuna, Ray Tune, Weights & Biases Sweeps 같은 도구를 사용해 분산 환경에서 자동 탐색할 수 있습니다.

**자주 쓰이는 hyperparameter의 권장 탐색 범위:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers (NN) | 2 to 6 |
| Number of neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## 모델 선택과 검증

1. **Baseline model**: 간단한 휴리스틱이나 단순 모델(예: logistic regression, mean predictor)로 시작해 성능의 하한선을 설정합니다.
2. **Candidate models**: Random Forest, XGBoost, Neural Network 등 여러 모델 계열을 학습합니다.
3. 각 후보를 validation 절차로 검증합니다.
4. **Compare metrics**: 신뢰구간까지 함께 비교해 가장 좋은 후보를 선택합니다.
5. 보류해 둔 test set에서 **최종 평가**를 수행합니다.
6. **Error analysis**: 모델이 틀린 예시를 직접 살펴보고, 희귀 클래스나 애매한 입력 같은 패턴을 찾은 뒤 그 통찰을 데이터 준비나 feature engineering에 다시 반영합니다.

---

## 배포와 모니터링

### Serving Patterns
- **Batch inference**: 대량의 데이터를 오프라인으로 처리합니다 (예: 야간 추천 생성).
- **Online inference**: API를 통해 실시간 예측을 제공합니다 (예: 신용평가, fraud detection).
- **Streaming inference**: 이벤트 기반으로 낮은 지연 시간의 실시간 추론을 수행합니다 (예: IoT sensor alerts).

### Model Monitoring
- **성능 모니터링**: 정답 레이블을 확보할 수 있을 때 실서비스 데이터에서 accuracy/F1의 변화를 추적합니다.
- **데이터 drift**: 입력 feature 분포의 변화를 감시합니다 (예: PSI – Population Stability Index).
- **Concept drift**: 입력과 출력의 관계가 바뀌는지 모니터링합니다.
- **Prediction drift**: 예측 결과 분포의 변화를 추적합니다.
- **Latency와 throughput**: SLA (Service Level Agreements)를 충족하는지 확인합니다.

### Logging and Alerting
- 익명화(anonymisation)를 적용해 모든 prediction request와 response를 기록합니다.
- 다음 상황에 대한 alert를 설정합니다.
  - 성능이 의미 있게 하락했을 때
  - 누락되었거나 잘못된 입력의 비율이 높을 때
  - 모델 출력이 예상 범위를 벗어날 때

### Model Versioning and Registry
- model registry(예: MLflow, Weights & Biases, Sagemaker Model Registry)를 사용해 모델, metadata, 평가 결과를 저장하고 버전 관리합니다.
- training code와 데이터 버전(DVC 또는 Git LFS 사용)을 모델과 함께 보관합니다.

---

## 실무 워크플로 체크리스트

- [ ] Problem framed and success metric defined.
- [ ] 데이터 탐색 수행 완료 (missing values, outliers, distribution).
- [ ] Train/validation/test split 생성 완료 (필요 시 stratified).
- [ ] Baseline model 수립 완료.
- [ ] Candidate models 학습 및 검증 완료.
- [ ] Hyperparameters 조정 완료.
- [ ] Cross-validation을 통해 최적 모델 선택 완료.
- [ ] Test set에서 최종 평가 완료.
- [ ] Error analysis 수행 완료.
- [ ] 배포 계획 준비 완료 (serving infrastructure).
- [ ] Monitoring dashboard 구성 완료.
- [ ] Documentation (data card, model card) 작성 완료.
