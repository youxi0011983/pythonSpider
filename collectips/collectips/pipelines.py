# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from scrapy.crawler import Crawler


class CollectipsPipeline:

    # 链接数据库
    @classmethod
    def from_crawler(cls, crawler: Crawler):
        DBKWARGS = crawler.settings['DBKWARGS']
        return cls(DBKWARGS)

    def __init__(self, DBKWARGS):
        self.conn = pymysql.connect(**DBKWARGS)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        sql = "insert into proxy (ip, port, type , position,speed,updatatime) values(%s,%s,%s,%s,%s,%s)"
        lis = (item['IP'], item['PORT'], item['TYPE'], item['POSITION'], item['SPEED'], item['LAST_CHECK_TIME'])
        try:
            self.cur.execute(sql, lis)
        except Exception as e:
            print("Insert error:", e)
            self.conn.rollback()
        else:
            self.conn.commit()
        return item
