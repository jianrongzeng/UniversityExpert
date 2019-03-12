from scrapy import cmdline

# cmdline.execute("scrapy crawl CNUMathSpider -o resource/cnu_math.json".split())
# cmdline.execute("scrapy crawl CNUIESpider -o resource/cnu_ie.json".split())
# cmdline.execute("scrapy crawl CUEBInfoSpider -o resource/cueb_info.json".split())
# cmdline.execute("scrapy crawl BISTUComputer -o resource/bistu_computer.json".split())
cmdline.execute("scrapy crawl CYUCECSpider -o resource/cyu_cec.json".split())
