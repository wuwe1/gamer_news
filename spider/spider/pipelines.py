# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json
import pymongo
import jieba
from zhconv import convert


stopwords = [
    ' ', '～', '！', '（', '）', '【', '】', '「', '」', '，', '。', '：', '《', '》', '？', '、',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_+-', '=', '{', '}', '[', ']', '‘', '’',
     ':', ';', '|', '\\', '<', '>', ',', '.', '/', '?','“','”',
    '的','游戏', '月', '日', '年', '将', '与', '推出', '新', '公开','已于','正为'
    '于', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '是',
    '发售', '释出', '登场', '活动', '版', '公布', '预告', '更新', '正式',
    '合作', '等', '全新', '宣布', '人', '平台', '在', '及', '抢先', '吧',
]


class DropNoneURLandExistURLPipeline:

    collection_name = 'game_news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://localhost:27017/'),
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
        if not url:
            raise DropItem("Missing url in %s" % item)

        result = self.db[self.collection_name].find_one({'url': url})
        if result:
            raise DropItem("Item existing %s" % item)
        return item


class DataCleaningPipeline:
    def process_item(self, item):
        adapter = ItemAdapter(item)

        adapter['title'] = adapter.get('title').replace('\n', '')
        adapter['excerpt'] = adapter.get('excerpt').replace('\n', '')
        image = adapter.get('image')
        adapter['image'] = adapter.get('image') if adapter.get('image') is not None else ''


class SetTagsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        title = adapter.get('title')
        source = adapter.get('source')
        if source == 'baha':
            title = convert(title, 'zh-cn')

        tokens = list(jieba.cut(title))
        tags = []
        for token in tokens:
            if token not in stopwords:
                tags.append(token)
        adapter['tags'] = tags
        return item


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

        
class ExcerptCleaningPipeline:
    def process_item(self, item):
        adapter = ItemAdapter(item)
        excerpt = adapter.get('excerpt')
        excerpt = excerpt.replace('\n','').replace('\t','').replace(' ','')
        adapter['excerpt'] = excerpt
        return item

        
class MongoPipeline:

    collection_name = 'game_news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://localhost:27017/'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'news')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item