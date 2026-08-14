# ImportError: Cannot Import Transformers

## 🔴 Error Message

```
ImportError: cannot import name 'transformers' from 'transformers'
```

Or variations:
```
ModuleNotFoundError: No module named 'transformers'
```

```
ImportError: cannot import name 'AutoModel' from 'transformers'
```

---

## 🎯 What This Means

Python can't find or properly load the Hugging Face `transformers` library. This is usually due to:
- The package isn't installed
- It's installed in a different Python environment
- There's a naming conflict
- The installation is corrupted

---

## ✅ Solutions (Try in Order)

### Solution 1: Verify Installation

**Check if transformers is installed:**
```bash
pip show transformers
```

**Expected output:**
```
Name: transformers
Version: 4.x.x
Summary: State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX
Location: /path/to/python/site-packages
```

**If you get "WARNING: Package(s) not found":**
Install it:
```bash
pip install transformers
```

---

### Solution 2: Check Your Import Statement

**❌ Wrong:**
```python
import Transformers  # Capital T - wrong!
from Transformer import AutoModel  # Singular - wrong!
import transformer  # Missing 's' - wrong!
```

**✅ Correct:**
```python
from transformers import AutoModel, AutoTokenizer
import transformers
print(transformers.__version__)
```

**Note:** The package name is all lowercase: `transformers`

---

### Solution 3: Activate Virtual Environment

**Problem:** You installed transformers in a virtual environment but aren't using it.

**Check which Python you're using:**
```bash
# In terminal
which python      # Linux/Mac
where python      # Windows

# In Python
import sys
print(sys.executable)
print(sys.path)
```

**If using virtual environment (venv/conda):**

**For venv:**
```bash
# Activate before running your script
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Then run your code
python your_script.py
```

**For conda:**
```bash
conda activate your_env_name
python your_script.py
```

**For Jupyter Notebook:**
Make sure the kernel matches your environment:
```python
import sys
print(sys.executable)
# Should point to your venv/conda Python, not system Python
```

To install a kernel for your venv:
```bash
# With venv activated
pip install ipykernel
python -m ipykernel install --user --name=myenv
```

Then in Jupyter: **Kernel → Change kernel → myenv**

---

### Solution 4: Fix Naming Conflicts

**Problem:** You have a file named `transformers.py` in your project folder.

**Check for conflicts:**
```bash
ls -la | grep transformers
```

**If you see `transformers.py` or `transformers.pyc`:**
```bash
# Rename your file!
mv transformers.py my_transformers_code.py
rm transformers.pyc
rm -rf __pycache__
```

**Why?** Python imports your local file instead of the actual library.

---

### Solution 5: Reinstall Transformers

**Sometimes installations get corrupted.**

**Complete reinstall:**
```bash
# Uninstall
pip uninstall transformers -y

# Clear cache
pip cache purge

# Reinstall with latest version
pip install --upgrade transformers

# Or install specific stable version
pip install transformers==4.36.0
```

**With dependencies:**
```bash
pip install transformers[torch]  # For PyTorch
pip install transformers[tf]     # For TensorFlow
```

---

### Solution 6: Check Python Version

**Transformers requires Python 3.8+:**

```bash
python --version
```

**If you have Python 3.7 or older:**

**Option A: Upgrade Python**
- Download from [python.org](https://www.python.org/downloads/)
- Or use conda: `conda create -n ai_env python=3.10`

**Option B: Install older transformers version**
```bash
pip install transformers==4.22.0  # Last version supporting Python 3.7
```

---

### Solution 7: Fix Permissions (Linux/Mac)

**If you get permission errors:**

```bash
# Don't use sudo pip! Create virtual environment instead
python -m venv venv
source venv/bin/activate
pip install transformers
```

**Or use user install:**
```bash
pip install --user transformers
```

---

## 🔍 Complete Working Example

Create a test file to verify everything works:

```python
# test_transformers.py
from transformers import AutoModel, AutoTokenizer

print("✅ Import successful!")

# Load a small model
model_name = "distilbert-base-uncased"
print(f"Loading {model_name}...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

print("✅ Model loaded successfully!")
print(f"Transformers version: {transformers.__version__}")
```

**Run it:**
```bash
python test_transformers.py
```

**Expected output:**
```
✅ Import successful!
Loading distilbert-base-uncased...
✅ Model loaded successfully!
Transformers version: 4.36.0
```

---

## 💻 Environment-Specific Solutions

### Google Colab

```python
# Usually pre-installed, but to be sure:
!pip install transformers

# Restart runtime after installation:
# Runtime → Restart runtime
```

### Jupyter Notebook

```python
# Install in the notebook cell
!pip install transformers

# Then restart kernel:
# Kernel → Restart
```

### Conda Environment

```bash
# Create fresh environment
conda create -n ai_env python=3.10
conda activate ai_env

# Install transformers
pip install transformers

# Or use conda (may be older version)
conda install -c huggingface transformers
```

### Docker

```dockerfile
FROM python:3.10-slim

RUN pip install transformers torch

WORKDIR /app
COPY . .
```

---

## 📊 Version Compatibility Matrix

| transformers | PyTorch | Python | Status |
|-------------|---------|--------|--------|
| 4.36.x      | 1.13+   | 3.8+   | ✅ Stable |
| 4.35.x      | 1.13+   | 3.8+   | ✅ Stable |
| 4.30.x      | 1.12+   | 3.8+   | ✅ Good |
| 4.22.x      | 1.10+   | 3.7+   | ⚠️ Old |
| < 4.0       | 1.6+    | 3.6+   | ❌ Deprecated |

**Check your versions:**
```bash
python --version
pip show transformers
pip show torch
```

---

## 🆘 Still Not Working? Debug Checklist

```python
# Run this diagnostic script
import sys
import subprocess

print("=== System Info ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current directory: {sys.path[0]}")

print("\n=== Installed Packages ===")
try:
    import transformers
    print(f"✅ transformers version: {transformers.__version__}")
except ImportError as e:
    print(f"❌ transformers import failed: {e}")

try:
    import torch
    print(f"✅ torch version: {torch.__version__}")
except ImportError as e:
    print(f"❌ torch import failed: {e}")

print("\n=== Pip List (transformers related) ===")
result = subprocess.run([sys.executable, "-m", "pip", "list"], 
                       capture_output=True, text=True)
for line in result.stdout.split('\n'):
    if 'transform' in line.lower():
        print(line)
```

---

## 📚 Related Errors

- [Torch_Not_Installed.md](Torch_Not_Installed.md) - PyTorch not found
- PIP_Install_Fails - Can't install packages
- HF_Connection_Error - Can't download models
- Virtual_Environment_Not_Active - Wrong Python environment
- See the [Common Errors index](README.md) for the full troubleshooting catalogue

---

## 🎓 Key Takeaway

Most import errors are caused by:

1. ✅ **Wrong import syntax** - Use lowercase `from transformers import ...`
2. ✅ **Package not installed** - Run `pip install transformers`
3. ✅ **Wrong environment** - Activate your venv/conda environment
4. ✅ **Naming conflict** - Don't name your files `transformers.py`

Always verify with the test script above! 🧪
