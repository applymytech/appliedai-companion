# scripts/personality_manager.py
import os
import shutil
import json
from logger import setup_logger

logger = setup_logger('personality_manager')
PERSONALITIES_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'personalities')
KNOWLEDGE_BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge_base')

def get_personalities(api_key, payload, output_dir):
    """Returns a list of all user-created personality filenames."""
    if not os.path.exists(PERSONALITIES_DIR):
        return json.dumps({"personalities": []})
    # Exclude the default, sacred personality
    personalities = [f for f in os.listdir(PERSONALITIES_DIR) if f != 'gemma_app_manager.txt']
    return json.dumps({"personalities": personalities})

def create_personality(api_key, payload, output_dir):
    """Creates a new, empty personality file and its knowledge directory."""
    name = payload.get('name')
    if not name.endswith('.txt'):
        name += '.txt'
    personality_path = os.path.join(PERSONALITIES_DIR, name)
    knowledge_path = os.path.join(KNOWLEDGE_BASE_DIR, name.replace('.txt', ''))
    
    if os.path.exists(personality_path):
        raise ValueError(f"Personality '{name}' already exists.")
        
    with open(personality_path, 'w', encoding='utf-8') as f:
        f.write("### PERSONA NAME\nNew Personality\n\n### TONE\n\n### PRIMARY GOAL\n")
    os.makedirs(knowledge_path, exist_ok=True)
    logger.info(f"Created new personality: {name}")
    return json.dumps({"message": f"Successfully created {name}."})

def delete_personality(api_key, payload, output_dir):
    """Deletes a personality and its entire knowledge base."""
    name = payload.get('name')
    personality_path = os.path.join(PERSONALITIES_DIR, name)
    knowledge_path = os.path.join(KNOWLEDGE_BASE_DIR, name.replace('.txt', ''))
    
    if os.path.exists(personality_path):
        os.remove(personality_path)
    if os.path.exists(knowledge_path):
        shutil.rmtree(knowledge_path)
    logger.info(f"Deleted personality and knowledge for: {name}")
    return json.dumps({"message": f"Successfully deleted {name}."})