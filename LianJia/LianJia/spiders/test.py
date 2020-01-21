# -*- coding: utf-8 -*-

import scrapy, random
from LianJia.settings import ip


class ShanghaiSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['sh.lianjia.com']

    def start_requests(self):
        # 测试随机IP代理和user_agent
        for i in range(0, 4):
            yield scrapy.Request('https://httpbin.org/get',
                             callback=self.parse_fangurl,
                             dont_filter=True,
                             meta={'proxy': random.choice(ip)})

    def parse_fangurl(self, response):
        # 测试https://httpbin.org/get
        print(response.text)
