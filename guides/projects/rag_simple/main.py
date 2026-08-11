"""
Simple RAG (Retrieval-Augmented Generation) System
====================================================

A minimal, fully-commented implementation of a RAG system.
Perfect for beginners learning about retrieval-augmented generation.

This demo intentionally uses a small corpus and a small generator. It is an
educational example, not a production RAG implementation.
"""

import sys

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("ERROR: sentence-transformers not installed!")
    print("Please run: pip install sentence-transformers")
    sys.exit(1)

try:
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    print("ERROR: scikit-learn not installed!")
    print("Please run: pip install scikit-learn")
    sys.exit(1)

import numpy as np

try:
    from transformers import pipeline
except ImportError:
    print("ERROR: transformers not installed!")
    print("Please run: pip install transformers")
    sys.exit(1)


class SimpleRAG:
    """A small educational retrieval-augmented generation pipeline."""

    def __init__(self):
        print("\n[1/3] Loading embedding model...")
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

        print("[2/3] Loading language model...")
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            max_new_tokens=50,
        )

        self.documents = []
        self.embeddings = None
        print("[3/3] System ready!\n")

    def add_documents(self, docs):
        """Replace the knowledge base with *docs* and encode them."""
        if not docs:
            raise ValueError("docs must contain at least one document")

        self.documents = list(docs)
        self.embeddings = self.embedding_model.encode(
            self.documents,
            normalize_embeddings=True,
        )

        print(f"Created embeddings for {len(self.documents)} documents")
        print(f"Each embedding has {self.embeddings.shape[1]} dimensions\n")

    def retrieve(self, query, top_k=1):
        """Return the top-k documents by cosine similarity."""
        if self.embeddings is None:
            raise RuntimeError("Add documents before retrieving")
        if top_k < 1:
            raise ValueError("top_k must be at least 1")

        top_k = min(top_k, len(self.documents))
        query_embedding = self.embedding_model.encode(
            [query],
            normalize_embeddings=True,
        )
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        retrieved_docs = [self.documents[i] for i in top_indices]
        print(f"\nRetrieved document (similarity: {similarities[top_indices[0]]:.3f}):")
        print(f"   {retrieved_docs[0][:100]}...")
        return retrieved_docs

    def generate_answer(self, query, context):
        """Generate an answer using only the supplied retrieved context."""
        if isinstance(context, (list, tuple)):
            context = "\n\n".join(context)

        prompt = f"""Answer the question using only the information in the context.
If the context does not contain the answer, say that the information is not available.

Context:
{context}

Question: {query}

Answer:"""
        result = self.generator(prompt)
        return result[0]["generated_text"]

    def answer(self, query, top_k=1):
        """Retrieve relevant context and generate an answer."""
        print(f"\nQuestion: {query}")
        retrieved_docs = self.retrieve(query, top_k=top_k)
        answer = self.generate_answer(query, retrieved_docs)
        print(f"Answer: {answer}\n")
        return answer


if __name__ == "__main__":
    rag = SimpleRAG()

    documents = [
        "Python is a high-level programming language created by Guido van Rossum in 1991.",
        "Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
        "Neural networks are computing systems inspired by biological neural networks in the brain.",
        "The Transformer architecture was introduced in the 2017 paper 'Attention Is All You Need'.",
        "RAG stands for Retrieval-Augmented Generation, combining search with text generation.",
    ]

    rag.add_documents(documents)

    questions = [
        "Who created Python?",
        "What is machine learning?",
        "What are neural networks inspired by?",
        "When was the Transformer architecture introduced?",
        "What does RAG stand for?",
    ]

    for question in questions:
        rag.answer(question)
        print("-" * 60)

    print("\nDemo complete!")
