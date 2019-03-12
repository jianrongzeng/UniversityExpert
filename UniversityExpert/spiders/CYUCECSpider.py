import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from UniversityExpert.items import UniversityexpertItem


class CYUCECSpider(CrawlSpider):
    name = 'CYUCECSpider'
    allowed_domains = ['cec.cyu.edu.cn']
    start_urls = [
        'http://cec.cyu.edu.cn/szjs/index.html',
        'http://cec.cyu.edu.cn/szjs/index_1.html',
        'http://cec.cyu.edu.cn/szjs/index_2.html'
    ]
    rules = [
        # http://cec.cyu.edu.cn/szjs/201311/t20131121_49710.html
        Rule(LinkExtractor(allow=('/(\d)*t(\d)*_(\d)*\.htm')), callback='parse_detail', follow=False),
    ]

    def parse_detail(self, response):
        item = UniversityexpertItem()
        unit = '中国青年政治学院'
        name = response.xpath("//p[@class='gray_line']/em/text()").extract()
        context = response.xpath("string(//div[@id='contentText'])").extract()
        item['unit'] = unit
        item['name'] = name
        item['context'] = context
        yield item
