import sys
import json
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import settings as scrapy_settings

# Import all spider classes
from single_page_text import SinglePageTextSpider
from sitemap import SitemapTextSpider
from file_downloader import FileDownloaderSpider
from sitemap_file_downloader import SitemapFileDownloaderSpider # Add this new import

# Add the new spider to the map
SPIDER_MAP = {
    'single_page_text': SinglePageTextSpider,
    'sitemap_text': SitemapTextSpider,
    'file_downloader': FileDownloaderSpider,
    'sitemap_file_downloader': SitemapFileDownloaderSpider, # Add this new entry
}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Missing spider name or arguments.", file=sys.stderr)
        sys.exit(1)

    spider_name = sys.argv[1]
    kwargs_json = sys.argv[2]
    kwargs = json.loads(kwargs_json)

    SpiderClass = SPIDER_MAP.get(spider_name)
    if not SpiderClass:
        print(f"Error: Spider '{spider_name}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        settings = Settings()
        settings.setmodule(scrapy_settings)
        process = CrawlerProcess(settings)
        process.crawl(SpiderClass, **kwargs)
        process.start()
    except Exception as e:
        print(f"Error running spider {spider_name}: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        sys.exit(0)