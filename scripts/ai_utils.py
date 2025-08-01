# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os # FIXED: Added missing import
import json
from logger import setup_logger
# Import the abstraction layer functions, not the clients themselves
from api_clients import call_summarizer_model, call_chatbot_model

logger = setup_logger('ai_utils')

# =============================================================================
# SECTION 2: CORE AI UTILITY FUNCTIONS
# =============================================================================
# These functions contain the business logic and prompt engineering for
# specialized, non-chatbot AI tasks. They rely on api_clients.py for execution.

def get_ai_log_summary(log_content):
    """
    Creates a prompt and calls the summarizer model to analyze log files.
    """
    prompt = f"Summarize the following application log, highlighting any errors or critical warnings:\n\n{log_content[-4000:]}"
    try:
        # Use a more powerful model for this critical task
        summary, cost = call_summarizer_model(prompt, model_id="google/gemini-2.5-pro")
        return summary, cost
    except Exception as e:
        logger.error(f"Error generating log summary: {e}", exc_info=True)
        return "Log summary could not be generated due to an API error.", 0

def get_ai_quality_check(text_content):
    """
    Creates a prompt and calls an AI model to perform a quality check on text.
    This is the bonus feature for verifying conversions.
    """
    prompt = f"Review the following text extracted from a document. Does it appear to be a high-quality conversion, or is it garbled and nonsensical? Respond with only one of the following words: Passed, Failed, or Needs Review.\n\nText:\n\"{text_content[:2000]}\""
    try:
        # Use the standard chatbot model for this simple classification task
        response, cost = call_chatbot_model([{"role": "user", "content": prompt}])
        result = response.choices[0].message.content.strip()
        
        # Ensure the response is one of the expected values for robustness
        valid_responses = ["Passed", "Failed", "Needs Review"]
        if result not in valid_responses:
            logger.warning(f"AI quality check returned an unexpected value: '{result}'")
            return "Needs Review", cost # Default to caution
            
        return result, cost
    except Exception as e:
        logger.error(f"Error performing quality check: {e}", exc_info=True)
        return "Error", 0

# NOTE: You would continue this pattern for all other utility functions
# that were previously in this file (e.g., get_ai_prettyname, get_ai_chat_summary).

# =============================================================================
# SECTION 3: ADAPTER FUNCTIONS FOR SCRIPT ROUTER
# =============================================================================
# These "adapter" functions are the entry points called by script_router.py.
# They handle parsing the payload and returning a JSON-serializable dictionary.

def get_ai_log_summary_adapter(payload, output_dir):
    log_file_path = payload.get('log_file_path', '')
    if not log_file_path or not os.path.exists(log_file_path):
        return {"error": "Log file not found or path not provided.", "coins_used": 0}
    
    with open(log_file_path, 'r', encoding='utf-8') as f:
        log_content = f.read()

    summary, cost = get_ai_log_summary(log_content)
    return {"summary": summary, "coins_used": cost}

def get_ai_quality_check_adapter(payload, output_dir):
    text_content = payload.get('text_content', '')
    if not text_content:
        return {"error": "No text content provided for quality check.", "coins_used": 0}

    result, cost = get_ai_quality_check(text_content)
    return {"quality_result": result, "coins_used": cost}
