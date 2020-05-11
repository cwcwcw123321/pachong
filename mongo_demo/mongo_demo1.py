import pymongo

#连接数据库
client=pymongo.MongoClient()

#选择实例
person=client.person
#选择集合
student=person.student
#操作数据
# result=student.find()

# for r in result:
#     print(r)
# print(result.next())
#过滤条件
# result=student.find({"country":"蜀国"})
# for r in result:
#     print(r)
#
# result=student.find().sort("age",1)
# for r in result:
#     print(r)

#分页
# result=student.find().limit(7).skip(6)
# for r in result:
#     print(r)

#查看文档个数
# result=student.estimated_document_count()
# print(result)

#增加数据
# data={"name":"黄月英","age":19}
# student.insert_one(data)

#删除数据
# student.delete_one(data)

#更新数据
data={"name":"黄月英"}
result=student.find_one(data)
print(result)
result["country"]="蜀国"
student.update_one(data,{"$set":result})