#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import requests
# 字典
headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
url = 'https://www.baidu.com/s?wd={}'
text = input("请输入要搜索的内容：")
#  用format将text中的内容转入大括号
response = requests.get(url.format(text), headers=headers)
print(response.content.decode())   # print(r.content.decode()) 图片格是与文本不同
with open('panda.html', 'w', encoding='utf-8') as f:  # w写入  b 二进制  文件不存在就会创建  windows下申明格式 utf-8
    f.write(response.content.decode())

