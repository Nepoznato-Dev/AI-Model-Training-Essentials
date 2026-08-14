# Reinforcement Learning

> **Welcome to the Reinforcement Learning guide!** Learn how to train AI agents that learn by trial and error — just like how you learned to ride a bike by falling off and getting back on.

---

## What Is Reinforcement Learning?

Reinforcement Learning (RL) is a type of machine learning where an **agent** learns to make decisions by interacting with an **environment**. The agent takes **actions**, receives **rewards** (or penalties), and gradually learns the best strategy to maximize its total reward.

### The RL Loop

```
         Action
    Agent ──────────> Environment
      ↑                    │
      │                    │
      └────────────────────┘
         State + Reward
```

1. **Agent** observes the current **state** of the environment
2. Agent chooses an **action** based on its current strategy (policy)
3. Environment transitions to a new state and gives a **reward**
4. Agent updates its strategy to get more rewards in the future

### Analogy

Think of training a dog with treats:
- **Agent:** The dog
- **Environment:** The room, obstacles, toys
- **Action:** Sit, stay, fetch, roll over
- **Reward:** A treat (positive) or a "no" (negative)
- **Policy:** The dog's learned behavior — "when I hear 'sit', I sit and get a treat"

The dog doesn't know the rules at first. It tries random things, gets treats for good actions, and learns which actions lead to the most treats over time.

---

## Why Is RL Important?

| Application | Example |
|-------------|---------|
| Game Playing | AlphaGo, Dota 2 bots, Atari game agents |
| Robotics | Teaching robots to walk, grasp objects, navigate |
| Autonomous Driving | Decision-making for self-driving cars |
| Resource Management | Optimizing data center cooling, network routing |
| Finance | Portfolio optimization, trading strategies |
| Healthcare | Treatment planning, drug dosage optimization |
| LLM Alignment | RLHF — making AI assistants helpful and harmless |

---

## Guide Structure

This guide is organized into **2 chapters**:

| Chapter | Title | What You'll Learn |
|---------|-------|-------------------|
| 1 | [RL Fundamentals](chapter_1_fundamentals.md) | Markov Decision Processes, Q-Learning, policy gradients, reward shaping |
| 2 | [Deep RL and Advanced Topics](chapter_2_deep_rl.md) | DQN, PPO, A3C, RLHF, multi-agent RL, sim-to-real transfer |

---

## Prerequisites

Before starting, you should be comfortable with:

| Topic | Recommended Resource |
|-------|---------------------|
| Python & NumPy | Basic programming, arrays, loops |
| PyTorch | Tensors, neural networks, training loops |
| Probability | Expected values, distributions |
| CNNs (helpful) | Our [CNNs Guide](../CNNs/README.md) — for deep RL with image inputs |

---

## Hardware Requirements

| Setup | Details |
|-------|---------|
| **Minimum** | CPU with 4GB RAM (for tabular Q-Learning and simple environments) |
| **Recommended** | CPU with 8GB RAM + PyTorch (for DQN, policy gradients) |
| **Ideal** | GPU with 4GB+ VRAM (for deep RL with image inputs, PPO, A3C) |

> **Note:** Most RL algorithms can be learned on CPU. GPU helps when processing image observations or training large neural networks.

---

## Quick Start

```bash
# Install dependencies
pip install gymnasium numpy torch matplotlib

# Verify installation
python -c "import gymnasium as gym; env = gym.make('CartPole-v1'); print(f'Environment ready! Observation: {env.observation_space}, Actions: {env.action_space}')"

# Run a random agent
python -c "
import gymnasium as gym
env = gym.make('CartPole-v1')
obs, info = env.reset()
total_reward = 0
for _ in range(100):
    action = env.action_space.sample()  # Random action
    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    if terminated or truncated:
        break
print(f'Random agent total reward: {total_reward}')
env.close()
"
```

---

## Key Concepts Glossary

| Term | Definition |
|------|-----------|
| **Agent** | The decision-maker (your AI algorithm) |
| **Environment** | The world the agent interacts with |
| **State** | A description of the current situation |
| **Action** | What the agent can do |
| **Reward** | A scalar signal telling the agent how well it's doing |
| **Policy** | The agent's strategy: which action to take in each state |
| **Value Function** | Expected total future reward from a state (how "good" is this situation?) |
| **Q-Value** | Expected total reward for taking a specific action in a specific state |
| **Episode** | One complete interaction from start to finish |
| **Discount Factor (gamma)** | How much the agent cares about future vs immediate rewards |
| **Exploration** | Trying new actions to discover better strategies |
| **Exploitation** | Using known good actions to maximize reward |
| **MDP** | Markov Decision Process — the mathematical framework for RL |
| **Bellman Equation** | Recursive equation that defines optimal values |
| **Model-Free** | RL without knowing the environment's dynamics |
| **Model-Based** | RL with a learned model of how the environment works |

---

## Best Practices

1. **Start with simple environments** — CartPole, MountainCar before Atari
2. **Normalize rewards** — Scale rewards to [0, 1] or [-1, 1] for stability
3. **Use epsilon-greedy exploration** — Start with high epsilon (explore), decay over time
4. **Monitor both reward and loss** — Reward should increase; loss patterns reveal issues
5. **Use experience replay** — Store past transitions and sample randomly (breaks correlations)
6. **Set random seeds** — RL is notoriously sensitive to random seeds; run multiple trials
7. **Visualize training** — Plot reward curves and record agent behavior periodically

---

## Common Pitfalls

1. **Reward hacking** — Agent finds unexpected ways to maximize reward (e.g., spinning in circles)
2. **Too much exploitation** — Agent gets stuck in a suboptimal strategy and never explores
3. **Discount factor too high** — Training becomes unstable; too low makes agent short-sighted
4. **Not enough episodes** — RL needs thousands of episodes; don't judge after 100
5. **Ignoring state representation** — Raw pixels are hard; use frame stacking and normalization
6. **Catastrophic forgetting** — Agent forgets good behaviors while learning new ones
7. **No baseline for policy gradients** — High variance without a value function baseline

---

## Troubleshooting

### "Agent reward stays at random level and doesn't improve"

```python
# Common causes and fixes:
# 1. Learning rate too high or too low
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)  # Try 1e-4 or 3e-4

# 2. Not enough exploration
epsilon = max(0.01, epsilon * 0.995)  # Decay epsilon slowly

# 3. Reward signal too sparse — add reward shaping
reward = reward + 0.1 * (distance_to_goal_before - distance_to_goal_after)
```

### "Training is very unstable — reward goes up then crashes"

```python
# Solution: Use experience replay and target network (DQN)
import random
from collections import deque

replay_buffer = deque(maxlen=10000)

# Store transitions
replay_buffer.append((state, action, reward, next_state, done))

# Sample random batch for training
batch = random.sample(replay_buffer, batch_size=32)
```

### "Agent works in training but fails in evaluation"

```python
# Solution: Make sure to set model to eval mode and disable exploration
model.eval()
with torch.no_grad():
    action = model(state).argmax().item()  # Greedy action, no epsilon
```

---

## Learning Pathway

```
Prerequisites (Python, PyTorch basics)
        │
        ▼
Chapter 1: Fundamentals
  - Markov Decision Processes
  - Tabular Q-Learning
  - Policy gradients (REINFORCE)
  - Reward shaping
        │
        ▼
Chapter 2: Deep RL & Advanced Topics
  - DQN (Deep Q-Networks)
  - PPO (Proximal Policy Optimization)
  - A3C / A2C
  - RLHF (RL from Human Feedback)
  - Multi-agent RL
        │
        ▼
  Build your own RL agent!
```

---

## What You'll Be Able to Do

After completing this guide:

- Understand the mathematical foundations of RL (MDPs, Bellman equations)
- Implement Q-Learning and Deep Q-Networks (DQN)
- Train agents using policy gradients (REINFORCE, PPO)
- Apply reward shaping to guide agent learning
- Use RLHF concepts for aligning AI behavior
- Choose the right RL algorithm for different problem types
- Train agents in classic control and Atari environments

---

## Additional Resources

- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [Spinning Up in Deep RL (OpenAI)](https://spinningup.openai.com/)
- [Sutton & Barto: Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html)
- [DeepMind's RL Course](https://www.deepmind.com/learning-resources)
- [CleanRL — Single-file RL implementations](https://github.com/vwxyzjn/cleanrl)

---

## Exercises

### Chapter 1 Exercises
1. Implement tabular Q-Learning for the FrozenLake environment (4x4 grid)
2. Compare epsilon-greedy vs UCB exploration strategies
3. Implement REINFORCE (policy gradient) on CartPole-v1
4. Experiment with different discount factors (0.9, 0.99, 0.999) and observe behavior

### Chapter 2 Exercises
1. Implement DQN with experience replay on CartPole-v1
2. Add a target network to your DQN and compare stability
3. Implement PPO and train it on LunarLander-v2
4. Try RLHF: create a simple reward model and fine-tune a policy with it
5. Train an agent on an Atari game (Pong) using DQN with frame stacking

---

## Related Guides

| Guide | Connection |
|-------|-----------|
| [Agentic Systems](../Agentic_Systems/README.md) | Agents that reason and use tools (overlaps with RL) |
| [Transformers](../Transformers/README.md) | Used in modern RL architectures (decision transformers) |
| [CNNs](../CNNs/README.md) | Processing image observations in deep RL |

---

*Ready to start? Head to [Chapter 1: RL Fundamentals](chapter_1_fundamentals.md).*
