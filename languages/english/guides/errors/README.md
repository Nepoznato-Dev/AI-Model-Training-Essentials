# Common Errors Guide

This directory contains solutions to common errors you may encounter when working with AI/ML projects.

## 📚 Available Error Guides

### Installation & Import Errors

| Error | Description | Solution |
|-------|-------------|----------|
| [ImportError: Transformers](ImportError_Transformers.md) | Cannot import transformers or related packages | Step-by-step installation guide |
| CUDA Out of Memory | GPU memory exhausted during training | Memory optimization techniques |
| Python Version Mismatch | Incompatible Python version for packages | Version management guide |

### Runtime Errors

| Error | Description | Solution |
|-------|-------------|----------|
| [CUDA OOM](CUDA_OOM.md) | Out of memory during model training | Batch size reduction, gradient accumulation |
| Model Download Failed | Cannot download pre-trained models | Network troubleshooting, manual download |
| Shape Mismatch | Tensor dimension errors | Debugging tensor shapes |

### Performance Issues

| Error | Description | Solution |
|-------|-------------|----------|
| Slow Training | Training is extremely slow on CPU | GPU setup, optimization tips |
| Low Accuracy | Model not learning effectively | Hyperparameter tuning guide |

## 🆘 Quick Troubleshooting

**Before diving into specific error guides:**

1. **Read the error message carefully** - Python error messages are descriptive
2. **Check your environment** - Ensure virtual environment is activated
3. **Verify installations** - Run `pip list` to confirm packages
4. **Google the exact error** - Copy-paste the full traceback

## 🔧 General Solutions

### For Import Errors:
```bash
# Reinstall the problematic package
pip uninstall <package-name>
pip install <package-name>

# Or reinstall all project dependencies
pip install -r requirements.txt --force-reinstall
```

### For CUDA/GPU Issues:
```python
# Check if CUDA is available
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Device count: {torch.cuda.device_count()}")
```

### For Memory Issues:
- Reduce batch size (e.g., from 64 to 16 or 8)
- Use gradient accumulation
- Enable mixed precision training
- Consider using Google Colab with free GPU

## 📖 Additional Resources

- [Projects README](../projects/README.md) - Main projects documentation
- [Prerequisites](../prerequisites/README.md) - Foundational knowledge
- [Hardware Reality Check](../hardware_reality_check.md) - Hardware requirements

---

**Still stuck?** Open an issue on GitHub or ask in community forums like Stack Overflow, Reddit's r/MachineLearning, or Hugging Face Discord.
