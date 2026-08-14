---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.1"
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
tags: [recommendation, systems, ai-and-machine-learning]
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
# Recommendation Systems

Recommendation systems predict what a user will want to see, buy, or interact with next. They power the content feeds on social media, product suggestions on e-commerce sites, movie picks on streaming platforms, and search results. Despite being invisible to most users, they are among the most commercially impactful AI systems in the world — Netflix estimates its recommendation engine saves over $1 billion per year by reducing subscriber churn.

---

## Why Recommendations Are Hard

| Challenge | Description |
|-----------|-------------|
| **Scale** | Millions of users × millions of items = billions of possible pairs |
| **Sparsity** | Each user has interacted with a tiny fraction of available items |
| **Cold start** | New users and new items have no interaction history |
| **Dynamic preferences** | User tastes change over time |
| **Beyond accuracy** | Recommendations must also be diverse, novel, and serendipitous |
| **Business goals** | Maximising engagement ≠ maximising user wellbeing |

---

## Core Approaches

### Collaborative Filtering

The idea: if users A and B agreed in the past, they'll probably agree in the future.

| Type | How It Works | Example |
|------|-------------|---------|
| **User-based** | Find similar users; recommend what they liked | "Users who liked this also liked..." |
| **Item-based** | Find similar items to what the user already likes | "Because you watched..." |
| **Matrix factorisation** | Decompose the user-item interaction matrix into latent factors | SVD, ALS (Alternating Least Squares) |

| Strength | Weakness |
|----------|----------|
| No need to understand the items themselves | Cold start problem: can't recommend new items |
| Captures complex, implicit preferences | Requires lots of interaction data |
| Works across any content type | Popularity bias: recommends already-popular items |

### Content-Based Filtering

Recommend items similar to ones the user already likes, based on item features.

| Feature Type | Example |
|-------------|---------|
| **Text** | Genre, description, keywords, cast |
| **Audio** | Tempo, genre, mood (for music) |
| **Visual** | Colour palette, style (for images/fashion) |
| **Metadata** | Price, brand, category |

| Strength | Weakness |
|----------|----------|
| No cold start for items (features are known) | Can't recommend items outside the user's existing taste |
| Works with less interaction data | Requires good feature engineering |
| Explainable ("recommended because it's similar to X") | Less serendipity |

### Hybrid Approaches

Most production systems combine collaborative and content-based methods.

| Hybrid Strategy | Description |
|----------------|-------------|
| **Weighted** | Combine scores from multiple models |
| **Switching** | Use content-based for new users, collaborative for established ones |
| **Cascade** | Use a simple model first, then refine with a complex one |
| **Feature combination** | Merge collaborative and content features into a single model |
| **Meta-learning** | Learn how to combine different recommenders |

---

## Modern Deep Learning Approaches

### Two-Tower Models

The dominant architecture for large-scale recommendation (used by YouTube, Pinterest, Spotify).

| Component | Role |
|-----------|------|
| **User tower** | Neural network that encodes user features and history into an embedding |
| **Item tower** | Neural network that encodes item features into an embedding |
| **Similarity** | Dot product or cosine similarity between user and item embeddings |

| Step | Description |
|------|-------------|
| 1 | Train both towers to produce similar embeddings for user-item pairs that interact |
| 2 | At serving time, pre-compute item embeddings |
| 3 | For a user request, compute user embedding |
| 4 | Use approximate nearest neighbour (ANN) search to find the most similar items |

### Sequence Models for Recommendations

User behaviour is sequential — what you watched yesterday influences what you'll watch today.

| Model | Approach |
|-------|----------|
| **GRU4Rec** | GRU-based model for session-based recommendations |
| **SASRec** | Self-attention based sequential recommender |
| **BERT4Rec** | Bidirectional Transformer for sequential recommendations |
| **YouTube DNN** | Deep neural network treating watch history as a sequence |

### Retrieval vs Ranking

Modern systems split recommendations into two stages:

| Stage | Purpose | Method |
|-------|---------|--------|
| **Retrieval (candidate generation)** | Narrow millions of items to ~1,000 candidates | Two-tower model; ANN search; fast but approximate |
| **Ranking (scoring)** | Precisely score and order the candidates | Deep model with many features; slower but accurate |
| **Re-ranking** | Adjust for diversity, business rules, freshness | Contextual bandits; constraint optimisation |

---

## Evaluation Metrics

| Metric | What It Measures | When to Use |
|--------|-----------------|-------------|
| **Precision@K** | Fraction of top-K recommendations that are relevant | When you care about accuracy of top picks |
| **Recall@K** | Fraction of relevant items found in top-K | When you care about not missing good items |
| **NDCG** (Normalised Discounted Cumulative Gain) | Ranking quality; rewards putting relevant items higher | When ranking order matters |
| **MAP** (Mean Average Precision) | Average precision across all users | Overall ranking quality |
| **Hit Rate@K** | Whether at least one relevant item appears in top-K | Binary relevance scenarios |
| **Coverage** | Fraction of items that get recommended | Diversity and fairness |
| **Serendipity** | Unexpected but relevant recommendations | User satisfaction |

---

## The Cold Start Problem

| Scenario | Challenge | Solutions |
|----------|-----------|-----------|
| **New user** | No interaction history | Use demographics; show popular items; use contextual signals (location, device, time) |
| **New item** | No one has interacted with it yet | Use content features; explore-exploit strategies; bandit algorithms |
| **New system** | No data at all | Transfer learning from similar domains; curate initial content |

---

## Exploration vs Exploitation

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| **ε-greedy** | Show random items with probability ε | Simple but inefficient |
| **Thompson sampling** | Sample from the posterior distribution of item quality | Principled; good theoretical properties |
| **Upper Confidence Bound (UCB)** | Prefer items with high uncertainty | Good balance of exploration and exploitation |
| **Contextual bandits** | Exploration conditioned on user context | More efficient than blind exploration |
| **Diversity injection** | Deliberately include diverse or novel items | Simple; may reduce short-term engagement |

---

## Bias and Fairness

| Bias Type | Description | Impact |
|-----------|-------------|--------|
| **Popularity bias** | Popular items get recommended more, becoming more popular | Long-tail items are underserved |
| **Selection bias** | Models learn from observed interactions, not all possible ones | Skewed toward active users |
| **Position bias** | Items shown in higher positions get more clicks regardless of quality | Reinforces top positions |
| **Exposure bias** | Items that have been shown get more training signal | Feedback loop |
| **Demographic bias** | Recommendations differ across demographics in unfair ways | Discrimination; poor experience for some groups |

### Mitigation Strategies

| Strategy | Description |
|----------|-------------|
| **Inverse propensity weighting** | Down-weight popular items in training |
| **Debiasing layers** | Add a debiasing component to the model |
| **Fairness constraints** | Add constraints to ensure equitable treatment |
| **Diverse recommendations** | Explicitly optimise for diversity alongside relevance |
| **Audit and monitoring** | Regularly check recommendations for bias across groups |

---

## Industry Examples

| Company | System | Approach |
|---------|--------|----------|
| **Netflix** | Movie/TV recommendations | Two-tower retrieval + deep ranking + contextual bandits for artwork |
| **YouTube** | Video recommendations | Deep neural network for candidate generation; separate ranking model |
| **Spotify** | Music recommendations | Collaborative filtering + NLP on playlists + audio analysis |
| **Amazon** | Product recommendations | Item-to-item collaborative filtering; personalised at scale |
| **TikTok** | Short video feed | Reinforcement learning; strong emphasis on exploration |
| **Pinterest** | Visual recommendations | Two-tower model; visual similarity |

---

## Tools and Frameworks

| Tool | Purpose |
|------|---------|
| **TensorFlow Recommenders (TFRS)** | Two-tower models, retrieval, ranking |
| **PyTorch RecSys** | Research-oriented recommendation models |
| **Surprise** | Classical collaborative filtering (SVD, NMF, KNN) |
| **Implicit** | Fast collaborative filtering for implicit feedback (ALS, BPR) |
| **Faiss** (Meta) | Approximate nearest neighbour search at scale |
| **Milvus / Pinecone / Weaviate** | Vector databases for similarity search |
| **Recbole** | Comprehensive recommendation research library |
| **Merlin** (NVIDIA) | GPU-accelerated recommendation pipeline |

---

## Summary

Recommendation systems are among the most impactful AI applications in industry. The field has evolved from simple collaborative filtering to deep learning architectures that combine user history, item content, contextual signals, and business objectives. Modern systems use a retrieval-ranking-re-ranking pipeline, with two-tower models for fast candidate generation and deep models for precise scoring. The challenges — cold start, bias, exploration, and balancing user satisfaction with business goals — remain active areas of research and engineering.
