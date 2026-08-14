---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Data Structures and Algorithms

Data structures are the ways we organise data in memory so that operations on it are efficient. Algorithms are the step-by-step procedures for solving problems. Together, they form the foundation of computer science — every program you've ever used relies on them. Choosing the right data structure can turn an impossibly slow program into a fast one, and knowing the right algorithm can turn an unsolvable problem into a trivial one.

---

## Fundamental Data Structures

### Linear Structures

| Structure | Access | Search | Insert | Delete | Use Case |
|-----------|--------|--------|--------|--------|----------|
| **Array** | O(1) by index | O(n) | O(n) | O(n) | Fixed-size collections; random access |
| **Linked List** | O(n) | O(n) | O(1) at head | O(1) at head | Dynamic size; insertions/deletions |
| **Stack** | O(n) | O(n) | O(1) push/pop | O(1) pop | Function calls; undo; parsing |
| **Queue** | O(n) | O(n) | O(1) enqueue | O(1) dequeue | Task scheduling; BFS; message queues |
| **Deque** | O(1) at both ends | O(n) | O(1) at both ends | O(1) at both ends | Sliding window; work-stealing |

### Hash-Based Structures

| Structure | Search | Insert | Delete | Use Case |
|-----------|--------|--------|--------|----------|
| **Hash Table** | O(1) average | O(1) average | O(1) average | Key-value lookups; caches; sets |
| **Hash Set** | O(1) | O(1) | O(1) | Membership testing; deduplication |

**Hash collisions**: when two keys hash to the same slot, they're stored in a linked list (chaining) or the next available slot (open addressing). Good hash functions minimise collisions.

### Tree Structures

| Structure | Search | Insert | Delete | Use Case |
|-----------|--------|--------|--------|----------|
| **Binary Search Tree** | O(log n) average | O(log n) | O(log n) | Sorted data; range queries |
| **AVL / Red-Black Tree** | O(log n) guaranteed | O(log n) | O(log n) | Self-balancing; used in maps/sets |
| **B-Tree / B+ Tree** | O(log n) | O(log n) | O(log n) | Database indexes; file systems |
| **Trie** | O(k) where k = key length | O(k) | O(k) | Autocomplete; prefix matching |
| **Heap (Binary)** | O(n) | O(log n) | O(log n) | Priority queues; scheduling |

### Graph Representations

| Representation | Space | Edge Lookup | Add Edge | Iterate Neighbours |
|---------------|-------|-------------|----------|-------------------|
| **Adjacency matrix** | O(V²) | O(1) | O(1) | O(V) |
| **Adjacency list** | O(V + E) | O(degree) | O(1) | O(degree) |
| **Edge list** | O(E) | O(E) | O(1) | O(E) |

---

## Algorithm Complexity (Big-O)

Big-O notation describes how an algorithm's time or space requirements grow as the input size increases.

| Complexity | Name | Example |
|-----------|------|---------|
| **O(1)** | Constant | Hash table lookup; array access by index |
| **O(log n)** | Logarithmic | Binary search; balanced tree operations |
| **O(n)** | Linear | Linear search; iterating an array |
| **O(n log n)** | Linearithmic | Merge sort; heap sort; most efficient general-purpose sorts |
| **O(n²)** | Quadratic | Bubble sort; nested loops over the same data |
| **O(2^n)** | Exponential | Brute-force subset generation; naive recursive Fibonacci |
| **O(n!)** | Factorial | Travelling salesman (brute force); permutations |

### Common Misconceptions

| Misconception | Reality |
|--------------|---------|
| "O(n) is always faster than O(n²)" | For small n, the constant factor matters more |
| "Lower Big-O is always better" | Space-time trade-offs exist; O(1) lookup uses O(n) memory |
| "Big-O tells you exact speed" | It describes growth rate, not absolute time |

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|-----------|------|---------|-------|-------|--------|----------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No |

**Practical advice**: use your language's built-in sort (Python's `sorted()`, JavaScript's `Array.sort()`). They use highly optimised algorithms (Tim Sort, Introsort) that handle all edge cases.

---

## Searching Algorithms

| Algorithm | Data Structure | Complexity | Requirement |
|-----------|---------------|-----------|-------------|
| **Linear search** | Any | O(n) | None |
| **Binary search** | Sorted array | O(log n) | Data must be sorted |
| **Hash table lookup** | Hash table | O(1) average | Good hash function |
| **BFS** (Breadth-First Search) | Graph / tree | O(V + E) | Unweighted shortest path |
| **DFS** (Depth-First Search) | Graph / tree | O(V + E) | Path finding; cycle detection |
| **Dijkstra's** | Weighted graph | O((V + E) log V) | Non-negative weights; shortest path |
| **A* Search** | Weighted graph | O((V + E) log V) | Heuristic-guided; optimal with admissible heuristic |

---

## Key Algorithm Patterns

| Pattern | Description | Example Problems |
|---------|-------------|-----------------|
| **Divide and conquer** | Split problem into sub-problems; solve recursively; combine | Merge sort; quicksort; binary search |
| **Dynamic programming** | Break into overlapping sub-problems; cache results | Fibonacci; knapsack; longest common subsequence |
| **Greedy** | Make the locally optimal choice at each step | Dijkstra's; Huffman coding; activity selection |
| **Backtracking** | Try possibilities; undo bad choices; try alternatives | Sudoku solver; N-queens; permutations |
| **Sliding window** | Maintain a window of elements; slide it across the data | Maximum sum subarray of size K; longest substring without repeats |
| **Two pointers** | Use two pointers moving toward each other or in the same direction | Pair sum in sorted array; remove duplicates |
| **Binary search on answer** | Binary search the answer space | Allocate minimum pages; aggressive cows |

---

## When to Use What

| Problem | Data Structure | Algorithm |
|---------|---------------|-----------|
| Fast key-value lookup | Hash table / dictionary | Hashing |
| Maintain sorted order | Balanced BST (TreeMap, std::set) | Tree operations |
| Priority-based processing | Heap / priority queue | Heap operations |
| Shortest path (unweighted) | Graph (adjacency list) | BFS |
| Shortest path (weighted) | Graph (adjacency list) | Dijkstra's / A* |
| Membership testing | Hash set / Bloom filter | Hashing |
| Prefix matching | Trie | Trie traversal |
| Range queries | Segment tree / Fenwick tree | Tree operations |
| LRU cache | Hash map + doubly linked list | Combined operations |
| Connected components | Disjoint Set Union (Union-Find) | Union and Find |

---

## Summary

Data structures and algorithms are not just interview topics — they're the building blocks of efficient software. Arrays and hash tables handle most everyday needs. Trees and graphs handle hierarchical and relational data. Sorting and searching are solved problems in standard libraries. The algorithmic patterns — divide and conquer, dynamic programming, greedy, backtracking — are reusable strategies for tackling new problems. The key skill isn't memorising algorithms; it's recognising which pattern fits a given problem and choosing the right data structure for the job.
