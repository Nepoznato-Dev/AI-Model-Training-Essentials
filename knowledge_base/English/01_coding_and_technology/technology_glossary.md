---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Technology Glossary

A reference glossary covering AI models, hardware, benchmarks, and core concepts
in the modern AI and computing landscape.

---

## AI Language Models and Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released in November 2022.
It is powered by the GPT series of large language models (LLMs). ChatGPT is one
of the fastest-growing consumer AI products in history, reaching 100 million
users within two months of launch. It supports text-based conversation, code
generation, summarisation, and creative writing. Paid tiers provide access to
more powerful models such as GPT-4 and GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family of large language models created by OpenAI. The architecture
uses a decoder-only Transformer trained with a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
for "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via the API), GPT-3.5 (the backbone of the original ChatGPT), and GPT-4
(2023, multimodal, performance close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, the founder of information theory. Anthropic was founded by former
OpenAI researchers and focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set of principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known for long context windows (up
to 200,000 tokens), nuanced reasoning, and reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family of multimodal AI models, announced in
December 2023. Gemini is natively multimodal — trained from the ground up on
text, images, audio, and video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), and Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) and Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small language model (SLM) developed by Microsoft with 3.8B
parameters. It was released in April 2026. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises data quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU and
HumanEval. It supports a 4k token context window in its base variant and a 128k
window in the long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone with sufficient RAM.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) is an open-weights family of models
released by Meta. Llama 2 (2023) was released for research and commercial use
with sizes ranging from 7B to 70B parameters. Llama 3 (2026) improved
performance significantly, with models ranging from 8B to 70B (and later 400B+).
Because the weights are publicly downloadable, Llama models are the foundation
for a large ecosystem of fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
and are widely used for local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open and proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match the
performance of much larger models using efficient techniques such as sliding
window attention and grouped-query attention. Mixtral 8x7B (2026) is a mixture-
of-experts model — it routes each token to a subset of 8 expert networks,
achieving GPT-3.5-level performance while being computationally cheaper.
Mistral's models are fully open-weight and can be run locally.

---

## GPU Hardware and Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed for massively parallel computation. Originally
built for rendering 3D graphics, GPUs have become essential for AI/ML training
and inference because they can perform thousands of floating-point operations
simultaneously using thousands of small cores. The two main GPU manufacturers
for AI are NVIDIA and AMD.

### NVIDIA GeForce RTX Series
The RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) and RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores for accelerating AI operations. VRAM (video RAM) is
critical for running AI models locally — an 8GB GPU can handle 7B parameter
models in 4-bit quantisation; a 24GB GPU can handle 70B models in 4-bit.

### NVIDIA A-Series and H-Series (Data Centre)
The A100 (Ampere, 2020) and H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB of HBM3 memory and is the standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× the AI throughput of consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. The RX 7900 XTX (2022) has 24GB VRAM and can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA for AI frameworks, though support is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting in 2022. Arc
GPUs support XeSS (Intel's super-sampling) and have limited but growing support
for AI inference tasks via OpenVINO and IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications database at ark.intel.com. It
provides detailed technical specifications for every Intel CPU, GPU, FPGA, and
NUC product, including core counts, clock speeds, TDP, supported memory types,
and instruction-set features. When you hear "check ARK for specs," it means
visiting that database for authoritative hardware information.

---

## AI Performance Benchmarks

### MMLU (Massive Multitask Language Understanding)
MMLU is a benchmark testing LLM knowledge across 57 academic subjects including
mathematics, history, law, medicine, and computer science. It consists of
multiple-choice questions drawn from real university-level exams. A score of
70% is roughly human undergraduate level; GPT-4 and Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark for code generation. It consists of 164 Python
programming problems with automated test cases. Models are measured on
pass@k — the probability that at least one of k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity and must choose the most likely continuation from
four options. The incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding of physical
and social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from the Allen Institute for AI. It consists of grade-school
science questions, split into "Easy" and "Challenge" sets. The Challenge set
contains questions that retrieval-based methods and simple statistical models
struggle with, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
database) with a language model. Instead of relying solely on the model's
parametric knowledge, RAG first retrieves relevant documents from an external
knowledge base and then includes them in the model's context. This allows the
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form of RAG — it retrieves from its KB
and includes the results in the context before generating a response.

### Fine-tuning
Fine-tuning is the process of continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts the model's weights for a
particular task or domain. For example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces the numerical precision of model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
in 16-bit precision requires ~14GB VRAM; the same model in 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation and is the main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
The context window is the maximum number of tokens a model can process at once,
including both the prompt and the generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo and Claude 3 support 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows the model to "see"
more of a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF is the training technique that transforms a base language model (which
simply predicts the next token) into an assistant that follows instructions and
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, and the language model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, and Gemini all use
variants of RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer Architecture
The Transformer is the neural network architecture underlying all modern LLMs.
Introduced in the 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens in parallel rather than
sequentially. Encoder-only Transformers (BERT) are used for understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used for generation tasks;
encoder-decoder Transformers (T5, BART) are used for translation and summarisation.

### Embeddings and Vector Databases
Embeddings are dense numerical representations of text (or images) produced by
a neural network. Semantically similar texts have embeddings that are close in
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings and support fast approximate nearest-neighbour search. They are
the storage backbone of RAG systems, including Potato.ai's cold-memory layer.
