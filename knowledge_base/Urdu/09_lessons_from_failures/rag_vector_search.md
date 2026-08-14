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
# RAG اور ویکٹر تلاش کی ناکامیاں
یہ دستاویز Retrieval-Augmented Generation (RAG) سسٹمز، ایمبیڈنگ استعمال، اور ویکٹر کی تلاش کے نفاذ میں عام ناکامیوں کو یکجا کرتی ہے۔
---

## بیڈ آر اے جی (ریٹریول-آگمینٹڈ جنریشن)
Retrieval-Augmented Generation (RAG) زیادہ درست اور سیاق و سباق سے متعلقہ ردعمل پیدا کرنے کے لیے بازیافت کے نظام کو جنریٹو AI کے ساتھ جوڑتا ہے۔ خراب RAG کا نفاذ خراب بازیافت کے معیار، ناکافی سیاق و سباق سے نمٹنے، یا نسل کے مسائل کا شکار ہے۔
### ناقص چنکنگ حکمت عملی
**بری مثال:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**مسائل:**
- جملے اور پیراگراف کو من مانی طور پر تقسیم کیا گیا ہے۔
- سیاق و سباق ٹکڑوں کی حدود میں کھو گیا ہے۔
- معنوی معنی بکھرا ہوا ہے۔
- بازیافت نامکمل معلومات لوٹاتا ہے۔
**بہتر نقطہ نظر:**```python
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

### سیاق و سباق کا اوورلیپ غائب ہے۔
**بری مثال:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**بہتر نقطہ نظر:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### استفسار کے ارادے کو نظر انداز کرنا
**بری مثال:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**بہتر نقطہ نظر:**```python
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

### سیاق و سباق کی ونڈو اوور فلو
**بری مثال:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**بہتر نقطہ نظر:**```python
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

## خراب ایمبیڈنگز
ایمبیڈنگز اعداد و شمار کی ویکٹر نمائندگی ہیں جو سیمنٹک معنی کو حاصل کرتی ہیں۔ خراب ایمبیڈنگز ماڈل کے ناقص انتخاب، ناکافی تربیت، یا غلط استعمال کے نتیجے میں ہوتی ہیں۔
### ڈومین کے لیے غلط ماڈل
**بری مثال:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**بہتر نقطہ نظر:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### ویکٹر کو نارمل نہیں کرنا
**بری مثال:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**بہتر نقطہ نظر:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### ایمبیڈنگ ڈائمینشنز کو نظر انداز کرنا
**بری مثال:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**بہتر نقطہ نظر:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## خراب ویکٹر کی تلاش
ویکٹر کی تلاش اعلی جہتی سرایت پر معنوی مماثلت کی تلاش کو قابل بناتی ہے۔ خراب عمل درآمد ناقص انڈیکس کنفیگریشن، نامناسب فاصلاتی میٹرکس، یا اسکیل ایبلٹی مسائل کا شکار ہیں۔
### غلط فاصلہ میٹرک
**بری مثال:**```python
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

**یہ برا کیوں ہے:**
- یوکلیڈین فاصلہ ویکٹر کی شدت سے متاثر ہوتا ہے۔
- نارملائزڈ ویکٹر کے لیے، کوزائن مماثلت (ڈاٹ پروڈکٹ) مناسب ہے۔
- سیمنٹک تلاش کے لیے نتائج کم درست ہوں گے۔
**بہتر نقطہ نظر:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### انڈیکس آپٹیمائزیشن غائب ہے۔
**بری مثال:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**بہتر نقطہ نظر:**```python
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

### اعلی جہتی ڈیٹا کو ہینڈل نہیں کرنا
**بری مثال:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**بہتر نقطہ نظر:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### یادداشت کو نظر انداز کرنا بمقابلہ لیٹنسی ٹریڈ آف
**بری مثال:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**بہتر نقطہ نظر:**```python
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

## بہترین طریقوں کا خلاصہ
### RAG سسٹمز
1. **حکمت عملی سے ٹکڑا**: معنوی حدود کا احترام کریں، اوورلیپ شامل کریں۔
2. **استفسار کے ارادے پر غور کریں**: صارف کی خواہش کی بنیاد پر بازیافت کو اپنائیں
3. **سیاق و سباق کا نظم کریں**: LLM ٹوکن کی حدود میں رہیں
4. **اختتام سے آخر تک کا اندازہ کریں**: مکمل RAG پائپ لائن کی جانچ کریں، نہ صرف بازیافت
### ایمبیڈنگز
1. **ڈومین کے لیے موزوں ماڈلز کا انتخاب کریں**: ماڈل کو اپنے مواد کی قسم سے ملائیں
2. **ویکٹرز کو معمول بنائیں**: کوزائن مماثلت کے لیے ضروری ہے۔
3. **مستقل مزاجی**: اپنے پورے سسٹم میں ایک ہی ماڈل استعمال کریں۔
4. **مانیٹر ڈرفٹ**: ڈیٹا تیار ہوتے ہی ایمبیڈنگز کو دوبارہ تربیت یا اپ ڈیٹ کریں۔
### ویکٹر کی تلاش
1. **دائیں فاصلہ میٹرک کو منتخب کریں**: معنوی کے لیے COSINE، مقامی کے لیے EUCLID
2. **انڈیکس ترتیب دیں**: بڑے ڈیٹا سیٹس کے لیے HNSW استعمال کریں۔
3. **ٹیون پیرامیٹرز**: آپ کے استعمال کے کیس کے لیے بیلنس ریکال بمقابلہ لیٹنسی
4. **کارکردگی کو مانیٹر کریں**: وقت کے ساتھ تلاش کے معیار اور تاخیر کو ٹریک کریں۔
---

## متعلقہ موضوعات
- **AI/LLM ناکامیاں**: فریب اور استدلال کے مسائل کے لیے`ai_llm_failures.md`دیکھیں
- **ایجنٹ ڈیزائن**: RAG کے ساتھ ایجنٹ بنانے کے لیے`../05_agents/agent_system_design.md`دیکھیں
- **ڈیٹا سیٹ کوالٹی**: ڈیٹا کی تربیت کے لیے`../08_machine_learning/ml_data_issues.md`دیکھیں
- **فوری انجینئرنگ**: سیاق و سباق سے نمٹنے کی تکنیکوں کے لیے`../02_artificial_intelligence/prompt_engineering.md`دیکھیں
---

## اعلی درجے کی RAG ناکامی کے پیٹرنز
### درمیانی رجحان میں کھو گیا۔
**یہ کیا ہے:** ایل ایل ایم سیاق و سباق کے آغاز اور آخر میں معلومات پر توجہ مرکوز کرتے ہیں، 
درمیانی مواد کو نظر انداز کرنا۔
**بری مثال:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**یہ برا کیوں ہے:**
- درمیانی حصوں میں اہم معلومات کو نظر انداز کیا جا سکتا ہے۔
- درمیانی مواد کے لیے ماڈل کی توجہ کم ہو جاتی ہے۔
- غیر متعلقہ بازیافت شدہ مواد پر ٹوکن ضائع کرتا ہے۔
**تخفیف:**```python
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

### ملٹی ہاپ بازیافت کی ناکامیاں
**یہ کیا ہے:** معلومات کی بازیافت میں ناکامی جس کے لیے متعدد مربوط ٹکڑوں کی ضرورت ہوتی ہے۔
**بری مثال:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**تخفیف:**```python
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

### وقتی استدلال کی ناکامیاں
**یہ کیا ہے:** RAG سسٹم وقت کے لحاظ سے حساس سوالات اور پرانی معلومات کے ساتھ جدوجہد کرتے ہیں۔
**بری مثال:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**تخفیف:**```python
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

### نفی سے نمٹنے میں ناکامیاں
**یہ کیا ہے:** معنوی تلاش اکثر سوالات میں نفی سے محروم رہتی ہے۔
**بری مثال:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**تخفیف:**```python
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

## اینٹی پیٹرنز کو سرایت کرنا
### ایمبیڈنگ ماڈلز کو ملانا
**یہ کیا ہے:** انڈیکسنگ بمقابلہ استفسار کے لیے مختلف ماڈلز کا استعمال مماثلت کو توڑ دیتا ہے۔
**بری مثال:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**یہ برا کیوں ہے:**
- مختلف ماڈل غیر مطابقت پذیر ویکٹر خالی جگہوں میں سرایت پیدا کرتے ہیں۔
- مختلف ماڈل ایمبیڈنگ کے درمیان کوزائن کی مماثلت بے ترتیب شور ہے۔
- سسٹم کام کرتا دکھائی دیتا ہے لیکن کچرا واپس کرتا ہے۔
** کھوج:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### ایمبیڈنگ ڈائمینشنز کو نظر انداز کرنا
**یہ کیا ہے:** کارکردگی پر سرایت کرنے والے طول و عرض کے اثرات پر غور نہیں کرنا۔
**تجارتی بندش:**
| طول و عرض | پیشہ | Cons | کیس استعمال کریں |
|------------|------|------|----------|
| کم (128-256) | تیز تلاش، کم میموری | کم اہم نمائندگی | آسان کام، بڑے پیمانے پر |
| میڈیم (384-768) | اچھا توازن | اعتدال پسند وسائل | عام مقصد |
| ہائی (1024+) | بھرپور نمائندگی | سست، یادداشت کی شدت | پیچیدہ سیمنٹک کام |
**بری مثال:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### خصوصی ٹوکن ہینڈل نہیں کرنا
**یہ کیا ہے:** یو آر ایل، کوڈ، نمبرز، اور خصوصی حروف کو صحیح طریقے سے ہینڈل کرنے میں ناکام ہونا۔
**بری مثال:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**تخفیف:**```python
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

## ویکٹر تلاش کی کارکردگی کے مسائل
### اسکیلنگ کے مسائل
**یہ کیا ہے:** ڈیٹا سیٹ کے بڑھنے کے ساتھ تلاش کا معیار یا تاخیر کم ہوتی جاتی ہے۔
**علامات:**
- لیٹینسی ڈیٹاسیٹ کے سائز کے ساتھ لکیری طور پر بڑھ جاتی ہے۔
- مزید ویکٹر شامل ہونے کے ساتھ ہی ڈراپس کو یاد کریں۔
- میموری کا استعمال پھٹ جاتا ہے۔
**خراب فن تعمیر:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**توسیع پذیر حل:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### کولڈ اسٹارٹ کا مسئلہ
**یہ کیا ہے:** نئی دستاویزات اس وقت تک بازیافت نہیں ہوتی جب تک کہ انڈیکس دوبارہ نہیں بنایا جاتا۔
**بری مثال:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**حل: انکریمنٹل انڈیکسنگ**```python
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

## RAG کے لیے تشخیصی میٹرکس
### سیاق و سباق کی درستگی
پیمائش کرتا ہے کہ کتنے بازیافت شدہ ٹکڑے درحقیقت متعلقہ ہیں۔
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### جواب کی مطابقت
اقدامات اگر پیدا کردہ جواب درحقیقت استفسار کو پورا کرتا ہے۔
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

### وفا۔۔
اگر جواب بازیافت شدہ سیاق و سباق میں بنیاد ہے تو اقدامات (غلط نہیں)۔
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

## حقیقی دنیا کے کیس اسٹڈیز
### کیس اسٹڈی 1: کسٹمر سپورٹ چیٹ بوٹ
**مسئلہ:** چیٹ بوٹ نے پروڈکٹ کی خصوصیات کے بارے میں غلط جوابات دیئے۔
**جڑ کا تجزیہ:**
- حدود کے پار تقسیم کی خصوصیت کی تفصیل
- بازیافت میں جزوی معلومات ملی
- LLM کی گمشدہ تفصیلات
**حل:**
- فیچر سیکشنز کے ذریعہ سیمنٹک چنکنگ کا نفاذ
- ٹکڑوں کے درمیان 150 ٹوکن اوورلیپ شامل کیا گیا۔
- top_k کو 3 سے بڑھا کر 5 کر دیا۔
- دوبارہ درجہ بندی کا مرحلہ شامل کیا گیا۔
**نتائج:**
- درستگی 62% سے 89% تک بہتر ہو گئی
- ہیلوسینیشن کی شرح 23 فیصد سے کم ہو کر 4 فیصد رہ گئی
- صارفین کی اطمینان میں 35 فیصد اضافہ ہوا
### کیس اسٹڈی 2: قانونی دستاویز کی تلاش
**مسئلہ:** وکلاء متعلقہ نظیریں تلاش نہیں کر سکے۔
**جڑ کی وجہ:**
- عام ایمبیڈنگ نے قانونی سیمنٹکس کو حاصل نہیں کیا۔
- نفی کے سوالات ناکام ہوئے ("ایسے معاملات جہاں ذمہ داری قائم نہیں ہوئی")
- الٹ جانے والے کیسز کے لیے کوئی وقتی فلٹرنگ نہیں۔
**حل:**
- قانونی کارپس پر ٹھیک ٹیونڈ ایمبیڈنگز
- لاگو نفی ہینڈلنگ
- کیس اسٹیٹس میٹا ڈیٹا اور فلٹرنگ شامل کی گئی۔
- حوالہ زنجیروں کے لئے ملٹی ہاپ بازیافت
**نتائج:**
- Recall@10 45% سے 78% تک بہتر
- تلاش کا وقت 8s سے کم کر کے 1.2s کر دیا گیا ہے۔
- قانونی ٹیم کے ذریعہ گود لینے میں 3 گنا اضافہ ہوا۔
### کیس اسٹڈی 3: تکنیکی دستاویزات
**مسئلہ:** ڈیولپرز کوڈ کی مثالیں نہیں مل سکے۔
**جڑ کی وجہ:**
- کوڈ بلاکس صرف ٹیکسٹ ماڈلز کے ساتھ خراب ایمبیڈڈ ہیں۔
- مماثل تھیوری "کیسے تصدیق کی جائے" جیسے سوالات، مثالیں نہیں۔
- API ورژن کے درمیان کوئی فرق نہیں۔
**حل:**
- استعمال شدہ کوڈ سے آگاہ ایمبیڈنگ ماڈل
- مواد کی قسم کے لحاظ سے ٹیگ کردہ ٹکڑے (تصور، ٹیوٹوریل، API حوالہ، مثال)
- ورژن میٹا ڈیٹا شامل کیا گیا۔
- استفسار کی روٹنگ کے لیے ارادے کی درجہ بندی کا نفاذ
**نتائج:**
- کوڈ کی مثال کی بازیافت کی درستگی: 34% → 82%
- وقت سے پہلے کامیاب سوال 60% کم ہو گیا
- دستاویزی ٹریفک میں 45 فیصد اضافہ ہوا