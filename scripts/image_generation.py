# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
from logger import setup_logger
from api_clients import call_deepai_model 
import requests 

logger = setup_logger('image_generation')

# =============================================================================
# SECTION 2: CORE IMAGE GENERATION LOGIC
# =============================================================================

def _process_image_generation(tool_type, prompt=None, image_path=None, width=None, height=None, img_gen_version=None, genius_pref=None, negative_prompt=None):

    coins_used = 0
    deepai_endpoint = None
    files_param = None
    data_param = {}

    # Map tool_type to DeepAI endpoint and prepare parameters
    if tool_type == 'text2img':
        deepai_endpoint = "text2img" 
        if not prompt:
            return {"error": "Prompt is required for Text to Image.", "coins_used": 0}
        data_param['text'] = prompt 
        if width: data_param['width'] = str(width) 
        if height: data_param['height'] = str(height) 
        if img_gen_version: data_param['image_generator_version'] = img_gen_version 
        if genius_pref: data_param['genius_preference'] = genius_pref 
        if negative_prompt: data_param['negative_prompt'] = negative_prompt 

    elif tool_type == 'ghibli-style':
        deepai_endpoint = "studio-ghibli" 
        if not image_path:
            return {"error": "Input image is required for Ghibli Style.", "coins_used": 0}
        files_param = {'image': open(image_path, 'rb')} 

    elif tool_type == 'toonify':
        deepai_endpoint = "toonify" # Assumed based on common DeepAI tools
        if not image_path:
            return {"error": "Input image is required for Toonify.", "coins_used": 0}
        files_param = {'image': open(image_path, 'rb')}

    elif tool_type == 'image-editor':
        deepai_endpoint = "image-editor" 
        if not image_path:
            return {"error": "Input image is required for AI Photo Editor.", "coins_used": 0}
        if not prompt: # Image editor also takes text prompt 
            return {"error": "Text prompt is required for AI Photo Editor.", "coins_used": 0}
        files_param = {'image': open(image_path, 'rb')} 
        data_param['text'] = prompt # DeepAI uses 'text' for description in image editor 

    elif tool_type == 'torch-srgan': # Super Resolution
        deepai_endpoint = "torch-srgan" 
        if not image_path:
            return {"error": "Input image is required for Super Resolution.", "coins_used": 0}
        files_param = {'image': open(image_path, 'rb')} 

    elif tool_type == 'waifu2x': # Premium Upscaler
        deepai_endpoint = "waifu2x" 
        if not image_path:
            return {"error": "Input image is required for Premium Upscaler.", "coins_used": 0}
        files_param = {'image': open(image_path, 'rb')} 

    elif tool_type == 'background-remover':
        deepai_endpoint = "background-remover" 
        if not image_path:
            return {"error": "Input image is required for Background Remover.", "coins_used": 0}
        files_param = {'image': open(image_path, 'rb')} 
        # Note: The output format forced to PNG will be handled in image_conversion.py or a post-processing step

    # --- Call DeepAI API ---
    if not deepai_endpoint:
        return {"error": f"Unknown or unsupported image generation tool: {tool_type}", "coins_used": 0}

    try:
        response_json, coins = call_deepai_model(deepai_endpoint, files=files_param, data=data_param)
        coins_used += coins
        
        if 'output_url' in response_json:
            result = {"image_url": response_json['output_url'], "message": f"{tool_type.replace('-', ' ').title()} completed successfully."}
        elif 'id' in response_json and 'output_url' not in response_json: # Some DeepAI APIs might return an ID and process asynchronously or have different output keys
            result = {"message": f"{tool_type.replace('-', ' ').title()} job submitted. Check DeepAI for result. (ID: {response_json['id']})", "image_url": None}
        else:
            result = {"error": f"DeepAI API failed for {tool_type}: {response_json.get('err') or response_json}", "coins_used": coins_used}

    except requests.exceptions.RequestException as e:
        logger.error(f"DeepAI API request failed for {tool_type}: {e}", exc_info=True)
        result = {"error": f"DeepAI API request failed: {e}", "coins_used": coins_used}
    except Exception as e:
        logger.error(f"An unexpected error occurred during image generation for {tool_type}: {e}", exc_info=True)
        result = {"error": f"An unexpected error occurred: {e}", "coins_used": coins_used}
    finally:
        # Ensure any opened file handles are closed
        if files_param and 'image' in files_param and hasattr(files_param['image'], 'close'):
            files_param['image'].close()
        
    result["coins_used"] = coins_used # Ensure coins_used is always returned in final result
    return result

# =============================================================================
# SECTION 3: ADAPTER FUNCTIONS FOR SCRIPT ROUTER
# =============================================================================
# This section remains unchanged from previous instructions for generate_image_adapter
def generate_image_adapter(payload, output_dir):
    tool_type = payload.get('tool')
    prompt = payload.get('prompt')
    image_path = payload.get('image_path')
    # Add other parameters from UI if available
    width = payload.get('width')
    height = payload.get('height')
    img_gen_version = payload.get('image_generator_version')
    genius_pref = payload.get('genius_preference')
    negative_prompt = payload.get('negative_prompt')

    if not tool_type:
        logger.error("No image generation tool type specified in payload.")
        return {"error": "No image generation tool type specified.", "coins_used": 0}

    logger.info(f"Generating image with tool: '{tool_type}'")
    
    try:
        # Pass all relevant parameters to the core processing function
        result = _process_image_generation(tool_type, prompt, image_path, width, height, img_gen_version, genius_pref, negative_prompt)
        logger.info(f"Image generation for '{tool_type}' completed. Result: {result.get('message', result.get('error'))}")
        return result
    except Exception as e:
        logger.error(f"Error in generate_image_adapter for tool '{tool_type}': {e}", exc_info=True)
        return {"error": f"Image generation failed: {e}", "coins_used": 0}