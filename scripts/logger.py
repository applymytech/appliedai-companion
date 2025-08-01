# =============================================================================
# SECTION 1: DEPENDENCIES
# =============================================================================
import logging
import os
import sys

# =============================================================================
# SECTION 2: SETUP FUNCTION
# =============================================================================
def setup_logger(name, log_file='python_main.log'):
    """
    Configures and returns a logger instance that writes to both a file
    and the console (stderr).
    """
    # --- Configuration ---
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers if the logger is called multiple times
    if not logger.handlers:
        # --- Formatter ---
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # --- File Handler ---
        file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # --- Console Handler (for Electron to capture) ---
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
