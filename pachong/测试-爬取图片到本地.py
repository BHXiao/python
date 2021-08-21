#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import requests

image_url = 'https://p2.ssl.qhimgs1.com/sdr/400__/t017ef2d5a1aad15d62.jpg'
response = requests.get(image_url)
print(response.content)   # print(r.content.decode()) 图片格是与文本不同
with open('panda.jpg', 'wb') as f:  # w写入  b 二进制  文件不存在就会创建
    f.write(response.content)

