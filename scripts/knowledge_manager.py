# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import shutil
import json
from logger import setup_logger

logger = setup_logger('knowledge_manager')

# =============================================================================
# SECTION 2: CONFIGURATION & PATHS
# =============================================================================
APP_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
KNOWLEDGE_BASE_DIR = os.path.join(APP_DATA_DIR, 'knowledge_base')

os.makedirs(KNOWLEDGE_BASE_DIR, exist_ok=True)

# =============================================================================
# SECTION 3: ADAPTER FUNCTIONS FOR SCRIPT ROUTER
# =============================================================================
# These are the clean entry points called by script_router.py.

def list_chatbot_files_adapter(payload, output_dir):
    """Lists all knowledge files for a given user."""
    user_id = payload.get('uid')
    if not user_id: return {"error": "Missing user ID.", "coins_used": 0}
    
    user_kb_path = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
    os.makedirs(user_kb_path, exist_ok=True)
    
    try:
        files = [f for f in os.listdir(user_kb_path) if os.path.isfile(os.path.join(user_kb_path, f))]
        return {"files": files, "coins_used": 0}
    except Exception as e:
        logger.error(f"Error listing files for user {user_id}: {e}")
        return {"error": str(e), "coins_used": 0}

def manage_chatbot_files_adapter(payload, output_dir):
    """Saves, deletes, or clears knowledge files for a given user."""
    user_id = payload.get('uid')
    action = payload.get('action')
    files = payload.get('files', [])
    if not user_id or not action: return {"error": "Missing user ID or action.", "coins_used": 0}

    user_kb_path = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
    os.makedirs(user_kb_path, exist_ok=True)
    
    try:
        if action == 'save':
            saved_count = 0
            skipped_count = 0
            for file_path in files:
                # REQUIREMENT: Only allow .md files to be saved to the knowledge base.
                if file_path.lower().endswith('.md'):
                    shutil.copy(file_path, user_kb_path)
                    saved_count += 1
                else:
                    skipped_count += 1
                    logger.warning(f"Skipped non-markdown file for user {user_id}: {os.path.basename(file_path)}")
            
            message = f"Saved {saved_count} markdown file(s)."
            if skipped_count > 0:
                message += f" Skipped {skipped_count} non-markdown file(s). Please convert them to .md and try again."

            # NOTE: Here you would trigger the re-indexing of the vector store
            # This is a placeholder for the call to the re-indexing function.
            # reindex_knowledge_base() 
            return {"message": message, "coins_used": 0}

        elif action == 'delete_one':
            if not files: return {"error": "No file specified for deletion."}
            os.remove(os.path.join(user_kb_path, os.path.basename(files[0])))
            # NOTE: Re-indexing should also be triggered here
            return {"message": f"Deleted {os.path.basename(files[0])}.", "coins_used": 0}

        elif action == 'delete_all':
            shutil.rmtree(user_kb_path)
            os.makedirs(user_kb_path, exist_ok=True)
            # NOTE: Re-indexing should also be triggered here
            return {"message": "Knowledge base cleared.", "coins_used": 0}
            
        else:
            return {"error": f"Unknown action: {action}"}
            
    except Exception as e:
        logger.error(f"Error managing files for user {user_id}: {e}")
        return {"error": str(e), "coins_used": 0}
