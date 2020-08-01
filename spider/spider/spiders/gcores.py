import scrapy
import time
import re

pattern = re.compile('background-image:url\((.*)\)')

class GcoresSpider(scrapy.Spider):
    name = 'gcores'
    start_urls = [
        'https://www.gcores.com/news'
    ]

    def parse(self, response):
        for article in response.css('div.am_card.original'):
            url = article.css('div.am_card_inner > a::attr(href)').get()
            url = response.urljoin(url)

            style = article.css('div.original_imgArea::attr(style)').get()
            match = pattern.match(style)
            image = match.group(1)
            yield {
                'title': article.css('div.am_card_inner > a > h3::text').get().strip(),
                'excerpt': article.css('a.original_imgArea_cover > p::text').get(),
                'url': url,
                'image': image,
                'source': 'gcores',
                'time': int(time.time() * 1000)
            }
