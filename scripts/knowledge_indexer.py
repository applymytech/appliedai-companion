import os
import re
from vector_store import create_embeddings, build_and_save_index

KNOWLEDGE_BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge_base')

def chunk_text(text, chunk_size=500, overlap=50):
    """Splits text into overlapping chunks."""
    # A simple sentence-based chunking strategy
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

def reindex_knowledge_base(api_key, payload, output_dir):
    """Reads all knowledge files, chunks them, and builds a vector index."""
    all_chunks = []
    
    # Iterate through all users' knowledge bases
    for user_id in os.listdir(KNOWLEDGE_BASE_DIR):
        user_path = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
        if os.path.isdir(user_path):
            for filename in os.listdir(user_path):
                if filename.endswith(".md"):
                    file_path = os.path.join(user_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        chunks = chunk_text(content)
                        all_chunks.extend(chunks)

    if not all_chunks:
        return {"message": "No knowledge files found to index."}

    # Generate embeddings and build the index
    embeddings = create_embeddings(all_chunks)
    build_and_save_index(embeddings, all_chunks)
    
    return {"message": f"Successfully indexed {len(all_chunks)} text chunks."}