from logging import exception

import requests
from bs4 import BeautifulSoup

def get_html(url):
    head = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36 Edg/137.0.0.0"
    }
    html = ""
    try:
        response = requests.get(url, headers=head)
        html = response.text
        print(html)
    except exception as e:
        print("请求失败")
    return html

def main():
    url = "https://movie.douban.com/review/best/"
    get_html(url)

if __name__ == '__main__':
    main()