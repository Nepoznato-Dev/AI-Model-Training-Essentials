# Text Generation Project

A minimal, beginner-friendly introduction to text generation using pre-trained language models.

## What This Project Does

This project demonstrates how to:
- Load a pre-trained text generation model (GPT-2)
- Generate coherent text from a prompt
- Control generation with parameters (temperature, top-p)
- Understand tokenization (how text becomes numbers)
- Build a custom text completion function

## Concepts Covered

- **Language Models**: Models that predict the next word/token
- **Text Generation**: Creating new text from a starting prompt
- **Tokenization**: Converting text into numbers the model can process
- **Temperature**: Controlling randomness vs. predictability
- **Top-p Sampling**: Controlling vocabulary size
- **Causal Language Modeling**: The task of predicting next tokens

## Prerequisites

Before running this project, you should be comfortable with:
- Basic Python programming
- Installing Python packages with pip
- Running Python scripts from the command line

If you're new to these concepts, check out:
- [Python Basics](../User%20Questions/prerequisites/python_basics.md)
- [Terminal Basics](../User%20Questions/prerequisites/terminal_basics.md)

## Quick Start

### Option 1: Google Colab (Recommended for Beginners)

1. Visit [Google Colab](https://colab.research.google.com)
2. Create a new notebook
3. Copy the code from `main.py` into cells
4. Click **Runtime → Change runtime type** and select **GPU** (optional but faster)
5. Run each cell sequentially

**Benefits:**
- No setup required
- Free GPU access (faster generation)
- Pre-installed libraries
- Easy to experiment and modify

### Option 2: Local Installation

```bash
# Navigate to this project directory
cd guides/projects/text_generation

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

## Code Walkthrough

### Step 1: Import Required Libraries

```python
from transformers import pipeline
import torch
```

We use the `transformers` library from Hugging Face, which provides:
- Pre-trained models ready for text generation
- Simple pipeline API for easy usage
- Tokenizers for text preprocessing

### Step 2: Load a Pre-trained Model

```python
generator = pipeline("text-generation", model="gpt2")
```

This single line:
- Downloads the GPT-2 model (124 million parameters)
- Loads the tokenizer
- Sets up the generation pipeline

GPT-2 is:
- Small enough to run on most computers
- Good at generating coherent English text
- Trained on a diverse internet dataset

### Step 3: Generate Text

```python
prompt = "Once upon a time in a magical land"
generated = generator(prompt, max_new_tokens=50)
```

The model:
1. Takes your prompt as input
2. Predicts the most likely next token
3. Adds it to the text
4. Repeats until reaching max_new_tokens

### Step 4: Control Generation

```python
generated = generator(
    prompt,
    max_new_tokens=50,
    temperature=0.7,
    top_p=0.95,
    do_sample=True
)
```

Key parameters:
- **temperature**: Higher = more creative, Lower = more predictable
- **top_p**: Controls vocabulary size
- **do_sample**: True for random sampling, False for greedy

## Exercises

Try these modifications to deepen your understanding:

### Exercise 1: Creative Writing
Write prompts for different genres:
- Science fiction
- Mystery
- Comedy
- Horror

### Exercise 2: Temperature Experiment
Generate the same prompt with different temperatures:
- 0.1 (very predictable)
- 0.7 (balanced)
- 1.5 (very creative)

Compare the results.

### Exercise 3: Story Completion
Start a story and let the model continue it:
```python
prompt = "The detective walked into the dark room and noticed"
```

### Exercise 4: Code Generation
Try generating code snippets:
```python
prompt = "def calculate_fibonacci(n):"
```

### Exercise 5: Build a Poem Generator
Create a function that generates poems:
```python
def generate_poem(starting_line):
    # Your code here
    pass
```

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'transformers'"

**Solution:**
```bash
pip install transformers torch
```

### Issue: Slow generation on CPU

**Solution:**
1. Use Google Colab with GPU enabled
2. Use a smaller model: `model="distilgpt2"`
3. Reduce `max_new_tokens`

### Issue: Repetitive text

**Solution:**
1. Add `repetition_penalty=1.2`
2. Increase `temperature` slightly
3. Use `top_p=0.9` instead of 1.0

### Issue: Nonsensical output

**Solution:**
1. Lower the temperature (try 0.5)
2. Provide a more detailed prompt
3. Remember: GPT-2 is small and makes mistakes

### Issue: CUDA out of memory

**Solution:**
```python
# Use CPU instead
generator = pipeline("text-generation", model="gpt2", device=-1)
```

Or use a smaller model like `distilgpt2`.

## Understanding Generation Parameters

### Temperature
- **Range**: 0.1 to 2.0
- **Low (0.1-0.5)**: Very predictable, may repeat
- **Medium (0.7-1.0)**: Balanced creativity and coherence
- **High (1.0-2.0)**: Very creative, may be nonsensical

### Top-p (Nucleus Sampling)
- **Range**: 0.0 to 1.0
- **Low (0.5)**: Only considers most likely words
- **High (0.95)**: Wider vocabulary
- **Default**: 1.0 (consider all words)

### Max New Tokens
- How many new tokens to generate
- More tokens = longer text but slower
- Typical: 20-100 for short text

### Repetition Penalty
- **Range**: 1.0 to 2.0
- **1.0**: No penalty
- **1.2-1.5**: Reduces repetition
- Higher = less repetition but may affect coherence

## Expected Results

With the default configuration:
- **Model**: GPT-2 (124M parameters)
- **Generation Time**: ~1-3 seconds per sample on CPU
- **Text Quality**: Coherent short passages
- **Best For**: Learning, experimentation, creative writing

**Note:** GPT-2 is a small model. Larger models (GPT-3, GPT-4) produce much better results but require API access.

## Next Steps

After completing this project:

1. **Read the Guide**: Check out the full [Transformers Guide](../../Transformers/) for deeper theory

2. **Try the Transformers Intro Project**: Learn about text classification

3. **Experiment with Prompts**:
   - Write story starters
   - Create conversation openers
   - Design creative writing prompts

4. **Try Larger Models**:
   - GPT-2 Large (774M parameters)
   - GPT-Neo (1.3B, 2.7B parameters)
   - Access via Hugging Face or APIs

5. **Build Applications**:
   - Story generator
   - Chatbot
   - Code completion tool
   - Creative writing assistant

## Resources

- [Hugging Face Documentation](https://huggingface.co/docs/transformers)
- [GPT-2 Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [Hugging Face Course](https://huggingface.co/course) - Free comprehensive course
- [GPT-2 Demo](https://huggingface.co/spaces/akhaliq/gpt-2) - Try it online

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~180 |
| Time to Complete | 15-20 minutes |
| GPU Required | No (but recommended) |
| Difficulty | ⭐☆☆ Beginner |
| Prerequisites | Basic Python |

## Contributing

Found an issue? Have a suggestion? Feel free to:
- Open an issue on GitHub
- Submit a pull request with improvements
- Share your extensions in the community

---

**Happy Learning!** 🎉

Remember: The best way to learn is by experimenting. Try different prompts, play with parameters, and see what creative text you can generate!
