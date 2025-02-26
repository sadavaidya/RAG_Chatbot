# RAG-Based Chatbot with Web Scraping

This project implements a Retrieval-Augmented Generation (RAG) chatbot that scrapes content from specified websites and uses it to answer user queries. The chatbot retrieves relevant information from the scraped data and generates responses using a language model.

## Features

- **Web Scraping**: Extracts content from specified URLs to build a knowledge base.
- **Retrieval-Augmented Generation**: Combines information retrieval with text generation to provide accurate and contextually relevant answers.
- **Streamlit Interface**: Offers an interactive web-based interface for user interaction.
- **Docker Support**: Containerized application for easy deployment.

## Installation

### Prerequisites

- Python 3.9 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Docker](https://www.docker.com/get-started) (optional, for containerized deployment)

### Clone the Repository

```bash
git clone https://github.com/sadavaidya/RAG_Chatbot.git
cd RAG_Chatbot
```

### Install Dependencies

Using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Chatbot Locally

1. **Start the Streamlit Application**:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the Chatbot**:

   Open your browser and navigate to `http://localhost:8501` to start interacting with the chatbot.

### Running the Chatbot with Docker

1. **Build the Docker Image**:

   ```bash
   docker build -t rag_chatbot .
   ```

2. **Run the Docker Container**:

   ```bash
    docker run --gpus all -p 8501:8501 rag_chatbot
   ```

   The application will be accessible at `http://localhost:8501`.

## Project Structure

```
RAG_Chatbot/
├── src/
│   ├── components/
│   │   ├── embedding.py
│   │   ├── generation.py
│   │   ├── retrieval.py
│   │   └── web_scraper.py
│   ├── pipeline/
│   │   └── rag_pipeline.py
│   └── utils.py
├── app.py
├── requirements.txt
└── Dockerfile
```

- `src/components/`: Contains modules for embedding, generation, retrieval, and web scraping.
- `src/pipeline/`: Defines the RAG pipeline that integrates the components.
- `app.py`: Streamlit application entry point.
- `requirements.txt`: Lists Python dependencies.
- `Dockerfile`: Defines the Docker image configuration.

## How It Works

1. **Web Scraping**: The `web_scraper.py` module fetches content from specified URLs and processes it into a list of documents.

2. **Embedding**: The `embedding.py` module encodes these documents into vector representations using a pre-trained model.

3. **Retrieval**: The `retrieval.py` module searches for documents relevant to the user's query based on vector similarity.

4. **Generation**: The `generation.py` module uses a language model to generate a response, conditioning on the retrieved documents and the user's query.

5. **Pipeline Integration**: The `rag_pipeline.py` module orchestrates the embedding, retrieval, and generation components to produce a final answer.

6. **User Interface**: The `app.py` file sets up a Streamlit web interface where users can input queries and receive responses from the chatbot.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/sadavaidya/RAG_Chatbot/blob/main/LICENSE) file for details.

---

*Note: Ensure that the URLs specified for web scraping in the `web_scraper.py` module are accessible and that scraping them complies with their terms of service.*

