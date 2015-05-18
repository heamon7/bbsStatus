# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.http import Request,FormRequest

import re
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem
from datetime import datetime
from  bbsOnline.items import BbsonlineItem
from bbsOnline import settings
import os

class OnlinerSpider(scrapy.Spider):
    name = "onliner"
    allowed_domains = ["bbs.byr.cn"]
    start_urls = (
        'http://bbs.byr.cn/index',
    )
    def __init__(self,stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def parse(self, response):
        item = BbsonlineItem()
        item['requestTime'] = datetime.now()
        item['totalOnlineCount'] = int(response.xpath('//*[@id="bot_info"]/span[@class="c-total"]/text()').extract()[0])
        item['userOnlineCount'] = int(response.xpath('//*[@id="bot_info"]/span[@class="c-user"]/text()').extract()[0])
        item['guestOnlineCount'] = int(response.xpath('//*[@id="bot_info"]/span[@class="c-guest"]/text()').extract()[0])

        return item

    def closed(self,reason):
        #f = open('../../nohup.out')
        #print f.read()
        leancloud.init(settings.APP_ID, master_key=settings.MASTER_KEY)

        try:
            nohupOut = open(os.getcwd()+'/nohup.out','r').read()
        except:
            nohupOut = "Cannot read nohup.out file"
        CrawlerLog = Object.extend('CrawlerLog')
        crawlerLog = CrawlerLog()

        crawlerLog.set('crawlerName',self.name)
        crawlerLog.set('crawlerLog',nohupOut)
        crawlerLog.set('closedReason',reason)
        crawlerLog.set('crawlerStats',self.stats.get_stats())
        try:
            crawlerLog.save()
        except:
            pass