# ImportError: Cannot Import Transformers

## Error Message

```
ModuleNotFoundError: No module named 'transformers'
```

or

```
ImportError: cannot import name 'pipeline' from 'transformers'
```

## Cause

This error occurs when:
1. The `transformers` library is not installed
2. The library is installed in a different Python environment
3. There's a version conflict or corrupted installation

## Solution

### Step 1: Verify Your Environment

First, make sure you're in the correct virtual environment:

```bash
# Check if virtual environment is active
# You should see (venv) or similar at the beginning of your prompt

# If not activated, activate it:
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 2: Install Transformers

Install the transformers library with the required dependencies:

```bash
pip install transformers torch sentence-transformers scikit-learn
```

For the projects in this repository, use the project-specific requirements:

```bash
cd guides/projects/transformers_intro
pip install -r requirements.txt
```

### Step 3: Verify Installation

Check that the package is installed correctly:

```bash
python -c "from transformers import pipeline; print('Success!')"
```

If you see "Success!", the installation worked.

### Step 4: Common Issues

**Issue: Permission Denied**
```bash
# Add --user flag
pip install --user transformers
```

**Issue: SSL Certificate Error**
```bash
# Try with trusted host
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org transformers
```

**Issue: Slow Download**
```bash
# Use a mirror (for users in China)
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple transformers
```

### Step 5: For Google Colab Users

In Google Colab, packages may need to be reinstalled each session:

```python
!pip install transformers torch sentence-transformers scikit-learn
```

Then restart the runtime: **Runtime → Restart Runtime**

## Prevention

Always create and activate a virtual environment before installing packages:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Still Having Issues?

1. **Check Python version**: Transformers requires Python 3.7+
   ```bash
   python --version
   ```

2. **Upgrade pip**:
   ```bash
   pip install --upgrade pip
   ```

3. **Clean reinstall**:
   ```bash
   pip uninstall transformers torch
   pip cache purge
   pip install transformers torch
   ```

4. **Check for conflicts**:
   ```bash
   pip list | grep -E "transform|torch"
   ```

## Related Errors

- [CUDA OOM](CUDA_OOM.md) - Out of memory errors
- [Main README](../README.md) - Return to guides overview

---

**Last updated:** 2024  
**Applies to:** All projects using Hugging Face transformers
