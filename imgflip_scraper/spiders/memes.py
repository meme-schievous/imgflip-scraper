import scrapy


class MemesSpider(scrapy.Spider):
    name = "memes"
    allowed_domains = ["imgflip.com"]
    start_urls = ["https://imgflip.com"]

    def parse(self, response):
        pass
