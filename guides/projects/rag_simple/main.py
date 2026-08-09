"""
Simple RAG (Retrieval-Augmented Generation) System
====================================================

A minimal, fully-commented implementation of a RAG system.
Perfect for beginners learning about retrieval-augmented generation.

What this does:
1. Takes a collection of documents (your "knowledge base")
2. Converts them to numerical vectors (embeddings)
3. When you ask a question, finds the most relevant document
4. Uses a language model to generate an answer based on that document

Total lines: ~150 (heavily commented)
Runtime: ~5 minutes on Google Colab Free tier
GPU required: No (works on CPU)

Author: AI Training Essentials
License: MIT
"""

# ============================================================
# STEP 1: IMPORT LIBRARIES
# ============================================================
# We need these libraries for different parts of the RAG pipeline

import os
import sys

# Check for required packages and provide helpful error messages
try:
    from sentence_transformers import SentenceTransformer  # For creating embeddings
except ImportError:
    print("ERROR: sentence-transformers not installed!")
    print("Please run: pip install sentence-transformers")
    sys.exit(1)

try:
    from sklearn.metrics.pairwise import cosine_similarity  # For finding similar documents
except ImportError:
    print("ERROR: scikit-learn not installed!")
    print("Please run: pip install scikit-learn")
    sys.exit(1)

import numpy as np  # For numerical operations

try:
    from transformers import pipeline  # For the language model
except ImportError:
    print("ERROR: transformers not installed!")
    print("Please run: pip install transformers")
    sys.exit(1)

print("=" * 60)
print("Simple RAG System - Starting...")
print("=" * 60)

# ============================================================
# STEP 2: DEFINE THE RAG CLASS
# ============================================================
# We'll create a class to organize our RAG system code

class SimpleRAG:
    """
    A simple Retrieval-Augmented Generation system.
    
    This class has three main jobs:
    1. Store documents and convert them to embeddings
    2. Find the most relevant document for a query
    3. Generate answers using a language model
    """
    
    def __init__(self):
        """
        Initialize the RAG system.
        
        This runs once when you create a new RAG object.
        It loads the models we'll use (this takes ~30 seconds on first run).
        """
        print("\n[1/3] Loading embedding model...")
        # Load a pre-trained model for creating embeddings
        # 'all-MiniLM-L6-v2' is small and fast, perfect for learning
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        print("[2/3] Loading language model...")
        # Load a small language model for generating answers
        # 'google/flan-t5-small' is tiny but works for demos
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            max_new_tokens=50  # Limit answer length
        )
        
        # These will store our documents and their embeddings
        self.documents = []
        self.embeddings = None
        
        print("[3/3] System ready!\n")
    
    def add_documents(self, docs):
        """
        Add documents to our knowledge base.
        
        Args:
            docs: A list of strings (your documents)
            
        What happens:
        1. Store the original text documents
        2. Convert each document to an embedding (vector)
        3. Store the embeddings for fast searching later
        """
        print(f"Adding {len(docs)} documents to knowledge base...")
        
        # Save the original documents
        self.documents = docs
        
        # Convert documents to embeddings
        # Each document becomes a vector of numbers (768 numbers in this case)
        self.embeddings = self.embedding_model.encode(docs)
        
        print(f"✓ Created embeddings for {len(docs)} documents")
        print(f"  Each embedding has {self.embeddings.shape[1]} dimensions\n")
    
    def retrieve(self, query, top_k=1):
        """
        Find the most relevant document(s) for a query.
        
        Args:
            query: The question or search query
            top_k: How many documents to return (default: 1)
            
        Returns:
            List of most relevant documents
            
        How it works:
        1. Convert the query to an embedding
        2. Compare it to all document embeddings using cosine similarity
        3. Return the document(s) with highest similarity scores
        """
        # Convert query to embedding
        query_embedding = self.embedding_model.encode([query])
        
        # Calculate similarity between query and all documents
        # Cosine similarity returns a value between -1 and 1
        # 1 = identical, 0 = unrelated, -1 = opposite
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Find the indices of the most similar documents
        # np.argsort sorts by similarity, we take the last top_k (highest values)
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Get the actual documents at those indices
        retrieved_docs = [self.documents[i] for i in top_indices]
        
        # Print which document was found (for learning purposes)
        print(f"\n📄 Retrieved document (similarity: {similarities[top_indices[0]]:.3f}):")
        print(f"   {retrieved_docs[0][:100]}...")
        
        return retrieved_docs
    
    def generate_answer(self, query, context):
        """
        Generate an answer using the language model.
        
        Args:
            query: The original question
            context: The retrieved document(s) to use as reference
            
        Returns:
            Generated answer as a string
            
        How it works:
        1. Create a prompt that combines context and question
        2. Pass it to the language model
        3. Return the model's response
        """
        # Create a prompt for the language model
        # We tell it to use the context to answer the question
        prompt = f"""Based on the following information, answer the question.
        
Context: {context}

Question: {query}

Answer:"""
        
        # Generate the answer
        result = self.generator(prompt)
        answer = result[0]['generated_text']
        
        return answer
    
    def answer(self, query):
        """
        Main method: Answer a question using RAG.
        
        This combines retrieval and generation into one easy function.
        
        Args:
            query: The question to answer
            
        Returns:
            The generated answer
        """
        print(f"\n❓ Question: {query}")
        
        # Step 1: Retrieve relevant document(s)
        retrieved_docs = self.retrieve(query, top_k=1)
        context = retrieved_docs[0]  # Get the top document
        
        # Step 2: Generate answer using the retrieved context
        answer = self.generate_answer(query, context)
        
        print(f"💡 Answer: {answer}\n")
        
        return answer


# ============================================================
# STEP 3: DEMO - USING THE RAG SYSTEM
# ============================================================
# Now let's actually use our RAG system!

if __name__ == "__main__":
    # Create a RAG system instance
    rag = SimpleRAG()
    
    # Create a small knowledge base
    # In a real application, you might have hundreds or thousands of documents
    documents = [
        "Python is a high-level programming language created by Guido van Rossum in 1991.",
        "Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
        "Neural networks are computing systems inspired by biological neural networks in the brain.",
        "The Transformer architecture was introduced in the 2017 paper 'Attention Is All You Need'.",
        "RAG stands for Retrieval-Augmented Generation, combining search with text generation."
    ]
    
    # Add documents to the system
    rag.add_documents(documents)
    
    print("=" * 60)
    print("Knowledge Base Ready! Asking questions...")
    print("=" * 60)
    
    # Ask some questions
    questions = [
        "Who created Python?",
        "What is machine learning?",
        "What are neural networks inspired by?",
        "When was the Transformer architecture introduced?",
        "What does RAG stand for?"
    ]
    
    # Get answers for each question
    for question in questions:
        rag.answer(question)
        print("-" * 60)
    
    print("\n✅ Demo complete!")
    print("\n💡 Try modifying the documents or adding your own questions!")
    print("=" * 60)
