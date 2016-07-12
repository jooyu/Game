# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

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
            host = '192.168.23.135' ,
            db = 'game',
            user = 'root', #replace with you user name
            passwd = '123456', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)



    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
    def insert_into_table(self,conn,item):
                conn.execute('insert into zreading(title,author,pub_date,types,tags,view_counts,content) values(%s,%s,%s,%s,%s,%s,%s)', (item['title'],item['author'],item['pub_date'],item['types'],item['tags'],item['view_count'],item['content']))