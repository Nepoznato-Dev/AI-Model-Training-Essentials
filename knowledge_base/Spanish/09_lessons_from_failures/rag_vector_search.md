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
# Fallos de búsqueda de RAG y vectores
Este documento consolida fallas comunes en los sistemas de recuperación-generación aumentada (RAG), el uso de incorporación y las implementaciones de búsqueda de vectores.
---

## Bad RAG (Generación aumentada de recuperación)
La generación aumentada de recuperación (RAG) combina sistemas de recuperación con IA generativa para producir respuestas más precisas y contextualmente relevantes. Las malas implementaciones de RAG sufren de una mala calidad de recuperación, un manejo inadecuado del contexto o problemas de generación.
### Mala estrategia de fragmentación
**Mal ejemplo:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Problemas:**
- Las oraciones y los párrafos se dividen arbitrariamente.
- El contexto se pierde en los límites de los fragmentos.
- El significado semántico está fragmentado.
- La recuperación devuelve información incompleta.
**Mejor enfoque:**```python
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

### Falta superposición de contexto
**Mal ejemplo:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Mejor enfoque:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Ignorar la intención de la consulta
**Mal ejemplo:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Mejor enfoque:**```python
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

### Desbordamiento de ventana de contexto
**Mal ejemplo:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Mejor enfoque:**```python
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

## Incrustaciones incorrectas
Las incrustaciones son representaciones vectoriales de datos que capturan el significado semántico. Las malas incorporaciones son el resultado de una mala selección de modelos, una formación inadecuada o un uso inadecuado.
### Modelo incorrecto para el dominio
**Mal ejemplo:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Mejor enfoque:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### No normalizar vectores
**Mal ejemplo:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Mejor enfoque:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Ignorar las dimensiones de incrustación
**Mal ejemplo:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Mejor enfoque:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Búsqueda de vectores incorrecta
La búsqueda vectorial permite la búsqueda de similitudes semánticas en incrustaciones de alta dimensión. Las malas implementaciones sufren de una mala configuración del índice, métricas de distancia inapropiadas o problemas de escalabilidad.
### Métrica de distancia incorrecta
**Mal ejemplo:**```python
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

**Por qué es malo:**
- La distancia euclidiana se ve afectada por la magnitud del vector.
- Para vectores normalizados, la similitud del coseno (producto escalar) es apropiada
- Los resultados serán menos precisos para la búsqueda semántica.
**Mejor enfoque:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Falta optimización del índice
**Mal ejemplo:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Mejor enfoque:**```python
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

### No manejar datos de alta dimensión
**Mal ejemplo:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Mejor enfoque:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Ignorar la compensación entre recuperación y latencia
**Mal ejemplo:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Mejor enfoque:**```python
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

## Resumen de mejores prácticas
### Sistemas RAG
1. **Fragmentar estratégicamente**: respetar los límites semánticos, agregar superposición
2. **Considere la intención de la consulta**: adapte la recuperación según lo que quiera el usuario
3. **Administrar el contexto**: mantenerse dentro de los límites del token LLM
4. **Evaluar de un extremo a otro**: probar la canalización RAG completa, no solo la recuperación
### Incrustaciones
1. **Elija modelos apropiados para el dominio**: haga coincidir el modelo con su tipo de contenido
2. **Normalizar vectores**: esencial para la similitud de cosenos
3. **Consistencia**: use el mismo modelo en todo su sistema
4. **Monitorizar deriva**: vuelva a entrenar o actualizar incorporaciones a medida que evolucionan los datos
### Búsqueda de vectores
1. **Seleccione la métrica de distancia correcta**: COSINO para semántica, EUCLID para espacial
2. **Configurar índices**: use HNSW para conjuntos de datos grandes
3. **Parámetros de ajuste**: recuperación de equilibrio frente a latencia para su caso de uso
4. **Supervisar el rendimiento**: realice un seguimiento de la calidad de la búsqueda y la latencia a lo largo del tiempo
---

## Temas relacionados
- **Fallos de AI/LLM**: consulte`ai_llm_failures.md`para alucinaciones y problemas de razonamiento.
- **Diseño de agente**: consulte`../05_agents/agent_system_design.md`para agentes de construcción con RAG
- **Calidad del conjunto de datos**: consulte`../08_machine_learning/ml_data_issues.md`para conocer consideraciones sobre datos de entrenamiento
- **Ingeniería rápida**: consulte`../02_artificial_intelligence/prompt_engineering.md`para conocer técnicas de manejo de contexto
---

## Patrones avanzados de falla de RAG
### Fenómeno perdido en el medio
**Qué es:** Los LLM tienden a centrarse en la información al principio y al final del contexto, 
ignorando el contenido medio.
**Mal ejemplo:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Por qué es malo:**
- Es posible que se pase por alto la información crítica en los fragmentos intermedios.
- La atención del modelo disminuye para el contenido intermedio.
- Desperdicia tokens en contenido recuperado irrelevante
**Mitigación:**```python
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

### Fallos de recuperación de múltiples saltos
**Qué es:** No se puede recuperar información que requiere varias piezas conectadas.
**Mal ejemplo:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Mitigación:**```python
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

### Fallos de razonamiento temporal
**Qué es:** Los sistemas RAG luchan con consultas urgentes e información desactualizada.
**Mal ejemplo:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Mitigación:**```python
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

### Fallos en el manejo de la negación
**Qué es:** La búsqueda semántica a menudo omite negaciones en las consultas.
**Mal ejemplo:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Mitigación:**```python
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

## Incrustar antipatrones
### Mezcla de modelos de incrustación
**Qué es:** El uso de diferentes modelos para indexar y consultar rompe la similitud.
**Mal ejemplo:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Por qué es malo:**
- Diferentes modelos producen incrustaciones en espacios vectoriales incompatibles.
- La similitud del coseno entre diferentes incorporaciones de modelos es ruido aleatorio.
- El sistema parece funcionar pero devuelve basura
**Detección:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Ignorar las dimensiones de incrustación
**Qué es:** Sin considerar el impacto de la dimensión integrada en el rendimiento.
**Compensaciones:**
| Dimensiones | Ventajas | Contras | Caso de uso |
|------------|------|------|----------|
| Bajo (128-256) | Búsqueda rápida, menos memoria | Representaciones menos matizadas | Tareas sencillas, a gran escala |
| Medio (384-768) | Buen equilibrio | Recursos moderados | Propósito general |
| Alto (1024+) | Ricas representaciones | Lento, requiere mucha memoria | Tareas semánticas complejas |
**Mal ejemplo:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### No manejar tokens especiales
**Qué es:** No manejar correctamente las URL, códigos, números y caracteres especiales.
**Mal ejemplo:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Mitigación:**```python
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

## Problemas de rendimiento de la búsqueda de vectores
### Problemas de escala
**Qué es:** La calidad de la búsqueda o la latencia se degradan a medida que crece el conjunto de datos.
**Síntomas:**
- La latencia aumenta linealmente con el tamaño del conjunto de datos.
- La recuperación disminuye a medida que se agregan más vectores.
- El uso de memoria se dispara
**Mala arquitectura:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Solución escalable:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Problema de arranque en frío
**Qué es:** Los documentos nuevos no se pueden recuperar hasta que se reconstruya el índice.
**Mal ejemplo:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Solución: Indexación incremental**```python
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

## Métricas de evaluación para RAG
### Precisión del contexto
Mide cuántos fragmentos recuperados son realmente relevantes.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Relevancia de la respuesta
Mide si la respuesta generada realmente aborda la consulta.
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

### Fidelidad
Mide si la respuesta se basa en el contexto recuperado (no es una alucinación).
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

## Estudios de casos del mundo real
### Estudio de caso 1: Chatbot de atención al cliente
**Problema:** Chatbot dio respuestas incorrectas sobre las características del producto.
**Análisis de causa raíz:**
- Fragmentación de descripciones de funciones divididas a través de límites
- Recuperación de información parcial encontrada.
- LLM alucinó que le faltaban detalles
**Solución:**
- Implementación de fragmentación semántica por secciones de características.
- Se agregó superposición de 150 tokens entre fragmentos.
- Aumentó top_k de 3 a 5.
- Se agregó un paso de reclasificación.
**Resultados:**
- La precisión mejoró del 62% al 89%
- La tasa de alucinaciones cayó del 23% al 4%
- La satisfacción del cliente aumentó un 35%
### Estudio de caso 2: Búsqueda de documentos legales
**Problema:** Los abogados no pudieron encontrar precedentes relevantes.
**Causa raíz:**
- Las incrustaciones genéricas no capturaron la semántica legal.
- Las consultas de negación fallaron ("casos donde NO se estableció responsabilidad")
- Sin filtrado temporal para casos anulados
**Solución:**
- Incorporaciones afinadas en corpus legales.
- Manejo de negación implementado
- Se agregaron metadatos y filtrado del estado del caso.
- Recuperación de múltiples saltos para cadenas de citas.
**Resultados:**
- Recall@10 mejoró del 45% al 78%
- Tiempo de búsqueda reducido de 8 segundos a 1,2 segundos.
- La adopción por parte del equipo legal aumentó 3 veces
### Estudio de caso 3: Documentación técnica
**Problema:** Los desarrolladores no pudieron encontrar ejemplos de código.
**Causa raíz:**
- Bloques de código mal integrados con modelos de solo texto
- Consultas como "cómo autenticar" la teoría coincidente, no ejemplos
- No hay distinción entre versiones de API.
**Solución:**
- Modelo de incrustación con reconocimiento de código usado
- Fragmentos etiquetados por tipo de contenido (concepto, tutorial, referencia de API, ejemplo)
- Metadatos de versión agregados
- Clasificación de intenciones implementada para el enrutamiento de consultas.
**Resultados:**
- Precisión de recuperación de ejemplo de código: 34% → 82%
- El tiempo hasta la primera consulta exitosa se redujo en un 60%
- El tráfico de documentación aumentó un 45%