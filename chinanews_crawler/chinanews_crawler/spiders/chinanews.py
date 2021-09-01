from scrapy.http import Request
from ..items import NewsFeedItem
from bs4 import BeautifulSoup
import scrapy
from scrapy.spiders import XMLFeedSpider


class ChinanewsSpider(scrapy.Spider):
    name = 'chinanews'
    allowed_domains = ['chinanews.com']
    start_urls = ['https://www.chinanews.com/rss/rss_2.html']

    def parse(self, response):
        rss_page = BeautifulSoup(response.body, "html.parser")
        rss_link = set([item['href'] for item in rss_page.find_all('a')])
        for link in rss_link:
            yield Request(url=link, callback=self.parse_feed)

    def parse_feed(self, response):
        rss = BeautifulSoup(response.body, 'lxml')
        for item in rss.find_all('item'):
            feed_item = NewsFeedItem()
            feed_item['title'] = str(item.contents[0])
            feed_item['link'] = item.contents[2]
            feed_item['desc'] = item.description.text
            feed_item['pub_date'] = item.pubdate.text
            yield feed_item
