# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
import traceback
import requests
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
        contextual_system_message_content = f"{system_prompt}{focus_content_prompt}{rag_context_prompt}"
        
        messages = []

        # Add the system message first, if it has content
        if contextual_system_message_content.strip():
            messages.append({"role": "system", "content": contextual_system_message_content.strip()})
        
        # Add cleaned historical messages (only user/assistant roles)
        for msg in user_history:
            if msg.get('role') in ['user', 'assistant']:
                messages.append(msg)
            else:
                logger.warning(f"Skipping invalid role '{msg.get('role')}' in chat history for user {user_id}: {msg}")

        # Add the current user's message
        messages.append({"role": "user", "content": final_user_content})
        
        # Limit total messages, ensuring system message and recent context are preserved
        # The API's token limit is important here, 15 is an arbitrary number.
        # It's better to limit by tokens rather than message count for large messages.
        # For now, we keep the last N messages (N=15 including system if present + current user)
        if len(messages) > 15:
            # Keep the system message (if any) and the last (15 - 1) actual conversation turns
            # This assumes the system message is always the first element if present
            if messages[0].get('role') == 'system':
                messages = [messages[0]] + messages[-(15-1):]
            else:
                messages = messages[-15:] # If no system message, just take last 15
        
        response, coins_used = call_chatbot_model(messages)
        total_coins_used += coins_used
        
        bot_response_content = response.choices[0].message.content
        
        # Update user history with the *new* conversation turn
        # Only append user and assistant messages for history, not system/context.
        user_history.append({"role": "user", "content": user_message}) # Original user message, not expanded
        user_history.append({"role": "assistant", "content": bot_response_content})
        save_user_history(user_id, user_history[-20:]) # Keep last 20 conversation turns in history file
        
        return {"history": user_history[-20:], "bot_response": bot_response_content, "coins_used": total_coins_used} # Return bot_response explicitly

    except Exception as e:
        logger.error(f"An unexpected error occurred in chatbot logic for user {user_id}: {traceback.format_exc()}")
        return {"error": f"Chatbot processing failed: {e}", "coins_used": total_coins_used}

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

        system_prompt_content = get_directive_and_personality()
        
        focus_content = ""
        if canvas_files:
            processed_files = [_process_file_for_prompt(fp) for fp in canvas_files]
            focus_content = "\n\n### PRIORITY CONTEXT: FOCUS DOCUMENTS\n" + "\n".join(processed_files)

        rag_context = ""
        try:
            # ## FIX 1: Removed the 'user_id' argument from the search_index call.
            # This resolves the TypeError warning seen in the logs.
            rag_chunks = search_index(user_message, k=3) 
            if rag_chunks:
                rag_context = "\n\n### ADDITIONAL CONTEXT: KNOWLEDGE BASE\n- " + "\n- ".join(rag_chunks)
        except Exception as e:
            logger.warning(f"RAG search failed: {e}. Proceeding without RAG context.")
            rag_context = "" 
        
        attached_file_context = ""
        if attached_files:
            processed_files = [_process_file_for_prompt(fp) for fp in attached_files]
            attached_file_context = "\n\n### ATTACHED FILE CONTEXT\n" + "\n".join(processed_files)

        full_system_message_content = f"{system_prompt_content}{focus_content}{rag_context}{attached_file_context}".strip()
        
        user_history = load_user_history(user_id)
        
        api_messages = []
        
        # ## FIX 2: The block that created the "system" role message has been removed.
        # Instead, the system content will be combined with the current user message.
        # This resolves the critical 'invalid_union_discriminator' BadRequestError.

        for msg in user_history:
            if msg.get('role') in ['user', 'assistant'] and isinstance(msg.get('content'), str):
                api_messages.append({"role": msg['role'], "content": msg['content']})
            else:
                logger.warning(f"Skipping invalid or malformed message in chat history for user {user_id}: {msg}")

        # ## FIX 2 (continued): Combine system instructions with the current user message.
        final_user_content = f"{full_system_message_content}\n\n{user_message}"
        api_messages.append({"role": "user", "content": final_user_content}) 
        
        max_conversation_turns = 10
        # The history limit logic needs to account for the fact that there is no separate system message anymore.
        if len(api_messages) > (max_conversation_turns * 2):
            # Just keep the last N conversation messages, as the system prompt is now part of the last user message.
            api_messages = api_messages[-(max_conversation_turns * 2):] 
            
        logger.debug(f"Sending messages to model: {json.dumps(api_messages, indent=2)}")

        response, coins_used = call_chatbot_model(api_messages)
        total_coins_used += coins_used
        
        bot_response_content = response.choices[0].message.content
        
        user_history.append({"role": "user", "content": user_message}) 
        user_history.append({"role": "assistant", "content": bot_response_content})
        save_user_history(user_id, user_history[-20:])
        
        return {"history": user_history[-20:], "bot_response": bot_response_content, "coins_used": total_coins_used, "message": "Chatbot responded."}

    except Exception as e:
        logger.error(f"An unexpected error occurred in chatbot logic for user {user_id}: {traceback.format_exc()}")
        return {"error": f"Chatbot processing failed: {e}", "coins_used": total_coins_used}

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
