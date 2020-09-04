# -*- coding: utf-8 -*-
import scrapy

import  os
from topdb.items import  BiqugeItem

class NovelsSpider(scrapy.Spider):
    name = 'novels'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']

    def parse(self, response):
        # 小说分类
        path = '/Users/qx/Documents/小说/new/'

        all=response.xpath(".//div[@class='novellist']")

        for oneitem in all:

            classname=oneitem.xpath('./h2/text()').extract_first()
            if classname=='奇幻小说、玄幻小说大全列表':
                classname='xuanhuan'
            if classname=='历史小说、军事小说、穿越小说大全列表':
                classname='chuanyue'
            if classname=='武侠小说、仙侠小说、修真小说大全列表':
                classname='xiuzhen'
            if classname=='言情小说、都市小说大全列表':
                classname='dushi'
            if classname=='异灵小说、科幻小说大全列表':
                classname='kehuan'
            if classname=='游戏小说、竞技小说、网游小说大全列表':
                classname='wangyou'

            urls=oneitem.xpath('./ul/li/a/@href').extract()

            names=oneitem.xpath('./ul/li/a/text()').extract()

            for i in range(len(urls)):
                url=urls[i]
                name=names[i]
                yield scrapy.Request(url, meta={'name': name, 'classname': classname}, callback=self.url_parse)


    def url_parse(self, response):
        # 小说章节列表
        print('小说章节')
        path = '/Users/qx/Documents/小说/new/'

        name = response.meta['name']
        classname = response.meta['classname']

        author = response.xpath("//div[@id ='info']/p/text()").extract_first()

        if author:
            author=author.split('：',1)[1]

        print(name+'-'+author)

        listurls = response.xpath("//div[@id ='list']/dl/dd/a/@href").extract()
        chapternames = response.xpath("//div[@id ='list']/dl/dd/a/text()").extract()

        for i in range(len(listurls)):
            url = "http://www.xbiquge.la" + listurls[i]
            chaptername=chapternames[i]

            oldname=path+ classname+'/'+name+ '-作者:' + author
            newname=path+ classname+'/'+name

            if (os.path.exists(oldname)):
                os.rename(oldname,newname)

            if (not os.path.exists(newname)):
                os.makedirs(newname)

            if(not os.path.exists(newname+'/'+ str(i) + ".txt")):
                yield scrapy.Request(url, meta={'chaptername':chaptername,'tag':classname,'name':name,'author':author,'index':i}, callback=self.detail_parse)

    def detail_parse(self, response):
        # 章节详细内容

        tag = response.meta['tag']
        name = response.meta['name']
        author = response.meta['author']
        chaptername = response.meta['chaptername']
        index = response.meta['index']

        item = BiqugeItem()

        novel = response.xpath("//div[@id='content']/text()").extract()
        item['novel'] = "\n".join(novel).replace("&nbsp", " ")
        item['name'] = name
        item['tag'] = tag
        item['author'] = author
        item['chapter'] = chaptername
        item['index'] = index

        # print(item['classname'])
        # print(item['name'])
        # print(item['title'])
        # print('\n')
        yield item

        # 这里是爬取整个网站且按照分类进行爬取  但是重点是 爬取太慢scrapy 是异步操作  还需要了解一下多线程的问题 这样速度能更快些
