import scrapy
import time
import json
from scrapy.http import HtmlResponse


class VgtimeSpider(scrapy.Spider):
    name = 'vgtime'
    start_urls = [
        'https://www.vgtime.com/topic/index/load.jhtml?page=1&pageSize=12'
    ]

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        data = data['data']
        res = HtmlResponse(url='vgtime', body=data, encoding='utf-8')
        for article in res.css('li'):
            url = article.css('div.info_box > a::attr(href)').get()
            url = "www.vgtime.com" + url
            yield {
                'title': article.css('div.info_box > a > h2::text').get().strip(),
                'excerpt': article.css('div.info_box > p::text').get(),
                'url': url,
                'source': 'vgtime',
                'time': int(time.time())
            }
