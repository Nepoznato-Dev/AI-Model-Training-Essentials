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
# فشل بحث RAG وVector
تعمل هذه الوثيقة على دمج حالات الفشل الشائعة في أنظمة إنشاء الاسترجاع المعزز (RAG)، واستخدام التضمين، وتطبيقات بحث المتجهات.
---

## Bad RAG (جيل الاسترجاع المعزز)
يجمع الجيل المعزز للاسترجاع (RAG) بين أنظمة الاسترجاع والذكاء الاصطناعي التوليدي لإنتاج استجابات أكثر دقة وملاءمة للسياق. تعاني تطبيقات RAG السيئة من ضعف جودة الاسترجاع، أو عدم كفاية التعامل مع السياق، أو مشكلات في الإنشاء.
### استراتيجية التقطيع الضعيفة
**مثال سيء:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**المشاكل:**
- يتم تقسيم الجمل والفقرات بشكل تعسفي
- يتم فقدان السياق عند حدود القطعة
- المعنى الدلالي مجزأ
- استرجاع إرجاع معلومات غير كاملة
** نهج أفضل: **```python
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

### تداخل السياق المفقود
**مثال سيء:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

** نهج أفضل: **```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### تجاهل نية الاستعلام
**مثال سيء:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

** نهج أفضل: **```python
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

### تجاوز سعة نافذة السياق
**مثال سيء:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

** نهج أفضل: **```python
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

## التضمينات السيئة
التضمينات هي تمثيلات متجهة للبيانات التي تلتقط المعنى الدلالي. تنتج عمليات التضمين السيئة عن سوء اختيار النموذج أو التدريب غير الكافي أو الاستخدام غير السليم.
### نموذج خاطئ للمجال
**مثال سيء:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

** نهج أفضل: **```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### عدم تطبيع المتجهات
**مثال سيء:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

** نهج أفضل: **```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### تجاهل أبعاد التضمين
**مثال سيء:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

** نهج أفضل: **```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## بحث متجه سيء
يتيح البحث المتجه إمكانية البحث عن التشابه الدلالي عبر التضمينات عالية الأبعاد. تعاني التطبيقات السيئة من ضعف تكوين الفهرس، أو مقاييس المسافة غير المناسبة، أو مشكلات قابلية التوسع.
### قياس المسافة الخاطئة
**مثال سيء:**```python
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

**لماذا هو سيء:**
- المسافة الإقليدية تتأثر بحجم المتجه
- بالنسبة للمتجهات المقيسة، يكون تشابه جيب التمام (المنتج النقطي) مناسبًا
- النتائج ستكون أقل دقة للبحث الدلالي
** نهج أفضل: **```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### تحسين الفهرس مفقود
**مثال سيء:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

** نهج أفضل: **```python
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

### عدم التعامل مع البيانات عالية الأبعاد
**مثال سيء:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

** نهج أفضل: **```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### تجاهل الاستدعاء مقابل مقايضة زمن الوصول
**مثال سيء:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

** نهج أفضل: **```python
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

## ملخص أفضل الممارسات
### أنظمة RAG
1. **التقسيم بشكل استراتيجي**: احترم الحدود الدلالية وأضف التداخل
2. **ضع في اعتبارك غرض الاستعلام**: قم بتكييف عملية الاسترجاع بناءً على ما يريده المستخدم
3. **إدارة السياق**: ابق ضمن حدود رموز LLM المميزة
4. **التقييم الشامل**: اختبار مسار RAG الكامل، وليس الاسترجاع فقط
### التضمينات
1. **اختر النماذج المناسبة للمجال**: قم بمطابقة النموذج مع نوع المحتوى الخاص بك
2. **تطبيع المتجهات**: ضروري لتشابه جيب التمام
3. **الاتساق**: استخدم نفس النموذج في نظامك بأكمله
4. **Monitor Drift**: إعادة تدريب التضمينات أو تحديثها مع تطور البيانات
### بحث المتجهات
1. **حدد مقياس المسافة الصحيح**: COSINE للدلالات، وEUCLID للمكانية
2. **تكوين الفهارس**: استخدم HNSW لمجموعات البيانات الكبيرة
3. **ضبط المعلمات**: موازنة الاستدعاء مقابل زمن الوصول لحالة الاستخدام الخاصة بك
4. **مراقبة الأداء**: تتبع جودة البحث ووقت الاستجابة مع مرور الوقت
---

## موضوعات ذات صلة
- **فشل AI/LLM**: راجع`ai_llm_failures.md`للتعرف على مشكلات الهلوسة والاستدلال
- **تصميم الوكيل**: راجع`../05_agents/agent_system_design.md`للتعرف على وكلاء البناء باستخدام RAG
- **جودة مجموعة البيانات**: راجع`../08_machine_learning/ml_data_issues.md`للتعرف على اعتبارات بيانات التدريب
- **الهندسة الفورية**: راجع`../02_artificial_intelligence/prompt_engineering.md`للتعرف على تقنيات التعامل مع السياق
---

## أنماط فشل RAG المتقدمة
### ظاهرة الضياع في الوسط
**ما هو:** يميل حاملو ماجستير إدارة الأعمال إلى التركيز على المعلومات في بداية السياق ونهايته، 
تجاهل المحتوى الأوسط.
**مثال سيء:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**لماذا هو سيء:**
- قد يتم التغاضي عن المعلومات الهامة في الأجزاء الوسطى
- يتضاءل الاهتمام بالنموذج بالنسبة للمحتوى المتوسط
- إهدار الرموز المميزة على محتوى مسترد غير ذي صلة
**التخفيف:**```python
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

### فشل استرداد القفزات المتعددة
**ما هو:** الفشل في استرداد المعلومات التي تتطلب عدة أجزاء متصلة.
**مثال سيء:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**التخفيف:**```python
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

### فشل الاستدلال الزمني
**ما هو:** تواجه أنظمة RAG صعوبة في التعامل مع الاستعلامات الحساسة للوقت والمعلومات القديمة.
**مثال سيء:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**التخفيف:**```python
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

### فشل التعامل مع النفي
**ما هو:** غالبًا ما يفتقد البحث الدلالي علامات النفي في الاستعلامات.
**مثال سيء:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**التخفيف:**```python
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

## تضمين الأنماط المضادة
### خلط نماذج التضمين
**ما هو:** يؤدي استخدام نماذج مختلفة للفهرسة مقابل الاستعلام إلى كسر التشابه.
**مثال سيء:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**لماذا هو سيء:**
- تنتج النماذج المختلفة تضمينات في مساحات متجهة غير متوافقة
- تشابه جيب التمام بين تضمينات النماذج المختلفة هو ضوضاء عشوائية
- يبدو أن النظام يعمل ولكنه يُرجع البيانات المهملة
**كشف:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### تجاهل أبعاد التضمين
**ما هو:** عدم مراعاة تأثير تضمين البعد على الأداء.
**المقايضات:**
| الأبعاد | الايجابيات | سلبيات | حالة الاستخدام |
|------------|------|------|----------|
| منخفض (١٢٨-٢٥٦) | بحث سريع، ذاكرة أقل | تمثيلات أقل دقة | مهام بسيطة، واسعة النطاق |
| المتوسطة (384-768) | توازن جيد | موارد معتدلة | غرض عام |
| عالية (1024+) | تمثيلات غنية | بطيئة، كثيفة الذاكرة | المهام الدلالية المعقدة |
**مثال سيء:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### عدم التعامل مع الرموز الخاصة
**ما هو:** الفشل في التعامل مع عناوين URL والأكواد والأرقام والأحرف الخاصة بشكل صحيح.
**مثال سيء:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**التخفيف:**```python
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

## مشكلات أداء بحث المتجهات
### مشاكل القياس
**ما هو:** تتدهور جودة البحث أو زمن الاستجابة مع نمو مجموعة البيانات.
**الأعراض:**
- يزداد زمن الوصول خطيًا مع حجم مجموعة البيانات
- انخفاض الاستدعاء مع إضافة المزيد من المتجهات
- استخدام الذاكرة ينفجر
**الهندسة المعمارية السيئة:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**حل قابل للتطوير:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### مشكلة البداية الباردة
**ما هو:** لا يمكن استرجاع المستندات الجديدة إلا بعد إعادة بناء الفهرس.
**مثال سيء:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**الحل: الفهرسة التزايدية**```python
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

## مقاييس التقييم لـ RAG
### دقة السياق
يقيس عدد القطع المستردة ذات الصلة بالفعل.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### صلة الإجابة
التدابير إذا تم إنشاء الإجابة تعالج بالفعل الاستعلام.
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

### الإخلاص
التدابير إذا كانت الإجابة مستندة إلى سياق مسترجع (غير مهلوس).
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

## دراسات الحالة في العالم الحقيقي
### دراسة الحالة 1: Chatbot لدعم العملاء
**المشكلة:** قدم برنامج Chatbot إجابات غير صحيحة حول ميزات المنتج.
**تحليل السبب الجذري:**
- تقطيع أوصاف ميزة الانقسام عبر الحدود
- العثور على استرجاع معلومات جزئية
- LLM هلوسة التفاصيل المفقودة
**الحل:**
- تم تنفيذ التقطيع الدلالي حسب أقسام الميزة
- تمت إضافة 150 رمزًا متداخلًا بين القطع
- زيادة top_k من 3 إلى 5
- أضيفت خطوة إعادة الترتيب
**النتائج:**
- تم تحسين الدقة من 62% إلى 89%
- انخفضت نسبة الهلوسة من 23% إلى 4%
- زيادة رضا العملاء بنسبة 35%
### دراسة الحالة 2: البحث في المستندات القانونية
**المشكلة:** لم يتمكن المحامون من العثور على سوابق ذات صلة.
**السبب الجذري:**
- التضمينات العامة لم تلتقط الدلالات القانونية
- فشلت استعلامات النفي ("الحالات التي لم يتم فيها إثبات المسؤولية")
- لا يوجد تصفية زمنية للقضايا المنقلبة
**الحل:**
- التضمين الدقيق في النصوص القانونية
- تنفيذ معالجة النفي
- أضيفت البيانات الوصفية لحالة الحالة والتصفية
- بناء استرجاع متعدد القفزات لسلاسل الاقتباس
**النتائج:**
- تحسن معدل Recall@10 من 45% إلى 78%
- تم تقليل وقت البحث من 8 ثوانٍ إلى 1.2 ثانية
- زاد اعتماد الفريق القانوني 3 مرات
### دراسة الحالة 3: التوثيق الفني
**المشكلة:** لم يتمكن المطورون من العثور على أمثلة للتعليمات البرمجية.
**السبب الجذري:**
- كتل التعليمات البرمجية المضمنة بشكل سيئ في النماذج النصية فقط
- استعلامات مثل "كيفية المصادقة" مطابقة للنظرية، وليس الأمثلة
- لا يوجد تمييز بين إصدارات API
**الحل:**
- نموذج التضمين المدرك للكود المستخدم
- الأجزاء الموسومة حسب نوع المحتوى (المفهوم، البرنامج التعليمي، مرجع واجهة برمجة التطبيقات، مثال)
- أضيفت البيانات الوصفية للنسخة
- تم تنفيذ تصنيف النوايا لتوجيه الاستعلام
**النتائج:**
- دقة استرجاع مثال الكود: 34% → 82%
- تم تقليل الوقت اللازم لأول استعلام ناجح بنسبة 60%
- زيادة حركة التوثيق بنسبة 45%