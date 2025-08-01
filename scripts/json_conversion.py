# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
import pandas as pd
from logger import setup_logger
from ai_utils import get_ai_quality_check

logger = setup_logger('json_conversion')

# =============================================================================
# SECTION 2: CORE CONVERSION LOGIC
# =============================================================================
def json_to_markdown(data):
    """Converts a JSON object (dict or list of dicts) to a markdown table."""
    if isinstance(data, list):
        df = pd.DataFrame(data)
        return df.to_markdown(index=False)
    elif isinstance(data, dict):
        df = pd.DataFrame([data])
        return df.to_markdown(index=False)
    else:
        raise TypeError("JSON data must be a list of objects or a single object.")

# =============================================================================
# SECTION 3: ADAPTER FUNCTION FOR SCRIPT ROUTER
# =============================================================================
def convert_json_adapter(payload, output_dir):
    """Adapter to handle JSON conversion requests."""
    files_to_convert = payload.get('files', [])
    output_format = payload.get('format', 'md')
    
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
                json_data = json.load(f)

            converted_content = ""
            if output_format == 'md':
                converted_content = json_to_markdown(json_data)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(converted_content)
            else:
                logger.warning(f"Unsupported JSON output format: {output_format}")
                fail_count += 1
                continue

            logger.info(f"Successfully converted {file_path} to {output_path}")
            success_count += 1

            # --- AI Quality Check ---
            logger.info(f"Performing AI quality check on conversion of '{file_path}'...")
            quality_result, cost = get_ai_quality_check(converted_content)
            total_coins_used += cost
            logger.info(f"AI Quality Check for '{base_name}.{output_format}' result: {quality_result}. Cost: {cost:.4f} AI Coins.")

        except Exception as e:
            logger.error(f"Failed to convert JSON file {file_path}: {e}", exc_info=True)
            fail_count += 1

    message = f"Successfully converted {success_count} JSON file(s)."
    if fail_count > 0:
        message += f" Failed to convert {fail_count}. See logs for details."
        
    return {"message": message, "coins_used": total_coins_used}
