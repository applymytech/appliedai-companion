# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
from logger import setup_logger
# Import the abstraction layer functions, not the clients themselves
from api_clients import call_summarizer_model, call_chatbot_model

logger = setup_logger('ai_utils')

# =============================================================================
# SECTION 2: CORE AI UTILITY FUNCTIONS
# =============================================================================

def get_ai_log_summary(log_content):

    prompt = f"Summarize the following application log, highlighting any errors or critical warnings:\n\n{log_content[-4000:]}"
    try:
        summary, cost = call_summarizer_model(prompt, model_id="google/gemma-3-27b-it")
        return summary, cost
    except Exception as e:
        logger.error(f"Error generating log summary: {e}", exc_info=True)
        return "Log summary could not be generated due to an API error.", 0

def get_ai_quality_check(text_content):

    prompt = f"Review the following text extracted from a document. Does it appear to be a high-quality conversion, or is it garbled and nonsensical? Respond with only one of the following words: Passed, Failed, or Needs Review.\n\nText:\n\"{text_content[:2000]}\""
    try:
        response, cost = call_chatbot_model([{"role": "user", "content": prompt}])
        result = response.choices[0].message.content.strip()
        
        valid_responses = ["Passed", "Failed", "Needs Review"]
        if result not in valid_responses:
            logger.warning(f"AI quality check returned an unexpected value: '{result}'")
            return "Needs Review", cost
            
        return result, cost
    except Exception as e:
        logger.error(f"Error performing quality check: {e}", exc_info=True)
        return "Error", 0

def get_ai_prettyname(filename):

    prompt = f"Generate a short, human-readable name for a file originally named '{filename}'. For example, 'report_q3_final_rev2.pdf' could become 'Q3 Final Report'. Respond with only the name itself."
    try:
        pretty_name, cost = call_summarizer_model(prompt)
        # Clean up the response to remove potential quotes
        return pretty_name.strip().replace('"', ''), cost
    except Exception as e:
        logger.error(f"Error generating pretty name for {filename}: {e}", exc_info=True)
        return filename, 0 # Fallback to original filename

def get_ai_chat_summary(chat_history):

    # Format the chat history for the prompt
    formatted_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])
    prompt = f"Please provide a concise, one-pragraph summary of the following conversation:\n\n{formatted_history}"
    try:
        summary, cost = call_summarizer_model(prompt)
        return summary.strip(), cost
    except Exception as e:
        logger.error(f"Error generating chat summary: {e}", exc_info=True)
        return "Summary unavailable.", 0

# =============================================================================
# SECTION 3: ADAPTER FUNCTIONS FOR SCRIPT ROUTER
# =============================================================================

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

def get_ai_prettyname_adapter(payload, output_dir):
    filename = payload.get('filename', '')
    if not filename:
        return {"error": "No filename provided.", "coins_used": 0}
    
    pretty_name, cost = get_ai_prettyname(filename)
    return {"pretty_name": pretty_name, "coins_used": cost}

def get_ai_chat_summary_adapter(payload, output_dir):
    chat_history = payload.get('history', [])
    if not chat_history:
        return {"error": "No chat history provided.", "coins_used": 0}
        
    summary, cost = get_ai_chat_summary(chat_history)
    return {"summary": summary, "coins_used": cost}
