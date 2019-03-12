from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

from UniversityExpert.items import UniversityexpertItem


class BISTUComputer(CrawlSpider):
    name = 'BISTUComputer'
    allowed_domains = ['jsjxy.bistu.edu.cn']
    start_urls = [
        'http://jsjxy.bistu.edu.cn/pubs/jsyl',
    ]
    rules = [
        Rule(LinkExtractor(allow='\?id=(\d)*'),callback='parse_detail',follow=False)
    ]

    def parse_detail(self,response):
        item = UniversityexpertItem()
        unit = "北京信息科技大学"
        name = response.xpath('//text()[preceding-sibling::td[text()="姓名："]]').extract()
        context = response.xpath("/html/body/div/table[1]/tbody/tr[5]/td/table/tbody/tr/td[3]").xpath(
            'string(.)').extract()
        item['unit'] = unit
        item['name'] = name
        item['context'] = context
        yield item
