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
# RAG 和矢量搜索失败
本文档整合了检索增强生成 (RAG) 系统、嵌入使用和矢量搜索实现中的常见故障。
---

## Bad RAG（检索增强生成）
检索增强生成 (RAG) 将检索系统与生成式 AI 相结合，以生成更准确且与上下文相关的响应。糟糕的 RAG 实现会受到检索质量差、上下文处理不足或生成问题的影响。
### 糟糕的分块策略
**错误的例子：**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**问题：**
- 句子和段落任意分割
- 上下文在块边界处丢失
- 语义碎片化
- 检索返回不完整的信息
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

### 缺少上下文重叠
**错误的例子：**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**更好的方法：**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### 忽略查询意图
**错误的例子：**```python
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

### 上下文窗口溢出
**错误的例子：**```python
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

## 错误的嵌入
嵌入是捕获语义的数据的向量表示。糟糕的嵌入是由于模型选择不当、训练不足或使用不当造成的。
### 域模型错误
**错误的例子：**```python
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

### 不标准化向量
**错误的例子：**```python
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
**错误的例子：**```python
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

## 错误的矢量搜索
向量搜索支持对高维嵌入进行语义相似性搜索。糟糕的实现会受到糟糕的索引配置、不适当的距离度量或可扩展性问题的影响。
### 错误的距离度量
**错误的例子：**```python
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

**为什么不好：**
- 欧氏距离受矢量幅度影响
- 对于归一化向量，余弦相似度（点积）是合适的
- 语义搜索的结果不太准确
**更好的方法：**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### 缺失索引优化
**错误的例子：**```python
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

### 不处理高维数据
**错误的例子：**```python
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

### 忽略召回率与延迟权衡
**错误的例子：**```python
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

## 最佳实践总结
### RAG 系统
1. **策略性分块**：尊重语义边界，添加重叠
2. **考虑查询意图**：根据用户想要的内容调整检索
3. **管理环境**：保持在 LLM 代币限制范围内
4. **评估端到端**：测试完整的 RAG 管道，而不仅仅是检索
### 嵌入
1. **选择适合领域的模型**：将模型与您的内容类型相匹配
2. **标准化向量**：对于余弦相似度至关重要
3. **一致性**：在整个系统中使用相同的模型
4. **监控漂移**：随着数据的发展重新训练或更新嵌入
### 矢量搜索
1. **选择右距离度量**：语义为 COSINE，空间为 EUCLID
2. **配置索引**：对大型数据集使用 HNSW
3. **调整参数**：针对您的用例平衡召回与延迟
4. **监控性能**：跟踪一段时间内的搜索质量和延迟
---

## 相关主题
- **AI/LLM 失败**：有关幻觉和推理问题，请参阅 `ai_llm_failures.md`
- **代理设计**：请参阅`../05_agents/agent_system_design.md`以了解使用 RAG 构建代理的信息
- **数据集质量**：有关训练数据注意事项，请参阅 `../08_machine_learning/ml_data_issues.md`
- **提示工程**：请参阅`../02_artificial_intelligence/prompt_engineering.md`了解上下文处理技术
---

## 高级 RAG 故障模式
### 迷失在中间现象中
**它是什么：** 法学硕士倾向于关注上下文开头和结尾的信息， 
忽略中间内容。
**错误的例子：**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**为什么不好：**
- 中间块中的关键信息可能会被忽略
- 模型对中间内容的注意力减少
- 在不相关的检索内容上浪费令牌
**减轻：**```python
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

### 多跳检索失败
**它是什么：** 无法检索需要多个连接部分的信息。
**错误的例子：**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**减轻：**```python
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

### 时间推理失败
**它是什么：** RAG 系统与时间敏感的查询和过时的信息作斗争。
**错误的例子：**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**减轻：**```python
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

### 否定处理失败
**它是什么：** 语义搜索经常会错过查询中的否定。
**错误的例子：**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**减轻：**```python
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
**它是什么：** 使用不同的模型进行索引与查询会破坏相似性。
**错误的例子：**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**为什么不好：**
- 不同的模型在不兼容的向量空间中产生嵌入
- 不同模型嵌入之间的余弦相似度是随机噪声
- 系统似乎工作但返回垃圾
**检测：**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### 忽略嵌入尺寸
**它是什么：** 不考虑嵌入维度对性能的影响。
**权衡：**
|尺寸|优点 |缺点 |使用案例|
|------------|------|------|----------|
|低 (128-256) |搜索速度快，占用内存少 |不那么细致的表述 |任务简单，规模大|
|中 (384-768) |良好的平衡性|中等资源|通用|
|高 (1024+) |丰富的表述 |速度慢，占用内存|复杂的语义任务 |
**错误的例子：**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### 不处理特殊令牌
**它是什么：** 无法正确处理 URL、代码、数字和特殊字符。
**错误的例子：**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**减轻：**```python
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

## 矢量搜索性能问题
### 扩展问题
**它是什么：** 搜索质量或延迟会随着数据集的增长而降低。
**症状：**
- 延迟随着数据集大小线性增加
- 随着更多向量的添加，召回率下降
- 内存使用量爆炸
**糟糕的架构：**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**可扩展的解决方案：**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### 冷启动问题
**它是什么：** 在重建索引之前，无法检索新文档。
**错误的例子：**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**解决方案：增量索引**```python
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

## RAG 的评估指标
### 上下文精度
测量有多少检索到的块实际上是相关的。
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### 答案相关性
测量生成的答案是否确实解决了查询。
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

### 忠诚
衡量答案是否基于检索到的上下文（不是幻觉）。
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

## 真实案例研究
### 案例研究 1：客户支持聊天机器人
**问题：** 聊天机器人给出了有关产品功能的错误答案。
**根本原因分析：**
- 跨边界分块分割特征描述
- 检索发现部分信息
- LLM幻觉缺失细节
**解决方案：**
- 通过特征部分实现语义分块
- 在块之间添加了 150 个令牌重叠
- 将 top_k 从 3 增加到 5
- 添加了重新排名步骤
**结果：**
- 准确度从 62% 提高到 89%
- 幻觉率从 23% 下降至 4%
- 客户满意度提高 35%
### 案例研究2：法律文件检索
**问题：**律师找不到相关先例。
**根本原因：**
- 通用嵌入没有捕获法律语义
- 否定查询失败（“责任未成立的情况”）
- 对于推翻的案件没有时间过滤
**解决方案：**
- 法律语料库上的微调嵌入
- 实施否定处理
- 添加了案例状态元数据和过滤
- 为引文链构建多跳检索
**结果：**
- Recall@10 从 45% 提高到 78%
- 搜索时间从 8 秒减少到 1.2 秒
- 法律团队的采用率增加了 3 倍
### 案例研究 3：技术文档
**问题：** 开发人员找不到代码示例。
**根本原因：**
- 代码块与纯文本模型的嵌入效果不佳
- 像“如何验证”这样的查询匹配理论，而不是示例
- API版本之间没有区别
**解决方案：**
- 使用代码感知嵌入模型
- 按内容类型标记的块（概念、教程、API 参考、示例）
- 添加了版本元数据
- 实现了查询路由的意图分类
**结果：**
- 代码示例检索准确率：34% → 82%
- 首次成功查询时间缩短 60%
- 文档流量增加 45%