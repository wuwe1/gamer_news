import scrapy
import time


class GamelookSpider(scrapy.Spider):
    name = 'gamelook'
    start_urls = [
        'http://www.gamelook.com.cn/page/2'
    ]

    def parse(self, response):
        for article in response.css('ul.article-list > li'):
            yield {
                'title': article.css('div.item-content > h2 > a::attr(title)').get().strip(),
                'excerpt': article.css('div.item-content > div.item-excerpt > p::text').get(),
                'url': article.css('div.item-content > h2 > a::attr(href)').get(),
                'source': 'gamelook',
                'time': int(time.time())
            }
