import requests
from fake_useragent import UserAgent

headers={
    "User-Agent":UserAgent().chrome
}

url="http://www.bljlmzzpt.com/Login_Member_Servlet"
params={
    "user":"adminblj",
    "psw":"adminblj"
}
response=requests.get(url,headers=headers,params=params)

print(response.text)