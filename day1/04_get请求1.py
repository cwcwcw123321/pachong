from urllib.request import Request,urlopen
from urllib.parse import quote

print(quote('尚学堂'))

url='http://www.baidu.com/s?wd={}'.format(quote('尚学堂'))
headers={
    'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0'
}
request=Request(url,headers=headers)
response=urlopen(request)
print(response.read().decode())

