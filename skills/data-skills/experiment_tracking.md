---
# Metadata
title: "Experiment Tracking"
description: "Systematically logging, organizing, and comparing machine learning experiments to enable reproducibility, collaboration, and informed model selection."
category: "Data Skills"
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
reviewed_by: "Data Skills Team"
next_review: "2027-02-10"

# Classification
tags: [experiment-tracking, mlflow, reproducibility, hyperparameter-tuning, model-registry, wandb]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Experiment Tracking

The practice of systematically logging machine learning experiments — including code versions, data versions, hyperparameters, metrics, and artifacts — so that any result can be reproduced, compared, and audited.

## Overview

Machine learning experimentation is inherently iterative. A data scientist may run dozens of experiments in a week, each with different hyperparameters, data subsets, model architectures, or preprocessing steps. Without systematic tracking, these experiments become a jumble of notebook outputs, forgotten terminal commands, and vague recollections of "what worked."

Experiment tracking solves this by treating each training run as a first-class artifact: a reproducible record that captures everything needed to understand, compare, and recreate it. This transforms ML development from artisanal craft into an auditable engineering discipline.

Beyond personal productivity, experiment tracking enables team collaboration (multiple people can see what has been tried), model governance (auditors can trace which model was deployed and why), and continuous improvement (past experiments inform future decisions).

## Core Competencies

- Setting up an experiment tracking system and integrating it into training workflows
- Logging hyperparameters, metrics, code versions, and data versions consistently
- Comparing experiments across runs to identify what drives performance changes
- Organizing experiments into meaningful projects, tags, and hierarchies
- Registering and versioning model artifacts alongside their evaluation metrics
- Building reproducible experiment pipelines that teammates can follow
- Querying and visualizing experiment history to inform decisions

## When to Use

- Starting any new ML project with more than a handful of experiments planned
- Working on a team where multiple people run experiments on the same problem
- Preparing models for production deployment and needing to justify model selection
- Debugging why a previous experiment produced a certain result
- Onboarding new team members who need to understand what has been tried
- Establishing reproducibility requirements for compliance or governance

## Framework/Methodology

### Phase 1: System Setup

Choose a tracking tool based on your needs:

| Tool | Best For | Key Feature | Hosting |
|------|----------|-------------|---------|
| MLflow | Open-source teams, model registry | Full lifecycle tracking, model registry | Self-hosted |
| Weights & Biases | Deep learning, rich visualizations | Interactive dashboards, hyperparameter sweeps | Cloud or self-hosted |
| Neptune | Enterprise teams, metadata-heavy | Flexible metadata, team collaboration | Cloud |
| TensorBoard | TensorFlow users, quick local viz | Real-time training curves, zero setup | Local |
| DVC | Data/model versioning focus | Git-like versioning for large artifacts | Self-hosted |
| Comet ML | End-to-end ML platform | Auto-logging, production monitoring | Cloud |

**Minimum viable setup** — If you're unsure, start with MLflow's local tracking. It requires no server, stores everything in a local directory, and can be upgraded to a remote server later.

### Phase 2: What to Log

Every experiment run should capture at minimum:

| Category | What to Log | Why |
|----------|-------------|-----|
| **Parameters** | All hyperparameters, learning rate, batch size, optimizer, epochs | Reproduce the run; understand what drives performance |
| **Metrics** | Loss (per epoch), evaluation metrics (accuracy, F1, etc.), training time | Compare runs; detect overfitting; track convergence |
| **Code version** | Git commit hash, branch name, uncommitted changes flag | Know exactly which code produced the result |
| **Data version** | Dataset hash, schema version, train/val/test split seed | Data changes are the most common source of "mystery" performance shifts |
| **Artifacts** | Model weights, config files, preprocessing pipelines | Deploy or analyze the exact model that was trained |
| **Tags** | Project name, experiment type, author, status | Organize and filter runs across projects |
| **Notes** | Free-text description of what this run tests | Future-you will not remember why you ran this |

### Phase 3: Integration Pattern

Integrate tracking into training code with minimal friction:

```python
# Pattern: Initialize tracking at the start, log at natural checkpoints
import mlflow

def train(config):
    # Start run with all parameters logged automatically
    mlflow.log_params(vars(config))
    mlflow.set_tag("git_commit", get_git_hash())
    mlflow.set_tag("data_version", config.data_version)
    
    model = build_model(config)
    
    for epoch in range(config.epochs):
        train_loss = train_epoch(model, train_loader)
        val_loss, val_metrics = evaluate(model, val_loader)
        
        # Log per-epoch metrics
        mlflow.log_metrics({
            "train_loss": train_loss,
            "val_loss": val_loss,
            "val_accuracy": val_metrics["accuracy"],
            "val_f1": val_metrics["f1"],
        }, step=epoch)
    
    # Log final model artifact
    mlflow.sklearn.log_model(model, "model")
    
    return model
```

### Phase 4: Comparison & Analysis

Once experiments are tracked, use the tracking system to:

1. **Filter** — Find all runs above a metric threshold (e.g., F1 > 0.90)
2. **Sort** — Rank runs by the metric that matters for your use case
3. **Compare** — Select two runs and diff their parameters to identify what changed
4. **Visualize** — Plot metric curves across runs to see convergence patterns
5. **Search** — Query runs by tag, parameter range, or metric range

### Phase 5: Model Registry

After identifying the best experiment, promote it to a model registry:

1. **Register** the model artifact with a name and version
2. **Stage** it through environments: `Staging` → `Production` → `Archived`
3. **Document** the model card: what it does, its limitations, evaluation results
4. **Link** the registry entry back to the experiment run for full traceability

## Practical Templates

### Template 1: MLflow Quickstart Configuration

```python
# experiment_setup.py
import mlflow
import os

def setup_experiment(project_name, experiment_name):
    """Initialize a reproducible experiment tracking setup."""
    # Set tracking URI (local or remote)
    mlflow.set_tracking_uri(os.getenv("MLFLOW_URI", "./mlruns"))
    
    # Create or get experiment
    mlflow.set_experiment(experiment_name)
    
    # Start run with automatic tags
    run = mlflow.start_run(run_name=f"{experiment_name}_baseline")
    mlflow.set_tag("project", project_name)
    mlflow.set_tag("author", os.getenv("USER", "unknown"))
    
    return run

def log_config(config_dict):
    """Log a configuration dictionary as parameters."""
    # Flatten nested dicts for MLflow compatibility
    flat = {}
    for key, value in config_dict.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                flat[f"{key}.{subkey}"] = subvalue
        else:
            flat[key] = value
    mlflow.log_params(flat)
```

### Template 2: Experiment Comparison Query

```python
# compare_experiments.py
import mlflow
import pandas as pd

def compare_runs(experiment_name, metric="val_f1", min_threshold=0.85):
    """Find and compare all runs above a metric threshold."""
    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name(experiment_name)
    
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        filter_string=f"metrics.{metric} > {min_threshold}",
        order_by=[f"metrics.{metric} DESC"],
        max_results=20,
    )
    
    rows = []
    for run in runs:
        rows.append({
            "run_id": run.info.run_id[:8],
            "run_name": run.info.run_name,
            "status": run.info.status,
            metric: run.data.metrics.get(metric),
            "learning_rate": run.data.params.get("learning_rate"),
            "batch_size": run.data.params.get("batch_size"),
            "epochs": run.data.params.get("epochs"),
            "created": run.info.start_time,
        })
    
    df = pd.DataFrame(rows)
    print(f"Found {len(df)} runs with {metric} > {min_threshold}\n")
    print(df.to_string(index=False))
    return df
```

### Template 3: Experiment Naming Convention

```
Project: [domain]-[task]
  Example: "fraud-detection", "sentiment-classification"

Experiment: [architecture]-[variant]-[description]
  Example: "bert-base-finetune-lr-sweep", "resnet50-augmentation-heavy"

Run name: [date]-[key-differentiator]
  Example: "2026-08-10-lr1e-4", "2026-08-10-augmentation-heavy"

Tags:
  - status: exploratory | candidate | production | archived
  - author: [team-member]
  - data-version: [dataset-hash-or-version]
  - priority: high | normal | low
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Tracking only metrics, not parameters | Cannot reproduce or understand what made a run succeed | Always log all hyperparameters alongside metrics |
| Not logging data version | Cannot explain why performance changed between runs | Hash your dataset and log the hash with every run |
| Using experiment tracking as a graveyard of unnamed runs | Cannot find relevant runs later | Use descriptive run names and consistent tags |
| Logging too many intermediate metrics | Storage bloat, slow dashboards | Log per-epoch at most; use sampling for per-step metrics |
| Not integrating tracking into training code | People forget to log manually; inconsistent records | Make tracking a mandatory wrapper around the training function |
| Comparing runs with different data splits | Apples-to-oranges comparison that misleads | Fix the random seed and split strategy; log the seed |

## Best Practices

1. **Make tracking frictionless.** If logging requires extra manual steps, people will skip it. Wrap tracking in a decorator or base class so it happens automatically.
2. **Log early, log often.** Start logging from the very first experiment. "I'll add tracking later" means you lose your baseline.
3. **Use consistent naming.** A naming convention for experiments and runs makes searching and filtering dramatically faster.
4. **Tag everything meaningful.** Tags are free-form and cheap. Use them for project, status, data version, and any categorical variable you'll want to filter by later.
5. **Set a quality bar for model registration.** Not every run should become a registered model. Define minimum metric thresholds before promotion.
6. **Clean up periodically.** Archive or delete failed and exploratory runs that no longer provide value. Keep the experiment history navigable.
7. **Connect tracking to your model registry.** The path from "best experiment" to "deployed model" should be traceable through linked artifacts.

## Tools & Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html) - Open-source experiment tracking, model registry, and deployment
- [Weights & Biases Quickstart](https://docs.wandb.ai/quickstart) - Cloud-based experiment tracking with rich visualization
- [DVC (Data Version Control)](https://dvc.org/doc) - Version control for ML datasets and model artifacts
- [Neptune.ai](https://neptune.ai/) - Metadata store for MLOps with flexible experiment tracking
- [TensorBoard](https://www.tensorflow.org/tensorboard) - TensorFlow's built-in visualization toolkit
- [Hyperopt](https://github.com/hyperopt/hyperopt) - Distributed hyperparameter optimization with experiment tracking integration
- [Optuna](https://optuna.org/) - Automatic hyperparameter optimization framework with MLflow/W&B integration

## Example Application

**Scenario**: A team of three data scientists is working on a text classification project. After two weeks, they have run approximately 80 experiments across different architectures, learning rates, and data augmentations. No one tracked anything systematically. Now they need to select the best model for deployment and cannot remember which run produced the best F1 score, or what parameters it used.

**Application**:

1. *Immediate fix* — The team sets up MLflow with a shared tracking server. They create a consistent experiment structure: `text-classification` as the project, with experiments named by architecture (`bert-base`, `distilbert`, `roberta-large`).

2. *Naming convention* — They adopt the convention `[date]-[key-change]` for run names (e.g., `2026-08-10-augmentation-synonyms`) and require tags for `status`, `author`, and `data_version` on every run.

3. *Integration* — They wrap the training function with a decorator that automatically logs all config parameters, git hash, and data hash. Individual metric logging is added at the end of each epoch.

4. *Recovery* — They re-run the 5 most promising configurations from memory, this time with full tracking. Within one day, they identify the best configuration (RoBERTa-large with synonym augmentation, F1=0.91) and can reproduce it exactly.

5. *Registry* — The best model is registered in MLflow's model registry with a model card documenting its evaluation results, known limitations, and the experiment run that produced it.

**Outcome**: What could have been a week of re-running experiments is resolved in one day. The team establishes a rule: no run counts unless it's tracked. Future onboarding of new team members takes hours instead of days because the experiment history is fully navigable.

## Success Indicators

You know you've mastered experiment tracking when:

- Every experiment you run is logged without manual effort (tracking is integrated into the training loop)
- You can find any past run and reproduce it within 10 minutes using only the tracked information
- Your team uses a consistent naming and tagging convention that makes search intuitive
- Model promotion to production always traces back to a specific tracked experiment
- New team members can understand what has been tried and why by browsing the experiment history
- You can compare two runs and immediately see what parameter or data change caused the performance difference
- Stakeholders trust your model selection process because it's evidence-based and documented

## Related Skills

- [Data Analysis](data_analysis.md) - Statistical analysis underpins meaningful experiment comparison
- [Model Evaluation](../technical-skills/model_evaluation.md) - Evaluation metrics are what you track and compare across experiments
- [MLOps](../devops-skills/mlops.md) - Experiment tracking feeds into the model registry and deployment pipeline
- [Planning](../behavior-skills/planning.md) - Systematic experiment planning prevents wasteful exploration
