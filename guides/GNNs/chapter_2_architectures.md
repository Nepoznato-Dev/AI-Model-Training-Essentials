# Chapter 2: GNN Architectures Deep Dive

## Introduction

Welcome back! In Chapter 1, you learned what graphs are and built your first Graph Neural Network from scratch. You discovered how messages flow between nodes, how to aggregate information from neighbors, and why graphs are perfect for connected data.

Now, in this chapter, we'll explore the **major GNN architectures** that researchers and engineers use in real-world applications. Think of this like learning different types of vehicles:

- **GCN (Graph Convolutional Network)** - Like a reliable sedan: simple, effective, works well for most tasks
- **GAT (Graph Attention Network)** - Like a sports car with adaptive suspension: pays attention to important neighbors
- **GraphSAGE** - Like an off-road vehicle: handles massive graphs by sampling neighbors
- **GIN (Graph Isomorphism Network)** - Like a precision instrument: theoretically powerful for graph classification
- **MPNN (Message Passing Neural Network)** - Like a customizable framework: flexible design pattern

By the end of this chapter, you'll know:
- ✅ How each architecture works internally
- ✅ When to use which architecture
- ✅ How to implement each one in PyTorch Geometric
- ✅ The strengths and weaknesses of each approach
- ✅ Real-world scenarios where each shines

Let's dive in!

---

## 2.1 Graph Convolutional Networks (GCN)

### What is a GCN?

The **Graph Convolutional Network (GCN)**, introduced by Kipf and Welling in 2017, is one of the most popular and influential GNN architectures. It's often the **first architecture people try** when working with graph data because it's:

- **Simple** - Easy to understand and implement
- **Effective** - Works well on many tasks
- **Efficient** - Fast to train and inference
- **Well-understood** - Lots of research and best practices

### The Intuition Behind GCN

Remember from Chapter 1 how we said GNNs work by passing messages between neighbors? GCN does this in a very specific way:

**GCN Rule**: Each node updates its features by taking a **weighted average** of its neighbors' features, then applying a neural network transformation.

Think of it like this: Imagine you're at a party trying to understand the mood of the room. You:
1. Talk to everyone near you (your neighbors)
2. Average their opinions (aggregate)
3. Form your own updated opinion (transform)

That's exactly what GCN does!

### The Math (Made Simple)

The GCN layer formula looks scary but let's break it down:

```
H^(l+1) = σ(D̃^(-1/2) Ã D̃^(-1/2) H^(l) W^(l))
```

Don't panic! Let's decode this step-by-step:

| Symbol | Meaning | Simple Explanation |
|--------|---------|-------------------|
| `H^(l)` | Node features at layer l | Current understanding of each node |
| `H^(l+1)` | Node features at layer l+1 | Updated understanding after talking to neighbors |
| `Ã` | Adjacency matrix with self-loops | Who is connected to whom (including yourself) |
| `D̃` | Degree matrix | How many connections each node has |
| `D̃^(-1/2) Ã D̃^(-1/2)` | Normalized adjacency | Fair averaging (prevents popular nodes from dominating) |
| `W^(l)` | Learnable weights | The "brain" that learns what features matter |
| `σ` | Activation function (ReLU) | Adds non-linearity so we can learn complex patterns |

### Visualizing GCN Message Passing

```
Before GCN Layer:
Node A: [0.5, 0.3, 0.8]
Node B: [0.2, 0.9, 0.1]
Node C: [0.7, 0.4, 0.6]

Connections: A-B, B-C, A-C

Step 1: Gather Neighbors
Node A sees: A(self), B, C
Node B sees: B(self), A, C
Node C sees: C(self), A, B

Step 2: Normalize and Average
Node A new = normalize([A, B, C]) × Weights
Node B new = normalize([B, A, C]) × Weights
Node C new = normalize([C, A, B]) × Weights

Step 3: Apply Non-linearity
Final output = ReLU(averaged features)
```

### Implementing GCN from Scratch

Let's build a GCN layer from scratch to truly understand it:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GCNLayer(nn.Module):
    """
    A single Graph Convolutional Network layer.
    
    This implements: H' = σ(D^(-1/2) A D^(-1/2) H W)
    """
    def __init__(self, in_features, out_features, bias=True):
        super(GCNLayer, self).__init__()
        
        # Learnable weight matrix
        self.weight = nn.Parameter(torch.FloatTensor(in_features, out_features))
        
        # Optional bias term
        if bias:
            self.bias = nn.Parameter(torch.FloatTensor(out_features))
        else:
            self.register_parameter('bias', None)
        
        # Initialize weights
        self.reset_parameters()
    
    def reset_parameters(self):
        """Initialize weights using Xavier initialization"""
        nn.init.xavier_uniform_(self.weight)
        if self.bias is not None:
            nn.init.zeros_(self.bias)
    
    def forward(self, x, adj_matrix):
        """
        Forward pass through GCN layer.
        
        Args:
            x: Node features [num_nodes, in_features]
            adj_matrix: Adjacency matrix [num_nodes, num_nodes]
        
        Returns:
            Updated node features [num_nodes, out_features]
        """
        # Step 1: Add self-loops to adjacency matrix
        # (I + A) - this ensures each node considers its own features
        num_nodes = x.shape[0]
        identity = torch.eye(num_nodes, device=x.device)
        adj_with_loops = adj_matrix + identity
        
        # Step 2: Compute degree matrix
        # D = diagonal matrix where D[i,i] = sum of row i in A
        degree = torch.diag(adj_with_loops.sum(dim=1))
        
        # Step 3: Compute normalized adjacency
        # D^(-1/2) A D^(-1/2)
        degree_inv_sqrt = torch.pow(degree, -0.5)
        degree_inv_sqrt = torch.nan_to_num(degree_inv_sqrt, nan=0.0)  # Handle isolated nodes
        
        normalized_adj = degree_inv_sqrt @ adj_with_loops @ degree_inv_sqrt
        
        # Step 4: Apply GCN formula
        # H' = σ(A_norm H W)
        support = x @ self.weight  # Linear transformation
        output = normalized_adj @ support  # Message passing
        
        # Add bias if present
        if self.bias is not None:
            output = output + self.bias
        
        # Apply activation function
        output = F.relu(output)
        
        return output


class GCN(nn.Module):
    """
    Multi-layer Graph Convolutional Network.
    """
    def __init__(self, in_features, hidden_features, out_features, num_layers=2):
        super(GCN, self).__init__()
        
        # Build layers
        layers = []
        
        # First layer
        layers.append(GCNLayer(in_features, hidden_features))
        
        # Hidden layers
        for _ in range(num_layers - 2):
            layers.append(GCNLayer(hidden_features, hidden_features))
        
        # Output layer (no activation)
        layers.append(GCNLayer(hidden_features, out_features, bias=False))
        
        self.layers = nn.ModuleList(layers)
    
    def forward(self, x, adj_matrix):
        """Forward pass through all layers"""
        for i, layer in enumerate(self.layers):
            x = layer(x, adj_matrix)
            # Don't apply ReLU on last layer
            if i < len(self.layers) - 1:
                x = F.relu(x)
        
        return x


# Example usage
if __name__ == "__main__":
    # Create a simple graph
    num_nodes = 5
    in_features = 16
    hidden_features = 32
    out_features = 3  # e.g., 3 classes
    
    # Random node features
    x = torch.randn(num_nodes, in_features)
    
    # Random adjacency matrix (connected graph)
    adj = torch.rand(num_nodes, num_nodes)
    adj = (adj > 0.5).float()  # Binary connections
    adj = (adj + adj.T) / 2  # Make symmetric
    adj = (adj > 0.5).float()  # Binary again
    
    # Create and run GCN
    gcn = GCN(in_features, hidden_features, out_features)
    output = gcn(x, adj)
    
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Output (node embeddings): \n{output}")
```

### Training a GCN for Node Classification

Now let's train a GCN on a real task - classifying nodes in a graph:

```python
import torch.optim as optim
from torch_geometric.datasets import Planetoid
from torch_geometric.utils import to_dense_adj

# Load Cora dataset (citation network)
dataset = Planetoid(root='/tmp/Cora', name='Cora')
data = dataset[0]

# Convert sparse edge index to dense adjacency matrix
adj_matrix = to_dense_adj(data.edge_index)[0]

# Create model
model = GCN(
    in_features=data.num_features,
    hidden_features=64,
    out_features=dataset.num_classes,
    num_layers=2
)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)

# Training loop
num_epochs = 200
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    
    # Forward pass
    output = model(data.x, adj_matrix)
    
    # Only compute loss on training nodes
    loss = criterion(output[data.train_mask], data.y[data.train_mask])
    
    # Backward pass
    loss.backward()
    optimizer.step()
    
    # Evaluate every 20 epochs
    if (epoch + 1) % 20 == 0:
        model.eval()
        with torch.no_grad():
            output = model(data.x, adj_matrix)
            predictions = output.argmax(dim=1)
            
            # Calculate accuracy on test set
            correct = predictions[data.test_mask] == data.y[data.test_mask]
            accuracy = correct.sum().item() / data.test_mask.sum().item()
            
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.4f}, Test Acc: {accuracy:.4f}")
```

### When to Use GCN

**✅ Good for:**
- Small to medium-sized graphs (< 100k nodes)
- Homophilic graphs (similar nodes connect)
- Node classification tasks
- When you need a strong baseline
- Semi-supervised learning

**❌ Not ideal for:**
- Very large graphs (memory intensive)
- Heterophilic graphs (dissimilar nodes connect)
- Dynamic graphs (changing structure)
- When you need interpretability

---

## 2.2 Graph Attention Networks (GAT)

### What is a GAT?

The **Graph Attention Network (GAT)**, introduced by Veličković et al. in 2018, adds a powerful twist to message passing: **attention mechanisms**.

While GCN treats all neighbors equally (simple averaging), GAT learns to **pay different attention** to different neighbors. Some neighbors matter more than others!

### The Intuition Behind GAT

Imagine you're deciding what movie to watch:
- Your film buff friend's opinion matters a lot
- Your friend who hates movies matters less
- Your partner's opinion matters the most

GAT works the same way - it learns **which neighbors to trust more** for each node.

### Key Advantages Over GCN

1. **Adaptive weighting**: Learns importance of each neighbor
2. **No matrix operations**: Works on sparse graphs efficiently
3. **Inductive capability**: Can generalize to unseen graphs
4. **Interpretability**: Attention weights show which edges matter

### The Math (Attention Mechanism)

GAT uses **self-attention** to compute weights:

```
α_ij = exp(LeakyReLU(a^T [Wh_i || Wh_j])) / Σ_k exp(LeakyReLU(a^T [Wh_i || Wh_k]))
```

Let's decode this:

| Component | Purpose |
|-----------|---------|
| `Wh_i`, `Wh_j` | Transform node features |
| `[||]` | Concatenate two vectors |
| `a^T` | Learnable attention vector |
| `LeakyReLU` | Activation function |
| `exp()` and denominator | Softmax normalization |

The result: `α_ij` tells us how much node `i` should pay attention to node `j`.

### Multi-Head Attention

Just like Transformers (Chapter X), GAT uses **multi-head attention**:

- Run multiple attention mechanisms in parallel
- Each head learns different relationships
- Combine results (concatenate or average)

This makes the model more robust and expressive!

### Visualizing GAT Attention

```
Node A has 3 neighbors: B, C, D

Without Attention (GCN):
A takes: 33% from B, 33% from C, 33% from D

With Attention (GAT):
A learns: 60% from B (important!), 10% from C (not relevant), 30% from D (somewhat useful)

Attention weights are learned during training!
```

### Implementing GAT from Scratch

```python
class GATLayer(nn.Module):
    """
    Graph Attention Network layer.
    
    Implements attention-based message passing.
    """
    def __init__(self, in_features, out_features, num_heads=1, dropout=0.6, concat=True):
        super(GATLayer, self).__init__()
        
        self.num_heads = num_heads
        self.out_features = out_features
        self.concat = concat  # Whether to concatenate heads or average
        
        # Learnable weight matrix for each head
        self.W = nn.Parameter(torch.FloatTensor(num_heads, in_features, out_features))
        
        # Attention mechanism for each head
        self.a = nn.Parameter(torch.FloatTensor(num_heads, 2 * out_features, 1))
        
        # LeakyReLU activation
        self.leaky_relu = nn.LeakyReLU(negative_slope=0.2)
        
        # Dropout for regularization
        self.dropout = nn.Dropout(dropout)
        
        self.reset_parameters()
    
    def reset_parameters(self):
        """Initialize parameters"""
        nn.init.xavier_uniform_(self.W)
        nn.init.xavier_uniform_(self.a)
    
    def forward(self, x, edge_index):
        """
        Forward pass through GAT layer.
        
        Args:
            x: Node features [num_nodes, in_features]
            edge_index: Edge list [2, num_edges]
        
        Returns:
            Updated node features [num_nodes, out_features * num_heads] or [num_nodes, out_features]
        """
        num_nodes = x.shape[0]
        
        # Transform features for each head
        # Shape: [num_heads, num_nodes, out_features]
        h = torch.matmul(x.unsqueeze(0), self.W)
        
        # Compute attention coefficients
        # For each edge (i, j), compute attention score
        row, col = edge_index  # Source and target nodes
        
        # Concatenate source and target features
        # Shape: [num_heads, num_edges, 2 * out_features]
        cat_features = torch.cat([h[:, row], h[:, col]], dim=-1)
        
        # Compute attention scores
        # Shape: [num_heads, num_edges, 1]
        e = torch.matmul(cat_features, self.a).squeeze(-1)
        
        # Apply LeakyReLU
        e = self.leaky_relu(e)
        
        # Softmax over neighbors for each node
        # We need to group by target node
        attention = self._softmax_by_target(e, row, col, num_nodes)
        
        # Apply dropout
        attention = self.dropout(attention)
        
        # Aggregate messages weighted by attention
        # Shape: [num_heads, num_nodes, out_features]
        out = torch.zeros_like(h)
        
        for head in range(self.num_heads):
            # Weight source node features by attention
            weighted_messages = h[head, row] * attention[head].unsqueeze(-1)
            
            # Aggregate to target nodes
            out[head] = torch.zeros(num_nodes, self.out_features, device=x.device)
            out[head].index_add_(0, col, weighted_messages)
        
        # Combine heads
        if self.concat:
            # Concatenate all heads
            out = out.view(num_nodes, -1)
        else:
            # Average heads
            out = out.mean(dim=0)
        
        return out
    
    def _softmax_by_target(self, e, row, col, num_nodes):
        """Apply softmax over neighbors for each target node"""
        # This is a simplified version - in practice, use efficient implementations
        attention = torch.zeros_like(e)
        
        for head in range(self.num_heads):
            # Group edges by target node
            for target in range(num_nodes):
                mask = (col == target)
                if mask.sum() > 0:
                    scores = e[head][mask]
                    attn_scores = torch.softmax(scores, dim=0)
                    attention[head][mask] = attn_scores
        
        return attention


class GAT(nn.Module):
    """Multi-layer Graph Attention Network"""
    def __init__(self, in_features, hidden_features, out_features, 
                 num_heads=8, num_layers=2, dropout=0.6):
        super(GAT, self).__init__()
        
        # Input layer with multi-head attention
        self.input_layer = GATLayer(
            in_features, hidden_features, num_heads=num_heads, 
            dropout=dropout, concat=True
        )
        
        # Hidden layers
        self.hidden_layers = nn.ModuleList([
            GATLayer(hidden_features * num_heads, hidden_features, 
                    num_heads=num_heads, dropout=dropout, concat=True)
            for _ in range(num_layers - 2)
        ])
        
        # Output layer (single head, no concatenation)
        self.output_layer = GATLayer(
            hidden_features * num_heads, out_features, 
            num_heads=1, dropout=dropout, concat=False
        )
        
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x, edge_index):
        """Forward pass"""
        x = self.input_layer(x, edge_index)
        x = F.elu(x)
        x = self.dropout(x)
        
        for layer in self.hidden_layers:
            x = layer(x, edge_index)
            x = F.elu(x)
            x = self.dropout(x)
        
        x = self.output_layer(x, edge_index)
        
        return x
```

### Using GAT with PyTorch Geometric

PyTorch Geometric has a highly optimized GAT implementation:

```python
from torch_geometric.nn import GATConv

class GATModel(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, num_heads=8):
        super().__init__()
        
        # First GAT layer with multi-head attention
        self.conv1 = GATConv(in_channels, hidden_channels, 
                            heads=num_heads, dropout=0.6)
        
        # Second GAT layer (single head for output)
        self.conv2 = GATConv(hidden_channels * num_heads, out_channels, 
                            heads=1, dropout=0.6)
        
        self.dropout = nn.Dropout(0.6)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.elu(x)
        x = self.dropout(x)
        x = self.conv2(x, edge_index)
        return x


# Training example
model = GATModel(
    in_channels=dataset.num_features,
    hidden_channels=64,
    out_channels=dataset.num_classes,
    num_heads=8
)

optimizer = optim.Adam(model.parameters(), lr=0.005, weight_decay=5e-4)

for epoch in range(200):
    model.train()
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)
    loss = criterion(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
```

### When to Use GAT

**✅ Good for:**
- Graphs where neighbor importance varies
- Heterophilic graphs
- When interpretability matters (attention weights)
- Inductive learning (unseen graphs)
- Social networks, citation networks

**❌ Not ideal for:**
- Very large graphs (attention is O(E))
- When all neighbors are equally important
- Memory-constrained environments

---

## 2.3 GraphSAGE: Sampling for Scale

### What is GraphSAGE?

**GraphSAGE** (Graph Sample and AggregatE), introduced by Hamilton et al. in 2017, solves a critical problem: **how to handle massive graphs**.

Traditional GNNs require loading the entire graph into memory. GraphSAGE instead **samples a fixed-size neighborhood** for each node, making it possible to train on graphs with millions or billions of nodes!

### The Key Innovation: Inductive Learning

GraphSAGE was designed for **inductive learning**:
- **Transductive** (GCN, GAT): Train and test on the same graph
- **Inductive** (GraphSAGE): Train on one graph, test on completely new graphs

This is crucial for real-world applications where new nodes appear constantly (new users, new papers, new products).

### How GraphSAGE Works

Instead of aggregating ALL neighbors, GraphSAGE:

1. **Samples** a fixed number of neighbors at each layer
2. **Aggregates** features from sampled neighbors
3. **Combines** with the node's own features
4. **Applies** a neural network transformation

### Sampling Strategy

For a 2-layer GraphSAGE:
- Layer 1: Sample 10 neighbors for each node
- Layer 2: Sample 10 neighbors for each of those neighbors

Result: Each node aggregates information from up to 100 neighbors (10 × 10), regardless of actual degree!

### Aggregator Functions

GraphSAGE supports multiple aggregation functions:

| Aggregator | How it Works | Best For |
|------------|--------------|----------|
| **Mean** | Average neighbor features | General purpose |
| **LSTM** | Sequential processing | Ordered neighbors |
| **Pooling** | Max/mean pooling | Complex patterns |
| **Attention** | Weighted aggregation | Important neighbors |

### Implementing GraphSAGE

```python
import numpy as np
from collections import defaultdict

class GraphSAGELayer(nn.Module):
    """
    GraphSAGE layer with mean aggregator.
    """
    def __init__(self, in_features, out_features, num_samples=10):
        super(GraphSAGELayer, self).__init__()
        
        self.num_samples = num_samples
        
        # Weight matrices
        self.self_weight = nn.Linear(in_features, out_features)
        self.neighbor_weight = nn.Linear(in_features, out_features, bias=False)
        
        self.reset_parameters()
    
    def reset_parameters(self):
        nn.init.xavier_uniform_(self.self_weight.weight)
        nn.init.xavier_uniform_(self.neighbor_weight.weight)
    
    def sample_neighbors(self, node, neighbors_dict):
        """Sample fixed number of neighbors"""
        neighbors = neighbors_dict.get(node, [])
        
        if len(neighbors) <= self.num_samples:
            return neighbors
        
        # Randomly sample without replacement
        return list(np.random.choice(neighbors, self.num_samples, replace=False))
    
    def forward(self, x, neighbors_dict):
        """
        Forward pass.
        
        Args:
            x: Node features [num_nodes, in_features]
            neighbors_dict: Dict mapping node_id -> list of neighbor_ids
        
        Returns:
            Updated node features
        """
        num_nodes = x.shape[0]
        device = x.device
        
        # Collect sampled neighbors for all nodes
        sampled_neighbors = []
        for node in range(num_nodes):
            sampled = self.sample_neighbors(node, neighbors_dict)
            sampled_neighbors.append(sampled)
        
        # Aggregate neighbor features
        neighbor_aggregates = []
        for node in range(num_nodes):
            neighbor_ids = sampled_neighbors[node]
            
            if len(neighbor_ids) == 0:
                # No neighbors - use zeros
                agg = torch.zeros(x.shape[1], device=device)
            else:
                # Mean aggregation
                neighbor_features = x[neighbor_ids]
                agg = neighbor_features.mean(dim=0)
            
            neighbor_aggregates.append(agg)
        
        neighbor_aggregates = torch.stack(neighbor_aggregates)
        
        # Combine self and neighbor features
        self_features = self.self_weight(x)
        neighbor_features = self.neighbor_weight(neighbor_aggregates)
        
        # Combine and activate
        combined = self_features + neighbor_features
        output = F.relu(combined)
        
        # Normalize
        output = F.normalize(output, p=2, dim=1)
        
        return output


class GraphSAGE(nn.Module):
    """Multi-layer GraphSAGE"""
    def __init__(self, in_features, hidden_features, out_features, 
                 num_samples=10, num_layers=2):
        super(GraphSAGE, self).__init__()
        
        self.layers = nn.ModuleList([
            GraphSAGELayer(in_features, hidden_features, num_samples),
            GraphSAGELayer(hidden_features, out_features, num_samples)
        ])
    
    def forward(self, x, neighbors_dict):
        for layer in self.layers:
            x = layer(x, neighbors_dict)
        return x
```

### Using GraphSAGE with PyTorch Geometric

```python
from torch_geometric.nn import SAGEConv
from torch_geometric.loader import NeighborLoader

# Create neighbor loader for mini-batch training
loader = NeighborLoader(
    data,
    num_neighbors=[10, 10],  # Sample 10 neighbors at each layer
    batch_size=32,
    shuffle=True
)

class SAGEModel(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        
        self.conv1 = SAGEConv(in_channels, hidden_channels)
        self.conv2 = SAGEConv(hidden_channels, out_channels)
        
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.dropout(x)
        x = self.conv2(x, edge_index)
        return x


# Mini-batch training
model = SAGEModel(dataset.num_features, 64, dataset.num_classes)
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(10):
    total_loss = 0
    for batch in loader:
        model.train()
        optimizer.zero_grad()
        
        # Get training mask for nodes in this batch
        batch_train_mask = batch.train_mask[:batch.batch_size]
        
        out = model(batch.x, batch.edge_index)
        loss = criterion(out[batch_train_mask], batch.y[batch_train_mask])
        
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    print(f"Epoch {epoch+1}, Average Loss: {total_loss / len(loader):.4f}")
```

### When to Use GraphSAGE

**✅ Good for:**
- Massive graphs (> 1M nodes)
- Inductive learning (new nodes/graphs)
- Dynamic graphs (constantly changing)
- Memory-constrained environments
- Real-time inference

**❌ Not ideal for:**
- Small graphs (overkill)
- When you need full neighborhood context
- Tasks requiring precise structural information

---

## 2.4 Other Important Architectures

### 2.4.1 Graph Isomorphism Network (GIN)

**GIN** is theoretically powerful - it can distinguish any two non-isomorphic graphs!

Key insight: Use **sum aggregation** instead of mean/max:

```python
from torch_geometric.nn import GINConv

class GINModel(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        
        # GIN uses MLP inside the convolution
        nn1 = nn.Sequential(
            nn.Linear(in_channels, hidden_channels),
            nn.ReLU(),
            nn.Linear(hidden_channels, hidden_channels)
        )
        self.conv1 = GINConv(nn1, train_eps=True)
        
        nn2 = nn.Sequential(
            nn.Linear(hidden_channels, hidden_channels),
            nn.ReLU(),
            nn.Linear(hidden_channels, out_channels)
        )
        self.conv2 = GINConv(nn2, train_eps=True)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x
```

**Best for**: Graph classification tasks where structure matters.

### 2.4.2 Message Passing Neural Networks (MPNN)

**MPNN** is a general framework that unifies many GNN variants:

```
Message: m_ij = M_t(h_i, h_j, e_ij)
Aggregate: m_i = Σ_j m_ij
Update: h_i' = U_t(h_i, m_i)
```

Implement custom MPNN:

```python
from torch_geometric.nn import MessagePassing

class CustomMPNN(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super().__init__(aggr='add')  # Sum aggregation
        
        self.message_nn = nn.Sequential(
            nn.Linear(in_channels * 2, in_channels),
            nn.ReLU()
        )
        self.update_nn = nn.Sequential(
            nn.Linear(in_channels * 2, out_channels),
            nn.ReLU()
        )
    
    def message(self, x_i, x_j):
        # Create message from source and target
        return self.message_nn(torch.cat([x_i, x_j], dim=-1))
    
    def update(self, aggr_out, x):
        # Update node features
        return self.update_nn(torch.cat([aggr_out, x], dim=-1))
```

**Best for**: Research and custom architectures.

### 2.4.3 Heterogeneous GNNs (R-GCN, HAN)

For graphs with **multiple node/edge types**:

```python
from torch_geometric.nn import HeteroConv, HGTConv

# Heterogeneous graph convolution
conv = HeteroConv({
    ('author', 'writes', 'paper'): GATConv((-1, -1), 64),
    ('paper', 'cites', 'paper'): GCNConv(-1, 64),
    ('paper', 'written_by', 'author'): SAGEConv((-1, -1), 64),
}, aggr='sum')
```

**Best for**: Knowledge graphs, recommendation systems, biological networks.

---

## 2.5 Architecture Comparison Guide

### Quick Decision Tree

```
Start: What's your graph size?
│
├─ Small (< 10k nodes)
│  └─ Need interpretability?
│     ├─ Yes → GAT
│     └─ No → GCN
│
├─ Medium (10k - 100k nodes)
│  └─ Heterophilic (different nodes connect)?
│     ├─ Yes → GAT or GraphSAGE
│     └─ No → GCN
│
└─ Large (> 100k nodes)
   └─ Need inductive learning?
      ├─ Yes → GraphSAGE
      └─ No → GraphSAGE with full neighborhoods
```

### Detailed Comparison Table

| Architecture | Speed | Memory | Accuracy | Inductive | Interpretability | Best Use Case |
|--------------|-------|--------|----------|-----------|------------------|---------------|
| **GCN** | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ❌ | ⭐⭐ | Baseline, small graphs |
| **GAT** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ✅ | ⭐⭐⭐⭐ | Variable neighbor importance |
| **GraphSAGE** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ⭐⭐ | Large-scale, dynamic |
| **GIN** | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ✅ | ⭐⭐ | Graph classification |
| **MPNN** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ | ⭐⭐⭐ | Custom architectures |

### Performance Benchmarks

On Cora citation network (node classification):

| Model | Accuracy | Training Time | Parameters |
|-------|----------|---------------|------------|
| GCN | 81.5% | 0.8s/epoch | 23K |
| GAT (8 heads) | 83.2% | 1.2s/epoch | 45K |
| GraphSAGE | 79.8% | 0.6s/epoch | 28K |
| GIN | 80.9% | 0.9s/epoch | 31K |

---

## 2.6 Hands-On: Choosing and Implementing the Right Architecture

### Scenario 1: Social Network Analysis

**Problem**: Classify users in a social network (spam vs. legitimate)

**Graph characteristics**:
- 50k users (medium)
- Heterophilic (spammers connect to legitimate users)
- New users join daily (dynamic)

**Recommended**: GraphSAGE or GAT

```python
def build_social_network_model(num_features, num_classes):
    # GraphSAGE for scalability and inductive learning
    return SAGEModel(num_features, 128, num_classes)
```

### Scenario 2: Molecular Property Prediction

**Problem**: Predict if a molecule is toxic

**Graph characteristics**:
- Small molecules (< 100 atoms)
- Structure is critical
- Fixed graphs

**Recommended**: GIN or GCN

```python
def build_molecular_model(num_features, num_classes):
    # GIN for maximum structural expressiveness
    return GINModel(num_features, 64, num_classes)
```

### Scenario 3: Citation Network Analysis

**Problem**: Classify research papers by topic

**Graph characteristics**:
- Homophilic (similar papers cite each other)
- Medium size (10k-50k papers)
- Interpretability important

**Recommended**: GAT

```python
def build_citation_model(num_features, num_classes):
    # GAT to see which citations matter most
    return GATModel(num_features, 64, num_classes, num_heads=8)
```

---

## Troubleshooting Common Issues

### Issue 1: "My GAT is slower than GCN"

**Cause**: Attention computation is expensive

**Solutions**:
- Reduce number of attention heads
- Use sparse attention mechanisms
- Try GCN if performance is similar

### Issue 2: "GraphSAGE accuracy is lower than GCN"

**Cause**: Too aggressive sampling

**Solutions**:
- Increase `num_neighbors`
- Add more layers
- Ensure sufficient training epochs

### Issue 3: "Out of memory on large graphs"

**Cause**: Loading entire graph

**Solutions**:
- Switch to GraphSAGE with NeighborLoader
- Reduce batch size
- Use gradient checkpointing

### Issue 4: "Attention weights are uniform"

**Cause**: Model isn't learning to differentiate

**Solutions**:
- Increase model capacity
- Add more training data
- Check for data leakage
- Try different initialization

---

## Chapter Summary

### Key Takeaways

1. **GCN** - Simple, effective baseline for small-medium graphs
2. **GAT** - Attention mechanism for variable neighbor importance
3. **GraphSAGE** - Sampling for massive, dynamic graphs
4. **GIN** - Maximum expressiveness for graph classification
5. **Choose wisely** - Match architecture to your problem constraints

### Architecture Selection Cheat Sheet

```
Small graph + homophily → GCN
Variable neighbor importance → GAT
Large/dynamic graph → GraphSAGE
Graph classification → GIN
Custom requirements → MPNN
Multiple node types → Heterogeneous GNN
```

---

## Exercises

### Exercise 1: Architecture Comparison (Beginner)

Train GCN, GAT, and GraphSAGE on the Cora dataset. Compare:
- Final accuracy
- Training time per epoch
- Number of parameters

```python
# Your code here
# Hint: Use the models from this chapter
```

### Exercise 2: Attention Visualization (Intermediate)

Train a GAT model and visualize the attention weights:
- Which edges have highest attention?
- Do they make semantic sense?
- Create a heatmap of attention patterns

```python
# Extract attention weights from trained GAT
# Plot using matplotlib or networkx
```

### Exercise 3: Custom Aggregator (Advanced)

Implement a GraphSAGE variant with a custom aggregator:
- Weighted mean based on edge features
- Or your own creative aggregation function
- Test on a real dataset

```python
class CustomGraphSAGE(MessagePassing):
    # Implement your custom aggregator
    pass
```

---

## Glossary

| Term | Definition |
|------|------------|
| **Inductive Learning** | Ability to generalize to unseen nodes/graphs |
| **Transductive Learning** | Learning only on the training graph |
| **Attention Mechanism** | Learning to weight neighbors differently |
| **Neighbor Sampling** | Selecting subset of neighbors for aggregation |
| **Aggregator Function** | Method for combining neighbor information |
| **Multi-head Attention** | Running multiple attention mechanisms in parallel |
| **Homophily** | Tendency of similar nodes to connect |
| **Heterophily** | Tendency of dissimilar nodes to connect |
| **Message Passing** | Framework for updating node features |
| **Graph Isomorphism** | When two graphs have identical structure |
| **Heterogeneous Graph** | Graph with multiple node/edge types |
| **Mini-batch Training** | Training on subsets of the graph |
| ** receptive Field** | How far information can propagate |
| **Over-smoothing** | When nodes become indistinguishable after many layers |

---

## Next Steps

In Chapter 3, we'll tackle **training GNNs at scale**:
- Distributed training across multiple GPUs
- Handling billion-edge graphs
- Memory optimization techniques
- Production deployment strategies

You'll learn how companies like Pinterest, Uber, and Amazon train GNNs on graphs with billions of nodes!

Ready to scale up? Let's go! 🚀
