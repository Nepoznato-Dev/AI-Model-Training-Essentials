# CUDA Out of Memory (OOM) Error

## Error Message

```
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate ...
```

or

```
RuntimeError: CUDA error: out of memory
```

## Cause

This error occurs when your GPU doesn't have enough memory to:
1. Load the model weights
2. Store intermediate activations during training
3. Handle the batch size you've specified

## Quick Solutions

### Solution 1: Reduce Batch Size (Fastest Fix)

In your training code, reduce the batch size:

```python
# Before
batch_size = 64

# After - try these values in order
batch_size = 32  # or 16, 8, 4, 2, 1
```

For CNN project, edit `main.py`:
```python
trainloader = DataLoader(trainset, batch_size=16, shuffle=True)  # Was 64
```

### Solution 2: Use Gradient Accumulation

Process small batches but accumulate gradients before updating weights:

```python
accumulation_steps = 4  # Accumulate over 4 batches

for i, (images, labels) in enumerate(trainloader):
    images, labels = images.to(device), labels.to(device)
    
    outputs = model(images)
    loss = criterion(outputs, labels) / accumulation_steps  # Normalize loss
    
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

### Solution 3: Enable Mixed Precision Training

Use automatic mixed precision (AMP) to reduce memory usage:

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for images, labels in trainloader:
    images, labels = images.to(device), labels.to(device)
    
    with autocast():  # Enable mixed precision
        outputs = model(images)
        loss = criterion(outputs, labels)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
    optimizer.zero_grad()
```

### Solution 4: Clear Cache Between Operations

Add explicit cache clearing:

```python
import torch

# After each epoch or heavy operation
torch.cuda.empty_cache()
```

### Solution 5: Use a Smaller Model

Switch to a smaller pre-trained model:

```python
# Instead of large models, use:
model_name = "google/flan-t5-small"  # Smallest
# or
model_name = "prajjwal1/bert-tiny"   # Tiny BERT
```

## For Specific Projects

### CNN Basics Project

Edit `guides/projects/cnn_basics/main.py`:

```python
# Line ~131: Reduce batch size
trainloader = DataLoader(trainset, batch_size=32, shuffle=True)  # Changed from 64

# Line ~175: Reduce epochs for testing
num_epochs = 5  # Changed from 10
```

### RAG Simple Project

The RAG project should work on CPU, but if using GPU:

```python
# In main.py, modify the pipeline call:
self.generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    max_new_tokens=50,
    device=-1,  # Force CPU if GPU OOM
    torch_dtype=torch.float32  # Avoid half precision issues
)
```

### Transformers Intro Project

```python
# Use smaller models
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased"  # Smaller than default
)
```

## Google Colab Specific Tips

1. **Check your GPU type:**
   ```python
   !nvidia-smi
   ```

2. **Free up memory:**
   ```python
   # Restart runtime if you get OOM
   # Runtime → Restart Runtime
   ```

3. **Use available GPU memory efficiently:**
   ```python
   import torch
   print(f"GPU Memory allocated: {torch.cuda.memory_allocated(0)/1e9:.2f} GB")
   print(f"GPU Memory reserved: {torch.cuda.memory_reserved(0)/1e9:.2f} GB")
   ```

## Prevention Strategies

### 1. Start Small
- Begin with tiny batch sizes (4 or 8)
- Use fewer epochs initially
- Test on a subset of data first

### 2. Monitor Memory Usage
```python
def print_gpu_memory():
    if torch.cuda.is_available():
        print(f"Allocated: {torch.cuda.memory_allocated(0)/1e9:.2f} GB")
        print(f"Reserved: {torch.cuda.memory_reserved(0)/1e9:.2f} GB")
        print(f"Max Allocated: {torch.cuda.max_memory_allocated(0)/1e9:.2f} GB")

print_gpu_memory()
```

### 3. Use Efficient Data Loading
```python
# Don't load everything into memory
trainloader = DataLoader(
    trainset, 
    batch_size=32, 
    shuffle=True,
    num_workers=2,  # Parallel data loading
    pin_memory=True  # Faster transfer to GPU
)
```

## When Nothing Works

### Option 1: Use CPU
Slower but guaranteed to work:

```python
device = torch.device("cpu")
# Or simply don't move data to GPU
```

### Option 2: Google Colab Free Tier
Get free GPU access:
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Upload your notebook
3. Runtime → Change runtime type → GPU

### Option 3: Cloud Services
- Kaggle Notebooks (free GPU)
- AWS Free Tier
- Azure for Students

## Related Errors

- [ImportError: Transformers](ImportError_Transformers.md) - Installation issues
- [Main README](../README.md) - Return to guides overview

---

**Last updated:** 2024  
**Applies to:** All GPU-accelerated projects
