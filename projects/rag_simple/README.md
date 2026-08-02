# Simple RAG (Retrieval-Augmented Generation) System

A minimal, fully-commented RAG implementation that runs on Google Colab free tier.

## 🎯 What This Does

This project builds a simple question-answering system that:
1. Takes a collection of documents
2. Converts them to searchable embeddings
3. Finds the most relevant document when you ask a question
4. Uses a small language model to generate an answer based on retrieved information

**Total lines:** ~150 (heavily commented)  
**Runtime:** ~5 minutes on Colab Free  
**GPU required:** No (works on CPU)

---

## 🚀 Quick Start

### Option 1: Google Colab (Recommended for Beginners)

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Upload notebook**
3. Upload `rag_simple.ipynb` (or copy code from `main.py`)
4. Click **Runtime → Change runtime type → GPU** (optional but faster)
5. Press **Play** button at the start of each cell

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/AI-Model-Training-Essentials/blob/main/projects/rag_simple/rag_simple.ipynb)

### Option 2: Run Locally

```bash
# Clone the repository
cd projects/rag_simple

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py
```

---

## 📁 Project Structure

```
projects/rag_simple/
├── README.md           # This file
├── main.py             # Complete RAG implementation (~150 lines)
├── rag_simple.ipynb    # Jupyter notebook version
└── requirements.txt    # Python dependencies
```

---

## 📦 Requirements

See `requirements.txt`:
```
transformers>=4.36.0
torch>=2.0.0
sentence-transformers>=2.2.0
scikit-learn>=1.3.0
numpy>=1.24.0
```

**Install with:**
```bash
pip install -r requirements.txt
```

---

## 🧠 Concepts You'll Learn

By running this project, you'll understand:

1. **Text Embeddings**: Converting text to numerical vectors
2. **Similarity Search**: Finding similar documents using cosine similarity
3. **Retrieval**: Selecting relevant context for a query
4. **Generation**: Using a language model to answer questions
5. **RAG Pipeline**: Combining retrieval + generation

---

## 📖 How It Works (Step by Step)

### Step 1: Prepare Documents
We create a small "knowledge base" of documents about AI topics.

### Step 2: Create Embeddings
Each document is converted to a vector (list of numbers) using a pre-trained model.

### Step 3: Store Vectors
We keep the document vectors in memory for fast searching.

### Step 4: Answer Questions
When you ask a question:
1. Convert the question to a vector
2. Find the most similar document vector
3. Pass the document + question to a language model
4. Get an answer!

---

## 💻 Example Usage

```python
from rag_system import RAGSystem

# Initialize the system
rag = RAGSystem()

# Add some documents
documents = [
    "Python is a programming language created by Guido van Rossum.",
    "Machine learning is a subset of artificial intelligence.",
    "Neural networks are inspired by the human brain."
]
rag.add_documents(documents)

# Ask questions
questions = [
    "Who created Python?",
    "What is machine learning?",
    "What are neural networks based on?"
]

for q in questions:
    answer = rag.answer(q)
    print(f"Q: {q}")
    print(f"A: {answer}\n")
```

---

## 🎓 Learning Checklist

After running this project, you should be able to:

- [ ] Explain what an embedding is
- [ ] Describe how similarity search works
- [ ] Identify the retrieval and generation components
- [ ] Modify the code to add your own documents
- [ ] Explain why RAG is useful compared to just using an LLM

---

## 🔧 Customization Ideas

Try these modifications to learn more:

1. **Add your own documents**: Replace the sample documents with your notes or articles
2. **Change the embedding model**: Try different models from sentence-transformers
3. **Adjust top_k**: Retrieve more or fewer documents
4. **Add a web interface**: Use Gradio or Streamlit for a UI

---

## ⚠️ Common Errors & Solutions

### Error: "ModuleNotFoundError: No module named 'transformers'"
**Solution:** Make sure your virtual environment is activated and run:
```bash
pip install -r requirements.txt
```

### Error: "CUDA out of memory"
**Solution:** The code automatically falls back to CPU. If it's slow, try Google Colab.

### Error: "ConnectionError" when downloading models
**Solution:** Check your internet connection. Models are downloaded on first run.

For more errors, see: [../../errors/README.md](../../errors/README.md)

---

## 📊 Expected Output

```
==================================================
Simple RAG System Demo
==================================================

Added 3 documents to the knowledge base.

Question: Who created Python?
Answer: Python was created by Guido van Rossum.

Question: What is machine learning?
Answer: Machine learning is a subset of artificial intelligence.

Question: What are neural networks based on?
Answer: Neural networks are inspired by the human brain.

==================================================
```

*Note: Exact answers may vary slightly based on the model.*

---

## 🚀 Next Steps

After completing this project:

1. **Read the guide**: See [../../guides/RAG/README.md](../../guides/RAG/README.md)
2. **Try the advanced version**: Build a RAG system with a vector database
3. **Experiment**: Add more documents, try different models
4. **Share**: Show your project to others or deploy it online

---

## 📚 Resources

- [RAG Fundamentals Guide](../../guides/RAG/CHAPTER_1_fundamentals.md)
- [Sentence Transformers Documentation](https://www.sbert.net/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Common Errors](../../errors/README.md)

---

## 💡 Tips for Success

1. **Read the comments**: Every line is explained in `main.py`
2. **Run it step by step**: Don't just copy-paste; understand each part
3. **Break it intentionally**: Change values and see what happens
4. **Ask questions**: Check the errors directory if stuck

---

**Happy Learning!** 🎉

Remember: Every expert started by running their first "Hello World" project. You've got this!
