# Chapter 1: RAG Fundamentals

## 1.1 Introduction to Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) is a hybrid approach that combines the power of retrieval-based and generation-based methods in natural language processing. It enhances large language models by providing them with access to external knowledge sources, enabling more accurate, up-to-date, and contextually relevant responses.

### Key Components of RAG

1. **Retriever**: Searches through a knowledge base to find relevant documents
2. **Generator**: Uses retrieved information to generate coherent responses
3. **Knowledge Base**: External data source containing domain-specific information
4. **Encoder**: Converts queries and documents into vector representations

### Why RAG Matters

- **Reduces Hallucination**: Grounds responses in factual information
- **Enables Updates**: Knowledge can be updated without retraining the model
- **Domain Specialization**: Allows customization for specific domains
- **Cost Efficiency**: Reduces need for massive model fine-tuning

## 1.2 Architecture Overview

```
User Query → Query Encoder → Vector Search → Retrieved Documents
                                                      ↓
                                            Generator (LLM)
                                                      ↓
                                              Final Response
```

### The RAG Pipeline

1. **Query Processing**: Tokenize and encode the user query
2. **Document Retrieval**: Search vector database for similar documents
3. **Context Construction**: Combine retrieved documents with query
4. **Generation**: Pass augmented context to language model
5. **Response Output**: Generate and return final answer

## 1.3 Mathematical Foundations

### Dense Retrieval

The core of RAG relies on dense vector representations. Given a query q and document d:

**Similarity Score**: 
```
sim(q, d) = cos(E_q(q), E_d(d)) = (E_q(q) · E_d(d)) / (||E_q(q)|| × ||E_d(d)||)
```

Where:
- E_q: Query encoder
- E_d: Document encoder
- ·: Dot product
- ||·||: L2 norm

### Training Objective

For contrastive learning in retriever training:

```
L = -log(exp(sim(q, d⁺)/τ) / (exp(sim(q, d⁺)/τ) + Σ exp(sim(q, d⁻)/τ)))
```

Where:
- d⁺: Positive (relevant) document
- d⁻: Negative (irrelevant) documents
- τ: Temperature parameter

## 1.4 Prerequisites for Training RAG

### Technical Requirements

- **Programming**: Python proficiency
- **Deep Learning**: PyTorch or TensorFlow
- **NLP Basics**: Tokenization, embeddings, attention mechanisms
- **Vector Databases**: FAISS, Pinecone, Weaviate, or Milvus

### Hardware Requirements

- **Minimum**: GPU with 8GB VRAM (e.g., RTX 3070)
- **Recommended**: GPU with 16-24GB VRAM (e.g., A100, RTX 4090)
- **Memory**: 32GB+ RAM for large datasets
- **Storage**: SSD with 100GB+ free space

### Software Stack

```python
# Core dependencies
transformers>=4.30.0
faiss-cpu>=1.7.4  # or faiss-gpu
sentence-transformers>=2.2.0
langchain>=0.1.0
pytorch>=2.0.0
datasets>=2.14.0
```

## 1.5 Common RAG Variants

### Naive RAG
- Simple retrieve-then-generate approach
- Single retrieval step
- Basic concatenation of context

### Advanced RAG
- Multi-step retrieval
- Re-ranking of retrieved documents
- Query expansion and transformation
- Hybrid search (dense + sparse)

### Modular RAG
- Composable retrieval modules
- Dynamic routing between retrievers
- Iterative refinement loops
- Feedback mechanisms

## 1.6 Evaluation Metrics

### Retrieval Quality
- **Recall@K**: Fraction of relevant documents in top-K results
- **Precision@K**: Fraction of top-K results that are relevant
- **Mean Reciprocal Rank (MRR)**: Average inverse rank of first relevant document
- **Normalized Discounted Cumulative Gain (NDCG)**: Position-weighted relevance

### Generation Quality
- **ROUGE**: Recall-Oriented Understudy for Gisting Evaluation
- **BLEU**: Bilingual Evaluation Understudy
- **BERTScore**: Contextual embedding-based similarity
- **Faithfulness**: Measure of hallucination
- **Answer Relevance**: Alignment with query intent

## 1.7 Next Steps

In the following chapters, we will:
- Set up the complete RAG infrastructure
- Prepare and process training data
- Train custom retrievers
- Fine-tune generator models
- Implement advanced RAG techniques
- Deploy production-ready systems

---

**Exercise 1.1**: Install the required dependencies and verify your GPU is accessible using PyTorch.

**Exercise 1.2**: Research and document three real-world applications where RAG outperforms standard LLM approaches.
