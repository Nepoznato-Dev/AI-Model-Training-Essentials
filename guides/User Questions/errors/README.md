# Common Errors Knowledge Base

Quick solutions to the most common errors you'll encounter when learning AI development.

## 🔍 How to Use This Guide

1. **Copy your error message** into a text editor
2. **Search for keywords** in this guide (Ctrl+F / Cmd+F)
3. **Follow the solution steps** exactly as written
4. **Still stuck?** Check the "Related Errors" section at the bottom of each entry

---

## 📦 Installation Errors

### [CUDA_Out_Of_Memory.md](errors/CUDA_OOM.md)
**Error:** `torch.cuda.OutOfMemoryError: CUDA out of memory`  
**When:** Training models or running inference on GPU

### [ImportError_Transformers.md](errors/ImportError_Transformers.md)
**Error:** `ImportError: cannot import name 'transformers'`  
**When:** Trying to import Hugging Face transformers

### [Torch_Not_Installed.md](errors/Torch_Not_Installed.md)
**Error:** `ModuleNotFoundError: No module named 'torch'`  
**When:** Running any PyTorch code

### [PIP_Install_Fails.md](errors/PIP_Install_Fails.md)
**Error:** `ERROR: Could not find a version that satisfies the requirement`  
**When:** Installing packages with pip

### [Python_Version_Mismatch.md](errors/Python_Version_Mismatch.md)
**Error:** `This version of X requires Python Y.Z or greater`  
**When:** Installing or running Python packages

---

## 🏗️ Runtime Errors

### [Shape_Mismatch_Error.md](errors/Shape_Mismatch_Error.md)
**Error:** `RuntimeError: size mismatch` or `ValueError: shapes not aligned`  
**When:** Matrix operations, model forward pass

### [Device_Cuda_Not_Available.md](errors/Device_Cuda_Not_Available.md)
**Error:** `Torch not compiled with CUDA enabled` or `Found no NVIDIA driver`  
**When:** Trying to use GPU acceleration

### [DataLoader_Worker_Error.md](errors/DataLoader_Worker_Error.md)
**Error:** `RuntimeError: DataLoader worker (pid(s) XXXXX) exited unexpectedly`  
**When:** Loading data during training

### [Gradient_Explosion.md](errors/Gradient_Explosion.md)
**Error:** `RuntimeError: NaN detected in loss` or gradients become `inf`  
**When:** Training deep neural networks

---

## 📁 File & Data Errors

### [File_Not_Found_Error.md](errors/File_Not_Found_Error.md)
**Error:** `FileNotFoundError: [Errno 2] No such file or directory`  
**When:** Loading datasets, models, or configuration files

### [JSON_Decode_Error.md](errors/JSON_Decode_Error.md)
**Error:** `json.decoder.JSONDecodeError: Expecting value`  
**When:** Loading JSON configuration or data files

### [Encoding_Error.md](errors/Encoding_Error.md)
**Error:** `UnicodeDecodeError: 'utf-8' codec can't decode byte`  
**When:** Reading text files or datasets

---

## 🤗 Hugging Face Specific

### [HF_Connection_Error.md](errors/HF_Connection_Error.md)
**Error:** `ConnectionError: Couldn't reach hub.huggingface.co`  
**When:** Downloading models from Hugging Face Hub

### [HF_Cache_Corrupted.md](errors/HF_Cache_Corrupted.md)
**Error:** `OSError: Unable to load weights from pytorch checkpoint`  
**When:** Loading cached Hugging Face models

### [Tokenizer_Error.md](errors/Tokenizer_Error.md)
**Error:** `TypeError: Argument 'input_ids' has incorrect type`  
**When:** Tokenizing text for transformers

---

## 💻 System & Environment

### [Virtual_Environment_Not_Active.md](errors/Virtual_Environment_Not_Active.md)
**Error:** Packages installed but still getting `ModuleNotFoundError`  
**When:** Running Python scripts

### [Path_Too_Long_Windows.md](errors/Path_Too_Long_Windows.md)
**Error:** `OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect`  
**When:** Working with deeply nested directories on Windows

### [Permission_Denied.md](errors/Permission_Denied.md)
**Error:** `PermissionError: [Errno 13] Permission denied`  
**When:** Writing files or installing packages

---

## 🧠 Model Training Errors

### [Loss_Is_NaN.md](errors/Loss_Is_NaN.md)
**Error:** Loss becomes `nan` during training  
**When:** Training neural networks

### [Overfitting_Early.md](errors/Overfitting_Early.md)
**Error:** Training accuracy high, validation accuracy low  
**When:** Model memorizes training data

### [Slow_Training.md](errors/Slow_Training.md)
**Error:** Training is taking hours/days instead of minutes  
**When:** Model training performance

---

## 📝 How to Report an Error

If you encounter an error not listed here:

1. **Copy the full error message** (not just the last line!)
2. **Note what you were doing** when it occurred
3. **Include your environment:**
   ```bash
   python --version
   pip list | grep torch
   pip list | grep transformers
   ```
4. **Check existing issues** in the repository
5. **Create a new issue** with all the information above

---

## 🎯 Quick Troubleshooting Checklist

Before diving deep, try these universal fixes:

- [ ] **Restart your Python kernel** (in Jupyter/Colab)
- [ ] **Clear cache:** `rm -rf ~/.cache/huggingface`
- [ ] **Update packages:** `pip install --upgrade package_name`
- [ ] **Check internet connection** (for downloading models)
- [ ] **Verify disk space:** `df -h` (Linux/Mac) or check Drive properties (Windows)
- [ ] **Try CPU instead of GPU** (add `.to('cpu')` to tensors)
- [ ] **Reduce batch size** (halve it and try again)
- [ ] **Reinstall problematic package:** `pip uninstall pkg && pip install pkg`

---

## 🆘 Getting Help

1. **Read the error carefully** - Python errors are usually descriptive
2. **Google the exact error message** (in quotes)
3. **Check Stack Overflow** for similar issues
4. **Look at the library's GitHub issues**
5. **Ask in community forums** (Reddit r/MachineLearning, Discord servers)

Remember: Every expert was once a beginner who learned to debug! 💪
