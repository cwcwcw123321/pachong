# 猫眼电影  xpath实现
from lxml import etree
from fake_useragent import UserAgent
import requests
from time import sleep
from random import randint


url = "https://maoyan.com/films?showType=2"

headers = {
    "User-Agent": UserAgent().chrome
}

response = requests.get(url, headers=headers)
response.encoding="utf-8"
e = etree.HTML(response.text)
movie_html_all = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
html = ['https://maoyan.com{}'.format(movie_html) for movie_html in movie_html_all]
print(html)

for movie_url in html:
    headers = {
        "User-Agent": UserAgent().chrome
    }

    response = requests.get(movie_url, headers=headers)
    response.encoding = "utf-8"

    m = etree.HTML(response.text)
    sleep(randint(5, 10))
    movie_name = m.xpath('//h1[@class="name"]/text()')
    sleep(randint(5, 10))
    movie_type = m.xpath('//li[@class="ellipsis"]/a/text()')
    sleep(randint(5, 10))
    movie_actor = m.xpath('//li[@class="celebrity actor"]/div/a/text()')


    print(movie_name,movie_type,movie_actor)
