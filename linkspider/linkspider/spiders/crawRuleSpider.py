import scrapy
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LinkspiderItem


class CrawrulespiderSpider(CrawlSpider):
    name = 'crawRuleSpider'
    allowed_domains = ['chinanews.com']
    start_urls = ['http://chinanews.com/rss/rss_2.html']

    rules = (
        Rule(LinkExtractor(allow=('\.xml',)), callback='parse_item'),
    )

    def parse_item(self, response):
        selector = Selector(response)
        for node in selector.xpath('//item').extract():
            item = LinkspiderItem()
            item['title'] = response.xpath('title/text()').extract_first()
            item['link'] = response.xpath('link/text()').extract_first()
            item['desc'] = response.xpath('description/text()').extract_first()
            item['pub_date'] = response.xpath('pubDate/text()"]').extract_first()
            yield item
