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
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFacePipeline
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
    # Clean up any existing database to avoid duplicate entries on re-run
    import shutil
    if os.path.exists('./chroma_db'):
        shutil.rmtree('./chroma_db')
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory='./chroma_db'  # Save to disk
    )
    vectorstore.persist()
    
    print("✓ Vector store created!")
    return vectorstore

# Step 6: Load Language Model
def load_llm():
    """Load the language model that generates answers."""
    print(f"🔄 Loading LLM: {CONFIG['llm_model']}...")
    
    tokenizer = AutoTokenizer.from_pretrained(CONFIG['llm_model'])
    model = AutoModelForCausalLM.from_pretrained(CONFIG['llm_model'])
    
    # Move model to the correct device
    model = model.to(device)
    
    # Create text generation pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=256,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.2,
        device=0 if device == 'cuda' else -1,  # 0=GPU, -1=CPU
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
