import os
import sys
import scrapy
from urllib.parse import urlparse

# Adjust sys.path to include the Logger directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Logger'))
from logger import setup_logger

class SinglePageTextSpider(scrapy.Spider):
    name = 'single_page_text'
    logger = setup_logger('single_page_text_spider')

    def __init__(self, url=None, output_dir=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not url:
            raise ValueError("A target URL must be provided using -a url=...")
        if not output_dir:
            raise ValueError("An output directory must be provided using -a output_dir=...")
        self.start_urls = [url]
        self.output_dir = output_dir
        self.logger.info(f"Initialized spider with URL: {url}, Output Dir: {output_dir}")

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }
        for url in self.start_urls:
            self.logger.debug(f"Sending request to {url}")
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        self.logger.debug(f"Received response for {response.url} with status {response.status}")
        if response.status != 200:
            self.logger.error(f"Failed to scrape {response.url}: HTTP status {response.status}")
            return

        title = response.xpath('//title/text()').get(default='No Title').strip()
        content_blocks = response.xpath('//h1 | //h2 | //h3 | //h4 | //h5 | //h6 | //p')
        md_lines = [f"# {title}\n"]

        for block in content_blocks:
            tag = block.root.tag
            text = ' '.join(block.xpath('.//text()').getall()).strip()
            if not text:
                continue

            if tag.startswith('h'):
                level = int(tag[1])
                md_lines.append(f"\n{'#' * level} {text}\n")
            elif tag == 'p':
                md_lines.append(f"{text}\n")
        
        parsed_url = urlparse(response.url)
        safe_path = parsed_url.path.strip('/').replace('/', '_').replace('?', '_').replace('&', '_')
        filename = f"{parsed_url.netloc}_{safe_path or 'index'}.md"

        os.makedirs(self.output_dir, exist_ok=True)
        filepath = os.path.join(self.output_dir, filename)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(md_lines))
            self.logger.info(f"Saved content to {filepath}")
        except Exception as e:
            self.logger.error(f"Error writing file {filepath}: {e}")
            raise