# Common Errors Knowledge Base

Quick solutions to the most common errors you'll encounter when learning AI development.

## 🔍 How to Use This Guide

1. **Copy your error message** into a text editor
2. **Search for keywords** in this guide (Ctrl+F / Cmd+F)
3. **Follow the solution steps** exactly as written
4. **Still stuck?** Check the "Related Errors" section at the bottom of each entry

---

## 📦 Installation Errors

### [CUDA_OOM.md](CUDA_OOM.md)
**Error:** `torch.cuda.OutOfMemoryError: CUDA out of memory`  
**When:** Training models or running inference on GPU

### [ImportError_Transformers.md](ImportError_Transformers.md)
**Error:** `ImportError: cannot import name 'transformers'`  
**When:** Trying to import Hugging Face transformers

### [Torch_Not_Installed.md](Torch_Not_Installed.md)
**Error:** `ModuleNotFoundError: No module named 'torch'`  
**When:** Running any PyTorch code

---

## 🏗️ Runtime Errors

*Additional runtime error guides are available in the [main errors directory](../../errors/README.md).*

---

## 📁 File & Data Errors

*File and data error guides are available in the [main errors directory](../../errors/README.md).*

---

## 🤗 Hugging Face Specific

*Hugging Face-specific error guides are available in the [main errors directory](../../errors/README.md).*

---

## 💻 System & Environment

*System and environment error guides are available in the [main errors directory](../../errors/README.md).*

---

## 🧠 Model Training Errors

*Model training error guides are available in the [main errors directory](../../errors/README.md).*

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
- [ ] **Reinstall problematic package:** `pip uninstall pkg; pip install pkg`

---

## 🆘 Getting Help

1. **Read the error carefully** - Python errors are usually descriptive
2. **Google the exact error message** (in quotes)
3. **Check Stack Overflow** for similar issues
4. **Look at the library's GitHub issues**
5. **Ask in community forums** (Reddit r/MachineLearning, Discord servers)

Remember: Every expert was once a beginner who learned to debug! 💪
