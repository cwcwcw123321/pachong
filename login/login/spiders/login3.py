# -*- coding: utf-8 -*-
import scrapy
import re

class Login3Spider(scrapy.Spider):
    name = 'login3'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):
        hash_code =re.findall(r'"__hash__":"(.+)"',response.text)[0]
        img_url='https://passport.ganji.com/ajax.php?dir=captcha&module=login_captcha'
        yield scrapy.Request(img_url,callback=self.parse_info,meta={'hash_code':hash_code})

    def parse_info(self,response):
        hash_code=response.request.meta['hash_code']
        with open('yzm.jpg','wb') as f:
            f.write(response.body)

        code=input('请输入验证码')
        form_data={
            "username": "18189558873",
            "password": "1988916.0jing",
            "setcookie": "0",
            "checkCode": code,
            "next": " /",
            "source": "passport",
            "__hash__": hash_code
        }
        login_url='https://passport.ganji.com/login.php'
        yield scrapy.FormRequest(login_url,callback=self.after_login,formdata=form_data)
    def after_login(self,response):
        print(response.text)