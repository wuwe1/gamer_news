import scrapy
import time


class SfwSpider(scrapy.Spider):
    name = 'sfw'
    start_urls = [
        'http://www.sfw.cn/game'
    ]

    def parse(self, response):
        for article in response.css('table.margin12 > tr'):
            yield {
                'title': article.css('div.title-new > div > a::text').get().strip(),
                'excerpt': article.css('div.intros::text').get(),
                'url': article.css('div.title-new > div > a::attr(href)').get(),
                'source': 'sfw',
                'time': int(time.time())
            }
