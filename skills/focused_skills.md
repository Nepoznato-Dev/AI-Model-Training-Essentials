# 🎯 Focused Skills Library

We've consolidated 40+ skill categories into **10 essential, well-developed skills** that directly support your AI learning journey.

Each skill includes:
- ✅ Clear learning objectives
- ✅ Practice exercises with solutions
- ✅ Common mistakes to avoid
- ✅ Direct links to relevant guides
- ✅ Portfolio project ideas

---

## Core Skills Matrix

| Skill | Priority | Related Guide | Practice Project | Time |
|-------|----------|---------------|------------------|------|
| 1. Debugging AI Code | 🔴 Critical | All Guides | Broken RAG Fix | 2 weeks |
| 2. Python for AI | 🔴 Critical | Prerequisites | Data Pipeline | 2 weeks |
| 3. PyTorch Fundamentals | 🔴 Critical | Infrastructure | Custom Layers | 3 weeks |
| 4. Data Preprocessing | 🟠 High | All Guides | Clean & Prepare Dataset | 2 weeks |
| 5. Model Evaluation | 🟠 High | Infrastructure | Metrics Dashboard | 2 weeks |
| 6. Prompt Engineering | 🟠 High | RAG, Transformers | Prompt Library | 1 week |
| 7. API Integration | 🟠 High | Orchestration | Multi-API Agent | 2 weeks |
| 8. Version Control for ML | 🟡 Medium | All Guides | Experiment Tracking | 1 week |
| 9. Performance Optimization | 🟡 Medium | Infrastructure | Speed-Up Challenge | 2 weeks |
| 10. Documentation | 🟡 Medium | All Guides | README Portfolio | 1 week |

---

## 1. Debugging AI Code 🔴

**Why it matters:** Beginners spend 80% of their time debugging. Master this early!

### Learning Objectives
- [ ] Read and understand error messages
- [ ] Use debuggers effectively
- [ ] Isolate problems systematically
- [ ] Fix common AI/ML errors

### Practice Exercise: Broken RAG System

You're given a deliberately broken RAG implementation. Your task: fix all bugs.

```python
# BROKEN CODE - Can you find all 5 bugs?
import torch
from sentence_transformers import SentenceTransformer

def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def create_embeddings(documents, model):
    embeddings = model.encode(documents)  # Bug 1: Missing convert_to_numpy
    return embeddings

def search(query_embedding, index, k=3):
    scores, indices = index.search(query_embedding, k)
    return scores, indices  # Bug 2: Not handling FAISS output format

def main():
    documents = ["Doc 1", "Doc 2", "Doc 3"]
    model = load_model()
    embeddings = create_embeddings(documents, model)
    
    query = "test query"
    query_emb = model.encode([query])  # Bug 3: Inconsistent shape
    results = search(query_emb, index)  # Bug 4: index not defined
    
    print(f"Found {len(results)} results")  # Bug 5: Wrong result handling

if __name__ == "__main__":
    main()
```

<details>
<summary><strong>💡 Click for Hints</strong></summary>

1. Check the return type expected by FAISS
2. Look at variable scoping
3. Verify tensor/array shapes match
4. Check function signatures
5. Trace the data flow

</details>

<details>
<summary><strong>✅ Click for Solutions</strong></summary>

```python
# FIXED CODE
import torch
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def create_embeddings(documents, model):
    # Fix 1: Add convert_to_numpy=True
    embeddings = model.encode(documents, convert_to_numpy=True)
    return embeddings

def search(query_embedding, index, k=3):
    # Fix 2: Properly handle FAISS output
    scores, indices = index.search(query_embedding, k)
    return list(zip(scores[0], indices[0]))

def main():
    documents = ["Doc 1", "Doc 2", "Doc 3"]
    model = load_model()
    embeddings = create_embeddings(documents, model)
    
    # Create index (Fix 4: define index)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    faiss.normalize_L2(embeddings)
    index.add(embeddings)
    
    query = "test query"
    # Fix 3: Consistent shape - use [query] not query
    query_emb = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(query_emb)
    
    results = search(query_emb, index)
    
    # Fix 5: Correct result handling
    print(f"Found {len(results)} results:")
    for score, idx in results:
        print(f"  Score: {score:.4f}, Doc: {documents[idx]}")

if __name__ == "__main__":
    main()
```

</details>

### Common Mistakes
1. ❌ Not reading full error messages
2. ❌ Changing multiple things at once
3. ❌ Not using print statements to trace values
4. ❌ Ignoring shape mismatches
5. ❌ Not checking documentation

### Resources
- [Common Errors Directory](../errors/)
- [Python Debugger Tutorial](https://docs.python.org/3/library/pdb.html)
- [PyTorch Debugging Guide](https://pytorch.org/docs/stable/notes/debugging.html)

---

## 2. Python for AI 🔴

**Why it matters:** Python is the language of AI. Master these essentials.

### 10 Essential Concepts

1. **Variables & Data Types**
2. **Lists & List Comprehensions**
3. **Dictionaries**
4. **Functions & Lambda**
5. **NumPy Arrays**
6. **Tensor Operations**
7. **Classes & Objects**
8. **Error Handling**
9. **File I/O**
10. **Importing Libraries**

### Practice Exercise: Build a Data Pipeline

```python
# Your task: Complete this data preprocessing pipeline
import numpy as np

def load_data(filepath):
    """Load data from file"""
    # TODO: Implement file loading
    pass

def clean_text(texts):
    """Remove special characters and normalize"""
    # TODO: Implement text cleaning
    pass

def create_features(texts):
    """Convert text to numerical features"""
    # TODO: Implement feature extraction
    pass

def save_features(features, filepath):
    """Save processed features"""
    # TODO: Implement saving
    pass

# Test your pipeline
if __name__ == "__main__":
    sample_texts = [
        "Hello World!",
        "AI is amazing.",
        "Python makes coding easy."
    ]
    
    cleaned = clean_text(sample_texts)
    features = create_features(cleaned)
    print(f"Created features with shape: {features.shape}")
```

### Quick Reference Card

```python
# List comprehension
squares = [x**2 for x in range(10)]

# Dictionary creation
word_counts = {word: texts.count(word) for word in unique_words}

# NumPy operations
arr = np.array([1, 2, 3])
normalized = arr / np.linalg.norm(arr)

# Tensor operations
import torch
tensor = torch.randn(3, 4)
result = torch.matmul(tensor, tensor.T)
```

---

## 3. PyTorch Fundamentals 🔴

**Why it matters:** PyTorch is the most popular deep learning framework.

### Learning Objectives
- [ ] Understand tensors and operations
- [ ] Build neural network layers
- [ ] Implement custom modules
- [ ] Use autograd for backpropagation

### Practice Exercise: Custom Layer

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CustomAttention(nn.Module):
    """
    Build a simple attention mechanism from scratch
    """
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        # TODO: Initialize weights
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        
        # Your code here
        self.query = nn.Linear(embed_dim, embed_dim)
        self.key = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)
        
    def forward(self, x):
        # TODO: Implement forward pass
        batch_size, seq_len, _ = x.shape
        
        # Your code here
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)
        
        # Compute attention scores
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.embed_dim ** 0.5)
        attention = F.softmax(scores, dim=-1)
        
        # Apply attention to values
        output = torch.matmul(attention, V)
        
        return output

# Test your layer
if __name__ == "__main__":
    batch_size = 2
    seq_len = 10
    embed_dim = 64
    
    # Create sample input
    x = torch.randn(batch_size, seq_len, embed_dim)
    
    # Create and test layer
    attention = CustomAttention(embed_dim, num_heads=4)
    output = attention(x)
    
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    assert output.shape == x.shape, "Output shape should match input"
    print("✓ Custom attention layer works!")
```

---

## 4-10. Additional Skills

Due to space, here are summaries of remaining skills:

### 4. Data Preprocessing 🟠
- Handle missing values
- Normalize/scale features
- Text tokenization
- Image augmentation
- **Project:** Build a complete data cleaning pipeline

### 5. Model Evaluation 🟠
- Accuracy, Precision, Recall, F1
- Confusion matrices
- ROC curves
- Cross-validation
- **Project:** Create an evaluation dashboard

### 6. Prompt Engineering 🟠
- Zero-shot prompting
- Few-shot examples
- Chain-of-thought
- Role prompting
- **Project:** Build a prompt library for common tasks

### 7. API Integration 🟠
- REST APIs
- Authentication
- Rate limiting
- Error handling
- **Project:** Multi-API agent system

### 8. Version Control for ML 🟡
- Git basics
- DVC for data versioning
- Experiment tracking
- Model registry
- **Project:** Track experiments with Git + DVC

### 9. Performance Optimization 🟡
- Vectorization
- Batch processing
- GPU utilization
- Memory management
- **Project:** Optimize slow inference code 10x

### 10. Documentation 🟡
- README writing
- Code comments
- API documentation
- Technical blogging
- **Project:** Document your portfolio projects

---

## 📊 Skill Progression Tracker

Use this table to track your progress:

| Skill | Started | Practiced | Mastered | Projects Completed |
|-------|---------|-----------|----------|-------------------|
| Debugging | [ ] | [ ] | [ ] | [ ] |
| Python | [ ] | [ ] | [ ] | [ ] |
| PyTorch | [ ] | [ ] | [ ] | [ ] |
| Data Prep | [ ] | [ ] | [ ] | [ ] |
| Evaluation | [ ] | [ ] | [ ] | [ ] |
| Prompts | [ ] | [ ] | [ ] | [ ] |
| APIs | [ ] | [ ] | [ ] | [ ] |
| Version Control | [ ] | [ ] | [ ] | [ ] |
| Optimization | [ ] | [ ] | [ ] | [ ] |
| Documentation | [ ] | [ ] | [ ] | [ ] |

---

## 🎯 Next Steps

1. **Pick one skill** to focus on this week
2. **Complete the practice exercise**
3. **Build a small project** using that skill
4. **Document your learning** (blog post or README)
5. **Move to the next skill**

Remember: Depth over breadth! Master these 10 skills thoroughly rather than skimming 40 superficially.

---

*For detailed guides on each skill, see the individual skill directories.*
