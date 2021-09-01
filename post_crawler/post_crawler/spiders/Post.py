import scrapy
from scrapy import Spider
from random import randint


class PostSpider(scrapy.Spider):
    name = 'Post'
    allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']
    post_rule = "http://example.com/posts/%s"
    user_agents = []

    def gen_post_urls(self, _max=2048):
        for i in range(_max):
            yield self.post_rule % i

    def start_requests(self):
        for url in self.gen_post_urls():
            yield scrapy.Request(url, headers={'User-Agent': self.user_agents[randint(len(self.user_agents))]})

    def parse(self, response):
        scrapy.http.FormRequest
        pass


