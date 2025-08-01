import os
import json
import numpy as np
import faiss
# REMOVED: from sentence_transformers import SentenceTransformer
# ADDED: Import the OpenAI client, which is used to interact with AIMLAPI
from openai import OpenAI

# --- CONFIGURATION ---
STORE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'vector_store')
INDEX_PATH = os.path.join(STORE_DIR, 'knowledge.index')
TEXT_MAP_PATH = os.path.join(STORE_DIR, 'text_map.json')

os.makedirs(STORE_DIR, exist_ok=True)

# This client will be initialized once by the main chatbot script
client = None

def init_client(api_client):
    """Initializes this module with an active API client from another script."""
    global client
    if client is None:
        client = api_client
        print("Vector store has been initialized with the API client.")

def create_embeddings(text_chunks):
    """
    Calls the AIMLAPI service to convert text chunks into vector embeddings.
    """
    if client is None:
        raise Exception("API client not initialized in vector_store. Please call init_client first.")

    try:
        # CORRECT: This makes a network API call to AIMLAPI
        res = client.embeddings.create(
            input=text_chunks,
            model="google/textembedding-gecko@003" # The model you selected
        )
        # Extract the vector embeddings and token count from the API response
        embeddings = [record.embedding for record in res.data]
        tokens_used = res.usage.total_tokens
        return np.array(embeddings), tokens_used
    except Exception as e:
        print(f"Error calling AIMLAPI for embeddings: {e}")
        return np.array([]), 0


def build_and_save_index(embeddings, text_chunks):
    """Builds and saves a FAISS index. (No changes needed here)."""
    if embeddings.size == 0:
        print("No embeddings were generated. Cannot build index.")
        return

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    text_map = {i: text for i, text in enumerate(text_chunks)}
    with open(TEXT_MAP_PATH, 'w', encoding='utf-8') as f:
        json.dump(text_map, f)
    print(f"Successfully built and saved index with {len(text_chunks)} chunks.")

def search_index(query_text, k=5):
    """Searches the index for the most relevant text chunks."""
    if not os.path.exists(INDEX_PATH):
        return []

    index = faiss.read_index(INDEX_PATH)
    with open(TEXT_MAP_PATH, 'r', encoding='utf-8') as f:
        text_map = json.load(f)

    # CORRECT: Use the API to create an embedding for the user's query
    query_embedding, _ = create_embeddings([query_text]) # We don't need the token count here
    if query_embedding.size == 0:
        return []

    # Perform the search
    distances, indices = index.search(query_embedding, k)
    
    results = [text_map[str(i)] for i in indices[0] if str(i) in text_map]
    return results