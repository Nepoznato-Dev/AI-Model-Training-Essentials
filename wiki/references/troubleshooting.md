# Troubleshooting Guide

## Overview

Common issues and solutions when working with AI/ML systems.

---

## Installation Issues

### CUDA/GPU Not Detected

**Symptoms:**
- `CUDA out of memory` errors
- Model training falls back to CPU
- `torch.cuda.is_available()` returns `False`

**Solutions:**
```bash
# Check CUDA installation
nvidia-smi
nvcc --version

# Verify PyTorch CUDA support
python -c "import torch; print(torch.version.cuda)"

# Reinstall with correct CUDA version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Package Version Conflicts

**Symptoms:**
- Import errors after installing new packages
- Incompatible dependency versions
- `ModuleNotFoundError` despite installation

**Solutions:**
```bash
# Create fresh virtual environment
python -m venv venv
source venv/bin/activate

# Install from requirements
pip install -r requirements.txt

# Or use conda for better dependency resolution
conda env create -f environment.yml
```

---

## Training Issues

### Loss Becomes NaN

**Possible Causes:**
- Learning rate too high
- Numerical instability
- Unnormalized data
- Gradient explosion

**Solutions:**
```python
# Reduce learning rate
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)  # Was 1e-3

# Add gradient clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

# Use mixed precision training
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()

with autocast():
    outputs = model(inputs)
    loss = criterion(outputs, targets)
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()

# Normalize inputs
from torchvision import transforms
transform = transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                  std=[0.229, 0.224, 0.225])
```

### Overfitting

**Symptoms:**
- Training accuracy >> Validation accuracy
- Validation loss increases while training loss decreases

**Solutions:**
```python
# Add dropout
model.dropout = nn.Dropout(0.5)

# Add weight decay
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-5)

# Use data augmentation
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
])

# Early stopping
best_val_loss = float('inf')
patience = 5
counter = 0

for epoch in range(num_epochs):
    val_loss = validate(model, val_loader)
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        counter = 0
        save_checkpoint(model)
    else:
        counter += 1
        if counter >= patience:
            print("Early stopping!")
            break
```

### Slow Training

**Solutions:**
```python
# Use DataLoader with multiple workers
loader = DataLoader(dataset, batch_size=64, num_workers=4, pin_memory=True)

# Enable cudnn benchmarking for fixed input sizes
torch.backends.cudnn.benchmark = True

# Use gradient accumulation for larger effective batch size
accumulation_steps = 4
for i, (inputs, targets) in enumerate(loader):
    outputs = model(inputs)
    loss = criterion(outputs, targets) / accumulation_steps
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()

# Profile to find bottlenecks
with torch.profiler.profile() as prof:
    train_one_epoch()
print(prof.key_averages().table(sort_by="cuda_time_total"))
```

---

## Inference Issues

### High Latency

**Solutions:**
```python
# Model optimization
import torch.ao.quantization
model_quantized = torch.ao.quantization.quantize_dynamic(
    model, {nn.Linear}, dtype=torch.qint8
)

# Use TorchScript for faster inference
scripted_model = torch.jit.script(model)
scripted_model.save("model.pt")

# Batch requests together
def batch_predict(inputs, batch_size=32):
    results = []
    for i in range(0, len(inputs), batch_size):
        batch = inputs[i:i+batch_size]
        with torch.no_grad():
            outputs = model(batch)
        results.extend(outputs)
    return results

# Use ONNX Runtime
import onnxruntime as ort
session = ort.InferenceSession("model.onnx")
outputs = session.run(None, {"input": input_data})
```

### Memory Issues During Inference

**Solutions:**
```python
# Clear cache
torch.cuda.empty_cache()

# Use smaller batch sizes
batch_size = 1  # Instead of 32

# Move model to CPU for occasional inference
model.cpu()
with torch.no_grad():
    output = model(input)
model.cuda()

# Use gradient checkpointing for large models
from torch.utils.checkpoint import checkpoint
```

---

## Model Quality Issues

### Poor Generalization

**Checklist:**
- [ ] Data distribution matches production
- [ ] No data leakage from test to train
- [ ] Sufficient training data
- [ ] Appropriate model capacity
- [ ] Proper evaluation metrics

**Solutions:**
```python
# Check for data leakage
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ensure proper preprocessing fit only on training data
scaler.fit(X_train)  # NOT on full dataset
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Use cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"CV Score: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### Class Imbalance

**Solutions:**
```python
# Use weighted loss
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
criterion = nn.CrossEntropyLoss(weight=torch.tensor(class_weights))

# Oversample minority class
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Use focal loss for hard examples
class FocalLoss(nn.Module):
    def __init__(self, alpha=1, gamma=2):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
    
    def forward(self, inputs, targets):
        ce_loss = nn.functional.cross_entropy(inputs, targets, reduction='none')
        pt = torch.exp(-ce_loss)
        focal_loss = self.alpha * (1-pt)**self.gamma * ce_loss
        return focal_loss.mean()
```

---

## Deployment Issues

### API Timeouts

**Solutions:**
```python
# Add async processing
from fastapi import BackgroundTasks

@app.post("/predict")
async def predict(request: PredictionRequest, background_tasks: BackgroundTasks):
    job_id = generate_id()
    background_tasks.add_task(process_prediction, job_id, request)
    return {"job_id": job_id, "status": "processing"}

# Increase timeout settings
# uvicorn main:app --timeout-keep-alive 300

# Use task queue
from celery import Celery
celery_app = Celery('tasks', broker='redis://localhost:6379')

@celery_app.task
def predict_task(input_data):
    return model.predict(input_data)
```

### Model Version Mismatch

**Solutions:**
```python
# Include version info in model artifact
model_info = {
    "version": "1.2.3",
    "pytorch_version": torch.__version__,
    "python_version": sys.version,
    "training_date": "2024-01-15",
    "git_commit": get_git_commit()
}
torch.save({"model": model.state_dict(), "info": model_info}, "model.pt")

# Validate on load
checkpoint = torch.load("model.pt")
assert checkpoint["info"]["pytorch_version"] == torch.__version__

# Use model registry
import mlflow
mlflow.pytorch.load_model("runs:/<run_id>/model")
```

---

## Debugging Tips

### Print Model Architecture
```python
print(model)
for name, param in model.named_parameters():
    print(f"{name}: {param.shape}, requires_grad={param.requires_grad}")
```

### Check Tensor Shapes
```python
def debug_forward(self, x):
    print(f"Input shape: {x.shape}")
    x = self.layer1(x)
    print(f"After layer1: {x.shape}")
    # ... continue for each layer
    return x
```

### Monitor Gradients
```python
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: grad_mean={param.grad.mean():.6f}, grad_std={param.grad.std():.6f}")
```

---

## Getting Help

### Useful Commands
```bash
# Check system info
python -c "import torch; print(f'PyTorch: {torch.__version__}, CUDA: {torch.version.cuda}')"

# List GPU usage
nvidia-smi

# Check disk space
df -h

# Monitor memory
free -h
```

### Resources
- [PyTorch Forums](https://discuss.pytorch.org/)
- [Stack Overflow - Machine Learning](https://stackoverflow.com/questions/tagged/machine-learning)
- [GitHub Issues](https://github.com/pytorch/pytorch/issues)
- [Hugging Face Forums](https://discuss.huggingface.co/)

---

## See Also

- [API Reference](api_reference.md)
- [Best Practices Checklist](checklist.md)
- [Glossary](glossary.md)
