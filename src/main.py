import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

import torch
torch.set_num_threads(1)

import streamlit as st


from src.pipeline.rag_pipeline import RAGPipeline
from src.components.web_scraper import scrape_news


# Example news URLs, replace with real URLs
urls = ["https://www.bbc.com/news", "https://www.bbc.co.uk/news/england"]

# Scrape news from the URLs
documents = scrape_news(urls)

# Check if news articles are found
if not documents:
    raise ValueError("No news articles found from the website")

# Initialize RAG chatbot pipeline with scraped documents
chatbot = RAGPipeline(documents)

# Example query
query = "What are the latest news updates?"

# Get the response from the chatbot
response = chatbot.run(query)

# Print chatbot response
print("Chatbot Response:", response)
