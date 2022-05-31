# -*- coding: utf8 -*-
import scrapy
from ..items import TopgoodsItem


class TmGoodsSpider(scrapy.Spider):
    name = 'TmGoods'
    allowed_domains = ['www.tmall.com']
    start_urls = ['http://www.tmall.com/']
    start_urls = (
        'https://list.tmall.com/search_product.htm?q=%C5%AE%D7%B0&type=p&spm=a220m.1000858.a2227oh.d100&xl=nvzh_1&from=.list.pc_1_suggest')
    # 记录处理的层数
    count = 0

    def parse(self, response):
        TmGoodsSpider.count += 1
        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")
        if not divs:
            self.log("List page error --%s" % response.url)

        for div in divs:
            item = TopgoodsItem()
            item["GOODS_PRICE"] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            item["GOODS_NAME"] = div.xpath("p[@class='productTitle']/a/@title")[0].extract()
            pre_goods_url = div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item["GOODS_URL"] = pre_goods_url if "http:" in pre_goods_url else ("http:" + pre_goods_url)

            yield scrapy.Request(url=item["GOODS_URL"], meta={'item': item}, callback=self.parse_def, dont_filter=True)

    def parse_detail(self, response):
        pass
