# Chapter 3: Training Dense Retrievers for RAG

## 3.1 Introduction to Dense Retrieval

Dense retrieval uses neural encoders to represent queries and documents as dense vectors, enabling semantic search beyond keyword matching. This chapter covers training custom dense retrievers from scratch and fine-tuning pre-trained models.

### Dense vs. Sparse Retrieval

| Aspect | Sparse (BM25) | Dense (Neural) |
|--------|--------------|----------------|
| Representation | Bag-of-words | Contextual embeddings |
| Matching | Lexical overlap | Semantic similarity |
| Vocabulary | Limited to training | Open vocabulary |
| Domain Adaptation | Requires re-indexing | Fine-tunable |
| Hardware | CPU-friendly | GPU recommended |

## 3.2 Architecture Choices

### Bi-Encoder Architecture

```python
import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer

class BiEncoder(nn.Module):
    def __init__(self, model_name='bert-base-uncased'):
        super().__init__()
        self.query_encoder = AutoModel.from_pretrained(model_name)
        self.doc_encoder = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Optional: projection layers
        self.query_projection = nn.Linear(768, 768)
        self.doc_projection = nn.Linear(768, 768)
        
    def encode_query(self, query_texts):
        inputs = self.tokenizer(
            query_texts,
            padding=True,
            truncation=True,
            max_length=128,
            return_tensors='pt'
        ).to(self.device)
        
        outputs = self.query_encoder(**inputs)
        # Use [CLS] token representation
        query_embeddings = outputs.last_hidden_state[:, 0, :]
        return self.query_projection(query_embeddings)
    
    def encode_document(self, doc_texts):
        inputs = self.tokenizer(
            doc_texts,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors='pt'
        ).to(self.device)
        
        outputs = self.doc_encoder(**inputs)
        doc_embeddings = outputs.last_hidden_state[:, 0, :]
        return self.doc_projection(doc_embeddings)
    
    @property
    def device(self):
        return next(self.parameters()).device
```

### Cross-Encoder Architecture

```python
class CrossEncoder(nn.Module):
    def __init__(self, model_name='bert-base-uncased'):
        super().__init__()
        self.model = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.classifier = nn.Linear(768, 1)
        
    def forward(self, queries, documents):
        # Concatenate query and document
        inputs = self.tokenizer(
            queries,
            documents,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors='pt',
            pad_to_multiple_of=8
        ).to(self.device)
        
        outputs = self.model(**inputs)
        cls_representation = outputs.last_hidden_state[:, 0, :]
        scores = self.classifier(cls_representation)
        
        return scores.squeeze(-1)
```

## 3.3 Loss Functions for Retrieval Training

### Contrastive Loss

```python
class ContrastiveLoss(nn.Module):
    def __init__(self, temperature=0.07):
        super().__init__()
        self.temperature = temperature
        self.ce = nn.CrossEntropyLoss()
    
    def forward(self, query_embeddings, doc_embeddings, labels=None):
        """
        query_embeddings: (batch_size, dim)
        doc_embeddings: (batch_size, dim) 
        labels: diagonal is positive, others are negative
        """
        # Normalize embeddings
        query_embeddings = nn.functional.normalize(query_embeddings, p=2, dim=1)
        doc_embeddings = nn.functional.normalize(doc_embeddings, p=2, dim=1)
        
        # Similarity matrix
        sim_matrix = torch.matmul(query_embeddings, doc_embeddings.T) / self.temperature
        
        # Labels are diagonal (each query matches its corresponding document)
        if labels is None:
            labels = torch.arange(sim_matrix.size(0)).to(sim_matrix.device)
        
        loss = self.ce(sim_matrix, labels)
        return loss
```

### Multiple Negatives Ranking Loss (MNRL)

```python
class MultipleNegativesRankingLoss(nn.Module):
    def __init__(self, scale=1.0, similarity_fct=nn.functional.cosine_similarity):
        super().__init__()
        self.scale = scale
        self.similarity_fct = similarity_fct
        self.cross_entropy_loss = nn.CrossEntropyLoss()
    
    def forward(self, query_embeddings, doc_embeddings):
        # Calculate similarity matrix
        scores = self.similarity_fct(
            query_embeddings.unsqueeze(1),
            doc_embeddings.unsqueeze(0),
            dim=2
        ) * self.scale
        
        # Diagonal elements are positive pairs
        labels = torch.arange(scores.size(0), device=scores.device)
        
        loss = self.cross_entropy_loss(scores, labels)
        return loss
```

### InfoNCE Loss

```python
def info_nce_loss(query_emb, pos_doc_emb, neg_doc_embs, temperature=0.07):
    """
    InfoNCE loss for one query-positive-negative set
    """
    # Positive similarity
    pos_score = torch.sum(query_emb * pos_doc_emb) / temperature
    
    # Negative similarities
    neg_scores = torch.matmul(query_emb.unsqueeze(0), neg_doc_embs.T).squeeze(0) / temperature
    
    # Compute loss
    all_scores = torch.cat([pos_score.unsqueeze(0), neg_scores])
    labels = torch.tensor([0], device=query_emb.device)
    
    loss = nn.functional.cross_entropy(all_scores.unsqueeze(0), labels)
    return loss
```

## 3.4 Training Loop Implementation

### Complete Training Pipeline

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
