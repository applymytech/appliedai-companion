# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
import base64
from logger import setup_logger
# Import the new, centralized API call wrapper
from api_clients import call_deepai_model

logger = setup_logger('image_generation')

# =============================================================================
# SECTION 2: CORE LOGIC FUNCTIONS
# =============================================================================
# These functions now only prepare data and call the wrapper from api_clients.py.
# They do not handle API keys or make direct web requests.

def text_to_image(prompt):
    """Generates an image from a text prompt."""
    data = {'text': prompt}
    return call_deepai_model('text2img', data=data)

def toonify_image(image_path):
    """Applies a cartoon effect to an image."""
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        return call_deepai_model('toonify', files=files)

def upscale_image(image_path):
    """Upscales an image using the torch-srgan model."""
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        return call_deepai_model('torch-srgan', files=files)

# Add other DeepAI tool functions here following the same pattern...

# =============================================================================
# SECTION 3: ADAPTER FUNCTION FOR SCRIPT ROUTER
# =============================================================================
def generate_image_adapter(payload, output_dir):
    """
    Adapter function that routes to the correct image generation tool
    based on the payload from the frontend.
    """
    tool_type = payload.get('type')
    params = payload.get('params', {})
    
    if not tool_type:
        return {"error": "No image generation tool type specified.", "coins_used": 0}

    logger.info(f"Routing to image generation tool: {tool_type}")

    try:
        if tool_type == 'text2img':
            prompt = params.get('text')
            if not prompt: return {"error": "Prompt is required for text-to-image.", "coins_used": 0}
            result_data, coins_used = text_to_image(prompt)
        
        elif tool_type == 'toonify':
            image_path = params.get('image')
            if not image_path: return {"error": "Image path is required for toonify.", "coins_used": 0}
            result_data, coins_used = toonify_image(image_path)
            
        elif tool_type == 'torch-srgan':
            image_path = params.get('image')
            if not image_path: return {"error": "Image path is required for upscaling.", "coins_used": 0}
            result_data, coins_used = upscale_image(image_path)
            
        # Add other tool routes here...
        else:
            return {"error": f"Unknown image generation tool: '{tool_type}'", "coins_used": 0}

        # Process the successful response
        if 'output_url' in result_data:
            # For DeepAI, we need to download the generated image
            import requests
            image_response = requests.get(result_data['output_url'])
            image_response.raise_for_status()
            image_base64 = base64.b64encode(image_response.content).decode('utf-8')
            return {"image_base64": image_base64, "coins_used": coins_used}
        else:
            logger.error(f"DeepAI response for '{tool_type}' did not contain 'output_url'. Response: {result_data}")
            return {"error": "Failed to retrieve image from API response.", "coins_used": coins_used}

    except Exception as e:
        logger.error(f"An error occurred in generate_image_adapter for tool '{tool_type}': {e}", exc_info=True)
        return {"error": str(e), "coins_used": 0}
