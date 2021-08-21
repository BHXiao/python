#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import hashlib
import json

import requests


class Tieba_spider(object):  # object 默认继承  可不写

    def __init__(self, text):
        self.text = text
        # 加  upbroad: function(e) {
        # 密               p.a.parse(e);
        # 方                var t = c()("6key_cibaifanyicjbysdlove1").toString().substring(0, 16);
        # 法               return g("/index.php?c=trans&m=copyevent&client=6&auth_user=key_ciba&sign=".concat(t), {
        #                     baseURL: "//ifanyi.iciba.com",
        # 初始翻译路径
        sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1" + self.text).encode('utf-8')).hexdigest())[0:16]

        self.url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=' + sign
        # self.url = url + sign
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /n'
            'Chrome/90.0.4430.93 Safari/537.36'
        }
        self.data = self.get_data()

    def get_date_formurl(self,):
        """从服务器获取数据"""
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content.decode()
        # pass

    def get_data(self):
        """获取请求体数据"""
        data = {
            'from': 'auto',
            'to': 'auto',
            'q': self.text
        }
        return data
        pass

    def parse_data(self, json_str):
        # {"status":1,"content":{"from":"en","to":"zh","out":"\u4f60\u597d","vendor":"ciba","err_no":0,"ttsLan":8}}
        dict_data = json.loads(json_str)  # 将json 数据整理成字典
        result = dict_data["content"]["out"]
        print('{} 翻译后的结果是：{}'.format(self.text, result))
        pass

    def run(self):
        # 1.获取URL请求头
        # 2.发起请求获取响应该数据
        json_str = self.get_date_formurl()
        # 3.提取数据
        self.parse_data(json_str)
        pass


if __name__ == '__main__':

    text = input("请输入要翻译的内容：")
    spider = Tieba_spider(text)
    spider.run()  #  晕，开始没给括号  找了1个小时错
