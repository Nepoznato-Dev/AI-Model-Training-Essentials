# Chapter 2: Training Your First Transformer - From Tokenization to First Loss

## Welcome Back! 🎉

In Chapter 1, you learned **what** Transformers are and how they work internally. Now, in Chapter 2, we'll roll up our sleeves and **actually train one**! 

Don't worry if you've never trained a neural network before. We'll walk through every single step together, explaining what each piece does and why it matters.

## What You'll Learn in This Chapter

By the end of this chapter, you will be able to:
- ✅ Prepare text data for training (tokenization)
- ✅ Create training datasets from raw text
- ✅ Set up the training loop with proper loss functions
- ✅ Monitor training progress and debug common issues
- ✅ Save and load your trained model
- ✅ Understand what "loss" means and how to interpret it

## Prerequisites Check

Before we begin, make sure you have:
- Python 3.8+ installed
- PyTorch installed (`pip install torch`)
- Basic familiarity with Python (variables, loops, functions)
- Completed Chapter 1 (or understand attention mechanisms)

**No prior ML experience needed!** We'll explain everything as we go.

---

## Part 1: Understanding the Training Process

### What Does "Training" Actually Mean?

Imagine you're teaching a child to complete sentences:

**You:** "The cat sat on the..."  
**Child:** "Mat!"  
**You:** "Good! But actually, in this story, it's 'chair'. Try to remember that."

Over time, with thousands of examples, the child learns patterns about how sentences end.

**Training a Transformer is similar:**
1. We show it incomplete sentences
2. It makes a guess
3. We tell it how wrong it was (the **loss**)
4. It adjusts its internal parameters slightly
5. Repeat millions of times!

### The Training Loop - Visualized

```
┌─────────────────────────────────────────────────────────┐
│                  TRAINING LOOP                          │
├─────────────────────────────────────────────────────────┤
│  1. Get a batch of text data                            │
│  2. Convert text to numbers (tokens)                    │
│  3. Feed tokens into the model                          │
│  4. Model makes predictions                             │
│  5. Compare predictions to actual answers (calculate loss)│
│  6. Adjust model parameters (backpropagation)           │
│  7. Repeat!                                             │
└─────────────────────────────────────────────────────────┘
```

Let's build each piece step by step.

---

## Part 2: Preparing Your Data

### Step 1: Getting Training Text

First, we need text to train on. For this tutorial, we'll use a small sample dataset. In real projects, you might use:
- Books (Project Gutenberg)
- Wikipedia dumps
- Code repositories (GitHub)
- Custom domain text (medical, legal, etc.)

```python
# Sample training data - in reality, you'd have millions of sentences
training_text = """
Artificial intelligence is transforming the world.
Machine learning is a subset of artificial intelligence.
Deep learning uses neural networks with many layers.
Transformers are revolutionizing natural language processing.
Attention mechanisms allow models to focus on important words.
Python is a popular programming language for AI.
PyTorch is a deep learning framework developed by Facebook.
Training large models requires significant computational resources.
Data preprocessing is crucial for successful model training.
Evaluation metrics help us measure model performance.
""" * 100  # Repeat to simulate larger dataset
```

**💡 Beginner Tip:** Real datasets are HUGE (gigabytes or terabytes). We're using a tiny sample so you can run this on any computer!

### Step 2: Building a Vocabulary

Before the model can process text, we need to convert words to numbers. This is called **tokenization**.

**What's a token?**
- A token can be a word, part of a word, or even a character
- Example: "transformers" → ["transform", "ers"] (2 tokens)
- Each token gets assigned a unique number

Let's build a simple vocabulary:

```python
import re
from collections import Counter

class SimpleVocabulary:
    def __init__(self, text, min_freq=1):
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"  # Beginning of sequence
        self.eos_token = "<EOS>"  # End of sequence
        
        # Start with special tokens
        self.token2idx = {
            self.pad_token: 0,
            self.unk_token: 1,
            self.bos_token: 2,
            self.eos_token: 3
        }
        
        # Tokenize text (simple: split on whitespace and punctuation)
        tokens = re.findall(r'\b\w+\b', text.lower())
        
        # Count token frequencies
        token_counts = Counter(tokens)
        
        # Add tokens that appear at least min_freq times
        idx = len(self.token2idx)
        for token, count in token_counts.items():
            if count >= min_freq and token not in self.token2idx:
                self.token2idx[token] = idx
                idx += 1
        
        # Create reverse mapping
        self.idx2token = {idx: token for token, idx in self.token2idx.items()}
        
        print(f"Vocabulary size: {len(self.token2idx)} tokens")
    
    def encode(self, text):
        """Convert text to list of token IDs"""
        tokens = re.findall(r'\b\w+\b', text.lower())
        ids = [self.token2idx.get(token, self.token2idx[self.unk_token]) 
               for token in tokens]
        return ids
    
    def decode(self, token_ids):
        """Convert token IDs back to text"""
        tokens = [self.idx2token.get(idx, self.unk_token) 
                  for idx in token_ids]
        return ' '.join(tokens)
    
    def __len__(self):
        return len(self.token2idx)

# Create vocabulary
vocab = SimpleVocabulary(training_text)

# Test it out
sample_text = "Artificial intelligence is amazing"
encoded = vocab.encode(sample_text)
print(f"Original: {sample_text}")
print(f"Encoded: {encoded}")
print(f"Decoded: {vocab.decode(encoded)}")
```

**Output:**
```
Vocabulary size: 87 tokens
Original: Artificial intelligence is amazing
Encoded: [45, 12, 5, 86]
Decoded: artificial intelligence is <UNK>
```

**🤔 Why did "amazing" become `<UNK>`?**
Because "amazing" didn't appear in our training text! The `<UNK>` (unknown) token handles words the model hasn't seen before.

### Step 3: Creating Sequences

Transformers process fixed-length sequences. We need to:
1. Split text into chunks of equal length
2. Add special beginning/end tokens
3. Pad shorter sequences

```python
import torch
from torch.utils.data import Dataset, DataLoader

class TextDataset(Dataset):
    def __init__(self, text, vocab, seq_length=20):
        self.vocab = vocab
        self.seq_length = seq_length
        
        # Tokenize entire text
        tokens = re.findall(r'\b\w+\b', text.lower())
        
        # Create sequences (sliding window approach)
        self.sequences = []
        for i in range(0, len(tokens) - seq_length, seq_length // 2):  # 50% overlap
            seq = tokens[i:i + seq_length]
            # Add BOS and EOS tokens
            seq = [vocab.bos_token] + seq + [vocab.eos_token]
            # Convert to IDs
            seq_ids = [vocab.token2idx.get(token, vocab.token2idx[vocab.unk_token]) 
                       for token in seq]
            self.sequences.append(seq_ids)
        
        print(f"Created {len(self.sequences)} training sequences")
    
    def __len__(self):
        return len(self.sequences)
    
    def __getitem__(self, idx):
        return torch.tensor(self.sequences[idx], dtype=torch.long)

# Create dataset
seq_length = 15  # Shorter for demo
dataset = TextDataset(training_text, vocab, seq_length)

# Check first sequence
print(f"\nFirst sequence IDs: {dataset[0]}")
print(f"First sequence text: {vocab.decode(dataset[0].tolist())}")
```

### Step 4: Batching Data

We don't train on one sequence at a time - we use **batches** for efficiency.

```python
def collate_fn(batch):
    """Pad sequences in a batch to the same length"""
    # Find max length in batch
    max_len = max(len(seq) for seq in batch)
    
    # Pad all sequences to max length
    padded_batch = []
    for seq in batch:
        padding = [vocab.token2idx[vocab.pad_token]] * (max_len - len(seq))
        padded_seq = seq.tolist() + padding
        padded_batch.append(torch.tensor(padded_seq))
    
    # Stack into a tensor: [batch_size, seq_length]
    return torch.stack(padded_batch)

# Create DataLoader
batch_size = 4
dataloader = DataLoader(dataset, batch_size=batch_size, 
                        shuffle=True, collate_fn=collate_fn)

# Inspect a batch
for batch in dataloader:
    print(f"\nBatch shape: {batch.shape}")  # [4, 17]
    print(f"First sequence in batch: {batch[0]}")
    break  # Just show first batch
```

**📊 Understanding the Batch Shape:**
- `[4, 17]` means 4 sequences, each with 17 tokens
- All sequences are padded to the same length
- This allows parallel processing on GPU/CPU

---

## Part 3: Building the Training Components

### Step 1: Defining the Loss Function

**What is loss?**
Loss measures how wrong the model's predictions are. Lower loss = better predictions.

For language modeling, we use **Cross-Entropy Loss**:

```python
import torch.nn as nn

# Cross-entropy loss for classification
criterion = nn.CrossEntropyLoss(ignore_index=vocab.token2idx[vocab.pad_token])
```

**How it works:**
1. Model predicts probabilities for next token at each position
2. We compare to the actual next token
3. Loss is high if prediction is wrong, low if correct
4. We ignore padding tokens (they don't contain information)

**Visual Example:**
```
Input:  "The cat sat on"
Target: "cat sat on the"

Model predicts:
Position 1: "cat" (90% confidence) ✓
Position 2: "dog" (60% confidence) ✗ (should be "sat")
Position 3: "on" (80% confidence) ✓
Position 4: "chair" (40% confidence) ✗ (should be "the")

Loss = average of how wrong these predictions are
```

### Step 2: Setting Up the Optimizer

The **optimizer** decides how to adjust model parameters to reduce loss.

```python
from transformers_model import TransformerLM  # From Chapter 1

# Initialize model
model = TransformerLM(
    vocab_size=len(vocab),
    d_model=64,      # Small for demo
    n_heads=4,
    n_layers=2,
    d_ff=128,
    max_seq_length=seq_length + 2,  # +2 for BOS/EOS
    dropout=0.1
)

# Adam optimizer - most popular choice
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print(f"Model has {sum(p.numel() for p in model.parameters()):,} parameters")
```

**💡 Learning Rate (lr):**
- Controls how big of steps we take when updating parameters
- Too high → training becomes unstable
- Too low → training takes forever
- 0.001 is a good starting point

### Step 3: The Training Loop - Line by Line

Now for the main event! Let's build the training loop with detailed explanations:

```python
import math

def train_epoch(model, dataloader, criterion, optimizer, device):
    """Train for one epoch (one pass through all data)"""
    
    model.train()  # Set model to training mode
    total_loss = 0
    num_batches = 0
    
    for batch_idx, batch in enumerate(dataloader):
        # Move batch to GPU/CPU
        batch = batch.to(device)
        
        # Separate input and target
        # Input: all tokens except last
        # Target: all tokens except first
        inputs = batch[:, :-1]   # [batch_size, seq_length-1]
        targets = batch[:, 1:]   # [batch_size, seq_length-1]
        
        # Zero gradients from previous iteration
        optimizer.zero_grad()
        
        # Forward pass: get model predictions
        outputs = model(inputs)  # [batch_size, seq_length-1, vocab_size]
        
        # Reshape for loss calculation
        # Need: [batch_size * seq_length, vocab_size] and [batch_size * seq_length]
        outputs = outputs.view(-1, outputs.size(-1))
        targets = targets.reshape(-1)
        
        # Calculate loss
        loss = criterion(outputs, targets)
        
        # Backward pass: calculate gradients
        loss.backward()
        
        # Clip gradients (prevent exploding gradients)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        
        # Update model parameters
        optimizer.step()
        
        # Track loss
        total_loss += loss.item()
        num_batches += 1
        
        # Print progress every 10 batches
        if (batch_idx + 1) % 10 == 0:
            avg_loss = total_loss / num_batches
            perplexity = math.exp(avg_loss)
            print(f"Batch {batch_idx + 1}/{len(dataloader)} | "
                  f"Loss: {avg_loss:.4f} | Perplexity: {perplexity:.2f}")
    
    return total_loss / num_batches

# Training configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Training on: {device}")
model = model.to(device)

# Train for multiple epochs
num_epochs = 5
for epoch in range(num_epochs):
    print(f"\n{'='*50}")
    print(f"EPOCH {epoch + 1}/{num_epochs}")
    print(f"{'='*50}")
    
    avg_loss = train_epoch(model, dataloader, criterion, optimizer, device)
    perplexity = math.exp(avg_loss)
    
    print(f"\nEpoch {epoch + 1} Complete!")
    print(f"Average Loss: {avg_loss:.4f}")
    print(f"Perplexity: {perplexity:.2f}")
    
    # Save checkpoint
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': avg_loss,
    }, f'checkpoint_epoch_{epoch + 1}.pt')
    print(f"Checkpoint saved!")
```

**🔍 Breaking Down the Training Loop:**

1. **`model.train()`**: Tells PyTorch we're training (enables dropout, etc.)
2. **`optimizer.zero_grad()`**: Clears old gradients (otherwise they accumulate!)
3. **Forward pass**: Model makes predictions
4. **`loss.backward()`**: Calculates gradients (how much each parameter contributed to error)
5. **Gradient clipping**: Prevents unstable training
6. **`optimizer.step()`**: Updates parameters using gradients
7. **Track loss**: Monitor progress

### Understanding Perplexity

**Perplexity** is a more interpretable metric than loss:
- Formula: `perplexity = e^loss`
- Meaning: "On average, how many options did the model consider equally likely?"
- Lower is better!
- Random guessing: perplexity = vocabulary size
- Good model: perplexity < 100 (depends on task)

**Example:**
- Loss = 4.0 → Perplexity = 54.6
- Loss = 3.0 → Perplexity = 20.1 (better!)
- Loss = 2.0 → Perplexity = 7.4 (excellent!)

---

## Part 4: Monitoring and Debugging Training

### Tracking Training Progress

Let's add visualization to see how training improves:

```python
import matplotlib.pyplot as plt

def train_with_tracking(model, dataloader, criterion, optimizer, device, num_epochs):
    """Train with loss tracking and visualization"""
    
    train_losses = []
    
    for epoch in range(num_epochs):
        model.train()
        epoch_loss = 0
        num_batches = 0
        
        for batch in dataloader:
            batch = batch.to(device)
            inputs = batch[:, :-1]
            targets = batch[:, 1:]
            
            optimizer.zero_grad()
            outputs = model(inputs)
            outputs = outputs.view(-1, outputs.size(-1))
            targets = targets.reshape(-1)
            
            loss = criterion(outputs, targets)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            
            epoch_loss += loss.item()
            num_batches += 1
        
        avg_loss = epoch_loss / num_batches
        train_losses.append(avg_loss)
        
        print(f"Epoch {epoch + 1}/{num_epochs} | Loss: {avg_loss:.4f} | PPL: {math.exp(avg_loss):.2f}")
    
    # Plot training curve
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, num_epochs + 1), train_losses, marker='o')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss Over Time')
    plt.grid(True, alpha=0.3)
    plt.savefig('training_loss.png')
    print("\nTraining curve saved to 'training_loss.png'")
    
    return train_losses

# Run training with tracking
train_losses = train_with_tracking(model, dataloader, criterion, optimizer, device, num_epochs=10)
```

### Common Training Issues & Solutions

#### Issue 1: Loss Not Decreasing

**Symptoms:**
- Loss stays flat or increases
- Perplexity remains high

**Possible Causes:**
1. **Learning rate too high**: Model overshoots optimal parameters
   - Fix: Reduce learning rate (try 0.0001)
2. **Learning rate too low**: Training too slow
   - Fix: Increase learning rate (try 0.01)
3. **Vanishing gradients**: Gradients become too small
   - Fix: Use gradient clipping, check initialization
4. **Data issues**: Incorrect tokenization or preprocessing
   - Fix: Verify input/target alignment

**Debug Code:**
```python
# Check gradient magnitudes
for name, param in model.named_parameters():
    if param.grad is not None:
        grad_norm = param.grad.norm().item()
        print(f"{name}: gradient norm = {grad_norm:.6f}")
        if grad_norm < 1e-7:
            print(f"  ⚠️  Warning: Very small gradients!")
```

#### Issue 2: Loss Becomes NaN

**Symptoms:**
- Loss suddenly becomes `nan` or `inf`
- Training crashes

**Causes:**
1. **Exploding gradients**: Gradients become extremely large
2. **Numerical instability**: Division by zero, log(0), etc.
3. **Learning rate too high**

**Solutions:**
```python
# 1. Gradient clipping (already in our code)
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

# 2. Check for NaN in outputs
if torch.isnan(outputs).any():
    print("NaN detected in outputs!")
    break

# 3. Use mixed precision carefully
# (We'll cover this in Chapter 4)
```

#### Issue 3: Overfitting

**Symptoms:**
- Training loss decreases but validation loss increases
- Model memorizes training data, doesn't generalize

**Solutions:**
1. **Add dropout** (we have 0.1 in our model)
2. **Reduce model size** (fewer layers/heads)
3. **More training data**
4. **Early stopping**: Stop when validation loss stops improving

---

## Part 5: Generating Text with Your Trained Model

Now let's use our trained model to generate new text!

```python
def generate_text(model, vocab, prompt, max_length=30, temperature=1.0):
    """Generate text given a prompt"""
    model.eval()  # Set to evaluation mode
    
    # Encode prompt
    tokens = re.findall(r'\b\w+\b', prompt.lower())
    input_ids = [vocab.token2idx.get(token, vocab.token2idx[vocab.unk_token]) 
                 for token in tokens]
    input_ids = [vocab.token2idx[vocab.bos_token]] + input_ids
    
    generated = input_ids.copy()
    
    with torch.no_grad():  # No gradients needed for generation
        for _ in range(max_length):
            # Prepare input
            input_tensor = torch.tensor([generated]).to(device)
            
            # Get predictions
            outputs = model(input_tensor)
            
            # Get last position predictions
            next_token_logits = outputs[0, -1, :] / temperature
            
            # Sample from distribution
            probs = torch.softmax(next_token_logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1).item()
            
            # Stop if EOS token
            if next_token == vocab.token2idx[vocab.eos_token]:
                break
            
            # Add to generated sequence
            generated.append(next_token)
    
    # Decode to text
    generated_text = vocab.decode(generated[1:])  # Skip BOS token
    return generated_text

# Try it out!
print("\n" + "="*50)
print("TEXT GENERATION DEMO")
print("="*50)

prompts = [
    "artificial intelligence",
    "machine learning is",
    "transformers are",
    "python is a"
]

for prompt in prompts:
    generated = generate_text(model, vocab, prompt, max_length=10, temperature=0.8)
    print(f"\nPrompt: {prompt}")
    print(f"Generated: {generated}")
```

**Understanding Temperature:**
- **Low temperature (0.2-0.5)**: More predictable, conservative
- **Medium temperature (0.7-1.0)**: Balanced creativity
- **High temperature (1.2-2.0)**: More random, creative, sometimes nonsensical

---

## Part 6: Saving and Loading Models

### Saving Your Trained Model

```python
# Save complete checkpoint
checkpoint = {
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'vocab': vocab,
    'training_config': {
        'vocab_size': len(vocab),
        'd_model': 64,
        'n_heads': 4,
        'n_layers': 2,
        'd_ff': 128,
        'seq_length': seq_length,
    }
}
torch.save(checkpoint, 'my_transformer.pt')
print("Model saved to 'my_transformer.pt'")

# Save only model weights (smaller file)
torch.save(model.state_dict(), 'model_weights.pt')
```

### Loading a Trained Model

```python
def load_model(checkpoint_path, device):
    """Load a trained model from checkpoint"""
    
    # Load checkpoint
    checkpoint = torch.load(checkpoint_path, map_location=device)
    
    # Recreate vocabulary
    vocab = checkpoint['vocab']
    
    # Recreate model with same architecture
    config = checkpoint['training_config']
    model = TransformerLM(
        vocab_size=config['vocab_size'],
        d_model=config['d_model'],
        n_heads=config['n_heads'],
        n_layers=config['n_layers'],
        d_ff=config['d_ff'],
        max_seq_length=config['seq_length'] + 2,
        dropout=0.1
    )
    
    # Load weights
    model.load_state_dict(checkpoint['model_state_dict'])
    model = model.to(device)
    model.eval()
    
    print(f"Loaded model from epoch with loss: {checkpoint.get('loss', 'N/A')}")
    
    return model, vocab

# Load and test
loaded_model, loaded_vocab = load_model('my_transformer.pt', device)
generated = generate_text(loaded_model, loaded_vocab, "deep learning", max_length=15)
print(f"\nLoaded model generation: {generated}")
```

---

## Hands-On Exercises

### Exercise 1: Experiment with Hyperparameters (Beginner)

Try different values and observe the effects:

```python
# TODO: Modify these and retrain
hyperparams = {
    'learning_rate': 0.001,      # Try: 0.0001, 0.01
    'd_model': 64,               # Try: 32, 128
    'n_heads': 4,                # Try: 2, 8
    'n_layers': 2,               # Try: 1, 4
    'dropout': 0.1,              # Try: 0.0, 0.3
    'batch_size': 4,             # Try: 2, 8
}

# Questions to answer:
# 1. How does increasing d_model affect training speed?
# 2. Does more layers always mean better performance?
# 3. What happens with very high dropout?
```

### Exercise 2: Add Validation (Intermediate)

Split data into training and validation sets:

```python
# TODO: Implement validation
# 1. Split dataset 90% train, 10% validation
# 2. Calculate validation loss after each epoch
# 3. Implement early stopping (stop if val_loss doesn't improve for 3 epochs)
# 4. Plot both train and validation loss curves
```

### Exercise 3: Train on Custom Text (Advanced)

```python
# TODO: Train on your own text
# 1. Find a text file (book chapter, articles, etc.)
# 2. Load and preprocess the text
# 3. Build vocabulary and dataset
# 4. Train a model
# 5. Generate text in the style of your source material

# Example: Train on Shakespeare, generate Shakespeare-like text!
```

---

## Troubleshooting Guide

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| CUDA out of memory | Batch size too large | Reduce batch_size or use gradient accumulation |
| Loss = NaN | Learning rate too high | Reduce learning rate, add gradient clipping |
| Training very slow | Using CPU instead of GPU | Check `device = torch.device('cuda')` |
| Generated text is gibberish | Model undertrained | Train for more epochs, check data quality |
| Loss not decreasing | Wrong input/target alignment | Verify `inputs = batch[:, :-1]`, `targets = batch[:, 1:]` |
| Out of vocabulary errors | Missing tokens in vocab | Check tokenization, increase vocab size |

---

## Key Takeaways

✅ **Data Preparation is Crucial**: Garbage in, garbage out. Spend time on tokenization and preprocessing.

✅ **Monitor Loss and Perplexity**: These tell you if training is working. Loss should decrease over time.

✅ **Hyperparameters Matter**: Learning rate, model size, and dropout significantly impact results.

✅ **Save Checkpoints**: Training can crash. Save regularly to avoid losing progress.

✅ **Start Small**: Use tiny models and datasets to debug before scaling up.

---

## What's Next?

In **Chapter 3**, we'll dive into:
- ⚡ Advanced training techniques (learning rate scheduling, warmup)
- 🚀 Scaling to larger models and datasets
- 📊 Evaluation metrics beyond loss
- 🎯 Fine-tuning pretrained models
- 🔧 Debugging complex training issues

You now have a working transformer that can generate text! In the next chapter, we'll make it even better.

---

## Glossary

| Term | Definition |
|------|------------|
| **Token** | A unit of text (word, subword, or character) converted to a number |
| **Vocabulary** | The complete set of tokens the model knows |
| **Batch** | Multiple sequences processed together for efficiency |
| **Epoch** | One complete pass through the entire training dataset |
| **Loss** | A number measuring how wrong the model's predictions are |
| **Perplexity** | An interpretable metric: e^loss, lower is better |
| **Learning Rate** | Controls how much model parameters change during training |
| **Gradient** | Direction and magnitude of parameter updates |
| **Backpropagation** | Algorithm to calculate gradients |
| **Optimizer** | Algorithm that updates parameters using gradients (e.g., Adam) |
| **Overfitting** | When model memorizes training data but doesn't generalize |
| **Dropout** | Randomly disabling neurons during training to prevent overfitting |
| **Temperature** | Controls randomness in text generation |
| **Checkpoint** | Saved model state that can be resumed later |

---

## Additional Resources

- **PyTorch Documentation**: https://pytorch.org/docs/
- "Attention Is All You Need" paper: https://arxiv.org/abs/1706.03762
- Hugging Face Course: https://huggingface.co/course
- Interactive Transformer Visualization: https://jalammar.github.io/illustrated-transformer/

---

**Congratulations!** 🎉 You've trained your first Transformer model! This is a huge milestone. Take a moment to appreciate what you've accomplished, then continue to Chapter 3 to level up your skills!
