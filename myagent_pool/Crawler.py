# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time

"""
    爬取代理网站的免费代理并返回
"""

cookie_xici = '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWU3OTJjYWVkYWQyMDVlN2NiMTUzNDI0OGQ2NGI3ZDY0BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWkwTUFiWWJXNW1adUd0Ymk0RUE4K3NUa2VpMFNya3hXcFE5b21qdENZS3M9BjsARg%3D%3D--60ef057aa905666629d7726c7d424b1405d50641; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1576426703,1576673326,1576841676,1577499725; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1577499736'
cookie_66 = 'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1577508322; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1577508322'
cookie_kuai = 'channelid=0; sid=1576426674807700; _ga=GA1.2.1038958140.1576426676; _gid=GA1.2.2004692490.1577509079; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1576426677,1576859075,1576895107,1577509079; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1577509104'


class Crawler(object):

    def get_crawler_proxy(self):
        proxy_list_xici = self.crawl_xici()
        # proxy_list_66 = self.crawl_66()
        # proxy_list_kuaidaili = self.crawl_kuaidaili()
        # return proxy_list_xici + proxy_list_66 + proxy_list_kuaidaili
        return proxy_list_xici

    def crawl_xici(self):
        """
            爬取西刺代理
        """
        print('爬取西刺代理......')
        proxy_list = []
        for i in range(1, 20):
            try:
                url = 'http://www.xicidaili.com/nn/' + str(i)
                # url = 'http://www.baidu.com'
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7',
                    'Host': 'www.xicidaili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                    'Cookie': cookie_xici
                }
                res = requests.get(url, headers=headers)
                if res.status_code == 200:
                    doc = pq(res.text)
                    # #是查找id的标签;.是查找class 的标签;link 是查找link 标签
                    # items遍历查找结果
                    for odd in doc('.odd').items():
                        info_list = odd.find('td').text().split(' ')
                        # print(info_list)
                        if len(info_list) == 11:
                            proxy = info_list[1].strip() + ':' + info_list[2].strip()
                            proxy = proxy.replace(' ', '')
                            proxy_list.append(proxy)
            except Exception as e:
                continue
        print('爬取到西刺代理 %s 个' % len(proxy_list))
        return proxy_list


    def crawl_66(self):
        """
            爬取66代理
        """
        print('爬取66代理......')
        proxies = set()
        for i in range(2, 50):
            try:
                url = 'http://www.66ip.cn/' + str(i) + '.html'
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7',
                    'Host': 'www.66ip.cn',
                    'Referer': 'http://www.66ip.cn/',
                    'Cookie': cookie_66,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                # print(res.status_code)
                # print(res.text)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('.container table tr')

                for i in range(1, len(items)):
                    tds = items[i].select('td')
                    ip = tds[0].string
                    port = tds[1].string
                    proxy = ip + ':' + port
                    if proxy:
                        # print(proxy)
                        # print(proxy.replace(' ', ''))
                        proxies.add(proxy.replace(' ', ''))
            except Exception as e:
                continue
        print('爬取到66代理 %s 个' % len(proxies))
        return list(proxies)


    def crawl_kuaidaili(self):
        print('爬取快代理......')
        proxies = set()
        for i in range(1, 50):
            try:
                url = 'https://www.kuaidaili.com/free/inha/' + str(i)
                time.sleep(1)
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7',
                    'Host': 'www.kuaidaili.com',
                    'Referer': 'https://www.kuaidaili.com/free/inha/1/',
                    'Cookie': cookie_kuai,
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                # print(res.status_code)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('#list tbody tr')
                for item in items:
                    tds = item.select('td')
                    ip = tds[0].string
                    port = tds[1].string
                    proxy = ip + ':' + port
                    if proxy:
                        proxies.add(proxy.replace(' ', ''))
            except Exception as e:
                continue
        print('爬取到块代理 %s 个' % len(proxies))
        return list(proxies)
