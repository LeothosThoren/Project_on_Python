import scrapy

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['http://www.topito.com/top-meilleures-repliques-cinema-americain']

    def parse(self, response):
        for characters in response.css('div.col-main ::before li'):
            yield {'character': characters.css('li ::text').extract_first()}