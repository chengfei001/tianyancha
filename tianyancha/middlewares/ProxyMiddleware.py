# -*-coding:utf-8 -*-
# 
# Created on 2016-03-02, by felix
# 

__author__ = 'chengfei'

import random
from ..settings import PROXIES


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = proxy['user_pass']
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print("**************ProxyMiddleware have pass************" + proxy['ip_port'])
        else:
            print ("**************ProxyMiddleware no pass************" + proxy['ip_port'])
            request.meta['proxy'] = "http://%s" % proxy['ip_port']