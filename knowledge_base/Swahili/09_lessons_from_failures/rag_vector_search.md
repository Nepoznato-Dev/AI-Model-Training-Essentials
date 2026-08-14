<!--
---
# Metadata
title: "RAG and Vector Search Failures"
description: "RAG and vector search pitfalls"
category: "Lessons from Failures"
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

-->
# Kushindwa kwa Utafutaji wa RAG na Vekta
Hati hii inaunganisha makosa ya kawaida katika mifumo ya Urejeshaji-Uboreshaji wa Mifumo (RAG), matumizi ya upachikaji, na utekelezaji wa utafutaji wa vekta.
---

## RAG Mbaya (Urejeshaji-Kizazi Kilichoongezwa)
Retrieval-Augmented Generation (RAG) inachanganya mifumo ya kurejesha na AI ya kuzalisha ili kutoa majibu sahihi zaidi na yanayohusiana kimuktadha. Utekelezaji mbaya wa RAG huathiriwa na ubora duni wa urejeshaji, ushughulikiaji duni wa muktadha, au masuala ya kizazi.
### Mkakati Mbaya wa Chunking
**Mfano Mbaya:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Matatizo:**
- Sentensi na aya zimegawanywa kiholela
- Muktadha umepotea kwenye mipaka ya chunk
- Maana ya kisemantiki imegawanyika
- Urejeshaji hurejesha habari isiyo kamili
**Njia Bora:**```python
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

### Muktadha Unaokosa Muingiliano
**Mfano Mbaya:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Njia Bora:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Kupuuza Kusudi la Hoji
**Mfano Mbaya:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Njia Bora:**```python
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

### Dirisha la Muktadha Kufurika
**Mfano Mbaya:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Njia Bora:**```python
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

## Upachikaji Mbaya
Upachikaji ni viwakilishi vya vekta vya data vinavyonasa maana ya kisemantiki. Upachikaji mbaya hutokana na uteuzi duni wa muundo, mafunzo duni au matumizi yasiyofaa.
### Muundo Mbaya wa Kikoa
**Mfano Mbaya:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Njia Bora:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Kutorekebisha Vekta
**Mfano Mbaya:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Njia Bora:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Kupuuza Vipimo vya Kupachika
**Mfano Mbaya:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Njia Bora:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Utafutaji Mbaya wa Vekta
Utafutaji wa Vekta huwezesha utafutaji wa mfanano wa kisemantiki juu ya upachikaji wa hali ya juu. Utekelezaji mbaya unakabiliwa na usanidi duni wa faharasa, vipimo vya umbali visivyofaa, au matatizo ya kuongeza kasi.
### Kipimo cha Umbali Si sahihi
**Mfano Mbaya:**```python
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

**Kwa nini ni mbaya:**
- Umbali wa Euclidean huathiriwa na ukubwa wa vekta
- Kwa vekta za kawaida, kufanana kwa cosine (bidhaa ya nukta) inafaa
- Matokeo hayatakuwa sahihi sana kwa utafutaji wa kimaana
**Njia Bora:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Uboreshaji wa Fahirisi
**Mfano Mbaya:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Njia Bora:**```python
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

### Kutoshughulikia Data ya Ukubwa wa Juu
**Mfano Mbaya:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Njia Bora:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Kupuuza Recall vs Latency Tradeoff
**Mfano Mbaya:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Njia Bora:**```python
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

## Muhtasari wa Mbinu Bora
### Mifumo ya RAG
1. **Chunk Strategically**: Heshimu mipaka ya kisemantiki, ongeza mwingiliano
2. **Zingatia Kusudi la Kuuliza**: Badilisha urejeshaji kulingana na kile mtumiaji anataka
3. **Dhibiti Muktadha**: Kaa ndani ya vikomo vya tokeni za LLM
4. **Tathmini Mwisho-hadi-Mwisho**: Jaribu bomba kamili la RAG, si urejeshaji tu
### Upachikaji
1. **Chagua Miundo Inayofaa ya Kikoa**: Linganisha muundo na aina ya maudhui yako
2. **Rekebisha Vekta**: Muhimu kwa kufanana kwa kosine
3. **Uthabiti**: Tumia muundo sawa katika mfumo wako wote
4. **Monitor Drift**: Funza upya au usasishe upachikaji data kadri inavyoendelea
### Utafutaji wa Vekta
1. **Chagua Kipimo cha Umbali wa Kulia**: COSINE ya semantiki, EUCLID ya anga
2. **Sanidi Fahirisi**: Tumia HNSW kwa seti kubwa za data
3. **Rekebisha Vigezo**: Kukumbuka salio dhidi ya muda wa kusubiri kwa kesi yako ya utumiaji
4. **Fuatilia Utendaji**: Fuatilia ubora wa utafutaji na muda wa kusubiri
---

## Mada Zinazohusiana
- **AI/LLM Kufeli**: Tazama`ai_llm_failures.md`kwa maonyesho na masuala ya hoja
- **Muundo wa Wakala**: Tazama`../05_agents/agent_system_design.md`kwa mawakala wa ujenzi walio na RAG
- **Ubora wa Seti ya Data**: Tazama`../08_machine_learning/ml_data_issues.md`kwa kuzingatia data ya mafunzo
- **Uhandisi wa Haraka**: Angalia`../02_artificial_intelligence/prompt_engineering.md`kwa mbinu za kushughulikia muktadha
---

## Mifumo ya Juu ya Kushindwa kwa RAG
### Imepotea Katika Hali ya Kati
**Ilivyo:** LLMs huwa zinalenga habari mwanzoni na mwisho wa muktadha, 
kupuuza maudhui ya kati.
**Mfano Mbaya:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Kwa nini ni mbaya:**
- Taarifa muhimu katika sehemu za kati zinaweza kupuuzwa
- Umakini wa mfano hupungua kwa maudhui ya kati
- Taka tokeni kwenye maudhui yasiyo na maana yaliyopatikana
**Kupunguza:**```python
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

### Urejeshaji wa Multi-Hop Umeshindwa
**Ilivyo:** Imeshindwa kupata maelezo ambayo yanahitaji vipande vingi vilivyounganishwa.
**Mfano Mbaya:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Kupunguza:**```python
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

### Kushindwa kwa Sababu za Muda
**Ilivyo:** Mifumo ya RAG inatatizika na hoja nyeti kwa wakati na maelezo yaliyopitwa na wakati.
**Mfano Mbaya:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Kupunguza:**```python
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

### Kukanusha Kushughulikia Kushindwa
**Ilivyo:** Utafutaji wa kisemantiki mara nyingi hukosa kukanusha katika hoja.
**Mfano Mbaya:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Kupunguza:**```python
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

## Kupachika Miundo ya Kupinga
### Kuchanganya Miundo ya Kupachika
**Ilivyo:** Kutumia miundo tofauti ya kuorodhesha dhidi ya kuuliza huvunja ulinganifu.
**Mfano Mbaya:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Kwa nini ni mbaya:**
- Aina tofauti hutoa upachikaji katika nafasi za vekta zisizolingana
- Kufanana kwa Cosine kati ya upachikaji wa muundo tofauti ni kelele isiyo ya kawaida
- Mfumo unaonekana kufanya kazi lakini unarudisha takataka
**Ugunduzi:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Kupuuza Vipimo vya Kupachika
**Ilivyo:** Bila kuzingatia athari za mwelekeo wa kupachika kwenye utendakazi.
**Mabadiliko ya biashara:**
| Vipimo | Faida | Hasara | Tumia Kesi |
|------------|------|------|-----------|
| Chini (128-256) | Utafutaji wa haraka, kumbukumbu kidogo | Uwakilishi mdogo | Kazi rahisi, kiwango kikubwa |
| Wastani (384-768) | Usawa mzuri | Rasilimali za wastani | Kusudi la jumla |
| Juu (1024+) | Uwakilishi tajiri | Polepole, yenye kumbukumbu nyingi | Kazi changamano za kisemantiki |
**Mfano Mbaya:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Kutoshughulikia Tokeni Maalum
**Ilivyo:** Imeshindwa kushughulikia URL, msimbo, nambari na herufi maalum ipasavyo.
**Mfano Mbaya:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Kupunguza:**```python
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

## Masuala ya Utendaji ya Utafutaji wa Vekta
### Kuongeza Matatizo
**Ilivyo:** Ubora wa utafutaji au muda wa kusubiri huharibika kadiri mkusanyiko wa data unavyoongezeka.
**Dalili:**
- Muda wa kusubiri huongezeka kulingana na saizi ya data
- Kumbuka matone kadri vekta zaidi zinaongezwa
- Matumizi ya kumbukumbu hulipuka
** Usanifu Mbaya:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

** Suluhisho linaloweza kubadilika:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Tatizo la Kuanza Baridi
**Ilivyo:** Hati mpya haziwezi kurejeshwa hadi faharasa itakapoundwa upya.
**Mfano Mbaya:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Suluhisho: Uwekaji Faharasa wa Kuongezeka**```python
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

## Vipimo vya Tathmini vya RAG
### Usahihi wa Muktadha
Hupima ni sehemu ngapi zilizorejeshwa zinafaa.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Jibu Umuhimu
Hatua ikiwa jibu limetolewa hushughulikia swali.
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

### Uaminifu
Hatua ikiwa jibu limeegemezwa katika muktadha uliorejeshwa (sio kuorodheshwa).
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

## Uchunguzi wa Kisa Ulimwenguni Halisi
### Uchunguzi Kifani 1: Chatbot ya Usaidizi kwa Wateja
**Tatizo:** Chatbot ilitoa majibu yasiyo sahihi kuhusu vipengele vya bidhaa.
**Uchambuzi wa Chanzo Chanzo:**
- Chunking mgawanyiko kipengele maelezo katika mipaka
- Retrieval kupatikana sehemu ya taarifa
- LLM iliibua maelezo yanayokosekana
**Suluhisho:**
- Kutekelezwa kwa semantic chunking na sehemu za kipengele
- Imeongeza mwingiliano wa ishara 150 kati ya vipande
- Kuongezeka kwa top_k kutoka 3 hadi 5
- Imeongeza hatua ya kuweka tena nafasi
**Matokeo:**
- Usahihi umeboreshwa kutoka 62% hadi 89%
- Kiwango cha uchungu kilipungua kutoka 23% hadi 4%
- Kuridhika kwa Wateja kuliongezeka kwa 35%
### Uchunguzi kifani 2: Utafutaji wa Hati ya Kisheria
**Tatizo:** Wanasheria hawakuweza kupata mifano muhimu.
**Chanzo Cha msingi:**
- Upachikaji wa jumla haukunasa semantiki za kisheria
- Maswali ya kukanusha yameshindwa ("kesi ambazo dhima HAIJAanzishwa")
- Hakuna uchujaji wa muda kwa kesi zilizopinduliwa
**Suluhisho:**
- Upachikaji uliopangwa vizuri kwenye kosi ya kisheria
- Ushughulikiaji wa kukanusha uliotekelezwa
- Metadata ya hali ya kesi iliyoongezwa na kuchuja
- Imeunda urejeshaji wa hop nyingi kwa minyororo ya manukuu
**Matokeo:**
- Kumbuka @ 10 imeboreshwa kutoka 45% hadi 78%
- Muda wa utafutaji umepunguzwa kutoka 8s hadi 1.2s
- Kuasili kwa timu ya wanasheria kuliongezeka mara 3
### Uchunguzi kifani 3: Hati za Kiufundi
**Tatizo:** Wasanidi programu hawakuweza kupata mifano ya msimbo.
**Chanzo Cha msingi:**
- Vizuizi vya msimbo vilivyopachikwa vibaya kwa miundo ya maandishi pekee
- Hoja kama "jinsi ya kuthibitisha" nadharia inayolingana, si mifano
- Hakuna tofauti kati ya matoleo ya API
**Suluhisho:**
- Muundo wa upachikaji unaotambua msimbo uliotumika
- Vipande vilivyowekwa alama na aina ya yaliyomo (dhana, mafunzo, kumbukumbu ya API, mfano)
- Aliongeza toleo metadata
- Uainishaji wa dhamira uliotekelezwa kwa uelekezaji wa hoja
**Matokeo:**
- Usahihi wa kurejesha mfano wa msimbo: 34% → 82%
- Swali la kufaulu-kwa-kwanza-limepunguzwa kwa 60%
- Trafiki ya hati iliongezeka 45%