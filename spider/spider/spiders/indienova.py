import scrapy
import time
import re

pattern = re.compile('(.*\.jpg)')

class IndienovaSpider(scrapy.Spider):
    name = 'indienova'
    start_urls = [
        'https://indienova.com/channel/news',
    ]

    def parse(self, response):
        for article in response.css('div.article-panel'):
            relative_url = article.css(
                'div.article-image > a::attr(href)').get()
            url = response.urljoin(relative_url)
            image = ''
            match = pattern.match(image)
            image = match.group(1)

            yield {
                'title': article.css('h4 > a::text').get().strip(),
                'excerpt': article.css('p::text').get(),
                'url': url,
                'source': 'indienova',
                'image': image,
                'time': int(time.time() * 1000)
            }
