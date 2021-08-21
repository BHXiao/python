#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import time

import requests

import re


class Image(object):
    def __init__(self):
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 /n"
                       "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
                       }
        self.url = "https://image.baidu.com/search/acjson?"
        self.params = {
            "tn": "resultjson_com",
            "logid": "8241392047603912563",
            "ipn": "rj",
            "ct": 201326592,
            "is": "",
            "fp": "result",
            "queryWord": "微信表情包",
            "cl": "2",
            "lm": "-1",
            "ie": "utf-8",
            "oe": "utf-8",
            "adpicid": "",
            "st": "",
            "z": "",
            "ic": "",
            "hd": "",
            "latest": "",
            "copyright": "",
            "word": "微信表情包",
            "s": "",
            "se": "",
            "tab": "",
            "width": "",
            "height": "",
            "face": "",
            "istype": "",
            "qc": "",
            "nc": "",
            "fr": "",
            "expermode": "",
            "force": "",
            "pn": "",
            "rn": "30",
            "gsm": "",
            "time": ""

        }
        self.image_list = []
        self.image_name = []
        pass

    def get_image(self, num):
        n = 0
        # reg = "(.*?)<strong>微信表情包</strong>"  # 可能要括号.已确认
        reg = "([\u4e00-\u9fa5]{1,10})<strong>微信表情包</strong>"  # 可能要括号.已确认 这里提取的是前面几个中文
        # print(reg)
        for i in range(0, num):

            if i != 11:
                self.params['time'] = int(time.time() * 1000)  # 整秒
                self.params['pn'] = i * 30
                response = requests.get(self.url, headers=self.header, params=self.params)
                for j in range(0, len(response.json()['data'])-1):
                    self.image_list.append(response.json()['data'][j]['thumbURL'])
                    # print(re.findall(reg, response.json()['data'][j]['fromPageTitle']))
                    self.image_name.append(re.findall(reg, response.json()['data'][j]['fromPageTitle']))
                else:
                    continue
                    # print(self.image_list)

                    # print(n)
        f = open('./f.txt', 'w', encoding='utf-8')
        f.write(str(self.image_list))
        f = open('./name.txt', 'w')
        f.write(str(self.image_name))
        pass

    def save_image(self):
        n = 1
        # for i in self.image_list:
        #     if i == '':
        #         continue
        #     else:
        #         image1 = requests.get(url=i)
        #         with open('F:/微信文件/{}.jpg'.format(n), 'wb') as f:  # 非反斜杠
        #             f.write(image1.content)   # TypeError: 'bytes' object is not callable 报错  content（）
        #         n += 1
        for url, name in zip(self.image_list, self.image_name):
            if url == '':
                continue
            else:
                image1 = requests.get(url=url)
                if name == [] or name == ['']:
                    with open('F:/新建文件夹/{}.jpg'.format(n), 'wb') as f:  # 非反斜杠
                        f.write(image1.content)   # TypeError: 'bytes' object is not callable 报错  content（）
                    n += 1
                else:
                    # image1 = requests.get(url=url)
                    print(name[0])

                    # name2 = str(name)
                    # print(name2)
                    # name3 = ''
                    # for i in name2:
                    #     while i not in ['/', '\\', ':', '*', '\'', '\"', '|', '?', '[', ']', '<', '>', '']:
                    #         name3 += i
                    #         i = ''  # 给个退出的条件
                    #         # return   # 整个退出
                    #         # print(name3)
                    #         # continue  # 回到上一步 判断  这里回到了 while
                    #
                    #     # # if i == 'r[/ \\ : * \" < > | ？\']'
                    #     # if i == '[' or i == ']' or i == '\'' or i == ',' or i == '\"' or i == '/' or i == '':
                    #     #     name3 += i
                    #     # else:
                    #     #     continue
                    # print(name3)
                    pass
                    # reg = re.findall("[\u4e00-\u9fa5]{1,10}", name2)
                    # name1 = re.findall(reg, name2)
                    # print(reg)
                    with open('F:/test/' + name[0] + '.jpg', 'wb') as f:  # 非反斜杠
                        f.write(image1.content)
        pass


if __name__ == '__main__':
    image = Image()
    image.get_image(1)
    image.save_image()

