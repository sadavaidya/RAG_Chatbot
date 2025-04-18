from src.components.embedding import EmbeddingModel
from src.components.retrieval import Retriever
from src.components.generation import Generator
from src.components.web_scraper import scrape_articles

class RAGPipeline:
    def __init__(self, documents):
        self.embedder = EmbeddingModel()
        self.embedder.encode_documents(documents)
        self.retriever = Retriever(self.embedder)
        self.generator = Generator()
    
    def run(self, query):
        relevant_docs = self.retriever.retrieve(query)
        context = " ".join(relevant_docs)
        return self.generator.generate(context, query)