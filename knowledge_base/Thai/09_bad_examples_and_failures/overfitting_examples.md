# Overfitting Examples

## Overview

Overfitting occurs when a model learns the training data too well, including noise and random fluctuations, resulting in poor generalization to new, unseen data. The model essentially memorizes the training set rather than learning underlying patterns, leading to high training accuracy but low test accuracy.

## When to Reference This Document

- Debugging poor model generalization
- Selecting appropriate regularization techniques
- Evaluating model complexity
- Designing training procedures
- Interpreting learning curves

## Common Overfitting Scenarios

### Excessive Model Capacity

**Bad Example**:
```python
# Using a massive model for a small dataset
from transformers import AutoModelForSequenceClassification

# 400M parameter model
model = AutoModelForSequenceClassification.from_pretrained("bert-large-uncased")

# Training on only 500 examples
train_dataset = load_dataset("small_dataset", split="train")  # 500 samples

# Model memorizes training data, fails on test set
# Train accuracy: 99%, Test accuracy: 45%
```

**Why It's Bad**:
- Too many parameters relative to data
- Model can memorize instead of learn
- Poor generalization to new data
- Wasted computational resources

**Solution**: Match model capacity to data size
```python
# Use smaller model or more data
if len(train_dataset) < 10000:
    # Small dataset: use smaller model
    model = AutoModelForSequenceClassification.from_pretrained("bert-tiny")
elif len(train_dataset) < 100000:
    # Medium dataset: use base model
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
else:
    # Large dataset: can use large model
    model = AutoModelForSequenceClassification.from_pretrained("bert-large-uncased")

# Or use data augmentation to increase effective dataset size
```

### No Regularization

**Bad Example**:
```python
# Neural network with no regularization
model = nn.Sequential(
    nn.Linear(100, 512),
    nn.ReLU(),
    nn.Linear(512, 512),
    nn.ReLU(),
    nn.Linear(512, 512),
    nn.ReLU(),
    nn.Linear(512, 10)
)

# No dropout, no weight decay, no batch norm
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loss decreases but validation loss increases after epoch 3
```

**Why It's Bad**:
- Weights grow unbounded
- Model fits noise in training data
- No constraint on complexity
- Large gap between train and validation performance

**Solution**: Apply regularization techniques
```python
# Add multiple forms of regularization
model = nn.Sequential(
    nn.Linear(100, 512),
    nn.BatchNorm1d(512),
    nn.ReLU(),
    nn.Dropout(0.5),
    
    nn.Linear(512, 512),
    nn.BatchNorm1d(512),
    nn.ReLU(),
    nn.Dropout(0.5),
    
    nn.Linear(512, 512),
    nn.BatchNorm1d(512),
    nn.ReLU(),
    nn.Dropout(0.5),
    
    nn.Linear(512, 10)
)

# Weight decay in optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)

# Early stopping
early_stopper = EarlyStopping(patience=5, min_delta=0.001)
```

### Training Too Long

**Bad Example**:
```python
# Fixed number of epochs without monitoring
for epoch in range(100):  # Always train for 100 epochs
    train_loss = train_one_epoch(model, train_loader)
    # No validation check
    # No early stopping

# Epoch 1-10: Both train and val loss decrease
# Epoch 11-50: Train loss decreases, val loss plateaus
# Epoch 51-100: Train loss near zero, val loss increases (overfitting)
```

**Why It's Bad**:
- Continues learning noise after signal is exhausted
- Validation performance degrades
- Wasted compute on later epochs
- Need to manually find optimal stopping point

**Solution**: Early stopping with validation monitoring
```python
class EarlyStopping:
    def __init__(self, patience=5, min_delta=0.001):
        self.patience = patience
        self.min_delta = min_delta
        self.best_loss = float('inf')
        self.counter = 0
        self.best_model_state = None
    
    def __call__(self, val_loss, model):
        if val_loss < self.best_loss - self.min_delta:
            self.best_loss = val_loss
            self.best_model_state = copy.deepcopy(model.state_dict())
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                model.load_state_dict(self.best_model_state)
                return True  # Stop training
        return False

# Usage
early_stopper = EarlyStopping(patience=5)
for epoch in range(max_epochs):
    train_loss = train_one_epoch(model, train_loader)
    val_loss = evaluate(model, val_loader)
    
    if early_stopper(val_loss, model):
        print(f"Early stopping at epoch {epoch}")
        break
```

### Data Leakage in Training

**Bad Example**:
```python
# Normalization using entire dataset statistics
mean = dataset.data.mean()  # Includes test set!
std = dataset.data.std()    # Includes test set!

dataset.data = (dataset.data - mean) / std

# Split after normalization
train_data, test_data = train_test_split(dataset.data, test_size=0.2)

# Model appears to perform well but leaks information
```

**Why It's Bad**:
- Test set information influences training
- Artificially inflated performance metrics
- Model fails on truly unseen data
- Invalid evaluation

**Solution**: Fit preprocessing on training data only
```python
# Split first
train_data, test_data = train_test_split(dataset.data, test_size=0.2)

# Fit normalizer on training data only
normalizer = StandardScaler()
normalizer.fit(train_data)  # Only sees training data

# Transform both sets
train_normalized = normalizer.transform(train_data)
test_normalized = normalizer.transform(test_data)  # Uses training stats

# Now evaluation is valid
```

### Insufficient Training Data

**Bad Example**:
```python
# Image classification with limited data
dataset = ImageDataset("rare_condition_images")  # Only 100 images total

# No augmentation, no transfer learning
model = ResNet50(num_classes=2)
train(model, dataset)  # Severe overfitting

# Train accuracy: 100%, Test accuracy: 50%
```

**Why It's Bad**:
- Not enough examples to learn patterns
- Model memorizes individual samples
- Cannot generalize to variations
- High variance in predictions

**Solution**: Data augmentation and transfer learning
```python
# Extensive data augmentation
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                         std=[0.229, 0.224, 0.225])
])

# Transfer learning with frozen backbone
model = resnet50(pretrained=True)
for param in model.parameters():
    param.requires_grad = False  # Freeze pretrained weights

# Only train classifier head
model.fc = nn.Linear(model.fc.in_features, num_classes)

# Fine-tune with augmented data
train(model, dataset, transform=transform)
```

## Real-World Scenarios

### Scenario 1: Medical Diagnosis Model
Model achieves 99% accuracy on training hospitals' data but only 60% at new hospitals due to memorizing hospital-specific artifacts.

### Scenario 2: Fraud Detection System
Model memorizes specific fraud patterns from historical data, missing novel fraud schemes in production.

### Scenario 3: Stock Price Predictor
Perfect fit on historical prices but catastrophic losses in live trading due to fitting noise rather than signal.

## Detection Patterns

Watch for these warning signs:
- Large gap between train and validation accuracy (>10%)
- Validation loss increasing while training loss decreases
- Perfect or near-perfect training accuracy
- Performance degrades on new data batches
- Learning curves diverge after certain epoch
- Model performs worse than simpler baselines

## Prevention Strategies

1. **Regularization**: Dropout, weight decay, batch normalization
2. **Early Stopping**: Monitor validation performance
3. **Cross-Validation**: K-fold to assess generalization
4. **Data Augmentation**: Increase effective dataset size
5. **Simplify Model**: Reduce capacity when appropriate
6. **More Data**: Collect additional training examples
7. **Ensemble Methods**: Average multiple models

## Testing Checklist

- [ ] Is train-validation gap less than 5%?
- [ ] Does validation loss stop decreasing?
- [ ] Are regularization techniques applied?
- [ ] Is early stopping implemented?
- [ ] Has cross-validation been performed?
- [ ] Is model capacity appropriate for data size?
- [ ] Has performance been tested on held-out data?

## Related Documents

- [[underfitting_examples]] - Opposite problem: model too simple
- [[bad_dataset_examples]] - Data quality issues causing overfitting
- [[benchmark_misuse]] - Improper evaluation masking overfitting
- [[code_smells]] - Signs of overfit implementation patterns
