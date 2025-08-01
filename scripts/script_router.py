# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import sys
import json
import os
from logger import setup_logger

script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

logger = setup_logger('script_router')

# =============================================================================
# SECTION 2: MODULE IMPORTS & FUNCTION MAPPING
# =============================================================================
try:
    logger.info("Importing worker modules...")
    import chatbot_request
    import image_generation
    import ai_utils
    import knowledge_manager # <-- ADDED NEW WORKER
    # import pdf_conversion 
    # import merge_files
    logger.info("Worker modules imported successfully.")
except ImportError as e:
    logger.error(f"Failed to import a worker module: {e}", exc_info=True)
    sys.exit(1)

FUNCTION_MAP = {
    # Chatbot Functions
    'get_chatbot_response': chatbot_request.get_chatbot_response_adapter,
    'clear_chat_history': chatbot_request.clear_chat_history_adapter,
    
    # Knowledge Base Functions (now routed to the new manager)
    'manage_chatbot_files': knowledge_manager.manage_chatbot_files_adapter,
    'list_chatbot_files': knowledge_manager.list_chatbot_files_adapter,

    # Image Generation Functions
    'generate_image': image_generation.generate_image_adapter,
    
    # AI Utility Functions
    'get_ai_log_summary': ai_utils.get_ai_log_summary_adapter,
    'get_ai_quality_check': ai_utils.get_ai_quality_check_adapter,
}

# =============================================================================
# SECTION 3: MAIN ROUTER LOGIC
# =============================================================================
def main():
    if len(sys.argv) != 5:
        error_msg = f"Incorrect number of arguments. Expected 5, got {len(sys.argv)}"
        logger.error(error_msg)
        print(json.dumps({"error": error_msg, "coins_used": 0}))
        sys.exit(1)

    function_name, _, payload_str, output_dir = sys.argv[1:5]
    logger.info(f"Received request to execute function: '{function_name}'")

    try:
        payload = json.loads(payload_str)
    except json.JSONDecodeError:
        error_msg = "Invalid JSON payload provided."
        logger.error(error_msg, exc_info=True)
        print(json.dumps({"error": error_msg, "coins_used": 0}))
        sys.exit(1)

    if function_name in FUNCTION_MAP:
        target_function = FUNCTION_MAP[function_name]
        try:
            result = target_function(payload, output_dir)
            logger.info(f"Function '{function_name}' executed successfully.")
            print(json.dumps(result))
        except Exception as e:
            logger.error(f"Function '{function_name}' failed with an unhandled exception: {e}", exc_info=True)
            print(json.dumps({"error": str(e), "coins_used": 0}))
            sys.exit(1)
    else:
        error_msg = f"Unknown function name provided: '{function_name}'"
        logger.error(error_msg)
        print(json.dumps({"error": error_msg, "coins_used": 0}))
        sys.exit(1)

if __name__ == "__main__":
    main()
