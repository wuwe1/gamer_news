import scrapy

class GamerskySpider(scrapy.Spider):
    name = 'gamersky'
    start_urls = [
        'https://www.gamersky.com/news/pc/zx/'
    ]

    def parse(self, response):
        for article in response.css('ul.contentpaging > li'):
            yield {
                'title': article.css('div.img > a::attr(title)').get().strip(),
                'excerpt': article.css('div.con > div.txt::text').get(),
                'url': article.css('div.img > a::attr(href)').get()
            }