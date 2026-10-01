# Model Development

## Overview

Best practices and techniques for developing, training, and optimizing machine learning models.

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

# Load and explore data
df = pd.read_csv('data.csv')
print(df.describe())
print(df.isnull().sum())

# Split data (before any preprocessing!)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['target'])

# Save splits
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)
```

### 3. Baseline Model

Always start with a simple baseline:

```python
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dummy baseline (predicts most frequent class)
dummy = DummyClassifier(strategy='most_frequent')
dummy.fit(X_train, y_train)
baseline_score = accuracy_score(y_test, dummy.predict(X_test))

# Simple logistic regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_score = accuracy_score(y_test, lr.predict(X_test))

print(f"Baseline: {baseline_score:.3f}, LR: {lr_score:.3f}")
```

### 4. Iterative Improvement

**Cycle:**
1. Train model
2. Evaluate on validation set
3. Analyze errors
4. Hypothesize improvements
5. Implement and test
6. Repeat

---

## Training Best Practices

### Learning Rate Scheduling

```python
import torch.optim.lr_scheduler as lr_scheduler

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Step decay
scheduler = lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)

# Reduce on plateau
scheduler = lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5)

# Cosine annealing
scheduler = lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)

# Training loop
for epoch in range(num_epochs):
    train_one_epoch()
    val_loss = validate()
    scheduler.step(val_loss)  # or just scheduler.step() for StepLR
```

### Gradient Management

```python
# Gradient clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

# Gradient accumulation
accumulation_steps = 4
optimizer.zero_grad()

for i, (inputs, targets) in enumerate(dataloader):
    outputs = model(inputs)
    loss = criterion(outputs, targets) / accumulation_steps
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

### Regularization Techniques

```python
import torch.nn as nn

# Dropout
model.dropout = nn.Dropout(0.5)

# Weight decay (in optimizer)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)

# Batch normalization
model.bn = nn.BatchNorm2d(num_features)

# Label smoothing
criterion = nn.CrossEntropyLoss(label_smoothing=0.1)
```

---

## Hyperparameter Tuning

### Grid Search

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': [0.01, 0.1, 1]
}

grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.3f}")
```

### Random Search

```python
from scipy.stats import uniform, loguniform
from sklearn.model_selection import RandomizedSearchCV

param_dist = {
    'C': loguniform(0.001, 1000),
    'gamma': loguniform(0.001, 1),
}

random_search = RandomizedSearchCV(
    SVC(), 
    param_distributions=param_dist,
    n_iter=50,
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
```

### Bayesian Optimization

```python
from optuna import create_study

def objective(trial):
    lr = trial.suggest_loguniform('lr', 1e-5, 1e-2)
    dropout = trial.suggest_uniform('dropout', 0.1, 0.5)
    batch_size = trial.suggest_categorical('batch_size', [16, 32, 64])
    
    model = create_model(lr=lr, dropout=dropout)
    score = train_and_evaluate(model, batch_size=batch_size)
    return score

study = create_study(direction='maximize')
study.optimize(objective, n_trials=100)

print(f"Best trial: {study.best_trial.params}")
```

---

## Model Optimization

### Quantization

```python
import torch.quantization as quantization

# Post-training quantization
model_int8 = quantization.quantize_dynamic(
    model, 
    {nn.Linear, nn.Conv2d}, 
    dtype=torch.qint8
)

# Quantization-aware training
model.qconfig = quantization.get_default_qat_qconfig('fbgemm')
model_prepared = quantization.prepare_qat(model)

# Train...
train(model_prepared)

# Convert to quantized model
model_quantized = quantization.convert(model_prepared.eval())
```

### Pruning

```python
import torch.nn.utils.prune as prune

# L1 unstructured pruning
prune.l1_unstructured(model.conv1, name='weight', amount=0.3)

# Structured pruning (entire channels)
prune.ln_structured(model.conv1, name='weight', amount=0.3, n=2, dim=0)

# Make pruning permanent
prune.remove(model.conv1, 'weight')
```

### Knowledge Distillation

```python
class DistillationLoss(nn.Module):
    def __init__(self, temperature=4.0):
        super().__init__()
        self.temperature = temperature
        self.ce = nn.CrossEntropyLoss()
        
    def forward(self, student_logits, teacher_logits, targets):
        soft_targets = nn.functional.softmax(teacher_logits / self.temperature, dim=-1)
        student_log_probs = nn.functional.log_softmax(student_logits / self.temperature, dim=-1)
        
        distillation_loss = nn.functional.kl_div(
            student_log_probs, soft_targets, reduction='batchmean'
        ) * (self.temperature ** 2)
        
        hard_loss = self.ce(student_logits, targets)
        
        return 0.7 * distillation_loss + 0.3 * hard_loss
```

---

## Experiment Tracking

### MLflow

```python
import mlflow
import mlflow.pytorch

mlflow.set_experiment("image-classification")

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_param("batch_size", 32)
    
    # Train
    model = train()
    
    # Log metrics
    mlflow.log_metric("train_accuracy", train_acc)
    mlflow.log_metric("val_accuracy", val_acc)
    
    # Log model
    mlflow.pytorch.log_model(model, "model")
    
    # Log artifacts
    mlflow.log_artifact("confusion_matrix.png")
```

### Weights & Biases

```python
import wandb

wandb.init(project="my-project", config={
    "learning_rate": 0.001,
    "batch_size": 32,
})

for epoch in range(epochs):
    train_loss = train_one_epoch()
    val_acc = validate()
    
    wandb.log({
        "train_loss": train_loss,
        "val_accuracy": val_acc,
        "epoch": epoch
    })

wandb.finish()
```

---

## Common Pitfalls

### Data Leakage

❌ **Wrong:**
```python
# Scaling before split - LEAKAGE!
scaler.fit(df)
X_train, X_test = train_test_split(scaler.transform(df))
```

✅ **Correct:**
```python
# Split first, then fit scaler only on training data
X_train, X_test = train_test_split(df)
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Evaluation Bias

❌ **Wrong:**
```python
# Using test set for hyperparameter tuning
best_params = grid_search.fit(X_test, y_test)  # LEAKAGE!
```

✅ **Correct:**
```python
# Use validation set or cross-validation
best_params = grid_search.fit(X_train, y_train)
final_score = model.score(X_test, y_test)  # Only once!
```

### Reproducibility Issues

✅ **Always set seeds:**
```python
import random
import numpy as np
import torch

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
torch.backends.cudnn.deterministic = True
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
