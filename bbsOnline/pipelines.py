# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem
from bbsOnline import settings

import time
class OnlinePipeline(object):
    dbPrime = 97

    def __init__(self):
        leancloud.init(settings.APP_ID, master_key=settings.MASTER_KEY)

    def process_item(self, item, spider):
        tableIndex = int(1000*time.time())%self.dbPrime
        if tableIndex<10:
            tableIndexStr = '0' +str(tableIndex)
        else :
            tableIndexStr = str(tableIndex)

        BbsStatus = Object.extend('BbsStatus'+tableIndexStr)
        bbsStatus = BbsStatus()
        bbsStatus.set('requestTime',item['requestTime'])
        bbsStatus.set('totalOnlineCount',item['totalOnlineCount'])
        bbsStatus.set('userOnlineCount',item['userOnlineCount'])
        bbsStatus.set('guestOnlineCount',item['guestOnlineCount'])



        try:
            bbsStatus.save()

        except LeanCloudError,e:
            print e

        #return item
        DropItem()


