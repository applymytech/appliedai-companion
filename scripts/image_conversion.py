# /scripts/image_conversion.py (Verified & Refactored)

# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import os
import sys
from PIL import Image, ImageOps
import img2pdf
from logger import setup_logger

logger = setup_logger('image_conversion')

# =============================================================================
# SECTION 2: CORE CONVERSION LOGIC
# =============================================================================
def convert_image(input_paths, output_format, output_dir, preserve_aspect, width, height):
    """
    Converts and optionally resizes a list of images to a specified format.
    Can also combine multiple images into a single PDF.
    """
    # Determine resizing parameters
    target_width = int(width) if width else None
    target_height = int(height) if height else None
    do_resize = target_width is not None or target_height is not None

    # Handle the special case for PDF conversion first
    if output_format == 'pdf':
        pdf_output_path = os.path.join(output_dir, "combined_images.pdf")
        try:
            with open(pdf_output_path, "wb") as f:
                f.write(img2pdf.convert(input_paths))
            logger.info(f"Successfully combined {len(input_paths)} images into {pdf_output_path}")
        except Exception as e:
            logger.error(f"Error during PDF combination: {str(e)}", exc_info=True)
            raise
        return # End execution after PDF creation

    # Handle all other image-to-image conversions
    for input_path in input_paths:
        base_name = os.path.basename(input_path).rsplit('.', 1)[0]
        output_path = os.path.join(output_dir, f"{base_name}.{output_format}")
        
        try:
            img = Image.open(input_path)
            
            # --- Resizing Logic ---
            if do_resize:
                original_width, original_height = img.size
                
                if preserve_aspect == 'true':
                    if target_width and target_height:
                        img.thumbnail((target_width, target_height), Image.LANCZOS)
                    elif target_width:
                        new_height = int(original_height * (target_width / original_width))
                        img = img.resize((target_width, new_height), Image.LANCZOS)
                    elif target_height:
                        new_width = int(original_width * (target_height / original_height))
                        img = img.resize((new_width, target_height), Image.LANCZOS)
                else: # Do not preserve aspect ratio
                    if target_width and target_height:
                        img = img.resize((target_width, target_height), Image.LANCZOS)
                    elif target_width:
                        img = img.resize((target_width, original_height), Image.LANCZOS)
                    elif target_height:
                        img = img.resize((original_width, target_height), Image.LANCZOS)

            # --- Save Logic ---
            # Convert RGBA to RGB for formats that don't support alpha (like JPEG)
            if output_format.lower() in ['jpeg', 'jpg', 'bmp'] and img.mode == 'RGBA':
                img = img.convert('RGB')
                
            img.save(output_path, format=output_format.upper())
            logger.info(f"Converted {input_path} to {output_path}")

        except Exception as e:
            logger.error(f"Error during image conversion for {input_path}: {str(e)}", exc_info=True)
            raise

# =============================================================================
# SECTION 3: MAIN EXECUTION BLOCK
# =============================================================================
if __name__ == '__main__':
    try:
        output_dir = sys.argv[1]
        output_format = sys.argv[2]
        preserve_aspect = sys.argv[3]
        width = sys.argv[4] if sys.argv[4] != "0" else None
        height = sys.argv[5] if sys.argv[5] != "0" else None
        input_paths = sys.argv[6:]

        if not input_paths:
            raise ValueError("No input files provided for image conversion.")

        convert_image(input_paths, output_format, output_dir, preserve_aspect, width, height)
        print("Image conversion completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred in the main execution block of image_conversion.py: {e}", exc_info=True)
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)