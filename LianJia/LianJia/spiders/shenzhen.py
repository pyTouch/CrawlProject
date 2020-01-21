# -*- coding: utf-8 -*-
# 	@time: 2020/1/12
# 	@content: 爬取链家网二手房信息
#   感谢链家网（sh.lianjia.com），数据仅用于学习参考，如有其他非法目的，与本代码无关。
#   转载请勿用于非法目的。
#   感谢小幻（https://ip.ihuan.me/）提供优质IP代理

import scrapy, random, time
from LianJia.items import LianjiaItem
from LianJia.settings import ip


class ShanghaiSpider(scrapy.Spider):
    name = 'Shenzhen'
    allowed_domains = ['sz.lianjia.com']
    base_url = 'https://sz.lianjia.com/ershoufang/'
    start_urls = ['https://sz.lianjia.com/ershoufang/pg1/']

    def start_requests(self):
        for i in range(0, 100):  # 一次爬取50页
            if i % 2 == 0:
                time.sleep(10)
            url = self.base_url + '/loupan/pg' + str(i + 1) + '/'
            # print(url)
            yield scrapy.Request(url, callback=self.parse_fangurl, dont_filter=True, meta={'proxy': random.choice(ip)})


    def parse_fangurl(self, response):
        """获取每一页相应楼盘对应的url"""
        fangurl_list = response.xpath('//div[@class="info clear"]/div/a/@href').extract()
        for fangurl in fangurl_list:
            yield scrapy.Request(fangurl, meta={'url': fangurl, 'proxy': random.choice(ip)},
                                 callback=self.parse_detail, dont_filter=True, )


    def parse_detail(self, response):
        """具体处理获取某一个楼盘的信息"""

        url = response.meta['url']
        # print(url)

        item = LianjiaItem()

        # 小区名称
        communityName = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        item["communityName"] = communityName

        # 所在区域和位置
        areaName = response.xpath('//div[@class="areaName"]/span[2]/a/text()').extract()
        if len(areaName) > 0:
            item["areaName"] = areaName[0]
        else:
            item["areaName"] = '暂无数据'
            # 具体位置
        if len(areaName) > 1:
            item["location"] = areaName[1]
        else:
            item["location"] = '暂无数据'

        # 基本信息
        baseContent = response.xpath('//div[@class="base"]/div[2]/ul/li/text()').extract()

        if len(baseContent) > 10:
            item["roomType"] = baseContent[0]
            item["louCeng"] = baseContent[1]
            item["area"] = baseContent[2]
            item["jianZhu"] = baseContent[5]
            item["chaoXiang"] = baseContent[6]
            item["zhuangXiu"] = baseContent[8]
            item["tiHu"] = baseContent[9]
        else:
            print('页面爬取失败' + url)
        # 交易信息
        transactionContent = response.xpath('//div[@class="transaction"]/div[2]/ul/li/span[2]/text()').extract()
        if len(transactionContent) > 5:

            item["guapaitime"] = transactionContent[0]
            item["jiaoyitime"] = transactionContent[2]
            item["nianxian"] = transactionContent[4]
        else:
            print('页面爬取失败' + url)
        # 总价
        totalPrice = response.xpath('//span[@class="total"]/text()').extract_first()
        if totalPrice != None:
            item["totalPrice"] = totalPrice + '万元'
        else:
            item["totalPrice"] = totalPrice
            print('页面爬取失败' + url)
        yield item