import scrapy
from dateutil import parser
import re

pattern = re.compile('background-image:url\((.*)\)')

class NgaSpider(scrapy.Spider):
    name = 'nga'
    start_urls = [
        'http://nga.cn/v/games/'
    ]

    def parse(self, response):
        for article in response.css('ul.topics > li'):
            style = article.css('div.img > a::attr(style)').get()
            match = pattern.match(style)
            image = match.group(1)

            time = article.css('div.oth > span.d::text').get()
            time = parser.parse(time).timestamp()
            time = int(time * 1000)
            yield {
                'title': article.css('div.txt > h2 > a::attr(title)').get().strip(),
                'excerpt': article.css('div.txt > p::text').get(),
                'url': article.css('div.txt > h2 > a::attr(href)').get(),
                'source': 'nga',
                'image': image,
                'time': time
            }
