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
# Lỗi tìm kiếm RAG và Vector
Tài liệu này tổng hợp các lỗi thường gặp trong các hệ thống Thế hệ tăng cường truy xuất (RAG), cách sử dụng tính năng nhúng và triển khai tìm kiếm vectơ.
---

## Bad RAG (Thế hệ tăng cường truy xuất)
Thế hệ tăng cường truy xuất (RAG) kết hợp các hệ thống truy xuất với AI tổng quát để tạo ra các phản hồi chính xác hơn và phù hợp với ngữ cảnh hơn. Việc triển khai RAG kém sẽ dẫn đến chất lượng truy xuất kém, xử lý ngữ cảnh không đầy đủ hoặc các vấn đề về tạo.
### Chiến lược phân đoạn kém
**Ví dụ tồi:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Vấn đề:**
- Câu, đoạn được chia tùy ý
- Bối cảnh bị mất ở ranh giới chunk
- Ý nghĩa ngữ nghĩa bị rời rạc
- Truy xuất trả về thông tin không đầy đủ
**Cách tiếp cận tốt hơn:**```python
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

### Thiếu bối cảnh chồng chéo
**Ví dụ tồi:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Cách tiếp cận tốt hơn:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Bỏ qua mục đích truy vấn
**Ví dụ tồi:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Cách tiếp cận tốt hơn:**```python
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

### Tràn cửa sổ ngữ cảnh
**Ví dụ tồi:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Cách tiếp cận tốt hơn:**```python
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

## Nhúng xấu
Phần nhúng là biểu diễn vectơ của dữ liệu nắm bắt ý nghĩa ngữ nghĩa. Khả năng nhúng kém là kết quả của việc lựa chọn mô hình kém, đào tạo không đầy đủ hoặc sử dụng không đúng cách.
### Mô hình sai cho tên miền
**Ví dụ tồi:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Cách tiếp cận tốt hơn:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Không chuẩn hóa vectơ
**Ví dụ tồi:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Cách tiếp cận tốt hơn:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Bỏ qua kích thước nhúng
**Ví dụ tồi:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Cách tiếp cận tốt hơn:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Tìm kiếm vectơ xấu
Tìm kiếm vectơ cho phép tìm kiếm sự tương đồng về ngữ nghĩa trên các phần nhúng có chiều cao. Việc triển khai không tốt sẽ dẫn đến cấu hình chỉ mục kém, số liệu khoảng cách không phù hợp hoặc các vấn đề về khả năng mở rộng.
### Số liệu khoảng cách sai
**Ví dụ tồi:**```python
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

**Tại sao nó xấu:**
- Khoảng cách Euclide bị ảnh hưởng bởi độ lớn của vectơ
- Đối với các vectơ đã chuẩn hóa, độ tương tự cosine (tích vô hướng) là phù hợp
- Kết quả sẽ kém chính xác hơn khi tìm kiếm theo ngữ nghĩa
**Cách tiếp cận tốt hơn:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Thiếu tối ưu hóa chỉ mục
**Ví dụ tồi:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Cách tiếp cận tốt hơn:**```python
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

### Không xử lý dữ liệu chiều cao
**Ví dụ tồi:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Cách tiếp cận tốt hơn:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Bỏ qua việc thu hồi và đánh đổi độ trễ
**Ví dụ tồi:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Cách tiếp cận tốt hơn:**```python
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

## Tóm tắt các phương pháp hay nhất
### Hệ thống RAG
1. **Chunk về mặt chiến lược**: Tôn trọng ranh giới ngữ nghĩa, thêm sự chồng chéo
2. **Xem xét Ý định truy vấn**: Truy xuất thích ứng dựa trên những gì người dùng muốn
3. **Quản lý bối cảnh**: Duy trì trong giới hạn mã thông báo LLM
4. **Đánh giá từ đầu đến cuối**: Kiểm tra toàn bộ đường dẫn RAG, không chỉ truy xuất
### Nhúng
1. **Chọn mô hình phù hợp với miền**: Ghép mô hình với loại nội dung của bạn
2. **Chuẩn hóa vectơ**: Cần thiết cho sự tương tự cosine
3. **Tính nhất quán**: Sử dụng cùng một mô hình trên toàn hệ thống của bạn
4. **Theo dõi độ trôi**: Đào tạo lại hoặc cập nhật các phần nhúng khi dữ liệu phát triển
### Tìm kiếm vectơ
1. **Chọn số liệu khoảng cách phù hợp**: COSINE cho ngữ nghĩa, EUCLID cho không gian
2. **Định cấu hình chỉ mục**: Sử dụng HNSW cho tập dữ liệu lớn
3. **Điều chỉnh thông số**: Cân bằng thu hồi so với độ trễ cho trường hợp sử dụng của bạn
4. **Theo dõi hiệu suất**: Theo dõi chất lượng tìm kiếm và độ trễ theo thời gian
---

## Chủ đề liên quan
- **Thất bại AI/LLM**: Xem`ai_llm_failures.md`để biết các vấn đề về ảo giác và lý luận
- **Thiết kế tác nhân**: Xem`../05_agents/agent_system_design.md`để biết các tác nhân xây dựng bằng RAG
- **Chất lượng tập dữ liệu**: Xem`../08_machine_learning/ml_data_issues.md`để biết các cân nhắc về dữ liệu đào tạo
- **Kỹ thuật nhắc nhở**: Xem`../02_artificial_intelligence/prompt_engineering.md`để biết kỹ thuật xử lý ngữ cảnh
---

## Các mẫu lỗi RAG nâng cao
###Hiện tượng Lạc giữa
**Nó là gì:** LLM có xu hướng tập trung vào thông tin ở đầu và cuối ngữ cảnh, 
bỏ qua nội dung ở giữa.
**Ví dụ tồi:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Tại sao nó xấu:**
- Thông tin quan trọng ở phần giữa có thể bị bỏ qua
- Sự chú ý của người mẫu giảm dần đối với nội dung ở giữa
- Lãng phí mã thông báo trên nội dung được truy xuất không liên quan
**Giảm thiểu:**```python
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

### Lỗi truy xuất nhiều bước nhảy
**Đó là gì:** Không truy xuất được thông tin yêu cầu nhiều phần được kết nối.
**Ví dụ tồi:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Giảm thiểu:**```python
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

### Thất bại về lý luận tạm thời
**Nó là gì:** Hệ thống RAG gặp khó khăn với các truy vấn nhạy cảm về thời gian và thông tin lỗi thời.
**Ví dụ tồi:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Giảm thiểu:**```python
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

### Lỗi xử lý phủ định
**Nó là gì:** Tìm kiếm ngữ nghĩa thường bỏ sót những phủ định trong truy vấn.
**Ví dụ tồi:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Giảm thiểu:**```python
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

## Nhúng Anti-Pattern
### Trộn các mô hình nhúng
**Nó là gì:** Việc sử dụng các mô hình khác nhau để lập chỉ mục và truy vấn sẽ phá vỡ sự giống nhau.
**Ví dụ tồi:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Tại sao nó xấu:**
- Các mô hình khác nhau tạo ra các phần nhúng trong không gian vectơ không tương thích
- Độ tương tự cosine giữa các mô hình nhúng khác nhau là nhiễu ngẫu nhiên
- Hệ thống có vẻ hoạt động nhưng lại trả về rác
**Phát hiện:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Bỏ qua kích thước nhúng
**Nó là gì:** Không xem xét tác động của việc nhúng thứ nguyên đến hiệu suất.
**Đánh đổi:**
| Kích thước | Ưu điểm | Nhược điểm | Trường hợp sử dụng |
|----------||------|------|----------|
| Thấp (128-256) | Tìm kiếm nhanh, ít bộ nhớ | Đại diện ít sắc thái hơn | Nhiệm vụ đơn giản, quy mô lớn |
| Trung bình (384-768) | Cân bằng tốt | Tài nguyên vừa phải | Mục đích chung |
| Cao (1024+) | Đại diện phong phú | Chậm, tốn nhiều bộ nhớ | Nhiệm vụ ngữ nghĩa phức tạp |
**Ví dụ tồi:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Không xử lý mã thông báo đặc biệt
**Đó là gì:** Không xử lý đúng cách các URL, mã, số và ký tự đặc biệt.
**Ví dụ tồi:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Giảm thiểu:**```python
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

## Vấn đề về hiệu suất tìm kiếm vectơ
### Vấn đề về tỷ lệ
**Nó là gì:** Chất lượng tìm kiếm hoặc độ trễ giảm khi tập dữ liệu tăng lên.
**Triệu chứng:**
- Độ trễ tăng tuyến tính với kích thước tập dữ liệu
- Thu hồi giảm khi có nhiều vectơ được thêm vào
- Việc sử dụng bộ nhớ bùng nổ
**Kiến trúc tồi:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Giải pháp có thể mở rộng:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Vấn đề khởi động nguội
**Nó là gì:** Không thể truy xuất được tài liệu mới cho đến khi chỉ mục được xây dựng lại.
**Ví dụ tồi:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Giải pháp: Lập chỉ mục gia tăng**```python
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

## Số liệu đánh giá cho RAG
### Độ chính xác của bối cảnh
Đo xem có bao nhiêu khối được truy xuất thực sự có liên quan.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Câu trả lời có liên quan
Đo lường xem câu trả lời được tạo có thực sự giải quyết được truy vấn hay không.
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

###Sự trung thành
Đo lường xem câu trả lời có căn cứ trong bối cảnh được truy xuất hay không (không gây ảo giác).
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

## Nghiên cứu điển hình trong thế giới thực
### Case Study 1: Chatbot hỗ trợ khách hàng
**Vấn đề:** Chatbot đưa ra câu trả lời không chính xác về tính năng của sản phẩm.
**Phân tích nguyên nhân gốc rễ:**
- Phân chia các mô tả tính năng theo ranh giới
- Truy xuất tìm thấy một phần thông tin
- LLM ảo giác thiếu chi tiết
**Giải pháp:**
- Thực hiện phân đoạn ngữ nghĩa theo các phần tính năng
- Đã thêm chồng chéo 150 mã thông báo giữa các khối
- Tăng top_k từ 3 lên 5
- Đã thêm bước xếp hạng lại
**Kết quả:**
- Độ chính xác được cải thiện từ 62% lên 89%
- Tỷ lệ ảo giác giảm từ 23% xuống 4%
- Sự hài lòng của khách hàng tăng 35%
### Case Study 2: Tìm kiếm văn bản pháp luật
**Vấn đề:** Luật sư không tìm được tiền lệ liên quan.
**Nguyên nhân cốt lõi:**
- Các phần nhúng chung không nắm bắt được ngữ nghĩa pháp lý
- Truy vấn phủ định không thành công ("trường hợp trách nhiệm pháp lý KHÔNG được thiết lập")
- Không lọc tạm thời cho các trường hợp bị lật ngược
**Giải pháp:**
- Các phần nhúng được tinh chỉnh trên kho văn bản pháp luật
- Thực hiện xử lý phủ định
- Đã thêm siêu dữ liệu và lọc trạng thái trường hợp
- Xây dựng tính năng truy xuất nhiều bước cho chuỗi trích dẫn
**Kết quả:**
- Recall@10 cải thiện từ 45% lên 78%
- Thời gian tìm kiếm giảm từ 8 giây xuống 1,2 giây
- Sự chấp nhận của nhóm pháp lý tăng gấp 3 lần
### Case Study 3: Tài liệu kỹ thuật
**Vấn đề:** Nhà phát triển không thể tìm thấy mã ví dụ.
**Nguyên nhân cốt lõi:**
- Khối mã được nhúng kém với các mô hình chỉ có văn bản
- Các truy vấn như lý thuyết phù hợp "làm thế nào để xác thực", không phải ví dụ
- Không có sự phân biệt giữa các phiên bản API
**Giải pháp:**
- Mô hình nhúng nhận biết mã được sử dụng
- Các phần được gắn thẻ theo loại nội dung (khái niệm, hướng dẫn, tham chiếu API, ví dụ)
- Đã thêm siêu dữ liệu phiên bản
- Thực hiện phân loại mục đích để định tuyến truy vấn
**Kết quả:**
- Độ chính xác khi truy xuất mã ví dụ: 34% → 82%
- Thời gian truy vấn thành công đầu tiên giảm 60%
- Lưu lượng tài liệu tăng 45%