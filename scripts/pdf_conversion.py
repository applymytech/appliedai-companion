# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
from logger import setup_logger
# Import the AI quality check utility
from ai_utils import get_ai_quality_check

# Third-party libraries for PDF processing
try:
    import fitz  # PyMuPDF
    from docx import Document
    import pandas as pd
    from PIL import Image
except ImportError as e:
    # This helps diagnose missing dependencies on startup
    raise ImportError(f"Missing required PDF processing library: {e}. Please run pip install PyMuPDF python-docx pandas Pillow.")

logger = setup_logger('pdf_conversion')

# =============================================================================
# SECTION 2: CORE CONVERSION LOGIC
# =============================================================================

def pdf_to_text(pdf_path):
    """Extracts all text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)
    doc.close()
    return text

def pdf_to_docx(pdf_path, output_path):
    """Converts a PDF to a DOCX file, preserving text."""
    text = pdf_to_text(pdf_path)
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def pdf_to_images(pdf_path, output_dir):
    """Converts each page of a PDF to a PNG image."""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        output_image_path = os.path.join(output_dir, f"{os.path.basename(pdf_path)}_page_{page_num + 1}.png")
        Image.frombytes("RGB", [pix.width, pix.height], pix.samples).save(output_image_path)
    doc.close()

# =============================================================================
# SECTION 3: ADAPTER FUNCTION FOR SCRIPT ROUTER
# =============================================================================

def convert_pdf_adapter(payload, output_dir):
    """
    Adapter function to handle PDF conversion requests from the frontend.
    It now includes an AI-powered quality check on text-based conversions.
    """
    files_to_convert = payload.get('files', [])
    output_format = payload.get('format', 'txt')
    
    if not files_to_convert:
        return {"error": "No files specified for conversion.", "coins_used": 0}

    total_coins_used = 0
    success_count = 0
    fail_count = 0

    for file_path in files_to_convert:
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}.{output_format}")
        
        try:
            logger.info(f"Converting '{file_path}' to format '{output_format}'...")
            
            extracted_text_for_qc = None

            if output_format == 'txt':
                text = pdf_to_text(file_path)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                extracted_text_for_qc = text
            
            elif output_format == 'docx':
                pdf_to_docx(file_path, output_path)
                extracted_text_for_qc = pdf_to_text(file_path) # Get text for QC
            
            elif output_format == 'png':
                pdf_to_images(file_path, output_dir)
                # Image conversion doesn't produce text for a quality check
            
            else:
                # Placeholder for other formats like csv, xlsx, etc.
                logger.warning(f"Conversion for format '{output_format}' is not yet implemented.")
                fail_count += 1
                continue

            logger.info(f"Successfully converted '{file_path}'.")
            success_count += 1

            # --- AI Quality Check ---
            if extracted_text_for_qc:
                logger.info(f"Performing AI quality check on conversion of '{file_path}'...")
                quality_result, cost = get_ai_quality_check(extracted_text_for_qc)
                total_coins_used += cost
                logger.info(f"AI Quality Check for '{base_name}.{output_format}' result: {quality_result}. Cost: {cost:.4f} AI Coins.")
                # You could add logic here to flag files that "Failed"

        except Exception as e:
            logger.error(f"Failed to convert '{file_path}': {e}", exc_info=True)
            fail_count += 1
            
    message = f"Successfully converted {success_count} PDF(s)."
    if fail_count > 0:
        message += f" Failed to convert {fail_count}. See logs for details."
        
    return {"message": message, "coins_used": total_coins_used}
