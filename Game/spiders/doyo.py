# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from Game.items import GameItem
class DoyoSpider(scrapy.Spider):
    name = "doyo"
    allowed_domains = ["www.doyo.cn"]
    start_urls = (
        'http://www.doyo.cn/',
    )

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)

        sites = sel.xpath('//div[@class="tl"]//ul//li')
        items = []

        for site in sites:
            item = GameItem()
            item['tag']=site.xpath('span/text()').extract()[0].encode('utf-8')
            item['hotTitle'] =site.xpath('a/text()').extract()[0].encode('utf-8')
            #2016.7.17修复抓取url，统一格式化输出相对路径
            item['url'] =site.xpath('a/@href').extract()[0].encode('utf-8').replace('http://www.doyo.cn','')
             #re.findall('\/\w*\/\w*',site.xpath('a/@href').extract()[0].encode('utf-8'))
            # site.xpath('a/@href').extract()[0].encode('utf-8').search('\/[A-Za-Z]*\/[0-9]*')
           # item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items