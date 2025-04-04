import streamlit as st
from src.pipeline.rag_pipeline import RAGPipeline
from src.components.web_scraper import scrape_articles

# Scrape news documents
url = ["https://www.bbc.com/news",
       "https://www.bbc.co.uk/news/england"]
documents = scrape_articles(url)

if not documents:
    st.error("No news articles found from the website")
else:
    # Initialize the chatbot pipeline with the scraped news documents
    chatbot = RAGPipeline(documents)

    # Streamlit app UI
    st.title("News Chatbot (using BBC)")

    # User input for querying the chatbot
    query = st.text_input("Ask me about news today:")

    # Button to get the chatbot's response
    if st.button("Get Answer"):
        if query:
            response = chatbot.run(query)
            st.write("**Chatbot Response:**", response)
        else:
            st.warning("Please enter a question!")
