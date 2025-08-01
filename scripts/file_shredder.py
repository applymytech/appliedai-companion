# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import json
from logger import setup_logger

logger = setup_logger('file_shredder')

# =============================================================================
# SECTION 2: CORE SHREDDING LOGIC
# =============================================================================
def shred_file(file_path):
    """Securely overwrites and deletes a single file."""
    try:
        if not os.path.exists(file_path):
            logger.warning(f"File not found for shredding: {file_path}")
            return
        
        with open(file_path, "rb+") as f:
            length = f.seek(0, 2)
            f.seek(0)
            f.write(os.urandom(length))
        os.remove(file_path)
        logger.info(f"Successfully shredded file: {file_path}")
    except Exception as e:
        logger.error(f"Failed to shred file {file_path}: {e}", exc_info=True)
        # We don't re-raise here to allow the script to continue shredding other files

def shred_folder_contents(folder_path):
    """Securely overwrites and deletes all files and subdirectories in a folder."""
    if not os.path.isdir(folder_path):
        logger.error(f"Directory not found for shredding: {folder_path}")
        return
        
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            shred_file(os.path.join(root, name))
        for name in dirs:
            try:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)
                logger.info(f"Removed empty directory: {dir_path}")
            except OSError as e:
                logger.error(f"Could not remove directory {dir_path}: {e}")

# =============================================================================
# SECTION 3: ADAPTER FUNCTIONS FOR SCRIPT ROUTER
# =============================================================================
def shred_files_adapter(payload, output_dir):
    """Adapter to shred a list of specified files."""
    files_to_shred = payload.get('files', [])
    if not files_to_shred:
        return {"error": "No files specified for shredding.", "coins_used": 0}
    
    for file_path in files_to_shred:
        shred_file(file_path)
        
    return {"message": f"Shredding process completed for {len(files_to_shred)} file(s).", "coins_used": 0}

def shred_folder_adapter(payload, output_dir):
    """Adapter to shred the contents of a specified folder."""
    folder_to_shred = payload.get('folder_path')
    if not folder_to_shred:
        return {"error": "No folder path specified for shredding.", "coins_used": 0}
        
    shred_folder_contents(folder_to_shred)
    return {"message": f"Shredding process completed for folder: {folder_to_shred}", "coins_used": 0}
