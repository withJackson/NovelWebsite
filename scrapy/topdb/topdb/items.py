# -*- coding: utf-8 -*-

import scrapy


class TopdbItem(scrapy.Item):
    serial_number = scrapy.Field()
    movie_name = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    evaluate = scrapy.Field()
    describle = scrapy.Field()

class CommentSpider(scrapy.Item):
    movie_name = scrapy.Field()
    comment_date = scrapy.Field()
    content = scrapy.Field()
    comment_score = scrapy.Field()

class MoriItem(scrapy.Item):
    name = scrapy.Field()  # 小说名字
    index = scrapy.Field()  # 章节名字
    chapter_name = scrapy.Field()  # 小说章节名字
    chapter_content = scrapy.Field()  # 小说章节内容


class BiqugeItem(scrapy.Item):
    tag = scrapy.Field()  # 小说类别

    name = scrapy.Field()  # 小说名字

    author = scrapy.Field()  # 小说作者

    chapter = scrapy.Field()  # 小说章节目录

    index = scrapy.Field()  # 小说次序

    novel = scrapy.Field()  # 小说章节内容

class LenwenItem(scrapy.Item):
    content=scrapy.Field()



class Douban_poetry_spiderItem(scrapy.Item):
    title = scrapy.Field()  # 名称
    author = scrapy.Field()  # 作者
    chuban = scrapy.Field()  # 出版
    date = scrapy.Field()  # 日期
    score = scrapy.Field()  # 评分
    commentsnum = scrapy.Field()  # 评论数




class Douban_tagsItem(scrapy.Item):


    tag=scrapy.Field()  #标签
    name=scrapy.Field()  #类别

    title=scrapy.Field()  #书名
    author=scrapy.Field()  #作者
    date=scrapy.Field()    #日期

    details=scrapy.Field()   #细节

    score=scrapy.Field()  #评分

    commentsnum = scrapy.Field()  # 评论数

    intro=scrapy.Field()   #简介

    autorintro=scrapy.Field()  #作者简介


class ninfosItem(scrapy.Item):

    name=scrapy.Field()  #书名
    intro=scrapy.Field()  #简介
    author=scrapy.Field()  #简介
    headimg=scrapy.Field()    #日期
    utime=scrapy.Field()   #细节



class rankItem(scrapy.Item):
    rank=scrapy.Field()    #排名
    classname=scrapy.Field()   #类别
    name = scrapy.Field()  # 书名
    bytime=scrapy.Field()   #时间序列



class homeItem(scrapy.Item):
    name = scrapy.Field()  # 书名
    area = scrapy.Field()  #
    idx = scrapy.Field()  # 排列顺序


class chapterItem(scrapy.Item):
    name = scrapy.Field()  #书名
    idx = scrapy.Field() #更新章节数



class novelroot(scrapy.Item):
    name=scrapy.Field()
    root=scrapy.Field()# 补充小说类型











