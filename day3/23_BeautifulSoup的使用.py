from bs4 import BeautifulSoup
from bs4.element import Comment

str='''
<title id="title">尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''
soup=BeautifulSoup(str,'lxml')
# print(soup.title)
# print(soup.div)
#
# print(soup.div.attrs)
# print(soup.div.get('class'))
# print(soup.div['float'])
# print(soup.a['href'])
#
# print(soup.div.string)
# print(type(soup.strong.string))
# print(soup.div.text)

if type(soup.strong.string)==Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())#原样子显示
else:
    print(soup.strong.text)
