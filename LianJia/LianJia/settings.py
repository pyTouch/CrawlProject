# -*- coding: utf-8 -*-

# Scrapy settings for LianJia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'LianJia'

SPIDER_MODULES = ['LianJia.spiders']
NEWSPIDER_MODULE = 'LianJia.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100  # 增大并发数
LOG_LEVEL = 'ERROR' # 降低日志等级，提高scrapy性能
DOWNLOAD_TIMEOUT = 30 # 建议分段爬取时打开，或者随机IP稳定情况下也可打开

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2    # 仅在使用随机代理IP情况下注销，否则打开
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'LianJia.middlewares.LianjiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'LianJia.middlewares.LianjiaDownloaderMiddleware': 543,
    # 'LianJia.middlewares.ProxyMiddleware': 543,   # 通过middlewares设置ip代理，但是请求头会携带本机ip
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,   # 通过scrapy_fake_useragent包设置随机代理
    # 'LianJia.middlewares.RandomUserAgent': 200, # 通过middlewares设置随机UA，但是请求头会携带scrapy的UA
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'LianJia.pipelines.LianjiaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 指定文件输出顺序
# 爬虫名称：shanghai、shengzhan
# FEED_EXPORT_FIELDS = ['communityName', 'areaName', 'roomType', 'louCeng', 'area', 'jianZhu', 'chaoXiang', 'zhuangXiu', 'tiHu', 'guapaitime', 'jiaoyitime', 'nianxian', 'totalPrice', 'location']

# 爬虫名称：shanghai1、nanning
FEED_EXPORT_FIELDS = ['location', 'areaName','communityName','roomType', 'houseTotalMoney',
                      'houseType', 'houseFloor', 'houseBuildingArea', 'houseStructure',
                      'houseAgeLimit','houseBuildingStructure','houseBuildingType','houseDecoration',
                      'houseInnerArea', 'houseElevator', 'houseElevatorRatio', 'houseLastTrade', 'houseOrientation',
                      'houseListDate','housePledge', 'housePrivilege',  'houseUsage', 'housePrivilegeProperty', 'houseTradeProperty',
                      'houseTitle', 'houseUrl','CrawlTime']

# 随机ip
ip = ['https://218.60.8.99:3129', 'https://120.234.63.196:3128',
      'https://51.158.113.142:8811', 'https://51.158.99.51:8811',
      'https://118.174.211.220:11', 'https://23.237.173.102:3128',
      'https://45.70.58.172:9991']















