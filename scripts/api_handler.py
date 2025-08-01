import sys
import json
import os
import base64
import subprocess
from logger import setup_logger

# Ensure the script directory is in the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

logger = setup_logger('api_handler')

# --- Enhanced Logging ---
def log_stderr(message):
    """Prints a message to stderr for Electron to capture as a log."""
    print(f"[Python Log] {message}", file=sys.stderr)

# =========================================================================
# MODULE IMPORTS
# =========================================================================
try:
    log_stderr("Importing modules...")
    import chatbot_request # pyright: ignore[reportMissingImports]
    import file_shredder # pyright: ignore[reportMissingImports]
    import image_conversion # pyright: ignore[reportMissingImports]
    import image_generation # pyright: ignore[reportMissingImports]
    import pdf_conversion # pyright: ignore[reportMissingImports]
    import json_conversion # pyright: ignore[reportMissingImports]
    import markdown_conversion # pyright: ignore[reportMissingImports]
    import merge_files # pyright: ignore[reportMissingImports]
    import ai_utils # pyright: ignore[reportMissingImports]
    import web_search_tool # pyright: ignore[reportMissingImports]
    log_stderr("Modules imported successfully.")
except ImportError as e:
    print(f"FATAL_IMPORT_ERROR: {e}", file=sys.stderr)
    sys.exit(1)


# =========================================================================
# ADAPTER FUNCTIONS
# =========================================================================

# --- [NEW] Direct AI Utility Adapters ---
def ai_get_summary_adapter(api_key, payload, output_dir):
    content = payload.get('content', '')
    summary, tokens_used = ai_utils.get_ai_summary(content)
    return json.dumps({"summary": summary, "tokens_used": tokens_used})

def ai_get_chat_summary_adapter(api_key, payload, output_dir):
    content = payload.get('content', '')
    summary, tokens_used = ai_utils.get_ai_chat_summary(content)
    return json.dumps({"summary": summary, "tokens_used": tokens_used})

def ai_get_quality_check_adapter(api_key, payload, output_dir):
    content = payload.get('content', '')
    result, tokens_used = ai_utils.get_ai_quality_check(content)
    return json.dumps({"result": result, "tokens_used": tokens_used})

def ai_get_log_summary_adapter(api_key, payload, output_dir):
    log_file_path = payload.get('log_file_path')
    if not log_file_path or not os.path.exists(log_file_path):
        return json.dumps({"summary": "Log file not found.", "tokens_used": 0})
    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    summary, tokens_used = ai_utils.get_ai_log_summary(content)
    return json.dumps({"summary": summary, "tokens_used": tokens_used})

# --- [NEW] Web Search Adapter ---
def perform_web_search_adapter(api_key, payload, output_dir):
    query = payload.get('query', '')
    if not query:
        return json.dumps({"results": [], "tokens_used": 0, "message": "No query provided for web search."})
    
    results, tokens_used = web_search_tool.perform_web_search(query, api_key)
    return json.dumps({"results": results, "tokens_used": tokens_used, "message": "Web search completed."})




# --- Existing Application Adapters ---
def chatbot_request_adapter(api_key, payload, output_dir):
    return chatbot_request.get_chatbot_response(api_key, payload, output_dir)

def clear_chat_history_adapter(api_key, payload, output_dir):
    return chatbot_request.clear_chat_history(api_key, payload, output_dir)

def list_chatbot_files_adapter(api_key, payload, output_dir):
    return chatbot_request.list_chatbot_files(api_key, payload, output_dir)

def manage_chatbot_files_adapter(api_key, payload, output_dir):
    return chatbot_request.manage_chatbot_files(api_key, payload, output_dir)

def file_shredder_adapter(api_key, payload, output_dir):
    files_to_shred = payload.get('files', [])
    for f in files_to_shred:
        file_shredder.shred_path(f, output_dir)
    return json.dumps({"message": f"Shredded {len(files_to_shred)} file(s) successfully."})

def folder_shredder_adapter(api_key, payload, output_dir):
    folder_to_shred = payload.get('folder_path')
    file_shredder.shred_path(folder_to_shred, output_dir)
    return json.dumps({"message": f"Shredded folder: {os.path.basename(folder_to_shred)}"})

def image_conversion_adapter(api_key, payload, output_dir):
    preserve_aspect = 'true' if payload.get('preserve_aspect', True) else 'false'
    image_conversion.convert_image(
        input_paths=payload.get('files', []),
        output_format=payload.get('format'),
        output_dir=output_dir,
        preserve_aspect=preserve_aspect,
        width=payload.get('width') if payload.get('width') != "0" else None,
        height=payload.get('height') if payload.get('height') != "0" else None
    )
    return json.dumps({"message": f"Converted {len(payload.get('files', []))} image(s)."})

def image_generation_adapter(api_key, payload, output_dir):
    image_path, tokens_used = image_generation.generate_image(
        payload.get('type'), 
        payload.get('params'), 
        output_dir
    )
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return json.dumps({
        "image_base64": encoded_string,
        "tokens_used": tokens_used
    })

def pdf_conversion_adapter(api_key, payload, output_dir):
    files = payload.get('files', [])
    output_format = payload.get('format')
    total_tokens = 0
    
    for file_path in files:
        output_file_path, conversion_tokens = pdf_conversion.convert_pdf(file_path, output_format, output_dir)
        total_tokens += conversion_tokens
        
        if output_format in ['txt', 'md', 'docx', 'html']:
            try:
                with open(output_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                quality_result, quality_tokens = ai_utils.get_ai_quality_check(content)
                total_tokens += quality_tokens
                logger.info(f"AI Quality Check for {os.path.basename(output_file_path)}: {quality_result}")
            except Exception as e:
                logger.error(f"Could not perform quality check on {output_file_path}: {e}")

    return json.dumps({
        "message": f"Converted {len(files)} PDF(s).",
        "tokens_used": total_tokens
    })

def json_conversion_adapter(api_key, payload, output_dir):
    files = payload.get('files', [])
    output_format = payload.get('format')
    result_message = json_conversion.convert_json(files, output_format, output_dir)
    return json.dumps({"message": f"{result_message} ({len(files)} file(s))", "tokens_used": 0})

def markdown_conversion_adapter(api_key, payload, output_dir):
    files = payload.get('files', [])
    output_format = payload.get('format')
    result_message = markdown_conversion.convert_markdown(files, output_format, output_dir)
    return json.dumps({"message": f"{result_message} ({len(files)} file(s))", "tokens_used": 0})

def merge_files_adapter(api_key, payload, output_dir):
    return merge_files.merge_files(api_key, payload, output_dir)

def scraper_adapter(api_key, payload, output_dir):
    run_scraper_path = os.path.join(os.path.dirname(__file__), 'run_scraper.py')
    env = os.environ.copy()
    env['SCRAPY_OUTPUT_DIR'] = output_dir
    spider_name = payload.get('spider_name')
    spider_args = payload.get('spider_args', {})
    spider_args['output_dir'] = output_dir
    command = [sys.executable, run_scraper_path, spider_name, json.dumps(spider_args)]
    log_stderr(f"Running Scrapy: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        log_stderr(f"Scrapy stderr: {result.stderr}")
        raise RuntimeError(f"Scraper '{spider_name}' failed.")
    log_stderr(f"Scrapy stdout: {result.stdout}")
    return json.dumps({"message": f"Scraper '{spider_name}' completed."})

def handle_error(message):
    """Prints a final error to stderr and exits."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


# =========================================================================
# ROUTER & MAIN EXECUTION
# =========================================================================
functions = {
    # App Health Summary
    'summarize_log': ai_get_log_summary_adapter,

    # Direct AI Utility Routes
    'ai_get_summary': ai_get_summary_adapter,
    'ai_get_chat_summary': ai_get_chat_summary_adapter,
    'ai_get_quality_check': ai_get_quality_check_adapter,
    'ai_get_log_summary': ai_get_log_summary_adapter,
    'perform_web_search': perform_web_search_adapter,
    
    # Chatbot Routes
    'chatbot_request': chatbot_request_adapter,
    'clear_chat_history': clear_chat_history_adapter,
    'list_chatbot_files': list_chatbot_files_adapter,
    'manage_chatbot_files': manage_chatbot_files_adapter,

    # Core Feature Routes
    'generate_image': image_generation_adapter,
    'convert_image': image_conversion_adapter,
    'convert_pdf': pdf_conversion_adapter,
    'convert_json': json_conversion_adapter,
    'convert_markdown': markdown_conversion_adapter,
    'merge_files': merge_files_adapter,
    'shred_files': file_shredder_adapter,
    'shred_folder': folder_shredder_adapter,
    'scrape_single_page': scraper_adapter,
    'scrape_sitemap': scraper_adapter,
    'download_files': scraper_adapter,
    'download_from_sitemap': scraper_adapter,
}

def main():
    if len(sys.argv) != 5:
        handle_error(f"Incorrect number of arguments. Expected 5, got {len(sys.argv)}")

    function_name = sys.argv[1]
    api_key = sys.argv[2]
    payload_str = sys.argv[3]
    output_dir = sys.argv[4]

    log_stderr(f"Executing function: '{function_name}'")

    try:
        payload = json.loads(payload_str)
    except json.JSONDecodeError:
        handle_error("Invalid JSON payload provided.")

    try:
        if function_name in functions:
            result = functions[function_name](api_key, payload, output_dir)
            logger.info(f"Function '{function_name}' executed successfully.")
            print(result) 
            sys.exit(0)
        else:
            handle_error(f"Unknown function name: '{function_name}'")
    except Exception as e:
        logger.error(f"An error occurred in function '{function_name}': {e}", exc_info=True)
        handle_error(f"Exception in '{function_name}': {e}")


if __name__ == "__main__":
    main()