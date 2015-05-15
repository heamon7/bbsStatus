# -*- coding: utf-8 -*-

# Scrapy settings for bbsOnline project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbsOnline'

SPIDER_MODULES = ['bbsOnline.spiders']
NEWSPIDER_MODULE = 'bbsOnline.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbsOnline (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'bbsOnline.pipelines.OnlinePipeline': 300,
   # 'zhihut.pipelines.SecondPipline': 800,
}