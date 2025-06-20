import urllib.request, urllib.error  # 制定url，获取网页数据
from bs4 import BeautifulSoup  # 解析网页
import re  # 正则表达式
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite数据库操作
import os
import requests


def main():
    # 网页url
    baseurl = "https://movie.douban.com/top250?start="
    # baseurl = "https://www.weather.com.cn/weather40d/101010100.shtml"
    # baseurl = "https://www.douban.com/"
    # baseurl = "https://tophub.today/"
    # baseurl = "https: // movie.douban.com / explore"
    # 1.网页爬取
    # datalist = getData(baseurl)
    # savepath = "影片1.csv"
    # dbpath = "movie.db"

    askURL(baseurl)
    # 3.保存数据
    # saveData(datalist, savepath)
    # saveDataToDB(datalist, dbpath)


# 影片详情链接
findList = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findReading = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span>(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p>(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面的信息10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')  # 后面是解析器
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)
            data = []  # 一部电影的所有信息
            item = str(item)
            # 获取影片详情的链接
            link = re.findall(findList, item)[0]  # 通过正则表达式来查找指定的字符串
            data.append(link)  # 添加链接

            imgsrc = re.findall(findImgSrc, item)[0]
            data.append(imgsrc)  # 添加图片

            title = re.findall(findTitle, item)  # 片名可能不止一个
            if (len(title) == 2):
                ctitle = title[0]  # 添加中文名
                data.append(ctitle)
                otitle = title[1].replace("/", "")  # 添加外国名
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')  # 外国名留空

            rating = re.findall(findReading, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加人数

            inq = re.findall(findInq, item)
            if len(inq) > 1:
                inq = inq[1].replace("。", "")
                data.append(inq)  # 添加概述
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            # bd = re.sub("\xa0",'',bd)
            bd = re.sub("/", '', bd)  # 去掉/
            bd = re.sub(' ', '', bd)
            bd = re.sub('\n', '', bd)

            data.append(bd)

            datalist.append(data)  # 把处理好的信息放入datalist中

        print(datalist)

    return datalist


# 得到指定一个url的网页内容
def askURL(url):
    # 模拟浏览器头部信息
    head = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36 Edg/137.0.0.0"
    }
    html = ""
    try:
        response = requests.get(url, headers=head)
        html = response.text
        print(html)
    except Exception as e:
        print("请求失败")
    return html


# 保存数据
def saveData(datalist, savepath):
    if os.path.exists(savepath):
        os.remove(savepath)

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影T250', cell_overwrite_ok=True)  # 创建工作表,可覆盖
    col = ('电影详情链接', '电影图片链接', '影片中文名', '影片外国名', '评分', '评价数量', '概况', '详情信息')
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    max_index = min(250, len(datalist))
    for i in range(0, max_index):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, len(col)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


# def saveDataToDB(datalist,dbpath):
#
#     conn = sqlite3.connect(dbpath)
#     cursor = conn.cursor()
#
#     for data in datalist:
#         for index in range(len(data)):
#             if index == 4 or index == 5:
#                 continue
#             data[index] = '"'+data[index]+'"'
#         sql = '''
#             insert into movie values (%s)
#         '''%','.join(data)
#         cursor.execute(sql)
#         # print(sql)
#         conn.commit()
#     cursor.close()
#     conn.close()

def saveDataToDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie (
            info_link, pic_url, cname, ename, score, rated, introduction, info)
            values(%s)'''%",".join(data)
        # print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie (
            info_link text,
            pic_url text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        )

    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    # init_db("movietest.db")
    print("爬取完毕")
