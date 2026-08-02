# Torch Not Installed / PyTorch Import Error 🔥

**Error Message:**
```
ModuleNotFoundError: No module named 'torch'
```

or

```
ImportError: No module named 'torch'
```

---

## What This Means

PyTorch (the most popular deep learning library) is not installed in your Python environment.

---

## Quick Fixes (Try in Order)

### Fix 1: Install PyTorch ⭐

**IMPORTANT:** Use the official installer for your system!

#### Option A: CPU Only (Smaller, works everywhere)
```bash
pip install torch torchvision torchaudio
```

#### Option B: With CUDA GPU Support (Faster, needs NVIDIA GPU)
```bash
# For CUDA 11.8 (most common)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1 (newer GPUs)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### Option C: Use the Official Installer
Visit [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) and select your configuration!

---

### Fix 2: Verify Installation

```bash
# Check if installed
python -c "import torch; print(f'PyTorch {torch.__version__} installed!')"

# Check CUDA availability
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

# If CUDA available, check GPU
python -c "import torch; print(f'GPU count: {torch.cuda.device_count()}'); print(f'GPU name: {torch.cuda.get_device_name(0)}')"
```

Expected output:
```
PyTorch 2.0.0+cu118 installed!
CUDA available: True
GPU count: 1
GPU name: Tesla T4
```

---

### Fix 3: Check Your Python Environment

You might have installed it in a different environment!

```bash
# Which Python are you using?
which python        # Mac/Linux
where python        # Windows

# Which pip?
which pip
pip --version

# They should match! If not:
python -m pip install torch
```

---

### Fix 4: Upgrade pip First

Old pip versions can't install new PyTorch:

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Then install torch
pip install torch
```

---

### Fix 5: Check System Requirements

#### Windows Users:
- Need Visual C++ Redistributable
- Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe

#### Mac Users:
- M1/M2 chips need special version:
```bash
pip install torch torchvision torchaudio
```
(Currently no CUDA support on Mac, but MPS acceleration available!)

#### Linux Users:
- May need to install system dependencies:
```bash
sudo apt-get update
sudo apt-get install libopenblas-base libomp-dev
```

---

## Virtual Environment Setup (Recommended)

Always use virtual environments!

```bash
# 1. Create environment
python -m venv ai_env

# 2. Activate
# Mac/Linux:
source ai_env/bin/activate

# Windows:
ai_env\Scripts\activate

# 3. Upgrade pip
pip install --upgrade pip

# 4. Install PyTorch
# CPU version:
pip install torch torchvision torchaudio

# OR GPU version (if you have NVIDIA GPU):
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 5. Test
python -c "import torch; print(torch.__version__)"
```

---

## Google Colab Specific

### Good News: PyTorch is Pre-installed!

```python
# Just import and use!
import torch
print(f"PyTorch {torch.__version__}")
print(f"CUDA {torch.version.cuda}")
```

### If You Need a Different Version:

```python
# Uninstall existing
!pip uninstall torch torchvision torchaudio -y

# Install specific version
!pip install torch==2.0.0 torchvision==0.15.0 --index-url https://download.pytorch.org/whl/cu118
```

### Enable GPU in Colab:
1. Go to **Runtime** → **Change runtime type**
2. Select **GPU** under Hardware accelerator
3. Click **Save**
4. Restart the runtime

---

## Common Errors & Fixes

### Error 1: "No module named 'torch'" after installation

**Cause:** Installed in wrong environment

**Fix:**
```bash
# Make sure you're using the right pip
python -m pip install torch
```

---

### Error 2: "DLL load failed" (Windows)

**Cause:** Missing Visual C++ redistributables

**Fix:**
1. Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Install and restart computer
3. Reinstall PyTorch

---

### Error 3: "CUDA not available" even after GPU install

**Cause:** Driver mismatch or no NVIDIA GPU

**Fix:**
```python
# Check if you have NVIDIA GPU
# Windows: Open Task Manager → Performance → GPU
# Mac/Linux: Run nvidia-smi in terminal

# If no NVIDIA GPU, use CPU version:
pip install torch torchvision torchaudio
```

**For Mac M1/M2:** Use MPS acceleration instead:
```python
import torch
device = torch.device("mps")  # Instead of "cuda"
```

---

### Error 4: Import works but "undefined symbol" error

**Cause:** Version conflict with numpy

**Fix:**
```bash
# Upgrade numpy
pip install --upgrade numpy

# Or install compatible version
pip install numpy==1.24.0
```

---

### Error 5: Works in terminal but not Jupyter

**Cause:** Jupyter using different Python kernel

**Fix for Jupyter:**
```python
# In notebook cell:
import sys
!{sys.executable} -m pip install torch
```

**Or install ipykernel:**
```bash
pip install ipykernel
python -m ipykernel install --user --name=ai_env
```

Then in Jupyter: Kernel → Change kernel → ai_env

---

## Verify Everything Works

Run this comprehensive test:

```python
# test_pytorch.py
import torch
import numpy as np

print("=" * 50)
print("PyTorch Installation Test")
print("=" * 50)

# Basic info
print(f"\n✓ PyTorch version: {torch.__version__}")
print(f"✓ CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"✓ CUDA version: {torch.version.cuda}")
    print(f"✓ GPU count: {torch.cuda.device_count()}")
    print(f"✓ GPU name: {torch.cuda.get_device_name(0)}")
    
    # Test GPU tensor
    gpu_tensor = torch.randn(3, 3).cuda()
    print(f"✓ GPU tensor created: {gpu_tensor.device}")
else:
    print("⚠ Using CPU only (that's okay for learning!)")

# Test basic operations
x = torch.rand(5, 3)
y = torch.rand(3, 5)
z = torch.matmul(x, y)
print(f"\n✓ Matrix multiplication works: {z.shape}")

# Test autograd (core feature)
a = torch.tensor([2.0], requires_grad=True)
b = a ** 2
b.backward()
print(f"✓ Autograd works: gradient = {a.grad}")

# Test neural network module
import torch.nn as nn
model = nn.Linear(10, 1)
output = model(torch.randn(1, 10))
print(f"✓ Neural network module works: output shape = {output.shape}")

print("\n🎉 All tests passed! PyTorch is ready!")
print("=" * 50)
```

Run it:
```bash
python test_pytorch.py
```

---

## Version Compatibility

| PyTorch | Python | CUDA | Status |
|---------|--------|------|--------|
| 2.0.x | 3.8-3.11 | 11.7/11.8 | ✅ Latest |
| 1.13.x | 3.7-3.10 | 11.6/11.7 | ✅ Stable |
| 1.12.x | 3.7-3.10 | 11.3/11.6 | ⚠️ Older |
| < 1.10 | Any | Any | ❌ Deprecated |

Check versions:
```python
import torch, sys
print(f"PyTorch: {torch.__version__}")
print(f"Python: {sys.version}")
print(f"CUDA: {torch.version.cuda if torch.cuda.is_available() else 'N/A'}")
```

---

## Hardware Reality Check

### Do You Need a GPU?

**For Learning:** NO! 
- CPU is fine for tutorials and small models
- Google Colab gives free GPU when needed

**For Serious Training:** YES
- GPU is 10-100x faster than CPU
- But start with free cloud GPUs first!

### GPU Options:

| Option | Cost | Speed | Best For |
|--------|------|-------|----------|
| **Colab Free** | $0 | Medium | Learning, small projects |
| **Colab Pro** | $10/mo | Fast | Regular usage |
| **Kaggle** | $0 | Fast | Occasional training |
| **RTX 3060** | $300 | Very Fast | Local development |
| **RTX 4090** | $1600 | Extreme | Production work |

---

## Still Not Working?

### Debug Checklist:

- [ ] Is Python installed? (`python --version`)
- [ ] Is pip working? (`pip --version`)
- [ ] Enough disk space? (~2GB for PyTorch + CUDA)
- [ ] Internet connection? (downloads packages)
- [ ] Antivirus blocking? (temporarily disable)

### Get Help:

1. **Check PyTorch forums:**
   - https://discuss.pytorch.org/

2. **GitHub Issues:**
   - https://github.com/pytorch/pytorch/issues

3. **Stack Overflow:**
   - Tag: `[pytorch]`

4. **PyTorch Discord:**
   - https://discord.gg/pytorch

---

## Related Errors

- [ImportError_Transformers](./ImportError_Transformers.md)
- [CUDA_OOM](./CUDA_OOM.md)

---

## Prevention Tips

1. **Use virtual environments** - Avoid system-wide conflicts
2. **Pin versions** - `requirements.txt` with exact versions
3. **Test immediately** - Run verification after install
4. **Document your setup** - Note what worked for future reference

Example `requirements.txt`:
```
torch==2.0.0
torchvision==0.15.0
torchaudio==2.0.0
numpy==1.24.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

**Remember:** Installation issues are the most common problem in ML! Don't get discouraged—everyone deals with this! 💪
