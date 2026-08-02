# Common Errors Knowledge Base 🔧

**Beginners spend 80% of their time debugging.** This directory turns frustration into learning moments!

---

## 📚 Available Error Guides

| Error | What It Means | Quick Fix |
|-------|---------------|-----------|
| [CUDA Out of Memory](./CUDA_OOM.md) | GPU ran out of video memory | Reduce batch size |
| [ImportError: transformers](./ImportError_Transformers.md) | Can't find transformers library | Install with pip |
| [Torch Not Installed](./Torch_Not_Installed.md) | PyTorch not found | Install from pytorch.org |

---

## 🎯 How to Use This Directory

### When You Get an Error:

1. **Copy the error message** (exact text)
2. **Search this directory** for matching error files
3. **Follow the fixes in order** (they're ranked by effectiveness)
4. **Still stuck?** Check the "Still Not Working?" section

---

## 🔍 Quick Diagnostic Flowchart

```
Got an error?
    ↓
Is it about memory/CUDA? 
    → Yes → [CUDA_OOM.md](./CUDA_OOM.md)
    ↓ No
Is it about importing a library?
    → transformers → [ImportError_Transformers.md](./ImportError_Transformers.md)
    → torch → [Torch_Not_Installed.md](./Torch_Not_Installed.md)
    ↓ No
Google the exact error message + "github"
```

---

## 💡 Pro Tips for Debugging

### Tip 1: Read the Full Error

Most errors have helpful messages at the bottom:
```python
RuntimeError: CUDA out of memory. Tried to allocate 2.00 GiB...
← This tells you exactly what went wrong!
```

### Tip 2: Search Smart

Good search queries:
- `"CUDA out of memory" site:github.com`
- `"No module named transformers" stackoverflow`
- `pytorch import error reddit`

### Tip 3: Check Your Versions

Many errors are version mismatches:
```python
import torch, transformers, sys
print(f"PyTorch: {torch.__version__}")
print(f"Transformers: {transformers.__version__}")
print(f"Python: {sys.version}")
```

### Tip 4: Start Fresh

When all else fails:
```bash
# Create new environment
python -m venv fresh_env
source fresh_env/bin/activate  # Windows: fresh_env\Scripts\activate

# Install only what you need
pip install torch transformers

# Test immediately
python -c "import torch; print('Works!')"
```

---

## 🆘 Emergency Checklist

Can't solve your error? Gather this info before asking for help:

- [ ] Exact error message (copy-paste, don't paraphrase)
- [ ] Python version (`python --version`)
- [ ] Installed packages (`pip list`)
- [ ] Operating system (Windows/Mac/Linux + version)
- [ ] What you were trying to do
- [ ] Code that caused the error (minimal example)
- [ ] What you've already tried

---

## 📖 Learning from Errors

Every error teaches you something:

| Error Type | What You Learn |
|------------|----------------|
| Import errors | Package management, environments |
| Memory errors | Resource optimization, model sizing |
| Type errors | Data structures, Python typing |
| Runtime errors | Logic flow, edge cases |
| Syntax errors | Python grammar, attention to detail |

**Remember:** Professional developers get errors daily. The skill isn't avoiding errors—it's solving them efficiently!

---

## 🔗 Linked from Guides

These errors are referenced throughout the guides:

### From RAG Guide:
- [CUDA_OOM.md](./CUDA_OOM.md) - Chapter 3 (Training Retrievers)
- [ImportError_Transformers.md](./ImportError_Transformers.md) - Chapter 1 (Setup)

### From Transformers Guide:
- [Torch_Not_Installed.md](./Torch_Not_Installed.md) - Chapter 1 (Setup)
- [CUDA_OOM.md](./CUDA_OOM.md) - Chapter 4 (Fine-tuning)

### From CNNs Guide:
- [Torch_Not_Installed.md](./Torch_Not_Installed.md) - Chapter 1 (Setup)
- [CUDA_OOM.md](./CUDA_OOM.md) - Chapter 3 (Training)

---

## 🙏 Contributing

Found an error not covered here? Contribute!

1. Create a new file: `Error_Name.md`
2. Follow the template below
3. Submit a pull request

### Error File Template:

```markdown
# Error Title 🔥

**Error Message:**
```
[paste exact error]
```

## What This Means

[Simple explanation]

## Quick Fixes (Try in Order)

### Fix 1: [Most common solution]
[Code/example]

### Fix 2: [Second most common]
[Code/example]

## Prevention Tips

[How to avoid this error]

## Related Errors

- [Link to related error files]
```

---

## 📞 Getting More Help

If these guides don't solve your problem:

1. **Stack Overflow** - https://stackoverflow.com/questions/tagged/pytorch
2. **GitHub Issues** - Check the library's issue tracker
3. **Reddit** - r/MachineLearning, r/learnmachinelearning
4. **Discord** - PyTorch Discord, Hugging Face Discord
5. **Forums** - https://discuss.pytorch.org/, https://discuss.huggingface.co/

---

<div align="center">

**Errors are not failures—they're learning opportunities!** 💪

[← Back to Prerequisites](../prerequisites/) | [Start RAG Guide](../guides/RAG/)

</div>
