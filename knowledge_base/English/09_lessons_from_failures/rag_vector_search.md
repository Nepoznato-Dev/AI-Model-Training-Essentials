---
# Metadata
title: "RAG and Vector Search Failures"
description: "RAG and vector search pitfalls"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [rag, vector, search, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "31 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

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

- **AI/LLM Failures**: See `ai_llm_failures.md` for hallucinations and reasoning issues
- **Agent Design**: See `../05_agents/agent_system_design.md` for building agents with RAG
- **Dataset Quality**: See `../08_machine_learning/ml_data_issues.md` for training data considerations
- **Prompt Engineering**: See `../02_artificial_intelligence/prompt_engineering.md` for context handling techniques

---

## Advanced RAG Failure Patterns

### Lost in the Middle Phenomenon

**What It Is:** LLMs tend to focus on information at the beginning and end of context, 
ignoring middle content.

**Bad Example:**
```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Why It's Bad:**
- Critical information in middle chunks may be overlooked
- Model attention diminishes for middle content
- Wastes tokens on irrelevant retrieved content

**Mitigation:**
```python
# Re-rank retrieved results by relevance
reranked_chunks = rerank(query, retrieved_chunks, top_k=5)

# Put most relevant chunks at beginning and end
context = organize_for_attention(reranked_chunks)

# Or use iterative retrieval
for iteration in range(3):
    response = llm.generate(query, current_context)
    if response_needs_more_info(response):
        more_chunks = retrieve_remaining_info()
        current_context = combine(current_context, more_chunks)
```

### Multi-Hop Retrieval Failures

**What It Is:** Failing to retrieve information that requires multiple connected pieces.

**Bad Example:**
```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Mitigation:**
```python
def multi_hop_retrieval(query):
    # First hop: initial retrieval
    chunks_1 = retrieve(query, top_k=5)
    
    # Extract entities from first results
    entities = extract_entities(chunks_1)
    
    # Second hop: retrieve about those entities
    chunks_2 = []
    for entity in entities:
        chunks_2.extend(retrieve(f"{entity} background", top_k=3))
    
    # Combine and deduplicate
    all_chunks = deduplicate(chunks_1 + chunks_2)
    return rerank(query, all_chunks)
```

### Temporal Reasoning Failures

**What It Is:** RAG systems struggle with time-sensitive queries and outdated information.

**Bad Example:**
```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Mitigation:**
```python
def temporal_aware_retrieval(query, documents):
    # Detect if query is time-sensitive
    if is_time_sensitive(query):
        # Filter for recent documents
        recent_docs = filter_by_date(documents, last_n_months=6)
        
        # Boost recent content in ranking
        results = retrieve(query, recent_docs, recency_boost=0.3)
        
        # Add temporal context to prompt
        context = format_with_dates(results)
        context += f"\n\nNote: Current date is {get_current_date()}"
        
        return context
    else:
        return retrieve(query, documents)
```

### Negation Handling Failures

**What It Is:** Semantic search often misses negations in queries.

**Bad Example:**
```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Mitigation:**
```python
def handle_negation_query(query, documents):
    # Detect negation patterns
    negation_terms = extract_negations(query)
    
    if negation_terms:
        # Remove negation for semantic search
        positive_query = remove_negation(query)
        candidates = retrieve(positive_query, documents, top_k=20)
        
        # Filter out results containing negated terms
        filtered = []
        for chunk in candidates:
            if not contains_any(chunk, negation_terms):
                filtered.append(chunk)
        
        return filtered[:5]
    else:
        return retrieve(query, documents)
```

---

## Embedding Anti-Patterns

### Mixing Embedding Models

**What It Is:** Using different models for indexing vs. querying breaks similarity.

**Bad Example:**
```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Why It's Bad:**
- Different models produce embeddings in incompatible vector spaces
- Cosine similarity between different model embeddings is random noise
- System appears to work but returns garbage

**Detection:**
```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Ignoring Embedding Dimensions

**What It Is:** Not considering the impact of embedding dimension on performance.

**Trade-offs:**
| Dimensions | Pros | Cons | Use Case |
|------------|------|------|----------|
| Low (128-256) | Fast search, less memory | Less nuanced representations | Simple tasks, large scale |
| Medium (384-768) | Good balance | Moderate resources | General purpose |
| High (1024+) | Rich representations | Slow, memory-intensive | Complex semantic tasks |

**Bad Example:**
```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Not Handling Special Tokens

**What It Is:** Failing to properly handle URLs, code, numbers, and special characters.

**Bad Example:**
```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Mitigation:**
```python
def preprocess_for_embedding(text):
    # Handle URLs
    urls = extract_urls(text)
    text = replace_urls_with_descriptions(text)
    
    # Handle code
    code_blocks = extract_code(text)
    text = replace_code_with_summaries(text)
    
    # Handle numbers (normalize)
    text = normalize_numbers(text)
    
    # Now embed
    embedding = model.encode(text)
    
    # Store metadata for later
    return embedding, {'urls': urls, 'code': code_blocks}
```

---

## Vector Search Performance Issues

### Scaling Problems

**What It Is:** Search quality or latency degrades as dataset grows.

**Symptoms:**
- Latency increases linearly with dataset size
- Recall drops as more vectors are added
- Memory usage explodes

**Bad Architecture:**
```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Scalable Solution:**
```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Cold Start Problem

**What It Is:** New documents aren't retrievable until index is rebuilt.

**Bad Example:**
```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Solution: Incremental Indexing**
```python
# Add documents as they arrive
def add_document(doc):
    embedding = model.encode(doc.content)
    vector_db.insert(id=doc.id, vector=embedding, metadata=doc.metadata)
    # Immediately searchable
    
# Periodically optimize index
def optimize_index():
    vector_db.optimize()  # Merge segments, improve performance
```

---

## Evaluation Metrics for RAG

### Context Precision

Measures how many retrieved chunks are actually relevant.

```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Answer Relevance

Measures if generated answer actually addresses the query.

```python
def answer_relevance_score(query, answer, retrieved_chunks):
    """
    Use LLM to judge if answer is relevant to query given the context
    """
    prompt = f"""
    Query: {query}
    Answer: {answer}
    
    Does this answer address the query? Rate 1-5.
    """
    rating = llm.generate(prompt)
    return parse_rating(rating)
```

### Faithfulness

Measures if answer is grounded in retrieved context (not hallucinated).

```python
def faithfulness_score(answer, retrieved_chunks):
    """
    Check if claims in answer can be traced back to context
    """
    claims = extract_claims(answer)
    supported_claims = 0
    
    for claim in claims:
        if any(claim_in_context(claim, chunk) for chunk in retrieved_chunks):
            supported_claims += 1
    
    return supported_claims / len(claims) if claims else 0
```

---

## Real-World Case Studies

### Case Study 1: Customer Support Chatbot

**Problem:** Chatbot gave incorrect answers about product features.

**Root Cause Analysis:**
- Chunking split feature descriptions across boundaries
- Retrieval found partial information
- LLM hallucinated missing details

**Solution:**
- Implemented semantic chunking by feature sections
- Added 150-token overlap between chunks
- Increased top_k from 3 to 5
- Added re-ranking step

**Results:**
- Accuracy improved from 62% to 89%
- Hallucination rate dropped from 23% to 4%
- Customer satisfaction increased 35%

### Case Study 2: Legal Document Search

**Problem:** Lawyers couldn't find relevant precedents.

**Root Cause:**
- Generic embeddings didn't capture legal semantics
- Negation queries failed ("cases where liability was NOT established")
- No temporal filtering for overturned cases

**Solution:**
- Fine-tuned embeddings on legal corpus
- Implemented negation handling
- Added case status metadata and filtering
- Built multi-hop retrieval for citation chains

**Results:**
- Recall@10 improved from 45% to 78%
- Search time reduced from 8s to 1.2s
- Adoption by legal team increased 3x

### Case Study 3: Technical Documentation

**Problem:** Developers couldn't find code examples.

**Root Cause:**
- Code blocks embedded poorly with text-only models
- Queries like "how to authenticate" matched theory, not examples
- No distinction between API versions

**Solution:**
- Used code-aware embedding model
- Tagged chunks by content type (concept, tutorial, API reference, example)
- Added version metadata
- Implemented intent classification for query routing

**Results:**
- Code example retrieval accuracy: 34% → 82%
- Time-to-first-successful-query reduced 60%
- Documentation traffic increased 45%
