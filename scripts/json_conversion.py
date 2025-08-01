# /scripts/json_conversion.py (Implemented JSON to Markdown)

# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import sys
import os
import json
from logger import setup_logger

logger = setup_logger('json_conversion')

# =============================================================================
# SECTION 2: CORE CONVERSION LOGIC
# =============================================================================

def json_to_markdown(data, indent=0):
    """Recursively converts a JSON object/array to a Markdown string."""
    markdown_str = ""
    indent_str = "  " * indent

    if isinstance(data, dict):
        for key, value in data.items():
            markdown_str += f"{indent_str}- **{key}**:\n"
            if isinstance(value, (dict, list)):
                markdown_str += json_to_markdown(value, indent + 1)
            else:
                markdown_str += f"{indent_str}  {value}\n"
    elif isinstance(data, list):
        for item in data:
            markdown_str += f"{indent_str}- "
            if isinstance(item, (dict, list)):
                markdown_str += "\n" + json_to_markdown(item, indent + 1)
            else:
                markdown_str += f"{item}\n"
    else:
        markdown_str += f"{indent_str}{data}\n"
    
    return markdown_str

def convert_json(input_paths, output_format, output_dir):
    """
    Converts JSON files to specified formats, with a focus on Markdown.
    """
    if output_format not in ['md', 'txt']: # Extend as needed for other formats
        logger.error(f"Unsupported output format for JSON conversion: {output_format}")
        raise ValueError(f"Unsupported output format for JSON conversion: {output_format}")

    converted_files_count = 0
    for input_path in input_paths:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}.{output_format}")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            if output_format == 'md':
                markdown_output = f"# Content from {os.path.basename(input_path)}\n\n"
                markdown_output += json_to_markdown(json_data)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_output)
            elif output_format == 'txt':
                # For plain text, just dump the JSON as a string
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(json_data, indent=2))
            
            logger.info(f"Converted {input_path} to {output_path}")
            converted_files_count += 1

        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from {input_path}: {e}")
            raise ValueError(f"Invalid JSON file: {os.path.basename(input_path)}")
        except Exception as e:
            logger.error(f"Error during JSON conversion for {input_path}: {e}")
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
        convert_json(input_paths, output_format, output_dir)
        print("JSON conversion completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred in json_conversion.py: {e}", exc_info=True)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
