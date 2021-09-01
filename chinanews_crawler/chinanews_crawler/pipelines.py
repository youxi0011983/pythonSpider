# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from bs4 import BeautifulSoup


class ChinanewsCrawlerPipeline:
    def process_item(self, item, spider):
        return item


# 过滤性管道
class BlockGamePipeline:
    def process_item(self, item, spider):
        filter_key = "游戏"
        if filter_key in (item['title']).encode('utf-8'):
            raise DropItem()
        return item


class DuplicatesPipeline:
    def __init__(self):
        self.fingerprints = set()

    def process_item(self, item, spider):
        if self.fingerprints in item['title']:
            self.fingerprints.add(item["title"])
            raise DropItem()
        return item


# 加工性管道
class ProductPricePipeline:
    def process_item(self, item, spider):
        item['total'] = float(item['price']) * float(item['count'])
        return item


class CleanHTMLPipeline:
    def clear_html(text):
        html = BeautifulSoup(text)
        return html.get_text()

    def process_item(self, item, spider):
        item['title'] = self.clear_html(item['title'])
        item['desc'] = self.clear_html(item['desc'])

        return item


# 存储性管道
class JsonFeedPipeline:
    def __init__(self):
        self.json_file = open('feed.json', 'wt')
        self.json_file.write("[\n")

    def process_item(self, item, spider):
        line = json.dump((dict(item))) + ",\n"
        self.json_file.write(line)
        return item

    def close_spider(self, spider):
        self.json_file.write("\n]")
        self.json_file.close()
