# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

import os

import json
class TopdbPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'database': 'novels',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        if spider.name=='douban_spider':
            self.cursor.execute("insert into douban_movie(movie_name,introduce,star,evaluate,describle,serial_number) values (%s,%s,%s,%s,%s,%s)",(item['movie_name'], item['introduce'],item['star'],item['evaluate'],item['describle'],item['serial_number']))
            self.conn.commit()
            return item

        if spider.name=='novels':
            # 同一个小说按章节名字保存txt文件
            if (not os.path.exists('/Users/qx/Documents/小说/new/'+item['tag']+'/'+item['name'] +'/'+ str(item['index']) + ".txt")):
                fp = open('/Users/qx/Documents/小说/new/'+item['tag']+'/'+item['name'] +'/'+ str(item['index']) + ".txt", "a", encoding='utf8')
                fp.write(item['chapter'])
                fp.write('\n\n')
                novel = item['novel'].encode('GBK', 'ignore').decode('GBk')  # 转码，否则报错
                fp.write(novel)
                fp.write('\n\n')
                fp.close()
                return item





