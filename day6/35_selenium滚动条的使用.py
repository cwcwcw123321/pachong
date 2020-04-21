from selenium import webdriver
from lxml import etree
from time import sleep

url="https://search.jd.com/Search?keyword=%E4%B8%80%E5%8A%A0%20%208," \
    "&enc=utf-8&suggest=3.his.0.0&wq=&pvid=60fe34f44a91482f8243b072f3b5712a"

firfox=webdriver.Firefox()
firfox.get(url)

#firfox
# js 控制浏览器到底部  到底部刷新出整个页面的完整信息
# js="var q=document.documentElement.scrollTop=10000"
#     driver.execute_script(js)
#chrome
# js = "var q=document.body.scrollTop=0"
# driver.execute_script(js)

js="var q=document.documentElement.scrollTop=100000"
firfox.execute_script(js)
sleep(5)
html=firfox.page_source
e=etree.HTML(html)
prices=e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
names=e.xpath('//div[@class="p-name p-name-type-2"]/a/em')
for name,price in zip(names,prices):
    print(name.xpath('string(.)') ,":" ,price)
firfox.quit()