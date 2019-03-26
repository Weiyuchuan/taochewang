# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class Pachongday14Pipeline(object):
    def __init__(self):
        #链接本地数据库
        self.client=pymongo.MongoClient('localhost')
        #数据库:
        self.db = self.client['taoche']
        #集合：
        self.esc =self.db['esc']
        print('--------------------')
    def process_item(self, item, spider):
        print("#####################3")
        self.esc.insert(dict(item))

        return item
