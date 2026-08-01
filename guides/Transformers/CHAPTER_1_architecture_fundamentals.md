# Chapter 1: Transformer Architecture Fundamentals

## 1.1 Introduction to Transformers

Transformers have revolutionized natural language processing and beyond. Introduced in the landmark paper "Attention Is All You Need" (Vaswani et al., 2017), transformers replaced recurrent and convolutional architectures with pure attention mechanisms, enabling unprecedented parallelization and performance.

### Why Transformers Matter

- **Parallelization**: Process entire sequences simultaneously
- **Long-range Dependencies**: Capture relationships across thousands of tokens
- **Transfer Learning**: Pre-train once, fine-tune for many tasks
- **Scalability**: Performance improves predictably with scale
- **Versatility**: Applied to text, images, audio, video, and more

## 1.2 The Original Transformer Architecture

### High-Level Overview

```
Input → Embedding + Positional Encoding → Encoder Stack → Decoder Stack → Output
                                              ↓              ↓
                                        Self-Attention   Cross-Attention
```

### Key Components

1. **Input Embeddings**: Convert tokens to vectors
2. **Positional Encodings**: Inject sequence order information
3. **Multi-Head Attention**: Learn relationships between positions
4. **Feed-Forward Networks**: Process attended information
5. **Layer Normalization**: Stabilize training
6. **Residual Connections**: Enable deep architectures

## 1.3 Mathematical Foundations

### Scaled Dot-Product Attention

The core innovation of transformers is the attention mechanism:

```
Attention(Q, K, V) = softmax(QK^T / √d_k)V
```

Where:
- **Q (Query)**: What am I looking for?
- **K (Key)**: What do I contain?
- **V (Value)**: What information do I provide?
- **d_k**: Dimension of key/query vectors
- **√d_k**: Scaling factor to prevent vanishing gradients

### Implementation from Scratch

```python
import torch
import torch.nn as nn
import math

class ScaledDotProductAttention(nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        self.scale = None
    
    def forward(self, query, key, value, mask=None):
        d_k = query.size(-1)
        self.scale = math.sqrt(d_k)
        
        # Compute attention scores
        scores = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        
        # Apply mask (for padding or causal masking)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        
        # Apply softmax and dropout
        attention_weights = self.dropout(torch.softmax(scores, dim=-1))
        
        # Apply attention to values
        output = torch.matmul(attention_weights, value)
        
        return output, attention_weights
```

### Multi-Head Attention

Multiple attention heads allow the model to focus on different representation subspaces:

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        assert d_model % num_heads == 0
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # Linear projections
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        
        self.attention = ScaledDotProductAttention(dropout)
        self.dropout = nn.Dropout(dropout)
    
    def split_heads(self, x):
        """Split last dimension into (num_heads, d_k)"""
        batch_size, seq_len, _ = x.size()
        return x.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
    
    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        
        # Linear projections and split heads
        Q = self.split_heads(self.W_q(query))
        K = self.split_heads(self.W_k(key))
        V = self.split_heads(self.W_v(value))
        
        # Apply attention
        attention_output, attention_weights = self.attention(Q, K, V, mask)
        
        # Concatenate heads
        attention_output = attention_output.transpose(1, 2).contiguous().view(
            batch_size, -1, self.d_model
        )
        
        # Final projection
        output = self.W_o(attention_output)
        output = self.dropout(output)
        
        return output, attention_weights
```

## 1.4 Positional Encodings

Since transformers have no inherent notion of sequence order, positional encodings are essential:

```python
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_len=5000, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout)
        
        # Create positional encoding matrix
        pe = torch.zeros(max_seq_len, d_model)
        position = torch.arange(0, max_seq_len).unsqueeze(1).float()
        
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * 
            -(math.log(10000.0) / d_model)
        )
        
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        
        self.register_buffer('pe', pe)
    
    def forward(self, x):
        x = x + self.pe[:, :x.size(1)]
        return self.dropout(x)
```

## 1.5 Feed-Forward Networks

Each transformer layer contains a position-wise feed-forward network:

```python
class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
        self.activation = nn.ReLU()
    
    def forward(self, x):
        return self.linear2(self.dropout(self.activation(self.linear1(x))))
```

## 1.6 Layer Normalization and Residual Connections

```python
class SublayerConnection(nn.Module):
    def __init__(self, size, dropout=0.1):
        super().__init__()
        self.norm = nn.LayerNorm(size)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x, sublayer):
        # Pre-normalization architecture (more stable)
        normed_x = self.norm(x)
        return x + self.dropout(sublayer(normed_x))
```

## 1.7 Complete Encoder Layer

```python
class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = PositionwiseFeedForward(d_model, d_ff, dropout)
        self.sublayer1 = SublayerConnection(d_model, dropout)
        self.sublayer2 = SublayerConnection(d_model, dropout)
    
    def forward(self, x, mask=None):
        x = self.sublayer1(x, lambda _x: self.self_attn(_x, _x, _x, mask)[0])
        x = self.sublayer2(x, self.feed_forward)
        return x
```

## 1.8 Complete Decoder Layer

```python
class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.cross_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = PositionwiseFeedForward(d_model, d_ff, dropout)
        self.sublayer1 = SublayerConnection(d_model, dropout)
        self.sublayer2 = SublayerConnection(d_model, dropout)
        self.sublayer3 = SublayerConnection(d_model, dropout)
    
    def forward(self, x, encoder_output, src_mask=None, tgt_mask=None):
        # Masked self-attention
        x = self.sublayer1(x, lambda _x: self.self_attn(_x, _x, _x, tgt_mask)[0])
        
        # Cross-attention
        x = self.sublayer2(x, lambda _x: self.cross_attn(_x, encoder_output, encoder_output, src_mask)[0])
        
        # Feed-forward
        x = self.sublayer3(x, self.feed_forward)
        
        return x
```

## 1.9 The Complete Transformer

```python
class Transformer(nn.Module):
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model=512, 
                 num_heads=8, num_encoder_layers=6, num_decoder_layers=6,
                 d_ff=2048, max_seq_len=5000, dropout=0.1):
        super().__init__()
        
        self.d_model = d_model
        
        # Embeddings
        self.src_embedding = nn.Embedding(src_vocab_size, d_model)
        self.tgt_embedding = nn.Embedding(tgt_vocab_size, d_model)
        self.pos_encoding = PositionalEncoding(d_model, max_seq_len, dropout)
        
        # Encoder stack
        self.encoder_layers = nn.ModuleList([
            EncoderLayer(d_model, num_heads, d_ff, dropout)
            for _ in range(num_encoder_layers)
        ])
        
        # Decoder stack
        self.decoder_layers = nn.ModuleList([
            DecoderLayer(d_model, num_heads, d_ff, dropout)
            for _ in range(num_decoder_layers)
        ])
        
        # Output projection
        self.output_layer = nn.Linear(d_model, tgt_vocab_size)
        
        self.dropout = nn.Dropout(dropout)
    
    def encode(self, src, src_mask):
        x = self.dropout(self.pos_encoding(self.src_embedding(src) * math.sqrt(self.d_model)))
        
        for layer in self.encoder_layers:
            x = layer(x, src_mask)
        
        return x
    
    def decode(self, x, tgt, src_mask, tgt_mask):
        x = self.dropout(self.pos_encoding(self.tgt_embedding(tgt) * math.sqrt(self.d_model)))
        
        for layer in self.decoder_layers:
            x = layer(x, encoder_output, src_mask, tgt_mask)
        
        return x
    
    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        # Encode source
        encoder_output = self.encode(src, src_mask)
        
        # Decode target
        decoder_output = self.decode(encoder_output, tgt, src_mask, tgt_mask)
        
        # Project to vocabulary
        output = self.output_layer(decoder_output)
        
        return output
```

## 1.10 Training Considerations

### Label Smoothing

```python
class LabelSmoothingLoss(nn.Module):
    def __init__(self, vocab_size, smoothing=0.1, ignore_index=-100):
        super().__init__()
        self.vocab_size = vocab_size
        self.smoothing = smoothing
        self.ignore_index = ignore_index
    
    def forward(self, pred, target):
        pred = pred.log_softmax(dim=-1)
        
        # Create smoothed labels
        with torch.no_grad():
            true_dist = torch.zeros_like(pred)
            true_dist.fill_(self.smoothing / (self.vocab_size - 2))
            true_dist.scatter_(1, target.unsqueeze(1), 1 - self.smoothing)
            true_dist[:, self.ignore_index] = 0
            
            # Mask special tokens
            mask = torch.nonzero(target == self.ignore_index, as_tuple=True)
            if mask[0].size(0) > 0:
                true_dist[mask] = 0
        
        return torch.mean(torch.sum(-true_dist * pred, dim=-1))
```

### Learning Rate Scheduling

```python
class TransformerLRScheduler:
    def __init__(self, optimizer, d_model, warmup_steps=4000):
        self.optimizer = optimizer
        self.d_model = d_model
        self.warmup_steps = warmup_steps
        self.step_num = 0
    
    def step(self):
        self.step_num += 1
        
        lr = (self.d_model ** -0.5) * min(
            self.step_num ** -0.5,
            self.step_num * (self.warmup_steps ** -1.5)
        )
        
        for param_group in self.optimizer.param_groups:
            param_group['lr'] = lr
        
        return lr
```

## 1.11 Next Steps

With understanding of transformer architecture, you can now:
- Implement transformers from scratch
- Understand modern variants (BERT, GPT, T5)
- Fine-tune pre-trained models
- Design custom architectures

---

**Exercise 1.1**: Implement the complete transformer from scratch and train it on a small translation task.

**Exercise 1.2**: Visualize attention weights from different heads and layers.

**Exercise 1.3**: Experiment with different numbers of heads and layers to observe their impact.
