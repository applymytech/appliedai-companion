import scrapy

class FileDownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()