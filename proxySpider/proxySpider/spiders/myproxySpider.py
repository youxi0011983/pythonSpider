import scrapy
from scrapy import Selector
from ..items import ProxyspiderItem


def _duration_to_millisecond(val):
    if val:
        if u'秒' in val:
            return int(float(val.replace(u'秒', '')) * 1000)
        if u'分钟' in val:
            return int(float(val.replace(u'分钟', '')) * 1000 * 60)
        if u'小时' in val:
            return int(float(val.replace(u'小时', '')) * 1000 * 60 * 60)
        if u'天' in val:
            return int(float(val.replace(u'天', '')) * 1000 * 60 * 60 * 24)
    return 0


class MyproxyspiderSpider(scrapy.Spider):
    name = 'myproxySpider'
    allowed_domains = ['ip3366.net']
    start_urls = ['http://ip3366.net/']

    def parse(self, response):
        selectors = Selector.xpath(response)

        # item['speed'] = row_selectors.xpath("td[3]/text()").extract_first()
        # item['ttl'] = row_selectors.xpath("td[2]/text()").extract_first()
        # item['validated'] = row_selectors.xpath("td[6]/text()").extract_first()
