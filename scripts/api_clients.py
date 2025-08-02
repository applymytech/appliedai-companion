# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import httpx
import requests
import json
import math # Added for math.ceil
from openai import OpenAI
from logger import setup_logger

logger = setup_logger('api_clients')

# =============================================================================
# SECTION 2: PRICING & MARKUP CONFIGURATION (FROM .ENV)
# =============================================================================

# --- STEP 1: Define the raw cost in USD charged by the API provider.
# Prices are per 1,000,000 tokens for text models, or per unit for image models.
MODEL_PRICING_USD = {
    "google/gemma-3-27b-it": {"input": 0.84, "output": 0.84},
    "google/gemma-3n-e4b-it": {"input": 0.84, "output": 0.84},
    "google/gemini-2.5-flash": {"input": 0.315, "output": 2.625},
    "google/gemini-2.5-pro": {"input": 1.3125, "output": 10.5},
    "google/textembedding-gecko@003": {"input": 0.15},
    "deepai_standard": {"image": 0.01} # This is the cost per "standard image click" from DeepAI
}

# --- STEP 2: Load your business markup rules from environment variables.

try:
    DEFAULT_MARKUP_MULTIPLIER = float(os.environ.get('DEFAULT_MARKUP_MULTIPLIER', 2.0))
    CUSTOM_MODEL_MARKUPS = json.loads(os.environ.get('CUSTOM_MODEL_MARKUPS', '{}'))
except (ValueError, json.JSONDecodeError) as e:
    logger.error(f"Could not parse markup environment variables. Using defaults. Error: {e}")
    DEFAULT_MARKUP_MULTIPLIER = 2.0
    CUSTOM_MODEL_MARKUPS = {}

def calculate_coin_cost(units_used, model_id, is_input=True):

    if model_id == "deepai_standard":
        # For DeepAI, units_used directly represents the number of "image" cost units
        cost_usd_raw = MODEL_PRICING_USD["deepai_standard"]["image"] * units_used
    else:
        model_costs = MODEL_PRICING_USD.get(model_id)
        if not model_costs:
            logger.error(f"Pricing not defined for model: {model_id}. Using default markup on 0 cost.")
            cost_usd_raw = 0.0
        else:
            # Assuming units_used for non-DeepAI models refers to tokens
            price_per_million_tokens = model_costs["input"] if is_input else model_costs["output"]
            cost_usd_raw = (units_used / 1_000_000) * price_per_million_tokens
    
    markup_multiplier = CUSTOM_MODEL_MARKUPS.get(model_id, DEFAULT_MARKUP_MULTIPLIER)
    final_cost_usd = cost_usd_raw * markup_multiplier
    
    # Round up to 5 decimal places for AI Coins
    precision_factor = 100000 
    coins_to_deduct = math.ceil(final_cost_usd * precision_factor) / precision_factor
    
    if model_id and model_id in CUSTOM_MODEL_MARKUPS:
        logger.info(f"Applying custom markup of {markup_multiplier}x for model '{model_id}'. Raw USD: {cost_usd_raw:.8f}, Final Coins: {coins_to_deduct:.5f}.")
    else:
        logger.info(f"Applying default markup of {markup_multiplier}x. Raw USD: {cost_usd_raw:.8f}, Final Coins: {coins_to_deduct:.5f}.")

    return coins_to_deduct

# =============================================================================
# SECTION 3: CLIENT INITIALIZATION (SINGLETON PATTERN)
# =============================================================================
_clients = {}

def get_aimlapi_client():
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
    api_key = os.environ.get('DEEP_AI_KEY')
    if not api_key: raise ValueError("CRITICAL: DEEP_AI_KEY not found.")
    return api_key

# =============================================================================
# SECTION 4: API ABSTRACTION LAYER (WRAPPERS)
# =============================================================================
# These are the standardized functions that other scripts will call.

def call_chatbot_model(messages, model_id="google/gemma-3n-e4b-it"):
    client = get_aimlapi_client()
    response = client.chat.completions.create(model=model_id, messages=messages)
    
    usage = response.usage
    input_coins = calculate_coin_cost(usage.prompt_tokens, model_id, is_input=True)
    output_coins = calculate_coin_cost(usage.completion_tokens, model_id, is_input=False)
    total_coins_to_deduct = input_coins + output_coins
    
    logger.info(f"Chat completion call ({model_id}) input tokens: {usage.prompt_tokens}, output tokens: {usage.completion_tokens}. Deducting {total_coins_to_deduct:.5f} AI Coins.")
    return response, total_coins_to_deduct

def call_embedding_model(text_chunks):
    client = get_aimlapi_client()
    model_id = "google/textembedding-gecko@003"
    response = client.embeddings.create(model=model_id, input=text_chunks)
    
    usage = response.usage
    coins_to_deduct = calculate_coin_cost(usage.total_tokens, model_id, is_input=True)
    
    logger.info(f"Embedding call ({model_id}) total tokens: {usage.total_tokens}. Deducting {coins_to_deduct:.5f} AI Coins.")
    return response, coins_to_deduct

def call_summarizer_model(prompt, model_id="google/gemma-3-27b-it"):
    client = get_aimlapi_client()
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": prompt}]
    )
    
    usage = response.usage
    input_coins = calculate_coin_cost(usage.prompt_tokens, model_id, is_input=True)
    output_coins = calculate_coin_cost(usage.completion_tokens, model_id, is_input=False)
    total_coins_to_deduct = input_coins + output_coins

    logger.info(f"Summarizer call ({model_id}) input tokens: {usage.prompt_tokens}, output tokens: {usage.completion_tokens}. Deducting {total_coins_to_deduct:.5f} AI Coins.")
    summary = response.choices[0].message.content.strip()
    return summary, total_coins_to_deduct

def call_deepai_model(endpoint, files=None, data=None):
    api_key = get_deepai_key()
    response = requests.post(
        f"https://api.deepai.org/api/{endpoint}",
        files=files, data=data, headers={'api-key': api_key}
    )
    response.raise_for_status()
    
    # Default to 1 unit for now, representing a 'standard click'
    # You will need to expand this mapping based on actual DeepAI endpoints
    # and their associated costs from their pricing page (deepai.org/pricing).
    # For example:
    # if endpoint == "text2img": deepai_cost_units = 1
    # elif endpoint == "super-resolution": deepai_cost_units = 5 # Example: if it costs 5x a standard image
    # else: deepai_cost_units = 1 # Fallback for unknown endpoints
    deepai_cost_units = 1 
    coins_to_deduct = calculate_coin_cost(deepai_cost_units, "deepai_standard")

    logger.info(f"DeepAI call ({endpoint}) deducting {coins_to_deduct:.5f} AI Coins. ({deepai_cost_units} cost units)")
    return response.json(), coins_to_deduct