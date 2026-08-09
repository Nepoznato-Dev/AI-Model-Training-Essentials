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

# RAG およびベクター検索の失敗
この文書には、検索拡張生成 (RAG) システム、埋め込みの使用、およびベクトル検索の実装における一般的な障害がまとめられています。
---

## Bad RAG (検索拡張生成)
検索拡張生成 (RAG) は、検索システムと生成 AI を組み合わせて、より正確で状況に応じた適切な応答を生成します。不適切な RAG 実装では、取得品質の低下、不適切なコンテキスト処理、または生成の問題が発生します。
### 不十分なチャンク戦略
**悪い例:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**問題:**
- 文と段落は任意に分割されます
- チャンク境界でコンテキストが失われる
- 意味上の意味が断片化されている
- 検索により不完全な情報が返される
**より良いアプローチ:**```python
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

### コンテキストの重複が欠落しています
**悪い例:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**より良いアプローチ:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### クエリの意図を無視する
**悪い例:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**より良いアプローチ:**```python
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

### コンテキストウィンドウのオーバーフロー
**悪い例:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**より良いアプローチ:**```python
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

## 不正な埋め込み
埋め込みは、意味論的な意味を捉えるデータのベクトル表現です。不適切な埋め込みは、不適切なモデルの選択、不適切なトレーニング、または不適切な使用によって発生します。
### ドメインの間違ったモデル
**悪い例:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**より良いアプローチ:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### ベクトルを正規化しない
**悪い例:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**より良いアプローチ:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### 埋め込み次元の無視
**悪い例:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**より良いアプローチ:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## 不良ベクトル検索
ベクトル検索により、高次元の埋め込みに対する意味的類似性検索が可能になります。不適切な実装では、不適切なインデックス構成、不適切な距離メトリック、またはスケーラビリティの問題が発生します。
### 間違った距離メトリック
**悪い例:**```python
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

**なぜ悪いのか:**
- ユークリッド距離はベクトルの大きさに影響されます
- 正規化されたベクトルの場合、コサイン類似度 (ドット積) が適切です
- セマンティック検索では結果の精度が低くなります
**より良いアプローチ:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### 欠落しているインデックスの最適化
**悪い例:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**より良いアプローチ:**```python
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

### 高次元データを処理しない
**悪い例:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**より良いアプローチ:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### リコールとレイテンシーのトレードオフを無視する
**悪い例:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**より良いアプローチ:**```python
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

## ベスト プラクティスの概要
### RAG システム
1. **戦略的にチャンク**: 意味上の境界を尊重し、重複を追加します
2. **クエリの意図を考慮する**: ユーザーの要望に基づいて取得を調整します。
3. **コンテキストの管理**: LLM トークンの制限内に留まります
4. **エンドツーエンドの評価**: 取得だけでなく、RAG パイプライン全体をテストします
### 埋め込み
1. **ドメインに適したモデルを選択**: モデルをコンテンツ タイプに一致させます
2. **ベクトルの正規化**: コサイン類似性に必須
3. **一貫性**: システム全体で同じモデルを使用します。
4. **ドリフトの監視**: データの進化に応じて埋め込みを再トレーニングまたは更新します
### ベクトル検索
1. **適切な距離メトリックを選択**: セマンティックの場合は COSINE、空間の場合は EUCLID
2. **インデックスの構成**: 大規模なデータセットには HNSW を使用します
3. **パラメーターの調整**: ユースケースに合わせてリコールとレイテンシのバランスをとります
4. **パフォーマンスを監視**: 検索の品質と遅延を経時的に追跡します
---

## 関連トピック
- **AI/LLM の障害**: 幻覚と推論の問題については、`ai_llm_failures.md` を参照してください。
- **エージェント設計**: RAG を使用したエージェントの構築については、`../05_agents/agent_system_design.md` を参照してください。
- **データセットの品質**: トレーニング データの考慮事項については、`../08_machine_learning/ml_data_issues.md` を参照してください。
- **プロンプト エンジニアリング**: コンテキスト処理技術については、`../02_artificial_intelligence/prompt_engineering.md` を参照してください。
---

## 高度な RAG 障害パターン
### 中間喪失現象
**概要:** LLM はコンテキストの最初と最後の情報に焦点を当てる傾向があります。 
中間の内容は無視します。
**悪い例:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**なぜ悪いのか:**
- 中間チャンクの重要な情報が見落とされる可能性がある
- 中間コンテンツに対するモデルの注意力が低下する
- 取得した無関係なコンテンツにトークンを浪費する
**緩和：**```python
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

### マルチホップ取得の失敗
**内容:** 複数の接続された部分を必要とする情報の取得に失敗します。
**悪い例:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**緩和：**```python
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

### 時間的推論の失敗
**概要:** RAG システムは、時間に敏感なクエリや古い情報に対処するのに苦労しています。
**悪い例:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**緩和：**```python
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

### 否定処理の失敗
**概要:** セマンティック検索では、クエリ内の否定が見逃されることがよくあります。
**悪い例:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**緩和：**```python
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

## アンチパターンの埋め込み
### 埋め込みモデルの混合
**概要:** インデックス作成とクエリ作成に異なるモデルを使用すると、類似性が失われます。
**悪い例:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**なぜ悪いのか:**
- モデルが異なると、互換性のないベクトル空間で埋め込みが生成される
- 異なるモデルの埋め込み間のコサイン類似性はランダム ノイズです
- システムは動作しているように見えますが、ガベージが返されます
**検出：**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### 埋め込み次元の無視
**概要:** 埋め込みディメンションがパフォーマンスに与える影響は考慮されていません。
**トレードオフ:**
|寸法 |長所 |短所 |使用例 |
|-----------|------|------|----------|
|低 (128-256) |高速検索、メモリ削減 |微妙な表現 |単純なタスク、大規模なタスク |
|中 (384-768) |バランスが良い |適度なリソース |汎用 |
|高 (1024+) |豊富な表現 |遅い、メモリを大量に消費する |複雑なセマンティックタスク |
**悪い例:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### 特別なトークンを処理しない
**概要:** URL、コード、数字、特殊文字を適切に処理できません。
**悪い例:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**緩和：**```python
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

## ベクトル検索のパフォーマンスの問題
### スケーリングの問題
**概要:** データセットが大きくなるにつれて、検索の品質または遅延が低下します。
**症状:**
- レイテンシーはデータセットのサイズに応じて直線的に増加します
- ベクトルを追加するとリコールが低下する
- メモリ使用量が爆発的に増加する
**悪いアーキテクチャ:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**スケーラブルなソリューション:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### コールドスタートの問題
**概要:** インデックスが再構築されるまで、新しいドキュメントは取得できません。
**悪い例:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**解決策: 増分インデックス作成**```python
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

## RAG の評価メトリクス
### コンテキストの精度
取得された実際に関連するチャンクの数を測定します。
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### 回答の関連性
生成された回答が実際にクエリに対応しているかどうかを測定します。
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

### 忠実さ
回答が取得されたコンテキストに基づいているかどうかを測定します (幻覚ではない)。
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

## 実際のケーススタディ
### ケーススタディ 1: カスタマー サポート チャットボット
**問題:** チャットボットが製品の機能に関して誤った回答をしました。
**根本原因の分析:**
- 境界を越えて分割されたフィーチャの説明をチャンク化する
- 検索で見つかった部分情報
- LLM は細部が欠けている幻覚を見せた
**解決策:**
- 機能セクションごとにセマンティックチャンクを実装
- チャンク間に 150 トークンのオーバーラップを追加
- top_k を 3 から 5 に増加しました
- 再ランキングステップを追加
**結果:**
- 精度が 62% から 89% に向上しました
- 幻覚率が 23% から 4% に低下しました。
- 顧客満足度が 35% 向上
### ケーススタディ 2: 法的文書の検索
**問題:** 弁護士は関連する先例を見つけることができませんでした。
**根本原因:**
- 汎用埋め込みが法的セマンティクスをキャプチャしていなかった
- 否定クエリが失敗した (「責任が確立されなかったケース」)
- 覆されたケースに対する一時的なフィルタリングはありません
**解決策:**
- 法的コーパスへの微調整された埋め込み
- 否定処理を実装しました
- ケースステータスのメタデータとフィルタリングを追加しました
- 引用チェーンのマルチホップ検索を構築
**結果:**
- Recall@10 が 45% から 78% に改善されました
- 検索時間が 8 秒から 1.2 秒に短縮されました
- 法務チームによる採用が 3 倍に増加
### ケーススタディ 3: 技術文書
**問題:** 開発者はコード例を見つけることができませんでした。
**根本原因:**
- テキストのみのモデルでコード ブロックが適切に埋め込まれていない
- 「認証方法」のようなクエリは例ではなく理論と一致しました
- API バージョンの区別なし
**解決策:**
- コード認識埋め込みモデルを使用
- コンテンツ タイプごとにタグ付けされたチャンク (コンセプト、チュートリアル、API リファレンス、例)
- バージョンメタデータを追加しました
- クエリルーティングのインテント分類を実装しました
**結果:**
- コード例の検索精度: 34% → 82%
- 最初にクエリが成功するまでの時間が 60% 短縮されました
- ドキュメントのトラフィックが 45% 増加