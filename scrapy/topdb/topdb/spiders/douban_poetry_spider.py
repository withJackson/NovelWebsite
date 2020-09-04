# -*- coding: utf-8 -*-
import scrapy

from topdb.items import Douban_poetry_spiderItem

class DoubanPoetrySpiderSpider(scrapy.Spider):
    name = 'douban_poetry_spider'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/%E8%AF%97%E6%AD%8C']

    def parse(self, response):
        print('nihao')
        poetry_list = response.xpath("//li[@class='subject-item']")
        for i_item in poetry_list:
            portry_item = Douban_poetry_spiderItem()

            portry_item['title'] = i_item.xpath(".//h2/a/text()").extract_first()
            if portry_item['title']:
                portry_item['title']=portry_item['title'].strip()

            details = i_item.xpath(".//div[@class='pub']/text()").extract_first()


            portry_item['score'] = i_item.xpath(".//span[@class='rating_nums']/text()").extract_first()
            if portry_item['score']:
                portry_item['score']=portry_item['score'].strip()
            portry_item['commentsnum'] = i_item.xpath(".//span[@class='pl']/text()").extract_first()
            if portry_item['commentsnum']:
                portry_item['commentsnum']=portry_item['commentsnum'].strip()
                portry_item['commentsnum']=portry_item['commentsnum'].split('人评价',1)[0].split('(',1)[1]


            arrs=details.split('/', 1)
            if len(arrs)>1:
                portry_item['author'] = arrs[0].strip()
                portry_item['chuban'] = arrs[1].strip()
                if len(portry_item['chuban'].split('/')) > 1:
                    portry_item['date'] = portry_item['chuban'].split('/').pop(-2).strip()
                else:
                    portry_item['date'] = ''
            else:
                portry_item['author'] = arrs
                portry_item['chuban'] = arrs
                portry_item['date'] = ''

            print(portry_item['title'])
            print(portry_item['author'])
            print(portry_item['score'])
            print(portry_item['chuban'])
            print(portry_item['commentsnum'])
            print(portry_item['date'])
            print('____________')
            yield portry_item

            # 解析下一页
        next_link = response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract_first()
        if next_link:
            yield scrapy.Request("https://book.douban.com" + next_link, callback=self.parse,dont_filter=True)