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
    import image_conversion 
    import ai_utils
    import knowledge_manager
    import file_shredder
    import pdf_conversion
    import json_conversion
    import markdown_conversion
    import merge_files
    import web_scraper
    logger.info("Worker modules imported successfully.")
except ImportError as e:
    logger.error(f"Failed to import a worker module: {e}", exc_info=True)
    sys.exit(1)


FUNCTION_MAP = {
    # Chatbot Functions
    'get_chatbot_response': chatbot_request.get_chatbot_response_adapter,
    'clear_chat_history': chatbot_request.clear_chat_history_adapter,
    
    # Knowledge Base Functions
    'manage_chatbot_files': knowledge_manager.manage_chatbot_files_adapter,
    'list_chatbot_files': knowledge_manager.list_chatbot_files_adapter,

    # Image Generation & Conversion
    'generate_image': image_generation.generate_image_adapter,
    'convert_image': image_conversion.convert_image_adapter, # Assumed function name

    # File Shredder & Management
    'shred_folder_adapter': file_shredder.shred_folder_adapter,
    'shred_files_adapter': file_shredder.shred_files_adapter,
    'merge_files': merge_files.merge_files_adapter,

    # Conversion Functions
    'convert_pdf': pdf_conversion.convert_pdf_adapter,
    'convert_json': json_conversion.convert_json_adapter,
    'convert_markdown': markdown_conversion.convert_markdown_adapter,
    
    # Web Scraper Functions
    'scrape_single_page': web_scraper.scrape_page_to_markdown_adapter, # Corrected name
    'scrape_sitemap': web_scraper.scrape_sitemap_to_markdown_adapter, # Corrected name
    'download_files_from_page': web_scraper.download_files_from_url_adapter, # Corrected name
    'download_website_adapter': web_scraper.download_website_adapter, # Corrected name

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
