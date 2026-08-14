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
# RAG 및 벡터 검색 실패
이 문서는 RAG(Retrieval-Augmented Generation) 시스템, 임베딩 사용 및 벡터 검색 구현의 일반적인 오류를 통합합니다.
---

## Bad RAG(검색 증강 생성)
검색 증강 생성(RAG)은 검색 시스템과 생성 AI를 결합하여 보다 정확하고 상황에 맞는 응답을 생성합니다. 잘못된 RAG 구현은 낮은 검색 품질, 부적절한 컨텍스트 처리 또는 생성 문제로 인해 어려움을 겪습니다.
### 빈약한 청킹 전략
**나쁜 예:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**문제:**
- 문장과 단락이 임의로 분할됩니다.
- 청크 경계에서 컨텍스트가 손실됩니다.
- 의미론적 의미가 단편화되어 있음
- 검색 결과 불완전한 정보가 반환됩니다.
**더 나은 접근 방식:**```python
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

### 컨텍스트 중복 누락
**나쁜 예:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**더 나은 접근 방식:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### 쿼리 의도 무시
**나쁜 예:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**더 나은 접근 방식:**```python
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

### 컨텍스트 창 오버플로
**나쁜 예:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**더 나은 접근 방식:**```python
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

## 잘못된 임베딩
임베딩은 의미론적 의미를 포착하는 데이터의 벡터 표현입니다. 잘못된 임베딩은 잘못된 모델 선택, 부적절한 교육 또는 부적절한 사용으로 인해 발생합니다.
### 도메인 모델이 잘못되었습니다.
**나쁜 예:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**더 나은 접근 방식:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### 벡터를 정규화하지 않음
**나쁜 예:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**더 나은 접근 방식:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### 임베딩 차원 무시
**나쁜 예:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**더 나은 접근 방식:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## 잘못된 벡터 검색
벡터 검색을 사용하면 고차원 임베딩에 대한 의미론적 유사성 검색이 가능합니다. 잘못된 구현은 잘못된 인덱스 구성, 부적절한 거리 측정 또는 확장성 문제로 인해 어려움을 겪습니다.
### 잘못된 거리 측정법
**나쁜 예:**```python
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

**나쁜 이유:**
- 유클리드 거리는 벡터 크기의 영향을 받습니다.
- 정규화된 벡터의 경우 코사인 유사성(내적)이 적합합니다.
- 의미 검색의 경우 결과의 정확성이 떨어집니다.
**더 나은 접근 방식:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### 누락된 인덱스 최적화
**나쁜 예:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**더 나은 접근 방식:**```python
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

### 고차원 데이터를 처리하지 않음
**나쁜 예:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**더 나은 접근 방식:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### 재현율과 지연 시간 트레이드오프 무시
**나쁜 예:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**더 나은 접근 방식:**```python
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

## 모범 사례 요약
### RAG 시스템
1. **전략적으로 청크**: 의미적 경계를 존중하고 중복을 추가합니다.
2. **쿼리 의도 고려**: 사용자가 원하는 것을 기반으로 검색을 조정합니다.
3. **컨텍스트 관리**: LLM 토큰 한도 내에서 유지
4. **엔드 투 엔드 평가**: 검색뿐 아니라 전체 RAG 파이프라인 테스트
### 임베딩
1. **도메인에 적합한 모델 선택**: 콘텐츠 유형에 모델을 일치시킵니다.
2. **벡터 정규화**: 코사인 유사성에 필수
3. **일관성**: 시스템 전체에서 동일한 모델을 사용하십시오.
4. **드리프트 모니터링**: 데이터가 발전함에 따라 임베딩을 다시 학습하거나 업데이트합니다.
### 벡터 검색
1. **적절한 거리 측정법 선택**: 의미론의 경우 COSINE, 공간의 경우 EUCLID
2. **인덱스 구성**: 대규모 데이터세트에는 HNSW를 사용하세요.
3. **매개변수 조정**: 사용 사례에 맞게 재현율과 지연 시간의 균형을 맞춥니다.
4. **성능 모니터링**: 시간 경과에 따른 검색 품질 및 대기 시간 추적
---

## 관련 주제
- **AI/LLM 오류**: 환각 및 추론 문제는 `ai_llm_failures.md`를 참조하세요.
- **에이전트 설계**: RAG를 사용하여 에이전트를 구축하려면 `../05_agents/agent_system_design.md`를 참조하세요.
- **데이터 세트 품질**: 학습 데이터 고려 사항은 `../08_machine_learning/ml_data_issues.md`를 참조하세요.
- **신속한 엔지니어링**: 컨텍스트 처리 기술은 `../02_artificial_intelligence/prompt_engineering.md`를 참조하세요.
---

## 고급 RAG 실패 패턴
### 중간 현상에서 길을 잃다
**정의:** LLM은 맥락의 시작과 끝 부분에 있는 정보에 초점을 맞추는 경향이 있습니다. 
중간 내용을 무시합니다.
**나쁜 예:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**나쁜 이유:**
- 중간 청크의 중요한 정보는 간과될 수 있음
- 중간 콘텐츠에 대한 모델 주의력이 감소합니다.
- 검색된 관련 없는 콘텐츠에 토큰을 낭비합니다.
**완화:**```python
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

### 멀티홉 검색 실패
**정의:** 여러 개의 연결된 부분이 필요한 정보를 검색하지 못했습니다.
**나쁜 예:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**완화:**```python
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

### 시간적 추론 실패
**정의:** RAG 시스템은 시간에 민감한 쿼리와 오래된 정보로 인해 어려움을 겪고 있습니다.
**나쁜 예:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**완화:**```python
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

### 부정 처리 실패
**정의:** 의미론적 검색은 쿼리에서 부정을 놓치는 경우가 많습니다.
**나쁜 예:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**완화:**```python
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

## 안티 패턴 삽입
### 임베딩 모델 혼합
**정의:** 색인 생성과 쿼리에 서로 다른 모델을 사용하면 유사성이 깨집니다.
**나쁜 예:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**나쁜 이유:**
- 다양한 모델이 호환되지 않는 벡터 공간에 임베딩을 생성합니다.
- 서로 다른 모델 임베딩 간의 코사인 유사성은 랜덤 노이즈입니다.
- 시스템이 작동하는 것처럼 보이지만 쓰레기를 반환합니다.
**발각:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### 임베딩 차원 무시
**정의:** 차원 삽입이 성능에 미치는 영향을 고려하지 않음.
**장점:**
| 치수 | 장점 | 단점 | 사용 사례 |
|------------|------|------|----------|
| 낮음(128-256) | 빠른 검색, 적은 메모리 | 덜 미묘한 표현 | 간단한 작업, 대규모 |
| 중형(384-768) | 좋은 균형 | 보통 자원 | 범용 |
| 높음(1024+) | 풍부한 표현 | 느리고 메모리 집약적 | 복잡한 의미 작업 |
**나쁜 예:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### 특수 토큰을 처리하지 않음
**정의:** URL, 코드, 숫자, 특수 문자를 제대로 처리하지 못하는 문제입니다.
**나쁜 예:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**완화:**```python
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

## 벡터 검색 성능 문제
### 확장 문제
**정의:** 데이터 세트가 늘어남에 따라 검색 품질이나 대기 시간이 저하됩니다.
**증상:**
- 데이터 세트 크기에 따라 지연 시간이 선형적으로 증가합니다.
- 더 많은 벡터가 추가됨에 따라 리콜 드롭이 발생합니다.
- 메모리 사용량이 폭발적으로 증가합니다.
**나쁜 아키텍처:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**확장 가능한 솔루션:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### 콜드 스타트 ​​문제
**정의:** 인덱스가 다시 작성될 때까지 새 문서를 검색할 수 없습니다.
**나쁜 예:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**해결책: 증분 인덱싱**```python
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

## RAG 평가 지표
### 컨텍스트 정밀도
검색된 청크 중 실제로 관련된 청크의 수를 측정합니다.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### 답변 관련성
생성된 답변이 실제로 쿼리를 해결하는지 측정합니다.
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

### 충실함
답변이 검색된 맥락(환각이 아닌)에 근거하는지 여부를 측정합니다.
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

## 실제 사례 연구
### 사례 연구 1: 고객 지원 챗봇
**문제:** 챗봇이 제품 기능에 대해 잘못된 답변을 했습니다.
**근본 원인 분석:**
- 경계를 넘나드는 청킹 분할 기능 설명
- 발견된 부분정보 검색
- LLM은 누락된 세부 사항을 환각으로 느꼈습니다.
**해결책:**
- 기능 섹션별 의미적 청킹 구현
- 청크 사이에 150개 토큰 중복이 추가되었습니다.
- top_k를 3에서 5로 늘렸습니다.
- 재순위 단계 추가
**결과:**
- 정확도가 62%에서 89%로 향상되었습니다.
- 환각률이 23%에서 4%로 감소했습니다.
- 고객 만족도 35% 증가
### 사례 연구 2: 법률 문서 검색
**문제:** 변호사들은 관련 판례를 찾을 수 없었습니다.
**근본 원인:**
- 일반 임베딩이 법적 의미를 포착하지 못했습니다.
- 부정 쿼리 실패("책임이 확립되지 않은 경우")
- 번복된 사건에 대해서는 시간적 필터링이 없습니다.
**해결책:**
- 법률 자료에 대한 미세 조정된 임베딩
- 부정 처리 구현
- 케이스 상태 메타데이터 및 필터링이 추가되었습니다.
- 인용 체인을 위한 다중 홉 검색 구축
**결과:**
- Recall@10이 45%에서 78%로 향상되었습니다.
- 검색 시간이 8초에서 1.2초로 단축되었습니다.
- 법무팀 채택률 3배 증가
### 사례 연구 3: 기술 문서
**문제:** 개발자가 코드 예제를 찾을 수 없습니다.
**근본 원인:**
- 텍스트 전용 모델에 제대로 포함되지 않은 코드 블록
- "인증 방법"과 같은 쿼리는 예시가 아닌 이론과 일치합니다.
- API 버전 간 구분이 없습니다.
**해결책:**
- 코드 인식 임베딩 모델 사용
- 콘텐츠 유형(개념, 튜토리얼, API 참조, 예제)별로 태그된 청크
- 버전 메타데이터 추가
- 쿼리 라우팅을 위한 의도 분류 구현
**결과:**
- 코드 예시 검색 정확도: 34% → 82%
- 첫 번째 쿼리 성공 시간 60% 감소
- 문서 트래픽 45% 증가