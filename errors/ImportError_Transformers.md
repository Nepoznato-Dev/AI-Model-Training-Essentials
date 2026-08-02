# ImportError: No module named 'transformers' 🔧

**Error Message:**
```
ModuleNotFoundError: No module named 'transformers'
```

or

```
ImportError: cannot import name 'xxx' from 'transformers'
```

---

## What This Means

Python can't find the `transformers` library (by Hugging Face). Either it's not installed, or there's a version conflict.

---

## Quick Fixes (Try in Order)

### Fix 1: Install Transformers ⭐

```bash
# Basic installation
pip install transformers

# With PyTorch
pip install transformers[torch]

# With TensorFlow
pip install transformers[tf]

# With JAX/Flax
pip install transformers[flax]
```

---

### Fix 2: Verify Installation

```bash
# Check if installed
pip show transformers

# Check version
python -c "import transformers; print(transformers.__version__)"
```

Expected output:
```
Name: transformers
Version: 4.x.x
Summary: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX
```

---

### Fix 3: Use Correct Python Environment

You might have installed it in a different Python environment!

```bash
# Check which Python you're using
which python      # Mac/Linux
where python      # Windows

# Check pip location
which pip
pip --version

# Make sure they match!
# If not, use:
python -m pip install transformers
```

---

### Fix 4: Upgrade Transformers

Old versions might be incompatible:

```bash
# Upgrade to latest
pip install --upgrade transformers

# Or install specific version
pip install transformers==4.35.0
```

---

### Fix 5: Reinstall Completely

Sometimes a clean install fixes issues:

```bash
# Uninstall
pip uninstall transformers

# Clear cache
pip cache purge

# Reinstall
pip install transformers
```

---

### Fix 6: Check for Conflicts

Some packages conflict with transformers:

```bash
# Problematic combinations:
# - old versions of torch + new transformers
# - tensorflow and pytorch in same env (sometimes)

# Solution: Create fresh virtual environment
python -m venv ai_env
source ai_env/bin/activate  # Windows: ai_env\Scripts\activate
pip install transformers torch
```

---

## Virtual Environment Setup (Recommended)

Always use virtual environments to avoid conflicts!

### Setup Steps:

```bash
# 1. Create virtual environment
python -m venv ai_env

# 2. Activate it
# Mac/Linux:
source ai_env/bin/activate

# Windows:
ai_env\Scripts\activate

# 3. Install dependencies
pip install transformers torch numpy pandas

# 4. Verify
python -c "import transformers; print('Success!')"

# 5. When done, deactivate
deactivate
```

---

## Google Colab Specific

### Colab Already Has Transformers!

```python
# In Colab, transformers is pre-installed
import transformers
print(transformers.__version__)

# If you need a newer version:
!pip install --upgrade transformers
```

### Complete Colab Setup:

```python
# Cell 1: Install/upgrade (if needed)
!pip install --quiet --upgrade transformers torch

# Cell 2: Import and verify
from transformers import AutoModel, AutoTokenizer
print("✓ Transformers ready!")

# Cell 3: Your code
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
```

---

## Common Import Errors & Fixes

### Error 1: "cannot import name 'xxx' from 'transformers'"

**Cause:** Using outdated tutorial with new library, or vice versa

**Fix:** Check version compatibility:

```python
import transformers
print(transformers.__version__)

# Then check documentation for your version
# https://github.com/huggingface/transformers/releases
```

Example fix:
```python
# Old code (v3.x):
from transformers import TFAutoModel

# New code (v4.x):
from transformers import TFAutoModel  # Still works
# OR use updated API
from transformers import AutoModel
```

---

### Error 2: "No module named 'transformers.models.xxx'"

**Cause:** Corrupted installation or incomplete download

**Fix:**
```bash
# Reinstall
pip uninstall transformers
pip install --no-cache-dir transformers
```

---

### Error 3: Works in terminal but not in Jupyter/IDE

**Cause:** Different Python interpreters

**Fix for Jupyter:**
```python
# In a notebook cell:
import sys
!{sys.executable} -m pip install transformers
```

**Fix for VS Code:**
1. Open Command Palette (`Ctrl+Shift+P`)
2. Select "Python: Select Interpreter"
3. Choose the one where transformers is installed

---

## Verify Everything Works

Run this test script:

```python
# test_transformers.py
try:
    from transformers import AutoTokenizer, AutoModel
    import torch
    
    print(f"✓ Transformers version: {transformers.__version__}")
    print(f"✓ PyTorch version: {torch.__version__}")
    
    # Test loading a model
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    model = AutoModel.from_pretrained('bert-base-uncased')
    
    print("✓ Model loaded successfully!")
    
    # Test inference
    inputs = tokenizer("Hello, world!", return_tensors="pt")
    outputs = model(**inputs)
    
    print("✓ Inference successful!")
    print("🎉 Everything works!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    raise
```

Run it:
```bash
python test_transformers.py
```

---

## Dependencies Checklist

Make sure these are also installed:

```bash
# Required
pip install torch numpy

# Recommended
pip install pandas matplotlib scikit-learn

# For NLP tasks
pip install sentencepiece protobuf

# For downloading models
pip install huggingface_hub
```

Or install all at once:
```bash
pip install transformers[torch,sentencepiece]
```

---

## Version Compatibility Matrix

| Transformers | PyTorch | Python | Status |
|--------------|---------|--------|--------|
| 4.35.x | 2.0+ | 3.8+ | ✅ Latest |
| 4.30.x | 1.13+ | 3.8+ | ✅ Stable |
| 4.25.x | 1.12+ | 3.7+ | ⚠️ Older |
| < 4.0 | Any | Any | ❌ Deprecated |

Check your versions:
```python
import transformers, torch, sys
print(f"Transformers: {transformers.__version__}")
print(f"PyTorch: {torch.__version__}")
print(f"Python: {sys.version}")
```

---

## Still Not Working?

### Debug Checklist:

- [ ] Is Python installed correctly?
- [ ] Are you in the right virtual environment?
- [ ] Did installation complete without errors?
- [ ] Is your internet working? (downloads models)
- [ ] Do you have enough disk space? (~1GB for transformers + models)

### Get Help:

1. **Check logs:**
   ```bash
   pip install transformers -vvv  # Verbose output
   ```

2. **Search GitHub Issues:**
   - https://github.com/huggingface/transformers/issues

3. **Ask on Stack Overflow:**
   - Tag: `[huggingface-transformers]`

4. **Hugging Face Forums:**
   - https://discuss.huggingface.co/

---

## Related Errors

- [Torch_Not_Installed](./Torch_Not_Installed.md)
- [CUDA_OOM](./CUDA_OOM.md)

---

## Prevention Tips

1. **Always use virtual environments**
2. **Pin versions in requirements.txt:**
   ```
   transformers==4.35.0
   torch==2.0.0
   ```

3. **Test imports immediately after install**
4. **Keep a working environment backup**

---

**Remember:** Package management issues are normal! Even experienced developers deal with this weekly. 💪
