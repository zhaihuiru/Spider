import sqlite3

#1. 连数据库
# conn = sqlite3.connect('test.db')  #打开或者创建数据库文件
#
# print("Opened database successfully")

# 2.建表
# conn = sqlite3.connect('test.db')  #打开或者创建数据库文件
# print("成功打开数据库")
# c = conn.cursor() #获取游标
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
#
# '''
# c.execute(sql) #执行sql语句
# conn.commit() #提交数据库操作
# conn.close() #关闭数据库连接
# print("成功建表")

#3.更改数据
# conn = sqlite3.connect('test.db')  #打开或者创建数据库文件
# print("成功打开数据库")
# c = conn.cursor() #获取游标
# sql = '''
#     insert into company values (1,'张三',32,'成都',8000)
#
# '''
# c.execute(sql) #执行sql语句
# conn.commit() #提交数据库操作
# conn.close() #关闭数据库连接
# print("更改数据完毕")

#4.查询数据
conn = sqlite3.connect('test.db')  #打开或者创建数据库文件
print("成功打开数据库")
c = conn.cursor() #获取游标
sql = '''
    select * from company
'''
cursor =  c.execute(sql) #执行sql语句
for row in cursor:
    print(row)
conn.close() #关闭数据库连接
print("查询数据完毕")

