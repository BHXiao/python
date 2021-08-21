#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import requests

r = requests.get('http://www.baidu.com')
print(r)
# <Response [200]>
print(r.status_code)
# 200
r.encoding = 'utf-8'   # 申明格式，解决乱码   gbk  utf-8
print(r.text)
# 乱码
# <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8>
# <title>百度一下，你就知道</title></head> <body link=#0000cc>
print(r.content.decode())   # decode默认以UTF-8格式输出
print(r.request.headers)    # 确认下请求头信息

