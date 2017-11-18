import scrapy

class BlogSpider(scrapy.Spider):
    name = 'quotespider'
    start_urls = ['http://www.topito.com/top-meilleures-repliques-cinema-americain']

    def parse(self, response):
        for citation in response.css('div.col-main li'):
            yield {'quote': citation.css('em ::text').extract_first()}
