# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class GamePipeline(object):
#class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    def __init__(self):
        self.file=open('./item.jl','wb')


    def process_item(self, item, spider):
        line=json.dump(dict(item))+"\n"
        self.file.write(line)
        return item