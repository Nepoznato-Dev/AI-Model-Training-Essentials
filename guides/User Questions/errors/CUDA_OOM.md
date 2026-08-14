# CUDA Out of Memory (OOM) Error

## 🔴 Error Message

```
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate X.XX GiB 
(GPU 0 of Y, Z.ZZ GiB total). GPU has been allocated W.WW GiB and has V.VV GiB free.
```

Or simpler:
```
RuntimeError: CUDA out of memory
```

---

## 🎯 What This Means

Your GPU doesn't have enough memory to:
- Load the model you're trying to use
- Process the batch size you specified
- Store intermediate calculations during training/inference

**This is the #1 error beginners face with deep learning!**

---

## ✅ Solutions (Try in Order)

### Solution 1: Reduce Batch Size (Most Common Fix)

**Why:** Smaller batches = less memory needed

**How:**
```python
# Before (too large)
batch_size = 64

# After (try these progressively smaller)
batch_size = 32
batch_size = 16
batch_size = 8
batch_size = 4  # Last resort
```

**In your training loop:**
```python
# Find this line in your code
train_dataloader = DataLoader(dataset, batch_size=64, ...)

# Change it to:
train_dataloader = DataLoader(dataset, batch_size=8, ...)
```

**Trade-off:** Training will take longer, but it will work!

---

### Solution 2: Use Gradient Accumulation

**Why:** Simulate large batch sizes with small memory footprint

**How:**
```python
# Instead of one large batch
batch_size = 64

# Use small batch + accumulation
batch_size = 8
accumulate_steps = 8  # 8 * 8 = 64 effective batch size

# In training loop:
for i, batch in enumerate(dataloader):
    outputs = model(batch)
    loss = criterion(outputs, labels)
    loss = loss / accumulate_steps  # Normalize loss
    loss.backward()
    
    if (i + 1) % accumulate_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

---

### Solution 3: Clear GPU Cache

**Why:** PyTorch doesn't always release memory immediately

**How:**
```python
import torch
import gc

# Add these before loading your model
torch.cuda.empty_cache()
gc.collect()

# Also add between epochs
for epoch in range(num_epochs):
    # training code...
    
    # At end of epoch
    torch.cuda.empty_cache()
```

---

### Solution 4: Use Mixed Precision Training

**Why:** 16-bit floats use half the memory of 32-bit

**How (PyTorch):**
```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for batch in dataloader:
    optimizer.zero_grad()
    
    with autocast():  # Enable mixed precision
        outputs = model(batch)
        loss = criterion(outputs, labels)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

**How (Transformers library):**
```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    fp16=True,  # Enable mixed precision
    per_device_train_batch_size=8,
)
```

---

### Solution 5: Use a Smaller Model

**Why:** Large models need lots of memory

**How:**
```python
# Instead of this (large)
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained("bert-large-uncased")

# Try this (smaller)
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Or even smaller
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")
```

**Model size comparison:**
- BERT Large: ~340M parameters (~1.3 GB)
- BERT Base: ~110M parameters (~440 MB)
- DistilBERT: ~66M parameters (~260 MB)
- TinyBERT: ~14M parameters (~60 MB)

---

### Solution 6: Move to CPU (Last Resort)

**Why:** CPU has access to system RAM (usually 16-64 GB vs GPU's 4-16 GB)

**How:**
```python
# Force CPU usage
import torch
device = torch.device("cpu")

model = model.to(device)
# All tensors also need to be on CPU
inputs = inputs.to(device)
```

**Trade-off:** Much slower, but works for debugging and small experiments.

---

### Solution 7: Use Google Colab Free Tier

**Why:** Free access to better GPUs than you might have locally

**How:**
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Upload your notebook or create new one
3. Go to **Runtime → Change runtime type**
4. Select **GPU** (Tesla T4, usually 16GB)
5. Run your code!

**Pro tip:** Colab Pro ($10/month) gives you access to V100/A100 GPUs with more memory.

---

## 📊 Quick Reference: Batch Size Guidelines

| GPU Memory | Max Batch Size (BERT Base) | Recommended Starting Point |
|------------|---------------------------|---------------------------|
| 4 GB       | 4-8                       | 4                         |
| 8 GB       | 16-32                     | 16                        |
| 12 GB      | 32-64                     | 32                        |
| 16 GB      | 64-128                    | 64                        |
| 24 GB      | 128-256                   | 128                       |

*Note: These are approximate. Actual values depend on sequence length and model.*

---

## 🔍 Debugging: Check Your GPU Memory

**Before running your code:**
```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
    print(f"Total memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    print(f"Allocated: {torch.cuda.memory_allocated(0) / 1e9:.2f} GB")
    print(f"Cached: {torch.cuda.memory_reserved(0) / 1e9:.2f} GB")
```

**Monitor during training:**
```python
# Add to your training loop
for epoch in range(num_epochs):
    # training...
    
    print(f"Epoch {epoch} - Memory allocated: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
```

---

## 💡 Prevention Tips

1. **Start small:** Begin with tiny batch sizes and increase gradually
2. **Profile first:** Run one batch and check memory before full training
3. **Use gradient checkpointing:** For very large models
   ```python
   model.gradient_checkpointing_enable()
   ```
4. **Limit sequence length:** Shorter texts = less memory
   ```python
   max_length = 128  # Instead of 512
   ```
5. **Freeze layers:** Don't train all layers at once
   ```python
   for param in model.base_model.parameters():
       param.requires_grad = False
   ```

---

## 🆘 Still Not Working?

Try this nuclear option - minimal memory setup:

```python
import torch
from transformers import AutoModel, AutoTokenizer

# Clear everything
torch.cuda.empty_cache()

# Use smallest settings
model_name = "distilbert-base-uncased"
max_length = 64
batch_size = 2

# Load model
model = AutoModel.from_pretrained(model_name)
model.to("cuda" if torch.cuda.is_available() else "cpu")

# Tokenize with short sequences
tokenizer = AutoTokenizer.from_pretrained(model_name)
inputs = tokenizer("Short text here", max_length=max_length, truncation=True, return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}

# Run inference
with torch.no_grad():
    outputs = model(**inputs)
```

---

## 📚 Related Errors

- Device_Cuda_Not_Available - GPU not detected at all
- Slow_Training - Training works but takes forever
- Gradient_Explosion - NaN losses during training
- See the [Common Errors index](README.md) for the full troubleshooting catalogue

---

## 🎓 Key Takeaway

**CUDA OOM errors are normal!** Even experienced developers face them daily. The solution is almost always:

1. ✅ Reduce batch size
2. ✅ Use mixed precision
3. ✅ Use a smaller model
4. ✅ Use Colab or cloud GPU

Don't get discouraged—this is just part of working with deep learning! 💪
