# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class TianyanchaPipeline(object):

    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client.tianyancha
        self.enterprise = self.db.enterprise

    def process_item(self, item, spider):
        if item['company_name'] != '':
            self.enterprise.insert(dict(item))
            return item
        pass

    def close_spider(self,spider):
        self.client.close()