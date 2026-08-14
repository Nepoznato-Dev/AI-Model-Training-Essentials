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

# RAG এবং ভেক্টর অনুসন্ধান ব্যর্থতা
এই নথিটি পুনরুদ্ধার-অগমেন্টেড জেনারেশন (RAG) সিস্টেম, এম্বেডিং ব্যবহার এবং ভেক্টর অনুসন্ধান বাস্তবায়নে সাধারণ ব্যর্থতাগুলিকে একত্রিত করে।
---

## খারাপ RAG (পুনরুদ্ধার-অগমেন্টেড জেনারেশন)
পুনরুদ্ধার-অগমেন্টেড জেনারেশন (RAG) আরও নির্ভুল এবং প্রাসঙ্গিকভাবে প্রাসঙ্গিক প্রতিক্রিয়া তৈরি করতে জেনারেটিভ এআই-এর সাথে পুনরুদ্ধার সিস্টেমগুলিকে একত্রিত করে। খারাপ RAG বাস্তবায়ন খারাপ পুনরুদ্ধার গুণমান, অপর্যাপ্ত প্রসঙ্গ পরিচালনা, বা প্রজন্মের সমস্যায় ভোগে।
### খারাপ চাঙ্কিং কৌশল
**খারাপ উদাহরণ:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**সমস্যা:**
- বাক্য এবং অনুচ্ছেদ নির্বিচারে বিভক্ত করা হয়
- প্রসঙ্গ খণ্ড সীমানায় হারিয়ে গেছে
- শব্দার্থক অর্থ খণ্ডিত
- পুনরুদ্ধার অসম্পূর্ণ তথ্য প্রদান করে
**উত্তম পদ্ধতি:**```python
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

### অনুপস্থিত প্রসঙ্গ ওভারল্যাপ
**খারাপ উদাহরণ:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**উত্তম পদ্ধতি:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### প্রশ্নের অভিপ্রায় উপেক্ষা করা
**খারাপ উদাহরণ:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**উত্তম পদ্ধতি:**```python
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

### প্রসঙ্গ উইন্ডো ওভারফ্লো
**খারাপ উদাহরণ:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**উত্তম পদ্ধতি:**```python
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

## খারাপ এমবেডিং
এমবেডিং হল ডেটার ভেক্টর উপস্থাপনা যা শব্দার্থগত অর্থ ক্যাপচার করে। খারাপ মডেল নির্বাচন, অপর্যাপ্ত প্রশিক্ষণ, বা অনুপযুক্ত ব্যবহারের ফলে খারাপ এমবেডিং হয়।
### ডোমেনের জন্য ভুল মডেল
**খারাপ উদাহরণ:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**উত্তম পদ্ধতি:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### ভেক্টরকে স্বাভাবিক করে না
**খারাপ উদাহরণ:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**উত্তম পদ্ধতি:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### এম্বেডিং মাত্রা উপেক্ষা করা
**খারাপ উদাহরণ:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**উত্তম পদ্ধতি:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## খারাপ ভেক্টর অনুসন্ধান
ভেক্টর অনুসন্ধান উচ্চ-মাত্রিক এম্বেডিংয়ের উপর শব্দার্থিক মিল অনুসন্ধান সক্ষম করে। খারাপ বাস্তবায়ন দুর্বল সূচক কনফিগারেশন, অনুপযুক্ত দূরত্ব মেট্রিক্স, বা স্কেলেবিলিটি সমস্যায় ভোগে।
### ভুল দূরত্ব মেট্রিক
**খারাপ উদাহরণ:**```python
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

**কেন এটা খারাপ:**
- ইউক্লিডীয় দূরত্ব ভেক্টর মাত্রা দ্বারা প্রভাবিত হয়
- স্বাভাবিক ভেক্টরের জন্য, কোসাইন সাদৃশ্য (ডট পণ্য) উপযুক্ত
- শব্দার্থিক অনুসন্ধানের জন্য ফলাফল কম নির্ভুল হবে
**উত্তম পদ্ধতি:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### অনুপস্থিত সূচক অপ্টিমাইজেশন
**খারাপ উদাহরণ:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**উত্তম পদ্ধতি:**```python
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

### উচ্চ-মাত্রিক ডেটা পরিচালনা করছে না
**খারাপ উদাহরণ:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**উত্তম পদ্ধতি:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### রিকল বনাম লেটেন্সি ট্রেডঅফ উপেক্ষা করা
**খারাপ উদাহরণ:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**উত্তম পদ্ধতি:**```python
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

## সর্বোত্তম অনুশীলনের সারাংশ
### RAG সিস্টেম
1. **কৌশলগতভাবে খণ্ড করুন**: শব্দার্থিক সীমানাকে সম্মান করুন, ওভারল্যাপ যোগ করুন
2. **কোয়েরির অভিপ্রায় বিবেচনা করুন**: ব্যবহারকারী যা চায় তার উপর ভিত্তি করে পুনরুদ্ধারকে মানিয়ে নিন
3. **প্রসঙ্গ পরিচালনা করুন**: LLM টোকেন সীমার মধ্যে থাকুন
4. **এন্ড-টু-এন্ড মূল্যায়ন করুন**: সম্পূর্ণ RAG পাইপলাইন পরীক্ষা করুন, শুধু পুনরুদ্ধার নয়
### এমবেডিং
1. **ডোমেন-উপযুক্ত মডেলগুলি চয়ন করুন**: আপনার সামগ্রীর প্রকারের সাথে মডেলের মিল করুন
2. **ভেক্টরকে স্বাভাবিক করুন**: কোসাইন সাদৃশ্যের জন্য অপরিহার্য
3. **সংগতি**: আপনার সিস্টেম জুড়ে একই মডেল ব্যবহার করুন
4. **মনিটর ড্রিফ্ট**: ডেটা বিকশিত হওয়ার সাথে সাথে এম্বেডিংগুলিকে পুনরায় প্রশিক্ষণ বা আপডেট করুন৷
### ভেক্টর অনুসন্ধান
1. **ডান দূরত্ব মেট্রিক নির্বাচন করুন**: শব্দার্থের জন্য COSINE, স্থানিকের জন্য EUCLID
2. **সূচীগুলি কনফিগার করুন**: বড় ডেটাসেটের জন্য HNSW ব্যবহার করুন
3. **টিউন প্যারামিটার**: আপনার ব্যবহারের ক্ষেত্রে ব্যালেন্স রিকল বনাম লেটেন্সি
4. **কর্মক্ষমতা নিরীক্ষণ**: সময়ের সাথে সাথে অনুসন্ধানের গুণমান এবং লেটেন্সি ট্র্যাক করুন
---

## সম্পর্কিত বিষয়
- **AI/LLM ব্যর্থতা**: হ্যালুসিনেশন এবং যুক্তি সংক্রান্ত সমস্যার জন্য`ai_llm_failures.md`দেখুন
- **এজেন্ট ডিজাইন**: RAG দিয়ে এজেন্ট তৈরির জন্য`../05_agents/agent_system_design.md`দেখুন
- **ডেটাসেটের গুণমান**: প্রশিক্ষণ ডেটা বিবেচনার জন্য`../08_machine_learning/ml_data_issues.md`দেখুন
- **প্রম্পট ইঞ্জিনিয়ারিং**: প্রসঙ্গ পরিচালনার কৌশলগুলির জন্য`../02_artificial_intelligence/prompt_engineering.md`দেখুন
---

## উন্নত RAG ব্যর্থতার নিদর্শন
### মধ্য ঘটনাতে হারিয়ে গেছে
**এটি কী:** এলএলএমগুলি প্রেক্ষাপটের শুরুতে এবং শেষে তথ্যের উপর ফোকাস করে, 
মধ্যম বিষয়বস্তু উপেক্ষা।
**খারাপ উদাহরণ:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**কেন এটা খারাপ:**
- মাঝামাঝি অংশে সমালোচনামূলক তথ্য উপেক্ষা করা যেতে পারে
- মধ্যম বিষয়বস্তুর জন্য মডেল মনোযোগ হ্রাস
- অপ্রাসঙ্গিক পুনরুদ্ধার করা সামগ্রীতে টোকেন নষ্ট করে
**প্রশমন:**```python
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

### মাল্টি-হপ পুনরুদ্ধার ব্যর্থতা
**এটি কী:** একাধিক সংযুক্ত টুকরা প্রয়োজন এমন তথ্য পুনরুদ্ধার করতে ব্যর্থ।
**খারাপ উদাহরণ:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**প্রশমন:**```python
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

### টেম্পোরাল রিজনিং ব্যর্থতা
**এটি কী:** RAG সিস্টেমগুলি সময়-সংবেদনশীল প্রশ্ন এবং পুরানো তথ্যের সাথে লড়াই করে।
**খারাপ উদাহরণ:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**প্রশমন:**```python
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

### নেতিবাচক হ্যান্ডলিং ব্যর্থতা
**এটি কী:** শব্দার্থগত অনুসন্ধান প্রায়শই প্রশ্নগুলিতে অস্বীকার মিস করে।
**খারাপ উদাহরণ:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**প্রশমন:**```python
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

## এন্টি-প্যাটার্ন এম্বেড করা
### মিক্সিং এমবেডিং মডেল
**এটা কি:** ইনডেক্সিং বনাম ক্যোয়ারী করার জন্য বিভিন্ন মডেল ব্যবহার করলে মিল ভেঙ্গে যায়।
**খারাপ উদাহরণ:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**কেন এটা খারাপ:**
- বিভিন্ন মডেল বেমানান ভেক্টর স্থানগুলিতে এমবেডিং তৈরি করে
- বিভিন্ন মডেল এমবেডিংয়ের মধ্যে কোসাইন সাদৃশ্য হল এলোমেলো শব্দ
- সিস্টেম কাজ করছে বলে মনে হয় কিন্তু আবর্জনা ফেরত দেয়
**শনাক্তকরণ:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### এম্বেডিং মাত্রা উপেক্ষা করা
**এটি কী:** কর্মক্ষমতার উপর এম্বেডিং মাত্রার প্রভাব বিবেচনা করে না।
**বাণিজ্য বন্ধ:**
| মাত্রা | পেশাদার | কনস | কেস ব্যবহার করুন |
|------------|------|------|----------|
| কম (128-256) | দ্রুত অনুসন্ধান, কম স্মৃতি | কম সংক্ষিপ্ত উপস্থাপনা | সহজ কাজ, বড় স্কেল |
| মাঝারি (384-768) | ভাল ভারসাম্য | পরিমিত সম্পদ | সাধারণ উদ্দেশ্য |
| উচ্চ (1024+) | সমৃদ্ধ উপস্থাপনা | ধীর, স্মৃতি-নিবিড় | জটিল শব্দার্থিক কাজ |
**খারাপ উদাহরণ:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### বিশেষ টোকেন পরিচালনা করা হচ্ছে না
**এটি কী:** সঠিকভাবে ইউআরএল, কোড, সংখ্যা এবং বিশেষ অক্ষর পরিচালনা করতে ব্যর্থ হওয়া।
**খারাপ উদাহরণ:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**প্রশমন:**```python
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

## ভেক্টর অনুসন্ধান কর্মক্ষমতা সমস্যা
### স্কেলিং সমস্যা
**এটি কী:** ডেটাসেট বাড়ার সাথে সাথে অনুসন্ধানের গুণমান বা লেটেন্সি হ্রাস পায়।
**লক্ষণ:**
- লেটেন্সি ডেটাসেটের আকারের সাথে রৈখিকভাবে বৃদ্ধি পায়
- আরও ভেক্টর যুক্ত হওয়ার সাথে সাথে ড্রপগুলি প্রত্যাহার করুন
- মেমরি ব্যবহার বিস্ফোরিত
**খারাপ আর্কিটেকচার:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**স্কেলযোগ্য সমাধান:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### কোল্ড স্টার্টের সমস্যা
**এটি কী:** ইনডেক্স পুনর্নির্মাণ না হওয়া পর্যন্ত নতুন নথিগুলি পুনরুদ্ধারযোগ্য নয়।
**খারাপ উদাহরণ:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**সমাধান: ইনক্রিমেন্টাল ইনডেক্সিং**```python
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

## RAG এর জন্য মূল্যায়ন মেট্রিক্স
### প্রসঙ্গ যথার্থতা
কতগুলি পুনরুদ্ধার করা অংশগুলি আসলে প্রাসঙ্গিক তা পরিমাপ করে৷
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### উত্তর প্রাসঙ্গিকতা
পরিমাপ করা হয় যদি উত্পন্ন উত্তর প্রকৃতপক্ষে প্রশ্নের ঠিকানা দেয়।
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

### বিশ্বস্ততা
উত্তর পুনরুদ্ধার করা প্রসঙ্গে (হ্যালুসিনেটেড নয়) ভিত্তিক হলে পরিমাপ করুন।
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

## বাস্তব-বিশ্ব কেস স্টাডিজ
### কেস স্টাডি 1: কাস্টমার সাপোর্ট চ্যাটবট
**সমস্যা:** চ্যাটবট পণ্যের বৈশিষ্ট্য সম্পর্কে ভুল উত্তর দিয়েছে।
**মূল কারণ বিশ্লেষণ:**
- চঙ্কিং বিভক্ত বৈশিষ্ট্য বর্ণনা সীমানা জুড়ে
- পুনরুদ্ধার আংশিক তথ্য পাওয়া গেছে
- এলএলএম হ্যালুসিনেটেড অনুপস্থিত বিবরণ
**সমাধান:**
- বৈশিষ্ট্য বিভাগ দ্বারা বাস্তবায়িত শব্দার্থিক খণ্ড
- খণ্ডগুলির মধ্যে 150-টোকেন ওভারল্যাপ যোগ করা হয়েছে৷
- top_k 3 থেকে 5 পর্যন্ত বেড়েছে৷
- পুনরায় র‌্যাঙ্কিং ধাপ যোগ করা হয়েছে
**ফলাফল:**
- সঠিকতা 62% থেকে 89% এ উন্নত হয়েছে
- হ্যালুসিনেশন হার 23% থেকে 4% এ নেমে এসেছে
- গ্রাহক সন্তুষ্টি 35% বৃদ্ধি পেয়েছে
### কেস স্টাডি 2: আইনি নথি অনুসন্ধান
**সমস্যা:** আইনজীবীরা প্রাসঙ্গিক নজির খুঁজে পাননি।
**মূল কারণ:**
- জেনেরিক এম্বেডিং আইনি শব্দার্থকে ক্যাপচার করেনি
- নেতিবাচক প্রশ্ন ব্যর্থ হয়েছে ("যে ক্ষেত্রে দায়বদ্ধতা প্রতিষ্ঠিত হয়নি")
- উল্টে যাওয়া ক্ষেত্রে কোন অস্থায়ী ফিল্টারিং নেই
**সমাধান:**
- আইনী সংস্থার উপর সূক্ষ্ম সুরযুক্ত এম্বেডিং
- বাস্তবায়িত নেগেটিভ হ্যান্ডলিং
- কেস স্ট্যাটাস মেটাডেটা এবং ফিল্টারিং যোগ করা হয়েছে
- উদ্ধৃতি চেইন জন্য মাল্টি-হপ পুনরুদ্ধার নির্মিত
**ফলাফল:**
- Recall@10 45% থেকে 78% এ উন্নত হয়েছে
- অনুসন্ধানের সময় 8s থেকে 1.2s এ কমে গেছে
- আইনি দল দ্বারা দত্তক 3x বৃদ্ধি
### কেস স্টাডি 3: প্রযুক্তিগত ডকুমেন্টেশন
**সমস্যা:** ডেভেলপাররা কোডের উদাহরণ খুঁজে পায়নি।
**মূল কারণ:**
- শুধুমাত্র টেক্সট মডেলের সাথে খারাপভাবে এম্বেড করা কোড ব্লক
- "কীভাবে প্রমাণীকরণ করা যায়" এর মতো প্রশ্নগুলি মিলে যাওয়া তত্ত্ব, উদাহরণ নয়
- API সংস্করণগুলির মধ্যে কোন পার্থক্য নেই
**সমাধান:**
- ব্যবহৃত কোড-সচেতন এম্বেডিং মডেল
- বিষয়বস্তুর প্রকার দ্বারা ট্যাগ করা অংশগুলি (ধারণা, টিউটোরিয়াল, API রেফারেন্স, উদাহরণ)
- সংস্করণ মেটাডেটা যোগ করা হয়েছে
- ক্যোয়ারী রাউটিং জন্য অভিপ্রায় শ্রেণীবিভাগ বাস্তবায়িত
**ফলাফল:**
- কোড উদাহরণ পুনরুদ্ধার সঠিকতা: 34% → 82%
- সময়-টু-প্রথম-সফল-কোয়েরি 60% কমেছে
- ডকুমেন্টেশন ট্রাফিক 45% বৃদ্ধি পেয়েছে