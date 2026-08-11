# Text Generation Project

A minimal, beginner-friendly introduction to text generation using a pre-trained causal language model.

## What This Project Does

This project demonstrates how to:
- Load GPT-2 with the Hugging Face Transformers pipeline
- Generate continuations from a prompt
- Control stochastic generation with temperature and top-p sampling
- Understand tokenization (text becomes token IDs)
- Build a reusable text-completion function

## Important terminology

**`max_new_tokens` counts tokens, not words.** A token can be a word, subword, punctuation mark, or other tokenizer unit.

**Temperature and top-p are sampling controls.** They matter when `do_sample=True`. If `do_sample=False`, generation is deterministic for a fixed model/input and sampling parameters such as temperature are not used.

## Prerequisites

- Basic Python
- `pip`
- Ability to run a Python script

## Quick Start

### Local installation

```bash
cd guides/projects/text_generation
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

The first run downloads the model from Hugging Face. An internet connection is therefore required unless the model has already been cached locally.

### Google Colab

You can also copy the project into a Colab notebook. A GPU is optional for GPT-2 but can reduce generation time.

## Generation controls

```python
generated = generator(
    prompt,
    max_new_tokens=50,
    temperature=0.7,
    top_p=0.95,
    do_sample=True,
)
```

- **`max_new_tokens`** — maximum number of newly generated tokens.
- **`temperature`** — rescales sampling probabilities. Lower values generally make sampling more conservative; higher values make it more varied.
- **`top_p`** — nucleus sampling. The model samples from the smallest probability mass whose cumulative probability reaches `top_p`.
- **`do_sample=True`** — enables stochastic sampling.
- **`do_sample=False`** — disables sampling; temperature/top-p are not sampling controls in this mode.
- **`repetition_penalty`** — can discourage repeated tokens when set above 1, but excessive values can reduce quality.

These parameters do not guarantee a particular writing quality. Results depend on the model, prompt, seed, hardware/runtime, and generation configuration.

## Tokenization

The example shows the relationship between text, tokens, token IDs, and decoded text:

```python
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text, add_special_tokens=False)
text_again = tokenizer.decode(token_ids)
```

The token list and token-ID list should use the same special-token policy when demonstrating a one-to-one mapping. The project therefore disables automatic special tokens for this simple mapping example.

## Common issues

### `ModuleNotFoundError`

Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Slow CPU generation

- Reduce `max_new_tokens`.
- Try `distilgpt2`.
- Use a supported GPU runtime if available.

Generation speed varies substantially by CPU/GPU, software versions, batch size, and prompt length, so this project intentionally does not promise a universal generation-time number.

### CUDA out of memory

Use CPU or a smaller model. With the pipeline API, CPU is selected with `device=-1`.

### Repetitive output

Experiment with `repetition_penalty`, temperature, top-p, prompt structure, and maximum generation length. There is no universally correct setting.

### Nonsensical output

GPT-2 is an older, relatively small causal language model. Generation quality is model- and prompt-dependent; lower temperature alone does not guarantee factual or coherent output.

## Exercises

1. Generate the same prompt with `temperature=0.3`, `0.7`, and `1.2` while keeping `do_sample=True`.
2. Compare sampling with deterministic generation using `do_sample=False`.
3. Try different `top_p` values.
4. Add a repetition penalty and observe the trade-off.
5. Inspect how different strings are split into tokens.
6. Build a small story generator around `complete_text()`.

## Expected behavior

The project is intended for learning and experimentation, not as a production text-generation service. GPT-2 can produce fluent-looking text but can also be incorrect, repetitive, biased, or nonsensical.

## Next Steps

- Learn more about Transformers and causal language modeling.
- Compare different tokenizers and model architectures.
- Experiment with larger or newer open-weight causal language models.
- Learn about fine-tuning and evaluation.
- Add automated tests around generation configuration and tokenization.

## Resources

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [GPT-2 paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [Hugging Face Course](https://huggingface.co/course)

## Project Stats

| Metric | Value |
|--------|-------|
| GPU Required | No |
| Difficulty | ⭐☆☆ Beginner |
| Prerequisites | Basic Python |

---

The goal is to learn by changing one generation parameter at a time and observing what actually changes.
