# -*- coding: utf-8 -*-
import scrapy
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
            item['hotTitle'] =site.xpath('a/text()')
            item['url'] =site.xpath('a/@href').extract()
           # item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items