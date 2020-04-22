import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql
#彩票数据所在的url
url='http://datachart.500.com/ssq/'
headers={
    "User-Agent":UserAgent().chrome
}
#提取数据
response=requests.get(url,headers=headers)
#通过xpath去解析
e=etree.HTML(response.text)
data_times=e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs=e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')
#链接数据库
client=pymysql.connect(host='localhost',port=3306,user='root',password='7895123',charset='utf8',db='ball')
cursor=client.cursor()
#插入数据的sql
sql= 'insert into t_ball values(0,%s,%s,%s)'
#查看数据是否存在
select_new_sql="select * from t_ball where data_time=%s"
#反转数据表
data_times.reverse()
#记录有多少条新数据
index=0
for data_time in data_times:
    result=cursor.execute(select_new_sql,[data_time])
    if result==1:
        break
    index+=1
print(index)
trs.reverse()
for i in range(index):
    red_ball = '-'.join(trs[i].xpath('./td[@class="chartBall01"]/text()'))
    blue_ball=trs[i].xpath('./td[@class="chartBall02"]/text()')[0]
    print("第" + data_times[i] + "红球是：" + '\t' + red_ball + '\t'"蓝球：" + blue_ball)
    cursor.execute(sql,[data_times[i],red_ball,blue_ball])
    client.commit()

# for data_time,tr in zip(data_times,trs):
#     red_ball='-'.join(tr.xpath('./td[@class="chartBall01"]/text()'))
#     blue_ball=tr.xpath('./td[@class="chartBall02"]/text()')[0]
#     print("第"+data_time+"红球是："+'\t'+red_ball+'\t'"蓝球："+blue_ball)
#     cursor.execute(sql,[data_time,red_ball,blue_ball])
#     client.commit()
cursor.close()
client.close()
