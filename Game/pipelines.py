# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#by zhuyu 2016.7.12
import json
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
class GamePipeline(object):
#class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    def __init__(self):
        dbargs = dict(
            host = '127.0.0.1',
            db = 'game',
            user = 'root', #replace with you user name
            passwd = '', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            #use_unicode = true,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
    def insert_into_table(self,conn,item):
        #先转码在存储2016.7.12
        conn.execute('insert into game_info(tag,hotTitle,url) values(%s,%s,%s)',
                            # (item['tag'],item['hotTitle'],item['url']))
                             (item['tag'],item['hotTitle'],item['url']))