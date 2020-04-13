from urllib.request import Request,urlopen
from urllib.error import URLError
from fake_useragent import UserAgent

url="http://www.sx123t.cn/index/login/login123"

headers={
    "User_Agent":UserAgent().chrome
}

try:
    request=Request(url,headers=headers)
    response=urlopen(request)
    print(response.read().decode())
except URLError as e:
    if e.args==():
        print(e.code)
    else:
        print(e.args[0].errno)
print('访问完成')