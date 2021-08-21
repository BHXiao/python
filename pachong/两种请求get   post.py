#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import requests

# get 一步到位   本地缓存  不安全  常用
#
# post   先发送请求头   再发请求休   本地不缓存  安全  账号密码之类  大文本

response_get = requests.get(url, headers=headers)
response_post = requests.post(url, headers=headers, data=data)   #  data  请求体  字典
