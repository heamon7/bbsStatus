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

class OnlinerSpider(scrapy.Spider):
    name = "onliner"
    allowed_domains = ["bbs.byr.cn"]
    start_urls = (
        'http://bbs.byr.cn/index',
    )

    def parse(self, response):
        item = BbsonlineItem()
	item['requestTime'] = datetime.now()
        item['totalOnlineCount'] = int(response.xpath('//*[@id="bot_info"]/span[@class="c-total"]/text()').extract()[0])
        item['userOnlineCount'] = int(response.xpath('//*[@id="bot_info"]/span[@class="c-user"]/text()').extract()[0])
        item['guestOnlineCount'] = int(response.xpath('//*[@id="bot_info"]/span[@class="c-guest"]/text()').extract()[0])

        return item
