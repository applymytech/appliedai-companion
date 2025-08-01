# /scripts/file_shredder.py (Verified)

# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import os
import sys
import random
import json
from logger import setup_logger

logger = setup_logger('file_shredder')

# =============================================================================
# SECTION 2: SAFETY CONFIGURATION
# =============================================================================
# Define critical system path prefixes to prevent accidental deletion of important files.
critical_paths = [
    os.path.expandvars('%SystemRoot%'),      # C:\Windows
    os.path.expandvars('%ProgramFiles%'),      # C:\Program Files
    os.path.expandvars('%ProgramFiles(x86)%'),  # C:\Program Files (x86)
    os.path.expandvars('%SystemDrive%\\'),      # C:\
    os.path.expandvars('%UserProfile%'),       # C:\Users\username
]

# =============================================================================
# SECTION 3: CORE SHREDDING LOGIC
# =============================================================================

def secure_shred_file(file_path):
    """Securely shred a single file by overwriting 3 times then deleting."""
    try:
        if not os.path.exists(file_path):
            logger.warning(f"File not found for shredding (may have already been deleted): {file_path}")
            return
        
        # Overwrite the file with random data three times
        file_size = os.path.getsize(file_path)
        with open(file_path, 'rb+') as f:
            for _ in range(3):
                f.seek(0)
                f.write(os.urandom(file_size))
                f.flush()
                os.fsync(f.fileno())
        
        # Delete the file
        os.remove(file_path)
        logger.info(f"Shredded file: {file_path}")
    except OSError as e:
        logger.error(f"OS Error shredding file {file_path}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error shredding file {file_path}: {e}")

def shred_path(input_path, output_dir_from_app):
    """Shred a file or a recursive folder, with safety checks."""
    try:
        # --- Safety Check ---
        is_safe = False
        norm_input_path = os.path.normpath(input_path).lower()
        norm_output_dir = os.path.normpath(output_dir_from_app).lower()
        
        # It's considered safe if it's inside the app's designated output directory.
        if norm_input_path.startswith(norm_output_dir):
            is_safe = True
        
        # As an additional check, it's also safe if it's inside the app's own data folder.
        app_data_path = os.path.normpath(os.path.expandvars('%APPDATA%\\appliedai-companion')).lower()
        if norm_input_path.startswith(app_data_path):
            is_safe = True

        if not is_safe:
            is_critical = any(norm_input_path.startswith(os.path.normpath(cp).lower()) for cp in critical_paths)
            if is_critical:
                logger.error(f"Safety override: Cannot shred critical system path: {input_path}")
                print(f"Error: Cannot shred critical system path: {input_path}", file=sys.stderr)
                sys.exit(1)

        logger.info(f"Path deemed safe for shredding: {input_path}")

        if not os.path.exists(input_path):
            logger.warning(f"Path not found for shredding: {input_path}")
            return

        # --- Shredding Logic ---
        if os.path.isfile(input_path):
            secure_shred_file(input_path)
        elif os.path.isdir(input_path):
            logger.info(f"Starting recursive shred of directory: {input_path}")
            # Walk through the directory from the bottom up
            for root, dirs, files in os.walk(input_path, topdown=False):
                for file in files:
                    secure_shred_file(os.path.join(root, file))
                for dir_name in dirs:
                    try:
                        os.rmdir(os.path.join(root, dir_name))
                        logger.info(f"Removed empty directory: {os.path.join(root, dir_name)}")
                    except OSError:
                        logger.warning(f"Directory not empty, skipping rmdir: {os.path.join(root, dir_name)}")
            # Finally, remove the top-level directory if it's empty
            try:
                os.rmdir(input_path)
                logger.info(f"Removed top-level directory: {input_path}")
            except OSError:
                 logger.warning(f"Top-level directory not empty after shredding, not removed: {input_path}")
        else:
            logger.error(f"Invalid path type: {input_path}")

    except Exception as e:
        logger.error(f"An unexpected error occurred while processing path {input_path}: {e}")
        raise

# =============================================================================
# SECTION 4: MAIN EXECUTION (FOR DIRECT CALLS)
# =============================================================================
# This block is executed when the script is called directly by api_handler.py
if __name__ == "__main__":
    # This environment variable is a final safety check set in main.js
    if os.environ.get('SHRED') != 'true':
        logger.error("SHRED environment variable not set to 'true'. Shredding operation cancelled.")
        print("Error: Shredding not authorized by environment variable.", file=sys.stderr)
        sys.exit(1)

    try:
        payload = json.loads(sys.argv[3])
        output_dir = sys.argv[4]
        
        logger.info("SHRED environment variable is 'true'. Proceeding with shredding.")

        if 'files' in payload:
            for file_path in payload['files']:
                shred_path(file_path, output_dir)
        elif 'folder_path' in payload:
            folder_path = payload['folder_path']
            shred_path(folder_path, output_dir)
        else:
            logger.error("Invalid payload: Must include 'files' or 'folder_path'.")
            print("Error: Invalid payload for shredding.", file=sys.stderr)
            sys.exit(1)
        
        # This message is sent back to the UI via api_handler
        print("Shredding completed successfully.")
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing payload JSON: {e}")
        print("Error: Invalid payload JSON.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error in shredder main: {e}", exc_info=True)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)