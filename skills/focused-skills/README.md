# 🎯 Focused Skills Library

**Quality over quantity!** These 10 well-developed skills directly tie to specific guides and projects.

---

## 📚 The Essential 10 Skills

Each skill includes:
- ✅ Clear learning objectives
- ✅ Practice exercises
- ✅ Deliberately broken code to debug
- ✅ Connection to specific guides
- ✅ Real-world application

---

## 1. 🔍 Debugging ML Code

**Linked Guide**: [Infrastructure Layers](../guides/Infrastructure_Layers/)  
**Project**: [RAG Chatbot](../projects/rag-chatbot/)  
**Time**: 4 hours

### What You'll Learn
- Reading stack traces
- Identifying common ML errors
- Systematic debugging approach
- Using debuggers effectively

### Practice Exercise: Broken RAG Pipeline

```python
# ❌ BROKEN CODE - Find and fix the bugs!
# This RAG system has 5 intentional bugs

from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_and_embed():
    # Bug 1: Wrong path
    loader = TextLoader("sample_docs/document.tx")  # Missing 't'
    
    # Bug 2: Not loading documents
    documents = loader  # Should be loader.load()
    
    # Bug 3: Wrong model name
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v3"  # v3 doesn't exist
    )
    
    # Bug 4: Missing device specification
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        # Missing: model_kwargs={'device': 'cuda'}
    )
    
    # Bug 5: Creating vectorstore incorrectly
    vectorstore = FAISS.from_documents(
        embeddings, documents  # Arguments swapped!
    )
    
    return vectorstore

# YOUR TASK: Fix all 5 bugs and run successfully!
```

### Solution Guide
<details>
<summary>Click to reveal solutions</summary>

```python
# Fixed version:
def load_and_embed():
    # Fix 1: Correct path
    loader = TextLoader("sample_docs/document.txt")
    
    # Fix 2: Actually load documents
    documents = loader.load()
    
    # Fix 3 & 4: Correct model name + device
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cuda'}
    )
    
    # Fix 5: Correct argument order
    vectorstore = FAISS.from_documents(
        documents, embeddings  # documents first, then embeddings
    )
    
    return vectorstore
```
</details>

### Mastery Checklist
- [ ] Can read and understand error messages
- [ ] Know how to use `pdb` or IDE debugger
- [ ] Can isolate variables to find issues
- [ ] Systematically test hypotheses
- [ ] Document fixes for future reference

---

## 2. 📊 Data Preprocessing

**Linked Guide**: [RAG Chapter 2](../guides/RAG/CHAPTER_2_data_preparation.md)  
**Project**: Custom document pipeline  
**Time**: 3 hours

### What You'll Learn
- Cleaning text data
- Handling missing values
- Normalization techniques
- Quality validation

### Practice Exercise: Dirty Data Challenge

```python
# ❌ BROKEN CODE - This preprocessing pipeline fails on edge cases

import re

def clean_text(text):
    """Clean text for RAG system - has bugs!"""
    
    # Bug: Doesn't handle None input
    text = text.lower()
    
    # Bug: Removes ALL numbers (sometimes we want to keep them)
    text = re.sub(r'\d+', '', text)
    
    # Bug: Over-aggressive whitespace removal
    text = text.replace(' ', '')
    
    # Bug: Doesn't handle special characters properly
    text = text.split()
    
    return text

# Test cases that should work but don't:
test_cases = [
    "Hello World!",           # Basic case
    None,                     # Should handle gracefully
    "Price: $100",           # Should keep numbers
    "Multiple   spaces",      # Should preserve word boundaries
    "Café résumé",           # Unicode characters
]

# YOUR TASK: Fix the function to handle all test cases!
```

### Best Practices
```python
def clean_text_robust(text, keep_numbers=True):
    """Robust text cleaning with proper error handling"""
    
    # Handle None/empty
    if not text:
        return ""
    
    # Convert to string if needed
    text = str(text)
    
    # Lowercase
    text = text.lower()
    
    # Remove extra whitespace (not all!)
    text = ' '.join(text.split())
    
    # Optionally remove numbers
    if not keep_numbers:
        text = re.sub(r'\d+', '', text)
    
    # Remove special chars but keep unicode
    text = re.sub(r'[^\w\s\u00C0-\u024F]', '', text)
    
    return text.strip()
```

---

## 3. 🧠 Model Selection

**Linked Guide**: [Transformers](../guides/Transformers/)  
**Project**: Sentiment analysis comparison  
**Time**: 5 hours

### What You'll Learn
- Comparing model architectures
- Understanding trade-offs (speed vs accuracy)
- Reading model cards
- Benchmarking performance

### Practice Exercise: Model Showdown

```python
# Compare 3 transformer models for sentiment analysis

MODELS_TO_TEST = [
    "distilbert-base-uncased",      # Fast, small
    "bert-base-uncased",            # Balanced
    "roberta-large",                # Accurate, slow
]

# YOUR TASK:
# 1. Load each model
# 2. Run on same test dataset
# 3. Measure: accuracy, inference time, memory usage
# 4. Create comparison table
# 5. Recommend best model for different scenarios

# Starter code:
from transformers import pipeline
import time

def benchmark_model(model_name, texts):
    """Benchmark a model's performance"""
    
    # Load model
    classifier = pipeline("sentiment-analysis", model=model_name)
    
    # Warm up
    _ = classifier(texts[0])
    
    # Time inference
    start = time.time()
    results = classifier(texts)
    end = time.time()
    
    return {
        'model': model_name,
        'time_per_sample': (end - start) / len(texts),
        'results': results
    }

# Now complete the comparison!
```

### Decision Framework
```markdown
Choose based on your needs:

🚀 Need speed? → DistilBERT
⚖️ Balanced? → BERT-base
🎯 Need accuracy? → RoBERTa-large
💻 Limited RAM? → DistilBERT or ALBERT
📱 Mobile deployment? → TinyBERT
```

---

## 4. ⚡ Performance Optimization

**Linked Guide**: [Infrastructure Layers](../guides/Infrastructure_Layers/)  
**Project**: Optimize RAG chatbot  
**Time**: 4 hours

### What You'll Learn
- Profiling code
- Identifying bottlenecks
- Batch processing
- Caching strategies
- GPU optimization

### Practice Exercise: Speed Up This Code

```python
# ❌ SLOW CODE - Make this 10x faster!

def process_documents_slow(docs):
    """Process documents one by one - very slow!"""
    
    results = []
    
    for doc in docs:  # Bug: No batching
        # Bug: Reloading model every time
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # Bug: Not using GPU
        embedding = embeddings.embed_query(doc)
        results.append(embedding)
    
    return results

# YOUR TASK: Optimize this code!
# Tips:
# - Load model once
# - Use batch processing
# - Enable GPU
# - Use mixed precision
```

### Optimized Solution
```python
def process_documents_fast(docs, batch_size=32):
    """Optimized document processing"""
    
    # Load once
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cuda'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    # Batch process
    all_embeddings = []
    
    for i in range(0, len(docs), batch_size):
        batch = docs[i:i + batch_size]
        batch_embeddings = embeddings.embed_documents(batch)
        all_embeddings.extend(batch_embeddings)
    
    return all_embeddings

# Result: 10-50x speedup!
```

---

## 5. 🔄 Version Control for ML

**Linked Guide**: [Git Basics](../prerequisites/git_basics.md)  
**Project**: Track model experiments  
**Time**: 3 hours

### What You'll Learn
- Git LFS for large files
- DVC for data versioning
- Experiment tracking
- Reproducible workflows

### Practice Exercise: Track Your Experiments

```bash
# Setup Git LFS for model files
git lfs install
git lfs track "*.bin"
git lfs track "*.pt"
git lfs track "*.h5"

# Track data with DVC
dvc init
dvc add data/training_dataset.csv
git add data/training_dataset.csv.dvc .gitignore

# Commit with good message
git commit -m "feat: Add BERT baseline model

- Trained on 10K samples
- Achieved 87% accuracy
- Model: bert-base-uncased
- Config in configs/bert_baseline.yaml"
```

### Best Practices
```markdown
✅ DO:
- Commit code frequently
- Tag model releases
- Write descriptive commit messages
- Use branches for experiments

❌ DON'T:
- Commit large binary files without LFS
- Commit raw datasets (>100MB)
- Use vague messages like "fix stuff"
- Work only on main branch
```

---

## 6. 📝 Prompt Engineering

**Linked Guide**: [Agentic Systems](../guides/Agentic_Systems/)  
**Project**: Build better agent prompts  
**Time**: 3 hours

### What You'll Learn
- Writing effective prompts
- Few-shot learning
- Chain-of-thought reasoning
- Prompt templates

### Practice Exercise: Improve This Prompt

```python
# ❌ WEAK PROMPT - Improve it!

prompt = "Answer this question."

# Test question: "What are the pros and cons of remote work?"

# Result: Short, shallow answer

# YOUR TASK: Rewrite the prompt to get:
# - Structured response
# - Multiple perspectives
# - Evidence-based points
# - Actionable insights
```

### Improved Version
```python
# ✅ STRONG PROMPT

prompt = """You are an expert workplace consultant.

Analyze the pros and cons of remote work.

Structure your response as follows:
1. Executive Summary (2-3 sentences)
2. Pros (list 5 with brief explanations)
3. Cons (list 5 with brief explanations)
4. Recommendations for companies considering remote work

Base your analysis on research and real-world examples.
Be balanced and objective.

Question: What are the pros and cons of remote work?"""

# Result: Comprehensive, structured, actionable answer
```

---

## 7. 🧪 Testing ML Systems

**Linked Guide**: [Orchestration Patterns](../guides/Orchestration_Patterns/)  
**Project**: Add tests to RAG system  
**Time**: 4 hours

### What You'll Learn
- Unit testing ML code
- Integration testing pipelines
- Testing non-deterministic systems
- Quality assurance

### Practice Exercise: Write Tests

```python
# ❌ NO TESTS - Add test coverage!

# YOUR TASK: Write tests for this RAG function

def retrieve_documents(query, vectorstore, k=3):
    """Retrieve relevant documents for query"""
    results = vectorstore.similarity_search(query, k=k)
    return results

# Write tests for:
# 1. Normal query returns k results
# 2. Empty query handled gracefully
# 3. Very long query doesn't crash
# 4. Special characters handled
# 5. Results are actually relevant

# Starter template:
def test_retrieve_normal():
    """Test normal retrieval"""
    # Setup
    # Execute
    # Assert
    pass

def test_retrieve_empty_query():
    """Test empty query handling"""
    # Your code here
    pass
```

### Solution Template
```python
import pytest

def test_retrieve_normal(vectorstore):
    """Test normal retrieval returns k results"""
    query = "machine learning"
    results = retrieve_documents(query, vectorstore, k=3)
    
    assert len(results) == 3
    assert all(hasattr(r, 'page_content') for r in results)

def test_retrieve_empty_query(vectorstore):
    """Test empty query handled gracefully"""
    query = ""
    results = retrieve_documents(query, vectorstore, k=3)
    
    # Should return something, not crash
    assert isinstance(results, list)

def test_retrieve_long_query(vectorstore):
    """Test very long query doesn't crash"""
    query = "word " * 1000
    results = retrieve_documents(query, vectorstore, k=3)
    
    assert isinstance(results, list)
```

---

## 8. 📈 Evaluation Metrics

**Linked Guide**: All guides (applies everywhere)  
**Project**: Evaluate model performance  
**Time**: 4 hours

### What You'll Learn
- Accuracy, Precision, Recall, F1
- BLEU, ROUGE for text generation
- Perplexity for language models
- Human evaluation

### Practice Exercise: Choose Right Metric

```python
# Scenario-based exercise: Which metric to use?

scenarios = [
    {
        'task': 'Spam detection',
        'challenge': 'Many more non-spam than spam emails',
        'best_metric': '?'  # Your answer
    },
    {
        'task': 'Medical diagnosis',
        'challenge': 'Missing a disease is worse than false alarm',
        'best_metric': '?'  # Your answer
    },
    {
        'task': 'Chatbot responses',
        'challenge': 'Need fluent, relevant answers',
        'best_metric': '?'  # Your answer
    },
]

# YOUR TASK: Fill in best metrics
# Options: Accuracy, Precision, Recall, F1, BLEU, ROUGE, Perplexity, Human Rating
```

### Answers
```python
answers = {
    'spam_detection': 'Precision + Recall (imbalanced classes)',
    'medical_diagnosis': 'Recall (minimize false negatives)',
    'chatbot': 'Human Rating + BLEU/ROUGE (quality + fluency)'
}
```

---

## 9. 🔒 Security Best Practices

**Linked Guide**: [Secure Mode](../agent_modes/Secure.md)  
**Project**: Secure RAG deployment  
**Time**: 3 hours

### What You'll Learn
- Input validation
- Output filtering
- API security
- Data privacy

### Practice Exercise: Secure This Code

```python
# ❌ INSECURE CODE - Find vulnerabilities!

@app.post("/query")
async def query(question: str):
    """Vulnerable endpoint"""
    
    # Bug: No input validation
    # Bug: No rate limiting
    # Bug: Logs sensitive data
    # Bug: Returns raw errors
    
    result = rag_system.query(question)
    log(f"User asked: {question}, got: {result}")  # Privacy issue!
    
    return {"answer": result}

# YOUR TASK: Identify and fix security issues!
```

### Secured Version
```python
from fastapi import HTTPException, RateLimiter
import re

@app.post("/query")
@RateLimiter(max_requests=10, period=60)  # 10 req/min
async def query(question: str):
    """Secure endpoint"""
    
    # Input validation
    if not question or len(question) > 1000:
        raise HTTPException(400, "Invalid question length")
    
    # Check for injection attempts
    if re.search(r'(DROP|DELETE|INSERT)', question, re.IGNORECASE):
        raise HTTPException(400, "Invalid input")
    
    try:
        result = rag_system.query(question)
        
        # Log without sensitive data
        log(f"Query processed successfully")
        
        # Filter output
        sanitized_result = filter_sensitive_info(result)
        
        return {"answer": sanitized_result}
        
    except Exception as e:
        # Log error details internally
        log_error(e)
        # Return generic error to user
        raise HTTPException(500, "Processing failed")
```

---

## 10. 🚀 Deployment Strategies

**Linked Guide**: [Infrastructure Layers](../guides/Infrastructure_Layers/)  
**Project**: Deploy RAG chatbot  
**Time**: 5 hours

### What You'll Learn
- Containerization (Docker)
- Cloud deployment
- Scaling strategies
- Monitoring

### Practice Exercise: Dockerize Your App

```dockerfile
# ❌ INEFFICIENT Dockerfile - Optimize it!

FROM python:3.9

# Bug: Installing everything in one layer
# Bug: No caching
# Bug: Including dev dependencies
# Bug: Running as root

COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "rag_chatbot.py"]

# YOUR TASK: Optimize this Dockerfile for:
# - Smaller image size
# - Faster builds
# - Better security
# - Production readiness
```

### Optimized Dockerfile
```dockerfile
# Multi-stage build for smaller image
FROM python:3.9-slim as builder

WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.9-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["python", "rag_chatbot.py"]

# Result: 5x smaller image, more secure, faster builds!
```

---

## 🎓 Skill Mastery Path

Complete these skills in order for maximum benefit:

```
Week 1: Debugging + Data Preprocessing
Week 2: Model Selection + Performance Optimization
Week 3: Version Control + Prompt Engineering
Week 4: Testing + Evaluation Metrics
Week 5: Security + Deployment
```

**Total Time**: ~35 hours (1 week per skill area)

---

## 🔗 Related Resources

- **[All Guides](../guides/)** - Deep theoretical knowledge
- **[Projects](../projects/)** - Apply skills practically
- **[Case Studies](../case_studies/)** - See skills in action
- **[Errors](../errors/)** - Practice debugging

---

<div align="center">

**Practice deliberately, learn systematically!** 🚀

[Start with Debugging](#1--debugging-ml-code) | [View All Skills](./README.md) | [Back to Main README](../README.md)

</div>
