# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
import numpy as np
from import faiss 
from logger import setup_logger

logger = setup_logger('vector_store')

# =============================================================================
# SECTION 2: CONFIGURATION
# =============================================================================
STORE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'vector_store')
INDEX_PATH = os.path.join(STORE_DIR, 'knowledge.index')
TEXT_MAP_PATH = os.path.join(STORE_DIR, 'text_map.json')

os.makedirs(STORE_DIR, exist_ok=True)

# This client will be initialized once by the main chatbot script
client = None

# =============================================================================
# SECTION 3: CORE FUNCTIONS
# =============================================================================
def init_client(api_client):
    """Initializes this module with an active API client from another script."""
    global client
    if client is None:
        client = api_client
        logger.info("Vector store has been initialized with the API client.")

def create_embeddings(text_chunks):
    """
    Calls the AIMLAPI service to convert text chunks into vector embeddings.
    NOTE: This function now relies on the centralized api_clients.py, but is
          called from here to keep the logic organized.
    """
    # This is a placeholder for the actual call which will be moved to api_clients.py
    # For now, we assume the client is the openai client.
    if client is None:
        raise Exception("API client not initialized in vector_store.")
    
    # This logic will be replaced by a call to api_clients.call_embedding_model
    from api_clients import call_embedding_model
    response, coins_used = call_embedding_model(text_chunks)
    embeddings = [record.embedding for record in response.data]
    return np.array(embeddings), coins_used

def build_and_save_index(embeddings, text_chunks):
    """Builds and saves a FAISS index."""
    if embeddings.size == 0:
        logger.warning("No embeddings were generated. Cannot build index.")
        return

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    text_map = {i: text for i, text in enumerate(text_chunks)}
    with open(TEXT_MAP_PATH, 'w', encoding='utf-8') as f:
        json.dump(text_map, f)
    logger.info(f"Successfully built and saved index with {len(text_chunks)} chunks.")

def search_index(query_text, k=5):
    """Searches the index for the most relevant text chunks."""
    if not os.path.exists(INDEX_PATH):
        return []

    index = faiss.read_index(INDEX_PATH)
    with open(TEXT_MAP_PATH, 'r', encoding='utf-8') as f:
        text_map = json.load(f)

    query_embedding, _ = create_embeddings([query_text])
    if query_embedding.size == 0:
        return []

    distances, indices = index.search(query_embedding, k)
    
    results = [text_map[str(i)] for i in indices[0] if str(i) in text_map]
    return results
