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

# RAG at Vector Search Failures
Pinagsasama-sama ng dokumentong ito ang mga karaniwang pagkabigo sa mga system ng Retrieval-Augmented Generation (RAG), paggamit ng pag-embed, at mga pagpapatupad ng vector search.
---

## Masamang RAG (Retrieval-Augmented Generation)
Pinagsasama-sama ng Retrieval-Augmented Generation (RAG) ang mga retrieval system na may generative AI para makabuo ng mas tumpak at nauugnay na mga tugon sa konteksto. Ang mga masamang pagpapatupad ng RAG ay dumaranas ng hindi magandang kalidad ng pagkuha, hindi sapat na paghawak sa konteksto, o mga isyu sa henerasyon.
### Hindi magandang Chunking Strategy
**Masama Halimbawa:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Mga Problema:**
- Ang mga pangungusap at talata ay hinahati nang arbitraryo
- Nawala ang konteksto sa mga hangganan ng tipak
- Ang kahulugan ng semantiko ay pira-piraso
- Ang retrieval ay nagbabalik ng hindi kumpletong impormasyon
**Mas mahusay na Diskarte:**```python
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

### Nawawalang Context Overlap
**Masama Halimbawa:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Mas mahusay na Diskarte:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Hindi pinapansin ang Layunin ng Query
**Masama Halimbawa:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Mas mahusay na Diskarte:**```python
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
**Masama Halimbawa:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Mas mahusay na Diskarte:**```python
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

## Masamang Pag-embed
Ang mga pag-embed ay mga representasyon ng vector ng data na kumukuha ng semantikong kahulugan. Ang hindi magandang pag-embed ay nagreresulta mula sa hindi magandang pagpili ng modelo, hindi sapat na pagsasanay, o hindi wastong paggamit.
### Maling Modelo para sa Domain
**Masama Halimbawa:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Mas mahusay na Diskarte:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Hindi Normalizing Vectors
**Masama Halimbawa:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Mas mahusay na Diskarte:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Hindi pinapansin ang Mga Dimensyon ng Pag-embed
**Masama Halimbawa:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Mas mahusay na Diskarte:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Masamang Paghahanap ng Vector
Ang paghahanap ng vector ay nagbibigay-daan sa paghahanap ng pagkakapareho ng semantiko sa mga high-dimensional na pag-embed. Ang mga hindi magandang pagpapatupad ay dumaranas ng hindi magandang configuration ng index, hindi naaangkop na sukatan ng distansya, o mga isyu sa scalability.
### Maling Sukatan ng Distansya
**Masama Halimbawa:**```python
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

**Bakit Masama:**
- Ang distansya ng Euclidean ay apektado ng vector magnitude
- Para sa mga na-normalize na vector, angkop ang cosine similarity (dot product).
- Ang mga resulta ay magiging mas tumpak para sa semantic na paghahanap
**Mas mahusay na Diskarte:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Nawawalang Index Optimization
**Masama Halimbawa:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Mas mahusay na Diskarte:**```python
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

### Hindi Pangasiwaan ang High-Dimensional na Data
**Masama Halimbawa:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Mas mahusay na Diskarte:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Hindi pinapansin ang Recall vs Latency Tradeoff
**Masama Halimbawa:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Mas mahusay na Diskarte:**```python
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

## Buod ng Pinakamahuhusay na Kasanayan
### RAG System
1. **Chunk Strategically**: Igalang ang semantic boundaries, magdagdag ng overlap
2. **Isaalang-alang ang Layunin ng Query**: Iangkop ang pagkuha batay sa gusto ng user
3. **Pamahalaan ang Konteksto**: Manatili sa loob ng mga limitasyon ng token ng LLM
4. **Suriin ang End-to-End**: Subukan ang buong RAG pipeline, hindi lamang ang pagkuha
### Mga pag-embed
1. **Pumili ng Mga Modelong Naaangkop sa Domain**: Itugma ang modelo sa iyong uri ng nilalaman
2. **I-normalize ang mga Vector**: Mahalaga para sa pagkakatulad ng cosine
3. **Consistency**: Gumamit ng parehong modelo sa iyong system
4. **Subaybayan ang Drift**: Sanayin muli o i-update ang mga pag-embed habang nagbabago ang data
### Paghahanap ng Vector
1. **Pumili ng Tamang Sukat ng Distansya**: COSINE para sa semantic, EUCLID para sa spatial
2. **I-configure ang Mga Index**: Gamitin ang HNSW para sa malalaking dataset
3. **Mga Parameter ng Tune**: Pag-recall ng balanse kumpara sa latency para sa iyong use case
4. **Subaybayan ang Pagganap**: Subaybayan ang kalidad ng paghahanap at latency sa paglipas ng panahon
---

## Mga Kaugnay na Paksa
- **AI/LLM Failures**: Tingnan ang`ai_llm_failures.md`para sa mga guni-guni at mga isyu sa pangangatwiran
- **Disenyo ng Ahente**: Tingnan ang`../05_agents/agent_system_design.md`para sa mga ahente ng gusali na may RAG
- **Dataset Quality**: Tingnan ang`../08_machine_learning/ml_data_issues.md`para sa mga pagsasaalang-alang sa data ng pagsasanay
- **Prompt Engineering**: Tingnan ang`../02_artificial_intelligence/prompt_engineering.md`para sa mga diskarte sa paghawak ng konteksto
---

## Mga Advanced na Pattern ng Pagkabigo ng RAG
### Nawala sa Gitnang Phenomenon
**Ano Ito:** Ang mga LLM ay may posibilidad na tumuon sa impormasyon sa simula at dulo ng konteksto, 
hindi pinapansin ang gitnang nilalaman.
**Masama Halimbawa:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Bakit Masama:**
- Maaaring hindi mapansin ang kritikal na impormasyon sa gitnang mga tipak
- Nababawasan ang atensyon ng modelo para sa gitnang nilalaman
- Nag-aaksaya ng mga token sa hindi nauugnay na nakuhang nilalaman
**Pagbabawas:**```python
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
**Ano Ito:** Nabigong makuha ang impormasyong nangangailangan ng maraming konektadong piraso.
**Masama Halimbawa:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Pagbabawas:**```python
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

### Mga Pagkabigo sa Temporal na Pangangatwiran
**Ano Ito:** Ang mga sistema ng RAG ay nakikipagpunyagi sa mga query na sensitibo sa oras at hindi napapanahong impormasyon.
**Masama Halimbawa:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Pagbabawas:**```python
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

### Mga Pagkabigo sa Paghawak ng Negasyon
**Ano Ito:** Ang semantic na paghahanap ay madalas na nakakaligtaan ng mga negasyon sa mga query.
**Masama Halimbawa:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Pagbabawas:**```python
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

## Pag-embed ng mga Anti-Pattern
### Paghahalo ng Mga Modelo sa Pag-embed
**Ano Ito:** Ang paggamit ng iba't ibang modelo para sa pag-index kumpara sa pag-query ay nakakasira ng pagkakatulad.
**Masama Halimbawa:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Bakit Masama:**
- Ang iba't ibang mga modelo ay gumagawa ng mga pag-embed sa hindi tugmang mga puwang ng vector
- Ang pagkakatulad ng cosine sa pagitan ng iba't ibang mga pag-embed ng modelo ay random na ingay
- Lumilitaw na gumagana ang system ngunit nagbabalik ng basura
**Detection:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Hindi pinapansin ang Mga Dimensyon ng Pag-embed
**Ano Ito:** Hindi isinasaalang-alang ang epekto ng dimensyon ng pag-embed sa pagganap.
**Trade-off:**
| Mga sukat | Mga Pros | Cons | Use Case |
|------------|------|------|----------|
| Mababa (128-256) | Mabilis na paghahanap, mas kaunting memorya | Mga hindi gaanong nuanced na representasyon | Mga simpleng gawain, malakihan |
| Katamtaman (384-768) | Magandang balanse | Katamtamang mapagkukunan | Pangkalahatang layunin |
| Mataas (1024+) | Mga mayamang representasyon | Mabagal, memory-intensive | Mga kumplikadong semantikong gawain |
**Masama Halimbawa:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Hindi Paghawak ng Mga Espesyal na Token
**Ano Ito:** Nabigong pangasiwaan nang maayos ang mga URL, code, numero, at espesyal na character.
**Masama Halimbawa:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Pagbabawas:**```python
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

## Mga Isyu sa Pagganap ng Vector Search
### Mga Problema sa Pagsusukat
**Ano Ito:** Ang kalidad ng paghahanap o latency ay bumababa habang lumalaki ang dataset.
**Mga Sintomas:**
- Ang latency ay tumataas nang linear sa laki ng dataset
- Bumaba ang recall habang nagdaragdag ng mga vector
- Ang paggamit ng memory ay sumasabog
**Masamang Arkitektura:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Scalable Solution:**```python
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
**Ano Ito:** Ang mga bagong dokumento ay hindi maaaring makuha hanggang sa muling itayo ang index.
**Masama Halimbawa:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Solusyon: Incremental Indexing**```python
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

## Mga Sukatan ng Pagsusuri para sa RAG
### Katumpakan ng Konteksto
Sinusukat kung gaano karaming mga nakuhang chunks ang aktwal na nauugnay.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Kaugnayan ng Sagot
Ang mga sukat kung ang nabuong sagot ay talagang tumutugon sa query.
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

### Katapatan
Sinusukat kung ang sagot ay batay sa nakuhang konteksto (hindi hallucinated).
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
### Pag-aaral ng Kaso 1: Customer Support Chatbot
**Problema:** Nagbigay ang Chatbot ng mga maling sagot tungkol sa mga feature ng produkto.
**Pagsusuri sa Root Cause:**
- Chunking split feature na mga paglalarawan sa mga hangganan
- Nahanap ang pagkuha ng bahagyang impormasyon
- LLM hallucinated nawawalang mga detalye
**Solusyon:**
- Ipinatupad ang semantic chunking ng mga seksyon ng tampok
- Nagdagdag ng 150-token na overlap sa pagitan ng mga chunks
- Tumaas na top_k mula 3 hanggang 5
- Nagdagdag ng hakbang sa muling pagraranggo
**Mga Resulta:**
- Napabuti ang katumpakan mula 62% hanggang 89%
- Bumaba ang Hallucination rate mula 23% hanggang 4%
- Tumaas ang kasiyahan ng customer ng 35%
### Pag-aaral ng Kaso 2: Paghahanap ng Legal na Dokumento
**Problema:** Hindi mahanap ng mga abogado ang mga nauugnay na precedent.
**Ugat Dahilan:**
- Hindi nakuha ng mga generic na pag-embed ang mga legal na semantika
- Nabigo ang mga negation query ("mga kaso kung saan HINDI itinatag ang pananagutan")
- Walang temporal na pagsala para sa mga binaligtad na kaso
**Solusyon:**
- Pino-pinong mga pag-embed sa legal na corpus
- Ipinatupad ang negation handling
- Nagdagdag ng metadata ng katayuan ng kaso at pag-filter
- Binuo ang multi-hop retrieval para sa mga citation chain
**Mga Resulta:**
- Napabuti ang Recall@10 mula 45% hanggang 78%
- Binawasan ang oras ng paghahanap mula 8s hanggang 1.2s
- Ang pag-ampon ng legal na koponan ay tumaas ng 3x
### Pag-aaral ng Kaso 3: Teknikal na Dokumentasyon
**Problema:** Hindi mahanap ng mga developer ang mga halimbawa ng code.
**Ugat Dahilan:**
- Hindi maganda ang pagkaka-embed ng mga bloke ng code sa mga text-only na modelo
- Mga query tulad ng "paano magpatotoo" na tumugma sa teorya, hindi mga halimbawa
- Walang pagkakaiba sa pagitan ng mga bersyon ng API
**Solusyon:**
- Ginamit na code-aware na modelo ng pag-embed
- Mga naka-tag na tipak ayon sa uri ng nilalaman (konsepto, tutorial, sanggunian ng API, halimbawa)
- Nagdagdag ng metadata ng bersyon
- Ipinatupad ang pag-uuri ng layunin para sa pagruruta ng query
**Mga Resulta:**
- Katumpakan ng pagkuha ng halimbawa ng code: 34% → 82%
- Nabawasan ng 60% ang time-to-first-successful-query
- Tumaas ng 45% ang trapiko ng dokumentasyon