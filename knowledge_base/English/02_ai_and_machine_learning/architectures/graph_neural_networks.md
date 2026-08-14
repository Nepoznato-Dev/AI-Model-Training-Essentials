<!--
---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
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
tags: [graph, neural, networks, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Graph Neural Networks

Graph Neural Networks (GNNs) are neural networks designed to operate on graph-structured data — networks of nodes connected by edges. While traditional neural networks work on grids (images) or sequences (text), GNNs handle arbitrary relational structures: social networks, molecular graphs, knowledge graphs, road networks, recommendation graphs, and more. They've become essential for drug discovery, fraud detection, recommendation systems, and any domain where relationships between entities matter.

---

## What Is a Graph?

| Component | Description | Example |
|-----------|-------------|---------|
| **Node (vertex)** | An entity | A person, a molecule's atom, a city |
| **Edge** | A relationship between two nodes | Friendship, chemical bond, road |
| **Edge weight** | Strength or type of relationship | Distance, similarity, capacity |
| **Node features** | Attributes of each node | Age, atomic number, population |
| **Edge features** | Attributes of each edge | Type of relationship, distance |
| **Adjacency matrix** | Matrix A where A[i][j] = 1 if nodes i and j are connected | Encodes the graph structure |

### Types of Graphs

| Type | Description | Example |
|------|-------------|---------|
| **Undirected** | Edges have no direction | Friendship network |
| **Directed** | Edges have direction (A→B ≠ B→A) | Twitter followers |
| **Weighted** | Edges have numerical values | Road network with distances |
| **Heterogeneous** | Multiple node and edge types | Academic graph (papers, authors, venues) |
| **Dynamic** | Graph structure changes over time | Social network evolving over time |
| **Bipartite** | Two types of nodes; edges only between types | User-item recommendation graph |

---

## Why Not Regular Neural Networks?

| Approach | Why It Fails |
|----------|-------------|
| **Feed-forward network** | Requires fixed-size input; graphs vary in size and structure |
| **CNN** | Assumes grid structure; graphs have no regular grid |
| **RNN/Transformer** | Assumes sequential order; graphs have no natural ordering |

GNNs solve this by operating directly on the graph structure, processing each node in the context of its neighbours.

---

## Core GNN Architectures

### Message Passing Framework

Most GNNs follow the same pattern: each node collects information from its neighbours, combines it, and updates its own representation.

| Step | Description |
|------|-------------|
| **1. Message** | Each node sends a message to its neighbours (based on its current features) |
| **2. Aggregate** | Each node collects and combines messages from all neighbours |
| **3. Update** | Each node updates its own representation using the aggregated message |
| **4. Repeat** | Do this for K layers → each node captures information from K hops away |

### Key GNN Models

| Model | Aggregation Method | Key Innovation |
|-------|-------------------|----------------|
| **GCN** (Graph Convolutional Network) | Mean of neighbour features | Simple; effective; spectral motivation |
| **GraphSAGE** | Sample and aggregate; can use mean, LSTM, or pooling | Inductive (handles unseen nodes); scalable |
| **GAT** (Graph Attention Network) | Attention-weighted neighbour aggregation | Learns which neighbours matter most |
| **GIN** (Graph Isomorphism Network) | Sum of neighbour features | Maximally expressive; can distinguish any graphs distinguishable by the WL test |
| **MPNN** (Message Passing Neural Network) | General message passing framework | Unifies many GNN variants |

### How GCN Works (Step by Step)

```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

After K layers, each node's representation encodes information from K hops away in the graph.

---

## Graph-Level Tasks

| Task | Description | Example |
|------|-------------|---------|
| **Node classification** | Predict the label of each node | Classify users as bots or humans |
| **Link prediction** | Predict whether an edge exists (or will exist) | Predict missing relationships; recommend connections |
| **Graph classification** | Predict a label for the entire graph | Classify molecules as toxic or non-toxic |
| **Community detection** | Find clusters of densely connected nodes | Identify social groups |
| **Graph generation** | Generate new graphs with desired properties | Design new molecules |

---

## Applications

### Drug Discovery and Molecular Property Prediction

| Task | How GNNs Help |
|------|--------------|
| **Molecular property prediction** | Represent molecules as graphs (atoms=nodes, bonds=edges); predict toxicity, solubility, binding affinity |
| **Drug-drug interaction** | Model drugs and targets as a graph; predict adverse interactions |
| **De novo drug design** | Generate novel molecular graphs with desired properties |

### Recommendation Systems

| Approach | Description |
|----------|-------------|
| **User-item graph** | Users and items are nodes; purchases/views are edges |
| **Graph-based collaborative filtering** | GNNs propagate preferences through the graph |
| **Knowledge graph recommendations** | Combine user preferences with item knowledge (genres, actors, directors) |

### Fraud Detection

| Application | Graph Structure |
|-------------|----------------|
| **Financial fraud** | Transactions form a graph; fraudulent patterns emerge as subgraph structures |
| **Insurance fraud** | Claimants, providers, and policies form a graph; rings of fraudsters are detected |
| **Account takeovers** | Login patterns form a graph; anomalous connections signal compromise |

### Knowledge Graphs

| Task | Description |
|------|-------------|
| **Link prediction** | Predict missing facts (e.g., "Paris is the capital of ?") |
| **Entity resolution** | Determine if two mentions refer to the same entity |
| **Question answering** | Navigate the graph to find answers |

---

## Advanced GNN Concepts

### Over-Smoothing

| Problem | Description | Solution |
|---------|-------------|----------|
| **Over-smoothing** | After many layers, all node representations become similar | Limit depth (2-4 layers); use residual connections; use Jumping Knowledge |

### Over-Squashing

| Problem | Description | Solution |
|---------|-------------|----------|
| **Over-squashing** | Information from distant nodes is compressed into fixed-size vectors | Use graph transformers; hierarchical pooling |

### Graph Transformers

| Model | Key Feature |
|-------|-------------|
| **Graph Transformer** | Apply standard Transformer attention to all node pairs |
| **GPS** (Graph Prompting System) | Combine local GNN layers with global Transformer layers |
| **Graphormer** | Add positional encoding based on graph structure |

### Heterogeneous Graph Networks

| Model | Description |
|-------|-------------|
| **R-GCN** | Relational GCN; different weight matrices for different edge types |
| **HAN** | Heterogeneous Attention Network; attention over different node and edge types |
| **HetGNN** | Heterogeneous Graph Neural Network; handles multiple node types |

---

## Scalability

| Challenge | Solution |
|-----------|----------|
| **Large graphs** (millions of nodes) | Mini-batch training; neighbour sampling |
| **Memory** | Graph partitioning across GPUs |
| **Speed** | Sparse matrix operations; specialised libraries |

### Sampling Strategies

| Strategy | Description |
|----------|-------------|
| **Node sampling** | Sample a subset of nodes and their K-hop neighbourhoods |
| **Edge sampling** | Sample edges and the nodes they connect |
| **Cluster sampling** | Partition the graph into clusters; train on clusters |
| **Random walk sampling** | Sample nodes via random walks from target nodes |

---

## Tools and Frameworks

| Tool | Purpose |
|------|---------|
| **PyTorch Geometric (PyG)** | Most popular GNN library; rich set of models and datasets |
| **DGL** (Deep Graph Library) | Framework-agnostic; supports PyTorch, TensorFlow, MXNet |
| **NetworkX** | Classical graph algorithms; data manipulation |
| **OGB** (Open Graph Benchmark) | Standard benchmarks and datasets for GNN research |
| **CogDL** | Deep learning for graphs; research-oriented |
| **Spektral** | GNN library for TensorFlow/Keras |

---

## Summary

Graph Neural Networks extend deep learning to relational data — networks, molecules, knowledge graphs, and any system where entities are connected. They work by passing messages between neighbours, allowing each node to learn from its local context. GNNs have found their strongest applications in drug discovery, recommendation systems, fraud detection, and knowledge graphs. The field is evolving toward graph transformers, heterogeneous graphs, and scalable training for massive real-world networks. If your data has relationships, GNNs are probably worth considering.
