from lxml import etree
import requests
from fake_useragent import UserAgent

url="https://www.qidian.com/rank/fengyun?style=1&chn=21&page=1"

headers={
    "User-Agent":UserAgent().chrome
}
response=requests.get(url,headers=headers)
e=etree.HTML(response.text)
names=e.xpath('//h4/a/text()')
authors=e.xpath('//p[@class="author"]/a[1]/text()')

for num  in range(len(names)):
    print(names[num],":",authors[num])

# for name,author in zip(names,authors):
#     print(name,":",author)