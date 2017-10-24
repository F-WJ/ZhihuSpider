# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuQuestionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 知乎的问题item
    zhihu_id = scrapy.Field()                # 知乎的id
    topics = scrapy.Field()                  # 问题标题
    url = scrapy.Field()                     # 问题地址
    content = scrapy.Field()                 # 问题内容
    answer_num = scrapy.Field()              # 回答人数
    watch_user_num = scrapy.Field()          # 浏览数
    click_num = scrapy.Field()               # 点击数
    crawl_time = scrapy.Field()              # 爬行时间


class ZhihuAnswerItem(scrapy.Item):
    # 知乎的问题回答item
    zhihu_id = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()
    praise_num = scrapy.Field()         # 点赞量
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()
