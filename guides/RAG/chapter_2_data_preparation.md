# Chapter 2: Data Preparation for RAG

## 2.1 Understanding RAG Data Requirements

Training an effective RAG system requires careful preparation of two distinct types of data:

### Retrieval Training Data
- **Query-Document Pairs**: Questions paired with relevant documents
- **Negative Samples**: Irrelevant documents for contrastive learning
- **Hard Negatives**: Documents similar to relevant ones but not correct

### Generation Training Data
- **Context-Answer Pairs**: Retrieved context with expected responses
- **Multi-hop Examples**: Queries requiring information from multiple documents
- **Domain-Specific Q&A**: Specialized question-answer pairs

## 2.2 Data Collection Strategies

### Source Types

1. **Public Datasets**
   - Natural Questions (Google)
   - TriviaQA
   - MS MARCO
   - BEIR Benchmark
   - Domain-specific corpora (PubMed, arXiv, legal databases)

2. **Proprietary Data**
   - Internal documentation
   - Customer support logs
   - Product manuals
   - Knowledge bases

3. **Synthetic Data Generation**
   - Use LLMs to generate Q&A pairs from documents
   - Paraphrase existing questions
   - Create multi-hop reasoning examples

### Data Collection Pipeline

```python
import datasets
from langchain.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
    DirectoryLoader
)

# Load from HuggingFace
dataset = datasets.load_dataset('natural_questions', split='train[:10000]')

# Load local documents
loader = DirectoryLoader(
    './knowledge_base/',
    glob='**/*.pdf',
    loader_cls=PyPDFLoader
)
documents = loader.load()
```

## 2.3 Data Preprocessing

### Document Chunking Strategies

Effective chunking is critical for RAG performance:

#### Fixed-Size Chunking
```python
def fixed_size_chunk(text, chunk_size=512, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks
```

#### Semantic Chunking
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = text_splitter.split_documents(documents)
```

#### Agentic Chunking
- Use LLM to identify natural break points
- Maintain semantic coherence
- Preserve complete thoughts/sections

### Text Cleaning Pipeline

```python
import re
from unstructured.cleaners.core import clean, group_broken_paragraphs

def preprocess_text(text):
    # Remove special characters
    text = re.sub(r'[^\w\s.,!?]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Fix broken paragraphs
    text = group_broken_paragraphs(text)
    
    # Lowercase (optional, depends on embedding model)
    text = text.lower()
    
    return text.strip()
```

## 2.4 Creating Training Pairs

### Query-Document Pair Construction

```python
from typing import List, Tuple
import random

class RAGDataBuilder:
    def __init__(self, documents: List[str]):
        self.documents = documents
        self.doc_embeddings = None
    
    def create_training_pair(self, query: str, positive_doc_idx: int, 
                            num_negatives: int = 7) -> dict:
        """Create a training sample with one positive and multiple negatives."""
        
        positive_doc = self.documents[positive_doc_idx]
        
        # Sample negative documents
        negative_indices = [i for i in range(len(self.documents)) 
                           if i != positive_doc_idx]
        negative_indices = random.sample(negative_indices, 
                                        min(num_negatives, len(negative_indices)))
        negative_docs = [self.documents[i] for i in negative_indices]
        
        return {
            'query': query,
            'positive': positive_doc,
            'negatives': negative_docs
        }
    
    def build_dataset(self, queries: List[str], 
                     positive_indices: List[int]) -> List[dict]:
        """Build complete training dataset."""
        return [
            self.create_training_pair(q, pos_idx) 
            for q, pos_idx in zip(queries, positive_indices)
        ]
```

### Hard Negative Mining

```python
import faiss
import numpy as np

def mine_hard_negatives(query_embeddings, doc_embeddings, 
                       positive_indices, k=10):
    """Find hard negatives using similarity search."""
    
    # Build FAISS index
    dimension = doc_embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
    index.add(doc_embeddings)
    
    # Search for similar documents
    similarities, indices = index.search(query_embeddings, k)
    
    hard_negatives = []
    for i, (pos_idx, sims, idxs) in enumerate(zip(positive_indices, 
                                                   indices, similarities)):
        # Filter out the positive document
        negatives = [(idx, sim) for idx, sim in zip(idxs, sims) 
                    if idx != pos_idx]
        hard_negatives.append(negatives)
    
    return hard_negatives
```

## 2.5 Data Augmentation Techniques

### Query Paraphrasing

```python
from transformers import pipeline

paraphraser = pipeline("text2text-generation", 
                      model="t5-base")

def augment_query(query: str, num_variants: int = 3) -> List[str]:
    """Generate paraphrased versions of a query."""
    
    prompts = [f"paraphrase: {query}"] * num_variants
    results = paraphraser(prompts, max_length=64, truncation=True)
    
    return [r['generated_text'] for r in results]
```

### Back Translation

```python
from transformers import MarianMTModel, MarianTokenizer

class BackTranslator:
    def __init__(self):
        self.en_to_de = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-de')
        self.de_to_en = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-de-en')
        self.tokenizer_de = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-de')
        self.tokenizer_en = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-de-en')
    
    def augment(self, text: str) -> str:
        # Translate to German and back
        translated = self.en_to_de.generate(
            **self.tokenizer_de.prepare_seq2seq_batch([text])
        )
        german = self.tokenizer_de.decode(translated[0], skip_special_tokens=True)
        
        # Translate back to English
        back = self.de_to_en.generate(
            **self.tokenizer_en.prepare_seq2seq_batch([german])
        )
        return self.tokenizer_en.decode(back[0], skip_special_tokens=True)
```

## 2.6 Dataset Statistics and Validation

### Quality Checks

```python
def validate_rag_dataset(dataset: List[dict]) -> dict:
    """Perform quality checks on RAG training data."""
    
    stats = {
        'total_samples': len(dataset),
        'avg_query_length': 0,
        'avg_doc_length': 0,
        'vocabulary_size': 0,
        'duplicate_queries': 0
    }
    
    all_words = set()
    queries = []
    
    for sample in dataset:
        queries.append(sample['query'])
        all_words.update(sample['query'].split())
        all_words.update(sample['positive'].split())
        
        stats['avg_query_length'] += len(sample['query'])
        stats['avg_doc_length'] += len(sample['positive'])
    
    # Calculate averages
    stats['avg_query_length'] /= len(dataset)
    stats['avg_doc_length'] /= len(dataset)
    stats['vocabulary_size'] = len(all_words)
    stats['duplicate_queries'] = len(queries) - len(set(queries))
    
    return stats

# Usage
stats = validate_rag_dataset(training_data)
print(f"Dataset Statistics: {stats}")
```

### Train/Validation/Test Split

```python
from sklearn.model_selection import train_test_split

def split_rag_dataset(dataset: List[dict], 
                     train_ratio: float = 0.8,
                     val_ratio: float = 0.1,
                     test_ratio: float = 0.1,
                     stratify_by: str = None) -> Tuple[List, List, List]:
    """Split dataset maintaining distribution."""
    
    # First split: train vs temp (val+test)
    train_data, temp_data = train_test_split(
        dataset,
        test_size=(val_ratio + test_ratio),
        random_state=42,
        stratify=None  # Can add stratification logic here
    )
    
    # Second split: val vs test
    val_ratio_adjusted = val_ratio / (val_ratio + test_ratio)
    val_data, test_data = train_test_split(
        temp_data,
        test_size=(1 - val_ratio_adjusted),
        random_state=42
    )
    
    return train_data, val_data, test_data
```

## 2.7 Storage Formats

### JSONL Format (Recommended)

```json
{"query": "What is machine learning?", "positive": "Machine learning is...", "negatives": ["irrelevant doc 1", "irrelevant doc 2"]}
{"query": "How do neural networks work?", "positive": "Neural networks are...", "negatives": ["irrelevant doc 3", "irrelevant doc 4"]}
```

### Loading JSONL Dataset

```python
import json
from torch.utils.data import Dataset

class RAGDataset(Dataset):
    def __init__(self, filepath: str):
        self.data = []
        with open(filepath, 'r') as f:
            for line in f:
                self.data.append(json.loads(line))
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
```

### Parquet Format (for Large Datasets)

```python
import pandas as pd
import pyarrow.parquet as pq

# Save to parquet
df = pd.DataFrame(training_data)
df.to_parquet('rag_training_data.parquet', index=False)

# Load from parquet
df = pd.read_parquet('rag_training_data.parquet')
```

## 2.8 Best Practices

### Do's
- ✅ Ensure diverse query formulations
- ✅ Include domain-specific terminology
- ✅ Balance easy and hard negatives
- ✅ Maintain consistent chunk sizes
- ✅ Document data sources and preprocessing steps
- ✅ Regular validation of data quality

### Don'ts
- ❌ Don't use overly short chunks (<100 tokens)
- ❌ Don't include duplicate query-document pairs
- ❌ Don't mix domains without clear separation
- ❌ Don't ignore class imbalance
- ❌ Don't skip data validation steps

## 2.9 Next Steps

With prepared data, we're ready to:
- Build embedding models for retrieval
- Implement vector indexing
- Train dense retrievers
- Fine-tune generator models

---

**Exercise 2.1**: Download a public Q&A dataset and implement the chunking pipeline.

**Exercise 2.2**: Generate 100 synthetic Q&A pairs from a domain-specific document using an LLM.

**Exercise 2.3**: Implement hard negative mining using FAISS on your prepared dataset.
