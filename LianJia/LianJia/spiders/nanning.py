#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created author: pyTouch
# created date: 2020-1-12
# content: 爬取链家网二手房信息
# 感谢链家网（sh.lianjia.com），数据仅用于学习参考，如有其他非法目的，与本代码无关。
# 感谢小幻（https://ip.ihuan.me/）提供优质IP代理

import scrapy, random, datetime, time
from LianJia.items import LianjiaItem
from LianJia.settings import ip
import re


class ShanghaiSpider(scrapy.Spider):
    name = 'nanning'
    allowed_domains = ['nn.lianjia.com']
    base_url = 'https://nn.lianjia.com/ershoufang/'
    start_urls = ['https://nn.lianjia.com/ershoufang/pg1/']

    def start_requests(self):
        for i in range(50, 100):  # 一次爬取50页
            url = self.base_url + '/loupan/pg' + str(i + 1) + '/'
            print(url)
            yield scrapy.Request(url, callback=self.parse_fangurl, dont_filter=True, meta={'proxy': random.choice(ip)})
            # yield scrapy.Request(url, callback=self.parse_fangurl, dont_filter=True)

    def parse_fangurl(self, response):
        """获取每一页相应楼盘对应的url"""
        fangurl_list = response.xpath('//div[@class="info clear"]/div/a/@href').extract()
        for fangurl in fangurl_list:
            yield scrapy.Request(fangurl, meta={'url': fangurl, 'proxy': random.choice(ip)},callback=self.parse_detail, dont_filter=True, )
            # yield scrapy.Request(fangurl, meta={'url': fangurl}, callback=self.parse_detail, dont_filter=True, )

    def parse_detail(self, response):
        """具体处理获取某一个楼盘的信息"""

        url = response.meta['url']
        print(url)

        item = LianjiaItem()
        # 房屋标题
        try:
            item['houseTitle'] = response.xpath('//div[@class="content"]/div[@class="title"]/h1/text()').extract_first().strip()
        except:
            item['houseTitle'] = ''
        # 小区名称
        communityName = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        try:
            item["communityName"] = communityName
        except:
            item["communityName"] = ''

        # 所在区域和位置
        areaName = response.xpath('//div[@class="areaName"]/span[2]/a/text()').extract()
        try:
            item["areaName"] = areaName[0]
        except:
            item["areaName"] = ''
        try:
            item["location"] = areaName[1]
        except:
            item["location"] = ''

        # 房屋总价
        try:
            # 数值
            houseTotalMoneyNum = response.xpath('//div[@class="price "]/span[@class="total"]/text()').extract_first()
            # 单位
            houseTotalMoneyUnit = response.xpath('//div[@class="price "]/span[@class="unit"]/span/text()').extract_first()
            item['houseTotalMoney'] = houseTotalMoneyNum + houseTotalMoneyUnit
        except:
            item['houseTotalMoney'] = ''


        # 基本信息
        baseContent = ''.join(response.xpath('//div[@class="base"]/div[2]/ul/li').extract())
        try:
            item["houseType"] = re.findall(r'房屋户型</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseType"] = ''
        try:
            item["houseFloor"] = re.findall(r'所在楼层</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseFloor"] = ''
        try:
            item["houseBuildingArea"] = re.findall(r'建筑面积</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseBuildingArea"] = ''
        try:
            item["houseStructure"] = re.findall(r'户型结构</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseStructure"] = ''
        try:
            item["houseInnerArea"] = re.findall(r'套内面积</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseInnerArea"] = ''
        try:
            item["houseBuildingType"] = re.findall(r'建筑类型</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseBuildingType"] = ''
        try:
            item["houseOrientation"] = re.findall(r'房屋朝向</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseOrientation"] = ''
        try:
            item["houseBuildingStructure"] = re.findall(r'建筑结构</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseBuildingStructure"] = ''
        try:
            item["houseDecoration"] = re.findall(r'装修情况</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseDecoration"] = ''
        try:
            item["houseElevatorRatio"] = re.findall(r'梯户比例</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseElevatorRatio"] = ''
        try:
            item["houseElevator"] = re.findall(r'配备电梯</span>(.*?)</li>', baseContent)[0]
        except:
            item["houseElevator"] = ''
        try:
            item['housePrivilege'] = re.findall(r'产权年限</span>(.*?)</li>', baseContent)[0]
        except:
            item['housePrivilege'] = ''


        # 交易信息
        transactionContent = ''.join(response.xpath('//div[@class="transaction"]/div[2]/ul/li').extract())
        try:
            item["housePrivilegeProperty"] = re.findall(r'产权所属</span>\n                              <span>(.*?)</span>', transactionContent)[0]
        except:
            item["housePrivilegeProperty"] = ''
        try:
            item['houseListDate'] = re.findall(r'挂牌时间</span>\n                              <span>(.*?)</span>', transactionContent)[0]
        except:
            item['houseListDate'] = ''
        try:
            item['houseTradeProperty'] = re.findall(r'交易权属</span>\n                              <span>(.*?)</span>', transactionContent)[0]
        except:
            item['houseTradeProperty'] = ''
        try:
            item['houseLastTrade'] = re.findall(r'上次交易</span>\n                              <span>(.*?)</span>', transactionContent)[0]
        except:
            item['houseLastTrade'] = ''
        # 房屋用途
        try:
            item['houseUsage'] = re.findall(r'上次交易</span>\n                              <span>(.*?)</span>', transactionContent)[0]
        except:
            item['houseUsage'] = ''
        try:
            item['houseAgeLimit'] = re.findall(r'上次交易</span>\n                              <span>(.*?)</span>', transactionContent)[0]
        except:
            item['houseAgeLimit'] = ''
        try:
            item['housePrivilegeProperty'] = re.findall(r'上次交易</span>\n                              <span>(.*?)</span>', transactionContent)[0]
        except:
            item['housePrivilegeProperty'] = ''
        try:
            item['housePledge'] = re.findall(r'抵押信息</span>\n                              <span>(.*?)</span>', transactionContent)[0].replace(' ','').replace('\n','')
        except:
            item['housePledge'] = ''

        # 爬虫关键信息
        # 房屋URL地址
        item['houseUrl'] = url

        # 房屋爬虫时间
        item['CrawlTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


        yield item