# --*-- coding: utf-8 -*-
import re

import scrapy
from scrapy import Selector

from ..items import CollectipsItem


class XiciSpider(scrapy.Spider):
    name = 'Xici'
    allowed_domains = ['free.kuaidaili.com']

    # start_urls = ['https://free.kuaidaili.com/free/intr']

    def start_requests(self):
        reqs = []
        for i in range(1, 4629):
            req = scrapy.Request("https://free.kuaidaili.com/free/intr/%i/" % i)
            reqs.append(req)
        return reqs

    def parse(self, response, **kwargs):
        # ip_list = response.xpath('//table[@id="ip_list"]')
        # trs = ip_list[0].xpath('tr')
        # items = []
        #
        # for ip in trs[1:]:
        #     pre_item = CollectipsItem()
        #     pre_item['IP'] = ip.xpath('td[3]/text()')[0].extract()
        #     pre_item['PORT'] = ip.xpath('td[4]/text()')[0].extract()
        #     pre_item['POSITION'] = ip.xpath('string(td[5])')[0].extract().strip()
        #     pre_item['TYPE'] = ip.xpath('td[7]/text()')[0].extract()
        #     pre_item['SPEED'] = ip.xpath('td[8]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
        #     pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()
        #     items.append(pre_item)
        #
        # return items
        sel = Selector(response)
        list_items = sel.css('#list > table > tbody > tr')
        items = []
        for i in range(1, 16):
            pre_item = CollectipsItem()
            pre_item['IP'] = list_items.css(":nth-child(%s) > td:nth-child(1)::text" % i).extract()[0]
            pre_item['PORT'] = list_items.css(":nth-child(%s) > td:nth-child(2)::text" % i).extract()[0]
            pre_item['POSITION'] = list_items.css(":nth-child(%s) > td:nth-child(5)::text" % i).extract()[0]
            pre_item['TYPE'] = list_items.css(":nth-child(%s) > td:nth-child(4)::text" % i).extract()[0]
            pre_item['SPEED'] = list_items.css(":nth-child(%s) > td:nth-child(6)::text" % i).re('\d{0,2}\.{0,}\d{0,}')[0]
            pre_item['LAST_CHECK_TIME'] = list_items.css(":nth-child(%s) > td:nth-child(7)::text" % i).extract()[0]
            items.append(pre_item)
        return items
