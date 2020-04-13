from urllib.request import Request,build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url="http://httpbin.org/get"

headers={
    "User_Agent":UserAgent().chrome
}

request=Request(url,headers=headers)
handler=ProxyHandler({'http':'202.115.142.147:9200'})
opener=build_opener(handler)
response=opener.open(request)
print(response.read().decode())