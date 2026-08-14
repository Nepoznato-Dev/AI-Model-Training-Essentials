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
# شکست RAG و Vector Search
این سند خرابی‌های رایج در سیستم‌های Retrieval-Augmented Generation (RAG)، استفاده از جاسازی و پیاده‌سازی‌های جستجوی برداری را ادغام می‌کند.
---

## بد RAG (نسل افزایش یافته بازیابی)
Retrieval-Augmented Generation (RAG) سیستم‌های بازیابی را با هوش مصنوعی مولد ترکیب می‌کند تا پاسخ‌های دقیق‌تر و مرتبط‌تری را تولید کند. پیاده‌سازی‌های بد RAG از کیفیت بازیابی ضعیف، مدیریت نامناسب زمینه یا مشکلات تولید رنج می‌برند.
### استراتژی ضعیف خرد کردن
**مثال بد:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**مشکلات:**
- جملات و پاراگراف ها خودسرانه تقسیم می شوند
- زمینه در مرزهای تکه گم می شود
- معنای معنایی پراکنده است
- بازیابی اطلاعات ناقص را برمی گرداند
**رویکرد بهتر:**```python
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

### همپوشانی زمینه وجود ندارد
**مثال بد:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**رویکرد بهتر:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### نادیده گرفتن هدف پرس و جو
**مثال بد:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**رویکرد بهتر:**```python
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

### سرریز پنجره زمینه
**مثال بد:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**رویکرد بهتر:**```python
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

## جاسازی های بد
جاسازی ها بازنمایی های برداری از داده ها هستند که معنای معنایی را به دست می آورند. تعبیه‌های بد ناشی از انتخاب ضعیف مدل، آموزش ناکافی یا استفاده نادرست است.
### مدل اشتباه برای دامنه
**مثال بد:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**رویکرد بهتر:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### بردارها را عادی نمی کند
**مثال بد:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**رویکرد بهتر:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### نادیده گرفتن ابعاد جاسازی
**مثال بد:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**رویکرد بهتر:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## جستجوی وکتور بد
جستجوی برداری، جستجوی تشابه معنایی را بر روی جاسازی‌های با ابعاد بالا فعال می‌کند. پیاده سازی های بد از پیکربندی شاخص ضعیف، معیارهای فاصله نامناسب یا مشکلات مقیاس پذیری رنج می برند.
### متریک فاصله اشتباه
**مثال بد:**```python
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

**چرا بد است:**
- فاصله اقلیدسی تحت تأثیر قدر برداری است
- برای بردارهای نرمال شده تشابه کسینوس (ضرب نقطه) مناسب است
- نتایج برای جستجوی معنایی دقت کمتری خواهند داشت
**رویکرد بهتر:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### بهینه سازی شاخص وجود ندارد
**مثال بد:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**رویکرد بهتر:**```python
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

### داده های با ابعاد بالا را مدیریت نمی کند
**مثال بد:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**رویکرد بهتر:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### نادیده گرفتن Recall در مقابل Latency Tradeoff
**مثال بد:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**رویکرد بهتر:**```python
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

## خلاصه بهترین شیوه ها
### سیستم های RAG
1. **چونک از نظر استراتژیک**: به مرزهای معنایی احترام بگذارید، همپوشانی اضافه کنید
2. ** قصد پرس و جو را در نظر بگیرید **: بازیابی را بر اساس آنچه کاربر می خواهد تطبیق دهید
3. **مدیریت زمینه**: در محدوده توکن LLM بمانید
4. **ارزیابی End-to-End**: آزمایش خط لوله RAG کامل، نه فقط بازیابی
### جاسازی ها
1. **مدل های مناسب دامنه را انتخاب کنید**: مدل را با نوع محتوای خود مطابقت دهید
2. **Normalize Vectors**: برای تشابه کسینوس ضروری است
3. **ثبات **: از یک مدل در سراسر سیستم خود استفاده کنید
4. **Monitor Drift**: تعبیه‌ها را با تکامل داده‌ها دوباره آموزش دهید یا به‌روزرسانی کنید
### جستجوی برداری
1. **متریک فاصله سمت راست را انتخاب کنید**: COSINE برای معنایی، EUCLID برای فضایی
2. **پیکربندی شاخص ها**: از HNSW برای مجموعه داده های بزرگ استفاده کنید
3. ** پارامترهای تنظیم **: یادآوری تعادل در مقابل تأخیر برای مورد استفاده شما
4. ** نظارت بر عملکرد **: کیفیت جستجو و تأخیر را در طول زمان پیگیری کنید
---

## موضوعات مرتبط
- **شکست های AI/LLM**: برای توهمات و مسائل استدلالی به`ai_llm_failures.md`مراجعه کنید
- **طراحی عامل**: برای ساخت عوامل با RAG به`../05_agents/agent_system_design.md`مراجعه کنید
- **کیفیت مجموعه داده**: برای ملاحظات داده های آموزشی به`../08_machine_learning/ml_data_issues.md`مراجعه کنید
- **مهندسی سریع**: برای تکنیک های مدیریت زمینه به`../02_artificial_intelligence/prompt_engineering.md`مراجعه کنید
---

## الگوهای شکست RAG پیشرفته
### گمشده در پدیده میانه
**چیست:** LLM ها تمایل دارند روی اطلاعات در ابتدا و انتهای زمینه تمرکز کنند، 
نادیده گرفتن محتوای میانی
**مثال بد:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**چرا بد است:**
- اطلاعات مهم در بخش های میانی ممکن است نادیده گرفته شود
- توجه مدل برای محتوای متوسط کاهش می یابد
- توکن‌ها را روی محتوای بازیابی شده بی‌ربط هدر می‌دهد
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

### شکست در بازیابی چند هاپ
**چیست:** بازیابی اطلاعاتی که به چندین قطعه متصل نیاز دارد بازیابی نشد.
**مثال بد:**```markdown
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

### شکست های استدلال موقت
**چیست:** سیستم های RAG با پرس و جوهای حساس به زمان و اطلاعات قدیمی دست و پنجه نرم می کنند.
**مثال بد:**```markdown
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

### شکست های رسیدگی به نفی
**چیست:** جستجوی معنایی اغلب نفی را در جستارها از دست می دهد.
**مثال بد:**```markdown
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

## تعبیه ضد الگوها
### مخلوط کردن مدل های جاسازی
**چیست:** استفاده از مدل های مختلف برای نمایه سازی در مقابل پرس و جو شباهت را از بین می برد.
**مثال بد:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**چرا بد است:**
- مدل های مختلف تعبیه هایی را در فضاهای برداری ناسازگار تولید می کنند
- شباهت کسینوس بین جاسازی های مدل های مختلف نویز تصادفی است
- به نظر می رسد که سیستم کار می کند اما زباله ها را برمی گرداند
**تشخیص:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### نادیده گرفتن ابعاد جاسازی
**چیست:** عدم در نظر گرفتن تأثیر ابعاد تعبیه شده بر عملکرد.
** معاوضه ها:**
| ابعاد | جوانب مثبت | معایب | مورد استفاده |
|------------|------|------|----------|
| کم (128-256) | جستجوی سریع، حافظه کمتر | نمایش های ظریف کمتر | کارهای ساده، در مقیاس بزرگ |
| متوسط ​​(384-768) | تعادل خوب | منابع متوسط ​​| هدف عمومی |
| بالا (1024+) | نمایندگی های غنی | آهسته و پرحافظه | وظایف پیچیده معنایی |
**مثال بد:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### عدم رسیدگی به توکن های خاص
**چیست:** ناتوانی در مدیریت صحیح URL ها، کدها، اعداد و کاراکترهای خاص.
**مثال بد:**```python
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

## مشکلات عملکرد جستجوی برداری
### مشکلات مقیاس بندی
**چیست:** با افزایش مجموعه داده ها، کیفیت جستجو یا تأخیر کاهش می یابد.
**علائم:**
- تاخیر به صورت خطی با اندازه مجموعه افزایش می یابد
- با اضافه شدن بردارهای بیشتر، به یاد بیاورید
- استفاده از حافظه منفجر می شود
**معماری بد:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**راه حل مقیاس پذیر:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### مشکل شروع سرد
**چیست:** اسناد جدید تا زمانی که فهرست دوباره ساخته نشود قابل بازیابی نیستند.
**مثال بد:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**راه حل: نمایه سازی افزایشی**```python
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

## معیارهای ارزیابی برای RAG
### دقت زمینه
اندازه گیری تعداد تکه های بازیابی شده واقعا مرتبط هستند.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### ارتباط پاسخ
اندازه‌گیری می‌کند اگر پاسخ تولید شود در واقع به پرس و جو می‌پردازد.
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

### وفاداری
اگر پاسخ در زمینه بازیابی شده باشد (نه توهم) را اندازه گیری می کند.
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

## مطالعات موردی در دنیای واقعی
### مطالعه موردی 1: چت ربات پشتیبانی مشتری
**مشکل:** Chatbot پاسخ های نادرستی در مورد ویژگی های محصول داد.
**تحلیل علت ریشه ای:**
- توضیحات ویژگی تقسیم تکه در سراسر مرزها
- بازیابی اطلاعات جزئی یافت شده است
- LLM توهم از دست رفته جزئیات
**راه حل:**
- اجرای تکه تکه معنایی توسط بخش های ویژگی
- اضافه شدن 150 توکن همپوشانی بین تکه ها
- افزایش top_k از 3 به 5
- اضافه شدن مرحله رتبه بندی مجدد
**نتایج:**
- دقت از 62% به 89% بهبود یافته است
- میزان توهم از 23 درصد به 4 درصد کاهش یافته است.
- افزایش رضایت مشتری 35 درصد
### مطالعه موردی 2: جستجوی اسناد حقوقی
**مشکل:** وکلا نتوانستند سوابق مربوطه را پیدا کنند.
**علت اصلی:**
- تعبیه‌های عمومی معنای حقوقی را در بر نمی‌گیرد
- پرس و جوهای نفی ناموفق بود ("مواردی که مسئولیت ایجاد نشد")
- بدون فیلتر زمانی برای موارد واژگون
**راه حل:**
- تعبیه‌های دقیق در مجموعه حقوقی
- مدیریت نفی را اجرا کرد
- اضافه شدن ابرداده وضعیت پرونده و فیلتر
- ساخته شده بازیابی چند هاپ برای زنجیره های استناد
**نتایج:**
- Recall@10 از 45% به 78% بهبود یافته است
- زمان جستجو از 8 ثانیه به 1.2 ثانیه کاهش یافت
- پذیرش توسط تیم حقوقی 3 برابر افزایش یافت
### مطالعه موردی 3: مستندات فنی
**مشکل:** توسعه دهندگان نتوانستند نمونه کد را پیدا کنند.
**علت اصلی:**
- بلوک‌های کد با مدل‌های متنی ضعیف جاسازی شده‌اند
- پرس و جوهایی مانند "چگونه احراز هویت" تئوری منطبق، نه مثال
- عدم تمایز بین نسخه های API
**راه حل:**
- استفاده از مدل تعبیه کد آگاه
- تکه های برچسب گذاری شده بر اساس نوع محتوا (مفهوم، آموزش، مرجع API، مثال)
- اضافه شدن ابرداده نسخه
- طبقه بندی قصد پیاده سازی برای مسیریابی پرس و جو
**نتایج:**
- دقت بازیابی کد: 34٪ → 82٪
- پرس و جوی زمان تا اولین موفقیت 60 درصد کاهش یافت
- ترافیک اسناد 45 درصد افزایش یافته است