# /scripts/ai_utils.py (Corrected)

# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import os
import httpx
from openai import OpenAI
from logger import setup_logger
import json # ADDED THIS IMPORT

logger = setup_logger('ai_utils')

# =============================================================================
# SECTION 2: CORE AI FUNCTIONS
# =============================================================================

def get_ai_client(api_key):
    """Creates a robust OpenAI client for AIMLAPI."""
    base_url = "https://api.aimlapi.com/v1"
    return OpenAI(api_key=api_key, base_url=base_url, http_client=httpx.Client(trust_env=False))

def get_ai_prettyname(filename):
    """Get a pretty name for the file using AI, returning the name and tokens used."""
    try:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: raise ValueError("AIML_API_KEY not found in environment.")
        client = get_ai_client(api_key)
        prompt = f"Generate a short, descriptive title for a file named '{filename}' based on typical content for that name. Keep it under 50 characters."
        response = client.chat.completions.create(
            # Updated model to a supported Gemma version
            model="google/gemma-2-27b-it", 
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
        )
        pretty = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        logger.info(f"Generated pretty name for {filename}: {pretty} (Tokens: {tokens_used})")
        return pretty, tokens_used
    except Exception as e:
        logger.error(f"Error generating pretty name for {filename}: {e}")
        return filename, 0

def get_ai_summary(content):
    """Get a summary for file content using AI, returning the summary and tokens used."""
    try:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: raise ValueError("AIML_API_KEY not found in environment.")
        client = get_ai_client(api_key)
        prompt = f"Generate a short summary (under 100 words) of this file content: {content[:2000]}"
        response = client.chat.completions.create(
            # Updated model to a supported Gemini Flash version
            model="google/gemini-2.5-flash",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
        )
        summary = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        logger.info(f"Generated summary for content. (Tokens: {tokens_used})")
        return summary, tokens_used
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        return "Summary not available.", 0

def get_ai_log_summary(content):
    """Get a summary for a log file using AI, returning the summary and tokens used."""
    try:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: raise ValueError("AIML_API_KEY not found in environment.")
        client = get_ai_client(api_key)
        prompt = f"Summarize the following application log, highlighting any errors or critical warnings:\n\n{content[-4000:]}"
        response = client.chat.completions.create(
            # Updated model to a supported Gemini Pro version
            model="google/gemini-2.5-pro",
            messages=[{"role": "system", "content": "You are an expert at analyzing application logs."}, {"role": "user", "content": prompt}]
        )
        summary = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        logger.info(f"Generated log summary. (Tokens: {tokens_used})")
        return summary, tokens_used
    except Exception as e:
        logger.error(f"Error generating log summary: {e}")
        return "Log summary not available.", 0

def get_ai_chat_summary(chat_content):
    """Get a summary for a chat history, returning the summary and tokens used."""
    try:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: raise ValueError("AIML_API_KEY not found in environment.")
        client = get_ai_client(api_key)
        prompt = f"Condense the following chat history into a single, concise paragraph. Capture the main topics, questions, and conclusions. This summary will be used to provide context for a future conversation.\n\nChat History:\n{chat_content}"
        response = client.chat.completions.create(
            # Updated model to a supported Gemini Flash version
            model="google/gemini-2.5-flash",
            messages=[{"role": "system", "content": "You are an expert at summarizing conversations."}, {"role": "user", "content": prompt}]
        )
        summary = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        logger.info(f"Generated chat summary. (Tokens: {tokens_used})")
        return summary, tokens_used
    except Exception as e:
        logger.error(f"Error generating chat summary: {e}")
        return "Chat summary not available.", 0

def get_ai_quality_check(content):
    """Perform a quality check on converted text, returning the result and tokens used."""
    try:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: raise ValueError("AIML_API_KEY not found in environment.")
        client = get_ai_client(api_key)
        prompt = f"Review the following text extracted from a document. Does it appear to be a high-quality conversion, or is it garbled and nonsensical? Respond with only one of the following words: Passed, Failed, or Needs Review.\n\nText:\n\"{content[:2000]}\""
        response = client.chat.completions.create(
            # Updated model to a supported Gemma version
            model="google/gemma-2-27b-it", 
            messages=[{"role": "system", "content": "You are a document quality control specialist."}, {"role": "user", "content": prompt}]
        )
        quality_result = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        logger.info(f"Performed quality check. Result: {quality_result} (Tokens: {tokens_used})")
        return quality_result, tokens_used
    except Exception as e:
        logger.error(f"Error performing quality check: {e}")
        return "Error", 0

def correct_text_with_ai(text_to_correct):
    """[NEW] Corrects grammar and spelling in a block of text, returning the corrected text and tokens used."""
    try:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: raise ValueError("AIML_API_KEY not found in environment.")
        client = get_ai_client(api_key)
        prompt = f"The following text was extracted via OCR and may contain errors. Please correct any spelling and grammatical mistakes, preserving the original meaning and structure as much as possible:\n\n{text_to_correct}"
        response = client.chat.completions.create(
            # Updated model to a supported Gemini Pro version
            model="google/gemini-2.5-pro",
            messages=[{"role": "system", "content": "You are an expert editor specializing in correcting OCR text."}, {"role": "user", "content": prompt}]
        )
        corrected_text = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        logger.info(f"AI text correction used {tokens_used} tokens.")
        return corrected_text, tokens_used
    except Exception as e:
        logger.error(f"AI text correction failed: {e}")
        return text_to_correct, 0

def summarize_web_search_results(search_results_json: str, query: str, api_key: str):
    """
    Summarizes web search results using an AI model and extracts citations.
    Assumes search_results_json is a JSON string containing a list of dictionaries
    with 'title', 'link', and 'snippet' keys.
    """
    try:
        if not api_key: raise ValueError("AIML_API_KEY not found in environment.")
        client = get_ai_client(api_key)

        search_results = json.loads(search_results_json) # Parse the JSON string
        
        if not search_results:
            return "No relevant information found from web search.", []

        snippets = []
        citations = []
        for result in search_results:
            if result.get("snippet"):
                snippets.append(result["snippet"])
            if result.get("link") and result.get("title"):
                citations.append({"url": result["link"], "title": result["title"]})

        if not snippets:
            return "No readable snippets found from web search for summarization.", []

        combined_snippets = "\n\n".join(snippets[:5]) # Take top 5 snippets for summarization

        prompt = f"Summarize the following search results concisely, focusing on key information relevant to '{query}'. Include direct answers if available. End with a list of provided links as citations.\n\nSearch Results:\n{combined_snippets}\n\n"
        
        response = client.chat.completions.create(
            model="google/gemini-2.5-flash", # Using Gemini-2.5-flash for summarization
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes web search results."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2, # Keep summary concise and factual
            max_tokens=500
        )
        
        summary = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        logger.info(f"Generated web search summary. (Tokens: {tokens_used})")

        return summary, citations, tokens_used # Return summary, citations, and tokens
    except Exception as e:
        logger.error(f"Error summarizing web search results for '{query}': {e}")
        return f"An error occurred during web search summarization: {str(e)}", [], 0