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
# RAG e falhas de pesquisa vetorial
Este documento consolida falhas comuns em sistemas de geração aumentada de recuperação (RAG), uso incorporado e implementações de pesquisa vetorial.
---

## Bad RAG (geração aumentada de recuperação)
A Geração Aumentada de Recuperação (RAG) combina sistemas de recuperação com IA generativa para produzir respostas mais precisas e contextualmente relevantes. Implementações RAG ruins sofrem com baixa qualidade de recuperação, tratamento inadequado de contexto ou problemas de geração.
### Estratégia de fragmentação deficiente
**Mau exemplo:**```python
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
- Frases e parágrafos são divididos arbitrariamente
- O contexto é perdido nos limites do bloco
- O significado semântico é fragmentado
- A recuperação retorna informações incompletas
**Melhor abordagem:**```python
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

### Sobreposição de contexto ausente
**Mau exemplo:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Melhor abordagem:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Ignorando a intenção de consulta
**Mau exemplo:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Melhor abordagem:**```python
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

### Estouro da janela de contexto
**Mau exemplo:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Melhor abordagem:**```python
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

## Incorporações ruins
Embeddings são representações vetoriais de dados que capturam significado semântico. Incorporações ruins resultam de seleção inadequada de modelos, treinamento inadequado ou uso impróprio.
### Modelo errado para domínio
**Mau exemplo:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Melhor abordagem:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Não normalizando vetores
**Mau exemplo:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Melhor abordagem:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Ignorando dimensões de incorporação
**Mau exemplo:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Melhor abordagem:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Pesquisa de vetor ruim
A pesquisa vetorial permite a pesquisa de similaridade semântica em embeddings de alta dimensão. Implementações ruins sofrem de configuração de índice inadequada, métricas de distância inadequadas ou problemas de escalabilidade.
### Métrica de distância errada
**Mau exemplo:**```python
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

**Por que é ruim:**
- A distância euclidiana é afetada pela magnitude do vetor
- Para vetores normalizados, a similaridade de cosseno (produto escalar) é apropriada
- Os resultados serão menos precisos para pesquisa semântica
**Melhor abordagem:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Otimização de índice ausente
**Mau exemplo:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Melhor abordagem:**```python
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

### Não tratando dados de alta dimensão
**Mau exemplo:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Melhor abordagem:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Ignorando a compensação entre recall e latência
**Mau exemplo:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Melhor abordagem:**```python
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

## Resumo das melhores práticas
### Sistemas RAG
1. **Pedaço estratégico**: respeite os limites semânticos, adicione sobreposição
2. **Considere a intenção de consulta**: adapte a recuperação com base no que o usuário deseja
3. **Gerenciar contexto**: Fique dentro dos limites de token LLM
4. **Avalie ponta a ponta**: teste o pipeline RAG completo, não apenas a recuperação
### Incorporações
1. **Escolha modelos apropriados ao domínio**: combine o modelo com o seu tipo de conteúdo
2. **Normalizar vetores**: essencial para similaridade de cossenos
3. **Consistência**: Use o mesmo modelo em todo o sistema
4. **Monitorar o desvio**: treinar novamente ou atualizar os embeddings à medida que os dados evoluem
### Pesquisa vetorial
1. **Selecione a métrica de distância correta**: COSINE para semântica, EUCLID para espacial
2. **Configurar índices**: use HNSW para grandes conjuntos de dados
3. **Parâmetros de ajuste**: equilibre recall versus latência para seu caso de uso
4. **Monitore o desempenho**: acompanhe a qualidade e a latência da pesquisa ao longo do tempo
---

## Tópicos Relacionados
- **Falhas de AI/LLM**: Consulte`ai_llm_failures.md`para alucinações e problemas de raciocínio
- **Design de Agente**: Consulte`../05_agents/agent_system_design.md`para construir agentes com RAG
- **Qualidade do conjunto de dados**: consulte`../08_machine_learning/ml_data_issues.md`para considerações sobre dados de treinamento
- **Engenharia de Prompt**: Consulte`../02_artificial_intelligence/prompt_engineering.md`para técnicas de manipulação de contexto
---

## Padrões avançados de falha RAG
### Perdido no Fenômeno Médio
**O que é:** LLMs tendem a se concentrar nas informações no início e no final do contexto, 
ignorando o conteúdo intermediário.
**Mau exemplo:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Por que é ruim:**
- Informações críticas em partes intermediárias podem ser ignoradas
- A atenção do modelo diminui para o conteúdo intermediário
- Desperdiça tokens em conteúdo recuperado irrelevante
**Mitigação:**```python
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

### Falhas de recuperação multi-hop
**O que é:** Falha ao recuperar informações que exigem várias peças conectadas.
**Mau exemplo:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Mitigação:**```python
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

### Falhas de raciocínio temporal
**O que é:** Os sistemas RAG enfrentam consultas urgentes e informações desatualizadas.
**Mau exemplo:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Mitigação:**```python
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

### Falhas no tratamento de negação
**O que é:** a pesquisa semântica muitas vezes perde negações nas consultas.
**Mau exemplo:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Mitigação:**```python
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

## Incorporando antipadrões
### Misturando modelos de incorporação
**O que é:** Usar modelos diferentes para indexação versus consulta quebra a similaridade.
**Mau exemplo:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Por que é ruim:**
- Diferentes modelos produzem incorporações em espaços vetoriais incompatíveis
- A similaridade de cosseno entre diferentes embeddings de modelos é ruído aleatório
- O sistema parece funcionar, mas retorna lixo
**Detecção:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Ignorando dimensões de incorporação
**O que é:** Não considera o impacto da incorporação da dimensão no desempenho.
**Compensações:**
| Dimensões | Prós | Contras | Caso de uso |
|------------|------|------|----------|
| Baixo (128-256) | Pesquisa rápida, menos memória | Representações menos matizadas | Tarefas simples, em grande escala |
| Médio (384-768) | Bom equilíbrio | Recursos moderados | Finalidade geral |
| Alto (1024+) | Representações ricas | Lento, que consome muita memória | Tarefas semânticas complexas |
**Mau exemplo:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Não manuseando tokens especiais
**O que é:** Falha ao lidar corretamente com URLs, códigos, números e caracteres especiais.
**Mau exemplo:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Mitigação:**```python
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

## Problemas de desempenho de pesquisa vetorial
### Problemas de escala
**O que é:** a qualidade ou latência da pesquisa diminui à medida que o conjunto de dados aumenta.
**Sintomas:**
- A latência aumenta linearmente com o tamanho do conjunto de dados
- A recuperação diminui à medida que mais vetores são adicionados
- O uso da memória explode
**Arquitetura ruim:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Solução Escalável:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Problema de inicialização a frio
**O que é:** Novos documentos não podem ser recuperados até que o índice seja reconstruído.
**Mau exemplo:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Solução: Indexação Incremental**```python
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

## Métricas de avaliação para RAG
### Precisão de Contexto
Mede quantos pedaços recuperados são realmente relevantes.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Relevância da resposta
Mede se a resposta gerada realmente aborda a consulta.
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

### Fidelidade
Mede se a resposta é baseada no contexto recuperado (não alucinado).
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

## Estudos de caso do mundo real
### Estudo de caso 1: Chatbot de suporte ao cliente
**Problema:** o chatbot deu respostas incorretas sobre os recursos do produto.
**Análise de causa raiz:**
- Divisão de descrições de recursos entre limites
- Recuperação de informações parciais encontradas
- LLM alucinado com detalhes faltantes
**Solução:**
- Implementação de segmentação semântica por seções de recursos
- Adicionada sobreposição de 150 tokens entre pedaços
- Aumento de top_k de 3 para 5
- Adicionada etapa de reclassificação
**Resultados:**
- Precisão melhorada de 62% para 89%
- A taxa de alucinações caiu de 23% para 4%
- A satisfação do cliente aumentou 35%
### Estudo de caso 2: Pesquisa de documentos legais
**Problema:** Os advogados não conseguiram encontrar precedentes relevantes.
**Causa raiz:**
- Os embeddings genéricos não capturaram a semântica legal
- Falha nas consultas de negação ("casos em que a responsabilidade NÃO foi estabelecida")
- Sem filtragem temporal para casos anulados
**Solução:**
- Incorporações ajustadas no corpus jurídico
- Implementado tratamento de negação
- Adicionados metadados e filtragem de status de caso
- Recuperação multi-hop construída para cadeias de citações
**Resultados:**
- Recall@10 melhorou de 45% para 78%
- Tempo de pesquisa reduzido de 8s para 1,2s
- A adoção pela equipe jurídica aumentou 3x
### Estudo de caso 3: Documentação técnica
**Problema:** os desenvolvedores não conseguiram encontrar exemplos de código.
**Causa raiz:**
- Blocos de código mal incorporados em modelos somente texto
- Consultas como "como autenticar" teoria correspondente, não exemplos
- Sem distinção entre versões da API
**Solução:**
- Modelo de incorporação com reconhecimento de código usado
- Pedaços marcados por tipo de conteúdo (conceito, tutorial, referência de API, exemplo)
- Adicionados metadados de versão
- Implementação de classificação de intenção para roteamento de consultas
**Resultados:**
- Precisão de recuperação de exemplo de código: 34% → 82%
- O tempo até a primeira consulta bem-sucedida foi reduzido em 60%
- O tráfego de documentação aumentou 45%