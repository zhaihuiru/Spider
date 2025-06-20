import urllib.request, urllib.error  # 制定url，获取网页数据
from calendar import month

from bs4 import BeautifulSoup  # 解析网页
import re  # 正则表达式
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite数据库操作
import os
import requests
import csv

month = ''
def main():
    # 网页url
    baseurl = "https://movie.douban.com/chart"
    # 1.网页爬取
    datalist = getData(baseurl)
    savepath = "北美票房榜.csv"
    # savepath = "北美票房榜.xlsx"
    # dbpath = "movie.db"

    # askURL(baseurl)
    # 3.保存数据
    saveData(datalist, savepath)
    # saveDataToDB(datalist, dbpath)


# 一周口碑榜日期
findDay = re.compile(r">(\d{1,2}月\d{1,2}日)\s*更新")  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片名称
findTitle = re.compile(r'>([^<]+)</a>')  # re.S让换行包含在字符中
# 影片票房
findMoney = re.compile(r'<span class="box_chart_num color-gray">(.*?)万</span>', re.S)

# 爬取网页
def getData(baseurl):
    datalist = []
    html = askURL(baseurl)
    # 2.逐一解析数据
    soup = BeautifulSoup(html, 'html.parser')  # 后面是解析器

     # 查找符合要求的字符串，形成列表

    for item in soup.find_all('span', class_="box_chart_num color-gray"):
        item = str(item)
        # 获取一周口碑榜日期
        time = re.findall(findDay, item)  # 通过正则表达式来查找指定的字符串
        if len(time) > 0:
            month = time[0]
            break
    number = 0

    for item in soup.find_all('li', class_="clearfix"):
        data=[]
        item = str(item)
        number = number + 1
        if number > 10:
            # 片名
            title = re.findall(findTitle, item)[0]
            title = re.sub("\n", '', title)
            title = re.sub("                            ", '', title)
            title = re.sub("                        ", '', title)
            data.append(title)

            # 票房
            movieMoney = re.findall(findMoney, item)[0]
            data.append(movieMoney)
        else:
            continue

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
        # print(html)
    except Exception as e:
        print("请求失败")
    return html


# 保存数据
def saveData(datalist, savepath):
    if os.path.exists(savepath):
        os.remove(savepath)

    # book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建workbook对象
    # sheet = book.add_sheet('豆瓣电影T250', cell_overwrite_ok=True)  # 创建工作表,可覆盖
    # col = ('电影名称', '电影票房')
    # for i in range(0, len(col)):
    #     sheet.write(0, i, col[i])
    # max_index = min(250, len(datalist))
    # for i in range(0, max_index):
    #     print("第%d条" % (i + 1))
    #     data = datalist[i]
    #     for j in range(0, len(col)):
    #         sheet.write(i + 1, j, data[j])
    # book.save(savepath)

    # 打开文件并写入数据
    with open(savepath, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # 写入表头
        writer.writerow(['电影名称', '电影票房'])
        # 写入数据
        for data in datalist:
            writer.writerow(data)
    print(f"数据已成功保存至 {savepath}")


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
            values(%s)''' % ",".join(data)
        # print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie (
            name varchar,
            money numeric
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
