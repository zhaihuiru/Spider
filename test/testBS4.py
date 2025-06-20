'''
BS4将负责的HTML文件转换为一个复杂的树形结构，每个节点都是python文件，所有对象可以归纳为4种：
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''

from bs4 import BeautifulSoup
import re

file = open('./baidu.html','rb')
html = file.read()
bs = BeautifulSoup(html, 'html.parser')  #确定解析器，形成解析树

#1.Tag标签及其内容：拿到第一个
# print(bs.title)
# print(bs.a) #拿到第一个标签及其所有
# print(bs.head)

#2.NavigableString标签里面的内容（字符串）
# print(bs.title.string)  #只要title里面的内容
# print(bs.a.attrs) #获取标签的属性字典

#3.BeautifulSoup 表示整个文档
# print(bs.name)
# print(type(bs))
# print(bs)

#4.Comment输出注释，但是不会包含注释符号
# print(bs.a.string)




#------------------------------------------------------------------


#文档遍历
# print(bs.head.contents)
# print(bs.head.contents[1])


#文档搜索
#(1)find_all()
#查找与字符串完全一样的
# t_list = bs.find_all("a")
# print(t_list)

#正则表达式搜索：使用search()方式来匹配内容,只要包含就搜索出来
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

#方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exist(tag):
#     return tag.has_attr('name')
#
# t_list = bs.find_all(name_is_exist)
# print(t_list)

#(2)kwargs 指定参数
# t_list = bs.find_all(id="head")
# for t in t_list:
#     print(t)

# t_list = bs.find_all(class_=True)
# for t in t_list:
#     print(t)

#(3)text参数
# t_list = bs.find_all(text="地图")
# t_list = bs.find_all(text=["地图","贴吧"])
# t_list = bs.find_all(text=re.compile("\d"))  #应用正则表达式来查找特定包含文本的内容（标签里的字符串）
# for t in t_list:
#     print(t)


#(4)limit参数
# t_list = bs.find_all('a',limit=3)
# for t in t_list:
#     print(t)

#css选择器
# print(bs.select('title')) #通过标签来查找

# t_list = bs.select(".mnav") #通过类名来查找

# t_list = bs.select("#ul") #通过id来查找

# t_list = bs.select("a[class = 'text-color']") #通过属性查找

# t_list = bs.select("head > title") #通过子标签查找
# for t in t_list:
#     print(t)






