# /scripts/markdown_conversion.py (Implemented Markdown Conversion)

# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import sys
import os
from logger import setup_logger
from docx import Document # For DOCX conversion
import markdown # For basic Markdown parsing to HTML

logger = setup_logger('markdown_conversion')

# =============================================================================
# SECTION 2: CORE CONVERSION LOGIC
# =============================================================================
def convert_markdown(input_paths, output_format, output_dir):
    """
    Converts Markdown files to specified formats (DOCX, HTML, PDF - basic).
    """
    if output_format not in ['docx', 'html', 'pdf']:
        logger.error(f"Unsupported output format for Markdown conversion: {output_format}")
        raise ValueError(f"Unsupported output format for Markdown conversion: {output_format}")

    converted_files_count = 0
    for input_path in input_paths:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}.{output_format}")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            if output_format == 'docx':
                doc = Document()
                # Simple conversion: just add the markdown content as a single paragraph.
                # A more advanced conversion would parse markdown elements (headings, lists)
                # and apply Word styles.
                doc.add_paragraph(markdown_content) 
                doc.save(output_path)
            elif output_format == 'html':
                html_content = markdown.markdown(markdown_content) # Convert Markdown to HTML
                full_html = f"<html><head><title>{base_name}</title></head><body>{html_content}</body></html>"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(full_html)
            elif output_format == 'pdf':
                # Basic PDF conversion from Markdown is complex and often requires external tools like pandoc.
                # For a simple placeholder, we can convert to HTML first and then save as a text PDF.
                # A proper implementation would involve a dedicated HTML-to-PDF library (e.g., WeasyPrint, wkhtmltopdf)
                # or calling pandoc via subprocess.
                logger.warning("PDF conversion from Markdown is a basic text dump. For rich PDF, consider external tools.")
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content) # Just write raw text for now
            
            logger.info(f"Converted {input_path} to {output_path}")
            converted_files_count += 1

        except Exception as e:
            logger.error(f"Error during Markdown conversion for {input_path}: {e}")
            raise

    return f"Successfully converted {converted_files_count} file(s)."

# =============================================================================
# SECTION 3: MAIN EXECUTION BLOCK
# =============================================================================
if __name__ == '__main__':
    try:
        output_dir = sys.argv[1]
        output_format = sys.argv[2]
        input_paths = sys.argv[3:]
        convert_markdown(input_paths, output_format, output_dir)
        print("Markdown conversion script ran successfully.")
    except Exception as e:
        logger.error(f"An error occurred in markdown_conversion.py: {e}", exc_info=True)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
