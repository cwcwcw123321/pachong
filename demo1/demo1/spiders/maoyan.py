# -*- coding: utf-8 -*-
import scrapy
from demo1.items import Demo1Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=3']

    def parse(self, response):
        names=response.xpath('///div[@class="channel-detail movie-item-title"]/@title').extract()
        scores_div=response.xpath('//div[@class="channel-detail channel-detail-orange"]')
        scores=[]
        for score in scores_div:
            scores.append(score.xpath('string(.)').extract_first())

        #通过pipelines 来传递参数
        # for name,score in zip(names,scores):
        #     # print(name,":",score)
        #     yield  {"name":name,"score":score}

        #通过item来传递参数
        item =Demo1Item()
        for name,score in zip(names,scores):
            item['name']=name
            item['score']=score

            yield item
