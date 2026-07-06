# Bad Embeddings

## Overview

Embeddings are vector representations of data (text, images, etc.) that capture semantic meaning. Bad embeddings result from poor model selection, inadequate training, improper preprocessing, or misuse of embedding spaces, leading to ineffective similarity search, clustering, and downstream task performance.

## When to Reference This Document

- Selecting embedding models for projects
- Debugging poor similarity search results
- Evaluating embedding quality
- Training custom embedding models
- Optimizing vector search performance

## Common Embedding Failures

### Wrong Model for Domain

**Bad Example**:
```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Why It's Bad**:
- Misses domain-specific semantics
- Poor clustering of related concepts
- Inaccurate similarity scores
- Reduced retrieval quality

**Solution**: Use domain-specific models
```python
# Legal domain
model = SentenceTransformer('nlp-studio/law-embeddings')

# Biomedical domain
model = SentenceTransformer('emilyalsentzer/Bio_ClinicalBERT')

# Code embeddings
model = SentenceTransformer('microsoft/codebert-base')
```

### Ignoring Normalization

**Bad Example**:
```python
# Not normalizing embedding vectors
embeddings = model.encode(texts, normalize=False)

# Using Euclidean distance instead of cosine similarity
distances = euclidean_distance(query_emb, embeddings)

# Results biased by vector magnitude rather than direction
```

**Why It's Bad**:
- Magnitude affects similarity unfairly
- Inconsistent with most use cases
- Poor performance in high dimensions
- Misleading similarity scores

**Solution**: Normalize and use cosine similarity
```python
embeddings = model.encode(texts, normalize_embeddings=True)

# Or manually normalize
from sklearn.preprocessing import normalize
embeddings = normalize(embeddings)

# Use cosine similarity
similarities = cosine_similarity(query_emb, embeddings)
```

### Dimensionality Mismatch

**Bad Example**:
```python
# Mixing embeddings from different models
model1 = SentenceTransformer('all-MiniLM-L6-v2')  # 384 dims
model2 = SentenceTransformer('all-mpnet-base-v2')  # 768 dims

# Storing both in same vector database
vector_store.add(model1.encode(texts_a))
vector_store.add(model2.encode(texts_b))

# Queries return meaningless results
```

**Why It's Bad**:
- Incomparable vector spaces
- Garbage similarity scores
- Wasted storage
- Broken retrieval

**Solution**: Consistent embedding dimensions
```python
# Choose one model for entire corpus
model = SentenceTransformer('all-mpnet-base-v2')

# Re-encode existing data if changing models
all_embeddings = model.encode(all_texts)
vector_store.clear()
vector_store.add(all_embeddings)
```

### Poor Preprocessing

**Bad Example**:
```python
# No text normalization before embedding
texts = [
    "  HELLO WORLD  ",
    "hello world!",
    "Hello\nWorld",
    "hello   world"
]

embeddings = model.encode(texts)

# Same content produces different embeddings
```

**Why It's Bad**:
- Inconsistent representations
- Reduced similarity accuracy
- Wasted embedding capacity on noise
- Poor clustering results

**Solution**: Standardize preprocessing
```python
import re

def preprocess(text):
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

cleaned_texts = [preprocess(t) for t in texts]
embeddings = model.encode(cleaned_texts)
```

### Outdated Embeddings

**Bad Example**:
```python
# Encode once, never update
product_embeddings = model.encode(product_descriptions)
vector_store.add(product_embeddings)

# Six months later with new products and updated model
new_product = "AI-powered smart watch"
new_embedding = new_model.encode([new_product])

# Old and new embeddings incomparable
```

**Why It's Bad**:
- Model drift over time
- Inconsistent similarity across batches
- Degraded search quality
- Cannot compare old vs new content

**Solution**: Version and re-embed periodically
```python
class EmbeddingManager:
    def __init__(self, model_version):
        self.model_version = model_version
        self.model = load_model(model_version)
    
    def embed(self, texts):
        embeddings = self.model.encode(texts)
        return {
            'vectors': embeddings,
            'model_version': self.model_version,
            'timestamp': datetime.now()
        }
    
    def should_reembed(self, stored_version):
        return stored_version != self.model_version
```

### Insufficient Training Data (Custom Models)

**Bad Example**:
```python
# Fine-tuning with only 50 example pairs
training_pairs = [
    ("query1", "relevant_doc1"),
    # ... 49 more pairs
]

model.fit(training_pairs, epochs=100)

# Severe overfitting, poor generalization
```

**Why It's Bad**:
- Overfits to training examples
- Poor performance on unseen data
- Unreliable similarity scores
- Wasted compute resources

**Solution**: Adequate training data
```python
# Minimum 1000+ diverse pairs for fine-tuning
training_pairs = generate_training_data(
    domain_corpus,
    min_pairs=5000,
    include_hard_negatives=True
)

model.fit(
    training_pairs,
    epochs=3,
    batch_size=32,
    validation_split=0.2,
    early_stopping=True
)
```

## Real-World Scenarios

### Scenario 1: E-commerce Search
Generic embeddings fail to distinguish product variants, showing winter coats when user searches for "light jacket."

### Scenario 2: Document Deduplication
Unnormalized embeddings cause near-duplicates to have low similarity, failing to identify redundant documents.

### Scenario 3: Semantic Cache
Mixed embedding versions cause cache misses for semantically identical queries, reducing cache effectiveness.

## Detection Patterns

Watch for these warning signs:
- Similar texts have low similarity scores
- Dissimilar texts rank highly
- Clustering produces meaningless groups
- Search results don't match query intent
- Performance degrades over time
- Different models produce incompatible results

## Prevention Strategies

1. **Choose Domain-Appropriate Models**: Match model to use case
2. **Normalize Vectors**: Always normalize for cosine similarity
3. **Consistent Preprocessing**: Standardize text cleaning
4. **Version Management**: Track model versions with embeddings
5. **Regular Evaluation**: Test embedding quality periodically
6. **Adequate Training Data**: Use sufficient examples for fine-tuning
7. **Monitor Drift**: Track embedding distribution changes

## Testing Checklist

- [ ] Is the model appropriate for the domain?
- [ ] Are embeddings normalized?
- [ ] Is preprocessing consistent?
- [ ] Are all embeddings from same model version?
- [ ] Do similar texts have high similarity (>0.7)?
- [ ] Do dissimilar texts have low similarity (<0.3)?
- [ ] Is there a plan for periodic re-embedding?

## Related Documents

- [[bad_vector_search]] - Vector database and search issues
- [[bad_rag]] - RAG systems depend on quality embeddings
- [[overfitting_examples]] - Overfitting in custom embedding models
- [[benchmark_misuse]] - Properly evaluating embedding quality
