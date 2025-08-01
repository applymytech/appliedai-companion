# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import os
import json
import httpx
from openai import OpenAI # AIMLAPI uses OpenAI client
from logger import setup_logger

logger = setup_logger('web_search_tool')

# =============================================================================
# SECTION 2: CORE WEB SEARCH FUNCTION
# =============================================================================

def get_aimlapi_client(api_key):
    # Creates an OpenAI client configured for AIMLAPI.
    base_url = "https://api.aimlapi.com/v1"
    return OpenAI(api_key=api_key, base_url=base_url, http_client=httpx.Client(trust_env=False))

def perform_web_search(query: str, api_key: str):
    # Performs a web search using the Bagoodex / Bagoodex Web Search v1 model via AIMLAPI.
    #
    # Args:
    #     query (str): The search query.
    #     api_key (str): The AIMLAPI key.
    #
    # Returns:
    #     tuple: A tuple containing:
    #         - list: A list of dictionaries, where each dictionary represents a search result
    #                 and contains 'title', 'link', and 'snippet'.
    #         - int: The number of tokens used for the search call (if applicable, or 0).
    try:
        if not api_key:
            raise ValueError("AIML_API_KEY not found in environment.")

        client = get_aimlapi_client(api_key)
        
        logger.info(f"Calling Bagoodex Web Search v1 for query: '{query}'")

        # The Bagoodex API documentation suggests a chat completion-like interface
        # with a specific model name.
        response = client.chat.completions.create(
            model="bagoodex/bagoodex-search-v1", # The specific model for Bagoodex search
            messages=[
                {"role": "user", "content": query}
            ],
            temperature=0.0, # Search should be factual, not creative
            max_tokens=1000 # Limit response size
        )

        # Assuming the response content is a JSON string containing search results
        # The exact structure needs to be confirmed by testing or more detailed docs.
        # For now, we'll parse it and extract relevant fields.
        raw_response_content = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens
        
        logger.info(f"Bagoodex raw response: {raw_response_content[:200]}...")

        # Attempt to parse the content. Bagoodex might return structured JSON directly.
        # If it returns a text summary, we'll need to adapt.
        try:
            search_data = json.loads(raw_response_content)
            results = []
            # Assuming search_data is a list of results or has a 'results' key
            if isinstance(search_data, list):
                for item in search_data:
                    results.append({
                        "title": item.get("title", "No Title"),
                        "link": item.get("link", "#"),
                        "snippet": item.get("snippet", "No snippet available.")
                    })
            elif isinstance(search_data, dict) and 'results' in search_data:
                 for item in search_data['results']:
                    results.append({
                        "title": item.get("title", "No Title"),
                        "link": item.get("link", "#"),
                        "snippet": item.get("snippet", "No snippet available.")
                    })
            else:
                logger.warning("Bagoodex response not in expected list/dict format. Treating as plain text.")
                # If it's not structured, treat the whole thing as a single snippet
                results.append({
                    "title": "Search Result",
                    "link": "#",
                    "snippet": raw_response_content
                })

        except json.JSONDecodeError:
            logger.warning("Bagoodex response is not JSON. Treating as plain text summary.")
            results = [{
                "title": "Web Search Result",
                "link": "#", # No specific link if it's just a summary
                "snippet": raw_response_content
            }]
        
        logger.info(f"Performed web search for '{query}'. Found {len(results)} results. (Tokens: {tokens_used})")
        return results, tokens_used

    except Exception as e:
        logger.error(f"Error performing web search with Bagoodex for '{query}': {e}")
        return [], 0 # Return empty list and 0 tokens on error