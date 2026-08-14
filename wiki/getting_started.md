# Getting Started

## Overview

This guide will help you set up your development environment and get started with the AI Engineering Knowledge Base.

## Prerequisites

Before you begin, ensure you have:

- Python 3.9+ installed
- pip or conda package manager
- Git installed
- Basic understanding of Python programming

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-Model-Training-Essentials
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n ai-eng python=3.9
conda activate ai-eng
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import torch; print(f'PyTorch {torch.__version__}')"
python -c "import transformers; print(f'Transformers {transformers.__version__}')"
```

## Project Structure

```
AI-Model-Training-Essentials/
├── guides/           # In-depth technical guides (including runnable projects)
├── skills/           # Skill-based documentation
├── knowledge_base/   # Organized knowledge repository
├── agent_modes/      # AI agent configurations
├── wiki/             # This wiki documentation
└── README.md         # Project overview
```

## Next Steps

- Explore [Learning Paths](learning_paths/beginner.md) based on your experience level
- Check out [Architecture Patterns](architecture_patterns.md) for system design guidance
- Review [Best Practices Checklist](references/checklist.md)
- Run the [Simple RAG Project](../guides/projects/rag_simple/README.md) to see retrieval-augmented generation in action

## Your First Hands-On Project: Simple RAG

The repository includes a minimal RAG (Retrieval-Augmented Generation) implementation that demonstrates core concepts:

**What it does:**
- Builds a small knowledge base from text documents
- Converts documents to embeddings using sentence-transformers
- Retrieves the most relevant document for a query using cosine similarity
- Generates an answer using a small text-to-text model

**How to run:**
```bash
cd guides/projects/rag_simple
pip install -r requirements.txt
python main.py
```

**Expected output:**
The demo shows question-answer pairs where the system retrieves relevant context and generates grounded answers.

**Customization ideas:**
- Add your own documents to the knowledge base
- Change the embedding model
- Adjust top_k parameter for retrieval
- Build a UI with Gradio or Streamlit

**Alternative:** Run in Google Colab for free GPU access (see project README for details)

## Hardware Reality Check

Most tutorials and the simple RAG demo run well on:
- **Free Google Colab**: No setup required, GPU available
- **Local CPU**: Works for learning and experimentation
- **Local GPU**: Faster iteration, optional for beginners

**Recommendation:** Start with Google Colab or CPU mode. Switch to GPU when scaling up to larger models or datasets.

## Prerequisite Knowledge

**Python basics:**
- Variables, lists, dictionaries, control flow, loops
- Functions, list comprehensions, imports, file I/O, error handling

**Git basics:**
- Cloning repositories, checking status, committing changes
- Pushing to remote, resolving conflicts

**ML fundamentals:**
- Supervised vs unsupervised learning, features and labels
- Training/evaluation, metrics, classical algorithms
- Neural networks basics, regularization, practical considerations

See the [Beginner Learning Path](learning_paths/beginner.md) for structured learning resources.

## Next Steps by User Type

**Learners following educational paths:**
- Start with the [beginner path](learning_paths/beginner.md), then progress through [intermediate](learning_paths/intermediate.md) and [advanced](learning_paths/advanced.md) tracks
- Explore domain-specific guides (RAG, Transformers, CNNs, Agentic Systems)
- Use the learning paths and prerequisites to structure your study plan

**Developers exploring agent modes:**
- Review [agent modes](agent_modes/agent_modes_system.md) for coding, research, debugging, review, testing, DevOps, and more
- Experiment with skills and orchestration patterns to build agentic workflows

**Contributors adding content:**
- Follow the [contributing guide](contributing.md)
- Update indexes and link to existing material instead of duplicating content
- Use the wiki as the detailed documentation hub

## Troubleshooting

### Common Issues

**Issue: Module not found errors**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Issue: Python version compatibility**
```bash
# Check your Python version
python --version

# Should be 3.9 or higher
```

## Related Resources

- [Main README](../README.md)
- [Requirements](../requirements.txt)
- [Guides](../guides/)
