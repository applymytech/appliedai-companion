# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
import traceback
from logger import setup_logger
from vector_store import search_index, init_client as init_vector_store_client
# Import the new, centralized API call wrappers
from api_clients import get_aimlapi_client, call_chatbot_model

logger = setup_logger('chatbot')

# =============================================================================
# SECTION 2: CONFIGURATION & PATHS
# =============================================================================
APP_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CHAT_HISTORY_DIR = os.path.join(APP_DATA_DIR, 'chat_histories')
PERSONALITY_DIR = os.path.join(APP_DATA_DIR, 'gemma_personality')
DIRECTIVE_FILE = os.path.join(PERSONALITY_DIR, 'directive.md')

os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)
os.makedirs(PERSONALITY_DIR, exist_ok=True)

# =============================================================================
# SECTION 3: HELPER FUNCTIONS
# =============================================================================

def get_directive_and_personality():
    """Reads and combines the base system directive and personality file."""
    directive = "You are a helpful AI assistant."
    personality = ""
    
    try:
        with open(DIRECTIVE_FILE, 'r', encoding='utf-8') as f:
            directive = f.read()
    except FileNotFoundError:
        logger.warning(f"Directive file not found at {DIRECTIVE_FILE}. Using default.")

    try:
        personality_path = os.path.join(PERSONALITY_DIR, 'gemma_app_manager.md')
        with open(personality_path, 'r', encoding='utf-8') as f:
            personality = f.read()
    except FileNotFoundError:
        logger.warning(f"Personality file not found at {personality_path}.")

    return f"{directive}\n\n### PERSONALITY BRIEF\n{personality}"

def load_user_history(user_id):
    """Loads a user's chat history from a JSON file."""
    try:
        with open(os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json"), 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_user_history(user_id, history):
    """Saves a user's chat history to a JSON file."""
    with open(os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json"), 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)

def _process_file_for_prompt(file_path):
    """Reads the content of a file to be injected into a prompt."""
    try:
        filename = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            return f"--- START OF FILE: {filename} ---\n{content}\n--- END OF FILE ---"
    except Exception as e:
        logger.error(f"Error processing attached file {file_path}: {e}")
        return f"[Error processing file: {os.path.basename(file_path)}]"

# =============================================================================
# SECTION 4: CORE CHATBOT LOGIC (HYBRID RAG IMPLEMENTATION)
# =============================================================================
def run_chatbot_logic(user_id, user_message, attached_files, canvas_files):
    """Manages the main chatbot conversation flow using the Hybrid RAG model."""
    total_coins_used = 0
    try:
        init_vector_store_client(get_aimlapi_client())

        system_prompt = get_directive_and_personality()
        
        focus_content_prompt = ""
        if canvas_files:
            processed_files = [_process_file_for_prompt(fp) for fp in canvas_files]
            focus_content_prompt = "\n\n### PRIORITY CONTEXT: FOCUS DOCUMENTS\n" + "\n".join(processed_files)

        rag_chunks = search_index(user_message, k=3)
        rag_context_prompt = ""
        if rag_chunks:
            rag_context_prompt = "\n\n### ADDITIONAL CONTEXT: KNOWLEDGE BASE\n- " + "\n- ".join(rag_chunks)
        
        attached_file_prompt = ""
        if attached_files:
            processed_files = [_process_file_for_prompt(fp) for fp in attached_files]
            attached_file_prompt = "\n\n### ATTACHED FILE CONTEXT\n" + "\n".join(processed_files)

        user_history = load_user_history(user_id)
        final_user_content = f"{user_message}{attached_file_prompt}"
        contextual_system_message = f"{system_prompt}{focus_content_prompt}{rag_context_prompt}"
        
        messages = user_history + [
            {"role": "system", "content": contextual_system_message},
            {"role": "user", "content": final_user_content}
        ]
        messages = messages[-15:]

        response, coins_used = call_chatbot_model(messages)
        total_coins_used += coins_used
        
        bot_response_content = response.choices[0].message.content
        
        user_history.append({"role": "user", "content": user_message})
        user_history.append({"role": "assistant", "content": bot_response_content})
        save_user_history(user_id, user_history[-20:])
        
        return {"history": user_history, "coins_used": total_coins_used}

    except Exception as e:
        logger.error(f"An unexpected error occurred in chatbot logic: {traceback.format_exc()}")
        return {"error": str(e), "coins_used": total_coins_used}

# =============================================================================
# SECTION 5: ADAPTER FUNCTIONS FOR SCRIPT ROUTER
# =============================================================================
def get_chatbot_response_adapter(payload, output_dir):
    user_id = payload.get('uid')
    if not user_id: return {"error": "Missing user ID.", "coins_used": 0}
    
    return run_chatbot_logic(
        user_id=user_id,
        user_message=payload.get('message', ''),
        attached_files=payload.get('attached_files', []),
        canvas_files=payload.get('canvas_files', [])
    )

def clear_chat_history_adapter(payload, output_dir):
    user_id = payload.get('uid')
    if not user_id: return {"error": "Missing user ID.", "coins_used": 0}
    
    history_path = os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json")
    if os.path.exists(history_path):
        os.remove(history_path)
    
    return {"message": "Chat history cleared successfully.", "coins_used": 0}
# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
import traceback
from logger import setup_logger
from vector_store import search_index, init_client as init_vector_store_client
# Import the new, centralized API call wrappers
from api_clients import get_aimlapi_client, call_chatbot_model

logger = setup_logger('chatbot')

# =============================================================================
# SECTION 2: CONFIGURATION & PATHS
# =============================================================================
APP_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CHAT_HISTORY_DIR = os.path.join(APP_DATA_DIR, 'chat_histories')
PERSONALITY_DIR = os.path.join(APP_DATA_DIR, 'gemma_personality')
DIRECTIVE_FILE = os.path.join(PERSONALITY_DIR, 'directive.md')

os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)
os.makedirs(PERSONALITY_DIR, exist_ok=True)

# =============================================================================
# SECTION 3: HELPER FUNCTIONS
# =============================================================================

def get_directive_and_personality():
    """Reads and combines the base system directive and personality file."""
    directive = "You are a helpful AI assistant."
    personality = ""
    
    try:
        with open(DIRECTIVE_FILE, 'r', encoding='utf-8') as f:
            directive = f.read()
    except FileNotFoundError:
        logger.warning(f"Directive file not found at {DIRECTIVE_FILE}. Using default.")

    try:
        personality_path = os.path.join(PERSONALITY_DIR, 'gemma_app_manager.md')
        with open(personality_path, 'r', encoding='utf-8') as f:
            personality = f.read()
    except FileNotFoundError:
        logger.warning(f"Personality file not found at {personality_path}.")

    return f"{directive}\n\n### PERSONALITY BRIEF\n{personality}"

def load_user_history(user_id):
    """Loads a user's chat history from a JSON file."""
    try:
        with open(os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json"), 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_user_history(user_id, history):
    """Saves a user's chat history to a JSON file."""
    with open(os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json"), 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)

def _process_file_for_prompt(file_path):
    """Reads the content of a file to be injected into a prompt."""
    try:
        filename = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            return f"--- START OF FILE: {filename} ---\n{content}\n--- END OF FILE ---"
    except Exception as e:
        logger.error(f"Error processing attached file {file_path}: {e}")
        return f"[Error processing file: {os.path.basename(file_path)}]"

# =============================================================================
# SECTION 4: CORE CHATBOT LOGIC (HYBRID RAG IMPLEMENTATION)
# =============================================================================
def run_chatbot_logic(user_id, user_message, attached_files, canvas_files):
    """Manages the main chatbot conversation flow using the Hybrid RAG model."""
    total_coins_used = 0
    try:
        init_vector_store_client(get_aimlapi_client())

        system_prompt = get_directive_and_personality()
        
        focus_content_prompt = ""
        if canvas_files:
            processed_files = [_process_file_for_prompt(fp) for fp in canvas_files]
            focus_content_prompt = "\n\n### PRIORITY CONTEXT: FOCUS DOCUMENTS\n" + "\n".join(processed_files)

        rag_chunks = search_index(user_message, k=3)
        rag_context_prompt = ""
        if rag_chunks:
            rag_context_prompt = "\n\n### ADDITIONAL CONTEXT: KNOWLEDGE BASE\n- " + "\n- ".join(rag_chunks)
        
        attached_file_prompt = ""
        if attached_files:
            processed_files = [_process_file_for_prompt(fp) for fp in attached_files]
            attached_file_prompt = "\n\n### ATTACHED FILE CONTEXT\n" + "\n".join(processed_files)

        user_history = load_user_history(user_id)
        final_user_content = f"{user_message}{attached_file_prompt}"
        contextual_system_message = f"{system_prompt}{focus_content_prompt}{rag_context_prompt}"
        
        messages = user_history + [
            {"role": "system", "content": contextual_system_message},
            {"role": "user", "content": final_user_content}
        ]
        messages = messages[-15:]

        response, coins_used = call_chatbot_model(messages)
        total_coins_used += coins_used
        
        bot_response_content = response.choices[0].message.content
        
        user_history.append({"role": "user", "content": user_message})
        user_history.append({"role": "assistant", "content": bot_response_content})
        save_user_history(user_id, user_history[-20:])
        
        return {"history": user_history, "coins_used": total_coins_used}

    except Exception as e:
        logger.error(f"An unexpected error occurred in chatbot logic: {traceback.format_exc()}")
        return {"error": str(e), "coins_used": total_coins_used}

# =============================================================================
# SECTION 5: ADAPTER FUNCTIONS FOR SCRIPT ROUTER
# =============================================================================
def get_chatbot_response_adapter(payload, output_dir):
    user_id = payload.get('uid')
    if not user_id: return {"error": "Missing user ID.", "coins_used": 0}
    
    return run_chatbot_logic(
        user_id=user_id,
        user_message=payload.get('message', ''),
        attached_files=payload.get('attached_files', []),
        canvas_files=payload.get('canvas_files', [])
    )

def clear_chat_history_adapter(payload, output_dir):
    user_id = payload.get('uid')
    if not user_id: return {"error": "Missing user ID.", "coins_used": 0}
    
    history_path = os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json")
    if os.path.exists(history_path):
        os.remove(history_path)
    
    return {"message": "Chat history cleared successfully.", "coins_used": 0}
