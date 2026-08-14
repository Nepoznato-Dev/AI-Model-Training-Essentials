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
# RAG 和向量搜尋失敗
本文檔整合了檢索增強生成 (RAG) 系統、嵌入使用和向量搜尋實作中的常見故障。
---

## Bad RAG（檢索增強生成）
檢索增強生成 (RAG) 將檢索系統與生成式 AI 結合，以產生更準確且與情境相關的回應。糟糕的 RAG 實作會受到檢索品質差、上下文處理不足或產生問題的影響。
### 糟糕的分塊策略
**錯誤的例子：**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**問題：**
- 句子和段落任意分割
- 上下文在區塊邊界處遺失
- 語意碎片化
- 檢索傳回不完整的訊息
**更好的方法：**```python
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

### 缺少上下文重疊
**錯誤的例子：**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**更好的方法：**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### 忽略查詢意圖
**錯誤的例子：**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**更好的方法：**```python
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

### 上下文視窗溢出
**錯誤的例子：**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**更好的方法：**```python
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

## 錯誤的嵌入
嵌入是捕獲語義的資料的向量表示。糟糕的嵌入是由於模型選擇不當、訓練不足或使用不當造成的。
### 域模型錯誤
**錯誤的例子：**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**更好的方法：**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### 不標準化向量
**錯誤的例子：**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**更好的方法：**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### 忽略嵌入尺寸
**錯誤的例子：**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**更好的方法：**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## 錯誤的向量搜尋
向量搜尋支援對高維嵌入進行語義相似性搜尋。糟糕的實作會受到糟糕的索引配置、不適當的距離測量或可擴展性問題的影響。
### 錯誤的距離測量
**錯誤的例子：**```python
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

**為什麼不好：**
- 歐氏距離受向量幅度影響
- 對於歸一化向量，餘弦相似度（點積）是適當的
- 語意搜尋的結果較不準確
**更好的方法：**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### 缺失索引優化
**錯誤的例子：**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**更好的方法：**```python
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

### 不處理高維度數據
**錯誤的例子：**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**更好的方法：**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### 忽略召回率與延遲權衡
**錯誤的例子：**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**更好的方法：**```python
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

## 最佳實務總結
### RAG 系統
1. **策略性分塊**：尊重語意邊界，增加重疊
2. **考慮查詢意圖**：根據使用者想要的內容調整檢索
3. **管理環境**：保持在 LLM 代幣限制範圍內
4. **評估端對端**：測試完整的 RAG 管道，而不僅僅是檢索
### 嵌入
1. **選擇適合領域的模型**：將模型與您的內容類型相匹配
2. **標準化向量**：對於餘弦相似度至關重要
3. **一致性**：在整個系統中使用相同的模型
4. **監控漂移**：隨著資料的發展重新訓練或更新嵌入
### 向量搜尋
1. **選擇右距離度量**：語意為 COSINE，空間為 EUCLID
2. **配置索引**：對大型資料集使用 HNSW
3. **調整參數**：針對您的用例平衡召回與延遲
4. **監控效能**：追蹤一段時間內的搜尋品質和延遲
---

## 相關主題
- **AI/LLM 失敗**：有關幻覺和推理問題，請參閱 `ai_llm_failures.md`
- **代理設計**：請參閱`../05_agents/agent_system_design.md`以了解使用 RAG 建置代理程式的信息
- **資料集品質**：有關訓練資料注意事項，請參閱 `../08_machine_learning/ml_data_issues.md`
- **提示工程**：請參閱`../02_artificial_intelligence/prompt_engineering.md`以了解情境處理技術
---

## 進階 RAG 故障模式
### 迷失在中間現像中
**它是什麼：** 法學碩士傾向於關注上下文開頭和結尾的信息，
忽略中間內容。
**錯誤的例子：**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**為什麼不好：**
- 中間區塊中的關鍵資訊可能會被忽略
- 模型對中間內容的注意力減少
- 在不相關的檢索內容上浪費令牌
**減輕：**```python
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

### 多跳檢索失敗
**它是什麼：** 無法檢索需要多個連接部分的資訊。
**錯誤的例子：**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**減輕：**```python
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

### 時間推理失敗
**它是什麼：** RAG 系統與時間敏感的查詢和過時的資訊作鬥爭。
**錯誤的例子：**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**減輕：**```python
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

### 否定處理失敗
**它是什麼：** 語意搜尋經常會錯過查詢中的否定。
**錯誤的例子：**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**減輕：**```python
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

## 嵌入反模式
### 混合嵌入模型
**它是什麼：** 使用不同的模型進行索引與查詢會破壞相似性。
**錯誤的例子：**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**為什麼不好：**
- 不同的模型在不相容的向量空間中產生嵌入
- 不同模型嵌入之間的餘弦相似度是隨機噪音
- 系統似乎工作但返回垃圾
**檢測：**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### 忽略嵌入尺寸
**它是什麼：** 不考慮嵌入維度對效能的影響。
**權衡：**
|尺寸|優點 |缺點 |使用案例|
|------------|------|------|----------|
|低 (128-256) |搜尋速度快，佔用記憶體少 |較不細緻的陳述 |任務簡單，規模大|
|中 (384-768) |良好的平衡性|中等資源|通用|
|高 (1024+) |豐富的表述 |速度慢，佔用記憶體|複雜的語意任務 |
**錯誤的例子：**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### 不處理特殊令牌
**它是什麼：** 無法正確處理 URL、程式碼、數字和特殊字元。
**錯誤的例子：**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**減輕：**```python
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

## 向量搜尋效能問題
### 擴充問題
**它是什麼：** 搜尋品質或延遲會隨著資料集的增長而降低。
**症狀：**
- 延遲隨著資料集大小線性增加
- 隨著更多向量的添加，召回率下降
- 記憶體使用量爆炸
**糟糕的架構：**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**可擴展的解決方案：**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### 冷啟動問題
**它是什麼：** 在重建索引之前，無法檢索新文件。
**錯誤的例子：**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**解決方案：增量索引**```python
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

## RAG 的評估指標
### 上下文精度
測量有多少檢索到的區塊實際上是相關的。
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### 答案相關性
測量產生的答案是否確實解決了查詢。
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

### 忠誠
衡量答案是否基於檢索到的上下文（不是幻覺）。
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

## 真實案例研究
### 案例研究 1：客戶支援聊天機器人
**問題：** 聊天機器人給了有關產品功能的錯誤答案。
**根本原因分析：**
- 跨邊界分塊分割特徵描述
- 檢索發現部分訊息
- LLM幻覺缺失細節
**解決方案：**
- 透過特徵部分實現語意分塊
- 在區塊之間新增了 150 個令牌重疊
- 將 top_k 從 3 增加到 5
- 新增了重新排名步驟
**結果：**
- 準確度從 62% 提高到 89%
- 幻覺率從 23% 下降至 4%
- 顧客滿意度提高 35%
### 案例研究2：法律文件檢索
**問題：**律師找不到相關先例。
**根本原因：**
- 通用嵌入沒有捕獲法律語義
- 否定查詢失敗（「責任未成立的情況」）
- 對於推翻的案件沒有時間過濾
**解決方案：**
- 法律語料庫上的微調嵌入
- 實施否定處理
- 新增了案例狀態元資料和過濾
- 為引文鏈建立多跳檢索
**結果：**
- Recall@10 從 45% 提高到 78%
- 搜尋時間從 8 秒減少到 1.2 秒
- 法律團隊的採用率增加了 3 倍
### 案例研究 3：技術文檔
**問題：** 開發人員找不到程式碼範例。
**根本原因：**
- 程式碼區塊與純文字模型的嵌入效果不佳
- 像“如何驗證”這樣的查詢匹配理論，而不是示例
- API版本之間沒有區別
**解決方案：**
- 使用程式碼感知嵌入模型
- 按內容類型標記的區塊（概念、教學課程、API 參考、範例）
- 新增了版本元數據
- 實現了查詢路由的意圖分類
**結果：**
- 程式碼範例擷取準確率：34% → 82%
- 首次成功查詢時間縮短 60%
- 文件流量增加 45%