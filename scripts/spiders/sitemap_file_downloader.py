import os
import sys
import scrapy
from urllib.parse import urlparse
from scrapy.spiders import SitemapSpider

# Adjust sys.path to include the Logger directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Logger'))
from logger import setup_logger

class SitemapFileDownloaderSpider(SitemapSpider):
    name = 'sitemap_file_downloader'
    logger = setup_logger('sitemap_file_downloader_spider')

    def __init__(self, sitemap_url=None, allowed_extensions=None, output_dir=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not sitemap_url:
            raise ValueError("A sitemap URL must be provided.")
        if not allowed_extensions:
            raise ValueError("Allowed extensions must be provided.")
        if not output_dir:
            raise ValueError("An output directory must be provided.")
            
        self.sitemap_urls = [sitemap_url]
        self.allowed_extensions = [ext.strip().lstrip('.').lower() for ext in allowed_extensions.split(',')]
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger.info(f"Initialized spider with sitemap: {sitemap_url}, extensions: {self.allowed_extensions}")

    def start_requests(self):
        """Router to handle both XML and HTML sitemaps."""
        sitemap_url = self.sitemap_urls[0]
        if sitemap_url.lower().endswith('.xml'):
            self.logger.info("XML sitemap detected.")
            yield from super().start_requests()
        else:
            self.logger.info("HTML sitemap detected.")
            yield scrapy.Request(sitemap_url, callback=self.parse_html_sitemap)

    def parse_html_sitemap(self, response):
        """Extracts all links from an HTML sitemap page."""
        self.logger.info(f"Extracting links from HTML sitemap: {response.url}")
        links = response.xpath('//a/@href').getall()
        for link in links:
            yield scrapy.Request(response.urljoin(link), callback=self.parse_page_for_files)

    def _parse_sitemap(self, response):
        """Override to point XML sitemap links to our file parser instead of the default 'parse'."""
        for req in super()._parse_sitemap(response):
            yield req.replace(callback=self.parse_page_for_files)

    def parse_page_for_files(self, response):
        """
        Parses a content page to find links to files with allowed extensions and yields them for download.
        """
        self.logger.debug(f"Scanning {response.url} for files.")
        file_links = response.xpath('//a/@href').getall()
        found_one = False
        for href in file_links:
            if any(href.lower().endswith(f".{ext}") for ext in self.allowed_extensions):
                full_url = response.urljoin(href)
                self.logger.info(f"Found downloadable file: {full_url}")
                found_one = True
                yield {'file_urls': [full_url]}
        if not found_one:
            self.logger.debug(f"No files with allowed extensions found on {response.url}")