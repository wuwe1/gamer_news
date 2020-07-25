# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json
import pymongo

class DropNoneURLPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('url'):
            return item
        else:
            raise DropItem("Missing url in %s" % item)

class JlWithEncodingPipeline:
    def open_spider(self, spider):
        self.file = open('items.jl', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        line = json.dumps(adapter.asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

        
class MongoPipeline:

    collection_name = 'game_news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'news')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        url = adapter.get('url')
        result = self.db[self.collection_name].find_one({'url': url})
        if not result:
            self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
            return item
        else:
            raise DropItem("Item existing %s" % item)