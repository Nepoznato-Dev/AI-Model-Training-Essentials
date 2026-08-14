<!--
---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
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
tags: [reinforcement, learning, ai-and-machine-learning]
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

-->
# Reinforcement Learning

Reinforcement learning (RL) is how machines learn to make sequences of decisions by trial and error. Unlike supervised learning, where the correct answer is provided for every example, RL gives an agent only a reward signal — and the agent must figure out which actions lead to the best outcomes over time. It's the approach behind AlphaGo, robotic control, game-playing AI, and — critically — RLHF, the technique used to align modern large language models with human preferences.

---

## Core Concepts

RL frames decision-making as a loop between an **agent** and an **environment**.

| Component | Role | Example |
|-----------|------|---------|
| **Agent** | The decision-maker | A chess program, a robot, a language model |
| **Environment** | The world the agent interacts with | The chessboard, a warehouse, a conversation |
| **State** | The current situation | Board position, robot sensor readings, chat history |
| **Action** | What the agent can do | Move a piece, turn left, generate a token |
| **Reward** | Feedback signal (scalar number) | +1 for winning, -1 for crashing, human preference score |
| **Policy** | Strategy mapping states to actions | "If the king is threatened, move it" |
| **Value function** | Expected cumulative reward from a state | "This board position is worth about +3 points" |

### The RL Loop

```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

The agent's goal is to maximise the **cumulative reward** over time, not just the immediate reward. This is what makes RL fundamentally different from supervised learning.

---

## Key Differences from Other Learning Paradigms

| Aspect | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|--------|-------------------|---------------------|----------------------|
| **Signal** | Correct labels for every example | No labels; find structure | Scalar reward, often delayed |
| **Feedback** | Immediate | None | Delayed and sparse |
| **Sequence** | Each example is independent | Each example is independent | Actions affect future states |
| **Goal** | Minimise prediction error | Discover patterns | Maximise cumulative reward |

---

## Markov Decision Processes (MDPs)

MDPs are the mathematical framework for RL. They assume the future depends only on the current state, not the history of how you got there (the **Markov property**).

| Component | Notation | Meaning |
|-----------|----------|---------|
| **States** | S | All possible situations the agent can be in |
| **Actions** | A | All things the agent can do |
| **Transition function** | P(s' \| s, a) | Probability of reaching state s' after taking action a in state s |
| **Reward function** | R(s, a, s') | Reward received for the transition |
| **Discount factor** | γ (gamma) | How much to value future rewards vs immediate ones (0 to 1) |

The **return** (total discounted reward) is:

```
G = R₁ + γR₂ + γ²R₃ + ...
```

A high discount factor (γ close to 1) means the agent is far-sighted. A low one means it's short-sighted.

---

## Classical RL Algorithms

### Value-Based Methods

These learn how good each state (or state-action pair) is.

| Algorithm | Key Idea | Limitation |
|-----------|----------|------------|
| **Q-Learning** | Learn a table of Q-values: Q(state, action) = expected reward | Doesn't scale to large state spaces |
| **Deep Q-Network (DQN)** | Use a neural network to approximate Q-values | Only handles discrete actions; can be unstable |
| **Double DQN** | Fix Q-learning's overestimation bias | Still limited to discrete actions |

Q-learning update rule:

```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Policy-Based Methods

These directly learn the policy (strategy) without estimating values.

| Algorithm | Key Idea | Advantage |
|-----------|----------|-----------|
| **REINFORCE** | Monte Carlo policy gradient; update policy in direction of good outcomes | Simple; works with continuous actions |
| **PPO** (Proximal Policy Optimization) | Clip policy updates to prevent large, destabilising changes | Stable; widely used; good default |
| **TRPO** | Trust region method for policy updates | More principled than PPO; harder to implement |

### Actor-Critic Methods

Combine the best of both: an **actor** (policy) and a **critic** (value function).

| Algorithm | Key Idea |
|-----------|----------|
| **A2C / A3C** | Advantage Actor-Critic; uses advantage estimation to reduce variance |
| **SAC** (Soft Actor-Critic) | Maximise reward while maintaining exploration (entropy regularisation) |
| **TD3** (Twin Delayed DDPG) | Address overestimation in continuous action spaces |

---

## RLHF: Reinforcement Learning from Human Feedback

RLHF is the technique that made ChatGPT possible. It bridges the gap between a model that can predict text and one that produces outputs humans actually find helpful.

### The Three Steps

| Step | What Happens | Output |
|------|-------------|--------|
| **1. Supervised Fine-Tuning (SFT)** | Fine-tune a pre-trained model on high-quality human-written examples | A model that follows instructions reasonably well |
| **2. Reward Model Training** | Humans compare pairs of model outputs; train a model to predict human preferences | A reward model that scores output quality |
| **3. RL Optimisation** | Use PPO to fine-tune the SFT model to maximise the reward model's scores | A model aligned with human preferences |

### Why RLHF Matters

Without RLHF, a language model is like a student who has read every book but doesn't know how to behave in a conversation. It can generate text, but the text might be unhelpful, toxic, or miss the point entirely. RLHF teaches the model *what humans want* — not just what text looks like.

### Variants and Alternatives

| Method | Description | Advantage |
|--------|-------------|-----------|
| **DPO** (Direct Preference Optimisation) | Skip the reward model; directly optimise policy from human preferences | Simpler; no separate reward model to train |
| **RLAIF** | Use AI (rather than humans) to generate preference labels | Cheaper than human labelling |
| **Constitutional AI** | Use a set of principles to guide model behaviour without human labels | More scalable; Anthropic's approach |
| **GRPO** (Group Relative Policy Optimisation) | Compare outputs within a group rather than against a separate model | Used in DeepSeek-R1; reduces need for value network |

---

## Exploration vs Exploitation

This is the central tension in RL. **Exploitation** means choosing actions you know work well. **Exploration** means trying new things to discover potentially better strategies.

| Strategy | How It Works | Trade-off |
|----------|-------------|-----------|
| **ε-greedy** | Choose the best action most of the time; random action with probability ε | Simple but inefficient |
| **Boltzmann exploration** | Choose actions probabilistically based on their estimated values | Smoother than ε-greedy |
| **UCB** (Upper Confidence Bound) | Prefer actions with high uncertainty (optimism in the face of uncertainty) | Good theoretical guarantees |
| **Entropy regularisation** | Add a bonus for visiting diverse states (used in SAC, PPO) | Encourages natural exploration |

---

## Multi-Agent Reinforcement Learning

When multiple agents learn simultaneously, the dynamics become far more complex.

| Scenario | Challenge | Example |
|----------|-----------|---------|
| **Cooperative** | Agents must coordinate; credit assignment is hard | Robot football teams; distributed sensor networks |
| **Competitive** | Opponents adapt; the environment is non-stationary | Game AI (poker, StarCraft); cybersecurity |
| **Mixed** | Some agents cooperate, others compete | Auction markets; traffic systems |

| Algorithm | Description |
|-----------|-------------|
| **MADDPG** | Multi-agent version of DDPG; centralised critic, decentralised actors |
| **MAPPO** | Multi-agent PPO; widely used in practice |
| **Self-Play** | Agents train against copies of themselves (AlphaGo, AlphaStar) |

---

## Sim-to-Real Transfer

Training robots in the real world is slow and dangerous. Instead, agents train in simulation and transfer to reality.

| Challenge | Solution |
|-----------|----------|
| **Reality gap** (simulation ≠ real world) | Domain randomisation: vary physics parameters during training |
| **Sample inefficiency** | Use model-based RL or train on large parallel simulations |
| **Safety** | Constrained RL: penalise unsafe actions during training |
| **Partial observability** | Train with noisy sensors and delayed observations |

Companies like Boston Dynamics and Tesla use simulation extensively, but the gap between simulated and physical performance remains one of the field's biggest challenges.

---

## Tools and Frameworks

| Tool | Purpose | Best For |
|------|---------|----------|
| **Stable-Baselines3** | Clean Python implementations of PPO, SAC, TD3, DQN | Learning and prototyping |
| **RLlib** | Scalable RL library built on Ray | Large-scale distributed training |
| **CleanRL** | Single-file implementations for research | Understanding algorithms deeply |
| **Gymnasium (OpenAI)** | Standardised environment interface | Defining RL problems |
| **Isaac Gym / Isaac Lab** | GPU-accelerated physics simulation | Robotics, sim-to-real |
| **TRL** (Transformer RL Library) | RLHF, DPO, PPO for language models | Aligning LLMs |
| **OpenRLHF** | Distributed RLHF framework | Training large models with RLHF |

---

## Practical Tips

- **Start with PPO.** It's the most reliable general-purpose algorithm. If you're not sure what to use, PPO is the default.
- **Normalise your rewards.** Reward scaling dramatically affects training stability.
- **Use vectorised environments.** Running many environments in parallel (e.g., 8–64) stabilises gradient estimates and speeds up training enormously.
- **Monitor both reward and entropy.** If entropy drops to zero, your agent has stopped exploring and may be stuck in a local optimum.
- **Reward shaping is an art.** Designing the right reward function is often the hardest part. Sparse rewards (only at the end) make learning extremely slow. Dense, well-shaped rewards guide the agent but can introduce unintended behaviour.
- **RLHF is fragile.** Small changes to the reward model or PPO hyperparameters can cause large quality drops. DPO is a more stable alternative if you don't need the full RLHF pipeline.

---

## Summary

Reinforcement learning is the study of how agents learn to make decisions through interaction. It ranges from classical algorithms like Q-learning to modern deep RL methods like PPO and SAC, and it underpins some of the most important recent advances in AI — from game-playing to language model alignment. The core challenge remains the same: how do you learn optimal behaviour when feedback is delayed, sparse, and noisy? The answer — trial and error, guided by clever mathematics — turns out to be one of the most powerful ideas in all of artificial intelligence.
