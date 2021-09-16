# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 品名
    link = scrapy.Field()  # 链接地址
    sn = scrapy.Field()  # 货号
    image_url = scrapy.Field()  # 产品图片地址
    image_path = scrapy.Field()  # 图片现在至本地的位置
    price = scrapy.Field()  # 价格
    deal = scrapy.Field()  # 成交人数
    free_shipping = scrapy.Field()  # 是否包邮
    shop = scrapy.Field()  # 淘宝店名
    location = scrapy.Field()  # 地区
