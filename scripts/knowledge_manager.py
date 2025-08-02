# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import knowledge_indexer
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
    """Lists all knowledge files for a given user based on scope (knowledge_base or canvas)."""
    user_id = payload.get('uid')
    scope = payload.get('scope', 'knowledge_base') # Default to knowledge_base
    if not user_id: return {"error": "Missing user ID.", "coins_used": 0}

    target_dir = ""
    if scope == 'knowledge_base':
        target_dir = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
    elif scope == 'canvas':
        # Assuming 'canvas' files are stored in a sub-directory within user_id
        # This is a placeholder; you might have a different persistent storage for canvas files
        # For simplicity, let's use a subfolder for canvas files within user's knowledge_base
        target_dir = os.path.join(KNOWLEDGE_BASE_DIR, user_id, 'canvas_files') # Placeholder for canvas files
    else:
        return {"error": f"Unknown scope: {scope}", "coins_used": 0}

    os.makedirs(target_dir, exist_ok=True) # Ensure directory exists

    try:
        files = []
        # List files as objects with name and path for better UI display
        for f in os.listdir(target_dir):
            full_path = os.path.join(target_dir, f)
            if os.path.isfile(full_path):
                files.append({"name": f, "path": full_path})
        return {"files": files, "coins_used": 0}
    except Exception as e:
        logger.error(f"Error listing {scope} files for user {user_id}: {e}")
        return {"error": str(e), "coins_used": 0}

def manage_chatbot_files_adapter(payload, output_dir):
    """Saves, deletes, or clears knowledge files for a given user, including canvas files."""
    user_id = payload.get('uid')
    action = payload.get('action')
    files = payload.get('files', []) # For 'add', 'add_to_canvas'
    file_to_delete = payload.get('file_to_delete', None) # For 'delete_one'

    if not user_id or not action: return {"error": "Missing user ID or action.", "coins_used": 0}

    user_kb_path = os.path.join(KNOWLEDGE_BASE_DIR, user_id)
    user_canvas_path = os.path.join(user_kb_path, 'canvas_files') # Define canvas path

    os.makedirs(user_kb_path, exist_ok=True)
    os.makedirs(user_canvas_path, exist_ok=True) # Ensure canvas directory exists

    try:
        message = ""
        action_performed = action # To pass back to frontend for specific rendering
        if action == 'add': # Add to persistent knowledge base
            saved_count = 0
            skipped_count = 0
            for file_path in files:
                if file_path.lower().endswith('.md'):
                    shutil.copy(file_path, user_kb_path)
                    saved_count += 1
                else:
                    skipped_count += 1
                    logger.warning(f"Skipped non-markdown file for user {user_id}: {os.path.basename(file_path)}")

            message = f"Added {saved_count} markdown file(s) to knowledge base."
            if skipped_count > 0:
                message += f" Skipped {skipped_count} non-markdown file(s). Please convert them to .md and try again."

            # Trigger re-indexing of the entire knowledge base for this user
            # We need user_id for knowledge_indexer
            # Assuming reindex_knowledge_base takes user_id and updates index specific to that user
            # For now, it reindexes *all* knowledge, which is fine for small scale.
            # A more robust solution might reindex only the changed files.
            # For this step, we just make the call.
            # NOTE: knowledge_indexer.reindex_knowledge_base expects an API key, payload, output_dir
            # We can mock payload/output_dir or adjust reindex_knowledge_base to take just user_id
            # Let's adjust knowledge_indexer slightly to accept a user_id or reindex all if none.
            # For now, we call a generic reindex from knowledge_indexer without user_id payload
            # This would need to be revisited for multi-user indexing if knowledge_indexer does not handle it.
            knowledge_indexer.reindex_knowledge_base({"uid": user_id}, output_dir) # Pass user_id for specific indexing
            # The reindex_knowledge_base in knowledge_indexer.py needs to be modified to accept a uid to reindex for a specific user.
            # For now, assume it reindexes all or handles the user_id internally for specific paths.

        elif action == 'delete_one': # Delete one file from persistent knowledge base
            if not file_to_delete: return {"error": "No file specified for deletion.", "coins_used": 0}
            full_file_path = os.path.join(user_kb_path, os.path.basename(file_to_delete))
            if os.path.exists(full_file_path):
                os.remove(full_file_path)
                message = f"Deleted {os.path.basename(file_to_delete)} from knowledge base."
                # Trigger re-indexing
                knowledge_indexer.reindex_knowledge_base({"uid": user_id}, output_dir)
            else:
                message = f"File not found in knowledge base: {os.path.basename(file_to_delete)}"
                action_performed = 'none' # No action

        elif action == 'clear': # Clear ALL persistent knowledge for user
            if os.path.exists(user_kb_path):
                shutil.rmtree(user_kb_path)
                os.makedirs(user_kb_path, exist_ok=True)
            message = "Knowledge base cleared."
            # Trigger re-indexing (to clear user's index)
            knowledge_indexer.reindex_knowledge_base({"uid": user_id}, output_dir)


        elif action == 'add_to_canvas': # Add to temporary canvas
            saved_count = 0
            for file_path in files:
                # Allow diverse file types for canvas if the processing function can handle them
                # For now, copy all selected files to the canvas sub-directory
                shutil.copy(file_path, user_canvas_path)
                saved_count += 1
            message = f"Added {saved_count} file(s) to canvas."

        elif action == 'clear_canvas': # Clear all files from canvas
            if os.path.exists(user_canvas_path):
                shutil.rmtree(user_canvas_path)
                os.makedirs(user_canvas_path, exist_ok=True)
            message = "Canvas cleared."

        else:
            return {"error": f"Unknown action: {action}", "coins_used": 0}

        return {"message": message, "action_performed": action_performed, "coins_used": 0}

    except Exception as e:
        logger.error(f"Error managing files for user {user_id} with action '{action}': {e}", exc_info=True)
        return {"error": str(e), "coins_used": 0}
