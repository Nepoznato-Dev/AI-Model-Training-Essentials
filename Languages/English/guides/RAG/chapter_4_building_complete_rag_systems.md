# Chapter 4: Building Complete RAG Systems

## 4.1 Introduction to End-to-End RAG Pipelines

Now that we've covered both retrievers (Chapter 3) and generators (Chapter 5), it's time to bring them together into a complete Retrieval-Augmented Generation system. This chapter focuses on the integration challenges and practical considerations that arise when combining these components.

### Why Integration Matters

You might think: "If I have a good retriever and a good generator, combining them should be straightforward." Unfortunately, it's not quite that simple. Here's why:

1. **Component Mismatch**: A retriever optimized for dense similarity might retrieve documents that don't align well with your generator's training format
2. **Error Propagation**: Mistakes in retrieval cascade into generation errors
3. **Latency Concerns**: The combined system must meet real-time requirements
4. **Resource Management**: Memory and compute need to be balanced across components

Think of building a RAG system like assembling a relay team: even if you have the fastest individual runners, they need to pass the baton smoothly to win.

### What This Chapter Covers

We'll walk through:
- How to connect retrievers and generators effectively
- Strategies for handling retrieval failures
- Techniques for optimizing the full pipeline
- Real-world deployment patterns
- Monitoring and debugging approaches

Let's start by understanding the basic architecture.

## 4.2 Basic RAG Architecture

### The Standard Pipeline

A typical RAG system follows this flow:

```
User Query → Retriever → Top-K Documents → Generator → Response
                ↓                              ↑
           Document Index              Context Processing
```

Each arrow represents a potential failure point or optimization opportunity. Let's break down each component:

**1. Query Processing**: Before retrieval, queries often need preprocessing (spelling correction, query expansion, etc.)

**2. Retrieval**: The retriever searches the document index for relevant content

**3. Re-ranking** (Optional): A cross-encoder can re-rank retrieved documents for better quality

**4. Context Selection**: Not all retrieved documents should be passed to the generator—context window limits matter

**5. Generation**: The generator produces a response conditioned on the query and selected context

**6. Post-processing**: Output validation, formatting, and safety checks

Here's a basic implementation that connects these pieces:

```python
from typing import List, Dict, Optional
import torch

class SimpleRAGSystem:
    """
    A minimal end-to-end RAG system connecting retriever and generator.
    
    This implementation shows the basic data flow without advanced optimizations.
    """
    
    def __init__(self, retriever, generator, tokenizer, k: int = 5):
        """
        Initialize the RAG system.
        
        Args:
            retriever: A trained bi-encoder retriever with encode_query method
            generator: A trained sequence-to-sequence model
            tokenizer: Tokenizer compatible with the generator
            k: Number of documents to retrieve
        """
        self.retriever = retriever
        self.generator = generator
        self.tokenizer = tokenizer
        self.k = k
        
    def retrieve(self, query: str, document_index, document_texts: List[str]) -> List[str]:
        """
        Retrieve top-k documents for a query.
        
        Args:
            query: User's question
            document_index: FAISS index or similar with pre-computed embeddings
            document_texts: Full list of documents (for returning text)
            
        Returns:
            List of top-k document texts
        """
        # Encode the query
        query_embedding = self.retriever.encode_query([query])
        query_embedding = query_embedding.cpu().numpy()
        
        # Search the index
        import faiss
        faiss.normalize_L2(query_embedding)
        distances, indices = document_index.search(query_embedding, self.k)
        
        # Return the actual document texts
        retrieved_docs = [document_texts[idx] for idx in indices[0]]
        
        return retrieved_docs
    
    def generate_response(self, query: str, contexts: List[str]) -> str:
        """
        Generate a response given query and retrieved contexts.
        
        Args:
            query: User's question
            contexts: List of retrieved document texts
            
        Returns:
            Generated response string
        """
        # Prepare input for generator
        context_text = ' '.join(contexts)
        input_text = f"Question: {query}\nContext: {context_text}\nAnswer:"
        
        # Tokenize
        inputs = self.tokenizer(
            input_text,
            return_tensors='pt',
            truncation=True,
            max_length=2048
        )
        
        # Generate
        with torch.no_grad():
            outputs = self.generator.generate(
                **inputs,
                max_length=256,
                num_beams=4,
                early_stopping=True
            )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    
    def answer(self, query: str, document_index, document_texts: List[str]) -> str:
        """
        Complete RAG pipeline: retrieve then generate.
        
        Args:
            query: User's question
            document_index: Pre-built document index
            document_texts: List of all documents
            
        Returns:
            Final answer string
        """
        # Step 1: Retrieve relevant documents
        contexts = self.retrieve(query, document_index, document_texts)
        
        # Step 2: Generate answer using retrieved context
        answer = self.generate_response(query, contexts)
        
        return answer
```

This basic structure works, but production systems need more sophistication. Let's explore the key enhancements.

## 4.3 Handling Retrieval Failures

One of the most common issues in RAG systems is when retrieval fails—either returning irrelevant documents or no documents at all. How should your system respond?

### Types of Retrieval Failures

**1. Low Confidence Retrievals**: The retriever returns documents, but similarity scores are very low

**2. Empty Results**: No documents meet the similarity threshold

**3. Contradictory Context**: Retrieved documents contain conflicting information

**4. Off-Topic Results**: Documents are tangentially related but don't help answer the query

### Detection Strategies

Before we can handle failures, we need to detect them:

```python
class RetrievalQualityChecker:
    """
    Detects when retrieval results are poor quality.
    """
    
    def __init__(self, similarity_threshold: float = 0.3):
        self.similarity_threshold = similarity_threshold
    
    def check_retrieval_quality(
        self, 
        query: str, 
        retrieved_docs: List[str], 
        similarity_scores: List[float]
    ) -> Dict:
        """
        Assess the quality of retrieval results.
        
        Returns a dictionary with quality metrics and flags.
        """
        quality_report = {
            'num_docs': len(retrieved_docs),
            'avg_similarity': sum(similarity_scores) / len(similarity_scores) if similarity_scores else 0,
            'max_similarity': max(similarity_scores) if similarity_scores else 0,
            'is_low_confidence': False,
            'is_empty': False,
            'recommendation': 'proceed'
        }
        
        # Check for empty results
        if len(retrieved_docs) == 0:
            quality_report['is_empty'] = True
            quality_report['recommendation'] = 'fallback'
            return quality_report
        
        # Check for low confidence
        if quality_report['max_similarity'] < self.similarity_threshold:
            quality_report['is_low_confidence'] = True
            quality_report['recommendation'] = 'warn_or_fallback'
        
        # Check for very short or degenerate documents
        doc_lengths = [len(doc.split()) for doc in retrieved_docs]
        if min(doc_lengths) < 10:
            quality_report['has_degenerate_docs'] = True
            quality_report['recommendation'] = 'filter_and_proceed'
        
        return quality_report
```

### Fallback Strategies

Once you detect poor retrieval, what should you do? Here are several strategies:

**Strategy 1: Graceful Degradation**
When retrieval fails, let the generator answer from its parametric knowledge—but warn the user.

```python
def answer_with_fallback(self, query: str, document_index, document_texts: List[str]) -> str:
    """
    Answer with fallback when retrieval quality is poor.
    """
    # Try retrieval
    contexts, scores = self.retrieve_with_scores(query, document_index, document_texts)
    
    # Check quality
    quality = self.quality_checker.check_retrieval_quality(query, contexts, scores)
    
    if quality['recommendation'] == 'fallback':
        # Use generator's internal knowledge
        return self.generate_without_context(query, include_warning=True)
    
    elif quality['recommendation'] == 'warn_or_fallback':
        # Proceed but warn user about uncertainty
        answer = self.generate_response(query, contexts)
        return f"[Note: Limited relevant information found] {answer}"
    
    else:
        # Normal case: proceed with retrieved context
        return self.generate_response(query, contexts)
```

**Strategy 2: Query Reformulation**
If initial retrieval fails, try rephrasing the query:

```python
def reformulate_and_retry(
    self, 
    query: str, 
    document_index, 
    document_texts: List[str],
    max_retries: int = 2
) -> List[str]:
    """
    Attempt retrieval with query reformulation if initial attempt fails.
    """
    from transformers import pipeline
    
    # Initialize paraphraser
    paraphraser = pipeline("text2text-generation", model="t5-base")
    
    current_query = query
    
    for attempt in range(max_retries + 1):
        # Try retrieval
        contexts, scores = self.retrieve_with_scores(
            current_query, document_index, document_texts
        )
        
        quality = self.quality_checker.check_retrieval_quality(
            current_query, contexts, scores
        )
        
        # If quality is acceptable, return
        if quality['recommendation'] == 'proceed':
            return contexts
        
        # Otherwise, reformulate and retry
        if attempt < max_retries:
            paraphrased = paraphraser(
                f"paraphrase: {current_query}",
                max_length=64
            )[0]['generated_text']
            
            print(f"Reformulating query: '{current_query}' → '{paraphrased}'")
            current_query = paraphrased
    
    # Return best available results even if poor
    return contexts if contexts else []
```

**Strategy 3: Hybrid Retrieval**
Combine dense and sparse retrieval to improve coverage:

```python
def hybrid_retrieve(
    self, 
    query: str, 
    dense_index, 
    sparse_index,  # BM25 index
    document_texts: List[str],
    dense_weight: float = 0.7,
    sparse_weight: float = 0.3,
    top_k: int = 10
) -> List[str]:
    """
    Combine dense and sparse retrieval for better coverage.
    """
    # Dense retrieval
    dense_results = self.dense_retrieve(query, dense_index, document_texts, k=top_k * 2)
    
    # Sparse retrieval (BM25)
    sparse_results = self.sparse_retrieve(query, sparse_index, document_texts, k=top_k * 2)
    
    # Reciprocal Rank Fusion
    fused_scores = {}
    
    for rank, doc_idx in enumerate(dense_results['indices']):
        score = dense_results['scores'][rank]
        fused_scores[doc_idx] = fused_scores.get(doc_idx, 0) + dense_weight * score
    
    for rank, doc_idx in enumerate(sparse_results['indices']):
        score = sparse_results['scores'][rank]
        fused_scores[doc_idx] = fused_scores.get(doc_idx, 0) + sparse_weight * score
    
    # Sort by fused score
    sorted_docs = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
    top_indices = [idx for idx, _ in sorted_docs[:top_k]]
    
    return [document_texts[idx] for idx in top_indices]
```

## 4.4 Context Window Management

Modern language models have limited context windows. When retrieved documents exceed this limit, you need smart selection strategies.

### The Problem

Suppose your generator accepts 2048 tokens, but:
- Your query takes ~50 tokens
- Each retrieved document averages 512 tokens
- You retrieved 10 documents (5120 tokens total)

You can't fit everything. What do you do?

### Strategy 1: Truncation

The simplest approach: take as many complete documents as fit, then truncate the last one.

```python
def truncate_to_fit(
    self, 
    query: str, 
    contexts: List[str], 
    max_tokens: int = 2048
) -> str:
    """
    Select and truncate contexts to fit within token limit.
    """
    # Reserve space for query and prompt template
    reserved_tokens = 200  # For query, instructions, etc.
    available_tokens = max_tokens - reserved_tokens
    
    # Count tokens in each context
    context_tokens = []
    for ctx in contexts:
        token_count = len(self.tokenizer.encode(ctx))
        context_tokens.append((ctx, token_count))
    
    # Greedily add contexts until we run out of space
    selected_contexts = []
    used_tokens = 0
    
    for ctx, count in context_tokens:
        if used_tokens + count <= available_tokens:
            selected_contexts.append(ctx)
            used_tokens += count
        else:
            # Truncate this context to fit remaining space
            remaining = available_tokens - used_tokens
            if remaining > 50:  # Only if we have meaningful space left
                truncated = self.truncate_document(ctx, remaining)
                selected_contexts.append(truncated)
            break
    
    return ' '.join(selected_contexts)

def truncate_document(self, document: str, max_tokens: int) -> str:
    """Truncate a document to max_tokens while preserving sentence boundaries."""
    tokens = self.tokenizer.encode(document)
    
    if len(tokens) <= max_tokens:
        return document
    
    # Truncate tokens
    truncated_tokens = tokens[:max_tokens]
    
    # Decode back to text
    truncated_text = self.tokenizer.decode(truncated_tokens, skip_special_tokens=True)
    
    # Optionally cut at last sentence boundary
    last_period = truncated_text.rfind('.')
    if last_period > max_tokens * 3:  # Only if we don't lose too much
        truncated_text = truncated_text[:last_period + 1]
    
    return truncated_text
```

### Strategy 2: Importance-Based Selection

Instead of taking documents in retrieval order, score them by importance to the query:

```python
def select_most_relevant(
    self, 
    query: str, 
    contexts: List[str], 
    relevance_scores: List[float],
    max_tokens: int = 2048
) -> str:
    """
    Select contexts based on relevance scores rather than retrieval order.
    """
    # Pair contexts with their scores
    scored_contexts = list(zip(contexts, relevance_scores))
    
    # Sort by relevance (highest first)
    scored_contexts.sort(key=lambda x: x[1], reverse=True)
    
    # Now fill context window with most relevant first
    selected = []
    used_tokens = 0
    reserved_tokens = 200
    available_tokens = max_tokens - reserved_tokens
    
    for ctx, score in scored_contexts:
        token_count = len(self.tokenizer.encode(ctx))
        
        if used_tokens + token_count <= available_tokens:
            selected.append(ctx)
            used_tokens += token_count
        else:
            break
    
    return ' '.join(selected)
```

### Strategy 3: Hierarchical Summarization

For very long documents, summarize before including in context:

```python
def hierarchical_context_compression(
    self, 
    query: str, 
    contexts: List[str], 
    max_tokens: int = 2048
) -> str:
    """
    Compress contexts by summarizing less relevant portions.
    """
    from transformers import pipeline
    
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # First, estimate total tokens
    total_tokens = sum(len(self.tokenizer.encode(ctx)) for ctx in contexts)
    
    if total_tokens <= max_tokens - 200:
        return ' '.join(contexts)
    
    # Need to compress: summarize longer contexts
    compressed_contexts = []
    
    for ctx in contexts:
        ctx_tokens = len(self.tokenizer.encode(ctx))
        
        # If this context is very long, summarize it
        if ctx_tokens > 300:
            summary = summarizer(
                ctx, 
                max_length=100, 
                min_length=50, 
                do_sample=False
            )[0]['summary_text']
            compressed_contexts.append(summary)
        else:
            compressed_contexts.append(ctx)
    
    # If still too long, apply truncation
    final_context = self.truncate_to_fit(query, compressed_contexts, max_tokens)
    
    return final_context
```

## 4.5 Latency Optimization

Real-world RAG systems need to respond quickly. Let's discuss optimization techniques.

### Profiling Your Pipeline

Before optimizing, measure where time is spent:

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label: str):
    """Context manager for timing code blocks."""
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"{label}: {end - start:.3f}s")

class ProfiledRAGSystem(SimpleRAGSystem):
    """RAG system with built-in profiling."""
    
    def answer(self, query: str, document_index, document_texts: List[str]) -> str:
        with timer("Total"):
            with timer("Retrieval"):
                contexts = self.retrieve(query, document_index, document_texts)
            
            with timer("Context Processing"):
                processed_context = self.truncate_to_fit(query, contexts)
            
            with timer("Generation"):
                answer = self.generate_response(query, [processed_context])
            
            return answer
```

Typical breakdown:
- **Retrieval**: 10-100ms (depends on index size)
- **Context Processing**: 5-20ms
- **Generation**: 100-1000ms (depends on model size and output length)

### Optimization Techniques

**1. Parallel Processing**

When retrieving multiple candidates or generating multiple responses:

```python
from concurrent.futures import ThreadPoolExecutor

def parallel_retrieve(
    self, 
    queries: List[str], 
    document_index, 
    document_texts: List[str],
    max_workers: int = 4
) -> List[List[str]]:
    """Retrieve for multiple queries in parallel."""
    
    def single_retrieve(query):
        return self.retrieve(query, document_index, document_texts)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(single_retrieve, queries))
    
    return results
```

**2. Caching**

Cache frequent queries and their results:

```python
from functools import lru_cache
import hashlib

class CachedRAGSystem(SimpleRAGSystem):
    """RAG system with query caching."""
    
    def __init__(self, *args, cache_size: int = 1000, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_size = cache_size
        self._cache = {}
    
    def _hash_query(self, query: str) -> str:
        """Create hash for query lookup."""
        return hashlib.md5(query.encode()).hexdigest()
    
    def answer(self, query: str, document_index, document_texts: List[str]) -> str:
        query_hash = self._hash_query(query)
        
        # Check cache
        if query_hash in self._cache:
            print("Cache hit!")
            return self._cache[query_hash]
        
        # Compute answer
        answer = super().answer(query, document_index, document_texts)
        
        # Store in cache (with simple LRU eviction)
        if len(self._cache) >= self.cache_size:
            # Remove oldest entry
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        
        self._cache[query_hash] = answer
        
        return answer
```

**3. Batched Generation**

When handling multiple queries, batch them for efficient GPU utilization:

```python
def batch_generate(
    self, 
    queries: List[str], 
    contexts_list: List[List[str]], 
    batch_size: int = 8
) -> List[str]:
    """Generate answers for multiple queries in batches."""
    all_answers = []
    
    for i in range(0, len(queries), batch_size):
        batch_queries = queries[i:i + batch_size]
        batch_contexts = contexts_list[i:i + batch_size]
        
        # Prepare batch inputs
        batch_inputs = []
        for query, contexts in zip(batch_queries, batch_contexts):
            context_text = ' '.join(contexts)
            input_text = f"Question: {query}\nContext: {context_text}\nAnswer:"
            batch_inputs.append(input_text)
        
        # Tokenize batch
        encoded = self.tokenizer(
            batch_inputs,
            return_tensors='pt',
            padding=True,
            truncation=True,
            max_length=2048
        ).to(self.generator.device)
        
        # Generate batch
        with torch.no_grad():
            outputs = self.generator.generate(
                **encoded,
                max_length=256,
                num_beams=4,
                early_stopping=True
            )
        
        # Decode batch
        batch_answers = [
            self.tokenizer.decode(output, skip_special_tokens=True)
            for output in outputs
        ]
        
        all_answers.extend(batch_answers)
    
    return all_answers
```

## 4.6 Evaluation of Complete RAG Systems

Evaluating RAG systems requires measuring both retrieval quality and generation quality—and how they interact.

### Component-wise Evaluation

First, evaluate each component separately:

**Retrieval Metrics:**
- **Recall@K**: Fraction of relevant documents in top-K results
- **MRR (Mean Reciprocal Rank)**: Average inverse rank of first relevant document
- **NDCG**: Normalized Discounted Cumulative Gain

**Generation Metrics:**
- **ROUGE/BLEU**: N-gram overlap with reference answers
- **BERTScore**: Semantic similarity using BERT embeddings
- **Faithfulness**: How much of the output is supported by context

### End-to-End Metrics

More importantly, measure the complete system:

```python
class RAGEvaluationSuite:
    """Comprehensive evaluation for complete RAG systems."""
    
    def __init__(self):
        from evaluate import load
        self.rouge = load('rouge')
        self.bertscore = load('bertscore')
    
    def evaluate_end_to_end(
        self,
        rag_system,
        test_queries: List[str],
        test_documents: List[str],
        ground_truth_answers: List[str],
        ground_truth_doc_indices: List[List[int]]
    ) -> Dict:
        """
        Evaluate complete RAG system.
        
        Args:
            rag_system: The RAG system to evaluate
            test_queries: Test questions
            test_documents: Document corpus
            ground_truth_answers: Reference answers
            ground_truth_doc_indices: Which documents are relevant for each query
            
        Returns:
            Dictionary of metrics
        """
        predictions = []
        retrieval_recalls = []
        
        for query, true_indices in zip(test_queries, ground_truth_doc_indices):
            # Get prediction
            answer = rag_system.answer(query, rag_system.doc_index, test_documents)
            predictions.append(answer)
            
            # Check if retrieval got relevant docs
            # (This assumes rag_system exposes retrieved indices)
            retrieved_indices = rag_system.last_retrieved_indices
            recall = len(set(retrieved_indices) & set(true_indices)) / len(true_indices)
            retrieval_recalls.append(recall)
        
        # Generation metrics
        rouge_scores = self.rouge.compute(predictions=predictions, references=ground_truth_answers)
        
        bertscore_results = self.bertscore.compute(
            predictions=predictions,
            references=ground_truth_answers,
            lang='en'
        )
        
        # Faithfulness metric
        faithfulness_scores = self.evaluate_faithfulness(
            predictions, test_documents, ground_truth_doc_indices
        )
        
        return {
            'generation_rouge1': rouge_scores['rouge1'],
            'generation_rougeL': rouge_scores['rougeL'],
            'generation_bertscore_f1': sum(bertscore_results['f1']) / len(bertscore_results['f1']),
            'retrieval_recall': sum(retrieval_recalls) / len(retrieval_recalls),
            'faithfulness': sum(faithfulness_scores) / len(faithfulness_scores),
            'predictions': predictions
        }
    
    def evaluate_faithfulness(
        self,
        predictions: List[str],
        documents: List[str],
        relevant_indices: List[List[int]]
    ) -> List[float]:
        """
        Measure how much of each prediction is supported by retrieved context.
        """
        from nltk import word_tokenize
        
        faithfulness_scores = []
        
        for pred, indices in zip(predictions, relevant_indices):
            # Combine relevant documents
            relevant_docs = ' '.join([documents[i] for i in indices])
            
            pred_tokens = set(word_tokenize(pred.lower()))
            context_tokens = set(word_tokenize(relevant_docs.lower()))
            
            # Ratio of prediction tokens found in context
            if len(pred_tokens) == 0:
                faithfulness_scores.append(0)
            else:
                overlap = len(pred_tokens & context_tokens)
                faithfulness_scores.append(overlap / len(pred_tokens))
        
        return faithfulness_scores
```

### Human Evaluation

Automated metrics don't tell the whole story. Consider human evaluation for:

- **Answer Relevance**: Does the answer actually address the question?
- **Factual Accuracy**: Is the information correct?
- **Coherence**: Is the response well-written and natural?
- **Helpfulness**: Would a user find this useful?

Create a simple rating form:

```python
evaluation_template = """
Query: {query}
Generated Answer: {answer}
Ground Truth: {ground_truth}

Please rate (1-5):
- Relevance: ___
- Accuracy: ___
- Coherence: ___
- Overall Quality: ___

Comments: ________________________________
"""
```

## 4.7 Debugging RAG Systems

When your RAG system produces poor outputs, systematic debugging helps identify the root cause.

### Debugging Checklist

**Step 1: Check Retrieval**
```python
def debug_retrieval(rag_system, query: str, document_texts: List[str]):
    """Inspect what was retrieved for a query."""
    contexts, scores = rag_system.retrieve_with_scores(
        query, rag_system.doc_index, document_texts
    )
    
    print(f"Query: {query}")
    print(f"\nRetrieved {len(contexts)} documents:")
    
    for i, (ctx, score) in enumerate(zip(contexts, scores)):
        print(f"\n[Doc {i}] Score: {score:.3f}")
        print(f"Preview: {ctx[:200]}...")
```

**Step 2: Check Context Processing**
```python
def debug_context_processing(rag_system, query: str, contexts: List[str]):
    """See what context actually reaches the generator."""
    processed = rag_system.truncate_to_fit(query, contexts)
    
    print(f"Original contexts: {len(contexts)} documents")
    print(f"Total original tokens: {sum(len(rag_system.tokenizer.encode(c)) for c in contexts)}")
    print(f"\nProcessed context tokens: {len(rag_system.tokenizer.encode(processed))}")
    print(f"\nProcessed context preview:\n{processed[:500]}...")
```

**Step 3: Check Generation**
```python
def debug_generation(rag_system, query: str, contexts: List[str]):
    """Analyze generation behavior."""
    inputs = rag_system.tokenizer(
        f"Question: {query}\nContext: {' '.join(contexts)}\nAnswer:",
        return_tensors='pt'
    )
    
    print(f"Input tokens: {inputs['input_ids'].shape[1]}")
    
    # Generate with attention visualization
    with torch.no_grad():
        outputs = rag_system.generator.generate(
            **inputs,
            max_length=100,
            output_attentions=True,
            return_dict_in_generate=True
        )
    
    generated_text = rag_system.tokenizer.decode(outputs.sequences[0], skip_special_tokens=True)
    print(f"Generated: {generated_text}")
```

### Common Issues and Fixes

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Irrelevant answers | Poor retrieval | Improve retriever training, use hybrid retrieval |
| Hallucinations | Generator ignoring context | Add context-constrained decoding, fine-tune with negative examples |
| Incomplete answers | Context truncation | Better context selection, hierarchical summarization |
| Slow responses | Large model or index | Use smaller models, optimize index, add caching |
| Contradictory answers | Conflicting retrieved docs | Re-ranking, consistency checking |

## 4.8 Production Deployment Patterns

Moving from prototype to production requires architectural decisions.

### Pattern 1: Microservices Architecture

Separate retriever and generator into independent services:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Client    │ ──→ │  Retriever   │ ──→ │  Generator  │
│             │ ←── │   Service    │ ←── │   Service   │
└─────────────┘     └──────────────┘     └─────────────┘
                           │                    │
                      ┌────▼────┐         ┌────▼────┐
                      │ Document│         │ Model   │
                      │  Index  │         │ Cache   │
                      └─────────┘         └─────────┘
```

Benefits:
- Independent scaling
- Technology flexibility
- Easier updates

### Pattern 2: Edge Caching

For high-traffic applications, cache at the edge:

```python
import redis

class RedisCachedRAG(RAGSystem):
    """RAG system with Redis caching for production."""
    
    def __init__(self, *args, redis_host: str = 'localhost', **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_client = redis.Redis(host=redis_host, decode_responses=True)
        self.cache_ttl = 3600  # 1 hour
    
    def answer(self, query: str, *args, **kwargs) -> str:
        cache_key = f"rag:answer:{hashlib.md5(query.encode()).hexdigest()}"
        
        # Try cache
        cached = self.redis_client.get(cache_key)
        if cached:
            return cached
        
        # Compute
        answer = super().answer(query, *args, **kwargs)
        
        # Store
        self.redis_client.setex(cache_key, self.cache_ttl, answer)
        
        return answer
```

### Pattern 3: Asynchronous Processing

For non-real-time use cases:

```python
import asyncio
from celery import Celery

app = Celery('rag_tasks', broker='redis://localhost:6379')

@app.task
def async_rag_answer(query: str, document_index_path: str):
    """Celery task for async RAG processing."""
    rag_system = load_rag_system(document_index_path)
    return rag_system.answer(query, rag_system.doc_index, rag_system.documents)

# Usage
result = async_rag_answer.delay("What is quantum computing?", "index.bin")
# Do other work...
answer = result.get()  # Blocks until complete
```

## 4.9 Monitoring and Maintenance

Production RAG systems need ongoing monitoring.

### Key Metrics to Track

1. **Latency**: P50, P95, P99 response times
2. **Throughput**: Queries per second
3. **Error Rate**: Failed queries, timeouts
4. **Cache Hit Rate**: Percentage of cached responses
5. **Retrieval Quality**: Sample-based relevance scoring
6. **User Feedback**: Thumbs up/down, ratings

### Logging Example

```python
import logging
from datetime import datetime
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('rag_system')

class MonitoredRAGSystem(RAGSystem):
    """RAG system with comprehensive logging."""
    
    def answer(self, query: str, *args, **kwargs) -> str:
        start_time = datetime.now()
        
        try:
            answer = super().answer(query, *args, **kwargs)
            
            # Log success
            log_entry = {
                'timestamp': start_time.isoformat(),
                'query': query[:100],  # Truncate for privacy
                'answer_length': len(answer),
                'latency_ms': (datetime.now() - start_time).total_seconds() * 1000,
                'status': 'success'
            }
            logger.info(json.dumps(log_entry))
            
            return answer
            
        except Exception as e:
            # Log failure
            log_entry = {
                'timestamp': start_time.isoformat(),
                'query': query[:100],
                'error': str(e),
                'status': 'failure'
            }
            logger.error(json.dumps(log_entry))
            raise
```

## 4.10 Next Steps

You now have the foundation for building complete RAG systems. In Chapter 5, we'll dive deep into training and fine-tuning generator models specifically for RAG tasks.

Key takeaways from this chapter:
- Integration requires careful handling of component interactions
- Retrieval failures need graceful degradation strategies
- Context window management is critical for quality
- Latency optimization enables real-time applications
- Comprehensive evaluation measures both components and end-to-end performance
- Production deployment requires monitoring and maintenance

---

**Exercise 4.1**: Build a complete RAG system using the retriever from Chapter 3 and a pre-trained generator. Test it on 10 sample queries.

**Exercise 4.2**: Implement retrieval quality checking and fallback strategies. Measure improvement on difficult queries.

**Exercise 4.3**: Profile your RAG system's latency and implement at least two optimization techniques. Compare before/after performance.

**Exercise 4.4**: Create an evaluation suite and benchmark your system against ground truth answers. Identify the weakest component.
