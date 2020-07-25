import scrapy
import time


class NgaSpider(scrapy.Spider):
    name = 'nga'
    start_urls = [
        'http://nga.cn/v/games/'
    ]

    def parse(self, response):
        for article in response.css('ul.topics > li'):
            yield {
                'title': article.css('div.txt > h2 > a::attr(title)').get().strip(),
                'excerpt': article.css('div.txt > p::text').get(),
                'url': article.css('div.txt > h2 > a::attr(href)').get(),
                'source': 'nga',
                'time': int(time.time())
            }
