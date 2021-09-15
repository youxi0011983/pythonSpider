# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class CollectipsPipeline:
    def process_item(self, item, spider):
        DBKWARGS = spider.setting.get('DBKWARGS')
        conn = pymysql.connect(**DBKWARGS)
        cur = conn.cursor()
        sql = "insert into proxy (IP, PORT, TYPE, POSITION, SPEED, LAST_CHECK_TIME) values(%s,%s,%s,%S,%S,%S)"
        lis = (item['IP'], item['PORT'], item['TYPE'], item['POSITION'], item['SPEED'], item['LAST_CHECK_TIME'])
        try:
            cur.execute(sql, lis)
        except Exception as e:
            print("Insert error:", e)
            conn.rollback()
        else:
            conn.commit()
        cur.close()
        conn.close()
        return item
