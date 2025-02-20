from src.pipeline.rag_pipeline import RAGPipeline

documents = ["AI is transforming the world.", "LLMs can be fine-tuned for tasks.", "RAG improves chatbot accuracy."]
chatbot = RAGPipeline(documents)

query = "How does RAG help chatbots?"
response = chatbot.run(query)
print("Chatbot Response:", response)