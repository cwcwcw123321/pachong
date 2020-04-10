from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

url='http://www.bljlmzzpt.com/LoginMember.jsp'
form_data={
    'user':'adminblj',
    'pwd':'adminblj'
}
headers={
    'User-Agent':UserAgent().firefox
}

f_data=urlencode(form_data)
request=Request(url,data=f_data.encode(),headers=headers)
response=urlopen(request)
print(response.read().decode())

print(f_data)