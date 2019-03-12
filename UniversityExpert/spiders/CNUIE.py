import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from UniversityExpert.items import UniversityexpertItem


class CNUIESpider(CrawlSpider):
    name = 'CNUIESpider'
    allowed_domains = ['ie.cnu.edu.cn']
    start_urls = [
        'http://www.ie.cnu.edu.cn/szdw/zrjs/index.htm',
    ]
    rules = [
        # http: // math.cnu.edu.cn / szdw / qtjs / 122187.htm
        Rule(LinkExtractor(allow=('/(\d)*\.htm')), callback='parse_detail', follow=True),
    ]

    def parse_detail(self, response):
        item = UniversityexpertItem()
        unit = '首都师范大学'
        name = response.xpath("//div[@class='articleTitle']/h2/text()").extract()
        context = response.xpath("string(//div[@class='pageArticle'])").extract()
        item['unit'] = unit
        item['name'] = name
        item['context'] = context
        yield item
