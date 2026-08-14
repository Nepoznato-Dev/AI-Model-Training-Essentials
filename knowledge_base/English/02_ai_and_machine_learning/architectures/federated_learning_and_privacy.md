---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
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
# Federated Learning and Privacy

Federated learning is a technique for training machine learning models across multiple devices or organisations without sharing the raw data. Instead of sending data to a central server, each device trains a local model and only shares the model updates (gradients or weights). The central server aggregates these updates to produce a global model. It was designed by Google for training keyboard language models on Android phones — and it has since become a key technique for privacy-preserving AI.

---

## Why Federated Learning?

| Motivation | Description | Example |
|------------|-------------|---------|
| **Data privacy** | Raw data never leaves the device | Medical records stay in the hospital; photos stay on the phone |
| **Regulatory compliance** | GDPR, HIPAA, and other regulations restrict data sharing | Banks can collaborate without sharing customer data |
| **Data volume** | Moving data is expensive and slow | Training on billions of phones is impractical if data must be uploaded |
| **Data sensitivity** | Some data is too sensitive to share, even with consent | Government intelligence; personal health data |

---

## How Federated Learning Works

### The Basic Protocol (FedAvg)

| Step | What Happens |
|------|-------------|
| **1. Initialise** | Central server creates a global model with random weights |
| **2. Distribute** | Server sends the current global model to selected devices |
| **3. Local training** | Each device trains the model on its local data for several epochs |
| **4. Upload** | Devices send their updated model weights (not data) back to the server |
| **5. Aggregate** | Server averages the weights (Federated Averaging) to create a new global model |
| **6. Repeat** | Go back to step 2 until the model converges |

```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Key Properties

| Property | Description |
|----------|-------------|
| **Non-IID data** | Each device has different data distributions (not independent and identically distributed) |
| **Unbalanced data** | Some devices have lots of data, others have very little |
| **Partial participation** | Not all devices are available in every round |
| **Communication efficiency** | The bottleneck is communication, not computation |

---

## Federated Learning Variants

| Variant | Description | Advantage |
|---------|-------------|-----------|
| **FedAvg** | Average model weights across devices | Simple; works well for IID data |
| **FedProx** | Adds a proximal term to local training | Better for non-IID data |
| **SCAFFOLD** | Uses control variates to correct for data heterogeneity | Faster convergence on non-IID data |
| **FedSGD** | Like FedAvg but with one gradient step per round | Lower communication cost per round |
| **Personalised FL** | Each device maintains a personalised model alongside the global one | Better per-device performance |
| **Vertical FL** | Different features (not different samples) across parties | When parties hold different aspects of the same data |

---

## Differential Privacy

Differential privacy (DP) provides a mathematical guarantee that the output of an algorithm doesn't reveal whether any individual's data was included.

### Core Definition

A mechanism M satisfies (ε, δ)-differential privacy if for any two datasets D and D' that differ in one record:

```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parameter | Meaning |
|-----------|---------|
| **ε (epsilon)** | Privacy budget. Smaller = more private. Typical values: 0.1–10. |
| **δ (delta)** | Probability of privacy guarantee failing. Typically set to 1/N (inverse of dataset size). |

### Mechanisms for Adding Privacy

| Mechanism | How It Works | Use Case |
|-----------|-------------|----------|
| **Gaussian mechanism** | Add Gaussian noise calibrated to the sensitivity of the query | Continuous values (model weights) |
| **Laplace mechanism** | Add Laplace noise | Counting queries |
| **Exponential mechanism** | Select outputs with probability proportional to their utility | Discrete choices |

### DP-SGD (Differentially Private Stochastic Gradient Descent)

| Step | Description |
|------|-------------|
| 1. Compute per-sample gradients | Instead of batch gradients |
| 2. Clip gradients | Bound the maximum norm of each gradient (limits any single sample's influence) |
| 3. Add noise | Add calibrated Gaussian noise to the aggregated gradient |
| 4. Update parameters | Standard gradient descent step |

| Trade-off | Description |
|-----------|-------------|
| **Privacy vs accuracy** | Stronger privacy (lower ε) requires more noise, which reduces model accuracy |
| **Privacy vs training time** | More noise means slower convergence |
| **Privacy budget tracking** | Each training step consumes some of the privacy budget; once spent, it can't be recovered |

---

## Combining Federated Learning with Differential Privacy

| Layer | Protection |
|-------|-----------|
| **Federated learning** | Raw data stays on devices |
| **Differential privacy** | Even the model updates are noisy, protecting individual contributions |
| **Secure aggregation** | The server only sees the aggregate of all updates, not individual ones |

This combination provides strong privacy guarantees: even if the server is compromised, it cannot determine whether any specific individual's data was used in training.

---

## Other Privacy-Preserving Techniques

### Secure Multi-Party Computation (SMPC)

Multiple parties compute a function over their combined data without revealing their individual inputs.

| Feature | Description |
|---------|-------------|
| **How it works** | Data is split into shares distributed across parties; computation happens on shares |
| **Guarantee** | No party learns anything about the others' inputs |
| **Overhead** | Significant communication and computation cost |
| **Use case** | Banks computing joint risk models without sharing customer data |

### Homomorphic Encryption (HE)

Perform computations directly on encrypted data.

| Type | What It Supports | Overhead |
|------|-----------------|----------|
| **Partially HE** | One operation (addition OR multiplication) | Low |
| **Somewhat HE** | Limited number of both operations | Medium |
| **Fully HE** | Arbitrary computations | Very high (100-1000x slowdown) |

| Application | Description |
|-------------|-------------|
| **Private inference** | Run ML models on encrypted data; return encrypted predictions |
| **Encrypted training** | Train on encrypted data (still mostly theoretical for deep learning) |
| **Private queries** | Query a database without revealing the query or the data |

### Trusted Execution Environments (TEEs)

Hardware-based isolation (Intel SGX, ARM Trustzone) that protects data even from the OS.

| Advantage | Limitation |
|-----------|------------|
| Near-native performance | Requires specific hardware |
| Strong security guarantees | Limited memory (enclave size) |
| No cryptographic overhead | Side-channel attacks possible |

---

## Privacy Regulations and ML

| Regulation | Region | Impact on ML |
|------------|--------|-------------|
| **GDPR** | EU | Right to explanation; data minimisation; consent for processing; right to erasure |
| **CCPA** | California | Right to know, delete, and opt out of data selling |
| **HIPAA** | US (healthcare) | Strict controls on health data; de-identification requirements |
| **PIPL** | China | Data localisation; consent requirements; cross-border transfer rules |
| **AI Act** | EU | Transparency requirements; risk classification; prohibited practices |

### Impact on ML Workflows

| GDPR Principle | ML Implication |
|----------------|---------------|
| **Data minimisation** | Collect only what's needed; federated learning helps |
| **Purpose limitation** | Can't repurpose data without new consent |
| **Right to erasure** | Must be able to remove a person's data from a trained model (machine unlearning) |
| **Right to explanation** | Models must be interpretable enough to explain individual predictions |
| **Privacy by design** | Privacy must be built into systems from the start |

---

## Challenges

| Challenge | Description |
|-----------|-------------|
| **Communication cost** | Sending model updates over millions of devices is expensive |
| **Non-IID data** | Devices have very different data distributions, hurting convergence |
| **Stragglers** | Slow devices delay the entire round |
| **Privacy-utility trade-off** | Stronger privacy means worse model performance |
| **Poisoning attacks** | Malicious participants can corrupt the global model |
| **Model extraction** | Even shared model updates can leak information about training data |
| **Hardware heterogeneity** | Different devices have different compute capabilities |

---

## Tools and Frameworks

| Tool | Purpose |
|------|---------|
| **Flower** | Open-source federated learning framework; framework-agnostic |
| **TensorFlow Federated** | Google's FL framework for TensorFlow models |
| **PySyft** (OpenMined) | Privacy-preserving ML in PyTorch |
| **FATE** (Webank) | Industrial-grade federated learning platform |
| **LEAF** | Benchmark suite for federated learning research |
| **Opacus** (Meta) | Differential privacy for PyTorch |
| **Google's TF Privacy** | Differential privacy for TensorFlow |

---

## Summary

Federated learning and privacy-preserving techniques address a fundamental tension: how do you build powerful AI models when the data is distributed, sensitive, or regulated? Federated learning keeps data on devices and shares only model updates. Differential privacy adds mathematical guarantees that individual contributions can't be detected. Secure computation and homomorphic encryption go further, allowing computation on encrypted data. Each technique has costs — communication overhead, reduced accuracy, computational expense — but together they form a toolkit for building AI that respects privacy while still learning from the world's data.
