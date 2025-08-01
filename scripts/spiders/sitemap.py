import os
import sys
import scrapy
from urllib.parse import urlparse
from scrapy.spiders import SitemapSpider

# Adjust sys.path to include the Logger directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Logger'))
from logger import setup_logger

class SitemapTextSpider(SitemapSpider):
    name = 'sitemap_text'
    logger = setup_logger('sitemap_text_spider')

    def __init__(self, sitemap_url=None, output_dir=None, *args, **kwargs):
        if not sitemap_url:
            raise ValueError("A sitemap URL must be provided using -a sitemap_url=...")
        if not output_dir:
            raise ValueError("An output directory must be provided using -a output_dir=...")
        
        self.sitemap_urls = [sitemap_url]
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger.info(f"Initialized spider with sitemap URL: {sitemap_url}, Output Dir: {output_dir}")
        super().__init__(*args, **kwargs)

    def start_requests(self):
        """
        This method acts as a router. It checks the sitemap URL and decides
        whether to use the default XML sitemap logic or our custom HTML logic.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
        sitemap_url = self.sitemap_urls[0]

        if sitemap_url.lower().endswith('.xml'):
            self.logger.info("XML sitemap detected, using default SitemapSpider behavior.")
            # Let the parent SitemapSpider handle the XML parsing
            for request in super().start_requests():
                request.headers.update(headers)
                yield request
        else:
            self.logger.info("HTML sitemap detected, using custom HTML link extractor.")
            # For .html or other pages, fetch it and parse links manually
            yield scrapy.Request(sitemap_url, headers=headers, callback=self.parse_html_sitemap)

    def parse_html_sitemap(self, response):
        """
        This method is called only for HTML sitemaps. It finds all links on the
        page and yields a new request for each one, which will be processed by self.parse().
        """
        self.logger.info(f"Extracting links from HTML sitemap: {response.url}")
        links = response.xpath('//a/@href').getall()
        for link in links:
            full_url = response.urljoin(link)
            yield scrapy.Request(full_url, callback=self.parse)

    def parse(self, response):
        """
        This method processes the final content pages from either the XML or HTML sitemap.
        """
        self.logger.debug(f"Parsing content from {response.url} (status: {response.status})")
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
        
        filepath = os.path.join(self.output_dir, filename)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(md_lines))
            self.logger.info(f"Saved content from {response.url} to {filepath}")
        except Exception as e:
            self.logger.error(f"Error writing file {filepath}: {e}")
            raise