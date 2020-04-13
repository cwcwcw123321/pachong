import requests
from fake_useragent import UserAgent

session=requests.Session()
headers={
    "User-Agent":UserAgent().chrome
}

login_url="http://www.bljlmzzpt.com/Login_Member_Servlet"
params={
    "user":"adminblj",
    "psw":"adminblj"
}
response=session.post(login_url,headers=headers,data=params)
info_url="http://www.bljlmzzpt.com/admin/idioplasm.jsp"
resp=session.get(info_url,headers=headers)

print(resp.text)