#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import requests


class Tieba_spider(object):  # object 默认继承  可不写

    def __init__(self, text):
        self.num = input('需要下载前几页:')
        self.num1 = eval(self.num)  # 改为int
        self.text = text
        self.url = 'https://tieba.baidu.com/f?kw=' + self.text + '&pn={}'
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /n'
            'Chrome/90.0.4430.93 Safari/537.36'
        }

    def get_url_list(self):
        """生成URL列表"""
        # num = input('需要下载前几页:')
        # num1 = eval(num)  # 改为int
        url_list = [self.url.format(i * 50) for i in range(self.num1)]
        return url_list
        # pass

    def get_date_formurl(self, item_url):
        """从服务器获取数据"""
        response = requests.get(item_url, headers=self.headers)
        return response.content.decode()
        # pass

    def save_html(self, html_str, num):
        """保存到本地"""
        file_name = "贴吧_" + self.text + '第{}页'.format(num) + ".html"
        with open(file_name, 'w', encoding='utf-8') as f:  # w写入  b 二进制  文件不存在就会创建  windows下申明格式 utf-8
            f.write(html_str)

        # pass

    def run(self):
        url_list = self.get_url_list()
        for item_url in url_list:
            html_str = self.get_date_formurl(item_url)
            # 保存
            self.save_html(html_str, url_list.index(item_url) + 1)
        # pass


if __name__ == '__main__':

    text = input("请输入要贴吧的名字：")
    spider = Tieba_spider(text)
    spider.run()  #  晕，开始没给括号  找了1个小时错





#
# # 字典
# headers = {
#         # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /n'
#         'Chrome/90.0.4430.93 Safari/537.36'
#     }
# url = 'https://tieba.baidu.com/f?kw={}&pn={}'
# text = input("请输入要贴吧的名字：")
# url_list = [url.format(text, i * 50) for i in range(3)]  # 前3页
# print(url_list)
# # params = {'wd': text, 'pn':}  #########
# #  用format将text中的内容转入大括号
# for item_url in url_list:
#     response = requests.get(item_url, headers=headers)
#     # print(response.content)   # print(r.content.decode()) 图片格是与文本不同
#     # file_name = "贴吧_" + text + '第｛｝页', format(url_list.index(item_url) + 1) + ".html"   format前的符号错了,导致
#     # open内报红说file_name类型错误
#     # file_name = "贴吧_" + text + '第｛｝页'.format(url_list.index(item_url) + 1) + ".html"   错误点：｛｝为中文符号
#     file_name = "贴吧_" + text + '第{}页'.format(url_list.index(item_url) + 1) + ".html"
#     with open(file_name, 'w', encoding='utf-8') as f:  # w写入  b 二进制  文件不存在就会创建  windows下申明格式 utf-8
#         f.write(response.content.decode())
