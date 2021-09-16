#!/usr/bin/python
# -*- coding:utf-8 -*-
import scrapy
from urllib.parse import quote
from ..items import ProductspiderItem
from ..product_data import product_sns

class MyproductspiderSpider(scrapy.Spider):
    name = 'myProductSpider'
    allowed_domains = ['www.taobao.com']
    start_urls = ['https://s.taobao.com/search?q=%s']

    def parse(self, response):
        pass
