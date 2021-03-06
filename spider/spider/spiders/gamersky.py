import scrapy
from dateutil import parser

class GamerskySpider(scrapy.Spider):
    name = 'gamersky'
    start_urls = [
        'https://www.gamersky.com/news/pc/zx/'
    ]

    def parse(self, response):
        for article in response.css('ul.contentpaging > li'):
            time = article.css('div.time::text').get()
            time = parser.parse(time).timestamp()
            time = int(time * 1000)
            yield {
                'title': article.css('div.img > a::attr(title)').get().strip(),
                'excerpt': article.css('div.con > div.txt::text').get(),
                'url': article.css('div.img > a::attr(href)').get(),
                'image': article.css('div.img > a > img::attr(src)').get(),
                'source': 'gamersky',
                'time': time
            }
