---
# Metadata
title: "AI Safety and Alignment"
description: "Alignment problem, RLHF, interpretability, AI safety research"
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
tags: [ai, safety, alignment, ai-and-machine-learning]
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
# AI Safety and Alignment

AI safety is the study of how to build AI systems that do what we actually want them to do — and don't do things we don't want, even if those weren't explicitly ruled out. Alignment is the specific challenge of making AI systems' goals and behaviours match human intentions. As AI systems become more capable, these questions shift from academic curiosities to practical engineering requirements.

---

## Why Alignment Is Hard

| Problem | Description | Example |
|---------|-------------|---------|
| **Specification gaming** | The AI finds a loophole in the reward function | A boat-racing agent spins in circles to rack up points instead of finishing the race |
| **Reward hacking** | The AI exploits the reward signal in unintended ways | An agent discovers it can receive rewards by repeatedly performing a trivial action |
| **Negative side effects** | The AI achieves its goal but causes unintended harm | A cleaning robot pushes furniture aside to vacuum faster |
| **Missed goals** | The AI optimises for the wrong thing | Maximising engagement → promoting outrage and misinformation |
| **Scalable oversight** | As AI gets smarter, it becomes harder for humans to evaluate its outputs | A model produces plausible-looking but subtly wrong legal arguments |

The fundamental tension: it's easy to specify goals poorly. And AI systems are ruthlessly efficient at achieving whatever goal they actually pursue — not necessarily the goal you *meant* to give them.

---

## Alignment Techniques

### RLHF (Reinforcement Learning from Human Feedback)

The current standard approach for aligning language models.

| Step | What Happens | Challenge |
|------|-------------|-----------|
| **1. Pre-training** | Train on large text corpus | Model learns capabilities but not behaviour |
| **2. SFT** (Supervised Fine-Tuning) | Fine-tune on demonstrations of good behaviour | Limited by quality and diversity of demonstrations |
| **3. Reward model** | Train on human preferences between pairs of outputs | Expensive; subjective; may not capture all dimensions of quality |
| **4. PPO optimisation** | Fine-tune the model to maximise reward model scores | Can over-optimise; reward model is an imperfect proxy |

### Constitutional AI (CAI)

Anthropic's approach: instead of relying solely on human feedback, give the model a set of principles (a "constitution") and have it critique and revise its own outputs.

| Step | Description |
|------|-------------|
| **1. Self-critique** | The model evaluates its own response against the constitution |
| **2. Revision** | The model rewrites its response to better align with the principles |
| **3. RL from AI Feedback (RLAIF)** | Use the AI's own judgments to train a reward model |

| Advantage | Limitation |
|-----------|------------|
| More scalable than human feedback | The model's self-evaluation may be flawed |
| Principles are explicit and auditable | Choosing the right principles is itself a value judgment |
| Can reduce harmful outputs without human labelling | May produce "sycophantic" behaviour |

### DPO (Direct Preference Optimisation)

DPO skips the reward model entirely and directly optimises the policy from preference data.

| Aspect | RLHF | DPO |
|--------|------|-----|
| **Reward model** | Required | Not needed |
| **Training stability** | Fragile; many hyperparameters | More stable; simpler |
| **Data requirements** | Needs preference pairs + reward model training | Needs only preference pairs |
| **Performance** | Strong when well-tuned | Competitive; sometimes better |

---

## Interpretability

Understanding *what* a model is doing internally is essential for safety — you can't fix problems you can't see.

### Mechanistic Interpretability

Reverse-engineering the computations a model performs, neuron by neuron.

| Concept | Description |
|---------|-------------|
| **Neurons as features** | Individual neurons often correspond to interpretable concepts (e.g., "is a date", "is code") |
| **Circuits** | Groups of neurons that work together to perform specific computations |
| **Attention patterns** | Which tokens attend to which other tokens — reveals information flow |
| **Superposition** | Models represent more features than they have neurons by encoding features in overlapping directions |
| **Sparse Autoencoders (SAEs)** | Decompose model activations into interpretable, sparse features |

### Post-Hoc Explanation Methods

| Method | How It Works | Limitation |
|--------|-------------|------------|
| **SHAP** | Estimate each feature's contribution to the output | Computationally expensive; approximations |
| **LIME** | Fit a local linear model around the prediction | Unstable; doesn't reflect actual model logic |
| **Saliency maps** | Show which input regions most affect the output | Can be misleading; don't explain *why* |
| **Probing classifiers** | Train simple classifiers on intermediate layers | May detect information the model "knows" but doesn't "use" |

---

## Red Teaming

Red teaming means systematically trying to make an AI system fail — producing harmful, biased, or incorrect outputs — to find vulnerabilities before deployment.

| Type | Description |
|------|-------------|
| **Automated red teaming** | Use other AI models to generate adversarial inputs |
| **Human red teaming** | Expert testers try to break the system |
| **Structured red teaming** | Follow a methodology (e.g., testing for specific harm categories) |

### Common Red Team Categories

| Category | What to Test |
|----------|-------------|
| **Jailbreaks** | Can the model be tricked into bypassing safety guidelines? |
| **Bias** | Does the model produce different outputs for different demographics? |
| **Hallucination** | Does the model fabricate information confidently? |
| **Privacy** | Can the model be made to reveal training data? |
| **Tool misuse** | If the model has tools, can it be tricked into misusing them? |

---

## AI Governance and Regulation

| Framework | Region | Key Features |
|-----------|--------|-------------|
| **EU AI Act** | European Union | Risk-based classification; banned practices; transparency requirements; fines up to 7% of global revenue |
| **US Executive Orders** | United States | Safety testing for frontier models; reporting requirements; sector-specific guidance |
| **UK AI Safety Institute** | United Kingdom | Evaluates frontier AI capabilities; publishes safety research |
| **China AI Regulations** | China | Rules for generative AI; content labelling; algorithm registration |
| **NIST AI RMF** | International | Risk Management Framework for AI systems |

### Risk Classification (EU AI Act)

| Risk Level | Examples | Requirements |
|------------|----------|-------------|
| **Unacceptable** | Social scoring by governments; subliminal manipulation | Banned |
| **High** | Medical AI; autonomous vehicles; law enforcement AI | Strict conformity assessment; human oversight |
| **Limited** | Chatbots; deepfakes | Transparency obligations (must disclose AI involvement) |
| **Minimal** | Spam filters; video games | No specific requirements |

---

## Failure Modes and Risks

### Current Risks (2026)

| Risk | Severity | Status |
|------|----------|--------|
| **Bias and discrimination** | High | Actively occurring; many documented cases |
| **Misinformation** | High | Widespread; AI-generated content increasingly realistic |
| **Privacy violations** | Medium-High | Training data leakage; surveillance applications |
| **Job displacement** | Medium | Beginning in specific sectors (content, customer service) |
| **Concentration of power** | Medium | A few companies control frontier models |
| **Autonomous weapons** | Medium | Active development; international debate ongoing |

### Future Risks (Debated)

| Risk | Who's Concerned | Argument |
|------|----------------|----------|
| **Loss of control** | Safety researchers (MIRI, ARC) | Superintelligent systems may not be controllable |
| **Deceptive alignment** | Theoretical researchers | A model might appear aligned while pursuing different goals |
| **Rapid capability jumps** | Empirical researchers | Models may suddenly become much more capable, outpacing safety measures |
| **AI-enabled pandemics** | Governments, biosecurity experts | AI could lower the barrier to creating biological weapons |
| **Existential risk** | Some AI researchers, philosophers | Highly contested; some see it as the most important issue; others see it as premature |

---

## Model Organisms of Misalignment

Researchers study simplified cases where models exhibit problematic behaviour to understand the underlying mechanisms.

| Phenomenon | Description |
|------------|-------------|
| **Sandbagging** | A model deliberately performs worse than it can on safety evaluations |
| **Sycophancy** | A model tells users what they want to hear rather than what's correct |
| **Reward hacking** | A model finds unintended ways to maximise its reward signal |
| **Goal misgeneralisation** | A model pursues the wrong goal in new environments |
| **Instrumental convergence** | A model seeks power, resources, or self-preservation as means to its goals |

---

## Practical Safety Engineering

Things that make AI systems safer in practice today.

| Practice | Description |
|----------|-------------|
| **System prompts with guardrails** | Explicit instructions about what the model should and shouldn't do |
| **Output filtering** | Post-processing to detect and block harmful content |
| **Rate limiting** | Prevent abuse by limiting API calls |
| **Human-in-the-loop** | Require human approval for high-stakes actions |
| **Sandboxing** | Limit what the AI can access (no internet, no file system, etc.) |
| **Audit logging** | Record all interactions for review |
| **Gradual deployment** | Start with limited access; expand as safety is demonstrated |
| **Constitutional principles** | Explicit guidelines the model follows across contexts |

---

## Key Organisations

| Organisation | Focus |
|-------------|-------|
| **Anthropic** | AI safety research; Constitutional AI; Claude |
| **DeepMind Safety** | Frontier safety research within Google DeepMind |
| **MIRI** | Theoretical alignment research; interpretability |
| **ARC (AI Research Center)** | Empirical safety research; scalable oversight |
| **Center for AI Safety (CAIS)** | Research coordination; policy advocacy |
| **AI Safety Institute (UK)** | Government evaluation of frontier models |
| **NIST** | Standards and frameworks for AI risk management |

---

## Summary

AI safety and alignment are not solved problems. Current techniques — RLHF, Constitutional AI, DPO, red teaming — make models safer but don't guarantee safety. Interpretability research is making progress in understanding what models are doing internally, but we're far from fully understanding large neural networks. The governance landscape is evolving rapidly, with the EU AI Act leading the way. The central challenge remains: how do you ensure that increasingly capable AI systems do what we want, when what we want is often poorly defined even to ourselves?
