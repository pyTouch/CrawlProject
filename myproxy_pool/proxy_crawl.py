# -*- coding: utf-8 -*-

from lxml import etree
from proxy_util import request_page, _is_proxy_available
from ipproxy import IPProxy
from pymongo import MongoClient


class ProxyBaseCrawler(object):

    def __init__(self, queue=None, website=None, urls=[]):
        self.queue = queue
        self.website = website
        self.urls = urls

    def _start_crawl(self):
        raise NotImplementedError


class XiCiDailiCrawler(ProxyBaseCrawler):  # 西刺代理

    def _start_crawl(self):
        self.client = MongoClient()

        for url_dict in self.urls:
            print(("开始爬取 {} :::> {}").format(self.website, url_dict['type']))
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                    if url_dict['page'] > 3:
                        # 限制每个url_dict['url']只爬取10页
                        has_more = False
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                tr_list = html.xpath("//table[@id='ip_list']//tr[@class!='subtitle']")
                for tr in tr_list:
                    ip = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    port = tr.xpath("./td[3]/text()")[0] if len(tr.xpath("./td[3]/text()")) else None
                    schema = tr.xpath("./td[6]/text()")[0] if len(tr.xpath("./td[6]/text()")) else None
                    if schema.lower() == "http" or schema.lower() == "https":
                        proxy = IPProxy(schema=schema.strip(), ip=ip.strip(), port=port.strip())
                        if _is_proxy_available(proxy):
                            if proxy.schema == 'https':
                                self.client.ippool.https.insert(
                                    {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                            if proxy.schema == 'http':
                                self.client.ippool.http.insert(
                                    {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                if tr_list is None:
                    has_more = False

        self.client.close()


class IPhaiDailiCrawler(ProxyBaseCrawler):  # IP海代理

    def _start_crawl(self):
        self.client = MongoClient()
        for url_dict in self.urls:
            print(("开始爬取 {} :::> {}").format(self.website, url_dict['type']))
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                    if url_dict['page'] > 20:
                        # 限制每个url_dict['url']只爬取10页
                        has_more = False
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                tr_list = html.xpath("//table//tr[position()>1]")
                for tr in tr_list:
                    ip = tr.xpath("./td[1]/text()")[0] if len(tr.xpath("./td[1]/text()")) else None
                    port = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    schema = tr.xpath("./td[4]/text()")[0] if len(tr.xpath("./td[4]/text()")) else 'http'
                    proxy = IPProxy(schema=schema.strip(), ip=ip.strip(), port=port.strip())
                    if _is_proxy_available(proxy):
                        if proxy.schema == 'https':
                            self.client.ippool.https.insert(
                                {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                        if proxy.schema == 'http':
                            self.client.ippool.http.insert(
                                {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                if tr_list is None:
                    has_more = False
        self.client.close()


class YunDailiCrawler(ProxyBaseCrawler):  # 云代理

    def _start_crawl(self):
        self.client = MongoClient()
        for url_dict in self.urls:
            print(("开始爬取 {} :::> {}").format(self.website, url_dict['type']))
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                    if url_dict['page'] > 4:
                        # 限制每个url_dict['url']只爬取3页
                        has_more = False
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url, encoding='gbk'))
                tr_list = html.xpath("//table/tbody/tr")
                for tr in tr_list:
                    ip = tr.xpath("./td[1]/text()")[0] if len(tr.xpath("./td[1]/text()")) else None
                    port = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    schema = tr.xpath("./td[4]/text()")[0] if len(tr.xpath("./td[4]/text()")) else None
                    proxy = IPProxy(schema=schema.strip(), ip=ip.strip(), port=port.strip())
                    if _is_proxy_available(proxy):
                        if proxy.schema == 'https':
                            self.client.ippool.https.insert(
                                {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                        if proxy.schema == 'http':
                            self.client.ippool.http.insert(
                                {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                if tr_list is None:
                    has_more = False
        self.client.close()


class FeiyiDailiCrawler(ProxyBaseCrawler):  # 飞蚁代理

    def _start_crawl(self):
        self.client = MongoClient()
        for url_dict in self.urls:
            print(("开始爬取 {} :::> {}").format(self.website, url_dict['type']))
            has_more = True
            url = None
            while has_more:
                if 'page' in url_dict.keys() and str.find(url_dict['url'], '{}') != -1:
                    url = url_dict['url'].format(str(url_dict['page']))
                    url_dict['page'] = url_dict['page'] + 1
                else:
                    url = url_dict['url']
                    has_more = False
                html = etree.HTML(request_page(url))
                tr_list = html.xpath("//div[@id='main-content']//table/tr[position()>1]")
                for tr in tr_list:
                    ip = tr.xpath("./td[1]/text()")[0] if len(tr.xpath("./td[1]/text()")) else None
                    port = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) else None
                    schema = tr.xpath("./td[4]/text()")[0] if len(tr.xpath("./td[4]/text()")) else None
                    proxy = IPProxy(schema=schema.strip(), ip=ip.strip(), port=port.strip())
                    if _is_proxy_available(proxy):
                        if proxy.schema == 'https':
                            self.client.ippool.https.insert(
                                {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                        if proxy.schema == 'http':
                            self.client.ippool.http.insert(
                                {"schema": proxy.schema, "ip": proxy.ip, "ip_url": proxy._get_url()})
                if tr_list is None:
                    has_more = False

        self.client.close()