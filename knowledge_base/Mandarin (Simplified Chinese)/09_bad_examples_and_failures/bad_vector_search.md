# Bad Vector Search

## Overview

Vector search enables semantic similarity search over high-dimensional embeddings. Bad vector search implementations suffer from poor index configuration, inappropriate distance metrics, scalability issues, or incorrect query handling, resulting in slow performance, inaccurate results, or system failures.

## When to Reference This Document

- Setting up vector databases
- Optimizing search performance
- Debugging retrieval quality issues
- Scaling vector search systems
- Choosing appropriate indexing strategies

## Common Vector Search Failures

### Wrong Distance Metric

**Bad Example**:
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

# Normalized embeddings should use cosine similarity
```

**Why It's Bad**:
- Euclidean distance biased by magnitude
- Cosine similarity better for text embeddings
- Incorrect ranking of results
- Poor retrieval quality

**Solution**: Match metric to embedding type
```python
# For normalized embeddings (most text models)
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct choice
    )
)

# For non-normalized embeddings
# Use DOT (dot product) or EUCLID appropriately
```

### Inappropriate Index Type

**Bad Example**:
```python
# Using exact search for million-scale database
client.create_collection(
    collection_name="large_corpus",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    hnsw_config=None  # Defaults to exact search
)

# Query latency: 5+ seconds for 1M vectors
```

**Why It's Bad**:
- O(n) complexity doesn't scale
- Unacceptable latency for production
- Wastes computational resources
- Poor user experience

**Solution**: Use approximate nearest neighbor (ANN) indexes
```python
client.create_collection(
    collection_name="large_corpus",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
    hnsw_config=models.HnswConfigDiff(
        m=16,           # Number of connections
        ef_construct=100,  # Build-time accuracy
        payload_m=16
    )
)

# Query with appropriate ef parameter
results = client.search(
    collection_name="large_corpus",
    query_vector=query,
    limit=10,
    params=models.SearchParams(hnsw_ef=50)  # Query-time accuracy
)
```

### Missing Payload Indexes

**Bad Example**:
```python
# Storing metadata but not indexing it
client.upsert(
    collection_name="docs",
    points=[
        {
            "id": 1,
            "vector": embedding,
            "payload": {
                "category": "tech",
                "date": "2024-01-15",
                "author": "john"
            }
        }
    ]
)

# Filtering by category requires full scan
results = client.search(
    collection_name="docs",
    query_vector=query,
    query_filter=models.Filter(
        must=[models.FieldCondition(key="category", match="tech")]
    )
)
# Slow because payload not indexed
```

**Why It's Bad**:
- Filters require linear scan
- Defeats purpose of ANN index
- Slow filtered searches
- Resource intensive

**Solution**: Create payload indexes
```python
client.create_payload_index(
    collection_name="docs",
    field_name="category",
    field_schema=models.KeywordIndex()
)

client.create_payload_index(
    collection_name="docs",
    field_name="date",
    field_schema=models.IntegerIndex()
)

# Now filtered searches are fast
```

### Improper Batch Sizes

**Bad Example**:
```python
# Inserting one vector at a time
for doc in documents:
    embedding = model.encode(doc.text)
    client.upsert(
        collection_name="docs",
        points=[{"id": doc.id, "vector": embedding, "payload": doc.metadata}]
    )
# 10,000 documents = 10,000 API calls = very slow
```

**Why It's Bad**:
- High network overhead
- Slow ingestion speed
- Increased latency
- Resource inefficient

**Solution**: Batch operations
```python
batch_size = 100
batches = [documents[i:i+batch_size] for i in range(0, len(documents), batch_size)]

for batch in batches:
    points = [
        {
            "id": doc.id,
            "vector": model.encode(doc.text),
            "payload": doc.metadata
        }
        for doc in batch
    ]
    client.upsert(collection_name="docs", points=points)

# 10,000 documents = 100 API calls = 100x faster
```

### No Quantization

**Bad Example**:
```python
# Storing full precision floats for billion-scale database
client.create_collection(
    collection_name="massive_corpus",
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE)
    # Uses 6KB per vector (1536 * 4 bytes)
    # 1B vectors = 6TB storage
)
```

**Why It's Bad**:
- Excessive storage requirements
- Higher memory usage
- Slower search due to cache misses
- Increased costs

**Solution**: Enable quantization
```python
client.create_collection(
    collection_name="massive_corpus",
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            quantile=0.99,
            always_ram=True
        )
    )
)

# Reduces storage by 4x (1.5KB per vector)
# 1B vectors = 1.5TB storage
```

## Real-World Scenarios

### Scenario 1: Recommendation System
Wrong distance metric causes dissimilar items to rank highly, degrading recommendation quality and user engagement.

### Scenario 2: Semantic Search Engine
Missing payload indexes make filtered searches (by date, category) unbearably slow, frustrating users.

### Scenario 3: Large-Scale RAG
No quantization leads to excessive memory usage, causing OOM errors and system crashes during peak load.

## Detection Patterns

Watch for these warning signs:
- Search latency > 100ms for small collections
- Irrelevant results ranking highly
- Memory usage growing linearly with data
- Filtered searches as slow as unfiltered
- Ingestion taking hours instead of minutes
- Frequent out-of-memory errors

## Prevention Strategies

1. **Choose Right Distance Metric**: COSINE for normalized, DOT for raw
2. **Configure ANN Indexes**: HNSW for most use cases
3. **Index Payloads**: Create indexes for frequently filtered fields
4. **Batch Operations**: Group inserts and updates
5. **Enable Quantization**: Reduce storage for large datasets
6. **Monitor Performance**: Track latency, recall, resource usage
7. **Tune Parameters**: Adjust ef_construct, m based on benchmarks

## Testing Checklist

- [ ] Is distance metric appropriate for embeddings?
- [ ] Are ANN indexes configured for scale?
- [ ] Are payload fields indexed for filtering?
- [ ] Are operations batched appropriately?
- [ ] Is quantization enabled for large datasets?
- [ ] Is search latency under 100ms (P95)?
- [ ] Is recall@k above 90% compared to exact search?

## Related Documents

- [[bad_embeddings]] - Embedding quality affects search results
- [[bad_rag]] - RAG depends on effective vector search
- [[benchmark_misuse]] - Properly evaluating search performance
- [[memory_leaks]] - Memory issues in vector databases
