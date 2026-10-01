# Text Generation - Main Script
# A minimal, heavily-commented introduction to text generation with pre-trained models
# Lines of code: ~180 (including comments)

from transformers import pipeline
import torch

print("=" * 70)
print("TEXT GENERATION PROJECT - Creating Text with AI")
print("=" * 70)
print()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
if device.type == "cpu":
    print("Note: Text generation works on CPU but is slower. GPU recommended!")
print()

print("Loading GPT-2 model...")
print("(First run will download the model, this may take a minute)")
print()

generator = pipeline(
    "text-generation",
    model="gpt2",
    device=device
)

print("✓ Model loaded successfully!")
print("  Model: GPT-2 (124 million parameters)")
print(f"  Device: {device}")
print()

print("-" * 70)
print("EXAMPLE 1: Basic Text Generation")
print("-" * 70)

prompt = "Once upon a time in a magical land"
print(f"Prompt: {prompt}")
print()

generated = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=2,
    do_sample=True,
    pad_token_id=generator.tokenizer.eos_token_id
)

print("Generated texts:")
for i, text in enumerate(generated, 1):
    print(f"\n{i}. {text['generated_text']}")

print()
print("-" * 70)
print("EXAMPLE 2: Controlling Generation Parameters")
print("-" * 70)

# Temperature only affects generation when sampling is enabled (do_sample=True).
# Lower values make sampling more conservative; higher values make it more random.
# Top-p (nucleus sampling) limits sampling to a probability mass of likely tokens.

prompt = "The future of artificial intelligence is"
print(f"Prompt: {prompt}")
print()

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

print("-" * 70)
print("EXAMPLE 3: Understanding Tokenization")
print("-" * 70)

tokenizer = generator.tokenizer
sample_text = "Artificial intelligence is amazing!"

print(f"Original text: {sample_text}")
print()

tokens = tokenizer.tokenize(sample_text)
print(f"Tokens: {tokens}")
print()

token_ids = tokenizer.encode(sample_text, add_special_tokens=False)
print(f"Token IDs: {token_ids}")
print()

# tokenizer.encode() may add special tokens for some models. We explicitly disable
# them here so the displayed token-to-ID mapping has exactly matching lengths.
print("Token → ID mapping:")
for token, token_id in zip(tokens, token_ids):
    print(f"  '{token}' → {token_id}")

print()
decoded = tokenizer.decode(token_ids)
print(f"Decoded back: {decoded}")
print()

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

print("-" * 70)
print("EXAMPLE 5: Build Your Own Text Completion Function")
print("-" * 70)

def complete_text(prompt, max_new_tokens=30, creativity=0.7):
    """Generate a sampled text completion.

    Args:
        prompt: Starting text.
        max_new_tokens: Maximum number of new tokens to generate.
        creativity: Sampling temperature. Higher values increase randomness.

    Returns:
        Generated text as a string.
    """
    if max_new_tokens < 1:
        raise ValueError("max_new_tokens must be at least 1")
    if creativity <= 0:
        raise ValueError("creativity/temperature must be greater than 0")

    result = generator(
        prompt,
        max_new_tokens=max_new_tokens,
        temperature=creativity,
        top_p=0.95,
        do_sample=True,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    return result[0]["generated_text"]

print("\nTesting custom text completion function:\n")

test_prompts = [
    ("The best thing about learning AI is", 20, 0.5),
    ("Neural networks work by", 25, 0.8),
    ("In the year 2050,", 30, 1.0),
]

for prompt, max_new_tokens, creativity in test_prompts:
    print(f"Prompt: {prompt}")
    print(f"Settings: max_new_tokens={max_new_tokens}, temperature={creativity}")
    result = complete_text(prompt, max_new_tokens, creativity)
    print(f"Result: {result}")
    print()

print("-" * 70)
print("KEY GENERATION PARAMETERS EXPLAINED")
print("-" * 70)

print("""
1. max_new_tokens:
   - How many new tokens (words/pieces) to generate
   - More tokens = longer text but slower

2. temperature:
   - Controls randomness when do_sample=True
   - Lower = more conservative sampling
   - Higher = more random sampling
   - Typical values are around 0.2-1.2, depending on the task

3. top_p (nucleus sampling):
   - Samples from the smallest set of tokens whose cumulative probability reaches p
   - Lower = narrower candidate set
   - Higher = wider candidate set

4. do_sample:
   - True = sample from the next-token distribution
   - False = use deterministic decoding such as greedy decoding
   - temperature/top_p do not control randomness when sampling is disabled

5. repetition_penalty:
   - Penalizes tokens that have already appeared
   - 1.0 means no penalty; larger values discourage repetition
""")

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
- Temperature: Controls sampling randomness when sampling is enabled
- Top-p sampling: Restricts sampling to a probability mass
- Causal language modeling: Predicting the next token

Tips for Better Generation:
1. Use detailed prompts for better results
2. Experiment with temperature (0.7 is a reasonable starting point)
3. Try top_p around 0.9-0.95
4. Use repetition_penalty to avoid loops when appropriate
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
