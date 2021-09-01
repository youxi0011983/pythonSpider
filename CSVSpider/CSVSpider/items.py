# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CsvspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 城市名
    norm = scrapy.Field()  # 指标类型
    value = scrapy.Field()  # 值
    date = scrapy.Field()  # 检测日期
