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
# Échecs de recherche RAG et Vector
Ce document consolide les échecs courants dans les systèmes de génération augmentée de récupération (RAG), l'utilisation de l'intégration et les implémentations de recherche vectorielle.
---

## Bad RAG (génération augmentée par récupération)
La génération augmentée par récupération (RAG) combine des systèmes de récupération avec une IA générative pour produire des réponses plus précises et contextuellement pertinentes. Les mauvaises implémentations de RAG souffrent d'une mauvaise qualité de récupération, d'une gestion du contexte inadéquate ou de problèmes de génération.
### Mauvaise stratégie de segmentation
**Mauvais exemple :**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Problèmes :**
- Les phrases et les paragraphes sont divisés arbitrairement
- Le contexte est perdu aux limites des morceaux
- Le sens sémantique est fragmenté
- La récupération renvoie des informations incomplètes
**Meilleure approche :**```python
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

### Chevauchement de contexte manquant
**Mauvais exemple :**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Meilleure approche :**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Ignorer l'intention de la requête
**Mauvais exemple :**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Meilleure approche :**```python
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

### Débordement de la fenêtre contextuelle
**Mauvais exemple :**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Meilleure approche :**```python
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

## Mauvaises intégrations
Les intégrations sont des représentations vectorielles de données qui capturent une signification sémantique. Les mauvaises intégrations résultent d’une mauvaise sélection de modèle, d’une formation inadéquate ou d’une utilisation inappropriée.
### Mauvais modèle de domaine
**Mauvais exemple :**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Meilleure approche :**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Ne normalise pas les vecteurs
**Mauvais exemple :**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Meilleure approche :**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Ignorer les dimensions d'intégration
**Mauvais exemple :**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Meilleure approche :**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Mauvaise recherche de vecteurs
La recherche de vecteurs permet une recherche de similarité sémantique sur des intégrations de grande dimension. Les mauvaises implémentations souffrent d'une mauvaise configuration d'index, de mesures de distance inappropriées ou de problèmes d'évolutivité.
### Mauvaise mesure de distance
**Mauvais exemple :**```python
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

**Pourquoi c'est mauvais :**
- La distance euclidienne est affectée par la magnitude vectorielle
- Pour les vecteurs normalisés, la similarité cosinus (produit scalaire) est appropriée
- Les résultats seront moins précis pour la recherche sémantique
**Meilleure approche :**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Optimisation de l'index manquant
**Mauvais exemple :**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Meilleure approche :**```python
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

### Ne gère pas les données de grande dimension
**Mauvais exemple :**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Meilleure approche :**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Ignorer le compromis entre rappel et latence
**Mauvais exemple :**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Meilleure approche :**```python
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

## Résumé des meilleures pratiques
### Systèmes RAG
1. **Chunk stratégiquement** : respectez les limites sémantiques, ajoutez un chevauchement
2. **Considérez l'intention de la requête** : adaptez la récupération en fonction de ce que souhaite l'utilisateur
3. **Gérer le contexte** : restez dans les limites des jetons LLM
4. **Évaluer de bout en bout** : tester le pipeline RAG complet, pas seulement la récupération
### Intégrations
1. **Choisissez des modèles appropriés au domaine** : faites correspondre le modèle à votre type de contenu
2. **Normaliser les vecteurs** : essentiel pour la similarité cosinus
3. **Cohérence** : utilisez le même modèle dans tout votre système
4. **Surveiller la dérive** : recycler ou mettre à jour les intégrations à mesure que les données évoluent
### Recherche de vecteurs
1. **Sélectionnez la métrique de bonne distance** : COSINE pour la sémantique, EUCLID pour la spatialité.
2. **Configurer les index** : utilisez HNSW pour les grands ensembles de données
3. **Paramètres de réglage** : équilibrez le rappel et la latence pour votre cas d'utilisation
4. **Surveiller les performances** : suivez la qualité et la latence de la recherche au fil du temps
---

## Sujets connexes
- **Échecs AI/LLM** : voir`ai_llm_failures.md`pour les hallucinations et les problèmes de raisonnement
- **Conception d'agent** : voir`../05_agents/agent_system_design.md`pour les agents de construction avec RAG
- **Qualité de l'ensemble de données** : voir`../08_machine_learning/ml_data_issues.md`pour les considérations relatives aux données d'entraînement.
- **Ingénierie rapide** : voir`../02_artificial_intelligence/prompt_engineering.md`pour les techniques de gestion du contexte
---

## Modèles de défaillance RAG avancés
### Perdu dans le phénomène du milieu
**Qu'est-ce que c'est :** Les LLM ont tendance à se concentrer sur les informations au début et à la fin du contexte, 
ignorer le contenu intermédiaire.
**Mauvais exemple :**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Pourquoi c'est mauvais :**
- Les informations critiques dans les morceaux du milieu peuvent être négligées
- L'attention du modèle diminue pour le contenu intermédiaire
- Gaspille des jetons sur du contenu récupéré non pertinent
**Atténuation:**```python
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

### Échecs de récupération multi-sauts
**Qu'est-ce que c'est :** Impossible de récupérer des informations nécessitant plusieurs éléments connectés.
**Mauvais exemple :**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Atténuation:**```python
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

### Échecs du raisonnement temporel
**Qu'est-ce que c'est :** Les systèmes RAG sont confrontés à des requêtes urgentes et à des informations obsolètes.
**Mauvais exemple :**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Atténuation:**```python
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

### Échecs de gestion des négations
**Qu'est-ce que c'est :** La recherche sémantique manque souvent des négations dans les requêtes.
**Mauvais exemple :**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Atténuation:**```python
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

## Intégration d'anti-modèles
### Mélange de modèles d'intégration
**Qu'est-ce que c'est :** L'utilisation de différents modèles pour l'indexation et l'interrogation rompt la similarité.
**Mauvais exemple :**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Pourquoi c'est mauvais :**
- Différents modèles produisent des plongements dans des espaces vectoriels incompatibles
- La similarité cosinus entre les différentes intégrations de modèles est un bruit aléatoire
- Le système semble fonctionner mais renvoie des déchets
**Détection:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Ignorer les dimensions d'intégration
**Qu'est-ce que c'est :** Ne tient pas compte de l'impact de la dimension d'intégration sur les performances.
**Compromis :**
| Dimensions | Avantages | Inconvénients | Cas d'utilisation |
|------------|------|------|--------------|
| Faible (128-256) | Recherche rapide, moins de mémoire | Des représentations moins nuancées | Tâches simples, à grande échelle |
| Moyen (384-768) | Bon équilibre | Ressources modérées | Usage général |
| Élevé (1024+) | Représentations riches | Lent, gourmand en mémoire | Tâches sémantiques complexes |
**Mauvais exemple :**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Ne gère pas les jetons spéciaux
**Qu'est-ce que c'est :** Impossible de gérer correctement les URL, le code, les chiffres et les caractères spéciaux.
**Mauvais exemple :**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Atténuation:**```python
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

## Problèmes de performances de recherche de vecteurs
### Problèmes de mise à l'échelle
**Qu'est-ce que c'est :** La qualité ou la latence de la recherche se dégrade à mesure que l'ensemble de données augmente.
**Symptômes :**
- La latence augmente linéairement avec la taille de l'ensemble de données
- Rappel des gouttes à mesure que d'autres vecteurs sont ajoutés
- L'utilisation de la mémoire explose
**Mauvaise architecture :**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Solution évolutive :**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Problème de démarrage à froid
**Qu'est-ce que c'est :** Les nouveaux documents ne peuvent pas être récupérés tant que l'index n'est pas reconstruit.
**Mauvais exemple :**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Solution : indexation incrémentielle**```python
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

## Métriques d'évaluation pour RAG
### Précision du contexte
Mesure combien de morceaux récupérés sont réellement pertinents.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Pertinence de la réponse
Mesure si la réponse générée répond réellement à la requête.
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

### Fidélité
Mesure si la réponse est fondée sur le contexte récupéré (non halluciné).
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

## Études de cas réels
### Étude de cas 1 : Chatbot de support client
**Problème :** Le chatbot a donné des réponses incorrectes sur les fonctionnalités du produit.
**Analyse des causes profondes :**
- Regroupement des descriptions de fonctionnalités divisées au-delà des frontières
- Récupération d'informations partielles trouvées
- LLM halluciné détails manquants
**Solution :**
- Implémentation du chunking sémantique par sections de fonctionnalités
- Ajout d'un chevauchement de 150 jetons entre les morceaux
- Augmentation du top_k de 3 à 5
- Ajout d'une étape de reclassement
**Résultats :**
- Précision améliorée de 62% à 89%
- Le taux d'hallucinations est passé de 23% à 4%
- La satisfaction des clients a augmenté de 35%
### Étude de cas 2 : Recherche de documents juridiques
**Problème :** Les avocats n'ont pas pu trouver de précédents pertinents.
**Cause fondamentale :**
- Les intégrations génériques n'ont pas capturé la sémantique juridique
- Les requêtes de négation ont échoué ("cas où la responsabilité n'a PAS été établie")
- Pas de filtrage temporel pour les cas annulés
**Solution :**
- Intégrations fines sur le corpus juridique
- Implémentation de la gestion des négations
- Ajout de métadonnées et de filtrage sur l'état du cas
- Création d'une récupération multi-sauts pour les chaînes de citations
**Résultats :**
- Rappel@10 amélioré de 45 % à 78 %
- Temps de recherche réduit de 8s à 1,2s
- L'adoption par l'équipe juridique a été multipliée par 3
### Étude de cas 3 : Documentation technique
**Problème :** Les développeurs n'ont pas trouvé d'exemples de code.
**Cause fondamentale :**
- Blocs de code mal intégrés aux modèles texte uniquement
- Les requêtes telles que "comment authentifier" correspondaient à la théorie, pas aux exemples
- Aucune distinction entre les versions d'API
**Solution :**
- Modèle d'intégration compatible avec le code utilisé
- Morceaux balisés par type de contenu (concept, tutoriel, référence API, exemple)
- Ajout des métadonnées de version
- Implémentation de la classification d'intention pour le routage des requêtes
**Résultats :**
- Précision de récupération des exemples de code : 34 % → 82 %
- Délai de première requête réussie réduit de 60 %
- Le trafic de documentation a augmenté de 45 %