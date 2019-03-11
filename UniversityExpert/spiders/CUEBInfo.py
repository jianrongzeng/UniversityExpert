from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

from UniversityExpert.items import UniversityexpertItem


class CUEBInfoSpider(CrawlSpider):
    name = 'CUEBInfoSpider'
    allowed_domains = ['infoweb2.cueb.edu.cn']
    start_urls = [
        'http://infoweb2.cueb.edu.cn/szdw/xxglyxxxtx/index.htm',
        'http://infoweb2.cueb.edu.cn/szdw/jsjkxyjzx/index.htm',
        'http://infoweb2.cueb.edu.cn/szdw/glkxygcx/index.htm'
    ]
    rules = [
        Rule(LinkExtractor(allow='(\d)*\.htm'),callback='parse_detail',follow=False)
    ]

    def parse_detail(self,response):
        item = UniversityexpertItem()
        unit = "首都经济贸易大学"
        name = response.xpath("//div[@class='articleTitle']/h2/text()").extract()
        context = response.xpath("//div[@class='article']//text()").extract()
        item['unit'] = unit
        item['name'] = name
        item['context'] = context
        yield item