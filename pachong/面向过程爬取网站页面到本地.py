#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://tieba.baidu.com/f?kw=太子&pn=50
"""
import requests
# 字典
headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /n'
        'Chrome/90.0.4430.93 Safari/537.36'
    }
url = 'https://tieba.baidu.com/f?kw={}&pn={}'
text = input("请输入要贴吧的名字：")
url_list = [url.format(text, i * 50) for i in range(3)]  # 前3页
print(url_list)
# params = {'wd': text, 'pn':}  #########
#  用format将text中的内容转入大括号
for item_url in url_list:
    response = requests.get(item_url, headers=headers)
    # print(response.content)   # print(r.content.decode()) 图片格是与文本不同
    # file_name = "贴吧_" + text + '第｛｝页', format(url_list.index(item_url) + 1) + ".html"   format前的符号错了,导致
    # open内报红说file_name类型错误
    # file_name = "贴吧_" + text + '第｛｝页'.format(url_list.index(item_url) + 1) + ".html"   错误点：｛｝为中文符号
    file_name = "贴吧_" + text + '第{}页'.format(url_list.index(item_url) + 1) + ".html"
    with open(file_name, 'w', encoding='utf-8') as f:  # w写入  b 二进制  文件不存在就会创建  windows下申明格式 utf-8
        f.write(response.content.decode())
