import scrapy
import time


class BahaSpider(scrapy.Spider):
    name = 'baha'
    start_urls = [
        'https://gnn.gamer.com.tw/'
    ]

    def parse(self, response):
        for article in response.css('div.BH-lbox > div'):
            url = article.css('h1 > a::attr(href)').get()
            url = response.urljoin(url)
            yield {
                'title': article.css('h1 > a::text').get().strip(),
                'excerpt': article.css('p::text').get().strip(),
                'url': url,
                'image': article.css('div.GN-lbox2E > a > img::attr(src)').get(),
                'source': 'baha',
                'time': int(time.time() * 1000)
            }
