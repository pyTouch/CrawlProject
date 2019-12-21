# -*- coding: utf-8 -*-
# @time: 2019/12/21
# @content: 利用mongodb构建IP代理池

from proxy_crawl import XiCiDailiCrawler, IPhaiDailiCrawler, YunDailiCrawler, FeiyiDailiCrawler


def run_xici():

    crawler = XiCiDailiCrawler(website='西刺代理',
                               urls=[{'url': 'https://www.xicidaili.com/', 'type': '首页推荐'},
                                     {'url': 'https://www.xicidaili.com/nn/{}', 'type': '国内高匿', 'page': 1},
                                     {'url': 'https://www.xicidaili.com/nt/{}', 'type': '国内普通', 'page': 1},
                                     {'url': 'https://www.xicidaili.com/wn/{}', 'type': '国外高匿', 'page': 1},
                                     {'url': 'https://www.xicidaili.com/wt/{}', 'type': '国外普通', 'page': 1}])


    crawler._start_crawl()


def run_iphai():
    crawler = IPhaiDailiCrawler(website='IP海代理',
                                urls=[{'url': 'http://www.iphai.com/free/ng', 'type': '国内高匿'},
                                      {'url': 'http://www.iphai.com/free/wg', 'type': '国外高匿'},
                                      {'url': 'http://www.iphai.com/free/wp', 'type': '国外普通'}])
    crawler._start_crawl()

    # {'url': 'http://www.iphai.com/free/np', 'type': '国内普通'}


def run_yun():
    crawler = YunDailiCrawler(website='云代理',
                              urls=[{'url': 'http://www.ip3366.net/free/?stype=1&page={}', 'type': '国内高匿', 'page': 1},
                                    {'url': 'http://www.ip3366.net/free/?stype=2&page={}', 'type': '国内普通', 'page': 1}])
    crawler._start_crawl()


def run_feiyi():
    feiyidailiCrawler = FeiyiDailiCrawler(website='飞蚁代理',
                                          urls=[{'url': 'http://www.feiyiproxy.com/?page_id=1457', 'type': '首页推荐'}])
    feiyidailiCrawler._start_crawl()


if __name__ == '__main__':

    run_xici()
    # run_iphai()
    # run_yun()
    # run_feiyi()

