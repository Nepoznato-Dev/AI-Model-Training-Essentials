<!--
---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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

-->
# Model Optimisation and Deployment

Training a large AI model is a significant achievement, but deploying it efficiently is where most of the engineering effort is required. A model that takes 10 seconds to respond or requires eight A100 GPUs is impractical for most real-world applications. Model optimisation is the process of making models smaller, faster, and more cost-effective — while maintaining acceptable quality. This file covers quantisation, pruning, distillation, and the practical tools for deploying models in production.

---

## Why Optimise?

| Concern | Impact |
|---------|--------|
| **Latency** | Users expect responses in under 1 second; every extra 100ms loses engagement |
| **Cost** | GPU inference is expensive; a 70B model costs ~$0.05-0.15 per 1M tokens on cloud hardware |
| **Memory** | A 7B model in FP32 needs 28 GB of VRAM; most consumer GPUs have 8-24 GB |
| **Energy** | Running large models consumes significant electricity; matters for mobile and edge |
| **Scale** | Serving millions of users requires models that fit on available hardware |

---

## Quantisation

Quantisation reduces the precision of model weights from 32-bit floating point (FP32) to smaller formats like INT8, INT4, or even lower.

### Precision Formats

| Format | Bits per Weight | Memory for 7B Model | Quality |
|--------|----------------|--------------------|---------|
| **FP32** | 32 | 28 GB | Baseline (full precision) |
| **FP16 / BF16** | 16 | 14 GB | Nearly identical to FP32 |
| **INT8** | 8 | 7 GB | Very small quality loss |
| **INT4** | 4 | 3.5 GB | Moderate quality loss; still usable |
| **INT3 / INT2** | 3-2 | 2.6-1.75 GB | Significant quality loss; research stage |

### Quantisation Methods

| Method | When It Happens | How It Works | Quality |
|--------|----------------|--------------|---------|
| **Post-Training Quantisation (PTQ)** | After training is complete | Calibrate the model on a small dataset; find optimal scales | Good for INT8; degrades at INT4 |
| **GPTQ** | After training | GPU-friendly INT4 quantisation using approximate second-order information | Good quality at INT4 |
| **AWQ** (Activation-aware Weight Quantisation) | After training | Protect salient weights based on activation magnitudes | Better than GPTQ at INT4 |
| **GGUF** (llama.cpp format) | After training | CPU-friendly quantisation; mixed precision per layer | Optimised for CPU inference |
| **Quantisation-Aware Training (QAT)** | During training | Simulate quantisation during training so the model learns to cope | Best quality; requires retraining |

### Practical Impact

| Model | FP16 Size | INT4 Size | Speedup | Quality Loss |
|-------|-----------|-----------|---------|-------------|
| **LLaMA 7B** | 14 GB | 3.5 GB | 2-4x | ~1-2% on benchmarks |
| **LLaMA 70B** | 140 GB | 35 GB | 2-3x | ~2-3% on benchmarks |

---

## Pruning

Pruning removes unnecessary weights or neurons from a trained model.

| Type | Description | Advantage | Challenge |
|------|-------------|-----------|-----------|
| **Unstructured** | Remove individual weights (set to zero) | Highest compression ratios | Requires sparse hardware support |
| **Structured** | Remove entire neurons, attention heads, or layers | Directly reduces model size | May lose more quality |
| **Magnitude-based** | Remove weights with smallest absolute values | Simple; works well | May miss important small weights |
| **Importance-based** | Remove weights based on their contribution to output | Better quality preservation | More expensive to compute |

### Pruning Pipeline

| Step | Description |
|------|-------------|
| 1. Train | Train the full model normally |
| 2. Score | Compute importance scores for each weight/neuron |
| 3. Prune | Remove the least important elements |
| 4. Fine-tune | Re-train to recover lost accuracy |
| 5. Repeat | Iterate pruning and fine-tuning for higher compression |

---

## Knowledge Distillation

Training a small "student" model to mimic a large "teacher" model.

| Component | Role |
|-----------|------|
| **Teacher** | Large, high-quality model |
| **Student** | Small model that learns from the teacher |
| **Distillation loss** | Student tries to match the teacher's output distribution (soft labels) |

### Types of Distillation

| Type | Description | Example |
|------|-------------|---------|
| **Logit-based** | Student matches teacher's output probabilities | Hinton's original distillation |
| **Feature-based** | Student matches teacher's intermediate representations | FitNets |
| **Relation-based** | Student matches relationships between samples | RKD (Relational Knowledge Distillation) |
| **Data-free** | No original training data needed; use teacher's generation | DAFL, DeepInversion |

### Notable Distillation Examples

| Teacher | Student | Result |
|---------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (rumoured) | Smaller model with much of GPT-4's quality |
| **BERT-Large** | DistilBERT | 40% smaller, 60% faster, 97% of BERT's performance |
| **LLaMA 70B** | LLaMA 7B (via distillation) | Open-source small model approaching large model quality |

---

## LLM-Specific Optimisations

### KV-Cache Optimisation

Large language models cache key-value pairs from previous tokens to avoid recomputation.

| Technique | Description | Impact |
|-----------|-------------|--------|
| **Multi-Query Attention (MQA)** | All attention heads share one KV pair | Reduces memory; slight quality loss |
| **Grouped-Query Attention (GQA)** | Groups of heads share KV pairs | Balance between MQA and standard attention |
| **Sliding window attention** | Only attend to the last W tokens | Reduces KV-cache size for long contexts |

### Speculative Decoding

| Step | Description |
|------|-------------|
| 1 | A small "draft" model generates K tokens quickly |
| 2 | The large model verifies all K tokens in one forward pass |
| 3 | Accepted tokens are kept; rejected ones are regenerated |

Result: 2-3x speedup in generation with no quality loss (the large model always has final say).

### Flash Attention

| Feature | Description |
|---------|-------------|
| **Problem** | Standard attention requires O(n²) memory for the attention matrix |
| **Solution** | Compute attention in blocks; never materialise the full matrix in memory |
| **Result** | 2-4x faster; enables much longer context windows |
| **Variants** | Flash Attention 2 (faster), FlashDecoding (optimised for inference) |

---

## Serving Frameworks

| Framework | Best For | Key Feature |
|-----------|----------|-------------|
| **vLLM** | LLM serving | PagedAttention; continuous batching; high throughput |
| **TensorRT-LLM** | NVIDIA GPU inference | Maximum performance on NVIDIA hardware |
| **llama.cpp** | CPU and consumer GPU inference | Runs quantised models on laptops and phones |
| **Ollama** | Local model running | User-friendly wrapper around llama.cpp |
| **Triton Inference Server** | Multi-framework serving | Supports TensorFlow, PyTorch, ONNX, TensorRT |
| **TorchServe** | PyTorch model serving | Native PyTorch integration |
| **ONNX Runtime** | Cross-platform inference | Optimised execution across hardware |
| **BentoML** | Production deployment | Framework-agnostic; handles packaging and serving |

---

## Deployment Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Edge deployment** | Run models on phones, IoT devices, or embedded hardware | Low latency; offline; privacy |
| **Cloud API** | Host models on cloud GPUs; serve via API | Maximum compute; pay per use |
| **Hybrid** | Small model on device; large model in cloud | Best of both worlds |
| **Serverless** | Scale to zero; pay only when used | Sporadic traffic; cost-sensitive |
| **Batch inference** | Process data in bulk on a schedule | When real-time isn't needed |

---

## Benchmarking

| Metric | What It Measures |
|--------|-----------------|
| **Tokens per second** | Generation throughput (higher is better) |
| **Time to first token (TTFT)** | Latency before the first output token appears |
| **Latency per request** | Total time from input to complete output |
| **Memory usage** | VRAM or RAM consumed during inference |
| **Throughput** | Requests served per second |
| **Cost per 1M tokens** | Dollar cost of processing 1 million tokens |

---

## Practical Tips

- **Start with quantisation.** INT4 quantisation (AWQ or GPTQ) gives the best quality-to-size trade-off. Most 7B models run comfortably on a single consumer GPU at INT4.
- **Use vLLM for LLM serving.** It's the fastest open-source option for high-throughput LLM inference.
- **Profile before optimising.** Measure where the time is actually spent. It's often memory bandwidth, not compute, that's the bottleneck.
- **Match the model to the task.** A 7B model is fine for most tasks. Don't use 70B when 7B will do.
- **Consider distillation.** If you need a small, fast model for production, distil from a larger model rather than training from scratch.
- **Monitor continuously.** Model performance can degrade over time as data distributions shift. Track latency, throughput, and quality metrics.

---

## Summary

Model optimisation is the bridge between research and production. Quantisation shrinks models by 4-8x with minimal quality loss. Pruning removes dead weight. Distillation transfers knowledge from large to small models. Flash Attention and KV-cache tricks make inference faster. Together, these techniques turn a model that requires a data centre into one that runs on a laptop or phone. The field is moving fast — what required eight A100s last year runs on a consumer GPU today.
