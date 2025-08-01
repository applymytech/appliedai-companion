# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
from logger import setup_logger
# Import the new, centralized API call wrapper
from api_clients import call_summarizer_model

logger = setup_logger('merge_files')

# =============================================================================
# SECTION 2: CORE MERGING LOGIC
# =============================================================================

def merge_with_ai_summary(file_paths, output_path):
    """
    Merges files with a main cover page and individual cover pages
    containing AI-generated summaries for each file.
    """
    total_coins_used = 0
    main_toc = ["# Table of Contents\n"]
    merged_content = []

    for file_path in file_paths:
        filename = os.path.basename(file_path)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Use the centralized API client to get a summary and cost
            summary, cost = call_summarizer_model(f"Summarize this document content: {content[:2000]}")
            total_coins_used += cost
            
            # Create cover page for the individual file
            file_cover = f"## File: {filename}\n\n**Summary:**\n{summary}\n\n---\n\n"
            merged_content.append(file_cover + content)
            main_toc.append(f"- {filename}")
        except Exception as e:
            logger.error(f"Could not process file {filename} for AI merge: {e}")
            merged_content.append(f"## File: {filename}\n\n---\n\n[Error processing this file.]")

    # Combine everything and write to the output file
    final_content = "\n".join(main_toc) + "\n\n---\n\n" + "\n\n---\n\n".join(merged_content)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    return total_coins_used

def straight_merge(file_paths, output_path):
    """Merges files by simply concatenating their content."""
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n---\n\n') # Separator
            except Exception as e:
                logger.error(f"Could not read file {file_path} for straight merge: {e}")
                outfile.write(f"[Error reading file: {os.path.basename(file_path)}]\n\n---\n\n")

# =============================================================================
# SECTION 3: ADAPTER FUNCTION FOR SCRIPT ROUTER
# =============================================================================
def merge_files_adapter(payload, output_dir):
    """Adapter to handle file merging requests."""
    files_to_merge = payload.get('files', [])
    mode = payload.get('mode', 'straight')
    
    if not files_to_merge:
        return {"error": "No files specified for merging.", "coins_used": 0}

    output_filename = f"merged_output_{len(files_to_merge)}_files.md"
    output_path = os.path.join(output_dir, output_filename)
    total_coins_used = 0

    try:
        if mode == 'with_contents':
            logger.info("Performing AI-powered merge with summaries.")
            total_coins_used = merge_with_ai_summary(files_to_merge, output_path)
        else:
            logger.info("Performing straight merge.")
            straight_merge(files_to_merge, output_path)
        
        message = f"Successfully merged {len(files_to_merge)} files into {output_filename}."
        return {"message": message, "coins_used": total_coins_used}
        
    except Exception as e:
        logger.error(f"An error occurred during file merging: {e}", exc_info=True)
        return {"error": str(e), "coins_used": total_coins_used}
