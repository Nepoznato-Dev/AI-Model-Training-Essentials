# Chapter 3: Training GNNs at Scale

## Introduction

Congratulations on making it through Chapter 2! You now understand the major GNN architectures (GCN, GAT, GraphSAGE, GIN) and when to use each one. But there's a problem...

**What happens when your graph has:**
- 100 million nodes? (Pinterest user graph)
- 1 billion edges? (Amazon product graph)
- Constantly changing structure? (Twitter follow graph)

You can't just load this into memory and train like we did in previous chapters. Your computer would crash instantly!

In this chapter, you'll learn **how to train GNNs on massive graphs** using techniques that companies like:
- **Pinterest** (PinnerSage - 3 billion pins)
- **Uber** (Learning embeddings for 5 million locations)
- **Amazon** (Product recommendations for 300 million customers)
- **LinkedIn** (Job recommendations for 700 million members)

use every day.

### What You'll Learn

By the end of this chapter, you'll be able to:
- ✅ Train GNNs on graphs with billions of edges
- ✅ Use mini-batch training for graphs
- ✅ Distribute training across multiple GPUs
- ✅ Optimize memory usage with advanced techniques
- ✅ Deploy GNNs in production environments
- ✅ Monitor and debug large-scale training

Let's scale up! 🚀

---

## 3.1 The Scaling Challenge

### Why is Training GNNs Hard at Scale?

Traditional neural networks (like CNNs for images) are easy to scale:
```
Image → Split into batches → Train on GPU → Done!
```

But graphs are different:

**Problem 1: Connected Data**
- Nodes are connected, so you can't randomly split them
- Training on node A requires information from its neighbors
- Those neighbors need information from THEIR neighbors
- This creates an "exponential explosion" of required data

**Problem 2: Memory Explosion**
```
Layer 1: Node needs 10 neighbors
Layer 2: Each of those needs 10 neighbors = 100 nodes
Layer 3: Each of those needs 10 neighbors = 1,000 nodes
Layer 4: = 10,000 nodes
```

For a 4-layer GNN, ONE training example might require loading 10,000+ nodes!

**Problem 3: Dynamic Graphs**
- New nodes appear constantly (new users, products, papers)
- Edges change (new friendships, purchases, citations)
- Can't pre-compute everything

### Real-World Scale Examples

| Company | Graph Size | Challenge |
|---------|-----------|-----------|
| Pinterest | 3B nodes, 100B edges | Recommend pins to users |
| Amazon | 500M products, 10B interactions | Product recommendations |
| Uber | 5M places, 1B trips | ETA prediction, demand forecasting |
| LinkedIn | 700M members, 50B connections | Job recommendations |
| Twitter | 400M users, 100B follows | Content recommendation |

These companies can't load their entire graph into memory. They need special techniques!

---

## 3.2 Mini-Batch Training for Graphs

### The Core Idea

Instead of training on the entire graph at once, we:
1. **Sample** a small batch of nodes
2. **Sample** their neighborhoods
3. **Train** on just this subgraph
4. **Repeat** for many batches

This is similar to how traditional neural networks use mini-batches, but with extra care for graph structure.

### Neighbor Sampling (GraphSAGE Approach)

The most popular approach is **neighbor sampling**:

```python
from torch_geometric.loader import NeighborLoader

# Create a neighbor loader
loader = NeighborLoader(
    data,
    num_neighbors=[10, 10, 10],  # Sample 10 neighbors at each of 3 layers
    batch_size=64,                # 64 nodes per batch
    shuffle=True,
    num_workers=4                 # Parallel data loading
)

# Training loop
for batch in loader:
    # batch contains a small subgraph
    out = model(batch.x, batch.edge_index)
    loss = criterion(out, batch.y)
    loss.backward()
    optimizer.step()
```

### How Neighbor Sampling Works

Visual explanation:

```
Full Graph (1M nodes):
[Cannot fit in memory]

Step 1: Sample batch of 64 seed nodes
[OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO]

Step 2: For each seed, sample 10 neighbors (layer 1)
[Each O now has 10 neighbors sampled]

Step 3: For each of those, sample 10 more neighbors (layer 2)
[Exponential growth controlled by sampling]

Result: Subgraph with ~6,400 nodes instead of 1M
[Fits easily in GPU memory!]
```

### Complete Example: Training on Large Graph

```python
import torch
from torch_geometric.datasets import Reddit
from torch_geometric.loader import NeighborLoader
from torch_geometric.nn import SAGEConv
import torch.nn.functional as F

# Load a large dataset (Reddit: 230k nodes, 11M edges)
dataset = Reddit(root='/tmp/Reddit')
data = dataset[0]

print(f"Graph stats:")
print(f"  Nodes: {data.num_nodes:,}")
print(f"  Edges: {data.num_edges:,}")
print(f"  Features: {data.num_features}")
print(f"  Classes: {dataset.num_classes}")


class ScalableGNN(torch.nn.Module):
    """GNN designed for large-scale training"""
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        
        # Use GraphSAGE convolutions (designed for sampling)
        self.conv1 = SAGEConv(in_channels, hidden_channels)
        self.conv2 = SAGEConv(hidden_channels, hidden_channels)
        self.conv3 = SAGEConv(hidden_channels, out_channels)
        
        self.dropout = nn.Dropout(0.5)
        self.batch_norm1 = nn.BatchNorm1d(hidden_channels)
        self.batch_norm2 = nn.BatchNorm1d(hidden_channels)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = self.batch_norm1(x)
        x = F.relu(x)
        x = self.dropout(x)
        
        x = self.conv2(x, edge_index)
        x = self.batch_norm2(x)
        x = F.relu(x)
        x = self.dropout(x)
        
        x = self.conv3(x, edge_index)
        return x


# Create neighbor loader for training
train_loader = NeighborLoader(
    data,
    input_nodes=data.train_mask,      # Only sample from training nodes
    num_neighbors=[25, 10, 5],        # Decreasing samples at deeper layers
    batch_size=1024,                   # Large batch size for efficiency
    shuffle=True,
    num_workers=4,                     # Parallel loading
    pin_memory=True                    # Faster CPU->GPU transfer
)

# Create validation loader
val_loader = NeighborLoader(
    data,
    input_nodes=data.val_mask,
    num_neighbors=[25, 10, 5],
    batch_size=1024,
    shuffle=False,
    num_workers=4
)

# Initialize model
model = ScalableGNN(
    in_channels=data.num_features,
    hidden_channels=256,
    out_channels=dataset.num_classes
)

# Move to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Optimizer with weight decay for regularization
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=5e-4)

# Learning rate scheduler
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.5, patience=5
)


def train_epoch():
    """Train for one epoch"""
    model.train()
    total_loss = 0
    total_correct = 0
    total_examples = 0
    
    for batch in train_loader:
        batch = batch.to(device)
        optimizer.zero_grad()
        
        # Forward pass
        out = model(batch.x, batch.edge_index)
        
        # Compute loss only on seed nodes (first batch_size nodes)
        loss = F.cross_entropy(out[:batch.batch_size], batch.y[:batch.batch_size])
        
        # Backward pass
        loss.backward()
        optimizer.step()
        
        # Track metrics
        total_loss += loss.item() * batch.batch_size
        pred = out[:batch.batch_size].argmax(dim=1)
        total_correct += int((pred == batch.y[:batch.batch_size]).sum())
        total_examples += batch.batch_size
    
    return total_loss / total_examples, total_correct / total_examples


@torch.no_grad()
def validate():
    """Evaluate on validation set"""
    model.eval()
    total_correct = 0
    total_examples = 0
    
    for batch in val_loader:
        batch = batch.to(device)
        out = model(batch.x, batch.edge_index)
        pred = out[:batch.batch_size].argmax(dim=1)
        total_correct += int((pred == batch.y[:batch.batch_size]).sum())
        total_examples += batch.batch_size
    
    return total_correct / total_examples


# Training loop
num_epochs = 50
best_val_acc = 0

for epoch in range(num_epochs):
    train_loss, train_acc = train_epoch()
    val_acc = validate()
    
    # Update learning rate
    scheduler.step(val_loss)
    
    print(f"Epoch {epoch+1}/{num_epochs}")
    print(f"  Train Loss: {train_loss:.4f}")
    print(f"  Train Acc: {train_acc:.4f}")
    print(f"  Val Acc: {val_acc:.4f}")
    
    # Save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), 'best_gnn_model.pt')

print(f"\nBest validation accuracy: {best_val_acc:.4f}")
```

### Key Parameters Explained

| Parameter | What it Does | Recommended Values |
|-----------|--------------|-------------------|
| `num_neighbors` | How many neighbors to sample at each layer | [25, 10, 5] or [15, 10, 5] |
| `batch_size` | Number of seed nodes per batch | 512-2048 (larger = more stable) |
| `num_workers` | Parallel data loading processes | 4-8 (match CPU cores) |
| `pin_memory` | Faster CPU→GPU transfer | True (if using GPU) |
| `input_nodes` | Which nodes can be sampled as seeds | Training mask |

### Best Practices for Mini-Batch Training

1. **Decrease sampling at deeper layers**
   ```python
   # Good: Focus on immediate neighbors
   num_neighbors=[25, 10, 5]
   
   # Bad: Equal sampling everywhere
   num_neighbors=[15, 15, 15]
   ```

2. **Use large batch sizes**
   - Small batches (< 128) → unstable training
   - Large batches (> 2048) → better convergence
   - Limited by GPU memory

3. **Enable multi-worker loading**
   ```python
   # Single worker (slow)
   num_workers=0
   
   # Multiple workers (fast)
   num_workers=4
   ```

4. **Normalize features**
   ```python
   from sklearn.preprocessing import StandardScaler
   
   scaler = StandardScaler()
   data.x = scaler.fit_transform(data.x.numpy())
   ```

---

## 3.3 Cluster-GCN: Graph Partitioning

### The Problem with Random Sampling

Neighbor sampling works well, but has limitations:
- Can miss important structural information
- High variance between batches
- Some nodes might never be sampled together

### The Cluster-GCN Solution

**Cluster-GCN** takes a different approach:
1. **Partition** the graph into clusters (communities)
2. **Train** on entire clusters instead of sampled neighborhoods
3. **Preserve** local graph structure within clusters

```
Original Graph:
[A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P]

After Clustering:
Cluster 1: [A-B-C-D-E]
Cluster 2: [F-G-H-I]
Cluster 3: [J-K-L-M-N]
Cluster 4: [O-P]

Training:
Batch 1: Train on Cluster 1
Batch 2: Train on Cluster 2
...
```

### Implementing Cluster-GCN

```python
from torch_geometric.loader import ClusterLoader, ClusterGCN
from torch_geometric.utils import to_scipy_sparse_matrix
import scipy.sparse as sp
from sklearn.cluster import KMeans

# Method 1: Using PyTorch Geometric's ClusterGCN
cluster_loader = ClusterLoader(
    data,
    num_parts=100,           # Divide graph into 100 clusters
    save_dir='/tmp/reddit_clustered',
    batch_size=10,           # 10 clusters per batch
    shuffle=True,
    num_workers=4
)


class ClusterGCNModel(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        self.conv3 = GCNConv(hidden_channels, out_channels)
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = self.dropout(x)
        x = F.relu(self.conv2(x, edge_index))
        x = self.dropout(x)
        x = self.conv3(x, edge_index)
        return x


model = ClusterGCNModel(data.num_features, 256, dataset.num_classes)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(50):
    total_loss = 0
    for batch in cluster_loader:
        batch = batch.to(device)
        optimizer.zero_grad()
        out = model(batch.x, batch.edge_index)
        loss = F.cross_entropy(out, batch.y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    print(f"Epoch {epoch+1}, Loss: {total_loss / len(cluster_loader):.4f}")
```

### Custom Clustering with METIS

For better control, use METIS graph partitioning:

```python
from torch_geometric.utils import metis

# Partition graph into 100 clusters
node_cluster_ids = metis.partition(data.edge_index, num_parts=100)

# Create custom loader
class CustomClusterLoader:
    def __init__(self, data, cluster_ids, batch_size=10):
        self.data = data
        self.cluster_ids = cluster_ids
        self.batch_size = batch_size
        self.unique_clusters = cluster_ids.unique().tolist()
    
    def __iter__(self):
        import random
        random.shuffle(self.unique_clusters)
        
        for i in range(0, len(self.unique_clusters), self.batch_size):
            batch_clusters = self.unique_clusters[i:i+self.batch_size]
            
            # Get nodes in these clusters
            mask = torch.isin(self.cluster_ids, torch.tensor(batch_clusters))
            
            # Extract subgraph
            batch = self.data.subgraph(mask)
            yield batch
    
    def __len__(self):
        return (len(self.unique_clusters) + self.batch_size - 1) // self.batch_size


loader = CustomClusterLoader(data, node_cluster_ids, batch_size=10)
```

### When to Use Cluster-GCN

**✅ Good for:**
- Graphs with clear community structure
- When preserving local structure matters
- More stable training than sampling
- Smaller variance between batches

**❌ Not ideal for:**
- Graphs without clear clusters
- Very deep GNNs (still limited by cluster size)
- Dynamic graphs (need to re-cluster)

---

## 3.4 Distributed Training

### Why Distribute Training?

Even with mini-batching, training on massive graphs can take days or weeks. **Distributed training** uses multiple GPUs/machines to speed this up.

### Data Parallelism

Simplest approach: Same model on multiple GPUs, different batches:

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler

# Initialize distributed training
dist.init_process_group("nccl")
local_rank = dist.get_rank()
torch.cuda.set_device(local_rank)

# Create model
model = ScalableGNN(data.num_features, 256, dataset.num_classes)
model = model.to(local_rank)

# Wrap with DDP
model = DDP(model, device_ids=[local_rank])

# Use distributed sampler
sampler = DistributedSampler(dataset, num_replicas=dist.get_world_size(), rank=local_rank)

loader = NeighborLoader(
    data,
    num_neighbors=[25, 10, 5],
    batch_size=1024,
    sampler=sampler,
    num_workers=4
)

# Training loop (same as before, but faster!)
for epoch in range(50):
    for batch in loader:
        batch = batch.to(local_rank)
        # ... training code ...
```

### Launching Distributed Training

Create a launch script:

```bash
#!/bin/bash
# train_distributed.sh

NUM_GPUS=4

torchrun --nproc_per_node=$NUM_GPUS \
    train_gnn.py \
    --epochs 50 \
    --batch_size 1024 \
    --lr 0.001
```

Run with:
```bash
bash train_distributed.sh
```

### Pipeline Parallelism (Advanced)

For extremely large models, split the model itself across GPUs:

```python
# Layer 1-2 on GPU 0
# Layer 3-4 on GPU 1
# Layer 5-6 on GPU 2

class PipelineGNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.stage1 = nn.Sequential(GCNLayer(...), GCNLayer(...)).to('cuda:0')
        self.stage2 = nn.Sequential(GCNLayer(...), GCNLayer(...)).to('cuda:1')
        self.stage3 = nn.Sequential(GCNLayer(...), GCNLayer(...)).to('cuda:2')
    
    def forward(self, x, edge_index):
        x = x.to('cuda:0')
        x = self.stage1(x, edge_index)
        
        x = x.to('cuda:1')
        x = self.stage2(x, edge_index)
        
        x = x.to('cuda:2')
        x = self.stage3(x, edge_index)
        
        return x
```

### Multi-Node Training

Scale beyond one machine:

```python
# On head node
torchrun --nnodes=4 --nproc_per_node=4 \
    --rdzv_id=job123 \
    --rdzv_backend=c10d \
    --rdzv_endpoint=head_node:29500 \
    train_gnn.py

# On worker nodes (same command)
torchrun --nnodes=4 --nproc_per_node=4 \
    --rdzv_id=job123 \
    --rdzv_backend=c10d \
    --rdzv_endpoint=head_node:29500 \
    train_gnn.py
```

### Performance Comparison

| Setup | Training Time (Reddit) | Speedup |
|-------|----------------------|---------|
| 1 GPU | 10 hours | 1x |
| 4 GPUs (data parallel) | 2.8 hours | 3.6x |
| 8 GPUs (data parallel) | 1.5 hours | 6.7x |
| 16 GPUs (multi-node) | 0.9 hours | 11.1x |

---

## 3.5 Memory Optimization Techniques

### Problem: GPU Out of Memory

Even with batching, you might hit memory limits. Here's how to optimize:

### Technique 1: Gradient Checkpointing

Trade computation for memory:

```python
from torch.utils.checkpoint import checkpoint

class MemoryEfficientGNN(nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.layers = nn.ModuleList([...])
    
    def forward(self, x, edge_index):
        for layer in self.layers:
            # Recompute activations during backward pass
            x = checkpoint(layer, x, edge_index)
        return x

# Reduces memory by 3-4x, slows training by ~20%
```

### Technique 2: Mixed Precision Training

Use 16-bit floats instead of 32-bit:

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for batch in loader:
    optimizer.zero_grad()
    
    with autocast():  # Automatic mixed precision
        out = model(batch.x, batch.edge_index)
        loss = criterion(out, batch.y)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()

# Reduces memory by 2x, often faster on modern GPUs
```

### Technique 3: Feature Caching

Pre-compute and cache node embeddings:

```python
class CachedGNN(nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.feature_cache = None
    
    def update_cache(self, data):
        """Pre-compute embeddings for all nodes"""
        self.model.eval()
        with torch.no_grad():
            self.feature_cache = self.model(data.x, data.edge_index)
    
    def forward(self, node_ids):
        # Just look up cached features
        return self.feature_cache[node_ids]

# Great for inference, reduces computation dramatically
```

### Technique 4: Sparse Operations

Use sparse matrices instead of dense:

```python
from torch_geometric.utils import to_torch_coo_tensor

# Convert to sparse format
edge_index_sparse = to_torch_coo_tensor(
    data.edge_index, 
    size=data.num_nodes
)

# Use sparse operations in model
class SparseGNN(nn.Module):
    def forward(self, x, edge_index_sparse):
        # Sparse matrix multiplication
        out = torch.sparse.mm(edge_index_sparse, x)
        return out

# Reduces memory for sparse graphs by 10-100x
```

### Memory Usage Comparison

| Technique | Memory Usage | Speed Impact |
|-----------|--------------|--------------|
| Baseline | 16 GB | 1.0x |
| Mixed Precision | 8 GB | 1.3x faster |
| Gradient Checkpointing | 5 GB | 0.8x slower |
| Both Combined | 3 GB | 1.1x faster |
| + Sparse Ops | 1 GB | 1.5x faster |

---

## 3.6 Production Deployment

### From Training to Production

Training is only half the battle. Now you need to serve predictions!

### Deployment Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Client    │────▶│  Load Balancer│────▶│ GNN Service │
│  (App/Web)  │     │              │     │  (Multiple  │
└─────────────┘     └──────────────┘     │   Instances)│
                                          └─────────────┘
                                                │
                                                ▼
                                         ┌─────────────┐
                                         │   Feature   │
                                         │   Store     │
                                         └─────────────┘
```

### Model Serving with TorchServe

1. **Create model handler**:

```python
# gnn_handler.py
from ts.torch_handler.base_handler import BaseHandler
import torch
from model import ScalableGNN

class GNNHandler(BaseHandler):
    def initialize(self, context):
        self.model = ScalableGNN(...)
        self.model.load_state_dict(torch.load('model.pt'))
        self.model.eval()
    
    def preprocess(self, data):
        # Convert input to tensors
        return data['nodes'], data['edge_index']
    
    def inference(self, nodes, edge_index):
        with torch.no_grad():
            return self.model(nodes, edge_index)
    
    def postprocess(self, output):
        # Convert to JSON-serializable format
        return output.argmax(dim=1).tolist()
```

2. **Create model archive**:
```bash
torch-model-archiver \
    --model-name gnn_recommender \
    --version 1.0 \
    --model-file model.py \
    --serialized-file model.pt \
    --handler gnn_handler.py
```

3. **Start server**:
```bash
torchserve --start --model-store ./model-store --models gnn_recommender.mar
```

4. **Make predictions**:
```python
import requests

response = requests.post(
    'http://localhost:8080/predictions/gnn_recommender',
    json={'nodes': [...], 'edge_index': [...]}
)
predictions = response.json()
```

### Real-Time Inference Optimization

For low-latency requirements:

```python
class OptimizedInference:
    def __init__(self, model_path):
        # Load model
        self.model = ScalableGNN(...)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        
        # Compile for faster inference (PyTorch 2.0+)
        self.model = torch.compile(self.model)
        
        # Warm up
        self.warmup()
    
    def warmup(self):
        # Run dummy inputs to optimize
        dummy_x = torch.randn(100, 256)
        dummy_edge = torch.randint(0, 100, (2, 500))
        self.model(dummy_x, dummy_edge)
    
    @torch.no_grad()
    def predict(self, x, edge_index):
        # Move to GPU
        x = x.cuda()
        edge_index = edge_index.cuda()
        
        # Predict
        output = self.model(x, edge_index)
        
        # Return probabilities
        return torch.softmax(output, dim=1)
```

### Monitoring in Production

Track model performance:

```python
import prometheus_client

class MonitoredGNN:
    def __init__(self, model):
        self.model = model
        
        # Define metrics
        self.prediction_latency = prometheus_client.Histogram(
            'gnn_prediction_latency_seconds',
            'Time for GNN prediction'
        )
        self.prediction_count = prometheus_client.Counter(
            'gnn_predictions_total',
            'Total number of predictions'
        )
        self.error_count = prometheus_client.Counter(
            'gnn_errors_total',
            'Total number of errors'
        )
    
    @torch.no_grad()
    def predict(self, x, edge_index):
        try:
            with self.prediction_latency.time():
                output = self.model(x, edge_index)
            
            self.prediction_count.inc()
            return output
            
        except Exception as e:
            self.error_count.inc()
            raise e
```

### A/B Testing

Test new models safely:

```python
class ABTestRouter:
    def __init__(self, model_a, model_b, traffic_split=0.9):
        self.model_a = model_a
        self.model_b = model_b
        self.traffic_split = traffic_split  # 90% to A, 10% to B
    
    def predict(self, x, edge_index):
        import random
        
        if random.random() < self.traffic_split:
            # Send to model A
            return self.model_a.predict(x, edge_index), 'A'
        else:
            # Send to model B
            return self.model_b.predict(x, edge_index), 'B'

# Compare metrics between A and B
```

---

## Troubleshooting Large-Scale Training

### Issue 1: "Training is too slow"

**Diagnosis**:
```python
# Profile data loading
import time

start = time.time()
for batch in loader:
    pass
end = time.time()

print(f"Data loading time: {end - start:.2f}s")
```

**Solutions**:
- Increase `num_workers`
- Use `pin_memory=True`
- Pre-fetch batches
- Reduce `num_neighbors`

### Issue 2: "Out of memory even with small batches"

**Solutions**:
- Enable mixed precision (`autocast`)
- Use gradient checkpointing
- Reduce hidden dimensions
- Switch to sparse operations
- Use CPU offloading

### Issue 3: "Validation accuracy much lower than training"

**Causes**:
- Overfitting
- Distribution shift between train/val
- Insufficient regularization

**Solutions**:
- Add dropout
- Increase weight decay
- Use early stopping
- Check data preprocessing consistency

### Issue 4: "Distributed training hangs"

**Solutions**:
- Check network connectivity
- Ensure same code on all nodes
- Set proper timeout
- Use `NCCL_DEBUG=INFO` for debugging

---

## Chapter Summary

### Key Takeaways

1. **Mini-batch training** enables training on massive graphs
2. **Neighbor sampling** controls memory usage
3. **Cluster-GCN** preserves local structure
4. **Distributed training** speeds up training linearly
5. **Memory optimization** techniques reduce GPU requirements
6. **Production deployment** requires careful planning

### Scaling Checklist

Before deploying at scale:
- [ ] Implemented mini-batch training
- [ ] Chosen appropriate sampling strategy
- [ ] Optimized memory usage
- [ ] Set up monitoring
- [ ] Tested inference latency
- [ ] Planned for A/B testing

---

## Exercises

### Exercise 1: Neighbor Sampling Analysis (Beginner)

Experiment with different sampling parameters:
```python
configs = [
    [5, 5, 5],
    [10, 10, 10],
    [25, 10, 5],
    [50, 20, 10]
]

# Train with each config and compare:
# - Training time per epoch
# - Final accuracy
# - Memory usage
```

### Exercise 2: Implement Cluster-GCN (Intermediate)

Implement Cluster-GCN from scratch:
1. Use METIS to partition a graph
2. Create custom data loader
3. Train and compare with neighbor sampling

### Exercise 3: Multi-GPU Training (Advanced)

Set up distributed training:
1. Configure DDP
2. Train on multiple GPUs
3. Measure speedup
4. Analyze scaling efficiency

---

## Glossary

| Term | Definition |
|------|------------|
| **Mini-batch Training** | Training on small subsets of data |
| **Neighbor Sampling** | Selecting subset of neighbors for each node |
| **Cluster-GCN** | Training on graph partitions instead of samples |
| **Data Parallelism** | Same model on multiple devices, different data |
| **Pipeline Parallelism** | Different model layers on different devices |
| **Gradient Checkpointing** | Trading computation for memory savings |
| **Mixed Precision** | Using 16-bit and 32-bit floats together |
| **Sparse Operations** | Computations on sparse matrices |
| **METIS** | Graph partitioning algorithm |
| **DDP** | PyTorch DistributedDataParallel |
| **NCCL** | NVIDIA Collective Communications Library |
| **TorchServe** | Model serving framework |
| **A/B Testing** | Comparing two models in production |

---

## Next Steps

In Chapter 4, we'll apply everything you've learned to **real-world applications**:
- Drug discovery with molecular graphs
- Recommendation systems
- Fraud detection in financial networks
- Traffic prediction in transportation networks

You'll build complete end-to-end projects that you can add to your portfolio!

Ready to build something amazing? Let's go! 🚀
