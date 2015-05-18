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
LOG_LEVEL = 'INFO'
DOWNLOAD_TIMEOUT = 700

CONCURRENT_REQUESTS = 70
CONCURRENT_REQUESTS_PER_DOMAIN = 70

APP_ID = 'rb4tkl4c970mzj32qgbjhvil7nhbq4fuzp6zs8o4yly9i8kn'
MASTER_KEY = 'kk2m9sscwun4ftihpj8az0zk55rry2ee22w25ip58yw7bfqt'

ITEM_PIPELINES = {
    'bbsOnline.pipelines.OnlinePipeline': 300,
   # 'zhihut.pipelines.SecondPipline': 800,
}