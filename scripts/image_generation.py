# /scripts/image_generation.py (Verified & Refactored)

# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import os
import sys
import json
import requests
import time
from logger import setup_logger

logger = setup_logger('image_generation')

# =============================================================================
# SECTION 2: CONFIGURATION
# =============================================================================
# This dictionary now reflects the curated and renamed list of features.
DEEPAI_ENDPOINTS = {
    'text2img': 'https://api.deepai.org/api/text2image',
    'ghibli-style': 'https://api.deepai.org/api/ghibli-style', # "Animation Style"
    'background-remover': 'https://api.deepai.org/api/background-remover',
    'image-editor': 'https://api.deepai.org/api/image-editor',         # "AI Photo Editor"
    'toonify': 'https://api.deepai.org/api/toonify',
    'torch-srgan': 'https://api.deepai.org/api/torch-srgan',         # "Super Resolution"
    'waifu2x': 'https://api.deepai.org/api/waifu2x',                 # "Premium Upscaler"
}

# =============================================================================
# SECTION 3: CORE GENERATION LOGIC
# =============================================================================
def generate_image(type, params, output_dir):
    """
    Calls the specified DeepAI endpoint to generate or modify an image.
    """
    if type not in DEEPAI_ENDPOINTS:
        raise ValueError(f"Invalid DeepAI type: {type}")
        
    api_key = os.environ.get('DEEP_AI_KEY')
    if not api_key:
        raise ValueError("DEEP_AI_KEY not found. Please set it in the .env file.")

    endpoint = DEEPAI_ENDPOINTS[type]
    try:
        logger.info(f"Calling DeepAI '{type}' with params: {params}")
        
        # Prepare headers and data for the API request
        headers = {'api-key': api_key}
        files = {}
        data = {}

        # Some DeepAI models expect 'image' as a file, others as a URL in 'data'
        if 'image' in params and os.path.exists(params['image']):
            files['image'] = open(params['image'], 'rb')
        else:
            data = params

        response = requests.post(endpoint, data=data, files=files, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        if 'output_url' not in response_data:
            raise ValueError("No 'output_url' in API response.")

        # Download the resulting image
        image_url = response_data['output_url']
        with requests.get(image_url, stream=True) as r:
            r.raise_for_status()
            image_data = r.content

        # Create a safe filename and save the image
        prompt_text = params.get('text', type)[:30]
        safe_name = "".join(c for c in prompt_text if c.isalnum() or c in " ._").rstrip()
        timestamp = int(time.time())
        filename = f"{type}_{safe_name}_{timestamp}.png"
        output_path = os.path.join(output_dir, filename)

        with open(output_path, "wb") as f:
            f.write(image_data)

        logger.info(f"Image saved to {output_path}")
        # Assuming DeepAI token cost is handled externally for now
        return output_path, 0 

    except Exception as e:
        logger.error(f"Error in {type}: {e}", exc_info=True)
        raise
    finally:
        if 'image' in files and files['image']:
            files['image'].close()

# =============================================================================
# SECTION 4: MAIN EXECUTION BLOCK
# =============================================================================
if __name__ == "__main__":
    try:
        output_dir_arg = sys.argv[1]
        type_arg = sys.argv[2]
        params_json = " ".join(sys.argv[3:])
        params_arg = json.loads(params_json)
        
        image_path, tokens_used = generate_image(type_arg, params_arg, output_dir_arg)
        
        print(json.dumps({
            "success": True, 
            "image_path": image_path, 
            "tokens_used": tokens_used
        }))
    except Exception as e:
        print(json.dumps({"error": str(e), "tokens_used": 0}), file=sys.stderr)
        sys.exit(1)