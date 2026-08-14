---
# Metadata
title: "Model Fine-Tuning"
description: "Adapt pre-trained models to specific tasks using full fine-tuning, LoRA, QLoRA, and other parameter-efficient methods with proper evaluation and resource management."
category: "AI Engineering Skills"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2026-08-10"
reviewed_by: "AI Engineering Skills Team"
next_review: "2027-02-10"

# Classification
tags: [fine-tuning, transfer-learning, lora, qlora, model-adaptation, parameter-efficient]
difficulty_level: "intermediate"
prerequisites:
  - "Python and PyTorch fundamentals"
  - "Basic transformer architecture knowledge"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Model Fine-Tuning

Adapt pre-trained models to downstream tasks efficiently — choosing the right strategy for your data size, hardware budget, and quality requirements.

## Overview

Fine-tuning is the process of taking a pre-trained model and adapting its weights (or a subset of them) to perform well on a specific downstream task. It is the primary technique for turning general-purpose foundation models into task-specific tools.

The landscape has evolved significantly: full fine-tuning of large models requires substantial GPU memory, which drove the development of parameter-efficient fine-tuning (PEFT) methods like LoRA and QLoRA. Understanding when to use each approach — and how to evaluate the results rigorously — is essential for practical AI engineering.

This skill covers the decision framework for selecting a fine-tuning strategy, implementing it correctly, and evaluating whether the adapted model meets production requirements.

## Quick-Start Decision Tree

```
Need to adapt a pre-trained model?
│
├─ Dataset < 1,000 examples?
│   ├─ Yes → Few-shot prompting first (skip fine-tuning)
│   │         └─ If prompting fails → LoRA with strong regularization
│   └─ No → Continue below
│
├─ Hardware: single consumer GPU (≤24GB VRAM)?
│   ├─ Yes → QLoRA (4-bit quantized + LoRA)
│   └─ No → Continue below
│
├─ Dataset 1K–50K examples?
│   ├─ Yes → LoRA (rank 16–64)
│   └─ No → Continue below
│
├─ Dataset > 50K examples AND task differs significantly from pre-training?
│   ├─ Yes → Full fine-tuning (if hardware allows)
│   └─ No → LoRA (rank 64–128)
│
└─ Need to merge multiple task adapters?
    └─ Yes → Full fine-tuning or sequential LoRA with task arithmetic
```

## Core Competencies

- **Strategy Selection**: Choose between full fine-tuning, LoRA, QLoRA, prefix tuning, and adapter methods based on data size, hardware, and task requirements
- **Data Preparation**: Format training data correctly — including prompt templates, label structures, and validation splits that reflect production distribution
- **Hyperparameter Tuning**: Set learning rate, batch size, rank (for LoRA), and training duration based on dataset characteristics rather than grid search
- **Catastrophic Forgetting Prevention**: Evaluate and mitigate capability loss in general abilities while gaining task-specific performance
- **Evaluation Rigor**: Design held-out test sets and benchmarks that measure real task quality, not just training loss
- **Resource Management**: Estimate VRAM requirements before training and optimize batch size, gradient accumulation, and quantization accordingly

## When to Use

- Adapting a foundation model (LLaMA, Mistral, BERT, etc.) to a domain-specific task
- Improving model performance on a narrow task beyond what prompting achieves
- Deploying models where inference latency or cost rules out large general-purpose models
- Building specialized classifiers, extractors, or generators for production pipelines
- Reducing model size while maintaining task performance (distillation via fine-tuning)

## Framework/Methodology

### Phase 1: Assess Whether Fine-Tuning Is Needed

Before fine-tuning, establish a baseline:

1. **Prompt engineering baseline**: Write the best prompt you can for the task. Measure performance on 50+ representative examples.
2. **Few-shot baseline**: Add 3–5 carefully chosen examples to the prompt. Re-measure.
3. **Gap analysis**: Compare baseline performance to your target. If the gap is small, prompt engineering may suffice. If the gap is large and systematic, fine-tuning is likely needed.

Common signals that fine-tuning will help:
- Consistent format violations that constraints can't fix
- Domain-specific knowledge the base model lacks
- Latency/cost requirements that rule out large models with long prompts
- Need for deterministic output structure

### Phase 2: Choose Your Strategy

| Strategy | VRAM (7B model) | Data Needed | Quality Ceiling | When to Use |
|----------|-----------------|-------------|-----------------|-------------|
| Full fine-tuning | ~56 GB | 10K+ | Highest | Maximum quality, significant task shift |
| LoRA (rank 64) | ~18 GB | 1K+ | High | Best default for most tasks |
| QLoRA (4-bit) | ~6 GB | 1K+ | High | Consumer hardware, tight VRAM |
| Prefix tuning | ~8 GB | 500+ | Medium | Very small datasets, classification |
| Adapter layers | ~12 GB | 1K+ | High | Multi-task scenarios |

**LoRA rank selection guide:**
- Rank 8–16: Simple tasks (classification, formatting, style transfer)
- Rank 32–64: Moderate tasks (summarization, Q&A, extraction)
- Rank 128–256: Complex tasks (reasoning, code generation, multi-step)

### Phase 3: Prepare Your Data

Data quality matters more than quantity for fine-tuning.

**Format template** (instruction-tuning style):
```json
{
  "instruction": "Extract all named entities from the following text.",
  "input": "Apple announced new AirPods at their Cupertino headquarters.",
  "output": "[{\"entity\": \"Apple\", \"type\": \"ORG\"}, {\"entity\": \"AirPods\", \"type\": \"PRODUCT\"}, {\"entity\": \"Cupertino\", \"type\": \"LOC\"}]"
}
```

**Data preparation checklist:**
- [ ] Remove duplicates and near-duplicates
- [ ] Validate output format consistency (every example must have correct output)
- [ ] Split 80/10/10 (train/val/test) with stratification if classification
- [ ] Ensure test set reflects production distribution, not just random split
- [ ] Check for data leakage (same source appearing in train and test)
- [ ] Balance classes or use weighted sampling if imbalanced

**Quality over quantity**: 1,000 high-quality, human-verified examples typically outperform 100,000 noisy examples. Invest time in cleaning and validating your dataset.

### Phase 4: Configure and Train

**Recommended starting hyperparameters** (LoRA):

```python
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import TrainingArguments
from trl import SFTTrainer

# LoRA configuration
lora_config = LoraConfig(
    r=64,                          # Rank — start with 64, adjust based on results
    lora_alpha=128,                # Alpha — typically 2x rank
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,            # 3–5 epochs for 1K–10K examples
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4, # Effective batch size = 16
    learning_rate=2e-4,            # LoRA can use higher LR than full fine-tuning
    lr_scheduler_type="cosine",
    warmup_ratio=0.03,
    fp16=True,
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=50,
    save_strategy="steps",
    save_steps=50,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
)
```

**Learning rate guidelines:**
- Full fine-tuning: 1e-5 to 5e-5 (lower for larger models)
- LoRA: 1e-4 to 3e-4 (higher is fine since fewer parameters)
- QLoRA: 1e-4 to 2e-4

**Training duration rules of thumb:**
- 1K examples: 3–5 epochs
- 10K examples: 2–3 epochs
- 100K+ examples: 1–2 epochs
- Watch for training loss plateau — stop when loss stabilizes for 0.5 epoch

### Phase 5: Evaluate Rigorously

**Evaluation hierarchy** (from fastest to most reliable):

1. **Automated metrics on held-out test set** — Run immediately after training
2. **Human evaluation on sample** — 50–100 examples rated by domain experts
3. **A/B comparison against baseline** — Side-by-side comparison with the prompting baseline
4. **Production shadow testing** — Run both systems in parallel, compare outputs

**Key metrics by task type:**

| Task Type | Primary Metric | Secondary Metric | Watch Out For |
|-----------|---------------|------------------|---------------|
| Classification | F1 (macro) | Accuracy | Class imbalance masking poor minority performance |
| Extraction | Exact match + F1 | Format compliance | Model generating valid JSON but wrong entities |
| Generation | ROUGE-L / BERTScore | Human preference | High ROUGE but factually incorrect |
| Summarization | BERTScore | Human coherence rating | Over-compression losing key facts |
| Code generation | Pass@k | Syntax validity | Passing tests but non-idiomatic code |

**Catastrophic forgetting check:**
Run a general-purpose benchmark (MMLU subset, HellaSwag, or your own diverse test set) before and after fine-tuning. If general capability drops more than 5%, your fine-tuning is too aggressive — reduce learning rate, rank, or epochs.

## Practical Templates

### Template 1: Fine-Tuning Experiment Plan

```markdown
## Fine-Tuning Experiment: [Task Name]

### Objective
- Task: [What the model should do]
- Target metric: [e.g., F1 > 0.90 on test set]
- Baseline: [Prompting baseline: X% / Previous model: Y%]

### Data
- Source: [Where data comes from]
- Size: [N train / N val / N test]
- Format: [instruction/input/output]
- Quality checks: [Who validated, how many reviewed]

### Strategy
- Method: [Full / LoRA / QLoRA]
- Model: [Base model name and size]
- Rank (if LoRA): [Value and rationale]
- Hardware: [GPU type and count]
- Estimated VRAM: [Calculation]

### Hyperparameters
- Learning rate: [Value]
- Epochs: [Value]
- Batch size: [Value]
- Effective batch size: [Value with gradient accumulation]

### Evaluation Plan
- Primary metric: [Metric and threshold]
- Forgetting check: [Benchmark to run]
- Human eval: [Sample size and rubric]

### Success Criteria
- Ship threshold: [Minimum acceptable performance]
- Rollback plan: [What to do if fine-tuning fails]
```

### Template 2: VRAM Estimation Calculator

```
VRAM estimate for fine-tuning:

Base model:          [e.g., 7B parameters]
Precision:           [e.g., 4-bit (QLoRA) / 16-bit (full)]
Method:              [Full / LoRA / QLoRA]

Formula:
  Model weights:     params × bytes_per_param
                     7B × 0.5 = 3.5 GB (4-bit)
                     7B × 2.0 = 14 GB (16-bit)
  
  Gradients:         trainable_params × 4 bytes
                     ~100M × 4 = 0.4 GB (LoRA)
                     7B × 4 = 28 GB (full)
  
  Optimizer state:   trainable_params × 8 bytes (Adam)
                     ~100M × 8 = 0.8 GB (LoRA)
                     7B × 8 = 56 GB (full)
  
  Activations:       ~2–4 GB (depends on batch size and sequence length)

Total estimate:      [Sum of above]
Recommended GPU:     [Based on total + 20% headroom]
```

### Template 3: Fine-Tuning Results Report

```markdown
## Fine-Tuning Results: [Experiment Name]

### Configuration
- Method: [LoRA rank=64]
- Training time: [X hours on Y GPU]
- Total cost: [$X if cloud]

### Performance Comparison
| Metric | Baseline (prompting) | Fine-tuned | Delta |
|--------|---------------------|------------|-------|
| [Primary metric] | | | |
| [Secondary metric] | | | |
| Inference latency | | | |
| Model size | | | |

### Forgetting Check
| Benchmark | Before | After | Delta |
|-----------|--------|-------|-------|
| [General benchmark] | | | |

### Failure Analysis
- Worst-performing category: [Which type of input fails]
- Error pattern: [What the failures have in common]
- Recommended next step: [More data / Different rank / Different approach]
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Fine-tuning when prompting would work | Wasted compute, maintenance burden of custom model | Always establish prompting baseline first |
| Training too many epochs | Overfitting, especially on small datasets | Use early stopping with validation loss monitoring |
| Ignoring data quality | Model learns noise or incorrect patterns | Invest 70% of effort in data cleaning, 30% in training |
| Not checking for catastrophic forgetting | Model becomes narrow specialist, loses general ability | Run general benchmarks before and after fine-tuning |
| Using the same test set for hyperparameter tuning | Overfitting to test set, unreliable estimates | Keep a completely held-out test set never used during development |
| Training on leaked data | Inflated metrics that don't reflect real performance | Deduplicate across train/val/test splits by source, not just exact match |
| Skipping the prompting baseline | No way to measure if fine-tuning actually helped | Always measure prompting performance first — it's free |
| Using learning rate too high (full fine-tuning) | Training instability, loss spikes | Start at 2e-5 for full fine-tuning; LoRA can tolerate 2e-4 |

## Best Practices

1. **Always establish a prompting baseline first.** If prompting gets you 80% of the way, fine-tuning may not be worth the added complexity of maintaining a custom model.

2. **Start with LoRA before full fine-tuning.** LoRA is faster, cheaper, and often matches full fine-tuning quality. Only move to full fine-tuning when LoRA plateaus.

3. **Invest in data quality over quantity.** 1,000 verified examples beat 50,000 noisy ones. Have humans review a random sample of your training data before training.

4. **Use cosine learning rate schedule with warmup.** This is the most robust schedule across tasks. Warmup for 3% of total steps, then cosine decay.

5. **Monitor validation loss, not training loss.** Training loss will always decrease. Validation loss tells you when you're overfitting. Set up early stopping.

6. **Version your data alongside your code.** A fine-tuned model is inseparable from its training data. Track both with DVC or similar tools.

7. **Test on production-distribution data, not convenient data.** Random splits often create distribution mismatch between test set and real inputs. Split by source, time, or domain instead.

8. **Keep the base model accessible.** With LoRA, you only store the delta weights. You still need the base model for inference — plan storage and loading accordingly.

## Tools & Resources

### Fine-Tuning Frameworks
- **[Hugging Face TRL](https://github.com/huggingface/trl)** - Purpose-built for LLM fine-tuning with SFTTrainer and DPOTrainer
- **[PEFT](https://github.com/huggingface/peft)** - Parameter-efficient fine-tuning (LoRA, prefix tuning, adapters)
- **[Unsloth](https://github.com/unslothai/unsloth)** - 2x faster LoRA training with reduced VRAM usage
- **[Axolotl](https://github.com/axolotl-ai-cloud/axolotl)** - Streamlined fine-tuning with YAML configuration
- **[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)** - Unified fine-tuning framework with web UI

### Data Preparation
- **[Datatrove](https://github.com/huggingface/datatrove)** - Large-scale data processing pipeline
- **[deduplicate-text-datasets](https://github.com/google-research/deduplicate-text-datasets)** - Exact and fuzzy deduplication
- **[Argilla](https://github.com/argilla-io/argilla)** - Human-in-the-loop data annotation and review

### Evaluation
- **[LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)** - Standardized evaluation across 60+ academic benchmarks
- **[OpenAI Evals](https://github.com/openai/evals)** - Evaluation framework with community-contributed test suites
- **[DeepEval](https://github.com/confident-ai/deepeval)** - LLM evaluation framework for RAG and conversational agents

### Experiment Tracking
- **[Weights & Biases](https://wandb.ai/)** - Experiment tracking with hyperparameter sweep support
- **[MLflow](https://mlflow.org/)** - Open-source experiment and model registry
- **[DVCLive](https://github.com/iterative/dvclive)** - Lightweight experiment tracking that integrates with DVC

## Example Application

**Scenario**: A legal tech startup needs a model that extracts contract clauses (parties, obligations, termination conditions, liability caps) from legal agreements. The base model (Mistral 7B) can do this with prompting but produces inconsistent JSON and misses subtle clauses.

**Application**:

1. **Baseline measurement**: Prompt engineering achieves 72% exact-match extraction on 100 test contracts. Main failure modes: missing implicit obligations (30% of failures) and malformed JSON (15%).

2. **Data preparation**: Annotate 2,000 contracts with human-reviewed clause extractions. Split by contract type (not randomly) to ensure test set covers all categories. Deduplicate by source law firm.

3. **Strategy selection**: 2,000 examples + single 24GB GPU → QLoRA with rank 64. Estimated VRAM: 5.5 GB for model + 2 GB for training = 7.5 GB total.

4. **Training**: 3 epochs, learning rate 2e-4, effective batch size 16. Validation loss plateaus at epoch 2.5 — best checkpoint selected at epoch 2.

5. **Results**: Exact-match extraction improves to 91%. JSON format compliance reaches 99.5%. General benchmark (MMLU subset) drops by 1.2% — acceptable. Inference latency decreases 40% because shorter prompts are now needed.

**Outcome**: The fine-tuned model replaces the prompting pipeline, reducing per-contract processing cost by 60% and eliminating the JSON parsing failures that caused downstream system errors.

## Success Indicators

You've mastered model fine-tuning when you can:

- Correctly estimate VRAM requirements before starting training
- Choose between LoRA, QLoRA, and full fine-tuning with clear justification
- Prepare training data that reflects production distribution
- Identify when fine-tuning is the wrong tool (prompting would suffice)
- Design evaluation that catches catastrophic forgetting
- Achieve consistent quality improvements over prompting baselines
- Version and reproduce fine-tuning experiments end-to-end

## Related Skills

- [Experiment Design](experiment_design.md) - Structuring rigorous ML experiments
- [Data Pipeline Design](data_pipeline_design.md) - Building reliable data workflows
- [Model Evaluation](../technical-skills/model_evaluation.md) - Comprehensive model assessment techniques
- [Experiment Tracking](../data-skills/experiment_tracking.md) - Logging and comparing experiments
- Performance Optimization - Speeding up inference and training
