import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.documents = []

    def encode_documents(self, documents):
        if not documents:
            raise ValueError("No documents provided for encoding")
        self.documents = documents
        embeddings = self.model.encode(documents)
        if len(embeddings) == 0:
            raise ValueError("Failed to generate embeddings for documents")
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def get_index(self):
        return self.index
    
    def get_documents(self):
        return self.documents