class Retriever:
    def __init__(self, embedding_model, top_k=2):
        self.embedding_model = embedding_model
        self.top_k = top_k
    
    def retrieve(self, query):
        query_embedding = self.embedding_model.model.encode([query])
        distances, indices = self.embedding_model.index.search(np.array(query_embedding), self.top_k)
        return [self.embedding_model.documents[i] for i in indices[0]]