# ModuleNotFoundError: No module named 'torch'

## 🔴 Error Message

```
ModuleNotFoundError: No module named 'torch'
```

Or:
```
ImportError: No module named torch
```

---

## 🎯 What This Means

PyTorch (the `torch` library) is not installed in your current Python environment. PyTorch is essential for deep learning and required by most AI tutorials.

---

## ✅ Solutions (Try in Order)

### Solution 1: Install PyTorch (Basic)

**Quick install:**
```bash
pip install torch
```

**For CPU-only (smaller, faster to install):**
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**Verify installation:**
```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
```

---

### Solution 2: Use the Official Installer Command

PyTorch has different versions for different systems. Get the right one:

1. Go to [pytorch.org/get-started](https://pytorch.org/get-started/locally/)
2. Select your configuration:
   - **PyTorch Build:** Stable
   - **Your OS:** Windows/Linux/macOS
   - **Package:** pip
   - **Language:** Python
   - **Compute Platform:** CUDA (if you have NVIDIA GPU) or CPU

3. Copy and run the generated command

**Example for Windows with CUDA 11.8:**
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**Example for macOS (CPU only):**
```bash
pip3 install torch torchvision torchaudio
```

---

### Solution 3: Check Your Python Environment

**Problem:** You installed torch in one environment but are running code in another.

**Diagnose:**
```bash
# In terminal
which python        # Linux/Mac
where python        # Windows

# In Python
import sys
print(sys.executable)
```

**Fix for virtual environments:**

```bash
# Activate your environment FIRST
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Then install
pip install torch

# Verify
python -c "import torch; print(torch.__version__)"
```

**Fix for conda:**
```bash
conda activate your_env
conda install pytorch torchvision torchaudio -c pytorch
```

**Fix for Jupyter:**
```python
# In a notebook cell
!pip install torch

# Then restart kernel: Kernel → Restart
```

---

### Solution 4: Upgrade pip First

**Old pip versions can't find recent PyTorch releases:**

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Then install torch
pip install torch
```

---

### Solution 5: Check System Compatibility

**PyTorch requires:**
- Python 3.8 or newer
- 64-bit system
- For GPU: NVIDIA card with CUDA support

**Check your setup:**
```bash
python --version           # Should be 3.8+
python -c "import struct; print(struct.calcsize('P') * 8)"  # Should be 64
```

**If Python is too old:**
```bash
# Create new conda environment with modern Python
conda create -n ai_env python=3.10
conda activate ai_env
pip install torch
```

---

### Solution 6: Fix Installation Issues

**If standard install fails:**

**Clear pip cache:**
```bash
pip cache purge
pip install --no-cache-dir torch
```

**Use specific version:**
```bash
pip install torch==2.1.0
```

**Add verbose output to see what's wrong:**
```bash
pip install torch -vvv
```

---

## 💻 Platform-Specific Instructions

### Windows

**With CUDA (NVIDIA GPU):**
```powershell
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**CPU only:**
```powershell
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

**Common Windows issues:**

1. **Visual C++ Redistributable needed:**
   Download from: [Microsoft VC++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

2. **Long path issues:**
   Enable long paths in Windows:
   ```powershell
   # Run as Administrator
   New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
   -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
   ```

### macOS

**Intel Mac:**
```bash
pip3 install torch torchvision torchaudio
```

**Apple Silicon (M1/M2/M3):**
```bash
# PyTorch now has native M1/M2 support
pip3 install torch torchvision torchaudio
```

**Verify MPS (Metal Performance Shaders) on M1/M2:**
```python
import torch
print(f"MPS available: {torch.backends.mps.is_available()}")
```

### Linux

**With pip:**
```bash
pip3 install torch torchvision torchaudio
```

**With CUDA:**
```bash
# First check your CUDA version
nvcc --version

# Then install matching PyTorch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**With conda (recommended on Linux):**
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

---

## 🔍 Verification Script

Create this file to test your installation:

```python
# test_torch.py
import torch

print("=" * 50)
print("PyTorch Installation Test")
print("=" * 50)

print(f"\n✅ PyTorch version: {torch.__version__}")
print(f"✅ CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"✅ GPU name: {torch.cuda.get_device_name(0)}")
    print(f"✅ CUDA version: {torch.version.cuda}")
    
    # Test GPU computation
    x = torch.rand(5, 3).cuda()
    y = torch.rand(5, 3).cuda()
    z = x + y
    print(f"✅ GPU computation works! Result shape: {z.shape}")
else:
    print("⚠️ Running on CPU (GPU not detected or not available)")

# Test basic operations
a = torch.randn(3, 3)
b = torch.randn(3, 3)
c = torch.matmul(a, b)
print(f"✅ Matrix multiplication works! Result shape: {c.shape}")

print("\n✅ All tests passed!")
```

**Run it:**
```bash
python test_torch.py
```

**Expected output (with GPU):**
```
==================================================
PyTorch Installation Test
==================================================

✅ PyTorch version: 2.1.0+cu118
✅ CUDA available: True
✅ GPU name: NVIDIA GeForce RTX 3060
✅ CUDA version: 11.8
✅ GPU computation works! Result shape: torch.Size([5, 3])
✅ Matrix multiplication works! Result shape: torch.Size([3, 3])

✅ All tests passed!
```

---

## 📊 Quick Reference: Which Version to Install?

| Your Setup | Install Command |
|------------|----------------|
| **Beginner, no GPU** | `pip install torch --index-url https://download.pytorch.org/whl/cpu` |
| **Windows + NVIDIA GPU** | `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` |
| **macOS (any)** | `pip3 install torch torchvision torchaudio` |
| **Linux + NVIDIA GPU** | `pip3 install torch torchvision torchaudio` |
| **Using Conda** | `conda install pytorch torchvision torchaudio -c pytorch` |
| **Google Colab** | Pre-installed! Just `import torch` |

---

## 🆘 Still Not Working?

### Check pip list
```bash
pip list | grep torch
```

Should show something like:
```
torch                    2.1.0
torchaudio               2.1.0
torchvision              0.16.0
```

### Try uninstalling completely and reinstalling
```bash
pip uninstall torch torchvision torchaudio -y
pip cache purge
pip install torch torchvision torchaudio
```

### Check for conflicting packages
```bash
pip list | grep -i pytorch
```

If you see `pytorch` (different from `torch`), remove it:
```bash
pip uninstall pytorch -y
```

---

## 📚 Related Errors

- [ImportError_Transformers.md](ImportError_Transformers.md) - Can't import transformers
- Device_Cuda_Not_Available - GPU not detected
- PIP_Install_Fails - pip installation errors
- Virtual_Environment_Not_Active - Wrong Python environment
- See the [Common Errors index](README.md) for the full troubleshooting catalogue

---

## 🎓 Key Takeaway

To fix `No module named 'torch'`:

1. ✅ **Install with the right command** for your system
2. ✅ **Activate your virtual environment** before installing
3. ✅ **Upgrade pip** if installation fails
4. ✅ **Verify** with the test script above

Most importantly: **Start with CPU version** if you're a beginner—it's easier and works great for learning! 🚀
