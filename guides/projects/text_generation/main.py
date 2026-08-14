# Text Generation - Main Script
# A minimal, heavily-commented introduction to text generation with pre-trained models
# Lines of code: ~180 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

print("=" * 70)
print("TEXT GENERATION PROJECT - Creating Text with AI")
print("=" * 70)
print()

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
if device.type == "cpu":
    print("Note: Text generation works on CPU but is slower. GPU recommended!")
print()

# ============================================================================
# STEP 2: LOAD A PRE-TRAINED TEXT GENERATION MODEL
# ============================================================================

# We'll use GPT-2, a famous text generation model from OpenAI
# It's small enough to run on most computers but powerful enough to generate
# coherent text

print("Loading GPT-2 model...")
print("(First run will download the model, this may take a minute)")
print()

# Method 1: Using the pipeline API (easiest)
# The pipeline handles everything: tokenization, generation, decoding
generator = pipeline(
    "text-generation",
    model="gpt2",
    device=device
)

print("✓ Model loaded successfully!")
print(f"  Model: GPT-2 (124 million parameters)")
print(f"  Device: {device}")
print()

# ============================================================================
# STEP 3: BASIC TEXT GENERATION
# ============================================================================

print("-" * 70)
print("EXAMPLE 1: Basic Text Generation")
print("-" * 70)

# Give the model a starting prompt
prompt = "Once upon a time in a magical land"

print(f"Prompt: {prompt}")
print()

# Generate text
# max_new_tokens: how many new words/tokens to generate
# num_return_sequences: how many different versions to create
generated = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=2,
    pad_token_id=generator.tokenizer.eos_token_id
)

print("Generated texts:")
for i, text in enumerate(generated, 1):
    print(f"\n{i}. {text['generated_text']}")

print()

# ============================================================================
# STEP 4: CONTROLLING GENERATION WITH PARAMETERS
# ============================================================================

print("-" * 70)
print("EXAMPLE 2: Controlling Generation Parameters")
print("-" * 70)

# Temperature: Controls randomness
# - Low (0.1-0.5): More predictable, repetitive
# - Medium (0.7-1.0): Balanced
# - High (1.0-2.0): More creative, random

# Top-p (nucleus sampling): Controls vocabulary size
# - Low (0.5): Only most likely words
# - High (0.95): Wider vocabulary

prompt = "The future of artificial intelligence is"

print(f"Prompt: {prompt}")
print()

# Low temperature - more predictable
print("With low temperature (0.3) - more predictable:")
low_temp = generator(
    prompt,
    max_new_tokens=30,
    temperature=0.3,
    top_p=0.9,
    do_sample=True,
    pad_token_id=generator.tokenizer.eos_token_id
)
print(f"  {low_temp[0]['generated_text']}")
print()

# High temperature - more creative
print("With high temperature (1.2) - more creative:")
high_temp = generator(
    prompt,
    max_new_tokens=30,
    temperature=1.2,
    top_p=0.95,
    do_sample=True,
    pad_token_id=generator.tokenizer.eos_token_id
)
print(f"  {high_temp[0]['generated_text']}")
print()

# ============================================================================
# STEP 5: UNDERSTANDING TOKENIZATION
# ============================================================================

print("-" * 70)
print("EXAMPLE 3: Understanding Tokenization")
print("-" * 70)

# Before the model can process text, it must be converted to numbers
# This process is called tokenization

tokenizer = generator.tokenizer

sample_text = "Artificial intelligence is amazing!"

print(f"Original text: {sample_text}")
print()

# Tokenize the text
tokens = tokenizer.tokenize(sample_text)
print(f"Tokens: {tokens}")
print()

# Convert to token IDs (without special tokens to match tokenize() output)
token_ids = tokenizer.encode(sample_text, add_special_tokens=False)
print(f"Token IDs: {token_ids}")
print()

# Show the mapping
print("Token → ID mapping:")
for token, token_id in zip(tokens, token_ids):
    print(f"  '{token}' → {token_id}")

print()

# Decode back to text
decoded = tokenizer.decode(token_ids)
print(f"Decoded back: {decoded}")
print()

# ============================================================================
# STEP 6: GENERATING WITH DIFFERENT PROMPTS
# ============================================================================

print("-" * 70)
print("EXAMPLE 4: Generating Different Types of Text")
print("-" * 70)

prompts = [
    "In a world where machines can think,",
    "The scientist discovered that",
    "Machine learning is useful because",
    "Python is a programming language that",
]

for prompt in prompts:
    print(f"\nPrompt: {prompt}")
    result = generator(
        prompt,
        max_new_tokens=25,
        temperature=0.7,
        do_sample=True,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    print(f"Result: {result[0]['generated_text']}")
    print("-" * 50)

print()

# ============================================================================
# STEP 7: BUILDING A SIMPLE TEXT COMPLETION FUNCTION
# ============================================================================

print("-" * 70)
print("EXAMPLE 5: Build Your Own Text Completion Function")
print("-" * 70)

def complete_text(prompt, max_words=30, creativity=0.7):
    """
    Generate text completion for a given prompt.
    
    Args:
        prompt: Starting text
        max_words: Maximum number of new tokens to generate
        creativity: 0.1 (predictable) to 1.5 (very creative)
    
    Returns:
        Generated text as a string
    """
    result = generator(
        prompt,
        max_new_tokens=max_words,
        temperature=creativity,
        top_p=0.95,
        do_sample=True,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    return result[0]['generated_text']

# Test our function
print("\nTesting custom text completion function:\n")

test_prompts = [
    ("The best thing about learning AI is", 20, 0.5),
    ("Neural networks work by", 25, 0.8),
    ("In the year 2050,", 30, 1.0),
]

for prompt, words, creativity in test_prompts:
    print(f"Prompt: {prompt}")
    print(f"Settings: max_words={words}, creativity={creativity}")
    result = complete_text(prompt, words, creativity)
    print(f"Result: {result}")
    print()

# ============================================================================
# STEP 8: UNDERSTANDING GENERATION PARAMETERS
# ============================================================================

print("-" * 70)
print("KEY GENERATION PARAMETERS EXPLAINED")
print("-" * 70)

print("""
1. max_new_tokens: 
   - How many new tokens (words/pieces) to generate
   - More tokens = longer text but slower

2. temperature:
   - Controls randomness (0.1 to 2.0)
   - Low = predictable, repetitive
   - High = creative, random
   - Default = 1.0

3. top_p (nucleus sampling):
   - Controls vocabulary size (0.0 to 1.0)
   - Low = only most likely words
   - High = wider vocabulary
   - Default = 1.0

4. do_sample:
   - True = sample randomly (creative)
   - False = always pick most likely (greedy)

5. repetition_penalty:
   - Penalizes repeating words (1.0 to 2.0)
   - Higher = less repetition
   - Default = 1.0
""")

# ============================================================================
# STEP 9: TRYING A DIFFERENT MODEL
# ============================================================================

print("-" * 70)
print("EXAMPLE 6: Using a Different Model (Optional)")
print("-" * 70)

print("Loading a smaller, faster model: distilgpt2...")
print("(This is a smaller version of GPT-2)")
print()

try:
    small_generator = pipeline(
        "text-generation",
        model="distilgpt2",
        device=device
    )
    
    prompt = "Deep learning is"
    print(f"Prompt: {prompt}")
    
    result = small_generator(
        prompt,
        max_new_tokens=30,
        temperature=0.7,
        do_sample=True,
        pad_token_id=small_generator.tokenizer.eos_token_id
    )
    
    print(f"Result: {result[0]['generated_text']}")
    print()
    print("Note: Smaller models are faster but may produce less coherent text")
    
except Exception as e:
    print(f"Could not load alternative model: {e}")
    print("This is okay! The default GPT-2 model works great.")

print()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the Text Generation Project!")
print("=" * 70)
print("""
What you learned:
✓ How to load a pre-trained text generation model
✓ How to generate text from a prompt
✓ How to control generation with parameters (temperature, top_p)
✓ How tokenization works (text → numbers)
✓ How to build a custom text completion function
✓ The difference between small and large models

Key Concepts:
- Tokens: Pieces of text (words, subwords, characters)
- Temperature: Controls randomness vs. predictability
- Top-p sampling: Controls vocabulary size
- Causal language modeling: Predicting the next token

Tips for Better Generation:
1. Use detailed prompts for better results
2. Experiment with temperature (0.7 is usually good)
3. Try top_p around 0.9-0.95
4. Use repetition_penalty to avoid loops
5. Longer prompts give more context

Next steps:
1. Try different prompts and see what you can create
2. Experiment with temperature and top_p
3. Try larger models (GPT-2 large, GPT-Neo)
4. Learn about fine-tuning for custom text generation
5. Build a story generator, chatbot, or creative writing tool

Resources:
- Hugging Face Documentation: https://huggingface.co/docs/transformers
- GPT-2 Paper: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- Hugging Face Course: https://huggingface.co/course
""")
print("=" * 70)
