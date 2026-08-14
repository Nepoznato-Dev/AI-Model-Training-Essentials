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
# Errori nella ricerca RAG e vettoriale
Questo documento consolida gli errori comuni nei sistemi RAG (Retrieval-Augmented Generation), nell'utilizzo dell'incorporamento e nelle implementazioni della ricerca vettoriale.
---

## Bad RAG (generazione aumentata di recupero)
La Retrieval-Augmented Generation (RAG) combina i sistemi di recupero con l'intelligenza artificiale generativa per produrre risposte più accurate e contestualmente rilevanti. Le cattive implementazioni RAG soffrono di scarsa qualità di recupero, gestione inadeguata del contesto o problemi di generazione.
### Strategia di suddivisione inadeguata
**Cattivo esempio:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Problemi:**
- Frasi e paragrafi sono divisi arbitrariamente
- Il contesto viene perso ai confini dei blocchi
- Il significato semantico è frammentato
- Il recupero restituisce informazioni incomplete
**Approccio migliore:**```python
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

### Sovrapposizione del contesto mancante
**Cattivo esempio:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Approccio migliore:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Ignorare l'intento della query
**Cattivo esempio:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Approccio migliore:**```python
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

### Overflow della finestra di contesto
**Cattivo esempio:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Approccio migliore:**```python
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

## Incorporamenti errati
Gli incorporamenti sono rappresentazioni vettoriali di dati che acquisiscono significato semantico. Incorporamenti errati derivano da una scarsa selezione del modello, da una formazione inadeguata o da un utilizzo improprio.
### Modello errato per il dominio
**Cattivo esempio:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Approccio migliore:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Non normalizzare i vettori
**Cattivo esempio:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Approccio migliore:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Ignorare le dimensioni di incorporamento
**Cattivo esempio:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Approccio migliore:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Ricerca vettoriale errata
La ricerca vettoriale consente la ricerca di somiglianza semantica su incorporamenti ad alta dimensione. Le implementazioni errate risentono di una scarsa configurazione dell'indice, di parametri di distanza inappropriati o di problemi di scalabilità.
### Metrica della distanza errata
**Cattivo esempio:**```python
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

**Perché non va bene:**
- La distanza euclidea è influenzata dalla grandezza del vettore
- Per i vettori normalizzati, è appropriata la somiglianza del coseno (prodotto scalare).
- I risultati saranno meno accurati per la ricerca semantica
**Approccio migliore:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Ottimizzazione dell'indice mancante
**Cattivo esempio:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Approccio migliore:**```python
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

### Mancata gestione dei dati ad alta dimensione
**Cattivo esempio:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Approccio migliore:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Ignorare il compromesso tra richiamo e latenza
**Cattivo esempio:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Approccio migliore:**```python
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

## Riepilogo delle migliori pratiche
### Sistemi RAG
1. **Clocca strategicamente**: rispetta i confini semantici, aggiungi sovrapposizioni
2. **Considera l'intento della query**: adatta il recupero in base alle esigenze dell'utente
3. **Gestisci contesto**: resta entro i limiti dei token LLM
4. **Valutazione end-to-end**: testare l'intera pipeline RAG, non solo il recupero
### Incorporamenti
1. **Scegli modelli appropriati per il dominio**: abbina il modello al tuo tipo di contenuto
2. **Normalizza vettori**: essenziale per la somiglianza del coseno
3. **Coerenza**: utilizza lo stesso modello in tutto il sistema
4. **Monitora la deriva**: riqualifica o aggiorna gli incorporamenti man mano che i dati evolvono
### Ricerca vettoriale
1. **Seleziona la metrica della distanza giusta**: COSENO per semantico, EUCLIDE per spaziale
2. **Configura indici**: utilizza HNSW per set di dati di grandi dimensioni
3. **Parametri di ottimizzazione**: bilancia il richiamo con la latenza per il tuo caso d'uso
4. **Monitora prestazioni**: monitora la qualità della ricerca e la latenza nel tempo
---

## Argomenti correlati
- **Errori AI/LLM**: consulta`ai_llm_failures.md`per allucinazioni e problemi di ragionamento
- **Progettazione agente**: vedere`../05_agents/agent_system_design.md`per la creazione di agenti con RAG
- **Qualità del set di dati**: consulta`../08_machine_learning/ml_data_issues.md`per considerazioni sui dati di addestramento
- **Prompt Engineering**: vedi`../02_artificial_intelligence/prompt_engineering.md`per le tecniche di gestione del contesto
---

## Modelli di errore RAG avanzati
### Perso nel fenomeno del mezzo
**Che cos'è:** Gli LLM tendono a concentrarsi sulle informazioni all'inizio e alla fine del contesto, 
ignorando il contenuto centrale.
**Cattivo esempio:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Perché non va bene:**
- Le informazioni critiche nelle parti centrali potrebbero essere trascurate
- L'attenzione del modello diminuisce per i contenuti intermedi
- Spreca token su contenuti recuperati irrilevanti
**Mitigazione:**```python
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

### Errori di recupero multi-hop
**Che cos'è:** Impossibile recuperare le informazioni che richiedono più parti connesse.
**Cattivo esempio:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Mitigazione:**```python
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

### Fallimenti del ragionamento temporale
**Che cos'è:** I sistemi RAG hanno problemi con query urgenti e informazioni obsolete.
**Cattivo esempio:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Mitigazione:**```python
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

### Errori nella gestione delle negazioni
**Che cos'è:** La ricerca semantica spesso non rileva le negazioni nelle query.
**Cattivo esempio:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Mitigazione:**```python
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

## Incorporamento di anti-pattern
### Miscelazione di modelli di incorporamento
**Che cos'è:** L'utilizzo di modelli diversi per l'indicizzazione e l'esecuzione di query interrompe la somiglianza.
**Cattivo esempio:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Perché non va bene:**
- Diversi modelli producono incorporamenti in spazi vettoriali incompatibili
- La somiglianza del coseno tra diversi incorporamenti di modelli è un rumore casuale
- Il sistema sembra funzionare ma restituisce spazzatura
**Rilevamento:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Ignorare le dimensioni di incorporamento
**Che cos'è:** Non considerare l'impatto dell'inclusione della dimensione sulle prestazioni.
**Compromessi:**
| Dimensioni | Pro | Contro | Caso d'uso |
|------------|------|------|----------|
| Basso (128-256) | Ricerca veloce, meno memoria | Rappresentazioni meno sfumate | Compiti semplici, su larga scala |
| Medio (384-768) | Buon equilibrio | Risorse moderate | Scopo generale |
| Alto (1024+) | Rappresentazioni ricche | Lento, ad alta intensità di memoria | Compiti semantici complessi |
**Cattivo esempio:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Non gestire i gettoni speciali
**Che cos'è:** Impossibile gestire correttamente URL, codice, numeri e caratteri speciali.
**Cattivo esempio:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Mitigazione:**```python
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

## Problemi di prestazioni della ricerca vettoriale
### Problemi di ridimensionamento
**Che cos'è:** La qualità o la latenza della ricerca peggiora man mano che il set di dati cresce.
**Sintomi:**
- La latenza aumenta linearmente con la dimensione del set di dati
- Richiama le gocce man mano che vengono aggiunti più vettori
- L'utilizzo della memoria esplode
**Architettura pessima:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Soluzione scalabile:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Problema di avviamento a freddo
**Che cos'è:** Non è possibile recuperare nuovi documenti finché l'indice non viene ricostruito.
**Cattivo esempio:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Soluzione: indicizzazione incrementale**```python
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

## Metriche di valutazione per RAG
### Precisione del contesto
Misura quanti blocchi recuperati sono effettivamente rilevanti.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Pertinenza della risposta
Misura se la risposta generata risponde effettivamente alla query.
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

### Fedeltà
Misura se la risposta è radicata nel contesto recuperato (non allucinato).
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

## Casi di studio nel mondo reale
### Caso di studio 1: Chatbot di assistenza clienti
**Problema:** Chatbot ha fornito risposte errate sulle funzionalità del prodotto.
**Analisi delle cause principali:**
- Suddivisione delle descrizioni delle funzionalità oltre i confini
- Il recupero ha trovato informazioni parziali
- Dettagli mancanti allucinati di LLM
**Soluzione:**
- Implementata suddivisione semantica per sezioni di funzionalità
- Aggiunta una sovrapposizione di 150 token tra i blocchi
- Aumentato top_k da 3 a 5
- Aggiunto passaggio di riclassificazione
**Risultati:**
- Precisione migliorata dal 62% all'89%
- Il tasso di allucinazioni è sceso dal 23% al 4%
- La soddisfazione del cliente è aumentata del 35%
### Caso di studio 2: ricerca di documenti legali
**Problema:** gli avvocati non sono riusciti a trovare precedenti rilevanti.
**Causa principale:**
- Gli incorporamenti generici non catturavano la semantica legale
- Richieste di negazione fallite ("casi in cui la responsabilità NON è stata accertata")
- Nessun filtraggio temporale per i casi ribaltati
**Soluzione:**
- Incorporamenti ottimizzati nel corpus giuridico
- Implementata la gestione della negazione
- Aggiunti metadati e filtri sullo stato del caso
- Costruito il recupero multi-hop per catene di citazioni
**Risultati:**
- Recall@10 migliorato dal 45% al 78%
- Tempo di ricerca ridotto da 8s a 1,2s
- L'adozione da parte del team legale è aumentata di 3 volte
### Caso di studio 3: documentazione tecnica
**Problema:** gli sviluppatori non sono riusciti a trovare esempi di codice.
**Causa principale:**
- Blocchi di codice incorporati male nei modelli di solo testo
- Domande come "come autenticare" la teoria abbinata, non gli esempi
- Nessuna distinzione tra le versioni API
**Soluzione:**
- Modello di incorporamento in grado di riconoscere il codice utilizzato
- Blocchi contrassegnati per tipo di contenuto (concetto, tutorial, riferimento API, esempio)
- Aggiunti metadati della versione
- Implementata la classificazione degli intenti per l'instradamento delle query
**Risultati:**
- Precisione nel recupero dell'esempio di codice: 34% → 82%
- Il tempo richiesto per la prima query riuscita è stato ridotto del 60%
- Il traffico della documentazione è aumentato del 45%