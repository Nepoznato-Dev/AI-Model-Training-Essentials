# Bad RAG (Retrieval-Augmented Generation)

## Overview

Retrieval-Augmented Generation (RAG) combines retrieval systems with generative AI to produce more accurate and contextually relevant responses. Bad RAG implementations suffer from poor retrieval quality, inadequate context handling, or generation issues that lead to inaccurate, irrelevant, or hallucinated outputs.

## When to Reference This Document

- Designing RAG-based systems
- Debugging poor RAG performance
- Evaluating retrieval quality
- Optimizing context window usage
- Training teams on RAG best practices

## Common RAG Failures

### Poor Chunking Strategy

**Bad Example**:
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

**Why It's Bad**:
- Breaks semantic meaning
- Loses context across boundaries
- Reduces retrieval accuracy
- Creates fragmented understanding

**Solution**: Semantic chunking
```python
def semantic_chunk(document):
    # Split by paragraphs first
    paragraphs = document.split('\n\n')
    
    # Keep related paragraphs together
    chunks = []
    current_chunk = []
    current_length = 0
    
    for para in paragraphs:
        if current_length + len(para) > MAX_CHUNK_SIZE:
            chunks.append(' '.join(current_chunk))
            current_chunk = [para]
            current_length = len(para)
        else:
            current_chunk.append(para)
            current_length += len(para)
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks
```

### Inadequate Embedding Model

**Bad Example**:
```python
# Using generic embeddings for domain-specific content
from sentence_transformers import SentenceTransformer

# Generic model for medical documents
model = SentenceTransformer('all-MiniLM-L6-v2')
medical_embeddings = model.encode(medical_texts)

# Results in poor semantic matching for specialized terminology
```

**Why It's Bad**:
- Misses domain-specific semantics
- Poor similarity scores for technical terms
- Reduced retrieval precision
- Context mismatch

**Solution**: Domain-adapted embeddings
```python
# Fine-tune on domain data or use specialized model
model = SentenceTransformer('emilyalsentzer/Bio_ClinicalBERT')
# Or fine-tune existing model
model.fine_tune(domain_specific_pairs)

medical_embeddings = model.encode(medical_texts)
```

### Naive Retrieval Strategy

**Bad Example**:
```python
# Only using top-k similar chunks without re-ranking
def retrieve(query, embeddings, k=5):
    query_embedding = embed(query)
    similarities = cosine_similarity(query_embedding, embeddings)
    top_k_indices = np.argsort(similarities)[-k:]
    return [chunks[i] for i in top_k_indices]

# No consideration for diversity, recency, or relevance
```

**Why It's Bad**:
- Returns redundant information
- Misses complementary context
- No quality filtering
- Vulnerable to embedding noise

**Solution**: Hybrid retrieval with re-ranking
```python
def hybrid_retrieve(query, chunks, k=10):
    # Dense retrieval
    dense_results = dense_search(query, chunks, k=k*2)
    
    # Sparse retrieval (BM25)
    sparse_results = bm25_search(query, chunks, k=k*2)
    
    # Combine results
    combined = reciprocal_rank_fusion(dense_results, sparse_results)
    
    # Re-rank with cross-encoder
    reranked = cross_encoder_rerank(query, combined, top_k=k)
    
    return reranked
```

### Context Window Overflow

**Bad Example**:
```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    context = ""
    for chunk in retrieved_chunks:
        context += chunk + "\n"
    # Sends 50k tokens to model with 8k limit
    return generate_response(query, context)
```

**Why It's Bad**:
- Truncates important information
- Wastes token budget
- Increases latency and cost
- May exceed model limits

**Solution**: Smart context selection
```python
def build_optimal_context(query, chunks, max_tokens=4000):
    # Score chunks by relevance
    scored = [(chunk, relevance_score(query, chunk)) for chunk in chunks]
    scored.sort(key=lambda x: x[1], reverse=True)
    
    # Add chunks until token limit
    context_chunks = []
    total_tokens = 0
    
    for chunk, score in scored:
        chunk_tokens = count_tokens(chunk)
        if total_tokens + chunk_tokens <= max_tokens:
            context_chunks.append(chunk)
            total_tokens += chunk_tokens
        else:
            break
    
    return "\n\n".join(context_chunks)
```

### Missing Metadata Filtering

**Bad Example**:
```python
# Retrieving from entire corpus without filters
results = vector_store.similarity_search(query, k=10)

# Returns outdated, irrelevant, or unauthorized content
```

**Why It's Bad**:
- Includes obsolete information
- Violates access controls
- Reduces precision
- Wastes retrieval budget

**Solution**: Metadata-aware retrieval
```python
results = vector_store.similarity_search(
    query,
    k=10,
    filter={
        "date": {"$gte": "2024-01-01"},
        "department": {"$in": ["engineering", "product"]},
        "access_level": {"$lte": user.clearance}
    }
)
```

## Real-World Scenarios

### Scenario 1: Customer Support Bot
RAG system retrieves outdated product documentation, giving customers incorrect information about discontinued features.

### Scenario 2: Legal Research Assistant
Poor chunking splits legal clauses mid-sentence, causing the model to misinterpret contract terms.

### Scenario 3: Medical Diagnosis Aid
Generic embeddings fail to distinguish between similar medical conditions, leading to irrelevant research paper retrieval.

## Detection Patterns

Watch for these warning signs:
- Irrelevant chunks in context
- Hallucinated facts despite source material
- Inconsistent answers to similar queries
- High token usage with low quality
- Duplicate information in responses
- Missing critical context

## Prevention Strategies

1. **Implement Quality Metrics**: Track retrieval precision, answer relevance
2. **Use Appropriate Chunking**: Semantic boundaries over fixed sizes
3. **Domain-Specific Embeddings**: Fine-tune for your use case
4. **Hybrid Retrieval**: Combine dense and sparse methods
5. **Re-ranking**: Use cross-encoders for final selection
6. **Metadata Filtering**: Leverage structured data
7. **Evaluation Pipeline**: Regular testing with ground truth

## Testing Checklist

- [ ] Are chunks semantically coherent?
- [ ] Do embeddings capture domain semantics?
- [ ] Is retrieval precision above 80%?
- [ ] Does context fit within token limits?
- [ ] Are metadata filters applied correctly?
- [ ] Is there diversity in retrieved results?
- [ ] Are responses grounded in retrieved context?

## Related Documents

- [[hallucination_examples]] - When RAG fails to ground responses
- [[bad_embeddings]] - Embedding-specific issues
- [[bad_vector_search]] - Vector database problems
- [[misinformation_examples]] - Handling incorrect retrieved information
