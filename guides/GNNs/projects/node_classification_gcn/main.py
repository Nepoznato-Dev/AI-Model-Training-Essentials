# Node Classification with Graph Convolutional Networks (GCN)
# Build a GCN from scratch and classify nodes in a citation graph
# Lines of code: ~300 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import time

print("=" * 70)
print("NODE CLASSIFICATION WITH GRAPH CONVOLUTIONAL NETWORKS (GCN)")
print("=" * 70)
print()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
print()

# ============================================================================
# STEP 2: UNDERSTAND GRAPH NEURAL NETWORKS
# ============================================================================
#
# Unlike images (grids) or text (sequences), graphs have irregular structure.
# Each node has a variable number of neighbors, so we can't use standard
# convolutions. Instead, GCNs "pass messages" between connected nodes.
#
# A GCN layer does this for each node:
#
#   1. Collect features from all neighboring nodes
#   2. Aggregate (sum/mean) the neighbor features
#   3. Transform the aggregated features with a weight matrix
#   4. Apply a non-linearity (ReLU)
#
# Mathematically:  H^(l+1) = sigma(D^{-1/2} A D^{-1/2} H^(l) W^(l))
#
# Where:
#   A = adjacency matrix (who is connected to whom)
#   D = degree matrix (how many connections each node has)
#   H = node feature matrix
#   W = learnable weight matrix
#
# Think of it like a "social influence" model:
#   - Your opinion (node features) is influenced by your friends' opinions
#   - The more friends you have, the more diluted each friend's influence
#   - You also have your own baseline opinion (self-loop / skip connection)
#
# ============================================================================

# ============================================================================
# STEP 3: CREATE A SYNTHETIC GRAPH DATASET
# ============================================================================
#
# We'll create a synthetic citation graph with:
#   - 200 nodes (papers)
#   - Features: 16-dimensional vectors (representing paper topics)
#   - Labels: 4 classes (e.g., ML, NLP, Vision, Systems)
#   - Edges: connections between related papers
#
# In a real scenario, you'd load Cora, Citeseer, or PubMed datasets.
# ============================================================================

def create_synthetic_graph(num_nodes=200, num_features=16, num_classes=4, edge_prob=0.05):
    """
    Create a synthetic graph dataset for node classification.
    
    Returns:
        features: Node feature matrix (num_nodes, num_features)
        labels: Node labels (num_nodes,)
        adj: Adjacency matrix (num_nodes, num_nodes)
        train_mask: Boolean mask for training nodes
        val_mask: Boolean mask for validation nodes
        test_mask: Boolean mask for test nodes
    """
    np.random.seed(42)
    torch.manual_seed(42)
    
    # Generate node features (each class has features centered around a different point)
    features = []
    labels = []
    nodes_per_class = num_nodes // num_classes
    
    for class_idx in range(num_classes):
        # Each class has a different "center" in feature space
        center = np.random.randn(num_features) * 3
        class_features = center + np.random.randn(nodes_per_class, num_features) * 0.5
        features.extend(class_features)
        labels.extend([class_idx] * nodes_per_class)
    
    features = torch.FloatTensor(np.array(features))
    labels = torch.LongTensor(labels)
    
    # Generate edges: nodes in the same class are more likely to be connected
    adj = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            # Higher probability if same class
            if labels[i] == labels[j]:
                prob = edge_prob * 4  # Same class -> more connections
            else:
                prob = edge_prob * 0.5  # Different class -> fewer connections
            
            if np.random.random() < prob:
                adj[i][j] = 1
                adj[j][i] = 1  # Undirected graph
    
    # Add self-loops (important for GCN — each node includes its own features)
    adj = adj + np.eye(num_nodes)
    
    adj = torch.FloatTensor(adj)
    
    # Create train/val/test masks (60% / 20% / 20%)
    indices = np.random.permutation(num_nodes)
    train_size = int(0.6 * num_nodes)
    val_size = int(0.2 * num_nodes)
    
    train_mask = torch.zeros(num_nodes, dtype=torch.bool)
    val_mask = torch.zeros(num_nodes, dtype=torch.bool)
    test_mask = torch.zeros(num_nodes, dtype=torch.bool)
    
    train_mask[indices[:train_size]] = True
    val_mask[indices[train_size:train_size + val_size]] = True
    test_mask[indices[train_size + val_size:]] = True
    
    return features, labels, adj, train_mask, val_mask, test_mask

# Create the dataset
features, labels, adj, train_mask, val_mask, test_mask = create_synthetic_graph()
features, labels, adj = features.to(device), labels.to(device), adj.to(device)
train_mask = train_mask.to(device)
val_mask = val_mask.to(device)
test_mask = test_mask.to(device)

num_nodes = features.shape[0]
num_features = features.shape[1]
num_classes = len(torch.unique(labels))

print("Synthetic graph created!")
print(f"  Nodes: {num_nodes}")
print(f"  Features per node: {num_features}")
print(f"  Classes: {num_classes}")
print(f"  Edges: {int(adj.sum().item() - num_nodes) // 2} (excluding self-loops)")
print(f"  Training nodes: {train_mask.sum().item()}")
print(f"  Validation nodes: {val_mask.sum().item()}")
print(f"  Test nodes: {test_mask.sum().item()}")
print()

# ============================================================================
# STEP 4: BUILD THE GCN LAYER
# ============================================================================

class GraphConvolution(nn.Module):
    """
    A single Graph Convolutional Layer.
    
    This is the core building block of a GCN. It:
    1. Normalizes the adjacency matrix (so popular nodes don't dominate)
    2. Multiplies node features by a learnable weight matrix
    3. Aggregates neighbor information using the normalized adjacency
    
    Input:  Node features (N x F_in)
    Output: Updated node features (N x F_out)
    """
    
    def __init__(self, in_features, out_features):
        super(GraphConvolution, self).__init__()
        
        # Learnable weight matrix (transforms features at each node)
        self.weight = nn.Parameter(torch.FloatTensor(in_features, out_features))
        self.bias = nn.Parameter(torch.FloatTensor(out_features))
        
        # Initialize parameters (Xavier initialization)
        nn.init.xavier_uniform_(self.weight)
        nn.init.zeros_(self.bias)
    
    def forward(self, x, adj):
        """
        Forward pass of the GCN layer.
        
        Args:
            x: Node feature matrix, shape (num_nodes, in_features)
            adj: Adjacency matrix (with self-loops), shape (num_nodes, num_nodes)
        
        Returns:
            Updated node features, shape (num_nodes, out_features)
        """
        # Step 1: Transform features with weight matrix
        # support = X * W  ->  (N, F_out)
        support = torch.mm(x, self.weight)
        
        # Step 2: Normalize adjacency matrix (symmetric normalization)
        # D^{-1/2} * A * D^{-1/2}
        # This ensures that nodes with many connections don't dominate
        degree = adj.sum(dim=1)  # Sum of each row = degree of each node
        d_inv_sqrt = torch.pow(degree, -0.5)
        d_inv_sqrt[torch.isinf(d_inv_sqrt)] = 0.0  # Handle isolated nodes
        d_mat_inv_sqrt = torch.diag(d_inv_sqrt)
        
        # Normalized adjacency: D^{-1/2} * A * D^{-1/2}
        adj_normalized = torch.mm(torch.mm(d_mat_inv_sqrt, adj), d_mat_inv_sqrt)
        
        # Step 3: Aggregate neighbor information
        # output = A_normalized * support  ->  (N, F_out)
        output = torch.mm(adj_normalized, support) + self.bias
        
        return output

# ============================================================================
# STEP 5: BUILD THE FULL GCN MODEL
# ============================================================================

class GCN(nn.Module):
    """
    A 2-layer Graph Convolutional Network for node classification.
    
    Architecture:
        GCN Layer 1: (N, F_in) -> (N, hidden_dim) + ReLU
        GCN Layer 2: (N, hidden_dim) -> (N, num_classes)
    
    The first layer learns local patterns (1-hop neighbors).
    The second layer captures broader context (2-hop neighbors).
    """
    
    def __init__(self, num_features, num_classes, hidden_dim=32, dropout=0.5):
        super(GCN, self).__init__()
        
        # First GCN layer: project features to hidden dimension
        self.gc1 = GraphConvolution(num_features, hidden_dim)
        
        # Second GCN layer: project to class predictions
        self.gc2 = GraphConvolution(hidden_dim, num_classes)
        
        # Dropout for regularization (prevents overfitting)
        self.dropout = nn.Dropout(p=dropout)
        
        # Activation function
        self.relu = nn.ReLU()
    
    def forward(self, x, adj):
        """
        Forward pass through the 2-layer GCN.
        
        Args:
            x: Node features, shape (num_nodes, num_features)
            adj: Adjacency matrix with self-loops, shape (num_nodes, num_nodes)
        
        Returns:
            Class logits for each node, shape (num_nodes, num_classes)
        """
        # Layer 1: GCN + ReLU + Dropout
        x = self.gc1(x, adj)
        x = self.relu(x)
        x = self.dropout(x)
        
        # Layer 2: GCN (no activation — output raw logits for CrossEntropyLoss)
        x = self.gc2(x, adj)
        
        return x

# Initialize the model
model = GCN(num_features=num_features, num_classes=num_classes, hidden_dim=32, dropout=0.5).to(device)

print("GCN Model created!")
print(f"  Architecture: 2-layer GCN")
print(f"  Hidden dimension: 32")
print(f"  Parameters: {sum(p.numel() for p in model.parameters()):,}")
print()

# ============================================================================
# STEP 6: DEFINE LOSS FUNCTION AND OPTIMIZER
# ============================================================================

# Cross-Entropy Loss for multi-class node classification
criterion = nn.CrossEntropyLoss()

# Adam optimizer (only train on the model's parameters)
optimizer = optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)

print("Training setup:")
print(f"  Loss: CrossEntropyLoss")
print(f"  Optimizer: Adam (lr=0.01, weight_decay=5e-4)")
print()

# ============================================================================
# STEP 7: TRAINING LOOP
# ============================================================================

num_epochs = 200
best_val_acc = 0.0
print(f"Starting training for {num_epochs} epochs...")
print("-" * 70)

start_time = time.time()

for epoch in range(num_epochs):
    model.train()
    
    # Forward pass
    output = model(features, adj)
    
    # Compute loss only on training nodes
    loss = criterion(output[train_mask], labels[train_mask])
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Evaluate every 20 epochs
    if (epoch + 1) % 20 == 0:
        model.eval()
        with torch.no_grad():
            output = model(features, adj)
            
            # Training accuracy
            _, pred_train = output[train_mask].max(dim=1)
            train_acc = (pred_train == labels[train_mask]).float().mean().item() * 100
            
            # Validation accuracy
            _, pred_val = output[val_mask].max(dim=1)
            val_acc = (pred_val == labels[val_mask]).float().mean().item() * 100
            
            if val_acc > best_val_acc:
                best_val_acc = val_acc
            
            print(f"Epoch [{epoch+1:3d}/{num_epochs}] | "
                  f"Loss: {loss.item():.4f} | "
                  f"Train Acc: {train_acc:.1f}% | "
                  f"Val Acc: {val_acc:.1f}%")

total_time = time.time() - start_time
print("-" * 70)
print(f"Training completed in {total_time:.1f}s")
print(f"Best validation accuracy: {best_val_acc:.1f}%")
print()

# ============================================================================
# STEP 8: EVALUATE ON TEST SET
# ============================================================================

print("Evaluating on test set...")
print("-" * 70)

model.eval()
with torch.no_grad():
    output = model(features, adj)
    
    # Test accuracy
    _, pred_test = output[test_mask].max(dim=1)
    test_acc = (pred_test == labels[test_mask]).float().mean().item() * 100
    
    # Per-class accuracy
    class_names = ['Class A', 'Class B', 'Class C', 'Class D']
    class_correct = [0] * num_classes
    class_total = [0] * num_classes
    
    for i in range(test_mask.sum().item()):
        idx = torch.where(test_mask)[0][i]
        label = labels[idx].item()
        class_correct[label] += (pred_test[i] == labels[idx]).item()
        class_total[label] += 1

print(f"Test Accuracy: {test_acc:.1f}%")
print()
print("Per-class accuracy:")
for i in range(num_classes):
    if class_total[i] > 0:
        acc = 100 * class_correct[i] / class_total[i]
        print(f"  {class_names[i]}: {acc:.1f}% ({class_correct[i]}/{class_total[i]})")

print("-" * 70)
print()

# ============================================================================
# STEP 9: VISUALIZE NODE EMBEDDINGS
# ============================================================================

print("Analyzing learned node representations...")
print("-" * 70)

model.eval()
with torch.no_grad():
    # Get intermediate representations (after first GCN layer)
    hidden = model.gc1(features, adj)
    hidden = model.relu(hidden)
    hidden = hidden.cpu().numpy()
    test_labels = labels[test_mask].cpu().numpy()

# Show how well-separated the classes are in the hidden space
print("Hidden representation statistics per class:")
for c in range(num_classes):
    class_mask = (test_labels == c)
    class_hidden = hidden[test_mask.cpu().numpy()][class_mask]
    centroid = class_hidden.mean(axis=0)
    print(f"  {class_names[c]}: centroid norm = {np.linalg.norm(centroid):.2f}, "
          f"spread = {class_hidden.std(axis=0).mean():.2f}")

print("-" * 70)
print()

# ============================================================================
# STEP 10: SAVE THE MODEL
# ============================================================================

save_path = "gcn_node_classification.pth"
torch.save({
    'model_state_dict': model.state_dict(),
    'test_accuracy': test_acc,
    'num_features': num_features,
    'num_classes': num_classes,
}, save_path)
print(f"Model saved to '{save_path}'")
print()

# To load and use the model later:
# checkpoint = torch.load(save_path, weights_only=True)
# model = GCN(num_features=checkpoint['num_features'],
#             num_classes=checkpoint['num_classes'])
# model.load_state_dict(checkpoint['model_state_dict'])
# model.eval()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the GCN Node Classification Project!")
print("=" * 70)
print(f"""
What you learned:
- How Graph Neural Networks process irregular graph data
- The message-passing mechanism of GCN layers
- Symmetric normalization of adjacency matrices (D^{-1/2} A D^{-1/2})
- Building a 2-layer GCN from scratch (no external graph libraries!)
- Semi-supervised node classification with graph structure

Results Summary:
- Training time: {total_time:.1f}s
- Test accuracy: {test_acc:.1f}%
- Best validation accuracy: {best_val_acc:.1f}%
- Model saved: {save_path}

Next steps:
1. Read Chapter 2 of the GNNs Guide: Advanced Architectures
2. Try loading the Cora dataset with torch-geometric
3. Implement GraphSAGE (sampling-based aggregation)
4. Try Graph Attention Networks (GAT) for weighted neighbor importance
5. Experiment with link prediction tasks

Resources:
- GCN Paper (Kipf & Welling): https://arxiv.org/abs/1609.02907
- PyTorch Geometric: https://pyg.org/
- Graph Networks Survey: https://arxiv.org/abs/1812.08494
""")
print("=" * 70)
