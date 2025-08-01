# /scripts/logger.py (Corrected)

# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import logging
import os
import sys

# NOTE: The import from 'ai_utils' has been removed to resolve the circular dependency.

# =============================================================================
# SECTION 2: SETUP FUNCTION
# =============================================================================
def setup_logger(name, log_file='python_main.log'):
    """
    Configures and returns a logger instance that writes to both a file
    and the console (stderr).

    This function is designed to be reusable across all Python scripts.
    Using different names (e.g., 'chatbot', 'file_merger') allows you to
    distinguish which script is logging a message.

    Args:
        name (str): The name for the logger, e.g., 'chatbot'.
        log_file (str): The name of the file to save logs to.

    Returns:
        logging.Logger: A configured logger instance.
    """
    # --- Configuration ---
    # Define a centralized log directory at the project's root.
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Get a logger instance.
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers.
    if not logger.handlers:
        # --- Formatter ---
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # --- File Handler ---
        file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # --- Console Handler ---
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger