# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SiteItem(scrapy.Item):
    region_count = scrapy.Field()
    all_count = scrapy.Field()
    web_online = scrapy.Field()
    play_online = scrapy.Field()

class BangumiItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    data = scrapy.Field()

class VideoItem(scrapy.Item):
    channel = scrapy.Field()
    aid = scrapy.Field()
    datetime = scrapy.Field()
    author = scrapy.Field()
    data = scrapy.Field()
    subChannel = scrapy.Field()
    title = scrapy.Field()
    mid = scrapy.Field()
    pic = scrapy.Field()

class AuthorItem(scrapy.Item):
    mid = scrapy.Field()
    name = scrapy.Field()
    face = scrapy.Field()
    official = scrapy.Field()
    sex = scrapy.Field()
    data = scrapy.Field()
    level = scrapy.Field()
    focus = scrapy.Field()

class VideoOnline(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    data = scrapy.Field()
    aid = scrapy.Field()
    subChannel = scrapy.Field()
    channel = scrapy.Field()
    
class VideoWatcherItem(scrapy.Item):
    mid = scrapy.Field()
    aid = scrapy.Field()
    channels = scrapy.Field()