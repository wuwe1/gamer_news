import scrapy
import time


class GouhuoSpider(scrapy.Spider):
    name = 'gouhuo'
    start_urls = [
        'https://gouhuo.qq.com/'
    ]

    def parse(self, response):
        for article in response.css('ul.we-list.we-list--square.we-list--1 > li'):
            yield {
                'title': article.css('div.we-figure-info > h3 > a::text').get().strip(),
                'excerpt': article.css('div.we-figure-info > a > p::text').get(),
                'url': article.css('div.we-figure-info > h3 > a::attr(href)').get(),
                'source': 'gouhuo',
                'image': article.css('div.we-imageBox > img::attr(src)').get(),
                'time': int(time.time() * 1000)
            }
