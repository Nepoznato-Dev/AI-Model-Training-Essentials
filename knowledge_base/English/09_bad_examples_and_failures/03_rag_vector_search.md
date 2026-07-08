# RAG and Vector Search Failures

This document consolidates common failures in Retrieval-Augmented Generation (RAG) systems, embedding usage, and vector search implementations.

---

## Bad RAG (Retrieval-Augmented Generation)

Retrieval-Augmented Generation (RAG) combines retrieval systems with generative AI to produce more accurate and contextually relevant responses. Bad RAG implementations suffer from poor retrieval quality, inadequate context handling, or generation issues.

### Poor Chunking Strategy

**Bad Example:**
```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Problems:**
- Sentences and paragraphs are split arbitrarily
- Context is lost at chunk boundaries
- Semantic meaning is fragmented
- Retrieval returns incomplete information

**Better Approach:**
```python
# Chunk by semantic boundaries (paragraphs, sections)
def chunk_by_paragraphs(text, max_chunk_size=500):
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        para_size = len(para)
        if current_size + para_size > max_chunk_size and current_chunk:
            chunks.append('\n\n'.join(current_chunk))
            current_chunk = [para]
            current_size = para_size
        else:
            current_chunk.append(para)
            current_size += para_size
    
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks
```

### Missing Context Overlap

**Bad Example:**
```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Better Approach:**
```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Ignoring Query Intent

**Bad Example:**
```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Better Approach:**
```python
def retrieve_with_intent(query, documents):
    # Classify query intent first
    intent = classify_intent(query)  # definition, how-to, comparison, etc.
    
    if intent == 'definition':
        # Boost chunks containing definitional patterns
        return boosted_search(query, documents, pattern='is defined as')
    elif intent == 'how-to':
        # Boost procedural content
        return boosted_search(query, documents, pattern='steps|procedure')
    else:
        return semantic_search(query, documents, top_k=5)
```

### Context Window Overflow

**Bad Example:**
```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Better Approach:**
```python
def build_context_within_limit(retrieved_chunks, max_tokens=4000):
    context_parts = []
    total_tokens = 0
    
    for chunk in retrieved_chunks:
        chunk_tokens = estimate_tokens(chunk.text)
        if total_tokens + chunk_tokens <= max_tokens:
            context_parts.append(chunk.text)
            total_tokens += chunk_tokens
        else:
            break
    
    return '\n\n'.join(context_parts)
```

---

## Bad Embeddings

Embeddings are vector representations of data that capture semantic meaning. Bad embeddings result from poor model selection, inadequate training, or improper usage.

### Wrong Model for Domain

**Bad Example:**
```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Better Approach:**
```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Not Normalizing Vectors

**Bad Example:**
```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Better Approach:**
```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Ignoring Embedding Dimensions

**Bad Example:**
```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Better Approach:**
```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Bad Vector Search

Vector search enables semantic similarity search over high-dimensional embeddings. Bad implementations suffer from poor index configuration, inappropriate distance metrics, or scalability issues.

### Wrong Distance Metric

**Bad Example:**
```python
# Using Euclidean distance for normalized embeddings
from qdrant_client import QdrantClient

client = QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.EUCLID  # Wrong for normalized vectors
    )
)
```

**Why It's Bad:**
- Euclidean distance is affected by vector magnitude
- For normalized vectors, cosine similarity (dot product) is appropriate
- Results will be less accurate for semantic search

**Better Approach:**
```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Missing Index Optimization

**Bad Example:**
```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Better Approach:**
```python
# Configure HNSW index for fast approximate nearest neighbor search
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    hnsw_config=models.HnswConfigDiff(
        m=16,           # Number of connections
        ef_construct=100,  # Size of dynamic candidate list
        payload_m=16
    )
)
# O(log n) search complexity
```

### Not Handling High-Dimensional Data

**Bad Example:**
```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Better Approach:**
```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Ignoring Recall vs Latency Tradeoff

**Bad Example:**
```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Better Approach:**
```python
# Tune search parameters based on requirements
# For high recall (accuracy-critical):
results = client.search(
    collection_name="docs",
    query_vector=query,
    limit=10,
    params=models.SearchParams(hnsw_ef=200)  # Higher = more accurate, slower
)

# For low latency (real-time applications):
results = client.search(
    collection_name="docs",
    query_vector=query,
    limit=10,
    params=models.SearchParams(hnsw_ef=32)  # Lower = faster, less accurate
)
```

---

## Best Practices Summary

### RAG Systems
1. **Chunk Strategically**: Respect semantic boundaries, add overlap
2. **Consider Query Intent**: Adapt retrieval based on what user wants
3. **Manage Context**: Stay within LLM token limits
4. **Evaluate End-to-End**: Test full RAG pipeline, not just retrieval

### Embeddings
1. **Choose Domain-Appropriate Models**: Match model to your content type
2. **Normalize Vectors**: Essential for cosine similarity
3. **Consistency**: Use same model throughout your system
4. **Monitor Drift**: Retrain or update embeddings as data evolves

### Vector Search
1. **Select Right Distance Metric**: COSINE for semantic, EUCLID for spatial
2. **Configure Indexes**: Use HNSW for large datasets
3. **Tune Parameters**: Balance recall vs latency for your use case
4. **Monitor Performance**: Track search quality and latency over time

---

## Related Topics

- **AI/LLM Failures**: See `01_ai_llm_failures.md` for hallucinations and reasoning issues
- **Agent Design**: See `05_agent_system_design.md` for building agents with RAG
- **Dataset Quality**: See `06_ml_data_issues.md` for training data considerations
