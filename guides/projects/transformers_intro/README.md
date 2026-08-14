# Transformers Introduction Project

A minimal, beginner-friendly introduction to using pre-trained transformer models for text classification.

## What This Project Does

This project demonstrates how to:
- Load pre-trained transformer models from Hugging Face
- Tokenize text input for transformer models
- Perform text classification using a pre-trained model
- Interpret model predictions

## Concepts Covered

- **Transformer Architecture Basics**: Understanding the encoder-decoder structure
- **Pre-trained Models**: Leveraging models trained on massive datasets
- **Tokenization**: Converting text into numerical inputs
- **Fine-tuning Fundamentals**: How to adapt models to specific tasks
- **Inference Pipeline**: Making predictions with trained models

## Prerequisites

Before running this project, you should be comfortable with:
- Basic Python programming
- Installing Python packages with pip
- Running Python scripts from the command line

If you're new to these concepts, check out:
- [Python Basics](../../User%20Questions/prerequisites/python_basics.md)
- [Terminal Basics](../../User%20Questions/prerequisites/terminal_basics.md)

## Quick Start

### Option 1: Google Colab (Recommended for Beginners)

1. Visit [Google Colab](https://colab.research.google.com)
2. Create a new notebook
3. Copy the code from `main.py` into cells
4. Click **Runtime → Change runtime type** and select **GPU** (optional but faster)
5. Run each cell sequentially

**Benefits:**
- No setup required
- Free GPU access (faster inference)
- Pre-installed libraries (transformers, torch)
- Easy to experiment and modify

### Option 2: Local Installation

```bash
# Navigate to this project directory
cd guides/projects/transformers_intro

# Create a virtual environment (recommended)
python -m venv venv

# Activate the environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the project
python main.py
```

## Files in This Project

| File | Description |
|------|-------------|
| `main.py` | Main script with heavily commented code (~180 lines) |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation file |
| `transformers_intro.ipynb` | Jupyter notebook version (optional) |

## Code Walkthrough

### Step 1: Import Required Libraries

```python
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
```

We use the `transformers` library from Hugging Face, which provides:
- Pre-trained models ready for inference
- Tokenizers for text preprocessing
- Simple pipelines for common tasks

### Step 2: Load a Pre-trained Model

```python
classifier = pipeline("sentiment-analysis")
```

This single line:
- Downloads a pre-trained sentiment analysis model
- Loads the appropriate tokenizer
- Sets up the inference pipeline

The default model is `distilbert-base-uncased-finetuned-sst-2-english`, which is:
- Small enough to run quickly
- Accurate for sentiment detection
- Trained on movie reviews (SST-2 dataset)

### Step 3: Make Predictions

```python
text = "I absolutely love this product! Best purchase ever."
result = classifier(text)
print(result)
# Output: [{'label': 'POSITIVE', 'score': 0.9998}]
```

The model returns:
- **label**: The predicted class (POSITIVE or NEGATIVE)
- **score**: Confidence level (0 to 1)

### Step 4: Batch Processing

```python
texts = [
    "This is amazing!",
    "Terrible experience, would not recommend.",
    "It's okay, nothing special."
]

results = classifier(texts)
for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} ({result['score']:.2%})")
    print()
```

### Step 5: Using Different Models

```python
# Load a different pre-trained model
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
classifier = pipeline("sentiment-analysis", model=model_name)
```

You can find thousands of pre-trained models at:
- [Hugging Face Model Hub](https://huggingface.co/models)
- Filter by task: text-classification, question-answering, etc.

## Exercises

Try these modifications to deepen your understanding:

### Exercise 1: Test Your Own Texts
Modify the script to analyze:
- Product reviews from Amazon
- Tweets about a topic you care about
- Email subject lines

### Exercise 2: Compare Models
Load two different sentiment analysis models and compare their predictions on the same texts. Do they agree?

### Exercise 3: Multi-class Classification
Find a model that does more than binary classification (e.g., positive/neutral/negative) and test it.

### Exercise 4: Build a Simple App
Create a function that takes user input and displays sentiment with emoji:
- POSITIVE → 😊
- NEGATIVE → 😞
- NEUTRAL → 😐

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'transformers'"

**Solution:**
```bash
pip install transformers torch
```

Or make sure your virtual environment is activated.

### Issue: Slow Performance on CPU

**Solution:**
Transformers can be slow on CPU. Options:
1. Use Google Colab with GPU enabled
2. Use smaller models (look for "distil" or "tiny" in model names)
3. Process fewer texts at once

### Issue: CUDA Out of Memory

**Solution:**
If you get this error on GPU:
```python
# Move model to CPU instead
classifier = pipeline("sentiment-analysis", device=-1)
```

Or reduce batch size when processing multiple texts.

### Issue: Unexpected Results

**Solution:**
Remember that models are trained on specific datasets. A model trained on movie reviews might not work well on:
- Medical texts
- Legal documents
- Technical manuals

Choose a model appropriate for your domain, or fine-tune it on your data.

## Understanding the Output

Example output:
```
[{'label': 'POSITIVE', 'score': 0.9998765432}]
```

- **label**: The predicted class. For sentiment analysis, this is typically:
  - `POSITIVE`: Positive sentiment
  - `NEGATIVE`: Negative sentiment
  
- **score**: Confidence score between 0 and 1
  - 0.99+ = Very confident
  - 0.7-0.9 = Moderately confident
  - < 0.7 = Uncertain (model is unsure)

## Next Steps

After completing this project:

1. **Read the Guide**: Check out the full [Transformers Guide](../../Transformers/) for deeper theory

2. **Try Fine-tuning**: Learn how to adapt a pre-trained model to your specific task

3. **Explore Other Tasks**:
   - Question answering
   - Text generation
   - Named entity recognition
   - Translation

4. **Build Something**: Create a small application:
   - Twitter sentiment tracker
   - Review analyzer
   - Spam detector

## Resources

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [Hugging Face Course](https://huggingface.co/course) - Free comprehensive course
- [Model Hub](https://huggingface.co/models) - Browse thousands of pre-trained models
- [Papers With Code](https://paperswithcode.com/) - Research papers with implementations

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~180 |
| Time to Complete | 15-20 minutes |
| GPU Required | No (but recommended) |
| Difficulty | ⭐⭐☆ Easy |
| Prerequisites | Basic Python |

## Contributing

Found an issue? Have a suggestion? Feel free to:
- Open an issue on GitHub
- Submit a pull request with improvements
- Share your extensions in the community

---

**Happy Learning!** 🎉

Remember: Every expert was once a beginner. Run the code, break it, modify it, and learn from it!
