# -*- coding: utf-8 -*-
import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/rank/yuepiao?style=1']

    def parse(self, response):
        names=response.xpath('//h4/a/text()').extract()
        authors=response.xpath('//p[@class="author"]/a[@class="name"]/text()').extract()
        book=[]
        for name,author in zip(names,authors):
            book.append({'name':name,'author':author})
        return book