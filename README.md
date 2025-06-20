# 🕸️ Spider 网络爬虫项目

<div align="center">
  <img src="word.jpg" alt="词云示例" width="400"/>
</div>
<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-green.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


</div>



## 📖 项目介绍

Spider 是一个多功能网络爬虫项目，主要用于爬取不同网站的信息并进行数据处理和分析。目前支持爬取豆瓣电影、豆瓣图书、中国天气网等多个网站的数据，并提供数据存储、分析和可视化功能。

## ✨ 功能特性

- 🎬 **豆瓣电影Top250爬虫**：爬取豆瓣电影Top250的电影信息
- 📚 **豆瓣图书爬虫**：按标签爬取豆瓣图书信息
- 🌤️ **中国天气网爬虫**：爬取全国各地区天气信息
- 💾 **多种数据存储**：支持Excel、CSV、SQLite等多种数据存储格式
- 📊 **数据可视化**：使用词云、图表等方式展示数据分析结果
- 🔄 **网页解析工具**：集成BeautifulSoup、正则表达式等网页解析工具

## 🛠️ 技术栈

- **Python**：主要编程语言
- **BeautifulSoup**：HTML解析库
- **Requests**：HTTP请求库
- **正则表达式**：数据提取
- **Matplotlib**：数据可视化
- **WordCloud**：词云生成
- **xlwt**：Excel文件操作

## 📥 安装说明

1. 克隆本仓库到本地
```bash
git clone https://github.com/zhaihuiru/Spider.git
cd Spider
```

2. 安装依赖库
```bash
pip install -r requirements.txt
```

## 🚀 使用方法

### 豆瓣电影Top250爬虫

```bash
python spider.py
```

该脚本会爬取豆瓣电影Top250的电影信息，并存储到Excel、CSV或SQLite数据库中。

### 豆瓣图书爬虫

```bash
python douban.py
```

该脚本支持按标签爬取豆瓣图书信息，可以在脚本中修改`book_tag_lists`变量来设置需要爬取的图书标签。

### 中国天气网爬虫

```bash
python ChinaWeather.py
```

该脚本会爬取中国天气网上全国各地区的天气信息，并进行数据分析。

### 词云生成

```bash
python testCloud.py
```

该脚本会从SQLite数据库中读取电影简介，生成词云图片。

## 📊 示例结果

- 电影数据会保存在`影片.xls`、`影片1.csv`或`movie.db`中
- 图书数据会保存为Excel格式
- 词云结果会保存为`word.jpg`

## 📄 开源许可证
本项目基于 MIT 开源许可发布。商业使用或衍生作品需要获得作者授权。