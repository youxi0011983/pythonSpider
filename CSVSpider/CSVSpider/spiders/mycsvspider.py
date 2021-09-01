from scrapy.spiders import CSVFeedSpider
from ..items import CsvspiderItem

names = ['北京', '上海', '广州']


class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['quotsoft.net']
    start_urls = ['https://quotsoft.net/air/data/china_cities_20201231.csv']

    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'

    # Do any adaptations you need here
    # def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        city = CsvspiderItem()
        for name in names:
            if row[name] != None:
                city['name'] = name
                city['norm'] = row['type']
                city['value'] = row[name]
                city['date'] = "%s-%s-%s" % (row['date'][0, 3], row['date'][4, 5], row['date'][6, 7])
                yield city
