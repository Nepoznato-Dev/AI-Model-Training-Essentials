# Node Classification with Graph Convolutional Networks (GCN)

Build a GCN from scratch and classify nodes in a citation graph.

## What This Project Does

This project demonstrates how to:
- Represent a **graph** (nodes, edges, adjacency matrix) in PyTorch
- Implement a **Graph Convolutional Network** layer from scratch
- Perform **node classification** on a synthetic citation graph
- Use **message passing** to aggregate neighbor information
- Train and evaluate the GCN on labeled nodes

## Concepts Covered

- Graph Neural Networks (GNNs) and why irregular graph structure requires special handling
- Graph convolution: aggregating neighbor features with normalization
- Adjacency matrix, degree matrix, and the GCN formula: `H^(l+1) = σ(D^{-1/2} A D^{-1/2} H^(l) W^(l))`
- Self-loops (adding identity to adjacency matrix so nodes aggregate their own features too)
- Semi-supervised node classification (only some nodes are labeled during training)
- Message passing paradigm

## Prerequisites

- Basic Python and PyTorch knowledge
- Familiarity with neural network fundamentals
- No graph-specific library required (implemented from scratch)

## Quick Start

```bash
# Navigate to this project directory
cd guides/GNNs/projects/node_classification_gcn

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py
```

## Files in This Project

| File | Description |
|------|-------------|
| `main.py` | Full GCN implementation (~300 lines, heavily commented) |
| `requirements.txt` | Python dependencies (torch, numpy) |
| `README.md` | This documentation file |

## How It Works

### Graph Representation

- **Nodes:** Each node has a feature vector (e.g., a paper's word embeddings in a citation graph)
- **Edges:** Connections between nodes (e.g., citation links)
- **Adjacency matrix (A):** Binary matrix where `A[i][j] = 1` if node i is connected to node j

### GCN Layer

A GCN layer updates each node's representation by:
1. Collecting features from all neighboring nodes
2. Aggregating (summing) the neighbor features
3. Normalizing by node degrees (so high-degree nodes don't dominate)
4. Transforming with a learnable weight matrix
5. Applying a non-linearity (ReLU)

### Architecture

The implementation builds a two-layer GCN:
- **Layer 1:** Input features → hidden dimension (with ReLU)
- **Layer 2:** Hidden dimension → number of classes (with softmax)

### Training

- **Setup:** Semi-supervised — only a subset of nodes have labels
- **Loss:** Cross-entropy on labeled nodes only
- **Optimizer:** Adam

## Exercises

1. Add a third GCN layer and measure accuracy change
2. Remove self-loops and observe the effect on node representations
3. Change the ratio of labeled vs. unlabeled nodes
4. Try mean aggregation instead of sum aggregation

## Common Issues

- **Slow on CPU:** Graph operations are sequential — GPU helps for larger graphs
- **Over-smoothing:** Too many GCN layers cause all node representations to converge — keep it shallow (2-3 layers)

## Next Steps

- Read the full [GNNs Guide](../../) for deeper theory
- Explore [GNNs Chapter 3: Training at Scale](../../chapter_3_training_at_scale.md)
- Check [Common Errors](../../../errors/) if you get stuck

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~300 |
| Time to Complete | 15-20 minutes |
| GPU Required | No (works on CPU) |
| Difficulty | ⭐⭐☆ Easy |
| Prerequisites | PyTorch, neural network fundamentals |
