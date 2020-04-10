from urllib.request import Request,urlopen
from fake_useragent import UserAgent

base_url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

for i in range(10):

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }
    url=base_url.format(i*20)
    request=Request(url,headers=headers)
    response=urlopen(request)
    print(response.read().decode())