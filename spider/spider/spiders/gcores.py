import scrapy

class GcoresSpider(scrapy.Spider):
    name = 'gcores'
    start_urls = [
        'https://www.gcores.com/news'
    ]

    def parse(self, response):
        for article in response.css('div.am_card.original'):
            url = article.css('div.am_card_inner > a::attr(href)').get()
            url = response.urljoin(url)
            yield {
                'title': article.css('div.am_card_inner > a > h3::text').get().strip(),
                'excerpt': article.css('a.original_imgArea_cover > p::text').get(),
                'url': url
            }