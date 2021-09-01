# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyspiderItem(scrapy.Item):
    ip = scrapy.Field()  # 地址
    port = scrapy.Field()  # 端口
    speed = scrapy.Field()  # 链接熟读
    connection_time = scrapy.Field()  # 连接时间
    ttl = scrapy.Field()  # 存活时间
    protocol = scrapy.Field()  # 连接协议
    validated = scrapy.Field()  # 是否有效（标致位）


