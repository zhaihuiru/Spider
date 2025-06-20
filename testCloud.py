import jieba #分词
from matplotlib import pyplot as plt #绘图，数据可视化
from wordcloud import WordCloud #词云
from PIL import Image #图片处理
import numpy as np #矩阵运算
import sqlite3

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from movie'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
# print(text)
cur.close()
con.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
# print(len(string))

#绘图
img = Image.open(r'词云背景图.jpg')
img_array = np.array(img) #将图片变成为数组
wc = WordCloud(
    background_color='white',
    mask = img_array,
    font_path = 'msyh.ttc',  #字体在windows的Fonts下面
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #不显示坐标轴
# plt.show()  #显示生成的词云图片

#输出词云图片到文件
plt.savefig('word.jpg',dpi=500)
