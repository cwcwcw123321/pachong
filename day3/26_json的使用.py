import json


str='{"name":"盗梦空间"}'

print(type(str))

#json.loads()函数是将字符串转化为字典
obj=json.loads(str)
print(type(obj))

#json.dumps()函数是将字典转化为字符串
str2=json.dumps(obj,ensure_ascii=False)#不通过ascii码来转换
print(type(str2),":",str2)

#json.dump()和json.load()主要用来读写json文件函数
json.dump(obj,open('movie.txt','w',encoding='utf-8'),ensure_ascii=False)

str3=json.load(open('movie.txt',encoding='utf-8'))
print(str3)