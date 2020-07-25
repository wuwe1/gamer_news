# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json

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

        
