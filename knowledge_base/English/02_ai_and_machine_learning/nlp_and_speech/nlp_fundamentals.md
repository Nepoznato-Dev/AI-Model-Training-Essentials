---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [nlp, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# NLP Fundamentals

Natural Language Processing (NLP) is the field of teaching machines to understand, generate, and work with human language. It powers search engines, chatbots, translation systems, sentiment analysis, and the large language models (LLMs) that have transformed AI since 2020. This file covers the evolution from classical techniques to modern Transformer-based architectures.

---

## Text Preprocessing

Raw text is messy. Before a model can use it, it needs to be cleaned and structured.

| Step | What It Does | Example |
|------|-------------|---------|
| **Tokenisation** | Split text into tokens (words, subwords, or characters) | "I love NLP" → `["I", "love", "NLP"]` |
| **Lowercasing** | Convert to lowercase | "Hello" → "hello" |
| **Stop word removal** | Remove common words (the, is, at) | "the cat sat" → "cat sat" |
| **Stemming** | Chop word endings (crude) | "running" → "run" |
| **Lemmatization** | Reduce to dictionary form (context-aware) | "better" → "good" |
| **Normalisation** | Fix encoding, remove special chars, expand contractions | "don't" → "do not" |

Modern Transformer models often skip stop word removal and stemming — they learn these patterns from data.

---

## Text Representation

Machines need numbers, not words. How we represent text as vectors is fundamental.

### Classical Approaches

| Method | Description | Limitation |
|--------|-------------|-----------|
| **One-Hot Encoding** | Each word is a unique position in a huge vector | Sparse; no semantic meaning |
| **Bag of Words (BoW)** | Count word frequencies; ignore order | Loses word order entirely |
| **TF-IDF** | Weight words by frequency in document × rarity across corpus | Still ignores order and context |

### Word Embeddings

Embeddings map words to dense vectors where similar words are close together.

| Model | Key Idea |
|-------|----------|
| **Word2Vec** (2013) | Predict word from context (CBOW) or context from word (Skip-gram) |
| **GloVe** (2014) | Global co-occurrence statistics → dense vectors |
| **FastText** (2016) | Word2Vec + subword information (handles rare words better) |

The famous example: `king - man + woman ≈ queen`. Embeddings capture semantic relationships.

**Limitation**: classical embeddings assign one vector per word, so they can't handle polysemy (words with multiple meanings). "Bank" in "river bank" and "bank account" gets the same vector.

---

## Sequence Models

Before Transformers, the standard approach for NLP was to process text sequentially.

| Architecture | How It Works | Strength | Weakness |
|-------------|-------------|----------|----------|
| **RNN** | Process tokens one at a time; maintain hidden state | Handles variable-length input | Vanishing gradients; can't capture long dependencies |
| **LSTM** | RNN with gates (forget, input, output) to control information flow | Better at long-range dependencies | Still sequential; slow to train |
| **GRU** | Simplified LSTM (fewer gates) | Faster than LSTM; similar performance | Same fundamental limitations |

These models process text left-to-right, which means they're slow to train (can't parallelise) and struggle with long-range dependencies.

---

## The Attention Mechanism

Attention lets a model look at all positions in a sequence simultaneously and decide which ones are most relevant for the current prediction.

### Key Insight

Instead of compressing an entire sentence into a single hidden state (as RNNs do), attention computes a weighted sum of all hidden states, where the weights are learned.

```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Component | Role |
|-----------|------|
| **Query (Q)** | What am I looking for? |
| **Key (K)** | What do I contain? |
| **Value (V)** | What information do I provide? |
| **√d_k** | Scaling factor to prevent large dot products |

---

## The Transformer Architecture

The Transformer (Vaswani et al., 2017 — "Attention Is All You Need") replaced recurrence entirely with attention. It's the foundation of virtually all modern NLP.

### Architecture

| Component | Description |
|-----------|-------------|
| **Encoder** | Reads input text; produces contextual representations |
| **Decoder** | Generates output text; attends to encoder output |
| **Self-Attention** | Each token attends to all other tokens in the same sequence |
| **Multi-Head Attention** | Run multiple attention heads in parallel; capture different relationships |
| **Positional Encoding** | Inject position information (since there's no recurrence) |
| **Feed-Forward Network** | Applied to each position independently |
| **Layer Normalisation** | Stabilise training |
| **Residual Connections** | Skip connections for gradient flow |

### Encoder-Only, Decoder-Only, Encoder-Decoder

| Variant | Architecture | Best For | Examples |
|---------|-------------|----------|---------|
| **Encoder-only** | Understands text | Classification, NER, sentiment analysis | BERT, RoBERTa, DeBERTa |
| **Decoder-only** | Generates text | Language models, chatbots, code generation | GPT-3/4, LLaMA, Claude |
| **Encoder-Decoder** | Transforms text | Translation, summarisation | T5, BART, mBART |

---

## Major Model Families

### BERT Family (Encoder-Only)

| Model | Key Feature |
|-------|-------------|
| **BERT** (2018) | Masked Language Model + Next Sentence Prediction |
| **RoBERTa** | Removed NSP; trained longer with more data |
| **ALBERT** | Parameter sharing; smaller footprint |
| **DeBERTa** | Disentangled attention; improved NLU |
| **DistilBERT** | 40% smaller, 60% faster, retains 97% of BERT's performance |

### GPT Family (Decoder-Only)

| Model | Parameters | Notes |
|-------|-----------|-------|
| **GPT-2** | 1.5B | Showed decoder-only models can generate coherent text |
| **GPT-3** | 175B | Few-shot learning; prompted rather than fine-tuned |
| **GPT-3.5 / GPT-4** | Undisclosed | Instruction-tuned + RLHF; conversational |
| **LLaMA** (Meta) | 7B–70B | Open-weight; spawned the open-source LLM ecosystem |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Efficient open models with strong performance |

---

## Core NLP Tasks

| Task | Description | Typical Model |
|------|-------------|--------------|
| **Text Classification** | Assign a label to text (spam/not spam, positive/negative) | BERT, fine-tuned classifiers |
| **Named Entity Recognition (NER)** | Identify people, organisations, locations in text | BERT + CRF layer |
| **Sentiment Analysis** | Determine emotional tone | Fine-tuned BERT or zero-shot LLM |
| **Machine Translation** | Translate between languages | T5, mBART, MarianMT |
| **Question Answering** | Answer questions given context | BERT (extractive), GPT (generative) |
| **Summarisation** | Condense long text | T5, BART, GPT |
| **Text Generation** | Produce coherent text | GPT-4, LLaMA, Claude |

---

## Fine-Tuning vs Prompting

| Approach | How It Works | When to Use |
|----------|-------------|-------------|
| **Fine-tuning** | Update model weights on your task-specific data | You have labelled data; need maximum performance |
| **Prompting** | Give the model instructions in natural language | Quick prototyping; limited data; using LLMs |
| **Few-shot** | Include examples in the prompt | When you have a few examples but not enough for fine-tuning |
| **LoRA / QLoRA** | Efficient fine-tuning; update small low-rank matrices | Fine-tune large models with limited GPU memory |

---

## Tools and Frameworks

| Tool | Purpose |
|------|---------|
| **Hugging Face Transformers** | Pre-trained models, tokenisers, fine-tuning pipelines |
| **spaCy** | Production-grade NLP pipeline (tokenisation, NER, POS, dependency) |
| **NLTK** | Educational; classical NLP algorithms |
| **Gensim** | Topic modelling (LDA), word embeddings (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Frameworks for building LLM-powered applications |
| **vLLM** | High-throughput LLM serving |
| **Tokenizers (HF)** | Fast tokenisation (BPE, WordPiece, SentencePiece) |

---

## The LLM Landscape

The modern NLP landscape is dominated by Large Language Models:

| Category | Examples | Notes |
|----------|---------|-------|
| **Proprietary** | GPT-4, Claude, Gemini | Best performance; API access only |
| **Open-weight** | LLaMA 3, Mistral, Qwen | Weights available; run locally |
| **Open-source** | Pythia, OPT | Fully open (data, weights, code) |
| **Multimodal** | GPT-4V, Gemini, LLaVA | Process text + images |
| **Code-specialised** | CodeLlama, StarCoder, DeepSeek Coder | Trained on code |
| **Small / Efficient** | Phi-3, Gemma, TinyLlama | Strong performance at small scale |

The field is moving fast. What's cutting-edge today may be superseded in months. The fundamentals — attention, tokenisation, fine-tuning, evaluation — remain stable.
