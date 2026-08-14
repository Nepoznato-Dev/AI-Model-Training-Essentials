---
# Metadata
title: "Experiment Design"
description: "Structure reproducible ML experiments with proper baselines, ablations, statistical rigor, and clear success criteria that support confident shipping decisions."
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
tags: [experiment-design, reproducibility, ablation-study, baselines, statistical-rigor]
difficulty_level: "intermediate"
prerequisites:
  - "Basic ML concepts (loss, optimization, train/val/test)"
  - "Python scripting"
estimated_reading_time: "20 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Experiment Design

Structure ML experiments so they produce reliable, interpretable results that support confident decisions about what to build, ship, or iterate on.

## Overview

Most ML experiments fail not because the code is wrong, but because the design is flawed: no baseline, confounded variables, data leakage, or unclear success criteria. A well-designed experiment tells you *why* something works, not just *that* it works.

This skill provides a framework for designing experiments that are reproducible, interpretable, and actionable. It covers baseline selection, ablation studies, statistical comparison, and the documentation practices needed to make experiments useful beyond a single run.

The core principle: **change one variable at a time, measure what matters, and record everything.**

## Quick-Start Workflow

```
1. Define the question    → What exactly are you testing?
2. Set the baseline       → What are you comparing against?
3. Choose metrics         → What does "better" mean quantitatively?
4. Control variables      → What stays fixed across runs?
5. Run & record           → Execute with full logging
6. Analyze & conclude     → Is the difference real and meaningful?
```

## Core Competencies

- **Hypothesis Formulation**: Frame testable, specific hypotheses rather than vague "let's try X" explorations
- **Baseline Selection**: Choose meaningful comparison points — from simple rules to prompting baselines to prior state-of-the-art
- **Ablation Design**: Isolate which components contribute to performance by systematically removing them
- **Statistical Comparison**: Determine whether observed differences are real improvements or noise
- **Reproducibility**: Configure seeds, environments, and logging so any result can be recreated
- **Documentation**: Record experiments in a way that future-you (and teammates) can understand months later

## When to Use

- Comparing model architectures, training strategies, or hyperparameter choices
- Evaluating whether a new technique (LoRA, data augmentation, new loss function) actually helps
- Debugging why a model performs poorly — isolating which component is the bottleneck
- Preparing results for publication, internal review, or shipping decisions
- Building benchmark suites for ongoing model evaluation

## Framework/Methodology

### Phase 1: Define the Question

A vague question produces useless results. Transform vague goals into specific, testable hypotheses.

| Vague Goal | Specific Hypothesis |
|-----------|-------------------|
| "Make the model better" | "Adding contrastive examples to the prompt improves extraction F1 by >5% on the legal domain test set" |
| "Try a different model" | "Mistral 7B outperforms LLaMA 7B on our summarization task at equal inference cost" |
| "Improve accuracy" | "Fine-tuning with class-weighted loss improves recall on the minority class from 60% to 80% without dropping majority accuracy below 90%" |

**Hypothesis template:**
```
"We hypothesize that [CHANGE] will improve [METRIC] by [AMOUNT] on [DATASET]
compared to [BASELINE], because [REASONING]."
```

### Phase 2: Establish the Baseline

Every experiment needs a reference point. Without one, you can't tell if a result is good.

**Baseline hierarchy** (from weakest to strongest):
1. **Random / heuristic baseline** — Simplest possible approach (random guessing, keyword matching)
2. **Prompting baseline** — Best prompt-only solution before fine-tuning
3. **Prior state-of-the-art** — Published results or existing production system
4. **Upper bound** — Oracle performance (e.g., human inter-annotator agreement)

**Rule**: Always measure at least two baselines — a "floor" (trivial approach) and a "ceiling" (current best). This frames your result in context.

### Phase 3: Design the Comparison

**The golden rule: change one variable at a time.**

If you change the model AND the data AND the learning rate simultaneously, you can't attribute improvement to any specific change.

**Ablation study pattern:**

```
Full system:           A + B + C + D  →  Score: 92%
Remove A:              _ + B + C + D  →  Score: 88%  (A contributes 4%)
Remove B:              A + _ + C + D  →  Score: 85%  (B contributes 7%)
Remove C:              A + B + _ + D  →  Score: 91%  (C contributes 1%)
Remove D:              A + B + C + _  →  Score: 78%  (D contributes 14%)
```

This tells you which components matter most and where to invest optimization effort.

**When you can't change one variable** (e.g., comparing two fundamentally different architectures):
- Acknowledge the confound explicitly
- Run additional controlled experiments to isolate contributing factors
- Report the comparison honestly: "Architecture X outperforms Y, but X also uses Z, so the improvement may partially come from Z"

### Phase 4: Choose Metrics Wisely

**Metric selection checklist:**
- [ ] Primary metric aligns with business/research objective
- [ ] At least one secondary metric catches side effects
- [ ] Metrics are computed on a held-out test set not used for any decisions
- [ ] You report confidence intervals or variance across multiple seeds
- [ ] You track both offline metrics (computed on test set) and online metrics (if deployed)

**Common metric pitfalls:**

| Pitfall | Example | Fix |
|---------|---------|-----|
| Optimizing the wrong proxy | Maximizing BLEU score produces fluent but factually wrong summaries | Add BERTScore or factual consistency check |
| Ignoring class imbalance | 95% accuracy on spam detection when 95% of emails are not spam | Use F1, precision-recall curves, or balanced accuracy |
| Reporting only averages | Mean latency hides P99 tail latency that affects users | Report percentiles (P50, P95, P99) |
| Single-seed luck | One random seed gives unusually good results | Run 3–5 seeds, report mean ± std |

### Phase 5: Ensure Reproducibility

**Reproducibility checklist:**
- [ ] Random seeds set for all libraries (Python, NumPy, PyTorch, CUDA)
- [ ] Exact model version/commit recorded (not just "LLaMA 7B" — include checkpoint hash)
- [ ] Training data version pinned (hash or DVC commit)
- [ ] Hardware configuration documented (GPU type, count, driver version)
- [ ] All hyperparameters logged (not just the ones you think matter)
- [ ] Software environment captured (requirements.txt, conda env, or Docker image)

**Seed setting pattern:**
```python
import random
import numpy as np
import torch

SEED = 42

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)

# For reproducibility (may impact performance)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```

### Phase 6: Analyze and Conclude

**Statistical significance — when it matters:**
- For small improvements (<2%), run a paired t-test or bootstrap confidence interval
- For large improvements (>5%), statistical significance is usually obvious
- Always report effect size, not just p-values

**Practical significance check:**
```
Metric improvement: +3% F1
Additional compute: 4x training time
Additional complexity: New data pipeline component
Deployment impact: Requires model retraining monthly

→ Is the 3% improvement worth the operational cost?
```

**Conclusion template:**
```markdown
## Experiment Conclusion

**Question**: Does [change] improve [metric] on [task]?
**Result**: [Yes/No/Uncertain] — [metric] improved by [amount] (± [variance])
**Confidence**: [High/Medium/Low] based on [number of seeds, test set size]
**Practical significance**: [Worth deploying / Marginal / Not worth the complexity]
**Next steps**: [What to try next based on this result]
**Artifacts**: [Link to logs, model checkpoint, evaluation script]
```

## Practical Templates

### Template 1: Experiment Plan

```markdown
# Experiment: [Short Descriptive Name]

## Question
Does [change] improve [metric] on [task] compared to [baseline]?

## Hypothesis
We expect [direction and magnitude of change] because [reasoning].

## Setup
- Base model: [name, version, link]
- Dataset: [name, size, split strategy]
- Metric: [primary] + [secondary]
- Hardware: [GPU type × count]
- Estimated runtime: [hours]
- Estimated cost: [$ if cloud]

## Conditions
| Condition | Description | What Changes |
|-----------|-------------|--------------|
| Baseline | [Description] | — |
| Treatment A | [Description] | [Variable] |
| Treatment B | [Description] | [Variable] |

## Controls (kept fixed)
- Random seed: [value]
- Data preprocessing: [description or link]
- Evaluation script: [link]
- Hyperparameters (except variable): [values]

## Success Criteria
- Ship: [metric] > [threshold]
- Iterate: [metric] > [baseline] but < [threshold]
- Abandon: [metric] ≤ [baseline]
```

### Template 2: Results Log

```markdown
# Results: [Experiment Name]
Date: [YYYY-MM-DD]
Run by: [Name]

## Summary
| Condition | [Primary Metric] | [Secondary Metric] | Training Time | VRAM Peak |
|-----------|-----------------|-------------------|---------------|-----------|
| Baseline  |                 |                   |               |           |
| Treatment A |               |                   |               |           |
| Treatment B |               |                   |               |           |

## Statistical Analysis
- Test used: [paired t-test / bootstrap / Wilcoxon]
- p-value: [value]
- Confidence interval: [lower, upper]
- Effect size: [Cohen's d / raw difference]

## Observations
- [What surprised you]
- [What confirmed expectations]
- [Failure patterns noticed]

## Conclusion
[Use the conclusion template from Phase 6]

## Artifacts
- Training logs: [path/URL]
- Checkpoints: [path/URL]
- Evaluation script: [path/URL]
- Raw results: [path/URL]
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| No baseline | Can't tell if result is good or bad | Always define baseline before running experiments |
| Changing multiple variables at once | Can't attribute improvement to specific change | Change one variable per experiment |
| Evaluating on training data | Overly optimistic results, fails in production | Maintain strict held-out test set |
| Reporting only best seed | Misleading — result may not be reproducible | Run 3+ seeds, report mean ± std |
| Optimizing metric that doesn't match goals | High metric score but poor real-world performance | Align primary metric with business/research objective |
| Not recording hyperparameters | Can't reproduce or understand what worked | Log everything automatically with experiment tracker |
| Test set contamination | Inflated metrics that don't reflect reality | Hash-based deduplication, split by source/time |
| Ignoring practical significance | Statistically significant but operationally not worth it | Always weigh improvement against added complexity/cost |

## Best Practices

1. **Write the experiment plan before running anything.** Documenting the hypothesis, baseline, and success criteria upfront prevents post-hoc rationalization of results.

2. **Automate logging from day one.** Manual experiment logs get lost, forgotten, or incompletely filled. Use W&B, MLflow, or even a structured JSON log from the start.

3. **Name experiments descriptively.** `exp_001` tells you nothing. `lora-r64-legal-extraction-3ep` tells you the method, data, and duration at a glance.

4. **Run ablations early, not as an afterthought.** Understanding which components matter guides where to invest optimization effort. It's more informative than a single end-to-end result.

5. **Version your data like code.** Data changes are the most common source of irreproducible results. Pin dataset versions with hashes or DVC.

6. **Separate the "decision" test set from the "development" validation set.** Use validation for hyperparameter choices. Use test only once, at the end, for the final comparison.

7. **Report negative results.** Knowing what doesn't work is valuable — for you in 6 months and for the community. Log failed experiments with the same rigor as successful ones.

## Tools & Resources

### Experiment Tracking
- **[Weights & Biases](https://wandb.ai/)** - Industry-standard experiment tracking with rich visualization
- **[MLflow](https://mlflow.org/)** - Open-source experiment, model, and deployment tracking
- **[Neptune](https://neptune.ai/)** - Metadata store for MLOps with team collaboration
- **[DVCLive](https://github.com/iterative/dvclive)** - Lightweight tracking that integrates with Git/DVC workflows

### Statistical Analysis
- **[SciPy stats](https://docs.scipy.org/doc/scipy/reference/stats.html)** - Standard statistical tests in Python
- **[Bootstrap](https://github.com/scikit-learn/scikit-learn)** - Scikit-learn's resampling methods for confidence intervals
- **[StatModels](https://www.statsmodels.org/)** - Comprehensive statistical modeling and testing

### Reproducibility
- **[DVC](https://dvc.org/)** - Data version control that integrates with Git
- **[Docker](https://www.docker.com/)** - Container environments for exact reproducibility
- **[Conda](https://docs.conda.io/)** - Package and environment management
- **[Git LFS](https://git-lfs.github.com/)** - Version large model files and datasets

## Example Application

**Scenario**: A team wants to know whether adding synthetic data (generated by GPT-4) improves their domain-specific NER model.

**Application**:

1. **Question**: Does GPT-4-generated synthetic training data improve NER F1 on legal contracts?

2. **Baseline**: Current model trained on 5,000 human-annotated contracts → F1 = 0.84

3. **Conditions**:
   - Baseline: 5K human examples only
   - Treatment A: 5K human + 5K synthetic (GPT-4 generated)
   - Treatment B: 5K human + 10K synthetic
   - Treatment C: 5K human + 5K synthetic (filtered by confidence threshold)

4. **Controls**: Same base model, same hyperparameters, same test set, same seed.

5. **Results** (mean of 3 seeds):
   - Baseline: 0.84 (±0.01)
   - Treatment A: 0.87 (±0.01) — +3% from synthetic data
   - Treatment B: 0.86 (±0.02) — more synthetic data adds variance
   - Treatment C: 0.89 (±0.01) — filtered synthetic data is best

6. **Conclusion**: Filtered synthetic data (Treatment C) improves F1 by 5% with high confidence. The filtering step matters — unfiltered synthetic data (A) helps less, and too much unfiltered data (B) adds noise. Worth deploying.

**Outcome**: Team adopts Treatment C, gaining 5% F1 improvement with zero additional annotation cost. The ablation (A vs C) reveals that quality filtering is the key variable, leading to a new standard practice for synthetic data in the organization.

## Success Indicators

You've mastered experiment design when you can:

- Frame every ML investigation as a testable hypothesis with clear success criteria
- Automatically log all experiments without manual effort
- Design ablation studies that isolate which components drive performance
- Distinguish statistically significant from practically significant improvements
- Reproduce any past experiment from your documentation alone
- Make confident go/no-go decisions based on experimental evidence

## Related Skills

- [Model Fine-Tuning](model_fine_tuning.md) - Applying experiment design to model adaptation
- [Data Pipeline Design](data_pipeline_design.md) - Building reliable data workflows for experiments
- [Experiment Tracking](../data-skills/experiment_tracking.md) - Tooling for systematic experiment logging
- [Critical Thinking](../research-skills/critical_thinking.md) - Evaluating evidence and avoiding bias
- [Model Evaluation](../technical-skills/model_evaluation.md) - Comprehensive assessment techniques
