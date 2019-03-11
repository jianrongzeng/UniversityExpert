import scrapy

from UniversityExpert.items import UniversityexpertItem


class CNUMathSpider(scrapy.Spider):
    name = 'CNUMathSpider'
    start_urls = [
        'http://math.cnu.edu.cn/szdw/qtjs/index.htm',
    ]
    # rules = [
    #     # http: // math.cnu.edu.cn / szdw / qtjs / 122187.htm
    #     Rule(LinkExtractor(allow=('(\d)*\.htm')), callback='parse_detail', follow=True),
    # ]

    def parse(self, response):
        teachers = response.xpath("//ul[@class='teacher2']/li")
        for teacher in teachers:
            item = UniversityexpertItem()
            unit = '首都师范大学'
            name = teacher.xpath(".//a[@title]/@title").extract()
            context = teacher.xpath(".//text()").extract()
            item['unit'] = unit
            item['name'] = name
            item['context'] = context
            yield item
