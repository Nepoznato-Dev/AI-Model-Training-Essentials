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
# RAG ve Vektör Arama Hataları
Bu belge, Almayla Artırılmış Üretim (RAG) sistemleri, yerleştirme kullanımı ve vektör arama uygulamalarındaki yaygın hataları birleştirir.
---

## Kötü RAG (Geri Alma-Artırılmış Nesil)
Almayla Artırılmış Üretim (RAG), daha doğru ve bağlamsal olarak alakalı yanıtlar üretmek için alma sistemlerini üretken yapay zekayla birleştirir. Kötü RAG uygulamaları, zayıf alma kalitesinden, yetersiz içerik işlemeden veya oluşturma sorunlarından muzdariptir.
### Kötü Parçalama Stratejisi
**Kötü Örnek:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Sorunlar:**
- Cümleler ve paragraflar keyfi olarak bölünmüştür
- Parça sınırlarında bağlam kayboluyor
- Anlamsal anlam parçalanmıştır
- Alma işlemi eksik bilgi döndürür
**Daha İyi Yaklaşım:**```python
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

### Eksik Bağlam Örtüşmesi
**Kötü Örnek:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Daha İyi Yaklaşım:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Sorgu Amacının Göz Ardı Edilmesi
**Kötü Örnek:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Daha İyi Yaklaşım:**```python
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

### Bağlam Penceresi Taşması
**Kötü Örnek:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Daha İyi Yaklaşım:**```python
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

## Kötü Yerleştirmeler
Gömmeler, verilerin anlamsal anlamı yakalayan vektör temsilleridir. Kötü yerleştirmeler, zayıf model seçiminden, yetersiz eğitimden veya uygunsuz kullanımdan kaynaklanır.
### Etki Alanı İçin Yanlış Model
**Kötü Örnek:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Daha İyi Yaklaşım:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Vektörler Normalleştirilmiyor
**Kötü Örnek:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Daha İyi Yaklaşım:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Gömme Boyutlarını Yoksayma
**Kötü Örnek:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Daha İyi Yaklaşım:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Kötü Vektör Arama
Vektör arama, yüksek boyutlu yerleştirmeler üzerinde anlamsal benzerlik aramasına olanak tanır. Kötü uygulamalarda zayıf dizin yapılandırması, uygun olmayan mesafe ölçümleri veya ölçeklenebilirlik sorunları yaşanır.
### Yanlış Mesafe Metriği
**Kötü Örnek:**```python
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

**Neden Kötü:**
- Öklid mesafesi vektör büyüklüğünden etkilenir
- Normalleştirilmiş vektörler için kosinüs benzerliği (nokta çarpımı) uygundur
- Anlamsal arama için sonuçlar daha az doğru olacaktır
**Daha İyi Yaklaşım:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Eksik Dizin Optimizasyonu
**Kötü Örnek:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Daha İyi Yaklaşım:**```python
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

### Yüksek Boyutlu Verileri İşlememek
**Kötü Örnek:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Daha İyi Yaklaşım:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Geri Çağırma ve Gecikme Dengesinin Göz ardı Edilmesi
**Kötü Örnek:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Daha İyi Yaklaşım:**```python
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

## En İyi Uygulamaların Özeti
### RAG Sistemleri
1. **Stratejik Olarak Parçalayın**: Anlamsal sınırlara saygı gösterin, örtüşmeyi ekleyin
2. **Sorgu Amacını Göz önünde bulundurun**: Alma işlemini kullanıcının isteklerine göre uyarlayın
3. **Bağlamı Yönetin**: LLM token limitleri dahilinde kalın
4. **Uçtan Uca Değerlendirin**: Yalnızca alımı değil, tüm RAG ardışık düzenini test edin
### Gömmeler
1. **Alana Uygun Modelleri Seçin**: Modeli içerik türünüze göre eşleştirin
2. **Vektörleri Normalleştirin**: Kosinüs benzerliği için gereklidir
3. **Tutarlılık**: Sisteminizin tamamında aynı modeli kullanın
4. **Drift'i İzleyin**: Veriler geliştikçe yerleştirmeleri yeniden eğitin veya güncelleyin
### Vektör Arama
1. **Doğru Mesafe Metriği'ni seçin**: Semantik için COSINE, uzamsal için EUCLID
2. **Dizinleri Yapılandırın**: Büyük veri kümeleri için HNSW'yi kullanın
3. **Ayar Parametreleri**: Kullanım durumunuz için geri çağırma ile gecikmeyi dengeleyin
4. **Performansı İzleyin**: Arama kalitesini ve zaman içindeki gecikmeyi izleyin
---

## İlgili Konular
- **AI/LLM Başarısızlıkları**: Halüsinasyonlar ve akıl yürütme sorunları için `ai_llm_failures.md`'ye bakın
- **Acente Tasarımı**: RAG içeren inşaat acenteleri için `../05_agents/agent_system_design.md`'ye bakın
- **Veri Kümesi Kalitesi**: Eğitim verileriyle ilgili hususlar için bkz. `../08_machine_learning/ml_data_issues.md`
- **Hızlı Mühendislik**: Bağlam işleme teknikleri için `../02_artificial_intelligence/prompt_engineering.md`'ye bakın
---

## Gelişmiş RAG Arıza Modelleri
### Orta Olayda Kaybolmak
**Nedir:** Yüksek Lisans'lar bağlamın başında ve sonundaki bilgilere odaklanma eğilimindedir. 
orta içeriğin göz ardı edilmesi.
**Kötü Örnek:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Neden Kötü:**
- Orta parçalardaki kritik bilgiler gözden kaçabilir
- Orta düzey içerik için modelin dikkati azalır
- Alakasız alınan içerik üzerinde jeton israfı
**Azaltma:**```python
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

### Çok Atlamalı Alma Hataları
**Nedir:** Birden çok parçanın birbirine bağlı olmasını gerektiren bilgilerin alınamaması.
**Kötü Örnek:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Azaltma:**```python
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

### Zamansal Muhakeme Başarısızlıkları
**Nedir:** RAG sistemleri, zamana duyarlı sorgular ve güncel olmayan bilgilerle mücadele eder.
**Kötü Örnek:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Azaltma:**```python
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

### Olumsuzluk İşleme Hataları
**Nedir:** Anlamsal arama genellikle sorgulardaki olumsuzlamaları gözden kaçırır.
**Kötü Örnek:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Azaltma:**```python
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

## Anti-Desenleri Yerleştirme
### Gömme Modellerini Karıştırma
**Nedir:** Dizine ekleme ve sorgulama için farklı modellerin kullanılması benzerliği bozar.
**Kötü Örnek:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Neden Kötü:**
- Farklı modeller uyumsuz vektör uzaylarında yerleştirmeler üretir
- Farklı model yerleştirmeleri arasındaki kosinüs benzerliği rastgele gürültüdür
- Sistem çalışıyor gibi görünüyor ancak çöp döndürüyor
**Algılama:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Gömme Boyutlarını Yoksayma
**Nedir:** Yerleştirme boyutunun performans üzerindeki etkisi dikkate alınmamıştır.
**Değişimler:**
| Boyutlar | Artıları | Eksileri | Kullanım Örneği |
|------------|------|------|----------|
| Düşük (128-256) | Hızlı arama, daha az bellek | Daha az incelikli gösterimler | Basit görevler, büyük ölçekli |
| Orta (384-768) | İyi denge | Orta düzey kaynaklar | Genel amaçlı |
| Yüksek (1024+) | Zengin temsiller | Yavaş, yoğun bellek kullanan | Karmaşık anlamsal görevler |
**Kötü Örnek:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Özel Tokenları İşlememek
**Nedir:** URL'lerin, kodun, sayıların ve özel karakterlerin düzgün şekilde işlenememesi.
**Kötü Örnek:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Azaltma:**```python
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

## Vektör Arama Performansı Sorunları
### Ölçekleme Sorunları
**Nedir:** Veri kümesi büyüdükçe arama kalitesi veya gecikme süresi düşer.
**Belirtiler:**
- Gecikme veri kümesi boyutuyla doğrusal olarak artar
- Daha fazla vektör eklendikçe düşüşleri hatırlayın
- Bellek kullanımı patlıyor
**Kötü Mimari:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Ölçeklenebilir Çözüm:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Soğuk Başlatma Sorunu
**Nedir:** Dizin yeniden oluşturulana kadar yeni belgeler alınamaz.
**Kötü Örnek:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Çözüm: Artımlı Dizin Oluşturma**```python
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

## RAG için Değerlendirme Metrikleri
### Bağlam Hassasiyeti
Alınan parçalardan kaçının gerçekten alakalı olduğunu ölçer.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Yanıtın Uygunluğu
Oluşturulan yanıtın gerçekten sorguya hitap edip etmediğini ölçer.
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

### Sadakat
Yanıtın geri alınan bağlama dayanıp dayanmadığını (halüsinasyona değil) ölçer.
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

## Gerçek Dünyadan Örnek Olay Çalışmaları
### Örnek Olay 1: Müşteri Desteği Chatbotu
**Sorun:** Chatbot ürün özellikleriyle ilgili yanlış yanıtlar verdi.
**Kök Neden Analizi:**
- Sınırlar boyunca bölünmüş özellik açıklamalarını parçalama
- Bulunan kısmi bilgilerin alınması
- LLM eksik detayların halüsinasyonunu gördü
**Çözüm:**
- Özellik bölümlerine göre anlamsal parçalama uygulandı
- Parçalar arasına 150 jetonluk çakışma eklendi
- Top_k sayısı 3'ten 5'e çıkarıldı
- Yeniden sıralama adımı eklendi
**Sonuçlar:**
- Doğruluk %62'den %89'a yükseltildi
- Halüsinasyon oranı %23'ten %4'e düştü
- Müşteri memnuniyeti %35 arttı
### Örnek Olay 2: Yasal Belge Arama
**Sorun:** Avukatlar ilgili emsal örnekleri bulamadılar.
**Temel Neden:**
- Genel yerleştirmeler yasal anlambilimi yakalayamıyordu
- Olumsuzluk sorguları başarısız oldu ("sorumluluğun belirlenmediği durumlar")
- Devrilen davalar için zamansal filtreleme yok
**Çözüm:**
- Yasal külliyatta ince ayarlı yerleştirmeler
- Olumsuzluk yönetimi uygulandı
- Vaka durumu meta verileri ve filtreleme eklendi
- Alıntı zincirleri için çok atlamalı erişim oluşturuldu
**Sonuçlar:**
- Recall@10'un oranı %45'ten %78'e yükseltildi
- Arama süresi 8 saniyeden 1,2 saniyeye düşürüldü
- Hukuk ekibi tarafından evlat edinme 3 kat arttı
### Örnek Olay 3: Teknik Dokümantasyon
**Sorun:** Geliştiriciler kod örnekleri bulamadı.
**Temel Neden:**
- Salt metin modellerinde kötü şekilde yerleştirilmiş kod blokları
- Eşleşen teorinin "nasıl doğrulanacağı" gibi sorgular, örnekler değil
- API sürümleri arasında ayrım yok
**Çözüm:**
- Kod bilinçli yerleştirme modeli kullanıldı
- Parçalar içerik türüne göre etiketlendi (kavram, öğretici, API referansı, örnek)
- Sürüm meta verileri eklendi
- Sorgu yönlendirme için uygulanan amaç sınıflandırması
**Sonuçlar:**
- Kod örneği alma doğruluğu: %34 → %82
- İlk başarılı sorguya kadar geçen süre %60 azaldı
- Dokümantasyon trafiği %45 arttı