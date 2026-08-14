---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
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
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
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
tags: [ai, ethics, governance, ai-and-machine-learning]
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
# AI Ethics and Governance

AI systems are not neutral. They reflect the data they were trained on, the values of their creators, and the incentives of the organisations deploying them. Ethics is about asking not just "can we build this?" but "should we?" Governance is about creating the structures — laws, standards, oversight bodies — that ensure AI is developed and used responsibly. This file covers the key ethical dimensions of AI and the governance frameworks emerging to address them.

---

## Core Ethical Principles for AI

Most AI ethics frameworks converge on a set of shared principles.

| Principle | What It Means | Challenge |
|-----------|--------------|-----------|
| **Fairness** | AI should not discriminate against protected groups | Defining fairness mathematically is difficult; different fairness definitions can conflict |
| **Transparency** | Users should know when they're interacting with AI and how it works | Full transparency can enable gaming; proprietary systems resist disclosure |
| **Accountability** | Someone must be responsible when AI causes harm | Diffuse responsibility across developers, deployers, and users |
| **Privacy** | AI should respect personal data and autonomy | Training data often includes personal information; privacy and utility conflict |
| **Safety** | AI should not cause physical or psychological harm | Defining harm is context-dependent; edge cases are unpredictable |
| **Human oversight** | Humans should retain meaningful control | Automation bias means humans defer to AI; oversight becomes rubber-stamping |

---

## Bias in AI Systems

### Where Bias Comes From

| Source | Description | Example |
|--------|-------------|---------|
| **Training data** | Historical biases encoded in data | Hiring data reflects past discrimination → model discriminates |
| **Label bias** | Human annotators impose their biases | Resumes with "female" names rated lower by annotators |
| **Selection bias** | Data doesn't represent the target population | Facial recognition trained mostly on light-skinned faces |
| **Measurement bias** | Features proxy for protected attributes | Zip code correlates with race |
| **Algorithmic bias** | Optimisation amplifies small biases | A small gap in training data becomes a large gap in predictions |

### Fairness Metrics

| Metric | Definition | When to Use |
|--------|-----------|-------------|
| **Demographic parity** | Positive rate is equal across groups | When you want equal outcomes |
| **Equalised odds** | True positive rate and false positive rate are equal across groups | When you want equal error rates |
| **Predictive parity** | Precision is equal across groups | When you want predictions to mean the same thing for all groups |
| **Individual fairness** | Similar individuals are treated similarly | When you want consistency |

**Impossibility theorem**: you generally can't satisfy multiple fairness definitions simultaneously. Choosing which fairness metric to use is itself a value judgment.

### Bias Mitigation

| Stage | Technique |
|-------|-----------|
| **Pre-processing** | Rebalance training data; remove biased features; synthetic oversampling |
| **In-processing** | Add fairness constraints to the loss function; adversarial debiasing |
| **Post-processing** | Adjust thresholds per group; calibrate predictions |
| **Evaluation** | Regular fairness audits; disaggregated performance metrics |

---

## Explainability

### Why Explainability Matters

| Reason | Description |
|--------|-------------|
| **Trust** | Users need to understand why a decision was made |
| **Debugging** | Developers need to find and fix model errors |
| **Regulation** | GDPR's "right to explanation"; EU AI Act requirements |
| **Fairness** | You can't detect bias without understanding model behaviour |
| **Accountability** | Organisations need to justify automated decisions |

### Explanation Methods

| Method | Type | How It Works | Limitation |
|--------|------|-------------|------------|
| **SHAP** | Feature importance | Estimates each feature's contribution using game theory | Computationally expensive; approximations |
| **LIME** | Local surrogate | Fits a simple model around the prediction | Unstable; doesn't reflect actual model logic |
| **Attention visualisation** | Internal mechanism | Show which inputs the model attends to | Attention ≠ importance; can be misleading |
| **Counterfactuals** | What-if analysis | "If this feature were different, would the prediction change?" | Depends on realistic counterfactuals |
| **Feature attribution** | Importance scores | Saliency maps, integrated gradients | Doesn't explain *why*; just *where* |

---

## AI Regulation

### EU AI Act (2026)

The world's first comprehensive AI law.

| Risk Level | Examples | Requirements |
|------------|----------|-------------|
| **Unacceptable risk** | Social scoring; subliminal manipulation; real-time biometric surveillance (with exceptions) | Banned |
| **High risk** | Medical AI; autonomous vehicles; law enforcement; critical infrastructure | Conformity assessment; human oversight; transparency |
| **Limited risk** | Chatbots; deepfakes; recommendation systems | Must disclose AI involvement |
| **Minimal risk** | Spam filters; video games; most AI applications | No specific requirements |

### Other Regulatory Approaches

| Region | Approach | Status |
|--------|----------|--------|
| **United States** | Sector-specific; executive orders; voluntary commitments | Fragmented; no comprehensive federal law |
| **United Kingdom** | Principles-based; sector regulators | AI Safety Institute; pro-innovation approach |
| **China** | Specific regulations for generative AI, deepfakes, recommendations | Active enforcement; content requirements |
| **Canada** | AIDA (Artificial Intelligence and Data Act) | Proposed; similar to EU approach |
| **Brazil** | AI regulation framework | In progress |

---

## Environmental Impact

Training and running AI models consumes energy and generates carbon emissions.

| Activity | Estimated Emissions | Comparison |
|----------|-------------------|------------|
| **Training GPT-4** | Estimated 50+ tonnes CO₂ | Equivalent to several cars' annual emissions |
| **Training a large Transformer** | 280-620 tonnes CO₂ | 5x a car's lifetime emissions |
| **Daily inference (1M users)** | Ongoing; depends on model size and hardware | Can exceed training emissions over time |
| **Fine-tuning a 7B model** | 1-5 tonnes CO₂ | Significant but much less than pre-training |

### Mitigation

| Strategy | Impact |
|----------|--------|
| **Efficient hardware** | New GPUs are more energy-efficient per computation |
| **Model optimisation** | Smaller, quantised models use less energy |
| **Green energy** | Power data centres with renewable energy |
| **Efficient architectures** | Mixture of Experts; sparse models; distillation |
| **Carbon-aware scheduling** | Run training when the grid is cleanest |

---

## Intellectual Property and Copyright

| Issue | Description | Status |
|-------|-------------|--------|
| **Training on copyrighted works** | Models trained on books, articles, images without permission | Active lawsuits; fair use debate |
| **AI-generated output** | Who owns content generated by AI? | US Copyright Office: AI-generated content is not copyrightable without sufficient human authorship |
| **Style imitation** | AI can mimic an artist's style | Legally grey; ethical concerns |
| **Opt-out mechanisms** | Some providers allow creators to opt out of training | robots.txt; content filtering |

---

## Responsible Disclosure

| Principle | Description |
|-----------|-------------|
| **Pre-deployment testing** | Red teaming, bias audits, safety evaluations before release |
| **Gradual deployment** | Start with limited access; expand as safety is demonstrated |
| **Incident reporting** | Document and share information about failures and harms |
| **Bug bounties** | Reward external researchers for finding vulnerabilities |
| **Model cards** | Document model capabilities, limitations, and intended use |

---

## Data Provenance

| Concern | Description |
|---------|-------------|
| **Training data transparency** | Most frontier models don't disclose their training data |
| **Consent** | Were individuals' data used with their knowledge and permission? |
| **Data poisoning** | Can attackers inject malicious data into training sets? |
| **Dataset cards** | Documentation of dataset composition, collection methods, and limitations |
| **Watermarking** | Embedding invisible markers in AI-generated content to identify it |

---

## Practical Ethics Frameworks

### For AI Developers

| Question | Why It Matters |
|----------|---------------|
| **Who could be harmed by this system?** | Identifies affected stakeholders |
| **What happens if the model is wrong?** | Assesses the cost of errors |
| **Can the model's decisions be explained?** | Determines explainability requirements |
| **Is the training data representative?** | Checks for selection and measurement bias |
| **What are the failure modes?** | Anticipates edge cases and misuse |
| **How will the system be monitored?** | Plans for ongoing oversight |

### For Organisations Deploying AI

| Practice | Description |
|----------|-------------|
| **AI governance board** | Cross-functional team reviewing AI deployments |
| **Impact assessments** | Evaluate potential harms before deployment |
| **Human oversight processes** | Clear escalation paths when AI makes errors |
| **Regular audits** | Check for bias, drift, and unintended consequences |
| **User feedback channels** | Allow affected people to report problems |
| **Documentation** | Maintain records of model decisions and rationale |

---

## Summary

AI ethics and governance are engineering requirements. Bias, opacity, environmental cost, and privacy violations are not only ethical concerns; they are defects that cause real harm. The governance landscape is evolving rapidly, with the EU AI Act setting the global standard. Regulation alone is insufficient — fairness, explainability, and accountability must be integrated into the daily work of every AI developer. The central question is how to build systems that are worthy of trust.
