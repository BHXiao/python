import re
import time
from multiprocessing import Pool
import multiprocessing
import requests


def get_html(url):
    # 代理IP
    proxies = {
        'https': '117.57.100.107:4213',
        # 'https': '111.179.73.109:3256'   # 不能复制：ctrl+ shift+i
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
    }
    response = requests.get(url, headers=headers, proxies=proxies)
    # print(response.cookies)
    # cookies = requests.utils.dict_from_cookiejar(response.cookies)
    # print(cookies)
    # response = requests.get(url, headers=headers, cookies=cookies)
    # response.encoding = 'utf-8'
    return response.text


def get_info(html):
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>'
                         r'.*?title="(.*?)"'
                         r'.*?star">(.*?)</p>'
                         r'.*?releasetime">(.*?)</p>', re.S)
    # pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?star">(.*?)</p>.*?</dd>', re.S)
    r = re.findall(pattern, html)
    # print(r)
    # 生成器
    for i in r:
        yield {
            "排名": i[0],
            "电影名": i[1],
            "主演": i[2].strip()[3:],  # 移除开头结尾的待定字符，默认是空格或tab 【切片的方式去掉‘主演：’】
            "上映时间": i[3].strip()[5:],
        }
    pass


def main(offset):
    if offset == 0:
        url = "https://maoyan.com/board/4"
        html = get_html(url)
        for i in get_info(html):
            print(i)
        # print(html)
    else:
        url = "https://maoyan.com/board/4?offset=" + str(offset)
        html = get_html(url)
        for i in get_info(html):
            print(i)


if __name__ == '__main__':
    # for num in range(10):
    #     # time.sleep(3)
    #     main(num * 10)
    pool = Pool()
    pool.map(main, [num*10 for num in range(10)])
