# -*- coding: utf-8 -*-

import pymongo
import random
import requests


class MongoDB(object):

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['ippool']
        self.proxies = self.db['ipproxy']

    """  
    def insert(self, proxy):
    try:
        self.proxies.insert(proxy)
        print('插入成功：{}'.format(proxy))
    except DuplicateKeyError:
        pass

    def update(self, conditions, values):
        self.proxies.update(conditions, {"$set": values})
        print('更新成功：{},{}'.format(conditions, values))
       
    """

    def delete(self, ip):
        self.proxies.remove({"ip": ip})
        print('删除成功：{}  代理池剩余ip数：{}'.format(ip, self.get_count()))


    def get(self, count):
        # 从代理池中随机取出一个ip并测试是否可用
        count = int(count)
        skip_num = random.randrange(count)
        items = self.proxies.find().skip(skip_num).limit(1)
        for item in items:
            schema = item['schema']
            ip_url = item['ip_url']
            ip = item['ip']
        if self._is_proxy_available(schema, ip_url):
            return ip_url
        else:
            # 不可用时直接删除
            self.delete(ip)
            return None

    def get_count(self):
        # 统计代理池中的ip数量
        return self.proxies.count({})

    def _is_proxy_available(self, schema, ip_url):

        # 验证ip可用性
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        proxies = {schema: ip_url}
        if schema == 'http':
            url = 'http://icanhazip.com'
            try:
                response = requests.get(url=url, proxies=proxies, headers=headers, timeout=10)
                if response.status_code == 200:
                    print((" 验证代理 {}   结果： 可用  ").format(ip_url))
                    return True
            except:
                print((" 验证代理 {}   结果： 不可用  ").format(ip_url))
            return False

        if schema == 'https':
            url = 'https://icanhazip.com'
            try:
                response = requests.get(url=url, proxies=proxies, headers=headers, timeout=10)
                if response.status_code == 200:
                    print((" 验证代理 {}   结果： 可用  ").format(ip_url))
                    return True
            except:
                print((" 验证代理 {}   结果： 不可用  ").format(ip_url))
            return False

    def close_mongo(self):

        # 关闭数据库连接
        self.client.close()


