from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

args={
    'wd':'尚学堂',
    'ie':'utf-8'
}

url='http://www.baidu.com/s?{}'.format(urlencode(args))
print(url)

headers={
    'User-Agent':UserAgent().random
}
request = Request(url,headers=headers)
response=urlopen(request)

info =response.read()
print(info.decode())