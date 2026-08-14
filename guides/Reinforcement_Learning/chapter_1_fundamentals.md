# Chapter 1: Reinforcement Learning Fundamentals

> **Goal:** Understand the mathematical framework of RL (MDPs), implement tabular Q-Learning, and learn policy gradient methods.

---

## 1.1 Markov Decision Processes (MDPs)

An MDP is the mathematical framework for RL. It formalizes the agent-environment interaction:

**Components of an MDP:**

| Symbol | Name | Description |
|--------|------|-------------|
| \(S\) | State space | All possible situations the agent can be in |
| \(A\) | Action space | All possible actions the agent can take |
| \(P(s'|s,a)\) | Transition model | Probability of reaching state \(s'\) after action \(a\) in state \(s\) |
| \(R(s,a,s')\) | Reward function | Immediate reward for the transition |
| \(\gamma\) | Discount factor | How much we care about future rewards (0 to 1) |
| \(\pi(a|s)\) | Policy | The agent's strategy: probability of taking action \(a\) in state \(s\) |

### The Goal

Find the **optimal policy** \(\pi^*\) that maximizes the expected cumulative discounted reward:

\[
\pi^* = \arg\max_\pi \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R_t \right]
\]

### Why Discount?

- \(\gamma = 0\): Agent only cares about immediate reward (myopic)
- \(\gamma = 0.99\): Agent cares about rewards ~100 steps into the future
- \(\gamma = 1\): Agent cares equally about all future rewards (may lead to infinite sums)

---

## 1.2 Value Functions and the Bellman Equations

### State Value Function

How good is it to be in state \(s\) under policy \(\pi\)?

\[
V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R_t \mid S_0 = s \right]
\]

### Action Value Function (Q-Value)

How good is it to take action \(a\) in state \(s\) under policy \(\pi\)?

\[
Q^\pi(s,a) = \mathbb{E}_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R_t \mid S_0 = s, A_0 = a \right]
\]

### The Bellman Equation

The value of a state equals the immediate reward plus the discounted value of the next state:

\[
V^\pi(s) = \sum_a \pi(a|s) \sum_{s'} P(s'|s,a) [R(s,a,s') + \gamma V^\pi(s')]
\]

For the **optimal** policy:

\[
V^*(s) = \max_a \sum_{s'} P(s'|s,a) [R(s,a,s') + \gamma V^*(s')]
\]

---

## 1.3 Tabular Q-Learning

Q-Learning is the simplest RL algorithm. It learns a table (lookup table) of Q-values for every state-action pair.

### The Update Rule

\[
Q(s,a) \leftarrow Q(s,a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s,a)]
\]

Where:
- \(\alpha\) = learning rate (how much to update)
- \(r\) = immediate reward received
- \(\gamma\) = discount factor
- \(s'\) = new state after taking action \(a\)
- \(\max_{a'} Q(s', a')\) = best estimated future value

### Implementation

```python
import numpy as np
import gymnasium as gym

class QLearningAgent:
    """
    Tabular Q-Learning agent.
    
    Learns a Q-table that maps (state, action) pairs to expected rewards.
    Works for environments with discrete, small state spaces.
    """
    
    def __init__(self, state_size, action_size, lr=0.1, gamma=0.99, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.q_table = np.zeros((state_size, action_size))
        self.lr = lr           # Learning rate (alpha)
        self.gamma = gamma     # Discount factor
        self.epsilon = epsilon # Exploration rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
    
    def choose_action(self, state):
        """Epsilon-greedy action selection."""
        if np.random.random() < self.epsilon:
            return np.random.randint(self.q_table.shape[1])  # Explore
        return np.argmax(self.q_table[state])  # Exploit
    
    def update(self, state, action, reward, next_state, done):
        """Update Q-value using the Q-Learning rule."""
        # Q(s,a) += alpha * [r + gamma * max_a' Q(s',a') - Q(s,a)]
        best_next = np.max(self.q_table[next_state]) if not done else 0
        target = reward + self.gamma * best_next
        current = self.q_table[state, action]
        self.q_table[state, action] += self.lr * (target - current)
    
    def decay_epsilon(self):
        """Reduce exploration over time."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)


def train_q_learning(env_name="FrozenLake-v1", num_episodes=10000):
    """Train a Q-Learning agent."""
    env = gym.make(env_name, is_slippery=False)
    
    state_size = env.observation_space.n
    action_size = env.action_space.n
    
    agent = QLearningAgent(state_size, action_size)
    
    rewards_history = []
    
    for episode in range(num_episodes):
        state, _ = env.reset()
        total_reward = 0
        done = False
        truncated = False
        
        while not (done or truncated):
            # Choose action
            action = agent.choose_action(state)
            
            # Take action
            next_state, reward, done, truncated, _ = env.step(action)
            
            # Update Q-table
            agent.update(state, action, reward, next_state, done)
            
            state = next_state
            total_reward += reward
        
        agent.decay_epsilon()
        rewards_history.append(total_reward)
        
        if (episode + 1) % 1000 == 0:
            avg = np.mean(rewards_history[-1000:])
            print(f"Episode {episode+1}/{num_episodes} | "
                  f"Avg Reward (last 1000): {avg:.3f} | "
                  f"Epsilon: {agent.epsilon:.3f}")
    
    env.close()
    return agent, rewards_history

# Train the agent
agent, rewards = train_q_learning()
```

---

## 1.4 Exploration vs Exploitation

This is the central dilemma in RL:

- **Exploitation:** Choose the action you know is best (maximize current reward)
- **Exploration:** Try a random action (might discover something better)

If you only exploit, you might miss the optimal strategy. If you only explore, you never learn.

### Epsilon-Greedy

The simplest strategy: with probability \(\epsilon\), explore; otherwise, exploit.

```python
def epsilon_greedy(q_values, epsilon):
    if np.random.random() < epsilon:
        return np.random.randint(len(q_values))  # Explore
    return np.argmax(q_values)  # Exploit
```

### Upper Confidence Bound (UCB)

A smarter strategy that considers both the value and the uncertainty:

\[
a_t = \arg\max_a \left[ Q(s,a) + c \sqrt{\frac{\ln N(s)}{N(s,a)}} \right]
\]

Where \(N(s)\) is total visits to state \(s\) and \(N(s,a)\) is visits to action \(a\) in state \(s\). Actions tried less often get a bonus.

---

## 1.5 Policy Gradients (REINFORCE)

Instead of learning Q-values, policy gradient methods directly learn the policy \(\pi(a|s)\) — a neural network that outputs action probabilities.

### The REINFORCE Algorithm

1. Run an episode using the current policy
2. For each step, compute the total return \(G_t\) from that point forward
3. Update the policy: increase probability of actions that led to high returns

\[
\nabla_\theta J(\theta) = \mathbb{E} \left[ \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t|s_t) \cdot G_t \right]
\]

### Implementation

```python
import torch
import torch.nn as nn
import torch.optim as optim
import gymnasium as gym
import numpy as np

class PolicyNetwork(nn.Module):
    """Neural network that outputs action probabilities."""
    
    def __init__(self, state_dim, action_dim, hidden_dim=64):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
            nn.Softmax(dim=-1)
        )
    
    def forward(self, state):
        return self.network(state)
    
    def act(self, state):
        """Sample an action from the policy."""
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        probs = self.forward(state_tensor)
        action_dist = torch.distributions.Categorical(probs)
        action = action_dist.sample()
        return action.item(), action_dist.log_prob(action)


def train_reinforce(env_name="CartPole-v1", num_episodes=1000, lr=1e-2, gamma=0.99):
    """
    REINFORCE: Monte Carlo Policy Gradient.
    
    For each episode:
    1. Collect trajectory (states, actions, rewards)
    2. Compute returns (discounted cumulative rewards)
    3. Update policy to favor actions with high returns
    """
    env = gym.make(env_name)
    
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    
    policy = PolicyNetwork(state_dim, action_dim)
    optimizer = optim.Adam(policy.parameters(), lr=lr)
    
    for episode in range(num_episodes):
        state, _ = env.reset()
        
        # Collect trajectory
        log_probs = []
        rewards = []
        done = False
        truncated = False
        
        while not (done or truncated):
            action, log_prob = policy.act(state)
            next_state, reward, done, truncated, _ = env.step(action)
            
            log_probs.append(log_prob)
            rewards.append(reward)
            state = next_state
        
        # Compute discounted returns
        returns = []
        G = 0
        for r in reversed(rewards):
            G = r + gamma * G
            returns.insert(0, G)
        
        # Normalize returns (reduces variance)
        returns = torch.FloatTensor(returns)
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
        # Compute policy gradient loss
        loss = 0
        for log_prob, G in zip(log_probs, returns):
            loss -= log_prob * G  # Negative because we want to maximize
        
        # Update policy
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (episode + 1) % 100 == 0:
            avg_reward = sum(rewards)
            print(f"Episode {episode+1}/{num_episodes} | "
                  f"Return: {sum(rewards):.1f} | "
                  f"Loss: {loss.item():.4f}")
    
    env.close()
    return policy

# Train the policy
policy = train_reinforce()
```

---

## 1.6 Reward Shaping

Sometimes the environment's reward is too sparse (e.g., you only get a reward at the very end). **Reward shaping** adds intermediate rewards to guide learning:

```python
# Example: MountainCar — the environment only gives reward at the top
# Without shaping: agent gets 0 reward for 200 steps, then +1 at the top
# With shaping: reward = distance_to_top improvement at each step

def shaped_reward(state, next_state, original_reward):
    """Add intermediate rewards based on progress."""
    # Reward for moving toward the goal
    progress = next_state[0] - state[0]  # Position improvement
    height_bonus = next_state[1] * 0.1   # Encourage climbing
    
    return original_reward + progress + height_bonus
```

### Potential-Based Reward Shaping

The theoretically safe form of reward shaping uses a potential function \(\Phi(s)\):

\[
F(s, s') = \gamma \Phi(s') - \Phi(s)
\]

This guarantees the optimal policy doesn't change — it just makes learning faster.

---

## 1.7 Key Takeaways

1. **MDPs** formalize the RL problem: states, actions, rewards, transitions
2. **Q-Learning** learns action values in a table — simple but limited to small state spaces
3. **Policy gradients** directly optimize the policy — works with large/continuous spaces
4. **Exploration** is essential — without it, the agent never discovers better strategies
5. **Reward shaping** guides learning when rewards are sparse
6. **Tabular methods** don't scale — we need neural networks for complex environments

---

## Exercises

1. **Q-Learning on FrozenLake:** Train on the 4x4 grid, then try the 8x8 version. How does performance change?
2. **Epsilon comparison:** Train Q-Learning with epsilon = 0.01, 0.1, 0.5, 1.0 and compare convergence speed
3. **REINFORCE on LunarLander:** Modify the REINFORCE code to work on LunarLander-v2 (continuous state space)
4. **Reward shaping:** Add reward shaping to MountainCar-v0 and compare with/without shaping
5. **Discount factor experiment:** Train with gamma = 0.9, 0.99, 0.999 and observe how the agent's behavior changes

---

*Next: [Chapter 2 — Deep RL and Advanced Topics](chapter_2_deep_rl.md)*
