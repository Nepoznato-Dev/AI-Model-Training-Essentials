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

# Błędy wyszukiwania RAG i wektorów
W tym dokumencie podsumowano typowe błędy w systemach generowania rozszerzonego wyszukiwania (RAG), wykorzystaniu osadzania i implementacjach wyszukiwania wektorowego.
---

## Zły RAG (generacja wzmocniona odzyskiwaniem)
Generowanie rozszerzone wyszukiwania (RAG) łączy systemy wyszukiwania z generatywną sztuczną inteligencją, aby zapewnić dokładniejsze i kontekstowo odpowiednie odpowiedzi. Złe implementacje RAG charakteryzują się słabą jakością wyszukiwania, nieodpowiednią obsługą kontekstu lub problemami z generowaniem.
### Zła strategia dzielenia
**Zły przykład:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Problemy:**
- Zdania i akapity są dzielone dowolnie
- Kontekst został utracony na granicach fragmentów
- Znaczenie semantyczne jest fragmentaryczne
- Pobieranie zwraca niekompletne informacje
**Lepsze podejście:**```python
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

### Brakujące nakładanie się kontekstów
**Zły przykład:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Lepsze podejście:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Ignorowanie intencji zapytania
**Zły przykład:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Lepsze podejście:**```python
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

### Przepełnienie okna kontekstowego
**Zły przykład:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Lepsze podejście:**```python
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

## Złe osadzenie
Osadzania to wektorowe reprezentacje danych, które oddają znaczenie semantyczne. Złe osadzenie wynika ze złego wyboru modelu, nieodpowiedniego przeszkolenia lub niewłaściwego użytkowania.
### Zły model domeny
**Zły przykład:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Lepsze podejście:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Nie normalizowanie wektorów
**Zły przykład:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Lepsze podejście:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Ignorowanie wymiarów osadzania
**Zły przykład:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Lepsze podejście:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Złe wyszukiwanie wektorów
Wyszukiwanie wektorów umożliwia semantyczne wyszukiwanie podobieństw w osadzaniach wielowymiarowych. Złe implementacje charakteryzują się słabą konfiguracją indeksu, niewłaściwymi metrykami odległości lub problemami ze skalowalnością.
### Nieprawidłowy wskaźnik odległości
**Zły przykład:**```python
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

**Dlaczego to jest złe:**
- Odległość euklidesowa zależy od wielkości wektora
- W przypadku wektorów znormalizowanych odpowiednie jest podobieństwo cosinusowe (iloczyn skalarny).
- Wyniki będą mniej dokładne w przypadku wyszukiwania semantycznego
**Lepsze podejście:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Brak optymalizacji indeksu
**Zły przykład:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Lepsze podejście:**```python
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

### Brak obsługi danych wielowymiarowych
**Zły przykład:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Lepsze podejście:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Ignorowanie kompromisu między wycofaniem a opóźnieniem
**Zły przykład:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Lepsze podejście:**```python
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

## Podsumowanie najlepszych praktyk
### Systemy RAG
1. **Podziel strategicznie**: Przestrzegaj granic semantycznych, dodaj nakładanie się
2. **Rozważ intencję zapytania**: Dostosuj pobieranie w oparciu o oczekiwania użytkownika
3. **Zarządzaj kontekstem**: Trzymaj się limitów tokenów LLM
4. **Oceń kompleksowo**: przetestuj cały rurociąg RAG, a nie tylko jego pobieranie
### Osadzenia
1. **Wybierz modele odpowiednie dla domeny**: Dopasuj model do rodzaju treści
2. **Normalizuj wektory**: Niezbędne dla podobieństwa cosinus
3. **Spójność**: Używaj tego samego modelu w całym systemie
4. **Monitoruj dryf**: Ponowne szkolenie lub aktualizacja osadzania w miarę rozwoju danych
### Wyszukiwanie wektorów
1. **Wybierz właściwą metrykę odległości**: COSINUS dla semantycznego, EUCLID dla przestrzennego
2. **Konfiguruj indeksy**: Użyj HNSW w przypadku dużych zbiorów danych
3. **Dostosuj parametry**: Przywołanie balansu vs opóźnienie dla Twojego przypadku użycia
4. **Monitoruj wydajność**: Śledź jakość wyszukiwania i opóźnienia w czasie
---

## Powiązane tematy
- **Awarie AI/LLM**: Zobacz`ai_llm_failures.md`w przypadku halucynacji i problemów z rozumowaniem
- **Projekt agenta**: Zobacz`../05_agents/agent_system_design.md`dla agentów budowlanych z RAG
- **Jakość zbioru danych**: Zobacz `../08_machine_learning/ml_data_issues.md`, aby zapoznać się z rozważaniami dotyczącymi danych szkoleniowych
- **Szybka inżynieria**: Zobacz `../02_artificial_intelligence/prompt_engineering.md`, aby zapoznać się z technikami obsługi kontekstu
---

## Zaawansowane wzorce awarii RAG
### Zagubiony w środku zjawiska
**Co to jest:** LLM zwykle skupiają się na informacjach znajdujących się na początku i na końcu kontekstu, 
ignorując środkową treść.
**Zły przykład:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Dlaczego to jest złe:**
- Krytyczne informacje w środkowych fragmentach mogą zostać przeoczone
- Uwaga modelki maleje w przypadku średniej zawartości
- Marnuje tokeny na nieistotne odzyskane treści
**Łagodzenie:**```python
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

### Błędy pobierania metodą wielu przeskoków
**Co to jest:** Nie można pobrać informacji wymagających wielu połączonych elementów.
**Zły przykład:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Łagodzenie:**```python
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

### Błędy w rozumowaniu czasowym
**Co to jest:** systemy RAG borykają się z zapytaniami, w których liczy się czas i nieaktualnymi informacjami.
**Zły przykład:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Łagodzenie:**```python
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

### Błędy obsługi negacji
**Co to jest:** W wyszukiwaniu semantycznym często pomijane są negacje w zapytaniach.
**Zły przykład:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Łagodzenie:**```python
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

## Osadzanie anty-wzorców
### Mieszanie modeli osadzania
**Co to jest:** używanie różnych modeli indeksowania i wykonywania zapytań psuje podobieństwo.
**Zły przykład:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Dlaczego to jest złe:**
- Różne modele powodują osadzanie w niezgodnych przestrzeniach wektorowych
- Podobieństwo cosinusowe pomiędzy różnymi osadzaniami modeli to szum losowy
- System wydaje się działać, ale zwraca śmieci
**Wykrywanie:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Ignorowanie wymiarów osadzania
**Co to jest:** Nie biorąc pod uwagę wpływu wymiaru osadzania na wydajność.
**Kompromisy:**
| Wymiary | Plusy | Wady | Przypadek użycia |
|------------|------|------|---------|
| Niski (128-256) | Szybkie wyszukiwanie, mniej pamięci | Mniej zniuansowane przedstawienia | Proste zadania, duża skala |
| Średni (384-768) | Dobra równowaga | Umiarkowane zasoby | Cel ogólny |
| Wysoka (1024+) | Bogate reprezentacje | Powolny, wymagający dużej ilości pamięci | Złożone zadania semantyczne |
**Zły przykład:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Nie obsługuje tokenów specjalnych
**Co to jest:** niewłaściwa obsługa adresów URL, kodu, liczb i znaków specjalnych.
**Zły przykład:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Łagodzenie:**```python
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

## Problemy z wydajnością wyszukiwania wektorowego
### Problemy ze skalowaniem
**Co to jest:** Jakość wyszukiwania lub opóźnienie spadają wraz ze wzrostem zbioru danych.
**Objawy:**
- Opóźnienie rośnie liniowo wraz z rozmiarem zbioru danych
- Przywołanie spada w miarę dodawania większej liczby wektorów
- Eksploduje wykorzystanie pamięci
**Zła architektura:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Skalowalne rozwiązanie:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Problem z zimnym startem
**Co to jest:** nowych dokumentów nie można odzyskać, dopóki indeks nie zostanie odbudowany.
**Zły przykład:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Rozwiązanie: Indeksowanie przyrostowe**```python
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

## Metryki oceny dla RAG
### Precyzja kontekstu
Mierzy, ile pobranych fragmentów jest rzeczywiście istotnych.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Trafność odpowiedzi
Mierzy, czy wygenerowana odpowiedź faktycznie odnosi się do zapytania.
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

### Wierność
Mierzy, czy odpowiedź jest osadzona w odzyskanym kontekście (nie jest halucynacją).
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

## Studia przypadków z prawdziwego świata
### Studium przypadku 1: Chatbot obsługi klienta
**Problem:** Chatbot udzielił błędnych odpowiedzi na temat cech produktu.
**Analiza pierwotnej przyczyny:**
- Dzielenie opisów obiektów podzielonych na kawałki ponad granicami
- Pobieranie znalezionych częściowych informacji
- LLM miał halucynacje, brakujące szczegóły
**Rozwiązanie:**
- Zaimplementowano podział semantyczny według sekcji funkcji
- Dodano nakładanie się 150 żetonów pomiędzy fragmentami
- Zwiększono top_k z 3 do 5
- Dodano etap ponownego rankingu
**Wyniki:**
- Celność zwiększona z 62% do 89%
- Częstotliwość halucynacji zmniejszona z 23% do 4%
- Zadowolenie klienta wzrosło o 35%
### Studium przypadku 2: Wyszukiwanie dokumentów prawnych
**Problem:** prawnicy nie mogli znaleźć odpowiednich precedensów.
**Główna przyczyna:**
- Osadzanie ogólne nie uwzględniało semantyki prawnej
- Zapytania o negację nie powiodły się („przypadki, w których NIE ustalono odpowiedzialności”)
- Brak tymczasowego filtrowania unieważnionych spraw
**Rozwiązanie:**
- Dopracowane osadzenie w korpusie prawnym
- Zaimplementowano obsługę negacji
- Dodano metadane statusu sprawy i filtrowanie
- Wbudowane wyszukiwanie wieloprzeskokowe dla łańcuchów cytowań
**Wyniki:**
- Przywołanie@10 poprawione z 45% do 78%
- Czas wyszukiwania zmniejszony z 8 s do 1,2 s
- Adopcja przez zespół prawniczy wzrosła 3-krotnie
### Studium przypadku 3: Dokumentacja techniczna
**Problem:** Programiści nie mogli znaleźć przykładów kodu.
**Główna przyczyna:**
- Bloki kodu słabo osadzone w modelach tekstowych
- Zapytania typu „jak uwierzytelnić” dopasowaną teorię, a nie przykłady
- Brak rozróżnienia pomiędzy wersjami API
**Rozwiązanie:**
- Używany model osadzania uwzględniający kod
- Oznaczone fragmenty według typu zawartości (koncepcja, samouczek, odniesienie do API, przykład)
- Dodano metadane wersji
- Wdrożono klasyfikację intencji dla routingu zapytań
**Wyniki:**
- Dokładność wyszukiwania przykładowego kodu: 34% → 82%
- Czas do pierwszego udanego zapytania zmniejszony o 60%
- Ruch związany z dokumentacją wzrósł o 45%