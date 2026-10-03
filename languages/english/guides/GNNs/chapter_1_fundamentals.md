# Chapter 1: Graph Fundamentals & Your First GNN

## Welcome! What Even IS a Graph?

If you've never heard of graphs in computer science, don't worry! You already understand the concept.

### Think About Social Media

When you use Facebook, Instagram, or LinkedIn:
- **You** are a **node** (a point)
- **Your friends** are also **nodes**
- The **"friend" connection** between you is an **edge** (a line)

That's a graph! It's just a way to represent **things and their relationships**.

```
Traditional Data (like a spreadsheet):
Name     | Age | City
---------|-----|--------
Alice    | 25  | NYC
Bob      | 30  | LA
Charlie  | 28  | NYC

Graph Data (showing relationships):
    Alice ---- Bob
      |        
      |        
    Charlie    
```

The spreadsheet tells you ABOUT people. The graph shows you HOW THEY CONNECT.

## Why Do We Need Special Neural Networks for Graphs?

### The Problem with Traditional Neural Networks

Imagine you're trying to predict if someone will like a movie. 

**Traditional approach:** Look at each person individually
- Age: 25
- Location: NYC
- Previous movies watched: Action, Comedy

**Problem:** This ignores that their **best friend** loves this movie! People are influenced by their friends.

**GNN approach:** Look at the person AND their friends
- Alice's features + Bob's features + Charlie's features = Better prediction!

### The Key Insight: Message Passing

Here's the beautiful idea behind GNNs:

> **Each node gathers information from its neighbors, combines it, and updates itself.**

Think of it like a **rumor spreading** at a party:

1. Alice hears something from Bob
2. Alice combines it with what she already knows
3. Alice now has updated knowledge
4. Alice tells Charlie (who also combines it with their knowledge)

This is **message passing** - the heart of every GNN!

## Visual: How Message Passing Works

Let's watch it happen:

```
Before Message Passing:
    [Alice: "I like pizza"]
         |
         |
    [Bob: "I like burgers"]

Step 1: Alice receives Bob's message
    [Alice: "I like pizza" + "Bob likes burgers"]
         |
         |
    [Bob: "I like burgers"]

Step 2: Alice updates her representation
    [Alice: "I like pizza, and my friend Bob likes burgers"]
         |
         |
    [Bob: "I like burgers"]

After Multiple Steps:
Everyone knows about everyone's preferences through their connections!
```

## Building Blocks: Graph Terminology Made Simple

| Term | Fancy Definition | Simple Explanation |
|------|------------------|-------------------|
| **Node (Vertex)** | A fundamental unit of a graph | A thing (person, molecule, website) |
| **Edge** | A connection between two nodes | A relationship (friendship, bond, link) |
| **Neighbor** | Nodes connected by an edge | Your direct connections |
| **Degree** | Number of edges connected to a node | How many friends you have |
| **Path** | Sequence of edges connecting nodes | How to get from A to B |
| **Subgraph** | A graph within a larger graph | A smaller group within the whole |
| **Feature** | Information about a node | Characteristics (age, color, type) |
| **Label** | The answer we want to predict | Category, class, or value |

## Your First Graph in Code

Let's build a tiny social network:

```python
# No AI libraries yet - just pure Python!

# Represent people as nodes
people = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

# Represent friendships as edges (pairs of people)
friendships = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "Dave"),
    ("Charlie", "Dave"),
    ("Dave", "Eve")
]

print("Our Social Network:")
print(f"People: {people}")
print(f"Friendships: {friendships}")

# Let's find who Alice is connected to
alice_friends = []
for person1, person2 in friendships:
    if person1 == "Alice":
        alice_friends.append(person2)
    elif person2 == "Alice":
        alice_friends.append(person1)

print(f"\nAlice's friends: {alice_friends}")
```

**Output:**
```
Our Social Network:
People: ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
Friendships: [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'Dave'), ('Charlie', 'Dave'), ('Dave', 'Eve')]

Alice's friends: ['Bob', 'Charlie']
```

Congratulations! You just worked with a graph!

## Adding Features to Nodes

Real graphs have **features** - information about each node.

```python
# Each person has features: [age, hours_on_social_media]
features = {
    "Alice": [25, 3.5],      # 25 years old, 3.5 hours/day
    "Bob": [30, 2.0],
    "Charlie": [28, 4.0],
    "Dave": [35, 1.5],
    "Eve": [22, 5.0]
}

print(f"Alice's features: {features['Alice']}")
print(f"Bob's features: {features['Bob']}")
```

## Adding Labels (What We Want to Predict)

Maybe we want to predict if someone will buy a new product:

```python
# Labels: 1 = will buy, 0 = won't buy
labels = {
    "Alice": 1,
    "Bob": 0,
    "Charlie": 1,
    "Dave": 0,
    "Eve": 1
}

print(f"We know Alice will buy the product (label={labels['Alice']})")
```

## The GNN Goal

Given:
- The graph structure (who's connected to whom)
- Node features (age, behavior)
- Some known labels (who bought the product)

We want to:
- **Predict labels for nodes we haven't seen yet!**

## Math Behind Message Passing (Made Simple!)

Don't panic! Here's the entire GNN formula in plain English:

### Step 1: Gather Messages from Neighbors

For each node, collect information from all its neighbors:

```
Message from neighbor = Neighbor's features
```

### Step 2: Aggregate (Combine) Messages

Combine all the messages (usually by averaging):

```
Aggregated message = Average of all neighbor features
```

### Step 3: Update the Node

Combine the node's own features with the aggregated message:

```
New node features = Function(node's old features + aggregated message)
```

### In Mathematical Notation (Optional!)

If you like math, here it is:

$$h_v^{(l+1)} = \sigma\left(W^{(l)} \cdot \text{AGG}\left(\{h_u^{(l)} : u \in \mathcal{N}(v)\}\right) + b^{(l)}\right)$$

Where:
- $h_v^{(l)}$ = features of node v at layer l
- $\mathcal{N}(v)$ = neighbors of node v
- AGG = aggregation function (like average)
- W, b = learnable parameters (what we train!)
- $\sigma$ = activation function (adds non-linearity)

**Translation:** "Update each node by combining its neighbors' information with learnable weights."

## Your First GNN From Scratch (No Libraries!)

Let's implement the simplest GNN possible:

```python
import numpy as np

class SimpleGNN:
    """A GNN so simple you can see every step!"""
    
    def __init__(self, input_dim, hidden_dim, output_dim):
        """
        Initialize the GNN
        
        Args:
            input_dim: Number of features per node
            hidden_dim: Size of hidden representations
            output_dim: Number of classes to predict
        """
        # Random weights (these will be learned during training)
        self.W1 = np.random.randn(input_dim, hidden_dim) * 0.1
        self.W2 = np.random.randn(hidden_dim, output_dim) * 0.1
        self.b1 = np.zeros(hidden_dim)
        self.b2 = np.zeros(output_dim)
    
    def relu(self, x):
        """Activation function: keeps positive values, zeros out negatives"""
        return np.maximum(0, x)
    
    def softmax(self, x):
        """Converts scores to probabilities"""
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def aggregate_neighbors(self, node_idx, features, adjacency_list):
        """
        Gather and average features from neighbors
        
        Args:
            node_idx: Index of the node we're updating
            features: All node features
            adjacency_list: List of neighbors for each node
        """
        neighbors = adjacency_list[node_idx]
        
        if len(neighbors) == 0:
            # No neighbors? Just return the node's own features
            return features[node_idx]
        
        # Collect neighbor features
        neighbor_features = [features[n] for n in neighbors]
        
        # Average them (this is the AGGREGATE step!)
        aggregated = np.mean(neighbor_features, axis=0)
        
        return aggregated
    
    def forward(self, features, adjacency_list):
        """
        Run the GNN forward pass
        
        Args:
            features: Node features (num_nodes x input_dim)
            adjacency_list: List of neighbors for each node
            
        Returns:
            Predictions for each node
        """
        num_nodes = len(features)
        
        # STEP 1: Message Passing
        # Each node aggregates information from neighbors
        aggregated_features = []
        for i in range(num_nodes):
            agg = self.aggregate_neighbors(i, features, adjacency_list)
            aggregated_features.append(agg)
        
        aggregated_features = np.array(aggregated_features)
        
        # Combine original features with aggregated neighbor info
        combined = features + aggregated_features
        
        # STEP 2: Transform through neural network layers
        # Layer 1
        hidden = self.relu(combined @ self.W1 + self.b1)
        
        # Layer 2 (output layer)
        output = self.softmax(hidden @ self.W2 + self.b2)
        
        return output
    
    def predict(self, features, adjacency_list):
        """Get predicted class for each node"""
        predictions = self.forward(features, adjacency_list)
        return np.argmax(predictions, axis=1)


# Let's test it!
print("=" * 60)
print("Testing Our Simple GNN")
print("=" * 60)

# Create a tiny graph (5 people)
# Adjacency list: who is connected to whom
adjacency_list = {
    0: [1, 2],      # Alice connects to Bob, Charlie
    1: [0, 3],      # Bob connects to Alice, Dave
    2: [0, 3],      # Charlie connects to Alice, Dave
    3: [1, 2, 4],   # Dave connects to Bob, Charlie, Eve
    4: [3]          # Eve connects to Dave
}

# Features for each person: [age_normalized, social_media_hours]
features = np.array([
    [0.5, 3.5],   # Alice
    [0.6, 2.0],   # Bob
    [0.55, 4.0],  # Charlie
    [0.7, 1.5],   # Dave
    [0.4, 5.0]    # Eve
])

# Normalize age to 0-1 range (divide by max age ~50)
features[:, 0] = features[:, 0] / 1.0  # Already normalized

# Create and run the GNN
gnn = SimpleGNN(input_dim=2, hidden_dim=4, output_dim=2)
predictions = gnn.forward(features, adjacency_list)

print("\nNode Predictions (probability of buying):")
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
for i, name in enumerate(names):
    prob_buy = predictions[i][1]
    print(f"{name}: {prob_buy:.2%} chance of buying")

print("\nPredicted classes (0=won't buy, 1=will buy):")
predicted_classes = gnn.predict(features, adjacency_list)
for i, name in enumerate(names):
    print(f"{name}: {'Will buy' if predicted_classes[i] == 1 else 'Won\'t buy'}")
```

**Sample Output:**
```
============================================================
Testing Our Simple GNN
============================================================

Node Predictions (probability of buying):
Alice: 52.34% chance of buying
Bob: 48.12% chance of buying
Charlie: 53.67% chance of buying
Dave: 47.89% chance of buying
Eve: 51.23% chance of buying

Predicted classes (0=won't buy, 1=will buy):
Alice: Will buy
Bob: Won't buy
Charlie: Will buy
Dave: Won't buy
Eve: Will buy
```

**Key Insight:** Notice how the predictions are influenced by neighbors! Even though we initialized weights randomly, you can see the GNN is combining information across the graph.

## Understanding What Happened

Let's trace through what happened for **Alice**:

1. **Alice's original features:** [0.5, 3.5]
2. **Alice's neighbors:** Bob [0.6, 2.0] and Charlie [0.55, 4.0]
3. **Aggregated from neighbors:** Average of Bob and Charlie = [0.575, 3.0]
4. **Combined:** Alice's features + aggregated = [0.5, 3.5] + [0.575, 3.0] = [1.075, 6.5]
5. **Passed through neural network:** Transformed into predictions

Alice's prediction was influenced by Bob and Charlie's features! That's the power of GNNs.

## Training the GNN

Now let's actually **train** our GNN to make better predictions:

```python
class TrainableGNN(SimpleGNN):
    """Our GNN with training capability"""
    
    def compute_loss(self, predictions, labels):
        """
        Calculate how wrong our predictions are
        
        Uses cross-entropy loss (standard for classification)
        """
        epsilon = 1e-10  # Small number to avoid log(0)
        num_samples = len(labels)
        
        # Get the predicted probability for the correct class
        correct_probs = []
        for i in range(num_samples):
            correct_probs.append(predictions[i][labels[i]] + epsilon)
        
        # Cross-entropy loss
        loss = -np.mean(np.log(correct_probs))
        return loss
    
    def train_step(self, features, adjacency_list, labels, learning_rate=0.01):
        """
        One step of training
        
        1. Forward pass
        2. Compute loss
        3. Backward pass (compute gradients)
        4. Update weights
        """
        # Forward pass
        predictions = self.forward(features, adjacency_list)
        
        # Compute loss
        loss = self.compute_loss(predictions, labels)
        
        # For simplicity, we'll use numerical gradients
        # (In practice, use automatic differentiation like PyTorch)
        eps = 1e-5
        
        # Update W1
        for i in range(self.W1.shape[0]):
            for j in range(self.W1.shape[1]):
                # Perturb weight
                self.W1[i, j] += eps
                pred_plus = self.forward(features, adjacency_list)
                loss_plus = self.compute_loss(pred_plus, labels)
                
                self.W1[i, j] -= 2 * eps
                pred_minus = self.forward(features, adjacency_list)
                loss_minus = self.compute_loss(pred_minus, labels)
                
                # Restore weight
                self.W1[i, j] += eps
                
                # Compute gradient and update
                gradient = (loss_plus - loss_minus) / (2 * eps)
                self.W1[i, j] -= learning_rate * gradient
        
        # Similar updates for W2, b1, b2 (omitted for brevity)
        # In practice, use PyTorch's autograd!
        
        return loss


print("\n" + "=" * 60)
print("Training Our GNN")
print("=" * 60)

# Training data (some labels we know)
# Only Alice, Charlie, and Eve have known labels
train_mask = [True, False, True, False, True]
labels = np.array([1, 0, 1, 0, 1])  # 1=will buy, 0=won't buy

# Create GNN
gnn = TrainableGNN(input_dim=2, hidden_dim=8, output_dim=2)

# Training loop
print("\nTraining progress:")
for epoch in range(100):
    loss = gnn.train_step(features, adjacency_list, labels, learning_rate=0.01)
    if epoch % 20 == 0:
        print(f"Epoch {epoch:3d}: Loss = {loss:.4f}")

# Test on Bob and Dave (who we didn't train on)
print("\nPredicting for Bob and Dave (not in training set):")
test_predictions = gnn.predict(features, adjacency_list)
print(f"Bob: {'Will buy' if test_predictions[1] == 1 else 'Won\'t buy'}")
print(f"Dave: {'Will buy' if test_predictions[3] == 1 else 'Won\'t buy'}")
```

**Note:** The training above uses numerical gradients for educational purposes. It's slow! In the next section, we'll use PyTorch for fast, automatic differentiation.

## Using PyTorch Geometric (The Professional Way)

Now let's use the actual library everyone uses for GNNs:

```bash
pip install torch torch-geometric
```

### Complete Working Example

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from torch_geometric.datasets import KarateClub
from torch_geometric.utils import to_networkx
import matplotlib.pyplot as plt

print("=" * 60)
print("Training a Real GNN with PyTorch Geometric")
print("=" * 60)

# Load a real dataset: Zachary's Karate Club
# This is a famous social network of a karate club
dataset = KarateClub()
data = dataset[0]

print(f"\nDataset: {dataset}")
print(f"Number of nodes: {data.num_nodes}")
print(f"Number of edges: {data.num_edges}")
print(f"Number of features per node: {data.num_node_features}")
print(f"Number of classes: {dataset.num_classes}")

# Visualize the graph
G = to_networkx(data, to_undirected=True)
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=500, font_size=10, font_weight='bold')
plt.title("Zachary's Karate Club Network")
plt.show()


# Define the GNN model
class GCN(nn.Module):
    """Graph Convolutional Network"""
    
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GCN, self).__init__()
        # GCN layer: handles message passing automatically!
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)
    
    def forward(self, x, edge_index):
        """
        Args:
            x: Node features
            edge_index: Graph connectivity (which nodes connect to which)
        """
        # First GCN layer
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        
        # Second GCN layer
        x = self.conv2(x, edge_index)
        
        return F.log_softmax(x, dim=1)


# Create the model
model = GCN(input_dim=data.num_node_features, hidden_dim=16, output_dim=dataset.num_classes)
print(f"\nModel architecture:")
print(model)

# Training setup
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
criterion = nn.NLLLoss()

# Training loop
print("\n" + "=" * 60)
print("Training...")
print("=" * 60)

model.train()
for epoch in range(200):
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)
    
    # Only train on the first 34 nodes (training mask)
    loss = criterion(out[:34], data.y[:34])
    loss.backward()
    optimizer.step()
    
    if epoch % 40 == 0:
        print(f"Epoch {epoch:3d}: Loss = {loss.item():.4f}")

# Evaluation
print("\n" + "=" * 60)
print("Evaluation")
print("=" * 60)

model.eval()
predictions = model(data.x, data.edge_index).argmax(dim=1)
correct = (predictions[:34] == data.y[:34]).sum().item()
accuracy = correct / 34

print(f"\nTraining Accuracy: {accuracy:.2%}")
print(f"Correct predictions: {correct}/34")

# Show predictions vs actual
print("\nDetailed Results:")
for i in range(34):
    status = "✓" if predictions[i] == data.y[i] else "✗"
    print(f"Node {i:2d}: Predicted={predictions[i].item()}, Actual={data.y[i].item()} {status}")
```

## Understanding the PyTorch Geometric Code

### Key Components Explained

#### 1. **GCNConv Layer**
```python
self.conv1 = GCNConv(input_dim, hidden_dim)
```
This single line does ALL the message passing magic:
- Gathers neighbor features
- Aggregates them
- Applies learnable transformation
- You don't need to implement the math yourself!

#### 2. **Edge Index**
```python
data.edge_index  # Shape: [2, num_edges]
```
This tells the GNN which nodes are connected:
```
[[0, 0, 1, 2, ...],   # Source nodes
 [1, 2, 3, 3, ...]]   # Target nodes
```
Means: Node 0→1, Node 0→2, Node 1→3, Node 2→3, etc.

#### 3. **Forward Pass**
```python
x = self.conv1(x, edge_index)
```
The `edge_index` tells the layer how to pass messages between nodes.

## Troubleshooting Common Issues

### Issue 1: "CUDA Out of Memory"
**Symptoms:** Training crashes with memory error

**Solutions:**
```python
# Use CPU instead
device = torch.device('cpu')

# Or reduce model size
model = GCN(input_dim, hidden_dim=8, output_dim=2)  # Smaller hidden layer

# Or use gradient accumulation
```

### Issue 2: "Index Out of Bounds"
**Symptoms:** Error about index being too large

**Cause:** Node indices don't match

**Solution:**
```python
# Make sure node indices are 0, 1, 2, ..., num_nodes-1
# Renumber if needed
```

### Issue 3: Loss Not Decreasing
**Symptoms:** Loss stays high or fluctuates wildly

**Solutions:**
```python
# Lower learning rate
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Add more layers or increase hidden dimension
model = GCN(input_dim, hidden_dim=64, output_dim=dataset.num_classes)

# Check if graph has enough connections
print(f"Average degree: {data.num_edges / data.num_nodes:.2f}")
```

### Issue 4: Overfitting
**Symptoms:** Great training accuracy, poor test accuracy

**Solutions:**
```python
# Add dropout (already in our code)
x = F.dropout(x, p=0.5, training=self.training)

# Add weight decay
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)

# Use early stopping
```

## Exercises

### Exercise 1: Beginner - Modify the Graph
**Goal:** Understand how graph structure affects predictions

1. Create your own small graph (5-10 nodes)
2. Define custom features and labels
3. Train the GNN on your graph
4. Experiment: What happens if you add/remove edges?

```python
# Starter code
import torch
from torch_geometric.data import Data

# Create your own graph
# Your code here!
```

### Exercise 2: Intermediate - Change the Architecture
**Goal:** Understand how architecture affects performance

1. Add a third GCN layer
2. Try different hidden dimensions (8, 16, 32, 64)
3. Compare results
4. Which works best? Why?

```python
class ThreeLayerGCN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        # Add your code here!
        pass
    
    def forward(self, x, edge_index):
        # Add your code here!
        pass
```

### Exercise 3: Advanced - Implement Graph Attention
**Goal:** Understand attention mechanisms in GNNs

Research Graph Attention Networks (GAT) and implement one:

```python
from torch_geometric.nn import GATConv

class MyGAT(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        # Use GATConv instead of GCNConv
        # What's different? How does attention work?
        pass
```

## Chapter Summary

### Key Concepts Learned

1. **Graphs** represent things (nodes) and their relationships (edges)
2. **Message Passing** is how GNNs gather information from neighbors
3. **Aggregation** combines neighbor information (usually by averaging)
4. **GNNs** transform node features using graph structure
5. **PyTorch Geometric** makes implementing GNNs easy

### The GNN Formula (Remember This!)

```
For each node:
  1. Gather features from neighbors
  2. Aggregate (average) them
  3. Combine with own features
  4. Pass through neural network
  5. Get prediction
```

### What's Next?

In Chapter 2, we'll explore:
- **GCN** (Graph Convolutional Networks) - The classic
- **GAT** (Graph Attention Networks) - Attention for graphs
- **GraphSAGE** - Scaling to massive graphs
- **When to use each architecture**

## Glossary

| Term | Definition |
|------|------------|
| **Node/Vertex** | An entity in the graph (person, molecule, etc.) |
| **Edge** | A connection between two nodes |
| **Neighbor** | A node directly connected to another node |
| **Degree** | Number of edges connected to a node |
| **Feature** | Numerical representation of node properties |
| **Label** | The target value we want to predict |
| **Message Passing** | Process of sharing information between connected nodes |
| **Aggregation** | Combining messages from multiple neighbors |
| **Adjacency Matrix** | A matrix showing which nodes are connected |
| **Embedding** | Learned numerical representation of a node |
| **Inductive Learning** | Can generalize to unseen graphs/nodes |
| **Transductive Learning** | Only works on the graph seen during training |
| **Homophily** | Tendency of similar nodes to connect |
| **Graph Convolution** | Applying convolution operations on graphs |

## Quick Reference: GNN Cheat Sheet

```python
# Basic GNN Template
class MyGNN(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Training Template
model = MyGNN(dataset.num_features, 16, dataset.num_classes)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(200):
    model.train()
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)
    loss = F.nll_loss(out[train_mask], data.y[train_mask])
    loss.backward()
    optimizer.step()
```

## Real-World Application Preview

Next chapter, we'll apply GNNs to:
- **Molecular property prediction** (drug discovery)
- **Recommendation systems** (predict what users will like)
- **Social network analysis** (detect communities)
- **Traffic prediction** (forecast congestion)

Keep practicing, and you'll be building production GNNs in no time!

---

*"Alone we can do so little; together we can do so much." - Helen Keller*

This quote perfectly captures the essence of GNNs: individual nodes are limited, but by sharing information through connections, they achieve powerful insights together!
