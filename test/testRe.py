#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
from re import findall

#创建模式对象

# pat = re.compile("AA") #此处的AA，是正则表达式，用来验证其他的字符串
# m =  pat.search("AACBA") #search 是被校验的的内容，且只找一个

#没有模式对象
# m = re.search("AA","ACVAA") #前面的字符串是规则（模板），后面的字符串是被校验的对象
# print(m)

# print(re.findall("a","asdfga")) #前面的字符串是规则（模板），后面的字符串是被校验的对象

# print(re.findall("[a-g]","asdfga")) #前面的字符串是规则（模板），后面的字符串是被校验的对象

# print(re.findall("[a-g]+","asdfga")) #前面的字符串是规则（模板），后面的字符串是被校验的对象

print(re.sub("a","A","abcdcasd")) #找到a用A替换，在第三个字符串中查找"A"

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
# a = r"r\aabd-\'"
# print(a)





