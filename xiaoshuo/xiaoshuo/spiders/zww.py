# -*- coding: utf-8 -*-
import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.us/book/606/424359.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract())

        yield {
            'title': title,
            'content': content
        }
        next_url = response.xpath('//div[@class="bottem2"]/a[4]/@href').extract_first()
        # base_url='https://www.81zw.us/book/606/{}'.format(next_url)#第一种方法 之前学习的方法
        # response.urljoin(next_url) 起的作用相当与上一行
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)  # 给一个参数 让parse来解析网址
