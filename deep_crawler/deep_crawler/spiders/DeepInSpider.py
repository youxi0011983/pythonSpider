import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 不要轻易将示例应用具有反爬机制的网站，否则非常容易被封ip
class DeepinspiderSpider(CrawlSpider):
    name = 'DeepInSpider'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']
    start_urls = ['http://www.example.com/default']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response, **kwargs):
        link_extracotr = LinkExtractor()
        seen = set()  # set是python中的一种不重复的数据集合
        # 此处是为了记录哪些页面已经被爬过了，避免重复爬取相同的页面内容
        links = [l for l in link_extracotr.extract_links(response) if l not in seen]
        for link in links:
            seen.add(link)
            cb = None
            if (link.contains('detail')):
                cb = 'parse_detail'
            yield scrapy.Request(url=link, callback=cb)

    def parse_detail(self, response):
        pass
