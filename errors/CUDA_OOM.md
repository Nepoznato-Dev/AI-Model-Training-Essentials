# CUDA Out of Memory (OOM) Error 🔥

**Error Message:**
```
RuntimeError: CUDA out of memory. Tried to allocate X MiB (GPU Y; Z GiB total capacity; ...)
```

---

## What This Means

Your GPU ran out of video memory (VRAM) while trying to run the model. This is the **most common error** in deep learning!

---

## Quick Fixes (Try in Order)

### Fix 1: Reduce Batch Size ⭐ (Most Effective)

```python
# Before
batch_size = 64

# After - try smaller sizes
batch_size = 32  # or 16, 8, 4, even 2 or 1
```

**Why it works:** Smaller batches use less memory at once.

---

### Fix 2: Use Gradient Accumulation

Train with effective large batches using small actual batches:

```python
# Instead of batch_size=64, use this:
actual_batch_size = 8  # Fits in memory
accumulation_steps = 8  # 8 * 8 = 64 effective batch size

for i, batch in enumerate(dataloader):
    loss = model(batch) / accumulation_steps
    loss.backward()
    
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

---

### Fix 3: Enable Mixed Precision Training

Use 16-bit instead of 32-bit numbers:

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for batch in dataloader:
    with autocast():
        outputs = model(inputs)
        loss = criterion(outputs, labels)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

**Memory savings:** ~50% reduction!

---

### Fix 4: Clear CUDA Cache

```python
import torch
import gc

# After each epoch or when needed
torch.cuda.empty_cache()
gc.collect()
```

---

### Fix 5: Use a Smaller Model

```python
# Instead of large model
# model = BertForSequenceClassification.from_pretrained('bert-large-uncased')

# Use smaller variant
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
# or
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')
```

**Model size comparison:**
- BERT Large: 340M parameters (~1.3GB VRAM just for weights)
- BERT Base: 110M parameters (~440MB VRAM)
- DistilBERT: 66M parameters (~264MB VRAM)

---

### Fix 6: Reduce Sequence Length

```python
# Before
max_length = 512

# After
max_length = 256  # or 128
```

**Why it works:** Attention mechanisms scale quadratically with sequence length!

---

### Fix 7: Use CPU (Last Resort)

If you have no GPU or it's too small:

```python
# Force CPU usage
device = torch.device('cpu')
model.to(device)
```

**Trade-off:** Much slower but avoids OOM errors entirely.

---

## Google Colab Specific Solutions

### Solution 1: Check Your GPU

```python
# In Colab, go to Runtime → Change runtime type
# Select GPU (free tier gives Tesla T4 with 16GB VRAM)

# Verify GPU is connected
!nvidia-smi
```

### Solution 2: Free Up Memory

```python
# Delete variables you don't need
del large_variable
del model
torch.cuda.empty_cache()
```

### Solution 3: Restart Runtime

Sometimes the simplest fix:
- Go to **Runtime → Restart runtime**
- Re-run your notebook from the beginning

---

## Prevention Tips

### Tip 1: Monitor GPU Usage

```python
# Check memory usage
print(f"Allocated: {torch.cuda.memory_allocated(0)/1024**2:.2f} MB")
print(f"Cached: {torch.cuda.memory_reserved(0)/1024**2:.2f} MB")
```

### Tip 2: Start Small

Always test with tiny data first:

```python
# Test with 2 samples before full dataset
test_dataloader = DataLoader(dataset[:2], batch_size=1)
# Run one iteration to check for OOM
```

### Tip 3: Use `gradient_checkpointing`

For very large models:

```python
from transformers import AutoModel

model = AutoModel.from_pretrained('bert-base-uncased')
model.gradient_checkpointing_enable()  # Trade compute for memory
```

---

## Hardware Reality Check

| GPU | VRAM | Can Train | Cost |
|-----|------|-----------|------|
| **Colab Free (T4)** | 16GB | Small-medium models | $0 |
| **Colab Pro (V100)** | 16GB | Medium models | $10/mo |
| **RTX 3060** | 12GB | Medium models | $300 |
| **RTX 3090/4090** | 24GB | Large models | $1500-2000 |
| **A100 (Cloud)** | 40-80GB | Very large models | $3-5/hr |

---

## When Nothing Works

If you've tried everything and still get OOM:

1. **Use a cloud service:**
   - [Google Colab Pro](https://colab.research.google.com/) - Better GPUs
   - [Kaggle Notebooks](https://kaggle.com/code) - Free P100 GPUs
   - [Paperspace Gradient](https://paperspace.com/gradient) - Affordable cloud GPUs

2. **Use pre-trained models:**
   - Don't train from scratch!
   - Fine-tune existing models (uses less memory)

3. **Optimize your code:**
   - Profile memory usage
   - Remove unnecessary operations
   - Use efficient data loaders

---

## Example: Complete OOM-Free Training Setup

```python
import torch
from transformers import AutoModel, AutoTokenizer
from torch.utils.data import DataLoader

# Configuration for low-memory training
config = {
    'model_name': 'distilbert-base-uncased',  # Smaller model
    'batch_size': 8,                          # Small batch
    'max_length': 128,                        # Short sequences
    'gradient_accumulation_steps': 4,         # Effective batch = 32
    'use_amp': True,                          # Mixed precision
}

# Load model
model = AutoModel.from_pretrained(config['model_name'])
model.gradient_checkpointing_enable()

# Move to GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Enable mixed precision
scaler = torch.cuda.amp.GradScaler()

# Training loop with gradient accumulation
for epoch in range(num_epochs):
    for i, batch in enumerate(dataloader):
        with torch.cuda.amp.autocast(enabled=config['use_amp']):
            outputs = model(**batch)
            loss = outputs.loss / config['gradient_accumulation_steps']
        
        scaler.scale(loss).backward()
        
        if (i + 1) % config['gradient_accumulation_steps'] == 0:
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad()
    
    # Clear memory after each epoch
    torch.cuda.empty_cache()
```

---

## Related Errors

- [Torch_Not_Installed](./Torch_Not_Installed.md)
- [ImportError_Transformers](./ImportError_Transformers.md)

---

## Still Stuck?

1. Share your exact error message
2. Include your GPU model (`!nvidia-smi`)
3. Show your batch size and model choice
4. Post on Stack Overflow or Reddit r/MachineLearning

---

**Remember:** OOM errors are normal! Every AI developer deals with them daily. The key is knowing these tricks! 💪
