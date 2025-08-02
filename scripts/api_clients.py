# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import httpx
import requests
import json
from openai import OpenAI
from logger import setup_logger

logger = setup_logger('api_clients')

# =============================================================================
# SECTION 2: PRICING & MARKUP CONFIGURATION (FROM .ENV)
# =============================================================================
# This is the single source of truth for your app's economy.

# --- STEP 1: Define the raw cost in USD charged by the API provider.
MODEL_PRICING_USD = {
    "google/gemma-2-27b-it": {"input": 0.84, "output": 0.84},
    "google/gemini-2.5-flash": {"input": 0.315, "output": 2.625},
    "google/gemini-2.5-pro": {"input": 1.3125, "output": 10.5},
    "google/textembedding-gecko@003": {"input": 0.15},
    "deepai_standard": {"image": 0.01}
}

# --- STEP 2: Load your business markup rules from environment variables.
# This keeps your business logic private and configurable.
try:
    DEFAULT_MARKUP_MULTIPLIER = float(os.environ.get('DEFAULT_MARKUP_MULTIPLIER', 2.0))
    CUSTOM_MODEL_MARKUPS = json.loads(os.environ.get('CUSTOM_MODEL_MARKUPS', '{}'))
except (ValueError, json.JSONDecodeError) as e:
    logger.error(f"Could not parse markup environment variables. Using defaults. Error: {e}")
    DEFAULT_MARKUP_MULTIPLIER = 2.0
    CUSTOM_MODEL_MARKUPS = {}

def calculate_coin_cost(cost_usd, model_id=None):
    """
    Calculates the final cost in "AI Coins" to be charged to the user.
    It checks for a custom markup first, then falls back to the default.
    """
    markup_multiplier = CUSTOM_MODEL_MARKUPS.get(model_id, DEFAULT_MARKUP_MULTIPLIER)
    if model_id and model_id in CUSTOM_MODEL_MARKUPS:
        logger.info(f"Applying custom markup of {markup_multiplier}x for model '{model_id}'.")
    
    return cost_usd * markup_multiplier

# =============================================================================
# SECTION 3: CLIENT INITIALIZATION (SINGLETON PATTERN)
# =============================================================================
_clients = {}

def get_aimlapi_client():
    """Returns a shared instance of the AIMLAPI client."""
    if 'aimlapi' not in _clients:
        api_key = os.environ.get('AIML_API_KEY')
        if not api_key: raise ValueError("CRITICAL: AIML_API_KEY not found.")
        
        base_url = os.environ.get('AIML_API_BASE_URL', "https://api.aimlapi.com/v1")
        
        _clients['aimlapi'] = OpenAI(
            api_key=api_key,
            base_url=base_url,
            http_client=httpx.Client(trust_env=False)
        )
        logger.info(f"AIMLAPI client initialized for base URL: {base_url}")
    return _clients['aimlapi']

def get_deepai_key():
    """Securely retrieves the DeepAI API key."""
    api_key = os.environ.get('DEEP_AI_KEY')
    if not api_key: raise ValueError("CRITICAL: DEEP_AI_KEY not found.")
    return api_key

# =============================================================================
# SECTION 4: API ABSTRACTION LAYER (WRAPPERS)
# =============================================================================
# These are the standardized functions that other scripts will call.

def call_chatbot_model(messages, model_id="google/gemma-3n-e4b-it"):
    """Handles calls for chat-style completions."""
    client = get_aimlapi_client()
    response = client.chat.completions.create(model=model_id, messages=messages)
    
    usage = response.usage
    input_cost_usd = (usage.prompt_tokens / 1_000_000) * MODEL_PRICING_USD[model_id]["input"]
    output_cost_usd = (usage.completion_tokens / 1_000_000) * MODEL_PRICING_USD[model_id]["output"]
    total_cost_usd = input_cost_usd + output_cost_usd
    coins_to_deduct = calculate_coin_cost(total_cost_usd, model_id)
    
    logger.info(f"Chat completion call ({model_id}) cost ${total_cost_usd:.6f}, deducting {coins_to_deduct:.4f} AI Coins.")
    return response, coins_to_deduct

def call_embedding_model(text_chunks):
    """Handles calls to create text embeddings for RAG."""
    client = get_aimlapi_client()
    model_id = "google/textembedding-gecko@003"
    response = client.embeddings.create(model=model_id, input=text_chunks)
    
    usage = response.usage
    total_cost_usd = (usage.total_tokens / 1_000_000) * MODEL_PRICING_USD[model_id]["input"]
    coins_to_deduct = calculate_coin_cost(total_cost_usd, model_id)
    
    logger.info(f"Embedding call ({model_id}) cost ${total_cost_usd:.6f}, deducting {coins_to_deduct:.4f} AI Coins.")
    return response, coins_to_deduct

def call_summarizer_model(prompt, model_id="google/gemini-2.5-flash"):
    """Handles calls for general summarization tasks."""
    client = get_aimlapi_client()
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": prompt}]
    )
    
    usage = response.usage
    input_cost_usd = (usage.prompt_tokens / 1_000_000) * MODEL_PRICING_USD[model_id]["input"]
    output_cost_usd = (usage.completion_tokens / 1_000_000) * MODEL_PRICING_USD[model_id]["output"]
    total_cost_usd = input_cost_usd + output_cost_usd
    coins_to_deduct = calculate_coin_cost(total_cost_usd, model_id)

    logger.info(f"Summarizer call ({model_id}) cost ${total_cost_usd:.6f}, deducting {coins_to_deduct:.4f} AI Coins.")
    summary = response.choices[0].message.content.strip()
    return summary, coins_to_deduct

def call_deepai_model(endpoint, files=None, data=None):
    """Handles all calls to the DeepAI API."""
    api_key = get_deepai_key()
    response = requests.post(
        f"https://api.deepai.org/api/{endpoint}",
        files=files, data=data, headers={'api-key': api_key}
    )
    response.raise_for_status()
    
    cost_usd = MODEL_PRICING_USD["deepai_standard"]["image"]
    coins_to_deduct = calculate_coin_cost(cost_usd)

    logger.info(f"DeepAI call ({endpoint}) cost ${cost_usd:.2f}, deducting {coins_to_deduct:.4f} AI Coins.")
    return response.json(), coins_to_deduct
