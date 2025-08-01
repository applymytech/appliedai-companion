# /scripts/chatbot_request.py (Final Version - All Functions Preserved)

# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import sys
import json
import traceback
import httpx
import shutil
import subprocess
from vector_store import search_index
from openai import OpenAI
from logger import setup_logger
from ai_utils import get_ai_chat_summary, summarize_web_search_results
from vector_store import init_client as init_vector_store_client


logger = setup_logger('chatbot')
client = None

# =============================================================================
# SECTION 2: CONFIGURATION & PATHS
# =============================================================================
APP_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
CHAT_HISTORY_DIR = os.path.join(APP_DATA_DIR, 'chat_histories')
KNOWLEDGE_BASE_DIR = os.path.join(APP_DATA_DIR, 'knowledge_base')
APP_KNOWLEDGE_DIR = os.path.join(APP_DATA_DIR, 'app_knowledge')
PERSONALITIES_DIR = os.path.join(APP_DATA_DIR, 'personalities')
DIRECTIVE_FILE = os.path.join(APP_DATA_DIR, 'directive.txt')

os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)
os.makedirs(KNOWLEDGE_BASE_DIR, exist_ok=True)
os.makedirs(APP_KNOWLEDGE_DIR, exist_ok=True)
os.makedirs(PERSONALITIES_DIR, exist_ok=True)


# =============================================================================
# SECTION 3: HELPER FUNCTIONS
# =============================================================================
def get_directive():
    try:
        with open(DIRECTIVE_FILE, 'r', encoding='utf-8') as f: return f.read()
    except FileNotFoundError: return "You are a helpful AI assistant."

def get_personality_brief(personality_filename):
    if not personality_filename: return ""
    try:
        with open(os.path.join(PERSONALITIES_DIR, personality_filename), 'r', encoding='utf-8') as f: return f.read()
    except FileNotFoundError:
        logger.error(f"Personality file not found: {personality_filename}")
        return ""

def load_user_history(user_id):
    try:
        with open(os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json"), 'r', encoding='utf-8') as f: return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): return []

def save_user_history(user_id, history):
    with open(os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json"), 'w', encoding='utf-8') as f: json.dump(history, f, indent=2)

def init_api_client(api_key):
    global client
    base_url = "https://api.aimlapi.com/v1"
    if client is None or getattr(client, 'api_key', '') != api_key:
        try:
            client = OpenAI(api_key=api_key, base_url=base_url, http_client=httpx.Client(trust_env=False))
            init_vector_store_client(client)
            logger.info("AIMLAPI client initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize AIMLAPI client: {e}", exc_info=True)
            client = None
    return client

def get_knowledge_base_content(user_id, directory):
    user_specific_path = os.path.join(directory, user_id) if user_id else directory
    if not os.path.exists(user_specific_path): return ""
    all_content = []
    try:
        for filename in os.listdir(user_specific_path):
            file_path = os.path.join(user_specific_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(5000)
                    all_content.append(f"--- START OF KNOWLEDGE FILE: {filename} ---\n{content}\n--- END OF KNOWLEDGE FILE ---")
    except Exception as e:
        logger.error(f"Error reading knowledge base for path {user_specific_path}: {e}")
    return "\n\n".join(all_content)

def call_api_handler_function(function_name, payload):
    script_path = os.path.join(os.path.dirname(__file__), 'api_handler.py')
    api_key = os.environ.get('AIML_API_KEY', '')
    output_dir = os.environ.get('OUTPUT_PATH', '')
    command = [sys.executable, script_path, function_name, api_key, json.dumps(payload), output_dir]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8')
        return json.loads(result.stdout.strip())
    except Exception as e:
        logger.error(f"Error calling api_handler for {function_name}: {e}")
        raise

def _process_attached_file(file_path):
    try:
        _, extension = os.path.splitext(file_path)
        filename = os.path.basename(file_path)
        text_extensions = ['.txt', '.md', '.py', '.js', '.html', '.css', '.json', '.xml']
        if extension.lower() in text_extensions:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(5000)
                return f"--- START OF ATTACHED FILE: {filename} ---\n{content}\n--- END OF ATTACHED FILE ---"
        else:
            return f"[User has attached a non-text file: '{filename}'. You cannot read its content, but you should acknowledge its presence.]"
    except Exception as e:
        logger.error(f"Error processing attached file {file_path}: {e}")
        return f"[Error processing attached file: {os.path.basename(file_path)}]"

# =============================================================================
# SECTION 4: CORE CHATBOT LOGIC
# =============================================================================
def run_chatbot_logic(user_id, user_message, attached_files, canvas_files, personality_file):
    try:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: return {"error": "API key not configured."}
        if not init_api_client(api_key): return {"error": "Failed to initialize AI client."}

        # --- System Prompt Assembly ---
        personality_brief = get_personality_brief(personality_file)
        app_knowledge_prompt = get_knowledge_base_content(None, APP_KNOWLEDGE_DIR)
        user_knowledge_prompt = get_knowledge_base_content(user_id, KNOWLEDGE_BASE_DIR)
        
        # --- File Content Processing ---
        canvas_content_prompt = ""
        if canvas_files:
            processed_canvas_files = [_process_attached_file(fp) for fp in canvas_files]
            canvas_content_prompt = "\n\n### FOCUS CANVAS CONTEXT\nThe following files are the primary focus of this session:\n" + "\n".join(processed_canvas_files)
        
        attached_file_prompt = ""
        if attached_files:
            processed_attached_files = [_process_attached_file(fp) for fp in attached_files]
            attached_file_prompt = "\n\n### ATTACHED FILE CONTEXT\nUse the following file(s) for this specific query:\n" + "\n".join(processed_attached_files)

        system_prompt = get_directive()
        system_prompt += "\n\nYour primary goal is to assist the user using your internal knowledge and provided files."
        if personality_brief: system_prompt += "\n\n### PERSONALITY BRIEF\n" + personality_brief
        if app_knowledge_prompt: system_prompt += "\n\n### APP INFO\n" + app_knowledge_prompt
        if user_knowledge_prompt: system_prompt += "\n\n### KNOWLEDGE FILE\n" + user_knowledge_prompt
        
        # --- Message Construction ---
        user_history = load_user_history(user_id)
        final_user_content = f"USER'S QUERY: {user_message}{attached_file_prompt}"
        contextual_user_message = f"{system_prompt}{canvas_content_prompt}\n\n---\n\n{final_user_content}"
        
        messages = user_history + [{"role": "user", "content": contextual_user_message}]
        messages = messages[-15:]

        # --- API Call ---
        response = client.chat.completions.create(
            model=os.environ.get('AIMLAPI_MODEL', "google/gemma-2-27b-it"),
            messages=messages,
            tools=[{"type": "function", "function": {"name": "web_search", "description": "Performs a web search.", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}}}]
        )
        bot_response_message = response.choices[0].message
        bot_response_content = bot_response_message.content

        # --- Tool Call Handling ---
        if bot_response_message.tool_calls:
            tool_call = bot_response_message.tool_calls[0]
            if tool_call.function.name == "web_search":
                search_query = json.loads(tool_call.function.arguments).get("query")
                logger.info(f"AI requested web search for: '{search_query}'")
                user_history.extend([{"role": "user", "content": user_message}, bot_response_message])
                
                web_search_result = call_api_handler_function('perform_web_search', {'query': search_query})
                search_results_list = web_search_result.get('results', [])
                
                summary, citations, _ = summarize_web_search_results(json.dumps(search_results_list), search_query, api_key)
                citations_text = "\n\n**Sources:**\n" + "\n".join([f"- [{c['title']}]({c['url']})" for c in citations]) if citations else ""
                tool_response_content = f"Web Search Results for \"{search_query}\":\n{summary}{citations_text}"

                messages_for_final_response = messages + [bot_response_message, {"role": "tool", "tool_call_id": tool_call.id, "name": tool_call.function.name, "content": tool_response_content}]
                
                final_response = client.chat.completions.create(model=os.environ.get('AIMLAPI_MODEL', "google/gemma-2-27b-it"), messages=messages_for_final_response)
                bot_response_content = final_response.choices[0].message.content
        
        # --- History Saving ---
        user_history.append({"role": "user", "content": user_message})
        user_history.append({"role": "assistant", "content": bot_response_content})
        save_user_history(user_id, user_history[-20:])
        
        return user_history

    except Exception as e:
        logger.error(f"An unexpected error occurred in chatbot logic: {traceback.format_exc()}")
        return {"error": str(e)}

# =============================================================================
# SECTION 5: ADAPTER FUNCTIONS (Entry points from api_handler.py)
# =============================================================================
def get_chatbot_response(api_key, payload, output_dir):
    user_id = payload.get('uid')
    if not user_id: return json.dumps({"error": "Missing user ID."})
    
    result = run_chatbot_logic(
        user_id=user_id,
        user_message=payload.get('message'),
        attached_files=payload.get('attached_files', []),
        canvas_files=payload.get('canvas_files', []),
        personality_file=payload.get('personality', 'gemma_app_manager.txt')
    )
    
    if isinstance(result, dict) and 'error' in result:
        return json.dumps(result)
    return json.dumps({"history": result})

def clear_chat_history(api_key, payload, output_dir):
    user_id = payload.get('uid')
    mode = payload.get('mode', 'delete')
    if not user_id: return json.dumps({"error": "Missing user ID in payload."})

    history_path = os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json")
    if not os.path.exists(history_path):
        return json.dumps({"message": "No chat history to clear.", "tokens_used": 0})

    if mode == 'summarize':
        history = load_user_history(user_id)
        if not history:
            return json.dumps({"message": "History is empty, nothing to summarize.", "tokens_used": 0})
        
        history_text = "\n".join([f"{item['role']}: {item['content']}" for item in history])
        summary, tokens_used = get_ai_chat_summary(history_text)
        
        new_history = [{"role": "assistant", "content": f"Previous conversation summary:\n{summary}"}]
        save_user_history(user_id, new_history)
        
        message = "Chat history summarized successfully."
        return json.dumps({"message": message, "tokens_used": tokens_used})
    
    else: # Default to 'delete'
        os.remove(history_path)
        message = "Chat history cleared successfully."
        return json.dumps({"message": message, "tokens_used": 0})

def list_chatbot_files(api_key, payload, output_dir):
    user_id = payload.get('uid')
    if not user_id: return json.dumps({"error": "Missing user ID."})
    user_kb_path = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
    os.makedirs(user_kb_path, exist_ok=True)
    try:
        files = [f for f in os.listdir(user_kb_path) if os.path.isfile(os.path.join(user_kb_path, f))]
        return json.dumps({"files": files})
    except Exception as e: return json.dumps({"error": str(e)})

def manage_chatbot_files(api_key, payload, output_dir):
    user_id = payload.get('uid')
    action = payload.get('action')
    files = payload.get('files', [])
    if not user_id or not action: return json.dumps({"error": "Missing user ID or action."})
    user_kb_path = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
    os.makedirs(user_kb_path, exist_ok=True)
    try:
        if action == 'save':
            for file_path in files: shutil.copy(file_path, user_kb_path)
            return json.dumps({"message": f"Saved {len(files)} file(s) to knowledge base."})
        elif action == 'delete_one':
            if not files: return json.dumps({"error": "No file specified."})
            os.remove(os.path.join(user_kb_path, os.path.basename(files[0])))
            return json.dumps({"message": f"Deleted {os.path.basename(files[0])}."})
        elif action == 'delete_all':
            shutil.rmtree(user_kb_path)
            os.makedirs(user_kb_path, exist_ok=True)
            return json.dumps({"message": "Knowledge base cleared."})
        else: return json.dumps({"error": f"Unknown action: {action}"})
    except Exception as e: return json.dumps({"error": str(e)})