# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
import requests
from logger import setup_logger

logger = setup_logger('web_search_tool')

# =============================================================================
# SECTION 2: CORE SEARCH LOGIC
# =============================================================================
def perform_search(query):
    api_key = os.environ.get('TAVILY_API_KEY')
    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables.")

    try:
        response = requests.post("https://api.tavily.com/search", json={
            "api_key": api_key,
            "query": query,
            "search_depth": "basic",
            "include_answer": False,
            "max_results": 5
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Tavily API request failed: {e}", exc_info=True)
        return {"error": f"Web search API request failed: {e}"}

# =============================================================================
# SECTION 3: ADAPTER FUNCTION FOR SCRIPT ROUTER
# =============================================================================
def perform_web_search_adapter(payload, output_dir):

    query = payload.get('query')
    if not query:
        return {"error": "No search query provided.", "coins_used": 0}

    logger.info(f"Performing web search for: '{query}'")
    search_results = perform_search(query)
    
    # The result from Tavily is already a dictionary, so we can return it directly.
    # We just ensure our standard 'coins_used' key is present.
    search_results['coins_used'] = 0
    return search_results
