# RAG Chatbot: Your First AI That Answers Questions 🤖

**A complete, minimal RAG (Retrieval-Augmented Generation) system**

---

## 🎯 What This Project Does

This chatbot:
1. **Reads your documents** (PDFs, text files, etc.)
2. **Finds relevant information** when you ask questions
3. **Generates accurate answers** using the retrieved info

**Example:** Upload a company handbook, then ask "What's the vacation policy?" and get instant answers!

---

## ⏱️ Time & Requirements

- **Time:** 30 minutes
- **Lines of code:** ~150 (heavily commented!)
- **Hardware:** Works on Google Colab Free tier
- **Prerequisites:** Basic Python (or complete the [prerequisites](../prerequisites/))

---

## 🚀 Quick Start

### Option A: Google Colab (Recommended for Beginners)

1. Click this badge to open in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/AI-Model-Training-Essentials/blob/main/projects/rag-chatbot/rag_chatbot.ipynb)

2. Run all cells (Runtime → Run all)
3. Start chatting!

### Option B: Jupyter Notebook (Interactive Learning)

```bash
# 1. Navigate to project folder
cd projects/rag-chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch notebook
jupyter notebook rag_chatbot.ipynb
```

Then follow the interactive tutorial with quizzes!

### Option C: Local Setup (Python Script)

```bash
# 1. Clone or download this project
cd projects/rag-chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the script
python rag_chatbot.py
```

---

## 📁 Project Structure

```
projects/rag-chatbot/
├── README.md              # This file
├── requirements.txt       # Dependencies
├── rag_chatbot.py         # Complete code (standalone)
├── rag_chatbot.ipynb      # Jupyter notebook version
└── sample_docs/           # Example documents
    └── sample.txt
```

---

## 💻 The Code (Complete Implementation)

Here's the entire chatbot in one file (`rag_chatbot.py`):

```python
"""
RAG Chatbot - A Minimal Retrieval-Augmented Generation System
==============================================================
This chatbot reads your documents and answers questions based on them.

How it works:
1. Load and chunk documents
2. Create embeddings (vector representations)
3. Store in a vector database
4. When asked a question:
   - Find relevant chunks (retrieval)
   - Generate answer using LLM (generation)
"""

# Step 1: Import libraries
import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

print("🚀 Starting RAG Chatbot...")

# Step 2: Configuration (adjust based on your hardware!)
CONFIG = {
    'embedding_model': 'sentence-transformers/all-MiniLM-L6-v2',  # Small, fast embeddings
    'llm_model': 'gpt2',  # Tiny LLM for demo (use better models in production!)
    'chunk_size': 500,     # Characters per chunk
    'chunk_overlap': 50,   # Overlap between chunks
    'top_k': 3,           # Number of chunks to retrieve
}

# Check if GPU available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"✓ Using device: {device}")

# Step 3: Load Documents
def load_documents(folder_path='sample_docs'):
    """Load all text files from a folder."""
    documents = []
    
    if not os.path.exists(folder_path):
        # Create sample document if folder doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        sample_text = """
        Artificial Intelligence (AI) is transforming industries worldwide.
        Machine Learning (ML) is a subset of AI that enables systems to learn from data.
        Deep Learning uses neural networks with many layers.
        Natural Language Processing (NLP) helps computers understand human language.
        Computer Vision enables machines to interpret visual information.
        AI applications include chatbots, recommendation systems, and autonomous vehicles.
        """
        with open(f'{folder_path}/sample.txt', 'w') as f:
            f.write(sample_text)
        print(f"📄 Created sample document")
    
    # Load all .txt files
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            loader = TextLoader(os.path.join(folder_path, filename))
            documents.extend(loader.load())
            print(f"✓ Loaded: {filename}")
    
    return documents

# Step 4: Split Documents into Chunks
def split_documents(documents):
    """Split documents into smaller chunks for better retrieval."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CONFIG['chunk_size'],
        chunk_overlap=CONFIG['chunk_overlap'],
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"✓ Split into {len(chunks)} chunks")
    return chunks

# Step 5: Create Embeddings and Vector Store
def create_vector_store(chunks):
    """Convert text chunks to vectors and store them."""
    print("🔄 Creating embeddings (this may take a minute)...")
    
    # Load embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name=CONFIG['embedding_model'],
        model_kwargs={'device': device},
    )
    
    # Create vector database
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory='./chroma_db'  # Save to disk
    )
    
    print("✓ Vector store created!")
    return vectorstore

# Step 6: Load Language Model
def load_llm():
    """Load the language model that generates answers."""
    print(f"🔄 Loading LLM: {CONFIG['llm_model']}...")
    
    tokenizer = AutoTokenizer.from_pretrained(CONFIG['llm_model'])
    model = AutoModelForCausalLM.from_pretrained(CONFIG['llm_model'])
    
    # Create text generation pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=256,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.2,
    )
    
    # Wrap in LangChain LLM
    llm = HuggingFacePipeline(pipeline=pipe)
    print("✓ LLM loaded!")
    return llm

# Step 7: Create QA Chain
def create_qa_chain(vectorstore, llm):
    """Combine retriever and LLM into a QA system."""
    retriever = vectorstore.as_retriever(search_kwargs={'k': CONFIG['top_k']})
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )
    
    return qa_chain

# Step 8: Chat Loop
def chat(qa_chain):
    """Interactive chat loop."""
    print("\n" + "="*50)
    print("🤖 RAG Chatbot Ready! Ask me anything.")
    print("Type 'quit' or 'exit' to stop")
    print("="*50 + "\n")
    
    while True:
        # Get user question
        query = input("You: ").strip()
        
        # Check for exit
        if query.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
        
        # Skip empty input
        if not query:
            continue
        
        # Get answer
        try:
            result = qa_chain({'query': query})
            answer = result['result']
            
            # Show answer
            print(f"\n🤖 Bot: {answer}\n")
            
            # Optional: Show source documents
            # print("\n📚 Sources:")
            # for doc in result['source_documents']:
            #     print(f"- {doc.page_content[:100]}...")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Try rephrasing your question!")

# Main Function
def main():
    """Run the complete RAG pipeline."""
    try:
        # Load and process documents
        documents = load_documents()
        chunks = split_documents(documents)
        
        # Create vector store
        vectorstore = create_vector_store(chunks)
        
        # Load language model
        llm = load_llm()
        
        # Create QA system
        qa_chain = create_qa_chain(vectorstore, llm)
        
        # Start chatting!
        chat(qa_chain)
        
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        print("\n💡 Troubleshooting tips:")
        print("1. Check your internet connection (downloads models)")
        print("2. Make sure you have enough disk space (~2GB)")
        print("3. Try using Google Colab if local setup fails")
        print("\nSee errors/ directory for detailed solutions.")

if __name__ == "__main__":
    main()
```

---

## 📦 Requirements (`requirements.txt`)

```txt
# Core ML libraries
torch>=2.0.0
transformers>=4.35.0

# LangChain for RAG pipeline
langchain>=0.1.0
langchain-community>=0.0.10

# Vector database
chromadb>=0.4.0

# Embeddings
sentence-transformers>=2.2.0

# Optional: For PDF support
# pypdf>=3.0.0

# Optional: For better UI
# ipywidgets>=8.0.0
```

---

## 🧪 Sample Usage

```
🚀 Starting RAG Chatbot...
✓ Using device: cuda
📄 Created sample document
✓ Loaded: sample.txt
✓ Split into 2 chunks
🔄 Creating embeddings (this may take a minute)...
✓ Vector store created!
🔄 Loading LLM: gpt2...
✓ LLM loaded!

==================================================
🤖 RAG Chatbot Ready! Ask me anything.
Type 'quit' or 'exit' to stop
==================================================

You: What is machine learning?

🤖 Bot: Machine Learning (ML) is a subset of AI that enables 
systems to learn from data...

You: What are AI applications?

🤖 Bot: AI applications include chatbots, recommendation 
systems, and autonomous vehicles.

You: quit
👋 Goodbye!
```

---

## 🔧 Customization Guide

### Use Your Own Documents

1. Put `.txt` files in `sample_docs/` folder
2. Or modify `load_documents()` to read other formats:

```python
# For PDFs (uncomment pypdf in requirements.txt)
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("your_file.pdf")
documents = loader.load()
```

### Better Models (When You Have More Resources)

```python
# In CONFIG dictionary:

# Better embeddings (slower but more accurate)
'embedding_model': 'sentence-transformers/all-mpnet-base-v2',

# Better LLM (needs more RAM/VRAM)
'llm_model': 'microsoft/DialoGPT-medium',  # or 'large'

# For GPUs with 8GB+ VRAM
'llm_model': 'meta-llama/Llama-2-7b-chat-hf',  # Requires Hugging Face login
```

### Adjust Retrieval

```python
# Get more context (but slower)
'top_k': 5,  # Retrieve 5 chunks instead of 3

# Larger chunks (more context per chunk)
'chunk_size': 1000,
```

---

## 🐛 Common Issues & Fixes

### Issue 1: "ModuleNotFoundError"
**Fix:** `pip install -r requirements.txt`

### Issue 2: "CUDA out of memory"
**Fix:** See [errors/CUDA_OOM.md](../errors/CUDA_OOM.md)
- Reduce batch size
- Use CPU: Change `device = 'cpu'`

### Issue 3: Slow performance
**Fix:** 
- Use smaller models (as shown in CONFIG)
- Enable GPU in Colab (Runtime → Change runtime type → GPU)
- Process fewer documents

### Issue 4: Bad quality answers
**Fix:**
- Use better LLM models (see Customization section)
- Improve your documents (clearer text = better answers)
- Increase `top_k` to get more context

---

## 📊 Hardware Requirements

| Setup | Minimum | Recommended |
|-------|---------|-------------|
| **RAM** | 4GB | 8GB+ |
| **Storage** | 2GB free | 5GB+ free |
| **GPU** | Not required | NVIDIA with 4GB+ VRAM |
| **Internet** | Required (first run) | Required |

### Google Colab (Free Tier)
- ✅ Works perfectly!
- Tesla T4 GPU (16GB VRAM)
- Enough for this project

---

## 🎓 What You Learned

By completing this project, you now understand:

1. ✅ **Document Loading** - How to read files for AI processing
2. ✅ **Text Chunking** - Why and how to split documents
3. ✅ **Embeddings** - Converting text to vectors
4. ✅ **Vector Databases** - Storing and searching embeddings
5. ✅ **Retrieval** - Finding relevant information
6. ✅ **Generation** - Using LLMs to create answers
7. ✅ **RAG Pipeline** - Combining retrieval + generation

---

## 🚀 Next Steps

### Enhance This Project

1. **Add PDF Support** - Uncomment pypdf in requirements
2. **Better UI** - Add Gradio or Streamlit interface
3. **Save Conversations** - Log chat history
4. **Multi-turn Chat** - Add conversation memory
5. **Deploy Online** - Use Hugging Face Spaces or Streamlit Cloud

### Learn More

➡️ Read the full [RAG Guide](../../guides/RAG/) for deep theory  
➡️ Try the [Transformers Guide](../../guides/Transformers/) next  
➡️ Check [Common Errors](../errors/) if you get stuck

---

## 📝 License & Credits

- **License:** MIT (use freely!)
- **Based on:** LangChain + Hugging Face Transformers
- **Created for:** AI-Model-Training-Essentials

---

<div align="center">

**Congratulations! You've built your first AI chatbot!** 🎉

[Report Issue](https://github.com/YOUR_USERNAME/AI-Model-Training-Essentials/issues) | 
[View Full RAG Guide](../../guides/RAG/) | 
[Back to Projects](../)

</div>
