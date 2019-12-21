# -*- coding: utf-8 -*-
import re

schema_pattern = re.compile(r'http|https$', re.I)
ip_pattern = re.compile(r'^([0-9]{1,3}.){3}[0-9]{1,3}$', re.I)
port_pattern = re.compile(r'^[0-9]{2,5}$', re.I)

PROXY_URL_FORMATTER = '%(schema)s://%(ip)s:%(port)s'

class IPProxy:
    '''
    {
        "schema": "http", # 代理的类型
        "ip": "127.0.0.1", # 代理的IP地址
        "port": "8050", # 代理的端口号
    }
    '''

    def __init__(self, schema, ip, port):
        """Initialize the proxy instance"""
        if schema == "" or schema is None:
            schema = "http"
        self.schema = schema.lower()
        self.ip = ip
        self.port = port

    def _get_url(self):
        ''' Return the proxy url'''

        return PROXY_URL_FORMATTER % {'schema': self.schema, 'ip': self.ip, 'port': self.port}

    def _check_format(self):
        ''' Return True if the proxy fields are well-formed,otherwise return False'''
        if self.schema is not None and self.ip is not None and self.port is not None:
            if schema_pattern.match(self.schema) and ip_pattern.match(self.ip) and port_pattern.match(self.port):
                return True
        return False

    def _is_https(self):
        ''' Return True if the proxy is https,otherwise return False'''
        return self.schema == 'https'

    def _update(self, successed=False):
        ''' Update proxy based on the result of the request's response'''
        self.used_total = self.used_total + 1
        if successed:
            self.continuous_failed = 0
            self.success_times = self.success_times + 1
        else:
            print(self.continuous_failed)
            self.continuous_failed = self.continuous_failed + 1


if __name__ == '__main__':
    # 测试
    proxy = IPProxy('HTTPS', '192.168.2.25', "8080")
    print(proxy._get_url())
    print(proxy._check_format())
    print(proxy._is_https())


