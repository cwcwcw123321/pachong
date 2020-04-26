# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZwwSpider(CrawlSpider):
    name = 'zww'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.us/book/17512/']

    rules = (
        # 第一页地址
        Rule(LinkExtractor(restrict_xpaths='//dl/dd[10]/a'), callback='parse_item', follow=True),
        # 下一页地址
        Rule(LinkExtractor(restrict_xpaths='//div[@class="bottem1"]/a[4]'), callback='parse_item', follow=True),\

    )

    def parse_item(self, response):
        title=response.xpath('//h1/text()').extract_first()
        content=''.join(response.xpath('//div[@id="content"]/text()').extract())

        yield {
            "title":title,
            "content":content
        }