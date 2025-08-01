# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
from logger import setup_logger
from ai_utils import get_ai_quality_check

# Third-party libraries for conversion
try:
    import markdown
    from docx import Document
except ImportError as e:
    raise ImportError(f"Missing required library: {e}. Please run pip install markdown python-docx.")

logger = setup_logger('markdown_conversion')

# =============================================================================
# SECTION 2: CORE CONVERSION LOGIC
# =============================================================================
def markdown_to_html(md_content):
    """Converts markdown content to an HTML string."""
    return markdown.markdown(md_content)

def markdown_to_docx(md_content, output_path):
    """Converts markdown content to a DOCX file."""
    # A simple conversion; more complex converters could be used for better styling
    html = markdown_to_html(md_content)
    doc = Document()
    doc.add_paragraph(html) # This is a basic implementation
    doc.save(output_path)

# =============================================================================
# SECTION 3: ADAPTER FUNCTION FOR SCRIPT ROUTER
# =============================================================================
def convert_markdown_adapter(payload, output_dir):
    """Adapter to handle markdown conversion requests."""
    files_to_convert = payload.get('files', [])
    output_format = payload.get('format', 'docx')
    
    if not files_to_convert:
        return {"error": "No files specified for conversion.", "coins_used": 0}

    total_coins_used = 0
    success_count = 0
    fail_count = 0

    for file_path in files_to_convert:
        try:
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_path = os.path.join(output_dir, f"{base_name}.{output_format}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if output_format == 'docx':
                markdown_to_docx(content, output_path)
            elif output_format == 'html':
                html_output = markdown_to_html(content)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_output)
            else:
                logger.warning(f"Unsupported markdown output format: {output_format}")
                fail_count += 1
                continue

            logger.info(f"Successfully converted {file_path} to {output_path}")
            success_count += 1
            
            # --- AI Quality Check ---
            # For markdown, the source content is already text, so we check that.
            logger.info(f"Performing AI quality check on content of '{file_path}'...")
            quality_result, cost = get_ai_quality_check(content)
            total_coins_used += cost
            logger.info(f"AI Quality Check for '{base_name}.{output_format}' result: {quality_result}. Cost: {cost:.4f} AI Coins.")

        except Exception as e:
            logger.error(f"Failed to convert markdown file {file_path}: {e}", exc_info=True)
            fail_count += 1

    message = f"Successfully converted {success_count} markdown file(s)."
    if fail_count > 0:
        message += f" Failed to convert {fail_count}. See logs for details."
        
    return {"message": message, "coins_used": total_coins_used}
