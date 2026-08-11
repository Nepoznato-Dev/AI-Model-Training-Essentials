# Model Development

## Overview

Best practices and techniques for developing, training, and optimizing machine learning models.

> **Example status:** Code on this page is intended to be runnable when its stated dependencies are installed. Version-sensitive APIs are called out explicitly.

---

## Development Workflow

### 1. Problem Definition

**Key Questions:**
- What business problem are we solving?
- What are the success metrics?
- What data is available?
- What are the constraints (latency, cost, interpretability)?

**Deliverables:**
- Problem statement document
- Success criteria definition
- Data availability assessment
- Risk analysis

### 2. Data Preparation

```python
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
print(df.describe())
print(df.isnull().sum())

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["target"],
)

train_df.to_csv("train.csv", index=False)
test_df.to_csv("test.csv", index=False)
```

For workflows that tune hyperparameters or select checkpoints, create a validation split (or use cross-validation) from the training portion. Keep the final test set untouched until the end.

### 3. Baseline Model

A baseline should be evaluated without turning the final test set into a tuning target. For a simple example, split training data into train/validation and reserve the test set for final evaluation.

```python
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_fit, X_val, y_fit, y_val = train_test_split(
    X_train,
    y_train,
    test_size=0.2,
    random_state=42,
    stratify=y_train,
)

dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_fit, y_fit)
baseline_score = accuracy_score(y_val, dummy.predict(X_val))

lr = LogisticRegression(max_iter=1000)
lr.fit(X_fit, y_fit)
lr_score = accuracy_score(y_val, lr.predict(X_val))

print(f"Validation baseline: {baseline_score:.3f}, LR: {lr_score:.3f}")
```

Only after model selection should the final model be evaluated on `X_test, y_test`.

### 4. Iterative Improvement

**Cycle:**
1. Train model
2. Evaluate on validation data
3. Analyze errors
4. Hypothesize improvements
5. Implement and test
6. Repeat

---

## Training Best Practices

### Learning Rate Scheduling

Do not use one `scheduler.step(...)` call for every scheduler type. The APIs differ.

**StepLR:**

```python
from torch.optim.lr_scheduler import StepLR

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
scheduler = StepLR(optimizer, step_size=30, gamma=0.1)

for epoch in range(num_epochs):
    train_one_epoch()
    validate()
    scheduler.step()
```

**ReduceLROnPlateau:**

```python
from torch.optim.lr_scheduler import ReduceLROnPlateau

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
scheduler = ReduceLROnPlateau(optimizer, mode="min", factor=0.5, patience=5)

for epoch in range(num_epochs):
    train_one_epoch()
    val_loss = validate()
    scheduler.step(val_loss)
```

**CosineAnnealingLR:**

```python
from torch.optim.lr_scheduler import CosineAnnealingLR

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
scheduler = CosineAnnealingLR(optimizer, T_max=num_epochs)

for epoch in range(num_epochs):
    train_one_epoch()
    validate()
    scheduler.step()
```

### Gradient Management

**Gradient clipping:**

```python
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

Call gradient clipping after `loss.backward()` and before `optimizer.step()`.

**Gradient accumulation:**

```python
accumulation_steps = 4
optimizer.zero_grad(set_to_none=True)

for i, (inputs, targets) in enumerate(dataloader):
    outputs = model(inputs)
    loss = criterion(outputs, targets) / accumulation_steps
    loss.backward()

    if (i + 1) % accumulation_steps == 0 or (i + 1) == len(dataloader):
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)
```

The final condition matters when the number of batches is not evenly divisible by `accumulation_steps`.

### Regularization Techniques

Dropout and BatchNorm must be part of the model's `forward()` path; assigning a module as an attribute does not automatically apply it.

```python
import torch.nn as nn

class Classifier(nn.Module):
    def __init__(self, features, classes):
        super().__init__()
        self.dropout = nn.Dropout(0.5)
        self.bn = nn.BatchNorm1d(features)
        self.fc = nn.Linear(features, classes)

    def forward(self, x):
        x = self.bn(x)
        x = self.dropout(x)
        return self.fc(x)
```

Weight decay and label smoothing remain optimizer/loss configuration choices:

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
criterion = nn.CrossEntropyLoss(label_smoothing=0.1)
```

---

## Hyperparameter Tuning

### Grid Search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf"],
    "gamma": [0.01, 0.1, 1],
}

grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring="accuracy")
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.3f}")
```

The cross-validation folds above are drawn from the training data. Keep the final test set outside the search.

### Random Search

```python
from scipy.stats import loguniform
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC

param_dist = {
    "C": loguniform(0.001, 1000),
    "gamma": loguniform(0.001, 1),
}

random_search = RandomizedSearchCV(
    SVC(),
    param_distributions=param_dist,
    n_iter=50,
    cv=5,
    random_state=42,
)
random_search.fit(X_train, y_train)
```

### Bayesian Optimization

Optuna must be installed separately for this example. Modern Optuna uses `suggest_float(..., log=True)` rather than the deprecated `suggest_loguniform`/`suggest_uniform` helpers.

```python
import optuna

def objective(trial):
    lr = trial.suggest_float("lr", 1e-5, 1e-2, log=True)
    dropout = trial.suggest_float("dropout", 0.1, 0.5)
    batch_size = trial.suggest_categorical("batch_size", [16, 32, 64])

    model = create_model(lr=lr, dropout=dropout)
    return train_and_evaluate(model, batch_size=batch_size)

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)

print(f"Best trial: {study.best_trial.params}")
```

`train_and_evaluate()` should evaluate against validation data or cross-validation folds, not the final test set.

---

## Model Optimization

### Quantization

Dynamic quantization is primarily intended for supported layers such as `nn.Linear` and recurrent layers. Do not pass `nn.Conv2d` to the dynamic quantization example as a generic rule.

```python
from torch.ao.quantization import quantize_dynamic
import torch.nn as nn

model_int8 = quantize_dynamic(
    model,
    {nn.Linear},
    dtype=torch.qint8,
)
```

For convolutional networks, use an appropriate static quantization or quantization-aware training workflow for the specific PyTorch version and backend.

### Pruning

```python
import torch.nn.utils.prune as prune

prune.l1_unstructured(model.conv1, name="weight", amount=0.3)
prune.ln_structured(model.conv1, name="weight", amount=0.3, n=2, dim=0)
prune.remove(model.conv1, "weight")
```

### Knowledge Distillation

When generating teacher logits, avoid retaining a teacher computation graph.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DistillationLoss(nn.Module):
    def __init__(self, temperature=4.0):
        super().__init__()
        self.temperature = temperature
        self.ce = nn.CrossEntropyLoss()

    def forward(self, student_logits, teacher_logits, targets):
        temperature = self.temperature
        soft_targets = F.softmax(teacher_logits / temperature, dim=-1)
        student_log_probs = F.log_softmax(student_logits / temperature, dim=-1)
        distillation_loss = F.kl_div(
            student_log_probs,
            soft_targets,
            reduction="batchmean",
        ) * (temperature ** 2)
        hard_loss = self.ce(student_logits, targets)
        return 0.7 * distillation_loss + 0.3 * hard_loss

teacher.eval()
with torch.no_grad():
    teacher_logits = teacher(inputs)

student_logits = student(inputs)
distill_criterion = DistillationLoss(temperature=4.0)
loss = distill_criterion(student_logits, teacher_logits, targets)
```

---

## Experiment Tracking

### MLflow

```python
import mlflow
import mlflow.pytorch

mlflow.set_experiment("image-classification")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_param("batch_size", 32)

    model = train()

    mlflow.log_metric("train_accuracy", train_acc)
    mlflow.log_metric("val_accuracy", val_acc)
    mlflow.pytorch.log_model(model, "model")
    mlflow.log_artifact("confusion_matrix.png")
```

### Weights & Biases

```python
import wandb

wandb.init(
    project="my-project",
    config={"learning_rate": 0.001, "batch_size": 32},
)

for epoch in range(epochs):
    train_loss = train_one_epoch()
    val_acc = validate()
    wandb.log({
        "train_loss": train_loss,
        "val_accuracy": val_acc,
        "epoch": epoch,
    })

wandb.finish()
```

---

## Common Pitfalls

### Data Leakage

❌ **Wrong:**

```python
scaler.fit(df)
X_train, X_test = train_test_split(scaler.transform(df))
```

The scaler has already seen the test data in this example.

✅ **Correct:**

```python
X_train, X_test = train_test_split(df)
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

In production pipelines, fit preprocessing only on training data and apply the fitted transformer to validation/test data.

### Evaluation Bias

❌ **Wrong:**

```python
best_params = grid_search.fit(X_test, y_test)
```

✅ **Correct:**

```python
best_params = grid_search.fit(X_train, y_train)
# Select/retrain the final model using the training data and chosen parameters.
final_score = model.score(X_test, y_test)
```

### Reproducibility

Seeds improve reproducibility but do not guarantee bit-for-bit identical results across all hardware and software configurations. Record the Python/library versions, hardware, dataset revision, and relevant deterministic settings as well.

```python
import random
import numpy as np
import torch

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
```

---

## Related Resources

- [Getting Started](getting_started.md)
- [API Reference](references/api_reference.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Best Practices Checklist](references/checklist.md)

## External References

- [PyTorch Training Best Practices](https://pytorch.org/tutorials/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Deep Learning Book](https://www.deeplearningbook.org/)
