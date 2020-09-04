# -*- coding: utf-8 -*-
import scrapy

from topdb.items import Douban_tagsItem

class DoubanTagsSpider(scrapy.Spider):
    name = 'douban_tags'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']

    def parse(self, response):
        divs=response.xpath(".//div[@class='article']//div[@class]/div[@class]")

        print(len(divs))

        for div in divs:
            tag= div.xpath(".//h2/text()").extract_first()

            tag=tag.split('· · · · · ·')[0]
            print(tag)

            # url='https://book.douban.com/tag/'+classitem
            names=div.xpath("./table[@class='tagCol']//a/text()").extract()
            urls=div.xpath("./table[@class='tagCol']//a/@href").extract()

            for i in range(len(urls)):
                yield scrapy.Request('https://book.douban.com'+urls[i],callback=self.get_list,meta={'tag':tag,'name':names[i]},dont_filter=True)

    def get_list(self,response):
        tag=response.meta['tag']
        name=response.meta['name']

        list = response.xpath("//li[@class='subject-item']")

        for i_item in list:
            item = Douban_tagsItem()

            item['title'] = i_item.xpath(".//h2/a/text()").extract_first()
            urlinfo = i_item.xpath(".//h2/a/@href").extract_first()
            # print(urlinfo)

            if item['title']:
                item['title'] = item['title'].strip()

            details = i_item.xpath(".//div[@class='pub']/text()").extract_first()

            item['score'] = i_item.xpath(".//span[@class='rating_nums']/text()").extract_first()

            if item['score']:
                item['score'] = item['score'].strip()
                item['commentsnum'] = i_item.xpath(".//span[@class='pl']/text()").extract_first()

                if item['commentsnum']:
                    item['commentsnum'] = item['commentsnum'].strip()
                    item['commentsnum'] = item['commentsnum'].split('人评价', 1)[0].split('(', 1)[1]
                else:
                    item['commentsnum']=''

            arrs = details.split('/', 1)
            if len(arrs) > 1:
                item['author'] = arrs[0].strip()
                item['details'] = arrs[1].strip()
                if len(item['details'].split('/')) > 1:
                    item['date'] = item['details'].split('/').pop(-2).strip()
                else:
                    item['date'] = ''
            else:
                item['author'] = arrs
                item['details'] = arrs
                item['date'] = ''

            item['tag']=tag
            item['name']=name

            # print(urlinfo)
            # yield scrapy.Request(urlinfo,meta={'tag':item['tag'],'name':item['name'],'author':item['author'],'details':item['details'],'date':item['date'],'title':item['title'],'commentsnum':item['commentsnum'],'score':item['score']}, callback=self.get_info, dont_filter=True)
            # yield scrapy.Request(urlinfo, meta={'url':urlinfo},  callback=self.get_info)
            print(item)
            yield item

            # 解析下一页
        next_link = response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract_first()
        if next_link:
            yield scrapy.Request("https://book.douban.com" + next_link,meta={'tag':tag,'name':name}, callback=self.get_list, dont_filter=True)

    def get_info(self,response):
        taginfo=response.meta['url']
        print('infos')
        print(taginfo)

        # item['intro']=response.xpath(".//div[@id='link-report']/span[@class='all hidden']//div[@class='intro']/text()").extract_first()
        # item['autorintro']=response.xpath(".//div[@classs='indent '][2]//div[@class='intro']/text()").extract_first()

        # print(item)
        print('____________')



