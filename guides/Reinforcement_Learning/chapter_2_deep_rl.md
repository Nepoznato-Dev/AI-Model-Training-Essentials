# Chapter 2: Deep RL and Advanced Topics

> **Goal:** Build deep reinforcement learning agents (DQN, PPO, A3C), understand RLHF for LLM alignment, and explore multi-agent systems.

---

## 2.1 Deep Q-Networks (DQN)

Tabular Q-Learning fails when the state space is huge (e.g., Atari pixels = \(210 \times 160 \times 3\) possible states). **DQN** (Mnih et al., 2015) replaces the Q-table with a neural network.

### Two Key Innovations

1. **Experience Replay:** Store all transitions \((s, a, r, s')\) in a buffer. Sample random batches for training. This breaks the correlation between consecutive samples.

2. **Target Network:** Use a separate, slowly-updated network to compute target Q-values. This stabilizes training by preventing the "moving target" problem.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
import gymnasium as gym
from collections import deque

class ReplayBuffer:
    """
    Experience replay buffer.
    
    Stores transitions (s, a, r, s', done) and samples random batches.
    Breaks temporal correlations that destabilize training.
    """
    
    def __init__(self, capacity=10000):
        self.buffer = deque(maxlen=capacity)
    
    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))
    
    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        return (
            np.array(states),
            np.array(actions),
            np.array(rewards, dtype=np.float32),
            np.array(next_states),
            np.array(dones, dtype=np.float32),
        )
    
    def __len__(self):
        return len(self.buffer)


class DQN(nn.Module):
    """Deep Q-Network for Atari-style games."""
    
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim)
        )
    
    def forward(self, state):
        return self.network(state)


class DQNAgent:
    """
    DQN Agent with experience replay and target network.
    
    Key components:
    - Q-Network: learns to predict Q-values
    - Target Network: frozen copy, updated periodically
    - Replay Buffer: stores and samples random transitions
    - Epsilon-Greedy: balances exploration and exploitation
    """
    
    def __init__(self, state_dim, action_dim, lr=1e-3, gamma=0.99,
                 buffer_size=10000, batch_size=64, target_update=10):
        self.q_net = DQN(state_dim, action_dim)
        self.target_net = DQN(state_dim, action_dim)
        self.target_net.load_state_dict(self.q_net.state_dict())  # Copy weights
        
        self.optimizer = optim.Adam(self.q_net.parameters(), lr=lr)
        self.buffer = ReplayBuffer(buffer_size)
        
        self.gamma = gamma
        self.batch_size = batch_size
        self.target_update = target_update
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.action_dim = action_dim
        self.update_count = 0
    
    def choose_action(self, state, training=True):
        if training and np.random.random() < self.epsilon:
            return np.random.randint(self.action_dim)
        
        with torch.no_grad():
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            q_values = self.q_net(state_tensor)
            return q_values.argmax().item()
    
    def train_step(self):
        """One step of DQN training."""
        if len(self.buffer) < self.batch_size:
            return 0.0
        
        # Sample random batch
        states, actions, rewards, next_states, dones = self.buffer.sample(self.batch_size)
        
        # Convert to tensors
        states_t = torch.FloatTensor(states)
        actions_t = torch.LongTensor(actions).unsqueeze(1)
        rewards_t = torch.FloatTensor(rewards).unsqueeze(1)
        next_states_t = torch.FloatTensor(next_states)
        dones_t = torch.FloatTensor(dones).unsqueeze(1)
        
        # Current Q-values (from Q-network)
        q_values = self.q_net(states_t).gather(1, actions_t)
        
        # Target Q-values (from target network — no gradient!)
        with torch.no_grad():
            next_q = self.target_net(next_states_t).max(1, keepdim=True)[0]
            target_q = rewards_t + self.gamma * next_q * (1 - dones_t)
        
        # Compute loss and update
        loss = nn.MSELoss()(q_values, target_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Update target network periodically
        self.update_count += 1
        if self.update_count % self.target_update == 0:
            self.target_net.load_state_dict(self.q_net.state_dict())
        
        # Decay exploration
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
        
        return loss.item()


def train_dqn(env_name="CartPole-v1", num_episodes=500):
    """Train a DQN agent."""
    env = gym.make(env_name)
    
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    
    agent = DQNAgent(state_dim, action_dim)
    
    for episode in range(num_episodes):
        state, _ = env.reset()
        total_reward = 0
        done = False
        truncated = False
        
        while not (done or truncated):
            action = agent.choose_action(state)
            next_state, reward, done, truncated, _ = env.step(action)
            
            agent.buffer.push(state, action, reward, next_state, done)
            loss = agent.train_step()
            
            state = next_state
            total_reward += reward
        
        if (episode + 1) % 50 == 0:
            print(f"Episode {episode+1}/{num_episodes} | "
                  f"Reward: {total_reward} | "
                  f"Epsilon: {agent.epsilon:.3f} | "
                  f"Buffer: {len(agent.buffer)}")
    
    env.close()
    return agent

# Train the DQN agent
agent = train_dqn()
```

---

## 2.2 Proximal Policy Optimization (PPO)

PPO (Schulman et al., 2017) is the most popular policy gradient algorithm. It's stable, easy to implement, and works well across many environments.

### The Problem with Vanilla Policy Gradients

REINFORCE has high variance and can make dangerously large updates. A single bad episode can wipe out all previous learning.

### PPO's Solution: Clipped Objective

PPO limits how much the policy can change in each update:

\[
L^{CLIP}(\theta) = \mathbb{E} \left[ \min \left( r_t(\theta) \hat{A}_t, \, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right]
\]

Where:
- \(r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)}\) is the probability ratio
- \(\hat{A}_t\) is the advantage estimate (how much better is this action vs average?)
- \(\epsilon\) is the clipping parameter (typically 0.1-0.2)

This means: if the new policy is too different from the old one, the update is clipped.

```python
class PPOAgent:
    """
    PPO Agent with actor-critic architecture.
    
    Actor: outputs action probabilities (policy)
    Critic: estimates state value (for computing advantages)
    """
    
    def __init__(self, state_dim, action_dim, lr=3e-4, gamma=0.99, gae_lambda=0.95,
                 clip_epsilon=0.2, k_epochs=4):
        # Actor: policy network
        self.actor = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, action_dim),
            nn.Softmax(dim=-1)
        )
        
        # Critic: value network
        self.critic = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, 1)
        )
        
        self.optimizer = optim.Adam(
            list(self.actor.parameters()) + list(self.critic.parameters()),
            lr=lr
        )
        
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        self.clip_epsilon = clip_epsilon
        self.k_epochs = k_epochs  # Number of optimization epochs per update
    
    def select_action(self, state):
        """Select action and compute log probability."""
        state_tensor = torch.FloatTensor(state)
        probs = self.actor(state_tensor)
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()
        return action.item(), dist.log_prob(action)
    
    def compute_advantage(self, rewards, values, dones, next_value):
        """Compute Generalized Advantage Estimation (GAE)."""
        advantages = []
        gae = 0
        
        values = list(values) + [next_value]
        
        for t in reversed(range(len(rewards))):
            delta = rewards[t] + self.gamma * values[t + 1] * (1 - dones[t]) - values[t]
            gae = delta + self.gamma * self.gae_lambda * (1 - dones[t]) * gae
            advantages.insert(0, gae)
        
        return torch.FloatTensor(advantages)
    
    def update(self, states, actions, old_log_probs, advantages):
        """PPO update: multiple epochs of clipped policy gradient."""
        states_t = torch.FloatTensor(np.array(states))
        actions_t = torch.LongTensor(actions)
        old_log_probs_t = torch.stack(old_log_probs).detach()
        advantages_t = advantages.clone()
        
        # Normalize advantages
        advantages_t = (advantages_t - advantages_t.mean()) / (advantages_t.std() + 1e-8)
        
        for _ in range(self.k_epochs):
            # Current policy
            probs = self.actor(states_t)
            dist = torch.distributions.Categorical(probs)
            new_log_probs = dist.log_prob(actions_t)
            
            # Ratio: new_policy / old_policy
            ratio = (new_log_probs - old_log_probs_t).exp()
            
            # Clipped surrogate objective
            surr1 = ratio * advantages_t
            surr2 = torch.clamp(ratio, 1 - self.clip_epsilon, 1 + self.clip_epsilon) * advantages_t
            actor_loss = -torch.min(surr1, surr2).mean()
            
            # Value loss
            values = self.critic(states_t).squeeze()
            returns = advantages_t + values.detach()  # Approximate returns
            critic_loss = nn.MSELoss()(values, returns)
            
            # Combined loss
            loss = actor_loss + 0.5 * critic_loss
            
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        
        return loss.item()
```

---

## 2.3 A3C / A2C: Parallel Training

**A3C** (Asynchronous Advantage Actor-Critic) uses multiple parallel workers to collect experience simultaneously. **A2C** (Advantage Actor-Critic) is the simpler synchronous version.

### How A2C Works

```
                    ┌─── Worker 1: Collect trajectories ───┐
                    │                                       │
Main Network ◄──────┼─── Worker 2: Collect trajectories ───┼───► Update
(shared params)     │                                       │
                    └─── Worker 3: Collect trajectories ───┘
```

1. Multiple workers run the same policy in different environment copies
2. Each worker collects a batch of experience
3. All experiences are combined into one large batch
4. A single gradient update is applied to the shared network

This is more stable than single-agent PPO and trains faster.

---

## 2.4 RLHF: Aligning LLMs with Human Preferences

**Reinforcement Learning from Human Feedback (RLHF)** is how modern AI assistants (like ChatGPT) are made helpful, honest, and harmless.

### The RLHF Pipeline

```
Step 1: Supervised Fine-Tuning (SFT)
    Pre-trained LLM + human demonstrations → SFT model
    
Step 2: Reward Model Training
    Human preferences (rank responses) → Reward model
    
Step 3: RL Fine-Tuning (PPO)
    SFT model + Reward model → RLHF model
```

### Step 1: Supervised Fine-Tuning

```python
# Fine-tune the base model on high-quality examples
# Input: prompt → Output: ideal response (written by humans)
# Standard language model training (cross-entropy loss)
```

### Step 2: Train a Reward Model

```python
class RewardModel(nn.Module):
    """
    Reward model: scores how good a response is.
    
    Trained on human preferences: given prompt + two responses,
    learn to predict which response humans prefer.
    """
    
    def __init__(self, base_model, hidden_dim=768):
        super().__init__()
        self.base = base_model  # Pre-trained language model
        self.reward_head = nn.Linear(hidden_dim, 1)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.base(input_ids=input_ids, attention_mask=attention_mask)
        # Use the last token's representation
        last_hidden = outputs.last_hidden_state[:, -1, :]
        reward = self.reward_head(last_hidden)
        return reward.squeeze(-1)

# Training: Bradley-Terry loss
# Given (prompt, response_A, response_B) where humans prefer A over B:
# Loss = -log(sigmoid(reward_A - reward_B))
```

### Step 3: RL Fine-Tuning with PPO

```python
def rlhf_training_step(policy_model, reward_model, prompt, ppo_agent):
    """
    One step of RLHF training.
    
    1. Policy generates a response to the prompt
    2. Reward model scores the response
    3. PPO updates the policy to maximize reward
    """
    # Generate response
    response = policy_model.generate(prompt)
    
    # Get reward from reward model
    with torch.no_grad():
        reward = reward_model(response)
    
    # Compute KL penalty (prevent policy from drifting too far from SFT)
    kl_penalty = kl_divergence(policy_model, reference_model, response)
    adjusted_reward = reward - 0.1 * kl_penalty
    
    # PPO update
    ppo_agent.update(response, adjusted_reward)
    
    return adjusted_reward.item()
```

---

## 2.5 Multi-Agent Reinforcement Learning

When multiple agents interact, things get more complex. Each agent's environment is no longer stationary — other agents are also learning!

### Approaches

| Approach | Description | Use Case |
|----------|-------------|----------|
| **Independent Learning** | Each agent learns independently | Simple cooperative tasks |
| **Centralized Training** | Train with global information, execute locally | StarCraft, team games |
| **Communication** | Agents share messages | Coordination tasks |
| **Self-Play** | Agents train against copies of themselves | Competitive games |

### Self-Play: How AlphaGo Worked

```python
# Self-play training loop
for iteration in range(num_iterations):
    # 1. Generate games by playing current model against itself
    games = []
    for _ in range(num_games):
        game = play_game(model, model)  # model vs model
        games.append(game)
    
    # 2. Train on all game data
    for state, action, winner in extract_training_data(games):
        # Reinforcement signal: did this action lead to winning?
        update_model(model, state, action, winner)
    
    # 3. Evaluate against previous version
    win_rate = evaluate(model, previous_model)
    if win_rate > 0.55:  # Only keep if better
        previous_model = copy(model)
```

---

## 2.6 Sim-to-Real Transfer

Training robots in the real world is slow and risky. Instead, we train in simulation and transfer to reality.

### The Sim-to-Real Gap

Simulation is never perfectly realistic. Differences include:
- Friction, mass, and contact dynamics
- Sensor noise and delays
- Visual appearance (for vision-based policies)

### Domain Randomization

The most practical solution: randomize simulation parameters so the policy learns to handle anything.

```python
def randomized_training(env, num_episodes=10000):
    """
    Train with randomized environment parameters.
    
    Each episode, randomize:
    - Friction coefficients
    - Mass of objects
    - Sensor noise levels
    - Initial conditions
    """
    for episode in range(num_episodes):
        # Randomize environment parameters
        env.set_params({
            'friction': np.random.uniform(0.5, 2.0),
            'mass': np.random.uniform(0.8, 1.2),
            'noise': np.random.uniform(0.0, 0.1),
            'gravity': np.random.uniform(-10.5, -9.0),
        })
        
        # Train normally
        train_episode(agent, env)
    
    # The agent learns to be robust to parameter variations
    # When deployed in reality, it handles the "real" parameters
```

---

## 2.7 Algorithm Selection Guide

| Problem Type | Recommended Algorithm | Why |
|-------------|----------------------|-----|
| Small discrete state space | Q-Learning | Simple, guaranteed convergence |
| Large discrete/continuous state | DQN | Handles high-dimensional states |
| Continuous actions | PPO, SAC | DQN can't handle continuous actions |
| Need sample efficiency | SAC, TD3 | Off-policy algorithms |
| Need stability | PPO | Clipped objective prevents large updates |
| Multi-agent | MAPPO, QMIX | Designed for multi-agent settings |
| LLM alignment | PPO + Reward Model | RLHF pipeline |
| Atari games | DQN (with enhancements) | RAINBOW combines 7 improvements |

---

## 2.8 Key Takeaways

1. **DQN** uses experience replay + target networks for stable deep Q-learning
2. **PPO** clips policy updates for stability — the go-to algorithm for most tasks
3. **A2C/A3C** parallelize experience collection for faster training
4. **RLHF** aligns LLMs with human preferences using a reward model + PPO
5. **Multi-agent RL** adds complexity because the environment becomes non-stationary
6. **Sim-to-real** uses domain randomization to bridge the simulation-reality gap
7. **Choose algorithms** based on your state/action space and sample efficiency needs

---

## Exercises

1. **DQN on CartPole:** Implement DQN from scratch and compare with tabular Q-Learning
2. **Target network impact:** Train DQN with and without a target network — observe the difference in stability
3. **PPO on LunarLander:** Train PPO on LunarLander-v2 and achieve an average score of 200+
4. **Reward model:** Create a simple reward model that scores CartPole episodes based on how long the pole stays upright
5. **Self-play:** Implement a simple self-play training loop for Tic-Tac-Toe
6. **Compare algorithms:** Train DQN, PPO, and REINFORCE on the same environment and compare sample efficiency

---

## Resources

- [DQN Paper (Mnih et al., 2015)](https://arxiv.org/abs/1312.5602)
- [PPO Paper (Schulman et al., 2017)](https://arxiv.org/abs/1707.06347)
- [InstructGPT / RLHF Paper (Ouyang et al., 2022)](https://arxiv.org/abs/2203.02155)
- [CleanRL — Single-file RL implementations](https://github.com/vwxyzjn/cleanrl)
- [Spinning Up in Deep RL](https://spinningup.openai.com/)
- [Stable Baselines3 — Production-ready RL](https://stable-baselines3.readthedocs.io/)

---

*Previous: [Chapter 1 — RL Fundamentals](chapter_1_fundamentals.md)*
