import scrapy

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['http://www.topito.com/top-meilleurs-personnages-film']

    def parse(self, response):
        for characters in response.css('div.col-main li'):
            yield {'character': characters.css('strong ::text').extract_first()}