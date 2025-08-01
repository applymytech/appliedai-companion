# python_scripts/Scrapers/settings.py

import os

BOT_NAME = 'magicconverter'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1

# Set the output directory for the FilesPipeline
FILES_STORE = os.getenv('SCRAPY_OUTPUT_DIR')
if not FILES_STORE:
    raise ValueError("The 'SCRAPY_OUTPUT_DIR' environment variable is not set. Scrapy cannot proceed without it.")

# Enable the custom pipeline for handling file downloads
ITEM_PIPELINES = {
    'file_downloader.CustomFilesPipeline': 1,
}

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': None,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'