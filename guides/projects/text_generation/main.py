# Text Generation - Main Script
# A minimal, beginner-friendly introduction to text generation with GPT-2.

from transformers import pipeline
import torch

print("=" * 70)
print("TEXT GENERATION PROJECT - Creating Text with AI")
print("=" * 70)

# Transformers accepts an integer device index for pipeline().
# Use 0 for the first CUDA GPU and -1 for CPU.
device = 0 if torch.cuda.is_available() else -1
print(f"Using device: {'cuda:0' if device == 0 else 'cpu'}")

print("Loading GPT-2 model...")
generator = pipeline("text-generation", model="gpt2", device=device)
print("✓ Model loaded successfully!")
print("  Model: GPT-2 (124 million parameters)")

# GPT-2 has no dedicated padding token. Reusing EOS for padding is appropriate
# for this simple single-example generation setup.
PAD_TOKEN_ID = generator.tokenizer.eos_token_id

prompt = "Once upon a time in a magical land"
print("\nExample 1: Basic text generation")
generated = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=2,
    pad_token_id=PAD_TOKEN_ID,
)
for i, text in enumerate(generated, 1):
    print(f"\n{i}. {text['generated_text']}")

print("\nExample 2: Sampling controls")
prompt = "The future of artificial intelligence is"

# temperature and top_p affect sampling. They are meaningful when sampling
# is enabled (do_sample=True).
for label, temperature, top_p in [
    ("Lower temperature", 0.3, 0.9),
    ("Higher temperature", 1.2, 0.95),
]:
    result = generator(
        prompt,
        max_new_tokens=30,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
        pad_token_id=PAD_TOKEN_ID,
    )
    print(f"\n{label} ({temperature=} {top_p=}):")
    print(result[0]["generated_text"])

print("\nExample 3: Understanding tokenization")
tokenizer = generator.tokenizer
sample_text = "Artificial intelligence is amazing!"
tokens = tokenizer.tokenize(sample_text)
token_ids = tokenizer.encode(sample_text, add_special_tokens=False)

print(f"Original text: {sample_text}")
print(f"Tokens: {tokens}")
print(f"Token IDs: {token_ids}")
print("Token → ID mapping:")
for token, token_id in zip(tokens, token_ids):
    print(f"  '{token}' → {token_id}")
print(f"Decoded back: {tokenizer.decode(token_ids)}")

print("\nExample 4: Different prompts")
prompts = [
    "In a world where machines can think,",
    "The scientist discovered that",
    "Machine learning is useful because",
    "Python is a programming language that",
]
for prompt in prompts:
    result = generator(
        prompt,
        max_new_tokens=25,
        temperature=0.7,
        do_sample=True,
        pad_token_id=PAD_TOKEN_ID,
    )
    print(f"\nPrompt: {prompt}\nResult: {result[0]['generated_text']}")

print("\nExample 5: A reusable completion function")

def complete_text(prompt, max_new_tokens=30, temperature=0.7):
    """Generate a sampled completion.

    ``max_new_tokens`` counts tokens, not words. ``temperature`` only has an
    effect because sampling is explicitly enabled.
    """
    if max_new_tokens <= 0:
        raise ValueError("max_new_tokens must be greater than zero")
    if temperature <= 0:
        raise ValueError("temperature must be greater than zero")

    result = generator(
        prompt,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=0.95,
        do_sample=True,
        repetition_penalty=1.0,
        pad_token_id=PAD_TOKEN_ID,
    )
    return result[0]["generated_text"]

for prompt, max_new_tokens, temperature in [
    ("The best thing about learning AI is", 20, 0.5),
    ("Neural networks work by", 25, 0.8),
    ("In the year 2050,", 30, 1.0),
]:
    print(f"\nPrompt: {prompt}")
    print(complete_text(prompt, max_new_tokens, temperature))

print("""

Key generation parameters
-------------------------
1. max_new_tokens: maximum number of newly generated tokens, not words.
2. temperature: sampling randomness; it requires do_sample=True.
3. top_p: nucleus sampling cutoff; it is meaningful when sampling.
4. do_sample: True samples from the distribution; False uses greedy/other
   deterministic decoding and ignores sampling controls such as temperature.
5. repetition_penalty: values above 1 can reduce repetition, but excessive
   penalties can hurt quality.

For deterministic generation, use do_sample=False and do not present
sampling parameters such as temperature as controls for that run.
""")

print("Example 6: Optional smaller model")
try:
    small_generator = pipeline("text-generation", model="distilgpt2", device=device)
    result = small_generator(
        "Deep learning is",
        max_new_tokens=30,
        temperature=0.7,
        do_sample=True,
        pad_token_id=small_generator.tokenizer.eos_token_id,
    )
    print(result[0]["generated_text"])
except Exception as exc:
    print(f"Could not load distilgpt2: {exc}")

print("\nNext steps: experiment with prompts, sampling settings, repetition control, and larger models.")
