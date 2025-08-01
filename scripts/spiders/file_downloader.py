import os
import sys
from urllib.parse import urlparse, urljoin
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.httpobj import urlparse_cached
from pathlib import PurePosixPath

# Adjust sys.path to include the Logger directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Logger'))
from logger import setup_logger

class FileDownloaderSpider(scrapy.Spider):
    name = 'file_downloader'
    logger = setup_logger('file_downloader_spider')

    def __init__(self, url=None, allowed_extensions=None, output_dir=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not url:
            raise ValueError("A target URL must be provided using -a url=...")
        if not output_dir:
            raise ValueError("An output directory must be provided using -a output_dir=...")
        self.start_url = url
        self.start_urls = [url]
        self.allowed_extensions = [ext.strip().lstrip('.').lower() for ext in (allowed_extensions or 'pdf,docx').split(',')]
        self.logger.info(f"Initialized spider with URL: {url}, Allowed Extensions: {self.allowed_extensions}, Output Dir: {output_dir}")

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }
        for url in self.start_urls:
            self.logger.debug(f"Sending request to {url}")
            yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        self.logger.debug(f"Received response for {response.url} with status {response.status}")
        if response.status != 200:
            self.logger.error(f"Failed to scrape {response.url}: HTTP status {response.status}")
            # Check for Cloudflare challenge
            if response.status in (403, 429) or 'cf-chl-bypass' in response.text:
                self.logger.warning(f"Possible Cloudflare challenge detected on {response.url}")
            return

        # If input is a sitemap.xml, extract page URLs
        if self.start_url.endswith('.xml'):
            page_urls = response.xpath('//loc/text()').getall()
            if not page_urls:
                self.logger.warning(f"No page URLs found in sitemap: {response.url}")
            for loc in page_urls:
                self.logger.debug(f"Found sitemap loc: {loc}")
                yield scrapy.Request(loc, callback=self.parse_page)
        else:
            # Single page mode
            yield from self.parse_page(response)

    def parse_page(self, response):
        self.logger.debug(f"Parsing page for files/images: {response.url}")
        if response.status != 200:
            self.logger.error(f"Failed to parse page {response.url}: HTTP status {response.status}")
            return

        found_files = False
        # Extract file links from <a href>
        for href in response.xpath('//a/@href').getall():
            full_url = urljoin(response.url, href)
            ext = os.path.splitext(full_url)[1].lstrip('.').lower()
            if ext in self.allowed_extensions:
                self.logger.info(f"Found downloadable file: {full_url}")
                found_files = True
                yield {'file_urls': [full_url]}

        # Extract image sources from <img src>
        for src in response.xpath('//img/@src').getall():
            full_url = urljoin(response.url, src)
            ext = os.path.splitext(full_url)[1].lstrip('.').lower()
            if ext in self.allowed_extensions:
                self.logger.info(f"Found downloadable image: {full_url}")
                found_files = True
                yield {'file_urls': [full_url]}

        if not found_files:
            self.logger.info(f"No files or images found on {response.url} with extensions {self.allowed_extensions}")

class CustomFilesPipeline(FilesPipeline):
    logger = setup_logger('custom_files_pipeline')

    def file_path(self, request, response=None, info=None, *, item=None):
        parsed = urlparse_cached(request)
        filename = os.path.basename(parsed.path) or f'downloaded_file_{hash(request.url)}'
        self.logger.debug(f"Custom file path for {request.url}: {filename}")
        return filename