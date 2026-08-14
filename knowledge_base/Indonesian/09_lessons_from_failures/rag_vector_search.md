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
# Kegagalan Pencarian RAG dan Vektor
Dokumen ini menggabungkan kegagalan umum dalam sistem Retrieval-Augmented Generation (RAG), penggunaan penyematan, dan implementasi pencarian vektor.
---

## RAG Buruk (Generasi Pengambilan Augmented)
Retrieval-Augmented Generation (RAG) menggabungkan sistem pengambilan dengan AI generatif untuk menghasilkan respons yang lebih akurat dan relevan secara kontekstual. Implementasi RAG yang buruk disebabkan oleh kualitas pengambilan yang buruk, penanganan konteks yang tidak memadai, atau masalah pembangkitan.
### Strategi Pemotongan yang Buruk
**Contoh Buruk:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Masalah:**
- Kalimat dan paragraf dipisahkan secara sewenang-wenang
- Konteks hilang pada batasan bongkahan
- Makna semantik terfragmentasi
- Pengambilan mengembalikan informasi yang tidak lengkap
**Pendekatan yang Lebih Baik:**```python
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

### Konteks Hilang Tumpang Tindih
**Contoh Buruk:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Pendekatan yang Lebih Baik:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Mengabaikan Maksud Kueri
**Contoh Buruk:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Pendekatan yang Lebih Baik:**```python
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

### Jendela Konteks Melimpah
**Contoh Buruk:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Pendekatan yang Lebih Baik:**```python
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

## Penyematan Buruk
Embeddings adalah representasi vektor dari data yang menangkap makna semantik. Penyematan yang buruk disebabkan oleh pemilihan model yang buruk, pelatihan yang tidak memadai, atau penggunaan yang tidak tepat.
### Model Domain Salah
**Contoh Buruk:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Pendekatan yang Lebih Baik:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Tidak Menormalkan Vektor
**Contoh Buruk:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Pendekatan yang Lebih Baik:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Mengabaikan Dimensi Penyematan
**Contoh Buruk:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Pendekatan yang Lebih Baik:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Pencarian Vektor Buruk
Penelusuran vektor memungkinkan penelusuran kesamaan semantik melalui penyematan berdimensi tinggi. Implementasi yang buruk disebabkan oleh konfigurasi indeks yang buruk, metrik jarak yang tidak tepat, atau masalah skalabilitas.
### Metrik Jarak Salah
**Contoh Buruk:**```python
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

**Mengapa Ini Buruk:**
- Jarak Euclidean dipengaruhi oleh besaran vektor
- Untuk vektor yang dinormalisasi, kesamaan kosinus (perkalian titik) sesuai
- Hasil pencarian semantik akan kurang akurat
**Pendekatan yang Lebih Baik:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Optimasi Indeks Hilang
**Contoh Buruk:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Pendekatan yang Lebih Baik:**```python
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

### Tidak Menangani Data Dimensi Tinggi
**Contoh Buruk:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Pendekatan yang Lebih Baik:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Mengabaikan Penarikan vs Pengorbanan Latensi
**Contoh Buruk:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Pendekatan yang Lebih Baik:**```python
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

## Ringkasan Praktik Terbaik
### Sistem RAG
1. **Bagian Secara Strategis**: Hormati batasan semantik, tambahkan tumpang tindih
2. **Pertimbangkan Maksud Kueri**: Sesuaikan pengambilan berdasarkan keinginan pengguna
3. **Kelola Konteks**: Tetap dalam batas token LLM
4. **Evaluasi End-to-End**: Uji pipeline RAG secara keseluruhan, bukan hanya pengambilan
### Penyematan
1. **Pilih Model yang Sesuai Domain**: Cocokkan model dengan jenis konten Anda
2. **Normalisasi Vektor**: Penting untuk kesamaan kosinus
3. **Konsistensi**: Gunakan model yang sama di seluruh sistem Anda
4. **Monitor Drift**: Latih ulang atau perbarui penyematan seiring perkembangan data
### Pencarian Vektor
1. **Pilih Metrik Jarak yang Tepat**: COSINE untuk semantik, EUCLID untuk spasial
2. **Konfigurasi Indeks**: Gunakan HNSW untuk kumpulan data besar
3. **Parameter Penyempurnaan**: Menyeimbangkan penarikan kembali vs latensi untuk kasus penggunaan Anda
4. **Pantau Kinerja**: Lacak kualitas dan latensi penelusuran dari waktu ke waktu
---

## Topik Terkait
- **Kegagalan AI/LLM**: Lihat`ai_llm_failures.md`untuk masalah halusinasi dan penalaran
- **Desain Agen**: Lihat`../05_agents/agent_system_design.md`untuk agen bangunan dengan RAG
- **Kualitas Kumpulan Data**: Lihat`../08_machine_learning/ml_data_issues.md`untuk pertimbangan data pelatihan
- **Rekayasa Cepat**: Lihat`../02_artificial_intelligence/prompt_engineering.md`untuk teknik penanganan konteks
---

## Pola Kegagalan RAG Tingkat Lanjut
### Tersesat di Tengah Fenomena
**Apa Artinya:** LLM cenderung berfokus pada informasi di awal dan akhir konteks, 
mengabaikan konten tengah.
**Contoh Buruk:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Mengapa Ini Buruk:**
- Informasi penting di bagian tengah mungkin diabaikan
- Perhatian model berkurang untuk konten menengah
- Membuang token pada konten yang diambil tidak relevan
**Mitigasi:**```python
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

### Kegagalan Pengambilan Multi-Hop
**Apa Artinya:** Gagal mengambil informasi yang memerlukan beberapa bagian yang terhubung.
**Contoh Buruk:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Mitigasi:**```python
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

### Kegagalan Penalaran Temporal
**Apa Artinya:** Sistem RAG kesulitan menghadapi kueri yang sensitif terhadap waktu dan informasi yang ketinggalan jaman.
**Contoh Buruk:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Mitigasi:**```python
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

### Kegagalan Penanganan Negasi
**Apa Artinya:** Penelusuran semantik sering kali melewatkan negasi dalam kueri.
**Contoh Buruk:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Mitigasi:**```python
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

## Menanamkan Anti-Pola
### Mencampur Model Penyematan
**Apa Artinya:** Menggunakan model yang berbeda untuk pengindeksan vs. pembuatan kueri akan merusak kesamaan.
**Contoh Buruk:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Mengapa Ini Buruk:**
- Model yang berbeda menghasilkan penyematan dalam ruang vektor yang tidak kompatibel
- Kesamaan kosinus antara penyematan model yang berbeda adalah gangguan acak
- Sistem tampaknya berfungsi tetapi mengembalikan sampah
**Deteksi:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Mengabaikan Dimensi Penyematan
**Apa Artinya:** Tidak mempertimbangkan dampak penyematan dimensi terhadap kinerja.
**Pengorbanan:**
| Dimensi | Kelebihan | Kontra | Kasus Penggunaan |
|------------|------|------|----------|
| Rendah (128-256) | Pencarian cepat, lebih sedikit memori | Representasi yang kurang bernuansa | Tugas sederhana, skala besar |
| Sedang (384-768) | Keseimbangan yang bagus | Sumber daya moderat | Tujuan umum |
| Tinggi (1024+) | Representasi yang kaya | Lambat, intensif memori | Tugas semantik yang kompleks |
**Contoh Buruk:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Tidak Menangani Token Khusus
**Apa Artinya:** Gagal menangani URL, kode, angka, dan karakter khusus dengan benar.
**Contoh Buruk:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Mitigasi:**```python
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

## Masalah Kinerja Pencarian Vektor
### Masalah Penskalaan
**Apa Artinya:** Kualitas atau latensi penelusuran menurun seiring bertambahnya kumpulan data.
**Gejala:**
- Latensi meningkat secara linier seiring dengan ukuran kumpulan data
- Penarikan kembali penurunan seiring bertambahnya vektor
- Penggunaan memori meledak
**Arsitektur Buruk:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Solusi Skalabel:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Masalah Start Dingin
**Apa Artinya:** Dokumen baru tidak dapat diambil sampai indeks dibuat ulang.
**Contoh Buruk:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Solusi: Pengindeksan Tambahan**```python
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

## Metrik Evaluasi untuk RAG
### Presisi Konteks
Mengukur berapa banyak potongan yang diambil yang benar-benar relevan.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Jawaban Relevansi
Mengukur apakah jawaban yang dihasilkan benar-benar menjawab pertanyaan.
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

### Kesetiaan
Mengukur apakah jawaban didasarkan pada konteks yang diambil (bukan halusinasi).
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

## Studi Kasus Dunia Nyata
### Studi Kasus 1: Chatbot Dukungan Pelanggan
**Masalah:** Chatbot memberikan jawaban yang salah tentang fitur produk.
**Analisis Akar Penyebab:**
- Memotong deskripsi fitur terpisah melintasi batas
- Pengambilan menemukan sebagian informasi
- LLM berhalusinasi detail yang hilang
**Solusi:**
- Menerapkan pengelompokan semantik berdasarkan bagian fitur
- Menambahkan 150 token yang tumpang tindih antar bongkahan
- Peningkatan top_k dari 3 menjadi 5
- Menambahkan langkah pemeringkatan ulang
**Hasil:**
- Akurasi meningkat dari 62% menjadi 89%
- Tingkat halusinasi turun dari 23% menjadi 4%
- Kepuasan pelanggan meningkat 35%
### Studi Kasus 2: Pencarian Dokumen Hukum
**Masalah:** Pengacara tidak dapat menemukan preseden yang relevan.
**Akar Penyebab:**
- Penyematan umum tidak menangkap semantik hukum
- Kueri negasi gagal ("kasus di mana tanggung jawab TIDAK ditetapkan")
- Tidak ada pemfilteran sementara untuk kasus yang dibatalkan
**Solusi:**
- Penyematan yang disempurnakan pada korpus hukum
- Penerapan penanganan negasi
- Menambahkan metadata dan pemfilteran status kasus
- Membangun pengambilan multi-hop untuk rantai kutipan
**Hasil:**
- Recall@10 ditingkatkan dari 45% menjadi 78%
- Waktu pencarian berkurang dari 8 detik menjadi 1,2 detik
- Adopsi oleh tim hukum meningkat 3x
### Studi Kasus 3: Dokumentasi Teknis
**Masalah:** Pengembang tidak dapat menemukan contoh kode.
**Akar Penyebab:**
- Blok kode tertanam dengan buruk pada model yang hanya berupa teks
- Pertanyaan seperti "cara mengautentikasi" teori yang cocok, bukan contoh
- Tidak ada perbedaan antara versi API
**Solusi:**
- Menggunakan model penyematan yang sadar kode
- Potongan yang diberi tag berdasarkan tipe konten (konsep, tutorial, referensi API, contoh)
- Menambahkan metadata versi
- Klasifikasi maksud yang diterapkan untuk perutean kueri
**Hasil:**
- Akurasi pengambilan contoh kode: 34% → 82%
- Waktu hingga kueri pertama berhasil berkurang 60%
- Lalu lintas dokumentasi meningkat 45%