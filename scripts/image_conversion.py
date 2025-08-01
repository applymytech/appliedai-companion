# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
from PIL import Image
from logger import setup_logger

logger = setup_logger('image_conversion')

# =============================================================================
# SECTION 2: CORE CONVERSION LOGIC
# =============================================================================
def convert_image(file_path, output_format, output_dir, resize_dims=None, preserve_aspect=True):
    """
    Converts a single image to a specified format, with optional resizing.
    """
    try:
        img = Image.open(file_path)
        original_format = img.format
        
        # Handle resizing if dimensions are provided
        if resize_dims and (resize_dims['width'] or resize_dims['height']):
            new_width = resize_dims['width']
            new_height = resize_dims['height']
            
            if preserve_aspect:
                img.thumbnail((new_width or 9999, new_height or 9999))
            else:
                # Ensure valid dimensions for non-aspect-preserving resize
                final_width = new_width or img.width
                final_height = new_height or img.height
                img = img.resize((final_width, final_height))

        # Construct the output path
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}.{output_format}")

        # Convert and save the image
        # Handle formats that require specific modes (e.g., RGBA for PNG, RGB for JPEG)
        if output_format.lower() in ['jpeg', 'jpg']:
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
        
        img.save(output_path, format=output_format.upper())
        logger.info(f"Successfully converted {file_path} to {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to convert image {file_path}: {e}", exc_info=True)
        return False

# =============================================================================
# SECTION 3: ADAPTER FUNCTION FOR SCRIPT ROUTER
# =============================================================================
def convert_image_adapter(payload, output_dir):
    """
    Adapter function to handle image conversion requests from the frontend.
    """
    files_to_convert = payload.get('files', [])
    output_format = payload.get('format', 'png')
    
    if not files_to_convert:
        return {"error": "No files specified for conversion.", "coins_used": 0}

    resize_dims = {
        'width': int(payload['width']) if payload.get('width') else None,
        'height': int(payload['height']) if payload.get('height') else None,
    }
    preserve_aspect = payload.get('preserve_aspect', True)
    
    success_count = 0
    fail_count = 0
    
    for file_path in files_to_convert:
        if convert_image(file_path, output_format, output_dir, resize_dims, preserve_aspect):
            success_count += 1
        else:
            fail_count += 1
            
    message = f"Successfully converted {success_count} image(s)."
    if fail_count > 0:
        message += f" Failed to convert {fail_count} image(s). See logs for details."
        
    return {"message": message, "coins_used": 0}
