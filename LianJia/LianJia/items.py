# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    communityName = scrapy.Field()
    areaName = scrapy.Field()
    roomType = scrapy.Field()
    louCeng = scrapy.Field()
    area = scrapy.Field()
    jianZhu = scrapy.Field()
    chaoXiang = scrapy.Field()
    zhuangXiu = scrapy.Field()
    tiHu = scrapy.Field()
    guapaitime = scrapy.Field()
    jiaoyitime = scrapy.Field()
    nianxian = scrapy.Field()
    totalPrice = scrapy.Field()
    location = scrapy.Field()
    """

    # 房屋基本信息
    houseTitle = scrapy.Field()  # 房屋标题
    houseTotalMoney = scrapy.Field()  # 房屋总价
    communityName = scrapy.Field()
    areaName = scrapy.Field()
    roomType = scrapy.Field()
    location = scrapy.Field()


    # 房屋基本属性
    houseType = scrapy.Field()  # 房屋户型
    houseFloor = scrapy.Field()  # 所在楼层
    houseBuildingArea = scrapy.Field()  # 房屋建筑面积
    houseStructure = scrapy.Field()  # 户型结构
    houseInnerArea = scrapy.Field()  # 房屋套内面积
    houseBuildingType = scrapy.Field()  # 建筑类型
    houseOrientation = scrapy.Field()  # 房屋朝向
    houseBuildingStructure = scrapy.Field()  # 建筑结构
    houseDecoration = scrapy.Field()  # 装修情况
    houseElevatorRatio = scrapy.Field()  # 梯户比例
    houseElevator = scrapy.Field()  # 电梯配备
    housePrivilege = scrapy.Field()  # 产权年限

    # 房屋交易属性
    houseListDate = scrapy.Field()  # 挂牌时间
    houseTradeProperty = scrapy.Field()  # 房屋交易权属
    houseLastTrade = scrapy.Field()  # 上次交易时间
    houseUsage = scrapy.Field()  # 房屋用途
    houseAgeLimit = scrapy.Field()  # 房屋年限
    housePrivilegeProperty = scrapy.Field()  # 产权所属
    housePledge = scrapy.Field()  # 抵押信息


    # 爬虫关键信息
    houseUrl = scrapy.Field()  # 房屋URL地址
    CrawlTime = scrapy.Field()  # 爬取时间
