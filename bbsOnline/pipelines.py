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

class OnlinePipeline(object):
    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')

    def process_item(self, item, spider):

        BbsStatus = Object.extend('BbsStatus')
        bbsStatus = BbsStatus()
	bbsStatus.set('requestTime',item['requestTime'])
        bbsStatus.set('totalOnlineCount',item['totalOnlineCount'])
        bbsStatus.set('userOnlineCount',item['userOnlineCount'])
        bbsStatus.set('guestOnlineCount',item['guestOnlineCount'])



        try:
            bbsStatus.save()

        except LeanCloudError,e:
            print e

        return item
        #DropItem()


