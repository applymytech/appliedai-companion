import os
import re
# Assuming 'logger' means the custom setup_logger from your project
from logger import setup_logger 
from vector_store import create_embeddings, build_and_save_index
from api_clients import get_aimlapi_client # Added this as discussed for vector_store client init

# Initialize logger for this script
logger = setup_logger('knowledge_indexer')

KNOWLEDGE_BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge_base')

def chunk_text(text, chunk_size=500, overlap=50):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def reindex_knowledge_base(payload, output_dir): # Adapter pattern
    user_id = payload.get('uid') # Get user_id from payload
    
    all_chunks = []
    target_dirs = []

    if user_id:
        user_kb_path = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
        if os.path.isdir(user_kb_path):
            target_dirs.append(user_kb_path)
    else:
        # If no user_id, iterate through all users' knowledge bases
        for u_id in os.listdir(KNOWLEDGE_BASE_DIR):
            user_path = os.path.join(KNOWLEDGE_BASE_DIR, u_id)
            if os.path.isdir(user_path):
                target_dirs.append(user_path)

    if not target_dirs:
        return {"message": "No user knowledge directories found to index.", "coins_used": 0}

    # Initialize vector store client (important for create_embeddings)
    # This assumes init_client from vector_store takes the aimlapi_client
    # from api_clients.
    # TODO: This may need to be handled more robustly by passing the client.
    # For now, it implicitly assumes vector_store can get the client.
    # We may need to pass the client down from script_router, or ensure
    # get_aimlapi_client() can be called from vector_store.py if it's not.
    # A better solution is to call init_vector_store_client with get_aimlapi_client()
    # at the start of script_router, or wherever it's first used.

    for current_dir in target_dirs:
        for filename in os.listdir(current_dir):
            if filename.endswith(".md"): # Only index markdown files
                file_path = os.path.join(current_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    chunks = chunk_text(content)
                    all_chunks.extend(chunks)

    if not all_chunks:
        return {"message": "No knowledge files found to index for the specified user(s).", "coins_used": 0}

    # Generate embeddings and build the index
    # IMPORTANT: The create_embeddings and build_and_save_index functions
    # in vector_store.py must use the AIMLAPI client.
    # If vector_store.py does not get the client via init_client(),
    # then this call might fail.
    # For now, assuming init_client is called correctly elsewhere, or
    # create_embeddings uses a globally initialized client.
    try:
        # Ensure the vector store client is initialized before using it.
        # This might be redundant if init_client is handled by vector_store itself on import or first use.
        # However, to be safe:
        # from vector_store import init_client
        # init_client(get_aimlapi_client())

        embeddings_response, embed_coins = create_embeddings(all_chunks) # create_embeddings should return coins
        build_and_save_index(embeddings_response, all_chunks, user_id=user_id) # Pass user_id to save index per user
        
        return {"message": f"Successfully indexed {len(all_chunks)} text chunks.", "coins_used": embed_coins}
    except Exception as e:
        logger.error(f"Error during knowledge base reindexing: {e}", exc_info=True)
        return {"error": f"Failed to reindex knowledge base: {e}", "coins_used": 0}
