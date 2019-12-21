# -*- coding: utf-8 -*-
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

def request_page(url, options={}, encoding='utf-8'):

    print(("正在抓取: {} ").format(url))
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(("抓取成功: {} ").format(url))
            return response.content.decode(encoding=encoding)
    except ConnectionError:
        print(("抓取失败: {} ").format(url))
        return None


def _is_proxy_available(proxy, options={}):

    """Check whether the Proxy is available or not"""
    proxies = {proxy.schema: proxy._get_url()}
    # PROXY_CHECK_URLS = {'https': ['https://icanhazip.com'], 'http': ['http://icanhazip.com']}

    if proxy.schema == 'http':
        url = 'http://icanhazip.com'
        try:
            response = requests.get(url=url, proxies=proxies, headers=headers, timeout=5)
            if response.status_code == 200:
                print((" 验证代理 {}   结果： 可用  ").format(proxy._get_url()))
                return True
        except:
            print((" 验证代理 {}   结果： 不可用  ").format(proxy._get_url()))
        return False

    if proxy.schema == 'https':
        url = 'https://icanhazip.com'
        try:
            response = requests.get(url=url, proxies=proxies, headers=headers, timeout=5)
            if response.status_code == 200:
                print((" 验证代理 {}   结果： 可用  ").format(proxy._get_url()))
                return True
        except:
            print((" 验证代理 {}   结果： 不可用  ").format(proxy._get_url()))
        return False

