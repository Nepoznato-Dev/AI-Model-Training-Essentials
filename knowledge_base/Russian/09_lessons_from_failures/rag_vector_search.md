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

# RAG и ошибки поиска векторов
В этом документе собраны общие сведения о типичных сбоях в системах расширенной генерации (RAG), использовании встраивания и реализациях векторного поиска.
---

## Bad RAG (генерация с расширенным поиском)
Поисково-дополненная генерация (RAG) сочетает в себе поисковые системы с генеративным искусственным интеллектом для получения более точных и контекстуально релевантных ответов. Плохие реализации RAG страдают от низкого качества извлечения, неадекватной обработки контекста или проблем с генерацией.
### Плохая стратегия дробления
**Плохой пример:**```python
# Chunking by fixed character count regardless of content
def chunk_document(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Results in chunks that cut sentences mid-way
# "The quick brown fox jumps over the l" + "azy dog..."
```

**Проблемы:**
- Предложения и абзацы разделяются произвольно
- Контекст теряется на границах блоков.
- Семантическое значение фрагментировано
- Поиск возвращает неполную информацию.
**Лучший подход:**```python
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

### Отсутствует перекрытие контекста
**Плохой пример:**```python
# No overlap between chunks - context lost at boundaries
chunks = chunk_document(text, chunk_size=500, overlap=0)
```

**Лучший подход:**```python
# Add overlap to preserve context across chunk boundaries
chunks = chunk_document(text, chunk_size=500, overlap=100)
```

### Игнорирование намерения запроса
**Плохой пример:**```python
# Using same retrieval for all query types
def retrieve(query, documents):
    query_embedding = model.encode(query)
    return semantic_search(query_embedding, documents, top_k=5)
# Doesn't consider if user wants definition, example, comparison, etc.
```

**Лучший подход:**```python
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

### Переполнение контекстного окна
**Плохой пример:**```python
# Blindly concatenating all retrieved chunks
def build_context(retrieved_chunks):
    return '\n\n'.join([chunk.text for chunk in retrieved_chunks])
# May exceed LLM's context window limit
```

**Лучший подход:**```python
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

## Плохие встраивания
Вложения — это векторные представления данных, которые отражают семантическое значение. Плохое встраивание является результатом неправильного выбора модели, неадекватного обучения или неправильного использования.
### Неверная модель домена
**Плохой пример:**```python
# Using general-purpose embeddings for legal documents
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
legal_embeddings = model.encode(legal_contracts)

# Fails to capture legal terminology nuances
# "force majeure" and "act of god" may not be close
```

**Лучший подход:**```python
# Use domain-specific embedding model
model = SentenceTransformer('law-bert-base')  # Trained on legal corpus
legal_embeddings = model.encode(legal_contracts)
```

### Не нормализовать векторы
**Плохой пример:**```python
# Using raw embeddings without normalization
embeddings = model.encode(documents)
# Cosine similarity will be affected by vector magnitude
```

**Лучший подход:**```python
from sklearn.preprocessing import normalize

embeddings = model.encode(documents)
embeddings_normalized = normalize(embeddings)  # L2 normalization
# Now cosine similarity works correctly
```

### Игнорирование внедренных размеров
**Плохой пример:**```python
# Mixing embeddings from different models
embedding1 = model_768.encode(text1)  # 768 dimensions
embedding2 = model_384.encode(text2)  # 384 dimensions
similarity = cosine_similarity(embedding1, embedding2)  # ERROR!
```

**Лучший подход:**```python
# Always use the same model for all embeddings in a system
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
similarity = cosine_similarity(embedding1, embedding2)
```

---

## Поиск неверных векторов
Векторный поиск обеспечивает поиск семантического сходства в многомерных вложениях. Плохие реализации страдают от плохой конфигурации индекса, неподходящих показателей расстояния или проблем с масштабируемостью.
### Неправильная метрика расстояния
**Плохой пример:**```python
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

**Почему это плохо:**
- Евклидово расстояние зависит от величины вектора
- Для нормализованных векторов подходит косинусное сходство (скалярное произведение).
- Результаты будут менее точными при семантическом поиске.
**Лучший подход:**```python
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(
        size=768,
        distance=models.Distance.COSINE  # Correct for semantic search
    )
)
```

### Отсутствует оптимизация индекса
**Плохой пример:**```python
# No index configuration - slow searches at scale
client.create_collection(
    collection_name="docs",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE)
)
# Will do brute-force search - O(n) complexity
```

**Лучший подход:**```python
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

### Не обработка многомерных данных
**Плохой пример:**```python
# Using very high-dimensional embeddings without consideration
embeddings = model.encode(documents)  # 4096 dimensions
# Curse of dimensionality makes all distances similar
```

**Лучший подход:**```python
# Use dimensionality reduction or choose appropriate embedding size
from sklearn.decomposition import PCA

embeddings = model.encode(documents)  # 4096 dimensions
pca = PCA(n_components=256)
embeddings_reduced = pca.fit_transform(embeddings)  # 256 dimensions
# Better distance discrimination, faster search
```

### Игнорирование компромисса между отзывом и задержкой
**Плохой пример:**```python
# Always using default search parameters
results = client.search(collection_name="docs", query_vector=query, limit=10)
# May be too slow or inaccurate for your use case
```

**Лучший подход:**```python
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

## Сводка лучших практик
### Тряпочные системы
1. **Стратегическое разделение**: соблюдайте семантические границы, добавляйте дублирование
2. **Учитывайте цель запроса**: адаптируйте поиск в соответствии с желаниями пользователя.
3. **Управление контекстом**: оставайтесь в рамках ограничений токена LLM.
4. **Оцените комплексную оценку**: протестируйте весь конвейер RAG, а не только извлечение данных.
### Вложения
1. **Выберите модели, соответствующие предметной области**: сопоставьте модель с вашим типом контента.
2. **Нормализация векторов**: необходимо для косинусного сходства.
3. **Последовательность**: используйте одну и ту же модель во всей системе.
4. **Отслеживание дрейфа**: переобучайте или обновляйте встраивания по мере развития данных.
### Векторный поиск
1. **Выберите метрику правильного расстояния**: COSINE для семантики, EUCLID для пространственного
2. **Настройка индексов**: используйте HNSW для больших наборов данных.
3. **Настройте параметры**: возврат баланса и задержку для вашего варианта использования.
4. **Отслеживание производительности**: отслеживайте качество поиска и задержку с течением времени.
---

## Похожие темы
- **Ошибки AI/LLM**: информацию о галлюцинациях и проблемах с рассуждением см. в `ai_llm_failures.md`.
- **Проектирование агента**: см.`../05_agents/agent_system_design.md`для создания агентов с помощью RAG.
- **Качество набора данных**: сведения об обучении данных см. в `../08_machine_learning/ml_data_issues.md`.
- **Быстрое проектирование**: см.`../02_artificial_intelligence/prompt_engineering.md`для получения информации о методах обработки контекста.
---

## Расширенные шаблоны ошибок RAG
### Затерянный посреди феномена
**Что это такое:** Магистр права, как правило, фокусируется на информации в начале и конце контекста, 
игнорируя средний контент.
**Плохой пример:**```python
# Retrieving 10 chunks and concatenating all
context = "\n\n".join(retrieved_chunks)  # 10,000+ tokens
response = llm.generate(query, context)

# Information in chunk 4-7 often ignored
```

**Почему это плохо:**
- Критическая информация в средних фрагментах может быть упущена из виду.
- Внимание модели снижается при среднем содержании.
- Тратить токены на нерелевантный полученный контент.
**Устранение последствий:**```python
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

### Ошибки многопрыжкового извлечения
**Что это такое:** Не удалось получить информацию, требующую нескольких связанных частей.
**Плохой пример:**```markdown
Query: "What programming language did the creator of Python work on before Python?"

Single-hop retrieval finds:
- "Guido van Rossum created Python"
- "He worked at CWI"

But misses:
- "At CWI, he worked on the ABC language"
- "ABC influenced Python's design"

Result: Incomplete answer
```

**Устранение последствий:**```python
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

### Ошибки временного рассуждения
**Что это такое:** RAG-системы борются с срочными запросами и устаревшей информацией.
**Плохой пример:**```markdown
Query: "What is the latest version of Django?"

Retrieved chunk (from 2022): "Django 4.0 is the latest LTS release"

Model responds: "Django 4.0 is the latest version"

Reality: Django 5.0 was released in 2026
```

**Устранение последствий:**```python
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

### Сбои обработки отрицаний
**Что это такое.** Семантический поиск часто пропускает отрицания в запросах.
**Плохой пример:**```markdown
Query: "What frameworks don't require TypeScript?"

Vector search retrieves:
- "React works well with TypeScript"  ❌ (opposite meaning!)
- "TypeScript support in Vue.js"      ❌

Misses:
- "Vanilla JavaScript frameworks"     ✓
- "Python web frameworks"             ✓
```

**Устранение последствий:**```python
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

## Встраивание анти-шаблонов
### Смешивание моделей внедрения
**Что это такое.** Использование разных моделей индексирования и запросов нарушает сходство.
**Плохой пример:**```python
# Indexing with model A
index_embeddings = model_A.encode(documents)
vector_db.add(index_embeddings)

# Querying with model B  
query_embedding = model_B.encode(query)  # WRONG!
results = vector_db.search(query_embedding)

# Results are meaningless - different vector spaces!
```

**Почему это плохо:**
- Различные модели создают вложения в несовместимые векторные пространства.
- Косинусное сходство между различными вложениями моделей представляет собой случайный шум.
- Система работает, но возвращает мусор
**Обнаружение:**```python
# Test embedding compatibility
test_doc = "This is a test document"
emb_1 = model_A.encode(test_doc)
emb_2 = model_B.encode(test_doc)

similarity = cosine_similarity(emb_1, emb_2)
if similarity < 0.8:  # Should be very high for same text
    print("WARNING: Embedding models are incompatible!")
```

### Игнорирование внедренных размеров
**Что это такое:** не учитывается влияние внедрения размеров на производительность.
**Компромиссы:**
| Размеры | Плюсы | Минусы | Вариант использования |
|------------|------|------|----------|
| Низкий (128-256) | Быстрый поиск, меньше памяти | Меньше нюансов | Простые задачи, масштабные |
| Средний (384-768) | Хороший баланс | Умеренные ресурсы | Общего назначения |
| Высокий (1024+) | Богатые представления | Медленный, требовательный к памяти | Сложные смысловые задачи |
**Плохой пример:**```python
# Using 1024-dim embeddings for simple keyword-like search
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims
# Overkill for "find documents mentioning 'invoice'"

# Or using 128-dim for complex reasoning
model = TinyEmbedding(128)
# Insufficient for nuanced semantic understanding
```

### Не обрабатываются специальные токены
**Что это такое:** Невозможно правильно обрабатывать URL-адреса, коды, цифры и специальные символы.
**Плохой пример:**```python
# Embedding URLs without preprocessing
url = "https://api.example.com/v2/users?id=123&token=abc"
embedding = model.encode(url)
# Model may not understand URL structure

# Embedding code without context
code = "def foo(x): return x + 1"
embedding = model.encode(code)
# Generic model doesn't understand programming semantics
```

**Устранение последствий:**```python
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

## Проблемы с производительностью векторного поиска
### Проблемы с масштабированием
**Что это такое?** Качество поиска или задержка ухудшаются по мере роста набора данных.
**Симптомы:**
- Задержка увеличивается линейно с размером набора данных.
- Восстановление падает по мере добавления новых векторов.
- Использование памяти резко возрастает
**Плохая архитектура:**```python
# Brute-force search on growing dataset
def search(query, all_vectors):
    similarities = []
    for vector in all_vectors:  # O(n) - gets slower as n grows
        sim = cosine_similarity(query, vector)
        similarities.append(sim)
    return top_k(similarities)
```

**Масштабируемое решение:**```python
# Use approximate nearest neighbor (ANN) index
import hnswlib

# Build index once
index = hnswlib.Index(space='cosine', dim=768)
index.init_index(max_elements=1000000, ef_construction=200, M=16)
index.add_items(vectors, ids)

# Search is now O(log n) instead of O(n)
labels, distances = index.knn_query(query_vector, k=10)
```

### Проблема холодного запуска
**Что это такое.** Новые документы невозможно получить, пока индекс не будет перестроен.
**Плохой пример:**```python
# Batch indexing - rebuild entire index nightly
def nightly_job():
    all_docs = fetch_all_documents()
    embeddings = compute_embeddings(all_docs)
    vector_db.rebuild_index(embeddings)  # Takes hours
    
# Documents added during day aren't searchable until next morning
```

**Решение: добавочное индексирование**```python
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

## Метрики оценки для RAG
### Точность контекста
Измеряет, сколько извлеченных фрагментов действительно актуально.
```python
def context_precision(retrieved_chunks, relevant_chunks):
    """
    retrieved_chunks: List of chunks returned by retrieval
    relevant_chunks: Set of chunks that should have been retrieved
    """
    relevant_retrieved = sum(1 for c in retrieved_chunks if c in relevant_chunks)
    return relevant_retrieved / len(retrieved_chunks) if retrieved_chunks else 0
```

### Ответ Релевантность
Измеряет, действительно ли сгенерированный ответ соответствует запросу.
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

### Верность
Определяет, основан ли ответ на полученном контексте (не на галлюцинациях).
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

## Практические примеры
### Пример 1: Чат-бот службы поддержки клиентов
**Проблема:** Чат-бот давал неправильные ответы о функциях продукта.
**Анализ первопричин:**
- Разделение описаний объектов на части по границам.
- Поиск найденной частичной информации
- LLM галлюцинировал недостающие детали
**Решение:**
- Реализовано семантическое разделение по разделам функций.
- Добавлено перекрытие в 150 токенов между чанками.
- Увеличен top_k с 3 до 5.
- Добавлен этап повторного ранжирования
**Результаты:**
- Точность улучшена с 62% до 89%.
- Уровень галлюцинаций снижен с 23% до 4%.
- Удовлетворенность клиентов выросла на 35 %
### Пример 2: Поиск юридических документов
**Проблема:** Юристам не удалось найти соответствующие прецеденты.
**Основная причина:**
- Общие вложения не отражают юридическую семантику.
- Не удалось выполнить отрицательные запросы («случаи, когда ответственность НЕ была установлена»)
- Нет временной фильтрации для отмененных дел.
**Решение:**
- Точные встраивания в юридический корпус.
- Реализована обработка отрицаний.
- Добавлены метаданные статуса дела и фильтрация.
- Встроенный многошаговый поиск для цепочек цитирования.
**Результаты:**
- Recall@10 улучшен с 45% до 78%.
- Время поиска уменьшено с 8 до 1,2 с.
- Принятие командой юристов увеличилось в 3 раза.
### Пример 3: Техническая документация
**Проблема.** Разработчики не смогли найти примеры кода.
**Основная причина:**
- Блоки кода плохо встроены в текстовые модели.
– Запросы типа «как аутентифицировать» соответствуют теории, а не примерам.
- Нет различия между версиями API.
**Решение:**
- Используемая модель внедрения с учетом кода.
- Отмечены фрагменты по типу контента (концепция, руководство, справочник по API, пример).
- Добавлены метаданные версии
- Реализована классификация намерений для маршрутизации запросов.
**Результаты:**
- Точность поиска примера кода: 34% → 82%
- Время до первого успешного запроса сокращено на 60 %.
- Трафик документации увеличился на 45 %.