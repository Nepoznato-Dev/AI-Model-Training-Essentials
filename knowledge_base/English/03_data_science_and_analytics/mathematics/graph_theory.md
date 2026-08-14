---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Graph Theory

A **graph** is a mathematical structure consisting of vertices (nodes) connected by edges (links). Graphs model relationships: social networks, road maps, neural networks, dependencies, communication channels. Graph theory — the study of these structures — provides algorithms and theorems that are central to computer science, operations research, and data science.

---

## Fundamental Concepts

### Definitions

| Term | Definition | Notation |
|------|------------|----------|
| **Graph** | A pair G = (V, E) of vertices and edges | G |
| **Vertex (node)** | An element of V | v, u, w |
| **Edge** | A connection between two vertices | e = (u, v) or {u, v} |
| **Order** | Number of vertices | \|V\| = n |
| **Size** | Number of edges | \|E\| = m |
| **Degree** | Number of edges incident to a vertex | deg(v) |
| **Path** | Sequence of distinct vertices connected by edges | v₁, v₂, ..., vₖ |
| **Cycle** | A path that starts and ends at the same vertex | v₁ → v₂ → ... → vₖ → v₁ |
| **Connected** | A path exists between every pair of vertices | — |
| **Component** | A maximal connected subgraph | — |
| **Subgraph** | A graph formed from a subset of V and E | H ⊆ G |

### Types of Graphs

| Type | Description | Example |
|------|-------------|---------|
| **Undirected** | Edges have no direction | Friendship network |
| **Directed (digraph)** | Edges have direction (arcs) | Web page links |
| **Weighted** | Edges carry numerical values | Road distances |
| **Unweighted** | All edges are equivalent | Social connections |
| **Simple** | No loops, no multiple edges | Most textbook graphs |
| **Multigraph** | Multiple edges between same vertices allowed | Flight routes (multiple flights between cities) |
| **Complete** | Every pair of vertices is connected | Kₙ has n(n−1)/2 edges |
| **Bipartite** | Vertices split into two groups; edges only cross groups | User-item recommendation matrices |
| **Planar** | Can be drawn without edge crossings | Circuit board layouts |
| **Tree** | Connected, acyclic graph | Decision trees, file systems |
| **DAG** | Directed, no directed cycles | Task scheduling, dependency graphs |

### The Handshaking Lemma

The sum of all vertex degrees equals twice the number of edges:
Σᵥ deg(v) = 2|E|

**Corollary:** Every graph has an even number of odd-degree vertices.

**Example:** In a party of 10 people where everyone shakes hands with exactly 3 others: Σ deg = 30, so |E| = 15 handshakes total.

---

## Graph Representations

How you store a graph in memory determines the efficiency of every algorithm you run on it.

| Representation | Space | Edge Lookup | Iterate Neighbours | Best For |
|----------------|-------|-------------|--------------------|----------|
| **Adjacency Matrix** | O(n²) | O(1) | O(n) | Dense graphs, quick edge tests |
| **Adjacency List** | O(n + m) | O(deg(v)) | O(deg(v)) | Sparse graphs, most real-world networks |
| **Edge List** | O(m) | O(m) | O(m) | Simple algorithms, Kruskal's MST |
| **Incidence Matrix** | O(n · m) | O(m) | O(m) | Specialised algorithms |

### Adjacency Matrix

An n × n matrix A where A[i][j] = 1 if edge (i,j) exists, 0 otherwise. For weighted graphs, A[i][j] = weight.

**Properties:**
- Symmetric for undirected graphs
- Aᵏ[i][j] = number of walks of length k from i to j
- Eigenvalues of A reveal structural properties (see Spectral Graph Theory)

### Adjacency List

An array (or hash map) where each vertex v stores a list of its neighbours.

```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

This is the most common representation for real-world graphs, which are typically sparse (m ≪ n²).

---

## Trees

A **tree** is a connected, acyclic undirected graph. A **forest** is a disjoint union of trees.

### Properties of Trees

For a tree with n vertices:
- It has exactly n − 1 edges
- There is exactly one path between any two vertices
- Removing any edge disconnects it
- Adding any edge creates exactly one cycle

### Types of Trees

| Type | Description | Application |
|------|-------------|-------------|
| **Rooted tree** | One vertex designated as root | File systems, organisational charts |
| **Binary tree** | Each node has at most 2 children | BSTs, expression parsing, decision trees |
| **Balanced tree** | Height is O(log n) | AVL trees, red-black trees (databases) |
| **Spanning tree** | Subgraph that includes all vertices and is a tree | Network design, approximation algorithms |
| **Minimum spanning tree** | Spanning tree with minimum total edge weight | Network design, clustering |
| **Star graph** | One central node connected to all others | Hub-and-spoke networks |

### Binary Tree Properties

| Property | Formula |
|----------|---------|
| Max nodes at depth d | 2ᵈ |
| Max nodes in tree of height h | 2ʰ⁺¹ − 1 |
| Min height for n nodes | ⌊log₂(n)⌋ |
| Leaf nodes in full binary tree | Internal nodes + 1 |

### Tree Traversals

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Pre-order** | Root → Left → Right | Copying a tree, prefix expression |
| **In-order** | Left → Root → Right | Sorted output from BST |
| **Post-order** | Left → Right → Root | Deleting a tree, postfix expression |
| **Level-order (BFS)** | Level by level, left to right | Shortest path in unweighted tree |

---

## Graph Traversals

Traversal algorithms visit every reachable vertex systematically.

### Breadth-First Search (BFS)

Explores vertices layer by layer, using a **queue**.

| Property | Value |
|----------|-------|
| Data structure | Queue (FIFO) |
| Time complexity | O(V + E) |
| Space complexity | O(V) |
| Finds shortest path? | Yes (unweighted graphs) |
| Complete? | Yes (explores all reachable vertices) |

**Algorithm:**
1. Start at source vertex s. Mark s visited. Enqueue s.
2. While queue is not empty: dequeue vertex u. For each unvisited neighbour v of u: mark v visited, enqueue v.

**Applications:** shortest path in unweighted graphs, connected components, bipartiteness testing, web crawling.

### Depth-First Search (DFS)

Explores as deep as possible before backtracking, using a **stack** (or recursion).

| Property | Value |
|----------|-------|
| Data structure | Stack (LIFO) / recursion |
| Time complexity | O(V + E) |
| Space complexity | O(V) |
| Finds shortest path? | No |
| Complete? | Yes (for finite graphs) |

**Algorithm:**
1. Start at vertex s. Mark s visited.
2. For each unvisited neighbour v of s: recursively DFS from v.

**DFS classifies edges into:**
- **Tree edges:** part of the DFS tree
- **Back edges:** connect a vertex to its ancestor (indicate cycles)
- **Forward edges:** connect a vertex to its descendant
- **Cross edges:** connect vertices in different branches

**Applications:** topological sorting, cycle detection, strongly connected components, solving mazes.

### BFS vs DFS Comparison

| Criterion | BFS | DFS |
|-----------|-----|-----|
| Strategy | Wide then deep | Deep then wide |
| Memory | Higher (stores frontier) | Lower (stores path) |
| Shortest path (unweighted) | Guaranteed | Not guaranteed |
| Use when solution is close to start | Better | Worse |
| Use when graph is very deep | Worse | Better |
| Topological sorting | Kahn's algorithm variant | Standard approach |

---

## Shortest Path Algorithms

Finding the shortest path between vertices is one of the most practically important graph problems.

### Dijkstra's Algorithm

Finds shortest paths from a single source to all other vertices in a graph with **non-negative** edge weights.

| Property | Value |
|----------|-------|
| Edge weights | Must be ≥ 0 |
| Time (binary heap) | O((V + E) log V) |
| Time (Fibonacci heap) | O(E + V log V) |
| Greedy? | Yes |
| Handles negative weights? | No |

**Algorithm:**
1. Initialize dist[s] = 0, dist[v] = ∞ for all v ≠ s. Priority queue Q with all vertices.
2. While Q is not empty: extract vertex u with minimum dist. For each neighbour v of u with edge weight w: if dist[u] + w < dist[v], update dist[v] = dist[u] + w.

**Worked Example:**
```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Bellman-Ford Algorithm

Handles **negative** edge weights and detects negative cycles.

| Property | Value |
|----------|-------|
| Edge weights | Any (detects negative cycles) |
| Time complexity | O(V · E) |
| Space complexity | O(V) |
| Handles negative cycles? | Yes (detects and reports) |

**Algorithm:**
1. Initialize dist[s] = 0, dist[v] = ∞ for all v ≠ s.
2. Repeat V − 1 times: for each edge (u, v) with weight w: if dist[u] + w < dist[v], update dist[v].
3. Check for negative cycles: if any edge can still be relaxed, a negative cycle exists.

### Floyd-Warshall Algorithm

Finds shortest paths between **all pairs** of vertices.

| Property | Value |
|----------|-------|
| Time complexity | O(V³) |
| Space complexity | O(V²) |
| Handles negative weights? | Yes (but not negative cycles) |
| Approach | Dynamic programming |

**Recurrence:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) for each intermediate vertex k.

### Algorithm Selection Guide

| Scenario | Algorithm |
|----------|-----------|
| Single source, non-negative weights | Dijkstra |
| Single source, negative weights possible | Bellman-Ford |
| All pairs, dense graph | Floyd-Warshall |
| All pairs, sparse graph | Run Dijkstra from each vertex |
| Unweighted graph | BFS |
| DAG (no cycles) | Topological sort + relaxation |
| A* (heuristic-guided) | A* search (for pathfinding with good heuristic) |

---

## Minimum Spanning Trees

A **minimum spanning tree (MST)** connects all vertices with minimum total edge weight.

### Properties

- An MST has exactly n − 1 edges (for n vertices)
- An MST exists iff the graph is connected
- A graph with distinct edge weights has a unique MST
- MST satisfies the **cut property**: the minimum-weight edge crossing any cut belongs to the MST
- MST satisfies the **cycle property**: the maximum-weight edge in any cycle does not belong to the MST

### Kruskal's Algorithm

| Property | Value |
|----------|-------|
| Strategy | Greedy — add edges in weight order |
| Data structure | Disjoint-set (union-find) |
| Time complexity | O(E log E) |
| Best for | Sparse graphs |

**Algorithm:**
1. Sort all edges by weight.
2. For each edge (in order): if adding it doesn't create a cycle (check with union-find), add it to the MST.
3. Stop when n − 1 edges are selected.

### Prim's Algorithm

| Property | Value |
|----------|-------|
| Strategy | Greedy — grow tree from a starting vertex |
| Data structure | Priority queue (min-heap) |
| Time complexity | O(E log V) with binary heap |
| Best for | Dense graphs |

**Algorithm:**
1. Start from any vertex. Mark it as part of the MST.
2. Repeatedly add the minimum-weight edge connecting a vertex in the MST to a vertex outside it.
3. Stop when all vertices are included.

### MST Applications

| Application | How MST Helps |
|-------------|---------------|
| Network design | Lay minimum cable/pipe to connect all locations |
| Clustering | Remove the k − 1 longest MST edges to get k clusters |
| Approximation algorithms | 2-approximation for metric TSP |
| Image segmentation | Group pixels by MST of colour similarity |
| Feature elimination | Remove redundant features using MST of correlation graph |

---

## Network Flow

Network flow problems model the movement of resources through a system.

### Flow Network Definition

A **flow network** is a directed graph with:
- A **source** vertex s (produces flow)
- A **sink** vertex t (consumes flow)
- **Capacities** c(u,v) ≥ 0 on each edge
- **Flow** f(u,v) satisfying:
  - **Capacity constraint:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Flow conservation:** flow in = flow out at every vertex except s and t

### Maximum Flow Problem

Find the maximum total flow from s to t.

**Ford-Fulkerson Method:**
1. While there exists an augmenting path from s to t in the residual graph:
2. Find the bottleneck capacity along the path
3. Increase flow along the path by the bottleneck amount
4. Update residual capacities

| Algorithm | Time Complexity | Notes |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) where f* is max flow | May not terminate with irrational capacities |
| Edmonds-Karp (BFS) | O(V · E²) | Always terminates, picks shortest augmenting path |
| Dinic's Algorithm | O(V² · E) | Uses blocking flows; O(V^(1/2) · E) for unit capacities |

### Max-Flow Min-Cut Theorem

The **maximum flow** from s to t equals the **minimum cut** capacity separating s from t.

A **cut** (S, T) partitions vertices into S (containing s) and T (containing t). The cut capacity is the sum of capacities of edges from S to T.

**Applications of max flow:**
- Bipartite matching (assign workers to jobs)
- Image segmentation (separate foreground from background)
- Baseball elimination (can team X still win?)
- Network reliability (maximum data throughput)

### Bipartite Matching via Max Flow

Given a bipartite graph G = (L ∪ R, E):
1. Add source s with edges to all vertices in L (capacity 1)
2. Add sink t with edges from all vertices in R (capacity 1)
3. Set all original edge capacities to 1
4. Maximum flow = maximum matching

---

## Spectral Graph Theory

Spectral graph theory studies graphs through the eigenvalues and eigenvectors of matrices associated with the graph.

### Key Matrices

| Matrix | Definition | What It Captures |
|--------|------------|------------------|
| **Adjacency matrix** A | A[i][j] = 1 if edge (i,j) exists | Connectivity pattern |
| **Degree matrix** D | Diagonal; D[i][i] = deg(i) | Vertex importance by degree |
| **Laplacian** L = D − A | L[i][j] = −1 if edge, deg(i) on diagonal | Smoothness of functions on graph |
| **Normalised Laplacian** L_norm = D^(−1/2) L D^(−1/2) | Scale-invariant version | Community structure |

### Eigenvalues of the Laplacian

The Laplacian L is positive semi-definite, so all eigenvalues are ≥ 0.

| Eigenvalue | Meaning |
|------------|---------|
| λ₁ = 0 | Always zero; eigenvector is the constant vector |
| λ₂ (algebraic connectivity) | > 0 iff graph is connected; larger = better connected |
| Number of zero eigenvalues | Equals number of connected components |
| λₙ | Related to maximum degree and graph expansion |

### Applications of Spectral Methods

| Application | Method |
|-------------|--------|
| **Graph partitioning** | Use eigenvectors of L to split graph into balanced parts |
| **Community detection** | Spectral clustering: embed vertices using bottom eigenvectors, then cluster |
| **PageRank** | Eigenvector of the adjacency matrix (or transition matrix) of the web graph |
| **Graph drawing** | Position vertices using eigenvectors of the Laplacian |
| **Semi-supervised learning** | Propagate labels using the graph Laplacian (label propagation) |
| **Graph neural networks** | Spectral convolutions: filter signals on graphs using eigenvectors of L |

### Cheeger's Inequality

Relates the second eigenvalue λ₂ to the graph's **expansion** (how well-connected it is):

λ₂ / 2 ≤ h(G) ≤ √(2λ₂)

where h(G) is the Cheeger constant (isoperimetric number). This means λ₂ approximately measures how hard it is to cut the graph into two pieces — a key insight for clustering.

---

## Special Graph Structures

| Graph | Vertices | Edges | Properties |
|-------|----------|-------|------------|
| Complete Kₙ | n | n(n−1)/2 | Every pair connected; diameter 1 |
| Cycle Cₙ | n | n | 2-regular; connected |
| Path Pₙ | n | n−1 | Tree; diameter n−1 |
| Hypercube Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-regular; diameter k; bipartite |
| Complete bipartite K_{m,n} | m+n | m·n | Every vertex in one part connects to all in other |
| Petersen graph | 10 | 15 | 3-regular; diameter 2; not planar; no Hamiltonian cycle |

---

## Relevance to Machine Learning and Data Science

| Graph Concept | Application |
|---------------|-------------|
| BFS / DFS | Web crawling, social network analysis, connected component labelling |
| Dijkstra / A* | Route planning, game AI pathfinding, robotics navigation |
| Minimum spanning tree | Clustering (single-linkage), feature selection, network design |
| Max flow / min cut | Image segmentation, bipartite matching, recommendation assignment |
| Spectral methods | Spectral clustering, graph neural networks, dimensionality reduction (Laplacian eigenmaps) |
| PageRank | Search engine ranking, influence analysis in social networks |
| DAGs | Bayesian networks, causal inference, task scheduling, computation graphs in deep learning |
| Bipartite graphs | User-item matrices in recommender systems, two-sided markets |
| Tree structures | Decision trees, random forests, hierarchical clustering, file system navigation |
| Graph representations | Knowledge graphs (Wikidata, DBpedia), molecular graphs (drug discovery), citation networks |

---

## Summary

| Topic | Core Idea | Key Algorithm / Result |
|-------|-----------|----------------------|
| Fundamentals | Vertices, edges, degrees, paths | Handshaking lemma |
| Representations | How to store graphs | Adjacency matrix vs adjacency list |
| Trees | Connected acyclic graphs | n vertices → n−1 edges |
| Traversals | Systematic vertex exploration | BFS (shortest path), DFS (deep exploration) |
| Shortest Paths | Minimum-weight routes | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Minimum Spanning Tree | Cheapest way to connect all vertices | Kruskal's, Prim's |
| Network Flow | Maximum throughput | Ford-Fulkerson, max-flow min-cut theorem |
| Spectral Theory | Eigenvalues reveal structure | Laplacian eigenvalues, spectral clustering |

Graph theory is arguably the most directly applicable branch of mathematics to modern data science. Social networks, knowledge graphs, molecular structures, computation graphs in deep learning frameworks, dependency resolution, recommendation systems — all are fundamentally graph problems. The algorithms covered here are not just theoretical; they run at scale in production systems every day.
