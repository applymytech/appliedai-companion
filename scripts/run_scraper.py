# /scripts/run_scraper.py (Fully Functional)

# =============================================================================
# SECTION 1: DEPENDENCIES & PATH SETUP
# =============================================================================
import sys
import os
import json
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# This is crucial for Scrapy to find the spiders and their settings.
# We add the new 'spiders' subdirectory to the Python path.
SPIDERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spiders')
sys.path.append(SPIDERS_DIR)

from logger import setup_logger
logger = setup_logger('scraper_runner')

# =============================================================================
# SECTION 2: SPIDER IMPORT & MAPPING
# =============================================================================
# We import the actual Spider classes from their files.
try:
    from spiders.single_page_text import SinglePageTextSpider
    from spiders.sitemap import SitemapTextSpider
    from spiders.file_downloader import FileDownloaderSpider
    from spiders.sitemap_file_downloader import SitemapFileDownloaderSpider
    import spiders.settings as scrapy_settings
except ImportError as e:
    logger.error(f"Failed to import spiders: {e}. Make sure they are in the 'scripts/spiders' directory.")
    print(f"Error: Could not import spider modules. {e}", file=sys.stderr)
    sys.exit(1)

# This map links the 'spider_name' from the frontend to the correct Python class.
SPIDER_MAP = {
    'single_page': SinglePageTextSpider,
    'sitemap': SitemapTextSpider,
    'download_files': FileDownloaderSpider,
    'download_from_sitemap': SitemapFileDownloaderSpider,
}

# =============================================================================
# SECTION 3: MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    if len(sys.argv) < 3:
        logger.error("Usage: python run_scraper.py <spider_name> [spider_args_json]")
        print("Error: Missing spider name or arguments.", file=sys.stderr)
        sys.exit(1)

    spider_name = sys.argv[1]
    kwargs_json = sys.argv[2]
    
    try:
        kwargs = json.loads(kwargs_json)
        logger.info(f"Received request to run spider '{spider_name}' with args: {kwargs}")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON provided for spider arguments: {kwargs_json}")
        print(f"Error: Invalid JSON arguments.", file=sys.stderr)
        sys.exit(1)

    SpiderClass = SPIDER_MAP.get(spider_name)
    if not SpiderClass:
        logger.error(f"Spider '{spider_name}' not found in SPIDER_MAP.")
        print(f"Error: Spider '{spider_name}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        # Configure Scrapy settings dynamically
        settings = Settings()
        settings.setmodule(scrapy_settings)
        # The output directory is now passed via environment variable from api_handler.py
        # and picked up by settings.py, so we don't need to set it here.

        # Run the crawl
        process = CrawlerProcess(settings)
        process.crawl(SpiderClass, **kwargs)
        process.start() # This will block until the crawl is finished
        
        logger.info(f"Spider '{spider_name}' finished successfully.")
        print(f"Scraper '{spider_name}' completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred while running spider '{spider_name}': {e}", exc_info=True)
        print(f"Error running spider {spider_name}: {e}", file=sys.stderr)
        sys.exit(1)