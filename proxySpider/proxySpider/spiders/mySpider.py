import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ProxyspiderItem
from scrapy import Selector


class MyspiderSpider(CrawlSpider):
    name = 'mySpider'
    allowed_domains = ['ip3366.net']
    start_urls = ['http://www.ip3366.net/free/?stype=1&page=1']
    rules = (
        Rule(LinkExtractor(allow=r'/free/*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        selectors = Selector(response)
        row_selectors = selectors.xpath("//tr")
        for row_selector in row_selectors[1:]:
            item = ProxyspiderItem()
            item['ip'] = row_selector.xpath("td[1]/text()").extract_first()
            item['protocol'] = row_selector.xpath("td[4]/text()").extract_first()
            item['port'] = row_selector.xpath("td[2]/text()").extract_first()
            item['connection_time'] = row_selector.xpath("td[6]/text()").extract_first()
            yield item
