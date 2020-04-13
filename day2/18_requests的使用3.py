from fake_useragent import UserAgent
import requests

url = "http://httpbin.org/get"
headers={
    "User-Agent":UserAgent().chrome
}
proxies={
    "http":"http://202.115.142.147:9200"
}
response=requests.get(url,headers=headers,proxies=proxies)
print(response.text)