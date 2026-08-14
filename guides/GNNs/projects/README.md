# GNN Projects

Runnable projects for Graph Neural Networks (GNNs).

## Projects

### 1. Node Classification with GCN

Graph Convolutional Network for node classification tasks. Built from scratch with plain PyTorch (no external graph libraries needed).

**Files:**
- `node_classification_gcn/` - GCN for node classification
  - `main.py` - Full GCN implementation with synthetic graph dataset
  - `requirements.txt` - Dependencies (torch, numpy)

### 2. Link Prediction with GraphSAGE

Predicting missing links in graphs using GraphSAGE.

**Files:**
- `link_prediction_graphsage/` - GraphSAGE for link prediction

### 3. Graph Classification with GAT

Graph Attention Networks for graph-level classification.

**Files:**
- `graph_classification_gat/` - GAT for graph classification

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run a project
python <project_name>/main.py
```

## Requirements

See the main `requirements.txt` file in each project folder.
