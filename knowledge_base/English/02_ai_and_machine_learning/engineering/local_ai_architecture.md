---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.1"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Local AI Architecture

A practical guide to running large language models entirely on-device — hardware considerations, inference engines, memory optimisation, and system design for edge deployment.

---

## Why Run AI Locally?

- **Privacy**: No data leaves the device.
- **Cost**: No API fees per token.
- **Latency**: Predictable, network-free inference.
- **Offline availability**: Works without internet.
- **Control**: Full control over model version, customisation, and fine-tuning.

---

## Hardware Requirements

### GPU Memory (VRAM)
The most critical resource. Model size in memory ≈ **parameters × bytes per parameter**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Practical guidelines:**
- 8GB VRAM → up to 7B models at 4-bit.
- 12GB VRAM → up to 13B models at 4-bit.
- 24GB VRAM → up to 70B models at 4-bit (or 13B at 8-bit).
- Apple Silicon (unified memory) can run 70B models on 64GB+ systems.

### RAM (System Memory)
- For CPU inference, you need enough system RAM to load the model (similar to VRAM numbers).
- For GPU inference, system RAM matters for loading the model into memory before offloading to VRAM.

### Storage
- Quantised model weights take up a few GB (e.g., 4-bit 7B ≈ 4 GB on disk). Ensure at least 20–50 GB free for multiple models.

### CPU
- For prompt processing (prefill) and CPU-offloading, a modern multi-core CPU helps.
- Apple M-series chips have excellent performance for LLMs due to the unified memory and Neural Engine.

---

## Quantisation

Quantisation reduces the numerical precision of weights, dramatically cutting memory and increasing speed at a small accuracy cost.

### Popular Formats

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp format, optimised for CPU/GPU hybrid | Best for local inference |
| **GPTQ** | 4–8 | GPU-only, efficient on CUDA | Best for NVIDIA GPUs |
| **AWQ** | 4 | Activation-aware, GPU-only | Good for batch inference on GPUs |
| **ONNX** | variable | Standardised, cross-platform | Production serving |

### Choosing a Quantisation Level
- **Q8_0** (8-bit): minimal quality loss, largest size.
- **Q6_K** (6-bit): good quality, decent compression.
- **Q5_K_M** (5-bit): common sweet spot.
- **Q4_K_M** (4-bit): smallest, acceptable quality for most tasks.
- **IQ4_XS** / **IQ3_XS**: Improved quantisation with better perplexity at 4/3 bits.

**Rule of thumb:** Use Q4_K_M for a good balance of quality and size. If you have extra VRAM, use Q5 or Q6.

---

## Inference Engines (Local)

### llama.cpp
- Written in C++.
- Supports GGUF format.
- Optimised for CPU and GPU (via CUDA, Metal, OpenCL).
- Very fast, especially on CPU.
- Command-line, server mode, and Python bindings.

**Example command:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Wraps llama.cpp with a simple CLI and REST API.
- Auto-downloads models, manages them.
- Great for prototyping and desktop apps.
- Supports custom Modelfiles for system prompts.

```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Graphical desktop app for Windows, macOS, Linux.
- One-click download and chat interface.
- Built-in local server with OpenAI-compatible API.
- Good for non-technical users and quick testing.

### Hugging Face Transformers + bitsandbytes
- The standard Python library for HF models.
- Use `bitsandbytes` for 4-bit quantisation (`load_in_4bit=True`).
- More flexible for fine-tuning but slower than llama.cpp for inference.

### ExLlamaV2
- Very fast GPU inference for GPTQ and AWQ.
- Best performance on NVIDIA GPUs.
- Supports batched generation.

### mlx (Apple)
- Apple's framework for M-series chips.
- Highly optimised for Apple Silicon.
- Python API.

---

## Memory Management

### Context Window and KV Cache
The KV cache stores key-value pairs for every layer and every token in the context. It grows linearly with context length.

Memory cost ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

For a 32-layer model with 8 KV heads and 128 head dim, each token costs ~32 × 8 × 128 × 2 bytes = 65 KB per token. For 128k tokens, that's ~8 GB just for the cache.

### Offloading Strategies
- **Layer offloading**: Put some layers on GPU, others on CPU. Faster than pure CPU, lower VRAM requirement.
- **Token streaming**: Process tokens incrementally rather than all at once.

### Prompt Caching
Reuse KV caches across similar prompts to avoid recomputing the prefill phase. Some frameworks support this (e.g., vLLM, llama.cpp with `--prompt-cache`).

### Memory-Mapped Files
Load model weights directly from disk without loading them entirely into RAM (useful for huge models on memory-limited systems). llama.cpp uses memory-mapping by default.

---

## Deployment Architectures

### Single-Device Mode
One model runs on one machine (laptop, smartphone, edge device). Used for personal assistants, note-taking apps, code completion.

### Hybrid Edge-Cloud
Local model handles common queries; fallback to a cloud model for complex questions. This gives the best of both worlds — speed/private for most, capability for edge cases.

### Distributed Inference (Multi-GPU)
For larger models, split layers across multiple GPUs (tensor parallelism) or split context across devices (pipeline parallelism). Use llama.cpp with `-ngl` or ExLlamaV2 with `--num-gpu-layers`.

### Mobile Deployment
- **Android**: Use llama.cpp via JNI bindings or ML Kit.
- **iOS**: Use llama.cpp via Swift bindings or mlx.
- **Web**: Use WebLLM (runs on WebGPU via ONNX runtime) or transformers.js.

---

## Performance Optimisation

### Flash Attention
Speeds up attention computation and reduces memory usage. Available in llama.cpp, ExLlamaV2, and modern transformers libraries.

### Batch Inference
Process multiple prompts in a single forward pass. Increases throughput dramatically. Use `llama-batch` or vLLM.

### Early Stopping / Token Budgeting
Set a maximum token budget to prevent unbounded generation.

### Speculative Decoding
Use a small fast model (draft) to predict tokens, then verify with the large model in parallel. Can yield 2–3× speedup.

---

## Practical Setup Guide

### 1. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Pull a Model

```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Run with API

```bash
ollama serve
```

Then send requests to `http://localhost:11434/api/generate`.

### 4. Python Integration

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternative) Use llama.cpp directly

```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Monitoring and Observability

- Track GPU utilisation (`nvidia-smi` on Linux, Activity Monitor on macOS).
- Track memory usage (RAM and VRAM).
- Track tokens per second (throughput).
- Track time to first token (latency).
- Use built-in logging from llama.cpp or Ollama.

---

## Limitations and Tradeoffs

- **Quality gap**: Small local models (3.8B–7B) generally underperform large cloud models (GPT-4, Claude 3.5) on complex reasoning.
- **Knowledge cutoff**: Model knowledge is frozen at training time; use RAG to inject current information.
- **Multilingual**: Smaller models may have less multilingual capability.
- **Tool use**: Agentic workflows (function calling) may be less reliable on small models.

For many everyday tasks (summarisation, Q&A, code completion, classification), local models are already sufficient and improving rapidly.
