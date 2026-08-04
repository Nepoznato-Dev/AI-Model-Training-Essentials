# Chapter 3: Training Dense Retrievers for RAG

## 3.1 Introduction to Dense Retrieval

Before we dive into training retrievers, let's understand what dense retrieval is and why it matters for RAG (Retrieval-Augmented Generation) systems.

### What is Dense Retrieval?

In a RAG system, the retriever's job is to find relevant documents from a large collection when given a query. **Dense retrieval** uses neural networks to convert both queries and documents into dense vector representations (embeddings). These vectors capture semantic meaning, allowing the system to find documents that are conceptually similar to the query, even if they don't share exact words.

Think of it this way: if you search for "automobile," a dense retriever can find documents about "cars" even though the words are different. This is because both concepts are mapped to similar regions in the vector space.

### Why Train Your Own Retriever?

You might wonder: "Why not just use pre-trained models?" While pre-trained models work well for general tasks, training your own retriever offers several advantages:

1. **Domain Adaptation**: Your documents may use specialized terminology (medical, legal, technical) that general models haven't seen
2. **Task-Specific Optimization**: Your RAG system has specific requirements that generic models can't address
3. **Better Performance**: Fine-tuning on your data typically yields 10-30% improvement in retrieval accuracy

### Dense vs. Sparse Retrieval

To appreciate dense retrieval, let's compare it with the traditional approach:

| Aspect | Sparse (BM25) | Dense (Neural) |
|--------|--------------|----------------|
| Representation | Bag-of-words | Contextual embeddings |
| Matching | Lexical overlap | Semantic similarity |
| Vocabulary | Limited to training | Open vocabulary |
| Domain Adaptation | Requires re-indexing | Fine-tunable |
| Hardware | CPU-friendly | GPU recommended |

**Sparse retrieval** (like BM25) works by counting word frequencies. It's fast and interpretable but fails when queries and documents use different vocabulary for the same concept.

**Dense retrieval** overcomes this limitation by learning continuous representations where semantically similar texts are close together in vector space, regardless of word overlap.

## 3.2 Understanding Retriever Architectures

Before writing any code, we need to understand the two main architectures used in dense retrieval: bi-encoders and cross-encoders. Each has trade-offs between speed and accuracy.

### Bi-Encoder Architecture

A **bi-encoder** uses two separate encoder networks (or the same network with shared weights) to independently encode queries and documents. This architecture is illustrated below:

```
Query → [Encoder] → Query Embedding ──┐
                                       ├→ Similarity Score
Document → [Encoder] → Doc Embedding ─┘
```

**Key Advantages:**
- **Efficiency**: Document embeddings can be pre-computed and stored in an index
- **Scalability**: Searching millions of documents becomes a simple nearest-neighbor lookup
- **Speed**: Query encoding is fast, making it suitable for real-time applications

**Trade-offs:**
- Less accurate than cross-encoders because query and document don't interact during encoding
- Cannot capture fine-grained interactions between specific query and document terms

Here's what a bi-encoder implementation looks like:

```python
import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer

class BiEncoder(nn.Module):
    def __init__(self, model_name='bert-base-uncased'):
        super().__init__()
        # We use two separate encoders for queries and documents
        # They can share weights or be trained independently
        self.query_encoder = AutoModel.from_pretrained(model_name)
        self.doc_encoder = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Optional: projection layers map encoder output to embedding space
        # This gives the model flexibility to learn task-specific representations
        self.query_projection = nn.Linear(768, 768)
        self.doc_projection = nn.Linear(768, 768)
        
    def encode_query(self, query_texts):
        """
        Encode query texts into dense vectors.
        
        Args:
            query_texts: List of query strings
            
        Returns:
            Tensor of shape (batch_size, embedding_dim)
        """
        # Tokenize the input queries
        inputs = self.tokenizer(
            query_texts,
            padding=True,  # Pad to longest sequence in batch
            truncation=True,  # Truncate sequences exceeding max_length
            max_length=128,  # Queries are typically shorter
            return_tensors='pt'
        ).to(self.device)
        
        # Get contextualized representations from the transformer
        outputs = self.query_encoder(**inputs)
        
        # Use [CLS] token representation as the sentence embedding
        # The [CLS] token is designed to aggregate sentence-level information
        query_embeddings = outputs.last_hidden_state[:, 0, :]
        
        # Project to final embedding space
        return self.query_projection(query_embeddings)
    
    def encode_document(self, doc_texts):
        """
        Encode document texts into dense vectors.
        
        Args:
            doc_texts: List of document strings
            
        Returns:
            Tensor of shape (batch_size, embedding_dim)
        """
        inputs = self.tokenizer(
            doc_texts,
            padding=True,
            truncation=True,
            max_length=512,  # Documents can be longer than queries
            return_tensors='pt'
        ).to(self.device)
        
        outputs = self.doc_encoder(**inputs)
        doc_embeddings = outputs.last_hidden_state[:, 0, :]
        return self.doc_projection(doc_embeddings)
    
    @property
    def device(self):
        """Helper property to get the current device."""
        return next(self.parameters()).device
```

**Key Implementation Details:**

1. **Separate Encoders**: Notice we have `query_encoder` and `doc_encoder`. While they start with the same pre-trained weights, they can diverge during training to specialize for their respective tasks.

2. **[CLS] Token**: We use the first token's embedding (`[:, 0, :]`) as the sentence representation. This is a common practice with BERT-style models, as the [CLS] token is trained to aggregate sentence-level semantics.

3. **Projection Layers**: These optional linear layers allow the model to transform the encoder's output into a more suitable embedding space for your specific retrieval task.

4. **Different Max Lengths**: Queries are typically shorter (128 tokens) while documents can be longer (512 tokens). This optimization saves computation.

### Cross-Encoder Architecture

While bi-encoders are efficient for retrieval, **cross-encoders** offer higher accuracy at the cost of speed. Let's understand when and why you might use them.

A cross-encoder processes the query and document *together* through a single encoder, allowing full attention between query and document tokens:

```
[Query] + [Document] → [Single Encoder] → Relevance Score
```

**When to Use Cross-Encoders:**
- **Re-ranking**: After a bi-encoder retrieves top-K candidates, use a cross-encoder to re-rank them
- **Training Data Generation**: Generate high-quality labels for training bi-encoders
- **Small-Scale Applications**: When you have fewer than ~10,000 documents and can afford slower inference

**Why Not Always Use Cross-Encoders?**

The main limitation is scalability. With a cross-encoder, you must process every query-document pair individually. For a corpus of 1 million documents, this means 1 million forward passes per query—clearly impractical for real-time systems.

Here's a cross-encoder implementation:

```python
class CrossEncoder(nn.Module):
    def __init__(self, model_name='bert-base-uncased'):
        super().__init__()
        # Single encoder processes query-document pairs jointly
        self.model = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Classifier head produces a relevance score
        self.classifier = nn.Linear(768, 1)
        
    def forward(self, queries, documents):
        """
        Compute relevance scores for query-document pairs.
        
        Args:
            queries: List of query strings
            documents: List of document strings (same length as queries)
            
        Returns:
            Tensor of shape (batch_size,) with relevance scores
        """
        # Concatenate query and document with special tokens
        # The tokenizer handles [CLS], [SEP] tokens automatically
        inputs = self.tokenizer(
            queries,
            documents,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors='pt',
            pad_to_multiple_of=8  # Padding to multiple of 8 improves efficiency
        ).to(self.device)
        
        # Get contextualized representations
        outputs = self.model(**inputs)
        
        # Use [CLS] token which now contains joint query-document information
        cls_representation = outputs.last_hidden_state[:, 0, :]
        
        # Produce relevance score
        scores = self.classifier(cls_representation)
        
        return scores.squeeze(-1)
```

**Understanding the Difference:**

The key distinction is *when* the query and document interact:
- **Bi-encoder**: No interaction during encoding → fast retrieval, lower accuracy
- **Cross-encoder**: Full interaction during encoding → slow retrieval, higher accuracy

A common pattern is to use both: a bi-encoder retrieves the top 100 candidates quickly, then a cross-encoder re-ranks them for optimal accuracy.

## 3.3 Loss Functions for Retrieval Training

Now that we understand the architectures, let's discuss how to train them. The choice of loss function is critical—it determines what patterns the model learns to recognize.

### What Makes a Good Loss Function for Retrieval?

In retrieval training, we want to:
1. **Pull together** matching query-document pairs (positives)
2. **Push apart** non-matching pairs (negatives)

The challenge is defining "apart" in a high-dimensional vector space. Different loss functions approach this differently.

### Contrastive Loss

Contrastive loss is one of the simplest approaches. It treats retrieval as a classification problem over a similarity matrix.

**How It Works:**

For a batch of query-document pairs, contrastive loss:
1. Computes all pairwise similarities (creating an N×N matrix)
2. Treats diagonal elements (matching pairs) as positive class
3. Treats off-diagonal elements (non-matching pairs) as negative class
4. Uses cross-entropy to optimize the model

Here's the implementation:

```python
class ContrastiveLoss(nn.Module):
    def __init__(self, temperature=0.07):
        super().__init__()
        self.temperature = temperature
        self.ce = nn.CrossEntropyLoss()
    
    def forward(self, query_embeddings, doc_embeddings, labels=None):
        """
        Compute contrastive loss for query-document pairs.
        
        Args:
            query_embeddings: Tensor of shape (batch_size, dim)
            doc_embeddings: Tensor of shape (batch_size, dim) 
            labels: Optional custom labels; by default, diagonal is positive
            
        Returns:
            Scalar loss value
        """
        # Step 1: Normalize embeddings to unit length
        # This ensures we're measuring cosine similarity, not dot product
        query_embeddings = nn.functional.normalize(query_embeddings, p=2, dim=1)
        doc_embeddings = nn.functional.normalize(doc_embeddings, p=2, dim=1)
        
        # Step 2: Compute similarity matrix
        # Each element [i,j] is the similarity between query i and document j
        sim_matrix = torch.matmul(query_embeddings, doc_embeddings.T) / self.temperature
        
        # Step 3: Define labels (diagonal elements are positive pairs)
        if labels is None:
            labels = torch.arange(sim_matrix.size(0)).to(sim_matrix.device)
        
        # Step 4: Apply cross-entropy loss
        loss = self.ce(sim_matrix, labels)
        return loss
```

**Understanding the Temperature Parameter:**

The `temperature` parameter controls how "sharp" the similarity distribution is:
- **Low temperature (e.g., 0.01)**: Makes differences between similarities more pronounced
- **High temperature (e.g., 0.1)**: Makes the distribution softer, more uniform

Typical values range from 0.01 to 0.1. The right value depends on your data and often requires tuning.

### Multiple Negatives Ranking Loss (MNRL)

MNRL is particularly effective for retrieval because it leverages all negatives in a batch simultaneously.

**Intuition:**

For each query, MNRL treats:
- Its paired document as the positive
- All other documents in the batch as negatives

This creates rich training signal from every batch without requiring explicit negative sampling.

```python
class MultipleNegativesRankingLoss(nn.Module):
    def __init__(self, scale=1.0, similarity_fct=nn.functional.cosine_similarity):
        super().__init__()
        self.scale = scale
        self.similarity_fct = similarity_fct
        self.cross_entropy_loss = nn.CrossEntropyLoss()
    
    def forward(self, query_embeddings, doc_embeddings):
        """
        Compute MNRL loss.
        
        The key insight: each query-document pair in the batch is treated as positive,
        while all other combinations are negatives.
        
        Args:
            query_embeddings: Tensor of shape (batch_size, dim)
            doc_embeddings: Tensor of shape (batch_size, dim)
            
        Returns:
            Scalar loss value
        """
        # Compute similarity matrix using broadcasting
        # query_embeddings: (batch_size, 1, dim)
        # doc_embeddings: (1, batch_size, dim)
        # Result: (batch_size, batch_size, dim) → reduced to (batch_size, batch_size)
        scores = self.similarity_fct(
            query_embeddings.unsqueeze(1),
            doc_embeddings.unsqueeze(0),
            dim=2
        ) * self.scale
        
        # Diagonal elements are positive pairs (query i matches doc i)
        labels = torch.arange(scores.size(0), device=scores.device)
        
        loss = self.cross_entropy_loss(scores, labels)
        return loss
```

**Why MNRL Works Well:**

1. **Efficient**: No need for explicit negative mining—every batch provides negatives
2. **Scalable**: Larger batches mean more negatives, improving training quality
3. **Effective**: Consistently strong performance across retrieval benchmarks

### InfoNCE Loss

InfoNCE (Information Noise Contrastive Estimation) is closely related to contrastive loss but explicitly handles one positive and multiple negatives per query.

**When to Use InfoNCE:**

InfoNCE shines when you have:
- One clear positive document per query
- A set of known negative documents (either sampled or mined)

```python
def info_nce_loss(query_emb, pos_doc_emb, neg_doc_embs, temperature=0.07):
    """
    Compute InfoNCE loss for one query-positive-negative set.
    
    Args:
        query_emb: Tensor of shape (dim,) - single query embedding
        pos_doc_emb: Tensor of shape (dim,) - positive document embedding
        neg_doc_embs: Tensor of shape (num_negatives, dim) - negative documents
        temperature: Scaling factor for similarity scores
        
    Returns:
        Scalar loss value
    """
    # Positive similarity: how similar is the query to its matching document?
    pos_score = torch.sum(query_emb * pos_doc_emb) / temperature
    
    # Negative similarities: how similar is the query to each negative?
    neg_scores = torch.matmul(query_emb.unsqueeze(0), neg_doc_embs.T).squeeze(0) / temperature
    
    # Combine positive and negative scores
    # The model should assign highest score to the positive (index 0)
    all_scores = torch.cat([pos_score.unsqueeze(0), neg_scores])
    labels = torch.tensor([0], device=query_emb.device)
    
    loss = nn.functional.cross_entropy(all_scores.unsqueeze(0), labels)
    return loss
```

**Comparing Loss Functions:**

| Loss Function | Best For | Batch Size Sensitivity | Negative Mining Required |
|---------------|----------|----------------------|-------------------------|
| Contrastive | General purpose | Medium | No (uses in-batch negatives) |
| MNRL | Large batch training | High (benefits from larger batches) | No |
| InfoNCE | Controlled negative sets | Low | Yes (explicit negatives) |

For most retrieval tasks, **MNRL** is a great starting point due to its simplicity and effectiveness.

## 3.4 Training Loop Implementation

Now let's put everything together into a complete training pipeline. This section walks through each component step-by-step.

### Complete Training Pipeline

Before diving into code, let's outline what a training pipeline needs:

1. **Data Loading**: Efficiently feed query-document pairs to the model
2. **Forward Pass**: Compute embeddings for queries and documents
3. **Loss Computation**: Measure how well the model separates positives from negatives
4. **Backward Pass**: Update model weights via gradient descent
5. **Evaluation**: Monitor progress on validation data
6. **Checkpointing**: Save the best model for later use

Here's a comprehensive implementation:

```python
from torch.utils.data import DataLoader
from transformers import get_linear_schedule_with_warmup
import numpy as np
from tqdm import tqdm

class DenseRetrieverTrainer:
    def __init__(self, model, train_dataset, val_dataset, 
                 learning_rate=2e-5, batch_size=32, num_epochs=3):
        self.model = model
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        
        # Optimizer and scheduler
        self.optimizer = torch.optim.AdamW(
            model.parameters(),
            lr=learning_rate,
            weight_decay=0.01
        )
        
        self.criterion = MultipleNegativesRankingLoss()
        
    def train_epoch(self, dataloader):
        self.model.train()
        total_loss = 0
        
        for batch in tqdm(dataloader, desc="Training"):
            queries = batch['query']
            positive_docs = batch['positive']
            negative_docs = batch['negatives']
            
            # Encode queries and positive documents
            query_embeddings = self.model.encode_query(queries)
            pos_doc_embeddings = self.model.encode_document(positive_docs)
            
            # Encode negative documents
            neg_doc_embeddings = self.model.encode_document(negative_docs)
            
            # Combine positive and negatives
            all_doc_embeddings = torch.cat([pos_doc_embeddings, neg_doc_embeddings], dim=0)
            
            # Calculate loss
            loss = self.criterion(query_embeddings, all_doc_embeddings)
            
            # Backward pass
            self.optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            self.optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    @torch.no_grad()
    def evaluate(self, dataloader):
        self.model.eval()
        total_loss = 0
        
        for batch in tqdm(dataloader, desc="Evaluating"):
            queries = batch['query']
            positive_docs = batch['positive']
            negative_docs = batch['negatives']
            
            query_embeddings = self.model.encode_query(queries)
            pos_doc_embeddings = self.model.encode_document(positive_docs)
            neg_doc_embeddings = self.model.encode_document(negative_docs)
            
            all_doc_embeddings = torch.cat([pos_doc_embeddings, neg_doc_embeddings], dim=0)
            loss = self.criterion(query_embeddings, all_doc_embeddings)
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def train(self):
        train_loader = DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            shuffle=True,
            collate_fn=self.collate_fn
        )
        
        val_loader = DataLoader(
            self.val_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            collate_fn=self.collate_fn
        )
        
        # Learning rate scheduler
        total_steps = len(train_loader) * self.num_epochs
        scheduler = get_linear_schedule_with_warmup(
            self.optimizer,
            num_warmup_steps=int(0.1 * total_steps),
            num_training_steps=total_steps
        )
        
        best_val_loss = float('inf')
        
        for epoch in range(self.num_epochs):
            print(f"\nEpoch {epoch + 1}/{self.num_epochs}")
            
            train_loss = self.train_epoch(train_loader)
            val_loss = self.evaluate(val_loader)
            
            print(f"Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")
            
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                torch.save(self.model.state_dict(), 'best_retriever.pt')
                print("✓ Saved best model")
            
            scheduler.step()
        
        return best_val_loss
    
    def collate_fn(self, batch):
        # Custom collation for batching
        queries = [item['query'] for item in batch]
        positives = [item['positive'] for item in batch]
        negatives = [item['negatives'] for item in batch]
        
        # Flatten negatives for batch processing
        flat_negatives = []
        for neg_list in negatives:
            flat_negatives.extend(neg_list)
        
        return {
            'query': queries,
            'positive': positives,
            'negatives': flat_negatives
        }
```

## 3.5 Fine-tuning Pre-trained Embedding Models

### Using Sentence Transformers

```python
from sentence_transformers import SentenceTransformer, losses, InputExample
from torch.utils.data import DataLoader

def finetune_sentence_transformer(train_examples, model_name='all-MiniLM-L6-v2'):
    # Load pre-trained model
    model = SentenceTransformer(model_name)
    
    # Create DataLoader
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=32)
    
    # Define loss
    train_loss = losses.MultipleNegativesRankingLoss(model)
    
    # Training configuration
    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=3,
        warmup_steps=100,
        use_amp=True,  # Mixed precision training
        show_progress_bar=True
    )
    
    return model

# Prepare training examples
train_examples = [
    InputExample(texts=['What is machine learning?', 
                       'Machine learning is a subset of AI...']),
    InputExample(texts=['How do neural networks work?',
                       'Neural networks are inspired by biological neurons...'])
]

model = finetune_sentence_transformer(train_examples)
model.save('fine_tuned_retriever')
```

## 3.6 In-Matrix Negatives and Advanced Techniques

### In-Batch Negatives Training

```python
class InBatchNegativesTrainer(DenseRetrieverTrainer):
    def train_epoch(self, dataloader):
        self.model.train()
        total_loss = 0
        
        for batch in tqdm(dataloader, desc="Training"):
            queries = batch['query']
            documents = batch['documents']  # Only positive docs
            
            # Encode all
            query_embeddings = self.model.encode_query(queries)
            doc_embeddings = self.model.encode_document(documents)
            
            # In-batch negatives: each query's negatives are other batch items' positives
            loss = self.criterion(query_embeddings, doc_embeddings)
            
            self.optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            self.optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
```

### Hard Negative Mining During Training

```python
class HardNegativeMiningTrainer(DenseRetrieverTrainer):
    def __init__(self, model, train_dataset, val_dataset, 
                 index_path='faiss_index.bin', **kwargs):
        super().__init__(model, train_dataset, val_dataset, **kwargs)
        self.index_path = index_path
        self.faiss_index = None
    
    def build_index(self, all_documents):
        import faiss
        import numpy as np
        
        self.model.eval()
        with torch.no_grad():
            doc_embeddings = self.model.encode_document(all_documents)
            doc_embeddings = doc_embeddings.cpu().numpy()
            doc_embeddings = doc_embeddings.astype('float32')
        
        dimension = doc_embeddings.shape[1]
        self.faiss_index = faiss.IndexFlatIP(dimension)
        faiss.normalize_L2(doc_embeddings)
        self.faiss_index.add(doc_embeddings)
        
        # Save index
        faiss.write_index(self.faiss_index, self.index_path)
    
    def mine_hard_negatives_batch(self, queries, positive_indices, k=20):
        if self.faiss_index is None:
            raise ValueError("Index not built")
        
        self.model.eval()
        with torch.no_grad():
            query_embeddings = self.model.encode_query(queries)
            query_embeddings = query_embeddings.cpu().numpy()
            faiss.normalize_L2(query_embeddings)
        
        similarities, indices = self.faiss_index.search(query_embeddings, k)
        
        hard_negatives = []
        for pos_idx, idxs in zip(positive_indices, indices):
            negatives = [idx for idx in idxs if idx != pos_idx]
            hard_negatives.append(negatives)
        
        return hard_negatives
```

## 3.7 Distributed Training

### Multi-GPU Training with DataParallel

```python
from torch.nn.parallel import DataParallel

def setup_multi_gpu(model, gpu_ids=[0, 1, 2, 3]):
    if len(gpu_ids) > 1:
        model = DataParallel(model, device_ids=gpu_ids)
    return model

# Usage
model = BiEncoder()
model = setup_multi_gpu(model, gpu_ids=[0, 1, 2, 3])
trainer = DenseRetrieverTrainer(model, train_dataset, val_dataset)
trainer.train()
```

### DDP Training (Recommended for Production)

```python
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler

def setup_ddp(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '29500'
    
    dist.init_process_group("nccl", rank=rank, world_size=world_size)
    torch.cuda.set_device(rank)

def cleanup_ddp():
    dist.destroy_process_group()

def ddp_train(rank, world_size, model, train_dataset):
    setup_ddp(rank, world_size)
    
    # Wrap model
    model = model.to(rank)
    model = DDP(model, device_ids=[rank])
    
    # Distributed sampler
    sampler = DistributedSampler(train_dataset, num_replicas=world_size, rank=rank)
    dataloader = DataLoader(train_dataset, batch_size=32, sampler=sampler)
    
    # Training loop
    for epoch in range(num_epochs):
        for batch in dataloader:
            # Training step
            pass
    
    cleanup_ddp()

# Launch
world_size = torch.cuda.device_count()
mp.spawn(ddp_train, args=(world_size, model, train_dataset), nprocs=world_size)
```

## 3.8 Evaluation During Training

### Recall@K Calculation

```python
@torch.no_grad()
def evaluate_recall(model, test_queries, test_documents, ground_truth, k_values=[1, 5, 10]):
    model.eval()
    
    # Encode all documents
    doc_embeddings = model.encode_document(test_documents)
    doc_embeddings = doc_embeddings.cpu().numpy()
    
    # Build index
    import faiss
    dimension = doc_embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    faiss.normalize_L2(doc_embeddings)
    index.add(doc_embeddings)
    
    # Encode queries and search
    query_embeddings = model.encode_query(test_queries)
    query_embeddings = query_embeddings.cpu().numpy()
    faiss.normalize_L2(query_embeddings)
    
    _, retrieved_indices = index.search(query_embeddings, max(k_values))
    
    # Calculate recall@k
    results = {}
    for k in k_values:
        correct = 0
        for i, (retrieved, true_idx) in enumerate(zip(retrieved_indices[:, :k], ground_truth)):
            if true_idx in retrieved:
                correct += 1
        results[f'recall@{k}'] = correct / len(test_queries)
    
    return results

# Usage
metrics = evaluate_recall(model, test_queries, test_docs, ground_truth_indices)
print(f"Evaluation Results: {metrics}")
```

## 3.9 Hyperparameter Tuning

### Key Hyperparameters

```python
hyperparameter_grid = {
    'learning_rate': [1e-5, 2e-5, 5e-5, 1e-4],
    'batch_size': [16, 32, 64, 128],
    'num_epochs': [2, 3, 5, 10],
    'temperature': [0.01, 0.05, 0.07, 0.1],
    'max_seq_length_query': [64, 128, 256],
    'max_seq_length_doc': [256, 512, 768],
    'warmup_ratio': [0.05, 0.1, 0.15],
    'weight_decay': [0.0, 0.01, 0.1]
}
```

### Automated Hyperparameter Search

```python
from optuna import create_study, Trial

def objective(trial: Trial):
    # Suggest hyperparameters
    lr = trial.suggest_loguniform('learning_rate', 1e-5, 1e-4)
    batch_size = trial.suggest_categorical('batch_size', [16, 32, 64])
    temperature = trial.suggest_uniform('temperature', 0.01, 0.1)
    
    # Initialize model with suggested params
    model = BiEncoder()
    trainer = DenseRetrieverTrainer(
        model,
        train_dataset,
        val_dataset,
        learning_rate=lr,
        batch_size=batch_size
    )
    trainer.criterion.temperature = temperature
    
    # Train and evaluate
    trainer.train()
    val_metrics = evaluate_recall(model, val_queries, val_docs, val_ground_truth)
    
    return val_metrics['recall@10']

# Run optimization
study = create_study(direction='maximize')
study.optimize(objective, n_trials=50)

print(f"Best parameters: {study.best_params}")
print(f"Best recall@10: {study.best_value}")
```

## 3.10 Next Steps

With a trained retriever, you can now:
- Index large document collections
- Integrate with generator models
- Implement end-to-end RAG pipelines
- Deploy to production

---

**Exercise 3.1**: Train a bi-encoder on a subset of MS MARCO dataset.

**Exercise 3.2**: Compare contrastive loss vs. MNRL on your validation set.

**Exercise 3.3**: Implement hard negative mining and measure improvement in recall@10.
