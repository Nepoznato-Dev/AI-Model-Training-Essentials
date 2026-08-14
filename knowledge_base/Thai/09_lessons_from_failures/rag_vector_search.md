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
# ความล้มเหลวในการค้นหา RAG และเวกเตอร์
เอกสารนี้รวบรวมความล้มเหลวทั่วไปในระบบการดึงข้อมูล-Augmented Generation (RAG) การใช้งานแบบฝัง และการใช้งานการค้นหาเวกเตอร์
---

## Bad RAG (การดึงข้อมูล-การสร้างเสริม)
การดึงข้อมูล-Augmented Generation (RAG) ผสมผสานระบบการดึงข้อมูลเข้ากับ generative AI เพื่อสร้างการตอบสนองที่แม่นยำและเกี่ยวข้องกับบริบทมากขึ้น การใช้งาน RAG ที่ไม่ดีประสบปัญหาคุณภาพการดึงข้อมูลต่ำ การจัดการบริบทไม่เพียงพอ หรือปัญหาการสร้าง
### กลยุทธ์การแบ่งชิ้นที่ไม่ดี
**ตัวอย่างที่ไม่ดี:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**ปัญหา:**
- ประโยคและย่อหน้าจะถูกแบ่งตามอำเภอใจ
- บริบทหายไปที่ขอบเขตก้อน
- ความหมายเชิงความหมายมีการแยกส่วน
- การดึงข้อมูลส่งคืนข้อมูลที่ไม่สมบูรณ์
**แนวทางที่ดีกว่า:**```python
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

### ขาดบริบทที่ทับซ้อนกัน
**ตัวอย่างที่ไม่ดี:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**แนวทางที่ดีกว่า:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### ละเว้นเจตนาการค้นหา
**ตัวอย่างที่ไม่ดี:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**แนวทางที่ดีกว่า:**```python
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

### หน้าต่างบริบทล้น
**ตัวอย่างที่ไม่ดี:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**แนวทางที่ดีกว่า:**```python
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

## การฝังที่ไม่ดี
การฝังคือการแสดงเวกเตอร์ของข้อมูลที่รวบรวมความหมายเชิงความหมาย การฝังที่ไม่ถูกต้องเป็นผลมาจากการเลือกแบบจำลองที่ไม่ดี การฝึกอบรมที่ไม่เพียงพอ หรือการใช้งานที่ไม่เหมาะสม
### โมเดลโดเมนไม่ถูกต้อง
**ตัวอย่างที่ไม่ดี:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**แนวทางที่ดีกว่า:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### ไม่ใช่การทำให้เวกเตอร์เป็นมาตรฐาน
**ตัวอย่างที่ไม่ดี:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**แนวทางที่ดีกว่า:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### ละเว้นมิติการฝัง
**ตัวอย่างที่ไม่ดี:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**แนวทางที่ดีกว่า:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## การค้นหาเวกเตอร์ที่ไม่ดี
การค้นหาเวกเตอร์ช่วยให้สามารถค้นหาความคล้ายคลึงทางความหมายเหนือการฝังมิติสูง การใช้งานที่ไม่ดีประสบปัญหาจากการกำหนดค่าดัชนีที่ไม่ดี การวัดระยะทางที่ไม่เหมาะสม หรือปัญหาความสามารถในการปรับขนาด
### การวัดระยะทางผิด
**ตัวอย่างที่ไม่ดี:**```python
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

**ทำไมมันแย่:**
- ระยะทางแบบยุคลิดได้รับผลกระทบจากขนาดเวกเตอร์
- สำหรับเวกเตอร์ที่ทำให้เป็นมาตรฐาน ความคล้ายคลึงของโคไซน์ (ผลคูณดอท) มีความเหมาะสม
- ผลลัพธ์จะแม่นยำน้อยลงสำหรับการค้นหาความหมาย
**แนวทางที่ดีกว่า:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### การเพิ่มประสิทธิภาพดัชนีที่ขาดหายไป
**ตัวอย่างที่ไม่ดี:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**แนวทางที่ดีกว่า:**```python
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

### ไม่จัดการกับข้อมูลมิติสูง
**ตัวอย่างที่ไม่ดี:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**แนวทางที่ดีกว่า:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### การเพิกเฉยต่อการเรียกคืนเทียบกับการแลกเปลี่ยนเวลาแฝง
**ตัวอย่างที่ไม่ดี:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**แนวทางที่ดีกว่า:**```python
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

## สรุปแนวทางปฏิบัติที่ดีที่สุด
### ระบบ RAG
1. **ส่วนเชิงกลยุทธ์**: เคารพขอบเขตความหมาย เพิ่มความทับซ้อนกัน
2. **พิจารณาจุดประสงค์ในการสืบค้น**: ปรับการดึงข้อมูลตามความต้องการของผู้ใช้
3. **จัดการบริบท**: อยู่ภายในขีดจำกัดโทเค็น LLM
4. **ประเมินตั้งแต่ต้นทางถึงปลายทาง**: ทดสอบไปป์ไลน์ RAG เต็มรูปแบบ ไม่ใช่แค่การดึงข้อมูลเท่านั้น
### การฝัง
1. **เลือกโมเดลที่เหมาะสมกับโดเมน**: จับคู่โมเดลกับประเภทเนื้อหาของคุณ
2. **ทำให้เวกเตอร์เป็นมาตรฐาน**: จำเป็นสำหรับความคล้ายคลึงของโคไซน์
3. **ความสม่ำเสมอ**: ใช้รุ่นเดียวกันทั่วทั้งระบบของคุณ
4. **Monitor Drift**: ฝึกใหม่หรืออัปเดตการฝังเมื่อข้อมูลมีการพัฒนา
### ค้นหาเวกเตอร์
1. **เลือกเมตริกระยะทางที่ถูกต้อง**: COSINE สำหรับความหมาย EUCLID สำหรับเชิงพื้นที่
2. **กำหนดค่าดัชนี**: ใช้ HNSW สำหรับชุดข้อมูลขนาดใหญ่
3. **ปรับแต่งพารามิเตอร์**: ปรับสมดุลการเรียกคืนเทียบกับเวลาแฝงสำหรับกรณีการใช้งานของคุณ
4. **ตรวจสอบประสิทธิภาพ**: ติดตามคุณภาพการค้นหาและเวลาในการตอบสนองเมื่อเวลาผ่านไป
---

## หัวข้อที่เกี่ยวข้อง
- **ความล้มเหลวของ AI/LLM**: ดู`ai_llm_failures.md`สำหรับปัญหาภาพหลอนและการใช้เหตุผล
- **การออกแบบตัวแทน**: ดู`../05_agents/agent_system_design.md`สำหรับตัวแทนการสร้างด้วย RAG
- **คุณภาพชุดข้อมูล**: ดู`../08_machine_learning/ml_data_issues.md`สำหรับข้อควรพิจารณาเกี่ยวกับข้อมูลการฝึกอบรม
- **วิศวกรรมพร้อมท์**: ดู`../02_artificial_intelligence/prompt_engineering.md`สำหรับเทคนิคการจัดการบริบท
---

## รูปแบบความล้มเหลว RAG ขั้นสูง
### หลงทางในปรากฏการณ์ภาคกลาง
**มันคืออะไร:** LLM มักจะมุ่งเน้นไปที่ข้อมูลที่จุดเริ่มต้นและจุดสิ้นสุดของบริบท 
โดยไม่สนใจเนื้อหาตรงกลาง
**ตัวอย่างที่ไม่ดี:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**ทำไมมันแย่:**
- ข้อมูลที่สำคัญในส่วนตรงกลางอาจถูกมองข้าม
- ความสนใจของโมเดลลดลงสำหรับเนื้อหาระดับกลาง
- เสียโทเค็นกับเนื้อหาที่ดึงมาที่ไม่เกี่ยวข้อง
**การบรรเทาผลกระทบ:**```python
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

### ความล้มเหลวในการดึงข้อมูล Multi-Hop
**มันคืออะไร:** ล้มเหลวในการดึงข้อมูลที่ต้องใช้ชิ้นส่วนที่เชื่อมต่อกันหลายชิ้น
**ตัวอย่างที่ไม่ดี:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**การบรรเทาผลกระทบ:**```python
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

### ความล้มเหลวในการใช้เหตุผลชั่วคราว
**มันคืออะไร:** ระบบ RAG ประสบปัญหากับการสืบค้นตามเวลาและข้อมูลที่ล้าสมัย
**ตัวอย่างที่ไม่ดี:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**การบรรเทาผลกระทบ:**```python
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

### ความล้มเหลวในการจัดการการปฏิเสธ
**มันคืออะไร:** การค้นหาเชิงความหมายมักจะพลาดการปฏิเสธในข้อความค้นหา
**ตัวอย่างที่ไม่ดี:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**การบรรเทาผลกระทบ:**```python
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

## การฝังรูปแบบต่อต้าน
### การผสมโมเดลการฝัง
**สิ่งนี้คืออะไร:** การใช้โมเดลที่แตกต่างกันสำหรับการจัดทำดัชนีและการสืบค้นทำให้ความคล้ายคลึงกันลดลง
**ตัวอย่างที่ไม่ดี:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**ทำไมมันแย่:**
- โมเดลที่แตกต่างกันทำให้เกิดการฝังในพื้นที่เวกเตอร์ที่เข้ากันไม่ได้
- ความคล้ายคลึงโคไซน์ระหว่างการฝังโมเดลต่างๆ คือสัญญาณรบกวนแบบสุ่ม
- ระบบดูเหมือนทำงานแต่ส่งคืนขยะ
**การตรวจจับ:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### ละเว้นมิติการฝัง
**สิ่งนี้คืออะไร:** ไม่ได้คำนึงถึงผลกระทบของมิติข้อมูลแบบฝังที่มีต่อประสิทธิภาพ
**การแลกเปลี่ยน:**
| ขนาด | ข้อดี | ข้อเสีย | ใช้กรณี |
|------------|------|-|----------|
| ต่ำ (128-256) | ค้นหาได้เร็ว หน่วยความจำน้อย | การแสดงที่เหมาะสมน้อยกว่า | งานง่ายๆ สเกลใหญ่ |
| ปานกลาง (384-768) | สมดุลดี | ทรัพยากรปานกลาง | วัตถุประสงค์ทั่วไป |
| สูง (1024+) | การนำเสนอที่หลากหลาย | ช้าและใช้หน่วยความจำมาก | งานความหมายที่ซับซ้อน |
**ตัวอย่างที่ไม่ดี:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### ไม่จัดการโทเค็นพิเศษ
**สิ่งนี้คืออะไร:** ไม่สามารถจัดการ URL, รหัส, ตัวเลข และอักขระพิเศษได้อย่างถูกต้อง
**ตัวอย่างที่ไม่ดี:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**การบรรเทาผลกระทบ:**```python
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

## ปัญหาประสิทธิภาพการค้นหาเวกเตอร์
### ปัญหาการปรับขนาด
**สิ่งนี้คืออะไร:** คุณภาพการค้นหาหรือเวลาในการตอบสนองลดลงเมื่อชุดข้อมูลเพิ่มมากขึ้น
**อาการ:**
- เวลาแฝงเพิ่มขึ้นเชิงเส้นตามขนาดชุดข้อมูล
- เรียกคืนการหยดเมื่อมีการเพิ่มเวกเตอร์มากขึ้น
- การใช้หน่วยความจำระเบิด
**สถาปัตยกรรมที่ไม่ดี:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**โซลูชันที่ปรับขนาดได้:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### ปัญหาสตาร์ทเย็น
**สิ่งนี้คืออะไร:** เอกสารใหม่ไม่สามารถเรียกดูได้จนกว่าจะสร้างดัชนีใหม่
**ตัวอย่างที่ไม่ดี:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**แนวทางแก้ไข: การจัดทำดัชนีแบบเพิ่มหน่วย**```python
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

## ตัวชี้วัดการประเมินผลสำหรับ RAG
### ความแม่นยำของบริบท
วัดจำนวนชิ้นข้อมูลที่ดึงมาซึ่งมีความเกี่ยวข้องจริงๆ
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### คำตอบที่เกี่ยวข้อง
การวัดว่าคำตอบที่สร้างขึ้นตรงกับคำถามจริงหรือไม่
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

### ความซื่อสัตย์
มาตรการหากคำตอบมีเหตุผลในบริบทที่ดึงข้อมูลมา (ไม่ใช่ภาพหลอน)
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

## กรณีศึกษาในโลกแห่งความเป็นจริง
### กรณีศึกษา 1: Chatbot การสนับสนุนลูกค้า
**ปัญหา:** Chatbot ให้คำตอบที่ไม่ถูกต้องเกี่ยวกับฟีเจอร์ของผลิตภัณฑ์
**การวิเคราะห์สาเหตุที่แท้จริง:**
- การแยกคำอธิบายคุณสมบัติออกเป็นชิ้น ๆ ข้ามขอบเขต
- การสืบค้นข้อมูลพบเพียงบางส่วน
- LLM ภาพหลอนรายละเอียดที่ขาดหายไป
**วิธีแก้ปัญหา:**
- ใช้งานการแบ่งส่วนความหมายตามส่วนฟีเจอร์
- เพิ่มการทับซ้อนกัน 150 โทเค็นระหว่างชิ้นส่วน
- เพิ่ม top_k จาก 3 เป็น 5
- เพิ่มขั้นตอนการจัดอันดับใหม่
**ผลลัพธ์:**
- ความแม่นยำดีขึ้นจาก 62% เป็น 89%
- อัตราอาการประสาทหลอนลดลงจาก 23% เป็น 4%
- ความพึงพอใจของลูกค้าเพิ่มขึ้น 35%
### กรณีศึกษา 2: การค้นหาเอกสารทางกฎหมาย
**ปัญหา:** ทนายความไม่พบตัวอย่างที่เกี่ยวข้อง
**สาเหตุที่แท้จริง:**
- การฝังทั่วไปไม่ได้จับความหมายทางกฎหมาย
- การสอบถามการปฏิเสธล้มเหลว ("กรณีที่ไม่มีการกำหนดความรับผิด")
- ไม่มีการกรองชั่วคราวสำหรับคดีพลิกกลับ
**วิธีแก้ปัญหา:**
- การฝังที่ปรับแต่งอย่างละเอียดในคลังข้อมูลทางกฎหมาย
- ดำเนินการจัดการการปฏิเสธแล้ว
- เพิ่มข้อมูลเมตาสถานะเคสและการกรอง
- สร้างการดึงข้อมูลแบบ multi-hop สำหรับห่วงโซ่การอ้างอิง
**ผลลัพธ์:**
- Recall@10 เพิ่มขึ้นจาก 45% เป็น 78%
- เวลาในการค้นหาลดลงจาก 8 วินาทีเป็น 1.2 วินาที
- การรับเลี้ยงบุตรบุญธรรมโดยทีมกฎหมายเพิ่มขึ้น 3 เท่า
### กรณีศึกษา 3: เอกสารทางเทคนิค
**ปัญหา:** นักพัฒนาไม่พบตัวอย่างโค้ด
**สาเหตุที่แท้จริง:**
- บล็อกโค้ดที่ฝังไว้ไม่ดีกับโมเดลแบบข้อความเท่านั้น
- ข้อความค้นหาเช่น "วิธีการตรวจสอบสิทธิ์" ตรงกับทฤษฎี ไม่ใช่ตัวอย่าง
- ไม่มีความแตกต่างระหว่างเวอร์ชัน API
**วิธีแก้ปัญหา:**
- ใช้โมเดลการฝังโค้ดรับรู้
- แท็กชิ้นตามประเภทเนื้อหา (แนวคิด บทช่วยสอน การอ้างอิง API ตัวอย่าง)
- เพิ่มข้อมูลเมตาของเวอร์ชัน
- ดำเนินการจำแนกเจตนาสำหรับการกำหนดเส้นทางแบบสอบถาม
**ผลลัพธ์:**
- ความแม่นยำในการดึงตัวอย่างโค้ด: 34% → 82%
- เวลาในการสืบค้นที่สำเร็จครั้งแรกลดลง 60%
- ปริมาณการใช้เอกสารเพิ่มขึ้น 45%